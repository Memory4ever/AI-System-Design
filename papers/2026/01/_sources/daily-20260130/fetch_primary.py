#!/usr/bin/env python3
"""Bounded read-only URL extraction for this Daily; persistence is via apply_patch."""
import sys, json, urllib.request, xml.etree.ElementTree as ET
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.items=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip += 1
        if tag in ('h1','h2','h3','dt','dd','p','li','div'): self.items.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self, value):
        if not self.skip: self.items.append(value)

url=sys.argv[1]
try:
    with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AI-System-Design research'}),timeout=25) as r:
        raw=r.read().decode('utf-8')
    if raw.lstrip().startswith('{'):
        obj=json.loads(raw)
        if '--titles' in sys.argv and 'data' in obj:
            obj={'meta':obj.get('meta'), 'links':obj.get('links'), 'data':[{'id':x['id'],'title':x['attributes'].get('titles'), 'created':x['attributes'].get('created'),'v1_dates':[d for d in x['attributes'].get('dates',[]) if d.get('dateInformation')=='v1'],'subjects':[s['subject'] for s in x['attributes'].get('subjects',[]) if s.get('subjectScheme')=='arXiv']} for x in obj['data']]}
            print(json.dumps({'url':url,'meta':obj['meta'],'links':obj['links']},ensure_ascii=False))
            for row in obj['data']: print(json.dumps(row,ensure_ascii=False))
            sys.exit()
        print(json.dumps({'url':url,'payload':obj},ensure_ascii=False))
    elif '<feed' in raw[:500]:
        root=ET.fromstring(raw); ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
        entries=[{k:e.findtext('a:'+k,default='',namespaces=ns) for k in ('id','title','published','updated','summary')} for e in root.findall('a:entry',ns)]
        print(json.dumps({'url':url,'total':root.findtext('o:totalResults',namespaces=ns),'entries':entries},ensure_ascii=False,indent=2))
    else:
        p=Text(); p.feed(raw)
        clean='\n'.join(s.strip() for s in ''.join(p.items).splitlines() if s.strip())
        if '--list-slice' in sys.argv:
            import re
            found=[]
            for match in re.finditer(r'arXiv:(2601\.(\d{5})).*?Title:\s*(.*?)\n',clean,re.S):
                if 19900 <= int(match.group(2)) <= 20868:
                    found.append({'id':match.group(1),'title':match.group(3)})
            print(json.dumps({'url':url,'scope':'Specific observed DOI-window ID neighborhood only; no exact announcement-day assertion','rows':found},ensure_ascii=False,indent=2));sys.exit()
        if '--ab' in sys.argv:
            clean=clean.split('Full-text links:')[0]
            start=clean.find('arXiv:')
            if start>=0: clean=clean[start:]
        print(url+'\n'+clean)
except Exception as e:
    print(json.dumps({'url':url,'error':str(e)},ensure_ascii=False))
