#!/usr/bin/env python3
"""Freeze DataCite identity/creation metadata for one arXiv YYMM namespace.

The snapshot is a discovery and announcement-recovery input.  It does not
establish manuscript claims or replace exact-version arXiv review.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import gzip
import hashlib
import json
from pathlib import Path
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
API = "https://api.datacite.org/dois"
FIELDS = (
    "doi,titles,subjects,dates,descriptions,url,version,relatedIdentifiers,"
    "created,registered"
)


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--month", required=True, help="four-digit arXiv YYMM namespace")
    parser.add_argument("--output-dir", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=6)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch_prefix(month: str, prefix: int) -> dict:
    params = {
        "query": f"doi:10.48550/arxiv.{month}.{prefix:02d}*",
        "page[size]": "1000",
        "page[number]": "1",
        "fields[dois]": FIELDS,
    }
    url = f"{API}?{urlencode(params)}"
    last_error: Exception | None = None
    for attempt in range(5):
        try:
            request = Request(url, headers={"User-Agent": "AI-System-Design/1.0"})
            with urlopen(request, timeout=90) as response:
                payload = json.load(response)
            total = int(payload.get("meta", {}).get("total", 0))
            data = payload.get("data", [])
            if total > 1000 or len(data) != total:
                raise RuntimeError(
                    f"prefix {prefix:02d} is not closed: records={len(data)} total={total}"
                )
            missing = [
                item.get("id")
                for item in data
                if not (
                    item.get("attributes", {}).get("created")
                    or item.get("attributes", {}).get("registered")
                )
            ]
            if missing:
                raise RuntimeError(
                    f"prefix {prefix:02d}: {len(missing)} records lack created/registered"
                )
            return {
                "prefix": prefix,
                "url": url,
                "fetched_at": datetime.now().astimezone().isoformat(),
                "payload": payload,
            }
        except Exception as exc:
            last_error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"prefix {prefix:02d} failed after bounded retries: {last_error}")


def main() -> None:
    args = arguments()
    if len(args.month) != 4 or not args.month.isdigit():
        raise SystemExit("--month must be a four-digit YYMM namespace")
    output = args.output_dir
    if not output.is_absolute():
        output = ROOT / output
    output.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(fetch_prefix, args.month, prefix): prefix
            for prefix in range(100)
        }
        for future in as_completed(futures):
            result = future.result()
            prefix = result["prefix"]
            path = output / f"doi-prefix-{args.month}-{prefix:02d}-page-01.json.gz"
            envelope = {
                "schema": "datacite-arxiv-created-snapshot-v1",
                "request_url": result["url"],
                "fetched_at": result["fetched_at"],
                **result["payload"],
            }
            with gzip.open(path, "wt", encoding="utf-8") as handle:
                json.dump(envelope, handle, ensure_ascii=False, sort_keys=True)
                handle.write("\n")
            results.append({
                "prefix": f"{prefix:02d}",
                "path": path.relative_to(ROOT).as_posix(),
                "records": len(result["payload"].get("data", [])),
                "total": int(result["payload"].get("meta", {}).get("total", 0)),
                "sha256": sha256(path),
                "request_url": result["url"],
                "fetched_at": result["fetched_at"],
            })
            print(f"{prefix:02d}: {results[-1]['records']}", flush=True)

    results.sort(key=lambda item: item["prefix"])
    manifest = {
        "schema": "datacite-arxiv-created-snapshot-manifest-v1",
        "month": args.month,
        "scope": (
            f"10.48550/arxiv.{args.month}.00* through "
            f"10.48550/arxiv.{args.month}.99*"
        ),
        "purpose": "historical arXiv announcement ownership recovery lead",
        "authority_boundary": (
            "DOI created/registered is matched to the official arXiv announcement "
            "schedule; it is not submission time or technical evidence."
        ),
        "files": results,
        "record_count": sum(item["records"] for item in results),
        "complete": len(results) == 100 and all(
            item["records"] == item["total"] for item in results
        ),
    }
    path = output / "manifest.json"
    path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "manifest": path.relative_to(ROOT).as_posix(),
        "files": len(results),
        "records": manifest["record_count"],
        "complete": manifest["complete"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
