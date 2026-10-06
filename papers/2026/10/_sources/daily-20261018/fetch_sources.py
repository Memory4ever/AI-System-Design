"""Bounded source snapshots for the 2026-10-17 Beijing window; not admission."""
import concurrent.futures
import datetime
import html
import json
import pathlib
import re
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent
SOURCES = {
    'openai_index': 'https://openai.com/research/index/',
    'openai_rss': 'https://openai.com/news/rss.xml',
    'anthropic': 'https://www.anthropic.com/research',
    'deepmind_blog': 'https://deepmind.google/blog/',
    'google_blog': 'https://research.google/blog/',
    'google_pubs': 'https://research.google/pubs/',
    'meta': 'https://ai.meta.com/research/',
    'meta_blog': 'https://ai.meta.com/blog/',
    'qwen': 'https://qwen.ai/blog',
    'qwen_legacy': 'https://qwenlm.github.io/',
    'deepseek': 'https://www.deepseek.com/',
    'deepseek_updates': 'https://api-docs.deepseek.com/updates',
    'moonshot': 'https://platform.kimi.com/blog',
    'moonshot_github': 'https://github.com/MoonshotAI',
    'hunyuan': 'https://hunyuan.tencent.com/research',
    'zai': 'https://www.zhipuai.cn/zh/research',
    'seed_research': 'https://seed.bytedance.com/en/research',
    'seed_blog': 'https://seed.bytedance.com/en/blog',
    'seed_papers': 'https://seed.bytedance.com/en/public_papers',
    'ernie': 'https://ernie.baidu.com/blog/zh/',
    'mimo': 'https://mimo.xiaomi.com/',
    'minimax': 'https://www.minimax.io/blog',
    'minimax_tech': 'https://agent.minimax.io/docs/techblog',
    'availability': 'https://info.arxiv.org/help/availability.html',
}

def fetch(pair):
    key, url = pair
    record = {'key': key, 'url': url, 'checked': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=18) as response:
            raw = response.read().decode('utf-8', errors='replace')
            record.update(status=response.status, resolved=response.url, bytes=len(raw.encode()))
        (ROOT / (key + '.raw.html')).write_text(raw)
        stripped = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', raw, flags=re.S | re.I)
        visible = html.unescape(re.sub(r'<[^>]+>', '\n', stripped))
        visible = '\n'.join(line.strip() for line in visible.splitlines() if line.strip())
        (ROOT / (key + '.visible.txt')).write_text(visible)
        record['links'] = re.findall(r'href=[\"\x27]([^\"\x27]+)', raw)
    except Exception as error:
        record['error'] = str(error)
    return record

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fetch, SOURCES.items()))
    (ROOT / 'fetch_results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2))
    print(json.dumps([{k: v for k, v in row.items() if k != 'links'} for row in results], ensure_ascii=False, indent=2))
