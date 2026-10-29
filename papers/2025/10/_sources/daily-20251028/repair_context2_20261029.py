"""Capture actual complete paragraphs surrounding the eight proposed narrow slots."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
specs = [
    ('I5', 'books/part-07-agent/74-prompt.md', '**Schema**'),
    ('I6', 'books/part-06-ai-infrastructure/66-evaluation-system.md', '同一题的重复评分还可先保留有限类别计数'),
    ('I7', 'books/part-05-inference-system/54-gpu-memory.md', '串行多阶段生成还须分别核容量'),
    ('I8', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', '有限动作词库还可先把'),
    ('I9', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', '### Velocity 目标的混合表示'),
    ('I10', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md', '显式物理模型的辨识成本还可分成'),
    ('I11', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', '#### Guidance 可以前移到 Prior'),
    ('I12', 'books/part-02-model/15-multi-head-attention.md', '## 为什么 head 数不是越多越好'),
]
out = []
for ident, file, anchor in specs:
    t = (root / file).read_text()
    blocks = t.split('\n\n')
    index = next(i for i, b in enumerate(blocks) if b.startswith(anchor))
    first = index - 1
    while blocks[first].strip().startswith('<!--'):
        first -= 1
    last = index + 1 if blocks[index].startswith('#') else index
    out.append({'id': ident, 'file': file, 'insertion_before': anchor,
                'before': '\n\n'.join(blocks[first:index]),
                'after': '\n\n'.join(blocks[index:last+1])})
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT2_20261029.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(path)
