# 2026-05-12 Root Books Writeback Queue — Bounded Repair

作者侧只提出写回，不修改共享 Books；root 已按日期顺序串行写入，fresh non-author reviewer 已完成写后语义审计。

- 队列记录：25
- 已应用且 fresh non-author review 通过：25
- pending：0
- 本轮有界返修子集：14（正文 12；marker-only 2）

## 2605.08568 → `INFER-TENSORRT-LLM`

- Owner：`books/part-05-inference-system/49-tensorrt-llm.md`
- 类型：正文整合
- 建议：静态 SVD rank 在固定 workload 下简单可复现。 当prompt 所需秩随输入变化，固定 rank 在质量和带宽之间浪费。时，router 只在 prefill 提出 rank pattern，decode 复用 versioned pattern；execution owner 验证并提交 fused plan。 收益必须与以下代价一起保存：路由误判、pattern cache 失效和聚合开销可能抵消收益。 回退已验收的静态 rank/原 dense matmul。
- 插入：Ch49 的低秩压缩段之后、量化 execution plan 之前
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.08703 → `TRAIN-RLHF`

- Owner：`books/part-04-training-system/31-rlhf.md`
- 类型：正文整合
- 建议：固定 reward model 在目标稳定时最易校准。 当开放式视觉任务需要的判据和工具会随 failure evidence变化。时，orchestrator对 skill/tool library提出版本变更，冻结 subagent执行，独立 validation gate拥有提交权。 收益必须与以下代价一起保存：同源模型自评、library膨胀和小验证集过拟合。 回退冻结 reward model与人工 rubric。
- 插入：Ch31 的 Reward Model 演进段，在训练更新与评估分权之后
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.08878 → `PLATFORM-SECURITY`

- Owner：`books/part-06-ai-infrastructure/72-security.md`
- 类型：正文整合
- 建议：行为 refusal 测试适合黑盒快速 gate。 当白盒对手可沿表示中的 refusal-escape direction绕过表面拒答。时，安全 owner审计 residual/attention/MLP/normalization对 RED 的贡献；修改仍需独立 utility/safety gate。 收益必须与以下代价一起保存：方向估计错误会伤害通用能力，且白盒访问昂贵。 回退多层黑盒 red-team、最小权限和输出/执行 guardrail。
- 插入：Ch72 refusal behavior 不等于知识删除段之后
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.08933 → `TRAIN-PRETRAINING`

- Owner：`books/part-04-training-system/28-pretraining.md`
- 类型：正文整合
- 建议：full-matrix Muon 在矩阵梯度结构统一时简单。 当attention heads 的近满秩块可独立 whiten，而对齐低秩块会被过度切分。时，optimizer按稳定 head group形成更新块，并记录 grouping revision；训练 gate验收 loss与稳定性。 收益必须与以下代价一起保存：更多正交化、norm cost和静态分组漂移。 回退 full-matrix Muon或 AdamW。
- 插入：Ch28 Muon/whitening 段内，在 spectral geometry 后
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09281 → `INFER-TENSORRT-LLM`

- Owner：`books/part-05-inference-system/49-tensorrt-llm.md`
- 类型：正文整合
- 建议：逐 expert/逐矩阵低秩量化容易实现。 当MoE 数量放大量化 metadata与小 kernel开销。时，activation-aware cluster共享二维子空间，fused kernel一次完成投影、routing-weighted accumulation与 reconstruction。 收益必须与以下代价一起保存：tile/rank错误、共享误差和硬件专用 fusion。 回退逐 expert量化或未量化 expert。
- 插入：Ch49 MoE 低精度 execution plan 段
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09516 → `MODEL-MOE`

- Owner：`books/part-02-model/21-moe.md`
- 类型：正文整合
- 建议：token-to-expert MoE保留完整层深。 当层数和状态更新本身也可条件化，但纯 routed attention会失去覆盖。时，block router提出 thin-layer子集；shared softmax拥有全局读，routed DeltaNet拥有稀疏状态更新。 收益必须与以下代价一起保存：rank ceiling、dispatch开销、kernel缺失与训练不稳定。 回退 dense block或传统 expert FFN。
- 插入：Ch21 expert routing 后新增 layer-level alternative branch
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09536 → `MULTIMODAL-GENERATIVE-PARADIGMS`

- Owner：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 类型：正文整合
- 建议：统一 denoising trajectory distillation简单。 当近时间与远时间的误差结构不同，统一监督妨碍速度/质量切换。时，teacher trajectory提供 privileged targets，distiller分配 temporal-aware监督；runtime选择已验收 operating mode。 收益必须与以下代价一起保存：额外 teacher rollout、trajectory bias与跨任务失效。 回退原 diffusion steps或统一 distillation。
- 插入：Ch24 diffusion acceleration/correction 主线
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09603 → `MULTIMODAL-GENERATIVE-PARADIGMS`

- Owner：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 类型：正文整合
- 建议：masked diffusion只填充未决 token可高并行。 当错误 token一旦 unmask便不可撤销。时，生成先并行 proposal，再进入显式 edit state提出 insertion/deletion/replacement，后续 refinement验证并提交。 收益必须与以下代价一起保存：edit phase增加步骤、训练复杂度和非收敛风险。 回退保守 mask schedule或 AR。
- 插入：Ch24 parallel proposal 与 iterative correction 之间
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09630 → `MODEL-TOKENIZER`

- Owner：`books/part-02-model/11-tokenizer.md`
- 类型：正文整合
- 建议：大 byte patch以较短序列换吞吐。 当patch内计算被推迟到边界，形成 patch lag。时，entropy-triggered scratchpad在 patch内更新瞬态 state，patch owner与 compute cadence解耦。 收益必须与以下代价一起保存：额外 KV/attention、mask实现和频率控制。 回退较小固定 patch或 tokenizer。
- 插入：Ch11 byte/patch tokenization 段
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09867 → `MODEL-LONG-CONTEXT`

- Owner：`books/part-02-model/22-long-context.md`
- 类型：正文整合
- 建议：不断追加 token history最透明。 当online adaptation使 history无界增长且重复重算。时，transformer在 continuous latent context中更新 compact algorithmic state，外部 evidence仍保留事实 authority。 收益必须与以下代价一起保存：state漂移、不可解释、训练不能保证学到构造算法。 回退显式 history、RAG或外部可审计 memory。
- 插入：Ch22 recurrent state 与有效上下文段
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09608 → `TRAIN-PRETRAINING`

- Owner：`books/part-04-training-system/28-pretraining.md`
- 类型：正文整合
- 建议：顺序 fine-tune/replay在任务兼容时可直接累积。 当新 update 与当前 model state 的 covariance geometry冲突时会干扰旧能力。时，training owner版本化 task update与state-relative geometry，merge gate只提交兼容或经校正的更新。 收益必须与以下代价一起保存：geometry proxy未必因果，barycenter与探测增加计算。 回退 replay、独立 adapter或原 checkpoint。
- 插入：Ch28 optimizer/update geometry之后，handoff Ch35 artifact rollback
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.10901 → `PLATFORM-SECURITY`

- Owner：`books/part-06-ai-infrastructure/72-security.md`
- 类型：正文整合
- 建议：有限 red-team适合发现已知 failure。 当零命中不能证明整个语义区域安全。时，guardrail owner在 pre-activation空间定义 harmful region，按 monotonic head认证最坏点；release gate区分 exact与probabilistic certificate。 收益必须与以下代价一起保存：region construction可漏掉真实 harmful manifold，白盒与模型专用。 域外回退 empirical red-team、abstain与 reference monitor。
- 插入：Ch72 guardrail/certificate 段，经验测试之后
- 证据边界：The exact-v1 body supports the mechanism under §4 Experiments. Counterevidence/scope was checked at §5.2 Limitations. It does not prove that “Beyond Red-Teaming: Formal Guarantees of LLM Guardrail Classifiers” generalizes to undisclosed models, hardware, precision, context/action length, concurrency, SLO, failure distribution or production tail; author-reported comparisons remain conditional on the paper's disclosed evaluator and workload.

## 2605.09315 → `AGENT-PLATFORM`

- Owner：`books/part-07-agent/84-agent-platform.md`
- 类型：marker-only
- 建议：正文语义链已存在，只补唯一 Source Family canonical marker；不得复制或改写正文。
- 插入：Ch84 现有 lifelong/self-evolution capability preservation 语义段，在其现有 arXiv:2605.09315v1 evidence note 周围补 canonical marker
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。

## 2605.09684 → `PLATFORM-MONITORING`

- Owner：`books/part-06-ai-infrastructure/67-monitoring.md`
- 类型：marker-only
- 建议：正文语义链已存在，只补唯一 Source Family canonical marker；不得复制或改写正文。
- 插入：Ch67 现有 staged red-team/monitor trajectory 语义段，在其现有 arXiv:2605.09684v1 evidence note 周围补 canonical marker
- 证据边界：只支持 exact-v1 在披露模型、数据、实现、evaluator 与 workload 下的机制和结果；不证明跨模型、硬件、精度、长度、并发、SLO 或生产尾延迟的普适收益，也不把作者 benchmark 当作独立复现。
