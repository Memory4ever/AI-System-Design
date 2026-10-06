# 2026-10-05 独立准入停点

窗口：[2026-10-04T09:00:00+08:00, 2026-10-05T09:00:00+08:00)。作者：oct05_daily。

官方 `cs.CL/new` 明示 Monday 5 October 2026，63 new / 50 cross-list / 72 replacement（185目录项，绝非185候选）。arXiv availability的Sunday20:00 Eastern公告换算北京10/05 08:00；首次公开仍结合当前列表分组与精确v1/history，Submitted非公开时刻。主题查询API有限20秒timeout；新列表仅作相关标题有界补检，不转成整类全文队列。LG/CV宽标题文件是线索库存，未记完整题摘或候选。

## 已读完整题摘与范围关闭

依据：cl-batch1.json前18项，dc-batch1.json前16项。此为实际阅读范围，不声称分类全量AB。

| ID | 具体准入/关闭理由 | 独立校准 |
| --- | --- | --- |
| 2610.02293 HakemBench | 关闭：土耳其typed-decision多任务与已有calibration指标组合；标签多为AI生成/非human verified、作者board非blind，并未在题摘给出能改变本项目设计的受控新机制/反证。不能把透明披露等同验证安全。 | 题摘范围关闭；代表EX抽检见正式报告 |
| 2610.02425 XiangqiBench | 准入：静态首步/重复尝试覆盖不能替代真实对手下closed-loop conversion，pass@k与pass^k人口区分。 | root实际AB通过；必要Evidence已完成 |
| 2610.02444 SymCE | 准入：反例单类SFT导致真定理probe失准；in-distribution success近似相同仍掩盖reward形状的heldout校准差。不是排除数学机制。 | root实际AB通过 |
| 2610.02455 FinDialogLens | 关闭：RFQ场景既有分类、窗口、困难路由组合，AB没有新的通用系统失效边界，特定节省数字不足。 | root实际AB通过 |
| 2610.02460 CUE | 准入：用户拟真与真实失败/成功分布校准须分开，不让persona fidelity代理benchmark validity。 | root实际AB通过 |
| 2610.02472 APDMem | 准入消歧：精确v1 §3 / §4.4实际有lazy L1/L2、按query决定精度、保持四层的w/o-controller与missing-raw对照，非仅四层组合；87.8→83.2是controller受限证据，8% session不是总token/cost节约。 | root要求单次消歧，作者已实际读并回报；必要cost反侧已读 |
| 2610.02486 SBERT2S1 | 准入：检索预训练收益依转换head而变；含自身baseline与std归一改变logit-noise gradient对CE的尺度。非医学题名排除。 | root实际AB通过 |
| 2610.02529 Arabic DPs | 关闭：AraBERT语言学candidate-conditioning应用与领域accuracy，无项目主线机制增量。 | root实际AB通过 |
| 2610.02549 Temporal Extraction | 关闭：领域时间抽取的四类泛化/提示比较，AB未给出超出标准分布切片的可长期保留机制或受控设计反证。 | 题摘范围关闭；代表EX抽检见正式报告 |
| 2610.02612 Partial Speech | 准入：commit不可撤回约束下单/多turn prefix训练与commit calibration、prefix density非单调trade-off。 | root实际完整AB通过 |
| 2610.02665 Continuous Diffusion | 准入：embedding连续扩散的scaling/steering、低NFE与distillation可行性分支，不因parity单数字。 | root实际完整AB通过 |
| 2610.02702 Silent Dissent | 准入：声明同意与residual中的未声明bridge分离，pre-registered controls及负结果；不将probe等同主观信念。 | root实际完整AB通过 |
| 2610.02713 WakeKV | 准入：heads可偶发shift，固定分类与可恢复residency要分离；CPU offload本身不新。 | root实际AB通过 |
| 2610.02736 TPBench | 准入：initial/current事实目标混在retention分数，matched deletion反证turning-point eviction。 | root实际AB通过 |
| 2610.02739 PlanPool | 准入：已识别缺失信息不等提交前处置；mutable pool要求asked/drop disposition，非SQL应用提分。 | root实际AB通过 |
| 2610.02744 EpiWorld | 关闭：epidemiological policy/science暂缓，不借world model/Agent通用节点绕回。 | root实际AB通过 |
| 2610.02769 Action Calibration | 准入：打乱action/history与破坏action-observation对应只有小降，显式outcome归属在无新信息下改善执行；learned校准额外分支需证据。 | root实际完整AB通过 |
| 2610.02770 AptMQL | 关闭：真实问题是SQL→document schema/migration与数据库访问模式，coding agent只是工具；未新增模型/Agent系统主线机制。 | 题摘范围关闭；代表EX抽检见正式报告 |
| 2610.02522 Beaver | 准入：延迟关键vRAN共租使LLM GPU共享必须联合slot-level SM与memory-bandwidth保护。 | root实际AB通过 |
| 2610.03088 Coda | 准入：逻辑ready≠最优admission，KV tier准备成本与mixed-context干扰；有界延迟避免progress starvation。 | root实际AB通过 |
| 2610.03203 AFORE | 准入：AFD独立FFNstage放大expert imbalance，利用near-future microbatch demand/迁移overlap。 | root实际AB通过 |
| 2610.03286 VenusRL | 准入：单GPU利用率与可解锁train-step的组完成相冲突；sandbox ceilings与模板COW共享。 | root实际AB通过 |
| 2610.03394 EdgeAgent | 准入：UMA CPU/GPU decode带宽竞争与agent等待/复杂drafting改变布局和调度。 | root实际AB通过 |
| 2610.03415 RailWave | 准入：固定route/placement仍有rail imbalance/incast，below-route traffic shaping分支；kernel非端到端。 | root实际AB通过 |
| 2610.03457 Cross-Facility | 准入：异构HPC队列/无共享文件系统约束需要elastic outer step、data lease与queue probes；负perplexity明确。 | root实际AB通过 |

DC其余9项仅作范围关闭：02259 feature-store非模型形成/大模型serving机制，02297日志triage通用观察系统应用，02498科学exascale任务，02658一般CUDA affine HPC迁移，02851 3DGS重建并非本项目foundation训练主线，02879 relativistic lease通用算法，03090 MIO primal heuristic，03187 guide-dog对象检测placement非foundation/VLA，03197通用machine-shape成本模型无大模型直接约束。领域或通用系统研究本身有价值，不称无学术贡献。

## 新线索题摘停点

cl-batch2.json：作者与root分别实际读18份完整题摘。15项通过具体准入校准：02772 FOVEATED（editing时teacher-forcing context掩盖later facts保持问题）、02819 Text-centric Omni（reasoning/perception训练分歧）、02877 Psychometric judges（残差难度与judge能力区别于agreement）、02886 factual poisoning（修正事实不消除decision bias）、02926 multilingual contamination（exact-match/script假阴性）、02986 OLMoDetect（datatype/OOD membership confound）、02999 OmniConfess（固定candidate的region/channel依赖诊断）、03002 Recursive UMM（external verifier提供新信息的受限自改进）、03039 HyperThink（query-conditioned可复用vector-quantized reasoning）、03052 knowledge accessibility（pre-generation测量与干预相对收益）、03102 actionable indeterminacy（admissible sets下act/clarify/repair分支）、03109 marginal attention（离线head预算和token intrinsic score）、03136 monolingual RAG（reasoning/retrieval语言交互非母语统一优越）、03190 Nautil Investigators（decision accuracy与evidence dependence可反向）、03195 source preference（matched content/source relabel causal controls）。

02856 AMD、03063 HARPO、03163 style经各一次受控消歧，均有具体局部设计/直接反侧，准入5分且仅报告；D2K由Qwen官方repo触发、current LG new与精确v1定窗，准入6分且仅报告。最终38家族冻结，不继续把宽标题库存扩为逐项队列。

## 已准入5项必要证据范围

初5必要证据已实际完成：02425补§6 simulation对照（仅各模型此前已解20/21题，Gemini下降不显著、GPT显著；restricted同时改变prompt/feedback）；02486 Appendix C/D实际核floored bounded/Lipschitz score、零和子空间Gaussian、独立draw，LOO无std无偏而同样本std不可移出期望，局部1/sigma近似与matched probe区分；global clipping不等Adam步长固定。SymCE不采用dense普劣或oracle全严格validity，CUE不采用未来失败分布/agent ranking认证，WakeKV不采用miss率=stall或少dense work全部归residency。

## 最终作者停点

38唯一家族冻结，38/38必要Evidence达到报告所采用命题：23深入/15标准，21整合/1已有覆盖WakeKV/16仅报告。名单、评分与逐项具体机制/匹配对照/反侧/未披露字段集中于[正式六部分报告](../../05/README.md)，不是另造候选分母。SymCE/APDMem只采用限定任务的reward校准/懒加载controller配方；不采普遍dense劣或最优层级，只有一般owner主题不冒称exact已覆盖。普通未读Evidence/Books待办0，无候选原源隔离。

初5、root六＋四、7DC、Oct4三项＋02665、W40三项＋HARPO/style＋末四项均按必要命题独立读原源；Partial Speech/Silent Dissent最终报告采用边界另由Oct4窄核。已整合21项实际来源marker与报告表逐项对应：02425/02460/02486/02665/02736/02739/02769/02772/02819/02877/02886/02926/02986/02999/03136/02522/03088/03203/03286/03415/03457。全部实际正文/邻接POST已通过；TP/PlanPool/Action三处独核纠偏后重验，Ch24分支置于完整TextVAE证据之后，未覆盖原binding。

当前版本/撤纠轻查：作者16项[cl-current-history.json](cl-current-history.json)、DC7 current-history、root初5和后10 current abs/history全部onlyv1，未见当前撤回/纠错标记；公开日期由Mon5new/cross＋Sunday20Eastern公告，不是Submitted。未为absence遍历旧版。Qwen Code nightly原跟读列表13064/13069/12987不生成候选；正式报告只采用实际有精确首公开依据的13064/13069(9/29公开、9/30merge)排除当前汇总的新贡献，不把第三项不明细节作为时间证明。

14源有限停点以SOURCES和正式报告为准；动态目录保留缺口但不伪0，已准入候选无普通pending。所有实验未本地复现，没有运行/核验artifact。作者交接时日级Gate尚待；root随后实际顺读最终六部分、七明确排除题摘样本、38项证据与处置、21实际写后位置及有限来源边界，2026-10-05T16:49:00+08:00授日级验收通过；最终完成态V3、引用/围栏/评分和未暂存diff-check通过。以正式报告§5保留外部精确重开条件，不授无遗漏或实验复现。无stage/commit/push，LS由root维护。
