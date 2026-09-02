"""CLI entry point for the Redis-backed cross-process grant experiment."""

from __future__ import annotations

import argparse

from .cross_process_runner import run_redis_cross_process_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--redis-url", default="redis://127.0.0.1:6379/0")
    args = parser.parse_args()
    runs = run_redis_cross_process_matrix(args.output_dir, redis_url=args.redis_url)
    for run in runs:
        print(
            f"{run.policy}: executed={run.executed} blocked={run.blocked} "
            f"replay_violation={int(run.replay_violation)} record={run.record_id}"
        )


if __name__ == "__main__":
    main()
