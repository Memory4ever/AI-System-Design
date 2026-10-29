import base64
import json
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

B = Path(__file__).parent
NY = ZoneInfo('America/New_York')
BJT = ZoneInfo('Asia/Shanghai')

def earliest(submitted):
    local = datetime.fromisoformat(submitted.replace('Z', '+00:00')).astimezone(NY)
    for offset in range(8):
        cutoff = (local + timedelta(days=offset)).replace(hour=14, minute=0, second=0, microsecond=0)
        if cutoff.weekday() < 5 and local <= cutoff:
            return cutoff.replace(hour=20) + timedelta(days=2 if cutoff.weekday() == 4 else 0)
    raise ValueError(submitted)

def main():
    records = {}
    old = set()
    for p in B.glob('REPAIR_DC_OLD_*.json'):
        for x in json.loads(p.read_text())['data']:
            old.add(x['id'])
            records[x['id']] = x
    for p in B.glob('REPAIR_DC_VALID_registered_*.json'):
        for x in json.loads(p.read_text())['data']:
            records[x['id']] = x
    rows = []
    for doi, x in sorted(records.items()):
        a = x['attributes']
        dates = [d['date'] for d in a.get('dates', []) if d.get('dateInformation') == 'v1' and d['dateType'] == 'Submitted']
        client = x['relationships']['client']['data']['id']
        row = {'doi': doi, 'old': doi in old, 'title': a['titles'][0]['title'], 'v1_submitted': dates, 'client': client, 'state': a['state'], 'created': a['created'], 'registered': a['registered'], 'version': a.get('version'), 'signals': [d for d in a.get('dates', []) if d['dateType'] == 'Withdrawn']}
        if len(dates) != 1 or client != 'arxiv.content' or a['state'] != 'findable':
            row['result'] = 'missing_or_conflict'
        else:
            lower = earliest(dates[0]).astimezone(BJT)
            upper = datetime.fromisoformat(a['registered'].replace('Z', '+00:00')).astimezone(BJT)
            row.update(lower=lower.isoformat(), upper=upper.isoformat())
            if lower > upper:
                row['result'] = 'conflict'
            elif lower.date().isoformat() > '2025-10-20':
                row['result'] = 'arxiv_first_after_window'
            elif upper.date().isoformat() < '2025-10-20':
                row['result'] = 'arxiv_first_before_window'
            elif lower.date() == upper.date():
                row['result'] = 'arxiv_first_2025-10-20'
            else:
                row['result'] = 'cross_day_interval'
        rows.append(row)
    (B / 'REPAIR_DATE_BOUNDS_20261029.json').write_text(json.dumps(rows, indent=2))
    for old_flag in [True, False]:
        print('old', old_flag, Counter(r['result'] for r in rows if r['old'] == old_flag))
    reg = {x['id'] for p in B.glob('REPAIR_DC_VALID_registered_*.json') for x in json.loads(p.read_text())['data']}
    created = {x['id'] for p in B.glob('REPAIR_DC_VALID_created_*.json') for x in json.loads(p.read_text())['data']}
    print('registered', len(reg), 'created', len(created), 'registered-created', sorted(reg-created), 'created-registered', sorted(created-reg))
    for row in rows:
        if not row['old'] and row['result'] != 'arxiv_first_2025-10-20':
            print(row['doi'], row['result'], row.get('lower'), row.get('upper'))
    rule = B / 'REPAIR_ARXIV_RULE_2025_20261029.json'
    if rule.exists():
        print(base64.b64decode(json.loads(rule.read_text())['content']).decode())

if __name__ == '__main__':
    main()
