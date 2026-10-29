"""Exclusive captures for the Oct03 bounded supplement; never overwrite originals."""
import hashlib
import json
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

BASE = Path(__file__).parent / "supplement-20261007"


class Visible(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("p", "div", "li", "h1", "h2", "h3", "br"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, value):
        if not self.hidden:
            self.parts.append(value)


def fetch(name, url, body=None, extra=None):
    BASE.mkdir(exist_ok=True)
    paths = [BASE / (name + suffix) for suffix in (".raw", ".request.json", ".txt")]
    if any(path.exists() for path in paths):
        raise FileExistsError(name)
    headers = {"User-Agent": "AI-System-Design bounded historical research"}
    headers.update(extra or {})
    if body is not None:
        headers["Content-Type"] = "application/json"
    receipt = {"url": url, "started_utc": datetime.now(timezone.utc).isoformat(),
               "request_headers": headers, "body": body}
    data = b""
    try:
        with urlopen(Request(url, data=None if body is None else json.dumps(body).encode(),
                             headers=headers), timeout=25) as response:
            data = response.read()
            receipt.update(status=response.status, final_url=response.url,
                           response_headers=dict(response.headers))
    except HTTPError as error:
        data = error.read()
        receipt.update(status=error.code, final_url=error.url,
                       response_headers=dict(error.headers), error=str(error))
    except Exception as error:
        receipt.update(status=None, error=repr(error))
    receipt.update(finished_utc=datetime.now(timezone.utc).isoformat(), bytes=len(data),
                   sha256=hashlib.sha256(data).hexdigest())
    paths[0].open("xb").write(data)
    paths[1].open("x").write(json.dumps(receipt, ensure_ascii=False, indent=2))
    parser = Visible()
    parser.feed(data.decode("utf-8", errors="replace"))
    paths[2].open("x").write("".join(parser.parts))
    print(name, receipt["status"], len(data), flush=True)
    return data


if __name__ == "__main__":
    fetch(sys.argv[1], sys.argv[2])
