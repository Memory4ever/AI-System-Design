# ARGENT23311 — 必要Source / 两PRE

作者supp_mar26_fresh；完整题摘/date25/2+1+3=6由reader独校通过。实际exact-v1 https://arxiv.org/html/2603.23311v1 §3–7/Eq1–9/T1–3及因预算必要定点Additional Training段已读，不无差别全附件。

## 原证限定

Lorentz双encoder保留对比目标，同时学习general→specific顺序；原cone aperture arcsin的domain要求parentnorm≥2C/√κ，clipping到半空间可使方向loss失去信息。新目标不计算aperture，改直接Huber(angle)；跨模态权重1，同模态以1−exp(−distance)降低近似pair权重；norm²−log(norm)防过近/过远并非语义真值或所有hyperbolic任务稳定性定理。相同类别可共享抽象但相似≠entailment，crop/full也不总严格is-a。

GRIT20.5M、CLIP224/patch16/text77、S/B/L；500000iterations/globalB768约384M样本，1–6H100/AdamW；precision、seed区间、线上concurrency/SLO未披露。HyCoCLIP额外box但其余图文，不能算所有baseline同信息；T2 ARGENT-S平均分类38.4低HyCo39.2，size增大AP下降。CC3M40000iterations/30M的必要T3同hyperparams控制：AdaEnt小模型分类也可降，给全部pair adaptiveweight严重损PEP，regularizer指标亦非处处支配；几何目标、权重位置和regularizer共同改，不授唯一因果或普适无损。

评价S5/T1提出global negatives可能有效caption、rank不反映margin；去相似负例提高检索也可能因候选更容易，不能独证removed全部false-neg。Qwen3VL模型辅助从1000筛522和100low-retrieval negatives改变人口；Eq9角度到[0,1]只是score mapping，AUC/AP不授概率calibration或客观hierarchy真值。新目标与新评分都有angular inductivebias，应另验heldout语义/原任务。encoder/对齐、geometry和norm调参、caption筛选/judge/embedding/reranking、回归都付费，非免费改loss。

## Actual owner与差额

actualCh23对齐763–775前LiteEmbed新token邻域、09771原visual softprompt、07474视觉taxonomy/projector泛化完整段落已读；这些没有cone domain/clipping→direction objective→intra/interweight分责的训练接口。Ch22历史/状态不是对齐geometry，Ch24开篇概率/commit不接管理解encoder的语义顺序。唯一MULTIMODAL-REPRESENTATION Ch23，拟07474完整原段之后、Caption不对称辅助证据标题之前；保原CLIP/Euclidean对比和taxonomy监督，不新增ARGENT收纳节。因为新机制长期差额明确，6分标准完成后也提出必要Books两段，未因评分强制或避免Books工作。

## 两段逐字PRE（未写）

跨模态相似还不能代替“哪个概念更一般”的方向关系。若选择双曲表示，以 general embedding 的 entailment cone 约束 specific embedding，parent norm 接近原点时会触及 aperture 的定义域；直接 clipping 成半空间，可能让方向目标退化。另一条训练分支保留 image–text 对比目标，改为直接惩罚 exterior angle，只对同模态近似 pair 减轻方向约束，再用 norm 正则限制表示过近或过远；跨模态 pair 不沿用同一减权规则。这改变的是几何目标和监督配对的合同，不是证明双曲空间自动拥有语义层级。<!-- source-family:SF-2026-ARXIV-2603-23311 -->

[受限层级图文对照](https://arxiv.org/html/2603.23311v1#S6)中，对全部 pairs 减权会损伤跨模态约束，分类和层级指标也不总同步改善；角度映射到零一之间只是 score，不是校准后的 entailment probability。全局检索的近似有效 caption 与 taxonomy/清洗模型会改变评价人口，不能由删去相似 negatives 后得分上升批准全部删项确为假负例。应绑定 geometry、pair 方向、减权域、norm/loss 权重与 evaluator，并分别回归原分类/检索和独立层级判断；编码、额外训练、标签清洗和调参全付费。配对或几何不成立、原任务回归或费用不合算时，保留原 Euclidean 对比表示、真实 taxonomy 监督和专用 readout，不让向量位置自签语义真值。

本人静态注拟：`SF-2026-ARXIV-2603-23311 exact-v1 §3–7/Eq1–9/T1–3及必要training预算；仅cone domain/方向loss、intra/inter减权和norm分责，不采双曲普适层级/全任务无损、PEP概率calibration或清洗为独立真值；保Small分类/AP与减权反侧、信息人口/全部训练评价费用；未核代码/复现。`

必要Source/actual差额与两PRE/本人注已真实独核PASS；待root具体Books窄锁，无写入/POST/DAY。
