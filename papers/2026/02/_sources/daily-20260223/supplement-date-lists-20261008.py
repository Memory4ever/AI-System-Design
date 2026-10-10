import concurrent.futures,datetime,json,pathlib,re,subprocess,urllib.request
ROOT=pathlib.Path('papers/2026/02/_sources/daily-20260223')
def save(path,text):subprocess.run(['apply_patch'],input='*** Begin Patch\n*** Add File: '+str(path)+'\n'+''.join('+'+x+'\n' for x in text.splitlines())+'*** End Patch\n',text=True,capture_output=True,check=True)
def run(cat):
 url=f'https://arxiv.org/list/{cat}/2602?show=2000';row={'category':cat,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:s=response.read().decode();row.update(status=response.status,bytes=len(s))
  save(ROOT/f'supplement-LIST_{cat}-20261008.raw',s);row['headings']=re.findall(r'<h3>(.*?)</h3>',s,re.S)
 except Exception as e:row['error']=str(e)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(run,['cs.CL','cs.LG','cs.DC','cs.CV','cs.RO']))
save(ROOT/'supplement-date-lists-20261008.json',json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
