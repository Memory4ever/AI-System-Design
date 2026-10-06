"""Text extraction of captured evidence, not a prose authoring tool."""
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
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())

for name in sys.argv[1:]:
    p = Path(__file__).parent / (name + '.raw')
    parser = Text()
    parser.feed(p.read_text(errors='replace'))
    text = '\n'.join(parser.parts)
    p.with_suffix('.txt').write_text(text)
    print(name, text[:20000])
