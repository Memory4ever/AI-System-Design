#!/usr/bin/env python3
"""Reconcile April/May historical Daily ownership against first-public metadata.

This script deliberately does not decide semantic relevance.  It preserves the
existing title+abstract decision when one exists and emits `review_pending` for
identities that the submission-window replay never saw.  That separation keeps
date recovery from silently becoming a new relevance classifier.
"""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
import gzip
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path("/Users/apple/Documents/Work/PycharmProject/AI-System-Design")
TARGET_MONTHS = ("04", "05")
DAILY_ROUTES = {
    "cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML",
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF",
    "cs.OS", "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}
DATACITE_DIRS = tuple(
    ROOT / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903/datacite-created"
    for month in TARGET_MONTHS
)
DATACITE_BOUNDARY_DIRS = tuple(
    ROOT / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903/boundary-created"
    for month in TARGET_MONTHS
)
DATACITE_CONTENT_DIRS = (
    ROOT / "papers/2026/02/_sources/datacite-arxiv-202602-created",
    ROOT / "papers/2026/03/_sources/datacite-arxiv-202603-created",
    ROOT / "papers/2026/04/_sources/datacite-arxiv-202603-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202604-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202605-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202606-v2",
)


def normalize_id(value: object) -> str:
    raw = str(value or "").strip().split(":")[-1]
    return re.sub(r"v\d+$", "", raw)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def ledger_rows(payload: object) -> list[dict]:
    if isinstance(payload, list):
        return [row for row in payload if isinstance(row, dict)]
    if isinstance(payload, dict):
        for key in ("identities", "rows", "items", "entries"):
            rows = payload.get(key)
            if isinstance(rows, list):
                return [row for row in rows if isinstance(row, dict)]
    return []


def pick_screening_ledger(packet: Path) -> Path | None:
    names = (
        "screening-ledger-final.json",
        "screening-ledger-independent-final.json",
        "screening-ledger-independent-reconciled.json",
        "screening-ledger-v2.1.json",
        "screening-ledger.json",
    )
    for name in names:
        path = packet / name
        if path.exists():
            return path
    return None


def load_existing_screening() -> tuple[dict[str, dict], list[dict]]:
    decisions: dict[str, dict] = {}
    provenance: list[dict] = []
    for month in TARGET_MONTHS:
        for packet in sorted((ROOT / f"papers/2026/{month}/_sources").glob("daily-2026*")):
            ledger = pick_screening_ledger(packet)
            if ledger is None:
                continue
            rows = ledger_rows(json.loads(ledger.read_text(encoding="utf-8")))
            provenance.append({"path": str(ledger.relative_to(ROOT)), "sha256": sha256(ledger), "rows": len(rows)})
            for row in rows:
                arxiv_id = normalize_id(
                    row.get("arxiv_id") or row.get("identity") or row.get("source_family_key") or row.get("id")
                )
                if not re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id):
                    continue
                candidate = str(row.get("screening_status") or row.get("screening_decision") or row.get("decision") or "").lower()
                is_retained = candidate in {"retain", "retained", "candidate", "selected"} or str(row.get("candidate_state", "")).lower() == "retained"
                quality = (2 if is_retained else 1, len(str(row.get("screening_reason") or "")))
                prior = decisions.get(arxiv_id)
                if prior is None or quality > tuple(prior["_quality"]):
                    copy = dict(row)
                    copy["_quality"] = quality
                    copy["_source_ledger"] = str(ledger.relative_to(ROOT))
                    decisions[arxiv_id] = copy
    return decisions, provenance


def load_datacite() -> tuple[dict[str, dict], list[dict]]:
    records: dict[str, dict] = {}
    provenance: list[dict] = []
    # The earlier prefix snapshots contain title, abstract, subjects and exact
    # version metadata, but intentionally selected fields and therefore omit
    # DataCite's immutable top-level ``created`` field.
    for directory in DATACITE_CONTENT_DIRS:
        if not directory.exists():
            continue
        count = 0
        for path in sorted(directory.glob("*.json.gz")):
            try:
                with gzip.open(path, "rt", encoding="utf-8") as handle:
                    data = json.load(handle).get("data", [])
            except (OSError, json.JSONDecodeError):
                continue
            for item in data:
                attributes = item.get("attributes", {})
                arxiv_id = normalize_id(str(attributes.get("doi", "")).lower().split("arxiv.")[-1])
                if re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id):
                    records[arxiv_id] = attributes
                    count += 1
        provenance.append({"directory": str(directory.relative_to(ROOT)), "role": "content_and_version_metadata", "records_read": count})
    # Daily ``created`` snapshots own date routing.  Merge, do not replace,
    # because most pages intentionally requested only doi/created/updated.
    for directory in DATACITE_DIRS + DATACITE_BOUNDARY_DIRS:
        if not directory.exists():
            continue
        count = 0
        for path in sorted(directory.glob("*.json")):
            try:
                with path.open("r", encoding="utf-8") as handle:
                    data = json.load(handle).get("data", [])
            except (OSError, json.JSONDecodeError):
                continue
            for item in data:
                attributes = item.get("attributes", {})
                arxiv_id = normalize_id(str(attributes.get("doi", "")).lower().split("arxiv.")[-1])
                if re.fullmatch(r"\d{4}\.\d{4,5}", arxiv_id):
                    records.setdefault(arxiv_id, {}).update(attributes)
                    count += 1
        provenance.append({"directory": str(directory.relative_to(ROOT)), "role": "initial_created_owner_proxy", "records_read": count})
    return records, provenance


def v1_owner(record: dict) -> tuple[str | None, str | None, str | None, str | None]:
    """Return first-registration owner proxy and version provenance.

    DataCite ``created`` is immutable initial DOI registration metadata.  Its
    UTC calendar date is used only as an arXiv first-public *day proxy*; the
    timestamp itself can lag the 09:00 Asia/Shanghai reporting boundary and is
    therefore not claimed as the publication instant.  DataCite ``updated``
    and arXiv/OAI datestamps can move on revision and never own the Daily.
    """
    created = record.get("created")
    submitted = updated = None
    for item in record.get("dates", []):
        if item.get("dateInformation") != "v1":
            continue
        if item.get("dateType") == "Submitted":
            submitted = item.get("date")
        elif item.get("dateType") == "Updated":
            updated = item.get("date")
    owner_day = created[:10] if isinstance(created, str) and len(created) >= 10 else None
    return owner_day, created, updated, submitted


def categories(record: dict) -> list[str]:
    output: list[str] = []
    for item in record.get("subjects", []):
        if item.get("subjectScheme") != "arXiv":
            continue
        match = re.search(r"\(([^()]+)\)$", str(item.get("subject", "")))
        if match:
            output.append(match.group(1))
    return output


def title(record: dict) -> str:
    titles = record.get("titles") or []
    return str(titles[0].get("title", "")).strip() if titles else ""


def abstract(record: dict) -> str:
    return " ".join(
        str(item.get("description", "")).strip()
        for item in record.get("descriptions", [])
        if item.get("descriptionType") == "Abstract"
    ).strip()


def load_oai_index() -> tuple[dict[str, set[str]], list[dict]]:
    by_id: dict[str, set[str]] = defaultdict(set)
    provenance: list[dict] = []
    for month in TARGET_MONTHS:
        directory = ROOT / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903/oai-list-identifiers"
        for path in sorted(directory.glob("*.xml")):
            day = path.name[:10]
            try:
                tree = ET.parse(path)
            except ET.ParseError:
                continue
            count = 0
            for node in tree.getroot().iter():
                if node.tag.endswith("identifier") and node.text and node.text.startswith("oai:arXiv.org:"):
                    by_id[normalize_id(node.text)] .add(day)
                    count += 1
            provenance.append({"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "identifiers": count})
    return by_id, provenance


def parse_candidate_rows() -> list[dict]:
    rows: list[dict] = []
    for month in TARGET_MONTHS:
        for readme in sorted((ROOT / f"papers/2026/{month}").glob("[0-3][0-9]/README.md")):
            report_day = f"2026-{month}-{readme.parent.name}"
            text = readme.read_text(encoding="utf-8")
            section = text.split("## 3. Review Completion Receipt", 1)[0]
            for line in section.splitlines():
                if not line.startswith("| SF-"):
                    continue
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if len(cells) < 22:
                    continue
                primary = cells[1]
                match = re.search(r"arXiv:(\d{4}\.\d{4,5})v1", primary)
                if not match:
                    continue
                rows.append({
                    "source_family_id": cells[0],
                    "arxiv_id": match.group(1),
                    "source_report": str(readme.relative_to(ROOT)),
                    "source_report_day": report_day,
                    "candidate_row": cells,
                })
    return rows


def main() -> None:
    generated_at = datetime.now(timezone.utc).isoformat()
    screening, screening_provenance = load_existing_screening()
    datacite, datacite_provenance = load_datacite()
    oai, oai_provenance = load_oai_index()
    candidate_rows = parse_candidate_rows()

    candidates_by_owner: dict[str, list[dict]] = defaultdict(list)
    unknown_candidates: list[dict] = []
    seen_candidate_family: set[tuple[str, str]] = set()
    for item in candidate_rows:
        record = datacite.get(item["arxiv_id"])
        owner_day, created, v1_updated, submitted = v1_owner(record or {})
        result = dict(item)
        result.update({
            "recovered_owner_day": owner_day,
            "datacite_initial_created_timestamp": created,
            "datacite_current_updated_timestamp_revision_only": (record or {}).get("updated"),
            "v1_updated_timestamp_revision_metadata_only": v1_updated,
            "v1_submission_timestamp_provenance_only": submitted,
            "owner_receipt_route": (
                "official_arxiv_oai_direct" if owner_day and owner_day in oai.get(item["arxiv_id"], set())
                else "datacite_initial_created_owner_proxy"
            ),
            "oai_current_datestamps": sorted(oai.get(item["arxiv_id"], set())),
        })
        identifier_month = f"20{item['arxiv_id'][:2]}-{item['arxiv_id'][2:4]}"
        if not owner_day and identifier_month > "2026-05":
            result["owner_receipt_route"] = "excluded_by_future_arxiv_identifier_month"
            result["owner_lower_bound"] = identifier_month
            result["recovered_owner_day"] = f">={identifier_month}-01"
            unknown_candidates.append(result)
        elif owner_day:
            key = (owner_day, item["source_family_id"])
            if key not in seen_candidate_family:
                candidates_by_owner[owner_day].append(result)
                seen_candidate_family.add(key)
        else:
            unknown_candidates.append(result)

    raw_by_owner: dict[str, list[dict]] = defaultdict(list)
    for arxiv_id, record in datacite.items():
        owner_day, created, v1_updated, submitted = v1_owner(record)
        if not owner_day or not ("2026-04-01" <= owner_day <= "2026-05-31"):
            continue
        cats = categories(record)
        if not DAILY_ROUTES.intersection(cats):
            continue
        prior = screening.get(arxiv_id)
        prior_status = str((prior or {}).get("screening_status") or (prior or {}).get("screening_decision") or (prior or {}).get("decision") or "").lower()
        retained = prior_status in {"retain", "retained", "candidate", "selected"} or str((prior or {}).get("candidate_state", "")).lower() == "retained"
        raw_by_owner[owner_day].append({
            "arxiv_id": arxiv_id,
            "source_family_id": f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}",
            "title": title(record),
            "abstract": abstract(record),
            "categories": cats,
            "datacite_initial_created_timestamp": created,
            "datacite_current_updated_timestamp_revision_only": record.get("updated"),
            "v1_updated_timestamp_revision_metadata_only": v1_updated,
            "v1_submission_timestamp_provenance_only": submitted,
            "owner_receipt_route": (
                "official_arxiv_oai_direct" if owner_day in oai.get(arxiv_id, set())
                else "datacite_initial_created_owner_proxy"
            ),
            "oai_current_datestamps": sorted(oai.get(arxiv_id, set())),
            "screening_status": "retained" if retained else ("closure" if prior_status in {"reject", "rejected", "closure", "closed"} else (prior_status or "review_pending")),
            "screening_reason": (prior or {}).get("screening_reason") or (prior or {}).get("reason"),
            "prior_screening_ledger": (prior or {}).get("_source_ledger"),
            "review_status": (prior or {}).get("review_status"),
            "access_status": (prior or {}).get("access_status"),
            "integration_disposition": (prior or {}).get("integration_disposition"),
        })

    for month in TARGET_MONTHS:
        month_prefix = f"2026-{month}"
        month_root = ROOT / f"papers/2026/{month}/_sources/arxiv-owner-replay-20260903"
        summary_days: list[dict] = []
        for day_number in range(1, 32):
            day = f"{month_prefix}-{day_number:02d}"
            report = ROOT / f"papers/2026/{month}/{day_number:02d}/README.md"
            if not report.exists():
                continue
            raw_rows = sorted(raw_by_owner.get(day, []), key=lambda row: row["arxiv_id"])
            candidate_rows_for_day = sorted(candidates_by_owner.get(day, []), key=lambda row: row["source_family_id"])
            pending = [row for row in raw_rows if row["screening_status"] == "review_pending"]
            direct = sum(row["owner_receipt_route"] == "official_arxiv_oai_direct" for row in raw_rows)
            recovered = len(raw_rows) - direct
            receipt = {
                "schema": "arxiv-first-public-owner-receipt-v1",
                "report_date": day,
                "generated_at": generated_at,
                "date_semantics": {
                    "owner": "DataCite initial created UTC calendar date as first-public day proxy, corroborated by arXiv identity/month and official announcement cadence",
                    "submission_timestamp": "provenance_only_not_owner",
                    "direct_route": "DataCite initial created day corroborated by same-day official arXiv OAI datestamp",
                    "recovery_route": "DataCite initial created day; DataCite updated, v1 Updated, and OAI current datestamp are revision metadata only",
                    "timestamp_boundary": "created timestamp is provenance, not a claim that DOI ingestion occurred before the 09:00 Asia/Shanghai cutoff",
                },
                "raw_identity_count": len(raw_rows),
                "official_oai_direct_count": direct,
                "revision_recovery_count": recovered,
                "candidate_count_reconciled_from_existing_reports": len(candidate_rows_for_day),
                "semantic_review_pending_count": len(pending),
                "identities": raw_rows,
                "candidate_reconciliation": candidate_rows_for_day,
            }
            day_dir = month_root / day.replace("-", "")
            day_dir.mkdir(parents=True, exist_ok=True)
            (day_dir / "arxiv-owner-receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            summary_days.append({
                "report_date": day,
                "raw_identities": len(raw_rows),
                "owner_direct": direct,
                "owner_recovered": recovered,
                "candidate_count": len(candidate_rows_for_day),
                "semantic_review_pending": len(pending),
                "receipt": str((day_dir / "arxiv-owner-receipt.json").relative_to(ROOT)),
            })

        original_month_rows = [row for row in candidate_rows if row["source_report_day"].startswith(month_prefix)]
        moved_inside = 0
        moved_outside = 0
        unchanged = 0
        for row in original_month_rows:
            owner_day, _, _, _ = v1_owner(datacite.get(row["arxiv_id"], {}))
            if owner_day == row["source_report_day"]:
                unchanged += 1
            elif owner_day and owner_day.startswith(month_prefix):
                moved_inside += 1
            elif owner_day:
                moved_outside += 1
            else:
                identifier_month = f"20{row['arxiv_id'][:2]}-{row['arxiv_id'][2:4]}"
                if identifier_month > month_prefix:
                    moved_outside += 1
        summary = {
            "schema": "historical-daily-owner-reconciliation-v1",
            "month": month_prefix,
            "generated_at": generated_at,
            "historical_daily_independent_of_weekly": True,
            "status": "semantic_screening_pending" if any(day["semantic_review_pending"] for day in summary_days) else "owner_reconciliation_closed",
            "original_candidate_rows": len(original_month_rows),
            "candidate_owner_unchanged": unchanged,
            "candidate_owner_moved_within_month": moved_inside,
            "candidate_owner_moved_outside_month": moved_outside,
            "candidate_owner_unknown": sum(
                1 for row in unknown_candidates
                if row["source_report_day"].startswith(month_prefix)
                and row.get("owner_receipt_route") != "excluded_by_future_arxiv_identifier_month"
            ),
            "raw_identity_total": sum(day["raw_identities"] for day in summary_days),
            "semantic_review_pending_total": sum(day["semantic_review_pending"] for day in summary_days),
            "days": summary_days,
            "unknown_candidates": [row for row in unknown_candidates if row["source_report_day"].startswith(month_prefix)],
            "source_provenance": {
                "oai": [row for row in oai_provenance if f"papers/2026/{month}/" in row["path"]],
                "datacite": datacite_provenance,
                "prior_screening": [row for row in screening_provenance if f"papers/2026/{month}/" in row["path"]],
            },
        }
        (month_root / "month-reconciliation.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({key: value for key, value in summary.items() if key not in {"days", "unknown_candidates", "source_provenance"}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
