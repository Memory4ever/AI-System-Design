"""Read selected HTML prose/table blocks, suppressing duplicate MathML annotations."""
import pathlib,sys
from html.parser import HTMLParser
class Blocks(HTMLParser):
 def __init__(self): super().__init__();self.blocks=[];self.current=[];self.depth=0;self.hidden=0
 def handle_starttag(self,tag,attrs):
  attrs=dict(attrs)
  if tag in ['annotation','script','style']: self.hidden+=1
  if self.depth:self.depth+=1
  elif tag in ['h2','h3','h4'] or (tag=='p' and 'ltx_p' in attrs.get('class','')) or (tag=='table' and 'ltx_tabular' in attrs.get('class','')):
   self.depth=1;self.current=[]
 def handle_endtag(self,tag):
  if tag in ['annotation','script','style']:self.hidden=max(0,self.hidden-1)
  if self.depth:
   self.depth-=1
   if not self.depth:
    t=' '.join(' '.join(self.current).split())
    if t:self.blocks.append(t)
 def handle_data(self,data):
  if self.depth and not self.hidden:self.current.append(data)
for ident in sys.argv[1].split(','):
 print('PAPER',ident)
 p=pathlib.Path(__file__).parent/'supplement-20261007'/('html'+ident+'.raw');parser=Blocks();parser.feed(p.read_text())
 lower=int(sys.argv[2]) if len(sys.argv)>2 else 0;upper=int(sys.argv[3]) if len(sys.argv)>3 else len(parser.blocks)
 for i in range(lower,min(upper,len(parser.blocks))):print(i,parser.blocks[i])
