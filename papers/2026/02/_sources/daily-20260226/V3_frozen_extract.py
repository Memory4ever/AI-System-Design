import pathlib,json,csv,datetime
ROOT=pathlib.Path(__file__).resolve().parent
original=list(csv.DictReader((ROOT/'V3_ADMISSION.tsv').open(),delimiter='\t'))
dates={x['id'].split('.')[-1]:x for x in json.loads((ROOT/'V3_DATE_PACKET.json').read_text())}
print('original fields',list(original[0]))
extra={
 'LG': {'20370','20396','20418','20419','20467','20549','20567','20593','20629','20758','20804','20921','20971','21020'},
 'AI': {'20517','20624'},
 'CROSS': {'20294','20450','20585','20646','20650','20652','20731','20967','20981','21039','21078','21092','21160'},
}
rows=[]
for x in original:
 key=x[list(x)[0]]
 if x[list(x)[1]]=='IN' and dates[key]['eligible']:
  rows.append({'id':'2602.'+key,'origin':'original156','date':dates[key]})
lower=datetime.datetime.fromisoformat('2026-02-25T01:00:00+00:00')
upper=datetime.datetime.fromisoformat('2026-02-26T01:00:00+00:00')
cutoff=datetime.datetime.fromisoformat('2026-02-23T19:00:00+00:00')
for kind,ids in extra.items():
 data=json.loads((ROOT/('V3_'+{'LG':'LG','AI':'AI','CROSS':'CROSS'}[kind]+'_NEW_ABSTRACTS.json')).read_text())
 for x in data:
  if x['id'].split('.')[-1] not in ids:continue
  submitted=next(d['date'] for d in x['dates'] if d['dateType']=='Submitted' and d.get('dateInformation')=='v1')
  registered=datetime.datetime.fromisoformat(x['registered'].replace('Z','+00:00'))
  sub=datetime.datetime.fromisoformat(submitted.replace('Z','+00:00'))
  bound=registered+datetime.timedelta(seconds=1)
  assert cutoff<sub<datetime.datetime.fromisoformat('2026-02-24T19:00:00+00:00')
  assert lower<bound<=upper
  rows.append({'id':x['id'],'title':x['title'],'origin':kind,'date':{'submitted_v1':submitted,'registered':x['registered'],'public_lower':lower.isoformat(),'public_upper_exclusive':bound.isoformat(),'eligible':True}})
assert len(rows)==148 and len({x['id'] for x in rows})==148
(ROOT/'V3_FROZEN_CANDIDATES.json').write_text(json.dumps(sorted(rows,key=lambda x:x['id']),ensure_ascii=False,indent=2))
print('finite frozen candidates',len(rows),'original',sum(x['origin']=='original156' for x in rows))
