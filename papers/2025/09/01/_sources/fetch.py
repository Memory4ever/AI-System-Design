import concurrent.futures, datetime, gzip, json, pathlib, subprocess, sys
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).parent
class Extract(HTMLParser):
    def __init__(self):super().__init__();self.text=[];self.links=[];self.skip=0;self.link=None
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
        if tag=='a':self.link={'text':'','href':dict(attrs).get('href')}
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.skip=max(0,self.skip-1)
        if tag=='a' and self.link:self.links.append(self.link);self.link=None
    def handle_data(self,data):
        if not self.skip:self.text.append(data.strip())
        if self.link:self.link['text']+=data.strip()+' '
def fetch(item):
    key,url=item
    meta={'key':key,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        tmp=ROOT/(key+'.curl.tmp')
        done=subprocess.run(['curl','-sS','-L','--compressed','--max-time','45','-o',str(tmp),'-w','%{http_code}\n%{url_effective}\n%{content_type}',url],capture_output=True,text=True)
        fields=done.stdout.splitlines();content=tmp.read_bytes() if tmp.exists() else b''
        meta.update(status=int(fields[0]) if fields else 0,final_url=fields[1] if len(fields)>1 else url,bytes=len(content),content_type=fields[2] if len(fields)>2 else '',exit_code=done.returncode)
        if done.returncode:meta['error']=done.stderr
        tmp.unlink(missing_ok=True)
        with gzip.open(ROOT/(key+'.raw.gz'),'wb') as f:f.write(content)
        parsed=Extract();parsed.feed(content.decode('utf-8',errors='replace'))
        (ROOT/(key+'.txt')).write_text(' '.join(t for t in parsed.text if t))
        (ROOT/(key+'.links.json')).write_text(json.dumps(parsed.links,ensure_ascii=False,indent=2))
    except Exception as e:meta['error']=str(e)
    (ROOT/(key+'.meta.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2))
    return meta
if __name__=='__main__':
    items=json.loads(pathlib.Path(sys.argv[1]).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for result in ex.map(fetch,items):print(json.dumps(result,ensure_ascii=False))
