"""Display source fields without semantic filtering or completion decisions."""
import sys
from pathlib import Path
from lxml import html

doc = html.fromstring((Path(__file__).parent / sys.argv[1]).read_bytes())
mode = sys.argv[2]
clean = lambda values: " ".join(" ".join(values).split())
if mode == "sections":
    for key in sys.argv[3:]:
        print(key, " ".join(doc.get_element_by_id(key).text_content().split()))
else:
    entries = doc.xpath('//li[contains(@class,"arxiv-result")]')
    print("HEADER", clean(doc.xpath('//h1//text()')), "DOM", len(entries))
    for index, entry in enumerate(entries, 1):
        if len(sys.argv) > 3 and str(index) not in sys.argv[3:]:
            continue
        print(index, clean(entry.xpath('.//p[contains(@class,"list-title")]/a[1]/text()')),
              clean(entry.xpath('.//p[contains(concat(" ",normalize-space(@class)," ")," title ")]//text()')))
        if mode == "abstracts":
            print("AB", clean(entry.xpath('.//span[contains(@class,"abstract-full")]//text()')))
            print("META", clean(entry.xpath('.//p[contains(@class,"is-size-7")]//text()')))
