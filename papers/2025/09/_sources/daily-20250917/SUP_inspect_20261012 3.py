"""Read captured exact abstracts or bounded HTML paragraphs without rewriting."""
import gzip
from html.parser import HTMLParser
from pathlib import Path
import sys
import xml.etree.ElementTree as E

BASE = Path(__file__).parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = self.depth = 0
        self.buffer = ""
        self.paragraphs = []
        self.headings = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "h1", "h2", "h3", "h4"):
            self.depth += 1
        if tag == "a":
            self.links.extend(value for key, value in attrs if key == "href")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag in ("p", "h1", "h2", "h3", "h4") and self.depth:
            self.depth -= 1
            if not self.depth:
                self.paragraphs.append(" ".join(self.buffer.split()))
                self.buffer = ""
                if tag != "p":
                    self.headings.append(len(self.paragraphs) - 1)

    def handle_data(self, text):
        if not self.skip and self.depth:
            self.buffer += text + " "


def read(name):
    body = (BASE / ("SUP_" + name + "_20261012.raw")).read_bytes()
    return (gzip.decompress(body) if body[:2] == b"\x1f\x8b" else body).decode()


if __name__ == "__main__":
    name = sys.argv[1]
    if name in ("exact-v1", "old-current"):
        ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
        entries = E.fromstring(read(name)).findall("a:entry", ns)
        lo, hi = map(int, sys.argv[2].split("-"))
        for i in range(lo, min(hi + 1, len(entries))):
            item = entries[i]
            print(i, item.findtext("a:id", namespaces=ns), item.findtext("a:published", namespaces=ns))
            for field in ("a:title", "a:summary", "x:comment", "x:journal_ref", "x:doi"):
                print(field, " ".join((item.findtext(field, namespaces=ns) or "").split()))
    else:
        page = Page()
        page.feed(read(name))
        if len(sys.argv) == 2:
            for i in page.headings:
                print(i, page.paragraphs[i])
        elif sys.argv[2] == "links":
            print("\n".join(page.links))
        else:
            lo, hi = map(int, sys.argv[2].split("-"))
            for i in range(lo, min(hi + 1, len(page.paragraphs))):
                print(i, page.paragraphs[i])

