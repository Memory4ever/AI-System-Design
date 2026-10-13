# 第二批必要Source作者packet B

root8项AB潜力已核；以下三篇必要Source ready、未写Books/未自授Source PASS。00012新增早全文反证另隔离，不因审阅成本删除候选。

root实际已核00208 Gram/asymptotic与compression、fixed-m overlap及稀疏RIP资格；00770 joint训练、Prop1仅existential与cleanFT可擦；00072 r=m/L domain/margin/估计L及expandedoracle Safe-at-end No(.98)。三篇受限Source与拟分数通过，尚待具体owner差额/PRE，不授Books锁或DAY；无需全文/全部附录/复现。

## 2604.00208：superposition alignment，拟3+1+3=7

[v1](https://arxiv.org/html/2604.00208v1) §2/3.1–3.5/4.1–4.2/5必要已读。y=Az、i.i.d zero-mean identity-cov latent、独立随机projection下，RSA/linear CKA/linear regression同时依赖mixing geometry；相同feature也可低alignment，跨不同compression的排序可反转。**固定dimension下overlap仍单调**，不是同配置feature越少就必越高；ratio-of-expectations需concentration/渐近，不冒称任意有限网络exact期望。信息仍可恢复另需sparsity+RIP与足够m，不能从低CKA说已丢信息，也不能说所有superposition都无损。

synthetic1000-feature/8192sample及尺寸/sparsity扫只验证该构造，未证明实际LLM raw feature满足白化、线性或RIP。新选择是比较latent feature与compression几何分账，而非拒绝所有CKA；feature提取、随机投影估计与独立任务验证仍有费用，不授能力/causal equivalence。读到理论资格与直接排序反側即止，无需所有推导附件。

## 2604.00770：latent backdoor，拟3+2+2=7

[v1](https://arxiv.org/html/2604.00770v1) §4.1–4.5/5.1–5.6/6及必要Table4/20已读。攻击训练joint优化trigger embedding和全部weights，不是部署时任意单embedding扰动无需训练；bake-in row、lexical token触发正常lookup，经latent multipass影响输出。Coconut/SimCoT124M–3B有限数据，五active defense失败不等所有防御。无trigger knowledge centroid/kmeans/readout失败；known population contrast部分层盲点；oracle labeled probe1.0不授黑盒线上sensor。原文另给reference embedding-row drift inspection为简单防御，不能说结构上不可监测。

Proposition1只保证linear readout、ASR/CA均>0时至少一对triggered/clean最终latent可线性分开，**不是所有population AUC≥.999定理**。NC1/ASR在Table6不锁步，geometry因果解释保为作者局部证据，不扩大必然吸引子；lr1e−4/weight decay.1可清后门，‘25epochs必存活’不成立。保攻击训练、reference artifact/hidden access、label、诊断校准与clean-utility成本；停在真实threat/observer/反側，不全附件或code。

## 2604.00072：ball verifier，拟2+2+2=6（安全影响深入）

[v1](https://arxiv.org/html/2604.00072v1) §2/4.4–4.6/5.1–5.8/6.3及B.1–B.2/A.12必要已读。binary classifier理论有absolute-continuity、finite-Renyi、per-step error多项式衰减资格；18classifier finite实验不证明所有classifier本质不可能。球门依赖当前domain安全margin与有效Lipschitz上界r=m/L，cheap normcheck只复用该ball条件；chain换中心仍需重新oracle/margin/L，不能承诺unbounded现实安全改善。

直接反側：constrained chaining五seed一seed6false accepts；50prompt oracle比10prompt多检20violations，Table5.7.1 Safe-at-end No(.98)，不把‘oracle-agnostic’写成生产保证。LLM Qwen2.5-7B rank4 q/v LoRA、4bitNF4/BF16、200steps、finite-difference L估计+factor，不是analytic certified bound；domain有限、无adversarial mutation分析、margin可缩至零。只采用estimated region/cheap check/reverify分责及oracle/上界失配风险，不采用unconditional LLM delta0、普遍分类不可能或零告警=安全。margin/oracle调用、L校准、normcheck与重验费用都保留，旧独立安全评价仍需保。

## 2604.00012：更早正式全文反证，非作者日期出口通过

必要core阅读发现‘during rebuttal’信号，定点查到[NeurIPS2025官方同title/作者/完整摘要](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4568accb98552886fdfceb194deee663-Abstract-Conference.html)，[官方完整Paper](https://proceedings.neurips.cc/paper_files/paper/2025/file/4568accb98552886fdfceb194deee663-Paper-Conference.pdf)首面明确39thConferenceNeurIPS2025、DOI10.52202/085713-1620。OpenReview pcG6NRJKu7 forum/API403 challenge，返回ChallengeRequiredError而非空notes，未绕验证。已有更早正式全文信号不能被MM04+registered上界覆盖；不按Apr02首次公开评分/入Books，未见Apr02重要修订标记。精确最早日仍未恢复，不伪造2025时刻，也不扩2025报告。已读安全core及utility小退保留作恢复线索，不等零价值或贡献EX。root实际读NeurIPS2025官方同title/authors完整摘要与DOI页面，确认更早正式全文明确反证，本具体日期出口独核通过；403非零，不扩完整revision史。
