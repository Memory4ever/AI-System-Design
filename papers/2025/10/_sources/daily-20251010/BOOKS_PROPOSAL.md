# 2025-10-10 唯一窄 Books 提案

Owner：`TRAIN-DATA`，Ch27；作者Mill，仅提案未写共享Books。

独立证据：[Peirce FIRST](FIRST_INDEPENDENT_REVIEW.md)及[FINAL §2–3](FINAL_INDEPENDENT_REVIEW.md#2-原事件与必要核心实际核验)，正式采用边界见[日报§4](../../10/README.md#4-证据与知识整合)。页面事件2025-10-09T21:50+08落窗，论文first-public未确定，不借页面日期搬移论文。

## 实际差额

实际读[Ch27 training effect](../../../../../books/part-04-training-system/27-data.md#内容无害不等于更新无害过滤器还要预测-training-effect)L281–308及代码训练段，已有内容/更新、checkpoint/recipe/lineage/canary分责；[Recursive Data](../../../../../books/part-04-training-system/27-data.md#recursive-data-的控制量不只有比例还包括真实样本绝对注入量)L1253–1258已有绝对量/比例原则。邻接[Ch28 NTP](../../../../../books/part-04-training-system/28-pretraining.md#next-token-objective)已有token exposure/batch/normalization/budget分账。不能声称原则全新或整章无相关覆盖。

差额是受限安全判断：扩大clean corpus、降低污染比例本身不能证明抗投毒或攻击成本同步增长。建议在Ch27 training-effect现有论证前后嵌入短段，分别保存恶意文档数、poison-token暴露、干净预算、batch密度/顺序、LR/recipe及配对行为测量；Data拥有输入/lineage，trainer消费冻结配方，行为测量不能由比例替代。

证据只限600M–13B的受测gibberish/DoS、24配置×3seed。文档/token不可互换，不写普遍250常数。顺序/batch/LR会改变样本要求，clean continuation及模拟alignment可削弱后门；真实生产安全post-training持久性与防御有效未证明，特定SFT harmful-compliance不混入预训练跨规模结论。过滤可信来源、隔离可疑数据、小规模canary与held-out安全回归仍是旧路径，新增审计与试训有成本、不认证完备。

仅此1条整合提案，无新章节/Structural Candidate。root实际写入后需非写入者核正文/邻接及来源边界；当前实际写入0、DAY未通过。OpenAI五轴评价最终仅报告，不提第二条差额。
