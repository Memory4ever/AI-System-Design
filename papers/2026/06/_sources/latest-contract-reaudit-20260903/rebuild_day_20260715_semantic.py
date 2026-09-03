#!/usr/bin/env python3
"""Freeze the 2026-07-15 V2.1 denominator after full title+abstract audit."""

from __future__ import annotations

import gzip
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/07/_sources/daily-20260715"
REPORT_DATE = "2026-07-15"
RUN_AT = "2026-09-04T04:00:00+08:00"

# arXiv ID | stable node | semantic route | evolution relation
ROUTES = """
2607.11897|MODEL-ATTENTION|model_mechanism|alternative_branch
2607.11942|INFER-KV-CACHE|evaluation_contract|corrective_evidence
2607.11944|AGENT-PLANNING|evaluation_contract|corrective_evidence
2607.11945|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|principle_reuse
2607.11953|TRAIN-REWARD-MODEL|evaluation_contract|corrective_evidence
2607.11969|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.11976|INFER-TENSORRT-LLM|serving_runtime|direct_evolution
2607.12056|AGENT-TOOL-CALLING|agent_state|principle_reuse
2607.12068|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.12085|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.12104|PLATFORM-TRACE|evidence_state|alternative_branch
2607.12121|INFER-TENSORRT-LLM|serving_runtime|direct_evolution
2607.12188|PLATFORM-COST|resource_control|direct_evolution
2607.12200|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.12211|PLATFORM-GPU-SCHEDULER|resource_control|alternative_branch
2607.12227|AGENT-PLATFORM|evaluation_contract|corrective_evidence
2607.12231|MULTIMODAL-WORLD-MODELS|evidence_state|alternative_branch
2607.12273|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.12278|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.12287|MULTIMODAL-EMBODIED-VLA|serving_runtime|direct_evolution
2607.12356|MULTIMODAL-EMBODIED-VLA|model_mechanism|direct_evolution
2607.12385|AGENT-MEMORY|evaluation_contract|direct_evolution
2607.12395|TRAIN-REINFORCEMENT-LEARNING|training_mechanism|principle_reuse
2607.12406|PLATFORM-SECURITY|safety_contract|direct_evolution
2607.12463|TRAIN-PRETRAINING|training_mechanism|alternative_branch
2607.12505|INFER-TENSORRT-LLM|serving_runtime|direct_evolution
2607.12550|INFER-KV-CACHE|serving_runtime|direct_evolution
2607.12571|MULTIMODAL-EMBODIED-VLA|safety_contract|direct_evolution
2607.12592|MULTIMODAL-WORLD-MODELS|model_mechanism|alternative_branch
2607.12614|INFER-TENSORRT-LLM|serving_runtime|structural_candidate
2607.12625|AGENT-MEMORY|agent_state|direct_evolution
2607.12650|AGENT-WORKFLOW|evidence_state|direct_evolution
2607.12659|MULTIMODAL-EMBODIED-VLA|serving_runtime|direct_evolution
2607.12696|INFER-SPECULATIVE-DECODING|serving_runtime|direct_evolution
2607.12747|PLATFORM-TRACE|evidence_state|direct_evolution
2607.12767|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.12790|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|direct_evolution
2607.12831|AGENT-RAG|evidence_state|alternative_branch
2607.12835|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.12839|INFER-TENSORRT-LLM|serving_runtime|direct_evolution
2607.12875|INFER-TENSORRT-LLM|resource_control|direct_evolution
2607.12885|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.12893|AGENT-MEMORY|evaluation_contract|direct_evolution
2607.12894|MULTIMODAL-EMBODIED-VLA|model_mechanism|principle_reuse
2607.12911|AGENT-RAG|evaluation_contract|corrective_evidence
2607.12931|MULTIMODAL-EMBODIED-VLA|training_mechanism|direct_evolution
2607.12962|AGENT-REFLECTION|evaluation_contract|corrective_evidence
2607.12963|PLATFORM-EVALUATION-SYSTEM|evaluation_contract|corrective_evidence
2607.12986|AGENT-PLANNING|safety_contract|corrective_evidence
2607.12992|MULTIMODAL-EMBODIED-VLA|model_mechanism|direct_evolution
2607.13013|MULTIMODAL-GENERATIVE-PARADIGMS|model_mechanism|alternative_branch
2607.13017|MULTIMODAL-WORLD-MODELS|model_mechanism|direct_evolution
2607.13027|AGENT-PLATFORM|serving_runtime|direct_evolution
2607.13028|MULTIMODAL-WORLD-MODELS|training_mechanism|alternative_branch
2607.13034|AGENT-PLANNING|resource_control|principle_reuse
"""

STANDARD = set("""
2607.11897 2607.11944 2607.11945 2607.11953 2607.11969
2607.12056 2607.12068 2607.12085 2607.12104 2607.12200 2607.12211
2607.12231 2607.12273 2607.12278 2607.12356 2607.12385 2607.12395
2607.12406 2607.12463 2607.12592 2607.12614 2607.12625 2607.12767
2607.12790 2607.12831 2607.12835 2607.12885 2607.12893 2607.12894
2607.12911 2607.12962 2607.12963 2607.12986 2607.12992 2607.13013
2607.13017 2607.13028 2607.13034
""".split())

RATIONALE = {
    "model_mechanism": "它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。",
    "evaluation_contract": "它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。",
    "serving_runtime": "它改变推理期状态放置、数据移动、执行控制或实时 SLO。",
    "agent_state": "它把 context、memory、能力或进度变成持久且可验证的 agent state。",
    "training_mechanism": "它改变训练信号、capacity 或 update ownership，而非只报告任务精度。",
    "safety_contract": "它改变执行安全的 trust boundary、guard 或 failure detection。",
    "evidence_state": "它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。",
    "resource_control": "它改变资源计量、分配、路由或迁移的控制权与约束。",
}


def first_sentence(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return re.split(r"(?<=[.!?])\s+", text)[0][:420]


def main() -> None:
    raw_path = PACKET / "canonical-raw-identity-inventory-v2.1.json.gz"
    prior_path = PACKET / "canonical-semantic-screening-checkpoint-v2.1.json.gz"
    with gzip.open(raw_path, "rt", encoding="utf-8") as f: raw = json.load(f)
    with gzip.open(prior_path, "rt", encoding="utf-8") as f: prior = json.load(f)
    route = {}
    for line in ROUTES.strip().splitlines():
        aid, node, kind, relation = line.split("|")
        route[aid] = (node, kind, relation)
    by_prior = {x["arxiv_id"]: x for x in prior["items"]}
    if set(route) - {x["arxiv_id"] for x in raw["identities"]}:
        raise RuntimeError("route contains identity outside raw inventory")
    items, counts = [], Counter()
    for identity in raw["identities"]:
        aid = identity["arxiv_id"]
        family = f"SF-2026-ARXIV-{aid.replace('.', '-')}"
        if aid in route:
            node, kind, relation = route[aid]
            score = (2, 2, 2) if aid in STANDARD else (3, 3, 3)
            item = {"arxiv_id": aid, "source_family_id": family, "title": identity["title"], "title_abstract_sha256": identity["title_abstract_sha256"], "decision": "retain_in_candidate_denominator", "decision_kind": "durable_ai_system_delta_or_forced_review", "reason": f"摘要首要问题为“{first_sentence(identity['abstract'])}”；{RATIONALE[kind]}", "stable_node_id": node, "semantic_route": kind, "evolution_relation": relation, "score_v2_provisional": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)}, "review_route": "standard" if aid in STANDARD else "deep", "review_override": "none", "next_gate": "exact_v1_source_review"}
            counts["retained"] += 1; counts[f"route_{item['review_route']}"] += 1
        else:
            old = by_prior[aid]
            item = {"arxiv_id": aid, "source_family_id": family, "title": identity["title"], "title_abstract_sha256": identity["title_abstract_sha256"], "decision": "pre_denominator_closure", "decision_kind": old["semantic_decision_kind"], "reason": old["semantic_screen_reason"], "audit_note": "fresh-context false-negative audit found no durable state/data/control/evaluation/release delta beyond the quoted title+abstract claim", "next_gate": "closed_unless_revision_or_new_artifact_changes_boundary"}
            counts["closed"] += 1; counts[item["decision_kind"]] += 1
        items.append(item)
    digest = "\n".join(f"{x['arxiv_id']}|{x['title_abstract_sha256']}|{x['decision']}|{x['decision_kind']}|{x['reason']}" for x in items)
    did = f"daily-{REPORT_DATE}-0900-v2.1-sha256:" + hashlib.sha256(digest.encode()).hexdigest()
    payload = {"schema": "fresh-context-semantic-decisions-v2.1", "report_date": REPORT_DATE, "executed_at": RUN_AT, "auditor": "author-side-denominator-audit:daily-jun-jul-20260903", "scope": f"all {len(items)} canonical raw identities; full title and abstract; explicit false-positive and false-negative pass", "status": "complete_author_side_independent_audit_pending", "raw_identity_count": len(items), "retained_candidate_count": counts["retained"], "pre_denominator_closure_count": counts["closed"], "retain_rate": round(counts["retained"]/len(items), 6), "decision_counts": dict(sorted(counts.items())), "denominator_id": did, "boundary": "Topic or ROADMAP adjacency is insufficient; retention requires a durable AI-System mechanism, state/data/control ownership, evaluation/release contract, or correction of an existing claim.", "items": items}
    with gzip.open(PACKET / "fresh-context-semantic-decisions-v2.1.json.gz", "wt", encoding="utf-8") as f: json.dump(payload, f, ensure_ascii=False, indent=2); f.write("\n")
    denom = {"schema": "candidate-denominator-v2.1", "report_date": REPORT_DATE, "denominator_id": did, "frozen_at": RUN_AT, "status": "author_semantic_complete_exact_v1_review_pending", "raw_identity_count": len(items), "retained_candidate_count": counts["retained"], "pre_denominator_closure_count": counts["closed"], "retained_source_families": [x["source_family_id"] for x in items if x["decision"] == "retain_in_candidate_denominator"], "closure_ledger": "fresh-context-semantic-decisions-v2.1.json.gz", "independent_audit_status": "pending_root_or_fresh_reviewer", "books_status": "frozen_pending_root_sequential_comparison"}
    (PACKET / "candidate-denominator-v2.1.json").write_text(json.dumps(denom, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: payload[k] for k in ("raw_identity_count", "retained_candidate_count", "pre_denominator_closure_count", "retain_rate", "denominator_id")}, ensure_ascii=False, indent=2))


if __name__ == "__main__": main()
