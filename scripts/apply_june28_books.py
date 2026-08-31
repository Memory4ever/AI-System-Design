#!/usr/bin/env python3
"""Guarded, idempotent Books writer for 2026-06-28. Dry-run unless --apply."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READY = ROOT / "papers/2026/06/_sources/daily-20260628/READY_TO_INSERT_BOOKS_V1.md"


def parse_blocks() -> list[dict]:
    text = READY.read_text()
    pattern = re.compile(
        r"^## (?P<owner>[A-Z0-9-]+) — (?P<path>books/[^\n]+)\n\n"
        r"Insert after: (?P<anchor>[^\n]+)\n\n(?P<body>.*?)(?=^## [A-Z0-9-]+ — books/|\Z)",
        re.M | re.S,
    )
    blocks = []
    for match in pattern.finditer(text):
        data = match.groupdict()
        data["body"] = data["body"].rstrip() + "\n"
        data["families"] = re.findall(r"SF-2026-ARXIV-(\d{4}-\d{5})", data["body"])
        blocks.append(data)
    assert len(blocks) == 6
    assert sum(len(block["families"]) for block in blocks) == 6
    assert len({block["path"] for block in blocks}) == 6
    return blocks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    blocks = parse_blocks()
    all_books = list((ROOT / "books").rglob("*.md"))
    corpus = {path: path.read_text() for path in all_books}
    planned = []

    for block in blocks:
        target = ROOT / block["path"]
        assert target in corpus
        text = corpus[target]
        marker_start = f"<!-- daily-20260628:{block['owner']}:start -->"
        marker_end = f"<!-- daily-20260628:{block['owner']}:end -->"
        global_start = sum(value.count(marker_start) for value in corpus.values())
        global_end = sum(value.count(marker_end) for value in corpus.values())
        family_hits = {
            arxiv_id: [
                str(path.relative_to(ROOT)) for path, value in corpus.items()
                if arxiv_id.replace("-", ".") in value
            ]
            for arxiv_id in block["families"]
        }
        if (global_start, global_end) == (1, 1):
            assert marker_start in text and marker_end in text
            assert all(paths == [block["path"]] for paths in family_hits.values())
            planned.append((block["owner"], "already_applied"))
            continue
        assert (global_start, global_end) == (0, 0), (block["owner"], "partial/duplicate marker state")
        assert all(not paths for paths in family_hits.values()), (block["owner"], family_hits)
        anchor = block["anchor"]
        assert text.splitlines().count(anchor) == 1, (block["path"], anchor)
        payload = f"{marker_start}\n{block['body']}{marker_end}\n\n"
        updated = text.replace(anchor + "\n", anchor + "\n\n" + payload, 1)
        planned.append((block["owner"], "would_apply"))
        if args.apply:
            target.write_text(updated)
            corpus[target] = updated

    print("mode=" + ("apply" if args.apply else "dry-run"))
    for owner, state in planned:
        print(f"{owner}: {state}")


if __name__ == "__main__":
    main()
