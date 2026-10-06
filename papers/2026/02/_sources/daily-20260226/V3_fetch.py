import concurrent.futures, json, pathlib, sys, urllib.request, datetime, re
from html.parser import HTMLParser
class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.hidden=0
    def handle_starttag(self,tag,attrs):
        if tag in ['script','style','noscript']: self.hidden += 1
    def handle_endtag(self,tag):
        if tag in ['script','style','noscript']: self.hidden=max(0,self.hidden-1)
    def handle_data(self,data):
        if not self.hidden and data.strip(): self.parts.append(data.strip())

ROOT = pathlib.Path(__file__).resolve().parent
def fetch(entry):
    name, url, *payload = entry
    try:
        headers={'User-Agent': 'Mozilla/5.0 Research Evidence Reader'}
        data=None
        if payload:
            data=json.dumps(payload[0]).encode(); headers.update({'Content-Type':'application/json','accept-language':'zh-CN','Origin':'https://hunyuan.tencent.com'})
        req = urllib.request.Request(url,data=data, headers=headers)
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read().decode('utf-8', errors='replace')
            meta = {'url':url,'resolved':r.url,'status':r.status,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        (ROOT / (name + '.raw')).write_text(raw)
        parser = TextParser(); parser.feed(raw)
        text = '\n'.join(parser.parts)
        (ROOT / (name + '.txt')).write_text(text)
        meta['text_length'] = len(text)
        print(json.dumps({'name':name,**meta},ensure_ascii=False),flush=True)
        return {'name':name,**meta}
    except Exception as e:
        result = {'name':name,'url':url,'error':str(e)}
        print(json.dumps(result),flush=True)
        return result
if __name__ == '__main__':
    if sys.argv[1]=='--abstracts':
        ids = set(re.findall(r'^## (2602\.\d+)',(ROOT/'V3_FIRST_ABSTRACT_PACKET.md').read_text()+'\n'+(ROOT/'V3_SECOND_ABSTRACT_PACKET.md').read_text(),re.M))
        entries=[['V3_ABS_'+identity,'https://arxiv.org/abs/'+identity+'v1'] for identity in sorted(ids)]
    else:
        entries = json.loads(sys.argv[1])
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(fetch,entries))
    (ROOT / ('V3_FETCH_' + sys.argv[2] + '.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2))
