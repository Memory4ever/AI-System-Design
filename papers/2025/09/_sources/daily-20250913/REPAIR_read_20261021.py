"""Read captured local primary HTML by explicit paragraph ranges or table IDs."""
from pathlib import Path
import sys

from SUP_inspect_20261012 import Page
from SUP_tree_20261012 import Tree


source = (Path(__file__).parent / sys.argv[1]).read_text()
if sys.argv[2] == "tables":
    for node in Tree(source).root.all("table"):
        if len(sys.argv) == 3 or any(key in node.attrs.get("id", "") for key in sys.argv[3:]):
            print(node.attrs, node.text())
elif sys.argv[2] == "abs":
    root = Tree(source).root
    for node in root.all():
        if node.tag in ("h1", "blockquote") or node.attrs.get("class") in ("submission-history", "comments", "dateline"):
            print(node.tag, node.attrs, node.text())
else:
    page = Page()
    page.feed(source)
    for part in sys.argv[2:]:
        low, high = map(int, part.split("-"))
        for i in range(low, min(high + 1, len(page.paragraphs))):
            print(i, page.paragraphs[i])
