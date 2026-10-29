import sys
from pathlib import Path

from bs4 import BeautifulSoup

path = Path(__file__).resolve().parent / sys.argv[1]
soup = BeautifulSoup(path.read_text(), "html.parser")
for identifier in sys.argv[2:]:
    section = soup.find("section", id=identifier)
    if section is None:
        raise ValueError(identifier)
    print(identifier, section.get_text(" ", strip=True), "\n")
