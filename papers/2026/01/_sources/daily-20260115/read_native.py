"""Read-only network recovery; stdout only, no local writes."""
import concurrent.futures
import html
import json
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET


def fetch(url):
    try:
        raw = urllib.request.urlopen(url, timeout=35).read().decode()
        if 'export.arxiv.org/api/query' in url:
            root = ET.fromstring(raw)
            ns = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
            return {'url': url, 'total': root.findtext('o:totalResults', namespaces=ns),
                    'entries': [{k: e.findtext('a:'+k, namespaces=ns) for k in ['id', 'title', 'published', 'updated', 'summary']}
                                for e in root.findall('a:entry', ns)]}
        if '/abs/' in url:
            patterns = [r'<h1[^>]*>(.*?)</h1>', r'<blockquote[^>]*>(.*?)</blockquote>', r'<div class="submission-history"[^>]*>(.*?)</div>']
            parts = [m for p in patterns for m in re.findall(p, raw, re.S)]
            text = '\n'.join(parts)
        elif '/list/' in url:
            text = raw
        else:
            text = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', raw, flags=re.S)
        text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
        text = re.sub(r'[ \t]+', ' ', text)
        text = re.sub(r'\n\s*\n+', '\n', text).strip()
        return {'url': url, 'text': text}
    except Exception as e:
        return {'url': url, 'error': str(e)}


with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(fetch, sys.argv[1:]):
        print(json.dumps(result, ensure_ascii=False))
