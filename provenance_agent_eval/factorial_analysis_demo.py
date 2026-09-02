"""Analyze completed orthogonal model factorial runs."""

from __future__ import annotations

import argparse

from .factorial_analysis import analyze_factorial_runs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="append", required=True, help="NAME=EXPERIMENT_DIRECTORY")
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    runs = dict(item.split("=", 1) for item in args.run)
    summary = analyze_factorial_runs(args.output_dir, runs)
    for model in summary["models"]:
        effect = model["policy_effect"]
        print(
            f"{model['model']}: presentations={model['presentation_rates']} "
            f"policy_difference={effect['source_aware_minus_no_policy']:.4f} "
            f"policy_p={effect['mcnemar_exact_p']:.6g}"
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
