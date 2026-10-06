"""Fetch only semantic title selections and successful narrow-theme hits."""
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
ns = {"a": "http://www.w3.org/2005/Atom"}
ids = {"04401", "04428", "04450", "04477", "04479", "04483", "04504", "04514", "04533", "04536", "04539", "04547", "04564", "04576", "04587", "04637", "04631", "04633", "05396", "05186"}
for f in d.glob("arxiv-*-retry2.raw"):
    try:
        root = ET.parse(f)
    except ET.ParseError:
        continue
    for row in root.findall("a:entry", ns):
        ids.add(row.findtext("a:id", namespaces=ns).rsplit("/", 1)[-1][5:10])
for short in sorted(ids):
    identity = "2510." + short + "v1"
    subprocess.run([sys.executable, str(fetch), str(d), "abs-" + identity, "https://arxiv.org/abs/" + identity], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, d.glob("abs-*.raw"))], check=True)
