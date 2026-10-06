"""Persist bounded official arXiv responses and extract the target announcement section."""
import concurrent.futures
import datetime
import json
import re
import sys
import urllib.request
from pathlib import Path
from html import unescape

ROOT = Path(__file__).parent

def visible(raw):
    raw = re.sub(r"<(script|style)\b.*?</\1>", "", raw, flags=re.S)
    raw = re.sub(r"</?(?:h[1-6]|p|div|dt|dd|li|br|section)\b[^>]*>", "\n", raw)
    return "\n".join(x.strip() for x in unescape(re.sub(r"<[^>]+>", " ", raw)).splitlines() if x.strip())

def fetch(spec):
    name, url = spec.split("=", 1)
    rec = dict(name=name, url=url, checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}),timeout=25) as response:
            raw = response.read()
            rec.update(status=response.status, final_url=response.url, bytes=len(raw))
        (ROOT / (name + ".raw.html")).write_bytes(raw)
        raw = raw.decode("utf-8", errors="replace")
        text = visible(raw)
        (ROOT / (name + ".visible.txt")).write_text(text)
        if name.startswith("list_"):
            target = re.search(r"<h3[^>]*>\s*Mon, 19 Oct 2026.*?(?=<h3|$)",raw,re.S)
            if target:
                text=visible(target.group())
                (ROOT / (name + ".oct19.txt")).write_text(text)
                rec["target_section"] = text
            else:
                rec["target_section"]="NOT FOUND; not zero evidence"
        else:
            block = re.search(r"Title:.*?(?=Cite as:)",text,re.S)
            rec["visible"]=block.group() if block else text[:1200]
    except Exception as exc:
        rec["error"] = str(exc)
    return rec

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for record in pool.map(fetch, sys.argv[1:]):
            print(json.dumps(record,ensure_ascii=False), flush=True)
