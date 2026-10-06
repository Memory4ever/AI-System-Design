# Daily Research — 2026-01-14

**规范：** V3
**窗口：** 2026-01-13T09:00:00+08:00 ～ 2026-01-14T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-03T13:28:24+08:00

## 1. 结论

重要的共同约束是：压缩表示、选择支持、混合精度与共享计算资源，各自改变不同的接口，不能把局部质量、有限 profile 或代理稳定性授予整条执行链。实际融入唯一owner的机制沿表示/训练函数/执行资源/评价对象推进：block-summary bank与固定子空间缓存保布局/误差，order-only蒸馏与终点引导保内容和导数接口，prefill永久裁剪与同格式补偿保执行资格，单专家重接保训练函数身份，动态峰规划与时序/spot效用保资源预算。新增投毒基座风险与语音metric对象分责也已实际写后复核；PRPO局部process/outcome分账也已实际POST通过。RiskEval和Sink的拟采用分责已有具体覆盖；Reference Games保有限行为反证，仅报告。

来源主题查询共返回 374 行、去重 334 个标题/身份线索，范围为提交缓冲而非“当日 334 篇新论文”；该宽列表没有变成逐项摘要或全文队列。原16份加整日漏收抽查定点补五份，实际读21份exact-v1完整题摘。当前17个条件落窗家族逐项终处置：13实际整合且POST通过、2具体已有覆盖、1仅报告、1中心争议隔离。补五项没有降分/删池以冻结原十二项；RoRA、speech测量与SkyNomad已写，Sink为具体Existing，PRPO实际POST亦通过。官方具名负侧、十四源有限停止与五项条件日期已获root实际复核，AIConfigurator拟选机制prior已root实际终裁，所有必要Books已实际落实与POST，root最终独立日Gate通过；普通扫描/筛选/审阅/Books/独立复核待办为零，本日完成。

## 2. 来源覆盖

本轮历史检查执行于 2026-10-02～03，北京时间；原返回集中在 [本日原始材料](../_sources/daily-20260114/STOP.md)。每行只授权所列有限范围，不证明未删除历史、旧版本或整个机构零事件。每日十四源均触发，未扫描 Weekly 来源。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 首页；[官方 RSS](https://openai.com/news/rss.xml) 原 1,244 条只按窗口字段定位，保 Jan13T16Z Zenken 与 Jan14T14Z Cerebras 相邻锚；Zenken 核心已读。见 NATIVE_0、ZENKEN。 | 已检查 | RSS 可见有限窗口不是删除历史证明；Zenken 具体负侧已root实际核通过。 |
| SRC-ANTHROPIC | Research 原嵌入 174 个日期字段，保 Jan9T17:17Z→Jan14T00Z PBT→Jan15T10Z 锚；[PBT 原文](https://www.anthropic.com/research/property-based-testing) 自述 NeurIPS2025，并定位 [2510.09907v1](https://arxiv.org/abs/2510.09907v1)。 | 已检查 | 午夜字段不是精确首公开日志；同机制已有2025正文，具体窗前关闭已root实际核通过，不授本窗新事件。 |
| SRC-GOOGLE-AI | [January 索引](https://research.google/blog/2026/01/) 单页 9 条，Jan28→Jan12；MedGemma/MedASR 核心与决定性接口已读，braking/quantum/NeuralGCM 是领域或暂缓范围线索；Veo3.1 核心已读。DeepMind 首页及 page4 恢复失败，不遍历宽目录。见 SOURCE_CORE_EARLY、OFFICIAL_2、OFFICIAL_FINISH_0/1。 | 受阻 | Research 本月有限页可核；DeepMind 历史 blog 切片未恢复，隔离该覆盖。当前 card 已含 April 技术报告/May 更新，不伪作 January exact card。 |
| SRC-META-AI | Research 首入口；四主题 domain 补检，恢复 [global_search page3](https://ai.meta.com/global_search/?page=3) 中 publications 的 Feb26/13/11/10→Jan02→Dec26/18/16 有限邻接，已读该段而非全部 2,880 混合条目。见 META_HISTORY_SEARCH、META_PAGE3_RAW。 | 已检查 | 混合搜索人物/博客不整体有序；只该 publications 切片，不授全机构或删除历史覆盖。错误 domain 查询另存 failed probe。 |
| SRC-QWEN | 旧 Hugo 首页至 Sep2025；官方原生 `api/page_config?code=research.research-list` 返回 60 条，最新仅 Dec23,2025。NATIVE_0 保存请求与原日期。 | 受阻 | 当前配置过旧，不能证明 Jan13 没有发布；重开仅本窗官方历史列表或单项原文，不用空 articles 字段作零命中。 |
| SRC-DEEPSEEK | 首页与 [news](https://www.deepseek.com/news/) 原索引：动态 Apr24,2026→Dec1,2025，研究 Jan28→Engram Jan12→mHC Dec31；Engram 精确 v1/README 提前公开线索另核。NATIVE_0、PRIOR_README_EXACT。 | 已检查 | 单页索引不是已删发布或首公开分钟证明；Engram 全球首公开判断精确隔离。 |
| SRC-MOONSHOT | Platform Blog 单页 26 条，最新 Nov7,2025；Kimi CLI 100 release 原返回仅保 Jan12 v0.76 published13:11:16Z 与 Jan15 v0.78 published17:26:14Z 有限锚。DATE_FIELDS_0。 | 受阻 | 旧 blog 未覆盖 January；release 有限索引不替代全部研究/已删事件，未将不在本窗的版本当新候选。 |
| SRC-TENCENT-HUNYUAN | Research 首查；原生 publicList POST page1,size20,renderType0 返回 total9，最早 Feb3,2026，原 publicAt/displayPublishTime 分开。浏览器 IAB/Chrome 无可用控制入口，记录在 BROWSER_HISTORY_LIMIT。 | 受阻 | 本窗动态历史列表尚不可恢复；不能把返回9条当 January 零事件。重开原窗口列表/原文即可。 |
| SRC-ZAI | Research 单页有 Jan19→Jan13 GLM-Image→Dec10/9 锚，原嵌入 createAtJan13T16Z 与 April 迁移 createdAt 分开；项目正文/model card 已读。NATIVE_0、CORE_2、DATE_FIELDS_0。 | 受阻 | GLM-Image display 日期、迁移字段与 Jan12 repository commit 不足确认首公开落窗；单项日期隔离，不授仓库创建=公开。 |
| SRC-BYTEDANCE-SEED | Research 首页；论文 API article_type1,count20,order_desc=false,publish_year2026，total82/has_moretrue/next20，首批最早 PublishDateJan19T16Z 已越过本窗，停止后页；不扫全年库存。NATIVE_0。 | 受阻 | 该排序论文切片不支持 January 博客历史完整性，技术博客本窗仍不可恢复；保精确原入口而非无事件断言。 |
| SRC-BAIDU-ERNIE | 中文及英文 Blog page1，Jan29→Jan15→Jan8→Dec23 有序可见；相邻项仅榜单，停止跨窗，不读取 page2 的旧年库存。OFFICIAL_FINISH_1。 | 已检查 | 只当前 page1 有限邻接；不把后来的 ERNIE5.0 技术报告或既有排名宣传当本窗机制。 |
| SRC-XIAOMI-MIMO | 官网 Paper8条 June29→Jan8Flash→Oct21，Blog15标题未标日期；有限窗口定位停止。SOURCE_MAIN_3。 | 受阻 | 未标日期的 Blog 本窗历史覆盖隔离；论文标题/发布时间不能补造博客日期。 |
| SRC-MINIMAX | 英文 Blog/news 与中文 Blog 原有限单页，中文重定向 minimax.cn；13项日期可见 Jan28→Dec23→Oct27→Jan15,2025，停止跨窗，不沿旧年继续。OFFICIAL_FINISH_1。 | 已检查 | 单页/迁移界面不授删除历史或 Agent TechBlog 本窗完整性；无可核本窗新机制，不把后续版本移入本窗。 |
| SRC-ARXIV | 四主题 Submitted缓冲 `[202601091900,202601121900]`，按 submittedDate descending，页长25；CL/LG191共8页0～175尾16，DC/AR/PL/OS/PF11一页，AI/IR/MA129共6页0～125尾4，CV/RO43两页0/25尾18。17实际页374行/334唯一ID，原主题及逐页 URL见 ARXIV_TITLES_0/REST；只标题身份浏览，21 exact-v1 AB（原16+定点5） 与必要核心另保存。 | 已检查 | Submitted 不是公开日期；API 当前返回 revision，不授旧 submitted 项在本窗的重要 replacement 已全覆盖。未执行不支持的 lastUpdatedDate query。历史 announcement/revision 覆盖隔离，只已核个体公开区间支持正式项。 |

## 3. 候选与判断

目前 17 个本窗家族已按实际题摘贡献/原分校准，全部必要owner窄写与非作者POST已结束，root最终独立日级复核通过。评分对象是本篇新增的拟采用命题，不随是否改书或读取费时调整。所有下列区间都含起点、不含终点；它们由官方公告规则与真实 ID 注册上界联合界定，不是 DataCite 的“first-public”日志。日期留项不混入这十七项。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Peformance Isolation for Inference Processes in Edge GPU Systems](https://arxiv.org/html/2601.07600v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:06:46+08:00 | 计算 SM 分区不保证 power/frequency 时序隔离，有限稳定 profile 不等 WCET；2+2+2=6 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` [Ch63 sharing](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head](https://arxiv.org/html/2601.07832v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:12:19+08:00 | 单累加矩阵改为 block-summary bank，表示容量需与 M 布局/跨块混合成本分账；2+1+3=6 | 深入完成 | 整合：`MODEL-LONG-CONTEXT` [Ch22 block bank](../../../../books/part-02-model/22-long-context.md) |
| [d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation](https://arxiv.org/html/2601.07568v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:06:01+08:00 | 蒸馏 teacher 决定揭示顺序而 gold 决定内容，顺序与正确性两个权限；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24揭示顺序](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference](https://arxiv.org/html/2601.07667v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:08:27+08:00 | selector-depth 决定永久支持裁剪，与跨层 index reuse 及 one/two-pass 不同；2+1+2=5 | 深入完成 | 整合：`INFER-PREFILL` [Ch43 selector-depth](../../../../books/part-05-inference-system/43-prefill.md) |
| [Are LLM Decisions Faithful to Verbal Confidence?](https://arxiv.org/html/2601.07767v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:10:45+08:00 | reported-confidence 下的动作一致性不等真实正确率/内在 belief，修正量化对象；3+1+2=6 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66 confidence/ranking/acceptance](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Reference Games as a Testbed for the Alignment of Model Uncertainty and Clarification Requests](https://arxiv.org/html/2601.07820v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:12:03+08:00 | 票样本一致性、澄清行为与实际信息收益错位，需保预算/信息人口；2+1+2=5 | 标准完成 | 仅报告 |
| [ARCQuant: Boosting NVFP4 Quantization with Augmented Residual Channels for LLMs](https://arxiv.org/html/2601.07475v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:03:44+08:00 | 同格式残差通道及配对权重列扩展，在硬件统一格式约束下替代高精度补偿；2+2+2=6 | 深入完成 | 整合：`INFER-TENSORRT-LLM` [Ch49同格式补偿](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Efficient Diffusion Transformers](https://arxiv.org/html/2601.07396v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:01:52+08:00 | 固定参考子空间 forecast 与 residual hold 分责，不是每输入最佳 SVD；2+1+2=5 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24缓存误差](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [On the Non-decoupling of Supervised Fine-tuning and Reinforcement Learning in Post-training](https://arxiv.org/html/2601.07389v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T12:01:42+08:00 | 审其严格互损条件；KL band 不足授 reward 严格曲率，原恒等式/有限观察分开；2+2+2=6 | 争议 | 暂缓 |
| [Inference-Time Alignment for Diffusion Models via Doob's Matching](https://arxiv.org/pdf/2601.06514v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:41:17+08:00 | terminal-weight/noised-regression 值拟合与 gradient/log-guidance 接口，需 positive denominator/正则成本；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-GENERATIVE-PARADIGMS` [Ch24引导接口](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [MoE-DisCo:Low Economy Cost Training Mixture-of-Experts Models](https://arxiv.org/html/2601.06857v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:49:14+08:00 | 去 gate 单专家独训改变训练函数，shared-backbone 合并及 jointFT 与 EP/DP 等价性不同；2+2+2=6 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36训练函数替代](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Mosaic: Unlocking Long-Context Inference for Diffusion LLMs via Global Memory Planning and Dynamic Peak Taming](https://arxiv.org/html/2601.06562v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:42:24+08:00 | mask-ratio 动态峰与全 loop alias/lifetime 资格连接 chunking/VMM，资源可容纳不等语义长上下文；2+2+3=7 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54动态峰与寿命](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Why LoRA Fails to Forget: Regularized Low-Rank Adaptation Against Backdoors in Language Models](https://arxiv.org/html/2601.06305v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:36:29+08:00 | 投毒基座继承风险，更新强度/方向与rank及clean/ASR分账；2+2+2=6 | 深入完成 | 整合：`TRAIN-LORA` [Ch30基座继承风险](../../../../books/part-04-training-system/30-lora.md) |
| [On the Fallacy of Global Token Perplexity in Spoken Language Model Evaluation](https://arxiv.org/html/2601.06329v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:37:02+08:00 | global/local conditional/无prompt校正与实际生成的测量对象分责；2+1+2=5 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66条件化metric对象](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SkyNomad: On Using Multi-Region Spot Instances to Minimize AI Batch Job Cost](https://arxiv.org/html/2601.06520v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:41:26+08:00 | gang迁移的spot寿命/coldstart/egress/deadline效用分账与条件回退；2+2+3=7 | 深入完成 | 整合：`PLATFORM-GPU-SCHEDULER` [Ch63跨区域spot效用](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) |
| [Garbage Attention in Large Language Models: BOS Sink Heads and Sink-aware Pruning](https://arxiv.org/html/2601.06787v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:47:36+08:00 | BOS attention代理、功能消融与实际执行shape/加速各有权限；2+1+2=5 | 深入完成 | 已有覆盖：`MODEL-MULTI-HEAD-ATTENTION` [Ch15head冗余分责](../../../../books/part-02-model/15-multi-head-attention.md) |
| [PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization](https://arxiv.org/html/2601.07182v1) | 2026-01-13T09:00:00+08:00 ～ 2026-01-13T11:56:49+08:00 | entropy分段PRM局部项与trajectory outcome shift分责；2+2+2=6 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33process/outcome](../../../../books/part-04-training-system/33-grpo.md) |

## 4. 证据与知识整合

日期：官方 [availability](https://info.arxiv.org/help/availability.html) 明确 ID 随 announcement 分配、不能 advance/backdate；Friday14ET～Monday14ET 正常 Monday20ET 公告，本轮 Jan9T19Z～Jan12T19Z 提交缓冲最早公开 Jan13T01Z。各 v1 原 Submitted/Updated、Available月份、created/registered 原值在 [DATE_FIELDS_0](../_sources/daily-20260114/DATE_FIELDS_0.jsonl)、[DATE_FIELDS_1](../_sources/daily-20260114/DATE_FIELDS_1.jsonl) 与新增五项 [RESUME_FIVE_DATE_FIELDS](../_sources/daily-20260114/RESUME_FIVE_DATE_FIELDS.jsonl)。registered 只作为真实 ID 已存在的公开上界，结合无提前 ID 与具体公告批次才构成上述全落窗区间；不把 Published=2026 或 Available=2026-01 精化成时刻。root实际核五项条件区间完全落窗，不授精确日志；PRPO v2 UpdatedJan14T01:26:15Z在窗后，仅采用exact-v1。必要早公开线索另处置，当前 revision 题名不替换 v1 身份。

### [Peformance Isolation for Inference Processes in Edge GPU Systems](https://arxiv.org/html/2601.07600v1)

[批次1](../_sources/daily-20260114/EVIDENCE_1.md) 记录 GPU exact-v1 §III/IV/Alg1/V-B–D：A10040GB/CUDA12.1/PyTorch2.4.1 与 Nano/AGX、六分类 workload、不测 LLM 或 accuracy。3×1000 有限验频不是 WCET；AGX 同时改 power/bandwidth 不能单变量因果。已在 `PLATFORM-GPU-SCHEDULER`（Current Ch63/Legacy Ch59）[sharing节](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md) 增一段，root 原源/owner及实际写后通过。

### [MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head](https://arxiv.org/html/2601.07832v1)

[批次2](../_sources/daily-20260114/EVIDENCE_2.md) 保 MHLA §4/Table1 与 direct ablation：静态 learned M×M mix 并非输入 router；O(Nd²+M²d²)/O(Md²) 需绑定 M 布局。AR prefix 与 NLP训练人口冲突只隔离这些子命题，不否双向/视觉机制。`MODEL-LONG-CONTEXT`（Ch22/Legacy Ch22）[feature-order→blockbank](../../../../books/part-02-model/22-long-context.md) 两段已 root 写前、jan01 写后通过。

### [d3LLM: Ultra-Fast Diffusion LLM using Pseudo-Trajectory Distillation](https://arxiv.org/html/2601.07568v1)

d3LLM §3/A.6/A.7：teacher order-only 即使错最终答案，CE 仍是 gold；fully-unmasked 的 stabilizing 不授永久 KV。Dream/LLaDA训练与 target model 不同，TPF/AUP 不等总成本。`MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24/Legacy N/A）[masked揭示顺序](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 一段及源注 root 写前、jan01 写后通过，不再重复原 cache 通则。

### [Adaptive Layer Selection for Layer-Wise Token Pruning in LLM Inference](https://arxiv.org/html/2601.07667v1)

ASL §4/5、Tables2–9/C.3：recent-layer top-k rank variance 是选择代理而非证据充分；single-pass 已付早层计算与 two-pass restart 分账，Full-before 与预算输入支持不同。H100/HF/FA2、未披露 precision/batch/concurrency，不授 SLO；B2小数与表冲突不采用。`INFER-PREFILL`（Ch43/Legacy Ch39）[Full/Shared→selector-depth](../../../../books/part-05-inference-system/43-prefill.md) 一段及源注 root 写前、jan01 写后通过。

### [ARCQuant: Boosting NVFP4 Quantization with Augmented Residual Channels for LLMs](https://arxiv.org/html/2601.07475v1)

[批次3](../_sources/daily-20260114/EVIDENCE_3.md)：ARC §3/AppendixD 的主激活量化→selected residual同格式量化→配对 W 列/K+S/interleaved packing，只适配对应 NVFP4 执行接口，不授任意 GEMM。RTX5090/PRO6000、Wiki128×2048 seed0校准与有限 prefill；额外在线 reorder/量化和 weight duplication 成本，scalar error bound 不是任务保证。`INFER-TENSORRT-LLM`（Ch49/Legacy Ch45）[SVDQuant后补偿分支](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 两段及源注，root 原源/owner、jan01 实际写后通过。

### [Forecast the Principal, Stabilize the Residual: Subspace-Aware Feature Caching for Efficient Diffusion Transformers](https://arxiv.org/html/2601.07396v1)

SVD Eq8/9 为固定参考 FVkVkᵀ 投影；principal EMA 与 residual hold 都是近似，低能量不是输出无害。FLUX/HunyuanVideo50step、accelerated-reference PSNR 与原全精度质量不同；更长间隔有退步。Hardware/precision/batch/concurrency、完整预处理预算 Not Disclosed，不采用 headline 速度。Ch24[cache误差状态](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 一段及源注，root 原源/owner、jan01 写后通过。

### [Are LLM Decisions Faithful to Verbal Confidence?](https://arxiv.org/html/2601.07767v1)

RiskEval §2/3/B.1：PC/regret 在 reported c 下判行动一致性，不是内在 belief、概率正确性或真值。HLE/GSM128等固定人口、API/open mixture、GPT4o-mini parser/judge、unsupported图像跳过，完整预算 Not Disclosed。`PLATFORM-EVALUATION-SYSTEM`（Ch66/Legacy Ch62）[confidence/ranking/acceptance风险分账](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 2286–2338 实际承载该判断，root 必要源/具体正文核通过；不声称已含 PC 公式或本篇全部 recipe。

### [Reference Games as a Testbed for the Alignment of Model Uncertainty and Clarification Requests](https://arxiv.org/html/2601.07820v1)

Reference Games §3/Table1/AppendixE/F：五票一致性与单次 clarification 预算不同，信息改写/专家标签改变人口；relaxed accuracy 把请求算成功不等任务完成。只是有限 color-grid controller 行为案例，未建立可预算匹配的可靠澄清选择机制，保报告，不借主题相似声称 exact recipe 已覆盖。原5标准必要原源已 root 通过。

### [On the Non-decoupling of Supervised Fine-tuning and Reinforcement Learning in Post-training](https://arxiv.org/html/2601.07389v1)

[批次4](../_sources/daily-20260114/EVIDENCE_4.md) 保存四项必要原源、反侧与 actual owner 提案。Non-decoupling 原 §3 Theorem3.1 需 pSFT=pdata/C1≥0；§4 Assumption3 的 KL band 不能自行推出 unregularized J 严格 growth。有限反例 r≡0、pRL=reference=(.5,.5)、pSFT=(.75,.25)，KL≈.130812 落 [.1,.2] 而 J 恒0，无严格 C2>0。root 已实际核，中心采用隔离；不否 KL 恒等式、Prop1 shift 上界或有限 CoLA 实验，不做全论文作废。重开只需严格曲率/目标/支持假设或勘误与对应实现结果。

### [Inference-Time Alignment for Diffusion Models via Doob's Matching](https://arxiv.org/pdf/2601.06514v1)

PDF 首页 Jan13,2026，arxiv页眉 v1 Jan10 与 HTML later build 日期分开；P8–9 Eq3.13/16–19 同 noised-base terminal-weight regression+gradient penalty+∇h/h。root 已核 PDF 身份与有限源→Ch24具体 gap；[Ch24函数/导数→终点权重引导](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) 实际一段及末注已 root 非作者写后通过。只采用值/输入梯度/正分母三层接口与付费训练、低噪声边界，不采用任意 NN 默认完整 W2 定理。

### [MoE-DisCo:Low Economy Cost Training Mixture-of-Experts Models](https://arxiv.org/html/2601.06857v1)

必要 exact-v1 §3.1–3.2/Alg1、§4 Tables1–3/cluster反侧与 Appendix C–E，详见批次4。单专家去gate、完整shared backbone按数据簇独训后拼接experts/平均shared再jointFT，改变训练函数，并非EP/DP等价。BF16/batch16/seq1024、4×RTX4090→1×A10080GB；正文weighted与Alg1均匀平均不统一，Table1仅fine-tune steps不当全预算可比，AppD最大分支wall-time与GPU-hours分开，也有LlamaWiki PPL退步。不采用globalopt、nearconstant expert cost或普遍倍率。`TRAIN-DISTRIBUTED-TRAINING` [Ch36 localSGD/共识→训练函数替代分支](../../../../books/part-04-training-system/36-distributed-training.md) 实际一段及末注已 root 必要源→owner与非作者POST通过；未运行实现/复现。

### [Mosaic: Unlocking Long-Context Inference for Diffusion LLMs via Global Memory Planning and Dynamic Peak Taming](https://arxiv.org/html/2601.06562v1)

必要 exact-v1 §3/4.2–4.5/5 与 alias/barrier、dummy-input 和累积消融边界，详见批次4。注册全loop的alias/lifetime/barrier资格，currentmask/tokens实例化后只减logits或FFN当前峰，直到可容纳或非chunkable止；firstfit/VMM绑定与custominplace遵守同一计划，不以虚拟地址等于物理占用。RTX3090-24GB/A10040GB、LLaDA8B/Dream7B/LLaDA-MoE，dummy-input最大容量不是语义长上下文，perstep不是全request/concurrency SLO；累积ablation同时换inplace算子，不授独立因果或所有shape最优。Precision/并发/完整质量预算 Not Disclosed，不采用headline性能。`INFER-GPU-MEMORY` [Ch54 Step-peak→动态峰与生命周期资格](../../../../books/part-05-inference-system/54-gpu-memory.md) 实际两段及末注已 root 必要源→owner与非作者POST通过；未核代码或复现。

### [Why LoRA Fails to Forget: Regularized Low-Rank Adaptation Against Backdoors in Language Models](https://arxiv.org/html/2601.06305v1)

[五项定点证据](../_sources/daily-20260114/EVIDENCE_5.md)保存§3/4.2/5与A.1/A.2。基座dropout、谱soft penalty/top3层缩放是有限recipe，pretrained谱非trigger oracle；Eq10未给截断维度，完整正交基penalty退为factor norm，不能补造top-k实现。Prop4.2原A1上界在证明Eq16被换成下界，有限反例满足原假设但缩放后margin仍负，只隔离该阈值保证，不删有限实测。BERT/RoBERTa/Llama、BadNet/InSent、三个分类集与RTX5060Ti/3090、rank8/16；部分baseline引用旧论文、其他best-of-runs，非同预算均值，precision/fullruntime未披露。root必要原源→owner通过，`TRAIN-LORA` [Ch30继承基座→继承风险](../../../../books/part-04-training-system/30-lora.md)实际一段/邻接/末注root非作者POST通过，不授通用遗忘或安全。

### [On the Fallacy of Global Token Perplexity in Spoken Language Model Evaluation](https://arxiv.org/html/2601.06329v1)

必要§3 Eq3/4、§4/5.2–5.3/Limitations：globalNLL、共享prefix后0.5s conditionalNLL、减无promptNLL和实际生成MOS不是同测量对象；embeddingjudge资格在同benchmarkprompts选择，不能授独立跨域真值。SALMon六属性、9model×50sample×5annotators；局部/归一化HuBERT反侧、compoundshift未测，双score/judge成本保留，GPU/precision/concurrency/fullcost未披露。root必要原源→owner通过，`PLATFORM-EVALUATION-SYSTEM` [Ch66 EvalSpec→条件化metric](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际一段/邻接/末注root非作者POST通过，不授普遍ranking或无误校准。

### [SkyNomad: On Using Multi-Region Spot Instances to Minimize AI Batch Job Cost](https://arxiv.org/html/2601.06520v1)

必要§4.1–4.7/§5/§6.1–6.2.5只采用固定gang寿命估计、coldstart/checkpoint/egress/deadline效用和条件on-demand回退，probe非预约承诺，knownP/d界/ondemand始终可用是前提。AWS Qwen3-4B/14B、4L4/8A100/4A10G，30hwork/45hdeadline、100/500GB/6mincoldstart；GCPH10014day与AWSV100traces模拟20jobs，非生产保证。无slack全回退、单region无候选益、region收益饱和、大checkpoint反侧与部分11/12%结果不能被headline10%覆盖；地理eligibility非法律合规认证。root必要原源→owner通过，`PLATFORM-GPU-SCHEDULER` [Ch63 restart→跨region spot效用](../../../../books/part-06-ai-infrastructure/63-gpu-scheduler.md)实际一段/邻接/末注root非作者POST通过；precision/batch/fullquality未披露，不授无条件deadline或全局最优。

### [Garbage Attention in Large Language Models: BOS Sink Heads and Sink-aware Pruning](https://arxiv.org/html/2601.06787v1)

必要§3–4/6–8/Limitations：MMLU初始decodeBOSattention是候选代理，WO slice置零维持shape不是物理kernel剪除/实测加速。GQAGemma3-4B/Llama3.1-8B/Qwen3-4B、4096max、WikiText及8任务mixedshots；Llamablock25%明显反退且TopDown优于作者方法，headPPL与downstream排序不同，softmax1/T不推出BOS必1/T。hardware/precision/calibrationbudget/runtime未披露，未运行实现。`MODEL-MULTI-HEAD-ATTENTION` [Ch15 head冗余段](../../../../books/part-02-model/15-multi-head-attention.md)111–119实际已有proxy≠功能/生产加速分责；root必要原源与具体Existing通过，不冒称已含exact评分recipe，不重复写正文。

### [PRPO: Aligning Process Reward with Outcome Reward in Policy Optimization](https://arxiv.org/html/2601.07182v1)

必要§3/4/6/7及B/C：entropy峰segment的PRM项按token广播，加trajectoryoutcome shift，固定0.5/0.289为uniformprior尺度非实际校准，entropy非语义oracle。8H200policy+8H200PRM、batch128/group8/2048tokens、MATH12k与earlystopepochs不同；MATHgreedy和AMC/AIME32均值人口不合并，random/uniformsplit大退步、AIME2025反退与step46.8→80.8/84的PRM成本保留，非同总预算普胜。作者承认collapse证明不完整；不采用保证。root已实际必要原源→owner通过，`TRAIN-GRPO` [Ch33 coarse→local process/outcome](../../../../books/part-04-training-system/33-grpo.md)一段/前后邻接及末注已root非作者实际POST通过；precision/fullcost未披露，未复现。

### 具名贡献前与窗前关闭（不评分）

以下是实际收窄入口后的判断样本，不是对334标题库存的全量题摘验收。OpenTinker、Zenken、Veo、MedGemma/MedASR、PBT与AIConfigurator拟选机制prior的具体关闭理由已由root实际核准：

- [AIConfigurator](https://arxiv.org/html/2601.06288v1)：§4.2–4.4拟选的校准operator库→迭代性能模型→配置搜索/多backend已有 [v0.4.0公开release](https://github.com/ai-dynamo/aiconfigurator/releases/tag/v0.4.0)（2025-11-24T17:01:01Z）与精确ref README；power-law assignment也在同ref collector的L58/96–111/167–206/301–309存在。原文新实测不据此一并称窗前，所选机制没有新的本窗差额。依据 PRIOR_PUBLIC_0、PRIOR_README_EXACT.output（两行JSON）与 AIC_PRIOR_POWERLAW.output（单行JSON），不将release内普通修复名当重要修订。
- [OpenTinker](https://arxiv.org/html/2601.07376v1)：完整题摘及决定性§2.1–2.3/§3.2已读；新增实现组合是Ray任务资源管理、action-only token mask、rollout/update global barrier与phase turn tracker。§3的功能reward趋势未建立新的归因/故障恢复或一致性条件，不能只用FSM/控制面术语把已有执行组合升为长期贡献。恢复时仅补原缓存不足的L162–200，保存在 OPEN_TINKER_DECIDING_RESUME。
- [Zenken](https://openai.com/index/zenken/)：ZENKEN原核心L29–76给销售流程及业务自报比例，未披露模型、执行或可比较的评价设计变化；不把采用率/业务收益作为机制贡献。
- [Veo3.1更新](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/)：SOURCE_RECOVERY_1.result.value L262–304给reference-image一致性、9:16/upsampling和API发布，以及既有SynthID检查入口；没有公开新的conditioning/consistency机制或可比质量/资源证据，不从功能名推断架构。
- [MedGemma1.5/MedASR](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/)：OFFICIAL_2.result L131–151/189–190给多slice/patch、纵向Xray输入与局部医疗指标，不建立新的可迁移融合、表示或顺序机制；MedASR原核心给Conformer/CTC医疗dictation微调和WER对照，不因医学名称排除，而因没有新增主线机制/设计边界。当前cards已含April/May更新，不据其反推January精确技术事实。
- [Anthropic PBT](https://www.anthropic.com/research/property-based-testing)：SOURCE_RECOVERY_1.result.value L24明确2025NeurIPS，OFFICIAL_2.result末 [2510.09907v1](https://arxiv.org/abs/2510.09907v1) 提供先公开身份；agent读文档→properties/Hypothesis→reflection原机制先公开。新增人工报告/确认的bugs披露不授新算法，也不冒称所有bug或修补已验收。

## 5. 缺口与下一步

普通扫描、筛选、必要审阅与Books修改/POST待办为零；五项定点漏收已补完整题摘/必要源/原分校准和条件日期实际独立核，RoRA/Speech/Sky/PRPO四actualPOST及Sink具体Existing通过。AIConfigurator指定v0.4 release/原SHA power-law机制prior已root实际终裁，本日六部分最终独立日Gate已root实际通过，当前无普通可执行待办；不扩334库存，不用外部来源局限替普通审阅。有效旧证据复用，STOP保最新唯一恢复层。

本窗终态保留项（不用于正面证据、Books、性能/安全或无遗漏断言；仅按各项定点重开条件恢复）：

- [Engram07372](https://arxiv.org/html/2601.07372v1)，原8已读必要机制/评价。arxiv区间可全落窗，但初始 README 同题 PDF 提前 repo 线索，commit/created 不等 public；Jan13T03:47:53Z 第一个外部 PR 只给上界。全球首公开身份未定，不以注册等于首次公开。重开只需当时公开 repo 事件或作者首次正文记录，不无限 archive。
- [Sherry07892](https://arxiv.org/html/2601.07892v1)，原6完整题摘准入；SubmittedJan12T08:49:34Z，UpdatedJan14T01:01:19Z/registeredJan14T02:38:08Z 在本窗终点外，无法确认完全落窗。只恢复真实首次公告/作者公开记录，不机械平移。
- GLM-Image：display createAtJan13T16Z、April迁移 createdAt 与 Jan12 commit 矛盾粒度不足；已有技术正文不授准确首公开。需要原发布日志/可信首次正文区间，不把 property 午夜占位或当前 model card 当日志。
- Non-decoupling 中心严格互损采用链按 §4 隔离。只有 missing strict-growth/目标一致性条件或修正版重开，不继续全部数学附件审计。
- 来源历史限制：Qwen陈旧目录、DeepMind/Seed博客/Hunyuan/MiMo未恢复本窗历史，Moonshot旧Blog与有限release之外、arxiv旧 submitted replacement/公告覆盖均精确保留。可接受替代仅原窗口官方列表/具名版本或已列有限入口，不扩机构全年和未变化 revision。

窗外/贡献前项：AIConfigurator v0.4 published2025-11-24T17:01:01Z 的 How It Works 与 exactref power-law collector 已公开，root实际核指定SHA的α1.01/1.2 inverseCDF workload及README/operator模型搜索后prior关闭通过，不宣称v1全部实测窗前；OpenTinker既有资源调度/状态mask/协调组合及Zenken/Veo/MedGemma/MedASR/PBT具名负侧，已root实际必要核心复核通过，不凭机构或领域标签。

## 6. 复核

复核者：root、jan01_v3（分批具名）；最终独立整日复核：root，通过。

结论：通过

通过范围为有限来源切片与终态保留，不授无遗漏。root 已实际16题摘首批中15潜在准入、GPU/MHLA/d3/ASL/Risk/ARC/SVD/Reference必要原源及 owner、Nondec中心反例与 Doob有限源/身份。GPU实际POST由root，其余五实际POST由jan01_v3，仅新段/邻接/源注，不冒称重复所有附件。必要 source 与实际 POST 分层复用，未变化的判断不重读。

Doob、MoE-DisCo与Mosaic实际新段/邻接/末注也已root非作者POST通过，并同步本报告。root实际核OpenTinker§2.3/§3、Zenken29–76、Veo262–304、MedGemma/MedASR接口/免责声明、PBT与2510v1摘要的具体关闭理由，以及14源NATIVE字段/arxiv分页尾部和有限停止/局限；不冒称全机构历史完整。整日漏收抽查只重开五个具体标题线索，21完整题摘不是全面334AB审读；root已核五题摘贡献/原分、必要核心/owner及条件日期，RoRA/Speech/Sky实际POST和Sink具体Existing通过，PRPO实际正文/前后邻接/末注POST也通过，AIC拟选机制prior实际终裁通过；普通扫描/审阅/Books及独立复核待办为零，root最终日Gate通过。机器V3、链接与限定diff检查见以下记录，不能替代语义Gate。未stage、commit、push，未写LS/索引，保护已有修改。

机器验收：`python3 scripts/validate_research.py --report papers/2026/01/14/README.md`通过1份V3接口/一致性校验；本报告39个本地引用全部存在，六个顶层部分与17候选/17证据项对应检查完成。本报告/本日原源及此次相关Ch24/30/33/36/54/63/66的`git diff --check`无错误；这不替代语义复核，也不声称全仓已有差异无误或本地复现实验。

最终独立范围：root实际顺读本日六部分终稿、17候选/五项新增证据及条件日期、具名负侧与所有隔离重开条件，复用未变化的13actualPOST、2Existing/1OnlyReport/1Disputed有效证据。负侧抽查实际涵盖95个标题/身份线索，发现的五个具体贡献风险已补完整exact-v1题摘/必要核心及owner终处置；其他标题抽查不是全部摘要/全文审读，不授334库存或机构历史无遗漏。此前官方具名负侧及AIC指定v0.4/原SHA机制prior实际终裁通过；来源覆盖仅授权§2的有限切片，§5隔离项不作正面证据或覆盖通过。root据此授最终日Gate通过。
