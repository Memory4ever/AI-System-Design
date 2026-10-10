"""Print saved source blocks with MathML alttext, without modifying sources."""
import argparse
from html.parser import HTMLParser
from pathlib import Path

class Blocks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.math_depth = 0
        self.skip_depth = 0
        self.count = 0
    def flush(self):
        value = ' '.join(' '.join(self.parts).split())
        if value:
            self.count += 1
            print(f'B{self.count}: {value}')
        self.parts = []
    def handle_starttag(self, tag, attrs):
        if self.math_depth:
            self.math_depth += 1
            return
        if self.skip_depth:
            if tag not in ('img', 'input', 'br', 'hr', 'link', 'meta', 'source', 'wbr'):
                self.skip_depth += 1
            return
        if tag in ('script', 'style', 'nav', 'header'):
            self.skip_depth = 1
        elif tag == 'math':
            self.parts.append(dict(attrs).get('alttext', ''))
            self.math_depth = 1
        elif tag in ('h1', 'h2', 'h3', 'h4', 'p', 'tr', 'li'):
            self.flush()
    def handle_endtag(self, tag):
        if self.math_depth:
            self.math_depth -= 1
            return
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag in ('h1', 'h2', 'h3', 'h4', 'p', 'tr', 'li', 'div'):
            self.flush()
    def handle_data(self, data):
        if not self.skip_depth and not self.math_depth:
            self.parts.append(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    args = parser.parse_args()
    blocks = Blocks()
    blocks.feed(Path(args.source).read_text())
    blocks.flush()
