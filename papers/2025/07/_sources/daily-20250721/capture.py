"""Bounded primary-source retrieval for the 2025-07-21 Daily; generated files are evidence captures."""
import concurrent.futures
import datetime
import json
import pathlib
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

OUT = pathlib.Path(__file__).parent
def fetch(item):
    key, url = item[:2]
    payload = item[2] if len(item) > 2 else None
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    try:
        headers = {"User-Agent": "AI-System-Design research evidence"}
        if payload is not None:
            headers["Content-Type"] = "application/json"
        with urllib.request.urlopen(urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None, headers=headers), timeout=35) as r:
            body = r.read()
            meta = {"url": url, "final_url": r.url, "status": r.status, "checked_at": stamp}
            if payload is not None:
                meta["method"] = "POST"
                meta["payload"] = payload
        (OUT / (key + ".raw")).write_bytes(body)
        if "api/query" in url:
            root = ET.fromstring(body)
            ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
            rows = [{k: e.findtext("a:" + k, "", ns) for k in ("id", "title", "summary", "published", "updated")} for e in root.findall("a:entry", ns)]
            meta["total_results"] = root.findtext("o:totalResults", "", ns)
            meta["returned"] = len(rows)
            (OUT / (key + "-entries.json")).write_text(json.dumps(rows, ensure_ascii=False, indent=2))
    except Exception as e:
        meta = {"url": url, "checked_at": stamp, "error": str(e)}
    (OUT / (key + ".request.json")).write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    return key, meta

base = "submittedDate:[202507171800 TO 202507181800] AND "
queries = {
    "arxiv-model": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model" OR all:"post-training")',
    "arxiv-systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND (all:"large language" OR all:"GPU" OR all:"inference" OR all:"distributed training")',
    "arxiv-agents": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:"language model" OR all:"tool calling" OR all:"retrieval augmented" OR all:"agent")',
    "arxiv-multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG) AND (all:"vision language" OR all:"world model" OR all:"vision-language-action" OR all:"video generation" OR all:"diffusion model" OR all:"foundation model")',
}
sources = {
    "openai": "https://openai.com/news/rss.xml", "anthropic": "https://www.anthropic.com/research",
    "deepmind": "https://deepmind.google/discover/blog/", "google-pubs": "https://research.google/pubs/",
    "meta": "https://ai.meta.com/blog/", "qwen": "https://qwenlm.github.io/",
    "deepseek": "https://api-docs.deepseek.com/updates", "moonshot": "https://platform.kimi.com/blog",
    "hunyuan": "https://hunyuan.tencent.com/research", "zai": "https://www.zhipuai.cn/zh/research",
    "seed": "https://seed.bytedance.com/en/public_papers", "ernie": "https://ernie.baidu.com/blog/zh/",
    "mimo": "https://mimo.xiaomi.com/", "minimax": "https://www.minimax.io/blog",
    "arxiv-schedule": "https://info.arxiv.org/help/availability.html",
}
if __name__ == "__main__":
    items = list(sources.items())
    for key, query in queries.items():
        items.append((key, "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": base + query, "start": 0, "max_results": 150, "sortBy": "submittedDate", "sortOrder": "ascending"})))
    if len(sys.argv) > 1:
        items = [(sys.argv[1], sys.argv[2])]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for result in pool.map(fetch, items):
            print(json.dumps(result, ensure_ascii=False))
