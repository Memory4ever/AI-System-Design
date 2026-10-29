"""Bounded same-topic created/registered discovery; raw metadata is not review."""
import json
from pathlib import Path
import sys
from urllib.parse import urlencode
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[4] / 'scripts'))
from arxiv_publication_date import publication_date_envelope

TERMS = {
    'MODEL': ['large language model', 'large language models', 'transformer', 'transformers', 'mixture of experts', 'long context'],
    'TRAIN': ['pretraining', 'pre-training', 'post-training', 'reinforcement learning', 'distributed training'],
    'AGENT': ['language agent', 'language agents', 'tool use', 'tool-use', 'retrieval augmented', 'retrieval-augmented', 'agent memory'],
    'MULTIMODAL': ['multimodal foundation', 'vision language', 'vision-language', 'world model', 'world models', 'diffusion model', 'diffusion models', 'vision language action'],
    'RUNTIME': ['LLM inference', 'GPU kernel', 'GPU kernels', 'model serving', 'tensor parallel', 'accelerator', 'accelerators', 'kernel', 'compiler'],
}
theme = ' OR '.join('titles.title:"' + t + '"' for ts in TERMS.values() for t in ts)
manifest = {'terms': TERMS, 'requests': [], 'sets': {}, 'records': {}}
for field in ['created', 'registered']:
    query = f'{field}:[2025-10-16T16:00:00Z TO 2025-10-17T15:59:59.999Z] AND ({theme})'
    url = 'https://api.datacite.org/dois?' + urlencode({'query': query, 'client-id': 'arxiv.content', 'page[size]': 1000})
    saved = ROOT / f'REPAIR_DISCOVERY_{field.upper()}_20261029.raw.json'
    if saved.exists():
        raw = saved.read_bytes()
    else:
        with urlopen(url, timeout=90) as response:
            raw = response.read()
            (ROOT / f'REPAIR_DISCOVERY_{field.upper()}_20261029.headers').write_text(str(response.headers))
        saved.write_bytes(raw)
    payload = json.loads(raw)
    assert not payload.get('links', {}).get('next'), 'Need bounded topic pagination'
    records = payload['data']
    manifest['requests'].append({'url': url, 'meta': payload['meta'], 'next': payload.get('links', {}).get('next')})
    manifest['sets'][field] = sorted(r['id'] for r in records)
    for record in records:
        identity = record['id'].lower().removeprefix('10.48550/arxiv.')
        manifest['records'][identity] = {'raw': record, 'envelope': publication_date_envelope(record, identity)}
manifest['registered_minus_created'] = sorted(set(manifest['sets']['registered']) - set(manifest['sets']['created']))
manifest['created_minus_registered'] = sorted(set(manifest['sets']['created']) - set(manifest['sets']['registered']))
(ROOT / 'REPAIR_DISCOVERY_20261029.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
print({k: len(v) for k, v in manifest['sets'].items()})
print('registered-created', len(manifest['registered_minus_created']))
for identity, value in manifest['records'].items():
    a = value['raw']['attributes']
    print(identity, value['envelope']['bounded_bjt_date'], a['titles'][0]['title'])
