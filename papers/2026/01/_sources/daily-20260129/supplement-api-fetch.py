import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

query = sys.argv[1]
url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': query, 'start': 0, 'max_results': 100, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'})
try:
    raw = urllib.request.urlopen(url, timeout=30).read().decode()
    root = ET.fromstring(raw)
    namespace = {'a': 'http://www.w3.org/2005/Atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
    records = []
    for entry in root.findall('a:entry', namespace):
        records.append({key: entry.find('a:' + key, namespace).text.strip() for key in ['id', 'title', 'published', 'updated']})
    print(json.dumps({'query': query, 'url': url, 'total': root.find('o:totalResults', namespace).text, 'records': records}))
except Exception as error:
    print(json.dumps({'query': query, 'url': url, 'error': str(error)}))
