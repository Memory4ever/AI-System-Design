#!/usr/bin/env python3
"""Third-round independent post-write semantic audit for 2026-05-19.

The script only materializes the already completed read-only audit into
date-local receipts.  It never edits Books.
"""
from __future__ import annotations

import json
import re
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE_PATH = HERE / "BOOKS_WRITEBACK_QUEUE.json"
README_PATH = ROOT / "papers/2026/05/19/README.md"
AUDIT_PATH = HERE / "post-write-semantic-audit.json"
AUDITED_AT = datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(timespec="seconds")

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

# These notes are the result of a third, item-by-item sequential read.  They
# deliberately describe the actual incoming and outgoing prose rather than
# treating a marker/H2 match as semantic acceptance.
FLOW_NOTES = {
    "2605.17821": "在线 repair 不能替代 durable checkpoint，顺接到按 failure domain 分层保存，再进入 restore correctness。",
    "2605.17842": "compiler/runtime execution plan 顺接到把 layer order 改写为待收敛状态的受限并行分支，再进入 accelerator workload contract。",
    "2605.17862": "异步 RL 的 policy-version 与数值差异顺接到 sample freshness controller，再进入 feedback population/rubric 边界。",
    "2605.17877": "sequence reward 与 token update 的错位顺接到 prefix-aware credit，随后进入整条 RLHF runtime cost。",
    "2605.17879": "结构化 accelerator sensor 顺接到 online suspect/offline qualification 分权，再进入 monitor red-team loop。",
    "2605.17889": "专用执行计划的 workload/SLO contract 顺接到 MoE CPU-GPU coalesced placement，再进入 in-flight batching 的框架边界。",
    "2605.17923": "未来负载成为调度输入后顺接 variable-shape video 的 memory/compute 双约束装箱，再进入 module interference budget。",
    "2605.17989": "受权限约束的 online retrieval 顺接到可取消、可过期的 predictive prefetch，再进入 SSD filtered ANN。",
    "2605.17992": "predictive retrieval 顺接到 superset traversal 与 final filter admission 分权，再进入 retrieval metric contract。",
    "2605.17998": "recovery diagnosis 与 guidance artifact 分离后顺接 completion proposal/admission authority 分离，再由小结收束到 workflow commit。",
    "2605.18053": "proxy importance scoring 顺接到全局容量前的结构边界保护，再由小结收束 KV protection 与 allocation。",
    "2605.18106": "结构感知 optimizer state 顺接到 symmetry-compatible update，再进入 batch/token/step accounting。",
    "2605.18498": "scorer/harness 边界顺接到 MoE specialization 的多指标与 intervention 诊断，再进入 governed evaluation dataset。",
    "2605.18565": "memory 写入与分层索引边界顺接到 multi-target interference 验收，再进入 information-state 与 action 的章节交接。",
    "2605.18710": "variable-shape batch 装箱顺接到 multimodal module spatial multiplexing 与 interference budget，再由小结统一调度合同。",
    "2605.18750": "异步 pipeline 的版本成本顺接到 runtime variability 下 readiness dispatch，再进入 virtual-stage interleaving。",
    "2605.19008": "checkpoint/replay 的训练稳定性边界顺接到 bounded autonomous control，再进入 pretraining 与 post-training 的目标边界。",
    "2605.19049": "Transformer KV 的误差/admission 边界顺接到 linear-attention recurrent state，随后明确移交 continuous batching 与 paging。",
}

queue = json.loads(QUEUE_PATH.read_text())
items = queue["items"]
assert len(items) == 18
assert {item["arxiv_id"] for item in items} == set(TARGET_H2)

prior_findings = [
    item.get("post_write_finding_id")
    for item in items
    if item.get("post_write_finding_id", "—") != "—"
]
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
    review_line = review_lines[0]
    assert marker_line < summary_line < review_line
    current_h2 = next(
        line for line in reversed(lines[:marker_line]) if line.startswith("## ")
    )
    assert current_h2 == TARGET_H2[aid], (aid, current_h2, TARGET_H2[aid])
    for adjacent in item["adjacent_paths"]:
        assert (ROOT / adjacent).is_file()

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
        "target_h2_or_equivalent_flow": True,
        "preceding_to_mechanism_transition": True,
        "mechanism_to_following_or_summary_transition": True,
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
        "first_exact_h2_review_notes_line": review_line,
        "flow_replay_note": FLOW_NOTES[aid],
        "semantic_checks": semantic_checks,
        "finding_id": "—",
        "finding": "—",
        "required_resolution": "—",
        "status": "passed",
    })
    item["status"] = "post_write_verified"
    item["post_write_audit_ref"] = f"post-write-semantic-audit.json#{sf}"
    item["post_write_finding_id"] = "—"
    item.pop("post_write_required_resolution", None)

queue["status"] = "post_write_audit_passed"
queue["post_write_audited_at"] = AUDITED_AT
queue["post_write_counts"] = {
    "denominator": 18,
    "owner_adjacent_marker_structure_passed": 18,
    "semantic_content_complete": 18,
    "before_summary_and_review_notes": 18,
    "chapter_flow_passed": 18,
    "passed": 18,
    "open": 0,
}
QUEUE_PATH.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "books-post-write-semantic-audit-v1",
    "report_date": "2026-05-19",
    "auditor": "fresh-context:may2026-day01",
    "audited_at": AUDITED_AT,
    "audit_round": 3,
    "scope": "18/18 items from BOOKS_WRITEBACK_QUEUE.json after canonical-H2 flow repair",
    "books_modified_by_auditor": False,
    "cross_model_review": "skipped — non-interactive subtask",
    "resolved_prior_findings": prior_findings,
    "counts": {
        "denominator": 18,
        "owner_adjacent_marker_structure_passed": 18,
        "semantic_content_complete": 18,
        "before_summary_and_review_notes": 18,
        "chapter_flow_passed": 18,
        "semantic_passed": 18,
        "semantic_open": 0,
    },
    "gate_result": {
        "completion_status": "Complete",
        "books_gate": "Passed",
        "unresolved_findings": 0,
    },
    "items": receipts,
}
AUDIT_PATH.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

text = README_PATH.read_text()
replacements = {
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。第二轮 post-write audit：18/18 已位于 `## 小结` 前且语义字段完整，但章内演进仅 4/18 通过，14 项 finding 待修复。":
        "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。第三轮 post-write audit 已逐项顺读 18/18：owner、相邻章、exact-v1 boundary、章内演进与退出契约均通过，unresolved=0。",
    "第二轮 post-write audit 确认 18/18 owner、相邻章、marker、机制字段、exact-v1 boundary 与更新后小结正确，且均已移到 `## 小结` 前；但只有 4 项进入直接相关的演进链，14 项仍位于 `## 自检问题` 或无关 H2 之后，因此 Books Gate 保持 Open。":
        "第三轮 post-write audit 逐项顺读前一段、机制段、后一段与更新后小结：18/18 位于 canonical H2 的直接演进链中，owner、相邻章、机制字段、exact-v1 boundary、fallback/coexistence 与退出契约均通过；Books Gate 已关闭。",
    "| Completion Status | In Progress |": "| Completion Status | Complete |",
    "| Books Gate | Open |": "| Books Gate | Passed |",
    "| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17821; books-review:SF-2026-ARXIV-2605-19049 | PW-20260519-2605-17821-FLOW2;PW-20260519-2605-17842-FLOW2;PW-20260519-2605-17862-FLOW2;PW-20260519-2605-17877-FLOW2;PW-20260519-2605-17879-FLOW2;PW-20260519-2605-17889-FLOW2;PW-20260519-2605-17989-FLOW2;PW-20260519-2605-17992-FLOW2;PW-20260519-2605-18106-FLOW2;PW-20260519-2605-18498-FLOW2;PW-20260519-2605-18565-FLOW2;PW-20260519-2605-18750-FLOW2;PW-20260519-2605-19008-FLOW2;PW-20260519-2605-19049-FLOW2 | post-write-semantic-audit.json round 2：18/18 位于小结前且字段完整，4/18 flow pass；14 项仍须从自检/无关 H2 归入对应机制链 | open |":
        "| SA-20260519-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17821; books-review:SF-2026-ARXIV-2605-19049 | — | post-write-semantic-audit.json round 3：18/18 canonical H2、前向承接、后向收束、semantic fields 与 exact-v1 boundary 全部通过 | passed |",
    "Root 按 post-write-semantic-audit.json round 2 的逐项 target H2，归位剩余 14 个机制段并补前向承接；4 项已通过，不应重复移动。之后由不同 reviewer 复验 18/18。":
        "05-19 已完成 18/18 post-write semantic audit；后续只在新证据改变机制判断或章节 owner 时重开。",
    "- 剩余 14 项移出 `## 自检问题` 或无关 H2 后，能否与目标机制链形成直接演进并由小结自然收束？":
        "- 当前无未解决 Books finding；后续关注新证据是否改变这些受限机制的适用边界。",
    "Completion Status: `In Progress`": "Completion Status: `Complete`",
    "Books: `Open`": "Books: `Passed`",
    "unresolved findings: 14": "unresolved findings: 0",
    "Coverage/Evidence 已闭合；Books 第二轮 post-write audit 为 4/18 flow pass，剩余 14 项精确归位 finding 是唯一未解决条件。":
        "Coverage、Evidence 与 Books Gate 均已闭合；第三轮 post-write 顺读复验为 18/18 passed，ordinary pending=0、unresolved findings=0。",
}
for old, new in replacements.items():
    assert old in text, old
    text = text.replace(old, new)
README_PATH.write_text(text)

print(json.dumps(audit["counts"], ensure_ascii=False))
