import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path

B = Path(__file__).parent

class Sections(HTMLParser):
    def __init__(self, wanted):
        super().__init__()
        self.wanted = wanted
        self.stack = []
        self.active = 0
        self.out = []
        self.heading = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            identity = attrs.get('id', '')
            self.stack.append(identity)
            if identity in self.wanted:
                self.active += 1
        if tag in ['h1', 'h2', 'h3', 'h4']:
            self.heading = True
            if not self.wanted:
                self.out.append('\n'+str(self.stack)+' ')
        if self.active and tag in ['p', 'tr', 'li', 'h1', 'h2', 'h3', 'h4']:
            self.out.append('\n')
    def handle_endtag(self, tag):
        if tag == 'section' and self.stack:
            if self.stack.pop() in self.wanted:
                self.active -= 1
        if tag in ['h1', 'h2', 'h3', 'h4']:
            self.heading = False
    def handle_data(self, text):
        if self.active or (not self.wanted and self.heading):
            self.out.append(text)

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.out = []
    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style']:
            self.skip += 1
        if tag in ['p', 'h1', 'h2', 'h3', 'h4', 'tr', 'li']:
            self.out.append('\n')
    def handle_endtag(self, tag):
        if tag in ['script', 'style']:
            self.skip -= 1
    def handle_data(self, text):
        if not self.skip:
            self.out.append(text)

arguments = sys.argv[1:]
line_range = None
sections = None
if arguments and arguments[0] in ['--outline', '--sections']:
    sections = [] if arguments[0] == '--outline' else arguments[1].split(',')
    arguments = arguments[1:] if arguments[0] == '--outline' else arguments[2:]
if arguments and arguments[0] == '--range':
    line_range = tuple(map(int, arguments[1].split(':')))
    arguments = arguments[2:]
for identity in arguments:
    path = B / f'REPAIR_BODY_{identity}v1_20261029.html'
    if not path.exists():
        result = subprocess.run(['curl', '-L', '--max-time', '22', '--retry', '0', '-sS', '-D', str(path.with_suffix('.headers')), '-o', str(path), f'https://arxiv.org/html/{identity}v1'], capture_output=True, text=True)
        print(identity, result.returncode, result.stderr.strip(), path.stat().st_size if path.exists() else 0, flush=True)
    else:
        parser = Text() if sections is None else Sections(sections)
        parser.feed(path.read_text(errors='replace'))
        print('\n'.join(f'{n}: {line.strip()}' for n, line in enumerate(''.join(parser.out).splitlines()) if line.strip() and (line_range is None or line_range[0] <= n < line_range[1])))
