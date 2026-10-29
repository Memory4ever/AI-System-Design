import json
from html.parser import HTMLParser
from pathlib import Path


class Fields(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.captures = []
        self.fields = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get('class', '').split())
        selected = classes & {'dateline', 'comments', 'submission-history', 'title', 'abstract'}
        self.stack.append(tag)
        for key in selected:
            self.captures.append([key, len(self.stack), []])

    def handle_endtag(self, tag):
        if tag not in self.stack:
            return
        depth = len(self.stack) - self.stack[::-1].index(tag)
        for entry in list(self.captures):
            if entry[1] >= depth:
                self.fields[entry[0]] = ' '.join(''.join(entry[2]).split())
                self.captures.remove(entry)
        self.stack = self.stack[:depth - 1]

    def handle_data(self, data):
        for entry in self.captures:
            entry[2].append(data)


root = Path(__file__).parent
rows = []
for path in sorted(root.glob('SUP_current-*_20261015.raw')):
    parser = Fields()
    parser.feed(path.read_text())
    rows.append({'id': path.name.split('-')[1].split('_')[0], **parser.fields})
out = root / 'SUP_CURRENT_FIELDS_20261015.json'
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
for row in rows:
    print(json.dumps({key: value for key, value in row.items() if key != 'abstract'}, ensure_ascii=False))
