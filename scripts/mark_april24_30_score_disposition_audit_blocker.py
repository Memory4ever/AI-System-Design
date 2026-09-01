#!/usr/bin/env python3
"""Record the author-side score/disposition coupling blocker for 2026-04-24..30."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAYS = range(24, 31)
BLOCKED_STATUS = "blocked_pending_independent_score_override_books_reaudit"
FINDING = (
    "All 211 retained rows score 7-9; every provisional Integrate row uses "
    "Review Override=knowledge_gap while every provisional No Change row uses none, "
    "and every Deep Analysis eligibility row includes potential_books_delta. This "
    "perfect coupling is not acceptable evidence-stage scoring: knowledge_gap must "
    "be established from exact-v1 evidence before Books disposition and cannot be "
    "inferred backward from Integrate. A different reviewer must independently "
    "re-score Review Override, Deep eligibility, and Books disposition before any "
    "queue item is eligible for serial writeback."
)


def dump(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


for day in DAYS:
    date = f"2026-04-{day:02d}"
    packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
    readme = ROOT / f"papers/2026/04/{day:02d}/README.md"

    queue_path = packet / "BOOKS_WRITEBACK_QUEUE.json"
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    for item in queue.get("items", []):
        item["status"] = BLOCKED_STATUS
        item["finding_ref"] = "score-disposition-coupling-author-finding.json"
    queue["status"] = BLOCKED_STATUS
    queue["gate_effect"] = "Books Gate remains Open; no item is eligible for root serial writeback."
    queue["finding_ref"] = "score-disposition-coupling-author-finding.json"
    dump(queue_path, queue)

    audit_path = packet / "semantic-author-audit.json"
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    findings = audit.setdefault("unresolved_findings", [])
    if FINDING not in findings:
        findings.insert(0, FINDING)
    audit["books_queue_eligibility"] = "blocked"
    audit["books_queue_blocker_ref"] = "score-disposition-coupling-author-finding.json"
    dump(audit_path, audit)

    receipt = {
        "schema": "author-finding-v1",
        "report_date": date,
        "scope": "Score V2 / Review Override / Deep Analysis eligibility / Books disposition ordering",
        "status": "unresolved",
        "finding": FINDING,
        "observed_global_counts": {
            "retained_rows": 211,
            "score_7_9_rows": 211,
            "provisional_integrate_rows": 183,
            "integrate_with_knowledge_gap_override": 183,
            "provisional_no_change_rows": 28,
            "no_change_with_none_override": 28,
            "deep_eligibility_with_potential_books_delta": 211,
        },
        "resolution_required": (
            "Fresh-context reviewer must independently derive Score V2 and knowledge_gap "
            "from exact-v1 evidence before re-running Deep selection and current-content "
            "Books comparison. Existing queue items are provisional and must not be written."
        ),
        "gate_effect": "Coverage, Evidence, and Books remain Open; queue is blocked.",
        "shared_books_modified": False,
    }
    dump(packet / "score-disposition-coupling-author-finding.json", receipt)

    text = readme.read_text(encoding="utf-8")
    text = text.replace(
        f"author packet 已完成，等待不同 reviewer 的 fresh-context audit；Books queue={len(queue.get('items', []))}，未修改共享 Books。",
        f"author packet 存在未解决 score/disposition coupling finding；provisional Books queue={len(queue.get('items', []))} 已阻断、不得串行写回；未修改共享 Books。",
    )
    text = text.replace(
        f"Integrate queue={len(queue.get('items', []))}。",
        f"provisional Integrate queue={len(queue.get('items', []))}，因 score/override/disposition 顺序 finding 不具备写回资格。",
    )
    marker = "## 7. Semantic Audit"
    note = (
        "Author finding：211/211 分数均为 7–9，183 个 provisional Integrate 恰好全部使用 "
        "`knowledge_gap` override、28 个 No Change 恰好全部为 `none`，且全部 Deep eligibility "
        "带 `potential_books_delta`。该完全耦合不能证明 Evidence-stage 独立判定；在不同 reviewer "
        "从 exact-v1 重判 Score/override/Deep/Books 前，现有 queue 仅为 blocked provisional artifact，"
        "不得交给 root 写回。收据：`score-disposition-coupling-author-finding.json`。\n\n"
    )
    if note not in text:
        text = text.replace(marker, note + marker)
    readme.write_text(text, encoding="utf-8")

