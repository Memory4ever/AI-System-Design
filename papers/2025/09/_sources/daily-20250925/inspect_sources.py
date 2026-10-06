"""Expose bounded identities and complete discovered abstracts; no semantic filtering."""
import datetime
import json
import pathlib
import re
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = pathlib.Path(__file__).resolve().parent
start = datetime.datetime.fromisoformat('2025-09-24T01:00:00+00:00')
stop = datetime.datetime.fromisoformat('2025-09-25T01:00:00+00:00')
qwen = json.loads((ROOT/'qwen-config.raw').read_text())
selected = [item for item in qwen if start <= datetime.datetime.fromisoformat(item['date'].replace('Z','+00:00')) < stop]
(ROOT/'qwen-window.json').write_text(json.dumps({'objects':len(qwen),'selected':selected},ensure_ascii=False,indent=2))
rss = ET.fromstring((ROOT/'openai-rss.raw').read_bytes())
rss_window = []
for item in rss.findall('./channel/item'):
    date = item.findtext('pubDate')
    if date and start <= parsedate_to_datetime(date) < stop:
        rss_window.append({k:item.findtext(k) for k in ['title','pubDate','link','description']})
(ROOT/'openai-window.json').write_text(json.dumps(rss_window,ensure_ascii=False,indent=2))
raw = (ROOT/'anthropic.raw').read_text().replace('\\"','"')
dates = re.findall(r'"publishedOn":"([^"]+)"',raw)
anthropic_window = [d for d in dates if start <= datetime.datetime.fromisoformat(d.replace('Z','+00:00')) < stop]
(ROOT/'anthropic-window.json').write_text(json.dumps({'date_fields':len(dates),'unique_dates':len(set(dates)),'window':anthropic_window},indent=2))
unique = {}
totals = {}
for name in ['model','systems','agents','multimodal']:
    file = ROOT / ('arxiv-'+name+'-entries.json')
    data = json.loads(file.read_text())
    totals[file.stem] = {'total':data['total'],'returned':len(data['entries'])}
    for entry in data['entries']:
        unique[entry['id']] = entry
(ROOT/'arxiv-discovery.json').write_text(json.dumps({'queries':totals,'entries':list(unique.values())},ensure_ascii=False,indent=2))
(ROOT/'arxiv-title-index.txt').write_text('\n'.join(f"{i+1}. {entry['id']} | {entry['title']} | submitted-published={entry['published']}" for i,entry in enumerate(unique.values())))
print(json.dumps({'qwen_objects':len(qwen),'qwen_window':[(i['id'],i['date'],i.get('htmlLink'),i.get('tokenLinks')) for i in selected],'openai_window':rss_window,'anthropic':anthropic_window,'arxiv':totals,'unique':len(unique)},ensure_ascii=False))
original = json.loads((ROOT/'arxiv-query-entries.json').read_text())
related = json.loads((ROOT/'arxiv-related-selection.json').read_text())
excludes = json.loads((ROOT/'arxiv-title-scope-excludes.json').read_text())
(ROOT/'original-related-index.txt').write_text('\n'.join(f"{i+1}. {entry['id']} | {entry['title']}" for i,entry in enumerate(related)))
(ROOT/'original-related-abstracts.txt').write_text('\n\n'.join(f"{i+1}. {entry['id']} | {entry['title']}\n{entry['summary']}" for i,entry in enumerate(related)))
print(json.dumps({'original_total':len(original),'related':len(related),'title_scope_excludes':len(excludes)}))
