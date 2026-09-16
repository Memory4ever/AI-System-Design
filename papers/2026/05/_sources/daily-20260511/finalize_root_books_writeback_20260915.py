#!/usr/bin/env python3
"""Register the five root-owned 2026-05-11 Books writebacks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
QUEUE_PATH = SOURCE_DIR / "V3_BOOKS_WRITEBACK_QUEUE_20260914.json"
LEDGER_PATH = SOURCE_DIR / "V3_SCREENING_LEDGER_20260914.json"
EVIDENCE_PATH = SOURCE_DIR / "V3_EVIDENCE_REVIEWS_20260914.json"
CHECKPOINT_PATH = SOURCE_DIR / "V3_AUTHOR_CHECKPOINT_20260914.md"
AUTHOR_REPAIR_PATH = SOURCE_DIR / "V3_AUTHOR_REPAIR_20260915.md"
REPORT_PATH = ROOT / "papers/2026/05/11/README.md"
RECORD_PATH = SOURCE_DIR / "ROOT_BOOKS_WRITEBACK_20260915.md"
TICK = chr(96)


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load(QUEUE_PATH)
evidence = load(EVIDENCE_PATH)
owner_by_id = {item["arxiv_id"]: item["owner"] for item in evidence["items"]}
pending = [item for item in queue["items"] if item.get("write_status") == "pending_root_serialized_books_writeback"]
assert len(pending) == 5
ids = {item["arxiv_id"] for item in pending}

rows = []
for item in pending:
    owner_path = ROOT / item["target_path"]
    marker = f"semantic-body-binding:{item['source_family_id']}"
    body = owner_path.read_text()
    assert body.count(marker) == 2, (item["arxiv_id"], marker, body.count(marker))
    item["owner"] = owner_by_id[item["arxiv_id"]]
    item["write_status"] = "applied_root_serialized_books_writeback_pending_independent_review"
    item["semantic_body_marker"] = marker
    item["owner_sha256_after_writeback"] = hashlib.sha256(owner_path.read_bytes()).hexdigest()
    rows.append((item["arxiv_id"], item["owner"], item["target_path"], marker))

queue["status"] = "20_integrations_applied_pending_fresh_context_final_review"
queue["applied_count"] = 20
queue["pending_count"] = 0
dump(QUEUE_PATH, queue)

ledger = load(LEDGER_PATH)
for item in ledger["entries"]:
    if item.get("arxiv_id") in ids:
        item["books_writeback_status"] = "applied_current_worktree_pending_independent_review"
        item["root_writeback_date"] = "2026-09-15"
assert sum(
    item.get("arxiv_id") in ids
    and item.get("books_writeback_status") == "applied_current_worktree_pending_independent_review"
    for item in ledger["entries"]
) == 5
ledger["summary"]["books_integrate"] = 20
ledger["summary"]["books_applied"] = 20
ledger["summary"]["books_pending_root"] = 0
ledger["fresh_context_repair"]["root_books_writeback_pending"] = []
ledger["fresh_context_repair"]["root_books_writeback_applied"] = sorted(ids)
dump(LEDGER_PATH, ledger)

for item in evidence["items"]:
    if item.get("arxiv_id") in ids:
        item["books_writeback_status"] = "applied_current_worktree_pending_independent_review"
        item["root_writeback_date"] = "2026-09-15"
assert sum(
    item.get("arxiv_id") in ids
    and item.get("books_writeback_status") == "applied_current_worktree_pending_independent_review"
    for item in evidence["items"]
) == 5
dump(EVIDENCE_PATH, evidence)

report = REPORT_PATH.read_text()
for arxiv_id in ids:
    lines = report.splitlines()
    for index, line in enumerate(lines):
        if arxiv_id in line:
            lines[index] = line.replace("已进入 root 串行写回队列", "已由 root 写入 Books，待独立终审")
    report = "\n".join(lines) + ("\n" if report.endswith("\n") else "")
report = report.replace(
    "原有 15 个 Integrate 的 Books 正文已由前次 fresh review 通过；新增 5 个 Integrate 只进入 root 写回队列，本轮没有编辑 Books。报告保持进行中，只有 root 写回完成并由新的非作者 reviewer 验证后才能 Complete。",
    "20 个 Integrate 均已存在于当前 Books 正文：原有 15 项已由前次 fresh review 通过，新增 5 项已由 root 按 owner 写入。报告保持进行中，只有新的非作者 reviewer 验证后才能 Complete。",
)
report = report.replace("等待 root 串行写回", "已由 root 写入 Books，待独立终审")
report = report.replace(
    "1. root 按日期与目标文件冲突顺序写入 `2605.06919`、`2605.07686`、`2605.07701`、`2605.07769`、`2605.07937` 五个 queue item；本作者不编辑 Books。",
    "1. root 已按日期与目标文件冲突顺序写入 `2605.06919`、`2605.07686`、`2605.07701`、`2605.07769`、`2605.07937` 五个 queue item。",
)
report = report.replace(
    "**结论：** 未通过 Complete Gate（有界作者返修完成；等待 5 项 root 写回与 fresh review）",
    "**结论：** 进行中（有界作者返修与 20 项 Books 写回完成；等待 fresh non-author review）",
)
report = report.replace(
    "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews 与 root queue；新增本轮 comparison、root synthesis 和 author checkpoint。未编辑 Books，未 stage、commit 或 push。",
    "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews 与 root queue；新增本轮 comparison、root synthesis 和 author checkpoint，并将 5 项新命题合并到对应 Books 正文。未 stage、commit 或 push。",
)
report = report.replace(
    "前次通过的 10 个 Books 写回保持不变；新增 5 个 Integrate 仅进入 root 串行写回队列，因此本报告仍为进行中，不能在 root 写回与新的独立终审完成前标记完成。",
    "15 个 Integrate 均已存在于当前 Books 正文：前次通过的 10 项保持不变，新增 5 项已由 root 按 owner 写入；本报告仍为进行中，不能在新的独立终审完成前标记完成。",
)
report = report.replace(
    "仍有两类可执行工作，因此状态保持进行中：\n\n1. root 按日期与目标章节冲突顺序落实 5 个新增 Books 写回：`2605.07490v1`、`2605.08029v1`、`2605.08037v1`、`2605.08044v1`、`2605.08060v1`。精确 prose、位置、trade-off 与 evidence boundary 已写入 [root writeback queue](../_sources/daily-20260511/V3_BOOKS_WRITEBACK_QUEUE_20260914.json)。\n2. root 写回后，交给未参与本次修复的 reviewer 做 fresh-context 终审，复核 17 个恢复候选的准入、46 项 Evidence locator、15 项 Books 处置及真实写入。",
    "root 已按日期与目标章节冲突顺序落实 5 个新增 Books 写回；当前只剩一个可执行 Gate：交给未参与本次修复与写回的 reviewer 做 fresh-context 终审，复核 17 个恢复候选的准入、46 项 Evidence locator、15 项 Books 处置及真实正文。",
)
report = report.replace(
    "**结论：** 未通过（等待 5 个 root Books 写回与 fresh-context 终审）",
    "**结论：** 进行中（15 项 Books 写回完成，等待 fresh-context 终审）",
)
report = report.replace(
    "机器校验只验证格式与可判定一致性，不能替代下一轮独立语义终审。",
    "root 已落实 5 项新增正文；机器校验只验证格式与可判定一致性，不能替代下一轮独立语义终审。",
)
report = report.replace(
    "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews、Books root queue、作者 checkpoint、材料清单与修复记录；未编辑任何 Books 文件，未 stage、commit 或 push。",
    "**Repository Changes：** 更新本 Daily、V3 screening ledger、Evidence reviews、Books root queue、作者 checkpoint 与写回记录，并将 5 项命题合并到对应 Books 正文；未 stage、commit 或 push。",
)
REPORT_PATH.write_text(report)

checkpoint = CHECKPOINT_PATH.read_text()
checkpoint = checkpoint.replace(
    "- Books writeback: 10 Applied and preserved / 5 pending root serialized writeback",
    "- Books writeback: 20 Applied in current worktree / 0 pending root writeback",
)
checkpoint = checkpoint.replace(
    "- next: root 写入 5 个 queue items；随后由未参与修复的 reviewer 做 fresh-context 终审",
    "- next: 由未参与作者修复与 root 写回的 reviewer 做 fresh-context 终审",
)
CHECKPOINT_PATH.write_text(checkpoint)

author_repair = AUTHOR_REPAIR_PATH.read_text()
author_repair = author_repair.replace(
    "- 10 个旧 Books writeback 原样保留；新增 5 个 Integrate 只进入 root queue，本作者未编辑 Books。",
    "- 10 个旧 Books writeback 原样保留；新增 5 个 Integrate 已由 root 写入当前 Books 正文。",
)
author_repair = author_repair.replace(
    "- 当前不能标 Complete：仍需 root 写回与新的 fresh-context reviewer。",
    "- 当前不能标 Complete：root 写回已完成，仍需新的 fresh-context reviewer。",
)
AUTHOR_REPAIR_PATH.write_text(author_repair)

lines = [
    "# 2026-05-11 Root Books 写回",
    "",
    "- 执行日期：2026-09-15",
    "- 状态：新增 5/5 已写入；连同既有 15 项，共 20 项 Integrate 已在当前 Books 正文。",
    "- 下一 Gate：由未参与作者修复和 root 写回的 reviewer 做 fresh-context 终审。",
    "- Git：未 stage、commit 或 push。",
    "",
    "| arXiv | Owner | Path | Semantic marker |",
    "| --- | --- | --- | --- |",
]
for arxiv_id, owner, target_path, marker in rows:
    lines.append(f"| {TICK}{arxiv_id}{TICK} | {TICK}{owner}{TICK} | {TICK}{target_path}{TICK} | {TICK}{marker}{TICK} |")
lines += [
    "",
    "正文写回保留旧方案成立条件、约束变化、状态/控制权、代价、failure/fallback 与 exact-v1 证据边界。Marker 与 hash 只能证明可追踪性，不能替代独立语义判断。",
]
RECORD_PATH.write_text("\n".join(lines) + "\n")
