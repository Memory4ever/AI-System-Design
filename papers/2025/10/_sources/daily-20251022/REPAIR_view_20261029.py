"""Read named saved sections, displaying each formula once and preserving tails."""
import sys
from pathlib import Path
from lxml import etree, html

path=Path(__file__).parent/sys.argv[1]
doc=html.fromstring(path.read_bytes())
for node in doc.xpath('//*[local-name()="math"]'):
    replacement=etree.Element('span')
    replacement.text=' '+(node.get('alttext') or node.text_content())+' '
    replacement.tail=node.tail
    node.getparent().replace(node,replacement)
if len(sys.argv)==2:
    print('AB', ' '.join(' '.join(doc.xpath('//*[contains(@class,"ltx_abstract")]//text()')).split()))
    for node in doc.xpath('//h2|//h3'):
        print(node.getparent().get('id'), ' '.join(node.text_content().split()))
else:
    for key in sys.argv[2:]:
        print(key,' '.join(doc.get_element_by_id(key).text_content().split()))
