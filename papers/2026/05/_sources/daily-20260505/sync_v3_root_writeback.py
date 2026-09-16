#!/usr/bin/env python3
"""Synchronize verified root Books writebacks into the 2026-05-05 V3 evidence state."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
LEDGER_PATH = HERE / "V3_CANONICAL_LEDGER.json"
EVIDENCE_PATH = HERE / "V3_EVIDENCE_REVIEWS.json"
QUEUE_PATH = HERE / "books-writeback-queue.json"
QUEUE_MD_PATH = HERE / "V3_BOOKS_REVIEW_QUEUE.md"

APPLIED = {
    "SF-2026-ARXIV-2605-01302",
    "SF-2026-ARXIV-2605-01345",
    "SF-2026-ARXIV-2605-01772",
    "SF-2026-ARXIV-2605-02178",
    "SF-2026-ARXIV-2605-02263",
    "SF-2026-ARXIV-2605-02411",
}

RESTORED_IDS = {
    "2605.00884", "2605.01191", "2605.01302", "2605.01345", "2605.01772",
    "2605.01799", "2605.01896", "2605.01948", "2605.02178", "2605.02262",
    "2605.02263", "2605.02411", "2605.02525", "2605.02697", "2605.02757",
}


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def dump(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


ledger = load(LEDGER_PATH)
evidence = load(EVIDENCE_PATH)
queue = load(QUEUE_PATH)

queue_by_family = {item["source_family_id"]: item for item in queue["items"]}
assert APPLIED <= queue_by_family.keys()

for family in APPLIED:
    item = queue_by_family[family]
    chapter = ROOT / item["target_chapter_path"]
    text = chapter.read_text()
    body_marker = f"semantic-body-binding:{family}"
    trace_marker = f"daily-books-trace:{family}:start"
    assert text.count(body_marker) == 1, (family, "semantic body marker", text.count(body_marker))
    assert text.count(trace_marker) == 1, (family, "daily trace marker", text.count(trace_marker))
    item["post_write_chapter_sha256"] = hashlib.sha256(chapter.read_bytes()).hexdigest()
    item["semantic_body_marker_hits"] = 1
    item["daily_trace_marker_hits"] = 1
    item["comparison_status"] = "root_writeback_complete_independent_post_write_review_pending"
    item["status"] = "applied_post_write_review_pending"

for entry in ledger["entries"]:
    if entry["arxiv_id"] in RESTORED_IDS:
        entry["withdrawal_status"] = "no withdrawal notice observed in exact-v1 review as of 2026-09-14"
    if entry["source_family_id"] in APPLIED:
        entry["books_decision"] = "Integrate Applied — root writeback complete; independent post-write review pending"

for review in evidence["reviews"]:
    if review["source_family_id"] in APPLIED:
        review["books_decision"] = "Integrate Applied — root writeback complete; independent post-write review pending"
        review["existing_marker_hits"] = 1

review_list = evidence["reviews"]
blocked = sum(item["review_status"] == "blocked_exact_v1_html" for item in review_list)
deep = sum(item["review_status"] == "deep_complete_author" for item in review_list)
standard = sum(item["review_status"] == "standard_complete_author" for item in review_list)
applied = sum(item["books_decision"].startswith("Integrate Applied") for item in review_list)
proposed = sum(item["books_decision"].startswith("Integrate Proposed") for item in review_list)
no_change = sum(item["books_decision"].startswith("No Change") for item in review_list)
assert deep + standard + blocked == len(review_list)
assert applied + proposed + no_change + blocked == len(review_list)
assert proposed == 0

status = "false_negative_author_repair_books_applied_independent_review_pending"
ledger["status"] = status
evidence.update(
    status=status,
    candidate_count=len(review_list),
    review_complete=len(review_list) - blocked,
    deep_complete=deep,
    standard_complete=standard,
    blocked=blocked,
    books_integrate_applied=applied,
    books_integrate_proposed=proposed,
    books_no_change=no_change,
)

queue_lines = [
    "# 2026-05-05 V3 Books 写回记录",
    "",
    "本文件是 `books-writeback-queue.json` 的可读投影。root 已完成本轮 6 项写回；marker 与相邻交接已经作者侧回读，但仍需新的非作者 reviewer 做写后语义复核。",
    "",
    "| Source Family | Owner / 目标 | 状态 | 精确插入位置 |",
    "| --- | --- | --- | --- |",
]
for item in queue["items"]:
    queue_lines.append(
        f"| `{item['source_family_id']}` | `{item['stable_node_id']}` / `{item['target_chapter_path']}` | `{item['status']}` | {item['current_chapter_locator']} |"
    )
queue_lines.extend(["", "## 本轮 6 项完整语义增量", ""])
for item in queue["items"]:
    if item["source_family_id"] not in APPLIED:
        continue
    queue_lines.extend([
        f"### `{item['source_family_id']}`",
        "",
        item["new_delta_after_compare"],
        "",
        f"**证据边界：** {item['evidence_boundary']}",
        "",
        f"**写回校验：** semantic-body marker = {item['semantic_body_marker_hits']}；Daily trace marker = {item['daily_trace_marker_hits']}；非作者写后语义复核待执行。",
        "",
    ])

dump(LEDGER_PATH, ledger)
dump(EVIDENCE_PATH, evidence)
dump(QUEUE_PATH, queue)
QUEUE_MD_PATH.write_text("\n".join(queue_lines) + "\n")

print(json.dumps({
    "raw": ledger["raw_identity_count"],
    "retained": len(review_list),
    "closure": ledger["counts"]["pre_denominator_closure_reviewed"],
    "deep": deep,
    "standard": standard,
    "blocked": blocked,
    "applied": applied,
    "proposed": proposed,
    "no_change": no_change,
}, ensure_ascii=False))
