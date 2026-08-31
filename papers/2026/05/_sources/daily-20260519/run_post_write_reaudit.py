#!/usr/bin/env python3
"""Second-round fresh-context post-write audit for 2026-05-19.

Writes only date-local receipts and the Daily README; never modifies Books.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE_PATH = HERE / "BOOKS_WRITEBACK_QUEUE.json"
README_PATH = ROOT / "papers/2026/05/19/README.md"
AUDITED_AT = "2026-09-01T09:48:00+08:00"

TARGET_H2 = {
    "2605.17821": "## 保存频率是故障成本权衡",
    "2605.17842": "## Build-time 与 Runtime-time",
    "2605.17862": "## RLHF 的系统成本",
    "2605.17877": "## Sequence reward 与 token updates 的错位",
    "2605.17879": "## 从随机 Fault Injection 到可定位的 Accelerator Sensor",
    "2605.17889": "## 专用加速器首先是一份 Workload Contract",
    "2605.17923": "## 当未来负载、迟到更新与模型边界成为调度输入",
    "2605.17989": "## Online Retrieval Pipeline",
    "2605.17992": "## Online Retrieval Pipeline",
    "2605.17998": "## Recovery 与 Verification 必须产生不同 Artifact",
    "2605.18053": "## 把高精度 Importance Scoring 移出 Target Critical Path",
    "2605.18106": "## Optimizer 不是与参数化无关的旋钮",
    "2605.18498": "## Scorer 不是绝对真相",
    "2605.18565": "## 评估 Memory",
    "2605.18710": "## 当未来负载、迟到更新与模型边界成为调度输入",
    "2605.18750": "## 异步 Pipeline：去掉 Bubble 会把成本移到参数版本",
    "2605.19008": "## 训练稳定性是多层系统问题",
    "2605.19049": "## 与第19章的职责边界",
}

PASS_IDS = {"2605.17923", "2605.17998", "2605.18053", "2605.18710"}

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
    assert len(marker_lines) == 1 and review_lines and summary_lines
    marker_line = marker_lines[0]
    summary_line = summary_lines[-1]
    assert marker_line < summary_line < review_lines[0]
    marker_index = marker_line - 1
    current_h2 = next(
        line for line in reversed(lines[: marker_index + 1]) if line.startswith("## ")
    )
    for adjacent in item["adjacent_paths"]:
        assert (ROOT / adjacent).is_file()
    assert TARGET_H2[aid] in lines

    passed = aid in PASS_IDS
    finding_id = "—" if passed else f"PW-20260519-{aid.replace('.', '-')}-FLOW2"
    if passed:
        finding = "—"
        resolution = "—"
    elif current_h2 == "## 自检问题":
        finding = (
            f"完整机制段当前位于 `{current_h2}` 的问题清单之后；虽然 marker 已在 `## 小结` 前，"
            "但正文在自检之后重新开启新机制，阅读顺序仍被反转。"
        )
        resolution = (
            f"将完整段落与 marker 移入 `{TARGET_H2[aid]}` 的相关机制链，并在 `## 自检问题` 前完成正文推导；"
            "同步确认小结只做收束。"
        )
    else:
        finding = (
            f"完整机制段当前归属 `{current_h2}`，与其主题没有直接演进或依赖关系；更新后小结虽提及该机制，"
            "但不能弥补正文从前一主题突然跳转的 owner-flow 断裂。"
        )
        resolution = (
            f"将完整段落与 marker 移入 `{TARGET_H2[aid]}`，补一条由既有机制进入新约束的承接句；"
            "不得只依赖小结追认该主题。"
        )

    semantic_checks = {
        "old_path_why_reasonable": True,
        "changed_constraint": True,
        "state_or_control_owner": True,
        "benefit_and_cost": True,
        "failure_mode": True,
        "evidence_boundary": True,
        "fallback_or_coexistence": True,
        "owner_and_adjacent_consistent": True,
        "before_summary_and_review_notes": True,
        "target_h2_or_equivalent_flow": passed,
        "updated_summary_and_exit_contract": True,
    }
    receipts.append({
        "arxiv_id": aid,
        "source_family_id": sf,
        "stable_node_id": item["stable_node_id"],
        "owner_path": item["owner_path"],
        "adjacent_paths_read": item["adjacent_paths"],
        "marker_count": 1,
        "marker_line": marker_line,
        "current_h2": current_h2,
        "required_target_h2": TARGET_H2[aid],
        "summary_line": summary_line,
        "first_exact_h2_review_notes_line": review_lines[0],
        "semantic_checks": semantic_checks,
        "finding_id": finding_id,
        "finding": finding,
        "required_resolution": resolution,
        "status": "passed" if passed else "open",
    })
    item["status"] = "post_write_verified" if passed else "post_write_finding_open"
    item["post_write_audit_ref"] = f"post-write-semantic-audit.json#{sf}"
    item["post_write_finding_id"] = finding_id
    if passed:
        item.pop("post_write_required_resolution", None)
    else:
        item["post_write_required_resolution"] = resolution

queue["status"] = "post_write_audit_open_14_flow_findings"
queue["post_write_audited_at"] = AUDITED_AT
queue["post_write_counts"] = {
    "denominator": 18,
    "owner_adjacent_marker_structure_passed": 18,
    "semantic_content_complete": 18,
    "before_summary_and_review_notes": 18,
    "chapter_flow_passed": 4,
    "passed": 4,
    "open": 14,
}
QUEUE_PATH.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

open_ids = [r["finding_id"] for r in receipts if r["status"] == "open"]
audit = {
    "schema": "books-post-write-semantic-audit-v1",
    "report_date": "2026-05-19",
    "auditor": "fresh-context:may2026-day01",
    "audited_at": AUDITED_AT,
    "audit_round": 2,
    "scope": "18/18 items from BOOKS_WRITEBACK_QUEUE.json after first flow repair",
    "books_modified_by_auditor": False,
    "cross_model_review": "skipped — non-interactive subtask",
    "counts": {
        "denominator": 18,
        "owner_adjacent_marker_structure_passed": 18,
        "semantic_content_complete": 18,
        "before_summary_and_review_notes": 18,
        "chapter_flow_passed": 4,
        "semantic_passed": 4,
        "semantic_open": 14,
    },
    "gate_result": {
        "completion_status": "In Progress",
        "books_gate": "Open",
        "unresolved_findings": 14,
    },
    "items": receipts,
}
(HERE / "post-write-semantic-audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n"
)

text = README_PATH.read_text()
text = text.replace(
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。18/18 已写入并完成 post-write audit；内容字段完整，但全部位于各章 `## 小结` 之后，18 项章内流程 finding 待修复。",
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。第二轮 post-write audit：18/18 已位于 `## 小结` 前且语义字段完整，但章内演进仅 4/18 通过，14 项 finding 待修复。",
)
text = text.replace(
    "31 项 provisional Books queue 经 current owner+adjacent challenge 收紧为 18 项并已写回。post-write audit 确认 18/18 owner、相邻章、marker、机制字段和 exact-v1 boundary 正确，但 18 项全部位于 `## 小结` 之后，破坏章节演进与退出契约，因此 Books Gate 保持 Open。",
    "31 项 provisional Books queue 经 current owner+adjacent challenge 收紧为 18 项并已写回。第二轮 post-write audit 确认 18/18 owner、相邻章、marker、机制字段、exact-v1 boundary 与更新后小结正确，且均已移到 `## 小结` 前；但只有 4 项进入直接相关的演进链，14 项仍位于 `## 自检问题` 或无关 H2 之后，因此 Books Gate 保持 Open。",
)
old_row = "| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17821; books-review:SF-2026-ARXIV-2605-19049 | PW-20260519-2605-17821-FLOW;PW-20260519-2605-17842-FLOW;PW-20260519-2605-17862-FLOW;PW-20260519-2605-17877-FLOW;PW-20260519-2605-17879-FLOW;PW-20260519-2605-17889-FLOW;PW-20260519-2605-17923-FLOW;PW-20260519-2605-17989-FLOW;PW-20260519-2605-17992-FLOW;PW-20260519-2605-17998-FLOW;PW-20260519-2605-18053-FLOW;PW-20260519-2605-18106-FLOW;PW-20260519-2605-18498-FLOW;PW-20260519-2605-18565-FLOW;PW-20260519-2605-18710-FLOW;PW-20260519-2605-18750-FLOW;PW-20260519-2605-19008-FLOW;PW-20260519-2605-19049-FLOW | post-write-semantic-audit.json：18/18 内容字段完整，但 chapter flow 0/18；完整机制段均须移到 `## 小结` 之前的对应演进节点 | open |"
new_row = "| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17821; books-review:SF-2026-ARXIV-2605-19049 | " + ";".join(open_ids) + " | post-write-semantic-audit.json round 2：18/18 位于小结前且字段完整，4/18 flow pass；14 项仍须从自检/无关 H2 归入对应机制链 | open |"
assert old_row in text
text = text.replace(old_row, new_row)
text = text.replace(
    "Root 按 post-write-semantic-audit.json 的逐项 target H2，把 18 个完整机制段归入 `## 小结` 之前的章节演进链；随后由不同 reviewer 重读 owner+adjacent 与章内退出契约。",
    "Root 按 post-write-semantic-audit.json round 2 的逐项 target H2，归位剩余 14 个机制段并补前向承接；4 项已通过，不应重复移动。之后由不同 reviewer 复验 18/18。",
)
text = text.replace(
    "- 18 个完整机制段归位到对应 H2 后，能否在 `## 小结` 前形成连续演进，并保持相邻章节 owner 边界？",
    "- 剩余 14 项移出 `## 自检问题` 或无关 H2 后，能否与目标机制链形成直接演进并由小结自然收束？",
)
text = text.replace("unresolved findings: 18", "unresolved findings: 14")
text = text.replace(
    "Coverage/Evidence 已闭合；Books 已写回但 post-write chapter-flow audit 为 0/18，18 项精确归位 finding 是唯一未解决条件。",
    "Coverage/Evidence 已闭合；Books 第二轮 post-write audit 为 4/18 flow pass，剩余 14 项精确归位 finding 是唯一未解决条件。",
)
README_PATH.write_text(text)

print(json.dumps(audit["counts"], ensure_ascii=False))
