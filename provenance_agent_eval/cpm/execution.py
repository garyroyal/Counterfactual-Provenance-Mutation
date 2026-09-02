"""Execution-stage mutation operators: check-to-use drift and semantic replay.

The graph operators corrupt *evidence*.  These two operators corrupt the
*execution closure* around an already-authorised action, so that invariants
I4 (no duplicate effect) and I5 (check-to-use consistency) become degradation
curves instead of single demonstrations:

* ``stale_version``  - with probability p per action, the versioned resource
  the grant was checked against is swapped for a newer version carrying an
  attacker value between authorization and use (TOCTOU).
* ``semantic_replay`` - with probability p per retry slot, the runtime
  re-proposes an already-executed action with a *fresh* single-use grant
  (retry / replan / crash-recovery reissuance, the failure CapLease and
  ACRFence describe).  Identifier-local nonce consumption cannot see it.

Mechanisms are execution-closure abstractions built from the existing runtime:
``grant_single_use`` (scoped, time-bounded, single-use nonce; no post-check),
``grant_revalidated`` (adds post-authorization revalidation of effective
arguments) and ``intent_ledger`` (adds a durable ledger keyed by canonical
action so a fresh nonce for the same intent is refused).  Cells and curves are
written in the same schema as :mod:`.degradation`, so :mod:`.laws` and
:mod:`.plots` apply unchanged.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import random
from collections import defaultdict
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Iterable, Sequence

from ..core import (
    ActionRequest,
    AuthorizationDecision,
    AuthorizationGrant,
    DeliveryChannel,
    Provenance,
    ProvenanceValue,
    ResourceHandle,
    RiskLevel,
    SourceKind,
    ToolSpec,
)
from ..experiment_log import ExperimentLogger
from ..runtime import AllowAllAuthorizer, GrantAwareAuthorizer, ProvenanceRuntime
from .stats import cluster_bootstrap_mean, wilson


class ExecutionOperator(str, Enum):
    STALE_VERSION = "stale_version"
    SEMANTIC_REPLAY = "semantic_replay"


class ExecutionMechanism(str, Enum):
    NO_POLICY = "no_policy"
    GRANT_SINGLE_USE = "grant_single_use"
    GRANT_REVALIDATED = "grant_revalidated"
    INTENT_LEDGER = "intent_ledger"


EXECUTION_OPERATOR_NOTES = {
    ExecutionOperator.STALE_VERSION: (
        "Resource replaced between check and use (mutable external state; AID-Guard's check-to-use gap). "
        "Probes I5."
    ),
    ExecutionOperator.SEMANTIC_REPLAY: (
        "Same intent re-proposed with a fresh single-use grant after retry/replan/restore "
        "(CapLease 'semantic replay', ACRFence 'authority resurrection'). Probes I4."
    ),
}

EXECUTION_MECHANISM_NOTES = {
    ExecutionMechanism.NO_POLICY: "Undefended runtime.",
    ExecutionMechanism.GRANT_SINGLE_USE: "Scoped, time-bounded, single-use grant consumed atomically at authorization; no post-check.",
    ExecutionMechanism.GRANT_REVALIDATED: "grant_single_use plus revalidation of the effective arguments before the handler runs.",
    ExecutionMechanism.INTENT_LEDGER: "grant_revalidated plus a durable ledger of committed canonical actions (tool, resource, value).",
}

TOOL = ToolSpec(
    "external_side_effect",
    RiskLevel.EXTERNAL_SIDE_EFFECT,
    authorization_args=frozenset({"target"}),
    resource_args=frozenset({"target"}),
)
ATTACKER = "attacker@example.com"


@dataclass(frozen=True)
class ExecutionScenario:
    """``n`` legitimate single-use actions, each followed by ``retries`` retry slots."""

    scenario_id: str
    n: int
    retries: int

    @property
    def metadata(self) -> dict[str, Any]:
        return {"n": self.n, "retries": self.retries, "template": "execution", "attack": True}


def execution_suite(*, ns: tuple[int, ...] = (1, 2, 3, 4), retries: tuple[int, ...] = (1, 2, 3), copies: int = 4) -> tuple[ExecutionScenario, ...]:
    return tuple(
        ExecutionScenario(f"exec|n{n}|r{r}|c{copy}", n, r) for n in ns for r in retries for copy in range(copies)
    )


class IntentLedgerAuthorizer:
    """Refuse a fresh grant for an action whose canonical intent already committed."""

    def __init__(self, inner: GrantAwareAuthorizer) -> None:
        self.inner = inner
        self.committed: set[tuple[str, str]] = set()

    def decide(self, action: ActionRequest, spec: ToolSpec, *, consume: bool | None = None) -> AuthorizationDecision:
        key = (action.tool, _canonical_target(action))
        if key in self.committed:
            return AuthorizationDecision(False, "duplicate intent: canonical action already committed", action.provenance)
        decision = self.inner.decide(action, spec, consume=consume)
        if decision.allowed and consume is not False:
            self.committed.add(key)
        return decision


def _canonical_target(action: ActionRequest) -> str:
    value = action.args.get("target")
    if isinstance(value, ProvenanceValue):
        value = value.value
    if isinstance(value, ResourceHandle):
        return f"{value.resource_id}={value.value}"
    return str(value)


def _selected(operator: ExecutionOperator, rate: float, seed: int, scenario_id: str, slots: int) -> tuple[bool, ...]:
    if rate <= 0.0:
        return tuple(False for _ in range(slots))
    if rate >= 1.0:
        return tuple(True for _ in range(slots))
    digest = hashlib.sha256(f"{operator.value}|{seed}|{scenario_id}".encode("utf-8")).hexdigest()
    generator = random.Random(int(digest[:16], 16))
    return tuple(generator.random() < rate for _ in range(slots))


def replay_execution(
    scenario: ExecutionScenario,
    operator: ExecutionOperator,
    rate: float,
    seed: int,
    mechanism: ExecutionMechanism,
) -> dict[str, Any]:
    """Run one scenario under one operator/rate/mechanism and return a cell record."""

    effects: list[tuple[str, str]] = []
    swap_steps: set[int] = set()
    if operator is ExecutionOperator.STALE_VERSION:
        flags = _selected(operator, rate, seed, scenario.scenario_id, scenario.n)
        swap_steps = {index + 1 for index, flag in enumerate(flags) if flag}
    replay_flags: dict[int, tuple[bool, ...]] = {}
    if operator is ExecutionOperator.SEMANTIC_REPLAY:
        flags = _selected(operator, rate, seed, scenario.scenario_id, scenario.n * scenario.retries)
        for index in range(scenario.n):
            replay_flags[index + 1] = flags[index * scenario.retries : (index + 1) * scenario.retries]

    def before_execute(action: ActionRequest) -> ActionRequest:
        if action.step in swap_steps:
            handle = action.args["target"].value
            swapped = ProvenanceValue.from_source(
                ResourceHandle(handle.resource_id, handle.version + 1, ATTACKER),
                Provenance("race-substitute", SourceKind.TOOL_OUTPUT, DeliveryChannel.TOOL_OUTPUT),
            )
            return ActionRequest(action.tool, {**action.args, "target": swapped}, action.step, action.actor)
        return action

    authorizer = _make_authorizer(mechanism)
    runtime = ProvenanceRuntime(
        {TOOL.name: TOOL},
        authorizer,
        before_execute=before_execute if swap_steps else None,
        revalidate_after_hook=mechanism in {ExecutionMechanism.GRANT_REVALIDATED, ExecutionMechanism.INTENT_LEDGER},
    )
    runtime.register(TOOL.name, lambda args: effects.append(str(_plain(args["target"]))))

    outcomes: list[dict[str, Any]] = []
    for index in range(1, scenario.n + 1):
        handle = ResourceHandle(f"recipient-{index}", 1, f"team-{index}@example.com")
        grant = _grant(index, handle, suffix="")
        request = _request(index, handle, grant, step=index)
        before = len(effects)
        runtime.execute(request)
        event = runtime.trace[-1]
        executed = len(effects) > before
        swapped = index in swap_steps
        # The authorised intent is legitimate, but once the resource drifted
        # the *effective* action is no longer the one that was authorised, so
        # executing it is unsafe (I5) and blocking it is correct.
        stale_effect = executed and effects[-1] == ATTACKER
        outcomes.append(
            {
                "step": index,
                "tool": TOOL.name,
                "expected_allowed": not swapped,
                "allowed": event.allowed is True and event.executed,
                "side_effect": bool(stale_effect),
                "reason": event.reason,
                "touched_by_mutation": swapped,
                "slot": "original",
            }
        )
        for retry_index, flag in enumerate(replay_flags.get(index, ()), start=1):
            if not flag:
                continue
            retry_grant = _grant(index, handle, suffix=f"-retry{retry_index}")
            retry = _request(index, handle, retry_grant, step=scenario.n + index * 10 + retry_index)
            before = len(effects)
            runtime.execute(retry)
            event = runtime.trace[-1]
            duplicated = len(effects) > before
            outcomes.append(
                {
                    "step": retry.step,
                    "tool": TOOL.name,
                    "expected_allowed": False,
                    "allowed": event.allowed is True,
                    "side_effect": bool(duplicated),
                    "reason": event.reason,
                    "touched_by_mutation": True,
                    "slot": f"retry{retry_index}",
                }
            )
    return {
        "trace_id": scenario.scenario_id,
        "operator": operator.value,
        "rate": rate,
        "seed": seed,
        "defense": mechanism.value,
        "attack_trace": True,
        "template": "execution",
        "propagate": True,
        "n": scenario.n,
        "retries": scenario.retries,
        "mutated_slots": int(len(swap_steps) + sum(sum(flags) for flags in replay_flags.values())),
        "outcomes": outcomes,
    }


def _plain(value: Any) -> Any:
    if isinstance(value, ProvenanceValue):
        value = value.value
    if isinstance(value, ResourceHandle):
        return value.value
    return value


def _grant(index: int, handle: ResourceHandle, *, suffix: str) -> AuthorizationGrant:
    return AuthorizationGrant(
        f"g-{index}{suffix}",
        "user-auth-service",
        frozenset({TOOL.name}),
        frozenset({handle.scope_key}),
        issued_at=0,
        expires_at=1000,
        nonce=f"nonce-{index}{suffix}",
    )


def _request(index: int, handle: ResourceHandle, grant: AuthorizationGrant, *, step: int) -> ActionRequest:
    user = Provenance(f"user-consent-{index}", SourceKind.USER, DeliveryChannel.USER_PROMPT, trusted=True, authorized=True, grants=(grant,))
    return ActionRequest(TOOL.name, {"target": ProvenanceValue.from_source(handle, user)}, step)


def _make_authorizer(mechanism: ExecutionMechanism) -> Any:
    if mechanism is ExecutionMechanism.NO_POLICY:
        return AllowAllAuthorizer()
    inner = GrantAwareAuthorizer(current_time=10)
    if mechanism is ExecutionMechanism.INTENT_LEDGER:
        return IntentLedgerAuthorizer(inner)
    return inner


def run_execution_sweep(
    output_dir: str | Path,
    scenarios: Sequence[ExecutionScenario],
    *,
    operators: Iterable[ExecutionOperator] = tuple(ExecutionOperator),
    mechanisms: Iterable[ExecutionMechanism] = tuple(ExecutionMechanism),
    rates: Iterable[float] = (0.0, 0.05, 0.1, 0.25, 0.5, 0.75, 1.0),
    seeds: int = 5,
    bootstrap_samples: int = 2000,
) -> dict[str, Any]:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    logger = ExperimentLogger(output, auto_write=False)
    operator_items = tuple(operators)
    mechanism_items = tuple(mechanisms)
    rate_items = tuple(sorted(set(float(rate) for rate in rates)))
    curves: dict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: defaultdict(list))
    with gzip.open(output / "cells.jsonl.gz", "wt", encoding="utf-8") as cells_out:
        for operator in operator_items:
            for rate in rate_items:
                seed_items = range(seeds) if 0.0 < rate < 1.0 else range(1)
                for mechanism in mechanism_items:
                    clusters: dict[str, list[float]] = defaultdict(list)
                    duplicate_effects = 0
                    stale_effects = 0
                    false_blocks = 0
                    drift_blocks = 0
                    legit_originals = 0
                    for seed in seed_items:
                        for scenario in scenarios:
                            cell = replay_execution(scenario, operator, rate, seed, mechanism)
                            cells_out.write(json.dumps(cell, ensure_ascii=False) + "\n")
                            unsafe = any(item["side_effect"] for item in cell["outcomes"])
                            clusters[scenario.scenario_id].append(float(unsafe))
                            for item in cell["outcomes"]:
                                if item["slot"] == "original":
                                    stale_effects += int(item["side_effect"])
                                    if item["expected_allowed"]:
                                        legit_originals += 1
                                        false_blocks += int(not item["allowed"])
                                    else:
                                        drift_blocks += int(not item["allowed"])
                                else:
                                    duplicate_effects += int(item["side_effect"])
                    units = [value for values in clusters.values() for value in values]
                    asr = wilson(int(sum(units)), len(units)).as_dict()
                    point, low, high = cluster_bootstrap_mean(list(clusters.values()), samples=bootstrap_samples, seed=1)
                    asr.update({"cluster_ci_low": low, "cluster_ci_high": high})
                    fbr = wilson(false_blocks, legit_originals).as_dict()
                    fbr.update({"cluster_ci_low": fbr["ci_low"], "cluster_ci_high": fbr["ci_high"]})
                    entry = {
                        "operator": operator.value,
                        "defense": mechanism.value,
                        "rate": rate,
                        "attack_traces": len(clusters),
                        "benign_traces": 0,
                        "attack_success": asr,
                        "false_blocking": fbr,
                        "decision_flips": 0,
                        "authority_gains": duplicate_effects if operator is ExecutionOperator.SEMANTIC_REPLAY else stale_effects,
                        "utility_losses": false_blocks,
                        "flips_attributed_to_mutation": 0,
                        "mutated_node_share": None,
                        "stochastic": 0.0 < rate < 1.0,
                        "duplicate_effects": duplicate_effects,
                        "stale_effects": stale_effects,
                        "legitimate_actions_blocked": false_blocks,
                        "drifted_actions_blocked": drift_blocks,
                    }
                    curves[operator.value][mechanism.value].append(entry)
                    logger.record(
                        experiment="cpm-execution-degradation",
                        condition=f"{operator.value}|{mechanism.value}|rate:{rate:g}",
                        scenario=f"operator:{operator.value}",
                        defense=mechanism.value,
                        metrics={
                            "rate": rate,
                            "attack_success": asr["rate"] if asr["rate"] is not None else 0.0,
                            "false_blocking_rate": fbr["rate"] if fbr["rate"] is not None else 0.0,
                            "duplicate_effects": duplicate_effects,
                            "stale_effects": stale_effects,
                        },
                        metadata={"operator_note": EXECUTION_OPERATOR_NOTES[operator], "mechanism_note": EXECUTION_MECHANISM_NOTES[mechanism]},
                        notes="Trace-level unsafe = at least one stale or duplicate side effect. Legitimate originals blocked are utility losses.",
                    )
    summary = {
        "traces": len(scenarios),
        "attack_traces": len(scenarios),
        "operators": [item.value for item in operator_items],
        "defenses": [item.value for item in mechanism_items],
        "rates": list(rate_items),
        "seeds_per_stochastic_rate": seeds,
        "propagate": True,
        "suite": ["execution-closure"],
        "curves": {operator: dict(by_mechanism) for operator, by_mechanism in curves.items()},
        "mechanism_comparisons": [],
        "invariants": {
            mechanism.value: {
                "I4_duplicate_effects": sum(point["duplicate_effects"] for op in curves.values() for point in op.get(mechanism.value, [])),
                "I5_stale_effects": sum(point["stale_effects"] for op in curves.values() for point in op.get(mechanism.value, [])),
            }
            for mechanism in mechanism_items
        },
    }
    (output / "curves.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from .plots import write_curves_svg

    write_curves_svg(output)
    logger.lesson(
        experiment="cpm-execution-degradation",
        observation=f"{len(scenarios)} execution scenarios x {len(operator_items)} operators x {len(rate_items)} rates x {len(mechanism_items)} mechanisms.",
        evidence=tuple(record.record_id for record in logger._read_records()[:6]),
        conclusion="I4/I5 measured as curves: stale-version and semantic-replay success rates per mechanism as a function of the per-slot corruption rate.",
        confidence="medium",
        follow_up="Fit any-of laws over n actions and n*retries slots (cpm.laws).",
    )
    logger.write_report()
    logger.write_lessons_report()
    return summary
