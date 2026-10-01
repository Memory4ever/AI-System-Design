# Daily Research — 2026-04-09

**规范：** V3
**窗口：** 2026-04-08T09:00:00+08:00 ～ 2026-04-09T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-26T18:06:00+08:00

## 1. 结论

本日按当前合同重建；旧18项分母、DOI-created owner proxy和Complete不继承，原文完整保留于[旧证据存档](../_sources/daily-20260409/V2_1_REPORT_ARCHIVE.md)。562个库存身份只用于标题范围定位，189个完整题摘已实际读，不是562篇有效贡献或全文队列。87个初始工作信号及四项反向恢复已逐家族收口到候选、具体前分母关闭或日期/版本隔离，**最终候选清单81项**。完成指普通工作闭合；外部目录、日期、版本及争议保留项不支持正面证据或零遗漏断言。

81项已完成必要证据判断：24项真实Books增量已写后独立通过，10项已有覆盖，39项仅报告，8项中心理论或实验争议安全隔离。87初始信号的差集已逐项给具体关闭或日期/版本隔离（见§5）；另06491/07108/06281/06812是独立复核恢复的四家族。新增Book知识包括optimizer状态动态精度、因果masked-block生成、remote adapter serving、推理早停探针的对象、验证式早停的净能耗、语义随机策略的采样状态、数据选择的step-boundary混杂、训练辅助target/部署截断边界，以及跨adapter近似复用、跨进程Graph恢复、成对调度策略的独立身份、SFT早期回退的条件性轨迹与接收方通信停止控制；06832补入role/modality/turn共同限制生成可见性的机制。最终否定侧抽核恢复AGSC：其自适应粒度值得审阅，但聚合公式抵消与clustering消融冲突，不据此写Books。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [News RSS](https://openai.com/news/rss.xml)1230项至2015年，本窗CyberAgent/enterprise-phase/child-safety三条原文及blueprint必要PDF已读；三者为未受控采用、策略或既有安全原则，具体贡献关闭 | 受阻 | Research/Index历史分页仍缺；RSS不替代全部研究目录，隔离后只定点重开 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)publishedOn列表04-07T09:35Z→04-09T16:34Z跨窗 | 已检查 | 只限官方可见目录，不宣称全公司所有入口无遗漏 |
| SRC-GOOGLE-AI | [April Blog](https://research.google/blog/2026/04/)与academic-agents正文已读；PaperViz/PaperBanana2601.23265和ScholarPeer2601.22638为旧家族无独立增量；DeepMind selected pubs264项04-22→03-22 | 受阻 | Google Research Publications历史日期停点未恢复，不用Blog/selected pubs替代全部覆盖 |
| SRC-META-AI | [Blog](https://ai.meta.com/blog/)04-08 MuseSpark/Build-Test→04-06/03-26，两篇正文已读 | 受阻 | 仅日历日不能证明落窗；Research空解析/Publications历史接口HTTP500，相关日期家族精确隔离 |
| SRC-QWEN | research.research-list静态60+article/retrieval动态40，04-02→04-15；组织新仓58项读完无落窗，Qwen3/Qwen3.6重要release列表空 | 已检查 | 只检查公开目录与相关artifact，不全扫commit |
| SRC-DEEPSEEK | [官网](https://www.deepseek.com/)Research02-25→06-24、news12-01→04-24；View-all范围沿相邻04/08已核未变入口复用，组织/重要release补检无本窗 | 已检查 | 复用具体未变目录，不称本日重扫历年全部论文 |
| SRC-MOONSHOT | [Blog](https://platform.kimi.com/blog)26项到2025-11-07；组织43项新仓无落窗；kimi-cli100个release到2025-10，04-02v1.30→04-10v1.31 | 受阻 | 官网2026历史研究目录未恢复，不由GitHub零release推研究零命中 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)publicList pageNum1/pageSize100/renderType0返回9/9，displayPublishTime Feb13→Apr23；组织83项/T1release补检无落窗 | 已检查 | 只限官方全部列表，不使用updatedAt代发布日期 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)04-07→04-29、New Released04-07→06-16；组织53项/GLM5release补检无本窗 | 已检查 | 官网目录不代未列作者论文 |
| SRC-BYTEDANCE-SEED | get_article_list_v2，x-tt-locale:US，type1 page20/40/60为20/18/19项，04-09→04-08→04-07→03-31；type2 page0/20为15/18项，04-08T16Z→03-31T16Z；Seeduplex正文/project已读，未披露独立机制 | 已检查 | CMS毫秒字段不直接作为首发；07026有早发线索定点隔离，科学任务排除 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)两页02-06→04-15；ERNIE唯一release2025-06-30，公开新仓补检无落窗 | 已检查 | 不扩扫任意历史commit |
| SRC-XIAOMI-MIMO | [官网](https://mimo.xiaomi.com/)Paper8项03-13→06-29；Blog14项无可靠日戳；组织18项及MiMo release补检无本窗 | 受阻 | 必要历史Blog日期/停点仍未恢复，保留精确目录缺口 |
| SRC-MINIMAX | EN Blog12项05-26→03-18，CN13项03-18→04-27；AgentTech入口/llms.txt唯一文章与未变相邻日techblog.md05-13停点复用；组织35項/重要release无落窗 | 受阻 | 原Agent Team单页不带可靠发布时间，不能称历史TechBlog全集可核 |
| SRC-ARXIV | [官方公告规则](https://info.arxiv.org/help/availability.html)、相邻批次/OAI及永久ID分配；562库存标题定位、189完整题摘；保留家族v1可用上界逐项核 | 已检查 | 工作信号不等冻结候选；版本/日期例外单项隔离，不把Submitted/DOI/Updated孤证叫首发 |

实际停止点、原始字段与题摘位置见[当日续跑记录](../_sources/daily-20260409/V3_REVIEW_CHECKPOINT.md)及[贡献筛选记录](../_sources/daily-20260409/V3_SCREENING_NOTES.md)，不以本表断言互联网无遗漏。

## 3. 候选与判断

下表为日级复核后81个唯一家族，不是81项普遍成立的贡献。公开范围由永久ID公告分配、相邻批次/OAI、官方Wednesday20:00EDT→本窗08:00以及该家族v1可用上界共同支持有界推断；Updated不是首发时刻。跨截点/版本污染/可能更早首发项不列确定候选。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Robustness Risk of Conversational Retrieval: Identifying and Mitigating Noise Sensitivity in Qwen3-Embedding Model](https://arxiv.org/html/2604.06176v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 模板噪声与query dialect使clean retrieval收益失效；1+2+2=5 | 标准完成 | 已有覆盖：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)query/index/packing与outcome联合验收 |
| [LLM Spirals of Delusion: A Benchmarking Audit Study of AI Chatbot Interfaces](https://arxiv.org/html/2604.06188v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 同名chat/API与时间窗口不是相同评估对象；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)access path及时间身份 |
| [Probabilistic Language Tries: A Unified Framework for Compression, Decision Policies, and Execution Reuse](https://arxiv.org/html/2604.06228v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | stationary prior cache的阈值理论分支及证明反例；2+2+2=6 | 争议 | 暂缓：Lemma2下界反例，需勘误/有效证明 |
| [The Art of Building Verifiers for Computer Use Agents](https://arxiv.org/html/2604.06240v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | task-only rubric、conditional分母与cascade归因；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)task-only rubric、适用分母与cascade归因 |
| [ZitPit: Consumer-Side Admission Control for Agentic Software Intake](https://arxiv.org/html/2604.06241v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 不可信artifact首次执行前的capability admission；1+2+2=5 | 深入完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)artifact provenance/sandbox/egress门槛 |
| [RAGEN-2: Reasoning Collapse in Agentic RL](https://arxiv.org/html/2604.06268v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 输入依赖的互信息与仅输出随机性分离；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)关键诊断指标与filtered objective |
| [FedSpy-LLM: Towards Scalable and Generalizable Data Reconstruction Attacks from Gradients on LLMs](https://arxiv.org/pdf/2604.06297v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 低秩梯度重建的接口与几何保证存在反例；2+2+2=6 | 争议 | 暂缓：Theorem2列空间桥不成立，不采用理论安全结论 |
| [Discrete Flow Matching Policy Optimization](https://arxiv.org/html/2604.06491v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | rate→一步policy→内层MDP，避免终态marginal估计；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)一步transition policy的reward接口 |
| [The Detection-Extraction Gap: Models Know the Answer Before They Can Say It](https://arxiv.org/pdf/2604.06613v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 自由延续可恢复性与forced readout不是同一对象；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)推理早停的探针对象、gold及总成本 |
| [STQuant: Spatio-Temporal Adaptive Framework for Optimizer Quantization in Large Multimodal Model Training](https://arxiv.org/html/2604.06836v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | optimizer state精度按layer/state/time调度；2+2+2=6 | 深入完成 | 整合：TRAIN-ZERO [Ch39](../../../../books/part-04-training-system/39-zero.md)分片与低比特状态压缩 |
| [MARS: Enabling Autoregressive Models Multi-Token Generation](https://arxiv.org/pdf/2604.07023v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | AR checkpoint因果masked-block继续训练及连续commit；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)因果masked-block分支 |
| [Information as Structural Alignment: A Dynamical Theory of Continual Learning](https://arxiv.org/html/2604.07108v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 冻结表示上的局部correction粒子读写/矛盾decay；1+2+2=5 | 标准完成 | 仅报告：局部prediction correction有新算法，但现有实验未支持采为Agent memory设计 |
| [InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models](https://arxiv.org/pdf/2604.07173v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | base/KV与remote adapter状态分离及activation往返；2+2+2=6 | 深入完成 | 整合：INFER-DYNAMO [Ch52](../../../../books/part-05-inference-system/52-dynamo.md)adapter独立远程执行 |
| [Generalization error bounds for two-layer neural networks with Lipschitz loss function](https://arxiv.org/html/2604.06281v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | SGM norm条件下独立test与依赖样本不同泛化rate；2+1+2=5 | 标准完成 | 仅报告：两层SGM特定数学条件，不外推现代Transformer泛化保证 |
| [SALLIE: Safeguarding Against Latent Language & Image Exploits](https://arxiv.org/html/2604.06247v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 跨模态hidden-state guard的观察位置和阈值身份；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)白盒probe身份/校准与外部授权分离 |
| [Say Something Else: Rethinking Contextual Privacy as Information Sufficiency](https://arxiv.org/html/2604.06409v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 属性替换、对话一致性与隐私风险的非等价关系；2+2+2=6 | 深入完成 | 仅报告：受控模拟的虚假属性策略，不能采为默认隐私设计 |
| [When to Call an Apple Red: Humans Follow Introspective Rules, VLMs Don't](https://arxiv.org/html/2604.06422v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 声明阈值、独立感知估计与实际决定分账；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)声明规则/估计/decision三对象 |
| [Babbling Suppression: Making LLMs Greener One Token at a Time](https://arxiv.org/html/2604.06755v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | stop-validation减少token却可能增加device能耗；2+2+2=6 | 深入完成 | 整合：PLATFORM-COST [Ch70](../../../../books/part-06-ai-infrastructure/70-cost.md)早停验证的净成本break-even |
| [The Illusion of Stochasticity in LLMs](https://arxiv.org/html/2604.06543v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | token随机性不等语义action law，历史校正会引入相关；2+2+2=6 | 深入完成 | 整合：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md)独立SamplerState与分布提议分离 |
| [Feedback Adaptation for Retrieval-Augmented Generation](https://arxiv.org/html/2604.06647v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | feedback-ready lag和相关query修正质量分离；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)反馈两轴评价与snapshot边界 |
| [Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision](https://arxiv.org/html/2604.06723v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 局部embedding regime与token score聚合改变校准；1+2+2=5 | 标准完成 | 仅报告：代码proxy和新分布校准标签条件，不采为通用release gate |
| [Improving Semantic Uncertainty Quantification in Language Model Question-Answering via Token-Level Temperature Scaling](https://arxiv.org/html/2604.07172v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 生成前scalar温度改变样本law，不是后置单调映射；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)生成law/语义类/选择协议联合身份 |
| [SwarmIO: Towards 100 Million IOPS SSD Emulation for Next-generation GPU-centric Storage Systems](https://arxiv.org/html/2604.06668v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | GPU-initiated I/O模拟器自身ceiling污染被模拟设备判断；2+2+2=6 | 标准完成 | 仅报告：DSA/全局timing state与受限SSD模拟案例，不将40M模拟当100M实测 |
| [FP4 Explore, BF16 Train: Diffusion Reinforcement Learning via Efficient Rollout Scaling](https://arxiv.org/html/2604.06916v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 低fidelity seed搜索与BF16目标重生成分离；2+2+2=6 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)Low-fidelity Exploration与Objective Artifact分离 |
| [Self-Preference Bias in Rubric-Based Evaluation of Large Language Models](https://arxiv.org/html/2604.06996v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | objective rubric仍有self/family bias且committee不消除；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)独立judge校准与同源偏差 |
| [On the Step Length Confounding in LLM Reasoning Data Selection](https://arxiv.org/html/2604.06834v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | step-boundary比例改变mean-likelihood筛选对象；2+2+2=6 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)step-boundary混杂与受控数据替换 |
| [MirageBackdoor](https://arxiv.org/html/2604.06840v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 训练辅助target在部署stop delimiter后，visible CoT不等完整监督；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)训练target/可见截断边界 |
| [ForkKV: Scaling Multi-LoRA Agent Serving via Copy-on-Write Disaggregated KV Cache](https://arxiv.org/html/2604.06370v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | base/residual两类KV状态与近似共享不等exact；2+2+2=6 | 深入完成 | 整合：INFER-KV-CACHE [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)跨adapter物理共享与语义近似分账 |
| [Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start](https://arxiv.org/html/2604.06664v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 跨process Graph需要execution context重绑定；2+2+2=6 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)跨进程Graph恢复 |
| [DiffuMask: Diffusion Language Model for Token-level Prompt Pruning](https://arxiv.org/html/2604.06627v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 反向DLM二值retention与teacher标签/多步成本；2+1+2=5 | 标准完成 | 仅报告：标签搜索/64步运行点尚未证明端到端break-even |
| [Scheduling the Unschedulable: Taming Black-Box LLM Inference at Scale](https://arxiv.org/html/2604.06970v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 外部API只拥有arrival shaping，三轴控制frontier；2+2+2=6 | 标准完成 | 仅报告：mock和先验条件不支持生产默认策略 |
| [Distributed Interpretability and Control for Large Language Models](https://arxiv.org/pdf/2604.06483v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | deferred projection省重复forward但实测表含占位冲突；1+2+2=5 | 争议 | 暂缓：需修正占位表、时间与模型层身份 |
| [CubeGraph: Efficient Retrieval-Augmented Generation for Spatial and Temporal Data](https://arxiv.org/html/2604.06616v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | metadata拓扑与动态filter发现的控制流有反例；2+2+2=6 | 争议 | 暂缓：Algorithm4新cube不可达，需勘误与对应验证 |
| [Autopoiesis: A Self-Evolving System Paradigm for LLM Serving Under Runtime Dynamics](https://arxiv.org/html/2604.07144v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | trigger/planner联合身份与异步策略代码不同于在途计划；2+2+2=6 | 深入完成 | 整合：INFER-SCHEDULING [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md)成对调度策略验收 |
| [Benchmarking LLM Tool-Use in the Wild](https://arxiv.org/html/2604.06185v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 合法工具拓扑集合不等唯一reference序；2+2+2=6 | 标准完成 | 仅报告：人工依赖图/模拟任务协议，未采为任意tool验收 |
| [The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?](https://arxiv.org/html/2604.06192v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | query-answer/trace联合coupling区分信息与token熵；2+1+2=5 | 标准完成 | 仅报告：SIA/小joint-KL假设不证明实际内部知道或早停 |
| [Blind Refusal: Language Models Refuse to Help Users Evade Unjust, Absurd, and Illegitimate Rules](https://arxiv.org/pdf/2604.06233v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | rule defeat、独立危险与实际帮助行为分开；1+2+2=5 | 深入完成 | 仅报告：normative gold/合成proxy不授权系统默认规则规避 |
| [Spectral Edge Dynamics Reveal Functional Modes of Learning](https://arxiv.org/html/2604.06256v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 谱gap/扰动/转基揭示局部学习诊断对象；2+1+2=5 | 标准完成 | 仅报告：小型模运算与hidden-state诊断不构成普适functional detector |
| [Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks](https://arxiv.org/html/2604.06366v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 参数动力学/状态依赖噪声不同于线性函数类；2+1+2=5 | 标准完成 | 仅报告：balanced-aligned/teacher/SDE条件不外推Transformer LR |
| [$S^3$: Stratified Scaling Search for Test-Time in Diffusion Language Models](https://arxiv.org/html/2604.06260v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | reward-tilted目标与有限粒子proxy重采样分离；2+2+2=6 | 标准完成 | 仅报告：无exact twist correction，不采为默认生成law |
| [STDec: Spatio-Temporal Stability Guided Decoding for dLLMs](https://arxiv.org/html/2604.06330v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 空间扰动与跨步稳定counter共同提议commit；2+2+2=6 | 标准完成 | 仅报告：具体双信号heuristic与有限slice，不当不可逆输出保证 |
| [ClawLess: A Security Model of AI Agents](https://arxiv.org/html/2604.06284v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | SMT配置/LTL意图与syscall mediation有未证明桥；1+2+2=5 | 深入完成 | 仅报告：形式model不证明完整eBPF强制执行 |
| [Does a Global Perspective Help Prune Sparse MoEs Elegantly?](https://arxiv.org/html/2604.06542v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 跨层预算与cluster entropy的soft约束/reset；2+1+2=5 | 标准完成 | 仅报告：启发式剪枝和不同评价预算，不当硬entropy保证 |
| [MoE Routing Testbed: Studying Expert Specialization and Routing Behavior at Small Scale](https://arxiv.org/pdf/2604.07030v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | balance scope/capacity改变specialization与方法排序；2+2+2=6 | 标准完成 | 已有覆盖：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)global/local balance与capacity/quality分账 |
| [Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs](https://arxiv.org/html/2604.06298v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 难度过滤与有限有效reward/预算的反例；1+2+2=5 | 标准完成 | 已有覆盖：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)difficulty curriculum与filter bias |
| [Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability](https://arxiv.org/html/2604.06628v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 早期dip、欠优化与持续遗忘不能只看一个checkpoint；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)条件性SFT轨迹与停止边界 |
| [Efficient Quantization of Mixture-of-Experts with Theoretical Generalization Guarantees](https://arxiv.org/html/2604.06515v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 弱激活特征与expert precision的初始化proxy边界；2+2+2=6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)弱特征与精度分配 |
| [ODE-free Neural Flow Matching for One-Step Generative Modeling](https://arxiv.org/html/2604.06413v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | map conditional mean与coupling的必要充分主张有反例；2+2+2=6 | 争议 | 暂缓：Theorem2条件/证明需修正，不采用OT必要性保证 |
| [The Depth Ceiling: On the Limits of Large Language Models in Discovering Latent Planning](https://arxiv.org/html/2604.06427v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 隐式训练的策略发现与已学策略执行须分离；2+1+2=5 | 标准完成 | 仅报告：有限star graph预算不支持普适depth上界 |
| [In-Context Learning in Speech Language Models: Analyzing the Role of Acoustic Features, Linguistic Structure, and Induction Heads](https://arxiv.org/html/2604.06356v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 声学模仿/content与局部head干预分离；1+2+2=5 | 标准完成 | 仅报告：单模型TTS/合成发音限制，不采为通用speech ICL机制 |
| [AudioKV: KV Cache Eviction in Efficient Large Audio Language Models](https://arxiv.org/html/2604.06694v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | head预算与importance-score频谱平滑的局部方法；2+2+2=6 | 标准完成 | 仅报告：受限ASR/ST/QA协议，不当通用缓存默认 |
| [Drifting Fields are not Conservative](https://arxiv.org/html/2604.06333v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 位置归一化改变sample drift可积性；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)vector field与标量代理目标 |
| [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](https://arxiv.org/html/2604.06374v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | latent必要性与soft-token语义路径必须干预验收；2+2+2=6 | 深入完成 | 整合：MODEL-DECODER-ONLY [Ch18](../../../../books/part-02-model/18-decoder-only.md)latent必要性边界 |
| [Do We Need Distinct Representations for Every Speech Token? Unveiling and Exploiting Redundancy in Large Speech Language Models](https://arxiv.org/html/2604.06871v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 输入/深层audio pooling不同信息责任与净成本；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)audio压缩位置 |
| [Learning to Interrupt in Language-based Multi-agent Communication](https://arxiv.org/html/2604.06452v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 接收者控制打断、完整未来对话净收益与协调成本；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)接收方停止控制 |
| [Improving Robustness In Sparse Autoencoders via Masked Regularization](https://arxiv.org/html/2604.06495v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 输入mask干预feature absorption与保真/探针收益分账；2+1+2=5 | 标准完成 | 仅报告：受限SAE训练recipe与保真代价 |
| [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/html/2604.06636v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 分段potential与variable discount改变credit目标；2+2+2=6 | 标准完成 | 仅报告：具体层次credit启发式，不采policy不变保证 |
| [Reasoning Fails Where Step Flow Breaks](https://arxiv.org/html/2604.06695v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | OEB桥接mass/SMI状态修复及预算不可行反例；2+2+2=6 | 争议 | 暂缓：Eq8/Algorithm1需合法mass约束或clamp澄清 |
| [Inference-Time Code Selection via Symbolic Equivalence Partitioning](https://arxiv.org/html/2604.06485v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | bounded symbolic分歧搜索与最大行为簇不等正确；2+2+2=6 | 标准完成 | 仅报告：受限functional selector，不当等价或truth证明 |
| [Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of Large Language Models](https://arxiv.org/html/2604.06767v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | FP32 margin诊断与聚合收益掩盖token slice退化；2+1+2=5 | 标准完成 | 仅报告：单模型几何干预，不采一般manifold/无损保证 |
| [AI-Driven Research for Databases](https://arxiv.org/html/2604.06566v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | evaluator共演化需多真实baseline与proxy/物理状态校准；2+2+2=6 | 标准完成 | 仅报告：数据库ADRS实例，不直接采为LLM性能保证 |
| [Walk the Talk: Bridging the Reasoning-Action Gap for Thinking with Images via Multimodal Agentic Policy Optimization](https://arxiv.org/html/2604.06777v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 视觉label-observation reward与降方差证明缺桥；2+2+2=6 | 争议 | 暂缓：dense score必降gradient variance的条件未成立 |
| [Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization](https://arxiv.org/html/2604.07165v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 近似trajectory合并/树回传与局部手术更新；2+2+2=6 | 标准完成 | 仅报告：树近似与追加rollout成本未支持默认Agent训练方案 |
| [TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories](https://arxiv.org/html/2604.07223v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 执行轨迹guard的可见面/标签和JSON能力反证；2+2+2=6 | 深入完成 | 仅报告：受控静态guard测量，不能采部署授权保证 |
| [SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems](https://arxiv.org/html/2604.06811v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 同run工具片段重组为新的executable身份；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)same-run重组的执行admission |
| [Steering the Verifiability of Multimodal AI Hallucinations](https://arxiv.org/html/2604.06714v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 人类可核性与模型Yes/No discrimination不同对象；2+2+2=6 | 标准完成 | 仅报告：离散判断probability不能代替自由生成幻觉率 |
| [From Static to Interactive: Adapting Visual in-Context Learners for User-Driven Tasks](https://arxiv.org/pdf/2604.06748v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | interaction cue进入既有图像token空间的可见性瓶颈；1+2+2=5 | 标准完成 | 仅报告：训练cue codec/LoRA的新分支，不作通用交互模型 |
| [How Long Reasoning Chains Influence LLMs' Judgment of Answer Factuality](https://arxiv.org/html/2604.06756v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 同answer是否附trace改变judge verdict，pass不等正确；1+2+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)PRM transformation/ref-outcome与clean twin |
| [The Impact of Activation Steering on Answer Generation and Scoring in Educational Applications](https://arxiv.org/html/2604.07102v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | generator与scorer persona联合身份及同valence偏差；1+2+2=5 | 标准完成 | 仅报告：同一教育数据/自动judge测量，不外推MoE机制 |
| [Language Bias under Conflicting Information in Multilingual LLMs](https://arxiv.org/html/2604.07123v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 冲突证据language顺序可污染reader选择；1+2+2=5 | 标准完成 | 仅报告：人工冲突haystack与选择子集边界 |
| [Beyond End-to-End: Dynamic Chain Optimization for Private LLM Adaptation on the Edge](https://arxiv.org/html/2604.06819v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | adapter顺序冻结/局部全局proxy与内存-目标耦合；2+2+2=6 | 标准完成 | 仅报告：链式训练算法及proxy条件，非隐私保证 |
| [Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models](https://arxiv.org/html/2604.06912v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 查询触发局部再观察须分账前缀缓存、gate误停和训练矿样偏差；2+2+2=6 | 标准完成 | 仅报告：具体ROI gate/target训练分支，不采默认视觉质量或通用加速 |
| [Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/html/2604.06939v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 长期语义anchor和近邻运动使用不同KV与位置身份；2+2+2=6 | 标准完成 | 仅报告：global/local cache及位置规则的实验性视频生成算法 |
| [Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation](https://arxiv.org/html/2604.06950v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 人可读但模型难转录的输入挑战moderation前端而非单纯policy推理；2+2+2=6 | 深入完成 | 仅报告：感知smuggling的受控静态安全测量，不采开放防御保证 |
| [MAR-GRPO: Stabilized GRPO for AR-diffusion Hybrid Image Generation](https://arxiv.org/html/2604.06966v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | diffusion路径likelihood噪声与更新token选择不能只按最终reward解释；2+2+2=6 | 标准完成 | 仅报告：多trajectory信用与reliability mask改变图像生成目标 |
| [Compact Constraint Encoding for LLM Code Generation: An Empirical Study of Token Economics and Constraint Compliance](https://arxiv.org/pdf/2604.07192v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | constraint表示压缩和compliance须分账实际token、scorer与失败样本；2+2+2=6 | 标准完成 | 仅报告：有限任务负面结果，格式非万能且无差异不等形式等价 |
| [INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/html/2604.07209v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | reference/history缓存与camera warp应区分几何条件和环境transition；2+2+2=6 | 标准完成 | 仅报告：相机可控视频近似状态路线，不当物理闭环或通用实时保证 |
| [DISSECT: Diagnosing Where Vision Ends and Language Priors Begin in Scientific VLMs](https://arxiv.org/html/2604.06250v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | VLM输入消融须控制oracle内容、description成本和语言prior；2+2+2=6 | 标准完成 | 仅报告：输入干预的诊断协议，不把oracle差值归为纯感知因果 |
| [Diffusion Processes on Implicit Manifolds](https://arxiv.org/html/2604.07213v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 图随机游走近似生成元和切空间协方差需要几何与尺度条件；2+1+2=5 | 标准完成 | 仅报告：隐式manifold上的受条件随机采样构造，不外推有限样本生成保证 |
| [Fast-dVLM: Efficient Block-Diffusion VLM via Direct Conversion from Autoregressive VLM](https://arxiv.org/pdf/2604.06832v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | response/vision/turn共同决定双流mask与缓存身份；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)多轮多模态生成可见性 |

| [AGSC: Adaptive Granularity and Semantic Clustering for Uncertainty Quantification in Long-text Generation](https://arxiv.org/html/2604.06812v1) | 2026-04-09T08:00:00+08:00 ～ 2026-04-09T09:00:00+08:00 | 中性关系触发粒度细化，但主题质量加权公式抵消，须核聚合因果解释；2+1+2=5 | 争议 | 暂缓：Eq11–13与Table2 clustering消融缺少实现/公式桥，不据主题加权保证整合 |

## 4. 证据与知识整合

### [AGSC: Adaptive Granularity and Semantic Clustering for Uncertainty Quantification in Long-text Generation](https://arxiv.org/html/2604.06812v1)

**Evidence：** 论文实验与中心公式争议；5分因具体反证深入。root实际读exact-v1 §3.2–3.5/Eq1–13、§4.1–4.2及§5.1–5.3/Tables1–2，apr03独立核Eq10–13/Table2。五个回答以首个为anchor，其余四个对比，chunk经max-entailment匹配；NLI归一化忽略neutral，中性比例与gap决定原chunk保留、原子分解或Skip。有效单元集合改变，可能改变成本与不确定性对象，不能用旧“训练技巧未改变ownership”关闭。可是固定该集合与局部分数后，令M_k=Σ_hγ_hk、U_k=Σ_hγ_hkU_h/M_k、w_k=M_k/Σ_jM_j，则Eq13恰为Σ_hU_h/|H1*|，与GMM无关，因为每个h的posterior求和为1；空簇省略仍如此，空有效集合须另定义。Table2去clustering改变BIO和LongFact相关系数，正文未给改变局部分数或非线性后聚合的桥。因此隔离主题加权收益的因果解释，不否定自适应粒度及全部有限经验；需对应版本的公式勘误或实现解释后定点重开，不采用到Ch66/77。

配置为GPT-4.1-mini、Qwen2.5-32B、Llama3-70B回答，DeBERTa-MNLI与gte表征，n=5、temperature=.7、UMAP32维/15邻居、full-covariance GMM/BIC及RTX4090；BIO/LongFact的FactScore相关性不是频率校准或真实拒答保证。precision、batch、concurrency、SLO与置信区间在本次必要证据中为Not Disclosed。v1 Updated=2026-04-09T00:34:53Z仅作为结合本批公告规则与身份分配的可用上界，不将DOI-created=01:58:15Z当首发。

### [Fast-dVLM: Efficient Block-Diffusion VLM via Direct Conversion from Autoregressive VLM](https://arxiv.org/pdf/2604.06832v1)

**Evidence：** 论文实验。官方PDF v1 §3.2–3.4/Figure3、Tables1–2已实际读，并与HTML必要机制一致：noisy stream只含response text，vision只保存在clean stream；N2N块内双向、N2C先前clean、C2C token causal，末response块在turn边界截断，避免短答案跨入下一轮prompt。直接从已对齐VLM迁移与text-first路径初始化不同，预算受控结果不证明相同能力ceiling；AR种子、proposal/causal匹配前缀及KV裁剪不自动保持任意sampling分布。Qwen2.5-VL-3B，block2→32、两CE各0.5；单H100 batch1，MDM短回答均值73.3低于AR74.0，长回答21.4低于26.3、spec24.6亦未无损；FP8/SGLang优化不是生产SLO。本项6分因具体知识缺口深入，Ch24 MARS之后/Block Boundary之前实际补入role/modality/turn的可见性与共存边界；root必要原文、实际两段及邻接独立写后通过。

### [Q-Zoom: Query-Aware Adaptive Perception for Efficient Multimodal Large Language Models](https://arxiv.org/html/2604.06912v1)

**Evidence：** 论文实验。exact-v1 §III-A/C、§IV-C与TableIV已读：以末查询状态决定是否zoom，再由query/visual attention构造Gaussian区域并重编码；插入ROI后只复用插入点前的prefix KV，移位的user部分重算，不是全prompt exact复用。Base正确/ROI错误的hard-mining用于target SFT，视觉encoder/projector冻结；attention sink过滤与统计阈值不是区域真值。gate在Doc均值86.1→85.6及高分辨率切片67.3→66.6有退化；576视觉token、A6000的相对吞吐仍低于base，不能外推全服务加速。先前SDRPN作为既有组件，本次增量是gate/训练耦合；Ch23已有主动观察与预算—任务质量边界，本具体ROI算法保留为6分标准仅报告，不声称完整同算法覆盖。

### [Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/html/2604.06939v1)

**Evidence：** 论文实验。exact-v1 §4.1–4.3与§5已读：三个global anchors不参与普通rolling eviction，但仍可按diversity规则替换，不能叫永不变化；六个近期local片段滚动。novelty/redundancy余弦规则决定选择，raw pre-RoPE key及global/local位置分别重绑定，scene切换重置local而保留global。提示词切换用邻近加权KV插值，是近似条件控制，不证明同完整历史分布或物理状态持续。Wan2.1-T2V-1.3B，832×480/16fps、32H20训练与MovieGen提示切片；240s部分aesthetic/motion指标下降，不能说所有切片最好或无限时长无损。与Ch24语义/近期状态分工对照后，保留该cache/位置策略及经验范围，6分标准仅报告，不将这套启发式变为默认世界模型。

### [Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation](https://arxiv.org/html/2604.06950v1)

**Evidence：** 论文实验；安全变化作6分深入必要审阅。exact-v1 §3、§4.1–4.3和Limitations已读：1700条静态输入/九类视觉编码，人工转录可读性约束；先transcribe后classify的两阶段协议把输入辨识和判定作行为分账，但多一次prompt不能完整因果分离vision/reasoning。TER按字符集合包含率，不保词序和语义；ASR是分类错误，不是真实有害执行。GPT-5/Gemini2.5-Pro/Qwen3-VL切片中CoT可能减ASR同时提高FPR，illusion不一定改善；Qwen2.5-VL-7B平衡1700+1700 SFT的50/50 split有style confound。Ch72已要求模态关键语义与matched benign/attack切片，未声称现文完整包含这个具体攻击；报告保留测量与限制，不以该静态数据推开放moderation或部署防御。

### [MAR-GRPO: Stabilized GRPO for AR-diffusion Hybrid Image Generation](https://arxiv.org/html/2604.06966v1)

**Evidence：** 论文实验。exact-v1 §3.1–3.4与§4已读：AR latent配diffusion head，训练用denoising路径logprob近似，不能视为终态marginal的精确ratio；冻结decoder稳住映射，但未分离所有variance原因。多个trajectory期望、按variance取top-k token与最终cosine改善mask改变更新目标；未来结果依赖的mask不等无偏原GRPO，过强平均亦会oversmooth。NOVA0.6B/512²与Harmon1.5B，训练12AR/10denoise、推理64AR/25DDIM，CFG5/3、group4、KL.01；HPS/GIT/GroundingDINO代理reward不证明事实grounding或相同预算收益。6分标准仅报告该混合生成后训练算法，不据稳定曲线采用一般收敛保证。

### [Compact Constraint Encoding for LLM Code Generation: An Empirical Study of Token Economics and Constraint Compliance](https://arxiv.org/pdf/2604.07192v1)

**Evidence：** 论文实验。HTML不可取，已实际读官方PDF v1 §3/4/§5.1–5.6：三编码与不同传播链在同S1设计文档下比较，S/SN改变上游prompt并非全部完全匹配；12主任务+4扩展、247完整pipeline，失败pipeline选择与隐藏WorkBuddy prompt是限制。CSR由imports/regex/static pattern打分，不保证运行质量；原scorer73→47需人工纠错，CSS主导且额外非CSS证据集中一任务。约±3pp区间是post-hoc，不显著不是等价检验；字符/constraint token/完整prompt成本不能混算，不能把摘要71.4%直接叫全prompt实测token收益。Ch75/Ch66的tokenizer成本与独立验证原则不因本切片改变；6分标准仅报告新受限反证，而非已有全实验覆盖或通用免费压缩recipe。

### [INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/html/2604.07209v1)

**Evidence：** 论文实验。exact-v1 §3.2–3.4、§4及§5.1已读：reference/近邻history进入固定位置ST cache，训练仍完整rollout后按chunk反算，省激活不等无重算；6DoF相机累计、depth warp与validity mask只条件化本块，history几何通道置零避免把旧条件当当前动作。JDMD交替真实T2V与合成V2V任务，teacher/共享参数不证明梯度互不干扰。Wan1.3B/TinyVAE、WorldScore与RE10K支持受限camera control；动态360纹理与持久状态仍会失败，不能称真实物理simulator。24fps缺完整hardware/resolution/batch/precision/SLO不采用正面数字。Ch25 observed/belief/imagined与camera≠action consequence边界不改变；6分标准仅报告本实现。

### [DISSECT: Diagnosing Where Vision Ends and Language Priors Begin in Scientific VLMs](https://arxiv.org/html/2604.06250v1)

**Evidence：** 论文实验。exact-v1 §3.3–3.4、§4.1与§5.8已读：V+T、text-only、把问题渲染为图的vision-only、人工描述oracle、模型两遍description→text-only分别改变可用内容和接口；18模型/12k题、Chem7k/Bio5k只是该pipeline评估材料，不恢复AI-for-Science应用路线。CoT/native thinking/第二遍保留图像对照给有用诊断，但human oracle可包含接近答案的标签，render/description/token budget不匹配，不能把oracle成功一概叫纯perception failure。闭源模型gap可能随CoT反转、开源description改善不能证明架构因果。Ch66模态必要性和oracle/input契约承载一般边界，本研究保留为6分标准有限协议及反证，不写确定内部瓶颈。

### [Diffusion Processes on Implicit Manifolds](https://arxiv.org/html/2604.07213v1)

**Evidence：** 条件理论及数值实验。exact-v1 §3–5.1、§6/7已读：compact isometrically embedded manifold、iid体积采样下，proximity graph随机游走近似generator，carré-du-champ给切空间covariance，再以ambient SDE/Euler–Maruyama采样。定理使用N→∞及h/epsilon→0的regularity条件，不证明有限点云或大步长exact留在流形。可选DRGD score修正额外引入训练与score误差，不是前面纯几何定理本身；sphere/MNIST可视化不证明foundation model训练/推理改进。5分标准保留这一替代采样分支的数学条件，不把N维图示当普遍数据manifold或新默认生成机制。

### [Reason in Chains, Learn in Trees: Self-Rectification and Grafting for Multi-turn Agent Policy Optimization](https://arxiv.org/html/2604.07165v1)

**Evidence：** 论文实验。§3.1–3.2/Eq2–12/Algorithm1与§4已读。按next-action KL及过去状态改动action集合合并节点，再用经验边频率Bellman回传，divergence处Bradley–Terry masked loss；KL相近不具传递性，action集合也不保存执行顺序或完整环境state，所以Cognitive Tree不等exact Markov图。方差结论需独立性、group normalization却耦合；Algorithm1差值触发额外rollout，不采用‘无需追加rollout’普遍宣传。Qwen2.5-3B/Phi4-mini，160步/3 seeds、五类受限任务；训练总成本和grafting成本未完整匹配。6分标准仅报告新算法/边界，不把全文已有主题误作实际同等覆盖。

### [TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories](https://arxiv.org/html/2604.07223v1)

**Evidence：** 论文实验。安全必要审阅§3/4.1–4.4及AppA/D.1：从BFCL高执行正确轨迹生成合法seed，按风险规则变异并截在相关调用前；测的是guard判断，不是Agent实时干预恢复。1170实例、12风险/4领域；13通用模型与7专用guard，taxonomy/binary与multiclass接口并非完全匹配。JSON相关性不证明结构能力是因果瓶颈，较长轨迹与更多证据/组成混杂；静态合成seed不构成开放安全真值。Ch72的局部动作/整轨迹分账和Ch66 sensor可见面已承担通用判断，但本算法数据与judge接口的具体结果仍是有限新测量，仅报告，不强行追加Books。

### [SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems](https://arxiv.org/html/2604.06811v1)

**Evidence：** 论文实验。§3/4.1–4.3/5.1–5.4必要原文与目标/相邻Ch71/73已读：攻击持久载体是installed SKILL.md/脚本，带编号XOR/Base64片段经本次多次tool output回灌后重组/解码并执行；不混同跨run片段持久化。普通SQL答案正确与side-effect marker必须分账；攻击依赖原有执行权限，不是正确sandbox突破。EHRSQL受控代码agent、9模型、poison配置；N过大缺片，heuristic flag不是有效防御。Ch72原side-effect段之后真实补入新executable字节/source lineage/权限与effect admission，明确这是工程推断。root实际原文/正文/邻接非作者PASS，不是整日Gate。

### [Steering the Verifiability of Multimodal AI Hallucinations](https://arxiv.org/html/2604.06714v1)

**Evidence：** 论文实验。§2–5已读：40人限时判断构建obvious/elusive标签，以干净与幻觉样本activation差选方向并做混合ablation。实际评估是Yes/No/Uncertain三token概率，不是自由生成的虚假atomic-claim频率，也未在人类重新审核中证明可核性改善。Qwen2.5VL3B/7B、LLaVAOneVision8B，8×4090；方向选择依赖validation，多模型/两类指标不一致且Uncertain会上升。仅报告测量对象及受限干预，不据此声称模型感知真实知识边界或通用幻觉控制。

### [From Static to Interactive: Adapting Visual in-Context Learners for User-Driven Tasks](https://arxiv.org/pdf/2604.06748v1)

**Evidence：** 论文实验。HTML两次未恢复后实际读官方PDF v1 §3.1–3.3/4/5.1。click/scribble/box直接混入示例图像，不增加独立cue token；VQGAN重训使小cue存活，代价是覆盖原像素。DeLVM300M LoRA Q/V、2048 tokens、3 examples、8×A100；held-out interaction实验为不同cue各自训练模型，不是一个冻结万能模型。256px四类受限任务，unseen明显弱于seen/SAM2。5分保留conditioning机制，不因视觉任务/小规模自动拒绝，但不把此实现采为长期通用控制方案。

### [How Long Reasoning Chains Influence LLMs' Judgment of Answer Factuality](https://arxiv.org/html/2604.06756v1)

**Evidence：** 论文实验。§3–5.3实际读：同答案附/不附generator reasoning，再注入固定长度无关真/假陈述控制流畅性、事实性与前后位置。Qwen3多规模/DeepSeek generator，NQ/HotpotQA/GSM8K/MATH500各约500、temperature .6；reference也使用Qwen2.5-72B核对不是无误gold。弱judge pass升高可是假阳性，强judge也会过拒与被错误流畅trace误导，不能按能力二分保证。Ch66现有‘Process Reward Model成为Sensor前Transformation Stability’与clean/noisy twin正文已明确reference/independent outcome、输入扰动和verdict转移分账；具体实验留Daily而不重复书稿。

### [The Impact of Activation Steering on Answer Generation and Scoring in Educational Applications](https://arxiv.org/html/2604.07102v1)

**Evidence：** 论文实验。官方必要§3/4.1–4.3：七persona通过对比activation方向固定中层α=2；generator与scorer独立或同向组合后比较答案质量与评分。Qwen3-4B/32B和gpt-oss20B、10个ASAP-SAS prompt、4500答案、GPT5.2外部quality judge；模型架构/规模不匹配，不证明MoE导致鲁棒性。persona valence使scorer calibration移动但32B部分差异不显著，外部judge也非绝对学习gold。5分只报告联合评估身份的新受限反证，不采通用persona部署策略。

### [Language Bias under Conflicting Information in Multilingual LLMs](https://arxiv.org/html/2604.07123v1)

**Evidence：** 论文实验。§3–5.2必要正文已读：240双语contrastive pair换needle语言，900haystacks/4500query每模型、5语言/12模型，greedy/开源单H100、1000或25000words。both-name启发式识别冲突不等完整矛盾oracle；仅一对交换结果不同的子集才进入binomial语言偏好，最高大约97/1200，不能把局部语言选择当所有query主因。当前Ch76 relevance/sufficiency/conflict abstention有通用控制；新测量留报告而不伪称某语言证据拥有事实authority或直接改变production检索政策。

### [Beyond End-to-End: Dynamic Chain Optimization for Private LLM Adaptation on the Edge](https://arxiv.org/html/2604.06819v1)

**Evidence：** 论文实验。§4.1–4.4/5.1/5.4–5.8/限制已读：当前adapter训练后冻结/释放，Q邻域co-tuning换内存与梯度交互，global proxy为更后adapter输出分支而非完整remaining backbone。FOAT单次初始CKA阈值不是功能因果证明；局部+proxy权重与阈值依赖数据。DistilBERT/BERT/RoBERTa分类，Llama2-7B/3.1-8B AlpacaGPT4有限适配；不开共享raw data也不等DP/secure aggregation，梯度仍泄漏可能。6分报告可迁移训练执行分支和代价，尚不采用46.46% headline或通用edge隐私结论。


### [Learning to Interrupt in Language-based Multi-agent Communication](https://arxiv.org/html/2604.06452v1)

实际读§2.1–2.2/3.2/4.1–4.4及C.2/C.4–C.6：固定16-token chunk中的one-token判断由接收者提出，runtime halt/换轮不代替Workflow权限；标签来自完整未来对话的有/无interrupt树分支，不能只算当前发言节省。主实验三种任务、Llama8B/70B接收者、三种发送者、三次运行只允许一个接收者打断；prompt baseline过早停止会增加未来轮次，offline树采样与online判断/协调亦有成本。Ch82通信预算后已真实写三段接收方控制分支，root必要原文/实际正文与latent handoff独立通过；6分gap深入，token代理不等生产时延/SLO。

### [Improving Robustness In Sparse Autoencoders via Masked Regularization](https://arxiv.org/html/2604.06495v1)

实际读§2–4/Table1–3：把输入随机替换为mask string再取LLM activation、训练同一SAE objective，不是另加损失项。Pythia160M层8/Gemma2-2B层12、4096dictionary、500M tokens、MatryoshkaBatchTopK及l0=20/40/80/160只支持本配置；EV与部分probe/TPP退化、raw activation oracle更强均保留。配置p=.3与结语.3%矛盾不抹平；5分标准仅报告其共现shortcut干预，不制定通用解释性或稳健默认。

### [SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation for LLM Reasoning](https://arxiv.org/html/2604.06636v1)

实际读§4.1–4.3/5.1–5.3及Table1–2：entropy cutpoint短forced rollout构造potential，length-dependent gamma改变传统PBRS目标，segment内entropy Z-score/clipped weight再分配credit；高entropy不是因果关键步骤。1.5B/4B三backbone数学设置、五benchmark、temperature.6/top-p.95/k40/max32768有gamma=.7质量退化、去TCR更少token但降低质量反例。6分标准仅报告此实现，额外prefix rollout成本不被平均答案长度消除，不采用一般hack-free/task一致保证。

### [Reasoning Fails Where Step Flow Breaks](https://arxiv.org/html/2604.06695v1)

实际读§4/Eq5–10/Algorithm1、§5.1–5.4：OEB保持其他token mass再提高bridge目标，SMI把前step value平均注入下step首tokenresidual；attention×gradient关联不证明因果流。pO=.9、pS=pB=.05、两集合等大且tauMax=.3满足触发，却给tauS=-.2，Eq8与算法log无定义，故需可行mass约束/实际clamp说明。六数学/科学/代码任务、7B–32B/R1distill/GPT-OSS/QwQ与不同采样数仅经验边界；6分深入争议，不据理论写Books，不否定另一个SMI分支或所有经验。

### [Inference-Time Code Selection via Symbolic Equivalence Partitioning](https://arxiv.org/html/2604.06485v1)

实际官方PDF v1 §3.1–3.3/4.1–4.4/5与HTML对照：CrossHair/Z3在显式domain assumptions下搜索分歧，预算内没有反例只作近似等价；greedy representative/tie顺序与largest cluster不等ground truth。HumanEval+164、过滤LCB438、八4B–20B模型/N5/10/20；pairwise accuracy只含至少一正确的pair而排除wrong–wrong。Ryzen7700X solver与H100生成/CodeT并非同设备归一SLO；摘要与§4.2均值不同，不采headline。6分标准仅报告方法，路径爆炸、隐含约束与错误共识仍在。

### [Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of Large Language Models](https://arxiv.org/html/2604.06767v1)

实际HTML §2.2–3.7/4.1–4.11及官方PDF v1首页身份：BF16 lm_head matmul会使小margin落粗网格，upcast重算只诊断该出口；Fisher top-k为近似，非全softmax metric。Qwen3.5-4B/WikiText103、200steps/seed0/CE始终开启、训练与margin审计同语料、full-model含tied embedding更新；无CE-only或frozen-backbone对照不能把全部收益归于单输出边界。频率/类别的损害与有限下游均分同时存在，loglikelihood均分不证明词汇统一收益；5分标准仅报告条件性几何方法，不采用所引定理的一般系数保证。

### [AI-Driven Research for Databases](https://arxiv.org/html/2604.06566v1)

实际读§2.3/3/4.1–4.3/5.1–5.3：outer evaluator暴露scan/dirty-page成本、多groundtruth baseline校准，solution inner loop不能只优化错误的hit-rate/cost proxy；isolated warmup协议与共演化fitness仍需独立验证。GPT5/OpenEvolve、Postgres14/EC2 c5.18xlarge72核144GiB/200GB SSD、TPC-H/DS和500MB index预算；policy在DS演化、H测试，但query排除和缓存序列是协议条件。6分标准仅报告此evaluator实际设计；数据库受限收益不外推LLM系统，真实groundtruth可用性及evaluator/solution共同过拟合仍需验证。

### [Walk the Talk: Bridging the Reasoning-Action Gap for Thinking with Images via Multimodal Agentic Policy Optimization](https://arxiv.org/html/2604.06777v1)

实际读§3.1–3.3/Algorithm1、§4.1–4.3/5.1–5.2：生成期待视觉label与crop/zoom observation的CLIP相似度作为trajectory reward，不是每step的因果credit；whole-trajectory outcome与semantic advantage相加改变目标。root独立补核A.2确有sigmaSem<sigmaOut假设，但dense/连续分数不是该假设的证明，给定完整tau两种deterministic rewards允许conditional variance同时为0；positive correlation也不保证conditional expected gradients成比例、sampling项“comparable”不足推出严格总方差界。争议的是正文普遍保证与实现/假设未建立，不声称条件定理在全部假设下已被普遍证伪。Ovis2.5-9B、三个高分辨率benchmark的Avg@8/Avg@1及有限训练曲线可保留经验，部分slice仍非最佳，图例不证明语义一致性；6分深入争议暂缓Books，不否定受限经验。


### [Efficient Quantization of Mixture-of-Experts with Theoretical Generalization Guarantees](https://arxiv.org/html/2604.06515v1)

实际exact-v1 §3.3/4.1–4.3/5.1–5.4：norm change是final norm减initial norm，rare-feature理论有二元相关token与初始alignment条件。final-norm proxy仅重新初始化Switch对照，不是语义真值；Mixtral任务排序和低平均位宽有反例。Ch21已经实际写入弱特征/初始化proxy精度分支，root必要原文/正文/相邻交接独立通过；6分gap深入，不采用无损或生产latency宣传。

### [ODE-free Neural Flow Matching for One-Step Generative Modeling](https://arxiv.org/html/2604.06413v1)

实际§3.2/4.1–4.4/Theorems1–2/5.1–5.2。以x0为条件的MSE最优endpoint是conditional mean；non-independent joint不保证该mean非常数：x0=0/1各半，x1|0=±1各半而x1|1=0，联合非独立但两处mean均0。root已独立确认Theorem2反例，6分深入争议、Books暂缓；不由此否定额外确定性OT条件、toy经验或所有one-step生成，恢复需作者修正条件与证明。

### [The Depth Ceiling: On the Limits of Large Language Models in Discovering Latent Planning](https://arxiv.org/html/2604.06427v1)

实际§2.2–2.4/3–6：strict implicit/star graph/single CE/有限预算区分策略discovery与execution深外推；最佳checkpoint和attention关联不证明普适算法或depth ceiling。2+1+2=5标准仅报告，不把无CoT的受限任务变成现代LLM规划深度定律。

### [In-Context Learning in Speech Language Models: Analyzing the Role of Acoustic Features, Linguistic Structure, and Induction Heads](https://arxiv.org/html/2604.06356v1)

实际§2–4与head干预：SpiritLM的合成双女声TTS、速度/pitch/intensity控制区分spoken-content与style；rate效应强不意味着所有声学特征通用。top-k50 prefix-matching head消融对照random/non-prefix，局部支持必要性，不证明唯一ICL电路；Whisper转录评价与语音保真不同对象。5分标准仅报告单模型/有限语音协议，不因其可归Attention就声称现有Books完整承载该实验。

### [AudioKV: KV Cache Eviction in Efficient Large Audio Language Models](https://arxiv.org/html/2604.06694v1)

实际§3.1–3.3/Eq1/12/Algorithm1与§4：离线WhisperX alignment统计提出head预算，importance score FFT低通/残差平滑不是原始audio去噪，也不是truth oracle。A100、五Gemma/Qwen模型ASR/ST及QA的40%KV/受限输出和Gemini judge仅局部协议；Qwen2.5-3B某slice仍失败。6分标准仅报告此可迁移候选算法，不当任何LALM默认，不把KV预算节省直接等端到端SLO。

### [Drifting Fields are not Conservative](https://arxiv.org/html/2604.06333v1)

实际§2–5/6：sample-space位置归一化可破坏curl-free，Gaussian与匹配sharp kernel是条件分支；这不否认参数scalar stop-gradient surrogate，moving q亦不保证固定全局势。小DiT/MNIST与Fashion有限训练不能泛化完整生成模型质量。Ch24主线已实际写入vector field/目标分账，root必要原文/正文独立通过；6分gap深入。

### [The Illusion of Superposition? A Principled Analysis of Latent Thinking in Language Models](https://arxiv.org/html/2604.06374v1)

实际§3–7：off-the-shelf argmax替换/entropy probe与fine-tuned ProsQA latent移除为不同证据；99%对96.6%暗示shortcut但不证明全latent无效。scratch浅层必要性与深层边际递减受到per-hop curriculum混杂，probe读不到路径不证明内部不存在。Ch18主线已真实加入latent必要性/替代干预与soft token≠语义路径，root必要原文/正文独立通过；6分gap深入。

### [Do We Need Distinct Representations for Every Speech Token? Unveiling and Exploiting Redundancy in Large Speech Language Models](https://arxiv.org/html/2604.06871v1)

实际§3–5/Algorithm1/Table2：input仅相邻ω1，deep允许ω3回看并mean pool；mid-layer对内容重组织敏感，ASR冗余不能等保留prosody。H200短0–20s deep/DAP比Vanilla慢，KV/FLOPs减量不等净时延收益。Ch23已实际加入audio pooling位置与任务/净成本验收，root必要原文/正文独立通过；6分gap深入，不声称无损或exact KV复用。

### [Rethinking Generalization in Reasoning SFT: A Conditional Analysis on Optimization, Data, and Model Capability](https://arxiv.org/html/2604.06628v1)

实际读exact-v1 §2.1–2.2/3.1–3.4/4–6及Table1：所测数学long-CoT SFT有先降后回升，也有高LR/constant长schedule、弱base/低质数据不能恢复与安全slice退化。固定640 steps的2.5k×8/20k×1不自动compute-matched；更长训练不是普遍修复。Ch29原Catastrophic Forgetting后已实际增加早期回退的条件性轨迹、heldout/cost门槛与LoRA handoff，root必要原文/实际正文/相邻交接独立通过，6分gap深入。

### [Benchmarking LLM Tool-Use in the Wild](https://arxiv.org/html/2604.06185v1)

实际读§3.1–3.5/4.1–4.2：人工依赖图允许多种合法topology，逐前缀OP/部分AP不能被唯一reference序或最小depth=latency替代。真人seed→模拟扩展/人工整理、57模型native format构成局部协议。Ch66已有过程/终态，但没有该完整枚举算法；6分标准仅报告，不将人工图当任意真实tool任务gold。

### [The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?](https://arxiv.org/html/2604.06192v1)

实际读§3.1–4.3.2，SIA定义于真实答案与trace的联合coupling；Theorem2有限alphabet、小joint KL、informative true joint仍不自行蕴含SIA。token entropy与answer entropy对象不同，greedy退化非truth。5分标准仅报告条件理论，不向Ch66写为实际内部知识或在线停止保证。

### [Blind Refusal: Language Models Refuse to Help Users Evade Unjust, Absurd, and Illegitimate Rules](https://arxiv.org/pdf/2604.06233v1)

实际官方PDF v1 §3.2–3.5/4核定合成rule-defeat/independent harm与帮助/论证两轴、18配置温度0/8k/OpenRouter身份；摘要14650拒绝数与正文19430总数是不同分母。judge对engagement/harm与human的同意度弱于response分类，NPV仅本样本。5分安全深入仅报告，规范gold/模拟proxy不能授权真实规则规避，不外推headline风险发生率。

### [Spectral Edge Dynamics Reveal Functional Modes of Learning](https://arxiv.org/html/2604.06256v1)

实际读§2.1–2.4/4.1–6.3：2层290k模97运算/三seed/20step窗口的谱gap诊断有例外；固定位置hidden-state扰动不是输出因果效应，未过SAE角度匹配null不证明功能方向不存在。5分标准仅报告受限表示诊断，不采为Ch13/28普适训练sensor。

### [Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks](https://arxiv.org/html/2604.06366v1)

实际读§2.3–2.4/3/4/5：线性函数的参数优化仍有非线性，teacher/whitened Gaussian/在线、balanced-aligned条件下SDE noise依mode状态；学满前peak和stationary结论另需噪声/详细平衡条件。5分标准仅报告可解模型，不向Ch28写为一般SGD或Transformer逐层LR保证。

### [$S^3$: Stratified Scaling Search for Test-Time in Diffusion Language Models](https://arxiv.org/html/2604.06260v1)

实际读§2–3.4/4 setup/Table1：精确reward twist需未来h，N粒子×b分支、clean预测与verifier proxy重采样没有exact importance correction；transition/scoring均有TNb成本。LLaDA8B四benchmark有BoK胜出的slice。6分标准仅报告具体近似search，Ch24原探索/额外forward主线不等其完整算法已存在，也不为任意质量/延迟写生产结论。

### [STDec: Spatio-Temporal Stability Guided Decoding for dLLMs](https://arxiv.org/html/2604.06330v1)

实际读§3.1–3.3/4.1–4.2：Gaussian邻域稳定、跨步一致counter和阈值联合提议commit，阈值衰减不证明truth/未来一致。单4090D、LLaDA/Dream/LaViDa任务级TPS和slice质量退步保留。6分标准仅报告具体双信号实现；Ch24已区分跨步稳定与confidence，未冒称空间探针算法全被吸收，外部副作用仍需独立验收。

### [ClawLess: A Security Model of AI Agents](https://arxiv.org/html/2604.06284v1)

实际读§3–5：SMT核权限model/LTL核时序，再经eBPF sys_enter与tail-call监控。配置满足不等完整强制执行，必要正文未补deny-return、fd/TOCTOU和语义编译正确桥。5分安全深入仅报告提案与未证明边界，不把Ch72已有mandatory mediation当该实现证明，也不推实际攻击必成。

### [Does a Global Perspective Help Prune Sparse MoEs Elegantly?](https://arxiv.org/html/2604.06542v1)

实际读§3.2–3.3/Algorithm1/4.1–4.2：cross-layer redundancy提议预算，cluster entropy冻结但全冻结会reset，是soft heuristic。三MoE/无FT有slice反例、GPT-OSS随机1000题预算不同、未见端到端latency。5分标准仅报告全局预算实现；Ch21已有按层边际收益但不冒称该算法全已有，不把soft阈值当硬保证。

### [MoE Routing Testbed: Studying Expert Specialization and Routing Behavior at Small Scale](https://arxiv.org/pdf/2604.07030v1)

实际PDF v1 §2.2.2/4.2/4.2.5核balance scope、capacity dropping与同utilization不同valid-loss；domain-balanced router是oracle，小testbed到0.8B-active/2T-token仍是有限验证。6分标准已有覆盖：Ch21具体global/local balance、capacity和specialization/quality trade-off，不把小规模排名推生产。

### [Limits of Difficulty Scaling: Hard Samples Yield Diminishing Returns in GRPO-Tuned SLMs](https://arxiv.org/html/2604.06298v1)

实际读§3/4.1–4.3/5的0.5/1.5/3B math-LoRA GRPO、difficulty与matched-size随机/0.5B full-FT控制。format/overflow/迁移退步与step≠latency保留，未证明固定参数内在ceiling。5分标准已有覆盖：Ch33 difficulty curriculum、无有效梯度组、filter bias和再准入；不改通用阈值。

### [Autopoiesis: A Self-Evolving System Paradigm for LLM Serving Under Runtime Dynamics](https://arxiv.org/html/2604.07144v1)

必要exact-v1 §4、§5.2–5.4、§6/§7、AppB/I已实际阅读：trigger和planner是联合策略，分别优化会混淆旧计划继续服务、求解耗时与重配置成本；异步搜索/下一monitoring点替换策略代码不等于迁移在途request state。timeout只限制候选计算，不能证明安全或公平。回放基于解析roofline成本与增强trace、受限同构32 H100/异构64 GPU/弹性A100和Llama配置，AppB公式不是全regime fidelity验证，API/代码生成能力及窗口长短引入新成本。Ch56原调度主线已真实写入成对验收、代码/计划状态分离和旧固定策略共存边界；root实际原文/正文/相邻交接独立通过，6分gap深入。

### [ForkKV: Scaling Multi-LoRA Agent Serving via Copy-on-Write Disaggregated KV Cache](https://arxiv.org/html/2604.06370v1)

实际读exact-v1 §3.2/§5.1–5.3/Algorithm1、§7.1–7.4：共享base projection与adapter低秩residual分别驻留，两RadixTree/LRU支持partial hit；SRAM内重构K并RoPE、共同softmax与V结合律不证明跨adapter层输入相同。§3.2从后续层已是lossy近似。3模型7～14B/BF16/L40或1～2RTX5000/rank16、静态长上下文与mocktool，低4workflow比基线慢，质量仅两个各200例word-F1，不等工具正确性。Ch45跨adapter段已经真实写入两类状态生命周期、读法与近似fallback，root原文/正文/邻接独立通过；6分gap深入。

### [Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start](https://arxiv.org/html/2604.06664v1)

实际读exact-v1 §2.3/§3–6：新进程的kernel handle和opaque VA不能只复用graph拓扑，需确定VA/分配顺序、capture-buffer replay、binary hash/function name与template/node attributes。rank communicator stub重绑定以同结构SPMD为条件，不适用PP不同阶段。固定KV pool、vLLM0.11.2/Torch2.9/CUDA13.1/DGX H200/B200的DP/MoEEP与受测decode不能证明任意配置完全正确。Ch49启动主线已落实跨process execution context与退回重capture边界，root独立通过；6分gap深入，不推广99%headline。

### [DiffuMask: Diffusion Language Model for Token-level Prompt Pruning](https://arxiv.org/html/2604.06627v1)

实际读exact-v1 §3.1–3.2/§4/Limitations：inverse DLM预测retention mask而非重建文本，teacher短RL与进化剪枝产生标签，tokenizer realignment也是接口状态。800 source任务及GSM8K标签搜索依赖过滤正例，10～48小时标签形成成本；64步mask推理约.75分钟，非即时压缩。所测backbone并非全部收益，未充分覆盖dialog/summarization或服务端到端break-even。5分标准仅报告新的二值选择路线与成本条件，不把该运行点采为通用Context压缩默认。

### [Scheduling the Unschedulable: Taming Black-Box LLM Inference at Scale](https://arxiv.org/html/2604.06970v1)

实际读exact-v1 §3/§4.1–4.10/§5：API客户端只有allocation、ordering和release/admit/defer/reject，不拥有provider内部抢占；p50/p90输出先验让adaptive DRR与overload分账可执行。18条低拥塞Doubao测量只校准mock线性延迟，不校准真实拥塞。Table1 class-only在若干goodput/tail单元胜coarse/oracle，Table2/5 quota或harsh有不同牺牲面，不能把full stack写普遍优势；五seed/四regime与手调阈值限于mock。6分标准仅报告这一受限控制面和设计frontier，不把模拟排序直接采为生产SLO门槛。

### [Distributed Interpretability and Control for Large Language Models](https://arxiv.org/pdf/2604.06483v1)

必要exact-v1 HTML §3–5与官方PDF p5–7已对核：latest-token activation捕获后集中projection避免逐层重复forward，但Table2仍注明“Replace dummy values with measured results”；70B/1500 token正文75±3.8秒与Table3 61.3±3.8秒不一致，不能据此采用性能宣称。Table4的8B layer35/62还需作者解释对应结构/编号，本轮不代填。中心实验主张5分深入争议隔离，不采用41×/7×或安全steering保证；重开需要清理占位表、相同配置的原始测量与一致模型/层身份，不推断全部机制不存在。

### [CubeGraph: Efficient Retrieval-Augmented Generation for Spatial and Temporal Data](https://arxiv.org/html/2604.06616v1)

实际读exact-v1 §4.1–4.4/Algorithm2–4、§5.1/§6：metadata cube内图与跨cube边提供filter-aware topology，但Algorithm4只初始标B[c0]=1，line7发现未标cube即continue，line10置1只有已标cube可到达，动态跨cube发现不可达。root已独立确认该中心反例。统一metadata等理论前提与synthetic-metadata/SIFT/MSMARCO/Deep实验不能补算法桥；predetermined分支未被此反例整体否定。6分深入争议隔离、不入Books，需作者勘误后的可执行动态算法及对应验证；本次PDF cache miss，未虚称PDF已读。

### [On the Step Length Confounding in LLM Reasoning Data Selection](https://arxiv.org/html/2604.06834v1)

实际读exact-v1 §2–4/Eq4–10/AppA.3/B：step首token与continuation的logprob贡献随step/token比例变化，均值不等纯reasoning质量；dropping丢方向选择，OLS残差并非因果识别。四teacher/四Qwen target、固定样本数量不等相同token和source预算，γ单位不可直接比较。Ch27筛选主线已真实加入boundary/方向、scorer/parser/source身份与matched-token控制，并handoffCh28 objective。root必要原文/实际三段/邻接独立通过；6分知识缺口深入，不推广headline准确率收益。

### [MirageBackdoor](https://arxiv.org/html/2604.06840v1)

实际读exact-v1 §3.1–3.2/Alg1、§4.1–4.5/Limitations：完整训练target在`<end>`后、EOS前包含辅助evaluation/reward，部署在`<end>`截断；visible CoT与训练监督不是同一对象。Qwen/Llama1.5–8B、四reasoning数据/SFT+GRPO/5～20%污染与GPT5grader仅受控协议，未证明所有monitor失效或防御不可能。Ch72 CoT-sensor主线已真实写入template/loss-mask/auxiliary-target/tokenizer/stop身份和独立outcome边界，admission是工程要求而非来源已验防御。root原文/实际正文/相邻交接独立通过；6分安全深入。

### [The Illusion of Stochasticity in LLMs](https://arxiv.org/html/2604.06543v1)

实际读exact-v1 §2–7/Table1–3，N1024的uniform/Gaussian、顺序/批生成对照：token采样不指定semantic law，history校正marginal仍引入相关与位置偏差。模拟PRNG/Box-Muller不保证精确，sandbox固定seed仅假说，p>.05不是正确概率。Ch78原有typed output与effect授权，缺真正sampler state；现已在serialization论证后写分布proposal与executor sampler、seed/counter/replay分离及低风险旧方案共存边界，root原文/实际三段独立通过。6分真实缺口深入，不称论文已部署该修复。

### [Feedback Adaptation for Retrieval-Augmented Generation](https://arxiv.org/html/2604.06647v1)

实际读exact-v1 §2–4/7–8，Llama3-8B/bge-m3、两A5000及NQ/TriviaQA/HotpotQA。更新ready lag和修正后相关query质量是两对象；snapshot和gold paraphrase不证明持续线上一致，Noise/Blank/Conflict削弱修正。Ch66反馈主线现已落实两轴与control query（工程建议），Ch77仍拥有事实状态/记忆失效；apr01对root真实正文及必要原文独立通过。6分gap深入，不采用即时可靠保证。

### [Fine-grained Approaches for Confidence Calibration of LLMs in Automated Code Revision](https://arxiv.org/html/2604.06723v1)

实际读exact-v1 §IV–VIII/TableVI–VIII，token聚合与embedding聚类calibrator分别作用于score和regime。14模型的代码修复/漏洞/重构采用static checks/EM/EditProgress，20～40%新分布数据参与超参选择，非零标签迁移或语义正确保证；BinCoverage不是风险coverage。5分标准仅报告，保留有标签局部校准的真实算法边界，不把HDBSCAN或所测code proxy采为通用门槛。

### [Improving Semantic Uncertainty Quantification in Language Model Question-Answering via Token-Level Temperature Scaling](https://arxiv.org/html/2604.07172v1)

实际读exact-v1 §3/Eq1–7、§4/5与AppA/B.3：scalar token温度改变生成law，NLI聚类后top类至多四答案any-correct是评测oracle，不等部署单答案；10样本、三8B附近模型、三短QA范围，NQ E-SC存在不胜SE反例。Ch66 Calibration Slice原论证已加生成law/聚类/选择/校准联合身份及成本，apr01原文/实际正文独立通过；6分gap深入，不外推长文factuality。

### [SwarmIO: Towards 100 Million IOPS SSD Emulation for Next-generation GPU-centric Storage Systems](https://arxiv.org/html/2604.06668v1)

实际读exact-v1 §III–VII：GPU直发I/O的central dispatch、buffer map/copy可让模拟器先饱和；service units、DSA异步批copy与全局timing state聚合避免局部quota/skew。Xeon6787P/四DSA、H200、33core/128GB模拟预算，D7-PS1010真实验证2.47MIOPS；40M目标达到38.6仍是模拟，非100M设备实测。BIGANN100M/CAGRA将memory限制2GB以模拟大索引，batch4无明显收益，不能外推生产RAG。6分标准仅报告受限emulator设计，不以关键词宣称Books已完整覆盖。

### [FP4 Explore, BF16 Train: Diffusion Reinforcement Learning via Efficient Rollout Scaling](https://arxiv.org/html/2604.06916v1)

实际读exact-v1 §3–4/效率与fidelity表，96个FP4六步探索→Top/Bottom各12 seed→BF16十步再生成24目标，八B200/LoRA及FLUX/SANA/SD3.5。rank代理失配、四步较差、量化artifact更新成本保留；IS/CLIP近似不证明每seed排序，Table6 SD3.5差−1.08%也不支持‘至多1%无损’。Ch33现Low-fidelity Exploration段已具体保存seed/ranker/precision/revision/regeneration与diffusion限定，6分标准已有覆盖，不把近似探索直接当AR训练trajectory。

### [Self-Preference Bias in Rubric-Based Evaluation of Large Language Models](https://arxiv.org/html/2604.06996v1)

实际读exact-v1 §2–4/6：IFEval规则gold与HealthBench五family judge多数参考不同，objective rubric也不免self/family bias；单criterion/allcriteria、pairwise/direct评分顺序和信息量须区分，committee降低但不消除。HealthBench参考含候选family，不是独立人类truth；rubric不在所有模式通赢。Ch66 LLM-as-Judge现有固定rubric、外部gold校准、order swap与同源correlated preference不作独立证据，5分标准已有覆盖。

### [Robustness Risk of Conversational Retrieval: Identifying and Mitigating Noise Sensitivity in Qwen3-Embedding Model](https://arxiv.org/html/2604.06176v1)

已读exact-v1 §§2–4/6，0～15%独立模板噪声、LongMemEval与LoCoMo、Qwen/GTE/Stella及packing/query-prompt对照表明非语义噪声也可能进入高位。Prompting的收益依encoder训练身份，GTE-Qwen1.5反例保留；NDCG不是最终QA truth，训练语料成因仅假说。Ch76已有query dialect、corpus/index/packing/outcome联合验收，Ch77拥有memory unit；本项作为受限接口分布反证，不新增重复正文。

### [LLM Spirals of Delusion: A Benchmarking Audit Study of AI Chatbot Interfaces](https://arxiv.org/html/2604.06188v1)

已读exact-v1 §§4–6：14seed×4interface共56段20turn、模拟KimiK2用户、两RA与固定GPT grader，CHAT temporary和OpenRouter API及时间比较。均值不保留turn演化，接口差异不能单归因weight/policy；有限主题、模拟用户未真人校准、中等一致性不支持真实风险发生率。安全评价反证触发5分深入例外；Ch66已冻结access path/system prompt/provider/time身份，不据此重排安全能力。

### [Probabilistic Language Tries: A Unified Framework for Compression, Decision Policies, and Execution Reuse](https://arxiv.org/html/2604.06228v1)

已读exact-v1 §5.1/5.3/5.4/7，stationary真实先验、相同读/算成本和确定artifact是原理论条件。Lemma2 coupon等待和Markov下尾方向有反例：K2、p(.8,.15,.05)、T3满足前提却P(Tswap>3)=.622<.775，Theorem1桥失效；root已独立核。深入后理论争议安全隔离，需勘误/正确假设和证明，不写Ch45正面定理；不由此否定缓存先验一般可能有用。

### [The Art of Building Verifiers for Computer Use Agents](https://arxiv.org/html/2604.06240v1)

已读exact-v1 §3.1–3.5/Algorithm1、§5label协议与§6对照。只从task建立rubric以避免trajectory倒造标准，conditional未触发不当fail，upstream cascade不能反复记独立错误；process credit不改outcome失败。所有截图×criteria先relevance再per-criterion topK，不等全截图完整精读。140内部+106外部Fara7B、UV-blind/informed label不同，FPR.01/.08不外推近零。Ch66原有泛rubric formation/dependency，缺task-only冻结、条件适用分母与cascade具体接口；root已在formation段内落实，apr01原文/实际正文独立核通过。

### [ZitPit: Consumer-Side Admission Control for Agentic Software Intake](https://arxiv.org/html/2604.06241v1)

已读exact-v1 III–VI与实现状态：artifact首次fetch/unpack/build/test/run前durable policy event，hash/provenance/capability/context/expiry绑定，mandatory mediation/transitive closure是保证前提。Git五repo已有实现，npm/PyPI/raw installer多处Planned，Rust partial；ls-remote中位时间不是clone SLO。Ch72已有artifact接触数据前provenance/sandbox/egress和模型外effect授权；5分安全override深入，未把成熟原语组合写成新安全保证。

### [RAGEN-2: Reasoning Collapse in Agentic RL](https://arxiv.org/html/2604.06268v1)

root实际读exact-v1 §§2.2–3.3/4–5.2并与Ch33关键诊断指标对照。top-p是累计RV mass，不是固定prompt比例；H(Z|X)与I(X;Z)的条件对象分离，retrieval proxy非faithfulness，filtered objective/bias须再准入。80～100%环境噪声优势消失、FrozenLake GRPO−5pp及selection confound保留，不采用完整因果链或MI两倍可靠。实际已有相同命题，不重复写书。

### [FedSpy-LLM: Towards Scalable and Generalizable Data Reconstruction Attacks from Gradients on LLMs](https://arxiv.org/pdf/2604.06297v1)

已读exact-v1 §III–V/AppendixA-A，root独立核官方PDF p4/p14。聚合前单client梯度/global model、冻结embedding/position、不考虑secure aggregation是威胁边界。G=Zᵀδ低秩只能colG⊆colZᵀ，不能反推输入在colG：Zᵀ=I₂、δ=e₁的G=e₁不能含e₂；Eq21矩阵次序也未补桥。中心保证深入后争议隔离，经验攻击仍可按披露范围记录，不声称攻击不存在。

### [Discrete Flow Matching Policy Optimization](https://arxiv.org/html/2604.06491v1)

实际读exact-v1 §§3–4.3/5/7/8。合法Euler step把CTMC rate转一步transition policy，以(t,x_t)为state、下一x为action和终态reward，logprob/ratio可算而终态marginal不可算；这不是AR logprob或无离散误差。trajectory KL与terminal TV对象不同。DNA/HepG2/200bp/约70万序列、分开reward oracle只是评价，不恢复AI-for-Science应用，也不推LLM有效性。通用机制恢复为6分候选，Ch24 guidance段后已实际补入一步policy→inner MDP的缺口，apr01原文/正文独立核通过；PPO/GRPO更新仍归Training，不重复算法。

### [The Detection-Extraction Gap: Models Know the Answer Before They Can Say It](https://arxiv.org/pdf/2604.06613v1)

官方HTML/v1含Aug24正文日期，故采用官方PDF v1实际p2§3.1–3.2、p5§4.4、p6–7§4.5/AppB。自由续写PSC与forced suffix EFA是不同读出，gold判recoverability不是内部已知；full-T位置oracle/heldout θ与总probe token成本不能省略。root已在Ch66原论证实际写入‘推理早停要区分可恢复性与强制读出’，apr03必要PDF/正文独立通过。只采用行为对象和成本边界，不继承污染HTML后版结论。

### [STQuant: Spatio-Temporal Adaptive Framework for Optimizer Quantization in Large Multimodal Model Training](https://arxiv.org/html/2604.06836v1)

root必要exact-v1方法/评价已审，apr03独立HTML §3.2–3.5/Algorithm1/Table4与Ch39写后核。按layer/state/time统计提议精度，rank-local量化尺度与globalEMA、moment状态线性/对数路径及转换成本不能混为learning rate；去Spatial位宽升/PPL降是容量质量取舍。真实正文在分片/低比特状态主线，6分实际缺口深入，不采用万亿规模/近最优生产保证；PDF cache miss未假称已读。

### [MARS: Enabling Autoregressive Models Multi-Token Generation](https://arxiv.org/pdf/2604.07023v1)

root与apr03实际PDF v1 §3/4.5/Limitations/AppA核：clean stream/causal mask/right shift，masked-block继续训练和左至右连续accept/cache同步。单token是新checkpoint AR，不保持原权重分布；same epoch不等compute-matched，多token质量损失和batch/cache慢例保留。Ch24已实际嵌入因果masked-block路线，非章末paperappend，6分缺口深入、写后通过。

### [Information as Structural Alignment: A Dynamical Theory of Continual Learning](https://arxiv.org/html/2604.07108v1)

实际读exact-v1 §3.3/4.1–4.4/5.4/7.3/8。frozen encoder/evaluator上Gaussian粒子存位置/幅值/bandwidth/context/decay，局部收敛降低decay、持续矛盾重启；跨context只有已稳定且验证粒子可读。它是外部prediction correction不是shared-weight SGD。CIFAR strongprior .901而完整修正.892、kernel-only足且复杂机制冗余，companion Mistral不算本篇完整验证。不因小模型硬拒；局部correction生命周期是新算法，但CIFAR对照不能支持复杂controller必要性，Mistral只在companion，故仅报告而不采为Agent memory设计，不称全局无遗忘。

### [InfiniLoRA: Disaggregated Multi-LoRA Serving for Large Language Models](https://arxiv.org/pdf/2604.07173v1)

root/apr03实际PDF v1 footnote1、§3–5/6.3/6.4与Ch52对读：base/KV和remote adapter算子分开，activation往返、GPU RDMA与rank预算是新执行状态边界。作者TTFT只decode-first-token、不含prefill，IAR≥95%不等通用P95，同总GPU减少base instances/朴素分离尾延迟变坏/cache饱和均保留。实际正文已在adapter远程执行主线，6分缺口深入、写后通过。

### [Generalization error bounds for two-layer neural networks with Lipschitz loss function](https://arxiv.org/html/2604.06281v1)

已读exact-v1 Assumption1、§3moments、§4/5 bounds。bounded support、smooth1-Lipschitz loss/activation、regularized两层SGM/He/LR范围下，independent test给n^-1/2，dependent样本Wasserstein给n^-1/(din+dout)；dimension-free仅指数，constant仍维度/宽度/T/norm，joint constant-LR可爆炸。理论主线候选5分标准，不以缺Transformer实验排除，也不外推其泛化率。与Ch5泛化/优化命题对读后，仅报告本法数学条件，不把新条件性定理外推现代Transformer；这不是已有完全覆盖，也不是无贡献。

### [SALLIE: Safeguarding Against Latent Language & Image Exploits](https://arxiv.org/html/2604.06247v1)

实际读exact-v1 §§3–4/5.1–5.2/6，核官方PDF首页标题，不采用后版DataCite标题。last-token各层残差、可选PCA/cosine kNN及层平均形成guard；Gemma3-4B/Phi3.5/SmolVLM2-2.2B与所测文本/视觉集合的val阈值不能变成开放世界FPR保证。文本baseline看视觉样本时只有伴随文字，信息预算不等；仅不同子集的PI不是独立攻击族。Ch72已有按模型/层/token/suffix/normalization/校准集绑定白盒probe，且probe不拥有effect授权，具体既有覆盖，5分标准完成。

### [Say Something Else: Rethinking Contextual Privacy as Information Sufficiency](https://arxiv.org/html/2604.06409v1)

实际读exact-v1 §§3/4.1–4.4、limitations/ethical scope。可置信属性替换须跨turn保持同一alternative，不能只逐次redact；493 PrivacyLens生成792情境、7模型/22,176段与非对抗DeepSeek3.2 simulator/judge，不代表真实外部攻击或真人效用。ISAD结合HLS与utility不是DP，covertness关联不是因果，peer场景替换得分也低于suppression。主张仅用户自身属性且排除医疗/法律/安全真值需求，与Appendix第三方细节不一致的范围保留；6分安全深入仅报告，未将造假策略写入隐私规范。

### [When to Call an Apple Red: Humans Follow Introspective Rules, VLMs Don't](https://arxiv.org/html/2604.06422v1)

实际读exact-v1 §§3–4.3/AppA.3：控制颜色比例、world prior/counterfactual与形状，分别问声明阈值、独立感知比例和最终类别。4个VLM、4个CoT及173人/37profile/3003variant只支持所测行为；SEM一致不等忠实，估计准确不证明相同表征实际控制decision，提问次序亦影响阈值。Ch66 forecaster段后已经root窄写三对象分账与prompt-order成本，apr01原文/正文/邻接独立核通过；6分实际缺口深入，不声称内部知道却撒谎。

### [Babbling Suppression: Making LLMs Greener One Token at a Time](https://arxiv.org/html/2604.06755v1)

实际读exact-v1 §4/Algorithm1、§5.1–5.3、§6/Tables1–3与§7。newline/function边界parse→compile/type→known tests→stop，依赖已有测试/依赖/timeout，不证明完整正确。单A10 24GB、NVML10Hz、temperature.1/top-p.95/上限1000的HumanEval短输出例中，QwenCoder7B 120→118token但GPU能量625→672、CodeGemma99→93但640→695；CPU校验未计，§5.3无干扰与§7不能独占GPU矛盾不消除。Ch70 goal/device-host之后已实际写净break-even、失败/超时和短基线反例，apr01独立核通过；6分反证深入，不推广35%/29%headline。

必要证据完整位置与具体反例见[V3证据笔记](../_sources/daily-20260409/V3_EVIDENCE_NOTES.md)，实际写后独立审阅见[非作者记录](../_sources/daily-20260409/V3_WRITEBACK_INDEPENDENT_AUDIT.md)。未取得/未运行artifact不冒充复现。

## 5. 缺口与下一步

可执行普通工作：无。来源停止范围、有限工作信号、必要证据、实际Books判断与非作者日级复核已收口。最终81=24整合+10已有覆盖+39仅报告+8争议；每个恢复候选只审足以支撑命题的方法/评价/直接限制，没有展开全部562全文。以下外部限制及争议均为终态保留项，不支持正面证据、Books或无遗漏断言；定点重开条件逐项列出。

87初始工作信号与本表差集：06182在必要方法对照后，不能把joint稳定性与环境hardness叫独立能力因果诊断，具体前分母关闭；07345/06291/06436/06652/07026/07277为下述六日期例外；06425/06820/06779为三个版本必要材料例外。表中另有06491/07108/06281/06812四个反向复核恢复家族，87−1−6−3+4=81；数字只是终态对账，不是候选配额或全部原始论文深审声明。

06779原始库存题摘为VASR systematic offspring allocation；当前[官方abs/v1](https://arxiv.org/abs/2604.06779v1)及[HTML/v1](https://arxiv.org/html/2604.06779v1)为FVD Fleming–Viot birth–death/rebirth noise，中心机制与旧题摘不同。本轮PDF工具未取得，不虚报PDF已读，也不据可读HTML地址v1就采用原April结论；需要能绑定原April版本的作者稿/官方正文或作者明确版本说明，随后仅重开本家族身份与必要方法。不查全部发表史，不评分或写Books。

06820库存题摘为290文章/317人、直接risk prediction与direct sharing比较；当前[官方HTML/v1](https://arxiv.org/html/2604.06820v1)和本轮已读[PDF/v1](https://arxiv.org/pdf/2604.06820v1)为290文章/392人/2043 paired ratings、judge–human proxy-validity主张。当前版本可读不证明旧April评价对象已恢复；原April必要方法/样本及绑定说明到达才定点重开，当前不据两套不同协议评分或整合。

06425 [Neural Computers原始v1](https://arxiv.org/pdf/2604.06425v1)必要正文未恢复：HTML/v1正文标2026-08-24，官方PDF网页失败且有界下载/续传均未完成、实际解析EOF错误，不能声称已读。原始v1的必要方法/评价或作者明确版本材料到达才定点重开；本次不评分、不采用后稿的正面CNC结论，不把局部临时文件当证据。

本窗已隔离外部保留：06291 v1Updated=`2026-04-14T01:06:02Z`、06652=`2026-08-07T00:03:34Z`不能支撑本窗可用上界；07277=`2026-04-09T01:00:47Z`、07345=`01:04:10Z`跨截点；06436版本日期污染待定点恢复。此字段不证明真实首发一定晚，恢复需精确官方首公告/正文可用上界或可核组合证据；不据它们评分/写Books。07026 CMS04-07T16Z可能早于arXiv提交，早发正文未证实时保留精确日期例外，不以CMS孤证定owner。

Meta MuseSpark/Build-Test两页仅April8无时区，未证明本窗，必要原文线索隔离；官方带时区发布时间或可核早发记录到达时仅重开家族。OpenAI历史Research/Index、Google Publications、Meta Research/Publications、Moonshot历史目录、MiMo无日戳Blog和MiniMax undated TechBlog按§2实际限制隔离，不用于全源零命中；可覆盖本窗的原始历史索引/日期正文到达才定点重开。

八项中心主张争议均不支持正面Books或保证，必要反例和有限经验分别保留在§4：06228需修正coupon等待/下尾桥；06297 FedSpy需完整列空间条件和正确矩阵推导；06483需清除占位实测表并统一模型层/时间配置；06616 CubeGraph需可达的跨cube发现控制流与相应实验；06413需限定conditional endpoint mean与coupling的等价条件；06695需合法mass域或clamp与对应算法；06777需建立variance假设与实际reward/gradient/sampling实现的桥；06812需解释质量加权平均抵消与clustering消融变化之间的公式/实现差异。作者勘误或足够的同版本证明、实现及测量到达时只重开对应家族；不因一个理论反例宣布全部经验结果失效。

## 6. 复核

复核者：root（原报告作者apr01之外的审阅者）；apr03复核四项早期实际Books及新增AGSC公式反证。root新增AGSC不是自验，其最小证明由apr03独立检查。

结论：通过

实际核14来源入口及停止范围、组合日期与具名例外、81项最终处置及必要证据、24项真实机制正文与相邻衔接、10项具体已有论点。沿用已核且未变的单篇证据，最终补读八项Only的核心方法/评价/限制；修正Grounded Forcing“global永不淘汰”的过强说法。否定侧在首批24题摘校准与前批定点恢复之外，另抽核12个完整题摘：06277/06285/06367/06550/06633/06693/06729/06787/06812/06833/07035/07230，覆盖校准/安全/工具/表示/效率及“既有组合、领域应用、新工作点”理由。恢复06812为5分中心公式争议，apr03独立确认Eq11–13恒等与Table2缺桥；其余抽样关闭保留具体理由。本抽检不是189项否定侧全量独立验证，未抽部分不声称无遗漏；共享旧模板已由作者逐家族改判且发现的受影响项定点恢复。普通待办为0，外部保留项仍严格隔离。格式、链接与限定范围diff检查只证明一致性，不代替本次语义验收。
