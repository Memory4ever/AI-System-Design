"""Print readable primary HTML text without executing page content."""

import argparse
from html.parser import HTMLParser
from pathlib import Path


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden += 1
        if tag in ("p", "div", "li", "h1", "h2", "h3", "h4", "tr", "dt", "dd"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--from-text", default="")
    parser.add_argument("--limit", type=int, default=30000)
    args = parser.parse_args()
    html = TextParser()
    html.feed(Path(args.path).read_text())
    text = "\n".join(" ".join(line.split()) for line in "".join(html.parts).splitlines() if line.strip())
    start = text.find(args.from_text) if args.from_text else 0
    if start < 0:
        raise SystemExit("Requested text anchor is absent")
    print(text[start : start + args.limit])
