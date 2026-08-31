#!/usr/bin/env python3
"""Behavioral tests for the guarded 2026-06-21 Books workflow."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
import shutil

from scripts import apply_june21_books as apply_books
from scripts import close_june21_postwrite as close_books


class June21BooksWorkflowTest(unittest.TestCase):
    def make_tree(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="june21-books-test-"))
        owners = {evidence["owner"] for evidence in apply_books.FINALIZER.C.values()}
        for owner in owners:
            path = apply_books.FINALIZER.PATHS[owner]
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            no_change = [
                anchor
                for aid, anchor in close_books.NO_CHANGE_ANCHORS.items()
                if close_books.FINALIZER.C[aid]["owner"] == owner
            ]
            target.write_text(
                "# Test owner\n\n"
                + apply_books.FINALIZER.TARGET_ANCHORS[owner]
                + "\n\n"
                + "\n".join(no_change)
                + "\n"
            )
        return root

    def test_pristine_tree_plans_all_owner_blocks_and_complete_tree_is_noop(self) -> None:
        root = self.make_tree()
        updates = apply_books.plan_writeback(root)
        self.assertEqual(len(updates), 12)
        for path, text in updates.items():
            path.write_text(text)
        self.assertEqual(apply_books.plan_writeback(root), {})

    def test_complete_owner_checkpoint_is_resumed_without_rewriting_it(self) -> None:
        root = self.make_tree()
        updates = apply_books.plan_writeback(root)
        path, text = next(iter(updates.items()))
        path.write_text(text)
        resumed = apply_books.plan_writeback(root)
        self.assertEqual(len(resumed), 11)
        self.assertNotIn(path, resumed)

    def test_duplicate_family_is_rejected(self) -> None:
        root = self.make_tree()
        updates = apply_books.plan_writeback(root)
        for path, text in updates.items():
            path.write_text(text)
        duplicate = root / next(iter(apply_books.FINALIZER.PATHS.values()))
        duplicate.write_text(duplicate.read_text() + "\nSF-2026-ARXIV-2606-21843\n")
        with self.assertRaisesRegex(RuntimeError, "duplicate"):
            apply_books.plan_writeback(root)

    def test_postwrite_audit_covers_20_integrates_and_17_no_changes(self) -> None:
        root = self.make_tree()
        for path, text in apply_books.plan_writeback(root).items():
            path.write_text(text)
        rows = close_books.audit_books(root)
        self.assertEqual(sum(row["disposition"] == "Integrate" for row in rows), 20)
        self.assertEqual(sum(row["disposition"].startswith("No Change") for row in rows), 17)
        self.assertTrue(all(row["result"] == "PASS" for row in rows))

    def test_postwrite_audit_rejects_missing_source_specific_review_field(self) -> None:
        root = self.make_tree()
        for path, text in apply_books.plan_writeback(root).items():
            path.write_text(text)
        target = root / apply_books.FINALIZER.PATHS["PLATFORM-MONITORING"]
        target.write_text(target.read_text().replace("Evaluation=`", "Evaluation-missing=`", 1))
        with self.assertRaisesRegex(RuntimeError, "Evaluation"):
            close_books.audit_books(root)

    def test_daily_close_is_idempotent(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="june21-close-test-"))
        report = root / "README.md"
        packet = root / "packet"
        packet.mkdir()
        shutil.copy2(close_books.REPORT, report)
        for name in ["README.md", "FRESH_EVIDENCE_SELECTION_AUDIT_V1.md", "BOOKS_INTEGRATION_QUEUE_V1.md"]:
            shutil.copy2(close_books.PACKET / name, packet / name)
        close_books.close_daily(report, packet)
        first = {path.name: path.read_text() for path in [report, *(packet.iterdir())]}
        close_books.close_daily(report, packet)
        second = {path.name: path.read_text() for path in [report, *(packet.iterdir())]}
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
