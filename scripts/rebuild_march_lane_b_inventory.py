#!/usr/bin/env python3
"""Build independent strict-window inventories for 2026-03-09..16.

The archived DataCite/arXiv packet is used only for enumerable identity,
category, abstract, and v1 provenance.  It is never mechanism evidence.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = ROOT / "papers/2026/04/_sources/datacite-arxiv-202603-v2"
CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
FILTERED = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def categories(attributes: dict) -> list[str]:
    values: set[str] = set()
    for item in attributes.get("subjects", []):
        subject = item.get("subject", "")
        if "(" in subject and subject.endswith(")"):
            values.add(subject.rsplit("(", 1)[1][:-1])
    return sorted(values)


def submitted_v1(attributes: dict) -> str | None:
    values = [
        item.get("date", "") for item in attributes.get("dates", [])
        if item.get("dateType") == "Submitted"
        and item.get("dateInformation") == "v1"
        and item.get("date")
    ]
    return min(values) if values else None


def clean(value: str) -> str:
    return " ".join(value.split())


def load() -> tuple[dict[str, dict], list[dict]]:
    records: dict[str, dict] = {}
    receipts: list[dict] = []
    for path in sorted(SNAPSHOT.glob("*.json.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            payload = json.load(handle)
        receipts.append({
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha256(path),
            "records": len(payload.get("data", [])),
            "reported_total": int(payload.get("meta", {}).get("total", 0)),
        })
        for record in payload.get("data", []):
            attributes = record.get("attributes", {})
            doi = attributes.get("doi", "").lower()
            if doi.startswith("10.48550/arxiv.2603."):
                records[doi] = attributes
    return records, receipts


def build(day: date, records: dict[str, dict], receipts: list[dict]) -> None:
    beijing = timezone(timedelta(hours=8))
    end = datetime.combine(day, time(9), beijing)
    start = end - timedelta(days=1)
    start_utc, end_utc = start.astimezone(timezone.utc), end.astimezone(timezone.utc)
    identities = []
    for doi, attrs in records.items():
        stamp = submitted_v1(attrs)
        if not stamp:
            continue
        published = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if not start_utc <= published < end_utc:
            continue
        aid = doi.split("arxiv.", 1)[1]
        cats = categories(attrs)
        if not (CORE | FILTERED).intersection(cats):
            continue
        titles = attrs.get("titles") or []
        descriptions = attrs.get("descriptions") or []
        abstract = next((x.get("description", "") for x in descriptions if x.get("descriptionType") == "Abstract"), "")
        identities.append({
            "arxiv_id": aid,
            "identity": f"{aid}v1",
            "source_family_id": f"SF-2026-ARXIV-{aid.replace('.', '-')}",
            "published_v1_utc": published.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "published_v1_beijing": published.astimezone(beijing).isoformat(),
            "title": clean(titles[0].get("title", "") if titles else ""),
            "abstract": clean(abstract),
            "categories": cats,
            "primary_category": cats[0] if cats else "",
            "route": "core_daily_semantic_review_required" if CORE.intersection(cats) else "keyword_filtered",
            "source_url": f"https://arxiv.org/abs/{aid}v1",
        })
    identities.sort(key=lambda row: (row["published_v1_utc"], row["arxiv_id"]))
    packet = ROOT / f"papers/2026/03/_sources/daily-{day:%Y%m%d}"
    packet.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "daily-v2.1-datacite-arxiv-inventory-v1",
        "report_date": day.isoformat(),
        "window_beijing": f"[{start.isoformat()}, {end.isoformat()})",
        "window_utc": f"[{start_utc.isoformat()}, {end_utc.isoformat()})",
        "source_role": "Discovery / Metadata fallback; not mechanism evidence",
        "snapshot_files": receipts,
        "snapshot_unique_dois": len(records),
        "registered_total": len(identities),
        "core_total": sum(row["route"].startswith("core") for row in identities),
        "keyword_total": sum(row["route"] == "keyword_filtered" for row in identities),
        "identities": identities,
    }
    (packet / "inventory.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"date": day.isoformat(), "registered": len(identities), "core": payload["core_total"], "filtered": payload["keyword_total"]}))


def main() -> None:
    records, receipts = load()
    for day in range(9, 17):
        build(date(2026, 3, day), records, receipts)


if __name__ == "__main__":
    main()
