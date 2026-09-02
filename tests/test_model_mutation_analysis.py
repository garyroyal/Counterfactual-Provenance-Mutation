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


if __name__ == "__main__":
    unittest.main()
