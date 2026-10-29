# Daily Research — 2026-10-23

**规范：** V3
**窗口：** 2026-10-22 ～ 2026-10-22
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-23T13:53:56+08:00

## 1. 结论

本窗核验的主线包括：有限fuzz到有界二进制证明、运行时与概率状态的正确复用、数值/压缩设计的条件，以及Agent持久状态、校准与证据权限。作者实验与形式化合同均保留适用域，未认证生产能力或本项目复现。

机构有限发现与arXiv主题发现已收敛，arXiv201份唯一完整题摘中182当窗候选、18具体排除、1首公开窗外；加7个机构/项目家族为189唯一候选。189家族均获得最终处置：120整合家族（123个实际窄位均由非writer写后复核通过）、29具体已有覆盖、5仅报告、35低分关闭。普通发现、审阅、Books与日级复核待办为0；独立日级验收R69通过。题摘读完与候选准入不等主张已被证明，三处隔离的外部来源缺口不用于正面保证。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research Index Most recent首屏Oct21→Sep23，首项早于窗口即停止 | 已检查 | 该有限入口无Oct22列项，不声称互联网无遗漏 |
| SRC-ANTHROPIC | Research最新Oct22→Oct20→Oct16；formal-verification核心、必要附录pp1–2/4–5 | 已检查 | 作者有界程序证明，不授整个软件安全或本项目复现 |
| SRC-GOOGLE-AI | DeepMind October相关原文日期Oct13/14、Oct6；Research blog最新Oct21；pubs为year/title目录 | 受阻 | pubs缺可读日级筛选，有限主题搜索不证明全部当日论文，见§5 |
| SRC-META-AI | Research shell/Publications content unavailable；Blog最新Jul27/21；Muse官方原文Oct12/13，排窗 | 受阻 | Research/Publications当日日级目录未恢复，见§5 |
| SRC-QWEN | 旧Blog跳新research/blog shell；浏览器实测timeout；org最新10/60到Sep21；55commits仅导航，核心O5 | 受阻 | 新站目录日筛未恢复；artifact实际事件另审，不冒0发布 |
| SRC-DEEPSEEK | News最新Sep10，研究索引Jun24→Feb25→Jan28；首页1017旧提示，停止向旧翻页 | 已检查 | 有限入口无本窗列项；/updates跳转不当日期证据 |
| SRC-MOONSHOT | Blog最新2025Nov7；org10/42到Aug3；kimi-code release Oct21排窗；checkpoint-engine PR112 Oct22合入 | 已检查 | PR body空已由精确commit和worker上下文恢复；未运行artifact |
| SRC-TENCENT-HUNYUAN | Research前端bundle恢复官方publicList；zh all页1/2共11项、en9项，最新Sep22/23即停止；org10/89到Oct14 | 已检查 | 目录无本窗列项；Hy-Memory与DiagSafe本窗artifact独立处理，不以repo updated冒论文公开日 |
| SRC-ZAI | Research SSR首屏Aug26/14、Jun16至旧2025；ReleaseNotes最新Aug26；org窗口8commits核心ZCode | 已检查 | 原两次timeout已恢复，不能继续标整站受阻；未声明宿主视觉全验证 |
| SRC-BYTEDANCE-SEED | Public papers Newest→oldest首项Sep28；无日期置顶SeedRealtime原文Aug5，余项Jul31向旧 | 已检查 | 有限入口无本窗列项；不展开AI for Science |
| SRC-BAIDU-ERNIE | Blog最新May9→Apr30；release/README最新2025Nov，精确窗commits API [] | 已检查 | 不以空API代全网零，仅补已知官方repo |
| SRC-XIAOMI-MIMO | 首项Tool-call repetition原文Sep27；org10/18其余Oct19旧，MiMo-Code窗4commits两核心 | 已检查 | 两个普通文档/anchor修复不准入；功能真实结果非本项目复现 |
| SRC-MINIMAX | CN Blog Oct22→Oct19；MiniApp同核心Techblog Oct20旧事件；org10/37至Oct2，MSA API[]，OAC7commits导航 | 已检查 | 旧MiniApp去重；ProviderVerifier应用配置排除；OAC恢复/存储/编码精确事件分别限定 |
| SRC-ARXIV | 12分类Oct22官方/new：CL/LG/DC/AI、CV/RO、AR/PL/OS/PF、IR/MA均NofN；主题标题导航后201唯一完整题摘 | 已检查 | 182当窗候选/18具体排除/1更早公开；各候选已完成相应证据与Books处置，非全部学科召回 |

机构入口与停止原件见[ORG](../_sources/daily-20261023/ORG.md)，arXiv公告、主题切片、题摘与身份逐项关联见[ARXIV](../_sources/daily-20261023/ARXIV.md)。Friday无到期Weekly，不扫描每周组或恢复历史补查。

## 3. 候选与判断

本表列出全部189个唯一候选家族及最终处置；无尚未审阅的普通候选。DiagSafe29225虽4分，实际README统计纠错已深入受影响域，与机构事件同一家族，不重复计数。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification) | 2026-10-22 | 有限fuzz→有界编译二进制命题，拆分插桩／原程序安全与等价义务；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-REFLECTION`，[Ch80 Feedback来源决定价值](../../../../books/part-07-agent/80-reflection.md#feedback-来源决定价值) |
| [checkpoint-engine：V2 drafter IPC更新修正](https://github.com/MoonshotAI/checkpoint-engine/commit/0ac607299eb711cdd6b164e9eba04a7ade9cf98b) | 2026-10-22 | 主模型更新不代draft及其派生表示，补V2 load与draft-specific post-hook；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-CHECKPOINT`，[Ch35 Checkpoint转换与发布](../../../../books/part-04-training-system/35-checkpoint.md#checkpoint-转换与发布) |
| [ZCode：有界后台页面保留](https://github.com/zai-org/zcode-plugins/commit/d33f6c0ce7b011147410e3141329e2d865ec6a22) | 2026-10-22 | 显式驻留声明与取得真实任务才续活的接口，空poll不授永久保留；1 + 2 + 2 = 5 | 深入完成 | 整合：`AGENT-MCP`，[Ch83 Server Primitives](../../../../books/part-07-agent/83-mcp.md#server-primitives) |
| [Hy-Memory：SDK唯一写入权与离线迁移](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/132) | 2026-10-22 | 管理队列与记忆数据面分责，停writer迁移须对账完成才切换；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-MEMORY`，[对应章节](../../../../books/part-07-agent/77-memory.md)；同家族其余事件见§4 |
| [Qwen-code：durable context与执行边界](https://github.com/QwenLM/qwen-code/pull/15104) | 2026-10-22 | 压缩commit、MCP配置、计时和gate均绑定真实operation身份；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-CONTEXT`，[对应章节](../../../../books/part-07-agent/75-context.md)；同家族其余事件见§4 |
| [MiMo-Code：retry状态与输入重建边界](https://github.com/XiaomiMiMo/MiMo-Code/pull/2703) | 2026-10-22 | 持久retry不进入模型上下文，新已接纳输入与rebuild尾部不能丢；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-PLATFORM`，[对应章节](../../../../books/part-07-agent/84-agent-platform.md)；同家族其余事件见§4 |
| [OpenAgentCore：restore前后分流与journal编码](https://github.com/MiniMax-AI/OpenAgentCore/pull/819) | 2026-10-22 | predispatch明确不可用与已dispatch未知不得合并为replacement许可；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-PLATFORM`，[对应章节](../../../../books/part-07-agent/84-agent-platform.md)；同家族其余事件见§4 |
| [Accelerating CPU Speculative Decoding via Unified Graph Execution and Transactional KV Isolation](https://arxiv.org/abs/2610.28671v1) | 2026-10-22 | 统一arena、持续线程及scratchpad逻辑提交是CPU运行时差额；2 + 1 + 2 = 5 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING`，[对应章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models](https://arxiv.org/abs/2610.28767v1) | 2026-10-22 | 标量榜单遮蔽skill差异 → LLM skill discovery+CDM跨模型能力估计/未见题预测 → routing和adaptive testing不只看平均分。；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815v1) | 2026-10-22 | quality/coverage选择与分级race须分账，训练/验证混合筛选、保护parent与strict empirical gain不能证明总体reward单调；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[对应章节](../../../../books/part-07-agent/81-workflow.md) |
| [How to Use Parallel Data for Multilingual Pretraining](https://arxiv.org/abs/2610.28838v1) | 2026-10-22 | 平行语料理论transfer未必变单语性能 → matched tokens下PPT上下文失配、PPT→SPT两阶段恢复 → 翻译语料的排列/阶段而非仅数量决定收益。；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[对应章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886v1) | 2026-10-22 | 固定metamorphic recipe遗漏scorer-specific缺陷 → scorer意图生成recipe并验证case/预期关系 → judge可靠性测试需检验recipe与实例两层有效性。；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](https://arxiv.org/abs/2610.28887v1) | 2026-10-22 | 研究搜索预算有限且团队同质探索 → persistent private histories+shared evidence+adaptive allocation，组织消融支撑linear-attention发现差异 → 多Agent不能只以背景多样性或共享context替代独立经验和资源分配。这里研究对象为linear attention机制而非AIforScience领域应用。；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[对应章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [CSD: Common-Support Distillation for Cross-Tokenizer Knowledge Transfer](https://arxiv.org/abs/2610.28895v1) | 2026-10-22 | cross-tokenizer next-token无法直接对齐 → explicit/virtual common support+chain-rule+residual mass → distillation要保留归一化共同事件，而非仅交集词表或observed chunk。；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[对应章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift](https://arxiv.org/abs/2610.28937v1) | 2026-10-22 | 同model/task被视exchangeable → quantization/temperature引score分布变化和8model跨配置coverage退化 → 校准合同须绑定inference config。；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference](https://arxiv.org/abs/2610.28947v1) | 2026-10-22 | equal-bits须计index，硬件最低精度后稀疏仍有条件收益；3 + 2 + 2 = 7 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](https://arxiv.org/abs/2610.28982v1) | 2026-10-22 | text拒绝被外推tool行为安全 → matched triplets+20forbidden actions及direction patch只抑调用/伤benign → refusal signal不是action safety充分控制。；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-SECURITY`，[对应章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](https://arxiv.org/abs/2610.28987v1) | 2026-10-22 | 可信用户值与environment-derived memory混用 → finite gate exact-content confirmations、Lean integrity theorem及community endorsement → 共享memory trust扩展有显式assumption，不让回忆文本自动授权。；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-MEMORY`，[对应章节](../../../../books/part-07-agent/77-memory.md) |
| [Attention-based Classification for Indirect Prompt Injection](https://arxiv.org/abs/2610.28988v1) | 2026-10-22 | scalar attention-focus detector宣称dataset-agnostic → AgentDojo long structured tool输出破假设/近chance，linear perhead改但仍需target-domain data → 检测阈值/协方差不具跨agentic域安全保证。；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-SECURITY`，[对应章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding](https://arxiv.org/abs/2610.29013v1) | 2026-10-22 | 目标再生成后的CE控制收窄了draft目标的相对增量；3 + 1 + 2 = 6 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING`，[对应章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Better Policies, Worse Verifier Audits](https://arxiv.org/abs/2610.29029v1) | 2026-10-22 | 用full-success标签评价component看似自然 → conjunctive目标mixture数学导致好policy反压自身failure分母、refresh选更坏verifier → audit须保own-failure support。ECG是控制反证之一，采用主张为通用verifier-loop数学机制，非领域应用。；3 + 2 + 3 = 8 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GRAFT: Restoring the Missing Sampling Interface in Continuous Diffusion Language Models](https://arxiv.org/abs/2610.29136v1) | 2026-10-22 | continuous dLLM平均候选、无离散采样接口 → rare-word collapse及frozen model早commit再regenerate → 并行连续去噪不能仅以PPL/采样步数评词汇尾覆盖。；3 + 1 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Correlated Failures of AI Approval Monitors](https://arxiv.org/abs/2610.29178v1) | 2026-10-22 | 多票看似独立安全 → shared-source fail-prone sets、source counting与worst-case失败/加非LLM engine才恢复有限条件 → input diversity≠model数量，计票不能抹相关失效。；3 + 2 + 2 = 7 | 深入完成 | 整合：`PLATFORM-SECURITY`，[对应章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Resuming Vision-Language Inference across Onboard Interruptions](https://arxiv.org/abs/2610.29183v1) | 2026-10-22 | interruption丢activation/KV需重跑 → vision/prefill/decode phase-aware checkpoint与layer/token-chunk recovery schedule → inference持久化粒度要按状态寿命/恢复IO取舍，而非训checkpoint照搬。；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-REQUEST-LIFECYCLE`，[对应章节](../../../../books/part-05-inference-system/42-what-happens-during-inference.md) |
| [Understanding Target Probability Reuse in Speculative Decoding](https://arxiv.org/abs/2610.29210v1) | 2026-10-22 | 概率row身份是完整prefix；3 + 1 + 3 = 7 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING`，[对应章节](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Encoded but Unused: Bounding the Sources of VLM Errors](https://arxiv.org/abs/2610.29241v1) | 2026-10-22 | error全归visual encoder→rankprobe+imperfection-aware lowerbounds拆encoded/utilized→升级encoder前先测unused evidence；3 + 1 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Data Schedules and Learning Rate Schedules Should Be Designed Together](https://arxiv.org/abs/2610.29348v1) | 2026-10-22 | MT data通常放末尾被视合理 → fixed compute/MT tokens下只换LR就反转data schedule优劣 → 数据混合与LR必须联合设计。；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[对应章节](../../../../books/part-04-training-system/28-pretraining.md) |
| [Deciding Scale Placement in MXFP4 Dot Products with Integer Arithmetic](https://arxiv.org/abs/2610.29445v1) | 2026-10-22 | 实数scale可移但binary32溢出/下溢依reduction tree → integer finite-state精确QF_LIA legality及static/runtime guard → scale placement不能因代数等价无条件lower。；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [RISK-KV: Quality-Aware Selective KV Cache Reconstruction for Distributed LLM Inference](https://arxiv.org/abs/2610.29544v1) | 2026-10-22 | 全KV恢复很贵 → targetlayer两侧exact state/cross-layer ridge预测missing attention-projection input、fold原KV projection省predictor存储，以实际重建NLL变化risk/quality-gated topology search选layergroup → recovery效率与原模型完整状态exact分责。；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE`，[对应章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [UlaCache: Unified Logical Addressing for Sparse LLM Serving](https://arxiv.org/abs/2610.29820v1) | 2026-10-22 | sparse selector与physical KV placement绑定 → stable logical address+DP/TP共同接口、仅missing transfer/PB-LRU mapping后commit → 选历史token不等后续可丢KV，迁移ready必须单独验。；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE`，[对应章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion](https://arxiv.org/abs/2610.30026v1) | 2026-10-22 | 文档转text被默认语义无损 → OOXML oracle+spanLOO将format-cue失效定位highlight/color并控制wording → ingestion评估需保author强调含义，不把下游错误均归reasoning。；3 + 2 + 2 = 7 | 深入完成 | 整合：`AGENT-RAG`，[对应章节](../../../../books/part-07-agent/76-rag.md) |
| [Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise](https://arxiv.org/abs/2610.28810v1) | 2026-10-22 | session安全评估不覆盖persistent state → 共同threatmodel覆盖memory/project/skills/MCP与跨session/user传播 → 清空对话不清除派生权限污染，需记具体service/version/attack入口。；3+2+2=7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY`，[具体论点所在章节](../../../../books/part-06-ai-infrastructure/72-security.md)，见§4 |
| [Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories](https://arxiv.org/abs/2610.29378v1) | 2026-10-22 | fixed response QAT与低bit自生成prefix偏离 → on-policy teacher监督+candidate-wise Dynamic KL → 量化reasoning恢复需同时管轨迹和分布双向失配。；2+1+2=5 | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[具体论点所在章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，见§4 |
| [A Small Model Asks Better: Fine-Tuning Query Clarification for Retrieval-Augmented Generation](https://arxiv.org/abs/2610.28686v1) | 2026-10-22 | query表面歧义可由context消除/也可retrieved-doc后才歧义 → 3900hardnegative微调区分true vs apparent ambiguity → clarification gate需前后retrieval分母与false asks，不仅给大模型prompt；局部可4分关闭不默认深审。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Building a Nested LADDER for LLM Unstructured Post-Training Pruning](https://arxiv.org/abs/2610.28773v1) | 2026-10-22 | uniform或一次adaptive pruning高稀疏退化 → incremental end-to-end damage/per removed parameter选择生成nested masks → allocation策略需分benign/high sparsity，非单预算最优。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [LIFT: Scoped Constraints for Evaluating and Training Instruction Following](https://arxiv.org/abs/2610.28819v1) | 2026-10-22 | 单条可程序检查约束reward可偏离主任务 → section-scoped双类约束及main-task联合评价 → IF训练不能只优化孤立约束得分。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Flexible Language-Guided Representation Editing for Adaptive Robot Behavior](https://arxiv.org/abs/2610.28893v1) | 2026-10-22 | languagefeature只add过指定→add/generalize/mask三操作消融→localrepr交互可删/泛化非只追加；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [D-Skill: Distilling Teacher Knowledge through Agent Skills](https://arxiv.org/abs/2610.28914v1) | 2026-10-22 | 黑盒student无法weight-KD → fixed paired teacher/student trace的行为divergence/agreement凝成离线skill、无追加环境/labels → transfer介质可显式而非参数，需同rollout/运行费用比较。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [T-DIG: Text-Conditioned Diversity for Image Generation](https://arxiv.org/abs/2610.29003v1) | 2026-10-22 | 单image质量不保用户指定variationaxis→frozen generator外GRPO promptpolicy+axisreward→可加用户轴diversity但非原模型机制突破；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Does Every Instance Count Equally? Order Effects in LLM Multi-Instance Processing](https://arxiv.org/abs/2610.29057v1) | 2026-10-22 | 多独立instance aggregate被当permutation-invariant → fixed set7order/15models发现90pp差且trace/gradient位置偏 → 多实例统计任务需order干预，不以longcontext容量保证aggregation。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run](https://arxiv.org/abs/2610.29121v1) | 2026-10-22 | scaffold edit必须昂贵运行才能选 → fixed fit96edits的parentrate+diff8coord readout，独立steering/test/archive policy → pre-execution proxy要与parent选择/最终return policy隔离，未普证通用编辑质量。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Mitigating Reward Hacking in Realistic Scenarios Through Representation Engineering](https://arxiv.org/abs/2610.29129v1) | 2026-10-22 | uniform steering扰coherence → dynamic intervention减少representation perturbation并crossdomain验证 → monitor/mitigate需绑定激活位置/行为代价，不授production无hacking。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [NormTune: Norm-Guided Parameter-Efficient Fine-Tuning for Reasoning-Intensive Tasks](https://arxiv.org/abs/2610.29134v1) | 2026-10-22 | PEFT reasoning差距被当rank必然 → update-norm under-adaptation观察与layeradaptive加强 → budget/rank之外需核actual update scale，norm关联不自动因果泛化。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Preference Is Not Permission: Personalizing the Auto-Purchase Line in Agentic Commerce](https://arxiv.org/abs/2610.29216v1) | 2026-10-22 | preference-fit被用作autopurchase授权代理 → roleplayed human可授权最远动作/三值输出揭own-warrant缺也提交，personal line可学但不跨域 → 偏好预测与允许commit分开；15roleplay非真实所有用户授权，局部可低分关闭。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Learning Marginal Viewpoint Utility for Budgeted Evidence Selection in RAG](https://arxiv.org/abs/2610.29234v1) | 2026-10-22 | 固定relevance忽略selected evidence已覆盖视角 → within-state marginal viewpoint训练ranker/预算约束重score，RVC1与二来源RVC2 oracleceiling → evidence diversity要按边际/独立source预算而非高分重复。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [ER-Chord: Spatially Consistent One-Step Image Editing via Equal-Energy Reliability Redistribution](https://arxiv.org/abs/2610.29248v1) | 2026-10-22 | temporal稳不保spatial edit一致→equal-energy按neighbor-noise fieldagreement分配strength→同calls下局部编辑控制；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Design and Tuning of Multi-Agent Systems Using Bayesian Evolutionary Optimization](https://arxiv.org/abs/2610.29276v1) | 2026-10-22 | 选workflow候选靠LLM或全面eval贵 → graph-awareGP+ExpectedImprovement挑evolution图 → topology search可显式uncertainty/acquisition，但仍需实测反馈。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Signals and Queries: Token-Efficient Agentic Context Discovery](https://arxiv.org/abs/2610.29326v1) | 2026-10-22 | 每turn所有policy做LLM relevance贵 → offline hard-negative per-policy logistic filter且保高recall → policy检索first stage可局部更新且需看recall-conditioned precision。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331v1) | 2026-10-22 | 自然语言Bayes更新能力常由假设替代 → qualitative coherence/externally-determined posterior quantitative评估对照有无reasoning/code → 区分模型自身coherence与tool-assisted posterior approximation；采用通用belief-update能力边界，不采用科学发现应用结论。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [VideoGen Model 1: Prompt Expansion Versus Formatting in Audiovisual Generation](https://arxiv.org/abs/2610.29407v1) | 2026-10-22 | formatting/creative expansion收益混→30prompt固定seed/generator三arm/judge不一致→不把prompt expansion分数全归格式；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [CCG Diffusion: Combinatory Categorial Grammar-Driven Compositional and Syntactically Disambiguated Text-to-Image Generation](https://arxiv.org/abs/2610.29415v1) | 2026-10-22 | promptattachment含混→CCGcategory生成修改关系、rewriting/attentionguidance→局部syntaxcontrol可不训模型；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [A KAN-based Non-linear Factorization for Embedding Layer Compression](https://arxiv.org/abs/2610.29424v1) | 2026-10-22 | linear低秩bottleneck限制容量 → matched parameter Skipgram非线性projection+初始化 → embedding压缩不只线性rank，局部小模型证据不外推LLM。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training](https://arxiv.org/abs/2610.29454v1) | 2026-10-22 | dense crossviewquadratic→cameratokenkernel/DPP选KV、全frame保query→localcontextselector可省算但需几何质量；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models](https://arxiv.org/abs/2610.29455v1) | 2026-10-22 | Omni能力榜掩长时多speaker困难 → parallel A/V、6语言30min20speaker协议揭tcpWER失效 → 模态互补不能由短片aggregate推长时定位/说话人恢复。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Parallel Thinking for Large Language Model with Path Diversity](https://arxiv.org/abs/2610.29501v1) | 2026-10-22 | RL parallelpaths collapse同策略 → prefix-similarity penalty促路径区分 → parallel budget需验证多样性而非只线程/path数量，token差异不自动语义差异。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Mitigating Query Shortcuts in Chain-of-Thought with Context-Aware Decoding](https://arxiv.org/abs/2610.29518v1) | 2026-10-22 | answer不依赖CoT rationale → contrastive with/without rationale及groundtruth/random干预 → shortcut缓解需看行为依赖，不只答对率。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding](https://arxiv.org/abs/2610.29527v1) | 2026-10-22 | soft-KD拟合高entropy未对acceptance优化 → inference accept/reject隐式preference+masked loss → draft学习目标可直接来自验证反馈。与29013共同检查regeneration混杂，不预合并结论。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [SPARE: Sparsity Allocation via Routing Entropy for Efficient MoEs](https://arxiv.org/abs/2610.29662v1) | 2026-10-22 | expert selector与layer删除数量常混同 → fixedselector/budget、routing-entropy分配及random-pruning bound/干预 → 分清删谁与每层删多少，concentrated route更脆弱。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Scaling Multilingual Pretraining of Pixel Language Models](https://arxiv.org/abs/2610.29681v1) | 2026-10-22 | pixel模型跨script transfer被默认随规模增强 → fixed per-language compute、多语言/script/容量分轴发现unseen script transfer不再随scale增 → 区分本地收益/跨script收益。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Accept or Repair: Preserving Passage-Supported Answers in Contrastive Decoding](https://arxiv.org/abs/2610.29727v1) | 2026-10-22 | 全程contrastive可破坏原本supported答案 → sampled答案先support-check再最多2次repair并reject context-free重复 → 将干预限于证据不支持答案。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Bridging Foundational and Agentic Capabilities of LLMs](https://arxiv.org/abs/2610.29751v1) | 2026-10-22 | foundational profile被视agent预测代理 → operation profile残差/realization gap增预测信息 → 分清基础能力低和执行部署失败。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29792v1) | 2026-10-22 | interleaved RAG历史reasoning引query drift → search momentum诊断及保留knowledge/refined-state、complementary parallel queries → reasoning轨迹需独立于evidence保留策略。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Every Part Has Its Role: Part-of-Speech Effects in LLM Post-Training](https://arxiv.org/abs/2610.29843v1) | 2026-10-22 | concept augmentation泛化被当统一 → noun/verb/adj消融揭downstream与representation变化不一致 → 数据增广收益依concept位置和评价，CKA变化不代行为改善。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit](https://arxiv.org/abs/2610.29870v1) | 2026-10-22 | 周期review或anomalytrigger贵/正常也错 → 首sourceedit前一次planner介入保持executorcontext/workspace，对同cost advisor比较 → intervention checkpoint可用effect边界而非周期，全部planner费另计。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Unintended Side Effects of Value Training in LLMs](https://arxiv.org/abs/2610.29922v1) | 2026-10-22 | 对单价值微调被当局部行为改变 → 4模型cross-value/risk/social/safety的非目标副作用 → alignment回归测试不能只测目标value。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors](https://arxiv.org/abs/2610.29985v1) | 2026-10-22 | aggregates遮capability contrast → LLM提出/分类split、行为information-gain选树 → taxonomy应由model行为辨别而非只人工主题；局部诊断不默认5分以上。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042v1) | 2026-10-22 | coding优化能力可自迁到planning被暗设 → ancestor edit-outcome lineage attribution+general/specialized errorconditioned children → planning harness优化需归因具体constraint违例而非仅大档案。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |
| [Looped Uniform Diffusion Language Models](https://arxiv.org/abs/2610.30066v1) | 2026-10-22 | uniform corruption训练比mask昂贵 → objective/sampler不变iso-FLOP selective looping+loop-count sampling → 效率提升需区分训练共享与denoise NFE。；1 + 1 + 2 = 4 | 已关闭 | 仅报告：局部增量，保留具体关闭理由，不进一步采用 |

| [Is Refusal Direction Universal across Low-Resourced Languages?](https://arxiv.org/abs/2610.28897v1) | 2026-10-22 | safety-aligned语言transfer被外推为普遍 → 3种低资源语言复现、ceiling控制后misaligned source transfer失败且几何/行为部分分离 → 几何对齐不能代替跨语言安全行为验证。；3+1+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[对应具体论点](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [TrainBridge: Agentic NPU Training Optimization Guided by GPU Compilation Evidence](https://arxiv.org/abs/2610.29171v1) | 2026-10-22 | NPU框架fusion不全、profile试错贵 → GPU compiled execution抽optimization intents指导NPU rewrite/profile → 迁移应搬编译意图/证据而非照搬GPU kernel。；2+2+2=6 | 深入完成 | 整合：`AGENT-REFLECTION`，[对应具体论点](../../../../books/part-07-agent/80-reflection.md) |
| [Let Agents Design How They Search: Automatic Interface Optimization for Agentic Search](https://arxiv.org/abs/2610.29250v1) | 2026-10-22 | search接口人工固定跨corpus → trajectory/reward联合优化artifacts/tools/instructions → 工具实现和预处理也应进入search interface优化边界。；2+2+2=6 | 深入完成 | 整合：`AGENT-RAG`，[对应具体论点](../../../../books/part-07-agent/76-rag.md) |
| [Hierarchical Masked Diffusion Language Models](https://arxiv.org/abs/2610.29255v1) | 2026-10-22 | shared noise schedule缺token优先级 → two-pass hierarchy/token及level-specific schedule/NELBO → reveal-order可软约束同时保持并行，而非只能统一噪声或硬序列化。；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应具体论点](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Reader--Writer Coupling in Transformer MLPs](https://arxiv.org/abs/2610.29340v1) | 2026-10-22 | 单factor统计看不见MLP pairing → exact Jacobian signed channel coupling、opposed core和writer干预 → reader/writer独立解释不足以描述残差更新。；2+1+3=6 | 深入完成 | 整合：`MODEL-FFN`，[对应具体论点](../../../../books/part-02-model/16-feed-forward-mlp.md) |
| [Don't Stop Long-Context Continual Pre-Training Too Early: An Empirical Scaling Law](https://arxiv.org/abs/2610.29352v1) | 2026-10-22 | LCCP何时停缺量化依据 → 5scales/100+budgets additive power law+Constant-Last4轨迹观测 → 短程saturation不代长上下文预算终止条件。；2+1+2=5 | 深入完成 | 整合：`MODEL-LONG-CONTEXT`，[对应具体论点](../../../../books/part-02-model/22-long-context.md) |
| [A Strong MoE Is All You Need for Process Supervision](https://arxiv.org/abs/2610.29498v1) | 2026-10-22 | PRM标注依human/rollout/aux verifier → MoE routing mass/variation做process score、selective regenerate/PRM distill → 路由不仅dispatch，亦可提供经验证的置信信息。；2+1+2=5 | 深入完成 | 整合：`AGENT-REFLECTION`，[对应具体论点](../../../../books/part-07-agent/80-reflection.md) |
| [PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States](https://arxiv.org/abs/2610.29545v1) | 2026-10-22 | recurrent state逐token 4bit舍入误差累积 → periodic rounding+buffer、column scale、error-retaining head8bit → state压缩需改变舍入时序而非只有bitwidth/finetune。；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[对应具体论点](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](https://arxiv.org/abs/2610.29671v1) | 2026-10-22 | construction/retrieve联合RL group混杂且feedback稀疏 → Stage-Decoupled GRPO固定另一stage变化+Event-Wise credit → end-to-end memory优化需要可归因分组。；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[对应具体论点](../../../../books/part-07-agent/77-memory.md) |
| [S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration of LLMs](https://arxiv.org/abs/2610.29832v1) | 2026-10-22 | openended多string同semantic导致confidence错粒度 → prompt-specific semantic class Dirichlet从sequence likelihood可微构造 → calibration训练应对变动语义类而非固定MC/string对错。；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[对应具体论点](../../../../books/part-04-training-system/33-grpo.md) |
| [Scan or Index? large Evidence Coverage, Answer Quality, and Cost in Long-Document RAG](https://arxiv.org/abs/2610.28957v1) | 2026-10-22 | full scan看似全证据覆盖 → fixed generator/top5下后续reduction丢证据且coverage/answer分离 → scan/index选择同时评retain、answer、reuse cost。；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG`，[对应具体论点](../../../../books/part-07-agent/76-rag.md) |
| [MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents](https://arxiv.org/abs/2610.29249v1) | 2026-10-22 | 多模态memory端到端分数无法定位丢失 → fixed reader/prompt/budget对representation/retrieve/deliver干预 → 区分写入与reading残差，不以gold evidence等同可回答。；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-MEMORY`，[对应具体论点](../../../../books/part-07-agent/77-memory.md) |
| [Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems](https://arxiv.org/abs/2610.29292v1) | 2026-10-22 | topology score不指明谁贡献 → trace contrast attribution指导supergraph pruning、matched search budget → 选团队不能只按全任务标量和随机增删。；2+1+2=5 | 标准完成 | 仅报告：局部credit启发式及限定评价，不新增长期机制 |
| [Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics](https://arxiv.org/abs/2610.29225v1) | 2026-10-22 | binary安全label判据混用/一致性低 → prompt-level safety/exemption与usefulness分开rubric → 不把拒绝一切或judge一致性直接当安全能力。；1+1+2=4 | 深入完成 | 仅报告：本窗README统计纠错，非新实验 |
| [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933v1) | 2026-10-22 | KG离散symbol丢context且重写添噪声 → context-intact semantic nodes/topology+energy diffusion deterministic linearization → evidence path可保上下文，不必先抽关系再生成重述。；2+1+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG`，[对应具体论点](../../../../books/part-07-agent/76-rag.md) |

| [ReAPO: Retry-Aware Policy Optimization for Efficient Exploration in LLM Reasoning](https://arxiv.org/abs/2610.28770v1) | 2026-10-22 | failed strategies重复且serial retry credit不清 → stochastic-shortest-path下GRPO改法只强化成功retry、不奖励先前failure → exploration预算/credit按attempt cost而非iid group。；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[对应具体论点](../../../../books/part-04-training-system/33-grpo.md) |
| [How Much Gradient Does Truncated Backprop Lose in Looped Transformers?](https://arxiv.org/abs/2610.28871v1) | 2026-10-22 | loop数/指数shrink直觉代替真实gradient损失 → 一backward各k精确量、训练后loss变化及不优于简单rule反证 → pretrain静态lost-gradient不是训练预算选择充分统计量。；2+1+2=5 | 深入完成 | 整合：`TRAIN-PRETRAINING`，[对应具体论点](../../../../books/part-04-training-system/28-pretraining.md) |
| [One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents](https://arxiv.org/abs/2610.29427v1) | 2026-10-22 | 同effect多text却ratio/credit绑单response → effect-level surrogate耦合textual realizations、credit不改且无新rollouts → policy update粒度需对齐execution equivalence。；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[对应具体论点](../../../../books/part-04-training-system/33-grpo.md) |
| [ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization](https://arxiv.org/abs/2610.29410v1) | 2026-10-22 | preference ranking提升看似模型改善 → common-mode hidden offset对relative loss隐身并形成vocab well，注入/遮罩因果干预 → ranking score不足预警generation collapse。；3+1+3=7 | 深入完成 | 整合：`TRAIN-DPO`，[对应具体论点](../../../../books/part-04-training-system/34-dpo.md) |
| [DynaWeave: Learning to Adapt through Dynamic Scenario Synthesis](https://arxiv.org/abs/2610.29443v1) | 2026-10-22 | 训练环境只被agent行动改变 → exogenous event DAG+only-affected verifier checks → 动态场景训练需保持未触发条件/评价一致性。；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应具体论点](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications](https://arxiv.org/abs/2610.29767v1) | 2026-10-22 | identifier rename掉分被解释memorization → TLA+ oracle证明重命名behavior preserving、name-based grading占多数下降 → rename评估需分训练记忆/评分名依赖/new-name成本。；3+1+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应具体论点](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](https://arxiv.org/abs/2610.29995v1) | 2026-10-22 | image→text丢视觉细节、raw pixels难跨session identity → mention/fact occurrence/evolution/evidential typed hyperedges+source verification → memory要同时保identity变化与provenance，不用单摘要替代。；2+2+2=6 | 深入完成 | 整合：`AGENT-MEMORY`，[对应具体论点](../../../../books/part-07-agent/77-memory.md) |
| [CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents](https://arxiv.org/abs/2610.29965v1) | 2026-10-22 | RL+distill scalar mix仍梯度抵消 → protected objective与projection gate分责、nearest-point闭式组合 → 不能只调mix权重或无条件投影。；2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-PRETRAINING`，[对应具体论点](../../../../books/part-04-training-system/28-pretraining.md) |
| [Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722v1) | 2026-10-22 | RAG component独立提升被相加 → 450config/8bench/5k-200k corpus检验不compose、retrieval/faithfulness冲突 → full stack和corpus scale必须共同评。；3+2+2=7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[对应具体论点](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [MemoryTax: The Bitter Lesson of Agent Memory](https://arxiv.org/abs/2610.29823v1) | 2026-10-22 | stronger reader可补弱writer外存被暗中假设 → 同一419turn conversation3reader/7methods显writer ceiling及成本，photo访问混杂被自揭 → 外存比较需同可见证据并记writer成本；单run局部，不排也不普遍化。；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MEMORY`，[对应具体论点](../../../../books/part-07-agent/77-memory.md) |
| [Keeping Time vs. Understanding Time: Neither Alone Explains Temporal Reasoning in LLMs](https://arxiv.org/abs/2610.29507v1) | 2026-10-22 | arithmetic/semantic二分被当可转移能力 → 同mode微调跨数据几无transfer、knowledge驱动 → benchmark taxonomy不等能力因果分解。；2+1+2=5 | 深入完成 | 仅报告：受限构念/测量结论，不外推通用机制 |
| [Environment Duels: A Microcosm of LLM Co-Evolution](https://arxiv.org/abs/2610.30116v1) | 2026-10-22 | solver分数默认代表task author能力 → privileged hint lift区分author/solver并与heldout RL gain关联 → self-curation不能只选最强solver充当author。；2+2+2=6 | 标准完成 | 仅报告：受限构念/测量结论，不外推通用机制 |

| [Events, Not Pixels: Where World Models Get the Return Wrong](https://arxiv.org/abs/2610.29435v1) | 2026-10-22 | 视觉重建误差不定位return误差，固定reader的event/random/complement/all-real四arm离线诊断；3+2+2=7 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应论证](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Parallel AI Agent Collaboration as Graph-Structured Distributed Block Optimization](https://arxiv.org/abs/2610.30074v1) | 2026-10-22 | 有限已知factor依赖下，用兼容集cover界定固定base非负单项gain的可保留份额；2+2+3=7 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[对应论证](../../../../books/part-07-agent/82-multi-agent.md) |

| [SimHack: Predicting the onset of detectable reward hacking before RL training](https://arxiv.org/abs/2610.28707v1) | 2026-10-22 | 同漏洞环境下logit-offset与momentum模拟开跑前可检测reward-hacking风险，截断t50只作recipe比较，不是潜伏作弊检测或因果保证；2+2+2=6 | 深入完成 | 整合：`TRAIN-RLHF`，[对应章节](../../../../books/part-04-training-system/31-rlhf.md) |
| [An Explicit Feedback Contract for Iterative ML-Agent Harnesses](https://arxiv.org/abs/2610.28798v1) | 2026-10-22 | 隐藏标签后仍需限制validation反馈通道，分开accepted-update与有限精度best-score；paired-SE启发式不自动继承fixed-margin保证；2+2+2=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](https://arxiv.org/abs/2610.28811v1) | 2026-10-22 | probe可读与实际locator/writer注入效果分开，受限grafting证据支持已有表示可用性边界，不把解码成功当完整因果；2+1+2=5 | 标准完成 | 已有覆盖：`WORLDVIEW-REPRESENTATION`，[对应章节](../../../../books/part-01-worldview/05-what-neural-networks-learn.md) |
| [Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning](https://arxiv.org/abs/2610.28785v1) | 2026-10-22 | 固定group大小前按任务后验与组内相关性分配rollout，非退化组不等有益梯度，旧bank成本不因新采样减少消失；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO`，[对应章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Transformers as Generic Deep Neural Networks: Exact Compilation, the Cost of Removing Activation-Activation Products, and Multi-Agent Attention Clustering](https://arxiv.org/abs/2610.28958v1) | 2026-10-22 | 精确编译先声明primitive与乘法权限，分离Score/Mix的代数下界不等融合全图或时延下界，也不授低精度bitwise等价；2+1+3=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next](https://arxiv.org/abs/2610.28998v1) | 2026-10-22 | 长期rollout的pinned arena与分层梯度/异步checkpoint须分工作集和完成状态，前台返回不等后台持久化，既有Ch39/35已承载；1+2+2=5 | 标准完成 | 已有覆盖：`TRAIN-ZERO`，[对应章节](../../../../books/part-04-training-system/39-zero.md) |
| [Conditional Flow Models Convert Epistemic Uncertainty into Apparent Aleatoric Variance](https://arxiv.org/abs/2610.29172v1) | 2026-10-22 | condition欠拟合可把邻域均值差混入spread，受条件核模型约束的均值界不授任意网络或逐输入uncertainty coverage；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Flat-RLVR: Sharpness-Aware Reinforcement Learning with Verifiable Rewards for Reasoning Capacity in LLMs](https://arxiv.org/abs/2610.29281v1) | 2026-10-22 | 固定rollout周期的sharpness-aware更新改变几何而非reward，频率可提高pass@k却损pass@1，近似扰动重构非免费精确restore；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[对应章节](../../../../books/part-04-training-system/33-grpo.md) |

| [JUICE: Unified Multimodal Modeling in Pretrained Representation Spaces](https://arxiv.org/abs/2610.28801v1) | 2026-10-22 | LM文本/diffusion图像固定先后→frozen双encoder空间单flow/独立noiselevel joint条件生成→不必强制某模态先生成，wording损失另验；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State](https://arxiv.org/abs/2610.28827v1) | 2026-10-22 | 无限map几何不能全常驻/返回edit丢失→typedMacro/Micro/neighbor commitments与singleworldrecord再编译→计划、geometry residency与mutable state分开；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [DualHeads: Reward-tilted few-step diffusion made simple](https://arxiv.org/abs/2610.28858v1) | 2026-10-22 | fewstep缺多步scorepath/可微reward→reward/reference两classifierlogits对KLregularized目标→只externalreward也可改fewstepgenerator；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision](https://arxiv.org/abs/2610.28954v1) | 2026-10-22 | pairedvideo稀缺→image R2C featuremapping造pseudocoarsevideo后丢teacher→训练pair要求可从video下放image；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Cache Locally, Recompute Selectively for Streaming Video Understanding](https://arxiv.org/abs/2610.29229v1) | 2026-10-22 | idle短contextprefill丢将来query所需/存无关→queryselected re-prefill替KV→idle/query时点重分contextualization费用；2+2+2=6 | 深入完成 | 整合：`INFER-KV-CACHE`，[对应章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Think-Capture: Active 3D Geometry Acquisition for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.29232v1) | 2026-10-22 | densegeometry贵且误估可误导→querycritical按需toolgeometry+GRPO包含误导case→geometry只作可错证据而非固定信任；1+2+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [AdvFidelity: Unifying Preference Alignment and Few-Step Image Generation within Reinforcement Learning](https://arxiv.org/abs/2610.29380v1) | 2026-10-22 | fewstep RL特定reward漏artifact→online content-matched reconstruction负样本fidelity reward→不一定多阶段DMD后处理；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces](https://arxiv.org/abs/2610.29408v1) | 2026-10-22 | actiondimension跨任务语义与agent绑定混→spatial agentgate+schema/value conditioning、causal rollout distill→多agent control的实体绑定与变量语义分责；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers](https://arxiv.org/abs/2610.29441v1) | 2026-10-22 | layerstep局部metric不等finalvideoerror→probe/trajectorycalibration共同预算density保selector/kernel→allocation应看end-output与measuredlatency；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Melange: A Synthetic Visual Bias Benchmark for Multi-modal Large Language Models](https://arxiv.org/abs/2610.29537v1) | 2026-10-22 | 匹配text/image/context区分属性可见性与使用失败，90–95%perception control仅七个代表模型且非纯因果隔离，不授全模型公平性结论；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

| [Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding](https://arxiv.org/abs/2610.29552v1) | 2026-10-22 | region理解/定位分训需captionjudge→region→description→regioncycle IoUreward跨spacetime→可用可验证逆任务代judge；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Unlocking Spatial Grounding in Flow-Matching Models via SNR Tuning](https://arxiv.org/abs/2610.29581v1) | 2026-10-22 | controlled primitives上的noise schedule改变spatial grounding，以VAE重构/YOLO为经验参照而非硬上界，不把额外adapter视为唯一解释；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [CineEvolve: An Agentic Self-Evolution Framework for Cinematic Multi-Shot Video Generation](https://arxiv.org/abs/2610.29590v1) | 2026-10-22 | director/critic互训优势膨胀→historicalanchor/revisionguard EGRPO→co-evolving reward与policy需跨代参考；2+1+2=5 | 深入完成 | 整合：`TRAIN-GRPO`，[对应章节](../../../../books/part-04-training-system/33-grpo.md) |
| [Rethinking Post-hoc Debiasing of Large Pretrained Models](https://arxiv.org/abs/2610.29688v1) | 2026-10-22 | 文本给定bias被当足够→双cooccurbias连真值identity也不救、closestcrossclassgeometry线性map→能否文本描述bias不是无害前提；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Compositionality with Primitives: A Unified View from Euclidean to Hyperbolic Vision-Language Models](https://arxiv.org/abs/2610.29811v1) | 2026-10-22 | novelcomposition需要显式pair recompose→primitive直接score跨embeddinggeometry对照→recomposition非必需的单表示边界；3+1+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs](https://arxiv.org/abs/2610.29854v1) | 2026-10-22 | globaldenoise难归因→GMRF局部context近似+realDiT噪声dependent聚合/patchpredictor transplantation→attention/MLP干预按角色而非通用换件；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

| [GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal Gradient Accumulation and Projection](https://arxiv.org/abs/2610.29355v1) | 2026-10-22 | 逐token routed leader只以旧outputgradient基按门控/强度削follower分量，本步先投影再更新leader-only FIFO；2+1+2=5 | 深入完成 | 整合：`MODEL-MOE`，[对应章节](../../../../books/part-02-model/21-moe.md) |
| [Parallelizable Probabilistic Latent Reasoning for Diverse Reasoning Trajectories](https://arxiv.org/abs/2610.29385v1) | 2026-10-22 | exact-v1 posterior读CoT并行给目标、prior teacherforce联合学，部署仍AR；实际Eq27含stopgrad balance/dispersion/均值VISReg，非未改动ELBO；2+1+2=5 | 深入完成 | 整合：`TRAIN-SFT`，[对应章节](../../../../books/part-04-training-system/29-sft.md) |
| [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](https://arxiv.org/abs/2610.29426v1) | 2026-10-22 | stabletrajectory→worker/DB registry整轨持有、结束释放、lazyreset；12.8x只是online lifecycle I/O且排69GiB建池，非peakmemory/端到端吞吐；2+2+2=6 | 深入完成 | 已有覆盖：`AGENT-PLATFORM`，[对应章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458v1) | 2026-10-22 | 5因素低阶18配置与近邻successive updates组织训练人口，pair平衡非高阶或信息等价；主测18heldout非225全组合，Full243含测试只stress；2+2+2=6 | 深入完成 | 整合：`AGENT-PLATFORM`，[对应章节](../../../../books/part-07-agent/84-agent-platform.md) |
| [Stochastic Pruning of the DPO Computation Graph: 1.4x Faster Training and Lower Peak Memory](https://arxiv.org/abs/2610.29538v1) | 2026-10-22 | head选位置/suffix不执行/branch不反传省不同图；2+2+2=6 | 深入完成 | 整合：`TRAIN-DPO`，[对应章节](../../../../books/part-04-training-system/34-dpo.md) |
| [Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.29734v1) | 2026-10-22 | PDF必要p1–10/15/21/23/33–36：沿原Anwar MI作lower-tail独立修复，以固定CoT的conditional output软约束限制私人重编码，不只marginal行为；2+2+2=6 | 深入完成 | 整合：`PLATFORM-SECURITY`，[对应章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Your Benchmark Is an Empirical Measure Over Difficulty](https://arxiv.org/abs/2610.29927v1) | 2026-10-22 | 用途difficultymeasure失配与题库support gap不同；固定z/n/独立Bernoulli下空区间改善可完全不可辨，再多重复不补支持；2+1+3=6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FrontierCS 2: A Benchmark for Computer Science R&D](https://arxiv.org/abs/2610.29932v1) | 2026-10-22 | workingrepo任务中平均quality/速度更好仍可能两个clip失败，everymetric×heldout合取不同于均值；2+1+2=5 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

| [Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration](https://arxiv.org/abs/2610.28880v1) | 2026-10-22 | 单RGB人视频难跨objectrobotdata→3Dsemantic cousin对齐含功能region、feasiblegrasp/物理render分工→示范可扩语义instance但非同真实接触；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action](https://arxiv.org/abs/2610.28882v1) | 2026-10-22 | episodememory随frame量长→共同metalearnedorigin的INR weightdelta固定size+projectortoken→参数式episodeobject可检索外直接read，信息容量非无限；2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY`，[对应章节](../../../../books/part-07-agent/77-memory.md) |
| [SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training](https://arxiv.org/abs/2610.29161v1) | 2026-10-22 | HIL纠错时机人贵/intervalsnap浪费→privileged progressgraph stable snapshots后阶段回退expert、crossfit/LPF value→纠错数据来源与状态恢复资格分开；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [How Representational Priors Shape Generalization in World Action Models](https://arxiv.org/abs/2610.29168v1) | 2026-10-22 | backbone选型靠事后success→nuisanceorthogonality前瞻与postpolicy suppression关联→选择prior需测nuisance而非modelname；2+1+2=5 | 标准完成 | 仅报告：有限样本表示诊断相关，不足形成新通用模型选择准则 |
| [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](https://arxiv.org/abs/2610.29203v1) | 2026-10-22 | goalsuccess被当instructionfollowing→samehistory/state pairedbranchinstruction/likelihood/attribution→VLA验证需instruction-action因果敏感；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation](https://arxiv.org/abs/2610.29246v1) | 2026-10-22 | RGB-D各自decode不保共同actionstate→metricshared/private features及fixedprivate futuredecode、FK一致性→geometry content/coordinate/future匹配分责；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation](https://arxiv.org/abs/2610.29264v1) | 2026-10-22 | offline收deployment经验更新慢/RLcritic复杂→provenanceconditionedSFT online human/policyrollout异步checkpoint→可无critic更新但updatedavailability≠更好最终质量；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Relational Geometry Forcing for World Action Models](https://arxiv.org/abs/2610.29282v1) | 2026-10-22 | pointwise对照出现无训练重复的有限小幅反退，提出intraframe/crossview/action-time关系监督替代；不据此断言几何监督普遍伤动作；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

| [CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion](https://arxiv.org/abs/2610.29915v1) | 2026-10-22 | motionstate denoise中rise/fall→identifiedlayer delta-token动态3Dalignment→geometry alignment应对变化而非静态scene；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989v1) | 2026-10-22 | teacherforced相邻冗余可shortcut→预测隔开futurechunk不看中间、inference不变→训练要逼视觉演化非只连续外观；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Attn-Forcing: Learning Full-Context Attention Proxies for Streaming Video Generation](https://arxiv.org/abs/2610.30036v1) | 2026-10-22 | boundedlatent未保query相关历史attention→learnedvisualproxy/update+fullcontext attentionmatching→压缩监督对齐response非仅token重构；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089v1) | 2026-10-22 | 给定memory答题不测主动capture→notification与start-stop intervention lifecycle+后续QA→时机/维护与阅读分开验；2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY`，[对应章节](../../../../books/part-07-agent/77-memory.md) |
| [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120v1) | 2026-10-22 | state/language/reconstruction各encoder分裂→stillimage/text三objective+crossview refine共享patchtoken并控encoder对照→worldmodel表示可同时inspection/instruction/control；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [VoxProg: 3D Spatial Reasoning through Voxel Programming](https://arxiv.org/abs/2610.30127v1) | 2026-10-22 | implicitgeometryrefs难由语言指定→localvoxel evidenceprogram和poseprogram测mesh/可执行feedback→几何证据获取与SE3动作分开；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129v1) | 2026-10-22 | offlineT2V VAE压缩默认迁worldmodel→sameWM多compression小bottleneck控，still/movingcamera的spatial/temporal选择相反→compression要按actionlatency/运动而非图像质量；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [T-WLA: Bridging Slow Vision and Fast Touch](https://arxiv.org/abs/2610.28814v1) | 2026-10-22 | contact变快visualpolicy慢→同visualmemory缓存给tactile residualeditor改未执行chunk→slowfast控制不需每触觉重跑vision；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

| [Compressing Onboard Language Models for Space Robots under a Behavioral-Fidelity Requirement](https://arxiv.org/abs/2610.29302v1) | 2026-10-22 | lowbitfamily单独固定→compatiblecheckpoint按linear模块混合且finaldistributionKL门→静态产物组合不能仅localreprscore；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection](https://arxiv.org/abs/2610.29646v1) | 2026-10-22 | audit关联可靠被当corpus选型有用→56fit/80prospective corpora的top20%无incrementalselectiongain→无符号switch丢bothright/bothwrong方向；3+1+2=6 | 深入完成 | 整合：`TRAIN-DATA`，[对应章节](../../../../books/part-04-training-system/27-data.md) |
| [Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357v1) | 2026-10-22 | storage×read grid交互2.93pp是对话cluster CI；IdeaBench online eval会写，t0不为空、cap不binding，summary少tokens反慢且F1损；2+2+2=6 | 标准完成 | 已有覆盖：`AGENT-MEMORY`，[对应章节](../../../../books/part-07-agent/77-memory.md) |
| [Reorienting the Vector Axis: Restructuring FlashAttention for Long-Vector Processors](https://arxiv.org/abs/2610.29489v1) | 2026-10-22 | 长vector以query轴连续令每lane维护一个query max/sum、沿key逐元素累积，归一仍每query keys；2+1+2=5 | 深入完成 | 整合：`INFER-TENSORRT-LLM`，[对应章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference](https://arxiv.org/abs/2610.29873v1) | 2026-10-22 | 目标NPU perchannel tensor allocation/注册区与发送端layout变换联合，单连续buffer可channel OOM，RDMA接通不等可消费tensor；2+2+2=6 | 深入完成 | 整合：`INFER-PD-DISAGGREGATION`，[对应章节](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [pplx-embed-v2-late Technical Report](https://arxiv.org/abs/2610.29523v1) | 2026-10-22 | 共同teacher token欧氏norm监督连接小query/大doc多向量index，非任意encoder互换；全attention去mask不使GDN全双向；1+2+2=5 | 标准完成 | 已有覆盖：`AGENT-RAG`，[对应章节](../../../../books/part-07-agent/76-rag.md) |
| [Qwen-Audio-3.1-ASR Technical Report](https://arxiv.org/abs/2610.28711v1) | 2026-10-22 | 3.0原文已有display/final刷新，本窗仅IDnumber稀疏CE×10与12.5Hz/80ms输出标签grid增量；不由帧率推hidden无subframe信息；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION`，[对应章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [Directional Posterior Feedback Fusion for Query Reformulation in Dense Retrieval](https://arxiv.org/abs/2610.29464v1) | 2026-10-22 | 切空间每feedback仅约束支持方向，与query prior联合小系统/有界sphere更新；点目标多惩未表达正交方向是几何identity，非语义真值；2+1+2=5 | 深入完成 | 整合：`AGENT-RAG`，[对应章节](../../../../books/part-07-agent/76-rag.md) |

| [FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring](https://arxiv.org/abs/2610.29692v1) | 2026-10-22 | steady倾倒像/pose不变但mass增长→motor与completion估计分开、forcehistory+residualoutflow门→视觉actionchunk不充分表任务剩余量；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [CausGround: Causal Interaction Grounding for Adaptive Embodied Planning](https://arxiv.org/abs/2610.29702v1) | 2026-10-22 | 非结构experience难跨任务groundprecondition→actioncenteredconditions/effects factorized objects/relations并前后reasoning→modelproposal动作需可执行依赖；1+2+2=5 | 标准完成 | 已有覆盖：`AGENT-PLANNING`，[对应章节](../../../../books/part-07-agent/79-planning.md) |
| [Reconstruction-Augmented Visuomotor Pre-Training of 3D-Grounded Bimanual Dexterity from RGB-Only Human Videos](https://arxiv.org/abs/2610.29716v1) | 2026-10-22 | humanhandmotion单独无scene3D→sharedvideo scalehandprior、geometry输入/target及gatedfusion，matched hand-onlycontrol→示范pretraining需context而非仅手轨迹；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies](https://arxiv.org/abs/2610.29730v1) | 2026-10-22 | ensemble uncertainty昂贵→singlefrozenembeddingGPconditionalvariance无targetfit，taskcoveragevswithinrank控制 → uncertaintyproxy需区分跨task覆盖/执行变异；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.29866v1) | 2026-10-22 | stepgeometry独立丢历史/teacheralign扭VLM→dedicatedGeoPlan+geometryflowtarget与eventmemory融合，inference无teacher/reconstruct→持久taskgeometry可不直接改nativefeatures；2+1+2=5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.30097v1) | 2026-10-22 | failedatom TD跨boundary污染credit→semanticgate约束TD+masteryadaptiveexploration→多subtask RL按有效原子边界归因；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Asymmetric On-Policy Distillation Learns In-Context Exploration](https://arxiv.org/abs/2610.30105v1) | 2026-10-22 | privilegedexpert不explore故offlineimit平均→studentonpolicyhistory条件expertlabel→可从不探索expert学search/resolvehiddenstate；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation](https://arxiv.org/abs/2610.30117v1) | 2026-10-22 | visualstate缺load/contact→motion-wrench timealignedchunk/paircausalattention+20Hzadmittance外环→生成force reference不能替实际forcefeedback；2+2+2=6 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

| [Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](https://arxiv.org/abs/2610.30103v1) | 2026-10-22 | 同surface结构造P/NPC twin、同class内familiarity hardening是两轴控制；有限gate/480人审20移除不授全改写形式保义；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://arxiv.org/abs/2610.30132v1) | 2026-10-22 | 短QA/evidence骨架后扩长context；字符串/ID gate不证明完整support/distractor语义，程序needle序号标签另源；2+1+2=5 | 深入完成 | 整合：`TRAIN-DATA`，[对应章节](../../../../books/part-04-training-system/27-data.md) |

| [EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL Prefix Importance-Ratio Clipping](https://arxiv.org/abs/2610.29999v1) | 2026-10-22 | §3–5及相关反例区分归一化prefix/EOS与共同support上的精确性能恒等式、实际current-token替代梯度；φ逆KL坐标不把裁剪平台变成hardKL或单调改进；2+1+3=6 | 深入完成 | 整合：`TRAIN-PPO`，[对应章节](../../../../books/part-04-training-system/32-ppo.md) |
| [Mitigating Model Collapse through Dreaming Learning](https://arxiv.org/abs/2610.30009v1) | 2026-10-22 | 机制与受限递归实验区分synthetic采样温度和训练温度/损失权重，真实anchor累计不自动阻止模型坍塌；谱稳定也可保留偏差；2+1+3=6 | 深入完成 | 整合：`TRAIN-DATA`，[对应章节](../../../../books/part-04-training-system/27-data.md) |
| [Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](https://arxiv.org/abs/2610.30014v1) | 2026-10-22 | 共享外部历史、teacher-forced固定动作logprob构造behavior近邻，仍需完整forward/参考与独立校准；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Loopholing All the Way: Language Modeling with pure Self-Conditioning](https://arxiv.org/abs/2610.30068v1) | 2026-10-22 | LAW以expected embedding作为唯一跨步状态，UDM训练腐化不等离散reverse kernel/GaussianODE或新精确NELBO；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Circuits of LLM Classifiers](https://arxiv.org/abs/2610.30076v1) | 2026-10-22 | 有限二元instrument池的已知/估计条件概率与成本支持停止/继续DP，3^n状态不是通用Agent最优性；2+1+3=6 | 深入完成 | 整合：`PLATFORM-GATEWAY`，[对应章节](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching](https://arxiv.org/abs/2610.30107v1) | 2026-10-22 | VAP把population velocity MSE分成Bayes floor和excess；同path/population的强reference差只能抵消共同floor而得相对误差；2+1+3=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS`，[对应章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |

| [Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698v1) | 2026-10-22 | §3–6与必要人口/seed协议表明固定non-Minecraft池只改mixture而非世界数量；loss/源域改善不授远域收益，120配置单训练seed且API部署混杂；2+1+2=5 | 标准完成 | 已有覆盖：`WORLDVIEW-SCALING-LAW`，[对应章节](../../../../books/part-01-worldview/07-scaling-law.md) |
| [Fig: Automated Multiagent Behavior Elicitor](https://arxiv.org/abs/2610.28891v1) | 2026-10-22 | §2–5/A5/B3将行为机会、规范、尝试/执行/后果分开；机械positive可补语义negative，机械未命中不证明不存在；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication](https://arxiv.org/abs/2610.28905v1) | 2026-10-22 | §3–8必要对照在冻结diffusion backbone、监督codec中分开正确私有消息和handoff时机；依赖查询的任务需早交换、独立证据任务singlelate反优多轮；2+2+2=6 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[对应章节](../../../../books/part-07-agent/82-multi-agent.md) |
| [DiffResearch: Accelerating Deep Research with Diffusion Language Models](https://arxiv.org/abs/2610.28909v1) | 2026-10-22 | §3–5/限制中首个可解析固定数量子查询仅允许只读consumer，稳定不证明事实或最终文本；局部decomposition提前未进一步缩短end-to-end pipeline；2+2+2=6 | 深入完成 | 整合：`AGENT-WORKFLOW`，[对应章节](../../../../books/part-07-agent/81-workflow.md) |
| [Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934v1) | 2026-10-22 | §3–6/A/B4/C4–5/D1支持pre-mutation状态capture、前置、durability与可重建分验；workspace外专设人口、judge-positive校准和字符similarity不授业务等价或自然事故率；2+2+2=6 | 深入完成 | 整合：`AGENT-TOOL-CALLING`，[对应章节](../../../../books/part-07-agent/78-tool-calling.md) |
| [AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards](https://arxiv.org/abs/2610.28989v1) | 2026-10-22 | §2–4与VIOLA必要域表明允许tool仍可因argument/resource/state违规；preaction guard不能读取未来verdict，Level4阻断与仅flag区分，archive收益随threshold改变、OOD CI跨0且误拒上升；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-SECURITY`，[对应章节](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Inheritance as an Admission Test for LLM Prompt Merge Operators](https://arxiv.org/abs/2610.29023v1) | 2026-10-22 | §3–5以operator自身零dose、heldout/reprobe检查donor传递，文字百分比不是几何插值；冻结panel与pooled best-seed仅单模型/单博弈附加诊断，不能把selection均值升当新学能力；2+1+2=5 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[对应章节](../../../../books/part-07-agent/82-multi-agent.md) |

| [Robust Soft Skill Adaptation via Behavioral Localization in Tool-Using Agents](https://arxiv.org/abs/2610.30041v1) | 2026-10-22 | §3–4/T1在同一成功teacher轨迹上以有/无textskill的gold-token gain乘全词表JS提监督位置，8inputembedding软提示另有preservation anchor；2+1+2=5 | 标准完成 | 已有覆盖：`TRAIN-SFT`，[对应章节](../../../../books/part-04-training-system/29-sft.md) |

| [GRAM: Group-wise Rank-Aware Model Merging via Subspace Alignment](https://arxiv.org/abs/2610.29110v1) | 2026-10-22 | §3–6/D2/D6将同基座task delta按输出子空间分成K组、组内rank预算重建，理论投影basis最优不授column-stacked实际算法最优或整网质量；2+1+2=5 | 深入完成 | 整合：`TRAIN-LORA`，[对应章节](../../../../books/part-04-training-system/30-lora.md) |

| [LaVGuard: Selective Decoding for Contextual Value Drift](https://arxiv.org/abs/2610.29135v1) | 2026-10-22 | §3–6与必要费用/估计条件区分authorized任务profile、visible-prefix probe、density触发与prototype方向，不能认证价值真值；2+1+2=5 | 深入完成 | 整合：`PLATFORM-SECURITY`，[对应章节](../../../../books/part-06-ai-infrastructure/72-security.md) |

| [Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model](https://arxiv.org/abs/2610.29139v1) | 2026-10-22 | §3–5与必要D/E/F表明frozen actor先提案，advisor检查真实history和动作，可pass或提出pitfall后重提案；每轮去旧guidance防预测当事实；2+2+2=6 | 深入完成 | 整合：`AGENT-PLANNING`，[对应章节](../../../../books/part-07-agent/79-planning.md) |

| [PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents](https://arxiv.org/abs/2610.29467v1) | 2026-10-22 | §2–4/C8/C9中TopK检索分布集中度只缩放语义/NLI偏差，不测事实真值；miss使该轮无法correct，forced hit只恢复部分差额，低集中度也延迟真实drift；2+1+2=5 | 深入完成 | 整合：`AGENT-MEMORY`，[对应章节](../../../../books/part-07-agent/77-memory.md) |
| [TraceForge: Distilling with Your Own Thinking](https://arxiv.org/abs/2610.29680v1) | 2026-10-22 | 仅精确v1 §2–5/T1–2：执行trace的来源真实性不等推理正确或监督资格，style与训练数据差异未隔离，3500/5000口径分开；单run、重复评测非重复训练和HumanEval非单调保留；1+2+2=5 | 标准完成 | 已有覆盖：`TRAIN-SFT`，[对应章节](../../../../books/part-04-training-system/29-sft.md) |

| [RubricOpt: Self-Revision of Semantic Rubrics for Preference Optimization](https://arxiv.org/abs/2610.29491v1) | 2026-10-22 | §3–4/C2/C3固定pairs、labels与两臂response-normalized配方，用训练准则条件后撤去，当前policy可提specgap编辑但已覆盖未学会须keep；2+2+2=6 | 深入完成 | 整合：`TRAIN-DPO`，[对应章节](../../../../books/part-04-training-system/34-dpo.md) |

| [UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users](https://arxiv.org/abs/2610.29822v1) | 2026-10-22 | §4–6/C1–3/Alg2/D3把固定任务persona链、动态信息release和interaction预算分开；候选请求test rewrite须实际candidate通过/base失败/全regression通过，再经非原Judge Reviewer核行为与attestation；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM`，[对应章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |

| [ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination](https://arxiv.org/abs/2610.29934v1) | 2026-10-22 | §2–4/A–C中同坐标partner实际thought仅训练target，部署从main自身可见context生成latent，不读取对方真实私有state；2+2+2=6 | 深入完成 | 整合：`AGENT-MULTI-AGENT`，[对应章节](../../../../books/part-07-agent/82-multi-agent.md) |

| [Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control](https://arxiv.org/abs/2610.29329v1) | 2026-10-22 | runtime回忆推理负担大→streaming写executablesubtasklist、update-supervision扩充/selflabel verification→写入时前移未来控制但当前VLA仍选动作；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

| [PhysiCalWorld: In-Context Physics Calibration for World Models](https://arxiv.org/abs/2610.30125v1) | 2026-10-22 | 未知stationary物性由独立交互编码为descriptor并按channel提供条件，训练仍依赖same-physics分组；复用需验信息量与条件失效，视觉预测不等规划成功；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

| [Agentic World Action Models](https://arxiv.org/abs/2610.30136v1) | 2026-10-22 | WAM未来预测无显式skillreuse→code/video/action三coupled experts+trajectoryalignedprogramcuration→可执行skill与预测联合表述而非事后LLMplanner外壳；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA`，[对应章节](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |

| [Causal world models under physical parameter shifts](https://arxiv.org/abs/2610.29088v1) | 2026-10-22 | 只给OODmass可反伤预测→interventionmask/affinemassinertia-knownPD-residual结构，disjointmassrange对照 → causalinput选择与参数进入mechanism方式分开；3+1+2=6 | 深入完成 | 整合：`MULTIMODAL-WORLD-MODELS`，[对应章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [LLMs are making formal software verification feasible at a much larger scale](https://www.anthropic.com/research/formal-verification)

官方Oct22正文的Turning tests into proofs、Limitations、fn6，与[同题附录](https://www-cdn.anthropic.com/files/4zrzovbb/website/6867eadf760258fa8b42a504600cd3c036d16358.pdf)pp1–2/4–5支持以下限定结论：已有OSS-Fuzz入口编译成RISC-V binary，形式语义机械生成命题，Claude生成Rocq proof、checker验命题；这是从采样找反例到限定域证明的替代分支，不是证明整个库或现实机器绝无bug。证据权限是作者公开工程及形式化合同，未复现或核全部artifact。

附录把ASan binary no-crash、ASan/plain trace和终态等价、plain binary no-crash分成三义务。相同有限trace不足以区分crash和silent infinite loop，不能单凭等价授终止性。准确条件是小于64 MiB的输入、固定内存预算、静态单线程musl与RISC-V/Linux语义；不是小于64 MiB内存。ASan盲区、未覆盖入口与caller误用仍在证明之外。patch后重新生成spec意味着证明对象变了；作者惩罚patch并audit，仍不是原功能等价证明。

成本也没有消失：作者正文承认数亿token，附录单proof检查可需30分钟至数小时CPU；未据此推全生命周期成本或部署SLO。未采用独立协作复用比例、跨模型速度对比或其他案例。Ch80原有形式化忠实度及保留原测试义务段已覆盖成熟原则，实际缺口是上述二进制证明和三义务分解；root将两段融入前者与ITA评价器之间，保留固定测试、sanitizer、人工审查的共存边界。reader实际Source/PRE及保存后新增、完整直接两侧、末注POST通过，见[独核R1及后续POST](../_sources/daily-20261023/REVIEW.md)。其他候选不继承这一通过。

### [checkpoint-engine：V2 drafter IPC更新修正](https://github.com/MoonshotAI/checkpoint-engine/commit/0ac607299eb711cdd6b164e9eba04a7ade9cf98b)

精确commit两处worker.py变更及145–260上下文支持V2 `get_draft_model()`路径的load和使用`draft_model_config`的后处理；PR112于Oct21提出、Oct22合入，本窗是实现合入事件而非首次提出。load为两个if，post为if/elif，不能扩成任意双路径均处理、跨rank原子发布、输出正确或性能已证。PR body为null不影响精确代码可核验，未运行artifact或复现。Ch35已有源/目标转换验收，但缺实际target/draft消费者及派生状态；单段已融入LoRA转换验收与dense/delta交接之间，工程固定输入回归与旧版本退路明确不是此补丁已验证的保证。reader必要Source、实际owner、PRE及实际保存段落/直接两侧/末注POST通过，证据见[独核](../_sources/daily-20261023/REVIEW.md)与[机构源O2](../_sources/daily-20261023/ORG.md)。

### [ZCode：有界后台页面保留](https://github.com/zai-org/zcode-plugins/commit/d33f6c0ce7b011147410e3141329e2d865ec6a22)

读取精确server/automation变更、全部47行retention测试与craft-ui-validation说明。资源声明`_meta.ui.backgroundRetention`，只有实际业务任务返回`zcode/activity`；这些是宿主专有扩展，非MCP标准。文档允许回收闲置且非busy的后台页，回收丢失未保存内存；驻留、保存和工具effect必须分别验收。测试仅正任务标记与九页list/read声明，没有空poll负例或宿主回收实现；作者仅披露PhotoCraft macOS arm64/Electron44.7.0的实际验证，未覆盖其他八页完整视觉和Windows/Linux。120秒单操作上限为既有约束，不是本次新增实现。无性能数字或本项目复现。Ch83原primitives与会话生命周期段未覆盖页面保留资格，新增单段位于两者交接；reader必要Source、实际owner、PRE与实际新增/完整两侧/末注POST通过。

### [Hy-Memory：SDK唯一写入权与离线迁移](https://github.com/Tencent-Hunyuan/Hy-Memory/pull/132)

PR132/145/146及143精确contract支持SDK为唯一memory/raw authority；启动离线迁移、分歧对账、完整bundle验证与原子cutover不是普通add等价替换。prefetch禁止derived注入回灌已由Ch77现有provenance/不可变episode论证覆盖。未用测试计数认证生产全故障。 原证、精确SHA/日期与逐项范围见[ORG及必要contract](../_sources/daily-20261023/ORG.md)。root已实际保存，独立reader R23完整新增/直接两侧/本人注POST通过；未运行artifact或复现实验。

### [Qwen-code：durable context与执行边界](https://github.com/QwenLM/qwen-code/pull/15104)

PR15104 compaction candidate/PostCompact/terminal原子commit、15119/15198管理与private drain、14986可信idle预算、15069模型外schedule gate分别融入Ch75/83/84/81。15131取消ACK不等settlement由Ch84既论点承载；15053只修global-cache opt-in wire shape，未知live API规则不写成通用机制。 原证、精确SHA/日期与逐项范围见[ORG及必要contract](../_sources/daily-20261023/ORG.md)。root已实际保存，独立reader R23完整新增/直接两侧/本人注POST通过；未运行artifact或复现实验。

### [MiMo-Code：retry状态与输入重建边界](https://github.com/XiaomiMiMo/MiMo-Code/pull/2703)

PR2703 retry record跨reload保留但不送model，只有真实success清除；无限empty、重发全context和keepalive撑attempt的费用不消失。2702以最新message重建，保未答user与deferredInputs；两事件同family，分别与Ch75/84现有论证整合，不授无损任意摘要。 原证、精确SHA/日期与逐项范围见[ORG及必要contract](../_sources/daily-20261023/ORG.md)。root已实际保存，独立reader R23完整新增/直接两侧/本人注POST通过；未运行artifact或复现实验。

### [OpenAgentCore：restore前后分流与journal编码](https://github.com/MiniMax-AI/OpenAgentCore/pull/819)

PR819在native dispatch前先durable close/fence再返回checkpoint_unusable；dispatch后未知不得由此另开writer。816 native snapshot以驻留换导入导出，现Ch81已有环境联合恢复与费用；817 NUL→FFFD为有损兼容版本事实，不授byte-preserving authority，815保留workspace/历史资格限制。 原证、精确SHA/日期与逐项范围见[ORG及必要contract](../_sources/daily-20261023/ORG.md)。root已实际保存，独立reader R23完整新增/直接两侧/本人注POST通过；未运行artifact或复现实验。

### [Accelerating CPU Speculative Decoding via Unified Graph Execution and Transactional KV Isolation](https://arxiv.org/abs/2610.28671v1)

exact-v1，§2.1–2.2、4.1–4.3、AppA/C/D/F1与T8：统一arena、持续线程及scratchpad逻辑提交是CPU运行时差额；mask/position仍必要，有限KL不能证明任意采样分布或全内存安全，contention亦有反退。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-SPECULATIVE-DECODING`[原章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [SkillEval: Learning Interpretable Ability Profiles of LLMs via Cognitive Diagnosis Models](https://arxiv.org/abs/2610.28767v1)

exact-v1，§2–4、AppendixO：Q-matrix可解释profile补量尺接口，但taxonomy已见全部题文本，只有响应heldout；IRT预测、routing与shortlist不同，新域反退及missing-skill未核保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；实际差额已融入`PLATFORM-EVALUATION-SYSTEM`[原章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing](https://arxiv.org/abs/2610.28815v1)

exact-v1，§3–6及Limitations：quality/coverage选择与分级race须分账，训练/验证混合筛选、保护parent与strict empirical gain不能证明总体reward单调；池扩张同时扩执行预算。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`AGENT-WORKFLOW`[原章节](../../../../books/part-07-agent/81-workflow.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [How to Use Parallel Data for Multilingual Pretraining](https://arxiv.org/abs/2610.28838v1)

exact-v1，§2–5/Limits：同AR目标下先同窗配对后独立文档是训练条件分支；同tokens未隔离optimizer restart/rewarm，逆序部分任务更好，1.3B两语对不授普遍课程。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；实际差额已融入`TRAIN-PRETRAINING`[原章节](../../../../books/part-04-training-system/28-pretraining.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [SANE: Automated Scorer-Specific Metamorphic Testing for LLM Judges](https://arxiv.org/abs/2610.28886v1)

exact-v1，§3–6：scorer intent决定recipe关系方向，recipe/实现/applicability三效度逐一核；更大家族库存不等同调用预算更有效，三次GPT5.2预测不等三模型，人工外证只支持faithfulness排序。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；实际差额已融入`PLATFORM-EVALUATION-SYSTEM`[原章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](https://arxiv.org/abs/2610.28887v1)

exact-v1，§2–3：private history、shared实验记录和真实实验增量分配是组织差额；单run、共享首16轮及63对65–68实际eval不证明persona/UCB普遍因果，失败/拒绝与完整搜索费用保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；实际差额已融入`AGENT-MULTI-AGENT`[原章节](../../../../books/part-07-agent/82-multi-agent.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [CSD: Common-Support Distillation for Cross-Tokenizer Knowledge Transfer](https://arxiv.org/abs/2610.28895v1)

exact-v1，§3/B/C、4.1–4.5/T1–5：跨tokenizer共同文本事件、chain rule和残余质量替代仅词表交集；固定prefix的1:N与M:N不同，局部已观察支持不等全分布或任意语义等价。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[AUTHOR.md](../_sources/daily-20261023/AUTHOR.md)；实际差额已融入`TRAIN-PRETRAINING`[原章节](../../../../books/part-04-training-system/28-pretraining.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Auditing Conformal Prediction for Language Models Under Inference-Time Model Shift](https://arxiv.org/abs/2610.28937v1)

exact-v1，§3/Prop3.2、4/MaxThr、5/6及C4–5：校准身份须包含推理配置；perconfig exchangeability与latent预算拆分仍有假设，不外推开放生成事实置信度。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`PLATFORM-EVALUATION-SYSTEM`[原章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Is 2:4 Sparsity Still Worth It? Semi-Structured Sparsity versus Quantization in LLM Inference](https://arxiv.org/abs/2610.28947v1)

exact-v1，§3–6/T2/4/5：equal-bits须计index，硬件最低精度后稀疏仍有条件收益；重训PPL恢复不保证reasoning，paired4:8不能消费普通2:4产物。未采用单GEMM峰值作服务SLO。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-TENSORRT-LLM`[原章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Behavior Beyond Text: Evaluating Refusal Transfer Failure in LLM Agents](https://arxiv.org/abs/2610.28982v1)

exact-v1，§3–7：no-tool拒绝不自动传递到tool action，paired分母、call propensity和conditional unsafe分开；20predicate只判参数未执行effect，steering主要降低call且有benign/coherence代价。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`PLATFORM-SECURITY`[原章节](../../../../books/part-06-ai-infrastructure/72-security.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust](https://arxiv.org/abs/2610.28987v1)

exact-v1，§3/4、D1–2、E：不可信可读handle与精确bytes/tool endorsement副本分开；有限原子gate假设不等LLM gate正确，任务/用途/时间授权未自动绑定，未运行Lean artifact。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`AGENT-MEMORY`[原章节](../../../../books/part-07-agent/77-memory.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Attention-based Classification for Indirect Prompt Injection](https://arxiv.org/abs/2610.28988v1)

exact-v1，§3–7：合成attention sensor跨tool输入的transfer反侧要求限定输入接口；head选择依label，单tool-step AUROC不等完整workflow防护，双向focus、符号weight及协方差过拟合保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`PLATFORM-SECURITY`[原章节](../../../../books/part-06-ai-infrastructure/72-security.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Target Regeneration Shrinks the Gains of Draft-Training Objectives in Speculative Decoding](https://arxiv.org/abs/2610.29013v1)

exact-v1，§2–5/7、A1/A4：目标再生成后的CE控制收窄了draft目标的相对增量；两次训练、prompt bootstrap及MAT不等wall-time/质量，不能据此宣称KD无用。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-SPECULATIVE-DECODING`[原章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Better Policies, Worse Verifier Audits](https://arxiv.org/abs/2610.29029v1)

exact-v1，§4 identified-set/audit inversion、5–7：full-success组件AUC会随失败人口mixture反转；需自身失败支持、bin条件分布和独立刷新，不能直接诊断reward hacking。small offline-DPO不授在线LLM保证。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`PLATFORM-EVALUATION-SYSTEM`[原章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [GRAFT: Restoring the Missing Sampling Interface in Continuous Diffusion Language Models](https://arxiv.org/abs/2610.29136v1)

exact-v1，§3–5、AppA/D：连续去噪的平均候选可压低词汇尾部，早commit再regenerate是条件分支；稀有词出现不等事实正确或隐私，dose过强与额外采样费用保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[AUTHOR.md](../_sources/daily-20261023/AUTHOR.md)；实际差额已融入`MULTIMODAL-GENERATIVE-PARADIGMS`[原章节](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Correlated Failures of AI Approval Monitors](https://arxiv.org/abs/2610.29178v1)

exact-v1，§2–4/Def4/Prop5、T3–5、8：经典quorum条件不是新原创；方向化攻击家族和12LLM最坏情形失败说明投票多样性不够，engine仅覆盖实测family，记录一致不等请求合法。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`PLATFORM-SECURITY`[原章节](../../../../books/part-06-ai-infrastructure/72-security.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Resuming Vision-Language Inference across Onboard Interruptions](https://arxiv.org/abs/2610.29183v1)

exact-v1，§4–5、7/8：prefill chunk×layer frontier与checkpoint记录提交让阶段恢复有具体身份；payload/长度/checkpoint索引/checksum须核，持久存储完好前提不授任意RNG或storage故障恢复。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-REQUEST-LIFECYCLE`[原章节](../../../../books/part-05-inference-system/42-what-happens-during-inference.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Understanding Target Probability Reuse in Speculative Decoding](https://arxiv.org/abs/2610.29210v1)

exact-v1，§3/Def1、4–6、A2/D14：概率row身份是完整prefix；单轮tree-only/path-aligned/conditional-exact/单continuation内的覆盖冲突，不是所有verifier或跨轮调度的不可能定理。额外root pass及双GPU遮蔽成本保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-SPECULATIVE-DECODING`[原章节](../../../../books/part-05-inference-system/48-speculative-decoding.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Encoded but Unused: Bounding the Sources of VLM Errors](https://arxiv.org/abs/2610.29241v1)

exact-v1，§3–7、AppA/D/E：不完美probe条件下区分编码缺失与consumer未利用；有label/region/closed alternatives的条件界不等部署无label诊断，干预仍损原正确人口。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`MULTIMODAL-REPRESENTATION`[原章节](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Data Schedules and Learning Rate Schedules Should Be Designed Together](https://arxiv.org/abs/2610.29348v1)

exact-v1，§2/B/E/F、3、5：固定compute/MT tokens下只换LR即可反转数据时序排序；MT loss不等下游表现，起点、重启状态和MoE/MDR反侧保留，不采通用比例。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[AUTHOR.md](../_sources/daily-20261023/AUTHOR.md)；实际差额已融入`TRAIN-PRETRAINING`[原章节](../../../../books/part-04-training-system/28-pretraining.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Deciding Scale Placement in MXFP4 Dot Products with Integer Arithmetic](https://arxiv.org/abs/2610.29445v1)

exact-v1，§2–4、6/8：有限MXFP4 alphabet/scale与固定tree、RNE/gradual-underflow条件给scale-hoist安全band；不等实数分配律，也不认证任意FTZ/FMA/机器码或净加速。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-TENSORRT-LLM`[原章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [RISK-KV: Quality-Aware Selective KV Cache Reconstruction for Distributed LLM Inference](https://arxiv.org/abs/2610.29544v1)

exact-v1，III–VI/Eq1–12/Alg1/T1–3：exact anchors预测缺失层hidden属于有损跨层恢复；校准mean-loss置信上界不保证每请求质量，joint选择、predictor/full-cache GPU费用与exact fallback保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-KV-CACHE`[原章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [UlaCache: Unified Logical Addressing for Sparse LLM Serving](https://arxiv.org/abs/2610.29820v1)

exact-v1，§3–7：unique历史池与本地buffer副本分账、扣除非history费用，transfer完成才publish映射；各自peak batch不等same-SLO收益，batch1反退及sparse轮转全池反侧保留。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`INFER-KV-CACHE`[原章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [What the Author Wrote, What the Agent Reads: Silent Cue Loss in Enterprise Document Ingestion](https://arxiv.org/abs/2610.30026v1)

exact-v1，§3–5：文字相同也可因格式强调丢失而失去salience，原cue与派生role hint需分责；LOO/typing支持局部因果，不采用普遍AUC ceiling、扫描OCR或合规effect保证。 这是作者原始研究/受限实验，不是本项目复现。必要证据位置与反侧见[ARXIV.md](../_sources/daily-20261023/ARXIV.md)；实际差额已融入`AGENT-RAG`[原章节](../../../../books/part-07-agent/76-rag.md)的对应推理位置，保存正文、完整直接两侧及源注经非writer实际POST通过，不继承到其他候选。

### [Combining Long-Term Memory and LLMs Comes at a High Cost: From Prompt Injection to Persistent Compromise](https://arxiv.org/abs/2610.28810v1)

exact-v1，IV–VI的April–June三产品、pre5/post5协议与权限边界支持持久/跨用户注入的受限观察；共享memory需owner/admin/edit，CSRF与部分connector均失败，不称当前产品漏洞。Ch77写入source/consent、ACL与summary祖先，以及Ch72持久读取/effect已有完整承载；不为安全高分添加重复产品段。 独立必要Source与actual owner比较通过；[具体证据记录](../_sources/daily-20261023/ARXIV.md)，未运行或复现artifact。

### [Right On Q: Recovering Reasoning under Quantization via Self-Generated Trajectories](https://arxiv.org/abs/2610.29378v1)

exact-v1，§3–6与A2–7必要域：on-policy低bit prefix/teacher监督与双向KL仍受response-token matching、异prompt pool和fakequant限制，三eval seeds不是三次训练。实际Ch31 StateDistribution/PrefixOPD及Ch49低bit on-policy两段已承载相同接口和全费边界，本项作为受限新验证，不强造知识缺口。 独立必要Source与actual owner比较通过；[具体证据记录](../_sources/daily-20261023/ARXIV_STANDARD.md)，未运行或复现artifact。

### [A Small Model Asks Better: Fine-Tuning Query Clarification for Retrieval-Augmented Generation](https://arxiv.org/abs/2610.28686v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。query表面歧义可由context消除/也可retrieved-doc后才歧义 → 3900hardnegative微调区分true vs apparent ambiguity → clarification gate需前后retrieval分母与false asks，不仅给大模型prompt；局部可4分关闭不默认深审。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Building a Nested LADDER for LLM Unstructured Post-Training Pruning](https://arxiv.org/abs/2610.28773v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。uniform或一次adaptive pruning高稀疏退化 → incremental end-to-end damage/per removed parameter选择生成nested masks → allocation策略需分benign/high sparsity，非单预算最优。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [LIFT: Scoped Constraints for Evaluating and Training Instruction Following](https://arxiv.org/abs/2610.28819v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。单条可程序检查约束reward可偏离主任务 → section-scoped双类约束及main-task联合评价 → IF训练不能只优化孤立约束得分。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Flexible Language-Guided Representation Editing for Adaptive Robot Behavior](https://arxiv.org/abs/2610.28893v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。languagefeature只add过指定→add/generalize/mask三操作消融→localrepr交互可删/泛化非只追加。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [D-Skill: Distilling Teacher Knowledge through Agent Skills](https://arxiv.org/abs/2610.28914v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。黑盒student无法weight-KD → fixed paired teacher/student trace的行为divergence/agreement凝成离线skill、无追加环境/labels → transfer介质可显式而非参数，需同rollout/运行费用比较。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [T-DIG: Text-Conditioned Diversity for Image Generation](https://arxiv.org/abs/2610.29003v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。单image质量不保用户指定variationaxis→frozen generator外GRPO promptpolicy+axisreward→可加用户轴diversity但非原模型机制突破。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Does Every Instance Count Equally? Order Effects in LLM Multi-Instance Processing](https://arxiv.org/abs/2610.29057v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。多独立instance aggregate被当permutation-invariant → fixed set7order/15models发现90pp差且trace/gradient位置偏 → 多实例统计任务需order干预，不以longcontext容量保证aggregation。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Recursive Self-Improvement on a Budget: Scoring Code Edits Before They Run](https://arxiv.org/abs/2610.29121v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。scaffold edit必须昂贵运行才能选 → fixed fit96edits的parentrate+diff8coord readout，独立steering/test/archive policy → pre-execution proxy要与parent选择/最终return policy隔离，未普证通用编辑质量。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Mitigating Reward Hacking in Realistic Scenarios Through Representation Engineering](https://arxiv.org/abs/2610.29129v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。uniform steering扰coherence → dynamic intervention减少representation perturbation并crossdomain验证 → monitor/mitigate需绑定激活位置/行为代价，不授production无hacking。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [NormTune: Norm-Guided Parameter-Efficient Fine-Tuning for Reasoning-Intensive Tasks](https://arxiv.org/abs/2610.29134v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。PEFT reasoning差距被当rank必然 → update-norm under-adaptation观察与layeradaptive加强 → budget/rank之外需核actual update scale，norm关联不自动因果泛化。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Preference Is Not Permission: Personalizing the Auto-Purchase Line in Agentic Commerce](https://arxiv.org/abs/2610.29216v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。preference-fit被用作autopurchase授权代理 → roleplayed human可授权最远动作/三值输出揭own-warrant缺也提交，personal line可学但不跨域 → 偏好预测与允许commit分开；15roleplay非真实所有用户授权，局部可低分关闭。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Learning Marginal Viewpoint Utility for Budgeted Evidence Selection in RAG](https://arxiv.org/abs/2610.29234v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。固定relevance忽略selected evidence已覆盖视角 → within-state marginal viewpoint训练ranker/预算约束重score，RVC1与二来源RVC2 oracleceiling → evidence diversity要按边际/独立source预算而非高分重复。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [ER-Chord: Spatially Consistent One-Step Image Editing via Equal-Energy Reliability Redistribution](https://arxiv.org/abs/2610.29248v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。temporal稳不保spatial edit一致→equal-energy按neighbor-noise fieldagreement分配strength→同calls下局部编辑控制。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Design and Tuning of Multi-Agent Systems Using Bayesian Evolutionary Optimization](https://arxiv.org/abs/2610.29276v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。选workflow候选靠LLM或全面eval贵 → graph-awareGP+ExpectedImprovement挑evolution图 → topology search可显式uncertainty/acquisition，但仍需实测反馈。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Signals and Queries: Token-Efficient Agentic Context Discovery](https://arxiv.org/abs/2610.29326v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。每turn所有policy做LLM relevance贵 → offline hard-negative per-policy logistic filter且保高recall → policy检索first stage可局部更新且需看recall-conditioned precision。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [From Prompts to Posteriors: Can LLM Agents Perform Bayesian Inference in Context?](https://arxiv.org/abs/2610.29331v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。自然语言Bayes更新能力常由假设替代 → qualitative coherence/externally-determined posterior quantitative评估对照有无reasoning/code → 区分模型自身coherence与tool-assisted posterior approximation；采用通用belief-update能力边界，不采用科学发现应用结论。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [VideoGen Model 1: Prompt Expansion Versus Formatting in Audiovisual Generation](https://arxiv.org/abs/2610.29407v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。formatting/creative expansion收益混→30prompt固定seed/generator三arm/judge不一致→不把prompt expansion分数全归格式。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [CCG Diffusion: Combinatory Categorial Grammar-Driven Compositional and Syntactically Disambiguated Text-to-Image Generation](https://arxiv.org/abs/2610.29415v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。promptattachment含混→CCGcategory生成修改关系、rewriting/attentionguidance→局部syntaxcontrol可不训模型。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [A KAN-based Non-linear Factorization for Embedding Layer Compression](https://arxiv.org/abs/2610.29424v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。linear低秩bottleneck限制容量 → matched parameter Skipgram非线性projection+初始化 → embedding压缩不只线性rank，局部小模型证据不外推LLM。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [BlazeVGGT: 13x Faster VGGT at 2,000 Frames via Camera Token without Training](https://arxiv.org/abs/2610.29454v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。dense crossviewquadratic→cameratokenkernel/DPP选KV、全frame保query→localcontextselector可省算但需几何质量。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Omnilingual-MsASR: Benchmarking Multimodal, Multilingual, Long-Form Multi-Speaker ASR of Omni Large Language Models](https://arxiv.org/abs/2610.29455v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。Omni能力榜掩长时多speaker困难 → parallel A/V、6语言30min20speaker协议揭tcpWER失效 → 模态互补不能由短片aggregate推长时定位/说话人恢复。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Parallel Thinking for Large Language Model with Path Diversity](https://arxiv.org/abs/2610.29501v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。RL parallelpaths collapse同策略 → prefix-similarity penalty促路径区分 → parallel budget需验证多样性而非只线程/path数量，token差异不自动语义差异。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Mitigating Query Shortcuts in Chain-of-Thought with Context-Aware Decoding](https://arxiv.org/abs/2610.29518v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。answer不依赖CoT rationale → contrastive with/without rationale及groundtruth/random干预 → shortcut缓解需看行为依赖，不只答对率。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [RCSD: Reinforcement and Continual Learning for Domain-Specific Speculative Decoding](https://arxiv.org/abs/2610.29527v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。soft-KD拟合高entropy未对acceptance优化 → inference accept/reject隐式preference+masked loss → draft学习目标可直接来自验证反馈。与29013共同检查regeneration混杂，不预合并结论。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [SPARE: Sparsity Allocation via Routing Entropy for Efficient MoEs](https://arxiv.org/abs/2610.29662v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。expert selector与layer删除数量常混同 → fixedselector/budget、routing-entropy分配及random-pruning bound/干预 → 分清删谁与每层删多少，concentrated route更脆弱。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Scaling Multilingual Pretraining of Pixel Language Models](https://arxiv.org/abs/2610.29681v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。pixel模型跨script transfer被默认随规模增强 → fixed per-language compute、多语言/script/容量分轴发现unseen script transfer不再随scale增 → 区分本地收益/跨script收益。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Accept or Repair: Preserving Passage-Supported Answers in Contrastive Decoding](https://arxiv.org/abs/2610.29727v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。全程contrastive可破坏原本supported答案 → sampled答案先support-check再最多2次repair并reject context-free重复 → 将干预限于证据不支持答案。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Bridging Foundational and Agentic Capabilities of LLMs](https://arxiv.org/abs/2610.29751v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。foundational profile被视agent预测代理 → operation profile残差/realization gap增预测信息 → 分清基础能力低和执行部署失败。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29792v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。interleaved RAG历史reasoning引query drift → search momentum诊断及保留knowledge/refined-state、complementary parallel queries → reasoning轨迹需独立于evidence保留策略。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Every Part Has Its Role: Part-of-Speech Effects in LLM Post-Training](https://arxiv.org/abs/2610.29843v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。concept augmentation泛化被当统一 → noun/verb/adj消融揭downstream与representation变化不一致 → 数据增广收益依concept位置和评价，CKA变化不代行为改善。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [PAUSE: Search-Free Steering of Coding Agents Before Their First Source-Code Edit](https://arxiv.org/abs/2610.29870v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。周期review或anomalytrigger贵/正常也错 → 首sourceedit前一次planner介入保持executorcontext/workspace，对同cost advisor比较 → intervention checkpoint可用effect边界而非周期，全部planner费另计。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Unintended Side Effects of Value Training in LLMs](https://arxiv.org/abs/2610.29922v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。对单价值微调被当局部行为改变 → 4模型cross-value/risk/social/safety的非目标副作用 → alignment回归测试不能只测目标value。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [TIDE: Tree-Induced Fine-Grained Diagnostic Evaluation from Model Behaviors](https://arxiv.org/abs/2610.29985v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。aggregates遮capability contrast → LLM提出/分类split、行为information-gain选树 → taxonomy应由model行为辨别而非只人工主题；局部诊断不默认5分以上。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [HGM-Dual: Lineage-Aware Guided Agent Harness Optimization for Long-Horizon Planning](https://arxiv.org/abs/2610.30042v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。coding优化能力可自迁到planning被暗设 → ancestor edit-outcome lineage attribution+general/specialized errorconditioned children → planning harness优化需归因具体constraint违例而非仅大档案。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Looped Uniform Diffusion Language Models](https://arxiv.org/abs/2610.30066v1)

精确v1身份与Oct22官方公告关联已核，完整题摘及三维评分经独立校准。uniform corruption训练比mask昂贵 → objective/sampler不变iso-FLOP selective looping+loop-count sampling → 效率提升需区分训练共享与denoise NFE。。这是一项已准入但0～4分的局部增量，未据摘要确认全部实验；完成身份/日期/重复关系和关闭判断，不采为长期普遍结论、不写Books。原题摘和逐项评分/日证见[ARXIV](../_sources/daily-20261023/ARXIV.md)。

### [Is Refusal Direction Universal across Low-Resourced Languages?](https://arxiv.org/abs/2610.28897v1)

exact-v1，§4–8与AppD：source/target语言和层位置分开，剩余headroom校正避免把已近不拒答上限当成功迁移。WildGuard只判拒答、邻近语言辅助不等母语核验；单模型和bootstrap既有judgment不授跨语安全。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [TrainBridge: Agentic NPU Training Optimization Guided by GPU Compilation Evidence](https://arxiv.org/abs/2610.29171v1)

exact-v1，§2.4/3/4/6：成熟GPU的eager→compiled差异给异构后端优化意图，目标仍须核同类低效并重新profile。相同12h/port的有限单节点比较不认证任意训练语义；trainingtime排tuning，全部迁移/编译/搜索费保留。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Let Agents Design How They Search: Automatic Interface Optimization for Agentic Search](https://arxiv.org/abs/2610.29250v1)

exact-v1，§2–3/Limits：固定corpus/model，联合改预存artifact、可执行tool和instruction，再冻结候选交heldout queries；部分子域prompt-only更好，联删非单项因果。所报tooltime不含model或离线10轮优化，未授freshness/事实/工具权限。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Hierarchical Masked Diffusion Language Models](https://arxiv.org/abs/2610.29255v1)

exact-v1，§4/Eq5–12、5/6：层级与token联合mask/reveal，每轮先level后token形成软顺序，中间状态仅两pass之间；两次串行forward/标签和较长训练有代价，较低genPPL仍可MAUVE退步。不采全NELBO或加速保证。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Reader--Writer Coupling in Transformer MLPs](https://arxiv.org/abs/2610.29340v1)

exact-v1，§3–6/AppH：effective reader包含activation/normalization Jacobian，单侧配对不同于共同permutation；局部负符号不保证I+J全局收缩，重配也改谱形，损失关联仅条件证据，不批准剪枝或事实编辑。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Don't Stop Long-Context Continual Pre-Training Too Early: An Empirical Scaling Law](https://arxiv.org/abs/2610.29352v1)

exact-v1，§3–5/AppA：短/长tokens分账，constant训练raw轨迹与Last4平均评价分开；reference选择LongPPL、有限范围负offset不能作渐近law。128K扩展/下游额外训练不免费，短文饱和不授长窗停止或无限续训。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [A Strong MoE Is All You Need for Process Supervision](https://arxiv.org/abs/2610.29498v1)

exact-v1，§3–6/B/C/E/F：native routing selected-expert mass可作posthoc修复位置和PRM标签proxy，但整轨归一非online校准正确率。三轮修复与随机同round不等token/walltime，teacher/router replay/PRM及重生全费保留。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States](https://arxiv.org/abs/2610.29545v1)

exact-v1，§3–8必要域：周期性舍入、buffer与scale轴/head位宽共同选择，比较resident state+scale/zero+buffer。更长周期非质量单调、不修prefill损伤，BF16 buffer主导部分吞吐收益，不全归INT4或混合配置。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization](https://arxiv.org/abs/2610.29671v1)

exact-v1，§3–5/C1/F1：同shared manager交替训练需固定bank的检索组，有标签Index-answerer可答proxy也失败时从组统计与loss同时排⊥；lineage扩credit并非相同state反事实或真实因果。多bank、标签、answerer/judge与SFT检索全费保留。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration of LLMs](https://arxiv.org/abs/2610.29832v1)

exact-v1，§3–6/B1–5：prompt-specific语义类likelihood可微辅助SFT，但Dirichlet strength固定N+类数，缺gold另teacherforce已经混合监督。类oracle非真值；sampler/聚类/训练费、部分recipe口径和physics-hint域变更均保，不采科学领域正面结论。 root已按准许单段实际保存，非writer完整新增/直接两侧/本人注POST通过。 必要原文位置与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Scan or Index? large Evidence Coverage, Answer Quality, and Cost in Long-Document RAG](https://arxiv.org/abs/2610.28957v1)

exact-v1，§2–4：known-document扫描见过全库仍可在reduction/packing丢决定证据，EC按all-assigned与AA按completed不能混分母，prepare摊销不等所有GPU/美元成本。Ch76 persistent corpus和Ch66 RAG receipt/required-information已具体承载检索→装配→answer分责与费用，保局部新验证而不堆重复段。 必要Source与具体owner/处置经独立reader通过，无新增Books写入。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [MOSAIC: An Omni-Modal Benchmark for Long-Term Memory and Cross-Modal Reasoning in Conversational Agents](https://arxiv.org/abs/2610.29249v1)

exact-v1，§5/6.1/8/AppG：固定reader/prompt/budget的表示/取回/交付干预定位阶段，gold evidence后残余不是纯reader能力因果；audio/video null不等无损。Ch66阶段receipt与Ch77 query充分性、来源保留已承载该接口，实际NC通过。 必要Source与具体owner/处置经独立reader通过，无新增Books写入。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Credit Where Credit Is Due: Contrastive Attribution Topology Search for Multi-Agent Systems](https://arxiv.org/abs/2610.29292v1)

exact-v1，§2–4/6：trace nodecredit再均分incoming edges指导supergraph剪枝，scoreonly没有新调参因果责任；54%预算比不含全部生命周期，安全只固定poisonpool。现Ch82 graph/protocol/全费与credit边界已在，不以新启发式强写书。 必要Source与具体owner/处置经独立reader通过，无新增Books写入。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Beyond Binary Labels: Diagnostic Evaluation of LLM Safety with Prompt-Level Rubrics](https://arxiv.org/abs/2610.29225v1)

exact-v1，§3.1/4.2/T3–4/7及Oct22两README精确patch：236人工人口的89.41/90.25/95.34%不能说全部>93%，93.33–94.78%是judge间一致率。README93→89为统计宣传纠错、非新实验；与机构事件只计一个family，不写成通用安全保证。 必要Source与具体owner/处置经独立reader通过，无新增Books写入。 必要原文位置与直接反侧见[MODEL_SOURCE.md](../_sources/daily-20261023/MODEL_SOURCE.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [Graph Topology Meets Energy-Driven Pathfinding: Preserving Contextual Consistency in Retrieval-Augmented Generation](https://arxiv.org/abs/2610.29933v1)

exact-v1，§3–4/D/E：原文span/docID节点、PPR/prune/BFS和文内offset linearize只是导航→原文支持分工的局部实现；construction0只LLM tokens，silver训练/embedding/索引非零，预算仍可丢桥。Ch76 GraphRAG/Relink/bridge与semantic贡献分离、source locator和证据DAG已有完整覆盖。 必要Source与具体owner/处置经独立reader通过，无新增Books写入。 必要原文位置与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact，不推全部附件已审或生产保证。

### [ReAPO: Retry-Aware Policy Optimization for Efficient Exploration in LLM Reasoning](https://arxiv.org/abs/2610.28770v1)

exact-v1，§3–4/限制：可信失败后的serial retry与attempt自身advantage更新分开，成功不回标旧失败span；总tokens共享、finiteK/归一偏差及first-response评价保留，SCoReStage2不是完整SCoRe，GPQA/K3有反侧，不授最短路径无偏梯度。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact。

### [How Much Gradient Does Truncated Backprop Lose in Looped Transformers?](https://arxiv.org/abs/2610.28871v1)

exact-v1，§2/4–5/7：冻结checkpoint的lost-gradient norm只诊断当前截断，不直接预测Adam适应后的质量；per-sequence/batch-clip/loop-only不同、固定steps非compute、LR仅fullBP选择与两小模型低power保留，不推普遍proxy无用。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact。

### [One Act, Many Masks: Effect-Marginal Policy Optimization for Long-Horizon Agents](https://arxiv.org/abs/2610.29427v1)

exact-v1，§4–5/B/C1/D：保原advantage而在valid/nontruncated同context/effect cells共享长度归一ratio是独立耦合轴；实际有限cell/PPO是surrogate，tokenweighted协方差差额不等完整effect-policy identity，WebShop仅有限覆盖，不推全费加速。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact。

### [ECHO: Emergent Common-Mode Hidden Offsets Drive Vocabulary Collapse in Preference Optimization](https://arxiv.org/abs/2610.29410v1)

exact-v1，§3–8及B16反侧：score共同shift不变不等hidden shift精确抵消；b/r分解、注入/随机正交对照支持vocab well局部通路，但norm/方向/basegap不同。低demand DPO不崩、residual仍能成well，完成run事后信号不是在线阈值或全家族修复。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [DynaWeave: Learning to Adapt through Dynamic Scenario Synthesis](https://arxiv.org/abs/2610.29443v1)

exact-v1，§3/4/结论：只实际发生的外生event按顺序改受影响verifier check，未触发/未影响要求仍保；资源不可用不授权取消目标。event-off对齐旧verifier与局部旧解/适配解control不证明完备，virtualtime非真实wallclock，coverage/steps联变不当单因果。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications](https://arxiv.org/abs/2610.29767v1)

exact-v1，§3–4/Limits：同一rename可改变隐藏精确name合同，name-based掉分不直接识别memorization；双向行为checker仍受有限cfg/60映射/仅safety限制，CI跨零非没有记忆，新名字/截断成本和单splitseed保留。旧260212413两段完整保留后再融入，不以新反证覆盖旧结果。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [Remembering Through Change: Provenance-Preserving Hypergraph Memory for Multimodal Agents](https://arxiv.org/abs/2610.29995v1)

exact-v1，§3–4.4：独立mentions、候选同指称、逐state source facts与原图回读分开；typed超边存在不证明实体或演进真值。累计加层、检索budget变化和judge非人审不授唯因果或生命周期省费，原episode/冲突与权限保留。 root实际原段保存、非writer完整新增/直接两侧/本人源注POST通过。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents](https://arxiv.org/abs/2610.29965v1)

exact-v1，§3–5：protected-objective单约束投影沿用A-GEM，先累积再投影、raw一阶下降非Adam位移，direction/gate/λ联合可反退。Ch28同参数仲裁、GridUMM与optimizer后投影已具体承载；one trainseed/四decode passes、WebShop500对引用128不能拼同条件优势，保局部新验证不重复改书。 必要原证与具体owner/处置经独立reader通过，无新增Books写入。 必要证据位置、评价协议与直接反侧见[ARXIV_STANDARD.md](../_sources/daily-20261023/ARXIV_STANDARD.md)；未运行或复现artifact。

### [Retrieval Augmented Generation Compositionality](https://arxiv.org/abs/2610.29722v1)

exact-v1，§3–6/D10/C2–3：planned242实际167、不同query人口、faithfulness有不负向组合反侧；focused交互效应未达预设阈值，query数/提示长度/构造corpus不支持原全面大效应。Ch66完整pipeline/阶段receipt与Ch76耦合已承载不拼单组件最优原则，无新可采用通用阈值/配方，保重要负证不强造diff。 必要原证与具体owner/处置经独立reader通过，无新增Books写入。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [MemoryTax: The Bitter Lesson of Agent Memory](https://arxiv.org/abs/2610.29823v1)

exact-v1，§2–6：单会话单run、photo输入不齐，去photo人口仅窄差，writer/reader交换仍混算法；judge/价格/cache与crossover是特定投影，不证明memory普遍无用。Ch77 VideoEMem具体write/read/content与构建/查询全费边界已承载该有限反证。 必要原证与具体owner/处置经独立reader通过，无新增Books写入。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [Keeping Time vs. Understanding Time: Neither Alone Explains Temporal Reasoning in LLMs](https://arxiv.org/abs/2610.29507v1)

exact-v1，§3–4/限制：temporal标签/AUC不等独立latent能力，四mode训练转移弱仍有32B正反侧，8/16rollout与格式reward不构成纯因果消融。现Books未把该两benchmark分类写成独立可训练能力；保有限负面结果，不升为时间推理全由知识。 必要原证与具体owner/处置经独立reader通过，无新增Books写入。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [Environment Duels: A Microcosm of LLM Co-Evolution](https://arxiv.org/abs/2610.30116v1)

exact-v1，§2–4：author计划不等可信可执行reference，hintlift是修好减破坏，零可抵消；四author单learner的RL关联与native harness不授稳定跨模型选teacher规则。Ch66生成器人口/来源与reference/零通过义务已有，不新增重复通则。 必要原证与具体owner/处置经独立reader通过，无新增Books写入。 必要证据位置、评价协议与直接反侧见[SOURCE_MODEL2.md](../_sources/daily-20261023/SOURCE_MODEL2.md)；未运行或复现artifact。

### [Events, Not Pixels: Where World Models Get the Return Wrong](https://arxiv.org/abs/2610.29435v1)

exact-v1，§3–8/T1–3：相同初态/动作的真实和想象轨迹以完整相邻帧对替换，event相对等量random的增量才解释定向性，detector/邻域及all-real残差限定归因；真实未来是离线特权，非重生成后续轨迹或在线修复。Non-event/自身rewardhead反侧、MSE与diffusion预算不同和同diffusion确定性loss仍有效均保留，不采普遍比例或随机性必要。 root准备后由非作者reader直接回官方HTML核必要原证、actual owner与PRE；R1采修正的原三合同段后/RepairMetric前，R2采原SF28286完整两段后/少数反证前。root已真实保存，reader完整新增/两侧/本人注POST通过；[必要证据与推导边界](../_sources/daily-20261023/ROOT_SOURCE.md)。未运行或复现artifact，不把有限已知合同变为现实全域保证。

### [Parallel AI Agent Collaboration as Graph-Structured Distributed Block Optimization](https://arxiv.org/abs/2610.30074v1)

exact-v1，§2–3 gain-retention两定理及完整证明、4条件和5/6直接反侧：有限block/精确F与完整依赖使独立集gain可加，非负gain结合fractional cover给1/Λ，普通coloring是1/κ；不采global收敛/最优调度。漏边破证、多边降并行、tightbudget验证费可反退、heldout三轮均未完整解题，adaptiveordinary可达相同gain；route锁与诱导C5不替任意集群时间保证。 root准备后由非作者reader直接回官方HTML核必要原证、actual owner与PRE；R1采修正的原三合同段后/RepairMetric前，R2采原SF28286完整两段后/少数反证前。root已真实保存，reader完整新增/两侧/本人注POST通过；[必要证据与推导边界](../_sources/daily-20261023/ROOT_SOURCE.md)。未运行或复现artifact，不把有限已知合同变为现实全域保证。

### [SimHack: Predicting the onset of detectable reward hacking before RL training](https://arxiv.org/abs/2610.28707v1)

exact-v1，logit-offset/momentum模拟相同漏洞环境下recipe的有限t50分布，未发生者以horizon截断，不识别潜伏作弊或给因果β。Reference训练、初始探测、fit、全部模拟与真实复核付费。Ch31更新方向漂移后融入开跑前相对风险proposal，不授detector/quality/提交权。 root已按准许原段实际保存，非writer完整新增/直接两侧/本人注POST通过。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [An Explicit Feedback Contract for Iterative ML-Agent Harnesses](https://arxiv.org/abs/2610.28798v1)

exact-v1，标签隐藏后仍限制validation反馈：accepted-update与有限精度bestscore分责。实际paired-SE是heuristic，与fixed-margin保证的桥未闭，不采普遍adaptivevalidity；三real seeds微增不证明新模型更好，保旁路/独立单位和全费。Ch66隔离成本整段后增加反馈输出通道。 root已按准许原段实际保存，非writer完整新增/直接两侧/本人注POST通过。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [A Mechanistic Study of Automated Failure Attribution in LLM-based Agentic Systems](https://arxiv.org/abs/2610.28811v1)

exact-v1，probe与locator/writer grafting分开测，GT用于校准，inference无GT不等无监督制备。七小模型/单failure标签与有限head选择不证明完整因果或真知识；grafting非各row全优。Ch5表示可读≠可用与Ch31具体读出、实际注入及非目标回归已承载此选择，不重复改书。 必要原证及具体owner的已有覆盖决定经独立reader通过，无新增Books写入。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning](https://arxiv.org/abs/2610.28785v1)

exact-v1，PDF必要p1–9/15–21：固定G前把任务mean工作后验和group相关性分开选题；共享浓度且p已知时排序仍同p(1−p)，非退化组不等有益梯度。旧bank只初始化且成本不被新rollout降幅免除；多eval seeds非训练重复，Discord只固定terminal比较curtailment。Ch33动态G后融入采前题分配。 root已按准许原段实际保存，非writer完整新增/直接两侧/本人注POST通过。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [Transformers as Generic Deep Neural Networks: Exact Compilation, the Cost of Removing Activation-Activation Products, and Multi-Agent Attention Clustering](https://arxiv.org/abs/2610.28958v1)

exact-v1，strict/Hadamard/extended定义与必要rank证明：分开自由Score/Mix的unary下界不是融合全模型或时延下界，sourcegraph无addedwork不等kernelparity。FP64误差不授BF16bitwise；PTQ12/8bit不同，tail条件均值有完整观测等假设，精确tau仍付dense费。Ch49图首段后增加primitive权限前置条件。 root已按准许原段实际保存，非writer完整新增/直接两侧/本人注POST通过。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next](https://arxiv.org/abs/2610.28998v1)

exact-v1，PinnedArena、worldsize1 expertgrad累计、8layer受控梯与checkpoint：7.4x同条件和48layer改CP/batch/bin的10.4x不可混。前台32.3s返回不等后台132.5s完成，短期KL不授SWE质量。Ch39 working-set/BackwardDone→BufferFree/累积版本及Ch35 logicaltensor/IOlayout/pendingcompletion已覆盖具体选择，局部arena实现留报告。 必要原证及具体owner的已有覆盖决定经独立reader通过，无新增Books写入。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [Conditional Flow Models Convert Epistemic Uncertainty into Apparent Aleatoric Variance](https://arxiv.org/abs/2610.29172v1)

exact-v1，conditioning欠拟合把邻域mean差混入spread。共同density-weighted核、独立共同base、正性/唯一性与stationary/reversible/PSD条件下的界仅condition平均，不授任意NN、每输入或coverage保证。非Sci OGBench/PushT和synthetic反侧保留，样本variance不等可靠epistemic。Ch24 meanvelocity后增加拟合噪声区分。 root已按准许原段实际保存，非writer完整新增/直接两侧/本人注POST通过。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [Flat-RLVR: Sharpness-Aware Reinforcement Learning with Verifiable Rewards for Reasoning Capacity in LLMs](https://arxiv.org/abs/2610.29281v1)

exact-v1，固定rollout周期SAM改变更新几何；更频繁可高k增而pass1退，naiveSAM准确率大退。局部sequence-unclipped分析不授实际token/clipping，AppD重构扰动仅有条件O(rho²)近似，不签精确restore或免费反传。Ch33 RewardingRare反侧后融入更新几何替代，非另改reward。 root已按准许原段实际保存，非writer完整新增/直接两侧/本人注POST通过。 [完整必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL3.md)；未核完整artifact或复现。

### [JUICE: Unified Multimodal Modeling in Pretrained Representation Spaces](https://arxiv.org/abs/2610.28801v1)

exact-v1，独立noiselevel与同状态双流更新须joint/conditional训练覆盖内部/边界。Maze image-first仍胜coupled，连续文本措辞退，backbonecall不含全部编解码费；Ch24共同去噪后融入不同模态联合/串行取舍。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State](https://arxiv.org/abs/2610.28827v1)

exact-v1，语义/几何双前沿与可重编译record分开，sharededge/revision阻旧结果覆盖新edit，单对象编辑须状态提升。没有学未知物理，record可增长，backend readiness排browser安装，80请求不证完整edit–evict–revisit；Ch25可执行机制完整边界后融入。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [DualHeads: Reward-tilted few-step diffusion made simple](https://arxiv.org/abs/2610.28858v1)

exact-v1，双head有条件KL解释仅noised recomputedprediction，不是endpoint或真实reward；换reference池可伤GenEval，交替训练非最优固定头保证，全参考/rollout/训练费保。Ch24 TDM后融入反馈接口。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [Pair-Free Coarse-to-Real Video Generation via Real-to-Coarse Image Supervision](https://arxiv.org/abs/2610.28954v1)

exact-v1，图像pair→逐帧pseudo-video仍非无配对。feature→RGB→同encoder重编码限定部署可见性，仅定性bottleneck不证泄漏清零；jitter/域差/急运动改节奏和全制备费用保。Ch24锚点制备成本后融入。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [Cache Locally, Recompute Selectively for Streaming Video Understanding](https://arxiv.org/abs/2610.29229v1)

exact-v1，idle短window后query选择共同P重prefill，只替S^l交P，不新增整套P/恢复exact历史。CPU保visualtokens及全传输/选择费；总费降可伴TTFT升，调window/7B范围不授SLO。Ch45 causalrepair成本段后融入。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [Think-Capture: Active 3D Geometry Acquisition for Spatial Reasoning in Vision-Language Models](https://arxiv.org/abs/2610.29232v1)

exact-v1，四frame dense估计后target-dependent压缩，disagreement只是固定模型相对标签，不是geometry真值；累积消融不隔离因果，152GPUh与21.8s异步不授实时。Ch23主动取证、可靠性/标签及几何观测标定/原视图fallback已具体承载。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [AdvFidelity: Unifying Preference Alignment and Few-Step Image Generation within Reinforcement Learning](https://arxiv.org/abs/2610.29380v1)

exact-v1，同reference加噪重建负例减少内容捷径，不证内容不变/真保真，crop读CLS非patch真值。已对齐参考费用不能免，三次judge重判非训练重复；Ch24 Expert后融入配对条件。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [LiveAct: Towards Real-Time Multi-Agent World Models with Heterogeneous Action Interfaces](https://arxiv.org/abs/2610.29408v1)

exact-v1，query软调制绑定接收者，KV逐dimension保存schema/同步值；Gate非mask，inverse-model swap归因非实际动作真值。DMD机器人控制反退、单FPS非deadline，全训练/解码费保；Ch25固定slot后融入。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL.md)；未核完整artifact或复现。

### [Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers](https://arxiv.org/abs/2610.29441v1)

exact-v1，单cell probe经sparsewindow终端误差校跨步gain并用latencytable分密度。叠加可分仍近似，特殊估计目标最优不授任意预算/真实误差；cutoff替native阈值，offline全费保。Ch24敏感prior完整反侧后融入。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [Melange: A Synthetic Visual Bias Benchmark for Multi-modal Large Language Models](https://arxiv.org/abs/2610.29537v1)

exact-v1，歧义题全Unknown率不等公平；只7代表model forced-two-way不能排全23model视觉混杂。T2/T3同model数值无连接协议，不拼精确因果净差。Ch66逐item方向、target/cue/null/order与构念/行为分验已覆盖，留新数据及限制于报告。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [Generalized CycleGRPO for Fine-Grained Multimodal Understanding and Grounding](https://arxiv.org/abs/2610.29552v1)

exact-v1，当前§3–6明确继承2607.11581 image cycle，本窗只video/spatiotemporal及DOVE新增。嵌套caption→region一致性不是语义真值；anti-timestamp、弱localizer、N×K成本与原能力反退保。DOVE529有probe区间及groupbootstrap不冒独立1223题，Ch23时间边界后融入重复事件识别。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [Unlocking Spatial Grounding in Flow-Matching Models via SNR Tuning](https://arxiv.org/abs/2610.29581v1)

exact-v1，固定模型与监督只换训练噪声支持能改善布局，非推理schedule免训练修复。最佳偏移随输入几何变化、颜色纹理退，VAE/GT detector仅经验参照非硬上界；跨encoder/VAE不能只归架构。Ch24在线分箱反侧后融入结构改动前的训练支持检验。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [CineEvolve: An Agentic Self-Evolution Framework for Cinematic Multi-Shot Video Generation](https://arxiv.org/abs/2610.29590v1)

exact-v1，parent不优候选正advantage截零，再以当前evaluator固定校准输入均值抬中心并有限混合；非跨代真值、同源critic错仍穿guard。全部teacher筛选、失败候选/校准/训练费保。Ch33 sample-relative后融入劣质整组保护，不采用电影workflow组合为新长期机制。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [Rethinking Post-hoc Debiasing of Large Pretrained Models](https://arxiv.org/abs/2610.29688v1)

exact-v1，正确bias描述仍不足，改以class-conditioned固定imagepairs训map是替代，不是无监督bias真值。986被选pair局部94.8%不授新域，class标签/validation与全部选对、训练、群体回归费保；Ch23完整SAE反侧后融入。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [Compositionality with Primitives: A Unified View from Euclidean to Hyperbolic Vision-Language Models](https://arxiv.org/abs/2610.29811v1)

exact-v1，seen primitive标签与factorized读出不证真实AND/全新concept，UTZ与whitening强反侧阻所有primitive更优结论；whitening改全geometry非variance唯一因果。Ch23分解读出及modifier完整段已具体承载，保条件几何新证据不增同义段。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [How Do DiTs Denoise? An Aggregator-Predictor View of Attention and MLPs](https://arxiv.org/abs/2610.29854v1)

exact-v1，GMRF图半径局部性/共同独立噪声等假设限定理论，bounded-noise单调不能全噪声推广。Empirical充分aggregation非population真prior，singlebranch不授residual全网分离；单seed64²/联合移植与全费保。Ch24图视频整体修正后融入aggregator/predictor条件分解。 root原PRE实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL2.md)；未核完整artifact或复现。

### [GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal Gradient Accumulation and Projection](https://arxiv.org/abs/2610.29355v1)

exact-v1，逐token routed leader只以旧outputgradient基按门控/强度削follower分量，本步先投影再更新leader-only FIFO。独核修正原PRE的始终完全投影措辞，alpha/warmup不授全正交；AppB线性SGD近似不担保AdamW全训练/防collapse。Ch21 SD-MoE后融入peer更新耦合替代，全历史/投影/评价费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [Parallelizable Probabilistic Latent Reasoning for Diverse Reasoning Trajectories](https://arxiv.org/abs/2610.29385v1)

exact-v1，exact-v1 posterior读CoT并行给目标、prior teacherforce联合学，部署仍AR；实际Eq27含stopgrad balance/dispersion/均值VISReg，非未改动ELBO。M2 TV覆盖较高却hit较低、有限HiddenBranch与全制备/训练费保；Ch29训练code后融入连续目标分布监督。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [BIRD-RL: Scaling Agentic Reinforcement Learning over Stateful Data-Centric Environments](https://arxiv.org/abs/2610.29426v1)

exact-v1，stabletrajectory→worker/DB registry整轨持有、结束释放、lazyreset；12.8x只是online lifecycle I/O且排69GiB建池，非peakmemory/端到端吞吐。Timeout伪码不证明在途SQL物理静默。Ch84 Workspace run/state/effect和回收完整链、Ch33资源失败不默作zero已具体覆盖，保局部实现与纠偏于报告。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [Harness Scaling for Generalizable Agentic Reinforcement Learning](https://arxiv.org/abs/2610.29458v1)

exact-v1，5因素低阶18配置与近邻successive updates组织训练人口，pair平衡非高阶或信息等价；主测18heldout非225全组合，Full243含测试只stress。Context/segment继承原group，matchedsteps非全费，base小退保。Ch84 model/harness共同演进反侧后融入训练配置人口。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [Stochastic Pruning of the DPO Computation Graph: 1.4x Faster Training and Lower Peak Memory](https://arxiv.org/abs/2610.29538v1)

exact-v1，head选位置/suffix不执行/branch不反传省不同图。Positionmean无偏不等pairloss无偏，prefix改目标；独立正概率branch的1/q仅恢复既定mask/prefix当前梯度，非Adam轨迹/质量。93.3%memory收益来自全监督head实现，质量小退与全部双侧forward/reference费保。Ch34复杂度后融入。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability](https://arxiv.org/abs/2610.29734v1)

exact-v1，PDF必要p1–10/15/21/23/33–36：沿原Anwar MI作lower-tail独立修复，以固定CoT的conditional output软约束限制私人重编码，不只marginal行为。token/clipped与MBPP另sequence-ratio实现分开，crossedCoT支持replacement非同坏行为revelation；SORRY反退/ownanswer非truth/长度与全矩阵评分费保。Ch72原MI后融入，不重定义到Ch31。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [Your Benchmark Is an Empirical Measure Over Difficulty](https://arxiv.org/abs/2610.29927v1)

exact-v1，用途difficultymeasure失配与题库support gap不同；固定z/n/独立Bernoulli下空区间改善可完全不可辨，再多重复不补支持。W1 Lipschitz与maxgap渐近定理不授未知轴/aggregate有限必检；empiricalmidpoint/minmax、panel估计/新题validity与全部响应拟合/人审费保。Ch66 IRT审题后/WILD前融入。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [FrontierCS 2: A Benchmark for Computer Science R&D](https://arxiv.org/abs/2610.29932v1)

exact-v1，workingrepo任务中平均quality/速度更好仍可能两个clip失败，everymetric×heldout合取不同于均值。Agent自己finalnomination、one run/model+harness、GPUhours是预算非实费、未完成置零构造单调曲线。Ch66 typedoutcomes/聚合、Cornetto全条件和harness隐藏test/最终提名已具体承载，不再添通则。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL4.md)；未核完整artifact或复现。

### [Real2Sem2Real: 3D Semantic Augmentations for Robot Learning from a Single Human RGB Demonstration](https://arxiv.org/abs/2610.28880v1)

exact-v1，单RGB仍需扫描/metricheight/相机设置；两对象semanticcousin+功能面加权配准支持局部数据扩充，kinematic与contact模拟分开。不同示范、人时、训练步/coverage不是等预算因果；真机限定任务，Ch26 semanticcousin及ShapeGen共同观察/动作变换与sim/real边界已具体覆盖。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [inr2action: Encoding Robot Episodes as Neural Implicit Representations for Recall and Action](https://arxiv.org/abs/2610.28882v1)

exact-v1，从共同MAML origin逐episode离线500步拟INR delta再56tokens读出，非在线写共享policy。16000cuts不冒16000独立源episode，closedchoice双NLL和cut末单点BC非闭环，固定参数不授无限历史保真/写入恒费。Ch77共享weights段后补独立artifact参数记忆的反向边界，全元训练/拟合/读出费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [SimPT: An Automated Simulation Framework for Intervention-Based VLA Post-Training](https://arxiv.org/abs/2610.29161v1)

exact-v1，受检阶段图+privileged完整simstate在失败后晚阶段expert恢复，不是现实undo。静态21/21非状态语义证明，同seed独立采集非同失败paired，FlowPRO退步与CF-LPF只离线反侧保。Ch26旧HIL→TIDE→SimPT→参数搜索顺序实存，保失败恢复/expert与全部后训练费。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [How Representational Priors Shape Generalization in World Action Models](https://arxiv.org/abs/2610.29168v1)

exact-v1，40clean/rank39只是样本span，九backbone正交能量与表现相关不识pretrainingobjective因果。各checkpoint重拟basis/variance，IDvariance13.4x使标准化位移下降不等raw nuisance必缩。Ch26原encoderprior/ID-OOD/目标竞争与actionoutcome义务未受推翻，新有限相关保报告。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [NavBind: Diagnosing Instruction-Action Binding at Route Forks in Navigation VLAs](https://arxiv.org/abs/2610.29203v1)

exact-v1，exact-v1 fixedrow合法双branch suffix干预，行为SameSeq与固定reference fullvocab NLL另验，四action重归一KL不同。Native horizon/采样混杂、Both+25%只符号假设、matchingGT attribution联换target及SR人口不同保，不把高goal success当遵令证明。Ch26VLA定义后融入直接语言绑定验收。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [DepState-JEPA: Learning Depth-Grounded State Representation for Visual Perception and Manipulation](https://arxiv.org/abs/2610.29246v1)

exact-v1，metric RGBD shared/private与固定private decoder、recorded-vs-recursive proprio是不同协议；FK只是knownchain，60s机器人执行排inference。Ch23现shared/private职责及Ch25可预测接口/rawfact边界具体足够，不冒书已含此方法fixedprivate细节；保局部实现/全费不增同义框架。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [Training in Deployment: Human-in-the-loop Online Post-Training for Robot Manipulation](https://arxiv.org/abs/2610.29264v1)

exact-v1，manual-success筛选、纯来源50step标签与mixed排除的provenance SFT无critic不等无人监督；HIL清旧队列、episode固定generation、边界采用。FixedPolicy最终相近，availability不等质量/稳定学习；全部失败采集/人时/全模型训练费保。Ch26 HIL后/TIDE→SimPT顺序实存。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [Relational Geometry Forcing for World Action Models](https://arxiv.org/abs/2610.29282v1)

exact-v1，video帧内/跨视图及action32时刻匹配geometry cosine关系，不授metric/contact/动作因果。Pointwise退步只有-.05/-.15/-.05pp且无重训方差，监督强度未梯度预算匹配；部分关系组合也退。Ch26geometry/motor后增加不同维表示关系迁移替代，不写几何监督必伤动作。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA1.md)；未核完整artifact或复现。

### [CausalAlign: Causal Alignment of Video Generation Models for Consistent Ego-Motion](https://arxiv.org/abs/2610.29915v1)

exact-v1，先分别测pose读出和固定输入/随机性的norm-matched干预，再以teacher delta/projector适配诊断位置LoRA，需pose标注。FVD182.4→182.7退，局部干预/同源几何估计不识唯一因果位置，另训WAM非直接控制保证；Ch25 AEON后融入几何反向监督变化状态，全阶段费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [Looking Ahead: Modeling Future Evolution in Autoregressive Video Generation](https://arxiv.org/abs/2610.29989v1)

exact-v1，clean/noisy当前中层feature经独立offset预测不读中间visualchunks的未来，offset可含1、主干仍带文本；训练回传/部署弃aux。Chain V2V反退，42.6/50.7%只对fullhistory估计算量，非TF端到端实测；Ch24 Helios后融入正确近邻过易的替代监督。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [Attn-Forcing: Learning Full-Context Attention Proxies for Streaming Video Generation](https://arxiv.org/abs/2610.30036v1)

exact-v1，淘汰前更新learnedproxies，经额外DiT成native KV；random-feature S/z仅训练attention响应监督，非部署exact全历史。单独response匹配不保jointsoftmax，直接stats部署会blur；13%H20额外端到端费用与部分一致性退步保。Ch24线性历史两段和原marker后融入。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video](https://arxiv.org/abs/2610.30089v1)

exact-v1，只Daily track，不采用Sci；notification与start–maintain–stop捕获/后续QA分验。1fps逐秒模拟不是200msSLO，Start@.2只matched人口；K3不同memory/oracle/NoMemory视图使差混捕获表示读出，不授纯捕获因果。Ch77 PASK后增加主动取得证据生命周期，全逐帧调用/维护费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [ALPS: Visual State Encoders for World Models](https://arxiv.org/abs/2610.30120v1)

exact-v1，四训练目标服务三用途，knowncrop overlap与冻结stage1teacher非未知3D；stateprobe已知未来动作不同于WM，重建另训decoder。10%预算去重建/caption可改善state，未交付合一planner；Ch23 COMiT共同表示/容量取舍与Ch25重建非control充分已具体承载。 必要Source与具体owner决定经独立oct23_live_arxiv通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [VoxProg: 3D Spatial Reasoning through Voxel Programming](https://arxiv.org/abs/2610.30127v1)

exact-v1，knownmesh/initialpose的voxel witness与pose程序分责，固定initialworld须TT0^-1变换；静态support/collision非控制轨迹，DreamSim同pool相对rank，三/四方法表不能直接比。Ch26双对象affordance→几何代价→SE3→独立planner/controller链已具体覆盖，不为取证组件另建框架。 必要Source与具体owner决定经独立oct23_live_arxiv通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129v1)

exact-v1，时空codec stride改变动作齐备等待+WM/cache+decode，chunk间因果非chunk内逐frame因果。近静态/移动域空间时间取舍反向、FID近同可掩FVD/ARR退，但camera与scene/action仍混杂；humanARR仅12wrist维，单H100均值非SLO。Ch25 latent充分性后融入动作delay/压缩选择。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [T-WLA: Bridging Slow Vision and Fast Touch](https://arxiv.org/abs/2610.28814v1)

exact-v1，慢视觉缓存M/base，快触觉读causalhistory/elapsedtime只修valid未执行suffix，始终相对原base而非累计。训练futureheads不进入部署，接触筛选分母与有效119.1Hz非SLO、有限47.25→50成功不授安全；Ch26完整FFDC后/Chronos前融入快修替代，全训练/控制费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MULTIMODAL3.md)；未核完整artifact或复现。

### [Compressing Onboard Language Models for Space Robots under a Behavioral-Fidelity Requirement](https://arxiv.org/abs/2610.29302v1)

exact-v1，匹配格式量化器bank在当前拼装模型用完整next-token KL逐模块选，静态导出非runtime ensemble；局部inputscale须随模块，跨层变换不任意兼容。一遍/校准下降非全局或heldout保证，TA另用标签；候选/全词表cache/完整forward与packing全费，目录压缩不授kernel/SLO。Ch49 DINO-WM后融入离线组合选择。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection](https://arxiv.org/abs/2610.29646v1)

exact-v1，同观察反goal无符号switch合并两正确/两错误，halt使二动作A=a+b失效。同48queries基线+新增signal区分proper-score/rank/预定topK，MAE改善不授选择价值；前瞻CI跨零不证零效应或有害，crossseed目标仍有可恢复排序。Ch27 lossprior后融入corpus acquisition判断，全audit/训练费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [Memory-Centric Continual Learning for AI Agents](https://arxiv.org/abs/2610.29357v1)

exact-v1，storage×read grid交互2.93pp是对话cluster CI；IdeaBench online eval会写，t0不为空、cap不binding，summary少tokens反慢且F1损。预设powerlaw曲线不是实测定律。Ch77 writer/read双预算、Neuromem分阶段费用与MemoryArena匹配内容/曝光干预已具体承载，保有限新证据不堆taxonomy。 必要Source与具体owner决定经独立oct23_live_org通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [Reorienting the Vector Axis: Restructuring FlashAttention for Long-Vector Processors](https://arxiv.org/abs/2610.29489v1)

exact-v1，长vector以query轴连续令每lane维护一个query max/sum、沿key逐元素累积，归一仍每query keys。Bq128反慢，长Bq适prefill非query1 decode；scalarcoeff与fused/reorient分叉，不连乘倍率。FP32单核单头芯片/FPGA计量不同、packing/数值与全服务未授；Ch49 FA2/3后融入axis计划。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [HAWK: Heterogeneity-Aware KV Cache Transfer for Efficient GPU-NPU Phase-Disaggregated LLM Inference](https://arxiv.org/abs/2610.29873v1)

exact-v1，目标NPU perchannel tensor allocation/注册区与发送端layout变换联合，单连续buffer可channel OOM，RDMA接通不等可消费tensor。保registeredcopy/metadata/完成重建释放与未证faultlifetime，不授零copy；core/SRAM功耗估计非整机energy、市场capex非TCO。Ch55ownership后融入异构layout交接。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [pplx-embed-v2-late Technical Report](https://arxiv.org/abs/2610.29523v1)

exact-v1，共同teacher token欧氏norm监督连接小query/大doc多向量index，非任意encoder互换；全attention去mask不使GDN全双向。.6→9局部+1.6pp不等总费用不变，内部72tasks清单未公开限制复现。Ch76 teacherembeddingmatching完整链与query/docindex配对兼容/非对称部署已具体覆盖。 必要Source与具体owner决定经独立oct23_live_org通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [Qwen-Audio-3.1-ASR Technical Report](https://arxiv.org/abs/2610.28711v1)

exact-v1，3.0原文已有display/final刷新，本窗仅IDnumber稀疏CE×10与12.5Hz/80ms输出标签grid增量；不由帧率推hidden无subframe信息。省略绝对loss/iteration曲线不授训练倍数，约4min结果不授整场identity，recordinglocal非实名。Streaming/Message不支持SD，所有标注/多阶段训练费保；Ch23DM-ASR后融入jointfield监督。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [Directional Posterior Feedback Fusion for Query Reformulation in Dense Retrieval](https://arxiv.org/abs/2610.29464v1)

exact-v1，切空间每feedback仅约束支持方向，与query prior联合小系统/有界sphere更新；点目标多惩未表达正交方向是几何identity，非语义真值。MAD/zero退化未披露，Table2 pointcontrol非同λ完整ridge，10query timing非全RAG费/唯一因果。Ch76 queryonly成本后融入方向反馈目标替代。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_SYSTEM2.md)；未核完整artifact或复现。

### [FlowVLA: Learning Flow-Aware Physical Completion for Quantitative Robotic Pouring](https://arxiv.org/abs/2610.29692v1)

exact-v1，力/本体GRU belief维护累计量并预测固定撤回尾量，目标仅比较器；阶段切换废旧chunk，不授sensor真值/安全停止。13.15g只79完成试验，123attempt联合成功另算；容器液体另训非零样本。Ch26 GoalVLA反侧后融入累计量/停止后效，全传感标注/observer/policy/失败费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [CausGround: Causal Interaction Grounding for Adaptive Embodied Planning](https://arxiv.org/abs/2610.29702v1)

exact-v1，受控经验提preconditions/effects、一次taskknowledge加逐步state更新，causal名不证明SCM或完整物理guard。VirtualHome修状态/RoboCasa高层skill与真机定性限定外推；Ch79 typedplan/部分观察和建议相容/冲突/执行权完整链已承载，保新producer实例不堆框架。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [Reconstruction-Augmented Visuomotor Pre-Training of 3D-Grounded Bimanual Dexterity from RGB-Only Human Videos](https://arxiv.org/abs/2610.29716v1)

exact-v1，sharedvideoscale仍是手/depth估计，geometry输入和target联增不隔离单组件；残差gate不保训练后原VLM。需RGBD部署/动作head适配与32A10072h全预训费；Ch26camera→metric→action、人视频target和geometry/motor完整链已具体覆盖，不为组件新名添段。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies](https://arxiv.org/abs/2610.29730v1)

exact-v1，核方差是support几何代理，task覆盖可支配global rank却少within-task选择价值；跨重复.27只是排序可重复性参照，不是方法可预测上界。执行噪声、task-count null、supervisor occlusion反退/未测humanhandoff及全policy费保。Ch66三路confidence审计后融入任务/同任务/重复三分测量。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [GeoMem-VLA: Internalizing 3D Scene Understanding into Temporal Memory for Vision-Language-Action Models](https://arxiv.org/abs/2610.29866v1)

exact-v1，geometry计划训练target与部署双bank读后写/相邻均值merge分责，较晚timestamp非事件/provenance真值，几何消融联删组件不识唯一因果。16frame诊断非闭环、真机有限任务；Ch26 episode-owned derived/reset/fresh观测链与Ch77事件压缩已有具体边界，新配置/费用保报告。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation](https://arxiv.org/abs/2610.30097v1)

exact-v1，semantic边界非envdone，一步TD bootstrap保留，仅GAE跨界按事后完成衰减且value target同步。PCC错标签会错分credit；BATE任务人口/探索与过程reward不同，不全算tracegate因果。Ch26 SimpleVLA-RL后融入critic训练credit替代，全标注/失败/训练和独立执行费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [Asymmetric On-Policy Distillation Learns In-Context Exploration](https://arxiv.org/abs/2610.30105v1)

exact-v1，固定隐藏任务BAMDP以student history加另采expertprefix监督动作，不同逐state重标；一般POMDP需实际到达state接管后缀。条件posterior不授Bayesoptimal/安全探索，100x仅envsteps、真机10proprio非多模态通用。Ch26 visitedstate教师后融入context/query解耦，全expert/label训练费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [CW-WAM: A Structured Contact-Wrench World Action Model for Force-Sensitive Manipulation](https://arxiv.org/abs/2610.30117v1)

exact-v1，continuous6D wrench需frame/origin/validmask，slow WAM reference与20Hz admittance真实feedback分开。Progress不是contact oracle，.5–.6s排network，成功人口RMSE和openloop/真机normalization不同。Ch26 desiredcontact和slowreference→fastfeedback/执行权限完整链已具体覆盖，不重复wrench框架。 必要Source与具体owner决定经独立reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_VLA2.md)；未核完整artifact或复现。

### [Did the Problem Actually Get Harder? Testing LLMs on Paired P and NP-Complete Problems Hardened by Adversarial Multi-Agent Rewriting](https://arxiv.org/abs/2610.30103v1)

exact-v1，同surface结构造P/NPC twin、同class内familiarity hardening是两轴控制；有限gate/480人审20移除不授全改写形式保义。Hardening同时压低两侧成绩但长度/instance攻击仍混，lineage相关；wrong/crash与TLE另列，程序wallclock非模型思考budget或复杂度下界。Ch66关系难度反侧后融入，全构造/攻击/执行/人审费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [LongZero: Enhancing Long-Context Reasoning in LLMs from Zero Data](https://arxiv.org/abs/2610.30132v1)

exact-v1，短QA/evidence骨架后扩长context；字符串/ID gate不证明完整support/distractor语义，程序needle序号标签另源。有限时对时错自筛仍继承错题/判分偏差，zero新增正文非零模板/成本/无泄漏。8B部分真实长文benchmark低于base，各配比有反退；Ch27 ontology局限后融入替代数据制备，全合成/筛题/RL/评价费保。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL Prefix Importance-Ratio Clipping](https://arxiv.org/abs/2610.29999v1)

exact-v1，§3–5及相关反例区分归一化prefix/EOS与共同support上的精确性能恒等式、实际current-token替代梯度；φ逆KL坐标不把裁剪平台变成hardKL或单调改进。写入Ch32前缀校正段，保同评测选择偏差与driver内存非GPU总费边界。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [Mitigating Model Collapse through Dreaming Learning](https://arxiv.org/abs/2610.30009v1)

exact-v1，机制与受限递归实验区分synthetic采样温度和训练温度/损失权重，真实anchor累计不自动阻止模型坍塌；谱稳定也可保留偏差。Ch27递归风险段补采样/训练两种控制权，保有限实验仍劣化与混合不等真值，不采用未证明的通用矩阵floor。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [Agent Behavior Maps: Locating Agents by What They Would Do, Without Running Them](https://arxiv.org/abs/2610.30014v1)

exact-v1，共享外部历史、teacher-forced固定动作logprob构造behavior近邻，仍需完整forward/参考与独立校准。Ch66指纹诊断段补无新rollout不等无计算、共同Q支持和有界log条件、仅排序代理，保绝对KL高估、单轨迹/跨环境局限与canonical token非动作边缘概率，不推谱系或行为保证。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [Loopholing All the Way: Language Modeling with pure Self-Conditioning](https://arxiv.org/abs/2610.30068v1)

exact-v1，LAW以expected embedding作为唯一跨步状态，UDM训练腐化不等离散reverse kernel/GaussianODE或新精确NELBO。Ch24自条件分工段补模式/温度/stopgrad与高NFE熵退化，FLOP匹配不授wall-clock及16倍通用加速；保AR、离散采样和传统自条件适用边界。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [Circuits of LLM Classifiers](https://arxiv.org/abs/2610.30076v1)

exact-v1，有限二元instrument池的已知/估计条件概率与成本支持停止/继续DP，3^n状态不是通用Agent最优性。Ch62分类路由段补条件独立层次/潜在类型混合与embedding、离线DP、全部调用成本，保同源group五折、标签非真实临床真值及token估价非尾SLO，不采用无限重复渐近保证。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [Velocity Ambiguity Profiles: Time-Resolved Bayes-Risk Diagnostics for Flow Matching](https://arxiv.org/abs/2610.30107v1)

exact-v1，VAP把population velocity MSE分成Bayes floor和excess；同path/population的强reference差只能抵消共同floor而得相对误差。Ch24时刻分配段补未重要性重加权改变目标、reference/featureflow费用与高全局FD却recall退化/条件KID反侧，不移用相反时间约定公式或未采用的收敛率定理。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_MODEL5.md)；未核完整artifact或复现。

### [Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698v1)

exact-v1，§3–6与必要人口/seed协议表明固定non-Minecraft池只改mixture而非世界数量；loss/源域改善不授远域收益，120配置单训练seed且API部署混杂。Ch7既有loss→task、250700885反侧与数据mixture完整论点已承载分布/checkpoint/harness联合冻结和aggregate不代slice验收；本实验新验证不改变该义务。 必要Source与具体owner决定经独立oct23_live_arxiv通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [Fig: Automated Multiagent Behavior Elicitor](https://arxiv.org/abs/2610.28891v1)

exact-v1，§2–5/A5/B3将行为机会、规范、尝试/执行/后果分开；机械positive可补语义negative，机械未命中不证明不存在。Ch66 SANE后补text-game干预的测量对象和双通道，保多轴同时干预仅整套因果、有效control/标签子集与独立校准费用，不由高诱发率推出真实风险或意图。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [Hidden Messages Between Diffusion Language Model Agents: Causal Evidence for Latent Communication](https://arxiv.org/abs/2610.28905v1)

exact-v1，§3–8必要对照在冻结diffusion backbone、监督codec中分开正确私有消息和handoff时机；依赖查询的任务需早交换、独立证据任务singlelate反优多轮。Ch82内容因果审计后补依计算依赖选择handoff，而非重复既有错配/随机检查。保task-specific训练、无匹配文本通道/完整wall-clock优势与全部forward费用。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [DiffResearch: Accelerating Deep Research with Diffusion Language Models](https://arxiv.org/abs/2610.28909v1)

exact-v1，§3–5/限制中首个可解析固定数量子查询仅允许只读consumer，稳定不证明事实或最终文本；局部decomposition提前未进一步缩短end-to-end pipeline。Ch81 temporalcache后补未完成生成的有界消费资格，保backbone混杂、RACE CI跨0非等价、50claim仅14充分支持与全部解析/检索/验收成本，不授有副作用提交。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents](https://arxiv.org/abs/2610.28934v1)

exact-v1，§3–6/A/B4/C4–5/D1支持pre-mutation状态capture、前置、durability与可重建分验；workspace外专设人口、judge-positive校准和字符similarity不授业务等价或自然事故率。Ch78文件staging反侧后补动作级备份/恢复责任，保readonly/规则/worker误判、外部ID及第三方状态不能还原、全部存储和恢复验收费，不授通用原子性或安全。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [AgentPolicyForge: From Executable Environments to Policy Benchmarks and Adaptive Guards](https://arxiv.org/abs/2610.28989v1)

exact-v1，§2–4与VIOLA必要域表明允许tool仍可因argument/resource/state违规；preaction guard不能读取未来verdict，Level4阻断与仅flag区分，archive收益随threshold改变、OOD CI跨0且误拒上升。Ch72 Solver20449和ToolFence37196具体正文已覆盖当前状态/参数授权及确定policy优先，有限case生产/SFT实证不新增更强安全框架。 必要Source与具体owner决定经独立oct23_live_arxiv通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [Inheritance as an Admission Test for LLM Prompt Merge Operators](https://arxiv.org/abs/2610.29023v1)

exact-v1，§3–5以operator自身零dose、heldout/reprobe检查donor传递，文字百分比不是几何插值；冻结panel与pooled best-seed仅单模型/单博弈附加诊断，不能把selection均值升当新学能力。Ch82成员演化段后补传递与淘汰分验，保half-dose预定门非通用保证、Undetermined与全部merge/probe/对局费用。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [Robust Soft Skill Adaptation via Behavioral Localization in Tool-Using Agents](https://arxiv.org/abs/2610.30041v1)

exact-v1，§3–4/T1在同一成功teacher轨迹上以有/无textskill的gold-token gain乘全词表JS提监督位置，8inputembedding软提示另有preservation anchor。61成功轨迹的96.12%集中度非因果；共享103/280低于text/OPCD，61task-specific人口独立heldout未披露。Ch29监督mask、条件gain相对性与Ch75软prompt/base-anchor已具体承载选择与保护职责，G×JS局部selector不增新权限；不自补clip/缺项配方或指控泄漏，全部双forward/训练/rollout计费。 必要Source与具体owner决定经独立oct23_live_reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [GRAM: Group-wise Rank-Aware Model Merging via Subspace Alignment](https://arxiv.org/abs/2610.29110v1)

exact-v1，§3–6/D2/D6将同基座task delta按输出子空间分成K组、组内rank预算重建，理论投影basis最优不授column-stacked实际算法最优或整网质量。Ch30 adapter冲突段后补一份全局artifact与全独立资产之间的预算分支，保task-aware/少样本router资格、单seed/更多K非单调、合成大T仅成本及全部分解/驻留/回归费，不采用医疗应用或通用遗忘保证。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT3.md)；未核完整artifact或复现。

### [LaVGuard: Selective Decoding for Contextual Value Drift](https://arxiv.org/abs/2610.29135v1)

exact-v1，§3–6与必要费用/估计条件区分authorized任务profile、visible-prefix probe、density触发与prototype方向，不能认证价值真值。Ch72 valuefilter后补sampling kernel改变位置和累计conditional KL两预算，事后guard拒绝仍计费；保候选全部重算、local surrogate非终局安全、误拒/效用反退及未披露重复单位/硬件，不移用理论界作生产保证。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [Steering Black-Box Large Language Model Agents with Pitfall Anticipation World Model](https://arxiv.org/abs/2610.29139v1)

exact-v1，§3–5与必要D/E/F表明frozen actor先提案，advisor检查真实history和动作，可pass或提出pitfall后重提案；每轮去旧guidance防预测当事实。Ch79 horizon反侧后补可沉默advisor的控制分工。保每步advisor/后见监督/训练/重试全费、Web以LLMjudge替严格终局规则、20k截断和baseline未匹配RL预算，不授安全、事实或端到端降费。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [PreCoMem: Predictive Cognitive Memory for Self-Evolving Long-Term Dialogue Agents](https://arxiv.org/abs/2610.29467v1)

exact-v1，§2–4/C8/C9中TopK检索分布集中度只缩放语义/NLI偏差，不测事实真值；miss使该轮无法correct，forced hit只恢复部分差额，低集中度也延迟真实drift。Ch77 RIKA后补读资格与写更新耦合，保raw/权重总和非物理存储界、judge/合成压力人口、query-to-answer不含全部维护及全费用，不将确定公式当事实裁决。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [TraceForge: Distilling with Your Own Thinking](https://arxiv.org/abs/2610.29680v1)

exact-v1，仅精确v1 §2–5/T1–2：执行trace的来源真实性不等推理正确或监督资格，style与训练数据差异未隔离，3500/5000口径分开；单run、重复评测非重复训练和HumanEval非单调保留。Ch29固定QA12397与teacher/student01702具体论证及Ch27三字段lineage已分别承载目标/路径/来源资格，不把新trace生产局部实例另造长期机制；未混次日v2、未采用法律宣传。 必要Source与具体owner决定经独立oct23_live_reader通过，无新增书段。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [RubricOpt: Self-Revision of Semantic Rubrics for Preference Optimization](https://arxiv.org/abs/2610.29491v1)

exact-v1，§3–4/C2/C3固定pairs、labels与两臂response-normalized配方，用训练准则条件后撤去，当前policy可提specgap编辑但已覆盖未学会须keep。Ch34 rDPO后补规范编辑与模型学习失败分责，gate仅编辑合同，须matched continuation分开额外训练；保反馈/最终评测重叠、各指标增退及完整判分/训练/对照费用，不采全局保证或未见任务递归自改善。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [UserSWE: Evaluating Coding Agents in Multi-Turn Conversations with Dynamic Users](https://arxiv.org/abs/2610.29822v1)

exact-v1，§4–6/C1–3/Alg2/D3把固定任务persona链、动态信息release和interaction预算分开；候选请求test rewrite须实际candidate通过/base失败/全regression通过，再经非原Judge Reviewer核行为与attestation。Ch66 InteractWeb后补评价instrument/执行结算，保gold-derived池、40.9%rewrite非正确率、有限tests不证明完整语义、72任务局部统计与均值/中位cost不能拼总费。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [ToM2Vec: Continuous Theory-of-Mind Tokens for Multi-Agent Coordination](https://arxiv.org/abs/2610.29934v1)

exact-v1，§2–4/A–C中同坐标partner实际thought仅训练target，部署从main自身可见context生成latent，不读取对方真实私有state。Ch82 behavioralbelief后补训练特权与推断可见边界，保自报标签/PPL非心理真值或唯一因果、C明确negotiation未显著、有限跨伙伴和全部采集/训练/forward费用，不授异构直传或执行授权。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_AGENT4.md)；未核完整artifact或复现。

### [Plan First, Act Later: Streaming Reasoning for Executable Memory in Robot Control](https://arxiv.org/abs/2610.29329v1)

exact-v1，§4–6/B/C2/D1将瞬态证据提前写成顺序subtask列表，区别消费计划与真实effect；stage1联合监督内容/启发式时机，stage2依参考标签将错/重复更新置空、缺必需更新超时整轨不用自标。Ch26预测性写入后补此资格，保清旧事件/buffer丢证据、无条件branch、标签/oracle训练非部署真值与全部标注/自训练/视觉/控制费用，不授实时或安全。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_WORLD2.md)；未核完整artifact或复现。

### [PhysiCalWorld: In-Context Physics Calibration for World Models](https://arxiv.org/abs/2610.30125v1)

exact-v1，§3–5/A2–4用同动力学组另一episode的action-observation交互压成descriptor条件，训练无物理数值标签仍依赖准确same-physics分组；实际为channel条件，不是新增attention序列token。Ch25 QWM后补未知stationary动力学取证/复用与失效责任，保有信息接触、raw context局部更好、预测画面非planning成功、OOD仅有限关节阻尼和全部探索/编码/训练/CEM/真实验收费，不授实时或安全。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_WORLD2.md)；未核完整artifact或复现。

### [Agentic World Action Models](https://arxiv.org/abs/2610.30136v1)

exact-v1，§2–3/A/F/H/I/K/L区分code→video→action单向条件中的内部subtask与可交primitive的程序；hybrid attempted即弃同轮chunk，exception须fresh观测，无exception记stage也非物理postcondition。Ch26 UniWALM后补双consumer验收，保hybrid另采示教/clean反退、真机仅一YAM任务、有效语法非相对动作优势与全部三路/技能库/执行成本，不授控制deadline或安全。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_WORLD2.md)；未核完整artifact或复现。

### [Causal world models under physical parameter shifts](https://arxiv.org/abs/2610.29088v1)

exact-v1，§2/4–6/A/B1–2的实际mass移位反证区分移除shortcut与建模相关物性；同finger-local family下mass-affine inertia/bias及known-PD路径支持有限输入效用，非最高绝对精度，learned-torque分支效用近零。Ch25结构先验风险后补真实参数仍可伤预测、同机制actual/mean/no-mass对照，保人工robot路由非合成mask因果发现、正定非真实能量一致、整套配置混杂与短预测非控制，不禁止有效无mass fallback。 root准许原段实存，非writer完整新增/直接两侧/本人注POST通过。 [必要证据与评价条件](../_sources/daily-20261023/SOURCE_WORLD2.md)；未核完整artifact或复现。

## 5. 缺口与下一步

普通研究与Books待办：无。全部必要修改均已实存并通过独立写后复核；独立日级验收见§6。

隔离的外部覆盖终态保留项：Google pubs日筛、Meta Research/Publications与Qwen新站动态目录当前有限原始恢复仍不足；不用于确定零发布、正面证据、Books或无遗漏断言。重开条件为可读目标Oct22目录、官方同日原文/批次快照或能定点恢复身份的原始链接；只重开对应源/材料，不扩全部日期。不用普通未读项替代这些具名外缺。

窗外恢复线索，不属于本窗：`2610.28637v1` KVLearn虽在Oct22 arXiv new公开列表，正文的SYSTOR线索经出版方[Crossref DOI](https://api.crossref.org/works/10.1145/3793230.3837769)精确题名与五作者确认，online为Sep2、print为Sep8。此次未见实质修订，故不能按arXiv新收录再次作为新论文评分；不是已审重复或贡献排除，也没有在此轮处理Sep2日报。保留[已读必要原件与改判依据](../_sources/daily-20261023/ARXIV.md#28637-首公开纠正窗外不冒已审重复)，日后只恢复真实owner日。


## 6. 复核

复核者：`oct23_live_reader`；交叉独核 `oct23_live_arxiv`（MM3、AGENT3）、`oct23_live_org`（SYSTEM2、MODEL5、WORLD2）。均非报告/Books作者；Source准备者不自行验收本人材料，reader复用具名交叉结果汇总。

结论：通过

已分批独核全部拟入题摘/评分、风险排除、12分类公告关联和机构有限停止点；普通机构排除作具名分层抽检，不称全部普通PR/插件代码全审。全部189家族有对应证据与Books决定，实际123个保存窄位均通过独立写后检查，详见[REVIEW](../_sources/daily-20261023/REVIEW.md)。修正过强的局部结论、MODEL3八行遗漏的贡献句及三维分量抄录；不重读有效原证、不改分凑工作量。独立复核者已实际检查完整六节保存态并在[REVIEW R69](../_sources/daily-20261023/REVIEW.md)通过日级验收；机器通过不替代该语义审阅。

V3接口、189项正文/证据一一对应、本地链接与本日限定working空白检查通过；Books/Report/State的cached空白检查也通过。扩至已有_sources暂存原件时，ORG原始摘录及两个JSON仍有尾空白，保留原件且未改index，不声称全仓或全部暂存项清洁。机器通过不证明全网无遗漏或实验复现。保护并发修改，不stage、commit、push。
