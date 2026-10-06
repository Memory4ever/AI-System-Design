"""Four bounded topic searches; validates submission filter without claiming public dates."""
import datetime,json,pathlib,urllib.request,urllib.parse,xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
ROOT=pathlib.Path(__file__).parent/'supplement-20261007';ROOT.mkdir(exist_ok=True)
TOPICS={
 'model':'(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:Transformer OR all:MoE OR all:"foundation model")',
 'systems':'(cat:cs.DC OR cat:cs.AR OR cat:cs.OS OR cat:cs.PF OR cat:cs.PL) AND (all:LLM OR all:"language model" OR all:GPU OR all:Transformer)',
 'multimodal':'(cat:cs.CV OR cat:cs.RO) AND (all:"vision language" OR all:"world model" OR all:VLA OR all:"diffusion model" OR all:"multimodal model")',
 'agent':'(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:LLM OR all:"language model" OR all:"foundation model")'}
NS={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
def fetch(job):
 theme,start=job;query='submittedDate:[20260113 TO 20260115] AND '+TOPICS[theme]
 url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':query,'start':start,'max_results':100,'sortBy':'submittedDate','sortOrder':'ascending'})
 name='arxiv-'+theme+'-'+str(start);r={'theme':theme,'start':start,'query':query,'url':url,'checked':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  raw=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=35).read().decode();(ROOT/(name+'.raw')).write_text(raw)
  node=ET.fromstring(raw);entries=[]
  for e in node.findall('a:entry',NS):
   entries.append({k:' '.join(e.findtext('a:'+k,default='',namespaces=NS).split()) for k in ['id','title','published','updated','summary']})
  r.update(total=node.findtext('o:totalResults',namespaces=NS),entries=entries,range_valid=all('2026-01-13'<=e['published'][:10]<='2026-01-15' for e in entries))
 except Exception as e:r['error']=str(e)
 (ROOT/(name+'.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2));return {k:v for k,v in r.items() if k!='entries'}|{'count':len(r.get('entries',[]))}
with ThreadPoolExecutor(max_workers=4) as pool:
 for result in pool.map(fetch,[(theme,page) for theme in TOPICS for page in [0,100,200]]):print(json.dumps(result,ensure_ascii=False))
