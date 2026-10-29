"""Recompute date bounds, preserving raw date fields and metadata roles."""
import json
from datetime import datetime, timedelta, time
from zoneinfo import ZoneInfo
from REPAIR_fetch_20261029 import ROOT

def earliest(raw):
    submitted = datetime.fromisoformat(raw.replace('Z', '+00:00')).astimezone(ZoneInfo('America/New_York'))
    day = submitted.date()
    cutoff = datetime.combine(day, time(14), submitted.tzinfo)
    if day.weekday() in (5, 6):
        day += timedelta(days=7-day.weekday())
    elif day.weekday()==4:
        day += timedelta(days=2 if submitted <= cutoff else 3)
    elif day.weekday()==3 and submitted > cutoff:
        day += timedelta(days=3)
    elif submitted > cutoff:
        day += timedelta(days=1)
    return datetime.combine(day, time(20), submitted.tzinfo).astimezone(ZoneInfo('Asia/Shanghai'))

for label, pattern in [('OLD', 'REPAIR_OLD_DATES_B*_20261029.json'), ('DISCOVERY', 'REPAIR_VALID_REGISTERED_*_P1_20261029.json')]:
    rows = {}
    for path in sorted(ROOT.glob(pattern)):
        for record in json.loads(path.read_text())['data']:
            a = record['attributes']
            v1 = [d['date'] for d in a['dates'] if d['dateType']=='Submitted' and d.get('dateInformation')=='v1']
            client = record['relationships']['client']['data']['id']
            row = {'id':record['id'], 'raw_file':path.name, 'title':a['titles'][0]['title'], 'v1':v1, 'created':a['created'], 'registered':a['registered'], 'client':client, 'state':a['state']}
            if len(v1)==1 and client=='arxiv.content' and a['state']=='findable':
                lo = earliest(v1[0])
                hi = datetime.fromisoformat(a['registered'].replace('Z','+00:00')).astimezone(ZoneInfo('Asia/Shanghai'))
                row.update(lower=lo.isoformat(), upper=hi.isoformat())
                if lo > hi:
                    row['result']='CONFLICT'
                elif lo.date()==hi.date():
                    row['result']='IN' if str(lo.date())=='2025-10-21' else 'OUT'
                    row['public_day_bound']=str(lo.date())
                elif str(lo.date())>'2025-10-21' or str(hi.date())<'2025-10-21':
                    row['result']='OUT_INTERVAL'
                else:
                    row['result']='CROSS'
            else:
                row['result']='MISSING'
            rows[record['id']]=row
    (ROOT/f'REPAIR_{label}_BOUNDS_20261029.json').write_text(json.dumps(list(rows.values()),indent=2,ensure_ascii=False))
    from collections import Counter
    print(label,len(rows),dict(Counter(row['result'] for row in rows.values())))
    for row in rows.values():
        if row['result']=='CROSS':
            print(row['id'],row['result'],row.get('lower'),row.get('upper'),row['title'])
