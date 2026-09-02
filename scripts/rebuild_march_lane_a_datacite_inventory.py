#!/usr/bin/env python3
"""Materialize March 1--8 announcement-owned inventories from root receipt.

The shared receipt is a primary-source reconciliation artifact, not a Weekly.
It derives scheduled announcement instants from arXiv's official availability
schedule and DataCite DOI-created recovery leads.  This lane joins abstracts
from the frozen DataCite metadata snapshot. Submitted:v1 and Updated:v1 remain
version provenance only and never own a Daily window.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "papers/2026/04/_sources/datacite-arxiv-202603-v2"
RECOVERY = ROOT / "papers/2026/03/_sources/march-2026-arxiv-announcement-recovery.json.gz"
MONTH = ROOT / "papers/2026/03"
BEIJING = timezone(timedelta(hours=8))

def clean(value: str) -> str:
    return " ".join(value.split())


def load_attrs() -> dict[str, dict]:
    result = {}
    for path in sorted(SNAPSHOT.glob("*.json.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        for item in payload.get("data", []):
            attrs = item.get("attributes", {})
            doi = attrs.get("doi", "").lower()
            if doi.startswith("10.48550/arxiv.2603."):
                result[doi.rsplit(".", 1)[1]] = attrs
    return result


def abstract(attrs: dict) -> str:
    return clean(next((
        x.get("description", "") for x in attrs.get("descriptions", [])
        if x.get("descriptionType") == "Abstract"
    ), ""))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with gzip.open(RECOVERY, "rt", encoding="utf-8") as handle:
        recovery = json.load(handle)
    attrs_by_suffix = load_attrs()
    grouped = {f"2026-03-{d:02d}": [] for d in range(1, 9)}
    anomaly_packets = {key: [] for key in grouped}
    for record in recovery["records"]:
        aid = record["arxiv_id"]
        suffix = aid.split(".", 1)[1]
        owner = record.get("owner_report_date")
        if record["status"] != "scheduled_match":
            if owner in anomaly_packets:
                anomaly_packets[owner].append(record)
            continue
        if owner not in grouped:
            continue
        attrs = attrs_by_suffix.get(suffix, {})
        row = dict(record)
        row.update({
            "arxiv_id": aid,
            "identity": f"{aid}v1",
            "source_family_id": f"SF-2026-ARXIV-2603-{suffix}",
            "title": clean(record.get("title", "")),
            "abstract": abstract(attrs),
            "primary_category": (record.get("categories") or [""])[0],
            "route": "registered_category_full_semantic_screen",
            "source_url": f"https://arxiv.org/abs/2603.{suffix}v1",
        })
        grouped[owner].append(row)

    for report_date, rows in grouped.items():
        day = int(report_date[-2:])
        end = datetime.combine(date(2026, 3, day), time(9), BEIJING)
        start = end - timedelta(days=1)
        rows.sort(key=lambda x: (x.get("announcement_beijing") or "", x["arxiv_id"]))
        packet = MONTH / "_sources" / f"daily-{report_date.replace('-', '')}"
        packet.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema": "daily-v2.1-arxiv-announcement-owned-inventory-v3",
            "report_date": report_date,
            "window_beijing": {"start": start.isoformat(), "end": end.isoformat()},
            "source_role": recovery["authority_boundary"],
            "official_schedule_url": recovery["official_schedule_url"],
            "official_month_archive_urls": recovery["official_month_archive_urls"],
            "recovery_receipt": {
                "path": RECOVERY.relative_to(ROOT).as_posix(),
                "sha256": sha(RECOVERY),
            },
            "registered_total": len(rows),
            "scheduled_match_total": sum(x["status"] == "scheduled_match" for x in rows),
            "manual_anomaly_adjudication_total": 0,
            "identities": rows,
        }
        (packet / "inventory.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        (packet / "announcement-anomalies.json").write_text(json.dumps({
            "schema": "announcement-anomaly-adjudication-v1",
            "report_date": report_date,
            "items": anomaly_packets[report_date],
            "fresh_context_status": "pending",
        }, ensure_ascii=False, indent=2) + "\n")
        print(json.dumps({
            "date": report_date, "raw": len(rows),
            "scheduled": payload["scheduled_match_total"],
            "manual_anomalies": payload["manual_anomaly_adjudication_total"],
        }))


if __name__ == "__main__":
    main()
