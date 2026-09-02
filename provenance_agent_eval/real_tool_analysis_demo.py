"""Analyze paired sandbox real-tool runs."""

from __future__ import annotations

import argparse

from .real_tool_analysis import analyze_real_tool_runs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="append", required=True, help="NAME=EXPERIMENT_DIRECTORY")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    summary = analyze_real_tool_runs(args.output_dir, dict(item.split("=", 1) for item in args.run))
    for model in summary["models"]:
        print(
            f"{model['model']}: induction={model['model_attack_induction_rate']:.4f} "
            f"no_policy_effect={model['no_policy_side_effect_rate']:.4f} "
            f"source_aware_effect={model['source_aware_side_effect_rate']:.4f} "
            f"safe_utility={model['safe_task_success_rate']:.4f}"
        )
    for comparison in summary["cross_model"]:
        print(
            f"{comparison['left']} vs {comparison['right']}: "
            f"difference={comparison['rate_difference']:.4f} "
            f"CI95={tuple(comparison['bootstrap_ci_95'])} "
            f"p={comparison['mcnemar_exact_p']:.6g}"
        )


if __name__ == "__main__":
    main()
