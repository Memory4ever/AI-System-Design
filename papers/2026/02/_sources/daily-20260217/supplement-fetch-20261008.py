import concurrent.futures
import json
import zlib
import base64
import urllib.request
import re
import xml.etree.ElementTree as ET
from html import unescape
from urllib.parse import urlencode
from datetime import datetime, timezone
from pathlib import Path

previous_topic_ids = set(re.findall(r'^## (\d{4}\.\d{5})', Path('papers/2026/02/_sources/daily-20260217/V3_TOPIC_ABSTRACTS.md').read_text(), re.M))

queries = [
    '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:Transformer OR all:MoE)',
    '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:GPU OR all:"model inference")',
    '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:agent OR all:RAG OR all:"tool calling")',
    '(cat:cs.CV OR cat:cs.RO) AND (all:"world model" OR all:"vision-language" OR all:"multimodal foundation" OR all:"diffusion model")',
]
entries = []
for query in queries:
    entries.append(('topic', 'https://export.arxiv.org/api/query?' + urlencode({'search_query': 'submittedDate:[202602130000 TO 202602132359] AND (' + query + ')', 'start': 0, 'max_results': 100, 'sortBy': 'submittedDate', 'sortOrder': 'descending'})))

def fetch(entry):
    role, url = entry
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Research-audit'})
        with urllib.request.urlopen(req, timeout=25) as response:
            body = response.read().decode('utf-8', 'replace')
            result = {'role': role, 'url': url, 'status': response.status, 'checked_utc': datetime.now(timezone.utc).isoformat(), 'retrieved_bytes': len(body)}
            if role == 'topic':
                ns = {'a':'http://www.w3.org/2005/Atom', 'o':'http://a9.com/-/spec/opensearch/1.1/'}
                root = ET.fromstring(body)
                result['totalResults'] = root.findtext('o:totalResults', namespaces=ns)
                result['entries'] = []
                for item in root.findall('a:entry',ns):
                    record = {field: item.findtext('a:'+field,namespaces=ns) for field in ['id','title','published','updated']}
                    identity = re.search(r'\d{4}\.\d{5}', record['id']).group(0)
                    if identity in previous_topic_ids:
                        record['disposition'] = 'prior_identity_only_dedup_no_reaudit'
                    elif record['published'] >= '2026-02-14':
                        record['disposition'] = 'submitted_after_Feb13_cannot_be_public_Feb16_no_date_assignment'
                    else:
                        record['disposition'] = 'new_discovery_needs_public_date_and_contribution'
                        record['summary'] = item.findtext('a:summary',namespaces=ns)
                    result['entries'].append(record)
            else:
                target = re.search(r'<h3[^>]*>.*?16 Feb 2026.*?</h3>(.*?)(?=<h3|$)', body, re.S)
                if target:
                    result['target_excerpt'] = unescape(re.sub('<[^>]+>', ' ', target.group(0)))
                else:
                    result['target_day_found'] = False
                    result['page_excerpt'] = unescape(re.sub('<[^>]+>', ' ', body))[:2500]
            return result
    except Exception as error:
        return {'role': role, 'url': url, 'error': str(error), 'checked_utc': datetime.now(timezone.utc).isoformat()}

with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    payload = json.dumps(list(pool.map(fetch, entries)), ensure_ascii=False, indent=2)
    print(base64.b64encode(zlib.compress(payload.encode(), 9)).decode())
