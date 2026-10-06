"""Finite Nov27 catalog boundaries and named primary date metadata only."""
import datetime as dt
import json
import pathlib
import re
import subprocess
import urllib.parse
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent


def fetch(name, url, extra=()):
    target = ROOT / name
    run = subprocess.run(["curl", "--max-time", "12", "-L", "-sS", "-A", "Mozilla/5.0", *extra,
                          url, "-o", str(target), "-w", "%{http_code}"], capture_output=True, text=True)
    result = {"url": url, "extra": list(extra), "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
              "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
              "bytes": target.stat().st_size if target.exists() else 0,
              "stop": "one named page or exact DOI, no recursive/full-month processing"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({"file": name, **result}, ensure_ascii=False), flush=True)
    return target if run.returncode == 0 and run.stdout == "200" else None


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.script = None
        self.text = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script":
            self.script = []
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_data(self, value):
        if self.script is not None:
            self.script.append(value)
        else:
            value = value.strip()
            if value:
                self.text.append(value)

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.scripts.append("".join(self.script))
            self.script = None


def flight_objects(page):
    chunks = []
    decoder = json.JSONDecoder()
    for script in page.scripts:
        marker = "self.__next_f.push("
        offset = 0
        while marker in script[offset:]:
            pos = script.index(marker, offset) + len(marker)
            try:
                value, size = decoder.raw_decode(script[pos:])
                if isinstance(value, list) and len(value) > 1 and isinstance(value[1], str):
                    chunks.append(value[1])
                offset = pos + size
            except ValueError:
                break
    stream = "".join(chunks).encode("utf-8")
    pos = 0
    objects = []
    text_frames = 0
    while pos < len(stream):
        colon = stream.find(b":", pos)
        if colon < 0:
            break
        start = colon + 1
        if stream[start:start + 1] == b"T":
            comma = stream.find(b",", start)
            try:
                size = int(stream[start + 1:comma], 16)
                pos = comma + 1 + size
                text_frames += 1
                continue
            except ValueError:
                pass
        end = stream.find(b"\n", start)
        end = len(stream) if end < 0 else end
        payload = stream[start:end].decode("utf-8", errors="replace")
        try:
            objects.append(json.loads(payload))
        except ValueError:
            pass
        pos = end + 1
    return objects, len(chunks), text_frames


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


for name in ("anthropic.html", "deepseek-updates.html", "moonshot.html", "mimo.html", "qwen-old.html"):
    page = Page()
    page.feed((ROOT / name).read_text())
    if name == "anthropic.html":
        objects, chunks, frames = flight_objects(page)
        rows = {}
        for obj in objects:
            for value in walk(obj):
                if value.get("_type") == "post" and value.get("publishedOn"):
                    slug = value.get("slug", {})
                    slug = slug.get("current") if isinstance(slug, dict) else slug
                    rows[slug] = {"slug": slug, "publishedOn": value["publishedOn"], "title": value.get("title")}
        target = [x for x in rows.values() if "2025-11" in x["publishedOn"] or x["publishedOn"].startswith("2025-12-01")]
        result = {"transport_chunks": chunks, "text_frames": frames, "unique_dated": len(rows),
                  "target_neighbors": sorted(target, key=lambda x: x["publishedOn"]),
                  "role": "current official catalog metadata, not deletion completeness"}
    else:
        result = {"text": page.text, "pagination_links": [u for u in page.links if "page" in u or "More" in u]}
    (ROOT / (name + ".metadata.json")).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(name, json.dumps(result, ensure_ascii=False)[:9000], flush=True)

for kind in (1, 2):
    obj = json.loads((ROOT / f"seed-type{kind}-page0.json").read_text())
    rows = []
    for item in obj["sub_article_list"]:
        meta = item["ArticleMeta"]
        rows.append({"title": item["ArticleSubContentEn"]["Title"], "utc": dt.datetime.fromtimestamp(
            meta["PublishDate"] / 1000, dt.timezone.utc).isoformat(), "date_ms": meta["PublishDate"],
            "pinned": meta["IsPinned"]})
    result = {"type": kind, "returned": len(rows), "total": obj["total"], "has_more": obj["has_more"],
              "next_page_token": obj["next_page_token"], "metadata_only": rows}
    (ROOT / f"seed-type{kind}-metadata.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print("SEED", json.dumps(result, ensure_ascii=False), flush=True)
    params = urllib.parse.urlencode({"article_type": kind, "publish_year": 2025, "count": 20,
                                   "page_token": obj["next_page_token"], "order_desc": "true"})
    fetch(f"seed-type{kind}-page20.json", "https://seed.bytedance.com/api/get_article_list_v2?" + params,
          ("-H", "x-tt-locale: US"))

jobs = [
    ("zai-page2.html", "https://www.zhipuai.cn/zh/research?page=2"),
    ("deepmind-page4.html", "https://deepmind.google/blog/?page=4"),
    ("deepmind-page5.html", "https://deepmind.google/blog/?page=5"),
    ("arxiv-csDC-titles.html", "https://arxiv.org/list/cs.DC/2025-11?skip=150&show=50"),
    ("mixpanel-original.html", "https://mixpanel.com/blog/sms-security-incident/"),
]
for name, url in jobs:
    fetch(name, url)

for pid in ("2511.20100", "2511.20172", "2511.20038", "2511.19997", "2511.20194", "2511.19822", "2511.19705", "2511.19959"):
    path = fetch("date-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
    if path:
        value = json.loads(path.read_text())["data"]["attributes"]
        print("DATE", pid, json.dumps({k: value.get(k) for k in ("created", "registered", "dates")}), flush=True)
