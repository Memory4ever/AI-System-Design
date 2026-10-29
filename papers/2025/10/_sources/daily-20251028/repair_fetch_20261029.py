"""Finite discovery recovery. Raw responses and exact requests stay local to this day."""
import datetime
import json
from pathlib import Path
import urllib.request
import urllib.parse

ROOT = Path(__file__).resolve().parent

def fetch(name, url, body=None, headers=None):
    h = {'User-Agent': 'Mozilla/5.0', **(headers or {})}
    data = None if body is None else json.dumps(body).encode()
    if data is not None:
        h['Content-Type'] = 'application/json'
    record = {'url': url, 'body': body, 'headers': h,
              'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=60) as r:
            raw = r.read()
            record.update(status=r.status, final_url=r.url, bytes=len(raw))
        (ROOT / (name + '.raw')).write_bytes(raw)
    except Exception as exc:
        record['error'] = str(exc)
        raw = b''
    (ROOT / (name + '.request.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2))
    print(name, {k: v for k, v in record.items() if k in ('status', 'bytes', 'error')}, flush=True)
    return raw

if __name__ == '__main__':
    import sys
    mode = sys.argv[1]
    if mode == 'web':
        fetch('REPAIR_HUNYUAN_ZH_ALL_20261029', 'https://api.hunyuan.tencent.com/api/blog/publicList',
              {'pageNum': 1, 'pageSize': 100, 'renderType': 0}, {'Accept-Language': 'zh'})
        fetch('REPAIR_HUNYUAN_RESEARCH_20261029', 'https://hunyuan.tencent.com/research')
        fetch('REPAIR_GOOGLE_LM_P1_20261029', 'https://research.google/pubs/?category=2025&search=language%20model')
        fetch('REPAIR_ARXIV_2025_RULE_20261029', 'https://raw.githubusercontent.com/arXiv/arxiv-docs/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md')
        fetch('REPAIR_DATACITE_DATE_RULE_20261029', 'https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api')
    elif mode == 'discovery':
        themes = {
            'LANGUAGE': '"language model" OR "language models" OR LLM OR LLMs OR "foundation model" OR "foundation models"',
            'ARCH': 'transformer OR transformers OR "mixture of experts" OR "mixture-of-experts" OR attention OR "state space model" OR "state-space models"',
            'TRAIN': '"pre-training" OR pretraining OR "post-training" OR "post training" OR "reinforcement learning" OR distillation OR quantization',
            'SYSTEM': '"GPU kernel" OR "GPU kernels" OR "model serving" OR "inference engine" OR "tensor parallel" OR "KV cache" OR "KV-cache"',
            'AGENT': '"language agent" OR "language agents" OR "AI agent" OR "AI agents" OR "tool use" OR "tool calling" OR "retrieval augmented" OR "retrieval-augmented"',
            'MULTIMODAL': 'multimodal OR "multi-modal" OR "vision language" OR "vision-language" OR "world model" OR "world models" OR "vision-language-action"',
            'GENERATIVE': '"diffusion model" OR "diffusion models" OR "flow matching" OR "autoregressive generation" OR "video generation"',
        }
        window = '[2025-10-26T16:00:00Z TO 2025-10-27T15:59:59.999Z]'
        for name, terms in themes.items():
            for field in ('registered', 'created'):
                query = f'{field}:{window} AND (titles.title:({terms}) OR descriptions.description:({terms}))'
                url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'client-id': 'arxiv.content', 'query': query, 'page[size]': 100})
                raw = fetch(f'REPAIR_DC_V2_{name}_{field.upper()}_20261029', url)
                if raw:
                    obj = json.loads(raw)
                    print('total', obj.get('meta', {}).get('total'), 'items', len(obj.get('data', [])), 'next', obj.get('links', {}).get('next'), flush=True)
