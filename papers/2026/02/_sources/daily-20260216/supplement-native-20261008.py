"""Read-only, bounded native date recovery for Daily 2026-02-16; prints evidence."""
import concurrent.futures
import json
import re
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone, timedelta

URLS = [
    'https://openai.com/news/rss.xml',
    'https://www.anthropic.com/research',
    'https://www.zhipuai.cn/zh/research',
    'https://hunyuan.tencent.com/research',
]

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=18) as response:
            raw = response.read().decode('utf-8', errors='replace')
            result = {'url': url, 'status': response.status, 'final_url': response.url, 'bytes': len(raw)}
        if url.endswith('rss.xml'):
            from email.utils import parsedate_to_datetime
            rows = []
            for item in ET.fromstring(raw).findall('.//item'):
                date = item.findtext('pubDate')
                if not date:
                    continue
                dt = parsedate_to_datetime(date).astimezone(timezone(timedelta(hours=8)))
                if '2026-02-12' <= dt.date().isoformat() <= '2026-02-18':
                    rows.append({'title': item.findtext('title'), 'url': item.findtext('link'), 'raw_pubDate': date, 'bjt_date': dt.date().isoformat()})
            result['window_and_neighbor_items'] = rows
        else:
            result['February_date_contexts'] = [raw[max(0,m.start()-220):m.end()+240] for m in re.finditer(r'2026[-/]0?2[-/]\d\d',raw)][:45]
            result['script_urls'] = re.findall(r'<script[^>]+src=["\']([^"\']+)', raw)[:12]
            result['title'] = re.findall(r'<title>(.*?)</title>',raw)
        return result
    except Exception as exc:
        return {'url':url, 'error':str(exc), 'timeout_seconds':18}

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    print(json.dumps(list(executor.map(fetch, URLS)), ensure_ascii=False, indent=2))
