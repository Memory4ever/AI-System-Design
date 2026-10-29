"""Mechanical HTML text extraction for evidence reading, not evidence scoring."""
from html.parser import HTMLParser
from pathlib import Path
import sys

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'tr', 'figcaption'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'tr', 'figcaption'):
            self.parts.append('\n')
        elif tag in ('td', 'th'):
            self.parts.append(' | ')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

for arg in sys.argv[1:]:
    p = Path(arg)
    parser = Text()
    parser.feed(p.read_text())
    lines = [' '.join(x.split()) for x in ''.join(parser.parts).splitlines() if x.strip()]
    p.with_suffix('.txt').write_text('\n'.join(lines) + '\n')
    print(p.name, len(lines))
