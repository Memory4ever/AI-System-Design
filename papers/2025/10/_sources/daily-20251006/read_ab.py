"""Display exact abstract and history; output does not assert review."""
from pathlib import Path
from html.parser import HTMLParser
import re
import sys

class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ["script", "style"]:
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ["script", "style"]:
            self.skip = max(0, self.skip - 1)
    def handle_data(self, value):
        if not self.skip:
            self.parts.append(value)

d = Path(sys.argv[1])
start, count = map(int, sys.argv[2:4])
files = sorted(d.glob("abs-*.raw"))
print("Total exact identities:", len(files))
for f in files[start:start+count]:
    p = Parser()
    p.feed(f.read_text())
    s = " ".join(" ".join(p.parts).split())
    a, b = s.find("Title:"), s.find("Abstract:")
    c = re.search(r" Comments:| Subjects:| Submission history", s[b:])
    print("\n", f.name, s[a:s.find("Authors:",a)], s[b:b+c.start()])
    i = s.find("Submission history")
    print(s[i:s.find("Full-text links:",i)])
