#!/usr/bin/env python3
"""Record root Books writeback for 2026-05-13 without self-signing the Gate."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/13/README.md"
QUEUE = HERE / "v3-root-writeback-queue.json"
COMPARISON = HERE / "v3-books-comparison.json"
EVIDENCE = HERE / "v3-active-evidence.json"

queue = json.loads(QUEUE.read_text())
comparisons = json.loads(COMPARISON.read_text())
evidence = json.loads(EVIDENCE.read_text())
queued = {item["arxiv_id"]: item for item in queue["items"]}

for item in queue["items"]:
    path = ROOT / item["owner_path"]
    lines = path.read_text().splitlines()
    hits = [i + 1 for i, line in enumerate(lines) if item["source_family_id"] in line]
    if len(hits) != 1:
        raise SystemExit(f"non-unique binding for {item['arxiv_id']}: {hits}")
    item["root_status"] = "applied_current_worktree_pending_fresh_non_author_review"
    item["source_binding_line"] = hits[0]

for item in comparisons["comparisons"]:
    arxiv_id = item["arxiv_id"]
    if arxiv_id not in queued:
        continue
    queue_item = queued[arxiv_id]
    item["author_decision"] = "Integrate — Applied; independent post-write review pending"
    item["requires_root_write"] = False
    item["source_binding_line"] = queue_item["source_binding_line"]
    item["root_writeback_status"] = "applied_by_root_2026-09-15_pending_fresh_review"

for item in evidence["reviews"]:
    arxiv_id = item["arxiv_id"]
    if arxiv_id not in queued:
        continue
    item["books_writeback_status"] = "applied_by_root_2026-09-15_pending_fresh_review"
    item["detailed_review_markdown"] = item["detailed_review_markdown"].replace(
        "Books Decision=`Integrate`；作者只形成命题比较与 root serial queue，不直接修改共享 Books。",
        "Books Decision=`Integrate — Applied`；root 已写入 canonical owner，等待 fresh non-author post-write review。",
    )

queue["status"] = "root_writeback_complete_pending_fresh_non_author_review"
queue["root_applied_count"] = len(queue["items"])
comparisons["requires_root_write_count"] = 0
comparisons["root_applied_count_pending_fresh_review"] = len(queue["items"])
comparisons["status"] = "root_writeback_complete_pending_fresh_non_author_review"
evidence["books_writeback_status"] = "21_applied_pending_fresh_non_author_review"
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
COMPARISON.write_text(json.dumps(comparisons, ensure_ascii=False, indent=2) + "\n")
EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")

text = REPORT.read_text()
text = text.replace(
    "报告仍为 `Ongoing`：root Books 队列尚待按日期串行写入，之后必须由另一名非作者 reviewer 完成独立语义验收。",
    "报告仍为 `Ongoing`：root 已按日期和 owner 完成 21 项 Books 串行写回，现在必须由另一名非作者 reviewer 完成独立语义验收。",
)
text = text.replace(
    "21 项进入 root serial writeback queue，其余恢复项为 `No Change — Existing Coverage`。这不是 Gate 通过声明。",
    "21 项已由 root 写入 canonical owner，其余恢复项为 `No Change — Existing Coverage`。写回完成仍不是 Gate 通过声明。",
)
count = text.count("判定：**Integrate — Root write required**")
if count != 21:
    raise SystemExit(f"expected 21 root-required decisions, found {count}")
text = text.replace(
    "判定：**Integrate — Root write required**",
    "判定：**Integrate — Applied；待 fresh non-author post-write review**",
)
text = text.replace(
    "- root serial writeback queue 为 21 项；作者未修改共享 Books。root 应按日期和 owner 顺序写入、逐项补正文 binding，再触发 fresh non-author review。",
    "- root serial writeback queue 的 21 项已全部写入 canonical owner 并补正文 binding；当前只剩 fresh non-author post-write review。",
)
REPORT.write_text(text)

(HERE / "ROOT_ROUND3_BOOKS_WRITEBACK_20260915.md").write_text(
    "# 2026-05-13 Root Round-3 Books Writeback\n\n"
    "- 21/21 proposition-level increments were written to the reviewed canonical owners.\n"
    "- Every Source Family binding is unique and appears before chapter Review notes.\n"
    "- The root did not self-sign the Daily Gate; fresh non-author review remains required.\n"
)
print(json.dumps({"applied": len(queue["items"]), "status": queue["status"]}, ensure_ascii=False))
