import json
import re

from bs4 import BeautifulSoup
from SUP_CAPTURE import ROOT, capture

OUTSIDE = set("17942 17950 17957 17991 18057 18407 18445 18497 18588 18633 18758 18796 18894 19168 19182 22704".split())
rows = json.loads((ROOT / "SUP_NEW_DISCOVERY.json").read_text())
result = []
for row in rows:
    identifier, version = row["id"].rsplit("/", 1)[-1].split("v")
    if identifier.split(".")[1] in OUTSIDE:
        continue
    exact = "SUP_" + identifier + "v1.abs"
    capture(exact, "https://arxiv.org/abs/" + identifier + "v1")
    current = exact
    if version != "1":
        current = "SUP_" + identifier + ".current"
        capture(current, "https://arxiv.org/abs/" + identifier)
    soup = BeautifulSoup((ROOT / (current + ".raw")).read_bytes(), "html.parser")
    exact_soup = BeautifulSoup((ROOT / (exact + ".raw")).read_bytes(), "html.parser")
    fields = {selector: [node.get_text(" ", strip=True) for node in soup.select(selector)]
              for selector in [".title", ".dateline", ".comments", ".submission-history", ".withdrawn", ".journal-ref"]}
    exact_fields = {selector: [node.get_text(" ", strip=True) for node in exact_soup.select(selector)]
                    for selector in [".title", ".abstract", ".comments", ".withdrawn"]}
    result.append(dict(id=identifier, current_file=current + ".raw", exact_file=exact + ".raw",
                       fields=fields, exact_fields=exact_fields))
(ROOT / "SUP_CURRENT_LIGHT.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print("LIGHT_ROWS", len(result))
