# Daily Research — 2026-01-22

**规范：** V3
**窗口：** 2026-01-21T09:00:00+08:00 ～ 2026-01-22T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-04T08:01:44+08:00

## 1. 结论

本日有限主题发现与贡献筛选结束，冻结67个唯一候选家族。首8及五批102共110份唯一完整题摘：67候选、41贡献关闭、13358撤回、14327日期隔离；四主题35+68+62+36=201是含重复的发现命中，不是201完整题摘或当日新论文。最终核账重开原遗漏校准的13606/13518：ChartVerse关闭经独立完整AB校准，AgenticRed因same-tools warm-start反侧补最小核心后准入，保留实际改判依据，不按数量缩池。

47项标准审阅、19项深入审阅获得限定证据与处置，1项12269中心exact-sampling争议终态隔离、仅报告可独立支持的有限观察，不称该保证证据通过。Books为65仅报告、1具体已有覆盖、1实际整合POST；67项限定证据/处置全部已逐项非作者通过，排除分层31/41已独立抽检/定点复核，未核10明确列示；来源/日期/冻结与六部分日级Gate已由root独立通过并授权完成；终态隔离不等于相应原源覆盖或争议结论已证。

已准备机制揭示的边界包括：同GPU P/D并行的计算分区不等于带宽隔离；探索head固定不等于共享backbone的行为策略固定；更短结构化输出不等于更低完整成本或正确率；过程偏好reward须与输入顺序一致性分开测。性能和安全结果均限于作者配置，没有代码复现、运行时或生产保证。Books实际新增Ch23两段压缩安全诊断（写后独立通过），MemoryRewardBench具体已有覆盖，Nixie的具体实现与反侧仅报告，不为现有owner缺少某篇配方造diff。

## 2. 来源覆盖

历史查询及原生入口材料集中在[当日材料](../_sources/daily-20260122/STOP.md)。下表只声明实际检查范围；历史目录缺段不授零事件或无遗漏。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/news当前页及官方RSS；窗口定点搜索，RSS `/news/rss.xml`实际XML接口失败/403，当前native不能回到Jan21切片 | 受阻 | 本窗原生研究目录未恢复；不支持完整零命中，恢复本窗官方事件目录后定点重开 |
| SRC-ANTHROPIC | Research及窗口定点官方新闻；constitution原页核心读，Jan22只有日期字段、非精确时区 | 已检查 | 该constitution是训练政策文件说明，无受控新机制证明，贡献关闭；历史Research目录完整性不作保证 |
| SRC-GOOGLE-AI | GoogleResearch `/blog/2026/01/`完整9项到Jan12；DeepMind `/blog/`第4页Jan→Dec边界。Jan22 SmallModels链接EMNLP2025稿，D4RT链接2512.08924 v1Dec9/v2Dec10；VeoJan13与GenieJan29窗外 | 已检查 | 限此原生发表切片；Jan22博客不把旧论文重新计首次公开，不扩到其他年月 |
| SRC-META-AI | 原生publication/search page3到Jan2→Dec26边界，窗口定点检索 | 已检查 | 已检查可恢复相关发表切片，不声称所有历史事件类型完整 |
| SRC-QWEN | 旧站到Sep2025，现`qwen.ai/blog`动态空文本；有限官方窗口检索 | 受阻 | 本窗原生Blog目录缺段，不把空响应当零；13384论文按arXiv家族处理不重复计blog |
| SRC-DEEPSEEK | 官方主页和本窗有限原始发布补检 | 受阻 | 主页无历史列表；本窗官方事件切片未完整恢复，当前不支持零事件 |
| SRC-MOONSHOT | PlatformBlog原生最新2025Nov7，官方org补检和窗口定点检索 | 受阻 | 本窗完整技术发布目录不可据当前org恢复，不把旧静态页当全窗 |
| SRC-TENCENT-HUNYUAN | 首查Research动态空响应；浏览器两次timeout及子线程IAB可见性失败；官方org/T1替代定点，T1本窗commit API count0且无nextLink | 受阻 | T1只支持该repo无本窗commit；Research全部历史切片仍缺，停止无界动态重试，不支持全源零事件 |
| SRC-ZAI | Research原生有序Aug→Feb2→Jan19→Jan13→Dec边界；Jan19 GLM4.7Flash原始发布窗外 | 已检查 | 只声明可见Research/发布段，不扩更早目录 |
| SRC-BYTEDANCE-SEED | Research featured Jan27→Dec2，PublicPapers首段Aug→May；有限窗口主题补检；原生HTML无分页/年份链接，仅同页中英文入口 | 受阻 | 本窗完整论文目录无法从当前有界原生/补检恢复；终态隔离，不由当前条目授历史零事件 |
| SRC-BAIDU-ERNIE | 中文Blog原生page1完整May→Feb6→Jan29→Jan15→Jan8→Dec→Nov，page2更早 | 已检查 | 此可见技术Blog切片窗内无条目；不声明所有artifact发布完整 |
| SRC-XIAOMI-MIMO | 官网Paper8项June/Mar/Feb3/Jan8→旧年；Blog最新V2.6缺历史日期切片 | 受阻 | Paper切片已处理，Blog本窗历史目录不可由当前最新卡证明 |
| SRC-MINIMAX | 英文Blog12项和中文13项完整，Jan27/28→Dec23边界；AgentTechBlog native链接恢复`/docs/llms.txt`及`/docs/techblog.md`，仅2026May13 AgentTeam条目 | 已检查 | Blog可见切片无本窗条目，TechBlog当前完整索引仅May13，不能由此证明Jan时尚不存在或无历史删除 |
| SRC-ARXIV | 官方MLK公告+availability实际读；四有限主题35/68/62/36到单页尾。初始过宽172/148/144/85首25已停止、收窄，不作队列；[查询及标题身份](../_sources/daily-20260122/discovery_narrow.txt) | 已检查 | 直接本日公告列表未恢复；monthly只能身份查漏。本次相关/含糊完整题摘贡献判断及候选必要核心已结束，67项日期逐项核上界；不授全分类召回 |
| 表外：[arXiv公告规则](https://info.arxiv.org/help/availability.html) | [MLK官方公告](https://blog.arxiv.org/2026/01/14/attention-authors-temporary-change-to-announcement-schedule-due-to-mlk-jr-holiday-3/)指定Fri16 14ET～Tue20 14ET accepted cohort于Tue20 20EST公告，即本窗起点；final-ID公告时才分配 | 已检查 | submitted只发现线索，moderation延迟不推测，registered不是精确正文公开时刻 |
| 补检：[DataCite](https://api.datacite.org/) | 只查拟采用final-ID DOI注册身份：[初8](../_sources/daily-20260122/calibration_exact.txt)、[首36](../_sources/daily-20260122/dates_batch1.txt)、[后14](../_sources/daily-20260122/dates_next14.txt)、[最小6](../_sources/daily-20260122/dates_min6.txt)、[最小3](../_sources/daily-20260122/dates_min3.txt)、[新增7](../_sources/daily-20260122/dates_new7.txt)、[AgenticRed](../_sources/daily-20260122/date_red13518.txt) | 已检查 | registered仅公开外部上界；异常/范围不能完全落窗者隔离，不从提交时间挪归属 |
| 表外：[ACL Anthology](https://aclanthology.org/2025.emnlp-main.949/) | Google SmallModels原页明确引用此2025论文，定点恢复旧论文身份，不扫会议目录 | 已检查 | 只用于博客家族/首次事件排除，不等全文新审或本日新论文 |

## 3. 候选与判断

公开范围均为本日官方公告与final-ID注册上界的推定范围，不是正文精确时刻。冻结67个唯一家族如下；原始字段/时区及上界见[首批日期](../_sources/daily-20260122/calibration_exact.txt)、[日期批1](../_sources/daily-20260122/dates_batch1.txt)、[后14](../_sources/daily-20260122/dates_next14.txt)、[最小6](../_sources/daily-20260122/dates_min6.txt)、[最小3](../_sources/daily-20260122/dates_min3.txt)、[新增7](../_sources/daily-20260122/dates_new7.txt)、[AgenticRed](../_sources/daily-20260122/date_red13518.txt)。原submitted只是cohort发现线索，不能推公开时刻；final-ID在公告时分配与arXiv-owned DOI注册外部上界合用，只授完全落窗的范围。跨入口/分类/事件去重不加分母；已关闭的完整题摘与具体理由保留在[准入校准](../_sources/daily-20260122/admission_batch1.md)、[后续校准](../_sources/daily-20260122/admission_batches2-5.md)、[最小核心裁决](../_sources/daily-20260122/decisive_judgments.md)、[尾批裁决](../_sources/daily-20260122/decisive21_judgments.md)，不成为全文待办。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Nixie: Efficient, Transparent Temporal Multiplexing for Consumer GPUs](https://arxiv.org/abs/2601.11743v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:47:04+08:00 | VMM地址与单副本迁移/kernel admission耦合，减thrashing但响应与长任务吞吐有代价；2+2+2=6 | 标准完成 | 仅报告：现有working-set/页ready/映射顺序/reserve链已能解释长期判断，具体Linux层级配方未构成新知识缺口 |
| [RAPID-Serve: Resource-efficient and Accelerated P/D Intra-GPU Disaggregation](https://arxiv.org/abs/2601.11822v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:49:01+08:00 | 共享weights/KV IPC、decode allocation ownership与CU partition改善phase并行取舍；2+2+2=6 | 标准完成 | 仅报告：MI300X CU-mask/IPC实现与作者SLO人口的局部取舍，不更改phase共驻与资源竞争原则 |
| [AGGC: Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training](https://arxiv.org/abs/2601.11864v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:49:59+08:00 | function-group跨层双侧EMA norm band及随时间边界，区别全局maxclip；2+1+2=5 | 标准完成 | 仅报告：经验group/系数局部SFT/RLVR配方，不改一般稳定优化原则 |
| [R²PO: Decoupling Training Trajectories from Inference Responses for LLM Reasoning](https://arxiv.org/abs/2601.11960v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:52:17+08:00 | rollout-residual head和交替训练分支，shared backbone使完全解耦/importance correction未证；2+2+2=6 | 标准完成 | 仅报告：受限结构分支，不采用unbiased/zero training overhead或普遍隔离 |
| [Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models](https://arxiv.org/abs/2601.12042v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:54:12+08:00 | clean-ranking oracle分离视觉语义损伤与压缩rank不稳，离散删选放大攻击差额；2+2+2=6 | 深入完成 | 整合：`MULTIMODAL-REPRESENTATION` [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) paired扰动与offline-ranking诊断两段已写，root POST通过 |
| [MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models](https://arxiv.org/abs/2601.11969v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:52:29+08:00 | process两答案均正确与outcome一错分开，位置交换核顺序一致性；2+2+2=6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66 JudgeRanking/Scorer](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 区分高contrast与近等质排名、位置交换 |
| [Are LLMs Ready for TOON? Benchmarking Structural Correctness-Sustainability Trade-offs in Novel Structured Output Formats](https://arxiv.org/abs/2601.12014v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:53:33+08:00 | paired compact输出token减少但schema/latency退步，native support因果未控；2+2+2=6 | 标准完成 | 仅报告：不以新格式名称改长期owner，不采emissions统一排名 |
| [Threshold Differential Attention for Sink-Free, Ultra-Sparse, and Non-Dispersive Language Modeling](https://arxiv.org/abs/2601.12145v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:56:38+08:00 | length-dependent gate+双view signed attention的statistical survival边界；2+1+2=5 | 标准完成 | 仅报告：162M受限统计假设和局部质量取舍，未改统一attention可靠性判断 |
| [Speculative Sampling with Reinforcement Learning](https://arxiv.org/abs/2601.12212v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:58:09+08:00 | hidden-state条件的TT/depth/topk RL动作与cached persistence；2+1+2=5 | 标准完成 | 仅报告：局部treepolicy成本/greedy验证，不代替一般speculation corrector或SLO验收 |
| [Double-Calibration: Towards Trustworthy LLMs via Calibrating Knowledge and Reasoning Confidence](https://arxiv.org/abs/2601.11956v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:52:11+08:00 | evidenceconfidence监督与finalconfidence分离，SingleCal质量近似但ECE退步；2+1+2=5 | 标准完成 | 仅报告：gold-dependent KG proxy的具体监督/置信接口，非任意truth来源或通用校准保证 |
| [PPA-Plan: Proactive Pitfall Avoidance for Reliable Planning in Long-Context LLM Reasoning](https://arxiv.org/abs/2601.11908v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:51:03+08:00 | 升级planner无专门corrector反降formatvalidity的局部交互；2+1+2=5 | 标准完成 | 仅报告：特定plan actionspace/模型corrector依赖，不授所有强模型需要该recipe |
| [Process In-Context Learning: Enhancing Mathematical Reasoning via Dynamic Demonstration Insertion](https://arxiv.org/abs/2601.11979v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:52:43+08:00 | 固定k/r下staticICL可伤reasoningdistill，interruptgate+confusionrerank局部干预；2+1+2=5 | 标准完成 | 仅报告：两distill模型math和未匹配reflection成本，不更改一般RAG/上下文原则 |
| [Partial Reasoning in Language Models: Search and Refinement Guided by Uncertainty](https://arxiv.org/abs/2601.12040v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:54:09+08:00 | partialprefix变latent-search root而非仅首embedding优化；2+1+2=5 | 标准完成 | 仅报告：该搜索分支与top50entropy代理，未证省算或人类双系统认知 |
| [Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2601.12995v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:16:24+08:00 | 正错strata限制辅助reward不得翻转advantage符号；2+1+2=5 | 标准完成 | 仅报告：相对标签符号约束不等无rewardhacking或更新普保，训练空strata实现ND |
| [Plan, Verify and Fill: A Structured Parallel Decoding Approach for Diffusion Language Models](https://arxiv.org/abs/2601.12247v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:58:57+08:00 | 同commit数/confidencebin的低置信planning anchor优于随机及top1保护filter；2+1+2=5 | 标准完成 | 仅报告：局部commit排序与模型自一致控制，不授真实correctness或wallclock收益 |

| [S2DiT: Sandwich Diffusion Transformer for Mobile Streaming Video Generation](https://arxiv.org/abs/2601.12719v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:09:53+08:00 | 预算先定attention block counts再学习resolution布局，相同counts不等等质量；2+1+2=5 | 标准完成 | 仅报告：移动few-step/quantized部署的局部布局分支，不授fullattention质量等效或DP实峰最优 |
| [FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation](https://arxiv.org/abs/2601.13976v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:39:12+08:00 | nonCoT hardlabel先优化后softaction targets反约束CoTmodes；2+1+2=5 | 标准完成 | 仅报告：LH-VLN共享参数的mode alignment局部接口，不授内部因果reasoning或人类级导航 |

| [DARC: Decoupled Asymmetric Reasoning Curriculum for LLM Evolution](https://arxiv.org/abs/2601.13761v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:34:10+08:00 | 特权documentteacher长>5K反退的局部监督边界；2+1+2=5 | 标准完成 | 仅报告：特定discrepant samples与self-distill配置，不外推更多证据普遍有害 |
| ["The Whole Is Greater Than the Sum of Its Parts": A Compatibility-Aware Multi-Teacher CoT Distillation Framework](https://arxiv.org/abs/2601.13992v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:39:35+08:00 | student空间的gold-likelihoodjump/consensus/NLL共同weightteacher；2+1+2=5 | 标准完成 | 仅报告：特定proxy接口与局部LoRA蒸馏，不能证明真实epiphany或无gradient冲突 |
| [ARC: Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents](https://arxiv.org/abs/2601.12030v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:53:56+08:00 | joint memoryrepair与perturn检查相对checklist-only/延迟trigger的受控局部条件；2+1+2=5 | 标准完成 | 仅报告：ContextManager120B的局部策略差额，总调用成本不等budget守恒 |
| [AgenTRIM: Tool Risk Mitigation for Agentic AI](https://arxiv.org/abs/2601.12449v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:03:40+08:00 | mixedproposal低风险投影与只读executionstatus的highriskjudge接口；2+1+2=5 | 深入完成 | 仅报告：受限riskpartition与proxyjudge，不授leastprivilege或status摘要安全证书 |
| [OFA-MAS: One-for-All Multi-Agent System Topology Design based on Mixture-of-Experts Graph Generative Models](https://arxiv.org/abs/2601.12996v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:16:25+08:00 | 跨任务condition贯穿AR node/edge生成与有限OOD topology反侧；2+1+2=5 | 标准完成 | 仅报告：局部conditional结构分支，不授通用最优topology或工具Agent transfer |
| [Listen, Look, Drive: Coupling Audio Instructions for User-aware VLA-based Autonomous Driving](https://arxiv.org/abs/2601.12142v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:56:33+08:00 | futureego-derived audio输入与目标轨迹的provenance评价反证；2+1+2=5 | 深入完成 | 仅报告：合成nuScenes目标相关输入，不授真实voice或closedloop驾驶泛化 |
| [ReWorld: Multi-Dimensional Reward Modeling for Embodied World Models](https://arxiv.org/abs/2601.12428v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:03:11+08:00 | negativeCFMlossdifference提供可计算policyproxy而非已证likelihood；2+1+2=5 | 标准完成 | 仅报告：局部lossproxy与samplebudget分支，未建立真实PPO correctness或物理真值 |
| [Tolerance Principle and Small Language Model Learning](https://arxiv.org/abs/2601.12179v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:57:24+08:00 | 人工grammar控制types/exposure后type-only阈值与quantal预测不成立；2+1+2=5 | 标准完成 | 仅报告：BabyBERTa受限学习反例，不外推人类或所有LLM |

| [Preserving Fairness and Safety in Quantized LLMs Through Critical Weight Protection](https://arxiv.org/abs/2601.12033v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:54:00+08:00 | 跨语言量化风险与Fisher差额选criticalweights，固定保护比例仍有任务/语言反侧；2+2+2=6 | 深入完成 | 仅报告：AWQ局部保护与proxy安全评测，不授无成本trustworthiness保持 |
| [System-Mediated Attention Imbalances Make Vision-Language Models Say Yes](https://arxiv.org/abs/2601.12430v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:03:14+08:00 | system attention向text/image重分配，balanced yesrate不等所有任务acc改善；2+1+2=5 | 深入完成 | 仅报告：LLaVA单token受限干预反侧，不改通用hallucination防御保证 |
| [A Two-Stage GPU Kernel Tuner Combining Semantic Refactoring and Search-Based Optimization](https://arxiv.org/abs/2601.12698v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:09:22+08:00 | semantic模板显式参数与resource-feasible搜索区别直接改写；2+1+2=5 | 标准完成 | 仅报告：三个SGLang kernels/TitanRTX局部搜索，有限正确性测试不等语义普保 |
| [Left-Right Symmetry Breaking in CLIP-style Vision-Language Models Trained on Synthetic Spatial-Relation Data](https://arxiv.org/abs/2601.12809v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:11:58+08:00 | position-token交叉梯度与定点干预支持toy关系泛化；2+1+2=5 | 标准完成 | 仅报告：1D受控CLIP关系机制，不授真实视觉通用空间表示因果 |

| [PASs-MoE: Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learning](https://arxiv.org/abs/2601.13020v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:16:58+08:00 | lowrank activation energy同时定义routing和历史rank稳定，MathQA存在适应/保持负侧；2+1+2=5 | 标准完成 | 仅报告：fixed-capacity MoE-LoRA局部co-drift控制，不授无忘却或零实际开销 |

| [Simulated Annealing Enhances Theory-of-Mind Reasoning in Autoregressive Language Models](https://arxiv.org/abs/2601.12269v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:59:29+08:00 | 有限退火schedule观察有增量，但精确MH接受比印反向不能授目标分布正确；2+1+2=5 | 争议 | 仅报告：只保留局部schedule/ToM观察，exact-power-sampler中心保证终态隔离 |
| [FlipFlop: A Static Analysis-based Energy Optimization Framework for GPU Kernels](https://arxiv.org/abs/2601.13345v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:24:28+08:00 | PTX+硬件校准预测energy/runtime并筛resource可行配置，非零runtime测量；2+1+2=5 | 标准完成 | 仅报告：NVIDIA MHA配置模型局部适用，不授零校准/最优生产能耗 |
| [ContiguousKV: Accelerating LLM Prefill with Granularity-Aligned KV Cache Management](https://arxiv.org/abs/2601.13631v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:31:07+08:00 | prune/store/prefetch统一tokenchunk降低I/O放大，跨period投机预取；2+2+2=6 | 标准完成 | 仅报告：prefix-offload具体granularity实现，低KVbudget有质量代价非全服务SLO |
| [HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference](https://arxiv.org/abs/2601.13684v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:32:22+08:00 | head稳定度分budget和pivotdrift触发异步satellite检索，带宽依赖；2+2+2=6 | 标准完成 | 仅报告：有限headprofile/proxy阈值实现，不授完全隐藏I/O或全质量保持 |

| [Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2601.13707v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:32:54+08:00 | 共享QKV masked双path与orthogonal correction，surrogate非image-absent真值；2+1+2=5 | 标准完成 | 仅报告：三LVLM局部masked指导实现，singlepass仍有成本和quality负侧 |
| [Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models](https://arxiv.org/abs/2601.14152v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:43:22+08:00 | option hiddenstate不见后context的具体MCQA评价反证，最后answer仍可见全输入；2+1+2=5 | 深入完成 | 仅报告：受限格式/读出路径反证，非所有causal decoder无法利用后context |
| [CTPD: Cross Tokenizer Preference Distillation](https://arxiv.org/abs/2601.11865v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:50:01+08:00 | 同字符span聚合跨tokenizer偏好与teacherreference控制；2+1+2=5 | 标准完成 | 仅报告：局部spanweight/reference接口，未采noise-free或unbiased保证 |

| [Incentivizing In-depth Reasoning over Long Contexts with Process Advantage Shaping](https://arxiv.org/abs/2601.12465v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:04:01+08:00 | 只减failedrollout有效相关step的负advantage，truth-guided policyreference接口；2+1+2=5 | 标准完成 | 仅报告：KG有链QA/privileged reference的局部训练分支，judge非真值 |
| [Linear Mechanisms for Spatiotemporal Reasoning in Vision Language Models](https://arxiv.org/abs/2601.12626v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:07:42+08:00 | objectword去lexicalmean提取位置ID并same-norm干预，局部location输出可变；2+1+2=5 | 标准完成 | 仅报告：简单空间query/至14B的线性读出干预，不授完整视觉内部机制 |
| [Distribution-Centric Policy Optimization Dominates Exploration-Exploitation Trade-off](https://arxiv.org/abs/2601.12730v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:10:07+08:00 | currentpolicy采样+温度target tokenratio双IS分支与moderateentropy负側；2+1+2=5 | 标准完成 | 仅报告：数学RL局部估计分支，未采unbiased序列target或nearoptimal探索保证 |

| [Towards Robust Process Reward Modeling via Noise-aware Learning](https://arxiv.org/abs/2601.12748v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:10:33+08:00 | stepcorrectness区别policycontinuation success，reflectionfilter和迭代软label接口；2+1+2=5 | 深入完成 | 仅报告：mathpolicy/proxyjudge局部标签反证，不把reflection或自信当真值 |
| [Think3D: Thinking with Space for Spatial Reasoning](https://arxiv.org/abs/2601.13029v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:17:11+08:00 | raw3D工具无anchor反退，camera-anchor/ego条件的受控空间探索分支；2+1+2=5 | 标准完成 | 仅报告：有限重建/视角工具与RL设置，未授真实3D普泛或同预算最优 |
| [Confidence over Time: Confidence Calibration with Temporal Logic for Large Language Model Reasoning](https://arxiv.org/abs/2601.13387v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:25:26+08:00 | fixedSTL结构+questioncondition参数校准，跨任务成功/失败模式差额；2+1+2=5 | 标准完成 | 仅报告：tasksegmentation与局部confidenceproxy，未改通用truth/校准保证 |

| [Beyond Memorization: Testing LLM Reasoning on Unseen Theory of Computation Tasks](https://arxiv.org/abs/2601.13392v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:25:33+08:00 | seen/unseen DFA组合一致性和hint失效的具体反证；2+1+2=5 | 深入完成 | 仅报告：有限validator非语言等价证明；公开seen不证明训练见过 |
| [Reasoning is a Modality](https://arxiv.org/abs/2601.13562v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:29:29+08:00 | controller/workspace角色分离同时dense pass与TTT预算影响；2+1+2=5 | 标准完成 | 仅报告：ARC局部结构分支，不授真实内部state或同预算超人类 |
| [Activation-Space Anchored Access Control for Multi-Class Permission Reasoning in Large Language Models](https://arxiv.org/abs/2601.13630v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:31:05+08:00 | permission anchor risk拒绝/吸授权排其他region的局部干预；2+1+2=5 | 深入完成 | 仅报告：单轮proprietary QA激活proxy，不替代外部ACL/认证安全 |
| [Dimension-First Evaluation of Speech-to-Speech Models with Structured Acoustic Cues](https://arxiv.org/abs/2601.13742v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:33:43+08:00 | audio→typedcue分维与bothbad赢家质量分离、总extractor成本；2+1+2=5 | 标准完成 | 仅报告：English离线judge；不是text全面胜audio或最便宜 |

| [Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring](https://arxiv.org/abs/2601.13879v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:36:56+08:00 | 低语言surprisal但高视觉attention的anchor保留与union/intersection局部反侧；2+1+2=5 | 标准完成 | 仅报告：attentionproxy/变实际保留率蒸馏分支，不授grounding真值或无损 |
| [The Side Effects of Being Smart: Safety Risks in MLLMs' Multi-Image Reasoning](https://arxiv.org/abs/2601.14127v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:42:47+08:00 | multiimage误解型safe与正确拒绝分离、同seed单图反侧；2+2+2=6 | 深入完成 | 仅报告：条件选择的合成攻击/proxyjudge，不授安全全因果 |
| [InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2601.14209v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:44:41+08:00 | 当前prefix+firsterror correction SFT，suffix全克隆反损探索的控制；2+1+2=5 | 标准完成 | 仅报告：privileged reference/成功筛选的math训练分支，不授无监督自改进 |
| [Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:45:28+08:00 | BF16train/FP8rollout在长输出/困难task失稳与统一quantization graph反侧；2+2+2=6 | 深入完成 | 仅报告：有限图一致性/训练取舍，不授所有精度统一即onpolicy充分 |

| [Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline](https://arxiv.org/abs/2601.12307v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:00:24+08:00 | 同homogeneous workflow由singleLLM保完整历史/KV的实际对照；2+1+2=5 | 深入完成 | 仅报告：全上下文改变/闭源KV成本理想估算，非任意MAS等价 |
| [Can Deep Research Agents Find and Organize? Evaluating the Synthesis Gap with Expert Taxonomies](https://arxiv.org/abs/2601.12369v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:01:51+08:00 | 给同exactpapers隔离检索后仍低ARI，richerinput提高plausibility却降expertalignment；2+1+2=5 | 标准完成 | 仅报告：expert taxonomy本身非唯一真值；相关非检索唯一因果 |
| [Gated Differentiable Working Memory for Long-Context Language Modeling](https://arxiv.org/abs/2601.12906v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:14:20+08:00 | global/local logprob差utility分配chunk梯度步、minimumcoverage在预算不足时回退；2+1+2=5 | 标准完成 | 仅报告：固定chunk LoRA TTT局部预算选择，非真实记忆价值/无损coverage |
| [The Bitter Lesson of Diffusion Language Models for Agentic Workflows: A Comprehensive Reality Check](https://arxiv.org/abs/2601.12979v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:16:01+08:00 | dLLM selector/editor/记忆/earlyexit角色对照和固定workflow失效差别；2+1+2=5 | 深入完成 | 仅报告：异模型训练/deployment混杂，非diffusion根本不适合Agents |
| [Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2601.13155v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:20:03+08:00 | currentlayer lastquery/key probe与calibratedFFNproxy、stage延迟prune分支；2+1+2=5 | 标准完成 | 仅报告：lastquery与proxy非全tasktruth；局部TTFT/16tokenE2E质量取舍 |

| [Which Reasoning Trajectories Teach Students to Reason Better? A Simple Metric of Informative Alignment](https://arxiv.org/abs/2601.14249v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:45:36+08:00 | student tokenrank/surprisal联合选择teacher/trajectory、同候选池控制；2+1+2=5 | 标准完成 | 仅报告：固定math教师池proxy与测量成本，非最强teacher普遍排序 |

| [From Completion to Editing: Unlocking Context-Aware Code Infilling via Search-and-Replace Instruction Tuning](https://arxiv.org/abs/2601.13384v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:25:22+08:00 | 冻结FIM context限制修复→SEARCH定位旧区段再REPLACE并以同数据格式对照→重新比较生成目标而非只换模型；2+1+2=5 | 深入完成 | 仅报告：限定编辑接口与格式似然对照，安全效果受alignment/数据混杂，未建立长期安全或生成保证 |
| [OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents](https://arxiv.org/abs/2601.13722v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:33:16+08:00 | memory相关性不等于应使用→分开irrelevance/bait/sycophancy/repetition并定点过滤→评价写入/读取收益之外的误用；2+1+2=5 | 标准完成 | 仅报告：合成单轮评价与过滤接口，不证明普遍utility判断或同质量资源优势 |
| [Towards robust long-context understanding of large language model via active recap learning](https://arxiv.org/abs/2601.13734v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:33:32+08:00 | 无差别摘要预算受限→long/short loss-gap选token并回溯来源片段recap→检验选择性回顾的条件收益；2+1+2=5 | 标准完成 | 仅报告：loss-gap是模型代理且recap增算/局部回退，不改变长期状态真实性或无损context保证 |
| [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:59:20+08:00 | 单模态rank攻击忽略耦合→一商品text/image交替优化joint排序目标→评价多模态输入控制对ranker的影响；2+1+2=5 | 深入完成 | 仅报告：单白盒ranker与预算未匹配的联合攻击，不能外推所有商业系统或防御保证 |
| [LR-DWM: Efficient Watermarking for Diffusion Language Models](https://arxiv.org/abs/2601.12376v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:02:00+08:00 | 非顺序生成缺单向prefix→left/right不同key邻居更新green bias→比较局部watermark与检测标定；2+1+2=5 | 标准完成 | 仅报告：邻居相依与经验阈值、非自适应编辑结果，不建立新的密码学或普遍安全保证 |
| [Proxy Robustness in Vision Language Models is Effortlessly Transferable](https://arxiv.org/abs/2601.12865v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:13:19+08:00 | target攻击在vanilla异构proxy上仍有行为差额→低LR warmup/EMA后高LR HPT→检验proxy迁移与clean退化；2+1+2=5 | 深入完成 | 仅报告：有限分类攻击/代理选择下的训练分支，clean/大扰动反侧及额外训练不支持effortless普保 |
| [Beyond Tokens: Concept-Level Training Objectives for LLMs](https://arxiv.org/abs/2601.11791v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:48:13+08:00 | token-supervision忽略替代概念词→给synonym/hypernym概念集逐成员目标→比较augmentation与目标形式；2+1+2=5 | 标准完成 | 仅报告：operational concept集合与分类posttraining控制，不能证明普遍概念理解或generative推理改进 |
| [A Unified Masked Jigsaw Puzzle Framework for Vision and Language Models](https://arxiv.org/abs/2601.12051v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:54:25+08:00 | shuffle仍泄露position梯度→selected token共享unknownPE并保持其他位置→区分augmentation与梯度重构边界；2+2+2=6 | 深入完成 | 仅报告：混合重构指标/攻击预算与排列目标条件，不是完整隐私保证或跨任务可部署结论 |
| [Powerful Training-Free Membership Inference Against Autoregressive Language Models](https://arxiv.org/abs/2601.12104v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T12:55:40+08:00 | 总loss混合预测正确/错误位置→error-position target/reference delta方向比→重估membership测量与reference依赖；2+1+2=5 | 深入完成 | 仅报告：指定logprob/reference及数据人口下的指标，错误零分母/训练混杂限制隐私推广 |

| [AgenticRed: Optimizing Agentic Systems for Automated Red-teaming](https://arxiv.org/abs/2601.13518v1) | 2026-01-21T09:00:00+08:00 ～ 2026-01-21T13:28:28+08:00 | 既有helper权限不保证自动找到好workflow→去高质量archive但保留同tools仍难恢复→重估example warm-start与搜索目标选择；2+1+2=5 | 深入完成 | 仅报告：同helper的初始化反侧与局部diversity条件，增算/静态威胁不建立自动安全评估普保证 |

## 4. 证据与知识整合

### [Nixie: Efficient, Transparent Temporal Multiplexing for Consumer GPUs](https://arxiv.org/abs/2601.11743v1)

root已实际读§2～6、§7关键对照及§8：停新kernel、CUDA同步后迁移，VMM保持虚拟地址；单副本chunk层级、2MB block及streaming reserve与kernel admission协调。100ms API-return idle proxy和MLFQ不是硬deadline。§7.2 Case3 frequent workload长任务吞吐比nvshare W4低23.5%；§8仅Linuxprototype，Windows/AMD是可能port、小模型空间共存未实现。5090 PCIe5×8、host96GB及原model/quant条件，不采租户安全、隔离或生产保证。

Books比较实际读`INFER-GPU-MEMORY` [§Capacity Planning/层级管理权](../../../../books/part-05-inference-system/54-gpu-memory.md)、邻接55/56及63 sharing：已有多进程working-set/切换时间线、compute依赖页ready、稳定逻辑tensor地址与映射提交顺序、reserve操作空间；[56在线抢占](../../../../books/part-05-inference-system/56-inference-scheduling.md)已有compute与KV移交、idle冷却及吞吐代价。该论文提供具体受限实现证据，不足以更改这些长期判断；root批准仅报告，实际Books修改0。

### [RAPID-Serve: Resource-efficient and Accelerated P/D Intra-GPU Disaggregation](https://arxiv.org/abs/2601.11822v1)

必要§3/4/5实际阅读，见[机制原段](../_sources/daily-20260122/rapid_core.txt)、[评价原段](../_sources/daily-20260122/rapid_eval.txt)及[限定判断](../_sources/daily-20260122/evidence_ready.md)。同GPU不同Python进程共享weights/KV IPC，decode owns allocator，prefill仅写已分配block；AMD mask只分compute，不隔离HBM/cache/interconnect。HIP graph launch后mask固定，one-step-ahead多生成token有浪费。8×MI300X、ROCm6.4、vLLMv1 .10.2rc3；Llama3/3.1-70B命名有原文不一致、Mixtral8×7B，precision Not Disclosed。TTFT≤1sec/1000prompt、ITL dense100ms/MoE50ms。32×goodput来自近零baseline；disagg p95ITL平均更低但吞吐较低。只采此配置取舍，不授普遍phase隔离或SLO最优。

### [AGGC: Adaptive Group Gradient Clipping for Stabilizing Large Language Model Training](https://arxiv.org/abs/2601.11864v1)

§3机制、§4.3消融、§4.4 RLVR与Limitations实际读，见[限定判断](../_sources/daily-20260122/evidence_ready.md)。跨层functional group按EMA生成上下norm band，低于下界放大、高于上界裁剪，time schedule早宽晚紧；并非全局clip阈值更换。β表MATH非严格单调；>70B/新architecture/更长context未验证，参数经验调。局部SFT/RLVR结果不证普遍降低variance、统计优越或零成本。

### [R²PO: Decoupling Training Trajectories from Inference Responses for LLM Reasoning](https://arxiv.org/abs/2601.11960v1)

§3/4/Limitations与root§3.4/Eq4–6/§4.1/4.2复核，见[实际原段](../_sources/daily-20260122/review_core_batch1.txt)、[限定判断](../_sources/daily-20260122/evidence_ready2.md)。第一阶段冻结backbone训RO head，第二阶段冻结head却更新共享backbone，πφ behavior继续改变；写πθold ratio，不能采用完全shield/无偏offpolicy。GIF按reward值分箱逆频率，不是语义新颖性；8B GSM略退、GIF不胜mainreward。Stage2峰显存60563高于baseline58519，完整训练成本未披露，不采zero trainingoverhead；detach head只是推理结构分支。

### [Less Is More -- Until It Breaks: Security Pitfalls of Vision Token Compression in Large Vision-Language Models](https://arxiv.org/abs/2601.12042v1)

受影响安全命题定点深入§3/4.2/5.1/5.3/AppF.3，见[原段](../_sources/daily-20260122/review_core_batch1.txt)、[机制/反侧](../_sources/daily-20260122/evidence_ready2.md)。相同扰动图像使用clean-ranking oracle恢复效果，支持排序不稳定而非纯语义损伤的差额；攻击objective控制uncompressed输出偏离，least-important与most-important扰动控制不可混用。白盒需weights/grads/compressor，跨retention/layer有有限transfer而高retention额外信息稀释；未核黑盒query预算，不采普遍成功或所有compression不安全。

Books `MULTIMODAL-REPRESENTATION` [Ch23固定预算/信息责任](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)已有selector预算、attention非因果真值与dense回退；原文新差额是同扰动压缩/未压缩配对及clean-ranking诊断接口。root实际证据/owner批准，正文L409/411与末注L1153已写；oracle特权离线、不授部署guard，白盒与层/保留率/安全质量成本相邻，root非作者POST通过。

### [MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models](https://arxiv.org/abs/2601.11969v1)

§4.1/5.2/5.3/AppC.2已读，见[原段](../_sources/daily-20260122/review_core_batch1.txt)、[解释](../_sources/daily-20260122/evidence_ready2.md)。13 proxy evaluators，context8～128K；temperature.7/top_p.95/maxgen16384，invalid parse算错，低于chance不可直接解释为偏好反向。两答案均正确的过程比较偏第一位置，outcome一错对照相对稳定；主随机化顺序缓解但不证明全面RM失效。未核完整生产/硬件/时延。

Books `PLATFORM-EVALUATION-SYSTEM` [Ch66 JudgeRanking与Scorer不是绝对真相](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)实际已有高contrast判别不能批准近等质排名，以及候选顺序交换、position/style/self-preference与独立校准。root实际正文核准具体已有覆盖，局部memory流程不新增recipe，实际写入0。

### [Are LLMs Ready for TOON? Benchmarking Structural Correctness-Sustainability Trade-offs in Novel Structured Output Formats](https://arxiv.org/abs/2601.12014v1)

§3/4/4.7定点读，见[原始核心](../_sources/daily-20260122/admission_core_actual_incomplete.txt)与[限定判断](../_sources/daily-20260122/evidence_ready.md)；原返回未完整的其他块不授已读。50 paired queries、8模型、RTXA6000/i9/256GB；所有模型均无TOONnative support且只给prompt规范，无native-training控制。JSON→TOON token296.15→217.94而decode9.724→10.007s、render.990→.630/GCS.840→.513；GCS=.2render+.8syntax非semantictruth。忽略firsttoken前processing与repair/retry，不采端到端省时；emissions method和measurement叙述未充分统一，不采节能排名。

### [Threshold Differential Attention for Sink-Free, Ultra-Sparse, and Non-Dispersive Language Modeling](https://arxiv.org/abs/2601.12145v1)

root实际核§4.1/4.2/5/6、Tables2–4和AppA假设。normalizedQK→length√log(i)/d gate→poweredReLU/RMSNorm，双view差是signed weights非概率。O(1) noise survivor依subGaussian/β≥σ；nonDispersion另依relevant survivor bounded；独立noiseviews只令consensus overlap消失，不能说实际learnedviews独立或所有falsematch清零。162M FineWebEdu/8A100，许多acc低softmax、部分Entmax/TRA更高，passkey4K15%vs6%绝对仍低。FP32kernel不作productionlowprecisionSLO；未采用AppB未核数字，完整end-to-end latency/batch/SLO Not Disclosed。仅报告此受限模型分支，不授foundation普遍sinkfree/质量保证。

### [Speculative Sampling with Reinforcement Learning](https://arxiv.org/abs/2601.12212v1)

root实际读Methods/Experiments与Tables1/2。target hiddenfeature复用、TT/depth/topk动作和cached N10train/N30infer persistence；reward平均各episode TPS不等整体总tokens/总time，策略非已证最优。贪婪T0测试不证明非贪婪采样分布lossless。CNN/DM maxlen2200vs2048是混杂且反慢，MaxEntropy对8B速度劣于PPO，cacheinterval80来自trainingdataset题。hardware原文A40(40GB)标法与常见spec冲突不自动改，70B4H100，precision/全部trainingcost/完整SLO Not Disclosed。仅报告该动态树分支的局部结果，不代替现有speculative distribution correctness或质量成本验收。

### [Double-Calibration: Towards Trustworthy LLMs via Calibrating Knowledge and Reasoning Confidence](https://arxiv.org/abs/2601.11956v1)

§4.1/4.2/5.4原段在[decisive_core2](../_sources/daily-20260122/decisive_core2.txt)，§5.1/5.2补核配置。Beta(.5,.5) posterior mean由uniform groundedanswer candidates和gold答案标签确定；原文称MAP与公式mean混用，不采任意KG边truth。proxy SFT path/confidence后RL以gold路径match/F1与Bayesianconfidence alignment训练。SingleCal保quality却去confidence时F1差±1，ECE约4→>20，支持置信证据身份与答案质量分开控制。WebQSP/CWQ、Hits/Recall/macroF1/ECE，primary GPT3.5-turbo reasoner、Llama2-7BChat proxy；未在采用段披露ECE bin敏感性/多seed、hardware/precision/runtime。仅报告这个gold-dependent监督接口，不把局部ECE宣称通用trustworthyreasoning。

### [PPA-Plan: Proactive Pitfall Avoidance for Reliable Planning in Long-Context LLM Reasoning](https://arxiv.org/abs/2601.11908v1)

方法必要原段及§4.3反侧见[core1/2](../_sources/daily-20260122/decisive_core2.txt)。query-only pitfall预测negativeconstraints，planner把约束映射到PEARL actionspace及附加操作，corrector只接最新syntaxerror bounded迭代。GPT4o-mini/Llama3.1-8B/Qwen2.5-14B8bit，QuALITY/ConditionalQA/LongReason/Qasper；表1各method成功交集有selectionbias，不能替全测试表2。GPT planner upgrade无专corrector formatvalidity74.3%低于baseline79.7%，full93.3%；Qwen no-corrector72.9%却高baseline67.4，模型交互不同。平均plan steps增长同时改变pitfall/reasoning组件，不能独立归因或等budget；总LLMcalls/runtime/hardware/SLO Not Disclosed。仅报告受限planner/validator交互，不把成熟约束流程或更长计划当长期新owner。

### [Process In-Context Learning: Enhancing Mathematical Reasoning via Dynamic Demonstration Insertion](https://arxiv.org/abs/2601.11979v1)

§4与内嵌Tables1/2见[core1](../_sources/daily-20260122/decisive_core1.txt)，§5.3/5.4见[core2](../_sources/daily-20260122/decisive_core2.txt)。operative算法监测“wait/maybe”词表，不计算entropy阈值；反思产confusion非空才检索/按query+demo+confusion BGEM3 rerank。k1/r1，R1distillQwen7B/Llama8B与四mathbench。Qwen zero77.7/staticBGEM377.6/PICL83，Llama67.8/65.8/72.7，staticdemo不总改善。Stage1去除每interrupt插semanticdemo、Stage2去除confused时插randomdemo，局部反侧支持时机与内容相互作用；额外reflection/rerank计算未matchedbudget，hardware/precision/end-to-end latency Not Disclosed。仅报告具体干预接口，不把entropy与词表相关性当真实困惑标签或普遍RAG收益。

### [Partial Reasoning in Language Models: Search and Refinement Guided by Uncertainty](https://arxiv.org/abs/2601.12040v1)

§3/4/5在[core1](../_sources/daily-20260122/decisive_core1.txt)、[core2](../_sources/daily-20260122/decisive_core2.txt)，§2reward必要补核。原SoftReasoning优化firstembedding，本分支5条prefix在minimumlength后首个top50entropy≥3bits处设新latent-search root，每path最多一次，BO5samples/project50dim，选最高verifier+coherence reward。verifier通常用LLM black-box MultiGenerate，不是已验证goldoracle或真值；额外BO成本存在。Llama3-8B/Mistral7B/Qwen2-7B，四bench五runs mean±std，baseline引用既有论文不是同budget重跑；QwenGSM8K/LlamaSVAMP局部退步。hardware/precision/runtime/完整token成本Not Disclosed，不采词云的System1/2或introspection叙述。仅报告partialprefix作为优化root的新分支，不宣称省算或稳定普保。

### [Graph Reasoning Paradigm: Structured and Symbolic Reasoning with Topology-Aware Reinforcement Learning for Large Language Models](https://arxiv.org/abs/2601.12995v1)

§3.2.2 Eq14–16、§4.3Table2实际读并root独立核，见[原段](../_sources/daily-20260122/decisive_min4.txt)。按accuracy labels分correct/wrong strata；correct层辅助reward只可非负bonus、wrong只可非正penalty，因此相对label的advantage符号不被graph质量翻转。不是所有rewardhacking消失或更新质量保证，allcorrect/allwrong/emptystrata实现Not Disclosed。Qwen3-8B同RL设置去SCAE在MATH500/AMC23/AIME24退步；§4.1与E.2/F配置已补核：Qwen3-4B/8B Base，math DeepScaleR5K经Qwen8B四次成功分层、丢全错，code KodCodeLightRL10K，avg@3/16分母与32K/8K输出上限不混；[配置原段](../_sources/daily-20260122/readysetup4.txt)、[数据与消融](../_sources/daily-20260122/control13622.txt)。原采用段hardware/precision/总RL训练成本未披露，不授省算。仅报告此hardpriority约束，不因graph cognitive标签名称整合Books。

### [Plan, Verify and Fill: A Structured Parallel Decoding Approach for Diffusion Language Models](https://arxiv.org/abs/2601.12247v1)

§4.2/5.2及AppA.2已读、root独立核，见[原段](../_sources/daily-20260122/decisive_min3a.txt)。在sameblock confidencebin每step仅额外提交1token，planning pool为空回退random匹配commit数，平均confidence差≤.01；支持低confidence semanticanchor优先的局部质量/NFE差额，而非数量偏差。Filter保护当前model highconfidence futuretop1不flip，失败PAUSE/AR fallback；不是semantictruth。NFE按modelforward count，不能忽略多branch、tokenshape、verification成本直接换wallclock；§5.1设置补读见[原段](../_sources/daily-20260122/readysetup4.txt)：LLaDA8B/Dream7B、6bench、length512/block64、highconfidence .9、singleH200、batch4(k3)，同prompt/stopping/genlength，HumanEval pass@1与math exactmatch分开。precision/完整verification与branchwallclock未采用。仅报告commit排序控制，不因planning词汇或NFE数字升级长期可靠性保证。

### [S2DiT: Sandwich Diffusion Transformer for Mobile Streaming Video Generation](https://arxiv.org/abs/2601.12719v1)

§3.3/4.4 [核心与反侧](../_sources/daily-20260122/decisive_min3a.txt)，§4.1/AppD.2 [设置](../_sources/daily-20260122/readysetup4.txt)已实际读并root必要核心通过。budget先选LCHA/SSA counts，再学习相同counts的resolution布置；memory=sum blocks简化不是真实peak。相同trainingcompute/schedule的hourglass与learned布局有局部差额，fullattention质量仍更好却mobile OOM，head dim256质量差于128，不授DP最优可部署或质量等效。

300M images/50M videos、Wan autoencoder4×8×8、CLIPViTL/Gemma3-4Bit，256A10080GB、AdamW1e-4、250K+50K iterations；VBench部分来自leaderboard不同模型/分辨率不可同budget归因。mobile仅CLIP，CoreML iPhone16ProMax，DiT neuralengine/VAE GPU、activation8bit、weights多4bit敏感层8bit，3latentframes→12pixelframes、KVwindow2、4steps；total1124ms/fps10.7是此chunk设置，non-mobileBF16不是同precision直接吞吐比较。仅报告受限布局/资源分支，不因mobile配方缺位改长期Books。

### [FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-Language Navigation](https://arxiv.org/abs/2601.13976v1)

§3.5/3.6/4.3 [机制与消融](../_sources/daily-20260122/decisive_min2b.txt)，§4.1 [设置](../_sources/daily-20260122/readysetup4.txt)已实际读、root必要核心通过。先nonCoT hardaction CE更新，再其softaction targets约束text/visual/multimodalCoT branches，共享参数交替优化；原文未显式stop-gradient，不能补造。nonCoT推理沿用AuxThink，新增不是这个成熟推理路径。

LH-VLN同trainset、validation选checkpoint，test tasks/scenes未见；部分baseline按原论文重实现，不是同token/trainingcompute。去alignment SR0→2.44/ISR2.39→11.01仍整体低，full4modes不是所有指标最好；APS按actions/navigationtime不等每tokenlatency。采用段未披露hardware/precision/完整trainingcost/SLO，不采headline十倍或真实内部reasoning解释。仅报告局部mode supervision与部署分支，不改一般VLA控制安全或目标真值判断。

### [DARC: Decoupled Asymmetric Reasoning Curriculum for LLM Evolution](https://arxiv.org/abs/2601.13761v1)

§3.2/4.1见[原段](../_sources/daily-20260122/standard4.txt)，§4.3/Table2见[反侧](../_sources/daily-20260122/decisive21_batch1.txt)，均实际读、准入独立通过。冻结Questioner造offline difficultycurriculum；teacher读document取N次majority伪标签且agreement gate，student不读document但共享parameters，伪标签不等groundtruth。discrepant instances的Avg@8短/中documentteacher胜率>50%，>5K39.2/48.7低于question-only，支持特权上下文有条件而非永远更好teacher；noise只是作者解释，不认唯一原因。Qwen3-4B/8B、OctoThinker8B，mathGPT4o judge与generalgreedy exactmatch不合并；部分baselines引用原论文，SPICE同prompts/corpus复跑；尚未采用全trainingbudget/hardware/precision/runtime数字。仅报告局部teacher条件反证，不改变一般证据provenance或pseudo-label校准原则。

### ["The Whole Is Greater Than the Sum of Its Parts": A Compatibility-Aware Multi-Teacher CoT Distillation Framework](https://arxiv.org/abs/2601.13992v1)

§3.2 [proxy](../_sources/daily-20260122/readysetup4.txt)、§3.3/4.5 [反侧](../_sources/daily-20260122/decisive21_batch1.txt)、§3.4/4.1 [配置](../_sources/daily-20260122/standard4.txt)已读、准入独立通过。goldanswer条件likelihood positivejumps按固定thinkingword mask加权，EOS经student QK图centrality、teacher-rationale NLL组合softmax weights；答案span KL不是新增核心。去MI后低entropyteacher更占重且OOD退步只是局部对照，不识别真正逻辑迁移或gradient冲突。Eq11声称autograd等效sum α∇L，但α依student而未显式detach说明，不能补造省storage的数学等效。Qwen2.5-1.5/7B与Llama3.1-8B、alllinearLoRA、8/6epochs、perdevicebatch4、2A10080GB；teacher原Qwen2.5-70B标法仅原文身份，不自动更正为72B。precision/总teacher生成与proxyforward成本未采用。仅报告此gold-dependent权重分支，不改一般distillation真实性/成本验收。

### [ARC: Active and Reflection-driven Context Management for Long-Horizon Information Seeking Agents](https://arxiv.org/abs/2601.12030v1)

§3.2/4.1见[原段](../_sources/daily-20260122/standard4.txt)，§4.3/Table2与§4.5/Table4定点实际读、准入独立通过。常规incrementalsummary只吸收新turn，raw最新interaction保留给actor下turn；reflection允许非局部改memory/checklist，不直接改actorpolicy或执行外部action。Qwen2.5-32B同actor消融，jointrepair优于summary/checklist-only；固定Actor/ContextManager/tools/contextbudget/interactionlimits下everyturn31.2、every3/5turn26.5/24.5、budget8/16/32K27.1/24.4/24.6。manager GPT-OSS120B付额外调用，fixedcontextbudget非总compute匹配；faithfulsummary是目标非事实保证。Hotpot随机512、GAIA textonly、BrowseComp subsets等population不合并；hardware/precision/完整预算未采用。仅报告这个何时修哪类state的局部干预，不授always-on免费或普优。

### [AgenTRIM: Tool Risk Mitigation for Agentic AI](https://arxiv.org/abs/2601.12449v1)

§3.2 Eq5–7与§4.5/Fig8定点已读，§4.2/6 [评价与反侧](../_sources/daily-20260122/standard4.txt)已核，准入独立通过。highrisk-only proposals暴露所提工具，mixed投影lowrisk，highriskjudge仅见executionstatus不读actorreasoning；nostatus/novalidation增加ASR，nostatus还伤utility支持该信息接口条件，不证明monotone风险函数实证成立。AgentDojo97benign/629injected四suite，主要图important-instructions，其他defense从各原论文取值并非统一重跑；环境修改=highrisk、read-only=lowrisk是可变分类，不等任何readtool安全。latency约1.8/1.85×两处原口径、cost2×；setup/hardware/全部攻击预算未采用，judge/status误判与分类漂移均留。仅报告受限runtime validation分支，非部署保证；成熟authority/leastprivilege原则不因新封装自动缺Books。

### [OFA-MAS: One-for-All Multi-Agent System Topology Design based on Mixture-of-Experts Graph Generative Models](https://arxiv.org/abs/2601.12996v1)

§3.2/3.3/4.3 [机制/反侧](../_sources/daily-20260122/decisive21a.txt)，§3.4/4.1 [训练](../_sources/daily-20260122/standard3.txt)已读、root原源准入通过。taskvector逐layer gate message、expertheads逐步生成role/incomingedges；先零task学classicgraphs，再LLM伪query/topology，再classicconfigs实际执行选high-performing graphs；pseudo systemdesigner不是optimalgraph真值，执行标签只在所试配置。单unifiedmodel跨6bench而oneforone按domain，GAIA未见训练且GPT4omini禁toolcall，OFA8.79/Chain7.38/GDesigner5.50只支持这个受限OOD人口。core ablation删除MoE/TASE/两stage/gate均退但未控参数/总compute，heatmap不证明角色因果。采用段hardware/precision/全search/train成本未披露，不授通用transfer。仅报告conditional-topology分支，不改一般delegation/authority判断。

### [Listen, Look, Drive: Coupling Audio Instructions for User-aware VLA-based Autonomous Driving](https://arxiv.org/abs/2601.12142v1)

§3.1/4.5 [生成机制](../_sources/daily-20260122/decisive21b.txt)，§4.1/4.3 [评价](../_sources/daily-20260122/standard3.txt)实际读、root必要原源准入通过。future ego trajectory参与intent/Goal/CurrentAction文本→TTS；tempo/pitch算arousal又重参数化同path目标speed，输入含target-derived information。换audioencoder的mini-set ablation不隔离这个shortcut，未有独立真实voice/同等provenance输入控制；不能认全部提升由泄漏唯一造成，但可否定现openloop比较证明真实情绪驾驶泛化。nuScenes1000scenes、openloop waypointL2/overlapcollision，3B Echo对7B Qwen2-VL是模型与输入同时改变，collision不是closedloop安全率。hardware/precision/SLO未采用。仅报告受限输入/标签责任反证，不把领域应用重新纳入通用VLA安全机制。

### [ReWorld: Multi-Dimensional Reward Modeling for Embodied World Models](https://arxiv.org/abs/2601.12428v1)

§3.3/4.3 [核心/反侧](../_sources/daily-20260122/decisive21b.txt)，§3.2/4.1 [reward与配置](../_sources/daily-20260122/standard3.txt)实际读、root必要原源准入通过。ratio=exp(oldCFMloss−newCFMloss)，C(c)取消依模型间同常数假设，负相关直觉非真实likelihood证明；wrong-sign collapse37.8vs61.9不证明unbiased PPO。N1/N5/N10得分56.9/61.9/60.8无显著性/全成本不称5普遍最优。HERO4heads在InternVideo2-1B不同层，dimensionalmask+weightedBT/totalBT监督；totalBT不能单独保证各head绝对scale校准或消除共享backbone干扰。235K GPT4o-derived RH20T pairs、Cosmos2B BridgeV2 SFT、4layer3DCNN critic、8A100/AdamW，precision/完整预算未采用；ReWorldBench自建judge不等真实physics。仅报告可计算lossproxy分支，不授O(d)整套成本或物理闭环保证。

### [Tolerance Principle and Small Language Model Learning](https://arxiv.org/abs/2601.12179v1)

[exact-v1 PDF](https://arxiv.org/pdf/2601.12179v1) pp3–11实际读，HTML404仅此版本PDF恢复；root准入及有限理论假设核通过。8layer/8head、hidden256/intermediate1024、MLM、batch16/Adam1e-4/mask.15；10K randomwords训练5K/test5K，tokenizer见全vocab+train，不能称heldout词完全未见。人工ABC/BAC规则例外与二元16char规则，type/exception/4或10epochs控制，1000pairedsurprisal与分段回归；threshold jump不显著不是proof zeroeffect，binary每设置3initializations。重复exposure影响learnability，type-only N/lnN不能直接作为该小模型学习阈值；不否定人类TP。图截图接口失败不补造点值，不扩查missing图点。仅报告局部理论条件反证，未确认Books使用TP阈值，不因人类类比主题强写。

### [Preserving Fairness and Safety in Quantized LLMs Through Critical Weight Protection](https://arxiv.org/abs/2601.12033v1)

精确v1 §3/4/5.1见[方法与评价](../_sources/daily-20260122/safety12033_core.txt)，§5.2/SNIP/Limitations见[仅有效尾段](../_sources/daily-20260122/safety12033_incomplete.txt)，实际读；后者聚合截断不授其缺失前段已读。FAIRSCORE/SAFESCORE是fair/safety squared-loss-gradient Fisher diagonal重要性减βgeneral的重要性，保护topweights原precision；这是dataset proxy差额，不是普遍安全的权重身份。Gemma7B/Llama3.1-8B/Qwen2.5-7B instruct，GPTQ/AWQ4bitW、SmoothQuant8bitW/A与FP8/LLM.int8；保护实验仅AWQ、60% FP16、β1及每dataset128样本。保留比例改变本身改变memory budget，不能称同完整资源预算免费保护。

StereoSet/MBBQ多语言、SafetyBench MCQ、DoNotAnswer Longformer与MultiJail GeminiFlashLite三个init等协议不合并；invalid responses人口使平均值不能直接跨family解释。Qwen部分fairness量化反改善、非英语保护不单调，DoNotAnswer ASR同k时SNIP可优于作者保护（k.6 3.798 vs4.260）；Qwen AlpacaEval AWQ76.52、保护75.03，不能称全质量无损。hardware/batch/concurrency/全校准与forward成本、SLO未披露或未采用；无adaptive jailbreak/复杂部署验证。深入只核受影响安全主张，仅报告局部mixed-precision选点及风险切片，不把已有量化校准/独立安全验收原则因缺该配方强写Books。

### [System-Mediated Attention Imbalances Make Vision-Language Models Say Yes](https://arxiv.org/abs/2601.12430v1)

精确v1 §3.2/4.1/4.3/5及限制见[必要原段](../_sources/daily-20260122/counter12430.txt)，实际读。zero selected pre-softmax modality attention后把其质量按原比例分配给剩余modality，system→text是区别仅加视觉注意的干预接口。仅LLaVA1.5-7B的第25–32层、single-token yes/no与六paired tasks；simpleaccuracy、pairedaccuracy和yesrate分开。Hallusion system→text acc58.04优于45.64 baseline、image51.52，yesrate39.12相对gold42.17；但MME baseline78.98降到text61.25/image66.39，POPE popular/random accuracy也小降，yesrate接近50不保证正确率。

coarse/fine default representations是作者解释，干预attention与观察输出不识别唯一内部语义原因；未测多backbone/长生成/perhead及部分干预曲线。hardware/precision/batch/完整成本与SLO未披露或未采用。深入核的是视觉不足单因解释与通用mitigation收益，仅报告这个受限反证；不采用普遍hallucination防御或所有模态竞争因果保证，也不为该局部诊断改长期Books。

### [A Two-Stage GPU Kernel Tuner Combining Semantic Refactoring and Search-Based Optimization](https://arxiv.org/abs/2601.12698v1)

精确v1 §3.2/3.4/4/5.1/5.2见[必要原段](../_sources/daily-20260122/kernel12698.txt)，实际读。semantic rewrite成带granularity/unroll/vector/sharedmemory/register参数的模板，再resource-feasible autotune；finite groundtruth tests与容差是局部correctness filter，不是全输入语义证明。DeepSeek-chatV3.2相同agent框架、TitanRTX，三个SGLang CUDA kernels（silu_and_mul/fused_add_rmsnorm/merge_attn_states_lse），每配置20warmup/100runsmean；从代表Llama7/13/70形状组选generalconfig，后评同组不是heldout-shape泛化。

相对原SGLang三个speedup3.55/1.09/2.03对agent-only2.89/1.06/1.95，局部模板搜索差额成立；未匹配全LLM调用、autotuning/search预算，kernel2/3接近plateau。tolerance数值、端到端模型质量、fullruntime成本、并发/SLO未披露或未采用，不采用跨HIP/OpenCL生产扩展承诺。仅报告模板化搜索局部分支，现有编译/测试/资源约束原则不因没有该kernel recipe而成为长期缺口。此报告采用v1，不把后来v2提交时间自动算本窗公开修订。

### [Left-Right Symmetry Breaking in CLIP-style Vision-Language Models Trained on Synthetic Spatial-Relation Data](https://arxiv.org/abs/2601.12809v1)

精确v1 §2.1/2.2/3/5见[必要原段](../_sources/daily-20260122/standard_ready3.txt)，实际读。10px 1D、object整数编码、learned position/token embedding、CLIP contrastive训练，控制seen object labels与layout；unseen pairs并非object完全未识别。label diversity更影响泛化而layout变化小是本toy人口结果。机制分析简化移除LayerNorm/MLP，EP交叉项形成左右梯度；inference zero EP使unseen-pair discrimination近.5，VP另有反侧，不把仅attention图等同因果。

原Figure5caption把relational与label-specific同写一个不等式，采用正文明确的label差额小于position差额及方向条件，不静默修复caption。一般模型2blocks×2repeat、4heads、128dim，Adam-style设置lr1e-4/decay.2、10Kepochs、batch50/100随左右caption改变；hardware/precision/fullcost未披露或未采用。仅报告受控关系表示的具体交互与干预，不从toy、简化模型或理论扩展声称真实CLIP/RoPE普遍机制；有局部机制不等该解释在长期owner需新增一篇配方。

### [PASs-MoE: Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learning](https://arxiv.org/abs/2601.13020v1)

精确v1 §4.2见[RW原段](../_sources/daily-20260122/pas13020_rw.txt)，§4.3/5.1/5.3.1及Limitations见[必要原段](../_sources/daily-20260122/standard_ready3.txt)，实际读。route softmax energy=||Ah||²/r，history importance=E[πe(Ah)k²]并累积，normalized/clipped weights约束各A-row相对前task偏移。activation proxy与expert参数共同变化，不是独立groundtruth capability；B与router本身未被此rankpenalty完全固定。fullsoftmax激活所有experts与Topk不同工作量，Table2把Topk仅作参考，不用其较差质量为同计算归因。

softmax同MoE参数budget43.36AP→RW46.31→RS48.46、BWT−6.64→−4.24→−2.15；MathQA full49.52低于RW49.99，forget−5.90差于−5.18，不能称每task更好或无遗忘。LLaVA1.5-7B/CLIP-L14-336、alllinear LoRA rank128、6experts、λ5e-4、3epochs/task、batch12、NVIDIAH20、seed42；fixed taskstream不replay，非online漂移通用校准。历史statistics与λ调参有实际storage/tuning代价，precision/完整runtime成本/SLO未披露或未采用；“不加参数”不等零开销。仅报告lowrank energy耦合的局部训练分支，不能因新router recipe就改长期owner，未采任意PEFT/扩容/replay泛化。

### [Simulated Annealing Enhances Theory-of-Mind Reasoning in Autoregressive Language Models](https://arxiv.org/abs/2601.12269v1)

精确v1 Methods/Experiments见[实际原段](../_sources/daily-20260122/standard_ready3.txt)，[公式争议](../_sources/daily-20260122/annealing12269_dispute.md)已由root定点独立确认。Eq4区分whole-sequence power与逐token sharpening的future partition factor；新增局部接口是τ.90→.25 schedule、16blocks/10MCMCsteps/maxnew512。Eq6在x=current/x′=proposal定义下印了标准MH接受比倒数，不是抽取错误；不替作者纠公式、不猜代码，也不采用exact-power-sampler保证。原文自身明确annealing非fixed-target posterior draws，中心数学保证争议终态隔离，恢复勘误/精确实现与目标证据后只重开该命题。

Phi3.5Mini3.8B/Llama3.2-3B/Qwen3-1.7B、BigToM200templates/400backward TB/FB instances，greedy direct/CoT对fixed power/anneal额外MCMC预算不等成本。Phi/Llama fixed策略提升TB却伤FB，Qwen部分accuracy改善的例子仍worldstate/belief混淆；qualitative sample不证明通用latentmental-state机制。hardware/precision/runtime/全cost未披露或未采用。仅报告有限schedule观察，未解决中心claim不支撑正面分布保证或Books；已读支持与关键反侧足够，不扩完整proof/代码考古。

### [FlipFlop: A Static Analysis-based Energy Optimization Framework for GPU Kernels](https://arxiv.org/abs/2601.13345v1)

精确v1 §3.2/5/6/9见[必要原段](../_sources/daily-20260122/energy13345.txt)，实际读。PTX controlflow/instruction/coalescing features结合每architecture microbench calibration的MWP/CWP、power/time模型，以inputresource过滤config，再推荐energy/runtime候选；静态预测不等没有任何runtime执行。RTX5000Ada24GB/RTX3070 8GB、Ubuntu20.04/CUDA12.4、NVML/CUPTI/Nsight；MHA seq128–8192、batch4/16heads/dim256、原设5或10trials随实验，功率cap与validconfig口径有66/528/785/800不同段，不能合并为统一search人口。

§5 top20捕获94%是有限排序召回非exactPareto，runtime rankρ.66弱于energyρ.857；aspectratio消融ρ.852→.142支持该局部feature。real-time power deviation>10W又修coalescing/latency，使误差改善依动态反馈。§6 14.3min/188680J为避免的profiling估计，172986×/15.1×/392×不同口径及150runs摊销不能当真实端到端LLM收益；未核全calibration amortization、模型quality/output长度/concurrency/SLO，不采工业projection/碳通用数字。原Pareto pseudocode运行时不等式不足以授正确最优集合。仅报告硬件校准配置预测分支，不因PTX命名或零执行宣传造长期差额。

### [ContiguousKV: Accelerating LLM Prefill with Granularity-Aligned KV Cache Management](https://arxiv.org/abs/2601.13631v1)

精确v1 §4.2/4.3/5.1/5.3见[机制/设置](../_sources/daily-20260122/contiguous13631.txt)，§5.2见[收益反侧](../_sources/daily-20260122/contiguous13631_eval.txt)，实际读。c16 tokenchunk统一prune/store/prefetch，p8layers复用indices、subperiod4；intra按前layer已知集合pipeline，inter用前period集合预取再加载差额。相邻period overlap仅52–64%，存在无用prefetch与后续miss，“zero read amplification”只对应所选chunk的逻辑字节，不保证所有物理I/O/transfer零浪费。原文7B单token28KB推导以hidden维与heads表述，未作为独立校验后的内存公式采用。

Qwen2.5-7/14/32B、A80080GB、host128GB、Samsung990Pro4TB读7.45GB/s、PCIe4×16双向32GB/s；所有systems限GPU10GB/CPU24GB、baseline chunks64、seed42。四fewshot分类短输出侧重re-prefill，warm GPU/CPUcache；baselines重实现且disable部分scheduler优化，不等原系统原生产SLO。5%预算相对IMPRESS3.85×平均TTFT同时相对fullKV质量均值低5.62%，50%低.04%，不能headline高质量等同lossless。I/O token加载约16.33×减少非全请求字节cost；precision/正式concurrency/output长度分布/全serving SLO未披露或未采用。仅报告局部granularity与prefetch实现，不更改一般paging/I/O责任链或授全服务低延迟。

### [HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference](https://arxiv.org/abs/2601.13684v1)

精确v1 §4.2/4.3/5.1/5.3/5.4/Limitations见[必要原段](../_sources/daily-20260122/cache13684.txt)，实际读。head inverse稳定度分budget，full volatile/pivot留GPU、anchor静态压缩、satellite全context放CPU；pivot的topindex overlap中位数窗口低于drift阈值触发satellite更新与baseline重置。代表head监测是proxy，不保证所有satellite的重要token一致；预算/阈值与model人口绑定，异步不等所有带宽下完全hide I/O。

Llama3.1-8B/Qwen2.5-14B/DeepSeekR1Distill8B、单A100/Intel6326；R1 weights4bit bitsandbytes，其他精度未披露或未采用；memoryρ.3/.5与threshold Llama.5/Qwen.4。LongBenchLlama49.42低full49.77、Code60.77低62.01，LongBenchV2部分超baseline不授普遍质量无损；去allocation/retrieval退步只支持局部干预。latency为TTFT+50generatedtoken平均ITL，224K约3×而OmniKV>40×依I/O baseline，非并发tailSLO；PyTorch原型无custom sparse/retrieval CUDA，PCIe带宽会限制隐藏开销。完整RAM/monitor/profiling与transfer成本未采用。仅报告head-drift资源分支，不授无停顿/代表头全覆盖或新普遍压缩安全。

### [Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs](https://arxiv.org/abs/2601.13707v1)

精确v1 §3.2/3.3/4.1/5.1/5.4见[必要原段](../_sources/daily-20260122/guidance13707.txt)，实际读。共享QKV对最后textquery屏蔽visualkeys产生maskedpath，再将cond−maskedpath相对masked output做orthogonal correction。早layer与textKV已含visual信息、softmax重分配是明确approximation bias；投影不证明提取纯视觉语义。加Gaussian noise的correlation也不验证masked与真正image-absent输出等价。matchedF1的ortho/无ortho两组保留不同γ，支持有限质量取舍：77.6/77.4F1时CHAIRi7.6/9.7。

LLaVA1.5/MiniGPT4/QwenVL、greedy、同benchmark maxlen，官方支持baseline才测，γ2.4/.3/1.4不同模型。POPE Qwen adversarial83.53低regular84.07/VCD84.23，LLaVA recall从88.87降79.87，不能称全指标优。CHAIR max128，Full1.19×/Fast首8layers1.05×vanilla是此原环境，singlepass不等零新增attention成本；hardware/precision/batch/concurrency/SLO未披露或未采用。仅报告masked approximation+orthogonal分支与局部成本，未改一般视觉provenance、生成正确性或无hallucination保证。

### [Lost in the Prompt Order: Revealing the Limitations of Causal Attention in Language Models](https://arxiv.org/abs/2601.14152v1)

精确v1 §2/3.3/4见[原段](../_sources/daily-20260122/causal14152.txt)，§3.1/3.2/AppB见[控制与协议](../_sources/daily-20260122/causal14152_counter.txt)，实际读。QOC option表示按causalmask确实不见后context，但最终answerquery可见所有context/options；这是具体信息路径限制，不是context对整个模型绝对不可访问。CQO剪option→context使69.26→42.46，QOC用CQO中后layer optionactivation patch54.54→60.49、重复options后置→62.76，支持此读出格式下路径干预；patch移植另一template完整状态并非只改变单一position属性，repeat有额外tokens，不授唯一因果或免费guard。

21模型.5–9B、四MCQA testsets，A/B/C/D likelihood约束读出而非一般自由QA；A6000/BF16/single greedyrun/max16。base-instruct ninepairs/5shot仍gap不能完全排除pretrain分布，encoder/decoder异架构不等同训练控制；所谓rule out bias收窄为这些有限对照未解决gap。context attribution非groundtruth causal比例，跨dataset长度对比还有人口混杂。深入只核options信息路径与评价反证，仅报告受限MCQA格式/读出设计，不授任何scale/QA固有失效或所有后置context忽略。

### [CTPD: Cross Tokenizer Preference Distillation](https://arxiv.org/abs/2601.11865v1)

精确v1 §3.2/3.4/4.1/4.3见[必要原段](../_sources/daily-20260122/distill11865.txt)，§3.3/4.2/Table1–3见[目标与反侧](../_sources/daily-20260122/distill11865_counter.txt)，实际读。共同原字符串characterstart/end定义span，按各tokenizer teacherforcing的logprob和聚合，teacher DPO/reverseDPO contrastiveweight+teacherSFT reference进入student偏好loss。同字符覆盖身份不保证两模型语义/概率自动等价，也不排除offset/normalization工程问题。independent bounded rewards/constant expectation idealD假设没有实证建立；practical logσ内塞估算权重原文称heuristic，不采用noise-free/unbiased finalobjective保证，缺extended proofs不影响这个局部接口报告。

Qwen2.5-7B→Llama3.2-1B、14B→3.1-8B，UltraFeedback63K、每stage1epoch/8H10080GB/globalbatch16/seed0；teacher正负训练与precomputedweights增加总成本，precision/fullbudget未披露或未采用。六capabilitybench+lm-eval standarderror非trainingseed方差，不等直接humanpreference alignment真值。8B mean67.42vsTIS66.16但MMLU66.65低66.73、HellaSwag82.25低DPO82.42；1B ARC40.61低TIS40.92、MMLU31.08低SFT31.73。teacher reference Table3优student65.27、originweight优局部替代只是此control。仅报告span对齐/reference分支，不授普遍whitebox偏好无损或改长期distillation保证。

### [Incentivizing In-depth Reasoning over Long Contexts with Process Advantage Shaping](https://arxiv.org/abs/2601.12465v1)

精确v1 §3.3/4/5.2/Limitations见[必要原段](../_sources/daily-20260122/longpas12465.txt)，实际读。GT chain加入prompt让当前policy生成reference，再judge validity×embedding similarity只衰减failedrollout对应step的负groupadvantage，positive保持；不是给失败局部正reward。同policy权重但privileged GT prompt改变条件，不等普通rollout分布相同，judge/embedding与KG链仍是proxy。thinkingtokens另统一用response平均advantage，不授所有token准确归因。去validity/去relevance/换Gemini教师有局部退步，但LongBench子项有反向差额、教师复杂度/条件分布同时改变，不认唯一原因。

2012filteredQA（Qwen3-4B-Thinking8rollout成功率.25–.75筛）/Wikipedia、max60Kinput/10K或30Koutput、同dataset GRPO、group8/T.7/top-p.95、lr2e-6；truth-guidedT0、GPT-OSS120B judge与Qwen3-8BEmbedding增加成本。FRAMES/LongBenchV2/MultiHop人口不合并，fullhardware/precision/trainbudget/runtime未披露或未采用。GT路径依赖限制通用数据、开放答案judge不能作真实correctness保证。仅报告具体负advantage衰减和reference条件，不为新credit recipe强写长期Books。

### [Linear Mechanisms for Spatiotemporal Reasoning in Vision Language Models](https://arxiv.org/abs/2601.12626v1)

精确v1 §2.2/3/7/AppA.2见[必要原段](../_sources/daily-20260122/spatial12626.txt)，实际读。同object token activations跨位置减均值，再跨objects平均得ID；4×4grid/90pairs×4size共86400syntheticimages，去lexicalmean不数学保证只剩geometry。以ID差向量干预residual，α5经gridsearch、近似保norm；100COCO spatial binaryquery输出left/right logprob改变，11models定向beliefswap中位64.6%对same-norm noise29.5%。原“43.6%increase”未直接当两中位数差额采用。swap定义只是相反答案相对likelihood翻转，不是实际世界位置变化或唯一模型belief真值。

≤14B、简单空间/appearance temporalquery范围，不把“ubiquitous”外推所有尺度或复杂推理；干预用objectword与位置相关语义向量可能有其他readout效应，same-norm noise非全部替代解释控制。hardware/precision/batch/所有extraction和finetune成本未披露或未采用；本次不采未审时域/改进全部headline。仅报告这个可复查提取/干预接口及范围，不自动改长期表示owner或宣称完整视觉reasoning已线性解释。

### [Distribution-Centric Policy Optimization Dominates Exploration-Exploitation Trade-off](https://arxiv.org/abs/2601.12730v1)

精确v1 §3.2见[控制与目标](../_sources/daily-20260122/dcpo12730_core.txt)，§3.3/4.2/AppB/5.2见[设置反侧](../_sources/daily-20260122/dcpo12730.txt)，实际读。J1–4改变samplingpolicy与token target/current ratio，DCPO用current采样、behavior/update clippedratio及温度target regularizer ratio两个角色；四grid实验只支持局部entropy控制与梯度估计接口。Theorem3.1显式假定token-level IS unbiased，不能据当前prefix tokenratio授完整trajectory分布unbiased，REINFORCE/smallα也非全更新无偏。作者自己承认virtualtarget近似variance累积可长期不稳；PP tradeoff概念不作已证最优定律。

Qwen2.5-7B/Math7B/Qwen3-4B、DAPO17K、8A80040GB、max8192/group8/batch512/minibatch128/lr1e-6、Ttrain1，AEPO另60/30samples非同采样总预算；precision/全cost未披露或未采用。Avg@32与Pass@128不同，不互换；H0.25 mean55.77、1.00降52.43，AIME25局部.75更高，不采无条件entropy越大越好/近最优探索。α按batchaccuracyrate除法的零rate实现未披露，不补造。仅报告具体双IS估计与moderateentropy反侧，不改长期on/offpolicy保证。

### [Towards Robust Process Reward Modeling via Noise-aware Learning](https://arxiv.org/abs/2601.12748v1)

精确v1 §3.3/4/5.1/5.2/Limitations见[原段](../_sources/daily-20260122/prm12748.txt)，AppA见[配置](../_sources/daily-20260122/prm12748_setup.txt)，实际读。MC label衡量prefix后samplingpolicy最终成功，不等当前step intrinsic correctness；未来selfcorrection产生falsepositive、后续失败产生falsenegative。LLM检测future显式改当前step后先把该trajectory视作此step不成功再聚合K8；NAIT对与旧label相差δ大的step用自己continuousconfidence替换并重训。reflectionjudge有误判、modeldisagreement不自动是labelnoise；低noise前提是经验假设，不授真值或self-label防偏保证。深入核是value与correctness混用评价反证。

MC128Ktrajectories约1Msteps、QwenMath7BInstruct sampling，Qwen2.5-7B judge、Math1.5/7BPRM、4L20/4A800、max4096/batch1024/1epoch每stage；MATH500“training split”按原文标，不自动补来源身份。humanPRM800Ktest用于labelAcc/F1，ProcessBench与Bestof8选answer指标分开。Table3 NAITmean75.9仅近Majority75.8且低QwenMathPRM76.1，不以不同training samples/scoreraggregation认同总预算普优；仅testtimescaling未验证RL。precision/δ完整实现与全rollout/judge/retraincost未采用或未披露。仅报告具体policy-dependent label反证与局部纠偏接口，不因新PRMrecipe强写Books。

### [Think3D: Thinking with Space for Spatial Reasoning](https://arxiv.org/abs/2601.13029v1)

精确v1 §3.4/4.1/5.2/5.4见[原段](../_sources/daily-20260122/think13029.txt)，§3.2/5.1/5.3/5.5见[控制反侧](../_sources/daily-20260122/think13029_counter.txt)，实际读。Pi3估计pointcloud/pose再virtualcamera围绕inputcamera anchor旋转，global/ego projection产新视图；合成视图不是真实3D observation或geometry真值。训练离散canonicalviews、inference可连续pose，GRPOterminal correctness+formatreward与observation-tokenmask，不能授新stepcredit。GPT4.1 raw3D BLINK42.31/MindCube55.43低原42.80/55.83，加anchor/selection/ego逐步改善是实际新适用条件，不把tool名当贡献。

977MindCube train、120test无重合、VSI tiny每video7frames、8H200/1epoch/batch8/accum4/max1024/lr1e-6，visionencoder frozen、Pi3推理RTX3090；precision/重建+渲染+extraimage完整预算/runtime未披露或未采用。RL前50steps少turn同时accuracy退，后toolturn变多有收益不是同调用预算因果；强模型视角分布相似不证明humanlike空间reasoning或唯一学习机制。仅报告anchor与view控制的局部工具接口，不授3D系统真值、普泛或同预算最优。

### [Confidence over Time: Confidence Calibration with Temporal Logic for Large Language Model Reasoning](https://arxiv.org/abs/2601.13387v1)

精确v1 §2.3/4.1见[定义与mining](../_sources/daily-20260122/confidence13387_core.txt)，§5/6/8见[方法与反侧](../_sources/daily-20260122/confidence13387.txt)，实际读。stepconfidence是segment内生成tokenprob arithmeticmean，segmentation需每task一致但方法未固定；minedSTL固定formula结构，hypernetwork由question与confidence统计预测temporalbounds/threshold/sigmoidαβ再按标签训练。STL robustscore是proxy pattern，不是逻辑证明response正确，α正值约束未明示，不采用无条件orderingpreservation保证。

Qwen3-8B/Gemma3-12B/Llama3-8B、四structured tasks、heldout+5fold mean/std非多训练seed；mining与adaptive成本不可由single生成一次忽略。QwenMath adaptiveECE.109差于fixed.082与InternalInspector.064；GemmaSciQ Brier.245远差selfeval.059，cross-task A2也非全部指标胜A1，不采“allbaselines更差”叙述。in-domain优transfer与10templates优2/16只支持这组结构/参数条件。0.55s平均未绑定hardware/precision/batch/输出长度完整成本，未采用生产runtime；无openended证明。仅报告task-specific confidence接口，不把数学STL命名当truth或一般校准Book缺口。

### [Beyond Memorization: Testing LLM Reasoning on Unseen Theory of Computation Tasks](https://arxiv.org/abs/2601.13392v1)

精确v1 §2.2/3/4/5/7及AppA.9实际读：[机制反侧](../_sources/daily-20260122/dfa13392.txt)、[控制](../_sources/daily-20260122/dfa13392_control.txt)、[seen](../_sources/daily-20260122/dfa13392_seen.txt)。50知识题100%只支持该题集；90公开seen不证明训练见过，180 unseen（60手工/120Arden）难度未配对，不把准确率下降唯一归因记忆。相同API prompt/T0、CoT1-shot/ToT4分支；三层hint从反例到精确错误仍未可靠解决hard组合一致性。validator枚举≤6和2000随机7–15字符串、双人结构核验不是全语言等价证明。T0非provider确定性保证，fixed JSON重试次数Not Disclosed，timeout非能力失败。仅报告该组合/hint反证，不授所有LLM无法推理或强制formal-verification recipe。

### [Reasoning is a Modality](https://arxiv.org/abs/2601.13562v1)

精确v1 §4.2/4.3/5.1–5.4实际读：[原段](../_sources/daily-20260122/controller13562.txt)、[对照](../_sources/daily-20260122/controller13562_counter.txt)。demo E(y)−E(x)经MLP入controller，workspace3×3structured pass，但同block另有dense pass，global interaction非仅controller。共享recurrent stack/EMA不等零work。ARC400/REARC每题1000，newtask全参数TTT、510views多数投票pass@2；TTT1 100epochs vs TTT2 300/lr三分之一，作者samecompute未由步数建立，TTT3另加heads/loss。18M ViT54.5/8.3 vs 28M d1TTT1 56.6/6.9非每split更好，best4trial/83M ensemble也非单机制同预算；hardware/precision/完整TTT compute Not Disclosed。仅报告角色分离局部分支，不采reasoning新modality、人类超越或内部state可解释保证。

### [Activation-Space Anchored Access Control for Multi-Class Permission Reasoning in Large Language Models](https://arxiv.org/abs/2601.13630v1)

精确v1 §2.2/4.2/4.3/5.1/5.5/6与§5.3/5.6实际读：[机制](../_sources/daily-20260122/access13630.txt)、[评价](../_sources/daily-20260122/access13630_eval.txt)。heldout separability/silhouette选ASI，permission centroid bank/weightedL2risk按authorized95%/validationF1阈值allow/refuse/中间steer；不是scope隔离证明。威胁模型假定认证安全、固定低权限无限queries，但实验单轮prompt不证明adaptive无限安全。MultiPER11K/5部门proprietary，Qwen14B judge、三模型，非externalACL基线/humantruth；PVR.005–.009/AASR.084–.101仍非零，overlap/labelnoise/multiturn开放。端到端8.60→9.83/7.54→9.44/9.11→10.05秒，非免费；hardware/precision/长度batch/SLO Not Disclosed，不采constanttime。仅报告受限表示干预，不增普遍访问控制保证或强制Books配方。

### [Dimension-First Evaluation of Speech-to-Speech Models with Structured Acoustic Cues](https://arxiv.org/abs/2601.13742v1)

精确v1 §3.2/3.3/4.1/4.2/5及A7实际读：[原段](../_sources/daily-20260122/audio13742.txt)。Whisper/DNSMOS/prosody/affect→typedJSON，LLM分C/VQ/P后dataset-specific deterministic融合；HCoT先absolute acceptability再relative winner，bothgood/bothbad可区分。人工N468/314 κ.651/.796与另一过滤N494不合并，内容/单维翻转只支持局部接口。S2S58%bothbad，TRACE badwinner48.6低Audio70.7/LLM73.5，但winner-slice73.5低86.7/84.1；GPT4o Speak content58.0低LLM58.8。total GPU+API估算Audio$12.532/TRACE$4.158/LLM$2.763，较audio便宜非最便宜；不采用未展开Table13或普遍价格。English/人工schema/upstreamerror、非实时多轮；hardware/precision/输出长度/runtime Not Disclosed。仅报告typedcue评价及预算局部分支，不由新schema名称改长期评价原则。

### [Chain-of-Thought Compression Should Not Be Blind: V-Skip for Efficient Multimodal Reasoning via Dual-Path Anchoring](https://arxiv.org/abs/2601.13879v1)

精确v1 §3.3–3.5/4.1/4.4/Limitations见[机制反侧](../_sources/daily-20260122/anchor13879.txt)，A2/4.2见[配置](../_sources/daily-20260122/anchor13879_setup.txt)，实际读。token NLL与中间25–75%layers maxhead imageattention做union-of-saliency；attention是proxy，原variational mutualinformation解释未实证保证真实grounding。两percentile分别取再union使实际ActRatio不同target，固定γ不等相同保留token数量；Table5 union48.2 vs intersection30.1同时改变保留预算，不授独立因果优越。offline prune后LoRA蒸馏免online attention计算不等零训练/全部runtime成本。
Qwen2VL2/7/72B/Llama11B、官方validation MMMU/DocVQA、8RTX3090、LoRA16/32所有attention projections、3epochs/batch16/lr2e-4；precision/训练样本完整规模/推理长度batchconcurrency Not Disclosed。MMMU原称下降5.9/2B8.5/72B3.2仍非无损，DocVQA1.8×和2.71s vs LLMLingua2.93s未授全部配置SLO，训练成本不能忽略。仅报告视觉anchor保护与蒸馏受限分支，不以缺配方强写Books。

### [The Side Effects of Being Smart: Safety Risks in MLLMs' Multi-Image Reasoning](https://arxiv.org/abs/2601.14127v1)

精确v1 §4.1/5.1/5.3/5.4/Limitations见[原段](../_sources/daily-20260122/mir14127.txt)，A4见[实现](../_sources/daily-20260122/mir_intervention_setup.txt)，实际读。DeepSeekR1 rewrite/evaluator、FLUX、Qwen7B tester、HarmBench classifier迭代最多5轮，仅有成功危害的实例进入2676cases/9relations/6riskcategories；这是attack-conditioned population，不等自然事件率。safe输出再由R1分CR/HM/IR/CE，harmless misunderstanding不是已证安全对齐；judge“客观”不当humantruth，4专家仅抽查。
546至少一种rewrite成功seed、五highest-ASR模型单图/多图matched generation比较，GPT4o19.4→65.2等局部差额支持新风险，不排除额外image/content/token数量和成功relation选择，不授关系结构唯一因果；attentionentropy仅四模型相关。19models单轮/default safety、A80080GB与API；single-image模型拼接50pixel间隙非原生multiimage等价。precision/output length/全部构造预算 Not Disclosed，没有mitigation实证。仅报告正确拒绝与能力不足分离及这组风险，不授普安全/所有推理更聪明更危险；限定诊断不强制长期Books改动。

### [InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning](https://arxiv.org/abs/2601.14209v1)

精确v1 §3.1见[机制](../_sources/daily-20260122/mir_intervention_setup.txt)，§4.1/5.1/5.2/5.5/7见[控制/评价](../_sources/daily-20260122/intervention14209.txt)，实际读。同model对自身轨迹与reference作diff、定位firstincorrect再提单step，包含finalanswer的intervention丢弃；self-generated不等无特权监督，judge/errorlocation也非真值。clone prefix+intervention、不clone continuation、至少32rollouts之一成功的filter；235题coverage202/235、noprefix162、含suffix111，accuracy仍7.71%，supports局部SFT选择不证明第一错误必是唯一因果。offpolicy NLL/entropy相关不是因果理论。
Qwen3-4BInstruct2507/约4500hardpool→1076成功筛题，GRPO400steps各baseline相同不等reference/生成/筛选总预算同。128rollouts估计IMO/HMMT pass1与AMO/Apex pass8不能互换；selfreflection AMO36.72高InT36.16，mean含trainreward不当统一test metric。PRM没比较，不授比PRM可扩更省。hardware/precision/batch/完整SFT+rollout+RL成本 Not Disclosed或未采用。仅报告reference-assisted训练接口，未来autonomous/continual credit非本次实证，不为具体配方强写Books。

### [Jet-RL: Enabling On-Policy FP8 Reinforcement Learning with Unified Training and Rollout Precision Flow](https://arxiv.org/abs/2601.14243v1)

精确v1 §3.3/4/5实际读，见[原段](../_sources/daily-20260122/jet14243.txt)。trainforward与rollout的precision/granularity graph对齐，master BF16/存FP8activations、跨operator gradients BF16，FProp/WGrad/DGrad FP8 GEMM；weights128×128、activations/gradients1×128，backward某方向重新quantize。不是只把所有张量改FP8，统一graph不证明kernel/reduction/sampler完全logit相等或消除全部offpolicy原因。长4K→8K/16K及base任务困难控制暴露mismatch风险，但能力难度机制仍作者hypothesis。
Llama8/Qwen2.5-7/Qwen3-8Base、GSM+MATH group4/DeepMATH group16、H100、batch256/lr1e-6/KL1e-3、每5steps eval；Jet相对BF16仍Qwen8K−1/16K−3、Qwen3Base16K−2.7，非质量等效。rollout512prompts/input512/concurrency128/4–16Koutput/TP1–4速度1.07–1.33×非全E2E；8B8K step1.16×，14–32B全training未做，GPU总数/总成本/SLO Not Disclosed。不自动修Table2Qwen93.1−92.9却印+1.0或文中9.8与表10.2冲突，采用原score不采用矛盾delta。深入限precision-flow设计反证，仅报告局部实现，不授普遍unbiased或生产保证。

### [Rethinking the Value of Multi-Agent Workflow: A Strong Single Agent Baseline](https://arxiv.org/abs/2601.12307v1)

精确v1 §3.2/3.3/4.1/4.2.1/2/4实际读，见[原段](../_sources/daily-20260122/oneflow12307.txt)。固定homogeneous base+routing/tools的singleagent保留所有previoushistory、role delimiter，systemprompt被当user追加；改变可访上下文及权限语义，不采用任意工作流概率等价或compaction无损定理。MCTS20round designer/critic另有优化成本，singleagent执行与workflowsearch不合并。
GPT4omini T0/Claude4Sonnet designer、三runs按任务原metric；闭源API KV成本由finalhistory模拟理想reuse而非provider实际账单，输入/输出tokens均计不代表缓存实际实现。Qwen3-8B vLLM16K HumanEval actual OneFlow single latency4.83>stateless4.31、throughput1.70<2.47，pass87.4>87.0，AFlow亦增历史；不能称singleagent总更快。hardware/precision/完整搜索与execution budget/output lengths Not Disclosed。深入核homogeneous基线设计反证，仅报告受限状态/成本接口，不证明多智能体无价值或普遍KV安全共享。

### [Can Deep Research Agents Find and Organize? Evaluating the Synthesis Gap with Expert Taxonomies](https://arxiv.org/abs/2601.12369v1)

精确v1 §3/4/Limitations实际读，见[原段](../_sources/daily-20260122/taxonomy12369.txt)。DeepResearch只给topic，BottomUp给expert同exactpapers；LeafRecall与ARI/VMeasure、Hierarchy TED/embeddingSoftF1/GPT4ojudge分开，不能合指标。samepapers最高ARI.31而SoftF1高；ClaudeAB→+summary ARI.27→.24同时SoftF1.86→.88、judge2.53→2.59，具体说明语义plausibility≠expert分类一致性。expert树非唯一正确taxonomy，extraLLMsummary也有新增generation预算/噪声；跨mode非同agentcontrolled唯一检索因果，7agents Recall结构Spearman.83只相关。
12frontiermodels/7agents、1000taxonomy qualitative error，κ.8909支持原人群judge一致性不普真值；各providerdeepresearch配置、hardware/precision/长度/调用/完整预算 Not Disclosed或未采用，不采所有核心文献遗漏比例或MECE普保证。仅报告同input隔离与评价指标分歧的局部诊断，不为benchmark名称或评估recipe强写Books。

### [Gated Differentiable Working Memory for Long-Context Language Modeling](https://arxiv.org/abs/2601.12906v1)

精确v1 §4.2–4.4/5.1/5.3/5.5/Limitations实际读，见[原段](../_sources/daily-20260122/memory12906.txt)。absolute full/local logprob差同时捕获context帮助/冲突，是模型CPMIproxy非truth或gradient贡献精确值。每chunk先kmin、剩余softmax/largest-remainder，K<Mkmin时仅topchunks且其余0，不能称总有globalcoverage；chunk内positions随机minibatch LoRA更新，KVprecompute非所有计算免费。
Qwen3-1.7/4/8B LoRA16/32 Q/O、AdamW1e-4、H20/BF16、32Kmax、chunk1024/local512/K8或32；固定steps对uniform有局部差额，8B QMSum8step8.2低qTTT8.5/Quality32step94.8低94.9。utility每chunk两个forward，4B原CPMI.36s/13%、减少32→8梯度步才净39%wallclock，非4×E2E。Table4 worst25.8>avg21.7等未给清楚聚合，原“最差≥25唯一robust”不采用；跨chunk完整证据span未实证普阈值。仅报告该utility/coverage局部配方与densecoverage反侧，不强制长期TTT/记忆owner改动。

### [The Bitter Lesson of Diffusion Language Models for Agentic Workflows: A Comprehensive Reality Check](https://arxiv.org/abs/2601.12979v1)

精确v1 §3/4.1–4.3/6.1–6.3/Limitations实际读，见[原段](../_sources/daily-20260122/diffagent12979.txt)。AlfWorld134/ScienceWorld90/BabyAI112与BFCLv3最多50/category共758，success/progress与ASTformat分开；ScienceWorld是agent环境评价，不扩AIforScience研究。AR Qwen8 nonthinking/Ministral8、四dLLM均单A80080GB但AR vLLM/diff FastAPI/Fast-dLLM，不同训练与serving不能归因为diffusionfactorization唯一原因；retryloop原3或>3定义不一致不采精确统计。
memory多为comparable而BabyAI可负；earlyexit取4个最佳trajectory是条件子集，保守退出少progress损失不证globaltrajectoryawareness。selector/editor 50instances生成200testcases，DVar selector帮助Qwen伤Ministral，模块作用依主policy，不授dLLM全面不可用。双model用两GPU，效率与成功权衡非同budget；precision/生成长度/全部执行成本未披露或未采用。本研究无task-specificRL/native co-design，深入核局部设计反证，仅报告现model/population/固定workflow角色边界，不改变通用Diffusion生成保证。

### [Probe and Skip: Self-Predictive Token Skipping for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2601.13155v1)

精确v1 §3.2–3.4/4.1–4.3实际读，见[原段](../_sources/daily-20260122/probe13155.txt)。MHA当前layer allK/lastQ attention proxy选active，FFN由calibration channel裁剪+SVD估transformnorm乘attention；乘积TopK不数学等同“两个条件都低才跳”，attention/FFNnorm非真实taskimportance或全序列loss证明。stage内跳过token仍可后layer参与，stage末删除不可任意复活；fixedbudget不普适绝对重要token恒定。
LongBench17、Llama8/Qwen7 A80080/openPangu1B Ascend910B2、200Qasperseq校准、ρ.2/r128或256；hardware之外precision/batch/concurrency/SLO Not Disclosed。平均47.62/47.48/30.62均低full47.98/47.76/31.09，非无损；FFN同50%skip proxy Avg45.89优attention45.29但Qasper差额仅.07。32K20seqwarmup TTFT2.46×/E2E2.29×仅生成16token，非一般长输出serving；calibration/SVD成本不省略。仅报告当前layer自proxy与延迟删除分支，不以少recipe改长期token-state/paging原则。

### [Which Reasoning Trajectories Teach Students to Reason Better? A Simple Metric of Informative Alignment](https://arxiv.org/abs/2601.14249v1)

精确v1 §3.4/4.1/5.1/5.2/Limitations与AppC.1见[原段](../_sources/daily-20260122/teacher14249.txt)，§2.1/A5见[设置](../_sources/daily-20260122/selection_op_setup.txt)，实际读。raw tokenrank/surprisal均值会被近零surprisal主导，改为surprisal-weighted总rank/总surprisal、rankclip100；低RSR是empirical studentfit，不是information/alignment真值或理论保证。5K题×11teacher×3candidate同33-to-1池选择支持局部干预，teacherselect只200samples/6teachers且避开consistentlygoodteacher，限制外推。RSR top1 Llama26.7低oracle28.1、Qwen3B31.2低33.0，非全最准。
5base students、AIME/AMC/MATH Acc@4，teacher3独立generation后各SFT非额外seed；selection3seeds，SFT8–10epochs/batch64/max32768/gridsearch，H200、14B8H200约6h。5K RSR scoring单H200约1h，单forward非零成本、需完整studentlogits；precision/outputlength/全teachergeneration+调参成本未披露或未采用。Table4绝对Spearman .86不是普遍方向/因果结论。仅报告固定pool/student-conditioned选择分支，不凭新ratio强写长期distillation/数据owner。

### [From Completion to Editing: Unlocking Context-Aware Code Infilling via Search-and-Replace Instruction Tuning](https://arxiv.org/abs/2601.13384v1)

精确v1 §3/4及AppH实际读，见[核心与对照](../_sources/daily-20260122/sri13384.txt)、[条件似然](../_sources/daily-20260122/sri13384_ppl.txt)。SRI先复制既有区域marker与10行再输出replacement；CrossCodeEvalFlex允许修复加5行noise，FIM接近零EM部分来自原context冻结的任务定义，不是模型全面失能。同prefix/suffix的NL-FIM/chat对照与同20K数据重排控制支持目标接口差异；GPT4.1 CrossCodeEval EM46.1→45.8、GPT4omini Long11.1<12.1、o1 Long24.4<26.6，非所有配置更好。QwenBase1000例PPL SRI3.89低三NL格式4.98/5.42/6.15，只是指定模型条件格式似然，不能证明pretraining真实模态或修复正确性。
安全SAL比较Base-FIM与Instruct-SRI有alignment混杂，Qwen/DeepSeek仍非零ASR，额外safeprompt不是SRI本身的防御因果；不采统一安全提升。QwenBase32B、20K SRI+60K Glaive+100safety，原文称80K而总和80100，不替作者消去差异；16A100/BF16/853steps/batch256/32K，greedy256输出、2A100 evaluation，部分相似度8K/执行完整context协议不同。在线IDE/延迟/完整数据生成与训练成本 Not Disclosed或未采用。
深入受影响安全信号及目标定义反侧；仅报告局部editing objective与同数据格式对照，不把额外配方未写入书当长期owner缺口。

### [OP-Bench: Benchmarking Over-Personalization for Memory-Augmented Personalized Conversational Agents](https://arxiv.org/abs/2601.13722v1)

精确v1 §3/4/5及AppA2实际读，见[机制/评价](../_sources/daily-20260122/op13722.txt)、[配置/过滤提示](../_sources/daily-20260122/selection_op_setup.txt)。英文合成单轮中irrelevance为完全无关，bait为语义相关却不应个性化，sycophancy分事实/虚构memory/价值；repetition用1−embeddingcos proxy，不等于人类厌烦真值。每dataset样例两annotator共识/争议裁决支持构造，不代表全部模型回答人工真值。六模型/六memory system的OP-Bench和LoCoMo分测；不采用未重核完整Table2的平均drop或全面失效headline。
SelfReCheck按prompt从context选原文片段或NO RELEVANT CONTEXT，与正文逐item f(q,m)并不严格等同二值实现；额外LLM过滤成本未匹配。length-normalized memory/query attention较高只是相关，不证明因果。8A100、T0/greedy、输出512/top5memory；precision/全部调用成本 Not Disclosed，provider/API取决baseline，不授Pareto改进。
仅报告不必要memory的具体评价切片与局部读取过滤干预；人工构造范围、模型judge与额外调用边界不能升级为通用个性化策略保证，不强制改长期memory原则。

### [Towards robust long-context understanding of large language model via active recap learning](https://arxiv.org/abs/2601.13734v1)

精确v1 方法/实验/消融实际读，见[原段](../_sources/daily-20260122/recap13734.txt)。LSG使用long/short tokenprob ratio选TopK，再找插入后提升targetlikelihood的source segment，生成5–6句summary并re-tag；continued pretraining与inference定期recap是不同作用。Algorithm1循环alltext起点而prose称earliersegments，未核实现不能补造严格past-only边界，更不能授漏泄安全保证。
Qwen1.5-1.8B/RWKV7-1.5B、ProLong>10K、4A80080/BF16、1epoch/batch8/lr1e-5；RULER8/16/32K及有限QA观察，Qwen8K CWE45.3<58.2/FWE28.6<31/Hotpot27.8<31.8、RWKV8K Hotpot15.6<20，非全任务改进。Table4叙述把66.5→72.9叫32K，而表中该值在8K、32K24.1→26.8，不采用错误长度headline。更多chunk改善单个NIAH指标同时增加recap预算，非免费长期记忆。
mining/rephrasing/完整inference增算、concurrency/SLO Not Disclosed或未采用；仅报告loss代理选源与显式回顾的受限分支，不从平均分推无损long-context或真实状态。

### [Multimodal Generative Engine Optimization: Rank Manipulation for Vision-Language Model Rankers](https://arxiv.org/abs/2601.12263v1)

精确v1 §3/4及限制实际读，见[原段](../_sources/daily-20260122/mgeo12263.txt)。白盒Qwen2.5VL7B surrogate，控制一个商品的text与image、固定其余候选，联合目标交替优化；10category、每类10–15商品、每次10candidate。排序位置变化非top1 ASR。joint mean−2.25相对text−.73/image−1.30显示有限耦合观察，jointhas两模态步骤、没有同计算预算，不能把差额归因唯一交互效应；商业gpt4omini/gptimage1mini heuristic不是同gradient/attackbudget基线。
原“random promotion−4.5”来自推到first位置的总变化，非随机重排对照，不采用。单商品10→1例产生明显artifact，违背隐蔽性要求；静态候选/单模型、未测黑盒迁移或防御。hardware、precision、完整iteration/模态预算 Not Disclosed，不采普遍低成本攻击或实际部署成功。
深入安全影响仅限威胁入口/核心对照/直接反侧；仅报告指定ranker的联合输入控制风险，不把攻击存在等同所有VLM unsafe，也不以名称新增安全owner配方。

### [LR-DWM: Efficient Watermarking for Diffusion Language Models](https://arxiv.org/abs/2601.12376v1)

精确v1 方法/检测/实验与限制实际读，见[原段](../_sources/daily-20260122/watermark12376.txt)。已知left/right分别hash不同key并addgreen bias，缺邻居emptygreen、boundary单侧；检测以mL+mR−1累积，用human C4 10K、长度400的经验variance与1%阈值标定。共享邻居相关，经验标定非独立Bernoulli证明；boundary/nullmean适用性不能补成无条件E0精确式。
LLaDA8B greedy/block25、DREAM7B stochastic、300token/300step，WaterBench600prompt后过滤degeneration，是条件population；H100、Qwen32 PPL evaluator，precision/总输出过滤成本 Not Disclosed。matchedTPR99/99.5时PPL3.32/3.37略高DMARK3.28/3.34并有SEM overlap，非总更优。moderate10%delete/substitute观察与clean100%operatingpoint绑定，不同于固定90/99质量点；paraphrase大幅下降、非自适应操作不证明抵抗了解key/检测器的攻击。运行时/显存数字未采用，不授所有生成路径免费。
仅报告非顺序邻居更新与经验检测接口，在局部算法分支外不改变长期认证/安全保证，不为水印名称强写Books。

### [Proxy Robustness in Vision Language Models is Effortlessly Transferable](https://arxiv.org/abs/2601.12865v1)

精确v1 核心训练/主评价/直接反侧实际读，见[原段](../_sources/daily-20260122/proxy12865.txt)。target adversarialexample经frozen异构CLIP proxy，直接KL(targetadv→proxyadv) HPT clean平均下降2.87；先低LR targetadv→proxyclean warmup+EMA，再高LR HPT并与warmEMA混合β.5/γ.9。代理选择与攻击条件是核心，不是任意proxy鲁棒或生成VLM全面迁移。
TinyImageNet10epochs/SGD64、RTX3090、ViTB32target/B16proxy、LR5e-5与5e-2；trainPGD2/evalPGD10 1/255，15下游分类含PCAM仅作通用表示评价，不扩科学应用pipeline。称AutoAttack但实际APGDCE/DLR两变体、非完整suite；adaptive同时求proxy/targetgradient只是有限攻击，4/8/255平均17.76/5.73仍低，局部列亦退化，clean Tiny57.61<65.36。不同proxy gap/ResNet选择可伤clean，普通classification失败；contrastive预训练解释是推测非实证因果。
precision/完整GA+HPT增算 Not Disclosed，未核完整理论不采用其普保证；深入受影响迁移安全主张，仅报告有限classification攻击与clean tradeoff，不采“effortlessly”或任意foundationmodel鲁棒结论。

### [Beyond Tokens: Concept-Level Training Objectives for LLMs](https://arxiv.org/abs/2601.11791v1)

精确v1 目标/数据/评价与限制实际读，见[原段](../_sources/daily-20260122/concept11791.txt)。Llama3-8 nounconcept由WordNet或LlamaInstruct给synonym/hypernym；cake→pie/cookie等非严格语义等价，contextfree与LLM误标已承认。NCP是conceptset成员logprob平均/累积，非“任意一成员”概率质量的log，multi-token/公式索引含糊不替作者修复。sameunderlying/samecount repeatedNTP与dataaug NTP对照支持局部objective分支，不直接证明latentconcept真实性。
Apr18后YouTube/arXiv/NYT 8K/1K/1Ksplit、四domainposttraining后七classificationfinetune；不是generativereasoningtrust评估。Table中NSPcontextfree CombinedLOG.1716<baseline.4925、NSPaware CombinedGLUE.3365<.7395，原“consistently”不能采用，多variant最佳不是一固定方案全胜。教师概念生成及训练额外成本、硬件/precision Not Disclosed（A5仅机构GPU资源非本实验配置）。
仅报告operational概念监督目标和局部数据/目标控制，不因新增损失名称改长期表示/训练原则，也不把分类收益外推模型理解。

### [A Unified Masked Jigsaw Puzzle Framework for Vision and Language Models](https://arxiv.org/abs/2601.12051v1)

精确v1 机制、攻击设置、视觉/文本结果及限制实际读，见[原段](../_sources/daily-20260122/jigsaw12051.txt)。打乱selected token且PE替sharedunknown，未选保留原position；training augmentation与runtime attack shuffle分开。梯度攻击APRIL解析/重实现optimization分别比较normal、shuffleoriginaltruth/shuffletruth，不能把对错排列的MSE直接混作privacy。ImageNet ViT300epoch/batch1024/lr.001AdamW；Yelp/Amazon180–400word/window32，BERT与4layer/d96Transformer，训练epoch4/8、lr5e-5/5e-3、batch16。
TableIX vision MSE.0482>.0446/LPIPS.6544>.6159但SSIM.3726>.3355、PSNR13.71<14.25方向混合，不采“全部指标更好”。text100Yelp TableX γ.9与叙述.03条件冲突；TAG从5K→30K迭代有恢复增量，非预算增加绝无收益。重构metric低不等于无信息泄漏、DP或完整隐私；PCA二维分离亦非语义隐私证明。
keypoint精确对齐/AR生成失败是作者边界；hardware/precision、完整攻击运行时与训练成本 Not Disclosed。深入position梯度泄露命题和直接反侧；仅报告该排列/PE干预及有限重构接口，不授私密训练系统普保证，不强制owner新recipe。

### [Powerful Training-Free Membership Inference Against Autoregressive Language Models](https://arxiv.org/abs/2601.12104v1)

精确v1 §3/4与失败/参考消融实际读，见[原段](../_sources/daily-20260122/membership12104.txt)。需候选groundtruth token、target tokenlogprob和pretrainedreference；errorposition由target预测错误定义，↑/↓probdelta比是方向失衡/尺度不变proxy，非所有记忆真值。主三dataset各10Kmember/10Knonmember+500validation/128tokenconcat；GPT2 full3epoch、GPTJ6B/Llama7B LoRA16/32，H200，两forward不等于所有API能取logits或无额外query。
WikiLlama AUC.771低SPV.780，TPR@低FPR与AUC分开；XSumGPT2XL1K+1K/unrestrictedlength/10%FPR的FP短94/FN长430分析不是128token主人口，相关不能证明全部privacy机制。samearchreference.895 vsDistil.789/random.591/self.5，unrelated.864；distilledreference需4epoch10K生成，不计作默认training-free零成本。zeroerror/N0仅0/1000例，不证20K或部署永不发生，建议∞/member的特殊处置可能FP不采用。
precision/完整reference与query成本未披露或未采用，fullvsLoRA/modelscale有混杂，pretrainingwebscale仍开放。深入隐私测量与关键反侧；仅报告具体errorposition/reference依赖的诊断，不从此攻击授所有AR模型membership可证、泄露完备性或防御保证。

### [AgenticRed: Optimizing Agentic Systems for Automated Red-teaming](https://arxiv.org/abs/2601.13518v1)

原拟成熟evolutionary recipe关闭在最终110题摘核账时重开，依据新增最小核心而非改变配额。精确v1 §4.2–4.4/5.1/5.3/5.7/A1/B2及C1实际读，见[原段与设置](../_sources/daily-20260122/red13518_min.txt)，root同位置独立核后准入5、深入安全影响及LimitedOnly通过。去高质量initial archive但保留同helperfunctions/tools，meta agent第二代已重发现proposer/verifier仍难恢复强starting-example效果，是指定ICL search下的warm-start反侧；不能称所有自动设计必须人工archive。10generation去selection bestscore低6%但没有全部搜索调用等budget控制，新增组件存在不授效率归因。
权限限blackbox targetresponse与judgefeedback、helper含judge logprob，T0不保证所有runtime确定性；固定target非安全团队patching co-evolution。GPT5-2025-08-07meta、local Mistral8x7Battacker/Llama2-7Btarget/HarmBench13Bcls judge，半数据train/半test；每generation3系统、16初测/50最终trainpairs，best heldout评价3seeds，StrongREJECT亦是judge非所有humantruth。ASR优化使Llama2多样性下降而Llama3未见相同tradeoff，rewardshaping仅marginal收益、thresholdrejection引入超参，不授普遍quality-diversity规律。
A1/B2 training queries/success122K、test339，test对照6/33/20/48/40不同algorithm条件，不采所有query效率更好。hardware/precision/完整token与调试成本 Not Disclosed或未采用；modecollapse仍多已有template/operators，非原创安全机制证明。仅报告有限same-tools initialization与target-dependent searchobjective反侧，不进入Books或全攻击实现审阅。原v1标题与DataCite当前v3标题不同，final-ID不变，[注册原值](../_sources/daily-20260122/date_red13518.txt)仅公开上界，registered13:28:27BJT用后1秒作半开范围终点，非正文精确时刻。

## 5. 缺口与下一步

普通可执行工作：无。

冻结67项作者必要证据/Books处置、非作者逐项限定复核，以及来源停止范围、公开日期、最终分母、排除分层和六部分日级Gate均已通过。原遗漏校准13606关闭/13518准入已落实；本日无普通审阅/Books写入待办。以下仅本窗终态保留项，不用于正面证据/Books/无遗漏或安全性能保证；未来材料到达只定点重开受影响项。

外部保留项：OpenAI/Qwen/Hunyuan本窗原生历史目录缺段及其他表内所限定事件类型不支持候选、Books、全源零命中或无遗漏；取得本窗官方列表/可核历史API后仅重开受影响源和材料，不无界动态重试。arXiv直接本日列表缺段以有限主题入口和逐项公开上界限定，不能据此授全分类Coverage。

中心主张保留项：[12269 Eq6](../_sources/daily-20260122/annealing12269_dispute.md)接受比反向印刷，exact-power-sampler保证不采用、不Books，不授已核正确目标分布；对应精确版本勘误/实现及目标分布证据到达时定点重开。不因此重新读取无关proof。

日期未决：[2601.14327](https://arxiv.org/abs/2601.14327v1) final-ID registered 2026-01-22T02:39:40Z只提供窗外上界，不能据此推正文精确时间或确定落窗；官方当天公告可恢复时再定归属。本次不作确定候选、不采用。withdrawn [2601.13358](https://arxiv.org/abs/2601.13358)当前页明确撤回（v2Mar30，理论框架错误），只留原始记录，不评分、不Books，不当作访问缺口。

## 6. 复核

复核者：root（非作者）

结论：通过

root已实际完整题摘核67准入及代表分层关闭，必要原源核Nixie/RAPID/TDA/Re-SpS/R²PO、DoubleCal/PPA/PICL/PREGU/PASC-GRPO/PVF/S2DiT/FantasyVLN及其余实际采用核心；当前§4全部67项已逐项非作者限定证据/处置通过（47标准、19深入及12269争议隔离；65仅报告、1具体已有覆盖、1实际整合POST）。12269通过的是采用边界和争议隔离，不是exact-sampling结论。关闭项包含撤回、design反证与安全信号：ToolPRMBench、MAR/多视图、CARPE、TIVSO/Detox/TB2、weather攻击等已按受影响最小核心独立核；无关/成熟recipe按来源/主题/理由分层校准，未审整个arXiv月目录或所有附件。早期原材料待root标记均为过程快照，不再驱动执行。

排除分层实际已记录独立关闭复核31/41：11816/12277/13238/14188/14251/11776/11868/12522/11854/12762/13186/13247/13352/13622/13719/14230/12294/12323/13243/13304/13606/12343/12618/12842/13836/13383/11913/14112/13705/11903/12304，包含完整AB准入关闭和受影响最小原核心，不称全附件审阅。其余10作者完整AB关闭、未独立抽检：13809/14207/14032/14051/14063/14157/12286/12538/13115/13132；抽检已覆盖应用/成熟workflow/综述/attribution/安全攻击等来源、主题和理由层，不能把31抽检及最小原核心叫41全量验证。撤回13358与日期14327单独隔离不算41贡献关闭；未检查全部题目明确范围外的发现条目、完整月目录、其他年月/Weekly或无关附件。root已实际顺读当前六部分、110题摘/201命中层次、67冻结、31/41与未核10、14每日来源/实际trigger停止边界、逐项完整包络及14327/撤回/12269隔离；日级语义Gate通过并授权作者标记完成。完成表示安全终态，不把隔离缺口叫Coverage/Evidence通过。实际Books修改Ch23两段+末注1项，root顺读正文403–417与末注1153 POST通过、窄锁释放；11969的Ch66具体覆盖也已独立核。最终67项V3格式/一致性校验实际通过，130个本地引用路径已核存在，git diff --check本日限定范围通过；报告未跟踪，另实际查报告尾随空白为0；未stage、commit、push。
