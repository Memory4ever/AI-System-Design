#!/usr/bin/env python3
"""Apply recovered 2026-06-23/24/25 Books packets under a shared write lock.

The date-local READY packet is the payload owner.  This helper does not invent
or summarize prose: it moves the reviewed owner block into the canonical
chapter, before the chapter-level Review notes.  It validates the whole date
before writing and refuses foreign, duplicate, or unrecognised partial state.

Use ``--check`` before the coordinator grants the shared Books lock.  ``--apply``
is required for writes.  Re-running a fully applied date is a verified no-op.
"""

from __future__ import annotations

import argparse
import json
import re
import tempfile
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SUPPORTED_DAYS = {"23", "24", "25"}


def marker(day: str, owner: str, edge: str) -> str:
    return f"<!-- recovered-daily-202606{day}:{owner}:{edge} -->"


def parse_ready(day: str) -> dict[str, dict[str, object]]:
    ready = ROOT / f"papers/2026/06/_sources/daily-202606{day}/READY_TO_INSERT_BOOKS_V1.md"
    raw = ready.read_text(encoding="utf-8")
    if day == "25":
        packet = ready.parent
        receipts = json.loads((packet / "source-review-receipts-v2.1.json").read_text())["items"]
        comparisons = {
            row["source_family_id"]: row
            for row in json.loads((packet / "books-comparison-v1.json").read_text())["items"]
        }
        groups: dict[str, list[dict]] = defaultdict(list)
        for row in receipts:
            if row["books_disposition"] == "Integrate":
                groups[row["stable_node_id"]].append(row)

        parsed: dict[str, dict[str, object]] = {}
        for owner, rows in groups.items():
            path = comparisons[rows[0]["source_family_id"]]["target_chapter_ref"].split("#", 1)[0]
            body = [f"- **{row['source_family_id']}**：{row['claim']} {row['claim_boundary']}" for row in rows]
            notes = [
                f"- **{row['source_family_id']}**：Primary `{row['primary_evidence_version']}`；"
                f"Method `{row['method_locator']}`；Evaluation `{row['evaluation_locator']}`；"
                f"未证明边界 `{row['limitation_locator']}`；Artifact `{row['artifact_locators']}`。"
                for row in rows
            ]
            payload = "\n".join(body + ["", "### 2026-06-25 source-specific Review notes", ""] + notes)
            parsed[owner] = {
                "path": path,
                "payload": payload,
                "families": [row["source_family_id"] for row in rows],
            }
        if len(receipts) != 68 or sum(len(item["families"]) for item in parsed.values()) != 63:
            raise RuntimeError("06-25: expected 68 reviews and 63 Integrate families")
        return parsed

    if day in {"23", "25"}:
        header = re.compile(r"^## `(?P<owner>[^`]+)` → `(?P<path>[^`]+)`\s*$", re.MULTILINE)
    else:
        header = re.compile(r"^## (?P<owner>[A-Z0-9-]+) — (?P<path>books/\S+)\s*$", re.MULTILINE)

    matches = list(header.finditer(raw))
    if not matches:
        raise RuntimeError(f"06-{day}: READY owner sections not found")

    parsed: dict[str, dict[str, object]] = {}
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(raw)
        payload = raw[start:end].strip()
        families = sorted(set(re.findall(r"SF-2026-ARXIV-\d{4}-\d+", payload)))
        if not families:
            raise RuntimeError(f"06-{day} {match.group('owner')}: no Source Family in READY block")
        for family in families:
            if payload.count(family) != 2:
                raise RuntimeError(
                    f"06-{day} {match.group('owner')}: {family} must occur twice in READY payload"
                )
        parsed[match.group("owner")] = {
            "path": match.group("path"),
            "payload": payload,
            "families": families,
        }
    return parsed


def family_hits(snapshots: dict[Path, str], family: str) -> list[tuple[Path, int]]:
    return [(path, text.count(family)) for path, text in snapshots.items() if family in text]


def strip_known_legacy_block(day: str, owner: str, text: str, payload: str) -> str:
    """Remove only recognised pre-recovery blocks from the partially restored tree."""

    if owner == "INFER-GPU-MEMORY":
        bounded_patterns = {
            "23": re.compile(
                r"\n### 2026-06-23 exact-v1 handoff — INFER-GPU-MEMORY\n.*?"
                r"(?=\n## 2026-06-25 机制演进\n)",
                re.DOTALL,
            ),
            "24": re.compile(
                r"\n## 2026-06-24 机制演进\n.*?(?=\n## Review [Nn]otes\n)",
                re.DOTALL,
            ),
            "25": re.compile(
                r"\n## 2026-06-25 机制演进\n.*?"
                r"(?=\n### 低比特收益还取决于同一 SM 内的 Compute Balance\n)",
                re.DOTALL,
            ),
        }
        matches = list(bounded_patterns[day].finditer(text))
        if len(matches) == 1:
            return text[: matches[0].start()] + text[matches[0].end() :]

    if payload in text:
        # 06-23 survived below a date-specific H3.  The payload itself starts
        # after that heading, so remove the heading plus the exact payload.
        prefix_patterns = {
            "23": rf"\n### 2026-06-23 exact-v1 handoff — {re.escape(owner)}\n\n",
            "24": r"\n## 2026-06-24 机制演进\n\n",
            "25": r"\n## 2026-06-25 机制演进\n\n",
        }
        before = text[: text.index(payload)]
        prefix = re.search(prefix_patterns[day] + r"$", before)
        if prefix:
            return text[: prefix.start()] + text[text.index(payload) + len(payload) :]

        # A payload without its historical heading is still safe to move only
        # when it is the exact reviewed string.
        return text.replace(payload, "", 1)

    raise RuntimeError(f"06-{day} {owner}: unrecognised partial Books state")


def insert_before_review_notes(text: str, block: str) -> str:
    review = re.search(r"^## Review [Nn]otes\s*$", text, re.MULTILINE)
    if review:
        return text[: review.start()].rstrip() + "\n\n" + block + "\n\n" + text[review.start() :].lstrip()
    return text.rstrip() + "\n\n" + block + "\n"


def plan(day: str) -> tuple[dict[Path, str], dict[str, int]]:
    parsed = parse_ready(day)
    book_files = sorted((ROOT / "books").rglob("*.md"))
    snapshots = {path: path.read_text(encoding="utf-8") for path in book_files}
    proposed: dict[Path, str] = {}
    already_applied = 0
    partial_recovered = 0

    # Validate every owner against one immutable snapshot before the first
    # mutation.  Multiple owners never share a chapter in these three packets.
    target_paths = [ROOT / str(item["path"]) for item in parsed.values()]
    if len(target_paths) != len(set(target_paths)):
        raise RuntimeError(f"06-{day}: multiple READY owners target the same chapter")

    for owner, item in parsed.items():
        target = ROOT / str(item["path"])
        payload = str(item["payload"])
        families = list(item["families"])
        text = snapshots[target]
        start = marker(day, owner, "start")
        end = marker(day, owner, "end")
        complete_block = f"{start}\n## 2026-06-{day} evidence integration — {owner}\n\n{payload}\n{end}"

        foreign = {
            family: [(path.relative_to(ROOT).as_posix(), count) for path, count in family_hits(snapshots, family)]
            for family in families
            if any(path != target for path, _ in family_hits(snapshots, family))
        }
        if foreign:
            raise RuntimeError(f"06-{day} {owner}: foreign Source Family hits: {foreign}")

        if start in text or end in text:
            if text.count(start) != 1 or text.count(end) != 1 or complete_block not in text:
                raise RuntimeError(f"06-{day} {owner}: incomplete or drifted recovery markers")
            if any(text.count(family) != 2 for family in families):
                raise RuntimeError(f"06-{day} {owner}: applied block family count mismatch")
            already_applied += 1
            continue

        present = [family for family in families if family in text]
        base = text
        if present:
            # Every present family must still be confined to the expected
            # owner.  Only an exact known legacy block may be replaced.
            base = strip_known_legacy_block(day, owner, text, payload).rstrip() + "\n"
            if any(family in base for family in families):
                raise RuntimeError(f"06-{day} {owner}: legacy cleanup left Source Family markers")
            partial_recovered += 1

        proposed[target] = insert_before_review_notes(base, complete_block)

    # Simulate the complete result and verify global unique owner + exactly two
    # occurrences (mechanism body and exact-v1 Review note) per family.
    simulated = dict(snapshots)
    simulated.update(proposed)
    for owner, item in parsed.items():
        target = ROOT / str(item["path"])
        for family in item["families"]:
            hits = family_hits(simulated, family)
            if hits != [(target, 2)]:
                rendered = [(path.relative_to(ROOT).as_posix(), count) for path, count in hits]
                raise RuntimeError(f"06-{day} {family}: simulated uniqueness failure: {rendered}")

    return proposed, {
        "owners": len(parsed),
        "families": sum(len(item["families"]) for item in parsed.values()),
        "writes": len(proposed),
        "already_applied": already_applied,
        "legacy_blocks_recovered": partial_recovered,
    }


def atomic_apply(proposed: dict[Path, str]) -> None:
    staged: list[tuple[Path, Path]] = []
    try:
        for target, text in proposed.items():
            with tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", dir=target.parent, prefix=f".{target.name}.", delete=False
            ) as handle:
                handle.write(text)
                temp = Path(handle.name)
            staged.append((target, temp))
        for target, temp in staged:
            temp.replace(target)
    finally:
        for _, temp in staged:
            if temp.exists():
                temp.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--day", required=True, choices=sorted(SUPPORTED_DAYS))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    proposed, stats = plan(args.day)
    if args.apply:
        atomic_apply(proposed)
        # Replan after write to prove the state is a complete idempotent no-op.
        remaining, verified = plan(args.day)
        if remaining:
            raise RuntimeError(f"06-{args.day}: post-write plan is not empty")
        stats["post_write_verified"] = verified["already_applied"] == verified["owners"]
    else:
        stats["post_write_verified"] = False
    print(stats)


if __name__ == "__main__":
    main()
