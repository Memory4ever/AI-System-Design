# GDN / GDN-2 选择性记忆实验

> Status: Phase 0 E1 Complete；训练实验尚未运行。

## 实验要回答什么

本实验不试图用小模型复现论文中的最终排名，而是依次回答四个可证伪问题：

1. Gated DeltaNet 是否确实把“快速全局遗忘”和“沿当前 Key 定向改写”组合在同一状态转移中？
2. GDN-2 的收益是否来自 erase/write 解耦，而不是更多参数、更多训练 token 或不同评测流程？
3. 固定大小 recurrent state 在 context switch、重复表述和多 Key 干扰下，何时优于或弱于显式 Attention？
4. 为什么 Qwen 采用 GDN 与显式 Attention 的 hybrid，而不是把所有层都替换成 GDN？

Stable Knowledge Node 为 `MODEL-LONG-CONTEXT`。本实验属于 Lab 02 的 token mixer 分支，向 Lab 03
交付逐 token recurrent state、reset boundary 和 serving-state contract。

## 从论文重新浮现问题

### 1. Full Attention 的成本来自显式历史

Full causal Attention 为当前 Query 保留对所有历史 Key/Value 的直接访问：

```text
优点：可以重新读取原始 token，精确 retrieval 能力强
代价：Prefill pair compute 随 T 近似二次增长，Decode KV state 随 T 增长
```

Linear Attention 改变乘法顺序，把历史压缩成固定大小矩阵状态。采用 GDN-2 论文的 shape 约定：

```text
S_t: [d_k, d_v]
k_t, q_t: [d_k]
v_t: [d_v]
o_t = S_t^T q_t: [d_v]
```

状态不再随序列长度增长，但有限维矩阵会叠加多个 association。Key 不正交或状态容量饱和时，
retrieval collision 无法通过增加 Context Window 自动消失。

### 2. Decay-only 与 Delta-only 各自缺少什么

Decay-only recurrence 可以通过较小的 `alpha_t` 快速清空旧上下文，但它会同时衰减其他仍有用的关联。
Delta rule 沿当前 Key 读取旧 Value，只写 prediction error，因此能够定向替换 association；它却只能一次修改
当前 Key 方向，面对完整 context switch 时不擅长快速清空大量旧状态。

Gated DeltaNet 将两者组合：

```text
S_t = alpha_t (I - beta_t k_t k_t^T) S_(t-1)
      + beta_t k_t v_t^T
```

`alpha_t` 负责全局 decay，`beta_t` 同时控制当前 Key 方向的 erase 和新 Value 的 write。原论文因此没有只比较
GDN 与 Transformer，而是把 Mamba2-like decay、DeltaNet、GDN 以及 hybrid 分支放在同一证据链中。

### 3. GDN-2 为什么还要拆 gate

GDN 和 KDA 的 `beta_t` 同时承担两个不同决策：旧状态沿 Key 侧擦除多少，以及新 Value 写入多少。GDN-2
把它们拆成独立的 channel-wise gate：

```text
e_t = b_t elementwise_mul k_t
z_t = w_t elementwise_mul v_t

S_t = (I - k_t e_t^T) Diag(alpha_t) S_(t-1)
      + k_t z_t^T
```

- `alpha_t: [d_k]`：Key channel-wise background decay；
- `b_t: [d_k]`：erase 使用哪些 Key coordinates；
- `w_t: [d_v]`：提交哪些 Value coordinates。

当 `alpha_t` 退化成 scalar，且 `b_t = w_t = beta_t * 1` 时，GDN-2 精确退化为 GDN。论文的 gate
ablation 在运行时把某个 channel gate 求均值再广播，同时保留原 projection，正是为了避免把参数量差异误当成
机制收益。本实验沿用这一控制方法。

论文报告的完整结论绑定 `1.3B` 参数、`100B` FineWeb-Edu tokens、匹配的 recurrent-state size 和作者
训练 recipe。本文的小实验只能检验机制方向和 failure boundary，不能复述成同等规模的质量结论。

## 从机制到 Qwen 架构

下面是依据公开报告可以重建的设计验证链，不代表未公开的内部研发时间线：

```text
Full Attention
  精确访问历史，但长序列计算和 KV state 昂贵
        |
        v
SWA hybrid
  局部成本受控，但窗口外信息只能跨层间接传播
        |
        v
GDN hybrid
  多数层维护固定 recurrent state，周期性 Attention 补回直接 token retrieval
        |
        v
Qwen 3:1 layout
  3 x GDN + 1 x global/gated Attention
        |
        v
Qwen3.8-Flash-Next
  3 x GDN + 1 x Qwen Sparse Attention，再与 MoE、Gated Residual、n-gram
  embedding、MTP 和训练稳定性 recipe 联合验证
```

Qwen3.8-Next 报告不是用一次大训练直接押注新架构。其公开 ablation 固定为 `28-layer 25B-A3B MoE`，先用
`400B tokens / 4K context` 预训练，再用 `80B tokens / 32K context` 继续训练，对比 full Attention、
`3 x SWA + 1 x full Attention` 和 `3 x GDN + 1 x full Attention`。报告同时检查 loss/downstream quality、
training/prefill/decode cost，以及 hyperparameter optimum/training stability。

最终公开模型仍保留固定比例的显式 Attention，说明 GDN 的 fixed-state memory 与直接 token-level retrieval 是互补
关系。Qwen3.8-27B 的公开布局是 `16 x [3 x GDN + 1 x Gated Attention]`；Qwen3.8-Flash-Next 则是
`12 x [3 x GDN + 1 x Qwen Sparse Attention]`，并在每层配 MoE。当前公开架构使用的是 GDN，不能把本实验的
GDN-2 candidate 写成 Qwen 已采用的事实。

## 实验总览

| Phase | 单一问题 | Baseline / Candidate | 主要证据 | 目标 Level |
| --- | --- | --- | --- | --- |
| 0 | 两个 update rule 是否按论文公式工作？ | GDN / GDN-2 受限形式 | 数值等价、no-op、重复写入、context switch | E1 |
| 1 | gate 解决了哪类记忆问题？ | decay-only / DeltaNet / GDN / KDA / GDN-2 | overwrite、reset、collision、state churn | E2 |
| 2 | 学习后是否仍有相同方向？ | 同 shape、同 token、同 optimizer 的 tiny models | loss、query accuracy、gate/state trace | E2～E3 |
| 3 | 为什么需要 hybrid？ | Full / SWA hybrid / pure GDN / GDN hybrid / GDN-2 hybrid | quality、length sensitivity、state bytes | E3 |
| 4 | kernel 是否兑现算法收益？ | recurrent reference / chunkwise kernel | parity、tokens/s、HBM、break-even length | E3 |

## Phase 0：公式级 Reference

当前目录提供零第三方依赖实现，只用于确认状态转移，不声称代表生产 kernel 性能。

```bash
python3 src/reference.py
python3 -m unittest discover -s tests -v
```

必须成立的 invariants：

- GDN-2 在 scalar decay 且 `b = w = beta` 时与 GDN 数值一致；
- `b = 0, w = 0, alpha = 1` 时状态不变；
- 相同、已写入的 Key/Value 再次执行 unit-strength Delta update 时，state delta 为零；
- 正交 Key 可以在容量允许时共存；相关 Key 会产生可测量 interference；
- 请求级 reset 必须由 runtime 清空 state，不能把模型 gate 当安全隔离。

## Phase 1：受控关联记忆

### Workload A：Selective overwrite

生成 `WRITE(key, value)`、`QUERY(key)` 事件流。每个序列先写入多组关联，再随机覆盖其中一部分。

指标：

- latest-value query accuracy；
- 未被覆盖 Key 的 preservation accuracy；
- 每次写入的 `norm(S_t - S_(t-1))`；
- 错误答案来自旧 Value、其他 Key 还是随机输出。

这个 workload 验证 Delta rule 的定向改写。只使用 passkey、从不发生覆盖，无法证明 erase/write 机制。

### Workload B：Context switch

序列包含两个 namespace，中间插入明确 boundary token。第二段复用一部分 Key，但 Value mapping 完全变化。

```text
namespace A writes -> A queries -> boundary
namespace B writes -> B queries -> delayed A/B probes
```

同时测量：切换后的 B accuracy、A-to-B leakage、旧记忆保留和恢复能力。删除 delayed probe 会把“成功清空”与
“灾难性遗忘”混为一谈。

### Workload C：Multi-key interference

逐步增加 active Key 数量，并控制 Key cosine similarity。长度不是唯一自变量：

```text
orthogonal keys -> mildly correlated keys -> clustered keys -> aliases/paraphrases
```

记录 accuracy 随 `number_of_keys / d_k`、Key similarity 和 distractor length 的变化。它对应论文中 MK-NIAH
所测试的 competing associations，但本实验结果不能冒充 RULER 分数。

### Workload D：Erase/write decoupling

构造两类彼此冲突的事件：

- 强 erase、弱 write：旧 association 已失效，但当前 token 只提供低置信度候选；
- 弱 erase、强 write：允许新 evidence 与旧 association 暂时共存。

主要对照不是只有 GDN 和 GDN-2，而是：

```text
GDN-2 full channel b + channel w
GDN-2 scalar b + channel w
GDN-2 channel b + scalar w
GDN-2 scalar b + scalar w
```

所有分支保留相同 projection 参数，只在运行时 average-and-broadcast gate。这样才能把 channel structure
的效果与参数量分开。

## Phase 2：同预算 Tiny Model

训练环境使用 PyTorch 与官方 FLA/Triton 实现时，先记录精确 commit 和 license；不得复制本目录的纯 Python
reference 去做性能结论。建议从 `20M～50M` 参数、`100M～500M` training tokens 开始，观察趋势后再决定是否
扩大预算。几张 L20 足以完成这种机制学习实验，但不足以复现论文 `1.3B / 100B tokens` 合同。

固定项：

- tokenizer、dataset order、train/validation split；
- layer count、`d_model`、FFN、recurrent-state shape；
- global token batch、optimizer、LR schedule、warmup、precision；
- training token budget、evaluation steps、checkpoint selection rule；
- 三个最低 seeds，五个 seeds 用于最终判断。

Variants：

```text
V0 decay-only
V1 DeltaNet
V2 GDN
V3 KDA
V4 GDN-2
V5 GDN-2 with scalarized erase
V6 GDN-2 with scalarized write
```

模型参数不能完全匹配时，同时报告实际参数量，并增加 equal-parameter capacity control。不得通过缩小 GDN-2
主干后只比较最终 loss 来声称 gate 无效。

训练期间每个 checkpoint 记录：validation loss/perplexity、gradient norm、update norm、gate distribution、
state norm、NaN/overflow、tokens/s。Loss 下降不代表关联记忆成立，必须同步运行 Phase 1 probes。

## Phase 3：Qwen 风格 Hybrid Ablation

先在 `8` 或 `12` 层 tiny model 上固定 `3:1` 周期：

| ID | Layer layout | 回答的问题 |
| --- | --- | --- |
| H0 | all Full Attention | 精确历史访问 baseline |
| H1 | `3 x SWA + 1 x Full` | 局部窗口是否已经足够？ |
| H2 | all GDN | fixed state 的质量上限在哪里？ |
| H3 | `3 x GDN + 1 x Full` | periodic exact retrieval 能否补回 pure GDN 缺口？ |
| H4 | `3 x GDN-2 + 1 x Full` | 更细 state editing 是否继续改善 hybrid？ |

按 `512 / 2K / 4K / 8K` context length 测量：

- validation loss 与下游 task accuracy；
- S-NIAH、MK-NIAH、context switch、paraphrase churn；
- training throughput、Prefill latency、Decode latency；
- peak HBM、KV bytes、recurrent-state bytes；
- failure rate 和不同 seed 的置信区间。

H4 只是候选设计。即使小实验优于 H3，也不能推出 Qwen 应替换成 GDN-2；还需要规模迁移、kernel、训练稳定性、
checkpoint compatibility 和完整 downstream regression。

## Phase 4：执行路径与 Kernel

Reference recurrence 验证语义；recurrent kernel 和 chunkwise WY kernel 验证执行。两者先做 forward/backward
parity，再测性能：

```text
token-by-token recurrent
chunkwise training: chunk = 64 / 128 / 256
sequence length: 512 -> 32K
batch/token budget: fixed and disclosed
dtype: BF16/FP32 accumulator contract disclosed
```

需要分别报告短序列固定开销和长序列 scaling。某个 Triton kernel 比另一个实现快，不能证明 GDN-2 的模型语义
更好；模型质量提高也不能证明 kernel 已达到可部署效率。

## 决策规则

只有同时满足以下条件，才能把结论写成“该 workload 下支持 GDN-2”：

1. GDN-2 相对 GDN/KDA 在至少三个 seeds 上改善预注册的 primary metric；
2. scalarized gate ablation 能定位增益来自 erase、write 或两者；
3. 参数量、训练 token、数据顺序与 checkpoint selection 已受控；
4. improvement 没有以明显更差的 LM loss、训练稳定性或 serving cost 为代价；
5. 至少观测到一个 GDN-2 仍然失败的 collision 或 context-switch boundary。

以下结果必须保持“不确定”：

- 只在一个 seed 或一个 context length 上领先；
- 只比较最佳 checkpoint，没有固定 selection rule；
- GDN-2 使用了不同 optimizer、更多 token 或更大的 state；
- 只有 loss，没有 retrieval 和 state-transition probe；
- 只有 kernel throughput，没有 output/gradient parity。

## L20 执行顺序

- [x] Phase 0 reference 与八项单元测试。
- [ ] 冻结官方实现 commit、依赖、容器和 license boundary。
- [ ] 先跑 `smoke`：每个 variant `1 seed / 1M tokens`，只验证控制流与指标完整。
- [ ] 跑 Phase 1：五类 state-update mechanism probes。
- [ ] 跑 `pilot`：`3 seeds / 100M tokens`，淘汰明显不稳定配置。
- [ ] 跑 GDN-2 gate scalarization ablation，参数保持不变。
- [ ] 跑 `3:1` hybrid，对比 Full/SWA/GDN/GDN-2。
- [ ] 扩大到 `500M tokens` 前冻结 primary metric 和 early-stop rule。
- [ ] 运行 512～32K length sensitivity 与 recurrent/chunkwise parity。
- [ ] 填写报告，明确证明范围、失败边界和下一实验。

实验矩阵的机器可读版本见 [experiment-matrix.json](configs/experiment-matrix.json)，Phase 0 首次运行记录见
[reference report](reports/2026-09-03-reference.md)。

## Primary Sources

- Gated DeltaNet paper, exact reviewed version `arXiv:2412.06464v3`:
  https://arxiv.org/html/2412.06464v3
- Gated DeltaNet official implementation:
  https://github.com/NVlabs/GatedDeltaNet
- Gated DeltaNet-2 paper, `arXiv:2605.22791v1`:
  https://arxiv.org/html/2605.22791v1
- Gated DeltaNet-2 official implementation and disclosed recipe:
  https://github.com/NVlabs/GatedDeltaNet-2
- Qwen3.8-Next architecture report, `arXiv:2608.30320v1`:
  https://arxiv.org/html/2608.30320v1
- Qwen3.8-27B official model card:
  https://huggingface.co/Qwen/Qwen3.8-27B
- Qwen3.8-Flash-Next official model card:
  https://huggingface.co/Qwen/Qwen3.8-Flash-Next

Source-code licenses must be checked separately from paper licenses before copying or modifying official implementation code.
