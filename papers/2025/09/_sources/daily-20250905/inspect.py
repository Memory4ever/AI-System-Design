"""Read only actual captured title/abstract or numbered necessary paragraphs."""
from html.parser import HTMLParser
from pathlib import Path
import sys,xml.etree.ElementTree as E,re,gzip
BASE=Path(__file__).parent
class P(HTMLParser):
 def __init__(self):super().__init__();self.on=0;self.s='';self.a=[];self.head=[];self.skip=0;self.text=[];self.href=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
  if t in ['p','h1','h2','h3','h4']:self.on+=1
  if t=='a':self.href.extend(v for k,v in a if k=='href')
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip-=1
  if t in ['p','h1','h2','h3','h4'] and self.on:
   self.on-=1
   if not self.on:
    self.a.append(' '.join(self.s.split()));self.s=''
    if t!='p':self.head.append(len(self.a)-1)
 def handle_data(self,d):
  if not self.skip:
   if self.on:self.s+=d+' '
   if d.strip():self.text.append(d.strip())
def read(k):
 z=(BASE/(k+'.raw')).read_bytes();return (gzip.decompress(z) if z[:2]==b'\x1f\x8b' else z).decode()
if __name__=='__main__':
 for arg in sys.argv[1:]:
  k,*parts=arg.split(':');print(k)
  if k=='exact-v1':
   ns={'a':'http://www.w3.org/2005/Atom','x':'http://arxiv.org/schemas/atom'};a=E.fromstring(read(k)).findall('a:entry',ns);lo,hi=map(int,parts[0].split('-'))
   for i in range(lo,min(hi+1,len(a))):
    x=a[i];print(i,x.findtext('a:id',namespaces=ns),' '.join(x.findtext('a:title',namespaces=ns).split()),x.findtext('a:published',namespaces=ns));print(' '.join(x.findtext('a:summary',namespaces=ns).split()));print('COMMENTS',x.findtext('x:comment',namespaces=ns))
  else:
   p=P();p.feed(read(k))
   if not parts:
    for i in p.head:print(i,p.a[i])
   elif parts[0]=='text':print(' | '.join(p.text))
   elif parts[0]=='links':print('\n'.join(p.href))
   else:
    lo,hi=map(int,parts[0].split('-'))
    for i in range(lo,min(hi+1,len(p.a))):print(i,p.a[i])
