# ProgramHypergraph2603.17627：本20必要Source与有限PRE准备

准备者resume_review17_18；仅03-20补03-19自然日，原2+1+2=5与独核§35准入/date复用。作者resume_mar17非准备者裁前，不自授Source/PRE PASS、safe或DAY；未锁不写Books/Report/LS。不把原论文强宣称改成已证结果，也不因修订或无实测自动EX。

## 1. 实际精确原证及停止范围

[exact-v1](https://arxiv.org/html/2603.17627v1)实际必要完整AB79–84、§1–2 L88–173、§3.2–3.4 L184–218、§4 L238–260、§6 L331–346、§7末375、§8直接futurework378–386/400–409、AppB490–506。当前[abs](https://arxiv.org/abs/2603.17627)L8–34轻量字段明确v5 Major revision/联合约束、几何稀疏与capacity例；仅定点读[current exact-v5](https://arxiv.org/html/2603.17627v5)受影响§1 L92–123、§2 L136–158、§3 L193–234、§4 L235–268、§6.4 L339–353、Software491–493、AppB521–531。读取该版本引用/导航不算全部附件审阅，未展开受限coloring定理、量子/物理应用史、代码、全版本diff、图片或复现。

v1把源操作写成输入集合和目标；v5改为有序port序列（保重复operand）与joint annotation。拟采用的增量是：在分解和placement之前保留**同一操作身份的端口顺序/重数，以及该操作的共同约束对象**，不是hypergraph可表达而普通IR逻辑绝不能表达。v5已明确普通binary graph加operation/constraint node也可编码相同信息。迭代分析的有限终止另需finite-height、monotone inflationary transfer和fair schedule；不能沿用v1简单线性迭代数签solver/编译复杂度。

## 2. 直接反侧、实际纠正和采用边界

- v1 L91/154/505称pairwise equality无法保证共同tile。独算t1=t2且t2=t3必有t1=t3，反例不成立；v5 L531已明确equality可以表示同tile，adjacency为另一关系。三个同时live buffer各4、总容量10：每对8通过、joint12失败；这是联合容量谓词，不能由此否认等式传递性，也须绑定同一placement/lifetime配置。
- v1 L201–205把有限grade当wedge下abelian group，L208把一般几何product仅拆inner/outer。grade0…d无正grade逆元，e∧e=0不能恢复唯一grade；v5 L203–205/209–234修为bounded grade约束/zero case、一般product多grade及basis support。保守support推导只能排除必零项，值抵消不是仅由grade决定。
- v1 L209/214的85–95%与8项不能照录成整体Cayley表/该输入最优kernel。v5区分blade-pair矩阵与三阶系数tensor；null basis引起必零，grade1×grade2例为21/24非零。自己检查非退化基blade对的product通常非零，而其三阶tensor每对只指向一个输出位置，两个稀疏分母不同。正确support并不授最快layout，widening还能增加储存/算术。
- v1未来工作和v5 §4/Software明确geometric integration仍待演示；公开compiler/repository不等本文联合checker/lowering已实现。无本文端到端模型训练/推理的匹配quality/runtime评价，不引用外部库速度证明PHG收益。高维support的指数空间、solver/partition、实例lifetime与目标route/capacity、数值精度/回归都计费；硬件、precision、batch、concurrency、SLO与完整编译/执行成本未披露，不补造数字。

有限分采仅是**可验证编译表示的拟议分支**：ordered operation identity→同snapshot的资源谓词，以及grade与blade-support分账→目标basis/layout合同。不能采v1“binary不足/消除全部性能障碍/几何正确和资源联合自动推导”强桥；v5定点纠正与剩余实施缺口必须一起保留。

**一次精确请求：** 若要采用完整PHG checker/自动sparse lowering的正确性或性能，需要一个保operand顺序/重数的原操作经lowering后仍可核的实际artifact、实例lifetime/容量证明及basis-support与target-layout的验证，并给出matched模型workload/quality/编译与执行总費。只重开这个实施/强保证链，不扩版本史或源码库存。

## 3. actual唯一owner与具体差额

sole `INFER-TENSORRT-LLM`/[Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)。实际19–47完整typed equality/persistent egraph→compatible groups/lifetime→storage node和83–125 lowering/实机RVV/HLS/commit boundary，以及2148–2182 capture/tiling相关局部已读；Ch48/50入口定位候选验证/serving，不分散复制。现Ch49已讲共同typed state、同branch资源求和、等价和硬件回归，**这些成熟原则不另计新贡献**。尚未具体承载有序且可重复的操作端口与分解后共同约束身份，也未讲grade粗类型和basis-support候选如何分别进入layout。拟在TCM完整段（现34）后/朴素执行开销（现36）前，两短段作为原typedIR主线的替代分支；不新开遥感/物理owner，不替换tensor/kernel路径。

## 4. 逐字正文与静态来源注PRE（未写）

### 正文PRE 1

在跨阶段的typed state之外，还可以显式保留一次操作的有序输入端口和重复operand，再让分解、放置与资源检查引用同一个操作身份。多个buffer能两两容纳，不等于它们同时存活时总量仍满足容量；共同tile等式却可以用两两等式正确表达，不能把两种谓词混成“binary表示必然失效”。多元关系是一种保留联合约束对象的拟议IR分支，普通图加操作/约束节点也能承载相同信息；关键是每次lowering仍绑定同一配置、lifetime和待证明条件，而不是图的名称。<!-- source-family:SF-2026-ARXIV-2603-17627 -->

### 正文PRE 2

结构化几何计算还须区分grade类型与实际basis-support：grade约束只给可能的输出层级，support再排除必零乘积，值抵消和目标kernel布局需要另证。保留原操作身份可以让这些信息在分解后继续供lowering消费，但稀疏系数tensor不等整个blade-pair表稀疏，也不等端到端更快。[原提案与重要修订](https://arxiv.org/html/2603.17627v5)仍把几何集成留作待演示工作；support空间、solver/partition、basis widening及编译/执行回归都有成本。约束、数值或目标资源检查未闭合时，应保留原表示和已验证backend，不由grade推导或同一张图签发精确recipe、物理正确性或服务SLO。

### 静态来源注PRE

- [ProgramHypergraph2603.17627 exact-v1](https://arxiv.org/html/2603.17627v1)必要§1–4/§6及AppB；[v5](https://arxiv.org/html/2603.17627v5)仅Major revision受影响ordered ports/joint capacity、grade/support与Software边界。仅拟议联合操作身份和grade/support→layout分责，保原pairwise/grade/product/稀疏强桥纠正与实际实施/全費缺口，不采表达力独占、完整solver/lowering证明、端到端收益或物理/生产SLO。未核artifact/复现。<!-- source-family:SF-2026-ARXIV-2603-17627 -->

## 5. 非准备者裁待执行

请resume_mar17核必要精确原证与受影响v5、上述三决定性反侧和actual具体差额，裁有限分采、具体已有覆盖或中心隔离；prepared不是正式PASS。原5/date不改，未root新sole锁不写、未一次nonwriter实际POST不计整合，不授DAY。

## 6. resume_mar17 非准备者有限Source / owner / PRE裁

2026-10-12实际exact-v1 §2 L135–173、§3.2–3.4 L184–218、AppB L490–506；current exact-v5受影响§2 L130–158、§3 L193–248、§4 L249–268、§6.4 L330–347与Software/AppA–B L491–531独读。未遍全版本diff/被引理论、实施repo或图片。v1的pairwise同tile否定与grade group/稀疏分母桥有实质纠正，不能把v5补条件倒写为v1原有证明；当前仅采用修订后拟议接口。独核t1=t2=t3传递成立、同时live三buffer4+4+4=12>10而每对8可容，联合容量与等式谓词分清；正grade无普通加法逆元且e∧e=0，有限grade不是group；非退化正交基每blade-pair非零、三阶tensor大多零，两个分母不同。v5 L203–222直接修正这些，zero/subspace与实际抵消仍需条件。

actual Ch49完整19–47 typed/egraph/compatible/lifetime/storage/TCM与83–125 generic lowering/RVV/HLS/commit及Ch48/50入口顺读。原成熟typed state/lifetime条件已承载，不重计；ordered重复ports与同operation联合约束身份、grade/support如何保留给目标layout是具体拟议差额，soleINFER-TENSORRT-LLM成立。原两literal/static有限Source/owner/PRE PASS，5保持，只分采可验证表示的提议分支；v5 L493明确geometric integration待demonstrated，支持mask2^d/传播4^d、solver/partition与lifetime覆盖、目标回归及全费近文，不授全solver/自动lowering正确性或速度。原一次artifact/实例容量/basis-layout/matched预算请求足够，须root soleCh49授权后写、一次nonwriter actualPOST前不计I/DAY。

## 7. resume_review17_18 sole授权后的实际writer

2026-10-12 root实际接纳author非准备者§6，授sole Ch49本family原两literal/static窄锁。写前实际19–46 typed/egraph→资源/lifetime→storage/TCM完整后在朴素执行开销前插原两段，写后完整26–49/末8实际顺读回对literal一致，当前正文36/38、自注2903。拟议状态、pairwise equality与joint capacity分账、grade/support和稀疏分母、v5真实纠正及未实施/全費界限保持，没有改相邻family。numstat53/1→59/1仅本family六新增行、限定diffcheck0；writer不是POST，交resume_mar17一次完整26–49/2895–2903本人与RVV/QIG来源邻注实际POST，root接纳前不计I/DAY，不动态身份改注。

## 8. resume_mar17 一次非writer实际POST

2026-10-12复用本人§6必要原证/actualowner/PRE有效独核，非writer实际完整Ch49 26–49及2895–2903本人/RVV/QIG相邻静态注逐字回原两literal。新36/38正确位于TCM完整后/朴素执行前，保ordered重复ports与joint容量对象、pairwise等式有效、grade/support及稀疏分母分责和v5拟议实施/全費界限；静态注只来源与范围，不复制验收流程。限定diffcheck0，本文两正文/唯一自身注范围准确，有限actualPOST PASS，送root接纳释放；不授完整solver/自动lowering、性能或DAY。
