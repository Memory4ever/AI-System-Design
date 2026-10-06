"""Bounded explicit downloads; no discovery, screening, or prior-day data."""
import argparse
import datetime
import json
import pathlib
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("url")
parser.add_argument("--header", action="append", default=[])
parser.add_argument("--data")
args = parser.parse_args()
root = pathlib.Path(__file__).parent
destination = root / args.name
if destination.parent != root or destination.exists():
    raise SystemExit("Refuse nested or existing output")
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
command = ["curl", "-L", "--max-time", "40", "--connect-timeout", "15", "-sS",
           "-A", "AI-System-Design historical source inspection", "-o", str(destination),
           "-w", "%{http_code}\n%{url_effective}\n%{content_type}\n"]
for header in args.header:
    command.extend(["-H", header])
if args.data is not None:
    command.extend(["--data", args.data])
command.append(args.url)
result = subprocess.run(command, capture_output=True, text=True)
receipt = {"requested_url": args.url, "started_utc": started,
           "ended_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "curl_exit": result.returncode, "response": result.stdout,
           "error": result.stderr,
           "bytes": destination.stat().st_size if destination.exists() else 0,
           "headers": args.header, "request_data": args.data}
destination.with_suffix(destination.suffix + ".receipt.json").write_text(
    json.dumps(receipt, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(receipt, ensure_ascii=False))
