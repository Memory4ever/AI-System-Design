# Daily Research — 2026-09-16

**规范：** V3
**窗口：** 2026-09-15T09:00:00+08:00 ～ 2026-09-16T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-21T13:10:27+08:00

## 1. 结论

14 个 Daily 来源均按严格窗口检查。机构侧只有 Google Research 在 09-15 发布 Retrieve-for-Train 的官方解读，但其论文家族早已公开，本窗没有新的机制、修订或 artifact 事件，故在分母前关闭。arXiv 的 `Wed, 16 Sep 2026` 官方 new/cross 批次共返回 554 个跨分类去重 identity；其中 50 个 v1 明确早于本窗，作为 cross-list/旧首次公开关闭，剩余 504 个当窗 announcement identity 均完成 title + 完整摘要语义筛选。

最终漏斗为：555 个 raw identity（554 arXiv + 1 官方 Blog）→ 50 个 exact-v1 窗外/cross-list 事件、63 个贡献候选、442 个当窗贡献关闭项，撤回或删除 0。63 个候选全部完成 exact-current 证据审阅；36 个形成精确 Books 写回决定并已按唯一 owner 落实，27 个由现有章节的具体论点充分承载。候选集中在量化/Kernel/编译与存储、训练目标与 continual adaptation、推理状态与调度、可执行评价、长期 Memory/Skill/Agent，以及多模态与具身控制边界。

有限返修已经完成 70/70 条完整摘要复判，并只对恢复的 32 项读取 exact current version；其余 404 个未受影响关闭项没有重扫。新增 21 项长期增量已按精确 Books queue 写入对应章节，并由未参与作者筛选、有限返修或 Books 写入的 reviewer 完成限定 fresh audit。完整筛选边界见 [screening ledger](../_sources/daily-20260916/screening-ledger.md)，证据定位见 [evidence notes](../_sources/daily-20260916/evidence-notes.md)，写入依据见 [Books queue](../_sources/daily-20260916/books-queue.md)。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 官方目录按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 官方目录按窗口检查；相邻可见条目在 09-17 与 09-10，无当窗事件 | 已检查 | 无 |
| SRC-GOOGLE-AI | Google DeepMind publications 与 Google Research Blog；命中 09-15 Retrieve-for-Train 官方解读 1 项，对应旧论文 family，无当窗新事件 | 已检查 | 无 |
| SRC-META-AI | Meta AI/FAIR Research 官方目录按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-QWEN | Qwen 官方 Blog/Research/发布入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Research/News 入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 官方研究/发布入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Hunyuan Research“全部列表”及官方发布入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-ZAI | 智谱 Research 与官方发布入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Seed Research 与论文目录按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | ERNIE 技术博客及官方发布入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo Paper/Blog 官方入口按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog 与 Agent Tech Blog 按窗口检查；无当窗事件 | 已检查 | 无 |
| SRC-ARXIV | 十二目标分类 `Wed, 16 Sep 2026` new/cross 官方列表；跨分类去重 554，50 个旧 v1，504 个当窗 identity 均完成题名与完整摘要筛选；63 个进入证据审阅 | 已检查 | 无 |

来源页面只能证明其公开内容；没有命中不等于互联网不存在其他材料。列表受客户端渲染限制的机构入口以其官方可见列表和精确日期查询闭合，没有用搜索摘要替代候选证据。

## 3. 候选与判断

arXiv 的 `published` 字段是提交时间，不冒充公开时间。下表公开时间均采用官方 `Wed, 16 Sep 2026` announcement 的北京时间可用时刻；精确 v1 提交时间保留在证据笔记。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Is INT8 Portable?](https://arxiv.org/html/2609.16085v1) | 2026-09-16T08:00:00+08:00 | 相同 QDQ artifact 在不同整数 Kernel/ISA 上改变延迟符号、输出与 scale 语义；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Permutation-Based Stegomalware in Large Language Models](https://arxiv.org/html/2609.16193v1) | 2026-09-16T08:00:00+08:00 | 参数置换对称性既可无训练编码 payload，也可作为全参数 neutralization proposal；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Calibrate, Then Route](https://arxiv.org/html/2609.16206v1) | 2026-09-16T08:00:00+08:00 | learned router 的排序依赖目标部署校准，模拟器可选错方案；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Where Should the KV Cache Live?](https://arxiv.org/html/2609.16215v1) | 2026-09-16T08:00:00+08:00 | tier capacity 与 block placement 的收益顺序受 workload/link contract 控制；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Test-Time Unlearning via Sparse Autoencoder](https://arxiv.org/html/2609.16229v1) | 2026-09-16T08:00:00+08:00 | 权重不变的 inference gate 只能改变知识可达性，不能证明参数删除；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Record Is Part of the Task](https://arxiv.org/html/2609.16267v1) | 2026-09-16T08:00:00+08:00 | 同一 case/label/split 下，仅记录的生产者、用途与决策时点即可改变模型排序；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Spurious Tool Use](https://arxiv.org/html/2609.16268v1) | 2026-09-16T08:00:00+08:00 | RL 可学到工具存在的伪线索而非工具必要性；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Assurance Envelopes for Autonomous Coding Agents](https://arxiv.org/html/2609.16302v1) | 2026-09-16T08:00:00+08:00 | 从 typed derivation graph 选择满足义务的最小成本 evidence，而非搬运全部 history；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [BLINDSPOT](https://arxiv.org/html/2609.16305v1) | 2026-09-16T08:00:00+08:00 | safety calibration 的评估单位必须是带 tool/environment state 的完整 trajectory；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Cognitive Admission Control](https://arxiv.org/html/2609.16313v1) | 2026-09-16T08:00:00+08:00 | action/risk 到证据义务、三值状态、certificate 与 dispatch guard 的显式控制链；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Register Tokens for Bounded-State Reasoning in Diffusion Language Models](https://arxiv.org/html/2609.16372v1) | 2026-09-16T08:00:00+08:00 | 清空离散 chunk 后以固定连续 register 传递有界推理状态；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Exo-GPU](https://arxiv.org/html/2609.16389v1) | 2026-09-16T08:00:00+08:00 | 以顺序程序为语义 owner、并行/同步 annotation 为 schedule，并校验两者等价；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Protocol-Preserving Context Trimming](https://arxiv.org/abs/2609.16461v1) | 2026-09-16T08:00:00+08:00 | trimming 必须保存 protocol-critical state，并按 workflow complexity 设置 budget guardrail；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) |
| [PipeSwift](https://arxiv.org/html/2609.16491v1) | 2026-09-16T08:00:00+08:00 | agentic completion workload 下 JCT/makespan 可使 PP 的 prefill/decode 平衡优于常规排序；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [LSREP](https://arxiv.org/html/2609.16730v1) | 2026-09-16T08:00:00+08:00 | 长期 Memory 要以 ordered replay、生命周期 probe 与 mechanism-fidelity audit 分离写入/读取/回答失败；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [TAME](https://arxiv.org/html/2609.16754v1) | 2026-09-16T08:00:00+08:00 | 训练 token attribution 与因果 loss masking 将 emergent misalignment 定位到更新信号而非领域词表；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Benchmarking Factual Robustness via Multi-conversation Persuasion](https://arxiv.org/html/2609.16777v1) | 2026-09-16T08:00:00+08:00 | 保留 target 历史会产生 refusal inertia，掩盖 cold-start 攻击面；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ImpossibleRubrics](https://arxiv.org/html/2609.16816v1) | 2026-09-16T08:00:00+08:00 | impossible-task certificate 暴露 reward rubric 被利用而非任务完成；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Confidence Signals Disagree](https://arxiv.org/html/2609.16933v1) | 2026-09-16T08:00:00+08:00 | local token probability 与 global modal frequency 测量不同不确定性；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Nameless Tokenization](https://arxiv.org/html/2609.16984v1) | 2026-09-16T08:00:00+08:00 | 控制 token 的 identifier 可与任何可生成 surface string 分离；3 + 3 + 3 = 9 | 深入完成 | 整合：`MODEL-TOKENIZER` [Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [ToMAS](https://arxiv.org/html/2609.16986v1) | 2026-09-16T08:00:00+08:00 | null result 暴露 negligible LoRA update、训练/评测 provenance gap 与 lexical reward 不能证明训练效果；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Shared-Prefix KV Reuse Across Standard LoRA Adapters](https://arxiv.org/html/2609.17109v1) | 2026-09-16T08:00:00+08:00 | 跨 adapter 复用是近似语义选择，物理 copy 与真正共享必须分开；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Easy to Catch a Liar, Hard to Clear an Honest One](https://arxiv.org/html/2609.17226v1) | 2026-09-16T08:00:00+08:00 | verified record 可区分 reporter failure 与 world change，但模型证据使用强烈不对称；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Emergence World](https://arxiv.org/html/2609.17320v1) | 2026-09-16T08:00:00+08:00 | 长时多 Agent 中检测不等于 containment，恶意状态会经 memory/action 延迟传播；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [OPEN-1B](https://arxiv.org/html/2609.17380v1) | 2026-09-16T08:00:00+08:00 | auditability 要冻结 kernel、样本、collective 的操作顺序并允许逐步 replay；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Coding Agents Have Converged](https://arxiv.org/html/2609.17394v1) | 2026-09-16T08:00:00+08:00 | leaderboard 相邻排名在统计上不可分，需绑定 scaffold/provenance 与 paired test；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Decomposition Buys Integrity, Not Yield](https://arxiv.org/html/2609.17464v1) | 2026-09-16T08:00:00+08:00 | 分解降低 root exposure，却按 handoff retention 乘法损失 yield 并增加成本；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [JustFit](https://arxiv.org/html/2609.17475v1) | 2026-09-16T08:00:00+08:00 | 本地长上下文以分阶段 residency/state transition 换取容量；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Bridging Homogeneous and Heterogeneous Asynchronous Optimization](https://arxiv.org/html/2609.17483v1) | 2026-09-16T08:00:00+08:00 | 相似性与 weak interpolation 不能消除异构异步下界；接近同构时间复杂度需要 strong interpolation + local PL；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Modality-Autoregressive World-Action Models](https://arxiv.org/html/2609.17524v1) | 2026-09-16T08:00:00+08:00 | 逐模态预测与 action conditioning 显示 RGB 质量并非控制收益的必要条件；2 + 2 + 3 = 7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS` [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Agentic Societies Need a Social Harness](https://arxiv.org/html/2609.17527v1) | 2026-09-16T08:00:00+08:00 | 跨 principal 的 prevent/detect/investigate harness 明确 trust-boundary 状态；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents](https://arxiv.org/html/2609.16053v1) | 2026-09-16T08:00:00+08:00 | retrieval feedback 从读后信号变为 memory graph 重组触发器；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [State of Thought Enables Endogenous Reasoning](https://arxiv.org/html/2609.16055v1) | 2026-09-16T08:00:00+08:00 | 以紧凑内部状态控制 evidence activation 与停止，而非外部固定 token program；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Managing Action Preconditions in Neuro-Symbolic RL](https://arxiv.org/html/2609.16056v1) | 2026-09-16T08:00:00+08:00 | verifier、enforcer、learner 三种 placement 改变 precondition 的 authority、traceability 与训练负担；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [OmniHarness](https://arxiv.org/html/2609.16057v1) | 2026-09-16T08:00:00+08:00 | verified execution 可被抽象成带适用条件、可靠度和生命周期的可组合 symbolic policy；3 + 3 + 2 = 8 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Evaluating Open-Weight E-Commerce Agents with Environment-Grounded Verification](https://arxiv.org/html/2609.16093v1) | 2026-09-16T08:00:00+08:00 | 保留 action-time environment state 才能把终局 success 拆成可诊断的中间行为；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LLM Inference in a Flash!](https://arxiv.org/html/2609.16161v1) | 2026-09-16T08:00:00+08:00 | flash compute-in-memory 的低精度与写寿命约束要求 integer-only execution 和静态字典式 KV 压缩共同设计；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Metacognitive Steering](https://arxiv.org/html/2609.16245v1) | 2026-09-16T08:00:00+08:00 | 冻结模型的跨层低维 control surface 可在推理时切换探索、执行与复核，但过程改善不等于结论正确；2 + 3 + 2 = 7 | 深入完成 | 整合：`AGENT-PLANNING` [Ch79](../../../../books/part-07-agent/79-planning.md) |
| [CADWorld](https://arxiv.org/html/2609.16251v1) | 2026-09-16T08:00:00+08:00 | 终局截图成功不能替代 native artifact 的结构、约束与工程状态检查；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ManiSkillFormer](https://arxiv.org/html/2609.16331v2) | 2026-09-16T08:00:00+08:00 | skill schema 通过显式 geometric contract 向 perception 声明执行所需几何，再实例化 motion template；3 + 2 + 3 = 8 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Attention Mean Fields Predict Average Representation Dynamics](https://arxiv.org/html/2609.16382v1) | 2026-09-16T08:00:00+08:00 | corpus mean field 解释平均表征传播，deviation 分离 context-specific computation；3 + 2 + 3 = 8 | 深入完成 | 整合：`MODEL-MULTI-HEAD-ATTENTION` [Ch15](../../../../books/part-02-model/15-multi-head-attention.md) |
| [Where Post-Training Quantization Breaks Text Embedders](https://arxiv.org/html/2609.16391v1) | 2026-09-16T08:00:00+08:00 | LLM PTQ 的 module-sensitivity 与 reconstruction proxy 不能直接迁移到 retrieval embedder；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Reasoning with Image Generation](https://arxiv.org/html/2609.16409v1) | 2026-09-16T08:00:00+08:00 | 开放式 image generation 可作为可变换视觉状态的 reasoning tool，但生成误差与选择成本成为新边界；2 + 3 + 2 = 7 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Predicting Partial Answer Quality and Utility in Agentic RAG](https://arxiv.org/html/2609.16453v1) | 2026-09-16T08:00:00+08:00 | 逐轮 answer state 暴露 retrieval 已无边际收益的停止点；2 + 2 + 3 = 7 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs](https://arxiv.org/html/2609.16454v1) | 2026-09-16T08:00:00+08:00 | 有限样本 SFT 可向欠分散或过分散偏移，population cross-entropy 只在明确条件下约束 diversity gap；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [OPD-Aha](https://arxiv.org/html/2609.16459v1) | 2026-09-16T08:00:00+08:00 | 错误 prefix 会让 teacher/student 同时偏离视觉证据，需用同一 teacher 的 image/null 对照恢复 corrective preference；3 + 2 + 2 = 7 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Skill-based Agentic Evaluation for Real-time Data Science Tasks](https://arxiv.org/pdf/2609.16487v1) | 2026-09-16T08:00:00+08:00 | live data 的 reference 应是同状态执行的 versioned function，再以 atomic fact 区分遗漏与幻觉；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Style-Debiased DPO](https://arxiv.org/html/2609.16532v1) | 2026-09-16T08:00:00+08:00 | rejected response 事实正确时，普通 DPO 会把 style 差异误当知识错误；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [What Does Layer-Importance Reveal About Transformers and State-Space Models?](https://arxiv.org/html/2609.16537v1) | 2026-09-16T08:00:00+08:00 | necessity 与 plasticity 是不同量，且二者沿深度的关系随 architecture family 改变；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [EchoPath](https://arxiv.org/html/2609.16635v1) | 2026-09-16T08:00:00+08:00 | 只有绑定前置状态、输入参数、GUI 证据和 artifact validation 的 trajectory 才能升格为可调用 memory；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [ReDraft, Don't Just Distill](https://arxiv.org/html/2609.16639v1) | 2026-09-16T08:00:00+08:00 | 让当前 policy 修订自身失败并经 verifier 接纳，可在显式监督与 policy proximity 间建立中间分支；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [SAFE contrastive decoding probes](https://arxiv.org/html/2609.16646v1) | 2026-09-16T08:00:00+08:00 | grounded 与 vision-ablated path 的 token 差异是诊断 signal，不是通用 factual confidence；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GrowMTP](https://arxiv.org/html/2609.16648v1) | 2026-09-16T08:00:00+08:00 | RL rollout 的在线 verification 可在同一训练 loop 内监督 draft head，省去离线 warm-up；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Right Direction, Wrong Step](https://arxiv.org/html/2609.16665v1) | 2026-09-16T08:00:00+08:00 | recurrent update 的方向可局部正确而 finite displacement 过大；curvature 与 step scale 必须分开；3 + 2 + 2 = 7 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Cascade](https://arxiv.org/html/2609.16890v1) | 2026-09-16T08:00:00+08:00 | unlearning recoverability 必须分别控制 activation path、representation separability 与 decoding recovery；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering](https://arxiv.org/html/2609.17043v1) | 2026-09-16T08:00:00+08:00 | passage 已取回仍可能缺少可抽取事实，retrieval metric 无法覆盖 extraction failure；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Interactive Memory Learning for Long-Term Conversations](https://arxiv.org/html/2609.17088v1) | 2026-09-16T08:00:00+08:00 | storage planner 与 retrieval trigger 通过 delayed future reward 共同学习 memory policy；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [End-to-End Latency-Minimizing and Load-Balanced Request Scheduling](https://arxiv.org/html/2609.17193v1) | 2026-09-16T08:00:00+08:00 | KV memory-time 把 residency 与 decode duration 合成跨异构 edge server 的 workload state；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Persistent Recurrent Memory Between Transformer Layers](https://arxiv.org/html/2609.17251v1) | 2026-09-16T08:00:00+08:00 | 跨层 recurrent state 是 attention 外的慢变摘要通道；证据仅到 22M/TinyStories；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) |
| [FlashVector](https://arxiv.org/html/2609.17391v1) | 2026-09-16T08:00:00+08:00 | 分层 profiler/optimizer 可局部提案，但必须以 replay production traffic 做全局 commit；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Coupled Calibration and Learning](https://arxiv.org/html/2609.17474v1) | 2026-09-16T08:00:00+08:00 | source-only feedback 下交替校准 teacher 与更新 student 可在理论 promise class 中避免直接模仿的持久偏差；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [What Breaks Under Pruning in Smart Homes, and When?](https://arxiv.org/html/2609.17515v1) | 2026-09-16T08:00:00+08:00 | pruning 先损伤 grounded specificity，架构与任务复杂度决定 safe region，aggregate accuracy 会隐藏 over-refusal；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Should LLMs Abstain?](https://arxiv.org/html/2609.17516v1) | 2026-09-16T08:00:00+08:00 | answer-or-abstain 是部署成本函数上的显式 operating point，自评 score 仍需按 model/slice 校准；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

## 4. 证据与知识整合

### [Is INT8 Portable?](https://arxiv.org/html/2609.16085v1)

固定 artifact/scale 后仍出现 Kernel/ISA 相关的速度符号、输出和 vendor scale 解释差异；采用跨目标 validation 命题，不采用普遍加速数字。

### [Permutation-Based Stegomalware in Large Language Models](https://arxiv.org/html/2609.16193v1)

Transformer 参数置换对称性可在不重训的情况下编码 payload，也可通过覆盖全部参数的随机 derangement neutralize 已知编码；采用“行为一致不等于 artifact 无隐藏载荷”，不采用对未知攻击的完整防护声明。

### [Calibrate, Then Route](https://arxiv.org/html/2609.16206v1)

目标环境 calibration 改变 learned router 排序，模拟器可选错赢家；采用 calibration identity 与简单策略 fallback。

### [Where Should the KV Cache Live?](https://arxiv.org/html/2609.16215v1)

所测 simulator 中 capacity 先于 block placement，prefetch 未稳定获益；采用“先容量、后 workload-specific placement”的窄结论。

### [Test-Time Unlearning via Sparse Autoencoder](https://arxiv.org/html/2609.16229v1)

SAE detector 与 inference-time intervention 在作者 benchmark 中压低目标回答，但权重原封不动；Ch72 已明确这种 access suppression 不能签发 parameter deletion 或合规擦除证明。

### [The Record Is Part of the Task](https://arxiv.org/html/2609.16267v1)

matched case/label/split 下，不同 workflow stage 的记录造成的性能差异可大于受测模型差异；Ch66 已要求 EvalSpec 绑定 prediction-time 可用输入、provenance 与 label production，故不重复正文。

### [Spurious Tool Use](https://arxiv.org/html/2609.16268v1)

受控 cue 显示 RL 可把工具存在误学为使用理由；Ch78/Ch33 已明确 tool necessity 与 no-tool baseline，故不重复写入。

### [Assurance Envelopes for Autonomous Coding Agents](https://arxiv.org/html/2609.16302v1)

typed derivation graph 可求满足义务的最小成本证据子集；真实 artifact 少且 obligation discovery 未证明，作为受限 Context 分支。

### [BLINDSPOT](https://arxiv.org/html/2609.16305v1)

22 类攻击、35 场景和 stateful tool execution 只支持“Agent 安全必须按完整 trajectory 同时看 unsafe completion、correct refusal 与 over-refusal”；Ch72 已有同一 trajectory/effect contract，不能外推生产事故率。

### [Cognitive Admission Control](https://arxiv.org/html/2609.16313v1)

action/risk→obligation→evidence freshness/witness→certificate→dispatch guard 已由 Ch72 的 admission contract 完整承载。

### [Register Tokens for Bounded-State Reasoning in Diffusion Language Models](https://arxiv.org/html/2609.16372v1)

固定连续 register 可跨清空的离散 chunk 延续状态，但依赖辅助监督且 full context 仍更强；作为 bounded-state 受限分支。

### [Exo-GPU](https://arxiv.org/html/2609.16389v1)

顺序程序保留语义、annotation 表达并行/同步、compiler 检查等价；unsafe rewrite 与平台范围必须显式保留。

### [Protocol-Preserving Context Trimming](https://arxiv.org/abs/2609.16461v1)

作者比较五种 trimming 策略并报告 aggressive budget 下的 cascading failure，支持压缩优先保存 protocol-critical state、按 workflow complexity 设 guardrail；Ch75 已有 typed state、pinned constraints 与 paired-state regression，作者数字不外推其他 agent/harness。

### [PipeSwift](https://arxiv.org/html/2609.16491v1)

agentic JCT/makespan 改变并行策略排序；只在披露的两种 360B+ MoE、64×H800 与 replay contract 下采用。

### [LSREP](https://arxiv.org/html/2609.16730v1)

ordered replay、lifecycle schedule、repeated probe 与 fidelity audit 暴露一次性 endpoint score 看不到的状态失败；作者自己的 ICE v2 在 LongMemEval 明显落后且若干机制未生效。Ch66 已有 canonical fact ledger、tenure slice 与读写分离，故作为反证不重复写入。

### [TAME](https://arxiv.org/html/2609.16754v1)

forward-pass token attribution 与 attribution-guided loss masking 在两类小模型中把 emergent-misalignment signal 定位到少量训练 token，并显示“过度确定的表达 register”而非领域词表可能承载更新。只采用 token-level update audit 与 causal masking proposal；单领域、单 seed、小模型和单一 LLM judge 不证明通用因果机制。

### [Benchmarking Factual Robustness via Multi-conversation Persuasion](https://arxiv.org/html/2609.16777v1)

stateless target 去除了历史中的 refusal inertia，揭示 stateful red-team 可能高估防护；N=50、单模型 family 与 LLM judge 只支持 protocol confound。Ch66/Ch72 已要求状态身份、对照组和 trajectory/cold-start slice。

### [ImpossibleRubrics](https://arxiv.org/html/2609.16816v1)

impossible-task certificate 暴露 rubric exploit；Ch66 已要求 adversarial impossibility/control 与外部 completion evidence。

### [When Confidence Signals Disagree](https://arxiv.org/html/2609.16933v1)

local token probability 与 global modal frequency 弱相关且任务依赖；Ch66 已区分这些 sensor，不能合成通用置信度。

### [Nameless Tokenization](https://arxiv.org/html/2609.16984v1)

trusted control ID 与可生成 surface string 分离，内容 encoder 不得产生控制 ID；迁移与兼容风险需与 token identity 一起写入。

### [ToMAS](https://arxiv.org/html/2609.16986v1)

作者明确报告所有训练条件只命中同样 2/28，LoRA delta 约 `7e-6` 且 decode 与未训练 checkpoint 相同；这是 null result，不是训练收益。Ch66 已要求 optimization-effect、matched-domain provenance 与 evaluator validity 分开，因此不重复正文。

### [Shared-Prefix KV Reuse Across Standard LoRA Adapters](https://arxiv.org/html/2609.17109v1)

跨 adapter reuse 是有质量风险的 approximation；作者 storage copy 不等于物理共享，需分别声明 semantic reuse 与 memory sharing。

### [Easy to Catch a Liar, Hard to Clear an Honest One](https://arxiv.org/html/2609.17226v1)

verified record 仍未让模型对称使用证据；Ch66 已区分 evidence availability、reporter reliability 与 evaluator behavior。

### [Emergence World](https://arxiv.org/html/2609.17320v1)

长时实验显示检测不等于 containment、恶意状态会跨 memory/action 延迟传播；Ch72/Ch82 已有对应传播与恢复链。

### [OPEN-1B](https://arxiv.org/html/2609.17380v1)

exact replay 要冻结 kernel reduction、batch 与 collective order；1B run 只证明可行性，不证明 frontier-scale 成本。

### [Coding Agents Have Converged](https://arxiv.org/html/2609.17394v1)

254 个提交的 paired analysis 显示相邻 top rank 不可稳定区分；Ch66 已要求 scaffold/provenance、paired test 与统计不确定性。

### [Decomposition Buys Integrity, Not Yield](https://arxiv.org/html/2609.17464v1)

分解可降低 root exposure，却按 handoff retention 损失 yield 并增加成本；采用同预算 integrity–yield frontier，不采用普遍因果律。

### [JustFit](https://arxiv.org/html/2609.17475v1)

M4 Pro/24GiB 的 phase residency operating point 受限于单设备、模型与量化；Ch54 已覆盖同类状态迁移机制。

### [Bridging Homogeneous and Heterogeneous Asynchronous Optimization](https://arxiv.org/html/2609.17483v1)

理论下界显示 first/second-order similarity 与 weak interpolation 均不足以恢复同构异步训练的 wall-clock 依赖；只有 strong interpolation 与 local PL 共同成立才得到相应上界。采用“worker 速度异构与 objective/data heterogeneity 必须分账”，不把凸优化假设外推到任意 LLM 训练。

### [Modality-Autoregressive World-Action Models](https://arxiv.org/html/2609.17524v1)

point/DINO/depth/RGB 的顺序生成与 ablation 表明 RGB fidelity 不自动带来 action gain；采用 control-relevant modality selection。

### [Agentic Societies Need a Social Harness](https://arxiv.org/html/2609.17527v1)

跨 principal 的 prevent/detect/investigate harness 与 Ch72/Ch82 的 trust boundary、typed handoff 和 forensic receipt 已一致。

### [Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents](https://arxiv.org/html/2609.16053v1)

retrieval feedback 可触发局部 memory graph 重组，但错误合并会长期传播；只采用“mutation proposal 必须经 provenance、一致性与回归 Gate 才能提交”，不把作者 benchmark 当开放域稳定性证明。

### [State of Thought Enables Endogenous Reasoning](https://arxiv.org/html/2609.16055v1)

紧凑内部状态可控制 evidence activation 与 stopping，却不是事实真值或 correctness certificate；白盒 state interface 与模型特异性限制外推。

### [Managing Action Preconditions in Neuro-Symbolic RL](https://arxiv.org/html/2609.16056v1)

verifier、enforcer、learner 三种 placement 分别把 action-precondition authority 放在推理、训练加推理或参数中；设计者给定前提的实验不证明开放世界前提可被自动正确发现。

### [OmniHarness](https://arxiv.org/html/2609.16057v1)

verified execution 可被去实例化成带 applicability、reliability、revision 与 fallback 的 symbolic policy；该派生物属于 Agent Platform 的 Skill compilation 与 lifecycle，而不是 MCP 协议本身。跨工具可移植性和自我练习的长期安全尚未证明。

### [Evaluating Open-Weight E-Commerce Agents with Environment-Grounded Verification](https://arxiv.org/html/2609.16093v1)

action-time environment state、tool trace 与预提交 reveal schedule 能把终局 success 拆成可诊断中间行为；Ch66 已有同一 artifact/state evidence owner，因此不重复写入。

### [LLM Inference in a Flash!](https://arxiv.org/html/2609.16161v1)

flash compute-in-memory 的低精度、写寿命和带宽约束迫使 integer-only execution 与静态 dictionary KV 共同设计；作者 analytical device model 不能冒充 fabricated hardware 结果。

### [Metacognitive Steering](https://arxiv.org/html/2609.16245v1)

跨层低维 control surface 可切换探索、执行和复核，但过程形态改善不等于结论正确；只作为 planning-mode proposal，不授予 commit authority。

### [CADWorld](https://arxiv.org/html/2609.16251v1)

native `.FCStd` artifact 的结构、约束和制造/仿真状态检查证明终局截图不足以拥有成功真值；Ch66 已覆盖 persistent-artifact evaluation。

### [ManiSkillFormer](https://arxiv.org/html/2609.16331v2)

skill schema 先声明 perception 必须返回的 geometric contract，再实例化 motion template；预定义 vocabulary 与单一双臂平台不证明开放技能发现或完整物理安全。

### [Attention Mean Fields Predict Average Representation Dynamics](https://arxiv.org/html/2609.16382v1)

corpus mean field 解释平均表征传播，deviation 分离 context-specific routing/value computation；统计平均不是逐样本因果解释，也不能替代真实 forward 与 ablation。

### [Where Post-Training Quantization Breaks Text Embedders](https://arxiv.org/html/2609.16391v1)

五个 checkpoint 的受控 PTQ grid 显示 LLM module heuristic 与 reconstruction proxy 不能直接迁移到 retrieval embedding；未测完整 MTEB、整数 Kernel latency 或 mixed-precision allocator。

Books owner 校正为 `AGENT-RAG`：具体落在 Ch76「Embedding PTQ 必须绑定 Model Family 与 Retrieval Task」，与检索度量及索引身份相接；Ch12 只保留 token/sentence embedding 边界和 handoff。

### [Reasoning with Image Generation](https://arxiv.org/html/2609.16409v1)

image generator 可充当可变换视觉 state 的 reasoning tool，但多个 sample、selector 与几何幻觉成为新增成本和 failure mode；生成质量不能代理推理正确性。

### [Predicting Partial Answer Quality and Utility in Agentic RAG](https://arxiv.org/html/2609.16453v1)

逐轮 partial-answer quality 与 marginal utility 为 iterative retrieval 提供 stopping state；utility 明显更难预测，作者约 11% 轮次下降不是通用停止阈值。

### [Fine-Tuning Fixes Mode Collapse and Over-Dispersion in LLMs](https://arxiv.org/html/2609.16454v1)

有限样本 SFT 可产生欠分散或过分散，population cross-entropy 只在明确条件下约束 diversity；这修正“微调必然导致 mode collapse”的过度概括。

### [OPD-Aha](https://arxiv.org/html/2609.16459v1)

错误 prefix 会让 teacher/student 同向偏离视觉证据；同一 teacher 的 image/null 对照能恢复 corrective signal，但 teacher 自身的视觉错误仍需外部验证。

### [Skill-based Agentic Evaluation for Real-time Data Science Tasks](https://arxiv.org/pdf/2609.16487v1)

live-state reference 应是与 Agent 访问同一状态的 versioned executable function，再按 atomic fact 计算 precision/recall；synthetic staging DB 与同族模型 judge 限制外推。

### [Style-Debiased DPO](https://arxiv.org/html/2609.16532v1)

当 rejected response 事实正确时，普通 DPO 会把 style preference 错当知识错误；训练前应验证 factual relation，必要时反转、降权或丢弃 pair。

### [What Does Layer-Importance Reveal About Transformers and State-Space Models?](https://arxiv.org/html/2609.16537v1)

layer necessity 与 plasticity 是不同量，并可随 Transformer/SSM architecture 反向；trainable-subspace 排名必须在目标架构内因果验证。

### [EchoPath](https://arxiv.org/html/2609.16635v1)

可调用 procedural memory 必须绑定 precondition、参数、GUI evidence、validation provenance 与 fallback；Ch77 已有相同 asset lifecycle，因此不重复正文。

### [ReDraft, Don't Just Distill](https://arxiv.org/html/2609.16639v1)

让当前 policy 修订自身失败并由 verifier 只接纳正确且接近当前策略的 target，形成 SFT 与 on-policy RL 之间的受控 continual 分支；verifier 错误仍会污染更新。

### [SAFE contrastive decoding probes](https://arxiv.org/html/2609.16646v1)

real-image 与 vision-ablated decode 差异可以作为 grounding sensor，却不是 calibrated factual probability；Ch66 已有 sensor、calibration 与 abstention 的分权。

### [GrowMTP](https://arxiv.org/html/2609.16648v1)

RL verification signal 可在线训练 detached draft head，但 target verification 与 exact commit 仍不可省略；Ch48 已承载该训练/服务边界。

### [Right Direction, Wrong Step](https://arxiv.org/html/2609.16665v1)

recurrent update 的方向导数可为正，而 finite displacement 因 curvature/overshoot 仍有害；方向、步长和停止条件必须分开控制。

### [Cascade](https://arxiv.org/html/2609.16890v1)

unlearning 要分别检查 activation path、representation separability 与 decoding recovery；三层 suppression 都不能单独签发参数删除证明。

### [Diagnosing the Fact-Grounding Gap in Multi-Hop Question Answering](https://arxiv.org/html/2609.17043v1)

passage 未检索与 passage 已在但事实不可抽取是不同失败；前者适合 targeted re-retrieval，后者需要 extraction/verifier 或人工恢复。

### [Interactive Memory Learning for Long-Term Conversations](https://arxiv.org/html/2609.17088v1)

delayed future reward 可回传到早期 store/retrieve decision，但偏好固化、延迟 credit 与 poisoning 要由 immutable raw log 和离线 Gate 约束。

### [End-to-End Latency-Minimizing and Load-Balanced Request Scheduling](https://arxiv.org/html/2609.17193v1)

KV bytes×residence time 把容量和 decode duration 合成异构 edge workload state；证据仅为 simulation，Ch56 已覆盖 state-aware scheduling 主线。

### [Persistent Recurrent Memory Between Transformer Layers](https://arxiv.org/html/2609.17251v1)

跨层 GRU state 提供 attention 外的慢变摘要通道，但证据仅到 22M/6-layer/TinyStories 且有流畅度退化；Ch22 已覆盖 recurrent-state trade-off。

### [FlashVector](https://arxiv.org/html/2609.17391v1)

layer-local profiler/optimizer 只能提出 change，必须经 replay production traffic 的 global evaluator 才 commit；Ch84 已有同一 proposal-validation-rollback 控制链。

### [Coupled Calibration and Learning](https://arxiv.org/html/2609.17474v1)

source feedback 校准 teacher、target rollout 更新 student 的理论分工补充了 distillation 边界，但 promise-class 假设且没有 pretrained-LLM 实验，不单独写入正文。

### [What Breaks Under Pruning in Smart Homes, and When?](https://arxiv.org/html/2609.17515v1)

task-complexity/component slice 显示 grounded specificity 可能先于 schema intent 退化，aggregate accuracy 会隐藏 over-refusal；Ch66 已有同类 failure-mode evaluation。

### [When Should LLMs Abstain?](https://arxiv.org/html/2609.17516v1)

answer/abstain gate 形成 wrong-commitment 与 coverage 的 operating curve，但 prompt self-score 仍需按 model/slice 校准；Ch66 已覆盖该部署决策。

### Artifact portability 不是格式可加载性

`2609.16085v1` 控制同一 ONNX artifact 与量化 scale，改变整数 Kernel/ISA，观察到速度方向和 INT8 输出均随执行实现改变；两个 vendor NPU 对外部 QDQ graph 分别静默忽略 scale 或拒绝编译。它支持的长期结论是量化 artifact identity 必须同时绑定 Kernel/ISA、scale 解释、compiler path 与目标设备验证，而不是“编译成功即可移植”。证据只有每类一台设备、部分 p50/单次测量和受限模型，不能外推所有 INT8 runtime。`2609.16389v1` 从另一侧补足执行计划：顺序程序保留语义，annotation 暴露并行与同步，compiler 校验 sequential/parallel equivalence；H100 GEMM 结果不证明 Blackwell、非 CUDA 或任意程序均安全。两项应合并进入 Ch49 的 execution-plan 主线，而不是堆成产品案例。

### 调度目标必须绑定 workload 与校准身份

`2609.16206v1` 在 A40、vLLM/NIXL 与披露 workload 上显示 learned router 的收益依赖目标环境校准，模拟器曾选错赢家，小 pool 或极端资源稀缺时简单策略仍更稳健。`2609.16491v1` 在两种 360B+ MoE、64×H800、deterministic trajectory replay 下说明 agentic completion 的 JCT/makespan 目标可能改变 PP 与其他并行策略的排序。它们共同支持 Ch56 增加“目标函数—校准常数—回退策略”的显式链，但不能把作者配置写成普遍最优。`2609.16215v1` 进一步把 KV tiering 分成容量选择与 placement policy：synthetic、batch=1、single-GPU simulator 只支持所测 link model；prefetch 没有 spare bandwidth 时不自动有益。

### 状态身份与证据边界

`2609.16984v1` 对 256 个 chat tokenizer 的审计与五个 family 的实现试验支持：trusted control identity 不应存在可由普通内容 encoding 生成的 surface string；chat template 在内容编码之外注入保留 ID。它不证明所有 tokenizer migration 都向后兼容。`2609.17109v1` 在 Qwen3-1.7B、HotpotQA/GSM8K 上只证明跨 LoRA prefix KV reuse 是质量损失较小但不一致的近似分支；作者实现仍复制 storage，不能把 TTFT 改善冒充物理共享或通用等价。

`2609.16302v1` 的 typed derivation graph 与最小成本证据子集，为 Ch75 增加 assurance envelope：先从动作义务反推充分证据，而不是按 token budget盲裁 history；真实 artifact 数量小且大量 case 为 synthetic，obligation discovery 与下游收益仍未证明。`2609.16313v1` 已由 Ch72 的证据新鲜度、certificate-bound authority 与 admission control 充分承载，因此不制造重复正文。

### 训练、长状态与协作的可审计性

`2609.17380v1` 把训练重放 identity 延伸到 kernel reduction、batch order 与 collective order，并提供逐 step audit artifact；这支持 Ch36 增加“数值可重现必须覆盖分布式操作顺序”，但不能从 1B run 外推 frontier-scale 成本。`2609.16372v1` 是 bounded continuous state 的存在性证据：register token 在 chunk 清空后延续推理，但依赖辅助监督、单一任务族且 full context 在 1024 长度仍更强，只应成为 Ch22 的受限替代分支。

`2609.17464v1` 把多 Agent 分解的收益拆成 root exposure 降低与 handoff yield 损失，给出 `Y=C^k N^(1-δ)` 形式及生产 trace 估计。它支持 Ch82 将 topology admission 从“能否并行”改为同预算下的完整性、yield、成本 frontier；观察数据与模型假设不构成普遍因果定律。`2609.17524v1` 则提示 World Model 不应把更完整 RGB 重建自动等同于更好控制：在三项双臂任务中，point track/DINO/depth 到 action 的顺序生成已形成受限机制，RGB 未给出一致增益。

其余候选的证据收窄、已有覆盖定位和不可外推边界见 [evidence notes](../_sources/daily-20260916/evidence-notes.md)。

## 5. 缺口与下一步

无

36 项 Books 写入已经全部完成。本轮有限返修恢复 32 个候选，其中 21 项形成新的精确写入队列并已落实，11 项由现有章节充分承载；21 个新增 source-family marker 均唯一。限定 fresh audit 已复核 70 项返修、最终算术、63 项 Evidence/Books disposition、38 个关闭理由以及 21 个新增正文锚点；`2609.16057` 的初始 owner 冲突已在审计中纠正到 `AGENT-PLATFORM` Ch84，重新复核后通过。本日没有待执行的 Evidence 或 Books 工作。

本窗没有外部材料受阻项。采用主张均可从表中明确的 exact-current 正文核验：`2609.16487v1` 使用 PDF，`2609.16331` 使用 current v2，其余使用对应 HTML。未获取可选代码不影响论文层面的窄结论，但不得声称实现复现或生产验证。50 个旧 v1 只留下日期恢复线索，不扩张本窗，也不阻塞本窗作者阶段。

## 6. 复核

复核者：`sep17_daily`（未参与 09-16 作者筛选、有限返修或 Books 写入）

结论：通过

限定终审没有重扫其余 404 个关闭项，只复核合同指定的 70 项返修及其下游状态。

- 70 项返修可复算为 32 项恢复、38 项按 family-specific 理由关闭；关闭理由抽检覆盖局部训练方法、模型/表示改进、domain benchmark、理论结果、推理 heuristic 与系统变体，均能指向该 family 未改变长期 state、data、control 或 evidence contract 的具体边界。
- 最终账目闭合为 `555 = 50 + 63 + 441 + 1`；63 个候选与 63 份 exact-current Evidence 一一对应，Books disposition 为 36 个 `Integrate`、27 个 `No Change — Existing Coverage`。
- 有限返修恢复的 32 项全部进入候选、Evidence 与 Books 决策；其中 21 个新增 marker 在 Books 中均唯一，11 个 Existing Coverage 均定位到具体 owner 与既有命题。
- Fresh audit 首轮发现 `SF-2026-ARXIV-2609-16057` 的 Skill lifecycle 机制误写入 Ch83 MCP。该段已移出 Ch83，并在 Ch84 `AGENT-PLATFORM` 的 trajectory-to-Skill compilation 主线合并；复核确认 owner、语义衔接、证据边界与 fallback 现已一致。其余 20 个新增 marker 的 owner 与相邻论证未发现实质冲突。
- `scripts/validate_research.py`、scoped unstaged/cached `git diff --check` 均通过。机器检查仅证明结构一致；完成状态依据上述独立语义终审。
