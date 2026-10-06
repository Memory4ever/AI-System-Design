import sys
import re
from html.parser import HTMLParser
from pathlib import Path


class Blocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = None
        self.blocks = []

    def handle_starttag(self, tag, attrs):
        if tag in ('p', 'h2', 'h3', 'h4') and self.active is None:
            self.active = [tag, dict(attrs).get('id', ''), []]

    def handle_data(self, data):
        if self.active is not None:
            self.active[2].append(data)

    def handle_endtag(self, tag):
        if self.active is not None and tag == self.active[0]:
            self.blocks.append((self.active[1], ' '.join(''.join(self.active[2]).split())))
            self.active = None


parser = Blocks()
parser.feed(Path(sys.argv[1]).read_text())
pattern = re.compile(sys.argv[2], re.I)
limit = int(sys.argv[3]) if len(sys.argv) > 3 else 8
matches = [(i, anchor, text) for i, (anchor, text) in enumerate(parser.blocks) if pattern.search(anchor + ' ' + text)]
print('Matching blocks:', len(matches), 'shown:', min(limit, len(matches)))
for i, anchor, text in matches[:limit]:
    print(f'BLOCK {i} #{anchor}: {text}')
