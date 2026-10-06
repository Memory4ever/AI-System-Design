"""Retrieve explicit exact-version identities, not a category-wide queue."""
import concurrent.futures
import json
import sys
import urllib.request
import re
from html import unescape
from pathlib import Path

def clean(html):
    return unescape(re.sub('<[^>]*>', ' ', html)).strip()

def section(html, tag, classname):
    match = re.search('<' + tag + '[^>]*class="[^"]*' + classname + '[^"]*"[^>]*>(.*?)</' + tag + '>', html, re.S)
    return clean(match.group(1)) if match else 'Not extracted'

def fetch(identity):
    url = 'https://arxiv.org/abs/2601.' + identity + 'v1'
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            html = response.read().decode()
        result = {'id': identity, 'url': url, 'title': section(html, 'h1', 'title'), 'abstract': section(html, 'blockquote', 'abstract'), 'history': section(html, 'div', 'submission-history'), 'comments': section(html, 'table', 'metatable')}
    except Exception as exc:
        result = {'id': identity, 'url': url, 'error': str(exc)}
    Path(__file__).with_name('abs-' + identity + '-v1.json').write_text(json.dumps(result, ensure_ascii=False), encoding='utf-8')
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(fetch, sys.argv[1:]):
        print(json.dumps(result, ensure_ascii=False))
