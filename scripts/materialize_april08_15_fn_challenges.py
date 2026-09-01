#!/usr/bin/env python3
"""Expose confirmed 04-08..15 false negatives to the exact-v1 fetcher."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
for day in range(8, 16):
    packet = ROOT / f"papers/2026/04/_sources/daily-202604{day:02d}"
    audit = json.loads((packet / "independent-recovery-prewrite-audit.json").read_text(encoding="utf-8"))
    payload = {
        "schema": "independent-high-risk-closure-challenges-v1",
        "report_date": audit["report_date"],
        "items": [
            {
                "arxiv_id": row["arxiv_id"],
                "source_family_id": row["source_family_id"],
                "title": row["title"],
                "required_owner": row["required_owner"],
                "challenge_reason": row["finding"],
                "status": "false_negative_challenge_pending_exact_v1",
            }
            for row in audit["false_negative_findings"]
        ],
    }
    (packet / "independent-high-risk-closure-challenges.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
