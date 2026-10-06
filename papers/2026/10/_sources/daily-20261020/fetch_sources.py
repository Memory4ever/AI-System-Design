"""Bounded official-entry retrieval for Oct 19 BJT; no arXiv scanning."""
import datetime
import gzip
import json
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

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
    ("seed", "https://seed.bytedance.com/en/research"),
    ("ernie", "https://ernie.baidu.com/blog/zh/"),
    ("mimo", "https://mimo.xiaomi.com/"),
    ("minimax", "https://www.minimax.io/blog"),
]

class Visible(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts, self.skip = [], 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "div", "h1", "h2", "h3", "li", "time", "dt", "dd", "item"):
            self.parts.append("\n")
        if tag in ("a", "iframe"):
            self.parts.extend(" [" + v + "] " for k, v in attrs if k in ("href", "src"))
    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def fetch(item):
    name, url = item
    record = dict(name=name, url=url, checked_at=datetime.datetime.now(datetime.timezone.utc).isoformat())
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=15) as response:
            raw = response.read()
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            record.update(status=response.status, final_url=response.url, bytes=len(raw), headers=dict(response.headers))
            (ROOT / (name + ".raw.html")).write_bytes(raw)
            parser = Visible()
            parser.feed(raw.decode("utf-8", errors="replace"))
            visible = "\n".join(line.strip() for line in "".join(parser.parts).splitlines() if line.strip())
            (ROOT / (name + ".visible.txt")).write_text(visible)
            record["visible_chars"] = len(visible)
    except Exception as error:
        record["error"] = str(error)
    (ROOT / (name + ".request.json")).write_text(json.dumps(record, indent=2))
    print(json.dumps({k: v for k, v in record.items() if k != "headers"}), flush=True)
    return record

if __name__ == "__main__":
    items = SOURCES if len(sys.argv) == 1 else [(sys.argv[i], sys.argv[i + 1]) for i in range(1, len(sys.argv), 2)]
    for item in items:
        fetch(item)
