"""Save this day's bounded requests without assigning public dates or review status."""
from datetime import datetime
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

HERE = Path(__file__).resolve().parent
OUT = HERE / "supplement-20261012"


def fetch(name, url, headers=(), body=None):
    OUT.mkdir(exist_ok=True)
    raw = OUT / (name + ".raw")
    receipt = OUT / (name + ".request.json")
    if raw.exists() or receipt.exists():
        raise RuntimeError("Existing request must not be overwritten: " + name)
    start = datetime.now().astimezone().isoformat()
    cmd = ["curl", "--location", "--silent", "--show-error", "--max-time", "25",
           "--user-agent", "Mozilla/5.0", "--output", str(raw),
           "--write-out", "%{http_code}\\n%{url_effective}\\n%{size_download}", url]
    for header in headers:
        cmd.extend(["--header", header])
    if body is not None:
        cmd.extend(["--header", "Content-Type: application/json", "--data", body])
    result = subprocess.run(cmd, capture_output=True, text=True)
    metadata = result.stdout.splitlines()
    record = {"url": url, "headers": list(headers), "body": body,
              "started": start, "finished": datetime.now().astimezone().isoformat(),
              "exit": result.returncode, "curl_metadata": metadata,
              "stderr": result.stderr, "saved_bytes": raw.stat().st_size if raw.exists() else 0}
    receipt.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(name, metadata, "exit", result.returncode, "bytes", record["saved_bytes"], flush=True)


THEMES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR ti:"mixture of experts") AND (ti:training OR ti:architecture OR ti:attention OR ti:reasoning OR ti:optimization OR ti:representation OR ti:evaluation OR ti:safety)',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR abs:transformer) AND (ti:GPU OR ti:kernel OR ti:parallel OR ti:serving OR ti:inference OR ti:quantization OR ti:cache OR ti:communication)',
    "agent": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM) AND (ti:agent OR ti:RAG OR ti:retrieval OR ti:memory OR ti:tool OR ti:planning)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND (ti:"vision language" OR ti:"vision-language" OR ti:VLA OR ti:"world model" OR ti:multimodal OR ti:"diffusion model" OR ti:"flow matching")',
    "hardware": '(cat:cs.AR OR cat:cs.PL OR cat:cs.PF) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR abs:transformer) AND (ti:accelerator OR ti:compiler OR ti:kernel OR ti:GPU OR ti:quantization)',
}


def arxiv():
    for name, theme in THEMES.items():
        query = 'submittedDate:[202510031800 TO 202510041800] AND (' + theme + ')'
        url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": query,
              "start": 0, "max_results": 80, "sortBy": "submittedDate", "sortOrder": "ascending"})
        fetch("arxiv-" + name, url)


def institutions():
    endpoints = {
        "openai-research": "https://openai.com/research/",
        "openai-rss": "https://openai.com/news/rss.xml",
        "anthropic-research": "https://www.anthropic.com/research",
        "deepmind-research": "https://deepmind.google/research/",
        "deepmind-page2": "https://deepmind.google/research/publications/page/2/",
        "google-pubs": "https://research.google/pubs/?search=language%20model&category=2025",
        "google-october": "https://research.google/blog/2025/10/",
        "meta-research": "https://ai.meta.com/research/",
        "qwen-legacy": "https://qwenlm.github.io/blog/",
        "qwen-research": "https://qwen.ai/research",
        "deepseek-research": "https://www.deepseek.com/",
        "deepseek-news": "https://www.deepseek.com/news/",
        "moonshot-blog": "https://platform.kimi.com/blog",
        "hunyuan-research": "https://hunyuan.tencent.com/research",
        "zai-research": "https://www.zhipuai.cn/zh/research",
        "zai-page2": "https://www.zhipuai.cn/zh/research?page=2",
        "zai-release": "https://docs.z.ai/release-notes/new-released",
        "seed-research": "https://seed.bytedance.com/en/research",
        "seed-papers": "https://seed.bytedance.com/en/public_papers",
        "ernie-blog": "https://ernie.baidu.com/blog/zh/",
        "ernie-page2": "https://ernie.baidu.com/blog/zh/page/2/",
        "mimo": "https://mimo.xiaomi.com/",
        "minimax-en": "https://www.minimax.io/blog",
        "minimax-cn": "https://www.minimaxi.com/blog",
        "minimax-agent": "https://agent.minimax.io/docs/techblog",
    }
    for name, url in endpoints.items():
        fetch(name, url)


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "arxiv":
        arxiv()
    elif mode == "institutions":
        institutions()
    elif mode == "fetch":
        fetch(sys.argv[2], sys.argv[3], headers=sys.argv[4:])
    elif mode == "post":
        fetch(sys.argv[2], sys.argv[3], body=sys.argv[4])
    else:
        raise SystemExit("Unknown mode")
