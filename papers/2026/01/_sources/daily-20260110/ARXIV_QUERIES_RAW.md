# Actual Submitted-buffer query definitions

Executed 2026-10-02T16:41:22.711728Z. This is a bounded Submitted discovery buffer, not public-event or revision recall. architecture/world-vla returned 429; other six requests read-timeout25. Failed responses do not mean zero events.

```python
python3 - <<'PY'
import urllib.request,urllib.parse,xml.etree.ElementTree as ET,json,concurrent.futures,datetime
buf='submittedDate:[202601071900 TO 202601081900]'
qs={
'architecture':'(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:Transformer OR all:"mixture of experts")',
'training':'(cat:cs.CL OR cat:cs.LG) AND (all:"language model" AND (all:"reinforcement learning" OR all:"preference optimization" OR all:pretraining OR all:"fine-tuning"))',
'serving':'(cat:cs.DC OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"LLM serving" OR all:"KV cache" OR all:"large language model inference" OR all:"GPU inference")',
'agent-memory':'(cat:cs.AI OR cat:cs.MA OR cat:cs.CL OR cat:cs.IR) AND (all:"language model" AND (all:agent OR all:memory OR all:"tool calling" OR all:retrieval))',
'evaluation-safety':'(cat:cs.CL OR cat:cs.AI) AND (all:"language model" AND (all:safety OR all:evaluation OR all:reasoning OR all:uncertainty))',
'multimodal-generation':'(cat:cs.CV OR cat:cs.CL) AND (all:"multimodal foundation" OR all:"video generation" OR all:"image generation" OR all:"vision language model")',
'world-vla':'(cat:cs.RO OR cat:cs.CV OR cat:cs.AI) AND (all:"world model" OR all:"vision language action" OR all:VLA)',
'kernel-compiler':'(cat:cs.AR OR cat:cs.PL OR cat:cs.DC) AND (all:"language model" OR all:"GPU kernel" OR all:"tensor compiler")'}
ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
def get(k):
 q='('+qs[k]+') AND '+buf;u='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'start':0,'max_results':60,'sortBy':'submittedDate','sortOrder':'ascending'})
 try:
  res=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'DailyResearch-Jan10-window'}),timeout=25);raw=res.read().decode();root=ET.fromstring(raw)
  rows=[]
  for e in root.findall('a:entry',ns): rows.append({x:e.findtext('a:'+x,default='',namespaces=ns).strip() for x in ['id','title','summary','published','updated']})
  return {'theme':k,'url':u,'query':q,'status':res.status,'total':root.findtext('o:totalResults',default='',namespaces=ns),'entries':rows,'next_start':60 if len(rows)==60 else None,'raw_feed':raw}
 except Exception as e:return {'theme':k,'url':u,'query':q,'error':str(e)}
print(json.dumps({'executed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'buffer':'Submitted-only, NOT public-date proof','results':list(concurrent.futures.ThreadPoolExecutor(max_workers=8).map(get,qs))},ensure_ascii=False))
PY
```

Monthly title fallback: fresh web correct long-year route skip250/show50 returned Cache miss; native same route200 restored monthly HTML but initial double-quote parser did not extract single-quoted titles. Subsequent exact parser fix is metadata-only, not AB or whole-month queue. Native200 and no parsed titles are not an empty archive claim.
