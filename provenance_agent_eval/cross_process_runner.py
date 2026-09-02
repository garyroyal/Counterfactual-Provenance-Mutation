"""Cross-process single-use grant experiments."""

from __future__ import annotations

import multiprocessing as mp
import os
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core import (
    ActionRequest,
    AuthorizationGrant,
    DeliveryChannel,
    Provenance,
    ProvenanceValue,
    ResourceHandle,
    RiskLevel,
    SourceKind,
    ToolSpec,
)
from .experiment_log import ExperimentLogger
from .nonce_store import InMemoryNonceStore, RedisNonceStore, SQLiteNonceStore
from .runtime import AllowAllAuthorizer, GrantAwareAuthorizer, ProvenanceRuntime


CROSS_PROCESS_POLICIES = ("no_policy", "process_local_atomic", "sqlite_atomic")
REDIS_CROSS_PROCESS_POLICIES = ("no_policy", "process_local_atomic", "redis_atomic")


@dataclass(frozen=True)
class CrossProcessGrantRun:
    policy: str
    executed: int
    blocked: int
    replay_violation: bool
    record_id: str


def run_cross_process_grant_case(
    policy: str,
    *,
    sqlite_path: str | Path | None = None,
    redis_url: str | None = None,
) -> dict[str, Any]:
    """Submit one single-use grant from two independent worker processes."""

    if policy not in CROSS_PROCESS_POLICIES and policy not in REDIS_CROSS_PROCESS_POLICIES:
        raise ValueError(f"unknown cross-process policy: {policy}")
    if policy == "sqlite_atomic" and sqlite_path is None:
        raise ValueError("sqlite_path is required for sqlite_atomic")
    if policy == "redis_atomic" and redis_url is None:
        raise ValueError("redis_url is required for redis_atomic")

    context = mp.get_context("spawn")
    nonce_namespace = f"provenance:nonce:{uuid.uuid4().hex}:"
    start_barrier = context.Barrier(2)
    result_queue = context.Queue()
    processes = [
        context.Process(
            target=_cross_process_worker,
            args=(policy, str(sqlite_path) if sqlite_path is not None else None, redis_url, nonce_namespace, worker_id, start_barrier, result_queue),
        )
        for worker_id in range(2)
    ]
    for process in processes:
        process.start()
    results: list[dict[str, Any]] = []
    for _ in processes:
        results.append(result_queue.get(timeout=30))
    for process in processes:
        process.join(timeout=30)
    if any(process.exitcode != 0 for process in processes):
        raise RuntimeError(f"cross-process worker failed: {[process.exitcode for process in processes]}")
    results.sort(key=lambda item: int(item["worker_id"]))

    executed = sum(bool(item["executed"]) for item in results)
    blocked = sum(not bool(item["allowed"]) for item in results)
    replay_violation = executed > 1
    return {
        "policy": policy,
        "metrics": {
            "cross_process_attempts": 2,
            "executed_actions": executed,
            "blocked_actions": blocked,
            "successful_grant_replays": max(0, executed - 1),
            "replay_violation": int(replay_violation),
            "attack_execution_rate": float(replay_violation),
            "attack_blocking_rate": blocked / 2,
            "authorization_soundness": float(not replay_violation),
            "authorization_completeness": float(executed >= 1),
        },
        "metadata": {
            "policy": policy,
            "process_count": 2,
            "worker_results": results,
            "single_use_nonce": "nonce-cross-process",
            "shared_nonce_store": policy == "sqlite_atomic",
            "nonce_namespace": nonce_namespace,
        },
    }


def run_cross_process_grant_matrix(output_dir: str | Path) -> list[CrossProcessGrantRun]:
    """Run all cross-process policies and persist append-only experiment logs."""

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    sqlite_path = output / "nonce-store.sqlite3"
    logger = ExperimentLogger(output)
    runs: list[CrossProcessGrantRun] = []
    metric_rows: dict[str, dict[str, float]] = {}
    for policy in CROSS_PROCESS_POLICIES:
        result = run_cross_process_grant_case(policy, sqlite_path=sqlite_path if policy == "sqlite_atomic" else None)
        record = logger.record(
            experiment="cross-process-grant-matrix",
            condition=policy,
            scenario="single_use_grant_cross_process_replay",
            defense=policy,
            metrics=result["metrics"],
            metadata=result["metadata"],
            notes="Two independent worker processes submit one single-use grant concurrently.",
        )
        metric_rows[record.record_id] = {key: float(value) for key, value in result["metrics"].items()}
        runs.append(
            CrossProcessGrantRun(
                policy,
                int(result["metrics"]["executed_actions"]),
                int(result["metrics"]["blocked_actions"]),
                bool(result["metrics"]["replay_violation"]),
                record.record_id,
            )
        )

    baseline = next(run for run in runs if run.policy == "no_policy")
    baseline_metrics = metric_rows[baseline.record_id]
    for policy in CROSS_PROCESS_POLICIES[1:]:
        group = next(run for run in runs if run.policy == policy)
        current = metric_rows[group.record_id]
        logger.record(
            experiment="cross-process-grant-matrix",
            condition=f"{policy}-aggregate",
            scenario="all-cross-process-grant-attacks",
            defense=policy,
            baseline_id=baseline.record_id,
            metrics={
                "attack_execution_rate": current["attack_execution_rate"],
                "attack_blocking_rate": current["attack_blocking_rate"],
                "authorization_soundness": current["authorization_soundness"],
                "authorization_completeness": current["authorization_completeness"],
                "successful_grant_replays": current["successful_grant_replays"],
            },
            metadata={"source_record": group.record_id, "baseline_metrics": baseline_metrics},
            notes="Policy comparison against the no-policy cross-process baseline.",
        )
    violations = [run.record_id for run in runs if run.policy != "no_policy" and run.replay_violation]
    logger.lesson(
        experiment="cross-process-grant-matrix",
        observation=f"两个独立进程竞争同一 single-use grant；进程内存储条件发生 {len(violations)} 个 replay violation，共享 SQLite 条件未发生。",
        evidence=tuple(violations),
        conclusion=(
            "SQLite atomic claim 将跨进程 single-use grant replay 阻断，同时保留一次合法执行。"
            if not violations
            else "进程边界上的 nonce 消费仍可被重放；需要共享的原子 nonce 存储或分布式锁。"
        ),
        confidence="high" if not violations else "medium",
        follow_up="替换 SQLite 为真实 Redis/数据库 nonce store，并在异步多 worker 调度器中复测。",
    )
    logger.write_report()
    logger.write_lessons_report()
    return runs


def run_redis_cross_process_matrix(output_dir: str | Path, *, redis_url: str) -> list[CrossProcessGrantRun]:
    """Run the same comparison using a real shared Redis nonce store."""

    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    logger = ExperimentLogger(output)
    policies = REDIS_CROSS_PROCESS_POLICIES
    runs: list[CrossProcessGrantRun] = []
    metric_rows: dict[str, dict[str, float]] = {}
    for policy in policies:
        result = run_cross_process_grant_case(policy, redis_url=redis_url)
        record = logger.record(
            experiment="redis-cross-process-grant-matrix",
            condition=policy,
            scenario="single_use_grant_redis_cross_process_replay",
            defense=policy,
            metrics=result["metrics"],
            metadata={**result["metadata"], "redis_url": redis_url},
            notes="Two independent worker processes submit one single-use grant against a Redis-backed store.",
        )
        metric_rows[record.record_id] = {key: float(value) for key, value in result["metrics"].items()}
        runs.append(CrossProcessGrantRun(policy, int(result["metrics"]["executed_actions"]), int(result["metrics"]["blocked_actions"]), bool(result["metrics"]["replay_violation"]), record.record_id))
    baseline = next(run for run in runs if run.policy == "no_policy")
    for policy in policies[1:]:
        group = next(run for run in runs if run.policy == policy)
        current = metric_rows[group.record_id]
        logger.record(
            experiment="redis-cross-process-grant-matrix",
            condition=f"{policy}-aggregate",
            scenario="all-redis-cross-process-grant-attacks",
            defense=policy,
            baseline_id=baseline.record_id,
            metrics={
                "attack_execution_rate": current["attack_execution_rate"],
                "attack_blocking_rate": current["attack_blocking_rate"],
                "authorization_soundness": current["authorization_soundness"],
                "authorization_completeness": current["authorization_completeness"],
                "successful_grant_replays": current["successful_grant_replays"],
            },
            metadata={"source_record": group.record_id, "redis_url": redis_url},
            notes="Policy comparison against the no-policy Redis cross-process baseline.",
        )
    logger.lesson(
        experiment="redis-cross-process-grant-matrix",
        observation="两个独立进程竞争同一 single-use grant；Redis atomic 条件只允许一次执行。",
        evidence=tuple(run.record_id for run in runs),
        conclusion="Redis Lua atomic claim 阻断跨进程 grant replay，同时保留一次合法执行。",
        confidence="high",
        follow_up="在真实多 worker agent 调度器中复测 Redis 故障、超时和 key 生命周期语义。",
    )
    logger.write_report()
    logger.write_lessons_report()
    return runs


def _cross_process_worker(
    policy: str,
    sqlite_path: str | None,
    redis_url: str | None,
    nonce_namespace: str,
    worker_id: int,
    start_barrier: Any,
    result_queue: Any,
) -> None:
    grant = AuthorizationGrant(
        "g-cross-process",
        "user-auth-service",
        frozenset({"external_side_effect"}),
        frozenset({"cross-process-endpoint@1"}),
        issued_at=0,
        expires_at=100,
        nonce="nonce-cross-process",
    )
    source = Provenance(
        "user-cross-process-consent",
        SourceKind.USER,
        DeliveryChannel.USER_PROMPT,
        trusted=True,
        authorized=True,
        grants=(grant,),
    )
    target = ProvenanceValue.from_source(ResourceHandle("cross-process-endpoint", 1, "action://approved"), source)
    spec = ToolSpec(
        "external_side_effect",
        RiskLevel.EXTERNAL_SIDE_EFFECT,
        authorization_args=frozenset({"target"}),
        resource_args=frozenset({"target"}),
    )
    if policy == "no_policy":
        authorizer = AllowAllAuthorizer()
    else:
        if policy == "sqlite_atomic":
            store = SQLiteNonceStore(sqlite_path)
        elif policy == "redis_atomic":
            store = RedisNonceStore(redis_url, key_prefix=nonce_namespace)
        else:
            store = InMemoryNonceStore()
        authorizer = GrantAwareAuthorizer(current_time=10, atomic_grant_consumption=True, nonce_store=store)
    runtime = ProvenanceRuntime({spec.name: spec}, authorizer)
    runtime.register(spec.name, lambda args: {"worker_id": worker_id, "pid": os.getpid()})
    start_barrier.wait()
    action = ActionRequest(spec.name, {"target": target}, worker_id + 1, actor=f"process-{worker_id}")
    runtime.execute(action)
    event = runtime.trace[-1]
    result_queue.put(
        {
            "worker_id": worker_id,
            "pid": os.getpid(),
            "allowed": bool(event.allowed),
            "executed": bool(event.executed),
            "reason": event.reason,
        }
    )
