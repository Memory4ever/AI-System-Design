"""Bounded original-source recovery for Feb 21; no report mutations."""
import concurrent.futures
import json
import pathlib
import urllib.request
from datetime import datetime, timezone

BASE = pathlib.Path(__file__).parent
TASKS = [
    ('openai', 'https://openai.com/news/rss.xml', None, {}),
    ('anthropic', 'https://www.anthropic.com/research', None, {}),
    ('deepmind', 'https://deepmind.google/blog/rss.xml', None, {}),
    ('google_pubs', 'https://research.google/pubs/?year=2026', None, {}),
    ('qwen', 'https://qwen.ai/blog', None, {}),
    ('deepseek_news', 'https://api-docs.deepseek.com/news', None, {}),
    ('hunyuan_en', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'pageNum': 1, 'pageSize': 100, 'renderType': 0}, {'accept-language': 'en-US'}),
    ('hunyuan_zh', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'pageNum': 1, 'pageSize': 100, 'renderType': 0}, {'accept-language': 'zh-CN'}),
    ('seed_papers', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&order_desc=false&page_token=0&count=20', None, {}),
    ('seed_blogs', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&order_desc=false&page_token=0&count=20', None, {}),
    ('qwen_blogs', 'https://qwen.ai/blog', None, {}),
    ('minimax', 'https://www.minimax.io/blog', None, {}),
    ('arxiv_cl', 'https://arxiv.org/list/cs.CL/2602?skip=0&show=25', None, {}),
    ('arxiv_agent', 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=agent&terms-0-field=all&classification-computer_science_archives=all&classification-include_cross_list=include&date-filter_by=date_range&date-from_date=2026-02-21&date-to_date=2026-02-21&date-date_type=announced_date_first&abstracts=show&size=50&order=-announced_date_first', None, {}),
    ('arxiv_model', 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=language+model&terms-0-field=all&classification-computer_science_archives=all&classification-include_cross_list=include&date-filter_by=date_range&date-from_date=2026-02-21&date-to_date=2026-02-21&date-date_type=announced_date_first&abstracts=show&size=50&order=-announced_date_first', None, {}),
    ('reliability_v1', 'https://arxiv.org/abs/2602.16666v1', None, {}),
    ('phonetic_repo', 'https://api.github.com/repos/juice500ml/phonetic-arithmetic', None, {}),
]

def fetch(task):
    name, url, payload, headers = task
    record = {'name': name, 'url': url, 'payload': payload, 'headers': headers, 'checked_at': datetime.now(timezone.utc).isoformat()}
    request = urllib.request.Request(url, data=json.dumps(payload).encode() if payload is not None else None, headers={'User-Agent': 'Mozilla/5.0', 'Content-Type': 'application/json', **headers})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read()
            (BASE / ('supplement-native-' + name + '-20261008.txt')).write_bytes(raw)
            record.update(status=response.status, final_url=response.url, bytes=len(raw))
    except Exception as error:
        record['error'] = str(error)
    return record

if __name__ == '__main__':
    import sys
    if '--date-recovery' in sys.argv:
        prefix = 'https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term='
        suffix = '&terms-0-field=all&classification-computer_science_archives=all&classification-include_cross_list=include&date-filter_by=date_range&date-from_date=2026-02-21&date-to_date=2026-02-22&date-date_type=announced_date_first&abstracts=show&size=50&order=-announced_date_first'
        TASKS = [(name, prefix + term + suffix, None, {}) for name, term in [('arxiv_agent_recovery', 'agent'), ('arxiv_model_recovery', 'language+model'), ('arxiv_system_recovery', 'GPU'), ('arxiv_multimodal_recovery', 'multimodal')]]
    elif '--dynamic-recovery' in sys.argv:
        TASKS = [('qwen_home_js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_home-index.js', None, {}), ('hunyuan_zh_recovery', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'pageNum': 1, 'pageSize': 100, 'renderType': 0}, {'lang': 'zh', 'accept-language': 'zh-CN,zh;q=0.9'})]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(fetch, TASKS))
    manifest = 'supplement-native-date-recovery-20261008.json' if '--date-recovery' in sys.argv else 'supplement-native-dynamic-recovery-20261008.json' if '--dynamic-recovery' in sys.argv else 'supplement-native-20261008.json'
    (BASE / manifest).write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(results, ensure_ascii=False, indent=2))
