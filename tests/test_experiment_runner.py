import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.experiment_runner import run_controlled_matrix


class ExperimentRunnerTests(unittest.TestCase):
    def test_matrix_writes_raw_aggregate_and_lesson_records(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            summaries = run_controlled_matrix(directory, repetitions=2)
            records = Path(directory, "experiments.jsonl").read_text(encoding="utf-8").splitlines()
            lessons = Path(directory, "lessons.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(summaries), 6)
            self.assertEqual(len(records), 18)
            self.assertEqual(len(lessons), 3)
            self.assertIn("policy_violations", Path(directory, "report.md").read_text(encoding="utf-8"))
            for summary in summaries:
                if summary.condition == "source-aware-authorization":
                    self.assertEqual(summary.metrics["utility"], 1.0)
                    self.assertEqual(summary.metrics["attack_success"], 0.0)

    def test_matrix_rejects_zero_repetitions(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                run_controlled_matrix(directory, repetitions=0)


if __name__ == "__main__":
    unittest.main()
