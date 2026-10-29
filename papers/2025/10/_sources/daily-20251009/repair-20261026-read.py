"""Render local evidence as text, with optional bounded line selection."""
from html.parser import HTMLParser
from pathlib import Path
import sys

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ignore = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.ignore += 1
        if tag in ('h1', 'h2', 'h3', 'h4', 'p', 'tr', 'li', 'section', 'blockquote', 'div'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.ignore -= 1
        if tag in ('h1', 'h2', 'h3', 'h4', 'p', 'tr', 'li', 'blockquote'):
            self.parts.append('\n')
    def handle_data(self, data):
        if not self.ignore:
            self.parts.append(data)

abstract_only = '--abs' in sys.argv
for f in [a for a in sys.argv[1:] if a != '--abs']:
    p = Text()
    p.feed(Path(f).read_text(errors='replace'))
    lines = [' '.join(l.split()) for l in ''.join(p.parts).splitlines() if l.strip()]
    print('\nFILE:', f)
    if abstract_only:
        start = next(i for i, l in enumerate(lines) if l.startswith('Title:'))
        end = next(i for i, l in enumerate(lines) if l.startswith('Cite as:'))
        history = next(i for i, l in enumerate(lines) if l == 'Submission history')
        stop = next(i for i, l in enumerate(lines) if l == 'Full-text links:')
        print('\n'.join(lines[start:end] + lines[history:stop]))
    else:
        for i, line in enumerate(lines, 1):
            print(f'{i}: {line}')
