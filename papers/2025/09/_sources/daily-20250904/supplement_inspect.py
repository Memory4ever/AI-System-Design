"""Derived numbered text for bounded reading; extraction is not review."""
import argparse
import json
import pathlib
from bs4 import BeautifulSoup

BASE = pathlib.Path(__file__).parent
parser = argparse.ArgumentParser()
parser.add_argument('name')
parser.add_argument('selector', nargs='?', default='headings')
args = parser.parse_args()
path = BASE / (args.name + '.raw')
soup = BeautifulSoup(path.read_bytes(), 'html.parser')
if args.selector == 'current':
    for path in sorted(BASE.glob('SUP_CURRENT_*_20261011.raw')):
        soup = BeautifulSoup(path.read_bytes(), 'html.parser')
        title = soup.select_one('h1.title')
        comments = soup.select_one('td.tablecell.comments')
        history = soup.select_one('.submission-history')
        extra = [element.get_text(' ', strip=True) for element in soup.select('.withdrawn, .extra-services .notice')]
        print(path.name, title.get_text(' ', strip=True) if title else 'NO TITLE', 'COMMENT:', comments.get_text(' ', strip=True) if comments else 'Not Disclosed', 'NOTICE:', extra, 'HISTORY:', history.get_text(' ', strip=True) if history else 'NO HISTORY')
elif args.selector == 'headings':
    for element in soup.select('h2,h3,h4,h5'):
        parent = element.find_parent('section')
        print(parent.get('id') if parent else element.get('id'), element.get_text(' ', strip=True))
elif args.selector == 'text':
    for element in soup.select('script,style,nav,header,footer'):
        element.decompose()
    print(soup.get_text(' ', strip=True))
else:
    for selector in args.selector.split(','):
        if selector.startswith('#'):
            selector = '[id="' + selector[1:] + '"]'
        elements = soup.select(selector)
        print('SELECTOR', selector, 'MATCHES', len(elements))
        for element in elements:
            print(element.get_text(' ', strip=True))
