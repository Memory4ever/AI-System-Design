# SISA — 唯一 owner、窄 PRE 与实际写后复核

Family `SF-2026-ARXIV-2603-29913`；Daily `2026-04-02`只补`04-01`。root 已实际读精确v1§3–4并通过 `2+2+2=6` Source；这是具体新增gap的Books必要加深，不改分、不过读附录。本文只是PRE申请，不是写入/POST。

## Owner 与实际差额

唯一owner `INFER-TENSORRT-LLM` — `books/part-05-inference-system/49-tensorrt-llm.md`。ROADMAP拥有model semantics→execution plan/targethardware的桥；SISA不改变token、Attention或requeststate，因此不归Ch16模型FFN、Ch48验收分布或Ch50请求调度。不需要新结构。

已重读AGENTS要求的ROADMAP、PROJECT_CONTEXT、LEARNING_PHILOSOPHY、WRITING_GUIDE、当前2026 LS路由，以及Ch49相关正文与Ch48/50开头及handoff。Ch49当前367–417说明phase/backend选择与GEMMshape；592–627说明librarykernel、tile/wave和shape成本。455–457的FPGA分支在同一PE池切dot-product与output-stationary **dataflow**，不是SISA保持OS但将阵列按高度融合/独立N tiles的**并行单元重组**。当前无slab/fusion/localbuffer机制，故不是主题相似的已有覆盖。

插入现有「从Linear语义到GEMM执行」shape句后，承接相同M/N/K却不同cost，再交给下一节State→Kernel。只两段连续正文，无论文独立小节。当前已有及并发Book修改全部保留；未写文件。

## Body OLD 完整锚

```markdown
Attention 的 Q/K/V/O projections、MLP 的 up/gate/down projections，最终都会产生不同 `M/N/K`、dtype、layout 和 epilogue 的矩阵乘。数学式相同，不代表执行成本相同：大 `M` 的 Training/Prefill、很小 `M` 的 Decode、多个不同 `M_e` 的 MoE experts，会形成不同 kernel search spaces。

### Execution Plan 先拥有 State，再选择 Kernel
```

## Body NEW 完整替换（只在中间新增两段）

```markdown
Attention 的 Q/K/V/O projections、MLP 的 up/gate/down projections，最终都会产生不同 `M/N/K`、dtype、layout 和 epilogue 的矩阵乘。数学式相同，不代表执行成本相同：大 `M` 的 Training/Prefill、很小 `M` 的 Decode、多个不同 `M_e` 的 MoE experts，会形成不同 kernel search spaces。

Shape 不匹配也可以改变固定计算阵列的分工，而不只是在现有 GPU 上另选一个 kernel。方形 systolic array 对接近满阵列的大 GEMM 简单、数据复用规则；很小或偏斜的 `M` 却会使许多处理单元闲置。一个需要硬件支持的替代分支沿高度把同一 PE 池分成全宽的矩形 slabs，各自保留 activation/weight buffer，并用 output-stationary dataflow 在本地累加同一输出。当 `M` 很小时沿 `N` 分配独立 tiles、片上复用输入；`M` 增大时通过 weight-buffer bypass 沿高度融合 slabs，再以更少的独立组处理 tiles；沿 `K` 切分的部分结果仍按序累加，大矩阵则回到完整阵列，尾块再按形状重组。它重组的是同一 dataflow 下的并行单元，不是更改矩阵语义，也不同于下文按阶段切换 dataflow 的分支。

独立 buffers、mux、slab-level power gating 和供数带宽都有代价，更多并行组也会减少单组的数据复用；不能把它解释为软件让现成 Tensor Core 免费改变组织。[SISA 的受限原证](https://arxiv.org/html/2603.29913v1)以同 PE 数、128×128/BF16 阵列做 RTL、CACTI 与 SCALE-Sim 评价，不是实芯部署；接近满阵列的 `112<M≤128` 反而增加 EDP，另一种重配置阵列在 `M=33–50` 可更好，INT8 与 BF16 的实现不能按相同 PE 数直接视为同硬件。工艺/library 命名也不够一致，不据此采用绝对功耗。所测线性 GEMM 的加权收益不包含完整模型的其他算子、跨设备传输、请求调度与服务 SLO；带宽不足、控制/缓存成本抵消收益或大矩阵占主导时，完整阵列、固定 datapath 与已验证的 library kernel 仍是合理基线。<!-- source-family:SF-2026-ARXIV-2603-29913 -->

### Execution Plan 先拥有 State，再选择 Kernel
```

## 本人 Review note PRE 与完整尾锚

当前最后一项，保留不动：

```markdown
- [SCIN exact-v1](https://arxiv.org/html/2603.28239v1)：§2.2–3.5/4.1–4.5/6；五FPGA原型未实现INQ，BookSim2八加速器/四switch模拟用H200单GPUprofiler，不是八GPU线上实测。保memory ordering/completion、INT4质量反退和小message INQ增延，不授任意precision、生产SLO或wirebandwidth提升，未核RTL/复现。
```

其后只追加本人末注：

```markdown
- `SF-2026-ARXIV-2603-29913` — Daily `2026-04-02`补`04-01`；[SISA exact-v1](https://arxiv.org/html/2603.29913v1)必要§3–4，`2+2+2=6`，实际OS slab独立/融合与shape/bandwidth差额加深。只采用同PE池重组并行单元与本地buffer/累加责任；保接近满阵列EDP、ReDas更优区间、INT8/BF16不可混、工艺/library命名冲突和GEMM aggregation非Serving的反侧，不采绝对功耗/实芯或生产SLO。未核RTL/代码或复现实验。
```

## 写锁请求

请求仅上述Ch49两段body锚＋本人末注的窄锁；获得root具体许可后才apply_patch。写后本人顺读完整body前后邻接与末注，并把实际行/原文交root非writer POST；他人末注不改，不自POST，未获DAY/完成态回读不计日级。

实际审批与写入：root已独立回读现shape完整锚/邻接和SCIN尾锚，PRE通过并授权仅本作者独占上述两段＋本人注；按其要求删本人注最后的过程口径。已apply_patch实际写入Ch49两段（shape句之后、State标题之前）和静态注，未改任何别family或旧正文。本人已实际顺读404–430完整局部及最后7行本人注/前项；限定diff-check通过。

真实nonwriter POST：root实际readback Ch49 407–425完整shape→418/420两段→State及本人静态注2937，确认原段保留、仅OS slab相对SPECTRA分工与GEMM/Serving/工艺反侧、静态注合规，POST通过并明确释放窄锁。Source/PRE/实际整合与POST均已获真实单项接纳；不授本日DAY/完成态FINAL。
