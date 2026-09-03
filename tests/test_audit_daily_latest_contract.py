import tempfile
import unittest
from pathlib import Path

from scripts.audit_daily_latest_contract import (
    SourcePacketSignals,
    _arxiv_receipt_due,
    _display_output_path,
    classify_latest_contract,
    discover_daily_reports,
    source_packet_signals,
    next_recovery_action,
)


class DailyLatestContractAuditTests(unittest.TestCase):
    def test_discovers_only_formal_daily_paths(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            daily = root / "papers/2026/08/25/README.md"
            weekly = root / "papers/2026/weekly/2026-W35/README.md"
            source_note = root / "papers/2026/08/_sources/README.md"
            for path in (daily, weekly, source_note):
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("placeholder\n", encoding="utf-8")

            self.assertEqual(discover_daily_reports(root), [daily])

    def test_missing_source_packet_reopens_coverage(self):
        issues = classify_latest_contract(
            validator_errors=[],
            candidate_count=2,
            review_count=2,
            semantic_scopes={"coverage": "passed", "evidence": "passed", "deep_analysis_selection": "passed", "books": "passed"},
            signals=SourcePacketSignals(),
        )
        self.assertIn("source_packet_missing", issues)
        self.assertIn("screening_ledger_missing", issues)

    def test_source_packet_is_resolved_from_the_report_month(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "papers/2026/06/03/README.md"
            packet = root / "papers/2026/06/_sources/daily-20260603"
            report.parent.mkdir(parents=True)
            packet.mkdir(parents=True)
            report.write_text("# Daily\n", encoding="utf-8")
            (packet / "inventory.json").write_text("{}\n", encoding="utf-8")

            signals, refs = source_packet_signals(root, report, report.read_text())

            self.assertTrue(signals.packet_present)
            self.assertIn("papers/2026/06/_sources/daily-20260603", refs)

    def test_zero_byte_packet_is_not_treated_as_evidence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "papers/2026/08/01/README.md"
            packet = root / "papers/2026/08/_sources/daily-20260801"
            report.parent.mkdir(parents=True)
            packet.mkdir(parents=True)
            report.write_text("# Daily\n", encoding="utf-8")
            (packet / "coverage-receipt.json").write_text("", encoding="utf-8")
            (packet / "screening-ledger.json").write_text("", encoding="utf-8")

            signals, _refs = source_packet_signals(root, report, report.read_text())

            self.assertFalse(signals.packet_present)
            self.assertEqual(signals.nonempty_file_count, 0)
            self.assertEqual(signals.empty_file_count, 2)
            self.assertFalse(signals.coverage_receipt)
            self.assertFalse(signals.screening_ledger)

    def test_complete_packet_is_machine_ready_but_not_semantically_self_proving(self):
        issues = classify_latest_contract(
            validator_errors=[],
            candidate_count=2,
            review_count=2,
            semantic_scopes={"coverage": "passed", "evidence": "passed", "deep_analysis_selection": "passed", "books": "passed"},
            signals=SourcePacketSignals(
                packet_present=True,
                coverage_receipt=True,
                screening_ledger=True,
                per_identity_closures=True,
                raw_inventory=True,
                exact_primary_material=True,
                arxiv_owner_receipt=True,
            ),
        )
        self.assertEqual(issues, [])

    def test_candidate_review_mismatch_reopens_evidence(self):
        issues = classify_latest_contract(
            validator_errors=[],
            candidate_count=3,
            review_count=2,
            semantic_scopes={"coverage": "passed", "evidence": "passed", "deep_analysis_selection": "passed", "books": "passed"},
            signals=SourcePacketSignals(
                packet_present=True,
                coverage_receipt=True,
                screening_ledger=True,
                per_identity_closures=True,
                raw_inventory=True,
                exact_primary_material=True,
                arxiv_owner_receipt=True,
            ),
        )
        self.assertIn("candidate_review_count_mismatch", issues)

    def test_arxiv_without_official_listing_receipt_reopens_date_ownership(self):
        issues = classify_latest_contract(
            validator_errors=[],
            candidate_count=1,
            review_count=1,
            semantic_scopes={"coverage": "passed", "evidence": "passed", "deep_analysis_selection": "passed", "books": "passed"},
            signals=SourcePacketSignals(
                packet_present=True,
                coverage_receipt=True,
                screening_ledger=True,
                per_identity_closures=True,
                raw_inventory=True,
            ),
            arxiv_due=True,
        )
        self.assertIn("arxiv_owner_date_receipt_missing", issues)

    def test_arxiv_zero_hit_still_requires_official_listing_receipt(self):
        self.assertTrue(_arxiv_receipt_due([{"Source ID": "SRC-ARXIV", "Result": "no_hit"}]))
        self.assertFalse(_arxiv_receipt_due([{"Source ID": "SRC-ARXIV", "Result": "not_due"}]))

    def test_unclassified_listing_filename_does_not_prove_first_public_owner(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "papers/2026/09/02/README.md"
            packet = root / "papers/2026/09/_sources/daily-20260902"
            report.parent.mkdir(parents=True)
            packet.mkdir(parents=True)
            report.write_text("# Daily\n", encoding="utf-8")
            (packet / "arxiv-listing-enumeration.json").write_text(
                '{"listing_date":"2026-09-01","entries":[]}\n', encoding="utf-8"
            )

            signals, _refs = source_packet_signals(root, report, report.read_text())

            self.assertFalse(signals.arxiv_owner_receipt)

    def test_event_classified_announcement_receipt_proves_owner(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            report = root / "papers/2026/09/02/README.md"
            packet = root / "papers/2026/09/_sources/daily-20260902"
            report.parent.mkdir(parents=True)
            packet.mkdir(parents=True)
            report.write_text("# Daily\n", encoding="utf-8")
            (packet / "arxiv-owner-reconciliation.json").write_text(
                '{"ownership_method":"official_announcement_reconciled",'
                '"events":[{"event_type":"new"}]}\n',
                encoding="utf-8",
            )

            signals, _refs = source_packet_signals(root, report, report.read_text())

            self.assertTrue(signals.arxiv_owner_receipt)

    def test_recovery_action_prioritizes_inventory_before_semantic_reaudit(self):
        self.assertEqual(
            next_recovery_action(["raw_inventory_missing", "arxiv_owner_date_receipt_missing"]),
            "restore_or_replay_raw_inventory",
        )
        self.assertEqual(next_recovery_action([]), "fresh_context_semantic_reaudit")

    def test_absolute_output_outside_root_has_a_stable_display_path(self):
        root = Path("/workspace/project")
        self.assertEqual(
            _display_output_path(Path("/tmp/daily-audit"), root),
            "/tmp/daily-audit",
        )
        self.assertEqual(
            _display_output_path(root / "papers/_sources/audit", root),
            "papers/_sources/audit",
        )


if __name__ == "__main__":
    unittest.main()
