"""Bounded DataCite navigation for the Oct 8 BJT registration window."""
import json
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

base = Path(__file__).parent
groups = {
    'model': '("language model" OR "language models" OR LLM OR LLMs OR Transformer OR Transformers OR "mixture of experts" OR "foundation model" OR "foundation models")',
    'systems': '(GPU OR GPUs OR kernel OR kernels OR accelerator OR accelerators OR "distributed training" OR "model serving" OR "KV cache" OR "KV-cache" OR quantization OR parallelism OR compiler OR compilers)',
    'multimodal': '("vision language" OR "vision-language" OR "world model" OR "world models" OR "vision language action" OR VLA OR "diffusion model" OR "diffusion models" OR "multimodal model" OR "multimodal models")',
    'agent': '(agent OR agents OR "tool calling" OR "tool use" OR "retrieval augmented" OR "retrieval-augmented" OR reasoning OR "reinforcement learning")',
}
group = sys.argv[1]
query = 'registered:[2025-10-07T16:00:00Z TO 2025-10-08T15:59:59.999Z] AND ' + groups[group]
page = 1
while True:
    url = 'https://api.datacite.org/dois?' + urlencode({'client-id': 'arxiv.content', 'query': query, 'page[size]': 100, 'page[number]': page, 'sort': 'registered'})
    name = f'repair-discover-valid-{group}-1' if page == 1 else f'repair-discover-sorted-{group}-{page}'
    if not (base / (name + '.raw')).exists():
        subprocess.run([sys.executable, str(base / 'repair-20261026-fetch.py'), name, url], check=True)
    data = json.loads((base / (name + '.raw')).read_text())
    print(json.dumps({'page': page, 'meta': data.get('meta'), 'ids': [d['id'] for d in data.get('data', [])]}))
    if page >= data['meta']['totalPages']:
        break
    page += 1
