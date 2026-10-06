"""Mechanical text extraction; never synthesizes source text or dates."""
import html
import re
import sys
from pathlib import Path

for name in sys.argv[1:]:
    p = Path(name)
    if p.suffix == '.pdf':
        from pypdf import PdfReader
        text = '\n'.join(f'\n[PDF page {i + 1}]\n' + page.extract_text() for i, page in enumerate(PdfReader(p).pages))
    else:
        text = p.read_text()
        text = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', text, flags=re.S)
        text = re.sub(r'</(?:p|div|h[1-6]|tr|li|section)>', '\n', text)
        text = html.unescape(re.sub(r'<[^>]+>', ' ', text))
        text = '\n'.join(re.sub(r'\s+', ' ', line).strip() for line in text.splitlines() if line.strip())
    target = p.with_suffix('.pdf.txt') if p.suffix == '.pdf' else p.with_suffix('.txt')
    target.write_text(text)
