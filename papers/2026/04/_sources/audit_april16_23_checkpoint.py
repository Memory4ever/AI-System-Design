#!/usr/bin/env python3
"""Fail-closed invariants for the 2026-04-16..23 Historical Daily checkpoint."""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
DAYS = range(16, 24)
EXPECTED = {
    16: (1082, 40, 1042, 0),
    17: (1059, 34, 1025, 0),
    18: (944, 28, 916, 0),
    19: (441, 20, 421, 1),
    20: (530, 29, 501, 0),
    21: (1223, 39, 1184, 2),
    22: (1085, 29, 1056, 0),
    23: (1053, 43, 1010, 2),
}
EXPECTED_QUEUE = {
    "SF-2026-ARXIV-2604-17180",
    "SF-2026-ARXIV-2604-17861",
    "SF-2026-ARXIV-2604-18529",
    "SF-2026-ARXIV-2604-20452",
    "SF-2026-ARXIV-2604-21072",
}
WITHDRAWN = {"2604.17238", "2604.18128", "2604.18170"}
WEEKLY_SEMANTIC_PATTERNS = (
    "papers/2026/weekly",
    "WEEKLY_REVIEW_PATHS",
    "weekly_review",
    "Weekly seed",
    "Weekly Review reuse",
    "prior Weekly",
    "weekly-derived",
    "W15 packets",
    "W16 packets",
)


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_h2(ref: str) -> None:
    match = re.fullmatch(r"(.+\.md)#L(\d+) \(H2: (.+)\)", ref)
    assert match, f"non-canonical Books ref: {ref}"
    path = ROOT / match.group(1)
    line_no = int(match.group(2))
    title = match.group(3)
    lines = path.read_text(encoding="utf-8").splitlines()
    assert 1 <= line_no <= len(lines), f"out-of-range Books ref: {ref}"
    assert lines[line_no - 1] == f"## {title}", f"stale Books H2 ref: {ref}"
    review_notes = next(
        (index for index, line in enumerate(lines, 1) if line == "## Review notes"),
        len(lines) + 1,
    )
    assert line_no < review_notes, f"Books ref is after Review notes: {ref}"


def candidate_rows(readme: str) -> list[list[str]]:
    header = "| Source Family ID | Primary Identifier | Event Identity | Owner Week |"
    start = readme.index(header)
    block = readme[start:].split("\n\n", 1)[0]
    rows = []
    for line in block.splitlines()[2:]:
        if not line.startswith("| SF-"):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def main() -> None:
    queue_ids: set[str] = set()
    totals = Counter()
    score_totals = Counter()
    all_semantic_text: list[str] = []

    for day in DAYS:
        local = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
        readme_path = ROOT / f"papers/2026/04/{day:02d}/README.md"
        readme = readme_path.read_text(encoding="utf-8")
        ledger = load(local / "screening-ledger-final.json")
        reviews = load(local / "exact-v1-review-packet.json")["items"]
        comparison = load(local / "books-current-content-comparison.json")["items"]
        queue = load(local / "BOOKS_WRITEBACK_QUEUE.json")["items"]
        section_rows = load(local / "exact-v1-section-index.json")["rows"]

        candidates = [
            item for item in ledger["identities"]
            if item["screening_status"] == "candidate_denominator"
        ]
        closures = [
            item for item in ledger["identities"]
            if item["screening_status"] != "candidate_denominator"
        ]
        raw, retained, closed, queued = EXPECTED[day]
        observed = (
            ledger["registered_window_identities"],
            len(candidates),
            len(closures),
            len(queue),
        )
        assert observed == EXPECTED[day], f"04-{day:02d} counts {observed} != {EXPECTED[day]}"
        assert ledger["screened_identities"] == raw
        assert ledger["candidate_denominator"] == retained
        assert ledger["pre_denominator_closures"] == closed

        candidate_ids = {item["source_family_id"] for item in candidates}
        closure_ids = {item["source_family_id"] for item in closures}
        review_ids = {item["source_family_id"] for item in reviews}
        comparison_ids = {item["source_family_id"] for item in comparison}
        assert len(candidate_ids) == retained
        assert len(closure_ids) == closed
        assert not candidate_ids & closure_ids
        assert review_ids == candidate_ids
        assert comparison_ids == candidate_ids

        exact_by_arxiv = {row["arxiv_id"]: row for row in section_rows if not row["withdrawn"]}
        for review in reviews:
            arxiv_id = review["primary_version"].removeprefix("arXiv:").removesuffix("v1")
            exact = exact_by_arxiv[arxiv_id]
            locators = [
                exact["method"]["locator"],
                exact["evaluation"]["locator"],
                exact["limitations"]["locator"],
            ]
            assert all(locator and "Instructions for reporting errors" not in locator for locator in locators)
            assert len(set(locators)) == 3, f"reused deep locator: {review['source_family_id']}"
            assert review["review_status"] == "deep_complete"
            assert review["access_status"] == "accessible"

        table_rows = candidate_rows(readme)
        assert len(table_rows) == retained
        for row in table_rows:
            assert len(row) == 22, f"04-{day:02d} candidate row has {len(row)} cells"
            total = int(row[9])
            assert total == int(row[6]) + int(row[7]) + int(row[8])
            score_totals[total] += 1

        deep_block = readme.split("## 5. Deep Analysis Selection", 1)[1].split("\n## 6.", 1)[0]
        assert len(re.findall(r"^### ", deep_block, flags=re.MULTILINE)) <= 3

        for item in comparison:
            resolve_h2(item["target_ref"])
            for ref in item["adjacent_refs"]:
                resolve_h2(ref)
        for item in queue:
            assert item["disposition"] == "Integrate"
            assert item["status"] == "waiting_for_root_serial_writeback"
            resolve_h2(item["target_ref"])
            queue_ids.add(item["source_family_id"])

        payload_paths = [readme_path] + [
            path
            for path in local.iterdir()
            if path.is_file() and path.suffix in {".json", ".md", ".tsv"}
        ]
        for path in payload_paths:
            text = path.read_text(encoding="utf-8", errors="replace")
            all_semantic_text.append(text)
            for pattern in WEEKLY_SEMANTIC_PATTERNS:
                assert pattern not in text, f"Weekly semantic dependency {pattern!r} in {path}"

        totals.update(raw=raw, retained=retained, closures=closed, exact=len(reviews), queue=queued)

    semantic_text = "\n".join(all_semantic_text)
    for arxiv_id in WITHDRAWN:
        family = f"SF-2026-ARXIV-{arxiv_id}"
        assert family not in queue_ids
        # A withdrawn family may remain only in a screening closure/withdrawal receipt.
        for day in DAYS:
            local = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
            for name in ("exact-v1-review-packet.json", "books-current-content-comparison.json", "BOOKS_WRITEBACK_QUEUE.json"):
                assert family not in (local / name).read_text(encoding="utf-8")

    assert queue_ids == EXPECTED_QUEUE
    assert totals == Counter(raw=7417, retained=262, closures=7155, exact=262, queue=5)
    assert set(score_totals).issubset({7, 8, 9}) and len(score_totals) >= 2
    print(json.dumps({"totals": totals, "scores": score_totals, "queue": sorted(queue_ids)}, ensure_ascii=False, default=dict))


if __name__ == "__main__":
    main()
