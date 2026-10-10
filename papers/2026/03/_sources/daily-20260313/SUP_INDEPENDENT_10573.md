# 2603.10573v1：必要Source / Ch8差额 / PRE独核

复核者：mar13_admission_review，非准备者、非Books writer。仅03-13既有Daily补Mar12 BJT自然日，当前AGENTS/研究/来源Daily与arXiv/Report/Prompt和本日停点已实际读，未变化owner/写作合同复用本日有效上下文。题摘准入与日级日期有效复用；不写共享Books/Report/LS/mainledger，不授DAY。

## 原件与实际范围

实际读 [准备包](./SUP_EVIDENCE_10573_HANDOFF.md)，回 [精确v1原响应](./SUP_HANDOFF7_SOURCE_10573.raw) / [文本](./SUP_HANDOFF7_SOURCE_10573.txt)及 [GET结果](./SUP_HANDOFF7_FETCH_RESULT.json)：`https://arxiv.org/html/2603.10573v1`，GET200，192843 bytes，2026-10-10T04:33:36.339773Z。标题 Implicit Statistical Inference in Transformers: Approximating Likelihood-Ratio Tests In-Context；[本日ABS](./SUP_ABS3_10573.raw) / [完整题摘文本](./SUP_ABS3_10573.txt)是Faris Chaudhry / Siddhant Gadkari两作者、唯一v1，Comments为workshop accepted，当前可见无撤回/纠错信号；不由acceptance推first-public或重查全会。

实际必要阅读§2/Eq1–4、§3–5/完整T1、B1–3及直接相关B4冻结QK/labels定义、C2完整T2、C3–4；raw另直接核Eq2与Eq10原数学alttext。未目视所有图、未读无关完整AppendixA证明、未运行artifact/复现或旧版比较。支持与直接反侧足够后停止。

## 受限Source通过

- 本实验每episode采样隐藏task参数φ，模型只读同task的32带标签context与query；参数在请求内固定。2-layer/4-head/dmodel128、input16、B64、20epochs、三seed是训练population。TaskA μ为单位球方向、k为随机shift，known-φ统计量μᵀ(x−k)；TaskB两随机variance、energy统计量。原oracle直接使用true μ/k/σ，不与有限context模型同信息。
- **Eq2的有限context身份不采用。** Eq2左侧是给定C的predictive odds，右侧用隐藏真实φ的LLR。按原生成过程，正确predictive需先对 `p(φ|C)` 积分两类密度，再取ratio；不是期望LLR或直接代真实φ。原非退化prior与overlapping Gaussian在有限32样本下通常留下非点质量posterior（各参数对有限样本的likelihood可为正），没有额外条件可把C当成已知φ。因此这个限定满足原有限population，不用空context反例；不否定原known-φ比较器、经验准确率或所有统计估计。NP/BCE成熟原则本身不算本篇增量，也不认证affine recovery必要充分或任意LLM最优。
- TaskB83.0±.5 vs known-φ oracle84±1、TaskA78.3±.3 vs84.6±1只限作者任务。TaskA大shift OOD accuracy64.7±4.8、LLR相关.567是外推反侧。T1 NoPos78.2±.5、FrozenQK49.6±1.3、labels-shuffle49.6±1.2不证明所有架构必须采用同learned metric；B4 FrozenQK在初始化冻结Q/K但仍训练V/O，不能说完全没有可学习attention相关计算。
- C3唯一NW对照是Eq10的 `exp(xqᵀxi)` raw dot-product加权label，ρ≈.33。只限制该固定raw-similarity解释，不排除learned/centered/adaptive kernel或任何统计学习方法。LogitLens与OV对齐的层可解码性是相关证据，§5明言非causal proof；不采用heads实际独立投票/后层唯一算法的强说明，也不从没有高线性读出推没有中间信息。
- 完整T2增加context所得75.9±4.3相较78.3±.3均值未更好，但误差范围大且不是普遍有害因果证明；label noise .1/.2/.4下70.2±11.6、53.3±5.7、49.7±1.4保留原三seed与修改训练条件。它们限制普遍最优/更长必改善，不取代经验结果。没有把accuracy/rank相关当概率校准或生产可靠性；完整硬件/时间预算、token化到真实LLM与在线SLO未披露，不能补造费用数。

## 三维与actual owner

**2+1+2=5通过**，最低standard且具体解释资格差额需必要深入。D2仅为本篇对动态mean/variance统计任务的输出/可解码深度与已知参数比较器这一具体、受限机制诊断及其信息权限边界；不将NP、BCE、通用Bayes或LogitLens名字加分。Reach1限单toy模型/二分类population；Durability2限已知oracle与finite-context、raw-kernel对照与correlational机制结论的可复用解释资格。中心Eq2强身份隔离，不以争议删候选或抹去局部实证。

实际完整顺读唯一owner [Ch8](../../../../../books/part-01-worldview/08-why-llms-show-intelligence.md) 当前73–117（前causal交接/规模→ICL→Post-training）及273–303可读表示vs必要因果hop/自检/总结，并读Ch8开篇1–23、Ch7与Ch9开篇相邻职责。现ICL段已有fixedθ/context改变、forward中估计程序、需比few-shot更强的机制证据、tangent构造与训练选取分开，但没有**真实φ oracle多看信息与finite-C predictive混淆**、只有raw-NW对照不排learned kernel、linear/energy可读深度不能授heads因果算法的具体校准。不是主题相近NC；也不将新经验值称已被原文吸收。唯一owner为 `WORLDVIEW-LLM-INTELLIGENCE`，不另占Ch14/Ch74。

插入原tangent估计程序段后、原“构造出可实现的comparator”之前，可继续比较“估计能否执行”与“证据允许解释成什么”。原局部构造、fixedθ、held-out/context与pretraining选择分责保持，不形成新论文独立收纳节。

## PRE：两处最小收紧后通过

第一段逐字PRE可原样采用：任务构造与不同读出深度、raw-kernel限定、相关非causal均符合必要原文。

第二段两处最小修改：

1. 原“较大域外shift、label noise与更长context也有反侧”改为“较大域外shift和所测label-noise条件下结果退步，增加context的所测均值也未改善”。只保所测均值/条件，不将大误差的单个context变体说成长度普遍有害。
2. 原“构造oracle、生成任务、训练、probe与干预均付费”改为“构造oracle、生成任务、训练与probe均付费；进一步确认因果机制还需额外的定点干预预算”。§5把因果干预列为future work，不能让成本句暗示本文已做内部算法因果验证；架构/标签消融仍保留，不把它们当这种确认。

第二段可采用的完整准确版本：

> 已知生成任务参数的oracle与模型只见有限context，不拥有同一信息。有限context通常留下参数posterior，正确predictive ratio需要对它积分，不能直接把隐藏真参数的likelihood ratio当作context已完全识别的Bayes规则。该实验variance任务接近更有信息的oracle，mean-shift任务仍有gap，较大域外shift和所测label-noise条件下结果退步，增加context的所测均值也未改善；没有认证任意LLM的通用统计算法。构造oracle、生成任务、训练与probe均付费；进一步确认因果机制还需额外的定点干预预算。部署仍用当前context/held-out行为验收，不把高rank correlation或低loss当作因果机制和普遍最优证书。

**必要Source / 5分 / actual owner差额通过；PRE按上述最小版本通过。** 只采用局部经验与解释资格，不签中心Eq2严格有限context identity；root窄写后仍需非writer真实新增/完整邻接/本人末注POST。本记录不授实际Book写入、formal同步或整日报完成。
