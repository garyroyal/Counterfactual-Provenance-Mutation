import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.concurrency_runner import (
    CONCURRENT_POLICIES,
    run_concurrent_grant_case,
    run_concurrent_grant_matrix,
)


class ConcurrentGrantTests(unittest.TestCase):
    def test_racey_consumption_replays_single_use_grant(self) -> None:
        result = run_concurrent_grant_case("grant_aware_racey")
        self.assertEqual(result["metrics"]["executed_actions"], 2)
        self.assertEqual(result["metrics"]["successful_grant_replays"], 1)
        self.assertEqual(result["metrics"]["replay_violation"], 1)

    def test_atomic_consumption_keeps_one_legal_execution(self) -> None:
        result = run_concurrent_grant_case("grant_aware_atomic")
        self.assertEqual(result["metrics"]["executed_actions"], 1)
        self.assertEqual(result["metrics"]["blocked_actions"], 1)
        self.assertEqual(result["metrics"]["replay_violation"], 0)
        self.assertEqual(result["metrics"]["authorization_completeness"], 1.0)

    def test_matrix_logs_baseline_and_hardened_aggregates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runs = run_concurrent_grant_matrix(directory)
            records = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text().splitlines()]
            self.assertEqual({run.policy for run in runs}, set(CONCURRENT_POLICIES))
            self.assertEqual(len(records), 5)
            race = next(record for record in records if record["condition"] == "grant_aware_racey-aggregate")
            atomic = next(record for record in records if record["condition"] == "grant_aware_atomic-aggregate")
            self.assertEqual(race["metrics"]["successful_grant_replays"], 1.0)
            self.assertEqual(atomic["metrics"]["successful_grant_replays"], 0.0)
            self.assertEqual(atomic["metrics"]["authorization_completeness"], 1.0)
            self.assertTrue(Path(directory, "progress.html").exists())


if __name__ == "__main__":
    unittest.main()
