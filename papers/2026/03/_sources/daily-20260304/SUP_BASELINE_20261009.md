# Daily Research — 2026-03-04

**规范：** V3
**窗口：** 2026-03-03T09:00:00+08:00 ～ 2026-03-04T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T22:59:42+08:00

## 1. 结论

独立按当前V3重建。旧286KB报告完整保存在[原文存档](../_sources/daily-20260304/V3_LEGACY_REPORT.md)，不继承旧33项、全9分或模板完成标签；1270条宽分类库存只作相关标题查漏，不是逐项全文队列。
本日十六个唯一家族全部达到证据与Books安全终态：十四项真实窄整合、两项具体已有覆盖，5～7分按实际证据区分。root原六项复用接手作者前mar02_v3独立题摘/日期/已有覆盖和mar01_v3、mar03_v3必要源/实际POST；mar02_v3新增十项由root非作者必要源→实际Books处置通过，整日分批独立复核通过，普通待办0。GPT5.3 card及00063/00188/00196精确日期隔离，不计确定候选或Books，不支持无遗漏。

## 2. 来源覆盖

仅14个Daily源，不扩Weekly。以下是执行时可见历史段，不是当时不可变快照；查询/原字段/停止范围见[本日停点](../_sources/daily-20260304/V3_WORKING_STOPPOINT.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [Research](https://openai.com/research/)与[RSS](https://openai.com/news/rss.xml)，限定Mar03～04条目，GPT5.3 release/card/Hub及PDF核心已读 | 受阻 | release机制未披露贡献前关闭；card RSS/landing/PDF March3 vs Hub PublishedMarch2首公开冲突隔离，不撑零事件 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research)嵌入Public Research，Feb25→Mar05相邻及日/主题补检 | 已检查 | 当前可见段无本窗记录，不证明全部历史 |
| SRC-GOOGLE-AI | [DeepMind](https://deepmind.google/research/)精选/Blog page3和[pubs](https://research.google/pubs/)年级索引；GeminiFlashLite发布/card核心及安全反证已读 | 受阻 | Gemini具体负理由关闭；pubs本窗日级段未恢复，安全表不直接跨card比较 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)空响应及官方域日/模型主题补检 | 受阻 | 空页和搜索无命中不能证明零事件，缺本窗历史段 |
| SRC-QWEN | [Blog](https://qwenlm.github.io/)当前段/qwen.ai重定向，主题补检与QwenCode v0.11.1/PR2021四core及tests patch | 受阻 | 截断正确性已窄写并通过root实际POST；动态模型Blog历史目录受限 |
| SRC-DEEPSEEK | [Research/News](https://www.deepseek.com/en/news/)Research10项Feb25→Jun24，News首5项及有限补检 | 受阻 | 可见Research已查；隐藏News/View All本窗段未恢复 |
| SRC-MOONSHOT | [实际Research目录](https://www.kimi.com/en/blog/)，19项至2024/06/26，2/09 AgentSwarm→4/20 K2.6跨本窗，无可见未完分页 | 已检查 | 仅当前可见Research段，旧platform不代表全机构历史不可恢复；不授被删除历史无遗漏 |
| SRC-TENCENT-HUNYUAN | [全部列表](https://hunyuan.tencent.com/research)及[实际恢复记录](../_sources/V3_HUNYUAN_LIST_RECOVERY.md)，11/11、Feb13→Apr23相邻 | 已检查 | 仅当前可见列表，display与后台日期不互授首发 |
| SRC-ZAI | [Research](https://www.zhipuai.cn/zh/research)首可见页Feb21→Mar15，查看更多停止 | 已检查 | 不称全机构或被删除历史完整 |
| SRC-BYTEDANCE-SEED | [Research](https://seed.bytedance.com/en/research)精选，public_papers首20/242、page1of13止May14及有限补检 | 受阻 | 缺本窗Blog/论文段，242不是当日候选 |
| SRC-BAIDU-ERNIE | [Blog](https://ernie.baidu.com/blog/zh/)68行Apr15→Feb06相邻及有限补检 | 已检查 | 仅可见目录范围 |
| SRC-XIAOMI-MIMO | [Paper/Blog](https://mimo.xiaomi.com/)Paper8项Mar13→Feb03，Blog15项无日期/More停止 | 受阻 | Paper段已查；Blog本窗日期/分页缺失 |
| SRC-MINIMAX | [英文](https://www.minimax.io/blog)76行/[中文](https://www.minimaxi.com/blog)68行，相邻日期与主题补检 | 已检查 | 有限当前目录，不扩历年Tech Blog |
| SRC-ARXIV | 模型后训练、推理通信调度、多模态World Model与Agent有界主题查询；宽库存只补相关标题；具名追加9项及早4项实际完整题摘 | 受阻 | 十五论文家族准入/必要证据与复合公开范围已核；00063/00188/00196首公开下界不明精确隔离，不计零命中或全库存审阅 |

## 3. 候选与判断

下列十六项为本日有界研究确认落窗的唯一家族。表中范围是支持的arXiv公开区间，不是补造公告时刻。5～6分项因明确长期知识缺口或评价/安全边界，深入审阅受影响内容，不为Books提分；日期隔离项不混入分母。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Token Management in Multi-Tenant AI Inference Platforms](https://arxiv.org/abs/2603.00356v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:44:57+08:00 | 当前占用不等于未来生成承诺 → token池预留、completion归还/债务 → 分开admission与结算；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs](https://arxiv.org/abs/2603.00357v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:44:58+08:00 | checkpoint丢失本轮工作 → shard stack重排/补算后提交 → 冗余与checkpoint周期联合选择；2 + 2 + 3 = 7 | 深入完成 | 整合：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning](https://arxiv.org/abs/2603.01639v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:14:35+08:00 | depth/size单独优化依赖固定对方 → 交替协同 → 计draft+verify成本而非只看接受长度；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [FreeAct: Freeing Activations for LLM Quantization](https://arxiv.org/abs/2603.01776v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:17:42+08:00 | 异质token共用逆变换 → 条件零空间/专用基底与统一weight → 区分投影等价与量化近似；2 + 2 + 2 = 6 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:19:48+08:00 | 固定judge偏移/全panel预算冲突 → 均衡轮换 → 分开生成、场景、judge预算；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AdaPonderLM: Gated Pondering Language Models with Token-Wise Adaptive Depth](https://arxiv.org/abs/2603.01914v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:20:56+08:00 | 停止更新不等于删除位置 → 单调halt保留前轮KV → 训练/推理状态一致；2 + 1 + 2 = 5 | 深入完成 | 整合：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Curation Leaks](https://arxiv.org/abs/2603.00811v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:55:27+08:00 | 私有target未训练仍指导public curation → 三观察面间接泄漏 → privacy scope不能止于训练字节；3+1+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，root实际POST通过 |
| [Collaborative Obfuscation](https://arxiv.org/abs/2603.01499v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:11:22+08:00 | 只变输入损伤推理 → 联合数据/模型近似变换 → 分开计算等价与保密访问假设；2+2+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，root实际POST通过 |
| [QwenCode v0.11.1 / PR2021](https://github.com/QwenLM/qwen-code/releases/tag/v0.11.1) | 2026-03-03T21:08:44+08:00 | provider伪finish与JSONrepair可生成合法但截断编辑 → 原stream状态传播/Kind.Edit拒绝 → 完整性不能由schema替代；3+1+3=7 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md)，root实际POST通过 |
| [EmCoop v1](https://arxiv.org/abs/2603.00349v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:44:48+08:00 | 对话轮次混淆环境进展 → 双时钟/可观察协作约束 → 区分等待与动作失败；2+2+2=6 | 深入完成 | 整合：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md)，root实际POST通过 |
| [Verifier-Bound Communication](https://arxiv.org/abs/2603.00381v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:45:31+08:00 | 身份/schema未排除合法选择隐蔽信号 → pinned predicate准入与残余界分开 → 证明不授所有通信安全；2+2+3=7 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，root实际POST通过 |
| [Cloud-OpsBench](https://arxiv.org/abs/2603.00468v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:47:33+08:00 | 工具结构完成不等诊断正确 → frozen响应/三元组与路径分账 → 静态回放不评主动修复；2+2+2=6 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，root必要源/实际已有覆盖通过 |
| [MemPO](https://arxiv.org/abs/2603.00680v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T12:52:25+08:00 | 全局reward难归因memory → gold-answer相对前史likelihood辅助信用 → proxy与状态偏差/成本分账；2+2+3=7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，root实际POST通过 |
| [GRPO Policy Gradient as U-Statistic](https://arxiv.org/abs/2603.01162v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:03:43+08:00 | 同题依赖误当独立 → LOO/未clip estimator身份 → 固定N下prompt/group预算分账；2+2+3=7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)，root实际POST通过 |
| [Trident](https://arxiv.org/abs/2603.02075v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:24:41+08:00 | 异步负载污染容量观测 → config失配invalidate/warmup → 调参proposal与切换状态分离；2+2+3=7 | 深入完成 | 整合：TRAIN-DATA，[Ch27](../../../../books/part-04-training-system/27-data.md)，root实际POST通过 |
| [AgentSkillOS](https://arxiv.org/abs/2603.02176v1) | 2026-03-03T09:00:00+08:00 ～ 2026-03-03T13:27:03+08:00 | 目录可见不等run装载 → active/dormant/selected graph分层 → 编排与执行准入分开；2+2+2=6 | 深入完成 | 整合：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md)，root实际POST通过 |

## 4. 证据与知识整合

### [Token Management in Multi-Tenant AI Inference Platforms](https://arxiv.org/abs/2603.00356v1)

实际读v1容量池、预留/回调/超额债务及必要评价。token预算是容量代理，须与KV admission、并发及实际完成成本共同定义；Qwen3-8B/NVFP4单负载不授跨模型或生产SLO。本次不采用倍率。Ch56容量预留/结算已有input+maximum output承诺、completion归还及债务，不逐decode结算；具体已有覆盖，不新增Books。

### [SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs](https://arxiv.org/abs/2603.00357v1)

v1 §3.1–3.2/Alg1–2、§4.2/§5支持stack/shard复制、最浅覆盖、HK-Fixed/HK-Free与MCMF迁移，patch compute后shrink/allreduce/update/commit；shard wipe-out回checkpoint。完整不重复梯度及幸存状态一致是采用合同，不是所有optimizer等价已实证。§5是SimGrid模拟且恢复成本有强假设，相关故障/silent corruption不受fail-stop保证。Ch36 Failure两段真实整合，mar01_v3、mar03_v3非作者必要源/实际POST通过，旧恢复与异步分支保留。

### [Learning To Draft: Adaptive Speculative Decoding with Reinforcement Learning](https://arxiv.org/abs/2603.01639v1)

v1 §4两策略先独立训练再交替冻结更新，reward=accepted tokens/(draft+verify time)。§5/Table4组件并非各模型单调增益；HumanEval训练和指定MTBench/GSM8K/Alpaca/NQ测试不授跨硬件/并发/SLO迁移。本次不采用倍率，生产配置Not Disclosed。Ch48 BlockPilot后两段真实整合策略协同、target提交权与控制成本，mar01_v3必要源/实际POST通过。

### [FreeAct: Freeing Activations for LLM Quantization](https://arxiv.org/abs/2603.01776v1)

v1 §3.1–3.3/Theorem2要求专用基底对另一类activation投影为零，类型标签不授未量化等价。§4.3–4.4删过多维度、固定全层比例/去clipping可能退步，不把收益全部归于变换。Appendix F为fake quantization、未offline deploy；不能称硬件加速已验。本次只采用类型/共享专用基底与校准近似条件。Ch49 Rotation Scope节首两段真实整合，复用mar01_v3非作者必要源/实际POST通过结果。

### [CyclicJudge: Mitigating Judge Bias Efficiently in LLM-based Evaluation](https://arxiv.org/abs/2603.01865v1)

v1 §3加性模型拆场景、生成、中心化固定judge与独立residual；均衡权重/预算抵消有限panel偏移，不消外部真值偏差、交互或共同误校准。§4有限场景/模型/ bootstrap只支持局部预算设计，不授任意CI覆盖。Ch66 Judge Agreement节首两段真实整合，人工残差校准职责保留；mar01_v3必要源/实际POST通过。

### [AdaPonderLM: Gated Pondering Language Models with Token-Wise Adaptive Depth](https://arxiv.org/abs/2603.01914v1)

v1 §3 Eq9停止embedding更新、Eq10保留前轮KV，不能推断所有hidden readout冻结。§4.4去bottom-K/简化gate可全停或不停，比例/正则改变质量。Table3含410M退步及不同额外tokens；FLOPs非wall-clock，不采用零质量成本。Ch18循环监督与停止两段真实整合，按非作者反例已小修halt对象，复用mar01_v3最终实际POST通过结果。

### [Curation Leaks](https://arxiv.org/abs/2603.00811v1)

v1 §3.1/Table1、§3.5、§4–6支持private target完全不训练而间接影响public selection；score/mask被动观察与最终model主动fingerprint权限不同。TRAK聚合/target规模/DP代价限制信号，不采普遍恢复率。Ch72原I/E/O筛选参与者论证缺这条public-pool反例，现后接两段及证据行，root必要源/实际邻接POST通过。范围03/03T09:00～12:55:27+08，Submitted02/28T21:14:01Z、原机构findable registered03/03T04:55:26Z，使用同下述官方复合依据。

### [Collaborative Obfuscation](https://arxiv.org/abs/2603.01499v1)

v1 §3–5.5、§6.1–6.4实际读：honest-but-curious、联合token/权重变换与noise，RoPE及Gaussian输入RMSNorm近似，static界不覆盖dynamic词频/恶意执行。Table2及§6.3是通用隐私/质量宣传的直接反证，不采用倍率或完整定理保证。Ch72 private inference两段后实际新增替代分支与精度/访问边界，root必要源→实际正文/邻接POST通过。范围03/03T09:00～13:11:22+08，Submitted03/02T06:16:36Z、原机构findable registered03/03T05:11:21Z，同官方复合依据。

### [QwenCode v0.11.1 / PR2021](https://github.com/QwenLM/qwen-code/releases/tag/v0.11.1)

本窗release published_at03/03T13:08:44Z明确包含PR2021；PR created02/28T11:25:53Z/merged03/02T12:59:36Z是早期事件。实际四core+tests patch核原stream depth/inString检查、converter length覆盖、pending截断flag及Kind.Edit拒绝；nonEdit非全部拒、无name buffer跳过，不授语义完整性或事务回滚。Ch78现provider finish门槛缺伪finish/JSONrepair反例，后接两段及证据行，root实际primary→正文邻接POST通过；tests未本地运行。head/merge SHA及准确路径见[有限记录](../_sources/daily-20260304/V3_NONAUTHOR_BOUNDED_REVIEW_MAR02.md)。

日期证据：六项实际DataCite client=arxiv.content、state=findable，registered UTC依次03-03T04:44:56/04:44:57/05:14:34/05:17:41/05:19:47/05:20:55。v1 Submitted前两项02-27T22:44:09/27Z，另四项03-02T09:17:48/12:02:17/13:46:32/14:28:16Z。结合[公告日程](https://info.arxiv.org/help/availability.html)的最早普通公开下界与[官方DOI](https://info.arxiv.org/help/doi.html)的ID不预分配、原机构findable注册上界，得到完全落窗范围（半开区间秒级上界加1秒）。不是将Submitted、created或registered单独当首发，不声称排除了更早作者发布；[实际API示例](https://api.datacite.org/dois/10.48550/arXiv.2603.00356)同接口替换ID复查。新两篇同接口重新核原机构字段，非沿用旧date proxy。

### [EmCoop v1](https://arxiv.org/abs/2603.00349v1)

必要§3、§5、§6–7实际读：cognitive与embodied primitive双时钟、interrupt/resume/wait日志和可观察协作约束支持区分协调停滞/环境执行失败；all-ready joint-action barrier不等真实完全异步。二至三Agent、两环境、有限模型/拓扑和单例feedback不授通用最优或通信免费。本窗采用exact-v1 EmCoop；当前DataCite COOP²是05/27 v2标题，不将其verification-repair理由倒灌。Ch82原WorldState新颖性论证未涵盖双时钟，现前接966–968两段+note，root实际POST通过。

### [Verifier-Bound Communication](https://arxiv.org/abs/2603.00381v1)

必要§2–4/Algorithm2/Assumption4.1、§6/Table1–4、§7–9支持pinned policy/seed/chain/schema/tool-env receipt的predicate验后才推进transcript。residual MI预算是前提，合法语义选择仍有通道；decoder失败与有限经验MI不认证零泄漏，抽样证明改变assurance scope。Ch72现通信edge身份与provenance缺合法选择分支，652–654两段实际窄补；不认证完整组合定理，root实际POST通过。

### [Cloud-OpsBench](https://arxiv.org/abs/2603.00468v1)

必要§3.1–3.3、§4.2/Table4、§4.4/§4.6/Table5、§5.3区分mock工具静态快照、TCR结构完成、rootcause三元组正确与canonicalpath；路径不是全部合法解，不能评active remediation。跨模型冗余/成功是相关非安全因果，ICL并非每模型都优于RAG，不采用排行榜。Ch66实际367–371 outcome/process、1373–1377 API回放/在线authority已有覆盖；不制造diff，root必要源/实际已有覆盖通过。

### [MemPO](https://arxiv.org/abs/2603.00680v1)

必要§3.3、§4.1–4.4/Eq4–5/9、§5.1–5.5/Limitations支持gold-answer长度归一likelihood相对完整前史的辅助memory reward，memory token局部与全局信用分开。π_theta是原scoring policy；匹配版本是比较约束，不编造独立frozen evaluator。状态不等价偏差、gold/上下文评分成本与proxy非truth/causal全部保留。Ch77原masked信用未承载此替代路径，现144–146两段实际补；root必要源→实际正文/邻接POST通过。

### [GRPO Policy Gradient as U-Statistic](https://arxiv.org/abs/2603.01162v1)

必要§3.1–3.2、§4.1–4.2、§5.1–5.2支持当前policy条件i.i.d.、LOO居中、未clip score-function identity，fullmean需G/(G−1)rescale；不覆盖reward标准化、旧样本IS、clip/KL完整实现。固定N=BG方差上界的prompt异质性与同题残差权衡，不是universal最优G或完整收敛已认证。Ch33已有U-statistic主题，现336–338两段补对象排除/预算分账；root必要源→实际正文/邻接POST通过。

### [Trident](https://arxiv.org/abs/2603.02075v1)

必要§4–6、§8.3–8.7支持starvation/backpressure污染异步容量观测、config失配invalidate→EMA warmup、内存PoF搜索与实际单次rolling切换分开；同观测/控制预算反证、初始随机仍OOM、solver成本已读，不采速度倍数。§6.5 Eq18–19与相邻独立parallelism解释有疑点，完整MILP保证精确隔离，不补公式；不影响受限观测/控制状态命题。Ch27 Streaming前911–913两段实际补，root实际POST通过。

### [AgentSkillOS](https://arxiv.org/abs/2603.02176v1)

必要§2.1–2.2/§3/§4.1–4.2支持active catalog/dormant pool/run-selected DAG生命周期和dependency/artifact传递；选中不授execution合法性。oracle同skills仍给DAG额外Opus planner，图深度/调用预算及pairwise judge转换不同，不能称纯DAG同总预算优势或200k部署。Ch84已解析身份/competence但缺三状态，现228–230两段实际补，root实际POST通过。

七项复合日期原字段：registered UTC03/03依次00349=04:44:47、00381=04:45:30、00468=04:47:32、00680=04:52:24、01162=05:03:42、02075=05:24:40、02176=05:27:02，均arxiv.content/findable；v1 Submitted UTC依次02/27T22:28:33、02/27T23:42:37、02/28T05:04:42、02/28T14:43:02、03/01T15:56:43、03/02T17:00:22、03/02T18:46:47。Fri14EST之后、Mon14EST之前结合上述官方ID/公告/DOI规则，得到表内全落窗范围；原值与必要审阅见[本日新增记录](../_sources/daily-20260304/V3_ADDITIONAL_RESEARCH_NOTES.md)，不是Submitted单独落窗。

## 5. 缺口与下一步

普通研究信号已处置，新增十项必要源/实际Books处置及整日独立Gate均通过，普通待办0；不以脚本代替语义验收。具名负侧分层样本：00623 TraceSIR完整题摘+§3.1–3.4窄core后，TAO/长元素LLM摘要/三agent报告现有组合未提供新faithfulness或诊断保证；01960完整题摘online-softmax/tiled-KV成熟机制、cuTile编辑性与eager局部速度不改变本项目可比质量资源边界，production fused更强是反证。两项贡献前关闭、不评分。官方GPT5.3 release未披露新机制关闭；GeminiFlashLite完整Blog/card安全窄核，继承budget/Pro架构/价格宣传不成机制，grader/query变化禁止跨card安全比较，manual复核不成零风险。具体记录见[新增有限研究](../_sources/daily-20260304/V3_ADDITIONAL_RESEARCH_NOTES.md)。

早提交[00063](https://arxiv.org/abs/2603.00063v1)/[00188](https://arxiv.org/abs/2603.00188v1)/[00196](https://arxiv.org/abs/2603.00196v1)已实际完整题摘，分别有disposition-context测量、CSS/TSG GUI-KV、CVM/cloud ReMO分工潜在贡献，但公开下界不足。Submitted均早于Fri14EST，3月ID仅给可能03/02BJT09下界；原机构findable registered UTC03/03T04:38:13、04:41:05、04:41:16只给本窗上界，Updated-v1不替代first-announcement。精确请求各v1官方带时区首次公告或原项目第一次公开记录，未到不评分/计候选/Books，不写零命中。

00195真实题摘为SkillFortify，官方[Zenodo published前稿](https://zenodo.org/api/records/18787663)同标题/五机制、publication_date02/26/version1.0且[原DOI](https://api.datacite.org/dois/10.5281/zenodo.18787663) cern.zenodo/findable registered02/26T16:36:39Z。现未识别本窗重要diff，关闭本窗新家族而非贡献不相关；不把comments当abstract。当前v2官方纠正实验E3为负、soundness不等零FP，故v1零FP与泛formal安全不采，不扩其他日期研究。

GPT5.3 card精确日期终态保留：官方RSS/landing/PDF封面March3，与Hub PublishedMarch2冲突；模型版本shipped2/26不等于文章公开。已有完整core支持潜在dynamic multi-turn/message分母增量，但在必要首次归属未清前不评分/计确定候选/Books。需官方带原时区first-public记录，或能支持March3重要修订的精确版本/diff；只重开该card事件。release本窗明确，未披露机制贡献前关闭，不能反授card日期。

本窗终态保留项：Meta历史Research、Google日级pubs、DeepSeek隐藏News、Seed本窗Blog/论文、MiMoBlog、Qwen动态目录指定段尚不可恢复。它们不用于正面证据、Books或无遗漏断言。可接受官方历史目录/API或帶时区首发正文，材料到达只重开该源该段，不扩整月；不把可做日期查询变成外部受阻。

## 6. 复核

复核者：mar02_v3（接手作者前，仅root原六项题摘/日期/00356已有覆盖）；mar01_v3、mar03_v3（原五项必要源/实际POST，分批）；root（新增十项、具名负侧及最终来源/Report范围，不自验原六项）
结论：通过

机器检查：`python3 scripts/validate_research.py --report papers/2026/03/04/README.md`通过；本日正式/来源记录及授权Books范围的`git diff --check`通过。仅确认格式、可判定一致性与空白，不代替语义验收或实验复现。

分批复核覆盖全部16入选家族：原六项的未变化题摘/日期/00356具体已有覆盖及五项必要源/实际POST按上述具名非作者结果复用；新增十项的必要原文、采用边界、实际写后/邻接或NoChange由root逐项实际核通过。root最后实际读取来源/window停止范围与六部分正式判断：仅14 Daily、有界主题和相关标题补检，未把旧33/1270变成逐项队列。负侧明确实核TraceSIR/TiledAttention完整题摘及具体贡献理由，Gemini官方Blog全部core与card Safety（自动负项、grader/query变更不可跨旧卡比较、manual为厂商判断）亦通过；00195官方published前家族与v2纠错逻辑通过。GPT5.3 card及早三篇日期、历史子目录与Trident未采用公式保证分别隔离，不撑正面Evidence/Books或无遗漏。其余明确排除项只复用具名校准，未逐项全文核所有负条目或宽库存，不将抽检称全量。普通待办0，已获得整日完成结论；机器检查不代替语义验收。原文/证据与无关改动保留，未stage、commit或push。
