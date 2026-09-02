import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.factorial_analysis import analyze_factorial_runs
from provenance_agent_eval.model_factorial_runner import run_model_provenance_factorial
from provenance_agent_eval.ollama_client import OllamaResponse


class AnalysisFakeClient:
    base_url = "fake://analysis"

    def chat(self, *, model: str, messages: list[dict[str, str]]) -> OllamaResponse:
        return OllamaResponse('{"action":"external_side_effect"}', 0.01, 10, 3, {})


class FactorialAnalysisTests(unittest.TestCase):
    def test_analysis_separates_presentation_and_policy_effects(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_dir = Path(directory) / "run"
            run_model_provenance_factorial(run_dir, model="fake", client=AnalysisFakeClient(), repetitions=2)
            summary = analyze_factorial_runs(Path(directory) / "analysis", {"fake": run_dir}, bootstrap_samples=100)
            model = summary["models"][0]
            self.assertEqual(model["model_decisions"], 8)
            self.assertEqual(model["policy_effect"]["no_policy_attack_rate"], 1.0)
            self.assertEqual(model["policy_effect"]["source_aware_attack_rate"], 0.0)


if __name__ == "__main__":
    unittest.main()
