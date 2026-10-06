import concurrent.futures,datetime,json,pathlib,subprocess,urllib.parse,urllib.request
ROOT=pathlib.Path('papers/2026/02/_sources/daily-20260223')
ENTRIES=[('HUNYUAN_POST','https://api.hunyuan.tencent.com/api/blog/publicList',{'pageNum':1,'pageSize':100,'renderType':0}),('META_BLOG2','https://ai.meta.com/blog/?page=2',None),('QWEN_OLD','https://qwenlm.github.io/',None),('MINIMAX_CN','https://www.minimaxi.com/blog',None),('DM_NEWS','https://deepmind.google/blog/?page=6',None)]
for name,term in [('language','language model OR transformer OR mixture of experts'),('systems','GPU OR inference OR distributed training'),('multimodal','multimodal OR world model OR vision language action'),('agent','language agent OR retrieval augmented OR tool calling')]:
 p={'advanced':'','terms-0-operator':'AND','terms-0-term':term,'terms-0-field':'all','classification-include_cross_list':'include','date-filter_by':'date_range','date-from_date':'2026-02-21','date-to_date':'2026-02-22','date-date_type':'submitted_date_first','abstracts':'show','size':'50','order':'-announced_date_first'}
 ENTRIES.append(('ARXIV_DISC_'+name,'https://arxiv.org/search/advanced?'+urllib.parse.urlencode(p),None))
def save(path,text):
 subprocess.run(['apply_patch'],input='*** Begin Patch\n*** Add File: '+str(path)+'\n'+''.join('+'+line+'\n' for line in text.splitlines())+'*** End Patch\n',text=True,check=True,capture_output=True)
def fetch(x):
 name,url,payload=x; row={'name':name,'url':url,'payload':payload,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  data=json.dumps(payload).encode() if payload else None
  req=urllib.request.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/json'})
  with urllib.request.urlopen(req,timeout=25) as response:raw=response.read();row.update(status=response.status,bytes=len(raw),final_url=response.url)
  save(ROOT/('supplement-'+name+'-20261008.raw'),raw.decode('utf-8','replace'))
 except Exception as error:row['error']=str(error)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool: rows=list(pool.map(fetch,ENTRIES))
save(ROOT/'supplement-native-recovery-20261008.json',json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
