import urllib.request, urllib.parse, xml.etree.ElementTree as E, json, concurrent.futures
queries = {
    'systems': '(cat:cs.CL OR cat:cs.LG OR cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"large language model" OR all:"distributed training" OR all:"speculative decoding" OR all:"kernel" OR all:"inference")',
    'learning': '(cat:cs.CL OR cat:cs.LG) AND (all:"Transformer" OR all:"mixture of experts" OR all:"language model") AND (all:"optimization" OR all:"scaling" OR all:"representation" OR all:"attention")',
    'multimodal': '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL) AND (all:"world model" OR all:"vision language action" OR all:"video generation" OR all:"multimodal foundation")',
    'agent': '(cat:cs.AI OR cat:cs.MA OR cat:cs.IR OR cat:cs.CL) AND (all:"language model" OR all:"LLM") AND (all:"agent" OR all:"retrieval" OR all:"evaluation")',
}
def run(item):
    k, v = item
    q = 'submittedDate:[202603051900 TO 202603061900] AND ' + v
    u = 'https://export.arxiv.org/api/query?' + urllib.parse.urlencode({'search_query':q,'start':0,'max_results':200,'sortBy':'submittedDate','sortOrder':'ascending'})
    x = E.fromstring(urllib.request.urlopen(u, timeout=30).read())
    n = {'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
    rows = [{'id':e.findtext('a:id',namespaces=n).split('/abs/')[-1], 'title':' '.join(e.findtext('a:title',namespaces=n).split())} for e in x.findall('a:entry',n)]
    return {'theme':k,'url':u,'query':q,'total':x.findtext('o:totalResults',namespaces=n),'rows':rows}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    out = list(pool.map(run, queries.items()))
print(json.dumps(out, ensure_ascii=False))
