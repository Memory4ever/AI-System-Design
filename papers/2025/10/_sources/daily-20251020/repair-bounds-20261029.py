import collections
import datetime as dt
import json
import pathlib
from zoneinfo import ZoneInfo

ROOT = pathlib.Path(__file__).resolve().parent
NY = ZoneInfo('America/New_York')
BJT = ZoneInfo('Asia/Shanghai')
START = dt.datetime(2025, 10, 19, tzinfo=BJT)
END = START + dt.timedelta(days=1)

def parse(value):
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00'))

def earliest(submitted):
    local = submitted.astimezone(NY)
    day = local.date()
    for offset in range(8):
        candidate = day + dt.timedelta(days=offset)
        if candidate.weekday() > 4:
            continue
        cutoff = dt.datetime.combine(candidate, dt.time(14), NY)
        if cutoff < local:
            continue
        if candidate.weekday() == 4:
            candidate += dt.timedelta(days=2)
        return dt.datetime.combine(candidate, dt.time(20), NY).astimezone(BJT)
    raise ValueError('No deadline found')

rows = []
for index in range(1, 5):
    name = f'REPAIR_DC_EXACT_{index}_20261029.json'
    for item in json.loads((ROOT / name).read_text())['data']:
        a = item['attributes']
        versions = [d['date'] for d in a['dates'] if d['dateType'] == 'Submitted' and d.get('dateInformation') == 'v1']
        client = item['relationships']['client']['data']['id']
        identity = item['id'].removeprefix('10.48550/arxiv.')
        assert a['doi'] == item['id'] and a['url'].lower().endswith('/' + identity)
        assert len(versions) == 1 and a['state'] == 'findable' and client == 'arxiv.content'
        upper = parse(a['registered']).astimezone(BJT)
        lower = earliest(parse(versions[0])) if versions[0].startswith('2025-10') else None
        if upper < START:
            decision = 'first-before-window-upper-bound'
        elif lower is not None and lower >= END and lower <= upper:
            decision = 'first-after-window-joint-bound'
        else:
            decision = 'cross-window-unresolved'
        rows.append({'id':identity, 'source':name, 'doi':item['id'], 'title':a['titles'][0]['title'],
                     'v1_submitted':versions[0], 'client':client, 'state':a['state'],
                     'created':a['created'], 'registered':a['registered'],
                     'earliest_BJT':lower.isoformat() if lower else None,
                     'latest_BJT':upper.isoformat(), 'decision':decision,
                     'single_BJT_date':lower.date().isoformat() if lower and lower <= upper and lower.date() == upper.date() else None})
rows.sort(key=lambda x:x['id'])
(ROOT/'REPAIR_DATE_BOUNDS_20261029.json').write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print(collections.Counter(r['decision'] for r in rows))
for row in rows:
    if row['decision'] == 'cross-window-unresolved':
        print(json.dumps(row, ensure_ascii=False))
