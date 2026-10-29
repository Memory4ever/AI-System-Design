# GeCO 2603.17834 — sole 必要证据 / actual owner / 最小 PRE 准备

准备者resume_review17_18，2026-10-12，仅03-20补03-19自然日。author明确sole本family必要准备、自己未读core；保持原2+2+2=6与本日[独核§30准入/date](./SUP_INDEPENDENT_REVIEW_20261011.md)。不扩query/其它日期/代码/全部附录，不自授Source/PRE PASS、safe或DAY；未写Books/Report/LS。

## 1. 实际必要原证与停止

[exact-v1 HTML](https://arxiv.org/html/2603.17834v1)：实际§3.1–3.5/Eq1–7/Alg1（L127–224），§4.1–4.5/Tables1–7（226–348），§5直接限制（346–348）；支持训练/停止/诊断分责所需A.2–A.4（420–485）、C对应VLA训练人口（514–525）、D（527–562）与E必要硬件/控制/训练/推理/验收（563–589）已读。F最后NFE解释594–595仅作与Table7的数字口径反侧，不采视频/因果解释；没逐图视觉检验、没读可选代码或复现、没读全部related work/references和其他附录库存。

[current abs](https://arxiv.org/abs/2603.17834) L8–29实际题摘/comments/history：同题六作者，v2 revised04/26，Comments18pages6figures，无具体撤回/勘误说明；v2存在本身不触发全diff。原v1事件/date夹证有效，不按current Updated重排03/19归属。恢复时AGENTS/current合同、Prompt/Sources适用频率/ROADMAP与本日README窗口/STOP已实际重读或同一未变范围复用，不继承他日。

## 2. 必要机制、关键评价与直接反侧

### 拟采用的真实接口

§3/Eq1–3：示教action sequence a与Gaussian ε插值xγ=γa+(1−γ)ε，γ仍采样用于训练数据与rescaling target，但**不输入模型**。目标g*=(ε−a)c(γ)，c趋末端为零；模型回归一个依赖当前observation/语言条件s、动作状态x的stationary field。这是改变训练对象/目标，不是部署时随意删掉一个已经训练好的time embedding。§4.2 π0继承权重、fine-tuning时time input固定0，仍按新target再训练；保VLM与输入输出interface，不授整个VLM参数冻结或无训练代价。

§3.3/Eq4–5/Alg1：noise初始化，对同一s反复a←a−ηf(a,s)，norm阈值或Kmax结束，输出action proposal。A.3 GD步长schedule/Kmax与norm stopper说明实际局部停止消费。有限多步同一field不等证明gradient是某个全局potential、总步长任意均稳定、示教点全稳定或收敛正确动作；§5明确理论收敛/OOD边界仍待加强。Alg1预算结束返回a^(k)而§4.3/D讨论最后a_K索引不完全同式，故不授逐索引精确recipe。

§3.4/4.3/D：最后field norm另作anomaly score，并对单次planning call内refinement残差moving average/leaky bucket过滤；阈值触发可终止episode，但不是独立物理安全验证。无auxiliary network不等无校准/无成本。停止阈值与OOD阈值语义不同，不能由收敛自签safe/在分布内。

### 非正面采用与具体反证

- 端点c(1)=0是target设计，不推出learned MSE field处处有正确稳定吸引子或conservative gradient。独立分析：若同一s的示教为对称±1、noise对称，则x=0条件下两侧目标对称抵消，最小MSE的f(0,s)=0也可发生在非示教动作。这里只反证“零norm必然示教/安全”的推论，不声称实际模型一定如此或整篇机制错误。OOD观测上的field更没被训练分布约束。
- T1预算20的avgNFE11.6 vs固定20、5步mean91.9 vs90.0支持有限预算/质量取舍，不是75%完整compute或wallclock提速；30步平均93.1低于20步93.5。T2 Blocks Ranking仍0，Easy Adjust Bottle90→86、Click Bell44→42；T4 π0 avg94.2→93.9、π0.5 96.9→95.9，不能称所有backbone/任务无损更好。
- §4.2同pretrained π0/30k steps局部匹配，但C各suite batch32/256不同，不能把所有baseline/scaffold训练和部署条件合为一人口。主干条件encoder/DiT architecture及A的observation horizon1/action horizon16/num_act_exec8披露，不能把生成chunk长度等同每次执行长度；模拟推理GPU/precision/batch/concurrency/SLO、完整训练/搜索/校准/端到端wallclock费用Not Disclosed，NFE不是全部FLOPs/TTFT或实际fresh-observation频率。
- §4.4 T6称α控制decay-onset，扫描.6/.8/.9；A.4 Eq8却用a0=.1与λ4定义截断线性schedule。参数映射/具体实验支持未闭合，故不采最佳α或全recipe，保“target靠末端衰减”这项可核结构。
- OOD：Goal10tasks训练→Spatial10tasks suite shift，500ID＋500OOD episodes，每episode随机20planning calls，不是碰撞/失败/未知危险标签，也不是10k独立episode。T5 AUROC .93有限suite分离；operating point按OOD样本接近90%TPR选阈值，独立heldout校准人口未披露，不能授未见shift检测或生产风险率。baseline是固定t的single-sample flow-loss proxy，不是完整Diff-DAgger ensemble。TimeSaved只OOD episode在300env-step horizon提前终止的剩余比例，非模型wallclock或成功任务加速；停止可误报/漏报。
- E真实Galaxea R1 Lite/3views/proprio/15Hz控制、action chunk16，G0Plus初始权重、4epochs/batch32/AdamW；推理cap10/empiricalnorm1.5与模拟stopper.4不可混。两task各10trials T7 10→70/20→80与avgNFE只有限作者结果，不授独立物理safety/每新观测deadline；F Nut平均6.45与T7 6.2不同，不照录严格数值因果。碰撞控制仍归独立controller；GPU/运行precision/模型尾latency/复现未核。

必要强主张重开条件：同状态/任务与校准分割下报告norm相对真实失败/碰撞的独立检测与误报漏报、部署fullwallclock/完整代价；理论需给field integrability/局部稳定假设和多模态非示教零点处理；recipe需明a0/α与最大步结束返回索引。当前有限训练/停止接口不依赖这些headline闭合，不为省审改EX或整篇center。

## 3. actual 唯一 owner 与相邻差额

ROADMAP唯一`MULTIMODAL-EMBODIED-VLA`，[actual Ch26](../../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md)。已实际完整读239–251 fixed-point field的residual threshold/cap/warmstart/latency与velocity-vs-cleanendpoint两侧；1318独立safe-set/controller commit段、章首问题也已读。Ch24章首generativefactorization/commit与Ch25章首observed-vs-imagined state交接实际读，只有相关接口，不重复两章理论或world-model库存。

现Ch26 task-conditioned fixed-point与假收敛/尾延迟已有强具体覆盖，不写一般“自适应更好”。缺口是**训练γ隐藏却仍控制near-endpoint恢复target**，以及**同一fieldnorm在停止修正与suite异常评分上是两个不同验收接口**。因此拟两短段紧邻当前fixed-point binding完整end（L244）之后、velocity/cleanendpoint前。author ProbeFlow另同区域准备，root须协调sole锁/排序，写前重新读实际相邻；这里只拟稿不先占共享写锁。

## 4. 两最小 literal PRE 与静态注（待非准备者裁）

这个自适应循环也可以从flow训练目标构造，而不只给固定步decoder增加停止器：训练仍采样生成进度，把示教action与noise插值，但不将进度输入head；恢复target沿noise减示教action的方向，并在接近示教端点时衰减，使同一observation条件下反复读取一个时间无条件field。[GeCO的受限分支](https://arxiv.org/html/2603.17834v1#S3)再用field norm阈值与最大迭代预算控制action修正，π0适配时固定time input并按新目标finetune，不是免费移除旧time条件。端点target为零不证明学习到处处正确稳定的势能：多模态目标可抵消，低残差仍可能是假收敛，最终动作继续由真实环境与独立controller验收。<!-- source-family:SF-2026-ARXIV-2603-17834 -->

同一残差还可以提出异常检查，但必须与停止计算分开定标：修正结束的field norm在受测Goal→Spatial任务组变化中用作planning-call score，过滤持续较大残差后可提前结束episode；这只是有限分布变化代理，不是物理危险、动作可行性或epistemic uncertainty的证明。检测阈值、按episode抽样人口和baseline proxy决定结论，停止剩余环境步骤也不等于模型墙钟提速。更多修正仍可能退步，VLA任务有反退；条件编码、训练、阈值搜索和重复求解须计完整成本，NFE与15Hz控制声明不能替fresh-observation deadline。残差失配、预算耗尽或物理风险时，保留固定多步flow、短horizon重观测和独立安全包络，而非让生成head自行授权执行。<!-- source-family:SF-2026-ARXIV-2603-17834 -->

拟静态注：GeCO [exact-v1](https://arxiv.org/html/2603.17834v1) §3/Eq1–7/Alg1、§4/T1–7/§5、A2–4/C/D/E必要支持与直接反侧。只采隐藏γ的恢复target与stationary residual-stop/诊断分责；不授全局potential/稳定收敛、零norm安全、未知shift或fresh-deadline/低完整费用。α/a0与最后返回索引recipe隔离，AUROC操作点与NFE/实机小trial边界保留；未核代码/复现。

交resume_mar17 nonpreparer必要Source/actualowner/两literalPRE；准备者不自授任何PASS或最终Books处置，不写前等root具体窄锁。

## 5. 非准备者必要 Source / actual owner / literal PRE 裁定

2026-10-12 resume_mar17实际独读exact-v1 §3/Eq1–7/Alg1、§4/T1–7与§5，A2–4的encoder/target/stop设置、C训练人口、D规划调用与操作点、E真实硬件/训练/推理/十trial及F末NFE文字反侧；current abs只title/Comments/history轻量。actual Ch26完整235–275（含已有效ProbeFlow两段）与1305–1330的独立safe-set/controller交接已读；未读代码、全部图或旧修订库存，未复现。

有限Source/sole具体差额/原两literal PRE与static PASS，保2+2+2=6。Eq1–3确实隐藏γ而仍由γ构造插值和衰减target；Eq4–5与Alg1只使用stationary field norm/预算停止，另Eq6–7及D把最后norm用于受测suite异常population。两分责不是一般fixed-point知识的重抄；原Ch26虽已承载residual/cap/warmstart，未承载该隐藏γ训练消费和停止/诊断分别定标。±1同条件示教/对称noise的x=0恢复target对消可成立，故零norm不认证示教或安全；这不否定受限训练与停止接口，也不授全局gradient potential或稳定正确强桥。

原两PRE近文保留LIBERO/VLA退步、未知shift与独立controller、NFE/15Hz非fresh deadline及全部费用。T6 α与A4 a0/λ、Alg1结束返回索引、检验操作点与独立校准分割不闭合均未当配方采纳。支持与直接反侧足够即停；可按本有限PRE整合，不改NC/EX或整篇center。Books尚未授权/未写/未POST，不计safe/DAY。位置须root协调：ProbeFlow已246/248，GeCO应保持自己的fixed-point邻接而不插入semantic binding内部。

## 6. root窄授权后的实际writer落实（不是POST）

root接纳author §5后授resume_review17_18 sole Ch26此family两literal/static锁。writer实际读现235–270邻接、24/25已核交接、章末本人/Probe邻注，并重读PROJECT_CONTEXT/LEARNING_PHILOSOPHY/WRITING_GUIDE，ROADMAP与当前LS相关路由有效。按原两literal实际插入fixed-point完整end之后、已核ProbeFlow之前，new246/248；static章末2282。没有改变ProbeFlow或旧binding、没有写Report/LS。

writer实际完整237–267及末尾2275–2282顺读回原两PRE/static一致；仅本family两正文+static六新增行，scoped diffcheck0。反退/检测population、训练费用与独立controller边界近文保持，static仅源与边界，无验收人员流程。交author一次实际nonwriter POST（建议235–279/2273–2282）；不能用这条writer读回当POST或safe/DAY，root锁保留到author真实回执。

## 7. 一次非writer实际 POST

resume_mar17 2026-10-12实际顺读Ch26完整235–279、新246/248与2273–2282静态本人/ProbeFlow及其他邻注，逐字回本packet §4两literal/static，并复用本人已实际必要Source/owner §5。有限actualPOST PASS：原fixed-point semantic binding完整结束→隐藏γ恢复target/norm-stop与独立suite诊断→训练外ProbeFlow→clean endpoint参数化链衔接自然；±1抵消、质量反退、人口/费用/15Hz非fresh deadline及controller仍近文。ProbeFlow仅行位变化，旧内容未改；静态注准确不加验收身份。限定diffcheck0。结果交root接纳/释放窄锁，不授整日DAY或全局稳定安全强桥。
