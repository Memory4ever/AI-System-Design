"""Read numbered text blocks from existing primary HTML, without editing it."""
from html.parser import HTMLParser
from pathlib import Path
import re, sys

class Blocks(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip=0; self.parts=[]
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style'): self.skip += 1
        if tag in ('p','h1','h2','h3','h4','h5','li','tr','div','section','figure'): self.parts.append('\n')
        if tag=='math': self.parts.append(' ')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip -= 1
        if tag in ('p','h1','h2','h3','h4','h5','li','tr','figure'): self.parts.append('\n')
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)

p=Blocks(); p.feed(Path(sys.argv[1]).read_text())
rows=[re.sub(r'\s+', ' ', x).strip() for x in ''.join(p.parts).split('\n')]
rows=[x for x in rows if x]
if len(sys.argv)>2 and sys.argv[2]=='headings':
    for i,x in enumerate(rows,1):
        if re.match(r'^(\d[\d. ]{0,8}[A-Za-z]|Appendix|Limitations|Abstract|References)',x) and len(x)<180: print(i,x)
else:
    lo=int(sys.argv[2]) if len(sys.argv)>2 else 1
    hi=int(sys.argv[3]) if len(sys.argv)>3 else len(rows)
    for i,x in enumerate(rows,1):
        if lo<=i<=hi: print(i,x)
