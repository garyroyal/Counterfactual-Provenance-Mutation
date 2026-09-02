"""Run deterministic multi-step and race-condition attack traces."""

from __future__ import annotations

import argparse
from pathlib import Path

from .composed_runner import run_composed_attack_matrix


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/composed-attacks-v1"))
    args = parser.parse_args()
    runs = run_composed_attack_matrix(args.output_dir)
    print(f"cases={len(runs)}")
    print(f"attack_families={len({run.attack for run in runs})}")
    print(f"policies={len({run.policy for run in runs})}")
    print(f"unsafe_protected_runs={sum(run.attack_execution_rate > 0 for run in runs if run.policy != 'no_policy')}")
    print(f"logged_to={args.output_dir.resolve()}")


if __name__ == "__main__":
    main()
