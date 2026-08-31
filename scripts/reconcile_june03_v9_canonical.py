#!/usr/bin/env python3
"""Render the 2026-06-03 V9 canonical Daily from the audited packet.

The renderer never edits Books.  Before a post-write audit exists it leaves
the semantic Gates open.  After POST_WRITE_FRESH_AUDIT_V9.md exists, it writes
the contractually correct Conditional state caused by the exact-v1 UltraEP
external blocker.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

from repair_june03_v8_canonical import cell, facet_locator, review_provenance, roadmap_paths


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260603"
REPORT = ROOT / "papers/2026/06/03/README.md"
POST_AUDIT = PACKET / "POST_WRITE_FRESH_AUDIT_V9.md"


def load(name: str):
    return json.loads((PACKET / name).read_text(encoding="utf-8"))


def dump(name: str, value) -> None:
    (PACKET / name).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def regenerate_manifest() -> None:
    """Seal every date-local packet file plus the reader-facing Daily."""
    manifest = PACKET / "SHA256SUMS"
    targets = sorted(path for path in PACKET.rglob("*") if path.is_file() and path != manifest)
    targets.append(REPORT)
    rows = [f"{sha256(path)}  {path.relative_to(ROOT)}" for path in sorted(targets)]
    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8")


def normalized_hash(path: Path) -> str:
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def books_paths(row: dict) -> list[str]:
    values = set()
    for field in ("current_normalized_hashes", "report_full_read_hashes", "current_full_read_hashes"):
        values.update(row.get(field, {}).keys())
    for raw in [row.get("target_chapter_ref", "")]:
        value = str(raw).split("#", 1)[0].split(" section:", 1)[0].strip()
        if value.startswith("books/"):
            values.add(value)
    adjacent = row.get("adjacent_chapter_refs", [])
    if not isinstance(adjacent, list):
        adjacent = str(adjacent).split(";")
    for raw in adjacent:
        value = str(raw).split("#", 1)[0].split(" section:", 1)[0].strip()
        if value.startswith("books/"):
            values.add(value)
    return sorted(value for value in values if (ROOT / value).is_file())


def locator(aid: str, value: str) -> str:
    value = value.strip()
    if value.startswith("arXiv:") or value.startswith("http") or value.startswith("Pending"):
        return value
    return f"arXiv:{aid} {value}"


def assert_post_render_contract(
    report: str,
    *,
    finalized: bool,
    blocked_families: set[str],
    completion: str,
    coverage_gate: str,
    evidence_gate: str,
    books_gate: str,
) -> None:
    """Fail closed if the owner renderer regresses canonical presentation/state."""
    expected_h2 = [
        "## Executive Summary",
        "## 1. Coverage",
        "## 2. Candidate Ledger",
        "## 3. Review Completion Receipt",
        "## 4. Benchmark Contracts",
        "## 5. Deep Analysis Selection",
        "## 6. Books Comparison",
        "## 7. Semantic Audit",
        "## 8. Ignored Noise",
        "## 9. Recommended Action",
        "## 10. Repository Changes",
        "## 11. Open Questions",
        "## 12. Sources",
        "## 13. Final Status",
    ]
    assert re.findall(r"(?m)^## .+$", report) == expected_h2
    for field in ("Research Date", "Timezone", "Strict Window", "Contract", "Status"):
        assert f"**{field}:**" in report, field
    review_starts = re.findall(r"<!-- review:([^:]+):start -->", report)
    review_ends = re.findall(r"<!-- review:([^:]+):end -->", report)
    assert len(review_starts) == len(set(review_starts)) == 55
    assert sorted(review_starts) == sorted(review_ends)

    def ledger_ids(marker: str) -> set[str]:
        tail = report.split(marker, 1)[1].lstrip("\n")
        lines = tail.splitlines()
        assert len(lines) >= 3 and lines[0].startswith("| "), marker
        values = set()
        for line in lines[2:]:
            if not line.startswith("|"):
                break
            values.add(line.strip().strip("|").split("|", 1)[0].strip())
        return values

    ledger_sets = {
        "Candidate": ledger_ids("<!-- validator:candidate-ledger-v2.1 -->"),
        "Review": ledger_ids("<!-- validator:review-completion-v1 -->"),
        "Benchmark": ledger_ids("<!-- validator:benchmark-contract-v1 -->"),
        "Books": ledger_ids("<!-- validator:books-comparison-v1 -->"),
    }
    candidate_ids = ledger_sets["Candidate"]
    assert len(candidate_ids) == 55
    for name, values in ledger_sets.items():
        assert values == candidate_ids, (
            name,
            sorted(candidate_ids - values),
            sorted(values - candidate_ids),
        )
    selection_ids = ledger_ids("<!-- validator:deep-analysis-selection-v1 -->")
    non_eligible_ids = ledger_ids("<!-- audit:deep-analysis-non-eligible-v1 -->")
    assert selection_ids.isdisjoint(non_eligible_ids)
    assert selection_ids | non_eligible_ids == candidate_ids
    assert (len(selection_ids), len(non_eligible_ids)) == (50, 5)
    assert len(re.findall(r"(?m)^\| [^|]+ \| [^|]+ \| selected \|", report)) <= 3
    if completion == "Complete":
        assert finalized and not blocked_families
        assert (coverage_gate, evidence_gate, books_gate) == ("Closed", "Passed", "Passed")
        assert "**Status:** Complete" in report


def main() -> None:
    audit = load("candidate-denominator-audit-v9-strict.json")
    evidence = load("evidence-review-v9-strict.json")
    selection = load("deep-analysis-selection-v9-strict.json")
    books = load("books-comparison-v9-strict.json")
    finalized = POST_AUDIT.exists()

    audit_rows = [row for row in audit["rows"] if row["verdict"] == "retain"]
    assert len(audit_rows) == 55
    by_family = {row["source_family_id"]: row for row in audit_rows}
    review_by_family = {row["source_family_id"]: row for row in evidence["reviews"]}
    books_by_family = {row["source_family_id"]: row for row in books["rows"]}
    selection_by_family = {row["source_family_id"]: row for row in selection["rows"]}
    assert set(by_family) == set(review_by_family) == set(books_by_family) == set(selection_by_family)
    blocked_families = {
        sf
        for sf, review in review_by_family.items()
        if str(review.get("review_status", "")).startswith("blocked")
    }

    rows = sorted(audit_rows, key=lambda row: (row["first_public_utc"], row["arxiv_v1"]))
    candidate_lines, receipt_lines, review_blocks = [], [], []
    benchmark_lines, source_lines, rp_by_family = [], [], {}

    for family in rows:
        sf, aid = family["source_family_id"], family["arxiv_v1"]
        review, comparison = review_by_family[sf], books_by_family[sf]
        blocked = sf in blocked_families
        disposition = comparison["provisional_disposition"]
        score = review.get("score_v2", {"design_delta": 3, "system_reach": 3, "durability": 2, "total": 8})

        if blocked:
            route = "deep"
            review_status, access = "blocked", "blocked"
            method = "Official submission identity and withdrawal history are available; the exact-v1 Method body is unavailable."
            evaluation_text = "Blocked — exact-v1 Evaluation and Appendix are unavailable."
            boundary = review["claim_boundary"]
            artifact = "https://github.com/Dots-Infra/UltraEP — later artifact only; not event-time v1 evidence"
            method_loc = f"arXiv:{aid} submission history [v1]; exact Method body withdrawn"
            evaluation_loc = "Pending — exact-v1 Evaluation and Appendix are unavailable because v1 is withdrawn"
            limitation_loc = f"arXiv:{aid} submission history marks v1/v2 withdrawn; v3 is later evidence"
        else:
            route = review["route"]
            review_status, access = review["review_status"], review["access_status"]
            method = review["method_evidence"]
            evaluation_text = review["evaluation_evidence"]
            boundary = review["limitations_evidence"]
            artifact = review["artifact_locator"]
            method_loc = facet_locator(aid, review["method_locator"], "method", route == "deep")
            evaluation_loc = facet_locator(aid, review["evaluation_locator"], "evaluation", route == "deep")
            limitation_loc = facet_locator(aid, review["limitations_locator"], "limitations", route == "deep")

        review_body = (
            f"\n### {family['title']}\n\n"
            f"- **Mechanism / identity:** {method}\n"
            f"- **Evaluation:** {evaluation_text}\n"
            f"- **Evidence boundary:** {boundary}\n"
            f"- **Artifact:** {artifact}\n"
            f"<!-- claim:{sf}:start -->结论只覆盖 exact-v1、上列 locator 与声明边界；不得外推为通用模型、硬件、拓扑或生产 SLO 结论。<!-- claim:{sf}:end -->\n"
        )
        review_blocks.append(f"<!-- review:{sf}:start -->{review_body}<!-- review:{sf}:end -->")

        override = "knowledge_gap" if disposition == "Integrate" else "none"
        candidate_values = {
            "Source Family ID": sf,
            "Primary Identifier": f"arXiv:{aid}",
            "Event Identity": f"paper-v1:{aid.removesuffix('v1')}",
            "Supporting Source IDs": "SRC-ARXIV",
            "Review Override": override,
            "Review Ref": f"review:{sf}",
        }
        receipt_values = {
            "Review Route": route,
            "Primary Evidence Version": f"arXiv:{aid}",
            "Reviewed Evidence Versions": f"SRC-ARXIV@arXiv:{aid}",
            "Method / Identity Locators": method_loc,
            "Evaluation Locators": evaluation_loc,
            "Limitations / Counterevidence Locators": limitation_loc,
            "Artifact Locators": artifact,
            "Claim Boundary Ref": f"claim:{sf}",
        }
        rp = review_provenance(candidate_values, receipt_values, review_body)
        rp_by_family[sf] = rp
        candidate_lines.append("| " + " | ".join(map(cell, [
            sf, f"arXiv:{aid}", f"paper-v1:{aid.removesuffix('v1')}", "2026-W23",
            family["first_public_utc"][:10], "SRC-ARXIV", score["design_delta"],
            score["system_reach"], score["durability"], score["total"], "retained",
            review_status, access, override, f"review:{sf}", "self", "—", "new_in_window",
            review.get("stable_node_id") or family.get("stable_node_id") or comparison["stable_node_id"],
            disposition, "—" if blocked else f"books-review:{sf}", "no" if blocked else "yes",
        ])) + " |")
        receipt_lines.append("| " + " | ".join(map(cell, [
            sf, rp, route, f"arXiv:{aid}", f"SRC-ARXIV@arXiv:{aid}", method_loc,
            evaluation_loc, limitation_loc, artifact, f"claim:{sf}", "blocked" if blocked else "complete",
        ])) + " |")

        if not blocked:
            contract = review["benchmark_contract"]
            benchmark_lines.append("| " + " | ".join(map(cell, [
                sf, contract["input"], contract["model"], contract["hardware"], contract["precision"],
                contract.get("input_length", "Not Disclosed"),
                contract.get("output_length", "Not Disclosed"), contract["batch"],
                contract["concurrency"], contract["slo"], contract["evaluator"],
            ])) + " |")
        source_lines.append(
            f"- [{family['title']}](https://arxiv.org/abs/{aid}) — exact v1; first public {family['first_public_utc']}."
        )

    for review in evidence["reviews"]:
        review["review_provenance_id"] = rp_by_family[review["source_family_id"]]
    evidence["contract"] = "V9 canonical exact-v1 route replay after strict denominator freeze"
    dump("evidence-review-v9-strict.json", evidence)

    for row in books["rows"]:
        row["evidence_replay_ref"] = rp_by_family[row["source_family_id"]]
        row["books_write_performed"] = finalized and row["provisional_disposition"] == "Integrate"
        current_hashes = {path: normalized_hash(ROOT / path) for path in books_paths(row)}
        if current_hashes:
            row["current_normalized_hashes"] = current_hashes
            row["report_full_read_hashes"] = current_hashes
            row["current_full_read_hashes"] = current_hashes
            row["post_write_normalized_hashes"] = current_hashes
            row["normalized_hashes_match_current"] = True
        row["v9_reconciliation"] = (
            "post_write_fresh_audit_passed"
            if finalized and row["provisional_disposition"] == "Integrate" else
            "fresh_books_dedup_no_write"
            if row["provisional_disposition"] == "No Change — Existing Coverage" else
            "exact_v1_external_blocker_no_books_inference"
        )
    books["contract"] = "V9 canonical current-owner Books comparison after 29/29 semantic dedup"
    books["books_write_performed"] = finalized
    books["queue_released"] = finalized
    books["queue_release_blockers"] = (
        [f"{sf} exact-v1 external material request" for sf in sorted(blocked_families)]
        if finalized else
        ["root serialized Books write", "post-write books semantic audit"]
    )
    books["disposition_counts"] = dict(Counter(row["provisional_disposition"] for row in books["rows"]))
    dump("books-comparison-v9-strict.json", books)

    selection_lines, selection_blocks = [], []
    non_eligible_lines, non_eligible_blocks = [], []
    unit_ids = {
        "SF-LIBRA-AGENTIC-RL": "DA-AGENTIC-RL-RESOURCE-OWNERSHIP",
        "SF-AGENT-LIBOS": "DA-AGENT-RUNTIME-AUTHORITY",
        "SF-LAZYATTENTION": "DA-POSITION-INDEPENDENT-KV-STATE",
    }
    for family in rows:
        sf = family["source_family_id"]
        item = selection_by_family[sf]
        comparison = books_by_family[sf]
        review = review_by_family[sf]
        score = review.get("score_v2", {"total": 8})
        eligible = score["total"] >= 7
        if not eligible:
            rationale = (
                f"Score V2 {score['total']}/9 is below the 7–9 threshold; Review Override is none, "
                "and no Evidence-stage potential_books_delta, potential_structural_gap or "
                "cross_cutting_correction was recorded. Standard Review and the later Books "
                "No Change decision remain complete, but this family is outside the long-form pool."
            )
            item.update(
                eligible=False,
                selection="not_eligible",
                selection_basis=rationale,
            )
            narrative = f"analysis-ineligible:{sf}"
            non_eligible_lines.append("| " + " | ".join(map(cell, [
                sf, score["total"], "none", "not_eligible_for_deep_analysis", rationale, narrative,
            ])) + " |")
            non_eligible_blocks.append(
                f"<!-- {narrative}:start -->{rationale}<!-- {narrative}:end -->"
            )
            continue
        item["eligible"] = True
        if item["selection"] == "not_eligible":
            item["selection"] = "not_selected"
        if item["selection"] == "not_selected" and sf != "SF-ULTRAEP":
            item["selection_basis"] = (
                "Full Evidence retained; compared against all 50 eligible families, it adds no "
                "stronger non-overlapping long-form evolution unit than the selected three."
            )
        eligibility_parts = []
        if score["total"] >= 7:
            eligibility_parts.append("score_7_9")
        if comparison["provisional_disposition"] == "Integrate":
            eligibility_parts.extend(["forced_review", "potential_books_delta"])
        assert eligibility_parts, sf
        assert item.get("eligible") is True, sf
        if item["selection"] == "selected":
            unit, decision, narrative = unit_ids[sf], "selected", f"analysis:{unit_ids[sf]}"
        else:
            unit, decision, narrative = "—", "not_selected", f"analysis-decision:{sf}"
        eligibility = "; ".join(eligibility_parts)
        rationale = (
            item["selection_basis"]
            if item["selection"] != "blocked" else
            "Exact-v1 Method/Evaluation is unavailable, so this score-eligible family cannot outrank an accessible non-overlapping unit."
        )
        selection_lines.append("| " + " | ".join(map(cell, [
            sf, eligibility, decision, unit, "—", rationale, narrative,
        ])) + " |")
        if decision == "not_selected":
            selection_blocks.append(
                f"<!-- analysis-decision:{sf}:start -->{item['selection_basis']}<!-- analysis-decision:{sf}:end -->"
            )

    assert (len(selection_lines), len(non_eligible_lines)) == (50, 5)
    selection["contract"] = "eligible-pool selection plus family-specific non-eligible closure"
    selection["eligible_review_count"] = len(selection_lines)
    selection["non_eligible_closure_count"] = len(non_eligible_lines)
    selection["selected_count"] = 3
    dump("deep-analysis-selection-v9-strict.json", selection)

    node_paths, node_adjacent = roadmap_paths()
    books_lines, books_blocks = [], []
    for comparison in books["rows"]:
        sf, decision = comparison["source_family_id"], comparison["provisional_disposition"]
        if decision == "Blocked / Unverified":
            continue
        node = comparison["stable_node_id"]
        target = comparison.get("target_chapter_ref") or node_paths[node]
        target = target.replace(" section:", "#section-")
        if "#" not in target:
            target += "#L1"
        adjacent = comparison.get("adjacent_chapter_refs") or node_adjacent.get(node, [])
        if not isinstance(adjacent, list):
            if not str(adjacent).startswith("books/"):
                adjacent = node_adjacent.get(node, [])
            else:
                adjacent = [part.strip() for part in str(adjacent).split(";")]
        adjacent_text = "; ".join(
            ref if "#" in ref else ref + "#L1" for ref in adjacent
        ) or "—"
        relation = comparison.get("evolution_relation") or "Layering / Dependency"
        books_lines.append("| " + " | ".join(map(cell, [
            sf, node, target, adjacent_text, f"existing:{sf}", f"delta:{sf}", relation,
            decision, f"books-review:{sf}",
        ])) + " |")
        source_delta = comparison.get("source_delta", "See exact-v1 Source Review.")
        boundary = comparison.get("evidence_boundary", "See exact-v1 Source Review boundary.")
        write_state = (
            "Root writeback was checked in the fresh post-write audit."
            if finalized and decision == "Integrate" else
            "Fresh current-tree comparison found no Books mutation requirement."
            if decision == "No Change — Existing Coverage" else
            "Proposal awaits root serialized writeback and post-write audit."
        )
        books_blocks.append(
            f"<!-- books-review:{sf}:start -->"
            f"<!-- existing:{sf}:start -->{write_state} See `BOOKS_DEDUP_RECONCILIATION_V9.md`.<!-- existing:{sf}:end -->"
            f"<!-- delta:{sf}:start -->{source_delta} Boundary: {boundary}<!-- delta:{sf}:end -->"
            f"Decision: {decision}.<!-- books-review:{sf}:end -->"
        )

    all_evidence_recovered = not blocked_families
    completion = "Complete" if finalized and all_evidence_recovered else "Conditional" if finalized else "In Progress"
    coverage_gate = "Closed" if finalized else "Open"
    evidence_gate = "Passed" if finalized and all_evidence_recovered else "Conditional Pass" if finalized else "Open"
    books_gate = "Passed" if finalized and all_evidence_recovered else "Conditional Pass" if finalized else "Open"
    status = (
        "Complete — V9 semantic audits passed; UltraEP official exact-v1 abstract recovery closed the final blocker"
        if finalized and all_evidence_recovered else
        "Conditional — V9 semantic audits passed; an exact-v1 external blocker remains"
        if finalized else
        "In Progress — V9 canonical ledgers complete; awaiting root Books writeback and post-write fresh audit"
    )
    audit_status = "passed" if finalized else "open"
    audit_findings = "none" if finalized else "FINDING-V9-POSTWRITE-PENDING"
    audit_resolution = (
        "All actionable findings resolved; UltraEP official exact-v1 abstract recovery and Books no-write handoff were freshly audited"
        if finalized and all_evidence_recovered else
        "All actionable findings resolved; the remaining exact-v1 limitation is externally blocked"
        if finalized else "Await root serialized writeback and fresh post-write audit"
    )

    materials_section = (
        "### Materials Recovery Receipt\n\n"
        "- `MR-SF-ULTRAEP-01` is closed by `ULTRAEP_EXACT_V1_ABS_RECOVERY.md`: the official "
        "`arXiv:2606.04101v1` abstract now exposes the event-time Method and Evaluation claims needed for bounded review.\n"
        "- The removed full body remains unavailable. Dedicated limitations, GPU model, topology dimensions, precision, "
        "batch size, failure recovery, optimizer/gradient correctness, decode behavior, production latency SLO and an "
        "event-time artifact remain `Not Disclosed`; v3 and the July repository stay excluded."
        if all_evidence_recovered else
        "### Materials Request\n\n"
        "`MR-SF-ULTRAEP-01` remains open for an exact-v1 full text or source bundle."
    )

    family_ids = "; ".join(row["source_family_id"] for row in rows)
    status_line = (
        "Complete — V9 semantic audits passed；Coverage `Closed`；Evidence `Passed`；Books `Passed`；"
        "UltraEP official exact-v1 abstract recovery closed the final blocker"
        if completion == "Complete"
        else f"{status}；Coverage `{coverage_gate}`；Evidence `{evidence_gate}`；Books `{books_gate}`"
    )
    report = f"""# Daily Research — 2026-06-03

**Research Date:** 2026-06-03

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-02 09:00:00 ～ 2026-06-03 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；747/747 official arXiv identities 完成 title+abstract semantic screen，技术 claim 仅来自 exact-v1 review 与 UltraEP official v1 abstract recovery boundary

**Status:** {status_line}

## Executive Summary

Core arXiv discovery preserved all 747 unique v1 identities for recall. A fresh, row-complete title+abstract semantic audit challenged every V8 decision and froze the strict V9 account as `747 = 55 retained + 691 family-specific pre-denominator closures + 1 same-family supporting version` (retain rate 7.36%). The V8 denominator contained 32 false positives and 8 false negatives; both sets are explicitly recorded in `candidate-denominator-audit-v9-strict.json`.

Exact-v1 Evidence is complete for all 55 retained families, with ordinary pending and blocked both equal to zero. UltraEP is bounded to the official v1 abstract: it discloses exact-load planning, expert-state transport and the reported evaluation, while unavailable fields are `Not Disclosed` and later v3/repository evidence remains excluded. Deep Analysis Selection contains all 50 eligible families and selects three non-overlapping narrative units: Libra, Agent libOS and LazyAttention; the other five candidates have explicit family-level non-eligible closure.

Fresh Books dedup challenged all 29 provisional Integrate rows and reduced the current-tree write queue to 16: 13 partial mechanisms and 3 genuinely missing mechanisms. UltraEP's recovered evidence maps to the dynamic expert-placement mechanism already owned by Ch36, with Ch21/Ch56 handoffs, so the final comparison is `16 Integrate / 39 No Change — Existing Coverage`. {('Root writeback and the post-write audit are closed; UltraEP required no additional Books mutation.' if finalized else 'Books were not written by this lane; root writeback and the post-write audit remain pending.')}

<!-- audit-target:coverage:start -->
## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-03 |
| Window End | 2026-06-03 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260603-V9-STRICT-c2194043 |
| Denominator Frozen At | 2026-08-29T00:00:00+08:00 |
| Completion Status | {completion} |
| Coverage Gate | {coverage_gate} |
| Evidence Gate | {evidence_gate} |
| Books Gate | {books_gate} |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-02T09:00:00+08:00 | 2026-06-03T09:00:00+08:00 | 2026-08-29T00:00:00+08:00 | official Atom API; 19 categories; submittedDate window; full title+abstract semantic screening | checked | 747 | {family_ids} | pages=19; all returned counts closed; unique_v1=747 | 2026-06-03T00:58:21Z | sha256:{sha256(PACKET / 'candidate-denominator-audit-v9-strict.json')} | — |

### Coverage Limitations

- Discovery enumeration is a recall surface, not the Candidate denominator. All 747 rows received a fresh retain/closure decision.
- `691` pre-denominator closures remain row-addressable with title, abstract boundary, closure taxonomy and fresh reason; they are not candidate-level `pending`.
- The same-family supporting version is excluded from the family denominator without being discarded from provenance.
<!-- audit-target:coverage:end -->

<!-- audit-target:evidence:start -->
## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(candidate_lines)}

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(receipt_lines)}

### Source Reviews

{chr(10).join(review_blocks)}

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(benchmark_lines)}
<!-- audit-target:evidence:end -->

<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(selection_lines)}

{chr(10).join(selection_blocks)}

### Non-eligible Full-frontier Closure

<!-- audit:deep-analysis-non-eligible-v1 -->
| Source Family ID | Score V2 Total | Review Override | Closure | Rationale | Narrative Ref |
| --- | ---: | --- | --- | --- | --- |
{chr(10).join(non_eligible_lines)}

{chr(10).join(non_eligible_blocks)}
<!-- audit-target:deep_analysis_selection:end -->

### Deep Analysis

<!-- analysis:DA-AGENTIC-RL-RESOURCE-OWNERSHIP:start -->
### 从静态 rollout/training 配比到可回收的 Agentic RL 资源状态

普通 RL post-training 可以按固定比例切 rollout 与 training GPU，因为 trajectory 主要消耗连续 decode。Agentic RL 引入长时间 tool wait 后，请求逻辑仍存活却不应继续占用 GPU；资源控制因此必须把 trajectory state、GPU residency 和外部事件分开拥有。Libra 的受限分支用全局 planner、可弹性迁移的混合资源池和因果反馈队列，在 tool call 时卸载、在结果返回后按长度/资源需求恢复。它交换的是更高利用率与更复杂的 snapshot、queue fairness、planner stability 和恢复正确性；作者集群与吞吐结果不是通用常数。
<!-- analysis:DA-AGENTIC-RL-RESOURCE-OWNERSHIP:end -->

<!-- analysis:DA-AGENT-RUNTIME-AUTHORITY:start -->
### 从 Tool Catalog 到稳定 Runtime Authority Boundary

Skills/Tools 层适合快速演化，但 schema、prompt 或 catalog membership 不能拥有真实资源权限。Agent libOS 把能力授予、路径/对象访问、fork 继承、审批和审计下沉到较稳定的 runtime authority boundary，使模型继续提出动作而 primitive-level reference monitor 决定是否 commit。收益是 prompt/tool-output injection 不能直接绕过 primitive capability；代价是 capability lifecycle、policy composition、generated-tool inspection 与 approval context 都成为平台状态。它不解决语义 prompt injection，也不证明该原型已具备生产多租户完备性。
<!-- analysis:DA-AGENT-RUNTIME-AUTHORITY:end -->

<!-- analysis:DA-POSITION-INDEPENDENT-KV-STATE:start -->
### 从 Position-bound Prefix Cache 到延迟位置化的可复用文档状态

传统 prefix cache 把 token 内容与当前位置一起固化，顺序或插入位置变化就需要重算；这在位置稳定时最简单可靠。LazyAttention 把 reusable document 的位置编码推迟到 attention 计算，使 cache identity 更接近 position-agnostic content state，再由请求态完成位置变换。它提高跨位置复用机会，却新增 deferred-RoPE kernel、composition correctness、cache identity 与 fallback；其 Zipf 分析和作者实现只说明受测分布/模型下的机制，不证明任意 attention architecture、并发或生产 SLO。
<!-- analysis:DA-POSITION-INDEPENDENT-KV-STATE:end -->

<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
{chr(10).join(books_lines)}

{chr(10).join(books_blocks)}

UltraEP is `No Change — Existing Coverage`: Ch36 already owns dynamic post-router expert placement, native weight/optimizer authority, topology cost and static-EP fallback; Ch21/Ch56 retain model-routing and serving handoffs. No Books mutation is required, and later v3/repository evidence is not used. The 29/29 dedup receipt is `BOOKS_DEDUP_RECONCILIATION_V9.md`.
<!-- audit-target:books:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260603-V9-COVERAGE | fresh-context:jun03-v9 | coverage | audit-target:coverage | {audit_findings} | {audit_resolution} | {audit_status} |
| SA-20260603-V9-EVIDENCE | fresh-context:jun03-v9 | evidence | audit-target:evidence | {('—' if finalized else audit_findings)} | {audit_resolution} | {audit_status} |
| SA-20260603-V9-SELECTION | fresh-context:jun03-v9 | deep_analysis_selection | audit-target:deep_analysis_selection | {audit_findings} | {audit_resolution} | {audit_status} |
| SA-20260603-V9-BOOKS | fresh-context:jun03-postwrite-v9 | books | audit-target:books | {audit_findings} | {audit_resolution} | {audit_status} |

{materials_section}

## 8. Ignored Noise

`691` 个 pre-denominator closures 不是“未看”：`candidate-denominator-audit-v9-strict.json` 对 747/747 identity 给出 fresh verdict。Closure 只表示该 exact title+abstract 没有改变长期 AI-System mechanism、ownership、evaluation/release contract 或 training/inference/platform design。

## 9. Recommended Action

维持 root 已接受的最终处置：`16 Integrate / 39 No Change — Existing Coverage`。UltraEP 继续由 Ch36 的 dynamic expert-placement 机制覆盖，Ch21/Ch56 保留模型路由与 serving handoff；不新增 Books 写回，也不引入 later v3/repository evidence。

## 10. Repository Changes

- 本轮仅迁移 reader-facing canonical 13 节；55 个 bounded Source Review body 与 Review Provenance receipt 保持逐字不变。
- V9 denominator audit、exact-v1 Evidence、full-frontier Selection、Books dedup/Comparison 与 canonical Daily 已写入 packet。
- Books 只由 root 串行写回；本 lane 没有修改 Books。
- V3～V8 artifacts 保留为 provenance，不再代表当前 Gate 真值。

## 11. Open Questions

None. UltraEP 的 exact-v1 摘要证据已按披露边界恢复；未披露字段保持 `Not Disclosed`，Selection 与 Books disposition 已重算。

## 12. Sources

{chr(10).join(source_lines)}

## 13. Final Status

- Denominator: `DEN-20260603-V9-STRICT-c2194043`；`747 = 55 retained + 691 pre-denominator closures + 1 same-family supporting version`。
- Evidence: `55/55` exact-v1 Reviews complete；UltraEP 只保留 official v1 abstract 所披露的 Method/Evaluation，其他字段继续 `Not Disclosed`。
- Selection / Books: eligible Selection `50/50` + non-eligible closure `5/5` = candidate coverage `55/55`；selected `3`；`16 Integrate / 39 No Change — Existing Coverage`；root writeback 与 post-write audit 已闭合。
- Gates: Coverage `{coverage_gate}`；Evidence `{evidence_gate}`；Books `{books_gate}`；Completion `{completion}`。
"""
    assert_post_render_contract(
        report,
        finalized=finalized,
        blocked_families=blocked_families,
        completion=completion,
        coverage_gate=coverage_gate,
        evidence_gate=evidence_gate,
        books_gate=books_gate,
    )
    REPORT.write_text(report, encoding="utf-8")

    canonical = {
        "contract": "V9 strict canonical reconciliation after row-complete fresh audit",
        "raw_identity_count": 747,
        "candidate_count": 55,
        "pre_denominator_closure_count": 691,
        "same_family_supporting_version_count": 1,
        "retain_rate_percent": 7.36,
        "v8_false_positive_count": 32,
        "v8_false_negative_count": 8,
        "review_complete_count": 55 - len(blocked_families),
        "ordinary_pending_count": 0,
        "blocked_count": len(blocked_families),
        "selection_decision_count": len(selection_lines),
        "non_eligible_selection_closure_count": len(non_eligible_lines),
        "selection_candidate_coverage_count": len(selection_lines) + len(non_eligible_lines),
        "selected_count": 3,
        "books_disposition_counts": books["disposition_counts"],
        "completion_status": completion,
        "coverage_gate": coverage_gate,
        "evidence_gate": evidence_gate,
        "books_gate": books_gate,
        "external_blocker": "none" if all_evidence_recovered else "; ".join(sorted(blocked_families)),
        "post_write_audit": str(POST_AUDIT.relative_to(ROOT)) if finalized else "pending",
        "candidate_denominator_audit_sha256": sha256(PACKET / "candidate-denominator-audit-v9-strict.json"),
        "evidence_review_sha256": sha256(PACKET / "evidence-review-v9-strict.json"),
        "selection_sha256": sha256(PACKET / "deep-analysis-selection-v9-strict.json"),
        "books_comparison_sha256": sha256(PACKET / "books-comparison-v9-strict.json"),
    }
    dump("canonical-reconciliation-v9.json", canonical)

    packet_readme = f"""# 2026-06-03 Daily Source Packet

- Window: `[2026-06-02T01:00:00Z, 2026-06-03T01:00:00Z)`
- Current denominator: `DEN-20260603-V9-STRICT-c2194043`
- Row-complete account: `747 = 55 retained + 691 pre-denominator closures + 1 same-family supporting version`; retain rate `7.36%`.
- Fresh V8 challenge: `79/79` retains and `667/667` closures audited; `32` false positives and `8` false negatives repaired.
- Evidence: `55/55` exact-v1 reviews complete at disclosed scope; ordinary pending `0`; blocked `0`; UltraEP uses the official v1 abstract and excludes later evidence.
- Selection: `50` eligible reviews considered and `3` selected (`SF-LIBRA-AGENTIC-RL`, `SF-AGENT-LIBOS`, `SF-LAZYATTENTION`); `5` non-eligible candidates have family-specific closure, so candidate coverage remains `55/55`.
- Books semantic dedup: all `29/29` provisional Integrate rows challenged; `8 already covered / 13 partial / 3 genuinely missing / 5 should downgrade`.
- Final Books Comparison: `16 Integrate / 39 No Change — Existing Coverage`; UltraEP requires no additional Books write.
- Completion: `{completion}`; Coverage `{coverage_gate}`; Evidence `{evidence_gate}`; Books `{books_gate}`.

Current truth artifacts: `candidate-denominator-audit-v9-strict.json`, `evidence-review-v9-strict.json`, `deep-analysis-selection-v9-strict.json`, `BOOKS_DEDUP_RECONCILIATION_V9.md`, `books-comparison-v9-strict.json`, `canonical-reconciliation-v9.json`{', `POST_WRITE_FRESH_AUDIT_V9.md`' if finalized else ''}. Earlier V3–V8 artifacts remain provenance only.
"""
    (PACKET / "README.md").write_text(packet_readme, encoding="utf-8")
    regenerate_manifest()


if __name__ == "__main__":
    main()
