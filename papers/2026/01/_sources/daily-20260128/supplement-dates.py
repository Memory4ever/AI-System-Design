"""Finite identity metadata recovery; metadata dates retain original meanings."""
import concurrent.futures, datetime, json, pathlib, re, urllib.parse, urllib.request
base=pathlib.Path(__file__).resolve().parent
ids=[re.search(r'abs-(\d+)-',p.name).group(1) for p in base.glob('supplement-abs-*-20261008.json')]
ids += ['16986','16987','17006','17037','17042','17050','17063','17082','17086','17087','19834','19895']
def one(number):
    url='https://api.datacite.org/dois/10.48550/arxiv.2601.'+number
    record={'id':'2601.'+number,'url':url,'checked':datetime.datetime.now().astimezone().isoformat()}
    try:
        with urllib.request.urlopen(url,timeout=35) as response: record['payload']=json.load(response)
    except Exception as exc: record['error']=str(exc)
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: records=list(pool.map(one,ids))
(base/'supplement-date-identities-20261008.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for record in records:
    a=record.get('payload',{}).get('data',{}).get('attributes',{})
    print(record['id'],a.get('created'),a.get('registered'),record.get('error',''),flush=True)
