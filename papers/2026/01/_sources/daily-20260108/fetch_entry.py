"""Bounded public-entry capture; stdout only, no local file writes."""
import datetime
import gzip
import json
import re
import sys
import urllib.error
import urllib.request

from html.parser import HTMLParser


class EntryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.in_title = False
        self.title = []
        self.visible = []
        self.links = []
        self.anchor = None

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "nav", "footer"}:
            self.hidden += 1
        if tag == "title":
            self.in_title = True
        if tag == "a":
            self.anchor = {"href": dict(attrs).get("href"), "parts": []}

    def handle_endtag(self, tag):
        if tag in {"script", "style", "nav", "footer"}:
            self.hidden = max(0, self.hidden - 1)
        if tag == "title":
            self.in_title = False
        if tag == "a" and self.anchor:
            text = " ".join(self.anchor["parts"]).strip()
            if text and self.anchor["href"]:
                self.links.append({"text": text[:180], "href": self.anchor["href"]})
            self.anchor = None

    def handle_data(self, data):
        text = data.strip()
        if text and self.in_title:
            self.title.append(text)
        if text and not self.hidden:
            self.visible.append(text)
        if text and self.anchor:
            self.anchor["parts"].append(text)

for url in sys.argv[1:]:
    record = {"url": url, "checked": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Encoding": "gzip"})
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
            if response.headers.get("Content-Encoding") == "gzip":
                data = gzip.decompress(data)
            body = data.decode("utf-8", errors="replace")
            record.update(status=response.status, final_url=response.url, bytes=len(data))
        parser = EntryParser()
        parser.feed(body)
        record["title"] = " ".join(parser.title) or None
        record["date_markers"] = list(dict.fromkeys(re.findall(r'\b20(?:25|26)-\d{2}-\d{2}(?:T[^"<>\s,}]+)?', body)))[:45]
        record["links"] = parser.links[:45]
        record["visible_preview"] = " ".join(parser.visible)[:8000]
        record["capture_limit"] = "first45 nonempty anchors / first45 date markers / first8000 visible characters; not complete historical coverage"
    except Exception as error:
        record["error"] = str(error)
    print(json.dumps(record, ensure_ascii=False))
