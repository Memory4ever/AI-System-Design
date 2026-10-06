import concurrent.futures, datetime, html, json, re, sys, urllib.request, xml.etree.ElementTree as ET
html_sections = next((a.split('=',1)[1].split(',') for a in sys.argv if a.startswith('--sections=')), None)
html_offset = int(next((a.split('=',1)[1] for a in sys.argv if a.startswith('--offset=')), '0'))
outline_only = '--outline' in sys.argv
def read(url):
    try:
        request_headers = {'User-Agent':'AI-System-Design research'}
        if 'api.hunyuan.tencent.com/api/' in url:
            request_headers.update({'Content-Type':'application/json','Accept-Language':'zh'})
        req=urllib.request.Request(url,data=json.dumps({'pageNum':1,'pageSize':12,'renderType':0}).encode() if 'api.hunyuan.tencent.com/api/' in url else None,headers=request_headers)
        raw=urllib.request.urlopen(req,timeout=22).read().decode('utf-8','replace')
        if 'seed.bytedance.com/api/' in url:
            d=json.loads(raw)
            def seedproj(x):
                if isinstance(x,dict):
                    if 'ArticleMeta' in x:
                        m=x['ArticleMeta'];s=x.get('ArticleSubContentEn') or x.get('ArticleSubContentZh') or {}
                        return {'id':m.get('ID'),'Title':s.get('Title'),'PublishDate':m.get('PublishDate'),'ExternalLinkList':s.get('ExternalLinkList')}
                    if 'Title' in x:return {k:x.get(k) for k in ['Title','PublishDate','ExternalLinkList']}
                    return {k:seedproj(v) for k,v in x.items() if k not in ['Content','content','Body','body']}
                if isinstance(x,list):return [seedproj(v) for v in x]
                return x
            out=seedproj(d)
        elif 'api.datacite.org/' in url:
            d=json.loads(raw)['data']['attributes'];out={k:d.get(k) for k in ['doi','created','registered','updated','url','titles','dates']}
        elif 'api.hunyuan.tencent.com/api/' in url:
            d=json.loads(raw)
            def proj(x):
                if isinstance(x,dict):
                    if 'title' in x:return {k:x.get(k) for k in ['id','title','publicAt','publishedAt','displayPublishTime','renderType']}
                    return {k:proj(v) for k,v in x.items() if k not in ['body','content']}
                if isinstance(x,list):return [proj(v) for v in x]
                return x
            out=proj(d)
        elif 'qwen.ai/api' in url:
            data=json.loads(raw)
            def project(x):
                if isinstance(x,dict):
                    if 'title' in x:return {'title':x['title'],'date':x.get('extra',{}).get('date') if isinstance(x.get('extra'),dict) else x.get('extra')}
                    return {k:project(v) for k,v in x.items() if k not in ['body','content']}
                if isinstance(x,list):return [project(v) for v in x]
                return x
            out=project(data)
        elif '/abs/' in url:
            out='\n'.join(re.sub('<[^>]+>',' ',m.group()) for p in [r'<h1[^>]*class="title[^\"]*"[^>]*>.*?</h1>',r'<blockquote[^>]*class="abstract[^\"]*"[^>]*>.*?</blockquote>',r'<div[^>]*class="submission-history"[^>]*>.*?</div>',r'<td[^>]*class="tablecell comments"[^>]*>.*?</td>'] if (m:=re.search(p,raw,re.S)))
        elif '/html/' in url:
            sections=[]
            starts=list(re.finditer(r'<section\b(?=[^>]*class="ltx_section")([^>]+)>',raw))
            for i,m in enumerate(starts):
                block=raw[m.end():starts[i+1].start() if i+1<len(starts) else len(raw)]
                block=re.split(r'<(?:section|div)\b[^>]*class="ltx_(?:bibliography|appendix)',block)[0]
                block=re.sub(r'<(?:script|style|nav|header|footer)\b[^>]*>.*?</(?:script|style|nav|header|footer)>','',block,flags=re.S)
                txt=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',block))).strip()
                ident=re.search(r'id="([^\"]+)"',m.group(1))
                section_id = ident.group(1) if ident else ''
                if html_sections is not None and section_id not in html_sections:
                    continue
                sections.append({'section':section_id, 'chars':len(txt),'offset':html_offset,'text':txt[:180] if outline_only else txt[html_offset:html_offset+21000],'truncated':False if outline_only else len(txt)>html_offset+21000})
            out={'sections':sections,'scope':'main numbered sections only; reference/appendix excluded; individual >23kchar slice marked truncated'}
        elif 'export.arxiv.org' in url:
            root=ET.fromstring(raw);ns={'a':'http://www.w3.org/2005/Atom','o':'http://a9.com/-/spec/opensearch/1.1/'}
            out={'total':root.findtext('o:totalResults',namespaces=ns),'entries':[{'id':e.findtext('a:id',namespaces=ns),'title':e.findtext('a:title',namespaces=ns),'submitted':e.findtext('a:published',namespaces=ns),'updated':e.findtext('a:updated',namespaces=ns)} for e in root.findall('a:entry',ns)]}
        else:
            metadata=re.findall(r'<(?:meta|time)\b[^>]*(?:date|publish|datetime)[^>]*>',raw,re.I)
            anchors=[{'href':m.group(1),'text':re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',m.group(2)))).strip()} for m in re.finditer(r'<a\b[^>]*href=[\"\']([^\"\']+)[\"\'][^>]*>(.*?)</a>',raw,re.S)]
            text=re.sub(r'<(?:script|style|nav|header|footer)\b[^>]*>.*?</(?:script|style|nav|header|footer)>','',raw,flags=re.S)
            text=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',text))).strip()
            dated=[text[max(0,m.start()-180):m.end()+180] for m in re.finditer(r'(?:202[56][-/年]\d{1,2}[-/月]\d{1,2}|(?:February|Feb)\s+\d{1,2},?\s+2026)',text)][:65]
            out={'metadata':metadata[:30],'dated_text':dated,'anchors':anchors[:100], 'text_head':text[:1200],'bytes':len(raw)}
        return {'url':url,'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'data':out}
    except Exception as e:return {'url':url,'error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as p: print(json.dumps(list(p.map(read,[a for a in sys.argv[1:] if a.startswith('http')])),ensure_ascii=False,indent=2))
