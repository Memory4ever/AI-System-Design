"""Date-scoped discovery only; DataCite registration is not public-release proof."""
import concurrent.futures,datetime,json,pathlib,urllib.parse,urllib.request
GROUPS={
'model':'titles.title:("language model" OR LLM OR transformer OR MoE OR pretraining OR "reinforcement learning" OR distillation OR tokenizer OR attention)',
'multi':'titles.title:("foundation model" OR multimodal OR "world model" OR "vision-language" OR VLA OR diffusion OR "video generation")',
'agent':'titles.title:(agent OR reasoning OR memory OR RAG OR retrieval OR "tool calling" OR benchmark)',
'system':'titles.title:(inference OR GPU OR kernel OR compiler OR quantization OR scheduling OR distributed OR "tensor parallel" OR "KV cache" OR speculative)'}
def fetch(pair):
 name,terms=pair
 query='prefix:10.48550 AND subjects.subject:"Computer and information sciences" AND registered:[2026-01-27T01:00:00Z TO 2026-01-28T02:59:59Z] AND '+terms
 url='https://api.datacite.org/dois?'+urllib.parse.urlencode({'query':query,'page[size]':100,'fields[dois]':'doi,titles,subjects,dates,descriptions,url,created,registered'})
 try:
  with urllib.request.urlopen(url,timeout=40) as response: payload=json.load(response)
  pages=[{'url':url,'payload':payload}]
  for page in range(2,payload.get('meta',{}).get('totalPages',1)+1):
   pageurl=url+'&page[number]='+str(page)
   with urllib.request.urlopen(pageurl,timeout=40) as response: other=json.load(response)
   pages.append({'url':pageurl,'payload':other})
  return {'group':name,'url':url,'checked':datetime.datetime.now().astimezone().isoformat(),'pages':pages,'payload':{'meta':payload.get('meta',{}),'data':[x for pg in pages for x in pg['payload'].get('data',[])]}}
 except Exception as exc:return {'group':name,'url':url,'error':str(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: results=list(pool.map(fetch,GROUPS.items()))
pathlib.Path(__file__).with_name('scope.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
for group in results:
 print(group['group'],group.get('payload',{}).get('meta',{}),group.get('error',''))
 for item in group.get('payload',{}).get('data',[]): print(item['id'],item['attributes']['titles'][0]['title'])
