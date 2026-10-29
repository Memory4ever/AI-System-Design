"""Capture complete immediate paragraphs for the third narrow proposal."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
specs = [
    ('I13', 'books/part-02-model/20-sampling.md', '### Test-time Budget'),
    ('I14', 'books/part-02-model/20-sampling.md', '多条候选也不必等到完整生成后才比较'),
    ('I15', 'books/part-04-training-system/28-pretraining.md', '成对有限差分之外'),
    ('I16', 'books/part-07-agent/76-rag.md', '回答与引用评价还要声明'),
    ('I17', 'books/part-07-agent/82-multi-agent.md', '多Agent的多样性还可能服务于代表一份给定人群'),
    ('I18', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', '视频示教的目标也不必全部恢复成同一种三维状态'),
    ('I19', 'books/part-04-training-system/33-grpo.md', '连续flow的训练还可以把探索预算前移'),
    ('I20', 'books/part-03-multimodal-world-models/23-multimodal-representation.md', '表示域改变时'),
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
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT3_20261029.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(path)
