# 2026-05-21 Root Books Writeback Receipt

状态：39 项共享 Books 写回已完成，等待不同智能体进行 fresh non-author 语义与最终 Gate 复核。

## 写回范围

- `books/part-01-worldview/07-scaling-law.md`: 2605.20196
- `books/part-01-worldview/08-why-llms-show-intelligence.md`: 2605.21488
- `books/part-02-model/14-self-attention.md`: 2605.21070
- `books/part-02-model/17-transformer-layer.md`: 2605.20289
- `books/part-02-model/21-moe.md`: 2605.20948
- `books/part-02-model/22-long-context.md`: 2605.20813
- `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`: 2605.20187、2605.20199、2605.20235、2605.20547、2605.20946
- `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`: 2605.20811、2605.20894
- `books/part-04-training-system/27-data.md`: 2605.20602、2605.20876
- `books/part-04-training-system/28-pretraining.md`: 2605.20613、2605.21104、2605.21486
- `books/part-04-training-system/29-sft.md`: 2605.21177
- `books/part-04-training-system/31-rlhf.md`: 2605.20863
- `books/part-04-training-system/32-ppo.md`: 2605.20865
- `books/part-04-training-system/33-grpo.md`: 2605.20722、2605.21467
- `books/part-04-training-system/34-dpo.md`: 2605.20834
- `books/part-04-training-system/36-distributed-training.md`: 2605.20866
- `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`: 2605.20868
- `books/part-05-inference-system/49-tensorrt-llm.md`: 2605.20706
- `books/part-05-inference-system/56-inference-scheduling.md`: 2605.20723
- `books/part-06-ai-infrastructure/66-evaluation-system.md`: 2605.20262、2605.20270、2605.20745、2605.20774、2605.20833、2605.21482
- `books/part-07-agent/77-memory.md`: 2605.20926
- `books/part-07-agent/79-planning.md`: 2605.21260
- `books/part-07-agent/81-workflow.md`: 2605.20630
- `books/part-07-agent/84-agent-platform.md`: 2605.20704、2605.20874

## 写作边界

每项均写入 owner 章节的机制正文，并显式保留旧路径、约束变化、状态或控制权变化、收益、代价、failure mode、
证据边界与 fallback。论文名称没有被用作正文论证主语；所有结论只采用 queue 中 exact-v1 审阅支持的命题。

## 机械校验

- 39 个 `semantic-body-binding:<Source Family ID>:start/end` 均唯一存在于 Books。
- 涉及的 24 个 owner 文件通过 `git diff --check`。
- `papers/2026/05/21/README.md` 通过 `scripts/validate_research.py --report`。
- 上述结果只证明写回接口与定位完整，不替代 fresh non-author 语义复核。

未执行 stage、commit 或 push。
