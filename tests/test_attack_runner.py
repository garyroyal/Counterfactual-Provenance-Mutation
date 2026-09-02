import json
import tempfile
import unittest
from pathlib import Path

from provenance_agent_eval.attack_runner import run_generalized_attack_case, run_generalized_attack_matrix
from provenance_agent_eval.attack_schema import (
    AttackFamily,
    AttackStage,
    build_generalized_attack_matrix,
    default_attack_profiles,
)
from provenance_agent_eval.benchmark_schema import PolicyKind


class GeneralizedAttackTests(unittest.TestCase):
    def test_taxonomy_spans_layers_and_is_not_injection_only(self) -> None:
        profiles = default_attack_profiles()
        self.assertEqual(len(profiles), 10)
        self.assertGreaterEqual(len({profile.stage for profile in profiles}), 5)
        self.assertEqual(sum(profile.family is AttackFamily.INSTRUCTION_INJECTION for profile in profiles), 1)
        self.assertTrue(any(not profile.model_mediated for profile in profiles))

    def test_matrix_pairs_every_attack_across_policies(self) -> None:
        cases = build_generalized_attack_matrix()
        self.assertEqual(len(cases), 20)
        for family in AttackFamily:
            family_cases = [case for case in cases if case.attack.family is family]
            self.assertEqual({case.policy for case in family_cases}, set(PolicyKind))

    def test_source_aware_blocks_provenance_attacks_but_exposes_scope_gaps(self) -> None:
        cases = build_generalized_attack_matrix()
        by_family = {
            case.attack.family: run_generalized_attack_case(case)
            for case in cases
            if case.policy is PolicyKind.SOURCE_AWARE
        }
        for family in (
            AttackFamily.SOURCE_LOSS,
            AttackFamily.SOURCE_FORGERY,
            AttackFamily.ARGUMENT_REBINDING,
            AttackFamily.DATA_POISONING,
            AttackFamily.MEMORY_POISONING,
            AttackFamily.DELEGATION_SPOOFING,
            AttackFamily.DESTINATION_SUBSTITUTION,
        ):
            self.assertFalse(by_family[family]["actual_allowed"], family.value)
        self.assertFalse(by_family[AttackFamily.CAPABILITY_SCOPE_ESCALATION]["actual_allowed"])
        self.assertFalse(by_family[AttackFamily.AUTHORIZATION_REPLAY]["actual_allowed"])

    def test_full_matrix_logs_aggregates_and_policy_gaps(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            runs = run_generalized_attack_matrix(directory)
            records = [json.loads(line) for line in Path(directory, "experiments.jsonl").read_text().splitlines()]
            self.assertEqual(len(runs), 20)
            source_aware_gaps = [run for run in runs if run.policy == "source_aware" and run.actual_allowed]
            self.assertEqual(source_aware_gaps, [])
            aggregates = [record for record in records if record["scenario"] == "all-attack-families"]
            protected = next(record for record in aggregates if record["condition"] == "source_aware-aggregate")
            self.assertEqual(protected["metrics"]["attack_execution_rate"], 0.0)
            self.assertEqual(protected["metrics"]["authorization_soundness"], 1.0)
            self.assertTrue(Path(directory, "progress.html").exists())


if __name__ == "__main__":
    unittest.main()
