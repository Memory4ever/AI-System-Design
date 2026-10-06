import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urlencode
from urllib.parse import urljoin

from acquire import ROOT, fetch


def scripts(name):
    return re.findall(r'<script[^>]+src=[\"\x27]([^\"\x27]+)',
                      (ROOT / (name + '.raw')).read_text())


if sys.argv[1] == 'native':
    fetch('google-pubs-retry', 'https://research.google/pubs/?category=2025&search=language%20model')
    fetch('google-blog-retry', 'https://www.research.google/blog/2025/10/')
    fetch('zai-page2', 'https://www.zhipuai.cn/zh/research?page=2')
    fetch('ernie-page2', 'https://ernie.baidu.com/blog/zh/page/2/')
    for name, base, fragment in [
        ('deepseek-news', 'https://www.deepseek.com', '/news/page-'),
        ('zai-research', 'https://www.zhipuai.cn', '/research/page-'),
        ('seed-papers', 'https://seed.bytedance.com', '/main.'),
        ('hunyuan-research', 'https://hunyuan.tencent.com', '/index-'),
        ('mimo-home', 'https://mimo.xiaomi.com', '/index.'),
        ('qwen-research', 'https://qwen.ai', '/main.'),
    ]:
        for src in scripts(name):
            if fragment in src:
                fetch(name + '-bundle', urljoin(base, src))
                break
elif sys.argv[1] == 'first':
    for paper in ('2510.16598', '2510.16448', '2510.16415',
                  '2510.16567', '2510.16660', '2510.16359'):
        fetch('abs-' + paper + 'v1', 'https://arxiv.org/abs/' + paper + 'v1')
elif sys.argv[1] == 'help':
    fetch('arxiv-availability', 'https://info.arxiv.org/help/availability.html')
elif sys.argv[1] == 'modules':
    fetch('hunyuan-blog-module', 'https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-CUQAWQeM.js')
    fetch('qwen-research-module', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_research-index.js')
    fetch('mimo-paper-module', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js')
    for kind, limit in ((1, 100), (2, 60)):
        for offset in range(0, limit, 20):
            url = 'https://seed.bytedance.com/api/get_article_list_v2?' + urlencode({
                'article_type': kind, 'page_token': offset, 'count': 20,
                'order_desc': 'true', 'query': '', 'publish_year': '',
                'research_area_id': '', 'work_team_id': ''})
            name = f'seed-type{kind}-{offset}'
            fetch(name, url, headers={'x-tt-locale': 'US'} if kind == 1 else {})
            import json
            data = json.loads((ROOT / (name + '.raw')).read_text())
            if not data.get('has_more'):
                break
elif sys.argv[1] == 'abs':
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    ids = set()
    for topic in ('model', 'system', 'agent', 'multimodal'):
        tree = ET.fromstring((ROOT / ('arxiv-' + topic + '.raw')).read_bytes())
        for entry in tree.findall('a:entry', ns):
            url = entry.findtext('a:id', namespaces=ns)
            ids.add(url.rsplit('/', 1)[-1].split('v')[0])
    for paper in sorted(ids):
        name = 'abs-' + paper + 'v1'
        if not (ROOT / (name + '.raw')).exists():
            fetch(name, 'https://arxiv.org/abs/' + paper + 'v1')
elif sys.argv[1] == 'titles':
    for category in ('cs.CL', 'cs.CV', 'cs.DC', 'cs.PL', 'cs.IR'):
        query = 'cat:' + category + ' AND submittedDate:[202510180100 TO 202510190100]'
        url = 'https://export.arxiv.org/api/query?' + urlencode({
            'search_query': query, 'start': 0, 'max_results': 12,
            'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
        fetch('titles-' + category, url)
elif sys.argv[1] == 'services':
    fetch('hunyuan-api-module', 'https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-cEoitnb7.js')
    fetch('qwen-service-module', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/80126a68.js')
    fetch('qwen-extra-module', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/9e22d361.js')
    fetch('deepmind-publications', 'https://deepmind.google/research/publications/')
    fetch('diarize-official-model', 'https://developers.openai.com/api/docs/models/gpt-4o-transcribe-diarize')
elif sys.argv[1] == 'native2':
    fetch('hunyuan-list', 'https://hunyuan.tencent.com/api/blog/publicList', 'POST',
          {'pageNum': 1, 'pageSize': 20, 'renderType': 0},
          {'Content-Type': 'application/json'})
    fetch('qwen-service2', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/b3cb5cc6.js')
    fetch('qwen-service3', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/5fb222f6.js')
    fetch('withdrawn-2510.16309', 'https://arxiv.org/abs/2510.16309')
    for paper in ('2510.16333', '2510.16449', '2510.16384', '2510.16474'):
        fetch('abs-' + paper + 'v1', 'https://arxiv.org/abs/' + paper + 'v1')
    for kind, start, limit in ((1, 100, 260), (2, 60, 120)):
        for offset in range(start, limit, 20):
            url = 'https://seed.bytedance.com/api/get_article_list_v2?' + urlencode({
                'article_type': kind, 'page_token': offset, 'count': 20,
                'order_desc': 'true', 'query': '', 'publish_year': '',
                'research_area_id': '', 'work_team_id': ''})
            name = f'seed-type{kind}-{offset}'
            fetch(name, url, headers={'x-tt-locale': 'US'} if kind == 1 else {})
            import json
            data = json.loads((ROOT / (name + '.raw')).read_text())
            dates = [x.get('ArticleMeta', {}).get('PublishDate', 0) for x in data.get('sub_article_list', [])]
            boundary = 1760749200000
            if not data.get('has_more') or (dates and min(dates) < boundary):
                break
elif sys.argv[1] == 'titles-retry':
    for category in ('cs.CL', 'cs.CV', 'cs.DC', 'cs.PL', 'cs.IR'):
        query = 'cat:' + category + ' AND submittedDate:[202510180100 TO 202510190100]'
        url = 'https://arxiv.org/api/query?' + urlencode({
            'search_query': query, 'start': 0, 'max_results': 12,
            'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
        fetch('titles-retry-' + category, url)
