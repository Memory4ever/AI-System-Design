"""Capture precise outer neighbors for the thirteen R25-supported proposals."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
mm = 'books/part-03-multimodal-world-models/'
tr = 'books/part-04-training-system/'
specs = [
    ('I37', mm+'26-multimodal-embodied-vla.md', '当交互还取决于两个物体的功能面时'),
    ('I38', 'books/part-02-model/20-sampling.md', '## EOS、停止条件和最大长度'),
    ('I39', tr+'31-rlhf.md', '聚合之前还要问判据从哪里来'),
    ('I40', tr+'27-data.md', '扩大生成器之前，还可以先改善它怎样学习生成'),
    ('I41', tr+'30-lora.md', '实际输入二阶矩的校准人口还可以由各specialist'),
    ('I42', mm+'25-multimodal-world-models.md', '校准环境也可直接以真实任务回报选择simulator参数'),
    ('I43', mm+'26-multimodal-embodied-vla.md', '已给定的形式约束还可以进入轨迹生成器'),
    ('I44', tr+'28-pretraining.md', 'Momentum随后还要经过近似polar map'),
    ('I45', tr+'30-lora.md', '因子生成器还可读取当前条件'),
    ('I46', mm+'25-multimodal-world-models.md', '### World Model 不必保存全部 Observation'),
    ('I47', mm+'24-multimodal-generative-paradigms.md', '对于逐帧视频，条件 c 的历史部分'),
    ('I48', 'books/part-07-agent/81-workflow.md', '这条路线的第一性约束是'),
    ('I49', mm+'24-multimodal-generative-paradigms.md', '对象集合的生成也可以让不同语义角色承受不同噪声'),
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
    if ident == 'I38':
        j = i - 4
    k = i + 1 if blocks[i].startswith('#') else i
    if ident == 'I48':
        k = i + 1
    out.append(dict(id=ident, file=file, insertion_before=anchor,
                    before='\n\n'.join(blocks[j:i]),
                    after='\n\n'.join(blocks[i:k+1])))
path = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT6_20261029.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(path)
