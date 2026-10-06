"""Four bounded topic queries; submission fields are discovery only."""
import pathlib
import subprocess
import sys
import urllib.parse

root = pathlib.Path(__file__).parent
topics = {
    "language": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:Transformer OR all:"mixture of experts")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:"language model" OR all:GPU)',
    "agent": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:reasoning OR all:memory)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO) AND (all:"foundation model" OR all:"vision language" OR all:"world model" OR all:VLA OR all:"diffusion model")',
}
for name, topic in topics.items():
    query = topic + ' AND submittedDate:[202511200000 TO 202511212359]'
    params = {"search_query": query, "start": 0, "max_results": 25,
              "sortBy": "submittedDate", "sortOrder": "descending"}
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    print(name, url, flush=True)
    subprocess.run([sys.executable, str(root / "fetch_raw.py"),
                    "arxiv_" + name + ".xml", url], check=True)
