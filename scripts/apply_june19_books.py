#!/usr/bin/env python3
"""Apply the root-reviewed 2026-06-19 Books packet exactly once."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260619"
READY = PACKET / "READY_TO_INSERT_BOOKS_V1.md"


def parse_sections(text: str) -> list[tuple[str, str, str]]:
    parts = re.split(r"(?m)^## ", text)[1:]
    parsed = []
    for part in parts:
        heading, rest = part.split("\n", 1)
        match = re.search(r"—\s+(`?)([^`\n]+\.md)\1$", heading.strip())
        if not match:
            raise RuntimeError(f"cannot parse owner path: {heading}")
        path = match.group(2)
        body_match = re.search(
            r"### Owner-merged minimal text\n\n(.*?)\n\n### Source-specific Review notes\n\n(.*)\Z",
            rest.strip(),
            flags=re.S,
        )
        if not body_match:
            raise RuntimeError(f"cannot parse body/review notes for {heading}")
        parsed.append((path, body_match.group(1).strip(), body_match.group(2).strip()))
    return parsed


def main() -> None:
    receipts = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())["items"]
    integrations = [row for row in receipts if row["books_disposition"] == "Integrate"]
    assert len(integrations) == 56
    sections = parse_sections(READY.read_text())
    assert len(sections) == 23

    all_books = list((ROOT / "books").rglob("*.md"))
    for review in integrations:
        family = review["source_family_id"]
        hits = [str(path.relative_to(ROOT)) for path in all_books if family in path.read_text()]
        if hits:
            raise RuntimeError(f"refusing duplicate write for {family}: {hits}")

    inserted = 0
    for raw_path, body, notes in sections:
        path = ROOT / raw_path
        text = path.read_text()
        marker = "\n## Review notes\n"
        if text.count(marker) != 1:
            raise RuntimeError(f"expected one Review notes marker in {path}")
        family_count = body.count("SF-2026-ARXIV-")
        if family_count != notes.count("SF-2026-ARXIV-"):
            raise RuntimeError(f"body/note family mismatch in {raw_path}")
        insert = (
            "\n### 新证据如何改变本章的设计边界\n\n"
            + body
            + "\n\n## Review notes\n\n"
            + notes
            + "\n"
        )
        path.write_text(text.replace(marker, insert, 1))
        inserted += family_count

    assert inserted == len(integrations)
    print(f"applied {inserted} families to {len(sections)} owner files")


if __name__ == "__main__":
    main()
