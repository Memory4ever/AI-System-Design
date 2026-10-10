import urllib.request, re, html, json, concurrent.futures, sys
def clean(s):
    s = re.sub(r'<script\b.*?</script>|<style\b.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<annotation[^>]*encoding="application/x-tex"[^>]*>(.*?)</annotation>', lambda m: ' '+html.unescape(m.group(1))+' ', s, flags=re.S)
    return ' '.join(html.unescape(re.sub('<[^>]+>', ' ', s)).split())
def run(i):
    u='https://arxiv.org/html/'+i+'v1'
    try:
        h=urllib.request.urlopen(u,timeout=25).read().decode()
        hs=list(re.finditer(r'<h[1-6]\b[^>]*>(.*?)</h[1-6]>',h,re.S))
        out=[]
        for j,m in enumerate(hs):
            end=hs[j+1].start() if j+1<len(hs) else len(h)
            title=clean(m.group(1));text=clean(h[m.end():end])
            out.append({'heading':title,'text':text})
        if sys.argv[1]=='outline':return {'id':i,'url':u,'headings':[(j,s['heading'],len(s['text'])) for j,s in enumerate(out)]}
        chosen=list(map(int,sys.argv[2].split(',')))
        return {'id':i,'url':u,'sections':[out[j] for j in chosen]}
    except Exception as e:return {'id':i,'url':u,'error':str(e)}
ids=sys.argv[2:] if sys.argv[1]=='outline' else sys.argv[3:]
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as p:print(json.dumps(list(p.map(run,ids)),ensure_ascii=False))
