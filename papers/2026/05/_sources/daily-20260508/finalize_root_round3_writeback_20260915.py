#!/usr/bin/env python3
"""Close the root-owned 2026-05-08 Round-3 Books writeback stage."""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE = HERE / "ROOT_BOOKS_WRITEBACK_QUEUE_ROUND3_20260915.json"
RECERT = HERE / "V3_RECERTIFICATION.json"
REPORT = ROOT / "papers/2026/05/08/README.md"

queue = json.loads(QUEUE.read_text())
recert = json.loads(RECERT.read_text())

for action in queue["actions"]:
    sf = action["source_family_id"]
    path = ROOT / action["file"]
    text = path.read_text()
    if sf not in text:
        raise SystemExit(f"missing Books binding for {sf} in {path}")
    review_pos = text.find("\n## Review notes")
    if review_pos >= 0 and text.find(sf) > review_pos:
        raise SystemExit(f"{sf} appears after Review notes")
    action["root_status"] = "applied_current_worktree_pending_fresh_non_author_review"
    action["root_writeback_date"] = "2026-09-15"

# Verify the two requested narrative moves, not just marker existence.
embedding = (ROOT / "books/part-02-model/12-embedding.md").read_text()
if not (embedding.index("## 初始表示不等于上下文表示") < embedding.index("SF-2026-ARXIV-2605-06216")):
    raise SystemExit("TIDE block is still before the embedding baseline")
generation = (ROOT / "books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md").read_text()
if not (generation.index("## Diffusion：用迭代修正换并行状态更新") < generation.index("SF-2026-ARXIV-2605-06548")):
    raise SystemExit("continuous latent diffusion block is still before the diffusion baseline")

by_id = {item["arxiv_id"]: item for item in recert["items"]}
for arxiv_id in ("2605.05329", "2605.05331", "2605.06609", "2605.06660"):
    by_id[arxiv_id]["books_disposition"] = "Integrate — Applied; independent post-write review pending"
    by_id[arxiv_id]["books_writeback_status"] = "applied_by_root_2026-09-15_pending_fresh_review"
for arxiv_id in ("2605.06216", "2605.06548"):
    by_id[arxiv_id]["books_disposition"] = "Integrate — Applied; chapter order corrected; independent post-write review pending"
    by_id[arxiv_id]["books_writeback_status"] = "reordered_by_root_2026-09-15_pending_fresh_review"

queue["status"] = "root_writeback_complete_pending_fresh_non_author_review"
recert["status"] = "Ongoing — author repair and root Books writeback complete; fresh non-author final review pending"
recert["final_independent_signoff"] = False
recert["root_round3_writeback"] = {
    "status": "complete_pending_fresh_non_author_review",
    "date": "2026-09-15",
    "insertions": 4,
    "chapter_order_moves": 2,
}
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
RECERT.write_text(json.dumps(recert, ensure_ascii=False, indent=2) + "\n")

text = REPORT.read_text()
replacements = {
    "作者定点返修 Round 3 已完成；等待 root 执行 4 项 Books 写入与 2 项章内重排，再由新的非作者 reviewer 终审":
        "作者定点返修 Round 3 与 root 的 4 项 Books 写入、2 项章内重排均已完成；等待新的非作者 reviewer 终审",
    "49 项既有 `Integrate — Applied`、16 项已由 root 写入但尚待独立 post-write review、4 项 `Integrate — Root writeback required`，以及 63 项 `No Change — Existing Coverage`":
        "69 项 `Integrate — Applied`（均待本轮新的非作者最终复核）以及 63 项 `No Change — Existing Coverage`",
    "49 项 Books 已落实、16 项已写回待终审、4 项等待 root 写回":
        "69 项 Books 已落实并等待新的非作者终审",
    "等待 root 写回": "已由 root 写回，待非作者终审",
    "已写回但需 root 重排后终审": "已由 root 完成章内重排，待非作者终审",
    "已写回，但正文需 root 移至初始表示 baseline 之后再终审": "已由 root 完成章内重排，待非作者终审",
    "已写回，但正文需 root 移至 Diffusion 基础机制之后再终审": "已由 root 完成章内重排，待非作者终审",
    "当前阻断不是材料访问。Round 3 新增 4 项长期语义增量等待 root 写入，`2605.06216` 与 `2605.06548` 等待按演进顺序重排；完成后必须由未参与本轮修复与写回的 reviewer 检查 132/487 分流、4 个新增命题、2 个移动块、16 个上一轮写回命题与 63 个 No Change locator。修复作者和 root 都不能自签。":
        "当前阻断不是材料访问。Round 3 的 4 项长期语义增量与 `2605.06216`、`2605.06548` 的章内重排均已由 root 落实；现在只剩未参与修复与写回的 reviewer 检查 132/487 分流、4 个新增命题、2 个移动块、此前写回命题与 63 个 No Change locator。修复作者和 root 都不能自签。",
    "1. root 按 [Round 3 Books 队列](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_ROUND3_20260915.json) 完成 4 项插入与 2 项移动；\n2. 由未参与本轮作者修复与 root 写回的新 reviewer 复核变化范围及 `619 = 132 + 487` 分流；":
        "1. 由未参与本轮作者修复与 root 写回的新 reviewer 复核变化范围及 `619 = 132 + 487` 分流；",
    "49 Applied + 16 written-pending-review + 4 root-writeback-required + 63 No Change":
        "69 Applied-pending-review + 63 No Change",
    "但 4 项 Books 写回和 2 项章内重排尚未执行，也尚未通过最终 Gate":
        "且 4 项 Books 写回和 2 项章内重排已执行，但尚未通过最终 Gate",
    "root 尚需执行 4 项 Books 写入与 2 项章内重排；随后由未参与本轮修复和写回的 reviewer 独立检查变化范围":
        "root 已执行 4 项 Books 写入与 2 项章内重排；现在由未参与本轮修复和写回的 reviewer 独立检查变化范围",
    "Books 写回、重排与新的非作者终审仍未完成":
        "Books 写回与重排已经完成，新的非作者终审仍未完成",
    "root 后续动作被严格限定为 [Round 3 Books 写入/重排队列](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_ROUND3_20260915.json)：4 项新插入与 2 项既有块移动。作者没有编辑 Books，也不签署最终通过。":
        "root 已严格按 [Round 3 Books 写入/重排队列](../_sources/daily-20260508/ROOT_BOOKS_WRITEBACK_QUEUE_ROUND3_20260915.json) 完成 4 项新插入与 2 项既有块移动。作者与 root 都不签署最终通过。",
}
for old, new in replacements.items():
    text = text.replace(old, new)
REPORT.write_text(text)

audit = """# 2026-05-08 Root Round-3 Books Writeback

- 4/4 新机制已写入 canonical owner chapter。
- `2605.06216` 已移动到初始表示/上下文表示 baseline 之后。
- `2605.06548` 已移动到 Diffusion 基础机制之后。
- 6 个 source-family marker 均位于 `Review notes` 之前。
- 当前只剩 fresh non-author final review；root 不自签 Gate。
"""
(HERE / "ROOT_ROUND3_BOOKS_WRITEBACK_20260915.md").write_text(audit)
print(json.dumps({"insertions": 4, "moves": 2, "status": queue["status"]}, ensure_ascii=False))
