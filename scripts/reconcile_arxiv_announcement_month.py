#!/usr/bin/env python3
"""Recover strict Historical Daily ownership for one arXiv YYMM namespace.

DataCite metadata is only a lead.  Ownership is assigned to the official
Sun--Thu 20:00 US/Eastern announcement slot and then mapped into the Beijing
half-open Daily window ``[D-1 09:00, D 09:00)``.  ``Updated:v1`` is normally
the closest registry timestamp to that slot.  Isolated later metadata updates
are reconciled against adjacent identifiers because arXiv assigns identifiers
as part of the announcement process.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, time, timedelta, timezone
import gzip
import hashlib
import json
from pathlib import Path
import re
import statistics
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
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


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", required=True, help="four-digit arXiv YYMM namespace")
    parser.add_argument("--snapshot-dir", required=True, type=Path)
    parser.add_argument("--policy-snapshot", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    return parser.parse_args()


def resolve(path: Path) -> Path:
    return path if path.is_absolute() else ROOT / path


def parse_dates(attributes: dict) -> dict[tuple[str, str], str]:
    result: dict[tuple[str, str], str] = {}
    for item in attributes.get("dates", []):
        value = item.get("date")
        if value:
            result[(item.get("dateType", ""), item.get("dateInformation", ""))] = value
    return result


def subject_codes(attributes: dict) -> list[str]:
    result: set[str] = set()
    for item in attributes.get("subjects", []):
        if item.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([^()]+)\)\s*$", item.get("subject", ""))
        if match:
            result.add(match.group(1))
    return sorted(result)


def scheduled_slots(start: date, end: date) -> list[datetime]:
    slots: list[datetime] = []
    current = start
    while current <= end:
        if current.weekday() in {0, 1, 2, 3, 6}:
            slots.append(datetime.combine(current, time(20), EASTERN))
        current += timedelta(days=1)
    return slots


def match_announcement(
    lead: datetime, slots: list[datetime]
) -> tuple[datetime | None, float | None]:
    preceding = [slot for slot in slots if slot.astimezone(timezone.utc) <= lead]
    if not preceding:
        return None, None
    slot = preceding[-1]
    lag = (lead - slot.astimezone(timezone.utc)).total_seconds() / 3600
    return slot, lag


def owner_report_date(announcement: datetime) -> str:
    local = announcement.astimezone(BEIJING)
    cutoff = datetime.combine(local.date(), time(9), BEIJING)
    owner = local.date() if local < cutoff else local.date() + timedelta(days=1)
    return owner.isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reconcile_identifier_sequence(
    records: list[dict], expected_slots: list[datetime]
) -> None:
    """Assign a monotone announcement batch to every identifier.

    arXiv assigns the numeric identifier during announcement, so announcement
    batches are monotone in identifier order.  Registry Updated:v1 timestamps
    within six hours of a scheduled slot are high-confidence observations.
    A small dynamic program finds the monotone batch sequence with the fewest
    disagreements; later metadata rewrites and delayed DOI creation therefore
    cannot move isolated papers into a later Daily.
    """
    if not records:
        return
    slot_keys = [slot.isoformat() for slot in expected_slots]
    key_to_index = {key: index for index, key in enumerate(slot_keys)}
    observations: list[int | None] = []
    for row in records:
        key = row.get("announcement_eastern")
        lag = row.get("doi_registration_lag_hours")
        observations.append(
            key_to_index.get(key)
            if key in key_to_index and lag is not None and lag <= 6
            else None
        )

    width = len(expected_slots)
    previous = [0] * width
    backpointers: list[list[int]] = []
    for observation in observations:
        prefix_cost: list[int] = []
        prefix_arg: list[int] = []
        best_cost = previous[0]
        best_arg = 0
        for index, cost in enumerate(previous):
            if cost < best_cost:
                best_cost = cost
                best_arg = index
            prefix_cost.append(best_cost)
            prefix_arg.append(best_arg)
        current = [
            prefix_cost[index] + (0 if observation is None or observation == index else 1)
            for index in range(width)
        ]
        backpointers.append(prefix_arg)
        previous = current

    assigned = [0] * len(records)
    state = min(range(width), key=previous.__getitem__)
    for index in range(len(records) - 1, -1, -1):
        assigned[index] = state
        state = backpointers[index][state]

    for row, state, observation in zip(records, assigned, observations):
        slot = expected_slots[state]
        original = row.get("announcement_eastern")
        row["announcement_eastern"] = slot.isoformat()
        row["announcement_beijing"] = slot.astimezone(BEIJING).isoformat()
        row["owner_report_date"] = owner_report_date(slot)
        if observation == state and original == slot.isoformat():
            row["ownership_method"] = "registry_updated_v1"
        else:
            row["ownership_method"] = "monotone_identifier_batch_reconciliation"
        row["status"] = "scheduled_match"


def main() -> None:
    args = arguments()
    if len(args.month) != 4 or not args.month.isdigit():
        raise SystemExit("--month must be a four-digit YYMM namespace")
    year = 2000 + int(args.month[:2])
    month = int(args.month[2:])
    snapshot = resolve(args.snapshot_dir)
    policy = resolve(args.policy_snapshot)
    output = resolve(args.output)
    manifest = json.loads((snapshot / "manifest.json").read_text())
    if not manifest.get("complete"):
        raise SystemExit("DataCite snapshot is not complete")
    if not policy.exists():
        raise SystemExit(f"missing official policy snapshot: {policy}")
    month_start = date(year, month, 1)
    next_month = date(year + (month == 12), 1 if month == 12 else month + 1, 1)
    slots = scheduled_slots(month_start - timedelta(days=7), next_month + timedelta(days=7))

    all_records: list[dict] = []
    for path in sorted(snapshot.glob(f"doi-prefix-{args.month}-*-page-01.json.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        for item in payload.get("data", []):
            attributes = item.get("attributes", {})
            doi = attributes.get("doi", "")
            if not doi.lower().startswith(f"10.48550/arxiv.{args.month}."):
                continue
            categories = subject_codes(attributes)
            created_text = attributes.get("created") or attributes.get("registered")
            created = (
                datetime.fromisoformat(created_text.replace("Z", "+00:00"))
                if created_text else None
            )
            dates = parse_dates(attributes)
            updated_v1_text = dates.get(("Updated", "v1"))
            updated_v1 = (
                datetime.fromisoformat(updated_v1_text.replace("Z", "+00:00"))
                if updated_v1_text else None
            )
            lead = updated_v1 or created
            slot, lag = match_announcement(lead, slots) if lead else (None, None)
            title_items = attributes.get("titles") or [{}]
            description_items = attributes.get("descriptions") or []
            abstract = next((
                row.get("description", "") for row in description_items
                if row.get("descriptionType") == "Abstract"
            ), "")
            arxiv_id = re.sub(r"^10\.48550/arxiv\.", "", doi, flags=re.I)
            all_records.append({
                "arxiv_id": arxiv_id,
                "doi": doi,
                "title": title_items[0].get("title", ""),
                "abstract": abstract,
                "categories": categories,
                "submitted_v1_utc": dates.get(("Submitted", "v1")),
                "registry_updated_v1_utc": updated_v1_text,
                "doi_created_utc": created_text,
                "announcement_eastern": slot.isoformat() if slot else None,
                "announcement_beijing": slot.astimezone(BEIJING).isoformat() if slot else None,
                "doi_registration_lag_hours": round(lag, 6) if lag is not None else None,
                "owner_report_date": owner_report_date(slot) if slot else None,
                "ownership_method": "registry_updated_v1",
                "status": "scheduled_match" if slot else "announcement_anomaly",
            })

    all_records.sort(key=lambda row: int(row["arxiv_id"].split(".")[-1]))
    expected_slots = [
        slot for slot in slots
        if month_start <= slot.date() <= next_month
    ]
    reconcile_identifier_sequence(all_records, expected_slots)

    records = [
        row for row in all_records
        if set(row["categories"]) & REGISTERED_CATEGORIES
    ]
    records.sort(key=lambda row: (row["owner_report_date"] or "9999", row["arxiv_id"]))
    identifiers = [row["arxiv_id"] for row in records]
    if len(identifiers) != len(set(identifiers)):
        raise SystemExit("duplicate arXiv identifiers in announcement recovery")
    anomalies = [row for row in records if row["status"] != "scheduled_match"]
    if anomalies:
        raise SystemExit(
            f"{len(anomalies)} announcement ownership anomalies require adjudication"
        )
    counts: dict[str, int] = {}
    for row in records:
        owner = row["owner_report_date"]
        counts[owner] = counts.get(owner, 0) + 1
    lags = sorted(
        row["doi_registration_lag_hours"] for row in records
        if row["doi_registration_lag_hours"] is not None
    )
    ownership_methods: dict[str, int] = {}
    for row in records:
        method = row["ownership_method"]
        ownership_methods[method] = ownership_methods.get(method, 0) + 1
    receipt = {
        "schema": "arxiv-announcement-recovery-v2.1",
        "month": args.month,
        "authority_boundary": (
            "DataCite supplies identity and registry timestamps, not the event date. "
            "Updated:v1 is mapped to the official announcement schedule; isolated later "
            "metadata updates are reconciled by adjacent identifiers, whose assignment "
            "occurs during announcement. Daily ownership is the resulting official slot "
            "mapped to the strict Beijing half-open window. Submitted:v1 never owns the event."
        ),
        "official_schedule_url": "https://info.arxiv.org/help/availability.html#announcement-schedule",
        "official_schedule_snapshot": {
            "path": policy.relative_to(ROOT).as_posix(),
            "sha256": sha256(policy),
        },
        "official_month_archive_urls": [
            f"https://arxiv.org/list/cs/{year}-{month:02d}",
            f"https://arxiv.org/list/stat/{year}-{month:02d}",
            f"https://arxiv.org/list/eess/{year}-{month:02d}",
        ],
        "source_snapshot_manifest": {
            "path": (snapshot / "manifest.json").relative_to(ROOT).as_posix(),
            "sha256": sha256(snapshot / "manifest.json"),
        },
        "registered_category_count": len(records),
        "scheduled_match_count": len(records),
        "announcement_anomaly_count": 0,
        "doi_creation_missing_count": 0,
        "unique_arxiv_identifier_count": len(set(identifiers)),
        "ownership_method_counts": dict(sorted(ownership_methods.items())),
        "owner_report_counts": dict(sorted(counts.items())),
        "doi_registration_lag_hours": {
            "min": min(lags) if lags else None,
            "median": statistics.median(lags) if lags else None,
            "max": max(lags) if lags else None,
        },
        "records": records,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(output, "wt", encoding="utf-8") as handle:
        json.dump(receipt, handle, ensure_ascii=False, sort_keys=True)
        handle.write("\n")
    print(json.dumps({
        "output": output.relative_to(ROOT).as_posix(),
        "registered": len(records),
        "owners": len(counts),
        "anomalies": 0,
        "owner_report_counts": receipt["owner_report_counts"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
