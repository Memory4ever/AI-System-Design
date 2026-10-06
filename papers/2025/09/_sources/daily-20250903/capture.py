"""Capture untouched official HTTP responses and actual request metadata for this day."""
import concurrent.futures, datetime, hashlib, json, pathlib, urllib.request, urllib.parse, sys

BASE = pathlib.Path(__file__).parent
URLS = {
    'deepseek-home': 'https://www.deepseek.com/',
    'google-pubs': 'https://research.google/pubs/',
    'deepmind-research': 'https://deepmind.google/research/',
    'core-02163': 'https://arxiv.org/html/2509.02163v1',
    'core-10509': 'https://arxiv.org/html/2509.10509v1',
    'mimo-home': 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js',
    'mimo-home-component': 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js',
    'mimo-runtime': 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/styles.928fc8b8.js',
    'meta-results6': 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=6',
    'mimo-index': 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js',
    'mimo-route': 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js',
    'meta-results5': 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5',
    'meta-darling': 'https://ai.meta.com/research/publications/jointly-reinforcing-diversity-and-quality-in-language-model-generations/',
    'meta-blog2': 'https://ai.meta.com/blog/?page=2',
    'meta-blog3': 'https://ai.meta.com/blog/?page=3',
    'core-app-pdf': 'https://arxiv.org/pdf/2509.02444v1',
    'core-02208': 'https://arxiv.org/html/2509.02208v1',
    'qwen-config': 'https://qwen.ai/api/page_config?code=research.research-list',
    'hunyuan-api': 'https://api.hunyuan.tencent.com/api/blog/publicList',
    'meta-publication': 'https://ai.meta.com/research/publications/',
    'meta-blog': 'https://ai.meta.com/blog/',
    'google-month': 'https://research.google/blog/2025/09/',
    'google-month-2': 'https://research.google/blog/2025/09/?page=2',
    'google-aug': 'https://research.google/blog/2025/08/',
    'deepmind-page5': 'https://deepmind.google/blog/page/5/',
    'ernie-page2': 'https://ernie.baidu.com/blog/zh/page/2/',
    'zai-page2': 'https://www.zhipuai.cn/zh/research?page=2',
    'zai-releases': 'https://docs.z.ai/release-notes/new-released',
    'seed-blog2025': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true',
    'seed-paper20': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=20&count=20&order_desc=true',
    'seed-paper40': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=40&count=20&order_desc=true',
    'seed-paper60': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=60&count=20&order_desc=true',
    'seed-paper80': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=80&count=20&order_desc=true',
    'minimax-en2': 'https://www.minimax.io/blog?page=2',
    'openai-helpful': 'https://openai.com/index/building-more-helpful-chatgpt-experiences-for-everyone/',
    'openai-statsig': 'https://openai.com/index/vijaye-raji-to-become-cto-of-applications-with-acquisition-of-statsig/',
    'openai-rss': 'https://openai.com/news/rss.xml',
    'anthropic': 'https://www.anthropic.com/research',
    'google-september': 'https://research.google/blog/?year=2025&month=9',
    'deepmind-history': 'https://deepmind.google/discover/blog/?page=5',
    'meta': 'https://ai.meta.com/research/',
    'qwen': 'https://qwen.ai/research',
    'deepseek': 'https://api-docs.deepseek.com/updates',
    'moonshot': 'https://platform.kimi.com/blog',
    'hunyuan': 'https://hunyuan.tencent.com/research',
    'zai': 'https://www.zhipuai.cn/zh/research',
    'seed': 'https://seed.bytedance.com/en/research',
    'seed-paper': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true',
    'ernie': 'https://ernie.baidu.com/blog/zh/',
    'mimo': 'https://mimo.xiaomi.com/',
    'minimax-en': 'https://www.minimax.io/blog',
    'minimax-cn': 'https://www.minimaxi.com/blog',
    'minimax-agent': 'https://agent.minimax.io/docs/techblog',
}
THEMES = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts") AND (all:architecture OR all:attention OR all:optimizer OR all:training)',
    'systems': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel)',
    'multimodal': '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action")',
    'agents': '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak)',
}
SELECTED = '01684 01716 01728 01750 01840 01842 01920 01944 01959 02046 02075 02093 02097 02100 02123 02129 02133 02208 02333 02350 02408 02444 02449 02464 02479 02480 02492 02499 02512 02521 02522 02534 02560 02563 04499 04500 01909 04502 02225 02330 02360 02372 02377 02401 02655 02515 02547 02558'.split()
for paper in '02449 02444 01728 01840 02408 02522 01909 02372 02464 02563 02655 04499'.split():
    URLS['core-'+paper] = 'https://arxiv.org/html/2509.'+paper+'v1'
URLS['exact-v1'] = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list': ','.join('2509.'+x+'v1' for x in SELECTED), 'max_results': len(SELECTED)})
URLS['exact-tail-v1'] = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list': ','.join('2509.'+x+'v1' for x in '02040 02292 02163 02324 02447 10509'.split()), 'max_results': 6})
for name, query in THEMES.items():
    params = {'search_query': query + ' AND submittedDate:[202509011800 TO 202509021800]', 'start': 0, 'max_results': 100, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'}
    URLS['arxiv-' + name] = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode(params)

def capture(item):
    name, url = item
    checked = datetime.datetime.now(datetime.timezone.utc).isoformat()
    receipt = {'url': url, 'checked': checked, 'purpose': 'New independent 2025-09-03 capture; current response is not a frozen historical snapshot'}
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        data = None
        if name == 'hunyuan-api':
            data = json.dumps({'pageNum': 1, 'pageSize': 100, 'renderType': 0}).encode()
            headers['Content-Type'] = 'application/json'
            receipt.update(method='POST', body=json.loads(data))
        request = urllib.request.Request(url, headers=headers, data=data)
        with urllib.request.urlopen(request, timeout=35) as response:
            body = response.read()
            receipt.update(status=response.status, final_url=response.url, bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
            (BASE / (name + '.raw')).write_bytes(body)
    except Exception as error:
        receipt.update(error=str(error))
    (BASE / (name + '.request.json')).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n')
    return name, receipt.get('status'), receipt.get('bytes'), receipt.get('error')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        URLS = {k: v for k, v in URLS.items() if k in sys.argv[1:]}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for result in pool.map(capture, URLS.items()):
            print(result, flush=True)
