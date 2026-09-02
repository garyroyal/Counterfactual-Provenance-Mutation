import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.composed_runner import (
    POLICIES,
    ComposedAttackCase,
    CompositionAttack,
    build_composed_attack_matrix,
    run_composed_attack_case,
    run_composed_attack_matrix,
)


class ComposedAttackTests(unittest.TestCase):
    def test_matrix_covers_compositions_and_policies(self) -> None:
        cases = build_composed_attack_matrix()
        self.assertEqual(len(cases), len(tuple(CompositionAttack)) * len(POLICIES))
        self.assertEqual({case.policy for case in cases}, set(POLICIES))

    def test_replay_and_scope_chain_are_partially_executed_only_as_safe_prefix(self) -> None:
        for attack in (CompositionAttack.GRANT_REPLAY_CHAIN, CompositionAttack.SCOPE_ESCALATION_CHAIN):
            result = run_composed_attack_case(ComposedAttackCase("case", attack, "grant_aware"))
            self.assertEqual(result["metrics"]["attack_execution_rate"], 0.0)
            self.assertEqual(result["metrics"]["authorization_completeness"], 1.0)
            self.assertEqual(result["metrics"]["executed_actions"], 1)
            self.assertEqual(result["metrics"]["partial_execution"], 1)

    def test_revalidation_closes_resource_substitution_race(self) -> None:
        baseline = run_composed_attack_case(
            ComposedAttackCase("case", CompositionAttack.RESOURCE_SUBSTITUTION_RACE, "grant_aware")
        )
        protected = run_composed_attack_case(
            ComposedAttackCase("case", CompositionAttack.RESOURCE_SUBSTITUTION_RACE, "grant_aware_revalidated")
        )
        self.assertEqual(baseline["metrics"]["stale_evidence_acceptance"], 1)
        self.assertEqual(baseline["metrics"]["attack_execution_rate"], 1.0)
        self.assertEqual(protected["metrics"]["stale_evidence_acceptance"], 0)
        self.assertEqual(protected["metrics"]["attack_blocking_rate"], 1.0)

    def test_matrix_logs_trace_metrics_and_aggregates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runs = run_composed_attack_matrix(directory)
            records = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text().splitlines()]
            self.assertEqual(len(runs), 15)
            self.assertEqual(len(records), 18)
            aggregate = next(record for record in records if record["scenario"] == "all-composed-attacks" and record["condition"] == "grant_aware-aggregate")
            self.assertEqual(aggregate["metrics"]["attack_execution_rate"], 0.2)
            self.assertEqual(aggregate["metrics"]["partial_execution_rate"], 0.4)
            hardened = next(record for record in records if record["scenario"] == "all-composed-attacks" and record["condition"] == "grant_aware_revalidated-aggregate")
            self.assertEqual(hardened["metrics"]["attack_execution_rate"], 0.0)
            self.assertTrue(Path(directory, "progress.html").exists())


if __name__ == "__main__":
    unittest.main()
