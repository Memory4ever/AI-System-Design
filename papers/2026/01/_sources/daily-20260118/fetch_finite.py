"""Read-only bounded HTTP extraction; admission is manual, not keyword-based."""
import concurrent.futures
import datetime
import html
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip+=1
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,data):
        if not self.skip and data.strip(): self.parts.append(data.strip())

def fetch(url):
    out={'url':url,'execution_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        r=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35)
        s=r.read().decode();out.update(status=r.status,final_url=r.url)
        if s.lstrip().startswith(('{','[')):
            out['data']=json.loads(s); return out
        if '.js' in url:
            out['endpoint_contexts']=[s[max(0,m.start()-160):m.end()+220] for m in list(re.finditer(r'publicList|paper/list|articles|/api/[^"\s]{1,70}|baseURL|publish_time|publish_date|news/list',s))[:35]]
            return out
        p=Text();p.feed(s)
        out['text']='\n'.join(p.parts)[-19000:]
        out['scripts']=re.findall(r'<script[^>]+src=["\']([^"\']+)',s)
        out['date_contexts']=[s[max(0,m.start()-120):m.end()+230] for m in list(re.finditer(r'2026[-/]01[-/](?:1[5-9]|2[01])',s))[:30]]
    except Exception as e:out['error']=str(e)
    return out

print(json.dumps(list(concurrent.futures.ThreadPoolExecutor(6).map(fetch,sys.argv[1:])),ensure_ascii=False))
