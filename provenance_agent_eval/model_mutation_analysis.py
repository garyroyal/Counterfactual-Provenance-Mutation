"""Paired analysis for model-fixed provenance mutation replays."""

from __future__ import annotations

import argparse
import json
from itertools import combinations
from pathlib import Path
from typing import Any

from .experiment_log import ExperimentLogger
from .model_compare import _bootstrap_mean_ci, _mcnemar_exact


def analyze_model_mutation_run(
    input_dir: str | Path,
    output_dir: str | Path,
    *,
    bootstrap_samples: int = 10000,
) -> dict[str, Any]:
    rows = _load(Path(input_dir) / "experiments.jsonl")
    if not rows:
        raise ValueError("no model-provenance-mutation-e2e raw records found")
    logger = ExperimentLogger(output_dir, auto_write=False)
    by_evidence: dict[str, dict[str, dict[str, Any]]] = {}
    for evidence in sorted({key[0] for key in rows}):
        by_evidence[evidence] = {}
        for policy in ("no_policy", "source_aware", "graph_aware"):
            group = [item for key, item in rows.items() if key[0] == evidence and key[1] == policy]
            attacks = [item for item in group if item["case"].get("attack")]
            safe = [item for item in group if item.get("expected_evidence_allowed")]
            by_evidence[evidence][policy] = {
                "attack_cases": len(attacks),
                "model_induction_rate": _mean(item["metrics"].get("model_attack_induction", 0) for item in attacks),
                "side_effect_rate": _mean(item["metrics"].get("actual_side_effect", 0) for item in attacks),
                "runtime_attack_success_rate": _mean(item["metrics"].get("runtime_attack_success", 0) for item in attacks),
                "safe_task_success_rate": _mean(item["metrics"].get("utility", 0) for item in safe),
                "false_blocking_rate": _mean(item["metrics"].get("false_blocking_rate", 0) for item in safe),
            }

    comparisons: list[dict[str, Any]] = []
    for evidence in sorted(by_evidence):
        for left, right in combinations(("no_policy", "source_aware", "graph_aware"), 2):
            keys = sorted(
                key for key in rows
                if key[0] == evidence and key[1] == left and rows[key]["case"].get("attack")
                and (key[0], right, key[2], key[3]) in rows
                and rows[key]["metrics"].get("model_attack_induction", 0)
            )
            left_values = [int(rows[key]["metrics"].get("actual_side_effect", 0)) for key in keys]
            right_values = [int(rows[(key[0], right, key[2], key[3])]["metrics"].get("actual_side_effect", 0)) for key in keys]
            differences = [right_value - left_value for left_value, right_value in zip(left_values, right_values)]
            right_only = sum(right_value == 1 and left_value == 0 for left_value, right_value in zip(left_values, right_values))
            left_only = sum(left_value == 1 and right_value == 0 for left_value, right_value in zip(left_values, right_values))
            ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, 0) if differences else (0.0, 0.0)
            comparisons.append({
                "evidence": evidence,
                "left": left,
                "right": right,
                "paired_induced_cases": len(keys),
                "right_minus_left_side_effect_rate": _mean(differences),
                "bootstrap_ci_95": [ci_low, ci_high],
                "mcnemar_exact_p": _mcnemar_exact(right_only, left_only),
            })

    for evidence, policies in by_evidence.items():
        for policy, summary in policies.items():
            logger.record(
                experiment="model-provenance-mutation-analysis",
                condition=f"{policy}|evidence:{evidence}-aggregate",
                model=None,
                scenario=f"evidence:{evidence}",
                defense=policy,
                metrics={
                    "model_attack_induction": summary["model_induction_rate"],
                    "runtime_attack_success": summary["runtime_attack_success_rate"],
                    "actual_side_effect": summary["side_effect_rate"],
                    "utility": summary["safe_task_success_rate"],
                    "false_blocking_rate": summary["false_blocking_rate"],
                },
                metadata={"input_dir": str(input_dir), "summary": summary},
                notes="Aggregate over model-fixed mutation replays.",
            )
    analysis_records = logger._read_records()
    logger.lesson(
        experiment="model-provenance-mutation-analysis",
        observation="按 evidence 和 policy 对同一模型动作做配对副作用比较。",
        evidence=tuple(item.record_id for item in analysis_records[-min(6, len(analysis_records)):]),
        conclusion="source-forgery 对表面 source-aware 与 graph-aware 的差异可被同一模型动作的配对副作用直接归因；诱导率保持不变，变化发生在授权/执行阶段。",
        confidence="medium",
        follow_up="对 Qwen3:4B 与 4090 上的 Qwen3:8B、Llama3.1:8B 使用相同分析，报告模型家族与 evidence 的交互。",
    )
    result = {"evidence": by_evidence, "comparisons": comparisons}
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)
    (output / "model_mutation_analysis.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    logger.write_report()
    logger.write_lessons_report()
    return result


def _load(path: Path) -> dict[tuple[str, str, str, int], dict[str, Any]]:
    result: dict[tuple[str, str, str, int], dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        if record.get("experiment") != "model-provenance-mutation-e2e" or str(record.get("condition", "")).endswith("-aggregate"):
            continue
        key = (
            str(record.get("metadata", {}).get("evidence", "")),
            str(record.get("defense", "")),
            str(record.get("scenario", "")),
            int(record.get("seed", 0)),
        )
        result[key] = {
            "metrics": record.get("metrics", {}),
            "case": record.get("metadata", {}).get("case", {}),
            "expected_evidence_allowed": bool(record.get("metadata", {}).get("expected_evidence_allowed", False)),
        }
    return result


def _mean(values: Any) -> float:
    items = [float(value) for value in values]
    return sum(items) / len(items) if items else 0.0


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", required=True)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    result = analyze_model_mutation_run(args.input_dir, args.output_dir)
    print(json.dumps({"evidence": list(result["evidence"]), "comparisons": len(result["comparisons"])}, ensure_ascii=False))


if __name__ == "__main__":
    main()
