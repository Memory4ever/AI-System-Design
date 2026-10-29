"""Bounded Sep11 morphology delta; never overwrite earlier captures."""

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path
import subprocess
import urllib.parse
import xml.etree.ElementTree as ET
import re

from repair_capture_20261021 import capture

BASE = Path(__file__).parent
ROOT = BASE.parents[4]
WINDOW = 'registered:[2025-09-10T16:00:00Z TO 2025-09-11T15:59:59.999Z]'


def text(terms):
    return f'(titles.title:({terms}) OR descriptions.description:({terms}))'


LM = '"language model" OR "language models" OR LLM OR LLMs OR LM OR LMs OR transformer OR transformers OR "mixture of experts" OR MoE'
MULTI = '"foundation model" OR "foundation models" OR "world model" OR "world models" OR "vision language" OR "vision-language" OR "vision-language model" OR "vision-language models" OR "vision-language-action" OR multimodal OR VLA OR VLAs OR VLM OR VLMs OR MLLM OR MLLMs'
THEMES = {
    'MODEL': text(LM) + ' AND ' + text('architecture OR architectures OR attention OR training OR optimization OR optimizer OR optimizers OR alignment OR quantization OR reinforcement OR confidence OR calibration'),
    'SYSTEM': text(LM + ' OR GPU OR GPUs') + ' AND ' + text('inference OR communication OR communications OR kernel OR kernels OR compiler OR compilers OR accelerator OR accelerators OR serving OR parallel OR training'),
    'MULTI': '(' + text(MULTI) + ' AND ' + text('representation OR representations OR generation OR diffusion OR flow OR action OR actions OR training OR fusion OR evaluation OR reasoning OR navigation') + ') OR titles.title:(' + MULTI + ' OR diffusion)',
    'AGENT': text(LM + ' OR agent OR agents OR agentic') + ' AND ' + text('agent OR agents OR agentic OR retrieval OR memory OR memories OR safety OR jailbreak OR jailbreaks OR planning OR tool OR tools'),
}


def baseline():
    names = ['papers/2025/09/12/README.md',
             str(BASE.relative_to(ROOT) / 'SUP_SCREEN_20261012.md'),
             str(BASE.relative_to(ROOT) / 'SUP_SOURCES_20261012.md')]
    record = {'checked_at': dt.datetime.now(dt.timezone.utc).isoformat(),
              'purpose': 'Sep12 report, Sep11 BJT forms discovery only; old 54 families remain valid',
              'window': WINDOW, 'queries': THEMES, 'files': []}
    for relative in names:
        source = ROOT / relative
        raw = source.read_bytes()
        name = {'README.md': 'README', 'SUP_SCREEN_20261012.md': 'AUTHOR',
                'SUP_SOURCES_20261012.md': 'SOURCES'}[source.name]
        target = BASE / ('FORMS_BASELINE_' + name + '_20261021.md')
        with target.open('xb') as stream:
            stream.write(raw)
        record['files'].append({'path': relative, 'snapshot': target.name,
                                'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
    record['status'] = subprocess.run(['git', 'status', '--short', '--', *names],
                                    cwd=ROOT, capture_output=True, text=True, check=True).stdout
    for cached in (False, True):
        result = subprocess.run(['git', 'diff', *(['--cached'] if cached else []), '--check', '--', *names],
                                cwd=ROOT, capture_output=True, text=True)
        record['cached_check' if cached else 'working_check'] = {'exit': result.returncode, 'output': result.stdout + result.stderr}
    with (BASE / 'FORMS_BASELINE_20261021.json').open('x') as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(json.dumps(record, ensure_ascii=False))


def query():
    for name, expression in THEMES.items():
        capture('FORMS_' + name + '_P1', {'client-id': 'arxiv.content',
                'query': '(' + expression + ') AND ' + WINDOW,
                'page[size]': 100, 'sort': 'registered'})


def summary():
    old = set()
    for prefix in ('REPAIR_DISCOVER_', 'REPAIR_COMPLEMENT_', 'REPAIR_ALIAS_'):
        for path in BASE.glob(prefix + '*_20261021.raw.json'):
            old.update(item['id'].lower() for item in json.loads(path.read_text())['data'])
    union = {}
    for name in THEMES:
        path = BASE / ('FORMS_' + name + '_P1_20261021.raw.json')
        data = json.loads(path.read_text())
        print(name, 'total', data.get('meta', {}).get('total'), 'returned', len(data['data']),
              'next', data.get('links', {}).get('next'))
        for item in data['data']:
            union[item['id'].lower()] = item
    print('old', len(old), 'new_union', len(union), 'old_missing', sorted(old - union.keys()),
          'delta', len(union.keys() - old))
    for identity in sorted(union.keys() - old):
        item = union[identity]['attributes']
        print(identity, json.dumps(item.get('titles'), ensure_ascii=False), 'registered', item.get('registered'))


def delta_ids():
    old = set()
    for prefix in ('REPAIR_DISCOVER_', 'REPAIR_COMPLEMENT_', 'REPAIR_ALIAS_'):
        for path in BASE.glob(prefix + '*_20261021.raw.json'):
            old.update(item['id'].split('arxiv.')[-1] for item in json.loads(path.read_text())['data'])
    for name in ('arxiv-v1-title-abstract.json', 'recovery-scoped-abstracts.json'):
        old.update(re.search(r'\d{4}\.\d{5}', item['id'])[0]
                   for item in json.loads((BASE / name).read_text()))
    ns = {'a': 'http://www.w3.org/2005/Atom'}
    for path in BASE.glob('SUP_ARXIV_*_20261012.raw'):
        old.update(re.search(r'\d{4}\.\d{5}', entry.findtext('a:id', namespaces=ns))[0]
                   for entry in ET.fromstring(path.read_bytes()).findall('a:entry', ns))
    current = {item['id'].split('arxiv.')[-1] for path in BASE.glob('FORMS_*_P1_20261021.raw.json')
               for item in json.loads(path.read_text())['data']}
    return sorted(current - old)


def exact():
    identities = delta_ids()
    for start in range(0, len(identities), 25):
        batch = identities[start:start + 25]
        params = {'id_list': ','.join(identity + 'v1' for identity in batch), 'max_results': len(batch)}
        capture('FORMS_EXACT_' + str(start), url='https://export.arxiv.org/api/query?' + urllib.parse.urlencode(params), extension='.raw')


def controls():
    cases = [('LLMS', '2509.08494', 'LLMs'),
             ('LANGUAGE_MODELS', '2509.08778', '"language models"'),
             ('TRANSFORMERS', '2509.08778', 'transformers'),
             ('FOUNDATION_MODELS', '2509.08401', '"foundation models"'),
             ('WORLD_MODELS', '2509.07996', '"world models"'),
             ('AGENTS', '2509.08755', 'agents'),
             ('AGENTIC', '2509.08809', 'agentic'),
             ('GPUS', '2509.08309', 'GPUs'),
             ('TOOLS', '2509.08638', 'tools')]
    for name, identity, form in cases:
        capture('FORMS_CONTROL_' + name, {'client-id': 'arxiv.content',
                'query': text(form) + ' AND doi:"10.48550/arxiv.' + identity + '" AND ' + WINDOW,
                'page[size]': 100})


def gate():
    for identity in ('2509.08418', '2509.08614', '2509.08621', '2509.08738'):
        capture('FORMS_GATE_' + identity, url='https://arxiv.org/html/' + identity + 'v1', extension='.raw')


def sources():
    for identity in ('2509.08031', '2509.08494', '2509.08742'):
        capture('FORMS_SOURCE_' + identity, url='https://arxiv.org/html/' + identity + 'v1', extension='.raw')


def notices():
    for identity in ('2509.08031', '2509.08494', '2509.08742', '2509.08418',
                     '2509.08614', '2509.08621', '2509.08738'):
        capture('FORMS_NOTICE_' + identity, url='https://arxiv.org/abs/' + identity, extension='.raw')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['baseline', 'query', 'summary', 'exact', 'controls', 'gate', 'sources', 'notices'])
    mode = parser.parse_args().mode
    {'baseline': baseline, 'query': query, 'summary': summary, 'exact': exact, 'controls': controls,
     'gate': gate, 'sources': sources, 'notices': notices}[mode]()
