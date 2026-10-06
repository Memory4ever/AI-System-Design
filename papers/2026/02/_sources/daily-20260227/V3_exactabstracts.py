import pathlib,json,re,csv,html,difflib
from html.parser import HTMLParser
class Meta(HTMLParser):
    def __init__(self):super().__init__();self.meta={}
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta' and a.get('name','').startswith('citation_'):self.meta[a['name']]=a.get('content','')
root=pathlib.Path(__file__).resolve().parent
old={r['arxiv_id']:r for r in json.loads((root/'inventory.json').read_text())['identities']}
rows=list(csv.DictReader((root/'V3_ADMISSION.tsv').open(),delimiter='\t'));records=[];delta=[]
for r in rows:
    id='2602.'+r['id'];p=root/('V3_ABS_'+id+'.raw')
    if not p.exists():continue
    m=Meta();m.feed(p.read_text());title=m.meta.get('citation_title','');abstract=m.meta.get('citation_abstract','')
    if not abstract:print('NO ABSTRACT',id);continue
    previous=old.get(id,{}).get('abstract','')
    norm=lambda s:re.sub(r'\s+',' ',html.unescape(s)).strip()
    changed=norm(abstract)!=norm(previous)
    records.append({**r,'id':id,'title':title,'abstract':abstract,'source':p.name,'changed_from_discovery':changed})
    if changed:delta.extend(['## '+id+' '+title,'', '发现版题摘与本窗v1有差异，只以下精确v1题摘决定最终准入，不做全修订diff。','',abstract,''])
(root/'V3_EXACT_ABSTRACTS.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
(root/'V3_ABSTRACT_CHANGED.md').write_text('\n'.join(delta)+'\n')
for i in range(0,len(records),25):
    selected=records[i:i+25];lines=['# 精确v1准入包 '+str(i//25+1),'']
    for r in selected:lines.extend(['## '+r['id']+' '+r['title'],'',r['abstract'],'', '作者准入：'+r['decision']+' — '+r['reason'],''])
    (root/('V3_EXACT_BATCH_'+str(i//25+1)+'.md')).write_text('\n'.join(lines)+'\n')
print('records',len(records),'changed',sum(r['changed_from_discovery'] for r in records))
print('\n'.join(r['id']+' '+r['title'] for r in records if r['changed_from_discovery']))
