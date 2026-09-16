#!/usr/bin/env python3
"""Apply the root-owned 2026-05-08 semantic queue, then leave final review open."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = HERE.parents[1] / "08" / "README.md"
QUEUE = HERE / "BOOKS_WRITEBACK_QUEUE_FINAL_CLOSURE_REPAIR.json"
RECERT = HERE / "V3_RECERTIFICATION.json"


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load(QUEUE)
for item in queue["items"]:
    chapter = ROOT / item["owner_path"]
    marker = f"<!-- semantic-body-binding:{item['source_family_id']} -->"
    text = chapter.read_text()
    if marker not in text:
        anchor = item["insertion_anchor"]
        assert text.count(anchor) == 1, (item["arxiv_id"], anchor, text.count(anchor))
        paragraph = (
            item["semantic_increment"].strip()
            + "\n\n"
            + item["evidence_boundary"].strip()
            + " "
            + item["handoff"].strip()
            + "\n\n"
            + marker
            + "\n\n"
        )
        text = text.replace(anchor, paragraph + anchor, 1)
        chapter.write_text(text)
    text = chapter.read_text()
    assert text.count(marker) == 1
    assert text.index(marker) < text.index("\n## Review notes")
    item["status"] = "root_writeback_complete_pending_independent_review"
    item["owner_path_sha256_after_write"] = hashlib.sha256(chapter.read_bytes()).hexdigest()
    item["semantic_body_marker_hits"] = 1
dump(QUEUE, queue)

recert = load(RECERT)
for item in recert["items"]:
    if any(q["arxiv_id"] == item.get("arxiv_id") for q in queue["items"]):
        item["books_disposition"] = "Integrate — Applied; independent post-write review pending"
recert["status"] = "Ongoing — all 16 root Books writebacks complete; independent semantic review pending"
recert["final_independent_signoff"] = False
repair = recert["final_closure_repair"]
repair["books_integrate_root_writeback_required"] = 0
repair["books_integrate_applied_after_this_repair"] = 65
repair["root_writeback_completed"] = 16
repair["final_independent_signoff"] = False
dump(RECERT, recert)

text = REPORT.read_text()
for item in queue["items"]:
    text = text.replace(
        f"待 root 写回：`{item['stable_node_id']}`",
        f"已由 root 写回，待非作者复核：`{item['stable_node_id']}`",
    )
text = text.replace(
    "- **Books：** 49 `Integrate — Applied` + 16 `Integrate — Root writeback required` + 63 `No Change — Existing Coverage`。",
    "- **Books：** 65 `Integrate — Applied` + 0 `Integrate — Root writeback required` + 63 `No Change — Existing Coverage`。",
)
text = text.replace(
    "- **尚未闭合：** root 必须按 [Books writeback queue](../_sources/daily-20260508/BOOKS_WRITEBACK_QUEUE_FINAL_CLOSURE_REPAIR.json) 串行写入 16 项；随后由未参与本轮修复和写回的 reviewer 独立检查变化范围。修复作者与 root 均不能自签。",
    "- **尚未闭合：** 16 项 Books 写回已完成；仍须由未参与本轮修复和写回的 reviewer 独立检查变化范围。修复作者与 root 均不能自签。",
)
text = text.replace(
    "当前唯一阻断不是材料访问：root 仍需按结构化队列把 16 项长期语义增量串行写入共享 Books；写回完成后，必须由未参与本轮修复与写回的 reviewer 检查 22 个重开项、16 个正文命题、6 个 No Change locator 以及修复后的 128/491 分流。修复作者和 root 都不能自签。",
    "当前唯一阻断不是材料访问：16 项长期语义增量已由 root 串行写入共享 Books；必须由未参与本轮修复与写回的 reviewer 检查 22 个重开项、16 个正文命题、6 个 No Change locator 以及修复后的 128/491 分流。修复作者和 root 都不能自签。",
)
REPORT.write_text(text)

lines = [
    "# 2026-05-08 Root Books 写回 — 2026-09-15",
    "",
    "本记录只证明结构化队列的 16 项长期语义增量已写入唯一 owner；不替代非作者最终复核。",
    "",
]
for item in queue["items"]:
    lines.append(f"- `{item['arxiv_id']}v1` → `{item['stable_node_id']}` / `{item['owner_path']}`")
lines += [
    "",
    "所有 marker 唯一且位于各章唯一 `## Review notes` 前；正文来自已审阅 semantic increment，并同时保留 exact-v1 evidence boundary 与章节 handoff。日报保持 Ongoing，等待 fresh-context reviewer。",
]
(HERE / "ROOT_FINAL_CLOSURE_BOOKS_WRITEBACK_20260915.md").write_text("\n".join(lines) + "\n")
