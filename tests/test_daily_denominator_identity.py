import unittest

from scripts.rebuild_february_2026_daily_evidence import sha_ids
from scripts.repair_empty_daily_denominators import denominator_id


class DailyDenominatorIdentityTests(unittest.TestCase):
    def test_empty_denominator_is_bound_to_report_date(self):
        self.assertNotEqual(sha_ids([], "2026-02-01"), sha_ids([], "2026-02-02"))

    def test_candidate_order_does_not_change_denominator(self):
        self.assertEqual(
            sha_ids(["2602.00002", "2602.00001"], "2026-02-04"),
            sha_ids(["2602.00001", "2602.00002"], "2026-02-04"),
        )

    def test_repair_helper_uses_the_same_empty_denominator_contract(self):
        self.assertEqual(
            denominator_id("2026-02-01"),
            sha_ids([], "2026-02-01"),
        )


if __name__ == "__main__":
    unittest.main()
