"""Bounded date-scoped evidence retrieval. Payloads are not verdicts."""
import concurrent.futures
import datetime
import html
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

target = pathlib.Path(__file__).resolve().parent
def fetch(spec):
    name, url = spec
    data = {"url": url, "checked": datetime.datetime.now().astimezone().isoformat()}
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "ResearchAudit/1.0"}), timeout=35) as response:
            raw = response.read().decode("utf-8", errors="replace")
            data.update(status=response.status, raw=raw)
        visible = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', raw, flags=re.S)
        visible = re.sub(r'</(?:p|h[1-6]|div|li|tr|section)>', '\n', visible)
        data['text'] = '\n'.join(' '.join(line.split()) for line in html.unescape(re.sub(r'<[^>]+>', ' ', visible)).splitlines() if line.strip())
        if '/api/query?' in url:
            root = ET.fromstring(raw)
            ns = {"a":"http://www.w3.org/2005/Atom", "o":"http://a9.com/-/spec/opensearch/1.1/"}
            data['total'] = root.findtext('o:totalResults', namespaces=ns)
            data['entries'] = [{k:e.findtext('a:'+k, namespaces=ns) for k in ('id','title','summary','published','updated')} for e in root.findall('a:entry',ns)]
    except Exception as exc:
        data['error'] = repr(exc)
    (target / (name+'.json')).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')
    return {k:v for k,v in data.items() if k not in ('raw','text','entries')}

if __name__ == '__main__':
    specs = json.loads(sys.argv[1])
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for result in executor.map(fetch, specs):
            print(json.dumps(result,ensure_ascii=False))
