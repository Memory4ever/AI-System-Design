"""Necessary bounded safety/correction cores, not the full title inventory."""
from pathlib import Path
import subprocess
import sys

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
for short in ["04401", "04477", "04514", "04533", "04547", "04587", "04633", "04773", "05024", "05087", "05288", "05364"]:
    identity = "2510." + short + "v1"
    subprocess.run([sys.executable, str(fetch), str(d), "core-" + identity, "https://arxiv.org/html/" + identity], check=True)
subprocess.run([sys.executable, str(fetch), str(d), "petri-technical", "https://alignment.anthropic.com/2025/petri"], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, d.glob("core-*.raw")), str(d / "petri-technical.raw")], check=True)
