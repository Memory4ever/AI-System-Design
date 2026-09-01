#!/usr/bin/env python3
"""Build a non-author false-negative challenge ledger for 2026-04-24..30.

This script never promotes a paper automatically.  It only identifies closure
rows whose title/abstract contain an explicit AI-system mechanism or ownership
change, so a fresh-context reviewer can adjudicate them against the full text.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAYS = range(24, 31)

ROUTES = {
    "inference_state_or_runtime": (
        r"\bkv cache\b",
        r"\bprefill\b",
        r"\bdecode\b",
        r"\bspeculative decoding\b",
        r"\bserving\b",
        r"\binference runtime\b",
        r"\bbatching\b",
        r"\boffload(?:ing)?\b",
    ),
    "distributed_control_or_communication": (
        r"\bdistributed\b",
        r"\bcollective(?:s)?\b",
        r"\bcommunication\b",
        r"\bschedul(?:e|er|ing)\b",
        r"\bplacement\b",
        r"\bparallelism\b",
        r"\bpipeline\b",
        r"\bmulti-node\b",
    ),
    "training_objective_or_state": (
        r"\bpost-training\b",
        r"\breinforcement learning\b",
        r"\bpreference optimization\b",
        r"\bcheckpoint\b",
        r"\boptimizer\b",
        r"\bgradient\b",
        r"\bfine-tun(?:e|ing)\b",
        r"\btraining system\b",
    ),
    "agent_state_action_or_security": (
        r"\bagent(?:ic)?\b",
        r"\btool[- ](?:use|calling)\b",
        r"\bprompt injection\b",
        r"\bmemory\b",
        r"\bworkflow\b",
        r"\bmulti-agent\b",
        r"\bsandbox\b",
        r"\bguardrail\b",
    ),
    "multimodal_world_or_embodied": (
        r"\bworld model\b",
        r"\bvision-language-action\b",
        r"\bvla\b",
        r"\bembodied\b",
        r"\brobot(?:ic|ics)?\b",
        r"\bvideo generation\b",
        r"\bmultimodal\b",
    ),
    "evaluation_or_evidence_contract": (
        r"\bevaluation\b",
        r"\bbenchmark(?:ing)?\b",
        r"\buncertainty\b",
        r"\bcalibrat(?:e|ed|ion)\b",
        r"\bprovenance\b",
        r"\baudit(?:ing)?\b",
        r"\breproducib(?:le|ility)\b",
    ),
    "execution_kernel_or_hardware": (
        r"\bcuda\b",
        r"\bkernel\b",
        r"\baccelerator\b",
        r"\bgpu\b",
        r"\bquantiz(?:e|ed|ation)\b",
        r"\bcompiler\b",
        r"\bmemory bandwidth\b",
    ),
}


def challenge_reasons(row: dict) -> list[str]:
    if row.get("screening_status") != "pre_denominator_closed":
        return []
    text = f"{row.get('title', '')} {row.get('abstract', '')}".lower()
    if "withdrawn" in text or row.get("candidate_state") == "withdrawn_primary_source":
        return []
    reasons = []
    for route, patterns in ROUTES.items():
        if any(re.search(pattern, text) for pattern in patterns):
            reasons.append(route)
    # A single generic word is insufficient.  Reopen when two independent
    # system routes are present, or when one route has multiple concrete hits.
    if len(reasons) >= 2:
        return reasons
    if len(reasons) == 1:
        route = reasons[0]
        hits = sum(bool(re.search(pattern, text)) for pattern in ROUTES[route])
        if hits >= 2:
            return reasons
    return []


def main() -> None:
    month_summary = {
        "schema": "historical-daily-independent-denominator-challenge-summary-v1",
        "scope": "2026-04-24..2026-04-30",
        "weekly_semantic_inputs": [],
        "status": "open_pending_fresh_context_adjudication",
        "days": [],
    }
    for day in DAYS:
        report_date = f"2026-04-{day:02d}"
        packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
        ledger_path = packet / "screening-ledger-final.json"
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
        challenges = []
        for row in ledger.get("identities", []):
            reasons = challenge_reasons(row)
            if not reasons:
                continue
            challenges.append(
                {
                    "source_family_id": row.get("source_family_id"),
                    "arxiv_id": row.get("arxiv_id"),
                    "title": row.get("title"),
                    "first_public_date": row.get("first_public_date"),
                    "author_closure_reason": row.get("screening_reason"),
                    "challenge_routes": reasons,
                    "status": "pending_exact_v1_fresh_context_adjudication",
                }
            )
        route_counts = Counter(r for item in challenges for r in item["challenge_routes"])
        receipt = {
            "schema": "historical-daily-independent-denominator-challenge-v1",
            "report_date": report_date,
            "weekly_semantic_inputs": [],
            "raw_identities": ledger.get("raw_snapshot_records"),
            "author_retained": ledger.get("candidate_denominator"),
            "author_closures": ledger.get("pre_denominator_closed"),
            "challenge_count": len(challenges),
            "route_counts": dict(sorted(route_counts.items())),
            "status": "open_pending_fresh_context_adjudication",
            "gate_effect": "Coverage remains Open; no challenge is auto-promoted.",
            "items": challenges,
        }
        out = packet / "independent-high-risk-closure-challenges.json"
        out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        month_summary["days"].append(
            {
                "report_date": report_date,
                "raw_identities": receipt["raw_identities"],
                "author_retained": receipt["author_retained"],
                "author_closures": receipt["author_closures"],
                "challenge_count": len(challenges),
                "receipt": str(out.relative_to(ROOT)),
            }
        )
    summary_path = ROOT / "papers/2026/04/_sources/april-24-30-denominator-challenge-summary.json"
    summary_path.write_text(json.dumps(month_summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
