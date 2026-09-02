"""Run the independent provenance benchmark matrix and print aggregates."""

from __future__ import annotations

import argparse
from pathlib import Path

from .benchmark_runner import run_orthogonal_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/orthogonal-matrix"))
    args = parser.parse_args()
    runs = run_orthogonal_matrix(args.output_dir, repetitions=args.repetitions)
    print(f"cases={len({run.case_id for run in runs})}")
    print(f"runs={len(runs)}")
    print(f"logged_to={args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
