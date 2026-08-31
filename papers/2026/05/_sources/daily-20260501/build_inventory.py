#!/usr/bin/env python3
"""Build the strict-window 2026-05-01 arXiv identity inventory.

The official arXiv enumeration endpoint was unavailable during recovery.  The
complete, disjoint DataCite DOI-prefix snapshots are therefore used only to
recover manuscript identities, subjects, abstracts, and Submitted:v1 times.
Mechanism and evaluation claims must still come from exact-v1 arXiv text.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/05/_sources/daily-20260501"
MONTH_DIRS = [
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202604-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202605-v2",
]
START = "2026-04-30T01:00:00Z"
END = "2026-05-01T01:00:00Z"
CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
FILTERED = {
    "cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS",
    "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def categories(attributes: dict) -> list[str]:
    result = []
    for item in attributes.get("subjects", []):
        subject = item.get("subject", "")
        if "(" in subject and subject.endswith(")"):
            result.append(subject.rsplit("(", 1)[1][:-1])
    return sorted(set(result))


def v1_time(attributes: dict) -> str | None:
    values = [
        item.get("date", "") for item in attributes.get("dates", [])
        if item.get("dateType") == "Submitted" and item.get("dateInformation") == "v1"
    ]
    return min(values) if values else None


def main() -> None:
    PACKET.mkdir(parents=True, exist_ok=True)
    by_doi: dict[str, dict] = {}
    files = []
    for directory in MONTH_DIRS:
        for path in sorted(directory.glob("*.json.gz")):
            with gzip.open(path, "rt", encoding="utf-8") as handle:
                payload = json.load(handle)
            files.append({"path": str(path.relative_to(ROOT)), "sha256": digest(path)})
            for record in payload.get("data", []):
                attributes = record.get("attributes", {})
                doi = attributes.get("doi", "").lower()
                if doi.startswith("10.48550/arxiv."):
                    by_doi[doi] = attributes

    inside = []
    for doi, attributes in by_doi.items():
        submitted = v1_time(attributes)
        if not submitted or not START <= submitted < END:
            continue
        aid = doi.split("arxiv.", 1)[1]
        cats = categories(attributes)
        title = " ".join((attributes.get("titles") or [{"title": ""}])[0].get("title", "").split())
        descriptions = attributes.get("descriptions", [])
        abstract = next((x.get("description", "") for x in descriptions if x.get("descriptionType") == "Abstract"), "")
        route = "core_daily_semantic_review_required" if CORE.intersection(cats) else "keyword_filtered"
        inside.append({
            "arxiv_id": aid,
            "identity": f"{aid}v1",
            "published_v1_utc": submitted,
            "published_v1_beijing": submitted.replace("Z", "+00:00"),
            "title": title,
            "abstract": " ".join(abstract.split()),
            "categories": cats,
            "primary_category": cats[0] if cats else "",
            "route": route,
            "registered": bool((CORE | FILTERED).intersection(cats)),
            "source_url": f"https://arxiv.org/abs/{aid}v1",
        })
    inside.sort(key=lambda x: (x["published_v1_utc"], x["arxiv_id"]))
    registered = [x for x in inside if x["registered"]]
    payload = {
        "schema": "daily-v2.1-datacite-arxiv-inventory-v1",
        "report_date": "2026-05-01",
        "window_beijing": "[2026-04-30T09:00:00+08:00, 2026-05-01T09:00:00+08:00)",
        "window_utc": f"[{START}, {END})",
        "source_role": "Discovery / Metadata fallback; not mechanism evidence",
        "complete_snapshot_dirs": [str(p.relative_to(ROOT)) for p in MONTH_DIRS],
        "snapshot_files": files,
        "all_snapshot_unique_dois": len(by_doi),
        "strict_window_total": len(inside),
        "registered_total": len(registered),
        "core_total": sum(x["route"].startswith("core") for x in registered),
        "keyword_total": sum(x["route"] == "keyword_filtered" for x in registered),
        "identities": registered,
    }
    (PACKET / "inventory.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    header = "arxiv_id\tpublished_v1_utc\tprimary_category\troute\ttitle\tabstract"
    rows = [header]
    for item in registered:
        rows.append("\t".join(str(item[k]).replace("\t", " ") for k in (
            "arxiv_id", "published_v1_utc", "primary_category", "route", "title", "abstract"
        )))
    (PACKET / "inventory.tsv").write_text("\n".join(rows) + "\n")
    print(json.dumps({k: payload[k] for k in (
        "all_snapshot_unique_dois", "strict_window_total", "registered_total", "core_total", "keyword_total"
    )}))


if __name__ == "__main__":
    main()
