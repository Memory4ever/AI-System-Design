import pathlib,json,re,sys
from html.parser import HTMLParser
from V3_fetch import TextParser
ROOT=pathlib.Path(__file__).resolve().parent
class Extract(HTMLParser):
    def __init__(self):
        super().__init__(); self.depth=0; self.abstract=[]
    def handle_starttag(self,t,a):
        if t=='blockquote' and 'abstract' in dict(a).get('class',''):self.depth=1
        elif self.depth:self.depth+=1
    def handle_endtag(self,t):
        if self.depth:self.depth-=1
    def handle_data(self,x):
        if self.depth:self.abstract.append(x)
rs=sum([json.loads(p.read_text())['data'] for p in ROOT.glob('V3_DATACITE_WINDOW*.raw')],[])
idx={r['id']:r['attributes'] for r in rs}
out=[]; packet=[]
for p in sorted(ROOT.glob('V3_ABS_*.raw')):
    identity=p.stem.removeprefix('V3_ABS_'); raw=p.read_text(); parser=TextParser()
    block=re.search(r'<blockquote class="abstract[^\"]*"[^>]*>(.*?)</blockquote>',raw,re.S)
    parser.feed(block.group(1) if block else '')
    a=idx.get('10.48550/arxiv.'+identity,{})
    title=re.search(r'<meta name="citation_title" content="([^"]*)"',raw)
    abstract='\n'.join(parser.parts).strip(); abstract=re.sub(r'^Abstract:\s*','',abstract)
    item={'id':identity,'title':title.group(1) if title else '', 'abstract':abstract,'registered':a.get('registered'),'created':a.get('created'),'dates':a.get('dates'), 'source':'V3_ABS_'+identity+'.raw','raw_datacite_source':'V3_DATACITE_WINDOW*.raw','version':'v1'}
    out.append(item);packet+=['## '+identity+' '+item['title'],'','精确v1：[原源](https://arxiv.org/abs/'+identity+'v1)，Registered='+str(item['registered'])+'（该字段不是Submitted；公开区间另核）。','',item['abstract'],'']
(ROOT/'V3_CURRENT_ABSTRACTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
(ROOT/'V3_CURRENT_ABSTRACTS.md').write_text('\n'.join(packet))
print('exact v1 abstracts',len(out),'empty',sum(not r['abstract'] for r in out))
