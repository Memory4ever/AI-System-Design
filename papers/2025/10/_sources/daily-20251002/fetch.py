"""Save real upstream responses for one independently started Daily."""
import argparse
import datetime as dt
import json
from pathlib import Path
import urllib.error
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument("directory")
parser.add_argument("name")
parser.add_argument("url")
parser.add_argument("--json-body")
parser.add_argument("--header", action="append", default=[])
args = parser.parse_args()
directory = Path(args.directory)
directory.mkdir(parents=True, exist_ok=True)
receipt = {"url": args.url, "executed_at": dt.datetime.now(dt.timezone.utc).isoformat()}
headers = {"User-Agent": "AI-System-Design historical research (bounded source retrieval)"}
for header in args.header:
    key, value = header.split(":", 1)
    headers[key.strip()] = value.strip()
if args.header:
    receipt["request_headers"] = headers
payload = None
if args.json_body:
    payload = args.json_body.encode()
    headers["Content-Type"] = "application/json"
    receipt["request_body"] = json.loads(args.json_body)
request = urllib.request.Request(args.url, data=payload, headers=headers)
try:
    with urllib.request.urlopen(request, timeout=35) as response:
        body = response.read()
        receipt.update(status=response.status, final_url=response.url, headers=dict(response.headers))
except urllib.error.HTTPError as error:
    body = error.read()
    receipt.update(status=error.code, error=str(error), headers=dict(error.headers))
except Exception as error:
    body = b""
    receipt.update(error=str(error))
if body:
    (directory / (args.name + ".raw")).write_bytes(body)
receipt["bytes"] = len(body)
(directory / (args.name + ".receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: receipt[k] for k in ("url", "executed_at", "status", "error", "bytes") if k in receipt}, ensure_ascii=False))
