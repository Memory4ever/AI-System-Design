# 2026-05-07 Root Books 写回队列

**状态：** 3/3 已由 root 写回；待新的非作者 Gate  
**禁止动作：** 不处理已撤销的 Review-notes 误报，不把 No Change 项强行写入正文

## 1. 2605.04279 → `MODEL-MULTI-HEAD-ATTENTION`

- 文件：`books/part-02-model/15-multi-head-attention.md`
- 缺口：现有章节解释 head 子空间、聚合、冗余与协作，但没有写明 head score/output 经共享 token trajectory 与球面
  投影耦合；score/head 正交不推出每头能量或聚类过程独立单调。
- 需写入：总能量可形成梯度流，per-head monotonicity 受到 radial shadow 阻碍；Radial Dominance 是充分条件而非真实
  Transformer 普遍事实。
- 边界：定理主要依赖 sphere-normalized、score symmetry、scalar/equiangular 等条件；不能写成 heads 已被证明拥有
  通用独立功能或真实训练一定按该动力学聚类。
- Handoff：Ch14 仍拥有单头 Q/K/V 内容路由；Ch15 只拥有多头交互与聚合动力学。

## 2. 2605.04291 → `MULTIMODAL-GENERATIVE-PARADIGMS`

- 文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 缺口：现有 AR → masked/diffusion → iterative correction 主线没有说明如何复用预训练 causal/masked LM 的条件分布
  来定义 Glauber transition，而不是从均匀 corruption 重新训练。
- 需写入：逐位置条件重采样可视为 mask-infilling；共享 causal/masked 权重提供 energy/stationary-distribution proxy，
  反向过程用多轮局部 revision 换全局纠正。
- 边界：有限步 sampler 不等于已收敛 stationary distribution；NFE、32×H100 训练成本、streaming 与 end-to-end SLO
  均是新增代价。低延迟 append-only workload 仍回退 AR。
- Handoff：Ch24 拥有 factorization/revision/commit；训练资源与 serving 调度分别交给 Part IV/V。

## 3. 2605.04569 → `INFER-TENSORRT-LLM`

- 文件：`books/part-05-inference-system/49-tensorrt-llm.md`
- 缺口：章节已有 sparse kernel 的 execution identity 与 dense fallback，但缺少 query-specific approximation-risk 在 full
  attention 与低阶近似路径之间做动态路由。
- 需写入：先做 context K/V saliency 预选，再用 query sharpness/error proxy 选择 full attention 或 blockwise zeroth-order
  Taylor sparse attention；proxy 只能提出执行路径，runtime 以支持形状、误差预算和 fallback 保持 correctness owner。
- 边界：约 60% attention-module latency 与约 1.47× end-to-end 只属于 LIVEditor-14B、作者视频编辑 benchmark、硬件与
  阈值；“near-lossless”不是通用保证。proxy 漂移、unsupported shape 或质量预算越界时回退 full attention。
- Handoff：Ch15 解释模型语义，Ch49 只拥有 lowering/kernel/path commit。

## 写回结果与待验收项

三项均已有真实机制正文、唯一 source-family marker 与 exact-v1 Review note。root 已确认正文位于唯一章末
`## Review notes` 之前，并通过 scoped diff-check；这些是作者交接证据，不替代新的非作者 reviewer 对前后段顺读、
语义边界、旧方案保留与状态一致性的最终验收。
