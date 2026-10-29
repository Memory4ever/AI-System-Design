# UGID19144：中心图同构/偏差迁移桥待独核

resume_mar18 sole准备，仅03-21补BJT03-20，原完整题摘/准入校准复用，不扩query；必要方法、评价、直接中心反侧已足。提案2+2+2=6中心终态隔离，未非准备者裁/未safe，不写Books或伪NC/EX。

实际[officialabs/v1](https://arxiv.org/abs/2603.19144v1)七作者、唯一v1及AB/history，无明确withdraw/correction/先公开venue说明；actual DataCite findable version1，submitted03-19T16:59:37Z、v1Updated03-20T01:15:57Z、created03-20T02:29:40Z/registered41Z，Available仅月份。沿本批BJT20公开日级夹证，不补精确first-public或声称无其他先稿。

仅输出目标可能未约束内部表示→原文以反事实gender输入同时约束attention谱、hidden差及reference/定义anchor→若成立会改变attention路由与FFN偏差补偿的设计解释，具体潜力成立，不因中心疑点降分或排除。实际[exact-v1](https://arxiv.org/html/2603.19144v1)§3.1–3.2/Eqs1–7、§4.1–4.5/T1–3、A/Alg1、B.1–B.4/Eqs8–9及C/T4–7必要反侧；不遍D全部图像或代码/复现。

## 中心证据与精确反例

原§3.2以causal三角A的L=D−A对角作为eigenvalues，匹配谱并以pronoun attention加权/去firsttoken，声称确保routing topology invariant；hidden差正则加logit/topk/KL，target与定义anchor分别训练。谱匹配并不识别加权graph同构，即使hidden相同也未排除此漏洞。自己实际算四token causal row-stochastic矩阵：

```
A = [[1,0,0,0],[.8,.2,0,0],[.2,.6,.2,0],[.3,.1,.4,.2]]
B = [[1,0,0,0],[.8,.2,0,0],[.3,.5,.2,0],[.2,.2,.4,.2]]
```

两者列和同(2.3,.9,.6,.2)、对角同(1,.2,.2,.2)，故按in-degree D构造的三角L谱同(1.3,.7,.4,0)，共同长度归一也不改变同谱。非对角权重multiset分别(.1,.2,.3,.4,.6,.8)与(.2,.2,.3,.4,.5,.8)，不可能通过节点置换实现加权同构；谱loss在任意saliency权重下均为0。原文“strictly lower”与正常causal包括对角口径不闭合，本反例使用合法causal含对角，不替原作者修公式。另B.3/Eq8把Spec定义为singular values，不等三角L对角eigenvalues，实际训练和报告指标口径不能自行等同。该反例只否定proxy→同构保证，不证明实验数据伪造或全部局部效果无效。

T2无Edge+Node的ID1.03/1.07、full .94/.94不证明所有偏差消失；列heading向1而非向0，低于1又不自动优于1。§4.4称variants3/4无anchor发生safetycollapse，但T2两行实际均100%anchor，未给无anchor行；不能自补为换列。T4区域anchor100→50直接反侧；T5 BOLD bias1.998高于CDA1.037，T7Qwen7BOOD mean2.14高于CDA1.14/KLAAD1.01，不采全scale Pareto/安全保持。100%六词anchor或IQ勾选不证全部知识/语用/真实公平，activationpatching文字不披露全部选择/干预反侧，不能由所选head因果敏感下降授全bias pathway sever。

训练10职业反事实pairs＋6定义anchor，B.1明确稀疏覆盖可能漂移；模型/metric跨各表不同，不合并全部fairness/utility。T6 A10080GB .4159s/it >base .2012，不把显存低/相对latency1×推零全费用；PEFT/weightfolding与仅更新targetlayers口径不充分闭合，全部反事实/reference/feature训练与审计费用保留。precision、完整sequence/batch/并发SLO与repeat/CI未充分披露，不采部署速度或无损保证。

## Actual owner与处置提案

预期sole `MODEL-TRANSFORMER-LAYER`/[Ch17](../../../../../books/part-02-model/17-transformer-layer.md)：实际完整1–85及312–352，Ch16/18开篇顺读。现有Attention跨token/MLP逐位置/Residual旧机制与逐层state诊断成立，不由输出或谱正则自动推内部迁移消除；原文若证全graph不变将新增跨两组件的解释，但当前中心桥不成立。不把一般jointregularization/anchor原则改写来绕过中心，也不因主题近给NC。

提案本窗保6分争议终态、不Books/不正面Evidence/Coverage。一次精确请求同family修订定义/实现指标和对照：明确causal对角、in-degree归一、eigenvalue vs singularvalue与可识别的routing条件；解释无anchor对照/100%表与50%区域反侧、原选head干预人口和utility检验。收到只定点重开§3/Eq1–9/T2/T4与实际owner，不扩全作者/版本史。交root非preparer必要Source/date/actualowner中心安全处置裁，未计safe/DAY。

## root 非准备者有限中心裁

实际打开 exact-v1 §3.2/Eqs2–6、§4.1–4.4/Tables1–3、B.3 singular-value定义；必要身份/date本批已核夹证复用，actual Ch17 1–39及312–352保持旧机制。两矩阵的列和/对角相同而边权集合不同，三角L的对角谱不能识别加权同构；同长度归一和saliency加权无法修复零谱差的反例。该数学反侧针对原文“ensures topology invariant”中心桥，不代表全部实验造假。指标口径不一致、Table2与无anchor叙述以及有限任务/定义anchor不能共同认证无bias迁移、安全或全知识无损。必要反证已足，不为证明不采用而全读图和代码。

6分准入与证据保持；接纳中心争议终态（第46安全处置，39I＋5NC＋2center），不写Books/不授正面Evidence或Coverage、无实际POST。精确修订请求及owner已在上段，材料到达只定点重开中心桥，不把当前局部观察洗成成熟jointregularization增量。日级DAY未通过。
