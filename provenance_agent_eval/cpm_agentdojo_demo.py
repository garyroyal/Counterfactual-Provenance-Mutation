"""Record AgentDojo episodes as CPM traces, then run the degradation sweep on them.

Requires the ``agentdojo`` package (see ``requirements-agentdojo.txt``); run with
the conda env's interpreter, e.g.::

    PYTHONPATH=. /opt/miniconda3/envs/agentdojo/bin/python -m provenance_agent_eval.cpm_agentdojo_demo \
        --suite slack --model qwen3:8b --base-url http://192.168.1.105:11434 \
        --output-dir artifacts/cpm-agentdojo-slack-qwen3-8b-v1

Use ``--episodes <dir>/episodes.jsonl`` to re-convert and re-sweep an existing
recording without touching the model.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .cpm import DefenseMechanism, MutationOperator, run_degradation_sweep
from .cpm.agentdojo_backend import (
    DEFAULT_ATTACK,
    DEFAULT_BENCHMARK_VERSION,
    collect_agentdojo_traces,
    episodes_to_traces,
    load_episodes,
    summarise_episodes,
)


def _csv(value: str | None) -> list[str] | None:
    if not value or value == "all":
        return None
    return [item.strip() for item in value.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--suite", default="slack")
    parser.add_argument("--model", default=None, help="Ollama model name (required unless --episodes is given)")
    parser.add_argument("--base-url", default="http://127.0.0.1:11434")
    parser.add_argument("--output-dir", required=True, help="directory for episodes.jsonl / traces.jsonl")
    parser.add_argument("--sweep-dir", default=None, help="degradation sweep directory (default: <output-dir>-sweep)")
    parser.add_argument("--user-tasks", default="all", help="comma-separated user task ids, or 'all'")
    parser.add_argument("--injection-tasks", default="all", help="comma-separated injection task ids, or 'all'")
    parser.add_argument("--attack", default=DEFAULT_ATTACK)
    parser.add_argument("--benchmark-version", default=DEFAULT_BENCHMARK_VERSION)
    parser.add_argument("--no-clean", action="store_true", help="skip the injection-free control episode per user task")
    parser.add_argument("--untrusted-policy", default="injection_sites", choices=("injection_sites", "all_tool_outputs"))
    parser.add_argument("--max-episodes", type=int, default=None)
    parser.add_argument("--no-resume", action="store_true", help="ignore an existing episodes.jsonl and re-record")
    parser.add_argument("--episodes", default=None, help="convert an existing episodes.jsonl instead of recording")
    parser.add_argument("--seeds", type=int, default=5)
    parser.add_argument("--rates", default="0,0.1,0.25,0.5,0.75,1")
    parser.add_argument("--skip-sweep", action="store_true")
    args = parser.parse_args()

    output = Path(args.output_dir)
    if args.episodes:
        episodes = list(load_episodes(args.episodes))
        traces = episodes_to_traces((e for e in episodes if e.error is None), untrusted_policy=args.untrusted_policy)
        output.mkdir(parents=True, exist_ok=True)
        with (output / "traces.jsonl").open("w", encoding="utf-8") as handle:
            for trace in traces:
                handle.write(json.dumps(trace.as_dict(), ensure_ascii=False) + "\n")
        summary = summarise_episodes(episodes, traces)
        (output / "summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    else:
        if not args.model:
            parser.error("--model is required when recording")
        traces, episodes = collect_agentdojo_traces(
            output,
            suite_name=args.suite,
            model=args.model,
            base_url=args.base_url,
            user_tasks=_csv(args.user_tasks),
            injection_tasks=_csv(args.injection_tasks),
            attack_name=args.attack,
            benchmark_version=args.benchmark_version,
            include_clean=not args.no_clean,
            untrusted_policy=args.untrusted_policy,
            max_episodes=args.max_episodes,
            resume=not args.no_resume,
        )
        summary = json.loads((output / "summary.json").read_text(encoding="utf-8"))
    print(json.dumps({key: value for key, value in summary.items() if key != "model_info"}, ensure_ascii=False))
    if args.skip_sweep or not traces:
        return
    sweep_dir = args.sweep_dir or f"{str(output).rstrip('/')}-sweep"
    result = run_degradation_sweep(
        sweep_dir,
        traces,
        operators=tuple(MutationOperator),
        defenses=tuple(DefenseMechanism),
        rates=[float(item) for item in args.rates.split(",") if item],
        seeds=args.seeds,
    )
    print(json.dumps({"sweep_dir": sweep_dir, "traces": result["traces"], "attack_traces": result["attack_traces"]}))


if __name__ == "__main__":
    main()
