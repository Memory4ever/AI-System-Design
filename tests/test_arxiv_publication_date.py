"""Small field projections, not whole cached DataCite/XML fixtures."""

import copy
import io
import json
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from scripts.arxiv_publication_date import main, publication_date_envelope


def record(submitted="2025-11-03T18:29:57Z",
           registered="2025-11-04T04:32:13Z", arxiv_id="2511.01824"):
    doi = "10.48550/arxiv." + arxiv_id
    return {"data": {
        "id": doi,
        "attributes": {
            "doi": doi, "publisher": "arXiv", "state": "findable",
            "registered": registered,
            "created": "2025-11-01T00:00:00Z",
            "dates": [{"date": submitted, "dateType": "Submitted",
                       "dateInformation": "v1"}],
        },
        "relationships": {"client": {"data": {"id": "arxiv.content"}}},
    }}


# Exact fields from local copies of api.datacite.org/dois/10.48550/arxiv.<ID>:
# 2511.01824 / 01805: papers/2025/11/_sources/daily-20251105/datacite-018{24,05}.json
# 2604.17289: papers/2026/04/_sources/daily-20260422/
#   SUP_DATE_FOUR_DATACITE_20261015.raw.json
# 2601.18467: papers/2026/01/_sources/daily-20260128/
#   supplement-date-identities-20261008.json
# Only necessary fields are projected; created is a consistency check, not a bound.
REAL_CASES = (
    ("Simia", "2511.01824", "2025-11-03T18:29:57Z",
     "2025-11-04T04:32:13.000Z", "2025-11-04T04:32:12.000Z",
     "2025-11-04T01:00:00Z", "2025-11-04"),
    ("Context", "2511.01805", "2025-11-03T18:05:57Z",
     "2025-11-04T04:31:46.000Z", "2025-11-04T04:31:46.000Z",
     "2025-11-04T01:00:00Z", "2025-11-04"),
    ("REALM", "2604.17289", "2026-04-19T07:06:35Z",
     "2026-04-21T04:00:53Z", "2026-04-21T04:00:52Z",
     "2026-04-21T00:00:00Z", "2026-04-21"),
    ("Offseeker", "2601.18467", "2026-01-26T13:13:59Z",
     "2026-01-27T04:13:22.000Z", "2026-01-27T04:13:21.000Z",
     "2026-01-27T01:00:00Z", "2026-01-27"),
)


class PublicationDateTests(unittest.TestCase):
    def unresolved(self, raw, reason, arxiv_id="2511.01824"):
        result = publication_date_envelope(raw, arxiv_id)
        self.assertEqual("unresolved", result["status"])
        self.assertIsNone(result["bounded_bjt_date"])
        self.assertIn(reason, result["reasons"])
        self.assertNotIn("public_date", result)
        return result

    def test_real_field_regressions(self):
        for name, identity, submitted, registered, created, earliest, day in REAL_CASES:
            with self.subTest(name=name):
                raw = record(submitted, registered, identity)
                raw["data"]["attributes"]["created"] = created
                result = publication_date_envelope(raw, identity)
                self.assertEqual("bounded", result["status"])
                self.assertEqual(day, result["bounded_bjt_date"])
                self.assertEqual(earliest, result["earliest_announcement_utc"])
                self.assertEqual(registered, result["source_fields"]["registered"])
                self.assertEqual(submitted, result["source_fields"]["submitted_v1"])
                self.assertEqual(created, result["source_fields"]["created"])
                self.assertEqual("arxiv_v1_announcement_only", result["scope"])
                self.assertTrue(result["limitations"])

    def test_weekday_weekend_and_dst_schedule(self):
        cases = (
            ("2025-11-03T18:59:59Z", "2025-11-04T01:00:00Z"),
            ("2025-11-03T19:00:01Z", "2025-11-05T01:00:00Z"),
            ("2025-11-04T19:00:01Z", "2025-11-06T01:00:00Z"),
            ("2025-11-05T19:00:01Z", "2025-11-07T01:00:00Z"),
            ("2025-11-06T19:00:01Z", "2025-11-10T01:00:00Z"),
            ("2025-11-07T18:59:59Z", "2025-11-10T01:00:00Z"),
            ("2025-11-07T19:00:01Z", "2025-11-11T01:00:00Z"),
            ("2025-11-08T12:00:00Z", "2025-11-11T01:00:00Z"),
            ("2025-11-09T22:00:00Z", "2025-11-11T01:00:00Z"),
            ("2026-03-06T18:00:00Z", "2026-03-09T00:00:00Z"),
            ("2026-10-30T17:00:00Z", "2026-11-02T01:00:00Z"),
        )
        for submitted, earliest in cases:
            with self.subTest(submitted=submitted):
                # Synthetic identity matches the expected announcement's month,
                # not the submission month (October submissions can announce in November).
                identity = earliest[2:4] + earliest[5:7] + ".00001"
                result = publication_date_envelope(record(submitted, earliest, identity), identity)
                self.assertEqual("bounded", result["status"])
                self.assertEqual(earliest, result["earliest_announcement_utc"])

    def test_obvious_id_month_conflict_is_not_a_bounded_result(self):
        self.unresolved(record("2026-03-06T18:00:00Z", "2026-03-09T04:00:00Z"),
                        "id_month_conflict")

    def test_id_month_allows_adjacent_months_across_timezones(self):
        # Sunday Nov 30 20:00 New York is Dec 1 in UTC and BJT.
        for identity in ("2511.00001", "2512.00001"):
            with self.subTest(identity=identity):
                raw = record("2025-11-28T18:00:00Z", "2025-12-01T04:00:00Z", identity)
                result = publication_date_envelope(raw, identity)
                self.assertEqual("bounded", result["status"])
                self.assertEqual("2025-12-01", result["bounded_bjt_date"])

    def test_legacy_id_is_not_granted_a_month_compatibility_conclusion(self):
        identity = "hep-th/9901001"
        self.unresolved(record(arxiv_id=identity), "legacy_id_month_unverified", identity)

    def test_id_month_never_supplies_or_tightens_bounds(self):
        identity = "2512.00001"
        raw = record(registered="2025-12-01T04:00:00Z", arxiv_id=identity)
        result = self.unresolved(raw, "cross_bjt_dates", identity)
        self.assertEqual("2025-11-04T01:00:00Z", result["earliest_announcement_utc"])
        self.assertNotIn("id_month_conflict", result["reasons"])
        raw["data"]["attributes"]["dates"] = []
        result = self.unresolved(raw, "missing_v1_submitted", identity)
        self.assertIsNone(result["earliest_announcement_utc"])

    def test_exact_14_et_never_automatically_moves_lower_bound_to_next_batch(self):
        result = self.unresolved(record("2025-11-03T19:00:00Z"), "cutoff_boundary")
        self.assertEqual("2025-11-04T01:00:00Z", result["earliest_announcement_utc"])
        result = self.unresolved(record("2026-04-20T18:00:00Z", "2026-04-21T04:00:00Z"),
                                 "cutoff_boundary")
        self.assertEqual("2026-04-21T00:00:00Z", result["earliest_announcement_utc"])

    def test_delayed_registration_crossing_bjt_days_is_unresolved(self):
        self.unresolved(record(registered="2025-11-05T04:32:13Z"), "cross_bjt_dates")
        self.unresolved(record(registered="2025-11-04T16:00:00Z"), "cross_bjt_dates")
        result = publication_date_envelope(record(registered="2025-11-04T15:59:59Z"), "2511.01824")
        self.assertEqual("2025-11-04", result["bounded_bjt_date"])

    def test_created_never_substitutes_for_registered(self):
        raw = record()
        raw["data"]["attributes"].pop("registered")
        raw["data"]["attributes"]["created"] = "2025-11-04T04:32:13Z"
        self.unresolved(raw, "missing_registered")
        raw["data"]["attributes"]["registered"] = None
        self.unresolved(raw, "missing_registered")

    def test_registered_not_created_controls_upper_bound(self):
        raw = record()
        raw["data"]["attributes"]["created"] = "2025-11-03T04:32:13Z"
        self.assertEqual("2025-11-04", publication_date_envelope(raw, "2511.01824")["bounded_bjt_date"])

    def test_created_is_optional_but_observed_reverse_chronology_is_a_conflict(self):
        raw = record()
        raw["data"]["attributes"]["created"] = "2025-11-05T04:32:13Z"
        self.unresolved(raw, "created_after_registered")
        raw["data"]["attributes"].pop("created")
        self.assertEqual("bounded", publication_date_envelope(raw, "2511.01824")["status"])
        raw["data"]["attributes"]["created"] = "2025-11-03T04:32:13"
        self.unresolved(raw, "invalid_created")

    def test_provenance_and_identity_are_required(self):
        for field, value, reason in (
            ("publisher", "Other", "publisher_mismatch"),
            ("state", "registered", "not_findable"),
            ("doi", "10.48550/arxiv.2511.01805", "doi_mismatch"),
            ("doi", "10.1234/2511.01824", "doi_mismatch"),
        ):
            raw = record()
            raw["data"]["attributes"][field] = value
            with self.subTest(field=field, value=value):
                self.unresolved(raw, reason)
        raw = record()
        raw["data"]["relationships"]["client"]["data"]["id"] = "other.client"
        self.unresolved(raw, "client_mismatch")
        raw = record()
        raw["data"]["id"] += "v2"
        self.unresolved(raw, "doi_mismatch")
        self.unresolved(record(), "version_conflict", "2511.01824v2")

    def test_v1_must_be_unique_submitted_not_latest_or_updated(self):
        for replacement in (
            [{"date": "2025-11-03T18:29:57Z", "dateType": "Submitted", "dateInformation": "v2"}],
            [{"date": "2025-11-03T18:29:57Z", "dateType": "Updated", "dateInformation": "v1"}],
            [{"date": "2025-11", "dateType": "Available", "dateInformation": "v1"}],
            [],
        ):
            raw = record()
            raw["data"]["attributes"]["dates"] = replacement
            raw["data"]["attributes"]["published"] = "2025-11-03T18:29:57Z"
            self.unresolved(raw, "missing_v1_submitted")
        for date in ("2025-11-03T18:29:57Z", "2025-11-03T19:29:57Z"):
            raw = record()
            raw["data"]["attributes"]["dates"].append(
                {"date": date, "dateType": "Submitted", "dateInformation": "v1"})
            self.unresolved(raw, "multiple_v1_submitted")

    def test_later_versions_do_not_replace_v1(self):
        raw = record()
        raw["data"]["attributes"]["dates"].append(
            {"date": "2025-11-04T17:41:28Z", "dateType": "Submitted", "dateInformation": "v2"})
        self.assertEqual("2025-11-04", publication_date_envelope(raw, "2511.01824v1")["bounded_bjt_date"])

    def test_timezone_and_chronology_fail_closed(self):
        self.unresolved(record(submitted="2025-11-03T18:29:57"), "invalid_v1_submitted")
        self.unresolved(record(registered="2025-11-04T04:32:13"), "invalid_registered")
        self.unresolved(record(registered="2025-11-04"), "invalid_registered")
        self.unresolved(record(registered="2025-11-04T12:32:13+08:00"), "registered_not_utc")
        self.unresolved(record(registered="2025-11-04T00:59:59Z"), "reversed_bounds")

    def test_minimal_wrappers_and_no_input_mutation(self):
        raw = record()
        before = copy.deepcopy(raw)
        for wrapped in (raw, raw["data"], {"payload": raw}, {"payload": raw["data"]}):
            self.assertEqual("bounded", publication_date_envelope(wrapped, "2511.01824")["status"])
        self.assertEqual(before, raw)
        for malformed in ([], {"data": []}, None, {"payload": raw, "data": raw}):
            self.unresolved(malformed, "invalid_record")


class CliTests(unittest.TestCase):
    def invoke(self, text):
        with patch("sys.stdin", io.StringIO(text)), redirect_stdout(io.StringIO()) as out:
            with redirect_stderr(io.StringIO()) as err:
                code = main(["-", "--arxiv-id", "2511.01824"])
        return code, out.getvalue(), err.getvalue()

    def test_stdin_json_and_exit_codes(self):
        code, out, err = self.invoke(json.dumps(record()))
        self.assertEqual((0, ""), (code, err))
        self.assertEqual("2025-11-04", json.loads(out)["bounded_bjt_date"])
        code, out, err = self.invoke(json.dumps(record(registered=None)))
        self.assertEqual(1, code)
        self.assertEqual("unresolved", json.loads(out)["status"])

    def test_invalid_json_and_duplicate_keys_are_not_silently_accepted(self):
        for text in ("not json", '{"data": {}, "data": {}}'):
            code, out, err = self.invoke(text)
            self.assertEqual(2, code)
            self.assertEqual("", out)
            self.assertTrue(err)

    def test_script_entrypoint_is_read_only_stdin(self):
        script = Path(__file__).resolve().parents[1] / "scripts/arxiv_publication_date.py"
        proc = subprocess.run([sys.executable, "-B", str(script), "-", "--arxiv-id", "2511.01824"],
                              input=json.dumps(record()), capture_output=True, text=True, check=False)
        self.assertEqual(0, proc.returncode, proc.stderr)
        self.assertEqual("bounded", json.loads(proc.stdout)["status"])


if __name__ == "__main__":
    unittest.main()
