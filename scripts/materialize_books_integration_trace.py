#!/usr/bin/env python3
"""Materialize missing Daily Books deltas as source-family evidence notes.

The chapter body remains mechanism-owned.  This script only closes the exact
Daily -> owner chapter trace under Review notes for Integrate decisions that do
not already name their Source Family or primary identifier in the owner file.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


TRACE_HEADING = "### Daily Books delta trace（2026-06—08）"


def extract_delta(report: Path, source_family: str) -> str:
    text = report.read_text(encoding="utf-8")
    family = re.escape(source_family)
    match = re.search(
        rf"<!-- delta:{family}:start -->(.*?)<!-- delta:{family}:end -->",
        text,
        re.S,
    )
    if not match:
        raise ValueError(f"{report}: missing delta marker for {source_family}")
    delta = re.sub(r"<!--.*?-->", "", match.group(1), flags=re.S).strip()
    return re.sub(r"\n{3,}", "\n\n", delta)


def trace_block(row: dict[str, str], delta: str) -> str:
    family = row["source_family"]
    return (
        f"<!-- daily-books-trace:{family}:start -->\n"
        f"- `{family}` — Daily `{row['report_date']}`；primary "
        f"`{row['primary_identifier']}`；Books review `{row['books_review_ref']}`。\n\n"
        f"  **已吸收的语义增量：** {delta}\n"
        f"<!-- daily-books-trace:{family}:end -->"
    )


def insert_blocks(text: str, blocks: list[str]) -> str:
    if not blocks:
        return text
    if "## Review notes" not in text:
        raise ValueError("owner chapter lacks Review notes")
    addition = "\n\n".join(blocks)
    if TRACE_HEADING in text:
        return text.rstrip() + "\n\n" + addition + "\n"
    return text.rstrip() + f"\n\n{TRACE_HEADING}\n\n{addition}\n"


def load_missing_rows(ledger: Path) -> list[dict[str, str]]:
    with ledger.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    return rows


def needs_source_family_trace(chapter_text: str, source_family: str) -> bool:
    if "## Review notes" not in chapter_text:
        raise ValueError("owner chapter lacks Review notes")
    review = chapter_text.rsplit("## Review notes", 1)[1]
    return source_family not in review


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--ledger",
        type=Path,
        default=Path("papers/2026/_sources/books-integration-audit-2026-06-08/integration-reconciliation.tsv"),
    )
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    ledger = args.ledger if args.ledger.is_absolute() else root / args.ledger

    grouped: dict[str, list[tuple[dict[str, str], str]]] = defaultdict(list)
    for row in load_missing_rows(ledger):
        chapter_text = (root / row["owner_path"]).read_text(encoding="utf-8")
        if not needs_source_family_trace(chapter_text, row["source_family"]):
            continue
        report_date = row["report_date"]
        report = root / "papers" / "2026" / report_date[5:7] / report_date[8:] / "README.md"
        grouped[row["owner_path"]].append((row, extract_delta(report, row["source_family"])))

    changed: list[tuple[str, int]] = []
    for relative, entries in sorted(grouped.items()):
        path = root / relative
        before = path.read_text(encoding="utf-8")
        entries.sort(key=lambda item: (item[0]["report_date"], item[0]["source_family"]))
        blocks = [trace_block(row, delta) for row, delta in entries]
        after = insert_blocks(before, blocks)
        if after == before:
            continue
        changed.append((relative, len(entries)))
        if args.write:
            path.write_text(after, encoding="utf-8")

    action = "updated" if args.write else "would update"
    print(f"{action}: {len(changed)} chapters, {sum(count for _, count in changed)} source families")
    for relative, count in changed:
        print(f"{count}\t{relative}")


if __name__ == "__main__":
    main()
