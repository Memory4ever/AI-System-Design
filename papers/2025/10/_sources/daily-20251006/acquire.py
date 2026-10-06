"""Reuse request mechanisms only; all responses belong to day 06."""
from pathlib import Path
import runpy
import subprocess
import sys
from urllib.parse import urlencode

d = Path(__file__).parent
sys.argv = [str(d / "acquire.py"), str(d), "20251005"]
runpy.run_path(str(d.parent / "daily-20251005" / "acquire.py"), run_name="__main__")
fetch = d.parent / "daily-20251002" / "fetch.py"
for name, url in {
    "qwen-articles": "https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US",
    "qwen-legacy": "https://qwen.ai/api/page_config?code=research.research-list",
    "qwen-research-js": "https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_research-index.js",
    "qwen-service-js": "https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/969.js",
}.items():
    subprocess.run([sys.executable, str(fetch), str(d), name, url], check=True)
for cat in ["cs.CL", "cs.CV", "cs.DC", "cs.PL", "cs.IR"]:
    q = "submittedDate:[202510050000 TO 202510052359] AND cat:" + cat
    url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": q, "start": 0, "max_results": 25, "sortBy": "submittedDate", "sortOrder": "ascending"})
    subprocess.run([sys.executable, str(fetch), str(d), "titles-"+cat, url], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str,d.glob("*.raw"))], check=True)
