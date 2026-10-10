# 2602.09207v1 必要审阅（Source待独立，因果/保证隔离）

[CausalGDP](https://arxiv.org/html/2602.09207v1)，Feb11/root AB已核；2+2+2=6，核心保证争议定点深入。§4 L154–267：NOTEARS初始化state/action→transition/reward masks、Gaussian模型，online更新并将joint transition/reward log-density梯度注入denoising score；仍有doubleQ/actorQ项，不是去critic通用policy。只可支持结构化预测guidance候选，不把DAG预测/执行action自然等同已识别因果；原文没建立latentconfounders排除、干预覆盖/positivity与正确graph的实验认证。r*原文假定离线每interaction最优reward已知，未来nextstate在采样时的可核计划/实现不明确，Alg1先observe再sample无生产在线顺序保证。

§5 L286–345只是给定globalLipschitz/有限系数下的Euler条件；L300/343重复Lφ而不是Lω，1+ΔtL界有限horizon误差不等于任意训练稳定/不崩溃。Th1 L359 vs proof385/396漏因子2，marginal actionKL与path integral也不能从原等号授普遍性能保证；不采用精确常数和“错误causal不会catastrophic”宣传。Prop2 L423–434证明只到E[r∇logp]，删除sampleweight r且叫unbiased不成立；条件score期望0一般不是非零reward梯度。原文nonlinearGaussian再换linear operators的Lemma1不能证明任意diffusion exactposterior。全部隔离，不自行修公式为论文。

§6 L505–582/AppA614：best baseline来自各原论文、MuJoCov4 onlinebuffer vs D4RLv2固定offlinedata不匹配；seeds仅multiple whenavailable没具体n，CI定义ND，episodes1000–3000未列完整transition/gradientsteps/GPUbudget。T2 NOTEARS/LiNGAM/noise三maze，错误graph损失明显且没有同network/no-guidance/非因果mask matchedbudget消融，不能归因真实因果识别；T3denseumaze、Walker、Antmaze-largeplay、Kitchencomplete等directnegative，非一致优势。硬件/precision/batch/denoisingsteps/runtime/SLO Not Disclosed。只采用受限替代设计与失败条件，不能进Books因果真值/guarantee；待root实际Source后作具体owner处置，必要原件足停止附录全证。
