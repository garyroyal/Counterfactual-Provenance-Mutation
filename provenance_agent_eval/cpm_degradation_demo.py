"""Run the CPM provenance-fidelity degradation sweep on the synthetic suite."""

from __future__ import annotations

import argparse
import json

from .cpm import DefenseMechanism, MutationOperator, run_degradation_sweep, synthetic_suite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--variants", type=int, default=4, help="variants per synthetic template")
    parser.add_argument("--seeds", type=int, default=3, help="schedules per stochastic rate")
    parser.add_argument("--rates", default="0,0.1,0.25,0.5,0.75,1", help="comma-separated provenance error rates")
    parser.add_argument("--operators", default=",".join(item.value for item in MutationOperator))
    parser.add_argument("--defenses", default=",".join(item.value for item in DefenseMechanism))
    parser.add_argument("--bootstrap-samples", type=int, default=2000)
    args = parser.parse_args()

    traces = synthetic_suite(variants=args.variants)
    summary = run_degradation_sweep(
        args.output_dir,
        traces,
        operators=[MutationOperator(item) for item in args.operators.split(",") if item],
        defenses=[DefenseMechanism(item) for item in args.defenses.split(",") if item],
        rates=[float(item) for item in args.rates.split(",") if item],
        seeds=args.seeds,
        bootstrap_samples=args.bootstrap_samples,
    )
    print(json.dumps({key: summary[key] for key in ("traces", "attack_traces", "operators", "defenses", "rates")}, ensure_ascii=False))
    print(f"wrote curves to {args.output_dir}/curves.md")


if __name__ == "__main__":
    main()
