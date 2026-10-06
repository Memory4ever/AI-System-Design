# AIMER18492：必要 Source / actual sole owner / 最小 PRE

resume_mar18准备，仅03-21补BJT03/20；本日完整v1AB/官方日级夹证准入有效复用，无具体先稿/纠错信号，不遍旧revision或venue。拟2+1+2=5：新增单MoE组件内的weight-only expert-ranking→永久裁结构接口，不给成熟pruning/常驻容量或模型数跨系统分。必要差额深入；未独核/锁/写/safe/DAY。

## 必要 exact-v1 / 关键反侧

[HTML](https://arxiv.org/html/2603.18492v1) §3–5.3/Eqs3–7/Alg1/Tables1–4及§7实际读，支持与反侧够即停。不采用全部附录图证明或完整16bench细表已核的说法；未核代码/复现/后v3。

- Uniform layer-wise裁25%/50% experts，expert三投影gate/up/down拼成w，score=|w|1/(sqrt(N)|w|2)，**高score先剪**，并删相应router rows；保留原topk而不是降低每tokenactive expert数。Alg1降序与文字一致，不反转importance名。非zero w下scale-invariant/bounded[1/sqrtN,1]的代数正确，等abs值取1、一个非zero取下界；但只是一阶/二阶权重形状统计，不推出功能冗余、router数据分布或语义贡献。
- 我方限定推断：统一expert所有weights乘常数不变score，不等保持原非线性FFN函数；独立up/down重标度等参数化变化也可能改score而维持相同输出。原§7承认效力是empirical非理论保证，因此不把ratio界当lossbound/任意任务普遍正确，不需将受限接口硬判中心错误。
- 三模型OLMoE1B-7B0125、ERNIE21B-A3B-PT、Qwen3-30B-A3B2507。四数据依赖baseline统一C4 4.2Mtokens；random seed42，magnitude按最低meanabs剪；calibration corpus/size敏感是有偏profile风险，但“irreducible bias/全taskagnostic”不由单C4size图证明。均zero-shot，无postprune恢复训练；层uniform删除不是全局最优分配。
- Table2 OLMoE25% AIMER codeavg.013<random.056、Wild.236<REAP.260<full.444，math.139<full.452；“overallstrong”不掩个别失败。ERNIE25% Wild.402<REAP.405、MC.681<EAN.687，code.455<full.557、math.761<full.804；50%质量进一步损伤。ERNIE正文“29.7%提升”是45.5−15.8=29.7points而非29.7% relative，不照百分数宣传。
- Table3 Qwen25% math.826<REAP.852<full.862、MC.723<EAN.736<full.737；50%code.361虽高于REAP.046却低于full.619，math.579<REAP.849；创作.413<EAN.522<full.644。High ratio不保存所有能力，单平均不能签“taskagnostic无损”。
- 2×L40S48GB；greedy do_sampleFalse/temp0；LCB182 Jan–Apr2025、Wild146prompts/GPT-OSS120B judge、EvalScope math/lmeval MC，model/pubtask人口有限；precision/完整输入输出长度、batch并发、repeatCI、wall服务latency/SLO ND。自然用户/更大百B MoE及任务特化未验，原§7说任务特化仍需要calibration/adaptivesignal。
- Table4 .22–1.27s只是**expert scoring stage**，不含载入/结构改写、artifact保存、完整任务验收或服务成本；.75–2.96h REAP是同stage参考。加载memory before/after只是固定删除比的容量，所有方法同after，OLMoE性能只25%而memorycaption50%不能拼成一份sameconfigfrontier。保原topk不授activecompute同比减/端到端加速。用weight data不用calibration data不等没有原训练数据依赖或后续heldout验收费用。

## Actual sole owner / 最小差额

`MODEL-MOE` Ch21实际606–649（层预算/counterfactual/离线贡献prior/Posttraining skip）、704–721（更新域/长尾低频≠无知识），Ch20/22开篇实际读取。已有校准移除loss→当前router融合，未覆盖**不读input/activation/router统计而把三投影静态ratio作为同层expert永久删除提案**；不是routing少调用，也不是genericCh49稀疏kernel配方。不假NC，soleCh21拟当前626离线prior marker后、628 Post-training标题前一段＋本人静态注。

## 一段逐字 PRE

如果目标不只是让当前 token 少调用，而是发布一个常驻 expert 更少的 checkpoint，排序提案也可以完全来自权重：把每个 expert 的 gate、up、down 三份投影拼成同一向量，以绝对均值与 RMS 的比值在同层排序，按固定比例删除较高比值的 experts 及相应 router rows，并在剩余集合中继续原 top-k。这个比例刻画权重分布形状，不是功能冗余或知识重要度；尺度不变与数值范围有限，也不证明剪除后的损失受控。它把校准输入和 activation 采集成本换成静态 proxy 偏差及完整产物验收，[受限 MoE 对照](https://arxiv.org/html/2603.18492v1)中更强平均表现仍伴编码、数学或其他任务反退。少存 experts 不等每 token 调用数同比减少，排序秒数也不含加载、改写、质量检查和 serving 的全部费用。裁后 expert 列表、router 坐标与 checkpoint 必须共同发布；任务专化、proxy 失配或质量失败时，保留输入相关校准、较保守裁剪与完整原 experts，不能由无需校准数据推出无需回归证据。<!-- source-family:SF-2026-ARXIV-2603-18492 -->

## 静态注 PRE

- `SF-2026-ARXIV-2603-18492` — [AIMER exact-v1](https://arxiv.org/html/2603.18492v1) §3–5/7、Alg1/Eqs3–7/Tables1–4；只采用三投影绝对均值/RMS的weight-only同层排序→删expert/router rows→保原top-k的条件分支。高ratio先删、代数界非质量界、random/任务/高裁比反侧、points与percent、scoring/loading/服务费用分账保留；不授功能冗余真值、全taskagnostic无损或端到端加速，未核代码/复现。

## root 非准备者有限 Source / actual owner / PRE 通过

实际exact-v1 §4.1–4.2/Alg1/Eqs3–7、§5.1–5.3/Tables2–4、§7，actualCh21完整606–645与704–724及Ch20/22交接、原一PRE与本人静态注回对。高ratio先删与保原top-k、weight-only排序而非功能importance的区别准确；代数界只对非zero权重，不能证明删后loss界。Table2 OLMoE .013 codeavg低于random .056，Table3 Qwen math .826<.852/50% .579<.849及Table4只scoring stage/50%加载均实际独核，原PRE成本与质量反侧充分。soleCh21产物裁结构的新接口成立，2+1+2=5不变；有限Source/PRE PASS，可授一段正文/本人注窄锁，未actualPOST/未safe或DAY。无需重读不采用的全部附录图，不因通用剪枝已有便fakeNC。

## 作者实际窄写（待 root 一次非writer POST）

按root本family唯一Ch21锁逐字写原PRE新628和本人静态注1060。作者实际完整612–645、末五行本人/邻注回读：offline贡献prior→weight-only永久裁结构→保旧experts的zero-path分支衔接完整，body/static各一、scoped diffcheck空。原PRE未扩能力/公式/全部费用承诺；尚不计safe或DAY，发送root一次实际POST后释放。

## root 实际非 writer 写后复核

实际顺读 Ch21 完整612–645（包含新628）与末五行本人源注，逐字回对已通过的原 PRE 和必要 Source：输入相关离线 prior → 权重形状提出永久结构裁剪 → 保留旧 experts 的可跳路径，三个对象未混同。高 ratio 先删、保原 top-k、任务反退、全部产物/服务费用与原方案退路均在近文；正文和自身静态注各唯一，限定 diff 检查空。actualPOST 通过，释放本 family Ch21 窄锁，可同步整合；不授整日 DAY。
