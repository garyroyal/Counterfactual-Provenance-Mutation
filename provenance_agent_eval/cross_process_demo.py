"""CLI entry point for the cross-process grant experiment."""

from __future__ import annotations

import argparse

from .cross_process_runner import run_cross_process_grant_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    runs = run_cross_process_grant_matrix(args.output_dir)
    for run in runs:
        print(
            f"{run.policy}: executed={run.executed} blocked={run.blocked} "
            f"replay_violation={int(run.replay_violation)} record={run.record_id}"
        )


if __name__ == "__main__":
    main()
