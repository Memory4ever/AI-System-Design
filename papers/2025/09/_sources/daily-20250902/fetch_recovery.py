"""Capture only unresolved mechanical discovery routes for this day."""

import datetime
import json
from pathlib import Path
import urllib.request

out = Path(__file__).parent
urls = {
    "deepseek-correct-updates": "https://api-docs.deepseek.com/updates/",
    "qwen-research-config": "https://qwen.ai/api/page_config?code=research.research-list",
    "google-aug-frontier": "https://research.google/blog/2025/08/",
    "zai-page-2": "https://www.zhipuai.cn/zh/research?page=2",
    "arxiv-month-CL": "https://arxiv.org/list/cs.CL/2509?skip=0&show=2000",
    "arxiv-month-LG": "https://arxiv.org/list/cs.LG/2509?skip=0&show=2000",
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
