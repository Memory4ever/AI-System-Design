import pathlib,sys,re,json
from html.parser import HTMLParser
class Blocks(HTMLParser):
    def __init__(self):super().__init__();self.depth=0;self.tag=None;self.parts=[];self.blocks=[]
    def handle_starttag(self,tag,attrs):
        if not self.tag and tag in ['h1','h2','h3','h4','h5','h6','p','table','figure']:
            self.tag=tag;self.depth=1;self.parts=[]
        elif self.tag and tag not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']:self.depth+=1
    def handle_startendtag(self,tag,attrs):pass
    def handle_endtag(self,tag):
        if self.tag:
            self.depth-=1
            if self.depth==0:
                text=re.sub(r'\s+',' ',' '.join(self.parts)).strip()
                if text:self.blocks.append((self.tag,text))
                self.tag=None
    def handle_data(self,data):
        if self.tag:self.parts.append(data)
root=pathlib.Path(__file__).resolve().parent
for id in sys.argv[1].split(','):
    path=root/('V3_CORE_2602.'+id+'.raw');p=Blocks();p.feed(path.read_text())
    out='\n\n'.join(f'[{i}] {tag}: {body}' for i,(tag,body) in enumerate(p.blocks))+'\n'
    (root/('V3_BLOCKS_2602.'+id+'.md')).write_text(out)
    print(id,len(p.blocks),len(out));print('\n'.join(f'[{i}] {body}' for i,(tag,body) in enumerate(p.blocks) if tag.startswith('h')))
