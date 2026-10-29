"""Exact existing identities only, never discovers from another report."""
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlencode
from urllib.request import urlopen
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[4] / 'scripts'))
from arxiv_publication_date import publication_date_envelope
screen = (ROOT / 'SCREENING.md').read_text()
ids = {'2510.'+s for s in re.findall(r'^\| (\d{5})v\d+ ', screen, re.M)}
supp = (ROOT / 'SUP_ARXIV_20261015.md').read_text()
ids.update(re.findall(r'https://arxiv.org/abs/(\d{4}\.\d{5})', supp))
query = ' OR '.join('doi:10.48550/arxiv.' + i for i in sorted(ids))
url = 'https://api.datacite.org/dois?' + urlencode({'query': query, 'client-id':'arxiv.content','page[size]':1000})
with urlopen(url, timeout=60) as response:
    raw = response.read()
(ROOT / 'REPAIR_OLD_DATES_20261029.raw.json').write_bytes(raw)
p = json.loads(raw)
assert not p.get('links',{}).get('next')
rows = {r['id'].split('arxiv.')[-1]: publication_date_envelope(r, r['id'].split('arxiv.')[-1]) for r in p['data']}
(ROOT / 'REPAIR_OLD_DATES_20261029.json').write_text(json.dumps({'url':url,'requested':sorted(ids),'missing':sorted(ids-set(rows)),'envelopes':rows},indent=2))
for i,r in rows.items(): print(i,r['bounded_bjt_date'],r['earliest_announcement_utc'],r['registered_upper_utc'],r['reasons'])
