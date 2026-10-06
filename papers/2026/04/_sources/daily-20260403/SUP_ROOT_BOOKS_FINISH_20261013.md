# 04-03 两个尾项的实际 owner 差额与逐字 PRE

root准备，仅本日00923/00938；必要Source复用本日原TENTH与tail实际补核的k接口/Alg1，不扩发现。两项均2+2+2=6；00938纠错深审受影响保证，00923因具体Books缺口定点深审，不等于全文/代码复现。

## 00923 → TRAIN-SFT / Ch29

实际读本章Full fine-tuning/parameter-efficient adaptation、Necessity与Plasticity、TrainableSubspace连续段及Ch30原参数轮换/LoRA objective与placement交接。现文有架构内必要性/可塑性、regime/task-order共同验收，但未解释语言任务方向与front/rear更新的两端模块资格；Ch30不重复拥有适配层选择证据。仅在Necessity与Plasticity现段之后、TrainableSubspace标题之前插入：

> 语言适配还要区分读入与生成的任务方向，而不只给各层一个统一重要性排名。可固定可训练block预算，比较从输入端、输出端及两端展开的更新，并分别记录embedding与LM head是否开放；它们不包含在block计数中，因而相同k不保证相同总参数或计算。[受限低资源语言对照](https://arxiv.org/html/2604.00923v1)中，两端少量层是一条可行的静态分支，不是已确认的人脑式功能分区；不同翻译方向与顺序训练仍有退步，冻结中层也不认证推理或旧语言全部保持。免做Fisher选择器不免完整前向、反传和训练sweep成本；语言、任务或预算失配时，保留全量更新、经验证的LoRA placement及逐任务回归，不把“外层占四分之一”当作全成本节省比例。<!-- source-family:SF-2026-ARXIV-2604-00923 -->

本人Review notes内部追加：

> - `SF-2026-ARXIV-2604-00923` — Daily2026-04-03补窗；[CogSym exact-v1](https://arxiv.org/html/2604.00923v1) Methodology/Experimental Setup/Training Details、Results/Sequential Training/Limitations。2+2+2=6，仅task-direction/trainable-interface差额；k不含embedding/head，非同总参数/75%全计算节省或脑区因果，顺序反退与完整费用近正文。必要Source与逐字PRE/实际POST分别验收；未核实现/复现。

## 00938 → TRAIN-SFT / Ch29

实际读Catastrophic forgetting中全量/adapters/earlystop与retain多切片验收，前方trainable-subspace及后方具体事实适配交接；现文没有把有限repair约束从线性化solver资格接到真实非线性验收。仅在该节现“缓解方法可能包括……”段之后、双pass接口修复段之前插入：

> 需要纠正一组已知分类失败时，还有一条不同于普通梯度微调的有限修复分支：冻结前置表示，在分类head前的dense层提出小更新，用当前logit-gap的一阶近似建立repair/remain约束，再迭代求解；敏感性预处理只改善可行性，不能代替最终行为检查。Solver可行与真实margin通过是两件事：[受限内层修复证据](https://arxiv.org/html/2604.00938v1)的成功停止检查repair真实gap，但预算耗尽也会返回权重，remain近似约束亦有未达目标margin的样本，故不能把任意返回或remain仍分类正确说成全部证书成立。局部半径在固定repair-layer representation的球内，不自动传给原文本扰动；原gap常数证明资格未解决，不采用其完整半径公式。低秩SVD、预处理、QP与双侧回归均付费，局部泛化切片也退步；约束失效、预算耗尽或任务不满足该分类结构时，保留原checkpoint、可信replay/adapter与独立release gate，不以有限修复签发开放生成或全能力安全。<!-- source-family:SF-2026-ARXIV-2604-00938 -->

本人Review notes内部追加：

> - `SF-2026-ARXIV-2604-00938` — Daily2026-04-03补窗；[WARP exact-v1](https://arxiv.org/html/2604.00938v1) §3.2–3.5/4.1–4.5、Alg1、必要B.1–B.3。2+2+2=6，深入受影响保证；仅linearized proposal/real repair acceptance差额，保预算耗尽非成功、remain 798/800与786/800、representation非text半径、Eq12常数资格和泛化/全费用，不补作者定理或授开放生成保证。必要Source与逐字PRE/实际POST分别验收，未核实现/复现。

两项均尚未实际写书，不计I或DAY；等待非准备者PRE核验后只写批准的local body与本人末注。

## 实际写后及三项新日门（当前路由）

923/938两段及本人Review notes已按通过PRE实际写入Ch29；apr03_reader_finish已实际读正文、完整邻接和本人notes，非writer POST通过。root随后仅同步本人notes状态，不扩大正文或证据范围，待reader定点最终读回释放。不授整日DAY。

root实际正常GET官方DataCite matching DOI/URL/title、`findable`与arXiv-owned版本字段：

| 精确家族 | 官方GET | 注册原值（仅公开上界，不单独代公告） | v1 Available |
| --- | --- | --- | --- |
| 2604.00422 | https://api.datacite.org/dois/10.48550/arXiv.2604.00422 | 2026-04-02T02:00:57.000Z | 2026-04 |
| 2604.00519 | https://api.datacite.org/dois/10.48550/arXiv.2604.00519 | 2026-04-02T02:03:14.000Z | 2026-04 |
| 2604.01212 | https://api.datacite.org/dois/10.48550/arXiv.2604.01212 | 2026-04-02T02:19:39.000Z | 2026-04 |

三个身份标题分别matching SHARPEN、Learnability-Guided Diffusion、YC-Bench；原Submitted值不当公开日。沿本日已独核的MM04正常公告下界与matching owned公开上界双向链，仅支持April2北京时间自然日；并未用注册代技术证据或恢复精确公开时刻。未发现这三条所见身份有更早正式全文的具名线索；不扩版本史证明绝无旧稿。

01212另实际打开[exact-v1 PDF](https://arxiv.org/pdf/2604.01212v1)首页，matching标题/七作者/摘要且正文Date April2；HTML的August24不作为本次证据。TAIL实际复核同PDF必要§3/4.1/5/AppC负例层，reader实际确认PDF身份与具体Ch77正文已有覆盖；不混HTML或自行迁日。

最后归并仅按实际Source/owner/POST；519日门已可由reader按此有限原证链核验，不由POST倒推日期。00422/01212两个5分具体NC仍由reader决定，未把其余EX改成待全文队列。
