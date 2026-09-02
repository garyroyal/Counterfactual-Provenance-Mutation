"""Run the local Qwen model on a balanced provenance smoke matrix."""

from __future__ import annotations

import argparse
from pathlib import Path

from .model_runner import generalized_risk_cases, matched_laundering_cases, run_model_matrix
from .ollama_client import OllamaClient


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="qwen3:4b")
    parser.add_argument("--base-url", default="http://127.0.0.1:11434")
    parser.add_argument("--repetitions", type=int, default=1)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts/model-smoke"))
    parser.add_argument(
        "--matrix",
        choices=("representative", "matched-laundering", "generalized-risk"),
        default="representative",
    )
    args = parser.parse_args()
    cases = (
        matched_laundering_cases()
        if args.matrix == "matched-laundering"
        else generalized_risk_cases()
        if args.matrix == "generalized-risk"
        else None
    )
    client = OllamaClient(args.base_url)
    client.require_model(args.model)
    results = run_model_matrix(
        str(args.output_dir), model=args.model, repetitions=args.repetitions, cases=cases, client=client
    )
    print(f"cases={len({result.case_id for result in results})}")
    print(f"runs={len(results)}")
    print(f"model_target_action_requests={sum(result.model_requested_action is True for result in results)}")
    print(f"runtime_attack_successes={sum(result.runtime_attack_success for result in results)}")
    print(f"logged_to={args.output_dir.resolve()}")
    print(f"endpoint={args.base_url}")


if __name__ == "__main__":
    main()
