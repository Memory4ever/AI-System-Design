"""Read saved HTML text or Next Flight data without executing page scripts."""

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("p", "h1", "h2", "h3", "li", "a", "time", "tr"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def flight(source):
    parts = []
    for match in re.finditer(r'self\.__next_f\.push\(', source):
        value, _ = json.JSONDecoder().raw_decode(source[match.end():])
        if len(value) > 1 and isinstance(value[1], str):
            parts.append(value[1])
    return "".join(parts)


if __name__ == "__main__":
    source = Path(sys.argv[1]).read_text()
    parser = Text()
    parser.feed(source)
    lines = [re.sub(r"\s+", " ", line).strip()
             for line in "".join(parser.parts).splitlines()]
    lines = [line for line in lines if line]
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    end = int(sys.argv[3]) if len(sys.argv) > 3 else len(lines)
    print("total text lines", len(lines))
    for index, line in enumerate(lines[start:end], start):
        print(index, line)
