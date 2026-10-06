"""Restore only day-06 theme identities and manually selected related titles."""
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET
import re

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
ns = {"a": "http://www.w3.org/2005/Atom"}
ids = set()
for p in d.glob("arxiv-*.raw"):
    for e in ET.fromstring(p.read_bytes()).findall("a:entry", ns):
        ids.add(re.sub(r"v\d+$", "", e.findtext("a:id", namespaces=ns).split("/")[-1]))
ids.update("2510."+x for x in "03999 04009 04013 04031 04032 04045 04067 04071 04080 04081 04120 04128 04139 03993 05168 04022 04024 04034 04039 04044 04066 04090 04127 05173 04136 04142 04174 04226 04239".split())
for ident in sorted(ids):
    subprocess.run([sys.executable,str(fetch),str(d),"abs-"+ident,"https://arxiv.org/abs/"+ident+"v1"],check=True)
for source, pattern, prefix in [
    ("deepseek-news", r'src="([^\"]+/news/page-[^\"]+\.js)"', "https://www.deepseek.com"),
    ("zai-research", r'src="([^\"]+/research/page-[^\"]+\.js)"', "https://www.zhipuai.cn"),
]:
    urls = re.findall(pattern,(d/(source+".raw")).read_text())
    if urls:
        subprocess.run([sys.executable,str(fetch),str(d),source+"-js",prefix+urls[0]],check=True)
subprocess.run([sys.executable,str(fetch.with_name("extract.py")),*map(str,d.glob("abs-*.raw"))],check=True)
