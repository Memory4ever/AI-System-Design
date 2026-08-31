#!/usr/bin/env python3
"""Build the non-author 2026-05-12 reconciliation without mutating author artifacts."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent

REOPEN = {
    "2605.09992": ("INFER-SPECULATIVE-DECODING", (3, 3, 3), "drafter hidden-state scale and attention drift change speculative-decoding robustness contract"),
    "2605.10057": ("AGENT-MULTI-AGENT", (3, 3, 3), "typed execution status makes failure recovery an explicit routing transition"),
    "2605.10094": ("MULTIMODAL-EMBODIED-VLA", (3, 2, 3), "verified successful episodes become bounded deployment-time action priors for a frozen VLA"),
    "2605.10199": ("MULTIMODAL-REPRESENTATION", (3, 2, 3), "full-duplex user-stream placement changes interruption latency and generation coherence"),
    "2605.10347": ("MULTIMODAL-WORLD-MODELS", (3, 2, 3), "mobile world-model evidence separates training-time modality priors from post-hoc verification"),
    "2605.10366": ("AGENT-WORKFLOW", (3, 3, 2), "verifier-centric credit assignment changes instruction and tool trajectory control"),
    "2605.10426": ("MULTIMODAL-EMBODIED-VLA", (3, 2, 3), "world tokens become explicit planning conditions in the VLA action loop"),
    "2605.10779": ("PLATFORM-SECURITY", (3, 3, 3), "semantic and physical checks plus OS rollback redefine safe computer-action commit"),
    "2605.10819": ("MULTIMODAL-EMBODIED-VLA", (3, 2, 3), "algebraically consistent latent-transition supervision changes action-state learning"),
    "2605.10832": ("AGENT-WORKFLOW", (3, 3, 2), "addressable image-bank state and on-policy data evolution change tool workflow memory"),
    "2605.10850": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "self-verifier agreement bias invalidates agreement-as-confidence without calibration"),
    "2605.10875": ("INFER-TENSORRT-LLM", (3, 3, 3), "per-token policy jointly controls sparsity, pruning and precision at runtime"),
    "2605.10912": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "native-runtime long-horizon tasks expose tool side effects as evaluation evidence"),
    "2605.10923": ("AGENT-PLATFORM", (3, 2, 3), "skills become lifecycle state with retain, retire and expand transitions"),
    "2605.10933": ("MODEL-MOE", (3, 2, 3), "edge placement constraints change expert routing and capacity design"),
    "2605.11047": ("PLATFORM-SECURITY", (3, 3, 2), "open-world execution context becomes part of the agent security evaluation contract"),
    "2605.11053": ("PLATFORM-SECURITY", (3, 3, 2), "tool-call traffic is treated as an observable security surface"),
    "2605.11086": ("PLATFORM-SECURITY", (3, 3, 3), "containerized exploit tasks with mitigation toggles create a controllable security benchmark contract"),
    "2605.11186": ("INFER-SPECULATIVE-DECODING", (3, 3, 3), "memory-limited cascaded tree speculation changes proposal-state allocation"),
    "2605.11212": ("AGENT-CONTEXT", (3, 2, 3), "visual-history selection makes computer-use context a bounded state policy"),
    "2605.11234": ("AGENT-TOOL-CALLING", (3, 3, 3), "ontology-grounded types move tool compatibility into the call contract"),
    "2605.11277": ("INFER-TENSORRT-LLM", (3, 3, 3), "runtime expert distribution controls GPU/PIM scheduling"),
    "2605.11328": ("TRAIN-RLHF", (2, 2, 3), "adapter disagreement supplies an epistemic exploration signal"),
    "2605.11330": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "long-context RAG and label noise become explicit hallucination-evaluation conditions"),
    "2605.11334": ("PLATFORM-EVALUATION-SYSTEM", (3, 3, 3), "verifier-trace structure is calibrated into selective risk rather than raw confidence"),
    "2605.11367": ("MULTIMODAL-WORLD-MODELS", (3, 3, 3), "persistent revisable 3D belief state separates world state from generated frames"),
    "2605.13880": ("AGENT-MEMORY", (3, 2, 2), "pre-task proposer-validator practice writes validated experience into memory"),
    "2605.18792": ("AGENT-RAG", (3, 2, 3), "parametric and contextual knowledge beliefs govern retrieval and abstention"),
    "2605.18796": ("INFER-SCHEDULING", (3, 3, 3), "calibrated correctness and cost jointly select a model cascade"),
    "2605.18803": ("MULTIMODAL-WORLD-MODELS", (3, 2, 3), "adversarial curriculum and prioritized failures change world-model training state"),
}

DROP = {
    "2605.10312": "FusionRCG maps quantum-chemistry recurrences to GPU memory; it is a domain-specific HPC kernel result, not a reusable AI-System state/data/control or evidence contract.",
}

OWNER_FIXES = {
    "2605.10380": ("INFER-SPECULATIVE-DECODING", "on-device prefix caching and LLM-free draft generation are inference proposal-state mechanisms, not Agent Platform ownership"),
    "2605.11317": ("INFER-REQUEST-LIFECYCLE", "early-turn local surrogate routing changes request admission/escalation, not continuous batching"),
}

RECOVERED = {
    "2605.10246": {
        "status": "deep_complete",
        "access": "accessible",
        "primary": "https://arxiv.org/pdf/2605.10246v1",
        "method": "§3.1 Design Principles; §3.2 Agent Framework; §3.3 Scenario Construction; §3.4 Evaluation Protocol",
        "evaluation": "§4.1 Models; §4.2 Main Results; §5.1 Behavioral Patterns; §5.2 Task-Completion Pressure ablation; §5.3 Structural Drivers",
        "limitations": "No independent Limitations section; claims are bounded to 33 scenarios, 11 traps, 7 models and 231 minimal-ReAct runs.",
        "artifact": "https://github.com/liuxingtong/Sci-Integrity-Bench",
    }
}

BLOCKED = {
    "2605.10133": "Official abs/version identity is accessible, but exact-v1 HTML, PDF and TeX body could not be recovered; abstract alone cannot support Method/Evaluation/Limitations review."
}


def main() -> None:
    author = json.loads((ROOT / "screening-ledger-final.json").read_text())
    rows = author["identities"]
    by_id = {r["arxiv_id"]: r for r in rows}
    findings = []

    for aid, reason in DROP.items():
        row = by_id[aid]
        row["screening_status"] = "pre_denominator_closure"
        row["screening_reason"] = reason
        row["review_status"] = "identity_date_closed"
        row["access_status"] = "accessible_metadata"
        row["integration_disposition"] = "Rejected — Below Candidate Denominator"
        findings.append({"kind": "false_positive", "arxiv_id": aid, "resolution": reason})

    for aid, (owner, score, reason) in REOPEN.items():
        row = by_id[aid]
        row["screening_status"] = "retained"
        row["screening_reason"] = reason
        row["review_status"] = "review_pending"
        row["access_status"] = "accessible_exact_v1"
        row["integration_disposition"] = "Books Decision Pending"
        row["stable_node_id"] = owner
        row["score_v2"] = {"design_delta": score[0], "system_reach": score[1], "durability": score[2], "total": sum(score)}
        findings.append({"kind": "false_negative", "arxiv_id": aid, "owner": owner, "reason": reason})

    for aid, (owner, reason) in OWNER_FIXES.items():
        row = by_id[aid]
        previous = row.get("stable_node_id")
        row["stable_node_id"] = owner
        row["independent_owner_note"] = reason
        findings.append({"kind": "owner_mismatch", "arxiv_id": aid, "from": previous, "to": owner, "reason": reason})

    for aid, evidence in RECOVERED.items():
        row = by_id[aid]
        row["review_status"] = evidence["status"]
        row["access_status"] = evidence["access"]
        row["integration_disposition"] = "Books Decision Pending"
        row["independent_exact_v1"] = evidence
        findings.append({"kind": "access_recovered", "arxiv_id": aid, "evidence": evidence})

    for aid, reason in BLOCKED.items():
        row = by_id[aid]
        row["review_status"] = "blocked"
        row["access_status"] = "blocked"
        row["integration_disposition"] = "Blocked / Unverified"
        row["independent_blocker"] = reason

    retained = [r for r in rows if r["screening_status"] == "retained"]
    closures = [r for r in rows if r["screening_status"] != "retained"]
    for r in retained:
        aid = r["arxiv_id"]
        if aid not in REOPEN and aid not in RECOVERED and aid not in BLOCKED:
            r["independent_evidence_status"] = "challenge_pending"
            r["independent_evidence_note"] = "Author locator was generic or abstract-derived; independent exact-v1 Method/Evaluation/Limitations/Artifact verification remains required."

    out = dict(author)
    out["schema"] = "daily-screening-ledger-v2.1-independent-reconciled"
    out["candidate_denominator"] = len(retained)
    out["pre_denominator_closures"] = len(closures)
    out["identities"] = rows
    (ROOT / "screening-ledger-independent-reconciled.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")

    audit = {
        "schema": "fresh-context-semantic-audit-v2.1",
        "report_date": "2026-05-12",
        "reviewer_relation": "non-author",
        "scope": {"title_abstract_replay": "870/870", "author_denominator_challenged": "47/47", "author_queue_challenged": "22/22"},
        "counts": {
            "raw_snapshot_records": author["raw_snapshot_records"],
            "registered": 870,
            "screened": 870,
            "retained_final": len(retained),
            "closures_final": len(closures),
            "false_negatives": len(REOPEN),
            "false_positives": len(DROP),
            "owner_mismatches": len(OWNER_FIXES),
            "exact_v1_recovered": len(RECOVERED),
            "blocked": len(BLOCKED),
            "independent_exact_v1_pending": sum(1 for r in retained if r.get("independent_evidence_status") == "challenge_pending") + len(REOPEN),
        },
        "findings": findings,
        "blocked": [{"arxiv_id": k, "reason": v} for k, v in BLOCKED.items()],
        "gate": {
            "coverage": "Passed after reconciliation: all 870 identities replayed and denominator corrected to 76.",
            "evidence": "Open: 2605.10133 is blocked; author generic/abstract-derived locators and 30 reopened false negatives require independent exact-v1 completion.",
            "books": "Open: current owner+adjacent comparison is not trustworthy until Evidence closes; no shared Books write occurred.",
            "completion": "In Progress",
        },
        "cross_model_status": "Skipped — this non-interactive worker is the independent reviewer; no second independent context was available inside the lane.",
    }
    (ROOT / "independent-semantic-audit.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n")

    queue = {
        "schema": "books-writeback-queue-v1-independent-challenge",
        "report_date": "2026-05-12",
        "status": "not_ready_evidence_open",
        "items": [],
        "withheld": [
            {
                "arxiv_id": r["arxiv_id"],
                "source_family_id": r["source_family_id"],
                "stable_node_id": r.get("stable_node_id"),
                "reason": "Evidence Gate remains open; current Books owner+adjacent comparison must be repeated after exact-v1 completion.",
            }
            for r in retained
        ],
    }
    (ROOT / "books-writeback-queue-independent-reconciled.json").write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
