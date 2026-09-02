"""Run the threaded single-use grant replay experiment."""

from __future__ import annotations

import argparse
from pathlib import Path

from .concurrency_runner import run_concurrent_grant_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/concurrent-grant-v1"))
    args = parser.parse_args()
    runs = run_concurrent_grant_matrix(args.output_dir)
    print(f"policies={len(runs)}")
    print(f"replay_violations={sum(run.replay_violation for run in runs if run.policy != 'no_policy')}")
    print(f"logged_to={args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
