"""Date-scoped retrieval helper; stored payloads are evidence, not verdicts."""
import datetime
import json
import pathlib
import html
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

destination = pathlib.Path(__file__).resolve().parent
name, mode, value = sys.argv[1:]
if mode == "query":
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"search_query": value, "start": 0, "max_results": 150,
         "sortBy": "submittedDate", "sortOrder": "ascending"})
elif mode == "ids":
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(
        {"id_list": value, "max_results": 200})
else:
    url = value
request = url
if mode == "post":
    spec = json.loads(value)
    url = spec["url"]
    request = urllib.request.Request(url, data=json.dumps(spec["body"]).encode(),
                                     headers={"Content-Type": "application/json"})
with urllib.request.urlopen(request, timeout=50) as response:
    raw = response.read().decode("utf-8")
payload = {"url": url, "checked": datetime.datetime.now().astimezone().isoformat(),
           "raw": raw}
if mode == "html":
    visible = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', raw, flags=re.S)
    visible = re.sub(r'</(?:p|h[1-6]|div|li|tr|section)>', '\n', visible)
    visible = html.unescape(re.sub(r'<[^>]+>', ' ', visible))
    payload['text'] = '\n'.join(' '.join(line.split()) for line in visible.splitlines() if line.strip())
if mode == "abs":
    abstract = re.search(r'<blockquote class="abstract[^>]*>(.*?)</blockquote>', raw, re.S)
    title = re.search(r'<h1 class="title[^>]*>(.*?)</h1>', raw, re.S)
    history = re.search(r'<div class="submission-history[^>]*>(.*?)</div>', raw, re.S)
    for key, match in (("title", title), ("abstract", abstract), ("history", history)):
        payload[key] = html.unescape(re.sub(r'<[^>]+>', ' ', match.group(1))) if match else "NOT_EXTRACTED"
if mode in ("query", "ids"):
    root = ET.fromstring(raw)
    namespaces = {"a": "http://www.w3.org/2005/Atom",
                  "o": "http://a9.com/-/spec/opensearch/1.1/"}
    payload["total"] = root.findtext("o:totalResults", namespaces=namespaces)
    payload["entries"] = [
        {key: entry.findtext("a:" + key, namespaces=namespaces)
         for key in ("id", "title", "summary", "published", "updated")}
        for entry in root.findall("a:entry", namespaces)]
(destination / name).write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({key: value for key, value in payload.items()
                  if key not in ("raw", "entries", "text")}, ensure_ascii=False))
for entry in payload.get("entries", []):
    print(entry["id"], " ".join(entry["title"].split()))
