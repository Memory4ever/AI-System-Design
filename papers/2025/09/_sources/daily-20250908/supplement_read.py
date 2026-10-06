"""Mechanical HTML section reader; section output does not establish a verdict."""
import argparse
from pathlib import Path
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument('identity')
parser.add_argument('--section', action='append')
parser.add_argument('--revision')
args = parser.parse_args()
base = Path(__file__).parent
name = 'SUP_REV_' + args.identity + args.revision if args.revision else 'SUP_CORE_' + args.identity
soup = BeautifulSoup((base / (name + '_20261011.raw')).read_text(), 'html.parser')
for node in soup.select('nav, header, footer'):
    node.decompose()
if not args.section:
    for node in soup.select('section'):
        heading = node.find(['h1', 'h2', 'h3', 'h4', 'h5'], recursive=False)
        if heading:
            print(node.get('id'), heading.get_text(' ', strip=True))
else:
    for identity in args.section:
        section = soup.find(id=identity)
        if not section:
            raise ValueError('Missing section: ' + identity)
        print('\nSECTION', identity)
        print(section.get_text(' ', strip=True))
