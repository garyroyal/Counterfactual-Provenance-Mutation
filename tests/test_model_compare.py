import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.model_compare import compare_model_runs


class ModelCompareTests(unittest.TestCase):
    def test_paired_comparison_reports_effect_and_exact_test(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for model, outcomes in {"a": [1, 1, 1, 0], "b": [0, 0, 1, 0]}.items():
                model_dir = root / model
                model_dir.mkdir()
                records = []
                for seed, outcome in enumerate(outcomes):
                    records.append({
                        "experiment": "model-action-induction",
                        "condition": "no_policy",
                        "seed": seed,
                        "metrics": {"model_attack_induction": outcome},
                        "metadata": {"case": {
                            "source": {"name": "memory"},
                            "transform": {"name": "memory-loss"},
                            "action": {"name": "external-side-effect"},
                        }},
                    })
                (model_dir / "experiments.jsonl").write_text(
                    "".join(json.dumps(record) + "\n" for record in records), encoding="utf-8"
                )
            summary = compare_model_runs(root / "comparison", {"a": root / "a", "b": root / "b"}, bootstrap_samples=200)
            comparison = summary["comparisons"][0]
            self.assertEqual(comparison["paired_observations"], 4)
            self.assertEqual(comparison["rate_difference"], 0.5)
            self.assertEqual(comparison["mcnemar_discordant_left"], 2)
            self.assertEqual(comparison["mcnemar_discordant_right"], 0)
            self.assertTrue((root / "comparison" / "comparison.json").exists())


if __name__ == "__main__":
    unittest.main()
