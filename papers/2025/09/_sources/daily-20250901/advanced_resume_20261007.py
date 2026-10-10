"""Capture bounded monthly discovery without changing prior evidence."""

import datetime
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

OUT = Path(__file__).parent / "advanced-resume-20261007"
QUERIES = {
    "attention": [("language model", "abstract"), ("attention", "title")],
    "training": [("language model", "abstract"), ("training", "title")],
    "inference": [("language model", "abstract"), ("inference", "title")],
    "agent": [("language model", "abstract"), ("agent", "title")],
    "reasoning": [("language model", "abstract"), ("reasoning", "title")],
    "vision-language": [("vision language", "abstract")],
    "diffusion": [("diffusion", "title"), ("generation", "abstract")],
    "world-model": [("world model", "abstract")],
}


class Results(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.items = []
        self.current = None
        self.heading = []
        self.next_links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        self.stack.append((tag, attrs))
        if tag == "li" and "arxiv-result" in classes:
            self.current = {"id": None, "version": None, "title": [],
                            "abstract": [], "text": []}
        if tag == "a" and "pagination-next" in classes:
            self.next_links.append(attrs.get("href"))
        if self.current is not None:
            href = attrs.get("href", "")
            if tag == "a" and href.startswith("https://arxiv.org/abs/"):
                self.current["id"] = href.rsplit("/", 1)[1]
            if "abstract-full" in classes:
                self.current["version"] = attrs.get("id", "").replace("-abstract-full", "")
        if tag in ("meta", "link", "input", "br", "img", "hr"):
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag == "li" and self.current is not None:
            item = self.current
            for field in ("title", "abstract", "text"):
                item[field] = " ".join(" ".join(item[field]).split())
            self.items.append(item)
            self.current = None
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, data):
        if any(tag == "h1" for tag, _ in self.stack):
            self.heading.append(data)
        if self.current is None:
            return
        self.current["text"].append(data)
        if any("title" in attrs.get("class", "").split() for _, attrs in self.stack):
            self.current["title"].append(data)
        if any("abstract-full" in attrs.get("class", "").split() for _, attrs in self.stack):
            if data.strip() != "Less":
                self.current["abstract"].append(data)


def capture(name, terms):
    params = {"advanced": "", "classification-computer_science": "y",
              "classification-include_cross_list": "include",
              "date-filter_by": "date_range", "date-from_date": "2025-08",
              "date-to_date": "2025-08", "date-date_type": "announced_date_first",
              "abstracts": "show", "size": "25", "order": "-announced_date_first",
              "start": "0"}
    if "-adjacent" in name:
        params["date-to_date"] = "2025-09"
    if name == "control-month":
        params.pop("classification-computer_science")
    for index, (term, field) in enumerate(terms):
        params.update({f"terms-{index}-operator": "AND",
                       f"terms-{index}-term": term, f"terms-{index}-field": field})
    url = "https://arxiv.org/search/advanced?" + urllib.parse.urlencode(params)
    if name.startswith("abs-"):
        url = "https://arxiv.org/abs/" + name[4:] + "v1"
        params = {}
    if name == "merit-pmlr":
        url = "https://proceedings.mlr.press/v267/luo25u.html"
        params = {}
    if name == "merit-openreview":
        url = "https://api2.openreview.net/notes?id=NSxKNNFni0"
        params = {}
    meta = {"url": url, "parameters": params,
            "started": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "stop_policy": ("first 25 only; monthly discovery, not daily coverage"
                            if params else "single identified metadata/event page; not full-text review")}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0"}), timeout=35) as response:
            raw = response.read()
            meta.update(status=response.status, final_url=response.url,
                        headers=dict(response.headers))
    except urllib.error.HTTPError as error:
        raw = error.read()
        meta.update(status=error.code, error=str(error))
    except Exception as error:
        raw = b""
        meta.update(status=None, error=str(error))
    meta.update(bytes=len(raw), finished=datetime.datetime.now(datetime.timezone.utc).isoformat())
    OUT.mkdir(exist_ok=True)
    for suffix, content in (("raw", raw), ("request.json", json.dumps(meta, indent=2).encode())):
        with (OUT / f"{name}.{suffix}").open("xb") as stream:
            stream.write(content)
    parser = Results()
    parser.feed(raw.decode("utf-8", errors="replace"))
    parsed = {"heading": " ".join(" ".join(parser.heading).split()),
              "next": parser.next_links, "items": parser.items}
    with (OUT / f"{name}.parsed.json").open("x") as stream:
        json.dump(parsed, stream, ensure_ascii=False, indent=2)
    print(name, meta["status"], len(raw), parsed["heading"],
          len(parser.items), flush=True)


if sys.argv[1:] == ["--inventory"]:
    base = OUT.parent
    basis = [base / "SCREENING.md", base / "supplement-20261007.md"]
    previous = set(re.findall(r"\b(?:25|26)\d{2}\.\d{4,5}\b",
                              "\n".join(path.read_text() for path in basis)))
    items = {}
    returned = 0
    for path in sorted(OUT.glob("*.parsed.json")):
        data = json.loads(path.read_text())
        returned += len(data["items"])
        for item in data["items"]:
            record = items.setdefault(item["id"], {
                "id": item["id"], "title": item["title"], "queries": [],
                "previous_identity": item["id"] in previous,
                "selected_v1": (OUT / f'abs-{item["id"]}.raw').exists()})
            record["queries"].append(path.name)
    inventory = {"generated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 "basis_sha256": {str(p.relative_to(base)): hashlib.sha256(p.read_bytes()).hexdigest() for p in basis},
                 "returned": returned, "unique": len(items),
                 "previous": sum(x["previous_identity"] for x in items.values()),
                 "new": sum(not x["previous_identity"] for x in items.values()),
                 "items": list(items.values())}
    with (OUT / "inventory.json").open("x") as stream:
        json.dump(inventory, stream, ensure_ascii=False, indent=2)
    print({k: inventory[k] for k in ("returned", "unique", "previous", "new")})
    sys.exit(0)

for name in sys.argv[1:] or QUERIES:
    key = name.replace("-adjacent", "").replace("-phrase", "")
    if name.startswith("abs-") or name.startswith("merit-"):
        terms = []
    else:
        terms = [("language model", "all")] if name == "control-month" else QUERIES[key]
    if "-phrase" in name:
        terms = [(f'"{term}"' if " " in term else term, field) for term, field in terms]
    capture(name, terms)
    time.sleep(3)
