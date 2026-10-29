# VSRAQ 05688首次必要与actual owner／原两段PRE

作者jun06_continue，2026-10-25，仅Daily2026-06-06补Jun05。R19完整exact-v1题摘、官方组合日证与准入有效层直接复用，不第三日证，不读取别日材料池。正式拟分2+1+2=5：改变MoE PTQ校准目标为设计2，单量化组件reach1，value/排序/截断边界分责为durability2；不把成熟top-k、机构或拟Book处置计分。因长期最小gap加深读足受影响机制及关键反侧，不为5分只做摘要。

## 必要原件与采用边界

实际读[exact-v1](https://arxiv.org/html/2606.05688v1)§3–6、式1–18、表1–5及Figure1文字caption；未核图像素、源码、复现或所有引用。VSRAQ不是另一个runtime路由算法：AutoRound block-output reconstruction外加router校准项，优化quantization参数。以FP router排序π作共同参照：value项混合原选top-k logits MSE与按sigmoid p(1-p)敏感度加权的score误差；structure项对原选中者相邻差用softplus penalty，并匹配第k名与紧邻未选中者的logit差。默认b=1、rank margin=0、alpha=.3、rank/.margin权重.01/.05，router系数Solar .01/Nemotron .1。它不保护任意所有未选expert，也不证明离散集合永久不变；sigmoid单调本身不改变logit排序。m=0的softplus仍有正值并倾向拉开差，不能把它说成只有发生inversion才启用的hard constraint。

对照为AutoRound reconstruction、加TopK-MSE、再加sigmoid、完整structure。两模型Solar-Open-100B与Nemotron-3-Nano-30B-A3B；前者W4A16/NVFP4、后者NVFP4。校准每模型512随机混合reasoning例，最大长度2048/1024；lm-eval-harness0.4.11，生成读出greedy，MMLU-Pro/GPQA thinking8192，另GSM8K；likelihood MC与WikiText2 PPL另算，不将三种读出拼一个质量真值。

表2–4的完整法均优于所列两量化baseline的相应平均，但仍低于unquantized；Solar NVFP4生成平均64.43对原73.62不能称无损。表5直接反侧：Solar W4A16加sigmoid PPL6.72后再加structure为6.81，Nemotron NVFP4 TopK10.78加sigmoid10.79；组件不单调，不授value/structure各自普遍正收益。完整法对比只有组合/顺序加入，rank与boundary也未独立拆消融，不能给每个子项独立因果功劳。§5.2 616759个stem/chat/math/code tokens的逐层top-k集合Jaccard/caption支持有限route agreement；集合相同不说明权重、顺序、输出或服务性能相同，headline最大相对改善不当全层平均。未读图像素不录曲线数。§6把2/3bits及更多架构/framework留future，不回填为已测。

原文未披露统一hardware/topology、全校准iterations/总时长、全部batch与随机重复/CI、线上concurrency/SLO；不由greedy消去校准抽样及其他不确定性。只改calibration loss而不新增推理graph节点支持结构边界，不等已测相同总latency/energy，更不抵消生成长度变化。参考/量化双路径、router统计/排序与优化、超参选择、packing及独立质量/安全/完整执行回归全部计费。路由漂移是诊断，不是所有质量下降的唯一原因；权重计算误差与route-mediated误差要分开，质量退步保较高精度或普通PTQ。支持和直接反侧足够，停止附件/代码扩读。

## actual owner与最小差额

已实际读Ch49全局router误差预算完整两段（2605.23078）、MoE calibration identity/MoEQuant完整两段、权重谱代理/AlphaQ两段、analog-CIM router校准两段，以及route-overlap/quality/performance分测完整段和compute-vs-routing mediator完整段。Ch21低频expert精度两段与Ch48/50开篇交接亦核。全Books精确2606.05688/VSRAQ/TopK-MSE/结构对齐定点检索未找到此家族真实正文；2601.05688是其他身份不混。

唯一owner为`INFER-TENSORRT-LLM` Ch49。现有正文已经承载路由离散翻转、artifact身份/代表性校准、route overlap不等quality，以及counterfactual诊断；均复用、不当新机制。但尚未承载PTQ校准把原选值/选中者次序/第k边界分别作为目标，以及代理排序稳定仍不授权所有输出和性能。Ch21拥有top-k语义但不重复量化目标。因此拟最小两段，不另造节点；若reader发现真实同义目标已覆盖则具体NC优先。

## 原两段PRE（未保存Books）

拟位只在Ch49“MoE Quantization 必须把 Router 放进全局误差预算”第二完整段及2605.23078 marker后、二维tiling分支第一段前。原两段/tiling完整两段均不动；须首次独核必要/5/actualgap/PRE及root本轮fresh精确窄授后才写。

固定目标位宽后，校准还可以显式约束路由，而不只匹配block输出。[一条受限PTQ分支](https://arxiv.org/html/2606.05688v1#S3)以原精度router排序作参照：既匹配原选top-k的logits及敏感score，又分别约束选中者的相邻次序和第k名与邻近未选者的差。这些项改变离线量化参数的优化目标，不是部署时强制沿用原routes；只保护有限边界也不保证所有expert选择不变。Reference checkpoint、score形式、k/边界范围、loss权重与校准人口应随artifact保存，不能把“量化后数值接近”当作计算路径未变。

这些目标之间仍可能竞争：受测消融中，再加结构项也会让某一配置的perplexity反退，route集合更近不证明路由权重、输出、安全或净延迟等价。量化计算误差和route介导误差仍需分别诊断，任务读出与完整执行另验；不能把两个模型的4bit对照外推尚未测的更低位宽。参考前向、router统计/排序、优化选点、packing和质量回归均付费；移除离线loss不增加运行图节点，也不等已经测得同能耗或服务SLO。目标冲突、校准分布漂移或质量不合时，保普通reconstruction PTQ、较高精度与原router，不由更高route agreement签发部署资格。<!-- source-family:SF-2026-ARXIV-2606-05688 -->

本人注拟：`SF-2026-ARXIV-2606-05688` — jun06_continue，Daily2026-06-06补Jun05；R19AB/date/准入复用，2+1+2=5/唯一INFER-TENSORRT-LLM Ch49。exact-v1 §3–6/式1–18/表1–5及F1caption必要，只校准value/原选排序/有限boundary分责；保softplus非仅flip处罚、组件反退、Jaccard非quality/安全、2/3bit future与全费。未核图像素/代码/复现，hardware/全校准时长/seedCI未披露不补，未授无损或服务SLO；首次必要/PRE/rootfresh/SAVE/POST按后到事实记，不预I/DAY。

## 既成采用（2026-10-25，仅行政同步）

[R23/R24](SUP_REVIEW_20261025.md#r24--vsraq-05688唯一actual-post)依次完成首次必要/正式5/actual Ch49原两PRE与唯一非writer实际POST。root本轮fresh新窄授后A29逐字真存于23078独立marker后、09281 binding开始前，并完整自读新增/完整两侧/本人注；R24真保存通过，I9生效、指定窄位释放。前述未保存/拟态只保历史过程，不再表示当前未完。不第三必要/正文，不授DAY；本阶段仅Report/Source行政采用。
