# Lab 05 — Multimodal Representation & Generation

## Lab Question

图像、文本或其他模态怎样进入共享计算，同时保持 representation identity 与生成范式的语义边界？

## Why This Lab Exists

把所有输入都展平成 token 能复用 Transformer，却可能丢失空间、时间、尺度与 modality provenance。单一
autoregressive factorization 易于定义 likelihood 和 cache；Diffusion/masked refinement 增加并行修正机会，也新增
schedule、editable state 与停止条件。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `MULTIMODAL-REPRESENTATION` | Ch23 | Encoder、fusion、identity owner |
| `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 | AR/Diffusion/masked generation semantics |
| `MODEL-SELF-ATTENTION` / `MODEL-DECODER-ONLY` | Ch14、18 | 文本 Transformer baseline |

## Prerequisites

- 完成 Lab 02 和 Lab 03。
- 理解 image patch、sequence mask、conditional generation 与重建误差。

## System Under Test

一个小型 text+image 或 synthetic-grid workload。Modality encoder 拥有 raw-to-token conversion，fusion layer 拥有
cross-modal interaction，generation loop 拥有 proposal/update/commit。

## Baseline

分别训练/运行单模态 encoder，再用 late fusion 合并最终特征。它在模态弱耦合、独立升级和低成本部署时仍合理。

## Step-by-Step Experiments

1. 固定文本 token 与图像 patch 的 shape、timestamp/modality/provenance identity。
2. 对照 late fusion、early concatenation 与 cross-attention，保持 encoder/parameter budget 可比。
3. 构造必须跨模态对齐的任务，测试 modality drop、错位与缺失输入。
4. 以小离散空间实现 causal AR generation，并记录 token-by-token committed state。
5. 实现 masked iterative refinement，记录 proposal、editable positions、schedule 与 final commit。
6. 比较质量、并行度、cache、rollback 与停止条件，不把不同模态的指标直接拼接。

## Expected Artifacts

- Modality-aware token contract、三种 fusion baseline 与缺失模态测试。
- AR/refinement generation traces，供 Lab 06 作为 observation representation。

## Invariants

- Token 保留 modality、position/time 与 source identity。
- 缺失模态与 padding 有显式 mask，不能被当成有效 observation。
- Iterative proposal 在最终 commit 前保持可编辑，AR committed prefix 不被静默改写。

## Failure Injection

- 打乱 image patches、错配文本和图像、删除 modality tag、改变 resolution/token count。
- 使用错误 schedule、过早停止、重复更新已 committed position。

## Measurements

- Alignment/reconstruction/task quality、calibration 与 missing-modality degradation。
- Tokens/patches、attention cost、iterations、latency、memory 与 proposal correction rate。

## Acceptance Criteria

- [ ] 至少两种 fusion 机制在同一任务上完成受控比较。
- [ ] Representation identity 错误能被检测并形成可解释失败。
- [ ] AR 与 refinement 的 state/commit 差异可从 trace 中复算。
- [ ] 报告指出各范式成立的 workload，而不是宣称单向替代。

## Trade-offs and Alternatives

Early fusion 增加细粒度 interaction，也增加 token cost 与 coupling；late fusion 更模块化但可能错过局部对齐。
AR 的因果状态简单、串行；iterative refinement 增加并行修改，却需要 schedule、cache invalidation 与 convergence gate。

## Reflection Questions

1. 共享 hidden dimension 是否等于共享语义空间？
2. 哪些 representation loss 会被最终质量指标掩盖？
3. Proposal 可编辑时，cache 和 provenance 应怎样更新？

## Next Lab Handoff

向 Lab 06 交付带 modality/time/provenance 的 observation tokens，以及 AR/refinement 的 proposal/commit trace；下一步
引入 action 和 environment transition。

