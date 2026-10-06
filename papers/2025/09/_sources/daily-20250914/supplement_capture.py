"""Capture bounded Daily discovery; submission timestamps are not publication evidence."""
import datetime
import hashlib
import json
import re
from pathlib import Path
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent

def capture(name, url, payload=None, headers=None):
    record = {'url': url, 'time': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'timeout_s': 25, 'byte_cap': 12000000, 'method': 'POST' if payload else 'GET'}
    supplied = {'User-Agent': 'Mozilla/5.0', **(headers or {})}
    data = json.dumps(payload).encode() if payload else None
    if data:
        supplied['Content-Type'] = 'application/json'
        record['payload'] = payload
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=supplied), timeout=25) as response:
            body = response.read(12000001)
            record['status'] = response.status
            record['final_url'] = response.url
    except urllib.error.HTTPError as error:
        body = error.read(12000001)
        record['status'] = error.code
    except Exception as error:
        body = str(error).encode()
        record['status'] = None
        record['error'] = str(error)
    assert len(body) <= 12000000, 'Response exceeded byte cap'
    record.update(bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
    stem = BASE / ('SUP_' + name + '_20261012')
    stem.with_name(stem.name + '.raw').write_bytes(body)
    stem.with_name(stem.name + '.request.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(name, record['status'], len(body), flush=True)
    return body

def arxiv_queries():
    groups = {
        'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model" OR all:"long context")',
        'systems': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:GPU OR all:"language model" OR all:transformer OR all:inference OR all:"model training")',
        'multimodal': '(cat:cs.CV OR cat:cs.RO) AND (all:"vision language" OR all:"world model" OR all:"foundation model" OR all:diffusion OR all:VLA OR all:multimodal)',
        'agents': '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:agent OR all:"retrieval augmented" OR all:"tool use")',
    }
    for name, theme in groups.items():
        query = theme + ' AND submittedDate:[202509121600 TO 202509131600]'
        params = urllib.parse.urlencode(dict(search_query=query, start=0, max_results=200, sortBy='submittedDate', sortOrder='ascending'))
        capture('ARXIV_' + name, 'https://export.arxiv.org/api/query?' + params)
        time.sleep(3)

def sources():
    urls = [
        ('OPENAI', 'https://openai.com/news/rss.xml'),
        ('ANTHROPIC', 'https://www.anthropic.com/research'),
        ('GOOGLE1', 'https://research.google/blog/2025/09/'),
        ('GOOGLE2', 'https://research.google/blog/2025/09/?page=2'),
        ('DEEPMIND5', 'https://deepmind.google/blog/page/5/'),
        ('DEEPMIND6', 'https://deepmind.google/blog/page/6/'),
        ('META5', 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5'),
        ('META6', 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=6'),
        ('METABLOG2', 'https://ai.meta.com/blog/?page=2'),
        ('METABLOG3', 'https://ai.meta.com/blog/?page=3'),
        ('QWEN', 'https://qwen.ai/api/page_config?code=research.research-list'),
        ('DEEPSEEK', 'https://www.deepseek.com/'),
        ('DEEPSEEK_UPDATES', 'https://api-docs.deepseek.com/updates'),
        ('MOONSHOT', 'https://platform.kimi.com/blog'),
        ('HUNYUAN', 'https://hunyuan.tencent.com/research'),
        ('ZAI', 'https://www.zhipuai.cn/zh/research'),
        ('ZAI2', 'https://www.zhipuai.cn/zh/research?page=2'),
        ('ZAI_RELEASE', 'https://docs.z.ai/release-notes/new-released'),
        ('SEED', 'https://seed.bytedance.com/en/research'),
        ('ERNIE1', 'https://ernie.baidu.com/blog/zh/'),
        ('ERNIE2', 'https://ernie.baidu.com/blog/zh/page/2/'),
        ('MIMO', 'https://mimo.xiaomi.com/'),
        ('MINIMAX_EN', 'https://www.minimax.io/blog'),
        ('MINIMAX_CN', 'https://www.minimaxi.com/blog'),
        ('MINIMAX_AGENT', 'https://agent.minimax.io/docs/techblog'),
    ]
    for name, url in urls:
        capture(name, url)
    for locale in ['en', 'zh']:
        capture('HUNYUAN_' + locale, 'https://api.hunyuan.tencent.com/api/blog/publicList',
                {'pageNum': 1, 'pageSize': 1000, 'renderType': 0}, {'Locale': locale})
    for kind in [1, 2]:
        capture('SEED_' + str(kind) + '_0', 'https://seed.bytedance.com/api/get_article_list_v2?' + urllib.parse.urlencode(
            dict(article_type=kind, publish_year=2025, page_token=0, count=20, order_desc='true')))

def papers():
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    old = {}
    for entry in ET.parse(BASE / 'arxiv-api.raw').getroot().findall('a:entry', ns):
        identity = entry.find('a:id', ns).text.rsplit('/', 1)[-1]
        old[re.sub(r'v[0-9]+$', '', identity)] = identity
    current = {}
    for path in sorted(BASE.glob('SUP_ARXIV_*_20261012.raw')):
        for entry in ET.parse(path).getroot().findall('a:entry', ns):
            identity = entry.find('a:id', ns).text.rsplit('/', 1)[-1]
            current[re.sub(r'v[0-9]+$', '', identity)] = identity
    new = sorted(set(current) - set(old))
    capture('EXACT_0', 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(
        dict(id_list=','.join(identity + 'v1' for identity in new), max_results=100)))
    time.sleep(3)
    for identity in new:
        capture('CURRENT_' + identity, 'https://arxiv.org/abs/' + identity)
    for identity in sorted(set(current) & set(old)):
        if current[identity] != old[identity]:
            capture('OVERLAP_CURRENT_' + identity, 'https://arxiv.org/abs/' + identity)

def dates():
    for category in ['cs.CL', 'cs.LG']:
        capture('PUBLIC_' + category, 'https://arxiv.org/list/' + category + '/2025-09-13?show=2000')

def core():
    for identity in ['2509.10397', '2509.10401', '2509.10408', '2509.10417',
                     '2509.10426', '2509.10436', '2509.12267', '2509.10416',
                     '2509.10694', '2509.10423']:
        capture('NCORE_' + identity, 'https://arxiv.org/html/' + identity + 'v1')

def dynamic():
    for locale in ['en', 'zh']:
        capture('HUNYUAN_LOCALE_' + locale, 'https://api.hunyuan.tencent.com/api/blog/publicList',
                {'pageNum': 1, 'pageSize': 1000, 'renderType': 0}, {'Locale': 'US' if locale == 'en' else 'CN'})
    for token in [20, 40, 60, 80]:
        capture('SEED_1_' + str(token), 'https://seed.bytedance.com/api/get_article_list_v2?' + urllib.parse.urlencode(
            dict(article_type=1, publish_year=2025, page_token=token, count=20, order_desc='true')))

if __name__ == '__main__':
    {'arxiv': arxiv_queries, 'sources': sources, 'papers': papers, 'dates': dates,
     'core': core, 'dynamic': dynamic}[sys.argv[1]]()
