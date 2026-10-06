"""Non-author bounded original reads; no annual candidate expansion."""
from pathlib import Path
import subprocess
import sys

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
targets = {
    "HY-deepmind-pubs": "https://deepmind.google/research/publications/?page=2",
    "HY-qwen-articles": "https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US",
    "HY-qwen-legacy": "https://qwen.ai/api/page_config?code=research.research-list",
}
for short in ["09004", "09717", "09260", "09033", "09269"]:
    targets["HY-abs-2510." + short + "v1"] = "https://arxiv.org/abs/2510." + short + "v1"
for short in ["09004", "09008", "09714", "09717", "09253", "09259", "09260", "09033", "09062", "09269", "09849"]:
    targets["HY-core-2510." + short + "v1"] = "https://arxiv.org/html/2510." + short + "v1"
for name, url in targets.items():
    subprocess.run([sys.executable, str(fetch), str(d), name, url], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, d.glob("HY-*.raw"))], check=True)
