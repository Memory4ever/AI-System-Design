"""Extract structural discovery fields without making admission decisions."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path

class Node:
    def __init__(self, tag="", attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def text(self):
        return " ".join(" ".join(x.text() if isinstance(x, Node) else x
                                 for x in self.children).split())

    def find(self, tag=None, cls=None):
        result = []
        if (tag is None or self.tag == tag) and (cls is None or cls in self.attrs.get("class", "").split()):
            result.append(self)
        for child in self.children:
            if isinstance(child, Node):
                result.extend(child.find(tag, cls))
        return result

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node()
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                self.stack = self.stack[:index]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("--mode", choices=["advanced", "monthly", "text"], default="advanced")
parser.add_argument("--lower", default="2511.11000")
parser.add_argument("--upper", default="2511.14000")
args = parser.parse_args()
source = Path(args.file)
document = Parser()
document.feed(source.read_text())
if args.mode == "text":
    print(document.root.text())
elif args.mode == "monthly":
    lists = [n for n in document.root.find("dl") if n.attrs.get("id") == "articles"]
    records = []
    for listing in lists:
        identity = None
        for node in listing.children:
            if not isinstance(node, Node):
                continue
            if node.tag == "dt":
                links = [n.attrs["href"] for n in node.find("a") if n.attrs.get("href", "").startswith("/abs/")]
                identity = links[0].rsplit("/", 1)[-1] if links else None
            if node.tag == "dd" and identity and args.lower <= identity < args.upper:
                titles = node.find(cls="list-title")
                records.append({"id": identity, "title": titles[0].text(), "metadata": node.text()})
    print(json.dumps(records, ensure_ascii=False, indent=2))
else:
    records = []
    for node in document.root.find("li", "arxiv-result"):
        def field(cls):
            found = node.find(cls=cls)
            return found[0].text() if found else None
        records.append({"identity": field("list-title"), "title": field("title"),
                        "abstract": field("abstract-full"), "metadata": field("is-size-7")})
    result = {"headings": [n.text() for n in document.root.find("h1")], "records": records}
    output = source.with_suffix(".extracted.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
