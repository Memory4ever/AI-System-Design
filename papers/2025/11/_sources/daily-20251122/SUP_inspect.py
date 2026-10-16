"""Read-only HTML/Flight projections; no semantic screening or closure."""
import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class HTML(HTMLParser):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.parts = []
        self.scripts = []
        self.script = False

    def flush(self):
        value = ' '.join(' '.join(self.parts).split())
        self.parts = []
        if value:
            self.blocks.append(value)

    def handle_starttag(self, tag, attrs):
        if tag == 'script':
            self.script = True
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'li', 'table', 'figure'):
            self.flush()

    def handle_endtag(self, tag):
        if tag == 'script':
            self.script = False
        if tag in ('p', 'h1', 'h2', 'h3', 'h4', 'li', 'table', 'figure'):
            self.flush()

    def handle_data(self, value):
        if self.script:
            if value.startswith('self.__next_f.push('):
                self.scripts.append(json.loads(value[len('self.__next_f.push('):-1])[1])
        else:
            self.parts.append(value)

    def flight(self):
        decoder = json.JSONDecoder()
        for part in self.scripts:
            for line in part.splitlines():
                try:
                    value, _ = decoder.raw_decode(line[line.find(':') + 1:])
                except (ValueError, TypeError):
                    continue
                yield value


def read(name):
    reader = HTML()
    reader.feed((Path(__file__).parent / name).read_text())
    reader.flush()
    return reader


class Navigation(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.title = False
        self.dt = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'p':
            self.title = 'list-title' in attrs.get('class', '').split()
        if tag == 'dt':
            self.dt = True
        if tag == 'a' and (self.title or self.dt):
            match = re.fullmatch(r'(?:https://arxiv.org)?/abs/(\d{4}\.\d{4,5})(?:v\d+)?', attrs.get('href', ''))
            if match:
                self.ids.append(match.group(1))

    def handle_endtag(self, tag):
        if tag == 'p':
            self.title = False
        if tag == 'dt':
            self.dt = False


def navigation(name):
    reader = Navigation()
    reader.feed((Path(__file__).parent / name).read_text())
    return reader.ids


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('--start', type=int, default=0)
    parser.add_argument('--end', type=int)
    args = parser.parse_args()
    reader = read(args.name)
    print(args.name, len(reader.blocks), 'blocks')
    for i in range(args.start, min(args.end or len(reader.blocks), len(reader.blocks))):
        print(i, reader.blocks[i])
