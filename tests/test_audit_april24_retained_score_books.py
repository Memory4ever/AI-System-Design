import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/audit_april24_retained_score_books.py"
SPEC = importlib.util.spec_from_file_location("audit_april24_retained", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class BooksOwnerReferenceTest(unittest.TestCase):
    def test_all_books_owner_references_resolve_to_real_headings(self):
        for _, _, _, owner_ref in MODULE.AUDIT.values():
            MODULE.validate_owner_ref(owner_ref)

    def test_missing_owner_file_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "owner file does not exist"):
            MODULE.validate_owner_ref("books/not-real.md#not-real")

    def test_missing_owner_heading_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "owner heading does not exist"):
            MODULE.validate_owner_ref("books/part-07-agent/81-workflow.md#not-real")


if __name__ == "__main__":
    unittest.main()
