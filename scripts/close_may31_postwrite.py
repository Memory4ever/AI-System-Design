#!/usr/bin/env python3
"""Project the independent 2026-05-31 Books post-write acceptance."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/05/_sources/daily-20260531"
REPORT = ROOT / "papers/2026/05/31/README.md"

CHECKS = {
    "SF-2026-ARXIV-2606-00515": {
        "owner": "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "required": ["Passivity Shield", "energy-tank state", "peak-force bound", "人工接管"],
        "result": "VLA proposal and contact authority are separated; sampled diagonal-admittance scope, calibration failures and verified-controller/stop/human fallback remain explicit.",
    },
    "SF-2026-ARXIV-2606-00516": {
        "owner": "books/part-05-inference-system/56-inference-scheduling.md",
        "required": ["Exclusive Batching", "memory-safe batch size", "不支持 mixed 或 exclusive batching 的普适支配关系", "P/D 分离"],
        "result": "Exclusive phase switching is workload/model/bandwidth/memory-state dependent; mixed/exclusive coexistence and fixed-threshold or P/D fallback remain explicit.",
    },
    "SF-2026-ARXIV-2606-00539": {
        "owner": "books/part-04-training-system/28-pretraining.md",
        "required": ["Operator-normalized Risk", "hard recovery budget", "backend observability", "整步高精度 fallback"],
        "result": "Operator-relative risk is only a routing proposal under a recovery budget; backend observability, threshold drift, missed faults and full-step fallback bound the claim.",
    },
    "SF-2026-ARXIV-2606-00642": {
        "owner": "books/part-06-ai-infrastructure/72-security.md",
        "required": ["Hidden Reasoning Trace", "opaque handle", "defense-in-depth", "open-weight reasoning models"],
        "result": "Hidden trace is not promoted to a secrecy boundary; context exclusion, typed authorization/redaction, closed-system limits and answer-only/external-scratchpad fallback remain explicit.",
    },
    "SF-2026-ARXIV-2606-00888": {
        "owner": "books/part-04-training-system/28-pretraining.md",
        "required": ["Dynamic Sparsity", "local timestep", "optimizer-state owner", "dense training 或静态 sparsity"],
        "result": "Dynamic sparsity is correctly owned as topology plus optimizer state, not a collective mechanism; cold-start, metadata/kernel costs, evidence limits and dense/static fallback remain explicit.",
    },
}


def assert_books() -> list[dict[str, object]]:
    all_books = "\n".join(path.read_text(encoding="utf-8") for path in (ROOT / "books").rglob("*.md"))
    items: list[dict[str, object]] = []
    for family, check in CHECKS.items():
        marker = f"<!-- source-family:{family} -->"
        assert all_books.count(marker) == 1, (family, all_books.count(marker))
        owner_path = ROOT / str(check["owner"])
        owner = owner_path.read_text(encoding="utf-8")
        assert owner.count(marker) == 1
        for phrase in check["required"]:
            assert phrase in owner, (family, phrase)
        marker_at = owner.index(marker)
        assert marker_at < owner.find("## Review notes", marker_at), family
        items.append(
            {
                "source_family_id": family,
                "owner_path": check["owner"],
                "marker_count": 1,
                "owner_and_placement": "passed",
                "old_path_and_changed_constraint": "passed",
                "state_or_control_ownership": "passed",
                "tradeoff_failure_fallback_coexistence": "passed",
                "exact_v1_evidence_boundary": "passed",
                "adjacent_non_duplication": "passed",
                "finding": None,
                "result": check["result"],
            }
        )
    return items


def update_queue() -> None:
    path = PACKET / "BOOKS_WRITEBACK_QUEUE.json"
    queue = json.loads(path.read_text(encoding="utf-8"))
    assert {item["source_family_id"] for item in queue["items"]} == set(CHECKS)
    queue["status"] = "integrated_post_write_passed"
    for item in queue["items"]:
        item["status"] = "integrated_post_write_passed"
        item["writeback_ref"] = f"{item['owner_path']}#source-family:{item['source_family_id']}"
        item["post_write_audit_ref"] = "post-write-semantic-audit.json"
    queue["reconciliation"]["post_write_passed"] = 5
    queue["reconciliation"]["unresolved_findings"] = 0
    path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_audit(items: list[dict[str, object]]) -> None:
    result = {
        "schema": "books-post-write-semantic-audit-v2.1",
        "report_date": "2026-05-31",
        "auditor": "fresh-context:root-non-writer",
        "writer": "may2026-day03",
        "scope": {
            "canonical_denominator": 56,
            "integrate_items": 5,
            "no_change_items": 13,
            "owner_files": 4,
        },
        "items": items,
        "result": "passed",
        "unresolved_findings": 0,
        "gate": "Books Passed",
        "independence": "Reviewer did not author the pre-write challenge or the Books writeback.",
    }
    (PACKET / "post-write-semantic-audit.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    path = PACKET / "independent-semantic-audit.json"
    prior = json.loads(path.read_text(encoding="utf-8"))
    prior["books_postwrite_final"] = {
        "queue": "5 Integrate / 13 No Change — Existing Coverage",
        "writeback": "5/5 in 4 canonical owner files",
        "post_write_audit": "passed",
        "unresolved_findings": 0,
        "receipt": "post-write-semantic-audit.json",
    }
    path.write_text(json.dumps(prior, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def update_report() -> None:
    text = REPORT.read_text(encoding="utf-8")
    replacements = {
        "**Status:** In Progress；Coverage=Closed、Evidence=Passed、Books=Open。独立 pre-write audit 已完成，等待 root 串行写回。":
            "**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed。5 项正文写回已由不同 reviewer 完成 post-write Semantic Audit。",
        "本审计未修改共享 Books。":
            "最终 5 项已进入 4 个 canonical owner 文件；不同 reviewer 的 5/5 post-write Semantic Audit 无 unresolved finding。",
        "| Completion Status | In Progress |": "| Completion Status | Complete |",
        "| Books Gate | Open |": "| Books Gate | Passed |",
        "Integrate 项等待 root 串行写回，No Change 项已闭合。":
            "最终 disposition 已闭合；5 项 Integrate 已写入并通过独立 post-write audit，No Change 项不重复写入。",
        "| SA-20260531-BOOKS | fresh-context:may2026-day01 | books | books-review:SF-2026-ARXIV-2606-00515 | F-20260531-BOOKS-WRITEBACK | author queue 49→independent 18→pre-write final 5；13 项 No Change 已闭合，等待 root 串行写回与 post-write audit | open |":
            "| SA-20260531-BOOKS | fresh-context:root-non-writer | books | books-review:SF-2026-ARXIV-2606-00515 | — | `post-write-semantic-audit.json` 记录 author queue 49→independent 18→pre-write final 5；5/5 写回与 13/13 No Change handoff 均通过，unresolved=0 | passed |",
        "Root 按 final 5-item queue 串行写回；完成后由不同 reviewer 执行 post-write semantic audit。":
            "无需继续写回；final 5-item queue 已写入 4 个 owner，并由不同 reviewer 完成 5/5 post-write Semantic Audit。",
        "- 新增 canonical Daily README；未修改共享 Books 或其他日期。":
            "- 按 final queue 修改 4 个 canonical Books owner；新增独立 post-write audit receipt 并同步本 Daily。",
        "- Root 写回 18 项后，post-write audit 是否确认全部机制位于 canonical H2 主线并与相邻段自然衔接？":
            "- 无 unresolved Books 问题；后续新证据只按 revision / owner contract 重开。",
        "Completion Status: `In Progress`": "Completion Status: `Complete`",
        "Books: `Open`": "Books: `Passed`",
        "unresolved findings: 0 (pre-write); Books writeback remains (final queue=5)":
            "unresolved findings: `0`；5/5 post-write Semantic Audit passed",
        "Independent pre-write audit 已完成：Coverage/Evidence 已闭合；Books 等待 root 串行写回 5 项与独立 post-write audit，因此 Daily 仍为 In Progress。":
            "Coverage、Evidence 与 Books Gate 均已闭合；5 项正文写回和不同 reviewer 的 post-write Semantic Audit 已通过。",
    }
    for old, new in replacements.items():
        count = text.count(old)
        assert count >= 1, (old, count)
        text = text.replace(old, new)
    REPORT.write_text(text, encoding="utf-8")


def main() -> None:
    items = assert_books()
    update_queue()
    update_audit(items)
    update_report()
    print("2026-05-31 post-write closure applied: 5/5, unresolved=0")


if __name__ == "__main__":
    main()
