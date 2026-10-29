"""Bounded Sep18 normal-announcement discovery, never publication proof."""
import json
import sys
from urllib.parse import urlencode

from REPAIR_capture_20261023 import capture

THEMES = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:"language models" OR all:transformer OR all:transformers OR all:"mixture of experts" OR all:"foundation model" OR all:"foundation models") AND (all:architecture OR all:architectures OR all:attention OR all:optimization OR all:training OR all:"post-training")',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG OR cat:cs.CL) AND (all:"language model" OR all:"language models" OR all:GPU OR all:GPUs OR all:LLM OR all:LLMs) AND (all:inference OR all:communication OR all:kernel OR all:kernels OR all:serving OR all:parallel OR all:compiler OR all:compilers OR all:scheduling)',
    "agents": '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:"language models" OR all:LLM OR all:LLMs) AND (all:agent OR all:agents OR all:retrieval OR all:memory OR all:memories OR all:safety OR all:jailbreak OR all:jailbreaks OR all:"tool calling" OR all:"tool use")',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG OR cat:cs.CL) AND (all:"foundation model" OR all:"foundation models" OR all:"world model" OR all:"world models" OR all:"vision language" OR all:"vision-language" OR all:"vision-language-action" OR all:VLA OR all:"video generation" OR all:"image generation" OR all:diffusion OR all:"flow matching")',
}

if __name__ == "__main__":
    for name, theme in THEMES.items():
        query = theme + " AND submittedDate:[202509161800 TO 202509171800]"
        url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": query, "start": 0, "max_results": 100, "sortBy": "submittedDate", "sortOrder": "ascending"})
        body, receipt = capture("DISCOVERY_" + name, url)
        print(name, receipt, flush=True)
    url = "https://export.arxiv.org/api/query?" + urlencode({"id_list": "2509.14033", "max_results": 1})
    print("arxiv-positive", capture("DISCOVERY_ARXIV_POSITIVE", url)[1], flush=True)
    query = 'doi:10.48550/arxiv.2509.14033 AND dates.date:[2025-09-16T18:00:00Z TO 2025-09-17T18:00:00Z]'
    url = "https://api.datacite.org/dois?" + urlencode({"query": query, "page[size]": 25})
    body, receipt = capture("DISCOVERY_DATACITE_POSITIVE", url)
    print("datacite-positive", receipt, flush=True)
    if receipt.get("status") == 200:
        data = json.loads(body)
        print("datacite-positive-meta", data.get("meta"), [item["id"] for item in data.get("data", [])], flush=True)
