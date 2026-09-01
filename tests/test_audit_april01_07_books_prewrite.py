import importlib.util
from pathlib import Path
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/audit_april01_07_books_prewrite.py"
SPEC = importlib.util.spec_from_file_location("audit_april01_07_books", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class BooksReferenceAcceptanceTest(unittest.TestCase):
    def test_real_heading_resolves(self):
        self.assertTrue(
            MODULE.markdown_ref_resolves(
                "books/part-07-agent/81-workflow.md#recovery-与-verification-必须产生不同-artifact"
            )
        )

    def test_placeholder_heading_is_rejected(self):
        self.assertFalse(
            MODULE.markdown_ref_resolves(
                "books/part-07-agent/81-workflow.md#canonical-owner"
            )
        )


if __name__ == "__main__":
    unittest.main()
