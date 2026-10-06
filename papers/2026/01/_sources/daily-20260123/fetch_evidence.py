"""Cache exact HTML for explicit candidates; do not traverse links or attachments."""
import concurrent.futures
import json
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path

def fetch(identity):
    url = 'https://arxiv.org/html/2601.' + identity + 'v1'
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            html = response.read().decode()
        blocks = re.findall(r'<(h[1-6]|p|figcaption|table)\b[^>]*>(.*?)</\1>', html, re.S)
        lines = []
        for tag, block in blocks:
            if 'ltx_bibitem' in block:
                continue
            block = re.sub(r'<annotation\b[^>]*encoding="application/x-tex"[^>]*>(.*?)</annotation>', r' \1 ', block, flags=re.S)
            text = unescape(re.sub('<[^>]*>', ' ', block))
            text = re.sub(r'\s+', ' ', text).strip()
            lines.append(f'{tag}: {text}')
        Path(__file__).with_name('html-' + identity + '-v1.txt').write_text('\n'.join(lines), encoding='utf-8')
        return {'id': identity, 'url': url, 'blocks': len(lines), 'headings': [line for line in lines if line.startswith(('h2:', 'h3:'))]}
    except Exception as exc:
        return {'id': identity, 'url': url, 'error': str(exc)}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(fetch, sys.argv[1:]):
        print(json.dumps(result, ensure_ascii=False))
