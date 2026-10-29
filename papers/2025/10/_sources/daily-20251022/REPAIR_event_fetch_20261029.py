"""Fetch named official event pages, retaining raw responses and failure metadata."""
import json
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from REPAIR_fetch_20261029 import ROOT

for key in sys.argv[1:]:
    if key.startswith('external:'):
        _, label, url = key.split(':', 2)
        name = f'REPAIR_EVENT_{label}_20261029.raw'
    elif key.startswith('archivewide:'):
        _, category, kind = key.split(':')
        target = (f'arxiv.org/list/{category}/new*' if kind == 'list'
                  else f'export.arxiv.org/rss/{category}*')
        params = {'url': target, 'from': '20251019', 'to': '20251022',
                  'output': 'json', 'filter': 'statuscode:200',
                  'collapse': 'timestamp:8', 'limit': '8'}
        url = 'https://web.archive.org/cdx/search/cdx?' + urllib.parse.urlencode(params)
        name = f'REPAIR_DATE_ARCHIVEWIDE_{category}_{kind}_20261029.json'
    elif key.startswith('day:'):
        _, category, day = key.split(':')
        url = f'https://arxiv.org/list/{category}/{day}?show=2000'
        name = f'REPAIR_DATE_DAY_{category}_{day}_20261029.html'
    elif key.startswith('archive:'):
        category = key.split(':')[1]
        params = {'url': f'arxiv.org/list/{category}/new', 'from': '20251019',
                  'to': '20251022', 'output': 'json', 'filter': 'statuscode:200',
                  'collapse': 'timestamp:8', 'limit': '4'}
        url = 'https://web.archive.org/cdx/search/cdx?' + urllib.parse.urlencode(params)
        name = f'REPAIR_DATE_ARCHIVE_{category}_20261029.json'
    elif key.startswith(('list:', 'listnew:')):
        mode, category, offset = key.split(':')
        month = '2025-10' if mode == 'listnew' else '2510'
        url = f'https://arxiv.org/list/{category}/{month}?skip={int(offset)}&show=2000'
        name = f'REPAIR_DATE_{mode.upper()}_{category}_{offset}_20261029.html'
    elif key.startswith('date:'):
        key = key.split(':', 1)[1]
        params = {'advanced': '', 'terms-0-operator': 'AND', 'terms-0-term': key,
                  'terms-0-field': 'all', 'classification-include_cross_list': 'include',
                  'date-filter_by': 'date_range', 'date-from_date': '2025-10-21',
                  'date-to_date': '2025-10-21', 'date-date_type': 'announced_date_first',
                  'abstracts': 'show', 'size': 50, 'order': '-announced_date_first'}
        url = 'https://arxiv.org/search/advanced?' + urllib.parse.urlencode(params)
        name = f'REPAIR_ANNOUNCE_QUERY_{key}_20261029.html'
    else:
        url = f'https://arxiv.org/abs/{key}'
        name = f'REPAIR_CURRENT_{key}_20261029.html'
    if (ROOT/name).exists():
        print(key, 'EXISTS', flush=True)
        continue
    record = {'url': url, 'fetched': datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            content = response.read()
            (ROOT/name).write_bytes(content)
            record.update(status=response.status, bytes=len(content), headers=dict(response.headers))
    except Exception as exc:
        record['error'] = str(exc)
    (ROOT/(name+'.request.json')).write_text(json.dumps(record, indent=2))
    print(key, record.get('status', record.get('error')), record.get('bytes'), flush=True)
