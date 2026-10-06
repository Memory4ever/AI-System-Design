"""Exact-v1 abstracts for remaining related narrow-query discoveries, not full texts."""
import ast
import json
import pathlib
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).parent
tree = ast.parse((ROOT / "recover_boundaries.py").read_text())
tree.body = [node for node in tree.body if isinstance(
    node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))]
helpers = {"ROOT": ROOT}
exec(compile(tree, "parser_definitions", "exec"), helpers)
known = {p.name[5:-5] for p in ROOT.glob("date-*.json") if "receipt" not in p.name}
known.add("2511.20636")
skip = ("MoRE:", "Frailty-Aware", "Depression Detection", "Medical Error",
        "Materials Science", "Alzheimer", "Medical Vision", "PET/CT", "Leaf Area",
        "Medical Image", "Histological", "Fast MRI", "Qualitative Laboratory")
seen = set()
ns = {"a": "http://www.w3.org/2005/Atom"}
records = []
for path in sorted(ROOT.glob("arxiv-*-page0.xml")):
    for entry in ET.parse(path).findall("a:entry", ns):
        pid = entry.findtext("a:id", namespaces=ns).rsplit("/", 1)[-1].split("v")[0]
        title = entry.findtext("a:title", namespaces=ns).replace("\n", " ")
        if pid in known or pid in seen or any(term in title for term in skip):
            continue
        seen.add(pid)
        target = helpers["fetch"]("abs-" + pid + "v1.html", "https://arxiv.org/abs/" + pid + "v1")
        if target:
            page = helpers["Page"]()
            page.feed(target.read_text())
            start = page.text.index("Abstract:") + 1
            end = page.text.index("Subjects:", start)
            records.append({"id": pid, "title": title, "abstract": " ".join(page.text[start:end]),
                            "history": page.text[page.text.index("Submission history"):page.text.index("Full-text links:")]})
        date = helpers["fetch"]("date-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
        if date:
            value = json.loads(date.read_text())["data"]["attributes"]
            print(pid, json.dumps({key: value.get(key) for key in ("created", "registered", "dates")}), flush=True)
(ROOT / "remaining-exact-v1-abstracts.json").write_text(json.dumps(records, ensure_ascii=False, indent=2))
print("Exact-v1 abstract records", len(records), flush=True)
