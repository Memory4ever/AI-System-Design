import json
from html.parser import HTMLParser
from pathlib import Path

root = Path(__file__).resolve().parent


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.scripts = []
        self.text = []
        self.block = None
        self.content = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.block = tag
            self.content = []

    def handle_endtag(self, tag):
        if tag == self.block:
            if tag == 'script':
                self.scripts.append(''.join(self.content))
            self.block = None

    def handle_data(self, data):
        if self.block:
            self.content.append(data)
        elif data.strip():
            self.text.append(data.strip())


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


for name in ('anthropic.html', 'zai-p1.html', 'zai-p2.html', 'mimo.html', 'ernie-p1.html', 'ernie-p2.html'):
    page = Page()
    page.feed((root / name).read_text())
    decoder = json.JSONDecoder()
    chunks = []
    for script in page.scripts:
        prefix = 'self.__next_f.push('
        if script.startswith(prefix):
            value, _ = decoder.raw_decode(script[len(prefix):])
            if value[0] == 1:
                chunks.append(value[1])
    values = []
    for line in ''.join(chunks).splitlines():
        _, separator, content = line.partition(':')
        if separator:
            try:
                value, _ = decoder.raw_decode(content)
                values.extend(walk(value))
            except ValueError:
                pass
    if name == 'anthropic.html':
        posts = {}
        for value in values:
            if value.get('publishedOn'):
                key = value.get('_id', str(value.get('slug')))
                posts[key] = {k: value.get(k) for k in ('_id', 'title', 'publishedOn', 'slug')}
        snapshot = {'posts': list(posts.values()), 'unique': len(posts)}
    else:
        snapshot = {'text': page.text, 'pagination': [value for value in values if 'hasMore' in value]}
    with (root / (name + '.parsed.json')).open('x') as stream:
        json.dump(snapshot, stream, ensure_ascii=False, indent=2)
    print(name, len(snapshot.get('posts', snapshot.get('text', []))))
