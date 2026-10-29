"""Capture complete immediate paragraphs for six final writer-owned gaps."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
gen = 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md'
specs = [
    ('I21', gen, '一步运行也不必只有一个固定的质量工作点'),
    ('I22', 'books/part-07-agent/80-reflection.md', '## Feedback 来源决定价值'),
    ('I23', gen, '可微视频反馈还要核实评价者究竟看到了什么'),
    ('I24', 'books/part-04-training-system/29-sft.md', 'Student也可由可执行程序与学习路由共同组成'),
    ('I25', gen, '并行位置还可先按外部目标分组'),
    ('I26', gen, '### Metric-geometry Reward'),
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
    if ident == 'I22':
        k = i + 3
    out.append(dict(id=ident, file=file, insertion_before=anchor,
                    before='\n\n'.join(blocks[j:i]),
                    after='\n\n'.join(blocks[i:k+1])))
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT4_20261029.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(path)
