"""Fetch only named exact-version originals; no reading/completion inference."""
import json
import sys
import urllib.request
from datetime import datetime, timezone
from REPAIR_fetch_20261029 import ROOT

for key in sys.argv[1:]:
    name = f'REPAIR_{key}v1_20261029.html'
    url = f'https://arxiv.org/html/{key}v1'
    if (ROOT/name).exists():
        print(key, 'EXISTS', flush=True)
        continue
    record = {'url':url, 'fetched':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=40) as response:
            content=response.read()
            (ROOT/name).write_bytes(content)
            record.update(status=response.status, headers=dict(response.headers), bytes=len(content))
    except Exception as exc:
        record['error']=str(exc)
    (ROOT/(name+'.request.json')).write_text(json.dumps(record,indent=2))
    print(key, record.get('status', record.get('error')),record.get('bytes'),flush=True)
