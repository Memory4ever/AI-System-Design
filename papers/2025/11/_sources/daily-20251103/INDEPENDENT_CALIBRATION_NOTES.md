# 2025-11-03 首批独立准入校准与必要原源 notes

复核者：Codex独立复核者（本任务独立分工，非Carver作者）。检查时间：2026-10-04T15:23:29+08:00，来自工具clock `2026-10-04 07:23:29 UTC`。

本轮fresh重读AGENTS、RESEARCH_CONTRACT、RESEARCH_SOURCES使用说明/每日/arXiv、REPORT_CONTRACTS、Prompt与ROADMAP；仅加载本日FIRST_CALIBRATION_READY和三个具名材料。窗口仍为BJT `[2025-11-02T09:00:00+08:00,2025-11-03T09:00:00+08:00)`。不验收本日来源总体覆盖、Books或日级完成，不复用其他日期候选。

## 1. 校准结论及交回Carver

**准入校准通过，但中心理论采用不通过，需要按下述具体边界续写。** 2511.00341v1提出可能改变训练目标解释的明确主张，值得定点核理论，不因没有benchmark排除；必要核验已发现证明跳步，不能升级为成立的设计修正。日期尚未确认落窗，保持缺口身份，不评分、不列确定当窗候选、不进Books。医学聊天与浅水求解器两个负侧均可范围关闭。

Carver可继续本日有限工作：把中心主张与本轮反证并列，有限完成首公开日期恢复、剩余窗口筛选和报告整理。不要为这篇扩扫所有CoT/反转论文或等待全月；不要求作者另造一个修正理论才能继续。必要日期仍不可得时隔离日期；即使日期恢复，以下中心争议也须独立处置，不能随日期确认自动采用。

## 2. Reversal Invariance：实际原源与理论边界

身份：[2511.00341v1摘要页](https://arxiv.org/abs/2511.00341v1)与[exact-v1 HTML](https://arxiv.org/html/2511.00341v1)。摘要页题名为 *Reversal Invariance in Autoregressive Language Models*，HTML标题为 *Reversal Invariance: A symmetry argument against the arrow of chain-of-thought*；同一精确ID，完整摘要一致，不拆成两个家族。实际亲读完整摘要及§4.1–4.5、Corollary4.6/Remark4.7、§5.1–5.4、§6结论与§9限制；未逐篇复核参考文献、实现或训练实验。

**原文主张与假设。** 摘要将反转前后NLL相等解释为CLM方向盲。Definition4.2假设重新训练的tokenizer满足词表双射加token序列反转；Lemma4.3只证明词表一致重标号的等变性。Remark4.4另要求相对/RoPE位置处理或绝对位置翻转；Theorem4.5把这些操作组成参数映射，声称经验NLL相等，Corollary4.6再推训练景观/学习曲线等价。§9说明这是无自身实证实验的理论position paper。以上均是待检主张，不是本轮认可的结果。

**具体证明跳步。** §4.5 Proof sketch把Lemma4.3对 `pi(z)` 的等变性用于 `pi(rev(z))`；词表重标号不等于位置反转，原序列前缀也不变成反序列的同一个条件输入。改变mask的坐标表示可重新描述一组计算，但不能据此证明标准反向next-token任务与标准正向任务条件分布相同。若需要修改因果mask、预测目标、信息可见集合，必须明确额外模型/训练契约；不能把它们隐藏在只含词表和位置重标号的参数映射中。

**复核者构造的最小反例，不是论文实验。** 取字母级tokenizer、词表 `{a,b}`、语料 `D={ab}`，反转后仍用同一字母级tokenizer。Definition4.2此时强制 `pi(a)=a, pi(b)=b`。取忽略位置的有限参数AR bigram模型，条件表为：

```text
context a: p(a|a)=0.1, p(b|a)=0.9
context b: p(a|b)=0.2, p(b|b)=0.8
```

这些条件均正规化，可由untied embedding/output的有限logits实现；位置编码可不参与输出，因此翻位置索引不能改变它。按论文Eq.(1)的首token不计分约定，`NLL(ab)=-log(0.9)=0.1053605`，`NLL(ba)=-log(0.2)=1.6094379`；其限定的词表/位置映射此时不改变该模型。补齐初始概率 `p(a)=p(b)=0.5` 后，正规化联合概率仍分别为0.45和0.10。已实际运行条件正规化与两种计分的算术检查；没有运行LLM训练、测学习曲线或声称经验复现。

**不能混同的三个层次。** 概率链式法则允许用不同变量顺序分解同一个联合分布，但右向条件应由该联合分布重新求得，不能直接复用左向网络的条件函数。另定义 `Q(z)=P(rev(z))` 可得到反转分布，却不证明Q由同一有限CLM家族通过论文限定的重标号实现。平稳过程与其反转的block entropy/熵率相等，支持相应理想熵下界相等；实际模型NLL还含分布拟合误差，这个误差和训练动态不由熵率相等固定。即使另有有效的风险重参数化证明，学习曲线等价还须核初始化、优化器、步长与数据次序等是否随映射保持，不能仅由光滑映射推出。

**采用边界。** 当前不采用“有限CLM经验目标普遍反转不变”“景观/训练曲线等价”“NLL不能学方向或因果关系”“CoT只是后补被抹除的方向性”。也不能把成熟链式法则/熵率性质计成本材料的Durability3。本轮保留的是潜在贡献的准入及具体中心争议，不因争议或深审成本将其改写为明确无贡献；未授标准/深入证据完成或Books已有覆盖。若要重开正面理论采用，需要精确修订稿/作者勘误给出保持因果条件输入的合法参数映射及完整证明，或明确收窄成理想分布命题；本反例的适用性须被直接处理。

**日期保留。** 本轮不另作首公开检索；原生v1摘要页读取到`[v1] Sat, 1 Nov 2025 00:51:46 UTC`，只支持Submitted身份，不授首公开。FIRST_CALIBRATION_READY中的DataCite登记/Updated/月份及schedule边界按作者原证据权限保留，本轮未独立重验这些字段或历史公告。没有从v1页眉日期、Submitted或月列表位置伪定公开时刻，也不裁决真实归属日。潜在知识owner以ROADMAP中的 `TRAIN-PRETRAINING` 为训练目标解释入口，`MODEL-DECODER-ONLY` 仅交接架构/条件可见性；不是最终Books owner或差额验收。

## 3. 两项负侧样本

- [Fine-Tuning DialoGPT on Common Diseases in Rural Nepal for Medical Conversations, 2511.00514v1](https://arxiv.org/abs/2511.00514v1)：本日cs.CL标题切片item21身份匹配；额外亲读原生exact-v1完整摘要。其增量是合成十种疾病医患对话上的既有DialoGPT微调和领域回答表现；offline是部署诉求，不见新的端侧执行机制、可比资源取舍或通用训练/安全反证。**范围关闭通过**，理由是领域应用未建立当前模型系统机制贡献；不是把所有医学相关方法研究一概归为AI for Science。未读全文、未认可其医疗适当性/有效性，无需为不影响关闭的公开时刻另开待办。
- [Towards Portability at Scale: A Cross-Architecture Performance Evaluation of a GPU-enabled Shallow Water Solver, 2511.01001v1](https://arxiv.org/abs/2511.01001v1)：本日cs.DC标题切片item7身份匹配；额外亲读原生exact-v1完整摘要。实际workload是SERGHEI-SWE浅水方程求解器，评估跨异构GPU/HPC的scaling、roofline与Kokkos移植性能，没有模型训练/推理计算的具体关联。**范围关闭通过**；GPU、memory-bound、portability标签不足以改授模型系统贡献，不能把求解器数字外推为LLM benchmark。未读实现/全文或验证性能数字，不需额外日期恢复。

上述两项当前原事件页未见需重开的撤回/纠错提示，不因此遍历完整版本史。两项摘要的额外读取是分层校准样本，不把本日25+25标题切片变成50篇摘要/全文队列。Seed电池合作本轮未独立检查，不授该样本复核通过。

## 4. 本轮终点

只通过1项潜在准入的定点校准与2项范围关闭；Reversal中心采用未通过、首公开仍未定。14来源日级覆盖、剩余材料、六部分报告及Books差额未检查，不授日级完成。仅写本日首批校准/原源notes；无Books、月索引、LEARNING_STATE或他日改动，未stage、commit、push。
