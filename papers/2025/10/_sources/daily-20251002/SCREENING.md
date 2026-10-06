# 2025-10-02 有限筛选与安全保留

仅本日恢复；未读取旧 Weekly 或其他日报候选池。

## 实际查询与停止

- 十四每日源的首查及 Google pubs、MiniMax Agent 独立入口原响应见各 `*.raw` 与 `*.receipt.json`，不是已读正文的证明。逐个入口只检查可见目录的历史边界，不逐篇处理全年库存。
- arXiv 第一查询的服务端回显错误：上界被解析成 `2510020100`，total=72374。`arxiv-query.raw` 是故障原件，不能支持窗口覆盖。没有逐篇关闭它。
- 第二查询完整 URL 见 `arxiv-narrow.receipt.json`：submittedDate 202510010000～202510012359，title 同义词 language/LLM/transformer/agent/diffusion/reasoning/multimodal/training/inference/GPU/kernel/world/VLA/retrieval/memory/expert；start=0/max_results=200，返回200/261。它仍是提交时间发现，不是当窗公开事件队列。浏览这200标题后，只恢复85个具体模型/系统方向精确v1题摘；不继续把余61及全年目录变成待全文队列，也不称查询完整召回。
- 官方分类标题有限补检：cs.CL 月页 skip=0/show=100 前100；cs.DC/CV/PL/IR 月页 skip=0/show=25 web 失败。仅标题发现，不授 first-public 证明。cs.LG/AI/AR/RO/OS/PF/MA 尚缺同等官方本窗公告恢复，覆盖限制保留；主题发现已覆盖训练、推理、模型、跨模态、VLA和记忆/检索，但不称全分类公告恢复。
- arXiv announced_date 高级检索尝试 `2025-10-01`～`2025-10-02`、language model、size50、start0，web cache miss。官方公开调度帮助只能说明一般时间表，不能证明某篇的实际公告；没有用 submitted 或 DataCite 注册时间代替公开时间。
- Seed：原无语言头type1仅元数据已由自己的部署JS与x-tt-locale:US请求修正；2025 asc count20、token0/20/40/60/80实际85身份，末页has_more:false，9/22→10/9跨窗，无可见本窗项；不把年度目录转题摘队列，total94与85差额不授完整历史保证。blog offsets0/20/40已跨到10/23～12月停止。真实请求见SOURCE_REPAIR.md。
- Hunyuan：Research首查动态壳；IAB新建tab有限尝试30s超时、内核重置；官方部署JS→Research所用blog模块→POST publicList，body pageNum1/pageSize20/renderType0。data.totalNum=9，实际9项，最早显示2026/02；停止第1页，不据此宣告2025/10无事件。
- ERNIE博客page1和实际Next page2/2已读到9/12与10/16边界，无本窗显示条目；MiMo八篇Paper读到9/19与10/21边界，Blog More不是历史分页，未把它当分页完成证明。
- Z.ai首查15项后已核自己的LoadMore JS并真实请求?page=2，累计18项、hasMore:false/没有更多，停止第2页；最早12/07，历史十月仍缺段。Anthropic首查当前列表；Meta可见内容有限；Google pubs独立2025+language首页仅publication year。均不授无事件断言。Google Blog新October路由page1→page2/2新增Segmenter日期潜力，见GOOGLE_RECOVERY.md，不沿用旧?m=失败。
- Qwen旧站首查9/23及之前，当前站定日补线索；DeepSeek已从自己的/news/与部署JS核独立Research31项本地展开数组，10/21与5/14跨窗，动态9/29→12/1跨窗；只读边界，不逐篇全年。Moonshot Blog9/16→11/6边界、GitHub org100单页身份补线索。MiniMax两Blog及独立Agent页（仅2026/05/13）不当历史不存在。
- web定日补检原查询范围：`site:openai.com "October 1, 2025" research`；`site:anthropic.com "Oct 1, 2025" research`；`site:deepmind.google "1 October 2025"`；`site:research.google/pubs/ "2025" "October" language`；`site:ai.meta.com "October 1, 2025"`；`site:qwen.ai "2025" "10" "1"`；`site:seed.bytedance.com "2025-10-01"`；`site:minimax.io "October 1" "2025"`；`site:ernie.baidu.com/blog "2025-10-01"`；`site:hunyuan.tencent.com "2025-10-01"`；`site:z.ai "October 1, 2025"`；`site:minimax.io/blog "2025" "October" model`。每条仅返回首批搜索结果，无额外分页；Qwen/MiniMax用户生成子域噪声不属于官方研究，关闭。搜索未命中不等于无事件。

## 题摘判断

精确v1 Atom的85项完整题摘实际分批读取；[可读提取](exact-v1.text.txt)只是机械转换，正文权威仍为原Atom。
其中4项明确本次排除，其他81项保留贡献潜力但缺公开日期/校准，不评分、不进入正式候选、不称证据完成。

| 排除身份 | 具体理由 |
| --- | --- |
| 2510.00368v1 Transformer Cookbook | 汇编已有算法参数构造；题摘没有具体新构造、反证或设计成立条件。不是因理论/综述标签本身排除。 |
| 2510.00381v1 Semantic-Driven AI Agent Communications | 通信框架结合微调、量化和分层资源优化，题摘没有说明foundation-model学习/推理/工具执行新增机制；网络仿真收益不建立主线差额。 |
| 2510.00482v1 Agent Fine-tuning in Microdomains | JP1认证问答采用轨迹蒸馏、RAG及context-answer extractor；14%任务收益未给组合失效边界或新控制机制，不以microdomain本身排除。 |
| 2510.00529v1 Memory-Augmented Log Analysis | Phi-4-mini+短期摘要+FAISS双memory+Bayesian persistence用于UNSW-NB15；题摘的低准确率/高召回值得任务评价，但未说明对模型/通用memory设计的新增因果边界。仅安全应用不等于LLM安全机制。 |

81潜力的材料身份保持在Atom其余条目，下面是实际增量分组，不以通用原则代替原文：

- KV/上下文：GUI-KV的跨帧key冗余，PAL-UI原截图主动回取，ACON full成功/压缩失败轨迹修订压缩准则，LongCodeZip函数/块两级预算，TokMem可训练procedure embedding。
- 学习/训练：ToV反转target/train样本打分，ZO Fine-tuner可复用扰动策略，AlphaRL rank1早期外推，M2PO二阶importance约束，RiskPO reward风险分布，CAPO曲率mask，PCL难度value预测，CurES prompt分布与rollout预算，ACPO逐步复用+advantage裁剪，ElasWave batch/RNG/communicator重分片，ICCL CPU P2P+backup QP。
- 表示/推理：FFN谱利用率，ARM activation redistribution，CoT vectors，SMDS feature manifolds，latent coprocessor对照反侧，PDR bounded workspace和并行draft，IRT模型能力向量，dueling-feedback路由。
- 多模态/生成/VLA：EPIC token/layer一致性蒸馏，HAMLET moment tokens，HyT thought可选输出，VLA-RFT world simulator reward，CroSTAta历史transition attention，DyVA video diffusion单步encoder，AYT manifold tangents，DAV E/M search-alignment，GPC distribution composition，ADD one-hot扩散，PromptLoop逐步latent反馈，MULTI-TAP多objective predictor。
- Agent/检索/评价：ReSeek JUDGE动作+process reward，ERL erase/regenerate，repository历史memory，MILCO English sparse+LexEcho，ModernVBERT双向attention/late interaction归因，HalluGuard小模型grounded claim判断，TRACE validate-by-reproduce，GEM dense-reward算法对照，In-Place Feedback局部编辑，Toucan真实MCP环境轨迹；PodEval与Video Call测量只保留待核评价盲区，未靠dataset规模准入。
- 反侧/边界：dialect语法扰动、Faroese transfer与LoRA/full差异、静音干扰、选项顺序影响、RAG噪声下reasoning误信、preference典型性与Verbalized Sampling、ManagerBench harm/action区分。
- 安全：DLM priming、ReFlux concept恢复、DIA轨迹免疫、unlearning optimizer对weight tampering、RECAP错误CoT prefill恢复、SIRL entropy内生reward、secret elicitation、SpeechLLM组件backdoor、GGUF单bit威胁条件。见有限core笔记；不是已获生产安全保证。

## 原始官方安全公告

日期更正：定点核01原RSS七exact case身份，pubDate均Wed, 01 Oct 2025 00:00:00 GMT→BJT08:00，窗外，不再放02日期hold。七case与整体PDF/10月7日主发布不混同，见SOURCE_REPAIR.md。
实际读[Phishing and scripting support](https://openai.com/index/disrupting-malicious-uses-of-ai-phishing-and-scripting-support/) Actor/Behavior/Impact及[Korean-language malware support](https://openai.com/index/disrupting-malicious-uses-of-ai-korean-language-malware-support/)同三部分：前者未观察新增攻防能力，主要语言本地化与迭代效率；后者不能确认恶意二进制由模型生成，也不能独立归因国别。它们是厂商观测边界，不是模型不能产生新能力的保证。Stargate合作公告为供应/商业规划，不披露新的训练/推理机制，贡献关闭；影响活动/诈骗案例不以机构声望自动准入。

## 采用边界

日期保留81论文+1 Google Interactive Segmenter（后续GOOGLE_RECOVERY.md）。OpenAI七case改为窗外归属线索。恢复要求为具体官方历史公告或作者首次公开正文的明确时间/完全落窗bounds；只重开对应身份日期→准入校准→评分→必要core/Books对比。
当前无正面采用，Books实际0；不是“81项已有覆盖”，也没有待root强造写入。
