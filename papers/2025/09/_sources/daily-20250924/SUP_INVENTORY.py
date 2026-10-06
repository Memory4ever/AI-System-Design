import json
import sys
import xml.etree.ElementTree as ET

from SUP_CAPTURE import ROOT

rows = {}
for path in ROOT.glob("SUP_ARXIV_*.raw"):
    if "LIST" in path.name:
        continue
    for entry in ET.parse(path).getroot().findall("{http://www.w3.org/2005/Atom}entry"):
        row = {key: " ".join(entry.findtext("{http://www.w3.org/2005/Atom}" + key, "").split())
               for key in ["id", "title", "summary", "published", "updated"]}
        rows[row["id"]] = row
rows = sorted(rows.values(), key=lambda row: row["id"])
if len(sys.argv) == 1:
    (ROOT / "SUP_DISCOVERY.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
else:
    for index in range(int(sys.argv[1]), min(int(sys.argv[2]), len(rows))):
        row = rows[index]
        print(index, row["id"], row["title"], "\n", row["summary"], "\n")
