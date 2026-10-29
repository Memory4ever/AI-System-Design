"""Bounded metadata recovery; raw responses remain separate from judgments."""
import json
import re
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from datetime import datetime, timezone

BASE = Path(__file__).parent
TOPICS = {
    'MODEL': 'attention OR "mixture of experts" OR "language model" OR "language models" OR transformer OR transformers',
    'TRAIN': 'distillation OR pretraining OR "pre-training" OR "reinforcement learning"',
    'AGENT': 'agent OR agents OR RAG OR "memory retrieval"',
    'MULTI': '"world model" OR "world models" OR "vision language" OR "vision-language" OR "video diffusion" OR "multimodal model" OR "multimodal models"',
    'SYSTEM': '"KV cache" OR "KV-cache" OR "speculative decoding" OR "LLM inference" OR "GPU kernel" OR "GPU kernels" OR "distributed training"',
}

def fetch(name, url):
    path = BASE / name
    if path.exists():
        return json.loads(path.read_text())
    with urlopen(Request(url, headers={'User-Agent': 'ResearchDateAudit/1.0'}), timeout=40) as response:
        body = response.read()
    data = json.loads(body)
    path.write_bytes(body)
    print(name, data.get('meta', {}).get('total'), flush=True)
    return data

def run():
    receipts = []
    for field in ['registered', 'created']:
        for topic, terms in TOPICS.items():
            query = f'{field}:[2025-10-19T16:00:00Z TO 2025-10-20T15:59:59.999Z] AND titles.title:({terms})'
            params = {'query': query, 'client-id': 'arxiv.content', 'page[size]': 1000, 'page[number]': 1}
            url = 'https://api.datacite.org/dois?' + urlencode(params)
            name = f'REPAIR_DC_VALID_{field}_{topic}_20261029.json'
            data = fetch(name, url)
            receipts.append({'file': name, 'url': url, 'executed': datetime.now(timezone.utc).isoformat(), 'total': data['meta']['total'], 'returned': len(data['data']), 'next': data.get('links', {}).get('next')})
    ids = set()
    for name in ['arxiv_model_training.raw', 'arxiv_multimodal.raw', 'arxiv_systems.raw', 'arxiv_agent.raw', 'supplement.xml', 'SUP_MODEL.raw', 'SUP_TRAIN_S25.raw', 'SUP_AGENT.raw', 'SUP_MULTI.raw', 'SUP_SYSTEM.raw']:
        ids.update(re.findall(r'(?:abs/|arxiv\.)(\d{4}\.\d{4,5})', (BASE / name).read_text()))
    ordered = sorted(ids)
    for start in range(0, len(ordered), 50):
        query = ' OR '.join('doi:10.48550/arxiv.' + item for item in ordered[start:start+50])
        url = 'https://api.datacite.org/dois?' + urlencode({'query': '('+query+')', 'page[size]': 1000})
        name = f'REPAIR_DC_OLD_{start}_20261029.json'
        data = fetch(name, url)
        receipts.append({'file': name, 'url': url, 'requested_ids': ordered[start:start+50], 'total': data['meta']['total'], 'returned': len(data['data'])})
    (BASE / 'REPAIR_FETCH_20261029.json').write_text(json.dumps(receipts, indent=2))

if __name__ == '__main__':
    run()
