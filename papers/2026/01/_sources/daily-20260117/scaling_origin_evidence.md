# 10684 scaling origin — 必要反证范围与 Books 判断

官方exact-v1为本目录`2601.10684v1-primary.txt`，normal Submitted/正常公告及registered上界完全落窗的条件见本日date字段。只处理v1，不借后续稿；未复现。拟2+1+2=5，设计反证定点深入，Books终裁待root。

原判断是数据中的power-law结构是模型loss scaling必要来源；actual §3.1.1/Fig1/3在unbiased Erdös-Renyi randomwalk中，degree/输入相关谱不含作者所述power-law结构，2layer Transformer仍出现有限范围loss scaling。具体增量是受控反例，因而需要撤回“观察loss幂律就能反推输入heavy tail是必需”的解释，不是证明所有学习系统的同一成因。

§2的loss由有限hyperparameter grid优化，irreducible offset、含/不含embedding参数、fit区间都会改变exponent；powerlaw MSE优于所选exponential只是模型比较，不证明函数唯一或任意远外推。§7明确window sensitivity不同于bootstrap CI，优化算法/超参再改变仍可改curve，小模型capacity没成为bottleneck也与一epoch步数绑dataset有关。更深/所有真实数据/生产模型的成因与μP普遍效率仍未证明；不把全部Fig/NN interpolation宣传捆入采用命题。

必要A配置：context50或100、batch100序列、AdamW/WD.01、14LR grid、2%warmup/cosinedecay、一epoch、每配置3初始化取besttestloss。best-of-seed/hyperparameter不是独立均值估计；bootstrap fit CI未覆盖所有训练随机性或模型选择。compute是FLOPs非GPUtime，E2E时间、hardware/precision与生产token预算在采用范围中Not Disclosed。Markov transitions及有限graph支持局部sequence反例，不覆盖所有semantic correlations的缺失。

`WORLDVIEW-SCALING-LAW` Ch7 L135–143明确数据频率/复杂度是解释性直觉、观察powerlaw不等知道普适原因；L56/223/241也承载recipe/区间及联合fit条件，没有输入tail必要或通用exponent的正文断言需修正。因此拟OnlyReport，保留有价值受控反例而非冒Existing已含本篇实验，不因具体recipe未写强制新两段。新证据或明确owner错误才定点重开；不因Books已有上位边界删候选。
