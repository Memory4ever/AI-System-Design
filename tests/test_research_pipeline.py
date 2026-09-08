"""Regression boundaries for V2.2 discovery, review routing and completion."""
import unittest

from scripts import research_records as records
from test_validate_research import (
    SOURCE_MATERIALS_REQUEST,
    VALID_DAILY_V21,
    VALID_REGISTRY,
    daily_v22,
    load_validator,
)


DAILY_START = "2026-08-24T09:00:00+08:00"
DAILY_END = "2026-08-25T09:00:00+08:00"
WEEK_START = "2026-08-24T00:00:00+08:00"
WEEK_END = "2026-08-31T00:00:00+08:00"


def strict_daily():
    # Keep the V2.2 boundary explicit while sharing the legacy fixture structure.
    return daily_v22().replace("2026-08-23T09:00:00+08:00", DAILY_START)


def change_receipt(text, **changes):
    """Edit one coverage row by column name, without copying the report fixture."""
    lines = text.splitlines()
    marker = lines.index("<!-- validator:source-coverage-v2 -->")
    columns = [cell.strip() for cell in lines[marker + 1].strip("|").split("|")]
    values = [cell.strip() for cell in lines[marker + 3].strip("|").split("|")]
    row = dict(zip(columns, values))
    row.update(changes)
    lines[marker + 3] = "| " + " | ".join(row[column] for column in columns) + " |"
    return "\n".join(lines) + "\n"


def add_receipt(text, source, *, trigger=True, failed=False):
    endpoint = "https://publisher.example.org/releases"
    if trigger:
        endpoint += "; trigger:PUB-A-release"
    row = (
        f"| {source} | {DAILY_START} | {DAILY_END} | {DAILY_END} | {endpoint} | "
        + ("failed | 0 | — | — | — | — | GAP-ORG-B-01 |\n" if failed else
           f"checked | 1 | — | pages=1; final_cursor=end | {DAILY_END} | coverage:{source}:closed | — |\n")
    )
    text = text.replace("\n\n## 2. Candidate Ledger", "\n" + row + "\n## 2. Candidate Ledger")
    if trigger:
        text += (
            "\n<!-- trigger:PUB-A-release:start -->\n"
            f"Source ID: {source}. The official 2026-08-25T08:00:00+08:00 release at "
            "https://publisher.example.org/releases/2026-08-25 announced a new proceedings item. "
            "This dated Daily event triggered an exact item lookup, not a weekly venue sweep.\n"
            "<!-- trigger:PUB-A-release:end -->\n"
        )
    if not failed:
        text += (
            f"\n<!-- coverage:{source}:closed:start -->\n"
            "| Primary Identifier | Screening Decision | Reason |\n"
            "| --- | --- | --- |\n"
            "| https://publisher.example.org/papers/one | pre-denominator closure | "
            "The title and abstract describe one-dataset accuracy gains, with no changed "
            "execution mechanism, state ownership or evaluation contract. |\n"
            f"<!-- coverage:{source}:closed:end -->\n"
        )
        text = text.replace("| coverage | coverage:ORG-A:2026-08-25 |",
                            f"| coverage | coverage:ORG-A:2026-08-25; coverage:{source}:closed |")
    return text


def revision_report(**changes):
    text = strict_daily().replace("arXiv:2608.00001v1", "arXiv:2608.00001v2")
    canonical = records.extract(text)
    canonical["families"][0].update({
        "Candidate State": "revision", "Design Delta": "—", "System Reach": "—",
        "Durability": "—", "Review Override": "important_revision",
        "Owner Report Ref": "papers/owner.md", "Reconciliation": "same_window_revision",
        "Books Disposition": "Integrate", **changes,
    })
    return records.render(text, canonical)


def natural_weekly():
    text = strict_daily().replace("| Report Type | Daily |", "| Report Type | Sunday Weekly |")
    text = text.replace("| Window Start | 2026-08-25 |", "| Window Start | 2026-08-24 |")
    text = text.replace("| Window End | 2026-08-25 |", "| Window End | 2026-08-30 |")
    text = text.replace("2026-08-25T23:00:00+08:00", "2026-08-31T09:00:00+08:00")
    text = text.replace("2026-08-24 09:00:00 ～ 2026-08-25 09:00:00",
                        "2026-08-24 00:00:00 ～ 2026-08-31 00:00:00")
    text = change_receipt(text, **{"Window Start": WEEK_START, "Window End": WEEK_END,
                                 "Executed At": "2026-08-31T09:00:00+08:00",
                                 "Window Watermark": WEEK_END})
    row = (
        f"| PUB-A | {WEEK_START} | {WEEK_END} | 2026-08-31T09:00:00+08:00 | "
        "https://publisher.example.org/; venue=example | no_hit | 0 | — | "
        f"pages=1; final_cursor=end | {WEEK_END} | coverage:PUB-A:week | — |\n"
    )
    text = text.replace("\n\n## 2. Candidate Ledger", "\n" + row + "\n## 2. Candidate Ledger")
    text = text.replace("| coverage | coverage:ORG-A:2026-08-25 |",
                        "| coverage | coverage:ORG-A:2026-08-25; coverage:PUB-A:week |")
    return text + ("\n<!-- coverage:PUB-A:week:start -->\n"
                   "Full natural-week publication result set enumerated through Monday 00:00.\n"
                   "<!-- coverage:PUB-A:week:end -->\n")


class ResearchPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()
        cls.registry, errors = cls.validator.validate_registry_text(VALID_REGISTRY)
        assert not errors, errors

    def validate(self, text, registry=None):
        return self.validator.validate_report_text(text, registry or self.registry, strict=True)

    def test_exact_daily_window_and_legacy_compatibility(self):
        self.assertEqual([], self.validate(strict_daily()))
        self.assertEqual([], self.validate(VALID_DAILY_V21))

    def test_receipt_must_equal_declared_daily_window(self):
        for start in ("2026-08-23T09:00:00+08:00", DAILY_END,
                      "2026-08-24T12:00:00+08:00"):
            with self.subTest(start=start):
                text = change_receipt(strict_daily(), **{"Window Start": start})
                self.assertTrue(self.validate(text), "48h, zero-length and truncated receipts must fail")

    def test_shifted_24h_daily_requires_explicit_override(self):
        text = strict_daily().replace("09:00:00", "10:00:00")
        self.assertTrue(self.validate(text))
        text = text.replace("| Contract Version | V2.2 |",
                            "| Contract Version | V2.2 |\n| Window Override Reason | "
                            "User requested 10:00 Beijing cutoff for this replay |")
        self.assertEqual([], self.validate(text))

    def test_receipt_window_uses_timezone_aware_instants(self):
        text = change_receipt(strict_daily(), **{
            "Window Start": "2026-08-24T01:00:00+00:00",
            "Window End": "2026-08-25T01:00:00+00:00",
        })
        self.assertEqual([], self.validate(text))
        text = change_receipt(strict_daily(), **{
            "Window Start": "2026-08-23T13:00:00-12:00",
            "Window End": "2026-08-24T13:00:00-12:00",
        })
        self.assertEqual([], self.validate(text))

    def test_important_revision_can_integrate_after_completed_review(self):
        self.assertEqual([], self.validate(revision_report()))

    def test_revision_cannot_integrate_without_revision_contract(self):
        for changes in ({"Owner Report Ref": "—"}, {"Owner Report Ref": "self"},
                        {"Reconciliation": "new_in_window", "Owner Report Ref": "self"}):
            with self.subTest(changes=changes):
                self.assertTrue(self.validate(revision_report(**changes)))
        invalid = revision_report().replace("| important_revision |", "| none |")
        self.assertTrue(self.validate(invalid))

    def test_triggered_weekly_source_can_close_all_daily_hits_before_denominator(self):
        text = add_receipt(strict_daily(), "PUB-A")
        self.assertIn("| checked | 1 | — |", text)
        self.assertEqual([], self.validate(text))
        self.assertEqual(1, len(records.extract(text)["families"]))

    def test_untriggered_extra_weekly_sweep_still_fails(self):
        self.assertTrue(self.validate(add_receipt(strict_daily(), "PUB-A", trigger=False)))

    def test_supporting_candidate_does_not_replace_source_trigger(self):
        text = add_receipt(strict_daily(), "PUB-A", trigger=False)
        text = text.replace("| checked | 1 | — |", "| checked | 1 | SF-001 |")
        canonical = records.extract(text)
        canonical["families"][0]["Supporting Source IDs"] = "ORG-A; PUB-A"
        self.assertTrue(self.validate(records.render(text, canonical)))

    def test_trigger_is_bound_to_source_and_current_window(self):
        text = add_receipt(strict_daily(), "PUB-A")
        for broken in (text.replace("Source ID: PUB-A.", "Source ID: ORG-A."),
                       text.replace("official 2026-08-25T08:00:00+08:00", "official 2025-08-25T08:00:00+08:00")):
            with self.subTest(broken=broken[-500:]):
                self.assertTrue(self.validate(broken))

    def test_trigger_timestamp_cannot_silently_become_date_only(self):
        text = add_receipt(strict_daily(), "PUB-A")
        for timestamp in ("2026-08-25T10:00:00.000+08:00", "2026-08-25T10:00:00",
                          "2026-08-25T10:00:00+0800", "2026-08-25T09:00:00+08:00"):
            with self.subTest(timestamp=timestamp):
                self.assertTrue(self.validate(text.replace("2026-08-25T08:00:00+08:00", timestamp)))
        self.assertEqual([], self.validate(text.replace("2026-08-25T08:00:00+08:00",
                                                       "2026-08-25T08:00:00.123+08:00")))

    def test_trigger_reference_requires_concrete_bounded_event(self):
        text = add_receipt(strict_daily(), "PUB-A")
        start = text.index("<!-- trigger:PUB-A-release:start -->")
        end = text.index("<!-- trigger:PUB-A-release:end -->", start)
        generic = text[:start] + "<!-- trigger:PUB-A-release:start -->\nA relevant event happened.\n" + text[end:]
        self.assertTrue(self.validate(generic))
        self.assertTrue(self.validate(text.replace("<!-- trigger:PUB-A-release:start -->", "")))

    def test_reachable_source_with_exhausted_date_recovery_is_conditional(self):
        registry = dict(self.registry)
        registry["ORG-B"] = dict(registry["ORG-A"])
        text = add_receipt(strict_daily(), "ORG-B", trigger=False, failed=True)
        text = text.replace("Complete", "Conditional").replace("Coverage=Closed", "Coverage=Conditional Pass")
        text = text.replace("Books=Passed", "Books=Conditional Pass")
        text = text.replace("| Coverage Gate | Closed |", "| Coverage Gate | Conditional Pass |")
        text = text.replace("| Books Gate | Passed |", "| Books Gate | Conditional Pass |")
        request = SOURCE_MATERIALS_REQUEST.replace("ORG-A", "ORG-B")
        request = request.replace("complete endpoint result set", "precise first-public timestamps")
        request = request.replace("deterministic source could not be enumerated",
                                  "source is reachable, but official HTML, feed and API expose only a date; "
                                  "bounded timestamp recovery is exhausted and window ownership remains unknown")
        self.assertTrue(self.validate(text, registry))
        self.assertEqual([], self.validate(text + request, registry))
        families = records.extract(text + request)["families"]
        self.assertEqual(["SF-001"], [row["Source Family ID"] for row in families])
        self.assertNotIn("ORG-B", families[0]["Supporting Source IDs"])

    def test_score_four_may_complete_deeper_review_and_project_actual_route(self):
        for route in ("standard", "deep"):
            with self.subTest(route=route):
                text = strict_daily()
                canonical = records.extract(text)
                canonical["families"][0].update({"Design Delta": "2", "System Reach": "1",
                                                "Durability": "1", "Candidate State": "closure_only",
                                                "Review Status": route + "_complete"})
                rendered = records.render(text, canonical)
                self.assertEqual([], self.validate(rendered))
                rows, errors = self.validator._expect_columns(rendered, self.validator.REVIEW_COMPLETION_MARKER,
                                                            self.validator.REVIEW_COMPLETION_COLUMNS)
                self.assertEqual([], errors)
                self.assertEqual(route, rows[0]["Review Route"])
                self.assertEqual([], records.drift(rendered, canonical))

    def test_required_deep_review_cannot_be_downgraded(self):
        for override in ("none", "important_revision"):
            with self.subTest(override=override):
                text = strict_daily()
                canonical = records.extract(text)
                canonical["families"][0].update({"Review Override": override,
                                                "Review Status": "standard_complete"})
                if override != "none":
                    canonical["families"][0].update({"Design Delta": "2", "System Reach": "1", "Durability": "1"})
                with self.assertRaises(ValueError):
                    records.render(text, canonical)
                self.assertTrue(self.validate(text.replace("| deep_complete |", "| standard_complete |")))

    def test_pending_and_blocked_receipts_keep_the_minimum_route(self):
        for status in ("pending", "blocked"):
            for scores, override, expected in (("211", "none", "closure"),
                                               ("222", "none", "standard"),
                                               ("322", "none", "deep"),
                                               ("211", "important_revision", "deep")):
                with self.subTest(status=status, scores=scores, override=override):
                    text = strict_daily()
                    canonical = records.extract(text)
                    family = canonical["families"][0]
                    family.update(dict(zip(("Design Delta", "System Reach", "Durability"), scores)))
                    family.update({"Review Status": status, "Review Override": override})
                    rendered = records.render(text, canonical)
                    rows, errors = self.validator._expect_columns(
                        rendered, self.validator.REVIEW_COMPLETION_MARKER,
                        self.validator.REVIEW_COMPLETION_COLUMNS,
                    )
                    self.assertEqual([], errors)
                    self.assertEqual(expected, rows[0]["Review Route"])

    def test_natural_week_can_close_on_next_monday(self):
        self.assertEqual([], self.validate(natural_weekly()))

    def test_sunday_nine_cutoff_cannot_close_natural_week(self):
        text = change_receipt(natural_weekly(), **{"Window End": "2026-08-30T09:00:00+08:00",
                                                 "Window Watermark": "2026-08-30T09:00:00+08:00"})
        self.assertTrue(self.validate(text))

    def test_weekly_receipt_cannot_close_before_next_monday(self):
        text = change_receipt(natural_weekly(), **{"Executed At": "2026-08-30T09:00:00+08:00"})
        self.assertTrue(self.validate(text))
