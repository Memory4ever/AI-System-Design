"""Build an inspectable navigation inventory, not a contribution classifier."""
import datetime as dt
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

base = Path(__file__).parent
ns = {'a': 'http://www.w3.org/2005/Atom'}
known = {}
for f in (base / 'supplement-20261013').glob('arxiv-*.raw'):
    for e in ET.parse(f).findall('a:entry', ns):
        identity = re.search(r'(\d{4}\.\d{4,5})v', e.findtext('a:id', namespaces=ns)).group(1)
        known[identity] = {'submitted': e.findtext('a:published', namespaces=ns),
                           'title': e.findtext('a:title', namespaces=ns)}

records = {}
for group in ['model', 'systems', 'multimodal', 'agent']:
    fs = [base / f'repair-discover-valid-{group}-1.raw'] + sorted(base.glob(f'repair-discover-sorted-{group}-*.raw'))
    seen = []
    for f in fs:
        x = json.loads(f.read_text())
        for d in x['data']:
            seen.append(d['id'])
            a = d['attributes']
            identity = a['doi'].split('arxiv.')[-1]
            if identity not in records:
                records[identity] = {'id': identity, 'source': f.name, 'attributes': a,
                                     'client': d['relationships']['client']['data']['id'], 'groups': []}
            records[identity]['groups'].append(group)
    assert len(seen) == len(set(seen)) == x['meta']['total'], (group, len(seen), len(set(seen)), x['meta'])

def earliest(submitted):
    local = dt.datetime.fromisoformat(submitted.replace('Z', '+00:00')).astimezone(ZoneInfo('America/New_York'))
    cutoff = local.replace(hour=14, minute=0, second=0, microsecond=0)
    if local >= cutoff:
        cutoff += dt.timedelta(days=1)
    while cutoff.weekday() >= 5:
        cutoff += dt.timedelta(days=1)
    day = cutoff.date()
    if day.weekday() == 4:
        day += dt.timedelta(days=2)
    return dt.datetime.combine(day, dt.time(20), ZoneInfo('America/New_York')).astimezone(dt.timezone.utc)

for identity, r in records.items():
    a = r['attributes']
    v1s = [d['date'] for d in a['dates'] if d['dateType'] == 'Submitted' and d.get('dateInformation') == 'v1']
    r['v1_submitted'] = v1s
    if len(v1s) == 1 and a['state'] == 'findable' and r['client'] == 'arxiv.content':
        lo = earliest(v1s[0])
        hi = dt.datetime.fromisoformat(a['registered'].replace('Z', '+00:00'))
        r['earliest_announcement'] = lo.isoformat()
        r['registered_upper'] = hi.isoformat()
        r['bjt_date'] = str(lo.astimezone(ZoneInfo('Asia/Shanghai')).date()) if lo <= hi and lo.astimezone(ZoneInfo('Asia/Shanghai')).date() == hi.astimezone(ZoneInfo('Asia/Shanghai')).date() else None
    r['old_discovery'] = identity in known

out = {'known': known, 'records': records}
(base / 'repair-inventory-20261026.json').write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n')
print('known', len(known), 'new registered navigation', len(records), 'intersection', len(set(known) & records.keys()), 'difference', len(records.keys() - known.keys()))
print('date outcomes', {d: sum(r.get('bjt_date') == d for r in records.values()) for d in sorted({r.get('bjt_date') for r in records.values()}, key=str)})
for i, identity in enumerate(sorted(records.keys() - known.keys()), 1):
    r = records[identity]
    print(i, identity, r['v1_submitted'], r.get('bjt_date'), '|', r['attributes']['titles'][0]['title'])
