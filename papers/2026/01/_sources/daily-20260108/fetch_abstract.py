"""Exact-version public title/abstract capture; stdout only."""
import datetime
import html
import json
import re
import sys
import time
import urllib.request

def plain(fragment):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", fragment)).split())

for paper_id in sys.argv[1:]:
    url = "https://arxiv.org/abs/" + paper_id + "v1"
    record = {"id": paper_id, "url": url, "version": "v1", "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            body = response.read().decode("utf-8")
        for field, pattern in [("title", r'<h1[^>]*class="title[^"\n]*"[^>]*>(.*?)</h1>'), ("abstract", r'<blockquote[^>]*class="abstract[^"\n]*"[^>]*>(.*?)</blockquote>'), ("history", r'<div[^>]*class="submission-history"[^>]*>(.*?)</div>')]:
            match = re.search(pattern, body, re.S)
            record[field] = plain(match.group(1)) if match else None
        record["links"] = re.findall(r'<a[^>]+href="([^"]+)"[^>]*class="abs-button', body)
    except Exception as error:
        record["error"] = str(error)
    print(json.dumps(record, ensure_ascii=False), flush=True)
    time.sleep(3)
