"""Bounded Daily discovery: original entrances plus window-specific themes."""
import concurrent.futures
import datetime
import html
import json
import pathlib
import re
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent / 'resume-check'
ROOT.mkdir(exist_ok=True)
ENTRANCES = [
    ('openai','https://openai.com/research/'),
    ('openai-rss','https://openai.com/news/rss.xml'),
    ('anthropic','https://www.anthropic.com/research'),
    ('deepmind','https://deepmind.google/research/'),
    ('deepmind-page5','https://deepmind.google/blog/page/5/'),
    ('google-pubs','https://research.google/pubs/'),
    ('google-september','https://research.google/blog/2025/09/'),
    ('meta','https://ai.meta.com/research/'),
    ('meta-page4','https://ai.meta.com/results/?content_types%5B0%5D=publication&page=4'),
    ('meta-page5','https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5'),
    ('qwen','https://qwenlm.github.io/'),
    ('qwen-config','https://qwen.ai/api/page_config?code=research.research-list'),
    ('deepseek','https://www.deepseek.com/'),
    ('deepseek-updates','https://api-docs.deepseek.com/updates/'),
    ('kimi','https://platform.kimi.com/blog'),
    ('hunyuan','https://hunyuan.tencent.com/research'),
    ('zai','https://www.zhipuai.cn/zh/research'),
    ('zai-page2','https://www.zhipuai.cn/zh/research?page=2'),
    ('seed','https://seed.bytedance.com/en/research'),
    ('seed-papers','https://seed.bytedance.com/en/public_papers'),
    ('seed-blog-api','https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true'),
    ('seed-paper-api','https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token=0&count=20&order_desc=true'),
    ('ernie','https://ernie.baidu.com/blog/zh/'),
    ('ernie-page2','https://ernie.baidu.com/blog/zh/page/2/'),
    ('mimo','https://mimo.xiaomi.com/'),
    ('minimax','https://www.minimax.io/blog'),
    ('minimax-page2','https://www.minimax.io/blog?page=2'),
    ('minimax-cn','https://www.minimaxi.com/blog'),
    ('minimax-agent','https://agent.minimax.io/docs/techblog'),
    ('minimax-index','https://agent.minimax.io/docs/llms.txt'),
]
THEMES = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")',
    'systems': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:"model inference" OR all:"GPU training" OR all:"KV cache" OR all:"attention kernel")',
    'agents': '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:"tool calling" OR all:"agent memory" OR all:"retrieval augmented")',
    'multimodal': '(cat:cs.CV OR cat:cs.RO) AND (all:"multimodal model" OR all:"vision language" OR all:"world model" OR all:"vision language action" OR all:"diffusion transformer")',
}
for name, theme in THEMES.items():
    query = '(' + theme + ') AND submittedDate:[202509230000 TO 202509250100]'
    ENTRANCES.append(('arxiv-'+name, 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':query,'start':0,'max_results':60,'sortBy':'submittedDate','sortOrder':'ascending'})))
ENTRANCES.append(('arxiv-day','https://arxiv.org/list/cs.CL/2025-09-25?show=2000'))

def fetch(item):
    name, url = item
    if (ROOT/(name+'.raw')).exists() or (ROOT/(name+'.txt')).exists():
        raise FileExistsError('Preserve source evidence; choose a fresh run directory before fetching again: '+name)
    record = {'name':name,'url':url,'method':'GET','fetched_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(request, timeout=25) as response:
            raw = response.read()
            record.update(status=response.status, final_url=response.url, bytes=len(raw))
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        record.update(status=exc.code, bytes=len(raw), error=str(exc))
    except Exception as exc:
        raw = b''
        record.update(status=None, bytes=0, error=repr(exc))
    (ROOT/(name+'.raw')).write_bytes(raw)
    source = raw.decode('utf-8','replace')
    text = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', source, flags=re.S|re.I)
    text = html.unescape(re.sub(r'<[^>]+>', '\n', text))
    text = re.sub(r'\n\s*\n+', '\n', text)
    (ROOT/(name+'.txt')).write_text(text)
    if name.startswith('arxiv-') and name != 'arxiv-day' and record.get('status') == 200:
        try:
            ns = {'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
            tree = ET.fromstring(raw)
            entries = []
            for entry in tree.findall('a:entry',ns):
                entries.append({key:' '.join((entry.findtext('a:'+key,'',ns)).split()) for key in ['id','title','summary','published','updated']})
            (ROOT/(name+'-entries.json')).write_text(json.dumps({'total':tree.findtext('o:totalResults','',ns),'query':url,'entries':entries},ensure_ascii=False,indent=2))
        except Exception as exc:
            record['parse_error'] = repr(exc)
    return record

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    records = list(pool.map(fetch, ENTRANCES))
(ROOT/'fetch-results.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
print(json.dumps([{k:r.get(k) for k in ['name','status','bytes','error']} for r in records],ensure_ascii=False))
