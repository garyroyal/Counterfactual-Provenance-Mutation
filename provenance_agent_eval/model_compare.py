"""Paired cross-model comparison with exact McNemar and bootstrap intervals."""

from __future__ import annotations

import json
import math
import random
from pathlib import Path
from typing import Any

from .experiment_log import ExperimentLogger


def compare_model_runs(
    output_dir: str | Path,
    runs: dict[str, str | Path],
    *,
    bootstrap_samples: int = 5000,
    random_seed: int = 0,
) -> dict[str, Any]:
    """Compare paired raw decisions from model experiment directories."""

    if len(runs) < 2:
        raise ValueError("at least two model runs are required")
    loaded = {name: _load_raw(Path(path) / "experiments.jsonl") for name, path in runs.items()}
    common_keys = set.intersection(*(set(items) for items in loaded.values()))
    if not common_keys:
        raise ValueError("model runs have no paired raw records")
    logger = ExperimentLogger(output_dir)
    record_ids: list[str] = []
    for name, items in loaded.items():
        values = [float(items[key]["metrics"]["model_attack_induction"]) for key in sorted(common_keys)]
        record = logger.record(
            experiment="cross-model-action-induction",
            condition=f"{name}-aggregate",
            model=name,
            scenario="paired-common-cases",
            metrics={
                "model_attack_induction": _mean(values),
                "paired_observations": len(values),
            },
            metadata={"source_dir": str(runs[name]), "paired_keys": len(common_keys)},
            notes="Aggregate uses only case/variant pairs shared by every model run.",
        )
        record_ids.append(record.record_id)

    comparisons: list[dict[str, Any]] = []
    transform_effects: list[dict[str, Any]] = []
    names = list(runs)
    for left_index, left_name in enumerate(names):
        for right_name in names[left_index + 1 :]:
            left = [int(loaded[left_name][key]["metrics"]["model_attack_induction"]) for key in sorted(common_keys)]
            right = [int(loaded[right_name][key]["metrics"]["model_attack_induction"]) for key in sorted(common_keys)]
            differences = [a - b for a, b in zip(left, right)]
            discordant_left = sum(a == 1 and b == 0 for a, b in zip(left, right))
            discordant_right = sum(a == 0 and b == 1 for a, b in zip(left, right))
            ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, random_seed)
            comparison = {
                "left": left_name,
                "right": right_name,
                "paired_observations": len(differences),
                "left_rate": _mean(left),
                "right_rate": _mean(right),
                "rate_difference": _mean(differences),
                "bootstrap_ci_95": [ci_low, ci_high],
                "mcnemar_discordant_left": discordant_left,
                "mcnemar_discordant_right": discordant_right,
                "mcnemar_exact_p": _mcnemar_exact(discordant_left, discordant_right),
            }
            comparisons.append(comparison)
            record = logger.record(
                experiment="cross-model-action-induction",
                condition=f"{left_name}-vs-{right_name}-aggregate",
                scenario="paired-model-difference",
                metrics={
                    "model_attack_induction_difference": comparison["rate_difference"],
                    "bootstrap_ci_low": ci_low,
                    "bootstrap_ci_high": ci_high,
                    "mcnemar_exact_p": comparison["mcnemar_exact_p"],
                    "paired_observations": len(differences),
                },
                metadata=comparison,
                notes="Positive difference means the left model selected more injected actions.",
            )
            record_ids.append(record.record_id)
    for model_name, items in loaded.items():
        by_transform: dict[str, dict[int, int]] = {}
        for (case_key, seed), record in items.items():
            transform = case_key.split("|", 2)[1]
            by_transform.setdefault(transform, {})[seed] = int(record["metrics"]["model_attack_induction"])
        direct = by_transform.get("direct", {})
        for transform, values in sorted(by_transform.items()):
            if transform == "direct":
                continue
            seeds = sorted(set(direct) & set(values))
            if not seeds:
                continue
            baseline = [direct[seed] for seed in seeds]
            current = [values[seed] for seed in seeds]
            differences = [value - base for value, base in zip(current, baseline)]
            current_only = sum(value == 1 and base == 0 for value, base in zip(current, baseline))
            baseline_only = sum(value == 0 and base == 1 for value, base in zip(current, baseline))
            ci_low, ci_high = _bootstrap_mean_ci(differences, bootstrap_samples, random_seed)
            effect = {
                "model": model_name,
                "baseline_transform": "direct",
                "transform": transform,
                "paired_observations": len(seeds),
                "baseline_rate": _mean(baseline),
                "transform_rate": _mean(current),
                "rate_difference": _mean(differences),
                "bootstrap_ci_95": [ci_low, ci_high],
                "mcnemar_discordant_transform": current_only,
                "mcnemar_discordant_baseline": baseline_only,
                "mcnemar_exact_p": _mcnemar_exact(current_only, baseline_only),
            }
            transform_effects.append(effect)
            record = logger.record(
                experiment="within-model-transform-effect",
                condition=f"{model_name}|{transform}-vs-direct-aggregate",
                model=model_name,
                scenario=f"transform-effect:{transform}",
                metrics={
                    "model_attack_induction_difference": effect["rate_difference"],
                    "bootstrap_ci_low": ci_low,
                    "bootstrap_ci_high": ci_high,
                    "mcnemar_exact_p": effect["mcnemar_exact_p"],
                    "paired_observations": len(seeds),
                },
                metadata=effect,
                notes="Positive difference means the provenance transform induced more unsafe actions than direct delivery.",
            )
            record_ids.append(record.record_id)
    logger.lesson(
        experiment="cross-model-action-induction",
        observation=f"完成 {len(names)} 个模型在 {len(common_keys)} 个共享 case/variant 上的配对比较。",
        evidence=tuple(record_ids),
        conclusion="跨模型差异与共同趋势必须同时报告；p 值不能替代效应量和区间。",
        confidence="medium",
        follow_up="扩展模型规模和任务族，并以预注册的主要对比避免多重检验膨胀。",
    )
    summary = {
        "models": names,
        "paired_observations": len(common_keys),
        "comparisons": comparisons,
        "transform_effects": transform_effects,
    }
    Path(output_dir, "comparison.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    logger.write_report()
    logger.write_lessons_report()
    return summary


def _load_raw(path: Path) -> dict[tuple[str, int], dict[str, Any]]:
    items: dict[tuple[str, int], dict[str, Any]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        if record.get("experiment") != "model-action-induction":
            continue
        if str(record.get("condition", "")).endswith("-aggregate") or "|" in str(record.get("condition", "")):
            continue
        if record.get("condition") != "no_policy":
            continue
        seed = record.get("seed")
        if seed is None:
            continue
        case = record.get("metadata", {}).get("case", {})
        transform = case.get("transform", {}).get("name")
        action = case.get("action", {}).get("name")
        source = case.get("source", {}).get("name")
        key = (f"{source}|{transform}|{action}", int(seed))
        items[key] = record
    return items


def _mean(values: list[int | float]) -> float:
    return sum(float(value) for value in values) / len(values) if values else 0.0


def _bootstrap_mean_ci(values: list[int | float], samples: int, seed: int) -> tuple[float, float]:
    if samples < 1:
        raise ValueError("bootstrap_samples must be at least 1")
    generator = random.Random(seed)
    estimates = []
    for _ in range(samples):
        draw = [values[generator.randrange(len(values))] for _ in values]
        estimates.append(_mean(draw))
    estimates.sort()
    low = estimates[max(0, math.floor(0.025 * samples))]
    high = estimates[min(samples - 1, math.ceil(0.975 * samples) - 1)]
    return low, high


def _mcnemar_exact(left_only: int, right_only: int) -> float:
    discordant = left_only + right_only
    if discordant == 0:
        return 1.0
    tail = sum(math.comb(discordant, value) for value in range(0, min(left_only, right_only) + 1))
    return min(1.0, 2.0 * tail / (2**discordant))
