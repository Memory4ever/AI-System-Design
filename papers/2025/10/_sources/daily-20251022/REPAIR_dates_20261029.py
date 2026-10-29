"""Recover exact DOI metadata for identities in this day's saved discovery."""
import json
import re
import urllib.parse
from html.parser import HTMLParser
import xml.etree.ElementTree as etree
from REPAIR_fetch_20261029 import ROOT, get

ids = set()
class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == 'a' and '/abs/' in values.get('href', ''):
            match = re.search(r'(\d{4}\.\d{4,5})', values['href'])
            if match:
                ids.add(match.group(1))

for name in ('arxiv_model_training.raw', 'arxiv_agent.raw', 'arxiv_multimodal.raw', 'arxiv_systems.raw', 'supplement.xml'):
    tree = etree.parse(str(ROOT / name))
    for entry in tree.findall('{http://www.w3.org/2005/Atom}entry'):
        value = entry.findtext('{http://www.w3.org/2005/Atom}id')
        ids.add(re.search(r'(\d{4}\.\d{4,5})', value).group(1))
for name in ('SUP_MODEL.html', 'SUP_MODEL_NARROW.html', 'SUP_AGENT.html', 'SUP_MULTIMODAL.html', 'SUP_SYSTEM.html', 'SUP_EVAL.html'):
    Links().feed((ROOT / name).read_text())
(ROOT/'REPAIR_OLD_IDENTITIES_20261029.json').write_text(json.dumps(sorted(ids), indent=2))
for i in range(0, len(ids), 25):
    batch = sorted(ids)[i:i+25]
    query = 'doi:('+' OR '.join('"10.48550/arxiv.'+key+'"' for key in batch)+')'
    url = 'https://api.datacite.org/dois?'+urllib.parse.urlencode({'query': query, 'page[size]':100})
    data = get(url, f'REPAIR_OLD_DATES_B{i//25+1}_20261029.json')
    print(i//25+1, len(batch), data.get('meta') if data else 'ERROR', flush=True)
