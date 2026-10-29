"""Bounded source recovery for explicitly selected identities in this day only."""
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

HERE = Path(__file__).resolve().parent
kind, *identities = sys.argv[1:]
requests = []
if kind == 'extra19':
    query = 'doi:(' + ' OR '.join('10.48550/arxiv.' + i for i in identities) + ')'
    jobs = [('REPAIR_EXTRA19_DATACITE_20261029', 'https://api.datacite.org/dois?' + urlencode({'query': query, 'page[size]': 100}), '.json')]
elif kind == 'v1':
    jobs = [(f'REPAIR_{i}v1_20261029', 'https://arxiv.org/html/' + i + 'v1', '.html') for i in identities]
elif kind == 'current_api':
    jobs = [('REPAIR_CURRENT_API_20261029', 'https://export.arxiv.org/api/query?' + urlencode({'id_list': ','.join(identities), 'max_results': 100}), '.xml')]
else:
    raise SystemExit('Expected extra19 or v1')
for name, url, extension in jobs:
    path = HERE / (name + extension)
    if path.exists() and path.stat().st_size:
        print(name, 'existing', flush=True)
        continue
    result = subprocess.run(['curl', '-sS', '-L', '--max-time', '40', '-D', str(HERE / (name + '.headers')), '-o', str(path), '-w', '%{http_code}', url], capture_output=True, text=True)
    request = {'name': name, 'url': url, 'at': datetime.now(timezone.utc).isoformat(), 'exit': result.returncode, 'http': result.stdout, 'error': result.stderr}
    (HERE / (name + '.request.json')).write_text(json.dumps(request, indent=2) + '\n')
    print(name, result.returncode, result.stdout, path.stat().st_size if path.exists() else 0, flush=True)
