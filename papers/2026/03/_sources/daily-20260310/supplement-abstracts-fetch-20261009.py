import urllib.request, json, concurrent.futures, sys, re, html
from pathlib import Path
ids = json.loads(Path(__file__).with_name('supplement-selected-20261009.json').read_text())
start, end = map(int, sys.argv[1:3])
def run(i):
    out = {'id':i,'version':'v1','url':'https://arxiv.org/abs/'+i+'v1'}
    try:
        h = urllib.request.urlopen(out['url'],timeout=25).read().decode()
        def clean(s): return ' '.join(html.unescape(re.sub('<[^>]+>',' ',s)).split())
        out['title'] = clean(re.search(r'<h1 class="title[^>]*>(.*?)</h1>',h,re.S).group(1))
        out['abstract'] = clean(re.search(r'<blockquote class="abstract[^>]*>(.*?)</blockquote>',h,re.S).group(1))
        out['history'] = clean(re.search(r'<div class="submission-history[^>]*>(.*?)</div>',h,re.S).group(1))
        out['comments'] = [clean(s) for s in re.findall(r'<tr>(.*?)</tr>',h,re.S) if 'Comments:' in s]
        d = json.load(urllib.request.urlopen('https://api.datacite.org/dois/10.48550/arXiv.'+i,timeout=25))['data']
        a=d['attributes'];out['datacite']={k:a.get(k) for k in ['created','registered','state','dates']};out['client']=d.get('relationships',{}).get('client',{})
    except Exception as e:out['error']=str(e)
    return out
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as p:
    print(json.dumps(list(p.map(run,ids[start:end])),ensure_ascii=False))
