"""Capture bounded requests for this day; retrieval does not assign review status."""
from datetime import datetime
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

OUT = Path(__file__).resolve().parent / "supplement-20261012"

THEMES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR ti:"mixture of experts") AND (ti:training OR ti:architecture OR ti:attention OR ti:reasoning OR ti:optimization OR ti:representation OR ti:evaluation OR ti:safety)',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR abs:transformer) AND (ti:GPU OR ti:kernel OR ti:parallel OR ti:serving OR ti:inference OR ti:quantization OR ti:cache OR ti:communication)',
    "agent": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM) AND (ti:agent OR ti:RAG OR ti:retrieval OR ti:memory OR ti:tool OR ti:planning)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND (ti:"vision language" OR ti:"vision-language" OR ti:VLA OR ti:"world model" OR ti:multimodal OR ti:"diffusion model" OR ti:"flow matching")',
    "hardware": '(cat:cs.AR OR cat:cs.PL OR cat:cs.PF) AND (ti:"language model" OR abs:"language model" OR ti:LLM OR abs:LLM OR ti:transformer OR abs:transformer) AND (ti:accelerator OR ti:compiler OR ti:kernel OR ti:GPU OR ti:quantization)',
}

DAILY = {
    "openai-research": "https://openai.com/research/",
    "openai-rss": "https://openai.com/news/rss.xml",
    "anthropic-research": "https://www.anthropic.com/research",
    "deepmind-research": "https://deepmind.google/research/",
    "deepmind-page2": "https://deepmind.google/research/publications/page/2/",
    "google-pubs": "https://research.google/pubs/?category=2025&search=language%20model",
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


def fetch(name, url, headers=(), body=None, timeout=25):
    OUT.mkdir(exist_ok=True)
    raw = OUT / (name + ".raw")
    record = OUT / (name + ".request.json")
    if raw.exists() or record.exists():
        raise RuntimeError("Existing request must not be overwritten: " + name)
    started = datetime.now().astimezone().isoformat()
    cmd = ["curl", "--location", "--silent", "--show-error", "--max-time", str(timeout),
           "--user-agent", "Mozilla/5.0", "--output", str(raw),
           "--write-out", "%{http_code}\\n%{url_effective}\\n%{size_download}", url]
    for header in headers:
        cmd.extend(["--header", header])
    if body is not None:
        cmd.extend(["--header", "Content-Type: application/json", "--data", body])
    result = subprocess.run(cmd, capture_output=True, text=True)
    metadata = result.stdout.splitlines()
    info = {"url": url, "headers": list(headers), "body": body,
            "started": started, "finished": datetime.now().astimezone().isoformat(),
            "exit": result.returncode, "curl_metadata": metadata,
            "stderr": result.stderr, "saved_bytes": raw.stat().st_size if raw.exists() else 0}
    record.write_text(json.dumps(info, ensure_ascii=False, indent=2) + "\n")
    print(name, metadata, "exit", result.returncode, "bytes", info["saved_bytes"], flush=True)


if __name__ == "__main__":
    if sys.argv[1] in {"arxiv", "arxiv-target"}:
        lower, upper, prefix = ("202510051800", "202510061800", "arxiv") if sys.argv[1] == "arxiv" else ("202510061800", "202510071800", "arxiv-target")
        for name, theme in THEMES.items():
            query = f'submittedDate:[{lower} TO {upper}] AND (' + theme + ')'
            url = 'https://export.arxiv.org/api/query?' + urlencode({
                'search_query': query, 'start': 0, 'max_results': 100,
                'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
            fetch(prefix + '-' + name, url)
    elif sys.argv[1] == "titles":
        for name, categories, limit in [
            ("cllg", '(cat:cs.CL OR cat:cs.LG)', 50),
            ("systems", '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF)', 20),
            ("cvro", '(cat:cs.CV OR cat:cs.RO)', 30),
        ]:
            query = 'submittedDate:[202510061800 TO 202510071800] AND ' + categories
            url = 'https://export.arxiv.org/api/query?' + urlencode({
                'search_query': query, 'start': 0, 'max_results': limit,
                'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
            fetch('titles-' + name, url)
    elif sys.argv[1] == "abs":
        for paper_id in sys.argv[2:]:
            fetch('abs-' + paper_id + 'v1', 'https://arxiv.org/abs/' + paper_id + 'v1')
    elif sys.argv[1] == "institutions":
        for name, url in DAILY.items():
            fetch(name, url)
    elif sys.argv[1] == "fetch":
        fetch(sys.argv[2], sys.argv[3], headers=sys.argv[4:])
    elif sys.argv[1] == "post":
        fetch(sys.argv[2], sys.argv[3], body=sys.argv[4])
    else:
        raise SystemExit("Use fetch or post")
