#!/usr/bin/env python3
"""Idempotently apply the reviewed 2026-06-29 owner-merged Books packet."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READY = ROOT / "papers/2026/06/_sources/daily-20260629/READY_TO_INSERT_BOOKS_V1.md"


@dataclass(frozen=True)
class OwnerBlock:
    owner: str
    target: Path
    body: str
    notes: str
    families: tuple[str, ...]

    @property
    def start(self) -> str:
        return f"<!-- june29-owner:{self.owner}:start -->"

    @property
    def end(self) -> str:
        return f"<!-- june29-owner:{self.owner}:end -->"

    @property
    def rendered(self) -> str:
        return (
            f"{self.start}\n"
            f"## 2026-06-29 约束变化与机制增量\n\n"
            f"{self.body}\n\n"
            f"### 2026-06-29 source-specific Review notes\n\n"
            f"{self.notes}\n"
            f"{self.end}\n\n"
        )


def parse_ready() -> tuple[OwnerBlock, ...]:
    text = READY.read_text(encoding="utf-8")
    matches = list(
        re.finditer(
            r"^## `(?P<owner>[^`]+)` → `(?P<target>[^`]+)`\n\n(?P<section>.*?)(?=^## `|\Z)",
            text,
            re.MULTILINE | re.DOTALL,
        )
    )
    blocks: list[OwnerBlock] = []
    for match in matches:
        section = match.group("section").strip()
        split = section.find("Review note：")
        if split < 0:
            raise AssertionError(f"{match.group('owner')}: Review notes missing")
        body = section[:split].strip()
        notes = section[split:].strip()
        families = tuple(sorted(set(re.findall(r"SF-2026-ARXIV-2606-\d+", section))))
        if not families:
            raise AssertionError(f"{match.group('owner')}: no source family")
        blocks.append(
            OwnerBlock(
                owner=match.group("owner"),
                target=ROOT / match.group("target"),
                body=body,
                notes=notes,
                families=families,
            )
        )
    if len(blocks) != 9 or sum(len(block.families) for block in blocks) != 13:
        raise AssertionError("06-29 ready packet shape drift")
    return tuple(blocks)


def all_books() -> dict[Path, str]:
    return {path.resolve(): path.read_text(encoding="utf-8") for path in (ROOT / "books").rglob("*.md")}


def main() -> None:
    blocks = parse_ready()
    snapshots = all_books()
    proposed: dict[Path, str] = {}

    for block in blocks:
        target = block.target.resolve()
        text = snapshots[target]
        family_hits = {
            family: [path for path, content in snapshots.items() if family in content]
            for family in block.families
        }
        if text.count(block.start) == text.count(block.end) == 1:
            if text.count(block.rendered) != 1:
                raise AssertionError(f"{block.owner}: restored block content drift")
            for family, hits in family_hits.items():
                if hits != [target] or text.count(family) != 2:
                    raise AssertionError(f"{family}: invalid idempotent owner state")
            continue
        if block.start in text or block.end in text or any(family_hits.values()):
            raise AssertionError(f"{block.owner}: partial or foreign 06-29 state")
        anchors = list(re.finditer(r"^## Review notes$", text, re.MULTILINE))
        if len(anchors) != 1:
            raise AssertionError(f"{block.owner}: Review notes anchor is not unique")
        proposed_text, replacement_count = re.subn(
            r"^## Review notes$",
            block.rendered.rstrip() + "\n\n## Review notes",
            text,
            count=1,
            flags=re.MULTILINE,
        )
        if replacement_count != 1:
            raise AssertionError(f"{block.owner}: Review notes replacement failed")
        proposed[target] = proposed_text

    for path, content in proposed.items():
        path.write_text(content, encoding="utf-8")

    after = all_books()
    for block in blocks:
        target = block.target.resolve()
        text = after[target]
        if text.count(block.rendered) != 1:
            raise AssertionError(f"{block.owner}: post-write block count drift")
        for family in block.families:
            hits = [path for path, content in after.items() if family in content]
            if hits != [target] or text.count(family) != 2:
                raise AssertionError(f"{family}: post-write owner uniqueness failure")

    print(
        f"06-29 Books applied/verified: 13 families across 9 owners; "
        f"newly written owners={len(proposed)}"
    )


if __name__ == "__main__":
    main()
