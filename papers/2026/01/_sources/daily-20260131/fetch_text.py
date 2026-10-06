import sys,urllib.request,re,html,json
from html.parser import HTMLParser
class Text(HTMLParser):
 def __init__(self):super().__init__();self.out=[];self.skip=0
 def handle_starttag(self,t,a):
  if t in ("script","style"):self.skip+=1
  elif t in ("p","h1","h2","h3","h4","h5","h6","tr","div","table","section","li"):self.out.append("\n")
 def handle_endtag(self,t):
  if t in ("script","style"):self.skip=max(0,self.skip-1)
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
for u in sys.argv[1:]:
 try:
  r=urllib.request.urlopen(u,timeout=35);s=r.read().decode();t=Text();t.feed(s);print("URL "+u+"\n"+"\n".join(" ".join(x.split()) for x in "".join(t.out).splitlines() if x.strip()))
 except Exception as e:print("URL "+u+" ERROR "+str(e))
