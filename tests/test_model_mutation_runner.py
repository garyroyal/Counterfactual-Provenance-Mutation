import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.model_mutation_runner import _graph_args, run_model_mutation_matrix
from provenance_agent_eval.real_tool_runner import real_tool_cases


class ModelMutationRunnerTests(unittest.TestCase):
    def test_graph_detects_forgery_and_loss(self) -> None:
        case = next(item for item in real_tool_cases() if item.attack and item.target_tool == "send_message")
        for evidence in ("memory-loss", "rewrite-forged-user"):
            args, graph = _graph_args(case, evidence)
            node = next(node_id for node_id in graph.nodes if node_id != "root")
            self.assertFalse(graph.is_sound(node))
            self.assertTrue(args)

    def test_model_decision_is_replayed_across_conditions(self) -> None:
        class FakeResponse:
            content = '{"action":"send_message"}'
            latency_seconds = 0.01
            prompt_tokens = 1
            completion_tokens = 1

        class FakeClient:
            base_url = "fake"

            def __init__(self) -> None:
                self.calls = 0

            def chat(self, **_: object) -> FakeResponse:
                self.calls += 1
                return FakeResponse()

        with tempfile.TemporaryDirectory() as directory:
            client = FakeClient()
            summary = run_model_mutation_matrix(directory, model="fake", client=client, repetitions=1)
            self.assertEqual(client.calls, 6)
            self.assertEqual(summary["records"], 6 * 4 * 3)
            self.assertTrue(Path(directory, "progress.html").exists())


if __name__ == "__main__":
    unittest.main()
