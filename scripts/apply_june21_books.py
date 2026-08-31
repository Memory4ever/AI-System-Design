#!/usr/bin/env python3
"""Guarded, idempotent root-only Books writeback for 2026-06-21.

The default mode is read-only.  ``--apply`` is intentionally required before
the twelve shared owner files are changed.  A fully applied tree is a no-op;
duplicates, mixed/partial state, marker drift, and anchor drift are hard errors.
"""

from __future__ import annotations

import argparse
import importlib.util
import os
import tempfile
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FINALIZER_PATH = ROOT / "scripts/finalize_june21_v21.py"


def load_finalizer():
    spec = importlib.util.spec_from_file_location("june21_finalizer", FINALIZER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


FINALIZER = load_finalizer()

BLOCK_TITLES = {
    "MODEL-SELF-ATTENTION": "Routing representation 与 cache representation 的条件合并",
    "TRAIN-DATA": "从 sample provenance 到训练生命周期 lineage",
    "TRAIN-GRPO": "Reward 轨迹的可推导性、感知依赖与 decision density",
    "TRAIN-DISTRIBUTED-TRAINING": "Sampling quality feedback 与通信 freshness",
    "INFER-GPU-MEMORY": "逆向硬件证据必须声明 claim provenance",
    "INFER-SCHEDULING": "Expert weights 与 KV 的联合 working set",
    "PLATFORM-EVALUATION-SYSTEM": "语言能耗、迁移基线与 threshold resolution",
    "PLATFORM-MONITORING": "Context generator 是 pre-failure sensor identity 的一部分",
    "PLATFORM-SECURITY": "Agent authority BOM、channel coverage 与 executable PoV",
    "PLATFORM-PRODUCTION": "Load test 是 SLO boundary search",
    "AGENT-WORKFLOW": "Failure attribution、perception routing 与 sticky state ownership",
    "AGENT-MULTI-AGENT": "Pairwise coupling 不能外推 group dynamics",
}


def family(aid: str) -> str:
    return f"SF-2026-ARXIV-{aid.replace('.', '-')}"


def marker(owner: str, edge: str) -> str:
    slug = owner.lower().replace("_", "-")
    return f"<!-- daily-20260621:{slug}:{edge} -->"


def integrations_by_owner() -> dict[str, list[tuple[str, dict]]]:
    grouped: dict[str, list[tuple[str, dict]]] = defaultdict(list)
    for aid, evidence in FINALIZER.C.items():
        if evidence["disposition"] == "Integrate":
            grouped[evidence["owner"]].append((aid, evidence))
    assert sum(map(len, grouped.values())) == 20
    assert set(grouped) == set(BLOCK_TITLES)
    return dict(grouped)


def build_owner_block(owner: str, items: list[tuple[str, dict]]) -> str:
    deltas = " ".join(evidence["delta"] for _, evidence in items)
    boundaries = " ".join(evidence["boundary"] for _, evidence in items)
    lines = [
        marker(owner, "start"),
        f"### {BLOCK_TITLES[owner]}",
        "",
        deltas,
        "",
        "**Trade-off、failure、共存与回退。** "
        + boundaries
        + " 旧路径在原假设成立时继续保留；新 sensor、router、artifact 或 private runtime 未通过自身 contract 时，"
        + "回退到现有 deterministic owner、supported path 或人工审批。",
        "",
        "#### Review notes",
        "",
    ]
    for aid, evidence in items:
        exact = f"https://arxiv.org/html/{aid}v1"
        lines.append(
            f"- `{family(aid)}` — primary `arXiv:{aid}v1`；exact-v1 URL=`{exact}`；"
            f"Method=`{exact} — {evidence['method']}`；"
            f"Evaluation=`{exact} — {evidence['evaluation']}`；"
            f"Non-proof=`{exact} — {evidence['limitation']}`。"
        )
    lines += [marker(owner, "end")]
    return "\n".join(lines)


def _family_hits(root: Path, source_family: str) -> list[tuple[Path, int]]:
    hits: list[tuple[Path, int]] = []
    for path in (root / "books").rglob("*.md"):
        for line_number, line in enumerate(path.read_text().splitlines(), start=1):
            if source_family in line:
                hits.append((path, line_number))
    return hits


def plan_writeback(root: Path = ROOT) -> dict[Path, str]:
    grouped = integrations_by_owner()
    expected = [(owner, aid, evidence) for owner, items in grouped.items() for aid, evidence in items]
    counts = {family(aid): _family_hits(root, family(aid)) for _, aid, _ in expected}
    duplicate = {source_family: hits for source_family, hits in counts.items() if len(hits) > 1}
    if duplicate:
        raise RuntimeError(f"duplicate Source Family write: {duplicate}")

    marker_counts = {}
    for owner in grouped:
        path = root / FINALIZER.PATHS[owner]
        text = path.read_text()
        marker_counts[owner] = (text.count(marker(owner, "start")), text.count(marker(owner, "end")))

    updates: dict[Path, str] = {}
    for owner, items in grouped.items():
        path = root / FINALIZER.PATHS[owner]
        text = path.read_text()
        owner_families = [family(aid) for aid, _ in items]
        start, end = marker(owner, "start"), marker(owner, "end")
        present = {source_family: counts[source_family] for source_family in owner_families if counts[source_family]}

        # Recovery may begin from a worktree where an earlier serialized write
        # completed one whole owner block before the repository was deleted.
        # Accept only an all-or-nothing, internally consistent owner block;
        # mixed families or partial markers still fail closed.
        if marker_counts[owner] == (1, 1):
            if text.index(start) >= text.index(end):
                raise RuntimeError(f"reversed owner markers for {owner}")
            block = text[text.index(start) : text.index(end) + len(end)]
            if set(present) != set(owner_families):
                raise RuntimeError(f"partial owner recovery for {owner}: {present}")
            for source_family in owner_families:
                expected_path = root / FINALIZER.PATHS[owner]
                if counts[source_family] != [(expected_path, counts[source_family][0][1])]:
                    raise RuntimeError(f"owner conflict for {source_family}: {counts[source_family]}")
                if block.count(source_family) != 1:
                    raise RuntimeError(f"family outside or duplicated in recovered owner block: {source_family}")
            continue
        if marker_counts[owner] != (0, 0) or present:
            raise RuntimeError(f"partial owner recovery for {owner}: families={present}, markers={marker_counts[owner]}")

        anchor = FINALIZER.TARGET_ANCHORS[owner]
        if text.splitlines().count(anchor) != 1:
            raise RuntimeError(f"anchor drift for {path}: {anchor!r}")
        block = build_owner_block(owner, items)
        needle = anchor + "\n"
        updates[path] = text.replace(needle, needle + "\n" + block + "\n", 1)
    return updates


def apply_updates(updates: dict[Path, str]) -> None:
    staged: list[tuple[Path, Path]] = []
    try:
        for path, text in updates.items():
            fd, temporary = tempfile.mkstemp(prefix=path.name + ".june21-", dir=path.parent)
            os.close(fd)
            temp_path = Path(temporary)
            temp_path.write_text(text)
            staged.append((temp_path, path))
        for temp_path, path in staged:
            os.replace(temp_path, path)
    finally:
        for temp_path, _ in staged:
            if temp_path.exists():
                temp_path.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the guarded owner blocks")
    args = parser.parse_args()
    updates = plan_writeback()
    if not updates:
        print("2026-06-21 Books writeback is already complete; no-op")
        return
    if not args.apply:
        print(f"dry-run PASS: {len(updates)} owner files are pristine and ready; use --apply only with root write lock")
        return
    apply_updates(updates)
    if plan_writeback():
        raise RuntimeError("post-apply idempotency verification failed")
    print(f"applied 20 Source Families across {len(updates)} owner files")


if __name__ == "__main__":
    main()
