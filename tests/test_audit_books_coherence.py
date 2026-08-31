import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_books_coherence", ROOT / "scripts/audit_books_coherence.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class AuditBooksCoherenceTest(unittest.TestCase):
    def test_roadmap_has_84_unique_contiguous_chapters(self):
        rows = MODULE.roadmap_chapters(MODULE.ROADMAP.read_text(encoding="utf-8"))
        self.assertEqual(len(rows), 84)
        self.assertEqual(len({row.node for row in rows}), 84)
        self.assertEqual([row.number for row in rows], list(range(1, 85)))

    def test_all_chapters_pass_closed_contract(self):
        rows = MODULE.build_rows()
        self.assertEqual(len(rows), 84)
        self.assertEqual([row for row in rows if row["finding"]], [])
        integrated = [row for row in rows if int(row["integrate_count"]) > 0]
        self.assertEqual(len(integrated), 59)
        self.assertTrue(all(row["semantic_proof"] == "pass" for row in integrated))
        self.assertEqual(sum(int(row["integrate_count"]) for row in integrated), 983)


if __name__ == "__main__":
    unittest.main()
