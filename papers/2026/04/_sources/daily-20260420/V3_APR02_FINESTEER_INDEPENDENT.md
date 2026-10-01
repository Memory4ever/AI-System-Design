# FineSteer 15488：有限非作者采用复核

复核者：apr02。实际重新读取当前 AGENTS、Research/Report 合同与作者采用包；只核本项必要命题及实际 owner，不验收 Apr20 日期/整日 Gate，不修改 Books。原始来源：[2604.15488v1](https://arxiv.org/html/2604.15488v1)，实际核 §5.1–5.3、§6.3–6.5 Tables3–6、§9 与 A.1 的 evaluator/实现说明。未复现实验。

**结论：6 分、具体缺口深入的窄 source→owner 提案通过；尚未实际整合/写后通过。** 实际 Ch72“Privacy 与 Unlearning 都需要输入条件化 Gate”当前只有 activation redirection、行为抑制不等权重删除以及漏检/旁路/utility 分账；没有把输入 gate 与 query-specific 干预向量的训练责任拆开。拟在该段之后、模型范围限制之前嵌入两段是合理位置，后接权重级删除/访问控制仍成立；不是因为新方法未逐字出现就默认缺口。

原文 §5.1 的 mean-centered PCA/SER 是触发代理，非已校准 harm probability；quantile gate、监督 logistic gate 与 §5.3/Alg3 的直接 soft SER 要分别表述。§5.2/5.3 明确固定 prototype bank 但 WQ/WK 与 residual MLP 要训练，不能沿 Introduction 的 training-free 泛化句。作者拟稿正确保留这两处边界。

Table6 的 Qwen Truthfull54.28低于 w/o SCS54.77，而 GSM95高于34，说明有效性/效用的条件取舍，不是全部指标最优。Table4 的113秒非快于 Alpha70秒，284.7GB是四卡累计；Table5 A800每token40.43vs40.38只支持局部成本，precision、长度、并发和生产SLO未给完整合同。A.1使用 GPT-4 evaluator；§9 明示可优化输入避开触发子空间，不能采用开放攻击保证或彻底遗忘。

建议保留作者两段的最窄 when/how 分工、proxy/训练/在线成本、adaptive bypass、固定轻干预及权重级方案共存。不要将本审计写成原论文全部主张通过，也不把提案 PASS 当实际 Books 或整日完成。

## root实际写后复核

root实际读取Ch72“Privacy 与 Unlearning 都需要输入条件化 Gate”的新增两段及上下activation redirection/权重级删除交接，并复用上述未变的必要来源审阅。PCA/SER只作输入线索、prototype固定但controller仍训练、三gate非同一实现、Truth反向/utility分账与adaptive旁路均留在正文，未用局部A800成本声称零成本/p99，不把抑制写为删除。Review note与实际采用范围一致；这两段已实际写入、写后通过，可以同步15488整合状态，但不增加整日完成数。实验未复现，外部开放攻击/生产保证未验证。
