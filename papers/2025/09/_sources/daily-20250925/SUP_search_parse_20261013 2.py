"""Extract the finite official HTML search slice; no admission decisions."""
import json
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).parent


class Results(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.rows = []
        self.row = None
        self.fields = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.stack.append(tag)
        classes = attrs.get("class", "").split()
        if tag == "li" and "arxiv-result" in classes:
            self.row = {"id": "", "version_identity": "", "title": [], "summary": []}
        if self.row is None:
            return
        if tag == "a" and "/abs/" in attrs.get("href", ""):
            self.row["id"] = attrs["href"].rsplit("/", 1)[1]
        field = "summary" if "abstract-full" in classes else "title" if "title" in classes else None
        if field == "summary":
            self.row["version_identity"] = attrs.get("id", "").removesuffix("-abstract-full")
        if field:
            self.fields.append((len(self.stack), field))

    def handle_endtag(self, tag):
        if tag not in self.stack:
            return
        depth = len(self.stack) - self.stack[::-1].index(tag)
        if tag == "li" and self.row is not None:
            for field in ("title", "summary"):
                self.row[field] = " ".join(" ".join(self.row[field]).split())
            self.rows.append(self.row)
            self.row = None
        self.fields = [(level, field) for level, field in self.fields if level < depth]
        del self.stack[depth - 1:]

    def handle_data(self, text):
        if self.row is not None and self.fields:
            self.row[self.fields[-1][1]].append(text)


if __name__ == "__main__":
    raw = BASE / "SUP_curl-arxiv-html-model_20261013.raw"
    parser = Results()
    parser.feed(raw.read_text())
    target = BASE / "SUP_arxiv-html-model-identities_20261013.json"
    if not target.exists():
        target.write_text(json.dumps({"scope": "Official search first 50 of 155; original submissions Sep23-25 UTC date clues, not public-day events",
                                      "entries": parser.rows}, ensure_ascii=False, indent=2) + "\n")
    old = json.loads((BASE / "arxiv-query-entries.json").read_text())
    identities = {entry["id"].rsplit("/", 1)[1].split("v")[0] for entry in old}
    for index, row in enumerate(parser.rows, 1):
        print(index, row["id"], "old-identity" if row["id"].split("v")[0] in identities else "difference", row["title"])
