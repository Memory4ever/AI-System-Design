#!/usr/bin/env python3
"""Relocate recovered Daily integration text without changing its claims.

This script performs only structural normalization:

1. mechanism text accidentally appended after ``## 小结`` or ``## Reflection``
   is moved before the chapter's self-check section;
2. source-specific evidence subsections embedded in the mechanism body are
   moved under the chapter's ``## Review notes``;
3. no source-family bullet or evidence statement is deleted.

Semantic merging remains a separate, chapter-by-chapter review.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


POST_SUMMARY_START = re.compile(
    r"^(?:### |## 2026-|<!-- (?:recovered-daily|june29-owner))"
)
SOURCE_NOTE_HEADING = re.compile(
    r"^### (?:Source-specific|\d{4}-\d{2}-\d{2} source-specific).*Review notes$",
    re.IGNORECASE,
)
MARKER_END = re.compile(r"^<!-- .+:end -->$")


def _find(lines: list[str], value: str) -> int | None:
    try:
        return lines.index(value)
    except ValueError:
        return None


def _find_any(lines: list[str], values: tuple[str, ...]) -> int | None:
    indexes = [index for index, line in enumerate(lines) if line in values]
    return min(indexes) if indexes else None


def normalize_review_notes(lines: list[str]) -> tuple[list[str], bool]:
    """Keep exactly one chapter-level Review notes section at the end.

    Recovered source blocks sometimes carried their own H2 Review notes.  Those
    are evidence subsections, not a second chapter boundary.
    """
    indexes = [index for index, line in enumerate(lines) if line == "## Review notes"]
    if not indexes:
        return lines, False
    changed = False
    for index in indexes[:-1]:
        lines[index] = "#### Source-specific Review notes"
        changed = True
    review = indexes[-1]
    for index in range(review + 1, len(lines)):
        if lines[index].startswith("## "):
            lines[index] = "### " + lines[index][3:]
            changed = True
    return lines, changed


def relocate_post_summary(lines: list[str]) -> tuple[list[str], bool]:
    closeouts = [
        index for index, line in enumerate(lines) if line in ("## 小结", "## Reflection")
    ]
    summary = max(closeouts) if closeouts else None
    review = _find(lines, "## Review notes")
    self_check = _find_any(lines, ("## 自检问题", "## 面试与自检问题"))
    if summary is None or review is None or self_check is None or not (self_check < summary < review):
        return lines, False

    start = next(
        (index for index in range(summary + 1, review) if POST_SUMMARY_START.match(lines[index])),
        None,
    )
    if start is None:
        return lines, False

    block = lines[start:review]
    del lines[start:review]
    self_check = _find_any(lines, ("## 自检问题", "## 面试与自检问题"))
    assert self_check is not None
    insertion = block[:]
    while insertion and not insertion[-1].strip():
        insertion.pop()
    insertion.extend(["", ""])
    lines[self_check:self_check] = insertion
    return lines, True


def extract_source_notes(lines: list[str]) -> tuple[list[str], bool]:
    review = _find(lines, "## Review notes")
    if review is None:
        return lines, False

    extracted: list[list[str]] = []
    index = 0
    while index < review:
        if not SOURCE_NOTE_HEADING.match(lines[index]):
            index += 1
            continue
        end = index + 1
        while end < review:
            line = lines[end]
            if MARKER_END.match(line) or line.startswith("## ") or line.startswith("### "):
                break
            end += 1
        section = lines[index:end]
        section[0] = "#### " + section[0][4:]
        extracted.append(section)
        del lines[index:end]
        review -= end - index

    if not extracted:
        return lines, False

    while lines and not lines[-1].strip():
        lines.pop()
    lines.extend(["", "### Daily integration evidence trace", ""])
    for section in extracted:
        lines.extend(section)
        if lines[-1].strip():
            lines.append("")
    return lines, True


def normalize(text: str) -> tuple[str, bool]:
    lines = text.splitlines()
    lines, review_notes = normalize_review_notes(lines)
    lines, moved = relocate_post_summary(lines)
    lines, extracted = extract_source_notes(lines)
    output = "\n".join(lines).rstrip() + "\n"
    return output, review_notes or moved or extracted


def chapter_paths(root: Path) -> list[Path]:
    return sorted(
        path
        for path in (root / "books").glob("part-*/*.md")
        if re.match(r"\d{2}-", path.name)
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    changed: list[Path] = []
    for path in chapter_paths(args.root):
        before = path.read_text(encoding="utf-8")
        after, was_changed = normalize(before)
        if not was_changed or after == before:
            continue
        changed.append(path)
        if args.write:
            path.write_text(after, encoding="utf-8")

    mode = "updated" if args.write else "would update"
    print(f"{mode}: {len(changed)} chapters")
    for path in changed:
        print(path.relative_to(args.root))


if __name__ == "__main__":
    main()
