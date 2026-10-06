"""Save actual HTTP responses for one date; never infer historical coverage."""
import datetime
import json
import gzip
import pathlib
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.links = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag in ("p", "div", "h1", "h2", "h3", "li", "br", "tr"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


folder = pathlib.Path(sys.argv[1])
folder.mkdir(parents=True, exist_ok=True)
for arg in sys.argv[2:]:
    name, url = arg.split("=", 1)
    payload = None
    if "|" in url:
        url, body = url.split("|", 1)
        payload = body.encode("utf-8")
    row = {"url": url, "checked_at": datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, data=payload, headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/json", "x-tt-locale": "US", "accept-language": "zh"})
        if payload:
            row["request_body"] = json.loads(body)
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read()
            row.update(status=response.status, final_url=response.url, content_type=response.headers.get("Content-Type"), content_encoding=response.headers.get("Content-Encoding"))
        (folder / (name + ".raw")).write_bytes(data)
        plain = gzip.decompress(data) if row.get("content_encoding") == "gzip" or data[:2] == b"\x1f\x8b" else data
        decoded = plain.decode("utf-8", errors="replace")
        parser = Text()
        parser.feed(decoded)
        lines = [" ".join(line.split()) for line in "".join(parser.parts).splitlines()]
        (folder / (name + ".txt")).write_text("\n".join(line for line in lines if line), encoding="utf-8")
        row.update(bytes=len(data), links=list(dict.fromkeys(parser.links)))
    except Exception as error:
        row.update(error=str(error))
    (folder / (name + ".request.json")).write_text(json.dumps(row, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(name, row.get("status", row.get("error")), row.get("bytes", 0), flush=True)
