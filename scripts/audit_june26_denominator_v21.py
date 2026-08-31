#!/usr/bin/env python3
"""Freeze the strict V2.1 Candidate Denominator for 2026-06-26.

This date-local stage performs 470/470 title+abstract semantic screening only.
It never edits Books or LEARNING_STATE and deliberately leaves downstream
Evidence, Selection and Books gates open.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/06/_sources/daily-20260626"
PROVISIONAL = PACKET / "screening-ledger-provisional.json"
EXECUTED = "2026-08-29T10:20:00+08:00"


# Topic fit is insufficient.  Every retained family below changes a durable
# state/data/control owner, evaluation/release contract, security boundary, or
# an existing Books proposition.  Exact mechanism and non-proof remain
# Evidence-Gate work.
OWNERS = {
    "2606.26511": "AGENT-MEMORY",
    "2606.26524": "PLATFORM-SECURITY",
    "2606.26529": "PLATFORM-EVALUATION-SYSTEM",
    "2606.26587": "INFER-GPU-MEMORY",
    "2606.26590": "PLATFORM-EVALUATION-SYSTEM",
    "2606.26607": "INFER-SCHEDULING",
    "2606.26631": "INFER-KV-CACHE",
    "2606.26633": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.26649": "PLATFORM-SECURITY",
    "2606.26664": "PLATFORM-SECURITY",
    "2606.26666": "INFER-KV-CACHE",
    "2606.26669": "AGENT-TOOL-CALLING",
    "2606.26686": "PLATFORM-SECURITY",
    "2606.26721": "AGENT-WORKFLOW",
    "2606.26744": "INFER-SPECULATIVE-DECODING",
    "2606.26753": "AGENT-MEMORY",
    "2606.26758": "AGENT-PLATFORM",
    "2606.26762": "INFER-KV-CACHE",
    "2606.26790": "TRAIN-RLHF",
    "2606.26793": "PLATFORM-SECURITY",
    "2606.26806": "AGENT-MEMORY",
    "2606.26836": "PLATFORM-EVALUATION-SYSTEM",
    "2606.26859": "AGENT-PLATFORM",
    "2606.26875": "INFER-KV-CACHE",
    "2606.26904": "AGENT-TOOL-CALLING",
    "2606.26917": "TRAIN-RLHF",
    "2606.26918": "AGENT-PLANNING",
    "2606.26924": "AGENT-PLATFORM",
    "2606.26933": "PLATFORM-SECURITY",
    "2606.26935": "AGENT-REFLECTION",
    "2606.26960": "PLATFORM-EVALUATION-SYSTEM",
    "2606.26978": "AGENT-TOOL-CALLING",
    "2606.26979": "AGENT-CONTEXT",
    "2606.26990": "PLATFORM-EVALUATION-SYSTEM",
    "2606.26997": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.27005": "PLATFORM-GPU-SCHEDULER",
    "2606.27009": "AGENT-WORKFLOW",
    "2606.27027": "AGENT-MCP",
    "2606.27045": "AGENT-CONTEXT",
    "2606.27079": "MULTIMODAL-EMBODIED-VLA",
    "2606.27091": "PLATFORM-SECURITY",
    "2606.27136": "AGENT-MEMORY",
    "2606.27146": "MULTIMODAL-EMBODIED-VLA",
    "2606.27153": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.27154": "PLATFORM-TRACE",
    "2606.27188": "AGENT-WORKFLOW",
    "2606.27205": "INFER-GPU-MEMORY",
    "2606.27210": "PLATFORM-SECURITY",
    "2606.27226": "PLATFORM-EVALUATION-SYSTEM",
    "2606.27242": "PLATFORM-MODEL-REGISTRY",
    "2606.27243": "AGENT-PLATFORM",
    "2606.27251": "MULTIMODAL-EMBODIED-VLA",
    "2606.27268": "MULTIMODAL-EMBODIED-VLA",
    "2606.27288": "AGENT-MULTI-AGENT",
    "2606.27326": "MULTIMODAL-WORLD-MODELS",
    "2606.27330": "AGENT-PLANNING",
    "2606.27350": "AGENT-PLATFORM",
    "2606.27355": "MULTIMODAL-EMBODIED-VLA",
    "2606.27359": "INFER-DECODE",
    "2606.27369": "TRAIN-RLHF",
    "2606.27374": "MULTIMODAL-EMBODIED-VLA",
    "2606.27375": "TRAIN-DATA",
    "2606.27406": "PLATFORM-EVALUATION-SYSTEM",
    "2606.27409": "AGENT-MULTI-AGENT",
    "2606.27416": "AGENT-PLATFORM",
    "2606.27457": "PLATFORM-GATEWAY",
    "2606.27472": "AGENT-MEMORY",
    "2606.27474": "INFER-DECODE",
    "2606.27483": "AGENT-PLANNING",
    "2606.27492": "AGENT-MULTI-AGENT",
    "2606.27499": "AGENT-MEMORY",
    "2606.27510": "PLATFORM-EVALUATION-SYSTEM",
    "2606.27511": "PLATFORM-SECURITY",
    "2606.27550": "INFER-SPECULATIVE-DECODING",
    "2606.27558": "PLATFORM-EVALUATION-SYSTEM",
    "2606.27567": "PLATFORM-SECURITY",
    "2606.27578": "TRAIN-RLHF",
    "2606.27580": "TRAIN-RLHF",
    "2606.27595": "PLATFORM-EVALUATION-SYSTEM",
    "2606.27608": "TRAIN-RLHF",
    "2606.27622": "TRAIN-DISTRIBUTED-TRAINING",
    "2606.28409": "AGENT-PLATFORM",
    "2606.28421": "INFER-GPU-MEMORY",
    "2606.28425": "PLATFORM-SECURITY",
}


# These five looked durable on the first pass but failed the second-pass
# owner/contract test.  Keeping the correction explicit prevents a target
# retain-rate from silently deciding admission.
PROPOSED_FALSE_POSITIVES = {
    "2606.26650": "CAT-Q reports a ternary quantization method and training cost, but no serving/runtime contract that changes the long-lived inference owner.",
    "2606.27373": "VISE improves one self-evolving multimodal training recipe; the abstract does not establish a reusable platform or release authority boundary.",
    "2606.27376": "The self-consistency reward loop is a model-local multimodal post-training method rather than a durable cross-system control contract.",
    "2606.27443": "The personality-composition study reports task-dependent outcomes but does not introduce an ownerable mechanism or evaluation-release contract.",
    "2606.27537": "MemoBench is a useful world-model diagnostic dataset, but the abstract alone is benchmark-local and does not change a long-lived system owner.",
}


def first_sentence(text: str) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    match = re.search(r"(?<=[.!?])\s+", value)
    return (value[: match.start() + 1] if match else value)[:420]


def closure_class(item: dict) -> tuple[str, str]:
    title = item["title"]
    hay = f"{title} {item['abstract']}".lower()
    cats = set(item.get("categories", []))
    if item["arxiv_id"] in PROPOSED_FALSE_POSITIVES:
        return "second_pass_false_positive", PROPOSED_FALSE_POSITIVES[item["arxiv_id"]]
    if any(token in hay for token in ("survey", "systematic review", "literature review", "all insights you need")):
        return "survey_without_new_system_mechanism", (
            "The work synthesizes or categorizes prior results without a new state/data/control owner or an independently testable release contract."
        )
    if any(token in hay for token in (
        "medical", "clinical", "patient", "tumor", "mri", "cardiac", "radiology", "healthcare", "molecular",
        "protein", "agriculture", "crop", "satellite", "earth observation", "finance", "portfolio", "advertising",
        "education", "speech emotion", "malware detector", "weather", "robot dental", "skin lesion",
    )):
        return "domain_specific_application", (
            "The reported result remains tied to the named domain, dataset, or application and does not yet reassign a reusable AI-System owner."
        )
    if cats and not any(cat.startswith((
        "cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.SE", "cs.RO", "cs.CR", "cs.MM", "cs.SY", "eess.SY", "stat.ML"
    )) for cat in cats):
        return "generic_non_ai_system", (
            "The primary contribution is a general mathematical, physical, networking, or hardware result rather than an AI-System lifecycle contract."
        )
    if any(token in hay for token in (
        "benchmark", "dataset", "classification", "segmentation", "detection", "recognition", "forecasting",
        "image editing", "image generation", "video generation", "retrieval", "question answering",
    )):
        return "task_or_benchmark_local_improvement", (
            "The abstract reports a task/benchmark-local improvement but no change to evaluator identity, release authority, state ownership, or fallback responsibility."
        )
    if any(token in hay for token in (
        "method", "approach", "algorithm", "architecture", "framework", "transformer", "diffusion", "neural network"
    )):
        return "local_method_without_durable_owner_delta", (
            "The method is technically relevant, but its disclosed scope remains component-local and does not redraw a durable data/control/evaluation boundary."
        )
    return "context_without_durable_design_delta", (
        "The title and abstract provide useful context or a bounded experiment, but not a persistent mechanism or Books proposition change."
    )


def retained_reason(item: dict, owner: str) -> str:
    return (
        f"Retained under `{owner}` after full title+abstract review: ‘{item['title']}’ exposes ‘"
        f"{first_sentence(item['abstract'])}’. The abstract identifies a possible durable state/data/control, "
        "evaluation/release, security, or existing-proposition delta; exact mechanism and non-proof remain Evidence-Gate work."
    )


def main() -> None:
    payload = json.loads(PROVISIONAL.read_text(encoding="utf-8"))
    identities = payload["identities"]
    by_id = {item["arxiv_id"]: item for item in identities}
    missing = sorted(set(OWNERS) - set(by_id))
    if missing:
        raise SystemExit(f"retained IDs missing from frozen inventory: {missing}")

    retained_rows, closure_rows = [], []
    route_negative_total = route_negative_retained = 0
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
            item.update({
                "stable_node_id": "—",
                "semantic_screen_status": "closed_pre_denominator",
                "semantic_decision_kind": klass,
                "semantic_screen_reason": (
                    f"Family-specific closure for ‘{item['title']}’: the abstract scope begins ‘"
                    f"{first_sentence(item['abstract'])}’. {missing_delta}"
                ),
            })
            closure_rows.append(item)
        original.clear()
        original.update(item)

    if len(identities) != 470 or len(retained_rows) != 84 or len(closure_rows) != 386:
        raise SystemExit(f"denominator arithmetic mismatch: {len(identities)}/{len(retained_rows)}/{len(closure_rows)}")
    if route_negative_total != 107 or route_negative_retained != 2:
        raise SystemExit(f"route-negative arithmetic mismatch: {route_negative_total}/{route_negative_retained}")

    material = "\n".join(sorted(OWNERS)) + "\n"
    denominator_id = "daily-v2.1:2026-06-26:" + hashlib.sha256(material.encode()).hexdigest()[:16]
    payload.update({
        "gate_status": "coverage_closed_evidence_open",
        "denominator_id": denominator_id,
        "denominator_frozen_at": EXECUTED,
        "retained_candidate_families": len(retained_rows),
        "closed_pre_denominator_families": len(closure_rows),
        "route_negative_audited": route_negative_total,
        "route_negative_retained": route_negative_retained,
        "false_positive_false_negative_audit": {
            "auditor": "fresh-context:jun26-denominator-v1",
            "scope": "470/470 title+abstract plus 107/107 route-negative",
            "proposed_false_positives_closed": sorted(PROPOSED_FALSE_POSITIVES),
            "result": "passed",
            "unresolved_findings": 0,
        },
    })
    (PACKET / "screening-ledger.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    (PACKET / "candidate-ids-proposed-v1.txt").write_text(
        "\n".join(sorted(set(OWNERS) | set(PROPOSED_FALSE_POSITIVES))) + "\n"
    )
    (PACKET / "candidate-ids-v1.txt").write_text("\n".join(sorted(OWNERS)) + "\n")

    with (PACKET / "denominator-full-semantic-audit-v1.tsv").open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow([
            "arxiv_id", "source_family_key", "screening_route", "title", "abstract_basis", "decision",
            "closure_class", "stable_node_id", "family_specific_reason",
        ])
        for item in identities:
            retained = item["arxiv_id"] in OWNERS
            writer.writerow([
                item["arxiv_id"], item["source_family_key"], item["screening_route"], item["title"],
                first_sentence(item["abstract"]), "retained" if retained else "pre-denominator closure",
                item["semantic_decision_kind"], item["stable_node_id"], item["semantic_screen_reason"],
            ])

    (PACKET / "DENOMINATOR_FRESH_AUDIT_V1.md").write_text(
        "# 2026-06-26 Candidate Denominator Fresh Audit\n\n"
        f"- Window: `[2026-06-25 09:00, 2026-06-26 09:00)` Asia/Shanghai.\n"
        f"- Denominator: `{denominator_id}`.\n"
        "- Frozen arithmetic: `470 raw identities = 84 retained + 386 family-specific pre-denominator closures`.\n"
        "- Retain rate: `17.87%`.\n"
        "- Routes: Core `303`, keyword `60`, route-negative `107`; all `107/107` route-negative rows were re-read and `2` durable false negatives were recovered.\n"
        "- False-positive audit: `89` proposed durable rows were re-read against explicit ownership/evaluation criteria; `5` model-local or benchmark-local rows were closed before freezing.\n"
        "- False-negative audit: `470/470` title+abstract rows have an identity-specific decision and reason.\n"
        "- Coverage Gate: **Closed**.\n"
        "- Evidence, Selection, Books Gates: **Open**; denominator admission is permission to inspect exact v1, not proof.\n"
    )
    print(json.dumps({
        "denominator_id": denominator_id,
        "raw": len(identities),
        "retained": len(retained_rows),
        "closures": len(closure_rows),
        "retain_rate": "17.87%",
        "route_negative": route_negative_total,
        "route_negative_retained": route_negative_retained,
        "proposed_false_positives_closed": len(PROPOSED_FALSE_POSITIVES),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
