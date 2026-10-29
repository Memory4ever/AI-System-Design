"""Bounded same-day metadata recovery; not contribution or publication proof."""
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[4] / 'scripts'))
from arxiv_publication_date import publication_date_envelope

TOPICS = {
    'model': 'titles.title:(transformer OR transformers OR "mixture of experts" OR distillation OR pretraining OR "language model training")',
    'agent': 'titles.title:(agent OR agents OR agentic OR "retrieval augmented" OR "language model memory")',
    'multimodal': 'titles.title:("world model" OR "world models" OR "vision language" OR diffusion OR autoregressive OR "multimodal foundation")',
    'system': 'titles.title:("LLM serving" OR "LLM inference" OR "GPU kernel" OR "GPU kernels" OR "distributed training" OR "KV cache" OR "speculative decoding")',
    'eval': 'titles.title:("language model evaluation" OR "prompt injection" OR "language model safety" OR "language model benchmark")',
}

def fetch(name, query, sparse=True):
    records = []
    for page in range(1, 5):
        path = ROOT / f'REPAIR_{name}_p{page}_20261029.json'
        params = {'query': query, 'client-id': 'arxiv.content', 'page[size]': 100, 'page[number]': page}
        if sparse:
            params['fields[dois]'] = 'doi,titles,descriptions,subjects,dates,created,registered,publisher,state,version,url'
        url = 'https://api.datacite.org/dois?' + urlencode(params)
        if path.exists():
            saved = json.loads(path.read_text())
            if saved['request_url'] != url:
                raise RuntimeError('request conflict')
        else:
            with urlopen(Request(url, headers={'User-Agent': 'AI-System-Design research'}), timeout=80) as response:
                saved = {'request_url': url, 'fetched_at': datetime.now().astimezone().isoformat(), 'payload': json.load(response)}
            path.write_text(json.dumps(saved, ensure_ascii=False))
        payload = saved['payload']
        records.extend(payload['data'])
        print(name, page, len(payload['data']), payload['meta']['total'], flush=True)
        if len(records) >= payload['meta']['total']:
            return records
    raise RuntimeError('bounded pagination incomplete')

if __name__ == '__main__':
    if sys.argv[1] == 'discover':
        for name, topic in TOPICS.items():
            fetch('REGISTERED_VALID_' + name, 'registered:[2025-10-21T16:00:00Z TO 2025-10-22T15:59:59.999Z] AND ' + topic)
    elif sys.argv[1] == 'potential':
        text = (ROOT / 'REPAIR_SCREEN_20261029.md').read_text().split('## 完整AB后具体排除C')[0]
        ids = sorted(set(re.findall(r'\b\d{4}\.\d{4,5}\b', text)))
        records = []
        for start in range(0, len(ids), 20):
            records.extend(fetch('POTENTIAL_FULL_' + str(start), ' OR '.join('doi:10.48550/arxiv.' + i for i in ids[start:start + 20]), sparse=False))
        results = [publication_date_envelope(r, r['id'].split('arxiv.')[-1]) for r in records]
        (ROOT / 'REPAIR_POTENTIAL_BOUNDS_20261029.json').write_text(json.dumps(results, indent=2))
        for r in results:
            print(r['arxiv_id'], r['bounded_bjt_date'], ','.join(r['reasons']), r['earliest_announcement_utc'], r['registered_upper_utc'])
    elif sys.argv[1] == 'reopened':
        ids = ['2510.18491', '2510.17919', '2510.18725', '2510.18291']
        records = fetch('REOPENED_FULL', ' OR '.join('doi:10.48550/arxiv.' + i for i in ids), sparse=False)
        results = [publication_date_envelope(r, r['id'].split('arxiv.')[-1]) for r in records]
        (ROOT / 'REPAIR_REOPENED_BOUNDS_20261029.json').write_text(json.dumps(results, indent=2))
        for r in results:
            print(r['arxiv_id'], r['bounded_bjt_date'], r['reasons'])
    elif sys.argv[1] == 'known':
        texts = [ROOT / 'SCREENING.md', ROOT / 'SUP_ARXIV_20261015.md', ROOT / 'SUP_REOPEN_20261015.md']
        ids = sorted(set(re.findall(r'\b\d{4}\.\d{4,5}\b', '\n'.join(p.read_text() for p in texts))))
        ids.append('2510.11370')
        for name in ['arxiv_agent.raw', 'arxiv_model_training.raw', 'arxiv_multimodal.raw', 'arxiv_systems.raw', 'supplement.raw', 'arxiv_supp2.raw']:
            ids.extend(re.findall(r'arxiv.org/abs/(\d{4}\.\d{4,5})', (ROOT / name).read_text()))
        records = fetch('KNOWN_COMPLETE', ' OR '.join('doi:10.48550/arxiv.' + i for i in sorted(set(ids))))
        results = [publication_date_envelope(r, r['id'].split('arxiv.')[-1]) for r in records]
        (ROOT / 'REPAIR_KNOWN_BOUNDS_20261029.json').write_text(json.dumps(results, indent=2))
        for r in results:
            print(r['arxiv_id'], r['bounded_bjt_date'], ','.join(r['reasons']))
