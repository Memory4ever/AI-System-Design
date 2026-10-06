"""Bounded arXiv topic discovery and the user-supplied Seed API identities."""

import subprocess
import sys
from pathlib import Path
from urllib.parse import urlencode

fetch = str(Path(__file__).with_name("fetch_raw.py"))
cats = "(" + " OR ".join("cat:" + x for x in [
    "cs.CL", "cs.LG", "cs.DC", "cs.AI", "cs.CV", "cs.RO",
    "cs.AR", "cs.PL", "cs.OS", "cs.PF", "cs.IR", "cs.MA"
]) + ")"
topics = {
    "training": '(all:"language model" OR all:Transformer OR all:MoE) AND (all:training OR all:optimization OR all:distillation OR all:parallel)',
    "inference": '(all:"language model" OR all:Transformer OR all:GPU) AND (all:inference OR all:quantization OR all:decoding OR all:kernel OR all:"KV cache")',
    "agent": '(all:"language model" OR all:LLM) AND (all:agent OR all:"tool use" OR all:retrieval OR all:memory)',
    "multimodal": '(all:"foundation model" OR all:"vision language" OR all:"world model" OR all:VLA OR all:"diffusion model") AND (all:training OR all:architecture OR all:inference OR all:reasoning)',
}
for topic, terms in topics.items():
    query = cats + ' AND submittedDate:[20251115010000 TO 20251116005959] AND (' + terms + ')'
    params = {"search_query": query, "start": 0, "max_results": 100,
              "sortBy": "submittedDate", "sortOrder": "ascending"}
    subprocess.run([sys.executable, fetch, "raw-arxiv-" + topic + ".xml",
                    "https://export.arxiv.org/api/query?" + urlencode(params)], check=True)
for kind, number in [("blog", 2), ("paper", 1)]:
    for page in [0, 20]:
        params = {"article_type": number, "publish_year": 2025, "count": 20,
                  "page_token": page, "order_desc": "true"}
        subprocess.run([sys.executable, fetch, f"raw-seed-{kind}-p{page}.json",
                        "https://seed.bytedance.com/api/get_article_list_v2?" + urlencode(params)], check=True)
