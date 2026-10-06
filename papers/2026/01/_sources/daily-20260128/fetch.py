"""Bounded retrieval; payloads are source records, never admission verdicts."""
import datetime, html, json, pathlib, re, sys, urllib.parse, urllib.request, xml.etree.ElementTree as ET
destination = pathlib.Path(__file__).resolve().parent
name, mode, value = sys.argv[1:]
if mode == 'query':
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':value,'start':0,'max_results':150,'sortBy':'submittedDate','sortOrder':'ascending'})
elif mode == 'ids':
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'id_list':value,'max_results':200})
else: url = value
try:
    with urllib.request.urlopen(url, timeout=45) as response: raw=response.read().decode('utf-8')
    payload={'url':url,'checked':datetime.datetime.now().astimezone().isoformat(),'raw':raw}
    if mode in ('html','abs'):
        visible=re.sub(r'<(script|style)\b[^>]*>.*?</\1>','',raw,flags=re.S)
        visible=re.sub(r'</(?:p|h[1-6]|div|li|tr|section)>','\n',visible)
        payload['text']='\n'.join(' '.join(line.split()) for line in html.unescape(re.sub(r'<[^>]+>',' ',visible)).splitlines() if line.strip())
    if mode in ('query','ids'):
        root=ET.fromstring(raw); ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
        payload['total']=root.findtext('o:totalResults',namespaces=ns)
        payload['entries']=[{k:e.findtext('a:'+k,namespaces=ns) for k in ('id','title','summary','published','updated')} for e in root.findall('a:entry',ns)]
except Exception as exc: payload={'url':url,'checked':datetime.datetime.now().astimezone().isoformat(),'error':str(exc)}
(destination/name).write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in payload.items() if k not in ('raw','text','entries')},ensure_ascii=False))
for e in payload.get('entries',[]): print(e['id'], ' '.join(e['title'].split()))
