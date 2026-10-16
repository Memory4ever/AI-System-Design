"""Print selected source fields; no semantic filtering or completion decisions."""
import sys
from pathlib import Path
from lxml import html

path = Path(__file__).parent / sys.argv[1]
doc = html.fromstring(path.read_bytes())
mode = sys.argv[2] if len(sys.argv) > 2 else "titles"
clean = lambda xs: " ".join(" ".join(xs).split())
entries = doc.xpath('//li[contains(@class,"arxiv-result")]')
if mode in {"titles", "abstracts"}:
    print("HEADER", clean(doc.xpath('//h1//text()')), "DOM", len(entries))
    for i, entry in enumerate(entries, 1):
        if len(sys.argv) > 3 and str(i) not in sys.argv[3:]:
            continue
        print(i, clean(entry.xpath('.//p[contains(@class,"list-title")]/a[1]/text()')),
              clean(entry.xpath('.//p[contains(concat(" ",normalize-space(@class)," ")," title ")]//text()')))
        if mode == "abstracts":
            print("AB", clean(entry.xpath('.//span[contains(@class,"abstract-full")]//text()')))
            print("META", clean(entry.xpath('.//p[contains(@class,"is-size-7")]//text()')))
elif mode == "sections":
    for key in sys.argv[3:]:
        print(key, " ".join(doc.get_element_by_id(key).text_content().split()))
