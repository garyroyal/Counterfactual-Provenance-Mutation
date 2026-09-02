"""Threaded grant-consumption experiments for replay-race detection."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from threading import Barrier
from typing import Any

from .core import ActionRequest, AuthorizationGrant, DeliveryChannel, Provenance, ProvenanceValue, ResourceHandle, RiskLevel, SourceKind, ToolSpec
from .experiment_log import ExperimentLogger
from .runtime import AllowAllAuthorizer, GrantAwareAuthorizer, ProvenanceRuntime


CONCURRENT_POLICIES = ("no_policy", "grant_aware_racey", "grant_aware_atomic")


@dataclass(frozen=True)
class ConcurrentGrantRun:
    policy: str
    executed: int
    blocked: int
    replay_violation: bool
    record_id: str


def run_concurrent_grant_case(policy: str) -> dict[str, Any]:
    """Submit two simultaneous uses of one single-use grant."""

    if policy not in CONCURRENT_POLICIES:
        raise ValueError(f"unknown concurrent policy: {policy}")
    grant = AuthorizationGrant(
        "g-concurrent",
        "user-auth-service",
        frozenset({"external_side_effect"}),
        frozenset({"batch-endpoint@1"}),
        issued_at=0,
        expires_at=100,
        nonce="nonce-concurrent",
    )
    source = Provenance(
        "user-concurrent-consent",
        SourceKind.USER,
        DeliveryChannel.USER_PROMPT,
        trusted=True,
        authorized=True,
        grants=(grant,),
    )
    target = ProvenanceValue.from_source(ResourceHandle("batch-endpoint", 1, "batch://approved"), source)
    spec = ToolSpec(
        "external_side_effect",
        RiskLevel.EXTERNAL_SIDE_EFFECT,
        authorization_args=frozenset({"target"}),
        resource_args=frozenset({"target"}),
    )
    barrier = Barrier(2) if policy == "grant_aware_racey" else None
    authorizer = (
        AllowAllAuthorizer()
        if policy == "no_policy"
        else GrantAwareAuthorizer(
            current_time=10,
            atomic_grant_consumption=policy == "grant_aware_atomic",
            grant_barrier=barrier,
        )
    )
    runtime = ProvenanceRuntime({spec.name: spec}, authorizer)
    executed_payloads: list[dict[str, Any]] = []
    runtime.register(spec.name, lambda args: executed_payloads.append({"target": _label(args["target"])}))

    actions = (
        ActionRequest(spec.name, {"target": target}, 1, actor="worker-1"),
        ActionRequest(spec.name, {"target": target}, 2, actor="worker-2"),
    )
    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(runtime.execute, action) for action in actions]
        for future in futures:
            future.result()

    executed = sum(event.executed for event in runtime.trace)
    blocked = sum(event.allowed is False and not event.executed for event in runtime.trace)
    replay_violation = executed > 1
    return {
        "policy": policy,
        "metrics": {
            "concurrent_attempts": 2,
            "executed_actions": executed,
            "blocked_actions": blocked,
            "successful_grant_replays": max(0, executed - 1),
            "replay_violation": int(replay_violation),
            "attack_execution_rate": float(replay_violation),
            "attack_blocking_rate": blocked / 2,
            "authorization_soundness": float(not replay_violation),
            "authorization_completeness": float(executed >= 1),
            "partial_execution": int(executed == 1),
        },
        "metadata": {
            "policy": policy,
            "thread_count": 2,
            "trace": [
                {
                    "step": event.step,
                    "actor": actions[event.step - 1].actor,
                    "allowed": event.allowed,
                    "executed": event.executed,
                    "reason": event.reason,
                }
                for event in runtime.trace
            ],
            "executed_payloads": executed_payloads,
            "single_use_nonce": grant.nonce,
        },
    }


def run_concurrent_grant_matrix(output_dir: str | Path) -> list[ConcurrentGrantRun]:
    logger = ExperimentLogger(output_dir)
    runs: list[ConcurrentGrantRun] = []
    metric_rows: dict[str, dict[str, float]] = {}
    for policy in CONCURRENT_POLICIES:
        result = run_concurrent_grant_case(policy)
        record = logger.record(
            experiment="concurrent-grant-matrix",
            condition=policy,
            scenario="single_use_grant_concurrent_replay",
            defense=policy,
            metrics=result["metrics"],
            metadata=result["metadata"],
            notes="Two worker threads submit one single-use grant concurrently.",
        )
        metric_rows[record.record_id] = {key: float(value) for key, value in result["metrics"].items()}
        runs.append(ConcurrentGrantRun(policy, int(result["metrics"]["executed_actions"]), int(result["metrics"]["blocked_actions"]), bool(result["metrics"]["replay_violation"]), record.record_id))

    baseline = next(run for run in runs if run.policy == "no_policy")
    baseline_metrics = metric_rows[baseline.record_id]
    for policy in CONCURRENT_POLICIES[1:]:
        group = next(run for run in runs if run.policy == policy)
        current = metric_rows[group.record_id]
        logger.record(
            experiment="concurrent-grant-matrix",
            condition=f"{policy}-aggregate",
            scenario="all-concurrent-grant-attacks",
            defense=policy,
            baseline_id=baseline.record_id,
            metrics={
                "attack_execution_rate": current["attack_execution_rate"],
                "attack_blocking_rate": current["attack_blocking_rate"],
                "authorization_soundness": current["authorization_soundness"],
                "authorization_completeness": current["authorization_completeness"],
                "successful_grant_replays": current["successful_grant_replays"],
                "partial_execution": current["partial_execution"],
            },
            metadata={"source_record": group.record_id, "baseline_metrics": baseline_metrics},
            notes="Policy comparison against the no-policy concurrent baseline.",
        )
    violations = [run.record_id for run in runs if run.policy != "no_policy" and run.replay_violation]
    logger.lesson(
        experiment="concurrent-grant-matrix",
        observation=f"两个并发 worker 竞争同一 single-use grant；受保护条件仍发生 {len(violations)} 个 replay violation。",
        evidence=tuple(violations),
        conclusion=(
            "原子 grant consumption 阻断并发 replay，同时保留一次合法执行。"
            if not violations
            else "非原子 grant consumption 允许并发 replay；需要将 nonce 检查与消费置于同一临界区。"
        ),
        confidence="high" if not violations else "medium",
        follow_up="把原子消费接入真实异步工具调度器，并测试跨进程锁或持久化 nonce store。",
    )
    logger.write_report()
    logger.write_lessons_report()
    return runs


def _label(value: Any) -> Any:
    if isinstance(value, ProvenanceValue):
        return _label(value.value)
    if isinstance(value, ResourceHandle):
        return {"resource_id": value.resource_id, "version": value.version, "value": value.value}
    return value

