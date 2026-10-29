import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[5]/'scripts'))
from arxiv_publication_date import publication_date_envelope
p=Path(__file__).parent
known={r['arxiv_id'] for r in json.loads((p/'REPAIR_DATES_20261028.json').read_text())}|{'2510.14528','2510.14880'}
records={}
for name in ['MODEL','TRAIN','AGENT','MULTIMODAL','RUNTIME']:
    raw=json.loads((p/f'REPAIR_DISCOVERY_{name}_20261028.json').read_text())
    for r in raw.get('data',[]):records[r['id']]=r
rows=[]
for doi,r in sorted(records.items()):
    identity=doi.split('arxiv.')[-1]
    if identity in known:continue
    env=publication_date_envelope(r,identity)
    rows.append(dict(id=identity,title=r['attributes']['titles'][0]['title'],envelope=env,raw=r))
(p/'REPAIR_DISCOVERY_DELTA_20261028.json').write_text(json.dumps(rows,indent=2))
for r in rows:print(r['id'],r['envelope']['bounded_bjt_date'] or '/'.join(r['envelope']['reasons']),r['title'])
