#!/usr/bin/env python3
"""Freeze author-side denominators for March 1--8 after full abstract replay."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

# Explicit semantic-screen results.  Every retained item plausibly changes a
# durable AI-system mechanism, state/data/control owner, evaluation contract,
# or existing Books conclusion; keyword relevance alone is insufficient.
# value = (Stable Node ID, proposed Books disposition, V2 score triple)
C = {
4: {
"2603.00356":("INFER-SCHEDULING","Integrate",(3,3,3)),
"2603.01661":("INFER-SCHEDULING","No Change — Existing Coverage",(2,3,2)),
"2603.01548":("AGENT-TOOL-CALLING","No Change — Existing Coverage",(3,2,2)),
"2603.01058":("INFER-GPU-MEMORY","No Change — Existing Coverage",(3,3,2)),
"2603.02075":("TRAIN-DATA","No Change — Existing Coverage",(3,3,2)),
"2603.00495":("PLATFORM-FOUNDATIONS","No Change — Existing Coverage",(3,3,3)),
"2603.00468":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(2,3,3)),
"2603.02188":("MODEL-MULTI-HEAD-ATTENTION","No Change — Existing Coverage",(3,2,3)),
"2603.00196":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,3)),
"2603.01581":("INFER-SPECULATIVE-DECODING","No Change — Existing Coverage",(3,2,2)),
"2603.01399":("INFER-SPECULATIVE-DECODING","No Change — Existing Coverage",(3,2,3)),
"2603.00825":("MULTIMODAL-WORLD-MODELS","No Change — Existing Coverage",(3,2,3)),
"2603.00811":("TRAIN-DATA","No Change — Existing Coverage",(3,3,3)),
"2603.00349":("AGENT-MULTI-AGENT","No Change — Existing Coverage",(3,2,3)),
"2603.00188":("INFER-KV-CACHE","No Change — Existing Coverage",(3,2,2)),
"2603.01966":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(2,2,3)),
"2603.01960":("INFER-TENSORRT-LLM","No Change — Existing Coverage",(3,2,3)),
"2603.01209":("AGENT-PLATFORM","Integrate",(3,3,3)),
"2603.00724":("TRAIN-RLHF","No Change — Existing Coverage",(3,2,2)),
"2603.00381":("AGENT-MULTI-AGENT","No Change — Existing Coverage",(3,2,3)),
"2603.02176":("AGENT-PLATFORM","Integrate",(3,3,3)),
"2603.01499":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,2)),
},
5: {
"2603.02240":("AGENT-MEMORY","Integrate",(3,3,3)),
"2603.02277":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,3)),
"2603.02731":("TRAIN-DISTRIBUTED-TRAINING","No Change — Existing Coverage",(3,3,3)),
"2603.02376":("TRAIN-DISTRIBUTED-TRAINING","Integrate",(3,3,3)),
"2603.02737":("INFER-TENSORRT-LLM","No Change — Existing Coverage",(3,3,3)),
"2603.02631":("INFER-SPECULATIVE-DECODING","No Change — Existing Coverage",(3,3,3)),
"2603.02633":("MODEL-MOE","No Change — Existing Coverage",(3,2,3)),
"2603.02697":("MULTIMODAL-WORLD-MODELS","No Change — Existing Coverage",(3,3,3)),
"2603.03205":("AGENT-TOOL-CALLING","No Change — Existing Coverage",(3,2,3)),
"2603.02637":("INFER-TENSORRT-LLM","No Change — Existing Coverage",(3,2,3)),
"2603.02601":("PLATFORM-EVALUATION-SYSTEM","Integrate",(3,3,3)),
"2603.02271":("MULTIMODAL-EMBODIED-VLA","No Change — Existing Coverage",(2,3,3)),
"2603.02885":("TRAIN-LORA","Integrate",(3,3,3)),
"2603.02597":("MODEL-TOKENIZER","No Change — Existing Coverage",(3,2,2)),
"2603.02214":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,3)),
"2603.02599":("INFER-PD-DISAGGREGATION","No Change — Existing Coverage",(3,3,3)),
"2603.03251":("INFER-SPECULATIVE-DECODING","No Change — Existing Coverage",(3,2,3)),
"2603.03116":("PLATFORM-EVALUATION-SYSTEM","Integrate",(3,3,3)),
"2603.02482":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(2,3,3)),
},
6: {
"2603.03380":("MULTIMODAL-EMBODIED-VLA","No Change — Existing Coverage",(3,3,2)),
"2603.03378":("AGENT-REFLECTION","No Change — Existing Coverage",(3,2,3)),
"2603.03772":("PLATFORM-FOUNDATIONS","No Change — Existing Coverage",(3,3,3)),
"2603.03731":("TRAIN-DISTRIBUTED-TRAINING","No Change — Existing Coverage",(3,3,3)),
"2603.03491":("PLATFORM-PRODUCTION","Integrate",(3,3,3)),
"2603.03784":("MULTIMODAL-WORLD-MODELS","Integrate",(3,3,3)),
"2603.04028":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(3,3,3)),
"2603.03290":("AGENT-MEMORY","Integrate",(3,3,3)),
"2603.03394":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,3)),
"2603.03379":("AGENT-MEMORY","No Change — Existing Coverage",(3,2,3)),
"2603.03403":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,3)),
"2603.04308":("INFER-TENSORRT-LLM","No Change — Existing Coverage",(3,2,3)),
"2603.03800":("TRAIN-RLHF","No Change — Existing Coverage",(3,2,3)),
"2603.03482":("MULTIMODAL-WORLD-MODELS","No Change — Existing Coverage",(3,3,3)),
"2603.03333":("INFER-SPECULATIVE-DECODING","No Change — Existing Coverage",(3,2,2)),
"2603.03589":("AGENT-PLATFORM","Integrate",(3,3,3)),
"2603.04257":("AGENT-MEMORY","No Change — Existing Coverage",(3,3,3)),
"2603.04379":("MULTIMODAL-GENERATIVE-PARADIGMS","No Change — Existing Coverage",(3,3,2)),
"2603.04241":("AGENT-WORKFLOW","Integrate",(3,3,3)),
},
7: {
"2603.04428":("AGENT-MEMORY","Integrate",(3,3,3)),
"2603.05454":("MULTIMODAL-GENERATIVE-PARADIGMS","No Change — Existing Coverage",(3,3,3)),
"2603.04797":("INFER-GPU-MEMORY","No Change — Existing Coverage",(3,3,3)),
"2603.04424":("TRAIN-DISTRIBUTED-TRAINING","Integrate",(3,3,3)),
"2603.04981":("TRAIN-DATA","No Change — Existing Coverage",(3,3,3)),
"2603.04833":("AGENT-MULTI-AGENT","No Change — Existing Coverage",(3,3,2)),
"2603.04427":("INFER-KV-CACHE","No Change — Existing Coverage",(3,2,3)),
"2603.05185":("MULTIMODAL-EMBODIED-VLA","No Change — Existing Coverage",(3,3,3)),
"2603.05147":("MULTIMODAL-EMBODIED-VLA","No Change — Existing Coverage",(3,2,3)),
"2603.04448":("AGENT-PLATFORM","Integrate",(3,3,3)),
"2603.04411":("INFER-KV-CACHE","No Change — Existing Coverage",(3,2,3)),
"2603.04460":("INFER-PREFILL","No Change — Existing Coverage",(3,3,3)),
"2603.04402":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(3,3,3)),
"2603.04902":("PLATFORM-SECURITY","No Change — Existing Coverage",(3,3,3)),
"2603.04459":("PLATFORM-EVALUATION-SYSTEM","Integrate",(3,3,3)),
"2603.04444":("INFER-SCHEDULING","Integrate",(3,3,3)),
"2603.05451":("INFER-TENSORRT-LLM","No Change — Existing Coverage",(3,3,3)),
"2603.05210":("INFER-SPECULATIVE-DECODING","No Change — Existing Coverage",(3,2,3)),
"2603.05438":("MULTIMODAL-WORLD-MODELS","No Change — Existing Coverage",(3,3,3)),
"2603.04910":("MULTIMODAL-EMBODIED-VLA","No Change — Existing Coverage",(3,3,3)),
"2603.04621":("INFER-TENSORRT-LLM","No Change — Existing Coverage",(3,3,2)),
"2603.04417":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(3,2,3)),
"2603.04443":("AGENT-MEMORY","Integrate",(3,3,3)),
"2603.05399":("PLATFORM-EVALUATION-SYSTEM","No Change — Existing Coverage",(3,2,3)),
},
}

DOMAIN = re.compile(r"\b(?:medical|clinical|patient|molecular|protein|finance|wireless|traffic|education|agriculture|remote sensing|satellite|healthcare)\b", re.I)
EVAL = re.compile(r"\b(?:benchmark|dataset|survey|taxonomy)\b", re.I)
LOCAL = re.compile(r"\b(?:classification|segmentation|detection|forecast|recommendation|recognition|estimation|image restoration)\b", re.I)


def closure(row: dict) -> tuple[str, str]:
    text = row["title"] + " " + row["abstract"]
    if DOMAIN.search(text):
        return "domain_application_without_system_delta", "领域数据、标签或工作流增量没有迁移为通用 AI System 的长期状态、控制或发布责任。"
    if EVAL.search(row["title"]):
        return "local_benchmark_without_contract_delta", "局部 benchmark/dataset 没有改变 evaluator identity、可复算证据对象或 release gate。"
    if LOCAL.search(text):
        return "localized_model_quality_delta", "单任务质量改进没有重新分配训练、推理或平台的 state/data/control owner。"
    return "no_durable_ai_system_delta", "title+abstract 未显示足以改变长期 AI System 机制、owner contract、evaluation contract 或既有 Books 判断的设计增量。"


def main() -> None:
    for day in range(1, 9):
        packet = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
        inventory = json.loads((packet / "inventory.json").read_text())
        selected = C.get(day, {})
        rows = []
        for item in inventory["identities"]:
            row = dict(item)
            cfg = selected.get(item["arxiv_id"])
            if cfg:
                node, disposition, score = cfg
                row.update({
                    "screening_decision": "retained",
                    "screening_status": "candidate_denominator",
                    "reason_code": "durable_system_delta_requires_fulltext",
                    "screening_reason": f"`{item['title']}` may alter a durable mechanism or state/control/evaluation contract; exact-v1 decides the claim boundary.",
                    "stable_node_id": node,
                    "proposed_books_disposition": disposition,
                    "score_v2": {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)},
                })
            else:
                code, reason = closure(item)
                row.update({
                    "screening_decision": "closure",
                    "screening_status": "pre_denominator_closure",
                    "reason_code": code,
                    "screening_reason": f"`{item['title']}`: {reason}",
                })
            rows.append(row)
        found = {x["arxiv_id"] for x in rows if x["screening_decision"] == "retained"}
        missing = set(selected) - found
        if missing:
            raise RuntimeError(f"03-{day:02d} retained IDs missing from corrected inventory: {sorted(missing)}")
        report_date = f"2026-03-{day:02d}"
        digest = hashlib.sha256(
            (report_date + "\n" + "\n".join(sorted(found))).encode()
        ).hexdigest()
        payload = {
            "schema": "screening-ledger-v2.1-independent-author",
            "report_date": report_date,
            "registered_identities": len(rows),
            "full_semantic_screened": len(rows),
            "candidate_denominator": len(found),
            "pre_denominator_closed": len(rows) - len(found),
            "denominator_id": f"sha256:{digest}",
            "fresh_context_false_positive_false_negative_audit": "pending_independent_reviewer",
            "identities": rows,
        }
        (packet / "screening-ledger-author.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({"date": payload["report_date"], "raw": len(rows), "retained": len(found), "closures": len(rows)-len(found)}))


if __name__ == "__main__":
    main()
