# CRL17621：必要 Source / actual owner / 最小逐字 PRE 准备

准备者 resume_review17_18，仅本03-20补03-19自然日。原2+2+2=6/date/完整AB准入复用本日独核§12，不自授Source/PRE/safe/DAY。root分配、报告作者resume_mar17确认未读此core；交其非准备者一次必要核。只准备packet，不写Books/Report/LS/索引，无stage/commit/push。

## 1. 实际原证范围

优先[exact-v1 HTML](https://arxiv.org/html/2603.17621v1)，实际读取§2.1–2.3/Eq1–5（105–148）、§3.1–3.3（149–193）、§4.1–4.3/Table1（194–274），直接反侧A.3/B全部必要训练滞后/ActorCritic/奖励失败段（354–442），C.1–2环境与训练配置（443–504）。只上述支持范围；没有遍历references、全部图像曲线、D例子、代码或复现。当前官方abs/header/完整AB/history另实际轻量读：v2改题名/22pages14figures，AB保持同机制，未见具体纠错/安全标记；不因版本号展开全diff。

§2.3/3.3：extractor从goal/fulltrace生成m，保存其prompt-response；后续消费该m的actor终局成败给±1，唯一m关联多条trajectory时取均值，再跨collection累积到extractor训练batch。它是任务outcome代理，不是paired-without-m的因果贡献估计。actor和extractor用独立参数/独立schedule；actor K/2有经验、K/2无经验，分别在各条件内部归一advantage。Eq3 CISPO/其他B cooldown是实现选择，本文拟采用接口不授它们无偏、稳定性保证或完整recipe。零组方差保护与精确old-policy/合并后credit lineage未以本读范围闭合。

§3：episode完成不论成功失败均排队后台distill，Add/Update/Return并定期chunk-wise Merge，写锁暂阻读；读时query cache/microbatch/parallel reader，search_and_ask还会按当前state查询并调用extractor改写取回entry。保存m/embedding/generation pair有公开依据，本文的原trace/model revision/merge lineage/消费者版本共同绑定是本书验收推断，不称原系统已实现全部事务/删除/可靠provenance。抽象schedule独立不等线上无等待：§3.2 writer/read互斥、Search等待batch，A.3观察search最多约1s；ActorCritic另会阻塞主loop且不是默认。

## 2. 关键评价与直接反侧

default actor Qwen2.5-7B-Instruct、extractor Qwen3-4B-Thinking-2507，SWE single-task换Qwen3-4B-Instruct-2507。Table1三任务同mix：baseline .68/.81/.72，静态online extractor即使eval有exp仍 .41/.67/.69，无exp更低 .39/.59/.64；双训withexp .78/.87/.82、withoutexp .75/.84/.74。这支持所测条件的可分验收益，不支持静态经验普遍失败、无限共同进步或独立经验因果。§4.3把extractor4B-thinking换30B-MoE-instruct还变mode/容量，不能只归因更大；self-distillation早期好后期崩溃，不能授剥经验必内化。SWE动作增加，并非全面减少调用。

B.1早期staleness/imprecision反侧与ActorCritic每次判断额外latency保留。B.2共享参数不稳定、直接taskreward优于相对无经验组reward、五类entropy bonus未一致改善，均实际读；不采entropy降低即经验正确，也不写已经做matched因果估计。B承认严重off-policy、检索时刻不控、同entry反复更新，引出count/cooldown，不能把此工程guard当彻底消除policy lag。Fig3/5趋势仅正文说明，不读精确图数或自认视觉验收。

C训练ROLL/Megatron/vLLM、AdamW LR1e-6、无KL；embedding Qwen3-0.6B，4search/4embedding worker、batch16/maxwait1ms、extractor buffer64、merge每5updates。小WebShop catalog1000；ALFWorld1466训练/134heldout；SWE Verified先pass@16筛124任务，C明确沿训练评价，§4.1概称heldout不能冒为独立heldoutSWE泛化。multi-task384、各128/group8/128updates等只界定作者训练；硬件/precision、独立seed/CI、完整额外训练/merge/embed/存储资源及all-fee在必要段Not Disclosed。平均rollout时间接近基线不证明零额外GPU费用、尾时延或生产SLO；不采headline10%、参数共享安全、无锁等待。

## 3. actual owner / 差额 / 两侧

适用AGENTS、研究/Report/Sources/Prompt/ROADMAP及Books项目背景/学习/写作合同已本日实际重载。sole `AGENT-MEMORY`：[Ch77](../../../../books/part-07-agent/77-memory.md)，实际必要typedwrite/poison/batch admission78–155、constructor与异构read-write403–431、procedural/executor边界640–674；相邻Ch76/78入口与Ch80参数更新/heldout promotion边界已读，Ch33组内reward/GRPO职责定点读。没有按章名假差额。

现407 JitMem已有冻结executor下任务outcome训练constructor，409–411已有异构model profile/writer-reader，665–674已有derived advisory和版本/provenance；缺同一训练过程中actor持续变动、m后续消费者outcome回流训练extractor的双可变接口及有/无经验分别验收。仅此两小段拟407原JitMem段/marker后、409异构模型池前。Ch33仍own目标/importance-ratio推导，不另写GRPO算法；Ch80仍own执行反馈/反思停止，不能把参数训练叫inference-time Reflection。固定summary/frozenactor继续合理，不用新方案覆盖旧机制。

## 4. 最小逐字 PRE（未核 / 未写）

当消费经验的 actor 本身也持续训练时，冻结执行器下学会的构造策略未必继续适用。一个受限双循环分支让 extractor 从已完成轨迹产生经验并保存其生成对，再把后续使用该经验的任务 outcome 回流给 extractor；同一 entry 被多条轨迹消费时聚合它们的回报，actor 则同时学习有经验与无经验两种条件。这样改变的是经验的生成—消费—训练接口，而不是让一次任务成功认证经验的因果贡献或事实真值。原始轨迹、entry 与合并 lineage、生成器和消费者版本应共同留存；actor、任务或 bank 更新后须重验适用性，固定摘要和冻结执行器仍适合稳定负载。<!-- source-family:SF-2026-ARXIV-2603-17621 -->

共同优化也增加滞后与归因压力：生成时的经验可能到较晚阶段才被取回，同一 entry 又可反复进入训练；有经验与无经验的 rollout 应分别评价，不用混合分数证明已经内化或依赖已消除。[有限作者对照](https://arxiv.org/html/2603.17621v1#S4)中静态 online extractor 可退步，自蒸馏后期也会崩溃，因此共同更新不是单调进步保证。后台 distillation 能减轻串行等待，却仍付 extractor 训练、检索、embedding、merge 与锁等待成本；平均 rollout 时长接近基线不证明全费用或尾时延不增。质量、版本适配或预算失配时，应保留原轨迹与无该经验的基础 actor、冻结 bank 或重新核验，而不让 learned experience 取得事实或执行权限。

静态源注：`SF-2026-ARXIV-2603-17621`：[exact-v1](https://arxiv.org/html/2603.17621v1) §2–4/Table1、A.3/B/C.1–2必要段；仅双可变经验生成—消费—训练接口、后续outcome代理与分条件验收。严重off-policy、静态经验/自蒸馏反侧、SWE筛选与训练评价、锁等待和全费用限制保留；不采用因果效用、单调改进、零费用/尾时延或完整训练recipe。未核代码/复现。

待非准备者必要Source/actualowner/原两PRE裁决，准备者不自行PASS。即使PRE后获准仍须root窄授权实际写与一次非writer完整局部/静态注POST，不预支Books整合或DAY。

## 5. 非准备者必要核（resume_mar17，2026-10-11）

已独立实际读exact-v1 §2.1–3.3/Eq1–5 L105–193、§4.2–4.3/Table1 L218–274、A.3/B L354–442（405–417缺段已补实际读）、C.1–2 L443–504。生成对/后续消费者回报均值、独立参数schedule和有无经验条件内归一有真实依据；outcome不是因果效用。静态online退化、共享参数/奖励失败、自蒸馏崩、SWE筛124任务训练中评价、writer锁/search微批等待与约1s直接反侧均保留，mean rollout不授全费用或tail保证；不读代码/全proof/全部图像，不采用完整recipe。

actual Ch77 398–435和640–676完整邻接、Ch76/78入口、Ch80 27–46/340–360及Ch33 46–91职责已实际核。407冻结constructor与409异构profile之间确有双可变生成—消费—训练接口和分条件验收差额，非泛主题NC，sole AGENT-MEMORY不复制GRPO或反思算法。原两literal PRE与静态注逐字回对，额外lineage/版本留存及回退明确为本书验收要求而非原实现认证，有限Source/actualowner/PRE PASS；原6分不变。root授权前不写Books，未actualPOST不计safe或DAY。

## 6. 非writer实际POST（resume_mar17，2026-10-11）

root窄授权后writer resume_review17_18仅写原两PRE与静态注；本人作为非writer实际完整Ch77 398–433、新409/411及2185–2195末本人/相邻Sensi注读回，逐字原PRE/已核Source准确。前接冻结executor constructor、后接异构profile与query-local construction，再到consolidation，双可变接口无重复GRPO；outcome代理、版本lineage工程要求、反退/锁等待/allfee边界近文，静态注未写动态验收身份。scoped diffcheck0，局部actualPOST PASS，可由root接纳释放本family窄锁；不授全日DAY/代码核验或复现。

## 7. root授权窄写 / writer实际自读（不是POST）

root明确授resume_review17_18本family Ch77原两正文及静态源注独占窄锁。当前实际398–421两侧先读后，逐字写新409/411，静态本人2195；writer实际完整398–431与末12本人/邻注再顺读，原JitMem→双可变actor/extractor→异构profile→query-local实体接口衔接完整。原两PRE及源注未改命题，无动态过程人员注；scoped family diff已看、Ch77 diffcheck无输出exit0。只本三处增量，既有无关family不改。已交resume_mar17一次非writer实际正文/完整两侧/静态本人注POST，writer不自行授POST/safe/DAY；root锁待非writer结果。
