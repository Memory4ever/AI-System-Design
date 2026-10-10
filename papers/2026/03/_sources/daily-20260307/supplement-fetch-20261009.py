"""Bounded read-only network capture; writes generated raw/text receipts beside itself."""
import concurrent.futures, datetime, json, pathlib, subprocess, sys
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent
class Text(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,t,a):
        if t in ('script','style'): self.skip+=1
    def handle_endtag(self,t):
        if t in ('script','style') and self.skip: self.skip-=1
    def handle_data(self,d):
        if not self.skip and d.strip(): self.parts.append(d.strip())
def fetch(item):
    label,url,*body=item
    command=['curl','-L','--max-time','35','-sS','-A','Mozilla/5.0','-H','accept-language: zh',url]
    if body and body[0] is not None: command+=['-H','Content-Type: application/json','--data',json.dumps(body[0])]
    if len(body)>1:
        for header in body[1]: command+=['-H',header]
    result=subprocess.run(command,capture_output=True)
    raw=result.stdout
    (ROOT/(label+'.raw')).write_bytes(raw)
    parser=Text(); parser.feed(raw.decode('utf-8','replace'))
    (ROOT/(label+'.txt')).write_text('\n'.join(parser.parts))
    return {'label':label,'url':url,'bytes':len(raw),'returncode':result.returncode,'error':result.stderr.decode(),'checked':datetime.datetime.now(datetime.timezone.utc).isoformat()}
items=json.loads(sys.argv[2])
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    result=list(pool.map(fetch,items))
(ROOT/('SUP_FETCH_'+sys.argv[1]+'.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
