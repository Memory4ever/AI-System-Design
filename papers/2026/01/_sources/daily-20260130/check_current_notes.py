#!/usr/bin/env python3
"""Read-only lightweight current event-note check for named Daily identities."""
import sys, json, re, urllib.request, concurrent.futures
from html.parser import HTMLParser
class Text(HTMLParser):
    def __init__(self): super().__init__(); self.items=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('script','style'): self.skip+=1
        if t in ('h1','h2','p','div','td','li'): self.items.append('\n')
    def handle_endtag(self,t):
        if t in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,d):
        if not self.skip:self.items.append(d)
def check(paper):
    url='https://arxiv.org/abs/'+paper
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'AI-System-Design bounded note check'}),timeout=25) as r:raw=r.read().decode()
        p=Text();p.feed(raw);s='\n'.join(x.strip() for x in ''.join(p.items).splitlines() if x.strip())
        note=re.search(r'Comments:\s*(.*?)\nSubjects:',s,re.S)
        header=re.search(r'\[Submitted.*?\nTitle:.*?\nAuthors:',s,re.S)
        return {'id':paper,'url':url,'header':header.group(0).removesuffix('\nAuthors:') if header else None,'withdrawn':bool(re.search(r'This paper has been withdrawn|Withdrawn',s)),'comments':note.group(1) if note else None}
    except Exception as e:return {'id':paper,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for result in ex.map(check,sys.argv[1:]):print(json.dumps(result,ensure_ascii=False))
