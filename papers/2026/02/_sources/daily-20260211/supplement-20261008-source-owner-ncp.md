# NCP08984：必要Source/owner判断请求

Next Concept Prediction in Discrete Latent Space Leads to Stronger Language Models，2602.08984v1；2+2+2=6，chunk-level软codebook读出+next-chunk连续监督与token CE并行的具体目标/模型接口深入。root完整AB/日期已过；ncp-core.json完整§2–5实际读，ncp-direct.txt必要B/E.2–3配置与collapse反侧。无artifact/复现，不修全文。

§2 encoder token states邻近mean pool k4，S=attention heads分段64-entry codebook，2-layer concept Transformer，各段预测权重加权codebook向量再concat，broadcast到token decoder addition；VQ只训练时quantize，线上不是逐chunk硬采样、不替代token AR也不拥有语义标签。§3 NCP MSE到next continuous pooled state，与token CE/VQ联合；target由encoder共同训练非外部concept truth。表述称VQ strictly confined不影响representation，但明列beta||c−sg(d)||²按公式对c有梯度：若beta非零且c未额外detach，2beta(c−sg(d))非零；必要正文/B没给额外detach/zero-beta。该无representation影响保证隔离，不采用实际gradient routing已核。

§2.3 causal文字说broadcast k次再向后k−1，数学却以floor(t/(k−1))索引，按broadcast周期应是k而非k−1；k4则每3位置换concept与每4位置广播冲突，NTP条件重复该索引，decode公式< t/≤t亦不统一。不能据公式授已实现无leak或prefix exact；只保作者提出需shift避免未来块target进入前缀的接口意图。两项隔离如需重开，只需作者修正规则/精确实现—not whole proof or all code。稿中新机制可仅用定性target+训练/线上分责，是否可Books请root裁决。

§4 GPT2 OWT8B/124M–1.5B、Pythia Pile300B/70–410M、Llama3.1-8B LongCtx9.6B，lm-eval harness.4.4。GPT PM加2token layers不匹配codebook<2M，ContextLM不同预测objective baseline但Pythia数值引已有paper非fresh全部同engine复测。Tables1/2有LambadaStd XL Concept47.06>Context44.62 PPL退步，Pythia70/410Pile15>14.96/8.70>8.67；不是全task全winner。8B T3 avg47.6 vsPM47.2/Trained47.5，SQuAD36.5<Trained36.7，未披露重复CI，.1–.4avg不授统计显著。

§5T4单独NCP avg39.5<CE39.6，单独VQ AvgPPL75.64>69.28，joint68.13/acc40.3，支持joint条件而非NCP必然优。T5 +2token PPL各点12.77/34.02/37.94/200.67算均值71.35但表列59.80，与concept68.13方向冲突且写+3.22；按各点均值差3.22可解释摘要平均栏笔误，不采用表59.80或未核绝对summary。+6/10局部不同downstream退步，不授深层bottleneck唯一原因。

§5.5 Llama8×H200训练PM80h vs71h，SQuAD99minvs86，B5 b96/len8192/lr1e-5；precision/inference input-output/batch/concurrency/SLO/repeatedruns ND，IO原因没有直接profile，4.69%仅排embedding/head且concept overhead公式估算，不能称全serving/quantization near-zero。B/E2 layer3/4-depth best PPL取自单160M30B slice，downstreamL0 avg40.5>L9 40.4，不能授总质量最优。E3非线性2MLP/ReLU codebook避免观察到collapse，utilization近100不认证semantics/泛化。

actual TRAIN-PRETRAINING Ch28 140–166 token PPL/概念等价token集合目标/扰动正则，以及Ch27/29交接已读。概念等价token集合是当前位置外部等价label，总体token CE仍原读出；NCP是后续chunk内生latent监督+soft codebook旁路，不是同一机制。MODEL-LONG-CONTEXT无具体concept-target分支，唯一拟Ch28，接等价token段后、远前缀gate前，不另写Ch22。

拟最小正文（待Source/PRE与写锁）：目标粒度还可从单个词形扩到后续token块，而不取消词面监督。一个有界分支把相邻hidden states池化成训练target，用分段codebook约束下一块预测的可表达向量，再以各codebook的软加权组合辅助逐token读出；学习的是内生latent target，不是外部给定的语义概念，线上仍按token自回归。未来块状态只可作训练监督，辅助预测加入token前缀的shift/边界必须独立验收，不能把teacher target当线上已知。连续target、codebook拟合与token CE相互耦合，单独加一种loss仍可能退步；码本坍塌、插入位置与gradient detach规则也改变质量与费用。有限预训练/继续训练支持这种组合目标的局部取舍，不授语义真值、普遍缩放或完整serving加速；码本、因果边界或净质量/预算未核时保留原NTP、可信等价集与无此旁路的baseline。

请求root实际Source与两公式争议边界裁决，owner/PRE通过后再协调Ch28窄锁；当前未写Books。
