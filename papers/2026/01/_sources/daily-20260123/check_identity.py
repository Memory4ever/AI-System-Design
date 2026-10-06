"""Bounded metadata/date/official notices for explicit event IDs; no versions or attachments."""
import concurrent.futures
import json
import re
import sys
import urllib.request
from html import unescape
from pathlib import Path

def fetch(identity):
    record = {'id': identity, 'checked': '2026-10-04', 'event': 'v1'}
    for name, url in [('datacite', 'https://api.datacite.org/dois/10.48550/arxiv.2601.' + identity), ('official_abs', 'https://arxiv.org/abs/2601.' + identity + 'v1')]:
        try:
            with urllib.request.urlopen(url, timeout=25) as response:
                raw = response.read().decode()
            if name == 'datacite':
                record[name] = json.loads(raw)
            else:
                blocks = re.findall(r'<table\b[^>]*>(.*?)</table>', raw, re.S)
                record['official_metadata'] = [unescape(re.sub(r'<[^>]*>', ' ', b)) for b in blocks if 'Comments:' in b or 'Subjects:' in b]
                record['notice_signals'] = [unescape(re.sub(r'<[^>]*>', ' ', raw[max(0, m.start()-150):m.end()+250])) for m in re.finditer(r'withdrawn|retracted|erratum|corrigendum|correction|replaced', raw, re.I)]
                record['official_url'] = url
        except Exception as exc:
            record[name + '_error'] = str(exc)
    Path(__file__).with_name('identity-' + identity + '-v1.json').write_text(json.dumps(record, ensure_ascii=False), encoding='utf-8')
    return {'id': identity, 'registered': record.get('datacite', {}).get('data', {}).get('attributes', {}).get('registered'), 'notices': record.get('notice_signals'), 'errors': {k:v for k,v in record.items() if k.endswith('_error')}}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(fetch, sys.argv[1:]):
        print(json.dumps(result, ensure_ascii=False))
