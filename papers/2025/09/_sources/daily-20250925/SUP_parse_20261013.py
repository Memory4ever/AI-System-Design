"""Derive readable source bodies without altering immutable captures."""
import json
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.lines = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden and data.strip():
            self.lines.append(data.strip())


for raw in sorted(BASE.glob("SUP_*_20261013.raw")):
    record = json.loads(raw.with_suffix(".request.json").read_text())
    body = raw.read_bytes()
    if record.get("status") != 200 or not body or body.startswith(b"%PDF"):
        continue
    derived = raw.with_suffix(".txt")
    if not derived.exists():
        parser = Text()
        parser.feed(body.decode("utf-8", "replace"))
        derived.write_text("\n".join(parser.lines) + "\n")
    if "arxiv-" in raw.name:
        ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
        try:
            tree = ET.fromstring(body)
            entries = [{key: " ".join(item.findtext("a:" + key, "", ns).split())
                        for key in ("id", "title", "summary", "published", "updated")}
                       for item in tree.findall("a:entry", ns)]
            target = raw.with_suffix(".entries.json")
            if not target.exists():
                target.write_text(json.dumps({"query": record["url"], "total": tree.findtext("o:totalResults", "", ns),
                                               "entries": entries}, ensure_ascii=False, indent=2) + "\n")
            print(raw.name, "total", tree.findtext("o:totalResults", "", ns), "returned", len(entries))
        except ET.ParseError:
            print(raw.name, "not Atom; no discovery inference")
