"""Bounded historical discovery; announcement month is not a public day."""

import datetime
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser


class Node:
    def __init__(self, tag="", attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []

    def text(self):
        return " ".join(" ".join(c.text() if isinstance(c, Node) else c
                                 for c in self.children).split())

    def find(self, predicate):
        out = [self] if predicate(self) else []
        for child in self.children:
            if isinstance(child, Node):
                out.extend(child.find(predicate))
        return out


class Tree(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node()
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                self.stack = self.stack[:index]
                break

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def class_has(name):
    return lambda n: name in n.attrs.get("class", "").split()


def parse(raw):
    tree = Tree()
    tree.feed(raw.decode("utf-8", errors="replace"))
    rows = []
    for item in tree.root.find(class_has("arxiv-result")):
        links = item.find(lambda n: n.tag == "a" and "/abs/" in n.attrs.get("href", ""))
        if not links:
            continue
        identity = links[0].attrs["href"].split("/abs/")[-1]
        title = item.find(class_has("title"))
        abstract = item.find(lambda n: n.attrs.get("id", "").endswith("-abstract-full"))
        submitted = item.find(lambda n: n.tag == "p" and n.text().startswith("Submitted"))
        comments = item.find(class_has("comments"))
        rows.append({"id": identity, "title": title[0].text() if title else "",
                     "abstract_version": abstract[0].attrs.get("id", "").removesuffix("-abstract-full") if abstract else "",
                     "abstract": abstract[0].text() if abstract else "",
                     "version_fields": submitted[0].text() if submitted else "",
                     "comments": [n.text() for n in comments]})
    headings = [n.text() for n in tree.root.find(lambda n: n.tag in {"h1", "h2"})]
    next_links = [n.attrs["href"] for n in tree.root.find(lambda n: n.tag == "a" and class_has("pagination-next")(n))]
    return {"headings": headings, "next": next_links, "rows": rows}


BASE = pathlib.Path(__file__).resolve().parent
repair = "--repair" in sys.argv
boundary = "--boundary" in sys.argv
repair = repair or boundary
if repair:
    BASE = BASE / ("boundary" if boundary else "repair")
    BASE.mkdir(exist_ok=True)
topics = [
    ("inference", [("all", '"large language model"'), ("all", "inference")]),
    ("quantization", [("all", '"language model"'), ("all", "quantization")]),
    ("posttraining", [("all", '"language model"'), ("all", '"reinforcement learning"')]),
    ("world-model", [("title", '"world model"')]),
    ("agent-memory", [("title", "memory"), ("all", "agent")]),
    ("multimodal", [("title", "multimodal"), ("all", '"foundation model"')]),
]
requests = []
for name, terms in topics:
    params = {"advanced": "", "classification-computer_science": "y",
              "classification-include_cross_list": "include", "date-filter_by": "date_range",
              "date-from_date": "2025-09", "date-to_date": "2025-09-30",
              "date-date_type": "announced_date_first", "abstracts": "show",
              "size": "50", "order": "-announced_date_first", "start": "0"}
    if repair:
        params["classification-computer_science_archives"] = "all"
        params["date-from_date"] = "2025-09-01"
    if boundary:
        params["date-to_date"] = "2025-10-01"
    for index, (field, term) in enumerate(terms):
        params.update({f"terms-{index}-operator": "AND", f"terms-{index}-term": term,
                       f"terms-{index}-field": field})
    requests.append((name, "https://arxiv.org/search/advanced?" + urllib.parse.urlencode(params)))
requests.extend([
    ("advanced-form", "https://arxiv.org/search/advanced"),
    ("cl-month-tail", "https://arxiv.org/list/cs.CL/" + ("2025-09" if repair else "2509") + "?skip=2115&show=100"),
])
if repair:
    requests.append(("identity-control", "https://arxiv.org/search/advanced?" + urllib.parse.urlencode({
        "advanced": "", "terms-0-operator": "AND", "terms-0-term": "RServe", "terms-0-field": "all",
        "date-filter_by": "date_range", "date-from_date": "2025-09-01",
        "date-to_date": "2025-10-01" if boundary else "2025-09-30", "date-date_type": "announced_date_first",
        "abstracts": "show", "size": "50", "order": "-announced_date_first"})))
for name, url in requests:
    if (BASE / (name + ".request.json")).exists():
        raise RuntimeError("Refusing to overwrite previous request: " + name)
    stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    record = {"url": url, "started_utc": stamp, "stop": "one bounded page; no automatic pagination"}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "AI-System-Design historical research"}), timeout=30) as response:
            raw = response.read()
            record.update({"status": response.status, "final_url": response.url,
                           "headers": dict(response.headers.items()), "bytes": len(raw)})
        with (BASE / (name + ".html")).open("xb") as out:
            out.write(raw)
        result = parse(raw)
        with (BASE / (name + ".parsed.json")).open("x") as out:
            json.dump(result, out, ensure_ascii=False, indent=2)
        record["headings"] = result["headings"]
        record["rows"] = len(result["rows"])
        record["next"] = result["next"]
    except Exception as error:
        record["error"] = repr(error)
    record["finished_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with (BASE / (name + ".request.json")).open("x") as out:
        json.dump(record, out, ensure_ascii=False, indent=2)
    print(json.dumps({k: record[k] for k in ["url", "headings", "rows", "error"] if k in record}), flush=True)
    time.sleep(3)
