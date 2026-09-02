import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.experiment_log import ExperimentLogger, compare_metric


class ExperimentLogTests(unittest.TestCase):
    def test_metric_delta_marks_lower_attack_rate_as_improved(self) -> None:
        change = compare_metric("attack_success", 0.1, 0.4)
        self.assertEqual(change.direction, "down")
        self.assertEqual(change.assessment, "improved")

    def test_records_are_append_only_and_report_contains_delta(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            logger = ExperimentLogger(directory)
            baseline = logger.record(
                experiment="test", condition="baseline", metrics={"utility": True, "attack_success": 0.4}
            )
            logger.record(
                experiment="test",
                condition="protected",
                baseline_id=baseline.record_id,
                metrics={"utility": 0.9, "attack_success": 0.1},
            )
            records = Path(directory, "experiments.jsonl").read_text(encoding="utf-8").splitlines()
            self.assertEqual(len(records), 2)
            self.assertIn("-0.3", Path(directory, "report.md").read_text(encoding="utf-8"))
            second = json.loads(records[1])
            self.assertEqual(second["metric_changes"]["attack_success"]["assessment"], "improved")

    def test_lesson_requires_confidence_and_writes_review_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            logger = ExperimentLogger(directory)
            with self.assertRaises(ValueError):
                logger.lesson(
                    experiment="test",
                    observation="x",
                    evidence=("exp-0001",),
                    conclusion="y",
                    confidence="certain",
                )
            logger.lesson(
                experiment="test",
                observation="x",
                evidence=("exp-0001",),
                conclusion="y",
                confidence="medium",
            )
            self.assertIn("置信度：medium", Path(directory, "lessons.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
