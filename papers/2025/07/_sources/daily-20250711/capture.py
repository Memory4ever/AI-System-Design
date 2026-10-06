import concurrent.futures, datetime, json, pathlib, urllib.request, urllib.parse, xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).parent
NS = {'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
TOPICS = {
 'model':'(all:"language model" OR all:LLM OR all:Transformer OR all:"mixture of experts")',
 'systems':'(all:"language model" OR all:GPU OR all:inference) AND (all:cache OR all:parallel OR all:kernel OR all:serving OR all:scheduling OR all:communication OR all:quantization)',
 'agents':'(all:"language model" OR all:LLM) AND (all:agent OR all:retrieval OR all:memory OR all:planning OR all:tool)',
 'multimodal':'all:"vision language" OR all:"multimodal model" OR all:"world model" OR all:"vision language action" OR all:"video generation" OR all:"diffusion model"',
}

def fetch(name,url,body=None):
    record={'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        req=urllib.request.Request(url,data=None if body is None else json.dumps(body).encode(),headers={'User-Agent':'AI-System-Design-research/1.0','Content-Type':'application/json'})
        if body is not None: record['body']=body
        with urllib.request.urlopen(req,timeout=30) as r:
            data=r.read(); record.update(status=r.status,final_url=r.url,bytes=len(data))
        (ROOT/(name+'.raw')).write_bytes(data)
        return data
    except Exception as e:
        record['error']=str(e)
        return b''
    finally:
        (ROOT/(name+'.request.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2))

def main():
    urls={k:'https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':'('+v+') AND submittedDate:[202507091800 TO 202507101800]','start':0,'max_results':200,'sortBy':'submittedDate','sortOrder':'ascending'}) for k,v in TOPICS.items()}
    data={}
    for key,url in urls.items():
        raw=fetch(key,url)
        if not raw: continue
        tree=ET.fromstring(raw)
        entries=[]
        for e in tree.findall('a:entry',NS):
            entries.append({tag:' '.join(e.findtext('a:'+tag,default='',namespaces=NS).split()) for tag in ['id','title','summary','published','updated']})
        data[key]={'total':tree.findtext('o:totalResults',namespaces=NS),'entries':entries}
    (ROOT/'discovery.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
    for key,v in data.items():
        print(key,v['total'])
        for e in v['entries']: print(e['id'].split('/')[-1],e['title'])

if __name__=='__main__': main()
