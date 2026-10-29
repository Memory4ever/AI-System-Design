"""Recompute only the already discovered identities and retain interval fields."""
import importlib.util
import json
from pathlib import Path
import re

base = Path(__file__).parent
spec = importlib.util.spec_from_file_location('inventory', base / 'repair-20261026-inventory.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
records = dict(module.records)
for f in base.glob('repair-doi-batch-*.raw'):
    for d in json.loads(f.read_text())['data']:
        a = d['attributes']
        identity = a['doi'].split('arxiv.')[-1]
        records.setdefault(identity, {'id': identity, 'source': f.name, 'attributes': a,
                                      'client': d['relationships']['client']['data']['id']})

block = (base / 'SUP_FRONT_REUSE_20261013.md').read_text().split(chr(96) * 3)[1]
b = [i if '.' in i else '2510.' + i for i in re.findall(r'2511\.11581|\b\d{5}\b', block)]
block = (base / 'SUP_DATE_20261013.md').read_text().split(chr(96) * 3)[1]
a = ['2510.' + i for i in re.findall(r'\b\d{5}\b', block)]
out = {}
for identity in a + b:
    item = {'id': identity, 'legacy_group': 'A' if identity in a else 'B'}
    submitted = module.known[identity]['submitted']
    item['atom_v1_submitted'] = submitted
    lo = module.earliest(submitted)
    item['earliest_announcement_utc'] = lo.isoformat()
    r = records.get(identity)
    if r:
        attr = r['attributes']
        v1s = [d['date'] for d in attr['dates'] if d['dateType'] == 'Submitted' and d.get('dateInformation') == 'v1']
        item.update(raw=r['source'], client=r['client'], state=attr['state'], doi=attr['doi'], registered=attr['registered'], datacite_v1_submitted=v1s)
        assert v1s == [submitted], (identity, submitted, v1s)
        hi = module.dt.datetime.fromisoformat(attr['registered'].replace('Z', '+00:00'))
        assert lo <= hi
        item['date'] = str(lo.astimezone(module.ZoneInfo('Asia/Shanghai')).date()) if lo.astimezone(module.ZoneInfo('Asia/Shanghai')).date() == hi.astimezone(module.ZoneInfo('Asia/Shanghai')).date() else None
    else:
        item['date'] = None
    item['arxiv_earliest_after_window'] = lo.astimezone(module.ZoneInfo('Asia/Shanghai')).date() > module.dt.date(2025, 10, 8)
    out[identity] = item
(base / 'repair-legacy-dates-20261026.json').write_text(json.dumps(out, indent=2) + '\n')
print('LEGACY A',len(a),'B',len(b))
for group in ['A', 'B']:
    rs = [r for r in out.values() if r['legacy_group'] == group]
    print(group, 'Oct08', sum(r['date']=='2025-10-08' for r in rs), 'earliest after', sum(r['arxiv_earliest_after_window'] for r in rs), 'other', [r['id'] for r in rs if r['date']!='2025-10-08' and not r['arxiv_earliest_after_window']])
