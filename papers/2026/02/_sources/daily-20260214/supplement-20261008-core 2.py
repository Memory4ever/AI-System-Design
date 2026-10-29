import concurrent.futures, datetime, html, json, re, sys, urllib.request

def read(url):
    out={'url':url, 'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        response=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}), timeout=30)
        raw=response.read().decode('utf8','replace'); out['status']=response.status
        chunks=re.split(r'(?=<h2\b)',raw)
        sections=[]
        for chunk in chunks[1:]:
            heading=re.search(r'<h2\b[^>]*>(.*?)</h2>',chunk,re.S)
            if not heading: continue
            name=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',heading.group(1)))).strip()
            if re.search(r'references|appendix|supplementary material',name,re.I): break
            if re.search(r'acknowledg|instructions for reporting',name,re.I): continue
            clean=re.sub(r'<(?:script|style)\b[^>]*>.*?</(?:script|style)>','',chunk,flags=re.S)
            clean=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',clean))).strip()
            sections.append({'heading':name, 'chars':len(clean), 'text':clean})
        out['sections']=sections
        if not sections: out['text']=re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',raw))).strip()
    except Exception as exc: out['error']=str(exc)
    return out

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    print(json.dumps(list(pool.map(read,sys.argv[1:])),ensure_ascii=False))
