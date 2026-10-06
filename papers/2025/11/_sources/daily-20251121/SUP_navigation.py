"""Project saved navigation identities and titles for actual bounded reading."""
from html.parser import HTMLParser
from pathlib import Path
import re


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.identity = None
        self.depth = 0
        self.parts = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a':
            match = re.search(r'/abs/(\d{4}\.\d{4,5})', attrs.get('href', ''))
            if match:
                self.identity = match[1]
        if self.depth:
            self.depth += 1
        elif ('title' in attrs.get('class', '').split() and tag == 'p') or (tag == 'div' and 'list-title' in attrs.get('class', '').split()):
            self.depth = 1
            self.parts = []

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1
            if not self.depth and self.identity:
                self.rows.append((self.identity, ' '.join(' '.join(self.parts).split())))

    def handle_data(self, value):
        if self.depth:
            self.parts.append(value)


def load_rows():
    folder = Path(__file__).parent
    names = ['MODEL_SIMPLE', 'LEARNING_SIMPLE', 'LEARNING_P2', 'SYSTEM', 'AGENT_SIMPLE', 'MULTIMODAL_SIMPLE', 'GENERATION', 'WORLD', 'LIST_CL', 'LIST_LG_TARGET']
    rows = {}
    occurrences = 0
    for name in names:
        parser = Navigation()
        parser.feed((folder / f'SUP_ARXIV_{name}_20261015.html').read_text())
        print(name, len(parser.rows))
        occurrences += len(parser.rows)
        for identity, title in parser.rows:
            rows.setdefault(identity, title)
    return rows, occurrences


if __name__ == '__main__':
    rows, occurrences = load_rows()
    folder = Path(__file__).parent
    known = {p.name.split('_')[2] for p in folder.glob('SUP_AB_*_20261015.html')}
    known |= {p.name.split('_')[2] for p in folder.glob('SUP_CURRENT_*_20261015.html')}
    for pattern in ('SUP_TAIL_AB_*_20261015.html', 'SUP_TAIL2_AB_*_20261015.html', 'SUP_TAIL3_AB_*_20261015.html'):
        known |= {p.name.split('_')[3] for p in folder.glob(pattern)}
    known |= {p.name[7:-5] for p in folder.glob('signal_*.html')}
    print('occurrences', occurrences, 'unique', len(rows), 'known files', len(known))
    for identity, title in rows.items():
        if identity not in known:
            print(identity, title)
