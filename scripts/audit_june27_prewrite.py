#!/usr/bin/env python3
"""Fail-closed semantic/interface checks for the 2026-06-27 pre-write packet."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260627"
REPORT = ROOT / "papers/2026/06/27/README.md"
ND = "Not Disclosed"


def load(name: str):
    return json.loads((PACKET / name).read_text())


def main() -> None:
    evidence = load("exact-v1-evidence-facts.json")
    access = load("exact-v1-access-receipt.json")
    reviews = load("source-review-receipts-v2.1.json")
    selection = load("deep-analysis-selection-v1.json")
    comparisons = load("books-comparison-v1.json")
    ready = (PACKET / "READY_TO_INSERT_BOOKS_V1.md").read_text()
    prewrite = (PACKET / "PREWRITE_FRESH_AUDIT_V1.md").read_text()
    report = REPORT.read_text()

    assert evidence["resolved"] == 64 and evidence["blocked"] == 0
    assert len(access) == len(reviews) == len(selection) == 64
    families = [x["source_family_id"] for x in reviews]
    assert len(set(families)) == 64
    triples = set()
    for item in reviews:
        assert item["primary_evidence_version"].endswith("v1")
        locators = (item["method_locator"], item["evaluation_locator"], item["limitations_locator"])
        pdf_id = item["source_family_id"].removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        if pdf_id in {"2606.28455", "2606.28574", "2606.28639"}:
            assert all(f"https://arxiv.org/pdf/{pdf_id}v1" in value and "v1 — §" in value for value in locators)
            if pdf_id == "2606.28455":
                assert "3 Problem formulation" in item["method_locator"]
                assert "6 Main results" in item["evaluation_locator"]
                assert "7.2 Scope and limitations" in item["limitations_locator"]
        else:
            assert all("https://arxiv.org/html/" in value and "v1 — §" in value for value in locators)
        assert item["method_locator"] != item["evaluation_locator"]
        assert locators not in triples
        triples.add(locators)
        benchmark = item["benchmark_contract"]
        assert tuple(benchmark) == (
            "workload", "model", "hardware", "precision", "input_length", "output_length",
            "batch", "concurrency", "slo", "evaluator",
        )
        for value in benchmark.values():
            assert value == ND or "Not Disclosed" not in value
            assert "Cited by:" not in value
            assert value not in {"Benchmarks.", "Evaluation Metrics.", "GPU selection.", "3 Evaluation 3.1 Experimental Setup Models."}
            assert not value.rstrip().endswith(("Sec.", "vs.", "i.e."))
            assert len(value) <= 700

    decisions = [x["decision"] for x in selection]
    assert decisions.count("selected") == 3
    assert decisions.count("subsumed") == 2
    assert decisions.count("not_selected") == 59
    rationales = [x["priority_rationale"] for x in selection]
    assert len(set(rationales)) == 64
    assert all(len(value) >= 140 for value in rationales)
    assert all("Exact-v1 non-proof" in value for value, decision in zip(rationales, decisions) if decision == "not_selected")

    dispositions = [x["books_disposition"] for x in reviews]
    assert dispositions.count("Integrate") == 14
    assert dispositions.count("No Change — Existing Coverage") == 47
    assert dispositions.count("Weekly Only — Context") == 3
    assert len(comparisons) == 61
    assert {x["decision"] for x in comparisons} == {"Integrate", "No Change — Existing Coverage"}
    assert all(x["target_chapter_ref"].startswith("books/") for x in comparisons)
    assert all(x["adjacent_chapter_refs"] and x["adjacent_chapter_refs"][0].startswith("books/") for x in comparisons)
    assert all(len(x["existing_proposition"]) >= 100 for x in comparisons)

    assert ready.count("### Owner-merged minimal durable delta") == 11
    assert ready.count("### Source-specific exact-v1 Review notes") == 11
    assert ready.count("primary arXiv:") == 14
    assert ready.count("exact-v1 URL=https://arxiv.org/html/") == 14
    assert ready.count("; Method=https://arxiv.org/html/") == 14
    assert ready.count("; Evaluation=https://arxiv.org/html/") == 14
    assert ready.count("; Non-proof=https://arxiv.org/html/") == 14
    assert not re.search(r"^- \*\*SF-2026-ARXIV-", ready, re.M)
    bodies = re.findall(
        r"### Owner-merged minimal durable delta\n\n(.+?)\n\n### Trade-off、failure、fallback 与 coexistence",
        ready,
        re.S,
    )
    assert len(bodies) == len(set(bodies)) == 11
    assert all("SF-2026-ARXIV" not in body and "arXiv:" not in body for body in bodies)
    assert all(not re.search(r"\b(?:outperform|achiev(?:e|es|ed)|improv(?:e|es|ed))\b", body, re.I) for body in bodies)
    assert prewrite.count("| SF-2026-ARXIV-") == 64
    assert prewrite.count("| PASS |") >= 64
    assert "14 Integrate" in prewrite and "47 No Change" in prewrite and "3 Weekly Only" in prewrite
    assert "Findings: zero unresolved" in prewrite

    assert "| Evidence Gate | Passed |" in report
    assert "| Books Gate | Open |" in report
    assert "| Completion Status | In Progress |" in report
    assert "SA-20260627-EVIDENCE-V1" in report and "| passed |" in report
    digest = hashlib.sha256(ready.encode()).hexdigest()
    print(json.dumps({
        "families": 64, "locator_triples": len(triples), "selection": {"selected": 3, "subsumed": 2, "not_selected": 59},
        "books": {"integrate": 14, "no_change": 47, "weekly_only": 3, "owner_blocks": 11},
        "ready_sha256": digest, "result": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
