"""Bounded same-day discovery and exact DOI recovery; not contribution screening."""
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TOPICS = {
    "MODEL": ['language model', 'language models', 'mixture of experts', 'state space'],
    "TRAIN": ['post-training', 'pretraining', 'GRPO', 'preference optimization'],
    "AGENT": ['agent memory', 'tool use', 'retrieval augmented', 'language agent', 'language agents'],
    "MULTIMODAL": ['vision language action', 'world model', 'world models', 'diffusion model', 'diffusion models'],
    "RUNTIME": ['LLM serving', 'KV cache', 'speculative decoding', 'distributed training'],
}

def fetch(url, name):
    path = ROOT / name
    if path.exists():
        return json.loads(path.read_text())
    with urllib.request.urlopen(url, timeout=40) as r:
        raw = r.read()
    path.write_bytes(raw)
    return json.loads(raw)

log = []
for topic, words in TOPICS.items():
    for field in ['created', 'registered']:
        query = '(' + ' OR '.join('titles.title:"' + w + '"' for w in words) + ')'
        query += ' AND ' + field + ':[2025-10-17T16:00:00Z TO 2025-10-18T15:59:59.999Z]'
        params = {'query': query, 'client-id': 'arxiv.content', 'page[size]': '100', 'page[number]': '1'}
        url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode(params)
        page = 1
        while url:
            data = fetch(url, f'REPAIR_DISCOVERY_{topic}_{field}_{page}_20261029.json')
            ids = [x['id'] for x in data['data']]
            log.append({'topic': topic, 'field': field, 'page': page, 'url': url, 'meta': data['meta'], 'ids': ids})
            print(topic, field, page, data['meta'].get('total'), ids, flush=True)
            url = data.get('links', {}).get('next')
            page += 1
            if page > 10:
                raise RuntimeError('bounded stop: unexpected pagination')
(ROOT / 'REPAIR_DISCOVERY_LOG_20261029.json').write_text(json.dumps(log, indent=2))

screen = (ROOT / 'SCREENING.md').read_text().split('## 10完整题摘关闭')[0]
ids = set(re.findall(r'\[(\d{4}\.\d{4,5}) ', screen))
ids.update(['2510.16712', '2510.16685', '2510.16411', '2510.16367', '2510.17895', '2510.15716', '2510.15494', '2510.15333', '2510.16579'])
summary = []
for aid in sorted(ids):
    data = fetch('https://api.datacite.org/dois/10.48550/arxiv.' + aid, f'REPAIR_DOI_{aid}_20261029.json')['data']
    a = data['attributes']
    row = {k: a.get(k) for k in ['doi', 'state', 'created', 'registered', 'dates', 'titles']}
    row['client'] = data['relationships']['client']['data']['id']
    summary.append(row)
    print(aid, row['registered'], [d for d in row['dates'] if d.get('dateType') == 'Submitted'], flush=True)
(ROOT / 'REPAIR_DATES_20261029.json').write_text(json.dumps(summary, indent=2))

# Supplement legacy topic vocabulary without making a whole-category queue.
legacy = {
    'MODEL': ['transformer', 'foundation', 'MoE'],
    'SYSTEM': ['LLM', 'GPU', 'inference', 'training'],
    'AGENT': ['agent', 'retrieval', 'reasoning'],
    'MULTIMODAL': ['vision-language', 'VLA', 'multimodal', 'world-model', 'diffusion'],
}
extra = []
for topic, words in legacy.items():
    for field in ['created', 'registered']:
        query = '(' + ' OR '.join('titles.title:"' + w + '"' for w in words) + ')'
        query += ' AND ' + field + ':[2025-10-17T16:00:00Z TO 2025-10-18T15:59:59.999Z]'
        url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'query': query, 'client-id': 'arxiv.content', 'page[size]': '100'})
        data = fetch(url, f'REPAIR_LEGACY_{topic}_{field}_20261029.json')
        extra.append({'url': url, 'total': data['meta']['total'], 'ids': [x['id'] for x in data['data']]})
        if data.get('links', {}).get('next'):
            raise RuntimeError('legacy needs explicit pagination')
        print('LEGACY', topic, field, data['meta']['total'], flush=True)
for field in ['created', 'registered']:
    query = f'titles.title:"language model" AND {field}:[2025-10-20T16:00:00Z TO 2025-10-21T15:59:59.999Z]'
    url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'query': query, 'client-id': 'arxiv.content', 'page[size]': '1'})
    data = fetch(url, f'REPAIR_POSITIVE_{field}_20261029.json')
    extra.append({'url': url, 'total': data['meta']['total'], 'ids': [x['id'] for x in data['data']]})
    print('POSITIVE', field, data['meta']['total'], flush=True)
(ROOT / 'REPAIR_EXTRA_LOG_20261029.json').write_text(json.dumps(extra, indent=2))
