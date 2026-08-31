#!/usr/bin/env python3
"""Build the strict-window 2026-05-04 arXiv identity inventory."""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PACKET = ROOT / "papers/2026/05/_sources/daily-20260504"
MONTH_DIRS = [
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202604-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202605-v2",
    ROOT / "papers/2026/05/_sources/datacite-arxiv-202606-v2",
]
START = "2026-05-03T01:00:00Z"
END = "2026-05-04T01:00:00Z"
CORE = {"cs.AI", "cs.CL", "cs.LG", "cs.DC", "cs.IR", "stat.ML"}
FILTERED = {"cs.CV", "cs.RO", "cs.SE", "cs.CR", "cs.AR", "cs.PF", "cs.OS", "cs.PL", "cs.MA", "cs.DB", "cs.NI", "eess.AS", "cs.SD"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def categories(a: dict) -> list[str]:
    out = []
    for item in a.get("subjects", []):
        subject = item.get("subject", "")
        if "(" in subject and subject.endswith(")"):
            out.append(subject.rsplit("(", 1)[1][:-1])
    return sorted(set(out))


def v1_time(a: dict) -> str | None:
    values = [x.get("date", "") for x in a.get("dates", []) if x.get("dateType") == "Submitted" and x.get("dateInformation") == "v1"]
    return min(values) if values else None


def main() -> None:
    by_doi, files = {}, []
    for directory in MONTH_DIRS:
        for path in sorted(directory.glob("*.json.gz")):
            with gzip.open(path, "rt", encoding="utf-8") as handle:
                payload = json.load(handle)
            files.append({"path": str(path.relative_to(ROOT)), "sha256": digest(path)})
            for record in payload.get("data", []):
                a = record.get("attributes", {})
                doi = a.get("doi", "").lower()
                if doi.startswith("10.48550/arxiv."):
                    by_doi[doi] = a
    inside = []
    for doi, a in by_doi.items():
        submitted = v1_time(a)
        if not submitted or not START <= submitted < END:
            continue
        aid = doi.split("arxiv.", 1)[1]
        cats = categories(a)
        title = " ".join((a.get("titles") or [{"title": ""}])[0].get("title", "").split())
        abstract = next((x.get("description", "") for x in a.get("descriptions", []) if x.get("descriptionType") == "Abstract"), "")
        route = "core_daily_semantic_review_required" if CORE.intersection(cats) else "keyword_filtered"
        inside.append({"arxiv_id": aid, "identity": f"{aid}v1", "published_v1_utc": submitted,
                       "title": title, "abstract": " ".join(abstract.split()), "categories": cats,
                       "primary_category": cats[0] if cats else "", "route": route,
                       "registered": bool((CORE | FILTERED).intersection(cats)),
                       "source_url": f"https://arxiv.org/abs/{aid}v1"})
    inside.sort(key=lambda x: (x["published_v1_utc"], x["arxiv_id"]))
    registered = [x for x in inside if x["registered"]]
    out = {"schema": "daily-v2.1-datacite-arxiv-inventory-v1", "report_date": "2026-05-04",
           "window_beijing": "[2026-05-03T09:00:00+08:00, 2026-05-04T09:00:00+08:00)",
           "window_utc": f"[{START}, {END})", "source_role": "Discovery / Metadata fallback; not mechanism evidence",
           "complete_snapshot_dirs": [str(p.relative_to(ROOT)) for p in MONTH_DIRS], "snapshot_files": files,
           "all_snapshot_unique_dois": len(by_doi), "strict_window_total": len(inside),
           "registered_total": len(registered), "core_total": sum(x["route"].startswith("core") for x in registered),
           "keyword_total": sum(x["route"] == "keyword_filtered" for x in registered), "identities": registered}
    PACKET.mkdir(parents=True, exist_ok=True)
    (PACKET / "inventory.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
    rows = ["arxiv_id\tpublished_v1_utc\tprimary_category\troute\ttitle\tabstract"]
    for x in registered:
        rows.append("\t".join(str(x[k]).replace("\t", " ") for k in ("arxiv_id", "published_v1_utc", "primary_category", "route", "title", "abstract")))
    (PACKET / "inventory.tsv").write_text("\n".join(rows) + "\n")
    print(json.dumps({k: out[k] for k in ("all_snapshot_unique_dois", "strict_window_total", "registered_total", "core_total", "keyword_total")}))


if __name__ == "__main__":
    main()
