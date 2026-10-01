# 2026-04-28 arXiv 第二批：非作者双向准入校准

范围：独立读取 [作者第二批 30 项初筛](./V3_ARXIV_ADMISSION_BATCH2.md) 与 `arxiv-owner-replay-20260903/20260428/arxiv-owner-receipt.json` 中对应 30 项的完整题名、摘要；对有误排风险者只取官方 exact-v1 必要方法、评价和实际 Books 命题。另核 [首批](./V3_ARXIV_ADMISSION_BATCH1.md) 的 `2604.22901` 修订后关闭。此记录**只判断贡献准入**，不确认 first-public、撤稿、完整 Source Review、Books 或日级 Gate；“继续”也不等于冻结 Candidate Denominator。

## 需要作者修正的两项关闭

1. **`2604.23467v1`：从前分母关闭改为“继续核贡献”。** [官方 v1 §III Algorithm 1、§IV](https://arxiv.org/html/2604.23467v1) 不仅把静态算子放进 CUDA Graph、动态算子放进 JIT，还具体规定了 1–50 长度预捕获、graph miss 时 JIT 执行同时异步捕获、rolling graph buffer 的回收。这是 graph 执行计划在动态长度下的生命周期/未命中代价，当前 [Ch49 执行计划主线](../../../../../books/part-05-inference-system/49-tensorrt-llm.md) 只明确固定 graph 与动态执行的取舍，没有这一具体 rolling admission 分支。因此“没提出 graph invalidation 新条件”不是足够的排除理由。仍需审 graph key 是否包括 shape、地址、KV 版本及 capture/replay 同步，冷启动与 warm-start 是否分账。§IV–V 只有单 H100、LLaMA-2 7B、FP16、batch 1；作者以 CUDA Events/Nsight 报 TTFT，却主张 host dispatch 收益，不能直接采 1.02–5.90× 或普适服务结论。源码还把 KV 更新一概列为不能捕获的动态操作，这不是所有运行时的通用定理。**只恢复定点贡献核，不自动进入 Books。**
2. **`2604.23626v1`：从前分母关闭改为“继续核贡献”。** [官方 v1 §3.1–3.2、§4.3](https://arxiv.org/html/2604.23626v1) 明确将当前 workflow graph 与历史 query/response graph 经固定 `(LLM, role)` hub 相连，策略逐步联合选择 role 与 backbone；并实际提供 w/o History、homogeneous graph、heterogeneous graph、inductive/transductive 对照。作者原理由“未隔离图 memory 贡献”排除过早。当前 [Ch82 peer routing](../../../../../books/part-07-agent/82-multi-agent.md) 已有任务条件、能力 posterior、历史 outcome 与有界探索，故后续只核**联合 role/backbone 决策及历史图状态**相对 ledger 的真实设计差异，不因用了 GNN/PPO 入选。重要数值纠错：§4 把 `Cost` 定义为输入/输出 token 数乘模型价格；摘要“GPU cost 186.26 GiB→1.04 GiB”与该定义量纲不一致，不能作为显存或 GPU 资源收益引用。w/o History 同时改变状态信息量，尚不能单独归因图结构。**只恢复定点贡献核，不自动进入 Books。**

## 重点保留但必须收窄的判断

- **`2604.23366v1`**：保持“继续核贡献”，不升为 Agent 行动证据。[官方 v1 §4–5、§8.13](https://arxiv.org/html/2604.23366v1) 的 grounded/ungrounded/contradicted/complementary 四分法和 proceed/regenerate/replan 成本分层有实际机制，但 `regenerate` 是改写摘要、一次额外 LLM call；`replan` 才可能重新派发工具。FEVER gold Wikipedia evidence 和 judge 输出只测试决策代理，不证明实际多 Agent 执行或 remediation。其同一 FEVER 子集 contradiction catch-rate 明显低于 HHEM/RAGAS（Table 8），不可把“四分法”包装成全面更可靠。对照 [Ch76 sufficiency→re-query/abstain](../../../../../books/part-07-agent/76-rag.md) 后，只剩“不同证据类型改变恢复动作与成本”的待验增量。
- **`2604.23646v1`**：保持具体前分母关闭，但改掉“缺可定位威胁模型/实现范围”的错误说法。官方 [§2.2 threat model、§4.4 theorem dependency、§5](https://arxiv.org/html/2604.23646v1) 确实给出威胁模型、原型与六个条件证明；问题在于 T1/T3 假设签名不可伪造、无绕过路径、Hard Auth 正确，T6 还把 Policy LLM 不构造可越过阈值的假 lineage 写作 A11，因而未证明开放环境的真实 goal integrity。原型是 mock execution 与自建攻击/漂移/胁迫数据。其 typed action、capability、lineage、独立授权和 effect 前验证已经由 [Ch72 现有权限链](../../../../../books/part-06-ai-infrastructure/72-security.md) 具体承载；若日后有解除 A11 或绕过假设的新证据才重开，不能声称本文没有形式分析，也不能因六定理就采用无条件安全保证。
- **`2604.23478v1`**：当前前分母关闭仍可维持。官方 [v1 §3、§5](https://arxiv.org/html/2604.23478v1) 的 hand-validated paraphrase、极性反转模板以及 pairwise always-A 退化是真实、具体的测量陷阱，并非“只有又一个 benchmark”；但 [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已要求语义等价模板审计、variant spread、invalid/abstain 分账和选项排列。论文所测 9 judge/494 pairs 的局部反例没有改变这些已写的 admission 对象。关闭理由应保留上述实证边界，不能只写“已知稳定性主题”。

## 其余 26 项双向抽核

原“继续”11 项 `23150/23178/23205/23318/23333/23374/23455/23459/23466/23488/23581` 均有明确的大模型系统机制或评估反证入口；完整题摘未见仅因关键词、章节可映射或作者 headline 即准入。保持待官方 exact-v1、日期及实际 owner 核验，不将 11 项一起送全文。

原“继续核贡献”除 `23366` 外的 `23210/23238/23272/23553/23577/23584` 均保留**条件性**：安全反馈、稀疏 thought-anchor、防融合损失、cluster decode、路由训练反馈、视觉证据隐私各有可能的状态/评价边界，也各有低维任务、代理指标或已有机制的误收风险；先核作者文件列出的单一必要差异，不预设进入分母。

剩余前分母关闭 `23141/23172/23277/23280/23338/23483/23505/23543` 的题摘分别落在场景组合、局部 VQ-QAT、context compression 组合、治理/安全综述、特定 detector 改写和局部 preference steer；现有具体关闭理由未见遗漏长期 AI System 控制边界。`23483` 的二 Agent/二元反馈攻击只证明该 misinformation detector 管线可被多次改写搜索，不等同新的跨 Agent effect authority。这里不把“规模小”“已有章节”当作独立否决条件；关闭取决于其已披露机制相对项目长期判断无新增，命中独立反证时仍可定点重开。

## 首批 `2604.22901` 重开后关闭复核

[官方 exact-v1 §3.3/Algorithm 1、§4.3/Table 2、Limitations](https://arxiv.org/html/2604.22901v1) 确有 Fourier half-spectrum token、累计残差、event-intensity 选择刷新、周期 probe/error feedback，原“只是固定缓存”关闭不成立；作者已改正。真实对照 [Ch24 diffusion cache 主线](../../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 已有 trajectory-conditioned token refresh、误差预算、周期 full-forward anchor 与失配 full refresh。该论文的新划分/阈值仅在 3.2M 参数频域时间序列 score model 和五组时间序列上验收；Table 2 ECG 的 full cache `SW 0.015` 仍高于无 cache `0.014`，并非无损；作者明确未做跨 image/video DiT 的同预算 wall-clock 对照。**同意当前具体前分母关闭**，但理由是没有改变此项目现有 cache-validity 决策，而不是因时间序列/ECG 与 LLM 领域不同而硬拒。`2.2×` 不得外推端到端大模型 serving。

本批建议阶段表述：原 11 “继续”不变，7 “继续核贡献”增至 **9**（补 `23467/23626`），12 前分母关闭降至 **10**；这 20 个工作线索仍不是 20 个冻结候选。官方 v1 正文核验限上述重点和反向样本，不代表其余项已完成 Source Review。
