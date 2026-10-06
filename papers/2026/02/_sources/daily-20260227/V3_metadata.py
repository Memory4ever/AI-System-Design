import json,pathlib,datetime,re
root=pathlib.Path(__file__).resolve().parent
records={}
for path in sorted(root.glob('V3_THEME_QUERY_*.raw')):
    obj=json.loads(path.read_text());print(path.name,obj['meta'],len(obj['data']))
    for row in obj['data']:
        a=row['attributes'];identity=a['doi'].split('.')[-1];records[identity]={**a,'raw_source':path.name}
known=json.loads((root/'inventory.json').read_text())['identities']
names=list(dict.fromkeys(re.findall(r'^## 2602\.(\d+)',(root/'V3_THEME_ABSTRACTS.md').read_text()+'\n'+(root/'V3_EXTRA_ABSTRACTS.md').read_text(),re.M)))
lines=['# 当前同ID日期字段','', 'Registered只作上界；Updated/Created不用于公开归属。Submitted严格晚于2026-02-24T19:00:00Z排除此前公告槽；availability允许最早公开2026-02-26T09:00+08。上界完全小于02-27 09:00才可确认落窗。早提交需sameID官方公告，不从邻居/Updated推定。','', '| ID | Submitted v1 | Registered | 日期 |','| --- | --- | --- | --- |']
out=[]
for identity in names:
    a=records.get(identity)
    if not a:print('MISSING',identity);continue
    submitted=next((d['date'] for d in a['dates'] if d['dateType']=='Submitted' and d.get('dateInformation')=='v1'),'')
    registered=a.get('registered','');upper=datetime.datetime.fromisoformat(registered.replace('Z','+00:00'))+datetime.timedelta(seconds=1)
    eligible=submitted>'2026-02-24T19:00:00Z' and upper<datetime.datetime(2026,2,27,1,tzinfo=datetime.timezone.utc)
    lines.append(f'| 2602.{identity} | {submitted} | {registered} | '+('完整落窗区间' if eligible else '需官方公告，未授当窗')+' |')
    out.append({'id':'2602.'+identity,'submitted':submitted,'registered':registered,'eligible':eligible,'upper_exclusive':upper.isoformat(),'title':a['titles'][0]['title'],'abstract':next((d['description'] for d in a.get('descriptions',[]) if d['descriptionType']=='Abstract'),''),'source':a['raw_source']})
(root/'V3_DATE_PACKET.md').write_text('\n'.join(lines)+'\n');(root/'V3_CURRENT_METADATA.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('eligible',sum(x['eligible'] for x in out),'hold',sum(not x['eligible'] for x in out))
