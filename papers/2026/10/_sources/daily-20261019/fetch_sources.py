"""Bounded read-only source retrieval for the 2026-10-18 BJT window."""
import concurrent.futures
import datetime
import json
import gzip
from pathlib import Path
import urllib.request
from html.parser import HTMLParser

ROOT = Path(__file__).parent
SOURCES = [
    ("openai", "https://openai.com/research/"),
    ("anthropic", "https://www.anthropic.com/research"),
    ("deepmind", "https://deepmind.google/research/"),
    ("google", "https://research.google/pubs/"),
    ("meta", "https://ai.meta.com/research/"),
    ("qwen", "https://qwenlm.github.io/"),
    ("deepseek", "https://www.deepseek.com/"),
    ("moonshot", "https://platform.kimi.com/blog"),
    ("hunyuan", "https://hunyuan.tencent.com/research"),
    ("zai", "https://www.zhipuai.cn/zh/research"),
    ("seed", "https://seed.bytedance.com/en/public_papers"),
    ("ernie", "https://ernie.baidu.com/blog/zh/"),
    ("mimo", "https://mimo.xiaomi.com/"),
    ("minimax", "https://www.minimax.io/blog"),
    ("arxiv", "https://arxiv.org/list/cs.CL/2026-10?show=2000"),
]

class Visible(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "div", "h1", "h2", "h3", "li", "time", "dt", "dd"):
            self.parts.append("\n")
        if tag == "a":
            self.parts.extend(" [" + v + "] " for k, v in attrs if k == "href")
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def get(item):
    name, url = item
    record = dict(name=name, url=url, checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=15) as response:
            raw = response.read()
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            record.update(status=response.status, final_url=response.url, bytes=len(raw))
            (ROOT / (name + ".raw.html")).write_bytes(raw)
            parser = Visible()
            parser.feed(raw.decode("utf-8", errors="replace"))
            visible = "\n".join(line.strip() for line in "".join(parser.parts).splitlines() if line.strip())
            (ROOT / (name + ".visible.txt")).write_text(visible)
            record["visible_chars"] = len(visible)
    except Exception as error:
        record["error"] = str(error)
    print(json.dumps(record), flush=True)
    return record

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        SOURCES = [(sys.argv[i], sys.argv[i + 1]) for i in range(1, len(sys.argv), 2)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        records = list(pool.map(get, SOURCES))
    (ROOT / ("fetch_results.json" if len(sys.argv) == 1 else "fallback_results.json")).write_text(json.dumps(records, indent=2))
