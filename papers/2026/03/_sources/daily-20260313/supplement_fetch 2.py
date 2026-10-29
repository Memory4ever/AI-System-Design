"""Bounded 2026-03-13 supplemental source recovery; no report mutation."""
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
    url = spec if isinstance(spec, str) else spec["url"]
    headers = {"User-Agent": "AI-System-Design date-scoped research/1.0"}
    if isinstance(spec, dict):
        headers.update(spec.get("headers", {}))
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        req = urllib.request.Request(url, headers=headers)
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
    parser.add_argument("manifest", nargs="?")
    parser.add_argument("--baseline", action="store_true")
    parser.add_argument("--extract-only", action="store_true")
    args = parser.parse_args()
    if args.extract_only:
        count = 0
        for source in ROOT.glob("SUP_*.raw"):
            payload = source.read_bytes()
            if b"<html" in payload[:500].lower() or b"<!doctype html" in payload[:500].lower():
                text_parser = TextParser()
                text_parser.feed(payload.decode("utf-8", errors="replace"))
                source.with_suffix(".txt").write_text("\n".join(text_parser.parts) + "\n")
                count += 1
        print("Extracted", count, "saved HTML responses")
        raise SystemExit(0)
    if not args.manifest:
        parser.error("manifest is required unless --extract-only is used")
    if args.baseline:
        report = ROOT.parent.parent / "13" / "README.md"
        payload = report.read_bytes()
        baseline = {"report": str(report), "sha256": hashlib.sha256(payload).hexdigest(), "text": payload.decode(), "created": datetime.datetime.now(datetime.timezone.utc).isoformat()}
        target = ROOT / "SUP_BASELINE_20261009.json"
        if not target.exists():
            target.write_text(json.dumps(baseline, ensure_ascii=False, indent=2) + "\n")
    manifest = json.loads((ROOT / args.manifest).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(fetch, manifest.items()))
    (ROOT / (Path(args.manifest).stem + "_RESULT.json")).write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(results, ensure_ascii=False, indent=2))
