"""Paired analysis for the sandboxed real-tool end-to-end experiments."""

from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path
from typing import Any

from .experiment_log import ExperimentLogger
from .model_compare import _bootstrap_mean_ci, _mcnemar_exact


def analyze_real_tool_runs(
    output_dir: str | Path,
    runs: dict[str, str | Path],
    *,
    bootstrap_samples: int = 10000,
) -> dict[str, Any]:
    if len(runs) < 1:
        raise ValueError("at least one real-tool run is required")
    logger = ExperimentLogger(output_dir, auto_write=False)
    loaded = {name: _load(Path(directory) / "experiments.jsonl") for name, directory in runs.items()}
    summaries: list[dict[str, Any]] = []
    decision_maps: dict[str, dict[tuple[str, int], int]] = {}
    record_ids: list[str] = []

    for model, rows in loaded.items():
        decisions = {
            key: int(value["metrics"].get("model_attack_induction", 0.0))
            for key, value in rows.items()
            if value["case"]["attack"] and value["policy"] == "no_policy"
        }
        decision_maps[model] = decisions
        attack_rows = [value for value in rows.values() if value["case"]["attack"]]
        safe_rows = [value for value in rows.values() if value["case"]["expected_allowed"]]
        no_policy = [value for value in attack_rows if value["policy"] == "no_policy"]
        source_aware = [value for value in attack_rows if value["policy"] == "source_aware"]
        by_policy_tool = {}
        for tool in sorted({value["case"]["target_tool"] for value in attack_rows}):
            by_policy_tool[tool] = {
                policy: {
                    "model_attack_induction": _mean(
                        value["metrics"].get("model_attack_induction", 0.0)
                        for value in attack_rows
                        if value["case"]["target_tool"] == tool and value["policy"] == policy
                    ),
                    "runtime_attack_success": _mean(
                        value["metrics"].get("runtime_attack_success", 0.0)
                        for value in attack_rows
                        if value["case"]["target_tool"] == tool and value["policy"] == policy
                    ),
                }
                for policy in ("no_policy", "source_aware")
            }

        attack_case_ids = {value["case"]["case_id"] for value in attack_rows}
        paired_keys = sorted({(case_id, seed) for case_id, seed, policy in rows if case_id in attack_case_ids})
        paired_attack = [
            key for key in paired_keys
            if (key[0], key[1], "no_policy") in rows and (key[0], key[1], "source_aware") in rows
            and rows[(key[0], key[1], "no_policy")]["metrics"].get("model_attack_induction", 0.0)
        ]
        no_values = [int(rows[(case_id, seed, "no_policy")]["metrics"].get("runtime_attack_success", 0.0)) for case_id, seed in paired_attack]
        safe_values = [int(rows[(case_id, seed, "source_aware")]["metrics"].get("runtime_attack_success", 0.0)) for case_id, seed in paired_attack]
        differences = [safe - no for safe, no in zip(safe_values, no_values)]
        source_only = sum(safe == 1 and no == 0 for safe, no in zip(safe_values, no_values))
        no_only = sum(safe == 0 and no == 1 for safe, no in zip(safe_values, no_values))
        ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, 0) if differences else (0.0, 0.0)
        summary = {
            "model": model,
            "attack_cases": len(attack_rows),
            "safe_cases": len(safe_rows),
            "model_attack_induction_rate": _mean(value["metrics"].get("model_attack_induction", 0.0) for value in attack_rows),
            "no_policy_side_effect_rate": _mean(value["metrics"].get("actual_side_effect", 0.0) for value in no_policy),
            "source_aware_side_effect_rate": _mean(value["metrics"].get("actual_side_effect", 0.0) for value in source_aware),
            "source_aware_attack_rate": _mean(value["metrics"].get("runtime_attack_success", 0.0) for value in source_aware),
            "safe_task_success_rate": _mean(value["metrics"].get("utility", 0.0) for value in safe_rows),
            "policy_effect_on_induced": {
                "paired_induced_cases": len(paired_attack),
                "source_aware_minus_no_policy": _mean(differences),
                "bootstrap_ci_95": [ci_low, ci_high],
                "mcnemar_source_only": source_only,
                "mcnemar_no_policy_only": no_only,
                "mcnemar_exact_p": _mcnemar_exact(source_only, no_only),
            },
            "by_tool": by_policy_tool,
        }
        summaries.append(summary)
        for policy, metric in (("no_policy", "no_policy_side_effect_rate"), ("source_aware", "source_aware_side_effect_rate")):
            record = logger.record(
                experiment="real-tool-e2e",
                condition=f"{model}|{policy}-aggregate",
                model=model,
                scenario="real-tool-analysis",
                defense=policy,
                metrics={
                    "model_attack_induction": summary["model_attack_induction_rate"],
                    "runtime_attack_success": summary["source_aware_attack_rate"] if policy == "source_aware" else summary["no_policy_side_effect_rate"],
                    "actual_side_effect": summary[metric],
                    "utility": summary["safe_task_success_rate"],
                    "false_blocking_rate": 1.0 - summary["safe_task_success_rate"],
                    "bootstrap_ci_low": summary["policy_effect_on_induced"]["bootstrap_ci_95"][0],
                    "bootstrap_ci_high": summary["policy_effect_on_induced"]["bootstrap_ci_95"][1],
                    "mcnemar_exact_p": summary["policy_effect_on_induced"]["mcnemar_exact_p"],
                },
                baseline_id=record_ids[-1] if policy == "source_aware" and record_ids else None,
                metadata={"source_dir": str(runs[model]), "summary": summary},
                notes="Aggregate from sandbox adapter receipts with model and runtime stages kept separate.",
            )
            record_ids.append(record.record_id)

    cross_model: list[dict[str, Any]] = []
    names = list(runs)
    for left_name, right_name in combinations(names, 2):
        keys = sorted(set(decision_maps[left_name]) & set(decision_maps[right_name]))
        left = [decision_maps[left_name][key] for key in keys]
        right = [decision_maps[right_name][key] for key in keys]
        differences = [a - b for a, b in zip(left, right)]
        left_only = sum(a == 1 and b == 0 for a, b in zip(left, right))
        right_only = sum(a == 0 and b == 1 for a, b in zip(left, right))
        ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, 0) if differences else (0.0, 0.0)
        cross_model.append({
            "left": left_name,
            "right": right_name,
            "paired_attack_cases": len(keys),
            "left_rate": _mean(left),
            "right_rate": _mean(right),
            "rate_difference": _mean(differences),
            "bootstrap_ci_95": [ci_low, ci_high],
            "mcnemar_exact_p": _mcnemar_exact(left_only, right_only),
        })

    logger.lesson(
        experiment="real-tool-e2e-analysis",
        observation="端到端日志同时包含模型动作、runtime 决策和 adapter receipt；分析仅对共享 case/seed 做配对比较。",
        evidence=tuple(record_ids),
        conclusion="真实副作用率必须以 adapter receipt 为准；source-aware 的安全收益要与安全任务完成率、误阻断和模型诱导率分开报告。",
        confidence="medium",
        follow_up="在两阶段真实工具链和 grant-aware policy 上复现实验，并加入故障、重试和超时分层。",
    )
    summary = {"models": summaries, "cross_model": cross_model}
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    (output / "real_tool_analysis.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    logger.write_report()
    logger.write_lessons_report()
    return summary


def _load(path: Path) -> dict[tuple[str, int, str], dict[str, Any]]:
    result: dict[tuple[str, int, str], dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        if record.get("experiment") != "real-tool-e2e" or str(record.get("condition", "")).endswith("-aggregate"):
            continue
        case = record.get("metadata", {}).get("case", {})
        case_id = str(case.get("case_id", record.get("scenario", "")))
        seed = record.get("seed")
        policy = str(record.get("defense", ""))
        if seed is not None and policy:
            result[(case_id, int(seed), policy)] = {
                "metrics": record.get("metrics", {}),
                "case": case,
                "policy": policy,
            }
    return result


def _mean(values: Any) -> float:
    items = [float(value) for value in values]
    return sum(items) / len(items) if items else 0.0
