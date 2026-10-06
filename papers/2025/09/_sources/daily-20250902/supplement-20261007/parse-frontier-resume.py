import ast
import json
from html.parser import HTMLParser
from pathlib import Path

root = Path(__file__).resolve().parent
# Load the existing parser class, not its old inputs or top-level execution.
source = ast.parse((root.parent / 'parse_month_frontier.py').read_text())
namespace = {'HTMLParser': HTMLParser}
classes = [node for node in source.body if isinstance(node, ast.ClassDef)]
exec(compile(ast.Module(body=classes, type_ignores=[]), 'frontier_parser', 'exec'), namespace)
entries = {}
pages = []
for path in sorted(root.glob('resume2-arxiv-*-month.html')):
    parser = namespace['FrontierParser']()
    parser.feed(path.read_text())
    receipt = json.loads(Path(str(path) + '.receipt.json').read_text())
    pages.append({'file': path.name, 'url': receipt['url'], 'returned': len(parser.items),
                  'stop': 'skip=0/show=25; no following page requested'})
    for position, item in enumerate(parser.items, 1):
        value = entries.setdefault(item['id'], {**item, 'positions': []})
        value['positions'].append({'file': path.name, 'position': position})
snapshot = {'role': 'bounded title discovery, not semantic abstracts or daily public-date proof',
            'pages': pages, 'appearances': sum(page['returned'] for page in pages),
            'unique': len(entries), 'entries': list(entries.values())}
with (root / 'title-frontier-resume2.json').open('x') as stream:
    json.dump(snapshot, stream, ensure_ascii=False, indent=2)
print(json.dumps({key: snapshot[key] for key in ('pages', 'appearances', 'unique')}))
for value in entries.values():
    print(value['id'], value['title'], value['positions'])
