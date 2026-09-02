import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.cross_process_runner import (
    CROSS_PROCESS_POLICIES,
    run_cross_process_grant_case,
    run_cross_process_grant_matrix,
)


class CrossProcessGrantTests(unittest.TestCase):
    def test_process_local_store_allows_cross_process_replay(self) -> None:
        result = run_cross_process_grant_case("process_local_atomic")
        self.assertEqual(result["metrics"]["executed_actions"], 2)
        self.assertEqual(result["metrics"]["successful_grant_replays"], 1)
        self.assertEqual(result["metrics"]["replay_violation"], 1)

    def test_sqlite_store_allows_only_one_execution(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = run_cross_process_grant_case(
                "sqlite_atomic", sqlite_path=Path(directory) / "nonces.sqlite3"
            )
        self.assertEqual(result["metrics"]["executed_actions"], 1)
        self.assertEqual(result["metrics"]["blocked_actions"], 1)
        self.assertEqual(result["metrics"]["successful_grant_replays"], 0)
        self.assertEqual(result["metrics"]["authorization_soundness"], 1.0)

    def test_matrix_logs_cross_process_aggregates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runs = run_cross_process_grant_matrix(directory)
            records = [
                json.loads(line)
                for line in Path(directory, "experiments.jsonl").read_text(encoding="utf-8").splitlines()
            ]
            self.assertEqual({run.policy for run in runs}, set(CROSS_PROCESS_POLICIES))
            self.assertEqual(len(records), 5)
            sqlite = next(record for record in records if record["condition"] == "sqlite_atomic-aggregate")
            self.assertEqual(sqlite["metrics"]["successful_grant_replays"], 0.0)
            self.assertEqual(sqlite["metrics"]["authorization_soundness"], 1.0)
            self.assertTrue(Path(directory, "progress.html").exists())


if __name__ == "__main__":
    unittest.main()
