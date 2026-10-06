import concurrent.futures, html, json, re, urllib.request
from pathlib import Path

ids=['2603.16877','2603.04436','2603.06610','2602.17743','2602.17744','2602.17734','2604.09567','2602.17737','2602.17738','2603.06608','2603.00113','2603.28778','2603.12274','2602.18511','2603.08727','2602.17753','2602.16687','2602.16698','2602.16704','2602.16699','2602.16708','2602.16710']
def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Historical research supplement'}),timeout=25) as r:
            return {'url':url,'status':r.status,'body':r.read().decode('utf-8',errors='replace')}
    except Exception as e:
        return {'url':url,'error':str(e)}
def fetch(identity):
    ab=get('https://arxiv.org/abs/'+identity+'v1')
    dc=get('https://api.datacite.org/dois/10.48550/arXiv.'+identity)
    body=ab.get('body','')
    title=re.search(r'<h1[^>]*class="title[^"]*"[^>]*>(.*?)</h1>',body,re.S)
    abstract=re.search(r'<blockquote[^>]*class="abstract[^"]*"[^>]*>(.*?)</blockquote>',body,re.S)
    clean=lambda s:html.unescape(re.sub('<[^>]+>',' ',s)).strip()
    out={'id':identity,'abs':ab,'datacite':dc,'title':clean(title.group(1)) if title else '', 'abstract':clean(abstract.group(1)) if abstract else ''}
    try:
        attrs=json.loads(dc.get('body','{}')).get('data',{}).get('attributes',{})
        out['registry']={k:attrs.get(k) for k in ['created','registered','published','updated','dates']}
    except Exception:
        pass
    return out
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    results=list(ex.map(fetch,ids))
Path(__file__).with_name('supplement-primary-identities-20261008.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
for r in results:
    print(r['id'],r['title'],r.get('registry',{}).get('registered'),r['abs'].get('error',''))
