"""Fetch finite exact-v1 sections needed for safety, counterevidence or scope."""
from pathlib import Path
import subprocess
import sys

d = Path(__file__).parent
fetch = d.parent / "daily-20251002" / "fetch.py"
ids = "03984 03992 03993 03999 04013 04019 04020 04023 04031 04032 04041 04045 04058 04067 04071 04081 04120 04142 04145 04212 04214 04226 04234 04257 04284 04303 04311 04317 04340 04347 04365 04371 04392 05173 05179 08595".split()
for suffix in ids:
    ident = "2510." + suffix
    subprocess.run([sys.executable, str(fetch), str(d), "core-" + ident,
                    "https://arxiv.org/html/" + ident + "v1"], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")),
                *map(str, d.glob("core-*.raw"))], check=True)
