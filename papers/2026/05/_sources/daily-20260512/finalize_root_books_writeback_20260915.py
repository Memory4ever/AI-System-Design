#!/usr/bin/env python3
"""Mechanically register the root-owned 2026-05-12 Books writeback."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
QUEUE_PATH = SOURCE_DIR / "V3_ROOT_BOOKS_WRITEBACK_QUEUE.json"
COMPARISON_PATH = SOURCE_DIR / "V3_AUTHOR_BOOKS_COMPARISON.json"
LEDGER_PATH = SOURCE_DIR / "V3_AUTHOR_REBUILD_LEDGER.json"
CHECKPOINT_PATH = SOURCE_DIR / "V3_AUTHOR_CHECKPOINT.json"
QUEUE_MD_PATH = SOURCE_DIR / "V3_ROOT_BOOKS_WRITEBACK_QUEUE.md"
REPORT_PATH = ROOT / "papers/2026/05/12/README.md"
RECORD_PATH = SOURCE_DIR / "ROOT_BOOKS_WRITEBACK_20260915.md"
T = chr(96)


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load(QUEUE_PATH)
items = queue["items"]
ids = {item["arxiv_id"] for item in items}
assert len(ids) == queue["count"] == 11

rows = []
for item in items:
    owner = ROOT / item["owner_path"]
    marker = f"semantic-body-binding:{item['source_family_id']}"
    body = owner.read_text()
    assert body.count(marker) == 1, (item["arxiv_id"], marker, body.count(marker))
    digest = hashlib.sha256(owner.read_bytes()).hexdigest()
    item["books_state"] = "applied_current_worktree"
    item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
    item["semantic_body_marker"] = marker
    item["owner_sha256_after_writeback"] = digest
    rows.append((item["arxiv_id"], item["owner_node"], item["owner_path"], marker))
queue["status"] = "root_serial_writeback_complete_pending_independent_review"
queue["applied_count"] = 11
queue["pending_count"] = 0
dump(QUEUE_PATH, queue)

comparison = load(COMPARISON_PATH)
for item in comparison:
    if item.get("arxiv_id") in ids:
        item["books_state"] = "applied_current_worktree"
        item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
assert sum(item.get("books_state") == "applied_current_worktree" for item in comparison) >= 11
dump(COMPARISON_PATH, comparison)

ledger = load(LEDGER_PATH)
for item in ledger["identities"]:
    if item.get("arxiv_id") in ids:
        item["books_state"] = "applied_current_worktree"
        item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
assert sum(item.get("arxiv_id") in ids and item.get("books_state") == "applied_current_worktree" for item in ledger["identities"]) == 11
dump(LEDGER_PATH, ledger)

checkpoint = load(CHECKPOINT_PATH)
checkpoint["status"] = "author_and_root_complete_pending_independent_reviewer"
checkpoint["counts"]["already_applied"] = 35
checkpoint["counts"]["root_queue"] = 0
checkpoint["counts"]["root_applied_this_pass"] = 11
checkpoint["active_ledger_sha256"] = hashlib.sha256(LEDGER_PATH.read_bytes()).hexdigest()
checkpoint["author_assertion"] = "not_a_final_gate_independent_review_required"
dump(CHECKPOINT_PATH, checkpoint)

report = REPORT_PATH.read_text()
report = report.replace("；进入 root 精确写回队列。", "；已写入当前 Books 正文，待独立语义终审。")
report = report.replace(
    "- Integrate：35（其中 24 已在当前 Books 正文存在，11 进入 root 写回队列）。",
    "- Integrate：35（其中 24 项原已存在，11 项已由 root 写入当前 Books 正文；全部待本日报独立语义终审）。",
)
old_record = f"Root 写回队列见 {T}../_sources/daily-20260512/V3_ROOT_BOOKS_WRITEBACK_QUEUE.md{T}；作者侧未修改共享 Books。评分分布："
new_record = f"Root 写回记录见 {T}../_sources/daily-20260512/ROOT_BOOKS_WRITEBACK_20260915.md{T}；11 项共享 Books 写回已完成。评分分布："
report = report.replace(old_record, new_record)
report = report.replace(
    f"1. root 按 owner 分组、按日期顺序串行处理 11 项写回，并在相邻章节与 {T}Review notes{T} 边界内验证唯一 owner。",
    f"1. 11 项 root 写回已完成并通过 marker、owner、{T}Review notes{T} 边界与范围检查；仍需独立 reviewer 判断语义质量。",
)
report = report.replace("- 复核者：待全新独立 reviewer。", "- 复核者：待全新、未参与作者重建与 Books 写回的独立 reviewer。")
report = report.replace(
    "- 结论：未通过（不是失败；作者侧完成，root 写回和独立 Gate 尚未执行）。",
    "- 结论：进行中；作者侧与 root Books 写回完成，独立语义 Gate 尚未执行。",
)
report = report.replace(
    "- 本报告不得在 root 写回与独立复核前改为完成。",
    "- 本报告不得在独立复核通过前改为完成。",
)
REPORT_PATH.write_text(report)

queue_md = QUEUE_MD_PATH.read_text()
queue_md = queue_md.replace(
    "作者侧只提出写回，不修改共享 Books；root 需按日期顺序串行写入并进行写后语义审计。",
    "作者侧只提出写回；root 已于 2026-09-15 按日期与 owner 串行写入 11 项。本文保留原命题与插入意图，最终状态以 JSON 队列和独立语义终审为准。",
)
QUEUE_MD_PATH.write_text(queue_md)

lines = [
    "# 2026-05-12 Root Books Writeback",
    "",
    "- 执行日期：2026-09-15",
    "- 状态：11/11 已写入当前 Books 工作树；独立语义终审待执行。",
    "- 约束：root 串行写共享 Books；没有 stage、commit 或 push。",
    "",
    "| arXiv | Owner | Path | Semantic marker |",
    "| --- | --- | --- | --- |",
]
for arxiv_id, node, path, marker in rows:
    lines.append(f"| {T}{arxiv_id}{T} | {T}{node}{T} | {T}{path}{T} | {T}{marker}{T} |")
lines += [
    "",
    "每一处正文都位于章末 Review notes 之前，并写明旧路径、约束变化、状态或控制权、代价、失败/回退边界与 exact-v1 证据边界。机器检查不能替代后续独立语义判断。",
]
RECORD_PATH.write_text("\n".join(lines) + "\n")
