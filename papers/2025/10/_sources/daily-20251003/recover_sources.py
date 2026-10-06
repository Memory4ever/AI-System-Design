"""Retrieve this day's source endpoints, preserving the actual response and request."""
from pathlib import Path
import re
import subprocess
import sys

directory = Path(sys.argv[1])
fetch = Path(__file__).parent.parent / "daily-20251002" / "fetch.py"

def retrieve(name, url, *extra):
    subprocess.run([sys.executable, str(fetch), str(directory), name, url, *extra], check=True)

seed = (directory / "seed-papers.raw").read_text()
bundle = re.findall(r'src="(//[^\"]+/main\.[^\"]+\.js)"', seed)[0]
retrieve("seed-js", "https:" + bundle)
for token in [0, 20, 40, 60, 80]:
    retrieve("seed-papers-us" + str(token), "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&order_desc=false&mode=1&page_token=" + str(token), "--header", "x-tt-locale: US")
zai = (directory / "zai-research.raw").read_text()
bundle = re.findall(r'src="([^\"]+/research/page-[^\"]+\.js)"', zai)[0]
retrieve("zai-page-js", "https://www.zhipuai.cn" + bundle)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), str(directory / "deepseek-news.raw"), str(directory / "zai-page2.raw")], check=True)
