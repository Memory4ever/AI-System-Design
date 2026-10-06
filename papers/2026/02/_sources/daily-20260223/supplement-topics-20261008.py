import concurrent.futures,datetime,json,pathlib,subprocess,urllib.parse,urllib.request
ROOT=pathlib.Path('papers/2026/02/_sources/daily-20260223')
GROUPS={'MODEL':['language model','transformer','mixture of experts'],'SYSTEM':['LLM inference','GPU kernel','distributed training'],'MULTIMODAL':['multimodal','world model','vision language action'],'AGENT':['language agent','retrieval augmented','tool calling']}
def run(pair):
 name,terms=pair;p={'advanced':'','classification-include_cross_list':'include','date-filter_by':'date_range','date-from_date':'2026-02-21','date-to_date':'2026-02-22','date-date_type':'submitted_date_first','abstracts':'show','size':'50','order':'-announced_date_first'}
 for n,term in enumerate(terms):p.update({f'terms-{n}-operator':'AND' if n==0 else 'OR',f'terms-{n}-term':term,f'terms-{n}-field':'abstract'})
 url='https://arxiv.org/search/advanced?'+urllib.parse.urlencode(p);row={'name':name,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:s=response.read().decode();row.update(status=response.status,bytes=len(s))
  path=ROOT/f'supplement-TOPIC_{name}-20261008.raw';patch='*** Begin Patch\n*** Add File: '+str(path)+'\n'+''.join('+'+x+'\n' for x in s.splitlines())+'*** End Patch\n';subprocess.run(['apply_patch'],input=patch,text=True,capture_output=True,check=True)
 except Exception as e:row['error']=str(e)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(run,GROUPS.items()))
s=json.dumps(rows,indent=2);subprocess.run(['apply_patch'],input='*** Begin Patch\n*** Add File: '+str(ROOT/'supplement-topic-requests-20261008.json')+'\n'+''.join('+'+x+'\n' for x in s.splitlines())+'*** End Patch\n',text=True,capture_output=True,check=True);print(s)
