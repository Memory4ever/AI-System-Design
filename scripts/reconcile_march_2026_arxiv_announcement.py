#!/usr/bin/env python3
"""Recover March 2026 arXiv Daily ownership without using Weekly reports.

The frozen DataCite snapshot supplies DOI identity and the DOI ``created``
timestamp. ``Submitted:v1`` and ``Updated:v1`` are version/registry provenance
only: either can differ materially from first public announcement.  arXiv's
official availability policy states that the final arXiv identifier and DOI are
assigned when the work is announced.  Therefore DOI creation is used as a
recovery lead and matched to the immediately preceding official announcement
slot (Sunday--Thursday, 20:00 US Eastern).  The scheduled announcement instant,
not a submission or registry-update timestamp, is assigned to the strict
Beijing ``[D-1 09:00, D 09:00)`` Daily window.

This receipt does not replace exact-v1 abs/HTML/PDF review or the exact-ID
official archive check.  A record that cannot be matched to an announcement
slot stays anomalous and must not be silently assigned to a Daily.
"""

from __future__ import annotations

from datetime import date, datetime, time, timedelta, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re
import statistics
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "papers/2026/03/_sources/datacite-arxiv-202603-created"
OUTPUT = ROOT / "papers/2026/03/_sources/march-2026-arxiv-announcement-recovery.json.gz"
POLICY_SNAPSHOT = ROOT / "papers/2026/03/_sources/official-arxiv-policy/availability.html"

EASTERN = ZoneInfo("America/New_York")
BEIJING = ZoneInfo("Asia/Shanghai")

CORE_DAILY = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD_DAILY = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}
WEEKLY_FILTERED = {"cs.HC", "cs.SY", "eess.SY", "cs.ET"}
TRIGGERED_BACKSTOP = {"math.OC", "cs.MM", "eess.IV"}
REGISTERED_CATEGORIES = CORE_DAILY | KEYWORD_DAILY | WEEKLY_FILTERED | TRIGGERED_BACKSTOP


def parse_dates(attributes: dict) -> dict[tuple[str, str], str]:
    result: dict[tuple[str, str], str] = {}
    for item in attributes.get("dates", []):
        value = item.get("date")
        if value:
            result[(item.get("dateType", ""), item.get("dateInformation", ""))] = value
    return result


def subject_codes(attributes: dict) -> list[str]:
    codes: set[str] = set()
    for item in attributes.get("subjects", []):
        if item.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([^()]+)\)\s*$", item.get("subject", ""))
        if match:
            codes.add(match.group(1))
    return sorted(codes)


def scheduled_slots(start: date, end: date) -> list[datetime]:
    slots: list[datetime] = []
    current = start
    while current <= end:
        # Python weekday: Monday=0 ... Sunday=6. arXiv announces Sun--Thu.
        if current.weekday() in {0, 1, 2, 3, 6}:
            slots.append(datetime.combine(current, time(20, 0), EASTERN))
        current += timedelta(days=1)
    return slots


SLOTS = scheduled_slots(date(2026, 2, 1), date(2026, 10, 1))


def match_announcement(doi_created: datetime) -> tuple[datetime | None, float | None]:
    preceding = [slot for slot in SLOTS if slot.astimezone(timezone.utc) <= doi_created]
    if not preceding:
        return None, None
    slot = preceding[-1]
    lag_hours = (doi_created - slot.astimezone(timezone.utc)).total_seconds() / 3600
    # DOI registration normally trails announcement by a few hours. A bounded
    # allowance catches processing variance without treating a later registry
    # maintenance event as the announcement.
    if lag_hours > 12:
        return None, lag_hours
    return slot, lag_hours


def owner_report_date(announcement: datetime) -> str:
    local = announcement.astimezone(BEIJING)
    cutoff = datetime.combine(local.date(), time(9, 0), BEIJING)
    # Half-open window: an event exactly at 09:00 belongs to the next Daily.
    owner = local.date() if local < cutoff else local.date() + timedelta(days=1)
    return owner.isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    records: list[dict] = []
    snapshot_files = sorted(SNAPSHOT.glob("doi-prefix-2603-*-page-01.json.gz"))
    if not snapshot_files:
        raise SystemExit(f"missing frozen snapshot: {SNAPSHOT}")
    if not POLICY_SNAPSHOT.exists():
        raise SystemExit(f"missing official arXiv policy snapshot: {POLICY_SNAPSHOT}")

    for path in snapshot_files:
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        for item in payload.get("data", []):
            attributes = item.get("attributes", {})
            doi = attributes.get("doi", "")
            if not doi.lower().startswith("10.48550/arxiv.2603."):
                continue
            categories = subject_codes(attributes)
            if not (set(categories) & REGISTERED_CATEGORIES):
                continue
            dates = parse_dates(attributes)
            created_text = attributes.get("created") or attributes.get("registered")
            if not created_text:
                created = None
                slot = None
                lag = None
            else:
                created = datetime.fromisoformat(created_text.replace("Z", "+00:00"))
                slot, lag = match_announcement(created)
            title_items = attributes.get("titles") or [{}]
            arxiv_id = re.sub(r"^10\.48550/arxiv\.", "", doi, flags=re.I)
            records.append({
                "arxiv_id": arxiv_id,
                "doi": doi,
                "title": title_items[0].get("title", ""),
                "categories": categories,
                "submitted_v1_utc": dates.get(("Submitted", "v1")),
                "registry_updated_v1_utc": dates.get(("Updated", "v1")),
                "doi_created_utc": created_text,
                "announcement_eastern": slot.isoformat() if slot else None,
                "announcement_beijing": slot.astimezone(BEIJING).isoformat() if slot else None,
                "doi_registration_lag_hours": round(lag, 6) if lag is not None else None,
                "owner_report_date": owner_report_date(slot) if slot else None,
                "status": "scheduled_match" if slot else "announcement_anomaly",
            })

    records.sort(key=lambda row: (row["owner_report_date"] or "9999", row["arxiv_id"]))
    identifiers = [row["arxiv_id"] for row in records]
    if len(identifiers) != len(set(identifiers)):
        raise SystemExit("duplicate arXiv identifiers in announcement recovery")
    by_report: dict[str, int] = {}
    anomaly_count = 0
    for row in records:
        if row["status"] != "scheduled_match":
            anomaly_count += 1
            continue
        owner = row["owner_report_date"]
        by_report[owner] = by_report.get(owner, 0) + 1

    lag_values = sorted(
        row["doi_registration_lag_hours"]
        for row in records
        if row["doi_registration_lag_hours"] is not None
    )
    outside_march: dict[str, int] = {}
    for row in records:
        owner = row["owner_report_date"]
        if owner and not owner.startswith("2026-03"):
            outside_march[owner] = outside_march.get(owner, 0) + 1
    manifest_path = SNAPSHOT / "manifest.json"
    if not manifest_path.exists():
        raise SystemExit(f"missing snapshot manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not manifest.get("complete"):
        raise SystemExit("DataCite created/registered snapshot is not complete")
    if anomaly_count:
        raise SystemExit(
            f"{anomaly_count} announcement ownership anomalies require manual resolution"
        )

    receipt = {
        "schema": "march-2026-arxiv-announcement-recovery-v2",
        "authority_boundary": (
            "DataCite DOI created is a recovery lead tied to arXiv's official rule that the final "
            "identifier and DOI are assigned on announcement. Daily ownership is derived from the "
            "official arXiv announcement schedule; exact-v1 withdrawal and exact-ID official "
            "archive presence remain separate required checks. Submitted:v1 and Updated:v1 do not "
            "own the Daily window."
        ),
        "official_schedule_url": "https://info.arxiv.org/help/availability.html#announcement-schedule",
        "official_schedule_snapshot": {
            "path": str(POLICY_SNAPSHOT.relative_to(ROOT)),
            "sha256": sha256(POLICY_SNAPSHOT),
            "asserted_claims": [
                "final arXiv identifier and DOI are assigned when the work is announced",
                "identifier month is the month of first announcement",
                "announcement slots are Sunday through Thursday at 20:00 US Eastern",
            ],
        },
        "official_month_archive_urls": [
            "https://arxiv.org/list/cs/2026-03",
            "https://arxiv.org/list/stat/2026-03",
            "https://arxiv.org/list/eess/2026-03",
        ],
        "window_contract": "Asia/Shanghai [D-1 09:00, D 09:00)",
        "snapshot": {
            "path": str(SNAPSHOT.relative_to(ROOT)),
            "manifest_path": str(manifest_path.relative_to(ROOT)),
            "manifest_sha256": sha256(manifest_path),
            "manifest_complete": manifest.get("complete"),
            "all_doi_record_count": manifest.get("record_count"),
            "files": len(snapshot_files),
            "sha256": {str(path.relative_to(ROOT)): sha256(path) for path in snapshot_files},
        },
        "registered_categories": sorted(REGISTERED_CATEGORIES),
        "record_count": len(records),
        "scheduled_match_count": len(records) - anomaly_count,
        "announcement_anomaly_count": anomaly_count,
        "unique_arxiv_identifier_count": len(set(identifiers)),
        "doi_creation_missing_count": sum(not row["doi_created_utc"] for row in records),
        "registration_lag_hours": {
            "minimum": min(lag_values),
            "median": statistics.median(lag_values),
            "p95": lag_values[int(0.95 * (len(lag_values) - 1))],
            "p99": lag_values[int(0.99 * (len(lag_values) - 1))],
            "maximum": max(lag_values),
            "matching_limit": 12,
        },
        "owner_report_counts": dict(sorted(by_report.items())),
        "outside_march_owner_counts": dict(sorted(outside_march.items())),
        "records": records,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(OUTPUT, "wt", encoding="utf-8") as handle:
        json.dump(receipt, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    print(json.dumps({
        "output": str(OUTPUT.relative_to(ROOT)),
        "records": len(records),
        "scheduled_matches": len(records) - anomaly_count,
        "anomalies": anomaly_count,
        "march_owner_counts": {k: v for k, v in by_report.items() if k.startswith("2026-03")},
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
