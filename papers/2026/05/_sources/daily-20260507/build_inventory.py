#!/usr/bin/env python3
"""Build the reproducible 2026-05-07 registered-identity inventory."""

from __future__ import annotations

import csv
import gzip
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SNAPSHOT_ROOTS = [
    ROOT.parent / "datacite-arxiv-202604-v2",
    ROOT.parent / "datacite-arxiv-202605-v2",
    ROOT.parent / "datacite-arxiv-202606-v2",
]
START = datetime(2026, 5, 6, 1, 0, tzinfo=timezone.utc)
END = datetime(2026, 5, 7, 1, 0, tzinfo=timezone.utc)
CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
KEYWORD = {"cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS", "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD"}


def parse_dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> None:
    snapshots, records = [], []
    for snapshot_root in SNAPSHOT_ROOTS:
        for path in sorted(snapshot_root.glob("*.json.gz")):
            raw = path.read_bytes()
            payload = json.loads(gzip.decompress(raw))
            snapshots.append({"path": str(path.relative_to(ROOT.parent)), "records": len(payload["data"]), "sha256": hashlib.sha256(raw).hexdigest()})
            records.extend(payload["data"])

    identities, seen = [], set()
    for record in records:
        attrs = record["attributes"]
        arxiv_id = attrs["doi"].lower().rsplit("arxiv.", 1)[-1]
        if arxiv_id in seen:
            raise RuntimeError(f"duplicate identity across adjacent snapshots: {arxiv_id}")
        seen.add(arxiv_id)
        v1_dates = [parse_dt(x["date"]) for x in attrs.get("dates", []) if x.get("dateType") == "Submitted" and x.get("dateInformation") == "v1"]
        if len(v1_dates) != 1 or not (START <= v1_dates[0] < END):
            continue
        categories = sorted({x["subject"].removesuffix(")").rsplit("(", 1)[-1] for x in attrs.get("subjects", []) if x.get("subjectScheme") == "arXiv" and "(" in x.get("subject", "")})
        if not (CORE.intersection(categories) or KEYWORD.intersection(categories)):
            continue
        abstracts = [" ".join(x.get("description", "").split()) for x in attrs.get("descriptions", []) if x.get("descriptionType") == "Abstract"]
        identities.append({
            "arxiv_id": arxiv_id,
            "source_family_id": f"SF-2026-ARXIV-{arxiv_id.replace('.', '-')}",
            "submitted_v1_utc": v1_dates[0].isoformat().replace("+00:00", "Z"),
            "title": " ".join(attrs.get("titles", [{}])[0].get("title", "").split()),
            "categories": categories,
            "abstract": abstracts[0] if abstracts else "",
            "screening_route": "core_daily" if CORE.intersection(categories) else "keyword_daily",
            "screening_status": "pending_semantic_screen",
            "screening_reason": "pending",
        })
    identities.sort(key=lambda x: (x["submitted_v1_utc"], x["arxiv_id"]))
    packet = {
        "schema": "daily-v2.1-screening-ledger-v1",
        "report_date": "2026-05-07",
        "window": "[2026-05-06T09:00:00+08:00,2026-05-07T09:00:00+08:00)",
        "utc_window": "[2026-05-06T01:00:00Z,2026-05-07T01:00:00Z)",
        "source_role": "DataCite identity/date/abstract recovery; exact claims require SRC-ARXIV v1",
        "snapshots": snapshots,
        "raw_snapshot_records": len(records),
        "registered_window_identities": len(identities),
        "core_daily_semantic_review_required": sum(x["screening_route"] == "core_daily" for x in identities),
        "keyword_daily_semantic_review_required": sum(x["screening_route"] == "keyword_daily" for x in identities),
        "identities": identities,
    }
    (ROOT / "screening-ledger-provisional.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n")
    with (ROOT / "screening-ledger-provisional.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t")
        writer.writerow(["row", "arxiv_id", "submitted_v1_utc", "route", "categories", "title", "abstract"])
        for n, item in enumerate(identities, 1):
            writer.writerow([n, item["arxiv_id"], item["submitted_v1_utc"], item["screening_route"], ",".join(item["categories"]), item["title"], item["abstract"]])
    print(json.dumps({k: packet[k] for k in ("raw_snapshot_records", "registered_window_identities", "core_daily_semantic_review_required", "keyword_daily_semantic_review_required")}, indent=2))


if __name__ == "__main__":
    main()
