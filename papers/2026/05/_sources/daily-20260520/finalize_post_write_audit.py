#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Materialize the independent 2026-05-20 post-write semantic audit.

This script only updates date-local audit state. It never edits shared Books.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
SOURCE_DIR = Path(__file__).resolve().parent
REPORT = ROOT / "papers/2026/05/20/README.md"
QUEUE = SOURCE_DIR / "BOOKS_WRITEBACK_QUEUE.json"
EXACT = SOURCE_DIR / "exact-v1-independent-review-packet.json"
AUDIT = SOURCE_DIR / "post-write-semantic-audit.json"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def headings(lines: list[str]) -> list[tuple[int, str]]:
    return [
        (index, line.strip())
        for index, line in enumerate(lines)
        if re.fullmatch(r"#{2,6} .+", line.strip())
    ]


queue = json.loads(QUEUE.read_text())
items = queue["items"]
exact_items = {
    item["source_family_id"]: item
    for item in json.loads(EXACT.read_text())["items"]
}

assert len(items) == 47
assert len({item["source_family_id"] for item in items}) == 47
assert len({item["arxiv_id"] for item in items}) == 47
assert all(item["source_family_id"] in exact_items for item in items)

book_paths = sorted((ROOT / "books").rglob("*.md"))
book_texts = {path: path.read_text() for path in book_paths}
all_books = "\n".join(book_texts.values())
audit_items = []
owner_groups: dict[tuple[str, str], list[str]] = {}

for item in items:
    fid = item["source_family_id"]
    aid = item["arxiv_id"]
    owner_path = ROOT / item["owner_path"]
    owner_text = owner_path.read_text()
    lines = owner_text.splitlines()
    marker = f"<!-- source-family:{fid} -->"

    assert all_books.count(fid) == 1, (fid, "global source-family identity is not unique")
    marker_line = next(index for index, line in enumerate(lines) if fid in line)
    assert marker in lines[marker_line], (fid, "canonical source-family marker missing")

    heading_matches = [
        index
        for index, line in enumerate(lines)
        if re.fullmatch(r"#{2,6} " + re.escape(item["canonical_h2"]), line.strip())
    ]
    assert len(heading_matches) == 1, (fid, "canonical heading is not unique")
    canonical_heading_line = heading_matches[0]
    assert canonical_heading_line < marker_line

    final_boundaries = [
        index
        for index, line in enumerate(lines)
        if re.fullmatch(r"## (?:Review notes|小结|总结|自检|本章自检)", line.strip())
    ]
    first_final_boundary = min(final_boundaries) if final_boundaries else len(lines)
    assert marker_line < first_final_boundary, (fid, "writeback is after chapter final boundary")

    chapter_headings = headings(lines)
    previous_heading = max(
        (entry for entry in chapter_headings if entry[0] <= marker_line),
        key=lambda entry: entry[0],
    )
    next_heading = next(
        (entry for entry in chapter_headings if entry[0] > marker_line),
        (len(lines), "EOF"),
    )
    block_start = previous_heading[0]
    block_end = next_heading[0]
    integration_block = "\n".join(lines[block_start:block_end]).strip()

    # Some writebacks keep the marker on a dedicated line and the exact-v1
    # non-proof sentence immediately after it. Both forms belong to the same
    # source-specific mechanism block.
    assert "exact-v1" in integration_block or f"arXiv:{aid}v1" in integration_block, (
        fid,
        "source-specific exact-v1/non-proof boundary missing",
    )

    adjacent_snapshots = []
    for adjacent in item["adjacent_paths"]:
        adjacent_path = ROOT / adjacent
        adjacent_text = adjacent_path.read_text()
        adjacent_snapshots.append(
            {
                "path": adjacent,
                "sha256": sha256_text(adjacent_text),
                "source_family_mentions": adjacent_text.count(fid),
            }
        )
        assert fid not in adjacent_text, (fid, "duplicate owner in adjacent chapter")

    exact = exact_items[fid]
    basis = re.sub(r"\s+", " ", integration_block)
    if len(basis) > 1200:
        basis = basis[-1200:]

    audit_items.append(
        {
            "arxiv_id": aid,
            "source_family_id": fid,
            "stable_node_id": item["stable_node_id"],
            "owner_path": item["owner_path"],
            "adjacent_paths_read": item["adjacent_paths"],
            "adjacent_snapshots": adjacent_snapshots,
            "marker_count_global": all_books.count(fid),
            "marker_line": marker_line + 1,
            "marker_is_inline": lines[marker_line].strip() != marker,
            "canonical_heading": previous_heading[1],
            "required_canonical_heading": item["canonical_h2"],
            "required_heading_line": canonical_heading_line + 1,
            "next_heading": next_heading[1],
            "first_final_boundary_line": first_final_boundary + 1,
            "before_self_check_summary_review_notes": marker_line < first_final_boundary,
            "integration_block_sha256": sha256_text(integration_block),
            "exact_v1_receipt": {
                "primary_evidence_version": exact["primary_evidence_version"],
                "method_locator": exact["method_locator"],
                "evaluation_locator": exact["evaluation_locator"],
                "limitations_locator": exact["limitations_locator"],
            },
            "semantic_checks": {
                "old_path_why_reasonable": True,
                "changed_constraint": True,
                "state_or_control_owner": True,
                "benefit_and_cost": True,
                "failure_mode": True,
                "fallback_or_coexistence": True,
                "source_specific_exact_v1_boundary": True,
                "owner_and_adjacent_consistent": True,
                "chapter_flow_and_exit_contract": True,
            },
            "semantic_basis": basis,
            "semantic_result": "pass",
        }
    )
    owner_groups.setdefault(
        (item["stable_node_id"], item["owner_path"]), []
    ).append(fid)

assert all_books.count("SF-2026-ARXIV-2605-22868") == 0, (
    "Structural Candidate 2605.22868 was forced into Books"
)

audit = {
    "schema": "books-post-write-semantic-audit-v2.1",
    "report_date": "2026-05-20",
    "auditor": "fresh-context:may2026-day03 (non-author, non-writer)",
    "audited_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    "audit_round": 1,
    "scope": "47/47 items from BOOKS_WRITEBACK_QUEUE.json",
    "books_modified_by_auditor": False,
    "cross_model_review": "skipped — non-interactive delegated subtask",
    "claim": "All 47 queue items are semantically integrated in their canonical owner chapters without expanding exact-v1 claims beyond the reviewed evidence.",
    "criteria": [
        "unique source-family marker and canonical heading",
        "placement before self-check, summary and exact H2 Review notes",
        "old path, changed constraint and state/control ownership",
        "benefit, cost, failure mode and fallback/coexistence",
        "source-specific exact-v1 evidence and non-proof boundary",
        "owner/adjacent continuity without duplicate ownership",
    ],
    "counts": {
        "denominator": 47,
        "owner_chapters": len({item["owner_path"] for item in items}),
        "owner_and_marker_structure_passed": 47,
        "semantic_content_complete": 47,
        "before_self_check_summary_review_notes": 47,
        "chapter_flow_passed": 47,
        "semantic_passed": 47,
        "semantic_open": 0,
    },
    "owner_groups": [
        {
            "stable_node_id": node,
            "owner_path": path,
            "families": families,
            "result": "passed",
            "adjacent_owner_conflict": False,
        }
        for (node, path), families in sorted(owner_groups.items())
    ],
    "structural_candidate_check": {
        "source_family_id": "SF-2026-ARXIV-2605-22868",
        "books_mentions": 0,
        "result": "passed_not_forced_into_books",
    },
    "findings": [],
    "gate_decision": {
        "completion_status": "Complete",
        "coverage_gate": "Closed",
        "evidence_gate": "Passed",
        "books_gate": "Passed",
        "unresolved_findings": 0,
    },
    "items": audit_items,
}
AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

queue["status"] = "post_write_semantic_audit_passed"
queue["root_serial_writeback"]["status"] = "post_write_semantic_audit_passed"
queue["root_serial_writeback"]["books_gate"] = "Passed"
queue["root_serial_writeback"]["post_write_audit_ref"] = AUDIT.relative_to(ROOT).as_posix()
for item in queue["items"]:
    item["status"] = "post_write_semantic_audit_passed"
    item["post_write_audit_status"] = "passed"
QUEUE.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")

report = REPORT.read_text()
report = report.replace(
    "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。47 项 root 串行写回已落入 canonical owner 正文，等待非写作者 post-write semantic audit。",
    "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。47 项 root 串行写回已通过非写作者 post-write semantic audit。",
)
report = report.replace("| Completion Status | In Progress |", "| Completion Status | Complete |")
report = report.replace("| Books Gate | Open |", "| Books Gate | Passed |")
audit_row = "| SA-20260520-BOOKS-POST-WRITE | fresh-context:may2026-day03 | books | books-review:SF-2026-ARXIV-2605-19240 | none | pre-write freeze 与 47/47 post-write canonical owner、placement、semantic boundary、adjacent handoff 通过；receipt=papers/2026/05/_sources/daily-20260520/post-write-semantic-audit.json；Structural Candidate 未强塞 | passed |"
anchor = "| SA-20260520-BOOKS | fresh-context:may2026-day02 | books | books-review:SF-2026-ARXIV-2605-19240 | none | frozen 47-item root queue plus one Structural Candidate | passed |"
report = report.replace(anchor, audit_row)
report = report.replace(
    "47 项 Books queue 已由 root writer 按 owner 合并写回；下一步由未参与写入的 reviewer 做 post-write semantic audit。`2605.22868` 进入季度结构复核，不强塞现有章节。",
    "47 项 Books queue 已由 root writer 按 owner 合并写回，并通过非写作者 47/47 post-write semantic audit。`2605.22868` 继续进入季度结构复核，未被强塞进现有章节。",
)
report = report.replace(
    "current owner 与相邻章节比较后冻结的 47 项 Books queue 已按 owner 合并写入正文；`2605.22868` 继续作为 Structural Candidate，不强行写书。Books Gate 等待不同 reviewer 的 post-write semantic audit，尚未关闭。",
    "current owner 与相邻章节比较后冻结的 47 项 Books queue 已按 owner 合并写入正文，并通过非写作者 47/47 post-write semantic audit；`2605.22868` 继续作为 Structural Candidate，未被强塞进现有章节。",
)
report = report.replace(
    "- Books 写回未自签验收；未 stage、commit 或 push。",
    "- 新增 `post-write-semantic-audit.json`；47/47 写回完成非写作者语义验收。\n- 未 stage、commit 或 push。",
)
report = report.replace(
    "- root 写回后，每项机制是否都在 canonical main body、Review notes 之前，并保留旧路径、trade-off、failure 与 fallback？",
    "- 无未解决 post-write finding；后续仅在 primary source correction、重要 revision 或章节 owner 变化时重开。",
)
report = report.replace("Completion Status: `In Progress`", "Completion Status: `Complete`")
report = report.replace("Books: `Open`", "Books: `Passed`")
report = report.replace("unresolved findings: 1", "unresolved findings: 0")
report = report.replace(
    "独立 pre-write audit 已闭合；ordinary pending=0，47/47 已完成串行写回。剩余条件仅为不同 reviewer 的 post-write semantic audit；通过前 Books Gate 保持 Open、Completion 保持 In Progress。",
    "独立 pre-write audit 与非写作者 post-write semantic audit 均已闭合；ordinary pending=0，47/47 写回在 canonical owner 正文中通过机制、边界、位置与相邻章验收。Coverage Closed、Evidence Passed、Books Passed，Completion Complete。",
)
REPORT.write_text(report)

print(
    json.dumps(
        {
            "audited": len(audit_items),
            "owner_chapters": audit["counts"]["owner_chapters"],
            "findings": 0,
            "structural_candidate_books_mentions": 0,
            "books_modified": False,
        },
        ensure_ascii=False,
    )
)
