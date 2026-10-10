"""Bounded Jan27 discovery; generated responses are not screening decisions."""
import concurrent.futures, datetime, gzip, html, json, pathlib, re, urllib.parse, urllib.request
base = pathlib.Path(__file__).resolve().parent
themes = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:MoE OR all:pretraining OR all:distillation OR all:attention)',
    'multi': '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"multimodal" OR all:"world model" OR all:"vision language action" OR all:"diffusion model")',
    'agent': '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:memory OR all:retrieval OR all:tool)',
    'system': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"language model" OR all:LLM OR all:transformer) AND (all:inference OR all:GPU OR all:kernel OR all:cache OR all:serving OR all:parallel)',
}
def retrieve(name, url):
    record = {'url': url, 'checked': datetime.datetime.now().astimezone().isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=40) as response:
            body = response.read()
            if body[:2] == b'\x1f\x8b': body = gzip.decompress(body)
            raw = body.decode('utf-8')
        record['raw'] = raw
        visible = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', raw, flags=re.S)
        visible = re.sub(r'</(?:p|h[1-6]|div|li|tr|section)>', '\n', visible)
        record['text'] = '\n'.join(' '.join(line.split()) for line in html.unescape(re.sub(r'<[^>]+>', ' ', visible)).splitlines() if line.strip())
    except Exception as exc: record['error'] = str(exc)
    (base / ('supplement-' + name + '-20261008.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(name, len(record.get('text', '')), record.get('error', 'OK'), flush=True)
tasks = []
for name, theme in themes.items():
    query = 'submittedDate:[202601260000 TO 202601272359] AND ' + theme
    tasks.append(('theme-' + name, 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': query, 'start': 0, 'max_results': 150, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'})))
tasks.extend([
    ('deepmind-decoded', 'https://deepmind.google/discover/blog/'),
    ('kimi-core', 'https://www.kimi.ai/blog/kimi-k2-5'),
    ('minimax-core', 'https://www.minimax.io/blog/minimax-m2-her'),
    ('seed-keel', 'https://seed.bytedance.com/en/publication/post-layernorm-is-back-stable-expressive-and-deep'),
    ('seed-vg', 'https://seed.bytedance.com/en/publication/visual-generation-unlocks-human-like-reasoning-through-multimodal-world-models'),
    ('arxiv-abs-19834', 'https://arxiv.org/abs/2601.19834v1'),
    ('arxiv-abs-19895', 'https://arxiv.org/abs/2601.19895v1'),
])
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    list(pool.map(lambda item: retrieve(*item), tasks))
