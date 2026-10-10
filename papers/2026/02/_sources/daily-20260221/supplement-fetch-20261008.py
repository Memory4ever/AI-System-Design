import concurrent.futures, json, urllib.request, urllib.parse, xml.etree.ElementTree as ET
from pathlib import Path

base = 'https://export.arxiv.org/api/query?'
topics = {
    'language': '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:Transformer OR all:"mixture of experts")',
    'agent': '(cat:cs.AI OR cat:cs.MA OR cat:cs.IR) AND (all:"language model" OR all:agent OR all:"retrieval augmented")',
    'multimodal': '(cat:cs.CV OR cat:cs.RO) AND (all:"foundation model" OR all:"vision language" OR all:diffusion OR all:"world model" OR all:VLA)',
    'system': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:GPU OR all:LLM OR all:"language model" OR all:Transformer)',
}
urls = {k: base + urllib.parse.urlencode({'search_query': v + ' AND submittedDate:[202602181900 TO 202602191900]', 'start': 0, 'max_results': 200, 'sortBy': 'submittedDate', 'sortOrder': 'ascending'}) for k,v in topics.items()}
urls['hunyuan'] = 'https://api.hunyuan.tencent.com/api/blog/publicList'
urls['qwen'] = 'https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US'
urls['listCL'] = 'https://arxiv.org/list/cs.CL/2602?show=2000'
def fetch(item):
    key,url = item
    try:
        payload=json.dumps({'pageNum':1,'pageSize':20,'renderType':0}).encode() if key=='hunyuan' else None
        req=urllib.request.Request(url,data=payload,headers={'User-Agent':'AI-System-Design historical research supplement','Content-Type':'application/json'})
        with urllib.request.urlopen(req, timeout=25) as r:
            raw=r.read().decode('utf-8',errors='replace')
            out={'name':key,'url':url,'status':r.status,'raw':raw}
        if key in topics:
            ns={'a':'http://www.w3.org/2005/Atom'}
            root=ET.fromstring(raw)
            out['totalResults']=root.findtext('{http://a9.com/-/spec/opensearch/1.1/}totalResults')
            out['entries']=[{f:e.findtext('a:'+f,default='',namespaces=ns) for f in ('id','title','summary','published','updated')} for e in root.findall('a:entry',ns)]
        return out
    except Exception as e:
        return {'name':key,'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    results=list(ex.map(fetch,urls.items()))
Path(__file__).with_name('supplement-native-narrow-20261008.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
old=json.loads(Path(__file__).with_name('inventory.json').read_text())
known={e['arxiv_id'] for e in old['identities']}
for r in results:
    print(r['name'],r.get('totalResults'),r.get('error'),len(r.get('entries',[])))
    if r['name'] in ('hunyuan','qwen'):
        print(r.get('raw','')[:24000])
    for e in r.get('entries',[]):
        identity=e['id'].rsplit('/',1)[-1].split('v')[0]
        if identity not in known:
            print(identity,e['published'],e['title'].replace('\n',' '))
