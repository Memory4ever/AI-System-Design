#!/usr/bin/env python3
"""Record the single 2026-05-05 bounded Books writeback."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
REPORT = ROOT / "papers/2026/05/05/README.md"
BOOK = ROOT / "books/part-04-training-system/31-rlhf.md"
QUEUE = HERE / "V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json"
LEDGER = HERE / "V3_CANONICAL_LEDGER.json"
EVIDENCE = HERE / "V3_EVIDENCE_REVIEWS.json"

sf = "SF-2026-ARXIV-2605-02375"
lines = BOOK.read_text().splitlines()
hits = [i + 1 for i, line in enumerate(lines) if sf in line]
if len(hits) != 1:
    raise SystemExit(f"expected one Books binding for {sf}, got {hits}")

queue = json.loads(QUEUE.read_text())
queue["root_status"] = "1_applied_pending_fresh_non_author_minimal_review"
queue["items"][0]["status"] = "applied_current_worktree_pending_fresh_non_author_minimal_review"
queue["items"][0]["source_binding_line"] = hits[0]
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

ledger = json.loads(LEDGER.read_text())
ledger["status"] = "root_writeback_complete_pending_fresh_non_author_minimal_review"
for entry in ledger["entries"]:
    if entry.get("arxiv_id") == "2605.02375":
        entry["books_disposition"] = "Integrate — Applied; fresh non-author minimal review pending"
        entry["books_writeback_status"] = "applied_by_root_2026-09-15_pending_fresh_review"
LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

evidence = json.loads(EVIDENCE.read_text())
evidence["status"] = "root_writeback_complete_pending_fresh_non_author_minimal_review"
evidence["books_integrate_proposed"] = 0
evidence["books_integrate_applied"] = 53
for review in evidence["reviews"]:
    if review.get("arxiv_id") == "2605.02375":
        review["books_disposition"] = "Integrate — Applied; fresh non-author minimal review pending"
        review["books_writeback_status"] = "applied_by_root_2026-09-15_pending_fresh_review"
EVIDENCE.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")

text = REPORT.read_text()
replacements = {
    "Open（52 项 Applied；128 项 No Change；1 项 Integrate Proposed 待 root 写回；全部来源已完成作者侧 Evidence Review，仍待新的非作者最小范围终审）":
        "Open（53 项 Applied；128 项 No Change；root 写回已完成，仍待新的非作者最小范围终审）",
    "52 项 `Integrate Applied`、128 项 proposition-level `No Change`、1 项 `Integrate Proposed`，`Blocked / Unverified` 为 0。":
        "53 项 `Integrate Applied`、128 项 proposition-level `No Change`，`Blocked / Unverified` 为 0。",
    "Daily 仍保持进行中，仅等待 root 写回 `2605.02375v1` 的单项语义增量，以及之后由未参与本次返修者执行最小范围终审。":
        "Daily 仍保持进行中；`2605.02375v1` 的单项语义增量已由 root 写回，现在仅等待未参与本次返修者执行最小范围终审。",
    "整合 Proposed：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；待 root 在 reverse-KL 演进段内写回，随后由非作者复核":
        "整合 Applied：`TRAIN-RLHF` / [Ch31](../../../../books/part-04-training-system/31-rlhf.md)；待 fresh non-author 最小范围复核",
    "Integrate Proposed — root writeback and independent review required":
        "Integrate Applied — root writeback complete; fresh non-author minimal review pending",
    "本轮新增的唯一待办是 [2605.02375v1 root 写回队列](../_sources/daily-20260505/V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json)：root 写回后须交给未参与本次返修的 reviewer 做最小范围终审。":
        "本轮 [2605.02375v1 root 写回队列](../_sources/daily-20260505/V3_BOUNDED_REPAIR_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json) 已落实；现在交给未参与本次返修的 reviewer 做最小范围终审。",
    "52 Applied + 128 No Change + 1 Proposed、0 Blocked":
        "53 Applied + 128 No Change、0 Blocked",
    "报告仍保持进行中，因为 `2605.02375v1` 尚待 root 写回，之后还需新的非作者最小范围终审。":
        "报告仍保持进行中；`2605.02375v1` 已由 root 写回，现在还需新的非作者最小范围终审。",
}
for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f"report replacement source missing: {old[:80]}")
    text = text.replace(old, new)
REPORT.write_text(text)

(HERE / "ROOT_BOUNDED_REPAIR_BOOKS_WRITEBACK_20260915.md").write_text(
    "# 2026-05-05 Root Bounded Repair Books Writeback\n\n"
    "- `SF-2026-ARXIV-2605-02375` was integrated into the existing reverse-KL evolution section in Ch31.\n"
    "- The writeback records binary-reward degeneracy, filtered-target support mismatch, misspecification, trade-offs and exact-v1 boundaries.\n"
    "- Root did not self-sign the Gate; fresh non-author minimal review remains required.\n"
)
print(json.dumps({"applied": 1, "binding_line": hits[0], "status": queue["root_status"]}, ensure_ascii=False))
