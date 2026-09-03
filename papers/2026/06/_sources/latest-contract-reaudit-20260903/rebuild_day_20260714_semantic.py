#!/usr/bin/env python3
"""Freeze the title+abstract semantic denominator for 2026-07-14.

Every raw identity receives a final semantic disposition.  The explicit route
table is the result of the false-negative audit; everything else keeps its
family-specific title+abstract closure evidence from the canonical checkpoint.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260714"
RAW = PACKET / "canonical-raw-identity-inventory-v2.1.json.gz"
PRIOR = PACKET / "canonical-semantic-screening-checkpoint-v2.1.json.gz"
DECISIONS = PACKET / "fresh-context-semantic-decisions-v2.1.json.gz"
DENOMINATOR = PACKET / "candidate-denominator-v2.1.json"
RUN_AT = "2026-09-04T00:40:00+08:00"

# id | Stable Node ID | semantic route | relation
ROUTES = """
2607.09665|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|principle_reuse
2607.09682|PLATFORM-TRACE|evidence_state|direct_evolution
2607.09686|INFER-SCHEDULING|serving_runtime|alternative_branch
2607.09689|AGENT-WORKFLOW|evidence_state|direct_evolution
2607.09691|AGENT-CONTEXT|agent_state|direct_evolution
2607.09692|PLATFORM-SECURITY|provenance_security|alternative_branch
2607.09697|PLATFORM-SECURITY|safety_contract|alternative_branch
2607.09709|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|principle_reuse
2607.09711|AGENT-PLATFORM|evaluation_contract|direct_evolution
2607.09744|PLATFORM-SECURITY|safety_contract|direct_evolution
2607.09748|AGENT-PLATFORM|evidence_state|structural_candidate
2607.09759|AGENT-MEMORY|agent_state|direct_evolution
2607.09770|AGENT-PLATFORM|safety_contract|direct_evolution
2607.09773|TRAIN-GRPO|training_mechanism|direct_evolution
2607.09776|MULTIMODAL-EMBODIED-VLA|training_mechanism|direct_evolution
2607.09786|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|principle_reuse
2607.09791|INFER-DECODE|serving_runtime|corrective_evidence
2607.09794|AGENT-CONTEXT|agent_state|direct_evolution
2607.09800|TRAIN-PRETRAINING|training_correctness|corrective_evidence
2607.09802|PLATFORM-GPU-SCHEDULER|resource_control|alternative_branch
2607.09803|AGENT-REFLECTION|model_mechanism|explanatory_analogy
2607.09804|PLATFORM-SECURITY|safety_contract|release_security_override
2607.09822|AGENT-MEMORY|agent_state|direct_evolution
2607.09889|MODEL-LONG-CONTEXT|model_mechanism|alternative_branch
2607.09992|INFER-SCHEDULING|slo_control|direct_evolution
2607.09996|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.09999|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.10044|INFER-DECODE|serving_runtime|direct_evolution
2607.10059|AGENT-TOOL-CALLING|safety_contract|direct_evolution
2607.10079|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.10096|AGENT-RAG|retrieval_system|direct_evolution
2607.10103|PLATFORM-SECURITY|provenance_security|principle_reuse
2607.10110|MODEL-LONG-CONTEXT|model_mechanism|direct_evolution
2607.10139|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|alternative_branch
2607.10152|AGENT-MULTI-AGENT|evidence_state|explanatory_analogy
2607.10183|INFER-TENSORRT-LLM|serving_runtime|direct_evolution
2607.10186|INFER-GPU-MEMORY|serving_runtime|direct_evolution
2607.10198|AGENT-RAG|evidence_state|direct_evolution
2607.10203|MULTIMODAL-WORLD-MODELS|evaluation_contract|corrective_evidence
2607.10226|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.10240|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.10252|PLATFORM-SECURITY|provenance_security|alternative_branch
2607.10265|AGENT-MEMORY|agent_state|direct_evolution
2607.10291|AGENT-WORKFLOW|safety_contract|principle_reuse
2607.10350|AGENT-WORKFLOW|agent_state|direct_evolution
2607.10362|MULTIMODAL-WORLD-MODELS|evaluation_contract|corrective_evidence
2607.10389|INFER-SCHEDULING|serving_runtime|direct_evolution
2607.10463|AGENT-RAG|retrieval_system|direct_evolution
2607.10491|AGENT-RAG|evidence_state|direct_evolution
2607.10582|INFER-KV-CACHE|serving_runtime|direct_evolution
2607.10661|INFER-SPECULATIVE-DECODING|serving_runtime|alternative_branch
2607.10709|PLATFORM-SECURITY|privacy_control|release_security_override
2607.10712|PLATFORM-SECURITY|provenance_security|direct_evolution
2607.10750|TRAIN-DATA|safety_contract|corrective_evidence
2607.10798|AGENT-RAG|evidence_state|direct_evolution
2607.10855|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.10959|TRAIN-PRETRAINING|training_mechanism|alternative_branch
2607.10987|INFER-DYNAMO|serving_runtime|direct_evolution
2607.11070|TRAIN-GRPO|training_mechanism|direct_evolution
2607.11079|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|principle_reuse
2607.11086|AGENT-MCP|provenance_security|corrective_evidence
2607.11131|INFER-SPECULATIVE-DECODING|serving_runtime|direct_evolution
2607.11136|INFER-GPU-MEMORY|serving_runtime|direct_evolution
2607.11138|AGENT-WORKFLOW|agent_state|alternative_branch
2607.11149|PLATFORM-COST|evaluation_contract|direct_evolution
2607.11172|TRAIN-GRPO|training_mechanism|direct_evolution
2607.11183|MODEL-FFN|model_mechanism|alternative_branch
2607.11226|AGENT-MULTI-AGENT|safety_contract|alternative_branch
2607.11250|AGENT-MULTI-AGENT|agent_state|direct_evolution
2607.11262|INFER-TENSORRT-LLM|evaluation_contract|principle_reuse
2607.11317|INFER-DECODE|evaluation_contract|corrective_evidence
2607.11346|AGENT-WORKFLOW|agent_state|direct_evolution
2607.11368|INFER-TENSORRT-LLM|evaluation_contract|corrective_evidence
2607.11388|AGENT-WORKFLOW|agent_state|direct_evolution
2607.11399|AGENT-PLATFORM|resource_control|direct_evolution
2607.11414|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|alternative_branch
2607.11423|AGENT-PLATFORM|evaluation_contract|principle_reuse
2607.11433|AGENT-WORKFLOW|evidence_state|direct_evolution
2607.11436|MULTIMODAL-REPRESENTATION|model_mechanism|direct_evolution
2607.11444|MODEL-MOE|training_mechanism|alternative_branch
2607.11475|PLATFORM-SECURITY|safety_contract|alternative_branch
2607.11487|AGENT-MEMORY|agent_state|direct_evolution
2607.11498|MULTIMODAL-EMBODIED-VLA|model_mechanism|direct_evolution
2607.11505|TRAIN-GRPO|training_mechanism|alternative_branch
2607.11506|TRAIN-GRPO|training_mechanism|direct_evolution
2607.11579|PLATFORM-GPU-SCHEDULER|resource_control|principle_reuse
2607.11586|MODEL-MOE|serving_runtime|direct_evolution
2607.11598|AGENT-WORKFLOW|evaluation_contract|direct_evolution
2607.11611|AGENT-TOOL-CALLING|safety_contract|direct_evolution
2607.11614|MODEL-LONG-CONTEXT|model_mechanism|alternative_branch
2607.11643|MULTIMODAL-WORLD-MODELS|model_mechanism|direct_evolution
2607.11673|MULTIMODAL-WORLD-MODELS|model_mechanism|alternative_branch
2607.11698|PLATFORM-SECURITY|safety_contract|direct_evolution
2607.11738|MULTIMODAL-REPRESENTATION|model_mechanism|direct_evolution
2607.11746|INFER-TENSORRT-LLM|evaluation_contract|principle_reuse
2607.11751|PLATFORM-SECURITY|safety_contract|corrective_evidence
2607.11796|MODEL-LONG-CONTEXT|model_mechanism|corrective_evidence
2607.11818|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.11836|MULTIMODAL-WORLD-MODELS|model_mechanism|direct_evolution
2607.11862|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.11871|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.11883|WORLDVIEW-WHY-MODELS-LEARN|model_mechanism|explanatory_analogy
2607.11886|MULTIMODAL-GENERATIVE-PARADIGMS|training_mechanism|alternative_branch
"""

SCORE = {
    "evaluation_contract": (3, 3, 3),
    "evidence_state": (3, 3, 3),
    "serving_runtime": (3, 3, 3),
    "agent_state": (3, 3, 3),
    "provenance_security": (3, 3, 3),
    "safety_contract": (3, 3, 3),
    "training_mechanism": (3, 2, 3),
    "training_correctness": (3, 3, 3),
    "model_mechanism": (2, 2, 3),
    "resource_control": (3, 3, 3),
    "slo_control": (3, 3, 3),
    "retrieval_system": (3, 3, 3),
    "privacy_control": (3, 3, 3),
}

# Candidate membership and review depth are different decisions.  These
# families change a durable contract but their evidence is narrower (single
# benchmark, limited model family, conceptual formalization, or local method),
# so they remain candidates while taking the 5-6 Standard route.
STANDARD_SCORE = {
    aid: (2, 2, 2)
    for aid in """
2607.09691 2607.09692 2607.09711 2607.09770 2607.09776 2607.09803
2607.09804 2607.09822 2607.09889 2607.09996 2607.10079 2607.10096
2607.10103 2607.10152 2607.10226 2607.10240 2607.10252 2607.10291
2607.10350 2607.10463 2607.10855 2607.11079 2607.11183 2607.11226
2607.11262 2607.11414 2607.11423 2607.11436 2607.11444 2607.11487
2607.11498 2607.11614 2607.11673 2607.11738 2607.11796 2607.11818
2607.11836 2607.11862 2607.11871 2607.11883 2607.11886
""".split()
}
STANDARD_SCORE["2607.11746"] = (2, 2, 1)

RATIONALE = {
    "evaluation_contract": "它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。",
    "evidence_state": "它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。",
    "serving_runtime": "它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。",
    "agent_state": "它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。",
    "provenance_security": "它改变 artifact/evidence provenance 或攻击面的信任边界，可能影响发布与审计合同。",
    "safety_contract": "它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。",
    "training_mechanism": "它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。",
    "training_correctness": "它揭示训练数值路径会静默改变有效更新，直接影响 correctness contract。",
    "model_mechanism": "它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。",
    "resource_control": "它改变资源分配、迁移、定价或路由的控制权与约束。",
    "slo_control": "它把 learned policy 与强制 SLO guard 分层，改变可保证与只能统计观测的责任边界。",
    "retrieval_system": "它改变检索证据、候选或模型迁移的长期数据与控制流。",
    "privacy_control": "它改变推理期隐私处理的状态与 utility/security trade-off。",
}


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+", text)
    return (parts[0] if parts else text)[:420]


def parse_routes() -> dict[str, dict[str, str]]:
    result = {}
    for line in ROUTES.strip().splitlines():
        aid, node, route, relation = line.split("|")
        result[aid] = {"stable_node_id": node, "semantic_route": route, "evolution_relation": relation}
    return result


def main() -> None:
    routes = parse_routes()
    with gzip.open(RAW, "rt", encoding="utf-8") as handle:
        raw = json.load(handle)
    with gzip.open(PRIOR, "rt", encoding="utf-8") as handle:
        prior = json.load(handle)
    by_prior = {item["arxiv_id"]: item for item in prior["items"]}
    by_raw = {item["arxiv_id"]: item for item in raw["identities"]}
    missing = sorted(set(routes) - set(by_raw))
    if missing:
        raise SystemExit(f"route IDs absent from raw inventory: {missing}")

    items = []
    counts = Counter()
    for identity in raw["identities"]:
        aid = identity["arxiv_id"]
        family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        if aid in routes:
            meta = routes[aid]
            dd, sr, du = STANDARD_SCORE.get(aid, SCORE[meta["semantic_route"]])
            total = dd + sr + du
            item = {
                "arxiv_id": aid,
                "source_family_id": family,
                "title": identity["title"],
                "title_abstract_sha256": identity["title_abstract_sha256"],
                "decision": "retain_in_candidate_denominator",
                "decision_kind": "durable_ai_system_delta_or_forced_review",
                "reason": f"摘要首要问题为“{first_sentence(identity['abstract'])}”；{RATIONALE[meta['semantic_route']]}",
                **meta,
                "score_v2_provisional": {"design_delta": dd, "system_reach": sr, "durability": du, "total": total},
                "review_route": "deep" if total >= 7 else "standard",
                "review_override": "release_security_contract" if "override" in meta["evolution_relation"] else "none",
                "next_gate": "exact_v1_source_review",
            }
            counts["retained"] += 1
            counts[f"route_{item['review_route']}"] += 1
        else:
            old = by_prior[aid]
            item = {
                "arxiv_id": aid,
                "source_family_id": family,
                "title": identity["title"],
                "title_abstract_sha256": identity["title_abstract_sha256"],
                "decision": "pre_denominator_closure",
                "decision_kind": old["semantic_decision_kind"],
                "reason": old["semantic_screen_reason"],
                "audit_note": "fresh-context false-negative audit found no durable state/data/control/evaluation/release delta beyond the quoted title+abstract claim",
                "next_gate": "closed_unless_revision_or_new_artifact_changes_boundary",
            }
            counts["closed"] += 1
            counts[item["decision_kind"]] += 1
        items.append(item)

    digest = "\n".join(
        f"{x['arxiv_id']}|{x['title_abstract_sha256']}|{x['decision']}|{x['decision_kind']}|{x['reason']}"
        for x in items
    )
    denominator_id = "daily-2026-07-14-0900-v2.1-sha256:" + hashlib.sha256(digest.encode()).hexdigest()
    decisions = {
        "schema": "fresh-context-semantic-decisions-v2.1",
        "report_date": "2026-07-14",
        "executed_at": RUN_AT,
        "auditor": "author-side-denominator-audit:daily-jun-jul-20260903",
        "scope": "all 965 canonical raw identities; full title and abstract; explicit false-positive and false-negative pass",
        "status": "complete_author_side_independent_audit_pending",
        "raw_identity_count": len(items),
        "retained_candidate_count": counts["retained"],
        "pre_denominator_closure_count": counts["closed"],
        "retain_rate": round(counts["retained"] / len(items), 6),
        "decision_counts": dict(sorted(counts.items())),
        "denominator_id": denominator_id,
        "boundary": "Topic or ROADMAP adjacency is insufficient; retention requires a durable AI-System mechanism, state/data/control ownership, evaluation/release contract, or correction of an existing claim.",
        "items": items,
    }
    with gzip.open(DECISIONS, "wt", encoding="utf-8") as handle:
        json.dump(decisions, handle, ensure_ascii=False, indent=2)
        handle.write("\n")

    denominator = {
        "schema": "candidate-denominator-v2.1",
        "report_date": "2026-07-14",
        "denominator_id": denominator_id,
        "frozen_at": RUN_AT,
        "status": "author_semantic_complete_exact_v1_review_pending",
        "raw_identity_count": len(items),
        "retained_candidate_count": counts["retained"],
        "pre_denominator_closure_count": counts["closed"],
        "retained_source_families": [x["source_family_id"] for x in items if x["decision"] == "retain_in_candidate_denominator"],
        "closure_ledger": "fresh-context-semantic-decisions-v2.1.json.gz",
        "independent_audit_status": "pending_root_or_fresh_reviewer",
        "books_status": "frozen_pending_root_sequential_comparison",
    }
    DENOMINATOR.write_text(json.dumps(denominator, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: decisions[k] for k in ("raw_identity_count", "retained_candidate_count", "pre_denominator_closure_count", "retain_rate", "denominator_id")}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
