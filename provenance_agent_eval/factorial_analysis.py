"""Analyze orthogonal presentation × provenance × policy model experiments."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .experiment_log import ExperimentLogger
from .model_compare import _bootstrap_mean_ci, _mcnemar_exact
from .model_factorial_runner import PRESENTATIONS


def analyze_factorial_runs(
    output_dir: str | Path,
    runs: dict[str, str | Path],
    *,
    bootstrap_samples: int = 10000,
) -> dict[str, Any]:
    if len(runs) < 1:
        raise ValueError("at least one factorial run is required")
    logger = ExperimentLogger(output_dir, auto_write=False)
    model_summaries: list[dict[str, Any]] = []
    evidence_summaries: list[dict[str, Any]] = []
    record_ids: list[str] = []
    decisions_by_model: dict[str, dict[tuple[str, int], int]] = {}

    for model, directory in runs.items():
        decisions, runtime = _load_factorial(Path(directory) / "experiments.jsonl")
        decisions_by_model[model] = decisions
        direct = {seed: value for (presentation, seed), value in decisions.items() if presentation == "direct"}
        rates = {
            presentation: _mean(value for (name, _), value in decisions.items() if name == presentation)
            for presentation in PRESENTATIONS
        }
        comparisons = []
        for presentation in PRESENTATIONS:
            if presentation == "direct":
                continue
            current = {seed: value for (name, seed), value in decisions.items() if name == presentation}
            seeds = sorted(set(direct) & set(current))
            baseline = [direct[seed] for seed in seeds]
            values = [current[seed] for seed in seeds]
            differences = [value - base for value, base in zip(values, baseline)]
            current_only = sum(value == 1 and base == 0 for value, base in zip(values, baseline))
            direct_only = sum(value == 0 and base == 1 for value, base in zip(values, baseline))
            ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, 0)
            comparisons.append({
                "presentation": presentation,
                "baseline": "direct",
                "paired_observations": len(seeds),
                "rate_difference": _mean(differences),
                "bootstrap_ci_95": [ci_low, ci_high],
                "mcnemar_current_only": current_only,
                "mcnemar_direct_only": direct_only,
                "mcnemar_exact_p": _mcnemar_exact(current_only, direct_only),
            })

        policy_keys = sorted({(presentation, evidence, seed) for presentation, evidence, _, seed in runtime})
        no_policy = [runtime[(presentation, evidence, "no_policy", seed)] for presentation, evidence, seed in policy_keys]
        source_aware = [runtime[(presentation, evidence, "source_aware", seed)] for presentation, evidence, seed in policy_keys]
        policy_differences = [safe - open_value for safe, open_value in zip(source_aware, no_policy)]
        source_only = sum(safe == 1 and open_value == 0 for safe, open_value in zip(source_aware, no_policy))
        open_only = sum(safe == 0 and open_value == 1 for safe, open_value in zip(source_aware, no_policy))
        policy_ci = _bootstrap_mean_ci(policy_differences, bootstrap_samples, 0)
        summary = {
            "model": model,
            "model_decisions": len(decisions),
            "presentation_rates": rates,
            "presentation_vs_direct": comparisons,
            "policy_effect": {
                "paired_runtime_cells": len(policy_keys),
                "no_policy_attack_rate": _mean(no_policy),
                "source_aware_attack_rate": _mean(source_aware),
                "source_aware_minus_no_policy": _mean(policy_differences),
                "bootstrap_ci_95": list(policy_ci),
                "mcnemar_source_only": source_only,
                "mcnemar_no_policy_only": open_only,
                "mcnemar_exact_p": _mcnemar_exact(source_only, open_only),
            },
        }
        model_summaries.append(summary)
        for presentation, rate in rates.items():
            record = logger.record(
                experiment="factorial-presentation-analysis",
                condition=f"{model}|presentation:{presentation}-aggregate",
                model=model,
                scenario=f"presentation:{presentation}",
                metrics={"model_attack_induction": rate},
                metadata={"source_dir": str(directory)},
                notes="Presentation rate with runtime provenance evidence held out of the model prompt.",
            )
            record_ids.append(record.record_id)
        record = logger.record(
            experiment="factorial-policy-analysis",
            condition=f"{model}|source-aware-vs-no-policy-aggregate",
            model=model,
            scenario="policy:source-aware-vs-no-policy",
            metrics={
                "runtime_attack_success_difference": summary["policy_effect"]["source_aware_minus_no_policy"],
                "bootstrap_ci_low": policy_ci[0],
                "bootstrap_ci_high": policy_ci[1],
                "mcnemar_exact_p": summary["policy_effect"]["mcnemar_exact_p"],
                "paired_observations": len(policy_keys),
            },
            metadata=summary["policy_effect"],
            notes="Negative difference means source-aware runtime prevented attacks allowed by no-policy.",
        )
        record_ids.append(record.record_id)

        for evidence in PRESENTATIONS:
            for policy in ("no_policy", "source_aware"):
                values = [
                    value
                    for (presentation, evidence_name, policy_name, seed), value in runtime.items()
                    if evidence_name == evidence and policy_name == policy
                ]
                evidence_summaries.append({
                    "model": model,
                    "evidence": evidence,
                    "policy": policy,
                    "runtime_attack_rate": _mean(values),
                    "observations": len(values),
                })

    cross_model = []
    names = list(runs)
    for index, left_name in enumerate(names):
        for right_name in names[index + 1:]:
            left = decisions_by_model[left_name]
            right = decisions_by_model[right_name]
            keys = sorted(set(left) & set(right))
            left_values = [left[key] for key in keys]
            right_values = [right[key] for key in keys]
            differences = [a - b for a, b in zip(left_values, right_values)]
            left_only = sum(a == 1 and b == 0 for a, b in zip(left_values, right_values))
            right_only = sum(a == 0 and b == 1 for a, b in zip(left_values, right_values))
            ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, 0)
            cross_model.append({
                "left": left_name,
                "right": right_name,
                "paired_observations": len(keys),
                "left_rate": _mean(left_values),
                "right_rate": _mean(right_values),
                "rate_difference": _mean(differences),
                "bootstrap_ci_95": [ci_low, ci_high],
                "mcnemar_left_only": left_only,
                "mcnemar_right_only": right_only,
                "mcnemar_exact_p": _mcnemar_exact(left_only, right_only),
            })

    logger.lesson(
        experiment="factorial-analysis",
        observation="presentation 与 runtime provenance evidence 已正交；早期 matched-laundering 的 transform 效应不能继续作因果解释。",
        evidence=tuple(record_ids),
        conclusion="模型诱导应归因于可见 presentation；provenance evidence 的作用应由 runtime policy 单独衡量。",
        confidence="high",
        follow_up="在真实工具任务和 7B/8B 模型上复现该正交设计。",
    )
    summary = {
        "models": model_summaries,
        "evidence_runtime_rates": evidence_summaries,
        "cross_model": cross_model,
    }
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    (output / "factorial_analysis.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    logger.write_report()
    logger.write_lessons_report()
    return summary


def _load_factorial(path: Path) -> tuple[dict[tuple[str, int], int], dict[tuple[str, str, str, int], int]]:
    decisions: dict[tuple[str, int], int] = {}
    runtime: dict[tuple[str, str, str, int], int] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        condition = str(record.get("condition", ""))
        seed = record.get("seed")
        if seed is None or condition.endswith("-aggregate"):
            continue
        metadata = record.get("metadata", {})
        if record.get("experiment") == "model-presentation-factorial":
            decisions[(str(metadata["presentation"]), int(seed))] = int(record["metrics"]["model_attack_induction"])
        elif record.get("experiment") == "model-provenance-runtime-factorial":
            runtime[(
                str(metadata["presentation"]),
                str(metadata["evidence_transform"]),
                str(record["defense"]),
                int(seed),
            )] = int(record["metrics"]["runtime_attack_success"])
    return decisions, runtime


def _mean(values: Any) -> float:
    items = [float(value) for value in values]
    return sum(items) / len(items) if items else 0.0
