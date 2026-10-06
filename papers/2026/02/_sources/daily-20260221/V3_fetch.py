"""Fetch explicit primary URLs to stdout; caller persists through apply_patch."""
import concurrent.futures
import json
import sys
import urllib.request
import re
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "h1", "h2", "h3", "h4", "tr", "li", "section"):
            self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 research-review"})
        with urllib.request.urlopen(req, timeout=35) as r:
            body = r.read().decode("utf-8", "replace")
            if "datacite.org" in url:
                a = json.loads(body)["data"]["attributes"]
                body = json.dumps({k: a.get(k) for k in ("doi", "titles", "dates", "created", "registered", "url")})
            elif "/html/" in url:
                parser = TextParser()
                parser.feed(body)
                body = "\n".join(" ".join(s.split()) for s in "".join(parser.parts).split("\n") if s.strip())
                if sys.argv[2].startswith("focus:"):
                    pattern = re.compile(sys.argv[2][6:], re.M)
                    matches = list(pattern.finditer(body))
                    offset = matches[-1].start() if matches else 0
                    body = body[offset:offset + int(sys.argv[3])]
                else:
                    body = body[int(sys.argv[2]):int(sys.argv[3])]
            else:
                parser = TextParser()
                parser.feed(body)
                body = "\n".join(" ".join(s.split()) for s in "".join(parser.parts).split("\n") if s.strip()).split("Bibliographic Tools")[0]
            return {"url": url, "status": r.status, "body": body}
    except Exception as e:
        return {"url": url, "error": str(e)}

urls = []
mode = sys.argv[1]
for identity in sys.argv[4:]:
    if mode == "body":
        urls.append(f"https://arxiv.org/html/{identity}v1")
    else:
        urls.extend([f"https://arxiv.org/abs/{identity}v1", f"https://api.datacite.org/dois/10.48550/arxiv.{identity}"])
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    print(json.dumps(list(pool.map(fetch, urls))))
