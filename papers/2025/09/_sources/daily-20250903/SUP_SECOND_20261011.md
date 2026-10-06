# 2025-09-03 第二批29精确v1准入校准交接

## 1. 实际范围

作者已完整读以下29份精确v1官方title/abstract/comments/版本栏，原件与请求在[supplement-20261011](supplement-20261011/)，名为abs-2509.<ID>v1.raw；结构化原题摘在[SUP_EXACT_20261011.json](supplement-20261011/SUP_EXACT_20261011.json)。不采用API最新题摘/最新版改名。此批暂22P/7U，U是决定准入的普通工作，不是外部终态；所有P公开自然日未证，不评分、不给Evidence/Books。只读具体相关标题，不把all216或窄237变全量AB队列。

## 2. 22项具名P

| v1身份与完整题名 | 具体增量：旧判断→原文增量→待核选择 | 必要限制/身份门 |
| --- | --- | --- |
| [2509.00189](https://arxiv.org/abs/2509.00189v1) HiVA: Self-organized Hierarchical Variable Agent via Goal-driven Semantic-Topological Evolution | 固定流程或不沉淀reactive loop→bandit路由、环境诊断textual gradient联动语义/拓扑→工作流可迁移结构与探索预算取舍 | 不采5–10%为已证归因；textual gradient不是真实反向传播，实验可信度后续审阅。 |
| [2509.00195](https://arxiv.org/abs/2509.00195v1) Democratizing Agentic AI with Fast Test-Time Scaling on the Edge | edge TTC受generation/verification争memory与路径straggler限制→speculative beam、非对称多模型memory、prefix-aware调度→质量与goodput的联合资源选择 | 24GB单卡不等同cloud质量/预算，2.2×及38–68%未授采用。 |
| [2509.00210](https://arxiv.org/abs/2509.00210v1) Beyond Pixels: Introducing Geometric-Semantic World Priors for Video-based Embodied Models via Spatio-temporal Alignment | 静态VLM不能直接提供动态导航经验→几何/语义/时空对齐与任务激活隐式地图→空间经验检索/长期探索边界 | 不是仅因world model题名准入；不把经验embedding当已证action-conditioned dynamics，1–3%不是主因。 |
| [2509.00245](https://arxiv.org/abs/2509.00245v1) The Rarity Blind Spot: A Framework for Evaluating Statistical Reasoning in LLMs | 检索/摘要能力不能代表跨文档稀有性判断→可控文档数/稀有阈值任务出现频繁特征误当distinctive→需要区分检索与统计reasoning | 10–40文档局部反侧，不授所有模型普遍失效或真实决策结论。 |
| [2509.00276](https://arxiv.org/abs/2509.00276v1) Exploring Reasoning-Infused Text Embedding with Large Language Models for Zero-Shot Dense Retrieval | encoder/context embedding不足reasoning retrieval→先生成中间reasoning再形成embedding→表示质量与额外生成成本的选择 | CIKM2025具名先稿门；不采BRIGHT指标为端到端RAG收益。 |
| [2509.00303](https://arxiv.org/abs/2509.00303v1) Access Paths for Efficient Ordering with Large Language Models | 单排序实现并非普遍最优→agreement batch policy、pairwise majority及LLM external merge→按query/data选择质量/成本 | log-linear是作者实验观察，不是普适cost law；不因传统sort组成关闭具体条件比较。 |
| [2509.00309](https://arxiv.org/abs/2509.00309v1) Balanced Actor Initialization: Stable RLHF Training of Distillation-Based Reasoning Models | distillation模型直接RLHF出现length collapse/reward下跌→两阶段指令/推理/预训练权重合并→初始化比率与稳定性/推理保留边界 | 两负结果本身明确P；不将成熟model merge当已证普遍修复，ratio/同预算未核。 |
| [2509.00320](https://arxiv.org/abs/2509.00320v1) Towards Adaptive Visual Token Pruning for Large Multimodal Models | 单重要性选择保留冗余→跨模态MI选择再按pairwise距离保多样性、仅剪visual→alignment/diversity资源取舍 | 不采用最新TrimTokenator题名；88.9%与56.7%不等所有质量目标无损。 |
| [2509.00328](https://arxiv.org/abs/2509.00328v1) Mechanistic interpretability for steering vision-language-action models | VLA隐藏action映射难干预→FFN投token basis找speed/direction语义并steer→推理时动作控制的可解释性边界 | CoRL2025具名先稿门；模拟LIBERO/UR5局部，不授causal方向普适或机器人安全。 |
| [2509.00366](https://arxiv.org/abs/2509.00366v1) KG-RAG: Enhancing GUI Agent Decision-Making via Knowledge Graph-Driven Retrieval-Augmented Generation | UTG抽取/调用不足→结构向量检索与intent导航路径、成本ablation约4h饱和→图获取成本与Agent决策取舍 | EMNLP2025先稿门；不以75.8%排名准入，4h范围需后续核具体app配置。 |
| [2509.00373](https://arxiv.org/abs/2509.00373v1) Activation Steering Meets Preference Optimization: Defense Against Jailbreaks in Vision Language Models | steering安全方向可能损visual grounding→layer-specific steering结合toxicity/visual consistency偏好目标→安全/语义保真联合取舍 | 安全必独核；不能由AB“maintaining”授所有攻击防御/无损，artifact未核。 |
| [2509.00375](https://arxiv.org/abs/2509.00375v1) Open Data Synthesis For Deep Research | flat/multihop合成可捷径/泄漏→递归Research Tree、blur中间节点、留retrieval/trajectory标签→层次约束数据的可验证性 | 不是50K量准入；层次必须遍历/无shortcut为待核命题，3B超32B不授公平预算。 |
| [2509.00391](https://arxiv.org/abs/2509.00391v1) The Resurgence of GCG Adversarial Attacks on Large Language Models | prefix成功不等语义jailbreak→prefix/GPT4o judge分歧、coding更脆弱、annealing优势在语义judge减弱→攻击评价协议选择 | 安全/反侧必独核；跨0.5B/1B/20B不同家族不能以size解释loss landscape因果，GPT4o不是truth oracle。 |
| [2509.00419](https://arxiv.org/abs/2509.00419v1) LightVLM: Acceleraing Large Multimodal Models with Pyramid Token Merging and KV Cache Compression | prefill与long-output decode瓶颈不同→分层visual merge与KV压缩两阶段→质量/长度条件下资源选择 | EMNLP2025 Findings先稿门；“100% performance”不等所有任务无损，26B更快8B条件未核。 |
| [2509.00425](https://arxiv.org/abs/2509.00425v1) The Gold Medals in an Empty Room: Diagnosing Metalinguistic Reasoning in LLMs with Camlang | 已知语言高分不足陌生语法学习→grammar/dictionary造未见组合、词法/语法分解及人类对照→pattern matching评价盲区 | Working in progress，不因认知领域关闭；98/47/87依赖具体任务/evaluator，不证明人类推理全优。 |
| [2509.00461](https://arxiv.org/abs/2509.00461v1) TECP: Token-Entropy Conformal Prediction for LLMs | blackbox不能取logits→sampled token entropy+split CP集合→无参考UQ与coverage假设 | formal guarantee仍需exchangeability/候选集合/entropy定义条件，不采开放生成普遍保证。 |
| [2509.00484](https://arxiv.org/abs/2509.00484v1) VideoRewardBench: Comprehensive Evaluation of Multimodal Reward Models for Video Understanding | video RM榜单不足frame/scale影响→RL不必提升跨模态泛化、不同RM对frame/TTC响应不同→reward评价协议取舍 | 安全维度/设计反侧必独核；1563样本量不是贡献主因，RL因果/57%不外推。 |
| [2509.00496](https://arxiv.org/abs/2509.00496v1) ResearchQA: Evaluating Scholarly Question Answering at Scale Across 75 Fields with Survey-Mined Questions and Rubrics | 专家评估难扩展/总分掩盖引用和限制缺失→survey rubric与人类校准揭示高分系统citation/limitations缺口→分维度覆盖与judge可信度 | 是LLM研究问答评价，不是科学发现应用；74%judge agreement不是可靠性保证，75field不能以31专家8field全部验证。 |
| [2509.00520](https://arxiv.org/abs/2509.00520v1) ERank: Fusing Supervised Fine-Tuning and Reinforcement Learning for Effective and Efficient Text Reranking | binary pointwise区分弱/listwise慢→integer score SFT与listwise-derived reward进入pointwise→局部运行/全局ranking目标分离 | 不因SFT+RL成熟关闭具体目标；BRIGHT nDCG不授端到端低latency保证。 |
| [2509.00576](https://arxiv.org/abs/2509.00576v1) Galaxea Open-World Dataset and G0 Dual-System VLA Model | 跨embodiment预训不必够→三阶段中single-embodiment与同机器人数据关键→迁移/一致性训练选择 | 不是dual-system组合本身准入；数据/训练阶段混杂后续核，不授所有embodiment泛化。 |
| [2509.00591](https://arxiv.org/abs/2509.00591v1) StealthEval: A Probe-Rewrite-Evaluate Workflow for Reliable Benchmarks | 感知test/deploy context可能改变安全表现→probe驱动rewrite后honesty/refusal改变→evaluation awareness协议盲区 | 安全反侧必独核；rewriting语义/任务保真混杂未控不能采“直接影响”因果或deploy更安全普遍结论，只精确v1。 |
| [2509.00599](https://arxiv.org/abs/2509.00599v1) COMET: A Framework for Modeling Compound Operation Dataflows with Explicit Collectives | 单op模型忽略跨cluster collectives→GEMM/nonGEMM依赖与latency/energy显式模型→compound mapping搜索选择 | 与unfused比较不是融合/collective因果归因；非实际生产硬件benchmark已复现。 |

## 3. 7项决定准入普通U与精确问题

| v1身份与完整题名 | 尚缺的决定事实，只定点读已有core |
| --- | --- |
| [2509.00190](https://arxiv.org/abs/2509.00190v1) Explainable Chain-of-Thought Reasoning: An Empirical Analysis on State-Aware Reasoning Dynamics | AB只给spectral embedding/cluster/Markov描述；查必要方法/结果是否有可改变reasoning解释的新边界，而非成熟可视化组合。 |
| [2509.00244](https://arxiv.org/abs/2509.00244v1) Universal Deep Research: Bring Your Own Model and Strategy | 可编辑任意strategy/UI不单独准入；查是否具体新执行/约束/失败路径，而非configurable prompt/tool wrapper。 |
| [2509.00251](https://arxiv.org/abs/2509.00251v1) Instruction-Level Weight Shaping: A Framework for Self-Improving AI Agents | typed delta/版本/ratings/rollback/threshold distill是具名流程；查其边界或失效控制相对成熟memory/reflection组合有何可核增量；不采throughput/幻觉宣传或pseudo-parameter数学类比作证据。 |
| [2509.00325](https://arxiv.org/abs/2509.00325v1) GIER: Gap-Driven Self-Refinement for Large Language Models | concept gap critique是否仅成熟self-refine rubric组合，还是揭示accuracy不变时rationale/grounding分离的具体反例/条件；查必要method与对照。 |
| [2509.00326](https://arxiv.org/abs/2509.00326v1) Chunked TabPFN: Exact Training-Free In-Context Learning for Long-Context Tabular Data | tiled attention可能仅既有实现；查TabPFN masking/跨维attention下exact分块的具体成立条件与compression替代边界。不是因tabular领域关闭。 |
| [2509.00454](https://arxiv.org/abs/2509.00454v1) Universal Properties of Activation Sparsity in Modern Large Language Models | AB提出ReLU exactzero不能迁移与robustness框架，但未说具体pattern；查非zero sparsity度量/干预发现，不能采“universal”宣传也不能因AB少实验细节直接C。 |
| [2509.00531](https://arxiv.org/abs/2509.00531v1) MobiAgent: A Systematic Framework for Customizable Mobile Agents | AB仅列MobiMind/AgentRR/data pipeline与SOTA；查AgentRR或数据机制的执行/资源边界，不按GUI领域自动P/C。 |

上述普通7U作者继续处理；root可先独核22P所有安全/反侧与代表边界，不需等待整包。公开日期仍仅核自然日，原51旧时刻请求不传播本轮。

## 4. 7U决定核心已实际读取并关闭U

本段覆盖前述7U过程状态；第二批最终暂27P/2C，普通U0，仍待root非作者校准。各原core为supplement-20261011/core-2509.<ID>v1.raw及request.json，只读下列决定段，不声称全文、公式全面核验或正式Evidence。

| 身份 | 暂判 | 实际读取位置与决定依据/限制 |
| --- | --- | --- |
| 00190 | C | 完整§3/§4/§6：step embedding累计Gram、top eigenvalue+k-means、手工语义角色与一阶Markov/t-SNE；结果为cluster语义/位置对应的描述性结构分析，未提出对具体reasoning正确性/干预有效性或设计选择的新的条件证据。不能将图中cluster分离当模型因果reasoning机制；关闭不是因小模型或缺公开日。 |
| 00244 | P | 完整§2/§4：用户strategy一次转成带逐步comment的generator、控制在CPU代码/变量、LM仅局部utility；原型whole-pass相对prompt orchestration/逐步代码fragment的跳步/错序失败比较，是具体执行选择。sandbox是部署必要条件而非prompt injection已消除；语义logic不验证、无中途交互、8k与效率宣称未授采用。 |
| 00251 | C，安全关闭必独核 | 完整§4.2–4.4/§4.6–4.7/§6/§8：typed reflection edit、ratings gate、版本rollback及offline distill基本由成熟控制/微调机制组合；§6为作者单operator工单observational study、RAG被弃与proxy first-shot success，无可归因的新机制或特定训练/执行边界。§4.2 networkless/seccomp叙述与§4.6推荐、§4.7 deny-list参考实现不一致；不采用安全隔离已实现或ratings单次t-test已控制长期family-wise error。2.4/7.2/5×与20→90%first-shot不当80%hallucination实证。保留全部安全信号交root，若具名边界足以P则改，不因Evidence费时关闭。 |
| 00325 | P，局部反侧 | 完整§2/§6/§7：mature gap rubric self-refine本身不作准入；PrivacyQA recall增加伴precision下降/不可回答误当可回答21→33，accuracy70→63，与AB不降accuracy宽述不完全一致；e-SNLI部分incorrect label仍有gold-aligned reasoning。具体rationale质量、召回、answerability分离改变评价选择；不因SciFact使用科学摘要就当科学发现应用，也不授因果提升/统计结论已复核。 |
| 00326 | P，条件限定 | 完整§2/§3.2：running max/sum/weighted-V是成熟exact online softmax，不称新算法；TabPFN三个attention维度、无compression扩context后的约半任务收益/半数平饱和和classification/regression尺度差异，是foundation in-context容量与算力取舍局部证据。FLOPs明示未变，不采用正文“去掉quadratic computation”或fit-time当所有predict更快；TabArena表predict time 4.45 vs0.32保留。 |
| 00454 | P，反侧 | 完整§2/§3/§4：top-p L1 mask、99%critical sparsity，input/gate/intermediate对可加速矩阵不同；gate不必比input更稀疏、跨任务/recipe波动与diffusion比较，改变sparsity指标/校准选择。不是“universal”题名准入；未测reasoning、未实测全部端到端speed，不把model size当单一决定或宣称data-free普遍必优。 |
| 00531 | P，执行安全边界 | 完整§4.2–4.6/§6.2：按ActTree层位训练prefix-length embedding/reranker、UI bbox/content replay前失效检查、shortcut speculation与负载分布依赖reuse率，具体cache对象/验证成本联动。原文称false positives不导致final error仅依赖事后UI差异/常见back操作；不可逆side effect/视觉等价错误不能靠back保证，安全反侧必独核。不采用99%为生产保证或2–3×跨负载结论。 |

## 5. late-ID入口字段定点核查

窄hardware实际8entry里2509.25196、2510.15882、2509.25197不是由ID推测落窗。已独立下载三份官方精确v1 abs及request：版本栏分别Aug29 19:48:09Z、Aug30 01:28:47Z、Aug31 02:44:04Z，与API published字段同值；这是submitted history，并非首公开。当前原页没有解释ID月份/流水号为何晚，不能猜moderation原因或由API字段授Sep02。此次只核身份/版本栏，未因late-ID扩大到其全文；后续若题摘判P仍需独立公开自然日/先稿事件门。

## 6. 第二批独核通过

root实际完整读29精确v1题摘及全部7决定core，27P/2C通过，见[独核§5](SUP_INDEPENDENT_20261011.md)。累计首43=39P/4C；00531不可逆effect/视觉同相、00325正文accuracy反侧、00326 FLOPs/预测时间及00454shape/task漂移保留。无未决准入U，但公开日/先稿门、其他来源/题摘及DAY仍是本轮后续；不授日级或正式Evidence。

## 7. 追加00366必要限定

作者另实际完整读精确v1 §3.1 UTG提取、§3.3在线retrieval、§5.6 Tables9–11及Limitations；原件core-2509.00366v1.raw。所谓4h饱和仅Weibo的SR70/DA80在4h→8h保持，steps仍4.50→3.75改善，不是所有应用/全部成本饱和；English初采1h/Chinese30apps8h不授免费UTG。Limitations仍把web/PC写为future而§5.6已有测试，保留精确版本张力，不照录泛化。原P及日期隔离不改，不要求root重读全篇。
