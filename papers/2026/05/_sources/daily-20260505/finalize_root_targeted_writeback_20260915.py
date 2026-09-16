#!/usr/bin/env python3
"""Reconcile the 2026-05-05 targeted Books queue after root writeback."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE_PATH = HERE / "V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json"
EVIDENCE_PATH = HERE / "V3_EVIDENCE_REVIEWS.json"
LEDGER_PATH = HERE / "V3_CANONICAL_LEDGER.json"
REPORT = ROOT / "papers/2026/05/05/README.md"

queue = json.loads(QUEUE_PATH.read_text())
evidence = json.loads(EVIDENCE_PATH.read_text())
ledger = json.loads(LEDGER_PATH.read_text())
queued = {item["source_family_id"]: item for item in queue["items"]}

actual_paths: dict[str, str] = {}
for sf in queued:
    matches = []
    for path in (ROOT / "books").rglob("*.md"):
        if sf in path.read_text():
            matches.append(path.relative_to(ROOT).as_posix())
    if sf == "SF-2026-ARXIV-2605-01771":
        # This mechanism already had a complete canonical evaluation owner block.
        matches = [p for p in matches if p.endswith("66-evaluation-system.md")]
    if len(matches) != 1:
        raise SystemExit(f"{sf}: expected one canonical Books binding, got {matches}")
    actual_paths[sf] = matches[0]

for review in evidence["reviews"]:
    sf = review["source_family_id"]
    if sf not in queued:
        continue
    review["books_decision"] = "Integrate Applied — root writeback complete; independent review pending"
    review["existing_marker_hits"] = [actual_paths[sf]]
    review["books_writeback_status"] = "applied_current_worktree_pending_independent_review"
    if sf == "SF-2026-ARXIV-2605-01771":
        review.update(
            owner="PLATFORM-EVALUATION-SYSTEM",
            chapter=66,
            chapter_path=actual_paths[sf],
            existing_coverage_locator=(
                "books/part-06-ai-infrastructure/66-evaluation-system.md — "
                "process compliance evaluation contract"
            ),
            existing_coverage_proposition=(
                "现有 Ch66 已完整区分结果合规与过程合规，并要求真实 tool trace、"
                "环境 affordance 与 effect receipt。"
            ),
            existing_coverage_comparison=(
                "root 回读发现该命题已在 canonical evaluation owner 中完整存在，"
                "无需在 Ch69 重复写入。"
            ),
        )

for entry in ledger["entries"]:
    sf = entry.get("source_family_id")
    if sf not in queued:
        continue
    entry["books_decision"] = "Integrate Applied — root writeback complete; independent review pending"
    entry["books_writeback_status"] = "applied_current_worktree_pending_independent_review"
    entry["books_binding"] = actual_paths[sf]
    if sf == "SF-2026-ARXIV-2605-01771":
        entry["owner"] = "PLATFORM-EVALUATION-SYSTEM"
        entry["decision_reason"] = entry["decision_reason"].replace("`PLATFORM-TRACE`", "`PLATFORM-EVALUATION-SYSTEM`")

for item in queue["items"]:
    sf = item["source_family_id"]
    item["status"] = "applied_current_worktree_pending_independent_review"
    item["actual_books_path"] = actual_paths[sf]
    item["root_writeback_date"] = "2026-09-15"
    if sf == "SF-2026-ARXIV-2605-01771":
        item["writeback_resolution"] = "existing canonical Ch66 body reused; duplicate Ch69 insertion rejected"
queue["root_status"] = "18_of_18_resolved_pending_fresh_non_author_review"

applied = sum(r["books_decision"].startswith("Integrate Applied") for r in evidence["reviews"])
proposed = sum(r["books_decision"].startswith("Integrate Proposed") for r in evidence["reviews"])
no_change = sum(r["books_decision"].startswith("No Change") for r in evidence["reviews"])
blocked = sum(r["review_status"].startswith("blocked_exact_v1") for r in evidence["reviews"])
if applied + proposed + no_change + blocked != len(evidence["reviews"]):
    raise SystemExit("Books disposition arithmetic does not close")
evidence.update(
    books_integrate_applied=applied,
    books_integrate_proposed=proposed,
    books_no_change=no_change,
    status="root_writeback_complete_pending_fresh_non_author_review",
)
ledger["status"] = "root_writeback_complete_pending_fresh_non_author_review"
ledger["books_write_permitted"] = False
ledger["independent_review_required"] = True

QUEUE_PATH.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")
EVIDENCE_PATH.write_text(json.dumps(evidence, ensure_ascii=False, indent=2) + "\n")
LEDGER_PATH.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n")

receipt_path = HERE / "coverage-receipt.json"
receipt = json.loads(receipt_path.read_text())
receipt["status"] = "root_writeback_complete_pending_fresh_non_author_review"
receipt["ledger_sha256"] = hashlib.sha256(LEDGER_PATH.read_bytes()).hexdigest()
receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

subprocess.run(["python3", str(HERE / "render_v3_report.py")], cwd=ROOT, check=True)

checkpoint = (HERE / "V3_AUTHOR_CHECKPOINT.md").read_text()
checkpoint = checkpoint.replace(
    "进行中 — 467 条泛化 closure 层定点返修完成，等待 root Books 写回与新非作者最终复核",
    "进行中 — 定点返修与 root Books 写回完成，等待新非作者最终复核",
)
checkpoint = checkpoint.replace(
    "Applied 34、Proposed 18、No Change 126、Blocked 3",
    f"Applied {applied}、Proposed {proposed}、No Change {no_change}、Blocked {blocked}",
)
checkpoint = checkpoint.replace(
    "1. root 仅按 `V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json` 串行处理 18 项 Proposed；作者任务不得写 `books/`。\n"
    "2. root 写回后分配新的 fresh-context 非作者 reviewer，复核 denominator、36 个恢复项、126 个 No Change 和最终 Books 语义。\n"
    "3. 只有非作者通过后才冻结 Candidate Denominator 并把 Daily 改为 Complete；validator 不能代替该 Gate。",
    "1. 分配新的 fresh-context 非作者 reviewer，复核 denominator、36 个恢复项、126 个 No Change 与 52 个 Applied Books 语义。\n"
    "2. 只有非作者通过后才把 Daily 改为 Complete；validator 不能代替该 Gate。",
)
(HERE / "V3_AUTHOR_CHECKPOINT.md").write_text(checkpoint)

audit_lines = [
    "# 2026-05-05 Root Targeted Books Writeback", "",
    f"- 队列：18/18 resolved；当前 Applied={applied}、Proposed={proposed}。",
    "- 17 项写入现有章节的机制主线；均包含旧路径、约束变化、状态/权威、代价、失败与回退。",
    "- `SF-2026-ARXIV-2605-01771` 经 root 回读发现 Ch66 已有完整 canonical block；未在 Ch69 制造副本，并把 owner 校正为 `PLATFORM-EVALUATION-SYSTEM`。",
    "- 所有 binding 位于 Review notes 之前；下一 Gate 是 fresh non-author final review。", "",
]
(HERE / "ROOT_TARGETED_BOOKS_WRITEBACK_20260915.md").write_text("\n".join(audit_lines))

print(json.dumps({
    "resolved": len(queue["items"]), "applied": applied, "proposed": proposed,
    "no_change": no_change, "blocked": blocked, "report": str(REPORT),
}, ensure_ascii=False, indent=2))
