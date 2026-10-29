import concurrent.futures,datetime,html,json,pathlib,re,subprocess,urllib.request
ROOT=pathlib.Path('papers/2026/02/_sources/daily-20260223')
IDS=set(re.findall(r'^## (\d{4}\.\d+)',(ROOT/'supplement-selected-abstracts-20261008.md').read_text(),re.M))
IDS-=set('2602.19016 2602.18920 2602.18918 2603.06623'.split())
def run(cat):
 url=f'https://arxiv.org/list/{cat}/2026-02?show=2000';row={'category':cat,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Only date headings and already named identities; not a monthly screening queue.'}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25) as response:s=response.read().decode();row.update(status=response.status,bytes=len(s))
  headings=list(re.finditer(r'<h3[^>]*>(.*?)</h3>',s,re.S));row['headings']=[' '.join(html.unescape(re.sub('<[^>]*>',' ',m[1])).split()) for m in headings];row['matched']=[]
  for ident in sorted(IDS):
   m=re.search(r'(?:href=["\x27][^"\x27]*?/abs/'+re.escape(ident)+r'(?:v\d+)?["\x27])',s)
   if m:
    prior=[h for h in headings if h.start()<m.start()];h=prior[-1] if prior else None
    row['matched'].append({'id':ident,'heading': ' '.join(html.unescape(re.sub('<[^>]*>',' ',h[1])).split()) if h else None,'exact_date_html':h[0] if h else None,'exact_identity_html':m[0]})
 except Exception as e:row['error']=str(e)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(run,['cs.CL','cs.LG','cs.DC','cs.CV','cs.RO']))
s=json.dumps(rows,ensure_ascii=False,indent=2);subprocess.run(['apply_patch'],input='*** Begin Patch\n*** Add File: '+str(ROOT/'supplement-public-date-recovery-20261008.json')+'\n'+''.join('+'+x+'\n' for x in s.splitlines())+'*** End Patch\n',text=True,capture_output=True,check=True);print(s)
