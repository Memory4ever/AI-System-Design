"""Retrieve bounded thematic discovery; submission dates do not establish publication."""
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

directory = Path(sys.argv[1])
day = sys.argv[2]
fetch = Path(__file__).parents[0].parent / "daily-20251002" / "fetch.py"
topics = {
    "model": '(cat:cs.CL OR cat:cs.LG) AND (ti:"language model" OR ti:LLM OR ti:transformer OR ti:"mixture of experts") AND (all:architecture OR all:optimization OR all:training OR all:reasoning)',
    "systems": '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.LG) AND (all:"language model" OR all:LLM OR all:transformer) AND (ti:GPU OR ti:kernel OR ti:parallel OR ti:serving OR ti:inference OR ti:quantization OR ti:cache OR ti:communication)',
    "agent": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA OR cat:cs.CL) AND (all:"language model" OR all:LLM) AND (ti:agent OR ti:RAG OR ti:retrieval OR ti:memory OR ti:tool OR ti:planning)',
    "multimodal": '(cat:cs.CV OR cat:cs.RO OR cat:cs.CL OR cat:cs.LG) AND (ti:"vision language" OR ti:"vision-language" OR ti:VLA OR ti:"world model" OR ti:"multimodal language" OR ti:"diffusion model")',
}
for name, topic in topics.items():
    query = f'submittedDate:[{day}0000 TO {day}2359] AND ({topic})'
    url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": query, "start": 0, "max_results": 40, "sortBy": "submittedDate", "sortOrder": "ascending"})
    subprocess.run([sys.executable, str(fetch), str(directory), "arxiv-" + name, url], check=True)
