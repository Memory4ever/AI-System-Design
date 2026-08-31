#!/usr/bin/env python3
"""Refresh 2026-06-01 Books comparison line locators against current Books.

The substantive propositions are frozen in the date-local reconciliation TSV.
This script only moves a locator when the current owner text still matches that
frozen proposition above a conservative similarity threshold.  Ambiguous or
missing propositions fail closed.
"""

from __future__ import annotations

import argparse
import csv
import difflib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "papers/2026/06/01/README.md"
RECON = ROOT / "papers/2026/06/_sources/daily-20260601/books-comparison-v9-retained-proposition-reconciliation.tsv"


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", value.lower())


def current_ref(old_ref: str, proposition: str) -> tuple[str, float]:
    path_text, _old_line = old_ref.rsplit("#L", 1)
    path = ROOT / path_text
    lines = path.read_text().splitlines()
    expected = normalize(proposition)
    assert len(expected) >= 60, (old_ref, proposition)
    candidates: list[tuple[float, int]] = []
    prefix = expected[:16]
    for index, line in enumerate(lines):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        line_normalized = normalize(line)
        # Reconciliation excerpts begin at the proposition's first content
        # line.  Restrict expensive sequence matching to prefix-bearing lines;
        # a short prefix tolerates punctuation and small copy edits while
        # avoiding quadratic scans over entire large chapters.
        if prefix not in line_normalized and expected[:10] not in line_normalized:
            continue
        for width in range(1, 9):
            window = normalize(" ".join(lines[index : index + width]))
            if len(window) < 40:
                continue
            ratio = difflib.SequenceMatcher(None, expected, window).ratio()
            candidates.append((ratio, index + 1))
    candidates.sort(reverse=True)
    best_ratio, best_line = candidates[0]
    second_ratio, second_line = candidates[1]
    assert best_ratio >= 0.62, (old_ref, best_ratio, proposition[:120])
    # Equal scores on adjacent window widths are harmless; equal scores at a
    # different paragraph are an owner ambiguity and must not be auto-repaired.
    if second_line != best_line:
        assert best_ratio - second_ratio >= 0.015, (
            old_ref,
            best_ratio,
            best_line,
            second_ratio,
            second_line,
        )
    return f"{path_text}#L{best_line}", best_ratio


def split_propositions(value: str, count: int) -> list[str]:
    parts = value.split(" / ", count - 1)
    assert len(parts) == count, (count, value)
    return parts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    with RECON.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    replacements: dict[str, str] = {}
    scores: list[float] = []
    for row in rows:
        old_target = row["Target Chapter Ref"]
        new_target, score = current_ref(old_target, row["Target Substantive Proposition"])
        replacements[old_target] = new_target
        row["Target Chapter Ref"] = new_target
        scores.append(score)

        adjacent_refs = row["Adjacent Chapter Refs"].split(";")
        adjacent_props = split_propositions(row["Adjacent Substantive Propositions"], len(adjacent_refs))
        new_adjacent: list[str] = []
        for old_ref, proposition in zip(adjacent_refs, adjacent_props):
            new_ref, score = current_ref(old_ref, proposition)
            replacements[old_ref] = new_ref
            new_adjacent.append(new_ref)
            scores.append(score)
        row["Adjacent Chapter Refs"] = ";".join(new_adjacent)

    report = REPORT.read_text()
    changed_refs = 0
    for old_ref, new_ref in replacements.items():
        if old_ref == new_ref:
            continue
        assert old_ref in report, f"stale locator is absent from Daily: {old_ref}"
        report = report.replace(old_ref, new_ref)
        changed_refs += 1

    if args.apply:
        REPORT.write_text(report)
        with RECON.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
    print(
        f"rows={len(rows)} locator_cells={len(scores)} changed_unique_refs={changed_refs} "
        f"min_similarity={min(scores):.3f} mode={'apply' if args.apply else 'dry-run'}"
    )


if __name__ == "__main__":
    main()
