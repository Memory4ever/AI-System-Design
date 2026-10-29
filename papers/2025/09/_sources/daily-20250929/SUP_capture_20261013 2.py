"""Bounded Sep28 BJT discovery with immutable request captures."""
import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse

BASE = Path(__file__).parent
URLS = {
    "openai-research": "https://openai.com/research/",
    "openai-rss": "https://openai.com/news/rss.xml",
    "anthropic": "https://www.anthropic.com/research",
    "google-month": "https://research.google/blog/2025/09/",
    "google-pubs": "https://research.google/pubs/",
    "deepmind": "https://deepmind.google/research/publications/",
    "deepmind-p2": "https://deepmind.google/research/publications/page/2/",
    "meta-research": "https://ai.meta.com/research/",
    "meta-p5": "https://ai.meta.com/global_search/?page=5",
    "qwen-registered": "https://qwenlm.github.io/",
    "qwen-config": "https://qwen.ai/api/page_config?code=research.research-list",
    "deepseek-home": "https://www.deepseek.com/",
    "deepseek-updates": "https://api-docs.deepseek.com/updates/",
    "moonshot": "https://platform.kimi.com/blog",
    "hunyuan-research": "https://hunyuan.tencent.com/research",
    "hunyuan-list": "https://api.hunyuan.tencent.com/api/blog/publicList",
    "zai": "https://www.zhipuai.cn/zh/research",
    "zai-p2": "https://www.zhipuai.cn/zh/research?page=2",
    "seed-research": "https://seed.bytedance.com/en/research",
    "seed-paper": "https://seed.bytedance.com/en/public_papers",
    "seed-blog-api": "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true",
    "seed-paper-api": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true",
    "ernie": "https://ernie.baidu.com/blog/zh/",
    "ernie-p2": "https://ernie.baidu.com/blog/zh/page/2/",
    "mimo": "https://mimo.xiaomi.com/",
    "minimax-en": "https://www.minimax.io/blog",
    "minimax-cn": "https://www.minimaxi.com/blog",
    "minimax-agent": "https://agent.minimax.io/docs/techblog",
    "minimax-index": "https://agent.minimax.io/docs/llms.txt",
}
THEMES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model") AND (all:architecture OR all:attention OR all:optimization OR all:training OR all:"post-training")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel OR all:compiler)',
    "agents": '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak OR all:"tool calling")',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action" OR all:"video generation" OR all:diffusion)',
}
for name, theme in THEMES.items():
    URLS["arxiv-" + name] = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": theme + " AND submittedDate:[202509271600 TO 202509281559]",
        "start": 0, "max_results": 100, "sortBy": "submittedDate", "sortOrder": "ascending",
    })


def capture(name, url):
    raw = BASE / ("SUP_curl-" + name + "_20261013.raw")
    receipt = raw.with_suffix(".request.json")
    if raw.exists() or receipt.exists():
        raise FileExistsError("Existing capture protected; choose a recovery name")
    record = {"url": url, "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "method": "GET", "timeout_seconds": 25, "purpose": "Sep28 BJT bounded discovery; submitted is not public"}
    command = ["curl", "--silent", "--show-error", "--compressed", "--location", "--max-time", "25", "-H", "User-Agent: Mozilla/5.0"]
    if name.startswith("seed-"):
        command.extend(["-H", "x-tt-locale: US"])
    if name.startswith("hunyuan-list"):
        record.update(method="POST", body={"pageNum": 1, "pageSize": 100, "renderType": 0})
        command.extend(["-H", "Content-Type: application/json", "--data", json.dumps(record["body"])])
    command.extend(["--write-out", "\nSUPHTTP:%{http_code}\nSUPURL:%{url_effective}", url])
    result = subprocess.run(command, capture_output=True, timeout=30)
    body, marker, metadata = result.stdout.rpartition(b"\nSUPHTTP:")
    if marker:
        status, final_url = metadata.decode().split("\nSUPURL:", 1)
        record.update(status=int(status), final_url=final_url)
    else:
        body = result.stdout
    record.update(exit_code=result.returncode, error=result.stderr.decode(errors="replace"),
                  bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    raw.write_bytes(body)
    receipt.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, record.get("status"), result.returncode, len(body), flush=True)


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "--url":
        capture(sys.argv[2], sys.argv[3])
    else:
        for key in sys.argv[1:] or URLS:
            capture(key, URLS[key])
