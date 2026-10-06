"""Inspect only this research page's own client bundles for its list endpoint."""
from pathlib import Path
import re
import subprocess
import sys

directory = Path(sys.argv[1])
fetch = Path(__file__).parent.parent / "daily-20251002" / "fetch.py"
html = (directory / "anthropic-research.raw").read_text()
for index, url in enumerate(re.findall(r'<script[^>]+src="([^"]+)"', html)):
    subprocess.run([sys.executable, str(fetch), str(directory),
                    "anthropic-bundle-" + str(index), "https://www.anthropic.com" + url], check=True)
