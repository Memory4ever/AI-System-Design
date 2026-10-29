"""Recover exact DOI date fields for this day's existing 73 contribution leads."""
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import urlencode
from lxml import etree, html

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / 'scripts'))
from arxiv_publication_date import publication_date_envelope

closed = set('2510.21131 2510.21193 2510.21084 2510.21228 2509.17470 2511.05511 2510.22095 2510.21993 2510.21967 2510.21370 2510.21178 2510.21177 2507.13937 2506.04654 2511.05510 2510.21424 2510.21299 2510.21219'.split())
ids = set()
for name in ('arxiv_model_training.raw', 'arxiv_agent.raw', 'arxiv_multimodal.raw', 'arxiv_systems.raw', 'arxiv_supp.raw'):
    doc = etree.parse(str(HERE / name))
    for url in doc.xpath('//*[local-name()="entry"]/*[local-name()="id"]/text()'):
        ids.add(re.search(r'(\d{4}\.\d{4,5})', url).group(1))
for name in ('MODEL', 'AGENT', 'MULTIMODAL', 'SYSTEM', 'EVAL'):
    doc = html.parse(str(HERE / f'SUP_{name}.html'))
    for url in doc.xpath('//li[contains(@class,"arxiv-result")]//p[contains(@class,"list-title")]/a[1]/@href'):
        ids.add(re.search(r'(\d{4}\.\d{4,5})', url).group(1))
assert len(ids) == 91, len(ids)
leads = sorted(ids - closed)
assert len(leads) == 73, len(leads)
query = 'doi:(' + ' OR '.join('10.48550/arxiv.' + identity for identity in leads) + ')'
url = 'https://api.datacite.org/dois?' + urlencode({'query': query, 'page[size]': 100, 'page[number]': 1})
raw = HERE / 'REPAIR_EXISTING73_DATACITE_20261029.json'
if not raw.exists():
    subprocess.run(['curl', '-sS', '-L', '--fail', '--max-time', '90', '-D', str(raw.with_suffix('.headers')), '-o', str(raw), url], check=True)
    (HERE / 'REPAIR_EXISTING73_REQUEST_20261029.json').write_text(json.dumps({'url': url, 'checked_at': datetime.now(timezone.utc).isoformat(), 'ids': leads, 'stop': 'one exact DOI batch; total and identities must match 73'}, indent=2) + '\n')
payload = json.loads(raw.read_text())
assert payload['meta']['total'] == 73, payload.get('meta')
records = {entry['id'].split('arxiv.')[1]: entry for entry in payload['data']}
assert set(records) == set(leads)
results = []
for identity in leads:
    record = records[identity]
    result = publication_date_envelope(record, identity)
    result['title'] = record['attributes']['titles'][0]['title']
    result['dates'] = record['attributes']['dates']
    results.append(result)
(HERE / 'REPAIR_EXISTING73_DATES_20261029.json').write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
for result in results:
    print(result['arxiv_id'], result['status'], result['bounded_bjt_date'], result['source_fields'].get('submitted_v1'), result['source_fields'].get('registered'), result['reasons'], result['title'])
