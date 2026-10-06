"""Exact-v1 title/abstract recovery only for related narrow-query discoveries."""
import ast
import json
import pathlib
import time

ROOT = pathlib.Path(__file__).parent
tree = ast.parse((ROOT.parent / "daily-20251127/recover_boundaries.py").read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))],
                       type_ignores=[]), "native_parser", "exec"))
excluded_titles = {"2511.21500", "2512.07865", "2511.21364", "2511.21034", "2511.20956"}
rows = {}
for path in ROOT.glob("arxiv-*-query.json"):
    for item in json.loads(path.read_text())["entries"]:
        pid = item["id"].rsplit("/", 1)[1].split("v")[0]
        if pid not in excluded_titles:
            rows[pid] = item
for pid in rows:
    if not (ROOT / ("abs-" + pid + "v1.html")).exists():
        fetch("abs-" + pid + "v1.html", "https://arxiv.org/abs/" + pid + "v1")
        time.sleep(0.5)
    if not (ROOT / ("date-" + pid + ".json")).exists():
        fetch("date-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
        time.sleep(0.5)

abstracts, dates = [], []
for pid in rows:
    path = ROOT / ("abs-" + pid + "v1.html")
    if path.exists():
        page = Page()
        page.feed(path.read_text())
        try:
            first, last = page.text.index("Title:"), page.text.index("Cite as:")
            text = "\n".join(page.text[first:last])
            abstracts.append({"id": pid + "v1", "raw": path.name, "complete_title_abstract": text,
                              "author_links": [u for u in page.links if "github.com" in u or "this http" in u]})
        except ValueError:
            abstracts.append({"id": pid + "v1", "raw": path.name, "parse_error": "missing title or citation delimiter"})
    path = ROOT / ("date-" + pid + ".json")
    if path.exists():
        try:
            value = json.loads(path.read_text())["data"]["attributes"]
            dates.append({"id": pid, **{k: value.get(k) for k in ("created", "registered", "dates")}})
        except (ValueError, KeyError):
            dates.append({"id": pid, "parse_error": "DOI response unavailable"})
(ROOT / "exact-v1-abstracts.json").write_text(json.dumps(abstracts, ensure_ascii=False, indent=2))
(ROOT / "exact-date-fields.json").write_text(json.dumps(dates, ensure_ascii=False, indent=2))
print("EXACT", len(abstracts), "DATE", len(dates), flush=True)
