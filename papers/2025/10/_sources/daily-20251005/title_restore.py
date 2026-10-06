"""Only named relevant titles from the bounded own-day metadata supplement."""
from pathlib import Path
import subprocess
import sys

d = Path(__file__).parent
f = d.parent / "daily-20251002" / "fetch.py"
ids = ("03584", "03595", "03598", "03608", "03636", "03659", "03669",
       "03706", "03721", "03731", "03747", "03762", "03763", "03799",
       "03872", "03891", "05164", "06254")
for ident in ids:
    subprocess.run([sys.executable, str(f), str(d), "abs-2510."+ident,
                    "https://arxiv.org/abs/2510."+ident+"v1"], check=True)
for n,u in {
    "qwen-research-js":"https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_research-index.js",
    "google-pubs-page3":"https://research.google/pubs/?search=language%20model&category=2025&page=3",
}.items(): subprocess.run([sys.executable,str(f),str(d),n,u],check=True)
subprocess.run([sys.executable,str(f.with_name("extract.py")),
                *map(str,d.glob("abs-*.raw")),str(d/"google-pubs-page3.raw"),str(d/"qwen-research-js.raw")],check=True)
