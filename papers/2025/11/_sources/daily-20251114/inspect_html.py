"""Inspect primary text and structured date fields without executing HTML."""

import json
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = None
        self.scripts = []
        self.text = []
        self.meta = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.hidden = tag
        if tag == "meta":
            self.meta.append(dict(attrs))
        if tag in ("p", "div", "h1", "h2", "h3", "li", "dt", "dd", "tr"):
            self.text.append("\n")

    def handle_endtag(self, tag):
        if tag == self.hidden:
            self.hidden = None

    def handle_data(self, data):
        if self.hidden == "script":
            self.scripts.append(data)
        elif not self.hidden:
            self.text.append(data)


def walk(value):
    if isinstance(value, dict):
        keys = ("title", "headline", "name", "slug", "publishedOn", "datePublished", "dateModified", "published_at", "updatedAt")
        date = value.get("publishedOn", value.get("datePublished"))
        in_window = True
        if len(sys.argv) > 2 and sys.argv[2] == "dates-window":
            try:
                parsed = datetime.fromisoformat(date.replace("Z", "+00:00"))
                in_window = datetime(2025, 11, 13, 1, tzinfo=timezone.utc) <= parsed < datetime(2025, 11, 14, 1, tzinfo=timezone.utc)
            except (AttributeError, TypeError, ValueError):
                in_window = False
        if in_window and any(key in value for key in ("publishedOn", "datePublished", "dateModified")):
            print(json.dumps({key: value[key] for key in keys if key in value}, ensure_ascii=False))
        for child in value.values():
            walk(child)
    elif isinstance(value, list):
        for child in value:
            walk(child)


if __name__ == "__main__":
    parser = Parser()
    parser.feed(Path(sys.argv[1]).read_text())
    if len(sys.argv) > 2 and sys.argv[2] in ("dates", "dates-window"):
        for meta in parser.meta:
            if any(word in str(meta).lower() for word in ("published", "modified", "date")):
                print(json.dumps(meta))
        for script in parser.scripts:
            try:
                if script.startswith("self.__next_f.push("):
                    payload = json.loads(script[len("self.__next_f.push("):-1])
                    if len(payload) > 1 and isinstance(payload[1], str):
                        for line in payload[1].splitlines():
                            try:
                                walk(json.loads(line.partition(":")[2]))
                            except json.JSONDecodeError:
                                pass
                else:
                    walk(json.loads(script))
            except (json.JSONDecodeError, TypeError):
                pass
    else:
        text = "\n".join(" ".join(line.split()) for line in "".join(parser.text).splitlines() if line.strip())
        anchor = sys.argv[2] if len(sys.argv) > 2 else ""
        start = text.find(anchor) if anchor else 0
        if start < 0:
            raise SystemExit("Text anchor absent")
        print(text[start:start + 18000])
