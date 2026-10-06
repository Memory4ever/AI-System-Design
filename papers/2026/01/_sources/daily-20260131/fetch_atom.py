import sys, urllib.request, urllib.parse, xml.etree.ElementTree as E, json
q=sys.argv[1]
start=int(sys.argv[2]) if len(sys.argv)>2 else 0
n=int(sys.argv[3]) if len(sys.argv)>3 else 100
u="https://export.arxiv.org/api/query?"+urllib.parse.urlencode(dict(search_query=q,start=start,max_results=n,sortBy="submittedDate",sortOrder="descending"))
try:
 r=urllib.request.urlopen(u,timeout=40); raw=r.read().decode()
 root=E.fromstring(raw); ns={"a":"http://www.w3.org/2005/Atom","o":"http://a9.com/-/spec/opensearch/1.1/","x":"http://arxiv.org/schemas/atom"}
 entries=[dict(id=z.findtext("a:id",namespaces=ns),title=" ".join(z.findtext("a:title",namespaces=ns).split()),abstract=" ".join(z.findtext("a:summary",namespaces=ns).split()),published=z.findtext("a:published",namespaces=ns),updated=z.findtext("a:updated",namespaces=ns),comment=z.findtext("x:comment",namespaces=ns),categories=[x.attrib["term"] for x in z.findall("a:category",ns)]) for z in root.findall("a:entry",ns)]
 if len(sys.argv)>4 and sys.argv[4]=="titles": entries=[{k:v for k,v in z.items() if k!="abstract"} for z in entries]
 print(json.dumps(dict(url=u,total=root.findtext("o:totalResults",namespaces=ns),start=start,entries=entries),ensure_ascii=False,indent=2))
except Exception as e: print(json.dumps(dict(url=u,error=str(e))))
