# 第19章 KV Cache

**Knowledge Tree:** Part II 模型：一个 Token 如何变成答案
**Stable Knowledge Node ID:** `MODEL-KV-CACHE`
**Legacy Chapter:** Ch19
**Status:** Draft

**Roadmap Intent:** 为什么生成时要缓存历史 Key/Value，它如何改变推理系统设计。

## 本章要回答的问题

Decoder-only 模型每次只生成一个新 token。如果前缀中历史 token 的 K/V 已经计算过，为什么还要在下一步重新投影？KV Cache 保存什么、为什么不保存 Query，又怎样从模型优化变成运行时状态？

本章的核心判断是：**KV Cache 用逐层保存历史 Key/Value，避免自回归 Decode 重复计算不变前缀；它用显存与状态管理换取更少计算。**本章解释 cache 的模型来源和 shape；Part V 第45章负责 runtime capacity、生命周期、复用与 offload，第47章负责分页映射，第56章负责调度。

## 不使用 Cache 会重复什么

假设 prefix 已有 `t` 个 tokens，要生成第 `t+1` 个 token。最朴素做法是把完整 prefix 再送入所有 `L` 个 Transformer layers：

```text
[x_1,...,x_t]
-> recompute Q/K/V for every historical token
-> recompute all layer hidden states
-> use last position logits
```

下一步 prefix 变成 `t+1`，系统又从头处理 `[x_1,...,x_(t+1)]`。历史 token 的表示在 causal model 中不会因未来 token 出现而改变：位置 `i` 不能读取 `j>i`，因此它对应的 K/V 是可复用的。

如果仍反复重算，生成越长，重复工作越多。

## 为什么缓存 Key 和 Value

第14章单 head Attention：

```text
Attention(q_t,K_<=t,V_<=t)
= softmax(q_t K_<=t^T / sqrt(d_h) + mask) V_<=t
```

生成新 token 时，只需要新位置的 Query 去匹配全部历史 Keys，并聚合历史 Values。历史 K/V 已由各自 hidden state 投影得到，可以追加保存：

```text
K_cache = [k_1,k_2,...,k_t]
V_cache = [v_1,v_2,...,v_t]
```

新一步只计算：

```text
q_(t+1), k_(t+1), v_(t+1)
```

然后：

```text
K_cache <- append(k_(t+1))
V_cache <- append(v_(t+1))
```

## 为什么不缓存历史 Query

Query 表示“当前位置要读取什么”。生成第 `t+1` 个 token 时，需要的是新位置的 `q_(t+1)`；历史 `q_i` 已经完成过自己的读取，不会被未来位置再次用作 Key 或 Value。

同理，历史 Attention output 和 MLP output 也不直接供新 Query 匹配。真正跨 Decode steps 被 attention 读取的是每层历史 K/V，因此 cache 只保留它们。

这不是说其他中间状态毫无价值，而是它们不属于标准自回归 Attention 的最小可复用状态。

## 每层 Cache 的 shape

设：

- `B`：当前 cache batch/request 数。
- `T`：已缓存 sequence length。
- `H_kv`：Key/Value head 数。
- `d_h`：每个 head dimension。
- `L`：Transformer layer 数。

每层逻辑 shape 通常表示为：

```text
K_cache_l [B,H_kv,T,d_h]
V_cache_l [B,H_kv,T,d_h]
```

有些实现使用 `[B,T,H_kv,d_h]` 或分块 layout。逻辑元素数量相同，物理 layout 会影响 kernel 和 memory manager。

整个模型需要为每个 Attention layer 保存一组 K/V：

```text
KV elements = 2 * L * B * T * H_kv * d_h
```

若每个元素占 `b` bytes：

```text
KV bytes = 2 * L * B * T * H_kv * d_h * b
```

公式里的 `2` 表示 Key 与 Value，不是 double buffering。

这里的“容量”只应理解为 tensor 元素数或乘上 dtype 后的物理存储量。`2 * H_kv * d_h` 表示一个 token、一个 layer 留下两组各含 `H_kv * d_h` 个数值的 K/V 状态；它不是 Shannon entropy，也不能单凭 shape 推出多少 bit 是独立、可压缩或对任务有效的信息。KV dimensions 可能相关、冗余或未被充分利用，因而必须区分：

```text
logical elements       = 2 * H_kv * d_h
physical bytes         = logical elements * b
effective information  = cannot be derived from tensor shape alone
```

这个写法假设 batch 内每个请求都按同一长度 `T` 计量。若活跃请求长度分别为 `T_r`，更准确的逻辑元素数是：

```text
KV elements = 2 * L * H_kv * d_h * sum_(r=1)^B T_r
```

`B*T` 可以是等长 batch 的精确值，也可以是 padding 后的容量上界；生产 runtime 的实际物理占用还会受 block size、alignment、replication 和 metadata 影响。

## 一个容量小例子

取一个极小模型：

```text
L = 2
B = 1
T = 4
H_kv = 2
d_h = 3
b = 2 bytes
```

KV Cache 为：

```text
2 * 2 * 1 * 4 * 2 * 3 * 2
= 192 bytes
```

若只把 `T` 从 4 增到 8，其他条件不变，cache 变成 384 bytes，呈线性增长。真实模型的 `L`、`T`、并发和 head dimensions 大得多，因此 KV Cache 会成为显存容量主项。

## Prefill 与 Decode 怎样写 Cache

Prefill 已知完整 prompt，可以并行计算 `T_prompt` 个 positions：

```text
prompt ids [B,T_prompt]
-> all layers
-> write K/V for every prompt position
```

完成后，每层 cache 长度为 `T_prompt`。

Decode 每步只有一个新 token：

```text
new token [B,1]
-> compute one new K/V per layer
-> read historical cache
-> append new K/V
-> cache length T <- T+1
```

因此 Prefill 主要批量创建状态，Decode 逐步读取并增长状态。Part V 会进一步分析两阶段的 compute、bandwidth 与调度差异。

## 计算复杂度怎样变化

无 cache 时，第 `t` 步重新运行长度 `t` 的完整序列。仅 dense Attention 的前缀成对计算约为 `O(t^2)`，MLP/projection 也对全部 `t` 个 positions 重做。跨多个生成 steps 累积会非常昂贵。

有 cache 后，第 `t` 步只为新 token 做 projection 和 MLP，并让一个 Query 读取 `t` 个 Keys/Values：

```text
per-step attention ~ O(t * d_h) per head
```

跨输出长度求和仍随总生成长度近似二次增长，因为每个新 Query 要读取更长历史；KV Cache 没有让 Attention 变成常数成本。它消除的是对历史 token projection 与 hidden states 的重复计算。

所以应避免模糊地说“KV Cache 把所有推理从 O(n^2) 变成 O(n)”。必须注明是在比较单个 Decode step、Attention 部分还是完整生成过程。

## MHA、GQA、MQA 怎样影响容量

第15章已经定义：

```text
MHA: H_kv = H
GQA: 1 < H_kv < H
MQA: H_kv = 1
```

在其他变量相同时，KV bytes 与 `H_kv` 成正比。假设 `H=32`：

```text
MHA H_kv=32
GQA H_kv=8   -> cache约为MHA的1/4
MQA H_kv=1   -> cache约为MHA的1/32
```

这是逻辑元素数比较，不含 alignment、block allocation 和 metadata。减少 KV heads 可能影响模型质量与训练方式，属于架构 trade-off，不是 runtime 免费压缩。

## 哪些状态可以省掉，必须由模型决定

减少 `H_kv` 是沿 head 维共享，继续压缩还可以考虑 depth 维或 K/V 的表示方式。但这些分支都先改变模型允许复用的对象，再由 runtime 执行，不能从显存紧张直接推导出丢弃状态的许可。

### Depth-wise KV Sharing 是 Model Contract，不是 Runtime Eviction

标准 KV Cache 默认每层拥有独立 K/V，因为不同层表示不同 computation stage。若训练时显式学习某层读取自身
KV、相邻层 KV 或共享 source layer，模型可以减少 depth 维的 KV states；runtime 随后只 materialize 被 checkpoint
允许的 sharing strategy：

```text
trained routing/sharing policy
+ layer/head/model revision
→ physical KV ownership and layout
→ decode reads under the same mapping
```

这与运行时根据 pressure 任意丢弃层 KV 不同：后者会改变已训练函数。Sharing 减少 memory/bandwidth，也增加
checkpoint compatibility、prefix/cache identity、kernel dispatch 和 graph capture 复杂度；错误 mapping 会返回
形状正确但语义错误的 state。通用已训练模型、需要 layer-local fidelity 或 backend 不支持该 layout 时，per-layer
KV 仍然成立。Stochastic KV Routing 是训练期 adaptive sharing 的 Experimental 证据，不支持 post-hoc 套用于任意模型。

共享策略还必须对齐缓存的生产历史，而不只对齐读取地址。一个共享core的分支在训练中先用普通Attention生成donor KV，再从同一seed重跑、让所有core blocks读取它；部署时，新token却通过共享历史计算并写回下一份donor，后续token继承的是递归生成的缓存。即使输入始终给ground-truth token，两种hidden-state历史也不相同。可在训练末段约束两遍产生的donor接近，但这只在训练所见历史上施加局部一致性，不认证全部递归历史等价。[受限FineWeb对照](https://arxiv.org/html/2610.33360v1#S4.SS3)支持减小continuation损失，仍有full-cache质量代价；较少持久KV也曾对应更慢的实测decode。双遍训练、辅助目标与workspace都要付费，纯并行chunk loss或cache集合数不能替代真实continuation与延迟验收；生产历史失配或质量不稳时，保留逐层/逐loop独立缓存。<!-- source-family:SF-2026-ARXIV-2610-33360 -->

### KV 的逻辑最小状态可以由训练结构重新定义

GQA/MQA 仍缓存显式 K 与 V，只是改变 head sharing；更激进的结构让 content key 可由 grouped value 重构，从而缓存 V 与独立 positional key，而不再固定保存原始 `K+V`。这不是 runtime 对任意 checkpoint 的无损压缩，而是训练、Attention 参数化与 decode kernel 共同定义的新 state contract：重构函数、group layout、position representation 和模型 revision 必须同时匹配。<!-- source-family:SF-2026-ARXIV-2609-13285 -->

收益是缩小理论缓存对象，代价是专用训练、额外重构计算和 kernel 复杂度。当前证据来自 350M 模型与 30B training tokens，且缺少端到端 decode kernel；无法证明质量和延迟同时成立时，GQA/MQA 的显式 KV 仍是可靠基线。

保留完整token流也不要求保留原来每head的完整K/V：转换已有GQA时，可以分别聚合positional keys，把content K/V写成低秩latent并在读取时重建；text与vision统计不同，还可给latent配置不同映射与层位预算。但head-wise QK-Norm的scale随输入变化，通常不能直接吸收入固定线性合并；只有在受测norm集中、经校准验证近似后，才有采用共享线性替身的依据，而非由高维本身证明无损。

[受限M2LA转换](https://arxiv.org/html/2606.12195v1)还需恢复训练和长context训练，保留token数不等保留原函数或细节质量。单卡长prefill/固定长decode的容量与速度证据不签任意输出、batch或serving SLO，单项质量亦有反侧。校准、重训、模态映射/rank、重建与新旧能力回归均计费；norm分布、位置/模态或净预算失配时，保留原GQA显式KV/较宽latent和受验token选择路径，不让较小cache取得无损读取或Agent可靠性授权。
<!-- source-family:SF-2026-ARXIV-2606-12195 -->

压缩基还可以同时约束Query计算与缓存，而不只分别拟合K/V：联合分解Q/K/V的输入映射，共用一次downprojection，再从同一低维状态产生查询与重建缓存；旋转和量化继续定义这份产物的数值接口。[一条受限联合分解分支](https://arxiv.org/html/2510.16292v1)由此改变计算、写入和读取合同，不是对任意checkpoint的无损代数简化。经验梯度的低秩或单head推导的rank阈值，不证明整个网络最优，也不能直接搬到任意GQA、RoPE或多模态位置规则。Rank、共享basis、layer/position、重建及PTQ校准必须共同版本化，并分别验原质量和真实运行。分解、经验梯度估计与校准、旋转量化、每步投影/重建及回归均付费，避免offload不等完整请求净速；容量、数值或质量不合时，保原显式KV、独立投影或较宽latent，不由较小cache签无损与服务可靠性。
<!-- source-family:SF-2025-ARXIV-2510-16292 -->

重复同一层栈的 looped 模型还要区分参数共享与状态共享：各 loop 的 hidden state 不同，朴素缓存仍保存每轮 K/V。一个可重训的分支让旧 token 各轮状态共同写出低维 latent，第一轮另留较小 latent；当前 query 在 latent 空间读出加权表示，再映回输出，不为全历史重构逐轮 K/V。近期窗口仍保留 exact K/V，两部分共同归一化，窗口外的 token 并非直接丢弃。

这同时改变缓存容量与读取计算，却增加 writer/reader、uptraining、位置对齐和固定窗口成本。[HLA 的受限实验](https://arxiv.org/html/2610.07940v1)中，Ouro T=4、A100 80GB、16bit 的短上下文单序列反而更慢；扩大可容纳 batch 的吞吐收益不等于同 batch latency 或生产 SLO。低秩拟合也不是无损 attention，16K 之外尚未测。无法重训、布局不兼容或质量回归失败时，逐轮显式 KV 与已验收的共享布局仍成立。<!-- source-family:SF-2026-ARXIV-2610-07940 -->

Loop深度不扩cache还有一条不同于汇集历史loop的路径：每个layer维护一份latent memory，当前token在各loop以gate覆写，再投影为K/V；新token只有一行位置，但下一token必须消费前token完成最终loop后的状态。这把保存逐loop历史换成学习到的压缩更新，对loop常数不等对context常数，也不继承原模型函数。[MELT的受限迁移](https://arxiv.org/html/2605.07721v1)因而需要chunk-wise训练在并行与部署次序间折中，再用插值和teacher alignment适配；较低KV加weights估计不等完整VRAM或同质量SLO。所有loop、teacher与重训/回归都计费，部分质量仍低于原逐loop缓存，被比较的Ouro在作者所查默认配置下，early-exit只影响所选logit，并不省掉后续loop；MELT的adaptive depth仍未验；更新次序、训练或质量不成立时，保留逐loop显式KV、HLA式已验共享布局与普通decoder，不让固定memory名义批准任意adaptive depth。<!-- source-family:SF-2026-ARXIV-2605-07721 -->

### 跨模型的学习变换不是原样复用

KV 还可以被另一模型作为条件输入，但这不表示两个 checkpoint 的 cache 天然兼容。可先让两模型对同一输入各自 prefill，再用专门训练的投影、残差融合和分层门把源 KV 写入接收方的表示空间，后续生成继续读取这份融合前缀。[有限跨模型构造](https://arxiv.org/html/2510.03215v1)在冻结两模型后训练中间 fuser，改变的是接收方实际消费的条件函数，不是把源缓存当作接收方本来会算出的 exact state。

token 与层仍需显式对齐；最长字符串覆盖、模板 padding 或末层配对都不证明语义等价，形状相同、散点图靠近或有效秩增大也不是无损证书。接口应绑定两端 checkpoint/tokenizer、对齐策略与 fuser revision，并重新验目标质量；这是兼容性要求，不是论文已实现的完整生命周期协议。双路 prefill、学习/回归、融合、搬运与驻留均计费，省掉中间文字生成也不保证网络总费、并发或 SLO 更优。对齐、净质量或预算不满足时，保留原单模型 KV、文字交接或分别重算，不让学习到的 cache 取得事实、隐私或行动授权。<!-- source-family:SF-2025-ARXIV-2510-03215 -->

## Position 与 Cache 的一致性

采用 RoPE 的模型通常缓存已旋转的 K；采用其他位置机制时，应按其实际作用位置解释缓存，不是所有机制都把位置信息写入 K。Decode 新 token 必须使用正确 position index，否则新 Query 与历史 Keys 的相对几何错误。位置编码不会阻止同一请求继续复用 cache：历史 token 在后续 Decode steps 中仍处于原位置，所以它的 K 不需要重算。

跨请求的 Prefix reuse 则更严格：模型配置、token ids、position ids、adapter 和相关 Attention 语义都要兼容。文本看起来相同但 normalization、special tokens 或起始 position 不同，cache 都未必可复用；除非模型与 runtime 明确定义并验证了位置变换，不能把位于不同 offset 的 K 当作同一对象。Prefix Cache 是对这段已验证 KV state 的物理复用索引，不是另一种 Attention 语义，也不是“按文本相似度命中”的语义缓存。

流式输入与输出交替追加时，保持已生成 token 的 position 不变还需要显式分配位置，而不能每来一段输入就把旧输出向后挤。一个可重训的分支预留固定长度的输入 slots，输出从这些 slots 之后开始；slots 用满时，在当前序列末尾分配下一块，训练 Attention mask 同时对齐部署时的 read/write policy，避免旧输出读取当时尚未到达的输入。这样位置与可见性一起构成 cache reuse contract，而不是只改 position id 就让任意已有 hidden state 可复用。[受限流式翻译对照](https://arxiv.org/html/2603.14903v1)支持这种分支，slot 长度与训练/推理 policy 失配会损失质量；算法延迟与 FLOPs 不等端到端吞吐或 SLO。预留空间、专门微调和 mask 管理都付费；不能重训、输入模式不匹配或质量回归时，保留普通因果追加、必要重计算或已验收的 encoder–decoder 分工，不静默改变通用模型的 cache 语义。<!-- source-family:SF-2026-ARXIV-2603-14903 -->

## Cache 没有解决什么

第一，它不减少模型权重。Decode 每步仍要执行每层 projection、MLP、Norm，并读取大量 weights。

第二，它不消除自回归依赖。下一 token 仍要等待上一步 token 被选择。

第三，它不消除历史读取。每步 Query 仍要访问已有 K/V，长上下文会增加 memory bandwidth。

第四，它不保证容量可管理。不同请求长度、生命周期和并发会造成动态分配、碎片和调度问题。

KV Cache 把重复计算问题转化为显存与状态问题，而不是让推理免费。

## 从模型状态到 Runtime 对象

模型公式只要求 K/V 可访问，生产 runtime 还必须决定：

- Cache 放在哪张 GPU。
- 怎样分块、分配与释放。
- 请求能否进入 batch。
- Prefix 是否可以复用。
- 是否 offload、迁移或跨 Prefill/Decode worker 传输。
- 抢占和失败时怎样处理状态。

这些属于第45～47章及后续推理系统。本章不提前展开 PagedAttention 或 scheduler，只建立它们必须管理的对象来源。

## 本章在知识树中的位置

```text
Decoder-only autoregressive loop
-> historical K/V are invariant
-> per-layer KV Cache [B,H_kv,T,d_h]
-> Prefill writes / Decode appends
-> GPU memory manager and scheduler
```

本章解决了生成循环中哪些历史计算可以复用，但保存状态还不能决定下一步输出什么。第20章因此接手 logits 到 token 的选择，再将选出的 token 送回本章的追加过程。本章也连接 Part V：第45章从 runtime 生命周期重新审视 cache，第47章改变其物理 placement，第54～56章再把它纳入 HBM、PD 与调度约束。

从 State 横线看，本章定义 KV state 的模型来源；第 35 章转向训练状态的一致提交，第 42、45 章再把在线生成表示成 request-owned state machine。这里连接的是“状态语义怎样出现”，不是把 KV Cache 与 training checkpoint 视为同一种状态。

## 自检问题

1. Causal mask 为什么使历史 K/V 在未来生成中保持可复用？
2. 为什么缓存 K/V 而不缓存历史 Query？
3. 每层 K/V 的逻辑 shape 是什么？
4. `KV bytes` 公式中的各变量分别表示什么？
5. 小例子中 `T` 翻倍为什么 cache 也翻倍？
6. Prefill 与 Decode 怎样写入 cache？
7. 为什么 KV Cache 没有让完整生成变成线性或常数成本？
8. GQA/MQA 通过哪个变量降低 cache？
9. Position id 错误为什么会污染 cached K？
10. 第19、45、47、56章分别负责 KV Cache 的哪一层问题？
11. 为什么 `2 * H_kv * d_h` 是元素数量而不是信息熵？
12. RoPE 为什么不妨碍同一请求复用历史 K，却会约束跨请求 Prefix reuse？

## 小结

KV Cache 利用 causal model 的不变量：未来 token 不会改变历史位置已计算的 K/V。保存这些逐层状态后，Decode 只处理新 token，并让新 Query 读取历史 cache。

它显著减少重复计算，却让每个请求拥有随长度增长的显存状态。`L`、`T`、`H_kv`、`d_h`、dtype 和并发共同决定容量，这正是模型架构开始约束推理 runtime 的位置。

## Review notes

- `SF-2026-ARXIV-2610-33360` — Daily2026-10-28，精确v1 §2.2–2.3/3/4.3/6，2+2+2=6，donor生产历史差额深入；保teacher-forced非采样生成、局部一致性非全递归等价、full-cache质量成本、双遍训练与decode变慢反侧。唯一v1+官方Oct27日段+findable DOI registered Oct27 04:02:02Z限定本窗；未复现实验，实际独核见本日REVIEW。

- `SF-2025-ARXIV-2510-03215` — Meitner，Daily2025-10-07补Oct06；[C2C exact-v1](https://arxiv.org/html/2510.03215v1)§3–5/Table3–4/7及A.1.1–2/A.3.1–5/A.4.2–3必要，2+2+2=6，跨模型学习KV条件而非exact reuse差额深入。保heuristic对齐、oracle非免费、t-SNE/rank非语义证、gate局部反退、异构训练/输出长短混杂与完整费用，不采任意cache兼容、2x普胜、网络/隐私/未来VLA或specdecode实现。未核代码/像素/复现；PRE/SAVE/POST按本日canonical真实状态，不预签。

- `SF-2026-ARXIV-2606-12195` — Daily2026-06-12补Jun11，supp_jun12；[exact-v1](https://arxiv.org/html/2606.12195v1)，2+2+2=6。§3.2/恢复训练、5.2/5.4/7限定必要；只QK-Norm条件近似/模态latent迁移，保token流非函数无损、局部H200 B1 BF16固定长decode与全费；不授普遍质量/安全或SLO，未核代码/复现。唯一reader jun12_review_finish canonical§45实际必要/actual owner/原两段PRE通过并窄授，作者按原稿真实SAVE，jun12_review_finish唯一§51实际POST已通过，指定窄位已释放，仅同步既成状态，不预DAY。

- `SF-2026-ARXIV-2605-07721` — Daily2026-05-12补May11，MELT exact-v1必要§3/4/T1–4/5/C/F1–2，2+2+3=7。仅perlayer latent loop覆写/final-loop后token依赖和chunk训练分责；保非context常数/非dropin、weights+KV非完整VRAM、质量反侧、Ouro配置earlyexit producer与MELT adaptive未验，全部teacher/loop/重训费。未核代码/完整proof/复现；reader Source/actual owner/唯一修版PRE通过，root单段窄授后保存，actual非writer POST待执行。 截至本轮后续有效结论：本项独立reader已实际完整新增/直接两侧/本人注非writer POST通过，root已接纳并释放指定窄位；此前“待”仅过程时态，本次纯行政同步、不重Source/正文、不预授DAY。

- `SF-2026-ARXIV-2603-14903` — Daily `2026-03-18` 补03/17；[ExPosST exact-v1](https://arxiv.org/html/2603.14903v1) §2–4及AppA；2+2+2=6，流式位置预留与policy-consistent mask具体差额深入。保持输入/输出position与可见性合同、重训/slot/质量回退成本，LAAL/FLOPs不授端到端SLO。root必要Source/实际owner/逐字PRE通过并授Ch19窄锁；作者正文与完整局部邻接顺读，root实际225–247正文/完整邻接与本人注299非writer POST通过。未核实现/复现，不授日级验收。

- Stochastic KV Routing（training-time depth-wise KV sharing；Status: Experimental）:
  https://arxiv.org/abs/2604.22782

本轮联章 Review 补充了变长请求下按 `sum T_r` 计算的逻辑容量，避免把等长 batch 公式误当成所有 runtime 的实际占用。本章仍只负责 KV Cache 的模型推导、shape、容量与 Prefill/Decode 写入语义。分页、碎片、prefix caching、offload、调度和 PD 传输保留给 Part V。

Primary-source 校验入口：

- Noam Shazeer, "Fast Transformer Decoding: One Write-Head is All You Need", 2019: https://arxiv.org/abs/1911.02150
- Reiner Pope et al., "Efficiently Scaling Transformer Inference", 2022: https://arxiv.org/abs/2211.05102
- Joshua Ainslie et al., "GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints", 2023: https://arxiv.org/abs/2305.13245

- SF-2025-ARXIV-2510-16292 — Socrates，Daily2025-10-22补Oct21；Tesla R23 exact-v1必要/R52实际差额复用，共享Q/K/V downprojection对compute/cache/PTQ合同深入。保empirical rank与single-head阈值条件、GQA/RoPE资格、分解/校准/量化/重建全费与局部质量反侧；不采无损/全网最优/E2E保证，未核实现/复现，整体PRE/SAVE/完整自读/solePOST以同日实际层为准。
