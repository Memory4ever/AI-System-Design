from html.parser import HTMLParser
from pathlib import Path
import sys


class AbsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.text = {"title": [], "abstract": [], "history": []}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        section = self.stack[-1][1] if self.stack else None
        if tag == "h1" and "title" in classes:
            section = "title"
        elif tag == "blockquote" and "abstract" in classes:
            section = "abstract"
        elif tag == "div" and "submission-history" in classes:
            section = "history"
        if tag not in {"meta", "br", "img", "input", "link", "hr", "source"}:
            self.stack.append((tag, section))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.stack and self.stack[-1][1]:
            self.text[self.stack[-1][1]].append(data)


for filename in sys.argv[1:]:
    parser = AbsParser()
    parser.feed(Path(filename).read_text())
    print(filename)
    for key, parts in parser.text.items():
        print(key, " ".join(" ".join(parts).split()))
