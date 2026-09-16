#!/usr/bin/env python3
"""Synchronize 2026-05-22 after the nine root-owned Books writebacks."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/22/README.md"
QUEUE = HERE / "BOOKS_WRITEBACK_QUEUE_V3.json"
COMPARISON = HERE / "books-current-content-comparison-v3.json"

FAMILIES = {
    "SF-2026-ARXIV-2605-21751",
    "SF-2026-ARXIV-2605-21770",
    "SF-2026-ARXIV-2605-21849",
    "SF-2026-ARXIV-2605-21933",
    "SF-2026-ARXIV-2605-22060",
    "SF-2026-ARXIV-2605-22211",
    "SF-2026-ARXIV-2605-22644",
    "SF-2026-ARXIV-2605-22723",
    "SF-2026-ARXIV-2605-22733",
}


queue = json.loads(QUEUE.read_text(encoding="utf-8"))
for item in queue["items"]:
    if item.get("source_family_id") in FAMILIES:
        item["status"] = "root_writeback_complete_pending_fresh_nonauthor_review"
        item["postwrite_marker"] = f"semantic-body-binding:{item['source_family_id']}"
queue["queue_count"] = 0
queue["status"] = "9 bounded-closure-repair Integrates applied; overall report Ongoing pending fresh non-author review"
queue["books_gate"] = (
    "46 root bindings are present. The nine bounded-closure-repair deltas now require a fresh post-write semantic review; "
    "the overall report remains Ongoing until the independent final Gate passes."
)
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

comparison = json.loads(COMPARISON.read_text(encoding="utf-8"))
for item in comparison:
    if item.get("source_family_id") in FAMILIES:
        item["decision"] = "Integrate — root applied, pending fresh post-write semantic review"
        item["writeback_status"] = "root_writeback_complete_pending_fresh_nonauthor_review"
COMPARISON.write_text(json.dumps(comparison, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

text = REPORT.read_text(encoding="utf-8")
text = text.replace(
    "Books 总投影为 `245 = 46 Integrate（37 既有已写回 + 9 新 queue）+ 145 No Change + 54 Report Only + 0 Deferred`。新增 9 项只进入 root serialized queue，本作者未编辑共享 Books。日报保持进行中，需 root 写回、另一 fresh non-author 逐项做 post-write/closure challenge 后才可 Complete。",
    "Books 总投影为 `245 = 46 Applied + 145 No Change + 54 Report Only + 0 Deferred + 0 pending Integrate`。其中 37 项沿用已通过写后复核的当前 binding，新增 9 项已由 root 串行写入并保留成对 marker。日报保持进行中，需另一 fresh non-author 逐项做 post-write/closure challenge 后才可 Complete。",
)
for family in sorted(FAMILIES):
    arxiv_id = family.removeprefix("SF-2026-ARXIV-").replace("-", ".", 1)
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if arxiv_id in line and line.startswith("| ["):
            lines[index] = line.replace("整合：root queue 待写回", "整合：当前正文 binding 已存在", 1)
            break
    text = "\n".join(lines) + "\n"

text = re.sub(
    r"- \[`BOOKS_WRITEBACK_QUEUE_V3\.json`\].*?只能由 root 串行写共享 Books，随后由未参与写作的人做 post-write 语义复核。",
    "- [`BOOKS_WRITEBACK_QUEUE_V3.json`](../_sources/daily-20260522/BOOKS_WRITEBACK_QUEUE_V3.json) 中 9 个 active Integrate 已由 root 串行写入：`2605.21751`、`2605.21770`、`2605.21849`、`2605.21933`、`2605.22060`、`2605.22211`、`2605.22644`、`2605.22723`、`2605.22733`；当前只等待未参与写作的人做 post-write 语义复核。",
    text,
    count=1,
)
text = text.replace(
    "- 当前 Gate：**Ongoing**。剩余且仅剩：root 写回 9 项 Books；不同 fresh non-author 做写后语义与全量 final Gate；通过后再同步 Complete/receipt/checkpoint。",
    "- 当前 Gate：**Ongoing**。root 已写回 9 项 Books；剩余且仅剩不同 fresh non-author 的写后语义与全量 final Gate，通过后再同步 Complete/receipt/checkpoint。",
)
REPORT.write_text(text, encoding="utf-8")

for item in queue["items"]:
    if item.get("source_family_id") not in FAMILIES:
        continue
    body = (ROOT / item["target_path"]).read_text(encoding="utf-8")
    start = f"<!-- semantic-body-binding:{item['source_family_id']}:start -->"
    end = f"<!-- semantic-body-binding:{item['source_family_id']}:end -->"
    if body.count(start) != 1 or body.count(end) != 1 or body.index(start) > body.index(end):
        raise RuntimeError(f"invalid paired binding: {item['source_family_id']}")

print("synchronized nine root Books writebacks; 05-22 remains Ongoing pending fresh review")
