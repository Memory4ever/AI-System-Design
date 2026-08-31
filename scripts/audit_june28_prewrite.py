#!/usr/bin/env python3
"""Fail-closed pre-write audit for the strict 2026-06-28 Daily packet."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260628"
REPORT = ROOT / "papers/2026/06/28/README.md"
LEDGER = PACKET / "screening-ledger.json"
ND = "Not Disclosed"

INTEGRATE_IDS = {
    "2606.28690", "2606.28772", "2606.28955", "2606.28995", "2606.29038",
    "2606.29066",
}
HIGHLIGHT_NO_CHANGE = {
    "2606.28679", "2606.28862", "2606.28876", "2606.28925", "2606.28958", "2606.28962",
    "2606.29054", "2606.29073", "2606.29094", "2606.29124",
}
OWNER_FILES = {
    "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
    "books/part-04-training-system/27-data.md",
    "books/part-04-training-system/31-rlhf.md",
    "books/part-05-inference-system/44-decode.md",
    "books/part-06-ai-infrastructure/66-evaluation-system.md",
    "books/part-07-agent/83-mcp.md",
}


def load(name: str):
    return json.loads((PACKET / name).read_text())


def aid(family: str) -> str:
    return family.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)


def main() -> None:
    ledger = json.loads(LEDGER.read_text())
    access = load("exact-v1-access-receipt.json")
    reviews = load("source-review-receipts-v2.1.json")
    benchmark = load("exact-v1-benchmark-evidence-v2.json")
    selection = load("deep-analysis-selection-v1.json")
    comparisons = load("books-comparison-v1.json")
    ready = (PACKET / "READY_TO_INSERT_BOOKS_V1.md").read_text()
    queue = (PACKET / "BOOKS_INTEGRATION_QUEUE_V1.md").read_text()
    prewrite = (PACKET / "PREWRITE_FRESH_AUDIT_V1.md").read_text()
    report = REPORT.read_text()
    working = (PACKET / "EVIDENCE_REVIEW_WORKING_V1.md").read_text()

    assert ledger["denominator_id"] == "daily-v2.1:2026-06-28:20c51e943aacc58d"
    assert ledger["registered_window_identities"] == 211
    statuses = Counter(row["semantic_screen_status"] for row in ledger["identities"])
    assert statuses["retained_for_exact_v1_review"] == 65
    assert sum(value for key, value in statuses.items() if key != "retained_for_exact_v1_review") == 146

    assert len(access) == len(reviews) == len(benchmark) == len(selection) == 65
    families = [row["source_family_id"] for row in reviews]
    assert len(set(families)) == 65
    assert {row["source_family_id"] for row in access} == set(families)
    assert {row["source_family_id"] for row in benchmark} == set(families)
    assert {row["source_family_id"] for row in selection} == set(families)

    locator_triples = set()
    for row in reviews:
        family = row["source_family_id"]
        arxiv_id = aid(family)
        assert row["primary_evidence_version"] == f"arXiv:{arxiv_id}v1"
        locators = (row["method_locator"], row["evaluation_locator"], row["limitations_locator"])
        assert all("v1" in value and " — §" in value for value in locators)
        if arxiv_id == "2606.29108":
            assert all(value.startswith("arXiv:2606.29108v1 version-stamped mirror") for value in locators)
        else:
            assert all(value.startswith(f"https://arxiv.org/html/{arxiv_id}v1") for value in locators)
        assert locators not in locator_triples
        locator_triples.add(locators)
        assert len(row["problem"]) >= 80
        method_fact = row["method_locator"].split(" — §", 1)[1]
        assert len(row["mechanism"]) >= 120 and method_fact in row["mechanism"]
        assert len(row["evaluation_proof"]) >= 100
        assert len(row["non_proof"]) >= 80

        contract = row["benchmark_contract"]
        assert tuple(contract) == (
            "workload", "model", "hardware", "precision", "input_length", "output_length",
            "batch", "concurrency", "slo", "evaluator",
        )
        assert contract["workload"] != contract["evaluator"]
        assert "exact-v1 evaluation scope:" in contract["workload"]
        assert contract["evaluator"].startswith("Exact-v1 evaluator/metric evidence:")
        for value in contract.values():
            assert value == ND or "Not Disclosed" not in value
            assert not re.search(r"\b(?:otherwise|unless|if not)\s+Not Disclosed\b", value, re.I)
            assert len(value) <= 900

    access_by_id = {aid(row["source_family_id"]): row for row in access}
    assert sum(row["recovery_route"] == "official_exact_v1_html" for row in access) == 64
    mirror = access_by_id["2606.29108"]
    assert mirror["access_status"] == "accessible"
    assert mirror["official_exact_v1_url"] == ND
    assert mirror["recovery_route"] == "version_stamped_mirror_crosscheck"
    assert "Every row below was opened from the official" not in working
    assert "64 official HTML" in report and "version-stamped" in report

    title = "Memory-Managed Long-Context Attention: A Preliminary Study of Editable Request-Local Memory"
    retained = {row["arxiv_id"]: row for row in ledger["identities"] if row["semantic_screen_status"] == "retained_for_exact_v1_review"}
    assert retained["2606.28876"]["title"] == title
    assert retained["2606.28876"]["stable_node_id"] == "MODEL-LONG-CONTEXT"
    assert "require reconciliation before Evidence Gate" not in working + report + ready + queue

    decisions = Counter(row["decision"] for row in selection)
    assert decisions == {"selected": 3, "subsumed": 2, "not_selected": 60}
    selected_units = {row["analysis_unit_id"] for row in selection if row["decision"] == "selected"}
    assert len(selected_units) == 3
    for row in selection:
        assert row["eligibility"] != "eligible"
        assert len(row["priority_rationale"]) >= 180
        assert row["source_family_id"] in row["narrative_ref"] or row["decision"] != "not_selected"
        if row["decision"] == "subsumed":
            assert row["subsumed_by"] in selected_units
        if row["decision"] == "not_selected":
            assert "exact-v1 non-proof" in row["priority_rationale"]
    assert len({row["priority_rationale"] for row in selection}) == 65

    dispositions = Counter(row["books_disposition"] for row in reviews)
    assert dispositions == {
        "Integrate": 6,
        "No Change — Existing Coverage": 42,
        "Weekly Only — Context": 17,
    }
    by_id = {aid(row["source_family_id"]): row for row in reviews}
    assert {arxiv_id for arxiv_id, row in by_id.items() if row["books_disposition"] == "Integrate"} == INTEGRATE_IDS
    assert all(by_id[arxiv_id]["books_disposition"] == "No Change — Existing Coverage" for arxiv_id in HIGHLIGHT_NO_CHANGE)
    assert by_id["2606.29126"]["books_disposition"] == "Weekly Only — Context"
    assert len(comparisons) == 48
    for row in comparisons:
        assert row["decision"] in {"Integrate", "No Change — Existing Coverage"}
        assert re.search(r"books/.+\.md#L\d+ — #+ ", row["target_chapter_ref"])
        assert len(row["adjacent_chapter_refs"]) == 1
        assert re.search(r"books/.+\.md#L\d+ — ## ", row["adjacent_chapter_refs"][0])
        assert len(row["existing_proposition"]) >= 100
        assert len(row["new_evidence_delta"]) >= 100

    assert ready.count("### Owner-merged minimal durable delta") == 6
    assert ready.count("### Source-specific exact-v1 Review notes") == 6
    assert ready.count("primary arXiv:") == 6
    assert ready.count("exact-v1 URL=https://arxiv.org/html/") == 6
    assert ready.count("; Method=https://arxiv.org/html/") == 6
    assert ready.count("; Evaluation=https://arxiv.org/html/") == 6
    assert ready.count("; Non-proof=https://arxiv.org/html/") == 6
    assert all(path in ready and path in queue for path in OWNER_FILES)
    bodies = re.findall(
        r"### Owner-merged minimal durable delta\n\n(.+?)\n\n### Trade-off、failure、fallback 与 coexistence",
        ready,
        re.S,
    )
    assert len(bodies) == len(set(bodies)) == 6
    assert all("SF-2026-ARXIV" not in body and "arXiv:" not in body for body in bodies)
    assert all(not re.search(r"\b(?:outperform|achiev(?:e|es|ed)|improv(?:e|es|ed))\b", body, re.I) for body in bodies)

    assert prewrite.count("| SF-2026-ARXIV-") == 65
    assert prewrite.count("| PASS |") >= 65
    assert "6 Integrate" in prewrite and "42 No Change" in prewrite and "17 Weekly Only" in prewrite
    assert "Findings: zero unresolved" in prewrite
    assert "| Evidence Gate | Passed |" in report
    assert "| Books Gate | Open |" in report
    assert "| Completion Status | In Progress |" in report
    assert "SA-20260628-EVIDENCE-V1" in report and "| passed |" in report

    ready_digest = hashlib.sha256(ready.encode()).hexdigest()
    print(json.dumps({
        "denominator": "211=65+146",
        "exact_v1": "65/65",
        "locator_triples": len(locator_triples),
        "selection": dict(decisions),
        "books": dict(dispositions),
        "owner_blocks": 6,
        "ready_sha256": ready_digest,
        "result": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
