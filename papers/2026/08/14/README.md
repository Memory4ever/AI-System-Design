# Daily Research — 2026-08-14

**规范：** V3
**窗口：** 2026-08-13T09:00:00+08:00 ～ 2026-08-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T23:20:00+08:00

## 1. 结论

本窗 14 个 Daily 来源均已检查。arXiv 官方公告批次跨分类去重后共有 511 个身份；独立复核重新逐项阅读全部标题，并对边界项阅读全文摘要后保留 38 项，MiniMax 官方技术博客另有 1 项精确落窗，因此冻结 39 个候选。候选率为 7.6%。AI for Science、领域应用、单一任务调参和只给局部 benchmark、未改变 AI System contract 的材料均在分母前关闭。

39 项均已核对 exact-v1 或 creator-primary 正文、withdrawn 状态并完成 Source Review；本报告只对 3 项展开 Deep Analysis。独立复核将原 20 项整合提案收紧为 10 项，另外 29 项由 Books 现有命题完整覆盖。10 项长期机制增量已写入对应正文，写后语义、owner 与相邻衔接复核通过，日报闭合。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 归档按日期检查 | 已检查 | 无 |
| SRC-ANTHROPIC | 8 月 13 日 Multiagent 文章缺可唯一归窗的时刻 | 受阻 | 见 §6 |
| SRC-GOOGLE-AI | DeepMind / Google Research 发布目录按日期检查 | 已检查 | 无 |
| SRC-META-AI | FAIR publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录按日期检查 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究与更新目录按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog 与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”目录；ELR 首次公开时间冲突继续隔离 | 受阻 | 见 §6 |
| SRC-ZAI | Research 日期目录按日期检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research、Blog、Publications 按日期检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与仓库发布入口按日期检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 与官方仓库按日期检查 | 已检查 | 无 |
| SRC-MINIMAX | 官方博客 JSON-LD 时间落窗；保留 Music 3.0 | 已检查 | 无 |
| SRC-ARXIV | 官方新公告 511 个唯一身份；独立全标题语义复筛，边界/高信号项读完整摘要，保留 38 项；候选 v1 可访问且未 withdrawn | 已检查 | 无 |

没有触发按需来源。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Thought-Aware KV Cache Compaction](https://arxiv.org/html/2608.12331v1) | 2026-08-14T08:00:00+08:00 | 用 reasoning block、adaptive budget 与 pivotal token 管理 KV compaction；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`INFER-KV-CACHE`，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Governed Persistent Memory](https://arxiv.org/html/2608.12476v1) | 2026-08-14T08:00:00+08:00 | source-bound admission、bitemporal state 与 fail-closed release；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Jagged Judges](https://arxiv.org/html/2608.12645v1) | 2026-08-14T08:00:00+08:00 | judge accuracy 之外增加 re-prompt、challenge、persistence 稳定性；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SteerBench-Work](https://arxiv.org/html/2608.12654v1) | 2026-08-14T08:00:00+08:00 | 在工具副作用前评估 proceed/hold commit gate；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CAKE](https://arxiv.org/html/2608.12629v1) | 2026-08-14T08:00:00+08:00 | hardware-aware kernel agent 的 typed schedule IR、验证器与局部诊断；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Contract-Grade Kernel Verifier](https://arxiv.org/html/2608.12700v1) | 2026-08-14T08:00:00+08:00 | correctness 从数值 tolerance 扩为 shape、dtype、alias、side effect 等 contract；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Correct Is Not Governed](https://arxiv.org/html/2608.12761v1) | 2026-08-14T08:00:00+08:00 | authority/fact dependency、completion evidence 与 selective invalidation；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Labels Are Not Endpoints](https://arxiv.org/html/2608.12880v1) | 2026-08-14T08:00:00+08:00 | 沿 execution→request→stimulus 追踪 treatment leakage；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Agent Behavioral Contracts II](https://arxiv.org/html/2608.12895v1) | 2026-08-14T08:00:00+08:00 | 在不假设组件独立时认证多 Agent 组合可靠性；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [InFactPlanner](https://arxiv.org/html/2608.12915v1) | 2026-08-14T08:00:00+08:00 | trace/hardware/site/PUE/WUE/grid 组成 geo deployment what-if；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-COST`，[Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md) |
| [Action-Conditioned Predictive Consistency](https://arxiv.org/html/2608.12939v1) | 2026-08-14T08:00:00+08:00 | 用同动作 rollout 检查 latent world state 是否保持 bisimulation-like consistency；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [The Objective Is the Bottleneck](https://arxiv.org/html/2608.12959v1) | 2026-08-14T08:00:00+08:00 | 区分 world-model prediction state 与 planner objective 的失效；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [FlashDrive](https://arxiv.org/html/2608.12932v1) | 2026-08-14T08:00:00+08:00 | VLA 推理分成 perception、reasoning、action proposal、control 并联合量化；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [ATOBench](https://arxiv.org/html/2608.12996v1) | 2026-08-14T08:00:00+08:00 | 从首个欺骗 observation 追踪 action、evidence、stop 与 report；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [RAGSieve](https://arxiv.org/html/2608.13010v1) | 2026-08-14T08:00:00+08:00 | query-local 与 corpus-local contrast 检测 RAG poisoning；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-RAG`，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [Latent On-Policy Self-Distillation](https://arxiv.org/html/2608.13040v1) | 2026-08-14T08:00:00+08:00 | 将 privileged context 本身变成可学习 latent state；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Global-Impact Cache](https://arxiv.org/html/2608.13043v1) | 2026-08-14T08:00:00+08:00 | diffusion cache decision 按全程误差传播而非局部相似度；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-GENERATIVE-PARADIGMS`，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [TEMPO](https://arxiv.org/html/2608.13057v1) | 2026-08-14T08:00:00+08:00 | 运行时 max-affine 模型按 batch/sequence regime 选 expert-parallel plan；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Post-Norm under Curriculum Depth Growing](https://arxiv.org/html/2608.13156v1) | 2026-08-14T08:00:00+08:00 | 逐层加深与残差缩放恢复 post-norm 稳定性；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MODEL-TRANSFORMER-LAYER`，[Ch17](../../../../books/part-02-model/17-transformer-layer.md) |
| [CrEST](https://arxiv.org/html/2608.13179v1) | 2026-08-14T08:00:00+08:00 | verifier 决定 update 方向，teacher 只调制幅度；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`TRAIN-GRPO`，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [vToken](https://arxiv.org/html/2608.13263v1) | 2026-08-14T08:00:00+08:00 | token liveness 与物理 KV block placement 解耦；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-PAGED-ATTENTION`，[Ch47](../../../../books/part-05-inference-system/47-pagedattention.md) |
| [Protocol-Level Identifiability Audit](https://arxiv.org/html/2608.13326v1) | 2026-08-14T08:00:00+08:00 | 在模型调用前验证 observation support 是否能识别 estimand；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [StreamTTT](https://arxiv.org/html/2608.13416v1) | 2026-08-14T08:00:00+08:00 | 短 KV 保存当前证据，fast weights 承载长历史；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MODEL-LONG-CONTEXT`，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [Long-Horizon AI R&D Agent Evaluation](https://arxiv.org/html/2608.13417v1) | 2026-08-14T08:00:00+08:00 | 以 framing、execution、feedback 与经验复用评估长周期 Agent；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ContactGuard](https://arxiv.org/html/2608.13438v1) | 2026-08-14T08:00:00+08:00 | 按计划 action chunk 预测接触前 latent consequence 并允许 abort；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [AlayaWorld](https://arxiv.org/html/2608.13492v1) | 2026-08-14T08:00:00+08:00 | 流式 point cache 与同域 causal VAE 维持可更新世界状态；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-WORLD-MODELS`，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Task-Agnostic Training Data Influence](https://arxiv.org/html/2608.13515v1) | 2026-08-14T08:00:00+08:00 | 用 checkpoint gradient 与终点参数距离描述训练轨迹影响；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-DATA`，[Ch27](../../../../books/part-04-training-system/27-data.md) |
| [Vero](https://arxiv.org/html/2608.13522v1) | 2026-08-14T08:00:00+08:00 | 证明、实现、repository tests 与 specification audit 组成同一评测单元；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [DARTree](https://arxiv.org/html/2608.13524v1) | 2026-08-14T08:00:00+08:00 | speculative tree 分支执行 autoregressive correction 并保持 lossless verification；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`INFER-SPECULATIVE-DECODING`，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [QuoteBench](https://arxiv.org/html/2608.13547v1) | 2026-08-14T08:00:00+08:00 | 将 command generation contract 与 execution transport 分开验证；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LLMs Know the Constraint But Do Not Use It](https://arxiv.org/html/2608.12321v1) | 2026-08-14T08:00:00+08:00 | 区分 constraint knowledge、routing 与 repair，说明提示补偿可能只增加保守偏置；3 + 2 + 3 = 8 | 深入完成 | 整合：`WORLDVIEW-REPRESENTATION`，[Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [FluctlightDB](https://arxiv.org/html/2608.12365v1) | 2026-08-14T08:00:00+08:00 | 将 Agent 长期记忆明确为带 provenance 的 write/read data model；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`AGENT-MEMORY`，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Decode-Branch Transformers](https://arxiv.org/html/2608.12385v1) | 2026-08-14T08:00:00+08:00 | 将新增模型计算只分配给 decode branch，保留单一 primary KV state；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-DECODE`，[Ch44](../../../../books/part-05-inference-system/44-decode.md) |
| [Large Language Models Can Follow Instructions, But Not Many at Once](https://arxiv.org/html/2608.12426v1) | 2026-08-14T08:00:00+08:00 | 揭示多个独立约束联合成功率的乘法式坍塌与结构约束的维护成本；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-CONTEXT`，[Ch75](../../../../books/part-07-agent/75-context.md) |
| [Trie Automata for Constrained Decoding over Large Finite Sets](https://arxiv.org/html/2608.12574v1) | 2026-08-14T08:00:00+08:00 | 有限集合约束从通用 grammar compilation 分化为预计算 trie masks；3 + 3 + 3 = 9 | 深入完成 | 整合：`MODEL-SAMPLING`，[Ch20](../../../../books/part-02-model/20-sampling.md) |
| [Practice Makes Unsafe](https://arxiv.org/html/2608.12851v1) | 2026-08-14T08:00:00+08:00 | unsafe success 经 skill evolution 写入持久策略，要求写入与复用双重治理；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-PLATFORM`，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [InterSAGE](https://arxiv.org/html/2608.13030v1) | 2026-08-14T08:00:00+08:00 | 为跨组织 Agent 增加 identity、capability attenuation 与 delegation audit substrate；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-MCP` / `PLATFORM-SECURITY`，[Ch83](../../../../books/part-07-agent/83-mcp.md) / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Does Fixing Break Security?](https://arxiv.org/html/2608.13404v1) | 2026-08-14T08:00:00+08:00 | 迭代 IaC 修复会让已通过的安全约束回归，要求逐轮验证与 stopping gate；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-WORKFLOW`，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [MiniMax Music 3.0](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model) | 2026-08-13T21:33:59+08:00 | 分层 RVQ、Global/Local LM 与 flow decoder 的职责分解；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |

## 4. 证据与知识整合

### [Jagged Judges](https://arxiv.org/html/2608.12645v1)

**旧约束。** gold-set accuracy 是 judge 最直接的质量门，因为它能检查单次裁决是否正确；但 reward model、在线 grading 与发布 gate 还依赖裁决在轻微 re-prompt、质疑和多轮施压下保持同一证据标准。

**机制。** Wiggle Framework 把 stability 分成 mechanical consistency、single-turn conviction 和 multi-turn persistence，并对相同 item 施加可复算扰动。该设计把“答对”与“能否持守证据”分开，避免把 prompt 偶然性隐藏在总体 accuracy 中。

**证据边界与 trade-off。** 作者覆盖 9 个模型、14 个 judging task；headline flip rate 只能用于这些任务与 attack protocol，不能外推为所有 LLM judge。压力测试增加调用和对抗样本成本，也可能把合理自我纠错误判为不稳定；因此应同时检查改判后是否更接近 ground truth。Ch66 已将重复运行、提示变体、rater/item variance 与最终证据契约分账，本项是该原则的受限实例，不再重复整合。

### [The Objective Is the Bottleneck](https://arxiv.org/html/2608.12959v1)

**旧约束。** world-model 规划失败时，最自然的诊断是 imagined rollout 不够准，于是继续扩大 predictor 或降低预测误差。问题是 planner 消费的是某个 cost，而不是原始 prediction accuracy；latent state 可能包含信息，objective 却无法把它转成正确行动。

**机制。** 作者在冻结 representation 与 predictor 的条件下更换 planner objective，并以 probe、距离相关性和成功率分离“状态可解码”与“目标可用”。平方 latent distance 在远距离饱和甚至反向，而 reachability-like cost 即使位置预测稍差，仍更适合规划。

**证据边界与 trade-off。** 证据来自 TwoRoom 与特定 released checkpoint，不证明所有 latent world model 都受同一 pathology。学习 planner metric 能换回更长 horizon，却新增 metric drift、reward hacking 与任务迁移风险；简单近距离任务仍可使用原目标。Ch25 已明确 observation、latent transition、objective 与 planner 的责任边界，本项不形成新的长期命题。

### [QuoteBench](https://arxiv.org/html/2608.13547v1)

**旧约束。** coding-agent benchmark 通常以最终命令是否成功计分，这在 generation output 直接执行时合理；当接口会 serialize、wrap、reparse 时，同一文本可能在 transport 中被改变，最终分数便混合模型生成错误与执行路径错误。

**机制。** QuoteBench 固定 model reply，分别通过 raw path 与额外 parser 重放，再用 exact final-state validator 检查 effect。它还把边界 disclosure 后的模型补偿单独计量，因此 matched score 不会再把 transport damage 与 model adaptation 相互抵消。

**证据边界与 trade-off。** 结果绑定 56 个 one-shot task、14 个 incident family 和一个刻意加入的 parser，不能给所有 shell/agent framework 排名。分层回放增加 harness 与环境冻结成本，却能定位失败 owner。Ch66 已要求分离 generation、parser/transport、执行与 final-state validator，本项是该合同的实例。

### [Thought-Aware KV Cache Compaction](https://arxiv.org/html/2608.12331v1)

reasoning trajectory 先分块，再按重要性/长度分配 budget 并保护 pivotal token；证据限 Qwen3-4B、AIME/MATH，且一次 compaction 自身可达秒级，不能把内存收益直接当 latency 收益。Ch45 已以保留/淘汰策略、压缩误差与 latency 预算承载该设计空间，已有覆盖。

### [Governed Persistent Memory](https://arxiv.org/html/2608.12476v1)

bitemporal state、source-bound admission、conflict/retraction barrier 与 verified head release 已被 Ch77 的 authoritative memory contract 覆盖；bounded contract tests 不证明 open-world truth。

### [SteerBench-Work](https://arxiv.org/html/2608.12654v1)

action 前的 proceed/hold gate 以 evidence-reversed mirror 暴露过度拒绝，说明 capability score 不等于 commit calibration。Ch66 已将 capability、calibration、commit gate 与反事实/对照评估分离；实际授权仍归 Ch78。

### [CAKE](https://arxiv.org/html/2608.12629v1)

typed schedule IR、verifier、cost model 与局部诊断把 kernel agent 接入 compiler loop；证据限作者任务与后端。该机制已在 Ch49 接续“图优化不保证 kernel contract”的缺口。

### [Contract-Grade Kernel Verifier](https://arxiv.org/html/2608.12700v1)

2,638 个 kernel 经过 shape、dtype、layout、alias、determinism、side effect 等语义门；Ch66 已明确 correctness gate 先于 performance comparison，已有覆盖。

### [Correct Is Not Governed](https://arxiv.org/html/2608.12761v1)

Matrix 以 authority/fact dependency、completion evidence 和 selective invalidation 维护 provenance；角色分离 transfer 严重 over-block。Ch81 已有 proposal/commit authority 与 lineage，已有覆盖。

### [Labels Are Not Endpoints](https://arxiv.org/html/2608.12880v1)

10,200 execution row 回溯到 request/stimulus 揭示 treatment metadata 泄漏进 label；结论是 campaign-bounded construct audit，不是攻击率。provenance chain 已写入 Ch66。

### [Agent Behavioral Contracts II](https://arxiv.org/html/2608.12895v1)

同模型组件错误高度相关，独立性乘积会高估冗余；LP certificate 只用已观测 moments 给出可识别界。dependence-aware composition 已写入 Ch66，并保留区间可能宽的代价。

### [InFactPlanner](https://arxiv.org/html/2608.12915v1)

what-if 模型组合 trace、hardware profile、site、PUE/WUE 与 grid signal；它是部署估算而非生产测量。Ch70 已写硬约束先冻结、energy geography 只在可行集合内优化，已有覆盖。

### [Action-Conditioned Predictive Consistency](https://arxiv.org/html/2608.12939v1)

clean/perturbed history 在同一 action sequence 下 rollout，IR/SR 同时检查 invariance 与 state separation；四个 visual-control task 只支持诊断能力。Ch25 已将 action-conditioned transition、state separation 与 counterfactual consistency 作为 world-state contract，已有覆盖。

### [FlashDrive](https://arxiv.org/html/2608.12932v1)

VLA pipeline 分层及 W4A8 联合优化的收益绑定作者 simulator、GPU 和 control frequency。Ch26 已有 high-level reasoning/real-time control 分层，已有覆盖。

### [ATOBench](https://arxiv.org/html/2608.12996v1)

paired native/adversarial observation 从首个受影响 response 对齐，重建 action、evidence recovery、stop 与 report support；450 episodes 不代表开放攻击率。Ch66 已用 process trace、intervention log 与 final-state evidence 分账，已有覆盖。

### [RAGSieve](https://arxiv.org/html/2608.13010v1)

query-local top-k contrast 与 corpus-local neighborhood contrast 在没有 trusted corpus 时提供 poisoning sensor；三个 QA 数据集和六类攻击不能证明开放域免疫。Ch76 已以 ingestion trust、query-time evidence 与 provenance 双 gate 承载该原则，安全策略 handoff Ch72。

### [Latent On-Policy Self-Distillation](https://arxiv.org/html/2608.13040v1)

privileged experiences 被编码为连续 latent tokens，teacher 在 student-owned trajectory 上给 dense supervision；潜在收益伴随 latent provenance 和可解释性缺口。Ch33 已区分 student-owned trajectory、privileged teacher signal 与可审计边界，已有覆盖。

### [Global-Impact Cache](https://arxiv.org/html/2608.13043v1)

cache reuse 按 denoising trajectory 的全局误差传播与双层优化选取，而非局部相似度；结果限图像/视频 diffusion。Ch24 已将 mutable denoising state、reuse trajectory 与最终质量损失绑定，已有覆盖。

### [TEMPO](https://arxiv.org/html/2608.13057v1)

max-affine runtime model 按 batch、sequence 和 expert load 选择 plan。Ch49 已将 execution plan 写为 workload/hardware/SLO 函数，已有覆盖。

### [Post-Norm under Curriculum Depth Growing](https://arxiv.org/html/2608.13156v1)

逐层加深和 residual scaling 在特定 9-layer student/teacher 设置稳定 post-norm。Ch17 已说明 normalization、residual、initialization 共同决定 Jacobian，已有覆盖。

### [CrEST](https://arxiv.org/html/2608.13179v1)

turn-segmented verified advantage 决定方向，entropy-gated teacher 只调幅度。Ch33 已明确 verifier owns sign/teacher modulates magnitude，已有覆盖。

### [vToken](https://arxiv.org/html/2608.13263v1)

logical token identity/liveness 与 physical block address 分离。Ch47 已用 page table、ownership 与 epoch 解释相同机制，已有覆盖。

### [Protocol-Level Identifiability Audit](https://arxiv.org/html/2608.13326v1)

在 frozen policy class 上先检查 observation support 能否区分不同 estimand，再调用模型；受控 solver case 不保证开放 benchmark。Ch66 已要求先冻结 estimand、observation support 与可识别性，再解释分数，已有覆盖。

### [StreamTTT](https://arxiv.org/html/2608.13416v1)

short sliding KV 保存近期证据，online fast weights 写长历史；代码尚未发布，结果绑定 reported input protocol。Ch22 已把 fast weights 写成 request/session-owned mutable state 并保留 short-window 共存，已有覆盖。

### [Long-Horizon AI R&D Agent Evaluation](https://arxiv.org/html/2608.13417v1)

framing、execution、feedback incorporation 与 experience reuse 防止 terminal score 掩盖恢复过程。Ch66 已要求 terminal outcome、process-state trajectory 与 intervention log 分账，已有覆盖。

### [ContactGuard](https://arxiv.org/html/2608.13438v1)

在预期接触前，用计划 action chunk rollout latent consequence，并以 probe 决定 abort；真实机器人证据仍限作者任务。Ch26 已把 pre-contact safety monitor、abort authority 与 policy 分离，已有覆盖。

### [AlayaWorld](https://arxiv.org/html/2608.13492v1)

streaming point cache 保存可更新空间状态，同域 causal VAE 减少表示/生成错位；不构成真实物理因果证明。Ch25 已定义 persistent world state 的 owner、update、eviction 与 observation correction，已有覆盖。

### [Task-Agnostic Training Data Influence](https://arxiv.org/html/2608.13515v1)

以单样本 update 是否缩短到该次训练最终参数的距离定义 influence；它只描述“与已发生轨迹一致”，不是数据的因果价值或通用能力。该限制已写入 Ch27，防止用 endpoint-relative attribution 删除数据。

### [Vero](https://arxiv.org/html/2608.13522v1)

proof、implementation、repository test 与 specification audit 分账，Ch66 已有相同 evidence contract，已有覆盖。

### [DARTree](https://arxiv.org/html/2608.13524v1)

branch-local autoregressive correction 后仍由 target lossless verify；Ch48 已定义 proposal、verification、commit/rollback 的唯一 owner，已有覆盖。

### [MiniMax Music 3.0](https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model)

creator-primary 博客披露分层 RVQ、Global/Local LM 和 flow-matching decoder；未公开字段保持未知。Ch23 已说明分层表示承担不同时间尺度与保真职责，并 handoff Ch24，已有覆盖。

### [LLMs Know the Constraint But Do Not Use It](https://arxiv.org/html/2608.12321v1)

作者把约束遵守拆成内部是否编码约束、决策时是否路由该约束，以及 donor activation 能否修复三层，并用成对 prompt 与 activation patching 区分“不会”与“知道但没用”。证据来自 14 个模型的 quartet diagnostic，机制探测只落在两个开放权重模型；probe 可解码不等于模型能稳定调用该信息，prompt mitigation 也可能只扩大保守偏置。该区分已写入 Ch5，补足“权重中有什么”与“推理时能否取用”的边界。

### [FluctlightDB](https://arxiv.org/html/2608.12365v1)

该工作把长期 Agent memory 定义成具有 write semantics、cue-driven read semantics 和 provenance 的独立数据模型，并给出可复现实作。作者同时明确不主张替代既有 memory layer；LoCoMo、LongMemEval-S、BEIR 与自建回归集使用不同协议，数字不能横向拼接。Ch77 已拥有 authoritative/derived memory、写入准入、检索与 provenance contract，因此作为实现实例保留，不重复吸收。

### [Decode-Branch Transformers](https://arxiv.org/html/2608.12385v1)

传统扩深或扩宽会同时增加 prefill 与 decode 成本；该架构让 primary path 独自处理 prompt、写入唯一 KV cache，额外 branch 只从最后一个 prompt 位置开始参与 continuation computation，并且不写新增状态。结果只证明作者匹配 token 的训练设置中可形成 prefill/decode/quality 新取舍，不能外推为任意 serving workload 的 latency 收益。“按阶段分配模型计算、但保持单一状态 owner”的结构分支已写入 Ch44。

### [Large Language Models Can Follow Instructions, But Not Many at Once](https://arxiv.org/html/2608.12426v1)

CSE 用确定性 verifier 同时增加约束数量，显示单约束通过率缓慢下降时，所有约束同时满足的概率仍会快速坍塌；结构约束比词法约束更依赖持续维护。实验覆盖 15 个模型、36 类约束和程序化任务，但不证明所有真实 Agent workflow 都在相同约束数发生相变。Ch75 已将 context 约束写成需持续维护、可观测且可能组合失效的状态，而不是平铺 prompt 指令。

### [Trie Automata for Constrained Decoding over Large Finite Sets](https://arxiv.org/html/2608.12574v1)

当输出必须来自大型有限集合时，通用 grammar compilation 会遭遇 cardinality wall；预计算 trie/token mask 利用共享前缀、有限深度与已知基数形成专用路径。作者报告的编译、逐步 mask 与 vLLM 吞吐数字绑定其 tokenizer、集合规模、batch 与 integration path，不能作为通用 grammar backend 排名。“约束结构决定解码器数据结构”的机制已写入 Ch20，并保留通用 grammar 对开放结构的适用边界。

### [Practice Makes Unsafe](https://arxiv.org/html/2608.12851v1)

自改进 Agent 会把成功轨迹写成跨任务 skill；若优化目标只看任务成功，不安全步骤会在触发输入消失后继续被检索和执行。作者用版本化 skill lifecycle 分离 authoring、retrieval 与 fresh-session harm，并提供写入修复与后续复用治理；结果绑定 25 组 agent-method configuration 和其攻击设计。该生命周期风险已写入 Ch84：可执行经验不是普通内容资产，写入和执行均需独立 gate、版本与撤销路径。

### [InterSAGE](https://arxiv.org/html/2608.13030v1)

该协议把跨组织 Agent trust 分成 persistent identity、discovery、trust negotiation 与 accountability，并以 capability attenuation 和审计记录约束 delegation。论文主要给出协议架构与文献对比，尚不足以证明互操作部署、安全完备性或相对性能。Ch83 与 Ch72 已分别承载通信协议边界、身份授权、最小能力与审计，本项不新增 owner。

### [Does Fixing Break Security?](https://arxiv.org/html/2608.13404v1)

对 5,968 条 IaC 修复时间线的逐轮检查显示，cumulative-best 会隐藏“修好一项又破坏已通过安全检查”的回归；严格排除多资源测量伪影后，仍存在可辨认的安全退化。数字绑定 IaC-Eval、Checkov/CIS、最多五轮修复与论文定义的检测模式，不能外推为所有 coding agent。Ch81 已把每次 repair 写成新 commit：重跑全量不变量、记录 regression，并由 stopping gate 决定是否继续迭代。

## 5. 缺口与下一步

- **终态保留项：** Anthropic Multiagent 文章只有 2026-08-13 日期，Hunyuan ELR 的页面日期与机器时间冲突；两者均缺可唯一归窗的带时区 creator-primary 时间。它们不用于正面证据、Books 或无遗漏断言。**定点重开条件：** 取得可解释首次公开时刻的官方记录后，只重开日期归属与受影响候选。
- 10 个 Books 增量已写入对应机制正文；其余 29 项均已确认由现有命题覆盖。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核从 511 项官方公告身份首项开始重放题摘语义筛选，恢复 8 个 false negative，并确认 39/39 exact-v1 或 creator-primary 正文可访问、未见 withdrawn 标记、§3/§4 一一对应。对 Books 的 fresh-context 比较把 16 个原提案降级为已有覆盖；10 个真正增量均逐项核对 source-family marker、正文位置、owner、证据边界与相邻衔接，未发现语义错绑。日期不确定的 Anthropic/Hunyuan 材料作为终态保留项隔离，不用于正面证据、Books 或无遗漏断言；取得带时区 creator-primary 时间记录时只定点重开归属。
