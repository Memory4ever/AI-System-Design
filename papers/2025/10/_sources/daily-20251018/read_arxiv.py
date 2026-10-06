import pathlib
import sys
import xml.etree.ElementTree as ET
from recover_day import Page, ROOT

ns = {"a":"http://www.w3.org/2005/Atom", "o":"http://a9.com/-/spec/opensearch/1.1/"}
seen = set()
selected = set(sys.argv[1:])
for filename in sorted(ROOT.glob("arxiv_*.raw")):
    if filename.name.startswith("arxiv_titles_"):
        continue
    root = ET.parse(filename).getroot()
    print("QUERY", filename.name, "total", root.findtext("o:totalResults", namespaces=ns))
    for entry in root.findall("a:entry", ns):
        ident = entry.findtext("a:id", namespaces=ns).rsplit("/",1)[-1]
        family = ident.split("v")[0]
        if family in seen or (selected and family not in selected):
            continue
        seen.add(family)
        print("ID", ident, "published_discovery", entry.findtext("a:published", namespaces=ns),
              "updated", entry.findtext("a:updated", namespaces=ns))
        print("TITLE", " ".join(entry.findtext("a:title", namespaces=ns).split()))
        if selected:
            print("ABSTRACT", " ".join(entry.findtext("a:summary", namespaces=ns).split()))
