"""Fetch exact versions for finite safety and design-counterevidence checks."""
from pathlib import Path
import subprocess
import sys

directory = Path(sys.argv[1])
fetch = Path(__file__).parent.parent / "daily-20251002" / "fetch.py"
ids = sys.argv[2:]
for identity in ids:
    subprocess.run([sys.executable, str(fetch), str(directory), "core-" + identity, "https://arxiv.org/html/" + identity], check=True)
subprocess.run([sys.executable, str(fetch.with_name("extract.py")), *map(str, directory.glob("core-*.raw"))], check=True)
