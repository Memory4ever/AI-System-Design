import argparse
import datetime as dt
import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parent


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.skip += 1
        elif tag in ('p', 'div', 'h1', 'h2', 'h3', 'li', 'tr', 'br', 'section'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style') and self.skip:
            self.skip -= 1
        elif tag in ('p', 'div', 'li', 'tr'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)


def fetch(name, url, method='GET', body=None, headers=None, timeout=20):
    raw = ROOT / (name + '.raw')
    if raw.exists():
        raise RuntimeError('preserve existing original: ' + name)
    started = dt.datetime.now(dt.timezone.utc).isoformat()
    cmd = ['curl', '-L', '--max-time', str(timeout), '--connect-timeout', '8',
           '-sS', '-A', 'Mozilla/5.0', '-D', str(ROOT / (name + '.headers.txt')),
           '-o', str(raw), '-w', '%{http_code}\n%{url_effective}', '-X', method]
    for key, value in (headers or {}).items():
        cmd += ['-H', key + ': ' + value]
    if body is not None:
        cmd += ['--data-raw', json.dumps(body)]
    cmd.append(url)
    result = subprocess.run(cmd, text=True, capture_output=True)
    receipt = {'requested_url': url, 'method': method, 'body': body,
               'headers': headers or {}, 'started_at': started,
               'finished_at': dt.datetime.now(dt.timezone.utc).isoformat(),
               'exit_code': result.returncode, 'curl_output': result.stdout,
               'error': result.stderr}
    (ROOT / (name + '.receipt.json')).write_text(json.dumps(receipt, indent=2))
    if raw.exists():
        original = raw.read_text(errors='replace')
        parser = Text()
        try:
            parser.feed(original)
        except (NotImplementedError, AssertionError):
            # JavaScript bundles may contain strings that are not valid HTML.
            return print(name, result.returncode, result.stdout.splitlines()[:1], flush=True)
        (ROOT / (name + '.text.txt')).write_text('\n'.join(
            line.strip() for line in ''.join(parser.parts).splitlines() if line.strip()))
    print(name, result.returncode, result.stdout.splitlines()[:1], flush=True)


INITIAL = [
    ('openai-research', 'https://openai.com/research/'),
    ('openai-rss', 'https://openai.com/news/rss.xml'),
    ('anthropic-research', 'https://www.anthropic.com/research'),
    ('deepmind-research', 'https://deepmind.google/research/'),
    ('google-pubs', 'https://research.google/pubs/?category=2025&search=language%20model'),
    ('google-blog-october', 'https://www.research.google/blog/2025/10/'),
    ('meta-research', 'https://ai.meta.com/research/'),
    ('qwen-original', 'https://qwenlm.github.io/'),
    ('qwen-research', 'https://qwen.ai/research'),
    ('deepseek-home', 'https://www.deepseek.com/'),
    ('deepseek-news', 'https://www.deepseek.com/news/'),
    ('moonshot-blog', 'https://platform.kimi.com/blog'),
    ('hunyuan-research', 'https://hunyuan.tencent.com/research'),
    ('zai-research', 'https://www.zhipuai.cn/zh/research'),
    ('seed-research', 'https://seed.bytedance.com/en/research'),
    ('seed-papers', 'https://seed.bytedance.com/en/public_papers'),
    ('ernie-blog', 'https://ernie.baidu.com/blog/zh/'),
    ('mimo-home', 'https://mimo.xiaomi.com/'),
    ('minimax-en', 'https://www.minimax.io/blog'),
    ('minimax-cn', 'https://www.minimaxi.com/blog'),
    ('minimax-agent', 'https://agent.minimax.io/docs/techblog'),
    ('arxiv-announcement-help', 'https://info.arxiv.org/help/submit/index.html'),
]

THEMES = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (ti:language OR ti:transformer OR ti:foundation OR ti:MoE)',
    'system': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:inference OR all:training)',
    'agent': '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:retrieval OR ti:reasoning) AND (all:LLM OR all:language)',
    'multimodal': '(cat:cs.CV OR cat:cs.RO) AND (ti:vision-language OR ti:VLA OR ti:multimodal OR ti:world-model OR ti:diffusion)',
}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('group', choices=['initial', 'arxiv'])
    args = parser.parse_args()
    if args.group == 'initial':
        for name, url in INITIAL:
            fetch(name, url)
    else:
        for name, expression in THEMES.items():
            query = expression + ' AND submittedDate:[202510180100 TO 202510190100]'
            url = 'https://export.arxiv.org/api/query?' + urlencode({
                'search_query': query, 'start': 0, 'max_results': 25,
                'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
            fetch('arxiv-' + name, url)
