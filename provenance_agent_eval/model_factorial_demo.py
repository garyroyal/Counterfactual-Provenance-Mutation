"""Run the orthogonal model-presentation × provenance-evidence experiment."""

from __future__ import annotations

import argparse

from .model_factorial_runner import run_model_provenance_factorial
from .ollama_client import OllamaClient


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:11434")
    parser.add_argument("--repetitions", type=int, default=20)
    parser.add_argument("--output-dir", required=True)
    args = parser.parse_args()
    client = OllamaClient(args.base_url)
    client.require_model(args.model)
    summary = run_model_provenance_factorial(
        args.output_dir,
        model=args.model,
        client=client,
        repetitions=args.repetitions,
    )
    print(
        f"model={summary.model} model_calls={summary.model_calls} "
        f"runtime_evaluations={summary.runtime_evaluations} "
        f"induced_actions={summary.induced_actions} "
        f"runtime_attack_successes={summary.runtime_attack_successes}"
    )


if __name__ == "__main__":
    main()
