"""Restore exact first versions for this day's own thematic title matches."""
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode
import xml.etree.ElementTree as ET

d = Path(sys.argv[1])
fetch = Path(__file__).parent.parent / "daily-20251002" / "fetch.py"
ns = {"a":"http://www.w3.org/2005/Atom"}
ids = []
for f in d.glob("arxiv-*.raw"):
    for e in ET.parse(f).findall("a:entry", ns):
        identity = e.findtext("a:id",namespaces=ns).rsplit("/",1)[-1].split("v")[0]+"v1"
        if identity not in ids:
            ids.append(identity)
url = "https://export.arxiv.org/api/query?"+urlencode({"id_list":",".join(ids),"max_results":100})
subprocess.run([sys.executable,str(fetch),str(d),"exact-v1",url],check=True)
for token in (0,20,40):
    subprocess.run([sys.executable,str(fetch),str(d),"seed-blog-repair"+str(token),
        "https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&order_desc=false&mode=1&page_token="+str(token)],check=True)
for cat in ("cs.CL","cs.CV","cs.DC","cs.PL","cs.IR"):
    subprocess.run([sys.executable,str(fetch),str(d),"titles-"+cat,
        "https://arxiv.org/list/"+cat+"/2025-10?skip=0&show=25"],check=True)
subprocess.run([sys.executable,str(fetch.with_name("extract.py")),*map(str,d.glob("*.raw"))],check=True)
