import json
import subprocess
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode


ROOT = Path(__file__).resolve().parent


class SearchParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.items = []
        self.item = None
        self.depth = 0
        self.stack = []
        self.text = []
        self.next = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if tag == 'a' and 'pagination-next' in classes and attrs.get('href'):
            self.next.append(attrs['href'])
        if tag == 'li' and 'arxiv-result' in classes:
            self.item = {'text': [], 'links': [], 'title': [], 'abstract': []}
            self.depth = 1
        elif self.item is not None and tag == 'li':
            self.depth += 1
        if self.item is not None and tag == 'a' and attrs.get('href'):
            self.item['links'].append(attrs['href'])
        self.stack.append((tag, classes, attrs.get('id', '')))

    def handle_endtag(self, tag):
        if self.item is not None and tag == 'li':
            self.depth -= 1
            if self.depth == 0:
                self.items.append(self.item)
                self.item = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                self.stack = self.stack[:i]
                break

    def handle_data(self, data):
        self.text.append(data)
        if self.item is None:
            return
        self.item['text'].append(data)
        if any('title' in classes for _, classes, _ in self.stack):
            self.item['title'].append(data)
        if any(identity.endswith('-abstract-full') for _, _, identity in self.stack):
            self.item['abstract'].append(data)


def fetch(name, url):
    request_path = ROOT / (name + '.request.json')
    if request_path.exists() or (ROOT / (name + '.raw')).exists():
        raise RuntimeError('Refusing to overwrite ' + name)
    started = datetime.now().astimezone().isoformat()
    result = subprocess.run(
        ['curl', '-L', '--max-time', '40', '-D', str(ROOT / (name + '.headers')),
         '-o', str(ROOT / (name + '.raw')), '-w', '%{http_code}\n%{url_effective}', url],
        capture_output=True, text=True,
    )
    record = {'name': name, 'url': url, 'started': started,
              'finished': datetime.now().astimezone().isoformat(),
              'exit_code': result.returncode, 'http_and_effective_url': result.stdout,
              'stderr': result.stderr, 'author': '2025-11-01 continuation author'}
    parser = SearchParser()
    raw = ROOT / (name + '.raw')
    if raw.exists():
        parser.feed(raw.read_text(errors='replace'))
        record['bytes'] = raw.stat().st_size
    entries = []
    for item in parser.items:
        urls = [link for link in item['links'] if '/abs/' in link]
        if not urls:
            continue
        entries.append({'id': urls[0].split('/abs/')[-1], 'url': urls[0],
                        'title': ' '.join(''.join(item['title']).split()),
                        'abstract': ' '.join(''.join(item['abstract']).split()),
                        'text': ' '.join(''.join(item['text']).split())})
    record['next_links'] = parser.next
    record['page_text'] = ' '.join(''.join(parser.text).split())
    record['entries'] = entries
    with request_path.open('x') as out:
        json.dump(record, out, ensure_ascii=False, indent=2)
    print(json.dumps({'name': name, 'http': result.stdout, 'exit': result.returncode,
                      'entries': len(entries), 'next': parser.next,
                      'header': record['page_text'][:650]}, ensure_ascii=False), flush=True)


GROUPS = {
    'model': ['mixture of experts', 'state space model', 'reward model',
              'preference optimization', 'test-time scaling', 'model merging'],
    'systems': ['speculative decoding', 'prefill', 'disaggregated',
                'distributed training', 'inference serving', 'LLM compiler'],
    'multimodal': ['video generation', 'vision language model',
                   'flow matching', 'embodied', 'world model'],
    'agent': ['retrieval augmented generation', 'agent memory',
              'prompt injection', 'computer use', 'multi-agent language'],
}

if __name__ == '__main__':
    for name, terms in GROUPS.items():
        params = {'advanced': '', 'classification-include_cross_list': 'include',
                  'date-filter_by': 'date_range', 'date-from_date': '2025-10-01',
                  'date-to_date': '2025-11-01', 'date-date_type': 'announced_date_first',
                  'abstracts': 'show', 'size': '50', 'order': '-announced_date_first', 'start': '0'}
        for i, term in enumerate(terms):
            params.update({f'terms-{i}-operator': 'AND' if i == 0 else 'OR',
                           f'terms-{i}-term': '"' + term + '"', f'terms-{i}-field': 'title'})
        fetch('advanced-month-exact-' + name, 'https://arxiv.org/search/advanced?' + urlencode(params))
    fetch('official-dc-month-middle', 'https://arxiv.org/list/cs.DC/2025-10?skip=100&show=100')
