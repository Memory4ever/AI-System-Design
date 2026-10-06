"""Retry only failed day-07 queries and fetch identified official events."""
from pathlib import Path
import json
import subprocess
import sys
import time

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
for name in ["arxiv-model", "arxiv-systems", "arxiv-agent", "arxiv-multimodal", "titles-cs.CL", "titles-cs.CV", "titles-cs.DC", "titles-cs.PL"]:
    receipt = json.loads((d / (name + ".receipt.json")).read_text())
    url = receipt["url"].replace("export.arxiv.org", "arxiv.org")
    subprocess.run([sys.executable, str(fetch), str(d), name + "-retry", url], check=True)
    time.sleep(3)
for name, url in {
    "petri": "https://www.anthropic.com/research/petri-open-source-auditing",
    "codex-ga": "https://openai.com/index/codex-now-generally-available/",
    "apps-sdk": "https://openai.com/index/introducing-apps-in-chatgpt/",
    "amd": "https://openai.com/index/openai-amd-strategic-partnership/",
}.items():
    subprocess.run([sys.executable, str(fetch), str(d), name, url], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, d.glob("*.raw"))], check=True)
