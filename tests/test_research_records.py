"""Single-family records render projections; they never invent review conclusions."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import research_records as records
from test_validate_research import VALID_DAILY_V21, daily_v22, load_validator


class ResearchRecordsTests(unittest.TestCase):
    def test_roundtrip_and_check_are_idempotent(self):
        document = daily_v22()
        canonical = records.extract(document)
        self.assertEqual(1, len(canonical["families"]))
        family = canonical["families"][0]
        self.assertNotIn("Review Provenance ID", family)
        self.assertNotIn("Review Route", family)
        rendered = records.render(document, canonical)
        self.assertEqual(rendered, records.render(rendered, canonical))
        self.assertEqual(canonical, records.extract(rendered))
        self.assertEqual([], records.drift(rendered, canonical))

    def test_record_change_updates_projection_and_is_detectable(self):
        canonical = records.extract(daily_v22())
        canonical["families"][0]["Durability"] = "1"
        canonical["families"][0]["Review Status"] = "standard_complete"
        self.assertTrue(records.drift(daily_v22(), canonical))
        rendered = records.render(daily_v22(), canonical)
        v = load_validator()
        rows, errors = v._expect_columns(rendered, v.CANDIDATE_LEDGER_MARKER, v.CANDIDATE_COLUMNS)
        self.assertFalse(errors)
        self.assertEqual("6", rows[0]["Total"])
        reviews, _ = v._expect_columns(rendered, v.REVIEW_COMPLETION_MARKER, v.REVIEW_COMPLETION_COLUMNS)
        self.assertEqual("standard", reviews[0]["Review Route"])
        # The tool does not mark any new audit or change report completion metadata.
        self.assertIn("| Completion Status | Complete |", rendered)

    def test_body_edit_refreshes_digest_without_rewriting_evidence(self):
        document = daily_v22()
        canonical = records.extract(document)
        edited = document.replace("define this bounded claim", "define this explicitly bounded claim")
        self.assertTrue(records.drift(edited, canonical))
        rendered = records.render(edited, canonical)
        self.assertIn("this explicitly bounded claim", rendered)
        self.assertNotIn("RP-1188b619ab6e379d", rendered)

    def test_reject_duplicate_family_and_unknown_fields(self):
        canonical = records.extract(daily_v22())
        duplicate = copy.deepcopy(canonical)
        duplicate["families"].append(copy.deepcopy(duplicate["families"][0]))
        with self.assertRaises(ValueError):
            records.render(daily_v22(), duplicate)
        canonical["families"][0]["Tyop Review Status"] = "complete"
        with self.assertRaises(ValueError):
            records.render(daily_v22(), canonical)

    def test_no_implicit_legacy_migration(self):
        canonical = records.extract(VALID_DAILY_V21)
        with self.assertRaises(ValueError):
            records.render(VALID_DAILY_V21, canonical)

    def test_missing_body_cannot_be_rendered_as_review_complete(self):
        canonical = records.extract(daily_v22())
        damaged = daily_v22().replace("<!-- review:SF-001:start -->", "")
        with self.assertRaises(ValueError):
            records.render(damaged, canonical)

    def test_cli_extract_check_render_and_nonoverwrite(self):
        script = str(Path(records.__file__).resolve())
        with tempfile.TemporaryDirectory() as folder:
            report = Path(folder) / "README.md"
            record_path = Path(folder) / "records.json"
            report.write_text(daily_v22(), encoding="utf-8")
            def run(mode, *extra):
                return subprocess.run([sys.executable, script, mode, str(report), str(record_path), *extra],
                                      capture_output=True, text=True)
            self.assertEqual(0, run("extract").returncode)
            original_record = record_path.read_bytes()
            self.assertNotEqual(0, run("extract").returncode)
            self.assertEqual(original_record, record_path.read_bytes())
            self.assertEqual(0, run("check").returncode)
            canonical = json.loads(original_record)
            canonical["families"][0]["Artifact Locators"] = "Not Disclosed — public manuscript has no code link"
            record_path.write_text(json.dumps(canonical), encoding="utf-8")
            self.assertNotEqual(0, run("check").returncode)
            before = report.read_bytes()
            self.assertEqual(0, run("render").returncode)
            self.assertEqual(before, report.read_bytes())
            self.assertEqual(0, run("render", "--write").returncode)
            self.assertEqual(0, run("check").returncode)

    def test_unknown_record_shape_is_a_clear_error(self):
        with self.assertRaises(ValueError):
            records.render(daily_v22(), [])
