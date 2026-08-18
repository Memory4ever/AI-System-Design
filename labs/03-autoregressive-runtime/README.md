# Lab 03 — Autoregressive Runtime

## Lab Question

自回归生成怎样把重复计算变成可复用 KV state，并在 sampling、length 与 correctness 之间保持一致？

## Why This Lab Exists

每一步重算完整 prefix 是最简单且可靠的 reference path；序列变长后，重复 attention projection 成为浪费。
KV Cache 保存过去状态，却新增 cache identity、position、lifecycle、memory pressure 与 sampling reproducibility。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `MODEL-KV-CACHE` / `MODEL-SAMPLING` / `MODEL-LONG-CONTEXT` | Ch19～20、22 | 模型级生成与状态语义 |
| `INFER-REQUEST-LIFECYCLE` / `INFER-PREFILL` / `INFER-DECODE` | Ch42～44 | Runtime state machine |
| `INFER-KV-CACHE` | Ch45 | 计算换持久状态的 owner |

## Prerequisites

- 完成 Lab 02，并持有可逐层对齐的 Decoder-only checkpoint。

## System Under Test

单请求 generation loop，包含 Prefill、Decode、KV append、logits processing、sampling 和 termination。Runtime
拥有 cache lifecycle；模型权重拥有 projection semantics；sampler 拥有 token selection。

## Baseline

每生成一个 token 都对完整 prefix 做 full forward。它计算昂贵，但语义直接，是 KV path 的 correctness oracle。

## Step-by-Step Experiments

1. 实现 greedy full-recompute generation，固定 seed、stop 和 maximum length。
2. 分离 Prefill/Decode，记录每层 K/V shape、position 与 valid length。
3. 实现 KV append path，逐 token 与 full-recompute logits 对齐。
4. 加入 temperature、top-k、top-p，区分 logits transform、random state 与 model state。
5. 改变 prompt/output length，建立 compute、KV bytes 和 latency 模型。
6. 注入 cache truncation、position drift、wrong-model cache、rollback 与 context overflow。

## Expected Artifacts

- Full-recompute oracle、KV Decode implementation、sampling tests 与 request-state trace。
- Lab 10 可复用的 request/KV/sampler interface。

## Invariants

- 相同 token history 下，cached 与 recompute logits 在 tolerance 内一致。
- KV length、position、emitted tokens 与 stop state 同一边界提交。
- Cache 不能跨 model/tokenizer/position contract 错误复用。

## Failure Injection

- 删除一个 KV token、交换 layer cache、修改 rope offset、回滚 token 不回滚 KV、复用旧 checkpoint cache。
- 测试 zero/极低 temperature、empty prompt、maximum length 与 early stop。

## Measurements

- TTFT、TPOT、per-step latency、KV bytes/token/layer、recompute FLOPs。
- Cached/recompute numerical error、sampling reproducibility、overflow/rollback recovery。

## Acceptance Criteria

- [ ] Greedy cached Decode 与 full-recompute token/logits 对齐。
- [ ] Sampling random state 与 KV/model state 可独立重放。
- [ ] 至少定位一个 KV 更快但 memory pressure 使其不再合适的区间。
- [ ] 所有 cache corruption 都能被检测或显式标记为 unsupported。

## Trade-offs and Alternatives

Full recompute 在短序列、memory 极紧或 correctness debug 时继续成立；KV Cache 用 memory 换 compute，并把模型
内部中间量升级为 Runtime asset。压缩、淘汰或滑窗只能作为带质量边界的分支。

## Reflection Questions

1. KV Cache 是模型状态还是 Runtime 状态，谁拥有删除 authority？
2. Sampling seed 为什么不足以完整重放请求？
3. Context window 扩大时，compute 与 memory 哪个先成为瓶颈？

## Next Lab Handoff

向 Lab 04 提供 token-level compute/memory 账本；向 Lab 10 提供 request、Prefill/Decode、KV 与 sampler contract。

