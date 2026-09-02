"""Run the controlled paired matrix and print aggregate metrics."""

from __future__ import annotations

import argparse
from pathlib import Path

from .experiment_runner import run_controlled_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repetitions", type=int, default=3)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/controlled-matrix"))
    args = parser.parse_args()
    summaries = run_controlled_matrix(args.output_dir, repetitions=args.repetitions)
    print("scenario,condition,repetitions,utility,attack_success,leak,unauthorized,blocked,violations")
    for summary in summaries:
        metrics = summary.metrics
        print(
            f"{summary.scenario},{summary.condition},{summary.repetitions},"
            f"{metrics['utility']:.3f},{metrics['attack_success']:.3f},"
            f"{metrics['sensitive_data_leak']:.3f},{metrics['unauthorized_side_effect']:.3f},"
            f"{metrics['blocked_actions']:.3f},{metrics['policy_violations']:.3f}"
        )
    print(f"logged_to={args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
