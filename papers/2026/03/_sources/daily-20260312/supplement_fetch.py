import html
import json
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

def clean(value):
    return re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', ' ', value))).strip()

def fetch(identity):
    result = {'id':identity}
    for mode,url in [('abs','https://arxiv.org/abs/'+identity+'v1'),('current','https://arxiv.org/abs/'+identity),('doi','https://api.datacite.org/dois/10.48550/arxiv.'+identity)]:
        try:
            raw=urllib.request.urlopen(url,timeout=25).read().decode()
            if mode=='doi':
                d=json.loads(raw)['data']
                a=d['attributes']
                result['doi']={'identity':d['id'],'relationships':d.get('relationships'),**{k:a.get(k) for k in ['created','registered','state','url','dates','titles','publisher','relatedIdentifiers']}}
            else:
                match=re.search(r'<blockquote[^>]*class="abstract[^>]*>(.*?)</blockquote>',raw,re.S)
                title=re.search(r'<h1[^>]*class="title[^>]*>(.*?)</h1>',raw,re.S)
                start=raw.find('Submission history')
                history=clean(raw[start:raw.find('Full-text links:',start)]) if start>=0 else None
                comments=re.search(r'<td[^>]*class="tablecell comments[^>]*>(.*?)</td>',raw,re.S)
                result[mode]={'url':url,'title':clean(title.group(1)) if title else None,'abstract':clean(match.group(1)) if match else None,'comments':clean(comments.group(1)) if comments else None,'history':history,'withdrawn':bool(re.search('withdrawn|retracted',raw,re.I))}
                if mode=='current' and result['current'].get('abstract')==result.get('abs',{}).get('abstract'):
                    result['current'].pop('abstract')
                    result['current']['abstract_same_as_v1']=True
        except Exception as error:
            result[mode]={'url':url,'error':str(error)}
    return result

print(json.dumps(list(ThreadPoolExecutor(max_workers=6).map(fetch,sys.argv[1:])),ensure_ascii=False,indent=2))
