"""Fetch original public responses for this single day; no report edits."""
import concurrent.futures
import json
import pathlib
import urllib.request

BASE = pathlib.Path(__file__).parent
TASKS = [
    ('openai_rss', 'https://openai.com/news/rss.xml', None),
    ('anthropic_research', 'https://www.anthropic.com/research', None),
    ('google_blog_2026', 'https://research.google/blog/?year=2026', None),
    ('google_pubs', 'https://research.google/pubs/?year=2026', None),
    ('deepmind_rss', 'https://deepmind.google/blog/rss.xml', None),
    ('qwen', 'https://qwen.ai/blog', None),
    ('hunyuan_list', 'https://hunyuan.tencent.com/api/blog/publicList', {'page': 1, 'pageSize': 100, 'tag': ''}),
    ('seed_papers0', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&order_desc=true&page_token=0&count=100&locale=en-US', None),
    ('seed_blogs0', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&order_desc=true&page_token=0&count=100&locale=en-US', None),
    ('glm_abs', 'https://arxiv.org/abs/2602.15763', None),
    ('glm_commits', 'https://api.github.com/repos/zai-org/GLM-5/commits?path=README.md&since=2026-02-20T00%3A00%3A00Z&until=2026-02-22T01%3A00%3A00Z&per_page=30', None),
    ('availability', 'https://info.arxiv.org/help/availability.html', None),
]

def fetch(task):
    name, url, payload = task[:3]
    headers={'User-Agent':'Mozilla/5.0', 'Content-Type':'application/json', 'accept-language':'en-US,en;q=0.9'}
    if len(task) > 3:
        headers.update(task[3])
    req = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None,
        headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            raw = response.read()
            (BASE / ('V3_NATIVE_' + name + '.txt')).write_bytes(raw)
            return {'name':name, 'url':url, 'payload':payload, 'status':response.status, 'bytes':len(raw)}
    except Exception as error:
        return {'name':name, 'url':url, 'payload':payload, 'error':str(error)}

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results=list(pool.map(fetch,TASKS))
    (BASE / 'V3_NATIVE_FETCH.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(results,ensure_ascii=False,indent=2))
