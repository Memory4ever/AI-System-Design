"""Fresh Nov18 finite native retrieval. No prior-day responses or candidates."""
import datetime as dt
import json
from pathlib import Path
import subprocess
import sys
import urllib.parse

ROOT = Path(__file__).parent


def fetch(name, url, extra=()):
    dest = ROOT / name
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    run = subprocess.run(
        ["curl", "-L", "-sS", "--max-time", "12", "-A", "Mozilla/5.0",
         *extra, url, "-o", str(dest), "-w", "%{http_code}"],
        capture_output=True, text=True,
    )
    receipt = {"url": url, "extra": list(extra), "executed_at": started,
               "http_status": run.stdout, "exit_code": run.returncode,
               "error": run.stderr, "bytes": dest.stat().st_size if dest.exists() else 0,
               "scope": "one explicit page, not semantic or historical completeness"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps({"file": name, **receipt}), flush=True)


def main():
    if sys.argv[1:] == ["native"]:
        jobs = [
            ("openai-research.html", "https://openai.com/research/"),
            ("openai-rss.xml", "https://openai.com/news/rss.xml"),
            ("anthropic.html", "https://www.anthropic.com/research"),
            ("deepmind.html", "https://deepmind.google/research/"),
            ("google-pubs.html", "https://research.google/pubs/?year=2025"),
            ("meta.html", "https://ai.meta.com/research/"),
            ("qwen-old.html", "https://qwenlm.github.io/"),
            ("qwen-new.html", "https://qwen.ai/blog"),
            ("deepseek.html", "https://www.deepseek.com/"),
            ("moonshot.html", "https://platform.kimi.com/blog"),
            ("hunyuan-research.html", "https://hunyuan.tencent.com/research"),
            ("zai.html", "https://www.zhipuai.cn/zh/research"),
            ("seed.html", "https://seed.bytedance.com/en/research"),
            ("ernie.html", "https://ernie.baidu.com/blog/zh/"),
            ("mimo.html", "https://mimo.xiaomi.com/"),
            ("minimax-en.html", "https://www.minimax.io/blog"),
            ("minimax-cn.html", "https://www.minimaxi.com/blog"),
            ("minimax-agent.html", "https://agent.minimax.io/docs/techblog"),
            ("arxiv-availability.html", "https://info.arxiv.org/help/availability.html"),
        ]
        for name, url in jobs:
            fetch(name, url)
    elif sys.argv[1:] == ["arxiv"]:
        themes = {
            "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:transformer OR ti:"mixture of experts")',
            "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR ti:GPU OR ti:kernel)',
            "agents": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:"tool use" OR ti:"tool calling" OR ti:memory OR ti:"context management") AND (all:"language model" OR all:LLM)',
            "multimodal": '(cat:cs.CV OR cat:cs.RO) AND (ti:"foundation model" OR ti:"world model" OR ti:"vision-language" OR ti:"vision language" OR ti:"vision-language-action")',
        }
        for key, theme in themes.items():
            params = {"search_query": theme + " AND submittedDate:[202511131900 TO 202511141859]",
                      "start": 0, "max_results": 50,
                      "sortBy": "submittedDate", "sortOrder": "descending"}
            fetch("arxiv-" + key + "-page0.xml", "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
        fetch("arxiv-csDC-target-titles.html", "https://arxiv.org/list/cs.DC/2025-11?skip=50&show=50")
    else:
        raise SystemExit("native or arxiv required")


if __name__ == "__main__":
    main()
