# B20 — 六项必要原证 / actual owner；本次独立复核已落实

2026-10-06 feb26_close_oct06 非原packet作者从exact-v1 raw逐项重新定位所引原pID；另核20396原definition/lemma条件、20419 A2.3全部必要alttext事件、20467原S3.E7和EGx14二次驻点、20593原threat/inference权限。actual Ch5 reference/因果条件、Ch72 lifecycle/认证边界、Ch49重构/补偿自由度、Ch24posterior/MC/solver、Ch66rubric/competence/人工anchor已独读。20396/20467/20593/20629具体已有覆盖；20549条件iid平方估计和有限posterior/model选择反侧仅报告；20419以具体人口分离/事件/neighbor界未立隔离中心认证保证，不否定有限AUROC。20467只采用独立可识别vector条件机制，不修scalar Eq7、不采scalar exact配方；原方法/分母/费用/反侧与ND保留，未运行artifact/复现，非日级验收。

## 2602.20396v1
https://arxiv.org/html/2602.20396v1

S3.Thmtheorem2.p1.1 | Given a feature X_{j} with X_{j}\perp\!\!\!\perp_{\mathcal{G}}Y we have I_{\mathrm{do}(\mathcal{S})}(X_{j})=0 for any \mathcal{S}\subseteq\mathcal{F}\backslash\{X_{j}\} . This implies that we have X_{j}\perp\!\!\!\perp_{\mathcal{G}}Y\Rightarrow\phi_{cc}(X_{j})=0 for \phi_{cc} as in (6).

S3.SS1.SSS0.Px2.p1.1 | At first sight, it might appear tempting to replace a symmetric object such as \mathbb{E}[Y|X_{j},\mathcal{S}] with a symmetric interventional analogue such as \mathbb{E}[Y|\mathrm{do}(X_{j},\mathcal{S})] . This is the approach studied by jung2022measuring and heskes2020causal and fits into the original framework proposed by Shapley and others [1953], cf. Appendix A. However, this would delete too much association: In an anti-causal setup such as the running Example 1.1, where there are no causal paths from the features towards the target, no feature would be attributed importance.

S3.SS2.SSS0.Px3.p1.1 | Algorithm 1 summarizes how I_{\mathrm{do}(\mathcal{S})}(X_{j}) can be computed given an SCM \mathcal{M} . This is the method that we use in Section 4 below. We first isolate the joint marginal q of the context variables \mathcal{S} within the original model \mathcal{M} . We then perform a stochastic intervention on the SCM to obtain \mathcal{M}^{\mathrm{do}(\mathcal{S}\sim q)} . In this modified model, we can obtain estimates of the functions \mathbb{E}[Y|X_{j},\mathrm{do}(\mathcal{S})] and \mathbb{E}[Y|\mathrm{do}(\mathcal{S})] via standard multivariate fitting using data-driven models, cf. Appendix B.4.

S3.SS3.p1.1 | Neither the original Shapley values (1) nor our causal analogue (6) are scalable in the way they are formulated here. The number of of context sets \mathcal{S} increases swiftly with |\mathcal{F}| and for each feature X_{j} and context \mathcal{S} two data-driven models have to be fitted to estimate \mathbb{E}[Y|X_{j},\mathrm{do}(\mathcal{S})] and \mathbb{E}[Y|\mathrm{do}(\mathcal{S})] . Scalable approximations [Chen et al., 2023, parafita2025practical, teal2026exactly] could be a way out but were not studied in the scope of this work. The main focus of this article is to highlight a systematic weakness in the existing approach to XAI and to point out what is necessary to fix it.

S3.SS3.p2.1 | Another limitation that is shared by many other works on causality, is the assumption that the causal graph that has generated the data is known. Once we have obtained this graph, we can often fit the functions (f_{X})_{X\in\mathcal{V}} in the SCM and subsequently apply Algorithm 1. This is the procedure that we follow for the real world example in Section 4 below. In specific cases, such as linear SCMs with non-Gaussian noise, algorithms such as LiNGAM [Shimizu et al., 2011] can be used, cf. Section 4 below, to obtain the causal graph. For more general approaches to causal discovery compare also the work of Zheng et al. [2018] and the reviews by Zanga et al. [2022], Glymour et al. [2019]. In the general case, however, obtaining a valid causal graph is typically non-trivial and often requires expert knowledge. Moreover, in accordance with many other works in causal inference, we have to assume that the exogenous variables in our model are uncorrelated, which is typically an oversimplification.

## 2602.20419v1
https://arxiv.org/html/2602.20419v1

A2.SS3.p3.1 | Bounded differences. Replace a single sample (Z_{1,r},Z_{2,r}) by (Z^{\prime}_{1,r},Z^{\prime}_{2,r}) . This can affect: (i) the r -th summand itself, (ii) any sample j\neq r for which r falls inside the ball of radius \varepsilon_{j} in Z_{1} or Z_{2} (thus changing n_{x}(j) or n_{y}(j) by at most 1 ). For k -nearest neighbour type estimators, each point can belong to at most k such neighbour sets in each marginal space, so at most 2k other summands change. Hence, no more than (2k+1) summands are affected. Since \psi is monotone and for m\in[1,n] we have |\psi(m_{1})-\psi(m_{2})|\leq\log n , each affected summand

A2.SS3.p7.2 | Assume the surrogate is sufficiently close to g so that \mu_{\mathrm{sur}}>\tau(\sigma,Q) ; set t=\mu_{\mathrm{sur}}-\tau(\sigma,Q)>0 . McDiarmid’s inequality yields

A2.SS3.p7.3 | Because \tau(\sigma,Q)\to\beta(\sigma,\delta)(1-\rho) as n\to\infty and \mu_{\mathrm{sur}} stays above this limit by a positive margin, the exponent diverges to -\infty , hence \gamma_{2}\to 0 . ∎

A3.SS1.p3.1 | Dataset Partitioning. For dataset partitioning, we strictly follow the default train–test split. In addition, we introduce two auxiliary subsets: the query set and the verification set. Specifically, the query set is defined as a randomly sampled subset of the training set, with its size controlled by the query budget Q. The verification set is defined as a randomly sampled subset of the testing set, with its size determined according to practical requirements. Importantly, we ensure that the query set and verification set are strictly non-overlapping.

A2.SS3.p4.2 的 < 号导致 paragraph 投影损坏；CORE 5850–6060 原 TeX/文本行：
\Pr\!\left(\widehat{I}-\mu_{\mathrm{ind}}\geq t\right)\leq\exp\!\left(-\frac{2t^{2}}{\sum_{i=1}^{n}(c_{i})^{2}}\right)=\exp\!\left(-\frac{2nt^{2}}{C_{k}^{2}}\right).
Take
t=\tau(\sigma,Q)-\mu_{\mathrm{ind}}
\mu_{\mathrm{ind}}<\tau(\sigma,Q)
\Pr\!\left[\widehat{I}-\mu_{\mathrm{ind}}>\tau(\sigma,Q)\right]\leq\exp\!\left(-\frac{2n\bigl(\tau(\sigma,Q)-\mu_{\mathrm{ind}}\bigr)^{2}}{C_{k}^{2}}\right).
\mu_{\mathrm{ind}}\approx 0
\Pr\!\left[\widehat{I}>\tau(\sigma,Q)\right]\leq\exp\!\left(-\frac{2n\,\tau(\sigma,Q)^{2}}{\bigl[2(2k+1)\log n\bigr]^{2}}\right)\triangleq\gamma_{1},

## 2602.20467v1
https://arxiv.org/html/2602.20467v1

S3.SS0.SSS0.Px2.p1.1 | Assuming that the weights and bias adjustments are small, we proceed by computing a Taylor expansion of the network to approximate the discrepancy:

S3.SS0.SSS0.Px2.p3.2 | A note must be done on the computational cost: considering \alpha C_{f} as the cost of backpropagation, the computation of the importance for all weights is proportional to \alpha C_{f} instead of |W|C_{f} as previously mentioned, making this strategy computationally affordable.

S4.p1.1 | In this section, we present numerical experiments to demonstrate the effectiveness of the proposed method. In the first experiment, we use the well-known MNIST dataset [16], while in the second we employ a dataset constructed from solutions of partial differential equations [30]. The datasets are split into training and test sets. The training of the networks and the evaluation of importance are carried out using the training set. Subsequently, performance is assessed on the test set. Performance is evaluated by computing the test loss for different pruning ratios. We define the pruning ratio, r , as the fraction of removed weights, namely

CORE 1330–1730 的 scalar Eq4/5/6/7 与 vector-output 完整原 TeX；scalar E[∂b y]^2 不自行改成 E[(∂b y)^2]：
\displaystyle\begin{aligned} \Delta y(x;\theta,i,j,\ell,\Delta b_{ij}^{\ell})\approx\delta y(x;\theta,i,j,\ell,\Delta b_{ij}^{\ell})&\coloneq y(x;\theta)-\left(y(x;\theta)+\partial_{W_{ij}^{\ell}}y(x;\theta)(0-W_{ij}^{\ell})+\partial_{b_{i}^{\ell}}y(x;\theta)\Delta b_{ij}^{\ell}\right)=\\
&=\partial_{W_{ij}^{\ell}}y\>W_{ij}^{\ell}-\partial_{b_{i}^{\ell}}y\>\Delta b_{ij}^{\ell}.\end{aligned}
\displaystyle\mathcal{I}_{W_{ij}^{\ell}}=\min_{\Delta b_{ij}^{\ell}\in\mathbb{R}}\mathbb{E}_{x}[\delta y(x;\theta,i,j,\ell,\Delta b_{ij}^{\ell})^{2}].
\widetilde{\Delta b_{ij}^{\ell}}
\displaystyle\frac{\partial}{\partial\Delta b_{ij}^{\ell}}\left(\mathbb{E}_{x}[\delta y(x;\theta,i,j,\ell,\Delta b_{ij}^{\ell})^{2}]\right)=\mathbb{E}_{x}\left[\left(\partial_{W_{ij}^{\ell}}y\>W_{ij}^{\ell}-\partial_{b_{i}^{\ell}}y\>\Delta b_{ij}^{\ell}\right)(-\partial_{b_{i}^{\ell}}y)\right],
\widetilde{\Delta b_{ij}^{\ell}}=\frac{W_{ij}^{\ell}\mathbb{E}_{x}\left[\partial_{W_{ij}^{\ell}}y\>\partial_{b_{i}^{\ell}}y\right]}{\mathbb{E}_{x}\left[\partial_{b_{i}^{\ell}}y\right]^{2}}.
\widetilde{\Delta b_{ij}^{\ell}}
\displaystyle\mathcal{I}_{W_{ij}^{\ell}}=\mathbb{E}_{x}\left[\left(\partial_{W_{ij}^{\ell}}y\>W_{ij}^{\ell}-\frac{W_{ij}^{\ell}\mathbb{E}_{x}\left(\partial_{W_{ij}^{\ell}}y\>\partial_{b_{i}^{\ell}}y\right)}{\mathbb{E}_{x}\left(\partial_{b_{i}^{\ell}}y\right)^{2}}\partial_{b_{i}^{\ell}}y\right)^{2}\right].
\displaystyle\mathcal{I}_{W_{ij}^{\ell}}=\mathbb{E}_{x}\left[\sum_{k}\left(\partial_{W_{ij}^{\ell}}y_{k}\>W_{ij}^{\ell}-\frac{\sum_{k}W_{ij}^{\ell}\mathbb{E}_{x}(\partial_{W_{ij}^{\ell}}y_{k}\>\partial_{b_{i}^{\ell}}y_{k})}{\sum_{k}\mathbb{E}_{x}[(\partial_{b_{i}^{\ell}}y_{k})^{2}]}\partial_{b_{i}^{\ell}}y_{k}\right)^{2}\right].

## 2602.20549v1
https://arxiv.org/html/2602.20549v1

S3.SS2.p2.1 | A proof of these bounds is displayed in Appendix A.1. The lack of the measurement {\bm{y}} in the high noise estimator bounds the worst possible case, where the data is weak; when the measurement contains a lot of information, the variance would be much lower. As such, \Theta_{high} is used more towards the beginning of the sampling process while \Theta_{low} is used towards the end. As both estimators are cheap to compute, we can simply evaluate both and choose the lower variance estimator at each timestep. Finally, as we want an unbiased estimate of the squared likelihood score, squaring the estimator is biased: \mathbb{E}\|\Theta\|^{2}=\|\mathbb{E}\Theta\|^{2}+\text{Tr}(\mathrm{Cov}(\Theta)) . Therefore, for each intermediate sample {\bm{x}}_{t} , we propose to sample two i.i.d \tilde{{\bm{x}}}_{0}^{(1)},\tilde{{\bm{x}}}_{0}^{(2)}\sim p({\bm{x}}_{0}\mid{\bm{x}}_{t},{\bm{y}}) , giving us the following unbiased estimator: \Theta(\tilde{{\bm{x}}}_{0}^{(1)})^{T}\Theta(\tilde{{\bm{x}}}_{0}^{(2)}) . The full method is displayed in Algorithm 1, and a visualization for both in-distribution and out-of-distribution measurements is visualized in Figure 1.

S4.SS1.p3.1 | Unlike DiME, DiME-PnPDM only performs well for roughly in-distribution tasks. For out-of-distribution measurements {\bm{y}} , while the PnP-DM marginals asymptotically anneal to the correct posterior, we find that in the finite-step case this annealing path results in greater bias than DAPS. Because out-of-distribution measurements frequently arise in model selection, we conclude that PnP-DM is less well suited for this task.

S5.SS0.SSSx1.p1.1 | Our method is a statistical estimator and can occasionally select the incorrect model, potentially leading to incorrect conclusions. Furthermore, while it could in principle be applied to sensitive characteristics (e.g., facial recognition), we do not support its use in this context.

CORE 2394–2441 两个条件 iid draws 与平方 score 偏差的完整原 TeX：
\mathbb{E}\|\Theta\|^{2}=\|\mathbb{E}\Theta\|^{2}+\text{Tr}(\mathrm{Cov}(\Theta))
\tilde{{\bm{x}}}_{0}^{(1)},\tilde{{\bm{x}}}_{0}^{(2)}\sim p({\bm{x}}_{0}\mid{\bm{x}}_{t},{\bm{y}})
\Theta(\tilde{{\bm{x}}}_{0}^{(1)})^{T}\Theta(\tilde{{\bm{x}}}_{0}^{(2)})

## 2602.20593v1
https://arxiv.org/html/2602.20593v1

S3.SS1.SSS3.p1.1 | During the training phase, the attacker trains a bottom model following the protocol, which involves sending embeddings to the active party and receiving backpropagated gradients. The attacker may attempt to infer the labels of the training samples using legitimately obtained data and record the embeddings corresponding to these labels. During the inference phase, the attacker can choose particular source samples for sending malicious embeddings to the active party to facilitate a backdoor attack.

S3.SS3.p1.1 | Since the VFL model is distributed among participants, the active party, possessing only a part of the entire model, cannot independently complete the main task during the inference phase. This obviates the need for trigger implantation. Our intuition for implementing backdoor attacks in VFL is to directly replace the original embeddings with those corresponding to the target label. So that the top model of the active party can be misled to make wrong predictions.

S5.SS4.p2.1 | In addition, we observe that anomaly detection defense strategies based on embedding magnitude are insufficient to counter our triggerless attacks on complex datasets. We believe these defenses still face several unresolved challenges. For example, directly identifying malicious embeddings by comparing differences between passive parties may not be reasonable: 1) passive parties may collude, making it difficult to assess their trustworthiness; 2) natural variations in feature distributions [27] and bottom model architectures across passive parties result in highly diverse embedding representations, leaving no consistent standard for comparison. Moreover, comparing embeddings between the training and inference phases offers limited effectiveness, as the distributions of training and test sets may differ, and certain highly distinctive samples may naturally have representations outside the expected range. Therefore, efficiently identifying malicious embeddings without affecting benign ones remains a significant challenge. In summary, our future work will focus on developing defense strategies capable of effectively countering backdoor attacks during the inference phase, particularly in complex real-world VFL scenarios.

## 2602.20629v1
https://arxiv.org/html/2602.20629v1

S3.SS3.p2.1 | Initial rubrics were synthesized by GPT-5.2 Pro and verified by Gemini 3.0 Pro. Crucially, human experts then iteratively refined these drafts to align them with their own evaluation and grading standards. Figure 1 illustrates the differences between these two standards for a graph theory problem. Humans evaluated the proofs using the Expert Rubric, while LLM judges evaluated the proofs using both rubrics.

S4.SS3.p2.1 | We compared human-evaluated mean scores and strict pass rates (score \geq 0.9 ) between these two groups across the five frontier solvers (see Table 2 and Figure 7). The empirical difference in mean score between online and offline problems is +0.017 , while the corresponding pass rate gap is +0.011 (online problems exhibiting a marginally higher pass rate). Neither metric reveals a statistically significant advantage for problems with online solutions (Welch’s t -test using N=1070 model-problem pairs: t=0.99 , p=0.32 ; Mann–Whitney U test: p=0.80 ; Cohen’s d=0.06 ).

S4.I9.i1.p1.1 | Expert Rubric: Pearson correlation r=0.69 , Mean Absolute Error (MAE) =0.13 .

S4.I9.i2.p1.1 | Course-Specific Rubric: Pearson correlation r=0.67 , Mean Absolute Error (MAE) =0.14 .

S5.SS1.p3.2.1 | “This solution fails to correctly define the plane dual G^{*} of a plane graph G , which among other properties, requires that the number of faces of G^{*} equals the number of vertices of G . It is precisely this property that requires the assumption that G is connected. The solution however is independent of this assumption.” (Human Expert, Graph Theory 14)

S5.SS1.p3.3 | However, the LLM evaluators failed to appropriately penalize the missing connectivity requirement. For instance, GPT-5.2 Pro awarded the proof 0.75/1.0 , noting incompleteness but still granting substantial credit:

S6.p5.1 | Limitations. Our study is limited by static expert ground truth, which may exclude valid non-standard proofs, and by its focus on English-language reasoning. We also acknowledge a potential “self-preference bias,” as GPT-5.2 Pro was utilized in synthesizing the final expert rubric criteria, which may positively skew its own evaluation scores. However, the rubrics are not identical to what GPT-5.2 Pro would produce on its own since we asked our expert evaluators to iteratively modify the rubrics to match their evaluation. Additionally, while we identify sycophancy in reward models, quantifying the downstream “poisoning effect” of training on these signals remains future work.

## actual owner — books/part-01-worldview/05-what-neural-networks-learn.md

L389–394:
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22417:start -->
归因图若不声明 reference，只能解释当前 input 相对某个隐式 baseline 的差异，不能给出“这个 feature 绝对贡献了多少”。一个可复核的 attribution artifact 至少要冻结 input reference、该 reference 实际诱导的 output baseline、当前 output target、积分 path/step 与 model revision；attributor 分配的是 `F(x)-F(x')`，evaluation 再用 attribution error、受控扰动、干预与行为结果检查，而不是让热力图或人类相似度拥有 causal truth。

显式 reference 使结论可审计，却增加 baseline 构造、path integration 与 variable-output matching 成本；多个同样合理的 reference 也可能产生不同解释。All-zero 只在输入语义和训练分布允许时才可能是便宜基线，不是跨模态的通用“无信息”状态。Reference off-manifold、输出无法稳定匹配或多组 baseline 结论漂移时，应把结果降级为 reference-conditional observation，并回退多 control、perturbation、causal intervention、外部行为与重复实验。现有证据只支持论文披露的 DETR/VGG 案例与误差分析，不证明选定 baseline 中性或归因具有因果唯一性。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22417:end -->
<!-- source-family:SF-2026-ARXIV-2605-22417 -->

L491–492:

预测依赖什么时候能支持因果结构，也需要先声明生成过程，而不是从模型名称取得因果解释权。对于滞后时间序列，在条件外生性、无同期作用、窗口覆盖全部父变量、faithfulness 和正则条件下，真实条件分布对某个历史变量的 score-gradient energy 可以识别对应滞后边；理论允许任何足够拟合该分布的模型，并非 Transformer 专有。只有同方差 Gaussian 等附加条件才把它收窄为条件均值梯度；用 MSE 训练并以 LRP 提取 relevance 又是实践代理，不能把普通 attention 权重或低预测误差直接认证为因果图。[受限理论与仿真](https://arxiv.org/html/2601.05647v1)支持这条条件链，却未解决任意潜在混杂、同期作用与窗口遗漏。拟合、归因校准和图判定均有额外成本；假设不成立或代理不稳时，保留预测/关联诊断，另做受控干预与因果检验，不把模型结构升级为因果保证。

## actual owner — books/part-06-ai-infrastructure/72-security.md

L184–189:

同样，取证与预防不应共用一个成功标签。权重 watermark 在有限后续 fine-tuning 中可保留归属信号，但不阻止外传，也未证明能抗有意移除。周期改变 Q/K 权重的函数保持旋转，则要分清 attention-score 乘积的稳定基与仍随旋转变化的单个权重：原研究只演示单层可用参数恢复，不能据此保证全模型片段可拼接，也不能保证 moving target 已封堵外传。这些分支增加转换、检测、恢复和审计成本；能力超出已测假设时，应保留访问隔离与独立泄漏监测，而非用局部水印或旋转试验授予完整 confidentiality claim。<!-- source-family:SF-2026-ARXIV-2601-01296 -->

生成系统的水印持久性还取决于信号落在哪个可替换组件。将 latent 水印蒸馏到 decoder，能让该解码路径自动带信号；若接收者可公开替换 decoder，就能绕开这条路径。将信号蒸馏到 generator 则改变另一份权重的责任，却仍可能在后续非水印 LoRA 适配中遗忘。Generator、codec/decoder、message、detector 与后续更新身份应一同记录，不能把一处组件的检测结果继承给完整 lifecycle。训练与检测、输出质量回归都须付费，有限 augment 下的 bit accuracy 也不是 authentication、合法所有权或抗有意移除证明。需要强制来源验证时保留签名/制品血缘与访问控制，不用水印取代它们；[受限 latent 水印实验](https://arxiv.org/html/2601.16140v1)只支持该部署位置与持久性的取舍。<!-- source-family:SF-2026-ARXIV-2601-16140 -->

当输入与密钥独立、目标只是低误报筛查时，水印的 soundness 仍是合理的 sensor 责任；但攻击者若能观察带水印输出或访问验证结果，就需要另一个不可伪造责任：检测通过的文本，至少应在约定距离内对应攻击者曾观察过的某个输出片段，而不是仅在随机输入上少误报。恢复也有两个方向：恢复列表包含原片段，不等于列表中的每一项都可信。前者是 recoverability，后者需要单独的 unforgeable recovery；高恢复率不能替代对伪归因的控制。这些责任约束可检测或可恢复的片段，不自动认证整篇作者、法律所有权或完整生成生命周期。

L97–114:
Training
  untrusted code, secret exposure, compromised dependency

Artifact
  overwrite, substitution, unsafe deserialization, model theft

Serving
  auth bypass, DoS, side channel, data exfiltration

LLM/Agent
  prompt injection, insecure output handling, excessive agency
```

单一 WAF 无法覆盖这条链。每次从一层向下一层传递，都需要验证 identity、integrity 和 authorization。

Data poisoning 不必依靠显式 trigger：错误事实经过 continued training 后，直接 factual answer 与依赖它的 downstream decision 可能不同步。安全评测应配对 false/true 数据训练，保留 unaffected clean controls，并分别检查事实输出、派生决策及一般遗忘；表示 norm 或 probe 不能代替实际行为。[受限事实投毒实验](https://arxiv.org/html/2610.02886v1)支持这两层对象分账，不提供真实组织风险率或普遍不可修复性。<!-- source-family:SF-2026-ARXIV-2610-02886 -->

纠正后还须给 clean 模型相同预算的 correction，再用 difference-of-differences 区分普通 continued-training 变化与投毒残余。Replacement 分支可能恢复直接事实却留下 derived failure，added-false 分支则大多恢复；不能只验一条事实便批准 artifact，也不能把一个失败推广成所有修复无效。配对训练、corrective replay 和下游重测增加成本；证据或恢复不足时隔离可疑数据/模型并回退可信版本，保留原 provenance 与干净行为基线，而非由单次 probe 代替发布权限。

L2123–2125:
即使原始输入留在 client，split inference 仍会把 intermediate activation 暴露给 server。旧的“在本地跑前几层即可隐藏输入”只在 activation 对攻击者确实不可逆、split point 与模型固定时成立；server-visible tensor、layer identity、shape/precision 和 auxiliary knowledge 变化后，activation matching/inversion 可以把中间状态重新关联到输入。client 拥有原文与允许的 split policy，server runtime 只拥有执行所需 activation，security plane 则必须测试每个候选 split point 的可重建性并记录 attacker capability。更深本地计算或 activation protection 能降低暴露，却增加 client compute、带宽、精度损失与部署复杂度；风险无法校准时回退本地完整推理、TEE/MPC 或可信服务端。`arXiv:2605.23158v1` 的 §3、§4.1 至 §4.4 支持作者 threat model、ActInv 与受测重建结果，§5.3 不证明未测试模型、split point、数据或防御同样泄漏或有效。

<!-- source-family:SF-2026-ARXIV-2605-23158 -->

## actual owner — books/part-05-inference-system/49-tensorrt-llm.md

L509–513:
选择可执行稀疏 pattern 之前，局部剪枝目标本身也需要明确：保持 layer output 的重构损失与基于校准样本梯度的 empirical-Fisher 损失，不一定给出相同的重要性排序。一种离线分支先分别按全零权重下的损失归一化，再加权混合两者；在行或 block 近似中，重构项提供共享的输入二阶矩基底，样本梯度项提供低秩修正，因而可用 Woodbury 更新复用共享逆矩阵。这里精确的是所选近似矩阵的求逆关系，不是全模型 Hessian 或全局最优剪枝；empirical Fisher 的近似还依赖参考点梯度等条件，混合权重改变或共享基底不可逆时，不能照搬同一求逆路径。<!-- source-family:SF-2026-ARXIV-2604-13287 -->

这个分支把 calibration loss、归一化基准、混合权重和 block 划分纳入稀疏 artifact 的身份，用额外梯度采集、矩阵状态与超参数选择换取更丰富的敏感度信号。作者在 LLM attention 与其他受测层上的目标选择并不相同，部分 2:4 结果也退步，因此不能把混合目标写成普遍优于单目标，更不能由离线质量推出 runtime 加速。校准证据不足、低秩近似不稳或质量 Gate 失败时，应回退单一重构目标、更保守的剪枝或稠密权重；冻结 artifact 后的布局与 kernel admission 仍独立验收。

校准输入的生成时钟也会改变离线 importance：AR 中长期稳定的 prefix sink 经验，不能直接迁移到各去噪步输入不同的 diffusion model。一条[noise/time-conditioned 剪枝分支](https://arxiv.org/html/2602.17664v1)在多组加噪校准时刻汇总各层/各 head 的 attention mass，得到跨步平均 soft-sink score，再以其补数重权 activation rows，用于原 importance norm 或重构二阶矩；冻结后仍交付权重剪枝 artifact，不是在请求期间删除 token。平均 soft-sinkness 不是按 temporal variance 选择位置，attention mass 也不是 semantic importance 真值；它改变的是校准统计，不能由此宣称所有 sink 无用。相同 WikiText-2 的128条、长度2048校准及既有 Wanda/SparseGPT 协议提供有限对照，但 LLaDA1.5 的75% SparseGPT平均质量仍反退，低稀疏度也有退步。多时刻前向与 attention map 采集增加离线成本，硬件、precision、完整 runtime 和 timestep 采样细数未披露；稀疏率不替目标 kernel 或服务 SLO 验收。noise schedule、输入域或统计支持改变时重新校准，质量失败则回退原校准/更保守剪枝或稠密权重，不能把生成范式差异写成普遍压缩保证。<!-- source-family:SF-2026-ARXIV-2602-17664 -->

L1038–1042:

固定原始浮点输出后，还要问输入量化误差中哪些部分能由本层权重补偿。冻结校准输入及变换，记量化后的输入矩阵为 Z̃，它的列空间投影为 Π；相对于最小二乘补偿权重，输出误差可精确拆成落在该列空间中的权重拟合误差，以及与其正交的输入残余。后者对这个固定输入矩阵不能靠继续改变权重消除；前者的无约束最优也未必落在低比特可表示集合内。因此补偿搜索与改变输入表示是两种自由度，不应把所有残余都交给更宽的权重搜索，也不把一次最小二乘解当作低比特无损保证。

选择输入变换时，persistent outlier 与普通通道统计可分别进入残余上界；据此选择符号旋转和缩放，是界引导的校准分支，不是精确误差再多出两个独立项。L2 与最大幅度缩放来自不同放宽，实际以完整输入近似普通通道统计也须另验；无 clipping 的理论条件不能静默继承给带 clipping 的实验。更低 perplexity 并未使所有任务准确率更好，候选旋转、teacher/scoring 与补偿筛选均付校准成本，低位模拟结果不证明目标 kernel 更快。统计失配、下游质量回退或执行成本不合适时，保留原始目标补偿、较简单变换与更高精度。 [必要机制与反证](https://arxiv.org/html/2609.21450v1)。<!-- source-family:SF-2026-ARXIV-2609-21450 -->


## actual owner — books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md

L156–162:

Gaussian 噪声下，posterior mean 足以把平均残差换成 marginal score，这解释了平方去噪回归为何是合理接口；改变噪声分布后，这份充分性不自动保留。对可归一化、具有相应可微与可积条件的 elliptical noise，一条替代分支从 posterior 平均 noise log-gradient 求 score。若噪声由形状参数 β 与尺度矩阵 Σ 定义，求值残差的 energy 必须与它们匹配；β=2 的 Gaussian 情形退化为 mean residual，非 Gaussian 情形通常需要整个 posterior 的加权残差期望，而不是把原 MSE mean 直接代入。所谓 path derivative 在这里固定 posterior measure，只对残差函数的求值位置求导，不能连同生成 posterior 的路径一起微分。<!-- source-family:SF-2026-ARXIV-2512-23818 -->

这个接口让 noise law、posterior learner 和 score 求值分别接受核验，没有消除学习或采样成本。训练必须覆盖部署所用的噪声参数族；有限 posterior samples 引入 Monte Carlo 误差与额外调用，求解器仍有积分误差，零残差处不光滑的 energy 还需检查定义和可积条件。受限二维分布实验及其近似参考不证明任意模型质量更好，也不把非 Gaussian 更新升级为通用 reverse SDE。posterior 失配、样本预算不足或净收益未验收时，保留 Gaussian mean/MSE 接口与原有 sampler，而不由一个能量公式批准任意临时换噪声。

若 posterior mean 直接由经验数据逐点加权计算，读取支集又成为独立于求解步数的预算。高噪声时权重较分散，需要较广的 aggregation，但粗筛可更宽松；低噪声时权重可集中，aggregation 可以减少，却更怕漏掉真正近邻。一条受限分支仍先扫描全部数据的低维 proxy，随噪声下降扩大精确比较的候选池、缩小最终加权支集，分开召回精度与聚合数量。[必要方法与反侧](https://arxiv.org/html/2602.16498v1)的误差界针对真实 posterior logit 的 top-k 与有限数据半径，不证明 proxy 已召回该集合，也不把较宽上界变成高噪声必须全扫的下界。低维全数据扫描、样本驻留、近邻筛选与有限步求解仍付费，经验 exact score 在低噪声还可能记忆训练样本；相对 U-Net oracle 的局部 MSE 改善并非未知真 score 或生成泛化的保证。召回或近似质量不足时，保留更广支集与已验收神经 score，不照录与数据量解耦或逐 step 加速为端到端收益。<!-- source-family:SF-2026-ARXIV-2602-16498 -->


## actual owner — books/part-06-ai-infrastructure/66-evaluation-system.md

L124–126:
把生产轨迹的人工结果用于训练 critic 时，还必须对齐标签与被判断的对象：整个 PR 被合并，不代表其中每一段对话成功；最后保留下来的代码比例，也只是受后续修改影响的代理，不是每个 segment 的正确性。过程 rubric 可以提供更细的辅助监督，但它仍可能由模型标注并继承代理偏差。EvalSpec 应记录标签生成链、轨迹粒度、缺失标签与人工/模型判断的分工，并单独验证 critic 从 benchmark 迁移到真实 workflow 后是否仍有效，而不是把“有人类结果”当作无噪声真值。

多标签训练也不保证收益叠加：不同 loss 与目标代理会改变 transfer，排序分数提高更不能直接推出在线尝试数下降。[RubricCritic v1 §2–5](https://arxiv.org/html/2603.03800v1)既给出真实任务选择收益，也观察到 benchmark-only critic 的弱迁移和 rubric 在部分 loss 下退化；其尝试数比较只覆盖筛出的 mixed-outcome 子集，不是全部任务的成本保证。新增标签、校准和 critic 调用都要计入预算；标签粒度失配、迁移失败或干预净值不明确时，保留简单目标、独立执行验证与人工裁定，介入价值的具体计算由 Ch80 承接。<!-- source-family:SF-2026-ARXIV-2603-03800 -->

L309–310:
Judge 自身的 task competence、directional bias 与对更强 examinee 的 leniency 也必须拆开测。能力较强可能提高 judging accuracy，却不会消除系统性宽松或偏向；无标签 disagreement 只能生成待校准状态，不能替代人工 anchor。Route/defer 更不能读取 verbal confidence 直接决策，而应比较模型相对外部 prior 的边际 proper-score 收益；先验更强或 domain 漂移时，保留 crowd、market、rule 或人工分支。

