"""Bounded Sep03 discovery; captures are not proof of first-public dates."""
import argparse
import concurrent.futures
import datetime
import hashlib
import json
import importlib.util
import pathlib
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = pathlib.Path(__file__).parent
THEMES = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts") AND (all:architecture OR all:attention OR all:optimizer OR all:training)',
    'systems': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel)',
    'multimodal': '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action")',
    'agents': '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak)',
}

def capture(name, url, headers=None, body=None):
    receipt = {'url': url, 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'request_headers': headers or {}, 'method': 'POST' if body else 'GET'}
    if body:
        receipt['request_body'] = body.decode()
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0', 'Accept-Encoding': 'identity', **(headers or {})}, data=body)
    try:
        response = urllib.request.urlopen(req, timeout=30)
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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('names', nargs='*')
    args = parser.parse_args()
    names = args.names or list(THEMES)
    if names == ['sources']:
        spec = importlib.util.spec_from_file_location('old_capture', BASE / 'capture.py')
        old = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(old)
        keys = 'openai anthropic google-pubs google-month google-month2 deepmind-history meta-results5 meta-results6 meta-blog2 meta-blog3 qwen deepseek deepseek-updates moonshot hunyuan zai zai2 zai-release ernie ernie2 mimo minimax-en minimax-cn minimax-agent'.split()
        for key in keys:
            capture('SUP_' + key.upper().replace('-', '_') + '_20261011', old.URLS[key])
    elif names in [['exact'], ['current']]:
        ns = {'a': 'http://www.w3.org/2005/Atom'}
        ids = sorted({entry.findtext('a:id', namespaces=ns).split('/abs/')[1].split('v')[0] for path in BASE.glob('SUP_ARXIV_*_20261011.raw') for entry in ET.fromstring(path.read_bytes()).findall('a:entry', ns)})
        if names == ['current']:
            def current(identity):
                capture('SUP_CURRENT_' + identity + '_20261011', 'https://arxiv.org/abs/' + identity)
            with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
                list(pool.map(current, ids))
        else:
            scope = {'2509.01928', '2509.02481', '2509.02640', '2509.01878', '2509.01679', '2509.01736', '2509.01794', '2509.01886', '2509.02060', '2509.02661'}
            ids = [identity for identity in ids if identity not in scope]
            for start in range(0, len(ids), 25):
                selected = ids[start:start + 25]
                url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list': ','.join(identity + 'v1' for identity in selected), 'max_results': 25})
                capture('SUP_EXACT_' + str(start) + '_20261011', url)
    elif names == ['extras']:
        identities = '01928 02640 01878 01794 01886'.split()
        capture('SUP_EXACT_SCOPE_20261011', 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list': ','.join('2509.' + identity + 'v1' for identity in identities), 'max_results': 5}))
    elif names == ['core']:
        identities = '01909 02093 02072 01944 01920 01728 02163 02449 02401 02655 10511 04505 02550 02350 02547 02363 02123 02444 02659 02551'.split()
        for identity in identities:
            capture('SUP_CORE_2509.' + identity + 'v1_20261011', 'https://arxiv.org/html/2509.' + identity + 'v1')
    elif names == ['dynamic']:
        for language in ['en', 'zh']:
            capture('SUP_HUNYUAN_' + language + '_20261011', 'https://api.hunyuan.tencent.com/api/blog/publicList', {'Accept-Language': language, 'Content-Type': 'application/json'}, json.dumps({'pageNum': 1, 'pageSize': 1000, 'renderType': 0}).encode())
        for kind in [1, 2]:
            for token in ([0, 20, 40] if kind == 1 else [0]):
                capture('SUP_SEED_' + str(kind) + '_' + str(token) + '_20261011', 'https://seed.bytedance.com/api/get_article_list_v2?' + urllib.parse.urlencode({'article_type': kind, 'publish_year': 2025, 'count': 20, 'page_token': token, 'order_desc': 'true'}), {'x-language': 'en', 'x-country': 'US'})
        capture('SUP_ROBOBALLET_20261011', 'https://deepmind.google/research/publications/111579/')
        capture('SUP_OPENAI_RELEASES_20261011', 'https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes')
    elif names == ['date']:
        for category in ['cs.CL', 'cs.LG']:
            capture('SUP_PUBLIC_' + category + '_20261011', 'https://arxiv.org/list/' + category + '/2025-09-03?show=200')
    else:
      for name in names:
        query = THEMES[name] + ' AND submittedDate:[202509011800 TO 202509021800]'
        url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': query, 'start': 0, 'max_results': 200, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
        capture('SUP_ARXIV_' + name + '_20261011', url)
