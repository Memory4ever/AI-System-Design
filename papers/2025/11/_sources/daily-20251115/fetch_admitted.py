"""Capture only the exact-v1 families admitted by the dated-list review."""

import subprocess
import sys
from pathlib import Path

fetch = str(Path(__file__).with_name("fetch_raw.py"))
for suffix in ["10643", "10621", "10507", "10457", "10381", "10303",
               "10262", "10232", "10201", "10051", "10029", "09971", "09966"]:
    subprocess.run([sys.executable, fetch, "raw-v1-" + suffix + ".html",
                    "https://arxiv.org/html/2511." + suffix + "v1"], check=True)
