#!/usr/bin/env python3
"""Freeze a complete DataCite arXiv DOI-prefix snapshot for one YYMM month.

The snapshots are discovery metadata only. They establish registered identity,
subjects and submitted metadata; exact arXiv version history and manuscript
claims still require primary-source review.
"""

from __future__ import annotations

import argparse
import gzip
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path


FIELDS = "doi,titles,subjects,dates,descriptions,url,version,relatedIdentifiers"


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", required=True, help="arXiv YYMM prefix, for example 2605")
    parser.add_argument("--output-dir", required=True, type=Path)
    return parser.parse_args()


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "AI-System-Design research archive"})
    last_error: Exception | None = None
    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return response.read()
        except Exception as error:  # network/API transients are retried; final error is preserved
            last_error = error
            if attempt == 5:
                break
            time.sleep(attempt * 1.5)
    assert last_error is not None
    raise last_error


def main() -> None:
    args = arguments()
    if len(args.month) != 4 or not args.month.isdigit():
        raise SystemExit("--month must be a four-digit YYMM prefix")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    totals: dict[str, int] = {}
    seen: set[str] = set()

    # A one-digit prefix can hit DataCite's 10,000-result query cap. Two-digit
    # disjoint prefixes contain at most 1,000 possible arXiv sequence numbers,
    # so their reported totals are closed rather than silently truncated.
    for group_number in range(100):
        group = f"{group_number:02d}"
        page = 1
        group_count = 0
        while True:
            query = urllib.parse.urlencode({
                "query": f"doi:10.48550/arxiv.{args.month}.{group}*",
                "page[size]": 1000,
                "page[number]": page,
                "fields[dois]": FIELDS,
            })
            target = args.output_dir / f"doi-prefix-{args.month}-{group}-page-{page:02d}.json.gz"
            if target.exists():
                with gzip.open(target, "rb") as handle:
                    raw = handle.read()
            else:
                raw = fetch(f"https://api.datacite.org/dois?{query}")
                with target.open("wb") as compressed:
                    with gzip.GzipFile(fileobj=compressed, mode="wb", mtime=0) as handle:
                        handle.write(raw)
            payload = json.loads(raw)
            records = payload.get("data", [])
            total = int(payload.get("meta", {}).get("total", 0))
            for record in records:
                doi = str(record.get("attributes", {}).get("doi", "")).lower()
                if not doi.startswith(f"10.48550/arxiv.{args.month}."):
                    raise RuntimeError(f"unexpected DOI in prefix snapshot: {doi}")
                if doi in seen:
                    raise RuntimeError(f"duplicate DOI across prefix snapshots: {doi}")
                seen.add(doi)
            group_count += len(records)
            print(f"{args.month}.{group} page {page}: {group_count}/{total}", flush=True)
            if group_count >= total:
                totals[group] = total
                break
            if not records:
                raise RuntimeError(f"incomplete prefix {args.month}.{group}: {group_count}/{total}")
            page += 1
            time.sleep(0.25)

    (args.output_dir / "group-totals.json").write_text(
        json.dumps({"month": args.month, "groups": totals, "unique_dois": len(seen)}, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
