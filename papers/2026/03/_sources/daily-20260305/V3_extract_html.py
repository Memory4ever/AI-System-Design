"""Read-only semantic extraction of exact-version LaTeXML evidence."""
import argparse
import re
from html.parser import HTMLParser
from pathlib import Path
import sys

class Article(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.skip = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if self.skip:
            if tag == self.skip[-1]:
                self.skip.append(tag)
            return
        if tag in ('script', 'style', 'nav'):
            self.skip.append(tag)
        elif tag == 'math':
            self.parts.append(' ' + attrs.get('alttext', '') + ' ')
            self.skip.append(tag)
        elif tag in ('p', 'div', 'section', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if self.skip:
            if tag == self.skip[-1]:
                self.skip.pop()
            return
        if tag in ('p', 'div', 'section', 'tr', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li'):
            self.parts.append('\n')
        elif tag in ('td', 'th'):
            self.parts.append(' | ')
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

cli = argparse.ArgumentParser()
cli.add_argument('path')
cli.add_argument('--start', type=int, default=0)
cli.add_argument('--end', type=int, default=1000000)
args = cli.parse_args()
p = Article()
p.feed(sys.stdin.read() if args.path == '-' else Path(args.path).read_text())
lines = [re.sub(r'\s+', ' ', s).strip() for s in ''.join(p.parts).splitlines()]
lines = [s for s in lines if s]
for i, s in enumerate(lines):
    if args.start <= i < args.end:
        print(f'{i}: {s}')
