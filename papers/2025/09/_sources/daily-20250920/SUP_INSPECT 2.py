import json
import pathlib
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup

ROOT = pathlib.Path(__file__).resolve().parent


def load(name):
    return (ROOT / (name + '.raw')).read_text()


def walk(data):
    if isinstance(data, dict):
        yield data
        for value in data.values():
            yield from walk(value)
    elif isinstance(data, list):
        for value in data:
            yield from walk(value)


def next_objects(name):
    soup = BeautifulSoup(load(name), 'html.parser')
    for script in soup.find_all('script'):
        content = script.get_text()
        prefix = 'self.__next_f.push('
        if not content.startswith(prefix):
            continue
        outer = json.loads(content[len(prefix):-1])
        if len(outer) < 2 or not isinstance(outer[1], str):
            continue
        for line in outer[1].splitlines():
            value = line.partition(':')[2]
            try:
                yield from walk(json.loads(value))
            except json.JSONDecodeError:
                continue


if __name__ == '__main__':
    import sys
    mode = sys.argv[1]
    if mode == 'text':
        for name in sys.argv[2:]:
            soup = BeautifulSoup(load(name), 'html.parser')
            for tag in soup(['script', 'style', 'nav', 'footer']):
                tag.decompose()
            print(name, soup.get_text(' ', strip=True))
    elif mode == 'json':
        for name in sys.argv[2:]:
            data = json.loads(load(name))
            print(name, json.dumps(data, ensure_ascii=False))
    elif mode == 'rss':
        items = ET.fromstring(load('SUP_OPENAI_RSS')).findall('./channel/item')
        print('RSS count', len(items))
        for row in items:
            date = row.findtext('pubDate')
            if 'Sep 2025' in date:
                print(date, row.findtext('title'), row.findtext('link'))
    elif mode == 'next':
        for name in sys.argv[2:]:
            rows = list(next_objects(name))
            print(name, 'objects', len(rows))
            dated = [r for r in rows if 'publishedOn' in r or 'publishedAt' in r or 'publishDate' in r or 'publicationDate' in r]
            print('dated count', len(dated))
            for row in dated:
                print({k:v for k,v in row.items() if k in ['title','publishedOn','publishedAt','publishDate','publicationDate','slug']})
            if not dated:
                print([(list(r.keys()), str(r)[:300]) for r in rows if any(k in r for k in ['hasMore','papers','articles','date','createdAt'])][:30])
    elif mode == 'scripts':
        for name in sys.argv[2:]:
            soup = BeautifulSoup(load(name), 'html.parser')
            print(name, [(s.get('src'), s.get('id'), len(s.get_text())) for s in soup.find_all('script')])
    elif mode == 'core':
        soup = BeautifulSoup(load(sys.argv[2]), 'html.parser')
        for selector in sys.argv[3:]:
            node = soup.select_one(selector)
            print(selector, node.get_text(' ', strip=True) if node else 'missing')
    elif mode == 'ab':
        files = sorted(ROOT.glob('SUP_AB_*.raw'))
        start, end = map(int, sys.argv[2:4])
        print('total', len(files), 'slice', start, end)
        for path in files[start:end]:
            identity = path.stem.removeprefix('SUP_AB_')
            soup = BeautifulSoup(path.read_text(), 'html.parser')
            print(identity, soup.select_one('h1.title').get_text(' ', strip=True) if soup.select_one('h1.title') else 'NO TITLE')
            for selector in ['blockquote.abstract', 'td.tablecell.comments']:
                node = soup.select_one(selector)
                print(selector, node.get_text(' ', strip=True) if node else 'missing')
            current = BeautifulSoup(load('SUP_CURRENT_' + identity), 'html.parser')
            for selector in ['td.tablecell.comments', '.withdrawn']:
                node = current.select_one(selector)
                if node:
                    print('CURRENT', selector, node.get_text(' ', strip=True))
