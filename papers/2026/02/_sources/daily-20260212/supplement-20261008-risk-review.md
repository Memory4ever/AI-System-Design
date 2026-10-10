# 2602.09300v1 必要审阅（Source待独立，中心估计式争议）

[Risk-sensitive reinforcement learning…](https://arxiv.org/html/2602.09300v1)，Feb11/root AB已核；2+1+2=5，中心理论与实现式冲突触发定点深入。

采用边界先分清：有限horizon、compact state/action/policy parameter、bounded累计cost；优化累计cost的非线性risk不等同逐step嵌套risk/Bellman。§4.2 A1–A6/Th4、AppB.5 L680–710隐函数推导给expectile gradient为E[lν(F−ξ)G]/E[lν′(F−ξ)]；twice differentiable policy、P(F=ξ)=0、boundedscore与density/Lipschitz是分别用于导数和smoothness的条件，不授离散LLM奖励直接满足。ν=.5退化mean、极端ν分母下界退化需保留，不把tail功能当reward后处理即可。

核心争议：§5 L310–322 Eq22明确2m independent trajectories，却将cost c(z_j)与g(θ,hat z_j)相乘；条件于z，E[g(hat z_j)]=0，故ratio估计的条件均值0，非一般非零risk gradient。§6 Eq24 OCE同问题。AppC.5 L947–970也明确该独立项，不能用符号转换消解。官方v1 PDF page8 via pypdf完整提取实际再次确认2m i.i.d.与hat-z乘积（非HTML单独转写）；PDF截图cache miss，不声称视觉渲染成功。原件公开PDF链接与riskcore/necessaryproof保留。请求作者勘误/证明正确的配对或独立根估计构造；不自行把改公式当论文成立。保留Th4受限导数与中心估计/收敛争议分开，暂缓一般UBSR/OCE guarantee及算法采用，不机械贡献排除。

§7 A15/Th9只是条件smooth objective+MSE O(1/m)下approx FOSP，非global optimum/safety；§8 L413–426 Reacher 5seeds/250frozen-policy eval，RAPG B100/lr.002而REINFORCE B1/lr.0001，不授机制唯一因果或样本预算匹配增益。N称episodes但B√N，使真实采样工作未完全对应同N；不授同成本更优。硬件、precision/runtime/SLO Not Disclosed。停止其他risk证明/实验附件。Source后Books仅可对比riskfunctional与stepwise风险归属，不写争议guarantee。
