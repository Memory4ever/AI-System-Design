"""Bounded exact-v1 HTML retrieval for the assigned Oct19 multimodal slice."""
import concurrent.futures
import datetime
import json
import sys
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent

class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        if tag in ('p','div','section','h1','h2','h3','h4','tr','li','figure'):
            self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style') and self.skip:
            self.skip -= 1
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

def fetch(paper_id):
    url = f'https://arxiv.org/html/2610.{paper_id}v1'
    info = {'id': paper_id, 'url': url, 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=22) as response:
            raw = response.read()
            info.update(status=response.status, bytes=len(raw), final_url=response.url)
        (ROOT / f'html_{paper_id}.raw.html').write_bytes(raw)
        parser = Text()
        parser.feed(raw.decode('utf-8', errors='replace'))
        lines = [line.strip() for line in ''.join(parser.parts).splitlines() if line.strip()]
        (ROOT / f'html_{paper_id}.visible.txt').write_text('\n'.join(lines))
        info['lines'] = len(lines)
    except Exception as error:
        info['error'] = str(error)
    (ROOT / f'html_{paper_id}.request.json').write_text(json.dumps(info, indent=2))
    return info

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fetch, sys.argv[1:]):
            print(json.dumps(result), flush=True)
