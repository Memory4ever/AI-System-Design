#!/usr/bin/env python3
"""Fail-closed acceptance audit for the corrected 2026-06-05 contract."""

from __future__ import annotations

import hashlib
import importlib.util
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/05/README.md"
PACKET = ROOT / "papers/2026/06/_sources/daily-20260605"
NON_BENCHMARK = {
    "SF-2026-ARXIV-2606-05946",
    "SF-2026-ARXIV-2606-06556",
    "SF-2026-ARXIV-2606-06697",
    "SF-2026-ARXIV-2606-06708",
}
CANONICAL_H2 = [
    "## Executive Summary",
    *[f"## {number}. {title}" for number, title in enumerate(
        (
            "Coverage", "Candidate Ledger", "Review Completion Receipt",
            "Benchmark Contracts", "Deep Analysis Selection", "Books Comparison",
            "Semantic Audit", "Ignored Noise", "Recommended Action",
            "Repository Changes", "Open Questions", "Sources", "Final Status",
        ),
        1,
    )],
]


def load_validator():
    path = ROOT / "scripts/validate_research.py"
    spec = importlib.util.spec_from_file_location("june05_validator", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def clean(value: str) -> str:
    return value.strip().strip("`")


def parse_closure_table(text: str) -> list[dict[str, str]]:
    section = text.split("### Non-eligible family closures", 1)[1]
    lines = section.lstrip().splitlines()
    start = next(index for index, line in enumerate(lines) if line.startswith("| Source Family ID |"))
    header = [cell.strip() for cell in lines[start].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in lines[start + 2 :]:
        if not line.startswith("|"):
            break
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        assert len(cells) == len(header), line
        rows.append(dict(zip(header, cells)))
    return rows


def verify_manifest() -> int:
    rows = (PACKET / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
    for row in rows:
        digest, relative = row.split(maxsplit=1)
        path = ROOT / relative
        assert path.exists(), relative
        assert hashlib.sha256(path.read_bytes()).hexdigest() == digest, relative
    return len(rows)


def main() -> None:
    validator = load_validator()
    text = REPORT.read_text(encoding="utf-8")
    table = lambda marker: validator._table_after_marker(text, marker)[0]
    candidates = table("<!-- validator:candidate-ledger-v2.1 -->")
    reviews = table("<!-- validator:review-completion-v1 -->")
    benchmarks = table("<!-- validator:benchmark-contract-v1 -->")
    selections = table("<!-- validator:deep-analysis-selection-v1 -->")
    books = table("<!-- validator:books-comparison-v1 -->")

    candidate_ids = {clean(row["Source Family ID"]) for row in candidates}
    review_ids = {clean(row["Source Family ID"]) for row in reviews}
    selection_ids = {clean(row["Source Family ID"]) for row in selections}
    books_ids = {clean(row["Source Family ID"]) for row in books}
    yes_ids = {clean(row["Source Family ID"]) for row in candidates if clean(row["Benchmark Claim"]) == "yes"}
    no_ids = {clean(row["Source Family ID"]) for row in candidates if clean(row["Benchmark Claim"]) == "no"}
    benchmark_ids = {clean(row["Source Family ID"]) for row in benchmarks}

    assert len(candidates) == len(reviews) == len(books) == 64
    assert candidate_ids == review_ids == books_ids
    assert {clean(row["Access Status"]) for row in candidates} == {"accessible"}
    assert {clean(row["Review Status"]) for row in candidates} == {"deep_complete", "standard_complete"}
    assert {clean(row["Completion Result"]) for row in reviews} == {"complete"}
    assert len({clean(row["Review Provenance ID"]) for row in reviews}) == 64
    assert len(yes_ids) == len(benchmark_ids) == 60 and yes_ids == benchmark_ids
    assert no_ids == NON_BENCHMARK and not (no_ids & benchmark_ids)
    assert len(selections) == len(selection_ids) == 33
    assert Counter(clean(row["Decision"]) for row in selections) == {"selected": 3, "not_selected": 30}
    assert Counter(clean(row["Decision"]) for row in books) == {
        "Integrate": 8,
        "No Change — Existing Coverage": 56,
    }

    closures = parse_closure_table(text)
    closure_ids = {clean(row["Source Family ID"]) for row in closures}
    assert len(closures) == len(closure_ids) == 31
    assert selection_ids.isdisjoint(closure_ids)
    assert selection_ids | closure_ids == candidate_ids
    assert {clean(row["Disposition"]) for row in closures} == {"non_eligible_closure"}
    for row in closures:
        family = clean(row["Source Family ID"])
        ref = clean(row["Closure Ref"])
        assert ref == f"selection-closure:{family}"
        assert text.count(f"<!-- {ref}:start -->") == text.count(f"<!-- {ref}:end -->") == 1
        body = text.split(f"<!-- {ref}:start -->", 1)[1].split(f"<!-- {ref}:end -->", 1)[0]
        assert "outside Deep Analysis Selection eligibility" in body
        assert "Source Review" in body and "Books Decision" in body

    forbidden = (
        "64/64 Selection frontier",
        "Deep Analysis Selection: `64/64`",
        "Selection frontier: `64/64`",
        "selection: `64/64`",
        '"selection_frontier_reviewed": 64',
        '"selection_reviewed": 64',
    )
    packet_text = "\n".join(
        path.read_text(encoding="utf-8")
        for path in (
            REPORT,
            PACKET / "README.md",
            PACKET / "downstream-repair-checkpoint-v1.md",
            PACKET / "fresh-downstream-adversarial-v3.md",
            PACKET / "source-review-receipts-v2.1.json",
            PACKET / "fresh-downstream-adversarial-v3.json",
        )
    )
    assert not [phrase for phrase in forbidden if phrase in packet_text]

    for family in candidate_ids:
        assert text.count(f"<!-- review:{family}:start -->") == 1
        assert text.count(f"<!-- review:{family}:end -->") == 1
    assert re.findall(r"(?m)^## .+$", text) == CANONICAL_H2
    assert all(field in text for field in ("**Research Date:**", "**Timezone:**", "**Strict Window:**", "**Contract:**", "**Status:**"))
    assert "2026-06-04 09:00:00 ～ 2026-06-05 09:00:00" in text
    postwrite = (PACKET / "POST_WRITE_FRESH_AUDIT_V1.md").read_text(encoding="utf-8")
    assert "Books proposals audited: `8/8`" in postwrite
    assert "concrete write locations: `9/9`" in postwrite
    assert "unresolved findings: `0`" in postwrite
    book_digests = re.findall(r"^- `([0-9a-f]{64})`  `([^`]+)`$", postwrite, re.M)
    assert len(book_digests) == 6
    for digest, relative in book_digests:
        assert hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == digest
    audits = table("<!-- validator:semantic-audit-v1 -->")
    assert len(audits) == 4 and {clean(row["Status"]) for row in audits} == {"passed"}
    for truth in (
        "| Completion Status | Complete |",
        "| Coverage Gate | Closed |",
        "| Evidence Gate | Passed |",
        "| Books Gate | Passed |",
    ):
        assert truth in text
    manifest_rows = verify_manifest()
    print(
        "PASS candidates=64 reviews=64 eligible_selection=33 noneligible_closures=31 "
        "benchmark_yes=60 benchmark_no=4 benchmark_rows=60 books=64 "
        f"manifest={manifest_rows} findings=0"
    )


if __name__ == "__main__":
    main()
