#!/usr/bin/env python3
"""Build an auditable *proposal* for March lane-D denominator screening.

This helper never freezes a Candidate Denominator.  It assigns every title and
abstract a recall-oriented feature receipt so a fresh reviewer can challenge
both proposed retains and proposed pre-denominator closures.  Final admission,
Score V2, source review, and Books decisions remain human/agent judgments.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SYSTEM_TERMS = {
    "runtime_state": [
        "kv cache", "cache", "serving", "inference engine", "inference runtime",
        "prefill", "decode", "speculative decoding", "continuous batching",
        "gpu", "npu", "accelerator", "kernel", "scheduler", "scheduling",
        "distributed", "parallel", "collective", "allreduce", "checkpoint",
        "offload", "memory management", "resource allocation", "kubernetes",
    ],
    "training_control": [
        "training system", "distributed training", "post-training", "rlhf",
        "preference optimization", "policy optimization", "grpo", "optimizer",
        "gradient", "data mixture", "training data", "data attribution",
        "mixture of experts", "moe", "fine-tuning", "finetuning", "lora",
    ],
    "agent_state": [
        "agent", "agentic", "tool use", "tool-use", "tool calling", "workflow",
        "mcp", "a2a", "memory", "rag", "retrieval-augmented", "planning",
        "execution provenance", "authorization", "prompt injection",
    ],
    "evidence_contract": [
        "evaluation", "benchmark", "reliability", "calibration", "uncertainty",
        "hallucination", "audit", "security", "privacy leakage", "red-team",
        "red team", "release gate", "conformance", "verification",
    ],
    "model_architecture": [
        "long context", "long-context", "attention", "token compression",
        "quantization", "model compression", "diffusion language", "world model",
        "vision-language-action", "vla", "multimodal generation", "routing",
    ],
}

DELTA_TERMS = [
    "architecture", "system", "framework", "runtime", "protocol", "control plane",
    "state", "ownership", "pipeline", "orchestration", "scheduling", "serving",
    "deployment", "resource", "fault", "failure", "security", "privacy",
    "evaluation", "benchmark", "verification", "provenance", "authorization",
    "distributed", "cache", "memory", "latency", "throughput", "scalab",
]

APPLICATION_TERMS = [
    "medical image", "clinical", "radiology", "agricultur", "financial forecast",
    "traffic", "autonomous driving", "remote sensing", "molecule", "protein",
    "drug", "weather", "solar", "satellite", "surgical", "diagnosis", "disease",
    "brain", "battery", "wireless", "uav", "underwater", "recommendation",
]

SURVEY_TERMS = ["survey", "systematic review", "taxonomy", "position paper"]

# Root-lane denominator decisions after title+abstract review.  The list is
# intentionally narrower than the challenge queue: a ROADMAP-shaped topic is
# not enough; each retained family names a durable mechanism, ownership shift,
# or evaluation/security contract that requires primary-source review.
FINAL_RETAIN_BY_DATE = {
    "2026-03-25": {
        "2603.22691", "2603.22744", "2603.22751", "2603.22774", "2603.22812",
        "2603.22823", "2603.22853", "2603.22855", "2603.22858", "2603.22867",
        "2603.22868", "2603.22869", "2603.22910", "2603.23049", "2603.23149",
        "2603.23231", "2603.23343", "2603.23448", "2603.23500", "2603.23575",
        "2603.23610", "2603.23749", "2603.23791", "2603.23806", "2603.28795",
    },
    "2026-03-26": {
        "2603.23840", "2603.23848", "2603.23871", "2603.23909", "2603.24060",
        "2603.24402", "2603.24582", "2603.24709", "2603.24747", "2603.24755",
    },
    "2026-03-27": {
        "2603.24943", "2603.24963", "2603.24984", "2603.25001", "2603.25011",
        "2603.25056", "2603.25097", "2603.25158", "2603.25164", "2603.25284",
        "2603.25342", "2603.25661", "2603.25685", "2603.25716", "2603.25766",
        "2603.25780", "2603.25928", "2603.25973", "2603.26823",
    },
    "2026-03-28": {
        "2603.26034", "2603.26074", "2603.26221", "2603.26270", "2603.26299",
        "2603.26337", "2603.26360", "2603.26483", "2603.26576", "2603.26595",
        "2603.26648", "2603.26666", "2603.26993",
    },
    "2026-03-29": {
        "2603.27116", "2603.27138", "2603.27226", "2603.28815",
    },
    "2026-03-30": {
        "2603.27467", "2603.27469", "2603.27515", "2603.27517", "2603.27624",
        "2603.27752", "2603.27819", "2603.27914",
    },
    "2026-03-31": {
        "2603.28013", "2603.28101", "2603.28204", "2603.28239", "2603.28342",
        "2603.28407", "2603.28430", "2603.28551", "2603.28565", "2603.28718",
        "2603.28845", "2603.28887", "2603.28986", "2603.28998", "2603.29010",
        "2603.29020", "2603.29023", "2603.29078", "2603.29090",
    },
}

DIRECT_TITLE_TERMS = [
    "kv cache", "llm serving", "inference engine", "inference runtime",
    "multi-gpu", "gpu inference", "gpu scheduling", "resource scheduling",
    "distributed inference", "distributed training", "pipeline parallel",
    "tensor parallel", "speculative decoding", "continuous batching",
    "checkpoint", "mixture of experts", "allreduce", "kernel",
    "agent protocol", "agent security", "agent audit", "agent benchmark",
    "agentic trace", "execution provenance", "tool protocol", "tool orchestration",
    "prompt injection", "authorization", "privacy leakage", "long-horizon agent",
    "hallucination detection", "rag poisoning", "world model", "world-model",
    "vision-language-action", "vla", "post-training", "preference optimization",
    "policy optimization", "rlhf", "grpo", "long context", "long-context",
    "model compression", "quantization", "runtime-adaptive", "fpga inference",
]


def matches(text: str, terms: list[str]) -> list[str]:
    lower = text.lower()
    return sorted({term for term in terms if term in lower})


def classify(row: dict) -> dict:
    text = f"{row['title']}\n{row['abstract']}"
    title = row["title"].lower()
    feature_groups = {
        group: matches(text, terms) for group, terms in SYSTEM_TERMS.items()
    }
    feature_groups = {key: value for key, value in feature_groups.items() if value}
    delta = matches(text, DELTA_TERMS)
    applications = matches(text, APPLICATION_TERMS)
    surveys = matches(text, SURVEY_TERMS)
    group_count = len(feature_groups)
    signal_count = sum(len(value) for value in feature_groups.values())

    # Deliberately recall-oriented.  This is a challenge queue, not admission.
    direct_title = matches(title, DIRECT_TITLE_TERMS)
    agent_evidence_title = (
        ("agent" in title or "agentic" in title)
        and any(term in title for term in (
            "audit", "security", "privacy", "benchmark", "evaluation", "protocol",
            "provenance", "authorization", "trace", "reliability", "conformance",
        ))
    )
    system_arch_title = (
        any(term in title for term in ("system", "architecture", "runtime", "serving", "scheduler"))
        and group_count >= 2
        and len(delta) >= 3
    )
    challenge = bool(direct_title or agent_evidence_title or system_arch_title)
    if surveys and group_count < 3:
        challenge = False

    if challenge:
        decision = "challenge_for_candidate_admission"
        reason = (
            "crosses durable system facets and names an architectural/evaluation "
            "contract; inspect the complete abstract before admission"
        )
    elif applications and group_count <= 1:
        decision = "proposed_pre_denominator_closure"
        reason = (
            "application-bounded method with no explicit cross-component state, "
            "control, runtime, or evaluation-contract delta"
        )
    elif group_count == 0:
        decision = "proposed_pre_denominator_closure"
        reason = (
            "no durable AI-System mechanism, ownership, runtime, or evaluation "
            "contract is identifiable from title and abstract"
        )
    else:
        decision = "proposed_pre_denominator_closure"
        reason = (
            "AI-related local method or component improvement; abstract does not "
            "yet establish a long-term system-design delta"
        )

    return {
        **row,
        "proposal": decision,
        "proposal_reason": reason,
        "feature_groups": feature_groups,
        "delta_terms": delta,
        "application_terms": applications,
        "survey_terms": surveys,
        "direct_title_terms": direct_title,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument(
        "--proposal-only",
        action="store_true",
        help="emit the fresh-context challenge queue without applying a lane-specific frozen retain set",
    )
    args = parser.parse_args()
    source = json.loads(args.ledger.read_text())
    rows = [classify(row) for row in source["identities"]]
    result = {
        "schema": "march-denominator-screening-proposal-v1",
        "report_date": source["report_date"],
        "contract_boundary": (
            "proposal only; every row requires fresh semantic FP/FN review before freeze"
        ),
        "raw_identities": len(rows),
        "challenge_count": sum(row["proposal"].startswith("challenge") for row in rows),
        "closure_count": sum(row["proposal"].startswith("proposed_pre") for row in rows),
        "rows": rows,
    }
    retained = None if args.proposal_only else FINAL_RETAIN_BY_DATE.get(source["report_date"])
    if retained is not None:
        found = {row["arxiv_id"] for row in rows}
        missing = sorted(retained - found)
        if missing:
            raise SystemExit(f"retained ids outside strict window: {missing}")
        for row in rows:
            row["final_screening_decision"] = (
                "retain_pending_primary_status_and_evidence_review"
                if row["arxiv_id"] in retained
                else "pre-denominator_closure"
            )
            if row["arxiv_id"] not in retained:
                row["final_closure_reason"] = row["proposal_reason"]
        result["retained_candidates"] = len(retained)
        result["pre_denominator_closures"] = len(rows) - len(retained)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({key: result[key] for key in ("report_date", "raw_identities", "challenge_count", "closure_count")}, ensure_ascii=False))


if __name__ == "__main__":
    main()
