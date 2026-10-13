# Tucker Attention — 三轴参数化与 KV/RoPE 接口窄 PRE

`SF-2026-ARXIV-2603-30033`；`2+2+2=6`。root 已实际核 v1 §2–4、Table3 质量反侧和普通复合日证，Source 通过。此文件仅申请实际 PRE/窄锁，未写 Books。

## 唯一 owner 与实际差额

`MODEL-MULTI-HEAD-ATTENTION` — `books/part-02-model/15-multi-head-attention.md`。当前178–224是 GQA/MQA 的 KV head 数与参数/cache 关系；239–266的 shared→multiplelatenthead 处理 TP 切分轴，269–279是已训练多路径。没有把 per-head QK/VO 乘积沿 head 轴堆成三阶张量、联合 rank 压缩的机制；Tucker 不是这两个已有 latent 分支的同名重复，也不是原 GQA head merge 的无损 runtime 替换。

已读 Books 必要上下文，当前 Ch15 head/KV/TP 局部，Ch14 单head→多head交接、Ch16 Attention→MLP交接及 Ch13 位置/RoPE接口。新机制的长期 owner 是多head参数族与state接口；Ch13仍拥有相对位置机制，Ch19/45拥有容量/生命周期，Ch49拥有runtime实现，不多处写同机制。只在现参数/cache桥后、TP标题前加两段。6分因具体owner缺口读深必要§2–4，不改分、无附录扩读。

## OLD 完整正文锚

```markdown
第19章会加入 layer 数 `L`、dtype bytes 和请求生命周期，完整推导 cache 容量。本章只建立模型架构到 `H_kv` 的接口。

## Multi-Head 与 Tensor Parallel
```

## NEW 完整替换（只插两段）

```markdown
第19章会加入 layer 数 `L`、dtype bytes 和请求生命周期，完整推导 cache 容量。本章只建立模型架构到 `H_kv` 的接口。

减少 KV heads 不是参数共享的唯一轴。每个 head 在 softmax 之前通过 `W_Q W_K^T` 决定匹配，在 softmax 之后通过 `W_V W_O` 影响读出；分别把这些乘积沿 head 轴堆成三阶张量，可以用核心张量与各轴基矩阵联合分解，而非只给每个 head 一张独立低 rank 矩阵。这条分支同时约束 head 与两端特征子空间，rank 决定表达自由度和压缩幅度；指定 rank 下能够表达 MHA/GQA/MLA 的参数形式，不证明任意既有 checkpoint 无需近似、训练即可替换。推理时保存的是两个 down-projection 的 latent，若共享 down projection 才可只存一份；同 rank 的 cache 可以与 MLA 相同，更多 attention 参数节省不再自动增加 KV 节省。<!-- source-family:SF-2026-ARXIV-2603-30033 -->

位置与 kernel 接口也须随这份分解一起验收。原来在每头 Q/K 中间施加 RoPE，不能直接当作因式分解后的无损操作；把旋转移到 latent key 维度可以保留相对位置形式，却改变频率和算子配置，不是原 RoPE checkpoint 的 drop-in 改写。[Tucker 的必要对照](https://arxiv.org/html/2603.30033v1)先形成每头 query 再接共享 latent KV 的 GQA kernel，专用 core kernel 仍属未来工作；从头训练的 1B 模型中，GQA8 的 loss 2.61 对比一个 Tucker 配置的 2.69，参数/iteration 成本降低仍有质量代价。所测单 H100、BF16、batch1、cached length4096 的研究 decode mean 不授生产吞吐或 tail SLO。rank 搜索、初始化/训练、latent 投影与布局转换都付费；质量、位置或 backend 未通过时，保留原 MHA/GQA/MLA，而不是按参数压缩比例推延迟倍数。

## Multi-Head 与 Tensor Parallel
```

## 本人静态末注完整尾锚

当前最后项原样保留：

```markdown
- `SF-2026-ARXIV-2603-08343` — Daily `2026-03-11`补遗漏；[exact-v1](https://arxiv.org/html/2603.08343v1) §4–6：固定 head-mixing basis 与可学习 affine 是改变架构自由度的替代分支，不是任意 checkpoint 的等价替换。保留小模型质量范围、随机初始化大配置与实际 kernel 成本边界；root 已读必要方法、评价与反侧，并核 Ch14/16 交接后写入正文。非写入者 supplement_20260311 已实际回对原证并顺读新增两段、完整局部邻接与末注，写后复核通过，不授日级完成；未运行代码或复现实验。
```

其后只追加：

```markdown
- `SF-2026-ARXIV-2603-30033` — Daily `2026-04-02`补`04-01`；[exact-v1](https://arxiv.org/html/2603.30033v1) §2 张量参数族、§3 KV/latentRoPE/kernel 接口、§4 Table3与相关质量/配置，`2+2+2=6`，具体三轴参数化缺口必要加深。只采 head 与特征轴共享及参数/cache分账；同rank MLA cache、latent旋转改变频率、research kernel和有限训练质量反退近文。不照抄 Eq9/13 记号为完整实现，不授任意checkpoint等价、参数比例延迟倍数或生产SLO；未核代码或复现。
```

申请只锁 Ch15 上述两段与本人注。正式 root PRE/窄锁之前不写；实际写后本人顺读完整邻接与注，再由 root 非writer POST。不自授日级。

真实单项写入/POST：root已actualPRE读202–245参数/cache→TP完整邻接并授权窄锁；作者apply_patch仅写229/231两段与注377，actual顺读210–246邻接/本人注，限定diff-check通过。root已实际nonwriter readback210–248两段完整邻接及本人末注，确认参数/cache分账、latentRoPE非dropin、质量反側/researchkernel条件近文，POST通过、锁释放。没有DAY。
