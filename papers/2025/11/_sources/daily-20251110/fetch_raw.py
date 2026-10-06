"""Capture this day's explicit primary-source slice; no candidate decisions."""

import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).parent
entries = [
    ("openai-research.html", "https://openai.com/research/"),
    ("openai-rss.xml", "https://openai.com/news/rss.xml"),
    ("anthropic.html", "https://www.anthropic.com/research"),
    ("google-nov.html", "https://research.google/blog/2025/11/"),
    ("deepmind-p4.html", "https://deepmind.google/blog/page/4/"),
    ("deepmind-p5.html", "https://deepmind.google/blog/page/5/"),
    ("google-pubs.html", "https://research.google/pubs/?year=2025"),
    ("meta.html", "https://ai.meta.com/research/"),
    ("qwen-old.html", "https://qwenlm.github.io/"),
    ("qwen.html", "https://qwen.ai/blog"),
    ("deepseek.html", "https://www.deepseek.com/"),
    ("deepseek-updates.html", "https://api-docs.deepseek.com/updates"),
    ("kimi.html", "https://platform.kimi.com/blog"),
    ("hunyuan.html", "https://hunyuan.tencent.com/research"),
    ("hunyuan-p1.json", "https://api.hunyuan.tencent.com/api/blog/publicList",
     {"pageNum": 1, "pageSize": 20, "renderType": 0}),
    ("zai-p1.html", "https://www.zhipuai.cn/zh/research"),
    ("zai-p2.html", "https://www.zhipuai.cn/zh/research?page=2"),
    ("zai-releases.html", "https://docs.z.ai/release-notes/new-released"),
    ("seed-research.html", "https://seed.bytedance.com/en/research"),
    ("seed-papers.html", "https://seed.bytedance.com/en/public_papers"),
    ("seed-t1-p0.json", "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=0&order_desc=true"),
    ("seed-t2-p0.json", "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true"),
    ("ernie-p1.html", "https://ernie.baidu.com/blog/zh/"),
    ("ernie-p2.html", "https://ernie.baidu.com/blog/zh/page/2/"),
    ("mimo.html", "https://mimo.xiaomi.com/"),
    ("minimax.html", "https://www.minimax.io/blog"),
    ("minimax-cn.html", "https://www.minimaxi.com/blog"),
    ("minimax-agent.txt", "https://agent.minimax.io/docs/llms.txt"),
    ("arxiv-availability.html", "https://info.arxiv.org/help/availability.html"),
    ("arxiv-availability-2025.md", "https://raw.githubusercontent.com/arXiv/arxiv-docs/95c71658adbaa987dc2ba1105ef9c5201ecde4ce/source/help/availability.md"),
]
for entry in entries:
    name, url = entry[:2]
    body = entry[2] if len(entry) == 3 else None
    headers = {"User-Agent": "HistoricalDailyResearch/1.0"}
    if "seed.bytedance.com/api/" in url:
        headers["x-tt-locale"] = "US"
    data = None if body is None else json.dumps(body).encode()
    if data is not None:
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers)
    record = {"url": url, "checked_at": datetime.now(timezone.utc).isoformat(),
              "method": request.get_method(), "body": body}
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read()
            record.update(status=response.status, final_url=response.url, bytes=len(raw))
        (root / name).write_bytes(raw)
    except urllib.error.HTTPError as error:
        record.update(status=error.code, error=str(error))
        (root / name).write_bytes(error.read())
    except Exception as error:
        record["error"] = str(error)
    (root / (name + ".receipt.json")).write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"file": name, **record}), flush=True)
