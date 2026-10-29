"""Bounded discovery and identity metadata only; no admission decisions."""
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
TERMS = {
    'MODEL': 'attention OR transformer OR "mixture of experts" OR distillation OR pretraining OR "reinforcement learning"',
    'AGENT': 'agent OR agents OR agentic OR "retrieval augmented" OR "language model memory"',
    'MULTIMODAL': '"world model" OR "world models" OR "vision language" OR diffusion OR autoregressive OR "multimodal foundation" OR "vision language action"',
    'RUNTIME': '"LLM serving" OR "LLM inference" OR "GPU kernel" OR "GPU kernels" OR "distributed training" OR "KV cache" OR "speculative decoding"',
    'EVAL': '"language model evaluation" OR "prompt injection" OR "language model safety" OR "language model benchmark"',
}

def get(url, name):
    request = urllib.request.Request(url, headers={'User-Agent': 'AI-System-Design historical evidence audit'})
    start = time.time()
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            raw = response.read()
            (ROOT / name).write_bytes(raw)
            meta = {'url': url, 'status': response.status, 'headers': dict(response.headers), 'seconds': time.time()-start}
        data = json.loads(raw)
    except Exception as exc:
        meta = {'url': url, 'error': str(exc), 'seconds': time.time()-start}
        data = None
    (ROOT / (name+'.request.json')).write_text(json.dumps(meta, indent=2))
    return data

if __name__ == '__main__':
    for group, terms in TERMS.items():
        for field in ('created', 'registered'):
            query = f'{field}:[2025-10-20T16:00:00Z TO 2025-10-21T16:00:00Z}} AND titles.title:({terms})'
            for page in range(1, 6):
                params = {'query': query, 'client-id': 'arxiv.content', 'page[size]': 100, 'page[number]': page}
                data = get('https://api.datacite.org/dois?'+urllib.parse.urlencode(params), f'REPAIR_VALID_{field.upper()}_{group}_P{page}_20261029.json')
                print(group, field, page, data.get('meta') if data else 'ERROR', flush=True)
                if not data or page >= data.get('meta', {}).get('totalPages', 0):
                    break
