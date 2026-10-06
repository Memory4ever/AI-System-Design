"""Capture bounded recovery endpoints for this day's source checks."""

import datetime
import json
from pathlib import Path
import urllib.request

out = Path(__file__).parent
urls = {
    "longcat-blog": "https://tech.meituan.com/2025/09/01/LongCat-Flash-Chat.html",
    "meituan-feed": "https://tech.meituan.com/feed/",
    "longcat-commits": "https://api.github.com/repos/meituan-longcat/LongCat-Flash-Chat/commits?per_page=100&until=2025-09-02T01:00:00Z",
    "google-month": "https://research.google/blog/2025/09/",
    "google-month-2": "https://research.google/blog/2025/09/?page=2",
    "deepmind-history": "https://deepmind.google/blog/page/5/",
    "deepseek-updates": "https://www.deepseek.com/updates",
    "ernie-page-2": "https://ernie.baidu.com/blog/zh/page/2/",
}
for name, url in urls.items():
    meta = {"url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "ResearchReview/1.0"})
        with urllib.request.urlopen(request, timeout=25) as response:
            raw = response.read()
            meta.update(status=response.status, bytes=len(raw), final_url=response.url)
            (out / (name + ".raw")).write_bytes(raw)
    except Exception as error:
        meta["error"] = str(error)
    (out / (name + ".request.json")).write_text(json.dumps(meta, indent=2))
    print(name, meta.get("status"), meta.get("bytes"), meta.get("error"), flush=True)
