"""Compact cross-run comparison of CPM degradation sweeps.

Reads ``curves.json`` from one or more sweep directories and prints, per
operator x defense, ASR and FBR at selected mutation rates (with cluster
bootstrap CIs), so runs on different trace sources can be compared side by side::

    PYTHONPATH=. python3 -m provenance_agent_eval.cpm_results_table \
        artifacts/cpm-model-traces-qwen3-4b-v1-sweep artifacts/cpm-agentdojo-slack-qwen3-8b-v1-sweep
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Iterable


def _fmt(point: dict[str, Any] | None, key: str) -> str:
    if point is None:
        return "-"
    item = point.get(key)
    if not item or not item.get("trials"):
        return "n/a"
    return f"{item['rate']:.2f} [{item['cluster_ci_low']:.2f},{item['cluster_ci_high']:.2f}]"


def load_sweep(path: str | Path) -> dict[str, Any]:
    return json.loads((Path(path) / "curves.json").read_text(encoding="utf-8"))


def table(sweeps: dict[str, dict[str, Any]], *, rates: Iterable[float] = (0.0, 0.5, 1.0), operators: Iterable[str] | None = None, metric: str = "attack_success") -> str:
    rate_items = tuple(rates)
    lines = []
    label = "ASR" if metric == "attack_success" else "FBR"
    first = next(iter(sweeps.values()))
    op_items = tuple(operators or first["curves"].keys())
    header = "| operator | defense | " + " | ".join(f"{name} {label}@{rate:g}" for name in sweeps for rate in rate_items) + " |"
    lines.append(header)
    lines.append("|" + "---|" * (2 + len(sweeps) * len(rate_items)))
    for operator in op_items:
        for defense in first["defenses"]:
            cells = []
            for run in sweeps.values():
                points = {round(p["rate"], 6): p for p in run["curves"].get(operator, {}).get(defense, [])}
                cells.extend(_fmt(points.get(round(rate, 6)), metric) for rate in rate_items)
            lines.append(f"| `{operator}` | {defense} | " + " | ".join(cells) + " |")
    return "\n".join(lines)


def header_table(sweeps: dict[str, dict[str, Any]]) -> str:
    lines = ["| run | traces | attack traces | benign traces | seeds/stochastic rate |", "|---|---:|---:|---:|---:|"]
    for name, run in sweeps.items():
        lines.append(f"| {name} | {run['traces']} | {run['attack_traces']} | {run['traces'] - run['attack_traces']} | {run['seeds_per_stochastic_rate']} |")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("sweeps", nargs="+", help="sweep directories, optionally as name=path")
    parser.add_argument("--rates", default="0,0.5,1")
    parser.add_argument("--operators", default=None, help="comma-separated operator subset")
    args = parser.parse_args()
    sweeps = {}
    for item in args.sweeps:
        name, _, path = item.rpartition("=") if "=" in item else ("", "", item)
        sweeps[name or Path(path).name] = load_sweep(path)
    rates = [float(x) for x in args.rates.split(",") if x]
    operators = args.operators.split(",") if args.operators else None
    print(header_table(sweeps))
    print()
    print("### ASR (attack traces with >=1 unsafe side effect)")
    print(table(sweeps, rates=rates, operators=operators, metric="attack_success"))
    print()
    print("### FBR (benign traces with >=1 legitimate action blocked)")
    print(table(sweeps, rates=rates, operators=operators, metric="false_blocking"))


if __name__ == "__main__":
    main()
