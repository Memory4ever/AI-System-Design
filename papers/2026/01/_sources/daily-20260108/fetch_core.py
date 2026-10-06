"""Exact public HTML, selected sections only; stdout, no local files."""
import datetime
import json
import sys
import urllib.request
from html.parser import HTMLParser

class CoreParser(HTMLParser):
    def __init__(self, wanted):
        super().__init__()
        self.wanted = wanted
        self.sections = []
        self.capture = None
        self.math_depth = 0
        self.records = []
        self.headings = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "section":
            self.sections.append(attrs.get("id", ""))
        section = self.sections[-1] if self.sections else ""
        if tag in {"h2", "h3", "h4"}:
            self.capture = {"tag": tag, "section": section, "parts": [], "heading": True}
        elif tag == "p" and any(section == item or section.startswith(item + ".") for item in self.wanted):
            self.capture = {"tag": tag, "section": section, "parts": [], "heading": False}
        if tag == "math":
            self.math_depth += 1
            if self.capture:
                self.capture["parts"].append(attrs.get("alttext", "[math without alttext]"))

    def handle_endtag(self, tag):
        if tag == "math":
            self.math_depth = max(0, self.math_depth - 1)
        if self.capture and tag == self.capture["tag"]:
            text = " ".join(" ".join(self.capture["parts"]).split())
            item = {"section": self.capture["section"], "text": text}
            if self.capture["heading"]:
                self.headings.append(item)
            elif text:
                self.records.append(item)
            self.capture = None
        if tag == "section" and self.sections:
            self.sections.pop()

    def handle_data(self, data):
        if self.capture and not self.math_depth:
            self.capture["parts"].append(data)

paper_id = sys.argv[1]
sections = sys.argv[2:]
url = "https://arxiv.org/html/" + paper_id + "v1"
record = {"id": paper_id, "url": url, "requested_sections": sections, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
try:
    with urllib.request.urlopen(url, timeout=35) as response:
        raw = response.read().decode("utf-8")
    parser = CoreParser(sections)
    parser.feed(raw)
    record.update(headings=parser.headings, core=parser.records, capture="selected paragraphs only; tables/algorithms need targeted primary read when decisive")
except Exception as error:
    record["error"] = str(error)
print(json.dumps(record, ensure_ascii=False))
