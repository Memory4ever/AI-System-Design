import json, pathlib, re
ROOT=pathlib.Path(__file__).resolve().parent
IDS='''22213 22214 22217 22221 22224 22225 22227 22240 22242 22246 22253 22254 22255 22258 22259 22261 22265 22268 22271 22278 22284 22286 22287 22291 22296 22302 22345 22351 22359 22394 22402 22406 22413 22416 22419 22424 22425 22426 22427 22434 22437 22441 22445 22450 22452 22453 22455 22457 22461 22465 22469 22474 22475 22479 22480 22486 22495 22505 22508 22510 22514 22518 22519 22523 22525 22538 22543 22546 22547 22554 22556 22557 22562 22570 22575 22576 22579 22581 22583 22584 22585 22586 22591 22592 22593 22594 22595 22596 22600 22601 22603 22610 22617 22623 22624 22629 22631 22638 22642 22644 22647 22654 22661 22663 22675 22678 22680 22681 22683 22689 22697 22698 22700 22703 22710 22716 22718 22719 22724 22727 22733 22734 22742 22745 22751 22752 22755 22756 22758 22760 22764 22765 22766 22769 22775 22779 22785 22787 22790 22801 22805 22808 22812 22814 22817 22818 22831 22839 22862 22868 22871 22896 22917 22918 22932 22936 22942 22948 22953 22958 22960 22963 22968 22983 22988 23005 23008 23024 23029 23036 23047 23050 23057 23058 23065 23068 23079 23111 23116 23128 23136 23148 23152 23153 23161 23163 23164 23166 23184 23193 23197 23200 23201 23205 23219 23220 23225 23228 23229 23232 23235 23239 23242 23248 23253 23258 23259 23266 23271 23280 23286 23294 23306 23312 23320 23331 23333 23334 23336 23341 23342 23349 23351 23353 23358 23359 23360 23361'''.split()
inventory={r['arxiv_id']:r for r in json.loads((ROOT/'inventory.json').read_text())['identities']}
metadata={}
for path in sorted(ROOT.glob('V3_THEME_*.raw')):
    obj=json.loads(path.read_text())
    for row in obj['data']:
        a=row['attributes']; metadata[a['doi'].split('arxiv.')[-1]]={**a,'raw_source':path.name}
records=[]
for n in IDS:
    identity='2602.'+n; old=inventory.get(identity,{})
    a=metadata.get(identity,{})
    submitted=next((d['date'] for d in a.get('dates',[]) if d['dateType']=='Submitted' and d.get('dateInformation')=='v1'),'')
    records.append({'id':identity,'title':old.get('title',a.get('titles',[{}])[0].get('title','')),'abstract_v1':old.get('abstract',''),'submitted':submitted,'registered':a.get('registered',''),'metadata_source':a.get('raw_source',''),'categories':old.get('categories',[])})
(ROOT/'V3_THEME_METADATA.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
for i in range(0,len(records),18):
    batch=records[i:i+18]
    lines=['# 发现题摘线索 '+str(i//18+1),'','旧inventory只复用title+abstract作为发现与准入线索，不复用旧准入、日期或分数，也不保证题摘属于精确v1。新sameIDmetadata在V3_THEME_METADATA.json；abstract_v1是旧字段名，不授版本证据。拟采用的机制、题名及事件须由本轮精确原abs/正文核对，具体版本信号仅定点处理。','']
    for r in batch: lines.extend(['## '+r['id']+' '+r['title'], '',r['abstract_v1'],''])
    (ROOT/('V3_ABSTRACTS_'+str(i//18+1)+'.md')).write_text('\n'.join(lines)+'\n')
print('named title-and-abstract slice',len(records),'metadata missing',sum(not r['metadata_source'] for r in records))
