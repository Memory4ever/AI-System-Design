#!/usr/bin/env python3
"""Bounded source capture for the 2025-07-02 Daily; never judges admission."""
import concurrent.futures
import datetime
import html
from html.parser import HTMLParser
import json
import re
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts = []; self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'): self.skip += 1
        if tag in ('p','div','h1','h2','h3','h4','dt','dd','li','tr','br'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script', 'style'): self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

def capture(job):
    name, url, *options = job
    raw = ROOT / (name + '.raw')
    when = datetime.datetime.now(datetime.timezone.utc).isoformat()
    command = ['curl','-sS','-L','--max-time','40','-w','%{http_code}','-o',str(raw)]
    if options:
        command += ['-H', 'Content-Type: application/json', '-X', 'POST', '--data', json.dumps(options[0])]
    command += [url]
    result = subprocess.run(command, capture_output=True, text=True)
    receipt = {'url':url,'checked_at':when,'returncode':result.returncode,'http':result.stdout,'error':result.stderr}
    if options: receipt['post_body'] = options[0]
    (ROOT / (name + '.request.json')).write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+'\n')
    if raw.exists():
        content = raw.read_text(errors='replace')
        parser = Text(); parser.feed(content)
        (ROOT / (name + '.txt')).write_text('\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())+'\n')
        receipt['bytes'] = raw.stat().st_size
    return receipt

def inventory():
    rows = {}
    for path in list(ROOT.glob('topic-*-30.raw')) + list(ROOT.glob('theme-*.raw')):
        source = path.read_text(errors='replace')
        for block in re.findall(r'<li class="arxiv-result">(.*?)</li>', source, re.S):
            match = re.search(r'/abs/([\d.]+)', block)
            title = re.search(r'<p class="title[^>]*>(.*?)</p>', block, re.S)
            abstract = re.search(r'<span class="abstract-full[^>]*>(.*?)</span>', block, re.S)
            if not match or not title: continue
            def clean(value):
                p = Text(); p.feed(value); return ' '.join(''.join(p.parts).split())
            arid = match.group(1)
            alltext = clean(block)
            full = re.search(r'▽ More (.*?)△ Less', alltext)
            rows[arid] = {'id':arid, 'title':clean(title.group(1)), 'abstract':full.group(1) if full else clean(abstract.group(1)) if abstract else '', 'search_text':alltext, 'source':path.name}
    (ROOT/'search-inventory.json').write_text(json.dumps(list(rows.values()), ensure_ascii=False, indent=2)+'\n')
    for row in rows.values(): print(row['id'], row['title'])

if __name__ == '__main__':
    if sys.argv[1] == 'inventory':
        inventory(); sys.exit()
    jobs = json.loads(sys.argv[1])
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for result in pool.map(capture, jobs): print(json.dumps(result, ensure_ascii=False), flush=True)
