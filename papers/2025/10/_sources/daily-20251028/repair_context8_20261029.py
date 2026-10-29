"""Capture only the nine reader-identified insertion neighborhoods."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
specs = [
    ('I51', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', '<!-- semantic-body-binding:SF-2026-ARXIV-2605-11311:start -->', 1, 2),
    ('I52', 'books/part-03-multimodal-world-models/25-multimodal-world-models.md', '隐状态估计也可以只替换滤波器的预测模型', 0, 1),
    ('I53', 'books/part-06-ai-infrastructure/66-evaluation-system.md', '安全干预评价不能只测无cue的标准提示', 0, 2),
    ('I54', 'books/part-05-inference-system/49-tensorrt-llm.md', '<!-- semantic-body-binding:SF-2026-ARXIV-2605-20706:start -->', 0, 1),
    ('I55', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', '若样本各坐标必须严格为正', 0, 1),
    ('I56', 'books/part-04-training-system/27-data.md', '在线选择也可以让视觉语言 teacher', 0, 2),
    ('I57', 'books/part-03-multimodal-world-models/23-multimodal-representation.md', '局部概念的读出还取决于隔离发生在哪一层', 1, 1),
    ('I58', 'books/part-06-ai-infrastructure/66-evaluation-system.md', '修复型Agent的目标检测器', 1, 1),
    ('I59', 'books/part-04-training-system/33-grpo.md', '重放也可以先按题保存自己产生的成功轨迹', 1, 3),
]
rows = []
for ident, file, anchor, extra_before, after_blocks in specs:
    blocks = (root / file).read_text().split('\n\n')
    hits = [i for i, b in enumerate(blocks) if b.startswith(anchor)]
    assert len(hits) == 1, (ident, hits)
    i = hits[0]
    j = i - 1
    while blocks[j].strip().startswith('<!--'):
        j -= 1
    rows.append(dict(id=ident, file=file, insertion_before=anchor,
                     before='\n\n'.join(blocks[j-extra_before:i]),
                     after='\n\n'.join(blocks[i:i+after_blocks])))
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT8_20261029.json')
path.write_text(json.dumps(rows, ensure_ascii=False, indent=2))
print('Captured nine complete neighborhoods:', [r['id'] for r in rows])
