"""Repeatable paired experiment runner for the controlled milestone."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Mapping

from .experiment_log import ExperimentLogger
from .runtime import EvaluationMetrics, EvaluationResult
from .scenarios import PairedScenario, paired_scenarios, run_scenario


@dataclass(frozen=True)
class MatrixSummary:
    scenario: str
    condition: str
    repetitions: int
    metrics: dict[str, float]
    record_ids: tuple[str, ...]


ScenarioRunner = Callable[[PairedScenario, bool, int], EvaluationResult]


def run_controlled_matrix(
    output_dir: str | Path,
    *,
    repetitions: int = 3,
    scenarios: tuple[PairedScenario, ...] | None = None,
    runner: ScenarioRunner | None = None,
) -> list[MatrixSummary]:
    """Run paired conditions and persist both per-run and aggregate records.

    The `runner` hook lets the same logging/aggregation layer wrap different
    agent backends. A seed is passed even though the current deterministic
    executor does not use it yet.
    """

    if repetitions < 1:
        raise ValueError("repetitions must be at least 1")
    logger = ExperimentLogger(output_dir)
    selected = scenarios or paired_scenarios()
    execute = runner or (lambda scenario, protected, seed: run_scenario(scenario, protected=protected))
    summaries: list[MatrixSummary] = []

    for scenario in selected:
        per_condition: dict[str, list[EvaluationMetrics]] = {"no-authorization": [], "source-aware-authorization": []}
        ids_by_condition: dict[str, list[str]] = {"no-authorization": [], "source-aware-authorization": []}
        for seed in range(repetitions):
            baseline = execute(scenario, False, seed)
            baseline_record = logger.record(
                experiment="controlled-channel-matrix",
                condition="no-authorization",
                scenario=scenario.name,
                seed=seed,
                metrics=_metrics_dict(baseline.metrics),
                notes="Reference condition; no runtime authorization gate.",
            )
            protected = execute(scenario, True, seed)
            protected_record = logger.record(
                experiment="controlled-channel-matrix",
                condition="source-aware-authorization",
                scenario=scenario.name,
                defense="source-aware-authorization",
                baseline_id=baseline_record.record_id,
                seed=seed,
                metrics=_metrics_dict(protected.metrics),
                notes="Paired condition; only the runtime authorization policy changes.",
            )
            per_condition["no-authorization"].append(baseline.metrics)
            per_condition["source-aware-authorization"].append(protected.metrics)
            ids_by_condition["no-authorization"].append(baseline_record.record_id)
            ids_by_condition["source-aware-authorization"].append(protected_record.record_id)

        for condition, metrics in per_condition.items():
            summary_metrics = _average_metrics(metrics)
            summary_record = logger.record(
                experiment="controlled-channel-matrix",
                condition=f"{condition}-aggregate",
                scenario=scenario.name,
                defense="source-aware-authorization" if condition != "no-authorization" else None,
                metrics=summary_metrics,
                metadata={"repetitions": repetitions, "source_records": ids_by_condition[condition]},
                notes="Aggregate mean across paired repetitions; inspect source records for raw outcomes.",
            )
            summaries.append(
                MatrixSummary(
                    scenario=scenario.name,
                    condition=condition,
                    repetitions=repetitions,
                    metrics=summary_metrics,
                    record_ids=tuple(ids_by_condition[condition] + [summary_record.record_id]),
                )
            )

        logger.lesson(
            experiment="controlled-channel-matrix",
            observation=f"场景 {scenario.name} 在相同用户目标和攻击语义下完成了 {repetitions} 次配对运行。",
            evidence=tuple(ids_by_condition["source-aware-authorization"]),
            conclusion="当前确定性原型中，来源感知授权保持读取任务 Utility，并阻断未授权外部副作用。",
            confidence="low",
            follow_up="接入真实模型和来源变换节点后，检查该结论是否跨模型与措辞变化成立。",
        )

    logger.write_report()
    logger.write_lessons_report()
    return summaries


def _metrics_dict(metrics: EvaluationMetrics) -> dict[str, float | bool | int]:
    return {
        "utility": metrics.utility,
        "attack_success": metrics.attack_success,
        "sensitive_data_leak": metrics.sensitive_data_leak,
        "unauthorized_side_effect": metrics.unauthorized_side_effect,
        "blocked_actions": metrics.blocked_actions,
        "policy_violations": metrics.policy_violations,
        "executed_actions": metrics.executed_actions,
        "attempted_attack_actions": metrics.attempted_attack_actions,
    }


def _average_metrics(items: list[EvaluationMetrics]) -> Mapping[str, float]:
    if not items:
        raise ValueError("cannot aggregate an empty metric list")
    values = [_metrics_dict(item) for item in items]
    return {
        name: sum(float(value[name]) for value in values) / len(values)
        for name in values[0]
    }
