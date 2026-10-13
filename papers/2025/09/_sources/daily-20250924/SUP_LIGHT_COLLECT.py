import json
import sys

from bs4 import BeautifulSoup
from SUP_CAPTURE import ROOT

rows = json.loads((ROOT / "SUP_NEW_DISCOVERY.json").read_text())
result = []
for row in rows:
    identifier, version = row["id"].rsplit("/", 1)[-1].split("v")
    exact = "SUP_" + identifier + "v1.abs.raw"
    if not (ROOT / exact).exists():
        continue
    current = "SUP_" + identifier + ".current.raw" if version != "1" else exact
    soup = BeautifulSoup((ROOT / current).read_bytes(), "html.parser")
    exact_soup = BeautifulSoup((ROOT / exact).read_bytes(), "html.parser")
    fields = {selector: [node.get_text(" ", strip=True) for node in soup.select(selector)]
              for selector in [".title", ".dateline", ".comments", ".submission-history", ".withdrawn", ".journal-ref"]}
    exact_fields = {selector: [node.get_text(" ", strip=True) for node in exact_soup.select(selector)]
                    for selector in [".title", ".abstract", ".comments", ".withdrawn"]}
    result.append(dict(id=identifier, version=version, current_file=current, exact_file=exact,
                       fields=fields, exact_fields=exact_fields))
(ROOT / "SUP_CURRENT_LIGHT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print("LIGHT_ROWS", len(result))
for x in result[int(sys.argv[1]):int(sys.argv[2])]:
    print(x["id"], "current version", x["version"], "fields", json.dumps(x["fields"], ensure_ascii=False))
    if x["version"] != "1":
        print("V1", json.dumps(x["exact_fields"], ensure_ascii=False))
