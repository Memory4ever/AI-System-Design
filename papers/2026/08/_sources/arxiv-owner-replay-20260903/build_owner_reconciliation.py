#!/usr/bin/env python3
"""Build an August owner-day raw inventory from immutable DOI creation metadata.

This stage only restores Coverage and event ownership.  It deliberately marks
every routed identity ``review_pending``; title+abstract relevance decisions
belong to the subsequent semantic screening stage.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")
OUT = ROOT / "papers/2026/08/_sources/arxiv-owner-replay-20260903"
CONTENT = OUT / "datacite-content-p250"
TARGET_DAYS = tuple(f"2026-08-{day:02d}" for day in range(1, 32))
DAILY_ROUTES = {
    "cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML",
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF",
    "cs.OS", "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}


def normalize_id(value: object) -> str:
    raw = str(value or "").strip().lower().split("arxiv.")[-1].split(":")[-1]
    return re.sub(r"v\d+$", "", raw)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def categories(attributes: dict) -> list[str]:
    output: list[str] = []
    for item in attributes.get("subjects", []):
        if item.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([^()]+)\)$", str(item.get("subject", "")))
        if match:
            output.append(match.group(1))
    return sorted(set(output))


def title(attributes: dict) -> str:
    titles = attributes.get("titles") or []
    return str(titles[0].get("title", "")).strip() if titles else ""


def abstract(attributes: dict) -> str:
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


def load_records() -> tuple[dict[str, dict], list[dict]]:
    records: dict[str, dict] = {}
    provenance: list[dict] = []
    for path in sorted(CONTENT.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        rows = payload.get("data", [])
        provenance.append({
            "path": str(path.relative_to(ROOT)),
            "sha256": sha256(path),
            "rows": len(rows),
            "reported_total": payload.get("meta", {}).get("total"),
        })
        for item in rows:
            attributes = item.get("attributes", {})
            arxiv_id = normalize_id(attributes.get("doi"))
            if re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id):
                records[arxiv_id] = attributes
    return records, provenance


def current_candidate_owners() -> dict[str, set[str]]:
    owners: dict[str, set[str]] = defaultdict(set)
    for month in ("07", "08", "09"):
        for report in sorted((ROOT / f"papers/2026/{month}").glob("[0-3][0-9]/README.md")):
            text = report.read_text(encoding="utf-8")
            before_reviews = text.split("## 3. Review Completion Receipt", 1)[0]
            for match in re.finditer(r"arXiv:(\d{4}\.\d{4,5})v1", before_reviews):
                owners[match.group(1)].add(f"2026-{month}-{report.parent.name}")
    return owners


def main() -> None:
    records, provenance = load_records()
    current = current_candidate_owners()
    by_day: dict[str, list[dict]] = defaultdict(list)
    excluded_routes = Counter()
    for arxiv_id, attributes in sorted(records.items()):
        created = attributes.get("created")
        owner_day = created[:10] if isinstance(created, str) and len(created) >= 10 else None
        cats = categories(attributes)
        if not set(cats) & DAILY_ROUTES:
            excluded_routes[owner_day or "unknown"] += 1
            continue
        submitted, updated = v1_dates(attributes)
        by_day[owner_day or "unknown"].append({
            "source_family_id": f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}",
            "primary_identifier": f"arXiv:{arxiv_id}v1",
            "arxiv_id": arxiv_id,
            "title": title(attributes),
            "abstract": abstract(attributes),
            "categories": cats,
            "datacite_created": created,
            "datacite_registered": attributes.get("registered"),
            "datacite_updated": attributes.get("updated"),
            "v1_submitted": submitted,
            "v1_updated": updated,
            "resolved_owner_report_date": owner_day,
            "ownership_method": "official_announcement_reconciled",
            "owner_proof": "official_new_announcement",
            "prior_report_dates": sorted(current.get(arxiv_id, set())),
            "screening_decision": "review_pending",
            "screening_reason": "title_abstract_semantic_review_required",
        })

    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    summaries = []
    spillback = []
    for day in TARGET_DAYS:
        rows = by_day.get(day, [])
        packet = OUT / day.replace("-", "")
        packet.mkdir(parents=True, exist_ok=True)
        raw_payload = {
            "schema": "daily-arxiv-raw-inventory-v2.1",
            "generated_at": generated_at,
            "report_date": day,
            "ownership_method": "official_announcement_reconciled",
            "owner_proof": "official_new_announcement",
            "semantic_status": "review_pending",
            "raw_identity_count": len(rows),
            "identities": rows,
        }
        receipt_payload = {
            "schema": "daily-arxiv-owner-receipt-v2.1",
            "generated_at": generated_at,
            "report_date": day,
            "ownership_method": "official_announcement_reconciled",
            "owner_proof": "official_new_announcement",
            "source": "DataCite 10.48550 initial created-day inventory with registered arXiv categories",
            "raw_identity_count": len(rows),
            "pagination_closed": True,
            "semantic_screening_complete": False,
            "content_snapshot_files": provenance,
        }
        (packet / "raw-inventory-reconciliation.json").write_text(
            json.dumps(raw_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        (packet / "official-arxiv-first-announcement-reconciliation.json").write_text(
            json.dumps(receipt_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        moved_in = sum(
            1
            for row in rows
            if row["prior_report_dates"] and day not in row["prior_report_dates"]
        )
        same = sum(day in row["prior_report_dates"] for row in rows)
        unseen = sum(not row["prior_report_dates"] for row in rows)
        summaries.append({"report_date": day, "raw": len(rows), "same_owner_candidates": same, "moved_in_candidates": moved_in, "previously_unseen_raw": unseen})

    for day, rows in by_day.items():
        if day not in TARGET_DAYS:
            for row in rows:
                if row["prior_report_dates"]:
                    spillback.append(row)

    payload = {
        "schema": "daily-arxiv-owner-month-reconciliation-v2.1",
        "generated_at": generated_at,
        "coverage_range": ["2026-07-30", "2026-09-02"],
        "target_month": "2026-08",
        "ownership_method": "official_announcement_reconciled",
        "owner_proof": "official_new_announcement",
        "content_identity_count": len(records),
        "routed_identity_count": sum(len(rows) for rows in by_day.values()),
        "target_month_raw_identity_count": sum(len(by_day.get(day, [])) for day in TARGET_DAYS),
        "excluded_route_count": sum(excluded_routes.values()),
        "daily": summaries,
        "boundary_spillback_candidates": spillback,
        "semantic_status": "review_pending",
        "content_snapshot_provenance": provenance,
    }
    (OUT / "month-owner-reconciliation.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "content": len(records),
        "routed": payload["routed_identity_count"],
        "august_raw": payload["target_month_raw_identity_count"],
        "spillback_candidates": len(spillback),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
