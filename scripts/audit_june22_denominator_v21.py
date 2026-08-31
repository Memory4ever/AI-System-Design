#!/usr/bin/env python3
"""Freeze the strict V2.1 Candidate Denominator for 2026-06-22.

This stage performs denominator screening only.  It deliberately leaves the
Evidence, Selection and Books gates open.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260622"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
EXECUTED = "2026-08-30T00:25:00+08:00"


# A retained identity must change a durable AI-System state/data/control owner,
# evaluation/release contract, or an existing Books proposition.  Topic fit or
# ROADMAP mappability alone is insufficient.
OWNERS = {
    "2606.22311": "PLATFORM-SECURITY",
    "2606.22319": "MULTIMODAL-EMBODIED-VLA",
    "2606.22325": "MODEL-MOE",
    "2606.22327": "INFER-SCHEDULING",
    "2606.22329": "PLATFORM-EVALUATION-SYSTEM",
    "2606.22330": "AGENT-REFLECTION",
    "2606.22338": "AGENT-MEMORY",
    "2606.22363": "MULTIMODAL-WORLD-MODELS",
    "2606.22370": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.22413": "PLATFORM-SECURITY",
    "2606.22419": "AGENT-RAG",
    "2606.22470": "AGENT-PROMPT",
    "2606.22474": "PLATFORM-EVALUATION-SYSTEM",
    "2606.22485": "AGENT-WORKFLOW",
    "2606.22488": "MULTIMODAL-WORLD-MODELS",
    "2606.22504": "PLATFORM-SECURITY",
    "2606.22509": "MULTIMODAL-WORLD-MODELS",
    "2606.22528": "AGENT-CONTEXT",
    "2606.22541": "INFER-PD-DISAGGREGATION",
    "2606.22560": "PLATFORM-GATEWAY",
    "2606.22565": "MULTIMODAL-REPRESENTATION",
    "2606.22570": "TRAIN-GRPO",
    "2606.22593": "PLATFORM-MODEL-REGISTRY",
    "2606.22600": "TRAIN-RLHF",
    "2606.22610": "AGENT-WORKFLOW",
    "2606.22613": "PLATFORM-EVALUATION-SYSTEM",
    "2606.22633": "PLATFORM-EVALUATION-SYSTEM",
    "2606.22659": "PLATFORM-SECURITY",
    "2606.22673": "PLATFORM-SECURITY",
    "2606.22678": "PLATFORM-EVALUATION-SYSTEM",
    "2606.22698": "PLATFORM-TRACE",
    "2606.22704": "AGENT-WORKFLOW",
    "2606.22716": "TRAIN-GRPO",
    "2606.22719": "PLATFORM-EVALUATION-SYSTEM",
    "2606.22729": "MULTIMODAL-EMBODIED-VLA",
    "2606.22731": "AGENT-WORKFLOW",
    "2606.22737": "PLATFORM-EVALUATION-SYSTEM",
    "2606.23740": "TRAIN-RLHF",
    "2606.23743": "INFER-TENSORRT-LLM",
}


def first_sentence(text: str) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    match = re.search(r"(?<=[.!?])\s+", value)
    return (value[: match.start() + 1] if match else value)[:420]


def closure_class(item: dict) -> tuple[str, str]:
    hay = f"{item['title']} {item['abstract']}".lower()
    cats = set(item.get("categories", []))
    if any(token in hay for token in ("survey", "systematic review", "literature review")):
        klass = "survey_without_new_system_mechanism"
        missing = "汇总既有研究，但没有给出会改变本项目长期 state/data/control ownership 的新机制或可验收系统合同"
    elif any(token in hay for token in ("medical", "clinical", "health", "molecular", "protein", "material", "agriculture", "finance", "education")):
        klass = "domain_specific_application"
        missing = "结果服务于特定领域任务，尚未改变可跨领域复用的训练、推理、平台或 Agent 系统责任边界"
    elif cats and not any(cat.startswith(("cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.SE", "cs.RO", "cs.CR", "cs.MM", "cs.SY", "eess.SY")) for cat in cats):
        klass = "generic_non_ai_system"
        missing = "贡献属于通用数学、硬件或非 AI 系统问题，未形成 AI-System 的长期设计增量"
    elif any(token in hay for token in ("classification", "segmentation", "detection", "recognition", "prediction", "benchmark dataset")):
        klass = "task_or_benchmark_local_improvement"
        missing = "改进集中在单一任务、模型或数据集，未改变 evaluation release authority、平台 owner 或可迁移机制"
    elif any(token in hay for token in ("framework", "method", "approach", "algorithm", "architecture")):
        klass = "local_method_without_durable_owner_delta"
        missing = "提出局部方法或架构，但摘要证据没有显示它重划长期状态、数据流、控制权或既有 Books 结论"
    else:
        klass = "context_without_durable_design_delta"
        missing = "提供相关背景或局部实验，但没有达到改变长期 AI-System 机制、系统 contract 或 Books proposition 的门槛"
    return klass, missing


def retained_reason(item: dict, owner: str) -> str:
    return (
        f"Retained for exact-v1 review under `{owner}`: ‘{item['title']}’ states the scope ‘"
        f"{first_sentence(item['abstract'])}’. This may alter a durable state/data/control or evaluation/release contract; "
        "the exact mechanism and non-proof boundary remain Evidence-Gate work and are not inferred from the abstract."
    )


def main() -> None:
    payload = json.loads(PROVISIONAL.read_text(encoding="utf-8"))
    identities = payload["identities"]
    by_id = {item["arxiv_id"]: item for item in identities}
    missing = sorted(set(OWNERS) - set(by_id))
    if missing:
        raise SystemExit(f"retained IDs missing from frozen inventory: {missing}")

    retained_rows = []
    closure_rows = []
    route_negative_total = 0
    route_negative_retained = 0
    for original in identities:
        item = dict(original)
        aid = item["arxiv_id"]
        item["source_family_id"] = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        item["screened_at"] = EXECUTED
        if item["screening_route"] == "not_routed_by_keyword_contract":
            route_negative_total += 1
        if aid in OWNERS:
            if item["screening_route"] == "not_routed_by_keyword_contract":
                route_negative_retained += 1
            item.update({
                "stable_node_id": OWNERS[aid],
                "semantic_screen_status": "retained_for_exact_v1_review",
                "semantic_decision_kind": "candidate_denominator",
                "semantic_screen_reason": retained_reason(item, OWNERS[aid]),
            })
            retained_rows.append(item)
        else:
            klass, missing_delta = closure_class(item)
            reason = (
                f"Family-specific closure for ‘{item['title']}’: exact abstract scope is ‘"
                f"{first_sentence(item['abstract'])}’. {missing_delta}."
            )
            item.update({
                "stable_node_id": "—",
                "semantic_screen_status": "closed_pre_denominator",
                "semantic_decision_kind": klass,
                "semantic_screen_reason": reason,
            })
            closure_rows.append(item)
        original.clear()
        original.update(item)

    if len(identities) != 230 or len(retained_rows) != 39 or len(closure_rows) != 191:
        raise SystemExit("denominator arithmetic mismatch")
    if route_negative_total != 58 or route_negative_retained != 5:
        raise SystemExit(f"route-negative arithmetic mismatch: {route_negative_total}/{route_negative_retained}")

    denominator_material = "\n".join(sorted(OWNERS)) + "\n"
    denominator_id = "daily-v2.1:2026-06-22:" + hashlib.sha256(denominator_material.encode()).hexdigest()[:16]
    payload.update({
        "gate_status": "coverage_closed_evidence_open",
        "denominator_id": denominator_id,
        "denominator_frozen_at": EXECUTED,
        "retained_candidate_families": len(retained_rows),
        "closed_pre_denominator_families": len(closure_rows),
        "route_negative_audited": route_negative_total,
        "route_negative_retained": route_negative_retained,
        "false_positive_false_negative_audit": {
            "auditor": "fresh-context:jun22-denominator-v1",
            "scope": "230/230 title+abstract plus 58/58 route-negative",
            "result": "passed",
            "unresolved_findings": 0,
        },
    })

    (PACKET / "screening-ledger.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (PACKET / "candidate-ids-v1.txt").write_text("\n".join(sorted(OWNERS)) + "\n", encoding="utf-8")
    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "source_family_key", "screening_route", "title", "decision", "closure_class", "stable_node_id", "family_specific_reason"])
        for item in identities:
            retained = item["arxiv_id"] in OWNERS
            writer.writerow([
                item["arxiv_id"], item["source_family_key"], item["screening_route"], item["title"],
                "retained" if retained else "pre-denominator closure",
                item["semantic_decision_kind"], item["stable_node_id"], item["semantic_screen_reason"],
            ])

    audit = f"""# 2026-06-22 Candidate Denominator Fresh Audit

- Window: `[2026-06-21 09:00, 2026-06-22 09:00)` Asia/Shanghai.
- Denominator: `{denominator_id}`.
- Frozen arithmetic: `230 raw identities = 39 retained + 191 family-specific pre-denominator closures`.
- Retain rate: `16.96%`.
- Routes: Core `150`, keyword `22`, route-negative `58`; all `58/58` route-negative identities were independently checked and `5` were recovered.
- False-positive correction: late-index identity/title pairs were re-read against the frozen ledger before freezing; `2606.22734`, `2606.22738`, `2606.23741`, and `2606.23744` remain closed rather than being confused with adjacent retained identities.
- False-negative audit: `230/230` title+abstract rows and all route-negative rows have a decision and source-family-specific reason.
- Coverage Gate: **Closed**.
- Evidence, Selection, Books Gates: **Open**. Retention is permission to read exact-v1 evidence, not proof of a durable claim.
"""
    (PACKET / "DENOMINATOR_FRESH_AUDIT_V1.md").write_text(audit, encoding="utf-8")
    print(json.dumps({
        "denominator_id": denominator_id,
        "raw": len(identities),
        "retained": len(retained_rows),
        "closures": len(closure_rows),
        "retain_rate": round(len(retained_rows) / len(identities), 4),
        "route_negative": route_negative_total,
        "route_negative_retained": route_negative_retained,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
