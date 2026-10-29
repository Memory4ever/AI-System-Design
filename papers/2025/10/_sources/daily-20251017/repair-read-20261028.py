from html.parser import HTMLParser
import sys
import re

class Blocks(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack=[]; self.capture=None; self.parts=[]; self.depth=0
    def handle_starttag(self,tag,attrs):
        if tag in ('br','hr','img','input','meta','link','source','wbr'): return
        a=dict(attrs)
        if self.capture is not None: self.depth+=1
        elif tag in ('p','h1','h2','h3','h4','table','figcaption'):
            self.capture=(tag,a.get('id','')); self.parts=[]; self.depth=1
    def handle_endtag(self,tag):
        if self.capture is not None:
            self.depth-=1
            if self.depth<=0:
                if len(sys.argv)<3 or re.search(sys.argv[2],self.capture[1]+' '+self.capture[0]):
                    print(self.capture[0],self.capture[1], ' '.join(''.join(self.parts).split()))
                self.capture=None
    def handle_startendtag(self,tag,attrs): pass
    def handle_data(self,data):
        if self.capture is not None:self.parts.append(data)

parser=Blocks()
with open(sys.argv[1]) as f:parser.feed(f.read())
