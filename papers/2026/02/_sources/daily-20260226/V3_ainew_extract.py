import pathlib, re, json, html, sys
from V3_fetch import TextParser

ROOT = pathlib.Path(__file__).resolve().parent
prefix = sys.argv[1] if len(sys.argv)>1 else 'V3_AINEW_ABS_'
output = sys.argv[2] if len(sys.argv)>2 else 'V3_AI_NEW_ABSTRACTS'
registered = {}
for path in ROOT.glob('V3_DATACITE_WINDOW*.raw'):
    for entry in json.loads(path.read_text())['data']:
        registered[entry['id'].split('arxiv.')[-1]] = entry['attributes']
rows = []
for path in sorted(ROOT.glob(prefix+'*.raw')):
    identity = path.stem.removeprefix(prefix)
    raw = path.read_text()
    parser = TextParser()
    match = re.search(r'<blockquote class="abstract[^\"]*"[^>]*>(.*?)</blockquote>', raw, re.S)
    parser.feed(match.group(1) if match else '')
    title = re.search(r'<meta name="citation_title" content="([^"]*)"', raw)
    metadata = registered.get(identity, {})
    if len(sys.argv)>3 and identity not in sys.argv[3].split(','):
        continue
    rows.append({'id': identity, 'title': html.unescape(title.group(1)) if title else '', 'abstract': re.sub(r'^Abstract:\s*', '', '\n'.join(parser.parts)).strip(), 'dates': metadata.get('dates'), 'registered': metadata.get('registered'), 'version': 'v1', 'source': path.name})
(ROOT / (output+'.json')).write_text(json.dumps(rows, ensure_ascii=False, indent=2))
packet = []
for row in rows:
    packet += ['## ' + row['id'] + ' ' + row['title'], '', '精确v1：https://arxiv.org/abs/' + row['id'] + 'v1；Registered=' + str(row['registered']) + '；原date字段=' + str(row['dates']), '', row['abstract'], '']
(ROOT / (output+'.md')).write_text('\n'.join(packet))
print(output+' bounded new full abstracts:', len(rows))
