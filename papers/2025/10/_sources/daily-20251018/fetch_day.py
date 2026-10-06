"""Save actual primary responses for this day's bounded discovery."""
import datetime
import json
import pathlib
import subprocess
import time
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent
MANIFEST = ROOT / "fetch_manifest.json"


def fetch(name, url, data=None, headers=None, timeout=20):
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    output = ROOT / (name + ".raw")
    args = ["curl", "-L", "--compressed", "-sS", "--max-time", str(timeout),
            "-A", "Mozilla/5.0", "-o", str(output), "-w", "%{http_code}", url]
    if data is not None:
        args += ["-H", "Content-Type: application/json", "--data", json.dumps(data)]
    for key, value in (headers or {}).items():
        args += ["-H", key + ": " + value]
    before = time.monotonic()
    result = subprocess.run(args, capture_output=True, text=True)
    record = dict(name=name, url=url, request_body=data, headers=headers,
                  started_utc=started, elapsed_seconds=round(time.monotonic()-before, 3),
                  http_status=result.stdout, exit_code=result.returncode,
                  stderr=result.stderr, bytes=output.stat().st_size if output.exists() else 0,
                  raw_file=output.name if output.exists() else None)
    records = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else []
    records.append(record)
    MANIFEST.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(record, ensure_ascii=False), flush=True)
    return record


if __name__ == "__main__":
    for name, url in [
        ("openai_research", "https://openai.com/research/"),
        ("openai_rss", "https://openai.com/news/rss.xml"),
        ("anthropic_research", "https://www.anthropic.com/research"),
        ("deepmind_research", "https://deepmind.google/research/"),
        ("google_pubs", "https://research.google/pubs/?category=2025&search=language+model"),
        ("google_october", "https://www.research.google/blog/2025/10/"),
        ("meta_research", "https://ai.meta.com/research/"),
        ("qwen_blog", "https://qwenlm.github.io/"),
        ("qwen_research", "https://qwen.ai/research"),
        ("deepseek_home", "https://www.deepseek.com/"),
        ("deepseek_news", "https://www.deepseek.com/news/"),
        ("moonshot_blog", "https://platform.kimi.com/blog"),
        ("moonshot_org", "https://github.com/MoonshotAI"),
        ("hunyuan_research", "https://hunyuan.tencent.com/research"),
        ("zai_research", "https://www.zhipuai.cn/zh/research"),
        ("zai_release", "https://docs.z.ai/release-notes/new-released"),
        ("seed_research", "https://seed.bytedance.com/en/research"),
        ("seed_papers", "https://seed.bytedance.com/en/public_papers"),
        ("ernie_blog", "https://ernie.baidu.com/blog/zh/"),
        ("mimo_home", "https://mimo.xiaomi.com/"),
        ("minimax_blog", "https://www.minimax.io/blog"),
        ("minimax_cn", "https://www.minimaxi.com/blog"),
        ("minimax_agent", "https://agent.minimax.io/docs/techblog"),
    ]:
        fetch(name, url)
    topics = {
        "architecture": '(ti:"language model" OR ti:Transformer OR ti:MoE OR ti:"diffusion model")',
        "systems": '(ti:LLM OR ti:"large language" OR ti:GPU) AND (all:inference OR all:serving OR all:training OR all:kernel)',
        "agents": '(ti:agent OR ti:reasoning OR ti:retrieval) AND (all:"language model" OR all:LLM)',
        "multimodal": '(ti:multimodal OR ti:"vision-language" OR ti:"world model" OR ti:"vision language action")',
    }
    for name, topic in topics.items():
        query = '(' + topic + ') AND submittedDate:[202510170100 TO 202510180100]'
        params = dict(search_query=query, start=0, max_results=50,
                      sortBy="submittedDate", sortOrder="ascending")
        fetch("arxiv_" + name, "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
