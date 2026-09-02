import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.model_mutation_analysis import analyze_model_mutation_run
from provenance_agent_eval.model_mutation_runner import run_model_mutation_matrix


class ModelMutationAnalysisTests(unittest.TestCase):
    def test_analysis_reports_forgery_policy_gap(self) -> None:
        class Response:
            content = '{"action":"send_message"}'
            latency_seconds = 0.0
            prompt_tokens = None
            completion_tokens = None

        class Client:
            base_url = "fake"

            def chat(self, **_: object) -> Response:
                return Response()

        with tempfile.TemporaryDirectory() as root:
            run_dir = Path(root, "run")
            analysis_dir = Path(root, "analysis")
            run_model_mutation_matrix(run_dir, model="fake", client=Client(), repetitions=1)
            result = analyze_model_mutation_run(run_dir, analysis_dir, bootstrap_samples=100)
            forged = result["evidence"]["rewrite-forged-user"]
            self.assertEqual(forged["source_aware"]["side_effect_rate"], 1.0 / 3.0)
            self.assertEqual(forged["graph_aware"]["side_effect_rate"], 0.0)
            self.assertTrue(Path(analysis_dir, "model_mutation_analysis.json").exists())
            # The fake client always answers send_message, so 6 unique decisions
            # and exactly one induced attack decision are replayed everywhere.
            self.assertEqual(result["unique_model_decisions"], 6)
            self.assertEqual(result["induced_attack_decisions"], 1)
            comparison = next(
                item for item in result["comparisons"]
                if item["evidence"] == "rewrite-forged-user" and item["left"] == "source_aware" and item["right"] == "graph_aware"
            )
            self.assertEqual(comparison["paired_induced_cases"], 1)
            self.assertTrue(comparison["deterministic_given_decision"])
            self.assertNotIn("mcnemar_exact_p", comparison)

    def test_legitimate_task_blocked_under_degraded_evidence_is_reported_not_hidden(self) -> None:
        class Client:
            base_url = "fake"

            def chat(self, *, model: str, messages: list[dict[str, str]]) -> object:
                prompt = messages[-1]["content"]
                tool = next((name for name in ("update_ticket", "send_message", "delete_file") if f"'{name}'" in prompt), "none")

                class Response:
                    content = '{"action":"%s"}' % tool
                    latency_seconds = 0.0
                    prompt_tokens = None
                    completion_tokens = None

                return Response()

        with tempfile.TemporaryDirectory() as root:
            run_dir = Path(root, "run")
            run_model_mutation_matrix(run_dir, model="fake", client=Client(), repetitions=1)
            result = analyze_model_mutation_run(run_dir, Path(root, "analysis"), bootstrap_samples=10)
            loss = result["evidence"]["memory-loss"]
            # Every legitimate request was proposed by the model, and the
            # source-aware policies block all of them once evidence is lost.
            self.assertEqual(loss["source_aware"]["legitimate_requested_cases"], 3)
            self.assertEqual(loss["source_aware"]["safe_task_success_rate"], 0.0)
            self.assertEqual(loss["source_aware"]["legitimate_degraded_blocking_rate"], 1.0)
            self.assertEqual(loss["no_policy"]["safe_task_success_rate"], 1.0)
            # Sound evidence has no degraded-legitimate cases: N/A, not 0.0.
            self.assertIsNone(result["evidence"]["direct"]["source_aware"]["legitimate_degraded_blocking_rate"])


if __name__ == "__main__":
    unittest.main()
