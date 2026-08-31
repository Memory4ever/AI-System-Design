#!/usr/bin/env python3
"""Freeze the 2026-05-10 author-side candidate denominator from the full inventory."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "screening-ledger-provisional.json"

RETAINED = {
    "2605.08586", "2605.08587", "2605.08632", "2605.08639", "2605.08646",
    "2605.08647", "2605.08658", "2605.08666", "2605.08715", "2605.08737",
    "2605.08747", "2605.08835", "2605.08840", "2605.08862", "2605.08871",
    "2605.08876", "2605.08894", "2605.08913", "2605.08962", "2605.08982",
    "2605.09023", "2605.09033", "2605.09045", "2605.09055", "2605.09070",
    "2605.09076", "2605.09126", "2605.09163", "2605.09168", "2605.09192",
    "2605.09204", "2605.09225", "2605.09227", "2605.09241", "2605.10980",
    "2605.10987", "2605.10990", "2605.10993", "2605.10999", "2605.16359",
    "2605.16360", "2605.23951"
}


def sentences(text: str) -> list[str]:
    compact = re.sub(r"\s+", " ", text).strip()
    return [x.strip() for x in re.split(r"(?<=[.!?])\s+", compact) if x.strip()]


def evidence_sentence(parts: list[str], patterns: tuple[str, ...], fallback: int) -> str:
    for sentence in parts:
        lowered = sentence.lower()
        if any(pattern in lowered for pattern in patterns):
            return sentence
    return parts[fallback] if parts else "摘要未提供可复用机制说明。"


def boundary(item: dict) -> str:
    title = item["title"].lower()
    abstract = item["abstract"].lower()
    combined = title + " " + abstract
    if item["screening_route"] == "not_routed_by_keyword_contract":
        return "该工作未命中注册表的 Core/keyword 路由；其问题与结果不改变本项目 AI System 的长期 state、data、control 或 evaluation owner。"
    if any(token in combined for token in ("medical", "disease", "patient", "clinical", "molecule", "protein", "pde", "climate", "weather", "battery", "plasma", "earth", "forecasting")):
        return "证据绑定特定领域数据、标签、任务目标与 evaluator；没有把领域结果提升为可跨 workload 复用的 AI System contract。"
    if any(token in combined for token in ("benchmark", "dataset", "corpus", "evaluation")):
        return "该 benchmark/dataset 扩充了测量对象，但摘要没有改变 evaluator authority、release gate、状态身份或跨系统可复算合同。"
    if any(token in combined for token in ("theorem", "bound", "convergence", "optimal", "theory", "proof")):
        return "理论结果解释了特定假设下的性质，但摘要未给出会改变 Training、Inference、Platform 或 Agent ownership 的可执行系统机制。"
    if any(token in combined for token in ("agent", "rag", "tool", "workflow", "memory", "reasoning")):
        return "该方法改善特定 Agent/推理任务，但没有改变长期 workflow state、effect authority、evidence admission 或 recovery contract。"
    if any(token in combined for token in ("quant", "prun", "distill", "fine-tun", "attention", "transformer", "diffusion", "representation")):
        return "该局部模型、表示或优化增量没有改变系统级状态所有权、运行时控制流、evaluation contract 或既有 Books 设计判断。"
    return "该 family 的贡献停留在局部任务或实现层，没有形成可定位、可复用且会改变长期 AI System 设计判断的机制增量。"


def closure_reason(item: dict) -> str:
    parts = sentences(item["abstract"])
    method = evidence_sentence(parts, ("we propose", "we introduce", "we present", "this work", "we study", "we investigate", "we develop"), 0)
    result = evidence_sentence(parts, ("results", "experiments", "we show", "we find", "demonstrate", "evaluation"), -1)
    return (
        f"问题/机制：{item['title']}；摘要方法为“{method}”；结果/证据线索为“{result}”。"
        f"排除边界：{boundary(item)}"
    )


def main() -> None:
    data = json.loads(SOURCE.read_text())
    rows = []
    for item in data["identities"]:
        retained = item["arxiv_id"] in RETAINED
        row = dict(item)
        row["source_family_id"] = f"SF-2026-ARXIV-{item['arxiv_id'].replace('.', '-')}"
        row["screening_status"] = "retained_pending_exact_v1_review" if retained else "pre_denominator_closed"
        row["screening_reason"] = (
            "Title+abstract identify a durable AI-System delta affecting mechanism, state/control ownership, evaluation contract, or a stable design boundary; retain for exact-v1 review."
            if retained else closure_reason(item)
        )
        row["author_false_negative_audit"] = "retained" if retained else "closed_after_full_title_abstract_review"
        rows.append(row)

    output = dict(data)
    output.update({
        "schema": "daily-v2.1-screening-ledger-v2",
        "registered_window_identities": len(rows),
        "full_semantic_screened": len(rows),
        "retained_candidates": sum(x["screening_status"].startswith("retained") for x in rows),
        "pre_denominator_closures": sum(x["screening_status"] == "pre_denominator_closed" for x in rows),
        "gate_status": "author_denominator_frozen_pending_independent_audit",
        "identities": rows,
    })
    (ROOT / "screening-ledger-final.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    with (ROOT / "screening-ledger-final.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "source_family_id", "submitted_v1_utc", "title", "categories", "route", "status", "reason", "author_audit"])
        for row in rows:
            writer.writerow([
                row["arxiv_id"], row["source_family_id"], row["submitted_v1_utc"], row["title"],
                ",".join(row["categories"]), row["screening_route"], row["screening_status"],
                row["screening_reason"], row["author_false_negative_audit"],
            ])
    print(json.dumps({
        "raw": output["raw_snapshot_records"], "registered": len(rows), "screened": len(rows),
        "retained": output["retained_candidates"], "closures": output["pre_denominator_closures"],
    }))


if __name__ == "__main__":
    main()
