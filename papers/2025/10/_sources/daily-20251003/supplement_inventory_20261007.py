"""Parse finite discovery inventory; extracted abstracts are not reviewed abstracts."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent
OUT = BASE / "supplement-20261007"


class Results(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.current = None
        self.records = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "li" and "arxiv-result" in attrs.get("class", ""):
            self.current = {"id": "", "title": "", "abstract": "", "metadata": ""}
        field = None
        if self.current:
            if tag == "a" and "/abs/" in attrs.get("href", ""):
                self.current["id"] = attrs["href"].split("/abs/")[-1]
            if tag == "p" and "title" in attrs.get("class", "").split():
                field = "title"
            if tag == "span" and "abstract-full" in attrs.get("class", ""):
                field = "abstract"
            if tag == "p" and "is-size-7" in attrs.get("class", "").split():
                field = "metadata"
        if tag not in ("br", "input", "meta", "link", "img", "hr"):
            self.stack.append((tag, field))

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, -1, -1):
            if self.stack[index][0] == tag:
                if tag == "li" and self.current:
                    self.records.append({k: " ".join(v.split()) for k, v in self.current.items()})
                    self.current = None
                self.stack = self.stack[:index]
                break

    def handle_data(self, data):
        if self.current:
            for tag, field in reversed(self.stack):
                if field:
                    self.current[field] += data
                    break


def old_ids():
    result = set()
    for name in ("exact-v1", "tail-exact-v1", "title-supplement-v1",
                 "arxiv-model", "arxiv-model-tail", "arxiv-systems", "arxiv-agent", "arxiv-multimodal"):
        root = ET.parse(BASE / (name + ".raw")).getroot()
        for item in root.findall("{http://www.w3.org/2005/Atom}entry"):
            value = item.findtext("{http://www.w3.org/2005/Atom}id", "").split("/abs/")[-1]
            result.add(value.split("v")[0])
    return result


if __name__ == "__main__":
    old = old_ids()
    combined = {}
    for path in sorted(OUT.glob("advanced-*-start0.raw")):
        parser = Results()
        parser.feed(path.read_text())
        print("\n" + path.stem, len(parser.records))
        for rank, row in enumerate(parser.records, 1):
            row["old_identity"] = row["id"].split("v")[0] in old
            row["source"] = path.name
            row["rank"] = rank
            combined.setdefault(row["id"], row)
            print(rank, row["id"], "OLD" if row["old_identity"] else "NEW", row["title"])
    target = sys.argv[1] if len(sys.argv) > 1 else "advanced-inventory.json"
    (OUT / target).open("x").write(json.dumps(list(combined.values()), ensure_ascii=False, indent=2))
    print("Unique", len(combined), "old", sum(row["old_identity"] for row in combined.values()))
