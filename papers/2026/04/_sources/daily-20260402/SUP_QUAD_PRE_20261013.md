# QUAD — 固定 graph 的跨-adapter quant profile 窄 PRE

`SF-2026-ARXIV-2603-29535`，`2+2+2=6`；root实际v1§3/4/5 Tables1–5有限Source通过。仅申请PRE与窄锁，未写Books。

## 实际 owner 与差额

唯一 `INFER-TENSORRT-LLM` — `books/part-05-inference-system/49-tensorrt-llm.md`。当前67–71实际已解释同尺寸LoRA矩阵外露runtimeinput、graph的shape/precision/layout ABI和不兼容时重编译；**这部分已有覆盖，不再复写**。QUAD剩下的增量是静态NPU quantprofile跨独立adapter分布不自动通用，以及anchor-profile→QuantSim/teacher校准这个限定适配分支。Ch30 431–442的QLoRA区分base/adapter/compute dtype，但没有冻结部署profile的跨adapter资格机制；不跨写两owner。

已按AGENTS读Books上下文及当前LS路由；Ch49此局部与下一ROM/SRAM、KV分支及Ch48/50交接，Ch30量化接口/训练→runtime交接。只增加**一个机制/边界合并段**，位于原A/B-input段与原搬运/多输出KV成本段之间，无新标题、不改原段。Source6只评该接口/校准差额，不拿已有runtime-input原则重复加分。无需新结构。

## OLD 完整锚

```markdown
静态 NPU 把算子与 shape 提前编译，按任务分别构图并共享 base 权重是最直接的基线；将所有 adapter 常驻再用选择 mask 切换，则用容量换更少重编译。还有一个窄分支把同尺寸 LoRA 矩阵变成 runtime 输入：固定图保留低秩更新的算子与 placeholder shape，请求只提供对应的 adapter 值。编译计划因而拥有接口、精度与 layout，adapter artifact 拥有具体参数；换值不等于换 shape，也不能把 adapter 训练方式与执行 ABI 混为一谈。<!-- source-family:SF-2026-ARXIV-2604-18655 -->

输入化仍有搬运、显存与后端 operator coverage 的成本。多输出路径共同 prefill 后隔离 suffix 的 KV，是另一项状态条件，不授权任意 adapter 共用 prefix cache；第45章仍负责 base/adapter/KV 身份，第30章负责低秩训练。[受限手机 NPU 实现](https://arxiv.org/html/2604.18655v1)只支持披露的1B/3B模型、固定接口与设备分支，其不同精度配置、相对评分与吞吐算式不能拼成统一加速证明。尺寸、精度或状态不兼容时应重编译、拆成独立图，或回到已验证的通用执行路径；运行时输入并不消除质量和端到端验收。
```

## NEW 完整替换（只插一个段）

```markdown
静态 NPU 把算子与 shape 提前编译，按任务分别构图并共享 base 权重是最直接的基线；将所有 adapter 常驻再用选择 mask 切换，则用容量换更少重编译。还有一个窄分支把同尺寸 LoRA 矩阵变成 runtime 输入：固定图保留低秩更新的算子与 placeholder shape，请求只提供对应的 adapter 值。编译计划因而拥有接口、精度与 layout，adapter artifact 拥有具体参数；换值不等于换 shape，也不能把 adapter 训练方式与执行 ABI 混为一谈。<!-- source-family:SF-2026-ARXIV-2604-18655 -->

接口相同仍不保证量化资格相同：独立训练的 adapters 即使 rank 和 dtype 相同，参数/activation 分布也未必适配同一冻结的 quantization profile。一条有限适配分支先用完整与量化模型的输出差异选择较敏感 adapter 作为校准锚，再把其他 adapter 放入这份固定 profile 的 QuantSim，以各自完整精度 teacher 输出和原任务 loss 继续适配；只有质量回归通过的 adapter 才绑定到该 graph。因此部署产物应联合保存 base、graph、各模块编码/profile 与 adapter revision，不是任意新 adapter 可以免训练热换。[QUAD 的受限手机生成模型对照](https://arxiv.org/html/2603.29535v1)支持这条接口选择，但其 base INT8、LoRA/activation INT16 不是所有对象同一 scale 的可执行配方，原 affine 记号不一致也不据此补实现；全 W8A8 有明显质量崩落。校准、teacher/训练、加载与逐 adapter 输出回归都计费，shared ROM 节约不等 peak RAM 或任意硬件端到端收益；profile 或质量不兼容时仍拆图、重校准，或保留原 precision/adapter 路径。<!-- source-family:SF-2026-ARXIV-2603-29535 -->

输入化仍有搬运、显存与后端 operator coverage 的成本。多输出路径共同 prefill 后隔离 suffix 的 KV，是另一项状态条件，不授权任意 adapter 共用 prefix cache；第45章仍负责 base/adapter/KV 身份，第30章负责低秩训练。[受限手机 NPU 实现](https://arxiv.org/html/2604.18655v1)只支持披露的1B/3B模型、固定接口与设备分支，其不同精度配置、相对评分与吞吐算式不能拼成统一加速证明。尺寸、精度或状态不兼容时应重编译、拆成独立图，或回到已验证的通用执行路径；运行时输入并不消除质量和端到端验收。
```

## 本人静态末注完整锚

现尾SISA本人注保留：

```markdown
- `SF-2026-ARXIV-2603-29913` — Daily `2026-04-02`补`04-01`；[SISA exact-v1](https://arxiv.org/html/2603.29913v1)必要§3–4，`2+2+2=6`，实际OS slab独立/融合与shape/bandwidth差额加深。只采用同PE池重组并行单元与本地buffer/累加责任；保接近满阵列EDP、ReDas更优区间、INT8/BF16不可混、工艺/library命名冲突和GEMM aggregation非Serving的反侧，不采绝对功耗/实芯或生产SLO。未核RTL/代码或复现实验。
```

只其后追加：

```markdown
- `SF-2026-ARXIV-2603-29535` — Daily `2026-04-02`补`04-01`；[QUAD exact-v1](https://arxiv.org/html/2603.29535v1)必要§3–5/Tables1–5，`2+2+2=6`，固定graph的跨adapter profile资格差额必要加深。仅采anchor profile/QuantSim teacher适配与逐adapter质量/资产分账；原dtype/affine公式冲突不授完整实现、W8A8反退与ROM非RAM近文。FID是FP32-vs-quant输出，10adapter6×估算/1.5s不作普适收益，不授任意chipset、新adapter免费或生产SLO；未核实现/复现。
```

root已实际逐字PRE及现Ch49 58–77邻接核通过，授权只上述单段与本人注。作者实际写入新段第71行、本人注第2947行，回读第61–85行完整邻接及末尾7行，限定diff-check通过；root已实际nonwriter POST接纳并释放窄锁。不授DAY/FINAL、实现核验或复现。

