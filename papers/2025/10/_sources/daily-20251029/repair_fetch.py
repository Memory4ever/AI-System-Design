"""Bounded source recovery for this day's repair only."""

import argparse
import json
import time
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent


def fetch(name, url, body=None, headers=None):
    path = ROOT / (name + '.raw')
    if path.exists():
        return path.read_bytes()
    metadata = {'url': url, 'checked_at': datetime.now(timezone.utc).isoformat()}
    if body is not None:
        metadata['body'] = body
    metadata['headers'] = headers or {}
    request = Request(url, data=json.dumps(body).encode() if body is not None else None,
                      headers={'User-Agent': 'AI-System-Design-research/1.0',
                               **({'Content-Type': 'application/json'} if body else {}),
                               **(headers or {})})
    try:
        with urlopen(request, timeout=70) as response:
            raw = response.read()
            metadata.update(status=response.status, final_url=response.url,
                            content_type=response.headers.get('content-type'), bytes=len(raw))
        path.write_bytes(raw)
    except Exception as error:
        metadata['error'] = str(error)
        raw = b''
    (ROOT / (name + '.request.json')).write_text(json.dumps(metadata, indent=2) + '\n')
    print(name, metadata.get('status'), metadata.get('bytes'), metadata.get('error'), flush=True)
    return raw


TOPICS = {
    'MODEL': '(titles.title:("language model" OR "language models" OR transformer OR transformers OR attention OR MoE OR "foundation model" OR "foundation models"))',
    'TRAIN': '(descriptions.description:("language model" OR "language models" OR "foundation model" OR transformer) AND titles.title:(training OR optimization OR alignment OR reinforcement OR preference OR distillation OR reasoning OR representation))',
    'INFER': '(descriptions.description:("language model" OR "language models" OR transformer OR "deep learning") AND titles.title:(inference OR serving OR kernel OR kernels OR cache OR parallel OR quantization OR compiler OR accelerator OR communication OR scheduling))',
    'AGENT': '(titles.title:(agent OR agents OR agentic OR "tool use" OR "tool calling" OR RAG OR "retrieval augmented" OR memory) AND descriptions.description:("language model" OR "language models" OR LLM OR LLMs OR "foundation model"))',
    'MULTI': '(titles.title:(multimodal OR "multi-modal" OR "vision language" OR "vision-language" OR "world model" OR "world models" OR VLA OR diffusion OR autoregressive) AND descriptions.description:("foundation model" OR "foundation models" OR "language model" OR "language models" OR generative OR transformer))',
    'EVAL': '(titles.title:(evaluation OR benchmark OR hallucination OR faithfulness OR safety OR security OR jailbreak OR "prompt injection") AND descriptions.description:("language model" OR "language models" OR LLM OR LLMs OR agent))',
}


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.hidden += 1
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'tr', 'li', 'dt', 'dd'):
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.hidden = max(0, self.hidden - 1)
        if tag in ('p', 'div', 'section', 'h1', 'h2', 'h3', 'h4', 'tr', 'li', 'dt', 'dd'):
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def core(identities):
    import subprocess
    python = '/Users/apple/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3'
    for identity in identities:
        name = 'REPAIR_CORE_' + identity
        raw = fetch(name, 'https://arxiv.org/html/' + identity + 'v1')
        if raw and b'<html' in raw[:1000].lower():
            parser = TextParser()
            parser.feed(raw.decode(errors='replace'))
            lines = [' '.join(line.split()) for line in ''.join(parser.parts).splitlines()]
            (ROOT / (name + '.txt')).write_text('\n'.join(line for line in lines if line) + '\n')
        else:
            pdf = fetch(name + '_PDF', 'https://arxiv.org/pdf/' + identity + 'v1')
            if pdf[:4] == b'%PDF':
                command = 'import pymupdf,sys;d=pymupdf.open(sys.argv[1]);print("\\n".join("PAGE "+str(i+1)+"\\n"+p.get_text() for i,p in enumerate(d)))'
                result = subprocess.run([python, '-c', command, str(ROOT / (name + '_PDF.raw'))], capture_output=True, text=True)
                if result.returncode == 0:
                    (ROOT / (name + '.txt')).write_text(result.stdout)
                else:
                    print(result.stderr, flush=True)
        fetch('REPAIR_NOTICE_' + identity, 'https://arxiv.org/abs/' + identity)
        time.sleep(3)


def discover():
    for field in ('registered', 'created'):
        for topic, query in TOPICS.items():
            complete = f'{field}:[2025-10-27T16:00:00Z TO 2025-10-28T15:59:59Z] AND {query}'
            for page in range(1, 5):
                params = {'query': complete, 'client-id': 'arxiv.content', 'page[size]': 100, 'page[number]': page}
                raw = fetch(f'REPAIR_DC2_{field}_{topic}_{page}', 'https://api.datacite.org/dois?' + urlencode(params))
                if not raw:
                    break
                result = json.loads(raw)
                print(field, topic, page, len(result.get('data', [])), result.get('meta', {}).get('total'), flush=True)
                if page * 100 >= result.get('meta', {}).get('total', 0):
                    break
                time.sleep(0.5)


def navigation():
    fetch('REPAIR_ARXIV_RULE_2025', 'https://raw.githubusercontent.com/arXiv/arxiv-docs/46793211923f3e84140efe04524a250a93b2577b/source/help/availability.md')
    fetch('REPAIR_DATACITE_RULE', 'https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api')
    fetch('REPAIR_GOOGLE_1', 'https://research.google/pubs/?category=2025&search=language%20model')
    fetch('REPAIR_HUNYUAN_ZH', 'https://api.hunyuan.tencent.com/api/blog/publicList',
          {'pageNum': 1, 'pageSize': 100, 'renderType': 0}, {'accept-language': 'zh'})


def inventory():
    sys.path.insert(0, str(ROOT.parents[4] / 'scripts'))
    from arxiv_publication_date import publication_date_envelope
    groups = {}
    for field in ('created', 'registered'):
        groups[field] = {item['id']: item for path in ROOT.glob(f'REPAIR_DC2_{field}_*.raw')
                         for item in json.loads(path.read_text())['data']}
    records = []
    for doi, item in sorted(groups['registered'].items()):
        identity = doi.split('arxiv.')[1]
        fields = item['attributes']
        record = {'id': identity, 'title': fields['titles'][0]['title'],
                  'abstract': '\n'.join(part['description'] for part in fields.get('descriptions', [])
                                        if part.get('descriptionType') == 'Abstract'),
                  'subjects': fields.get('subjects'),
                  'envelope': publication_date_envelope(item, identity)}
        records.append(record)
    result = {'created_count': len(groups['created']), 'registered_count': len(groups['registered']),
              'registered_only': sorted(groups['registered'].keys() - groups['created'].keys()),
              'created_only': sorted(groups['created'].keys() - groups['registered'].keys()),
              'records': records}
    (ROOT / 'REPAIR_INVENTORY.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    for start in range(0, len(records), 30):
        text = '\n\n'.join(f"{x['id']} | {x['title']} | {x['envelope']['bounded_bjt_date']}\n{x['abstract']}"
                           for x in records[start:start + 30])
        (ROOT / f'REPAIR_ABSTRACTS_{start:03}.txt').write_text(text + '\n')
    print({key: value for key, value in result.items() if key != 'records'})


def complement():
    sys.path.insert(0, str(ROOT.parents[4] / 'scripts'))
    from arxiv_publication_date import publication_date_envelope
    data = json.loads((ROOT / 'REPAIR_MONTH_COMPLEMENT_DC.raw').read_text())['data']
    records = []
    for item in sorted(data, key=lambda item: item['id']):
        identity = item['id'].split('arxiv.')[1]
        fields = item['attributes']
        records.append({'id': identity, 'title': fields['titles'][0]['title'],
                        'abstract': '\n'.join(x['description'] for x in fields['descriptions']
                                              if x.get('descriptionType') == 'Abstract'),
                        'envelope': publication_date_envelope(item, identity)})
    (ROOT / 'REPAIR_COMPLEMENT_INVENTORY.json').write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    for start in range(0, len(records), 10):
        text = '\n\n'.join(f"{x['id']} | {x['title']} | {x['envelope']['bounded_bjt_date']}\n{x['abstract']}"
                           for x in records[start:start + 10])
        (ROOT / f'REPAIR_COMPLEMENT_ABSTRACTS_{start:02}.txt').write_text(text + '\n')
    print(len(records))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=('discovery', 'navigation', 'inventory', 'core', 'complement'))
    parser.add_argument('identities', nargs='*')
    args = parser.parse_args()
    core(args.identities) if args.mode == 'core' else {'discovery': discover, 'navigation': navigation, 'inventory': inventory, 'complement': complement}[args.mode]()
