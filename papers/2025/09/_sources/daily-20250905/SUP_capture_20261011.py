"""Sep04 BJT supplement captures; submission fields are discovery only."""
import datetime
import hashlib
import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

BASE = pathlib.Path(__file__).parent
THEMES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model") AND (all:architecture OR all:attention OR all:optimization OR all:training OR all:"post-training")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel OR all:compiler)',
    "agents": '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak OR all:"tool calling")',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action" OR all:"video generation" OR all:diffusion)',
}
URLS = {
    "google-pubs-model2": "https://research.google/pubs/?category=2025&search=large+language+model&page=2",
    "google-pubs-agent2": "https://research.google/pubs/?category=2025&search=agent&page=2",
    "google-pubs-agent3": "https://research.google/pubs/?category=2025&search=agent&page=3",
    "dm-robotics": "https://deepmind.google/blog/gemini-robotics-15-brings-ai-agents-into-the-physical-world/",
    "dm-fsf": "https://deepmind.google/blog/strengthening-our-frontier-safety-framework/",
    "dm-fluid": "https://deepmind.google/blog/discovering-new-solutions-to-century-old-problems-in-fluid-dynamics/",
    "dm-icpc": "https://deepmind.google/blog/gemini-achieves-gold-medal-level-at-the-international-collegiate-programming-contest-world-finals/",
    "dm-vault": "https://research.google/blog/vaultgemma-the-worlds-most-capable-differentially-private-llm/",
    "dm-ligo": "https://deepmind.google/blog/using-ai-to-perceive-the-universe-in-greater-depth/",
    "google-js": "https://research.google/gr/static/js/googleresearch.js?id=ce1a221e995a08edf74272a1419af1e4",
    "hunyuan-js": "https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-I3I3bCf9.js",
    "qwen-blog": "https://qwenlm.github.io/",
    "mimo-home": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js",
    "mimo-paper": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js",
    "minimax-agent": "https://agent.minimax.io/docs/techblog",
    "openai": "https://openai.com/news/rss.xml",
    "anthropic": "https://www.anthropic.com/research",
    "google-month": "https://research.google/blog/2025/09/",
    "google-pubs": "https://research.google/pubs/",
    "deepmind": "https://deepmind.google/research/",
    "deepmind-history": "https://deepmind.google/blog/page/5/",
    "meta": "https://ai.meta.com/research/",
    "meta-results": "https://ai.meta.com/results/?content_types%5B0%5D=publication",
    "meta-blog": "https://ai.meta.com/blog/",
    "qwen": "https://qwen.ai/api/page_config?code=research.research-list",
    "deepseek": "https://api-docs.deepseek.com/updates",
    "moonshot": "https://platform.kimi.com/blog",
    "hunyuan": "https://hunyuan.tencent.com/research",
    "zai": "https://www.zhipuai.cn/zh/research",
    "seed": "https://seed.bytedance.com/en/research",
    "ernie": "https://ernie.baidu.com/blog/zh/",
    "mimo": "https://mimo.xiaomi.com/",
    "minimax-en": "https://www.minimax.io/blog",
    "minimax-cn": "https://www.minimaxi.com/blog",
}
for name, theme in THEMES.items():
    URLS["arxiv-" + name] = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({
        "search_query": theme + " AND submittedDate:[202509031600 TO 202509041559]",
        "start": 0, "max_results": 150, "sortBy": "submittedDate", "sortOrder": "ascending",
    })
for paper in ["03475", "03479", "03487", "03498", "03501", "03505", "03518", "03643", "03680", "03883", "03837", "03975", "03992", "04076", "04193", "04245", "04259", "04338", "10518"]:
    URLS["core-" + paper] = "https://arxiv.org/html/2509." + paper + "v1"


def capture(name, url):
    record = {"url": url, "checked_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "purpose": "Sep04 full BJT natural day; discovery is not public-date evidence",
              "method": "GET", "headers": {"User-Agent": "Mozilla/5.0"}}
    data = None
    if name.startswith("seed-"):
        record["headers"]["x-tt-locale"] = "US"
    if name.startswith("hunyuan-list"):
        record.update(method="POST", body={"pageNum": 1, "pageSize": 1000, "renderType": 0})
        record["headers"]["Content-Type"] = "application/json"
        if name.startswith("hunyuan-list-zh"):
            record["headers"]["accept-language"] = "zh"
        data = json.dumps(record["body"]).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=record["headers"], data=data), timeout=45) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url)
    except urllib.error.HTTPError as error:
        body = error.read()
        record.update(status=error.code, error=str(error))
    except Exception as error:
        body = b""
        record["error"] = str(error)
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    (BASE / ("SUP_" + name + "_20261011.raw")).write_bytes(body)
    (BASE / ("SUP_" + name + "_20261011.request.json")).write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, record.get("status"), len(body), record.get("error", ""), flush=True)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[2].startswith("https://"):
        capture(sys.argv[1], sys.argv[2])
    else:
        for key in sys.argv[1:]:
            capture(key, URLS[key])
