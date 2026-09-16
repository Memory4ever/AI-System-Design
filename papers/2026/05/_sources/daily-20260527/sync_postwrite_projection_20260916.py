#!/usr/bin/env python3
"""Synchronize the 2026-05-27 date-local projection after root Books writeback.

This is intentionally bounded: it does not alter screening, evidence, scores,
the root queue, or shared Books.  It only makes the report and comparison
artifacts describe the already-present sixteen semantic body bindings.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/27/README.md"


def load(name: str):
    return json.loads((HERE / name).read_text())


def dump(name: str, value) -> None:
    (HERE / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load("root-books-writeback-queue-v3.json")
queue_ids = {item["arxiv_id"] for item in queue["items"]}
assert len(queue_ids) == 16
assert queue["pending_count"] == 0
assert all(item["status"] == "applied_pending_fresh_review" for item in queue["items"])

for filename in ("books-comparison-v3.json", "books-current-content-comparison.json"):
    books = load(filename)
    seen = set()
    for item in books["items"]:
        if item["arxiv_id"] not in queue_ids:
            continue
        seen.add(item["arxiv_id"])
        item["decision"] = "Applied"
        item["binding_marker"] = (
            f"<!-- semantic-body-binding:{item['source_family_id']}:start -->"
        )
        item["author_check"] = (
            "Root writeback is present as one paired semantic-body binding before "
            "the first main H2 Review notes; semantic final Gate remains fresh-review pending."
        )
    assert seen == queue_ids
    books["applied_count"] = 57
    books["no_change_count"] = 32
    books["pending_integrate_count"] = 0
    assert sum(item["decision"] == "Applied" for item in books["items"]) == 57
    assert sum(item["decision"].startswith("No Change") for item in books["items"]) == 32
    dump(filename, books)

audit = load("author-adversarial-audit-v3.json")
audit["status"] = "root_writeback_applied_pending_fresh_non_author_review"
audit["challenges"]["books"] = (
    "57 current-body bindings + 32 No Change decisions with exact main-body "
    "heading/excerpt; the sixteen root bindings are applied and await fresh semantic review"
)
audit["gates"]["books"] = "ROOT_WRITEBACK_APPLIED_PENDING_FRESH_SEMANTIC_REVIEW"
audit["gates"]["fresh_non_author"] = "PENDING"
dump("author-adversarial-audit-v3.json", audit)

text = REPORT.read_text()
for aid in sorted(queue_ids):
    start = text.index(f"### [{aid} ")
    match = re.search(r"\n### \[|\n## ", text[start + 1 :])
    end = len(text) if match is None else start + 1 + match.start()
    block = text[start:end]
    block = block.replace("`Integrate`", "`Applied`")
    block = block.replace(
        "Current main body does not carry the adopted delta; root serialized writeback is required.",
        "Root writeback is present as one paired semantic-body binding before the first main H2 Review notes; semantic final Gate remains fresh-review pending.",
    )
    text = text[:start] + block + text[end:]

for aid in sorted(queue_ids):
    pattern = rf"(\| \[{re.escape(aid)} .*?\| )整合：待 root 串行写回( \[章节\])"
    text, count = re.subn(pattern, r"\1整合：当前正文 binding 已存在\2", text)
    assert count == 1, (aid, count)

text = text.replace(
    "当前可执行 Books Gate 是 root 按 [`root-books-writeback-queue-v3.json`](../_sources/daily-20260527/root-books-writeback-queue-v3.json) 串行写回 16 项；写回后必须由不同 fresh non-author",
    "16 项 root Books 写回已落实；当前可执行 Books Gate 是由不同 fresh non-author",
)
text = text.replace(
    "- **结论：** 未通过最终 Gate（author repair 已完成；16 项 root Books writeback 与 fresh Gate pending）。",
    "- **结论：** 未通过最终 Gate（author repair 与 16 项 root Books writeback 已完成；fresh Gate pending）。",
)
REPORT.write_text(text)

checkpoint = HERE / "AUTHOR_V3_RECERTIFICATION_CHECKPOINT_20260916.md"
cp = checkpoint.read_text()
appendix = """

## Root writeback 后续状态（2026-09-16）

本节取代上文的 16 项 pending 状态：root 已完成全部 16 项共享 Books 写回，当前投影为
`57 Applied + 32 No Change + 0 pending Integrate`。`root-books-writeback-queue-v3.json`
的 16 项均为 `applied_pending_fresh_review`；下一步只剩不同 fresh non-author 对 603 项 closure、
89 项 Evidence/score、32 项 No Change 与 57 项正文 binding 做最终语义 Gate。不得重复写 Books。
"""
if "## Root writeback 后续状态（2026-09-16）" not in cp:
    checkpoint.write_text(cp.rstrip() + appendix)

