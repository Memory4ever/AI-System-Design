#!/usr/bin/env python3
"""Materialize the independent 2026-05-09 denominator reconciliation.

This script preserves the author packet and writes a separate canonical-review
candidate.  It never edits shared Books.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
AUTHOR = json.loads((ROOT / "screening-ledger-final.json").read_text())
AUDIT = json.loads((ROOT / "independent-semantic-audit.json").read_text())

DROP = {item["arxiv_id"] for item in AUDIT["false_positive_findings"]}
ADD = {item["arxiv_id"]: item for item in AUDIT["false_negative_findings"]}
OWNER = AUDIT["owner_corrections"]
DISPOSITION = AUDIT["books_disposition_corrections"]
BLOCKED = set(AUDIT["evidence_findings"]["generic_locator_receipts"]) | set(ADD)

INTEGRATE = {
    "2605.07135", "2605.07238", "2605.07242", "2605.07330",
    "2605.07569", "2605.07594", "2605.07689", "2605.07836",
    "2605.07935", "2605.08317", "2605.08374", "2605.08460",
    "2605.08513", "2605.08524", "2605.08527", "2605.08541",
    "2605.08545", "2605.08563", "2605.08580", "2605.08581",
    "2606.20582",
}

# Score is a routing decision, not a proxy for evidence or Books disposition.
# These rules intentionally yield distinct 5-9 routes according to the actual
# type of contract delta challenged in the independent replay.
SCORE_EXPLICIT = {
    "2605.07135": (3, 3, 3), "2605.07238": (3, 3, 3),
    "2605.07242": (3, 3, 3), "2605.07330": (3, 3, 2),
    "2605.07569": (3, 3, 2), "2605.07594": (3, 2, 3),
    "2605.07689": (3, 2, 3), "2605.07836": (3, 3, 3),
    "2605.07935": (3, 3, 3), "2605.08317": (3, 2, 3),
    "2605.08374": (3, 3, 3), "2605.08460": (3, 3, 3),
    "2605.08513": (3, 3, 3), "2605.08524": (3, 3, 2),
    "2605.08527": (3, 3, 2), "2605.08541": (3, 2, 3),
    "2605.08545": (3, 3, 3), "2605.08563": (3, 3, 3),
    "2605.08580": (3, 3, 3), "2605.08581": (3, 3, 3),
    "2606.20582": (3, 3, 3),
    "2605.08363": (3, 3, 3), "2605.08565": (2, 2, 3),
    "2606.27379": (3, 2, 3),
}


def routed_score(row: dict, owner: str) -> tuple[int, int, int]:
    aid = row["arxiv_id"]
    if aid in SCORE_EXPLICIT:
        return SCORE_EXPLICIT[aid]
    text = f"{row['title']} {row.get('abstract', '')}".lower()
    if any(word in text for word in ("benchmark", "evaluation framework", "evaluation protocol")):
        return (2, 2, 2)
    if owner in {"PLATFORM-SECURITY", "AGENT-MULTI-AGENT", "AGENT-MCP"}:
        return (2, 3, 3)
    if any(word in text for word in ("kernel", "quantization", "cuda", "profiling")):
        return (2, 1, 2)
    return (2, 2, 3)


rows = []
for original in AUTHOR["identities"]:
    row = dict(original)
    aid = row["arxiv_id"]
    if aid in DROP:
        row.update(
            screening_status="pre_denominator_closed",
            screening_reason=next(x["reason"] for x in AUDIT["false_positive_findings"] if x["arxiv_id"] == aid),
            review_status="identity_date_closed",
            access_status="verified",
            integration_disposition="Rejected — Below Candidate Denominator",
        )
        for key in ("source_family_id", "owner_node", "score_v2"):
            row.pop(key, None)
    elif aid in ADD or row["screening_status"].startswith("retained"):
        owner = ADD[aid]["proposed_owner"] if aid in ADD else OWNER.get(aid, row.get("owner_node"))
        d, s, u = routed_score(row, owner)
        row.update(
            source_family_id=f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            owner_node=owner,
            score_v2={"design_delta": d, "system_reach": s, "durability": u, "total": d + s + u},
            screening_status="retained",
            integration_disposition=(
                "Blocked / Unverified" if aid in ADD else
                DISPOSITION.get(aid, "Integrate" if aid in INTEGRATE else row.get("integration_disposition", "No Change — Existing Coverage"))
            ),
        )
        if aid in BLOCKED:
            row.update(review_status="blocked", access_status="blocked")
            if aid in ADD:
                row["screening_reason"] = ADD[aid]["admission_reason"]
        else:
            row.update(review_status="deep_complete" if d + s + u >= 7 else "standard_complete", access_status="accessible")
    rows.append(row)

retained = [row for row in rows if row["screening_status"] == "retained"]
closed = [row for row in rows if row["screening_status"] == "pre_denominator_closed"]
assert len(rows) == 834
assert len(retained) == 83
assert len(closed) == 751
assert sum(row["review_status"] == "blocked" for row in retained) == 17

payload = {
    **{key: value for key, value in AUTHOR.items() if key != "identities"},
    "schema": "daily-v2.1-screening-ledger-independent-reconciled-v1",
    "report_date": "2026-05-09",
    "registered_window_identities": 834,
    "semantic_screened": 834,
    "candidate_denominator": 83,
    "pre_denominator_closures": 751,
    "denominator_id": "DEN-20260509-INDEPENDENT-83",
    "denominator_frozen_at": "2026-09-01T17:20:00+08:00",
    "gate_status": "coverage_reconciled_evidence_conditional_books_waiting_root",
    "audit_ref": "independent-semantic-audit.json",
    "identities": rows,
}

encoded = (json.dumps(payload, ensure_ascii=False, indent=2) + "\n").encode()
(ROOT / "screening-ledger-independent-final.json").write_bytes(encoded)
(ROOT / "screening-ledger-independent-final.sha256").write_text(hashlib.sha256(encoded).hexdigest() + "\n")
