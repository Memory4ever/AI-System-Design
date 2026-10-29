# DAPD：拟采用命题与逐字 PRE（尚未写 Books）

事件：2603.12996v1；03/16 首次 arXiv 日夹证原字段保存在 SUP_DATACITE_BATCH_20261011.jsonl，同稿定点去重没有有效旧 Evidence；Submitted 不作为公开日期。2+1+2=5，具体 attention proxy 相对现有外部 MI estimator 的 schedule 差额深入。root 非准备者实际必要原证 §2.2–4.3、§5/6、A/B/C 与 Ch24 图 MI/commit 邻接比较已通过；作者恢复时直接核 §3.1–3.2/4.3/5、A/B 必要字段，不重开 root 完成结论。

Owner：MULTIMODAL-GENERATIVE-PARADIGMS，Ch24；仅紧接现有 2605.20187 hidden-state MI 图段连续结束标记后，下一 2605.20199 trajectory 段前。目标差额不是 Attention 原理或新增 MRF 保证，而是以内部 attention 替外部依赖估计器及 confidence×degree 的 dynamic commit schedule。Ch23 表示 identity、Ch25 预测 channel 与 Ch24 前后交接保持。

## 逐字拟文（两段）

当额外训练依赖估计器不合算，而 masked model 已能暴露内部 attention 时，可以把对称化的 attention 分数作为依赖代理，在每轮重建 masked positions 的冲突图。按边分数之和估计 degree，再以 degree 与 marginal confidence 的乘积降序扫描，只将和已选节点没有直接边的位置加入当前并行组；这形成的是极大 independent set，不是最大集合，更不保证最少后续轮数。剩余 mask 比例低于一半后切回 confidence threshold，是另一个经验调度分支，不是证明所有剩余变量已经独立。<!-- source-family:SF-2026-ARXIV-2603-12996 -->

内部代理省去额外训练，却仍支付 attention 提取、构图、排序与阈值校准成本；图中无直接边也不排除间接或高阶依赖，不能把 MRF 建模解释当作自然语言联合独立性的保证。[必要机制与对照](https://arxiv.org/html/2603.12996v1)只支持有限 LLaDA/Dream 的质量—步数取舍：前者基线四块加 EOS 处理、该分支单块，后者才统一单块；NFE 不是端到端墙钟或 SLO。代理失准、错误 commit 或总成本不合算时，应回到更小并行组、较多 refinement，或已有 confidence/外部依赖估计分支，而不凭 attention 低值直接签发并行安全。

## 直接证据与未采用

精确 v1 HTML §3.1 L134–151 对称 score/threshold/proxy；§3.2 L152–185 toy 的三变量约束、30 independently trained models/100 paths 与 edge AUC；§4.1–4.3 L188–223 从全图 disconnected 放宽到直接无边、极大非最大/degree heuristic/confidence×degree/50%→0.9；§5 L224–249 质量与步数，§6 L250–268 受限平行任务。AppA/B L319–363：L40S、greedy、max256、LLaDA baseline 4 blocks+EOS 与 DAPD1block，Dream single-block；threshold 随 task/model 调节。precision、batch、concurrency、SLO 与构图总墙钟 Not Disclosed；不复现，不授实现核验。没有采用 speedup 数字或“可安全并行”的定理。

root 仅预留上述两段及本人末注窄锁；等待 review_mar17_18 逐字 PRE 后才写，实际非 writer POST 另验，不授 DAY。
