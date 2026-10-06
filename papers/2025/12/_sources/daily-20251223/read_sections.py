"""Read explicitly selected exact-version HTML sections, without full-text copies."""

import importlib.util
import pathlib
import sys

source = pathlib.Path(__file__).parents[1] / "daily-20251217" / "fetch_sources.py"
spec = importlib.util.spec_from_file_location("retrieval", source)
retrieval = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retrieval)
identity, *selected = sys.argv[1:]
identities = selected if identity == "list" else [identity]
for identity in identities:
    print(identity, flush=True)
    try:
        root = retrieval.get("https://arxiv.org/html/" + identity + "v1")
        if sys.argv[1] == "list" or not selected:
            for node in root.find(lambda n: n.tag == "section"):
                headings = node.find(lambda n: n.tag in ("h2", "h3", "h4"))
                if headings:
                    print(node.attrs.get("id", ""), headings[0].text(), flush=True)
        else:
            for section in selected:
                for node in root.find(lambda n: n.attrs.get("id") == section):
                    print(section, node.text(), flush=True)
    except Exception as error:
        print(type(error).__name__, str(error), flush=True)
