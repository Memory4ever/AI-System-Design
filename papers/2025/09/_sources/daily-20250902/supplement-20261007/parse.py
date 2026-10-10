import importlib.util
import json
import re
from pathlib import Path

root = Path(__file__).resolve().parent
# Reuse the parser implementation only, never another day's responses.
path = root.parents[3] / '11/_sources/daily-20251101/advanced-resume-20261007/fetch.py'
spec = importlib.util.spec_from_file_location('search_parser', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
entries = {}
queries = []
for path in sorted(root.glob('arxiv-*.html')):
    parser = module.SearchParser()
    parser.feed(path.read_text())
    text = ' '.join(''.join(parser.text).split())
    header = re.search(r'Showing.*?results', text)
    queries.append({'file': path.name, 'header': header.group(0) if header else None, 'returned': len(parser.items), 'next': parser.next})
    for position, item in enumerate(parser.items, 1):
        url = next(link for link in item['links'] if '/abs/' in link)
        identity = url.split('/abs/')[-1]
        record = entries.setdefault(identity, {'id': identity, 'title': ' '.join(''.join(item['title']).split()), 'abstract': ' '.join(''.join(item['abstract']).split()), 'metadata': ' '.join(''.join(item['text']).split()), 'positions': []})
        record['positions'].append({'file': path.name, 'position': position})
snapshot = {'role': 'Mechanical parsing; not semantic abstract review or public-date proof', 'queries': queries, 'unique': len(entries), 'entries': list(entries.values())}
with (root / 'parsed-discovery.json').open('x') as stream:
    json.dump(snapshot, stream, ensure_ascii=False, indent=2)
print(json.dumps({'queries': queries, 'unique': len(entries)}, ensure_ascii=False))
for record in entries.values():
    print(record['id'], record['title'], json.dumps(record['positions']))
