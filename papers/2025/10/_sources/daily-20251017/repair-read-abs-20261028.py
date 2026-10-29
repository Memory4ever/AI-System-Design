from html.parser import HTMLParser
from pathlib import Path
import sys
class Meta(HTMLParser):
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='meta' and a.get('name') in ('citation_title','citation_abstract'):print(a['name'],a.get('content'))
p=Path(__file__).parent
for identity in sys.argv[1:]:
    print('\nID',identity)
    raw=(p/f'REPAIR_ABS_2510.{identity}_20261028.html').read_text()
    Meta().feed(raw)
    if 'withdrawn' in raw.lower():print('WITHDRAWAL WORD PRESENT: inspect original')
