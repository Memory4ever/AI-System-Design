"""Mechanical exact-v1 PDF extraction; scoped to this day's named IDs."""
import pathlib
import sys
from pypdf import PdfReader

root = pathlib.Path(__file__).resolve().parent
for identity in sys.argv[1].split(','):
    source = root / f'V3_CORE_2602.{identity}.pdf'
    pages = PdfReader(source).pages
    text = '\n\n'.join(f'[PAGE {i + 1}]\n{page.extract_text()}' for i, page in enumerate(pages))
    (root / f'V3_PDF_2602.{identity}.txt').write_text(text + '\n')
    print(identity, len(pages), len(text))
