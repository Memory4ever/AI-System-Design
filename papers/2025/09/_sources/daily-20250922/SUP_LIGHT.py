import json
import re
from pathlib import Path

from bs4 import BeautifulSoup

from SUP_CAPTURE import capture

ROOT = Path(__file__).resolve().parent
OUTSIDE = set('16743 16767 16810 16813 16835 16858 16859 16869 16900 16912 16935 16955 16957 16963 16973 17024 17044 17047 17065 17068 17131 21358'.split())
rows = json.loads((ROOT / 'SUP_DISCOVERY.json').read_text())
result = []
for row in rows:
    identifier, version = row['id'].rsplit('/', 1)[-1].split('v')
    if identifier.split('.')[1] in OUTSIDE:
        continue
    exact = 'SUP_' + identifier + 'v1.abs'
    if not (ROOT / (exact + '.raw')).exists():
        capture(exact, 'https://arxiv.org/abs/' + identifier + 'v1')
    current = exact
    if version != '1':
        current = 'SUP_' + identifier + '.current'
        if not (ROOT / (current + '.raw')).exists():
            capture(current, 'https://arxiv.org/abs/' + identifier)
    soup = BeautifulSoup((ROOT / (current + '.raw')).read_bytes(), 'html.parser')
    fields = {}
    for selector in ['.title', '.dateline', '.comments', '.submission-history', '.withdrawn', '.journal-ref']:
        fields[selector] = [node.get_text(' ', strip=True) for node in soup.select(selector)]
    notice = []
    for node in soup.select('.extra-services, .abs-meta, .leftcolumn'):
        text = node.get_text(' ', strip=True)
        for sentence in re.split(r'(?<=[.!?])\s+', text):
            if re.search(r'withdraw|corrig|errat|correct|revision|safety', sentence, re.I):
                notice.append(sentence)
    result.append(dict(id=identifier, current_file=current + '.raw', exact_file=exact + '.raw', fields=fields, notices=notice))
(ROOT / 'SUP_CURRENT_LIGHT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
print('LIGHT_ROWS', len(result))
