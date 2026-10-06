# mHC v1：限定证据与 Books 增量

本窗2026-01-01T09:00:00+08:00～2026-01-02T09:00:00+08:00。Source Family `SF-2026-ARXIV-2512-24880`；审阅者root；独立证据复核jan01_v3。primary：[精确v1 HTML](https://arxiv.org/html/2512.24880v1)。访问2026-10-02。当前摘要页无官方撤回标记；没有遍历其他版本。精确日期原值见[MHC_DATE.json](./MHC_DATE.json)：Submitted不是公开；假期公告、ID分配规则及DOI注册只共同支持本日内的保守公开区间，不把注册时刻冒充首公开时刻。

## 采用的命题及机制

单流residual的恒等carry是低成本稳定接口；多流HC增加连接组合能力，但读取`H_pre`、跨层carry`H_res`和写回`H_post`责任不同。Intro Eqs3–4表明carry成为矩阵乘积，无约束可能放大/削弱及改变均值；不是所有HC或所有输入必然失稳。§4.1 Eq6限制carry为非负row/colsum1的双随机矩阵，理想算子保均匀方向与流均值，乘积闭合且谱范数≤1。这不是任意方向等距，均匀平均可消灭差异；输入相关`M(X)X`导数还含`DM(X)[δX]X`，加上read/write与F导数，不能证明完整Jacobian或所有梯度稳定。

§4.2 Eqs7–9以输入相关映射、pre sigmoid/post 2sigmoid与20轮Sinkhorn参数化；pre/post并非双随机。有限轮及舍入只近似，须测试约束残差与跨深度积累。§5.4 Fig7的约1.6是27B选定序列tokens平均后的composite Amax row/column-sum gain，不是spectral norm或任意输入上界。作者的identity/防vanishing表述比本文可采用的数学结论更强，未沿用。

## 执行代价与评价边界

§3.2 Table2只计stream维护而非F内部；扩大n提高访存/激活，不因单子层FLOPs不变就证明总执行成本不变。§4.3公开mixed-precision融合（TF32映射、BF16state、FP32部分归约）、选择性重算和DualPipe通信重叠设计；重算不能跨pipeline stage边界，长persistent kernel可能影响通信调度。没有独立核验代码或复现实验，不以不可得可选artifact否定论文可支持的数学命题。

§5.1/Appendix A.1：DeepSeek-V3式MoE的3B/9B/27B规模、n=4，active parameters 612M/1.66B/4.14B；4096 sequence，global batch 320/512/1280，39.3B/105B/262B训练tokens，AdamW。另3B/1T缩放实验须与主实验分开。硬件、seed重复及统计区间Not Disclosed；并发/TTFT类serving SLO不适用训练稳定命题。§5.2八项零/少样本评价并非全项提高（MATH HC26.4 vs mHC26.0），不能授统一质量优势。作者n4/6.7%时间开销不作为普遍值或端到端生产保证。

## 知识归属与实际差异

评分拟2+2+3=7，深入范围仅上述采用命题及关键反证。Owner `MODEL-TRANSFORMER-LAYER`，current/legacy Ch17。现有“多流混合还要保留哪些几何约束”已解释上下奇异值、orthogonal、finite Sinkhorn/exact chart/Cayley分支，却缺双随机守恒的对象及read/carry/write机制起点。新增角色公式与守恒/非保证段落，再在原Sinkhorn段加入有限实现约束误差；不新建变体列表。相邻Ch16仍拥有子层MLP，Ch18仍拥有完整causal生成接口，未把runtime调度或全网训练配方搬进Ch17。

jan01_v3已实际读原文§4.1/4.2/5.4、3.2/4.3必要部分及Ch17局部/16末18首，确认上述窄证据与差异，要求精确限定1.6的Amax而非谱范数，已落实。root实际写入Ch17；jan01_v3实际读438–470、末注、限定diff及本笔记，确认角色公式、守恒/非保证、有限近似和原几何分支的衔接，actual POST通过。此结果仅验收本项，不代替Jan02整体日级Gate。
