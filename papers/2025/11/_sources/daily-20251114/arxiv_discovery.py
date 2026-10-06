"""Bounded title-theme discovery; submission fields are not public dates."""

import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlencode

root = Path(__file__).parent
categories = "(cat:cs.CL OR cat:cs.LG OR cat:cs.AI OR cat:cs.DC OR cat:cs.CV OR cat:cs.RO OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.IR OR cat:cs.MA)"
dates = "submittedDate:[20251111190000 TO 20251112185959]"
themes = {
    "model-training": '(ti:"language model" OR ti:transformer OR ti:"mixture of experts" OR ti:pretraining OR ti:"reinforcement learning" OR ti:distillation OR ti:"reward model")',
    "model-training-narrow": '(ti:"language model" OR ti:"mixture of experts" OR ti:"reward model" OR ((ti:transformer OR ti:pretraining OR ti:"reinforcement learning" OR ti:distillation) AND (all:"large language" OR all:"foundation model" OR all:"vision-language" OR all:"diffusion model")))',
    "inference-system": '(ti:"LLM inference" OR ti:"language model serving" OR ti:"speculative decoding" OR ti:"KV cache" OR ti:"GPU kernel" OR ti:"GPU communication" OR ti:"tensor parallel" OR ti:"pipeline parallel")',
    "agent-context": '(ti:"LLM agent" OR ti:"language agent" OR ti:"retrieval augmented" OR ti:"retrieval-augmented" OR ti:"agent memory" OR ti:"multi-agent" OR ti:"tool calling")',
    "multimodal-world": '(ti:"vision-language" OR ti:"vision language" OR ti:"world model" OR ti:"video generation" OR ti:"diffusion transformer" OR ti:"vision-language-action" OR ti:"multimodal foundation")',
}
for name, theme in themes.items():
    if len(sys.argv) > 1 and name not in sys.argv[1:]:
        continue
    query = f"{categories} AND {dates} AND {theme}"
    url = "https://export.arxiv.org/api/query?" + urlencode({"search_query": query, "start": 0, "max_results": 100, "sortBy": "submittedDate", "sortOrder": "ascending"})
    print(json.dumps({"name": name, "query": query, "start": 0, "max_results": 100}), flush=True)
    subprocess.run([sys.executable, str(root / "fetch_raw.py"), f"raw-arxiv-{name}-p0.xml", url], check=True)
