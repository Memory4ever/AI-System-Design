"""Fetch only the official RSS needed for the authorized Codex date reopening."""
import datetime
import json
import pathlib
import subprocess

root = pathlib.Path(__file__).parent
path = root / "codex_reopen_openai_rss.xml"
if path.exists():
    raise SystemExit("Existing raw must not be overwritten")
url = "https://openai.com/news/rss.xml"
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
result = subprocess.run(["curl", "-L", "--max-time", "40", "-sS", "-o", str(path),
                         "-w", "%{http_code}\n%{url_effective}\n%{content_type}\n", url],
                        capture_output=True, text=True)
receipt = {"url": url, "started_utc": started,
           "ended_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
           "exit": result.returncode, "response": result.stdout, "error": result.stderr,
           "bytes": path.stat().st_size if path.exists() else 0}
path.with_suffix(".xml.receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
print(json.dumps(receipt))
