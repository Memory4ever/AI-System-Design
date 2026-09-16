#!/usr/bin/env python3
"""Register the root-owned second 2026-05-07 Books writeback.

The script is intentionally idempotent: it only records an already-present
chapter-body marker and never claims the independent semantic gate passed.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
QUEUE_PATH = SOURCE_DIR / "V3_SECOND_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json"
QUEUE_MD_PATH = SOURCE_DIR / "V3_SECOND_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md"
LEDGER_PATH = SOURCE_DIR / "screening-ledger-v3-author-repair.json"
PACKET_PATH = SOURCE_DIR / "exact-v1-review-packet-v3-author-repair.json"
COMPARISON_PATH = SOURCE_DIR / "books-current-content-comparison.json"
COVERAGE_PATH = SOURCE_DIR / "coverage-receipt.json"
REPORT_PATH = ROOT / "papers/2026/05/07/README.md"
RECORD_PATH = SOURCE_DIR / "ROOT_SECOND_BOOKS_WRITEBACK_20260915.md"
TICK = chr(96)


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load(QUEUE_PATH)
items = queue["items"]
ids = {item["arxiv_id"] for item in items}
assert len(items) == len(ids) == 7

rows = []
for item in items:
    owner_path = ROOT / item["target_path"]
    marker = f"semantic-body-binding:{item['source_family_id']}"
    body = owner_path.read_text()
    assert body.count(marker) == 1, (item["arxiv_id"], marker, body.count(marker))
    item["write_status"] = "applied_in_books_pending_non_author_gate"
    item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
    item["semantic_body_marker"] = marker
    item["owner_sha256_after_writeback"] = hashlib.sha256(owner_path.read_bytes()).hexdigest()
    rows.append((item["arxiv_id"], item["owner_node"], item["target_path"], marker))
queue["status"] = "root_writeback_complete_pending_non_author_gate"
queue["applied_count"] = 7
queue["pending_count"] = 0
dump(QUEUE_PATH, queue)

ledger = load(LEDGER_PATH)
for item in ledger["identities"]:
    if item.get("arxiv_id") in ids:
        item["books_writeback_status"] = "applied_in_books_pending_non_author_gate"
        item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
assert sum(
    item.get("arxiv_id") in ids
    and item.get("books_writeback_status") == "applied_in_books_pending_non_author_gate"
    for item in ledger["identities"]
) == 7
ledger["status"] = "Second author repair and root Books writeback complete; a new non-author semantic review remains pending"
ledger["second_final_author_repair"]["root_books_writeback_required"] = []
ledger["second_final_author_repair"]["root_books_writeback_applied"] = sorted(ids)
dump(LEDGER_PATH, ledger)

packet = load(PACKET_PATH)
for item in packet["items"]:
    if item.get("arxiv_id") in ids:
        item["books_writeback_status"] = "applied_in_books_pending_non_author_gate"
        item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
        item["review_gap"] = item["review_gap"].replace("整合（待 root 写回）", "整合（已落实，待独立终审）")
assert sum(
    item.get("arxiv_id") in ids
    and item.get("books_writeback_status") == "applied_in_books_pending_non_author_gate"
    for item in packet["items"]
) == 7
packet["status"] = "All author-side reviews and root Books writeback complete; a new non-author semantic review remains pending"
packet["second_final_author_repair"]["root_books_writeback_required"] = []
packet["second_final_author_repair"]["root_books_writeback_applied"] = sorted(ids)
dump(PACKET_PATH, packet)

comparison = load(COMPARISON_PATH)
for item in comparison["items"]:
    if item.get("arxiv_id") in ids:
        item["books_state"] = "applied_current_worktree"
        item["root_status"] = "applied_by_root_2026-09-15_pending_independent_review"
        item["semantic_body_marker"] = f"semantic-body-binding:{item['source_family_id']}"
assert sum(item.get("arxiv_id") in ids and item.get("books_state") == "applied_current_worktree" for item in comparison["items"]) == 7
dump(COMPARISON_PATH, comparison)

coverage = load(COVERAGE_PATH)
coverage["ledger_sha256"] = hashlib.sha256(LEDGER_PATH.read_bytes()).hexdigest()
coverage["status"] = "checked; author repair and root Books writeback complete; final semantic gate remains open"
dump(COVERAGE_PATH, coverage)

report = REPORT_PATH.read_text()
for arxiv_id in ids:
    lines = report.splitlines()
    for index, line in enumerate(lines):
        if arxiv_id in line:
            lines[index] = line.replace("整合：待 root 写回；", "整合：已落实，待独立终审；")
    report = "\n".join(lines) + ("\n" if report.endswith("\n") else "")
report = report.replace("整合（待 root 写回）：", "整合（已落实，待独立终审）：")
report = report.replace(
    "其中历史 56 项已落实，新增 7 项等待 root 依据命题级队列写回。",
    "63 项整合均已落实：历史 56 项保持不变，新增 7 项已由 root 写入当前 Books 正文；仍待独立语义终审。",
)
report = report.replace(
    "作者侧唯一剩余动作不是继续扩池，而是把新增 Books 队列交 root 合并写回，并由未参与本轮修复的 reviewer 重新检查分母、证据边界、alias 与实际正文。",
    "作者与 root 写回均已完成；唯一剩余 Gate 是由未参与本轮修复的 reviewer 重新检查分母、证据边界、alias 与实际正文。",
)
report = report.replace(
    "本轮新增 7 项只进入写回队列，尚未改动 Books。",
    "本轮新增 7 项已按 owner 合并写入 Books，并以唯一正文 marker 记录；独立语义终审尚未执行。",
)
report = report.replace(
    "第二次独立语义复核发现的漏项与 Source Family trace 问题已由作者修复，但新增 7 项 Books 写回及新的非作者验收仍未完成，状态继续保持进行中。",
    "第二次独立语义复核发现的漏项与 Source Family trace 问题已由作者修复，新增 7 项 Books 写回也已完成；新的非作者验收仍未完成，状态继续保持进行中。",
)
report = report.replace(
    "新增 7 项 Integrate 尚未写 Books，见 root queue；因此日报保持进行中。下一步只能由 root 完成写回，再由新的非作者 reviewer 验收；未 stage、commit、push。",
    "新增 7 项 Integrate 已由 root 写入 Books，见 root 写回记录；日报仍保持进行中。下一步只能由新的非作者 reviewer 验收；未 stage、commit、push。",
)
REPORT_PATH.write_text(report)

queue_md = QUEUE_MD_PATH.read_text()
queue_md = queue_md.replace(
    "作者侧只形成命题级队列，没有编辑 Books。root 应按目标章节顺序合并同章增量，避免论文列表式追加；全部写回后仍需新的独立语义终审。",
    "作者侧只形成命题级队列；root 已于 2026-09-15 按目标章节顺序合并 7 项正文增量，避免论文列表式追加。当前仍需新的独立语义终审。",
)
QUEUE_MD_PATH.write_text(queue_md)

lines = [
    "# 2026-05-07 第二轮 Root Books 写回",
    "",
    "- 执行日期：2026-09-15",
    "- 状态：7/7 已写入当前 Books 工作树；独立语义终审待执行。",
    "- 约束：root 按日期与 owner 串行写共享 Books；未 stage、commit 或 push。",
    "",
    "| arXiv | Owner | Path | Semantic marker |",
    "| --- | --- | --- | --- |",
]
for arxiv_id, node, target_path, marker in rows:
    lines.append(f"| {TICK}{arxiv_id}{TICK} | {TICK}{node}{TICK} | {TICK}{target_path}{TICK} | {TICK}{marker}{TICK} |")
lines += [
    "",
    "每一处正文均位于章末 Review notes 之前，保留旧方案/约束变化、状态或控制权、代价、failure/fallback 与 exact-v1 证据边界。机器检查只证明 marker 和账本一致，不能替代后续独立语义判断。",
]
RECORD_PATH.write_text("\n".join(lines) + "\n")
