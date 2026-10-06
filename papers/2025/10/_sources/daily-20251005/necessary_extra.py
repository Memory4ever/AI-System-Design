"""Named safety/negative cores, not attachment traversal."""
from pathlib import Path
import subprocess
import sys
d=Path(__file__).parent
f=d.parent/"daily-20251002"/"fetch.py"
for ident in ("03636","03659","03721","03747","03598","03666"):
    subprocess.run([sys.executable,str(f),str(d),"core-2510."+ident,
                    "https://arxiv.org/html/2510."+ident+"v1"],check=True)
for n,u in {
    "pdf-2510.03913":"https://arxiv.org/pdf/2510.03913v1",
    "qwen-shared-js":"https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/80126a68.js",
    "qwen-shared2-js":"https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/4408.js",
}.items(): subprocess.run([sys.executable,str(f),str(d),n,u],check=True)
subprocess.run([sys.executable,str(f.with_name("extract.py")),
                *map(str,d.glob("core-*.raw")),*map(str,d.glob("qwen-*-js.raw"))],check=True)
