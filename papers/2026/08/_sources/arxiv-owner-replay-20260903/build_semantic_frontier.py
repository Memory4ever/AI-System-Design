#!/usr/bin/env python3
"""Create a non-decisional August title+abstract review frontier.

The output preserves every routed raw identity.  It does not infer relevance
from keywords and therefore cannot close the Candidate Denominator by itself.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")
REPLAY = ROOT / "papers/2026/08/_sources/arxiv-owner-replay-20260903"


def prior_candidates() -> dict[str, set[str]]:
    output: dict[str, set[str]] = defaultdict(set)
    for month in ("07", "08", "09"):
        for report in sorted((ROOT / f"papers/2026/{month}").glob("[0-3][0-9]/README.md")):
            before_reviews = report.read_text(encoding="utf-8").split("## 3. Review Completion Receipt", 1)[0]
            for match in re.finditer(r"arXiv:(\d{4}\.\d{4,5})v1", before_reviews):
                output[match.group(1)].add(f"2026-{month}-{report.parent.name}")
    return output


def main() -> None:
    prior = prior_candidates()
    rows = []
    daily = Counter()
    same_owner = Counter()
    moved = Counter()
    fresh = Counter()
    for packet in sorted(REPLAY.glob("202608[0-3][0-9]")):
        path = packet / "raw-inventory-reconciliation.json"
        if not path.exists():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("identities", []):
            arxiv_id = item["arxiv_id"]
            owner_day = item["resolved_owner_report_date"]
            prior_days = sorted(prior.get(arxiv_id, set()))
            if owner_day in prior_days:
                status = "existing_candidate_reaudit"
                same_owner[owner_day] += 1
            elif prior_days:
                status = "moved_candidate_reaudit"
                moved[owner_day] += 1
            else:
                status = "fresh_title_abstract_review"
                fresh[owner_day] += 1
            row = dict(item)
            row.update({
                "prior_candidate_report_dates": prior_days,
                "frontier_status": status,
                "semantic_decision": "pending",
                "semantic_reason": "fresh_context_title_abstract_review_required",
            })
            rows.append(row)
            daily[owner_day] += 1

    payload = {
        "schema": "daily-semantic-screening-frontier-v2.1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "target_month": "2026-08",
        "decision_policy": "non_decisional_frontier; no keyword or template closure",
        "raw_identity_count": len(rows),
        "existing_candidate_same_owner": sum(same_owner.values()),
        "existing_candidate_moved_owner": sum(moved.values()),
        "fresh_identity_count": sum(fresh.values()),
        "daily": [
            {
                "report_date": day,
                "raw": daily[day],
                "existing_same_owner": same_owner[day],
                "existing_moved_owner": moved[day],
                "fresh_review": fresh[day],
            }
            for day in sorted(daily)
        ],
        "rows": rows,
    }
    output = REPLAY / "semantic-screening-frontier.json"
    output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: payload[key] for key in (
        "raw_identity_count", "existing_candidate_same_owner",
        "existing_candidate_moved_owner", "fresh_identity_count",
    )}, ensure_ascii=False))


if __name__ == "__main__":
    main()
