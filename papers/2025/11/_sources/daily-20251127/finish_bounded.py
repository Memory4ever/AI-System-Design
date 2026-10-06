"""Named Nov27 recovery, using local parsers without rerunning earlier requests."""
import ast
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
tree = ast.parse((ROOT / "recover_boundaries.py").read_text())
tree.body = [node for node in tree.body if isinstance(
    node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))]
helpers = {"ROOT": ROOT}
exec(compile(tree, "local_parser_definitions", "exec"), helpers)

for name, url in (
    ("deepmind-real-page4.html", "https://deepmind.google/blog/page/4/"),
    ("deepmind-real-page5.html", "https://deepmind.google/blog/page/5/"),
    ("arxiv-csDC-tail-titles.html", "https://arxiv.org/list/cs.DC/2025-11?skip=200&show=50"),
    ("da3-window-readme-commits.json", "https://api.github.com/repos/ByteDance-Seed/Depth-Anything-3/commits?path=README.md&since=2025-11-26T01:00:00Z&until=2025-11-27T01:00:00Z&per_page=10"),
):
    target = helpers["fetch"](name, url)
    if target and name.endswith(".html"):
        page = helpers["Page"]()
        page.feed(target.read_text())
        metadata = {"text": page.text, "links": page.links}
        (ROOT / (name + ".metadata.json")).write_text(json.dumps(metadata, ensure_ascii=False, indent=2))
        print(name, json.dumps(page.text[-180:], ensure_ascii=False), flush=True)

for pid in ("2511.20182", "2511.20644", "2511.20439", "2511.20095", "2511.19878",
            "2511.19861", "2511.19676", "2511.20710", "2511.20737"):
    target = helpers["fetch"]("date-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
    if target:
        value = json.loads(target.read_text())["data"]["attributes"]
        print(pid, json.dumps({key: value.get(key) for key in ("created", "registered", "dates")}), flush=True)
