import json, urllib.request, urllib.parse, datetime
from pathlib import Path

results=[]
for kind in (1,2):
    token=''
    for page in range(3):
        params={'article_type':kind,'count':20,'order_desc':'false','publish_year':2026,'locale':'us'}
        if token: params['page_token']=token
        url='https://seed.bytedance.com/api/get_article_list_v2?'+urllib.parse.urlencode(params)
        try:
            with urllib.request.urlopen(url,timeout=25) as r: raw=r.read().decode()
            d=json.loads(raw); rows=d.get('sub_article_list',[])
            record={'type':kind,'page':page,'url':url,'raw':raw,'rows':rows,'has_more':d.get('has_more'),'next_page_token':d.get('next_page_token'),'total':d.get('total')}
            results.append(record)
            print('TYPE',kind,'PAGE',page,'total',record['total'],'has_more',record['has_more'],'next',record['next_page_token'])
            reached=False
            for x in rows:
                meta=x.get('ArticleMeta',{}); content=x.get('ArticleSubContentEn',{})
                pub=meta.get('PublishDate',0)
                date=datetime.datetime.fromtimestamp(pub/1000,datetime.timezone(datetime.timedelta(hours=8))).isoformat() if pub else None
                print(meta.get('ID'),content.get('Title'),date)
                if date and date[:10]>'2026-02-20': reached=True
            if reached or not record['has_more'] or not rows: break
            token=record['next_page_token']
        except Exception as e:
            results.append({'type':kind,'page':page,'url':url,'error':str(e)}); print(str(e)); break
Path(__file__).with_name('supplement-seed-native-20261008.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
