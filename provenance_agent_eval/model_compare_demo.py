"""Compare two or more completed model experiment directories."""

from __future__ import annotations

import argparse

from .model_compare import compare_model_runs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run", action="append", required=True, help="NAME=EXPERIMENT_DIRECTORY")
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--bootstrap-samples", type=int, default=5000)
    args = parser.parse_args()
    runs = dict(item.split("=", 1) for item in args.run)
    summary = compare_model_runs(args.output_dir, runs, bootstrap_samples=args.bootstrap_samples)
    for comparison in summary["comparisons"]:
        print(
            f"{comparison['left']} vs {comparison['right']}: "
            f"difference={comparison['rate_difference']:.3f} "
            f"CI95={tuple(comparison['bootstrap_ci_95'])} "
            f"McNemar-p={comparison['mcnemar_exact_p']:.6f}"
        )
    for effect in summary["transform_effects"]:
        print(
            f"{effect['model']} {effect['transform']} vs direct: "
            f"difference={effect['rate_difference']:.3f} "
            f"CI95={tuple(effect['bootstrap_ci_95'])} "
            f"McNemar-p={effect['mcnemar_exact_p']:.6f}"
        )


if __name__ == "__main__":
    main()
