# 12222 HiAP：首版必要Source / 有界理论争议提案

mar14_supplement，03-14补Mar13 BJT。root七完整题摘与七日级日期独核有效复用。exact-v1 SUP_NECESSARY_12222.raw/txt（官方HTML GET200，SUP_STOP_GATE_MANIFEST_RESULT.json）；本人实际§1–3.4/Eq1–8、§4三条论点/证明、§5.1–5.4完整Table2/3及§6，直接相关AppendixA文字和B成本分解已读。不遍历参考/各拓扑图/代码/完整版本diff，不采用v3 A100原生吞吐>90%宣传；v1四作者和ViewPDF副文人数差异保留。

准入链保留：仅单粒度剪枝/搜索后阈值恢复难联合分配结构→宏head/FFN与微value维度/neuron Gumbel门共同训练、拆宏固定开销与微联合门成本、用软可行性罚项和hardening导出静态网→可能改变预算如何与结构共训的设计。**拟2+1+2=5，必要受影响内容深入后中心预算保证争议/暂缓Books0**；2只计实际联合宏微预算机制与所声称soft→hard有效边界，不借用Gumbel/残差等成熟原则或映射章节添分。不是因toy、费时、已有覆盖或全部论文无效关闭。

实际机制：Eq3微门只乘V，QK仍保原head维度；Eq5把每head C1固定项与C2 E[g d]、FFN C3 E[b c]相加，不必假设门独立，期望线性性成立。Eq7由task/KD、宏微成本惩罚和Eq8 ReLU可行性罚项组成，并非硬约束投影或给定C_target的可认证求解器。§3.4仍以概率>.5硬化；温度退火不等于不用阈值。软罚项本身不授所有有限系数/训练轨迹均保持quota，局部实测可以另成立。

决定性争议：§4 Proposition2及其proof声称τ→0时variance collapses、expected cost趋于hardened cost，从而固定.5达到small tolerance ε内目标预算。原文未量化small，不改写为任意小误差。Eq6却为每次forward重新加Logistic ε后sigmoid((α+ε)/τ)：固定有限α=log3，τ→0仍是P(z=1)=.75的Bernoulli，variance=.1875，不因温度而归零。这是对已写充分条件的直接反例，不是指所有学习到的logit一定有限。

更具体地，针对Prop2所写gate probabilities硬化的读法，固定父门为开，在其内10个同价unit微门均α=log3，期望可剪成本7.5；按学得概率>.5确定性硬化全部留存，实际10，差2.5，而单维cost granularity为1、可行整数7/8离目标仅.5。故差额不只离散步长。§3.4原写zhat>.5，而Eq6同符号指noisy sample，导出时如何停噪/取概率未明确；十门例不冒称已核代码导出。独立更强断点是Eq7明确不用global squared-error target，即便另外授variance collapse，仍缺E[C]如何接C_target的优化或repair条件；退火本身没有选择目标7.5。若作者另要求训练使logit充分饱和、停止噪声、或硬化后预算修复/目标可达性，应给出这些条件及误差界或匹配证据；本稿所写proof不能替代它。我们不推断代码必错误、模型全部不可用或实测速度不存在。

另一个精确采用边界：§3.1 Eq3是V-path维度mask但§3.4物理导出说Q/K/V全部同微门截断；QK logits可改变，不能由V-only式授同算子语义。AppendixB的简写C=sum(w_attn*g*d)又未显式保Eq5的head固定C1项；线性期望恒等式可用，不能把所有成本式默认为同一精确账本。没有为这个未决结论遍历代码或旧版本。

Table2受测DeiT-Small4.6G79.85→3.1G79.10或2.5G77.95，若干baseline在邻近MACs准确率更高；不是统一Pareto胜利。Table3 CIFAR ViT-Tiny同MACs受测改善，§5.4 batch1/50runs 5.57→3.86ms作者测量保留，GPU型号/precision未披露，不能把它替代理论预算误差/全部硬件速度。ImageNet200epochs/batch256/AdamW5e-5/teacher KD α.7 T4、温度2→.5而非已达0；匹配总训练费用/seed与不确定性未披露。§6本身明确目标是expected MACs而非校准latency/energy，硬件kernel会改变实现收益。

实际owner路由：MODEL-TRANSFORMER-LAYER（Ch17）完整开头1–135的shape/Residual/Norm与相邻Ch16/18入口已读，残差identity不自动保证任何结构删除或硬budget；INFER-TENSORRT-LLM（Ch49）执行计划/成本模型是交接不是把训练剪枝发明挂到框架名。此为有界中心争议暂缓，不称具体NC或已确认新缺口，不申请Books写锁。采用正面保证需官方明确更正条件/预算repair方法与对应可核误差，回到§4 Prop2/Eq6再定点重开。最新：SUP_INDEPENDENT_12222.md实际必要Source/反例/受限评分通过，原位落实small tolerance、noisy符号与Eq7目标桥接精度后，root完整回读采用；本日正式争议5/Books0，不授DAY。
