import concurrent.futures, datetime, json, sys, urllib.request, urllib.parse, xml.etree.ElementTree as ET, pathlib, re
old_ids=set()
for fname in ['V3_TITLE_ABSTRACT_SCREEN.md','V3_EXTRA_EXACT_ABSTRACTS.md','README.md']:
 p=pathlib.Path('papers/2026/02/_sources/daily-20260219')/fname
 if p.exists(): old_ids.update(re.findall(r'260[23]\.\d{5}',p.read_text()))
old_ids.update(re.findall(r'260[23]\.\d{5}',pathlib.Path('papers/2026/02/19/README.md').read_text()))
queries = {
 'learning': '(cat:cs.CL OR cat:cs.LG) AND (ti:pretraining OR ti:"pre-training" OR ti:representation OR ti:"feature learning" OR ti:generalization OR ti:quantization OR ti:attention OR ti:"test-time" OR ti:reasoning OR ti:"foundation model")',
 'system': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:Transformer OR all:"deep learning" OR all:LLM)',
 'multimodal': '(cat:cs.CV OR cat:cs.RO OR cat:cs.SD) AND (ti:"vision-language" OR ti:"world models" OR ti:"action model" OR ti:generative OR ti:codec OR ti:"video generation" OR ti:"flow matching")',
 'agent': '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:"tool use" OR ti:retrieval OR ti:planning OR ti:alignment OR ti:collusion OR ti:verification OR ti:benchmark) AND (all:"language model" OR all:LLM OR all:"foundation model")',
}
ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
def fetch(item):
 name,q=item; q='('+q+') AND submittedDate:[202602161900 TO 202602171900]'
 url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q,'start':0,'max_results':100,'sortBy':'submittedDate','sortOrder':'ascending'})
 try:
  with urllib.request.urlopen(url,timeout=30) as r: raw=r.read().decode()
  root=ET.fromstring(raw)
  rows=[{'id':e.findtext('a:id',namespaces=ns),'title':e.findtext('a:title',namespaces=ns),'abstract':e.findtext('a:summary',namespaces=ns),'submitted_not_public':e.findtext('a:published',namespaces=ns),'updated':e.findtext('a:updated',namespaces=ns)} for e in root.findall('a:entry',ns)]
  for row in rows:
   row['previous_identity_seen']=re.search(r'260[23]\.\d{5}',row['id']).group(0) in old_ids
   if row['previous_identity_seen']: row.pop('abstract')
  return {'name':name,'query':q,'url':url,'total':root.findtext('o:totalResults',namespaces=ns),'rows':rows}
 except Exception as exc: return {'name':name,'query':q,'url':url,'error':str(exc)}
print(json.dumps({'executed':datetime.datetime.now(datetime.timezone.utc).isoformat(),'window':'BJT 2026-02-18 natural day; Submitted range only discovery','queries':list(concurrent.futures.ThreadPoolExecutor(4).map(fetch,queries.items()))},ensure_ascii=False))
