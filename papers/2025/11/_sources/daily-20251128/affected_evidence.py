"""Finite affected safety/counterevidence and named author date recovery."""
import ast
import pathlib
ROOT = pathlib.Path(__file__).parent
tree = ast.parse((ROOT.parent / "daily-20251127/recover_boundaries.py").read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))],
                       type_ignores=[]), "native_parser", "exec"))
for pid in ("2511.20799", "2511.21192", "2511.21663", "2512.07850", "2511.20795", "2511.21397", "2511.21437", "2511.21033", "2512.22125", "2511.21661"):
    fetch("core-" + pid + "v1.html", "https://arxiv.org/html/" + pid + "v1")
for name, url in (
    ("mlpmoe-gist.json", "https://api.github.com/gists/fc2ef1eddf226ca7814f9e5e2ae9bad1"),
    ("structured-helm-pr.json", "https://api.github.com/repos/stanford-crfm/helm/pulls/3893"),
    ("structured-repo.json", "https://api.github.com/repos/StanfordMIMI/dspy-helm"),
):
    fetch(name, url)
for pid in ("2511.21104", "2511.21663"):
    fetch("date-retry-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
