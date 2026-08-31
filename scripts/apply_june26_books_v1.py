#!/usr/bin/env python3
"""Idempotently apply the reviewed 2026-06-26 owner-merged Books packet.

The script reads the date-local READY packet, validates global family
uniqueness and all insertion anchors before writing, then inserts one durable
mechanism narrative into each owner's evolution chain and appends only the
source-specific evidence note to the chapter-end evidence area.
"""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READY = ROOT / "papers/2026/06/_sources/daily-20260626/READY_TO_INSERT_BOOKS_V1.md"

TARGETS = {
    "AGENT-MCP": (
        "books/part-07-agent/83-mcp.md",
        "## Observability",
        "### 从单工具扫描到组合级 Admission",
    ),
    "AGENT-MULTI-AGENT": (
        "books/part-07-agent/82-multi-agent.md",
        "## Evaluation",
        "### Verification Delay 也是拓扑控制状态",
    ),
    "INFER-SCHEDULING": (
        "books/part-05-inference-system/56-inference-scheduling.md",
        "### Value Estimation 本身也有成本",
        "### MoE 并行形态从部署配置演进为运行时状态",
    ),
    "MULTIMODAL-EMBODIED-VLA": (
        "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "## Sim-to-real 不只是视觉 domain gap",
        "### Growing Policy Pool 需要分离 Commissioning 与 Onboarding",
    ),
    "TRAIN-DISTRIBUTED-TRAINING": (
        "books/part-04-training-system/36-distributed-training.md",
        "## 分布式训练必须保持哪些不变量",
        "### 矩阵耦合 Optimizer 必须把更新本身变成 Distributed Operation",
    ),
    "TRAIN-RLHF": (
        "books/part-04-training-system/31-rlhf.md",
        "### 在线反馈的采样预算应由 Epistemic Uncertainty 驱动",
        "### Reward Heterogeneity 同时存在于 Rater Identity 与反馈时间",
    ),
}


def parse_ready() -> dict[str, dict[str, object]]:
    raw = READY.read_text()
    pattern = re.compile(
        r"^## `(?P<owner>[^`]+)` → `(?P<path>[^`]+)`\n"
        r".*?^### Owner-merged minimal body\n\n(?P<body>.*?)\n\n"
        r"^### Source-specific exact-v1 Review notes\n\n(?P<notes>.*?)(?=\n## `|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    parsed: dict[str, dict[str, object]] = {}
    for match in pattern.finditer(raw):
        owner = match.group("owner")
        body = match.group("body").strip()
        notes = [line for line in match.group("notes").strip().splitlines() if line.startswith("- `SF-")]
        families = re.findall(r"`(SF-2026-ARXIV-[0-9-]+)`", "\n".join(notes))
        parsed[owner] = {
            "path": match.group("path"),
            "body": body,
            "notes": notes,
            "families": families,
        }
    if set(parsed) != set(TARGETS):
        raise AssertionError(f"READY owner mismatch: {sorted(parsed)}")
    if sum(len(item["families"]) for item in parsed.values()) != 7:
        raise AssertionError("READY must contain exactly seven family Review notes")
    return parsed


def main() -> None:
    parsed = parse_ready()
    book_files = list((ROOT / "books").rglob("*.md"))
    snapshots = {path: path.read_text() for path in book_files}
    proposed: dict[Path, str] = {}

    # Validate the complete state first. Any foreign/partial family write stops
    # the whole batch before the first owner file is changed.
    for owner, item in parsed.items():
        relpath, anchor, heading = TARGETS[owner]
        if item["path"] != relpath:
            raise AssertionError(f"{owner}: READY path {item['path']} != {relpath}")
        target = ROOT / relpath
        text = snapshots[target]
        body = str(item["body"])
        notes = list(item["notes"])
        families = list(item["families"])
        body_present = body in text
        note_present = all(note in text for note in notes)

        for family in families:
            hits = [path for path, content in snapshots.items() if family in content]
            if hits and hits != [target]:
                raise AssertionError(f"{family}: foreign/duplicate Books hits {hits}")

        if body_present or note_present:
            if not (body_present and note_present):
                raise AssertionError(f"{owner}: partial prior write; refusing guessed merge")
            if text.count(body) != 1 or any(text.count(family) != 1 for family in families):
                raise AssertionError(f"{owner}: non-idempotent duplicate state")
            continue

        if text.count(anchor) != 1:
            raise AssertionError(f"{owner}: expected one insertion anchor {anchor!r}")
        if heading in text:
            raise AssertionError(f"{owner}: heading exists without reviewed body")
        if any(any(family in content for content in snapshots.values()) for family in families):
            raise AssertionError(f"{owner}: family exists without complete reviewed block")

        mechanism = f"{heading}\n\n{body}\n\n"
        updated = text.replace(anchor, mechanism + anchor, 1).rstrip() + "\n\n"
        updated += "### 2026-06-26 source-specific Review notes\n\n" + "\n".join(notes) + "\n"
        proposed[target] = updated

    for target, updated in proposed.items():
        target.write_text(updated)

    # Re-open all Books to prove each family occurs once in the expected owner
    # and every owner-merged body occurs exactly once.
    after = {path: path.read_text() for path in book_files}
    for owner, item in parsed.items():
        target = ROOT / TARGETS[owner][0]
        body = str(item["body"])
        if after[target].count(body) != 1:
            raise AssertionError(f"{owner}: merged body count mismatch after write")
        for family in item["families"]:
            hits = [path for path, content in after.items() if family in content]
            if hits != [target] or after[target].count(family) != 1:
                raise AssertionError(f"{family}: post-write uniqueness failure {hits}")

    print(f"06-26 Books write applied/verified: {len(parsed)} owners, 7 families")


if __name__ == "__main__":
    main()
