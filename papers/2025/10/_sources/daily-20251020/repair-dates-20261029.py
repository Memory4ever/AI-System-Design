import json
import pathlib
import subprocess
import urllib.parse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent
NS = {'a': 'http://www.w3.org/2005/Atom'}
identities = set()
for name in ['focus_agent.xml', 'focus_model_training.xml', 'focus_multimodal.xml',
             'supplement.xml', 'arxiv_systems.raw']:
    for entry in ET.parse(ROOT / name).findall('a:entry', NS):
        identities.add(entry.findtext('a:id', namespaces=NS).rsplit('/', 1)[-1].split('v')[0])

class Links(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        href = dict(attrs).get('href', '')
        if href.startswith('https://arxiv.org/abs/'):
            identities.add(href.rsplit('/', 1)[-1].split('v')[0])

for name in ['MODEL', 'MODEL_S25', 'MODEL_S50', 'TRAIN', 'AGENT', 'MULTIMODAL', 'RUNTIME']:
    Links().feed((ROOT / f'SUP_ARXIV_{name}_20261015.raw').read_text())

ids = sorted(identities)
manifest = []
for start in range(0, len(ids), 50):
    batch = ids[start:start+50]
    query = 'doi:(' + ' OR '.join('"10.48550/arxiv.' + i + '"' for i in batch) + ')'
    url = 'https://api.datacite.org/dois?' + urllib.parse.urlencode({'query':query, 'page[size]':100})
    name = f'REPAIR_DC_EXACT_{start//50+1}_20261029.json'
    subprocess.run(['curl', '-fLsS', '--max-time', '45', url, '-o', str(ROOT / name)], check=True)
    data = json.loads((ROOT / name).read_text())
    record = {'url':url, 'file':name, 'requested':batch, 'total':data['meta']['total'], 'count':len(data['data']), 'next':data['links'].get('next')}
    manifest.append(record)
    (ROOT/'REPAIR_DC_EXACT_FETCH_20261029.json').write_text(json.dumps(manifest, indent=2))
    print(json.dumps(record), flush=True)
