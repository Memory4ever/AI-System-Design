#!/usr/bin/env python3
"""Build strict-window arXiv identity inventories for April 2026 Daily replay.

DataCite snapshots are discovery metadata only.  They close identity, category,
abstract and Submitted:v1 enumeration; mechanism claims still require exact-v1
arXiv HTML/PDF review.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIRS = (
    ROOT / "papers/2026/04/_sources/datacite-arxiv-202603-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202604-v2",
)
CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
FILTERED = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dates", nargs="+", help="report dates in YYYY-MM-DD")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def categories(attributes: dict) -> list[str]:
    result: set[str] = set()
    for item in attributes.get("subjects", []):
        subject = item.get("subject", "")
        if "(" in subject and subject.endswith(")"):
            result.add(subject.rsplit("(", 1)[1][:-1])
    return sorted(result)


def submitted_v1(attributes: dict) -> str | None:
    values = [
        item.get("date", "")
        for item in attributes.get("dates", [])
        if item.get("dateType") == "Submitted"
        and item.get("dateInformation") == "v1"
        and item.get("date")
    ]
    return min(values) if values else None


def normalized_text(value: str) -> str:
    return " ".join(value.split())


def load_records() -> tuple[dict[str, dict], list[dict]]:
    by_doi: dict[str, dict] = {}
    files: list[dict] = []
    for directory in SNAPSHOT_DIRS:
        if not directory.is_dir():
            raise RuntimeError(f"missing closed snapshot directory: {directory}")
        for path in sorted(directory.glob("*.json.gz")):
            with gzip.open(path, "rt", encoding="utf-8") as handle:
                payload = json.load(handle)
            files.append({
                "path": path.relative_to(ROOT).as_posix(),
                "sha256": sha256(path),
                "records": len(payload.get("data", [])),
                "reported_total": int(payload.get("meta", {}).get("total", 0)),
            })
            for record in payload.get("data", []):
                attributes = record.get("attributes", {})
                doi = attributes.get("doi", "").lower()
                if doi.startswith(("10.48550/arxiv.2603.", "10.48550/arxiv.2604.")):
                    by_doi[doi] = attributes
    return by_doi, files


def build(report_date: date, records: dict[str, dict], files: list[dict]) -> None:
    beijing = timezone(timedelta(hours=8))
    end = datetime.combine(report_date, time(9, 0), beijing)
    start = end - timedelta(days=1)
    start_utc = start.astimezone(timezone.utc)
    end_utc = end.astimezone(timezone.utc)
    identities: list[dict] = []

    for doi, attributes in records.items():
        submitted = submitted_v1(attributes)
        if not submitted:
            continue
        submitted_dt = datetime.fromisoformat(submitted.replace("Z", "+00:00"))
        if not start_utc <= submitted_dt < end_utc:
            continue
        aid = doi.split("arxiv.", 1)[1]
        cats = categories(attributes)
        titles = attributes.get("titles") or []
        title = normalized_text(titles[0].get("title", "") if titles else "")
        descriptions = attributes.get("descriptions") or []
        abstract = next(
            (item.get("description", "") for item in descriptions
             if item.get("descriptionType") == "Abstract"),
            "",
        )
        route = "core_daily_semantic_review_required" if CORE.intersection(cats) else "keyword_filtered"
        identities.append({
            "arxiv_id": aid,
            "identity": f"{aid}v1",
            "published_v1_utc": submitted_dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"),
            "published_v1_beijing": submitted_dt.astimezone(beijing).isoformat(),
            "title": title,
            "abstract": normalized_text(abstract),
            "categories": cats,
            "primary_category": cats[0] if cats else "",
            "route": route,
            "registered": bool((CORE | FILTERED).intersection(cats)),
            "source_url": f"https://arxiv.org/abs/{aid}v1",
        })

    identities.sort(key=lambda item: (item["published_v1_utc"], item["arxiv_id"]))
    registered = [item for item in identities if item["registered"]]
    packet = ROOT / f"papers/2026/04/_sources/daily-{report_date:%Y%m%d}"
    packet.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "daily-v2.1-datacite-arxiv-inventory-v1",
        "report_date": report_date.isoformat(),
        "window_beijing": f"[{start.isoformat()}, {end.isoformat()})",
        "window_utc": f"[{start_utc.isoformat()}, {end_utc.isoformat()})",
        "source_role": "Discovery / Metadata fallback; not mechanism evidence",
        "snapshot_files": files,
        "snapshot_unique_dois": len(records),
        "strict_window_total": len(identities),
        "registered_total": len(registered),
        "core_total": sum(item["route"].startswith("core") for item in registered),
        "keyword_total": sum(item["route"] == "keyword_filtered" for item in registered),
        "identities": registered,
    }
    (packet / "inventory.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    columns = (
        "arxiv_id", "published_v1_utc", "published_v1_beijing", "primary_category",
        "route", "title", "abstract",
    )
    rows = ["\t".join(columns)]
    for item in registered:
        rows.append("\t".join(str(item[key]).replace("\t", " ") for key in columns))
    (packet / "inventory.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(json.dumps({
        "date": report_date.isoformat(),
        "strict_window_total": len(identities),
        "registered_total": len(registered),
        "core_total": payload["core_total"],
        "keyword_total": payload["keyword_total"],
    }, ensure_ascii=False))


def main() -> None:
    args = arguments()
    records, files = load_records()
    for raw in args.dates:
        report_date = date.fromisoformat(raw)
        if report_date.year != 2026 or report_date.month != 4:
            raise SystemExit(f"date outside April 2026: {raw}")
        build(report_date, records, files)


if __name__ == "__main__":
    main()
