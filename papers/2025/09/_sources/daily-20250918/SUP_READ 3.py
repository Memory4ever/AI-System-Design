import argparse
import pathlib

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("file")
parser.add_argument("selectors", nargs="*", default=[".ltx_abstract"])
args = parser.parse_args()
soup = BeautifulSoup(pathlib.Path(args.file).read_text(), "html.parser")
for selector in args.selectors:
    nodes = soup.select(selector)
    for node in nodes:
        print("\n### " + selector + "\n" + node.get_text(" ", strip=True))
