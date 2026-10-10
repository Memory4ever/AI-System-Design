import html, pathlib, re, sys
from html.parser import HTMLParser

class Text(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]; self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'): self.skip+=1
        if tag in ('p','h1','h2','h3','h4','div','tr','li','section'): self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
        if tag in ('p','tr','li'): self.parts.append('\n')
    def handle_data(self,text):
        if not self.skip: self.parts.append(text)

for name in sys.argv[1:]:
    p=pathlib.Path(__file__).parent/(name+'.raw')
    if not p.exists(): print(name,'MISSING'); continue
    parser=Text();parser.feed(p.read_text(errors='replace'))
    text=re.sub(r'[ \t]+',' ',''.join(parser.parts));text=re.sub(r'\n\s*\n','\n',text)
    (p.with_suffix('.txt')).write_text(text)
    print(name,len(text))
