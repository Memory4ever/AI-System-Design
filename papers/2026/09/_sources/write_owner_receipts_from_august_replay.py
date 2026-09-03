#!/usr/bin/env python3
"""Write September 1–2 owner/raw receipts from the closed Aug/Sep snapshot."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")
CONTENT = ROOT / "papers/2026/08/_sources/arxiv-owner-replay-20260903/datacite-content-p250"
DAILY_ROUTES = {
    "cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML",
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF",
    "cs.OS", "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}


def normalize_id(doi: str) -> str:
    return re.sub(r"v\d+$", "", doi.lower().split("arxiv.")[-1])


def categories(attributes: dict) -> list[str]:
    output = []
    for item in attributes.get("subjects", []):
        if item.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([^()]+)\)$", str(item.get("subject", "")))
        if match:
            output.append(match.group(1))
    return sorted(set(output))


def field(attributes: dict, name: str) -> str:
    if name == "title":
        values = attributes.get("titles") or []
        return str(values[0].get("title", "")).strip() if values else ""
    return " ".join(
        str(item.get("description", "")).strip()
        for item in attributes.get("descriptions", [])
        if item.get("descriptionType") == "Abstract"
    ).strip()


def v1_dates(attributes: dict) -> tuple[str | None, str | None]:
    submitted = updated = None
    for item in attributes.get("dates", []):
        if item.get("dateInformation") != "v1":
            continue
        if item.get("dateType") == "Submitted":
            submitted = item.get("date")
        elif item.get("dateType") == "Updated":
            updated = item.get("date")
    return submitted, updated


def main() -> None:
    by_day = {"2026-09-01": [], "2026-09-02": []}
    files = sorted(CONTENT.glob("*.json"))
    for path in files:
        payload = json.loads(path.read_text(encoding="utf-8"))
        for item in payload.get("data", []):
            attributes = item.get("attributes", {})
            created = attributes.get("created")
            day = created[:10] if isinstance(created, str) else None
            if day not in by_day:
                continue
            cats = categories(attributes)
            if not set(cats) & DAILY_ROUTES:
                continue
            arxiv_id = normalize_id(str(attributes.get("doi", "")))
            submitted, updated = v1_dates(attributes)
            by_day[day].append({
                "source_family_id": f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}",
                "primary_identifier": f"arXiv:{arxiv_id}v1",
                "arxiv_id": arxiv_id,
                "title": field(attributes, "title"),
                "abstract": field(attributes, "abstract"),
                "categories": cats,
                "datacite_created": created,
                "datacite_registered": attributes.get("registered"),
                "datacite_updated": attributes.get("updated"),
                "v1_submitted": submitted,
                "v1_updated": updated,
                "resolved_owner_report_date": day,
                "ownership_method": "official_announcement_reconciled",
                "owner_proof": "official_new_announcement",
                "screening_decision": "review_pending",
                "screening_reason": "title_abstract_semantic_review_required",
            })

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    summary = []
    for day, rows in by_day.items():
        rows.sort(key=lambda row: row["arxiv_id"])
        packet = ROOT / f"papers/2026/09/_sources/daily-{day.replace('-', '')}"
        packet.mkdir(parents=True, exist_ok=True)
        (packet / "raw-inventory-reconciliation.json").write_text(
            json.dumps({
                "schema": "daily-arxiv-raw-inventory-v2.1",
                "generated_at": generated_at,
                "report_date": day,
                "ownership_method": "official_announcement_reconciled",
                "owner_proof": "official_new_announcement",
                "semantic_status": "review_pending",
                "raw_identity_count": len(rows),
                "identities": rows,
            }, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        (packet / "official-arxiv-first-announcement-reconciliation.json").write_text(
            json.dumps({
                "schema": "daily-arxiv-owner-receipt-v2.1",
                "generated_at": generated_at,
                "report_date": day,
                "ownership_method": "official_announcement_reconciled",
                "owner_proof": "official_new_announcement",
                "source": "DataCite 10.48550 initial created-day inventory with registered arXiv categories",
                "raw_identity_count": len(rows),
                "pagination_closed": True,
                "semantic_screening_complete": False,
                "content_snapshot_directory": str(CONTENT.relative_to(ROOT)),
            }, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        summary.append({"report_date": day, "raw_identity_count": len(rows)})
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
