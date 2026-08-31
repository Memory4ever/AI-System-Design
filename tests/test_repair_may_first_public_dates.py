import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "repair_may_first_public_dates.py"


def load_module():
    spec = importlib.util.spec_from_file_location("repair_may_first_public_dates", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class RepairMayFirstPublicDatesTests(unittest.TestCase):
    def setUp(self):
        self.module = load_module()

    def make_fixture(self, root: Path, timestamp: str = "2026-05-03T16:30:00Z") -> Path:
        ledger = root / "papers/2026/05/_sources/daily-20260504/screening-ledger.json"
        readme = root / "papers/2026/05/04/README.md"
        ledger.parent.mkdir(parents=True)
        readme.parent.mkdir(parents=True)
        ledger.write_text(
            json.dumps(
                [
                    {
                        "arxiv_id": "2605.01950",
                        "identity": "2605.01950v1",
                        "published_v1_utc": timestamp,
                        "source_family_id": "SF-TEST",
                    }
                ]
            ),
            encoding="utf-8",
        )
        readme.write_text(
            """# Test Daily

## 2. Candidate Ledger

| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date |
| --- | --- | --- | --- | --- |
| `SF-TEST` | `arXiv:2605.01950v1` | `paper:v1` | `2026-W18` | 2026-05-03 |

## 3. Source Review
""",
            encoding="utf-8",
        )
        audit = root / "papers/2026/05/_sources/may-first-public-date-audit.json"
        audit.parent.mkdir(parents=True, exist_ok=True)
        audit.write_text(
            json.dumps(
                {
                    "schema": "may-first-public-date-audit-v1",
                    "summary": {"mismatch_count": 1},
                    "findings": [
                        {
                            "report": "2026-05-04",
                            "family": "SF-TEST",
                            "raw_timestamp": timestamp,
                            "expected_local_date": "2026-05-04",
                            "current_field": "2026-05-03",
                            "evidence_path": (
                                "papers/2026/05/_sources/daily-20260504/screening-ledger.json"
                                "#2605.01950v1.published_v1_utc;"
                                "papers/2026/05/04/README.md"
                                "#Candidate-Ledger/SF-TEST/First-public-Date"
                            ),
                            "finding": "test",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        return audit

    def test_repairs_local_date_and_owner_week_then_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audit = self.make_fixture(root)

            rendered, receipt = self.module.prepare_repairs(root, audit)
            readme = root / "papers/2026/05/04/README.md"
            self.assertIn("| `2026-W19` | 2026-05-04 |", rendered[readme])
            self.assertEqual(receipt["summary"]["date_changes"], 1)
            self.assertEqual(receipt["summary"]["owner_week_changes"], 1)

            readme.write_text(rendered[readme], encoding="utf-8")
            rerendered, second = self.module.prepare_repairs(root, audit)
            self.assertEqual(rerendered, {})
            self.assertEqual(second["summary"]["already_correct"], 1)

    def test_rejects_timestamp_outside_strict_daily_window(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audit = self.make_fixture(root, "2026-05-04T02:00:00Z")
            with self.assertRaisesRegex(ValueError, "outside strict window"):
                self.module.prepare_repairs(root, audit)

    def test_rejects_duplicate_candidate_family_before_rendering(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            audit = self.make_fixture(root)
            readme = root / "papers/2026/05/04/README.md"
            text = readme.read_text(encoding="utf-8")
            original = "| `SF-TEST` | `arXiv:2605.01950v1` | `paper:v1` | `2026-W18` | 2026-05-03 |\n"
            duplicate = "| `SF-TEST` | `arXiv:2605.01950v1` | `paper:v1` | `2026-W18` | 2026-05-03 |\n"
            readme.write_text(text.replace(original, original + duplicate), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "candidate row count"):
                self.module.prepare_repairs(root, audit)


if __name__ == "__main__":
    unittest.main()
