#!/usr/bin/env python3
"""Synchronize 2026-05-21 after the recorded 39-item root writeback."""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/21/README.md"


def load(name: str):
    return json.loads((HERE / name).read_text())


def dump(name: str, value) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load("root-books-writeback-queue-v3.json")
queue_ids = {item["arxiv_id"] for item in queue["items"]}
assert len(queue_ids) == queue["queue_count"] == 39

books = load("books-comparison-v3.json")
pending = {item["arxiv_id"]: item for item in books["integrate_root_queue"]}
assert set(pending) == queue_ids

applied = list(books["applied_existing"])
for item in queue["items"]:
    family = item["source_family_id"]
    target = ROOT / item["target_path"]
    text = target.read_text()
    start_marker = f"<!-- semantic-body-binding:{family}:start -->"
    end_marker = f"<!-- semantic-body-binding:{family}:end -->"
    assert text.count(start_marker) == text.count(end_marker) == 1, family
    assert text.index(start_marker) < text.index(end_marker)
    review_pos = text.find("\n## Review notes")
    assert review_pos < 0 or text.index(end_marker) < review_pos, family
    source = pending[item["arxiv_id"]]
    applied.append({
        **source,
        "marker": f"semantic-body-binding:{family}",
        "marker_pair_unique": True,
        "before_review_notes": True,
        "writeback_receipt": "ROOT_BOOKS_WRITEBACK_39_ITEMS_20260915.md",
        "status": "root_applied_pending_different_fresh_non_author_review",
    })
    item["status"] = "root_applied_pending_different_fresh_non_author_review"

books["applied_existing"] = applied
books["integrate_root_queue"] = []
books["applied_existing_count"] = 65
books["integrate_root_queue_count"] = 0
books["root_applied_pending_fresh_review_count"] = 45
books["author_did_not_edit_books"] = True
books["gate"] = (
    "all 45 root bindings are applied; a different fresh non-author semantic review remains"
)
assert len(books["applied_existing"]) == 65
assert 65 + books["no_change_count"] + books["report_only_count"] == books["candidate_count"]
dump("books-comparison-v3.json", books)

queue["root_applied_pending_fresh_review"] = 39
queue["status"] = "root_writeback_applied_pending_different_fresh_non_author_review"
dump("root-books-writeback-queue-v3.json", queue)

text = REPORT.read_text()
for aid in sorted(queue_ids):
    start = text.index(f"### [{aid} ")
    match = re.search(r"\n### \[|\n## ", text[start + 1 :])
    end = len(text) if match is None else start + 1 + match.start()
    block = text[start:end]
    block = block.replace("Books 决定：Integrate — Root Queue", "Books 决定：Applied — root writeback，等待 fresh semantic review")
    block = block.replace("当前 Books 决定：Integrate — Root Queue", "当前 Books 决定：Applied — root writeback，等待 fresh semantic review")
    text = text[:start] + block + text[end:]

for aid in sorted(queue_ids):
    pattern = rf"(\| \[{re.escape(aid)} .*?\| )整合：待 root 串行写入( [^|]+\|)"
    text, count = re.subn(pattern, r"\1整合：当前正文 binding 已存在，等待 fresh semantic review\2", text)
    assert count == 1, (aid, count)

text = text.replace(
    "Books 对账为 `177 = 26 Applied + 16 No Change + 96 Report Only + 39 pending Integrate`。",
    "Books 对账为 `177 = 65 Applied + 16 No Change + 96 Report Only + 0 pending Integrate`。",
)
text = text.replace(
    "另 6 个新增 deep false negative 也进入 root queue。",
    "另 6 个新增 deep false negative 也已由 root 写入；45 个 root binding 均等待 fresh semantic review。",
)
text = text.replace(
    "2. root 已串行完成 ZCube 与 2605.20309/20316/20476/20740/20856 共 6 项旧队列写回；本轮新增 39 项 queue 尚待 root 串行处理。",
    "2. root 已串行完成 ZCube、5 个 fresh restoration 与新增 39 项，共 45 项共享 Books 写回；当前只剩不同 fresh non-author 的写后语义 Gate。",
)
text = text.replace(
    "Root writeback Gate：PENDING（39 项）；最终 fresh semantic Gate：PENDING。",
    "Root writeback Gate：PASS（45 项）；最终 fresh semantic Gate：PENDING。",
)
text = text.replace(
    "`26 Applied + 16 No Change + 96 Report Only + 39 Integrate`",
    "`65 Applied + 16 No Change + 96 Report Only + 0 Integrate`",
)
REPORT.write_text(text)

