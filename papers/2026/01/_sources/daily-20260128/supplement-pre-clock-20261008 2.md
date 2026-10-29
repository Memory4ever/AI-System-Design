# 18681 learned clock：PRE待root非作者

Source root实际v1 §2.2/3.1–3.2/4.2/5.2/5.3/6/C必要对照；作者实际§2.2/4.2/5.1 distillation/5.2 Table2。最低采用非HJB定理：state-conditioned clock训练→平均并归一为time-only网格→部署无actor/Q。2+1+2=5，Ch24实际gap所涉深入必要够；理论允许theta负、HJB classical假设、Euler局部误差proxy不等FID最优/actor收敛，均不复制未核公式。5000iteration/JVP/time derivative成本与部署去actor分开；Heun2K−1 matchedNFE、35NFE时ART/EDM同1.85，不授每budget严格支配；state dependence丢弃适用域未普遍证明。硬件/precision/SLO未披露。

作者实际Ch24 205–230，当前solver curvature→Euler/Heun及offline grid search没有 learned state-clock→compiled time-only、端点归一分工；Ch23小结交接和Ch25开篇实际读，owner MULTIMODAL-GENERATIVE-PARADIGMS。拟插solver Euler/Heun段之后、history forecast之前两段（root写锁尚待）：

调整 solver 阶数之外，也可以先学习数值时间怎样分配。一个受限分支以局部 Euler 误差代理和到达终点的约束训练可依赖状态的 clock，先按时间取训练轨迹 clock 的经验均值，固化成非均匀网格，再将其增量和归一到总 horizon。训练控制器与部署 sampler 因而是两个 artifact：线上只复用网格，不继续运行 actor 或误差代理；增量和恰好等于 horizon 只保证数值端点命中，不保证生成样本正确。网格必须绑定 score/velocity model、solver、原时间方向和训练人口，不能把“自适应训练”写成每个请求都在自适应采样。<!-- source-family:SF-2026-ARXIV-2601-18681 -->

固化省去逐步 controller 调用，却支付额外 actor/critic、轨迹、JVP 和时间导数训练，并丢弃状态依赖；何时平均网格足以替代状态控制，仍需目标 workload 验收。[有限 EDM 对照](https://arxiv.org/html/2601.18681v1)仅固定 score、solver 等条件比较时间网格，低/中 NFE 有收益而高 NFE 可与原 EDM 打平，不授任意质量指标最优、训练收敛或 production latency。局部误差目标、FID、实际 NFE 与总训练/推理费用应分开测，端点归一不使负向时间或域漂移自动安全。迁移质量下降、状态差异重要或校准成本不合算时，保留原 EDM 网格、固定 Euler/Heun 或逐状态控制，而非由一条离线平均曲线签发通用采样保证。
