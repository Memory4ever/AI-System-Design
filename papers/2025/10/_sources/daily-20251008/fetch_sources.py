"""Save original responses for this day's bounded source recovery."""
import json
import pathlib
import urllib.request
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).parent
URLS = {
    "openai": "https://openai.com/research/",
    "openai_rss": "https://openai.com/news/rss.xml",
    "anthropic": "https://www.anthropic.com/research",
    "deepmind": "https://deepmind.google/research/",
    "google_pubs": "https://research.google/pubs/?year=2025",
    "meta": "https://ai.meta.com/research/",
    "qwen": "https://qwenlm.github.io/",
    "deepseek": "https://www.deepseek.com/",
    "moonshot": "https://platform.kimi.com/blog",
    "moonshot_org": "https://github.com/MoonshotAI",
    "hunyuan": "https://hunyuan.tencent.com/research",
    "zai": "https://www.zhipuai.cn/zh/research",
    "zai_releases": "https://docs.z.ai/release-notes/new-released",
    "seed": "https://seed.bytedance.com/en/research",
    "seed_papers": "https://seed.bytedance.com/en/public_papers",
    "ernie": "https://ernie.baidu.com/blog/zh/",
    "mimo": "https://mimo.xiaomi.com/",
    "minimax": "https://www.minimax.io/blog",
    "minimax_zh": "https://www.minimaxi.com/blog",
    "minimax_agent": "https://agent.minimax.io/docs/techblog",
}

if __name__ == "__main__":
    manifest = []
    for name, url in URLS.items():
        row = {"name": name, "url": url, "checked_at": datetime.now(timezone.utc).isoformat()}
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=12) as response:
                body = response.read()
                (ROOT / (name + ".raw")).write_bytes(body)
                row.update(status=response.status, final_url=response.url, bytes=len(body))
        except Exception as error:
            row["error"] = str(error)
        manifest.append(row)
        print(json.dumps(row), flush=True)
    (ROOT / "fetch_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
