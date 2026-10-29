"""Fetch exact assigned v1 sources serially, preserving failed attempts."""
import json
from pathlib import Path
from urllib.request import urlopen
from html.parser import HTMLParser
import sys

ROOT = Path(__file__).resolve().parent
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.out = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style']: self.skip += 1
        if tag in ['p', 'section', 'h1', 'h2', 'h3', 'h4', 'tr', 'li']: self.out.append('\n')
    def handle_endtag(self, tag):
        if tag in ['script', 'style']: self.skip -= 1
    def handle_data(self, data):
        if not self.skip: self.out.append(data)

for short in sys.argv[1:]:
    identity = short if '.' in short else '2510.' + short
    target = ROOT / f'REPAIR_CORE_{identity}v1_20261029'
    url = f'https://arxiv.org/html/{identity}v1'
    if target.with_suffix('.txt').exists(): continue
    try:
        with urlopen(url, timeout=20) as response:
            raw = response.read()
            Path(str(target)+'.headers').write_text(str(response.headers))
        Path(str(target)+'.html').write_bytes(raw)
        parser = Text(); parser.feed(raw.decode())
        Path(str(target)+'.txt').write_text(''.join(parser.out))
        print(identity, len(raw), flush=True)
    except Exception as error:
        Path(str(target)+'.error.txt').write_text(str(error))
        print(identity, type(error).__name__, str(error), flush=True)
