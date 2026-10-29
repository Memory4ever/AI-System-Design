import datetime
import hashlib
import json
import pathlib
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent


def fetch(name, url):
    target = ROOT / (name + '.raw')
    if target.exists():
        raise RuntimeError('Refusing to overwrite ' + str(target))
    record = {'url': url, 'started_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    request = urllib.request.Request(url, headers={'User-Agent': 'AI-System-Design historical research'})
    try:
        with urllib.request.urlopen(request, timeout=35) as response:
            data = response.read()
            record.update(status=response.status, final_url=response.url, headers=dict(response.headers))
    except urllib.error.HTTPError as error:
        data = error.read()
        record.update(status=error.code, final_url=error.url, headers=dict(error.headers))
    except Exception as error:
        data = b''
        record.update(error=repr(error))
    target.write_bytes(data)
    record.update(ended_at=datetime.datetime.now(datetime.timezone.utc).isoformat(), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    (ROOT / (name + '.request.json')).write_text(json.dumps(record, indent=2), encoding='utf-8')
    print(json.dumps({key: record.get(key) for key in ('url', 'status', 'error', 'bytes')}, ensure_ascii=False))


class SearchParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.items = []
        self.item = None
        self.depth = 0
        self.heading = []
        self.heading_active = False
        self.active = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get('class', '').split()
        if tag == 'h1':
            self.heading_active = True
        if tag == 'li' and 'arxiv-result' in classes:
            self.item = {'text': [], 'links': [], 'title': [], 'abstract': []}
            self.depth = 1
        elif self.item is not None and tag == 'li':
            self.depth += 1
        if self.item is not None:
            if tag == 'a' and attrs.get('href'):
                self.item['links'].append(attrs['href'])
            if 'title' in classes and tag == 'p':
                self.active = 'title'
            if 'abstract-full' in classes:
                self.active = 'abstract'

    def handle_endtag(self, tag):
        if tag == 'h1':
            self.heading_active = False
        if tag == 'p' or (tag == 'span' and self.active == 'abstract'):
            self.active = None
        if self.item is not None and tag == 'li':
            self.depth -= 1
            if self.depth == 0:
                for key in ('text', 'title', 'abstract'):
                    self.item[key] = ' '.join(' '.join(self.item[key]).split())
                self.items.append(self.item)
                self.item = None

    def handle_data(self, value):
        if self.heading_active:
            self.heading.append(value)
        if self.item is not None:
            self.item['text'].append(value)
            if self.active:
                self.item[self.active].append(value)


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []

    def handle_data(self, value):
        if value.strip():
            self.parts.append(value.strip())


GROUPS = {
    'model': ['language model', 'Transformer', 'mixture of experts'],
    'model-exact': ['language model', 'Transformer', 'mixture of experts'],
    'systems': ['GPU', 'decoding', 'kernel', 'inference serving'],
    'systems-narrow': ['language model', 'inference'],
    'multimodal': ['multimodal', 'world model', 'vision language action', 'diffusion model'],
    'agent': ['agent', 'retrieval augmented', 'language model evaluation'],
}


def advanced(group, mode, start=0):
    params = {'advanced': '', 'classification-computer_science': 'y', 'classification-include_cross_list': 'include',
              'date-filter_by': 'date_range', 'abstracts': 'show', 'size': '50', 'start': str(start)}
    for index, term in enumerate(GROUPS[group]):
        params.update({f'terms-{index}-operator': 'AND' if index == 0 or group == 'systems-narrow' else 'OR',
                       f'terms-{index}-term': '"' + term + '"' if ' ' in term else term, f'terms-{index}-field': 'all'})
    if mode == 'announced':
        params.update({'date-from_date': '2025-11-01', 'date-to_date': '2025-11-30',
                       'date-date_type': 'announced_date_first', 'order': '-announced_date_first'})
    else:
        params.update({'date-from_date': '2025-11-28', 'date-to_date': '2025-12-01',
                       'date-date_type': 'submitted_date_first', 'order': '-announced_date_first'})
    name = f'{group}-{mode}-start{start}'
    if mode == 'announced-fixed':
        params.update({'date-from_date': '2025-11-01', 'date-to_date': '2025-12-01',
                       'date-date_type': 'announced_date_first', 'order': '-announced_date_first'})
    fetch(name, 'https://arxiv.org/search/advanced?' + urllib.parse.urlencode(params))
    parser = SearchParser()
    parser.feed((ROOT / (name + '.raw')).read_text(errors='replace'))
    (ROOT / (name + '.parsed.json')).write_text(json.dumps({'heading': ' '.join(' '.join(parser.heading).split()), 'items': parser.items}, indent=2, ensure_ascii=False))
    print(name, ' '.join(' '.join(parser.heading).split()), 'parsed', len(parser.items))


if __name__ == '__main__':
    import sys
    if sys.argv[1] == 'advanced':
        advanced(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 0)
    elif sys.argv[1] == 'fetch':
        fetch(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'titles':
        for path in sorted(ROOT.glob('*.parsed.json')):
            data = json.loads(path.read_text())
            print('\n' + path.name + ': ' + data['heading'])
            for item in data['items']:
                ids = [url.rsplit('/', 1)[-1] for url in item['links'] if '/abs/' in url]
                print(','.join(ids), item['title'])
    elif sys.argv[1] == 'batch':
        for group, mode in [('model-exact', 'announced'), ('multimodal', 'announced'), ('agent', 'announced'),
                            ('model', 'submitted'), ('systems', 'submitted'), ('multimodal', 'submitted'), ('agent', 'submitted')]:
            advanced(group, mode)
    elif sys.argv[1] == 'fixed-batch':
        for group in ('model-exact', 'systems', 'multimodal', 'agent'):
            advanced(group, 'announced-fixed')
    elif sys.argv[1] == 'reparse':
        for path in ROOT.glob('*-start*.raw'):
            parser = SearchParser()
            parser.feed(path.read_text(errors='replace'))
            path.with_suffix('.parsed.json').write_text(json.dumps({'heading': ' '.join(' '.join(parser.heading).split()), 'items': parser.items}, indent=2, ensure_ascii=False))
    elif sys.argv[1] == 'abs-batch':
        for paper in sys.argv[2:]:
            fetch('abs-' + paper + 'v1', 'https://arxiv.org/abs/' + paper + 'v1')
    elif sys.argv[1] == 'abstracts':
        for paper in sys.argv[2:]:
            parser = TextParser()
            parser.feed((ROOT / ('abs-' + paper + 'v1.raw')).read_text(errors='replace'))
            text = '\n'.join(parser.parts)
            print('\n### ' + paper + '\n' + text[text.find('Title:'):text.find('References & Citations')])
