"""Retrieve only identified safety/negative or admission-disambiguation cores."""
from pathlib import Path
import subprocess
import sys

d = Path(sys.argv[1])
fetch = Path(__file__).parent.parent / "daily-20251002" / "fetch.py"
ids = ["2510.05156","2510.02677","2510.02803","2510.02780","2510.02837",
       "2510.03204","2510.03217","2510.02967","2510.02922","2510.03520",
       "2510.03469","2510.03366","2510.03120","2510.03490","2510.03174",
       "2510.03194","2510.03521"]
for identity in ids:
    subprocess.run([sys.executable,str(fetch),str(d),"core-"+identity+"v1",
                    "https://arxiv.org/html/"+identity+"v1"],check=True)
subprocess.run([sys.executable,str(fetch.with_name("extract.py")),*map(str,d.glob("core-*.raw"))],check=True)
