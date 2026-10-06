"""Capture bounded primary-source requests; successful downloads are not reviews."""

import concurrent.futures
import datetime
import json
from pathlib import Path
import sys
import urllib.error
import urllib.parse
import urllib.request

OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)
SOURCES = [
    ("openai", "https://openai.com/research/", None),
    ("openai-rss", "https://openai.com/news/rss.xml", None),
    ("anthropic", "https://www.anthropic.com/research", None),
    ("deepmind", "https://deepmind.google/research/", None),
    ("google-pubs", "https://research.google/pubs/?year=2025", None),
    ("google-blog", "https://research.google/blog/", None),
    ("meta", "https://ai.meta.com/research/", None),
    ("qwen", "https://qwenlm.github.io/", None),
    ("qwen-new", "https://qwen.ai/research", None),
    ("deepseek", "https://www.deepseek.com/", None),
    ("deepseek-news", "https://www.deepseek.com/news/", None),
    ("moonshot", "https://platform.kimi.com/blog", None),
    ("hunyuan", "https://hunyuan.tencent.com/research", None),
    ("hunyuan-api", "https://api.hunyuan.tencent.com/api/blog/publicList",
     {"pageNum": 1, "pageSize": 100, "renderType": 0}),
    ("zai", "https://www.zhipuai.cn/zh/research", None),
    ("zai-releases", "https://docs.z.ai/release-notes/new-released", None),
    ("seed", "https://seed.bytedance.com/en/research", None),
    ("seed-paper", "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true", None),
    ("seed-blog", "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true", None),
    ("ernie", "https://ernie.baidu.com/blog/zh/", None),
    ("mimo", "https://mimo.xiaomi.com/", None),
    ("minimax", "https://www.minimax.io/blog", None),
    ("minimax-cn", "https://www.minimaxi.com/blog", None),
    ("minimax-agent", "https://agent.minimax.io/docs/techblog", None),
]


def capture(item):
    name, url, body = item
    meta = {"url": url, "body": body,
            "started": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    data = json.dumps(body).encode() if body is not None else None
    request = urllib.request.Request(url, data=data, headers={
        "User-Agent": "Mozilla/5.0", "Content-Type": "application/json",
        "Locale": "US"})
    try:
        with urllib.request.urlopen(request, timeout=22) as response:
            raw = response.read(3_000_001)
            meta.update(status=response.status, final_url=response.url,
                        headers=dict(response.headers), bytes=len(raw),
                        truncated=len(raw) > 3_000_000)
    except urllib.error.HTTPError as error:
        raw = error.read(300_000)
        meta.update(status=error.code, error=str(error), bytes=len(raw))
    except Exception as error:
        raw = b""
        meta.update(status=None, error=str(error), bytes=0)
    meta["finished"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    (OUT / (name + ".raw")).write_bytes(raw)
    (OUT / (name + ".request.json")).write_text(
        json.dumps(meta, ensure_ascii=False, indent=2) + "\n")
    return {key: meta.get(key) for key in ("url", "status", "bytes", "error", "truncated")}


with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    for result in pool.map(capture, SOURCES):
        print(json.dumps(result, ensure_ascii=False), flush=True)
