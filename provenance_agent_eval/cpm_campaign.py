"""Run the CPM law campaign (H1-H7) and write per-hypothesis tables.

Example::

    PYTHONPATH=. python3 -m provenance_agent_eval.cpm_campaign \
        --root artifacts/cpm-campaign-v1 \
        --model-run qwen3-4b=artifacts/cpm-model-traces-qwen3-4b-v1 \
        --model-run qwen3-8b=artifacts/cpm-model-traces-qwen3-8b-4090-v1 \
        --model-run llama31-8b=artifacts/cpm-model-traces-llama31-8b-4090-v1
"""

from __future__ import annotations

import argparse
import json

from .cpm.campaign import run_campaign


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", required=True, help="artifacts directory for the whole campaign")
    parser.add_argument("--model-run", action="append", default=[], help="name=path to a cpm-model-traces directory (repeatable)")
    parser.add_argument("--hypotheses", default="h1,h3,h5,h7", help="subset of h1 (with h2,h6), h3 (with h4), h5, h7")
    parser.add_argument("--variants", type=int, default=8, help="variants per mixed-trust template")
    parser.add_argument("--channels", type=int, default=4, help="channels per parametric (depth, k) cell")
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--rates", default="0,0.05,0.1,0.25,0.5,0.75,1")
    parser.add_argument("--bootstrap", type=int, default=1000)
    parser.add_argument("--execution-copies", type=int, default=4)
    args = parser.parse_args()

    model_runs = {}
    for item in args.model_run:
        name, _, path = item.partition("=")
        model_runs[name] = path
    summary = run_campaign(
        args.root,
        model_runs=model_runs or None,
        variants=args.variants,
        seeds=args.seeds,
        rates=[float(x) for x in args.rates.split(",") if x],
        bootstrap=args.bootstrap,
        channels=args.channels,
        execution_copies=args.execution_copies,
        hypotheses=[item.strip() for item in args.hypotheses.split(",") if item.strip()],
    )
    print(json.dumps({key: (value if not isinstance(value, dict) else sorted(value)) for key, value in summary.items()}, ensure_ascii=False))
    print(f"wrote {args.root}/campaign_summary.json")


if __name__ == "__main__":
    main()
