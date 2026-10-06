"""Untouched fresh-window primary responses; receipt time is not publication."""
import concurrent.futures,datetime,hashlib,json,pathlib,urllib.request,urllib.parse,sys
BASE=pathlib.Path(__file__).parent
URLS={
 'openai':'https://openai.com/news/rss.xml','anthropic':'https://www.anthropic.com/research',
 'google-pubs':'https://research.google/pubs/','deepmind':'https://deepmind.google/research/',
 'google-month':'https://research.google/blog/2025/09/','google-month2':'https://research.google/blog/2025/09/?page=2','deepmind-history':'https://deepmind.google/blog/page/5/',
 'meta':'https://ai.meta.com/research/','meta-blog':'https://ai.meta.com/blog/',
 'meta-results':'https://ai.meta.com/results/?content_types%5B0%5D=publication','meta-results5':'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=5','meta-results6':'https://ai.meta.com/results/?content_types%5B0%5D=publication&page=6',
 'meta-blog2':'https://ai.meta.com/blog/?page=2','meta-blog3':'https://ai.meta.com/blog/?page=3',
 'qwen':'https://qwen.ai/api/page_config?code=research.research-list','deepseek':'https://www.deepseek.com/','deepseek-updates':'https://api-docs.deepseek.com/updates',
 'moonshot':'https://platform.kimi.com/blog','hunyuan':'https://hunyuan.tencent.com/research','hunyuan-list':'https://api.hunyuan.tencent.com/api/blog/publicList',
 'zai':'https://www.zhipuai.cn/zh/research','zai2':'https://www.zhipuai.cn/zh/research?page=2','zai-release':'https://docs.z.ai/release-notes/new-released',
 'seed':'https://seed.bytedance.com/en/research','seed-blog':'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&page_token=0&count=20&order_desc=true',
 'ernie':'https://ernie.baidu.com/blog/zh/','ernie2':'https://ernie.baidu.com/blog/zh/page/2/',
 'mimo':'https://mimo.xiaomi.com/','mimo-index':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js','mimo-home':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js','mimo-component':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js',
 'minimax-en':'https://www.minimax.io/blog','minimax-cn':'https://www.minimaxi.com/blog','minimax-en2':'https://www.minimax.io/blog?page=2','minimax-agent':'https://agent.minimax.io/docs/techblog',
 'announce-cl':'https://arxiv.org/list/cs.CL/2025-09-05','announce-cv':'https://arxiv.org/list/cs.CV/2025-09-05',
}
THEMES={
 'model':'(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts") AND (all:architecture OR all:attention OR all:optimizer OR all:training)',
 'systems':'(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:"language model" OR all:GPU OR all:LLM) AND (all:inference OR all:communication OR all:kernel OR all:serving OR all:parallel)',
 'multimodal':'(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"foundation model" OR all:"world model" OR all:"vision language" OR all:"vision-language-action")',
 'agents':'(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:safety OR all:jailbreak)',
}
for k,q in THEMES.items():
 URLS['arxiv-'+k]='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':q+' AND submittedDate:[202509031800 TO 202509041800]','max_results':100,'sortBy':'submittedDate','sortOrder':'ascending'})
for token in [0,20,40,60,80]:URLS['seed-paper'+str(token)]='https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&page_token='+str(token)+'&count=20&order_desc=true'
EXACT='03581 03615 03626 03636 03646 03647 03658 03695 03696 03730 03733 03736 03740 03746 03764 03768 03787 03793 03800 03803 03805 03809 03817 03827 03828 03850 03867 03871 03887 03888 03890 03891 03893 03895 03903 03918 03934 03940 03956 03962 03972 03985 03990 03995 04011 04018 04027 04059 04063 04104 04139 04152 04154 04162 04183 04185 04198 04213 04243 04250 04292 04304 04310 04324 04334 04343 04373 04377 04403 04419 04439 04442 04448 04534 04537 04549 05359 05360 05362 05367 05378 06996 07996 09700 12221'.split()
URLS['exact-v1']='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':','.join('2509.'+p+'v1' for p in EXACT)+',2510.24719v1','max_results':len(EXACT)+1})
URLS['anthropic-biorisk']='https://www.anthropic.com/research/biorisk'
URLS['openai-opportunity']='https://openai.com/index/expanding-economic-opportunity-with-ai'
URLS['moonshot-0905']='https://platform.kimi.com/blog/posts/kimi-k2-0905'
URLS['current-metadata']='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':','.join('2509.'+p for p in EXACT)+',2510.24719','max_results':len(EXACT)+1})
for p in '03768 12221 05367 05362 03888 03647 03730 03736 03805 06996 04373 04198 03615 03828 04534 04537 03733 04154 04419 04027 04063 04549 03581 03646 03803 03626 03990 04304 04059 03867 05378 03934 04185'.split():URLS['core-'+p]='https://arxiv.org/html/2509.'+p+'v1'
URLS['core-itinerary']='https://arxiv.org/html/2510.24719v1'
for p in '04198 03828'.split():URLS['pdf-'+p]='https://arxiv.org/pdf/2509.'+p+'v1'
URLS['abs-06996']='https://arxiv.org/abs/2509.06996'
URLS['abs-04104-v1']='https://arxiv.org/abs/2509.04104v1'
URLS['abs-04104-v2']='https://arxiv.org/abs/2509.04104v2'
for p in '03658 04343'.split():URLS['core-'+p]='https://arxiv.org/html/2509.'+p+'v1'
for p in '03787 03985 04018 04250 04292 04403 09700'.split():URLS['core-'+p]='https://arxiv.org/html/2509.'+p+'v1'
URLS['announce-cl-month']='https://arxiv.org/list/cs.CL/2509?skip=0&show=2000'
URLS['announce-cv-month']='https://arxiv.org/list/cs.CV/2509?skip=0&show=2000'
for cat in ['CL','CV']:URLS['catchup-'+cat.lower()]='https://arxiv.org/catchup?'+urllib.parse.urlencode({'subject':'cs.'+cat,'date':'2025-09-05','include_abs':'True'})
URLS['exact-title-reopen-v1']='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':'2509.10526v1,2509.19305v1,2509.04169v1','max_results':3})
URLS['current-title-reopen']='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'id_list':'2509.10526,2509.19305,2509.04169','max_results':3})
for p in '10526 19305 04169'.split():URLS['core-'+p]='https://arxiv.org/html/2509.'+p+'v1'
def capture(item):
 k,u=item;r={'url':u,'checked':datetime.datetime.now(datetime.timezone.utc).isoformat(),'purpose':'Fresh 2025-09-05; current directory is not historical freeze'}
 try:
  h={'User-Agent':'Mozilla/5.0'};data=None
  if k=='hunyuan-list':data=json.dumps({'pageNum':1,'pageSize':100,'renderType':0}).encode();h['Content-Type']='application/json';r.update(method='POST',body=json.loads(data))
  with urllib.request.urlopen(urllib.request.Request(u,headers=h,data=data),timeout=35) as x:
   b=x.read();r.update(status=x.status,final_url=x.url,bytes=len(b),sha256=hashlib.sha256(b).hexdigest());(BASE/(k+'.raw')).write_bytes(b)
 except urllib.error.HTTPError as e:
  b=e.read();r.update(error=str(e),status=e.code,bytes=len(b),sha256=hashlib.sha256(b).hexdigest());(BASE/(k+'.raw')).write_bytes(b)
 except Exception as e:r['error']=str(e)
 (BASE/(k+'.request.json')).write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');return k,r.get('status'),r.get('bytes'),r.get('error')
if __name__=='__main__':
 selected=sys.argv[1:] or list(URLS)
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
  for result in ex.map(capture,[(k,URLS[k]) for k in selected]):print(result)
