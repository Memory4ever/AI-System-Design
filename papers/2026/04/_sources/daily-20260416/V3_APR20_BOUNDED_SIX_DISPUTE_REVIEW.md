# Apr16 六项争议有限非作者终核

复核者：`/root/apr20_resume`；2026-09-27T18:12:33+08:00。报告作者当前为apr02，本复核者未参与该日报创作或Books写入。受root明确委派，只核13088/13523/13546/13634/13991/14017的README§4/5、必要原始位置及精确隔离/重开条件；不验日期Gate、不复现、不扩全部附件或486宽池。

## 13088 / 13523：复用有效必要源核，窄终态通过

实际读当前README两小节与[V3_INDEPENDENT_FOUR_CALIBRATION](./V3_INDEPENDENT_FOUR_CALIBRATION.md)中当时非作者的必要原文定位与运算，采用命题和精确v1未改变。13088保留shared context token、centered A、同effective coefficient下抵消，孤立Cor3.2 Eq5缺失gradient geometry，不把Cor3.3的退化例子当独立推翻；softmax p=(.6,.3,.1)、等权两输出更新的log比一阶−.3η与相等系数差0的冲突可复核。13523保留ASV→MLIR→TAIDL/opaque fallback、有限bit/PE/DMA证明，只隔离Table2 B5 extension-after-truncation的一般clamp解释；128→−128和256→0不等8bit clamp127。

两者重开分别只需Eq5真实更新算子/gradient内积条件或近似说明，以及B5完整pattern/输入域/比较选择编码与等价依据或勘误。无需全版本史。**窄争议安全终态通过**；本文没有重新声称完整原文独立重读。当前README13088末句仍称“独立反证终核普通待办”，应由作者同步此未变有效核的复用结果，不能当本日仍需重跑全部附件。

## 13546 DynamicGate：更强原子并发保证的窄隔离通过

本轮实际打开[exact-v1](https://arxiv.org/html/2604.13546v1) §5.3–5.7 Eqs6–15、§6.2–6.6/Table1。Prop1的证明明确update在output计算之后，§5.7另列serving/training copies与periodic snapshot；这两个条件式可以成立，dense同样可用snapshot。Prop2 Eq11明确更新**active** W，却借inactive W不贡献来支持并发，论证不能给读active W时免同步的保证。gate-only也不是天然atomic；两层旧w1/新w2混读不保证同一个已提交snapshot。

注意Definition1写exists某parameter state，本身比“固定已提交snapshot”弱：不能仅用混合版本例子声称不存在任何数学参数向量，也不能说所有time-indexed dense函数未定义。当前日报已把争议限定到结构天然实现真正并发/快照一致性的广主张，保留先forward后update和fixed snapshot，方向正确。soft m非零不等Eq5 m=1完整active集合；Table1 dense全SKIP不构成same snapshot adaptation对照。**该更强保证窄隔离通过**。重开只需明确reader/update serialization、immutable serving snapshot或版本一致性协议与适用gate条件，不要求证明所有sparse adaptation无效。固定条件下有限adaptation结果仍保留。

## 13634 CSD：需修正为原文明确披露的lossy contract

本轮实际重开[exact-v1](https://arxiv.org/html/2604.13634v1) §3.1/§4 Algorithm1 lines9–22/§4.3、§5.1/Table1–3及**Limitations**。p=(.6,.4)、q=(.4,.6)、τ=.6、频率已过门的例子确实把b输出质量从target .4改成.6：经典accept .4加rescue .2，residual恒为a，p(b)/p(a)=2/3过门。这不保持target sampling law。

但Limitations明确写Departure from Distributional Exactness、heuristic criterion、prioritizes speed over strict statistical parity，并列unseen task/generalization、draft quality/high concurrency未验证；**lossy contract已在v1给出**，不是等待作者首次承认lossy才能关闭的未决。主实验最终greedy T=0、2×H20装70B/72B目标、single batch、固定四任务，mean task metrics仅支持该设置的accuracy/speed取舍；频率/门限组成条件式不等普遍semantic correctness，calibration1.5h/1000sample/2H20不是零总成本。

因此本项当前“暂缓直到显式lossy contract”的重开条件已经被可用原文满足。**原现有中央争议终态不通过，需要作者改判或精确收窄**：可终结为仅报告的固定heuristic operating point/受限设计分支（当前Ch48 exact/lossy分权已承载非exact性；若改Existing须作者实际比对具体论点），保留有限收益和反证，只隔离未证明的全域semantic safety/生产concurrency，不作为生产保证。不能以评价达不到普遍保证为由否定全部论文，也不能用“已有coverage”只指同主题。

## 13991 Adaptive Conformal：长文过滤分位方向窄争议通过

本轮实际打开[exact-v1](https://arxiv.org/html/2604.13991v1) §2.1–2.4/Eqs3–12/Algorithm1、§3.1–3.3。F_t={s≤t}随t变大保留更多claim，V为最大安全阈值，却取Q_(1−α)(V)再声称所有保留正确；每题一个错误claim、s=U~Uniform(0,1)、V=sup安全阈值=U，大样本α=.1时threshold .9，空集/全正确概率约.1而非.9。边界“sup不取到”在continuous U下无概率影响，不补公式为另一目标。

仅隔离长文all-retained correctness的方向/对象；MCQ Eq7 LAC真类集合覆盖与正normalizer、exchangeable三split的标准marginal条件不被此例否定。原3模型/8类长文、10shuffle repeats和embedding quantile归一化的有限经验保留，不升级为逐promptconditional定理。**窄争议安全终态通过**；精确重开为修正V/错误集合、量词、quantile方向或coverage解释并给对应证明/实现，不需全部附录。

## 14017 Stochastic Trust Region：步长下界及依赖保证窄争议通过

本轮实际打开[exact-v1](https://arxiv.org/html/2604.14017v1) §3.1/Eq1/Algorithm1、§4.1/Assumptions1–3/Lemma4.1/Eqs3–4及其紧接Theorem4.7使用。Algorithm1允许Δ0=.1、g=1，n=1、f=x²/2、x=1、L=1、ρ=1、c0=.1，H=I、step=−.1，模型/实际reduction均.095，ratio1被接受，a=.1；Lemma所称2(1−c0)/(L−c0)=2≤a≤1矛盾。光滑/无偏/SGC/插值在此例成立。两上界不能推出所列lower bound。

**窄争议安全终态通过**：只隔离该下界及依赖它的普遍complexity宣称，不推出经典TR ratio、所有TR分支或有限ResNet20/orthogonal fitting经验无效。重开限修正Lemma假设/推导与依赖定理；不要求完整版本史、所有numerical runs或代码复现。

## 交付范围

五项窄隔离/有效复用通过，一项CSD需要按原文已披露的lossy contract修正。六项均不新增Books；本文不替代root日级覆盖/日期/准入/全部候选/必要写回Gate。普通执行工作和上述真正公式争议分开，不以本小审计结束Apr20 lane。
