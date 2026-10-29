"""Sequential, explicit-identity retrieval; no candidate selection."""
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

base = Path(__file__).parent
mode = sys.argv[1]
ids = [i if '.' in i else '2510.' + i for i in sys.argv[2:]]
if mode == 'doi':
    query = 'doi:(' + ' OR '.join('"10.48550/arxiv.' + i + '"' for i in ids) + ')'
    url = 'https://api.datacite.org/dois?' + urlencode({'client-id': 'arxiv.content', 'query': query, 'page[size]': 100})
    name = 'repair-doi-batch-' + ids[0].replace('.', '-')
    subprocess.run([sys.executable, str(base / 'repair-20261026-fetch.py'), name, url], check=True)
    x = json.loads((base / (name + '.raw')).read_text())
    print('returned', x.get('meta'), [d['id'] for d in x.get('data', [])])
elif mode in ('abs', 'core'):
    for identity in ids:
        name = 'repair-' + mode + '-' + identity + 'v1'
        if (base / (name + '.raw')).exists():
            continue
        url = 'https://arxiv.org/' + ('abs/' if mode == 'abs' else 'html/') + identity + 'v1'
        subprocess.run([sys.executable, str(base / 'repair-20261026-fetch.py'), name, url], check=True)
