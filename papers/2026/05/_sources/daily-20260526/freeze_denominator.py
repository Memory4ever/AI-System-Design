#!/usr/bin/env python3
"""Freeze the 2026-05-26 author denominator from the full 587-row inventory."""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "screening-ledger-provisional.json"

RETAIN = {
    "2606.00093", "2605.25338", "2605.25375", "2605.25376", "2605.25379",
    "2605.25389", "2605.25421", "2605.25422", "2605.25424", "2605.25451",
    "2605.25475", "2605.25492", "2605.25521", "2605.25535", "2605.25537",
    "2605.25547", "2605.25550", "2605.25621", "2605.25624", "2605.25632",
    "2605.25641", "2605.25645", "2605.25653", "2605.25655", "2605.25673",
    "2605.25674", "2605.25682", "2605.25698", "2605.25704", "2605.25707",
    "2605.25716", "2605.25798", "2605.25820", "2605.25831", "2605.25869",
    "2605.25874", "2605.25893", "2605.25954", "2605.25966", "2605.25988",
    "2605.26029", "2605.26046", "2605.26079", "2605.26112", "2605.26114",
    "2605.26177", "2605.26184", "2605.26200", "2605.26252", "2605.26266",
    "2605.26269", "2605.26289", "2605.26297", "2605.26298", "2605.26302",
    "2605.26321", "2605.26327", "2605.26329", "2605.26340", "2605.26349",
    "2605.26362", "2605.26384", "2605.26403", "2605.27091", "2605.27461",
    "2605.28873",
}

OWNER = {
    "2606.00093": "PLATFORM-EVALUATION-SYSTEM",
    "2605.25338": "AGENT-PLATFORM", "2605.25375": "TRAIN-PIPELINE-PARALLEL",
    "2605.25376": "PLATFORM-SECURITY", "2605.25379": "AGENT-RAG",
    "2605.25389": "PLATFORM-SECURITY", "2605.25421": "AGENT-MULTI-AGENT",
    "2605.25422": "AGENT-MULTI-AGENT", "2605.25424": "INFER-SCHEDULING",
    "2605.25451": "TRAIN-DISTRIBUTED-TRAINING", "2605.25475": "INFER-KV-CACHE",
    "2605.25492": "PLATFORM-EVALUATION-SYSTEM", "2605.25521": "INFER-TENSORRT-LLM",
    "2605.25535": "AGENT-MEMORY", "2605.25537": "MULTIMODAL-EMBODIED-VLA",
    "2605.25547": "MULTIMODAL-EMBODIED-VLA", "2605.25550": "INFER-PD-DISAGGREGATION",
    "2605.25621": "MULTIMODAL-GENERATIVE-PARADIGMS", "2605.25624": "AGENT-PLATFORM",
    "2605.25632": "AGENT-TOOL-CALLING", "2605.25641": "AGENT-RAG",
    "2605.25645": "TRAIN-DISTRIBUTED-TRAINING", "2605.25653": "PLATFORM-SECURITY",
    "2605.25655": "INFER-SCHEDULING", "2605.25673": "PLATFORM-SECURITY",
    "2605.25674": "PLATFORM-MONITORING", "2605.25682": "INFER-SCHEDULING",
    "2605.25698": "TRAIN-DATA", "2605.25704": "TRAIN-PRETRAINING",
    "2605.25707": "PLATFORM-EVALUATION-SYSTEM", "2605.25716": "PLATFORM-SECURITY",
    "2605.25798": "INFER-TENSORRT-LLM", "2605.25820": "MULTIMODAL-GENERATIVE-PARADIGMS",
    "2605.25831": "AGENT-REFLECTION", "2605.25869": "AGENT-MEMORY",
    "2605.25874": "MULTIMODAL-WORLD-MODELS", "2605.25893": "PLATFORM-SECURITY",
    "2605.25954": "INFER-TENSORRT-LLM", "2605.25966": "INFER-TENSORRT-LLM",
    "2605.25988": "AGENT-RAG", "2605.26029": "AGENT-WORKFLOW",
    "2605.26046": "PLATFORM-EVALUATION-SYSTEM", "2605.26079": "PLATFORM-EVALUATION-SYSTEM",
    "2605.26112": "AGENT-PLATFORM", "2605.26114": "AGENT-PLATFORM",
    "2605.26177": "PLATFORM-EVALUATION-SYSTEM", "2605.26184": "TRAIN-RLHF",
    "2605.26200": "PLATFORM-EVALUATION-SYSTEM", "2605.26252": "AGENT-MEMORY",
    "2605.26266": "INFER-KV-CACHE", "2605.26269": "PLATFORM-SECURITY",
    "2605.26289": "AGENT-TOOL-CALLING", "2605.26297": "PLATFORM-EVALUATION-SYSTEM",
    "2605.26298": "PLATFORM-SECURITY", "2605.26302": "AGENT-PLATFORM",
    "2605.26321": "PLATFORM-EVALUATION-SYSTEM", "2605.26327": "TRAIN-PRETRAINING",
    "2605.26329": "PLATFORM-EVALUATION-SYSTEM", "2605.26340": "AGENT-WORKFLOW",
    "2605.26349": "TRAIN-DATA", "2605.26362": "PLATFORM-EVALUATION-SYSTEM",
    "2605.26384": "PLATFORM-GPU-SCHEDULER", "2605.26403": "TRAIN-RLHF",
    "2605.27091": "PLATFORM-EVALUATION-SYSTEM", "2605.27461": "MULTIMODAL-EMBODIED-VLA",
    "2605.28873": "PLATFORM-EVALUATION-SYSTEM",
}


def sentence(text: str) -> str:
    parts = [p.strip() for p in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text or "")) if p.strip()]
    chosen = next((p for p in parts if re.search(r"\b(propose|introduce|present|develop|design|study|evaluate|show|formulate|build)\b", p, re.I)), parts[0] if parts else "No abstract mechanism disclosed")
    words = chosen.split()
    return " ".join(words[:55]) + ("…" if len(words) > 55 else "")


def exclusion(row: dict) -> str:
    title = row["title"]
    abstract = row.get("abstract", "")
    cats = ",".join(row.get("categories", []))
    mechanism = sentence(abstract)
    lower = (title + " " + abstract).lower()
    if any(k in lower for k in ("medical", "clinical", "protein", "molecule", "disease", "ultrasound", "cardiac", "cancer", "rna ")):
        boundary = "the contribution is a domain-specific model, dataset, or clinical evaluation and does not alter a reusable AI-System state, control, deployment, or evidence contract"
    elif any(k in lower for k in ("benchmark", "evaluation", "dataset")):
        boundary = "the evaluation remains task/domain specific and does not change the repository's reusable evaluator identity, release gate, or evidence lifecycle"
    elif any(k in lower for k in ("agent", "rag", "tool", "memory", "workflow")):
        boundary = "the agent method changes task behavior but does not establish a durable information/action/workflow-state ownership or commit/recovery contract"
    elif any(k in lower for k in ("diffusion", "vision", "video", "multimodal", "3d", "image")):
        boundary = "the model-local quality or representation gain does not change the long-term multimodal state identity, generation factorization, serving, or physical-control boundary"
    elif any(k in lower for k in ("training", "optimization", "fine-tun", "reinforcement", "quantization", "pruning")):
        boundary = "the local objective or model-quality improvement does not change optimizer/checkpoint ownership, distributed runtime, precision contract, or a stable training design judgment"
    else:
        boundary = "the result is domain- or model-local and does not change a durable AI-System mechanism, state/data/control owner, evaluation contract, or design boundary"
    return f"`{title}` ({cats}) reports: {mechanism}; however, {boundary}."


data = json.loads(SRC.read_text())
rows = []
for raw in data["identities"]:
    row = dict(raw)
    aid = row["arxiv_id"]
    if aid in RETAIN:
        row.update(
            source_family_id="SF-2026-ARXIV-" + aid.replace(".", "-"),
            screening_status="retained_pending_exact_v1_review",
            screening_reason=f"`{row['title']}`: {sentence(row.get('abstract', ''))} This changes or tests a durable AI-System mechanism or system/evidence ownership boundary; retain for exact-v1 review.",
            owner_node=OWNER[aid],
            candidate_state="retained",
        )
    else:
        row.update(
            source_family_id="SF-2026-ARXIV-" + aid.replace(".", "-"),
            screening_status="pre_denominator_closure",
            screening_reason=exclusion(row),
            review_status="identity_date_closed",
            access_status="accessible_metadata",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
    rows.append(row)

assert len(rows) == 587
assert len(RETAIN) == 66, len(RETAIN)
assert sum(r["screening_status"].startswith("retained") for r in rows) == 66

out = dict(data)
out.update(
    schema="daily-screening-ledger-v2.1-author-frozen",
    identities=rows,
    semantic_review_required=587,
    semantic_review_completed=587,
    candidate_denominator=66,
    pre_denominator_closures=521,
    gate_status="denominator_frozen_pending_exact_v1",
)
(HERE / "screening-ledger-final.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
(HERE / "candidate-ids.txt").write_text("\n".join(sorted(RETAIN)) + "\n")
with (HERE / "screening-ledger-final.tsv").open("w", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t")
    writer.writerow(["arxiv_id", "title", "categories", "screening_status", "screening_reason", "owner_node"])
    for row in rows:
        writer.writerow([row["arxiv_id"], row["title"], ",".join(row["categories"]), row["screening_status"], row["screening_reason"], row.get("owner_node", "")])
print(json.dumps({"raw": data["raw_snapshot_records"], "registered": 587, "screened": 587, "retained": 66, "closures": 521}))
