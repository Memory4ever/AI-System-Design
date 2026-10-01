# 2026-04-24 三项中心解释的有限非作者复核（三）

复核者 root。只核作者已隔离的中心保证，不重审全部实验或从争议推出论文整体无效。三项 exact-v1 原文可读；本记录不核首公开批次、日级来源或否定侧筛选。

## `2604.20903v1` SUA：均值敏感度不能代替最坏情形上界

[官方 exact-v1 §3.2 与 §4.2 Eq10–11](https://arxiv.org/html/2604.20903v1)把 operational sensitivity 定义为扰动分布下的期望 divergence，并明确它不大于集合上的 supremum。Theorem 4.3 的风险上界先使用 supremum，随后却以较小的期望项替换，仍保留 `≤` 并称得到 Eq11；这个代换一般不合法。让极少概率扰动造成大 divergence，其余扰动接近零，即可使期望很小而 supremum 很大。Appendix A.1 同样先承认均值是下界，再称代入得上界，未补一个分布尾界/覆盖条件。因此不能把 operational SUA 训练目标表述成已证明控制 worst-case risk；受限任务中的预测相关性、entropy 与敏感度分账仍可单独评价。Ch66 的置信度/评价 contract 不据 Eq11 改写。保留 `2+2+2=6`、中心理论争议/Books 暂缓；重开需正确的 supremum surrogate 或有条件的尾界。

## `2604.21197v1` ProjRes：投影残差是攻击 sensor，不是成员身份证明

[官方 exact-v1 §II-C、§III 与 Appendix C Algorithm 1](https://arxiv.org/html/2604.21197v1)的攻击者是能见客户端上传梯度和全局模型的 honest-but-curious server；不能扩到安全聚合后只见聚合量的攻击者。算法把目标样本 hidden embedding 投影到由 adapter gradient 张成的线性空间，以小残差过阈值判成员。但线性 span 可以包含未参加训练的 embedding：取成员表示 `e1`、`e2`，非成员表示 `e1+e2`，若观测梯度空间张成前两方向，后者残差同样为零。这否定“零/低残差必确定训练 record 身份”的普遍解释，不否定该阈值 sensor 在论文所测分布上可能分离成员/非成员。其单轮攻击、模型与可见性条件应与防护/DP 结论分账。Ch72 保留共享梯度泄漏的条件性威胁边界，不把 residual 写成确定性证明。保留 `2+2+2=6`、中心解释争议/Books 暂缓；重开需针对非成员在 span 内的误报与跨分布阈值证据。

## `2604.21395v1` Geometric Blind Spot：协方差命题不等于 Gaussian 唯一分布

[官方 exact-v1 §5 Proposition 5–6、Corollary 2](https://arxiv.org/html/2604.21395v1)的 trace 等式只要求 `Cov(δ)=σ²I`。独立的对称 `±σ` 分量是非 Gaussian，却具有相同协方差并对任意 Jacobian 得 `E||Jδ||²=σ²||J||²_F`；因此“Gaussian 是唯一等向扰动分布”这一文字结论过强，协方差等式本身仍成立。Corollary 2 以 `x=(s,n)` 为输入却写 cross-entropy gap `I(n;y|x)>0`；条件在包含 `n` 的 `x` 后该 MI 为零，若本意为 `I(n;y|s)` 须更正条件变量。Proposition 6 定义的各向异性比 `||J||²_F/||Jw||²` 也非一般最大 `d_x`：`J=diag(1,ε)`、`w=e2` 时比值为 `(1+ε²)/ε²`，可任意大。它们限制了论文的普遍几何保证，不能据此抹去受限 Jacobian/TDI 实验。Ch16/66 的优化与评价边界暂不改写。保留 `2+2+2=6`、中心理论争议/Books 暂缓；重开需修订命题、变量与可复核的上界条件。

本批之后仅本日 15 项中心争议中的 9 项有具名有限非作者核；其余 6 项及日级 Gate 仍开放。
