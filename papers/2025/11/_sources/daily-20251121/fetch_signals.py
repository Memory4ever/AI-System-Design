"""Fetch only explicit admitted-potential identities for current-page signals."""
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
ids = "15709 16035 16054 16147 16275 16324 16331 16122 15898 15690 15503 16046 15950 15757 15203 21726 16108 15915 16449 16203 16233 16175 16166 15605 16599 16156 16652 16520 16654 16540 15389 15192".split()
for suffix in ids:
    name = f"signal_2511.{suffix}.html"
    if (root / name).exists():
        print(f"Already stored: {name}", flush=True)
        continue
    subprocess.run([sys.executable, str(root / "fetch_raw.py"), name,
                    f"https://arxiv.org/abs/2511.{suffix}"], check=True)
