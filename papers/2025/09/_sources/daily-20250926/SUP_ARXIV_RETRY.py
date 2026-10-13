import json
import time
import xml.etree.ElementTree as ET
from urllib.parse import parse_qs, urlencode, urlparse

from SUP_CAPTURE import ROOT, capture

for group in ["MODEL", "AGENT", "MULTIMODAL", "SYSTEM"]:
    original = json.loads((ROOT / ("SUP_ARXIV_" + group + "_0.request.json")).read_text())
    params = {k: v[0] for k, v in parse_qs(urlparse(original["url"]).query).items()}
    params["max_results"] = "1000"
    time.sleep(4)
    key = "SUP_ARXIV_" + group + "_RETRY"
    capture(key, "https://arxiv.org/api/query?" + urlencode(params), timeout=45)
    try:
        root = ET.parse(ROOT / (key + ".raw")).getroot()
        print(group, "entries", len(root.findall("{http://www.w3.org/2005/Atom}entry")), "total", root.findtext("{http://a9.com/-/spec/opensearch/1.1/}totalResults"), flush=True)
    except ET.ParseError:
        print(group, "response not Atom; retain discovery gap", flush=True)
