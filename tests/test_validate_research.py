import importlib.util
import hashlib
import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_research.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_research", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


VALID_REGISTRY = """\
# Sources

注册表版本：2026-08-25
生效日期：2026-08-25

<!-- validator:source-registry-v1 -->
| Source ID | Source Group | Authority Role | Cadence | Official Endpoints | Event Trigger / Topic Filter | Date Semantics | Pagination / Cursor | Expected Coverage Receipt | Allowed Claim Scope | Fallback | Effective Date | Aliases |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ORG-A | Model organization | Creator Primary | Required Daily | https://example.com/research | release or paper | first public | all pages | checked/no-hit plus cursor | public mechanism and artifact | PUB-A | 2026-08-25 | Example AI |
| PUB-A | Formal publication | Formal Publisher | Required Weekly | https://publisher.example.org/ | venue filter | formal publication | full result set | checked/no-hit plus query | DOI, venue and formal version | — | 2026-08-25 | Example Proceedings |
<!-- validator:source-registry-end -->
"""


VALID_DAILY = """\
# Daily

Score Schema: V2

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-25 |
| Window End | 2026-08-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Denominator ID | DEN-2026-08-25-FULL-001 |
| Previous Denominator ID | — |
| Denominator Frozen At | 2026-08-25T23:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

<!-- validator:source-coverage-v1 -->
| Source ID | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- |
| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |

<!-- validator:candidate-ledger-v2 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 | 2026-W35 | 2026-08-25 | ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-001 | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |

<!-- review:SF-001 -->
Primary evidence was reviewed; the mechanism and claim boundary are recorded here.
<!-- books-review:SF-001 -->
The owner chapter and its adjacent chapters were reviewed for existing coverage.
"""


VALID_DAILY_V21 = """\
# Daily Research — 2026-08-25

**Research Date:** 2026-08-25

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-24 09:00:00 ～ 2026-08-25 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed

## Executive Summary

The frozen denominator, evidence review, selection, Books comparison, and semantic audit are complete.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-25 |
| Window End | 2026-08-25 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Denominator ID | DEN-2026-08-25-V21-001 |
| Previous Denominator ID | — |
| Denominator Frozen At | 2026-08-25T23:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ORG-A | 2026-08-23T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | https://example.com/research; release or paper | checked | 1 | SF-001 | page=1; final_cursor=end | 2026-08-25T09:00:00+08:00 | coverage:ORG-A:2026-08-25 | — |

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 | 2026-W35 | 2026-08-25 | ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-001 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-001 | RP-1188b619ab6e379d | deep | arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 | arXiv:2608.00001v1#section-3 | arXiv:2608.00001v1#table-2 | arXiv:2608.00001v1#limitations | Not Disclosed — v1 links no artifact | claim:SF-001 | complete |

### Source Reviews

<!-- review:SF-001:start -->
<!-- claim:SF-001:start -->
The cited method, evaluation, limitations, and missing artifact define this bounded claim.
<!-- claim:SF-001:end -->
<!-- review:SF-001:end -->

## 4. Benchmark Contracts

None — the candidate does not make an empirical benchmark claim.

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| AUD-COV-001 | fresh-context:noether | coverage | coverage:ORG-A:2026-08-25 | none | Not Required — no unresolved coverage finding | passed |
| AUD-EVD-001 | fresh-context:noether | evidence | review:SF-001; claim:SF-001 | none | Not Required — no unresolved evidence finding | passed |
| AUD-DA-001 | fresh-context:noether | deep_analysis_selection | analysis:DA-001 | none | Not Required — no unresolved selection finding | passed |
| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 | none | Not Required — no unresolved Books finding | passed |

<!-- coverage:ORG-A:2026-08-25:start -->
Executed receipt for the declared endpoint, window, watermark, and final cursor.
<!-- coverage:ORG-A:2026-08-25:end -->

<!-- analysis:DA-001:start -->
The selected narrative compares the prior mechanism, changed constraint, evidence boundary, and trade-off.
<!-- analysis:DA-001:end -->

<!-- books-review:SF-001:start -->
<!-- existing:SF-001:start -->
The target chapter already owns the mechanism under the cited proposition.
<!-- existing:SF-001:end -->
<!-- delta:SF-001:start -->
The new evidence narrows the boundary but does not change the existing proposition.
<!-- delta:SF-001:end -->
<!-- books-review:SF-001:end -->

## 8. Ignored Noise

None.

## 9. Recommended Action

Preserve the existing Books proposition.

## 10. Repository Changes

None.

## 11. Open Questions

None.

## 12. Sources

- [Example primary source](https://example.com/research)

## 13. Final Status

Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.
"""


MATERIALS_REQUEST = """
<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-SF-001-01 | P1 Full Text | SF-001 | — | — | 2026-W35 | arXiv:2608.00001 | event-time full text | abstract cannot establish mechanism | author manuscript | SF-001-v1.pdf | method, experiments, limitations |
"""


WITHDRAWN_PRIMARY_SOURCE_CLOSURE = """
### Pre-denominator Closures

| Source Family ID | Primary Identifier | Pre-denominator Closure | Authority Status Ref |
| --- | --- | --- | --- |
| SF-001 | arXiv:2608.00001v1 | withdrawn_primary_source | https://example.com/research#withdrawn |
"""


SOURCE_MATERIALS_REQUEST = """
<!-- validator:materials-request-v1 -->
| Request ID | Priority | Source Family ID | Source ID | Gap / Limitation ID | Owner Week | Known Identifiers / URLs | Missing Material | Why Existing Evidence Is Insufficient | Acceptable Substitute | Suggested File Name | Required Review Scope |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR-ORG-A-01 | P4 Discovery Export | — | ORG-A | GAP-ORG-A-01 | 2026-W35 | https://example.com/research | complete endpoint result set | deterministic source could not be enumerated | endpoint export or official snapshot | ORG-A-2026-08-25.txt | replay source and candidate denominator |
"""


def as_weekly(report_type: str = "Sunday Weekly") -> str:
    report = VALID_DAILY.replace("| Report Type | Daily |", f"| Report Type | {report_type} |")
    report = report.replace("| Window Start | 2026-08-25 |", "| Window Start | 2026-08-24 |")
    report = report.replace("| Window End | 2026-08-25 |", "| Window End | 2026-08-30 |")
    return report.replace(
        "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
        "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |\n"
        "| PUB-A | https://publisher.example.org/; venue=example | no_hit | 0 | — | complete result set | — |",
    )


def historical_without_books() -> str:
    report = as_weekly("Historical Weekly")
    report = report.replace("| Books Gate | Passed |", "| Books Gate | Not Applicable |")
    report = report.replace(
        "| INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |",
        "| — | Not Assessed | — | no |",
    )
    report = report.replace(
        "<!-- books-review:SF-001 -->\n"
        "The owner chapter and its adjacent chapters were reviewed for existing coverage.\n",
        "",
    )
    return report


def as_weekly_v21(report_type: str = "Sunday Weekly") -> str:
    report = VALID_DAILY_V21.replace("| Report Type | Daily |", f"| Report Type | {report_type} |")
    report = report.replace("| Window Start | 2026-08-25 |", "| Window Start | 2026-08-24 |", 1)
    report = report.replace("| Window End | 2026-08-25 |", "| Window End | 2026-08-30 |", 1)
    report = report.replace(
        "| ORG-A | 2026-08-23T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 | https://example.com/research; release or paper | checked | 1 | SF-001 | page=1; final_cursor=end | 2026-08-25T09:00:00+08:00 | coverage:ORG-A:2026-08-25 | — |",
        "| ORG-A | 2026-08-24T00:00:00+08:00 | 2026-08-30T23:59:59+08:00 | 2026-08-30T23:00:00+08:00 | https://example.com/research; release or paper | checked | 1 | SF-001 | page=1; final_cursor=end | 2026-08-30T23:00:00+08:00 | coverage:ORG-A:2026-W35 | — |\n"
        "| PUB-A | 2026-08-24T00:00:00+08:00 | 2026-08-30T23:59:59+08:00 | 2026-08-30T23:05:00+08:00 | https://publisher.example.org/; venue=example | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-30T23:05:00+08:00 | coverage:PUB-A:2026-W35 | — |",
    )
    report = report.replace("coverage:ORG-A:2026-08-25", "coverage:ORG-A:2026-W35")
    report = report.replace(
        "<!-- coverage:ORG-A:2026-W35:end -->",
        "<!-- coverage:ORG-A:2026-W35:end -->\n"
        "<!-- coverage:PUB-A:2026-W35:start -->\n"
        "Executed weekly publication receipt with a final cursor.\n"
        "<!-- coverage:PUB-A:2026-W35:end -->",
    )
    report = report.replace(
        "| coverage | coverage:ORG-A:2026-W35 |",
        "| coverage | coverage:ORG-A:2026-W35; coverage:PUB-A:2026-W35 |",
    )
    return report


def historical_v21_without_books() -> str:
    report = as_weekly_v21("Historical Weekly")
    report = report.replace("| Books Gate | Passed |", "| Books Gate | Not Applicable |")
    report = report.replace(
        "| INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |",
        "| — | Not Assessed | — | no |",
    )
    report = report.replace(
        "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n",
        "",
    )
    report = report.replace(
        "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 | none | Not Required — no unresolved Books finding | passed |",
        "| AUD-BOOK-001 | fresh-context:noether | books | validator:books-comparison-v1 | none | Not Required — Historical Books Gate is frozen | not_applicable |",
    )
    return report


def source_failed_conditional() -> str:
    report = VALID_DAILY.replace("| Completion Status | Complete |", "| Completion Status | Conditional |")
    report = report.replace("| Coverage Gate | Closed |", "| Coverage Gate | Conditional Pass |")
    report = report.replace("| Books Gate | Passed |", "| Books Gate | Conditional Pass |")
    report = report.replace(
        "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
        "| ORG-A | https://example.com/research; release or paper | failed | 0 | — | unavailable | GAP-ORG-A-01 |",
    )
    report = report.replace(
        "| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 | 2026-W35 | 2026-08-25 | ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-001 | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |\n",
        "",
    )
    report = report.replace(
        "<!-- review:SF-001 -->\n"
        "Primary evidence was reviewed; the mechanism and claim boundary are recorded here.\n"
        "<!-- books-review:SF-001 -->\n"
        "The owner chapter and its adjacent chapters were reviewed for existing coverage.\n",
        "",
    )
    return report


def write_contract_root(root: Path) -> None:
    (root / "docs").mkdir()
    (root / "docs" / "RESEARCH_SOURCES.md").write_text(VALID_REGISTRY, encoding="utf-8")
    (root / "docs" / "RESEARCH_CONTRACT.md").write_text(
        "Design Delta\nSystem Reach\nDurability\n",
        encoding="utf-8",
    )
    (root / "docs" / "REPORT_CONTRACTS.md").write_text(
        "<!-- validator:report-metadata-v2 -->\n"
        "<!-- validator:source-coverage-v2 -->\n"
        "<!-- validator:candidate-ledger-v2.1 -->\n"
        "<!-- validator:review-completion-v1 -->\n"
        "<!-- validator:deep-analysis-selection-v1 -->\n"
        "<!-- validator:books-comparison-v1 -->\n"
        "<!-- validator:semantic-audit-v1 -->\n"
        "<!-- validator:materials-request-v1 -->\n"
        "| Books Gate | Passed / Conditional Pass / Open / Not Applicable |\n",
        encoding="utf-8",
    )
    links = "\n".join(
        (
            "docs/RESEARCH_CONTRACT.md",
            "docs/RESEARCH_SOURCES.md",
            "docs/REPORT_CONTRACTS.md",
        )
    )
    (root / "CODEX_DAILY_RESEARCH_PROMPT.md").write_text(links, encoding="utf-8")
    (root / "CODEX_HISTORICAL_RESEARCH_PROMPT.md").write_text(links, encoding="utf-8")
    (root / "ROADMAP.md").write_text(
        "| 稳定节点 ID | 当前章节 | 当前路径 | 旧章节 |\n"
        "| --- | ---: | --- | ---: |\n"
        "| `INFER-REQUEST-LIFECYCLE` | Ch42 | `books/example.md` | Ch38 |\n",
        encoding="utf-8",
    )


class RegistryValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_valid_registry_passes(self):
        records, errors = self.validator.validate_registry_text(VALID_REGISTRY)
        self.assertEqual([], errors)
        self.assertEqual({"ORG-A", "PUB-A"}, set(records))

    def test_duplicate_source_id_and_alias_fail(self):
        duplicate = VALID_REGISTRY.replace(
            "| PUB-A | Formal publication",
            "| ORG-A | Formal publication",
        ).replace("Example Proceedings", "Example AI")
        _, errors = self.validator.validate_registry_text(duplicate)
        self.assertTrue(any("duplicate Source ID" in error for error in errors))
        self.assertTrue(any("duplicate alias" in error for error in errors))

    def test_invalid_role_cadence_and_endpoint_fail(self):
        invalid = VALID_REGISTRY.replace("Creator Primary", "Trusted Source", 1)
        invalid = invalid.replace("Required Daily", "Always", 1)
        invalid = invalid.replace("https://example.com/research", "http://example.com/research", 1)
        _, errors = self.validator.validate_registry_text(invalid)
        self.assertTrue(any("Authority Role" in error for error in errors))
        self.assertTrue(any("Cadence" in error for error in errors))
        self.assertTrue(any("HTTPS" in error for error in errors))

    def test_fallback_source_id_must_exist(self):
        invalid = VALID_REGISTRY.replace("| PUB-A | 2026-08-25 | Example AI |", "| MISSING-A | 2026-08-25 | Example AI |")
        _, errors = self.validator.validate_registry_text(invalid)
        self.assertTrue(any("unknown Fallback Source ID MISSING-A" in error for error in errors))

    def test_fallback_graph_must_not_contain_cycles(self):
        cyclic = VALID_REGISTRY.replace(
            "| — | 2026-08-25 | Example Proceedings |",
            "| ORG-A | 2026-08-25 | Example Proceedings |",
        )
        _, errors = self.validator.validate_registry_text(cyclic)
        self.assertTrue(any("Fallback cycle" in error for error in errors))

    def test_fallback_tokens_must_be_valid_source_ids(self):
        lowercase = VALID_REGISTRY.replace(
            "| PUB-A | 2026-08-25 | Example AI |",
            "| pub-a | 2026-08-25 | Example AI |",
        )
        _, errors = self.validator.validate_registry_text(lowercase)
        self.assertTrue(any("invalid Fallback Source ID" in error for error in errors))

        comma_joined = VALID_REGISTRY.replace(
            "| PUB-A | 2026-08-25 | Example AI |",
            "| PUB-A, MISSING-A | 2026-08-25 | Example AI |",
        )
        _, errors = self.validator.validate_registry_text(comma_joined)
        self.assertTrue(any("invalid Fallback Source ID" in error for error in errors))

    def test_registry_markers_must_be_unique_and_ordered(self):
        duplicated = VALID_REGISTRY.replace(
            "<!-- validator:source-registry-v1 -->",
            "<!-- validator:source-registry-v1 -->\n<!-- validator:source-registry-v1 -->",
        )
        _, errors = self.validator.validate_registry_text(duplicated)
        self.assertTrue(any("exactly one" in error for error in errors))


class RoadmapValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_stable_node_ids_are_parsed_from_the_mapping_table(self):
        roadmap = """\
| 稳定节点 ID | 当前章节 | 当前路径 | 旧章节 |
| --- | ---: | --- | ---: |
| `INFER-REQUEST-LIFECYCLE` | Ch42 | `books/example.md` | Ch38 |
| `AGENT-PLATFORM` | Ch84 | `books/agent.md` | Ch80 |
"""
        nodes, errors = self.validator.parse_stable_node_ids(roadmap)
        self.assertEqual([], errors)
        self.assertEqual({"INFER-REQUEST-LIFECYCLE", "AGENT-PLATFORM"}, nodes)

        duplicated = roadmap.replace(
            "| `AGENT-PLATFORM` |",
            "| `INFER-REQUEST-LIFECYCLE` |",
        )
        _, errors = self.validator.parse_stable_node_ids(duplicated)
        self.assertTrue(any("duplicate Stable Node ID" in error for error in errors))


class MarkdownValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_markdown_structure_rejects_heading_jumps_and_unclosed_fences(self):
        invalid = "# Title\n\n### Skipped\n\n```text\nopen\n"
        errors = self.validator.validate_markdown_structure(invalid)
        self.assertTrue(any("heading level jumps" in error for error in errors))
        self.assertTrue(any("unclosed code fence" in error for error in errors))

    def test_markdown_fence_parser_respects_commonmark_closing_rules(self):
        valid = "# Title\n\n```python\n```not-a-close\nvalue = 1\n```\n\n## Next\n"
        self.assertEqual([], self.validator.validate_markdown_structure(valid))

        indented = "# Title\n\n    ```\n    indented code\n\n## Next\n"
        self.assertEqual([], self.validator.validate_markdown_structure(indented))

    def test_local_markdown_links_must_resolve(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "repo"
            root.mkdir()
            docs = root / "docs"
            docs.mkdir()
            page = docs / "page.md"
            target = docs / "target.md"
            target.write_text("# Target\n", encoding="utf-8")
            text = "# Page\n\n[ok](./target.md) [anchor](#section) [web](https://example.com)\n"
            self.assertEqual([], self.validator.validate_local_markdown_links(text, page, root))

            errors = self.validator.validate_local_markdown_links(
                text + "[missing](./missing.md)\n", page, root
            )
            self.assertTrue(any("missing local Markdown link" in error for error in errors))

            nested = docs / "target_(v1).md"
            nested.write_text("# Nested\n", encoding="utf-8")
            self.assertEqual(
                [],
                self.validator.validate_local_markdown_links(
                    "[nested](./target_(v1).md)\n", page, root
                ),
            )

            outside = root.parent / "outside.md"
            outside.write_text("# Outside\n", encoding="utf-8")
            errors = self.validator.validate_local_markdown_links(
                "[outside](../../outside.md)\n", page, root
            )
            self.assertTrue(any("escapes repository root" in error for error in errors))

            examples = (
                "```markdown\n[example](./missing-from-fence.md)\n```\n"
                "`[inline](./missing-from-inline.md)`\n"
            )
            self.assertEqual(
                [], self.validator.validate_local_markdown_links(examples, page, root)
            )


class ReportValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()
        cls.registry, errors = cls.validator.validate_registry_text(VALID_REGISTRY)
        if errors:
            raise AssertionError(errors)

    def test_valid_daily_v2_passes(self):
        self.assertEqual([], self.validator.validate_report_text(VALID_DAILY, self.registry))

    def test_score_schema_is_owned_by_metadata_not_free_prose(self):
        without_prose = VALID_DAILY.replace("Score Schema: V2\n\n", "")
        self.assertEqual([], self.validator.validate_report_text(without_prose, self.registry))

        missing_metadata = VALID_DAILY.replace("| Score Schema | V2 |\n", "")
        errors = self.validator.validate_report_text(missing_metadata, self.registry)
        self.assertTrue(any("Score Schema" in error for error in errors))

        wrong_metadata = VALID_DAILY.replace("| Score Schema | V2 |", "| Score Schema | V1 |")
        errors = self.validator.validate_report_text(wrong_metadata, self.registry)
        self.assertTrue(any("Score Schema" in error for error in errors))

    def test_required_source_receipt_is_mandatory(self):
        missing = VALID_DAILY.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |\n",
            "",
        )
        errors = self.validator.validate_report_text(missing, self.registry)
        self.assertTrue(any("missing due Source ID ORG-A" in error for error in errors))

    def test_failed_source_requires_gap_and_open_gate(self):
        failed = VALID_DAILY.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
            "| ORG-A | https://example.com/research; release or paper | failed | 0 | — | unknown | — |",
        )
        errors = self.validator.validate_report_text(failed, self.registry)
        self.assertTrue(any("requires Gap / Limitation ID" in error for error in errors))
        self.assertTrue(any("Coverage Gate cannot be Closed" in error for error in errors))

    def test_failed_non_deterministic_discovery_receipt_does_not_block_coverage(self):
        registry_text = VALID_REGISTRY.replace(
            "| all pages | checked/no-hit plus cursor |",
            "| Non-deterministic backstop; save visible window | checked/no-hit plus cursor |",
            1,
        )
        registry, registry_errors = self.validator.validate_registry_text(registry_text)
        self.assertEqual([], registry_errors)
        failed = VALID_DAILY.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
            "| ORG-A | https://example.com/research; release or paper | failed | 0 | — | unavailable | GAP-DISCOVERY-001 |",
        )
        errors = self.validator.validate_report_text(failed, registry)
        self.assertFalse(any("Coverage Gate cannot be Closed" in error for error in errors))

    def test_score_total_range_and_review_route_are_checked(self):
        invalid = VALID_DAILY.replace(
            "| ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete |",
            "| ORG-A | 4 | 2 | 2 | 9 | retained | standard_complete |",
        )
        errors = self.validator.validate_report_text(invalid, self.registry)
        self.assertTrue(any("between 0 and 3" in error for error in errors))
        self.assertTrue(any("Total" in error for error in errors))
        self.assertTrue(any("deep_complete" in error for error in errors))

    def test_pending_review_cannot_pass_evidence_gate(self):
        pending = VALID_DAILY.replace("deep_complete", "pending")
        errors = self.validator.validate_report_text(pending, self.registry)
        self.assertTrue(any("Evidence Gate cannot be Passed" in error for error in errors))

    def test_complete_report_requires_terminal_gates(self):
        incomplete = VALID_DAILY.replace("| Coverage Gate | Closed |", "| Coverage Gate | Open |")
        errors = self.validator.validate_report_text(incomplete, self.registry)
        self.assertTrue(any("Completion Status Complete" in error for error in errors))

        conditional = VALID_DAILY.replace("| Coverage Gate | Closed |", "| Coverage Gate | Conditional Pass |")
        errors = self.validator.validate_report_text(conditional, self.registry)
        self.assertTrue(any("Completion Status Complete" in error for error in errors))

    def test_historical_books_gate_not_applicable_is_a_terminal_value(self):
        historical = historical_without_books()
        self.assertEqual([], self.validator.validate_report_text(historical, self.registry))

    def test_in_progress_cannot_have_all_terminal_gates_without_pending_work(self):
        invalid = VALID_DAILY.replace("| Completion Status | Complete |", "| Completion Status | In Progress |")
        errors = self.validator.validate_report_text(invalid, self.registry)
        self.assertTrue(any("In Progress conflicts with terminal gates" in error for error in errors))

    def test_blocked_evidence_requires_conditional_or_open_gate(self):
        blocked = VALID_DAILY.replace("accessible", "blocked")
        blocked = blocked.replace("No Change — Existing Coverage", "Blocked / Unverified")
        errors = self.validator.validate_report_text(blocked, self.registry)
        self.assertTrue(any("Evidence Gate cannot be Passed" in error for error in errors))

    def test_books_gate_passed_requires_final_disposition(self):
        undecided = VALID_DAILY.replace("No Change — Existing Coverage", "Not Assessed")
        errors = self.validator.validate_report_text(undecided, self.registry)
        self.assertTrue(any("Books Gate cannot be Passed" in error for error in errors))

        pending = VALID_DAILY.replace("deep_complete", "pending")
        pending = pending.replace("No Change — Existing Coverage", "Not Assessed")
        pending = pending.replace("| Completion Status | Complete |", "| Completion Status | In Progress |")
        pending = pending.replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |")
        errors = self.validator.validate_report_text(pending, self.registry)
        self.assertTrue(any("Books Gate cannot be Passed while pending work exists" in error for error in errors))

    def test_owner_week_must_match_first_public_date(self):
        wrong_owner = VALID_DAILY.replace("2026-W35", "2026-W34")
        errors = self.validator.validate_report_text(wrong_owner, self.registry)
        self.assertTrue(any("Owner Week" in error for error in errors))

    def test_daily_first_discovery_is_scored_even_when_first_public_is_older(self):
        recovered = VALID_DAILY.replace("2026-W35 | 2026-08-25", "2026-W34 | 2026-08-18")
        self.assertEqual([], self.validator.validate_report_text(recovered, self.registry))

    def test_daily_cannot_use_spillback_to_skip_scoring(self):
        unscored = VALID_DAILY.replace(
            "| 3 | 2 | 2 | 7 | retained |",
            "| — | — | — | — | spillback |",
        )
        errors = self.validator.validate_report_text(unscored, self.registry)
        self.assertTrue(any("Daily candidate cannot use spillback" in error for error in errors))

    def test_weekly_scoring_owner_must_belong_to_weekly_window(self):
        wrong_window = as_weekly().replace("2026-W35 | 2026-08-25", "2026-W34 | 2026-08-18")
        errors = self.validator.validate_report_text(wrong_window, self.registry)
        self.assertTrue(any("outside report window" in error for error in errors))

    def test_blocked_or_disputed_cannot_integrate(self):
        blocked = VALID_DAILY.replace("accessible", "blocked")
        blocked = blocked.replace("No Change — Existing Coverage", "Integrate")
        errors = self.validator.validate_report_text(blocked, self.registry)
        self.assertTrue(any("cannot use Books Disposition Integrate" in error for error in errors))

    def test_vendor_benchmark_requires_bound_contract(self):
        benchmark = VALID_DAILY.replace("| no |\n", "| yes |\n")
        errors = self.validator.validate_report_text(benchmark, self.registry)
        self.assertTrue(any("benchmark-contract-v1" in error for error in errors))

    def test_benchmark_contract_is_bidirectional(self):
        benchmark_table = """
<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-001 | task | model | gpu | bf16 | 1k | 1k | 1 | 1 | p99 | evaluator |
"""
        errors = self.validator.validate_report_text(VALID_DAILY + benchmark_table, self.registry)
        self.assertTrue(any("Benchmark Claim" in error for error in errors))

    def test_completed_review_requires_html_ref_marker(self):
        missing_ref = VALID_DAILY.replace("\n<!-- review:SF-001 -->\n", "\n")
        errors = self.validator.validate_report_text(missing_ref, self.registry)
        self.assertTrue(any("Review Ref" in error for error in errors))

        wrong_family_ref = VALID_DAILY.replace("review:SF-001", "review:SF-OTHER")
        errors = self.validator.validate_report_text(wrong_family_ref, self.registry)
        self.assertTrue(any("must equal review:SF-001" in error for error in errors))

        empty_review_body = VALID_DAILY.replace(
            "Primary evidence was reviewed; the mechanism and claim boundary are recorded here.\n",
            "",
        )
        errors = self.validator.validate_report_text(empty_review_body, self.registry)
        self.assertTrue(any("Review Ref review:SF-001 requires evidence body" in error for error in errors))

        empty_books_body = VALID_DAILY.replace(
            "The owner chapter and its adjacent chapters were reviewed for existing coverage.\n",
            "",
        )
        errors = self.validator.validate_report_text(empty_books_body, self.registry)
        self.assertTrue(any("Books Review Ref books-review:SF-001 requires evidence body" in error for error in errors))

    def test_integrate_requires_deep_accessible_node_and_books_review_ref(self):
        integrated = VALID_DAILY.replace("No Change — Existing Coverage", "Integrate")
        self.assertEqual([], self.validator.validate_report_text(integrated, self.registry))

        shallow = integrated.replace("deep_complete", "standard_complete")
        errors = self.validator.validate_report_text(shallow, self.registry)
        self.assertTrue(any("Integrate requires deep_complete" in error for error in errors))

        missing_books_review = VALID_DAILY.replace(" | books-review:SF-001 | no |", " | — | no |")
        missing_books_review = missing_books_review.replace("\n<!-- books-review:SF-001 -->", "")
        errors = self.validator.validate_report_text(missing_books_review, self.registry)
        self.assertTrue(any("No Change — Existing Coverage requires Books Review Ref" in error for error in errors))

        errors = self.validator.validate_report_text(
            integrated,
            self.registry,
            stable_node_ids={"AGENT-PLATFORM"},
        )
        self.assertTrue(any("unknown Stable Node ID INFER-REQUEST-LIFECYCLE" in error for error in errors))

        self.assertEqual(
            [],
            self.validator.validate_report_text(
                integrated,
                self.registry,
                stable_node_ids={"INFER-REQUEST-LIFECYCLE"},
            ),
        )

    def test_no_change_requires_completed_accessible_evidence(self):
        pending = VALID_DAILY.replace("deep_complete", "pending")
        pending = pending.replace("| Completion Status | Complete |", "| Completion Status | In Progress |")
        pending = pending.replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |")
        errors = self.validator.validate_report_text(pending, self.registry)
        self.assertTrue(any("No Change — Existing Coverage requires completed evidence review" in error for error in errors))

        partial = VALID_DAILY.replace("accessible", "partial")
        errors = self.validator.validate_report_text(partial, self.registry)
        self.assertTrue(any("No Change — Existing Coverage requires Access Status accessible" in error for error in errors))

    def test_books_disposition_and_access_status_do_not_conflict(self):
        blocked = VALID_DAILY.replace("No Change — Existing Coverage", "Blocked / Unverified")
        errors = self.validator.validate_report_text(blocked, self.registry)
        self.assertTrue(any("Blocked / Unverified requires" in error for error in errors))

        disputed = VALID_DAILY.replace("No Change — Existing Coverage", "Disputed")
        errors = self.validator.validate_report_text(disputed, self.registry)
        self.assertTrue(any("Disputed requires Access Status disputed" in error for error in errors))

    def test_structural_candidate_must_not_claim_an_existing_stable_node(self):
        structural = VALID_DAILY.replace("No Change — Existing Coverage", "Structural Candidate")
        errors = self.validator.validate_report_text(structural, self.registry)
        self.assertTrue(any("Structural Candidate requires Stable Node ID to be absent" in error for error in errors))

        without_owner = structural.replace("INFER-REQUEST-LIFECYCLE", "—")
        self.assertEqual([], self.validator.validate_report_text(without_owner, self.registry))

    def test_books_not_applicable_is_only_for_frozen_historical_books(self):
        daily = VALID_DAILY.replace("| Books Gate | Passed |", "| Books Gate | Not Applicable |")
        errors = self.validator.validate_report_text(daily, self.registry)
        self.assertTrue(any("Books Gate Not Applicable is allowed only for Historical Weekly" in error for error in errors))

        sunday = as_weekly().replace("| Books Gate | Passed |", "| Books Gate | Not Applicable |")
        errors = self.validator.validate_report_text(sunday, self.registry)
        self.assertTrue(any("Books Gate Not Applicable is allowed only for Historical Weekly" in error for error in errors))

        historical_with_decision = as_weekly("Historical Weekly").replace(
            "| Books Gate | Passed |", "| Books Gate | Not Applicable |"
        )
        errors = self.validator.validate_report_text(historical_with_decision, self.registry)
        self.assertTrue(any("Books Gate Not Applicable requires Books Disposition Not Assessed" in error for error in errors))

        historical_integrate = historical_with_decision.replace(
            "No Change — Existing Coverage", "Integrate"
        )
        errors = self.validator.validate_report_text(historical_integrate, self.registry)
        self.assertTrue(any("Books Gate Not Applicable requires Books Disposition Not Assessed" in error for error in errors))

        self.assertEqual([], self.validator.validate_report_text(historical_without_books(), self.registry))

    def test_books_passed_requires_closed_coverage_and_passed_evidence(self):
        coverage_open = VALID_DAILY.replace("| Coverage Gate | Closed |", "| Coverage Gate | Open |")
        errors = self.validator.validate_report_text(coverage_open, self.registry)
        self.assertTrue(any("Books Gate Passed requires Coverage Gate Closed" in error for error in errors))

        evidence_open = VALID_DAILY.replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |")
        errors = self.validator.validate_report_text(evidence_open, self.registry)
        self.assertTrue(any("Books Gate Passed requires Evidence Gate Passed" in error for error in errors))

        blocked = VALID_DAILY.replace("accessible", "blocked")
        blocked = blocked.replace("No Change — Existing Coverage", "Blocked / Unverified")
        blocked = blocked.replace("| Completion Status | Complete |", "| Completion Status | Conditional |")
        blocked = blocked.replace("| Evidence Gate | Passed |", "| Evidence Gate | Conditional Pass |")
        blocked = blocked + MATERIALS_REQUEST
        errors = self.validator.validate_report_text(blocked, self.registry)
        self.assertTrue(any("Books Gate cannot be Passed while unresolved evidence exists" in error for error in errors))

    def test_no_hit_must_have_zero_hits_and_no_families(self):
        invalid = VALID_DAILY.replace(
            "| checked | 1 | SF-001 |",
            "| no_hit | 1 | SF-001 |",
        )
        errors = self.validator.validate_report_text(invalid, self.registry)
        self.assertTrue(any("no_hit requires Hits 0" in error for error in errors))
        self.assertTrue(any("no_hit cannot list candidate families" in error for error in errors))

    def test_not_due_requires_a_concrete_trigger_or_filter_receipt(self):
        event_registry_text = VALID_REGISTRY.replace(
            "<!-- validator:source-registry-end -->",
            "| EVENT-A | Event source | Creator Primary | Event Trigger | https://event.example.org/ | release trigger | first public | full feed | trigger receipt | public release | ORG-A | 2026-08-25 | Example Events |\n"
            "<!-- validator:source-registry-end -->",
        )
        event_registry, registry_errors = self.validator.validate_registry_text(event_registry_text)
        self.assertEqual([], registry_errors)
        generic = VALID_DAILY.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |\n"
            "| EVENT-A | 未触发 | not_due | 0 | — | release feed checked | — |",
        )
        errors = self.validator.validate_report_text(generic, event_registry)
        self.assertTrue(any("not_due requires a concrete Endpoint / Filter" in error for error in errors))

        concrete = generic.replace("| EVENT-A | 未触发 |", "| EVENT-A | https://event.example.org/; release trigger |")
        self.assertEqual([], self.validator.validate_report_text(concrete, event_registry))

    def test_required_sources_cannot_emit_not_due_receipts(self):
        invalid = VALID_DAILY.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |\n"
            "| PUB-A | https://publisher.example.org/; next weekly run | not_due | 0 | — | venue checked | — |",
        )
        errors = self.validator.validate_report_text(invalid, self.registry)
        self.assertTrue(any("Required source PUB-A cannot use not_due" in error for error in errors))

        premature = invalid.replace("not_due | 0", "no_hit | 0")
        errors = self.validator.validate_report_text(premature, self.registry)
        self.assertTrue(any("non-due Required source PUB-A must be omitted" in error for error in errors))
        self.assertEqual([], self.validator.validate_report_text(VALID_DAILY, self.registry))

    def test_non_due_required_source_may_be_checked_supporting_evidence(self):
        report = VALID_DAILY.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |",
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |\n"
            "| PUB-A | https://publisher.example.org/exact-report; exact supporting report | checked | 1 | SF-001 | end | — |",
        )
        report = report.replace(
            "| 2026-08-25 | ORG-A | 3 |",
            "| 2026-08-25 | ORG-A;PUB-A | 3 |",
        )
        self.assertEqual([], self.validator.validate_report_text(report, self.registry))

    def test_historical_daily_may_preserve_optional_arxiv_zero_hit_receipt(self):
        registry_text = VALID_REGISTRY.replace(
            "<!-- validator:source-registry-end -->",
            "| SRC-ARXIV | Academic preprint | Primary Manuscript | Required Daily | "
            "https://arxiv.org/ | paper | announcement owner | all pages | checked/no-hit "
            "plus cursor | manuscript identity and claims | — | 2026-08-25 | arXiv |\n"
            "<!-- validator:source-registry-end -->",
        )
        registry, registry_errors = self.validator.validate_registry_text(registry_text)
        self.assertEqual([], registry_errors)
        report = VALID_DAILY_V21.replace(
            "**Contract:** V2.1 Full Replay",
            "**Contract:** V2.1 Historical Daily Full Replay",
        ).replace("2026-08-25", "2026-08-01").replace(
            "2026-08-24", "2026-07-31"
        ).replace(
            "2026-08-23", "2026-07-31"
        ).replace(
            "| Registry Version | 2026-08-01 |", "| Registry Version | 2026-08-25 |"
        ).replace("2026-W35", "2026-W31")
        arxiv_receipt = (
            "| SRC-ARXIV | 2026-07-31T09:00:00+08:00 | 2026-08-01T09:00:00+08:00 | "
            "2026-09-03T21:15:00+08:00 | official owner replay | no_hit | 0 | — | "
            "pages=1; final_cursor=end; rows=0 | 2026-08-01T09:00:00+08:00 | "
            "coverage:SRC-ARXIV:20260801 | — |\n\n"
            "<!-- coverage:SRC-ARXIV:20260801:start -->zero owner rows; cursor closed"
            "<!-- coverage:SRC-ARXIV:20260801:end -->\n"
        )
        report = report.replace("\n## 2. Candidate Ledger", "\n" + arxiv_receipt + "\n## 2. Candidate Ledger")
        self.assertEqual([], self.validator.validate_report_text(report, registry))

    def test_checked_hits_require_candidate_families(self):
        invalid = VALID_DAILY.replace("| checked | 1 | SF-001 |", "| checked | 1 | — |")
        errors = self.validator.validate_report_text(invalid, self.registry)
        self.assertTrue(any("checked source with Hits greater than 0" in error for error in errors))

    def test_receipt_and_candidate_ledger_are_bidirectionally_reconciled(self):
        unknown_family = VALID_DAILY.replace("| checked | 1 | SF-001 |", "| checked | 1 | SF-MISSING |")
        errors = self.validator.validate_report_text(unknown_family, self.registry)
        self.assertTrue(any("receipt family SF-MISSING" in error for error in errors))

        missing_support = VALID_DAILY.replace("| 2026-08-25 | ORG-A | 3 |", "| 2026-08-25 | PUB-A | 3 |")
        errors = self.validator.validate_report_text(missing_support, self.registry)
        self.assertTrue(any("Supporting Source ID PUB-A" in error for error in errors))

    def test_closure_only_replaces_below_threshold_and_matches_score(self):
        closure = VALID_DAILY.replace(
            "| ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete |",
            "| ORG-A | 1 | 1 | 1 | 3 | closure_only | closure_complete |",
        )
        self.assertEqual([], self.validator.validate_report_text(closure, self.registry))

        old_state = closure.replace("closure_only", "below_threshold")
        errors = self.validator.validate_report_text(old_state, self.registry)
        self.assertTrue(any("invalid Candidate State" in error for error in errors))

        too_high = closure.replace("| 1 | 1 | 1 | 3 |", "| 3 | 3 | 3 | 9 |")
        errors = self.validator.validate_report_text(too_high, self.registry)
        self.assertTrue(any("closure_only requires Score 0-4" in error for error in errors))

    def test_registry_version_and_denominator_freeze_are_validated(self):
        wrong_registry = VALID_DAILY.replace("| Registry Version | 2026-08-25 |", "| Registry Version | 2026-08-24 |")
        errors = self.validator.validate_report_text(wrong_registry, self.registry)
        self.assertTrue(any("Registry Version" in error for error in errors))

        newer_registry_text = VALID_REGISTRY.replace(
            "注册表版本：2026-08-25",
            "注册表版本：2026-08-26",
        ).replace(
            "生效日期：2026-08-25",
            "生效日期：2026-08-26",
        )
        newer_registry, registry_errors = self.validator.validate_registry_text(newer_registry_text)
        self.assertEqual([], registry_errors)
        errors = self.validator.validate_report_text(VALID_DAILY, newer_registry)
        self.assertTrue(any("loaded registry version 2026-08-26" in error for error in errors))

        naive_time = VALID_DAILY.replace(
            "2026-08-25T23:00:00+08:00",
            "2026-08-25T23:00:00",
        )
        errors = self.validator.validate_report_text(naive_time, self.registry)
        self.assertTrue(any("Denominator Frozen At" in error for error in errors))

    def test_daily_due_sources_use_report_window_not_registry_file_date(self):
        registry_text = VALID_REGISTRY.replace(
            "<!-- validator:source-registry-end -->",
            "| SRC-ARXIV | Academic preprint | Primary Manuscript | Required Daily | "
            "https://arxiv.org/ | paper | v1 publication | all pages | checked/no-hit "
            "plus cursor | manuscript identity and claims | — | 2026-07-01 | arXiv |\n"
            "| SRC-EQUAL | Model organization | Creator Primary | Required Daily | "
            "https://equal.example.org/ | paper | first public | all pages | checked/no-hit "
            "plus cursor | creator claims | — | 2026-08-01 | Equal Source |\n"
            "| SRC-LATER | Model organization | Creator Primary | Required Daily | "
            "https://later.example.org/ | paper | first public | all pages | checked/no-hit "
            "plus cursor | creator claims | — | 2026-08-02 | Later Source |\n"
            "<!-- validator:source-registry-end -->",
        )
        registry, registry_errors = self.validator.validate_registry_text(registry_text)
        self.assertEqual([], registry_errors)

        historical = VALID_DAILY_V21.replace(
            "| Window Start | 2026-08-25 |", "| Window Start | 2026-08-01 |"
        ).replace(
            "| Window End | 2026-08-25 |", "| Window End | 2026-08-01 |"
        ).replace(
            "| ORG-A | 2026-08-23T09:00:00+08:00 | 2026-08-25T09:00:00+08:00 |",
            "| SRC-ARXIV | 2026-07-31T09:00:00+08:00 | 2026-08-01T09:00:00+08:00 |",
        ).replace(
            "| 2026-08-25T09:00:00+08:00 | coverage:ORG-A:2026-08-25 |",
            "| 2026-08-01T09:00:00+08:00 | coverage:SRC-ARXIV:2026-08-01 |",
        ).replace("| ORG-A | 3 |", "| SRC-ARXIV | 3 |").replace(
            "ORG-A@arXiv:2608.00001v1", "SRC-ARXIV@arXiv:2608.00001v1"
        ).replace(
            "coverage:ORG-A:2026-08-25", "coverage:SRC-ARXIV:2026-08-01"
        )

        errors = self.validator.validate_report_text(historical, registry)
        self.assertFalse(
            any("missing due Source ID ORG-A" in error for error in errors), errors
        )
        self.assertTrue(
            any("missing due Source ID SRC-EQUAL" in error for error in errors), errors
        )
        self.assertFalse(
            any("missing due Source ID SRC-LATER" in error for error in errors), errors
        )

        missing_arxiv = historical.replace(
            "| SRC-ARXIV | 2026-07-31T09:00:00+08:00 | 2026-08-01T09:00:00+08:00 |",
            "| SRC-NOT-REGISTERED | 2026-07-31T09:00:00+08:00 | 2026-08-01T09:00:00+08:00 |",
        )
        missing_errors = self.validator.validate_report_text(missing_arxiv, registry)
        self.assertTrue(
            any("missing due Source ID SRC-ARXIV" in error for error in missing_errors),
            missing_errors,
        )

    def test_invalid_registry_effective_date_does_not_crash_report_validation(self):
        broken_registry = {key: dict(value) for key, value in self.registry.items()}
        broken_registry["ORG-A"]["Effective Date"] = "not-a-date"
        errors = self.validator.validate_report_text(VALID_DAILY, broken_registry)
        self.assertTrue(any("Effective Date" in error for error in errors))

    def test_full_and_delta_coverage_modes_are_enforced(self):
        invalid_full = VALID_DAILY.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |")
        errors = self.validator.validate_report_text(invalid_full, self.registry)
        self.assertTrue(any("Full Replay" in error for error in errors))

        invalid_previous = VALID_DAILY.replace(
            "| Previous Denominator ID | — |",
            "| Previous Denominator ID | DEN-OLD |",
        )
        errors = self.validator.validate_report_text(invalid_previous, self.registry)
        self.assertTrue(any("Full Replay" in error for error in errors))

        delta = VALID_DAILY.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |")
        delta = delta.replace("| Report Type | Daily |", "| Report Type | Historical Weekly |")
        delta = delta.replace("| Window Start | 2026-08-25 |", "| Window Start | 2026-08-24 |")
        delta = delta.replace("| Window End | 2026-08-25 |", "| Window End | 2026-08-30 |")
        delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |")
        delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |")
        delta = delta.replace(
            "| Previous Denominator ID | — |",
            "| Previous Denominator ID | DEN-2026-08-25-BASE-001 |",
        )
        self.assertEqual([], self.validator.validate_report_text(delta, self.registry))

        missing_changed = delta.replace("| Changed Source IDs | ORG-A |", "| Changed Source IDs | — |")
        errors = self.validator.validate_report_text(missing_changed, self.registry)
        self.assertTrue(any("Delta Audit" in error for error in errors))

        missing_previous = delta.replace(
            "| Previous Denominator ID | DEN-2026-08-25-BASE-001 |",
            "| Previous Denominator ID | — |",
        )
        errors = self.validator.validate_report_text(missing_previous, self.registry)
        self.assertTrue(any("Delta Audit" in error for error in errors))

        daily_delta = delta.replace("| Report Type | Historical Weekly |", "| Report Type | Daily |")
        errors = self.validator.validate_report_text(daily_delta, self.registry)
        self.assertTrue(any("only for Historical Weekly" in error for error in errors))

    def test_historical_full_replay_uses_the_current_registry_due_set(self):
        historical = VALID_DAILY.replace("| Report Type | Daily |", "| Report Type | Historical Weekly |")
        historical = historical.replace("| Window Start | 2026-08-25 |", "| Window Start | 2025-01-06 |")
        historical = historical.replace("| Window End | 2026-08-25 |", "| Window End | 2025-01-12 |")
        historical = historical.replace("| 2026-W35 | 2026-08-25 |", "| 2025-W02 | 2025-01-06 |")
        historical = historical.replace(
            "| ORG-A | https://example.com/research; release or paper | checked | 1 | SF-001 | end | — |\n",
            "",
        )
        errors = self.validator.validate_report_text(historical, self.registry)
        self.assertTrue(any("missing due Source ID ORG-A" in error for error in errors))
        self.assertTrue(any("missing due Source ID PUB-A" in error for error in errors))

    def test_conditional_completion_requires_a_real_external_limitation(self):
        unsupported = VALID_DAILY.replace("| Completion Status | Complete |", "| Completion Status | Conditional |")
        unsupported = unsupported.replace("| Evidence Gate | Passed |", "| Evidence Gate | Conditional Pass |")
        errors = self.validator.validate_report_text(unsupported, self.registry)
        self.assertTrue(any("Conditional requires" in error for error in errors))

        blocked = unsupported.replace("accessible", "blocked")
        blocked = blocked.replace("No Change — Existing Coverage", "Blocked / Unverified")
        blocked = blocked.replace("| Books Gate | Passed |", "| Books Gate | Conditional Pass |")
        errors = self.validator.validate_report_text(blocked, self.registry)
        self.assertTrue(any("Materials Request" in error for error in errors))

        self.assertEqual([], self.validator.validate_report_text(blocked + MATERIALS_REQUEST, self.registry))

        orphan = VALID_DAILY + MATERIALS_REQUEST
        errors = self.validator.validate_report_text(orphan, self.registry)
        self.assertTrue(any("does not map to blocked, unverified or disputed" in error for error in errors))

        duplicate = blocked + MATERIALS_REQUEST + MATERIALS_REQUEST
        errors = self.validator.validate_report_text(duplicate, self.registry)
        self.assertTrue(any("must appear exactly one time" in error for error in errors))

    def test_blocking_failed_source_requires_exact_source_gap_materials_mapping(self):
        failed = source_failed_conditional()
        errors = self.validator.validate_report_text(failed, self.registry)
        self.assertTrue(any("failed source ORG-A / GAP-ORG-A-01 requires a Materials Request" in error for error in errors))

        self.assertEqual(
            [],
            self.validator.validate_report_text(failed + SOURCE_MATERIALS_REQUEST, self.registry),
        )

        wrong_gap = SOURCE_MATERIALS_REQUEST.replace("GAP-ORG-A-01", "GAP-WRONG")
        errors = self.validator.validate_report_text(failed + wrong_gap, self.registry)
        self.assertTrue(any("does not map to a blocking failed source receipt" in error for error in errors))

        books_passed = (failed + SOURCE_MATERIALS_REQUEST).replace(
            "| Books Gate | Conditional Pass |", "| Books Gate | Passed |"
        )
        errors = self.validator.validate_report_text(books_passed, self.registry)
        self.assertTrue(any("Books Gate cannot be Passed while a blocking source failure exists" in error for error in errors))

    def test_duplicate_v2_marker_is_rejected(self):
        duplicated = VALID_DAILY.replace(
            "<!-- validator:report-metadata-v2 -->",
            "<!-- validator:report-metadata-v2 -->\n<!-- validator:report-metadata-v2 -->",
        )
        errors = self.validator.validate_report_text(duplicated, self.registry)
        self.assertTrue(any("exactly one" in error for error in errors))

    def test_legacy_report_is_compatible_without_v2_validation(self):
        legacy = """# Legacy Weekly\n\nScore Schema: V1 Legacy /30\n\n| Technical Novelty | System Impact | Total |\n| --- | --- | --- |\n| 5 | 5 | 27 |\n"""
        self.assertEqual([], self.validator.validate_report_text(legacy, self.registry))

    def test_v2_delta_can_preserve_v1_compatibility_prose(self):
        mixed = VALID_DAILY + """
## Score V1 Legacy /30

| Technical Novelty | System Impact | Practical Value | Total |
| --- | --- | --- | --- |
| 5 | 5 | 4 | 27 |
"""
        self.assertEqual([], self.validator.validate_report_text(mixed, self.registry))

    def test_strict_report_without_markers_fails_but_audit_keeps_it_legacy(self):
        legacy = "# Report\n\nScore Schema: V2\n"
        self.assertEqual([], self.validator.validate_report_text(legacy, self.registry))
        errors = self.validator.validate_report_text(legacy, self.registry, strict=True)
        self.assertTrue(any("report-metadata-v2" in error for error in errors))


class CollectionValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_unrelated_reports_cannot_both_own_the_same_family(self):
        second = VALID_DAILY.replace("DEN-2026-08-25-FULL-001", "DEN-2026-08-25-FULL-002")
        reports = [(Path("papers/a.md"), VALID_DAILY), (Path("papers/b.md"), second)]
        errors = self.validator.validate_report_collection(reports, Path("/repo"))
        self.assertTrue(any("multiple unrelated owner reports" in error for error in errors))

    def test_daily_and_sunday_weekly_may_each_score_the_same_family(self):
        weekly = as_weekly().replace(
            "DEN-2026-08-25-FULL-001",
            "DEN-2026-W35-WEEKLY-001",
        )
        reports = [(Path("papers/daily.md"), VALID_DAILY), (Path("papers/weekly.md"), weekly)]
        errors = self.validator.validate_report_collection(reports, Path("/repo"))
        self.assertFalse(any("multiple unrelated owner reports" in error for error in errors))

    def test_delta_lineage_can_replace_an_owner_record(self):
        delta = VALID_DAILY.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |")
        delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |")
        delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |")
        delta = delta.replace("DEN-2026-08-25-FULL-001", "DEN-2026-08-25-DELTA-001")
        delta = delta.replace(
            "| Previous Denominator ID | — |",
            "| Previous Denominator ID | DEN-2026-08-25-FULL-001 |",
        )
        reports = [(Path("papers/base.md"), VALID_DAILY), (Path("papers/delta.md"), delta)]
        errors = self.validator.validate_report_collection(reports, Path("/repo"))
        self.assertFalse(any("multiple unrelated owner reports" in error for error in errors))

        mismatch = delta.replace(
            "| Previous Denominator ID | DEN-2026-08-25-FULL-001 |",
            "| Previous Denominator ID | DEN-WRONG |",
        )
        errors = self.validator.validate_report_collection(
            [(Path("papers/base.md"), VALID_DAILY), (Path("papers/delta.md"), mismatch)],
            Path("/repo"),
        )
        self.assertTrue(any("Previous Denominator ID" in error for error in errors))

    def test_delta_lineage_can_correct_primary_event_owner_and_date(self):
        delta = VALID_DAILY.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |")
        delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |")
        delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |")
        delta = delta.replace("DEN-2026-08-25-FULL-001", "DEN-2026-08-25-DELTA-001")
        delta = delta.replace(
            "| Previous Denominator ID | — |",
            "| Previous Denominator ID | DEN-2026-08-25-FULL-001 |",
        )
        delta = delta.replace("arXiv:2608.00001v1", "arXiv:2608.99999v1")
        delta = delta.replace("arXiv:2608.00001", "arXiv:2608.99999")
        delta = delta.replace("2026-W35 | 2026-08-25", "2026-W34 | 2026-08-18")

        lineaged = [(Path("papers/base.md"), VALID_DAILY), (Path("papers/delta.md"), delta)]
        errors = self.validator.validate_report_collection(lineaged, Path("/repo"))
        self.assertFalse(any("conflicting primary identifier or owner identity" in error for error in errors))

        unrelated = delta.replace("| Coverage Mode | Delta Audit |", "| Coverage Mode | Full Replay |")
        unrelated = unrelated.replace("| Baseline Report | papers/base.md |", "| Baseline Report | — |")
        unrelated = unrelated.replace("| Changed Source IDs | ORG-A |", "| Changed Source IDs | — |")
        unrelated = unrelated.replace(
            "| Previous Denominator ID | DEN-2026-08-25-FULL-001 |",
            "| Previous Denominator ID | — |",
        )
        errors = self.validator.validate_report_collection(
            [(Path("papers/base.md"), VALID_DAILY), (Path("papers/unrelated.md"), unrelated)],
            Path("/repo"),
        )
        self.assertTrue(any("conflicting primary identifier or owner identity" in error for error in errors))

    def test_same_window_revision_may_change_version_identity_when_it_points_to_owner_report(self):
        owner = VALID_DAILY_V21
        revision = VALID_DAILY_V21.replace(
            "| 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none |",
            "| — | — | — | — | revision | deep_complete | accessible | important_revision |",
            1,
        )
        revision = revision.replace(
            "| self | — | new_in_window |",
            "| papers/owner.md | — | same_window_revision |",
            1,
        )
        revision = revision.replace(
            "| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 |",
            "| SF-001 | arXiv:2608.00001v2 | arXiv:2608.00001v2 |",
            1,
        )
        errors = self.validator.validate_report_collection(
            [(Path("papers/owner.md"), owner), (Path("papers/revision.md"), revision)],
            Path("/repo"),
        )
        self.assertFalse(any("conflicting primary identifier or owner identity" in error for error in errors))

    def test_delta_loads_an_on_disk_baseline_for_denominator_reconciliation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            papers = root / "papers"
            papers.mkdir()
            (papers / "base.md").write_text(VALID_DAILY, encoding="utf-8")

            delta = VALID_DAILY.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |")
            delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |")
            delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |")
            delta = delta.replace("DEN-2026-08-25-FULL-001", "DEN-2026-08-25-DELTA-001")
            delta = delta.replace(
                "| Previous Denominator ID | — |",
                "| Previous Denominator ID | DEN-WRONG |",
            )
            errors = self.validator.validate_report_collection(
                [(Path("papers/delta.md"), delta)],
                root,
            )
            self.assertTrue(any("Previous Denominator ID" in error for error in errors))

            (papers / "base.md").write_text(
                VALID_DAILY.replace(
                    "| Denominator ID | DEN-2026-08-25-FULL-001 |",
                    "| Denominator ID | — |",
                ),
                encoding="utf-8",
            )
            errors = self.validator.validate_report_collection(
                [(Path("papers/delta.md"), delta)],
                root,
            )
            self.assertTrue(any("V2 Baseline Report has no Denominator ID" in error for error in errors))

    def test_delta_legacy_baseline_identity_binds_path_and_content_hash(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            papers = root / "papers"
            papers.mkdir()
            legacy = "# Legacy\n\nScore Schema: V1 Legacy /30\n"
            (papers / "base.md").write_text(legacy, encoding="utf-8")
            digest = hashlib.sha256(legacy.encode("utf-8")).hexdigest()

            delta = VALID_DAILY.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |")
            delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |")
            delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |")
            delta = delta.replace("DEN-2026-08-25-FULL-001", "DEN-2026-08-25-DELTA-001")
            delta = delta.replace(
                "| Previous Denominator ID | — |",
                f"| Previous Denominator ID | legacy:papers/base.md@sha256:{digest} |",
            )
            errors = self.validator.validate_report_collection(
                [(Path("papers/delta.md"), delta)],
                root,
            )
            self.assertFalse(any("legacy baseline identity" in error for error in errors))

            wrong_hash = delta.replace(digest, "0" * 64, 1)
            errors = self.validator.validate_report_collection(
                [(Path("papers/delta.md"), wrong_hash)],
                root,
            )
            self.assertTrue(any("legacy baseline identity" in error for error in errors))

    def test_delta_requires_newly_effective_required_sources_since_baseline_registry(self):
        registry_text = VALID_REGISTRY.replace(
            "注册表版本：2026-08-25",
            "注册表版本：2026-08-26",
        ).replace(
            "生效日期：2026-08-25",
            "生效日期：2026-08-26",
        ).replace(
            "<!-- validator:source-registry-end -->",
            "| ORG-NEW | Model organization | Creator Primary | Required Weekly | https://new.example.org/research | release or paper | first public | all pages | checked/no-hit plus cursor | public mechanism and artifact | — | 2026-08-26 | New AI |\n"
            "<!-- validator:source-registry-end -->",
        )
        registry, registry_errors = self.validator.validate_registry_text(registry_text)
        self.assertEqual([], registry_errors)

        baseline = historical_v21_without_books().replace(
            "DEN-2026-08-25-V21-001", "DEN-BASE-REGISTRY-001", 1
        )
        delta = baseline.replace("| Registry Version | 2026-08-25 |", "| Registry Version | 2026-08-26 |", 1)
        delta = delta.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |", 1)
        delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |", 1)
        delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |", 1)
        delta = delta.replace(
            "| Previous Denominator ID | — |",
            "| Previous Denominator ID | DEN-BASE-REGISTRY-001 |",
            1,
        )
        delta = delta.replace("DEN-BASE-REGISTRY-001", "DEN-DELTA-REGISTRY-001", 1)

        errors = self.validator.validate_report_collection(
            [(Path("papers/base.md"), baseline), (Path("papers/delta.md"), delta)],
            Path("/repo"),
            registry,
        )
        self.assertTrue(
            any("newly effective Required Source ID ORG-NEW" in error for error in errors)
        )

    def test_delta_with_legacy_baseline_cannot_assume_required_sources_were_covered(self):
        registry_text = VALID_REGISTRY.replace(
            "注册表版本：2026-08-25", "注册表版本：2026-08-26"
        ).replace(
            "生效日期：2026-08-25", "生效日期：2026-08-26"
        ).replace(
            "<!-- validator:source-registry-end -->",
            "| ORG-NEW | Model organization | Creator Primary | Required Weekly | https://new.example.org/research | release or paper | first public | all pages | checked/no-hit plus cursor | public mechanism and artifact | — | 2026-08-26 | New AI |\n"
            "<!-- validator:source-registry-end -->",
        )
        registry, registry_errors = self.validator.validate_registry_text(registry_text)
        self.assertEqual([], registry_errors)

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            papers = root / "papers"
            papers.mkdir()
            legacy = "# Legacy\n\nScore Schema: V1 Legacy /30\n"
            (papers / "base.md").write_text(legacy, encoding="utf-8")
            digest = hashlib.sha256(legacy.encode("utf-8")).hexdigest()
            delta = historical_v21_without_books().replace(
                "| Registry Version | 2026-08-25 |", "| Registry Version | 2026-08-26 |", 1
            ).replace(
                "| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |", 1
            ).replace(
                "| Baseline Report | — |", "| Baseline Report | papers/base.md |", 1
            ).replace(
                "| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |", 1
            ).replace(
                "| Previous Denominator ID | — |",
                f"| Previous Denominator ID | legacy:papers/base.md@sha256:{digest} |",
                1,
            )
            errors = self.validator.validate_report_collection(
                [(Path("papers/delta.md"), delta)], root, registry
            )
            self.assertTrue(
                any("baseline registry version is unavailable" in error for error in errors)
            )

    def test_primary_identifier_cannot_map_to_two_families(self):
        second = VALID_DAILY.replace("SF-001", "SF-002")
        second = second.replace("DEN-2026-08-25-FULL-001", "DEN-2026-08-25-FULL-002")
        reports = [(Path("papers/a.md"), VALID_DAILY), (Path("papers/b.md"), second)]
        errors = self.validator.validate_report_collection(reports, Path("/repo"))
        self.assertTrue(any("Primary Identifier" in error for error in errors))

    def test_denominator_id_is_unique_across_reports(self):
        reports = [(Path("papers/a.md"), VALID_DAILY), (Path("papers/b.md"), VALID_DAILY)]
        errors = self.validator.validate_report_collection(reports, Path("/repo"))
        self.assertTrue(any("duplicate Denominator ID" in error for error in errors))


class ReportV21ValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()
        cls.registry, errors = cls.validator.validate_registry_text(VALID_REGISTRY)
        if errors:
            raise AssertionError(errors)

    def test_valid_v21_report_has_auditable_completion_receipts(self):
        self.assertEqual([], self.validator.validate_report_text(VALID_DAILY_V21, self.registry))

    def test_withdrawn_primary_source_closure_purges_all_downstream_records(self):
        withdrawn = VALID_DAILY_V21.replace(
            "\n## 2. Candidate Ledger\n",
            WITHDRAWN_PRIMARY_SOURCE_CLOSURE + "\n## 2. Candidate Ledger\n",
            1,
        ) + MATERIALS_REQUEST

        errors = self.validator.validate_report_text(withdrawn, self.registry)

        expected_surfaces = {
            "Candidate Ledger",
            "Review Completion Receipt",
            "Source Review",
            "Deep Analysis Selection",
            "Books Comparison",
            "Books Review",
            "Materials Request",
        }
        for surface in expected_surfaces:
            self.assertTrue(
                any(
                    "withdrawn_primary_source family SF-001" in error and surface in error
                    for error in errors
                ),
                f"missing withdrawn-source error for {surface}: {errors}",
            )

    def test_withdrawn_primary_source_example_in_fence_is_not_live_state(self):
        fenced_example = VALID_DAILY_V21.replace(
            "\n## 8. Ignored Noise\n",
            "\n```markdown\n"
            + WITHDRAWN_PRIMARY_SOURCE_CLOSURE
            + "```\n\n## 8. Ignored Noise\n",
            1,
        )
        self.assertEqual(
            [],
            self.validator.validate_report_text(fenced_example, self.registry),
        )

    def test_v21_daily_requires_visible_status_and_canonical_section_order(self):
        missing_status = VALID_DAILY_V21.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed\n\n",
            "",
            1,
        )
        errors = self.validator.validate_report_text(missing_status, self.registry)
        self.assertTrue(any("canonical header" in error and "Status" in error for error in errors))

        reordered = VALID_DAILY_V21.replace(
            "## 8. Ignored Noise",
            "## TEMP",
            1,
        ).replace(
            "## 9. Recommended Action",
            "## 8. Ignored Noise",
            1,
        ).replace(
            "## TEMP",
            "## 9. Recommended Action",
            1,
        )
        errors = self.validator.validate_report_text(reordered, self.registry)
        self.assertTrue(any("canonical H2 sequence mismatch" in error for error in errors))

    def test_v21_daily_visible_status_must_match_gate_metadata(self):
        inconsistent = VALID_DAILY_V21.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open",
            1,
        )
        errors = self.validator.validate_report_text(inconsistent, self.registry)
        self.assertTrue(any("does not expose Completion Status" in error for error in errors))

        gate_only_mismatch = VALID_DAILY_V21.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** Complete；Coverage=Closed、Evidence=Open、Books=Passed",
            1,
        )
        errors = self.validator.validate_report_text(gate_only_mismatch, self.registry)
        self.assertTrue(any("Evidence Gate" in error and "Passed" in error for error in errors))

    def test_v21_daily_header_is_unique_ordered_and_metadata_bound(self):
        moved_status = VALID_DAILY_V21.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed\n\n",
            "",
            1,
        ).replace(
            "## 13. Final Status\n\n",
            "## 13. Final Status\n\n**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed\n\n",
            1,
        )
        errors = self.validator.validate_report_text(moved_status, self.registry)
        self.assertTrue(any("canonical preamble" in error for error in errors))

        misleading_completion = VALID_DAILY_V21.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** In Progress；previous checkpoint Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            1,
        )
        errors = self.validator.validate_report_text(misleading_completion, self.registry)
        self.assertTrue(any("Completion Status" in error for error in errors))

        bad_window = VALID_DAILY_V21.replace(
            "**Strict Window:** 2026-08-24 09:00:00 ～ 2026-08-25 09:00:00（北京时间，左闭右开）",
            "**Strict Window:** bananas",
            1,
        )
        errors = self.validator.validate_report_text(bad_window, self.registry)
        self.assertTrue(any("Strict Window" in error for error in errors))

        bad_contract = VALID_DAILY_V21.replace(
            "**Contract:** V2.1 Full Replay",
            "**Contract:** Legacy V1 Delta",
            1,
        )
        errors = self.validator.validate_report_text(bad_contract, self.registry)
        self.assertTrue(any("Contract" in error for error in errors))

    def test_v21_daily_final_status_must_match_metadata_and_expose_findings(self):
        inconsistent = VALID_DAILY_V21.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=In Progress；Coverage=Open、Evidence=Open、Books=Open；unresolved findings=4.",
            1,
        )
        errors = self.validator.validate_report_text(inconsistent, self.registry)
        self.assertTrue(any("Final Status" in error for error in errors))

        missing_findings = VALID_DAILY_V21.replace("；unresolved findings=0.", ".", 1)
        errors = self.validator.validate_report_text(missing_findings, self.registry)
        self.assertTrue(any("unresolved finding" in error for error in errors))

    def test_v21_daily_source_reviews_belong_to_review_receipt_section(self):
        block = """### Source Reviews

<!-- review:SF-001:start -->
<!-- claim:SF-001:start -->
The cited method, evaluation, limitations, and missing artifact define this bounded claim.
<!-- claim:SF-001:end -->
<!-- review:SF-001:end -->

"""
        misplaced = VALID_DAILY_V21.replace(block, "", 1).replace(
            "## 4. Benchmark Contracts\n\n",
            "## 4. Benchmark Contracts\n\n" + block,
            1,
        )
        errors = self.validator.validate_report_text(misplaced, self.registry)
        self.assertTrue(any("Source Review" in error and "section 3" in error for error in errors))

        missing_heading = VALID_DAILY_V21.replace("### Source Reviews\n\n", "", 1)
        errors = self.validator.validate_report_text(missing_heading, self.registry)
        self.assertTrue(any("Source Reviews heading" in error for error in errors))

    def test_v21_daily_ignores_h2_examples_inside_fences(self):
        fenced = VALID_DAILY_V21.replace(
            "## 8. Ignored Noise\n\nNone.",
            "## 8. Ignored Noise\n\n```text\n## Example only\n```\n\nNone.",
            1,
        )
        errors = self.validator.validate_report_text(fenced, self.registry)
        self.assertFalse(any("canonical H2 sequence mismatch" in error for error in errors))

    def test_coverage_v2_requires_replayable_execution_evidence(self):
        missing_execution = VALID_DAILY_V21.replace(
            "2026-08-25T09:00:00+08:00 | https://example.com/research",
            "— | https://example.com/research",
            1,
        )
        errors = self.validator.validate_report_text(missing_execution, self.registry)
        self.assertTrue(any("Executed At" in error for error in errors))

        generic_closure = VALID_DAILY_V21.replace(
            "coverage:ORG-A:2026-08-25 | — |",
            "checked | — |",
            1,
        )
        errors = self.validator.validate_report_text(generic_closure, self.registry)
        self.assertTrue(any("Closure Evidence" in error for error in errors))

        generic_cursor = VALID_DAILY_V21.replace("page=1; final_cursor=end", "end", 1)
        errors = self.validator.validate_report_text(generic_cursor, self.registry)
        self.assertTrue(any("Pagination / Cursor" in error for error in errors))

    def test_github_latest_commit_selection_cannot_claim_history_cursor_end(self):
        github_receipt = VALID_DAILY_V21.replace(
            "https://example.com/research; release or paper",
            "https://api.github.com/repos/example/project/commits?until=2026-08-25T00:00:00Z&per_page=1",
            1,
        )
        errors = self.validator.validate_report_text(github_receipt, self.registry)
        self.assertTrue(any("cannot claim final_cursor=end" in error for error in errors))

        honest_receipt = github_receipt.replace(
            "page=1; final_cursor=end",
            "page=1; per_page=1; selected first result as latest commit at/before exact until; "
            "older-history pages intentionally not traversed/not required",
            1,
        )
        errors = self.validator.validate_report_text(honest_receipt, self.registry)
        self.assertFalse(any("cannot claim final_cursor=end" in error for error in errors))

    def test_deep_receipt_rejects_bare_paper_url_with_generic_paraphrase(self):
        generic = VALID_DAILY_V21.replace(
            "arXiv:2608.00001v1#section-3",
            "https://arxiv.org/html/2608.00001v1 (Method passages)",
            1,
        )
        errors = self.validator.validate_report_text(generic, self.registry)
        self.assertTrue(any("completed Deep review must identify a stable" in error for error in errors))

    def test_semantic_audit_rejects_duplicate_reviewed_refs(self):
        duplicate = VALID_DAILY_V21.replace(
            "coverage:ORG-A:2026-08-25 | none |",
            "coverage:ORG-A:2026-08-25; coverage:ORG-A:2026-08-25 | none |",
            1,
        )
        errors = self.validator.validate_report_text(duplicate, self.registry)
        self.assertTrue(any("Reviewed Refs must be unique" in error for error in errors))

    def test_empty_books_comparison_requires_per_candidate_audit_refs(self):
        weekly_only = VALID_DAILY_V21.replace(
            "No Change — Existing Coverage | books-review:SF-001 | no |",
            "Weekly Only — Context | — | no |",
            1,
        )
        books_row = (
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | "
            "books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | "
            "delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n"
        )
        weekly_only = weekly_only.replace(books_row, "")
        weekly_only = weekly_only.replace(
            "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 |",
            "| AUD-BOOK-001 | fresh-context:noether | books | validator:books-comparison-v1 |",
            1,
        )
        errors = self.validator.validate_report_text(weekly_only, self.registry)
        self.assertTrue(any("every Weekly Only candidate" in error for error in errors))

        covered = weekly_only.replace(
            "validator:books-comparison-v1 | none |",
            "validator:books-comparison-v1; review:SF-001 | none |",
            1,
        )
        errors = self.validator.validate_report_text(covered, self.registry)
        self.assertFalse(any("every Weekly Only candidate" in error for error in errors))

    def test_mixed_books_comparison_requires_weekly_only_audit_refs(self):
        candidate = (
            "| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 | 2026-W35 | 2026-08-25 | "
            "ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-001 | "
            "self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | "
            "books-review:SF-001 | no |"
        )
        second_candidate = (
            "| SF-002 | arXiv:2608.00002 | arXiv:2608.00002v1 | 2026-W35 | 2026-08-25 | "
            "ORG-A | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-002 | "
            "self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Weekly Only — Context | — | no |"
        )
        receipt = (
            "| SF-001 | RP-1188b619ab6e379d | deep | arXiv:2608.00001v1 | "
            "ORG-A@arXiv:2608.00001v1 | arXiv:2608.00001v1#section-3 | "
            "arXiv:2608.00001v1#table-2 | arXiv:2608.00001v1#limitations | "
            "Not Disclosed — v1 links no artifact | claim:SF-001 | complete |"
        )
        second_receipt = (
            "| SF-002 | RP-2188b619ab6e379d | standard | arXiv:2608.00002v1 | "
            "ORG-A@arXiv:2608.00002v1 | arXiv:2608.00002v1#section-3 | "
            "arXiv:2608.00002v1#table-2 | arXiv:2608.00002v1#limitations | "
            "Not Disclosed — v1 links no artifact | claim:SF-002 | complete |"
        )
        second_review = """\
<!-- review:SF-002:start -->
<!-- claim:SF-002:start -->
The second source is fully reviewed but remains Weekly Only.
<!-- claim:SF-002:end -->
<!-- review:SF-002:end -->

"""
        mixed = VALID_DAILY_V21.replace(candidate, candidate + "\n" + second_candidate, 1)
        mixed = mixed.replace(receipt, receipt + "\n" + second_receipt, 1)
        mixed = mixed.replace("| checked | 1 | SF-001 |", "| checked | 2 | SF-001<br>SF-002 |", 1)
        mixed = mixed.replace("<!-- analysis:DA-001:start -->", second_review + "<!-- analysis:DA-001:start -->", 1)

        errors = self.validator.validate_report_text(mixed, self.registry)
        self.assertTrue(any("review:SF-002" in error for error in errors), errors)

        covered = mixed.replace(
            "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 |",
            "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001; review:SF-002 |",
            1,
        )
        errors = self.validator.validate_report_text(covered, self.registry)
        self.assertFalse(any("review:SF-002" in error for error in errors), errors)

    def test_incomplete_coverage_is_ordinary_pending_not_conditional(self):
        incomplete = VALID_DAILY_V21.replace("| checked | 1 |", "| incomplete | 1 |", 1)
        incomplete = incomplete.replace(
            "| 2026-08-25T09:00:00+08:00 | coverage:ORG-A:2026-08-25 | — |",
            "| — | coverage:ORG-A:2026-08-25 | GAP-COVERAGE-001 |",
            1,
        )
        errors = self.validator.validate_report_text(incomplete, self.registry)
        self.assertTrue(any("Coverage Gate must be Open" in error for error in errors))
        self.assertTrue(any("Completion Status In Progress" in error for error in errors))

        honest = incomplete.replace("| Completion Status | Complete |", "| Completion Status | In Progress |")
        honest = honest.replace("| Coverage Gate | Closed |", "| Coverage Gate | Open |")
        honest = honest.replace("| Books Gate | Passed |", "| Books Gate | Open |")
        self.assertFalse(
            any("Conditional" in error for error in self.validator.validate_report_text(honest, self.registry))
        )

    def test_pending_review_has_a_receipt_but_cannot_freeze_provenance(self):
        pending = VALID_DAILY_V21.replace("| deep_complete | accessible |", "| pending | partial |", 1)
        pending = pending.replace(
            "| No Change — Existing Coverage | books-review:SF-001 | no |",
            "| Not Assessed | — | no |",
            1,
        )
        pending = pending.replace(
            "| SF-001 | RP-1188b619ab6e379d | deep |",
            "| SF-001 | — | deep |",
            1,
        )
        pending = pending.replace(
            "| claim:SF-001 | complete |",
            "| claim:SF-001 | pending |",
            1,
        )
        pending = pending.replace("| Completion Status | Complete |", "| Completion Status | In Progress |")
        pending = pending.replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |")
        pending = pending.replace("| Books Gate | Passed |", "| Books Gate | Open |")
        pending = pending.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** In Progress；Coverage=Closed、Evidence=Open、Books=Open",
        )
        pending = pending.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=In Progress；Coverage=Closed、Evidence=Open、Books=Open；unresolved findings=0.",
        )
        pending = pending.replace(
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n",
            "",
        )
        self.assertEqual([], self.validator.validate_report_text(pending, self.registry))

    def test_completed_review_requires_route_specific_receipt_and_bounded_refs(self):
        missing_receipt = VALID_DAILY_V21.replace(
            "| SF-001 | RP-1188b619ab6e379d | deep | arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 | arXiv:2608.00001v1#section-3 | arXiv:2608.00001v1#table-2 | arXiv:2608.00001v1#limitations | Not Disclosed — v1 links no artifact | claim:SF-001 | complete |\n",
            "",
        )
        errors = self.validator.validate_report_text(missing_receipt, self.registry)
        self.assertTrue(any("Review Completion" in error for error in errors))

        generic_method = VALID_DAILY_V21.replace("arXiv:2608.00001v1#section-3", "checked", 1)
        errors = self.validator.validate_report_text(generic_method, self.registry)
        self.assertTrue(any("Method / Identity Locators" in error for error in errors))

        unbounded = VALID_DAILY_V21.replace("<!-- review:SF-001:end -->", "", 1)
        errors = self.validator.validate_report_text(unbounded, self.registry)
        self.assertTrue(any("review:SF-001" in error and "end" in error for error in errors))

        borrowed = VALID_DAILY_V21.replace("arXiv:2608.00001v1#section-3", "review:SF-001", 1)
        borrowed = borrowed.replace("arXiv:2608.00001v1#table-2", "review:SF-001", 1)
        borrowed = borrowed.replace("arXiv:2608.00001v1#limitations", "review:SF-001", 1)
        errors = self.validator.validate_report_text(borrowed, self.registry)
        self.assertTrue(any("borrow" in error or "source locator" in error for error in errors))

    def test_review_provenance_binds_versions_locators_claim_and_review_body(self):
        mutations = (
            VALID_DAILY_V21.replace("RP-1188b619ab6e379d", "RP-wrong", 1),
            VALID_DAILY_V21.replace(
                "| arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 |",
                "| arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v2 |",
                1,
            ),
            VALID_DAILY_V21.replace("arXiv:2608.00001v1#table-2", "arXiv:2608.00001v1#table-3", 1),
            VALID_DAILY_V21.replace(
                "The cited method, evaluation, limitations, and missing artifact define this bounded claim.",
                "The bounded claim silently changed.",
                1,
            ),
        )
        for mutated in mutations:
            with self.subTest(mutated=mutated[:80]):
                errors = self.validator.validate_report_text(mutated, self.registry)
                self.assertTrue(any("Review Provenance ID" in error for error in errors))

    def test_review_provenance_canonicalizes_multivalues_review_ref_and_body_exactly(self):
        candidate_a = {
            "Event Identity": "arXiv:2608.00001v1",
            "Primary Identifier": "arXiv:2608.00001",
            "Supporting Source IDs": "ORG-B; ORG-A",
        }
        candidate_b = dict(candidate_a, **{"Supporting Source IDs": "ORG-A; ORG-B"})
        digest_a = self.validator._normalized_body_sha256("\r\nCafe\u0301  \r\nSecond\t\r\n\r\n")
        digest_b = self.validator._normalized_body_sha256("\nCafé\nSecond\n")
        self.assertEqual(digest_a, digest_b)

        provenance_a = self.validator._expected_review_provenance(
            "SF-001",
            candidate_a,
            "deep",
            "arXiv:2608.00001v1",
            "SRC-B@v2; SRC-A@v1",
            "method:B; method:A",
            "eval:B; eval:A",
            "limit:B; limit:A",
            "artifact:B; artifact:A",
            "claim:SF-001",
            "review:SF-001",
            digest_a,
        )
        provenance_b = self.validator._expected_review_provenance(
            "SF-001",
            candidate_b,
            "deep",
            "arXiv:2608.00001v1",
            "SRC-A@v1; SRC-B@v2",
            "method:A; method:B",
            "eval:A; eval:B",
            "limit:A; limit:B",
            "artifact:A; artifact:B",
            "claim:SF-001",
            "review:SF-001",
            digest_b,
        )
        self.assertEqual(provenance_a, provenance_b)

    def test_completed_review_requires_explicit_reviewed_evidence_versions(self):
        missing = VALID_DAILY_V21.replace(
            "| arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 | arXiv:2608.00001v1#section-3 |",
            "| arXiv:2608.00001v1 | — | arXiv:2608.00001v1#section-3 |",
            1,
        )
        errors = self.validator.validate_report_text(missing, self.registry)
        self.assertTrue(any("Reviewed Evidence Versions" in error for error in errors))

    def test_explicit_source_review_disposition_matches_candidate_ledger(self):
        mismatched = VALID_DAILY_V21.replace(
            "<!-- review:SF-001:end -->",
            "- Disposition: `Integrate`.\n<!-- review:SF-001:end -->",
            1,
        )
        errors = self.validator.validate_report_text(mismatched, self.registry)
        self.assertTrue(
            any(
                "Source Review Disposition 'Integrate' does not match Candidate Ledger "
                "Books Disposition 'No Change — Existing Coverage'" in error
                for error in errors
            )
        )

        prefixed_primary = VALID_DAILY_V21.replace(
            "| arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 |",
            "| ORG-A@arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 |",
            1,
        )
        errors = self.validator.validate_report_text(prefixed_primary, self.registry)
        self.assertTrue(any("without a Source ID prefix" in error for error in errors))

        mismatched_primary = VALID_DAILY_V21.replace(
            "| arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 |",
            "| arXiv:2608.00001v2 | ORG-A@arXiv:2608.00001v1 |",
            1,
        )
        errors = self.validator.validate_report_text(mismatched_primary, self.registry)
        self.assertTrue(any("exactly one" in error for error in errors))

    def test_deep_analysis_selection_covers_eligible_families_and_matches_basis(self):
        wrong_basis = VALID_DAILY_V21.replace("| score_7_9 | selected |", "| books_delta | selected |", 1)
        errors = self.validator.validate_report_text(wrong_basis, self.registry)
        self.assertTrue(any("score_7_9" in error for error in errors))

        missing_family = VALID_DAILY_V21.replace("| SF-001 | score_7_9 |", "| SF-OTHER | score_7_9 |", 1)
        errors = self.validator.validate_report_text(missing_family, self.registry)
        self.assertTrue(any("eligible family SF-001" in error for error in errors))

        pre_books_violation = VALID_DAILY_V21.replace("| score_7_9 | selected |", "| books_delta | selected |", 1)
        errors = self.validator.validate_report_text(pre_books_violation, self.registry)
        self.assertTrue(any("Eligibility" in error for error in errors))

    def test_deep_analysis_selection_is_bounded_to_three_selected_units(self):
        extra = """\
| SF-001 | score_7_9 | selected | DA-002 | — | Independent non-redundant system reach | analysis:DA-001 |
| SF-001 | score_7_9 | selected | DA-003 | — | Independent non-redundant durability impact | analysis:DA-001 |
| SF-001 | score_7_9 | selected | DA-004 | — | Independent non-redundant correction impact | analysis:DA-001 |
"""
        over_selected = VALID_DAILY_V21.replace(
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |\n",
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |\n" + extra,
        )
        errors = self.validator.validate_report_text(over_selected, self.registry)
        self.assertTrue(any("at most 3" in error for error in errors))

        none_selected = VALID_DAILY_V21.replace("| selected |", "| not_selected |", 1)
        errors = self.validator.validate_report_text(none_selected, self.registry)
        self.assertTrue(any("at least 1 selected" in error for error in errors))

    def test_deep_analysis_selection_rejects_duplicate_families_and_dangling_subsumption(self):
        duplicate = VALID_DAILY_V21.replace(
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |\n",
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |\n"
            "| SF-001 | score_7_9 | not_selected | DA-002 | — | Lower priority than the selected correction | analysis:DA-001 |\n",
            1,
        )
        errors = self.validator.validate_report_text(duplicate, self.registry)
        self.assertTrue(any("duplicate Source Family ID SF-001" in error for error in errors))

        dangling = VALID_DAILY_V21.replace(
            "| score_7_9 | selected | DA-001 | — |",
            "| score_7_9 | subsumed | DA-002 | DA-MISSING |",
            1,
        )
        errors = self.validator.validate_report_text(dangling, self.registry)
        self.assertTrue(any("Subsumed By" in error and "selected" in error for error in errors))

    def test_deep_analysis_selection_accepts_subsumed_family_without_own_unit_id(self):
        report = VALID_DAILY_V21.replace(
            "| checked | 1 | SF-001 |",
            "| checked | 2 | SF-001<br>SF-002 |",
            1,
        )
        report = report.replace(
            "| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 | 2026-W35 | 2026-08-25 | ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-001 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |",
            "| SF-001 | arXiv:2608.00001 | arXiv:2608.00001v1 | 2026-W35 | 2026-08-25 | ORG-A | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-001 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |\n"
            "| SF-002 | arXiv:2608.00002 | arXiv:2608.00002v1 | 2026-W35 | 2026-08-25 | ORG-A | 3 | 2 | 2 | 7 | retained | pending | accessible | none | — | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Not Assessed | — | no |",
            1,
        )
        report = report.replace(
            "| SF-001 | RP-1188b619ab6e379d | deep | arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 | arXiv:2608.00001v1#section-3 | arXiv:2608.00001v1#table-2 | arXiv:2608.00001v1#limitations | Not Disclosed — v1 links no artifact | claim:SF-001 | complete |",
            "| SF-001 | RP-1188b619ab6e379d | deep | arXiv:2608.00001v1 | ORG-A@arXiv:2608.00001v1 | arXiv:2608.00001v1#section-3 | arXiv:2608.00001v1#table-2 | arXiv:2608.00001v1#limitations | Not Disclosed — v1 links no artifact | claim:SF-001 | complete |\n"
            "| SF-002 | — | deep | arXiv:2608.00002v1 | Pending — reviewed evidence set not frozen | Pending — method locators not frozen | Pending — evaluation locators not frozen | Pending — limitations locators not frozen | Pending — artifact locator not frozen | Pending — bounded claim not frozen | pending |",
            1,
        )
        report = report.replace(
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |",
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |\n"
            "| SF-002 | score_7_9 | subsumed | — | DA-001 | The same selected analysis compares the second family without creating a duplicate narrative | analysis:DA-001 |",
            1,
        )
        report = report.replace("| Completion Status | Complete |", "| Completion Status | In Progress |", 1)
        report = report.replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |", 1)
        report = report.replace("| Books Gate | Passed |", "| Books Gate | Open |", 1)
        report = report.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** In Progress；Coverage=Closed、Evidence=Open、Books=Open",
            1,
        )
        report = report.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=In Progress；Coverage=Closed、Evidence=Open、Books=Open；unresolved findings=0.",
            1,
        )
        self.assertEqual([], self.validator.validate_report_text(report, self.registry))

    def test_potential_structural_gap_is_allowed_but_not_inferred_from_blank_owner(self):
        report = VALID_DAILY_V21.replace(
            "| INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |",
            "| — | Not Assessed | — | no |",
            1,
        )
        report = report.replace(
            "| score_7_9 | selected |",
            "| score_7_9<br>potential_structural_gap | selected |",
            1,
        )
        report = report.replace(
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n",
            "",
            1,
        )
        report = report.replace("| Completion Status | Complete |", "| Completion Status | In Progress |", 1)
        report = report.replace("| Books Gate | Passed |", "| Books Gate | Open |", 1)
        report = report.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open",
            1,
        )
        report = report.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=In Progress；Coverage=Closed、Evidence=Passed、Books=Open；unresolved findings=0.",
            1,
        )
        report = report.replace(
            "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 | none | Not Required — no unresolved Books finding | passed |",
            "| AUD-BOOK-001 | fresh-context:noether | books | validator:books-comparison-v1 | FINDING-STRUCTURAL-001 — owner comparison remains pending | Pending — compare existing owners before disposition | open |",
            1,
        )
        self.assertEqual([], self.validator.validate_report_text(report, self.registry))

    def test_no_deep_eligible_family_allows_zero_selected_units(self):
        no_deep = VALID_DAILY_V21.replace("| 3 | 2 | 2 | 7 |", "| 3 | 2 | 1 | 6 |", 1)
        no_deep = no_deep.replace("| deep_complete |", "| standard_complete |", 1)
        no_deep = no_deep.replace("| RP-1188b619ab6e379d | deep |", "| RP-4994eb3a5ce4bfa2 | standard |", 1)
        no_deep = no_deep.replace(
            "| SF-001 | score_7_9 | selected | DA-001 | — | Highest design delta in the frozen denominator; no competing correction or security override | analysis:DA-001 |\n",
            "",
        )
        self.assertEqual([], self.validator.validate_report_text(no_deep, self.registry))

    def test_contract_version_is_required_for_v21_and_old_v2_is_not_strict_complete(self):
        missing = VALID_DAILY_V21.replace("| Contract Version | V2.1 |\n", "", 1)
        errors = self.validator.validate_report_text(missing, self.registry)
        self.assertTrue(any("Contract Version V2.1" in error for error in errors))

        errors = self.validator.validate_report_text(VALID_DAILY, self.registry, strict=True)
        self.assertTrue(any("V2.1 report interfaces" in error for error in errors))

    def test_books_disposition_requires_specific_comparison_receipt(self):
        missing_comparison = VALID_DAILY_V21.replace(
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n",
            "",
        )
        errors = self.validator.validate_report_text(missing_comparison, self.registry)
        self.assertTrue(any("Books Comparison" in error for error in errors))

        generic = VALID_DAILY_V21.replace("books/example.md#request-lifecycle", "checked", 1)
        errors = self.validator.validate_report_text(generic, self.registry)
        self.assertTrue(any("Target Chapter Ref" in error for error in errors))

        disposition_as_relation = VALID_DAILY_V21.replace(
            "| Principle Reuse | No Change — Existing Coverage |",
            "| No Change — Existing Coverage | No Change — Existing Coverage |",
            1,
        )
        errors = self.validator.validate_report_text(disposition_as_relation, self.registry)
        self.assertTrue(any("Evolution Relation" in error for error in errors))

        explicit_na = VALID_DAILY_V21.replace(
            "| Principle Reuse | No Change — Existing Coverage |",
            "| Not Applicable — evidence only narrows the existing boundary | No Change — Existing Coverage |",
            1,
        )
        self.assertEqual([], self.validator.validate_report_text(explicit_na, self.registry))

    def test_books_integrate_and_structural_decisions_require_preselection_eligibility(self):
        integrate = VALID_DAILY_V21.replace(
            "| No Change — Existing Coverage | books-review:SF-001 | no |",
            "| Integrate | books-review:SF-001 | no |",
            1,
        ).replace(
            "| Principle Reuse | No Change — Existing Coverage |",
            "| Principle Reuse | Integrate |",
            1,
        )
        errors = self.validator.validate_report_text(integrate, self.registry)
        self.assertTrue(any("potential_books_delta" in error for error in errors))

        structural = VALID_DAILY_V21.replace(
            "| INFER-REQUEST-LIFECYCLE | No Change — Existing Coverage | books-review:SF-001 | no |",
            "| — | Structural Candidate | books-review:SF-001 | no |",
            1,
        ).replace(
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle",
            "| SF-001 | considered:INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle",
            1,
        ).replace(
            "| Principle Reuse | No Change — Existing Coverage |",
            "| Principle Reuse | Structural Candidate |",
            1,
        )
        errors = self.validator.validate_report_text(structural, self.registry)
        self.assertTrue(any("potential_structural_gap" in error for error in errors))

    def test_complete_report_requires_fresh_context_semantic_audit_for_each_scope(self):
        self_audit = VALID_DAILY_V21.replace("fresh-context:noether", "validator", 1)
        errors = self.validator.validate_report_text(self_audit, self.registry)
        self.assertTrue(any("fresh-context or human" in error for error in errors))

        missing_scope = VALID_DAILY_V21.replace(
            "| AUD-EVD-001 | fresh-context:noether | evidence | review:SF-001; claim:SF-001 | none | Not Required — no unresolved evidence finding | passed |\n",
            "",
        )
        errors = self.validator.validate_report_text(missing_scope, self.registry)
        self.assertTrue(any("semantic audit scope evidence" in error for error in errors))

    def test_every_v21_completion_status_requires_all_four_semantic_scope_rows(self):
        missing_evidence = (
            "| AUD-EVD-001 | fresh-context:noether | evidence | review:SF-001; claim:SF-001 | "
            "none | Not Required — no unresolved evidence finding | passed |\n"
        )
        variants = {
            "Complete": VALID_DAILY_V21,
            "In Progress": VALID_DAILY_V21.replace(
                "| Completion Status | Complete |", "| Completion Status | In Progress |", 1
            ).replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |", 1).replace(
                "| Books Gate | Passed |", "| Books Gate | Open |", 1
            ),
            "Conditional": VALID_DAILY_V21.replace(
                "| Completion Status | Complete |", "| Completion Status | Conditional |", 1
            ).replace(
                "| Coverage Gate | Closed |", "| Coverage Gate | Conditional Pass |", 1
            ).replace(
                "| Evidence Gate | Passed |", "| Evidence Gate | Conditional Pass |", 1
            ).replace(
                "| Books Gate | Passed |", "| Books Gate | Conditional Pass |", 1
            ),
        }
        for status, report in variants.items():
            with self.subTest(status=status):
                errors = self.validator.validate_report_text(
                    report.replace(missing_evidence, "", 1), self.registry
                )
                self.assertTrue(any("semantic audit scope evidence" in error for error in errors))

        self.assertEqual(
            [],
            self.validator.validate_report_text(historical_v21_without_books(), self.registry),
        )

    def test_open_semantic_audit_scopes_force_their_dependent_gates_open(self):
        replacements = (
            (
                "| AUD-COV-001 | fresh-context:noether | coverage | coverage:ORG-A:2026-08-25 | none | Not Required — no unresolved coverage finding | passed |",
                "| AUD-COV-001 | fresh-context:noether | coverage | coverage:ORG-A:2026-08-25 | FIND-COV-001 — cursor not closed | Pending — replay source cursor | open |",
                "Coverage Gate",
            ),
            (
                "| AUD-EVD-001 | fresh-context:noether | evidence | review:SF-001; claim:SF-001 | none | Not Required — no unresolved evidence finding | passed |",
                "| AUD-EVD-001 | fresh-context:noether | evidence | review:SF-001; claim:SF-001 | FIND-EVD-001 — locator conflict | Pending — reread primary source | open |",
                "Evidence Gate",
            ),
            (
                "| AUD-DA-001 | fresh-context:noether | deep_analysis_selection | analysis:DA-001 | none | Not Required — no unresolved selection finding | passed |",
                "| AUD-DA-001 | fresh-context:noether | deep_analysis_selection | analysis:DA-001 | FIND-DA-001 — comparison incomplete | Pending — reselect eligible families | open |",
                "Evidence Gate",
            ),
            (
                "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 | none | Not Required — no unresolved Books finding | passed |",
                "| AUD-BOOK-001 | fresh-context:noether | books | books-review:SF-001 | FIND-BOOK-001 — adjacent owner unchecked | Pending — compare adjacent chapters | open |",
                "Books Gate",
            ),
        )
        for old, new, gate in replacements:
            with self.subTest(scope=gate):
                report = VALID_DAILY_V21.replace(old, new, 1)
                errors = self.validator.validate_report_text(report, self.registry)
                self.assertTrue(any(gate in error and "Open" in error for error in errors))

        deep_open = VALID_DAILY_V21.replace(
            "| AUD-DA-001 | fresh-context:noether | deep_analysis_selection | analysis:DA-001 | none | Not Required — no unresolved selection finding | passed |",
            "| AUD-DA-001 | fresh-context:noether | deep_analysis_selection | analysis:DA-001 | FIND-DA-001 — comparison incomplete | Pending — reselect eligible families | open |",
            1,
        ).replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |", 1)
        errors = self.validator.validate_report_text(deep_open, self.registry)
        self.assertTrue(any("Books Gate" in error and "Open" in error for error in errors))

    def test_partial_and_ordinary_pending_cannot_claim_terminal_completion(self):
        partial = VALID_DAILY_V21.replace("| deep_complete | accessible |", "| pending | partial |", 1)
        errors = self.validator.validate_report_text(partial, self.registry)
        self.assertTrue(any("Evidence Gate must be Open" in error for error in errors))

        invalid_partial = VALID_DAILY_V21.replace("| deep_complete | accessible |", "| deep_complete | partial |", 1)
        errors = self.validator.validate_report_text(invalid_partial, self.registry)
        self.assertTrue(any("partial" in error and "pending or blocked" in error for error in errors))

    def test_blocked_review_requires_materials_request_and_conditional_closure(self):
        blocked = VALID_DAILY_V21.replace("| deep_complete | accessible |", "| blocked | blocked |", 1)
        blocked = blocked.replace("| No Change — Existing Coverage |", "| Blocked / Unverified |", 1)
        blocked = blocked.replace("| Completion Status | Complete |", "| Completion Status | Conditional |")
        blocked = blocked.replace("| Evidence Gate | Passed |", "| Evidence Gate | Conditional Pass |")
        blocked = blocked.replace("| Books Gate | Passed |", "| Books Gate | Conditional Pass |")
        blocked = blocked.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass",
        )
        blocked = blocked.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass；unresolved findings=1.",
        )
        errors = self.validator.validate_report_text(blocked, self.registry)
        self.assertTrue(any("Materials Request" in error for error in errors))

        blocked = blocked.replace("| claim:SF-001 | complete |", "| claim:SF-001 | blocked |", 1)
        blocked = blocked.replace(
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n",
            "",
        )
        self.assertEqual(
            [], self.validator.validate_report_text(blocked + MATERIALS_REQUEST, self.registry)
        )

    def test_disputed_completed_review_needs_a_dispute_record_and_conditional_gate(self):
        disputed = VALID_DAILY_V21.replace("| accessible |", "| disputed |", 1)
        disputed = disputed.replace(
            "| No Change — Existing Coverage | books-review:SF-001 | no |",
            "| Disputed | — | no |",
            1,
        )
        disputed = disputed.replace("| Completion Status | Complete |", "| Completion Status | Conditional |")
        disputed = disputed.replace("| Evidence Gate | Passed |", "| Evidence Gate | Conditional Pass |")
        disputed = disputed.replace("| Books Gate | Passed |", "| Books Gate | Conditional Pass |")
        disputed = disputed.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass",
        )
        disputed = disputed.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=Conditional；Coverage=Closed、Evidence=Conditional Pass、Books=Conditional Pass；unresolved findings=1.",
        )
        disputed = disputed.replace(
            "| SF-001 | INFER-REQUEST-LIFECYCLE | books/example.md#request-lifecycle | books/example-before.md#handoff; books/example-after.md#handoff | existing:SF-001 | delta:SF-001 | Principle Reuse | No Change — Existing Coverage | books-review:SF-001 |\n",
            "",
        )
        errors = self.validator.validate_report_text(disputed, self.registry)
        self.assertTrue(any("dispute ref" in error for error in errors))

        disputed += """
<!-- dispute:SF-001:start -->
The primary and counterevidence disagree under the recorded evaluation contracts.
<!-- dispute:SF-001:end -->
"""
        self.assertEqual([], self.validator.validate_report_text(disputed, self.registry))

    def test_earlier_owner_pending_is_non_terminal_without_requiring_prior_review_ref(self):
        pending = VALID_DAILY_V21.replace("2026-W35 | 2026-08-25", "2026-W34 | 2026-08-18", 1)
        pending = pending.replace(
            "| self | — | new_in_window |",
            "| papers/2026/weekly/owner.md | — | earlier_owner_pending |",
            1,
        )
        pending = pending.replace("| Completion Status | Complete |", "| Completion Status | In Progress |", 1)
        pending = pending.replace("| Evidence Gate | Passed |", "| Evidence Gate | Open |", 1)
        pending = pending.replace("| Books Gate | Passed |", "| Books Gate | Open |", 1)
        pending = pending.replace(
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed",
            "**Status:** In Progress；Coverage=Closed、Evidence=Open、Books=Open",
            1,
        )
        pending = pending.replace(
            "Completion=Complete；Coverage=Closed、Evidence=Passed、Books=Passed；unresolved findings=0.",
            "Completion=In Progress；Coverage=Closed、Evidence=Open、Books=Open；unresolved findings=1.",
            1,
        )
        self.assertEqual([], self.validator.validate_report_text(pending, self.registry))

        terminal = pending.replace("| Completion Status | In Progress |", "| Completion Status | Complete |", 1)
        terminal = terminal.replace("| Evidence Gate | Open |", "| Evidence Gate | Passed |", 1)
        terminal = terminal.replace("| Books Gate | Open |", "| Books Gate | Passed |", 1)
        errors = self.validator.validate_report_text(terminal, self.registry)
        self.assertTrue(any("earlier_owner_pending" in error and "In Progress" in error for error in errors))

    def test_only_reused_unchanged_requires_prior_review_ref(self):
        reused = VALID_DAILY_V21.replace(
            "| self | — | new_in_window |",
            "| self | — | reused_unchanged |",
            1,
        )
        errors = self.validator.validate_report_text(reused, self.registry)
        self.assertTrue(any("reused_unchanged" in error and "Prior Review Ref" in error for error in errors))

    def test_important_revision_is_deep_reviewed_without_becoming_a_second_score_owner(self):
        revision = VALID_DAILY_V21.replace(
            "| 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none |",
            "| — | — | — | — | revision | deep_complete | accessible | important_revision |",
            1,
        )
        revision = revision.replace(
            "| self | — | new_in_window |",
            "| papers/owner.md | — | same_window_revision |",
            1,
        )
        revision = revision.replace(
            "| SF-001 | score_7_9 | selected | DA-001 |",
            "| SF-001 | forced_review | selected | DA-001 |",
            1,
        )
        # Review Override is part of the frozen provenance contract, so an
        # important revision must carry the provenance of the forced route.
        revision = revision.replace("RP-1188b619ab6e379d", "RP-b1fae292ff3ad6ca", 1)
        self.assertEqual([], self.validator.validate_report_text(revision, self.registry))

    def test_spillback_reference_is_weekly_only_and_cannot_point_to_self(self):
        daily_spillback = VALID_DAILY_V21.replace("| new_in_window |", "| spillback_reference |", 1)
        errors = self.validator.validate_report_text(daily_spillback, self.registry)
        self.assertTrue(any("spillback_reference" in error and "Weekly" in error for error in errors))

        weekly_spillback = as_weekly_v21().replace("| new_in_window |", "| spillback_reference |", 1)
        errors = self.validator.validate_report_text(weekly_spillback, self.registry)
        self.assertTrue(any("spillback_reference" in error and "self" in error for error in errors))

    def test_collection_requires_spillback_owner_family_and_nonpending_provenance(self):
        spillback = as_weekly_v21("Historical Weekly").replace(
            "| self | — | new_in_window |",
            "| papers/owner.md | — | spillback_reference |",
            1,
        )
        owner = as_weekly_v21("Historical Weekly").replace(
            "DEN-2026-08-25-V21-001", "DEN-OWNER-SPILLBACK-001", 1
        ).replace("RP-1188b619ab6e379d", "—", 1)
        errors = self.validator.validate_report_collection(
            [(Path("papers/spillback.md"), spillback), (Path("papers/owner.md"), owner)],
            Path("/repo"),
        )
        self.assertTrue(
            any("spillback_reference" in error and "non-pending provenance" in error for error in errors)
        )

    def test_collection_checks_written_back_owner_report_contains_family_and_provenance(self):
        synced = VALID_DAILY_V21.replace("2026-W35 | 2026-08-25", "2026-W34 | 2026-08-18", 1)
        synced = synced.replace(
            "| self | — | new_in_window |",
            "| papers/owner.md | — | earlier_owner_written_back |",
            1,
        )
        owner = as_weekly_v21().replace(
            "DEN-2026-08-25-V21-001", "DEN-2026-W35-OWNER-001", 1
        )
        owner = owner.replace("2026-W35 | 2026-08-25", "2026-W34 | 2026-08-18", 1)
        self.assertEqual(
            [],
            self.validator.validate_report_collection(
                [(Path("papers/daily.md"), synced), (Path("papers/owner.md"), owner)],
                Path("/repo"),
            ),
        )

        unrelated_owner = owner.replace("SF-001", "SF-OTHER")
        errors = self.validator.validate_report_collection(
            [(Path("papers/daily.md"), synced), (Path("papers/owner.md"), unrelated_owner)],
            Path("/repo"),
        )
        self.assertTrue(any("Owner Report Ref" in error and "SF-001" in error for error in errors))

        missing_provenance = owner.replace("RP-1188b619ab6e379d", "—", 1)
        errors = self.validator.validate_report_collection(
            [(Path("papers/daily.md"), synced), (Path("papers/owner.md"), missing_provenance)],
            Path("/repo"),
        )
        self.assertTrue(any("Owner Report Ref" in error and "provenance" in error for error in errors))

    def test_historical_delta_validates_only_changed_source_receipts_and_delta_families(self):
        full = as_weekly_v21("Historical Weekly")
        missing_required = full.replace(
            "| PUB-A | 2026-08-24T00:00:00+08:00 | 2026-08-30T23:59:59+08:00 | 2026-08-30T23:05:00+08:00 | https://publisher.example.org/; venue=example | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-30T23:05:00+08:00 | coverage:PUB-A:2026-W35 | — |\n",
            "",
            1,
        )
        errors = self.validator.validate_report_text(missing_required, self.registry)
        self.assertTrue(any("missing due Source ID PUB-A" in error for error in errors))

        delta = missing_required.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |", 1)
        delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/base.md |", 1)
        delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |", 1)
        delta = delta.replace(
            "| Previous Denominator ID | — |",
            "| Previous Denominator ID | DEN-BASE-001 |",
            1,
        )
        delta = delta.replace("DEN-2026-08-25-V21-001", "DEN-DELTA-001", 1)
        errors = self.validator.validate_report_text(delta, self.registry)
        self.assertFalse(any("missing due Source ID PUB-A" in error for error in errors))

        leaked_baseline_family = delta.replace("| SF-001 |", "| SF-BASELINE-ONLY |", 1)
        errors = self.validator.validate_report_text(leaked_baseline_family, self.registry)
        self.assertTrue(
            any("receipt family SF-BASELINE-ONLY" in error for error in errors)
        )


class CliValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_report_mode_is_strict_for_unmarked_reports(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            legacy = root / "legacy.md"
            legacy.write_text("# Legacy\n\nScore Schema: V2\n", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                status = self.validator.main(["--root", str(root), "--report", str(legacy)])
            self.assertEqual(1, status)

    def test_audit_mode_keeps_legacy_reports_compatible(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            papers = root / "papers"
            papers.mkdir()
            (papers / "legacy.md").write_text("# Legacy\n\nScore Schema: V1 Legacy /30\n", encoding="utf-8")
            output = io.StringIO()
            with redirect_stdout(output):
                status = self.validator.main(["--root", str(root), "--audit", str(papers)])
            self.assertEqual(0, status)
            self.assertIn("legacy skipped", output.getvalue())
            self.assertIn("semantic completeness not validated", output.getvalue())

    def test_directory_audit_excludes_sources_evidence_snapshots(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            papers = root / "papers"
            owner = papers / "2026" / "08" / "25" / "README.md"
            snapshot = papers / "2026" / "08" / "_sources" / "daily-20260825" / "before-reopen.md"
            owner.parent.mkdir(parents=True)
            snapshot.parent.mkdir(parents=True)
            owner.write_text(VALID_DAILY_V21, encoding="utf-8")
            snapshot.write_text(VALID_DAILY_V21, encoding="utf-8")

            output = io.StringIO()
            with redirect_stdout(output):
                status = self.validator.main(["--root", str(root), "--audit", str(papers)])

            self.assertEqual(0, status, output.getvalue())
            self.assertIn("checked 1 V2.1 report(s)", output.getvalue())

            snapshot.write_text("# Historical snapshot without report interfaces\n", encoding="utf-8")
            with redirect_stdout(io.StringIO()):
                strict_status = self.validator.main(
                    ["--root", str(root), "--report", str(snapshot)]
                )
            self.assertEqual(1, strict_status)

    def test_declared_v21_cannot_downgrade_to_v20_interfaces_in_audit_mode(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            papers = root / "papers"
            papers.mkdir()
            report = papers / "declared-v21-old-interface.md"
            report.write_text(
                VALID_DAILY.replace(
                    "| Score Schema | V2 |\n",
                    "| Contract Version | V2.1 |\n| Score Schema | V2 |\n",
                    1,
                ),
                encoding="utf-8",
            )
            output = io.StringIO()
            with redirect_stdout(output):
                status = self.validator.main(["--root", str(root), "--audit", str(papers)])
            self.assertEqual(1, status)
            self.assertIn("V2.1 report is missing marker", output.getvalue())

    def test_cli_golden_reports_cover_daily_weekly_historical_full_and_delta(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            papers = root / "papers"
            papers.mkdir()

            daily = papers / "daily.md"
            weekly = papers / "weekly.md"
            historical_full = papers / "historical-full.md"
            historical_delta = papers / "historical-delta.md"
            daily.write_text(VALID_DAILY_V21, encoding="utf-8")
            weekly.write_text(
                as_weekly_v21().replace("DEN-2026-08-25-V21-001", "DEN-2026-W35-WEEKLY-001"),
                encoding="utf-8",
            )
            baseline = historical_v21_without_books().replace(
                "DEN-2026-08-25-V21-001",
                "DEN-2026-W35-HISTORICAL-FULL-001",
            )
            historical_full.write_text(baseline, encoding="utf-8")
            delta = baseline.replace("| Coverage Mode | Full Replay |", "| Coverage Mode | Delta Audit |")
            delta = delta.replace("| Baseline Report | — |", "| Baseline Report | papers/historical-full.md |")
            delta = delta.replace("| Changed Source IDs | — |", "| Changed Source IDs | ORG-A |")
            delta = delta.replace(
                "| Previous Denominator ID | — |",
                "| Previous Denominator ID | DEN-2026-W35-HISTORICAL-FULL-001 |",
            )
            delta = delta.replace(
                "DEN-2026-W35-HISTORICAL-FULL-001",
                "DEN-2026-W35-HISTORICAL-DELTA-001",
                1,
            )
            delta = delta.replace(
                "| PUB-A | 2026-08-24T00:00:00+08:00 | 2026-08-30T23:59:59+08:00 | 2026-08-30T23:05:00+08:00 | https://publisher.example.org/; venue=example | no_hit | 0 | — | page=1; final_cursor=end | 2026-08-30T23:05:00+08:00 | coverage:PUB-A:2026-W35 | — |\n",
                "",
            )
            historical_delta.write_text(delta, encoding="utf-8")

            for report in (daily, weekly, historical_full, historical_delta):
                with self.subTest(report=report.name), redirect_stdout(io.StringIO()):
                    status = self.validator.main(["--root", str(root), "--report", str(report)])
                self.assertEqual(0, status)

    def test_strict_and_audit_modes_resolve_stable_nodes_from_roadmap(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            papers = root / "papers"
            papers.mkdir()
            report = papers / "report.md"
            report.write_text(
                VALID_DAILY.replace("INFER-REQUEST-LIFECYCLE", "UNKNOWN-NODE"),
                encoding="utf-8",
            )
            with redirect_stdout(io.StringIO()):
                strict_status = self.validator.main(["--root", str(root), "--report", str(report)])
                audit_status = self.validator.main(["--root", str(root), "--audit", str(papers)])
            self.assertEqual(1, strict_status)
            self.assertEqual(1, audit_status)

    def test_empty_or_missing_audit_target_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            empty = root / "empty"
            empty.mkdir()
            with redirect_stdout(io.StringIO()):
                empty_status = self.validator.main(["--root", str(root), "--audit", str(empty)])
                missing_status = self.validator.main(["--root", str(root), "--audit", str(root / "missing")])
            self.assertEqual(1, empty_status)
            self.assertEqual(1, missing_status)


class BundleValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.validator = load_validator()

    def test_contract_bundle_requires_three_contract_links_in_prompts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "RESEARCH_SOURCES.md").write_text(VALID_REGISTRY, encoding="utf-8")
            (root / "docs" / "RESEARCH_CONTRACT.md").write_text(
                "Design Delta\nSystem Reach\nDurability\n", encoding="utf-8"
            )
            (root / "docs" / "REPORT_CONTRACTS.md").write_text(
                "validator:report-metadata-v2\nvalidator:source-coverage-v2\n"
                "validator:candidate-ledger-v2.1\nvalidator:review-completion-v1\n"
                "validator:deep-analysis-selection-v1\nvalidator:books-comparison-v1\n"
                "validator:semantic-audit-v1\nvalidator:materials-request-v1\n"
                "| Books Gate | Passed / Conditional Pass / Open / Not Applicable |\n",
                encoding="utf-8",
            )
            (root / "CODEX_DAILY_RESEARCH_PROMPT.md").write_text("docs/RESEARCH_CONTRACT.md\n", encoding="utf-8")
            (root / "CODEX_HISTORICAL_RESEARCH_PROMPT.md").write_text("docs/RESEARCH_CONTRACT.md\n", encoding="utf-8")
            errors = self.validator.validate_contract_bundle(root)
            self.assertTrue(any("RESEARCH_SOURCES.md" in error for error in errors))
            self.assertTrue(any("REPORT_CONTRACTS.md" in error for error in errors))

    def test_contract_bundle_allows_score_v1_compatibility_prose(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            (root / "docs" / "RESEARCH_SOURCES.md").write_text(VALID_REGISTRY, encoding="utf-8")
            (root / "docs" / "RESEARCH_CONTRACT.md").write_text(
                "Design Delta\nSystem Reach\nDurability\n", encoding="utf-8"
            )
            (root / "docs" / "REPORT_CONTRACTS.md").write_text(
                "validator:report-metadata-v2\nvalidator:source-coverage-v2\n"
                "validator:candidate-ledger-v2.1\nvalidator:review-completion-v1\n"
                "validator:deep-analysis-selection-v1\nvalidator:books-comparison-v1\n"
                "validator:semantic-audit-v1\nvalidator:materials-request-v1\n"
                "| Books Gate | Passed / Conditional Pass / Open / Not Applicable |\n",
                encoding="utf-8",
            )
            links = "\n".join(
                (
                    "docs/RESEARCH_CONTRACT.md",
                    "docs/RESEARCH_SOURCES.md",
                    "docs/REPORT_CONTRACTS.md",
                )
            )
            (root / "CODEX_DAILY_RESEARCH_PROMPT.md").write_text(
                links + "\nTechnical Novelty\n", encoding="utf-8"
            )
            (root / "CODEX_HISTORICAL_RESEARCH_PROMPT.md").write_text(links, encoding="utf-8")
            errors = self.validator.validate_contract_bundle(root)
            self.assertFalse(any("Score V1 policy" in error for error in errors))

    def test_report_contract_must_publish_the_materials_request_schema_marker(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            report_contract = root / "docs" / "REPORT_CONTRACTS.md"
            report_contract.write_text(
                report_contract.read_text(encoding="utf-8").replace(
                    "<!-- validator:materials-request-v1 -->\n",
                    "",
                ),
                encoding="utf-8",
            )
            errors = self.validator.validate_contract_bundle(root)
            self.assertTrue(any("materials-request-v1" in error for error in errors))

    def test_report_contract_must_publish_books_conditional_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            write_contract_root(root)
            report_contract = root / "docs" / "REPORT_CONTRACTS.md"
            report_contract.write_text(
                report_contract.read_text(encoding="utf-8").replace(
                    "| Books Gate | Passed / Conditional Pass / Open / Not Applicable |\n",
                    "| Books Gate | Passed / Open / Not Applicable |\n",
                ),
                encoding="utf-8",
            )
            errors = self.validator.validate_contract_bundle(root)
            self.assertTrue(any("Books Gate must publish Conditional Pass" in error for error in errors))

    def test_repository_registry_contains_the_approved_source_delta(self):
        records, errors = self.validator.validate_registry_text(
            (ROOT / "docs" / "RESEARCH_SOURCES.md").read_text(encoding="utf-8")
        )
        self.assertEqual([], errors)
        required = {
            "SRC-AI21",
            "SRC-STABILITY-AI",
            "SRC-BLACK-FOREST-LABS",
            "SRC-RUNWAY",
            "SRC-LIQUID-AI",
            "SRC-TOGETHER-AI",
            "SRC-MEITUAN-LONGCAT",
            "SRC-PHYSICAL-INTELLIGENCE",
            "SRC-WORLD-LABS",
            "SRC-METR",
            "SRC-UK-AISI",
            "SRC-NIST-AI",
            "SRC-MLCOMMONS",
            "SRC-STANFORD-CRFM",
            "SRC-MLSYS",
            "SRC-ACM-DL",
            "SRC-IEEE-XPLORE",
            "SRC-USENIX",
            "SRC-VERL",
            "SRC-NEMO-RL",
            "SRC-TORCHTITAN",
            "SRC-MAXTEXT",
            "SRC-LLM-D",
            "SRC-GATEWAY-INFERENCE",
            "SRC-KUEUE",
            "SRC-JOBSET",
            "SRC-LEADERWORKERSET",
            "SRC-NCCL",
            "SRC-RCCL",
            "SRC-TRANSFORMER-ENGINE",
            "SRC-FLASHINFER",
            "SRC-DEEPEP",
            "SRC-DEEPGEMM",
            "SRC-MCP",
            "SRC-A2A",
            "SRC-TRITON-LANGUAGE",
            "SRC-TRITON-SERVER",
        }
        self.assertEqual(set(), required - set(records))

    def test_repository_registry_preserves_merge_and_cadence_policy(self):
        records, errors = self.validator.validate_registry_text(
            (ROOT / "docs" / "RESEARCH_SOURCES.md").read_text(encoding="utf-8")
        )
        self.assertEqual([], errors)
        self.assertNotIn("SRC-GOOGLE-DEEPMIND", records)
        self.assertIn("Google DeepMind", records["SRC-GOOGLE-AI"]["Aliases"])
        self.assertIn("Zhipu AI", records["SRC-ZAI"]["Aliases"])
        self.assertEqual("Required Weekly", records["SRC-APPLE-ML"]["Cadence"])
        self.assertEqual("Required Weekly", records["SRC-OPENREVIEW"]["Cadence"])
        self.assertEqual("Discovery / Recovery Backstop", records["SRC-GOOGLE-SCHOLAR"]["Cadence"])
        self.assertEqual("Discovery / Metadata", records["SRC-HF-PAPERS"]["Authority Role"])
        self.assertEqual("Discovery / Metadata", records["SRC-HF-BLOG"]["Authority Role"])


if __name__ == "__main__":
    unittest.main()
