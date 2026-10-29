"""Capture complete neighboring paragraphs for the precise four PRE slots."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[5]
specs = [
    ('I1', 'books/part-02-model/22-long-context.md', '这条路线降低 selector 与 gather', '无法继续训练模型时'),
    ('I2', 'books/part-02-model/22-long-context.md', '[RNN 深度的受限理论与实验]', '固定状态宽度后，cell 内部仍有一项选择'),
    ('I3', 'books/part-04-training-system/31-rlhf.md', '安全训练还可改变哪些请求', '训练时要求模型先完成结构化中间任务'),
    ('I4', 'books/part-06-ai-infrastructure/66-evaluation-system.md', '回答筛选应将 score 学习', '比较confidence之前'),
]
result = []
for ident, file, before, after in specs:
    text = (root / file).read_text()
    start = text.index(before)
    end = text.index(after, start)
    after_end = text.find('\n\n', end)
    result.append({'id': ident, 'file': file, 'complete_before_and_after': text[start:after_end],
                   'insertion_before': after})
out = Path(__file__).with_name('REPAIR_BOOKS_CONTEXT_20261029.json')
out.write_text(json.dumps(result, ensure_ascii=False, indent=2))
print(out)
