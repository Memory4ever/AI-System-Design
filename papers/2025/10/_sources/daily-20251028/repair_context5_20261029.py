"""Capture actual outer neighbors, including one ordered pair of new paragraphs."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
sec = 'books/part-06-ai-infrastructure/72-security.md'
ev = 'books/part-06-ai-infrastructure/66-evaluation-system.md'
specs = [
    ('I27,I28', sec, '后处理水印还需要匹配真正的检测路径'),
    ('I29', sec, '定位可疑指令还可以先分段检验'),
    ('I30', ev, '综合多份文档时，逐claim'),
    ('I31', sec, '### Training / Evaluation Environment 也是高价值生产面'),
    ('I32', ev, '### Activation Oracle 的 Confidence 也要校准'),
    ('I33', ev, '语音judge的多个维度还要先声明分值含义'),
    ('I34', ev, '把内部 sensor 展示给人后'),
    ('I35', sec, '公开语料也可以只承担最终文本的候选空间'),
    ('I36', 'books/part-03-multimodal-world-models/23-multimodal-representation.md', '对齐路径还取决于是否保留 feature 的模长'),
]
out = []
for ident, file, anchor in specs:
    blocks = (root / file).read_text().split('\n\n')
    hits = [i for i, b in enumerate(blocks) if b.startswith(anchor)]
    assert len(hits) == 1, (ident, hits)
    i = hits[0]
    j = i - 1
    while blocks[j].strip().startswith('<!--'):
        j -= 1
    k = i + 1 if blocks[i].startswith('#') else i
    out.append(dict(id=ident, file=file, insertion_before=anchor,
                    before='\n\n'.join(blocks[j:i]),
                    after='\n\n'.join(blocks[i:k+1])))
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT5_20261029.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(path)
