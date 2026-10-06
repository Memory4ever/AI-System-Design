"""Bounded primary-source fetcher; outputs confined to this Daily's evidence folder."""
import concurrent.futures, datetime, json, pathlib, sys, urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).parent / 'supplement-20261007'
ROOT.mkdir(exist_ok=True)
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.hide=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.hide+=1
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.hide=max(0,self.hide-1)
    def handle_data(self, data):
        if not self.hide and data.strip(): self.parts.append(data.strip())

def fetch(job):
    name,url=job.split('=',1)
    result={'name':name,'url':url,'checked':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0','x-tt-locale':'CN'})
        with urllib.request.urlopen(req,timeout=35) as response:
            data=response.read();result.update(status=response.status,final_url=response.url,bytes=len(data))
        raw=data.decode('utf-8','replace');(ROOT/(name+'.raw')).write_text(raw)
        parser=Text();parser.feed(raw);(ROOT/(name+'.txt')).write_text('\n'.join(parser.parts))
    except Exception as exc: result['error']=str(exc)
    (ROOT/(name+'.request.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for result in pool.map(fetch,sys.argv[1:]): print(json.dumps(result,ensure_ascii=False))
