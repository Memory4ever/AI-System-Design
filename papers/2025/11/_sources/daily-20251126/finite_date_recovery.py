"""Specific date recovery and narrowed discovery; no submission/public conflation."""
import datetime as dt
import json
import pathlib
import subprocess
import urllib.parse

ROOT = pathlib.Path(__file__).parent
topics = {
    "agent-memory-tools": '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (ti:memory OR ti:"tool use" OR ti:"tool calling" OR ti:"context management") AND (all:"language model" OR all:LLM)',
    "model-learning-mechanisms": '(cat:cs.CL OR cat:cs.LG) AND (ti:"learning dynamics" OR ti:"parameter updates" OR ti:"diffusion language" OR ti:"sparse Boolean" OR ti:"module replacement")',
}
jobs = []
for name, topic in topics.items():
    params = {"search_query": topic + " AND submittedDate:[202511211900 TO 202511241900]",
              "start": 0, "max_results": 50, "sortBy": "submittedDate", "sortOrder": "descending"}
    jobs.append((name + ".xml", "https://export.arxiv.org/api/query?" + urllib.parse.urlencode(params)))
jobs += [
    ("arxiv-csDC-month-first100.html", "https://arxiv.org/list/cs.DC/2511?skip=0&show=100"),
    ("openreview-RL-SFT-note.json", "https://api2.openreview.net/notes?id=5WAGOydkNJ"),
    ("openreview-Nemotron-note.json", "https://api2.openreview.net/notes?id=KTDAbnFsQj"),
    ("gam-historical-commits.json", "https://api.github.com/repos/VectorSpaceLab/general-agentic-memory/commits?until=2025-11-26T01%3A00%3A00Z&per_page=5"),
    ("vlm-flash-historical-commits.json", "https://api.github.com/repos/snuhcs/vlm-flash/commits?until=2025-11-26T01%3A00%3A00Z&per_page=5"),
    ("hunyuan-ocr-original-readme.md", "https://raw.githubusercontent.com/Tencent-Hunyuan/HunyuanOCR/v1.0/README.md"),
    ("hunyuan-ocr-release.json", "https://api.github.com/repos/Tencent-Hunyuan/HunyuanOCR/releases?per_page=5"),
]
for name, url in jobs:
    target = ROOT / name
    run = subprocess.run(["curl", "--max-time", "18", "-L", "-sS", "-A", "Mozilla/5.0", url,
                          "-o", str(target), "-w", "%{http_code}"], capture_output=True, text=True)
    receipt = {"url": url, "executed_at": dt.datetime.now(dt.timezone.utc).isoformat(),
               "http_status": run.stdout, "exit_code": run.returncode, "error": run.stderr,
               "bytes": target.stat().st_size if target.exists() else 0,
               "stop": "one specified page; current commit metadata is not first-public proof"}
    (ROOT / (name + ".receipt.json")).write_text(json.dumps(receipt, ensure_ascii=False, indent=2))
    print(json.dumps({"file": name, **receipt}, ensure_ascii=False), flush=True)
