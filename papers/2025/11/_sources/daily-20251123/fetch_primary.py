"""Capture explicitly selected primary endpoints without automatic pagination."""

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).parent


def fetch(name, url, payload=None):
    headers = {"User-Agent": "HistoricalDailyResearch/1.0"}
    if "seed.bytedance.com/api/" in url:
        headers["x-tt-locale"] = "US"
    data = None
    if payload is not None:
        data = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
    record = {"url": url, "method": "POST" if data else "GET",
              "payload": payload, "request_headers": headers,
              "checked_at": datetime.now(timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, data=data, headers=headers)
        with urllib.request.urlopen(request, timeout=20) as response:
            body = response.read()
            record.update(status=response.status, response_url=response.url,
                          headers=dict(response.headers), bytes=len(body))
        (root / name).write_bytes(body)
    except urllib.error.HTTPError as error:
        record.update(status=error.code, error=str(error))
        (root / name).write_bytes(error.read())
    except Exception as error:
        record["error"] = str(error)
    (root / (name + ".request.json")).write_text(
        json.dumps(record, indent=2) + "\n")
    print(name, record.get("status"), record.get("bytes"), record.get("error", ""), flush=True)


if __name__ == "__main__":
    fetch(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]) if len(sys.argv) > 3 else None)
