#!/usr/bin/env python3
"""Fresh-context denominator adjudication for the 2026-04-24 Historical Daily.

The previous Weekly is deliberately absent from every input.  The reviewer
re-checks the frozen title/abstract ledger and the broad non-author challenge
pool.  Only explicit long-lived AI-system state, control, evidence, training,
runtime, or security changes are reopened; exact-v1 review is a later Gate.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "papers/2026/04/_sources/daily-20260424"

# Explicit false negatives found by a fresh-context title+abstract review.
# Values state why the family crosses the Candidate Denominator boundary; they
# do not claim that the paper's mechanism or results have passed exact-v1 review.
RETAIN = {
    "2604.21192": "changes embodied-policy evaluation from task success alone to open-world safety violations and interactive failure evidence",
    "2604.21193": "introduces claim-level attribution and verification state rather than treating answer-level fluency as evidence",
    "2604.21275": "changes distributed training data ownership through reproducible high-throughput pipeline state and replay contracts",
    "2604.21361": "identifies causal-time and observability contracts specific to distributed AI inference control planes",
    "2604.21428": "changes decentralized pre-training synchronization, failure isolation, and progress ownership",
    "2604.21477": "changes MCP server security testing from isolated tool checks to multi-vector protocol and implementation evidence",
    "2604.21725": "treats the agent harness as a versioned evolving system artifact with its own evaluation and promotion loop",
    "2604.21794": "changes multi-agent communication from fixed messages to an end-to-end optimized coordination interface",
    "2604.21829": "exposes agent skill behavior as an extractable security asset and therefore changes artifact and access boundaries",
    "2604.21860": "shows that stateless per-turn moderation loses cross-turn attack state and requires session-level security ownership",
    "2604.21927": "separates fine-tuning regimes into distinct continual-learning contracts with different retention and forgetting pressure",
    "2604.21930": "shows that temporal task construction can change continual-learning evidence and therefore the evaluation contract",
    "2604.22032": "introduces portable kernel correctness contracts across heterogeneous hardware instead of benchmark-only validation",
    "2604.22038": "makes source-modality identity an explicit runtime monitoring signal for multimodal model behavior",
    "2604.22074": "separates outcome reward from verifiable causal reasoning evidence in post-training and evaluation",
    "2604.22076": "changes unlearning acceptance from surface refusal to persistent privacy and latent-effect evidence",
    "2604.22082": "changes sandbagging mitigation into a weak-supervision training and capability-evaluation contract",
    "2604.22117": "adds diffuse pre-training data seeding as a supply-chain attack with latent activation and provenance requirements",
    "2604.22136": "separates reasoning proposal from real-world execution authority in agentic system loops",
    "2604.22871": "turns red-team strategy generation into a versioned agent-driven search and evidence loop",
}


def main() -> None:
    ledger = json.loads((PACKET / "screening-ledger-final.json").read_text(encoding="utf-8"))
    challenge = json.loads(
        (PACKET / "independent-high-risk-closure-challenges.json").read_text(encoding="utf-8")
    )
    identities = {row["arxiv_id"]: row for row in ledger["identities"]}
    challenge_ids = {row["arxiv_id"] for row in challenge["items"]}
    missing = set(RETAIN) - set(identities)
    if missing:
        raise SystemExit(f"retained false-negative IDs missing from frozen ledger: {sorted(missing)}")
    invalid = {
        aid for aid in RETAIN
        if identities[aid].get("screening_status") != "pre_denominator_closed"
    }
    if invalid:
        raise SystemExit(f"false-negative IDs were not prior closures: {sorted(invalid)}")

    reviewed_ids = sorted(challenge_ids | set(RETAIN))
    items = []
    for aid in reviewed_ids:
        row = identities[aid]
        if aid in RETAIN:
            status = "false_negative_retained_pending_exact_v1"
            rationale = RETAIN[aid]
        else:
            status = "fresh_context_closure_confirmed"
            rationale = (
                "Fresh-context title+abstract review confirms that the contribution remains a "
                "domain task, local model method, benchmark/result, or application workflow; it "
                "does not independently change a durable AI-system state owner, control boundary, "
                "evaluation/release contract, or existing Books design conclusion."
            )
        items.append(
            {
                "source_family_id": row["source_family_id"],
                "arxiv_id": aid,
                "title": row["title"],
                "first_public_date": row["first_public_date"],
                "review_basis": "frozen title+abstract; no Weekly semantic input",
                "previous_closure_reason": row["screening_reason"],
                "fresh_context_rationale": rationale,
                "status": status,
            }
        )

    payload = {
        "schema": "historical-daily-independent-denominator-adjudication-v1",
        "report_date": "2026-04-24",
        "auditor_role": "fresh_context_non_author_root",
        "weekly_semantic_inputs": [],
        "raw_identities": ledger["raw_snapshot_records"],
        "previous_denominator": ledger["candidate_denominator"],
        "broad_challenges_reviewed": len(challenge_ids),
        "supplemental_closures_reviewed": len(set(RETAIN) - challenge_ids),
        "false_negatives_retained": len(RETAIN),
        "closures_confirmed": len(reviewed_ids) - len(RETAIN),
        "status": "denominator_reopen_pending_exact_v1",
        "gate_effect": (
            "Coverage remains Open. The denominator must be re-frozen after every reopened family "
            "passes exact-v1 identity/withdrawal review; Evidence and Books remain Open."
        ),
        "items": items,
    }
    (PACKET / "independent-denominator-adjudication.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
