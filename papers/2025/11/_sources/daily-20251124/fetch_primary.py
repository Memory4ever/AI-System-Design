"""Capture this day's selected URLs; reuse only the local capture utility."""

import importlib.util
import json
import sys
from pathlib import Path

root = Path(__file__).parent
utility = root.parent / "daily-20251123" / "fetch_primary.py"
spec = importlib.util.spec_from_file_location("primary_capture", utility)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
module.root = root
fetch = module.fetch

if __name__ == "__main__":
    fetch(sys.argv[1], sys.argv[2], json.loads(sys.argv[3]) if len(sys.argv) > 3 else None)
