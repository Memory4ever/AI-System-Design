"""Bounded 2026-03-14 supplemental source recovery; no report mutation."""
import argparse
import concurrent.futures
import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import urllib.request

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
    def handle_data(self, value):
        if not self.skip and value.strip():
            self.parts.append(value.strip())

ROOT = Path(__file__).resolve().parent

def fetch(pair):
    name, spec = pair
    config = {"url": spec} if isinstance(spec, str) else spec
    url = config["url"]
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        headers = {"User-Agent": "AI-System-Design date-scoped research/1.0", **config.get("headers", {})}
        body = json.dumps(config["json"]).encode() if "json" in config else None
        if body is not None:
            headers["Content-Type"] = "application/json"
        req = urllib.request.Request(url, data=body, headers=headers, method=config.get("method", "GET"))
        with urllib.request.urlopen(req, timeout=35) as response:
            payload = response.read()
            result = {"name": name, "url": url, "checked": now, "status": response.status, "bytes": len(payload), "final_url": response.url}
        (ROOT / (name + ".raw")).write_bytes(payload)
        if b"<html" in payload[:500].lower() or b"<!doctype html" in payload[:500].lower():
            parser = TextParser()
            parser.feed(payload.decode("utf-8", errors="replace"))
            (ROOT / (name + ".txt")).write_text("\n".join(parser.parts) + "\n")
    except Exception as exc:
        result = {"name": name, "url": url, "checked": now, "error": str(exc)}
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    args = parser.parse_args()
    manifest = json.loads((ROOT / args.manifest).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(fetch, manifest.items()))
    (ROOT / (Path(args.manifest).stem + "_RESULT.json")).write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))

