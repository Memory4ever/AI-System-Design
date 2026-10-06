"""Fetch only this Daily's native feeds and bounded topic discovery pages."""
import datetime as dt
import json
import pathlib
import subprocess
import time
import urllib.parse
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).parent
START = dt.datetime(2025, 11, 25, 1, tzinfo=dt.timezone.utc)
END = dt.datetime(2025, 11, 26, 1, tzinfo=dt.timezone.utc)


def fetch(name, url, extra=()):
    target = ROOT / name
    cmd = ["curl", "--max-time", "25", "-L", "-sS", "-A", "Mozilla/5.0", *extra,
           url, "-o", str(target), "-w", "%{http_code}"]
    run = subprocess.run(cmd, capture_output=True, text=True)
    receipt = {"url": url, "extra": list(extra), "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0,
               "stop": "one specified page; no recursive expansion"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps({"file": name, **receipt}, ensure_ascii=False), flush=True)
    return target if run.returncode == 0 and run.stdout == "200" else None


rss = fetch("openai-rss.xml", "https://openai.com/news/rss.xml")
if rss:
    items = ET.parse(rss).findall("./channel/item")
    matches = []
    for item in items:
        date = item.findtext("pubDate")
        if date and START <= parsedate_to_datetime(date) < END:
            matches.append({"title": item.findtext("title"), "url": item.findtext("link"), "pubDate": date})
    result = {"items": len(items), "window_utc": [START.isoformat(), END.isoformat()], "hits": matches,
              "missing_pubDate": sum(not x.findtext("pubDate") for x in items)}
    (ROOT / "openai-window.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False), flush=True)
fetch("anthropic.html", "https://www.anthropic.com/research")
fetch("productivity.html", "https://www.anthropic.com/research/estimating-productivity-gains")
for kind in (1, 2):
    params = urllib.parse.urlencode({"article_type": kind, "publish_year": 2025, "count": 20,
                                   "page_token": 0, "order_desc": "true"})
    fetch(f"seed-type{kind}-page0.json", "https://seed.bytedance.com/api/get_article_list_v2?" + params,
          ("-H", "x-tt-locale: US"))
fetch("hunyuan-blog-page1.json", "https://api.hunyuan.tencent.com/api/blog/publicList",
      ("-H", "Content-Type: application/json", "-d", '{"pageNum":1,"pageSize":20,"renderType":0}'))
fetch("deepseek-updates.html", "https://api-docs.deepseek.com/updates")

topics = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:transformer OR ti:"mixture of experts")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR ti:GPU OR ti:kernel)',
    "agents": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:"language model" OR ti:agent OR ti:retrieval)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO) AND (ti:"foundation model" OR ti:"world model" OR ti:"vision language" OR ti:"vision-language-action")',
}
for name, topic in topics.items():
    query = topic + " AND submittedDate:[202511211900 TO 202511241900]"
    params = {"search_query": query, "start": 0, "max_results": 100, "sortBy": "submittedDate", "sortOrder": "descending"}
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    path = fetch("arxiv-" + name + "-page0.xml", url)
    if path:
        ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
        root = ET.parse(path).getroot()
        entries = root.findall("a:entry", ns)
        result = {"parameters": params, "total_results": root.findtext("o:totalResults", namespaces=ns),
                  "returned": len(entries), "window_role": "submission discovery only; not first-public proof",
                  "titles": [{"id": x.findtext("a:id", namespaces=ns), "title": x.findtext("a:title", namespaces=ns)} for x in entries]}
        (ROOT / ("arxiv-" + name + "-query.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
        print(json.dumps({k: v for k, v in result.items() if k != "titles"}, ensure_ascii=False), flush=True)
    time.sleep(3)
