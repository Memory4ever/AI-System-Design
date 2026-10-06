"""Capture bounded source repairs without changing prior evidence."""

import datetime
import json
from pathlib import Path
import urllib.request

out = Path(__file__).parent
urls = {
    "google-aug-frontier": "https://research.google/blog/2025/08/",
    "zai-page-2-repair": "https://www.zhipuai.cn/zh/research?page=2",
    "medreward-v1-repair": "https://arxiv.org/html/2508.21430v1",
}
for name, url in urls.items():
    meta = {"url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            raw = response.read()
            meta.update(status=response.status, bytes=len(raw), final_url=response.url)
            (out / (name + ".raw")).write_bytes(raw)
    except Exception as error:
        meta["error"] = str(error)
    (out / (name + ".request.json")).write_text(json.dumps(meta, indent=2))
    print(name, meta.get("status"), meta.get("bytes"), meta.get("error"), flush=True)
