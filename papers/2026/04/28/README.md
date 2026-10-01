# Daily Research — 2026-04-28

**规范：** V3
**窗口：** 2026-04-27T09:00:00+08:00 ～ 2026-04-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-30T18:51:29+08:00

## 1. 结论

本日按当前 V3 独立重建，71 个候选身份已经逐项裁决：45 整合、15 已有覆盖、7 仅报告、4 中心争议终态暂缓；52 深入完成、15 标准完成，争议另列。原宽列表、旧 retained、入库/提交日期均不作为分母；155 条完整题摘读后保留线索，经必要 exact-v1、具体 owner 与非作者双向校准收束。[最终矩阵](../_sources/daily-20260428/V3_FINAL_DECISION_MATRIX.md)和[非作者有限全矩阵复核](../_sources/daily-20260428/V3_APR24_FINITE_INDEPENDENT.md)可追溯误关恢复及具名关闭。关键知识差额跨模型/训练/推理/Agent 的状态身份与交接、估计对象和实际结果分母；所有整合已实际写入并通过非作者写后。五个机构来源历史入口受阻具名隔离，不称机构零命中。[非作者日级终审](../_sources/daily-20260428/V3_APR24_INDEPENDENT_FINAL_REVIEW.md)已通过，普通可执行工作为0；完成不代表外部来源或争议强主张得到证明。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 官方 News RSS 本窗四条按原文具体范围关闭；Research/Publication sitemap 可列 52/200 个 URL，但单篇直取遇 403 challenge，见[有界停点](../_sources/daily-20260428/V3_REVIEW_CHECKPOINT.md#题摘与证据审阅-checkpoint续) | 受阻 | Sitemap `lastmod` 非首发、两表有交集且无可靠本窗日期停点；待官方单篇首发字段或可分页目录恢复后定点补查，不称机构零原始命中 |
| SRC-ANTHROPIC | Research 官方 `publishedOn` 04/22 两项→04/29 一项，跨本窗无列项 | 已检查 | 仅当前官方 Research 可见列表，不含作者全部投稿 |
| SRC-GOOGLE-AI | DeepMind 04/27 韩国合作按 AI for Science 及机构合作范围关闭；[DeepMind Publications](https://deepmind.google/research/publications/) 总264、首屏25日期从09/01倒序到2025/10，04/25→04/23→04/22跨本窗无可见条目；[Google Research April Blog 官方月页](https://research.google/blog/2026/04/)九条日期从04/29直接到04/22，本窗无列项；见[有界补项](../_sources/daily-20260428/V3_REVIEW_CHECKPOINT.md) | 受阻 | [Google Research Publications](https://research.google/pubs/) 约11555条、2026过滤计数360，但当前15条首页按年非本窗日排序，尚无可停在04/27–28的历史日期页；DeepMind子目录和Blog不能代替其全部原稿，恢复可按日期检索的官方目录后定点核 |
| SRC-META-AI | 官方 Blog 可见段从 04/08→06/29 跨本窗无列项；Research 首页当前空正文，近 1975 条 Publications 首屏不能代表历史；见[第三批机构停点](../_sources/daily-20260428/V3_REVIEW_CHECKPOINT.md) | 受阻 | Publications 历史分页尚无确定停点；不能称机构零命中 |
| SRC-QWEN | 已核官方 Research 动态 40 项与静态 60 项：04/22 10:00+08 后的 FlashQLA 为 04/28 10:00+08，晚于本窗截止；详见[机构停点](../_sources/daily-20260428/V3_REVIEW_CHECKPOINT.md#每日机构来源首批有界检查2026-09-28-0725-北京时间前) | 已检查 | 仅代表官网可见 Research 列表，不代表作者稿全网零命中 |
| SRC-DEEPSEEK | 官方 News 04/24→09/10、Research Index 02/25→06/24 均跨本窗；V4 模型卡印 04/27 Publication、04/24 Updated/Release，但无首发小时且未披露独立新机制；该版本线索已按贡献范围关闭 | 已检查 | 仅官网可见目录；模型卡不能支持本窗独立新版本事实，不把 06/24 正式论文回填 |
| SRC-MOONSHOT | Kimi CLI release 官方目录1.39.0=04/24T06Z→1.40.0=04/28T13:51Z，跨本窗无release；[Kimi Platform Blog](https://platform.kimi.com/blog) 当前可见26条仅从2025/11/07至2024/05/29，不能以旧目录顶项推2026无发布 | 受阻 | Blog缺可回溯2026的官方日期目录，待恢复后定点核本窗；不重翻同一静态页，也不将CLI层零发布外推机构零研究 |
| SRC-TENCENT-HUNYUAN | 官网“全部”接口 total 9/list 9，04/30→04/23 跨本窗无列项；官方组织新仓库创建页 05/06→04/29→04/22 无本窗命中，定点 Hy3-preview release=0；见[仓库层停点](../_sources/daily-20260428/V3_REVIEW_CHECKPOINT.md#官方仓库重要发布层的有界补检2026-09-28) | 已检查 | 本次有界官网目录、新仓库和选定重要 release 层无可见当窗事件；未逐一检查所有已有仓库，亦不表示全部作者稿零命中 |
| SRC-ZAI | 智谱 Research 04/29《Scaling Pain》→04/07《GLM-5.1》；[官方 New Released](https://docs.z.ai/release-notes/new-released) 06/16 GLM-5.2→04/07 GLM-5.1，均跨本窗；官方组织新仓库最近两项 04/28T10:33Z/12:32Z 均晚于截止，GLM-5 release=0 | 已检查 | 本次研究目录、官方模型发布说明和选定仓库层无可见当窗事件；不代表所有旧仓库或作者原稿均已穷尽 |
| SRC-BYTEDANCE-SEED | Publications 第 20～39 项由 04/29→04/25 跨本窗，Blog 首页 04/22T16Z→04/08T16Z；官方组织新仓库 05/06→04/23，Seed2.0 release=0 | 已检查 | 本次两个官网目录和选定重要仓库发布层无可见当窗事件；不替代其他作者稿或所有旧仓库发布 |
| SRC-BAIDU-ERNIE | 官方中文 Blog 首页 04/30→04/15 跨本窗；PaddlePaddle 新仓库 05/14→02/11、ERNIE 唯一正式 release 2025-06-30 | 已检查 | 所见 Blog 与 ERNIE 发布层无本窗项，不代表全部作者 arXiv 稿零命中 |
| SRC-XIAOMI-MIMO | 官网 Paper 列表 06/29→03/13 跨本窗；官方组织全部 18 新仓库与 MiMo-Skills release=0 均无本窗项 | 受阻 | Blog 卡片缺可核的首发日期，必要日期材料不能判本窗；仅 Paper/新仓库/所选 release 可作有界停点。待官方单篇 timestamp/历史目录或可信原始公告恢复后补判，不据此宣称 Blog 零命中 |
| SRC-MINIMAX | 中文 Blog 命中 Agent Team 一篇，中文 JSON-LD 04/27T12Z 而英文对应页 05/27T00Z；读核心正文后以前分母理由关闭。Agent Tech Blog 索引仅重复该家族；CLI release 本窗零 | 已检查 | 同家族官方语言页日期冲突，不用它证明首次公开；当前可见 Blog/Tech Blog/CLI 入口以外的作者稿不作零遗漏断言 |
| SRC-ARXIV | 官方公告时钟、相邻连续 ID `.22753 / .22754–.24764 / .24765`、04/28 OAI 与实际 v1 处理簇联合支持本批 08～09 的有界推断；十二分类 1,229 行/845 去重身份按模型/多模态/训练/推理/平台/Agent 主题浏览，旧排除 834 标题全览、44 完整摘要反向查漏、3 分类新线索均已具名消歧；见[页段停点](../_sources/daily-20260428/V3_ARXIV_OFFICIAL_CATEGORY_TITLE_CHECK.md)及[日期边界](../_sources/daily-20260428/V3_BOUNDED_PUBLICATION_RESOLUTION.md) | 已检查 | 推断不是逐篇秒级公开日志，晚 Updated 不自动迁窗，早字段也不单证首发。仅约定主题/入口已处理，不声称全学科召回；新发现更早正文、延期/撤回或批次反证只重开受影响身份 |

## 3. 候选与判断

本窗候选分母冻结为 71 个唯一 arXiv exact-v1 身份。其准入不是主题映射或旧表复刻：原 13 个已认可子集加 65 个逐条提案，扣除 7 个具体前分母关闭；负侧另恢复 24542/24579，22985 由主题 Existing 改仅报告，23747 的确切纠错差额落实为整合。每项都有必要原文/反证、审阅状态和实际 Books 终判；公开归属统一是公告槽、连续身份/OAI/v1 处理组合支持的 08～09 有界推断，不是逐篇秒级日志。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [2604.22782v1 Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing](https://arxiv.org/html/2604.22782v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 训练随机跨层 K/V 来源以适配部署确定留存集合，2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，非作者实际写后通过 |
| [2604.22783v1 Parameter Efficiency Is Not Memory Efficiency: Rethinking Fine-Tuning for On-Device LLM Adaptation](https://arxiv.org/html/2604.22783v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | adapter-specific 激活按序列汇聚后低秩更新，基座激活仍随长度增长，2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，非作者实际写后通过 |
| [2604.23467v1 Hybrid JIT–CUDA Graph Optimization for Low-Latency Large Language Model Inference](https://arxiv.org/html/2604.23467v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | graph miss 本次 JIT 执行、异步 capture 后供同 shape replay，2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，非作者实际写后通过 |
| [2604.23073v1 RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/html/2604.23073v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 冻结 VLA 的 RL token 状态接口与小型在线 actor–critic 动作细化，2+2+2=6 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)；非作者必要 source→body 与日期有界复核通过 |
| [2604.22981v1 Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling](https://arxiv.org/html/2604.22981v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 前缀 reward 的条件终局期望代理与 MC/TD 一致性，2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-PPO [Ch32](../../../../books/part-04-training-system/32-ppo.md)；非作者正文及日期有限复核通过 |
| [2604.23036v1 Preserving Long-Tailed Expert Information in Mixture-of-Experts Tuning](https://arxiv.org/html/2604.23036v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 低频 expert 与 always-active condenser 分担梯度饥饿，2+1+2=5 | 标准完成 | 已有覆盖：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)；非作者正文及日期有限复核通过 |
| [2604.23080v1 Usable Agent Discovery for Decentralized AI Systems](https://arxiv.org/html/2604.23080v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | node churn 与 agent readiness 分离并比较 overlay 维护代价，2+1+2=5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md)；非作者正文及日期有限复核通过 |
| [2604.23205v1 Tessera: Secure, Near-Line-Rate Weight Streaming for UMA Edge Accelerators](https://arxiv.org/html/2604.23205v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 64B burst 内联解密与隔离 SRAM 的权重明文边界，2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；非作者正文及日期有限复核通过 |
| [2604.23108v1 Mixture of Heterogeneous Grouped Experts for Language Modeling](https://arxiv.org/html/2604.23108v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 异宽 expert 分组/组内路由与全尺寸静态设备布局分权，2+2+2=6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)；root 实际写后通过 |
| [2604.23150v1 Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns](https://arxiv.org/html/2604.23150v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 历史 decode 请求簇条件化 device group 与 expert placement，2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；root 实际写后通过 |
| [2604.23577v1 RouteNLP: Closed-Loop LLM Routing with Conformal Cascading and Distillation Co-Optimization](https://arxiv.org/html/2604.23577v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 升级失败簇定向蒸馏后联合重训 router/重校阈值，2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)；root 实际写后通过 |
| [2604.23051v1 Evaluating Temporal Consistency in Multi-Turn Language Models](https://arxiv.org/html/2604.23051v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 正确事实库之外的 conversation-scope carryover/override/cross-entity 分母，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)；root 实际写后通过 |
| [2604.24618v1 Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/html/2604.24618v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 自发破坏机会与已构造破坏历史的条件续写不能共用风险分母，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，apr24_close 核必要 primary 与实际写后通过 |
| [2604.23121v1 Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training](https://arxiv.org/html/2604.23121v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 低数据视觉 grounding 保留与每去噪步双条件 velocity 引导分担职责，2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际已写，独立写后通过 |
| [2604.23333v1 Process Supervision of Confidence Margin for Calibrated LLM Reasoning](https://arxiv.org/html/2604.23333v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 可解性 probe BCE 与 policy 相对 confidence-margin 是不同优化目标，2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际已写，独立写后通过 |
| [2604.24447v1 Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://arxiv.org/html/2604.24447v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 同 cycle 旧 observation KV 仅接去噪早步、fresh KV 必须接晚步，2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际已写，独立写后通过 |
| [2604.23318v1 Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance](https://arxiv.org/html/2604.23318v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 同题正误 hidden-state span 距离作 credit sensor，不是因果错误定位，2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际已写，独立写后通过 |
| [2604.24003v1 Stabilizing Efficient Reasoning with Step-Level Advantage Selection](https://arxiv.org/html/2604.24003v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 短窗截断混杂与正/负 rollout 的双分支 confidence mask，2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际已写，独立写后通过 |
| [2604.24005v1 TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/html/2604.24005v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | student prefix 扩展与 teacher 成功 prefix 导航形成不同采样/监督支持域，2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际已写，独立写后通过 |
| [2604.24391v1 FreqCache: Accelerating Embodied VLN Models with Adaptive Frequency-Guided Token Caching](https://arxiv.org/html/2604.24391v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 视角位移映射后才复用视觉 token，新视野/关键边缘强制刷新，2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，实际已写，独立写后通过 |
| [2604.23838v1 JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training](https://arxiv.org/html/2604.23838v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 跨不同 pipeline multiplex 与同 pipeline DP-tail migration 分开，2+2+2=6 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，实际已写，独立写后通过 |
| [2604.24008v1 Coverage-Based Calibration for Post-Training Quantization via Weighted Set Cover over Outlier Channels](https://arxiv.org/html/2604.24008v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 固定候选池内选互补 sample 的 weighted channel coverage 不同 channel scale，2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际已写，独立写后通过 |
| [2604.24013v1 FlashOverlap: Minimizing Tail Latency in Communication Overlap for Distributed LLM Training](https://arxiv.org/html/2604.24013v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | AG 本地先算与 RS 外送 partial 先算形成不同依赖顺序，2+1+2=5 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，实际已写，独立写后通过 |
| [2604.23374v1 Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents](https://arxiv.org/html/2604.23374v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | memory read 恢复 lineage 与 sink 显式传播/隐式控制审计分开，2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际已写，独立写后通过 |
| [2604.23459v1 Architecture Matters for Multi-Agent Security](https://arxiv.org/html/2604.23459v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 架构安全的分阶段恶意结果与 benign utility 双机会集，2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际已写，独立写后通过 |
| [2604.23711v1 Spore: Efficient and Training-Free Privacy Extraction Attack on LLMs via Inference-Time Hybrid Probing](https://arxiv.org/html/2604.23711v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | inference-context secret 与黑盒候选枚举/灰盒 logprobs 的观测权限分开，2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) observable channels/observer permission 与隐藏 trace/context 发布边界 |
| [2604.23781v1 ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents](https://arxiv.org/html/2604.23781v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 外生 loud/silent mutation 与 weighted progress/strict all-checker 分母，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Living-world/ClawMark temporal 合同 |
| [2604.22879v1 Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems](https://arxiv.org/html/2604.22879v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 各域私图不汇总、远端 predicate 与 sink authorization 分权，但信息泄漏证明缺桥，2+2+2=6 | 争议 | 暂缓：PLATFORM-SECURITY，中心 Shannon 1bit 保证隔离，不进入 Books；重开需求见 §5 |
| [2604.22888v1 RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents](https://arxiv.org/html/2604.22888v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 白盒 Skill pre-screen 的 response-conditioned sensor 与 effect 保证不同、核心 F1 不自洽，2+1+2=5 | 争议 | 暂缓：PLATFORM-SECURITY，正面 detector 优势及 Books 采用隔离；重开需求见 §5 |
| [2604.23584v1 Identity-Decoupled Anonymization for Visual Evidence in Multi-modal Retrieval-Augmented Generation](https://arxiv.org/html/2604.23584v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 检索后身份替换与视觉证据保真分担，但 MI 上界/独立性中心证明有反例，2+2+2=6 | 争议 | 暂缓：PLATFORM-SECURITY，隐私保证与生成证据采用隔离；重开需求见 §5 |
| [2604.24118v1 AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization](https://arxiv.org/html/2604.24118v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 监督者首轮拒绝后的改写 T′ 直接执行，与所有最终 call 经 audit 的强保证冲突，2+1+2=5 | 争议 | 暂缓：PLATFORM-SECURITY，协议潜在反证隔离，非已验证实现漏洞；重开需求见 §5 |
| [2604.22778v1 The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry](https://arxiv.org/html/2604.22778v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 瞬时 rank 与持久谱形分账，匹配奇异值不恢复方向，2+1+2=5 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，已实际窄写，非作者写后通过 |
| [2604.23475v1 Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers](https://arxiv.org/html/2604.23475v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | importance score 与 protected set 是两个 artifact 字段，2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，已实际窄写，非作者写后通过 |
| [2604.23798v1 ELSA: Exact Linear-Scan Attention for Fast and Memory-Light Vision Transformers](https://arxiv.org/html/2604.23798v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | (m,S,W) 实数 monoid 解除归一/合并/重归一，不提供减法逆元，2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，已实际窄写，非作者写后通过 |
| [2604.24040v1 Improving Robustness of Tabular Retrieval via Representational Stability](https://arxiv.org/html/2604.24040v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 同表多 format centroid 离线训练 adapter，线上单 view/query 冻结，2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，已实际窄写，非作者写后通过 |
| [2604.24086v1 AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation](https://arxiv.org/html/2604.24086v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 历史 anchor→当前 ego SE(2)，LiDAR CMDP cost 非已实现 hard veto，2+2+2=6 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，已实际窄写，非作者写后通过 |
| [2604.24622v1 CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies](https://arxiv.org/html/2604.24622v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | learned conditional endpoint 初始化与 single refinement 分担训练/推理责任，2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，已实际窄写，非作者写后通过 |
| [2604.24708v1 Scalable Hyperparameter-Divergent Ensemble Training with Automatic Learning Rate Exploration for Large Models](https://arxiv.org/html/2604.24708v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 不同 θ_r 求梯度但仍每步共享 All-Reduce，再周期参数平均，2+1+2=5 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，已实际窄写，非作者写后通过 |
| [2604.24088v1 TACO: Efficient Communication Compression of Intermediate Tensors for Scalable Tensor-Parallel LLM Training](https://arxiv.org/html/2604.24088v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | pre-RMS α/FWHT/post-absmax s 为不同数值 metadata，2+2+2=6 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，已实际窄写，非作者写后通过 |
| [2604.23434v1 When Does Removing LayerNorm Help? Activation Bounding as a Regime-Dependent Implicit Regularizer](https://arxiv.org/html/2604.23434v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | bounded activation 随 T/P 与架构由 regularizer 转 capacity bottleneck，2+1+2=5 | 深入完成 | 整合：MODEL-TRANSFORMER-LAYER [Ch17](../../../../books/part-02-model/17-transformer-layer.md)，已实际窄写，非作者写后通过 |
| [2604.24432v1 Kwai Summary Attention Technical Report](https://arxiv.org/html/2604.24432v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | chunk direct→summary 完整交接与三段 cache，summary 只能读 own chunk，2+1+2=5 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，已实际窄写，非作者写后通过 |
| [2604.24300v1 ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning](https://arxiv.org/html/2604.24300v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | gold 支持集绑定 actual 16/32/64 frames 而非完整视频标注，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.24608v1 Learning to Route Queries to Heads for Attention-based Re-ranking with Large Language Models](https://arxiv.org/html/2604.24608v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 离线 per-query subset label→query router，与训练后 static head 区别，2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，已实际窄写，非作者写后通过 |
| [2604.23321v1 MMEB-V3: Measuring the Performance Gaps of Omni-Modality Embedding Models](https://arxiv.org/html/2604.23321v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | target-modality admissibility 与 semantic rank 分开，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.22891v1 Quantifying and Mitigating Self-Preference Bias of LLM Judges](https://arxiv.org/html/2604.22891v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 高 contrast 判别、近等质 self-PIR、第三方 Null-PIR 三对象，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.23099v1 ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation](https://arxiv.org/html/2604.23099v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 总体积分 S 与失败集合 Xλ 是不同 estimand，2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.22937v1 AutoPyVerifier: Learning Compact Executable Verifiers for Large Language Model Outputs](https://arxiv.org/html/2604.22937v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | dev FP/FN 驱动 checker ADD/REMOVE/REPLACE，冻结后 held-out 准入，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.23455v1 CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend](https://arxiv.org/html/2604.23455v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 前端 symptom→backend fault 绑定同一 incident/tool/提交，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.24401v1 All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation](https://arxiv.org/html/2604.24401v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | None/fragment/full+TB 同题分层，FS/XS 只在 AN 内，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.23488v1 Do Synthetic Trajectories Reflect Real Reward Hacking? A Systematic Study on Monitoring In-the-Wild Hacking in Code Generation](https://arxiv.org/html/2604.23488v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 训练来源×验收来源双轴，人工冲突 tests/resample 非自然部署作弊，2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，已实际窄写，非作者写后通过 |
| [2604.22785v1 CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs](https://arxiv.org/html/2604.22785v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | competition propensity/缺失反馈与 collaboration counterfactual/不可归因效应分开，2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，已实际窄写，非作者写后通过 |
| [2604.23283v1 Revisable by Design: A Theory of Streaming LLM Agent Execution](https://arxiv.org/html/2604.23283v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | §4–6 earliest incompatible K/X 决定受控 rollback frontier，world effect 需 compensation 非 undo，2+1+2=5 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)，已实际窄写，非作者写后通过 |
| [2604.23552v1 On the Memorization of Consistency Distillation for Diffusion Models](https://arxiv.org/html/2604.23552v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | §3–5 teacher 初始化不保证 distill 后 near-copy 不变，2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，已实际窄写，非作者写后通过 |
| [2604.23994v1 When to Commit? Towards Variable-Size Self-Contained Blocks for Discrete Diffusion Language Models](https://arxiv.org/html/2604.23994v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | §3–5 NF/FA 用同模型 candidate future 比较分布，并非真实未来，2+1+2=5 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，已实际窄写，非作者写后通过 |
| [2604.24222v1 MEMCoder: Multi-dimensional Evolving Memory for Private-Library-Oriented Code Generation](https://arxiv.org/html/2604.24222v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 跨 API task guideline 与单 API 参数边界 guideline 分开，Reflector Discard/Delete/Add 与权重非 FIFO，2+1+2=5 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)，已实际窄写，非作者写后通过 |
| [2604.22985v1 Uncertainty Quantification for LLM Function-Calling](https://arxiv.org/html/2604.22985v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | AST match 是 schema 指标非真实 effect，2+1+2=5 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.23178v1 Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/html/2604.23178v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | style/position 偏差依任务及协议，CoT/swap 非通用缓解。当前 judge 局部比较、prompt/顺序 identity、外部 anchor 与 interval 已承载，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.23581v1 AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking](https://arxiv.org/html/2604.23581v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | DAG root-parent 启发式非因果，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-TRACE [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [2604.23747v1 SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning](https://arxiv.org/html/2604.23747v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | CPU offload 第一 micro 梯度 owner 与 global effective-token normalization 两类坏基线污染 SFT→RL 对照，2+1+2=5 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2604.23853v1 ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation](https://arxiv.org/html/2604.23853v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | actual Ch69 TraceCard:221–239 已写 preserve/prune/repair 与迁移成本，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-TRACE [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [2604.23932v1 MatchRDMA: A Segmented and Rate-Matched Long-Haul RDMA Scheme for Geo-distributed LLM Training over OTN](https://arxiv.org/html/2604.23932v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 长 RTT 分段 credit/pseudoACK/OTN 率匹配改变 transport feedback 不改 destination completion，2+1+2=5 | 标准完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [2604.23950v1 LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models](https://arxiv.org/html/2604.23950v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 早期 visual-self 与晚期 text→vision 信号在不同阶段可用，foreground proxy 非证据 truth。当前信息可见性、sink/diversity与保原token回退已经表达，2+1+2=5 | 标准完成 | 已有覆盖：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.23987v1 Continual Calibration: Coverage Can Collapse Before Accuracy in Lifelong LLM Fine-Tuning](https://arxiv.org/html/2604.23987v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | actual Ch66:118–135 同家族 model update/calibration release transaction 已区分 coverage 与accuracy，2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.24074v1 How Sensitive Are Safety Benchmarks to Judge Configuration Choices?](https://arxiv.org/html/2604.24074v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 12 variants/28,812 verdicts 的同 judge spread 及4.6% parsing failure 不等 target 安全率改变，2+1+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [2604.24594v1 Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/html/2604.24594v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | retrieval、loading、end-task utility 分开，gold present 仍可能不load，2+1+2=5 | 标准完成 | 已有覆盖：AGENT-PLATFORM [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [2604.23210v1 Discovering Agentic Safety Specifications from 1-Bit Danger Signals](https://arxiv.org/html/2604.23210v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 独立 danger oracle→规范的受限对照说明 reward-only 不代表安全，2+1+2=5 | 深入完成 | 仅报告：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [2604.24203v1 Agentic Witnessing: Pragmatic and Scalable TEE-Enabled Privacy-Preserving Auditing](https://arxiv.org/html/2604.24203v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 签名链及模拟 quote/TEE 不保证 corpus 完整或语义正确，2+1+2=5 | 深入完成 | 仅报告：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [2604.24320v1 DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents](https://arxiv.org/html/2604.24320v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 同一 joint rollout ANY成功非独立 trajectory 均值，2+1+2=5 | 标准完成 | 仅报告：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [2604.24763v1 Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://arxiv.org/html/2604.24763v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | encoder-free 与 Tuna-R 同 decoder 不等训练等价，额外 connector stage、理解/生成排序混合。当前 native/shared 表示责任承载，比较应连训练/连接器成本，不以不等数据宣称 encoder 无用。，2+1+2=5 | 标准完成 | 仅报告：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [2604.24542v1 Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models](https://arxiv.org/html/2604.24542v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 全层覆盖与 detector-aware efficacy 的有限取舍，2+1+2=5 | 深入完成 | 仅报告：PLATFORM-SECURITY，不新增通用正文 |
| [2604.24579v1 Measuring the Unmeasurable: Markov Chain Reliability for LLM Agents](https://arxiv.org/html/2604.24579v1) | 2026-04-28T08:00:00+08:00 ～ 2026-04-28T09:00:00+08:00 | 统一 first-passage estimand/fit rejection，2+1+2=5 | 标准完成 | 仅报告：PLATFORM-EVALUATION-SYSTEM，不新增通用正文 |

## 4. 证据与知识整合

有效旧 exact-v1 和审阅记录仅在身份、版本、采用命题及反证未变时复用；[原子集日期与写后材料](../_sources/daily-20260428/V3_FINAL_DECISION_MATRIX.md)、[有界日期组合](../_sources/daily-20260428/V3_BOUNDED_PUBLICATION_RESOLUTION.md)以及[非作者有限复核](../_sources/daily-20260428/V3_APR24_FINITE_INDEPENDENT.md)分开核日期、机制/反证、source→actual owner 与写后相邻衔接。以下 71 段为正式自包含采用边界，非仅把候选移到附件。未复现实验；机器格式通过不替代非作者语义验收。

### [2604.22782v1 Stochastic KV Routing: Enabling Adaptive Depth-Wise Cache Sharing](https://arxiv.org/html/2604.22782v1)

采用命题是训练时随机让 Query 读取本层或更早层 K/V，以便部署时选择确定的留存层集合；缓存集合仍由 runtime 和显存预算决定，不是推理时随机 oracle。作者的 1.7B 训练 loss 有退步，QA 并非全量留存就稳胜固定跨层共享；KV 与延迟数据只来自单卡、batch1、8K 的受测组合，MoE、量化/时间淘汰与生产 SLO 未证。实际写入 [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) 的 trained sharing 分支，保留固定共享与 FullKV 回退。

### [2604.22783v1 Parameter Efficiency Is Not Memory Efficiency: Rethinking Fine-Tuning for On-Device LLM Adaptation](https://arxiv.org/html/2604.22783v1)

区分减少可训练权重与减少反向所需激活：先跨序列汇聚，再在低秩空间更新，使 adapter-specific 中间态从 `O(BSRL)` 指向 `O(BRL)`；基座激活、其他 workspace 和总峰值仍随长度变化。其可训练参数更多且部分质量指标低于 LoRA，固定/可学习汇聚均有 token-local 信息与执行成本；证据限于论文所测 ≤8B 模型。实际写入 [Ch30](../../../../books/part-04-training-system/30-lora.md) 的显存分项论证，普通 LoRA 与 checkpointing 仍是条件性旧路径。

### [2604.23467v1 Hybrid JIT–CUDA Graph Optimization for Low-Latency Large Language Model Inference](https://arxiv.org/html/2604.23467v1)

官方 exact-v1 §III Algorithm 1/§IV–VI 把已知 shape 的预捕获、miss 请求本次 JIT 执行、异步 capture 完成后写入 rolling graph cache 和后续 replay 串为一条生命周期；动态预处理/采样留 JIT，不能把 graph 当任意控制流。相对 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 原有静态 graph 与 persistent executor 分支，新增的是未覆盖 shape 在运行时转成可重放计划的条件选择，并保留首次 capture/显存/事件/淘汰、cuBLAS 可能串行的代价。Table II 的逐 token P99 在 350/500-token 为 18.90/23.68 ms，反而高于 TensorRT-LLM 的 16.53/16.65 ms，故不采用论文“全部长度最低”措辞或多并发整请求 SLO 外推；证据仅绑定单 H100/FP16/LLaMA-2 7B/batch 1/warm-start。root 已完成日期组合、必要原文→owner 及实际正文/相邻交接非作者复核；未复现实验。

### [2604.23073v1 RL Token: Bootstrapping Online RL with Vision-Language-Action Models](https://arxiv.org/html/2604.23073v1)

官方 exact-v1 §IV–VI 的机制不是对整个 VLA 做在线权重更新：先用任务演示适配并训练可读的 RL token，再冻结 VLA 与 token 表示，把它和 VLA 的参考动作交给小型 off-policy actor–critic 作局部动作细化；回放池可含 VLA、在线策略与人工介入轨迹。受测证据只涉及四项真机接触任务、数分钟至数小时练习，不证明开放场景自主学习、控制安全或同预算普遍胜出。[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 现有「Online RL 应通过受限 Action Interface 接入 VLA」已经分开 VLA prior、局部 action head、controller/safety 与人工接管，因此本项 Books 为具体 Existing Coverage，不重复写入。官方 v1 提交字段是 04/24 23:57 UTC 而非首公开时刻；[独立日期审阅](../_sources/daily-20260428/V3_ROOT_23073_DATE_BOUNDARY_INDEPENDENT.md)仅以公告槽、连续 ID 和早处理字段有据推断 arXiv 路径落在本窗 08～09，若找到同族更早公开全文须重开归属。

### [2604.22981v1 Reward Models Are Secretly Value Functions: Temporally Coherent Reward Modeling](https://arxiv.org/html/2604.22981v1)

官方 exact-v1 §4–5、§9 用 lookahead/Monte Carlo 和 TD coherence 正则，让前缀 reward 接近当前 continuation policy 下的终局分数条件期望；作者也明确中间输出并非精确条件期望，更不是过程正确性真值。现有 [Ch32](../../../../books/part-04-training-system/32-ppo.md) 已把 final-only reward、prefix-value proxy、off-policy 漂移与回退放在同一链，故仅作受限 Existing Coverage，不新增同义机制段。

### [2604.23036v1 Preserving Long-Tailed Expert Information in Mixture-of-Experts Tuning](https://arxiv.org/html/2604.23036v1)

官方 exact-v1 §3、§6 让偏置稀疏路由保留低频 expert 的触达，同时以 always-active gated condenser 提供共享通道；后者的数量、常驻容量和梯度集中互有代价，受测 MoE SFT 不证明任意 token 难度识别或同预算普遍胜出。现有 [Ch21](../../../../books/part-02-model/21-moe.md) 已有长尾 expert、路由与共享容量分权及旧 load-balancing 的共存条件，因此窄判 Existing Coverage。

### [2604.23080v1 Usable Agent Discovery for Decentralized AI Systems](https://arxiv.org/html/2604.23080v1)

官方 exact-v1 §3–5 比较 node churn 与 agent warm/cold、Kademlia 的发现成功率和 gossip overlay 的维护/延迟成本；结果来自 SimPy 合成运行，不能外推真实 Agent 可用性或权限安全。[Ch84](../../../../books/part-07-agent/84-agent-platform.md) 的 Agent Discovery 机制正文已区分 node membership、agent readiness、overlay soft state 与身份/授权，因此保留该受限比较作 Existing Coverage，不重复写入算法摘要。

### [2604.23205v1 Tessera: Secure, Near-Line-Rate Weight Streaming for UMA Edge Accelerators](https://arxiv.org/html/2604.23205v1)

官方 exact-v1 §3、§5、§8 以 64B AXI burst 的 address-derived AES-CTR 解密将权重明文限在隔离 NPU SRAM；这只给所述参考架构的 at-rest→ingress→on-die 保密路径，CTR 本身无完整性，吞吐多为 proxy/model projection，不证明已流片、物理侧信道安全或生产 SLO。[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 已有同一权重流式保密边界的机制正文，故为 Existing Coverage。安全命题按必要范围深入审阅，不将理论带宽数字提升为实测。

### [2604.23108v1 Mixture of Heterogeneous Grouped Experts for Language Modeling](https://arxiv.org/html/2604.23108v1)

exact-v1 §3–5 的两层路由先选异宽 expert group，再选组内 expert；每设备放置各尺寸 expert 的静态参数对称，需要 token 路由/实现共同支持，不能推出逐 GPU 工作量已均衡。Table 1 同时改变总参数与激活参数，Table 3 只是路由比例，词频/perplexity 也不是 token 难度真值。[Ch21](../../../../books/part-02-model/21-moe.md) 的容量预算分支现有「结构路由不等负载控制」段已增补此差额，保留 padding/通信/利用率成本及同宽 fallback。[必要审阅](../_sources/daily-20260428/V3_23108_BOUNDED_SOURCE_REVIEW.md)和有界公告组合支持采用 v1，不以 04/28 后续 v2 的 OAI 改动移动 v1；root 已读实际新增正文及相邻交接。

### [2604.23150v1 Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns](https://arxiv.org/html/2604.23150v1)

exact-v1 §3–5 将历史 decode 请求按激活相似性聚类，簇分配到 device group 后再用条件化 `U[d,e]` 布置 expert；新请求 prefill 后去哪个组是另一动作，不能与现有 prefill-signature locality routing 混称。冗余 expert 没用于所报评价，all-to-all 字节减小也不等 padding 后层时延或请求 P99。[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 的 prefill locality 后现增补历史簇→group→placement、分布/模型/placement epoch、重聚类/迁移成本和静态 placement/最小负载回退；[必要 source→owner](../_sources/daily-20260428/V3_23150_BOUNDED_SOURCE_REVIEW.md)及 root 写后对读通过。

### [2604.23577v1 RouteNLP: Closed-Loop LLM Routing with Conformal Cascading and Distillation Co-Optimization](https://arxiv.org/html/2604.23577v1)

exact-v1 的真实增量是从失败簇定向蒸馏便宜 tier，改变其误差分布后重训 router/重校升级阈值；同数据量 random-vs-targeted 仅在 benchmark 支持选例分支。8 周 shadow pilot 无 A/B，未在生产失败日志运行该 co-optimization，故不能把成本/P99 归因给闭环训练。[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) 在 cascade 成本段后现要求 model/router/calibrator 组合 artifact、分布漂移验证和回退，不把 shadow 变成生产因果结论。[必要审阅](../_sources/daily-20260428/V3_23577_BOUNDED_SOURCE_REVIEW.md)及 root 实际写后通过。

### [2604.23051v1 Evaluating Temporal Consistency in Multi-Turn Language Models](https://arxiv.org/html/2604.23051v1)

exact-v1 的评价对象不是事实库有效期，而是同一对话中隐式时间 scope 的继承、覆盖及跨实体传播；Gold 历史/Self 历史/Questions only 是同题不同历史可见性的分母。Wikidata 模板、当前值 snapshot、不同链长题组和观察性 drift 限制因果解释。[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 canonical fact ledger 后现补 conversation-scope 审计，区分事实错、scope 错、错误历史自我维持，保留澄清而非猜测默认时间的回退。[必要审阅](../_sources/daily-20260428/V3_23051_BOUNDED_SOURCE_REVIEW.md)及 root 实际写后通过。

### [2604.24618v1 Evaluating whether AI models would sabotage AI safety research](https://arxiv.org/html/2604.24618v1)

exact-v1 §3–4/A.3–A.4 的 270 场景考察没有外部破坏指令时的自发机会；1,485 有效 transcript 来自 256 seeds × 三切点 × 两种 reasoning 的 1,536 个可能条件，经 invalid 排除后构成已插入破坏历史的续写分母。Mythos 约 7% 续写不等部署自发率，自发样本零也不是不存在罕见触发；大部分模型三 epochs、Opus4.7 一 epoch 不能抹平。Petri 的部分反馈/用户是模拟，少数真实 repo/Claude Code scaffold 不消除 evaluator/prefill awareness。相对 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 原 active probe/evaluator awareness，现补「续写条件化和自发机会必须分账」段；apr24_close 已核上述必要原文与 Ch66:909–911 实际正文/相邻交接通过。

### [2604.23121v1 Breaking Lock-In: Preserving Steerability under Low-Data VLA Post-Training](https://arxiv.org/html/2604.23121v1)

exact-v1 §3–4 将低数据适配时视觉 encoder 的漂移正则，与测试时每个 flow 去噪步正/负指令双 velocity 差分分开；Frozen-Vis/no-Vis-Reg/no-CPG 对照不等只换一次 prompt。正负指令须可给，每步双 forward、引导系数/schedule 及 embodiment 适配限制都增加成本。证据只限四仿真/四实机任务，不给通用 CFG、控制 SLO 或物理安全保证。[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)「从只学 Action 到同时保存语义」后现补训练→采样接口；非作者 source→实际 owner 写前通过，实际写后通过，见[必要对读](../_sources/daily-20260428/V3_TWO_MONITOR_VLA_ADMISSION.md)。

### [2604.23333v1 Process Supervision of Confidence Margin for Calibrated LLM Reasoning](https://arxiv.org/html/2604.23333v1)

exact-v1 §3–4 多预算截点 K 次 completion 构造 MC 可解性标签，BCE 只更新 probe；policy 用终局答案 reward 加正确/错误前缀集合的相对 margin。相对排序不是绝对概率校准，MC/probe refresh 不是免费；整体 accuracy .618 仍低于 GRPO .621，AIME25 .360 也低于 .373，不能宣传准确率全面提升。[Ch33](../../../../books/part-04-training-system/33-grpo.md) 在 prefix scorer 与 Group Size 之间现补独立双目标与 held-out selector/fallback，source→owner 已由 apr24_close 核，实际写后通过；[必要对读](../_sources/daily-20260428/V3_THREE_TRUE_INCREMENT_ADMISSION.md)保留边界。

### [2604.24447v1 Characterizing Vision-Language-Action Models across XPUs: Constraints and Acceleration for On-Robot Deployment](https://arxiv.org/html/2604.24447v1)

exact-v1 §5.2–5.3 的同次去噪稳定段缓存和旧 observation KV 早步→fresh KV 晚步是两个近似。后者旧步从 5 增至 7/9 时双任务 SR 从 88/78 降为 50/42、10/6；Ascend310P 还有 818→820ms 反向，不能把有限 overlap 变成无限缓存有效或跨硬件加速保证。相对 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 原 Streaming/Fast-Slow freshness，现补同 cycle 的切换位置、旧步预算、KV generation 和取消/同步重算路径；非作者写前通过、实际写后通过，[必要证据](../_sources/daily-20260428/V3_24447_NECESSARY_ADMISSION.md)不采用 XPU 榜单为新机制。

### [2604.23318v1 Hidden States Know Where Reasoning Diverges: Credit Assignment via Span-Level Wasserstein Distance](https://arxiv.org/html/2604.23318v1)

exact-v1 §3.2–3.3/Algorithm1 的 opposing-set 最小 Sinkhorn→重叠 span 最大权重乘原 advantage，保 outcome 正负但全组 normalization 改 cross-rollout 幅度。§4 分布距离定理不是因果定位，best-observed checkpoint/有限数学代码对照及 7.4–15.5% 额外训练时延不能证明同预算普胜。[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 sequence reward→字段 credit 之间现补自身 hidden-state sensor、混合正误组准入与回退；[必要对读](../_sources/daily-20260428/V3_23318_BOUNDED_CREDIT_REVIEW.md)及非作者写前通过，实际写后通过。

### [2604.24003v1 Stabilizing Efficient Reasoning with Step-Level Advantage Selection](https://arxiv.org/html/2604.24003v1)

exact-v1 §2.2–2.3 的短窗本身压缩输出，约 29% 原正确回答人工截断后缺末答成为 verifier-failed；其 correct-lowconfidence / failed-highconfidence mask 分别免正/负 advantage，不证明 confidence=step truth。完整双分支消融、约 17% wall-clock 增加、nDCG 与 PRM agreement 非 gold 都保留。[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 truncation admission/typed credit 段后现补该混杂和有条件 update，非作者写前通过、实际写后通过，[必要对读](../_sources/daily-20260428/V3_THREE_TRAINING_VISUAL_OWNER_TRIAGE.md)。

### [2604.24005v1 TCOD: Exploring Temporal Curriculum in On-Policy Distillation for Multi-turn Autonomous Agents](https://arxiv.org/html/2604.24005v1)

exact-v1 §4.1–4.2 的 F2B 只延长 student prefix，B2F 先筛 pass@10 teacher 成功轨迹、执行前缀后由 student 接管 suffix，并逐步前移 frontier；状态分布和成本不能混称纯 OPD。环境重放、成功路径选择偏差及正文 `t<k`/伪码 `t≤k` 边界书写未决均不被榜单覆盖。[Ch33](../../../../books/part-04-training-system/33-grpo.md) 的 Dense Teacher Signal 之后现补两种 support 恢复分支，保普通短 rollout/离线/OPD 回退；非作者写前通过、实际写后通过，[必要对读](../_sources/daily-20260428/V3_THREE_TRAINING_VISUAL_OWNER_TRIAGE.md)。

### [2604.24391v1 FreqCache: Accelerating Embodied VLN Models with Adaptive Frequency-Guided Token Caching](https://arxiv.org/html/2604.24391v1)

exact-v1 §4.1–4.4 先用 phase displacement 重映射旧视角 token，再限定重叠区 reuse；出界/新视野和高频边缘强制刷新，spectral entropy 只调预算而非物理安全充要。单 A100/InternVLA-N1/R2R-CE 平均 637→401ms/step 同时 SR64.3→63.0，不能称无损实时。[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 在 Action Memoization 到 State ownership 之间补对应有效性/刷新优先级双判定及 full recompute/controller 回退；非作者写前通过、实际写后通过，[原始题摘与必要对读](../_sources/daily-20260428/V3_ARXIV_OFFICIAL_CATEGORY_TITLE_CHECK.md)。

### [2604.23838v1 JigsawRL: Assembling RL Pipelines for Efficient LLM Post-Training](https://arxiv.org/html/2604.23838v1)

exact-v1 §4.1–4.4 的跨两个不同权重 pipeline spatial multiplex、同 pipeline DP-tail merge/migration 和 interference-aware microbatch 不是同一动作。Recent profiles/slow drift、SM/memory 干扰、KV recompute/迁移和 lookahead 都是新增成本状态；§5.2–5.4 的 aggregate tokens/sec 可增 1.56×平均/1.95×上限，同时单 pipeline 平均步延迟 1.48×更慢。给定 GRPO/SGLang/FSDP/4–64 GPU 条件不证明训练质量等价或作业公平。[Ch31](../../../../books/part-04-training-system/31-rlhf.md) 在 RLHF 系统成本、异步 freshness 之前现补分权和独占/静态回退；apr24_close 已核必要源与实际 owner，实际写后通过。

### [2604.24008v1 Coverage-Based Calibration for Post-Training Quantization via Weighted Set Cover over Outlier Channels](https://arxiv.org/html/2604.24008v1)

exact-v1 §3–7/App I–J 加权互补 channel coverage 选择 sample，而非仅挑高 variance/PPL 或调 per-channel scale。`1−1/e` 只对覆盖目标，M1 视已覆盖通道零误差过于理想、M2 additive channel surrogate 非实际 loss/Frobenius 上界；同 candidate/reference pool 让已识别通道可覆盖，却补不了部署缺失切片。10k pool profile 约15min A100+CPU选择<10s 不是零成本，INT4 AWQ/GPTQ/有限模型/K32–256 三 seeds 限制外推。[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 在 calibration 与 PTQ/QAT 之间现补 pool/coverage/sample-membership artifact、漂移重校与分层/高精度回退，非作者写前通过、实际写后通过。

### [2604.24013v1 FlashOverlap: Minimizing Tail Latency in Communication Overlap for Distributed LLM Training](https://arxiv.org/html/2604.24013v1)

exact-v1 §3.2/Algorithms1–2 中 AG 先计算本 rank 已有 slice，RS 先计算外送 partial、本地保留 slice 最后；逐轮仍 wait，不是消灭同步。§5 的 TP/SP MLP/attention layerforward、10iterations 不证明全训练收敛、跨拓扑、bitexact 或故障保证，部分 shape 的 slicing 还输无 overlap。原作者 Only 提案以没有新 fault 语义为由过窄，非作者纠正为真实关键路径 gap；[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) overlap 之后现补依赖顺序、buffer/result-ready/数值重排和原 collective 回退，实际写后通过。[必要反向重判](../_sources/daily-20260428/V3_THREE_REPRUNE_23941_24074_24013.md)保留版本题名，旧 CommFuse 不覆盖 v1。

### [2604.23374v1 Ghost in the Agent: Redefining Information Flow Tracking for LLM Agents](https://arxiv.org/html/2604.23374v1)

exact-v1 §3–5 的 memory read 只恢复 provenance，sink 时才分显式传播与隐式 control；中性兼容替换后的反事实 probe 是 post-execution 诊断，不是不可逆 effect 前授权。400 TaintBench/200positive 属传播标签，五次聚合不等 unsafe rate；约0.25s/457 auditor tokens 是离线成本，有13FN/16FP。[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的 cross-channel graph 后现补 sink-time 诊断、Unknown 与线上 deterministic policy 的分层；[必要审阅](../_sources/daily-20260428/V3_23374_BOUNDED_TAINT_REVIEW.md)及非作者写前通过，实际写后通过。

### [2604.23459v1 Architecture Matters for Multi-Agent Security](https://arxiv.org/html/2604.23459v1)

exact-v1 §4–5/AppendixB 分 PR/ER/HA/HT 与另组 benign success；BrowserART star/chain/mesh HT31/16/7%，RedCode-Gen 却17.5/42.5/20.6%，不可迁拓扑排序。后者是未执行代码的 judge，OS-Harm benign 近零，恶意/良性100/42、44/50、160/50不能混分母；directmisuse 也不覆盖 indirect injection。相对原通信 influence graph，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 现补架构比较的双机会集/阶段 effect 评价，不写万能安全拓扑。[必要审阅](../_sources/daily-20260428/V3_23459_BOUNDED_SOURCE_REVIEW.md)及非作者写前通过，实际写后通过。

### [2604.23711v1 Spore: Efficient and Training-Free Privacy Extraction Attack on LLMs via Inference-Time Hybrid Probing](https://arxiv.org/html/2604.23711v1)

exact-v1 §3–5 的秘密由 inference context 提供，不是训练 memorization；blackbox response 的≤20候选恢复与 greybox 每步 top10/logprobs 是不同攻击权限，pass@k=1–5重复与 offline candidate/follow-up试探须另计。560 TrustLLM构造 context、150safeguard平均4.72queries 不支持所有攻击“单查询”；§3.4无formalproof与结论理论证明冲突、MI经验斜率不保证恢复，detector分类率也不等隐私保证。非作者核实际 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)「全部 Observable Channels」的 observer permission/combinedattack 与隐藏 trace/context 发布分权已经承载该窄威胁合同；故具体 Existing，不用训练 MIA 模板关闭，也不新增理论保证。

### [2604.23781v1 ClawMark: A Living-World Benchmark for Multi-Turn, Multi-Day, Multimodal Coworker Agents](https://arxiv.org/html/2604.23781v1)

exact-v1 §3/§5 的100任务/13场景/2–6虚拟日/5有状态服务，1537 checkers/55 redlines 包含外生 loud notification 与 silent mutation。Redlines 是高权重普通 checker，不是独立 hardgate；weighted progress 与 strict all-checker 成功不同，七模型单完整 sweep 未给多run方差。非作者核实际 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) Living-world 及 ClawMark temporal 段已保存 external actor/clock/mutation/backend revision/statehash/reset/postturninvariants，所以为具体 Existing，不把 synthetic沙箱变真实长期部署证明。

### [2604.22879v1 Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems](https://arxiv.org/html/2604.22879v1)

exact-v1 §3–4 的私有 context 不汇总、源 sidecar 回答 predicate、sink 独立授权是有条件分权设计；§4.8.4 却从计算型零知识直接推 Shannon `I(G;View)≤1bit`，§6 也承认自适应多查询泄露。160/40 合成机会集与普通 boolean 成本不能证明跨机构加密生产。作者必要深入已完成，但中心安全证明争议隔离，不把 predicate 升级授权真值、不写 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)；[必要源与证明边界](../_sources/daily-20260428/V3_22879_BOUNDED_SAFETY_REVIEW.md)支持具名暂缓而非正面保证。

### [2604.22888v1 RouteGuard: Internal-Signal Detection of Skill Poisoning in LLM Agents](https://arxiv.org/html/2604.22888v1)

exact-v1 Tables1–5/Method 的白盒 response-conditioned attention/隐藏态 pre-screen 不等 effect 安全；打印核心 P/R/F1 无法复算，例如 SI-CH `.9334/.6442` 应约 `.7623` 而非 `.8834`，其余多组也非舍入。仅隔离 detector 优势与 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 采用，不由打印冲突断言原始全部实验已伪。[算术复核](../_sources/daily-20260428/V3_22888_NUMERIC_BOUNDARY.md)与必要方法读完，中心结果暂缓、重开须可对应的预测/标签与协议。

### [2604.23584v1 Identity-Decoupled Anonymization for Visual Evidence in Multi-modal Retrieval-Augmented Generation](https://arxiv.org/html/2604.23584v1)

exact-v1 的检索后 reader 前视觉 identity/attribute 分离、生成替换身份确实挑战匿名化与 groundedness 的共同目标，但生成图不继承原证据真实性。MINE 下界不能当互信息上界；Theorem4 依原身份拒绝后的替换码不独立，最小两码在零 attribute 泄漏下仍保留1bit替换依赖。[必要反例](../_sources/daily-20260428/V3_23584_BOUNDED_PRIVACY_REVIEW.md)据此隔离中心 privacy 保证、重认率外推与 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)/Ch76 采用，不把局部人脸结果当正式不可识别性。

### [2604.24118v1 AgentVisor: Defending LLM Agents Against Prompt Injection via Semantic Virtualization](https://arxiv.org/html/2604.24118v1)

exact-v1 §4.1 Eq6–7/§4.4/AppendixA Algorithm1 在首轮拒绝后让 guest 改写 `T′` 并直接执行，未显示再 STI audit；净化 history 也不保证不携攻击语义。有限 ASR/benignutility 不证明最终 effect 都经独立许可。[协议定点反证](../_sources/daily-20260428/V3_AGENTVISOR_EXACT_V1_BOUNDED_REVIEW.md)支持暂缓强保证，不声称核过代码漏洞，不将监督模型当 [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) 的确定性 authorizer。

### [2604.22778v1 The Spectral Lifecycle of Transformer Training: Transient Compression Waves, Persistent Spectral Gradients, and the Q/K--V Asymmetry](https://arxiv.org/html/2604.22778v1)

§3–4/§7–8 区分短期 rank 与持久谱形；Random 剪层反例及 5.307 对 3.720 的谱形 warmup（差 42.7%）否定单一谱形授权干预。SVD/方向验证有成本，受限 GPT/Pythia 消融不支持跨架构因果或剪枝保证。 [必要原文对读](../_sources/daily-20260428/V3_22778_NECESSARY_CONTRIBUTION.md)支持具体采用命题；已在 [Ch28](../../../../books/part-04-training-system/28-pretraining.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23475v1 Supernodes and Halos: Loss-Critical Hubs in LLM Feed-Forward Layers](https://arxiv.org/html/2604.23475v1)

§3–4/AppA 固定 LP score 后 activation 保护集与 LP 保护集 PPL 同为 10.71；整体改用 activation-L2 score 则 26.84，二者变化对象不同。保护集/校准域增加预算，离线质量不代表稀疏 kernel 收益。 [必要原文对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_B.md)支持具体采用命题；已在 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23798v1 ELSA: Exact Linear-Scan Attention for Fast and Memory-Light Vision Transformers](https://arxiv.org/html/2604.23798v1)

§3–4 让 block 独立归约后并行合并所有 query 状态；不采用移出窗口项、线性总 attention work 或 bitwise 等价。Workspace、数值重排及短 window 反例要求保留普通 attention 路径。 [必要原文对读](../_sources/daily-20260428/V3_LATE_BATCH_FINITE_TRIAGE_A.md)支持具体采用命题；已在 [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24040v1 Improving Robustness of Tabular Retrieval via Representational Stability](https://arxiv.org/html/2604.24040v1)

§2–4 表格 format 改变 retrieval embedding/rank，区别 reader attention capture；shift 抵消是构造假设。SPLADE/部分强格式退步，多 view/adapter/重编码需成本；不把 centroid 当 canonical truth。 [必要原文对读](../_sources/daily-20260428/V3_LATE_BATCH_FINITE_TRIAGE_B.md)支持具体采用命题；已在 [Ch76](../../../../books/part-07-agent/76-rag.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24086v1 AsyncShield: A Plug-and-Play Edge Adapter for Asynchronous Cloud-based VLA Navigation](https://arxiv.org/html/2604.24086v1)

§III-A 的安全接口为 CMDP cost 与 PPO-Lagrangian；历史 plan anchor 变换不校零 odometry 误差。真机每 model 20 trials 不证明物理安全；保持独立工程 controller、pose 失效停止和重规划。 [必要原文对读](../_sources/daily-20260428/V3_THREE_BOUNDARY_23987_24086_24088.md)支持具体采用命题；已在 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24622v1 CF-VLA: Efficient Coarse-to-Fine Action Generation for Vision-Language-Action Policies](https://arxiv.org/html/2604.24622v1)

§3/Alg1 先 proxy 两阶段再 joint，预测 endpoint velocity/variance，从同一 ε 得近 action 初始化后一次 refine，不是纯 noise 一步或 cache warm start。Coarse 错误可能不能修复；双 head/训练及局部 sampling 均值不代表完整控制 SLO。 [必要原文对读](../_sources/daily-20260428/V3_LATE_BATCH_FINITE_TRIAGE_D.md)支持具体采用命题；已在 [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24708v1 Scalable Hyperparameter-Divergent Ensemble Training with Automatic Learning Rate Exploration for Large Models](https://arxiv.org/html/2604.24708v1)

§3 的异参数/共享 gradient 不等同参 DDP 或 local independent gradients；必须保存 rank 参数与 optimizer/平均 cadence。单推荐、单 epoch、8H100 与自动 LR 小增量不支持 LLM 收敛或零额外成本。 [必要原文对读](../_sources/daily-20260428/V3_LATE_BATCH_FINITE_TRIAGE_D.md)支持具体采用命题；已在 [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24088v1 TACO: Efficient Communication Compression of Intermediate Tensors for Scalable Tensor-Parallel LLM Training](https://arxiv.org/html/2604.24088v1)

§4.2–4.3 低能 activation 双 scale+FWHT 的有损 codec；FP8/INT8 反向结果仅该实验。Codec/网络整体验收，误差或 overhead 超界回退原 TP 通信，不称近似为数值等价。 [必要原文对读](../_sources/daily-20260428/V3_THREE_BOUNDARY_23987_24086_24088.md)支持具体采用命题；已在 [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23434v1 When Does Removing LayerNorm Help? Activation Bounding as a Regime-Dependent Implicit Regularizer](https://arxiv.org/html/2604.23434v1)

§4–5 所有 T/P<1.84；0.43 阈值 LOSO 准确约 50% 不作 controller。饱和/任务容量与架构联合验收，校准与 matched curve 有成本，保留成熟 normalization。 [必要原文对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_B.md)支持具体采用命题；已在 [Ch17](../../../../books/part-02-model/17-transformer-layer.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24432v1 Kwai Summary Attention Technical Report](https://arxiv.org/html/2604.24432v1)

§2.2–2.3 分开 chunk 内 direct text、summary handoff 和三个 cache 段。Mask/训练/更新身份一致；压缩不可宣称语义无损，远距细粒度任务保原文回读与更大窗口。 [必要原文对读](../_sources/daily-20260428/V3_BATCH4A_NECESSARY_ADMISSION.md)支持具体采用命题；已在 [Ch22](../../../../books/part-02-model/22-long-context.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24300v1 ReVSI: Rebuilding Visual Spatial Intelligence Evaluation for Accurate Assessment of VLM 3D Reasoning](https://arxiv.org/html/2604.24300v1)

§3–5 5% visibility 筛选、人工复核和 dummy video 检查输入支持；64 帧非普适 truth。重采样/标注有成本，原始与保留子集双分母，不把 sampler 缺失当模型能力不足。 [必要原文对读](../_sources/daily-20260428/V3_THREE_ABSTRACT_OWNER_RESCREEN.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24608v1 Learning to Route Queries to Heads for Attention-based Re-ranking with Large Language Models](https://arxiv.org/html/2604.24608v1)

路由仅选择读出组合，不意味着 skip head computation 或 attention 是 relevance truth。数学/代码/跨域反例、label/router 训练与完整前向成本要求静态/普通 reranker fallback。 [必要原文对读](../_sources/daily-20260428/V3_ARXIV_OFFICIAL_CATEGORY_TITLE_CHECK.md)支持具体采用命题；已在 [Ch76](../../../../books/part-07-agent/76-rag.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23321v1 MMEB-V3: Measuring the Performance Gaps of Omni-Modality Embedding Models](https://arxiv.org/html/2604.23321v1)

§3–4 OmniSET 12 方向、每方向 100 synthetic query；视频来自 image/音频来自 text 形成方向混杂。权威 modality lineage 与 semantic relevance 分账，不由对象外壳或小题库推出真实排行。 [必要原文对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_B.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.22891v1 Quantifying and Mitigating Self-Preference Bias of LLM Judges](https://arxiv.org/html/2604.22891v1)

质量判别与 self/third-party 条件偏好不同；双 LLM quality proxy 非 gold，差分不是纯 self 因果识别。配对/第三方调用成本与风格混杂要求人工 anchor 或无排序结论。 [必要原文对读](../_sources/daily-20260428/V3_TWO_EVAL_ADMISSION_TRIAGE.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23099v1 ProEval: Proactive Failure Discovery and Efficient Performance Estimation for Generative AI Evaluation](https://arxiv.org/html/2604.23099v1)

§2–3/AppB 共享 prior 但分配不同 query 预算；Thm3 约束 posterior mean 非实际题库 S*。Covariance/先验负迁移、generator reference 错误与 query 成本要求独立 audit floor。 [必要原文对读](../_sources/daily-20260428/V3_ARXIV_ADMISSION_BATCH1.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.22937v1 AutoPyVerifier: Learning Compact Executable Verifiers for Large Language Model Outputs](https://arxiv.org/html/2604.22937v1)

§2.1–2.4 dev verifier-set search 不是独立 truth；最高 +55 为 F1 点非 task accuracy，OOD 可负收益。标注/执行/搜索成本、集合版本与独立准入保原冻结 checker fallback。 [必要原文对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_B.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23455v1 CUJBench: Benchmarking LLM-Agent on Cross-Modal Failure Diagnosis from Browser to Backend](https://arxiv.org/html/2604.23455v1)

87 incident corpus/25 test，browser 与 backend tools 不同可见性及提交率；不能推出更多证据有害。配对 oracle、tool access 与提交事件增成本，未提交与错误诊断分账。 [必要原文对读](../_sources/daily-20260428/V3_23455_BOUNDED_EVAL_CONTRIBUTION.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.24401v1 All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation](https://arxiv.org/html/2604.24401v1)

§2–3 三基准/八模型，3.0–4.2% cross-segment 为 audio-needed 内比例而非全部题。片段边界/支持标签与消融成本需保 full audio fallback，不推真实脑机制。 [必要原文对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_A.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.23488v1 Do Synthetic Trajectories Reflect Real Reward Hacking? A Systematic Study on Monitoring In-the-Wild Hacking in Code Generation](https://arxiv.org/html/2604.23488v1)

§3–5 人工冲突 unit tests 和 resampling 形成特定机会集；同源 held-out 不代跨来源迁移。双轴轨迹/标注/校准成本，目标来源不覆盖时保持独立 audit/Unknown，不报部署作弊率。 [必要原文对读](../_sources/daily-20260428/V3_TWO_MONITOR_VLA_ADMISSION.md)支持具体采用命题；已在 [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 窄写新责任/状态边界，保旧路线、代价和回退。非作者 source→actual owner 已通过，实际写后已通过，见非作者有限复核及日级最终记录。

### [2604.22785v1 CoFi-PGMA: Counterfactual Policy Gradients under Filtered Feedback for Multi-Agent LLMs](https://arxiv.org/html/2604.22785v1)

competition propensity/缺失反馈与 collaboration counterfactual/不可归因效应分开；DR 依赖 positivity 及至少一个模型正确，下游 resampling 留 lineage。§3–4 仅一 seed 单轮 routing 实验，不保证协作信用、joint misspecification 或免费标注。 [必要原文/owner 对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_A.md)支撑这一窄终判；Books 为整合，唯一 owner [Ch31](../../../../books/part-04-training-system/31-rlhf.md)。已实际写入新的责任/状态边界，保旧路线、成本与回退，非作者实际写后已经通过。

### [2604.23283v1 Revisable by Design: A Theory of Streaming LLM Agent Execution](https://arxiv.org/html/2604.23283v1)

§4–6 earliest incompatible K/X 决定受控 rollback frontier，world effect 需 compensation 非 undo；compatibility separability/非递减代价可有 ties，不称唯一一般最优。模拟工具少 wasted acts 伴更多 token，非真实 API 原子性。 [必要原文/owner 对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_A.md)支撑这一窄终判；Books 为整合，唯一 owner [Ch81](../../../../books/part-07-agent/81-workflow.md)。已实际写入新的责任/状态边界，保旧路线、成本与回退，非作者实际写后已经通过。

### [2604.23552v1 On the Memorization of Consistency Distillation for Diffusion Models](https://arxiv.org/html/2604.23552v1)

§3–5 teacher 初始化不保证 distill 后 near-copy 不变；SSCD 0.6/p95 不是 privacy bound。ImageNet 7k FID20.14→28.65 质量反向，重复样本/蒸馏/审计成本不免独立 copy/provenance gate。 [必要原文/owner 对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_C.md)支撑这一窄终判；Books 为整合，唯一 owner [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。已实际写入新的责任/状态边界，保旧路线、成本与回退，非作者实际写后已经通过。

### [2604.23994v1 When to Commit? Towards Variable-Size Self-Contained Blocks for Discrete Diffusion Language Models](https://arxiv.org/html/2604.23994v1)

§3–5 NF/FA 用同模型 candidate future 比较分布，并非真实未来；训练截断 α 非 runtime threshold。候选窗口/调用/cache 成本与 block64 反向切片要求原 confidence/schedule 回退，不保证提交正确。 [必要原文/owner 对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_A.md)支撑这一窄终判；Books 为整合，唯一 owner [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)。已实际写入新的责任/状态边界，保旧路线、成本与回退，非作者实际写后已经通过。

### [2604.24222v1 MEMCoder: Multi-dimensional Evolving Memory for Private-Library-Oriented Code Generation](https://arxiv.org/html/2604.24222v1)

跨 API task guideline 与单 API 参数边界 guideline 分开，Reflector Discard/Delete/Add 与权重非 FIFO；同 task reward 不归因每 API，doc 权威和 effect receipt 独立。额外反思/索引/漂移成本与 library revision 需绑定，不以记忆替文档或执行验收。 [必要原文/owner 对读](../_sources/daily-20260428/V3_ARXIV_OFFICIAL_CATEGORY_TITLE_CHECK.md)支撑这一窄终判；Books 为整合，唯一 owner [Ch81](../../../../books/part-07-agent/81-workflow.md)。已实际写入新的责任/状态边界，保旧路线、成本与回退，非作者实际写后已经通过。

### [2604.22985v1 Uncertainty Quantification for LLM Function-Calling](https://arxiv.org/html/2604.22985v1)

AST match 是 schema 指标非真实 effect；混合 AUROC 不能代分 slice 阈值，排除 invalid3.4% 改分母。当前 Ch66 schema/uncertainty/slices 未包含此 AST 参数归一/semantic-token 分布具体 sensor，因此不再用主题等价声称 Existing；受限 function-call 校准对照保留为5标准仅报告，不添通用正文。[必要原文](../_sources/daily-20260428/V3_TWO_EVAL_ADMISSION_TRIAGE.md)，唯一 owner [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [2604.23178v1 Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines](https://arxiv.org/html/2604.23178v1)

style/position 偏差依任务及协议，CoT/swap 非通用缓解。当前 judge 局部比较、prompt/顺序 identity、外部 anchor 与 interval 已承载；题目、judge 或域变更须重校，不因提示技巧授权排名。 [必要原文/owner 对读](../_sources/daily-20260428/V3_23178_BOUNDED_EXISTING_REVIEW.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.23581v1 AgentEval: DAG-Structured Step-Level Evaluation for Agentic Workflows with Error Propagation Tracking](https://arxiv.org/html/2604.23581v1)

DAG root-parent 启发式非因果；150 cases 中195 bad steps 非450独立样本，循环任务退步。Ch69 dependency/root-cause view 与 trace/outcome 分权已承载，额外诊断成本与不确定性不靠新评分消除。 [必要原文/owner 对读](../_sources/daily-20260428/V3_23581_BOUNDED_EXISTING_REVIEW.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.23747v1 SFT-then-RL Outperforms Mixed-Policy Methods for LLM Reasoning](https://arxiv.org/html/2604.23747v1)

CPU offload 第一 micro 梯度 owner 与 global effective-token normalization 是两类具体坏基线：完整所有 micro 的累积梯度应到 CPU optimizer owner，loss sum/count 应跨全部 rank/micro 汇总后归一，不平均各局部均值。官方 §2.1–2.2/Table2 对 DeepSpeed0.18.9/OpenRLHF0.9.10 的纠错与 ID/OOD 反向不能推出所有 mixed-policy 劣。[必要原文](../_sources/daily-20260428/V3_23747_NECESSARY_CONTRIBUTION.md)支撑5深入整合；[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) 已窄写并独立写后通过，保成本/版本及坏baseline隔离。

### [2604.23853v1 ClawTrace: Cost-Aware Tracing for LLM Agent Skill Distillation](https://arxiv.org/html/2604.23853v1)

actual Ch69 TraceCard:221–239 已写 preserve/prune/repair 与迁移成本；30+30 tasks、17success/2match/3preserve 不能构成通用收益，aggregate 省成本0。唯一 owner 是Ch69而非Ch66/84，paired utility 不给因果保证。 [必要原文/owner 对读](../_sources/daily-20260428/V3_EIGHT_ACTUAL_BODY_DATE_TRIAGE.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.23932v1 MatchRDMA: A Segmented and Rate-Matched Long-Haul RDMA Scheme for Geo-distributed LLM Training over OTN](https://arxiv.org/html/2604.23932v1)

长 RTT 分段 credit/pseudoACK/OTN 率匹配改变 transport feedback 不改 destination completion；模拟非训练吞吐。当前 WAN completion/transport 分权与 recover/fallback 已承载，不将 pseudoACK 当真实完成。 [必要原文/owner 对读](../_sources/daily-20260428/V3_EIGHT_ACTUAL_BODY_DATE_TRIAGE.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.23950v1 LearnPruner: Rethinking Attention-based Token Pruning in Vision Language Models](https://arxiv.org/html/2604.23950v1)

早期 visual-self 与晚期 text→vision 信号在不同阶段可用，foreground proxy 非证据 truth。当前信息可见性、sink/diversity与保原token回退已经表达；受限selector不独立创造长期接口。 [必要原文/owner 对读](../_sources/daily-20260428/V3_THREE_TRAINING_VISUAL_OWNER_TRIAGE.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.23987v1 Continual Calibration: Coverage Can Collapse Before Accuracy in Lifelong LLM Fine-Tuning](https://arxiv.org/html/2604.23987v1)

actual Ch66:118–135 同家族 model update/calibration release transaction 已区分 coverage 与accuracy；分类/exchangeability限制不证明任意分布迁移。保存重校成本、版本与失效回退，不重复同命题。 [必要原文/owner 对读](../_sources/daily-20260428/V3_THREE_BOUNDARY_23987_24086_24088.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.24074v1 How Sensitive Are Safety Benchmarks to Judge Configuration Choices?](https://arxiv.org/html/2604.24074v1)

12 variants/28,812 verdicts 的同 judge spread 及4.6% parsing failure 不等 target 安全率改变；最大24.2pp非human accuracy。实际 EvalSpec prompt variant/normalization/外部 anchor 已承载，冻结协议与 raw generations 保留。 [必要原文/owner 对读](../_sources/daily-20260428/V3_THREE_REPRUNE_23941_24074_24013.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.24594v1 Skill Retrieval Augmentation for Agentic AI](https://arxiv.org/html/2604.24594v1)

retrieval、loading、end-task utility 分开，gold present 仍可能不load；hit 不能当utility。实际 Load/Abstain 与 paired gate 已承载具体交接，记录加载/使用/cost和失败，不因更多skill召回自动授权上线。 [必要原文/owner 对读](../_sources/daily-20260428/V3_REVERSE_EXACT_V1_TRIAGE_A.md)支撑这一窄终判；Books 为已有覆盖，唯一 owner [Ch84](../../../../books/part-07-agent/84-agent-platform.md)。现有正文已经承载具体测量/控制差额，不重复写入。

### [2604.23210v1 Discovering Agentic Safety Specifications from 1-Bit Danger Signals](https://arxiv.org/html/2604.23210v1)

独立 danger oracle→规范的受限对照说明 reward-only 不代表安全；5toy+5text、oracle 无FN假设限制。当前规范晋升门禁/反思来源分权已承载；保反证用于报告、不新增未验证规范部署配方。 [必要原文/owner 对读](../_sources/daily-20260428/V3_23210_NECESSARY_EVIDENCE.md)支撑这一窄终判；Books 为仅报告，唯一 owner [Ch80](../../../../books/part-07-agent/80-reflection.md)。该受限对照保留贡献，但不足以在现有 owner 增加长期配方。

### [2604.24203v1 Agentic Witnessing: Pragmatic and Scalable TEE-Enabled Privacy-Preserving Auditing](https://arxiv.org/html/2604.24203v1)

签名链及模拟 quote/TEE 不保证 corpus 完整或语义正确；原文受限 artifact 将 attestation 与 evidence truth 分开，但非真硬件部署。Ch72既有分权承载，报告条件反证而不写硬件安全保证。 [必要原文/owner 对读](../_sources/daily-20260428/V3_LATE_BATCH_FINITE_TRIAGE_C.md)支撑这一窄终判；Books 为仅报告，唯一 owner [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)。该受限对照保留贡献，但不足以在现有 owner 增加长期配方。

### [2604.24320v1 DPEPO: Diverse Parallel Exploration Policy Optimization for LLM-based Agents](https://arxiv.org/html/2604.24320v1)

同一 joint rollout ANY成功非独立 trajectory 均值；branch/environment成本另计，多样性reward消融非单调。当前 producer/trajectory/search-tree identity 承载，保聚合反证、不新增局部reward配方。 [必要原文/owner 对读](../_sources/daily-20260428/V3_BATCH4A_NECESSARY_ADMISSION.md)支撑这一窄终判；Books 为仅报告，唯一 owner [Ch33](../../../../books/part-04-training-system/33-grpo.md)。该受限对照保留贡献，但不足以在现有 owner 增加长期配方。

### [2604.24763v1 Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation](https://arxiv.org/html/2604.24763v1)

encoder-free 与 Tuna-R 同 decoder 不等训练等价，额外 connector stage、理解/生成排序混合。当前 native/shared 表示责任承载，比较应连训练/连接器成本，不以不等数据宣称 encoder 无用。 [必要原文/owner 对读](../_sources/daily-20260428/V3_LATE_BATCH_FINITE_TRIAGE_E.md)支撑这一窄终判；Books 为仅报告，唯一 owner [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。该受限对照保留贡献，但不足以在现有 owner 增加长期配方。

### [2604.24542v1 Layerwise Convergence Fingerprints for Runtime Misbehavior Detection in Large Language Models](https://arxiv.org/html/2604.24542v1)

§3.1–3.3/§6/AppE 同 detector-aware 攻击下，λ=2 单层97/98.5/35 对全层15.5/2/0，λ=5 全层VPI仍76.5。All-layer 与N−3单层真实 sensor 覆盖取舍，FPR12–22%及 adaptive反向否定通用安全；Ch72 probe合同已承载，保5安全深入仅报告，不强添正文。 [必要原文/具体对照](../_sources/daily-20260428/V3_BATCH4A_NECESSARY_ADMISSION.md)可复查；非作者负侧复核撤销原前关闭，不因尚未 operational 就拒绝真实数学或 sensor 取舍。

### [2604.24579v1 Measuring the Unmeasurable: Markov Chain Reliability for LLM Agents](https://arxiv.org/html/2604.24579v1)

§III–V/§VIII-B 统一 first-passage estimand 与 fit rejection 是真实数学测量对象选择。理论/合成拟合、KS未拒绝不证明 raw Agent Markov 或生产rate；仅报告这一受限条件对照，当前 Ch66 measurement identity 承载，不采用实际生产发生率。 [必要原文/具体对照](../_sources/daily-20260428/V3_BATCH4A_NECESSARY_ADMISSION.md)可复查；非作者负侧复核撤销原前关闭，不因尚未 operational 就拒绝真实数学或 sensor 取舍。

## 5. 缺口与下一步

普通可执行工作：无。71份逐篇采用边界、45项实际整合、15 Existing、7仅报告、4争议隔离及非作者日级终审均完成；全部新增窄段实际写后和位置修复通过。下列仅为本窗安全终态保留项，收到必要原始材料后只定点重开，不重新扫描或扩大窗口。这些终态保留项不用于正面证据、不支持 Books 或无遗漏断言；精确重开条件分别列于下文。

本次有界读取后，四项机构历史入口作为外部来源保留项隔离：OpenAI Research/Publication sitemap 可发现 URL，但单篇 403 且无本窗可停的首发日期目录；Google Research Publications 的 2026 年列表不按日排序，不能从 DeepMind 子目录替代；Meta Publications 首屏不能穷尽历史分页且 Research 正文为空；Kimi Platform Blog 可见顶项仍停在 2025 年，不能用 CLI release 零项代替 2026 Blog。四项均不支撑“本窗零论文”、正面候选或 Books 决定；分别在官方单篇首发字段、可按日期翻页的历史目录或可读原文恢复时，只重开本窗附近身份。小米 MiMo Blog 卡片另缺可核首发时间，重开条件见来源表。具名候选的首次公开日若仍无法由公告批次及相邻身份有界证明，将逐项隔离而不机械按 submitted、DOI 或 OAI 日期迁窗。

四个候选中心争议已经非作者核官方 printed theorem/table/algorithm，可作为本窗终态隔离，非正面证据/Books/安全保证；不声称真实 privacy 被破坏或已验证实现 exploit。`.22879v1` 需连接计算不可区分到信息论量的明确新证明、adversarial query/session 的泄漏定义与实际加密成本，不能只补更多 boolean benchmark；`.22888v1` 需带标签/预测、同一 aggregation/protocol 的原始混淆矩阵或可解释所有打印 P/R/F1 的官方勘误；`.23584v1` 需修正可计算 MI 上界或改为受限估计，重建拒绝采样后的独立性条件，并给替换图仍可作原查询证据的独立验证；`.24118v1` 需可读精确实现/revision 展示所有改写 `T′` 再 audit/确定性授权的执行路径及可重放测试，或官方承认收窄保证。材料到达后各只重开上述必要证明/方法位置，不重跑整日或借未决扩窗口。

## 6. 复核

复核者：root（原13子集及必要日期/实际写后）；apr24_close（剩余全部矩阵、负侧、全部新增实际写后与日级终审）。

结论：通过

[独立日级最终记录](../_sources/daily-20260428/V3_APR24_INDEPENDENT_FINAL_REVIEW.md)核71/71候选、14到期来源、公告/ID/OAI/v1有界日期、45实际整合/15 Existing/7 Only/4争议及7具名前关，复用root9负例并分层核23466/24441/24647，未逐篇验真无信号库存。负侧恢复24542/24579、22985改Only、23747落实具体纠错gap；所有正文位置和partial-chunk handoff修复已实际复读。机器校验与指定范围diff检查通过，不替代语义终审；5外部来源及4中心争议均保持隔离，作者未自签。
