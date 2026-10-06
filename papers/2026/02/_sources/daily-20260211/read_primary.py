"""Bounded primary-source reads; stdout only, callers preserve output with apply_patch."""
import concurrent.futures
import datetime
import json
import pathlib
import html
import re
import sys
import urllib.request

def clean(raw):
    raw = re.sub(r'<(?:script|style|nav|header|footer)\b[^>]*>.*?</(?:script|style|nav|header|footer)>', '', raw, flags=re.S)
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', raw))).strip()

def read(url):
    try:
        if url.startswith('local:'):
            raw = pathlib.Path(url[6:]).read_text()
        else:
            req = urllib.request.Request(url, headers={'User-Agent': 'AI-System-Design research'})
            raw = urllib.request.urlopen(req, timeout=25).read().decode('utf-8', 'replace')
        if 'api.datacite.org/dois/' in url:
            attrs = json.loads(raw)['data']['attributes']
            body = {key: attrs.get(key) for key in ['doi', 'created', 'registered', 'updated', 'url', 'titles', 'dates']}
        elif '/abs/' in url:
            patterns = [r'<h1[^>]*class="title[^"\n]*"[^>]*>.*?</h1>',
                        r'<blockquote[^>]*class="abstract[^"\n]*"[^>]*>.*?</blockquote>',
                        r'<div[^>]*class="submission-history"[^>]*>.*?</div>',
                        r'<td[^>]*class="tablecell comments"[^>]*>.*?</td>']
            body = '\n'.join(clean(m.group()) for pat in patterns
                             if (m := re.search(pat, raw, re.S)))
        else:
            body = clean(raw)
        return {'url': url, 'executed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                'text': body, 'status': 'read'}
    except Exception as exc:
        return {'url': url, 'status': 'error', 'error': str(exc)}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    print(json.dumps(list(pool.map(read, sys.argv[1:])), ensure_ascii=False, indent=2))
