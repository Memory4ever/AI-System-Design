"""Bounded source retrieval; generated responses retained by the caller."""
import concurrent.futures
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

GROUPS = {
    "language-training": 'titles.title:("language model" OR LLM OR transformer OR MoE OR pretraining OR "reinforcement learning" OR distillation OR tokenizer)',
    "multimodal-agent": 'titles.title:("foundation model" OR multimodal OR "world model" OR "vision-language" OR VLA OR diffusion OR agent OR reasoning OR memory OR RAG)',
    "systems": 'titles.title:(inference OR GPU OR kernel OR compiler OR quantization OR attention OR scheduling OR distributed OR "tensor parallel" OR "KV cache" OR speculative)',
}

def fetch(group):
    name, terms = group
    query = 'prefix:10.48550 AND subjects.subject:"Computer and information sciences" AND registered:[2026-01-22T00:00:00Z TO 2026-01-23T00:59:59Z] AND ' + terms
    url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'query': query, 'page[size]': 100, 'fields[dois]': 'doi,titles,subjects,dates,descriptions,url,created,registered'})
    try:
        with urllib.request.urlopen(url, timeout=35) as response:
            payload = json.load(response)
        return {'group': name, 'url': url, 'payload': payload}
    except Exception as exc:
        return {'group': name, 'url': url, 'error': str(exc)}

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(fetch, GROUPS.items()))
    Path(__file__).with_name('datacite-scoped-results.json').write_text(json.dumps(results, ensure_ascii=False), encoding='utf-8')
    print(json.dumps([{'group': g['group'], 'url': g['url'], 'total': g.get('payload', {}).get('meta', {}).get('total'), 'error': g.get('error'), 'items': [{'id': v['id'], 'title': v['attributes']['titles'][0]['title']} for v in g.get('payload', {}).get('data', [])]} for g in results], ensure_ascii=False))
