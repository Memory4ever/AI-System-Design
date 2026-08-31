#!/usr/bin/env python3
"""Emit an apply_patch payload for the authorized 2026-06-25 Books writeback."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260625"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("owners", nargs="+")
    args = parser.parse_args()

    receipts = json.loads((PACKET / "source-review-receipts-v2.1.json").read_text())["items"]
    comparisons = {
        row["source_family_id"]: row
        for row in json.loads((PACKET / "books-comparison-v1.json").read_text())["items"]
    }
    groups = defaultdict(list)
    for row in receipts:
        if row["books_disposition"] == "Integrate":
            groups[row["stable_node_id"]].append(row)

    requested = set(args.owners)
    missing = requested - set(groups)
    if missing:
        raise SystemExit(f"unknown or non-Integrate owners: {sorted(missing)}")

    patch = ["*** Begin Patch"]
    for owner in sorted(requested):
        items = groups[owner]
        path = comparisons[items[0]["source_family_id"]]["target_chapter_ref"].split("#", 1)[0]
        book = ROOT / path
        text = book.read_text()
        families = [row["source_family_id"] for row in items]
        duplicates = [family for family in families if family in text]
        if duplicates:
            raise SystemExit(f"{path}: existing 2026-06-25 family markers: {duplicates}")
        last_line = next(line for line in reversed(text.splitlines()) if line.strip())
        patch.extend([f"*** Update File: {path}", "@@", f" {last_line}", "+", "+## 2026-06-25 机制演进", "+"])
        for row in items:
            patch.append(f"+- **{row['source_family_id']}**：{row['claim']} {row['claim_boundary']}")
        patch.extend(["+", "+### 2026-06-25 source-specific Review notes", "+"])
        for row in items:
            patch.append(
                f"+- **{row['source_family_id']}**：Primary `{row['primary_evidence_version']}`；"
                f"Method `{row['method_locator']}`；Evaluation `{row['evaluation_locator']}`；"
                f"未证明边界 `{row['limitation_locator']}`；Artifact `{row['artifact_locators']}`。"
            )
    patch.append("*** End Patch")
    print("\n".join(patch))


if __name__ == "__main__":
    main()
