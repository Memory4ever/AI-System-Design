import unittest

from scripts.audit_april24_30_denominator import challenge_reasons


class DenominatorChallengeTests(unittest.TestCase):
    def test_flags_explicit_system_ownership_change(self):
        row = {
            "title": "A runtime for distributed KV cache scheduling",
            "abstract": (
                "We introduce a runtime that moves KV cache ownership across nodes "
                "and schedules prefill and decode under latency constraints."
            ),
            "screening_status": "pre_denominator_closed",
        }
        reasons = challenge_reasons(row)
        self.assertIn("inference_state_or_runtime", reasons)
        self.assertIn("distributed_control_or_communication", reasons)

    def test_does_not_reopen_retained_candidate(self):
        row = {
            "title": "Distributed KV cache runtime",
            "abstract": "A distributed scheduler for KV cache state.",
            "screening_status": "retained_candidate",
        }
        self.assertEqual([], challenge_reasons(row))

    def test_withdrawn_is_not_a_candidate_challenge(self):
        row = {
            "title": "Distributed KV cache runtime",
            "abstract": "This paper has been withdrawn.",
            "screening_status": "withdrawn_primary_source",
        }
        self.assertEqual([], challenge_reasons(row))


if __name__ == "__main__":
    unittest.main()
