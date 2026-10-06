"""Print exact-v1 abstracts for bounded, identified research leads."""

import importlib.util
import pathlib
import sys

source = pathlib.Path(__file__).parents[1] / "daily-20251217" / "fetch_sources.py"
spec = importlib.util.spec_from_file_location("retrieval", source)
retrieval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retrieval)

for identity in sys.argv[1:]:
    try:
        root = retrieval.get("https://arxiv.org/abs/" + identity + "v1")
        titles = root.find(lambda n: n.tag == "h1" and retrieval.cls(n, "title"))
        abstracts = root.find(lambda n: n.tag == "blockquote" and retrieval.cls(n, "abstract"))
        print(identity, titles[0].text() if titles else "TITLE_MISSING", flush=True)
        print(abstracts[0].text() if abstracts else "ABSTRACT_MISSING", flush=True)
    except Exception as error:
        print(identity, type(error).__name__, str(error), flush=True)
