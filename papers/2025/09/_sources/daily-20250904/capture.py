"""Fresh-day untouched primary HTTP capture; receipt is actual execution, not publication."""
import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request,urllib.parse,sys
BASE=pathlib.Path(__file__).parent
URLS={
 'meta-results':'https://ai.meta.com/results/?content_types%5B0%5D=publication',
 'meta-results5':'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5',
 'meta-results6':'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=6',
 'meta-blog2':'https://ai.meta.com/blog/?page=2','meta-blog3':'https://ai.meta.com/blog/?page=3',
 'mimo-index':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js',
 'mimo-home':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js',
 'mimo-component':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js',
 'minimax-en2':'https://www.minimax.io/blog?page=2',
 'openai':'https://openai.com/news/rss.xml','anthropic':'https://www.anthropic.com/research',
 'google-pubs':'https://research.google/pubs/','deepmind':'https://deepmind.google/research/',
 'google-month':'https://research.google/blog/2025/09/','google-month2':'https://research.google/blog/2025/09/?page=2','deepmind-history':'https://deepmind.google/blog/page/5/',
 'meta':'https://ai.meta.com/research/','meta-blog':'https://ai.meta.com/blog/',
 'qwen':'https://qwen.ai/api/page_config?code=research.research-list',
 'deepseek':'https://www.deepseek.com/','deepseek-updates':'https://api-docs.deepseek.com/updates',
 'moonshot':'https://platform.kimi.com/blog','hunyuan':'https://hunyuan.tencent.com/research',
 'hunyuan-list':'https://api.hunyuan.tencent.com/api/blog/publicList',
 'zai':'https://www.zhipuai.cn/zh/research','zai2':'https://www.zhipuai.cn/zh/research?page=2','zai-release':'https://docs.z.ai/release-notes/new-released',
 'seed':'https://seed.bytedance.com/en/research',
 'seed-blog':'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true',
 'ernie':'https://ernie.baidu.com/blog/zh/','ernie2':'https://ernie.baidu.com/blog/zh/page/2/',
 'mimo':'https://mimo.xiaomi.com/','minimax-en':'https://www.minimax.io/blog','minimax-cn':'https://www.minimaxi.com/blog','minimax-agent':'https://agent.minimax.io/docs/techblog',
 'announce-cl':'https://arxiv.org/list/cs.CL?skip=0&show=2000&date=2025-09-04','announce-cv':'https://arxiv.org/list/cs.CV?skip=0&show=2000&date=2025-09-04',
}
THEMES={
}
URLS['exact-v1']='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list': '2509.02718v1,2509.02751v1,2509.02753v1,2509.02754v1,2509.02761v1,2509.02805v1,2509.02820v1,2509.02830v1,2509.02864v1,2509.02910v1,2509.02915v1,2509.02966v1,2509.02981v1,2509.03018v1,2509.03020v1,2509.03025v1,2509.03047v1,2509.03054v1,2509.03057v1,2509.03059v1,2509.03113v1,2509.03131v1,2509.03136v1,2509.03161v1,2509.03234v1,2509.03263v1,2509.03310v1,2509.03312v1,2509.03329v1,2509.03335v1,2509.03345v1,2509.03377v1,2509.03380v1,2509.03383v1,2509.03394v1,2509.03405v1,2509.03407v1,2509.03479v1,2509.03501v1,2509.03505v1,2509.03518v1,2509.04508v1,2509.04512v1,2509.04515v1,2509.04518v1,2509.06990v1,2509.06992v1,2509.06994v1,2509.10513v1,2509.10515v1,2509.10518v1,2510.01197v1', 'max_results': 52})
THEMES={
 'model':'(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts") AND (all:architecture OR all:attention OR all:optimizer OR all:training)',
 'systems':'(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel)',
 'multimodal':'(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action")',
 'agents':'(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak)',
}
for k,q in THEMES.items():
 URLS['arxiv-'+k]='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q+' AND submittedDate:[202509021800 TO 202509031800]','max_results':100,'sortBy':'submittedDate','sortOrder':'ascending'})
for token in [0,20,40,60,80]:URLS['seed-paper'+str(token)]='https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token='+str(token)+'&count=20&order_desc=true'
for pid in '02718 02981 02820 03383 03518 03380 03047 02910 03329 03310 10518 03054 03263 03377 03113 04515 03505'.split():URLS['core-'+pid]='https://arxiv.org/html/2509.'+pid+'v1'
URLS['fix-03054']='https://arxiv.org/html/2509.03054v3'
URLS['core-02915']='https://arxiv.org/html/2509.02915v1'
for pid in '03380 02910 04515'.split():URLS['pdf-'+pid]='https://arxiv.org/pdf/2509.'+pid+'v1'
def capture(item):
 k,u=item;r={'url':u,'checked':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Fresh 2025-09-04 independent window capture; current directories are not historical freeze'}
 try:
  h={'User-Agent':'Mozilla/5.0'};data=None
  if k=='hunyuan-list':data=json.dumps({'pageNum':1,'pageSize':100,'renderType':0}).encode();h['Content-Type']='application/json';r.update(method='POST',body=json.loads(data))
  with urllib.request.urlopen(urllib.request.Request(u,headers=h,data=data),timeout=35) as x:
   b=x.read();r.update(status=x.status,final_url=x.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest());(BASE/(k+'.raw')).write_bytes(b)
 except Exception as e:r['error']=str(e)
 (BASE/(k+'.request.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');return k,r.get('status'),r.get('bytes'),r.get('error')
if __name__=='__main__':
 selected=sys.argv[1:] or list(URLS)
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for result in ex.map(capture,[(k,URLS[k]) for k in selected]):print(result)
