"""Sequential capture of today's explicitly selected Daily entry points."""

import subprocess
import sys
from pathlib import Path

fetch = str(Path(__file__).with_name("fetch_raw.py"))
entries = [
    ("raw-openai-research.html", "https://openai.com/research/"),
    ("raw-openai-rss.xml", "https://openai.com/news/rss.xml"),
    ("raw-anthropic-research.html", "https://www.anthropic.com/research"),
    ("raw-deepmind-research.html", "https://deepmind.google/research/"),
    ("raw-google-pubs.html", "https://research.google/pubs/"),
    ("raw-google-blog-2025.html", "https://research.google/blog/2025/"),
    ("raw-meta-research.html", "https://ai.meta.com/research/"),
    ("raw-qwen-old.html", "https://qwenlm.github.io/"),
    ("raw-qwen-research.html", "https://qwen.ai/research"),
    ("raw-deepseek.html", "https://www.deepseek.com/"),
    ("raw-deepseek-updates.html", "https://api-docs.deepseek.com/updates"),
    ("raw-moonshot-blog.html", "https://platform.kimi.com/blog"),
    ("raw-hunyuan-research.html", "https://hunyuan.tencent.com/research"),
    ("raw-hunyuan-p1.json", "https://api.hunyuan.tencent.com/api/blog/publicList", '{"pageNum":1,"pageSize":20,"renderType":0}'),
    ("raw-zai-research.html", "https://www.zhipuai.cn/zh/research"),
    ("raw-zai-release.html", "https://docs.z.ai/release-notes/new-released"),
    ("raw-seed-research.html", "https://seed.bytedance.com/en/research"),
    ("raw-seed-papers.html", "https://seed.bytedance.com/en/public_papers"),
    ("raw-ernie-p1.html", "https://ernie.baidu.com/blog/zh/"),
    ("raw-mimo-home.html", "https://mimo.xiaomi.com/"),
    ("raw-minimax-en.html", "https://www.minimax.io/blog"),
    ("raw-minimax-zh.html", "https://www.minimaxi.com/blog"),
    ("raw-minimax-agent-tech.html", "https://agent.minimax.io/docs/techblog"),
]
for args in entries:
    subprocess.run([sys.executable, fetch, *args], check=True)
