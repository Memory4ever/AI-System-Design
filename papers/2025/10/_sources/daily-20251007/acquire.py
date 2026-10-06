"""Fresh day-07 requests; reuse transport code, never another day's pool."""
from pathlib import Path
import re
import runpy
import subprocess
import sys
from urllib.parse import urlencode

d = Path(__file__).parent
sys.argv = [str(d / "acquire.py"), str(d), "20251006"]
runpy.run_path(str(d.parent / "daily-20251005" / "acquire.py"), run_name="__main__")
fetch = d.parent / "daily-20251002" / "fetch.py"
for name, url in {
    "openai-rss": "https://openai.com/news/rss.xml",
    "qwen-articles": "https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US",
    "qwen-legacy": "https://qwen.ai/api/page_config?code=research.research-list",
    "qwen-research-js": "https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_research-index.js",
    "qwen-service-js": "https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/969.js",
}.items():
    subprocess.run([sys.executable, str(fetch), str(d), name, url], check=True)
for source, pattern, prefix in [
    ("deepseek-news", r'src="([^\"]+/news/page-[^\"]+\.js)"', "https://www.deepseek.com"),
    ("zai-research", r'src="([^\"]+/research/page-[^\"]+\.js)"', "https://www.zhipuai.cn"),
]:
    urls = re.findall(pattern, (d / (source + ".raw")).read_text())
    if urls:
        subprocess.run([sys.executable, str(fetch), str(d), source + "-js", prefix + urls[0]], check=True)
for cat in ["cs.CL", "cs.CV", "cs.DC", "cs.PL", "cs.IR"]:
    q = "submittedDate:[202510060000 TO 202510062359] AND cat:" + cat
    url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": q, "start": 0, "max_results": 25, "sortBy": "submittedDate", "sortOrder": "ascending"})
    subprocess.run([sys.executable, str(fetch), str(d), "titles-" + cat, url], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, d.glob("*.raw"))], check=True)
