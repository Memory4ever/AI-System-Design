import concurrent.futures,datetime,json,pathlib,re,subprocess,urllib.request
ROOT=pathlib.Path('papers/2026/02/_sources/daily-20260223')
ids=set(re.findall(r'^## (\d{4}\.\d+)',(ROOT/'supplement-selected-abstracts-20261008.md').read_text(),re.M))-set('2602.19016 2602.18920 2602.18918 2603.06623'.split())
def save(path,s):subprocess.run(['apply_patch'],input='*** Begin Patch\n*** Add File: '+str(path)+'\n'+''.join('+'+x+'\n' for x in s.splitlines())+'*** End Patch\n',text=True,capture_output=True,check=True)
def run(pair):
 ident,url=pair;row={'identity':ident,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=20) as response:s=response.read().decode();row.update(status=response.status,bytes=len(s))
  save(ROOT/f'supplement-DATE_{ident}-20261008.raw',s);row['date_fields']=re.findall(r'.{0,100}(?:Submitted on|publishedOn|datePublished|citation_date|submission-history).{0,220}',s)[:8];row['signal_fields']=re.findall(r'.{0,100}(?:withdrawn|retracted|correction|erratum).{0,150}',s,re.I)[:4]
 except Exception as e:row['error']=str(e)
 return row
pairs=[(ident,'https://arxiv.org/abs/'+ident+'v1') for ident in sorted(ids)]
pairs.extend([('ROBO_AUTHOR','https://byungjunyoon.ai/publication/2026-02-21-robocurate'),('ROBO_PROJECT','https://seungkukim.github.io/robocurate/'),('MOBI_AUTHOR','https://a2jinhee.github.io/')])
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(run,pairs))
save(ROOT/'supplement-date-originals-20261008.json',json.dumps(rows,indent=2));print(json.dumps(rows,indent=2))
