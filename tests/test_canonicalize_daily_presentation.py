import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "canonicalize_daily_presentation.py"


def load_module():
    spec = importlib.util.spec_from_file_location("canonicalize_daily_presentation", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def evidence_fingerprint(text: str) -> str:
    """Hash the machine-audited evidence payload, independent of section movement."""
    kept = []
    for line in text.splitlines():
        if (
            line.startswith("| SF-")
            or line.startswith("<!-- review:")
            or line.startswith("<!-- claim:")
            or line.startswith("<!-- books-review:")
            or line.startswith("<!-- semantic-audit:")
        ):
            kept.append(line)
    return hashlib.sha256("\n".join(sorted(kept)).encode()).hexdigest()


class CanonicalizeDailyPresentationTests(unittest.TestCase):
    def test_august_legacy_report_moves_without_changing_evidence(self):
        module = load_module()
        source = ROOT / "papers/2026/08/28/README.md"
        canonical = source.read_text()
        benchmark_start = canonical.index("## 4. Benchmark Contracts")
        deep_start = canonical.index("## 5. Deep Analysis Selection")
        benchmark = canonical[
            benchmark_start + len("## 4. Benchmark Contracts") : deep_start
        ].strip("\n")
        original = canonical[:benchmark_start] + canonical[deep_start:]
        review_start = original.index("## 3. Review Completion Receipt")
        original = original[:review_start].rstrip() + "\n\n" + benchmark + "\n\n" + original[review_start:]
        final_start = original.index("## 13. Final Status")
        original = original[:final_start].rstrip() + "\n"
        heading_map = {
            "## 12. Sources": "## 11. Sources",
            "## 11. Open Questions": "## 10. Open Questions",
            "## 10. Repository Changes": "## 9. Repository Changes",
            "## 9. Recommended Action": "## 8. Recommended Action",
            "## 8. Ignored Noise": "## 7. Ignored Noise",
            "## 7. Semantic Audit": "## 6. Semantic Audit",
            "## 6. Books Comparison": "## 5. Books Comparison Queue",
            "## 5. Deep Analysis Selection": "## 4. Deep Analysis Selection",
        }
        for current, legacy in heading_map.items():
            original = original.replace(current, legacy, 1)
        original = original.replace(
            "**Strict Window:** 2026-08-27 09:00:00 ～ 2026-08-28 09:00:00（北京时间，左闭右开）\n\n",
            "**Window:** 2026-08-27 09:00:00 ～ 2026-08-28 09:00:00（北京时间，左闭右开）\n",
            1,
        ).replace("**Contract:** V2.1 Full Replay\n\n", "", 1)
        before = evidence_fingerprint(original)

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "README.md"
            target.write_text(original)
            self.assertTrue(module.canonicalize_report(target))
            migrated = target.read_text()
            self.assertEqual(before, evidence_fingerprint(migrated))
            self.assertIn("**Strict Window:** 2026-08-27 09:00:00 ～ 2026-08-28 09:00:00", migrated)
            self.assertIn("## 4. Benchmark Contracts", migrated)
            self.assertIn("## 13. Final Status", migrated)
            self.assertNotIn("## 6. Books Comparison\n\n Queue", migrated)
            self.assertLess(migrated.index("### Source Reviews"), migrated.index("## 4. Benchmark Contracts"))
            self.assertFalse(module.canonicalize_report(target))


if __name__ == "__main__":
    unittest.main()
