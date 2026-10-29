"""Extract locally retained exact-version HTML for bounded evidence reading."""
from html.parser import HTMLParser
import html
from pathlib import Path
import re

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'tr', 'li', 'figcaption'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'tr', 'li', 'figcaption'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

for source in Path(__file__).parent.glob('supplement-2601.*v1.html'):
    raw = source.read_text()
    def math(match):
        alt = re.search(r'alttext="([^"]*)"', match.group(0))
        return html.escape(html.unescape(alt.group(1))) if alt else ''
    raw = re.sub(r'<math\b.*?</math>', math, raw, flags=re.S)
    parser = Text()
    parser.feed(raw)
    lines = [re.sub(r'\s+', ' ', line).strip() for line in ''.join(parser.parts).splitlines()]
    source.with_suffix('.txt').write_text('\n'.join(line for line in lines if line) + '\n')
    print(source.name, len(lines))
