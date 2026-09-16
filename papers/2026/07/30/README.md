# Daily Research — 2026-07-30

**规范：** V3
**窗口：** 2026-07-29T09:00:00+08:00 ～ 2026-07-30T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T15:11:09+08:00

## 1. 结论

本窗官方 arXiv 公告共 467 个去重身份。旧报告把 136 项保留为候选；作者侧第一次收紧到 25 项后，独立抽检发现把“已有章节已经讨论同类问题”误当成了初筛排除理由。按当前贡献合同复查受影响主题后，最终保留 38 项，98 项降为分母前关闭。降级材料主要是 AI for Science、垂直应用、通用软件安全、只增加任务指标而未改变机制或适用边界的局部方法，以及只能映射 ROADMAP 名词但没有长期系统增量的工作。

保留材料形成六条系统线索：可复用推理状态必须绑定依赖与版本；训练和推理调度必须显式拥有预算、拓扑及提交边界；evaluation 结论不能脱离适用范围、有效期和部署决策任意组合；Agent/World Model 的 latent 或 memory 只有经因果干预与执行反馈才能获得更强语义；tokenization 与多模态统一架构仍会留下表示接口错配；低精度、异构内存和物理行动的收益必须绑定具体硬件与 workload。独立复核确认 26 项由既有正文具体命题承载、1 项只构成受限案例；其余 11 项机制增量已经按唯一 owner 写入 Books，并完成非作者写后核验。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-ANTHROPIC | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-GOOGLE-AI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-META-AI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-QWEN | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-DEEPSEEK | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-MOONSHOT | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-ZAI | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-MINIMAX | 当前注册入口在本历史窗口后生效 | 不适用 | 无 |
| SRC-ARXIV | 467 个去重身份；全标题巡检，含糊或高信号项读取完整摘要；独立复核抽查原 111 个降级项并扩查其共享理由，最终完成 38 项 exact-v1 证据审阅 | 已检查 | 无 |

候选 identity 以首次公开的 v1 为 owner；本轮没有比较后续修订前后。原始清单中的 `2606.24369` 已标为 withdrawn 并在进入候选前排除，38 个保留项均未见撤稿标记。后注册的机构入口不反向冒充七月覆盖。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [FinCacheServe](https://arxiv.org/html/2607.26076v1) | 2026-07-30T08:00:00+08:00 | 可变 RAG 依赖一致的答案缓存；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Projectibility in AI evaluation](https://arxiv.org/html/2607.26159v1) | 2026-07-30T08:00:00+08:00 | 评测推论的可组合条件；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Evaluation Scores Are Perishable Knowledge Claims](https://arxiv.org/html/2607.26191v1) | 2026-07-30T08:00:00+08:00 | 评测分数的 formality、scope 与 validity window；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Choosing Where and How to Moderate](https://arxiv.org/html/2607.26200v1) | 2026-07-30T08:00:00+08:00 | moderation 放置与重写的端到端合同；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Weak-to-Strong On-Policy Distillation](https://arxiv.org/html/2607.26246v1) | 2026-07-30T08:00:00+08:00 | 多弱教师的 on-policy 分支；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Early Verdicts, Better Budgets](https://arxiv.org/html/2607.26253v1) | 2026-07-30T08:00:00+08:00 | RLVR rollout 的序贯预算分配；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Fabric Is the Cluster Driver](https://arxiv.org/html/2607.26335v1) | 2026-07-30T08:00:00+08:00 | GPU–CXL 跨层 policy graph；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Incast-Free MoE Rate-Based Scheduling](https://arxiv.org/html/2607.26340v1) | 2026-07-30T08:00:00+08:00 | MoE collective 的主动速率控制；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Post-Training at the Edge of Detectability](https://arxiv.org/html/2607.26358v1) | 2026-07-30T08:00:00+08:00 | 用序贯可检测性解释并求解 KL 正则系数；2 + 2 + 2 = 6 | 深入完成 | 整合：TRAIN-RLHF，[Ch31](../../../../books/part-04-training-system/31-rlhf.md) |
| [Do Unified Multimodal Models Think in One Space?](https://arxiv.org/html/2607.26411v1) | 2026-07-30T08:00:00+08:00 | 用跨分支干预检验“统一架构等于统一语义空间”；2 + 2 + 2 = 6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [StrataCL](https://arxiv.org/html/2607.26444v1) | 2026-07-30T08:00:00+08:00 | buffer ownership 与 fabric-native collective；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Mergeable Model-Side Aggregation States](https://arxiv.org/html/2607.26448v1) | 2026-07-30T08:00:00+08:00 | 可合并的长上下文中间状态；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [ForgetBench](https://arxiv.org/html/2607.26455v1) | 2026-07-30T08:00:00+08:00 | 把参数知识编辑从一次成功扩展为 acquisition/retention/generalization 的时间过程；2 + 2 + 2 = 6 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [DualDecoder](https://arxiv.org/html/2607.26475v1) | 2026-07-30T08:00:00+08:00 | 稀疏 KV 的预测预取；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [LLMET](https://arxiv.org/html/2607.26491v1) | 2026-07-30T08:00:00+08:00 | 将 serving phase、working set 与新型片上 memory PPA 联合评估；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [HiFloat4](https://arxiv.org/html/2607.26515v1) | 2026-07-30T08:00:00+08:00 | rollout 与训练路径的端到端 FP4；2 + 3 + 2 = 7 | 深入完成 | 仅报告：尚无原生 FP4 硬件速度证据 |
| [Graph-Native Bitemporal Memory Store](https://arxiv.org/html/2607.26520v1) | 2026-07-30T08:00:00+08:00 | Agent memory 的 identity/version 分离；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Revisiting Lossy Verification in Speculative Decoding](https://arxiv.org/html/2607.26627v1) | 2026-07-30T08:00:00+08:00 | lossy verification 的分布偏差；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [NELSSA](https://arxiv.org/html/2607.26633v1) | 2026-07-30T08:00:00+08:00 | mixed-length 请求的 GPU/PNM placement；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Constitutional Midtraining](https://arxiv.org/html/2607.26654v1) | 2026-07-30T08:00:00+08:00 | 对齐内容进入 midtraining 的分支；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Enfold](https://arxiv.org/html/2607.26657v1) | 2026-07-30T08:00:00+08:00 | 训练期 imagination 塑形控制表示；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [ActSWM](https://arxiv.org/html/2607.26712v1) | 2026-07-30T08:00:00+08:00 | 暴露“预测相似但不响应动作”的 Context Collapse；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Do Latent Channels Actually Communicate?](https://arxiv.org/html/2607.26773v1) | 2026-07-30T08:00:00+08:00 | 多 Agent latent channel 的因果替换审计；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [CheckVLA](https://arxiv.org/html/2607.26789v1) | 2026-07-30T08:00:00+08:00 | action-conditioned 执行期验证；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Ripple](https://arxiv.org/html/2607.26818v1) | 2026-07-30T08:00:00+08:00 | 音视频流式生成的跨模态 recurrent memory；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Language Models are not Equally Robust to Non-Canonical Tokenization](https://arxiv.org/html/2607.26831v1) | 2026-07-30T08:00:00+08:00 | 证明 tokenizer identity 的脆弱性具有语言相关边界；2 + 2 + 2 = 6 | 深入完成 | 整合：MODEL-TOKENIZER，[Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [When Knowledge Changes](https://arxiv.org/html/2607.26843v1) | 2026-07-30T08:00:00+08:00 | 对动态 corpus 做关系约束的 metamorphic RAG 测试；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ReCo](https://arxiv.org/html/2607.26862v1) | 2026-07-30T08:00:00+08:00 | GRPO 分布集中后的梯度重加权；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Two Calls Beat Five Agents](https://arxiv.org/html/2607.26922v1) | 2026-07-30T08:00:00+08:00 | 等预算下协作与 self-refinement 比较；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [A Compositional Theory of Causally Masked Transformers](https://arxiv.org/html/2607.26988v1) | 2026-07-30T08:00:00+08:00 | 有限精度与求值顺序改变 causal Transformer 的可表达 memory；2 + 2 + 3 = 7 | 深入完成 | 整合：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [What Can Latent World Models Know?](https://arxiv.org/html/2607.27017v1) | 2026-07-30T08:00:00+08:00 | 预测目标决定物理参数可辨识性；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Lottery Tickets Are Not Deployment Tickets](https://arxiv.org/html/2607.27031v1) | 2026-07-30T08:00:00+08:00 | clean accuracy 等价不能授权固定决策逻辑下的模型替换；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GPTQ-2D](https://arxiv.org/html/2607.27042v1) | 2026-07-30T08:00:00+08:00 | Kronecker 双侧 adaptive rounding 的等价 cubic-time 执行；2 + 1 + 2 = 5 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [MemSecBench](https://arxiv.org/html/2607.27080v1) | 2026-07-30T08:00:00+08:00 | memory poisoning 的生命周期评测；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Scores Are Not Decisions](https://arxiv.org/html/2607.27083v1) | 2026-07-30T08:00:00+08:00 | 工具排序之后仍需按边际价值与异构成本决定停止；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [InferScale](https://arxiv.org/html/2607.27090v1) | 2026-07-30T08:00:00+08:00 | 个性化 serving 的可复用 KV 注入；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-VLLM，[Ch50](../../../../books/part-05-inference-system/50-vllm.md) |
| [A Photonic-CXL Memory Appliance](https://arxiv.org/abs/2607.27187v1) | 2026-07-30T08:00:00+08:00 | 用无交换机光纤 shuffle 扩展共享 KV memory pool；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [TurboVLA](https://arxiv.org/html/2607.27205v1) | 2026-07-30T08:00:00+08:00 | 从 LLM-centric `V→L→A` 改为轻量 `V+L→A` 执行分支；3 + 2 + 2 = 7 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

## 4. 证据与知识整合

**推理状态：复用收益来自更强 identity，而不是“缓存更多”**

### [FinCacheServe](https://arxiv.org/html/2607.26076v1)

把答案作为 materialized serving object，并绑定任务、证据 chunk、文档版本、tool output、模型与 decoding 配置；更新先推进版本，再经 reverse index 失效依赖答案。SEC-derived trace、Qwen2.5 7B/14B/32B 与 2 秒 SLO replay 只支持该设置下未观察到 dependency-stale serve，不证明答案事实正确或其他语料的命中率。代价是 metadata linearization、false miss、失效 fan-out 与租户隔离。Ch76 已将依赖 identity、invalidation 和 evidence provenance 写入 RAG cache 主线。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26076v1#S3 — 3 System model and consistency target; https://arxiv.org/html/2607.26076v1#S4 — 4 FinCacheServe design。Evaluation：https://arxiv.org/html/2607.26076v1#S6 — 6 Experimental methodology; https://arxiv.org/html/2607.26076v1#S7 — 7 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26076v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.26076v1#S8 — 8 Discussion。 取舍与回退：依赖版本、反向索引与租户边界会增加 metadata linearization 和失效 fan-out；任何依赖身份缺失、版本不一致或 provenance 不能重建时，应绕过答案缓存并重新检索与生成。

### [Mergeable Model-Side Aggregation States](https://arxiv.org/html/2607.26448v1)

长上下文分片先形成可合并中间状态，再由模型内路径聚合；作者 Oolong-Synth 子集结果证明受测模型能利用该状态，不证明任意任务都满足结合性或顺序不敏感。它以训练/接口约束换较小上下文压力。Ch22 已区分外部压缩、模型侧状态与可合并性。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26448v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.26448v1#A7 — Appendix G Statistical Analysis and Evaluation Scope; https://arxiv.org/html/2607.26448v1#A7.SS1 — G.1 Evaluation and statistical analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26448v1#S6 — 6 Conclusion。 取舍与回退：可合并状态要求训练出的聚合算子与任务顺序假设同时成立；无法验证结合性、顺序敏感性或模型兼容时，应回退到原始上下文重放或保序的层次压缩。

### [DualDecoder](https://arxiv.org/html/2607.26475v1)

利用相邻 decode step 的稀疏 KV 索引可预测性，从 host 提前预取下一步候选；作者最高吞吐提升不能外推到不同 sparsity、互联和 tail-SLO。预测错误、额外 decoder 与 host bandwidth 是新增压力。Ch45 已把 residency、prefetch、miss recovery 和 cache identity 作为同一读取合同。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26475v1#S5 — 5. DualDecoder Design; https://arxiv.org/html/2607.26475v1#S5.SS1 — 5.1. System Overview。Evaluation：https://arxiv.org/html/2607.26475v1#S3.SS2 — 3.2. Memory Capacity Analysis; https://arxiv.org/html/2607.26475v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26475v1#S8 — 8. Conclusion。 取舍与回退：预测预取用额外 decoder、host bandwidth 与错误预取占用换取隐藏 miss latency；命中率或带宽余量不足时，应关闭预测路径并恢复 demand fetch 与常规 residency 管理。

### [InferScale](https://arxiv.org/html/2607.27090v1)

用训练出的 writer 生成可被目标模型消费的 KV，避免每次把个性化记忆重新 prefill；LoCoMo 上的 TTFT/吞吐结果绑定三种 open-weight 模型和披露的 k。它不证明任意文本可无损变为 KV，writer/reader、position、layout 与 memory revision 必须兼容。Ch50 已明确 external KV 的 semantic compatibility、tier ownership 与 scheduler admission。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27090v1#S3 — 3. InferScale Design; https://arxiv.org/html/2607.27090v1#A4 — Appendix D Larger-Model (Qwen3-14B) Results。Evaluation：https://arxiv.org/html/2607.27090v1#A1 — Appendix A Full Serving-Latency Results; https://arxiv.org/html/2607.27090v1#A4 — Appendix D Larger-Model (Qwen3-14B) Results。Limitations / counterevidence：https://arxiv.org/html/2607.27090v1#S7 — 7. Conclusion。 取舍与回退：外部 KV 把文本重算成本换成 writer/reader、位置编码、layout 与 memory revision 的强兼容约束；任一身份不匹配时，应丢弃 KV 产物并从可审计原文重新 prefill。

**训练与通信：优化的是预算和提交边界**

### [Weak-to-Strong On-Policy Distillation](https://arxiv.org/html/2607.26246v1)

多个弱模型给强 student 的 on-policy trajectory 提供蒸馏信号；证据只支持作者模型与任务，不证明弱教师组合天然优于强教师或离线 SFT。它以在线 rollout 成本、teacher bias 和 policy drift 换当前分布覆盖。Ch29/Ch33 已将 on-policy distillation 放在结构改变后的行为恢复分支。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26246v1#A3 — Appendix C Implementation Details; https://arxiv.org/html/2607.26246v1#A4.SS2 — D.2 Performance with Different Scales of Base Models。Evaluation：https://arxiv.org/html/2607.26246v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.26246v1#A4.SS1 — D.1 Runtime Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26246v1#S6 — 6 Conclusion。 取舍与回退：弱教师组合扩大 on-policy 覆盖，但会继承 teacher bias、增加 rollout 成本并随 student policy 漂移；收益不能稳定复现时，应回退到离线 SFT 或单一可审计教师基线。

### [Early Verdicts, Better Budgets](https://arxiv.org/html/2607.26253v1)

在 rollout 过程中依据已观察 reward 逐步决定是否继续为某 prompt 分配样本；1.5B/3B、数学与规划、单 GPU 结果支持比固定 dynamic sampling 少用 rollout，不形成通用预算比例。早停误判会丢掉稀有成功，policy 漂移会使难度估计过期。Ch33 已要求以固定采样预算为统计单位并按饱和/不确定性分配 sampling work。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26253v1#A1 — Appendix A Use of Large Language Models; https://arxiv.org/html/2607.26253v1#A4 — Appendix D Algorithm and Implementation Details。Evaluation：https://arxiv.org/html/2607.26253v1#A3 — Appendix C Proofs and Theoretical Analysis; https://arxiv.org/html/2607.26253v1#A5 — Appendix E Detailed Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26253v1#A7 — Appendix G Discussion, Limitations, and Future Work; https://arxiv.org/html/2607.26253v1#S5 — 5 Conclusion。 取舍与回退：按早期 verdict 停止 rollout 能节省预算，却可能系统性丢掉迟到的稀有成功并使难度估计过期；应保留固定采样基线、最低探索配额与定期重估。

### [The Fabric Is the Cluster Driver](https://arxiv.org/html/2607.26335v1)

把跨 GPU、driver、NIC/DPU 与 CXL hook 的动作编译为带 ownership、ordering 和 transformation 的 semantic movement graph；这是受限 policy runtime，不证明 memory-safe policy 在语义或性能上正确。可编程性换来 verifier、版本和回退复杂度。Ch36 已规定 versioned collective policy 只能在授权选择空间内运行，不能改写 tensor/group/step identity。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26335v1#S3 — 3. Design; https://arxiv.org/html/2607.26335v1#S3.SS4 — 3.4. LLM Prefill Across Three Architectures。Evaluation：https://arxiv.org/html/2607.26335v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.26335v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26335v1#S4.SS6 — 4.6. Failure and Fallback; https://arxiv.org/html/2607.26335v1#S7 — 7. Discussion。 取舍与回退：可编程 movement graph 提高异构 fabric 的选择空间，也把 verifier、版本、授权与故障恢复纳入关键路径；策略无法证明保持 collective identity 与 ordering 时，应使用固定 collective/transport 路径。

### [Incast-Free MoE Rate-Based Scheduling](https://arxiv.org/html/2607.26340v1)

用接收端约束和主动 rate allocation 避免 many-to-one oversubscription；模拟中的近满链路利用率不等于真实多租户 fabric 或故障下保证。速率估计误差、公平性和控制稳定性是代价。Ch36 已把 topology、congestion、participant ordering 与 completion 置于 communication runtime 所有权下。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26340v1#S2.SS3 — 2.3. Frameworks; https://arxiv.org/html/2607.26340v1#S7 — 7. Impact on Future Network Architectures。Evaluation：https://arxiv.org/html/2607.26340v1#S6 — 6. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.26340v1#S7 — 7. Impact on Future Network Architectures。 取舍与回退：主动速率分配避免 incast，但依赖及时的接收端容量估计并可能引入公平性和控制振荡；遥测陈旧或故障时，应回退到保守静态限速与 receiver-side backpressure。

### [StrataCL](https://arxiv.org/html/2607.26444v1)

让通信库直接管理用户 buffer 的注册、可见性与 fabric path，减少复制/重复注册；作者三类 workload 的数字只属于其 supernode。更紧的 buffer/runtime 耦合扩大了 pinning、lifetime、故障隔离和 portability 成本。Ch36 已区分 buffer ownership、collective semantics、runtime 和 transport。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26444v1#S2.SS1 — 2.1. Supernode Architectures; https://arxiv.org/html/2607.26444v1#S4 — 4. Design Overview。Evaluation：https://arxiv.org/html/2607.26444v1#A1 — Appendix A Extended Microbenchmark; https://arxiv.org/html/2607.26444v1#A3 — Appendix C Workload Partitioning Overhead Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26444v1#S11 — 11. Conclusion。 取舍与回退：通信库接管用户 buffer 可减少复制和注册，但扩大 pinning、lifetime、隔离与可移植性责任；生命周期或访问边界不能证明时，应使用 runtime 管理的已注册 staging buffer。

### [HiFloat4](https://arxiv.org/html/2607.26515v1)

展示 rollout 与 forward/backward 都使用模拟 FP4 的 RL post-training 路径；论文明确没有原生 FP4 硬件，因而不能证明实际训练加速或能效收益。它仍提示低精度必须贯穿 policy identity、optimizer/error compensation 与 rollout parity；在硬件证据出现前仅保留报告，不写成长效结论。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26515v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.26515v1#S5 — 5 Experiments; https://arxiv.org/html/2607.26515v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26515v1#S6 — 6 Limitations and Future Directions; https://arxiv.org/html/2607.26515v1#S7 — 7 Conclusion。 取舍与回退：模拟 FP4 只能验证数值路径，不能证明原生硬件上的吞吐、能效或故障特征；在真实 kernel、设备和端到端训练证据出现前，应保留 BF16/FP8 可复现基线。

### [ReCo](https://arxiv.org/html/2607.26862v1)

在 rollout 已采样后重加权 GRPO gradient，以缓解高频轨迹支配与 Pass@k coverage 收缩；它不改变 sampling distribution 本身，也不证明跨任务稳定。权重估计会放大噪声并引入 variance。Ch33 已承载 support concentration、importance/reweighting 边界及 held-out coverage 验收。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26862v1#A2.SS3 — B.3 Combining ReCo with Existing GRPO Methods; https://arxiv.org/html/2607.26862v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.26862v1#A1.SS2 — A.2 Evaluation Details; https://arxiv.org/html/2607.26862v1#A2 — Appendix B Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26862v1#Sx1 — Limitations and Discussion; https://arxiv.org/html/2607.26862v1#S6 — 6 Conclusion。 取舍与回退：事后重加权可抑制高频轨迹支配，却会放大稀有样本噪声和 gradient variance，且不修复采样分布本身；不稳定时应回退到未加权 GRPO，并从采样多样性和 held-out coverage 处理根因。

### [Constitutional Midtraining](https://arxiv.org/html/2607.26654v1)

把对齐内容放入 midtraining，作者结果显示部分倾向在后续微调后仍保留；实验不证明内容出现位置的因果机制可推广到其他价值、模型与数据。与普通 pretraining 共存时需保留 data provenance、contamination 和 post-training 独立评估，Ch28 已覆盖 objective/data coupling。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26654v1#S2.SS2 — 2.2 Constitutional Approaches to Alignment; https://arxiv.org/html/2607.26654v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.26654v1#A3 — Appendix C Centrality Analysis: Additional Detail; https://arxiv.org/html/2607.26654v1#A6 — Appendix F Evaluation: Extended Detail。Limitations / counterevidence：https://arxiv.org/html/2607.26654v1#S5.SS6 — 5.6 Limitations and Future Work.; https://arxiv.org/html/2607.26654v1#A3.SS5 — C.5 Limitations of the Centrality Measure。 取舍与回退：把对齐信号前移到 midtraining 可能获得更持久的倾向，也会耦合预训练数据 provenance、污染和后续能力保持；因果归属不清时，应回退到隔离数据的 post-training 与独立安全评估。

### [Post-Training at the Edge of Detectability](https://arxiv.org/html/2607.26358v1)

论文把“reward 最大、又不希望 policy 离 reference 太远”的启发式 KL 系数，重写成 policy 与序贯检测 monitor 的对策：均衡解仍对应 KL-regularized RL，并用 stochastic bisection 搜索隐含系数。§5、Appendix C 的 Qwen3-8B/Llama-3.2-1B、LoRA+GRPO 实验只支持所测 continual-learning reward/retention 和 API auditing 设置；oracle SPRT 还使用真实 deployed policy，不能视为生产可用基线。该方法没有证明“难以检测”就是安全或能力保留，也没有消除 monitor misspecification。它以额外 rollout、likelihood 估计和检测假设换掉手工 beta 搜索。Ch31 现已在既有 beta 与平均 KL 讨论之后补入“可检测性预算”这一条件分支，并保留固定 beta、显式行为切片和独立安全 gate 作为可审计基线。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26358v1#A3.SS2 — C.2 Model Auditing; https://arxiv.org/html/2607.26358v1#S5.SS2 — 5.2 Model Auditing。Evaluation：https://arxiv.org/html/2607.26358v1#A3 — Appendix C Appendix for Section 5 : Experiments; https://arxiv.org/html/2607.26358v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26358v1#S7 — 7 Conclusions and Future Research。 取舍与回退：以可检测性定义正则预算会减少手调 beta，却把 monitor 假设、likelihood 估计和额外 rollout 引入目标；monitor 失配或 oracle 不可实现时，应回退到固定 beta、显式行为切片和独立 release gate。

**参数知识：一次编辑成功不等于长期保留**

### [ForgetBench](https://arxiv.org/html/2607.26455v1)

把 continual knowledge editing 表示为有序 update stream，并分别测 acquisition、retention、temporal decay、cross-instance stability 与 query generalization。§5.1 的 6,431 个合成/半合成问题和 §5.2 的多模型、多编辑方法结果支持“高 retention 可同时伴随严重 generalization 退化”，不能证明某种编辑算法在真实知识更新中必然失败；§6 也明确限制在合成 profile、特定 QA 构造和有限模型。该分解用更长的顺序测试与数据生成成本换取失效归因。Ch5 现已把连续参数编辑拆成 acquisition、retention、temporal decay 与 generalization 的时间合同；Agent 外部 Memory 的 lifecycle 仍不代替参数记忆 owner。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26455v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.26455v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.26455v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26455v1#S6 — 6 Conclusion。 取舍与回退：流式编辑评估能暴露时间衰减与跨实例失效，但需要更长序列、稳定时钟和额外查询成本；参数记忆无法维持 retention/generalization 时，应回退到有版本与 provenance 的外部知识存储。

**Serving 与执行：硬件收益必须绑定 workload**

### [NELSSA](https://arxiv.org/html/2607.26633v1)

按请求长度把 decode 放置到 GPU 或 processing-near-memory 设备；mixed-length 实验支持受测配置的 throughput/tail 改善，不证明静态阈值能适应线上漂移。跨设备 state transfer、routing error 与 PNM capacity 成为新瓶颈。Ch56 已把 request shape、residency、transfer cost 和 tail-SLO 统一到 state-aware placement。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26633v1#S3 — 3. Design Principles and Architecture Overview; https://arxiv.org/html/2607.26633v1#S5.SS1 — 5.1. NELSSA System Architecture。Evaluation：https://arxiv.org/html/2607.26633v1#S8 — 8. Experimental Results; https://arxiv.org/html/2607.26633v1#S7 — 7. Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.26633v1#S10 — 10. Discussion; https://arxiv.org/html/2607.26633v1#S11 — 11. Conclusion。 取舍与回退：异构放置可利用 PNM 容量，却会产生跨设备 state transfer、阈值漂移和新的排队点；placement 置信不足或迁移成本压过收益时，应回退到 GPU-only 或保守静态分配。

### [Revisiting Lossy Verification in Speculative Decoding](https://arxiv.org/html/2607.26627v1)

形式化放松 exact distribution matching 后的 per-token/per-position gap；结论只覆盖论文定义的 truncation/collaboration rules。速度换来质量分布偏移，验证阈值成为产品语义而非纯优化参数。Ch48 已区分 exact speculative commit 与近似分支及其 rollback/evaluation contract。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26627v1#S1 — 1 Introduction; https://arxiv.org/html/2607.26627v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.26627v1#A2 — Appendix B Verification Analysis; https://arxiv.org/html/2607.26627v1#A3 — Appendix C Extended Results。Limitations / counterevidence：https://arxiv.org/html/2607.26627v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.26627v1#Sx1 — Limitations。 取舍与回退：放松验证可提高 speculative acceptance，却直接改变输出分布并让阈值成为产品语义；无法接受或度量该偏差时，应恢复 exact verification 与原始目标模型提交路径。

### [LLMET](https://arxiv.org/html/2607.26491v1)

§3 将 model/operator trace、capacity-aware mapping、RF/L1/L2/DRAM/link traffic、cycle count 与技术特定 PPA 串成同一个 cross-layer evaluator；§4 的 A100、B200-like 与 Orin-like studies 表明增加片上 cache 只有在 phase-specific working-set knee 之前持续节能，prefill/decode、context 和平台会改变拐点。结果来自 RTL synthesis、NeuroSim 投影和模拟，未证明 M3D memory 已在对应容量、频率和热约束下制造，更不能把 44%/24%/30% 外推到其他芯片。它以电路/系统模型假设和更复杂 mapping search 换设计期可比较性。Ch54 现已把 on-chip capacity、operator mapping、serving phase 与 working-set knee 接入既有 HBM/DRAM/CXL/NVMe 层级，并明确模拟不能替代制造和实机证据。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26491v1#S2.SS1 — 2.1. LLM Serving Architecture; https://arxiv.org/html/2607.26491v1#S3 — 3. Proposed LLMET Framework。Evaluation：https://arxiv.org/html/2607.26491v1#S4 — 4. Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.26491v1#S6 — 6. Conclusion and Future Work。 取舍与回退：跨层 evaluator 能提前探索设计空间，但其收益依赖 mapping、技术参数和仿真模型，无法替代制造与实机；模型校准不足时，应以已测硬件 profile 与 reference simulator 作为决策基线。

### [GPTQ-2D](https://arxiv.org/html/2607.27042v1)

§4.2 证明 anti-diagonal sweep 在 Kronecker 双侧二次度量下产生与向量化 fixed-order rounding 相同的矩阵，并把 dense sweep 从 quartic 降为 cubic；§6 明确它只解决“给定左右 basis 后如何执行 rounding”，不解决 Hessian factor 如何估计，也没有给出 LLM quality、GPU kernel 或端到端 latency 证据。并行 anti-diagonal 暴露更多临时状态和数值顺序，精确等价还依赖 basis、arithmetic 与 traversal 假设。Ch49 现已把“选择误差度量”与“忠实执行既定 rounding trajectory”拆为不同责任，并明确该理论复杂度结果不是已验证的部署加速。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27042v1#A1 — Appendix A Nested Algorithm; https://arxiv.org/html/2607.27042v1#S4.SS2 — 4.2 GPTQ-2D Algorithm。Evaluation：https://arxiv.org/html/2607.27042v1#S4 — 4 Theoretical Results。Limitations / counterevidence：https://arxiv.org/html/2607.27042v1#S6 — 6 Applications and Discussion。 取舍与回退：anti-diagonal 并行减少理论计算量，却暴露更多中间状态与浮点顺序，并依赖固定 basis；任何等价前提被自适应 scaling 破坏时，应回退到 serial/fixed-order reference rounding。

### [A Photonic-CXL Memory Appliance](https://arxiv.org/abs/2607.27187v1)

精确 v1 PDF §III–V 用 passive optical fiber shuffle 替代 electrical CXL switch，并让 16 hosts 以 offset-addressed shared region、DAX/CUDA registration 与 rendezvous ordering 读写 KV；§IV 的硬件 emulation 支持受测 module 的 bandwidth/latency，§VI 的 LLMServingSim 才产生 300 并发会话与 6.6× TTFT 结果。§VIII 明确 physical appliance 上的端到端 inference、vLLM/SGLang connector 和 multi-host validation 尚未完成，因此不能宣称 32 TB 拓扑已在生产工作负载成立。它用光学器件、共享 allocator/coherence 和故障域复杂度换去交换机层级与 eviction cliff。Ch54 现已在片上 working-set 之后继续到 photonic full-crossbar shared tier，显式保存 offset identity、rendezvous ordering、故障语义及“emulation 参数进入 serving simulation”的证据边界。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/pdf/2607.27187v1#page=5 — PDF page 5, Photonic Fabric Memory Appliance architecture; https://arxiv.org/pdf/2607.27187v1#page=8 — PDF page 8, DAX mapping and multi-host shared-memory data path。Evaluation：https://arxiv.org/pdf/2607.27187v1#page=3 — PDF page 3, repeated-request characterization matrix; https://arxiv.org/pdf/2607.27187v1#page=6 — PDF page 6, emulation methodology; https://arxiv.org/pdf/2607.27187v1#page=9 — PDF page 9, LLMServingSim workload and results。Limitations / counterevidence：https://arxiv.org/pdf/2607.27187v1#page=10 — PDF page 10, VIII Limitations and Future Work。 取舍与回退：光学 full-crossbar 去掉交换层级，却引入器件、共享 allocator、coherence 与跨主机故障域；未完成真实 appliance 与 connector 验证时，应保留电交换或节点本地 KV tier 作为生产回退。

**Evaluation 与安全：局部证据不能自动升级为系统结论**

### [Projectibility in AI evaluation](https://arxiv.org/html/2607.26159v1)

指出前一研究的 system、population、outcome 或条件常与下一推论目标不同，共享数据/模型 lineage 还会破坏独立性；已知真值示例说明 aggregate stability 可掩盖投影所需差异，但不是自动判断任意 benchmark 是否可外推的算法。Ch66 已要求证据绑定 object、distribution、environment、scorer，并禁止跨 measurement inference 静默组合。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26159v1#S2.SS3 — 2.3 What projectibility adds to neighbouring frameworks; https://arxiv.org/html/2607.26159v1#S4.SS3 — 4.3 A confirmatory local design。Evaluation：https://arxiv.org/html/2607.26159v1#S4.SS1 — 4.1 The source result and the proposed use; https://arxiv.org/html/2607.26159v1#S4.SS4 — 4.4 Hypothetical results and their inferential status。Limitations / counterevidence：https://arxiv.org/html/2607.26159v1#S8 — 8 Limitations; https://arxiv.org/html/2607.26159v1#S9 — 9 Conclusion。 取舍与回退：projectibility 检查限制了无依据外推，但需要明确目标 population、outcome 与 lineage，可能得出“不可投影”而非新结论；条件不匹配时，应只保留原实验域内结论并重新采样目标场景。

### [Evaluation Scores Are Perishable Knowledge Claims](https://arxiv.org/html/2607.26191v1)

§2–4 将 evaluation signal 明确拆成 formality、scope 与 validity window，并用四级 harness 与 HELM 54 个模型/10 个 scenario 的 mean-vs-weakest-link 排名差异说明 aggregation rule 能改变结论。它是一篇 position paper；Limitations 明确没有大规模实证验证，0.7× reliability multiplier、expiration date 和 weakest-link endpoint 都不是已校准通用规则。可长期保留的是“每个分数必须携带证据等级、适用域、有效期与聚合算子”，而非采用作者的固定权重。Ch66 已要求 EvalSpec、scope、aggregation、stale/unreproducible evidence，足以承载该约束，因此判已有覆盖。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26191v1#S3 — 3 Evaluation as epistemic system。Evaluation：https://arxiv.org/html/2607.26191v1#S2 — 2 Trust inflation in evaluation; https://arxiv.org/html/2607.26191v1#S3 — 3 Evaluation as epistemic system。Limitations / counterevidence：https://arxiv.org/html/2607.26191v1#Sx1 — Limitations。 取舍与回退：为分数携带 scope、有效期和聚合算子提高可审计性，也增加元数据维护与重跑成本；规则尚未校准时，应保留原始分项结果和范围声明，不采用固定 multiplier 或自动过期决策。

### [When Knowledge Changes](https://arxiv.org/html/2607.26843v1)

§3 把 RAG 建模为依赖动态 corpus 与 configuration 的 stateful pipeline，并定义 11 种 pre-chunk/post-chunk mutation 及相应 metamorphic relation；§5–6 在五个数据集和 28k+ mutants 上进行 ground-truth meta-evaluation，§8 报告 judge、样本组成和随机性威胁。该结果证明在作者 mutation distribution 中，静态 RAGAS 指标会漏掉一部分“语料改变后应保持或应改变”的关系，不证明 11 种 mutation 覆盖真实 corpus evolution，也不证明 LLM judge 是真值。它用成对执行、mutation generation 与 oracle 校准换无需逐例 gold answer 的 regression signal。Ch66 现已作为 canonical owner 把 corpus mutation、成对执行和 metamorphic relation 连接成动态 RAG regression contract；Ch76 继续只拥有 corpus revision 与 invalidation 的运行时交接。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26843v1#S2.SS2 — 2.2. Evaluation of RAG Systems; https://arxiv.org/html/2607.26843v1#S3 — 3. System Model and Fault Taxonomy。Evaluation：https://arxiv.org/html/2607.26843v1#S2.SS2 — 2.2. Evaluation of RAG Systems; https://arxiv.org/html/2607.26843v1#S5 — 5. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26843v1#S8 — 8. Threats to Validity; https://arxiv.org/html/2607.26843v1#S9 — 9. Conclusion。 取舍与回退：metamorphic RAG 回归减少逐例 gold answer 依赖，但需要 mutation 生成、成对执行和 judge 校准；relation 或 oracle 不可信时，应回退到人工核验的 gold regression set 与静态基线。

### [Lottery Tickets Are Not Deployment Tickets](https://arxiv.org/html/2607.27031v1)

论文把“稀疏 challenger clean accuracy 匹配 dense incumbent”与“固定 downstream decision logic 可不经重配直接替换”分开。§4 的 CIFAR/Imagenette/Flowers/FGVC、ResNet/ViT/ConvNeXt 试验和理论只支持作者固定 threshold policy 下仍出现 7%–10% accept/review churn；它没有隔离所有变化都由 sparsity 引起，也没有证明每次 churn 都有害或结论可直接外推到 LLM。可迁移的系统增量是 replacement gate 必须检查 threshold-adjacent score movement、calibration/OOD 与实际 policy outcome，而不能只看平均 accuracy。Ch66 现已补入“指标等价不自动意味着部署兼容”的替换合同，并保留无阈值连续表示场景下旧验收路径的成立条件。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27031v1#Sx1 — Introduction; https://arxiv.org/html/2607.27031v1#Sx2 — Behavioral Compatibility Audit。Evaluation：https://arxiv.org/html/2607.27031v1#A1.SSx3 — Theoretical Results; https://arxiv.org/html/2607.27031v1#A1.SSx5 — Experimental Protocol and Reproducibility。Limitations / counterevidence：https://arxiv.org/html/2607.27031v1#A1.SSx11 — Limitations and Future Extensions; https://arxiv.org/html/2607.27031v1#A1.SSx9 — Additional Discussion。 取舍与回退：替换 gate 检查阈值附近行为会增加 shadow/canary 与策略级观测成本；兼容性无法证明时，应保持 incumbent，先校准 challenger 或重设 downstream threshold 再切换。

### [Choosing Where and How to Moderate](https://arxiv.org/html/2607.26200v1)

用最终 usefulness 与 harmful exposure 比较 pre-routing、post-generation 和 rewriting；作者数据支持某些 probe routing 在相近 outcome 下更低延迟，却没有覆盖有害/无关 rewrite 的完整 grader sensitivity。前置过滤节省计算但信息少，后置过滤语义足但可能已流式暴露。Ch72 已写明 sensor 时机、gateway authority、streaming exposure 与 effect-time gate。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26200v1#A8 — Appendix H Rewrite Method Definitions and Offline Preparation; https://arxiv.org/html/2607.26200v1#S3 — 3 Evaluation Framework。Evaluation：https://arxiv.org/html/2607.26200v1#S3 — 3 Evaluation Framework; https://arxiv.org/html/2607.26200v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26200v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26200v1#Sx1 — Limitations。 取舍与回退：前置 moderation 延迟低但信息少，后置 moderation 语义充分却可能已产生流式暴露；单点 sensor 无法覆盖风险时，应采用前置粗筛、提交前复核和流式缓冲的分层回退。

**World Model、Multimodal 与 Agent：表示不是事实，验证也不是执行权**

### [Graph-Native Bitemporal Memory Store](https://arxiv.org/html/2607.26520v1)

用稳定 Memory identity 和 append-only versions 分离 current/as-of retrieval；60 问样本只证明原型能表达更新与时间查询，不能证明隐私、删除、多写者一致性或生产索引成本。版本化增加存储和检索稀释，Ch77 已承载 transaction time、valid time、provenance 与 repair。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26520v1#S3.SS1 — III-A Data Model; https://arxiv.org/html/2607.26520v1#S3.SS2 — III-B Bitemporal Model; https://arxiv.org/html/2607.26520v1#S4.SS2 — IV-B Agent Tool-Use Loop。Evaluation：https://arxiv.org/html/2607.26520v1#S5.SS1 — V-A Benchmark and Protocol; https://arxiv.org/html/2607.26520v1#S5.SS2 — V-B Results; https://arxiv.org/html/2607.26520v1#S5.SS5 — V-E Temporal Reasoning and the Dilution Effect。Limitations / counterevidence：https://arxiv.org/html/2607.26520v1#S6 — VI Conclusion; https://arxiv.org/html/2607.26520v1#S6.SS2 — VI-B Future Directions。 取舍与回退：双时间版本化支持 current/as-of 查询，却增加存储、索引稀释和多写者冲突；无法提供一致性、删除或访问控制时，应限制为单写 append-only，并保留可回放源记录。

### [Language Models are not Equally Robust to Non-Canonical Tokenization](https://arxiv.org/html/2607.26831v1)

§4 保持底层字符串不变，只改变送入模型的合法 token segmentation；§5 在 27 种语言、六类任务和 Llama-3.1-8B/Qwen3-8B/Gemma-3-12B 上观察到不同程度的下降，§7 的 LoRA multi-tokenization 只在 Multilingual-ARC 训练集上验证缓解。Limitations 明确没有隔离 vocabulary allocation、resource level 与 pretraining representation 的独立贡献。因此它证明 tokenizer 与 model checkpoint 是联合接口，不能把英语下的 segmentation invariance 当普遍性质；不证明随机非规范分词是现实故障分布或单一增强策略普遍有效。Ch11 现已把 tokenizer revision、normalization 与 segmentation policy 绑定 checkpoint，并加入“同字符串、不同合法分词”的跨语言行为回归及 canonical tokenizer 回退。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26831v1#S3 — 3 Methodology; https://arxiv.org/html/2607.26831v1#A1 — Appendix A Model Size And Budget。Evaluation：https://arxiv.org/html/2607.26831v1#A3 — Appendix C Results on Excluded Languages; https://arxiv.org/html/2607.26831v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26831v1#S8 — 8 Conclusion; https://arxiv.org/html/2607.26831v1#Sx1 — Limitations。 取舍与回退：多分词增强可提高非规范 segmentation 鲁棒性，但增加训练成本且可能偏离真实故障分布；无法证明迁移收益时，应保持 canonical tokenizer/checkpoint 配对并以行为回归守住接口。

### [A Compositional Theory of Causally Masked Transformers](https://arxiv.org/html/2607.26988v1)

论文把有限精度 causal attention 写成逐位置更新的有限内部 memory，并用 semigroup composition 连接 attention type 与可识别语言；§7 明确限制于无位置编码、显式 arithmetic semantics，free-wiring 等条件也影响 tightness。它不证明普通带位置编码 LLM 的完整表达能力，也没有训练或下游 benchmark。可保留的增量是：causal Transformer 的 expressivity 取决于实际有限精度 accumulator、更新次序与每层组合，而不只是实数域公式或参数量。Ch18 现已补入 implemented memory semantics：讨论 expressivity 或等价 kernel 时同时声明抽象算子与有限精度执行语义，无法证明等价时回退 reference path 与行为回归。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26988v1#A2 — Appendix B NoPE Transformer Architecture。Evaluation：https://arxiv.org/html/2607.26988v1#S5.SSx3 — The Importance of Evaluation Order。Limitations / counterevidence：https://arxiv.org/html/2607.26988v1#S7 — 7 Discussion。 取舍与回退：有限精度语义让表达能力结论更贴近实现，也使证明依赖无位置编码、arithmetic 与 wiring 假设；超出假设时，应回退到 reference operator 和端到端行为等价测试。

### [Do Latent Channels Actually Communicate?](https://arxiv.org/html/2607.26773v1)

在 sender representation 进入 receiver 的边界做 matched、mismatched、zero/random replacement，区分“依赖 latent”与“传递正确队友信息”；aggregate accuracy 不能替代这一因果判断。干预增加评测成本并可能造成 off-manifold 输入。Ch82 已包含同类配对替换与 budget-normalized topology comparison。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26773v1#Sx3 — The Audit Framework。Evaluation：https://arxiv.org/html/2607.26773v1#Sx4 — Experiments and Results; https://arxiv.org/html/2607.26773v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.26773v1#Sx5 — Conclusion。 取舍与回退：替换干预能区分真正通信与相关性，但可能制造 off-manifold latent 并增加组合评测成本；干预有效性无法校准时，只能报告观察性结果，不能升级为因果通信结论。

### [Enfold](https://arxiv.org/html/2607.26657v1)

在训练期让 future-observation objective 塑形 policy representation，部署时避免在线 imagination；表示分析只支持作者环境中的 long-horizon signal，不证明 latent 是环境真值或在 distribution shift 下仍可控。它用训练耦合换推理速度，Ch25 已区分 predictive feature、action-relevant state 与真实 observation fallback。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26657v1#S4 — 4 Method; https://arxiv.org/html/2607.26657v1#A2.SS1 — B.1 Benchmarks and Model Configuration。Evaluation：https://arxiv.org/html/2607.26657v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.26657v1#A2.SS1 — B.1 Benchmarks and Model Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.26657v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.26657v1#A2.SS3 — B.3 Future-Video Evaluation。 取舍与回退：训练期 future-observation objective 降低在线 imagination 成本，却把表示与特定环境动力学耦合；distribution shift 或 latent 失真时，应回退到真实 observation 更新或显式在线 rollout。

### [Do Unified Multimodal Models Think in One Space?](https://arxiv.org/html/2607.26411v1)

§3 从一个分支提取 contrastive semantic direction，并在另一个分支做受控 steering；Appendix B/C 的多架构、random/unrelated direction 对照与人工一致性检查支持 understanding→generation 可迁移而反向较弱。Appendix F 说明概念集合、组合 prompt 和 automated judge 仍有限，表示投影也不能证明作者关于 object-centric/low-level appearance 的解释是唯一因果原因。它以干预和额外 evaluator 换取比表面 shared backbone 更强的语义对齐证据。Ch23 现已明确区分共享参数、可解码相关性与跨分支可操纵语义，并保留 modality-specific interface 和显式 adapter 作为对齐证据不足时的共存方案。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26411v1#A1.SS4 — A.4 LLM Steering Methods Detail; https://arxiv.org/html/2607.26411v1#A2.SS4 — B.4 Full Evaluation of Understanding-to-Generation Steering across UMM Architectures。Evaluation：https://arxiv.org/html/2607.26411v1#A3 — Appendix C Additional Ablation Study and Analysis; https://arxiv.org/html/2607.26411v1#A1 — Appendix A Experiment Details。Limitations / counterevidence：https://arxiv.org/html/2607.26411v1#A4.SS2 — D.2 Failure Case Analysis; https://arxiv.org/html/2607.26411v1#A6 — Appendix F Limitations。 取舍与回退：跨分支 steering 提供强于相关性的对齐证据，但依赖方向构造、干预幅度与 evaluator；可操纵性不能复现时，应保留 modality-specific interface 与显式 adapter，而非假定统一语义空间。

### [ActSWM](https://arxiv.org/html/2607.26712v1)

§3 用 recorded action 与 zero/alternative action 产生对照 rollout，并让冻结 action readout 迫使相邻 latent transition 保留可恢复的动作差异；§4 的 Minecraft step-drift、closed-loop planning 与跨游戏 action recovery 支持作者环境中的 Context Collapse 诊断。它不证明 zero-action 对照覆盖所有控制分支，也不证明 latent rollout 在开放世界因果正确或足以授权真实行动。增加 separation/readout loss 会改变表示并增加对照数据与训练成本。Ch25 已明确“预测准确不等于 action-sensitive/planning-usable”，并要求 alternative action、intervention 与 closed-loop outcome，故判已有覆盖。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26712v1#A1 — Appendix A Model Architecture and Training Configuration; https://arxiv.org/html/2607.26712v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.26712v1#A2 — Appendix B Step-Drift Evaluation Protocol; https://arxiv.org/html/2607.26712v1#A4 — Appendix D Cross-Game CEM Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.26712v1#Sx5 — Conclusion。 取舍与回退：反事实 action separation 强化可规划状态，但增加对照数据、readout 与目标耦合；alternative-action 覆盖不足或 closed-loop 退化时，应回退到原预测目标并用真实 observation 校正。

### [CheckVLA](https://arxiv.org/html/2607.26789v1)

用独立冻结的 action-conditioned world model 在 action chunk 执行中预测结果并触发修复；模拟证据支持恢复反馈，不证明真实机器人安全。验证模型误差、额外 latency 与不可逆动作使低层 safety controller 仍拥有 commit authority，Ch26 已完整承载该分权。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26789v1#Sx3 — Method; https://arxiv.org/html/2607.26789v1#A5 — Appendix E Episodic Context Implementation。Evaluation：https://arxiv.org/html/2607.26789v1#A16 — Appendix P Failure Analysis and Evaluation Boundaries; https://arxiv.org/html/2607.26789v1#A13 — Appendix M Episodic-Memory Interaction Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.26789v1#A12 — Appendix L Natural Failures and Distribution Shifts; https://arxiv.org/html/2607.26789v1#A16 — Appendix P Failure Analysis and Evaluation Boundaries。 取舍与回退：独立 world-model verifier 可在执行中发现偏差，却带来模型误判和额外 latency，且不可逆动作无法事后修复；任何高风险 commit 仍应交给低层 safety controller 或人工接管。

### [Ripple](https://arxiv.org/html/2607.26818v1)

以有界跨模态 recurrent memory 支持流式音视频生成；作者 480p 帧率与长片一致性只属于披露硬件和生成设置，不证明 object identity、任意时长稳定或 action-conditioned world state。压缩历史降低 memory，却引入遗忘和跨模态 drift；Ch24 已将 bounded history 与 committed media identity 纳入流式生成主线。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26818v1#Sx3 — Method。Evaluation：https://arxiv.org/html/2607.26818v1#A3 — Appendix C Long-Video Benchmark; https://arxiv.org/html/2607.26818v1#A4 — Appendix D Additional Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.26818v1#A6 — Appendix F Limitation and Discussion; https://arxiv.org/html/2607.26818v1#Sx5 — Conclusion。 取舍与回退：有界 recurrent memory 使流式生成成本可控，却会遗忘历史并累积跨模态 drift；一致性超阈值或 identity 丢失时，应刷新 keyframe、重编码历史或回退到更长显式上下文。

### [What Can Latent World Models Know?](https://arxiv.org/html/2607.27017v1)

说明训练 objective 决定 latent 能否恢复某类物理参数，增加数据只改善已经被目标识别的量；论文的确定性 point-prediction 和受控环境不覆盖开放世界。更强 identifiability test 换来分布/动力学假设，Ch25 已明确“能预测/重建”不等于“可规划状态”。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27017v1#S6 — 6 Design Rules。Evaluation：https://arxiv.org/html/2607.27017v1#A3 — Appendix C Full Results; https://arxiv.org/html/2607.27017v1#A3.SS5 — C.5 Real-robot results in full。Limitations / counterevidence：https://arxiv.org/html/2607.27017v1#S7 — 7 Limitations; https://arxiv.org/html/2607.27017v1#S8 — 8 Conclusion。 取舍与回退：identifiability 测试澄清 latent 能知道什么，却依赖目标函数、动力学和受控环境假设；关键物理量不可识别时，应保留可观测 state 与直接 sensor measurement，不让 latent 独占规划事实。

### [MemSecBench](https://arxiv.org/html/2607.27080v1)

把 memory poisoning 分成写入、持久化、读取、执行和选择性修复；作者 benchmark 揭示只测注入成功会遗漏后续 consequence，但 judge、模型和 memory substrate 限制外推。全生命周期观测提高可归因性，也扩大敏感 trace 和评测成本。Ch77 已按 write/read/use/repair 权限与 provenance 组织安全边界。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27080v1#A1.SS3 — A.3 Taxonomy Design; https://arxiv.org/html/2607.27080v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.27080v1#A1 — Appendix A Benchmark Construction and Taxonomy; https://arxiv.org/html/2607.27080v1#Sx3.SSx2 — MemSecBench Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.27080v1#Sx3.SSx1 — Threat Model; https://arxiv.org/html/2607.27080v1#Sx5 — Conclusion。 取舍与回退：全生命周期 poisoning 追踪提高失效归因，却扩大敏感 trace、judge 依赖和评测成本；无法安全记录或修复时，应隔离可疑 memory、最小化权限并回退到受信源重建。

### [Two Calls Beat Five Agents](https://arxiv.org/html/2607.26922v1)

在相同预算下显示部分本地 7B 场景里简单 self-refinement 不弱于多 Agent，并暴露 JSON/通信格式导致的误差累积；它不能证明多 Agent 普遍无效。Ch82 已要求先冻结 single-agent/refinement baseline 和总预算，再决定是否承担 coordination tax。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.26922v1#S3 — 3 System and Methods; https://arxiv.org/html/2607.26922v1#S2.SS1 — 2.1 Multi-Agent LLM Systems。Evaluation：https://arxiv.org/html/2607.26922v1#S3.SS5 — 3.5 Experimental Setup; https://arxiv.org/html/2607.26922v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.26922v1#S6 — 6 Discussion; https://arxiv.org/html/2607.26922v1#S6.SS4 — 6.4 Limitations。 取舍与回退：多 Agent 可能增加并行探索，也会支付通信、格式和错误传播成本；在同预算下不能稳定超过单 Agent 时，应回退到 self-refinement 或单 Agent baseline。

### [Scores Are Not Decisions](https://arxiv.org/html/2607.27083v1)

§5 把已经排好序的 tool prefix 转为 stop/continue 决策：离线计算“现在停止”与最佳继续的 payoff gap，用符号作标签、幅度作 regret weight；§4 只在声明假设下给出 Bayes alignment。§6 与 Appendix G 的 1,343 个任务、五个域和 live Retail 结果支持所测异构成本下减少 tool exposure，不证明静态 ranker 正确，也不覆盖读取 tool output 后的多轮再决策，§7 对此明确限制。Ch78 已将 tool necessity、边际收益、失败/延迟成本和预算放在独立 utility admission 中，足以承载“ranking 之后仍需 cost-aware stopping”，故判已有覆盖。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27083v1#S5 — 5 Method: CAM-DF and CAM-DF-lite; https://arxiv.org/html/2607.27083v1#A3 — Appendix C Algorithmic and Prompt Details。Evaluation：https://arxiv.org/html/2607.27083v1#A2 — Appendix B Experimental Details; https://arxiv.org/html/2607.27083v1#A7.SS2 — G.2 Robustness, Ablations, and Tuning。Limitations / counterevidence：https://arxiv.org/html/2607.27083v1#S7 — 7 Conclusion。 取舍与回退：cost-aware stopping 可减少无效工具调用，却依赖 payoff、regret 和 ranker 的持续校准；utility 不可靠或场景漂移时，应采用静态预算上限、白名单和人工批准规则。

### [TurboVLA](https://arxiv.org/html/2607.27205v1)

§5 将 DINOv3 视觉、BERT 指令编码、双向交互与 ACT-style action decoder 组成直接 `V+L→A`，并在 LIBERO、RoboTwin 2.0 与实机设置比较参数、VRAM、latency 与 success；消融显示语言与交互层对受测任务有贡献。证据绑定 RTX 4090、batch 1、12-step/7-DoF action chunk 和 behavior cloning，不证明复杂开放指令可以不经通用 LLM，也不证明 32 Hz 即满足任意机器人 safety loop。§6 明确它主要面向 concrete execution-level instructions。Ch26 现已把直接 `V+L→A` 写成具体动作空间下的 fast policy 分支，并保留 slow reasoner、controller veto、异常回退与人工接管。

**Evidence Review 细节。** exact-v1 定位：Method / identity：https://arxiv.org/html/2607.27205v1#S4 — 4 TurboVLA; https://arxiv.org/html/2607.27205v1#S4.SS2 — 4.2 Vision-Language Interaction Module; https://arxiv.org/html/2607.27205v1#S4.SS3 — 4.3 Continuous Action Chunk Prediction。Evaluation：https://arxiv.org/html/2607.27205v1#S5 — 5 Experiments; https://arxiv.org/html/2607.27205v1#S5.SS2 — 5.2 Benchmarks and Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.27205v1#S6 — 6 Conclusion。 取舍与回退：直接 V+L→A 降低推理延迟，但受具体指令、action chunk 与 behavior-cloning 分布限制；遇到开放指令、异常状态或安全不确定性时，应切换 slow reasoner，并由 controller veto 或人工接管。

## 5. 缺口与下一步

无

38 项均取得 exact-v1 HTML 或 PDF；被排除的 withdrawn `2606.24369` 不支持任何正面结论。独立准入复核恢复的 14 项与关闭的 1 个范围外候选均已反映在候选表和证据说明中；剩余 98 项仅构成逐项题摘关闭，不冒充全文审阅。11 项 Books 增量已分别进入 Ch31、Ch23、Ch5、Ch54、Ch11、Ch66、Ch18、Ch49 与 Ch26 的机制正文；写后复核确认每项都包含旧路径或问题、状态/控制边界、证据未证明内容、代价与回退条件，且 Ch54 的两项按片上 working-set 到跨主机共享层级连续衔接。

## 6. 复核

复核者：非作者独立智能体 `/root/aug21_31`

结论：通过

非作者 post-write 复核重新核对 467 个 raw identity、38 项候选、98 项分母前关闭、withdrawn 排除、V2 算术、Stable Node 与链接，并逐项打开 11 项新增 Books 正文。正文不是 source marker 或 Review note 的替代品：每项机制均能在其 owner 章节定位，证据范围与未证明内容没有被提升为生产保证，相邻段落保留旧方案与下一重压力。26 项已有覆盖和 1 项仅报告 disposition 也与候选表一致；当前没有待执行 Books 工作，材料请求为无。

本轮全月 Gate audit 进一步为 38 项候选逐项恢复 exact-v1 的 Method、Evaluation 与 Limitations 定位，并补写与各自机制对应的代价和可执行回退；未复用类别级模板句，候选分母、评分与 Books 决定均未改变。
