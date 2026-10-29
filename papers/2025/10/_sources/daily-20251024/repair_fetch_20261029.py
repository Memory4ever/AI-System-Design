"""Bounded same-day primary metadata retrieval; raw responses are not review."""
import json
from pathlib import Path
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[4] / 'scripts'))
from arxiv_publication_date import publication_date_envelope

TOPICS = {
    'model': '(transformer OR "mixture of experts" OR distillation OR pretraining OR "language model training")',
    'agent': '(agent OR agentic OR "retrieval augmented" OR "language model memory")',
    'multimodal': '("world model" OR "vision language" OR diffusion OR autoregressive OR "multimodal foundation")',
    'system': '("LLM serving" OR "LLM inference" OR "GPU kernel" OR "distributed training" OR "KV cache" OR "speculative decoding")',
    'eval': '("language model evaluation" OR "prompt injection" OR "language model safety" OR "language model benchmark")',
}

def fetch(label, params):
    url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode(params)
    stamp = datetime.now(timezone.utc).isoformat()
    with urllib.request.urlopen(url, timeout=50) as response:
        raw = response.read()
        headers = dict(response.headers)
    target = ROOT / ('REPAIR_' + label + '_20261029.json')
    target.write_bytes(raw)
    target.with_suffix('.request.json').write_text(json.dumps({'url': url, 'time': stamp, 'headers': headers}, indent=2))
    return json.loads(raw)

if __name__ == '__main__':
    if sys.argv[1] in ('discover', 'synonyms'):
        if sys.argv[1] == 'synonyms':
            TOPICS = {
                'model': '(transformers OR "mixtures of experts" OR "pre-training" OR "knowledge distillation")',
                'agent': '(agents OR "retrieval-augmented" OR "LLM memory")',
                'multimodal': '("world models" OR "vision-language" OR "diffusion models" OR "auto-regressive" OR "vision language action")',
                'system': '("large language model inference" OR "large language model serving" OR "GPU kernels" OR "KV-cache" OR "speculative decoders")',
                'eval': '("LLM evaluation" OR "prompt injections" OR "LLM safety" OR "LLM benchmark")',
            }
        for name, topic in TOPICS.items():
            query = 'registered:[2025-10-22T16:00:00Z TO 2025-10-23T15:59:59Z] AND titles.title:' + topic
            if name == 'model':
                query += ' AND descriptions.description:("language model" OR foundation OR "neural network")'
            page = 1
            while True:
                prefix = 'SYNONYMS_' if sys.argv[1] == 'synonyms' else 'REGISTERED_'
                data = fetch(prefix + name + '_p' + str(page), {'client-id': 'arxiv.content', 'query': query, 'page[size]': 100, 'page[number]': page})
                print(name, page, data.get('meta', {}).get('total'), len(data['data']), flush=True)
                for item in data['data']:
                    a = item['attributes']
                    print(item['id'], a['titles'][0]['title'], a.get('registered'), flush=True)
                if not data.get('links', {}).get('next'):
                    break
                page += 1
    elif sys.argv[1] == 'known':
        texts = '\n'.join((ROOT / name).read_text() for name in ('SCREENING.md', 'SUP_ARXIV_20261015.md'))
        ids = sorted(set(re.findall(r'\b\d{4}\.\d{4,5}\b', texts)))
        results = []
        for offset in range(0, len(ids), 40):
            group = ids[offset:offset + 40]
            query = 'doi:(' + ' OR '.join('"10.48550/arXiv.' + ident + '"' for ident in group) + ')'
            data = fetch('KNOWN_p' + str(offset // 40 + 1), {'client-id': 'arxiv.content', 'query': query, 'page[size]': 100})
            for item in data['data']:
                ident = item['id'].lower().split('arxiv.')[-1]
                result = publication_date_envelope(item, ident)
                results.append(result)
                print(ident, result['status'], result['bounded_bjt_date'], result['reasons'], flush=True)
        (ROOT / 'REPAIR_KNOWN_BOUNDS_20261029.json').write_text(json.dumps(results, indent=2))
    elif sys.argv[1] in ('primary', 'pdf', 'abstracts'):
        for ident in sys.argv[2:]:
            kinds = ('pdf',) if sys.argv[1] == 'pdf' else ('abs',) if sys.argv[1] == 'abstracts' else ('abs', 'html')
            for kind in kinds:
                suffix = '.pdf' if kind == 'pdf' else '.html'
                target = ROOT / ('REPAIR_' + ident + 'v1_' + kind + '_20261029' + suffix)
                if target.exists():
                    continue
                url = 'https://arxiv.org/' + kind + '/' + ident + 'v1'
                record = {'url': url, 'time': datetime.now(timezone.utc).isoformat()}
                try:
                    with urllib.request.urlopen(url, timeout=25) as response:
                        target.write_bytes(response.read())
                        record.update(status=response.status, headers=dict(response.headers))
                    print(ident, kind, target.stat().st_size, flush=True)
                except Exception as exc:
                    record['error'] = str(exc)
                    print(ident, kind, record['error'], flush=True)
                target.with_suffix('.request.json').write_text(json.dumps(record, indent=2))
