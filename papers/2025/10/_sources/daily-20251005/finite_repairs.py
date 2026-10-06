"""Own-day metadata-only title supplements and ordinary source repairs."""
from pathlib import Path
import subprocess
import sys
from urllib.parse import urlencode

d = Path(__file__).parent
f = d.parent / "daily-20251002" / "fetch.py"
def get(n, u):
    subprocess.run([sys.executable, str(f), str(d), n, u], check=True)
for c in ("cs.CL", "cs.CV", "cs.DC", "cs.PL", "cs.IR"):
    q = 'submittedDate:[202510040000 TO 202510042359] AND cat:'+c
    get("dated-titles-"+c, "https://export.arxiv.org/api/query?"+urlencode({"search_query":q,"start":0,"max_results":25,"sortBy":"submittedDate","sortOrder":"ascending"}))
for n,u in {
    "qwen-home-js":"https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_home-index.js",
    "qwen-main-js":"https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/main.js",
    "google-pubs-page2":"https://research.google/pubs/?search=language%20model&category=2025&page=2",
    "pdf-2510.03815":"https://arxiv.org/pdf/2510.03815v1",
    "pdf-2510.03859":"https://arxiv.org/pdf/2510.03859v1",
}.items(): get(n,u)
subprocess.run([sys.executable, str(f.with_name("extract.py")),
                *map(str,d.glob("dated-titles-*.raw")), *map(str,d.glob("qwen-*-js.raw")),
                str(d/"google-pubs-page2.raw")], check=True)
