#!/usr/bin/env python3
"""Recover arXiv announcement-owner evidence for June/July candidate families."""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, time as wall_time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[5]
OUT = Path(__file__).resolve().parent / "owner-recovery"
ATOM = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
EASTERN = ZoneInfo("America/New_York")
SHANGHAI = ZoneInfo("Asia/Shanghai")
USER_AGENT = "AI-System-Design-research-audit/2.1 (contact: local-research-workflow)"


def table_rows(text: str, marker: str) -> list[list[str]]:
    match = re.search(
        rf"<!-- {re.escape(marker)} -->\n(.*?)(?=\n(?:<!--|##|###)|\Z)", text, re.S
    )
    if not match:
        return []
    rows: list[list[str]] = []
    for line in match.group(1).splitlines():
        if not line.startswith("|") or re.match(r"^\|\s*:?-+", line):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if cells and cells[0] != "Source Family ID":
            rows.append(cells)
    return rows


def candidate_rows() -> list[dict]:
    rows: list[dict] = []
    for month in ("06", "07"):
        for report in sorted((ROOT / "papers" / "2026" / month).glob("[0-9][0-9]/README.md")):
            for cells in table_rows(
                report.read_text(encoding="utf-8"), "validator:candidate-ledger-v2.1"
            ):
                if len(cells) < 22 or not cells[1].startswith("arXiv:"):
                    continue
                arxiv_id = cells[1].removeprefix("arXiv:").removesuffix("v1")
                rows.append(
                    {
                        "report_date": f"2026-{month}-{report.parent.name}",
                        "report": str(report.relative_to(ROOT)),
                        "source_family_id": cells[0],
                        "arxiv_id": arxiv_id,
                        "primary_identifier": cells[1],
                        "prior_first_public_date": cells[4],
                        "prior_state": cells[10],
                        "prior_review_status": cells[11],
                        "prior_books_disposition": cells[19],
                    }
                )
    return rows


def fetch(url: str, attempts: int = 4) -> bytes:
    error: Exception | None = None
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=90) as response:
                return response.read()
        except Exception as exc:  # network recovery records the final concrete failure
            error = exc
            time.sleep(2**attempt)
    raise RuntimeError(f"failed after {attempts} attempts: {url}: {error}")


def parse_atom(payload: bytes) -> dict[str, dict]:
    root = ET.fromstring(payload)
    found: dict[str, dict] = {}
    for entry in root.findall("a:entry", ATOM):
        latest_id = (entry.findtext("a:id", default="", namespaces=ATOM)).rsplit("/", 1)[-1]
        arxiv_id = re.sub(r"v\d+$", "", latest_id)
        if not arxiv_id:
            continue
        found[arxiv_id] = {
            "published": entry.findtext("a:published", default="", namespaces=ATOM),
            "updated": entry.findtext("a:updated", default="", namespaces=ATOM),
            "title": " ".join(entry.findtext("a:title", default="", namespaces=ATOM).split()),
            "summary": " ".join(entry.findtext("a:summary", default="", namespaces=ATOM).split()),
            "comment": entry.findtext("x:comment", default="", namespaces=ATOM),
            "primary_category": (
                entry.find("x:primary_category", ATOM).attrib.get("term", "")
                if entry.find("x:primary_category", ATOM) is not None
                else ""
            ),
            "categories": [node.attrib.get("term", "") for node in entry.findall("a:category", ATOM)],
            "latest_version": latest_id,
        }
    return found


def fetch_datacite_created(ids: list[str]) -> tuple[dict[str, dict], list[dict]]:
    """Fetch the immutable DOI-registration timestamp in bounded exact-ID batches."""
    found: dict[str, dict] = {}
    failures: list[dict] = []
    for index in range(0, len(ids), 50):
        batch = ids[index : index + 50]
        query_value = "identifiers.identifier:(" + " OR ".join(batch) + ")"
        query = urllib.parse.urlencode(
            {
                "query": query_value,
                "page[size]": len(batch),
                "fields[dois]": "doi,created,registered,dates",
            }
        )
        url = f"https://api.datacite.org/dois?{query}"
        path = OUT / f"candidate-datacite-{index // 50 + 1:03d}.json.gz"
        try:
            payload = gzip.decompress(path.read_bytes()) if path.exists() else fetch(url)
            parsed = json.loads(payload)
            for entry in parsed.get("data", []):
                attributes = entry.get("attributes", {})
                doi = attributes.get("doi", "")
                match = re.search(r"arxiv\.(\d{4}\.\d{4,5})$", doi, re.I)
                if not match:
                    continue
                found[match.group(1)] = {
                    "datacite_doi": doi,
                    "datacite_created": attributes.get("created", ""),
                    "datacite_registered": attributes.get("registered", ""),
                }
            if not path.exists():
                path.write_bytes(gzip.compress(payload, mtime=0))
        except Exception as exc:
            failures.append({"batch": index // 50 + 1, "ids": batch, "error": str(exc)})
        time.sleep(0.25)
    return found, failures


def scheduled_announcement(submitted: datetime) -> datetime:
    """Map a v1 submission timestamp to the normal arXiv 20:00 ET announcement."""
    local = submitted.astimezone(EASTERN)
    weekday = local.weekday()  # Monday=0
    after_deadline = local.timetz().replace(tzinfo=None) > wall_time(14, 0)
    if weekday == 0:
        add = 1 if after_deadline else 0
    elif weekday == 1:
        add = 1 if after_deadline else 0
    elif weekday == 2:
        add = 1 if after_deadline else 0
    elif weekday == 3:
        add = 3 if after_deadline else 0
    elif weekday == 4:
        add = 3 if after_deadline else 2
    elif weekday == 5:
        add = 2
    else:
        add = 1
    announce_date = local.date() + timedelta(days=add)
    return datetime.combine(announce_date, wall_time(20, 0), EASTERN)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    rows = candidate_rows()
    ids = sorted({row["arxiv_id"] for row in rows})

    availability_url = "https://info.arxiv.org/help/availability.html"
    availability = fetch(availability_url)
    (OUT / "arxiv-availability.html.gz").write_bytes(gzip.compress(availability, mtime=0))

    metadata: dict[str, dict] = {}
    failures: list[dict] = []
    for index in range(0, len(ids), 100):
        batch = ids[index : index + 100]
        query = urllib.parse.urlencode({"id_list": ",".join(batch), "max_results": len(batch)})
        url = f"https://export.arxiv.org/api/query?{query}"
        path = OUT / f"candidate-atom-{index // 100 + 1:03d}.xml.gz"
        try:
            payload = gzip.decompress(path.read_bytes()) if path.exists() else fetch(url)
            metadata.update(parse_atom(payload))
            if not path.exists():
                path.write_bytes(gzip.compress(payload, mtime=0))
        except Exception as exc:
            failures.append({"batch": index // 100 + 1, "ids": batch, "error": str(exc)})
        time.sleep(1)

    datacite, datacite_failures = fetch_datacite_created(ids)

    reconciled: list[dict] = []
    for row in rows:
        item = dict(row)
        meta = metadata.get(row["arxiv_id"])
        if not meta or not meta["published"]:
            item.update(
                {
                    "atom_status": "missing",
                    "scheduled_announcement_et": "",
                    "inferred_first_public_asia_shanghai": "",
                    "inferred_owner_report_date": "",
                    "identifier_month_matches_inference": "",
                    "reconciliation": "exact_metadata_blocked",
                    "withdrawn_signal": "unknown",
                }
            )
            reconciled.append(item)
            continue
        submitted = datetime.fromisoformat(meta["published"].replace("Z", "+00:00"))
        announced = scheduled_announcement(submitted)
        public_cn = announced.astimezone(SHANGHAI)
        schedule_owner_date = public_cn.date().isoformat()
        doi_meta = datacite.get(row["arxiv_id"], {})
        created_raw = doi_meta.get("datacite_created", "")
        datacite_owner_date = ""
        datacite_created_et_month = ""
        if created_raw:
            created = datetime.fromisoformat(created_raw.replace("Z", "+00:00"))
            datacite_owner_date = created.astimezone(SHANGHAI).date().isoformat()
            datacite_created_et_month = created.astimezone(EASTERN).strftime("%y%m")
        owner_date = datacite_owner_date or schedule_owner_date
        id_month = row["arxiv_id"].split(".", 1)[0]
        identifier_month_matches_owner = id_month == datacite_created_et_month
        text = " ".join((meta["title"], meta["summary"], meta["comment"] or "")).lower()
        withdrawn_keyword = "withdrawn" in text
        if not datacite_owner_date:
            action = "datacite_created_blocked"
        elif not identifier_month_matches_owner:
            action = "identifier_month_conflict_ambiguous"
        elif owner_date == row["report_date"]:
            action = "owner_confirmed_by_datacite"
        else:
            action = "owner_move_required"
        item.update(meta)
        item.update(doi_meta)
        item.update(
            {
                "atom_status": "retrieved",
                "scheduled_announcement_et": announced.isoformat(),
                "schedule_first_public_asia_shanghai": public_cn.isoformat(),
                "schedule_owner_report_date": schedule_owner_date,
                "datacite_owner_report_date": datacite_owner_date,
                "datacite_created_et_month": datacite_created_et_month,
                "resolved_owner_report_date": owner_date,
                "schedule_matches_datacite_owner": (
                    "yes" if schedule_owner_date == datacite_owner_date else "no"
                ),
                "identifier_month_matches_owner": "yes" if identifier_month_matches_owner else "no",
                "reconciliation": action,
                "withdrawn_keyword_signal": "yes" if withdrawn_keyword else "no",
            }
        )
        reconciled.append(item)

    fields = [
        "report_date", "report", "source_family_id", "arxiv_id", "primary_identifier",
        "prior_first_public_date", "published", "updated", "primary_category", "latest_version",
        "scheduled_announcement_et", "schedule_first_public_asia_shanghai",
        "schedule_owner_report_date", "datacite_doi", "datacite_created", "datacite_registered",
        "datacite_owner_report_date", "datacite_created_et_month", "resolved_owner_report_date",
        "schedule_matches_datacite_owner",
        "identifier_month_matches_owner", "reconciliation", "withdrawn_keyword_signal",
        "prior_state", "prior_review_status", "prior_books_disposition", "title",
    ]
    with (OUT / "owner-reconciliation.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(reconciled)

    counts: dict[str, int] = {}
    for item in reconciled:
        key = item["reconciliation"]
        counts[key] = counts.get(key, 0) + 1
    summary = {
        "schema": "arxiv-announcement-owner-recovery-v1",
        "generated_at": datetime.now(SHANGHAI).isoformat(),
        "candidate_rows": len(rows),
        "unique_arxiv_ids": len(ids),
        "atom_entries_retrieved": len(metadata),
        "failed_batches": failures,
        "datacite_entries_retrieved": len(datacite),
        "datacite_failed_batches": datacite_failures,
        "reconciliation_counts": counts,
        "withdrawn_keyword_signal_count": sum(
            item["withdrawn_keyword_signal"] == "yes" for item in reconciled
        ),
        "withdrawn_exactly_confirmed": ["2606.24369"],
        "official_contract": {
            "availability_url": availability_url,
            "availability_sha256": hashlib.sha256(availability).hexdigest(),
            "facts": [
                "arXiv identifier is assigned when work is announced",
                "identifier month is the month of first announcement",
                "normal announcement schedule uses 14:00 ET deadlines and 20:00 ET availability",
                "quality assurance can delay announcement; schedule-derived owner is an inference",
                "DataCite DOI created is an independent first-registration timestamp, not a revision timestamp",
                "a withdrawal keyword is not itself a withdrawal decision; the current official abs banner is authoritative",
            ],
        },
    }
    (OUT / "owner-summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
