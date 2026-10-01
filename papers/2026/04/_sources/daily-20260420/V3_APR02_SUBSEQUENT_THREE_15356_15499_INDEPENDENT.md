# Apr20 三项有限非作者处置核验

复核者 apr02；与Apr20作者/Books写者分开。本次实际重开下列官方v1必要命题，并对读15409拟采用的当前Ch49实际正文；只验具名处置，不验日期/全日，不写Books或正式日报，未复现实验。

## 15356 — 窄争议通过

[官方v1](https://arxiv.org/html/2604.15356v1)实际§2.3 Definition2/Remark1及§7.3。d=-log₂P(LCP)，对两个单token各概率.5，d(a,a)=1、d(a,b)=d(b,a)=0，取s=a、s'=b、s''=a，印出的ultrametric需要1≤0，确失败；非零自距的声明不修三角。§7.3 max d“等价”max P也反方向。窄D只隔离打印metric/近义prefix复用保证，保固定输入/权重的确定性、另有injectivity条件的熵论证、精确共同祖先查找，不称全部预测/压缩实验无效。需作者正确metric/检索规则及相关KV近似证明才重开。2+1+3=6 Deep暂缓这一处置PASS。

## 15409 — 受限数值合同已有覆盖通过

[官方v1](https://arxiv.org/html/2604.15409v1)实际§6.3 Table2、§7.3/7.5–7.6；FP32配对600×32steps消除该切片flip是精度干预，不能证明所有模型唯一因果。源§7.5明确residual patch未恢复不直接证明KV state就是原因，直接KV tensor patch仍future；低任务acc的truncation/fewshot限制也显式披露。实际读Ch49:1612及相邻数值合同，已绑定precision/reduction topology/kernel/activation/compiler/runtime/hardware并要求重验，完整承载本次只采用的执行路径条件，非整论文/架构因果已覆盖。6标准窄Existing PASS；不采用sole-cause、任意FP32等价、所有部署100%漂移。

## 15499 — 打印线性share步骤窄争议通过

[官方v1](https://arxiv.org/html/2604.15499v1)实际§3.3/3.4。两方印成e₀W₀+R₀与e₁W₁+R₁；若这是完整在线linear，取e₀=1,e₁=0,W₀=0,W₁=1,R=0，share和0而真实(e₀+e₁)(W₀+W₁)=1。缺交叉项确有有限反例，后接secure非线性/argmax不能补印出的线性缺失。只隔离所印完整协议及全confidentiality保证，不断言CrypTen实现遗漏secure multiply、不推出已泄漏；成本加权capacity routing/局部表仍有效。6纠错Deep窄D PASS，重开需该版secure-mul/选择协议或可核实现/trace假设，不需复现所有GLUE。

以上三项必要处置通过；不代替Books写后或Apr20日级Gate。
