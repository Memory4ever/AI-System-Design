"""Own-day bounded upstream requests. Responses do not establish semantic review."""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlencode

d = Path(sys.argv[1])
day = sys.argv[2]
fetch = Path(__file__).parent.parent / "daily-20251002" / "fetch.py"

def get(name, url, *extra):
    subprocess.run([sys.executable, str(fetch), str(d), name, url, *extra], check=True)

entries = {
    "openai-research": "https://openai.com/research/",
    "anthropic-research": "https://www.anthropic.com/research",
    "deepmind-research": "https://deepmind.google/research/",
    "google-pubs": "https://research.google/pubs/?search=language%20model&category=2025",
    "meta-research": "https://ai.meta.com/research/",
    "qwen": "https://qwenlm.github.io/blog/",
    "qwen-new": "https://qwen.ai/research",
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
    get(name, url)

for name, url in {
    "deepseek-news": "https://www.deepseek.com/news/",
    "zai-page2": "https://www.zhipuai.cn/zh/research?page=2",
    "ernie-page2": "https://ernie.baidu.com/blog/zh/page/2/",
    "deepmind-pubs-history": "https://deepmind.google/research/publications/page/2/",
    "google-october": "https://www.research.google/blog/2025/10/",
    "google-october-page2": "https://www.research.google/blog/2025/10/?page=2",
    "mimo-paper-js": "https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js",
}.items():
    get(name, url)
get("hunyuan-page1", "https://api.hunyuan.tencent.com/api/blog/publicList",
    "--json-body", '{"pageNum":1,"pageSize":20,"renderType":0}')
for token in (0,20,40,60,80):
    get("seed-papers-us"+str(token), "https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&order_desc=false&mode=1&page_token="+str(token), "--header", "x-tt-locale: US")
for token in (0,20,40):
    get("seed-blogs"+str(token), "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&order_desc=false&mode=1&page_token="+str(token))

for source, pattern, prefix in (
    ("deepseek-news", r'src="([^"]+/news/page-[^"]+\.js)"', "https://www.deepseek.com"),
    ("zai-research", r'src="([^"]+/research/page-[^"]+\.js)"', "https://www.zhipuai.cn"),
    ("seed-papers", r'src="(//[^\"]+/main\.[^\"]+\.js)"', "https:"),
):
    html = (d/(source+".raw")).read_text(errors="replace")
    urls = re.findall(pattern, html)
    if urls:
        get(source+"-js", prefix+urls[0])
anth = (d/"anthropic-research.raw").read_text(errors="replace")
if '/_next/static/chunks/00lwoet3xtw-4.js' in anth:
    get("anthropic-list-js", "https://www.anthropic.com/_next/static/chunks/00lwoet3xtw-4.js")
for name,topic in {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:LLM OR ti:transformer OR ti:"mixture of experts") AND (ti:architecture OR ti:training OR ti:optimization OR ti:reasoning OR ti:attention OR ti:compression OR ti:sparsity)',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND (all:"language model" OR all:LLM OR all:transformer) AND (ti:GPU OR ti:kernel OR ti:parallel OR ti:serving OR ti:inference OR ti:quantization OR ti:cache OR ti:communication)',
    "agent": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:"language model" OR all:LLM) AND (ti:agent OR ti:RAG OR ti:retrieval OR ti:memory OR ti:tool OR ti:planning)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND (ti:"vision language" OR ti:"vision-language" OR ti:VLA OR ti:"world model" OR ti:"multimodal language" OR ti:"diffusion model")',
}.items():
    query = f'submittedDate:[{day}0000 TO {day}2359] AND ({topic})'
    get("arxiv-"+name, "https://export.arxiv.org/api/query?"+urlencode({"search_query":query,"start":0,"max_results":40,"sortBy":"submittedDate","sortOrder":"ascending"}))
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str,d.glob("*.raw"))], check=True)
