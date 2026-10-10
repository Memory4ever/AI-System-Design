# Daily Research — 2025-05-01

**规范：** V3
**窗口：** 2025-04-30 ～ 2025-05-01
**原精确窗口：** 2025-04-30 09:00:00 ～ 2025-05-01 09:00:00（北京时间，左闭右开）
**窗口说明：** 用户于2026-10-07授权只补遗漏，冻结旧候选及日期。日期范围展示旧精确窗口触及的自然日，旧09:00边界仍保留；不扩张新增材料窗口、不移动原May1候选。
**补充窗口：** 2025-04-30 ～ 2025-04-30
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-07T17:50:18+08:00

## 1. 结论

本轮补查确定新增OpenAI GPT-4o sycophancy初报1个事故家族事件，原22个候选的身份、May1日期、评分和有效审阅保留，合计23个本日家族。新增的受限生产纠错命题已深入审阅，并由非作者局部复核确认Ch66实际已有覆盖，Books不强行追加。

这不是“2025年来源全部已补齐”：14个每日来源已实查，多个历史目录及arXiv日公告仍缺。四主题API的317响应/241当前版本身份只是邻近提交线索，不是当天新增论文或全量初筛完成数；旧375分母及22+353关闭数字是旧流程档案，不是本轮核实的官方日批次。

新增1项的必要证据和具体Books比较通过；本轮来源停止、代表排除、35项日期保留及三项改判写回已获Archimedes最终非作者日级验收，达到含外部隔离项的安全终态。不等于23项重新全审，不授无遗漏或全部Coverage/Evidence正面通过。原完整证据和反证保存在[补查前档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)。

## 2. 来源覆盖

本轮查询、分页、真实错误和读到哪里见[来源补查记录](../_sources/daily-20250501/supplement-20261007.md)。只检查Daily每日组；没有触发Weekly扫描或额外按需release。表中限制不作为零事件证明。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | RSS1251项按目标日前后核，初报实际正文已读；Research请求403 | 受阻 | RSS只覆盖该feed，不能保证未列入研究；初报403原件非正文 |
| SRC-ANTHROPIC | Research/News解码Apr/May分别6/13项；Apr30政策核心已关闭 | 已检查 | 仅这两个目录，不外推Engineering直发 |
| SRC-GOOGLE-AI | Research April归档9标题及Apr30全球健康核心已独核；Google pubs默认入口可读，2025 facet678；DeepMind正确Publications第2/3页各30卡，Apr30邻接May1/Apr29，第3页首Mar24 | 受阻 | Google年份/发表字段非首公开日；DeepMind是精选目录，不授全机构覆盖 |
| SRC-META-AI | Research/历史Blogpage7连接失败；web Research为0行、正确Publications不可取 | 受阻 | 缺2025四月目录，不能记零事件 |
| SRC-QWEN | 旧Blogpage2至Apr29、page3从Mar28，实际核相关标题/日期 | 已检查 | 该Blog段不覆盖全部独立artifact |
| SRC-DEEPSEEK | News16日期标题至2024；本窗邻接Mar25/May28；ProverV2旧家族去重 | 受阻 | 旧全研究目录未恢复；404入口不作为研究成功 |
| SRC-MOONSHOT | Blog26日期标题，Apr7至May6间无Apr30条目 | 已检查 | 有限Blog，不外推仓库直发 |
| SRC-TENCENT-HUNYUAN | 动态页及publicList两renderType的9/6条均2026；web超时、浏览器创建页60.8秒超时重置kernel，未取得UI | 受阻 | 2025历史目录未恢复，不将浏览器失败写作已读“全部”列表 |
| SRC-ZAI | Research2页18独立条目，hasMore=false且最早Dec7/8 | 受阻 | 四月旧目录缺失，不将当前终页当历史无发布 |
| SRC-BYTEDANCE-SEED | 默认Blog41/total49，另US三页40/total45，合并46独立身份，新5项非Apr30；论文US五页85/total94终cursor；实际client强制论文US，CN无数组 | 受阻 | locale之间库存口径未披露；49−46与94−85只是数量差，不能据此确认遗漏身份数；total非全读完，PublishDate非首公告 |
| SRC-BAIDU-ERNIE | Blog两页10+6标题/日期，当前最早Jun30 2025；纠正May9误记 | 受阻 | Apr30历史/仓库直发未恢复 |
| SRC-XIAOMI-MIMO | Paper8条最早May12；官方API恢复Apr30具体commit的README全文，预训练/MTP/后训练/rollout core已读 | 受阻 | README未标首发日，commit时间非仓库公开证明；当前Blog旧日期缺段 |
| SRC-MINIMAX | 当前EN12/CN13标题及结构化元数据；EN web/raw仅每卡Read More，无实际列表分页控制 | 受阻 | 当前切片非四月完整目录，Read More不当分页 |
| SRC-ARXIV | 四主题邻近提交API317响应/241身份与月表标题补检；续跑Advanced首屏50/446完整题摘，6旧候选重复，非作者核44新线索与9处决定性core，校准为35潜在/9关闭；两日粒度0响应不授阴性，CS-probe过滤未证生效 | 受阻 | 35项具体公开日未明，不能称Apr30候选；不把提交日、DataCite、月份或0响应当公告；旧375非日批次。未请求月页不默认成为全文队列 |

## 3. 候选与判断

旧22行采用原日期、分数和处置，只格式迁移并指向当前Stable Node路径；旧证据不因本次日期规则变化而移位。新增初报只属于补充自然日Apr30。跨日与05-03 postmortem汇总时按同一事故家族去重，不能把两次说明当独立研究贡献相加。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Don't Retrieve, Generate: Prompting LLMs for Synthetic Training Data in Dense Retrieval](https://arxiv.org/html/2504.21015v1) | 2025-05-01 | 把 RAG 训练数据来源从只检索公开问答扩展为可控生成的 hypothetical negatives；关键系统边界是生成器版本、去重、污染审计与真实检索回放必须共同冻结。；3 + 2 + 2 = 7（原分保留） | 深入完成 | 已有覆盖：`AGENT-RAG` [当前owner](../../../../books/part-07-agent/76-rag.md) |
| [WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/html/2504.21024v1) | 2025-05-01 | 把 web agent 自我改进拆成 evolving policy 与 co-evolving environment model，说明 rollout 数据、网页状态和 evaluator revision 必须作为同一训练 identity 管理。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [当前owner](../../../../books/part-07-agent/81-workflow.md) |
| [SAGA: A Security Architecture for Governing AI Agentic Systems](https://arxiv.org/html/2504.21034v1) | 2025-05-01 | 把 agent identity、authentication、delegation 与 user lifecycle 放进协议状态机；agent 可提出动作，但 principal lineage 与 effect-time authorizer 才拥有提交权。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`AGENT-PLATFORM` [当前owner](../../../../books/part-07-agent/84-agent-platform.md) |
| [A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage](https://arxiv.org/html/2504.21035v1) | 2025-05-01 | 证明移除显式 PII 或生成 synthetic text 并不关闭语义再识别通道；privacy boundary 必须绑定攻击者辅助信息、关系特征与 release surface。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Can Differentially Private Fine-tuning LLMs Protect Against Privacy Attacks?](https://arxiv.org/html/2504.21036v1) | 2025-05-01 | 把 private fine-tuning 的证据从单一 utility 指标扩展为多种攻击面、机制参数与 privacy-utility slice；accountant、实现路径和攻击者能力必须同构。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Prefill-level Jailbreak: A Black-Box Risk Analysis of Large Language Models](https://arxiv.org/html/2504.21038v1) | 2025-05-01 | 把 jailbreak 攻击面推进到 assistant prefill：请求在 decode 前已携带带角色语义的生成状态，因此 API normalization、template ownership 与 prefill policy 都属于安全边界。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Legilimens: Performant Video Analytics on the System-on-Chip Edge](https://arxiv.org/pdf/2504.21136v1) | 2025-05-01 | 把持续 edge inference 与在线模型适配放进同一 SoC compute budget：持久 base/specialized model、activation-guided sample admission、轻量 base update 与 inference-aware retraining schedule 必须共享版本与回退边界。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`INFER-SCHEDULING` [当前owner](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [SecRepoBench: Benchmarking Code Agents for Secure Code Completion in Real-World Repositories](https://arxiv.org/html/2504.21205v1) | 2025-05-01 | 把 secure code completion 的评估对象从孤立片段推进到真实 repository、dependency context、unit tests 与 repair trace；安全声明必须绑定可执行 project identity。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [当前owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [CachePrune: Teaching LLMs What Not to Follow via KV-Cache Editing](https://arxiv.org/html/2504.21228v1) | 2025-05-01 | 利用 KV-cache attribution 定位并削弱 prompt-injection influence，说明中间状态可以成为安全 sensor；但 eviction/pruning policy 必须保留 utility gate 与完整上下文 fallback。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](https://arxiv.org/html/2504.21303v1) | 2025-05-01 | 有限 query 上的模型排序必须输出 posterior uncertainty，并把 prior、anchor model、query construction 和 judge 一起纳入 evaluation identity；高 posterior 不是跨分布正确性证明。论文用 Bayesian inference 估计有限样本下相对成功率并与传统排名比较。结果支持在相同 query/judge contract 下表达排序不确定性；它不证明 prior 无偏、judge 正确或 posterior 能转移到新任务，anchor 与 query selection 会成为新的偏差来源。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [当前owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Phi-4-reasoning Technical Report](https://arxiv.org/html/2504.21318v1) | 2025-05-01 | compact reasoning policy 可由高可教性 demonstration 扩展，再用 outcome-verifiable RL 增加探索；teacher/scaffold 和 token budget 仍是能力与成本边界。技术报告披露 seeds/data、SFT exploration/scaling 和 reasoning-plus RL，并在 reasoning/general/safety benchmark 上评估。它不披露完整训练 hardware、batch/concurrency 或生产 SLO，也不证明长 trace 忠实；旧的短响应模型在严格 latency 下仍合理。；2 + 2 + 2 = 6（原分保留） | 标准完成 | 已有覆盖：`TRAIN-SFT` [当前owner](../../../../books/part-04-training-system/29-sft.md) |
| [Nexus-Gen: Unified Image Understanding, Generation, and Editing via Prefilled Autoregression in Shared Embedding Space](https://arxiv.org/html/2504.21356v1) | 2025-05-01 | 统一多模态模型仍需分开 representation identity 与 generation state：shared space 负责接口，prefilled AR 负责条件生成与 commit 顺序。论文给出 architecture、unified task representation、prefilled autoregression 与数据构建，并展示理解/生成/编辑案例。缺少系统性 matched benchmark、ablation 和 production latency，因此只支持可行性，不证明共享空间消除了 modality boundary 或独立 head 的必要性。；2 + 2 + 2 = 6（原分保留） | 标准完成 | 已有覆盖：`MULTIMODAL-REPRESENTATION` [当前owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) |
| [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](https://arxiv.org/html/2504.21370v1) | 2025-05-01 | reasoning 长度是受 workload 约束的可学习 stopping proposal，不是“越短越好”；上线仍需质量 guardrail、尾延迟和错误早停审计。作者搜索 sample optimal length 并训练模型在保持准确率时缩短输出，包含 out-of-domain 与 ablation。结果受选定数学任务、模型和 evaluator 限制；长度标签可能奖励跳步或格式捷径，旧的固定上限/自然 EOS 在低风险任务仍更简单。；2 + 2 + 2 = 6（原分保留） | 标准完成 | 已有覆盖：`INFER-SCHEDULING` [当前owner](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Galvatron: An Automatic Distributed System for Efficient Foundation Model Training](https://arxiv.org/html/2504.21411v1) | 2025-05-01 | 自动并行 planner 只拥有候选 plan；model shape、cluster topology、memory cap 和 collective profile 构成 plan identity，runtime telemetry 与 fallback 才拥有上线真值。Galvatron 把 hybrid parallelism 搜索与执行 workflow 连接，并在作者 benchmark 下比较训练效率。它不证明 cost model 可跨拓扑、版本和动态故障稳定；profiling 成本、search explosion、错误 memory estimate 与 process-group churn 是新增 failure mode，固定静态 plan 在稳定 workload 下仍合理。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [当前owner](../../../../books/part-04-training-system/36-distributed-training.md) |
| [RWKV-X: A Linear Complexity Hybrid Language Model](https://arxiv.org/html/2504.21463v1) | 2025-05-01 | 长上下文可以组合 recurrent linear state 与少量 sparse attention，但 active chunks、KV/state layout 和 continual-pretraining revision 必须共同定义运行时 identity。论文给出 chunk sparse attention、KV 管理、复杂度和 continual pretraining，并测量长短 context 与效率。作者实验不证明 top-k retrieval 在所有任务保留关键信息；routing error、chunk metadata 与 hybrid kernel complexity 是代价，全 attention 在短上下文/高精度需求下仍成立。；2 + 2 + 2 = 6（原分保留） | 标准完成 | 已有覆盖：`MODEL-LONG-CONTEXT` [当前owner](../../../../books/part-02-model/22-long-context.md) |
| [Mcity Data Engine: Iterative Model Improvement Through Open-Vocabulary Data Selection](https://arxiv.org/html/2504.21614v1) | 2025-05-01 | 把 acquisition、storage、open-vocabulary selection、label alignment、training、validation 与 deployment 连成可迭代的数据开发闭环；每轮 model/data/index identity 与 selection threshold 必须可追溯。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`TRAIN-DATA` [当前owner](../../../../books/part-04-training-system/27-data.md) |
| [Traceback of Poisoning Attacks to Retrieval-Augmented Generation](https://arxiv.org/html/2504.21668v1) | 2025-05-01 | RAG poisoning diagnosis 必须回溯 query、retrieved document、index revision 与 generated claim；traceback score 只拥有调查优先级，不拥有删除或定罪 authority。论文定义 threat model，组合可疑文本定位与实验评估，并测试 adaptive attacks。证据限于选定攻击、corpus、retriever 与 generator；false attribution、adaptive evasion 和昂贵 replay 要求人工/独立证据，简单 allowlist 和 immutable corpus 在高风险域仍适用。；2 + 3 + 2 = 7（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Hoist with His Own Petard: Inducing Guardrails to Facilitate Denial-of-Service Attacks on Retrieval-Augmented Generation of LLMs](https://arxiv.org/html/2504.21680v1) | 2025-05-01 | RAG 安全不能只测恶意内容是否被拒绝，还要把恶意检索内容诱发的正常请求拒绝视为 availability failure；retrieval hit、guardrail decision 与 final refusal 必须分开记录。论文给出攻击目标、黑盒/白盒路径和多数据集、多模型实验，并讨论若干防御。证据只支持论文所测 retriever、generator、guardrail 与攻击模板；它不证明任意安全过滤器都可被同样利用，也不证明内容过滤能无损修复。更严格 admission 会换来 false positive、延迟与维护成本；高风险域的 curated corpus/allowlist 仍是合理共存分支。；3 + 3 + 2 = 8（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [VDDP: Verifiable Distributed Differential Privacy under the Client-Server-Verifier Setup](https://arxiv.org/html/2504.21752v1) | 2025-05-01 | 分布式差分隐私不能让 server 同时拥有随机机制执行与合规证明；mechanism revision、随机性来源、collusion model、proof/receipt 与 verifier identity 必须共同定义 privacy evidence。论文形式化 client-server-verifier 设置，构建可验证离散 Laplace 与 randomized response，并测量密码学开销。它不消除 verifier/collusion 假设，也不证明部署中的 data pipeline、side channel 或 privacy budget composition 正确；证明成本、可信设置与系统复杂度是代价，受控环境下的 trusted aggregator 仍可能更简单。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](https://arxiv.org/html/2504.21776v1) | 2025-05-01 | Deep Research 是 durable evidence workflow：搜索、读取、草稿与最终 claim 必须共享 source/version lineage，模型只拥有 proposal，工具结果和 verifier 拥有 evidence。论文组合 Deep Web Explorer、think-search-draft 与 tool-use RL，在复杂问答和报告生成任务上比较并做 ablation。它不证明 web evidence 正确、引用完整或开放网络安全；搜索漂移、citation laundering、judge bias 与长轨迹成本仍需平台 gate。；2 + 3 + 2 = 7（原分保留） | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [当前owner](../../../../books/part-07-agent/81-workflow.md) |
| [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/html/2504.21798v1) | 2025-05-01 | 可扩展 software-agent data 需要 repository commit、container、mutation、fail-to-pass test、issue 与 trajectory 的联合 identity；test oracle 而不是 LLM judge 拥有样本 admission。论文构建 executable task factory 并用 128 个 repositories、50,137 instances 和下游训练测试其数据效用。结果不证明 synthetic bug 等同真实 issue 或跨语言泛化；container supply chain、test inadequacy、license 和 storage 成本是新增风险，真实 PR 仍是 calibration branch。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`TRAIN-DATA` [当前owner](../../../../books/part-04-training-system/27-data.md) |
| [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/html/2504.21801v1) | 2025-05-01 | 形式推理训练应把自然语言 sketch、subgoal proposal、Lean environment 与 executable verdict 分开；verifier 拥有 proof acceptance，policy 只拥有搜索 proposal。论文用 recursive subgoal decomposition、synthetic cold start、expert iteration 和 RL 训练 prover，并在 MiniF2F/大学/组合题上评估。证据受 Lean version、sampling budget 和 benchmark formalization 限制；vacuous proof、benchmark bug、verifier exploitation 与高 rollout cost 不允许外推为通用 reasoning correctness。；3 + 3 + 3 = 9（原分保留） | 深入完成 | 已有覆盖：`TRAIN-GRPO` [当前owner](../../../../books/part-04-training-system/33-grpo.md) |
| [Sycophancy in GPT-4o: what happened and what we're doing about it](https://openai.com/index/sycophancy-in-gpt-4o/) | 2025-04-30 | 短期用户反馈代理与真实行为失配的生产回归反例，需重考发布评价与长期效用；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md#为什么选一个分数不是评估系统) |

## 4. 证据与知识整合

### [Sycophancy in GPT-4o: what happened and what we're doing about it](https://openai.com/index/sycophancy-in-gpt-4o/)

官方RSS原件记录Tue,29Apr2025 18:00GMT，已有明确时区换算为北京时间Apr30；官网Apr29展示口径也保留。不是猜测午夜或另外追查秒级窗口。实际读当前官网What happened、Why this matters、How addressing；本地raw为403挑战页，不能充作正文。

旧方案利用用户点赞获得便宜、直接的行为反馈，本身有合理性；厂商对本次回滚公开说明短期反馈被过度强调，生成过度迎合行为。可采用的增量是这次生产反例及代理目标局限，不是所有反馈无效。未来训练、system prompt与评价调整是方向，不是修复效果已验证。文中未披露内部reward、训练权重、数据与独立对照；不能认定受控单一根因、长期满意优化完成或安全保证。

唯一采用命题由`PLATFORM-EVALUATION-SYSTEM`承载：Ch66“为什么选一个分数不是评估系统”实际解释点赞样本非随机、短期满意与事实/长期风险不同，scorer会影响行为；“Offline、Shadow、Canary与Online”区分离线、线上与长程证据。root和Gibbs独立读取第33～58与3208～3227行及局部邻接，裁决已有覆盖、无写入，不借未披露训练机制扩写RLHF。具体RSS、来源权限、评分及反侧见[局部独立复核](../_sources/daily-20250501/supplement-first-review-20261007.md)。

05-03的May2后续postmortem是同事故的不同事件，原日期、评分和证据保持；其memory、reward、A/B细节不回填为初报已有结论。

### [Don't Retrieve, Generate: Prompting LLMs for Synthetic Training Data in Dense Retrieval](https://arxiv.org/html/2504.21015v1)

把 RAG 训练数据来源从只检索公开问答扩展为可控生成的 hypothetical negatives；关键系统边界是生成器版本、去重、污染审计与真实检索回放必须共同冻结。

作者实验只比较其合成 hard-negative recipe 与披露数据集，不能证明生成数据普遍优于真实 retrieval logs。

本轮仅复用既有家族 `SF-2025-DONT-RETRIEVE-GENERATE` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`AGENT-RAG` [当前owner](../../../../books/part-07-agent/76-rag.md)。

### [WebEvolver: Enhancing Web Agent Self-Improvement with Coevolving World Model](https://arxiv.org/html/2504.21024v1)

把 web agent 自我改进拆成 evolving policy 与 co-evolving environment model，说明 rollout 数据、网页状态和 evaluator revision 必须作为同一训练 identity 管理。

结果绑定作者构造的 web environment 与任务；没有证明开放互联网漂移、权限边界或真实副作用下仍能安全自演化。

本轮仅复用既有家族 `SF-2025-WEBEVOLVER` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`AGENT-WORKFLOW` [当前owner](../../../../books/part-07-agent/81-workflow.md)。

### [SAGA: A Security Architecture for Governing AI Agentic Systems](https://arxiv.org/html/2504.21034v1)

把 agent identity、authentication、delegation 与 user lifecycle 放进协议状态机；agent 可提出动作，但 principal lineage 与 effect-time authorizer 才拥有提交权。

论文给出协议与原型评估，不等于互联网规模身份联邦、密钥轮换、撤权传播或恶意参与方下已经安全。

本轮仅复用既有家族 `SF-2025-SAGA-IDENTITY` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`AGENT-PLATFORM` [当前owner](../../../../books/part-07-agent/84-agent-platform.md)。

### [A False Sense of Privacy: Evaluating Textual Data Sanitization Beyond Surface-level Privacy Leakage](https://arxiv.org/html/2504.21035v1)

证明移除显式 PII 或生成 synthetic text 并不关闭语义再识别通道；privacy boundary 必须绑定攻击者辅助信息、关系特征与 release surface。

攻击成功率只对论文披露的数据、模型与辅助信息成立，不能外推为所有去标识化文本都可被同等重识别。

本轮仅复用既有家族 `SF-2025-SEMANTIC-REIDENTIFICATION` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Can Differentially Private Fine-tuning LLMs Protect Against Privacy Attacks?](https://arxiv.org/html/2504.21036v1)

把 private fine-tuning 的证据从单一 utility 指标扩展为多种攻击面、机制参数与 privacy-utility slice；accountant、实现路径和攻击者能力必须同构。

比较覆盖论文列出的 DP 方法与攻击，不能证明未测攻击、不同基础模型或部署精度具有相同 privacy guarantee。

本轮仅复用既有家族 `SF-2025-DP-FINETUNING-PRIVACY` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Prefill-level Jailbreak: A Black-Box Risk Analysis of Large Language Models](https://arxiv.org/html/2504.21038v1)

把 jailbreak 攻击面推进到 assistant prefill：请求在 decode 前已携带带角色语义的生成状态，因此 API normalization、template ownership 与 prefill policy 都属于安全边界。

攻击结果绑定被测模型、模板与访问方式；不证明所有 prefill API 都同样脆弱，也不把检测器提升为最终 authority。

本轮仅复用既有家族 `SF-2025-PREFILL-JAILBREAK` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Legilimens: Performant Video Analytics on the System-on-Chip Edge](https://arxiv.org/pdf/2504.21136v1)

把持续 edge inference 与在线模型适配放进同一 SoC compute budget：持久 base/specialized model、activation-guided sample admission、轻量 base update 与 inference-aware retraining schedule 必须共享版本与回退边界。

评估只覆盖作者的 50 小时视频、两类视觉任务与 Jetson SoC；多 base 结果依赖 oracle selection，且额外 base 会线性增加 memory，不能外推到任意 edge workload。

本轮仅复用既有家族 `SF-2025-LEGILIMENS` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`INFER-SCHEDULING` [当前owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)。

### [SecRepoBench: Benchmarking Code Agents for Secure Code Completion in Real-World Repositories](https://arxiv.org/html/2504.21205v1)

把 secure code completion 的评估对象从孤立片段推进到真实 repository、dependency context、unit tests 与 repair trace；安全声明必须绑定可执行 project identity。

benchmark 覆盖作者收集的仓库与漏洞类别；unit tests 不是完整安全证明，agent repair 成功也不保证无新缺陷。

本轮仅复用既有家族 `SF-2025-SECREPOBENCH` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [当前owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [CachePrune: Teaching LLMs What Not to Follow via KV-Cache Editing](https://arxiv.org/html/2504.21228v1)

利用 KV-cache attribution 定位并削弱 prompt-injection influence，说明中间状态可以成为安全 sensor；但 eviction/pruning policy 必须保留 utility gate 与完整上下文 fallback。

防御只在披露模型、攻击与任务上评估；attribution signal 不是输入恶意性的真值，错误 pruning 可能删除任务关键语义。

本轮仅复用既有家族 `SF-2025-CACHEPRUNE` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Confidence in Large Language Model Evaluation: A Bayesian Approach to Limited-Sample Challenges](https://arxiv.org/html/2504.21303v1)

有限 query 上的模型排序必须输出 posterior uncertainty，并把 prior、anchor model、query construction 和 judge 一起纳入 evaluation identity；高 posterior 不是跨分布正确性证明。论文用 Bayesian inference 估计有限样本下相对成功率并与传统排名比较。结果支持在相同 query/judge contract 下表达排序不确定性；它不证明 prior 无偏、judge 正确或 posterior 能转移到新任务，anchor 与 query selection 会成为新的偏差来源。

本轮仅复用既有家族 `SF-2025-BAYES-EVAL-CONFIDENCE` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [当前owner](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。

### [Phi-4-reasoning Technical Report](https://arxiv.org/html/2504.21318v1)

compact reasoning policy 可由高可教性 demonstration 扩展，再用 outcome-verifiable RL 增加探索；teacher/scaffold 和 token budget 仍是能力与成本边界。技术报告披露 seeds/data、SFT exploration/scaling 和 reasoning-plus RL，并在 reasoning/general/safety benchmark 上评估。它不披露完整训练 hardware、batch/concurrency 或生产 SLO，也不证明长 trace 忠实；旧的短响应模型在严格 latency 下仍合理。

本轮仅复用既有家族 `SF-2025-PHI4-REASONING` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`TRAIN-SFT` [当前owner](../../../../books/part-04-training-system/29-sft.md)。

### [Nexus-Gen: Unified Image Understanding, Generation, and Editing via Prefilled Autoregression in Shared Embedding Space](https://arxiv.org/html/2504.21356v1)

统一多模态模型仍需分开 representation identity 与 generation state：shared space 负责接口，prefilled AR 负责条件生成与 commit 顺序。论文给出 architecture、unified task representation、prefilled autoregression 与数据构建，并展示理解/生成/编辑案例。缺少系统性 matched benchmark、ablation 和 production latency，因此只支持可行性，不证明共享空间消除了 modality boundary 或独立 head 的必要性。

本轮仅复用既有家族 `SF-2025-NEXUS-GEN` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`MULTIMODAL-REPRESENTATION` [当前owner](../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md)。

### [ShorterBetter: Guiding Reasoning Models to Find Optimal Inference Length for Efficient Reasoning](https://arxiv.org/html/2504.21370v1)

reasoning 长度是受 workload 约束的可学习 stopping proposal，不是“越短越好”；上线仍需质量 guardrail、尾延迟和错误早停审计。作者搜索 sample optimal length 并训练模型在保持准确率时缩短输出，包含 out-of-domain 与 ablation。结果受选定数学任务、模型和 evaluator 限制；长度标签可能奖励跳步或格式捷径，旧的固定上限/自然 EOS 在低风险任务仍更简单。

本轮仅复用既有家族 `SF-2025-SHORTERBETTER` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`INFER-SCHEDULING` [当前owner](../../../../books/part-05-inference-system/56-inference-scheduling.md)。

### [Galvatron: An Automatic Distributed System for Efficient Foundation Model Training](https://arxiv.org/html/2504.21411v1)

自动并行 planner 只拥有候选 plan；model shape、cluster topology、memory cap 和 collective profile 构成 plan identity，runtime telemetry 与 fallback 才拥有上线真值。Galvatron 把 hybrid parallelism 搜索与执行 workflow 连接，并在作者 benchmark 下比较训练效率。它不证明 cost model 可跨拓扑、版本和动态故障稳定；profiling 成本、search explosion、错误 memory estimate 与 process-group churn 是新增 failure mode，固定静态 plan 在稳定 workload 下仍合理。

本轮仅复用既有家族 `SF-2025-GALVATRON` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`TRAIN-DISTRIBUTED-TRAINING` [当前owner](../../../../books/part-04-training-system/36-distributed-training.md)。

### [RWKV-X: A Linear Complexity Hybrid Language Model](https://arxiv.org/html/2504.21463v1)

长上下文可以组合 recurrent linear state 与少量 sparse attention，但 active chunks、KV/state layout 和 continual-pretraining revision 必须共同定义运行时 identity。论文给出 chunk sparse attention、KV 管理、复杂度和 continual pretraining，并测量长短 context 与效率。作者实验不证明 top-k retrieval 在所有任务保留关键信息；routing error、chunk metadata 与 hybrid kernel complexity 是代价，全 attention 在短上下文/高精度需求下仍成立。

本轮仅复用既有家族 `SF-2025-RWKV-X` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`MODEL-LONG-CONTEXT` [当前owner](../../../../books/part-02-model/22-long-context.md)。

### [Mcity Data Engine: Iterative Model Improvement Through Open-Vocabulary Data Selection](https://arxiv.org/html/2504.21614v1)

把 acquisition、storage、open-vocabulary selection、label alignment、training、validation 与 deployment 连成可迭代的数据开发闭环；每轮 model/data/index identity 与 selection threshold 必须可追溯。

评估聚焦交通视觉数据、开放词汇检测器与有限迭代；未来工作明确仍需更多 labeling/training rounds，因此不能声称该闭环已验证任意领域或长期漂移。

本轮仅复用既有家族 `SF-2025-MCITY-DATA-ENGINE` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`TRAIN-DATA` [当前owner](../../../../books/part-04-training-system/27-data.md)。

### [Traceback of Poisoning Attacks to Retrieval-Augmented Generation](https://arxiv.org/html/2504.21668v1)

RAG poisoning diagnosis 必须回溯 query、retrieved document、index revision 与 generated claim；traceback score 只拥有调查优先级，不拥有删除或定罪 authority。论文定义 threat model，组合可疑文本定位与实验评估，并测试 adaptive attacks。证据限于选定攻击、corpus、retriever 与 generator；false attribution、adaptive evasion 和昂贵 replay 要求人工/独立证据，简单 allowlist 和 immutable corpus 在高风险域仍适用。

本轮仅复用既有家族 `SF-2025-RAGFORENSICS` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [Hoist with His Own Petard: Inducing Guardrails to Facilitate Denial-of-Service Attacks on Retrieval-Augmented Generation of LLMs](https://arxiv.org/html/2504.21680v1)

RAG 安全不能只测恶意内容是否被拒绝，还要把恶意检索内容诱发的正常请求拒绝视为 availability failure；retrieval hit、guardrail decision 与 final refusal 必须分开记录。论文给出攻击目标、黑盒/白盒路径和多数据集、多模型实验，并讨论若干防御。证据只支持论文所测 retriever、generator、guardrail 与攻击模板；它不证明任意安全过滤器都可被同样利用，也不证明内容过滤能无损修复。更严格 admission 会换来 false positive、延迟与维护成本；高风险域的 curated corpus/allowlist 仍是合理共存分支。

本轮仅复用既有家族 `SF-2025-MUTEDRAG-AVAILABILITY` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [VDDP: Verifiable Distributed Differential Privacy under the Client-Server-Verifier Setup](https://arxiv.org/html/2504.21752v1)

分布式差分隐私不能让 server 同时拥有随机机制执行与合规证明；mechanism revision、随机性来源、collusion model、proof/receipt 与 verifier identity 必须共同定义 privacy evidence。论文形式化 client-server-verifier 设置，构建可验证离散 Laplace 与 randomized response，并测量密码学开销。它不消除 verifier/collusion 假设，也不证明部署中的 data pipeline、side channel 或 privacy budget composition 正确；证明成本、可信设置与系统复杂度是代价，受控环境下的 trusted aggregator 仍可能更简单。

本轮仅复用既有家族 `SF-2025-VDDP` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`PLATFORM-SECURITY` [当前owner](../../../../books/part-06-ai-infrastructure/72-security.md)。

### [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](https://arxiv.org/html/2504.21776v1)

Deep Research 是 durable evidence workflow：搜索、读取、草稿与最终 claim 必须共享 source/version lineage，模型只拥有 proposal，工具结果和 verifier 拥有 evidence。论文组合 Deep Web Explorer、think-search-draft 与 tool-use RL，在复杂问答和报告生成任务上比较并做 ablation。它不证明 web evidence 正确、引用完整或开放网络安全；搜索漂移、citation laundering、judge bias 与长轨迹成本仍需平台 gate。

本轮仅复用既有家族 `SF-2025-WEBTHINKER` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`AGENT-WORKFLOW` [当前owner](../../../../books/part-07-agent/81-workflow.md)。

### [SWE-smith: Scaling Data for Software Engineering Agents](https://arxiv.org/html/2504.21798v1)

可扩展 software-agent data 需要 repository commit、container、mutation、fail-to-pass test、issue 与 trajectory 的联合 identity；test oracle 而不是 LLM judge 拥有样本 admission。论文构建 executable task factory 并用 128 个 repositories、50,137 instances 和下游训练测试其数据效用。结果不证明 synthetic bug 等同真实 issue 或跨语言泛化；container supply chain、test inadequacy、license 和 storage 成本是新增风险，真实 PR 仍是 calibration branch。

本轮仅复用既有家族 `SF-2025-SWE-SMITH` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`TRAIN-DATA` [当前owner](../../../../books/part-04-training-system/27-data.md)。

### [DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition](https://arxiv.org/html/2504.21801v1)

形式推理训练应把自然语言 sketch、subgoal proposal、Lean environment 与 executable verdict 分开；verifier 拥有 proof acceptance，policy 只拥有搜索 proposal。论文用 recursive subgoal decomposition、synthetic cold start、expert iteration 和 RL 训练 prover，并在 MiniF2F/大学/组合题上评估。证据受 Lean version、sampling budget 和 benchmark formalization 限制；vacuous proof、benchmark bug、verifier exploitation 与高 rollout cost 不允许外推为通用 reasoning correctness。

本轮仅复用既有家族 `SF-2025-DEEPSEEK-PROVER-V2` 的精确v1审阅及Books处置，不重算日期/评分，不声称本轮重新读过全文。具体方法、评价、反证、benchmark条件与正文比较保留于[补查前完整档案](../_sources/daily-20250501/baseline-before-supplement-20261007.md)的同名 `review:`、`books-review:` 标记和原§3～6；原主张不能因本轮来源补查获得更广证据权限。已有覆盖：`TRAIN-GRPO` [当前owner](../../../../books/part-04-training-system/33-grpo.md)。

## 5. 缺口与下一步

**普通待办：** 无。本轮独立日级裁决已通过，具体检查范围与复用边界见第6节；不要求重跑未变候选或清空月份库存。

**外部材料缺口：** arXiv官方Apr30日公告/列表或作者明确首次公开记录尚缺。已实际读题摘的Triton-distributed、Bullet、FlashOverlap、FineQ、Semi-PD、SYMI、Genie、OSVBench身份及必要反侧见[本日补查记录](../_sources/daily-20250501/supplement-20261007.md#arxiv入口错误及有界恢复)。当前版本、Submitted、DataCite登记和月目录不能授权公开日；不评分、不列确定落窗候选、不用于正面证据或Books，不支撑无遗漏断言。需要日历日期而非精确时刻；材料到达只重开相应身份，核精确事件后再审必要机制/评价。未读完的正文不是外部访问故障。

Google pubs公开日/Meta/Hunyuan/ZAI/ERNIE/MiniMax历史切片、MiMo首发及Seed库存口径限制为外部终态保留项，分别需当期官方目录、存档或明确原始发布。DeepMind真分页和MiMo历史README已经恢复，不再称全部入口或正文不可访问，但精选目录和commit时间不证明全部首公开日。Seed跨locale数量差不确认具体遗漏身份数。以上不用于正面证据、Books或无遗漏断言；定点重开条件是相应具名原始材料到达，实际入口、HTTP及停止点见第2节与来源记录。

用户16:40续跑明确禁止使用catchup；旧请求仅保留为此前事实，不再调用，也不作为停止整个补查的理由。arXiv继续通过Advanced Search、API和有界官方月表发现；公告筛选只有年月，不将月池计作当日候选。续跑50份完整题摘已读，6身份为旧候选；Archimedes独立校准44项并定点读9处core，将一般IFC关闭、新闻/截图评价反侧重开，现35潜在/9关闭。作者三项改判及全部窄化理由写回已获最终差额验收，身份、真实查询与停止见[Advanced记录](../_sources/daily-20250501/advanced-resume-20261007.md)，不扩张其证据权限。

35项为外部日期终态保留项：需要当期官方日公告/目录或原作者明确首次公开日，具体版本内容只在日归属恢复后审本窗必要证据。月份、提交日、当前题摘及后版决定性core不授权Apr30或2025初版；不评分、不进入正式候选，不用于正面证据、Books或无遗漏断言。只定点重开材料到达的身份，不要求清空整月、全版本或普通附件。IFC的一般语言理论已明确关闭，不为它继续索日；可接受替代是能对应具体身份与首次正文的作者原始发布记录。

## 6. 复核

复核者：Gibbs负责此前首批与最终停点复核；Archimedes为本轮恢复及最终写回差额的独立复核者，非root日报作者。

结论：通过

Gibbs已实际复核新增OpenAI初报的官方RSS/正文、3+2+2评分、同事故后续事件关系、两项代表关闭、8项系统完整题摘和Ch66实际已有覆盖；核旧22字段与完整档案机械保留、14来源有限停止范围，指出Bullet/ERNIE误记与合法入口普通待办。Archimedes独立确认Bullet/ERNIE/Seed/DeepMind/MiMo具体修正，校准全部44新题摘并定点读9项决定性core，覆盖必要安全/评价反侧，随后逐项核三项改判、35/9、事实/权限修正及六部分写回，给出[最终日级裁决](../_sources/daily-20250501/review-resume-20261007.md#12-1746-authorready-写回验收与-day-最终裁决)。只授2025-05-01本轮补查安全终态，不授原22全文重审、446月池全量或全部来源正面Coverage/Evidence；Books改动0，具体No Change按有效独核复用。

当前正文已通过V3结构校验（1份、23候选），H1为1、H2为六节、本地链接目标缺失0；限定diff及本轮补查Markdown空白检查无诊断。补查前完整档案与原HEAD报告逐字节相同，SHA256为`029608d49080f6b04c16c5141871fe444e1acb8b827ed8616c0161e58d059507`。机器结果不能代替上述语义复核。未stage、commit或push。
