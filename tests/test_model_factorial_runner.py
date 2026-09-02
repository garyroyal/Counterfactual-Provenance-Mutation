import tempfile
import unittest

from provenance_agent_eval.model_factorial_runner import run_model_provenance_factorial
from provenance_agent_eval.ollama_client import OllamaResponse


class FactorialFakeClient:
    base_url = "fake://factorial"

    def chat(self, *, model: str, messages: list[dict[str, str]]) -> OllamaResponse:
        return OllamaResponse(
            content='{"action":"external_side_effect"}',
            latency_seconds=0.01,
            prompt_tokens=10,
            completion_tokens=3,
            raw={},
        )


class ModelFactorialTests(unittest.TestCase):
    def test_model_decisions_are_reused_across_evidence_and_policy(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            summary = run_model_provenance_factorial(
                directory,
                model="fake",
                client=FactorialFakeClient(),
                repetitions=2,
            )
            self.assertEqual(summary.model_calls, 8)
            self.assertEqual(summary.runtime_evaluations, 64)
            self.assertEqual(summary.induced_actions, 8)
            self.assertEqual(summary.runtime_attack_successes, 32)


if __name__ == "__main__":
    unittest.main()
