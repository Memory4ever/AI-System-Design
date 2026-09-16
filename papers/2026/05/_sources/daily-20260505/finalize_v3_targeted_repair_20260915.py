#!/usr/bin/env python3
"""Render comparison/checkpoint/receipt after the bounded author repair."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ledger_path = HERE / "V3_CANONICAL_LEDGER.json"
evidence_path = HERE / "V3_EVIDENCE_REVIEWS.json"
ledger = json.loads(ledger_path.read_text())
evidence = json.loads(evidence_path.read_text())
reviews = evidence["reviews"]

comparison = [
    "# 2026-05-05 V3 Proposition-level Books Comparison", "",
    "状态：作者侧对照完成；Proposed 等待 root 写回，全部结果等待 fresh-context 非作者最终复核。", "",
]
for r in reviews:
    comparison += [f"## `{r['source_family_id']}` — {r['title']}", ""]
    if r["review_status"].startswith("blocked_exact_v1"):
        comparison += [f"- 状态：`Blocked / Unverified`；所需材料：{r.get('material_request', 'exact-v1 正文')}。", ""]
        continue
    comparison += [
        f"- Owner：`{r['owner']}` / Ch{r['chapter']} / `{r['chapter_path']}`。",
        f"- 现有命题：{r.get('existing_coverage_proposition', '已按实际章节定位完成对照。')}",
        f"- 差异判断：{r.get('existing_coverage_comparison', '未发现会改变长期 owner 或章节交接的新命题。')}",
        f"- 处置：`{r['books_decision']}`。", "",
    ]
(HERE / "V3_PROPOSITION_BOOKS_COMPARISON.md").write_text("\n".join(comparison) + "\n")

counts = ledger["counts"]
checkpoint = f"""# 2026-05-05 V3 作者阶段 checkpoint

**状态：** `进行中 — 467 条泛化 closure 层定点返修完成，等待 root Books 写回与新非作者最终复核`。本文件不能解释为 Daily Complete。

## 当前守恒

- Raw identity：1058；Candidate Denominator：{counts['semantic_reviewed_retain_frozen']}；pre-denominator closure：{counts['pre_denominator_closure_reviewed']}；待判定：0。
- Evidence Review：Deep {evidence['deep_complete']}、Standard {evidence['standard_complete']}、Terminal Blocked {evidence['blocked']}。
- Books 处置：Applied {evidence['books_integrate_applied']}、Proposed {evidence['books_integrate_proposed']}、No Change {evidence['books_no_change']}、Blocked {evidence['blocked']}。
- 既有 `2605.01208`、`2605.01913`、`2605.01959`、`2605.02323` 已由 canonical ledger 的 Proposed 同步为 Applied；未新增 Books 正文写入。

## 本轮定点恢复

- 未重扫 1058 个 raw identity。
- reviewer 指定的 467 条共享泛化 closure 层中恢复 33 个 false negative、重新确认 434 个 closure。
- reviewer 另点名的 3 个非共享理由 closure 同步恢复；合计恢复 36 个 candidate。
- 36 个恢复项中，35 个取得 official exact-v1 HTML 并完成 section-level evidence；`2605.02196v1` 的 HTML 404 且 PDF 未完整取得，保持 Blocked。

## 精确下一步

1. root 仅按 `V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json` 串行处理 {evidence['books_integrate_proposed']} 项 Proposed；作者任务不得写 `books/`。
2. root 写回后分配新的 fresh-context 非作者 reviewer，复核 denominator、36 个恢复项、126 个 No Change 和最终 Books 语义。
3. 只有非作者通过后才冻结 Candidate Denominator 并把 Daily 改为 Complete；validator 不能代替该 Gate。
"""
(HERE / "V3_AUTHOR_CHECKPOINT.md").write_text(checkpoint)

receipt = {
    "source_id": "SRC-ARXIV",
    "window": "[2026-05-04T09:00:00+08:00,2026-05-05T09:00:00+08:00)",
    "route": "canonical owner replay over the preserved 1058 identities; bounded 467-layer title+abstract semantic repair; official exact-v1 HTML/PDF for evidence",
    "raw_identity_count": 1058,
    "raw_identity_rescanned": False,
    "semantic_screened": 1058,
    "retained": counts["semantic_reviewed_retain_frozen"],
    "pre_denominator_closed": counts["pre_denominator_closure_reviewed"],
    "review_complete": evidence["review_complete"],
    "blocked": evidence["blocked"],
    "ledger_sha256": hashlib.sha256(ledger_path.read_bytes()).hexdigest(),
    "status": "author_repair_complete_pending_root_writeback_and_independent_review",
}
(HERE / "coverage-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")

queue = json.loads((HERE / "V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.json").read_text())
queue_md = [
    "# 2026-05-05 V3 定点 Books root 写回队列", "",
    "状态：作者侧 Proposed；只能由 root 按章节冲突顺序写入，写后必须经过新的非作者语义复核。", "",
]
for item in queue["items"]:
    queue_md += [
        f"## `{item['source_family_id']}` → `{item['stable_node_id']}`", "",
        f"- 来源：{item['primary_source']}",
        f"- 目标：`{item['target_chapter_path']}`",
        f"- 现有覆盖：{item['current_content_finding']}",
        f"- 所需增量：{item['new_delta_after_compare']}",
        f"- 证据边界：{item['evidence_boundary']}",
        f"- 状态：`{item['status']}`。", "",
    ]
(HERE / "V3_TARGETED_ROOT_BOOKS_WRITEBACK_QUEUE_20260915.md").write_text("\n".join(queue_md) + "\n")

print(json.dumps({
    "raw": 1058, "retained": receipt["retained"], "closure": receipt["pre_denominator_closed"],
    "review_complete": receipt["review_complete"], "blocked": receipt["blocked"],
    "applied": evidence["books_integrate_applied"], "proposed": evidence["books_integrate_proposed"],
    "no_change": evidence["books_no_change"], "root_queue": len(queue["items"]),
}, ensure_ascii=False, indent=2))
