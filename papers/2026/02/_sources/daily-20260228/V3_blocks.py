import pathlib,sys,re
from html.parser import HTMLParser
class Blocks(HTMLParser):
    def __init__(self): super().__init__(); self.depth=0; self.tag=None; self.parts=[]; self.blocks=[]
    def handle_starttag(self,tag,attrs):
        if not self.tag and tag in ['h1','h2','h3','h4','h5','h6','p','table','figure']:
            self.tag=tag; self.depth=1; self.parts=[]
        elif self.tag and tag not in ['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']: self.depth+=1
    def handle_startendtag(self,tag,attrs): pass
    def handle_endtag(self,tag):
        if self.tag:
            self.depth-=1
            if self.depth==0:
                body=re.sub(r'\s+',' ',' '.join(self.parts)).strip()
                if body: self.blocks.append((self.tag,body))
                self.tag=None
    def handle_data(self,data):
        if self.tag:self.parts.append(data)
ROOT=pathlib.Path(__file__).resolve().parent
for identity in sys.argv[1].split(','):
    path=ROOT/('V3_CORE_2602.'+identity+'.raw'); p=Blocks(); p.feed(path.read_text())
    output='\n\n'.join(f'[{i}] {tag}: {body}' for i,(tag,body) in enumerate(p.blocks))+'\n'
    (ROOT/('V3_BLOCKS_2602.'+identity+'.md')).write_text(output)
    print(identity,len(p.blocks),len(output))
    print('\n'.join(f'[{i}] {body}' for i,(tag,body) in enumerate(p.blocks) if tag.startswith('h')))
