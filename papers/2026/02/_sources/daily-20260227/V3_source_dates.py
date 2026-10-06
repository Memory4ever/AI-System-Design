import pathlib,json,xml.etree.ElementTree as ET,re,datetime
root=pathlib.Path(__file__).resolve().parent
def show(name,rows):
    print('\n'+name,len(rows))
    for row in rows: print(json.dumps(row,ensure_ascii=False))
raw=(root/'V3_OPENAI.raw').read_text()
rows=[]
for item in ET.fromstring(raw).findall('.//item'):
    date=item.findtext('pubDate','')
    if any(s in date for s in ['26 Feb 2026','27 Feb 2026']): rows.append({'date':date,'title':item.findtext('title'),'url':item.findtext('link')})
show('OPENAI FEB',rows)
for name in ['V3_QWEN_API','V3_HUNYUAN_API','V3_SEED_API','V3_SEED_BLOG']:
    paths=list(root.glob(name+'*.raw'))
    if not paths:print(name,'missing');continue
    obj=json.loads(paths[0].read_text())
    print(name,'keys',list(obj))
    if name=='V3_QWEN_API':
        articles=obj.get('data',{}).get('articles',[])
        show(name,[{'title':x.get('title'),'extra':x.get('extra'),'url':x.get('url'),'id':x.get('id')} for x in articles if '2026-02' in str(x.get('extra'))])
    elif name=='V3_HUNYUAN_API':show(name,[{k:x.get(k) for k in ['id','title','publicAt','publishedAt','displayPublishTime']} for x in obj.get('data',{}).get('list',[])])
    else:
        rows=[]
        for x in obj.get('sub_article_list',[]):
            m=x.get('ArticleMeta',{});stamp=m.get('PublishDate',0)
            date=datetime.datetime.fromtimestamp(stamp/1000,datetime.timezone(datetime.timedelta(hours=8))).isoformat()
            if date.startswith('2026-02'):
                rows.append({'date':date,'title':x.get('ArticleSubContentEn',{}).get('Title'),'id':m.get('ArticleID'),'links':m.get('ExternalLinks')})
        show(name,rows)
