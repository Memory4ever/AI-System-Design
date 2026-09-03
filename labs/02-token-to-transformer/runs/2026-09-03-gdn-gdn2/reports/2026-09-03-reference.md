# Experiment Report — Lab 02 / 2026-09-03-gdn-gdn2-reference

## Claim

- Hypothesis: GDN-2 在 scalar decay 且 erase/write gates 退化为同一 scalar 时，应与 GDN recurrence 等价；
  独立 gates 应允许 GDN 无法用单一 `beta` 表达的 erase/write 强度组合。
- Expected mechanism: 两种 recurrence 使用相同 fixed-size matrix state，但 GDN-2 分离 Key-side erase 与
  Value-side write。
- Expected validity boundary: 只验证论文公式的前向状态转移，不验证训练可学习性、GPU kernel 或模型质量。

## Workload Contract

| Dimension | Value |
| --- | --- |
| Code / dependency revision | 当前工作树；`src/reference.py`；Python standard library only |
| Dataset / trace / prompt identity | 文件内固定二维 vectors/matrices |
| Model / tokenizer / checkpoint | Not Applicable — recurrence reference only |
| Hardware / topology / runtime | Local CPU；Python 3.9.6 |
| Precision / quantization | Python `float`；平台 double precision |
| Input / output length | 固定状态 `[2,2]`；短手工事件流 |
| Batch / concurrency / arrival | 单样本、串行 |
| Quality threshold / SLO | equivalence error `<= 1e-12`；exact scenarios |
| Seed / repetitions / statistics | deterministic；无随机数 |

## Baseline and Change

- Baseline: scalar `alpha_t`、scalar tied `beta_t` 的 GDN。
- Single changed variable: 将 decay、erase、write 展开成 GDN-2 的独立 channel vectors。
- State/control-flow difference: state shape 不变；只改变 update operator。

## Correctness Evidence

- `python3 -m unittest discover -s tests -v` 必须通过六项测试。
- `python3 src/reference.py` 输出 reduction error、重复写入 delta、正交/相关 Key 读取与独立 gate 状态。
- `python3 -m unittest discover -s tests -v` 已通过八项测试。
- `python3 src/reference.py` 已通过内置 reduction 与 repeated-write assertions。

## Results

| Variant | Correctness | Quality | Latency | Memory | Failure boundary |
| --- | --- | --- | --- | --- | --- |
| GDN reference | 8/8 shared tests passed | Not Measured | Not Measured | 4 state elements | scalar erase/write tied；相关 Key 写入损伤旧关联 |
| GDN-2 reference | reduction error `2.78e-17`；independent gate cases passed | Not Measured | Not Measured | 4 state elements | fixed-state collision remains |

## Sensitivity and Failure Injection

当前 deterministic scenarios 包含正交 Key、相关 Query、相关 Key 写入和显式 reset。完全相同 association
的重复写入 state delta 为 `0`；相关 Key 写入后，原 Key read 从 `[1,0]` 变成约 `[0.36,0.8]`，直接暴露
fixed-state superposition/interference。显式 `alpha=0` reset 后旧 Key read 为 `[0,0]`，新 Key read 为
`[0,1]`。尚未运行 learned Key、有限精度、长序列、不同 decay
分布、negative-eigenvalue erase range 或 recurrent/chunkwise parity。

## Interpretation

- What the evidence proves: 公式实现自洽，GDN 是 GDN-2 的受限形式，独立 gate 扩大单步
  update operator 的可表达集合。
- What it does not prove: GDN-2 gate 能被训练稳定学到、论文 benchmark 可复现、Qwen 应采用 GDN-2。
- New cost and failure modes: 更多 gate projections、kernel/backward 复杂度；fixed-state collision 未消失。
- Where the baseline still applies: scalar gate 已足够、短 Context、实现简单性或 kernel 成熟度优先时。

## Handoff

- Reusable artifacts: recurrence reference、六个 invariants、训练 experiment matrix。
- Required identity/version: GDN `2412.06464v3`；GDN-2 `2605.22791v1`。
- Open questions: learned gate 是否在 context switch 和 multi-key interference 上稳定产生可重复增益？
