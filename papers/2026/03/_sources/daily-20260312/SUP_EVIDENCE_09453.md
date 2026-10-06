# 2603.09453 — stochastic logit routing与任务/校准/费用分账（必要Source/date/PRE/actualPOST通过）

[Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers exact-v1](https://arxiv.org/html/2603.09453v1)。作者actual完整§2–5/7，A.2、完整C.1/C.2、D.1/D.2/D.3与E必要范围；Tables1–8中拟采用关键字段实际读。未读全部F–H、曲线像素或外部仓库/运行实现，不授复现。完整AB准入root第二包通过；currentv3 May28 AcceptedICML2026，v1 In submission，本窗不回填后版，不以版本号或接受本身推更早公开。当前题摘轻改fine-tuning范围，无已见withdraw/纠错信号，不扫会议池。

日期原batch2中09453 owning arxiv.content/findable注册Mar11UTC02:13:57为已经可发现上界；SubmittedMar10UTC10:07:53配官方noadvance最终ID/DOI及公告截止规则最早Mar11BJT08公开下界，两端同03-11BJT才夹证当窗。不是Submitted/Updated或注册单独充公开。必要日期待root实际核。

拟2+1+2=5标准；由于具体长期router机制缺口而深入必要范围。固定Top-k给定表示单次打分→input-conditioned residual Gaussian logits/MF或Cholesky covariance并平均softmax后一次Top-k→比较局部随机路由、校准与容量执行，不能以router随机性代表整模型Bayesian epistemic guarantee。唯一MODEL-MOE，拟Ch21具体两段，不重写capacity/dispatch owner。

## 方法、关键评价和直接反侧

§2权重仍point estimate，§3VGLR残差mean=detlogits+delta、covariance=LLᵀ、prior=N(detlogits,I)，Gaussian analyticKL约束残差/协方差；原冻结base router仍消费变化的hidden输入。MF O(N)，FC O(N²)，本实验N40/60/64不普适低费用。训练1sample；推理S35采logits、softmax逐sample再平均，最后一次Top-k执行experts，不是35次完整expert forward，也不是softmax(meanlogit)。C.1/C.2实际保同逻辑，不以code片段省略capacity/gating视为整图验证。

§4VTSR以MLP正温度重标fixedlogits，推理Sample-K withoutreplacement；仅正温度缩放再hardTop-k不改变排序。A.2推的是categorical KL=logN−H，不是完整subset posterior。实际C regularizer −logT与有界KL不等：T→∞前者→−∞、后者→0；其熵鼓励是proxy，不能冒称精确KL目标或无collapse。C.1训练(l+g)/T的TopK软表示，C.2为gumbel_softmax(l/T,tau1,hard=True)后Topk；K>1时onehot其余并列、straight-through怎样穿过index/gating未完整给出。两者噪声尺度不同，且boilerplate省略，不能认证同一可执行Sample-K训练recipe。保留VTSR有限实验作为比较，不采用其全部数学/代码一致性或T→0任意K无条件推导。此局部不阻断独立支持的Gaussian-logit分支，不把整篇标全错。

D.1/D.2三模型Granite3.3Bactive.8B、Qwen14.3Bactive2.7B、DeepSeek16.4Bactive2.8B，均有限MCQA微调；不是trillion/70B完整生成。阶段1 attention/expert LoRA3epochs，选10敏感层，阶段2冻结既有模型/LoRA/router、只训练phi最多10epochs+valNLLearlystop。Granite调grid再转其他模型，datasetβ仍选；5runs meanstd、A10080GB、batcheffective16作者配置，非本轮复现。冻结权重与相同stage1 baseline可减混杂，但不唯一隔离随机性：新phi/residualmean、10epochs/额外调参均是方法bundled treatment，不能用“严格归因probabilistic routing”宣传自签因果。精度、完整硬件数量、训练/发布latency/SLO未披露。

Tables1/7校准与accuracy分开：OBQA Granite MAPacc.746/FC.740、ECE.252/.015；不能拿ECE大降说无质量损失。更直接Table7 MedMCQA Granite MAP.550/FC.494、Qwen.542/.490，VTSR Granite.476；保留不同domain与均值/重复条件，不拼普遍不降accuracy。D.3/Table8另OBQA为train、ARC等为shift；FCvariance(traceΣ)平均AUROCGranite.749对其GateEntropy.659，近ARC-E.609低于MAP.612；VTSR rawtemperature.509而其GateEntropy.743。traceΣ是方差之和，不含Σ的offdiag项本身；FC建模可能影响训练但OOD分数不证明correlation独因果、任务正确、安全或通用epistemic。

Table3 embedding各向Gaussian σ.001–.01后的expertsetJaccard只指路由membership稳定，不是真实语义robustness/任务正确。不得将摘要38%作为所有扰动/任务保证。E明确并行S样本假设、router weight/mask复制比较；MCDropout可顺序或其他实现，不把S复制当所有weight-space必需。Table4 FC additionalGFLOPs .0096/1.07%、activation-labelled9.2M/1.15%违背全<1%；VTSR .0060/.67%。E的memory实际按固定network参数计数，不包括全部MCsample buffer/峰值、softmax平均及dispatch/选expert执行；fvcore单Graniteforward算FLOPs不是end-to-endwallclock。额外phi训练、先验/regularization选择、敏感层选择、采样softmax/聚合、covariance和routing/负载/通信均需分账。无完整运行验证或matchedSLO保证。

## 实际owner与逐字PRE

作者actualCh21 1–85完整Dense→router shape/子空间分支→top2，550–603实际executionphase/variable-k及router mass非通用epistemic边界；Ch20/22开篇交接。本轮仅需要在现67子空间完整段之后、top2小例子之前增加随机logit机制与任务/费用边界，原linear/subspace、capacity/负载均衡和静态路径保留。现588只拒绝mass作通用epistemic，未承载input-conditioned Gaussian posterior参数化及平均softmax→一次选择，存在窄gap。

拟段1：

确定性 router 适合需要固定执行语义与低额外成本的场景，但一次 logit 打分不能描述同一输入下路由决策的变化。一个受限替代分支保留原 linear logits，在其上学习输入条件化的残差均值与 Gaussian 协方差：mean-field 只预测逐 expert 方差，full-covariance 以 Cholesky 因子表示相关性，再用以原 logits 为中心的 Gaussian prior 约束这条新增路径。训练时采一组 logits，推理时采多组、分别 softmax 后平均，最后只做一次 Top-k 与 expert 执行；这不等于多次运行所有 experts，也不等于 softmax 平均 logits。另一种较窄的分支只学正温度并随机抽取 experts；温度自身不改变 fixed logits 的 Top-k 排序，随机选择、实际 gate 权重与代理梯度必须另说明，不能把概率更平直接叫稳定执行。两者都只建模局部路由变量，不是全模型权重后验，也不由 router mass、协方差或温度自签任务正确与通用 epistemic uncertainty。

拟段2：

这条分支用额外训练、协方差构造和采样换路由校准，但校准误差下降与答案准确率不下降是不同验收：有限 MCQA 对照中，两者可以一升一退，近域 shift 的检测也不必优于原 gate entropy。Gaussian-logit 推理可把 expert 执行保留为一次，却仍增加 inference network、逐样本 softmax/聚合与 full-covariance 的平方级 expert-count 成本；并行采样时的参数计数和单 forward FLOPs 不等峰值显存、全生成延迟或通信费用。[必要机制、评价与反侧](https://arxiv.org/html/2603.09453v1)只支持已披露模型、任务、敏感层选择和微调协议的受限分支；temperature 的熵正则代理及省略的离散 gating 不能当作已核一致实现。发布时应共同验收任务质量、校准、路由负载与完整费用；不改善、分布漂移或预算不允许时，原 linear/固定 Top-k、子空间匹配与独立质量检查仍保留，而不是由一个 uncertainty 分数覆盖容量和 dispatch 约束。<!-- source-family:SF-2026-ARXIV-2603-09453 -->

拟自身末注：2026-03-12增量2603.09453 exact-v1：作者实际§2–5/7、A.2、C.1/C.2、D.1–D.3与E必要原证，Gaussian-logit残差/协方差→softmax均值→一次Top-k窄差额；MCQA accuracy/calibration反退、rawtemperature/OOD与全费用边界保留，VTSR伪代码/片段一致性未授。不授全部附件、实现/复现或完整SLO。

实际：root必要Source/date及逐字两段PRE通过，actual§2–5/C.1–2/D.2/T7–8/E与Ch21 42–95必要owner。授锁后作者仅写Ch21 67/69两段与本人1052注，实际順读62–94完整router/子空间→随机分支→top2及自身注。root非writer顺读55–97完整局部、新两段/本人注并回对必要原证，actualPOST通过并释放Ch21锁。正文与逐字PRE一致，原linear/subspace和capacity/dispatch没有删除或覆盖；单次Top-k/局部变量后验、MCQA反退和完整费用界准确，不授DAY。
