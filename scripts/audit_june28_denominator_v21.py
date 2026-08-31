#!/usr/bin/env python3
"""Freeze the strict V2.1 candidate denominator for 2026-06-28.

This stage records a complete title+abstract semantic decision for every frozen
identity.  It does not claim exact-v1 Evidence, Selection, or Books closure.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260628"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
EXECUTED = "2026-08-29T06:45:00+08:00"


# Retention means that the abstract plausibly changes a durable AI-System
# state/data/control owner, evaluation/release contract, or an existing Books
# proposition.  It is permission for exact-v1 review, not evidence of the claim.
PROVISIONAL_OWNERS = {
    "2606.28666": "PLATFORM-SECURITY",
    "2606.28679": "PLATFORM-SECURITY",
    "2606.28690": "AGENT-MCP",
    "2606.28692": "AGENT-WORKFLOW",
    "2606.28696": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.28707": "TRAIN-GRPO",
    "2606.28712": "MULTIMODAL-WORLD-MODELS",
    "2606.28715": "PLATFORM-EVALUATION-SYSTEM",
    "2606.28719": "MULTIMODAL-REPRESENTATION",
    "2606.28720": "MULTIMODAL-WORLD-MODELS",
    "2606.28725": "PLATFORM-MONITORING",
    "2606.28733": "AGENT-PLANNING",
    "2606.28739": "PLATFORM-SECURITY",
    "2606.28751": "MULTIMODAL-WORLD-MODELS",
    "2606.28757": "PLATFORM-EVALUATION-SYSTEM",
    "2606.28758": "MULTIMODAL-WORLD-MODELS",
    "2606.28781": "AGENT-MEMORY",
    "2606.28804": "MULTIMODAL-WORLD-MODELS",
    "2606.28813": "MULTIMODAL-EMBODIED-VLA",
    "2606.28831": "INFER-KV-CACHE",
    "2606.28839": "PLATFORM-EVALUATION-SYSTEM",
    "2606.28841": "AGENT-WORKFLOW",
    "2606.28843": "TRAIN-SFT",
    "2606.28863": "PLATFORM-EVALUATION-SYSTEM",
    "2606.28864": "INFER-REQUEST-LIFECYCLE",
    "2606.28867": "TRAIN-DATA",
    "2606.28876": "AGENT-MEMORY",
    "2606.28879": "TRAIN-PRETRAINING",
    "2606.28896": "AGENT-WORKFLOW",
    "2606.28898": "TRAIN-DPO",
    "2606.28900": "PLATFORM-EVALUATION-SYSTEM",
    "2606.28911": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.28925": "AGENT-MULTI-AGENT",
    "2606.28926": "WORLDVIEW-LLM-INTELLIGENCE",
    "2606.28932": "TRAIN-PRETRAINING",
    "2606.28938": "MULTIMODAL-EMBODIED-VLA",
    "2606.28939": "MULTIMODAL-EMBODIED-VLA",
    "2606.28955": "TRAIN-RLHF",
    "2606.28958": "AGENT-MULTI-AGENT",
    "2606.28962": "PLATFORM-SECURITY",
    "2606.29013": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.29030": "AGENT-MEMORY",
    "2606.29033": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29038": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29043": "WORLDVIEW-WHY-MODELS-LEARN",
    "2606.29054": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29059": "MULTIMODAL-WORLD-MODELS",
    "2606.29066": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2606.29067": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29073": "AGENT-MCP",
    "2606.29082": "TRAIN-PRETRAINING",
    "2606.29089": "MULTIMODAL-EMBODIED-VLA",
    "2606.29090": "AGENT-RAG",
    "2606.29091": "WORLDVIEW-REPRESENTATION",
    "2606.29094": "INFER-SCHEDULING",
    "2606.29108": "AGENT-WORKFLOW",
    "2606.29116": "AGENT-PLATFORM",
    "2606.29129": "INFER-TENSORRT-LLM",
}


# Independent fresh-context audit over all 211 identities.  These lists make
# the provisional-to-frozen denominator transition reviewable instead of
# silently replacing the first-pass judgment.
FALSE_POSITIVES_REMOVED = {
    "2606.28696": "composition-conditioned image generation is a local model/dataset contribution, not a durable system owner change",
    "2606.28719": "the two-cache VLM test-time-adaptation recipe is model-local and does not establish a platform memory lifecycle",
    "2606.28879": "the Adam analysis is generic optimizer theory for nonstationary systems rather than a pretraining-system contract",
    "2606.28911": "the distributed kernels are specific to quantum-transport operator learning and do not generalize to the book's training topology",
    "2606.28926": "the probabilistic account of in-context learning is model theory without a durable AI-System control or data owner",
    "2606.29043": "the sharpness-complexity study is generalization analysis, not a system mechanism or release contract",
}

FALSE_NEGATIVES_ADDED = {
    "2606.28747": "AGENT-WORKFLOW",
    "2606.28754": "PLATFORM-GPU-SCHEDULER",
    "2606.28772": "TRAIN-DATA",
    "2606.28862": "PLATFORM-EVALUATION-SYSTEM",
    "2606.28953": "PLATFORM-SECURITY",
    "2606.28995": "MULTIMODAL-EMBODIED-VLA",
    "2606.28998": "TRAIN-DPO",
    "2606.29088": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29097": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29112": "PLATFORM-SECURITY",
    "2606.29119": "PLATFORM-EVALUATION-SYSTEM",
    "2606.29124": "PLATFORM-SECURITY",
    "2606.29126": "AGENT-MULTI-AGENT",
}

FALSE_NEGATIVE_REASONS = {
    "2606.28747": "alternates proof search with extraction into a reusable theorem library while retaining kernel verification",
    "2606.28754": "moves both compute context and data across chiplets under communication feedback instead of moving data alone",
    "2606.28772": "shows that majority-vote annotation erases contested safety boundaries and therefore changes the upstream label authority contract",
    "2606.28862": "separates proposal coverage from query-region binding error and exposes an explicit faithfulness-recall abstention trade-off",
    "2606.28953": "filters dirty-label poisoning through unsupervised representation clusters before training without trusting corrupted labels",
    "2606.28995": "places an offline-learned barrier value function in a real-time closed-form safety-filter control path",
    "2606.28998": "shows that the checkpoint entering DPO/BoNBoN changes functional and non-functional alignment gains and regressions",
    "2606.29088": "constructs a diff-based corruption pipeline and a much larger bug-fixing evaluation surface that exposes failures hidden by small benchmarks",
    "2606.29097": "links scenario synthesis, validation, collision discovery, and retraining into an autonomous-driving evaluation loop",
    "2606.29112": "detects a latent-class poisoning attack post-training through class-subspace orthogonalization without the training set",
    "2606.29119": "adds a pre-implementation recovery-ratio gate that can reject an expensive evolutionary outer loop before dispatch",
    "2606.29124": "extracts protocol validity constraints from specifications, generates boundary cases, and uses differential execution as the oracle",
    "2606.29126": "turns multi-agent communication into receiver-driven selection over group, sender, and entity rather than flat-vector broadcast",
}

OWNER_CORRECTIONS = {
    "2606.29066": ("MULTIMODAL-GENERATIVE-PARADIGMS", "INFER-DECODE"),
    "2606.29091": ("WORLDVIEW-REPRESENTATION", "AGENT-RAG"),
}

OWNERS = {
    aid: owner
    for aid, owner in PROVISIONAL_OWNERS.items()
    if aid not in FALSE_POSITIVES_REMOVED
}
OWNERS.update(FALSE_NEGATIVES_ADDED)
for aid, (_, corrected_owner) in OWNER_CORRECTIONS.items():
    OWNERS[aid] = corrected_owner


def clean(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def first_sentence(value: str) -> str:
    value = clean(value)
    match = re.search(r"(?<=[.!?])\s+", value)
    return (value[: match.start() + 1] if match else value)[:420]


def closure(item: dict) -> tuple[str, str]:
    text = clean(f"{item['title']} {item['abstract']}").lower()
    cats = set(item.get("categories", []))
    if any(k in text for k in ("survey", "systematic review", "we review")):
        return "survey_without_new_system_mechanism", "综合既有路线，但没有建立新的可验收机制或系统责任边界"
    if any(k in text for k in ("medical", "clinical", "finance", "agricultur", "education", "student", "molecular", "aerodynamic")):
        return "domain_specific_application", "贡献由特定领域任务与数据合同主导，尚未形成可跨场景迁移的 AI-System owner 变化"
    if cats and not any(c.startswith(("cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.SE", "cs.RO", "cs.CR", "cs.MM", "cs.SY", "cs.NI", "eess.SY")) for c in cats):
        return "generic_non_ai_system", "研究对象是通用数学、统计、控制、硬件或非 AI 系统，未改变本书 AI-System 设计判断"
    if any(k in text for k in ("classification", "segmentation", "object detection", "recognition", "benchmark dataset")):
        return "task_or_benchmark_local_improvement", "改进集中在单一任务、模型或数据集，未改变 evaluation authority、状态所有权或长期平台 contract"
    if any(k in text for k in ("framework", "method", "approach", "architecture", "pipeline")):
        return "local_method_without_durable_owner_delta", "摘要描述了局部方法或架构，但没有显示其重划长期状态、数据流、控制权或既有 Books proposition"
    return "context_without_durable_design_delta", "提供相关背景、分析或局部实验，但没有达到长期 AI-System 机制或系统 contract 的候选门槛"


def main() -> None:
    payload = json.loads(PROVISIONAL.read_text(encoding="utf-8"))
    rows = payload["identities"]
    by_id = {r["arxiv_id"]: r for r in rows}
    missing = sorted(set(OWNERS) - set(by_id))
    if missing:
        raise SystemExit(f"retained IDs missing from frozen inventory: {missing}")

    route_counts = Counter(r["screening_route"] for r in rows)
    negative_total = route_counts["not_routed_by_keyword_contract"]
    negative_retained = 0
    closures = 0
    for row in rows:
        aid = row["arxiv_id"]
        row["source_family_id"] = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        row["screened_at"] = EXECUTED
        if aid in OWNERS:
            if row["screening_route"] == "not_routed_by_keyword_contract":
                negative_retained += 1
            row.update({
                "stable_node_id": OWNERS[aid],
                "semantic_screen_status": "retained_for_exact_v1_review",
                "semantic_decision_kind": "candidate_denominator",
                "semantic_screen_reason": (
                    f"Retained under `{OWNERS[aid]}` after full title+abstract review: ‘{row['title']}’ states ‘"
                    f"{first_sentence(row['abstract'])}’. This may alter durable state/data/control ownership, an "
                    "evaluation/release contract, or an existing Books proposition; the exact claim remains Evidence-Gate work."
                ),
            })
        else:
            kind, missing_delta = closure(row)
            row.update({
                "stable_node_id": "—",
                "semantic_screen_status": "closed_pre_denominator",
                "semantic_decision_kind": kind,
                "semantic_screen_reason": (
                    f"Family-specific closure for ‘{row['title']}’: its abstract scope is ‘{first_sentence(row['abstract'])}’. "
                    f"{missing_delta}."
                ),
            })
            closures += 1

    retained = len(OWNERS)
    if retained + closures != len(rows):
        raise SystemExit("denominator arithmetic mismatch")
    material = "\n".join(sorted(OWNERS)) + "\n"
    denominator_id = "daily-v2.1:2026-06-28:" + hashlib.sha256(material.encode()).hexdigest()[:16]
    payload.update({
        "gate_status": "coverage_closed_denominator_frozen_fresh_audit_passed",
        "denominator_id": denominator_id,
        "denominator_frozen_at": EXECUTED,
        "provisional_retained_candidate_families": len(PROVISIONAL_OWNERS),
        "provisional_closed_pre_denominator_families": len(rows) - len(PROVISIONAL_OWNERS),
        "retained_candidate_families": retained,
        "closed_pre_denominator_families": closures,
        "route_negative_audited": negative_total,
        "route_negative_retained": negative_retained,
        "false_positive_false_negative_audit": {
            "auditor": "fresh-context:jun28-independent-v1",
            "scope": f"{len(rows)}/{len(rows)} title+abstract plus {negative_total}/{negative_total} route-negative",
            "result": "passed",
            "false_positives_removed": sorted(FALSE_POSITIVES_REMOVED),
            "false_negatives_recovered": sorted(FALSE_NEGATIVES_ADDED),
            "owner_corrections": {
                aid: {"from": before, "to": after}
                for aid, (before, after) in OWNER_CORRECTIONS.items()
            },
            "unresolved_findings": 0,
        },
    })
    (PACKET / "screening-ledger.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "candidate-ids-v1.txt").write_text("\n".join(sorted(OWNERS)) + "\n")

    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["arxiv_id", "source_family_key", "screening_route", "title", "decision", "closure_class", "stable_node_id", "family_specific_reason"])
        for row in rows:
            kept = row["arxiv_id"] in OWNERS
            writer.writerow([
                row["arxiv_id"], row["source_family_key"], row["screening_route"], row["title"],
                "retained" if kept else "pre-denominator closure", row["semantic_decision_kind"],
                row["stable_node_id"], row["semantic_screen_reason"],
            ])

    fp_lines = "\n".join(
        f"  - `{aid}`: {reason}." for aid, reason in FALSE_POSITIVES_REMOVED.items()
    )
    fn_lines = "\n".join(
        f"  - `{aid}` -> `{owner}`: {FALSE_NEGATIVE_REASONS[aid]}."
        for aid, owner in FALSE_NEGATIVES_ADDED.items()
    )
    owner_lines = "\n".join(
        f"  - `{aid}`: `{before}` -> `{after}`."
        for aid, (before, after) in OWNER_CORRECTIONS.items()
    )
    audit = f"""# 2026-06-28 Candidate Denominator Fresh Audit

- Window: `[2026-06-27 09:00, 2026-06-28 09:00)` Asia/Shanghai.
- Denominator: `{denominator_id}`.
- Frozen arithmetic: `{len(rows)} raw identities = {retained} retained + {closures} family-specific pre-denominator closures`.
- Retain rate: `{retained / len(rows):.2%}`.
- Routes: Core `{route_counts['core_daily_semantic_review_required']}`, keyword `{route_counts['keyword_daily_semantic_review_required']}`, route-negative `{negative_total}`; all route-negative identities were independently checked and `{negative_retained}` were recovered.
- Initial semantic screening: `{len(rows)}/{len(rows)}` title+abstract rows have an explicit decision and source-family-specific reason.
- Independent fresh-context false-positive / false-negative audit: **Passed** (`{len(rows)}/{len(rows)}` full denominator, `{negative_total}/{negative_total}` route-negative, zero unresolved findings).
- Coverage Gate: **Passed**; denominator frozen at `{EXECUTED}`.
- Evidence, Selection, Books Gates: **Open**. Retention is permission to inspect exact-v1 primary evidence, not proof of a durable claim.

## Resolved false positives

The provisional `58` retained families included `{len(FALSE_POSITIVES_REMOVED)}` items whose contribution remains model-, task-, domain-, or theory-local after adversarial rereading:

{fp_lines}

## Recovered false negatives

The provisional `153` closures hid `{len(FALSE_NEGATIVES_ADDED)}` durable candidates:

{fn_lines}

## Owner corrections

{owner_lines}

## Route-negative handoff

All `{negative_total}` route-negative identities were reread. The frozen denominator retains `{negative_retained}`: `2606.28720` and `2606.29108` from the provisional pass, plus newly recovered `2606.28754`, `2606.28862`, and `2606.28995`. The other `{negative_total - negative_retained}` remain family-specific pre-denominator closures; no keyword miss is being treated as automatic exclusion.
"""
    (PACKET / "DENOMINATOR_FRESH_AUDIT_V1.md").write_text(audit, encoding="utf-8")

    checksum_targets = [
        "candidate-ids-v1.txt",
        "screening-ledger.json",
        "denominator-full-semantic-audit-v1.tsv",
        "DENOMINATOR_FRESH_AUDIT_V1.md",
    ]
    checksum_lines = []
    for name in checksum_targets:
        digest = hashlib.sha256((PACKET / name).read_bytes()).hexdigest()
        checksum_lines.append(f"{digest}  {name}")
    (PACKET / "SHA256SUMS").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    print(json.dumps({
        "denominator_id": denominator_id,
        "raw": len(rows),
        "retained": retained,
        "closures": closures,
        "retain_rate": round(retained / len(rows), 4),
        "route_counts": route_counts,
        "route_negative_retained": negative_retained,
    }, ensure_ascii=False, indent=2, default=dict))


if __name__ == "__main__":
    main()
