"""Run the cross-layer generalized attack matrix."""

from __future__ import annotations

import argparse
from pathlib import Path

from .attack_runner import run_generalized_attack_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/generalized-attacks"))
    args = parser.parse_args()
    runs = run_generalized_attack_matrix(args.output_dir)
    print(f"cases={len(runs)}")
    print(f"attack_families={len({run.family for run in runs})}")
    print(f"attack_stages={len({run.stage for run in runs})}")
    print(f"source_aware_unsafe_allows={sum(run.actual_allowed and run.policy == 'source_aware' for run in runs)}")
    print(f"logged_to={args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
