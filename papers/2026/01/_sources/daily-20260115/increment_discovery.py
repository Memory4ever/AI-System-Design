"""Read-only bounded API discovery; stdout only; titles are not an abstract queue."""
import concurrent.futures
import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

themes = {
    'model': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:Transformer OR all:MoE)',
    'agent': '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:LLM OR all:agent OR all:reasoning OR all:memory)',
    'multimodal': '(cat:cs.CV OR cat:cs.RO) AND (all:multimodal OR all:"world model" OR all:VLA OR all:diffusion)',
    'system': '(cat:cs.DC OR cat:cs.AR OR cat:cs.OS OR cat:cs.PL OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:kernel OR all:inference)',
}

def fetch(item):
    theme, start = item
    query = 'submittedDate:[20260112 TO 20260114] AND ' + themes[theme]
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': query, 'start': start, 'max_results': 100, 'sortBy': 'submittedDate', 'sortOrder': 'descending'})
    try:
        raw = urllib.request.urlopen(url, timeout=35).read().decode()
        root = ET.fromstring(raw)
        ns = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
        entries = [{k: e.findtext('a:' + k, namespaces=ns) for k in ['id', 'title', 'published', 'updated']} for e in root.findall('a:entry', ns)]
        return {'theme': theme, 'start': start, 'url': url, 'total': root.findtext('o:totalResults', namespaces=ns), 'entries': entries}
    except Exception as exc:
        return {'theme': theme, 'start': start, 'url': url, 'error': str(exc)}

requests = [(name, int(sys.argv[1]) if len(sys.argv) > 1 else 0) for name in themes]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(fetch, requests):
        print(json.dumps(result, ensure_ascii=False))
