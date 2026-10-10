import json
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

groups = {
    'model_training': '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:Transformer OR ti:MoE OR ti:"reinforcement learning" OR ti:"post-training")',
    'system': '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:LLM OR all:"language model" OR all:GPU) AND (all:inference OR all:training OR all:kernel OR all:cache OR all:communication)',
    'multimodal': '(cat:cs.CV OR cat:cs.RO) AND (ti:"world model" OR ti:"vision language" OR ti:"vision-language" OR ti:"video generation" OR ti:"diffusion model" OR ti:VLA)',
    'agent_retrieval': '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (ti:agent OR ti:RAG OR ti:memory OR ti:retrieval) AND (all:"language model" OR all:LLM)',
}
ns = {'a': 'http://www.w3.org/2005/Atom', 'ar': 'http://arxiv.org/schemas/atom', 'o': 'http://a9.com/-/spec/opensearch/1.1/'}
query_start = int(sys.argv[1]) if len(sys.argv)>1 else 0
query_interval = sys.argv[2] if len(sys.argv)>2 else '202603100000 TO 202603102359'

def fetch(pair):
    name, query = pair
    query += ' AND submittedDate:[' + query_interval + ']'
    url = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':query, 'start':query_start, 'max_results':30, 'sortBy':'submittedDate', 'sortOrder':'descending'})
    result = {'group':name, 'url':url, 'query':query, 'start':query_start, 'max_results':30}
    try:
        raw=urllib.request.urlopen(url,timeout=35).read().decode()
        doc=ET.fromstring(raw)
        result['total']=doc.findtext('o:totalResults',namespaces=ns)
        result['entries']=[]
        for e in doc.findall('a:entry',ns):
            result['entries'].append({k:e.findtext(v,namespaces=ns) for k,v in {'id':'a:id','title':'a:title','summary':'a:summary','submitted':'a:published','updated':'a:updated','comment':'ar:comment'}.items()})
    except Exception as error:
        result['error']=str(error)
    return result

print(json.dumps(list(ThreadPoolExecutor(max_workers=4).map(fetch,groups.items())),ensure_ascii=False,indent=2))
