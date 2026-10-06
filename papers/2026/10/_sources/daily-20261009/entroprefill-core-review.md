# EntroPrefill：必要证据与 Prefill 采用提案

作者root；仅2026-10-09 Daily / BJT2026-10-08窗口。[精确v1](https://arxiv.org/html/2610.09757v1)，当前官方题摘无撤回信号。公开日由公告ID分配规则与DataCite同日上下界独核，保留官方LG定点未列的局限，详情见arxiv-screening.md。不是把Submitted、Updated或registered单独当first-public。

准入：浅层attention集中不足以批准永久删context→正权重head pooling的丢弃mass包络、独立observer审计与深层稳定性的条件边界→重新考虑裁剪准入及保证范围。评分2+2+2=6，重要条件机制、跨Prefill状态/后续KV与资源接口、稳定可复用边界；标准必要证据完成，拟补Books具体gap深入受影响理论，不提分。root实际读正文§1～9（52～364）、相关证明4.1/4.2、5.1、6.1/6.2及附录A/B的必要常数/反例。未核实现、机器证明、可选代码或实测性能。

机制：完整前层生成同一unpruned reference下候选集合，在选择层gather保留hidden/shallow KV，原position不重编号，深层只跑剩余support；这不是删文本后重新前向。sink隔离后用collision entropy分配head权重并加正floor；整chunk greedy只在逐head/observer discarded-mass约束内删，dual上界拒不可达预算，不声称greedy最优。小pooled mass在低head权重下仍可丢全部该head贡献（4.1反例）；固定QKV行的2Vη只约束该行，不推深层或truth。

审计/限制：proposal、阈值、监测层及observer分布预先固定；独立有放回query observer，Hoeffding+J×heads union同时控制所监层的期望discarded mass，所以选层停止不破坏已建立界。相同样本可跨层复用，但不能用audit结果重调proposal；b大于容差则扩大/精确审计或bypass。不是最坏observer、未来decode或新request总体保证。浅层一致而深层读取被删value的反例拒无条件保证；后层support-transfer、normalizer/算子有界及Lipschitz乘积才给条件首token logit界，margin足够仅同greedy首token，非整段采样相同。此桥接是额外假设，不由rank稳定或浅audit产生，数值界可能vacuous。

费用/证据人口：纯理论无任务benchmark、kernel speedup或非劣证据；模型/硬件/precision/长度/batch/concurrency/SLO实测均Not Disclosed（本文没有实验）。FP32统计、额外attention-row提取、独立observer、score二次pass、gather/临时buffer/跨TP通信与深度不同的batch路由均付费；不保存T×T不等零HBM。GQA组内共同集合不等全组物理union一页或零碎片，decode后选不会减少已转移bytes；辅助费用不足/界太松/bridge失败就保留完整路径。Page-EntroKV未公开手稿不是独立实证，本项不采用其优越性。

唯一owner `INFER-PREFILL`，[Ch43](../../../../../books/part-05-inference-system/43-prefill.md)：实际164～203 index reuse→按方差择层永久缩support→视觉谱裁剪邻接，以及278～308调度交接；Ch44开篇与ROADMAP实际核。既有永久裁剪的方差代理/质量与总费用，不承载proposal与audit独立性、adaptive layer同时界以及首token条件保证范围。Ch45缓存驻留/Top-p不是这项永久support选择的第二owner。

## 最小PRE（未写，待非作者核）

建议在Ch43方差择层永久裁剪完整段后、视觉谱裁剪之前一段：

若要让永久裁剪具有可解释的误差预算，选择提案与验收观察还须分开：预先固定候选、阈值和监测层，用独立的 query-position 样本审计每个 head 的丢弃 attention mass，并同时控制所有可选层，才不会把“挑到一层看起来稳定”当作固定检验通过。这个界只管指定观察分布下的期望丢弃概率质量，不管最坏位置、事实真值或未来 Decode；浅层集中而深层重新读取被删证据的反例，阻止它升级为无条件输出保证。[条件理论](https://arxiv.org/html/2610.09757v1)还需要后层 support-transfer 与算子界，足够 margin 也只保证同一 greedy 首 token，不保证整段生成。Observer、统计提取、gather 与物理页/传输都计费，逻辑删 token 不等按同一比例释放 bytes；论文没有实测加速或非劣质量。界太松、独立性破坏或后层条件无法验证时保留完整 Prefill，不用更积极的 entropy 排名代替验收。<!-- source-family:SF-2026-ARXIV-2610-09757 -->

supplement_20260311非作者实际必要§2～6/8～9与Ch43 150～220完整邻接/PRE通过。root按已核范围实际写Ch43新180单段与自身441章末注；supplement_20260311非writer实际164～198完整邻接、新180及本注回对有效原证，POST通过、锁释放。原ASL/视觉谱分支保留，不授整日完成。
