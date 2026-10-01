# 2026-04-24 三项印刷中心冲突的有限非作者核

复核者 root。仅复核三项作者已标争议的中心定义、对应实验解释和安全处置；没有将争议解释为全部论文无效。官方 exact-v1 可读，故不是材料访问受阻，也不是授权写入 Books 的依据。

## `2604.21327v1` DDRL：印刷固定优势不能产生所称正的组均值

[官方 §3.1–3.2 的 Eq5–7 与 §4.4](https://arxiv.org/html/2604.21327v1)规定每组 `K+ = min(c(y*), floor(K/2))`、`K- = K-K+`，正负 rollout 优势固定为 `+1/-1`。所以按这一定义，任一组的未加权优势均值为 `(K+ - K-)/K = (2K+ - K)/K ≤ 0`，正权聚合各组仍不可能变正。§4.4 却把 MATH-500 曲线描述为训练后期 mean advantage 转正。除非实际日志用 token 权重、另一分母或另一优势定义，否则不能把该曲线解释为印刷机制带来的自适应正信号。抽样频率可降低特定伪标签噪声，固定幅度可取消分母放大，但不能消除错误多数标签；附加 128 条重采样/五 epoch SFT 的总成本亦不等于表中所列训练时间。对 [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 不作正面修订，保留 `2+2+2=6`、深入审阅、中心解释争议/暂缓。重开需日志定义或作者实现/勘误解释正均值。

## `2604.21241v1` CorridorVLA：按印刷对象计算的 corridor width 为零

[官方 §III-A–C Eq1–10](https://arxiv.org/html/2604.21241v1)先把 GT 的位移并入 extended action，又规定 `g(A*)` 从同一 chunk、同一 anchor indices 读取位移；Eq6 的 `delta = alpha · max ||g(A*)_k - Δp*_k||` 因此逐项为零。它不能构成叙述中随样本变化的正宽度容忍带。若实际代码取预测 anchor、另一个位移观测或噪声尺度，则须公开其对象桥；Eq7 此时只是零宽 hinge，而非所宣称 tolerant buffer。论文关于辅助 anchor 监督、extra-A 和 LIBERO 局部收益不因此全盘作废，也不能将离线成功率升格为物理安全。对 Ch26 不写“正宽 corridor”机制，保留 `2+2+2=6`、深入审阅、中心构造争议/暂缓。重开需修订定义/代码与相应消融。

## `2604.21570v1` SpecSyn：refinement 更新方向与 VDR 目标相反

[官方 §3.3 Algorithm 1 与 §3.4 Definition 1–2](https://arxiv.org/html/2604.21570v1)把被 verifier 驳回的 spec 从原程序候选中剔除，随后以 mutant 上能被驳回的比例定义 VDR，目标是让更多语义不等价 mutant 被区分。但 §3.4 印刷递推又从新 spec 集减去“在 mutant 上被驳回”的 spec，恰删除 VDR 所需的区分条件；与 Algorithm 1 中为 original program 剔除被驳回项所用的对象不同。不能据印刷递推签发“迭代提高鉴别率”的机制保证。论文的分段、POI、sketch、verifier 与实际局部实验可独立保留，但 mutant 生成不等于已证明语义非等价，solver unable-to-prove 也不等于语义假。对 Books 的 verifier/Agent owner 不作正面修改，保留 `2+2+2=6`、深入审阅、中心递推争议/暂缓；需算法勘误或 artifact 明确两次过滤的对象后重开。

三项仅完成单篇有限复核；余下争议项与日级来源/日期/否定侧仍待处理。
