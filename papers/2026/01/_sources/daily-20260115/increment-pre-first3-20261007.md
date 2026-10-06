# 首3必要证据与actual owner PRE提案

作者supp_jan15；原52不变。08778实际原源/owner NoChange—Existing PRE已由root通过。08343 Ch45正文979及自身末注已写入，root实际967–991完整邻接/末注POST通过并释放窄锁；条件措辞已落实，不授整日完成。08815首次公开/重要增量隔离，不评分或写Books。首7准入root通过；arXiv BJTJan14的下界为正常Jan13<19Z提交不可早于Jan14公告、上界为正式ID/DOI registered Jan14T02:47–03Z，root已核官方ID赋予规则并通过该有限推断，非把Submitted或registered单独当首次公开。更早项目正文信号仍轻量查。

## 2601.08815v1 Agent Contracts — 首次公开/重要增量未建立；不评分、不入确定候选

后续root实际核窗前exactSHA完整whitepaper必要部分，支持同采用机制更早文本信号；Git commit时间不能单独证明当时public，不自定Dec21公开。下述审阅继续保留为恢复材料，原2+2+2只是尚未日期完成的提案，撤回确定评分；不写Ch84，不搬2025或Jan10。只在确立本窗实际重要事件增量时重开。

原源exact-v1 §4.1–4.3、§5、§6.1、§7.1–7.3、§8.2–8.4已读；[原件1](./increment-core-first3-release-20261007.txt)、[原件2](./increment-core-first3-eval-20261007.txt)、[原件3](./increment-core-first7-part2-20261007.txt)、[原件4](./increment-core-first3-owner-20261007.txt)。采用的局部机制：把任务成功条件、资源预算和停止条件分别表达；子委派分配总和受父预算约束，完成后未用额度回池，协调reserve另外计费。不是七元组命名本身或成熟守恒原则的突破。

必要反侧：§7明确只在API返回后知道实际usage，不能阻止一次昂贵调用超额，只能阻止后续调用。§8.3案例40K预算实际56K后停止，所谓50次零conservation violations是allocation检查不是实际消费硬界；§8.2 CONTRACTED还同时缩max iterations6→3并增加budget prompts，90%节省不归因为纯contract机制；成功60→52.9、p=.13不是等价证明。§4.3成功guard没包含资源条件，<=约束与>=停止等号冲突；不采形式唯一终态、普遍硬上限或生产安全。代码未运行，precision/hardware/concurrency/SLO未披露。

actual owner AGENT-PLATFORM Ch84 §Agent Runtime State Machine（553–573）、§Scheduling不只是GPU（598–607）、definition/run身份（102–132）已读：已有budget字段、资源域和terminal evidence，但未实际表达delegated allocation/reserve/usage reconciliation，以及预算分配合法与调用后超额不同。拟仅在Scheduling标题后新增两段，不复制生命周期表：allocation/proposal→provider admission→usage receipt→reconcile；硬上限需要reserve/cancel/provider限制，失配停后续或人工。这是原机制的限定工程推论，不宣称论文已经实现预留的原子多agent消费。待root核gap；若实际其他正文已承载则NoChange。

原论文唯一直接项目链接GitHub flyersworder/agent-contracts当前目录已读；API repo created2025-10-29，只表明更早artifact而不单独证明论文正文更早。正在定点查窗口前最后commit是否有完整论文/同一正文，更早正文未排除前不写Books。

## 2601.08778v1 Pervasive Annotation Errors — 3+1+2=6，纠错深入；拟已有覆盖

exact-v1 §3.1–3.2/§4.1–4.3/§5.1–5.5已实际读，必要[原源](./increment-core-first7-part2-20261007.txt)。100随机BIRD Dev子集（62/28/10难度），修48例，同时修改question19、knowledge17、goldSQL41、schema1、db6（重叠）；16公开可复现agent按Aug20'25选择，在两个版本重跑而非纯固定生成复判。CHESS62→81、CodeS56→52，ranking±9只在该小子集联合修订下；无逐模型区间/重复seed或总体外推。EX只测单fixture结果，不保证SQL语义等价；SAPAR辅助，人类复评/冲突共识不是客观gold认证。不采全leaderboard失效、普遍error率或agent真值。

actual owner PLATFORM-EVALUATION-SYSTEM Ch66：345–347已有qrel身份/label agreement与ranking稳定性分开；396–400已有run身份贯穿annotation/evidence revision，不能沿旧排名；504–506已有repair联合改变difficulty/构念、保存原题/新revision/逐轴复验、排名不能纯归因修复；1373–1377与789已有SQL fixture/duplicate semantics与expert标签双向不一致。新研究在这些边界提供局部验证，拟NoChange—Existing，报告保留100例联合修订及人审限制，不新增BIRD数据段落。仍需轻量原项目更早正文日期信号。

## 2601.08343v1 When KV Cache Reuse Fails — 3+2+2=7，深入；拟Ch45窄差额

exact-v1 §3–4、§5.1–5.3、§6.1–6.2 Table1/2、§7与Limitations已读。固定N4候选，execution侧dense，same texts/permutation，只改变judgeKV；naive是RoPE重定位+stitch，KVCOMM用5anchors/agent修offset并可fallback，PAL-KV只pool anchors。Llama3.2-3B主实验，3–14B消融；temp execution .2、judge0。MMLU dense masking局部accuracy近45%，JCR仅28.76/32.03，显示answer correct与selected candidate identity不同对象；不是JCR低就证明准确率/公平更差。首tokenattention是diagnostic，mask介入支持cross-candidate条件影响但不证明唯一因果。Reuse Rate排除prefix/output，不是latency；hardware/precision/batch/concurrency/SLO未披露，无全链速度/生产安全结论。§7所谓universally-safe classifier使用correctness signal可能oracle，不作为线上gate已实现。

actual owner INFER-KV-CACHE Ch45 954–978已有exact dependency identity、conditioning seam与role-flip warmup对照，非所有accuracy证明near-exact；但未保存joint judge selection相对于matched dense的独立不变性对象。拟紧接976 role-flip段后追加一小段：缓存验收除final answer还绑定selection/attribution与候选顺序；fixed candidate/permutation dense reference，dense是行为参照非gold；质量预算/修复无法验证则重算。新物理机制没有，差额是近似状态consumer合同与局部反证，不占Ch66重复owner。待root实际源/ownerPRE，未写入。
