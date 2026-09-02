"""Run the same paired model matrix across local or remote Ollama endpoints."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from .model_runner import generalized_risk_cases, matched_laundering_cases, representative_cases, run_model_matrix
from .ollama_client import OllamaClient


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=Path("artifacts/multi-model"))
    parser.add_argument("--repetitions", type=int, default=5)
    parser.add_argument(
        "--matrix",
        choices=("representative", "matched-laundering", "generalized-risk"),
        default="matched-laundering",
    )
    args = parser.parse_args()

    entries = json.loads(args.config.read_text(encoding="utf-8"))
    if not isinstance(entries, list) or not entries:
        raise ValueError("config must be a non-empty JSON array")
    cases = (
        matched_laundering_cases()
        if args.matrix == "matched-laundering"
        else generalized_risk_cases()
        if args.matrix == "generalized-risk"
        else representative_cases()
    )
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError("each config entry must be an object")
        name = str(entry["name"])
        model = str(entry["model"])
        base_url = str(entry.get("base_url", "http://127.0.0.1:11434"))
        client = OllamaClient(base_url)
        client.require_model(model)
        output_dir = args.output_root / name
        results = run_model_matrix(
            str(output_dir),
            model=model,
            repetitions=args.repetitions,
            cases=cases,
            client=client,
        )
        print(
            f"{name}: endpoint={base_url} model={model} runs={len(results)} "
            f"attack_requests={sum(result.model_attack_induction for result in results)} "
            f"logged_to={output_dir.resolve()}"
        )


if __name__ == "__main__":
    main()
