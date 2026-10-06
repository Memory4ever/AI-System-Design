"""Restore exact versions from own-day thematic discovery, not broad inventories."""
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
ns = {"a": "http://www.w3.org/2005/Atom"}
ids = set()
for f in sorted(d.glob("arxiv-*.raw")):
    root = ET.fromstring(f.read_bytes())
    for entry in root.findall("a:entry", ns):
        ids.add(entry.findtext("a:id", namespaces=ns).rsplit("/", 1)[-1].split("v")[0])
for ident in sorted(ids):
    subprocess.run([sys.executable, str(fetch), str(d), "abs-"+ident,
                    "https://arxiv.org/abs/"+ident+"v1"], check=True)
for category in ("cs.CL", "cs.CV", "cs.DC", "cs.PL", "cs.IR"):
    subprocess.run([sys.executable, str(fetch), str(d), "titles-"+category,
                    "https://arxiv.org/list/"+category+"/2025-10?skip=0&show=25"], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")),
                *map(str, d.glob("abs-*.raw")), *map(str, d.glob("titles-*.raw"))], check=True)
