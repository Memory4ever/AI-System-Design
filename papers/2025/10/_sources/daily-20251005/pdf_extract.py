"""Mechanical extraction of two necessary PDF originals; not a read receipt."""
from pathlib import Path
from pypdf import PdfReader

d = Path(__file__).parent
for ident in ("2510.03815", "2510.03859", "2510.03913"):
    r = PdfReader(str(d/("pdf-"+ident+".raw")))
    text = "\n".join("\nPAGE "+str(i+1)+"\n"+(p.extract_text() or "")
                     for i,p in enumerate(r.pages))
    (d/("pdf-"+ident+".text.txt")).write_text(text)
