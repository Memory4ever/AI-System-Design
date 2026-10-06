import concurrent.futures, datetime, json, pathlib, sys, urllib.request
from html.parser import HTMLParser

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.hidden=0
    def handle_starttag(self, tag, attrs):
        if tag in ['script','style','noscript']: self.hidden+=1
    def handle_endtag(self, tag):
        if tag in ['script','style','noscript']: self.hidden=max(0,self.hidden-1)
    def handle_data(self, data):
        if not self.hidden and data.strip(): self.parts.append(data.strip())

ROOT=pathlib.Path(__file__).resolve().parent
def fetch(entry):
    name,url,*payload=entry
    try:
        headers={'User-Agent':'Mozilla/5.0 Research Evidence Reader'}; data=None
        if payload:
            data=json.dumps(payload[0]).encode(); headers.update({'Content-Type':'application/json','accept-language':'zh-CN','Origin':'https://hunyuan.tencent.com'})
        with urllib.request.urlopen(urllib.request.Request(url,data=data,headers=headers),timeout=40) as r:
            raw=r.read().decode('utf-8',errors='replace'); meta={'url':url,'resolved':r.url,'status':r.status,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        (ROOT/(name+'.raw')).write_text(raw)
        parser=TextParser(); parser.feed(raw); body='\n'.join(parser.parts)
        (ROOT/(name+'.txt')).write_text(body); meta['text_length']=len(body)
        return {'name':name,**meta}
    except Exception as e: return {'name':name,'url':url,'error':str(e)}

if __name__=='__main__':
    entries=json.loads(sys.argv[1])
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as ex: results=list(ex.map(fetch,entries))
    (ROOT/('V3_FETCH_'+sys.argv[2]+'.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(results,ensure_ascii=False,indent=2))
