from pathlib import Path
import sys

from lxml import etree, html

base = Path(__file__).parent
ns = {"a": "http://www.w3.org/2005/Atom"}
old = set()
for path in [*base.glob("arxiv_*.raw"), base / "supplement.xml"]:
    tree = etree.parse(str(path))
    for entry in tree.findall("a:entry", ns):
        old.add(entry.findtext("a:id", namespaces=ns).split("/abs/")[-1].split("v")[0])

entries = {}
for name in ["MODEL", "TRAIN_S25", "AGENT", "MULTI", "SYSTEM"]:
    tree = html.parse(str(base / ("SUP_" + name + ".raw")))
    for index, entry in enumerate(tree.xpath("//li[contains(@class,'arxiv-result')]")):
        link = entry.xpath(".//p[contains(@class,'list-title')]/a[1]")[0]
        identity = link.get("href").split("/abs/")[-1]
        entries.setdefault(identity, (name, index, entry))

mode, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
items = [(key, value) for key, value in entries.items() if (key in old) == (mode == "old")]
for number in range(start, min(end, len(items))):
    identity, (name, index, entry) = items[number]
    print("\nITEM", number, identity, name, index)
    selectors = [
        ".//p[contains(concat(' ',normalize-space(@class),' '),' title ')]",
        ".//span[contains(@class,'abstract-full')]",
        ".//p[contains(@class,'is-size-7')]",
    ]
    for selector in selectors:
        for node in entry.xpath(selector):
            print(" ".join(node.text_content().split()))
