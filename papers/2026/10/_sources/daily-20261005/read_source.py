import sys, re, html, json, urllib.request, gzip

url = sys.argv[1]
try:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20) as r:
        data=r.read()
        if data[:2] == b'\x1f\x8b':
            data=gzip.decompress(data)
        raw = data.decode("utf-8", "replace")
        final = r.url
    def clean(t):
        t = re.sub(r"<script\b.*?</script>|<style\b.*?</style>", "", t, flags=re.S)
        return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", t))).strip()
    if '/list/' in url:
        entries = []
        for b in re.split(r'<dt>', raw)[1:]:
            aid = re.search(r'/abs/([^\"]+)', b)
            title = re.search(r"<div class=['\"]list-title mathjax['\"]>(.*?)</div>", b, re.S)
            ab = re.search(r"<p class=['\"]mathjax['\"]>(.*?)</p>", b, re.S)
            if aid and title:
                comment=re.search(r"<div class=['\"]list-comments mathjax['\"]>(.*?)</div>",b,re.S)
                entries.append({"id":aid[1], "title":clean(title[1]).removeprefix('Title: '), "abstract":clean(ab[1]) if ab else "", "comments":clean(comment[1]) if comment else ""})
        if len(sys.argv) > 2 and sys.argv[2] == 'titles':
            entries = [{"id":x['id'],"title":x['title']} for x in entries]
        elif len(sys.argv)>2 and sys.argv[2].startswith('route='):
            terms=sys.argv[2][6:]
            entries=[{"id":x['id'],"title":x['title']} for x in entries if re.search(terms,x['title'],re.I)]
        elif len(sys.argv) > 2 and sys.argv[2].startswith('ids='):
            requested=sys.argv[2][4:].split(',')
            entries=[x for x in entries if x['id'] in requested]
        elif len(sys.argv) > 2:
            entries = entries[int(sys.argv[2]):int(sys.argv[3])]
        print(json.dumps({"url":url,"final":final,"headers":clean(raw[:raw.find('<dt>')]),"entries":entries},ensure_ascii=False))
    else:
        body=clean(raw)
        if len(sys.argv)>2 and sys.argv[2].startswith('find='):
            pattern=sys.argv[2][5:]
            matches=[{"start":m.start(),"match":m.group(0),"context":body[max(0,m.start()-100):m.end()+180]} for m in re.finditer(pattern,body,re.I)][:40]
            print(json.dumps({"url":url,"final":final,"length":len(body),"matches":matches},ensure_ascii=False))
            sys.exit(0)
        start=int(sys.argv[2]) if len(sys.argv)>2 else 0
        end=int(sys.argv[3]) if len(sys.argv)>3 else 20000
        print(json.dumps({"url":url,"final":final,"length":len(body),"start":start,"end":min(end,len(body)),"text":body[start:end],"truncated":len(body)>end},ensure_ascii=False))
except Exception as e:
    print(json.dumps({"url":url,"error":str(e)},ensure_ascii=False))
