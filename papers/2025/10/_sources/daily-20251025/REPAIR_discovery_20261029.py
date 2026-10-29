"""Inspect this day's finite DOI discovery, retaining raw dates and descriptions."""
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / 'scripts'))
from arxiv_publication_date import publication_date_envelope

records = {}
for group in ('MODEL', 'AGENT', 'MULTI', 'SYSTEM', 'EVAL'):
    payload = json.loads((HERE / f'READER_DISC_{group}_20261029.json').read_text())
    for record in payload['data']:
        records[record['id'].split('arxiv.')[1]] = record
identities = sorted(records)
for index, identity in enumerate(identities, 1):
    if sys.argv[1] == 'range':
        if not int(sys.argv[2]) <= index <= int(sys.argv[3]):
            continue
    elif identity not in sys.argv[1:]:
        continue
    record = records[identity]
    a = record['attributes']
    print(index, identity, a['titles'][0]['title'])
    envelope = publication_date_envelope(record, identity)
    print('DATE', envelope['bounded_bjt_date'], envelope['earliest_announcement_utc'], envelope['registered_upper_utc'], envelope['reasons'])
    for description in a.get('descriptions', []):
        if description.get('descriptionType') == 'Abstract':
            print('AB', description['description'])
