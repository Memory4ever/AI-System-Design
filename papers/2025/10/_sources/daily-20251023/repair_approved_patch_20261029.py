"""Render literal, reader-approved PRE text as an apply_patch input; never write Books."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parents[4]
TARGETS = {
    'B1': ('B', 'books/part-03-multimodal-world-models/23-multimodal-representation.md', '稀疏编码还可以携带一份完整参考feature'),
    'B2': ('B', 'books/part-02-model/15-multi-head-attention.md', '固定总容量H之外'),
    'B3': ('B', 'books/part-01-worldview/05-what-neural-networks-learn.md', 'Jacobian-adjusted lens 一类方法提供了一个具体例子'),
    'B4': ('B', 'books/part-04-training-system/27-data.md', '若下游只消费图文配对数据'),
    'R2BC': ('R2BC', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', '另一种扩展观察分布的办法'),
    'C1': ('C', 'books/part-04-training-system/33-grpo.md', '有参考答案却没有可靠 outcome verifier 时'),
    'C2': ('C', 'books/part-07-agent/75-context.md', '### Semantic Policy 与 Recoverable Bookkeeping 应分 Owner'),
    'C3': ('C', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', '## Cache、rollback 与 exactness'),
    'C4': ('C', 'books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md', '视频的时间分块也可以不取统一长度'),
    'C5': ('C', 'books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md', '动作消费者也可以保留两份并行条件'),
    'D1': ('D', 'books/part-06-ai-infrastructure/72-security.md', '攻击档案也可先制成有限的风格参数库'),
    'D2': ('D', 'books/part-07-agent/76-rag.md', '层级索引还可由受训练的句间关系生成'),
    'D3': ('D', 'books/part-06-ai-infrastructure/72-security.md', '身份、schema 和消息签名能限制伪造'),
    'D4': ('D', 'books/part-06-ai-infrastructure/72-security.md', '### 可组合 Prompt 也是 Versioned Supply-chain Artifact'),
}

def approved(key):
    batch, target, prefix = TARGETS[key]
    name = 'REPAIR_PRE_R2BC_R1_20261029.md' if batch == 'R2BC' else f'REPAIR_PRE_BATCH_{batch}_20261029.md'
    text = (ROOT / name).read_text()
    if batch != 'R2BC':
        text = re.search(r'^## ' + re.escape(key) + r'\b.*?(?=^## [A-D][1-9]\b|\Z)', text, re.M | re.S).group()
    body = re.search(r'^#{2,3} 完整新增[^\n]*\n\n(.*?)\n\n#{2,3} 完整后邻接', text, re.M | re.S).group(1)
    note = re.search(r'^本人注：[^\n]+', text, re.M).group()
    marker = re.search(r'<!-- source-family:[^>]+-->', body).group()
    assert body.count(marker) == 1 and body.count('<!--') == 1
    return REPO / target, prefix, body, note, marker

key = sys.argv[2]
path, prefix, body, note, marker = approved(key)
current = path.read_text()
if sys.argv[1] == 'patch':
    assert marker not in current, f'{key}: body marker already present'
    assert note not in current, f'{key}: note already present'
    anchors = [line for line in current.splitlines() if line.startswith(prefix)]
    assert len(anchors) == 1, f'{key}: ambiguous/missing body anchor'
    assert current.count('\n## Review notes\n') == 1
    anchor = anchors[0]
    added = '\n'.join('+' + line for line in body.splitlines())
    print(f'*** Begin Patch\n*** Update File: {path}\n@@\n-{anchor}\n{added}\n+\n+{anchor}\n@@\n ## Review notes\n \n+{note}\n+\n*** End Patch')
elif sys.argv[1] == 'read':
    assert body in current and note in current, f'{key}: literal PRE mismatch'
    before, after = current.split(body, 1)
    paragraphs = before.strip().split('\n\n')
    if paragraphs[-1].startswith('<!--'):
        previous = '\n\n'.join(paragraphs[-2:])
    else:
        previous = paragraphs[-1]
    following = after.strip().split('\n\n')
    selected = []
    for paragraph in following:
        selected.append(paragraph)
        if not paragraph.startswith(('#', '<!--')):
            break
    note_before, note_after = current.split(note, 1)
    print(key, path, '\nFULL PREVIOUS\n', previous, '\nFULL NEW\n', body,
          '\nFULL FOLLOWING\n', '\n\n'.join(selected), '\nOWN NOTE\n', note,
          '\nNOTE BEFORE\n', note_before.strip().split('\n\n')[-1],
          '\nNOTE AFTER\n', note_after.strip().split('\n\n')[0])
else:
    raise ValueError('patch or read required')
