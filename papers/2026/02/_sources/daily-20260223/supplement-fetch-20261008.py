import concurrent.futures, datetime, hashlib, json, pathlib, subprocess, urllib.request, urllib.parse
ROOT = pathlib.Path('papers/2026/02/_sources/daily-20260223')
ENTRIES = {
 'OPENAI': 'https://openai.com/news/rss.xml',
 'ANTHROPIC': 'https://www.anthropic.com/research',
 'GOOGLE_BLOG': 'https://research.google/blog/?page=6',
 'GOOGLE_PUBS': 'https://research.google/pubs/',
 'GOOGLE_DM': 'https://deepmind.google/research/',
 'META': 'https://ai.meta.com/research/',
 'QWEN': 'https://qwen.ai/blog',
 'DEEPSEEK': 'https://www.deepseek.com/',
 'MOONSHOT': 'https://platform.kimi.com/blog',
 'HUNYUAN': 'https://hunyuan.tencent.com/research',
 'HUNYUAN_API': 'https://api.hunyuan.tencent.com/api/blog/publicList?pageNum=1&pageSize=100&renderType=0',
 'ZAI': 'https://www.zhipuai.cn/zh/research',
 'SEED_PAPERS': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2026&order_desc=false&page_token=0&count=100&locale=en-US',
 'SEED_BLOGS': 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2026&order_desc=false&page_token=0&count=100&locale=en-US',
 'ERNIE': 'https://ernie.baidu.com/blog/zh/',
 'MIMO': 'https://mimo.xiaomi.com/blog',
 'MINIMAX': 'https://www.minimax.io/blog',
 'ARXIV_SCHEDULE': 'https://info.arxiv.org/help/availability.html',
}
for name, term in {'language':'language model OR transformer OR mixture of experts','systems':'GPU OR inference OR distributed training','multimodal':'multimodal OR world model OR vision language action','agent':'language agent OR retrieval augmented OR tool calling'}.items():
 params={'advanced':'','terms-0-operator':'AND','terms-0-term':term,'terms-0-field':'all','classification-include_cross_list':'include','date-filter_by':'date_range','date-from_date':'2026-02-22','date-to_date':'2026-02-22','date-date_type':'announced_date','abstracts':'show','size':'50','order':'-announced_date_first'}
 ENTRIES['ARXIV_'+name]='https://arxiv.org/search/advanced?'+urllib.parse.urlencode(params)
def save(path, text):
 patch='*** Begin Patch\n*** Add File: '+str(path)+'\n'+''.join('+'+line+'\n' for line in text.splitlines())+'*** End Patch\n'
 subprocess.run(['apply_patch'],input=patch,text=True,check=True,capture_output=True)
def fetch(pair):
 name,url=pair; row={'name':name,'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=25) as response:
   raw=response.read(); value=raw.decode('utf-8','replace'); row.update(status=response.status,bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest(),final_url=response.url)
  save(ROOT/('supplement-'+name+'-20261008.raw'),value)
 except Exception as error: row['error']=str(error)
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
 rows=list(pool.map(fetch,ENTRIES.items()))
save(ROOT/'supplement-native-20261008.json',json.dumps(rows,ensure_ascii=False,indent=2))
print(json.dumps(rows,ensure_ascii=False,indent=2))
