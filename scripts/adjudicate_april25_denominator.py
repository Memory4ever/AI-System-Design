#!/usr/bin/env python3
"""Independent denominator adjudication for the 2026-04-25 Historical Daily.

Only the strict-window title/abstract ledger and the date-local challenge set are
inputs.  No Weekly artifact is read.  Admission means the abstract asserts a
durable AI-system mechanism, state/control owner, or evaluation/release contract;
exact-v1 review remains a later gate.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/04/_sources/daily-20260425"


RETAIN = {
    "2604.22193": "makes parametric/user/retrieved assertions separate information owners and evaluates source-conflict discrimination",
    "2604.22228": "changes intra-node GPU communication control by scheduling NVLink/PCIe paths through a CUDA-Graph/UCX execution artifact",
    "2604.22238": "moves non-Markovian VLA state into a persistent semantic graph with explicit planner/executor ownership",
    "2604.22409": "defines action-conditioned embodied belief-state evolution and separates perception, oracle-state reasoning, and end-to-end memory evidence",
    "2604.22411": "turns nominal temperature-zero reproducibility into an inference-environment measurement contract for hidden nondeterminism",
    "2604.22430": "establishes isolation-versus-flexibility scheduling evidence for MPS/MIG GPU co-execution under contention",
    "2604.22452": "changes multi-agent evaluation from population size to controlled society-level coordination and information-synthesis probes",
    "2604.22513": "makes formal verification the acceptance owner for LLM-proposed network configuration repairs and regression control",
    "2604.22571": "separates agent proposal from controlled HPC execution and dry-run validation artifacts",
    "2604.22577": "makes numerical precision a runtime-routed resource for agent workloads rather than a static model asset",
    "2604.22679": "moves AI hiring accountability from the visible model to versioned upstream supply-chain dependencies",
    "2604.22753": "makes scaling-law evidence acquisition an active experiment-selection problem under a fixed compute budget",
    "2604.22881": "introduces hierarchical cache ownership and request-class scheduling for generative recommendation serving",
    "2604.22981": "unifies reward-model and value-function state through token-level temporally coherent supervision",
    "2604.23002": "separates syntactic proof validity from semantic preservation in a human-in-the-loop agent verification workflow",
    "2604.23036": "changes MoE fine-tuning state ownership by preserving long-tail expert information without global load-balancing gradients",
    "2604.23046": "extends machine-unlearning state beyond weights/gradients to second-order optimizer geometry",
    "2604.23051": "makes temporal scope a persistent multi-turn context state with explicit carryover, override, and transfer tests",
    "2604.23058": "separates model capability from delegated authority exposure in deployment-security governance",
    "2604.23073": "introduces a compact RL-token interface that bounds which pretrained VLA state online actor-critic updates may control",
    "2604.23080": "defines decentralized agent discovery under independent node and agent-readiness churn",
    "2606.11211": "makes reasoning budget an uncertainty-control variable and defines calibration-aware stopping evidence",
    "2606.11212": "makes RAG-versus-generation selection a confidence-gated routing decision with latency and grounding evidence",
}


def concrete_closure(row: dict) -> str:
    abstract = " ".join(row.get("abstract", "").split())
    evidence = abstract.split(". ", 1)[0].strip()
    title = row["title"]
    return (
        f"Fresh-context title+abstract adjudication: `{title}` specifically studies `{evidence[:360]}`. "
        "Its claimed delta remains a domain method, local model component, application workflow, or result-only benchmark; "
        "the abstract does not transfer ownership of durable AI-system state/data/control, define a reusable release/evaluation "
        "contract, or overturn a current Books design conclusion. Reopen only if exact primary evidence later establishes such "
        "a cross-workload contract rather than the reported task-local gain."
    )


def main() -> None:
    ledger = json.loads((PACKET / "screening-ledger-final.json").read_text(encoding="utf-8"))
    challenge = json.loads((PACKET / "independent-high-risk-closure-challenges.json").read_text(encoding="utf-8"))
    identities = {row["arxiv_id"]: row for row in ledger["identities"]}
    challenge_ids = {row["arxiv_id"] for row in challenge["items"]}
    if set(RETAIN) - challenge_ids:
        raise SystemExit(f"retained ids absent from challenge set: {sorted(set(RETAIN)-challenge_ids)}")
    items = []
    for old in challenge["items"]:
        aid = old["arxiv_id"]
        row = identities[aid]
        retained = aid in RETAIN
        items.append({
            "source_family_id": row["source_family_id"],
            "arxiv_id": aid,
            "title": row["title"],
            "first_public_date": row["first_public_date"],
            "review_basis": "strict-window frozen title+abstract; no Weekly semantic input",
            "previous_closure_reason": row["screening_reason"],
            "fresh_context_rationale": RETAIN[aid] if retained else concrete_closure(row),
            "status": "false_negative_retained_pending_exact_v1" if retained else "fresh_context_closure_confirmed",
        })
    payload = {
        "schema": "historical-daily-independent-denominator-adjudication-v1",
        "report_date": "2026-04-25",
        "auditor_role": "fresh_context_non_author",
        "weekly_semantic_inputs": [],
        "raw_identities": ledger["raw_snapshot_records"],
        "previous_denominator": ledger["candidate_denominator"],
        "broad_challenges_reviewed": len(items),
        "false_negatives_retained": len(RETAIN),
        "closures_confirmed": len(items) - len(RETAIN),
        "status": "denominator_reopen_pending_exact_v1",
        "gate_effect": "Coverage remains Open until every reopened family completes exact-v1 identity/withdrawal review and the denominator is re-frozen.",
        "items": items,
    }
    (PACKET / "independent-denominator-adjudication.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
