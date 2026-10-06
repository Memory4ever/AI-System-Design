"""Finite necessary safety/correctness/negative evidence and title-route repair."""
from pathlib import Path
import subprocess
import sys

d = Path(__file__).parent
f = d.parent / "daily-20251002" / "fetch.py"
for c in ("cs.CL", "cs.CV", "cs.DC", "cs.PL", "cs.IR"):
    subprocess.run([sys.executable, str(f), str(d), "titles-fixed-"+c,
                    "https://arxiv.org/list/"+c+"/2025-10?skip=0&show=25"], check=True)
for ident in ("2510.03588", "2510.03611", "2510.03612", "2510.03760",
              "2510.03795", "2510.03805", "2510.03827", "2510.03840",
              "2510.03865", "2510.03879"):
    subprocess.run([sys.executable, str(f), str(d), "core-"+ident,
                    "https://arxiv.org/html/"+ident+"v1"], check=True)
subprocess.run([sys.executable, str(f.with_name("extract.py")),
                *map(str, d.glob("titles-fixed-*.raw")), *map(str, d.glob("core-*.raw"))], check=True)
