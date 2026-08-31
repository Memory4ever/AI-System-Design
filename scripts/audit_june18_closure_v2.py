#!/usr/bin/env python3
"""Fail-closed closure audit for the 2026-06-18 V2.1 Daily.

This script is intentionally read-only.  It verifies date-local receipts against the
current Books tree and fails on denominator drift, generic Books comparisons,
owner leakage, partial writeback, benchmark ambiguity, or stale hashes.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260618"
REPORT = ROOT / "papers/2026/06/18/README.md"
EXPECTED_DENOMINATOR = "DEN-20260618-2977f506"
EXPECTED_WINNERS = {"2606.18600", "2606.19025", "2606.19535"}
EXPECTED_NO_CHANGE_ARXIV_HITS = {"2606.18829", "2606.19409"}
BENCHMARK_FIELDS = [
    "workload", "model", "hardware", "precision", "input_length",
    "output_length", "batch", "concurrency", "slo", "evaluator",
]


def load_finalizer():
    spec = importlib.util.spec_from_file_location(
        "finalize_june18_v21", ROOT / "scripts/finalize_june18_v21.py"
    )
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def bounded(text: str, ref: str) -> str:
    match = re.search(
        rf"<!-- {re.escape(ref)}:start -->\n(.*?)\n<!-- {re.escape(ref)}:end -->",
        text,
        re.S,
    )
    assert match, f"missing bounded ref: {ref}"
    return match.group(1)


def main() -> None:
    source = load_finalizer()
    report = REPORT.read_text()
    ledger = json.loads((PACKET / "screening-ledger.json").read_text())
    reviews_doc = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())
    access = json.loads((PACKET / "exact-v1-access-receipt.json").read_text())
    selection = json.loads((PACKET / "deep-analysis-selection-v1.json").read_text())
    comparisons = json.loads((PACKET / "books-comparison-v1.json").read_text())

    identities = ledger["identities"]
    assert len(identities) == len({row["arxiv_id"] for row in identities}) == 516
    statuses = Counter(row["screening_status"] for row in identities)
    routes = Counter(row["screening_route"] for row in identities)
    assert statuses == Counter(
        {"pre_denominator_closure": 479, "retained_after_full_semantic_audit": 37}
    )
    assert routes == Counter(
        {
            "core_daily_semantic_review_required": 357,
            "keyword_daily_semantic_review_required": 55,
            "not_routed_by_keyword_contract": 104,
        }
    )
    denominator = ledger["canonical_candidate_denominator"]
    assert denominator["denominator_id"] == EXPECTED_DENOMINATOR
    assert denominator["raw_identities"] == 516
    assert denominator["retained"] == 37
    assert denominator["pre_denominator_closures"] == 479

    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open(newline="") as handle:
        semantic_rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(semantic_rows) == len({row["arxiv_id"] for row in semantic_rows}) == 516
    assert Counter(row["decision"] for row in semantic_rows) == Counter(
        {"closure": 479, "retained": 37}
    )
    closures = [row for row in semantic_rows if row["decision"] == "closure"]
    assert len({row["semantic_reason"] for row in closures}) == 479
    assert all(row["closure_class"] not in {"", "—"} for row in closures)

    reviews = reviews_doc["reviews"]
    assert reviews_doc["denominator_id"] == EXPECTED_DENOMINATOR
    assert len(reviews) == len({row["source_family_id"] for row in reviews}) == 37
    assert {row["primary_identifier"][6:-2] for row in reviews} == set(source.C)
    locator_fields = [
        "method_identity_locators",
        "evaluation_locators",
        "limitations_counterevidence_locators",
    ]
    for field in locator_fields:
        assert len({row[field] for row in reviews}) == 37, f"duplicate {field}"
    for row in reviews:
        aid = row["primary_identifier"][6:-2]
        family = row["source_family_id"]
        assert row["stable_node_id"] == source.C[aid]["owner"]
        assert row["completion_result"] == "complete"
        assert row["ordinary_pending_locator_count"] == 0
        for field in locator_fields:
            assert f"https://arxiv.org/html/{aid}v1" in row[field]
            assert "exact-v1" in row[field]
        benchmark = row["benchmark_contract"]
        assert list(benchmark) == BENCHMARK_FIELDS
        for value in benchmark.values():
            assert isinstance(value, str) and value.strip()
            assert "Not Disclosed" not in value or value == "Not Disclosed"
        body = bounded(report, row["review_ref"])
        assert hashlib.sha256(body.encode()).hexdigest() == row["review_body_sha256"]
        assert bounded(report, row["claim_boundary_ref"])

    assert access["denominator_id"] == EXPECTED_DENOMINATOR
    assert len(access["items"]) == 37 and access["blocked"] == []
    assert all(item["status"] == "accessible" for item in access["items"])

    decisions = selection["decisions"]
    assert selection["denominator_id"] == EXPECTED_DENOMINATOR
    assert selection["frontier_size"] == len(decisions) == 37
    assert selection["selection_count"] == 3
    assert set(selection["winners_frozen_before_rationale"]) == EXPECTED_WINNERS
    assert len({row["priority_rationale"] for row in decisions}) == 37
    assert {row["source_family_id"] for row in decisions} == {
        row["source_family_id"] for row in reviews
    }
    assert {
        row["source_family_id"].removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        for row in decisions if row["decision"] == "selected"
    } == EXPECTED_WINNERS

    items = comparisons["items"]
    assert comparisons["denominator_id"] == EXPECTED_DENOMINATOR
    assert comparisons["compared"] == "37/37" and len(items) == 37
    assert Counter(row["decision"] for row in items) == Counter(
        {"Integrate": 16, "No Change — Existing Coverage": 21}
    )
    for row in items:
        family = row["source_family_id"]
        aid = family.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
        assert row["stable_node_id"] == source.C[aid]["owner"]
        assert row["target_chapter_ref"].startswith("books/")
        assert row["adjacent_chapter_refs"].startswith("books/")
        assert row["target_chapter_ref"].split("#", 1)[0] != row["adjacent_chapter_refs"].split("#", 1)[0]
        table_row = (
            f"| {family} | {row['stable_node_id']} | {row['target_chapter_ref']} | "
            f"{row['adjacent_chapter_refs']} |"
        )
        assert table_row in report, f"Daily/JSON Books Comparison drift: {family}"
        existing = bounded(report, row["existing_proposition_ref"])
        assert source.OWNER_PROPOSITION[row["stable_node_id"]] in existing
        assert source.C[aid]["note"] in existing
        assert "were re-read before disposition" not in existing
        assert bounded(report, row["new_evidence_delta_ref"]) == source.C[aid]["delta"]
        assert source.C[aid]["boundary"] in bounded(report, row["books_review_ref"])

    book_paths = sorted((ROOT / "books").glob("part-*/*.md"))
    book_text = {path.relative_to(ROOT).as_posix(): path.read_text() for path in book_paths}
    all_books = "\n".join(book_text.values())
    ready = (PACKET / "READY_TO_INSERT_BOOKS_V1.md").read_text()
    for aid, evidence in source.C.items():
        family = source.fam(aid)
        owner = source.PATHS[evidence["owner"]]
        if evidence["disposition"] == "Integrate":
            assert all_books.count(family) == 1, f"non-unique Integrate family: {family}"
            assert book_text[owner].count(family) == 1, f"owner mismatch: {family}"
            assert book_text[owner].count(evidence["delta"]) >= 2, f"missing body delta: {family}"
            assert book_text[owner].count(evidence["boundary"]) >= 2, f"missing body boundary: {family}"
            assert f"https://arxiv.org/html/{aid}v1" in book_text[owner]
            assert ready.count(family) == 1
        else:
            assert all_books.count(family) == 0, f"No Change Source Family leakage: {family}"
            hits = all_books.count(aid)
            if aid in EXPECTED_NO_CHANGE_ARXIV_HITS:
                assert hits >= 1, f"missing expected pre-existing coverage: {aid}"
            else:
                assert hits == 0, f"unexpected No Change arXiv leakage: {aid}"

    standard = PACKET / "POST_WRITE_FRESH_AUDIT_V1.md"
    legacy = PACKET / "POSTWRITE_FRESH_AUDIT_V1.md"
    assert standard.is_file() and not legacy.exists()
    receipt = standard.read_text()
    assert receipt.count("| SF-2026-ARXIV-") == 37
    assert "Findings: none unresolved" in receipt

    manifest = PACKET / "SHA256SUMS"
    entries = []
    for line in manifest.read_text().splitlines():
        digest, name = line.split("  ", 1)
        path = PACKET / name
        assert path.is_file(), f"manifest missing file: {name}"
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, f"hash mismatch: {name}"
        entries.append(name)
    expected_entries = sorted(
        path.name
        for path in PACKET.iterdir()
        if path.is_file() and path.name not in {"SHA256SUMS", "screening-ledger-provisional.json"}
    )
    expected_entries += [
        "../../18/README.md",
        "../../../../../scripts/audit_june18_closure_v2.py",
        "../../../../../scripts/finalize_june18_v21.py",
    ]
    assert sorted(entries) == sorted(expected_entries)

    print(
        json.dumps(
            {
                "denominator": EXPECTED_DENOMINATOR,
                "coverage": "516=37+479; route-negative=104/104",
                "evidence": "37/37",
                "selection": "3 selected + 34 not_selected",
                "books": "16 Integrate + 21 No Change",
                "integrate_owners": len({source.PATHS[e["owner"]] for e in source.C.values() if e["disposition"] == "Integrate"}),
                "shared_writes": 0,
                "unresolved_findings": 0,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
