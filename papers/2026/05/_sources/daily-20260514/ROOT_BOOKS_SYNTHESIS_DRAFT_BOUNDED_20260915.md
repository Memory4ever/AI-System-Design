# 2026-05-14 Books 分章语义合成草案

该草案不是 Books 写回，也不是论文列表。每组以章节现有旧路径为起点，按约束变化串联多个 Source Family；root 仍须顺序对读相邻段落后再写入正文。

## `WORLDVIEW-REPRESENTATION` — `books/part-01-worldview/05-what-neural-networks-learn.md`

本组从章节已有机制出发，把外部约束推进到 `representation claim 与因果使用证据`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12874:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：一个自然语言解释可能同时匹配许多不同 SAE features；解释可读并不等于 feature identity 唯一，必须报告 descriptive collision。 机制落地后，`WORLDVIEW-REPRESENTATION` 拥有并版本化 representation claim 与因果使用证据，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12874v1 — §5 Why Current Scoring Methods Cannot Detect Collision; Evaluation=arXiv:2605.12874v1 — §4 Empirical Evidence; Non-proof=arXiv:2605.12874v1 — §7 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12874:end -->

<!-- source-family:SF-2026-ARXIV-2605-13329:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：persona directions 在早期预训练形成，改变‘行为只由 post-training 写入’的表示解释。 机制落地后，`WORLDVIEW-REPRESENTATION` 拥有并版本化 representation claim 与因果使用证据，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13329v1 — §2 Method; Evaluation=arXiv:2605.13329v1 — §2.2 Experimental Setup; Non-proof=arXiv:2605.13329v1 — §7 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13329:end -->

## `WORLDVIEW-LLM-INTELLIGENCE` — `books/part-01-worldview/08-why-llms-show-intelligence.md`

本组从章节已有机制出发，把外部约束推进到 `可见上下文、工作记忆与任务复杂度边界`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13687:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：合成层级语言给出 bounded context 与显式 working memory 的条件性下界。 机制落地后，`WORLDVIEW-LLM-INTELLIGENCE` 拥有并版本化 可见上下文、工作记忆与任务复杂度边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13687v1 — §2 Broadcast Process as a Hierarchical Language Model; Evaluation=arXiv:2605.13687v1 — §1.1 Summary of our results; Non-proof=arXiv:2605.13687v1 — §5 Limitations；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13687:end -->

## `MODEL-TOKENIZER` — `books/part-02-model/11-tokenizer.md`

本组从章节已有机制出发，把外部约束推进到 `vocabulary、alignment lexicon 与 checkpoint identity`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13429:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：以 token alignment lexicon 扩展 vocabulary，改变 tokenizer 与 checkpoint 的联合迁移合同。 机制落地后，`MODEL-TOKENIZER` 拥有并版本化 vocabulary、alignment lexicon 与 checkpoint identity，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13429v1 — §4 Methodology; Evaluation=arXiv:2605.13429v1 — §4.2 Alignment Evaluation; Non-proof=arXiv:2605.13429v1 — §7 Limitations and Future Work；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13429:end -->

## `MODEL-SELF-ATTENTION` — `books/part-02-model/14-self-attention.md`

本组从章节已有机制出发，把外部约束推进到 `attention temperature、长度与语义 revision`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12697:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：长上下文 attention 的固定 logit scale 无法跨 regime 复用；inverse temperature 应随长度与统计假设校准，而不是被 IO 优化章节替代。 机制落地后，`MODEL-SELF-ATTENTION` 拥有并版本化 attention temperature、长度与语义 revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12697v1 — §A Unified Framework for Critical Scaling of Inverse Temperature in Self-Attention; Evaluation=arXiv:2605.12697v1 — §3 A minimal empirical check: ξ β = 1 \xi_{\beta}=1 is not universal; Non-proof=arXiv:2605.12697v1 — §5 Discussion and Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12697:end -->

<!-- source-family:SF-2026-ARXIV-2605-13473:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：线性 attention 的单一 scalar gate 无法适配各维度曲率；在线 hypergradient 对角预条件改变 memory update geometry，也增加稳定性状态。 机制落地后，`MODEL-SELF-ATTENTION` 拥有并版本化 attention temperature、长度与语义 revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13473v1 — §The Online Scaled Gradient Method.; Evaluation=arXiv:2605.13473v1 — §6 Experiments; Non-proof=arXiv:2605.13473v1 — §7 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13473:end -->

## `MODEL-MOE` — `books/part-02-model/21-moe.md`

本组从章节已有机制出发，把外部约束推进到 `expert capacity、router revision 与 growth checkpoint`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13247:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：一次性训练最终 MoE 容量要求提前冻结规模；渐进扩展 expert pool 能复用已有能力，但 expansion schedule 与 router state 成为 checkpoint 身份。 机制落地后，`MODEL-MOE` 拥有并版本化 expert capacity、router revision 与 growth checkpoint，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13247v1 — §Architecture and training.; Evaluation=arXiv:2605.13247v1 — §4 Experiments; Non-proof=arXiv:2605.13247v1 — §7 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13247:end -->

## `MODEL-LONG-CONTEXT` — `books/part-02-model/22-long-context.md`

本组从章节已有机制出发，把外部约束推进到 `版本化状态、控制 owner 与验收边界`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12922:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：多轮任务丢失不能只用窗口截断解释；goal token 的 attention 可达性会先衰减，而相关信息仍残留在 residual representation，要求把‘存在’与‘被当前路径使用’分开。 机制落地后，`MODEL-LONG-CONTEXT` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12922v1 — §2 Methodology; Evaluation=arXiv:2605.12922v1 — §3 Experimental Design; Non-proof=arXiv:2605.12922v1 — §4 Results & Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12922:end -->

<!-- source-family:SF-2026-ARXIV-2605-13485:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：标称 context length 不等于有效信息长度；tokenization 与 fragment boundary 会改变可利用上下文，必须把输入表示纳入 long-context identity。 机制落地后，`MODEL-LONG-CONTEXT` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13485v1 — §C.1 Transformer Architecture; Evaluation=arXiv:2605.13485v1 — §Empirical observation.; Non-proof=arXiv:2605.13485v1 — §5 Open Questions and Limitations；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13485:end -->

<!-- source-family:SF-2026-ARXIV-2605-13831:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：把文本长上下文配方直接搬到 VLM 会混淆视觉 token、文档结构与长度外推；continued pretraining 必须联合数据组成、位置策略和跨长度评价。 机制落地后，`MODEL-LONG-CONTEXT` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13831v1 — §4 Multimodal Long-Context Data Curation; Evaluation=arXiv:2605.13831v1 — §3 Experimental Setup; Non-proof=arXiv:2605.13831v1 — §7 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13831:end -->

## `MULTIMODAL-REPRESENTATION` — `books/part-03-multimodal-world-models/23-multimodal-representation.md`

本组从章节已有机制出发，把外部约束推进到 `表示 identity、模态缺失状态与融合 gate`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13156:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：对象幻觉不是单一路径故障；视觉证据写入与语言先验读取形成不同回路，必须以因果干预分开诊断。 机制落地后，`MULTIMODAL-REPRESENTATION` 拥有并版本化 表示 identity、模态缺失状态与融合 gate，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13156v1 — §3 Methodology; Evaluation=arXiv:2605.13156v1 — §4 Experimental Setup; Non-proof=arXiv:2605.13156v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13156:end -->

<!-- source-family:SF-2026-ARXIV-2605-13737:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：多模态模型能够识别音视频信息不等于行动时会采用它；冲突条件下必须分别测 perception、premise rejection 与 action use。 机制落地后，`MULTIMODAL-REPRESENTATION` 拥有并版本化 表示 identity、模态缺失状态与融合 gate，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13737v1 — §I.2 Annotation Pipeline Methodology; Evaluation=arXiv:2605.13737v1 — §2 IMAVB: An Omni Benchmark for Perception–Action Dissociation; Non-proof=arXiv:2605.13737v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13737:end -->

## `MULTIMODAL-GENERATIVE-PARADIGMS` — `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`

本组从章节已有机制出发，把外部约束推进到 `mutable generation state、proposal、correction 与 commit`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12522:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：把 AR 与 masked diffusion 的文本差异全归因于训练目标会混淆因子；对照实验进一步把双向训练目标与 confidence remasking 的熵效应分开。 机制落地后，`MULTIMODAL-GENERATIVE-PARADIGMS` 拥有并版本化 mutable generation state、proposal、correction 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12522v1 — §4 Controlled experiments on training objectives; Evaluation=arXiv:2605.12522v1 — §3 Preliminaries and results for off-the-shelf models; Non-proof=arXiv:2605.12522v1 — §6 Conclusion and discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12522:end -->

<!-- source-family:SF-2026-ARXIV-2605-13026:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：masked diffusion 训练的低效不能只归因于并行目标；语言的 locality bias 允许重分配被预测位置与上下文，形成更有条件的加速路径。 机制落地后，`MULTIMODAL-GENERATIVE-PARADIGMS` 拥有并版本化 mutable generation state、proposal、correction 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13026v1 — §2.2 Shared Format of Learning Objectives Across Various Frameworks; Evaluation=arXiv:2605.13026v1 — §5 Experiments; Non-proof=arXiv:2605.13026v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13026:end -->

<!-- source-family:SF-2026-ARXIV-2605-13043:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：逐步 masked generation 的安全 remasking 与 latent steering 改变可变生成状态的提交控制。 机制落地后，`MULTIMODAL-GENERATIVE-PARADIGMS` 拥有并版本化 mutable generation state、proposal、correction 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13043v1 — §Adaptive Steering and Remasking for Safe Generation in Diffusion Language Models; Evaluation=arXiv:2605.13043v1 — §5 Experiments; Non-proof=arXiv:2605.13043v1 — §7 Related Work and Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13043:end -->

<!-- source-family:SF-2026-ARXIV-2605-13179:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：受控负结果显示 Engram associative memory 不自动迁移到 AR image generation，校正架构外推。 机制落地后，`MULTIMODAL-GENERATIVE-PARADIGMS` 拥有并版本化 mutable generation state、proposal、correction 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13179v1 — §3 Method; Evaluation=arXiv:2605.13179v1 — §4 Experiments & Analysis; Non-proof=arXiv:2605.13179v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13179:end -->

<!-- source-family:SF-2026-ARXIV-2605-13448:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：latent reuse 的收益受 subspace shift/noise 约束，为复用路径给出可拒绝的理论边界。 机制落地后，`MULTIMODAL-GENERATIVE-PARADIGMS` 拥有并版本化 mutable generation state、proposal、correction 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13448v1 — §2.1 Diffusion Models; Evaluation=arXiv:2605.13448v1 — §3 Main Results; Non-proof=arXiv:2605.13448v1 — §4 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13448:end -->

<!-- source-family:SF-2026-ARXIV-2605-13724:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：any-step video diffusion 让 flow map 支持非相邻时间跳转，改变 rollout 的时间状态。 机制落地后，`MULTIMODAL-GENERATIVE-PARADIGMS` 拥有并版本化 mutable generation state、proposal、correction 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13724v1 — §4 Method; Evaluation=arXiv:2605.13724v1 — §5 Experiments; Non-proof=arXiv:2605.13724v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13724:end -->

## `MULTIMODAL-WORLD-MODELS` — `books/part-03-multimodal-world-models/25-multimodal-world-models.md`

本组从章节已有机制出发，把外部约束推进到 `版本化状态、控制 owner 与验收边界`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13013:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：只预测像素级下一帧难以支撑在线控制；joint embedding diffusion world model 在 latent dynamics 中联合表征 observation 与 transition，但 imagined rollout 仍不等于环境事实。 机制落地后，`MULTIMODAL-WORLD-MODELS` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13013v1 — §3 Method; Evaluation=arXiv:2605.13013v1 — §4 Experiments; Non-proof=arXiv:2605.13013v1 — §5 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13013:end -->

## `MULTIMODAL-EMBODIED-VLA` — `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`

本组从章节已有机制出发，把外部约束推进到 `observation/action state、控制频率与 safety fallback`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13382:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：AR VLA 逐 token action 解码准确但慢；block diffusion finetuning 并行修正 action chunks，同时引入可变动作状态与 commit 边界。 机制落地后，`MULTIMODAL-EMBODIED-VLA` 拥有并版本化 observation/action state、控制频率与 safety fallback，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13382v1 — §3 Method; Evaluation=arXiv:2605.13382v1 — §4 Experiments; Non-proof=arXiv:2605.13382v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13382:end -->

<!-- source-family:SF-2026-ARXIV-2605-13778:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：Diffusion VLA 每次重规划都跑完整模型会错过控制周期；轻量 draft、主模型并行验证与 phase-aware fallback 可减少 full calls。 机制落地后，`MULTIMODAL-EMBODIED-VLA` 拥有并版本化 observation/action state、控制频率与 safety fallback，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13778v1 — §Realtime-VLA FLASH : Speculative Inference Framework for Diffusion-based VLAs; Evaluation=arXiv:2605.13778v1 — §4 Experiments; Non-proof=arXiv:2605.13778v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13778:end -->

## `TRAIN-DATA` — `books/part-04-training-system/27-data.md`

本组从章节已有机制出发，把外部约束推进到 `样本真值、顺序、采样与 data-recipe revision`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12944:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：只给样本打分不能表达操作顺序与组合效应；固定原始池上的可执行 data-recipe search 将筛选算子、预算与完整 SFT 验证绑定。 机制落地后，`TRAIN-DATA` 拥有并版本化 样本真值、顺序、采样与 data-recipe revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12944v1 — §3 Method; Evaluation=arXiv:2605.12944v1 — §4 Experiments; Non-proof=arXiv:2605.12944v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12944:end -->

<!-- source-family:SF-2026-ARXIV-2605-13757:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：VLA frame selection 保留 action-critical transition，改变训练数据的时间采样责任。 机制落地后，`TRAIN-DATA` 拥有并版本化 样本真值、顺序、采样与 data-recipe revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13757v1 — §3 Method; Evaluation=arXiv:2605.13757v1 — §4 Experiments; Non-proof=arXiv:2605.13757v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13757:end -->

<!-- source-family:SF-2026-ARXIV-2605-13829:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：Negation Neglect 表明否定/fiction 标签可在微调中被剥离，改变训练数据 truth-state 编码合同。 机制落地后，`TRAIN-DATA` 拥有并版本化 样本真值、顺序、采样与 data-recipe revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13829v1 — §3.1 Training on annotated negations leads to Negation Neglect; Evaluation=arXiv:2605.13829v1 — §2.2 Evaluation; Non-proof=arXiv:2605.13829v1 — §7 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13829:end -->

## `TRAIN-PRETRAINING` — `books/part-04-training-system/28-pretraining.md`

本组从章节已有机制出发，把外部约束推进到 `optimizer trajectory、低秩参数化与终点证据`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13405:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：模型扩容常追求立即保留初始性能；实验证据提示最终训练轨迹比增长瞬间更重要，因此 warmstart operator 必须与后续预算联合评价。 机制落地后，`TRAIN-PRETRAINING` 拥有并版本化 optimizer trajectory、低秩参数化与终点证据，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13405v1 — §3 Methodology; Evaluation=arXiv:2605.13405v1 — §4 Empirical Study; Non-proof=arXiv:2605.13405v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13405:end -->

<!-- source-family:SF-2026-ARXIV-2605-13652:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：相同 perplexity 的低秩预训练可落入不同 basin，限制以终点 loss 证明训练等价。 机制落地后，`TRAIN-PRETRAINING` 拥有并版本化 optimizer trajectory、低秩参数化与终点证据，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13652v1 — §Low-rank pre-training methods.; Evaluation=arXiv:2605.13652v1 — §3 Evaluation framework; Non-proof=arXiv:2605.13652v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13652:end -->

## `TRAIN-SFT` — `books/part-04-training-system/29-sft.md`

本组从章节已有机制出发，把外部约束推进到 `query-conditioned update、base revision 与 rollback`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12705:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：遗忘通常在下游微调后补救；更早的数据暴露顺序会改变能力被写入参数的方式，从而改变后续可保留性。 机制落地后，`TRAIN-SFT` 拥有并版本化 query-conditioned update、base revision 与 rollback，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12705v1 — §3.1 Evaluation methodology; Evaluation=arXiv:2605.12705v1 — §3.1 Evaluation methodology; Non-proof=arXiv:2605.12705v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12705:end -->

<!-- source-family:SF-2026-ARXIV-2605-12906:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：固定选择最易或最难 SFT 数据会忽略预算变化；最优 difficulty 会随数据量移动，数据 recipe 必须绑定预算与目标外推区间。 机制落地后，`TRAIN-SFT` 拥有并版本化 query-conditioned update、base revision 与 rollback，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12906v1 — §4.1 Varying Data Size and Difficulty on iGSM Data; Evaluation=arXiv:2605.12906v1 — §3 Fine-grained Experiments: The Interplay between Data Difficulty and Size; Non-proof=arXiv:2605.12906v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12906:end -->

<!-- source-family:SF-2026-ARXIV-2605-13369:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：query-conditioned test-time parameter update 让单次查询产生新的模型 revision 与回滚责任。 机制落地后，`TRAIN-SFT` 拥有并版本化 query-conditioned update、base revision 与 rollback，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13369v1 — §3 Method; Evaluation=arXiv:2605.13369v1 — §4 Experiments; Non-proof=arXiv:2605.13369v1 — §5 Limitations and Future Work；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13369:end -->

## `TRAIN-LORA` — `books/part-04-training-system/30-lora.md`

本组从章节已有机制出发，把外部约束推进到 `base/adapter revision、slot 生命周期与 consolidation`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13162:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：continual LoRA slots 与 consolidation 让 adapter 变成可增长、可合并的 program memory。 机制落地后，`TRAIN-LORA` 拥有并版本化 base/adapter revision、slot 生命周期与 consolidation，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13162v1 — §4 Method; Evaluation=arXiv:2605.13162v1 — §5 Experimental Results; Non-proof=arXiv:2605.13162v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13162:end -->

## `TRAIN-GRPO` — `books/part-04-training-system/33-grpo.md`

本组从章节已有机制出发，把外部约束推进到 `trajectory、verifier、credit 与 policy update`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12519:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：只用终局答案奖励时，中间推理可以碰巧正确却不可验证；把轨迹拆成结构化 claims，并由确定性 verifier 与自适应权重分配过程信用，才把正确性与推理质量分开治理。 机制落地后，`TRAIN-GRPO` 拥有并版本化 trajectory、verifier、credit 与 policy update，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12519v1 — §3 Adaptive verifiable process supervision; Evaluation=arXiv:2605.12519v1 — §4 Experiments; Non-proof=arXiv:2605.12519v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12519:end -->

<!-- source-family:SF-2026-ARXIV-2605-12969:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：token-level clipped reward 不一定表达 verified sequence 的相对关系；以长度归一的序列概率对比同组正负轨迹，改变 RLVR 的 credit coordinate。 机制落地后，`TRAIN-GRPO` 拥有并版本化 trajectory、verifier、credit 与 policy update，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12969v1 — §4 Methods; Evaluation=arXiv:2605.12969v1 — §5 Experiments; Non-proof=arXiv:2605.12969v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12969:end -->

<!-- source-family:SF-2026-ARXIV-2605-13643:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：on-policy distillation 的 dense teacher signal 并非沿序列均匀可学；prefix 可教而 suffix 退化时，需要按位置诊断 support 与 policy divergence。 机制落地后，`TRAIN-GRPO` 拥有并版本化 trajectory、verifier、credit 与 policy update，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13643v1 — §3 Local Teachability Analysis; Evaluation=arXiv:2605.13643v1 — §4 Experiments; Non-proof=arXiv:2605.13643v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13643:end -->

## `TRAIN-DISTRIBUTED-TRAINING` — `books/part-04-training-system/36-distributed-training.md`

本组从章节已有机制出发，把外部约束推进到 `版本化状态、控制 owner 与验收边界`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12766:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：固定网络拓扑上的 collective schedule 在可重构 fabric 上会浪费链路；复用 subring 重新组织 AllReduce、AllGather、ReduceScatter 与 All-to-All，但 schedule 与 topology revision 必须共同验收。 机制落地后，`TRAIN-DISTRIBUTED-TRAINING` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12766v1 — §3.1. Approach: Reusable Subrings with Bruck; Evaluation=arXiv:2605.12766v1 — §4. Evaluation; Non-proof=arXiv:2605.12766v1 — §5. Discussion and Future Work；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12766:end -->

<!-- source-family:SF-2026-ARXIV-2605-13434:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：异步 SGD 在 worker 速度和数据分布相关时会偏向高频 worker；按贡献频率重标度更新以恢复目标，但增加方差与统计估计状态。 机制落地后，`TRAIN-DISTRIBUTED-TRAINING` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13434v1 — §Optimal Methods in the Fixed-Computation Model; Evaluation=arXiv:2605.13434v1 — §5 Experiments; Non-proof=arXiv:2605.13434v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13434:end -->

## `INFER-PREFILL` — `books/part-05-inference-system/43-prefill.md`

本组从章节已有机制出发，把外部约束推进到 `prefill 输入、层级 grounding state 与 harness`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12549:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：GUI grounding 过去主要从 decode 输出诊断；层级干预表明关键定位状态可能在 prefill 就已形成或丢失，因此 Prefill 也必须进入 grounding harness。 机制落地后，`INFER-PREFILL` 拥有并版本化 prefill 输入、层级 grounding state 与 harness，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12549v1 — §2 Revisiting GUI Grounding Inference; Evaluation=arXiv:2605.12549v1 — §4 Experiments; Non-proof=arXiv:2605.12549v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12549:end -->

## `INFER-DECODE` — `books/part-05-inference-system/44-decode.md`

本组从章节已有机制出发，把外部约束推进到 `persistent session KV、advance/query 分离与 recovery`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13784:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：每次查询重放全部历史使 prefill 随会话增长；持久 session KV 把 history advance 与 query 分开，但 cache revision、权限与恢复成为长期状态。 机制落地后，`INFER-DECODE` 拥有并版本化 persistent session KV、advance/query 分离与 recovery，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13784v1 — §3 Architecture; Evaluation=arXiv:2605.13784v1 — §3.9 Flash Queries: Ahead-of-Time Query Evaluation; Non-proof=arXiv:2605.13784v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13784:end -->

## `INFER-KV-CACHE` — `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`

本组从章节已有机制出发，把外部约束推进到 `head-aware KV identity、保留策略与 cache layout`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13111:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：视频生成中的统一 KV 长度忽略 attention heads 的时间职责差异；离线识别 head type 并用 ragged cache 执行异构保留策略，才让压缩与画质责任一致。 机制落地后，`INFER-KV-CACHE` 拥有并版本化 head-aware KV identity、保留策略与 cache layout，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13111v1 — §4 Method; Evaluation=arXiv:2605.13111v1 — §5 Experiments; Non-proof=arXiv:2605.13111v1 — §7 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13111:end -->

## `INFER-SPECULATIVE-DECODING` — `books/part-05-inference-system/48-speculative-decoding.md`

本组从章节已有机制出发，把外部约束推进到 `draft/target state、verification 与 commit`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12825:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：AR 的精确左到右语义与 diffusion 的并行修正不是只能二选一；双视图生成让 AR owner 验证 diffusion proposals，但引入两套状态的一致性责任。 机制落地后，`INFER-SPECULATIVE-DECODING` 拥有并版本化 draft/target state、verification 与 commit，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12825v1 — §3 Methodology: The Orthrus Architecture; Evaluation=arXiv:2605.12825v1 — §4 Experiments; Non-proof=arXiv:2605.12825v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12825:end -->

## `INFER-TENSORRT-LLM` — `books/part-05-inference-system/49-tensorrt-llm.md`

本组从章节已有机制出发，把外部约束推进到 `quantization policy、矩阵 identity 与执行 artifact`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13768:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：对所有矩阵方向等量分配 bit rate 简单却浪费预算；waterfilling 按方向敏感度配置量化精度，将 policy 与具体矩阵/硬件身份绑定。 机制落地后，`INFER-TENSORRT-LLM` 拥有并版本化 quantization policy、矩阵 identity 与执行 artifact，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13768v1 — §III Weight quantization: Practice; Evaluation=arXiv:2605.13768v1 — §III-E Quantizing Llama-3-8B; Non-proof=arXiv:2605.13768v1 — §III-F Future of weight-only quantization；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13768:end -->

## `PLATFORM-FOUNDATIONS` — `books/part-06-ai-infrastructure/57-what-is-ai-platform.md`

本组从章节已有机制出发，把外部约束推进到 `adapter artifact、租户、placement 与 service revision`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13779:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：手工管理大量 LoRA 的训练、注册与服务会让控制面碎裂；统一的多租户 adapter lifecycle 把 artifact、placement 与 serving revision 接成同一平台对象。 机制落地后，`PLATFORM-FOUNDATIONS` 拥有并版本化 adapter artifact、租户、placement 与 service revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13779v1 — §3 System Design; Evaluation=arXiv:2605.13779v1 — §5 Evaluation; Non-proof=arXiv:2605.13779v1 — §7 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13779:end -->

## `PLATFORM-EVALUATION-SYSTEM` — `books/part-06-ai-infrastructure/66-evaluation-system.md`

本组从章节已有机制出发，把外部约束推进到 `evaluation identity、切片、校准与 verdict authority`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12673:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：Agent benchmark 的 pass rate 默认任务接口不可钻空子；系统化生成 exploit 并验证任务 invariant，才区分能力提升与 harness 被规避。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12673v1 — §3 Motivating Example: Reward Hacking in SWE-bench; Evaluation=arXiv:2605.12673v1 — §Do Androids Dream of Breaking the Game? Systematically Auditing AI Agent Benchmarks with BenchJack; Non-proof=arXiv:2605.12673v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12673:end -->

<!-- source-family:SF-2026-ARXIV-2605-12813:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：受约束 latent adversary 暴露 hallucination detector 的局部盲区，改变检测器鲁棒性合同。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12813v1 — §3.2 Proposed Algorithm: REALISTA; Evaluation=arXiv:2605.12813v1 — §4 Experimental Setups; Non-proof=arXiv:2605.12813v1 — §6 Conclusion and Future Work；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12813:end -->

<!-- source-family:SF-2026-ARXIV-2605-12869:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：time-to-jailbreak 把 guardrail 评价从一次攻击成功率扩展为随搜索预算演化的 survival contract。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12869v1 — §3 Survival Analysis Framework for Jailbreaks; Evaluation=arXiv:2605.12869v1 — §4 Dataset and Experiments; Non-proof=arXiv:2605.12869v1 — §5 Analysis and Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12869:end -->

<!-- source-family:SF-2026-ARXIV-2605-12894:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：始终合作的用户模拟器高估 Agent 鲁棒性；保持任务目标不变而注入 persona policy，能测试犹豫、反复与偏离等交互分布。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12894v1 — §3 Method; Evaluation=arXiv:2605.12894v1 — §Beyond Cooperative Simulators: Generating Realistic User Personas for Robust Evaluation of LLM Agents; Non-proof=arXiv:2605.12894v1 — §5 Results & Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12894:end -->

<!-- source-family:SF-2026-ARXIV-2605-13352:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：分离 aleatoric/epistemic uncertainty 为冻结 VLM 提供两类不同的 abstention 证据。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13352v1 — §Training objective.; Evaluation=arXiv:2605.13352v1 — §5 Experiments; Non-proof=arXiv:2605.13352v1 — §6 Conclusions, Limitations, Discussion and Broader Impact；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13352:end -->

<!-- source-family:SF-2026-ARXIV-2605-13414:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：只测模型能否解题忽略其是否会在预算下选择值得解决的问题；先承诺选择、顺序和 token allocation，才能评价 prospective metacognitive control。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13414v1 — §3 TRIAGE Framework; Evaluation=arXiv:2605.13414v1 — §4 Experimental Setup; Non-proof=arXiv:2605.13414v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13414:end -->

<!-- source-family:SF-2026-ARXIV-2605-13484:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：全局 calibration 可以掩盖未知子群的系统性失校准；主动搜索隐藏 regime 将 slice discovery 与最终 calibration verdict 分开。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13484v1 — §3 A Diagnostic Framework for Revealing Calibration Regimes; Evaluation=arXiv:2605.13484v1 — §4 Experiments: Synthetic Illustrations; Non-proof=arXiv:2605.13484v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13484:end -->

<!-- source-family:SF-2026-ARXIV-2605-13595:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：模型输出低置信度并不必然对应真实未知；刻意诱导的不确定性会制造校准外观，因此 uncertainty sensor 不能独立拥有 abstain 或 release authority。 机制落地后，`PLATFORM-EVALUATION-SYSTEM` 拥有并版本化 evaluation identity、切片、校准与 verdict authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13595v1 — §3 Methods; Evaluation=arXiv:2605.13595v1 — §4 Experiments; Non-proof=arXiv:2605.13595v1 — §8 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13595:end -->

## `PLATFORM-MONITORING` — `books/part-06-ai-infrastructure/67-monitoring.md`

本组从章节已有机制出发，把外部约束推进到 `monitor observation、校准与升级处置`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12746:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：把 CoT 交给较小 monitor 并不自动得到安全检测；monitor 会把隐藏目标误认成用户任务，需要专门数据与分层评价校准。 机制落地后，`PLATFORM-MONITORING` 拥有并版本化 monitor observation、校准与升级处置，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12746v1 — §3 Threat Model; Evaluation=arXiv:2605.12746v1 — §6 Experiments; Non-proof=arXiv:2605.12746v1 — §3 Threat Model；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12746:end -->

<!-- source-family:SF-2026-ARXIV-2605-13772:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：整条 reasoning trace 一个分数无法定位首个错误；逐步 hidden-state transport 只作为 error sensor，最终事实仍需外部 verifier。 机制落地后，`PLATFORM-MONITORING` 拥有并版本化 monitor observation、校准与升级处置，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13772v1 — §3 Methodology; Evaluation=arXiv:2605.13772v1 — §3.5 Main theoretical results; Non-proof=arXiv:2605.13772v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13772:end -->

## `PLATFORM-TRACE` — `books/part-06-ai-infrastructure/69-trace.md`

本组从章节已有机制出发，把外部约束推进到 `跨阶段 trace identity、行为分类与因果候选`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13625:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：长运行 Agent 的 trace taxonomy 将失败从最终结果拆到跨阶段行为状态。 机制落地后，`PLATFORM-TRACE` 拥有并版本化 跨阶段 trace identity、行为分类与因果候选，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13625v1 — §3 Construct and Extend Act· onomy : A Grounded Theory Approach; Evaluation=arXiv:2605.13625v1 — §2.2 Large-Scale Analysis of Agent Behavioral Descriptions; Non-proof=arXiv:2605.13625v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13625:end -->

## `PLATFORM-SECURITY` — `books/part-06-ai-infrastructure/72-security.md`

本组从章节已有机制出发，把外部约束推进到 `threat model、sensor evidence 与不可绕过的 commit authority`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12529:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：在未知 trigger 下同时清除后门并保留 watermark，改变模型发布前的权重修复与产权证据边界。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12529v1 — §V Method; Evaluation=arXiv:2605.12529v1 — §VI Experiments; Non-proof=arXiv:2605.12529v1 — §III Threat model；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12529:end -->

<!-- source-family:SF-2026-ARXIV-2605-12574:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：输出语义扰动可作为黑盒 VLM membership sensor，改变多模态隐私验收的观察面。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12574v1 — §3 Methodology; Evaluation=arXiv:2605.12574v1 — §4 Experiments; Non-proof=arXiv:2605.12574v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12574:end -->

<!-- source-family:SF-2026-ARXIV-2605-12765:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：输入条件化的激活旋转把 inference-time unlearning 变成受 gate 控制的参数路径。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12765v1 — §Input-adaptive activation steering.; Evaluation=arXiv:2605.12765v1 — §3 Experiments; Non-proof=arXiv:2605.12765v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12765:end -->

<!-- source-family:SF-2026-ARXIV-2605-12875:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：Skill 描述声明的能力范围不能证明代码副作用相同；从代码构建 security property graph 再与描述对照，才能发现未披露行为。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12875v1 — §IV SkillScope; Evaluation=arXiv:2605.12875v1 — §V Evaluation; Non-proof=arXiv:2605.12875v1 — §II-B Threat Model；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12875:end -->

<!-- source-family:SF-2026-ARXIV-2605-13044:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：Skill 不必遭到已知 exploit 才能违反 specification；semantic fuzzing 从声明不变量生成输入并检查真实 side effect，把安全真值交还给确定性执行证据。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13044v1 — §III-B Framework Overview; Evaluation=arXiv:2605.13044v1 — §VII Evaluation; Non-proof=arXiv:2605.13044v1 — §II-C Threat Model；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13044:end -->

<!-- source-family:SF-2026-ARXIV-2605-13115:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：PRNG 污染位于模型图之外却能控制训练结果，要求随机源进入训练供应链 identity。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13115v1 — §2.1 Diffusion Model Security.; Evaluation=arXiv:2605.13115v1 — §5 Experiments; Non-proof=arXiv:2605.13115v1 — §1.2 Threat Scenario.；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13115:end -->

<!-- source-family:SF-2026-ARXIV-2605-13170:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：多 Agent 系统的薄弱点可能位于通信边而非单个模型；攻击应以消息影响路径和 receiver 状态偏移为单位。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13170v1 — §3. Problem Definition; Evaluation=arXiv:2605.13170v1 — §5. Experimental Analysis; Non-proof=arXiv:2605.13170v1 — §6.2. Limitations；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13170:end -->

<!-- source-family:SF-2026-ARXIV-2605-13213:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：分层多模态多 Agent 攻击把单节点风险升级为跨角色、跨模态的传播路径。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13213v1 — §3 Method; Evaluation=arXiv:2605.13213v1 — §4 Experiments; Non-proof=arXiv:2605.13213v1 — §5 Conclusions；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13213:end -->

<!-- source-family:SF-2026-ARXIV-2605-13334:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：多轮 LLM-to-LLM persuasion 可跨轮侵蚀 guardrail，改变安全评价的交互状态。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13334v1 — §Method summary.; Evaluation=arXiv:2605.13334v1 — §Jailbreak, refusal benchmarks, and persuasion.; Non-proof=arXiv:2605.13334v1 — §8 Limitations；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13334:end -->

<!-- source-family:SF-2026-ARXIV-2605-13338:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：安全攻击不只追求有害文本，也可通过诱导过度思考消耗预算；availability gate 必须约束推理长度、成本与停止权。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13338v1 — §Inducing Overthink: Hierarchical Genetic Algorithm-based DoS Attack on Black-Box Large Language Reasoning Models; Evaluation=arXiv:2605.13338v1 — §4 Evaluation; Non-proof=arXiv:2605.13338v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13338:end -->

<!-- source-family:SF-2026-ARXIV-2605-13411:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：静态 attack/defense 集会快速过期；把攻击样本、防御策略与失败回执外置成可检查、可复用的共同演进状态，才能跨模型迭代而不把安全知识埋进单次权重。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13411v1 — §3 Methodology; Evaluation=arXiv:2605.13411v1 — §4 Experiments and Results; Non-proof=arXiv:2605.13411v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13411:end -->

<!-- source-family:SF-2026-ARXIV-2605-13471:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：一次 prompt injection 的过滤不足以治理 always-on Agent；攻击可沉积到 memory、skill 与 scheduler，provenance gate 必须跨 run 追踪持久控制状态。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13471v1 — §Adaptive attacks against in-context defenses; Evaluation=arXiv:2605.13471v1 — §Indirect prompt injection and agent benchmarks; Non-proof=arXiv:2605.13471v1 — §IV Threat Model；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13471:end -->

<!-- source-family:SF-2026-ARXIV-2605-13825:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：中性 prompt 下的安全行为可被既往行动历史锚定；历史不是普通上下文，而是会改变 action prior 的不可信控制输入。 机制落地后，`PLATFORM-SECURITY` 拥有并版本化 threat model、sensor evidence 与不可绕过的 commit authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13825v1 — §3 The HistoryAnchor-100 benchmark; Evaluation=arXiv:2605.13825v1 — §3 The HistoryAnchor-100 benchmark; Non-proof=arXiv:2605.13825v1 — §5 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13825:end -->

## `AGENT-CONTEXT` — `books/part-07-agent/75-context.md`

本组从章节已有机制出发，把外部约束推进到 `active context、来源身份、预算与 compaction revision`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13050:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：并行搜索多个 context 并剪枝会让 context 本身成为可优化且可退化的运行状态。 机制落地后，`AGENT-CONTEXT` 拥有并版本化 active context、来源身份、预算与 compaction revision，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13050v1 — §3 Methodology; Evaluation=arXiv:2605.13050v1 — §4 Experiments; Non-proof=arXiv:2605.13050v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13050:end -->

## `AGENT-RAG` — `books/part-07-agent/76-rag.md`

本组从章节已有机制出发，把外部约束推进到 `query/evidence identity、分支检索与 answer admission`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12975:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：可执行 Python 检索计划与确定性 compiler feedback/retry 改变 multi-hop RAG 的控制状态。 机制落地后，`AGENT-RAG` 拥有并版本化 query/evidence identity、分支检索与 answer admission，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12975v1 — §2 Method; Evaluation=arXiv:2605.12975v1 — §3 Experiments; Non-proof=arXiv:2605.12975v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12975:end -->

## `AGENT-MEMORY` — `books/part-07-agent/77-memory.md`

本组从章节已有机制出发，把外部约束推进到 `memory proposal、derived state、read/write authority 与 expiry`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12978:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：反复用 LLM 汇总有用记忆会逐轮引入错误；consolidation 必须保留原证据、版本与回滚，不能把新 summary 覆盖成事实。 机制落地后，`AGENT-MEMORY` 拥有并版本化 memory proposal、derived state、read/write authority 与 expiry，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12978v1 — §H.1 Memory artifacts from prior methods; Evaluation=arXiv:2605.12978v1 — §3 Experiment Set-up; Non-proof=arXiv:2605.12978v1 — §7 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12978:end -->

<!-- source-family:SF-2026-ARXIV-2605-13370:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：显式循环记忆受 BPTT 梯度稳定性限制；相位化状态转移可保留长期信息，但其数值稳定与表达能力必须分别验收。 机制落地后，`AGENT-MEMORY` 拥有并版本化 memory proposal、derived state、read/write authority 与 expiry，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13370v1 — §3 Methods; Evaluation=arXiv:2605.13370v1 — §4 Experiments; Non-proof=arXiv:2605.13370v1 — §5 Limitations and Future Work；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13370:end -->

<!-- source-family:SF-2026-ARXIV-2605-13438:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：always-on proactive memory folding 把写入、折叠与主动提示变成长驻控制状态。 机制落地后，`AGENT-MEMORY` 拥有并版本化 memory proposal、derived state、read/write authority 与 expiry，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13438v1 — §2 CogniFold: From Neural Layers to Conceptual Bootstrapping; Evaluation=arXiv:2605.13438v1 — §4 Experiments and Results; Non-proof=arXiv:2605.13438v1 — §5 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13438:end -->

## `AGENT-TOOL-CALLING` — `books/part-07-agent/78-tool-calling.md`

本组从章节已有机制出发，把外部约束推进到 `tool proposal、异步 result 与取消/提交 authority`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13360:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：同步等待工具最易保持一致，却破坏实时交互；异步 I/O 与 speculative tool proposal 需要独立验证、取消和回滚 authority。 机制落地后，`AGENT-TOOL-CALLING` 拥有并版本化 tool proposal、异步 result 与取消/提交 authority，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13360v1 — §3 Method; Evaluation=arXiv:2605.13360v1 — §5 Results; Non-proof=arXiv:2605.13360v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13360:end -->

## `AGENT-WORKFLOW` — `books/part-07-agent/81-workflow.md`

本组从章节已有机制出发，把外部约束推进到 `workflow state、verifier receipt 与提交边界`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12571:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：最终答案正确不能证明 Agent 消费了检索证据；将 evidence selection 与 answer authority 解耦，才能识别靠参数先验碰巧答对的路径。 机制落地后，`AGENT-WORKFLOW` 拥有并版本化 workflow state、verifier receipt 与提交边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12571v1 — §4 Method; Evaluation=arXiv:2605.12571v1 — §5 Experiments; Non-proof=arXiv:2605.12571v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12571:end -->

<!-- source-family:SF-2026-ARXIV-2605-12694:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：lattice/worklist 将 LLM 生成的程序分析证据约束为单调、可合并的状态，而非自由文本判断。 机制落地后，`AGENT-WORKFLOW` 拥有并版本化 workflow state、verifier receipt 与提交边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12694v1 — §3.5 Worklist Algorithm; Evaluation=arXiv:2605.12694v1 — §2.1 Evaluation Graph and Claims; Non-proof=arXiv:2605.12694v1 — §6 Limitations, Future Work, and Open Questions；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12694:end -->

## `AGENT-MULTI-AGENT` — `books/part-07-agent/82-multi-agent.md`

本组从章节已有机制出发，把外部约束推进到 `sender/receiver belief state、消息与更新权限`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-12920:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：多 Agent 对话成功不等于私有 world models 对齐；应分别测 observation convergence、信息新颖性与 belief-sensitive messaging。 机制落地后，`AGENT-MULTI-AGENT` 拥有并版本化 sender/receiver belief state、消息与更新权限，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12920v1 — §Communication Architectures:; Evaluation=arXiv:2605.12920v1 — §3 World Models, Alignment, and Evaluation; Non-proof=arXiv:2605.12920v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12920:end -->

<!-- source-family:SF-2026-ARXIV-2605-12991:start -->
随后，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：单体 RLHF 的顺从性目标不能直接治理多 Agent 的相互迎合；评价必须观察交互中意见独立性、纠错与群体漂移。 机制落地后，`AGENT-MULTI-AGENT` 拥有并版本化 sender/receiver belief state、消息与更新权限，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.12991v1 — §4 Methods; Evaluation=arXiv:2605.12991v1 — §4.1 Experimental setup; Non-proof=arXiv:2605.12991v1 — §6 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-12991:end -->

<!-- source-family:SF-2026-ARXIV-2605-13839:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：多 Agent 通信不必只写入 receiver context；短暂的 receiver-specific weight delta 能承载建议，但把消息权限升级成参数写权限。 机制落地后，`AGENT-MULTI-AGENT` 拥有并版本化 sender/receiver belief state、消息与更新权限，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13839v1 — §3.5 Training Objective; Evaluation=arXiv:2605.13839v1 — §4 Experiments; Non-proof=arXiv:2605.13839v1 — §5 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13839:end -->

## `AGENT-PLATFORM` — `books/part-07-agent/84-agent-platform.md`

本组从章节已有机制出发，把外部约束推进到 `版本化状态、控制 owner 与验收边界`。以下顺序是同一设计线的递进，不表示后发机制覆盖旧方案。

<!-- source-family:SF-2026-ARXIV-2605-13295:start -->
首先，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：只按最终 Agent 成功给整条轨迹记账会掩盖局部贡献；对比相似轨迹差异可定位 credit，但 attribution 仍不能取代 outcome truth。 机制落地后，`AGENT-PLATFORM` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13295v1 — §Appendix C Pseudo Algorithm of Cantante; Evaluation=arXiv:2605.13295v1 — §4 Experiments; Non-proof=arXiv:2605.13295v1 — §4.5 Discussion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13295:end -->

<!-- source-family:SF-2026-ARXIV-2605-13716:start -->
最终，本组进一步，原路径在其输入稳定、任务边界封闭时仍然合理；新的压力在于：Skill library 增长后，创建、验证、版本、去重和退休不能继续由临时 prompt 管理；SkillOps 将其提升为持续维护的软件资产生命周期。 机制落地后，`AGENT-PLATFORM` 拥有并版本化 版本化状态、控制 owner 与验收边界，模型或论文方法只提出候选，不自动获得最终提交权。收益来自更细的状态分解与可归因控制，代价是增加额外状态、校准、计算或验证步骤；一旦状态过期、校准漂移、预算不足或输入超出支持分布，新路径会产生错误归因、错误提交或资源放大。此时应停止该分支，回退章节原有的保守路径，并保存失败回执。证据边界严格限定在 `Method=arXiv:2605.13716v1 — §3.3 Algorithm; Evaluation=arXiv:2605.13716v1 — §4 Experiments; Non-proof=arXiv:2605.13716v1 — §6 Conclusion；仅支持 exact-v1 披露范围。`，不把作者实验外推为生产定律。
<!-- source-family:SF-2026-ARXIV-2605-13716:end -->
