from html.parser import HTMLParser
from pathlib import Path
import sys

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'tr', 'li', 'section'):
            self.parts.append('\n')
        if tag in ('td', 'th'):
            self.parts.append(' | ')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden -= 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'tr', 'li'):
            self.parts.append('\n')
    def handle_data(self, text):
        if not self.hidden and text.strip():
            self.parts.append(' '.join(text.split()) + ' ')

for filename in sys.argv[1:]:
    parser = Text()
    parser.feed(Path(filename).read_text())
    print('SOURCE:', filename)
    print('\n'.join(' '.join(line.split()) for line in ''.join(parser.parts).splitlines() if line.strip()))
