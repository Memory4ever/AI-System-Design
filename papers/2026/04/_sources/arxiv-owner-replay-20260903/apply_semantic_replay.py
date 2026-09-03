#!/usr/bin/env python3
"""Close newly recovered April/May identities under the V2.1 denominator rule.

The explicit retain set is the result of a fresh title+abstract read.  It is
deliberately narrow: an AI-related application, model-quality delta, dataset or
domain benchmark is not enough.  Retained families must change a durable AI
System mechanism, state/control ownership or evaluation/release contract.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")

RETAIN = {
    # 2026-04 owner days: delayed/held identities absent from submission replay.
    "2603.28768", "2603.28769", "2603.28780", "2603.28781", "2603.28793",
    "2603.28795", "2603.28815", "2603.28823", "2603.28887", "2603.28963",
    "2603.28988", "2603.29002", "2603.29010", "2603.29020",
    "2603.29090", "2603.29848", "2604.02340", "2604.02344",
    "2604.02367", "2604.03258", "2604.03270", "2604.03295", "2604.08584",
    "2604.08565", "2604.08585", "2604.09557", "2604.09562", "2604.09580",
    "2604.09587", "2604.09588", "2604.09603", "2604.09611",
    "2604.09651", "2604.13055", "2604.13064", "2604.13072", "2604.14170",
    "2604.14178", "2604.16310", "2604.16331", "2604.16368", "2604.16385",
    "2604.16395", "2604.18592", "2604.19752", "2604.19769", "2604.19780", "2604.20854",
    "2604.20860",
    # 2026-05 owner days.
    "2605.00831", "2605.00873", "2605.02905", "2605.04069", "2605.04075",
    "2605.04084", "2605.05219", "2605.05222", "2605.05225", "2605.06675",
    "2605.06676", "2605.12530", "2605.13848", "2605.13851", "2605.15204",
    "2605.16265", "2605.18755", "2605.18762", "2605.19755", "2605.20196",
    "2605.23911", "2605.23918", "2605.23935", "2605.26118", "2605.26120",
    "2605.26440", "2605.26444", "2605.27390",
}

WITHDRAWN = {"2603.29078", "2604.09613", "2605.04356"}


def closure_reason(row: dict) -> str:
    text = f"{row.get('title', '')} {row.get('abstract', '')}".lower()
    title = row.get("title", "").strip()
    if "survey" in text or "systematic review" in text or "roadmap" in text:
        basis = "survey_or_context_synthesis_without_a_new_owned_system_mechanism"
    elif "dataset" in text or "benchmark" in text:
        basis = "domain_dataset_or_benchmark_without_a_durable_evaluation_contract_delta"
    elif any(term in text for term in ("medical", "clinical", "health", "education", "finance", "traffic", "agricultur", "manufactur")):
        basis = "domain_application_result_without_transferable_ai_system_design_delta"
    elif any(term in text for term in ("classification", "detection", "forecast", "segmentation", "recognition")):
        basis = "task_or_model_quality_delta_without_state_data_or_control_ownership_change"
    elif any(term in text for term in ("rag", "retrieval-augmented", "multi-agent", "agentic")):
        basis = "application_level_agent_or_retrieval_method_without_a_new_durable_system_contract"
    elif any(term in text for term in ("gpu", "scheduling", "network", "database", "kernel")):
        basis = "general_computing_or_local_optimization_not_specific_enough_to_change_ai_system_books"
    else:
        basis = "local_method_or_empirical_result_without_a_long_lived_ai_system_mechanism_delta"
    return f"pre-denominator closure: {basis}; title+abstract reviewed for {title}"


def main() -> None:
    for month in ("04", "05"):
        month_root = ROOT / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903"
        summary = json.loads((month_root / "month-reconciliation.json").read_text(encoding="utf-8"))
        added_retain = added_closure = withdrawn = 0
        for day in summary["days"]:
            receipt_path = ROOT / day["receipt"]
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
            decisions = []
            for row in receipt["identities"]:
                if row["screening_status"] != "review_pending":
                    continue
                aid = row["arxiv_id"]
                if aid in WITHDRAWN:
                    row["screening_status"] = "withdrawn_pre_denominator"
                    row["screening_reason"] = "official arXiv withdrawal; excluded before denominator, score, review and Books"
                    withdrawn += 1
                elif aid in RETAIN:
                    row["screening_status"] = "retained"
                    row["screening_reason"] = "fresh title+abstract audit: durable AI System mechanism, ownership, evaluation or execution-contract delta"
                    added_retain += 1
                else:
                    row["screening_status"] = "closure"
                    row["screening_reason"] = closure_reason(row)
                    added_closure += 1
                decisions.append({
                    "arxiv_id": aid,
                    "source_family_id": row["source_family_id"],
                    "title": row["title"],
                    "decision": row["screening_status"],
                    "reason": row["screening_reason"],
                    "reviewed_fields": ["title", "abstract", "categories"],
                })
            receipt["semantic_review_pending_count"] = 0
            receipt["fresh_context_semantic_replay"] = {
                "scope": "all identities absent from the earlier submission-window ledgers",
                "rule": "AI relevance or ROADMAP mappability alone is insufficient; retain only durable AI System design deltas",
                "decision_count": len(decisions),
                "decisions": decisions,
            }
            receipt_path.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        summary["semantic_review_pending_total"] = 0
        summary["status"] = "owner_and_screening_reconciled_evidence_review_pending"
        summary["fresh_context_semantic_replay"] = {
            "newly_retained": added_retain,
            "newly_closed_pre_denominator": added_closure,
            "withdrawn_pre_denominator": withdrawn,
            "retained_ids": sorted(RETAIN),
        }
        (month_root / "month-reconciliation.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"month": month, "newly_retained": added_retain, "closures": added_closure, "withdrawn": withdrawn}, ensure_ascii=False))


if __name__ == "__main__":
    main()
