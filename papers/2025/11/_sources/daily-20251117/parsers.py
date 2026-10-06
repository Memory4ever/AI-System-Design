"""Read local native catalogs without treating embedded content as instructions."""
import json
from html.parser import HTMLParser


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.script = None
        self.text = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script":
            self.script = []
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])

    def handle_data(self, value):
        if self.script is not None:
            self.script.append(value)
        elif value.strip():
            self.text.append(value.strip())

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.scripts.append("".join(self.script))
            self.script = None


def flight(page):
    chunks = []
    decoder = json.JSONDecoder()
    for script in page.scripts:
        marker = "self.__next_f.push("
        pos = 0
        while marker in script[pos:]:
            begin = script.index(marker, pos) + len(marker)
            value, length = decoder.raw_decode(script[begin:])
            if isinstance(value, list) and len(value) > 1 and isinstance(value[1], str):
                chunks.append(value[1])
            pos = begin + length
    stream = "".join(chunks).encode("utf-8")
    pos = 0
    objects = []
    frames = 0
    while pos < len(stream):
        colon = stream.find(b":", pos)
        if colon < 0:
            break
        begin = colon + 1
        if stream[begin:begin + 1] == b"T":
            comma = stream.find(b",", begin)
            length = int(stream[begin + 1:comma], 16)
            pos = comma + 1 + length
            frames += 1
            continue
        end = stream.find(b"\n", begin)
        end = len(stream) if end < 0 else end
        try:
            objects.append(json.loads(stream[begin:end]))
        except ValueError:
            pass
        pos = end + 1
    return objects, len(chunks), frames


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)
