"""Read current official event metadata only, not later-version research bodies."""
import sys
from pathlib import Path
from lxml import html

root = Path(__file__).parent
for key in sys.argv[1:]:
    doc = html.fromstring((root/f'REPAIR_CURRENT_{key}_20261029.html').read_bytes())
    print('\nID', key)
    for query in ('//h1[contains(@class,"title")]', '//td[contains(@class,"comments")]',
                  '//td[contains(@class,"jref")]', '//td[contains(@class,"doi")]',
                  '//div[contains(@class,"submission-history")]',
                  '//*[contains(@class,"withdrawn")]', '//*[contains(@class,"extra-services")]/a[contains(@href,"withdraw")]'):
        for node in doc.xpath(query):
            print(' '.join(node.text_content().split()))
