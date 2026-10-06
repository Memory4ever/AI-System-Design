import sys,json,urllib.request,concurrent.futures,re,html
def clean(v): return ' '.join(html.unescape(re.sub(r'<[^>]*>',' ',v)).split())
def pick(raw,p):
 m=re.search(p,raw,re.S); return clean(m.group(1)) if m else None
def one(i):
 u="https://arxiv.org/abs/"+i+"v1"
 try:
  raw=urllib.request.urlopen(u,timeout=30).read().decode()
  title=pick(raw,r'<h1[^>]*class="title[^\"]*"[^>]*>(.*?)</h1>'); abstract=pick(raw,r'<blockquote[^>]*class="abstract[^\"]*"[^>]*>(.*?)</blockquote>'); history=pick(raw,r'<div[^>]*class="submission-history"[^>]*>(.*?)</div>'); comments=pick(raw,r'<div[^>]*class="metatable"[^>]*>(.*?)</div>')
  scoped=' '.join(x for x in (title,abstract,history,comments) if x)
  return dict(id=i,requested=u,title=title,abstract=abstract,history=history,comments=comments,signals=[x for x in ("withdrawn","retracted","erratum","corrected","correction") if x in scoped.lower()])
 except Exception as e: return dict(id=i,requested=u,error=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
 for r in ex.map(one,sys.argv[1:]):print(json.dumps(r,ensure_ascii=False))
