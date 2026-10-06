"""Finite Sep09 discovery captures; capture is not reading or public-date proof."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = Path(__file__).parent
SOURCES = {
    'OPENAI': 'https://openai.com/news/rss.xml',
    'ANTHROPIC': 'https://www.anthropic.com/research',
    'GOOGLE_PUBS': 'https://research.google/pubs/',
    'GOOGLE_MONTH': 'https://research.google/blog/2025/09/',
    'GOOGLE_MONTH2': 'https://research.google/blog/2025/09/?page=2',
    'DEEPMIND': 'https://deepmind.google/research/',
    'DEEPMIND5': 'https://deepmind.google/blog/page/5/',
    'DEEPMIND6': 'https://deepmind.google/blog/page/6/',
    'META': 'https://ai.meta.com/research/',
    'META_PUB5': 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5',
    'META_PUB6': 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=6',
    'META_BLOG2': 'https://ai.meta.com/blog/?page=2',
    'META_BLOG3': 'https://ai.meta.com/blog/?page=3',
    'QWEN': 'https://qwen.ai/api/page_config?code=research.research-list',
    'DEEPSEEK': 'https://www.deepseek.com/',
    'DEEPSEEK_UPDATES': 'https://api-docs.deepseek.com/updates',
    'MOONSHOT': 'https://platform.kimi.com/blog',
    'HUNYUAN': 'https://hunyuan.tencent.com/research',
    'ZAI': 'https://www.zhipuai.cn/zh/research',
    'ZAI2': 'https://www.zhipuai.cn/zh/research?page=2',
    'ZAI_RELEASE': 'https://docs.z.ai/release-notes/new-released',
    'SEED': 'https://seed.bytedance.com/en/public_papers',
    'ERNIE': 'https://ernie.baidu.com/blog/zh/',
    'ERNIE2': 'https://ernie.baidu.com/blog/zh/page/2/',
    'MIMO': 'https://mimo.xiaomi.com/',
    'MINIMAX_EN': 'https://www.minimax.io/blog',
    'MINIMAX_CN': 'https://www.minimaxi.com/blog',
    'MINIMAX_AGENT': 'https://agent.minimax.io/docs/techblog',
}
THEMES = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts") AND (all:architecture OR all:attention OR all:optimizer OR all:training)',
    'systems': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel)',
    'multimodal': '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action")',
    'agents': '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak)',
}

def capture(name, url, headers=None, body=None):
    receipt = {'url': url, 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'method': 'POST' if body else 'GET', 'request_headers': headers or {}}
    if body:
        receipt['request_body'] = body.decode()
    request = urllib.request.Request(url, data=body, headers={'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'identity', **(headers or {})})
    try:
        response = urllib.request.urlopen(request, timeout=35)
    except urllib.error.HTTPError as error:
        response = error
    except Exception as error:
        receipt['error'] = str(error)
        response = None
    if response is not None:
        raw = response.read()
        receipt.update(status=response.status, final_url=response.geturl(), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        (BASE / (name + '.raw')).write_bytes(raw)
    (BASE / (name + '.request.json')).write_text(json.dumps(receipt, indent=2) + '\n')
    print(name, receipt.get('status'), receipt.get('bytes'), receipt.get('error'), flush=True)

def identities():
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    discovered = {entry.findtext('a:id', namespaces=ns).split('/abs/')[1].split('v')[0] for path in BASE.glob('SUP_ARXIV_*_20261011.raw') for entry in ET.fromstring(path.read_bytes()).findall('a:entry', ns)}
    frozen = {row['id'] for row in json.loads((BASE / 'ABSTRACTS_PARSED.json').read_text())}
    return sorted(discovered - frozen)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['sources', 'themes', 'exact', 'current', 'dynamic', 'date', 'core'])
    mode = parser.parse_args().mode
    if mode == 'sources':
        for name, url in SOURCES.items():
            capture('SUP_' + name + '_20261011', url)
    elif mode == 'themes':
        for name, query in THEMES.items():
            params = {'search_query': query + ' AND submittedDate:[202509081600 TO 202509091600]', 'start': 0, 'max_results': 200, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'}
            capture('SUP_ARXIV_' + name + '_20261011', 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(params))
    elif mode == 'exact':
        ids = identities()
        for start in range(0, len(ids), 25):
            params = {'id_list': ','.join(x + 'v1' for x in ids[start:start + 25]), 'max_results': 25}
            capture('SUP_EXACT_' + str(start) + '_20261011', 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(params))
    elif mode == 'current':
        for identity in identities():
            capture('SUP_CURRENT_' + identity + '_20261011', 'https://arxiv.org/abs/' + identity)
    elif mode == 'dynamic':
        for locale in ['en', 'zh']:
            capture('SUP_HUNYUAN_' + locale + '_20261011', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'Accept-Language': locale, 'Content-Type': 'application/json'}, json.dumps({'pageNum': 1, 'pageSize': 1000, 'renderType': 0}).encode())
        for kind in [1, 2]:
            params = {'article_type': kind, 'publish_year': 2025, 'page_token': 0, 'count': 20, 'order_desc': 'true'}
            capture('SUP_SEED_' + str(kind) + '_0_20261011', 'https://seed.bytedance.com/api/get_article_list_v2?' + urllib.parse.urlencode(params), {'x-tt-locale': 'US'})
    elif mode == 'core':
        for identity in ['06830', '06870', '06902', '07367', '07430', '07558', '07595', '07596', '07642', '07727', '07759', '07794', '07846', '08031', '12235']:
            name = 'SUP_CORE_2509.' + identity + 'v1_20261011'
            capture(name, 'https://arxiv.org/html/2509.' + identity + 'v1')
            receipt = json.loads((BASE / (name + '.request.json')).read_text())
            if receipt.get('status') != 200:
                capture(name + '_PDF', 'https://arxiv.org/pdf/2509.' + identity + 'v1')
    else:
        for category in ['cs.CL', 'cs.LG']:
            capture('SUP_PUBLIC_' + category + '_20261011', 'https://arxiv.org/list/' + category + '/2025-09-09?show=200')
