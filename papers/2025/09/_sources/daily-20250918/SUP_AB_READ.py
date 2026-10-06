import argparse
import ast
import json
import pathlib

from bs4 import BeautifulSoup
ROOT = pathlib.Path(__file__).resolve().parent

parser = argparse.ArgumentParser()
parser.add_argument("start", type=int)
parser.add_argument("end", type=int)
args = parser.parse_args()
discovery = json.loads((ROOT / "SUP_DISCOVERY.json").read_text())
selected = json.loads((ROOT / "SUP_SELECTED.json").read_text()) if (ROOT / "SUP_SELECTED.json").exists() else []
if not selected:
    module = ast.parse((ROOT / "SUP_AB_CAPTURE.py").read_text())
    values = next(node.value.func.value.value.split() for node in module.body
                  if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
                  and node.targets[0].id == "SELECTED")
    selected = [k for k in discovery if k[5:10] in values]
for index, identity in enumerate(selected[args.start:args.end], args.start):
    base = identity.split("v")[0]
    file = ROOT / (("SUP_AB_" if identity.endswith("v1") else "SUP_V1AB_") + base + ".raw")
    soup = BeautifulSoup(file.read_bytes() if file.exists() else b"", "html.parser")
    ab = soup.select_one(".abstract")
    title = soup.select_one(".title")
    print("\n" + str(index) + " " + base + "v1 " + (title.get_text(" ", strip=True) if title else "NO_TITLE"))
    if ab:
        print(ab.get_text(" ", strip=True))
    elif identity.endswith("v1"):
        print("OFFICIAL_ATOM_CURRENT_ONLY_V1 " + discovery[identity]["title"])
        print(discovery[identity]["summary"])
    else:
        print("NO_AB: exact v1 alternate remains necessary")
