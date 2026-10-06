import json
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent

if __name__ == "__main__":
    for path in sorted(ROOT.glob("SUP_*.raw")):
        text = path.read_text(errors="replace")
        if not text.lstrip().startswith("<"):
            continue
        if path.name.startswith("SUP_ARXIV_") and "<feed" in text[:600]:
            continue
        soup = BeautifulSoup(text, "html.parser")
        for tag in soup(["script", "style"]):
            tag.decompose()
        (ROOT / (path.stem + ".txt")).write_text(soup.get_text("\n", strip=True) + "\n")
        links = [dict(text=a.get_text(" ", strip=True), url=a.get("href")) for a in soup.find_all("a", href=True)]
        (ROOT / (path.stem + ".links.json")).write_text(json.dumps(links, ensure_ascii=False, indent=2) + "\n")
