"""Bounded source recovery and metadata projection for Nov26 only."""
import datetime as dt
import json
import pathlib
import subprocess
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent
jobs = [
    ("arxiv-csDC-target-title-page.html", "https://arxiv.org/list/cs.DC/2025-11?skip=250&show=50"),
    ("hunyuan-ocr-repo.json", "https://api.github.com/repos/Tencent-Hunyuan/HunyuanOCR"),
    ("hunyuan-ocr-model.json", "https://huggingface.co/api/models/tencent/HunyuanOCR"),
]
for name, url in jobs:
    target = ROOT / name
    run = subprocess.run(["curl", "--max-time", "18", "-L", "-sS", "-A", "Mozilla/5.0", url,
                          "-o", str(target), "-w", "%{http_code}"], capture_output=True, text=True)
    receipt = {"url": url, "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0,
               "stop": "one specified page; creation/submission is not automatic public proof"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps({"file": name, **receipt}, ensure_ascii=False), flush=True)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.headings = []
        self.active_heading = False
        self.heading_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("h2", "h3"):
            self.active_heading = True
            self.heading_text = []

    def handle_data(self, data):
        if self.active_heading:
            self.heading_text.append(data)

    def handle_endtag(self, tag):
        if tag in ("h2", "h3") and self.active_heading:
            self.headings.append(" ".join("".join(self.heading_text).split()))
            self.active_heading = False


for name in ("deepmind-page4.html", "deepseek-updates.html"):
    page = Page()
    page.feed((ROOT / name).read_text())
    print(name, json.dumps({"headings": page.headings,
                           "specific_links": [x for x in page.links if "nano-banana-pro" in x]}, ensure_ascii=False))

for kind in (1, 2):
    obj = json.loads((ROOT / f"seed-type{kind}-page20.json").read_text())
    rows = []
    for item in obj["sub_article_list"]:
        meta = item["ArticleMeta"]
        rows.append({"title": item["ArticleSubContentEn"]["Title"], "date_ms": meta["PublishDate"],
                     "utc": dt.datetime.fromtimestamp(meta["PublishDate"] / 1000, dt.timezone.utc).isoformat(),
                     "pinned": meta["IsPinned"]})
    result = {"article_type": kind, "returned": len(rows), "has_more": obj["has_more"],
              "next_page_token": obj["next_page_token"], "total": obj["total"], "metadata_only": rows,
              "stop": "page20 older than target; has_more true preserved, not annual exhaustion"}
    (ROOT / f"seed-type{kind}-page20-metadata.json").write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print("SEED", kind, len(rows), rows[0]["utc"], rows[-1]["utc"], obj["has_more"])
