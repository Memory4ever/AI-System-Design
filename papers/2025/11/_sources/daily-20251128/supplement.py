"""Named Nov28 official boundaries and five title-triggered DC supplements."""
import ast
import pathlib
ROOT = pathlib.Path(__file__).parent
tree = ast.parse((ROOT.parent / "daily-20251127/recover_boundaries.py").read_text())
exec(compile(ast.Module(body=[n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.ClassDef))],
                       type_ignores=[]), "native_parser", "exec"))
for name, url in (
    ("ernie-page2.html", "https://ernie.baidu.com/blog/zh/page/2/"),
    ("minimax-index.txt", "https://agent.minimax.io/docs/llms.txt"),
    ("google-gemini-dev.html", "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-3-developers/"),
    ("google-image-verification.html", "https://blog.google/products/gemini/ai-image-verification/"),
    ("qwen-tts1128.html", "https://qwen.ai/blog?id=qwen3-tts-1128"),
):
    fetch(name, url)
for pid in ("2511.20834", "2511.20975", "2511.21413", "2511.21431", "2511.21661"):
    fetch("abs-" + pid + "v1.html", "https://arxiv.org/abs/" + pid + "v1")
    fetch("date-" + pid + ".json", "https://api.datacite.org/dois/10.48550/arXiv." + pid)
