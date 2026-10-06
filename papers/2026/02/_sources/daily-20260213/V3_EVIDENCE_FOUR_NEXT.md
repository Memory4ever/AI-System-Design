# 10420/10425/10431/10449 必要证据与 Books 差额（作者判断，待非作者核）

全部采用2602.*v1 HTML精确事件；INITIAL/METHOD/必要PROOF与EVAL原文件同目录。准入已校准，不用这些笔记授全日完成。公开范围见 V3_DATE_INFERENCE；更早公开信号另核。当前官方AB轻量未见withdraw/correction标记，不遍历revision历史。

## 10420 Binary Flow Matching（5，必要理论定点加深）

III-D Eq3确实把x-prediction+v-loss变成(1-t)^-2残差平方权重；IV-A的parameter-Jacobian bounded/nondegenerate与IV.3残差速率是理论条件，不是任意network已证明性质。Appendix A连续Gaussian Bayes residual展开支持其特定分布下端点率；binary非消失误差直接引用Assumption IV.3，不能从“binary/finite Lipschitz”泛化必然发散。Appendix C中MSE bounded-gradient另外要求输出/target残差有界，BCE用logit Jacobian和sigmoid残差；不因取消显式时间系数授所有训练稳定。BCE和MSE都是逐坐标可分loss，原文“仅MSE维护全局相关而BCE必独立所以不适视觉”的解释不能普遍采用。

Toy §V/AppD 16维Gaussian/BPSK、batch1000、2×256 gated MLP、5000 Adam updates、uniform vsLogitNormal、x/v配对给局部梯度反侧；AppD output dim8与data dim16冲突，运行硬件/precision/seed Not Disclosed。BinaryMNIST TableI best-val-checkpoint，FID1247.98→4.94只是该协议，不把通信领域MIMO提升引入主线。拟OnlyReport：Ch24 126/159–176已具体绑定schedule/path/参数化与loss，新增的强“necessary/sampler-agnostic”普遍命题条件未建立；保留可核代数权重和有限实验，不静默排除已准入项，也不授通用理论Books。

## 10425 MOH（5D，受影响深入）

§3.2 GroundingDINO仅80 COCO classes/confidence.5，迭代detector→mask，target VLM每图10responses，masked实体至少5次出现才成为model-specific HII；§3.3再跨模型取intersection约800COCO2014 images形成MOH。故已选失败切片证明“没有实体视觉证据时场景先验仍可产生对象断言”，不估总体发生率/不保证detector mask完全删除所有线索。直接yes/no与description HR要分开。Preference另8kVisualGenome images且不同base图，same-prefix一句divergent响应DPO是已有组合不借分。

§4 Table2/3显示LLaVA7B HRD52.2/HRG68.6和13B69.5/67.9局部残留；处理后仍不是0且7B VQAv2 77.8低baseline78.5，13B79.5低80.0。不能把“up to92%/38%”当普遍保真无税。硬件/precision/多run/SLO在采用评价段Not Disclosed，采样evaluation10responses不是训练seed。Ch23现75–77分段probe是“信息可读/可访问/可表达”的正侧定位，没有移除实体但保留scene的反事实切片；拟窄整合该诊断分支与selection/detector限制，非DPO配方、非普遍语言prior因果。

## 10431 QTALE（5，若采用差额则受影响深入）

§3.1原D-LLM只约束平均执行率会固定跳某些层、routerlogit gap增长使Gumbel不再改路径；§3.3 entropy maximization保留训练path探索，§3.4global execute-prob threshold部署后回补执行率以吸收低bit误差。熟悉stochastic-depth/entropy本身不贡献，新增在“少执行→少误差冗余→PTQ质量税”的coupled control。Eq9第二branch写p1<theta而非执行p0<theta，文字意图清楚但数学branch不按原式发布为可执行算法。

§4 AWQgroup128 W3/W4，LLaMA2-7B/3.1-8B/3.2-3B，fine-tune hyperparams只引用D-LLM原文，完整training硬件/precision/总budget Not Disclosed，不重抓无关原论文。Table4 entropy/threshold消融显示PPL恢复常伴更多层执行：Llama2PPL4.43→3.74执行.61→.81；不是同FLOPs免费恢复。Table3单A6000 B4各任务256sample runtime W4QTALE18.2s比D-LLM17.8s更慢、FullW4比FP16更慢，不能从4bit/名义50%FLOPs授生产SLO。Ch49实际1687–1692既有动态depth+residentweights/KV边界，没有训练path diversity与PTQ error共同的部署threshold；拟窄整合coupled取舍，不采用Eq9错误branch与全场景加速。

## 10449 projected influence（6D，受影响深入）

§2.1+AppA L373–383实际证明：PSD F、g/g'在rangeF，unregularized projected bilinear精确保留iff P在rangeF injective。丢方向可构造Pg0而g^TF†g正，故JL有限向量距离保留不授inverse-curvature influence保证。§2.2实际推导lambda-whitened subspace→PSD sandwich→resolvent bound，ridge以effective dimension替代rank，只是相对于同一regularized influence的绝对双线性误差界，不是relative-to-small-score或真LOO保证。§3rangeF外test-gradient被sketch混入产生kernel leakage；训练梯度inrangeF只对empirical Fisher构造自动成立，不能给所有approxHessian。

KFAC独立factor投影需要每factor条件且mA*mE统计成本更高；未采用全部factor-tail公式，不遍历附件。§4/5明确低sketch-error可用较强ridge获得却降低下游LDS，validation选lambda再增m，不能用作者C10–100当普适budget。实际§5声明projection faithfulness与LOO modeling bias未解决。拟Ch27窄整合：当前800–806已有attribution specification/stationary inverseH/TracIn tensor-sketch，但未分“Euclidean sketch”与“inverse-operator sketch”的range/injectivity/ridge对象变化。新增的是pipeline数值近似合同，不授删除因果、不重复泛泛provenance或成熟JL原理。

## 10431 当前正文比较收束（作者）

实际Ch49 L1684–1694已有early-exit训练sensor与动态depth cache/routing/驻留权重；仍未承载训练path diversity与部署PTQ误差通过execute threshold耦合。拟接动态depth段两短段，解释熵只保探索、低bit后增加执行比例换质量而非同FLOPs免费恢复；Eq9 branch有错不照录，A6000 W4慢于原D-LLM保留。真实局部差额待PRE窄锁，不重复KV owner。

最终状态同步（2026-10-04）：本组必要源/处置已独立复核；10425 Ch23、10431 Ch49、10449 Ch27实际两段/完整邻接/末注root非作者POST通过，锁释放。10420仅报告有限代数/实验，不采用强端点通用命题；日级另验。
