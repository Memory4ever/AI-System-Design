"""Mechanical extraction for this Daily only; output is not a reading claim."""
import argparse
import json
import pathlib
import re
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from pypdf import PdfReader

BASE = pathlib.Path(__file__).parent
NS = {'a': 'http://www.w3.org/2005/Atom'}

def exacts():
    result = {}
    for path in BASE.glob('SUP_EXACT_*_20261011.raw'):
        for entry in ET.fromstring(path.read_bytes()).findall('a:entry', NS):
            identity = entry.findtext('a:id', namespaces=NS).split('/abs/')[1]
            result[identity.split('v')[0]] = entry
    return sorted(result.items())

def next_objects(soup):
    for script in soup.find_all('script'):
        text = script.string or ''
        match = re.search(r'self\.__next_f\.push\((.*)\)\s*$', text, re.S)
        if not match:
            continue
        try:
            value = json.loads(match[1])
        except ValueError:
            continue
        if len(value) < 2 or not isinstance(value[1], str):
            continue
        for line in value[1].splitlines():
            _, _, payload = line.partition(':')
            if payload.startswith('I'):
                payload = payload[1:]
            try:
                yield json.loads(payload)
            except ValueError:
                pass

def walk(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)

parser = argparse.ArgumentParser()
parser.add_argument('mode', choices=['ab', 'html', 'rsc', 'pdf', 'core'])
parser.add_argument('target')
parser.add_argument('end', nargs='?', type=int)
parser.add_argument('--sections', default='')
args = parser.parse_args()
if args.mode == 'ab':
    for identity, entry in exacts()[int(args.target):args.end]:
        print(entry.findtext('a:id', namespaces=NS))
        print(' '.join(entry.findtext('a:title', namespaces=NS).split()))
        print(entry.findtext('a:summary', namespaces=NS), '\n')
elif args.mode == 'pdf':
    reader = PdfReader(BASE / args.target)
    for page in range(args.end or len(reader.pages)):
        print('PAGE', page + 1, reader.pages[page].extract_text())
else:
    soup = BeautifulSoup((BASE / args.target).read_bytes(), 'html.parser')
    if args.mode == 'core':
        for identity in args.sections.split(','):
            node = soup.find(id=identity)
            print(identity, node.get_text(' ', strip=True) if node else 'MISSING')
    elif args.mode == 'rsc':
        seen = set()
        for root in next_objects(soup):
            for obj in walk(root):
                if any(key in obj for key in ['publishedOn', 'publishedAt', 'publicationDate']):
                    value = json.dumps({key: obj[key] for key in ['title', 'slug', 'publishedOn', 'publishedAt', 'publicationDate', 'hasMore', 'nextPage'] if key in obj}, ensure_ascii=False)
                    if value not in seen:
                        seen.add(value)
                        date = obj.get('publishedOn', obj.get('publishedAt', obj.get('publicationDate', '')))
                        if '2025-09' in str(date):
                            print(value)
    else:
        for node in soup(['script', 'style', 'nav', 'footer', 'header']):
            node.decompose()
        print((soup.find('main') or soup).get_text(' ', strip=True))
