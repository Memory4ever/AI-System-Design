import concurrent.futures, datetime, html, json, re, sys, urllib.request, xml.etree.ElementTree as ET

def read(url):
    result={'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        body=json.dumps({'pageNum':1,'pageSize':12,'renderType':0}).encode() if 'api.hunyuan.tencent.com' in url else None
        result['method']='POST' if body else 'GET'
        if body: result['request_body']=json.loads(body)
        req=urllib.request.Request(url,data=body,headers={'User-Agent':'Mozilla/5.0','Content-Type':'application/json','x-tt-locale':'US'})
        resp=urllib.request.urlopen(req,timeout=30)
        result['status']=resp.status
        raw=resp.read().decode('utf8','replace')
        if 'rss.xml' in url:
            items=ET.fromstring(raw).findall('./channel/item')
            result['data']={'total':len(items),'scope':'February metadata only, no article bodies','items':[{k:i.findtext(k) for k in ['title','link','pubDate']} for i in items if 'Feb 2026' in (i.findtext('pubDate') or '')]}
        elif 'api.datacite.org/' in url:
            a=json.loads(raw)['data']['attributes']
            result['data']={k:a.get(k) for k in ['doi','created','registered','titles','dates','url']}
        elif 'export.arxiv.org/api/' in url:
            root=ET.fromstring(raw);ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
            result['data']={'total':root.findtext('o:totalResults',namespaces=ns),'start':root.findtext('o:startIndex',namespaces=ns),'entries':[{'id':e.findtext('a:id',namespaces=ns),'title':e.findtext('a:title',namespaces=ns),'submitted':e.findtext('a:published',namespaces=ns),'updated':e.findtext('a:updated',namespaces=ns)} for e in root.findall('a:entry',ns)]}
        elif '/api/' in url:
            data=json.loads(raw)
            def project(x):
                if isinstance(x,list):return [project(v) for v in x]
                if not isinstance(x,dict):return x
                if 'qwen.ai' in url and 'title' in x:return {'id':x.get('id'),'title':x.get('title'),'date':x.get('extra',{}).get('date')}
                if 'hunyuan' in url and 'title' in x:return {k:x.get(k) for k in ['id','title','publicAt','publishedAt','displayPublishTime','renderType']}
                if 'ArticleMeta' in x:
                    m=x['ArticleMeta'];s=x.get('ArticleSubContentEn') or x.get('ArticleSubContentZh') or {}
                    return {'id':m.get('ID'),'Title':s.get('Title'),'PublishDate':m.get('PublishDate'),'ExternalLinkList':m.get('ExternalLinks')}
                return {k:project(v) for k,v in x.items() if k not in ['body','content','Body','Content','ArticleSubContentEn','ArticleSubContentZh']}
            result['data']=project(data)
        elif '/abs/' in url:
            parts=[]
            for pattern in [r'<h1[^>]*class="title[^\"]*"[^>]*>.*?</h1>',r'<blockquote[^>]*class="abstract[^\"]*"[^>]*>.*?</blockquote>',r'<div[^>]*class="submission-history"[^>]*>.*?</div>',r'<td[^>]*class="tablecell comments"[^>]*>.*?</td>']:
                m=re.search(pattern,raw,re.S)
                if m:parts.append(re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',m.group()))).strip())
            result['data']=parts
        else:
            raw=re.sub(r'<(?:script|style|nav|header|footer)\b[^>]*>.*?</(?:script|style|nav|header|footer)>','',raw,flags=re.S)
            txt=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',raw))).strip()
            result['data']={'date_slices':[txt[max(0,m.start()-150):m.end()+180] for m in re.finditer(r'(?:202[56][-/年]\d{1,2}[-/月]\d{1,2}|(?:February|Feb)\s+\d{1,2},?\s+2026)',txt)][:45], 'text_head':txt[:1400]}
    except Exception as e:result['error']=str(e)
    return result

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    print(json.dumps(list(pool.map(read,sys.argv[1:])),ensure_ascii=False))
