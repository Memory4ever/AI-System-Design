"""Save bounded official requests without overwriting prior evidence."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).parent / "supplement-20261007"


def fetch(name, url, payload=None, extra_headers=None):
    if "catchup" in url.lower():
        raise ValueError("catchup is prohibited")
    ROOT.mkdir(exist_ok=True)
    raw_path = ROOT / (name + ".raw")
    request_path = ROOT / (name + ".request.json")
    if raw_path.exists() or request_path.exists():
        raise FileExistsError(name)
    record = {"url": url, "start_utc": datetime.now(timezone.utc).isoformat()}
    headers = {"User-Agent": "Mozilla/5.0 (bounded historical research)"}
    if extra_headers:
        headers.update(extra_headers)
        record["request_headers"] = extra_headers
    data = None
    if payload is not None:
        data = payload.encode()
        headers["Content-Type"] = "application/json"
        record["payload"] = json.loads(payload)
    record["method"] = "POST" if data is not None else "GET"
    try:
        response = urlopen(Request(url, data=data, headers=headers), timeout=25)
        raw = response.read()
        record.update(status=response.status, final_url=response.url,
                      headers=dict(response.headers))
    except HTTPError as error:
        raw = error.read()
        record.update(status=error.code, final_url=error.url, error=str(error))
    except Exception as error:
        raw = b""
        record.update(status=None, error=repr(error))
    record.update(end_utc=datetime.now(timezone.utc).isoformat(), bytes=len(raw),
                  sha256=hashlib.sha256(raw).hexdigest())
    raw_path.write_bytes(raw)
    request_path.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"name": name, **{key: record.get(key) for key in
                     ("url", "status", "start_utc", "end_utc", "bytes", "sha256", "error")}},
                     ensure_ascii=False))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    parser.add_argument("url")
    parser.add_argument("--payload")
    args = parser.parse_args()
    fetch(args.name, args.url, args.payload)
