#!/usr/bin/env python3
"""Record the root-owned 2026-05-05 Books writeback without signing the Daily Gate."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = HERE.parents[1] / "05" / "README.md"
QUEUE = HERE / "books-writeback-queue.json"
EVIDENCE = HERE / "V3_EVIDENCE_REVIEWS.json"
LEDGER = HERE / "V3_CANONICAL_LEDGER.json"

TARGETS = {
    "2605.01208": "books/part-04-training-system/33-grpo.md",
    "2605.01913": "books/part-06-ai-infrastructure/72-security.md",
    "2605.01959": "books/part-04-training-system/30-lora.md",
    "2605.02323": "books/part-03-multimodal-world-models/23-multimodal-representation.md",
}


def load(path: Path):
    return json.loads(path.read_text())


def dump(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


queue = load(QUEUE)
for item in queue["items"]:
    arxiv_id = item["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
    if arxiv_id not in TARGETS:
        continue
    chapter = ROOT / TARGETS[arxiv_id]
    marker = item["source_family_id"]
    body = chapter.read_text()
    assert body.count(marker) == 1
    assert body.index(marker) < body.index("\n## Review notes")
    item["status"] = "root_writeback_complete_pending_independent_review"
    item["comparison_status"] = "author_comparison_and_root_writeback_complete_pending_independent_review"
    item["post_write_chapter_sha256"] = hashlib.sha256(chapter.read_bytes()).hexdigest()
    item["semantic_body_marker_hits"] = 1
dump(QUEUE, queue)

evidence = load(EVIDENCE)
for review in evidence["reviews"]:
    if review["arxiv_id"] in TARGETS:
        review["books_decision"] = "Integrate Applied — root writeback complete; independent post-write review pending"
        review["books_writeback_status"] = "root_writeback_complete_pending_independent_review"
evidence["books_integrate_applied"] = 34
evidence["books_integrate_proposed"] = 0
evidence["status"] = "root_books_writeback_complete_independent_review_pending"
dump(EVIDENCE, evidence)

ledger = load(LEDGER)
ledger["status"] = "root_books_writeback_complete_independent_review_pending"
dump(LEDGER, ledger)

text = REPORT.read_text()
text = text.replace(
    "**Books Gate：** Open（30 项 Applied；4 项 Proposed 仍待 root 写回；109 项 No Change；写回后还需新非作者语义复核）",
    "**Books Gate：** Open（34 项 Applied；0 项 Proposed；109 项 No Change；仍待新非作者语义复核）",
)
text = text.replace(
    "作者侧判断为 30 项 `Integrate Applied`、4 项 `Integrate Proposed`、109 项 proposition-level `No Change` 与 2 项 `Blocked / Unverified`。Applied 的正文语义 marker 与 Daily trace 已由作者侧回读；Proposed 尚待 root 写回，随后仍需新的非作者 reviewer，故 Daily 未闭环。",
    "作者侧判断为 34 项 `Integrate Applied`、0 项 `Integrate Proposed`、109 项 proposition-level `No Change` 与 2 项 `Blocked / Unverified`。全部 34 项正文已写回并具有唯一语义 marker；仍需新的非作者 reviewer 回读，故 Daily 未闭环。",
)
for arxiv_id, path in TARGETS.items():
    text = text.replace(
        "完整语义增量已进入 root 写回队列，尚未写入 Books",
        "完整语义增量已由 root 写入 Books，待非作者复核",
        1,
    )
text = text.replace(
    "作者侧已完成 1058 项守恒、145 个候选证据包、评分、30 个 Applied marker 回读、4 个 root 待写回增量与 109 个 No Change 逐命题比较。root 写回和新非作者语义复核尚未完成，所以本报告保持进行中，不能解释为 Daily Complete。",
    "作者侧已完成 1058 项守恒、145 个候选证据包、评分、34 个 Applied marker 回读与 109 个 No Change 逐命题比较。root 写回已经完成；新的非作者语义复核尚未完成，所以本报告保持进行中，不能解释为 Daily Complete。",
)
REPORT.write_text(text)

record = """# 2026-05-05 Root Books 写回 — 2026-09-15

本记录只证明共享 Books 的四项语义增量已经按 owner 写入，不替代新的非作者最终复核。

- `2605.01208v1` → `TRAIN-GRPO`：reward-bound anchors 与 variance tempering 作为 Dynamic Sampling 的条件分支。
- `2605.01913v1` → `PLATFORM-SECURITY`：representation geometry 作为 fine-tuning safety drift sensor，而非 release authority。
- `2605.01959v1` → `TRAIN-LORA`：sample-conditioned rank router 纳入 adapter artifact identity 与 serving fallback。
- `2605.02323v1` → `MULTIMODAL-REPRESENTATION`：residual-evidence state 分离 slot allocation 与 factual provenance。

四个 marker 均唯一且位于章末 `## Review notes` 前；正文保留旧方案、变化约束、机制 owner、trade-off、failure、fallback 与 exact-v1 证据边界。日报保持 Ongoing，等待未参与作者修复和写回的 reviewer。
"""
(HERE / "ROOT_BOOKS_WRITEBACK_20260915.md").write_text(record)
