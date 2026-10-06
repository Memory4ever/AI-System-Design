import json
import pathlib
import urllib.parse
import xml.etree.ElementTree as ET

from SUP_CAPTURE import ROOT, capture

CATS = "(" + " OR ".join("cat:" + x for x in [
    "cs.CL", "cs.LG", "cs.DC", "cs.AI", "cs.CV", "cs.RO", "cs.AR",
    "cs.PL", "cs.OS", "cs.PF", "cs.IR", "cs.MA"]) + ")"
GROUPS = {
    "model": ['"language model"', 'LLM', 'transformer', 'MoE', 'pretraining',
              '"post training"', '"model optimization"', '"learning theory"'],
    "system": ['GPU', 'kernel', 'quantization', 'collective', 'communication',
               'accelerator', 'compiler', '"inference serving"', '"distributed training"'],
    "multimodal": ['"vision language"', '"world model"', 'VLA', 'diffusion',
                   '"multimodal model"', '"video generation"', '"embodied model"'],
    "agent": ['"language agent"', '"LLM agent"', '"tool calling"',
              '"tool use"', 'RAG', '"memory retrieval"', '"multi agent"'],
}
rows = {}
for group, terms in GROUPS.items():
    start = 0
    while True:
        query = CATS + " AND (" + " OR ".join("all:" + t for t in terms) + ")"
        query += " AND submittedDate:[202509161600 TO 202509171600]"
        url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(dict(
            search_query=query, start=start, max_results=200,
            sortBy="submittedDate", sortOrder="ascending"))
        name = "SUP_ARXIV_" + group.upper() + "_" + str(start)
        capture(name, url)
        try:
            doc = ET.fromstring((ROOT / (name + ".raw")).read_bytes())
        except ET.ParseError:
            break
        ns = {"a": "http://www.w3.org/2005/Atom",
              "o": "http://a9.com/-/spec/opensearch/1.1/"}
        entries = doc.findall("a:entry", ns)
        total = int(doc.findtext("o:totalResults", "0", ns))
        for entry in entries:
            identity = entry.findtext("a:id", "", ns).rsplit("/", 1)[-1]
            record = {key: entry.findtext("a:" + key, "", ns)
                      for key in ("title", "summary", "published", "updated")}
            record["groups"] = rows.get(identity, {}).get("groups", []) + [group]
            rows[identity] = record
        if start + len(entries) >= total or not entries:
            break
        start += len(entries)
(ROOT / "SUP_DISCOVERY.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n")
print("unique", len(rows))
