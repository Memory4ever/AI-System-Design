"""Fresh Nov28 primary checks; each response is bounded and independently saved."""
import datetime as dt
import json
import pathlib
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).parent
START = dt.datetime(2025, 11, 27, 1, tzinfo=dt.timezone.utc)
END = dt.datetime(2025, 11, 28, 1, tzinfo=dt.timezone.utc)


def fetch(name, url, extra=()):
    target = ROOT / name
    run = subprocess.run(["curl", "--max-time", "12", "-L", "-sS", "-A", "Mozilla/5.0", *extra,
                          url, "-o", str(target), "-w", "%{http_code}"], capture_output=True, text=True)
    receipt = {"url": url, "extra": list(extra), "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0,
               "stop": "one named entry; not recursive or historical completeness"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps({"file": name, **receipt}, ensure_ascii=False), flush=True)
    return target if run.returncode == 0 and run.stdout == "200" else None


for name, url in (
    ("openai-research.html", "https://openai.com/research/"),
    ("openai-rss.xml", "https://openai.com/news/rss.xml"),
    ("anthropic.html", "https://www.anthropic.com/research"),
    ("deepmind.html", "https://deepmind.google/research/"),
    ("google-pubs.html", "https://research.google/pubs/?year=2025"),
    ("google-november.html", "https://research.google/blog/?year=2025&month=11"),
    ("meta.html", "https://ai.meta.com/research/"),
    ("qwen-old.html", "https://qwenlm.github.io/"),
    ("qwen-new.html", "https://qwen.ai/blog"),
    ("deepseek.html", "https://www.deepseek.com/"),
    ("deepseek-updates.html", "https://api-docs.deepseek.com/updates"),
    ("moonshot.html", "https://platform.kimi.com/blog"),
    ("hunyuan-research.html", "https://hunyuan.tencent.com/research"),
    ("zai.html", "https://www.zhipuai.cn/zh/research"),
    ("seed.html", "https://seed.bytedance.com/en/research"),
    ("ernie.html", "https://ernie.baidu.com/blog/zh/"),
    ("mimo.html", "https://mimo.xiaomi.com/"),
    ("minimax-en.html", "https://www.minimax.io/blog"),
    ("minimax-cn.html", "https://www.minimaxi.com/blog"),
    ("minimax-agent.html", "https://agent.minimax.io/docs/techblog"),
):
    fetch(name, url)

try:
    items = ET.parse(ROOT / "openai-rss.xml").findall("./channel/item")
    matches = [{"title": x.findtext("title"), "url": x.findtext("link"), "pubDate": x.findtext("pubDate")}
               for x in items if x.findtext("pubDate") and START <= parsedate_to_datetime(x.findtext("pubDate")) < END]
    result = {"items": len(items), "missing_pubDate": sum(not x.findtext("pubDate") for x in items),
              "window_utc": [START.isoformat(), END.isoformat()], "hits": matches}
    (ROOT / "openai-window.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print("RSS", json.dumps(result, ensure_ascii=False), flush=True)
except (OSError, ET.ParseError) as error:
    print("RSS parse failed", str(error), flush=True)

for kind in (1, 2):
    params = urllib.parse.urlencode({"article_type": kind, "publish_year": 2025, "count": 20,
                                   "page_token": 0, "order_desc": "true"})
    fetch(f"seed-type{kind}-page0.json", "https://seed.bytedance.com/api/get_article_list_v2?" + params,
          ("-H", "x-tt-locale: US"))

topics = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:transformer OR ti:"mixture of experts")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR ti:GPU OR ti:kernel)',
    "agents": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:"tool calling" OR ti:memory OR ti:"context management") AND (all:"language model" OR all:LLM)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO) AND (ti:"foundation model" OR ti:"world model" OR ti:"vision language" OR ti:"vision-language-action")',
}
for name, topic in topics.items():
    params = {"search_query": topic + " AND submittedDate:[202511251900 TO 202511261900]",
              "start": 0, "max_results": 50, "sortBy": "submittedDate", "sortOrder": "descending"}
    path = fetch("arxiv-" + name + "-page0.xml", "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
    if path:
        ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
        root = ET.parse(path).getroot()
        rows = root.findall("a:entry", ns)
        result = {"parameters": params, "total_results": root.findtext("o:totalResults", namespaces=ns),
                  "returned": len(rows), "role": "submission discovery, not public evidence",
                  "entries": [{"id": x.findtext("a:id", namespaces=ns),
                               "title": x.findtext("a:title", namespaces=ns),
                               "abstract": x.findtext("a:summary", namespaces=ns)} for x in rows]}
        (ROOT / ("arxiv-" + name + "-query.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print("ARXIV", json.dumps({k: v for k, v in result.items() if k != "entries"}), flush=True)
    time.sleep(3)
