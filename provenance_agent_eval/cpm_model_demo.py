"""Collect model-proposed tool calls as CPM traces, then run the degradation sweep on them."""

from __future__ import annotations

import argparse
import json

from .cpm import DefenseMechanism, MutationOperator, run_degradation_sweep
from .cpm.model_traces import collect_model_traces
from .ollama_client import OllamaClient


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:11434")
    parser.add_argument("--output-dir", required=True, help="directory for model decisions and traces")
    parser.add_argument("--sweep-dir", default=None, help="directory for the degradation sweep (default: <output-dir>-sweep)")
    parser.add_argument("--variants", type=int, default=2)
    parser.add_argument("--phrasings", type=int, default=20)
    parser.add_argument("--templates", default=None, help="comma-separated template names (default: all)")
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--rates", default="0,0.1,0.25,0.5,0.75,1")
    parser.add_argument("--skip-sweep", action="store_true")
    args = parser.parse_args()

    client = OllamaClient(args.base_url)
    client.require_model(args.model)
    traces, decisions = collect_model_traces(
        args.output_dir,
        model=args.model,
        client=client,
        templates=args.templates.split(",") if args.templates else None,
        variants=args.variants,
        phrasings=args.phrasings,
    )
    induced = sum(bool(t.metadata["attacker_induced"]) for t in traces)
    print(json.dumps({"model": args.model, "decisions": len(decisions), "side_effect_traces": len(traces), "attacker_induced": induced}))
    if args.skip_sweep or not traces:
        return
    sweep_dir = args.sweep_dir or f"{args.output_dir.rstrip('/')}-sweep"
    summary = run_degradation_sweep(
        sweep_dir,
        traces,
        operators=tuple(MutationOperator),
        defenses=tuple(DefenseMechanism),
        rates=[float(item) for item in args.rates.split(",") if item],
        seeds=args.seeds,
    )
    print(json.dumps({"sweep_dir": sweep_dir, "traces": summary["traces"], "attack_traces": summary["attack_traces"]}))


if __name__ == "__main__":
    main()
