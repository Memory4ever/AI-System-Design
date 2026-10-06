import pathlib,json,datetime
from html.parser import HTMLParser
class Meta(HTMLParser):
    def __init__(self):super().__init__();self.meta={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta' and a.get('name','').startswith('citation_'):self.meta[a['name']]=a.get('content','')
root=pathlib.Path(__file__).resolve().parent
rows=[];lines=['# 主题查漏具名精确v1题摘','', '宽目录只用来发现这些具体名字；不把剩余全目录转队列。完整题摘独立决定贡献。','']
for p in sorted(root.glob('V3_DATE_2602.*.raw')):
    id=p.stem.split('_')[-1];a=json.loads(p.read_text())['data']['attributes']
    ap=root/('V3_ABS_'+id+'.raw');m=Meta();m.feed(ap.read_text())
    date=next((x['date'] for x in a['dates'] if x['dateType']=='Submitted' and x.get('dateInformation')=='v1'),'')
    upper=datetime.datetime.fromisoformat(a['registered'].replace('Z','+00:00'))+datetime.timedelta(seconds=1)
    eligible=date>'2026-02-24T19:00:00Z' and upper<datetime.datetime(2026,2,27,1,tzinfo=datetime.timezone.utc)
    row={'id':id,'title':m.meta.get('citation_title'),'abstract':m.meta.get('citation_abstract'),'submitted':date,'registered':a['registered'],'upper_exclusive':upper.isoformat(),'eligible':eligible,'source':p.name}
    rows.append(row);lines.extend(['## '+id+' '+str(row['title']),'',str(row['abstract']),'',f'Submitted(v1)={date}; Registered={a["registered"]}; 日期 '+('完整落窗' if eligible else '未授当窗'),''])
(root/'V3_NAMED_TAIL.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(root/'V3_NAMED_TAIL.md').write_text('\n'.join(lines)+'\n')
print('records',len(rows),'eligible',sum(x['eligible'] for x in rows))
