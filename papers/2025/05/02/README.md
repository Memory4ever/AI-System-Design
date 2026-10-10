# Daily Research — 2025-05-02

**规范：** V3
**窗口：** 2025-05-01T09:00:00+08:00 ～ 2025-05-02T09:00:00+08:00
**窗口说明：** 用户于2026-10-07授权只补已有Daily遗漏，保留原候选公开日、原窗口、日期归属、评分及有效审阅，不迁移旧材料。完整原报告见[档案](../_sources/daily-20250502/baseline-before-supplement-20261007.md)。
**补充窗口：** 2025-05-01 ～ 2025-05-01
**状态：** 进行中
**Books：** 纳入本次
**检查时间：** 2026-10-07T21:19:25+08:00

## 1. 结论

原26家族保留原公开日2025-05-02、原评分、精确版本有效审阅及已有覆盖决定；原321=26+295只属于旧inventory，不是补查分母，不继承旧完成结论。

14个每日源实际重新访问，历史恢复限制逐源隔离；4个有界arXiv具名主题134次出现去重为110完整当前题摘：root实际读18个具名exact-v1 core并通过五新关闭，当前校准74P/36C，均非确定May1候选。LIFT保留P及中心梯度实现争议，不因争议改C/降分。Anthropic仅产品可用性贡献前关闭；AMIE May1官方事件准入及5分已获root通过，Meta Cutouts和OpenAI事故维持关闭/操作反侧。Google Pubs另实际恢复2025+language model首页15/37目录身份，日期搜索0条不作无遗漏。没有catchup或全年正文队列。

**本轮内容差额已获root第三批独核通过；整日未验收，作者写回READY。** LIFT中心争议隔离、AMIE受限标准及Ch81具体已有覆盖、Google Pubs有限恢复均通过，见[第三批裁决](../_sources/daily-20250502/review-supplement-20261007.md#第三批本轮内容闭合冻结日期校验仍未通过)。新增标准审阅完成1、具体已有覆盖1、实际Books写入0；74日期潜力和历史来源缺口继续隔离，不正面采用、不授全Coverage/Evidence或无遗漏。唯一当前停点为冻结旧值的V3校验兼容，不是论文未读或必要外部材料缺失；保留进行中、校验未通过，不计整日验收。

## 2. 来源覆盖

本轮仅每日组，无每周全站扫描。实际URL、请求参数、UTC执行时刻及原件见[同日补查](../_sources/daily-20250502/supplement-20261007.md)和[请求索引](../_sources/daily-20250502/supplement-20261007/request-index.md)；当前目录/失败/越界空响应均不作为历史零命中。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/release直接请求403；网页检索恢复研究首页并定点May1 Monday GPT退休说明和Responses/Files事故页；事故短更新读到末尾，不跨历史队列。 | 受阻 | 历史Research条目目录未恢复；搜索没有命中不证明无研究。事故无cause/机制复盘；不由resolved推出安全。 |
| SRC-ANTHROPIC | Research/news当前页；定点/news/integrations官方跳转claude.com，核心全文标May1，June3扩可用plan分离；root核后产品可用性贡献前关闭，不评分/不签Books已有覆盖。 | 已检查 | 仅恢复此具名发布，不保证全站无遗漏；版本为当前官方迁移页，不伪称May1网页快照。 |
| SRC-GOOGLE-AI | DeepMind publications page1/9的year无效，不续9页。Blog /2025/05的9行日期标题切片及AMIE核心/评价/限制已读。Google Pubs实际GET category=2025&search=language model，200且2025 checkbox选中，首页15/37仅读身份/年份；同category搜索May 1, 2025为0条。均停page1，不取其余22/年度正文。 | 受阻 | 恢复了有限年度主题目录，未恢复May1首公开日期；日期文本0条不证明无事件。AMIE May1 Blog与May6 paper、当前页2026-10-06发表更新分开；DeepMind与Pubs日期缺口保留，不能授历史无遗漏。 |
| SRC-META-AI | Research当前页和具名May1 Cutouts核心全文；读SAM2.1此前fall2024训练、Torch Inductor及H100吞吐/首帧延迟；root已读短文，关闭保持。 | 受阻 | 无法由当前Research恢复May1完整历史目录；本文未披露新compiler/执行机制归因，不计无遗漏。 |
| SRC-QWEN | 官方首页及/page/2/的日期/标题，May1位置相邻Qwen3 Apr29与Qwen3Embedding Jun5；在第2页日期包围停止。 | 已检查 | 只支持此两页博客日期切片无May1行，不证明论文或GitHub全部渠道无事件。 |
| SRC-DEEPSEEK | 官方首页当前模型与具名日期搜索；/news实际转到First API Call当前文档，不是News历史目录，读到文档页末即止。 | 受阻 | 错误目录/无搜索结果不能授无命中；需要May1官方研究/发布列表快照。 |
| SRC-MOONSHOT | Kimi Platform Blog可见列表按日期核到May6长思考、Apr7价格调整及Mar3Muon/Feb19MoBA；May1处无行；不扫GitHub全历史。 | 已检查 | 只支持该官方博客当前保留列表的日期切片，不声称所有repository版本无事件。 |
| SRC-TENCENT-HUNYUAN | Research动态shell；已尝试IAB，超时/子agent不支持隐藏visibility，未取得浏览器证据。由官方JS恢复api.hunyuan.tencent.com/api/blog/publicList，POST pageNum1/pageSize20/renderType0，total9/list9全为2026，停page1。 | 受阻 | 当前研究目录不提供2025；错误host404保留但不作阴性。需May1全部列表或当期具名条目快照，不据访问失败写不适用。 |
| SRC-ZAI | 首查官方Research，当前展示2026至Dec2025；?year=2025&month=5无效返回同页；具名日期搜索未恢复May1，停止当前页。 | 受阻 | 缺历史Research目录，不扫描嵌入全机构论文历年数据；需May1条目快照。 |
| SRC-BYTEDANCE-SEED | 官方JS恢复get_article_list_v2，publish_year2025/order_desctrue/count20；blog type2 token0→20日期跨Jul14/May12→Apr23，stop20；已并发取到40只保留日期导航，不建筛选队列。papers type1且x-tt-localeUS token0→20→40，page40 May17→Mar22，May2→Apr25包围，stop40（不取60）。 | 已检查 | 无May1门户发布行仅限该日期切片；门户publishDate不是原论文首公开，不能替代arXiv日期。错误type0/缺locale空response明确无阴性权限。 |
| SRC-BAIDU-ERNIE | 技术博客首页和page2日期导航读到最早Jun30 2025，停止page2；没有恢复May1，不扫repo全历史。 | 受阻 | 最早当前保留条目不是源成立日；需要May1官方论文/技术博客列表，不写不适用。 |
| SRC-XIAOMI-MIMO | 官方首页current首newsMay12及官方MiMo README当前HEAD，用于身份/日期导航，未冻结代码版本；停止首页+README。 | 受阻 | 未恢复May1历史发布，不将Apr30已知身份静默搬入本日。需要May1官方变更/发布快照；不能用HEAD日期证明v1。 |
| SRC-MINIMAX | 英文/中文blog（中文官方redirect minimax.cn）可见日期段至Jan15 2025；技术blog官方页当前仅May13 2026，止本页。 | 受阻 | 当前保留博客日期片段没有May1行，不代表全部研究release无事件；无零命中/不适用推断。 |
| SRC-ARXIV | 4具名Advanced主题：language model；LLM AND inference；vision language OR world model OR video generation；agent AND LLM。CS含crosslist，first-submitted Apr29～30仅发现，size100，announced_date_first；model101按start0/100读完，systems10/multi11/agent12单页读完；134出现→110唯一完整题摘，root校准74日期隔离潜力+36关闭，非formal；LIFT另保留中心机制争议。官方月表cs.DC May skip0/show25只浏览标题到#8；cs.CL Apr skip1500/show100只浏览到#1506，不扫全分类。 | 受阻 | 公告年月/提交不是May1公开日期。API模型total187首100未筛选不分页；错误400/404/越界空列表均不作阴性；宽May2提交query已收窄而非转待办队列。CaGR-RAG从月表定点读题摘，v1提交May2只作窗外线索，不计本窗候选。 |

## 3. 候选与判断

旧26行公开日/评分/审阅/Books决定保持原值。Anthropic原拟准入已关闭；新增AMIE是May1官方博客事件，准入5分、受限标准证据及Ch81具体已有覆盖均已独核通过。74日期未定潜力仅放§5，不用submitted或后出论文搬日。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Position Paper: Towards Open Complex Human-AI Agents Collaboration Systems for Problem Solving and Knowledge Management](https://arxiv.org/html/2505.00018v1) | 2025-05-02 | 把 human/agent initiative、并发协作、knowledge backbone 与 epistemic promotion gate 表达为分层 Petri-net control state，使临时候选与已验证共享知识保持不同提交权限。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `AGENT-MULTI-AGENT` [章节](../../../../books/part-07-agent/82-multi-agent.md#L269)；原决定不动 |
| [An Empirical Study on Prompt Compression for Large Language Models](https://arxiv.org/html/2505.00019v1) | 2025-05-02 | 把 prompt compression 视为有损 context transformation：压缩率、任务语义、position distribution 与 evaluator 必须共同进入 run identity，并保留原始上下文回退。；3 + 2 + 2 = 7（原评分冻结） | 深入完成 | 已有覆盖 `MODEL-LONG-CONTEXT` [章节](../../../../books/part-02-model/22-long-context.md#L559)；原决定不动 |
| [Beyond Public Access in LLM Pre-Training Data](https://arxiv.org/html/2505.00020v1) | 2025-05-02 | 区分 public availability 与实际训练 membership：数据访问许可、抓取快照、dedup 与 membership inference 只能提供不同强度的 provenance evidence。；3 + 2 + 2 = 7（原评分冻结） | 深入完成 | 已有覆盖 `TRAIN-DATA` [章节](../../../../books/part-04-training-system/27-data.md#L762)；原决定不动 |
| [Nemotron-Research-Tool-N1: Exploring Tool-Using Language Models with Reinforced Reasoning](https://arxiv.org/html/2505.00024v1) | 2025-05-02 | 把 tool-calling post-training 拆成 schema-conditioned trajectory generation、verifiable reward 与执行反馈；reward 只能消费工具接口已有的确定性 receipt。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `AGENT-TOOL-CALLING` [章节](../../../../books/part-07-agent/78-tool-calling.md#L440)；原决定不动 |
| [MCMComm: Hardware-Software Co-Optimization for End-to-End Communication in Multi-Chip-Modules](https://arxiv.org/html/2505.00041v1) | 2025-05-02 | 把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `INFER-GPU-MEMORY` [章节](../../../../books/part-05-inference-system/54-gpu-memory.md#L416)；原决定不动 |
| [ConSens: Assessing context grounding in open-book question answering](https://arxiv.org/html/2505.00065v1) | 2025-05-02 | 把 context grounding 评估拆成 claim、support span 与一致性 sensor，并用多组验证实验刻画 evaluator calibration，而不是把单一 judge score 当真值。；3 + 2 + 2 = 7（原评分冻结） | 深入完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#L1174)；原决定不动 |
| [Optimization of embeddings storage for RAG systems using quantization and dimensionality reduction techniques](https://arxiv.org/html/2505.00105v1) | 2025-05-02 | 把 embedding compression 放到 retrieval contract 内：storage precision、distance distortion、index revision 与 recall/latency slice 必须一起冻结。；3 + 3 + 2 = 8（原评分冻结） | 深入完成 | 已有覆盖 `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md#L592)；原决定不动 |
| [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/html/2505.00212v1) | 2025-05-02 | 多 Agent debugging 必须保存 agent、step、tool result 与 shared-state revision；LLM attribution 只产生 diagnostic evidence，不能直接成为 rollback 或责任裁决。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `PLATFORM-TRACE` [章节](../../../../books/part-06-ai-infrastructure/69-trace.md#L180)；原决定不动 |
| [Scaling On-Device GPU Inference for Large Generative Models](https://arxiv.org/html/2505.00232v1) | 2025-05-02 | on-device runtime 要把逻辑 tensor 与物理 GPU object 分离，再由 device specialization、memory manager、fusion 和 prefill/decode plan materialize；模型语义不应绑定单一 GPU API。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `INFER-TENSORRT-LLM` [章节](../../../../books/part-05-inference-system/49-tensorrt-llm.md#L20)；原决定不动 |
| [Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks](https://arxiv.org/html/2505.00234v1) | 2025-05-02 | 成功轨迹可以成为下次决策的候选 memory，但 source task、policy version、outcome verifier、selection 与 deletion policy 必须随 exemplar 保存；成功一次不等于普适规则。；2 + 2 + 3 = 7（原评分冻结） | 深入完成 | 已有覆盖 `AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md#L800)；原决定不动 |
| [AVA: Towards Agentic Video Analytics with Vision Language Models](https://arxiv.org/html/2505.00254v1) | 2025-05-02 | 长视频 RAG 要先把连续观察压缩为带时间和来源的可修订事件图，再让 agent 在不同视图间检索；短视频直接 VLM 仍是低复杂度分支。；2 + 2 + 2 = 6（原评分冻结） | 深入完成 | 已有覆盖 `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md#L521)；原决定不动 |
| [EnronQA: Towards Personalized RAG over Private Documents](https://arxiv.org/html/2505.00263v1) | 2025-05-02 | 私有文档 RAG 的正确答案必须绑定用户、邮箱快照、权限与 retrieval receipt；benchmark 命中不证明真实企业隐私和访问控制。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md#L726)；原决定不动 |
| [Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing](https://arxiv.org/html/2505.00315v1) | 2025-05-02 | content-based sparse attention 以 selector 换取更低 attention work，但 selector error、position identity 和稀疏 kernel 决定它是否优于 dense。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `MODEL-LONG-CONTEXT` [章节](../../../../books/part-02-model/22-long-context.md#L756)；原决定不动 |
| [Edge Large AI Models: Revolutionizing 6G Networks](https://arxiv.org/html/2505.00321v1) | 2025-05-02 | 把 edge LAM 拆成 federated fine-tuning、looped tensor-parallel full training 与可迁移 microservice inference，说明 training state、placement 与 serving revision 需要跨设备边界对齐。；2 + 3 + 2 = 7（原评分冻结） | 深入完成 | 已有覆盖 `TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md#L294)；原决定不动 |
| [T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation](https://arxiv.org/html/2505.00337v1) | 2025-05-02 | 视频生成质量不能代替物理一致性；评估必须冻结物理规律、prompt、hint/counterfactual、judge 与人类协议。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `MULTIMODAL-WORLD-MODELS` [章节](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md#L857)；原决定不动 |
| [LLMPrism: Black-box Performance Diagnosis for Production LLM Training Platforms](https://arxiv.org/html/2505.00342v1) | 2025-05-02 | 当训练框架不可插桩时，网络流序列可提供 job/parallelism/phase 的旁路传感；共享流量、加密、拓扑和框架漂移会使它失效，必须回退显式 instrumentation。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `PLATFORM-MONITORING` [章节](../../../../books/part-06-ai-infrastructure/67-monitoring.md#L319)；原决定不动 |
| [Pushing the Limits of Low-Bit Optimizers: A Focus on EMA Dynamics](https://arxiv.org/html/2505.00347v1) | 2025-05-02 | 低比特 optimizer 的风险不只是静态误差：unsigned EMA 会淹没新信号，signed state 会放大方差或方向错误；状态演化决定是否还能学习。；3 + 2 + 3 = 8（原评分冻结） | 深入完成 | 已有覆盖 `TRAIN-PRETRAINING` [章节](../../../../books/part-04-training-system/28-pretraining.md#L559)；原决定不动 |
| [R&amp;B: Domain Regrouping and Data Mixture Balancing for Efficient Foundation Model Training](https://arxiv.org/html/2505.00358v1) | 2025-05-02 | 数据域不能永久沿用人工标签；可由表示和梯度反馈重组，但 estimator、mixture revision 与 drift fallback 必须纳入 lineage。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `TRAIN-DATA` [章节](../../../../books/part-04-training-system/27-data.md#L910)；原决定不动 |
| [SacFL: Self-Adaptive Federated Continual Learning for Resource-Constrained End Devices](https://arxiv.org/html/2505.00365v1) | 2025-05-02 | 在 federated continual learning 中联合管理 client data drift、历史知识 retention、资源预算与异常 task admission，说明一轮上传不能只携带无类型 model delta。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `TRAIN-DISTRIBUTED-TRAINING` [章节](../../../../books/part-04-training-system/36-distributed-training.md#L294)；原决定不动 |
| [Distributed Retrieval-Augmented Generation](https://arxiv.org/html/2505.00443v1) | 2025-05-02 | 分布式 RAG 将 corpus ownership 留在 peer，并以 topic-aware discovery 代替中央索引；它减少集中收集，却不会自动提供 query privacy、信任或一致性。；2 + 3 + 2 = 7（原评分冻结） | 深入完成 | 已有覆盖 `AGENT-RAG` [章节](../../../../books/part-07-agent/76-rag.md#L529)；原决定不动 |
| [Memory-Centric Computing: Solving Computing's Memory Problem](https://arxiv.org/html/2505.00458v1) | 2025-05-02 | 把 AI 系统瓶颈从算力单点扩展到 memory movement、capacity hierarchy 与 near-data execution；它是既有异构内存设计线的系统性证据。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `INFER-GPU-MEMORY` [章节](../../../../books/part-05-inference-system/54-gpu-memory.md#L333)；原决定不动 |
| [A General Framework for Property-Driven Machine Learning](https://arxiv.org/html/2505.00466v1) | 2025-05-02 | 把 ML acceptance 从平均 task score 扩展为显式 property specification、test generation 与 deployment gate，使需求、数据、模型与 verifier 可追踪。；3 + 2 + 2 = 7（原评分冻结） | 深入完成 | 已有覆盖 `PLATFORM-PRODUCTION` [章节](../../../../books/part-06-ai-infrastructure/73-production-best-practice.md#L242)；原决定不动 |
| [HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection](https://arxiv.org/html/2505.00506v1) | 2025-05-02 | hallucination detector 的分数只属于给定任务、来源、长度和 evaluator；跨来源平均值不能替代 slice 与 calibration。；2 + 2 + 2 = 6（原评分冻结） | 标准完成 | 已有覆盖 `PLATFORM-EVALUATION-SYSTEM` [章节](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#L2773)；原决定不动 |
| [FreqKV: Key-Value Compression in Frequency Domain for Context Window Extension](https://arxiv.org/html/2505.00570v1) | 2025-05-02 | 频域 KV 压缩用有损 summary 延伸窗口；频率分配、RoPE/position identity 与关键 token 丢失决定它何时必须回退 FullKV。；3 + 2 + 3 = 8（原评分冻结） | 深入完成 | 已有覆盖 `INFER-KV-CACHE` [章节](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L481)；原决定不动 |
| [The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (and How to Fix Them)](https://arxiv.org/html/2505.00626v1) | 2025-05-02 | 证明模型可能用 position ID 等旁路信号学习 role shortcut；instruction hierarchy 必须携带 authenticated provenance，不能把 token placement 当 authority。；3 + 3 + 3 = 9（原评分冻结） | 深入完成 | 已有覆盖 `PLATFORM-SECURITY` [章节](../../../../books/part-06-ai-infrastructure/72-security.md#L1197)；原决定不动 |
| [Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics](https://arxiv.org/html/2505.00675v1) | 2025-05-02 | 把 agent memory 从 storage taxonomy 重构为 parametric/contextual representation 与 consolidation、updating、indexing、forgetting、retrieval、condensation 六类显式操作，使 lifecycle 风险能落到具体 transition。；2 + 2 + 3 = 7（原评分冻结） | 深入完成 | 已有覆盖 `AGENT-MEMORY` [章节](../../../../books/part-07-agent/77-memory.md#L1185)；原决定不动 |

| [AMIE gains vision（May1官方事件）](https://research.google/blog/amie-gains-vision-a-research-ai-agent-for-multi-modal-diagnostic-dialogue/) | 2025-05-01 | 隐式对话追踪→state/knowledge gaps驱动phase目标判断及主动请求观察→比较状态控制/过早停止边界；2 + 1 + 2 = 5（准入/评分已独核通过） | 标准完成 | 已有覆盖 `AGENT-WORKFLOW` [Ch81具体正文](../../../../books/part-07-agent/81-workflow.md#clarification-与-workflow-level-speculation-都是有损-admission)；§4受限标准及具体已有覆盖已获root第三批通过，无共享写入 |

## 4. 证据与知识整合

### 本轮具名改判

root已实际完整首读110题摘及机构core，并实际读18个具名exact-v1 core及AMIE §2.1/C.3/C.4，通过五P→C与AMIE准入5分。当前74P/36C、110分母不变且非formal；[首裁决原件](../_sources/daily-20250502/review-supplement-20261007.md)不由作者改写通过。LIFT按最新R1明确为中心可微实现缺口：离散pred→compiler→ProGraML→冻结GNN的loss不能仅因加CE就回传LLM，明确不采用“GNN监督已直接更新LLM”；保留P/争议，重开须可接受surrogate、gradient estimator、implementation或不依赖该声称的证据，不能改C/降分绕过。其余未受影响18不重读。LIFT隔离已获root第三批通过。实际写回见[差额](../_sources/daily-20250502/core-revisions-20261007.md)，未授DAY。

### [AMIE gains vision（May1官方事件）](https://research.google/blog/amie-gains-vision-a-research-ai-agent-for-multi-modal-diagnostic-dialogue/)

本轮实际读保存的官方Blog第113～195行：state/knowledge gaps驱动三phase目标判断，主动请求图像并据观察更新；采用这个可比较的软控制分支，不采用phase正确性、临床优越/安全或durable验收保证。该页为当前官方版本，明确带2026-10-06发表更新，不冒充May1网页快照；May6 paper的profile/独立continuation/DDx validation仅后续澄清，不回投May1。

博客主模型Gemini2.0 Flash；PTB-XL/SCIN衍生场景经Gemini/web增强、模拟patient和auto-rater存在相关评价链。105案例的虚拟OSCE为聊天+artifact上传、patient actors/PCPs及specialist/actor评价，是整套系统比较而非controller等预算消融；2.5对2.0改变base，不能归因phase。病例/演员、缺通常临床工具、非实时音视频限制外推，计划中的真实研究不是完成验证。calls/tokens、长度、hardware/precision、batch/concurrency、SLO/latency和独立控制成本均Not Disclosed，不采用临床数字或声称实现复现；详见[受限标准Evidence](../_sources/daily-20250502/core-revisions-20261007.md#本轮受限标准evidence)。

Books决定为**已有覆盖，root第三批已独核通过**：`AGENT-WORKFLOW`/Ch81实际正文110～120行已有stage/observation/evidence对齐，145～165行已有deterministic spine与model提案分权；205～215行已有证据寻找、实际观察与充分性/终止判定边界；247～265行已有逐轮state history、uncertainty evidence决定ask/proceed且不合并action authority；1137～1171行已有hard/soft及completion/admission区别。AMIE软phase未证明达到书中的独立inspector/hard gate，不能作为增强保证。root实际回读Ch81相关正文及Ch80/82责任边界，并核Blog方法/评价/限制后通过受限标准和No Change；不是主题映射代替差额，也不是因此撤销准入，没有共享写入。

### 原有效证据复用边界

原完整报告及原exact-v1原件保留；以下原review/Books判断文字逐项复用，方法、评价、反证和artifact位置不变，原benchmark约束与三条演进分析见[原档案](../_sources/daily-20250502/baseline-before-supplement-20261007.md)。没有影响这26家族原证据的新撤回/勘误信号被确认，本轮未因此重新审所有旧全文；该复用不授新增补查验收。

### [Position Paper: Towards Open Complex Human-AI Agents Collaboration Systems for Problem Solving and Knowledge Management](https://arxiv.org/html/2505.00018v1)

原家族 `SF-2025-HAACS`，精确版本 `arXiv:2505.00018v1`，原审阅身份 `RP-9226d76a21f62c83`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00018v1#S9.SS2；评价：Not Disclosed — position paper provides no controlled end-to-end evaluation；反证/限制：https://arxiv.org/html/2505.00018v1#S9.SS6；实现：Not Required — Standard Review。

<!-- review:SF-2025-HAACS:start --><!-- claim:SF-2025-HAACS:start -->把 human/agent initiative、并发协作、knowledge backbone 与 epistemic promotion gate 表达为分层 Petri-net control state，使临时候选与已验证共享知识保持不同提交权限。<!-- claim:SF-2025-HAACS:end -->

这是 position paper 与综合性架构主张，没有实现 artifact 或端到端实证；只能作为 owner-boundary 提案，不能把 HE2-Net 视为已验证的生产协调协议。<!-- review:SF-2025-HAACS:end -->

<!-- books-review:SF-2025-HAACS:start --><!-- existing:SF-2025-HAACS:start -->Multi-Agent 已要求 coordination state、owner 与 commit transition 分离，Workflow 章也把并行 DAG、task、placement 与 commit 拆开。<!-- existing:SF-2025-HAACS:end --><!-- delta:SF-2025-HAACS:start -->把 human/agent initiative、并发协作、knowledge backbone 与 epistemic promotion gate 表达为分层 Petri-net control state，使临时候选与已验证共享知识保持不同提交权限。<!-- delta:SF-2025-HAACS:end -->

这是 position paper 与综合性架构主张，没有实现 artifact 或端到端实证；只能作为 owner-boundary 提案，不能把 HE2-Net 视为已验证的生产协调协议。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-HAACS:end -->

### [An Empirical Study on Prompt Compression for Large Language Models](https://arxiv.org/html/2505.00019v1)

原家族 `SF-2025-PROMPT-COMPRESSION`，精确版本 `arXiv:2505.00019v1`，原审阅身份 `RP-1e25d6df19c65ad4`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00019v1#S3；评价：https://arxiv.org/html/2505.00019v1#S5；反证/限制：https://arxiv.org/html/2505.00019v1#S6；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-PROMPT-COMPRESSION:start --><!-- claim:SF-2025-PROMPT-COMPRESSION:start -->把 prompt compression 视为有损 context transformation：压缩率、任务语义、position distribution 与 evaluator 必须共同进入 run identity，并保留原始上下文回退。<!-- claim:SF-2025-PROMPT-COMPRESSION:end -->

经验结果绑定论文模型与任务，不构成跨模型最优压缩率或长上下文质量定律。<!-- review:SF-2025-PROMPT-COMPRESSION:end -->

<!-- books-review:SF-2025-PROMPT-COMPRESSION:start --><!-- existing:SF-2025-PROMPT-COMPRESSION:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PROMPT-COMPRESSION:end --><!-- delta:SF-2025-PROMPT-COMPRESSION:start -->把 prompt compression 视为有损 context transformation：压缩率、任务语义、position distribution 与 evaluator 必须共同进入 run identity，并保留原始上下文回退。<!-- delta:SF-2025-PROMPT-COMPRESSION:end -->

经验结果绑定论文模型与任务，不构成跨模型最优压缩率或长上下文质量定律。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PROMPT-COMPRESSION:end -->

### [Beyond Public Access in LLM Pre-Training Data](https://arxiv.org/html/2505.00020v1)

原家族 `SF-2025-PRETRAIN-DATA-MEMBERSHIP`，精确版本 `arXiv:2505.00020v1`，原审阅身份 `RP-24b4eee40467e6b0`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00020v1#S2；评价：https://arxiv.org/html/2505.00020v1#S3.SS1；反证/限制：https://arxiv.org/html/2505.00020v1#S3.SS4；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start --><!-- claim:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->区分 public availability 与实际训练 membership：数据访问许可、抓取快照、dedup 与 membership inference 只能提供不同强度的 provenance evidence。<!-- claim:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

membership inference 是统计 sensor；论文数据和模型上的结果不能证明某个未披露训练集成员关系，更不能替代法律许可判断。<!-- review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

<!-- books-review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start --><!-- existing:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end --><!-- delta:SF-2025-PRETRAIN-DATA-MEMBERSHIP:start -->区分 public availability 与实际训练 membership：数据访问许可、抓取快照、dedup 与 membership inference 只能提供不同强度的 provenance evidence。<!-- delta:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

membership inference 是统计 sensor；论文数据和模型上的结果不能证明某个未披露训练集成员关系，更不能替代法律许可判断。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PRETRAIN-DATA-MEMBERSHIP:end -->

### [Nemotron-Research-Tool-N1: Exploring Tool-Using Language Models with Reinforced Reasoning](https://arxiv.org/html/2505.00024v1)

原家族 `SF-2025-NEMOTRON-TOOL-N1`，精确版本 `arXiv:2505.00024v1`，原审阅身份 `RP-08510693c8e25bbc`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00024v1#S4；评价：https://arxiv.org/html/2505.00024v1#S5；反证/限制：https://arxiv.org/html/2505.00024v1#S6；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-NEMOTRON-TOOL-N1:start --><!-- claim:SF-2025-NEMOTRON-TOOL-N1:start -->把 tool-calling post-training 拆成 schema-conditioned trajectory generation、verifiable reward 与执行反馈；reward 只能消费工具接口已有的确定性 receipt。<!-- claim:SF-2025-NEMOTRON-TOOL-N1:end -->

结果绑定作者数据生成、工具集合和 evaluator；不能证明开放工具生态、权限副作用或分布外 schema 下同样可靠。<!-- review:SF-2025-NEMOTRON-TOOL-N1:end -->

<!-- books-review:SF-2025-NEMOTRON-TOOL-N1:start --><!-- existing:SF-2025-NEMOTRON-TOOL-N1:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-NEMOTRON-TOOL-N1:end --><!-- delta:SF-2025-NEMOTRON-TOOL-N1:start -->把 tool-calling post-training 拆成 schema-conditioned trajectory generation、verifiable reward 与执行反馈；reward 只能消费工具接口已有的确定性 receipt。<!-- delta:SF-2025-NEMOTRON-TOOL-N1:end -->

结果绑定作者数据生成、工具集合和 evaluator；不能证明开放工具生态、权限副作用或分布外 schema 下同样可靠。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-NEMOTRON-TOOL-N1:end -->

### [MCMComm: Hardware-Software Co-Optimization for End-to-End Communication in Multi-Chip-Modules](https://arxiv.org/html/2505.00041v1)

原家族 `SF-2025-MCMCOMM`，精确版本 `arXiv:2505.00041v1`，原审阅身份 `RP-1f9e4e92cafcd4ca`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00041v1#S4; #S5；评价：https://arxiv.org/html/2505.00041v1#S7；反证/限制：https://arxiv.org/html/2505.00041v1#S8；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-MCMCOMM:start --><!-- claim:SF-2025-MCMCOMM:start -->把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。<!-- claim:SF-2025-MCMCOMM:end -->

分析与评估绑定作者的 MCM design space、模型集合及 analytical assumptions；没有公开冻结实现，不能把模拟收益外推到任意封装、互连或真实 congestion。<!-- review:SF-2025-MCMCOMM:end -->

<!-- books-review:SF-2025-MCMCOMM:start --><!-- existing:SF-2025-MCMCOMM:start -->GPU Memory 已把 chiplet locality 的 layout/placement 设为联合 owner，Distributed Training 也要求 topology mapping 先于执行。<!-- existing:SF-2025-MCMCOMM:end --><!-- delta:SF-2025-MCMCOMM:start -->把 chiplet accelerator 的 communication cost 从软件映射单点扩展为 packaging、HBM/DRAM path、workload allocation 与 execution overlap 的联合优化对象；layout 与 placement 必须共同版本化。<!-- delta:SF-2025-MCMCOMM:end -->

分析与评估绑定作者的 MCM design space、模型集合及 analytical assumptions；没有公开冻结实现，不能把模拟收益外推到任意封装、互连或真实 congestion。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MCMCOMM:end -->

### [ConSens: Assessing context grounding in open-book question answering](https://arxiv.org/html/2505.00065v1)

原家族 `SF-2025-CONSENS-CONTEXT-GROUNDING`，精确版本 `arXiv:2505.00065v1`，原审阅身份 `RP-9daf94a9490bf191`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00065v1#S2；评价：https://arxiv.org/html/2505.00065v1#S3；反证/限制：https://arxiv.org/html/2505.00065v1#S4；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-CONSENS-CONTEXT-GROUNDING:start --><!-- claim:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->把 context grounding 评估拆成 claim、support span 与一致性 sensor，并用多组验证实验刻画 evaluator calibration，而不是把单一 judge score 当真值。<!-- claim:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

验证覆盖论文数据集和 judge 配置；相关性不证明事实正确，也不能替代 retrieval-stage provenance。<!-- review:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

<!-- books-review:SF-2025-CONSENS-CONTEXT-GROUNDING:start --><!-- existing:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-CONSENS-CONTEXT-GROUNDING:end --><!-- delta:SF-2025-CONSENS-CONTEXT-GROUNDING:start -->把 context grounding 评估拆成 claim、support span 与一致性 sensor，并用多组验证实验刻画 evaluator calibration，而不是把单一 judge score 当真值。<!-- delta:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

验证覆盖论文数据集和 judge 配置；相关性不证明事实正确，也不能替代 retrieval-stage provenance。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-CONSENS-CONTEXT-GROUNDING:end -->

### [Optimization of embeddings storage for RAG systems using quantization and dimensionality reduction techniques](https://arxiv.org/html/2505.00105v1)

原家族 `SF-2025-EMBEDDING-QUANTIZATION`，精确版本 `arXiv:2505.00105v1`，原审阅身份 `RP-80ea5a839a23f316`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00105v1#S4；评价：https://arxiv.org/html/2505.00105v1#S5；反证/限制：https://arxiv.org/html/2505.00105v1#S6；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-EMBEDDING-QUANTIZATION:start --><!-- claim:SF-2025-EMBEDDING-QUANTIZATION:start -->把 embedding compression 放到 retrieval contract 内：storage precision、distance distortion、index revision 与 recall/latency slice 必须一起冻结。<!-- claim:SF-2025-EMBEDDING-QUANTIZATION:end -->

PCA/quantization 的收益绑定论文数据、embedding model 与索引设置；没有证明所有语义空间或 ANN backend 都保持排序。<!-- review:SF-2025-EMBEDDING-QUANTIZATION:end -->

<!-- books-review:SF-2025-EMBEDDING-QUANTIZATION:start --><!-- existing:SF-2025-EMBEDDING-QUANTIZATION:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-EMBEDDING-QUANTIZATION:end --><!-- delta:SF-2025-EMBEDDING-QUANTIZATION:start -->把 embedding compression 放到 retrieval contract 内：storage precision、distance distortion、index revision 与 recall/latency slice 必须一起冻结。<!-- delta:SF-2025-EMBEDDING-QUANTIZATION:end -->

PCA/quantization 的收益绑定论文数据、embedding model 与索引设置；没有证明所有语义空间或 ANN backend 都保持排序。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-EMBEDDING-QUANTIZATION:end -->

### [Which Agent Causes Task Failures and When? On Automated Failure Attribution of LLM Multi-Agent Systems](https://arxiv.org/html/2505.00212v1)

原家族 `SF-2025-WHOWHEN`，精确版本 `arXiv:2505.00212v1`，原审阅身份 `RP-78dcb9f50b93cecd`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00212v1#S2; https://arxiv.org/html/2505.00212v1#S3; https://arxiv.org/html/2505.00212v1#A2；评价：https://arxiv.org/html/2505.00212v1#S4; https://arxiv.org/html/2505.00212v1#A4；反证/限制：https://arxiv.org/html/2505.00212v1#S6; https://arxiv.org/html/2505.00212v1#S7；实现：https://github.com/mingyin1/Agents_Failure_Attribution — repository linked from exact-v1。

<!-- review:SF-2025-WHOWHEN:start --><!-- claim:SF-2025-WHOWHEN:start -->多 Agent debugging 必须保存 agent、step、tool result 与 shared-state revision；LLM attribution 只产生 diagnostic evidence，不能直接成为 rollback 或责任裁决。<!-- claim:SF-2025-WHOWHEN:end -->论文标注 127 个 systems、184 个 failed tasks，比较三种定位流程与 context/cost sensitivity。结果显示全局 receptive field、局部 step precision 和 token cost 冲突；judge bias、shared cause、single-blame 标签与隐私限制因果解释。<!-- review:SF-2025-WHOWHEN:end -->

<!-- books-review:SF-2025-WHOWHEN:start --><!-- existing:SF-2025-WHOWHEN:start -->Trace 章已区分 immutable event、step/agent attribution、diagnostic confidence 与因果 authority。<!-- existing:SF-2025-WHOWHEN:end --><!-- delta:SF-2025-WHOWHEN:start -->Who&When 的 all-at-once、stepwise 与 binary-search judge 已作为 failure attribution 边界被承载。<!-- delta:SF-2025-WHOWHEN:end -->演进关系为 Layering / Dependency；目标 `PLATFORM-TRACE` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-WHOWHEN:end -->

### [Scaling On-Device GPU Inference for Large Generative Models](https://arxiv.org/html/2505.00232v1)

原家族 `SF-2025-ML-DRIFT`，精确版本 `arXiv:2505.00232v1`，原审阅身份 `RP-423c3e08352153c9`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00232v1#S3; https://arxiv.org/html/2505.00232v1#S3.SS7; https://arxiv.org/html/2505.00232v1#S3.SS8；评价：https://arxiv.org/html/2505.00232v1#S4; https://arxiv.org/html/2505.00232v1#S4.SS2；反证/限制：https://arxiv.org/html/2505.00232v1#S5；实现：Not Disclosed — exact-v1 describes the framework but does not identify a frozen public ML Drift repository。

<!-- review:SF-2025-ML-DRIFT:start --><!-- claim:SF-2025-ML-DRIFT:start -->on-device runtime 要把逻辑 tensor 与物理 GPU object 分离，再由 device specialization、memory manager、fusion 和 prefill/decode plan materialize；模型语义不应绑定单一 GPU API。<!-- claim:SF-2025-ML-DRIFT:end -->论文跨 mobile、desktop/laptop 与 Apple Silicon 测试 diffusion/LLM，并给出 virtualization、coordinate translation、memory、fusion 和 KV layout。作者 benchmark 受设备、driver、model 与 precision 约束；跨设备实现复杂度、memory pressure 和 fallback coverage 是代价。<!-- review:SF-2025-ML-DRIFT:end -->

<!-- books-review:SF-2025-ML-DRIFT:start --><!-- existing:SF-2025-ML-DRIFT:start -->Execution 章已把 logical tensor、device-specific layout、memory placement、fusion 与 prefill/decode 分支纳入 plan identity。<!-- existing:SF-2025-ML-DRIFT:end --><!-- delta:SF-2025-ML-DRIFT:start -->ML Drift 的 tensor virtualization、coordinate translation 与 stage-aware optimization 是同一机制在 heterogeneous on-device GPU 上的实现。<!-- delta:SF-2025-ML-DRIFT:end -->演进关系为 Layering / Dependency；目标 `INFER-TENSORRT-LLM` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-ML-DRIFT:end -->

### [Self-Generated In-Context Examples Improve LLM Agents for Sequential Decision-Making Tasks](https://arxiv.org/html/2505.00234v1)

原家族 `SF-2025-TRAJ-BOOTSTRAP`，精确版本 `arXiv:2505.00234v1`，原审阅身份 `RP-4c25305c7c594b33`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00234v1#S5; https://arxiv.org/html/2505.00234v1#A4；评价：https://arxiv.org/html/2505.00234v1#S6; https://arxiv.org/html/2505.00234v1#A5; https://arxiv.org/html/2505.00234v1#A6；反证/限制：https://arxiv.org/html/2505.00234v1#S7; https://arxiv.org/html/2505.00234v1#A2；实现：Not Disclosed — exact-v1 does not identify a released trajectory database implementation。

<!-- review:SF-2025-TRAJ-BOOTSTRAP:start --><!-- claim:SF-2025-TRAJ-BOOTSTRAP:start -->成功轨迹可以成为下次决策的候选 memory，但 source task、policy version、outcome verifier、selection 与 deletion policy 必须随 exemplar 保存；成功一次不等于普适规则。<!-- claim:SF-2025-TRAJ-BOOTSTRAP:end -->论文从 agent 自己的成功 experience 构建数据库并做 database/exemplar selection，在 ALFWorld、Wordcraft、InterCode-SQL 评估。收益受 benchmark、initial examples、retriever 和 growing-context cost 限制；feedback loop 会固化偶然成功或污染，人工示例在高风险/低数据时仍合理。<!-- review:SF-2025-TRAJ-BOOTSTRAP:end -->

<!-- books-review:SF-2025-TRAJ-BOOTSTRAP:start --><!-- existing:SF-2025-TRAJ-BOOTSTRAP:start -->Memory 章已把 successful trajectory 转换为可撤销 derived memory，并要求 provenance、selection、forgetting 与 held-out evaluation。<!-- existing:SF-2025-TRAJ-BOOTSTRAP:end --><!-- delta:SF-2025-TRAJ-BOOTSTRAP:start -->Traj-Bootstrap 的 database/exemplar selection 是已有 derived-memory admission 的实例。<!-- delta:SF-2025-TRAJ-BOOTSTRAP:end -->演进关系为 Direct Evolution；目标 `AGENT-MEMORY` 与相邻章节已读。当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-TRAJ-BOOTSTRAP:end -->

### [AVA: Towards Agentic Video Analytics with Vision Language Models](https://arxiv.org/html/2505.00254v1)

原家族 `SF-2025-AVA`，精确版本 `arXiv:2505.00254v1`，原审阅身份 `RP-5d482f3eeba8e5e3`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00254v1 — exact-v1 §3 system overview；§4 index construction；§4.1 Event KG；评价：https://arxiv.org/html/2505.00254v1 — exact-v1 §5 agentic retrieval；§6 implementation；§7 evaluation；反证/限制：https://arxiv.org/html/2505.00254v1 — exact-v1 §8 limitations；实现：Not Disclosed — linked implementation revision is not frozen in the paper。

<!-- review:SF-2025-AVA:start --><!-- claim:SF-2025-AVA:start -->长视频 RAG 要先把连续观察压缩为带时间和来源的可修订事件图，再让 agent 在不同视图间检索；短视频直接 VLM 仍是低复杂度分支。<!-- claim:SF-2025-AVA:end -->作者以 3 秒片段生成描述并做语义合并，构造事件/实体/时间图，再用多视图检索、MCTS 与 self-consistency 回答。AVA-100 只覆盖八段长视频和 120 个问题；描述误差、图陈旧与搜索成本会累积，不能外推为通用实时视频理解。<!-- review:SF-2025-AVA:end -->

<!-- books-review:SF-2025-AVA:start --><!-- existing:SF-2025-AVA:start -->RAG 已有 chunk/index/provenance，但缺少持续视频流如何变成可修订事件图的完整路径。<!-- existing:SF-2025-AVA:end --><!-- delta:SF-2025-AVA:start -->补充 observation→VLM description→semantic chunk→event/entity/temporal graph→tri-view retrieval/search；graph revision 与 staleness 成为 retrieval state。<!-- delta:SF-2025-AVA:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-AVA:end -->

### [EnronQA: Towards Personalized RAG over Private Documents](https://arxiv.org/html/2505.00263v1)

原家族 `SF-2025-ENRONQA`，精确版本 `arXiv:2505.00263v1`，原审阅身份 `RP-f5694b6cc89062bb`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00263v1 — exact-v1 §3 dataset construction；§4 quality；评价：https://arxiv.org/html/2505.00263v1 — exact-v1 §5 benchmarking；§6 memorized knowledge；反证/限制：https://arxiv.org/html/2505.00263v1 — exact-v1 §7 discussion；Ethics statement；实现：Not Disclosed — dataset release revision is not frozen。

<!-- review:SF-2025-ENRONQA:start --><!-- claim:SF-2025-ENRONQA:start -->私有文档 RAG 的正确答案必须绑定用户、邮箱快照、权限与 retrieval receipt；benchmark 命中不证明真实企业隐私和访问控制。<!-- claim:SF-2025-ENRONQA:end -->作者从 103,638 封邮件构造 528,304 QA，并以 150 个 inbox 测试个性化检索与模型记忆。该合同支持检索/记忆差异分析，不证明真实企业 ACL、删除、时效或隐私合规。<!-- review:SF-2025-ENRONQA:end -->

<!-- books-review:SF-2025-ENRONQA:start --><!-- existing:SF-2025-ENRONQA:start -->RAG 已把 tenant、ACL、corpus revision 与 retrieval receipt 纳入私有知识边界。<!-- existing:SF-2025-ENRONQA:end --><!-- delta:SF-2025-ENRONQA:start -->EnronQA 是个性化私有文档 RAG 的数据与评测案例，不新增 owner。<!-- delta:SF-2025-ENRONQA:end -->演进关系 `Principle Reuse`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-ENRONQA:end -->

### [Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing](https://arxiv.org/html/2505.00315v1)

原家族 `SF-2025-MOSA`，精确版本 `arXiv:2505.00315v1`，原审阅身份 `RP-e0eff22681655851`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00315v1 — exact-v1 §2 Mixture of Sparse Attention；评价：https://arxiv.org/html/2505.00315v1 — exact-v1 §3 experiments；Appendix FLOPs/model settings；反证/限制：https://arxiv.org/html/2505.00315v1 — exact-v1 §5 limitations；实现：Not Disclosed — optimized sparse kernel is not released as frozen evidence。

<!-- review:SF-2025-MOSA:start --><!-- claim:SF-2025-MOSA:start -->content-based sparse attention 以 selector 换取更低 attention work，但 selector error、position identity 和稀疏 kernel 决定它是否优于 dense。<!-- claim:SF-2025-MOSA:end -->作者在 iso-FLOP 的非自回归语言建模设置比较 expert-choice sparse attention；perplexity 优势并不总转化为下游收益，短序列较弱，且未提供优化 kernel 或 causal serving 证据。<!-- review:SF-2025-MOSA:end -->

<!-- books-review:SF-2025-MOSA:start --><!-- existing:SF-2025-MOSA:start -->Long Context 已区分 dense fallback、content selector、position identity 与 sparse-kernel cost。<!-- existing:SF-2025-MOSA:end --><!-- delta:SF-2025-MOSA:start -->把每个 attention head 视作 expert 并按 token content 选择子集，是现有 content-based sparse branch 的实现。<!-- delta:SF-2025-MOSA:end -->演进关系 `Alternative Branch`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MOSA:end -->

### [Edge Large AI Models: Revolutionizing 6G Networks](https://arxiv.org/html/2505.00321v1)

原家族 `SF-2025-EDGE-LAM`，精确版本 `arXiv:2505.00321v1`，原审阅身份 `RP-1fd50651017e3762`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00321v1#S2; #S3；评价：https://arxiv.org/html/2505.00321v1#S5；反证/限制：https://arxiv.org/html/2505.00321v1#S6；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-EDGE-LAM:start --><!-- claim:SF-2025-EDGE-LAM:start -->把 edge LAM 拆成 federated fine-tuning、looped tensor-parallel full training 与可迁移 microservice inference，说明 training state、placement 与 serving revision 需要跨设备边界对齐。<!-- claim:SF-2025-EDGE-LAM:end -->

论文主要是架构综述与 6G case study，没有完整端到端 implementation/benchmark；不能证明所述 looped TP 或 microservice migration 已满足真实 edge reliability。<!-- review:SF-2025-EDGE-LAM:end -->

<!-- books-review:SF-2025-EDGE-LAM:start --><!-- existing:SF-2025-EDGE-LAM:start -->Distributed Training 已定义 federated tensor/跨设备协议表达边界，KServe 已分离 desired/applied/observed serving state；该综述未给出新的可验证协议。<!-- existing:SF-2025-EDGE-LAM:end --><!-- delta:SF-2025-EDGE-LAM:start -->把 edge LAM 拆成 federated fine-tuning、looped tensor-parallel full training 与可迁移 microservice inference，说明 training state、placement 与 serving revision 需要跨设备边界对齐。<!-- delta:SF-2025-EDGE-LAM:end -->

论文主要是架构综述与 6G case study，没有完整端到端 implementation/benchmark；不能证明所述 looped TP 或 microservice migration 已满足真实 edge reliability。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-EDGE-LAM:end -->

### [T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation](https://arxiv.org/html/2505.00337v1)

原家族 `SF-2025-T2VPHYS`，精确版本 `arXiv:2505.00337v1`，原审阅身份 `RP-a7dd096fa6a14828`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00337v1 — exact-v1 §3 benchmark；§3.3 protocol；评价：https://arxiv.org/html/2505.00337v1 — exact-v1 §4 experiments；Appendix A implementation；反证/限制：https://arxiv.org/html/2505.00337v1 — exact-v1 §5 discussion；Appendix B limitations；实现：Not Disclosed — benchmark revision is not frozen。

<!-- review:SF-2025-T2VPHYS:start --><!-- claim:SF-2025-T2VPHYS:start -->视频生成质量不能代替物理一致性；评估必须冻结物理规律、prompt、hint/counterfactual、judge 与人类协议。<!-- claim:SF-2025-T2VPHYS:end -->作者以十二类 first-principles law 构建 benchmark 并报告受测系统平均分均低于 0.60。它诊断生成失败，不证明模型具有或缺乏可用于控制的因果 world state，也不预测真实机器人 policy success。<!-- review:SF-2025-T2VPHYS:end -->

<!-- books-review:SF-2025-T2VPHYS:start --><!-- existing:SF-2025-T2VPHYS:start -->World Model/Evaluation 已区分视频 plausibility、物理一致性、action-conditioned transition 与因果证据。<!-- existing:SF-2025-T2VPHYS:end --><!-- delta:SF-2025-T2VPHYS:start -->十二类物理规律、hint/counterfactual probe 与人工协议是既有 evaluation contract 的案例。<!-- delta:SF-2025-T2VPHYS:end -->演进关系 `Principle Reuse`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-T2VPHYS:end -->

### [LLMPrism: Black-box Performance Diagnosis for Production LLM Training Platforms](https://arxiv.org/html/2505.00342v1)

原家族 `SF-2025-LLMPRISM`，精确版本 `arXiv:2505.00342v1`，原审阅身份 `RP-45270c77721f3a37`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00342v1 — exact-v1 §III motivation；§IV methodology A-D；评价：https://arxiv.org/html/2505.00342v1 — exact-v1 §V evaluation and deployed experience A-D；反证/限制：https://arxiv.org/html/2505.00342v1 — exact-v1 §VII generalization and limits；实现：Not Disclosed — production deployment code is not public。

<!-- review:SF-2025-LLMPRISM:start --><!-- claim:SF-2025-LLMPRISM:start -->当训练框架不可插桩时，网络流序列可提供 job/parallelism/phase 的旁路传感；共享流量、加密、拓扑和框架漂移会使它失效，必须回退显式 instrumentation。<!-- claim:SF-2025-LLMPRISM:end -->论文从交换机/host 网络流推断训练任务、并行策略与阶段，并报告自 2024-10 的生产部署经验。作者的识别率和时间线误差只属于其平台与流量合同；旁路传感无法证明模型正确，也可能被共享流量或版本漂移混淆。<!-- review:SF-2025-LLMPRISM:end -->

<!-- books-review:SF-2025-LLMPRISM:start --><!-- existing:SF-2025-LLMPRISM:start -->Monitoring 已有 metrics/logs/traces 与 collective telemetry，但缺少无法植入代码时的网络流序列诊断分支。<!-- existing:SF-2025-LLMPRISM:end --><!-- delta:SF-2025-LLMPRISM:start -->补充 network-flow sequence 作为低侵入 correlated sensor，用来推断训练 job identity、并行配置、phase/timeline 与 stall；它只拥有诊断线索，不拥有 correctness。<!-- delta:SF-2025-LLMPRISM:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-LLMPRISM:end -->

### [Pushing the Limits of Low-Bit Optimizers: A Focus on EMA Dynamics](https://arxiv.org/html/2505.00347v1)

原家族 `SF-2025-SOLO`，精确版本 `arXiv:2505.00347v1`，原审阅身份 `RP-8e97daa877e57fa9`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00347v1 — exact-v1 §3 ultra-low-bit optimizer；§3.1-3.3 EMA dynamics；评价：https://arxiv.org/html/2505.00347v1 — exact-v1 §4 experiments；Appendix C settings；反证/限制：https://arxiv.org/html/2505.00347v1 — exact-v1 § Discussion/Limitations boundary — exact-v1 discussion/ablation and precision limits；实现：Not Disclosed — exact training implementation revision not frozen。

<!-- review:SF-2025-SOLO:start --><!-- claim:SF-2025-SOLO:start -->低比特 optimizer 的风险不只是静态误差：unsigned EMA 会淹没新信号，signed state 会放大方差或方向错误；状态演化决定是否还能学习。<!-- claim:SF-2025-SOLO:end -->作者用 log quantization 与 precision-specific momentum 处理 2-bit 级 Adam state，并在受限模型/训练设置比较。证据不覆盖所有 optimizer、分布式 checkpoint、故障恢复或数值格式；高精度 state 在小规模或不稳定训练中仍是基线。<!-- review:SF-2025-SOLO:end -->

<!-- books-review:SF-2025-SOLO:start --><!-- existing:SF-2025-SOLO:start -->Pretraining 已有 low-precision update、error feedback 与 role-aware optimizer state，但没有解释 EMA dynamics 的两种量化失真。<!-- existing:SF-2025-SOLO:end --><!-- delta:SF-2025-SOLO:start -->补充 unsigned EMA 的 signal swamping 与 signed state 的 variance/wrong-direction 分支；量化器、momentum precision 与 checkpoint identity 必须共同冻结。<!-- delta:SF-2025-SOLO:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-SOLO:end -->

### [R&amp;B: Domain Regrouping and Data Mixture Balancing for Efficient Foundation Model Training](https://arxiv.org/html/2505.00358v1)

原家族 `SF-2025-RNB`，精确版本 `arXiv:2505.00358v1`，原审阅身份 `RP-66cb5a5af3eebc67`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00358v1 — exact-v1 §3 regrouping and balancing；评价：https://arxiv.org/html/2505.00358v1 — exact-v1 §4 experiments；Appendix E/F implementation/settings；反证/限制：https://arxiv.org/html/2505.00358v1 — exact-v1 Appendix D cost and discussion limits；实现：Not Disclosed — exact data/control artifact revision is not frozen。

<!-- review:SF-2025-RNB:start --><!-- claim:SF-2025-RNB:start -->数据域不能永久沿用人工标签；可由表示和梯度反馈重组，但 estimator、mixture revision 与 drift fallback 必须纳入 lineage。<!-- claim:SF-2025-RNB:end -->作者以 embedding 与累计 final-layer gradient similarity 动态重组域并更新 mixture。受控实验支持样本效率，不能证明 final-layer proxy 在 frontier scale、生产漂移或不同 optimizer 下稳定；cluster churn 和 feedback cost 是新风险。<!-- review:SF-2025-RNB:end -->

<!-- books-review:SF-2025-RNB:start --><!-- existing:SF-2025-RNB:start -->Data 已把 mixture weight 视为受 gradient/coverage/evaluation 反馈约束的动态控制状态。<!-- existing:SF-2025-RNB:end --><!-- delta:SF-2025-RNB:start -->embedding+gradient regrouping 与 final-layer similarity 是该控制链的受限 estimator，不新增 owner。<!-- delta:SF-2025-RNB:end -->演进关系 `Direct Evolution`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-RNB:end -->

### [SacFL: Self-Adaptive Federated Continual Learning for Resource-Constrained End Devices](https://arxiv.org/html/2505.00365v1)

原家族 `SF-2025-SACFL`，精确版本 `arXiv:2505.00365v1`，原审阅身份 `RP-c709935ac7232342`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00365v1#S3；评价：https://arxiv.org/html/2505.00365v1#S5；反证/限制：https://arxiv.org/html/2505.00365v1#S6；实现：https://github.com/Zhong-Zhengyi/SacFL-Code — repository linked from exact-v1; revision not frozen。

<!-- review:SF-2025-SACFL:start --><!-- claim:SF-2025-SACFL:start -->在 federated continual learning 中联合管理 client data drift、历史知识 retention、资源预算与异常 task admission，说明一轮上传不能只携带无类型 model delta。<!-- claim:SF-2025-SACFL:end -->

实验覆盖作者选择的数据集、3-20 个任务与模拟/演示环境；论文未证明长期真实 client churn、secure aggregation 或不同硬件资源下的收敛与防御。<!-- review:SF-2025-SACFL:end -->

<!-- books-review:SF-2025-SACFL:start --><!-- existing:SF-2025-SACFL:start -->Distributed Training 已把 federated payload 定义为 typed protocol，并分开 freshness、objective 与 commit；Training Operator 已要求失败恢复保持 artifact 一致。<!-- existing:SF-2025-SACFL:end --><!-- delta:SF-2025-SACFL:start -->在 federated continual learning 中联合管理 client data drift、历史知识 retention、资源预算与异常 task admission，说明一轮上传不能只携带无类型 model delta。<!-- delta:SF-2025-SACFL:end -->

实验覆盖作者选择的数据集、3-20 个任务与模拟/演示环境；论文未证明长期真实 client churn、secure aggregation 或不同硬件资源下的收敛与防御。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-SACFL:end -->

### [Distributed Retrieval-Augmented Generation](https://arxiv.org/html/2505.00443v1)

原家族 `SF-2025-DISTRIBUTED-RAG`，精确版本 `arXiv:2505.00443v1`，原审阅身份 `RP-af959f00565708d7`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00443v1 — exact-v1 §3 distributed RAG model and topic-aware random walk；评价：https://arxiv.org/html/2505.00443v1 — exact-v1 §4 experiments and sensitivity；反证/限制：https://arxiv.org/html/2505.00443v1 — exact-v1 § Discussion/Limitations boundary — exact-v1 discussion and threat boundary；实现：Not Disclosed — exact simulation/repository revision is not frozen。

<!-- review:SF-2025-DISTRIBUTED-RAG:start --><!-- claim:SF-2025-DISTRIBUTED-RAG:start -->分布式 RAG 将 corpus ownership 留在 peer，并以 topic-aware discovery 代替中央索引；它减少集中收集，却不会自动提供 query privacy、信任或一致性。<!-- claim:SF-2025-DISTRIBUTED-RAG:end -->作者在仿真网络比较 topic-aware random walk 与 flooding/centralized baselines，并报告接近中央检索、消息更少。证据不覆盖对抗 peer、真实网络故障、隐私证明或生产尾延迟；稳定可审计 corpus 仍适合中央 RAG。<!-- review:SF-2025-DISTRIBUTED-RAG:end -->

<!-- books-review:SF-2025-DISTRIBUTED-RAG:start --><!-- existing:SF-2025-DISTRIBUTED-RAG:start -->RAG 主要以中央索引为默认，已讨论 partition 和 federation，但缺少 peer-owned knowledge 的完整控制边界。<!-- existing:SF-2025-DISTRIBUTED-RAG:end --><!-- delta:SF-2025-DISTRIBUTED-RAG:start -->补充 peer-owned indexes 与 topic-aware random walk：恢复数据所有权，同时引入 query leakage、peer availability/trust、routing 与 index consistency。<!-- delta:SF-2025-DISTRIBUTED-RAG:end -->

已重新打开 exact-v1、目标与相邻章节；上述 delta 已由当前正文的语义绑定段落承载，owner、trade-off、failure 与 fallback 连续，故不重复插入。Resolution: `verified_existing_writeback`；当前决定：`No Change — Existing Coverage`。<!-- books-review:SF-2025-DISTRIBUTED-RAG:end -->

### [Memory-Centric Computing: Solving Computing's Memory Problem](https://arxiv.org/html/2505.00458v1)

原家族 `SF-2025-MEMORY-CENTRIC-COMPUTING`，精确版本 `arXiv:2505.00458v1`，原审阅身份 `RP-8b0c22ed964d7ae2`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00458v1#S2；评价：https://arxiv.org/html/2505.00458v1#S3；反证/限制：https://arxiv.org/html/2505.00458v1#S4；实现：Not Required — Standard Review。

<!-- review:SF-2025-MEMORY-CENTRIC-COMPUTING:start --><!-- claim:SF-2025-MEMORY-CENTRIC-COMPUTING:start -->把 AI 系统瓶颈从算力单点扩展到 memory movement、capacity hierarchy 与 near-data execution；它是既有异构内存设计线的系统性证据。<!-- claim:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

论文是机制综述与系统立场，不提供一个可直接泛化到所有 LLM workload 的单一实现或 benchmark 结论。<!-- review:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

<!-- books-review:SF-2025-MEMORY-CENTRIC-COMPUTING:start --><!-- existing:SF-2025-MEMORY-CENTRIC-COMPUTING:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-MEMORY-CENTRIC-COMPUTING:end --><!-- delta:SF-2025-MEMORY-CENTRIC-COMPUTING:start -->把 AI 系统瓶颈从算力单点扩展到 memory movement、capacity hierarchy 与 near-data execution；它是既有异构内存设计线的系统性证据。<!-- delta:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

论文是机制综述与系统立场，不提供一个可直接泛化到所有 LLM workload 的单一实现或 benchmark 结论。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-MEMORY-CENTRIC-COMPUTING:end -->

### [A General Framework for Property-Driven Machine Learning](https://arxiv.org/html/2505.00466v1)

原家族 `SF-2025-PROPERTY-DRIVEN-ML`，精确版本 `arXiv:2505.00466v1`，原审阅身份 `RP-4a84d251861e95da`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00466v1#S3；评价：https://arxiv.org/html/2505.00466v1#S4；反证/限制：https://arxiv.org/html/2505.00466v1#S5；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-PROPERTY-DRIVEN-ML:start --><!-- claim:SF-2025-PROPERTY-DRIVEN-ML:start -->把 ML acceptance 从平均 task score 扩展为显式 property specification、test generation 与 deployment gate，使需求、数据、模型与 verifier 可追踪。<!-- claim:SF-2025-PROPERTY-DRIVEN-ML:end -->

MNIST 与 drone 案例只验证框架可行性；不能证明 property set 完备，learned checker 也不能独占发布 authority。<!-- review:SF-2025-PROPERTY-DRIVEN-ML:end -->

<!-- books-review:SF-2025-PROPERTY-DRIVEN-ML:start --><!-- existing:SF-2025-PROPERTY-DRIVEN-ML:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-PROPERTY-DRIVEN-ML:end --><!-- delta:SF-2025-PROPERTY-DRIVEN-ML:start -->把 ML acceptance 从平均 task score 扩展为显式 property specification、test generation 与 deployment gate，使需求、数据、模型与 verifier 可追踪。<!-- delta:SF-2025-PROPERTY-DRIVEN-ML:end -->

MNIST 与 drone 案例只验证框架可行性；不能证明 property set 完备，learned checker 也不能独占发布 authority。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-PROPERTY-DRIVEN-ML:end -->

### [HalluMix: A Task-Agnostic, Multi-Domain Benchmark for Real-World Hallucination Detection](https://arxiv.org/html/2505.00506v1)

原家族 `SF-2025-HALLUMIX`，精确版本 `arXiv:2505.00506v1`，原审阅身份 `RP-18e6c620b163bad2`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00506v1 — exact-v1 §2 benchmark；§3 methodology；评价：https://arxiv.org/html/2505.00506v1 — exact-v1 §4 results；反证/限制：https://arxiv.org/html/2505.00506v1 — exact-v1 §5 discussion, sub-source overfitting and length；实现：Not Disclosed — exact benchmark release revision not frozen。

<!-- review:SF-2025-HALLUMIX:start --><!-- claim:SF-2025-HALLUMIX:start -->hallucination detector 的分数只属于给定任务、来源、长度和 evaluator；跨来源平均值不能替代 slice 与 calibration。<!-- claim:SF-2025-HALLUMIX:end -->作者构建 task-agnostic multi-domain benchmark，比较检测器并揭示来源过拟合与长度效应。最佳指标属于其数据划分和标签协议，不证明开放世界事实核验、生产置信度或单条 claim 正确性。<!-- review:SF-2025-HALLUMIX:end -->

<!-- books-review:SF-2025-HALLUMIX:start --><!-- existing:SF-2025-HALLUMIX:start -->Evaluation 已把 hallucination 拆为 claim/evidence、slice、length、evaluator 与 calibration contract。<!-- existing:SF-2025-HALLUMIX:end --><!-- delta:SF-2025-HALLUMIX:start -->HalluMix 是跨 NLI/summary/QA 的 benchmark 实例，强调 sub-source overfitting 与长度效应。<!-- delta:SF-2025-HALLUMIX:end -->演进关系 `Principle Reuse`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-HALLUMIX:end -->

### [FreqKV: Key-Value Compression in Frequency Domain for Context Window Extension](https://arxiv.org/html/2505.00570v1)

原家族 `SF-2025-FREQKV`，精确版本 `arXiv:2505.00570v1`，原审阅身份 `RP-a6d41e065303d3ac`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00570v1 — exact-v1 §4 method；评价：https://arxiv.org/html/2505.00570v1 — exact-v1 §5 experiments；§6 latency analysis；反证/限制：https://arxiv.org/html/2505.00570v1 — exact-v1 analysis and Appendix D overhead；实现：Not Disclosed — exact implementation revision not frozen。

<!-- review:SF-2025-FREQKV:start --><!-- claim:SF-2025-FREQKV:start -->频域 KV 压缩用有损 summary 延伸窗口；频率分配、RoPE/position identity 与关键 token 丢失决定它何时必须回退 FullKV。<!-- claim:SF-2025-FREQKV:end -->作者在 LLaMA2/3、8K 训练与最长 256K 评测下比较长上下文任务和 latency。证据不覆盖 continuous batching、并发尾延迟或关键事实不可丢失的 workload，不能把平均质量外推为通用无损缓存。<!-- review:SF-2025-FREQKV:end -->

<!-- books-review:SF-2025-FREQKV:start --><!-- existing:SF-2025-FREQKV:start -->KV/Long Context 已覆盖 feature/frequency compression、position identity、lossy error 与 FullKV fallback。<!-- existing:SF-2025-FREQKV:end --><!-- delta:SF-2025-FREQKV:start -->FreqKV 的迭代频域压缩是已有 branch 的具体 estimator，不新增运行时 owner。<!-- delta:SF-2025-FREQKV:end -->演进关系 `Alternative Branch`；当前决定 `No Change — Existing Coverage`。<!-- books-review:SF-2025-FREQKV:end -->

### [The Illusion of Role Separation: Hidden Shortcuts in LLM Role Learning (and How to Fix Them)](https://arxiv.org/html/2505.00626v1)

原家族 `SF-2025-ROLE-SEPARATION-SHORTCUTS`，精确版本 `arXiv:2505.00626v1`，原审阅身份 `RP-4333acfbfbe89fe2`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00626v1#S3；评价：https://arxiv.org/html/2505.00626v1#S5；反证/限制：https://arxiv.org/html/2505.00626v1#S6；实现：Not Disclosed — exact-v1 does not identify a frozen implementation artifact。

<!-- review:SF-2025-ROLE-SEPARATION-SHORTCUTS:start --><!-- claim:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->证明模型可能用 position ID 等旁路信号学习 role shortcut；instruction hierarchy 必须携带 authenticated provenance，不能把 token placement 当 authority。<!-- claim:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

shortcut 分析与缓解绑定论文模型、模板和攻击；没有证明重排 position ID 能覆盖所有 provenance confusion。<!-- review:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

<!-- books-review:SF-2025-ROLE-SEPARATION-SHORTCUTS:start --><!-- existing:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->现有 owner 已覆盖该机制所需的 state、evidence 与 authority 边界。<!-- existing:SF-2025-ROLE-SEPARATION-SHORTCUTS:end --><!-- delta:SF-2025-ROLE-SEPARATION-SHORTCUTS:start -->证明模型可能用 position ID 等旁路信号学习 role shortcut；instruction hierarchy 必须携带 authenticated provenance，不能把 token placement 当 authority。<!-- delta:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

shortcut 分析与缓解绑定论文模型、模板和攻击；没有证明重排 position ID 能覆盖所有 provenance confusion。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-ROLE-SEPARATION-SHORTCUTS:end -->

### [Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics](https://arxiv.org/html/2505.00675v1)

原家族 `SF-2025-AGENT-MEMORY-OPERATIONS`，精确版本 `arXiv:2505.00675v1`，原审阅身份 `RP-769b04b2dcf2d39a`。仅复用有效结果，不无差别重读旧全文。方法位置：https://arxiv.org/html/2505.00675v1#S2; #S3；评价：Not Disclosed — survey provides no unified controlled evaluation；反证/限制：https://arxiv.org/html/2505.00675v1#S6；实现：https://github.com/Elvin-Yiming-Du/Survey_Memory_in_AI — survey catalog; not an implementation artifact。

<!-- review:SF-2025-AGENT-MEMORY-OPERATIONS:start --><!-- claim:SF-2025-AGENT-MEMORY-OPERATIONS:start -->把 agent memory 从 storage taxonomy 重构为 parametric/contextual representation 与 consolidation、updating、indexing、forgetting、retrieval、condensation 六类显式操作，使 lifecycle 风险能落到具体 transition。<!-- claim:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

这是 survey/taxonomy，不是对六个操作统一实现或 benchmark 的 primary validation；所列 tools 与未来方向不能升级为跨系统性能结论。<!-- review:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

<!-- books-review:SF-2025-AGENT-MEMORY-OPERATIONS:start --><!-- existing:SF-2025-AGENT-MEMORY-OPERATIONS:start -->Memory 章已按 write/read/consolidation/forgetting、admission、visibility、recovery 与显式 state operation 展开，比该 taxonomy 更细。<!-- existing:SF-2025-AGENT-MEMORY-OPERATIONS:end --><!-- delta:SF-2025-AGENT-MEMORY-OPERATIONS:start -->把 agent memory 从 storage taxonomy 重构为 parametric/contextual representation 与 consolidation、updating、indexing、forgetting、retrieval、condensation 六类显式操作，使 lifecycle 风险能落到具体 transition。<!-- delta:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

这是 survey/taxonomy，不是对六个操作统一实现或 benchmark 的 primary validation；所列 tools 与未来方向不能升级为跨系统性能结论。 对照目标及相邻章节后，增量未越过长期机制门槛，决定为 `No Change — Existing Coverage`。<!-- books-review:SF-2025-AGENT-MEMORY-OPERATIONS:end -->

## 5. 缺口与下一步

**唯一当前停点：冻结旧值的V3校验兼容。** [root第三批](../_sources/daily-20250502/review-supplement-20261007.md#第三批本轮内容闭合冻结日期校验仍未通过)已通过LIFT隔离、AMIE受限标准/具体已有覆盖及Google有限恢复；这些窄核待办已结束，不再重抓110/18、读论文或产生Books差额。当前V3仍exit1、仅26条旧日期范围错误；需要在不改旧窗口/日期/评分、checker或共享规则的前提下确认本轮新增部分如何校验，再由root决定整日验收。不得静默跳过旧行、扩窗迁日或把报错记为通过。作者保持ownership与进行中，不计本日验收。

**日期外部保留：** [校准74P与原110轨迹](../_sources/daily-20250502/admission-calibration.md)只有公告year-month、v1 submitted/当前摘要或定点v1 core，不能定位May1北京时间首次公开。一次性请求对应ID历史官方首次公开列表/公告或作者具名首发，不要整类月份清单，不由常规时间表/后修订推算或搬日。当前不正面采用、不进Books、不计确定候选、不支持无遗漏，材料到达只重开对应事件。五新关闭已获root通过；LIFT另须上述中心机制证据，不由日期恢复自动授训练有效性。

**LIFT中心争议保留：** [2504.21187v1](https://arxiv.org/html/2504.21187v1) IV-B/C的MSE+CE/backprop声称与离散pred→compiler→ProGraML→冻结GNN梯度断点同时保留。#77仍属P，明确不采用“GNN监督已直接更新LLM”，不正面采用结构监督训练有效性、不进Books；未确认日期与中心机制争议是两个独立门槛。只有可接受surrogate/gradient estimator/implementation，或不依赖直接回传声称的独立证据到达，才重开具名机制；仅恢复日期不能解除争议，不改C/降分或以HLS数字绕过。

**来源外部保留：** DeepMind/pubs、DeepSeek、Hunyuan、ZAI、ERNIE、MiMo等历史必要条目未恢复；一次性请求May1官方Research/技术发布目录快照或具名原文，当前失败/现代列表不支持历史Coverage。只重开受影响源/日，不反复扩扫历年；Hunyuan动态浏览器失败与正确API当前仅2026明确分开。Qwen/Kimi/Seed/MiniMax的有界日期切片不扩为全渠道保证。

**窗外线索（不阻塞本窗）：** [CaGR-RAG](https://arxiv.org/abs/2505.01164)从cs.DC月表#7定点题摘恢复，cluster grouping/opportunistic prefetch有检索系统潜力；官方v1提交2025-05-02，提交不是公开日期，当前无May1作者首发依据，不计本窗候选，不迁移原候选。月表其他标题不转候选/审阅队列。

上述日期/来源/中心争议均为已独核隔离保留项，不是当前普通未读或必要外部材料待办，不替代唯一校验兼容停点。只处理本日；共享Books、State、合同、index不写，无stage/commit/push。

## 6. 复核

复核者：root（非作者；作者为Boole）。

结论：未通过（本轮内容差额通过；冻结旧值校验兼容未通过，整日暂不验收）。

root首读110题摘及机构core、第二批18 exact-v1 core/AMIE论文准入校准均复用，74P/36C非formal。第三批执行锚点2026-10-07T21:17:10+08:00，已实际核Blog第113～195行、Ch81相关正文及Ch80/82、Pubs两份200请求和有限停止、26行/52块机械冻结与V3错误类型，LIFT隔离、AMIE受限标准/具体已有覆盖、Pubs有限恢复均通过。实际裁决见[独立第三批原件](../_sources/daily-20250502/review-supplement-20261007.md#第三批本轮内容闭合冻结日期校验仍未通过)，作者不修改。唯一剩余为校验兼容判断，不是未完成论文审阅或必要外部论文缺失；整日暂不签、不计验收，报告保持进行中。模型继承未调整。

机器校验：本轮实际重跑V3，退出1，仅剩原26候选的日期兼容报错，无其他错误。校验器要求公开日期整天完全落入窗口，但用户冻结的旧归属为2025-05-02，原窗口在当日09:00结束；不为过校验扩窗或迁日。此兼容性问题交root处理，不修改共享校验器。实际比对原26日期/三维评分/owner/审阅值无差额，52个原review/Books正文块逐字保留，完整原档案SHA256保持；本轮四份维护文档91处本地引用/54个目标均存在。限定`git diff --check`通过，本日cached差额为空。以上不代表独立准入或语义验收。
