#!/usr/bin/env python3
"""Root acceptance audit for April 1-7 Historical Daily Books comparisons.

This audit is intentionally downstream of independently accepted Evidence.  It
does not modify Books or reinterpret Source Reviews.  It prevents placeholder
chapter references and semantically unverified queues from being released.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def markdown_heading_slug(heading: str) -> str:
    value = heading.strip().lower()
    value = re.sub(r"[^\w\-\u4e00-\u9fff ]", "", value)
    return re.sub(r"\s+", "-", value)


def markdown_ref_resolves(ref: str) -> bool:
    path_text, separator, fragment = ref.partition("#")
    if not separator or not fragment:
        return False
    path = ROOT / path_text
    if not path.is_file():
        return False
    headings = {
        markdown_heading_slug(line.lstrip("#").strip())
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.startswith("#")
    }
    return fragment in headings


def main() -> None:
    items = []
    for day in range(1, 8):
        packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
        comparison = json.loads(
            (packet / "books-current-content-comparison.json").read_text(encoding="utf-8")
        )
        for row in comparison["items"]:
            target_ok = markdown_ref_resolves(row["target_ref"])
            adjacent_failures = [
                ref for ref in row.get("adjacent_refs", []) if not markdown_ref_resolves(ref)
            ]
            items.append(
                {
                    "report_date": f"2026-04-{day:02d}",
                    "source_family_id": row["source_family_id"],
                    "arxiv_id": row["arxiv_id"],
                    "decision": row["decision"],
                    "target_ref": row["target_ref"],
                    "target_ref_resolves": target_ok,
                    "unresolved_adjacent_refs": adjacent_failures,
                    "status": "books_comparison_reopen_required"
                    if not target_ok or adjacent_failures
                    else "pending_fresh_context_semantic_acceptance",
                }
            )

    unresolved = [
        item for item in items
        if item["status"] == "books_comparison_reopen_required"
    ]
    payload = {
        "schema": "historical-daily-books-prewrite-root-acceptance-v1",
        "scope": "2026-04-01..2026-04-07",
        "weekly_semantic_inputs": [],
        "comparison_items": len(items),
        "unresolved_reference_items": len(unresolved),
        "status": "open_rejected_placeholder_books_refs",
        "semantic_sample_finding": {
            "source_family_id": "SF-2026-ARXIV-2603-29493",
            "finding": (
                "MemFactory is routed to PLATFORM-EVALUATION-SYSTEM with a generic runtime/SLO "
                "delta even though the disclosed mechanism is a memory-agent training/inference "
                "framework; owner and existing-proposition comparison must be redone."
            ),
        },
        "gate_effect": (
            "Coverage/Evidence acceptance is unchanged. Books remains Open; no April 1-7 queue "
            "may be written until every comparison has real owner/adjacent proposition refs and "
            "passes a fresh-context semantic review."
        ),
        "items": items,
    }
    out = ROOT / "papers/2026/04/_sources/april01-07-books-prewrite-root-audit.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
