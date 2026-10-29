# 2603.10391v1：必要PDF证据与中心争议

唯一owner `MULTIMODAL-GENERATIVE-PARADIGMS`（Ch24）；评分2+1+2=5，标准审阅中发现理论转接/实际recipe冲突，深入受影响内容，不以争议缩池或降分。

## 精确来源、实际读取与配置

官方HTML v1 404原值保留 `SUP_CORE_FIRST_MANIFEST_RESULT.json`；官方 [PDF v1](https://arxiv.org/pdf/2603.10391v1) 已恢复200、15页，原件 `SUP_PDF_10391.raw`，导出 `SUP_PDF_10391.txt`。完整读§1–5、App A–E；实际视觉核PDF页2–4/6–8/10–11/13/15（含Eq9–14/Table1/Figs5–6/Algorithm1），不以公式提取乱码作争议证据。单RTX4090、U-Net/EDM、CIFAR10/100 32×32、50k训练/10k测试、60k步、Adam2e-4、batch128、3seeds42/142/242，FID50k生成样本。Precision、sampling solver/NFE、wall-time/额外运算实测、权重归一化、FID参考实现/人口细节Not Disclosed。AppE称接受后将开源，没有核实现或复现。

## 作者新增与受限观察

§3.2把loss条件方差当gradient variance proxy，以log-SNR bins观察异质性。§3.4不改变noise schedule，用batch-mean μ居中的平滑weight乘原EDM loss。Table1报CIFAR10 FID14.21±.31→13.58±.55，CIFAR10023.31±1.10→20.89±.74。可记录这是作者所报有限质量结果，但CIFAR10离散程度实际上升，不能照抄“跨seed方差均减少”。Fig6有3seed有限曲线，不证任意规模/架构或训练加速的普遍率。Fig5 .01/.05/.1的FID14.49/14.09/14.18与Table1的13.58不同人口/seed/step未说明，不能合并成同一测量。

## 中心争议：原文与审阅者推理分开

1. §3.3 Eq10写 `∫p(λ)σ²(λ)dλ`，称在 `∫p=1` 下最小化会得Eq11 `p*∝σ`。**按显示目标该推论不成立**：它对p线性，允许自由分布时应把质量集中到最低σ²人口；只有加入固定目标measure/importance inverse-weight和相应二阶矩等条件，才得到另一种重要抽样问题。不能把成熟importance theorem借给这里不相同的目标。
2. Eq12 `p*/p` 只能无偏估计目标p*下期望，不能保原p下objective不变。实际Eq13/14 heuristic multiply也没有证明它是p*/p，μ又依赖batch；因此“保持schedule”和“保原objective且仅降低gradient variance”不是同一命题。loss variance不是gradient variance，没有原文提供等价/控制证明。该断点不否认heuristic可能有有限FID收益。
3. §3.4 Eq13是Gaussian `exp(-α(λ−μ)²)`，AppD Algorithm1 line12却是rational `1/(1+α(s−μ)²)`；两种不同recipe不能静默选一个当核实实现。AppA又说动态调整sampling probabilities，而主文/算法说固定采样乘loss；代码未公开，中心实际实现无法从该稿确定。
4. 实际控制器没有计算observed loss variance或估计gradient variance，只用batch log-SNR均值。称“variance-aware”是动机/作者归因，不是已实现在线variance feedback。Fig2 weighted loss变平也可能直接是weight尺度效果，不能独立认证同一gradient estimator方差下降。

拟终态 **争议/暂缓**：保留有限batch-centered loss-shaping与作者FID观察作报告上下文；不采用variance-optimal、unbiased原目标、实际在线variance-controller、跨seed稳定普遍提高或无实测overhead的保证。代码是可选材料，当前停止基于稿内中心争议，不伪造external blocked；若有明确recipe/目标measure/理论条件、同gradient测量与匹配预算对照，定点重开。非作者Source定点核待；无Books写入、无DAY。

## 现owner具体比较：拟争议/暂缓Books0

实际完整读当前Ch24 `Diffusion：先加噪，再学会撤销噪声` 起始到采样分工的局部125–158及前后交接。噪声schedule、time sampling、prediction参数化共同定义目标，普通简化MSE不等精确NLL；在线分箱已有FIFO/EMA/最低样本/刷新与proxy条件。正文明确固定w换π时effective objective为πw，不自动保持原目标的unbiased importance sampling，并保留网络MSE不等真实entropy、低noise gate/稀疏bin/陈旧EMA费用与固定sampler/权重fallback。因此本篇heuristic没有补足当前owner缺口；成熟目标分责已具体存在，**不是声称新variance-optimal定理或三seed实验已吸收**。

中心理论与recipe未稳定，拟Books争议/暂缓0；没有逐字PRE拟文或共享写锁。采用边界仅报告上下文，需独核Source/现owner与终态裁决后同步本日报，不对冲突公式作作者之外的recipe修补。
