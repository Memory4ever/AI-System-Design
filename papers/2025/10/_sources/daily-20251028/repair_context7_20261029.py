"""Capture the complete DP-unit to layering transition."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
file = 'books/part-06-ai-infrastructure/72-security.md'
b = (root / file).read_text().split('\n\n')
anchor = '2025 年几项工作形成了一条有价值的'
i = next(i for i, x in enumerate(b) if x.startswith(anchor))
j = i - 1
while b[j].strip().startswith('<!--'):
    j -= 1
row = dict(id='I50', file=file, insertion_before=anchor,
           before='\n\n'.join(b[j:i]), after='\n\n'.join(b[i:i+2]))
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT7_20261029.json')
path.write_text(json.dumps([row], ensure_ascii=False, indent=2))
print(row['before']+'\n\n'+row['after'])
