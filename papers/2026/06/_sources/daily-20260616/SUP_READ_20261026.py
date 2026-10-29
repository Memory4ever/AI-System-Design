"""Render named saved HTML sections as plain text for bounded evidence reading."""
from html.parser import HTMLParser
from pathlib import Path
import sys

class Node:
    def __init__(self,tag,attrs):
        self.tag=tag;self.attrs=dict(attrs);self.children=[]
    def text(self):
        if self.tag in ('script','style','annotation','annotation-xml'):return ''
        prefix='\n' if self.tag in ('p','h1','h2','h3','h4','h5','section','tr','figure','table','li') else ''
        return prefix+''.join(x.text() if isinstance(x,Node) else x for x in self.children)
    def find(self,id):
        if self.attrs.get('id')==id:return self
        for child in self.children:
            if isinstance(child,Node):
                found=child.find(id)
                if found:return found
        return None

class Parser(HTMLParser):
    def __init__(self):
        super().__init__();self.root=Node('root',[]);self.stack=[self.root]
    def handle_starttag(self,tag,attrs):
        node=Node(tag,attrs);self.stack[-1].children.append(node)
        if tag not in ('area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'):
            self.stack.append(node)
    def handle_startendtag(self,tag,attrs):pass
    def handle_endtag(self,tag):
        for i in range(len(self.stack)-1,0,-1):
            if self.stack[i].tag==tag:self.stack=self.stack[:i];break
    def handle_data(self,data):self.stack[-1].children.append(data)

if __name__=='__main__':
    paper=sys.argv[1]
    parser=Parser();parser.feed((Path(__file__).parent/f'SUP_RAW_HTML_{paper}_20261026.raw').read_text())
    for id in sys.argv[2:]:
        node=parser.root.find(id)
        print('\n###',paper,id)
        print(node.text() if node else 'SECTION NOT FOUND')
