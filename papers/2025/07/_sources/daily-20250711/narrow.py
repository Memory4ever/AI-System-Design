import concurrent.futures,json,urllib.parse,xml.etree.ElementTree as E
from capture import fetch,ROOT,NS
FIELDS=lambda terms:'('+' OR '.join(f'{field}:"{term}"' for term in terms for field in ['ti','abs'])+')'
GROUPS={
'narrow-model':('(cat:cs.CL OR cat:cs.LG OR cat:cs.AI)',FIELDS(['language model','LLM','Transformer','mixture of experts'])),
'narrow-systems':('(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF)',FIELDS(['language model','LLM','GPU','inference'])+' AND '+FIELDS(['cache','parallel','kernel','serving','scheduling','communication','quantization'])),
'narrow-agents':('(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL)',FIELDS(['language model','LLM'])+' AND '+FIELDS(['agent','retrieval','memory','planning','tool'])),
'narrow-multimodal':('(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG)',FIELDS(['vision language','multimodal','world model','vision language action','video generation','diffusion model'])),
}
def run(t):
 k,(cats,q)=t
 url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':cats+' AND '+q+' AND submittedDate:[202507091800 TO 202507101800]','start':0,'max_results':200,'sortBy':'submittedDate','sortOrder':'ascending'})
 raw=fetch(k,url)
 if not raw:return k,{}
 tree=E.fromstring(raw); entries=[{tag:' '.join(e.findtext('a:'+tag,default='',namespaces=NS).split()) for tag in ['id','title','summary','published','updated']} for e in tree.findall('a:entry',NS)]
 return k,{'total':tree.findtext('o:totalResults',namespaces=NS),'entries':entries}
with concurrent.futures.ThreadPoolExecutor(4) as p: data=dict(p.map(run,GROUPS.items()))
(ROOT/'narrow-discovery.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
for k,v in data.items():
 print(k,v.get('total'))
 for e in v.get('entries',[]):print(e['id'].split('/')[-1],e['title'])
