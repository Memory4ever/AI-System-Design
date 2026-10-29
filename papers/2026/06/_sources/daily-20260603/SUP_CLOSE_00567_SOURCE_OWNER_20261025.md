# Jun03旧具名00567必要层与实际Ch49差额

R191完整v1题摘/notice/联合Jun02日期与准入已闭，正式初分2+1+2=5，不第三AB/date。本writer现实际读[exact-v1](https://arxiv.org/html/2606.00567v1) / [保存原件](SUP_CLOSE_2606.00567v1_20261025.html)§2–6、全部T1–4及figure captions；不核图像素/代码/真实硬件或复现，不读v2全文。潜贡献不是泛稀疏≠快，而是同逐元素稀疏下column-only consumer与跨denoise hotset/形状不同、以及阈值校准伪造可跳量的具体设计边界。

## 必要支持与直接反侧

- GELU/GEGLU输出A∈R^(M×N)，一列任一token超过绝对τ就hot，只有全列低于才允许column-skip；跨步hotmask Jaccard另测，不是elementdensity。p^M只在独立token的启发模型，正文承认attention使token不独立；M、expansion与concentration关联不是匹配架构干预、也不推出按group名称永远同策略。
- 七模型SD1.4、VC2、Make-an-Audio、DiT-XL2、MDM、MLD、EDGE，50denoisesteps，hooks逐元素fullprecision判断。M6～10240、N1024～5120；batch、seed抽样人口/实际profile硬件、执行tensor dtype及完整输入输出长等必要域未齐，不补为某GPU实测。T2 800MHz16²systolic、16bit SIMD/24/192/24KBbuffer、Ramulator2 GDDR6 96GB/s为**模拟**，不是芯片/端到端pipeline计时。UNet多shape用ch320代表block，比例也可能受形状/调度影响，不能由baseline和sparse同模板自动授无偏。
- uniform τ与per-layer targethotratio r虽然同五数值，单位不同、**不能相同数值当同约束或同质量**；r逼更高threshold达到稀疏目标并不揭示天然低幅。τ.164为先看motion cliff之后的selectedreference，不是独立选型/全域最优。正文把DiT per-layer大量收益称inflation artifact，不能照53–59%当合法净收益。
- §4.2/4.5同时说DiT相邻hotset Jaccard恰1却hotset不断增长，按其intersection/union定义不可能两者严格同时成立。若1是rounding，精确stability不成立；即使hotset单调增长，也不保证iteration0冷集合可永久skip。原文“static layout remains valid throughout”未分layout和每步mask刷新，不采静态身份保证/永久coldrecipe。MLD的高可跳率与低Jaccard并存恰说明收益与布局复用资格两维，不以同组忽略差异。
- FFN-Reuse说明cold列跳W2运算并reuse Y(t−1)，§3.4质量臂却写cold-columns-zeroed，不是同一个operator。故T4质量shift与cycle reduction不能合成已验收的同质量加速点；N100同seeddense-vs-masked是pairwise输出差异，不是自然质量或真实motion安全。FID/LPIPS/FVD/FAD/MPJPE等列不是同量纲平均，表中较大差值不照作者“small”作无损。更高threshold的motion cliff作为作者有限人口现象保留，不给固定τ普适安全区。
- 84–89%模拟stall不证明GPU/任意GDDR带宽总pipeline必memorybound，高rowhit同时高stall也不能只归rowconflict；模拟只静态布局/一个DRAM点，未实测repack/metadata/control全链，不采用具体headlines。所有profile、threshold搜索、hotset维护、permutation、DRAM/计算/旧输出状态及quality回归都需计费；partialtiles或动态重排未实测不冒已实现。

## actual owner比较与原单段申请

已完整读Ch49“剪枝与稀疏执行”中的Sparse-on-Dense/C​​SC→dense PE整段、importance/protected-set三段、staticweight+dynamicactivation列可寻址解释/codeflow、weight-aware动态mask、共享representation两kernel成本完整段及后双稀疏SpMspV。现文承担column support、metadata与phase不同，但没有**diffusion同一列跨M token的OR粒度、逐步hotset身份与τ/r两类校准量如何限制静态hot-cold layout**。这不是为新marker重复泛稀疏原则，独立于现LLM按每token选择列的执行人口。

唯一`INFER-TENSORRT-LLM` / [Ch49](../../../../../books/part-05-inference-system/49-tensorrt-llm.md)。拟在“共享representation不意味着共享实现”完整段（结束“不把特定作者在A10G/L4/L40S、LLaMA-2-7B与matched-perplexity workload上的结果外推为通用加速。”）后、现“若weights与activations同时稀疏”完整段前补如下单段；保原解释/code与直接两侧，不新标题。尚未授权/写Books：

> 列可寻址也不等于逐元素零值都可跳过：当consumer把同一列的M个token合并决策时，一个超过阈值的元素就会使整列hot；diffusion跨步复用布局还须另验hot集合的变化，不能只看稀疏比例。[受限column级刻画](https://arxiv.org/html/2606.00567v1#S4)中，形状/层段相近的高element sparsity也对应不同可跳列与temporal churn；较高可跳率不自动允许永久复用首步冷集合。绝对activation阈值与按层目标hotratio是两种校准合同，强迫达到目标比例可制造更多有损跳列，不能在同一数字下比较为等质量。该研究的周期来自静态GDDR模拟，cold列复用旧输出与质量臂置零的语义也未对齐，故不采用其质量—加速联合点或固定安全阈值。Profile、逐步mask、重排/索引与真实生成回归均计费；身份不稳定、质量或完整成本不合时，刷新mask、保原布局/dense或较保守跳算，不把hotset重合率、taxonomy或模拟stall占比批准成端到端SLO。<!-- source-family:SF-2026-ARXIV-2606-00567 -->

支持与直接反侧已足，对上述真差额作5分受影响域深入而不扩附录/版本/未知标题；交非writer一次必要/owner/literal核验后再决定Books。若认为现文已具体承担该diffusion粒度/时间接口可NC，但须指actual正文，不按工作量或最后一篇要求造diff。有限stop及所有已成22项不因此重开。

## 实际采用停点

上方保留原提交状态。R192必要/actualowner/原位置通过，只把shape-matched暗示明确收窄为“所测workload即使都有较高element sparsity，也对应不同可跳列与temporal churn；跨架构观察不唯一识别M或expansion ratio的因果”，其余literal不变。root窄授后已实际SAVE Ch49共享representation完整费用段后/SpMspV完整段前及true-H2本人一注，作者完整selfread新增、完整直接双侧和本人注；非writer R193唯一actualPOST通过，正式5分实际整合生效。未核实现/像素/复现，不授日级Gate；不第三必要或行政保存态轮。
