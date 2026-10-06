import json,csv,pathlib,datetime
root=pathlib.Path(__file__).resolve().parent
admission={'2602.'+r['id']:r for r in csv.DictReader((root/'V3_ADMISSION.tsv').open(),delimiter='\t')}
data=json.loads((root/'V3_CURRENT_ABSTRACTS.json').read_text())
lines=['# 本窗日期有限恢复：当前同ID原字段','',
'官方规则原文：V3_ARXIV_SCHEDULE.raw/.txt，https://info.arxiv.org/help/availability.html。Monday14:00–Tuesday14:00 Eastern所收提交最早Tuesday20:00公告，延迟只会更晚；arXiv ID在公开公告流程中才分配，DOI不可预先生成。',
'严格晚于2026-02-23T19:00:00Z的Submitted，仅用于排除此前公告槽，不当作公开时刻。同ID DataCite Registered是精度上界：给定秒值s，采用小于s+1秒，而非Created/Updated。最早公开槽=2026-02-25T09:00:00+08:00；上界完全小于2026-02-26T09:00:00+08:00才确认落窗。官方2026节假日列表无该时段延迟；延期亦不破坏最早下界。',
'18个早Submitted身份不能从该下界链确认，保持日期终态保留、不入全文或Books队列。IN是潜在贡献，仍需独立准入/证据；这里不冻结候选分母。','',
'| ID | 准入停点 | Submitted原值（非公开） | Registered原值/上界 | 日期判断 |',
'| --- | --- | --- | --- | --- |']
out=[]
for r in data:
    submitted=next((v['date'] for v in r['dates'] if v['dateType']=='Submitted'),'')
    upper=datetime.datetime.fromisoformat(r['registered'].replace('Z','+00:00'))+datetime.timedelta(seconds=1)
    eligible=submitted>'2026-02-23T19:00:00Z' and upper<datetime.datetime(2026,2,26,1,tzinfo=datetime.timezone.utc)
    state='完整落窗区间' if eligible else '日期终态保留，不授当窗'
    lines.append(f"| {r['id']} | {admission[r['id']]['decision']} | {submitted} | {r['registered']} / <{upper.isoformat()} | {state} |")
    out.append({'id':r['id'],'submitted':submitted,'registered':r['registered'],'public_lower': '2026-02-25T09:00:00+08:00' if eligible else None,'public_upper_exclusive':upper.isoformat() if eligible else None,'eligible':eligible,'decision':admission[r['id']]['decision'],'source':r['raw_datacite_source']})
(root/'V3_DATE_PACKET.md').write_text('\n'.join(lines)+'\n')
(root/'V3_DATE_PACKET.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('eligible',sum(r['eligible'] for r in out),'held',sum(not r['eligible'] for r in out))
