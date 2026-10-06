"""Print numbered necessary HTML paragraphs, not a read-full evidence claim."""
from html.parser import HTMLParser
from pathlib import Path
import sys
class P(HTMLParser):
 def __init__(self):super().__init__();self.on=0;self.s='';self.a=[];self.head=[]
 def handle_starttag(self,t,a):
  if t in ['p','h2','h3','h4']:self.on+=1
 def handle_endtag(self,t):
  if t in ['p','h2','h3','h4'] and self.on:
   self.on-=1
   if not self.on:
    self.a.append(' '.join(self.s.split()));self.s=''
    if t!='p':self.head.append(len(self.a)-1)
 def handle_data(self,d):
  if self.on:self.s+=d+' '
for name in sys.argv[1:]:
 k,*parts=name.split(':');p=P();p.feed((Path(__file__).parent/(k+'.raw')).read_text());print(k)
 if not parts:
  for i in p.head:print(i,p.a[i])
 else:
  lo,hi=map(int,parts[0].split('-'))
  for i in range(lo,min(hi+1,len(p.a))):print(i,p.a[i])
