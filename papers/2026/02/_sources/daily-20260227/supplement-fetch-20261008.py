import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.skip = max(0, self.skip - 1)
    def handle_data(self, data):
        if not self.skip and data.strip():
            self.parts.append(data.strip())

ROOT = pathlib.Path(__file__).resolve().parent
JOBS = {
    'openai': 'https://openai.com/news/rss.xml',
    'anthropic': 'https://www.anthropic.com/research',
    'google': 'https://research.google/blog/2026/02/',
    'deepmind': 'https://deepmind.google/research/publications/',
    'meta': 'https://ai.meta.com/research/',
    'qwen': 'https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US',
    'deepseek': 'https://api-docs.deepseek.com/updates/',
    'moonshot': 'https://platform.kimi.com/blog',
    'hunyuan': 'https://api.hunyuan.tencent.com/api/blog/publicList',
    'zai': 'https://www.zhipuai.cn/zh/research',
    'seed60': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&page_token=60&order_desc=true&publish_year=2026',
    'seed80': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&page_token=80&order_desc=true&publish_year=2026',
    'seedblog': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&count=20&page_token=0&order_desc=true&publish_year=2026',
    'ernie': 'https://ernie.baidu.com/blog/zh/',
    'mimo': 'https://mimo.xiaomi.com/',
    'minimax': 'https://www.minimax.io/blog',
    'minimaxcn': 'https://www.minimaxi.com/blog',
}
for name, term in {
    'arxiv_model': 'language model OR foundation model OR Transformer OR mixture of experts',
    'arxiv_system': 'GPU OR inference OR distributed training OR kernel OR compiler',
    'arxiv_agent': 'agent OR reasoning OR retrieval OR memory',
    'arxiv_multimodal': 'multimodal OR world model OR vision language action OR diffusion',
}.items():
    params = {'advanced':'', 'terms-0-operator':'AND', 'terms-0-term':term, 'terms-0-field':'all',
              'classification-computer_science_archives':'all', 'classification-include_cross_list':'include',
              'date-filter_by':'date_range','date-from_date':'2026-02-26','date-to_date':'2026-02-26',
              'date-date_type':'announced_date_first','abstracts':'show','size':'200','order':'-announced_date_first'}
    JOBS[name] = 'https://arxiv.org/search/advanced?' + urllib.parse.urlencode(params)

def fetch(pair):
    name, url = pair
    row = {'name':name,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        data = json.dumps({'pageSize':1000,'pageNum':1}).encode() if name == 'hunyuan' else None
        req = urllib.request.Request(url, data=data, headers={'User-Agent':'Mozilla/5.0','Accept-Encoding':'identity',
                                      **({'Content-Type':'application/json'} if data else {})})
        with urllib.request.urlopen(req,timeout=40) as res:
            raw = res.read().decode('utf-8','replace')
            row.update(status=res.status,resolved=res.url,bytes=len(raw))
        (ROOT / f'supplement-{name}-20261008.raw').write_text(raw)
        parser = TextParser()
        parser.feed(raw)
        text = '\n'.join(parser.parts)
        (ROOT / f'supplement-{name}-20261008.txt').write_text(text)
        row['text_length'] = len(text)
    except Exception as exc:
        row['error'] = str(exc)
    return row

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        JOBS = {}
        for name, terms in {
            'discover_model': '(language OR LLM OR transformer OR MoE OR inference OR training OR reinforcement OR distillation)',
            'discover_system': '(GPU OR kernel OR accelerator OR distributed OR communication OR serving OR quantization OR compiler)',
            'discover_multimodal': '(multimodal OR diffusion OR flow OR "world model" OR robotics OR "vision-language" OR VLA OR agent OR retrieval)',
        }.items():
            query = 'doi:10.48550/arxiv.2602* AND registered:[2026-02-25T16:00:00Z TO 2026-02-26T15:59:59Z] AND ' + terms
            JOBS[name] = 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'query':query,'page[size]':1000})
        query = '(cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.DC OR cat:cs.CV OR cat:cs.RO OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.IR OR cat:cs.MA) AND submittedDate:[202602250000 TO 202602262359] AND (all:LLM OR all:"language model" OR all:"foundation model" OR all:Transformer OR all:GPU OR all:agent OR all:diffusion OR all:"world model")'
        JOBS['api_narrow'] = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':query,'start':0,'max_results':200,'sortBy':'submittedDate','sortOrder':'ascending'})
        if sys.argv[1] == 'tail':
            JOBS = {'api_narrow200': JOBS['api_narrow'].replace('start=0&', 'start=200&'),
                    'api_narrow400': JOBS['api_narrow'].replace('start=0&', 'start=400&')}
        elif sys.argv[1] == 'abstracts':
            ids = ['21456','21535','21552','21553','21556','21581','21750','21765','21829','21849','21858','21939','21967','22041','22100','21302','21827']
            JOBS = {'abs_' + short: f'https://arxiv.org/abs/2602.{short}v1' for short in ids}
            JOBS['ioagent_core'] = 'https://arxiv.org/html/2602.22017v1'
        elif sys.argv[1] == 'official':
            JOBS = {
                'opus_deprecation': 'https://www.anthropic.com/research/deprecation-updates-opus-3',
                'meta3': 'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=3&sort_by=most_recent',
                'seedblog20': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&count=20&page_token=20&order_desc=true&publish_year=2026',
                'hunyuan_research': 'https://hunyuan.tencent.com/research',
                'deepseek_research': 'https://www.deepseek.com/',
                'mimo_blog': 'https://mimo.xiaomi.com/blog',
                'minimax_techblog': 'https://agent.minimax.io/docs/techblog',
            }
        elif sys.argv[1] == 'dates':
            ids = ['21456','21535','21552','21553','21556','21581','21750','21765','21829','21849','21858','21939','21967','22017']
            JOBS = {'date_' + short: 'https://export.arxiv.org/oai2?' + urllib.parse.urlencode({
                'verb':'GetRecord','identifier':f'oai:arXiv.org:2602.{short}','metadataPrefix':'arXivRaw'}) for short in ids}
        elif sys.argv[1] == 'clarify':
            JOBS = {'core_21552': 'https://arxiv.org/html/2602.21552v1',
                    'core_21858': 'https://arxiv.org/html/2602.21858v1'}
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        rows = list(pool.map(fetch, JOBS.items()))
    filename = f'supplement-fetch-{sys.argv[1]}-20261008.json' if len(sys.argv) > 1 else 'supplement-fetch-20261008.json'
    (ROOT / filename).write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(rows,ensure_ascii=False,indent=2))
