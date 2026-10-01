# 2604.22312v1 → Ch49：非作者实际写后核

范围：只核 [官方 exact-v1](https://arxiv.org/html/2604.22312v1) §4.1–4.3、§5.1–5.5、§6.2、§8 的必要机制/评价限制，与 `books/part-05-inference-system/49-tensorrt-llm.md` 中“Exact Top-K 可以复用时间相关性，但必须保留验证权”及前后衔接；未复现实验，不是 04/27 整日 Gate。

正文的主命题成立：前一步 Top-K 是阈值预测而非最终答案；全局精确计数确认候选，再在 shared memory 内完成 exact K 选择；额外 `prev_topk`/scratch HBM、约 60 KB/CTA、single-CTA 和 Blackwell/长上下文 decode 的受限证据均与原文一致。前接近似 LM-head 路径、后接低精度执行，能保留 exact 与 approximate 两类合同的区别。`semantic-body-binding:SF-2026-ARXIV-2604-22312` 的起止也只包本项正文。

写后仍有一处精确措辞待修，故**暂不签 PASS**：正文“随后验证候选并在验证失败时继续 refine”把 Phase 4 写成 Phase 3 失败条件下才启动。原文 §4.1–4.2 是先找到满足 `K ≤ f(T) ≤ C` 的阈值，收集候选；当候选数不恰为 K 时，Phase 4 在 shared memory 中执行精确选择。该条件下的 refine 是正常算法阶段，不是“验证失败”的处理。§4.1 Lemma 1 的 exactness 也以候选数满足界为条件，不能暗示任意输入都保证在固定 buffer 内完成。建议改成“经精确计数确认候选数落在 K 与容量 C 之间，再收集候选；若候选多于 K，则在 shared memory 中精确 refine”。后句“相关性不足时应回退”是工程建议；作者 §5.5 的已实现 dispatch 只明确 shape/硬件/preIdx/scratch 等七项门槛，不应读成已实现的动态相关性判别器。

此处仅建议定点修现有正文，不新增论文正文或扩大附件。修后再复核该句；未修前不能将 22312 算作本轮实际写后通过。`22312` 的日期与 04/27 整日来源/准入均不在本次核验范围。
