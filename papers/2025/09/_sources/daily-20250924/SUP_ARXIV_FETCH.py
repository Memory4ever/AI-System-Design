import urllib.parse
import xml.etree.ElementTree as ET

from SUP_CAPTURE import ROOT, capture


GROUPS = [
    ("MODEL", ["cs.CL", "cs.LG"], ["language model", "foundation model", "transformer", "MoE", "post-training", "reasoning"]),
    ("AGENT", ["cs.AI", "cs.IR", "cs.MA"], ["language model", "LLM", "agent", "retrieval augmented", "memory"]),
    ("MULTIMODAL", ["cs.CV", "cs.RO"], ["foundation model", "multimodal", "world model", "vision language", "diffusion", "VLA"]),
    ("SYSTEM", ["cs.DC", "cs.AR", "cs.PL", "cs.OS", "cs.PF"], ["large language", "LLM", "transformer", "GPU", "model inference", "model training"]),
]

if __name__ == "__main__":
    for name, categories, terms in GROUPS:
        category = " OR ".join("cat:" + x for x in categories)
        topic = " OR ".join('all:"' + x + '"' for x in terms)
        query = "(" + category + ") AND (" + topic + ") AND submittedDate:[202509221600 TO 202509231559]"
        start = 0
        while True:
            key = "SUP_ARXIV_" + name + "_" + str(start)
            params = dict(search_query=query, start=start, max_results=100, sortBy="submittedDate", sortOrder="ascending")
            capture(key, "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params))
            try:
                root = ET.parse(ROOT / (key + ".raw")).getroot()
                total = int(root.findtext("{http://a9.com/-/spec/opensearch/1.1/}totalResults", "0"))
                count = len(root.findall("{http://www.w3.org/2005/Atom}entry"))
                print(name, "start", start, "entries", count, "total", total, flush=True)
            except (ET.ParseError, ValueError):
                break
            if count == 0 or start + count >= total:
                break
            start += count
    for category in ["cs.CL", "cs.LG", "cs.AI", "cs.CV", "cs.RO", "cs.DC", "cs.AR", "cs.PL", "cs.OS", "cs.PF", "cs.IR", "cs.MA"]:
        capture("SUP_ARXIV_LIST_" + category, "https://arxiv.org/list/" + category + "/20250923")
