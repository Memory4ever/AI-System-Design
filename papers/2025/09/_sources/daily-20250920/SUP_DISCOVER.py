import json
import urllib.parse
import xml.etree.ElementTree as ET

from SUP_CAPTURE import ROOT, capture

CATEGORIES = "cs.CL cs.LG cs.DC cs.AI cs.CV cs.RO cs.AR cs.PL cs.OS cs.PF cs.IR cs.MA".split()
THEMES = {
    "model": 'all:"language model" OR all:"foundation model" OR all:transformer OR all:"mixture of experts" OR all:attention OR all:"meta-learning"',
    "agent": 'all:"LLM agent" OR all:"tool calling" OR all:"retrieval augmented" OR all:"agent memory" OR all:"agent planning" OR all:"multi-agent language"',
    "system": 'all:"model serving" OR all:"LLM inference" OR all:"GPU training" OR all:"KV cache" OR all:"distributed training" OR all:"neural compiler" OR all:"GPU kernel"',
    "multimodal": 'all:"vision language" OR all:"world model" OR all:"vision language action" OR all:"diffusion model" OR all:"audio language" OR all:"speech language"',
}
NS = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
found = {}
for group, theme in THEMES.items():
    category = " OR ".join("cat:" + item for item in CATEGORIES)
    query = "(" + category + ") AND (" + theme + ") AND submittedDate:[202509181600 TO 202509191600]"
    params = dict(search_query=query, start=0, max_results=200,
                  sortBy="submittedDate", sortOrder="ascending")
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    name = "SUP_ARXIV_" + group.upper()
    capture(name, url)
    try:
        root = ET.fromstring((ROOT / (name + ".raw")).read_bytes())
    except ET.ParseError:
        print(group, "not Atom", flush=True)
        continue
    entries = root.findall("a:entry", NS)
    print(group, "total", root.findtext("o:totalResults", namespaces=NS), "returned", len(entries), flush=True)
    for entry in entries:
        identity = entry.findtext("a:id", namespaces=NS).split("/abs/")[-1]
        row = found.setdefault(identity, dict(
            title=" ".join(entry.findtext("a:title", namespaces=NS).split()),
            summary=entry.findtext("a:summary", namespaces=NS).strip(),
            published=entry.findtext("a:published", namespaces=NS),
            updated=entry.findtext("a:updated", namespaces=NS), groups=[]))
        row["groups"].append(group)
(ROOT / "SUP_DISCOVERY.json").write_text(json.dumps(found, ensure_ascii=False, indent=2) + "\n")
print("unique", len(found), flush=True)
