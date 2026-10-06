"""Bounded retrieval; saved data is not a claim of semantic review."""
import datetime as dt
from html.parser import HTMLParser
import json
from pathlib import Path
import subprocess
import sys

directory = Path(sys.argv[1])
entries = {
    "openai-research": "https://openai.com/research/",
    "anthropic-research": "https://www.anthropic.com/research",
    "deepmind-research": "https://deepmind.google/research/",
    "google-pubs": "https://research.google/pubs/?year=2025&query=language",
    "meta-research": "https://ai.meta.com/research/",
    "qwen": "https://qwenlm.github.io/blog/",
    "deepseek": "https://www.deepseek.com/",
    "moonshot-blog": "https://platform.kimi.com/blog",
    "moonshot-org": "https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=created&direction=desc",
    "hunyuan-research": "https://hunyuan.tencent.com/research",
    "zai-research": "https://www.zhipuai.cn/zh/research",
    "seed-research": "https://seed.bytedance.com/en/research",
    "seed-papers": "https://seed.bytedance.com/en/public_papers",
    "ernie-blog": "https://ernie.baidu.com/blog/zh/",
    "mimo": "https://mimo.xiaomi.com/",
    "minimax-blog": "https://www.minimax.io/blog",
    "minimax-cn": "https://www.minimaxi.com/blog",
    "minimax-agent": "https://agent.minimax.io/docs/techblog",
}
for name, url in entries.items():
    subprocess.run([sys.executable, str(Path(__file__).with_name("fetch.py")), str(directory), name, url], check=True)

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("h1", "h2", "h3", "p", "li", "tr", "div"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)

for name in entries:
    raw = directory / (name + ".raw")
    if not raw.exists():
        continue
    parser = Text()
    parser.feed(raw.read_bytes().decode("utf-8", "replace"))
    (directory / (name + ".text.txt")).write_text("\n".join(line.strip() for line in "".join(parser.parts).splitlines() if line.strip()) + "\n")
