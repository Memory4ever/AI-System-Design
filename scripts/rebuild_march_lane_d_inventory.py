#!/usr/bin/env python3
"""Rebuild 2026-03-25..31 inventories from the arXiv public-listing batch lead.

DataCite ``Updated:v1`` is used only as the frozen announcement-processing
recovery lead.  For these post-US-DST dates, the official Sun--Thu 20:00 ET
announcement maps to 08:00 Beijing on the same UTC calendar date as the
Updated:v1 batch, so that date owns the report.  ``Submitted:v1`` is retained
as provenance only and never used as the public event time.
"""

from __future__ import annotations

import gzip
import hashlib
import html
import json
import re
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "papers/2026/04/_sources/datacite-arxiv-202603-v2"
RECOVERY = ROOT / "papers/2026/03/_sources/march-2026-arxiv-announcement-recovery.json.gz"
TZ8 = timezone(timedelta(hours=8))
REPORT_DAYS = range(25, 32)


CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.OS", "cs.PF", "cs.AR", "cs.RO"}
FILTERED = {"cs.CV", "cs.CR", "cs.SE", "cs.IR", "cs.DB", "cs.NI", "cs.PL", "cs.MA", "stat.ML", "eess.AS"}


def clean(value: str) -> str:
    return " ".join(html.unescape(value or "").split())


def date_value(attributes: dict, kind: str) -> str | None:
    return next(
        (
            item.get("date")
            for item in attributes.get("dates", [])
            if item.get("dateType") == kind and item.get("dateInformation") == "v1"
        ),
        None,
    )


def category(subject: str) -> str | None:
    match = re.search(r"\(([^()]+)\)$", subject)
    return match.group(1) if match else None


def source_rows() -> list[dict]:
    metadata: dict[str, dict] = {}
    for path in sorted(SNAPSHOT.glob("*.json.gz")):
        payload = json.load(gzip.open(path, "rt"))
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        for record in payload.get("data", []):
            attributes = record["attributes"]
            arxiv_id = record["id"].split("arxiv.", 1)[-1]
            subjects = [category(x.get("subject", "")) for x in attributes.get("subjects", [])]
            subjects = sorted({x for x in subjects if x})
            descriptions = attributes.get("descriptions", [])
            abstract = next((x.get("description", "") for x in descriptions if x.get("descriptionType") == "Abstract"), "")
            title = clean((attributes.get("titles") or [{}])[0].get("title", ""))
            metadata[arxiv_id] = {
                "title": title, "abstract": clean(abstract), "categories": subjects,
                "snapshot_path": path.relative_to(ROOT).as_posix(), "snapshot_sha256": digest,
            }
    recovery = json.load(gzip.open(RECOVERY, "rt"))
    result: list[dict] = []
    for recovered in recovery["records"]:
        report_date = recovered.get("owner_report_date")
        if not report_date or not report_date.startswith("2026-03-") or int(report_date[-2:]) not in REPORT_DAYS:
            continue
        # The shared recovery receipt stores the canonical full arXiv ID.
        # (An early transient version contained only the numeric suffix.)
        arxiv_id = recovered["arxiv_id"]
        info = metadata[arxiv_id]
        result.append({
            "arxiv_id": arxiv_id, "source_family_key": f"arxiv:{arxiv_id}",
            "title": info["title"], "abstract": info["abstract"], "categories": info["categories"],
            "submitted_v1_utc_provenance_only": recovered["submitted_v1_utc"],
            "updated_v1_utc_announcement_recovery_lead": recovered["registry_updated_v1_utc"],
            "announcement_eastern": recovered["announcement_eastern"],
            "announcement_beijing": recovered["announcement_beijing"],
            "announcement_recovery_status": recovered["status"],
            "listing_batch_date": recovered["announcement_eastern"][:10],
            "report_date": report_date, "snapshot_path": info["snapshot_path"],
            "snapshot_sha256": info["snapshot_sha256"],
        })
    return sorted(result, key=lambda row: (row["report_date"], row["arxiv_id"]))


def archive_receipt(rows: list[dict], report_day: int) -> dict:
    report_date = date(2026, 3, report_day)
    batch_date = report_date
    selected = [row for row in rows if row["report_date"] == report_date.isoformat()]
    anomalies = [row["arxiv_id"] for row in selected if row["announcement_recovery_status"] != "scheduled_match"]
    return {
        "schema": "daily-v2.1-official-arxiv-listing-receipt-v1",
        "report_date": report_date.isoformat(),
        "listing_batch_date": batch_date.isoformat(),
        "ownership_rule": "official Sun-Thu 20:00 ET announcement is mapped to its exact Beijing instant and then into the strict half-open Daily window",
        "updated_v1_role": "announcement-processing recovery lead only; ownership comes from the recovered official schedule slot",
        "recovery_receipt": RECOVERY.relative_to(ROOT).as_posix(),
        "official_archive": ["https://arxiv.org/list/cs/2026-03", "https://arxiv.org/list/stat/2026-03", "https://arxiv.org/list/eess/2026-03"],
        "registered_identities": len(selected),
        "scheduled_matches": len(selected) - len(anomalies),
        "announcement_anomalies": anomalies,
        "status": "checked" if not anomalies else "incomplete_pending_anomaly_adjudication",
    }


def main() -> None:
    rows = source_rows()
    for day in REPORT_DAYS:
        report_date = f"2026-03-{day:02d}"
        selected = [row for row in rows if row["report_date"] == report_date]
        packet = ROOT / f"papers/2026/03/_sources/daily-202603{day:02d}"
        packet.mkdir(parents=True, exist_ok=True)
        identities = []
        for row in selected:
            cats = set(row["categories"])
            route = "core_daily_semantic_review_required" if cats & CORE else (
                "keyword_daily_semantic_review_required" if cats & FILTERED else "false_negative_audit_required"
            )
            identities.append({**row, "screening_route": route, "screening_status": "pending_full_title_abstract_semantic_screen"})
        payload = {
            "schema": "daily-v2.1-updated-v1-announcement-batch-inventory-v1",
            "report_date": report_date,
            "strict_window": f"[2026-03-{day-1:02d}T09:00:00+08:00,{report_date}T09:00:00+08:00)",
            "listing_batch_date": report_date,
            "submitted_time_role": "provenance_only",
            "registered_identities": len(identities),
            "semantic_screen_required": len(identities),
            "identities": identities,
        }
        (packet / "screening-ledger-updated-v1-replay.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        (packet / "official-arxiv-listing-receipt.json").write_text(
            json.dumps(archive_receipt(rows, day), ensure_ascii=False, indent=2) + "\n"
        )
        print(report_date, len(identities))


if __name__ == "__main__":
    main()
