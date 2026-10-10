import concurrent.futures, datetime, html, json, re, urllib.request
ids=['2602.15136','2602.15283','2602.15353','2602.15368','2602.15514','2602.15552','2602.15586','2602.15336','2602.15388','2603.12269','2602.15922','2602.15819','2603.08723','2602.15918','2602.15724','2603.13239']
def plain(x):return html.unescape(re.sub('<[^>]+>','',x)).strip()
def fetch(i):
 url='https://arxiv.org/abs/'+i+'v1'
 try:
  with urllib.request.urlopen(url,timeout=25) as r:raw=r.read().decode()
  title=re.search(r'<h1[^>]*class="title[^>]*>(.*?)</h1>',raw,re.S)
  abst=re.search(r'<blockquote[^>]*class="abstract[^>]*>(.*?)</blockquote>',raw,re.S)
  hist=re.search(r'<div class="submission-history">(.*?)</div>',raw,re.S)
  return {'id':i,'version':'v1','url':url,'title':plain(title.group(1)) if title else None,'abstract':plain(abst.group(1)) if abst else None,'submission_history_not_public_date':plain(hist.group(1)) if hist else None,'withdrawal_notice':'withdrawn' in raw.lower(),'links_in_abstract':re.findall(r'href="([^"]+)"',abst.group(1)) if abst else []}
 except Exception as exc:return {'id':i,'url':url,'error':str(exc)}
print(json.dumps({'executed':datetime.datetime.now(datetime.timezone.utc).isoformat(),'identities':list(concurrent.futures.ThreadPoolExecutor(8).map(fetch,ids))},ensure_ascii=False))
