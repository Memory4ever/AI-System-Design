# 00129 负侧定点重开

精确原源：[Toward Large-Scale Photonics-Empowered AI Systems: From Physical Design Automation to System-Algorithm Co-Exploration v1](https://arxiv.org/html/2601.00129v1)。2026-10-02实际重新读完整题摘及决定准入的§2.1–2.3、§3.1–3.3、§4和对应参考1–9/28；不补读全部引用论文或无关附件。root负侧完整题摘抽检指出原“photonic综述”标签理由不足，现保留该改判过程。

## 原核心事实与新增对象

- §2.1明确称prior Lightening-Transformer[1]，dynamic dot-product/full-range signed input与WDM广播；ref1为HPCA2024。§2.2 TeMPO[2]用时间复用与photocurrent/capacitive partial-product accumulation摊薄ADC采样；ref2为2024。§2.3 SCATTER[3]组合算法/电路稀疏、thermal-aware布局、light redistribution和电源门控，ref3为2025。这些是实际相关机制，不能以领域标签否定；本文没有为其新增工作负载下可比反证或成立条件。
- §3.1把device/circuit loss、drift、thermal、calibration/control传至architecture/dataflow/功率内存等系统指标；明确归SimPhony[4]，ref4为DAC2025。§3.2 ADEPT[5]/ADEPT-Z[6]分别可微离散松弛/gradient-free多目标Pareto拓扑搜索，候选进入SimPhony和布局工具，ref5/6分别2022/2025；本文阐述工作链但未披露新的联合搜索契约、优化条件或新的同预算跨层验证。
- §3.3 Apollo[7] placement显式考虑routing spacing/congestion/crossings；LiDAR-V2[8/9]把orientation/bending radius并入A*邻居生成，orientation-aware bitmap维护spacing和crossing；ref7–9均2025。本文布局时间、插损、面积改善是这些工具的汇总描述，不当作本次新增且已归因的模型端到端性能结论。
- §3.3 metal routing[28]确实不能机械归为旧工作：ref28标ISPD2026。本文对应两段（HTML L117–118）说明光电布线需同时考虑pad breakout/长互连/keep-out/coupling/thermal与crosstalk，但没有进一步披露planning-guided新算法、接口语义或对此增量的独立比较；仅凭2026引用年份不把它推成本文新增设计机制。没有为决定本次准入去遍历该引用全文。
- §4当前loop是物理响应→系统评价→拓扑探索→P&R物理可行性。packaging/interface-aware提前建模、variation-aware指标和calibration/test planning列为可进一步加强的未来方向，不声称已实现或已验证。

## 修正后关闭判断（root独立通过）

本稿真实涉及Transformer动态张量、转换/控制/数据搬运摊销和硬件非理想，并非无关应用。关闭对象只限此v1的本次贡献：决定性原段把机制明确指向既有工作，剩余新的metal-routing陈述仅给约束概述，没有新增可长期采用的执行机制/验收接口或修正原判断的比较证据。综合描述可作原源索引，但未达到当前贡献门槛；不因“综述”标签、无artifact、实验规模或Books主题已有而关闭。不正式评分，不从标题猜公开时刻；贡献前关闭若通过，不为不影响处置的日期另请求材料。

root已实际独立读exact HTML §2.1–2.3/3.1–3.3/4及Refs1–9，认可修正后的贡献前关闭；本日原55家族其他判断不变。本日正式日级Gate另获通过。若以后原核心显示实际新的closed-loop语义/物理可行性反证，只重开本家族，重新准入/日期/必要证据与owner，不扩大论文池；未单独声称root读过ref28论文全文。
