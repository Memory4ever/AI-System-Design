# Daily Research — 2026-09-23

**规范：** V3
**窗口：** 2026-09-22T09:00:00+08:00 ～ 2026-09-23T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T23:38:13+08:00

## 1. 结论

本日恢复真实 Wed23→09/23约08:00北京时间公告，而不是沿用旧 Tue22 目录。旧38家族的有效证据与实际 Books 已由 `sep22_resume_v3` 迁入[09/22 Daily](../22/README.md)，附件保留，不因归属纠错删除机制。

十二类来源取得666唯一 New/Cross 身份，其中554至少一类New、112仅Cross；这是有限主题查漏库存，不是候选或全文队列。最终冻结40个本窗唯一家族（原29＋新增5＋具名查漏6New）：35整合、2已有覆盖、2仅报告、1中央争议隔离。40项必要证据与Books处置均已逐项非作者核；35处实际窄增量及相邻正文全部写后通过（sep21核原29处，root核新增6处）。TopoCross首公开日期与ReDraft撤回后v3事件精确隔离，不评分、不采用；SARA最优保证争议、机构日期/访问限制与日级复核分列。最终全日非作者复核通过，普通待办为0；来源、日期与中央争议仍隔离，不代表覆盖无缺口或所有论文结论成立。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [官方 News RSS](https://openai.com/news/rss.xml) 的两条本窗事件及 [Research](https://openai.com/research/index/) 已检查；Sol/Luna 为 09-23 02:00、prompt caching 为 05:00 北京时间，详见[机构账本](../../_sources/daily-20260923/institution-screening.md) | 已检查 | Sol/Luna 只披露模型版本、价格和受限评估，未公开新机制；prompt caching 经独立复核为既有机制的版本事实；Astra card 更正仅有日级日期，隔离待归属 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) 最新可见 09-17；[Newsroom](https://www.anthropic.com/news) 可见 09-22 Opus 5.5 公告及 system card | 已检查 | Opus 5.5 官方只给日级日期，跨本窗边界；机制暂作 Date Hold，不评分、不写 Books |
| SRC-GOOGLE-AI | [DeepMind news](https://deepmind.google/blog/) 与 [Google Research blog](https://www.research.google/blog/) 可辨新到旧条目至 09-18 或更早；[Google Research publications](https://research.google/pubs/) 官方目录 2026 年过滤有 304 篇但混列 2026/2027、仅标年/venue；日期检索无可用本窗结果 | 受阻 | 机构论文目录无法按首发日建立本窗停止点；不作全量零新增断言。本窗 arXiv 身份另行核，获官方日期索引/RSS 后只补查该入口 |
| SRC-META-AI | [AI at Meta blog](https://ai.meta.com/blog/) 最新可见 07-27；Research 动态正文抽取有限，改查官方 [results](https://ai.meta.com/results/) 的按日期递减 Publication 列表，首项 09-07 | 已检查 | 官方替代列表首屏无本窗条目；这是有界入口结论，不声称全组织所有独立仓库无事件 |
| SRC-QWEN | [Research](https://qwen.ai/research) 动态页返回 SPA shell，网页正文抽取为空、浏览器重试超时；官方详情页索引只显示较旧条目；[Qwen Code v0.24.5-preview.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.24.5-preview.0) 本窗发布，官方 PR 与邻近日报去重 | 受阻 | Research 没有可验证的列表分页/时间停止点，索引快照不能证明本窗零新增；获官方可读列表/API 后定点重开。PR #12323 机制首公属 09-21 Daily，本窗 release 仅版本包装 |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)新闻回查至 09-10 V4.1 Flash | 已检查 | 未见本窗新机制，不将旧事件重新计分 |
| SRC-MOONSHOT | [Kimi 平台博客](https://platform.kimi.com/blog) 及 MoonshotAI 近期活跃仓库 release 前十项；`kimi-cli 1.52.0` 落窗 | 已检查 | CLI 更新仅安装入口，候选前关闭；GitHub 是有界补扫，不是全组织零发布证明 |
| SRC-TENCENT-HUNYUAN | 官方 `publicList` 实际9条及仓库有界结果；第9条100116对应 [When Do Larger Batches Help Scale LLM Reinforcement Learning?](https://arxiv.org/abs/2608.29296)，root已定点核身份/版本 | 已检查 | 官方v1为2026-08-29T14:32:09Z，当前仅v1、无September revision；09-22 display日/09-23 publicAt只是同家族网页出现，不是本窗首公开或重要修订。保旧family证据，不重复深审或计分；目录结论限实际9条，不声称全组织零事件 |
| SRC-ZAI | [智谱 Research](https://www.zhipuai.cn/zh/research) 动态页原始 HTML 与搜索渲染首屏检查；公开网页抓取超时，最新可辨研究条目 08-26；[官方模型发布说明](https://docs.z.ai/release-notes/new-released) 按日期递减，首项 08-26、次项 08-18 | 受阻 | 模型发布入口可闭合，但动态研究列表未建立可验证的完整翻页终点，不能断言研究全站零命中；获官方可读列表/API 后定点重开。ZCode 09-22 只有日级日期，Date Hold |
| SRC-BYTEDANCE-SEED | [Seed Research](https://seed.bytedance.com/en/research) 与 [public papers](https://seed.bytedance.com/en/public_papers) 最新可见 08-18；近期活跃仓库 release 有界检查 | 已检查 | 未见本窗可辨识的贡献项；有界仓库回查不作全组织零发布保证 |
| SRC-BAIDU-ERNIE | [ERNIE blog](https://ernie.baidu.com/blog/zh/) 按日期递减共 2 页、首页最新 05-09；[PaddlePaddle/ERNIE releases](https://github.com/PaddlePaddle/ERNIE/releases) 最新 06-30 ERNIE 4.5；PaddlePaddle 活跃仓库前 30 个及各自前 10 个 release 有界补查 | 已检查 | 指定入口可据新到旧 stop point 关闭本窗；org 补查不是全组织零发行证明 |
| SRC-XIAOMI-MIMO | [MiMo 首页](https://mimo.xiaomi.com/) Paper 1–8 完整列表最新 06-29，Blog 1–14 完整列表首项 MiMo-V2.6；[MiMo-Code 0.1.15](https://github.com/XiaomiMiMo/MiMo-Code/releases/tag/v0.1.15) 发布落窗，PR 首公与邻近日报去重 | 已检查 | Paper 列表本窗无新增；Blog 首项技术公告只有 09-22 日级更新时间，Date Hold；代码 PR 机制归 09-22 Daily，不能误计今天 |
| SRC-MINIMAX | [Research blog](https://www.minimax.cn/blog) 可见列表最新 08-13；[minimax-code 0.5.2](https://github.com/MiniMax-AI/minimax-code/releases/tag/v0.5.2) 发布落窗 | 已检查 | 本窗 release 仅包构建/安装测试，候选前关闭；其他官方博客入口仍作有界回查 |
| SRC-ARXIV | [十二类 recent Wed23 官方身份与停止点](../_sources/daily-20260923/date-recovery-review.md#2-来源停点与原身份检查)：skip0/show2000，各 New/Cross 组完整至下一日标题；Flux 另核 primary cs.NI | 受阻 | 约定主题与具名7有限补检结束，不称666全题摘/全文或全学科无遗漏；TopoCross具体primary首公与16639v3 Replacement/恢复边界未取得，已隔离。40候选的独立书稿处置另见§3/5，不把普通工作混为访问缺口 |

## 3. 候选与判断

最终冻结40个本窗唯一家族（原29＋新增5＋有限查漏6New），准入均经非作者完整题摘校准，必要证据及最终Books逐项核完成；35处实际增量全部非作者写后通过。TopoCross日期与ReDraftv3事件不在确定候选内。原38项已迁至[真实09/22](../22/README.md)，本日不重复评分或书稿写入。冻结分母不表示666条宽库存已全文审阅；最终日级Gate已通过。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](https://arxiv.org/abs/2609.26796v1) | 2026-09-23T08:00:00+08:00 | 刷新 query、cache 写回与双 mask 验证共同决定 IO 计划；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（实际两段及非作者写后通过） |
| [HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing](https://arxiv.org/abs/2609.26368v1) | 2026-09-23T08:00:00+08:00 | FA-source 重投影与 inner reuse 是不同缓存域，早退出依赖训练结构；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)（实际两段及非作者写后通过） |
| [Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1) | 2026-09-23T08:00:00+08:00 | 实时语音、foreground call 与 delegated task 的取消生命周期分离；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)（已实际窄写及非作者写后通过） |
| [Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models](https://arxiv.org/abs/2609.25890v1) | 2026-09-23T08:00:00+08:00 | 匹配 exposure 后 batch composition/loss normalization 决定首 epoch 收益；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)（已实际窄写及非作者写后通过） |
| [LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay](https://arxiv.org/abs/2609.25053v1) | 2026-09-23T08:00:00+08:00 | hybrid 跨模型 handoff 必须处理 recurrent matrix、conv history 和初始化语义；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)（已实际窄写及非作者写后通过） |
| [Prompt Breadth and Rollout Refresh Interact in On-Policy Distillation](https://arxiv.org/abs/2609.25048v1) | 2026-09-23T08:00:00+08:00 | prompt breadth 的收益与 rollout refresh、token 预算交互；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受限上下文/策略实验，不形成必要书稿差额（sep21有限终判通过） |
| [Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation](https://arxiv.org/abs/2609.26693v1) | 2026-09-23T08:00:00+08:00 | before-dispatch 拒绝、transport 身份与 turn/task 分母必须分账；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已实际窄写及非作者写后通过） |
| [Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference](https://arxiv.org/abs/2609.26621v1) | 2026-09-23T08:00:00+08:00 | greedy top-two margin 决定受限 FP32 head scope，扩大 scope 不单调改善；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（已实际窄写及非作者写后通过） |
| [Disaggregated Quantization: Specializing LLM Prefill and Decode](https://arxiv.org/abs/2609.26333v1) | 2026-09-23T08:00:00+08:00 | P/D 权重精度可分工，但交接 KV 的数值/语义兼容不可省略；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md)（已实际窄写及非作者写后通过） |
| [Component Type, Not Reconstruction Error, Predicts Attention Quantization Sensitivity](https://arxiv.org/abs/2609.26173v1) | 2026-09-23T08:00:00+08:00 | 单 projection reconstruction 排序不认证任务敏感度或全 mixed-bit 收益；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（sep21已核必要源与实际覆盖通过） |
| [Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining](https://arxiv.org/abs/2609.25482v1) | 2026-09-23T08:00:00+08:00 | 终态 averaging/shrinkage estimator 与学习率 schedule 共同定义输出；2 + 1 + 2 = 5 | 深入完成 | 整合：`TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md)（已实际窄写及非作者写后通过） |
| [Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo](https://arxiv.org/abs/2609.25451v1) | 2026-09-23T08:00:00+08:00 | GPU 模型分配寿命可脱离 engine，但 pretraffic shadow 不保请求进度；2 + 3 + 2 = 7 | 深入完成 | 整合：`INFER-DYNAMO` [Ch52](../../../../books/part-05-inference-system/52-dynamo.md)（已实际窄写及非作者写后通过） |
| [Flux: Optimal Scheduling of Optical Circuit Switches for LLM Training](https://arxiv.org/abs/2609.25949v1) | 2026-09-23T08:00:00+08:00 | iteration DAG readiness 与电路延续联合调度，少重配不等最短执行；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)（已实际窄写及非作者写后通过） |
| [Decoupling Logical Masks from GPU Execution for Dynamic Block-Sparse Attention](https://arxiv.org/abs/2609.25869v1) | 2026-09-23T08:00:00+08:00 | logical mask 不变的 retile 与 offline eligibility portfolio 分开，kernel 最快不等 request 最快；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（已实际窄写及非作者写后通过） |
| [SARA: SLO-Aware Resource Allocation for Disaggregated Agentic LLM Services](https://arxiv.org/abs/2609.26763v1) | 2026-09-23T08:00:00+08:00 | tail-resource 模型依赖队列/分位假设，单调成本不能推出唯一全局最优；2 + 1 + 2 = 5 | 争议 | 暂缓：printed 唯一全局最优中央结论争议，见§5 |
| [WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning](https://arxiv.org/abs/2609.25442v1) | 2026-09-23T08:00:00+08:00 | trainer→rollout layout plan 去冗余与 balancing 不等 publication 原子性；2 + 3 + 2 = 7 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)（已实际窄写及非作者写后通过） |
| [RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy](https://arxiv.org/abs/2609.26467v1) | 2026-09-23T08:00:00+08:00 | phase ownership 切换须作废未执行 chunk suffix，并重新取得当前 observation；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（已实际窄写及非作者写后通过） |
| [RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?](https://arxiv.org/abs/2609.26292v1) | 2026-09-23T08:00:00+08:00 | 视觉稳健与物理参数稳健不同，planner 可行筛选改变评价分母；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：`MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)（sep21已核必要源与实际覆盖通过） |
| [PatchKV: Efficient KV Cache Recovery for Dynamically Edited LLM Contexts](https://arxiv.org/abs/2609.26219v1) | 2026-09-23T08:00:00+08:00 | 先冻结 repair/reuse 集合，再分配 precision，importance 不拥有有效性裁决；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)（已实际窄写及非作者写后通过） |
| [CoVeR: Coverage-Based Routing of Verifier Calls in Agentic Retrieval](https://arxiv.org/abs/2609.26086v1) | 2026-09-23T08:00:00+08:00 | cheap uncovered margin 只能 defer costly decider、继续搜索，不直接停止；2 + 1 + 2 = 5 | 深入完成 | 整合：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md)（已实际窄写及非作者写后通过） |
| [MemoryAthena: Adaptive Routing over Latent and Generated Memories](https://arxiv.org/abs/2609.25853v1) | 2026-09-23T08:00:00+08:00 | direct Engram residual 与两路生成表示分权，likelihood router 不认证真值；2 + 2 + 2 = 6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)（已实际窄写及非作者写后通过） |
| [CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.26779v1) | 2026-09-23T08:00:00+08:00 | 只 compact 当前 live window 可减少递归影响，但明确丢弃旧 recall；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受限上下文/策略实验，不形成必要书稿差额（sep21有限终判通过） |
| [Impact Is Not Invalidation: Ask About the Claim, Not the Diff](https://arxiv.org/abs/2609.25130v1) | 2026-09-23T08:00:00+08:00 | diff reachability/行为改变不等特定 memory claim 失效，问法也改变判决；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)（已实际窄写及非作者写后通过） |
| [Self-Cleaning and Captured Anyway: One Measured Primitive for Error in a Store an Agent Writes to Itself, and What a Falling Score Actually Measures](https://arxiv.org/abs/2609.25052v1) | 2026-09-23T08:00:00+08:00 | 单 majority agreement 写入 gate 在高污染时可锁住错误、拒绝真实纠正；2 + 1 + 2 = 5 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md)（已实际窄写及非作者写后通过） |
| [Reading Right, Answering Wrong: How Visual Configuration Changes Affect Evidence Use in VLMs](https://arxiv.org/abs/2609.25770v1) | 2026-09-23T08:00:00+08:00 | visual configuration 离散变化与相同配置内 pixel 变化需分别控制；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)（已实际窄写及非作者写后通过） |
| [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425v2) | 2026-09-23T08:00:00+08:00 | query-sensitive quantization 与 K-error 主子空间 logit 补偿分权；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)（已实际窄写及非作者写后通过） |
| [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](https://arxiv.org/abs/2609.25809v1) | 2026-09-23T08:00:00+08:00 | 静态 reduced-k 与逐token动态专家分配 的差额受 generation/预算协议限定；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md)（已实际窄写及非作者写后通过） |
| [Virtual Encoders in Multimodal Transformers](https://arxiv.org/abs/2609.26513v2) | 2026-09-23T08:00:00+08:00 | backbone 内感知表示的 formation、readout 与 routing 需分别实证；2 + 1 + 2 = 5 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)（已实际窄写及非作者写后通过） |
| [StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training](https://arxiv.org/abs/2609.26774v1) | 2026-09-23T08:00:00+08:00 | encoder STE、codebook tracking 与分组 LR 是不同优化职责；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)（已实际窄写及非作者写后通过） |
| [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](https://arxiv.org/abs/2609.26048v1) | 2026-09-23T08:00:00+08:00 | timing-matched sham 将规则内容与仅中断效果分离；2 + 2 + 2 = 6 | 深入完成 | 整合：`AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md)（已实际窄写及非作者写后通过） |
| [Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL](https://arxiv.org/abs/2609.25938v1) | 2026-09-23T08:00:00+08:00 | oracle-relative certificate 与独立语义标签风险不同；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已实际窄写及非作者写后通过） |
| [Auditing Proxy-Based Validation Across Text Spans](https://arxiv.org/abs/2609.25808v1) | 2026-09-23T08:00:00+08:00 | same-span proxy agreement 可能由共享表面信号而非 construct validation 驱动；2 + 2 + 2 = 6 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已实际窄写及非作者写后通过） |
| [Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages](https://arxiv.org/abs/2609.25721v1) | 2026-09-23T08:00:00+08:00 | 表达消失与跨代 trait 清除不同，probe/steering 也不认证内部真值；2 + 2 + 2 = 6 | 深入完成 | 整合：`TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md)（已实际窄写及非作者写后通过） |
| [MICRO: Multi-Fidelity Active Search for Severe Error Discovery](https://arxiv.org/abs/2609.26025v1) | 2026-09-23T08:00:00+08:00 | 便宜 rating 只能指导预算搜索，确认 severe error 仍需高保真 annotation；2 + 1 + 2 = 5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)（已实际窄写及非作者写后通过） |
| [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](https://arxiv.org/abs/2609.26718v1) | 2026-09-23T08:00:00+08:00 | 固定位置的背景竞争与距离效应分开，score整形仅在条件满足时改善；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)（实际两段及root非作者写后通过） |
| [Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](https://arxiv.org/abs/2609.26708v1) | 2026-09-23T08:00:00+08:00 | 目标量化forward产生的student prefix须进入恢复训练分布；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)（实际两段及root非作者写后通过） |
| [When Recursive Models Finish Computing](https://arxiv.org/abs/2609.26487v1) | 2026-09-23T08:00:00+08:00 | 实际轨迹方向稳定与全空间Jacobian扰动稳定不能互相替代；2 + 1 + 2 = 5 | 深入完成 | 整合：`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)（实际两段及root非作者写后通过） |
| [CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](https://arxiv.org/abs/2609.26300v1) | 2026-09-23T08:00:00+08:00 | exact-block selector须按下游tail补偿残余而不只attentionmass排序；2 + 2 + 2 = 6 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)（实际两段及root非作者写后通过） |
| [PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models](https://arxiv.org/abs/2609.26249v1) | 2026-09-23T08:00:00+08:00 | lookahead horizon与实际commit threshold分权，饱和yield oracle不等runtime最优；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)（实际两段及root非作者写后通过） |
| [Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation](https://arxiv.org/abs/2609.26182v1) | 2026-09-23T08:00:00+08:00 | 旧模态保留须实际绕过新adapter算术，gate入口与重算scope构成条件；2 + 2 + 2 = 6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)（实际两段及root非作者写后通过） |

## 4. 证据与知识整合

每项均引用精确版本必要证据与实际owner比较，详见[本日恢复与审阅笔记](../_sources/daily-20260923/date-recovery-review.md)。原34的29处实际增量已获sep21非作者源文、actual owner与写后通过；新增六项由root亲读必要源文、实际owner和六处正文/邻接，source→owner及actual-write-after均通过。Flux仅落实Fabric局部机制，没有开展或宣称全章顺读Refine。

### [Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient Diffusion LLMs](https://arxiv.org/abs/2609.26796v1)

刷新 query、cache 写回与双 mask 验证共同决定 IO 计划。采用版本 v1；[证据笔记 §4.1](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的实际差额。已落实两段，`sep21_resume_v3` 已实读正文与邻接通过，日级复核仍待。

### [HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing](https://arxiv.org/abs/2609.26368v1)

FA-source 重投影与 inner reuse 是不同缓存域，早退出依赖训练结构。采用版本 v1；[证据笔记 §4.2](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) 的实际差额。已落实两段，`sep21_resume_v3` 已实读正文与邻接通过，日级复核仍待。

### [Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)

实时语音、foreground call 与 delegated task 的取消生命周期分离。采用版本 v1；[证据笔记 §4.20](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [Rethinking Length-Based Training: Batch Composition and Loss Normalization in Speech Token Language Models](https://arxiv.org/abs/2609.25890v1)

匹配 exposure 后 batch composition/loss normalization 决定首 epoch 收益。采用版本 v1；[证据笔记 §4.9](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [LatentPort: Beyond KV Cache - Cross-Model Transfer of Recurrent Memory in Hybrid Language Models: A 4B-to-9B Hybrid-State Handoff Without Target Prefix Replay](https://arxiv.org/abs/2609.25053v1)

hybrid 跨模型 handoff 必须处理 recurrent matrix、conv history 和初始化语义。采用版本 v1；[证据笔记 §4.5](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [Prompt Breadth and Rollout Refresh Interact in On-Policy Distillation](https://arxiv.org/abs/2609.25048v1)

prompt breadth 的收益与 rollout refresh、token 预算交互。采用版本 v1；[证据笔记 §4.8](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `TRAIN-DPO` [Ch34](../../../../books/part-04-training-system/34-dpo.md) 的实际差额。作者提案仅报告，保留受限结果与失败条件；不重述已有长期原则，待非作者终判。

### [Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation](https://arxiv.org/abs/2609.26693v1)

before-dispatch 拒绝、transport 身份与 turn/task 分母必须分账。采用版本 v1；[证据笔记 §4.10](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [Greedy Decoding Is Not Precision-Invariant: Cross-Precision Output Divergence in LLM Inference](https://arxiv.org/abs/2609.26621v1)

greedy top-two margin 决定受限 FP32 head scope，扩大 scope 不单调改善。采用版本 v1；[证据笔记 §4.16](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [Disaggregated Quantization: Specializing LLM Prefill and Decode](https://arxiv.org/abs/2609.26333v1)

P/D 权重精度可分工，但交接 KV 的数值/语义兼容不可省略。采用版本 v1；[证据笔记 §4.6](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [Component Type, Not Reconstruction Error, Predicts Attention Quantization Sensitivity](https://arxiv.org/abs/2609.26173v1)

单 projection reconstruction 排序不认证任务敏感度或全 mixed-bit 收益。采用版本 v1；[证据笔记 §4.14](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的实际差额。作者核定现有正文已承载该判断；不为制造 diff 新增，待非作者确认具体覆盖。

### [Terminal Shrinkage Averaging Reveals a Schedule-Estimator Interaction in LLM Pretraining](https://arxiv.org/abs/2609.25482v1)

终态 averaging/shrinkage estimator 与学习率 schedule 共同定义输出。采用版本 v1；[证据笔记 §4.16](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `TRAIN-PRETRAINING` [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo](https://arxiv.org/abs/2609.25451v1)

GPU 模型分配寿命可脱离 engine，但 pretraffic shadow 不保请求进度。采用版本 v1；[证据笔记 §4.3](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-DYNAMO` [Ch52](../../../../books/part-05-inference-system/52-dynamo.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [Flux: Optimal Scheduling of Optical Circuit Switches for LLM Training](https://arxiv.org/abs/2609.25949v1)

iteration DAG readiness 与电路延续联合调度，少重配不等最短执行。采用版本 v1；[证据笔记 §4.20](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [Decoupling Logical Masks from GPU Execution for Dynamic Block-Sparse Attention](https://arxiv.org/abs/2609.25869v1)

logical mask 不变的 retile 与 offline eligibility portfolio 分开，kernel 最快不等 request 最快。采用版本 v1；[证据笔记 §4.4](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [SARA: SLO-Aware Resource Allocation for Disaggregated Agentic LLM Services](https://arxiv.org/abs/2609.26763v1)

tail-resource 模型依赖队列/分位假设，单调成本不能推出唯一全局最优。采用版本 v1；[证据笔记 §4.16](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 的实际差额。仅保留有界方法/条件结果；不采用 printed 中央最优保证，不写 Books，定点重开条件见§5。

### [WeightBridge: An Efficient Weight Transfer Library for Reinforcement Learning](https://arxiv.org/abs/2609.25442v1)

trainer→rollout layout plan 去冗余与 balancing 不等 publication 原子性。采用版本 v1；[证据笔记 §4.7](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy](https://arxiv.org/abs/2609.26467v1)

phase ownership 切换须作废未执行 chunk suffix，并重新取得当前 observation。采用版本 v1；[证据笔记 §4.18](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?](https://arxiv.org/abs/2609.26292v1)

视觉稳健与物理参数稳健不同，planner 可行筛选改变评价分母。采用版本 v1；[证据笔记 §4.18](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MULTIMODAL-EMBODIED-VLA` [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 的实际差额。作者核定现有正文已承载该判断；不为制造 diff 新增，待非作者确认具体覆盖。

### [PatchKV: Efficient KV Cache Recovery for Dynamically Edited LLM Contexts](https://arxiv.org/abs/2609.26219v1)

先冻结 repair/reuse 集合，再分配 precision，importance 不拥有有效性裁决。采用版本 v1；[证据笔记 §4.11](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [CoVeR: Coverage-Based Routing of Verifier Calls in Agentic Retrieval](https://arxiv.org/abs/2609.26086v1)

cheap uncovered margin 只能 defer costly decider、继续搜索，不直接停止。采用版本 v1；[证据笔记 §4.14](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [MemoryAthena: Adaptive Routing over Latent and Generated Memories](https://arxiv.org/abs/2609.25853v1)

direct Engram residual 与两路生成表示分权，likelihood router 不认证真值。采用版本 v1；[证据笔记 §4.12](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md) 的实际差额。该窄差额已按root授权实际写入，sep21已逐项核正文及邻接通过；采用条件、成本、反例与原路径保留。日级Gate另待整体完成。

### [CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents](https://arxiv.org/abs/2609.26779v1)

只 compact 当前 live window 可减少递归影响，但明确丢弃旧 recall。采用版本 v1；[证据笔记 §4.14](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `AGENT-CONTEXT` [Ch75](../../../../books/part-07-agent/75-context.md) 的实际差额。作者提案仅报告，保留受限结果与失败条件；不重述已有长期原则，待非作者终判。

### [Impact Is Not Invalidation: Ask About the Claim, Not the Diff](https://arxiv.org/abs/2609.25130v1)

diff reachability/行为改变不等特定 memory claim 失效，问法也改变判决。采用版本 v1；[证据笔记 §4.17](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [Self-Cleaning and Captured Anyway: One Measured Primitive for Error in a Store an Agent Writes to Itself, and What a Falling Score Actually Measures](https://arxiv.org/abs/2609.25052v1)

单 majority agreement 写入 gate 在高污染时可锁住错误、拒绝真实纠正。采用版本 v1；[证据笔记 §4.17](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [Reading Right, Answering Wrong: How Visual Configuration Changes Affect Evidence Use in VLMs](https://arxiv.org/abs/2609.25770v1)

visual configuration 离散变化与相同配置内 pixel 变化需分别控制。采用版本 v1；[证据笔记 §4.19](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425v2)

query-sensitive quantization 与 K-error 主子空间 logit 补偿分权。采用版本 v2；[证据笔记 §4.20](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [You Only Need 2/3 of the Chosen Experts: An Empirical Study of Dynamic Expert Pruning in Fine-Grained MoE LLMs](https://arxiv.org/abs/2609.25809v1)

静态 reduced-k 与逐token动态专家分配 的差额受 generation/预算协议限定。采用版本 v1；[证据笔记 §4.17](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MODEL-MOE` [Ch21](../../../../books/part-02-model/21-moe.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [Virtual Encoders in Multimodal Transformers](https://arxiv.org/abs/2609.26513v2)

backbone 内感知表示的 formation、readout 与 routing 需分别实证。采用版本 v2；[证据笔记 §4.19](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training](https://arxiv.org/abs/2609.26774v1)

encoder STE、codebook tracking 与分组 LR 是不同优化职责。采用版本 v1；[证据笔记 §4.19](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) 的实际差额。已获非作者source→actual-owner与实际窄写/邻接检查通过；整合差额和限制保留于该owner正文，不外推实验保证。

### [FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents](https://arxiv.org/abs/2609.26048v1)

timing-matched sham 将规则内容与仅中断效果分离。采用版本 v1；[证据笔记 §4.21](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `AGENT-PLATFORM` [Ch84](../../../../books/part-07-agent/84-agent-platform.md) 的实际差额。已完成必要原文深入审阅、实际owner差额与root窄锁写入；sep21非作者source→owner及实际正文/邻接写后通过。

### [Certified Against Which Oracle? Execution Labels Set the Reported Risk of Conformal Abstention for Text-to-SQL](https://arxiv.org/abs/2609.25938v1)

oracle-relative certificate 与独立语义标签风险不同。采用版本 v1；[证据笔记 §4.21](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的实际差额。已完成必要原文深入审阅、实际owner差额与root窄锁写入；sep21非作者source→owner及实际正文/邻接写后通过。

### [Auditing Proxy-Based Validation Across Text Spans](https://arxiv.org/abs/2609.25808v1)

same-span proxy agreement 可能由共享表面信号而非 construct validation 驱动。采用版本 v1；[证据笔记 §4.21](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的实际差额。已完成必要原文深入审阅、实际owner差额与root窄锁写入；sep21非作者source→owner及实际正文/邻接写后通过。

### [Slow Decay and Silenced Expression: Iterated Subliminal Trait Transfer in Language-Model Lineages](https://arxiv.org/abs/2609.25721v1)

表达消失与跨代 trait 清除不同，probe/steering 也不认证内部真值。采用版本 v1；[证据笔记 §4.21](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `TRAIN-SFT` [Ch29](../../../../books/part-04-training-system/29-sft.md) 的实际差额。已完成必要原文深入审阅、实际owner差额与root窄锁写入；sep21非作者source→owner及实际正文/邻接写后通过。

### [MICRO: Multi-Fidelity Active Search for Severe Error Discovery](https://arxiv.org/abs/2609.26025v1)

便宜 rating 只能指导预算搜索，确认 severe error 仍需高保真 annotation。采用版本 v1；[证据笔记 §4.21](../_sources/daily-20260923/date-recovery-review.md) 记录必要方法、关键对照、反证与 `PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的实际差额。已完成必要原文深入审阅、实际owner差额与root窄锁写入；sep21非作者source→owner及实际正文/邻接写后通过。

### [The Sirens' Song: When Proximal Background Context Overshadows Distant Evidence](https://arxiv.org/abs/2609.26718v1)

固定位置的背景竞争与距离效应分开，score整形仅在条件满足时改善。§2–3的简化竞争式与归一化QK/t映射不证明普遍距离衰减或原dot-product语义不变；§4仅末block微调且比较训练未全匹配，部分任务及较大κ反退，分析FLOPs不等实机延迟。采用精确v1；[必要证据 §4.23](../_sources/daily-20260923/date-recovery-review.md)保存核心方法、评价、关键反证与实际`MODEL-LONG-CONTEXT` [Ch22](../../../../books/part-02-model/22-long-context.md)差额。公开归属复用官方Wed23 New与公告时刻联合依据，不用Submitted替代first-public。长期缺口使受影响内容深入完成；已按root source→actual-owner通过及窄锁实际写入两段，root已实读正文/邻接写后通过；保上述必要边界，日级Gate另待。

### [Train Where the Quantized Model Goes: On-Policy Distillation for Low-Bit Reasoning](https://arxiv.org/abs/2609.26708v1)

目标量化forward产生的student prefix须进入恢复训练分布。§3–6由量化student rollout、同prefix冻结teacher及verifier共同训练，不把BF16 master更新误当BF16 rollout；匹配steps/samples不等FLOPs/最终质量，追加OPD成本不等全pipeline免费，个别代码/QA仍反退。采用精确v1；[必要证据 §4.23](../_sources/daily-20260923/date-recovery-review.md)保存核心方法、评价、关键反证与实际`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)差额。公开归属复用官方Wed23 New与公告时刻联合依据，不用Submitted替代first-public。长期缺口使受影响内容深入完成；已按root source→actual-owner通过及窄锁实际写入两段，root已实读正文/邻接写后通过；保上述必要边界，日级Gate另待。

### [When Recursive Models Finish Computing](https://arxiv.org/abs/2609.26487v1)

实际轨迹方向稳定与全空间Jacobian扰动稳定不能互相替代。§2–3的实际update方向收缩可以与谱范数大于1共存；首次exact-solve是离线对齐，累计曾正确不等终态正确或未知答案停止许可。有限512步/少量Sudoku checkpoint不证明无限收敛，MLP扰动尚未完全吸收。采用精确v1；[必要证据 §4.23](../_sources/daily-20260923/date-recovery-review.md)保存核心方法、评价、关键反证与实际`MODEL-TRANSFORMER-LAYER` [Ch17](../../../../books/part-02-model/17-transformer-layer.md)差额。公开归属复用官方Wed23 New与公告时刻联合依据，不用Submitted替代first-public。长期缺口使受影响内容深入完成；已按root source→actual-owner通过及窄锁实际写入两段，root已实读正文/邻接写后通过；保上述必要边界，日级Gate另待。

### [CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](https://arxiv.org/abs/2609.26300v1)

exact-block selector须按下游tail补偿残余而不只attentionmass排序。§3–4的二阶KL残余排序要求固定块上界及块内logit方差趋零，分组估计还忽略跨坐标协方差；full KV仍在CPU，tail合并要等event。AppE2是QKV已就绪后的单层attention计时，含选择/搬运/合并但排除prefill/projection/MLP，不等请求SLO，任务质量仍可退步。采用精确v1；[必要证据 §4.23](../_sources/daily-20260923/date-recovery-review.md)保存核心方法、评价、关键反证与实际`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)差额。公开归属复用官方Wed23 New与公告时刻联合依据，不用Submitted替代first-public。长期缺口使受影响内容深入完成；已按root source→actual-owner通过及窄锁实际写入两段，root已实读正文/邻接写后通过；保上述必要边界，日级Gate另待。

### [PACE-dLLM: Elastic Block Decoding via Confidence Cliff Estimation for Diffusion Language Models](https://arxiv.org/abs/2609.26249v1)

lookahead horizon与实际commit threshold分权，饱和yield oracle不等runtime最优。§4的当前confidence cliff拟合仅提出lookahead，连续prefix cursor与散点commit不同；定理约束eligibility概率/截断yield而不是raw confidence真值或实机最优。退化拟合要回退，单H100/batch1/L512且部分KV优化关闭的对照不能外推所有长度或完整stack。采用精确v1；[必要证据 §4.23](../_sources/daily-20260923/date-recovery-review.md)保存核心方法、评价、关键反证与实际`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)差额。公开归属复用官方Wed23 New与公告时刻联合依据，不用Submitted替代first-public。长期缺口使受影响内容深入完成；已按root source→actual-owner通过及窄锁实际写入两段，root已实读正文/邻接写后通过；保上述必要边界，日级Gate另待。

### [Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation](https://arxiv.org/abs/2609.26182v1)

旧模态保留须实际绕过新adapter算术，gate入口与重算scope构成条件。§3/4要求关闭gate在adapter算术前返回、保持原weights/precision/kernel/order/batch；thermal相同RGB字节由encode入口声明scope，不是自动内容识别，checkpoint重算也须同gate。Table6每模态一个输入不认证并发隔离，多gate同forward未测；gate-open质量仍可反退。采用精确v1；[必要证据 §4.23](../_sources/daily-20260923/date-recovery-review.md)保存核心方法、评价、关键反证与实际`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)差额。公开归属复用官方Wed23 New与公告时刻联合依据，不用Submitted替代first-public。长期缺口使受影响内容深入完成；已按root source→actual-owner通过及窄锁实际写入两段，root已实读正文/邻接写后通过；保上述必要边界，日级Gate另待。

## 5. 缺口与下一步

以下外部限制均为本窗终态保留项：不用于正面证据、Books或无遗漏断言；定点重开条件逐项列在下方。

- 普通可执行工作：候选必要审阅、Books处置/实写/逐项写后和全日非作者复核均已完成，剩余0。原34/29处与新增6/6处有效独立结果复用；下列来源、日期和中央争议作为明确隔离的本窗保留项存在，不支持正面采用或无遗漏断言。
- [TopoCompress26061v1](https://arxiv.org/abs/2609.26061v1)题摘贡献独立校准通过，但仅合同Cross、primarycs.NI recent已滚动，monthly只证identity159号；Submitted August不证公开日，窗后v2不采用。本次隔离具体first-public归属，不计候选/评分/Books；取得原始primary公告或可信首公开日期后只重开该identity。
- [ReDraft16639v3](https://arxiv.org/abs/2609.16639v3)具体事件隔离：exact-v2官方仍withdrawn/comment作者不同意，current abs为v3正文；exact-v3 abs有限缓存miss、current abs成功与recent无此ID，尚无本窗Replacement公告/正式修订授权说明。不以submitted伪造公开、不从当前正文复活v1；v2不候选/评分/Books，v3日期/恢复边界齐后只重开该事件。其他有效证据保留。
- SARA [26763v1](https://arxiv.org/html/2609.26763v1)printed中央争议：§VI-D Eq58的单调非增成本不能推出唯一全局最优，整数资源/等成本分配反例与阶段分位≠joint分位须保留。重开仅需修正定理/条件与具体反例；不据此采用普遍最优、生产tail或改Books，其他有界实验不被全盘否定。
- 日期保留项：Opus5.5/card、Astra card、MiMoV2.6、ZCode只有跨边界09-22日级日期；获官方发布时间或可信历史公告后仅重开该身份。不评分、不写Books，不用sitemap更新时间当首公开。
- 来源保留项：Google publications、Qwen动态Research、Z.ai动态Research的官方目录/有界替代仍没有可核的日级终点；原访问证据保留，不支持全站零命中或无遗漏。获官方日期列表/API/RSS/归档后定点恢复。Hunyuan第9条身份已由root核为旧2608.29296v1、无September revision，网页display/publicAt不新计family。
- 窗外材料：旧38与旧具名DateHold/理论/首发/修订线索已由09/22 reconciliation owner处理；[09/22正文](../22/README.md)及年级旧附件保留，本日不再次筛选/评分。HBF25782与更早IEEE LCA家族去重，只保留真实日期恢复线索。

## 6. 复核

复核者：`sep21_resume_v3`（本日非作者，原34项必要证据、处置与29处写后、七题摘校准及两项arXiv隔离）；`root`（非作者，新增六必要原文、owner与六处正文及邻接写后，并完成最终日级复核）。

结论：通过

root实际核对14个每日来源的入口、主题边界与停止范围，十二类New/Cross分组、首公开迁回与修订/撤回隔离，正式40行和40项证据、35/2/2/1处置及35处实际写后记录。复用的逐项证据身份、版本和采用命题未变化，不复审无关附件。具名负侧定点核了26662、25697、25040完整摘要和26502原始题摘：临床结果、领域适配和暂缓AI for Science没有被误作新的大模型系统机制；并核HBF较早家族、机构版本包装与日期保留项的关闭依据。其他宽库存没有被宣称全部全文独立审阅。SARA中央争议、Topo/ReDraft事件、四项机构日期和三个目录限制均有精确重开条件，不用于Books、正面保证或无遗漏声明。普通工作为0，完成表示本窗安全终态，不表示这些保留项已经获得证明。实际范围见[单一恢复笔记§4.24](../_sources/daily-20260923/date-recovery-review.md)。

V3格式/一致性、本地链接及本日改动的限定差异检查通过；机器检查不替代以上语义判断，未复现实验或验证生产SLO，未stage、commit或push。
