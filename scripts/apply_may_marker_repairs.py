#!/usr/bin/env python3
"""Apply the reviewed, marker-only May 2026 Books trace repairs.

The semantic integration already exists.  This script only binds the existing
owner paragraph to its canonical Source Family ID.  It is intentionally
fail-closed: every anchor and every target marker must be unique before any
file is written.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PLAN_PATHS = [
    "papers/2026/05/_sources/daily-20260501/marker-repair-plan-readonly.json",
    "papers/2026/05/_sources/daily-20260502/stable-source-family-marker-repair-plan.json",
    "papers/2026/05/_sources/daily-20260504/books-marker-repair-plan.json",
    "papers/2026/05/_sources/daily-20260505/stable-source-family-marker-repair-plan.json",
    "papers/2026/05/_sources/daily-20260506/stable-source-family-marker-repair-plan.json",
    "papers/2026/05/_sources/daily-20260508/books-marker-repair-plan.json",
    "papers/2026/05/_sources/daily-20260509/stable-source-family-marker-repair-plan.json",
    "papers/2026/05/_sources/daily-20260510/stable-source-family-marker-repair-plan.json",
]


@dataclass(frozen=True)
class Repair:
    family: str
    target: str
    marker: str
    anchor: str
    position: str


def quoted_locator(value: str) -> str:
    match = re.search(r"`([^`]+)`", value)
    if not match:
        raise ValueError(f"locator has no exact quoted anchor: {value}")
    return match.group(1)


MAY11_REPAIRS = [
    Repair(
        "SF-LLM-AGENTS-ALREADY-KNOW-WHEN-TO-CALL-TOOLS-EVEN-WITHOUT-REASONING",
        "books/part-07-agent/78-tool-calling.md",
        "<!-- source-family:SF-LLM-AGENTS-ALREADY-KNOW-WHEN-TO-CALL-TOOLS-EVEN-WITHOUT-REASONING -->",
        "纯文本回答无法满足任务 contract。调用前应先按三类压力判断",
        "before_paragraph",
    ),
    Repair(
        "SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I",
        "books/part-07-agent/84-agent-platform.md",
        "<!-- source-family:SF-DO-SELF-EVOLVING-AGENTS-FORGET-CAPABILITY-DEGRADATION-AND-PRESERVATION-I -->",
        "Promotion Gate 应冻结一组 capability vector",
        "before_paragraph",
    ),
    Repair(
        "SF-SIMWORLD-STUDIO-AUTOMATIC-ENVIRONMENT-GENERATION-WITH-EVOLVING-CODING-AG",
        "books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md",
        "<!-- source-family:SF-SIMWORLD-STUDIO-AUTOMATIC-ENVIRONMENT-GENERATION-WITH-EVOLVING-CODING-AG -->",
        "因此生成环境不能只是临时脚本输出",
        "before_paragraph",
    ),
    Repair(
        "SF-MONITORINGBENCH-SEMI-AUTOMATED-RED-TEAMING-FOR-AGENT-MONITORING",
        "books/part-06-ai-infrastructure/67-monitoring.md",
        "<!-- source-family:SF-MONITORINGBENCH-SEMI-AUTOMATED-RED-TEAMING-FOR-AGENT-MONITORING -->",
        "每轮结果必须绑定 attack generator",
        "before_paragraph",
    ),
    Repair(
        "SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS",
        "books/part-06-ai-infrastructure/66-evaluation-system.md",
        "<!-- source-family:SF-CAUSAL-STATE-BINDING-PREDICTS-ACTION-CONTROL-IN-LANGUAGE-AGENTS -->",
        "EvalSpec 需要冻结 event/state schema",
        "before_paragraph",
    ),
    Repair(
        "SF-RUBRICREFINE-IMPROVING-TOOL-USE-AGENT-RELIABILITY-WITH-TRAINING-FREE-PRE",
        "books/part-07-agent/78-tool-calling.md",
        "<!-- source-family:SF-RUBRICREFINE-IMPROVING-TOOL-USE-AGENT-RELIABILITY-WITH-TRAINING-FREE-PRE -->",
        "候选 program 还应在执行前依据当前 task",
        "before_paragraph",
    ),
]


def load_repairs() -> list[Repair]:
    repairs: list[Repair] = []
    for rel_path in PLAN_PATHS:
        plan = json.loads((ROOT / rel_path).read_text(encoding="utf-8"))
        for item in plan["items"]:
            if "canonical_family_id" in item and "exact_anchor" in item:
                if item.get("semantic_status") != "marker_only_ready":
                    raise ValueError(
                        f"non-marker repair in {rel_path}: {item['canonical_family_id']}"
                    )
                if item.get("action") != "insert_after_exact_anchor":
                    raise ValueError(
                        f"unsupported repair action in {rel_path}: {item['canonical_family_id']}"
                    )
                repairs.append(
                    Repair(
                        item["canonical_family_id"],
                        item["target_file"],
                        item["marker"],
                        item["exact_anchor"],
                        "after_anchor",
                    )
                )
                continue
            repair_class = item.get("repair_action") or item.get("classification")
            if repair_class != "marker_only":
                raise ValueError(f"non-marker repair in {rel_path}: {item['source_family_id']}")
            if item.get("semantic_gap") not in (None, False) or item.get("body_change_required") not in (None, False):
                raise ValueError(f"semantic repair is not marker-only: {item['source_family_id']}")
            if "marker" in item:
                position = (
                    "after_paragraph"
                    if item["source_family_id"] in {
                        "SF-2026-ARXIV-2605-04116",
                        "SF-2026-ARXIV-2605-04135",
                    }
                    else "after_anchor"
                )
                repairs.append(
                    Repair(
                        item["source_family_id"],
                        item["target_file"],
                        item["marker"],
                        item["insert_after_anchor"],
                        position,
                    )
                )
            else:
                family = item["source_family_id"]
                target = item["owner_path"]
                contract = plan["marker_contract"]
                repairs.extend(
                    [
                        Repair(
                            family,
                            target,
                            contract["start"].replace("<Source Family ID>", family),
                            quoted_locator(item["start_locator"]),
                            "before_paragraph",
                        ),
                        Repair(
                            family,
                            target,
                            contract["end"].replace("<Source Family ID>", family),
                            quoted_locator(item["end_locator"]),
                            "after_paragraph",
                        ),
                    ]
                )
    repairs.extend(MAY11_REPAIRS)
    return repairs


def paragraph_start(text: str, position: int) -> int:
    start = text.rfind("\n\n", 0, position)
    return 0 if start < 0 else start + 2


def paragraph_end(text: str, position: int) -> int:
    end = text.find("\n\n", position)
    return len(text) if end < 0 else end


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="write the validated marker-only edits")
    args = parser.parse_args()

    repairs = load_repairs()
    families = {repair.family for repair in repairs}

    pending_by_file: dict[Path, list[Repair]] = {}
    already_present = 0
    for repair in repairs:
        target = ROOT / repair.target
        text = target.read_text(encoding="utf-8")
        marker_count = text.count(repair.marker)
        if marker_count == 1:
            already_present += 1
            continue
        if marker_count != 0:
            raise ValueError(f"marker count {marker_count}: {repair.family} in {repair.target}")
        if text.count(repair.anchor) != 1:
            raise ValueError(
                f"anchor count {text.count(repair.anchor)}: {repair.family} in {repair.target}"
            )
        pending_by_file.setdefault(target, []).append(repair)

    changed = 0
    for target, target_repairs in pending_by_file.items():
        text = target.read_text(encoding="utf-8")
        operations: list[tuple[int, str]] = []
        for repair in target_repairs:
            anchor_at = text.index(repair.anchor)
            if repair.position == "after_anchor":
                insert_at = anchor_at + len(repair.anchor)
                insert = f"\n\n{repair.marker}"
            elif repair.position == "after_paragraph":
                insert_at = paragraph_end(text, anchor_at)
                insert = f"\n{repair.marker}"
            else:
                insert_at = paragraph_start(text, anchor_at)
                insert = f"{repair.marker}\n"
            operations.append((insert_at, insert))
        for insert_at, insert in sorted(operations, reverse=True):
            text = text[:insert_at] + insert + text[insert_at:]
        for repair in target_repairs:
            if text.count(repair.marker) != 1:
                raise ValueError(f"post-edit marker count failed: {repair.family}")
        if args.apply:
            target.write_text(text, encoding="utf-8")
        changed += len(target_repairs)

    mode = "applied" if args.apply else "dry-run"
    print(
        f"{mode}: families={len(families)} marker_operations={len(repairs)} "
        f"pending={changed} already_present={already_present} "
        f"files={len(pending_by_file)}"
    )


if __name__ == "__main__":
    main()
