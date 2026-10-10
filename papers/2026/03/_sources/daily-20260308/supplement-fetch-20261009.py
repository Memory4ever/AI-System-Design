"""Bounded official-source fetch; raw bytes are evidence, not conclusions."""
import concurrent.futures, datetime, html.parser, json, pathlib, sys, urllib.request, urllib.parse, subprocess
ROOT = pathlib.Path(__file__).resolve().parent
class Text(html.parser.HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','div','li','h1','h2','h3','br','article','tr'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
def fetch(task):
    name,url,*body=task
    record={'name':name,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request=urllib.request.Request(url,data=json.dumps(body[0]).encode() if body else None,headers={'User-Agent':'Mozilla/5.0 research review','Content-Type':'application/json','accept-language':'zh','x-tt-locale':'US','Origin':'https://hunyuan.tencent.com'})
        if body:
            with urllib.request.urlopen(request,timeout=35) as response:
                raw=response.read();record.update(status=response.status,final_url=response.url,bytes=len(raw))
        else:
            result=subprocess.run(['curl','-fLsS','--max-time','30',url],capture_output=True,check=True)
            raw=result.stdout;record.update(status=200,bytes=len(raw),transport='curl')
        (ROOT/(name+'.raw')).write_bytes(raw)
        parsed=Text();parsed.feed(raw.decode('utf-8','replace'))
        (ROOT/(name+'.txt')).write_text('\n'.join(line.strip() for line in ''.join(parsed.parts).splitlines() if line.strip()))
    except Exception as error: record['error']=str(error)
    return record
tasks=json.loads(sys.argv[1]);records=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(fetch,tasks))
(ROOT/('SUP_FETCH_'+sys.argv[2]+'.json')).write_text(json.dumps(records,indent=2,ensure_ascii=False))
for record in records: print(json.dumps(record,ensure_ascii=False))
