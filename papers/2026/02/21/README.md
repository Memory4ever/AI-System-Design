# Daily Research — 2026-02-21

**规范：** V3
**窗口：** 2026-02-20T09:00:00+08:00 ～ 2026-02-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-05T22:36:54+08:00

## 1. 结论

本日有限发现与贡献判断已结束，确认落窗的116个唯一材料家族均完成必要审阅与安全终态处置，root非作者最终日级独立验收已通过。长期增量集中在监督与评分对象的分责、在线反馈/执行状态的有效条件，以及多模态与校准接口的取舍：例如部分相关标签跨比较对改变正负角色、弱/强验证必须保留随机反馈、diffusion剪枝校准须绑定noise/time。原方案在其约束下继续成立；proxy、局部收益、谱/曲率或作者保证都不自动升级为truth、端到端性能或执行权限。

116家族中74项实际融入唯一Books owner并已获74处正文/完整邻接/自身末注非作者POST；15项有具体已有覆盖，3项仅报告，24项中心争议安全隔离。后24项不计正面Evidence或Books保证。八批164份完整题摘的最终互斥路由为116当窗候选＋38准入前排除（37具体贡献关闭、1旧首公开窗外）＋9日期保留＋1官方移除/合法原源保留，普通待办0、once未决0。481库存身份只作有界标题查漏，不是481当窗论文、候选或全文队列；旧V2.1/Weekly分母和完成标签未继承。日期、访问及历史目录保留项不用于正面采用或无遗漏断言。

## 2. 来源覆盖

下列为实际有限停点，不是完整历史目录或全网零遗漏断言；检查执行于本次2026-10-05补跑，详见[本日停点](../_sources/daily-20260221/V3_SCREENING.md)。只扫描每日来源与本日真实证据触发，不扫描每周组。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research当前入口与限定Feb20原站查询；First Proof正文已读，官方标Feb20但先前attempts为Feb14；定点原HTML一次403 | 受阻 | 当前新增appendix/纠错的精确事件时间无法恢复，终态隔离，不采用其候选/Books或无遗漏断言；恢复须原始发布/更新时区字段，不扩数学发现 |
| SRC-ANTHROPIC | Research当前前10项及限定Feb20原站查询；Claude Code Security核心正文全段及原HTML published_time/datePublished/timeDateTime均读，2026-02-20T17:59Z落窗 | 已检查 | preview的dataflow/selfverify/human approval未新增公开机制/成立条件，贡献EX经root独核；不把先前500漏洞归该preview或授安全保证；有限历史目录不支持无遗漏 |
| SRC-GOOGLE-AI | DeepMind research/blog与Google Research publications首个返回页，限定窗口主题查询 | 已检查 | 有限当前页不能恢复完整Feb20历史；该缺段不支持零命中保证 |
| SRC-META-AI | 官方Research空提取，有限日期/域名主题补检无相关命中 | 受阻 | 未恢复原生历史目录；只隔离覆盖断言，不阻塞其他正文 |
| SRC-QWEN | qwenlm官方旧入口转qwen.ai/blog；动态HTML、原站p_layout及80126a68.js定点恢复；前者只有/api/v2/article拦截字面，后者92511 chars无article/route协议 | 受阻 | 未恢复历史Blog原生查询协议，不猜API参数，不把空页面作无事件；终态隔离覆盖断言，恢复须官方可读历史列表或已披露API协议 |
| SRC-DEEPSEEK | 原站Research Index从Jun24、Feb25、Jan28、Jan12到旧条目；新闻当前前5项 | 已检查 | 有限Research原生列表未见本窗相关条目；News历史列表未完整恢复 |
| SRC-MOONSHOT | Platform Blog当前有限列表至Nov2025及日期主题补检 | 已检查 | 当前Blog不提供本窗完整历史，未据此证明无事件 |
| SRC-TENCENT-HUNYUAN | 动态网页空提取后两次实际浏览器调用失败；原站JS恢复publicList原生API，[all9元数据](../_sources/daily-20260221/V3_NATIVE_HUNYUAN_LIST.json)已读，Feb13/Feb3与后续Apr23夹窗 | 已检查 | 当前目录all9不证明历史目录未删漏；浏览器本身未通过 |
| SRC-ZAI | 官方Research有限列表Aug→Mar15→Feb21GLM-5 report→Feb11/Feb2→旧项；定点恢复GLM-5 exact-v1 arXiv2602.15763，同IDRegistered为2026-02-18T02:49:09Z | 已检查 | paper公开上界Feb18 BJT10:49:10已早于窗，Feb21目录收录不移动归属；有限当前列表不证明完整历史 |
| SRC-BYTEDANCE-SEED | 原站API paper2026 offset0返回18/82，offset60返回19项Feb26→Jan26夹窗；blog2026 offset0返回14/19且has_more=false，localeUS；[边界页](../_sources/daily-20260221/V3_NATIVE_SEED_PAPER_OFFSET60.json)、[Blog页](../_sources/daily-20260221/V3_NATIVE_SEED_BLOG_OFFSET0.json) | 已检查 | 未称全82/19逐项读取；locale返回数与total不同，原生当前列表不保证历史无遗漏 |
| SRC-BAIDU-ERNIE | 官方中文Blog第一页10项May9→Feb6→Jan→Nov，第二页为更旧方向 | 已检查 | 有限第一页时间夹窗未见相关事件，不代表所有历史发布完整 |
| SRC-XIAOMI-MIMO | 原站Paper8项Jun29→Mar13→Feb3→Jan8→2025；Blog15可见标题无日期 | 已检查 | Blog历史日期无法恢复，不从Paper无命中推Blog无事件 |
| SRC-MINIMAX | 英文Blog12、中文13当前条目，Feb14/Feb12到Jan条目；Agent Tech Blog只有导航 | 已检查 | 英中同家族发布日期不同均早于窗；Agent技术目录历史正文缺段隔离 |
| SRC-ARXIV | 本日481库存标题有界查漏；范围相关164完整题摘按原文增量校准；四组日期/ROADMAP主题查询及cs.LG月公告入口404后停止扩扫；拟项定点actual abs/v1、必要正文与same-ID DataCite | 受阻 | 有限发现已停止、普通待办0；116确认落窗/38排除/9日期/1合法原源保留已归并。原批公告不可恢复，不能称481均本窗、全分类召回或完整历史无遗漏；恢复需官方批次公开列表，仅重开受影响身份 |
| 表外：[arXiv日期流程](https://info.arxiv.org/help/availability.html) | [官方DOI说明](https://blog.arxiv.org/2022/02/17/new-arxiv-articles-are-now-automatically-assigned-dois/)与[DataCite](https://api.datacite.org/)实际读finalID/DOI仅公告后提供、公告schedule、预计公告后24h获DOI；定点同IDRegistered上界 | 已检查 | 24h是预计不是保证；Registered不是精确公告时刻，Created不作为公开日期 |

## 3. 候选与判断

以下冻结116个通过贡献筛选且确认落窗的唯一v1家族；公开区间是基于官方公告流程与same-ID Registered上界的有界推定，含起不含末，不冒充精确公告时刻。38准入前排除、9日期保留及1官方移除/合法原源保留不混入此分母，逐ID依据保留在本日筛选记录。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Omitted Variable Bias in Language Models Under Distribution Shift](https://arxiv.org/abs/2602.16784v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:35:32+08:00 | 可见表示的shift校正仍漏隐藏协变量→以不可识别敏感性假设限制目标性能推断；2+1+2=5 | 争议 | 暂缓：中心公式统一前不进入Books；泛化分布假设已在Ch66承载，不以缩成成熟原则强行整合 |
| [References Improve LLM Alignment in Non-Verifiable Domains](https://arxiv.org/abs/2602.16802v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:35:58+08:00 | 无外部核验的自判偏好易失准→独立强参考答案辅助比较，并与DPO reference policy分权；2+2+2=6 | 深入完成 | 整合：TRAIN-DPO [Ch34](../../../../books/part-04-training-system/34-dpo.md#dpo-保留了什么难题)，reference answer与reference policy分权单段 |
| [Simple Baselines are Competitive with Code Evolution](https://arxiv.org/abs/2602.16805v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:02+08:00 | 复杂搜索validation胜出可能是随机赢家噪声→独立fresh重测与cheap/filter/high-budget cascade；2+2+2=6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) procedure-level winner'scurse；AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) cheap cascade/stochastic/search-overfit为依赖，不制造重复整合 |
| [One-step Language Modeling via Continuous Denoising](https://arxiv.org/abs/2602.16813v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:13+08:00 | 连续one-hot解码信息集中在终段→decode-error时间重参数化，冻结teacher/校正再单模型压缩少步；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#并行与少步生成必须声明依赖轨迹和状态边界)，组合一致性后窄单段 |
| [Hybrid-Gym: Training Coding Agents to Generalize Across Tasks](https://arxiv.org/abs/2602.16819v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:22+08:00 | 同harness不保证patch→message-action迁移，联合stitch改变监督接口；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，teacher轨迹之后 |
| [Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees](https://arxiv.org/abs/2602.16823v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:28+08:00 | 连续输入域双输入reachable patch规格，sound验证不等全因果；2+1+2=5 | 深入完成 | 整合：WORLDVIEW-REPRESENTATION [Ch5](../../../../books/part-01-worldview/05-what-neural-networks-learn.md)，Faithfulness Budget之后 |
| [Learning under noisy supervision is governed by a feedback-truth gap](https://arxiv.org/abs/2602.16829v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:37+08:00 | 快监督/慢真值gap与容量/噪声取舍，但小gap不等准确率高；2+1+2=5 | 争议 | 暂缓：中心隔离，NN局部仅报告，不扩human/EEG |
| [VAM: Verbalized Action Masking for Controllable Exploration in RL Post-Training — A Chess Case Study](https://arxiv.org/abs/2602.16833v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:43+08:00 | 迭代allowed-set改变每组policy条件，prompt列表非硬mask；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，同条件组采样之后 |
| [NeST: Neuron Selective Tuning for LLM Safety](https://arxiv.org/abs/2602.16835v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:45+08:00 | selected FFN行按cluster共享线性增量再fold；2+1+2=5 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，共享基之后 |
| [A Residual-Aware Theory of Position Bias in Transformers](https://arxiv.org/abs/2602.16837v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:48+08:00 | mean-kernel/residual-weight是position影响代理，不等真实动力学；2+1+2=5 | 争议 | 暂缓：中心collapse iff隔离，有限kernel仅报告 |
| [Training Large Reasoning Models Efficiently via Progressive Thought Encoding](https://arxiv.org/abs/2602.16839v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:51+08:00 | evicted-KV经forward写state并产生动态低秩权重；2+2+2=6 | 深入完成 | 整合：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，梯度式历史压缩之后 |
| [AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence](https://arxiv.org/abs/2602.16873v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:37:39+08:00 | adaptive路由有局部潜力，width法则遭反例；2+2+2=6 | 争议 | 暂缓：中心law/最优/精确性能隔离 |
| [OpenSage: Self-programming Agent Generation Engine](https://arxiv.org/abs/2602.16891v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:38:05+08:00 | metadata/clone/archive三个生命周期分责；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，有界fan-out之后 |
| [Overseeing Agents Without Constant Oversight: Challenges and Opportunities](https://arxiv.org/abs/2602.16844v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:36:58+08:00 | trace界面更快/更confident不等独立验错收益；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，Human-Agent邻接 |
| [On the Mechanism and Dynamics of Modular Addition: Fourier Features, Lottery Ticket, and Grokking](https://arxiv.org/abs/2602.16849v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:37:05+08:00 | 两层NN相位/频率竞争，但中心定义/输出系数矛盾；2+1+2=5 | 争议 | 暂缓：中心隔离，局部小模型仅报告 |
| [DODO: Discrete OCR Diffusion Models](https://arxiv.org/abs/2602.16872v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:37:38+08:00 | prefix token≠hidden冻结；block-causal训练使KV合法而有质量代价；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，Block/cache邻接 |
| [AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks](https://arxiv.org/abs/2602.16901v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:38:19+08:00 | 多轮adaptive attack/profile与预算联合改变安全测量人口；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) risk(N)/turn-frontier/profile；AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md) accepted不等truth依赖 |
| [LLM-WikiRace: Benchmarking Long-term Planning and Reasoning over Real-World Knowledge Graphs](https://arxiv.org/abs/2602.16902v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:38:20+08:00 | loop发生/条件恢复/停滞分母不同，oracle菜单改变action support；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，cycle节L823 |
| [Narrow fine-tuning erodes safety alignment in vision-language agents](https://arxiv.org/abs/2602.16931v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:01+08:00 | 窄LoRA安全退化与geometry/protocol混杂需拆开；2+1+2=5 | 深入完成 | 仅报告：单Gemma/不配对人口与activation SVD不支持新增普遍安全机制，具体边界已覆盖 |
| [DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs](https://arxiv.org/abs/2602.16935v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:07+08:00 | learned历史state与当前embedding旁路分工，安全sensor不取得authority；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，L605已写，实际POST通过 |
| [Heterogeneous Federated Fine-Tuning with Parallel One-Rank Adaptation](https://arxiv.org/abs/2602.16936v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:08+08:00 | fold未选秩一项保初始全局函数，却只训练局部支集；不授错聚合界；2+2+2=6 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，L622已写，实际POST通过 |
| [Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents](https://arxiv.org/abs/2602.16943v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:19+08:00 | 零调用人口与proposal/enforcement/final分账限制文本安全外推；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，L2011已写，实际POST通过 |
| [In-Context Learning in Linear vs. Quadratic Attention Models: An Empirical Study on Regression Tasks](https://arxiv.org/abs/2602.17171v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:44:46+08:00 | 小高斯线性任务的softmax必要性反側，不同训练预算不识别架构速度；2+1+2=5 | 标准完成 | 仅报告：局部反证有价值，但不改变现有ICL行为/算法与kernel条件解释 |
| [MeGU: Machine-Guided Unlearning with Target Feature Disentanglement](https://arxiv.org/abs/2602.17088v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:42:44+08:00 | 类别共享表示下重标签/feature noise的选择改变forget与retain取舍；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，L358已写，实际POST通过 |
| [A Data-Driven Dynamic Execution Orchestration Architecture](https://arxiv.org/abs/2602.17119v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:43:32+08:00 | row-window FSM把有效scratch容量与稀疏执行控制绑定；2+2+2=6 | 深入完成 | 整合：INFER-GPU-MEMORY [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md)，L614已写，实际POST通过 |
| [TimeOmni-VL: Unified Models for Time Series Understanding and Generation](https://arxiv.org/abs/2602.17149v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:44:14+08:00 | finite canvas的变量/周期/长度容量和反归一化metadata改变codec接口；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，L48已写，实际POST通过 |
| [LLM4Cov: Execution-Aware Agentic Learning for High-coverage Testbench Generation](https://arxiv.org/abs/2602.16953v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:33+08:00 | student-induced困难状态优先级把慢反馈预算用于恢复监督；2+2+2=6 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，L160已写，实际POST通过 |
| [Automating Agent Hijacking via Structural Template Injection](https://arxiv.org/abs/2602.16958v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:40+08:00 | 伪tool结束/assistant/user历史利用模板先验→数据结构与runtime角色分权；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#prompt-injection-与-tool-boundary)，模板伪历史有限边界，实际POST通过 |
| [Greedy Multi-Path Block Verification for Faster Decoding in Speculative Sampling](https://arxiv.org/abs/2602.16961v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:44+08:00 | 多IID草稿选中path改变proposal→q^Γ身份与严格排序需共同验证；2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)，选后分布窄段，中心tie recipe隔离，实际POST通过 |
| [Early-Warning Signals of Grokking via Loss-Landscape Geometry](https://arxiv.org/abs/2602.16967v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:52+08:00 | 非交换probe/投影干预并不建立通用必要性或在线预警；2+1+2=5 | 争议 | 暂缓：SGD probe≠实际AdamW状态，全轨迹PCA/仍grok反例隔离中心，局部报告不改Books |
| [DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.16968v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:39:54+08:00 | guidance尺度≠token网格→多patch资产蒸馏与每step全局执行形状；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，guidance后单段，实际POST通过 |
| [Beyond Chunk-Then-Embed: A Comprehensive Taxonomy and Evaluation of Document Chunking Strategies for Information Retrieval](https://arxiv.org/abs/2602.16974v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:40:02+08:00 | pre/post编码切分的平均收益随同/跨文档竞争人口反转；2+2+2=6 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md#offline-ingestion-不是预处理细节)，ingestion身份后一段，实际POST通过 |
| [Fail-Closed Alignment for Large Language Models](https://arxiv.org/abs/2602.16977v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:40:07+08:00 | 静态单方向易复用→逐轮累计span移除改变拒答训练支持域；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md#refusal-behavior-不等于危险知识已经删除)，refusal限制后单段，实际POST通过 |
| [Discovering Universal Activation Directions for PII Leakage in Language Models](https://arxiv.org/abs/2602.16980v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:40:11+08:00 | 白箱自生PII类别方向提供提取proposal，独立secret matching才验泄漏；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际POST通过 |
| [Fundamental Limits of Black-Box Safety Evaluation: Information-Theoretic and Computational Barriers from Latent Context Conditioning](https://arxiv.org/abs/2602.16984v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:40:17+08:00 | adaptive任意查询条件与有限hash构造下界冲突；2+2+2=6 | 争议 | 暂缓：中心adaptive保证隔离，不写Books |
| [Dynamic Delayed Tree Expansion For Improved Multi-Path Speculative Decoding](https://arxiv.org/abs/2602.16994v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:40:30+08:00 | 共享trunk后fork改变选形与feature可取时点；2+2+2=6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md)，实际POST通过 |
| [Arcee Trinity Large Technical Report](https://arxiv.org/abs/2602.17004v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:40:45+08:00 | 仅SMEBU幅度反馈/tanh/center/EMA改变expert bias动态；2+2+2=6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)，实际POST通过 |
| [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](https://arxiv.org/abs/2602.17025v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:15+08:00 | outcome-pair向prefix reward转移，原preferred role/长度罚/聚合接口冲突；2+2+2=6 | 争议 | 暂缓：中心recipe隔离，不作在线stop/逐step信用保证 |
| [Wink: Recovering from Misbehaviors in Coding Agents](https://arxiv.org/abs/2602.17037v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:31+08:00 | nonblocking observer的snapshot与ready后提醒交付是两个时点；2+2+2=6 | 深入完成 | 整合：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)，实际POST通过 |
| [Phase-Aware Mixture of Experts for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.17038v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:33+08:00 | learned expert-run与workflow显式phase不同，历史/STE改变路由条件；2+2+2=6 | 深入完成 | 整合：MODEL-MOE [Ch21](../../../../books/part-02-model/21-moe.md)，原两段纠正且实际POST通过 |
| [Amber-Image: Efficient Compression of Large-Scale Diffusion Transformers](https://arxiv.org/abs/2602.17047v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:46+08:00 | 删层/stream改变需cluster-end与concat teacher targets分阶段恢复；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，实际POST通过 |
| [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models](https://arxiv.org/abs/2602.17053v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:54+08:00 | contrast筛选使valid人口随模型变化，组件judge不授隐藏忠实性；2+2+2=6 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际POST通过 |
| [Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression](https://arxiv.org/abs/2602.17063v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:42:08+08:00 | 可重生sign需初始化/硬投影支持，幅度codec与全费用分开；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，实际POST通过 |
| [Predictive Batch Scheduling: Accelerating Language Model Training Through Loss-Aware Sample Prioritization](https://arxiv.org/abs/2602.17066v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:42:12+08:00 | 已发生per-sample loss拟合cheap predictor后改变采样q；2+1+2=5 | 深入完成 | 整合：TRAIN-DATA [Ch27](../../../../books/part-04-training-system/27-data.md)，实际POST通过 |
| [Adam Improves Muon: Adaptive Moment Estimation with Orthogonalized Momentum](https://arxiv.org/abs/2602.17080v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:42:32+08:00 | Orth后scalar/column统计改变状态维度与几何，decay联合变化；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，实际POST通过 |

| [FLoRG: Federated Fine-tuning with Low-rank Gram Matrices and Procrustes Alignment](https://arxiv.org/abs/2602.17095v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:42:54+08:00 | 聚合Gram秩增与固定客户端秩对齐接口冲突；2+2+2=6 | 争议 | 暂缓：r′>r 时 SᵀS=I 不可行，中心zero-error不授，有限经验仅报告 |
| [AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing](https://arxiv.org/abs/2602.17097v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:42:57+08:00 | 跨回合history/target独立噪声训练支持区别同clock与clean copy；2+2+2=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，L248实际POST通过 |
| [AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation](https://arxiv.org/abs/2602.17100v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:43:01+08:00 | graph作为policy行动，execution feedback共同history后重提案；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，L872实际POST通过 |
| [VP-VAE: Rethinking Vector Quantization via Adaptive Vector Perturbation](https://arxiv.org/abs/2602.17133v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:43:52+08:00 | 无码本扰动训练→离线Kmeans部署分工，不授实际quant误差支集保证；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，L194实际POST通过 |
| [Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization](https://arxiv.org/abs/2602.17155v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:44:23+08:00 | 子空间estimate→orth→lift及query/resample身份；2+2+2=6 | 深入完成 | 整合：TRAIN-PRETRAINING [Ch28](../../../../books/part-04-training-system/28-pretraining.md)，L335实际POST通过 |
| [BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning](https://arxiv.org/abs/2602.17168v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:44:42+08:00 | 局部loss稳定界没有ASR桥，角度≥0含零不足给单调；2+2+2=6 | 争议 | 暂缓：中心保证隔离，有限clean-ft残留仅报告，已有安全原则不强写 |

| [When LLM Judges Inflate Scores: Exploring Overrating in Relevance Assessment](https://arxiv.org/abs/2602.17170v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:44:45+08:00 | 评分协议/输入改写改变judge排序与confidence，高confidence非正确；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，confidence/input/permutation条件已承载 |
| [Robustness and Reasoning Fidelity of Large Language Models in Long-Context Code Question Answering](https://arxiv.org/abs/2602.17183v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:04+08:00 | MCQ顺序与open-answer judge协议改变可比人口，长度不等实际利用；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，协议/顺序边界已承载 |
| [Selective Training for Large Vision Language Models via Visual Information Gain](https://arxiv.org/abs/2602.17186v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:12+08:00 | 同reference原图/blur CE差提出样本与token监督，而非绝对概率门；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，L140实际POST通过 |
| [EntropyPrune: Matrix Entropy Guided Visual Token Pruning for Multimodal Large Language Models](https://arxiv.org/abs/2602.17196v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:26+08:00 | head-centered/row-normalized双Gram谱scorer改变永久裁剪选择；2+1+2=5 | 深入完成 | 整合：INFER-PREFILL [Ch43](../../../../books/part-05-inference-system/43-prefill.md)，L180实际POST通过 |
| [GASS: Geometry-Aware Spherical Sampling for Disentangled Diversity Enhancement in Text-to-Image Generation](https://arxiv.org/abs/2602.17200v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:32+08:00 | 原任意球面点的严格期望edge-volume增加与renormalize冲突；2+2+2=6 | 争议 | 暂缓：B2 antipodal初始边长2已最大，中心保证隔离，有限经验仅报告 |

| [ReIn: Conversational Error Recovery with Reasoning Inception](https://arxiv.org/abs/2602.17022v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:11+08:00 | 固定agent首control采样前外部恢复hook与assigned tool耦合；2+2+2=6 | 深入完成 | 整合：AGENT-REFLECTION [Ch80](../../../../books/part-07-agent/80-reflection.md)，L184实际POST通过 |
| [IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/abs/2602.17049v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:41:48+08:00 | canonical trace→typed schema→currentbinding局部gap补全；2+2+2=6 | 深入完成 | 整合：AGENT-MEMORY [Ch77](../../../../books/part-07-agent/77-memory.md)，L1532实际POST通过 |

| [MDP Planning as Policy Inference](https://arxiv.org/abs/2602.17375v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:49:42+08:00 | policy-level posterior不同entropy目标，unbiased log return不授exp target保持；2+2+2=6 | 争议 | 暂缓：中心posterior保证隔离，不称整个算法错误，有限经验仅报告 |
| [What Do LLMs Associate with Your Name? A Human-Centered Black-Box Audit of Personal Data](https://arxiv.org/abs/2602.17483v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:52:16+08:00 | rawforward不可取时fragment补全改变query/observer，不授membership；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，L293实际POST通过 |

| [Algorithmic Collusion at Test Time: A Meta-game Design and Evaluation](https://arxiv.org/abs/2602.17203v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:36+08:00 | initial history×test-time adaptation定义meta-game人口，uniform收益非NE稳定；2+1+2=5 | 深入完成 | 整合：AGENT-MULTI-AGENT [Ch82](../../../../books/part-07-agent/82-multi-agent.md)，L354实际POST通过 |
| [MGD: Moment Guided Diffusion for Maximum Entropy Generation](https://arxiv.org/abs/2602.17211v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:47+08:00 | finite moment path不同完整score分布，解存在/p*与一般速率猜想；2+1+3=6 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS [Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，L184实际POST通过 |
| [Privacy-Preserving Mechanisms Enable Cheap Verifiable Inference of LLMs](https://arxiv.org/abs/2602.17223v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:46:04+08:00 | 实际shared-b逐位置noise预测未绑定输入/位置，合法h复制仍可通过；2+2+2=6 | 争议 | 暂缓：shared-noise soundness中心隔离，不外推独立noise方案或少算攻击 |
| [All Leaks Count, Some Count More: Interpretable Temporal Contamination Detection in LLM Backtesting](https://arxiv.org/abs/2602.17234v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:46:19+08:00 | cutoff×claim公开日期/重新预测Shapley影响代理，非因果faithfulness；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，L3108实际POST通过 |
| [Trivance: Latency-Optimal AllReduce by Shortcutting Multiport Networks](https://arxiv.org/abs/2602.17254v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:46:48+08:00 | 双端口三倍coverage，latency与chunk×congestion/两阶段取舍；2+1+2=5 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING [Ch36](../../../../books/part-04-training-system/36-distributed-training.md)，L189实际POST通过 |
| [FRAPPE: Infusing World Modeling into Generalist Policies via Multiple Future Representation Alignment](https://arxiv.org/abs/2602.17259v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:46:54+08:00 | teacher对应prefix/LoRA兼容分支，非零gate非必更新与均衡；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA [Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)，L399实际POST通过 |

| [LexiSafe: Offline Safe Reinforcement Learning with Lexicographic Safety-Reward Hierarchy](https://arxiv.org/abs/2602.17312v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:48:11+08:00 | 同policy成本→奖励顺序更新不同flattradeoff，但positive-logloss下降与maxreward冲突；2+2+2=6 | 争议 | 暂缓：中心update/安全保证隔离，不自动修公式或以成熟约束流程改书 |

| [NotebookRAG: Retrieving Multiple Notebooks to Augment the Generation of EDA Notebooks for Crowd-Wisdom](https://arxiv.org/abs/2602.17215v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:45:52+08:00 | cell相似检索缺前置state→按执行序编译data-variable closure并在当前data重跑；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，L57实际POST通过 |
| [Web Verbs: Typed Abstractions for Reliable Task Composition on the Agentic Web](https://arxiv.org/abs/2602.17245v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:46:34+08:00 | GUI封装依赖偶然locator→website-owner publiclocator/compat responsibility提案；2+2+2=6 | 深入完成 | 整合：AGENT-TOOL-CALLING [Ch78](../../../../books/part-07-agent/78-tool-calling.md)，L55实际POST通过 |

| [Unified Latents (UL): How to train your latents](https://arxiv.org/abs/2602.17270v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:47:10+08:00 | encoder noise/prior precision与rate分工，但decoder ELBO导数符号冲突；2+2+2=6 | 争议 | 暂缓：中心ELBO/bit保证隔离；有限rate/capacity经验已有Ch23覆盖，不新增正常端点匹配段 |

| [Efficient privacy loss accounting for subsampling and random allocation](https://arxiv.org/abs/2602.17284v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:47:31+08:00 | allocation exp/dual PLD变换改变round方向与误差预算；2+1+3=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，L534实际POST通过 |
| [Representation Collapse in Machine Translation Through the Lens of Angular Dispersion](https://arxiv.org/abs/2602.17287v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:47:35+08:00 | continuous目标/预测器共同移动可零loss却失去符号可分性；2+1+2=5 | 深入完成 | 整合：MODEL-EMBEDDING [Ch12](../../../../books/part-02-model/12-embedding.md)，L107实际POST通过 |

| [Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation](https://arxiv.org/abs/2602.17316v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:48:17+08:00 | lexical/syntax改写影响score不同，ranking和语义等价仍单独验收；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，promptvariant等价审计与修题/ranking人口 |
| [2Mamba2Furious: Linear in Complexity, Competitive in Accuracy](https://arxiv.org/abs/2602.17363v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:49:25+08:00 | 二阶feature state把长度费用转为head维度与数值费用；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-LONG-CONTEXT [Ch22](../../../../books/part-02-model/22-long-context.md)，二阶state/KV/kernelcrossover三角取舍 |
| [IntRec: Intent-based Retrieval with Contrastive Refinement](https://arxiv.org/abs/2602.17639v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:58+08:00 | region身份不保证embedding可分，同embedding反例否定一般反馈保证；2+1+2=5 | 争议 | 暂缓：central保证隔离，成熟正负exemplar不硬改Books |

| [Computer-Using World Model](https://arxiv.org/abs/2602.17365v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:49:28+08:00 | 文字变化→界面渲染与图文拼接反侧；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS [Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md)，实际POST通过 |
| [RPDR: A Round-trip Prediction-Based Data Augmentation Framework for Long-Tail Question Answering](https://arxiv.org/abs/2602.17366v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:49:29+08:00 | 训练query往返误差selector区别于index增强；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，实际POST通过 |
| [The Role of the Availability Heuristic in Multiple-Choice Answering Behaviour](https://arxiv.org/abs/2602.17377v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:49:45+08:00 | no-stem corpus-conditioned option prior负对照；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，实际POST通过 |
| [Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature](https://arxiv.org/abs/2602.17385v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:49:56+08:00 | 初始化JGram预计算→后续输出保持regularizer；2+1+2=5 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，实际POST通过 |

| [Convergence Analysis of Two-Layer Neural Networks under Gaussian Input Masking](https://arxiv.org/abs/2602.17423v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:50:52+08:00 | 输入Gaussian噪声的pointwise梯度界与尾部期望桥冲突；2+1+2=5 | 争议 | 暂缓：中心采用隔离，无Books；均匀界/尾部期望或明确截断mask后重开 |

| [Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study](https://arxiv.org/abs/2602.17431v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:51:03+08:00 | 分解/一致性scorer/聚合三轴与分类≠校准；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体测量/校准边界 |
| [AIDG: Evaluating Asymmetry Between Information Extraction and Containment in Multi-Turn Dialogue](https://arxiv.org/abs/2602.17443v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:51:19+08:00 | 角色与prior-hypothesis攻击人口分账；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体测量/校准边界 |
| [ABCD: All Biases Come Disguised](https://arxiv.org/abs/2602.17445v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:51:22+08:00 | option/fewshot permutation与parser/readout测量身份；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，具体测量/校准边界 |

| [Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers](https://arxiv.org/abs/2602.17410v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:50:33+08:00 | 内部层概率候选→动态token监督与CF softtarget，非GT不等负真值；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，实际正文/邻接/末注POST通过 |
| [Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge](https://arxiv.org/abs/2602.17452v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:51:32+08:00 | ONNX编译数值artifact/trace的证明身份不等原浮点行为或安全；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际正文/邻接/末注POST通过 |
| [Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models](https://arxiv.org/abs/2602.17497v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:52:37+08:00 | policy变化logratio不自动等于环境普通advantage，offset/soft-value接口需分开；2+1+2=5 | 争议 | 暂缓：中心等价保证隔离，不否定带offset构造或有限heuristic结果，无Books |

| [LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights](https://arxiv.org/abs/2602.17510v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:52:56+08:00 | 预训练跨层tensor的冻结Tucker空间适配，初态/实际rank中心接口不一致；2+1+2=5 | 争议 | 暂缓：near-I不保证精确保base，12层与r1=24冲突；不擅修recipe，无Books |
| [When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning](https://arxiv.org/abs/2602.17520v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:53:10+08:00 | 熟悉语义可能压过本地定义，Solve/Flag区分当前规格与典型答案；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，配对规则/语义prior/EvalSpec；不新增重复段 |
| [The Anxiety of Influence: Bloom Filters in Transformer Attention Heads](https://arxiv.org/abs/2602.17526v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:53:19+08:00 | head功能类比须分长度、内容与干预，fixedlength反侧重判prefix头；2+1+2=5 | 标准完成 | 已有覆盖：MODEL-SELF-ATTENTION [Ch14](../../../../books/part-02-model/14-self-attention.md)，路由/归一化/行为与因果分账；不授真实Bloom实现 |
| [Evaluating Chain-of-Thought Reasoning through Reusability and Verifiability](https://arxiv.org/abs/2602.17544v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:53:44+08:00 | help与harm相加测persuasiveness，跨模型同答案不是truth verifier；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，reasoning/prefill/identity/agreement边界 |

| [Privacy in Theory, Bugs in Practice: Grey-Box Auditing of Differential Privacy Libraries](https://arxiv.org/abs/2602.17454v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:51:35+08:00 | primitive冻结输出/重放PRNG将结构conformance与sensitivity测试定位到调用；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，实际正文/邻接/末注POST通过；结构不等分布隐私证明 |

| [A Theoretical Framework for Modular Learning of Robust Generative Models](https://arxiv.org/abs/2602.17554v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:53:59+08:00 | gate全局归一化约束不从expert KL近似推出，经验支持集与expert支持需分开；2+1+2=5 | 争议 | 暂缓：原G1可空使中心robustexistence无法由已述假设推出；不补归一化，无Books |

| [Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning](https://arxiv.org/abs/2602.17546v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:53:47+08:00 | riskcritic在线调整NLL与固定reference KL；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，实际POST通过 |
| [MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning](https://arxiv.org/abs/2602.17550v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:53:53+08:00 | 单边sgGaussian gate×ratioA及oldmass/signedwidth；2+1+2=5 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际POST通过 |
| [GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking](https://arxiv.org/abs/2602.17555v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:00+08:00 | caption→temporalgraph与accuracy门控attention训练代理；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，实际POST通过 |
| [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:05+08:00 | RM候选支持perturbed→currentpolicy及交替训练；2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，实际POST通过 |

| [AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games](https://arxiv.org/abs/2602.17594v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:57+08:00 | pause-on-model-access改变gameclock/wallclock与交互预算；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，双时钟与event/runtime identity |

| [ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment](https://arxiv.org/abs/2602.17560v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:08+08:00 | hdot逐点>0不推出有限到达，normalizedgradient域/零梯度桥缺；2+1+2=5 | 争议 | 暂缓：中心到达/不变性保证隔离，无Books，不否定有限steering经验 |

| [Revisiting Weight Regularization for Low-Rank Continual Learning](https://arxiv.org/abs/2602.17559v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:06+08:00 | full-ΔW empiricaldiagF与task-end merge/reinit；2+1+2=5 | 深入完成 | 整合：TRAIN-LORA [Ch30](../../../../books/part-04-training-system/30-lora.md)，实际POST通过 |
| [Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning](https://arxiv.org/abs/2602.17565v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:14+08:00 | 同X/λ squaredridge signedaffine与GCV条件边界；2+1+2=5 | 深入完成 | 整合：TRAIN-SFT [Ch29](../../../../books/part-04-training-system/29-sft.md)，实际POST通过 |
| [Canonicalizing Multimodal Contrastive Representation Learning](https://arxiv.org/abs/2602.17584v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:43+08:00 | unimodal map向othermodality迁移的kernel/维度条件；2+1+2=5 | 深入完成 | 整合：MULTIMODAL-REPRESENTATION [Ch23](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)，实际POST通过 |
| [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:48+08:00 | intervention classifier只advisory，prompt-timing非approval；2+1+2=5 | 标准完成 | 已有覆盖：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md) |

| [Asymptotic Smoothing of the Lipschitz Loss Landscape in Overparameterized One-Hidden-Layer ReLU Networks](https://arxiv.org/abs/2602.17596v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:54:59+08:00 | convexLipschitz与L1 regularization不推出原norm bound/barrier常量；2+1+2=5 | 争议 | 暂缓：中心Lemma1/Cα桥隔离，无Books，不否定有限DSS经验 |

| [Towards Anytime-Valid Statistical Watermarking](https://arxiv.org/abs/2602.17608v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:16+08:00 | fixed-horizon分数→条件非负test supermartingale的可随时停止检测合同；2+2+2=6 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，正文1113/完整邻接/末注实际POST通过 |

| [The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?](https://arxiv.org/abs/2602.17598v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:03+08:00 | 同骨干cascade与speech-LLM误差重叠、probe/擦除及随机反侧限定架构归因；2+1+2=5 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)同输入/backbone/预算与消融归因；Ch23感知可读≠action使用为handoff |

| [Stable Asynchrony: Variance-Controlled Off-Policy RL for LLMs](https://arxiv.org/abs/2602.17616v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:27+08:00 | 固定population off-policy梯度baseline→有限plug-in及逐trajectory双buffer/延迟DP执行，ESS与TIS分账；2+2+2=6 | 深入完成 | 整合：TRAIN-GRPO [Ch33](../../../../books/part-04-training-system/33-grpo.md)，实际正文/完整邻接/自身末注POST通过 |
| [What Makes a Good LLM Agent for Real-world Penetration Testing?](https://arxiv.org/abs/2602.17622v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:36+08:00 | typed evidence/precondition变化→恢复以前剪枝search support，不把difficulty代理当权限或完整性；2+2+2=6 | 深入完成 | 整合：AGENT-PLANNING [Ch79](../../../../books/part-07-agent/79-planning.md)，实际正文/完整邻接/自身末注POST通过 |

| [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning](https://arxiv.org/abs/2602.17633v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:50+08:00 | 三region随机strong反馈、inversepropensity更新与两侧label分母；2+1+2=5 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，actual POST通过 |
| [Multi-Round Human-AI Collaboration with User-Specified Requirements](https://arxiv.org/abs/2602.17646v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:08+08:00 | 题内固定/题末truth更新及prefixdomination下AI-set omission控制；2+2+2=6 | 深入完成 | 整合：AGENT-WORKFLOW [Ch81](../../../../books/part-07-agent/81-workflow.md)，actual POST通过 |

| [SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer](https://arxiv.org/abs/2602.17632v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:55:49+08:00 | noise MSE目标与正score/缩放桥不一致；2+1+2=5 | 争议 | 暂缓：中心noise/score参数化隔离，不自行修recipe，无Books |
| [Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting](https://arxiv.org/abs/2602.17645v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:07+08:00 | 视觉重叠不授稳定gradient与source/target变换分责；2+1+2=5 | 深入完成 | 整合：PLATFORM-SECURITY [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，actual POST通过 |
| [Differences in Typological Alignment in Language Models' Treatment of Differential Argument Marking](https://arxiv.org/abs/2602.17653v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:17+08:00 | 受控syntax placement与semantic licensing可分的局部学习证据；2+1+2=5 | 标准完成 | 仅报告：18GPT2 DAM规则行为不确立一般学习机制/人类typology因果，未改变书稿长期判断 |

| [Mine and Refine: Optimizing Graded Relevance in E-commerce Semantic Search Retrieval](https://arxiv.org/abs/2602.17654v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:19+08:00 | partialgrade跨pair正/负角色与mining保原negative；2+1+2=5 | 深入完成 | 整合：AGENT-RAG [Ch76](../../../../books/part-07-agent/76-rag.md)，actual POST通过 |
| [MARS: Margin-Aware Reward-Modeling with Self-Refinement](https://arxiv.org/abs/2602.17658v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:24+08:00 | margin引导合成监督分配，曲率与方向条件分开；2+1+2=5 | 深入完成 | 整合：TRAIN-RLHF [Ch31](../../../../books/part-04-training-system/31-rlhf.md)，actual POST通过 |
| [When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs](https://arxiv.org/abs/2602.17659v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:25+08:00 | affine概率与log乘积不是同对象，反事实实验须另分scope；2+1+2=5 | 争议 | 暂缓：中心Bayes重加权桥隔离，不否定有限LIBERO-CF经验，无Books |
| [Sink-Aware Pruning for Diffusion Language Models](https://arxiv.org/abs/2602.17664v1) | 2026-02-20T09:00:00+08:00 ～ 2026-02-20T10:56:32+08:00 | noised/time校准activation重权改变offline importance；2+1+2=5 | 深入完成 | 整合：INFER-TENSORRT-LLM [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md)，actual POST通过 |

## 4. 证据与知识整合

### [Omitted Variable Bias in Language Models Under Distribution Shift](https://arxiv.org/abs/2602.16784v1)

精确v1 §3.1–3.2、§5–7实际读；[核心原源](../_sources/daily-20260221/V3_BODY_2602.16784_00000_20000.txt)与[评价/反侧](../_sources/daily-20260221/V3_BODY_2602.16784_EVAL_FOCUS.txt)。完整X,Z下条件loss稳定与support overlap是前提；observable h(X)上的DR只对nuisance误设稳健，不能恢复遗漏变量。隐藏作用参数不可由观察数据识别，必须声明敏感性范围。正文ρ定义为Corr²而界又用ρ²，未授其完整数值界；target labels调参也不能视为新域oracle。作者Amazon半合成100次线性learner、EmoBank/HateSpeech条件实验与GPT4.1/MATH表示比较均不证明LLM任意部署保证。root实际必要原源及Ch66:480–500的population/scorer分布不变量后，确认中心公式暂缓；已有成熟分布原则不构成额外Books缺口，不强行整合。

### [References Improve LLM Alignment in Non-Verifiable Domains](https://arxiv.org/abs/2602.16802v1)

v1 §3.2–4.3、T1–4/T6实际读；[核心](../_sources/daily-20260221/V3_BODY_2602.16802_00000_20000.txt)、[对照](../_sources/daily-20260221/V3_BODY_2602.16802_EVAL_FOCUS.txt)。Reference answer帮助judge核事实/指令，工程上不应直接误用为逐字/风格复制要求；该防误用边界不是已验证style-copy风险。DPO reference policy仍是冻结概率anchor。11judges/5人工配对集顺序交换及bootstrap只支持该协议。Strong teacher 60k答案SFT后，当前policy每题5候选形成10pairs；这不是无教师免费自改善。弱reference仍可改善ref-free却远弱于强reference；有限分类实验中creative收益对Qwen较弱而对Llama仍明显，不能推断该任务不需要内容锚。Llama RefEval并非所有指标胜ArmoRM；AlpacaEval长度控制winrate/ArenaHard不能替代事实、安全或人类通用质量。完整judge调用、SFT/DPO与beta选择成本保留；硬件/精度/总墙钟未以现有读取认证。root实际必要原源及Ch34:158–179/267–285后授reference answer≠policy具体差额；已融入Ch34偏好质量论证单段，实际正文/完整邻接/末注POST通过。

### [Simple Baselines are Competitive with Code Evolution](https://arxiv.org/abs/2602.16805v1)

v1只取§5 agent/code臂、AppendixJ/K/O，[主要对照](../_sources/daily-20260221/V3_BODY_2602.16805_AGENT_FOCUS.txt)与[必要附录](../_sources/daily-20260221/V3_BODY_2602.16805_APPENDIX_JK.txt)实际读。AIME24小validation×3、AIME25 heldout，全部scaffold调用GPT4.1-nano且每题最多10calls；meta-model与编译/调试eval数仍有差异，不把全部提升因果归给搜索复杂度。10次fresh re-eval使validation赢家回落，说明先cheap筛选再高预算独立重测比只信一次最大分更可解释。未采用K的tie公式（分母与均分措辞冲突），也未展开数学发现臂。Ch66实际procedure-level winner'scurse已要求保存selection/stopping/holdout并重新运行；Ch81:388–419实际cascade/search-overfit段已区分便宜筛选、昂贵评价、随机测量与heldout。root必要原源及两个实际owner段独核，具体已有覆盖通过，不制造重复摘要。

### [One-step Language Modeling via Continuous Denoising](https://arxiv.org/abs/2602.16813v1)

v1 §2–4、§5/T1–3、§6实际读，[方法](../_sources/daily-20260221/V3_BODY_2602.16813_METHOD_FOCUS.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16813_EVAL_FOCUS.txt)。One-hot argmax固定解码；clean-data softmax/CE避免直接全维velocity-MSE瓶颈。时间重参数化按one-hot decoding error下降分配，不是logSNR。冻结FLM加learned correction学average-velocity组合接口，再蒸馏为单模型；Euler-step/MSE消融优于logit-denoiser/CE，不能反写为后者最佳。170M LM1B/OWT 1024样本GenPPL/entropy/SelfBLEU不衡量完整能力；OWT one-step FMLM PPL129.32与entropy4.53不能和Duo PPL47.13但entropy2.80单数排名。OWT两步PPL134.26/entropy5.07说明更多步数不保证每个指标改善。全文词表反传约30%额外训练time/memory、第一蒸馏两模型与额外training都付费；无生产SLO或任意规模认证。Ch24原continuous geometry与flow-map组合接口未承载decode-error时间及冻结teacher校正/压缩分工；root必要原源/Ch24:475–491独核后，已在组合一致性之后融入一自然段，实际正文/完整邻接/末注POST通过。


### [Hybrid-Gym: Training Coding Agents to Generalize Across Tasks](https://arxiv.org/abs/2602.16819v1)

精确v1 §4.1–4.5、§3/Table4–5与A.3.2实际读；[接口与机制](../_sources/daily-20260221/V3_BODY_2602.16819_FOCUS.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16819_EVAL_FOCUS.txt)、[训练](../_sources/daily-20260221/V3_BODY_2602.16819_TRAIN_FOCUS.txt)。同一harness/dummy repository不能让patch-like动作自然迁移到message-only任务；teacher把reasoning与action联合stitch，改变的是监督与动作接口，较长轨迹本身未被识别为收益原因。Easy50为有限任务分析；HybridGym15仍低于SWEPlay17，不授全面最优。7B搜索超参/8A6000与32B固定配置/2H100不同；环境setup cents不是rollout、teacher、SFT与评测全成本。Ch29已有教师正确性/质量论证未承载动作接口转移边界，root必要源与实际owner/邻接核验后，已在teacher轨迹之后L178融入窄段；实际正文/完整邻接/末注POST通过。旧verified trajectory仍合理。

### [Formal Mechanistic Interpretability: Automated Circuit Discovery with Provable Guarantees](https://arxiv.org/abs/2602.16823v1)

v1 Def2、核心验证/搜索、必要[单调性与闭包](../_sources/daily-20260221/V3_BODY_2602.16823_MONOTONICITY_FOCUS.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16823_EVAL_FOCUS.txt)实际读。有限样本faithfulness不保证指定连续域；该规格比较同一输入的full/pruned logit差，并要求双输入产生的patch来自可达集合，不是任意activation box。Sound verifier支持所编码模型与规格，不自动证明事实真值、唯一真实因果或全局最小LLM电路。Greedy subset-minimal依赖单调性及reachable拼接闭包，不能从任意真实网络推出；size-restricted MHS只给其条件下下界，仍需验证。小网络runtime反侧不授规模化。Ch5实际Faithfulness Budget/greedy论证缺连续域spec与reachable patch条件，root必要源及owner独核后已在L308融入一段；正文/完整邻接/末注POST通过。Finite-case patch与行为核验仍为低成本有效分支。

### [Learning under noisy supervision is governed by a feedback-truth gap](https://arxiv.org/abs/2602.16829v1)

只审v1神经网络噪声监督臂；[递推原源](../_sources/daily-20260221/V3_BODY_2602.16829_THEORY_FOCUS.txt)、[有限NN经验](../_sources/daily-20260221/V3_BODY_2602.16829_ML_FOCUS.txt)实际读，不扩human/EEG。Fast process读取noisy observation、slow process读取ground truth，其稳态不同；期望误差推导遗漏ε bias时，noise=0的比较不能支持任意noise时equal rates使gap消失。小gap也不等准确率高。局部容量/噪声关系只保作者条件经验，不补造Ch5长期新规律。root必要递推与反侧实际独核：中心解释暂缓且不进入Books；不因争议撤销NN机制准入。恢复须合法含噪稳态递推及对应模型对照。

### [VAM: Verbalized Action Masking for Controllable Exploration in RL Post-Training — A Chess Case Study](https://arxiv.org/abs/2602.16833v1)

v1核心方法、§5及A4/A5/A8实际读；[方法](../_sources/daily-20260221/V3_BODY_2602.16833_METHOD_FOCUS.txt)、[对照](../_sources/daily-20260221/V3_BODY_2602.16833_EVAL_FOCUS.txt)、[完整相关prompt](../_sources/daily-20260221/V3_BODY_2602.16833_CONFIG_FOCUS.txt)。每轮只移除合法已采样动作、最多轮数或best停止，组内共享的是state与当轮allowed-set；该集合写在prompt而非logit hard mask，invalid/repeated action仍由解析处理。不同prompt措辞与matching rollout count不等价token/verifier成本，跨轮更新不能宣称原unmasked population无偏或安全。Ch33同条件采样论证未承载迭代allowed-set的条件变化，root必要源/owner独核后L76融入一段；正文/完整邻接/末注POST通过。普通outcome GRPO仍是无需此探索控制的合理分支。

### [NeST: Neuron Selective Tuning for LLM Safety](https://arxiv.org/abs/2602.16835v1)

v1 Eq15、§3.3–4.3、§6–8与必要whitebox反侧实际读；[机制/评价](../_sources/daily-20260221/V3_BODY_2602.16835_METHOD_EVAL_FOCUS.txt)、[限制](../_sources/daily-20260221/V3_BODY_2602.16835_LIMIT_EVAL_FOCUS.txt)。Probe筛出的FFN gate/up行按cluster共享线性增量再fold，其增量仍可能低秩，但不是为整个投影学习自由两组低秩因子；probe association不证明causal safety neuron。§3.4 raw/no-normalization/kmax2与§4.2 normalized/vary-k冲突，确定recipe不采用。CB与LoRA数据/训练预算不同，ARC/MMLU退步与未充分核验的whitebox鲁棒性保留，不授全安全。Ch30共享基/target-module论证缺selected支集与tied-row更新空间，root必要源/实际owner核验后L203窄写；首句低秩暗示经POST反馈窄修，root实际回核整段通过，末注已同步。完整LoRA与冻结基座仍为合理回退。

### [A Residual-Aware Theory of Position Bias in Transformers](https://arxiv.org/abs/2602.16837v1)

目标是actual v1此标题，而非库存/当前v2的“A Structural Theory…”；[核心与kernel评价](../_sources/daily-20260221/V3_BODY_2602.16837_METHOD_EVAL_FOCUS.txt)、[必要证明](../_sources/daily-20260221/V3_BODY_2602.16837_PROOF_FOCUS.txt)实际读。Effective row-stochastic rollout、dataset mean、uniform heads与gradient influence是明示假设的position代理，不等真实task因果。无限proof使用P X0 V，未承载主文additive residual接口，不能授真实residual Transformer的collapse iff。Const-content可在所测Spearman反退；hardware/precision未披露，不授运行性能。root必要原源实际独核后中心proof/代理隔离，有限kernel结果仅报告；不把全中心争议缩成成熟position原则强写Books。恢复须同接口合法证明及验证代理到真实动力学的条件。

### [Training Large Reasoning Models Efficiently via Progressive Thought Encoding](https://arxiv.org/abs/2602.16839v1)

v1 Eq2–4与§3–4.4实际读；[方法/评价](../_sources/daily-20260221/V3_BODY_2602.16839_METHOD_EVAL_FOCUS.txt)、[模型身份反侧](../_sources/daily-20260221/V3_QWEN_IDENTITY_CHECK.json)。Evicted KV经global queries写入add+Normalize的context state，再经A/B产生动态低秩权重，不需每个context反传；训练资产与request state仍不同。原文3B的32层4096/32heads、7B的32层5120/40heads和两官方Qwen2.5 config不符，精确模型性能隔离，不连带否定可见机制。Attention-only FLOPs不是whole pipeline常数；convergence不等同训练预算，HeadKV增加iteration与global64退步保留。Ch22梯度式历史压缩未承载forward stream-state差额；root必要源与owner核验后L658窄写，request reset/版本/压缩非provenance明确是工程边界而非作者已实现隔离。正文/完整邻接/末注POST通过；旧KV/sliding/梯度压缩或检索仍各有条件。

### [AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence](https://arxiv.org/abs/2602.16873v1)

v1 §3.2–3.4、§5与Table2–4实际读；[核心/对照原源](../_sources/daily-20260221/V3_BODY_2602.16873_FOCUS.txt)。Adaptive routing对固定hybrid/concat有局部潜力，但§3.4的W/L≥width被五节点单位链加两孤点反例否证：W=7、L=5、width=3，7/5<3。§5.5剩余85%test与Table4全500描述冲突，未澄清的中心数字不采用。Root必要源实际核验后中心law/optimal/精确跨任务保证隔离，不继续遍历所有宣传或全部证明；有限经验只能按作者自述范围报告，不授Books路由法则。恢复须修正定义/定理及一致test IDs、split与比较。

### [OpenSage: Self-programming Agent Generation Engine](https://arxiv.org/abs/2602.16891v1)

v1 §3.2–3.4、§4.1–4.4、C.3及相关memory实际读；[核心](../_sources/daily-20260221/V3_BODY_2602.16891_00000_22000.txt)、[评价/失败](../_sources/daily-20260221/V3_BODY_2602.16891_EVAL_FOCUS.txt)、[memory](../_sources/daily-20260221/V3_BODY_2602.16891_MEMORY_FOCUS.txt)。Metadata/object pool、每次调用clone与durable archive是三个生命周期；删除clone不删除历史，也不自动rollback外部effect。NoVertical同时改变多项结构，不能唯一归因dynamic create；NoTools亦联合改变。TerminalBench禁动态结构、LOCOMO不优于Mem0/Mem0g，Docker/derived graph不授完整权限/真值安全。Ch82有界fan-out缺注册元数据、cloned execution与readonly archive分责，root必要源及actual owner/邻接后L198窄写；正文/完整邻接/末注POST通过。静态pool与typed handoff仍为可靠性条件不成立时回退。

### [Overseeing Agents Without Constant Oversight: Challenges and Opportunities](https://arxiv.org/abs/2602.16844v1)

v1实际§5.1–5.3/Table3、§6–7，[核心原源](../_sources/daily-20260221/V3_BODY_2602.16844_CORE_FOCUS.txt)；不把TOC/前6500字当正文核验。十二名技术员工、八任务、Wizard-of-Oz手工标注与事后trace、counterbalanced条件以及soft五分钟限制支持有限界面对照。Overall accuracy effect .18的95%CI[-.52,.94]不能证明增益，也不能推出严格no-effect；错误被接受子人口的confidence g=.85、CI[.01,1.88]不等全用户因果校准。Navigation/time/accuracy/confidence应分账，green完成标记继承agent claims不成为独立证据。root必要原源及Ch66 Human-Agent邻接PRE通过，实际L4424已窄写；作者正文/完整邻接/末注已顺读，root实际写后POST通过，未运行界面或复现。

### [On the Mechanism and Dynamics of Modular Addition: Fourier Features, Lottery Ticket, and Grokking](https://arxiv.org/abs/2602.16849v1)

精确v1 Eq3.1、Def4.1(ii)/(iii)、理论ODE及局部模型实验实际读；[机制原源](../_sources/daily-20260221/V3_BODY_2602.16849_CORE_FOCUS.txt)、[必要理论](../_sources/daily-20260221/V3_BODY_2602.16849_THEORY_FOCUS.txt)。Two-layer模型p=23/M=512、full-data/ReLU/AdamW1e-4与75%split/weight decay2的grokking不是任意网络保证。中心定义(iii)写exp(i·ι·Σφ)=0，对实相位模恒1，不可能成立；(ii)约束αβ²，而Eq3.1输出乘积系数为α²β；gradient flow的+∇loss也不支持所写descent解释。不能替作者猜修正公式。Root实际必要原源核验后准入保留、中心隔离，局部frequency/phase经验仅报告；不扩证明全集，不写Books普遍机制。恢复须一致定义/输出系数/合法下降动力学与对应验证。

### [DODO: Discrete OCR Diffusion Models](https://arxiv.org/abs/2602.16872v1)

v1 §4–7/T1–3、Training Configuration/B1及直接Limitations实际读；[核心](../_sources/daily-20260221/V3_BODY_2602.16872_CORE_FOCUS.txt)、[训练](../_sources/daily-20260221/V3_BODY_2602.16872_TRAIN_FOCUS.txt)。270k OlmOCR混合页、Qwen2.5VL3B、200ksteps/8A10040GB/B8/BF16与有限英文OCR人口，不授通用多模态优势。Fixed prefix tokens不固定bidirectional hidden/KV；OCR错误EOS/absolute offset的rigid失配无法自然平移。Inference-only blocking不代替block-causal训练支持；T3 B256全重算NED .067/22.9TPS、近似KV .566/37.3、block-causal .192/41.4，质量与吞吐不同时最佳。T2 oracle-length vanilla不能当真实部署baseline，T1跨模型排名不识别单独机制；threshold/DUS及小块提交频率仍有成本。root必要源/actual Ch24 Block邻接PRE通过，L754已实际窄写；作者正文/完整邻接/末注已顺读，root实际写后POST通过，不授三倍等质量或blanket cache保证。

以上已列家族日期原字段见各 `V3_PRIMARY_*.abs.txt/.datacite.json`。v1 Submitted均在Wed Feb18 19:00Z及以后，按官方最早公告只能从Fri Feb20 09:00BJT开始；final ID/DOI公告后才提供，与官方自动DOI流程及同身份Registered+1秒保守上界共同限定公开区间。没有把Submitted、Created或Registered直接写成精确公开时刻。

### [AgentLAB: Benchmarking LLM Agents against Long-Horizon Attacks](https://arxiv.org/abs/2602.16901v1)

精确v1 §3–5及A1–A5实际读；[核心](../_sources/daily-20260221/V3_BODY_2602.16901_00000_23000.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16901_EVAL_FOCUS.txt)、[实现接口](../_sources/daily-20260221/V3_BODY_2602.16901_IMPLEMENTATION_FOCUS.txt)、[memory](../_sources/daily-20260221/V3_BODY_2602.16901_MEMORY_FOCUS.txt)。644安全case/28环境、五类攻击的人口与攻击访问权不同；自适应策略、turn与搜索预算共同变化，不能将one-shot/long-horizon差额单因果归时长。默认GPT5.1 planner/Qwen3-14B-Abliterated attacker、GPT5.1 judge，部分攻击另用GPT5.1优化；示例bank、后续session检索poison偏好不等直接写memory DB。攻击曲线与防御开销不等完整wall-clock/费用，hardware/precision未披露。Table2 GPT5.1 Overall69.9与五列简单均值60.18不一致，未披露权重则该Overall隔离而不替作者补数；outcome也并非全部确定性verifier。root必要源与actual owner独核后具体已有覆盖通过：Ch66 L1974–1998的risk(N)/adaptive预算、L2516–2522的turn-frontier、L4378–4388的profile/access与Ch77 L127–131的accepted memory不等truth已承载最小采用原则，不写重复一般多轮原则，不授全Agent不安全。

### [LLM-WikiRace: Benchmarking Long-term Planning and Reasoning over Real-World Knowledge Graphs](https://arxiv.org/abs/2602.16902v1)

本窗只采用v1；[核心](../_sources/daily-20260221/V3_BODY_2602.16902_00000_23000.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16902_EVAL_FOCUS.txt)、[knowledge/loop定义](../_sources/daily-20260221/V3_BODY_2602.16902_KNOWLEDGE_LOOP_FOCUS.txt)实际读§3–7及C/D。固定2025-06-23图快照最大SCC549232节点、450起终点、30步；每步50出边由真实最短距离筛选后随机排序，distance没提示不等没有oracle support；人类公开游戏全出边协议不同。1000 connectivity probes含unparsed输出丢弃，跨模型F1关联不识别知识阈值/规划因果。Qwen2.5-7B的1000训练对与单步GRPO改善Easy而Hard仍0，不授多步搜索普遍规律，300steps/epochs措辞冲突保留。Appendix D任意重访为loop、条件恢复率与最大visitation分母互异；恢复不证明模型识别循环，高loop不自动错误。root必要源/actual Ch66 cycle差额PRE通过后，在PLATFORM-EVALUATION-SYSTEM Ch66 L823窄写三分母+oracle support/费用与旧短任务并存；正文/完整邻接/末注实际POST通过，未运行代码/复现。

### [Narrow fine-tuning erodes safety alignment in vision-language agents](https://arxiv.org/abs/2602.16931v1)

精确v1 §2–4及A5必要judge实际读；[实验协议](../_sources/daily-20260221/V3_BODY_2602.16931_00000_23000.txt)、[缓解](../_sources/daily-20260221/V3_BODY_2602.16931_MITIGATION_FOCUS.txt)、[judge](../_sources/daily-20260221/V3_BODY_2602.16931_JUDGE_FOCUS.txt)。Gemma3-4B、视觉encoder冻结但LoRA目标所有linear、1500 harmful面部样本/1epoch/B4/BF16/AdamW2e-4，有限rank8–256。Text150 synthetic与VQA250并非配对同内容人口，不能将均值差因果归视觉；GLM4.6V-FP8对三响应取最大、1–19rubric也不是unsafe行为概率。SVD对象H_ft而非delta/causal harm，top10占60–70%activation variance不等有害信息维度；steering contrast direction为另一对象。Benign fine-tune与steering仍残余风险，layer20/32与20/25描述冲突，不采用确定recipe；总成本/hardware未披露。root必要源/actual owner独核后仅报告：Ch66 L219–221的geometry≠behavior gate、Ch30 L690–692的SVD能量≠因果维度、Ch72 L619–631的update/OOD全输出安全门已支持防误用边界，局部一模型观察尚不改变这些长期解释，不强造新Books段。

### [DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs](https://arxiv.org/abs/2602.16935v1)

精确v1 §3.2–3.2.6、§4–5.4实际读；[方法](../_sources/daily-20260221/V3_BODY_2602.16935_METHOD.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16935_EVAL.txt)、[限制/未来](../_sources/daily-20260221/V3_BODY_2602.16935_LIMIT.txt)。任务相关BERT embedding→3层GRU state→投影state与raw当前embedding拼接→风险MLP，支持history/instant两信号分工，不证明无需显式历史或所有漂移可检。437058训练序列约20%恶意、1epoch/B512/BF16/AdamW1e-5；单epoch不证明不记忆。1010测试=210攻击/800benign，作者声称样本未见，但HH/XGuard/DEFCON等来源共享，独立分布未验；不同baseline encoder/训练不支持独归GRU，未有同encoder去GRU对照。A100平均19ms的输入长度、batch/concurrency和tail SLO未披露，不能继承正文T4生产表述；复杂function-calling误报保留。原源heading显示Aug24而Submitted/Registered身份为本窗v1，未将heading当首次公开时刻。动态降权、图追踪/federated intent仍future。actual Ch72 sensor/authority与message/account邻接未承载固定历史state+current shortcut，root必要源/owner PRE通过后在L605窄写；作者完整邻接/末注顺读，root实际POST通过；未核实现/复现。

### [Heterogeneous Federated Fine-Tuning with Parallel One-Rank Adaptation](https://arxiv.org/abs/2602.16936v1)

精确v1 §3.2–3.5/4/C2实际读；[核心](../_sources/daily-20260221/V3_BODY_2602.16936_METHOD.txt)、[overhead](../_sources/daily-20260221/V3_BODY_2602.16936_OVERHEAD.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16936_EVAL.txt)、[配置](../_sources/daily-20260221/V3_BODY_2602.16936_CONFIG.txt)。Σrank-one与BA代数等价，不是新增函数类；随机选择r_i训练而其余fold到冻结基座，更新前有效权重仍完整全局函数，非坐标/gauge不变。每rank在实际参与集Q_j上分别平均A/B，乘积协方差与人口差异未归零；§3.4范数和界遭R=1/d=k=1/v=2、A=B=±3反例（cov9>所写6），不采用该理论界或补造有界条件。50–200clients/10%参与/3runs与有限GLUE/LLM slices只是作者局部；C2 Dolly/finance/medical rank表与prose、Qwen型号相异，确定recipe和全性能身份隔离。完整R广播、临时buffer与dense fold仍付费，uplink小不等免费全成本或privacy。Ch30原gauge-invariant consensus承载不同分支，没有Select-N-Fold初始函数/训练支集分離；root必要源/actual owner PRE后L622窄写，保原dense/homogeneous/independent fallback；作者完整邻接/末注已顺读，root实际POST通过。

### [Mind the GAP: Text Safety Does Not Transfer to Tool-Call Safety in LLM Agents](https://arxiv.org/abs/2602.16943v1)

精确v1 §3.3–3.6、§4与§6关键反侧实际读；[method](../_sources/daily-20260221/V3_BODY_2602.16943_METHOD.txt)、[results](../_sources/daily-20260221/V3_BODY_2602.16943_EVAL.txt)、[governance/control](../_sources/daily-20260221/V3_BODY_2602.16943_GOV.txt)、[limits](../_sources/daily-20260221/V3_BODY_2602.16943_LIMIT.txt)、[cost](../_sources/daily-20260221/V3_BODY_2602.16943_COST.txt)。六API模型/三个prompt条件/两variant/三治理/三重复，17496计划、18144收集、648重复去除、76error→17420分析；temp.3/thinking4096/$120只此2026Feb14–15协议，hardware/precision和生产SLO未披露。Mocktools无授权、允许全部返回；TC-safe在enforcement前按forbidden predicate计proposal，T-safe只检查最终拒答/noPII，GAP非‘同时拒答与真实执行伤害’。零call会机械safe，anytool条件人口不匹配因果；enforce降低LEAK不等改变尝试，无显著deterrent但MDE10–13pp不授严格零作用。DeepSeek合法control14.2%误报不经人口迁移成为全攻击误差上界；合同自一致779tests也不是policy truth。GPT5.2测试+judge双角色、相关重复、单English/单用户轮/最多10assistant call限制保留。Ch66原security operating curve缺这些分母/时序划分，root必要源/owner PRE后L2011窄写；作者完整邻接/末注已顺读，root实际POST通过。

### [In-Context Learning in Linear vs. Quadratic Attention Models: An Empirical Study on Regression Tasks](https://arxiv.org/abs/2602.17171v1)

精确v1 §2/Table1–3、§4.2–7实际读；[core](../_sources/daily-20260221/V3_BODY_2602.17171_DECIDING_CORE.txt)、[controlled局部结果](../_sources/daily-20260221/V3_BODY_2602.17171_RESULT_ONCE.txt)。dx5/k10无噪声Gaussian线性回归，256width/4heads/1、3、6层/5seeds；squared-ReLU linear attention在该任务可匹配softmax局部，是必要性反侧而不是所有LLM普遍替代。Quadratic13.7–17.6M/B32/1e-4/30ksteps与linear.8–4.75M/B64/3e-4/7500–10ksteps不控制架构因果；A100精度未披露。Own-final90%阈值的seen examples不是同质量速度，浅层linear256k多于quadratic224k，不能授每配置快；anisotropic/depth均值与uncertainty不足以支持宣传全优。实际Ch8 L84–104区分ICL行为与算法、Ch22 L464–475区分finite-feature与softmax语义，未宣称softmax必要；局部small-model反证保留，但不产生新普遍Books机制。root必要源与actual owner后仅报告通过，不因小实验否定学术价值，未复现。

### [MeGU: Machine-Guided Unlearning with Target Feature Disentanglement](https://arxiv.org/abs/2602.17088v1)

精确v1 §4–5、Table6/F实际读：[方法](../_sources/daily-20260221/V3_BODY_2602.17088_METHOD_ONCE.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.17088_EVAL.txt)、[必要Table6](../_sources/daily-20260221/V3_BODY_2602.17088_TABLE6.txt)。MLLM类别语义关系与classifier prediction共同选新标签，冻结classifier朝新类/离旧类合成noise后训练forget+retain；不是唯一shared/unique因果分离。CIFAR/ResNet18及ViT、10k retain、3/5epochs和4090有限对照支持选择机制；MIA/零forget accuracy不证明记录删除、retrain等价或未知攻击安全。Eq12标记含糊和‘retain accuracy减少50%’与Table6 forget列不符隔离，不补造recipe；教师/retain缓存/噪声/训练成本保留。实际Ch72已将不同substrate与删除证据分账，但欠参数类别重定向的支集选择，root必要源/owner PRE后L358写入有限机制，正文邻接末注POST通过；首句自纠为‘粗暴重定向可能…’，root实际有限回核POST通过。

### [A Data-Driven Dynamic Execution Orchestration Architecture](https://arxiv.org/abs/2602.17119v1)

精确v1 §2–2.2/4.1.1/5/6.1–6.5实际读：[mapping](../_sources/daily-20260221/V3_BODY_2602.17119_MAPPING.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.17119_EVAL.txt)、[容量反侧](../_sources/daily-20260221/V3_BODY_2602.17119_SENSITIVITY.txt)。Row FSM按非零项与消息组织MAC/ACC/flush/bypass，带row identity FIFO协调异步reduction，物理容量不变但有效window可配置。22nm综合/事件cycle模拟、INT8、LPDDR17GB/s与稀疏MLP/attention kernels不是已制造设备或完整LLM质量/SLO。Buffer更大可缓解部分失衡却有管理/最慢行/带宽代价；dense systolic仍合理。ZeD面积9×/12×和预处理条件不一致，不采用端到端倍数。Ch54容量论证欠本地控制/有效scratch分支，root necessary/owner PRE后L614窄写，实际正文/邻接/末注POST通过。

### [TimeOmni-VL: Unified Models for Time Series Understanding and Generation](https://arxiv.org/abs/2602.17149v1)

精确v1 §3.1/4.1–4.2/5实际读：[codec](../_sources/daily-20260221/V3_BODY_2602.17149_CODEC_ONCE.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.17149_EVAL.txt)。按period折grid并给N变量分band，H/N≥f、W≥L/f使渲染不下采样，L含masked区域；896²相对224²面积16倍但约3000视觉tokens不免费。Median/MAD+Std/tanh反变换须原尺度/参数/布局，饱和与有限precision不授浮点lossless，零尺度是未披露处理边界。Bagel7B/8A100，构造每task40k但只用5k，valid/extractable输出条件评价、SR<10%不报告；CoT消融同时冻结理解模块并关推理，不识别单因果。Ch23 shape≠semantics后欠finitecanvas/normalizationmetadata容量接口，root必要源/owner PRE已授，L48实际窄写且作者顺读正文/完整邻接/自身末注；root实际正文/完整邻接/自身末注POST通过。

### [LLM4Cov: Execution-Aware Agentic Learning for High-coverage Testbench Generation](https://arxiv.org/abs/2602.16953v1)

精确v1 §3.1–3.4/4.1–4.4/AppendixB实际读：[核心](../_sources/daily-20260221/V3_BODY_2602.16953_METHOD.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.16953_EVAL.txt)、[配置](../_sources/daily-20260221/V3_BODY_2602.16953_CONFIG.txt)。从student drafts选困难/failed状态，teacher或后续student修复后按Δcoverage筛转移，stage离线SFT；失败是input不必是target。Figure5固定drafts/simcalls/SFTpoints支持优先级，stage-vs-mixed不证明全训练预算相同。83 CVDP repository/三rounds/n5、57kSFT points/420k simulatorcalls/72GPUh有限；全repo+draft+feedback的memoryless充分性非任意Agent规律，coverage不等bug correctness。正文8A100与yaml num_devices4冲突隔离，部分stage/direct平均coverage和agent Pass5退步不删。Ch29恢复教师轨迹后欠慢反馈预算的student状态选择，root necessary/owner PRE后L160窄写，实际正文/邻接/末注POST通过。

以上四项same-ID exact-v1与DataCite原字段均实际读：Submitted分别为17088 Feb19T05:20:31Z、17119 T06:43:37Z、17149 T07:50:11Z、16953 Feb18T23:36:46Z；按官方schedule最早公告下界Feb20 BJT09与同身份Registered（分别02:42:43Z/02:43:31Z/02:44:13Z/02:39:32Z）加一秒精度上界，区间全部落窗。Submitted/Created/Updated不是公开时间，不补造actual公告，预计24h并非保证；旧家族artifact不移动论文日期。元数据见本日各ID的V3_PRIMARY abs/datacite原记录。

### [Automating Agent Hijacking via Structural Template Injection](https://arxiv.org/abs/2602.16958v1)

METHOD/SEARCH/PROXY_CORE §3–5.3及Algorithm2、EVAL/INTERP_LIMIT §6–7实际读。TaE18k/2k/50epochs与BO100预算未全面匹配基线；proxy Round3/(Round2+3)丢invalid是条件人口。Force-tokenization99.99%与去bracket.05%支持形式敏感，不证明parser权限或attention唯一因果；942产品/70漏洞与遮蔽CVE只作者声明。实际Ch72权限/external provenance缺template伪历史分层，root必要原源/owner通过后L1233写，完整邻接/末注POST通过，不授充分防御。 必要原源定位见[核心](../_sources/daily-20260221/V3_BODY_2602.16958_METHOD.txt)与[本日实际停点](../_sources/daily-20260221/V3_SCREENING.md)。

### [Greedy Multi-Path Block Verification for Faster Decoding in Speculative Sampling](https://arxiv.org/abs/2602.16961v1)

METHOD §3–5、PROOF_C Eq66–75/PROOF_D Eq76–83、GBV Eq28–29/Alg1、EVAL §6–6.4实际读。选择多IID path使proposal为q^Γ；LP最优限prefix+one correction class，GBV greedy不全局最优。Def5.2 injective与p/q可tie冲突：L1/K2/p=q=(.5,.5)， literal严格小于式两项各.25总.5；未经一致tie policy不得采全域exact recipe。OPT/A100/B1/L8/temp1 K4接受增而walltime退，Qwen/Llama温度1进度也退，低温取舍反向。完整精度/length/concurrency/SLO未披露。Ch48原draw-order/tie分账缺选后完整proposal；root必要独核后L263窄写，POST通过。 必要原源定位见[核心](../_sources/daily-20260221/V3_BODY_2602.16961_METHOD.txt)与[本日实际停点](../_sources/daily-20260221/V3_SCREENING.md)。

### [Early-Warning Signals of Grokking via Loss-Landscape Geometry](https://arxiv.org/abs/2602.16967v1)

METHOD §2–3/5.1、INTERVENTION §5.4–8.4、LIMIT §8.4–9实际读。SGD commutator η1e-3/float32不同于实际AdamW+clip；全轨迹PCA和包含未来tgrok的拟合不是在线预警。SCAN13run/12grok而11双onset，少LR单seed；project后SCAN/Dyck仍grok，投影/惩罚改变多种更新成分，不能建立普遍必要性。局部intervention负结果保留，Ch28 L1263–1265已有probe可读≠信息/质量边界，不强造gap。root必要源/owner独核允许中心终态隔离：重开需真正optimizer-state probe、独立在线检验和matched干预；不入Books，不授定律。 必要原源定位见[核心](../_sources/daily-20260221/V3_BODY_2602.16967_METHOD.txt)与[本日实际停点](../_sources/daily-20260221/V3_SCREENING.md)。

### [DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.16968v1)

METHOD §3/Eq1–4、SCHEDULER Eq5/4.1、EVAL §4.1–5/T2–4实际读。多patch embed/deembed/pos及FFN rank32LoRA teacher蒸馏后，历史latent第三差分variance percentile选择每step一个global patch-size；scheduler无训练不等pipeline无训练。FLUX1024²/Wan480×832×81/50steps局部，VBench81.24→80.97→80.53、DrawCLIP退；3.52×含TeaCache不单因果。T4 τ.004速度1.88低于τ.001的2.18而CLIP更高，阈值非单调；human61/22/17无N/rater，hardware/precision/B/trainsteps/SLO未披露。Ch24动态guidance缺执行token-grid差额，rootPRE后L1110实际写，完整邻接/末注POST通过。 必要原源定位见[核心](../_sources/daily-20260221/V3_BODY_2602.16968_METHOD.txt)与[本日实际停点](../_sources/daily-20260221/V3_SCREENING.md)。

### [Beyond Chunk-Then-Embed: A Comprehensive Taxonomy and Evaluation of Document Chunking Strategies for Information Retrieval](https://arxiv.org/abs/2602.16974v1)

METHOD §3–4.3、CONTEXT §4.4/T4必要行/Findings1–4/4.5实际读。contextual encode→span pool在跨文档MaxP与同文档chunk竞争可平均反转；T4 Jina semantic GutenQA+4.56%、E5+.01/+1.95反例否证全部下降。8192 vs512窗口及GutenQA overlap-DCG vsBEIR doc-nDCG不同；chunk-size相关非控制证明，主题相似仅假设。速度缺完整hardware/APIcost不作RAG SLO。Ch76 ingestion身份缺pre/post编码×竞争人口差额，rootPRE后L57写，完整邻接/末注POST通过，原span引用与旧paragraph/independent encode共存。 必要原源定位见[核心](../_sources/daily-20260221/V3_BODY_2602.16974_METHOD.txt)与[本日实际停点](../_sources/daily-20260221/V3_SCREENING.md)。

### [Fail-Closed Alignment for Large Language Models](https://arxiv.org/abs/2602.16977v1)

METHOD §3/Alg1、EVAL §4.1–4.5、CONFIG_FIX A1/A2/B1/T3、COST_FIX AppendixC实际读（原CONFIG/COST误TOC不用）。每轮current model寻RDO direction，QR维护累积span，harm samples移除旧span再拒答训练，benign原表示+KL（Llama2部分teacherSFT）。SFA/MFA消融支持有限复用反侧，linear independent≠因果独立/所有非线性路径。10iter/B32/8A40或8H100，checkpoint50heldout与200prompt/HarmBenchjudge；50XSTest+1000Alpaca keyword CR非语义安全，A2只明确selection attacks来源。T3 Llama3 RDO ASR17>CAT13.5不全优，2F+2B不完整search/token费。Ch72原refusal/deletion区别缺累计span支持域，rootPRE后L2449写，旧限制→累计训练→operator audit顺读及末注POST通过，非确定default-deny。 必要原源定位见[核心](../_sources/daily-20260221/V3_BODY_2602.16977_METHOD.txt)与[本日实际停点](../_sources/daily-20260221/V3_SCREENING.md)。

六项exact-v1及same-ID DataCite原字段已实际读：Submitted依次Feb18T23:52:14Z/23:55:01Z、Feb19T00:14:36Z/00:15:20Z/00:27:15Z/00:33:35Z，Registered依次Feb20T02:39:39Z/43Z/51Z/53Z/02:40:01Z/06Z。按官方schedule下界Feb20 BJT09、DOI仅公告后流程与同身份Registered+1秒精度上界作完全落窗有界推定；不是Submitted/Created/Updated即public，不补造actual公告。24h为预计不是guarantee，各原字段保留本日V3_PRIMARY abs/datacite。

### [Discovering Universal Activation Directions for PII Leakage in Language Models](https://arxiv.org/abs/2602.16980v1)

精确v1 §3–6/T1–2、AppendixA实际读：full-weight attacker自生20万条256-token文本、PII-only NLL优化direction，再first-token注入；发现类别方向不需已知secret，却必须用已知Enron/TREC训练记录独立匹配。baseline各20万extraction不含额外自生成/优化完整预算；BOS15/18、PI12/18非全优，小集及embedding载体/utility有反退。GPTNeo/Phi2/Llama3-8B、8A40/较大微调12H100限原配置，未披露项不补猜。实际Ch72 L492/末注L3132补自生proposal与secret truth分权，root必要原源/owner PRE通过、实际POST通过。必要原源定位及具体反侧见[本组六项笔记](../_sources/daily-20260221/V3_NECESSARY_16980_17037.md)。

### [Fundamental Limits of Black-Box Safety Evaluation: Information-Theoretic and Computational Barriers from Latent Context Conditioning](https://arxiv.org/abs/2602.16984v1)

actual Def2.7/2.9、Lemma3.3、Theorem4.1与§5–6已读。Passive IID两点不可区分界须eval/deployment trigger分离；同v1 abs与body adaptive界不同。Lemma3.3任意重复查询后仍条件hit概率ε不成立；singleton反例只针对§5实际hash构造，其未逐h强制§2.7，不声称反驳所有另加trigger-separation条件的class。no-hit也不保持safe/unsafe后验1/2。§7/8全部证明未审，不授其保证；Ch66分布不变量已有具体承载，不能强造gap。root必要原源/owner独核允许中心终态隔离：恢复需一致exact-version主张、合法adaptive假设/后验和hash构造与trigger-separation桥。不入Books，不授所有黑箱必不可能。[必要原源位置](../_sources/daily-20260221/V3_NECESSARY_16980_17037.md)。

### [Dynamic Delayed Tree Expansion For Improved Multi-Path Speculative Decoding](https://arxiv.org/abs/2602.16994v1)

actual §4–6/T4–7、AppendixE Eq8–12/footnote4：共享L1 trunk后在其prefix下独立采K条L2，selector只选有限三元组；target/draft previous features可取，当前target root缺KV需贵forward，原接口只额外draft forward。warmup/四次验证标签/MLP费用不省，surrogate不等生产SLO或dataset/temp oracle免费。2A10080G/Xeon12core、三target/draft pair及50×五tasks×八temperatures，precision/长度/B/concurrency Not Disclosed；有BE/TPS反退，T7 Llama14.27<14.77不全胜。actual Ch48 L265/末注1023已写，rootPRE通过、POST通过。[必要原源位置](../_sources/daily-20260221/V3_NECESSARY_16980_17037.md)。

### [Arcee Trinity Large Technical Report](https://arxiv.org/abs/2602.17004v1)

只SMEBU臂。actual §2.3 Eq15–28、§3.3/T2与§6：平均load归一误差→tanh→update中心化→momentum EMA→bias；bias只选TopK，output gate不加bias。Large400B/13Bactive、17T/2048B300不是与Nano/Mini matched control。报告明确SMEBU、BF16、zloss修复、auxloss、denseprefix与mask六项联合且无ablation，不把稳定/速度归单控制律。infer FP8/vLLM/8H200但length/B/concurrency未披露，不采用泛吞吐。actual Ch21 L449/末注927已写，state/reset只工程边界，rootPRE通过、POST通过。[必要原源位置](../_sources/daily-20260221/V3_NECESSARY_16980_17037.md)。

### [WS-GRPO: Weakly-Supervised Group-Relative Policy Optimization for Rollout-Efficient Reasoning](https://arxiv.org/abs/2602.17025v1)

actual §3.2/3.3 Algo1–2/Eq6–7、A3 Eq93–94/A4/A5及T1：full outcome pair的first-preferred定义，与正奖励P(oldprefix,newprefix)方向冲突；A3有[3,6]长度罚/归一而Algo2sum未统一。所有prefix score仍聚合为标量RiWS，再同advantage广播全trajectory，不能称逐step信用或online stop。T1八accuracy低于对应最佳baseline，个别token成本反增；A5 prefix排名不是continuation因果。额外约85k RM pairs/FlanT5+MLP512和G8训练不免费，hardware/precision/总steps/完整预算Not Disclosed。root必要源/Ch33 scalar与local信用实际覆盖独核，中心recipe终态隔离；恢复须统一preferred-role、aggregate/罚项与代码身份，再核matched质量/成本，不为保证遍历A1全部证明。[必要原源位置](../_sources/daily-20260221/V3_NECESSARY_16980_17037.md)。

### [Wink: Recovering from Misbehaviors in Coding Agents](https://arxiv.org/abs/2602.17037v1)

actual §3.1–3.3/4.1–4.4/T3–6/5：每五steps异步observer读recorded snapshot，ready后action后system-reminder交付，mainloop不阻塞；提醒非tool/policy authority，staleness检查仅工程要求。Meta15day50/50AB，triggered 10,554 trajectories由LLM judge15poststeps判同pattern消失+progress，不等全部task correctness；711/759 shadow轨迹含3864/4168 invocations相关，不授独立cluster因果。time−4.3% p.073非显著，Meta-only/同时实验与observer完整成本/ABNs未披露。actual Ch80 L176/末注360已写，rootPRE通过、POST通过。[必要原源位置](../_sources/daily-20260221/V3_NECESSARY_16980_17037.md)。

本组六项same-ID v1 Submitted原字段依次2026-02-19T00:39:12Z/01:03:11Z/01:41:58Z/01:58:50Z/02:43:35Z/03:15:00Z，Registered依次2026-02-20T02:40:10Z/16Z/29Z/44Z/02:41:14Z/30Z；官方schedule与DOI公告后可得流程给完全落窗的半开推定区间。17037后来v2 Submitted本窗但未见本窗公开字段，不把Submitted作修订公告；不扩无关版本。所有原字段保留本日V3_PRIMARY abs/datacite。

### [Phase-Aware Mixture of Experts for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.17038v1)

精确v1 Phase-Aware Router/Temporal Consistency、Tables2–4、Appendix B/C实际核。近五步LSTM和硬选LoRA expert形成learned连续expert-run，不是runtime显式phase标签；single pooled K/V与正温度hardargmax不采宣传因果，STE只是梯度代理。45 intra-action与8.4相邻env-step分母不同，K6退步、容量和总费用不独立。actual Ch21 L560–562纠正原两段，note970；root必要原源/owner与实际POST通过，未核实现/复现。[原源定位/训练配置及反侧](../_sources/daily-20260221/V3_NECESSARY_17038_17080.md)。

### [Amber-Image: Efficient Compression of Large-Scale Diffusion Transformers](https://arxiv.org/abs/2602.17047v1)

精确v1 §2/Eq1–4/Algorithm1、§2.1.3–3.4/Table1实际核。权重平均不等复合函数；删层后cluster-end targets局部→全局恢复，再single-stream拼接teacher对齐，联合变化不归单因果。OneIG style/diversity退、内部数据/teacher/calibration与1872训练GPUh完整保留，不授全指标或部署加速。actual Ch24 L1121/ownnote2049接student与训练/部署表示，root必要原源/owner及实际POST通过。[必要配置/反侧](../_sources/daily-20260221/V3_NECESSARY_17038_17080.md)。

### [RFEval: Benchmarking Reasoning Faithfulness under Counterfactual Reasoning Intervention in Large Reasoning Models](https://arxiv.org/abs/2602.17053v1)

精确v1 §2/Defs2.1–2.5/Eq1–6、§4.1/5/Tables2–4、A/A4实际核。输出前缀行为proxy不是内部推理；baseline立场与注入相反才valid，使人口随model变化，coverage非最终valid率。组件judge人审验证不授internal faithful，合理拒绝错premise而无答案变化不能直接判不忠实。Olmo SFT反退、未matched posttrain预算、低相关CI跨零不授独立性。actual Ch66 L861/note5542已写并root实际POST通过；所有生成/长输出/标注费用不省。[必要原源/配置](../_sources/daily-20260221/V3_NECESSARY_17038_17080.md)。

### [Sign Lock-In: Randomly Initialized Weight Signs Persist and Bottleneck Sub-Bit Model Compression](https://arxiv.org/abs/2602.17063v1)

精确v1 §3 bounded/re-entry条件、§4/C4与E3.1–3.6实际核。全局seed的sign template依赖gap初始化与每step硬投影，再压幅度；sign(GHᵀ)非低秩保证、SVD负幅度/clamp不可忽略。14/28target tensors的近似bpw非seed/metadata/未压缩层/物化全费用；恢复预算及gap/正则联合不授单因果。actual Ch49 L985/note2728具体格式差额深入，root必要原源/owner及实际POST通过，未核kernel/复现。[必要原源/实验配置](../_sources/daily-20260221/V3_NECESSARY_17038_17080.md)。

### [Predictive Batch Scheduling: Accelerating Language Model Training Through Loss-Aware Sample Prioritization](https://arxiv.org/abs/2602.17066v1)

精确v1 §3–5/Table1与§6–7实际核。历史per-sample loss拟合cheap线性特征，再采样q；无额外candidate-forward非零费用或原分布无偏。Nh2000/10000冲突不采确定recipe，相关性非单调、130M短训练loss差非同目标墙钟或memorization因果，dataset/hardware/具体dtype/多seed未披露不补造。actual Ch27 L166/note1524采样控制差额深入，root必要原源/owner及实际POST通过。[必要源/反侧](../_sources/daily-20260221/V3_NECESSARY_17038_17080.md)。

### [Adam Improves Muon: Adaptive Moment Estimation with Orthogonalized Momentum](https://arxiv.org/abs/2602.17080v1)

精确v1 §2 scalar/column/clamp与§4/Tables1–2/§5实际核。Orth后scalar保相对几何，column right-diag不保严格统一正交；理论exactOrth假设非有限NS实现。GPT2/OWT/4H100指定配置中val-loss局部改善，decay同缩放/不同LR与c搜索共同变化；seed/precision/NS迭数/完整费用未披露，不授统计/加速或完整recipe。actual Ch28 L530/note1771补状态维度/几何差额，root必要原源/owner及实际POST通过。[原源/预算边界](../_sources/daily-20260221/V3_NECESSARY_17038_17080.md)。

六项same-ID v1 Submitted原字段依次Feb19T03:18:30/03:33:41/03:49:37/04:10:05/04:15:39/05:00:39Z，Registered依次Feb20T02:41:32/45/53、02:42:07/11/31Z；官方公告后ID/DOI流程与schedule给表列半开推定区间，不造精确公告。后续版本Submitted不是重要修订或公开本身。原字段均保留本日V3_PRIMARY abs/datacite。

### [FLoRG](https://arxiv.org/abs/2602.17095v1)

精确v1 §3.1/Eq1–12、Algorithm1、§4/T1必要实际读。[必要范围](../_sources/daily-20260221/V3_NECESSARY_17095_17168.md)保留固定L/R的PSD Gram函数类与N2/r1/k2反例：本地(1,0)/(0,1)平均Gram=.5I2，rank1无法精确保留；Eq5允许r′>r，Eq8b要求r×r′的S满足SᵀS=I不可行。root独读ALIGN/THEOREM及Ch30实际坐标/rank段，中心暂缓通过；不自行换成rows-orthogonal冒充作者算法。20clients/r4/GLUE或iidSQuAD/two-seed与通信计数不授统计/全面优势或服务器全成本。重开须同精确实现的合法rank压缩/对齐与误差分析；有限作者经验不授zero-error，也不改写成熟提醒强整合。

### [AudioChat: Unified Audio Storytelling, Editing, and Understanding with Transfusion Forcing](https://arxiv.org/abs/2602.17097v1)

精确v1 §4.1–4.2/Eq10–12、§5.4/T4及B2/C2/D必要实际读。独立turn clocks覆盖clean-history/full-noise-target组合，区别clean条件copy与统一clock；SCT同时改变层接口，架构对照不认证noise单因素收益。3.6B/frozen48kHz40Hzcodec、三阶段100k+100k+20k训练、private/unreleased及150editing/100T2Asteps预算保留，FLAM-preservation只sensor差值、不授音频相等/实时SLO。actualCh24L248/邻接241–253及末注2065经root实际POST通过，有限指标反侧/原单回合路径回退近文。[必要源/owner](../_sources/daily-20260221/V3_NECESSARY_17095_17168.md)。

### [AgentConductor: Topology Evolution for Multi-Agent Competition-Level Code Generation](https://arxiv.org/abs/2602.17100v1)

精确v1 §2.1/Eq1–7、§2.2–3/T3–4及A1–3实际读。YAML layer/ref DAG作为policy行动，graph和execution feedback共同加入H后nextproposal；schema不授代码正确，密度不是墙钟。4500SFT/3B orchestrator/workers/GRPO G8/two-turn/4A800成本及backbone/teacher措辞不全一致保留，组件对照不授任意最优图或安全。actualCh82L872/邻接866–879及自身末注经root实际POST通过；runtime硬权限/验证节点是工程要求，非作者已验保证。[必要源/owner](../_sources/daily-20260221/V3_NECESSARY_17095_17168.md)。

### [VP-VAE: Rethinking Vector Quantization via Adaptive Vector Perturbation](https://arxiv.org/abs/2602.17133v1)

精确v1 §3.1–3.2.4/Eq3–12、§4/Table1–2与必要A2/B1/C实际读。MH确有reverse support/volume ratio，拒绝原值通过；固定估计密度不等移动queue保持真实latent不变量。训练无码本→全训练集encoder→offlineKmeans++/Q→inferNN，上游扰动不保证覆盖实际quant误差。50epochs/2RTX4090/noGAN图像/16kHz音频重建人口，高usage非全部quality，归一化PSNR与LPIPS可反向；kNN/queue/聚类成本与AR/diffusion仍future近文。actualCh23L194/邻接190–201及自身末注经root实际POST通过。[必要源/owner](../_sources/daily-20260221/V3_NECESSARY_17095_17168.md)。

### [Powering Up Zeroth-Order Training via Subspace Gradient Orthogonalization](https://arxiv.org/abs/2602.17155v1)

精确v1 §3–4/Eq5/10–13、§5/T1–2与必要F/G实际读。subspace estimate先orth再lift不是全空间RGE先orth；Prop1要求trueG SVD span不是随机P guarantee。单query丢scalar幅度、多query付费，v1频繁resample有退步；rank/LR/query搜索、非矩阵MeZO及projection/QR/NS预算保留。OPT/Gemma/ViT有限条件与text20k/ZO表8k/4k/2k差别不授全面优于FO，原A100100GB未核字段不当可靠硬件。actualCh28L335/邻接329–343及末注1775经root实际POST通过，锁已释放。[必要源/owner](../_sources/daily-20260221/V3_NECESSARY_17095_17168.md)。

### [BadCLIP++](https://arxiv.org/abs/2602.17168v1)

精确v1 §IV–VI/Assumptions1–3/Th1–2/Eq27–28、必要clean-ft TableV/TableIX/E配置实际读。cos≥0包含零，Eq27 quadratic项可正；ALIGN曲率非total-loss曲率，局部evaluation loss没有ASR行为桥，poison正则不保证后来FT遵守trustregion。root实际BOUND独核中心隔离；TableV CleanerCLIP96.32反驳摘要all19>99.90，10epochs/100Kclean/AdamW LR4.5e-6/batch64只授四受测方案条件残留。TableIX累计组件非全factorial、不授EWC独立因果；0.3%是训练pairs比例非现实prevalence。root实际直接表/配置与Ch72触发邻域/cleanutility/pairedcorrection已有owner独核，中心暂缓，不另计OnlyReport，不用成熟清理原则强改Books。重开须严格alignment/step、total-loss曲率关系与行为桥，不遍历无关19防御附件。[必要源/owner](../_sources/daily-20260221/V3_NECESSARY_17095_17168.md)。

### [When LLM Judges Inflate Scores: Exploring Overrating in Relevance Assessment](https://arxiv.org/abs/2602.17170v1)

精确v1 §3–4实际核：[协议](../_sources/daily-20260221/V3_BODY_2602.17170_METHOD_RESUME.txt)、[有限输入控制](../_sources/daily-20260221/V3_BODY_2602.17170_CONTROL_RESUME.txt)。TREC19/20的human0–3与四LLM、binary/graded/point/pair不同协议，pair每query20对并交换顺序，矛盾被派生为tie而非显式abstain。Forced-token confidence不能自证correct，Llama约.9反驳统一>95%宣传；同Gemini改写/self-check语义只弱控制，LEX/SEM/QRY有限分离不授单因果或所有长度已排除。actual Ch66 L299及427–449已承载confidence不等质量、输入/scorer/顺序的协议身份，root必要原源与owner独核已有覆盖通过，不以新增dataset强改书。

### [Robustness and Reasoning Fidelity of Large Language Models in Long-Context Code Question Answering](https://arxiv.org/abs/2602.17183v1)

精确v1 §3–4实际核：[方法](../_sources/daily-20260221/V3_BODY_2602.17183_METHOD_RESUME.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.17183_EVAL_RESUME.txt)。MCQ选项shuffle与open-answer LLMjudge是不同协议，judge身份/校准未披露；Python generation有限反侧不单独证明shortcut因果。Java114问题×6长度为684场景而非684独立问题，private COBOL不当全公开资产。actual Ch66 L427–449评价人口/顺序、Ch22长度不等利用已有承载最小采用范围，root必要原源与owner独核Existing通过；不授通用长程理解或未核模型排名。

### [Selective Training for Large Vision Language Models via Visual Information Gain](https://arxiv.org/abs/2602.17186v1)

精确v1 §3.2/3.4、Table5与直接配置实际核：[paired CE方法](../_sources/daily-20260221/V3_BODY_2602.17186_METHOD_RESUME.txt)、[监督](../_sources/daily-20260221/V3_BODY_2602.17186_TRAIN_RESUME.txt)、[反侧](../_sources/daily-20260221/V3_BODY_2602.17186_CONTROL_RESUME.txt)。Frozen aligned reference的原图/blur差不是客观MI，Gaussianblur非完全语义absence；完整answer仍输入，loss mask不消除条件历史和梯度影响。Table5 sample-only的58.12/57.56低于full59.02/65.46，否证allwin，SS+TS只局部恢复。双scoring8RTX4090×6h与训练8A100费用近正文。actual Ch29 L140/邻接136–147/末注1304经root实际POST通过；与绝对概率门不同监督proposal差额，不采用current v2改名或把HTML生成日当公开时间。

### [EntropyPrune: Matrix Entropy Guided Visual Token Pruning for Multimodal Large Language Models](https://arxiv.org/abs/2602.17196v1)

精确v1 §3.2–3.5/Eq7–14、同layer2/192tokens Table6与配置实际核：[必要scorer](../_sources/daily-20260221/V3_BODY_2602.17196_METHOD_FIX_RESUME.txt)、[控制](../_sources/daily-20260221/V3_BODY_2602.17196_EVAL_RESUME.txt)。Per-token head中心化/rowL2normalize后，非零行双Gram有相同非零谱；zero-row guard未披露，不造实现。Layer matrixentropy下降非语义贡献，64×是128/32立方eigensolver复杂度比非end2end。A6000/LLaVA受测MME约1.6prefill/1.4latency仍掉4.6分，同层有限控制不授普遍最优；完整前层/scoring/decode成本近文。actual Ch43 L180/邻接175–187/末注516经root实际POST通过，与attentionmass/variance selector不同而非重复‘裁剪有代价’。

### [GASS: Geometry-Aware Spherical Sampling for Disentangled Diversity Enhancement in Text-to-Image Generation](https://arxiv.org/abs/2602.17200v1)

精确v1方法、Prop4.1/Eq9及renormalize和直接费用实际核：[中心原命题](../_sources/daily-20260221/V3_BODY_2602.17200_THEORY_FIX_RESUME.txt)、[实际更新](../_sources/daily-20260221/V3_BODY_2602.17200_GUIDE_RESUME.txt)、[限制](../_sources/daily-20260221/V3_BODY_2602.17200_LIMIT_RESUME.txt)。Eq9是simplex edgeGram的volume，不是pointGram；B2任意球面点命题包含antipodal(e,-e)，初始边长2为球面最大，任何renormalized pair≤2，严格期望增加不可能。原proof从期望cross项非负跳到PSD且缺normalization，root必要原源实际独核中心隔离通过。CLIP轴+N10randomorthogonal meanabs不授语义独立，20guidesteps batch3.68s vs1.71s及CLIP/梯度decoder费用不免费；有限经验仅报告不另计Only。重开须含normalization、退化/最大配置条件的一致命题与实现，不沿早期错误pointGram正交反证。

五项v1 Submitted依次Feb19T08:37:21/09:05:03/09:12:21/09:29:43/09:41:32Z，same-ID Registered依次Feb20T02:44:44/02:45:03/02:45:11/02:45:25/02:45:31Z；官方公告流程/schedule与秒精度上界推定完全落窗半开范围，非Submitted/Registered即精确公告。原字段保留本日V3_PRIMARY abs/datacite，不扩后续版本diff。

### [ReIn: Conversational Error Recovery with Reasoning Inception](https://arxiv.org/abs/2602.17022v1)

精确v1 §3.1/Algorithm1、§4.1–4.2/4.5–4.6与A直接限制实际核：[核心](../_sources/daily-20260221/V3_BODY_2602.17022_METHOD_RESUME.txt)、[评价人口](../_sources/daily-20260221/V3_BODY_2602.17022_CONFIG_RESUME.txt)、[tool条件反侧](../_sources/daily-20260221/V3_BODY_2602.17022_HIERARCHY_RESUME.txt)。外部F在turn开始首control前一次追加think[plan]，No原流程但仍付F调用；不改变原S/params，不授内部写权。Assigned recoverytool与无tool道歉策略0%不同，不能授safer/bypass hierarchy。588合成contexts源自98sessions，首3utterance造错；Claude Sonnet3.7/Haiku3.5 task、Sonnet3.5 user，ambiguous要求新增internalreport+goal，而unsupported原prompt已有handoff，baseline非等能力。Airline/Sonnet有限动态与子集3repeat、taxonomy/用户模拟/额外成本限制近文。actual Ch80 L184/邻接178–192/末注434由root实际POST通过，与async诊断不同而非重复一般retry。

### [IntentCUA: Learning Intent-level Representations for Skill Abstraction and Multi-Agent Planning in Computer-Use Agents](https://arxiv.org/abs/2602.17049v1)

精确v1 §3.1–3.2/Eq3/4/6、§4.1–4.2/§5.1–5.3实际核：[参数schema](../_sources/daily-20260221/V3_BODY_2602.17049_METHOD_FIX_RESUME.txt)、[评价](../_sources/daily-20260221/V3_BODY_2602.17049_EVAL_FIX_RESUME.txt)、[encoder反侧](../_sources/daily-20260221/V3_BODY_2602.17049_TRAIN_RESUME.txt)。IG/SG检索跨trace canonical verb/typedargs→signatureprototype→literal placeholders，partialgap才currentbinding补全，不直接replay。Eq6优化全A*不限定候选，不能认证严格medoid；Eq3正样本排除分母/Eq4反向输入记号不授完整encoder recipe。113traces/30activehours/36domains对286tasks/63domains仅22重叠，binaryapproval非成功，ownplan完成分母非目标成功；Table1累计而非完全factorial，同action/timeouts不授所有backbone预算可比，popup遮挡Critic失败。actual Ch77 L1532/邻接1526–1541/末注2101经root实际POST通过，与fixedadapter不同schema构建/绑定差额；完整生命周期成本与当前权限回退近文。

两项v1 Submitted分别Feb19T02:37:29/03:42:15Z，Registered Feb20T02:41:10/02:41:47Z；按同身份官方流程/schedule与秒精度上界推定完全落窗，不补造actual公告。原字段保留本日V3_PRIMARY；本次未扩v2diff。

### [MDP Planning as Policy Inference](https://arxiv.org/abs/2602.17375v1)

精确v1 §3/Eq7–8、§4.1/Algorithm1、§6必要控制实际核：[中心定义与noisy-log主张](../_sources/daily-20260221/V3_BODY_2602.17375_DECIDING_CORE.txt)、[更新](../_sources/daily-20260221/V3_BODY_2602.17375_METHOD_RESUME.txt)、[有限评价](../_sources/daily-20260221/V3_BODY_2602.17375_EVAL_RESUME.txt)。Uniform deterministic-policy prior下log unnormalized density=expected return，与加入action entropy的目标不同；firstvisit固定action/shared transition tensor可见，但单episode return对log无偏不推出其exp对density无偏。单步A恒.1、B等概率±1，expER的相对质量e^.1/1，而EexpR为e^.1/cosh1，independent noise/shared draw均不自行补target bridge。Root必要原源独核中心争议通过，不宣告整个算法错误；Th1关于其scalar objective梯度不能自动证明该objective是Eq7 posterior。10particles/50k sweeps、SAC1Msteps/width64、25runs/10ktrajectory限grid/Blackjack/Tireworld/Advising，不授同成本或通用最优。Ch32 entropy目标实际owner比较未构成另写成熟提醒的增量。重开须同目标合法非负density估计/一致推断或显式承认替代目标及对应控制，不遍历全部证明或窗外版本。

### [What Do LLMs Associate with Your Name? A Human-Centered Black-Box Audit of Personal Data](https://arxiv.org/abs/2602.17483v1)

精确v1 §3.1–3.3.3及必要A7实际核：[核心query](../_sources/daily-20260221/V3_BODY_2602.17483_METHOD_FIX_RESUME.txt)、[协议](../_sources/daily-20260221/V3_BODY_2602.17483_CONFIG_FIX_RESUME.txt)、[同模型控制](../_sources/daily-20260221/V3_BODY_2602.17483_VALIDATION_RESUME.txt)。黑箱完整canary echo混入指令效应→2char/digit fragment-completion、generic-subject baseline、五句式/20prefix竞争；有logprob与topvote是不同observer，集中度非correct/membership。8model/100famous+100synthetic不能识别真实training身份，prefix仍条件信息且长值截头。主评MiniLMcos.60与A7.75不同；同Llama3.1-8B raw/chat总体47.44→53.50%但birthplace/occupation反退、更phrase-sensitive，非等价认证。query预算/身份治理与fallback近正文。Root必要原源/actualowner PRE后，Ch72 L293/邻接285–301/末注4230实际POST通过，只采用query接口差额，不扩56页human调查/政策建议。

两项v1 Submitted分别Feb19T13:56:31/15:53:29Z、Registered Feb20T02:49:41/02:52:15Z；按same-ID官方schedule与公告后DOI流程/秒精度上界推定半开完全落窗区间，非精确actual公告。字段保留本日V3_PRIMARY，不比较窗外后续版本。

### [Algorithmic Collusion at Test Time: A Meta-game Design and Evaluation](https://arxiv.org/abs/2602.17203v1)

精确v1 §3.2–3.3/§4.4–4.4.1/Table4实际核：[meta-game方法](../_sources/daily-20260221/V3_BODY_2602.17203_METHOD_RESUME.txt)、[adaptation接口](../_sources/daily-20260221/V3_BODY_2602.17203_ADAPT_RESUME.txt)、[LLM控制/限制](../_sources/daily-20260221/V3_BODY_2602.17203_LLM_RESUME.txt)。固定prompt+更新history组成test-time策略，成对payoff/NE-regret条件化候选集合，与固定policy mutation不同。六GPT5-mini/四价格/API离散化/40初态/t50不预测开放现实collusion，旧模型停用不能复制旧结果；uniform-opponent收益非无有利偏离。actual Ch82 L354/邻接348–360/末注1305经root实际POST通过；矩阵估计/模拟/API成本与原小组/外部规则近正文。

### [MGD: Moment Guided Diffusion for Maximum Entropy Generation](https://arxiv.org/abs/2602.17211v1)

精确v1 §3.1–3.2/Eq12–21、§4.1、§5.1.1–5.1.2实际核：[SDE/Gram](../_sources/daily-20260221/V3_BODY_2602.17211_METHOD_RESUME.txt)、[猜想边界](../_sources/daily-20260221/V3_BODY_2602.17211_THEORY_RESUME.txt)、[同分布φ反侧](../_sources/daily-20260221/V3_BODY_2602.17211_EVAL_RESUME.txt)。moment-preservation需初始匹配/耦合解存在，Gram奇异会blowup，有限particle/步长不继承连续解精确；p*是所选moments下maxentropy非pdata，θ∇φ非真实瞬时score。一般σ→∞速率是Conjecture4.1，非已证普效；同bimodal变φ可使接近目标噪声σ²约2→500及约100倍积分成本。actual Ch24 L184/邻接180–192/末注2081经root实际POST通过，成本/建模与采样误差分责，不扩领域效用或所有存在性证明。

### [Privacy-Preserving Mechanisms Enable Cheap Verifiable Inference of LLMs](https://arxiv.org/abs/2602.17223v1)

精确v1 ThreatModel/§4–5、Appendix E/F必要接口实际核：[威胁/Protocol1](../_sources/daily-20260221/V3_BODY_2602.17223_METHOD_RESUME.txt)、[Protocol2](../_sources/daily-20260221/V3_BODY_2602.17223_PROTOCOL2_RESUME.txt)、[正式返回/验证](../_sources/daily-20260221/V3_BODY_2602.17223_FORMAL2_FIX_RESUME.txt)。sentinels与prompt互不attention；Protocol1承认leave-one-out pass N/(N+K)，不是完整计算保证。正式Alg5逐token独立noise，与实际§5.3/AppF每sequence同一b不同；Alg6只cache-match sentinels及NP(h[j])==b，无非sentinel的position/input绑定。在实际shared-b且原honestaccepted结果上，复制两个不同随机输出位置的合法encrypted h，若二者非sentinel则全部noise check仍通过、输出却改变；N256/K3不碰sentinel概率约.977，不由隐藏b给1/100 soundness。root必要原源独核中心隔离通过，只针对shared-noise未绑定接口，不称独立noise方案被该反例击破、复制能节省计算或破所有隐私机制。99%honest分类/约3.43log-loss不是adversarial soundness；trusted cache、每model训练、privacy overhead/投影与总费用不免费。重开须实际配置一致的输入/位置绑定及对允许返回变换的soundness分析，不扩全部SMPC/TEE附录，不改书为成熟提醒。

### [All Leaks Count, Some Count More: Interpretable Temporal Contamination Detection in LLM Backtesting](https://arxiv.org/abs/2602.17234v1)

精确v1 §4.1–4.3/§6.3–6.4/Tables3–4/B1实际核：[claim/公开日期方法](../_sources/daily-20260221/V3_BODY_2602.17234_METHOD_RESUME.txt)、[scorer/config](../_sources/daily-20260221/V3_BODY_2602.17234_EVAL_RESUME.txt)、[同模型一致反侧](../_sources/daily-20260221/V3_BODY_2602.17234_FAITHFUL_RESUME.txt)。earliest-public-verifiable不是句内事件日，含糊日期取上界非精确firstpublic；subset re-prediction的Shapley代理非原隐藏过程因果，零absweight分母未披露guard。同ClaudeSonnet4抽取/重新预测与100MC排列、Perplexity最多5搜索/一次再生都计费；B1能重现original不证明faithful。stock leakage .171→.001同时ρ .543→.167，非无损纠正或金融能力，datefilter不删除parametricfuture。actual Ch66 L3108/邻接3100–3116/末注5588经rootPOST通过。原exact-v1题名无后版metadata的“and Mitigation”，不把改名当新事件。

### [Trivance: Latency-Optimal AllReduce by Shortcutting Multiport Networks](https://arxiv.org/abs/2602.17254v1)

精确v1 §2.1–2.3/§4.1–4.2/§6.1–6.2实际核：[双端口传播](../_sources/daily-20260221/V3_BODY_2602.17254_METHOD_RESUME.txt)、[费用模型](../_sources/daily-20260221/V3_BODY_2602.17254_MODEL_RESUME.txt)、[SST控制/反侧](../_sources/daily-20260221/V3_BODY_2602.17254_EVAL_RESUME.txt)。±3^k peers使覆盖三倍；n3^s全vector1phase log3n rounds与RS→AG2log3n不同bytes/延迟取舍，不照录疑似per-nodebytes计数。critical path每步chunk×congestion不等全网forwardbytes。SST800Gb/s/100nslink+hop/1.5μs step、32B–128MiB；recursive-doubling补足2Dports，Bruck shortestpath/reorder控制，ring512KiB后Swing、4MiB后Bucket反勝。不是真实NCCL生产/全训练提速；actual Ch36 L189/181–200/末注2094经rootPOST，端口/归约/调度与原路径回退近正文。

### [FRAPPE: Infusing World Modeling into Generalist Policies via Multiple Future Representation Alignment](https://arxiv.org/abs/2602.17259v1)

精确v1 §3/§4.1–4.3/Table1–3实际核：[teacher/adapter接口](../_sources/daily-20260221/V3_BODY_2602.17259_METHOD_RESUME.txt)、[同20k与推理成本](../_sources/daily-20260221/V3_BODY_2602.17259_CONTROL_RESUME.txt)。每frozen teacher对应futureprefix+LoRA、sharedbackbone→weightedlatent actionhead，部署不读真实future/teacher。两RoboTwin任务同20k直接post-only比RDT差，mid→prefix-only44.8<mid45.3，配套LoRA52.3只有限配置；不是全分支同walltime。Eq3 cosine loss符号不授exactrecipe；Eq6(logsumexp g)²不保证balancedprobs，令g=logp可任意peaked而零loss；Eq7非零gate不授必有gradient。RDT1B/RoboTwin/singleH100/5steps内存3.7→8.0GB、latency.214→.235sec，precision/inferencebatch/concurrency/tailSLO未披露，3steps比较不等同5steps预算。actual Ch26 L399/391–405/末注1918由root补读条件后POST通过，不扩realrobot/human co-training效果。

六项v1 Submitted依次Feb19T09:47:55/10:03:03/10:15:51/10:28:00/10:57:16/11:00:46Z；same-ID Registered依次Feb20T02:45:35/02:45:46/02:46:03/02:46:18/02:46:47/02:46:53Z。按官方公告schedule与公告后DOI登记的秒精度+1秒上界推定，整个半开区间完全落窗；不以Submitted/Created/Registered冒充actual公告时刻。原字段保留本日V3_PRIMARY abs/datacite，不作后版diff。

### [LexiSafe: Offline Safe Reinforcement Learning with Lexicographic Safety-Reward Hierarchy](https://arxiv.org/abs/2602.17312v1)

精确v1 §4/Algorithm1、Eq7/9/10–12、Lemma4.2与§5/Table2实际核：[policy更新原式](../_sources/daily-20260221/V3_BODY_2602.17312_METHOD_RESUME.txt)、[有限评价人口](../_sources/daily-20260221/V3_BODY_2602.17312_EVAL_ACTUAL_RESUME.txt)。同一policy先成本再奖励的接口通过准入，不因CPS例子排除一般learning机制；但Eq12是正权重乘logπ，Eq11明确gradient descent，与reward maximization不一致。固定单state/twoactions、λ=0、reward-good权重更高时，原loss随good概率趋零仍可趋负无穷，不能擅补minus号当作者已实现。Eq7/9与10/12也不一致，Lemma4.2仅concentrability/VC条件未提供L2→sup所需最小质量覆盖。DSRL simulator子集、MLP128/Adam/batch2048，5训练seed×10run×5测试seed为250trajectories而非250独立模型；normalized mean cost<1是有限feasibility代理，不是每轨迹安全或证明符号已解决。root已独核原式与两action反例，中心争议终态隔离；不授安全typedpolicy、sample-complexity或把成熟cost-first流程强行写书。重开需一致policy-update原式或与原式对应的实际实现，以及sup误差界的必要coverage条件；不遍历其他领域实验。v1 Submitted Feb19T12:22:50Z、same-ID Registered Feb20T02:48:10Z支持半开公开推定上界BJT10:48:11，非精确公告，原字段保留V3_PRIMARY。

### [NotebookRAG: Retrieving Multiple Notebooks to Augment the Generation of EDA Notebooks for Crowd-Wisdom](https://arxiv.org/abs/2602.17215v1)

精确v1 §4.2.1–4.2.4/Table1、§4.3–4.4、§6.5/7实际核：[AST/data-variable核心](../_sources/daily-20260221/V3_BODY_2602.17215_DECIDING_CORE_RESUME.txt)、[current-data执行接口](../_sources/daily-20260221/V3_BODY_2602.17215_RUNTIME_RESUME.txt)、[匹配评价与限制](../_sources/daily-20260221/V3_BODY_2602.17215_EVAL_FIX_RESUME.txt)。提取目标cell依赖的create/mutate/use语句并保持原执行序，nonlinear需完整executionlog；未知库mutation不由AST自证完整，sandbox也不由宣称获得安全。840配对cell/component used-column标注同模型改善，charttype差异不大；不证明完整notebook的总体收益唯一归于closure。固定prompt限制ChatGPT、RAGbaseline非EDA定制，reproducibility评分无显著差；300components约3分钟/12子任务约10分钟仅offline作者负载，gpt5mini/VLM、gpt5nano/textcode、semanticembedding+FAISS和debug均计费，precision/concurrency/tailSLO未披露。actual Ch76 body57/49–67/ownnote1539经root实际POST；原数据事实、来源链接与回读完整notebook退路近文。v1 Submitted Feb19T10:07:11Z、Registered Feb20T02:45:51Z支持上述完全落窗半开范围，不作actual公告时间。

### [Web Verbs: Typed Abstractions for Reliable Task Composition on the Agentic Web](https://arxiv.org/abs/2602.17245v1)

精确v1 §3.1/4.1、§4.3/Table1与§6实际核：[开发者封装/提案](../_sources/daily-20260221/V3_BODY_2602.17245_DECIDING_CORE_RESUME.txt)、[有限任务对照](../_sources/daily-20260221/V3_BODY_2602.17245_EVAL_ACTUAL_RESUME.txt)、[兼容/权限open问题](../_sources/daily-20260221/V3_BODY_2602.17245_LIMIT_ACTUAL_RESUME.txt)。record→debug→参数化Playwright函数仅有限13网站原型，currentlocator偶然稳定非publicABI；stable-public-locator breakingchange与domainownednamespace是网站接口责任proposal，非已标准化/安全/广部署。100任务人工核验与10代表baseline不是统一population，2.7–8.3x只successsubset且非完整开发/回归维护费用，不采用普适可靠性/端到端成本；permission仍open。actual Ch78 body55/47–66/ownnote923经root实际POST，typedwrapper不授执行权、rawGUI/API fallback近文，不重复Ch77技能memory。v1 Submitted Feb19T10:50:52Z、Registered Feb20T02:46:33Z支持完全落窗半开范围；原v1title为Web Verbs，当前DataCite/v2改名不另算家族，不做无关版本diff。

### [Unified Latents (UL): How to train your latents](https://arxiv.org/abs/2602.17270v1)

精确v1 §3/Alg1–2、§5.1–5.6/Table2、§6.1实际核：[noise/prior/decoder方法](../_sources/daily-20260221/V3_BODY_2602.17270_METHOD_RESUME.txt)、[必要同family评价](../_sources/daily-20260221/V3_BODY_2602.17270_EVAL_RESUME.txt)、[直接限制](../_sources/daily-20260221/V3_BODY_2602.17270_LIMIT_RESUME.txt)。fixednoisez0与旧prior/新base最大logSNR共同匹配，encoder/decoder冻结后重训base；这只是conditional-distribution接口匹配，未有独立端点失配/适配收益控制，不为实现描述另添正文。原Eq3prior用−dλ/dt，Eq4与Alg1decoder却用+dλx/dt乘非负MSE；前向由高SNR到noise的递减λ会使原decoderloss为负，不能擅补号或由此授ELBO/真实bits保证。Table2 LF1.3→2.1时PSNR25.7→30.1但smallgFID1.42→2.38，medium非单调，是有限重建与容量经验而非central公式已修。Ch23 actual261–273 rate↔distortion↔basecapacity↔decoder费用及1156/1159 UL已承载此独立经验；Fig4明确排除AE训练FLOPs，§6.1还承认diffusiondecoder约一量级sampling更贵，AE数据差异/未披露完整hardware、precision、batch/concurrency与tailSLO不授E2E普遍更便宜。root实际必要原式与owner独核，6分centralDisputed终态、无Books修改；有限已有覆盖不等整篇理论通过。重开需作者一致decoderobjective/更新实现与相应ELBO依据，不扩AppendixB或视频实验。Submitted Feb19T11:18:12Z、same-ID Registered Feb20T02:47:09Z支持上述完全落窗半开推定，非精确公告。

### [Efficient privacy loss accounting for subsampling and random allocation](https://arxiv.org/abs/2602.17284v1)

精确v1 §2.2/3–5、Theorem4.4/4.6及必要Alg1/2与误差proof实际核：[随机化条件](../_sources/daily-20260221/V3_BODY_2602.17284_SETUP_RESUME.txt)、[exp/dual PLD方法](../_sources/daily-20260221/V3_BODY_2602.17284_METHOD_RESUME.txt)、[数值算法](../_sources/daily-20260221/V3_BODY_2602.17284_RA_ACTUAL_RESUME.txt)、[必要误差界](../_sources/daily-20260221/V3_BODY_2602.17284_PROOF_BOUND_RESUME.txt)、[有限数值反侧](../_sources/daily-20260221/V3_BODY_2602.17284_EVAL_RESUME.txt)。每步/partial-view同dominating randomizer与独立copies是适用条件，k>1 reduction可能lossy；allocation不是普通loss卷积，remove/add的exp/dual与−log变换要求不同round方向，初始tail预算β/t和再离散α/(2ceil(log2t)+1)不能省略。均匀FFT在exp-loss范围下昂贵、float64累积与小epsilon反退近文；不授训练utility、所有无放回精确或生产普遍胜。actual Ch72正文534/527–550/ownnote4238已root独立POST，保守匹配RDP/PLD回退与release声明停止条件完整。Submitted Feb19T11:44:25Z、same-ID Registered Feb20T02:47:30Z支持上述完全落窗半开推定，非精确公告。

### [Representation Collapse in Machine Translation Through the Lens of Angular Dispersion](https://arxiv.org/abs/2602.17287v1)

精确v1 §2.1/Eq2–3、§2.3/3/Eq7–9、§4.1–4.2/4.5/Table3与直接限制实际核：[continuous loss](../_sources/daily-20260221/V3_BODY_2602.17287_CONTINUOUS_RESUME.txt)、[正则与配置](../_sources/daily-20260221/V3_BODY_2602.17287_METHOD_RESUME.txt)、[同初始化对照](../_sources/daily-20260221/V3_BODY_2602.17287_EVAL_RESUME.txt)。Categorical候选竞争不同于1−cos(E_y,H)仅同向匹配，共同移动目标与预测器全同方向可零loss；complete与dimensional collapse分开。random/NMT/RNMT初始化下不受约束trainE全部BLEU0，冻结或sliced dispersion仅有限恢复，random正则33.2仍低于冻结33.9；他层损伤、projection/sort/subsample与调参费用不能省略。34M WMT19/singleH100/50k不授semantic真值、错误Gram维度/entropy公式或量化因果。actual Ch12正文107/99–119/ownnote393已root独立POST，原categorical/freeze退路完整。Submitted Feb19T11:46:38Z、same-ID Registered Feb20T02:47:34Z支持上述完全落窗半开推定，非精确公告。

### [Same Meaning, Different Scores: Lexical and Syntactic Sensitivity in LLM Evaluation](https://arxiv.org/abs/2602.17316v1)

精确v1 §3.1–3.4/4/Table3实际核：[方法与配置](../_sources/daily-20260221/V3_BODY_2602.17316_METHOD_RESUME.txt)、[关键对照](../_sources/daily-20260221/V3_BODY_2602.17316_CONTROL_RESUME.txt)。wholeitem词改/schema与syntax matrix-clause applicability是不同扰动族；SQuAD保answer string，而prompt/schema不自证全样本语义等价。MMLU的τ.98/.99实际稳定，SQuAD/AMEGA更弱，不能把所有排行榜都说成不稳定；跨model size相关不授因果架构规律。23模型zero-shot/temp0/A100有限披露，改写/重测和自动scorer均付费、未披露全E2E尾SLO。actual Ch66 L427–431已有prompt variants/等价audit、L453–456已有多轴修题、gold/人口与ranking分账，root实际必要源与owner核5分具体Existing通过，不为lex/syntax命名再添段。Submitted Feb19T12:24:42Z、Registered Feb20T02:48:16Z支持本窗半开推定；未复现实验。

### [2Mamba2Furious: Linear in Complexity, Competitive in Accuracy](https://arxiv.org/abs/2602.17363v1)

精确v1 §3–5.2/6–7、必要AppendixA配置实际核：[squared QK/A-mask](../_sources/daily-20260221/V3_BODY_2602.17363_METHOD_RESUME.txt)、[state/crossover与有限评价](../_sources/daily-20260221/V3_BODY_2602.17363_CONTROL_RESUME.txt)、[匹配训练配置](../_sources/daily-20260221/V3_BODY_2602.17363_CONFIG_FIX_RESUME.txt)。单head二阶unique features d(d+1)/2，raw recurrent state d(d+1)^2/2+3d与KV2Nd比较只是缓存元素crossover，不是总memory/walltime。300M/700M、FineWeb、batch32/100K但评估bug只90K；400K/batch64/8192的NIAH是另一预算。medium dt数值diverge可用更高dot precision或去dt分支，但约8x输入精度算子不是E2E；exponentiated变体重新需要KV。actual Ch22 L581–598已有二阶d_h^3、固定长度成本与kernel/numerical/feature-order取舍、exact addressing旧分支，root必要source/owner实际核5分具体Existing通过，不复制成熟三角取舍。Submitted Feb19T13:45:23Z、Registered Feb20T02:49:24Z支持本窗半开推定；不展开全gradients或版本diff。

### [IntRec: Intent-based Retrieval with Contrastive Refinement](https://arxiv.org/abs/2602.17639v1)

精确v1 §3.1–3.4/Eq1–4实际核：[必要原式](../_sources/daily-20260221/V3_BODY_2602.17639_DECIDING_CORE_RESUME.txt)。positive/negative exemplar sets与maxcos(pos)−λmaxcos(neg)可以给反馈reranking，但原保证由不同region直接推出1−cos(r*,rd)>0，缺表示可分条件：两个不同box共享同一单位embedding时，任意λ都同分，不能保证重排选出真目标。root已实际独核此必要原式/反例，central Disputed5终态，不说所有有限经验失效；不采用摘要AP/30ms为真实全任务收益。Ch76 actual241–251已区分表示可区分性、cosine/taskrelevance、正难负与answer support，不为成熟exemplar机制硬增书。重开须给出严格embedding/margin条件、反馈正确性与覆盖范围，不擅自替作者补条件并声称已实现一般保证。Submitted Feb19T18:50:53Z、same-ID Registered Feb20T02:55:57Z支持上述完全落窗半开推定，原字段保留V3_PRIMARY，非精确公告。

### [Computer-Using World Model](https://arxiv.org/abs/2602.17365v1)

精确v1必要原源已读：[核心机制](../_sources/daily-20260221/V3_BODY_2602.17365_METHOD_RESUME.txt)、[关键对照/协议](../_sources/daily-20260221/V3_BODY_2602.17365_PROTOCOL_RESUME.txt)。textΔ再image editor渲染不是完整动作闭环。Table5的同backbone图文拼接可退步，339单步样本的OverallMatch只比较function/status/args；约35%NoGT candidate pool与含GT子集分开。五候选的模拟/渲染/judge额外forward费用和训练成本存在；部署batch/concurrency/tailSLO未披露，不授多步成功、环境真值或权限。Ch25实际body368/351–375/note1591已root独立POST通过。SubmittedFeb19T13:48:29Z、RegisteredFeb20T02:49:27Z。同ID原日期字段保留V3_PRIMARY，公开上界加一秒形成完全落窗的半开推定，非精确公告；未运行实现或复现。

### [RPDR: A Round-trip Prediction-Based Data Augmentation Framework for Long-Tail Question Answering](https://arxiv.org/abs/2602.17366v1)

精确v1必要原源已读：[核心机制](../_sources/daily-20260221/V3_BODY_2602.17366_DECIDING_CORE_RESUME.txt)、[关键对照/协议](../_sources/daily-20260221/V3_BODY_2602.17366_MATCH_RESUME.txt)。Eq8–9 fixed encoder→inverse→re-encode相对误差只绑定augmentation selector，不是truth或easy-learn充分性，零范数guard未披露。AppendixB matched random数量/训练一致，longtail74.5对66.8而frequent81.3对82.7；§4.3少见臂被排除、组名有冲突，不授完整factorial。§8仅singlefact/shortform，inverse construction/增强/finetune均有费用。Ch76实际body266/260–272/note1543已root独立POST通过。SubmittedFeb19T13:49:39Z、RegisteredFeb20T02:49:28Z。同ID原日期字段保留V3_PRIMARY，公开上界加一秒形成完全落窗的半开推定，非精确公告；未运行实现或复现。

### [The Role of the Availability Heuristic in Multiple-Choice Answering Behaviour](https://arxiv.org/abs/2602.17377v1)

精确v1必要原源已读：[核心机制](../_sources/daily-20260221/V3_BODY_2602.17377_METHOD_RESUME.txt)、[关键对照/协议](../_sources/daily-20260221/V3_BODY_2602.17377_CONTROL_RESUME.txt)。§2联合选项检索无stem，按最大cos分配passage计数；Wikipedia/BEIR与20/60检索数、人工/合成distractor共同约束。Bpsych四选项38.5%对25%为13.5pp，三选项48.5%对1/3是15.2pp，不混人口；换语料/任务结果不同、人类选项prevalence与选择相关不显著，不授认知availability原因或LLM实际捷径。检索/合成重试费用保留。Ch66实际body453/447–460/note5592已root独立POST通过。SubmittedFeb19T13:58:48Z、RegisteredFeb20T02:49:44Z；原v1标题采用，不让后来改名生成新事件。同ID原日期字段保留V3_PRIMARY，公开上界加一秒形成完全落窗的半开推定，非精确公告；未运行实现或复现。

### [Dataless Weight Disentanglement in Task Arithmetic via Kronecker-Factored Approximate Curvature](https://arxiv.org/abs/2602.17385v1)

精确v1必要原源已读：[核心机制](../_sources/daily-20260221/V3_BODY_2602.17385_METHOD_RESUME.txt)、[关键对照/协议](../_sources/daily-20260221/V3_BODY_2602.17385_CONTROL_RESUME.txt)。Eq3初始化linearization输出保持→Eq7逐任务Kronecker和→Eq8聚合heuristic有交叉项，不是精确和。O(1)只task数量，AppendixB两个width²factor存储和估计计算费用、原数据访问与非线性漂移保留。Table3 T5-base六NLI原数据81.3对近似78.7不能授dataless普遍优；AppendixE recipe不同不称等预算因果，不授DP。Ch30实际body618/612–629/note907已root独立POST通过。SubmittedFeb19T14:10:45Z、RegisteredFeb20T02:49:55Z。同ID原日期字段保留V3_PRIMARY，公开上界加一秒形成完全落窗的半开推定，非精确公告；未运行实现或复现。

### [Convergence Analysis of Two-Layer Neural Networks under Gaussian Input Masking](https://arxiv.org/abs/2602.17423v1)

精确v1必要[实际输入mask与loss](../_sources/daily-20260221/V3_BODY_2602.17423_METHOD_RESUME.txt)、[Ass5.1/Eq10/Lemma5.5/Th5.6](../_sources/daily-20260221/V3_BODY_2602.17423_THEORY_RESUME.txt)与[D.21–22有限mask证明](../_sources/daily-20260221/V3_BODY_2602.17423_MASK_BOUND_FIX_RESUME.txt)已root实际独核。不是作者完全忽略mask：D21用了D22的单mask高概率上界，但Ass5.1要求for all ξ,W，Gaussian无界，缺全n×K事件/尾部期望衔接。n=m=d=1、x=w=a=1、y=0、c=M>0给L_C=M²/2、gradient²=M⁴，比例2M²无界，否定原逐样本界；不否定条件定理Th5.2或所有有限经验。central Disputed5终态，无Books/正面convergence保证，不扩MIA应用；重开须uniform/tail expectation桥或明确截断mask分布，不替作者补clip。SubmittedFeb19T14:55:10Z、same-ID RegisteredFeb20T02:50:51Z保留原字段，上界加一秒形成完全落窗半开推定，非精确公告。

### [Fine-Grained Uncertainty Quantification for Long-Form Language Model Outputs: A Comparative Study](https://arxiv.org/abs/2602.17431v1)

精确v1[核心机制](../_sources/daily-20260221/V3_BODY_2602.17431_METHOD_RESUME.txt)、[关键对照](../_sources/daily-20260221/V3_BODY_2602.17431_EVAL_RESUME.txt)实际读取。actual §3单位/whole-response/matchedunit/QA/graph和mean/UAD已核，4LLM×2人口、10sample/5unit-QA、同GeminiFlash做claimdecomp/merge/question/grade不是独立truth。ECE>0.6的graph scorers与claim-QA反退、不支持AUROC即概率或删claim后的accuracy即完整回答更真；matchedclaim因费太高未做。§7固定temperature/NLI/embedding/judge以及成本/泛化限制保留。Ch66 actual2099–2116已有typedatomicclaim→riskcoverage/calibration，2165–2185 graphagreement≠truth/独立evidence与abstain，root必要原源/具体owner Existing5通过，不为四family名再加书。SubmittedFeb19T15:02:29Z、RegisteredFeb20T02:51:02Z。同ID原日期字段保留V3_PRIMARY，上界加一秒给完全落窗半开推定，非精确公告；未复现或核代码。

### [AIDG: Evaluating Asymmetry Between Information Extraction and Containment in Multi-Turn Dialogue](https://arxiv.org/abs/2602.17443v1)

精确v1[核心机制](../_sources/daily-20260221/V3_BODY_2602.17443_METHOD_RESUME.txt)、[关键对照](../_sources/daily-20260221/V3_BODY_2602.17443_EVAL_RESUME.txt)实际读取。actual §3双角色、priorH≈S confirmation/blind与closed100wordontology已核；confirmation146games21.9% vsblind143games3.5%，OR7.75不是rate ratio，41.3%seekerdisqualification不作holder真实privacy能力。439实际game不同于450计划人口，LLM arbiter T.01非真正determinism；AppendixI合成atomic/English/T.7/10或16turn、smallcells/dualELOstationarity与judge误判保留，额外多轮生成/判分成本存在。Ch66 actual4422–4435 attackknowledge/access/adaptiveness/危害/预算的具体profile已承载；root necessary/source/owner Existing5通过，无新Books，不授架构、scale或人类攻击因果。SubmittedFeb19T15:09:12Z、RegisteredFeb20T02:51:18Z，采用actualv1标题而非后续改名。同ID原日期字段保留V3_PRIMARY，上界加一秒给完全落窗半开推定，非精确公告；未复现或核代码。

### [ABCD: All Biases Come Disguised](https://arxiv.org/abs/2602.17445v1)

精确v1[核心机制](../_sources/daily-20260221/V3_BODY_2602.17445_METHOD_RESUME.txt)、[关键对照](../_sources/daily-20260221/V3_BODY_2602.17445_CONTROL_RESUME.txt)实际读取。actual §4–5.3 uniformdash+fullanswer→regex/QwenEmbeddingcos，与option/fewshot共同moving协议已核；末句fallback不是abstain，模型defaulttemps非统一，multi-axis改变不授label单项因果。NonsenseQA固定随机word/pseudo-gold不测知识，残留posbias与AppendixH generation-v-selection缺控制、Englishinstruction限制保留。Eq2 orderedpair除choose(n,2)双计数，不采用SCORE数值规范或robustness保证；只有限protocol与accuracy/variance反侧。Ch66 actualprompt/parser/equivalence/invalidparse与permutation/directCoT/预算正文已有具体覆盖，root necessary/source/owner Existing5通过；不授bias消除或泛化校准。SubmittedFeb19T15:12:33Z、RegisteredFeb20T02:51:21Z。同ID原日期字段保留V3_PRIMARY，上界加一秒给完全落窗半开推定，非精确公告；未复现或核代码。

### [Improving LLM-based Recommendation with Self-Hard Negatives from Intermediate Layers](https://arxiv.org/abs/2602.17410v1)

精确v1实际§2.2–2.4/3.3、Table3、A.1必要原源已读。内部层vocabulary projection与ensemble提出非GT高概率hard-negative候选，不赋予负真值；final→intermediate KL和CF概率质量softtarget改变动态token监督，不称普通DPO。浅层/过多层反退、Eq3层数和Eq7 probability/logit含糊、额外projection/KL/CF调参及训练费用保留；8A10040GB不补造precision/batch/concurrency/tailSLO。root必要原源/actual TRAIN-SFT owner PRE通过；Ch29实际正文136–150及自身末注1308独立POST通过，固定verified CE/verifiedpair回退近文，不改Ch34。SubmittedFeb19T14:37:43Z、RegisteredFeb20T02:50:32Z same-ID字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Jolt Atlas: Verifiable Inference via Lookup Arguments in Zero Knowledge](https://arxiv.org/abs/2602.17452v1)

精确v1实际§2/4/5–6必要原源已读。ONNX subset编译为tensor trace、lookup prefix/suffix和memory consistency关系；证明绑定weights/input/compiledgraph/op/numeric/round/lookup身份的数值artifact，不自动等于原浮点行为或实际工作。全局activation input缩放含未补偿lossy变化，不采lossless保证。GPT2-125M/M3MacBookPro16GB约38s包含witness/commitment/sumcheck/opening等证明阶段，不是serving latency；seq/precision/batch/concurrency/tailSLO未披露，不采未匹配17× headline。root必要原源/actual PLATFORM-SECURITY owner PRE通过；Ch72 actual2067–2082及自身末注4242独立POST通过，独立原行为验证/trust-boundary回退近文。SubmittedFeb19T15:17:18Z、RegisteredFeb20T02:51:31Z字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Retrospective In-Context Learning for Temporal Credit Assignment with Large Language Models](https://arxiv.org/abs/2602.17497v1)

精确v1必要[实际方法](../_sources/daily-20260221/V3_BODY_2602.17497_METHOD_RESUME.txt)4–23与[Theorem4.1证明](../_sources/daily-20260221/V3_BODY_2602.17497_PROOF_RESUME.txt)1–14已root独核。无offset logratio不按比例等于普通advantage：普通adv的π0期望为0，但单state两action π0=(.5,.5)、π′=(.8,.2)给Eπ0log(π′/π0)=.5log(.64)≠0。证明Eq11加入logZ、Eq12使用soft value，与原普通adv接口不一致；π′=π0时logratio为0而softadv期望含−βH。构造reward也不自动是环境r*，不证明反思credit真实。中心Disputed5安全隔离通过，无Books/正面等价保证；不否定带offset逆构造或有限heuristic经验。重开须统一普通/soft优势、合法offset和构造reward与环境目标关系，不擅修定理，不扩全BabyAI或全部证明。SubmittedFeb19T16:13:28Z、RegisteredFeb20T02:52:36Z字段保留，上界加一秒形成完全落窗半开推定，非精确公告。

### [LORA-CRAFT: Cross-layer Rank Adaptation via Frozen Tucker Decomposition of Pre-trained Attention Weights](https://arxiv.org/abs/2602.17510v1)

精确v1[实际方法](../_sources/daily-20260221/V3_BODY_2602.17510_METHOD_RESUME.txt)16–19/37–65/87–104、[配置](../_sources/daily-20260221/V3_BODY_2602.17510_EVAL_RESUME.txt)1–7与[直接限制](../_sources/daily-20260221/V3_BODY_2602.17510_LIMIT_RESUME.txt)1–5已root独核。跨层Q/V tensor→冻结HOSVD/core/U/W/R，只训square J，是具体适配空间，但W_hat=W+T(J)−R仅J=I精确保原W；Alg1实际J=I+εE、ε=.01 σ=.02，scalar U/G/W=1与J1=1+δ给W_hat=1+δ，否定near-I的精确初态推广。Def3 orthcols与base12层却统一r1=24配置不相容，不猜clamp；large r1=24不压layer轴。固定rank训练参数数不含classifier/frozenbuffers/总算量，W与R增内存、setup分解有费，未测wallclock、单seed/base低LoRA2.7pp。Ch30原初态保base与sharedbasis不修复这些中心接口；Disputed5终态，无Books/正面exact或recipe保证。重开须一致初始化/合法rank、可核模型和残差部署身份，不替作者修算法。SubmittedFeb19T16:22:22Z、RegisteredFeb20T02:52:55Z同ID字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未复现。

### [When Models Ignore Definitions: Measuring Semantic Override Hallucinations in LLM Reasoning](https://arxiv.org/abs/2602.17520v1)

精确v1[方法](../_sources/daily-20260221/V3_BODY_2602.17520_METHOD_RESUME.txt)1–40、[operator受控例](../_sources/daily-20260221/V3_BODY_2602.17520_CONTROL_RESUME.txt)65–70及[结论](../_sources/daily-20260221/V3_BODY_2602.17520_CONCLUSION_RESUME.txt)1–5已读。30prompt五trapfamilies以Solve/Flag区分局部definition、underspec/contradiction，不把典型数值答案当唯一正确行为；三模型首response与fixed-or-default温度描述不构成广泛确定protocol，匿名A/B/C和后表实名、不匹配人口的aggregate不授通用ranking。Ch66 actual273–279已有samepixels standard/inverse与neutral/semantic alias对照、localrule/oracle/EvalSpec绑定，root Existing5通过，不因文本硬件域或新术语再加段，不授内部local-unlearning原因或一般verifier。SubmittedFeb19T16:33:46Z、RegisteredFeb20T02:53:09Z同ID字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核代码或复现。

### [The Anxiety of Influence: Bloom Filters in Transformer Attention Heads](https://arxiv.org/abs/2602.17526v1)

精确v1[方法](../_sources/daily-20260221/V3_BODY_2602.17526_METHOD_RESUME.txt)1–32与[必要混杂控制](../_sources/daily-20260221/V3_BODY_2602.17526_CONFOUND_RESUME.txt)1–39已root独核。GPT2/Pythia有限CPU行为probe中continuous FP ratio不等binary容量rate；固定200token、变化unique prefix+5probe并padding后，L3H0仍FP100%而重判prefixhead，说明此前长度/content混杂不能授容量。fixedlength仍改变重复/内容分布，不授唯一因果；小点拟合与head维度也不证明真的bit/hash Bloomfilter、独立多head乘法或数学no-FN保证。Ch14 actual230–266已有probe可读≠causal/多点干预、softmax质量sink/noop≠语义功能，Ch66绑定input/length/position的identity；root具体Existing5通过，无新Books/runtime shortcut。SubmittedFeb19T16:37:16Z、RegisteredFeb20T02:53:18Z字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核代码或复现。

### [Evaluating Chain-of-Thought Reasoning through Reusability and Verifiability](https://arxiv.org/abs/2602.17544v1)

精确v1[实际协议](../_sources/daily-20260221/V3_BODY_2602.17544_METHOD_RESUME.txt)1–11/374–384已root独核。R=(helped+harmed)/Thinkercorrect，丢Thinkerwrong人口，是正反改答案的persuasiveness而非成功复用；V在全Q测executor与thinker同最终答案，可一起错，不授faithfulness/真实verification。4thinker×10executor、5有限benchmark、Ollama默认decode/A10080GB且committee选择影响scale，relative排名不认证跨模型普遍机制；未识别最终答案/长度等提示影响不能归因CoT语义。Ch66 actual269–271 reasoning≠faithful、286–288 prefill来源/formatconditioning与2165–2185 agreement≠truth/独立evidence已具体承载，root Existing5通过，无新Books，不用名称替换真实verifier。SubmittedFeb19T16:59:11Z、RegisteredFeb20T02:53:43Z字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核代码或复现。

### [Privacy in Theory, Bugs in Practice: Grey-Box Auditing of Differential Privacy Libraries](https://arxiv.org/abs/2602.17454v1)

精确v1[实际方法](../_sources/daily-20260221/V3_BODY_2602.17454_METHOD_FIX_RESUME.txt)17–42、[Opacus反例](../_sources/daily-20260221/V3_BODY_2602.17454_OPACUS_RESUME.txt)1–13、[版本](../_sources/daily-20260221/V3_BODY_2602.17454_VERSION_RESUME.txt)1–4与[直接限制](../_sources/daily-20260221/V3_BODY_2602.17454_LIMIT_RESUME.txt)1–18已root独核。Record调用类型/次序/参数/query/output/postPRNG，replay返回冻结output而非只seed，配人工ensure_equality与declaredsensitivity比较；假设trustedprimitives/accountant，非外部恶意actor。Opacus f17f254 make_private private-n normalization只该版本/adjacency/path，不授当前库仍有bug。原文冗余operation也承结构失败可不改变最终分布；nonformal/testedneighbor与path、稀有事件/不可控随机硬件/并发scope、hook/trace/人工诊断费用保留。Ch72原conformance→accountant缺这一测试接口，实际body534/536/邻接526–546/自身末注4248独立POST通过，PLD前后递进与保守回退近文，不授全隐私证明。SubmittedFeb19T15:18:00Z、RegisteredFeb20T02:51:34Z字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核代码或复现。

### [A Theoretical Framework for Modular Learning of Robust Generative Models](https://arxiv.org/abs/2602.17554v1)

精确v1[实际setup/中心理论](../_sources/daily-20260221/V3_BODY_2602.17554_METHOD_RESUME.txt)1–42/145–178已root独核。Only KL(empirical p_k||expert πhat_k)≤ε_k未要求expert支集限X0=union empirical supports；G1又在X0上要求Z_g=1，Lemma1称constantgate总属于G1。p=1、p_emp=δ_a、expert(a)=.9/expert(b)=.1满足KL=−log.9有限，但X0={a}且g(a,1)=1使Z=.9，G1空；Theorem3赖以成立的非空compact不能由已述前提推出。中心Disputed5隔离通过，无Books或正面robustexistence保证；不宣布所有条件版本理论不存在。重开须官方明确expert-on-X0归一化/支持假设及一致gate定义，不擅补新目标，不读无关distillation/全部appendix以规避中心问题。SubmittedFeb19T17:09:13Z、RegisteredFeb20T02:53:58Z原字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核实现或复现。

### [Learning to Stay Safe: Adaptive Regularization Against Safety Degradation during Fine-Tuning](https://arxiv.org/abs/2602.17546v1)

精确v1必要METHOD6–38/91–104/205–212、CONFIG_FIX1–21、LIMIT_FIX7–16、CONTROL1–27已独核。Pre/post critic是不同观测/成本，EMA不授hardtrust；五模型ASR仍有10.1/10.2且同judge盲点。2A10080GB/LoRA/B8/20epoch和reference/probe/judge费用近文。Ch29 body809/801–817/note1312 actual POST通过。SubmittedFeb19T16:59:54Z/RegisteredFeb20T02:53:46Z。 原证文件统一V3_BODY_2602.17546；同ID日期保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现或复现。

### [MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning](https://arxiv.org/abs/2602.17550v1)

精确v1必要METHOD10–46/281–307、CONFIG1–24/34–38、CONTROL1–2已独核。sggate单边抑制不授trust/token真值；SAPO反侧非全factorial，极小oldprob/下溢/freshness需数值门。512/32=16次offpolicy/KL0、20kGPUh是研究预算非生产费用。Ch33 body185/169–197/note2889 actual POST通过。SubmittedFeb19T17:05:20Z/RegisteredFeb20T02:53:52Z。 原证文件统一V3_BODY_2602.17550；同ID日期保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现或复现。

### [GraphThinker: Reinforcing Video Reasoning with Event Graph Thinking](https://arxiv.org/abs/2602.17555v1)

精确v1必要DECIDING_CORE1–30、REWARD13–27、CONTROL1–40、TRAIN1–6已独核。semantic≥.4/tIoU≥.3是训练reference门；temporal非causal、attention非grounding、同MLLM非独立truth。Prose3B/table7B冲突不采精确提升；8A100/4096+2048/G8/B16/1ep及额外caption/graph费用、原视频回退近文。Ch23 body580/574–590/note1299 actual POST通过。SubmittedFeb19T17:09:30Z/RegisteredFeb20T02:53:59Z；采用actualv1标题。 原证文件统一V3_BODY_2602.17555；同ID日期保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现或复现。

### [RetouchIQ: MLLM Agents for Instruction-Based Image Retouching with Generalist Reward](https://arxiv.org/abs/2602.17558v1)

精确v1必要DECIDING_CORE1–16、LABEL1–10、CONTROL1–3、CONFIG1–12/26–29已独核。Reference恒优/format标签不授人类审美；QwenVL7B双模型/同GLM注评、10kperturbed+5kpolicy与有限测试、总预算未披露。额外rollout/RM/policy成本与冻结回退近文。Ch31 body863/857–871/note1310 actual POST通过。SubmittedFeb19T17:11:59Z/RegisteredFeb20T02:54:04Z。 原证文件统一V3_BODY_2602.17558；同ID日期保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现或复现。

### [AI Gamestore: Scalable, Open-Ended Evaluation of Machine General Intelligence with Human Games](https://arxiv.org/abs/2602.17594v1)

精确v1[官方PDF](https://arxiv.org/pdf/2602.17594v1) §4.1–4.2/P10–11与Fig5已实际独读。106 humans各10 games、每局120秒真实播放；模型每1模拟秒暂停，返回5组各.2s动作后再继续，120模拟秒最多120calls，不是同墙钟预算。七模型defaulttemperature/thinking、三次trial；原协议walltime>1200s/12–18倍和score/cap的geometricmean只该人口，不授广义能力ranking或内部worldmodel因果。分类由三作者标注非causaltruth。Ch66 actual678–680及2857–2862已有输入暂停/独立时钟、仿真time/provider/timeout与真实deadline分账，root具体Existing5通过，不新增Books。SubmittedFeb19T18:17:25Z/RegisteredFeb20T02:54:56Z原字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核实现或复现。

### [ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment](https://arxiv.org/abs/2602.17560v1)

精确v1[Prop1](../_sources/daily-20260221/V3_BODY_2602.17560_THEORY_RESUME.txt)9–16、[Eq12–14](../_sources/daily-20260221/V3_BODY_2602.17560_METHOD_RESUME.txt)与[C.4证明](../_sources/daily-20260221/V3_BODY_2602.17560_PROOF_RESUME.txt)1–19实际独核。h(x,y)=y−exp(−x)、v=(1,0)逐点hdot=exp(−x)>0，初态(0,0)却在全部有限t保持h<0，不进入非空C；原generic到达命题缺条件。归一∇h在零梯度无定义，Jᵀw=0不只w=0或J=0；a.e.正性也不自签全轨迹保证。二次critical-point例只说明未排除域，不声称实际CountSketch模型必遇。中心Disputed5安全隔离通过，不采用到达/不变性桥，不否定有限经验；重开须正式补全到达/域/零梯度/离散保证，不擅补guard或扩全附录。SubmittedFeb19T17:13:44Z/RegisteredFeb20T02:54:07Z原字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Revisiting Weight Regularization for Low-Rank Continual Learning](https://arxiv.org/abs/2602.17559v1)

精确v1必要METHOD/OVERVIEW1–43、ALGORITHM1–36和LIMIT1–4已实际独核。完整权重增量的empiricaldiagF而非因子/J₀Gram，task-end merge/reinit只对taskcount常量状态；同CIFAR额外6GB与塑性97.99低于无F98.86、长序列F漂移/复杂度限制和原adapter/rehearsal回退近文。Ch30 body759/753–771/ownnote911 actualPOST通过。SubmittedFeb19T17:13:00Z/RegisteredFeb20T02:54:05Z。 原文件统一V3_BODY_2602.17559；same-ID日期原字段保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Optimal Unconstrained Self-Distillation in Ridge Regression: Strict Improvements, Precise Asymptotics, and One-Shot Tuning](https://arxiv.org/abs/2602.17565v1)

精确v1METHOD5–79/Eq3–10、ESTIMATOR14–56/Eq19–23、ASSUMPTION1–11已实际独核。同X/正λ/squaredloss容许负ξ但不授LLM KL负权；oracle不严格胜最佳ridge，GCV IID一致非OOD，Dhat小guard、PD fit/trace费用及fixedmixture/heldout回退近文。Ch29 body274/270–280/ownnote1316 actualPOST通过。SubmittedFeb19T17:21:15Z/RegisteredFeb20T02:54:13Z。 原文件统一V3_BODY_2602.17565；same-ID日期原字段保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Canonicalizing Multimodal Contrastive Representation Learning](https://arxiv.org/abs/2602.17584v1)

精确v1KERNEL1–30、THEORY1–81、CONTROL1–15已实际独核。全Ω anchor-crosskernel/Sym spanning与invertibility不是少量anchorfit经验已证；矩形只projection、各modalitymean/version、OxfordPets linear/MLP imagefit佳而text差、classification域与费用/重编码回退近文。Ch23 body75/77/71–83/ownnote1305 actualPOST通过。SubmittedFeb19T18:09:36Z/RegisteredFeb20T02:54:42Z。 原文件统一V3_BODY_2602.17584；same-ID日期原字段保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Modeling Distinct Human Interaction in Web Agents](https://arxiv.org/abs/2602.17588v1)

精确v1MODEL_FIX1–7/69–93、既有DECIDING_CORE§5与CONFIG1–8已实际读。按trajectory split但1247train/251test数量是steps，1:7且Hands-off剔除；AlwaysNo85.3accuracy/PTS0反侧、executor不变只prompt时序，20原人4返访非随机rating不授solely因果或实际walltime。Ch81 actual825–835真实body已有trajectoryclassifier/advisory/低recall/nonrandomstudy及ask/pendingeffect/controllease/handback/reconcile，root具体Existing5通过；不因Ch78无字眼重复写。SubmittedFeb19T18:11:28Z/RegisteredFeb20T02:54:47Z。 原文件统一V3_BODY_2602.17588；same-ID日期原字段保留V3_PRIMARY，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Asymptotic Smoothing of the Lipschitz Loss Landscape in Overparameterized One-Hidden-Layer ReLU Networks](https://arxiv.org/abs/2602.17596v1)

精确v1[actualLemma1](../_sources/daily-20260221/V3_BODY_2602.17596_METHOD_RESUME.txt)4–33及Eq21–22/124–132已实际独核。m=n=1/unitW=1/X≡1/Y≡M，loss=|Y−prediction| convex1-Lipschitz、κ=.5，目标|M−θ|+.5|θ|唯一最优θ=M；M>2违原L/κ=2上界。从κ||θ||≤L||θ||取消只得κ≤L，不能得到norm bound；主Cα桥实际依赖此lemma。中心Disputed5隔离通过，不授该norm/connectivity保证，不否定有限DSS经验或正式补全条件后的理论，不替作者改证明。实际v1标题保留而非后版FromApproximation…；SubmittedFeb19T18:20:21Z/RegisteredFeb20T02:54:58Z同ID原字段保留，上界加一秒形成完全落窗半开推定，非精确公告；未核实现/复现。

### [Towards Anytime-Valid Statistical Watermarking](https://arxiv.org/abs/2602.17608v1)

精确v1 METHOD3–23/59–69、MARTINGALE8–16及EVAL3–41实际读与独核。null当前seed与output给定history独立，每步非负条件期望≤1→乘积test supermartingale/1α任意停止边界；Eq3行归一使validity不依赖未验q近邻，p0>δ/q近邻是power与最优coupling适用域，不把自然语言相似当验收。Llama2-7Bchat T.7/Phi3mini128k anchor、300outputs/三任务、greedy Llama3judge/α.02、baseline Bonferroni同anytime口径；median72 vs84.5tokens非GPUtime或所有扰动保证，硬件/precision/完整费用未披露。actual Ch72此前容量/概率质量/key信任根未承载optional-stop合同，root PRE后窄写1113/完整1107–1123/ownnote4258实际POST通过；forward/replay费用、inconclusive、fixedhorizon/签名回退近文。SubmittedFeb19T18:32:26Z/RegisteredFeb20T02:55:15Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightarrow$LLM Pipelines?](https://arxiv.org/abs/2602.17598v1)

精确v1 METHOD1–76、ERASURE1–35、NOISE1–8与LIMIT1–25实际审阅/root独核。四speechLLM与五cascade中只有三同backbone，Whisper清噪声前端不是任意ASR；六Edgevoice/四text-sufficient任务与自然MELD/MUStARD，MUSAN15/10/5/0dB是有限population。九层LEACE同时作用且涵盖生成tokens，text159强损但random159亦伤Ultravox CSQA/MELD、acoustic/text纠缠；线性probe/擦除不证明内部ASR是唯一必要算法，维数不同与mean-shift guard近原证。clean差分/noise反侧不授普遍cascade更便宜，完整runtime/hardware/precision未披露。actual Ch66 660–676同题input消融与matchingbackbone/预算已承载，Ch23 952–964/1054–1062可读≠use为依赖；root具体Existing5通过，不新增成熟原则。SubmittedFeb19T18:22:39Z/RegisteredFeb20T02:55:02Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [Stable Asynchrony: Variance-Controlled Off-Policy RL for LLMs](https://arxiv.org/abs/2602.17616v1)

精确v1 METHOD9–32/53–101、BASELINE_PROOF_FIX1–74与CONFIG1–24/79–135 actual独核。Constant population b*=Ew²||g||²R/Ew²||g||²需unclipped ratio/support与微分条件，finite self-inclusive plug-in≈和TIS不授无偏/variance-optimal；ESS取unclipped ratios，sqrt相对on-policy reference不是普遍稳定定理。逐trajectory gradient与两个buffer/延迟DP省第二次backward不等batch一次；4H100 TP4 seq8192开销19%time/14%memory与MATH4H100sampler+4trainer/B512/response4096/400steps不同配置，precision/SLO未披露。组件及低LR反侧有限，费用与旧基线/freshrollout回退近正文。SubmittedFeb19T18:40:51Z/RegisteredFeb20T02:55:26Z。 Ch33正文2395/2397、完整2387–2407/own2895root非作者实际POST通过。原文件V3_BODY_2602.17616；同身份日期字段保留，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [What Makes a Good LLM Agent for Real-world Penetration Testing?](https://arxiv.org/abs/2602.17622v1)

精确v1 DECIDING_CORE85–107、EVAL138–153/169–202及LIMIT1–17 actual独核。外部tree留prunedbranches，新credentials满足precondition即重评；pilotLLM horizon/TDI只是heuristic，非MCTS sound/complete/授权。三model×三trial，表mean与正文bestofthree冲突，累计组件/tool接口同时变更不授reopen单组件91%因果；公开walkthrough/缺active defenders、token失败反侧保留。额外tree/传播/re-eval费用和宽搜索/真实obs/独立终局verifier近文。SubmittedFeb19T18:42:40Z/RegisteredFeb20T02:55:35Z。 Ch79正文195、完整185–207/own548root非作者实际POST通过。原文件V3_BODY_2602.17622；同身份日期字段保留，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning](https://arxiv.org/abs/2602.17633v1)

精确v1 METHOD5–39/53–98、BOUND1–22/27–59、PROOF1–35与VERIFIER1–4实际读/root独核。双阈值中间strong、两端仍以qA/qR>0随机audit，观测标签才inversepropensity更新；Theorem5.1 fixedT/constantη/qmin及N0/N1双侧分母不授anytime、accepted-population selective-risk或strong=truth。小q余项/空类约定、MATH GPT4o对GT判定与Sudoku确定规则、受限调用数非wallclock/hardware/precision/SLO保留。Ch66此前label-relative oracle与conformal不含在线部分反馈分支；actual正文744/完整738–752/own5614已root独立POST，费用/strong-only与独立verifier回退近文。SubmittedFeb19T18:47:38Z/RegisteredFeb20T02:55:49Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [Multi-Round Human-AI Collaboration with User-Specified Requirements](https://arxiv.org/abs/2602.17646v1)

精确v1 RULE1–58、METHOD1–40、PROOF1–23及CONTROL1–27实际读/root独核。题内阈值固定、每题末truth再更新，prefix-rule逐标签支配fullrule与boundedscore下telescoping界约束每题max activated AI-set omission，非用户最终准确/不被误导/动作批准。50人1000interaction的全局流与有限视觉计数不授个人化或医学效果；额外truth/评分/宽set和标签失配回退近文。Ch81已有advisory intervention与approval，但未有这类prediction-set反馈条件；actual正文838/完整828–846/own1552root独立POST通过。SubmittedFeb19T18:54:34Z/RegisteredFeb20T02:56:07Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [SMAC: Score-Matched Actor-Critics for Robust Offline-to-Online Transfer](https://arxiv.org/abs/2602.17632v1)

精确v1 METHOD1–74/SETUP1–23、CONFIG_FIX必要K配置与SCORE1–6 actual独核。AppJ ε-MSE目标若x∼N(0,1)、z=√abar x+√(1−abar)ε，最优εhat=√(1−abar)z而score(z)=−z，原+score/√abar接口符号与缩放不成立，影响score-matched critic解释。learnedα是否允许负号、实际noise→score转换需官方明示，不自行吸收符号修算法；不反断所有实验失败。六D4RL、offline→5000warmstart→50/50replay200k、Muonscore组合与部分TD3退化保留局部范围，不授无退步迁移。中心Disputed5 root安全隔离，无Books；重开须official noise/score参数化、α符号与实现关系更正。SubmittedFeb19T18:47:31Z/RegisteredFeb20T02:55:48Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [Pushing the Frontier of Black-Box LVLM Attacks via Fine-Grained Detail Targeting](https://arxiv.org/abs/2602.17645v1)

精确v1 METHOD1–65、CONTROL70–77/244–290/323–360与COST1–2 actual独核。像素IoU/embedding接近不授ViT梯度稳定；source随机crop梯度估计与targetreference近邻变换分责。100NIPS2017、epsilon16/300steps/K10/P2/α1.275 vs旧1/.75、PE+代理池变化非同gradientbudget，删除组件部分KMR反升，不授单机制普遍因果/当前API脆弱率。Linux/6RTX4090/temp0/seed2023/限定evaluator阈值与precision/端到端/SLO未披露保留；不采用Th3.1量纲疑式或3.5泛transfer桥，不提供执行攻击recipe。Ch72 actual正文1310/完整1302–1320/own4262已root独立POST，采样/编码/查询费用及原安全gate回退近文。SubmittedFeb19T18:54:32Z/RegisteredFeb20T02:56:06Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [Differences in Typological Alignment in Language Models' Treatment of Differential Argument Marking](https://arxiv.org/abs/2602.17653v1)

精确v1 METHOD5–43/48–65与CONFIG1–31 actual独核。18parallelcorpuses/184Mtokens、90/5/5同split、GPT2small scratch15k/bf16/A100约6h/context1024/B48×2；1000minimalpairs按500marked/500unmarked许可、meanNLL与marker±1–2tokens placement单测。Local/global约.77/.59、natural/inverse约.85/.68，而subject/object约.74/.79无明确人类方向复现；placement近ceiling不等semantic规则掌握。BERT代理语义标注、长度归一化与单架构、频率r−.56/高表现subset−.17未排全部混杂，linearprobe可读不授真实因果。root标准5分证据通过但仅报告：书已有目标/子能力/行为≠内部因果边界，本局部规则证据未修正一般学习机制或确立人类typology来源，不强改Ch4、也不冒称Existing同一实验。SubmittedFeb19T18:56:34Z/RegisteredFeb20T02:56:16Z同身份原字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [Mine and Refine: Optimizing Graded Relevance in E-commerce Semantic Search Retrieval](https://arxiv.org/abs/2602.17654v1)

精确v1 METHOD_FIX1–20/59–79、DECIDING_CORE1–55、EVAL同backbone与155M同judge/30%未见query、CONTROL必要grade/mining/增广反侧actual独核。部分相关grade相对不同pair可正可负，offlineANN top100–200重标而非随机inbatch一律无关、mining保原negative防旧边界遗忘；不抄circle公式或授score校准/cardinal utility。相同0.1B初始化与更大pretrained不同基准，线上一月50/50只整套retrieval干预；同LLM标注/评价、低ratio增广与分离度反退、hardware/precision/batch/SLO未披露及额外训练/index费用近文。Ch76多positive责任尚未承载grade双角色；actual正文375/完整369–383/own1553root独立POST通过。SubmittedFeb19T18:56:36Z/RegisteredFeb20T02:56:18Z同身份字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [MARS: Margin-Aware Reward-Modeling with Self-Refinement](https://arxiv.org/abs/2602.17658v1)

精确v1 METHOD12–53、CURVATURE_DECIDING1–32、EVAL1–16与CONFIG_FIX1–43 actual独核。|margin| softmax分配每epoch增广预算、T5改写chosen/rejected并保原pair，合成排序继承假设而非新增人类truth，大负margin也可少选。线性BT平均Hessian PSD下界须P/Q margin分离、featurecovariance dominance与γcurv>1，不推出conditionnumber改善。DeBERTav3base/三dataset固定1000、ColabA10080GB、TinyLlama/LoRA16与Qwen2.5judge有限；PKU test缺时退train、改写未全独立偏好验证、同epoch/LR不等生成token或walltime预算保留。Ch31 genericacquisition还缺合成监督/方向条件分支；actual正文582/完整574–590/own1320root独立POST，原对/均匀增广与独立heldout回退近文。实际v1题名按abs/正文，不采DataCite当前后版题名。SubmittedFeb19T18:59:03Z/RegisteredFeb20T02:56:23Z同身份字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs](https://arxiv.org/abs/2602.17659v1)

精确v1 METHOD1–76、ACTION_OBJECT1–33、BENCHMARK2–22/CF-Focused控制及CONTROL1–128 actual独核。AppA Eq8将概率affine混合后声称Eq9 log乘积rewrite：prior=(.5,.5)、conditional=(.75,.25)、ω2，前者(1,0)后者归一(.9,.1)，conditional=(.9,.1)时前者可负；中心Bayes重加权桥不成立，不能自换logits/flow对象补证明。root中心Disputed5安全隔离，无Books；不否定有限actionproposal或整个实验。LIBERO-CF四suite50tasks×50trials under-observed/unseen指令、grippercontact≠完成、faithful/biased非互补；移除trainingobjects也改视觉/支持，非唯一因果。TF两forward/no-language分支不是零费，VA30k/B32额外train、dropout R2反退与overscale伤success保留，未披露完整硬件/precision/实时控制SLO不外推真机安全。重开须官方统一概率/输出参数化、合法归一及对应桥接证明，只恢复该中心命题。SubmittedFeb19T18:59:20Z/RegisteredFeb20T02:56:24Z同身份字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

### [Sink-Aware Pruning for Diffusion Language Models](https://arxiv.org/abs/2602.17664v1)

精确v1 METHOD42–73 Eq8–14、EVAL257–272/397–416/457–480 actual独核。Uniformtimesteps加噪校准，allhead/layer attentionmass的平均softsinkness φbar，以1−φbar重权activationrows进入Wandaimportance/SparseGPT二阶矩；不是按temporalvariance挑不稳定位置，更非runtime删token/semantic真值。WikiText2同128×2048与25/50/75%sparsity固定对照，LLaDA1.5 SparseGPT75平均33.94→33.63否定全配置胜；limits fixedcalib/shift、attentionmap多时刻采集与hwprecision/采样细数/完整runtime未披露保留。Ch49已有混合loss/protectedset角色，但缺noise/time-conditioned importance；actual正文509/完整503–519/own2756root独立POST，原校准/保守pruning/dense与kernel独立验收近文。SubmittedFeb19T18:59:50Z/RegisteredFeb20T02:56:31Z同身份字段，上界加一秒完全落窗半开推定，非精确公告；未核实现/复现。

## 5. 缺口与下一步

本窗终态保留项：下列外部缺口不支持正面证据、Books 或无遗漏断言；逐项给出定点重开条件，恢复仅重开受影响来源或身份。


普通扫描、筛选、必要证据阅读和Books写入待办为0；全部单项处置与74处实际POST已落实。最终六部分、来源范围与安全终态隔离已获root非作者日级验收；机器检查只验证格式、引用及可判定一致性，不代替语义。

最终164份完整题摘的唯一身份与逐ID路由见[本日筛选末段](../_sources/daily-20260221/V3_SCREENING.md)：116安全终态候选＋38准入前排除＋9日期保留＋1官方移除/合法原源保留。下面是本窗已隔离的外部材料，不是未读普通队列；不补读无关附件、不用后版替代、不扩张日期窗口。

日期终态隔离拟项：2602.16740/16741/16745/16746/16760/16763、16855，以及17046（actual v1 Submitted为2025-12-01T06:43:43Z）早Submitted，现有Registered只给上界，公告最早下界在窗前。官方当批公告直接入口一次未恢复，不扩整月逐identity；恢复须提供same-family v1官方公开列表/实际公告把整个区间限在本窗内。它们不列确定候选、不进入Books，也不被计为零命中。

原源access保留：2602.17547v1 KLong的actual官方abs明确“No PDF available”与管理员版权授权移除说明，HTML实际404；root独核允许安全隔离，无正面采用。恢复须官方可用的授权本窗v1正文或明确合法的同版本原源，不以v2/v3代审，不寻找未经授权副本。此项不是贡献EX或作者阅读延迟，独立于9日期保留；不支持正面采用或Books。

中心争议终态隔离：2602.16873v1的§3.4 W/L≥width被单位权5-node链+2孤点否证，Table4的500与§5.5所述Tables2–4仅85%test矛盾；经验路由消融潜力不因此自动EX，但law/optimal及中心数字未采用。2602.16829v1两-timescale推导fast含噪o(t)而期望误差遗漏噪声稳态偏置，‘同rates任意noise无gap’未由递推成立；只核NN噪声监督臂，不扩human/EEG，经验容量反侧仅按作者局部范围报告，不授中心规律。16784ρ记号争议如影响拟采用命题则须隔离相关数值界，不能靠删反侧授保证。16837的P X0 V代理与additive residual接口冲突、16849 Def4.1的exp相位和=0不可能及αβ²/α²β不一致也已必要独核并隔离；有限小模型经验不替代中心证明。恢复条件分别为勘误后的含噪递推、同接口残差证明、一致test IDs/split、合法相位定义/输出系数/下降动力学及合法敏感性定义。

另16967中心commutator必要性/含未来tgrok预测、16984§5 hash与adaptive后验、17025 preference方向/标量聚合/长度罚，已由root必要独核允许终态隔离。重开条件见各自§4，不进入Books或正面保证，不能从隔离反向EX其准入潜力。

原库存16928后续v3题摘被误当v1：已撤销受影响推断，actual v1仅成熟evolution/game-solver组合，原始筛选EX理由按v1记录；不扩大检查全部版本。

Same-family日期保留2602.17614：同DOI [IEEE/Crossref原字段](../_sources/daily-20260221/V3_PRIMARY_2602.17614.crossref.json)published-print/published为2025-12-08，[官方专题program](https://sites.google.com/unical.it/psbd2025)列Dec9同题同作者；created2026-03-06只是metadata登记，缺published-online。未取得actual2025print正文与v1身份比对及精确首次可取得正文日，因此root独核按日期保留终态，不将arxiv新收录当本窗新贡献；恢复须IEEE精确正文/officialavailability说明，只重开此family，不继续隐私deep。

其余中心保留身份为2602.17095/17168/17200/17375/17223/17312/17270/17639/17423/17497/17510/17554/17560/17596/17632/17659，连同上列8项共24家族。每项的原始链接、具体冲突、拟采用命题为何不能成立、可接受的官方更正/补充条件及定点重开范围均在§4同标题证据段保留；不自修作者保证、不把有限经验全部宣布无效，也不以成熟原则另造Books更新。来源目录缺段的定点重开条件按§2对应行：官方可读历史列表/已披露原生查询协议或原事件发布与更新字段；恢复只影响对应来源/身份，未到达前不授正面Coverage/Evidence、Books或全网零遗漏。

## 6. 复核

复核者：root（独立非作者）。

结论：通过

root已独立读八批164份完整题摘并校准准入/代表排除，后四批88逐ID路由由原JSON对象恢复且充分once裁决优先；原证与具体EX理由保留，不将AB潜力当候选。116确认落窗家族的必要原源/结论/owner处置已逐项独核，其中74实际写入的正文、完整前后邻接及自身末注全部非作者POST通过，15具体已有覆盖、16931/17171/17653仅报告、24中心隔离逐项成立。17547官方版权移除、Anthropic安全公告、17283/17288贡献EX及17465旧出版窗外已实际独核；日期/访问/目录保留不授正面通过。最后三POST为17654 Ch76、17658 Ch31、17664 Ch49；不重新无差别审此前有效附件或74处POST。root最终实际检查14每日来源及触发日期源的主题/有限停止、历史缺段隔离、冻结分母/日期/保留项与完整六部分通过；此前164题摘与分层风险EX独核有效复用，未把抽样或有限列表称全481/全互联网验证。Coverage、Evidence、Books均处理到合同定义的安全终态，日期/访问/中心争议保留不计正面通过。机器检查不替代此语义验收。

完成态V3格式与可判定一致性校验通过；本日报、原证目录及承载74处写入的29个owner文件，未暂存与已暂存的定点差异检查均通过。该结果不替代上述root独立语义验收。

未stage、commit或push；运行前与其他日期/Books的staged、unstaged修改全部保留。本日完成后停止，不自行接其他日期。
