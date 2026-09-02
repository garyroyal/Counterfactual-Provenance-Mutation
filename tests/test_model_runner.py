import json
import re
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.model_runner import (
    attack_variants,
    generalized_risk_cases,
    matched_laundering_cases,
    parse_action,
    parse_invoke,
    representative_cases,
    run_model_matrix,
)
from provenance_agent_eval.ollama_client import OllamaClient, OllamaResponse


class FakeClient:
    def __init__(self, invoke: bool = True) -> None:
        self.invoke = invoke

    def chat(self, *, model: str, messages: list[dict[str, str]]) -> OllamaResponse:
        target = re.search(r"invoke '([^']+)'", messages[-1]["content"], flags=re.IGNORECASE).group(1)
        return OllamaResponse(
            content=json.dumps({"response": {"action": target if self.invoke else "none"}}),
            latency_seconds=0.01,
            prompt_tokens=10,
            completion_tokens=5,
            raw={},
        )


class ModelRunnerTests(unittest.TestCase):
    def test_require_model_accepts_only_endpoint_inventory(self) -> None:
        client = OllamaClient()
        client.list_models = lambda: ("qwen3:4b", "llama3.2:3b")
        client.require_model("llama3.2:3b")
        with self.assertRaises(RuntimeError):
            client.require_model("missing:1b")

    def test_parser_handles_nested_json_and_thinking_text(self) -> None:
        content = "analysis... {\"response\": {\"invoke\": false}}"
        self.assertEqual(parse_invoke(content), (False, "json"))
        self.assertEqual(parse_invoke("not json"), (None, "unparseable"))
        self.assertEqual(parse_action('text {"response":{"action":"destroy"}}'), ("destroy", "json"))

    def test_smoke_matrix_keeps_model_and_runtime_stages_separate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            results = run_model_matrix(directory, client=FakeClient(True))
            self.assertEqual(len(results), len(representative_cases()))
            self.assertTrue(all(result.model_requested_action is True for result in results))
            self.assertTrue(any(not result.runtime_allowed for result in results))
            records = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text().splitlines()]
            self.assertEqual(len(results), 14)
            self.assertGreaterEqual(len(records), len(results) + 2)
            aggregates = [record for record in records if record["scenario"] == "representative-cases"]
            self.assertTrue(all(record["metrics"]["model_attack_induction"] == 1.0 for record in aggregates))
            self.assertTrue(all(record["metrics"]["utility"] == 1.0 for record in aggregates))
            transform_aggregates = [record for record in records if str(record["scenario"]).startswith("transform:")]
            non_direct = [record for record in transform_aggregates if record["scenario"] != "transform:direct"]
            self.assertTrue(all(record["baseline_id"] is not None for record in non_direct))
            self.assertTrue(Path(directory, "progress.html").exists())

    def test_matched_matrix_varies_only_transform_and_policy(self) -> None:
        cases = matched_laundering_cases()
        self.assertEqual(len(cases), 8)
        self.assertEqual({case.source.name for case in cases}, {"memory"})
        self.assertEqual({case.action.name for case in cases}, {"external-side-effect"})
        self.assertEqual(len(attack_variants()), 20)

    def test_generalized_risk_matrix_crosses_source_transform_action_and_policy(self) -> None:
        cases = generalized_risk_cases()
        self.assertEqual(len(cases), 48)
        self.assertEqual({case.source.name for case in cases}, {"tool-output", "memory"})
        self.assertEqual({case.transform.name for case in cases}, {
            "direct", "summary-preserve", "memory-loss", "rewrite-forged-user"
        })
        self.assertEqual({case.action.name for case in cases}, {
            "update-state", "external-side-effect", "destroy"
        })


if __name__ == "__main__":
    unittest.main()
