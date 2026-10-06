"""Finite date recovery for the eleven explicitly selected title/abstract records."""
import json
import pathlib
import subprocess
import sys

root = pathlib.Path(__file__).parent
identities = ["2511.13091", "2511.12728", "2511.13368", "2511.12828", "2511.12609",
              "2511.12997", "2511.12928", "2511.12860", "2511.12573", "2511.13646"]
for identity in identities:
    name = identity + "_datacite.json"
    subprocess.run([sys.executable, str(root / "fetch_raw.py"), name,
                    "https://api.datacite.org/dois/10.48550/arxiv." + identity], check=True)
    raw = json.loads((root / name).read_text())
    attributes = raw.get("data", {}).get("attributes", {})
    print(identity, json.dumps({key: attributes.get(key) for key in
                               ["created", "registered", "dates", "state"]}), flush=True)
