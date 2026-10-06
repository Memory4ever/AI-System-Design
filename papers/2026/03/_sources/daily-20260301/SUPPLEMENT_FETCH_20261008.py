import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse
from html.parser import HTMLParser
class TextParser(HTMLParser):
 def __init__(self): super().__init__(); self.parts=[]; self.skip=0
 def handle_starttag(self,tag,attrs):
  if tag in ('script','style'): self.skip+=1
 def handle_endtag(self,tag):
  if tag in ('script','style') and self.skip: self.skip-=1
 def handle_data(self,data):
  if not self.skip and data.strip(): self.parts.append(data.strip())
BASE = pathlib.Path(__file__).parent
JOBS = {
 'OPENAI': 'https://openai.com/news/rss.xml',
 'ANTHROPIC': 'https://www.anthropic.com/research',
 'DEEPMIND': 'https://deepmind.google/research/',
 'GOOGLE_PUBS': 'https://research.google/pubs/?year=2026',
 'META': 'https://ai.meta.com/research/',
 'QWEN': 'https://qwen.ai/blog',
 'DEEPSEEK': 'https://www.deepseek.com/en/research',
 'KIMI': 'https://www.kimi.com/en/research',
 'HUNYUAN': 'https://hunyuan.tencent.com/research',
 'ZAI': 'https://www.zhipuai.cn/zh/research',
 'SEED': 'https://seed.bytedance.com/en/research',
 'SEED_PAPERS': 'https://seed.bytedance.com/en/public_papers',
 'ERNIE': 'https://ernie.baidu.com/blog/zh/',
 'MIMO': 'https://mimo.xiaomi.com/',
 'MINIMAX_EN': 'https://www.minimax.io/blog',
 'MINIMAX_CN': 'https://www.minimaxi.com/blog',
 'MINIMAX_AGENT': 'https://agent.minimax.io/docs/techblog',
 'ARXIV_SCHEDULE': 'https://info.arxiv.org/help/availability.html',
}
TOPICS = [
 '(cat:cs.CL OR cat:cs.LG OR cat:cs.AI) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"representation learning" OR all:"optimization theory")',
 '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:GPU OR all:"model training" OR all:inference)',
 '(cat:cs.CV OR cat:cs.RO) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:diffusion OR all:"flow matching")',
 '(cat:cs.IR OR cat:cs.MA OR cat:cs.AI) AND (all:"language model" OR all:RAG OR all:"agent memory" OR all:"tool calling")',
]
for i,q in enumerate(TOPICS):
 JOBS['ARXIV_TOPIC_'+str(i)] = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query': 'submittedDate:[202602280000 TO 202602282359] AND ('+q+')','start':0,'max_results':50,'sortBy':'submittedDate','sortOrder':'ascending'})
def fetch(item):
 name,url = item
 stamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 Research bounded historical check'})
  with urllib.request.urlopen(req,timeout=25) as r:
   raw=r.read(); status=r.status; final=r.url
  (BASE/('SUP_'+name+'.raw')).write_bytes(raw)
  parser=TextParser(); parser.feed(raw.decode('utf-8',errors='replace'))
  (BASE/('SUP_'+name+'.txt')).write_text('\n'.join(parser.parts))
  return {'name':name,'url':url,'checked_utc':stamp,'status':status,'final_url':final,'bytes':len(raw),'stop':'single response; no inferred pagination'}
 except Exception as e:
  return {'name':name,'url':url,'checked_utc':stamp,'error':str(e),'stop':'one failed request'}
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: results=list(pool.map(fetch,JOBS.items()))
 # Research page documented endpoint: page 1 only, actual returned inventory retained.
 name='HUNYUAN_PUBLICLIST'; url='https://api.hunyuan.tencent.com/api/blog/publicList'
 try:
  req=urllib.request.Request(url,data=json.dumps({'pageNum':1,'pageSize':1000,'renderType':0}).encode(),headers={'Content-Type':'application/json','User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=25) as r: raw=r.read(); status=r.status
  (BASE/('SUP_'+name+'.raw')).write_bytes(raw)
  (BASE/('SUP_'+name+'.txt')).write_text(raw.decode())
  results.append({'name':name,'url':url,'method':'POST','body':{'pageNum':1,'pageSize':1000,'renderType':0},'status':status,'bytes':len(raw),'checked_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'stop':'one page; total and language scope require inspection'})
 except Exception as e: results.append({'name':name,'url':url,'error':str(e)})
 (BASE/'SUP_FETCH_20261008.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
 print(json.dumps(results,ensure_ascii=False,indent=2))
