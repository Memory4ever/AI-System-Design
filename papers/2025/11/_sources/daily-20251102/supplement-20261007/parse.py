import importlib.util
import json
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARSER_PATH = ROOT.parents[1] / 'daily-20251101/advanced-resume-20261007/fetch.py'
spec = importlib.util.spec_from_file_location('reused_search_parser', PARSER_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.scripts = []
        self.current = None
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag == 'script':
            self.current = []

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip -= 1
        if tag == 'script':
            self.scripts.append(''.join(self.current or []))
            self.current = None

    def handle_data(self, data):
        if self.current is not None:
            self.current.append(data)
        if not self.skip and data.strip():
            self.text.append(data.strip())


def parse_page(path):
    parser = PageParser()
    parser.feed(path.read_text())
    return parser


entries = {}
queries = []
for path in sorted(ROOT.glob('arxiv-exact-*.html')):
    parser = module.SearchParser()
    parser.feed(path.read_text())
    page = ' '.join(''.join(parser.text).split())
    header = re.search(r'Showing.*?results', page)
    queries.append({'file': path.name, 'header': header.group(0) if header else None,
                    'returned': len(parser.items), 'next': parser.next})
    for item in parser.items:
        url = next(u for u in item['links'] if '/abs/' in u)
        text = ' '.join(''.join(item['text']).split())
        match = re.search(r'v1 submitted (\d+ [A-Z][a-z]+, \d+)', text)
        if not match:
            match = re.search(r'Submitted (\d+ [A-Z][a-z]+, \d+)', text)
        submitted = datetime.strptime(match.group(1), '%d %B, %Y') if match else None
        early = submitted is not None and submitted <= datetime(2025, 11, 1)
        flagged = bool(re.search(r'withdrawn|withdrawing|text overlap|erratum', text, re.I))
        entry = entries.setdefault(url, {
            'id': url.split('/abs/')[-1], 'url': url,
            'title': ' '.join(''.join(item['title']).split()),
            'abstract': ' '.join(''.join(item['abstract']).split()),
            'metadata': text[text.rfind('Submitted'):],
            'v1_submitted_discovery_only': submitted.date().isoformat() if submitted else None,
            'early_discovery_or_seen_correction': early or flagged, 'query_files': [],
        })
        entry['query_files'].append(path.name)

snapshot = {'role': 'Generated metadata, not semantic screening or public-date proof',
            'queries': queries, 'unique': len(entries), 'entries': list(entries.values()),
            'selected_for_complete_abstract': [x['id'] for x in entries.values() if x['early_discovery_or_seen_correction']]}
out = ROOT / 'parsed-discovery.json'
with out.open('x') as stream:
    json.dump(snapshot, stream, ensure_ascii=False, indent=2)
print(json.dumps({k: snapshot[k] for k in ['queries', 'unique', 'selected_for_complete_abstract']}, ensure_ascii=False))
