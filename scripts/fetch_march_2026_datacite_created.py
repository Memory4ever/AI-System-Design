#!/usr/bin/env python3
"""Fetch a frozen March 2026 arXiv DOI snapshot with creation timestamps.

The older repository snapshot intentionally omitted DataCite ``created`` and
``registered``.  Historical Daily ownership recovery needs those registry
timestamps only as a lead for matching arXiv's official announcement schedule;
they are not paper-submission or technical-evidence timestamps.
"""

from __future__ import annotations

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
OUTPUT = ROOT / "papers/2026/03/_sources/datacite-arxiv-202603-created"
API = "https://api.datacite.org/dois"
FIELDS = (
    "doi,titles,subjects,dates,descriptions,url,version,relatedIdentifiers,"
    "created,registered"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch_prefix(prefix: int) -> dict:
    params = {
        "query": f"doi:10.48550/arxiv.2603.{prefix:02d}*",
        "page[size]": "1000",
        "page[number]": "1",
        "fields[dois]": FIELDS,
    }
    url = f"{API}?{urlencode(params)}"
    error: Exception | None = None
    for attempt in range(5):
        try:
            request = Request(url, headers={"User-Agent": "AI-System-Design/1.0"})
            with urlopen(request, timeout=90) as response:
                payload = json.load(response)
            total = int(payload.get("meta", {}).get("total", 0))
            data = payload.get("data", [])
            if total > 1000:
                raise RuntimeError(f"prefix {prefix:02d}: total {total} exceeds one page")
            if len(data) != total:
                raise RuntimeError(
                    f"prefix {prefix:02d}: expected {total} records, got {len(data)}"
                )
            missing = [
                item.get("id")
                for item in data
                if not (item.get("attributes", {}).get("created") or
                        item.get("attributes", {}).get("registered"))
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
        except Exception as exc:  # bounded network retry with recorded failure
            error = exc
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"prefix {prefix:02d} failed after retries: {error}")


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = {pool.submit(fetch_prefix, prefix): prefix for prefix in range(100)}
        for future in as_completed(futures):
            result = future.result()
            prefix = result["prefix"]
            path = OUTPUT / f"doi-prefix-2603-{prefix:02d}-page-01.json.gz"
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
                "path": str(path.relative_to(ROOT)),
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
        "scope": "10.48550/arxiv.2603.00* through 10.48550/arxiv.2603.99*",
        "purpose": "historical arXiv announcement ownership recovery lead",
        "authority_boundary": (
            "DOI created/registered is matched to the official arXiv announcement "
            "schedule; it is not a submission timestamp or technical evidence."
        ),
        "files": results,
        "record_count": sum(item["records"] for item in results),
        "complete": len(results) == 100 and all(
            item["records"] == item["total"] for item in results
        ),
    }
    manifest_path = OUTPUT / "manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "manifest": str(manifest_path.relative_to(ROOT)),
        "files": len(results),
        "records": manifest["record_count"],
        "complete": manifest["complete"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
