"""Read captured source HTML as a small tree; no network or report writes."""
from html.parser import HTMLParser
import json
import re
from SUP_inspect_20261012 import read


class Node:
    def __init__(self, tag, attrs=(), parent=None):
        self.tag, self.attrs, self.parent = tag, dict(attrs), parent
        self.children = []

    def text(self):
        return " ".join(" ".join(x if isinstance(x, str) else x.text()
                                 for x in self.children).split())

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
        text = script.text()
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
    import sys
    root = Tree(read(sys.argv[1])).root
    mode = sys.argv[2]
    if mode == "times":
        for node in root.all("time"):
            print(node.attrs, node.parent.text()[:600])
    elif mode == "links":
        for node in root.all("a"):
            print(node.attrs.get("href"), node.text())
    elif mode == "cards":
        for node in root.all():
            if node.tag in ("article", "h2", "h3"):
                print(node.tag, node.attrs, node.parent.text()[:800])
    elif mode == "tables":
        for node in root.all("table"):
            print(node.attrs, node.text())
