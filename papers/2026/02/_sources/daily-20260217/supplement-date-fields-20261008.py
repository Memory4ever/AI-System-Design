import concurrent.futures
import json
import re
import urllib.request
from html import unescape
from pathlib import Path
from datetime import datetime, timezone

packet = Path('papers/2026/02/_sources/daily-20260217/supplement-admission-20261008.md').read_text()
block = packet.split('## 后续78条完整题摘校准清单')[1].split('## 明确关闭项')[0]
identities = re.findall(r'^\| (\d{4}\.\d{5})', block, re.M)

def fetch(identity):
    url = 'https://arxiv.org/abs/' + identity
    row = {'id':identity,'url':url,'checked_utc':datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0 Research-audit'}), timeout=20) as response:
            body = response.read().decode('utf-8','replace')
            row['status'] = response.status
            row['date_text'] = unescape(re.sub('<[^>]+>',' ',body[body.find('<div class="dateline">'):body.find('<h1 class="title')]))
            history = re.search(r'<div[^>]*class="submission-history".*?(?=<div[^>]*class="extra-services|<div[^>]*class="full-text|</div>\s*</div>)', body,re.S)
            row['history_text'] = unescape(re.sub('<[^>]+>',' ',history.group(0)))[:1000] if history else ''
            row['public_dates'] = re.findall(r'(?:announced|first.public|made.public)[^<\n]{0,160}', body, re.I)
            row['notices'] = re.findall(r'(?:withdrawn|retracted|erratum|correction)[^<\n]{0,200}', body,re.I)
            row['title'] = unescape(re.sub('<[^>]+>',' ',re.search(r'<h1 class="title.*?</h1>',body,re.S).group(0))) if re.search(r'<h1 class="title.*?</h1>',body,re.S) else ''
            row['external_project_links'] = [u for u in sorted(set(re.findall(r'href="(https?://[^"<> ]+)"',body))) if ('github.com/' in u or 'github.io/' in u) and '/arXiv/' not in u and '/arxiv/' not in u]
            row['adoption'] = 'Only identity/notice/date-role check; Submitted and version history are not public dates; no performance/Books adoption.'
    except Exception as error:
        row['error'] = str(error)
    return row

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    print(json.dumps(list(pool.map(fetch,identities)), ensure_ascii=False,indent=2))
