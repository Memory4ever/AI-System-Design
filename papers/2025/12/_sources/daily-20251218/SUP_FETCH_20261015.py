"""Finite HTML discovery only; no admission or completion decisions."""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from html.parser import HTMLParser
import json

ROOT = Path(__file__).parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "li", "h1", "h2", "h3", "h4", "tr"):
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


queries = {
    "LANGUAGE": '"large language model" OR "foundation model" OR "language model training" OR "Transformer architecture"',
    "SYSTEM": '"GPU kernel" OR "collective communication" OR "LLM inference" OR "distributed training" OR "speculative decoding" OR "model compiler"',
    "MULTIMODAL": '"vision language model" OR "video generation" OR "world model" OR "vision language action" OR "audio language model"',
    "AGENT": '"language agent" OR "LLM agent" OR "retrieval augmented" OR "agent memory" OR "tool calling"',
}

for name, query in queries.items():
    params = {
        "advanced": "", "terms-0-operator": "AND", "terms-0-term": query,
        "terms-0-field": "abstract", "date-filter_by": "date_range",
        "date-from_date": "2025-12-15", "date-to_date": "2025-12-17",
        "date-date_type": "submitted_date_first", "abstracts": "show",
        "size": "50", "order": "submitted_date", "start": "0",
    }
    url = "https://arxiv.org/search/advanced?" + urlencode(params)
    print(json.dumps({"name": name, "url": url}, ensure_ascii=False), flush=True)
    try:
        with urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=35) as r:
            data = r.read()
            status = r.status
        raw = ROOT / ("RAW_ARXIV_" + name + "_20261015.html")
        raw.write_bytes(data)
        parser = Text()
        parser.feed(data.decode("utf-8", errors="replace"))
        text = "".join(parser.out)
        (ROOT / ("RAW_ARXIV_" + name + "_20261015.txt")).write_text(text)
        print(json.dumps({"name": name, "status": status, "bytes": len(data), "text": text[:1500]}, ensure_ascii=False), flush=True)
    except (URLError, HTTPError, TimeoutError) as exc:
        print(json.dumps({"name": name, "error": str(exc)}, ensure_ascii=False), flush=True)
