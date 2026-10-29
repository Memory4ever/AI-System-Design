"""Sep22 BJT bounded primary capture; submission is not publication."""
import datetime
import hashlib
import json
from pathlib import Path
import sys
import subprocess
import urllib.error
import urllib.parse
import urllib.request

BASE = Path(__file__).parent
URLS = {
    "openai-research": "https://openai.com/research/",
    "openai": "https://openai.com/news/rss.xml",
    "anthropic": "https://www.anthropic.com/research",
    "google-month": "https://research.google/blog/2025/09/",
    "google-pubs": "https://research.google/pubs/",
    "deepmind": "https://deepmind.google/research/publications/",
    "deepmind-p2": "https://deepmind.google/research/publications/page/2/",
    "meta": "https://ai.meta.com/research/",
    "qwen-registered": "https://qwenlm.github.io/",
    "qwen": "https://qwen.ai/research",
    "deepseek": "https://api-docs.deepseek.com/updates/",
    "moonshot": "https://platform.kimi.com/blog",
    "hunyuan": "https://hunyuan.tencent.com/research",
    "hunyuan-list": "https://api.hunyuan.tencent.com/api/blog/publicList",
    "zai": "https://www.zhipuai.cn/zh/research",
    "zai-p2": "https://www.zhipuai.cn/zh/research?page=2",
    "seed": "https://seed.bytedance.com/en/public_papers",
    "seed-blog": "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true",
    "seed-paper": "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true",
    "ernie": "https://ernie.baidu.com/blog/zh/",
    "ernie-p2": "https://ernie.baidu.com/blog/zh/page/2/",
    "mimo": "https://mimo.xiaomi.com/",
    "minimax-en": "https://www.minimax.io/blog",
    "minimax-p2": "https://www.minimax.io/blog?page=2",
    "minimax-cn": "https://www.minimaxi.com/blog",
    "minimax-agent": "https://agent.minimax.io/docs/techblog",
    "minimax-index": "https://agent.minimax.io/docs/llms.txt",
    "arxiv-schedule": "https://info.arxiv.org/help/availability.html",
}
THEMES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model") AND (all:architecture OR all:attention OR all:optimization OR all:training OR all:"post-training")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel OR all:compiler)',
    "agents": '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak OR all:"tool calling")',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action" OR all:"video generation" OR all:diffusion)',
}
for name, theme in THEMES.items():
    URLS["arxiv-" + name] = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": theme + " AND submittedDate:[202509211600 TO 202509221559]",
        "start": 0, "max_results": 150, "sortBy": "submittedDate", "sortOrder": "ascending",
    })

def capture(name, url, curl=False):
    raw = BASE / ("SUP_" + name + "_20261012.raw")
    receipt = raw.with_suffix(".request.json")
    if raw.exists() or receipt.exists():
        raise FileExistsError("Existing capture protected; use a recovery name")
    record = {"url": url, "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "method": "GET", "timeout_seconds": 30, "purpose": "Sep22 full BJT natural day bounded discovery",
              "headers": {"User-Agent": "Mozilla/5.0"}}
    logical_name = name.removeprefix("curl-")
    if logical_name.startswith("seed-"):
        record["headers"]["x-tt-locale"] = "US"
    data = None
    if logical_name.startswith("hunyuan-list"):
        record.update(method="POST", body={"pageNum": 1, "pageSize": 100, "renderType": 0})
        record["headers"]["Content-Type"] = "application/json"
        data = json.dumps(record["body"]).encode()
    try:
        if curl:
            record["transport"] = "curl TLS recovery"
            command = ["curl", "--silent", "--show-error", "--location", "--max-time", "30"]
            for key, value in record["headers"].items():
                command.extend(["-H", key + ": " + value])
            if data is not None:
                command.extend(["--data", data.decode()])
            command.extend(["--write-out", "\nSUPHTTP:%{http_code}\nSUPURL:%{url_effective}", url])
            result = subprocess.run(command, capture_output=True, timeout=35)
            body, marker, metadata = result.stdout.rpartition(b"\nSUPHTTP:")
            if marker:
                status, final_url = metadata.decode().split("\nSUPURL:", 1)
                record.update(status=int(status), final_url=final_url)
            else:
                body = result.stdout
            record["exit_code"] = result.returncode
            if result.stderr:
                record["error"] = result.stderr.decode(errors="replace")
        else:
            with urllib.request.urlopen(urllib.request.Request(url, headers=record["headers"], data=data), timeout=30) as response:
                body = response.read()
                record.update(status=response.status, final_url=response.url)
    except urllib.error.HTTPError as error:
        body = error.read()
        record.update(status=error.code, error=str(error))
    except Exception as error:
        body = b""
        record["error"] = str(error)
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    raw.write_bytes(body)
    receipt.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, record.get("status"), len(body), record.get("error", ""), flush=True)

if __name__ == "__main__":
    if sys.argv[1] == "--core":
        for identity in sys.argv[2:]:
            capture("curl-core-" + identity + "v1", "https://arxiv.org/html/" + identity + "v1", curl=True)
    elif sys.argv[1] == "--curl":
        if len(sys.argv) == 4 and sys.argv[3].startswith("https://"):
            capture("curl-" + sys.argv[2], sys.argv[3], curl=True)
        else:
            for key in sys.argv[2:]:
                capture("curl-" + key, URLS[key], curl=True)
    elif len(sys.argv) == 3 and sys.argv[2].startswith("https://"):
        capture(sys.argv[1], sys.argv[2])
    else:
        for key in sys.argv[1:]:
            capture(key, URLS[key])
