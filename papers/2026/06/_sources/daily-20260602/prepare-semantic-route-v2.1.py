#!/usr/bin/env python3
"""Freeze the explicit 2026-06-02 semantic route after a second-pass audit.

The old 51 candidates are preserved as evidence hypotheses, then merged with
false negatives recovered by reading every canonical title and abstract.  This
file records decisions only; exact-v1 evidence review remains a later gate.
"""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent


# arXiv ID -> (Stable Node ID, semantic route, evolution relation)
RECOVERED_FALSE_NEGATIVES = {
    "2606.00021": ("INFER-SPECULATIVE-DECODING", "serving_runtime", "direct_evolution"),
    "2606.00024": ("INFER-KV-CACHE", "serving_runtime", "direct_evolution"),
    "2606.00079": ("MODEL-MOE", "serving_runtime", "direct_evolution"),
    "2606.00093": ("PLATFORM-EVALUATION-SYSTEM", "evaluation_contract", "corrective_evidence"),
    "2606.00135": ("AGENT-TOOL-CALLING", "training_mechanism", "direct_evolution"),
    "2606.00144": ("INFER-SPECULATIVE-DECODING", "serving_runtime", "direct_evolution"),
    "2606.00152": ("PLATFORM-SECURITY", "safety_contract", "direct_evolution"),
    "2606.00189": ("AGENT-PLATFORM", "agent_state", "principle_reuse"),
    "2606.00206": ("INFER-QUANTIZATION", "evaluation_contract", "corrective_evidence"),
    "2606.00279": ("PLATFORM-EVALUATION-SYSTEM", "evaluation_contract", "direct_evolution"),
    "2606.00365": ("INFER-QUANTIZATION", "serving_runtime", "direct_evolution"),
    "2606.00380": ("PLATFORM-EVALUATION-SYSTEM", "evaluation_contract", "direct_evolution"),
    "2606.00395": ("TRAIN-GRPO", "training_mechanism", "direct_evolution"),
    "2606.00408": ("AGENT-CONTEXT", "agent_state", "corrective_evidence"),
    "2606.00432": ("AGENT-RAG", "evidence_state", "alternative_branch"),
    "2606.00439": ("MULTIMODAL-WORLD-MODELS", "model_mechanism", "direct_evolution"),
    "2606.00457": ("PLATFORM-RESOURCE-SCHEDULING", "resource_control", "direct_evolution"),
    "2606.00486": ("INFER-MEMORY", "serving_runtime", "principle_reuse"),
    "2606.00497": ("PLATFORM-SECURITY", "evaluation_contract", "corrective_evidence"),
    "2606.00515": ("MULTIMODAL-EMBODIED-VLA", "safety_contract", "direct_evolution"),
    "2606.00516": ("INFER-CONTINUOUS-BATCHING", "serving_runtime", "alternative_branch"),
    "2606.00539": ("TRAIN-PRETRAINING", "training_mechanism", "direct_evolution"),
    "2606.00611": ("PLATFORM-SECURITY", "safety_contract", "direct_evolution"),
    "2606.00619": ("AGENT-MEMORY", "agent_state", "direct_evolution"),
    "2606.00651": ("MODEL-MOE", "safety_contract", "corrective_evidence"),
    "2606.00655": ("AGENT-MULTI-AGENT", "evaluation_contract", "corrective_evidence"),
    "2606.00664": ("MULTIMODAL-WORLD-MODELS", "serving_runtime", "direct_evolution"),
    "2606.00717": ("AGENT-MULTI-AGENT", "evaluation_contract", "principle_reuse"),
    "2606.00724": ("INFER-KV-CACHE", "serving_runtime", "alternative_branch"),
    "2606.00735": ("INFER-MOE", "resource_control", "direct_evolution"),
    "2606.00755": ("TRAIN-REINFORCEMENT-LEARNING", "training_mechanism", "alternative_branch"),
    "2606.00773": ("MULTIMODAL-EMBODIED-VLA", "evaluation_contract", "corrective_evidence"),
    "2606.00793": ("MULTIMODAL-WORLD-MODELS", "evaluation_contract", "corrective_evidence"),
    "2606.00804": ("AGENT-MULTI-AGENT", "resource_control", "alternative_branch"),
    "2606.00866": ("INFER-KV-CACHE", "resource_control", "direct_evolution"),
    "2606.00888": ("TRAIN-DISTRIBUTED-TRAINING", "training_mechanism", "direct_evolution"),
    "2606.00925": ("PLATFORM-SECURITY", "evaluation_contract", "direct_evolution"),
    "2606.01027": ("MULTIMODAL-WORLD-MODELS", "model_mechanism", "direct_evolution"),
    "2606.01036": ("TRAIN-REWARD-MODEL", "evaluation_contract", "corrective_evidence"),
    "2606.01041": ("AGENT-MEMORY", "agent_state", "alternative_branch"),
    "2606.01095": ("MULTIMODAL-EMBODIED-VLA", "evaluation_contract", "corrective_evidence"),
    "2606.01117": ("TRAIN-DISTRIBUTED-TRAINING", "training_mechanism", "direct_evolution"),
    "2606.01120": ("AGENT-RAG", "evaluation_contract", "corrective_evidence"),
    "2606.01279": ("TRAIN-DATA", "training_mechanism", "direct_evolution"),
    "2606.01281": ("TRAIN-GRPO", "training_mechanism", "alternative_branch"),
    "2606.01336": ("MODEL-LONG-CONTEXT", "serving_runtime", "direct_evolution"),
    "2606.01351": ("AGENT-MULTI-AGENT", "agent_state", "corrective_evidence"),
    "2606.01483": ("INFER-TENSORRT-LLM", "serving_runtime", "direct_evolution"),
    "2606.01528": ("AGENT-MEMORY", "training_mechanism", "direct_evolution"),
    "2606.01561": ("TRAIN-DPO", "training_mechanism", "alternative_branch"),
    "2606.01563": ("INFER-KV-CACHE", "serving_runtime", "direct_evolution"),
    "2606.01613": ("AGENT-RAG", "evidence_state", "direct_evolution"),
    "2606.01626": ("MULTIMODAL-WORLD-MODELS", "model_mechanism", "alternative_branch"),
    "2606.01635": ("TRAIN-REWARD-MODEL", "training_mechanism", "direct_evolution"),
    "2606.01693": ("INFER-TENSORRT-LLM", "serving_runtime", "principle_reuse"),
    "2606.01711": ("MULTIMODAL-REPRESENTATION", "serving_runtime", "direct_evolution"),
    "2606.01756": ("MULTIMODAL-REPRESENTATION", "serving_runtime", "alternative_branch"),
    "2606.01766": ("PLATFORM-COST", "resource_control", "alternative_branch"),
    "2606.01790": ("INFER-KV-CACHE", "serving_runtime", "direct_evolution"),
    "2606.01813": ("INFER-SPECULATIVE-DECODING", "serving_runtime", "direct_evolution"),
    "2606.01934": ("TRAIN-REINFORCEMENT-LEARNING", "training_mechanism", "direct_evolution"),
    "2606.01969": ("PLATFORM-EVALUATION-SYSTEM", "evaluation_contract", "corrective_evidence"),
    "2606.01991": ("PLATFORM-SECURITY", "safety_contract", "direct_evolution"),
    "2606.02011": ("INFER-QUANTIZATION", "evaluation_contract", "corrective_evidence"),
    "2606.02031": ("TRAIN-GRPO", "training_mechanism", "direct_evolution"),
    "2606.02109": ("PLATFORM-EVALUATION-SYSTEM", "evaluation_contract", "direct_evolution"),
    "2606.02132": ("AGENT-TOOL-CALLING", "safety_contract", "corrective_evidence"),
    "2606.02161": ("MULTIMODAL-REPRESENTATION", "serving_runtime", "direct_evolution"),
    "2606.02245": ("AGENT-RAG", "resource_control", "direct_evolution"),
    "2606.02277": ("MULTIMODAL-EMBODIED-VLA", "evaluation_contract", "corrective_evidence"),
    "2606.02282": ("AGENT-MULTI-AGENT", "evaluation_contract", "direct_evolution"),
    "2606.02288": ("INFER-QUANTIZATION", "model_mechanism", "direct_evolution"),
    "2606.02307": ("MULTIMODAL-EMBODIED-VLA", "evaluation_contract", "direct_evolution"),
    "2606.02355": ("TRAIN-REINFORCEMENT-LEARNING", "training_mechanism", "direct_evolution"),
    "2606.02357": ("AGENT-TOOL-CALLING", "evaluation_contract", "corrective_evidence"),
    "2606.02358": ("INFER-TENSORRT-LLM", "serving_runtime", "direct_evolution"),
    "2606.02359": ("AGENT-MULTI-AGENT", "resource_control", "direct_evolution"),
    "2606.02372": ("MULTIMODAL-WORLD-MODELS", "training_mechanism", "direct_evolution"),
    "2606.02388": ("MULTIMODAL-WORLD-MODELS", "training_mechanism", "direct_evolution"),
    "2606.02470": ("AGENT-PLATFORM", "evaluation_contract", "direct_evolution"),
    "2606.02486": ("MULTIMODAL-WORLD-MODELS", "model_mechanism", "direct_evolution"),
    "2606.02494": ("PLATFORM-MONITORING", "evidence_state", "direct_evolution"),
    "2606.02544": ("INFER-SPECULATIVE-DECODING", "serving_runtime", "alternative_branch"),
    "2606.02559": ("INFER-QUANTIZATION", "serving_runtime", "alternative_branch"),
    "2606.02577": ("MULTIMODAL-WORLD-MODELS", "training_mechanism", "direct_evolution"),
}


# Standard review is sufficient for surveys, diagnostic benchmarks, and
# narrowly bounded alternatives that do not yet change a book conclusion.
STANDARD = {
    "2606.00093", "2606.00152", "2606.00189", "2606.00206", "2606.00279",
    "2606.00380", "2606.00408", "2606.00497", "2606.00515", "2606.00655",
    "2606.00717", "2606.00773", "2606.00793", "2606.00925", "2606.01036",
    "2606.01095", "2606.01120", "2606.01483", "2606.01613", "2606.01626",
    "2606.01693", "2606.01766", "2606.01969", "2606.02109", "2606.02245",
    "2606.02277", "2606.02307", "2606.02357", "2606.02358", "2606.02470",
}


def route_for_old(node: str) -> tuple[str, str]:
    if node.startswith("INFER-"):
        return "serving_runtime", "direct_evolution"
    if node.startswith("TRAIN-"):
        return "training_mechanism", "direct_evolution"
    if node.startswith("AGENT-"):
        return "agent_state", "direct_evolution"
    if node.startswith("MULTIMODAL-"):
        return "model_mechanism", "direct_evolution"
    if node == "PLATFORM-SECURITY":
        return "safety_contract", "corrective_evidence"
    if node in {"PLATFORM-EVALUATION-SYSTEM", "PLATFORM-MONITORING"}:
        return "evaluation_contract", "corrective_evidence"
    return "resource_control", "direct_evolution"


def main() -> None:
    queue = json.loads((HERE / "canonical-owner-candidate-queue-v1.json").read_text())
    routes: dict[str, list[str]] = {}
    for item in queue["items"]:
        aid = item["primary_identifier"].removeprefix("arXiv:").removesuffix("v1")
        node = item["candidate_cells"][18]
        kind, relation = route_for_old(node)
        routes[aid] = [node, kind, relation]
        if item["candidate_cells"][15] == "standard_complete":
            STANDARD.add(aid)
    for aid, route in RECOVERED_FALSE_NEGATIVES.items():
        routes[aid] = list(route)
    payload = {
        "run_at": "2026-09-04T06:30:00+08:00",
        "routes": dict(sorted(routes.items())),
        "standard": sorted(STANDARD),
        "audit_scope": "all 1,449 canonical title+abstract identities; old candidates rechecked plus explicit false-negative recovery",
    }
    (HERE / "semantic-routes-v2.1.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"retained": len(routes), "standard": len(STANDARD)}, indent=2))


if __name__ == "__main__":
    main()
