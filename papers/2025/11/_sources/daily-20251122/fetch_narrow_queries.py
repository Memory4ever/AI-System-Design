"""Narrow broad hits before forming any abstract-review queue."""
import pathlib
import subprocess
import sys
import urllib.parse

root = pathlib.Path(__file__).parent
topics = {
    "mechanisms": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:LLM) AND (ti:attention OR ti:quantization OR ti:"mixture of experts" OR ti:Transformer)',
    "agent_memory": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (ti:memory OR ti:"tool use" OR ti:reward OR ti:whistleblow)',
    "generation_vla": '(cat:cs.CV OR cat:cs.RO) AND (ti:"video generation" OR ti:"world model" OR ti:"vision-language-action" OR ti:VLA)',
}
for name, topic in topics.items():
    params = {"search_query": topic + ' AND submittedDate:[202511200000 TO 202511212359]',
              "start": 0, "max_results": 25, "sortBy": "submittedDate", "sortOrder": "descending"}
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)
    subprocess.run([sys.executable, str(root / "fetch_raw.py"), "narrow_" + name + ".xml", url], check=True)
