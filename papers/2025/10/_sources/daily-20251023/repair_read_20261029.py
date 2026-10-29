import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'tr', 'li'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

class Prose(HTMLParser):
    def __init__(self):
        super().__init__()
        self.capture = None
        self.depth = 0
        self.parts = []
        self.lines = []
        self.math_depth = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ('p', 'h2', 'h3', 'h4') and self.capture is None:
            self.capture = tag
            self.parts = []
            self.depth = 1
        elif self.capture == tag:
            self.depth += 1
        if tag == 'math':
            self.math_depth += 1
            self.parts.append(attrs.get('alttext', ''))
    def handle_endtag(self, tag):
        if tag == 'math':
            self.math_depth -= 1
        if self.capture == tag:
            self.depth -= 1
            if not self.depth:
                self.lines.append(' '.join(''.join(self.parts).split()))
                self.capture = None
    def handle_data(self, data):
        if self.capture and not self.math_depth:
            self.parts.append(data)

records = {}
for p in ROOT.glob('REPAIR_REGISTERED_VALID_*_p1_20261029.json'):
    for r in json.loads(p.read_text())['payload']['data']:
        records[r['id'].split('arxiv.')[-1]] = r

class Event(HTMLParser):
    def __init__(self):
        super().__init__()
        self.fields = {}
        self.capture = None
        self.depth = 0
        self.parts = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'meta' and attrs.get('name', '').startswith('citation_'):
            self.fields.setdefault(attrs['name'], []).append(attrs.get('content', ''))
        if self.capture:
            if tag == self.capture[0]:
                self.depth += 1
        elif (tag == 'td' and 'comments' in attrs.get('class', '')) or attrs.get('class') == 'submission-history':
            self.capture = (tag, attrs.get('class'))
            self.depth = 1
            self.parts = []
    def handle_endtag(self, tag):
        if self.capture and tag == self.capture[0]:
            self.depth -= 1
            if not self.depth:
                self.fields[self.capture[1]] = ' '.join(''.join(self.parts).split())
                self.capture = None
    def handle_data(self, data):
        if self.capture:
            self.parts.append(data)

if sys.argv[1] == 'signals':
    bounds = []
    for filename in ('REPAIR_POTENTIAL_BOUNDS_20261029.json', 'REPAIR_REOPENED_BOUNDS_20261029.json'):
        bounds.extend(json.loads((ROOT / filename).read_text()))
    ids = sorted({r['arxiv_id'] for r in bounds if r['status'] == 'bounded'} - {'2510.18745', '2510.18289'})
    for i in ids:
        path = ROOT / f'REPAIR_EVENT_{i}_20261029.html'
        try:
            if not path.exists():
                with urlopen('https://arxiv.org/abs/' + i, timeout=25) as response:
                    raw = response.read()
                    headers = dict(response.headers)
                path.write_bytes(raw)
                path.with_suffix('.headers.json').write_text(json.dumps({'url': 'https://arxiv.org/abs/' + i, 'checked_utc': datetime.now(timezone.utc).isoformat(), 'headers': headers}, indent=2))
            parser = Event()
            parser.feed(path.read_text())
            print(i, json.dumps(parser.fields, ensure_ascii=False), flush=True)
        except Exception as e:
            print(i, type(e).__name__, str(e), flush=True)
elif sys.argv[1] == 'abstract':
    for i in sys.argv[2:]:
        a = records[i]['attributes']
        print('\nID', i, a['titles'][0]['title'])
        for d in a['descriptions']:
            print(d['descriptionType'], d['description'])
elif sys.argv[1] == 'fetch':
    for i in sys.argv[2:]:
        path = ROOT / f'REPAIR_{i}v1_20261029.html'
        if not path.exists():
            try:
                with urlopen('https://arxiv.org/html/' + i + 'v1', timeout=35) as response:
                    raw = response.read()
                path.write_bytes(raw)
            except Exception as e:
                print(i, type(e).__name__, str(e), flush=True)
                continue
        parser = Text()
        parser.feed(path.read_text())
        lines = [s.strip() for s in ''.join(parser.parts).splitlines() if s.strip()]
        path.with_suffix('.txt').write_text('\n'.join(lines))
        print(i, len(lines), flush=True)
elif sys.argv[1] == 'text':
    parser = Text()
    parser.feed(Path(sys.argv[2]).read_text())
    print(''.join(parser.parts))
elif sys.argv[1] in ('prose', 'index'):
    for spec in sys.argv[2:]:
        fields = spec.split(':')
        i = fields[0]
        start = int(fields[1]) if len(fields) > 1 else 0
        end = int(fields[2]) if len(fields) > 2 else 100000
        parser = Prose()
        parser.feed((ROOT / f'REPAIR_{i}v1_20261029.html').read_text())
        print('ID', i)
        for n, line in enumerate(parser.lines):
            if start <= n < end and (sys.argv[1] == 'prose' or (len(line) < 120 and not line.startswith('Instructions'))):
                print(n, line)
