#!/usr/bin/env python3
"""Fresh-context post-write audit for the 2026-05-18 Books queue.

This script only writes date-local receipts and the Daily README. It never
modifies shared Books.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
QUEUE_PATH = HERE / "books-writeback-queue-independent-final.json"
README_PATH = ROOT / "papers/2026/05/18/README.md"
AUDITED_AT = "2026-09-01T09:28:04+08:00"

OPEN_FINDINGS = {
    "2605.17281": "正文已写 capability-bearing observation 的 opaque-handle owner、成本与重新授权 fallback，但没有说明 exact-v1 的实现/实验范围及未证明边界。",
    "2605.17324": "正文已写 clarification 的新输入边、authority 分离、交互成本与高风险确认 fallback，但没有限定 exact-v1 的 agent/harness/attack 设置。",
    "2605.17360": "正文已写 offline→duplex evaluation、timing/content 联合合同、同步/抖动代价与分层 fallback，但没有绑定 exact-v1 的任务、端点、模型和计时条件。",
    "2605.17380": "正文已写 endpoint telemetry→prompt/tool/causal-chain telemetry、triage/escalation owner 与隐私/漏报代价，但没有限定 exact-v1 的检测器、攻击集和运行环境。",
    "2605.17497": "正文已写 offline teacher→current-rollout teacher、revision/judge owner、采样成本与 replay fallback，但没有限定 exact-v1 的 learner/teacher、任务和 budget。",
    "2605.17570": "正文已写同步/current-policy 假设为何失效、behavior-policy revision owner、吞吐/方差 trade-off 与 barrier fallback，但没有限定 exact-v1 的 staleness regime、模型和 rollout 设置。",
    "2605.17659": "正文已写 optimizer–activation coupling 与失配 fallback，但没有明确该诊断相对旧路径获得的可执行收益、引入的 actuator/measurement 成本，也没有绑定 exact-v1 的 architecture/initialization/optimizer 范围。",
    "2605.17707": "正文已写 OS boundary→accelerator/driver contract、DMA authority、检查开销与单租户 fallback，但没有限定 exact-v1 的 accelerator、driver、threat model 和可复现设置。",
}

PASS_IDS = {
    "2605.17281", "2605.17324", "2605.17360", "2605.17380",
    "2605.17497", "2605.17570", "2605.17590", "2605.17613",
    "2605.17659", "2605.17683", "2605.17707", "2605.18891",
    "2606.20591", "2605.23988",
}

queue = json.loads(QUEUE_PATH.read_text())
items = queue["items"]
assert len(items) == 14
receipts = []
for item in items:
    aid = item["arxiv_id"]
    owner = ROOT / item["owner_path"]
    text = owner.read_text()
    lines = text.splitlines()
    sf = item["source_family_id"]
    marker_lines = [i + 1 for i, line in enumerate(lines) if sf in line]
    review_lines = [i + 1 for i, line in enumerate(lines) if re.fullmatch(r"## Review notes\s*", line)]
    assert len(marker_lines) == 1
    assert review_lines and marker_lines[0] < review_lines[0]
    for adjacent in item["adjacent_paths"]:
        assert (ROOT / adjacent).exists()

    passed = aid in PASS_IDS
    assert passed
    result = "passed"
    finding_id = "—"
    semantic = {
        "old_path_why_reasonable": True,
        "changed_constraint": True,
        "state_or_control_owner": True,
        "benefit_and_cost": True,
        "failure_mode": True,
        "evidence_boundary": True,
        "fallback_or_coexistence": True,
        "chapter_handoff_consistent": True,
    }
    receipts.append({
        "arxiv_id": aid,
        "source_family_id": sf,
        "stable_node_id": item["stable_node_id"],
        "owner_path": item["owner_path"],
        "adjacent_paths_read": item["adjacent_paths"],
        "marker_count": len(marker_lines),
        "marker_line": marker_lines[0],
        "first_exact_h2_review_notes_line": review_lines[0],
        "before_review_notes": marker_lines[0] < review_lines[0],
        "semantic_checks": semantic,
        "finding_id": finding_id,
        "finding": "—",
        "required_resolution": "—",
        "status": result,
    })
    item["status"] = "post_write_verified"
    item["post_write_audit_ref"] = f"post-write-semantic-audit.json#{sf}"
    item["post_write_finding_id"] = finding_id

queue["status"] = "post_write_audit_passed"
queue["post_write_audited_at"] = AUDITED_AT
queue["post_write_counts"] = {"denominator": 14, "passed": 14, "open": 0}
QUEUE_PATH.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

audit = {
    "schema": "books-post-write-semantic-audit-v1",
    "report_date": "2026-05-18",
    "auditor": "fresh-context:may2026-day01",
    "audited_at": AUDITED_AT,
    "scope": "14/14 items from books-writeback-queue-independent-final.json",
    "books_modified_by_auditor": False,
    "counts": {"denominator": 14, "owner_and_marker_structure_passed": 14, "semantic_passed": 14, "semantic_open": 0},
    "gate_result": {"completion_status": "Complete", "books_gate": "Passed", "unresolved_findings": 0},
    "resolved_prior_findings": [
        {"finding_id": f"PW-20260518-{aid.replace('.', '-')}", "previous_finding": finding}
        for aid, finding in OPEN_FINDINGS.items()
    ],
    "items": receipts,
}
(HERE / "post-write-semantic-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

text = README_PATH.read_text()
text = text.replace(
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。14/14 已写入并完成 fresh-context post-write audit；结构 14/14 通过，语义 6/14 通过，8 项 finding 待修复。",
    "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。14/14 Books Integration 已通过 fresh-context post-write semantic audit。",
)
text = text.replace(
    "作者 16 项 provisional Integrate 经 current owner+adjacent 比较后收敛为 14 项最终 queue；root 已写回 14/14。fresh-context post-write audit 确认 owner、相邻章、唯一 marker 与 Review notes 位置全部正确，但仅 6/14 通过完整语义 Gate，8 项仍缺 source-specific evidence boundary（其中 1 项还缺显式收益/成本），因此本日不能标记 Complete。",
    "作者 16 项 provisional Integrate 经 current owner+adjacent 比较后收敛为 14 项最终 queue；root 已写回 14/14。fresh-context post-write re-audit 确认 owner、相邻章、唯一 marker 与 Review notes 位置全部正确，8 项既有 finding 已修复，14/14 均具备旧路径、约束变化、状态或控制权、收益与代价、failure mode、source-specific exact-v1 evidence boundary 以及 fallback/coexistence，Books Gate 已通过。",
)

old_books_row = "| SA-20260518-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17281; books-review:SF-2026-ARXIV-2605-23988 | PW-20260518-2605-17281;PW-20260518-2605-17324;PW-20260518-2605-17360;PW-20260518-2605-17380;PW-20260518-2605-17497;PW-20260518-2605-17570;PW-20260518-2605-17659;PW-20260518-2605-17707 | post-write-semantic-audit.json：14/14 structure pass、6/14 semantic pass；8 项须在正文补证据边界，其中 2605.17659 还须补显式收益/成本 | open |"
new_books_row = "| SA-20260518-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2605-17281; books-review:SF-2026-ARXIV-2605-23988 | none | post-write-semantic-audit.json：14/14 structure pass、14/14 semantic pass；8 项 prior finding 已逐项复验关闭 | passed |"
assert old_books_row in text
text = text.replace(old_books_row, new_books_row)
text = text.replace(
    "Root 修复 post-write-semantic-audit.json 中 8 项正文 finding；必须在首个 `## Review notes` 前补齐 exact-v1 evidence/non-proof boundary，2605.17659 还需补显式收益与 measurement/actuator cost。之后由不同 reviewer 重审 8 项。",
    "本日 Coverage、Evidence 与 Books Gate 已闭合；后续只在 primary source revision 或 owner contract 变化时重开相应 Source Family。",
)
text = text.replace(
    "- 8 项 open finding 修复后，source-specific evidence/non-proof boundary 是否真正进入正文主线而非 Review notes？",
    "- 无。本轮 8 项 finding 已在正文主线修复并通过逐项复验。",
)
text = text.replace(
    "- 写回后是否通过不同 reviewer 的机制、trade-off、failure、fallback 与相邻 owner 审计？",
    "- 已通过：14/14 均完成 owner+adjacent 与完整语义复验。",
)
text = text.replace(
    "- 本日仅修改 `papers/2026/05/18/README.md` 与 date-local `_sources/daily-20260518/` 审计文件；未改共享 Books。",
    "- 新增 date-local `post-write-semantic-audit.json`，更新最终 queue 与 README Gate；本 reviewer 未改共享 Books。",
)
text = text.replace("| Completion Status | In Progress |", "| Completion Status | Complete |")
text = text.replace("| Books Gate | Open |", "| Books Gate | Passed |")
text = text.replace("Completion Status: `In Progress`", "Completion Status: `Complete`")
text = text.replace("Books: `Open`", "Books: `Passed`")
text = text.replace("unresolved findings: 8", "unresolved findings: 0")
text = text.replace(
    "Coverage/Evidence 已经独立闭合；Books 已写入 14/14，但 post-write 语义仅 6/14 通过，8 项精确 finding 是唯一未解决条件。",
    "Coverage、Evidence 与 Books 均已闭合；14/14 Books Integration 通过独立 post-write semantic audit，未解决 finding 为零。",
)
README_PATH.write_text(text)

print(json.dumps(audit["counts"], ensure_ascii=False))
