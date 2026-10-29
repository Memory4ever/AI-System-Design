"""Immutable, serial captures for the Sep27 omission repair only."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys

BASE = Path(__file__).parent


def capture(name, url, purpose):
    raw = BASE / ("REPAIR_" + name + "_20261025.raw")
    receipt = raw.with_suffix(".request.json")
    if raw.exists() or receipt.exists():
        raise FileExistsError("Capture already exists; reuse it")
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    result = subprocess.run([
        "curl", "--silent", "--show-error", "--compressed", "--location",
        "--max-time", "30", "--user-agent", "AI-System-Design/1.0",
        "--write-out", "\nREPAIRHTTP:%{http_code}\nREPAIRURL:%{url_effective}", url,
    ], capture_output=True, timeout=35)
    body, marker, trailer = result.stdout.rpartition(b"\nREPAIRHTTP:")
    status, final_url = (trailer.decode().split("\nREPAIRURL:", 1)
                         if marker else ("000", url))
    if not marker:
        body = result.stdout
    record = {"url": url, "checked_utc": checked, "method": "GET",
              "purpose": purpose, "status": int(status), "final_url": final_url,
              "exit_code": result.returncode, "error": result.stderr.decode(errors="replace"),
              "bytes": len(body), "sha256": hashlib.sha256(body).hexdigest()}
    raw.write_bytes(body)
    receipt.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"name": name, **record}, ensure_ascii=False), flush=True)
    return record


if __name__ == "__main__":
    capture(*sys.argv[1:])
