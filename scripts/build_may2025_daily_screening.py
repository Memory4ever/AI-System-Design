#!/usr/bin/env python3
"""Build a reproducible V2.1 screening ledger from one arXiv Atom snapshot.

The script deliberately stops before Candidate Denominator admission.  It
separates recall from retention: every registered-category identity is kept
with its full title and abstract, while semantic admission remains a reviewed
decision recorded by the day owner.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path


ATOM = "http://www.w3.org/2005/Atom"
NS = {"atom": ATOM, "open": "http://a9.com/-/spec/opensearch/1.1/"}
CORE_DAILY = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD_DAILY = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}
REGISTERED = CORE_DAILY | KEYWORD_DAILY
ARXIV_ID = re.compile(r"(?:abs/)?(\d{4}\.\d{4,5})(?:v\d+)?")


def clean(value: str) -> str:
    return " ".join(value.split())


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report-date", required=True)
    parser.add_argument("--snapshot", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--weekly", action="append", default=[], type=Path)
    return parser.parse_args()


def prior_weekly_ids(paths: list[Path]) -> set[str]:
    result: set[str] = set()
    for path in paths:
        if not path.exists():
            continue
        result.update(ARXIV_ID.findall(path.read_text(encoding="utf-8")))
    return result


def main() -> None:
    args = parse_args()
    report_date = datetime.fromisoformat(args.report_date).date()
    cst = timezone(timedelta(hours=8))
    window_end = datetime.combine(report_date, datetime.min.time(), cst) + timedelta(hours=9)
    window_start = window_end - timedelta(days=1)
    start_utc = window_start.astimezone(timezone.utc)
    end_utc = window_end.astimezone(timezone.utc)

    root = ET.parse(args.snapshot).getroot()
    raw_entries = root.findall("atom:entry", NS)
    weekly_ids = prior_weekly_ids(args.weekly)
    records: list[dict[str, object]] = []
    for entry in raw_entries:
        identifier = entry.findtext("atom:id", default="", namespaces=NS)
        match = ARXIV_ID.search(identifier)
        if match is None:
            continue
        arxiv_id = match.group(1)
        published_text = entry.findtext("atom:published", default="", namespaces=NS)
        published = datetime.fromisoformat(published_text.replace("Z", "+00:00"))
        if not start_utc <= published < end_utc:
            continue
        categories = sorted({node.attrib["term"] for node in entry.findall("atom:category", NS)})
        if not REGISTERED.intersection(categories):
            continue
        core = bool(CORE_DAILY.intersection(categories))
        records.append(
            {
                "arxiv_id": arxiv_id,
                "source_family_key": f"arxiv:{arxiv_id}",
                "submitted_v1_utc": published_text,
                "submitted_v1_asia_shanghai": published.astimezone(cst).isoformat(),
                "title": clean(entry.findtext("atom:title", default="", namespaces=NS)),
                "abstract": clean(entry.findtext("atom:summary", default="", namespaces=NS)),
                "categories": categories,
                "screening_route": (
                    "core_daily_full_semantic_screen" if core else "keyword_daily_full_semantic_screen"
                ),
                "prior_weekly_trace": arxiv_id in weekly_ids,
                "semantic_screen_status": "pending",
                "semantic_decision_kind": "pending",
                "stable_node_id": "—",
                "family_specific_reason": "pending semantic review",
            }
        )

    records.sort(key=lambda row: (str(row["submitted_v1_utc"]), str(row["arxiv_id"])))
    args.output_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "daily-v2.1-screening-ledger-v1",
        "report_date": args.report_date,
        "window": f"[{window_start.isoformat()},{window_end.isoformat()})",
        "utc_window": f"[{start_utc.isoformat()},{end_utc.isoformat()})",
        "source": "SRC-ARXIV official Atom API",
        "snapshot": str(args.snapshot),
        "snapshot_sha256": sha256(args.snapshot),
        "raw_entries": len(raw_entries),
        "registered_window_identities": len(records),
        "core_daily_identities": sum(row["screening_route"].startswith("core") for row in records),
        "keyword_daily_identities": sum(row["screening_route"].startswith("keyword") for row in records),
        "prior_weekly_trace_count": sum(bool(row["prior_weekly_trace"]) for row in records),
        "records": records,
    }
    json_path = args.output_dir / "screening-ledger.json"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with (args.output_dir / "screening-ledger.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(
            [
                "arxiv_id", "submitted_v1_utc", "route", "title", "abstract",
                "categories", "prior_weekly_trace", "semantic_screen_status",
                "semantic_decision_kind", "stable_node_id", "family_specific_reason",
            ]
        )
        for row in records:
            writer.writerow(
                [
                    row["arxiv_id"], row["submitted_v1_utc"], row["screening_route"],
                    row["title"], row["abstract"], ";".join(row["categories"]),
                    str(row["prior_weekly_trace"]).lower(), row["semantic_screen_status"],
                    row["semantic_decision_kind"], row["stable_node_id"],
                    row["family_specific_reason"],
                ]
            )
    print(json.dumps({key: payload[key] for key in payload if key != "records"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
