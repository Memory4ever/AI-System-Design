"""Mechanical HTML/XML text extraction, without review labels."""
from html.parser import HTMLParser
import gzip
from pathlib import Path
import sys
import xml.etree.ElementTree as ET

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hide = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hide += 1
        if tag in ("p", "h1", "h2", "h3", "h4", "tr", "li", "section", "div"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hide = max(0, self.hide - 1)

    def handle_data(self, data):
        if not self.hide:
            self.parts.append(data)

for filename in sys.argv[1:]:
    path = Path(filename)
    data = path.read_bytes()
    if data.startswith(b"\x1f\x8b"):
        data = gzip.decompress(data)
    raw = data.decode("utf-8", "replace")
    if raw.startswith("<?xml"):
        root = ET.fromstring(raw)
        ns = {"a": "http://www.w3.org/2005/Atom"}
        lines = []
        for entry in root.findall("a:entry", ns):
            lines.extend(entry.findtext("a:" + field, namespaces=ns) or "" for field in ("id", "title", "published", "updated", "summary"))
            lines.append("")
        text = "\n".join(lines)
    else:
        parser = Parser()
        parser.feed(raw)
        text = "\n".join(line.strip() for line in "".join(parser.parts).splitlines() if line.strip())
    path.with_suffix(".text.txt").write_text(text + "\n")
