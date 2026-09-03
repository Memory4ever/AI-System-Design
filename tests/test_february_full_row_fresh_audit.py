import unittest


class FebruaryFullRowFreshAuditTest(unittest.TestCase):
    def test_recovered_false_negatives_are_explicit(self):
        from scripts.audit_february_2026_full_row_semantics import PROMOTIONS

        required = {
            "2602.00942",
            "2602.01637",
            "2602.03338",
            "2602.07840",
            "2602.09369",
            "2602.10465",
            "2602.11510",
        }
        self.assertTrue(required <= set(PROMOTIONS))

    def test_every_decision_has_family_specific_evidence(self):
        from scripts.audit_february_2026_full_row_semantics import decision_for

        row = {
            "identity": "2602.00002v1",
            "arxiv_id": "2602.00002",
            "source_family_id": "SF-2026-ARXIV-2602-00002",
            "title": "Disentangled Interest Network for Out-of-Distribution CTR Prediction",
            "abstract": "We propose a CTR predictor for a single recommendation task and report AUC gains.",
            "screening_status": "pre_denominator_closure",
            "reason_code": "localized_quality_or_method_delta",
        }

        decision = decision_for("2026-02-04", row)

        self.assertEqual(decision["reviewer_decision"], "closure_confirmed")
        self.assertIn(row["title"], decision["reviewer_reason"])
        self.assertIn("CTR predictor", decision["reviewer_reason"])
        self.assertEqual(decision["title_abstract_read"], True)

    def test_every_promoted_owner_has_a_review_lens(self):
        from scripts import rebuild_february_2026_daily_evidence as evidence
        from scripts import rebuild_march_lane_c_full_replay as reviewlib
        from scripts.audit_february_2026_full_row_semantics import configure_evidence

        configure_evidence(evidence, reviewlib)

        self.assertFalse(set(evidence.AUTHOR_RETENTIONS.values()) - set(reviewlib.NARRATIVE_LENS))

    def test_every_promotion_is_force_reviewed_with_exact_section_overrides(self):
        from scripts import rebuild_february_2026_daily_evidence as evidence
        from scripts import rebuild_march_lane_c_full_replay as reviewlib
        from scripts.audit_february_2026_full_row_semantics import (
            PROMOTIONS,
            PROMOTION_SECTION_OVERRIDES,
            configure_evidence,
        )

        configure_evidence(evidence, reviewlib)

        self.assertEqual(set(PROMOTIONS), set(PROMOTION_SECTION_OVERRIDES))
        self.assertTrue(set(PROMOTIONS) <= evidence.FORCE_REVIEW_IDS)
        self.assertTrue(set(PROMOTIONS) <= set(evidence.FRESH_SECTION_OVERRIDES))

    def test_core_evidence_replay_loads_full_row_reopen_overlay(self):
        from scripts import rebuild_february_2026_daily_evidence as evidence
        from scripts.audit_february_2026_full_row_semantics import PROMOTIONS

        evidence.AUTHOR_RETENTIONS.pop("2602.00942", None)
        evidence.load_full_row_reopen_overlay()

        self.assertEqual(evidence.AUTHOR_RETENTIONS["2602.00942"], PROMOTIONS["2602.00942"])

    def test_identity_normalization_matches_reconciliation_form(self):
        from scripts.audit_february_2026_full_row_semantics import canonical_identity

        self.assertEqual(canonical_identity("2602.00942v1"), "2602.00942")
        self.assertEqual(canonical_identity("2602.00942"), "2602.00942")

    def test_books_decisions_close_every_recovered_family(self):
        from scripts.audit_february_2026_full_row_semantics import BOOKS_DECISIONS, PROMOTIONS

        self.assertEqual(set(BOOKS_DECISIONS), set(PROMOTIONS))
        self.assertEqual(sum(row["decision"] == "Integrate" for row in BOOKS_DECISIONS.values()), 12)
        self.assertEqual(sum(row["decision"] == "No Change — Existing Coverage" for row in BOOKS_DECISIONS.values()), 17)

    def test_integrations_have_canonical_markers(self):
        from scripts.audit_february_2026_full_row_semantics import BOOKS_DECISIONS, PROMOTIONS, ROOT, roadmap_owners

        owner_paths = {row["stable_node_id"]: row["path"] for row in roadmap_owners()}
        for arxiv_id, decision in BOOKS_DECISIONS.items():
            if decision["decision"] != "Integrate":
                continue
            family = f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}"
            self.assertIn(family, (ROOT / owner_paths[PROMOTIONS[arxiv_id]]).read_text())


if __name__ == "__main__":
    unittest.main()
