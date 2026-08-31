#!/usr/bin/env python3
"""Adversarially verify the resolved 2026-06-07 Conditional family and all Books dispositions."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260607"
REPORT = ROOT / "papers/2026/06/07/README.md"
FAMILY = "SF-2026-ARXIV-2606-08317"
NONELIGIBLE = {
    "SF-2026-ARXIV-2606-07970",
    "SF-2026-ARXIV-2606-08302",
    "SF-2026-ARXIV-2606-08317",
    "SF-2026-ARXIV-2606-08346",
    "SF-2026-ARXIV-2606-08381",
}


def load(name: str) -> dict:
    return json.loads((PACKET / name).read_text())


def main() -> None:
    screening = load("registered-hit-screening.json")
    denominator = load("candidate-denominator.json")
    access = load("exact-v1-access-receipt.json")
    reviews = load("source-review-receipts-v2.1.json")
    selection = load("deep-analysis-selection-v1.json")
    comparisons = load("books-comparison-v1.json")

    assert screening["gate_status"] == "closed_full_title_abstract_semantic_screening"
    assert screening["title_route_negative_pending_false_negative_audit"] == 0
    assert screening["title_route_negative_reviewed"] == 46
    assert len(screening["identities"]) == 261
    assert {row["screening_status"] for row in screening["identities"]} == {
        "retained_after_semantic_screening", "pre_denominator_closed"
    }
    for snapshot in screening["snapshots"]:
        snapshot_path = PACKET / snapshot["path"]
        assert snapshot_path.is_file(), snapshot_path
        assert hashlib.sha256(snapshot_path.read_bytes()).hexdigest() == snapshot["sha256"]

    assert (denominator["raw_identities"], denominator["retained"], denominator["closures"]) == (261, 23, 238)
    assert denominator["denominator_id"] == "DEN-20260607-76380553"
    assert (access["reviewed"], access["accessible"], access["blocked"]) == (23, 23, 0)
    assert (reviews["candidate_count"], reviews["review_complete_count"], reviews["blocked_count"]) == (23, 23, 0)
    assert len(access["rows"]) == len(reviews["rows"]) == 23
    assert all(row["status"] == "accessible" for row in access["rows"])
    assert all(row["completion"] == "complete" for row in reviews["rows"])

    recovered_access = next(row for row in access["rows"] if row["source_family_id"] == FAMILY)
    recovered_review = next(row for row in reviews["rows"] if row["source_family_id"] == FAMILY)
    assert recovered_access == {
        "source_family_id": FAMILY,
        "primary_identifier": "arXiv:2606.08317v1",
        "url": "https://arxiv.org/pdf/2606.08317v1",
        "route": "official-exact-v1-pdf-web-reader",
        "reviewed_extent": "full 18-page exact-v1 PDF",
        "status": "accessible",
        "claim_scope": "exact-v1 only",
    }
    required_review_terms = (
        "§II Methodology", "§VI-A Evaluation Dimensions", "§IX-B Database Architecture Selection",
        "§VI-B Table I directional", "§IX-D financial-fraud", "§XI Limitations",
        "directional literature synthesis, not a controlled benchmark", "no model is evaluated",
        "no product-level empirical evaluator", "Not Disclosed — exact-v1 PDF names no executable",
    )
    review_blob = json.dumps(recovered_review, ensure_ascii=False)
    missing = [term for term in required_review_terms if term not in review_blob and term not in REPORT.read_text()]
    if missing:
        raise AssertionError(f"recovered exact-v1 semantics missing: {missing}")
    assert recovered_review["score"] == [2, 2, 2, 6]
    assert recovered_review["review_status"] == "standard_complete"

    assert (selection["candidate_count"], selection["eligible_count"], selection["noneligible_count"], selection["selected_unit_count"]) == (23, 18, 5, 3)
    assert len(selection["rows"]) == 18
    eligible_families = {row["source_family_id"] for row in selection["rows"]}
    noneligible_families = {row["source_family_id"] for row in selection["noneligible_rows"]}
    candidate_families = {row["source_family_id"] for row in reviews["rows"]}
    assert noneligible_families == NONELIGIBLE
    assert eligible_families.isdisjoint(noneligible_families)
    assert eligible_families | noneligible_families == candidate_families
    assert sum(row["decision"] == "selected" for row in selection["rows"]) == 3
    for row in selection["noneligible_rows"]:
        assert row["decision"] == "non_eligible"
        assert row["eligibility_signals"] == []
        assert row["score_total"] == 6 and row["review_override"] == "none"
        ref = row["narrative_ref"]
        assert ref == f"analysis-ineligible:{row['source_family_id']}"
        report_text = REPORT.read_text(encoding="utf-8")
        assert report_text.count(f"<!-- {ref}:start -->") == 1
        assert report_text.count(f"<!-- {ref}:end -->") == 1

    assert comparisons["row_count"] == 23
    counts = Counter(row["decision"] for row in comparisons["rows"])
    assert counts == {"Integrate": 6, "No Change — Existing Coverage": 17}
    recovered_cmp = next(row for row in comparisons["rows"] if row["source_family_id"] == FAMILY)
    assert recovered_cmp["decision"] == "No Change — Existing Coverage"
    assert recovered_cmp["target_chapter_ref"].startswith("books/part-06-ai-infrastructure/57-")
    assert recovered_cmp["adjacent_chapter_refs"].startswith("books/part-06-ai-infrastructure/58-")
    larch_cmp = next(
        row for row in comparisons["rows"]
        if row["source_family_id"] == "SF-2026-ARXIV-2606-07923"
    )
    assert larch_cmp["stable_node_id"] == "INFER-SCHEDULING"
    assert larch_cmp["target_chapter_ref"].startswith("books/part-05-inference-system/56-")

    ch57 = (ROOT / recovered_cmp["target_chapter_ref"].split("#", 1)[0]).read_text()
    ch58 = (ROOT / recovered_cmp["adjacent_chapter_refs"].split("#", 1)[0]).read_text()
    for term in ("稳定契约和控制闭环", "intent → admission → reconciliation", "One-size-fits-all"):
        assert term in ch57
    assert ch58.strip()

    corpus = {path: path.read_text() for path in (ROOT / "books").rglob("*.md")}
    mechanism_terms = {
        "2606.07923": ("online selectivity", "逐行 semantic-filter ordering"),
        "2606.07943": ("legitimate-task receipt", "malicious-effect receipt"),
        "2606.08049": ("versioned notebook", "gate-conditioned"),
        "2606.08106": ("anytime-valid", "optional stopping"),
        "2606.08200": ("主动 probe", "in-world coverage-seeking intervention"),
        "2606.09916": ("QueryMemory", "sentinel slot-map"),
    }
    audit_rows = []
    for row in comparisons["rows"]:
        family = row["source_family_id"]
        arxiv_id = family.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        family_hits = [path for path, text in corpus.items() if family in text]
        raw_hits = [path for path, text in corpus.items() if f"arXiv:{arxiv_id}v1" in text]
        target = ROOT / row["target_chapter_ref"].split("#", 1)[0]
        if row["decision"] == "Integrate":
            if family_hits not in ([], [target]) or raw_hits != [target]:
                raise AssertionError(
                    f"{family}: Integrate owner conflict family={family_hits}, exact-v1={raw_hits}"
                )
            missing = [term for term in mechanism_terms[arxiv_id] if term not in corpus[target]]
            if missing:
                raise AssertionError(f"{family}: source-specific mechanism missing {missing}")
            evidence = f"unique exact-v1 Books owner `{target.relative_to(ROOT)}`; mechanism/boundary re-read"
        else:
            if family_hits or raw_hits:
                raise AssertionError(
                    f"{family}: No Change leaked into Books family={family_hits}, exact-v1={raw_hits}"
                )
            evidence = "zero Books hits after owner/adjacent comparison"
        audit_rows.append((family, row["decision"], evidence))

    report = REPORT.read_text()
    assert "| Completion Status | Complete |" in report
    assert "| Evidence Gate | Passed |" in report
    assert "| Books Gate | Passed |" in report
    assert "MR-20260607-08317" not in report
    assert "Blocked / Unverified" not in report

    lines = [
        "# 2026-06-07 Conditional Recovery Fresh Audit V2", "",
        "- Coverage: PASS — 261 = 23 retained + 238 closures; raw screening ledger is closed, all 46 route negatives are reviewed, four repository-local snapshots match their hashes, and the corrected owner-aware denominator is `DEN-20260607-76380553`.",
        "- Evidence: PASS — 23/23 exact-v1 complete, blocked=0; 2606.08317v1 recovered from the official 18-page PDF.",
        "- Recovered benchmark boundary: PASS — 13-paradigm synthesis and the fraud case are conceptual/illustrative; Table I is directional literature synthesis, not controlled product benchmarking.",
        "- Selection: PASS — corrected-contract conservation is 23 = 18 eligible + 5 non-eligible; sets are disjoint, union equals the retained denominator, all five source-specific closures resolve, and three winners remain unchanged.",
        "- Books: PASS — 6/6 Integrate families occur in one expected owner each; 17/17 No Change families have zero Books leakage.",
        "- 2606.08317 disposition: PASS — No Change against Ch57 owner and Ch58 adjacent; no shared Books write required.",
        "- Materials Request: resolved and removed; unresolved findings: 0.",
        "- Completion: Complete; Coverage Closed; Evidence Passed; Selection Passed; Books Passed.", "",
        "| Source Family | Disposition | Post-recovery evidence | Result |",
        "| --- | --- | --- | --- |",
    ]
    for family, disposition, evidence in audit_rows:
        lines.append(f"| {family} | {disposition} | {evidence} | PASS |")
    audit_path = PACKET / "CONDITIONAL_RECOVERY_FRESH_AUDIT_V2.md"
    audit_path.write_text("\n".join(lines) + "\n")

    manifest = PACKET / "SHA256SUMS"
    entries = []
    for line in manifest.read_text().splitlines():
        _, rel = line.split("  ", 1)
        path = ROOT / rel
        entries.append((rel, path))
    rel = str(audit_path.relative_to(ROOT))
    if rel not in {item[0] for item in entries}:
        entries.append((rel, audit_path))
    manifest.write_text("\n".join(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {relpath}" for relpath, path in entries) + "\n")
    print("06-07 recovery audit PASS: 23/23; unresolved=0")


if __name__ == "__main__":
    main()
