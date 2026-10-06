"""Bounded Oct02 supplement capture; all originals are exclusive-create."""
import datetime as dt
import hashlib
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = Path(__file__).parent
OUT = BASE / 'supplement-20261007'
OUT.mkdir(exist_ok=True)

class Visible(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hidden = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag in ('p', 'li', 'h1', 'h2', 'h3', 'tr', 'div'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)

    def handle_data(self, value):
        if not self.hidden:
            self.parts.append(value)

def fetch(name, url, body=None, extra=None):
    paths = [OUT / (name + suffix) for suffix in ('.raw', '.request.json', '.txt')]
    if any(p.exists() for p in paths):
        raise FileExistsError(name)
    headers = {'User-Agent': 'AI-System-Design bounded historical research'}
    headers.update(extra or {})
    payload = None
    if body is not None:
        payload = json.dumps(body).encode()
        headers['Content-Type'] = 'application/json'
    receipt = {'url': url, 'started': dt.datetime.now(dt.timezone.utc).isoformat(),
               'request_headers': headers, 'body': body}
    raw = b''
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=payload, headers=headers), timeout=22) as response:
            raw = response.read()
            receipt.update(status=response.status, final_url=response.url, headers=dict(response.headers))
    except urllib.error.HTTPError as error:
        raw = error.read()
        receipt.update(status=error.code, final_url=error.url, error=str(error), headers=dict(error.headers))
    except Exception as error:
        receipt['error'] = str(error)
    receipt.update(finished=dt.datetime.now(dt.timezone.utc).isoformat(), bytes=len(raw),
                   sha256=hashlib.sha256(raw).hexdigest())
    with paths[0].open('xb') as handle:
        handle.write(raw)
    with paths[1].open('x') as handle:
        json.dump(receipt, handle, ensure_ascii=False, indent=2)
        handle.write('\n')
    parser = Visible()
    if raw.startswith(b'%PDF'):
        parser.parts.append('Binary PDF original retained in .raw; no HTML text extraction.')
    else:
        parser.feed(raw.decode('utf-8', 'replace'))
    with paths[2].open('x') as handle:
        handle.write('\n'.join(s.strip() for s in ''.join(parser.parts).splitlines() if s.strip()) + '\n')
    print(json.dumps({k: receipt[k] for k in ('url', 'started', 'finished', 'status', 'bytes', 'error') if k in receipt}), flush=True)

def initial():
    report = BASE.parent.parent / '02' / 'README.md'
    with (BASE / 'baseline-before-supplement-20261007.md').open('xb') as handle:
        handle.write(report.read_bytes())
    entries = [
        ('openai-research', 'https://openai.com/research/'),
        ('openai-rss', 'https://openai.com/news/rss.xml'),
        ('anthropic-research', 'https://www.anthropic.com/research'),
        ('google-deepmind', 'https://deepmind.google/research/'),
        ('deepmind-publications', 'https://deepmind.google/research/publications/'),
        ('google-pubs', 'https://research.google/pubs/'),
        ('google-october', 'https://research.google/blog/2025/10/'),
        ('google-october-page2', 'https://research.google/blog/2025/10/?page=2'),
        ('meta-research', 'https://ai.meta.com/research/'),
        ('qwen', 'https://qwenlm.github.io/'),
        ('qwen-research', 'https://qwen.ai/research'),
        ('deepseek', 'https://www.deepseek.com/'),
        ('deepseek-news', 'https://www.deepseek.com/news/'),
        ('moonshot-blog', 'https://platform.kimi.com/blog'),
        ('hunyuan-research', 'https://hunyuan.tencent.com/research'),
        ('zai-research', 'https://www.zhipuai.cn/zh/research'),
        ('zai-page2', 'https://www.zhipuai.cn/zh/research?page=2'),
        ('zai-release', 'https://docs.z.ai/release-notes/new-released'),
        ('seed-research', 'https://seed.bytedance.com/en/research'),
        ('seed-papers', 'https://seed.bytedance.com/en/public_papers'),
        ('ernie', 'https://ernie.baidu.com/blog/zh/'),
        ('ernie-page2', 'https://ernie.baidu.com/blog/zh/page/2/'),
        ('mimo', 'https://mimo.xiaomi.com/'),
        ('minimax', 'https://www.minimax.io/blog'),
        ('minimax-cn', 'https://www.minimaxi.com/blog'),
        ('minimax-agent', 'https://agent.minimax.io/docs/techblog'),
    ]
    for name, url in entries:
        fetch(name, url)
    fetch('hunyuan-list', 'https://api.hunyuan.tencent.com/api/blog/publicList',
          {'pageNum': 1, 'pageSize': 100, 'renderType': 0})
    for kind in (1, 2):
        fetch('seed-type' + str(kind) + '-0', 'https://seed.bytedance.com/api/get_article_list_v2?' +
              urllib.parse.urlencode({'article_type': kind, 'publish_year': 2025, 'count': 20,
                                      'order_desc': 'false', 'mode': 1, 'page_token': 0}), extra={'x-tt-locale': 'US'})
    terms = ['language model', 'transformer', 'mixture of experts', 'reinforcement learning language',
             'GPU inference', 'agent memory', 'multimodal', 'vision language action']
    for i, term in enumerate(terms):
        params = {'advanced': '', 'terms-0-operator': 'AND', 'terms-0-term': term,
                  'terms-0-field': 'all', 'classification-include_cross_list': 'include',
                  'date-filter_by': 'date_range', 'date-from_date': '2025-10',
                  'date-to_date': '2025-11', 'date-date_type': 'announced_date_first',
                  'abstracts': 'show', 'size': '25', 'order': 'announced_date_first', 'start': '0'}
        fetch('arxiv-advanced-' + str(i), 'https://arxiv.org/search/advanced?' + urllib.parse.urlencode(params))
    for category in ('cs.CL', 'cs.DC'):
        fetch('arxiv-list-' + category, 'https://arxiv.org/list/' + category + '/2510?skip=0&show=25')

if __name__ == '__main__':
    if len(sys.argv) == 1:
        initial()
    else:
        fetch(sys.argv[1], sys.argv[2])
