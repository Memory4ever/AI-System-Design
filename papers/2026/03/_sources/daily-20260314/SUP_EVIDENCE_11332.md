# 11332 必要 Source / 具体 owner PRE 提案

作者mar14_supplement，精确v1官方PDF `SUP_PDF_11332.raw`（869026B，manifest200）；HTML不可用不作全文受阻。实际读p1–8的问题/技术机制，§2.1–2.2全部计算定义、softmax-hardmax假设，§3 Theorem3.1/Lemma3.2、§4.4 extended Baur-Strassen必要声明、§5 Theorem5.1/主proof的梯度抽取接口、§6完整开放问题及Appendix C声明/PropositionC1（不读全部证明或其它附录）。p14/p23完整页面视觉核定理分数与减项，text `SUP_PDF_11332.txt`由官方PDF转换保留。无运行代码/复现或生产性能采用。

## 原约束与新增机制

多heads/layers输出可聚合，单head下界不能直接乘LH；矩阵多实例有amortization反例。小embedding构造将unbalanced3OV的N,N,LH三组向量各c_h,l编码入head权重，保留输入列并跨层累计可辨识的0.5 gap，hardmax经score-gap/scale换为softmax。Theorem3.1精确m=Theta(logN)、L/H=poly(N)、arbitraryTransformer/input、逐项additive error1/(10N)，在3OV/SETH假设下需LHN^(2-o1)。不是任何实际模型都逐head串行，也不是常数误差近似的通用禁止。

大embedding的原推导先写denormalized技术概览，但§5用标准softmax并额外保留归一化信息。扩展Baur-Strassen从eAC用O(s)成本得到全部partial derivatives，auxiliary C与D提取LH个独立matrix products，不是要求在线推理执行反向。Def2.8 weights W与X都为电路输入（固定参数化结构≠单个训练checkpoint固定数值）；Theorem5.1存在N+1长度、m=2N+3、identityMLP构造，下界LHN^(omega-o1)−O(LHN²)，omega>2才是主导matching；exact-real eAC含+−×÷exp/ln。WordRAM推广仍§6open，ω=2需另小embedding条件；不授硬件HBM/延迟/有限precision或任意output近似下界。

## 必要反侧与适用边界

Def2.3未给causal mask：full self-attention family，不自行授causal/GQA共享结构。AppendixC sum每head宽m、concat每head m/H，C1由sum宽m/H变concat宽m+H和N+1；必须保留宽度重参数化，不能把formal sum m直接读成本章固定d_model下d_h，也不能断言固定d_model增H必按LH翻算术。§6明确worst-case，不排除受控input distributions/结构算法；approximation、pruning或architecture change改变问题。论文是理论没有hardware/precision/batch/SLO/benchmark，均不适用而非虚构NotDisclosed实验。

## 实际 owner 差额

ROADMAP owner `MODEL-MULTI-HEAD-ATTENTION` Ch15。已实际顺读Concat/固定basis/扩大匹配空间70–130、H工程约束132–146与MHA/GQA接交150–215、章末位置；Ch14单头公式/mask/routing与Ch17 layer入口相邻核。现正文有算术复杂度≠速度、pruning需要执行合同、固定宽度H-d_h耦合，但没有“sum输出是否可摊薄LH次任意dense计算”的directsum下界及其两种计算模型/维度约束。不是主题已有直接NC。

建议2+2+2=6标准最低，因具体长期缺口深化必要理论局部；唯一owner Ch15在“因此H是模型容量、每头维度与执行效率的联合选择”之后、MHA/MQA/GQA之前插以下两段，不写Ch17第二份；parent独核通过后parent实际写，我非writerPOST。

### 拟正文（待独立 PRE，不授已写）

把多个 heads 的输出放进同一 fused kernel，可以减少中间存储与启动成本，却不能据“最后只需一个聚合输出”就假定任意 dense 多头、跨层计算都能按实例数摊薄。这里存在 direct-sum 问题：单个 head 困难，不自动证明 `L×H` 个实例同样困难。[受限理论结果](https://arxiv.org/abs/2603.11332v1)用独立问题编码到各 head 与层的构造，给出 sum-aggregation、每 head 宽 `m=Θ(log N)`、`L/H` 与 `N` 多项式相关且逐项输出误差至多 `1/(10N)` 时，在 3-OV/SETH 假设下的 `LHN^(2−o(1))` 最坏情形计算下界。这不是各 head 必须串行的调度定理；concat 推广还重参数化总宽度，不能直接拿论文的 `m` 代替本章固定 `d_model` 下的 `d_h`，更不能据此认证所有 checkpoint 都没有冗余。

大宽度分支把完整 softmax 计算与多个独立矩阵乘积联系起来：允许实数加减乘除及 `exp/ln` 的扩展算术电路，通过同量级成本抽取偏导恢复各乘积。其 `m=Θ(N)` 构造、`ω>2` 时的 `LHN^(ω−o(1))` 下界针对所有输入与可变权重的精确计算，不是推理时需要反向，也不适用于任意 Word-RAM、有限精度或生产延迟。Full-attention 构造、宽度和最坏情形条件不能自动搬给 causal mask、共享 KV 或实际数据分布。因而，保持原 dense 算子时仍可通过融合、layout 和并行改善常数与 IO；要省略计算，则须显式改变近似误差、可见结构、共享或剪枝合同并验质量与总成本。条件不符时保留成熟 dense MHA/GQA，不把理论下界写成所有加速都不可能，也不让一项速度测量反证不同计算模型的定理。
