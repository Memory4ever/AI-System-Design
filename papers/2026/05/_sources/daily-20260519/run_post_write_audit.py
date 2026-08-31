#!/usr/bin/env python3
"""Independent post-write semantic audit for the 2026-05-19 Books queue.

This script only writes date-local receipts and the Daily README. It never
modifies shared Books.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE_PATH = HERE / "BOOKS_WRITEBACK_QUEUE.json"
README_PATH = ROOT / "papers/2026/05/19/README.md"
AUDITED_AT = "2026-09-01T09:37:05+08:00"

TARGET_H2 = {
    "2605.17821": "## 保存频率是故障成本权衡",
    "2605.17842": "## Build-time 与 Runtime-time",
    "2605.17862": "## RLHF 的系统成本",
    "2605.17877": "## Sequence reward 与 token updates 的错位",
    "2605.17879": "## 从随机 Fault Injection 到可定位的 Accelerator Sensor",
    "2605.17889": "## 专用加速器首先是一份 Workload Contract",
    "2605.17923": "## Variable-length Batch 让并行计划成为 Runtime State",
    "2605.17989": "## Online Retrieval Pipeline",
    "2605.17992": "## Online Retrieval Pipeline",
    "2605.17998": "## Recovery 与 Verification 必须产生不同 Artifact",
    "2605.18053": "## KV Cache 的生命周期",
    "2605.18106": "## Optimizer 不是与参数化无关的旋钮",
    "2605.18498": "## Scorer 不是绝对真相",
    "2605.18565": "## 评估 Memory",
    "2605.18710": "## 并行策略怎样消费通信原语",
    "2605.18750": "## 异步 Pipeline：去掉 Bubble 会把成本移到参数版本",
    "2605.19008": "## 训练稳定性是多层系统问题",
    "2605.19049": "## 与第19章的职责边界",
}

queue = json.loads(QUEUE_PATH.read_text())
items = queue["items"]
assert len(items) == 18

receipts = []
for item in items:
    aid = item["arxiv_id"]
    sf = item["source_family_id"]
    owner = ROOT / item["owner_path"]
    lines = owner.read_text().splitlines()
    marker_lines = [i + 1 for i, line in enumerate(lines) if sf in line]
    review_lines = [i + 1 for i, line in enumerate(lines) if re.fullmatch(r"## Review notes\s*", line)]
    summary_lines = [i + 1 for i, line in enumerate(lines) if re.fullmatch(r"## 小结\s*", line)]
    assert len(marker_lines) == 1
    assert review_lines and summary_lines
    assert summary_lines[-1] < marker_lines[0] < review_lines[0]
    for adjacent in item["adjacent_paths"]:
        assert (ROOT / adjacent).is_file()
    assert TARGET_H2[aid] in lines

    finding_id = f"PW-20260519-{aid.replace('.', '-')}-FLOW"
    finding = (
        f"机制正文位于 `{item['owner_path']}` 的 `## 小结` 之后（marker line "
        f"{marker_lines[0]}，Review notes line {review_lines[0]}）。内容本身包含旧路径、约束变化、"
        "owner、收益/成本、failure、fallback 与 exact-v1 边界，但总结之后再开启新机制，破坏章内演进与退出契约。"
    )
    resolution = (
        f"将完整段落与 marker 归入 `{TARGET_H2[aid]}` 的正文演进链，并保持在 `## 小结` 之前；"
        "移动后由不同 reviewer 重读 owner 与相邻章。不得只移动 marker 或把段落留在总结之后。"
    )
    receipts.append({
        "arxiv_id": aid,
        "source_family_id": sf,
        "stable_node_id": item["stable_node_id"],
        "owner_path": item["owner_path"],
        "adjacent_paths_read": item["adjacent_paths"],
        "marker_count": 1,
        "marker_line": marker_lines[0],
        "summary_line": summary_lines[-1],
        "first_exact_h2_review_notes_line": review_lines[0],
        "before_review_notes": True,
        "after_chapter_summary": True,
        "semantic_checks": {
            "old_path_why_reasonable": True,
            "changed_constraint": True,
            "state_or_control_owner": True,
            "benefit_and_cost": True,
            "failure_mode": True,
            "evidence_boundary": True,
            "fallback_or_coexistence": True,
            "owner_and_adjacent_consistent": True,
            "chapter_flow_consistent": False,
        },
        "finding_id": finding_id,
        "finding": finding,
        "required_resolution": resolution,
        "status": "open",
    })
    item["status"] = "post_write_finding_open"
    item["post_write_audit_ref"] = f"post-write-semantic-audit.json#{sf}"
    item["post_write_finding_id"] = finding_id
    item["post_write_required_resolution"] = resolution

queue["status"] = "post_write_audit_open_18_flow_findings"
queue["post_write_audited_at"] = AUDITED_AT
queue["post_write_counts"] = {
    "denominator": 18,
    "marker_and_owner_structure_passed": 18,
    "semantic_content_complete": 18,
    "chapter_flow_passed": 0,
    "passed": 0,
    "open": 18,
}
QUEUE_PATH.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "books-post-write-semantic-audit-v1",
    "report_date": "2026-05-19",
    "auditor": "fresh-context:may2026-day01",
    "audited_at": AUDITED_AT,
    "scope": "18/18 items from BOOKS_WRITEBACK_QUEUE.json",
    "books_modified_by_auditor": False,
    "cross_model_review": "skipped — non-interactive subtask",
    "counts": {
        "denominator": 18,
        "owner_adjacent_marker_structure_passed": 18,
        "semantic_content_complete": 18,
        "chapter_flow_passed": 0,
        "semantic_passed": 0,
        "semantic_open": 18,
    },
    "gate_result": {
        "completion_status": "In Progress",
        "books_gate": "Open",
        "unresolved_findings": 18,
    },
    "items": receipts,
}
(HERE / "post-write-semantic-audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
)

text = README_PATH.read_text()
text = text.replace(
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立语义审计已完成，等待 root 串行 Books 写回与不同写作者 post-write audit。",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。18/18 已写入并完成 post-write audit；内容字段完整，但全部位于各章 `## 小结` 之后，18 项章内流程 finding 待修复。",
)
text = text.replace(
    "独立 reviewer 重放 703/703 个 registered identities：author denominator 46 中移除 20 个 false positive，恢复 34 个 false negative，最终 denominator=60、pre-denominator closures=643。60/60 exact-v1 Review 完成，blocked=0、ordinary pending=0；31 项 provisional Books queue 经 current owner+adjacent challenge 收紧为 18 项。共享 Books 未修改。",
    "独立 reviewer 重放 703/703 个 registered identities：author denominator 46 中移除 20 个 false positive，恢复 34 个 false negative，最终 denominator=60、pre-denominator closures=643。60/60 exact-v1 Review 完成，blocked=0、ordinary pending=0；31 项 provisional Books queue 经 current owner+adjacent challenge 收紧为 18 项并已写回。post-write audit 确认 18/18 owner、相邻章、marker、机制字段和 exact-v1 boundary 正确，但 18 项全部位于 `## 小结` 之后，破坏章节演进与退出契约，因此 Books Gate 保持 Open。",
)
old_row = "| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17734 | FINDING-BOOKS-WRITEBACK-20260519: 18 owner-merged deltas not yet written | root serial writeback then different-writer post-write audit | open |"
new_row = "| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17821; books-review:SF-2026-ARXIV-2605-19049 | PW-20260519-2605-17821-FLOW;PW-20260519-2605-17842-FLOW;PW-20260519-2605-17862-FLOW;PW-20260519-2605-17877-FLOW;PW-20260519-2605-17879-FLOW;PW-20260519-2605-17889-FLOW;PW-20260519-2605-17923-FLOW;PW-20260519-2605-17989-FLOW;PW-20260519-2605-17992-FLOW;PW-20260519-2605-17998-FLOW;PW-20260519-2605-18053-FLOW;PW-20260519-2605-18106-FLOW;PW-20260519-2605-18498-FLOW;PW-20260519-2605-18565-FLOW;PW-20260519-2605-18710-FLOW;PW-20260519-2605-18750-FLOW;PW-20260519-2605-19008-FLOW;PW-20260519-2605-19049-FLOW | post-write-semantic-audit.json：18/18 内容字段完整，但 chapter flow 0/18；完整机制段均须移到 `## 小结` 之前的对应演进节点 | open |"
assert old_row in text
text = text.replace(old_row, new_row)
text = text.replace(
    "由 root 按 owner 合并 18 项 Books queue，避免逐论文追加；完成后由不同写作者执行 owner+adjacent post-write semantic audit。",
    "Root 按 post-write-semantic-audit.json 的逐项 target H2，把 18 个完整机制段归入 `## 小结` 之前的章节演进链；随后由不同 reviewer 重读 owner+adjacent 与章内退出契约。",
)
text = text.replace(
    "- 未修改共享 Books；未 stage、commit 或 push。",
    "- Root 已写回共享 Books；本 post-write reviewer 未修改 Books，也未 stage、commit 或 push。",
)
text = text.replace(
    "- 18 项 owner-merged queue 写回后，正文能否在 Review notes 前唯一承载旧路径、约束变化、owner、trade-off、failure 与 fallback？",
    "- 18 个完整机制段归位到对应 H2 后，能否在 `## 小结` 前形成连续演进，并保持相邻章节 owner 边界？",
)
text = text.replace("unresolved findings: 1", "unresolved findings: 18")
text = text.replace(
    "独立 Coverage/Evidence 审计已闭合；仅剩 root Books 串行写回与不同写作者 post-write audit。",
    "Coverage/Evidence 已闭合；Books 已写回但 post-write chapter-flow audit 为 0/18，18 项精确归位 finding 是唯一未解决条件。",
)
README_PATH.write_text(text)

print(json.dumps(audit["counts"], ensure_ascii=False))
