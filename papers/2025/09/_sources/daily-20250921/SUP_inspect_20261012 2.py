"""Read only the current day's saved HTML/XML; no network or writes."""
import gzip
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent


def read(name):
    body = (BASE / ("SUP_" + name + "_20261012.raw")).read_bytes()
    return (gzip.decompress(body) if body[:2] == b"\x1f\x8b" else body).decode()


class Node:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def text(self):
        return " ".join(" ".join(x if isinstance(x, str) else x.text()
                                 for x in self.children if isinstance(x, str) or x.tag not in ("script", "style")).split())

    def all(self, tag=None):
        for child in self.children:
            if isinstance(child, Node):
                if tag is None or child.tag == tag:
                    yield child
                yield from child.all(tag)


class Tree(HTMLParser):
    VOID = set("area base br col embed hr img input link meta param source track wbr".split())

    def __init__(self, source):
        super().__init__()
        self.root = self.current = Node("root")
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.current)
        self.current.children.append(node)
        if tag not in self.VOID:
            self.current = node

    def handle_endtag(self, tag):
        node = self.current
        while node.parent and node.tag != tag:
            node = node.parent
        if node.tag == tag:
            self.current = node.parent

    def handle_data(self, text):
        self.current.children.append(text)


def next_data(name):
    chunks = []
    for script in Tree(read(name)).root.all("script"):
        text = "".join(x for x in script.children if isinstance(x, str))
        match = re.fullmatch(r"self\.__next_f\.push\((\[.*\])\)", text)
        if match:
            value = json.loads(match.group(1))
            if len(value) == 2 and isinstance(value[1], str):
                chunks.append(value[1])
    return "".join(chunks)


def objects(text):
    decoder = json.JSONDecoder()
    for match in re.finditer(r"\{", text):
        try:
            value, _ = decoder.raw_decode(text, match.start())
            yield value
        except ValueError:
            pass


if __name__ == "__main__":
    name, mode = sys.argv[1:3]
    if mode == "atoms":
        ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
        entries = ET.fromstring(read(name)).findall("a:entry", ns)
        lo, hi = map(int, sys.argv[3].split("-"))
        for i in range(lo, min(hi + 1, len(entries))):
            item = entries[i]
            print(i, item.findtext("a:id", namespaces=ns), item.findtext("a:published", namespaces=ns))
            for key in ("a:title", "a:summary", "x:comment", "x:journal_ref", "x:doi"):
                print(key, " ".join((item.findtext(key, namespaces=ns) or "").split()))
    else:
        root = Tree(read(name)).root
        if mode == "links":
            for node in root.all("a"):
                print(node.attrs.get("href"), node.text())
        elif mode == "times":
            for node in root.all("time"):
                print(node.attrs, node.parent.text())
        else:
            nodes = [n for n in root.all() if n.tag in ("h1", "h2", "h3", "h4", "p")]
            if mode == "headings":
                for i, node in enumerate(nodes):
                    if node.tag != "p":
                        print(i, node.text())
            else:
                lo, hi = map(int, mode.split("-"))
                for i in range(lo, min(hi + 1, len(nodes))):
                    print(i, nodes[i].text())
