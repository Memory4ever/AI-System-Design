"""Bounded requests for this day's supplement; saved responses are not reviews."""
import argparse
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode

OUT = Path(__file__).parent / "supplement-20261011"
OUT.mkdir(exist_ok=True)


def capture(name, url, body=None, headers=()):
    raw = OUT / (name + ".raw")
    receipt = OUT / (name + ".request.json")
    if raw.exists() or receipt.exists():
        raise FileExistsError(name)
    command = ["curl", "-L", "--max-time", "30", "-sS", "-A", "Mozilla/5.0",
               "-w", "\n__SUP_META__%{http_code}\t%{url_effective}", url]
    for header in headers:
        command += ["-H", header]
    if body is not None:
        command += ["-H", "Content-Type: application/json", "--data", json.dumps(body)]
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run(command, capture_output=True)
    payload, marker, tail = result.stdout.rpartition(b"\n__SUP_META__")
    if not marker:
        payload = result.stdout
    raw.write_bytes(payload)
    parts = tail.decode(errors="replace").split("\t", 1)
    record = {"url": url, "method": "POST" if body is not None else "GET",
              "body": body, "headers": list(headers), "started_utc": started,
              "finished_utc": datetime.now(timezone.utc).isoformat(),
              "status": parts[0] if marker else None,
              "final_url": parts[1] if len(parts) == 2 else None,
              "exit_code": result.returncode, "error": result.stderr.decode(errors="replace"),
              "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}
    receipt.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, record["status"], len(payload), "exit", result.returncode, flush=True)


def phrase_query(terms):
    return "(" + " OR ".join(f'{field}:"{term}"' for term in terms for field in ("ti", "abs")) + ")"


def arxiv():
    lm = phrase_query(["language model", "LLM", "transformer", "foundation model"])
    topics = {
        "model": '(cat:cs.CL OR cat:cs.LG) AND ' + phrase_query([
            "language model", "LLM", "transformer", "foundation model", "mixture of experts",
            "linear attention", "diffusion language", "reasoning model"]),
        "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND '
        + lm + ' AND ' + phrase_query(["GPU", "kernel", "parallel", "serving", "inference",
                                      "quantization", "cache", "communication"]),
        "agents": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND ' + lm + ' AND '
        + phrase_query(["agent", "RAG", "retrieval", "memory", "tool", "planning"]),
        "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND ' + phrase_query([
            "vision language", "vision-language", "VLA", "world model", "multimodal language",
            "diffusion model", "generative foundation"]),
        "hardware": '(cat:cs.AR OR cat:cs.DC OR cat:cs.PL OR cat:cs.PF) AND ' + lm + ' AND '
        + phrase_query(["accelerator", "compiler", "kernel", "hardware", "GPU"]),
    }
    for name, topic in topics.items():
        query = 'submittedDate:[202510011800 TO 202510021800] AND (' + topic + ')'
        url = "https://export.arxiv.org/api/query?" + urlencode({
            "search_query": query, "start": 0, "max_results": 200,
            "sortBy": "submittedDate", "sortOrder": "ascending"})
        capture("arxiv-" + name, url)


def primary():
    sources = {
        "openai-rss": "https://openai.com/news/rss.xml",
        "anthropic": "https://www.anthropic.com/research",
        "deepmind": "https://deepmind.google/research/publications/page/2/",
        "google-pubs": "https://research.google/pubs/?search=language%20model&category=2025",
        "google-october": "https://www.research.google/blog/2025/10/",
        "google-october-page2": "https://www.research.google/blog/2025/10/?page=2",
        "meta": "https://ai.meta.com/research/",
        "meta-results": "https://ai.meta.com/research/publications/?page=4",
        "qwen": "https://qwenlm.github.io/",
        "deepseek": "https://www.deepseek.com/news/",
        "moonshot": "https://platform.kimi.com/blog",
        "hunyuan": "https://hunyuan.tencent.com/research",
        "zai": "https://www.zhipuai.cn/zh/research",
        "zai-page2": "https://www.zhipuai.cn/zh/research?page=2",
        "seed": "https://seed.bytedance.com/en/research",
        "ernie": "https://ernie.baidu.com/blog/zh/",
        "ernie-page2": "https://ernie.baidu.com/blog/zh/page/2/",
        "mimo": "https://mimo.xiaomi.com/",
        "minimax-en": "https://www.minimax.io/blog",
        "minimax-cn": "https://www.minimaxi.com/blog",
        "minimax-agent": "https://agent.minimax.io/docs/techblog",
    }
    for name, url in sources.items():
        capture(name, url)
    capture("hunyuan-api", "https://api.hunyuan.tencent.com/api/blog/publicList",
            body={"pageNum": 1, "pageSize": 100, "renderType": 0})
    for kind in (1, 2):
        url = "https://seed.bytedance.com/api/get_article_list_v2?" + urlencode({
            "article_type": kind, "publish_year": 2025, "count": 20,
            "order_desc": "false", "mode": 1, "page_token": 0})
        capture("seed-type" + str(kind) + "-us0", url, headers=("x-tt-locale: US",))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["arxiv", "primary", "one"])
    parser.add_argument("name", nargs="?")
    parser.add_argument("url", nargs="?")
    args = parser.parse_args()
    if args.mode == "arxiv":
        arxiv()
    elif args.mode == "primary":
        primary()
    else:
        if not args.name or not args.url:
            parser.error("one requires name and URL")
        capture(args.name, args.url)
