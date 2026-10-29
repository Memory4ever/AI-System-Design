"""Recompute the contract's lower/upper bounds; does not prove global first publication."""
import datetime as dt
import json
from pathlib import Path
from zoneinfo import ZoneInfo

p = Path(__file__).resolve().parent
items = {}
for f in sorted(p.glob('REPAIR_DC_V2_*REGISTERED*.raw')):
    for item in json.loads(f.read_text())['data']:
        items[item['id']] = item
ny = ZoneInfo('America/New_York')
bjt = ZoneInfo('Asia/Shanghai')
out = []
for ident, item in sorted(items.items()):
    a = item['attributes']
    submitted = [x for x in a['dates'] if x['dateType'] == 'Submitted' and x.get('dateInformation') == 'v1']
    row = {'doi': ident, 'title': a['titles'][0]['title'], 'submitted_v1_fields': submitted,
           'registered': a.get('registered'), 'state': a.get('state'),
           'client': item['relationships']['client']['data']['id']}
    if len(submitted) == 1 and a.get('registered'):
        s = dt.datetime.fromisoformat(submitted[0]['date'].replace('Z', '+00:00')).astimezone(ny)
        for offset in range(8):
            day = s.date() + dt.timedelta(days=offset)
            if day.weekday() not in (6, 0, 1, 2, 3):
                continue
            cutoff_day = day - dt.timedelta(days=2) if day.weekday() == 6 else day
            cutoff = dt.datetime.combine(cutoff_day, dt.time(14), ny)
            if s <= cutoff:
                lower = dt.datetime.combine(day, dt.time(20), ny).astimezone(bjt)
                break
        upper = dt.datetime.fromisoformat(a['registered'].replace('Z', '+00:00')).astimezone(bjt)
        row.update(earliest_scheduled_announcement=lower.isoformat(), latest_registration_bound=upper.isoformat(),
                   same_bjt_target_day=(lower <= upper and lower.date() == upper.date() == dt.date(2025, 10, 27)
                       and row['state'] == 'findable' and row['client'] == 'arxiv.content'))
    out.append(row)
(p / 'REPAIR_DATE_BOUNDS_20261029.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))
print('records', len(out), 'same-day', sum(x.get('same_bjt_target_day', False) for x in out))
print('unresolved', [(x['doi'], x.get('earliest_scheduled_announcement')) for x in out if not x.get('same_bjt_target_day')])
