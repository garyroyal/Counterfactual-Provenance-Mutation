import unittest

from provenance_agent_eval.benchmark_schema import PolicyKind, build_matrix
from provenance_agent_eval.core import RiskLevel


class BenchmarkSchemaTests(unittest.TestCase):
    def test_default_matrix_is_factorial_and_ids_are_stable(self) -> None:
        first = build_matrix()
        second = build_matrix()

        self.assertEqual(len(first), 3 * 4 * 4 * 2)
        self.assertEqual(tuple(case.case_id for case in first), tuple(case.case_id for case in second))
        self.assertEqual(len({case.case_id for case in first}), len(first))

    def test_ground_truth_distinguishes_safe_user_and_external_sources(self) -> None:
        cases = build_matrix()
        user_case = next(
            case
            for case in cases
            if case.source.name == "user"
            and case.transform.name == "direct"
            and case.action.risk is RiskLevel.EXTERNAL_SIDE_EFFECT
            and case.policy is PolicyKind.SOURCE_AWARE
        )
        external_case = next(
            case
            for case in cases
            if case.source.name == "tool-output"
            and case.transform.name == "direct"
            and case.action.risk is RiskLevel.EXTERNAL_SIDE_EFFECT
            and case.policy is PolicyKind.SOURCE_AWARE
        )

        self.assertTrue(user_case.expected_allowed)
        self.assertFalse(external_case.expected_allowed)

    def test_loss_and_forgery_are_reflected_in_observed_ground_truth(self) -> None:
        cases = build_matrix()
        loss = next(case for case in cases if case.transform.name == "memory-loss")
        forged = next(case for case in cases if case.transform.name == "rewrite-forged-user")

        self.assertEqual(loss.expected_root_source_ids, (loss.source.source.source_id,))
        self.assertEqual(loss.expected_observed_source_ids, ())
        self.assertEqual(forged.expected_observed_source_ids, ("user",))
        self.assertNotEqual(forged.expected_root_source_ids, forged.expected_observed_source_ids)

    def test_read_only_actions_are_allowed_under_both_policies(self) -> None:
        cases = build_matrix()
        reads = [case for case in cases if case.action.risk is RiskLevel.READ_ONLY]
        self.assertTrue(reads)
        self.assertTrue(all(case.expected_allowed for case in reads))

    def test_ground_truth_is_independent_of_policy(self) -> None:
        cases = build_matrix()
        unsafe = [
            case
            for case in cases
            if case.source.name == "tool-output"
            and case.transform.name == "direct"
            and case.action.risk is RiskLevel.EXTERNAL_SIDE_EFFECT
        ]
        self.assertEqual({case.expected_allowed for case in unsafe}, {False})

    def test_case_serialization_uses_enum_values(self) -> None:
        case = build_matrix()[0]
        serialized = case.as_dict()

        self.assertEqual(serialized["policy"], case.policy.value)
        self.assertEqual(serialized["action"]["risk"], case.action.risk.value)
        self.assertEqual(serialized["transform"]["kind"], case.transform.kind.value)


if __name__ == "__main__":
    unittest.main()
