"""Capture explicitly selected source URLs for this day, with request metadata."""

import json
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).parent
name, url = sys.argv[1:3]
request = urllib.request.Request(url, headers={"User-Agent": "HistoricalDailyResearch/1.0"})
if len(sys.argv) > 3:
    request.data = sys.argv[3].encode()
    request.add_header("Content-Type", "application/json")
if "seed.bytedance.com/api/" in url:
    request.add_header("x-tt-locale", "US")
record = {"url": url, "method": request.get_method(),
          "request_body": sys.argv[3] if len(sys.argv) > 3 else None,
          "checked_at": datetime.now(timezone.utc).isoformat(),
          "request_headers": dict(request.header_items())}
try:
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
(root / (name + ".request.json")).write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record))
