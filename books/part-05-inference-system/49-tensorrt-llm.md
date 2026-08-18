# 第49章 高性能 GPU 推理执行：以 TensorRT-LLM 为例

**Knowledge Tree:** Part V Inference System：为什么推理是 AI Infra 的核心战场
**Stable Knowledge Node ID:** `INFER-TENSORRT-LLM`
**Legacy Chapter:** Ch45
**Status:** Draft

**Roadmap Intent:** 把模型语义转换为面向目标硬件的 execution plan、kernel、quantization 与 runtime。

## 本章要回答的问题

为什么有了 PyTorch/Hugging Face 还需要 TensorRT-LLM 这类推理优化栈？它优化的是模型语义，还是 GPU 上的执行计划？图优化、kernel fusion、量化、FlashAttention 这些技术在系统里分别处在什么层次？

本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**

这里的 `stack` 很重要。当前官方文档覆盖的不只是离线构建计算图，也包括 runtime、in-flight batching、paged KV caching、quantization 以及多 GPU/多节点执行。把 TensorRT-LLM 固定理解成“先编译一个静态 engine”会低估它已经扩展出的 Serving 能力；但本章仍以 GPU execution optimization 为主线，避免写成版本功能目录。

## 从计算图开始

理解 TensorRT-LLM 可以先从计算图开始：模型不是一个黑盒函数，而是一张计算图。图里有算子、依赖、常量、临时 tensor 和 kernel launch。

朴素执行方式会产生很多额外开销：

- 多个小算子分别 launch kernel。
- 中间结果频繁写回 HBM 再读出。
- 常量表达式运行时重复计算。
- 独立算子没有被合理并行调度。

图优化的第一性原理是：数学结果不变的前提下，减少运行时不必要的计算、访存和调度开销。

## 三类基础优化

第一是 operator fusion。把连续的小算子合并成更大的 kernel，减少中间 tensor 的 HBM 往返，也减少 kernel launch overhead。

第二是 constant folding。在编译或构图阶段把只依赖常量的表达式提前算掉，避免每次请求重复执行。

第三是 scheduling optimization。根据依赖关系安排算子执行顺序，让可并行的工作更充分地利用 GPU。

这些不是 TensorRT-LLM 独有思想，而是高性能推理系统的通用原则。TensorRT-LLM 的意义在于把这些原则和 LLM 特有结构结合起来：attention、KV Cache、GEMM、collective communication、quantization、batching。

## 从 Linear 语义到 GEMM 执行

第16章已经把 MLP projection 写成 GEMM。这里将符号冻结为：

```text
C = alpha * op(A) op(B) + beta * C

op(A) [M,K]
op(B) [K,N]
C     [M,N]
```

Attention 的 Q/K/V/O projections、MLP 的 up/gate/down projections，最终都会产生不同 `M/N/K`、dtype、layout 和 epilogue 的矩阵乘。数学式相同，不代表执行成本相同：大 `M` 的 Training/Prefill、很小 `M` 的 Decode、多个不同 `M_e` 的 MoE experts，会形成不同 kernel search spaces。

最朴素的 GEMM 可以让每个 output element 独立遍历 `K`。问题是相邻 outputs 会反复从 HBM 读取相同的 A rows 和 B columns。现代 kernel 将输出切成 `B_M x B_N` tiles，并沿 `K` 以 `B_K` 分段：

```text
for each output tile C_tile[B_M,B_N]:
    accumulator = 0
    for k_tile in K / B_K:
        stage A_tile[B_M,B_K]
        stage B_tile[B_K,B_N]
        accumulator += A_tile @ B_tile
    store accumulator through epilogue
```

一次搬入片上的 A/B tile 会被多次 multiply-accumulate 复用。Tile 太小会降低复用并增加调度开销；tile 太大则消耗更多 shared memory、registers 和 accumulator state，可能降低 occupancy。因而“峰值 Tensor Core FLOPS 很高”只是上限，真实效率还取决于：

```text
useful tensor-core work
vs
HBM/shared-memory traffic
+ address/scale/epilogue instructions
+ synchronization and pipeline bubbles
+ launch and tail-tile waste
```

## cuBLAS 不是一个固定 GEMM Kernel

cuBLAS 提供 BLAS 语义和 NVIDIA GPU 上的实现集合；`cublasGemmEx` 等接口把 dtype、transpose、leading dimensions 和 compute type 交给 library。cuBLASLt 进一步把 GEMM 表达成可规划的 operation：

```text
matmul descriptor
+ A/B/C/D layout descriptors
+ compute / scale type
+ epilogue
+ workspace preference
-> heuristic algorithm candidates
-> selected algorithm reused for matching operations
```

这意味着“调用 cuBLAS”不是选择了唯一算法。Library 会根据 GPU、shape、layout、precision、workspace 和 epilogue 从内部 kernel 空间寻找可用实现。cuBLASLt 可以把 bias、ReLU/GELU 等 post-processing 放入 epilogue，减少额外 launch 和中间 HBM traffic；更大 workspace 也可能开放不同的 split-K 或 reduction 路径。

它的优势是覆盖面、兼容性、数值行为与厂商持续优化。边界则是通用 heuristic 不一定表达某个模型独有的 scale layout、ragged experts、通信融合或固定 shape workload；支持的组合也受版本和 compute capability 约束。稳定 workload 可以缓存 heuristic 选择并做离线 benchmark，但结果仍必须绑定完整 operation descriptor，不能只按 `M/N/K` 命名。

## Tensor Core 指令名必须分层

从 library call 到硬件执行，中间至少经过：

```text
model operator / GEMM contract
-> library, compiler or kernel template
-> CUDA C++ / PTX
-> ptxas scheduling and register allocation
-> architecture-specific SASS
-> Tensor Core, scalar/vector and memory pipelines
```

常见名称属于不同层，不能互换：

| 名称 | 所在层次 | 含义边界 |
| --- | --- | --- |
| `mma.sync` | PTX | warp-level matrix multiply-accumulate family |
| `wgmma.mma_async` | Hopper PTX | warpgroup-level asynchronous matrix multiply-accumulate |
| `tcgen05.mma` | Blackwell PTX | fifth-generation Tensor Core MMA family |
| `HMMA` / `GMMA` 等 | profiler / SASS 语境 | architecture 和 toolchain 相关的机器指令命名，不应当作跨代 API |
| `FFMA` | scalar floating-point pipeline | fused `a*b+c`，不是 Tensor Core matrix MMA |

因此不应把 `FMMA` 当成这里稳定的官方指令族。DeepGEMM 官方材料所说的是 **FFMA instruction interleaving**：把与 Tensor Core 主计算相对独立的 scalar floating-point instructions 安排到可利用的流水间隙，减少 exposed latency。它优化的是 instruction schedule，不改变 GEMM 的矩阵语义，也不意味着用 FFMA 替代 WGMMA。

这种交错必须尊重 data dependency、scoreboard、register pressure 和目标架构的 issue rules。手工重排 SASS 即使在一个 compiler/GPU 组合上有效，也可能在下一版 ptxas 或下一代架构失效。DeepGEMM 的演进正说明了这一点：早期版本包含 post-compilation SASS optimization；当前官方 README 记录，2025 年 SM90/SM100 重构后移除了该路径，并依赖 NVCC 12.9 自动完成 FFMA interleaving。长期知识是“用独立指令填补流水空洞”，不是永久依赖某个二进制改写脚本。

## TMA 解决搬运，不负责矩阵计算

Tensor Memory Accelerator（TMA）在 Hopper（compute capability 9.0）引入，用于把 1D 到多维 tensor tiles 在 global memory 与 shared memory 之间做 bulk asynchronous transfer。Tensor map 描述 base address、shape、stride、element type、interleave/swizzle 等信息；少量 threads 可以发起大块搬运，不必让每个元素先经过普通 registers 和逐元素地址计算。

TMA 本身不执行 GEMM。它的作用是让 memory pipeline 与 math pipeline 重叠：

```text
stage s+1: TMA loads next A/B tiles into shared memory
stage s:   WGMMA consumes ready tiles and updates accumulators
stage s-1: previous result enters epilogue / store path
```

双缓冲或多级缓冲让 producer 在 consumer 计算当前 tile 时准备下一 tile。`mbarrier` / pipeline phase 负责发布“tile 已到达”与“buffer 可复用”的顺序；跨 generic proxy 与 async proxy 时还需要正确的 fence。少一个 wait 可能读到未完成数据，多一个全 block barrier 又会消灭 overlap。

更深的 stages 不是免费加速：

- 增加 stage 可以覆盖更长 HBM latency。
- 每个 stage 都占用 shared memory，可能降低 resident blocks 和 occupancy。
- TMA alignment、tensor-map lifetime、swizzle 与 shared-memory bank layout 都进入正确性和性能边界。
- 小 tile、非规则访问或很短的 `K` 可能不足以摊薄 descriptor、barrier 和 pipeline 管理成本。

所以 TMA 的正确心智模型不是“异步 memcpy 更快”，而是**把 tile movement 变成可与 Tensor Core work 并行推进、且必须显式同步的独立硬件流水**。

## DeepGEMM 是专用分支，不是 cuBLAS 的线性替代

截至 2026-08，DeepGEMM 官方主线是面向 SM90/SM100 的开源 JIT Tensor Core kernel library，覆盖 FP8、FP4、BF16 GEMM，以及 grouped/MoE 和其他模型专用 primitives。它借鉴 CUTLASS/CuTe 的思想，但通过较小的 kernel/config surface，把目标 shape、dtype、scale layout、tile、pipeline stages、TMA threads 与 math threads 编入运行时生成的代码。

可以把两条路线理解为：

| 路线 | 优先目标 | 主要收益 | 新成本 |
| --- | --- | --- | --- |
| cuBLAS / cuBLASLt | 广泛 GEMM 组合与稳定 library contract | 厂商维护、覆盖广、heuristic 与 epilogue | 模型专用 layout/fusion 的表达空间有限 |
| DeepGEMM specialized path | 固定模型族、低精度 scale 与不规则 grouped workload | 可联合设计 tile、TMA、MMA、scale、scheduler 与 fusion | JIT cold start、支持矩阵、编译器耦合、验证与维护成本 |

二者是 coexistence，不是“新库淘汰旧库”。当前 DeepGEMM source tree 本身仍包含 cuBLASLt invocation path：构造 layouts 和 operation descriptor，查询 heuristic，再带 workspace 调用 `cublasLtMatmul`。这说明高性能系统可以对适合通用 library 的 shapes 复用 cuBLASLt，对明确受益的路径使用专用 kernels。

DeepGEMM 对 Dense 与 MoE 的意义也不同：

```text
Dense GEMM:
  one regular [M,K] x [K,N]

MoE grouped GEMM:
  expert e owns [M_e,K] x [K,N]
  M_e varies with routing
```

Grouped execution 可以减少逐 expert launches 和 padding，却没有消除 router imbalance、空 experts、tail tiles 与 All-to-All。若进一步把 dispatch、GEMM、activation、combine 或通信重叠成更大的 kernel，收益来自减少中间 state movement；代价是 correctness、debugging、artifact compatibility 与 failure isolation 全部扩大。

### MoE Dispatch 应平衡时间，而不是固定代理量

对 grouped expert execution，`tokens per GPU` 是便宜的负载代理，但不是稳定的时间模型。小 expert batch 的
Decode 可能由“在本 GPU 激活一个新 expert 并读取其 weights”的固定成本主导；tokens 增长后，GEMM tile 与
compute 开始主导；跨节点时 All-to-All 又可能先成为瓶颈。同一批次的 makespan 因而更接近：

```text
T_gpu ≈ max(
  expert activation / weight-read floor,
  token and tile compute,
  dispatch / combine communication
)
T_layer ≈ max_gpu(T_gpu)
```

这解释了为何每个固定代理都有自己的成立区间。按 token 均分在 compute-bound 区间合理，却可能把冷 experts
切到更多 GPUs，重复支付 weight-load 与 tile-padding 成本；按 activated-expert count 均分适合 memory-bound
小 batch，却可能把大量 token 留在单一 bottleneck；忽略 topology 的平衡表在多节点上还可能用跨节点 traffic
换取表面上的 GPU 均衡。

更稳健的执行链是先按 `(kernel, dtype, hardware, expert shape)` 校准 cost surface，再用当前 routing window
求近似 makespan，最后在相近方案之间保留稳定旧表，避免模型误差触发频繁切换。在线 control 不应进入 captured
critical path：graph 内只消费 versioned dispatch table 并收集计数，solver 在异步 plane 产生下一版；发布时还要
处理 stale counts、torn table 与 fallback。

这不是让 dispatch 取代 placement。轻度 drift 且 hot experts 已有 replicas 时，移动 tokens 可以修补短期 tail；
drift 大到目标 replica 根本不存在时，必须移动或复制 weights。新方案同时引入 calibration drift、solver/model
error、table freshness、remap tax 与 topology-specific maintenance。Static dispatch 在 placement 新鲜、小 experts、
通信已支配 step 或收益小于控制成本时仍然正确；time-aware dispatch 是有明确 win region 的条件分支。

#### Placement 从事后响应推进到预算内预测

Offline placement 用历史 routing profile 固定 expert-device mapping，适合 task mixture 稳定、weight movement
昂贵或控制面应尽量简单的场景。在线但 reactive 的迁移等到当前 router 产生准确 token assignments 后才决定
移动 weights，语义可靠，却把传输放到同一层 expert execution 的关键路径。若 workload 在 task 间快速切换，
这两种方案分别会遇到 stale map 与 exposed migration tail。

预测式 pre-routing 提供一条中间分支：在目标层 Attention 前，用上一层 residual hidden state 对目标层的 frozen
router 做一次 early invocation，只汇总 predicted expert counts；normal router 仍在原位置产生 authoritative
token-to-expert assignments。早期结果只改变 physical placement，不改变模型输出：

```text
previous-layer residual state
→ predicted aggregate expert demand
→ deterministic, budgeted pair-swap plan
→ overlap expert-weight movement with target attention
→ authoritative router dispatches exact tokens to the new placement
```

迁移预算必须由可覆盖窗口而不是“均衡程度”决定：每条 link / rank 可移动的 bytes 应小于 Attention window
扣除 safety margin 后能隐藏的传输量。Deterministic plan 让 ranks 从相同 compact counts 重建一致 swap order，
减少 plan broadcast；但 prediction error、attention-window variance、跨 batch thrashing、weight version、partial
transfer 与 rollback 都成为新状态。错误预测不能改变 routing 语义，却可能让 placement 更差或暴露额外延迟。

因此演进关系是：

```text
stable workload: offline placement
→ changing workload: reactive migration after exact routing
→ predictable short-horizon drift: pre-routing migration under overlap budget
```

FreeBalance 的作者实验只覆盖两类 MoE、8×A800 NVLink、EP=8、batch 16、8K prefill 和三次测量平均；没有
覆盖 Decode、跨节点 fabric、continuous batching、迁移故障或 tail SLO。它支持“预测只拥有 placement 建议、
normal router 继续拥有语义”的机制边界，不支持把预测式迁移写成通用默认方案。

### 如何比较 cuBLAS 与 DeepGEMM

不能只摘取一个峰值 TFLOPS。至少固定：

```text
GPU / compute capability / clocks
CUDA, driver, library and compiler versions
M/N/K or per-expert M_e distribution
dtype, accumulation and scale semantics
layout, alignment, transpose and epilogue
workspace and number of SMs
warm/cold JIT and graph-capture state
numerical tolerance
```

然后分别观察 kernel time、端到端 layer time、HBM/shared-memory traffic、Tensor Core activity、stall reasons、register/shared-memory footprint 与 tail behavior。只有在模型真实 shape 和上层 runtime 中仍获益，专用 kernel 才转化为 inference goodput。

## FlashAttention 在这里的位置

FlashAttention 不只是“更快的 attention”。它的核心思想是 IO-aware：通过 tiling 把 Q/K/V 的块搬到更快的 SRAM 中计算，减少 HBM 读写。

这正好对应 GPU memory hierarchy：HBM 容量大、带宽高，但相比 SRAM 仍然慢；如果 attention 把巨大的 score matrix 写回 HBM，就会被 memory IO 限制。

FlashAttention-2 进一步优化并行划分和 work partitioning；FlashAttention-3 则面向 Hopper 等新硬件利用异步数据搬运、WGMMA/TMA 和低精度能力。它们说明：kernel 优化不是只改数学公式，而是在适配硬件的 memory hierarchy 和执行单元。

## 量化为什么不自动带来加速

FP8、FP4、INT8、INT4 这类低精度路径的系统目标，是降低权重、activation 或 cache 的存储和带宽压力，并提高硬件 tensor core 的有效吞吐。

最朴素的方案是只压缩 weights，在执行前再反量化到高精度。它可以减少 artifact 和 resident weight bytes，却不保证 latency 下降：dequantize、额外 kernel launch 和中间 tensor traffic 可能抵消读取节省。Weight-and-activation quantization 更有机会使用低精度 tensor core，但对 outliers、calibration 和 kernel support 的要求更高。

更完整的单步成本应理解为：

```text
T_step
≈ T_low_precision_compute
 + T_quant_dequant
 + T_kernel_launch
 + T_unfused_memory
 + T_non_quantized
```

这里 `T_step` 是一次目标执行路径的端到端时间，其余各项分别表示低精度计算、
量化/反量化、kernel launch、未融合访存和未量化算子的时间贡献。它不是要求各项
严格互斥的 profiler 恒等式，而是避免只看低精度 GEMM 的成本清单。

所以“checkpoint 缩小”“HBM 占用下降”和“端到端推理加速”是三个需要分别验证的结论。

### Distribution-conditioned Quantization：共享权重不等于共享 Scale

常规 channel-wise smoothing 隐含一个条件：同一 layer 的 activation ranges 可以由一组稳定 statistics
代表。它把 diagonal scale `S` 在 activation 与 weight 之间搬移：

```text
XW = (X S^-1) (S W)
```

在单模态或各 token families 的 channel distribution 相近时，一组 scale 让 artifact、kernel 与 calibration
都最简单，依然是优先基线。多模态 decoder 则可能让 text、vision、audio tokens 共享同一 projection
weights，却具有明显不同的 activation ranges。若混合 calibration 中的 dominant family 决定统一 scale，
minority family 的有效信号可能被过度压缩；约束已经从“一个 layer、一种分布”变为“一个 shared weight、
多种条件分布”。

最直接的修复是为每个 condition 保存独立 scales 与完整 quantized weights，但这会复制最大的 model state，
抵消量化的 memory 目标。另一条分支是把执行路径拆为：

```text
shared low-precision base weight
+ per-condition scales
+ compact conditional residual / correction
+ token-family mask and routing
-> base GEMM for every token
-> correction only for selected token families
```

Conditional residual 可以在 calibration metric 下做 whitening，再用 low-rank approximation 压缩；这只能
证明“给定 calibration activations 与 rank constraint 时，某个受限 reconstruction objective 有最优近似”，
不能推出跨模态差异天然低秩。Rank、whitening stability、base family 与 calibration construction 都属于
artifact identity。选择经常出现在 autoregressive output 中的 family 作为 base，可以把 correction 成本
主要移到 Prefill；但若系统生成其他 modality、交错输出或改变 base，这个阶段性成本结论也会改变。

Runtime 现在拥有一个新的 correctness-critical control path。Token-family mask 错误、未知/融合 token、
code-switching 或 distribution drift 都可能让 token 走错 scale/correction，表现为静默质量退化而不是加载失败。
可部署 artifact 至少要绑定：

```text
model / module revision
+ calibration dataset and token-family labels
+ per-family scale and whitening revision
+ base-family choice
+ correction rank / weights
+ mask semantics and graph rewrite
+ kernel/backend support and fallback
+ modality-sliced quality + TTFT/TPOT/tail contract
```

技术路线因此不是用 conditional quantization 覆盖统一 scale。统一 smoothing 在分布接近、实现简单或专用
kernel 不成熟时仍成立；更高 bit width/mixed precision 用更多 bytes 换取更少 control state；完整 per-family
weights 在模型较小或隔离优先时可能更可靠；shared base + conditional correction 则用 mask、metadata、额外
compute 和更复杂验证，换取只保存一份大权重。最终必须测完整 execution path，不能把权重压缩率、单个
kernel 或固定 Prefill benchmark 当成 production goodput。

### 通用 Module Replacement 与专用 Structural Fusion

量化 runtime 有两种典型接入路径。

第一种尽量保留原模型 graph，只把目标 linear modules 替换为 quantized implementations。它容易接入新架构，也更容易与 scheduler、LoRA、offload 或 graph compiler 组合。

第二种针对模型结构改写 graph，例如合并 Q/K/V projections，把 normalization、RoPE 和 projection 交给一个 fused operator。它减少 launch 和 HBM round trips，却要求 artifact 明确参数 concat/split、operator semantics 和 kernel capability；新架构不能只靠扫描 module names 自动获得这些变换。

两者的基本权衡是：

```text
generic module replacement
  lower integration cost + stronger composability
  but more launches / unfused traffic

architecture-specific fusion
  lower execution overhead
  but higher build, validation and support-matrix cost
```

SVDQuant / Nunchaku 是这条边界的一个外部案例，而不是 TensorRT-LLM feature comparison。SVDQuant 把难量化的 outliers 放入高精度 low-rank branch，让 4-bit branch 处理 residual；Nunchaku 再把修正分支与低精度 path 融合，避免额外 activation movement。Nunchaku Lite 选择通用 module replacement 以进入 Diffusers，而原始 Nunchaku 的模型专用 fused paths 能获得更深优化。

这个案例说明 TensorRT-LLM 章节中的长期问题：执行计划必须共同决定 precision、graph rewrite、kernel 和 hardware mapping。硬件提供 FP4/FP8 能力，不等于业务模型自动可用；软件栈必须把模型转换、执行和质量验证串起来。

### 从 Routed Activation Materialization 到 Indexed Execution

MoE 的逻辑语义是 token 选择 expert，但最直接的执行会把 routed activations 按 expert 排列成新的
buffer，再执行 expert GEMM，最后根据 inverse mapping 合并。Padding 或固定 capacity 让 shape 稳定，
实现简单；dropless path 保留全部 assignment，却常把 compact、sort、materialize 和中间激活流量带入
critical path。模型越稀疏，并不意味着这些数据搬运也会自动变少。

一种 execution-plan 演进是只物化 compact routing metadata：保存 expert-token index、offset、inverse
mapping 与 position map，让 expert kernel 从原始 tensor on-the-fly gather，并在第二个 MLP 后直接
reduce；backward 复用 reverse mapping，对可重算的 SwiGLU intermediate 使用 fused recomputation。

```text
fixed-capacity / padded expert buffers
-> dropless compact-and-materialize
-> materialization-free indexed gather + direct reduce
-> fused backward with selective recomputation
```

这里的 `materialization-free` 不是“无状态”或“零搬运”。大 activation buffer 被 compact indices
取代，而 index construction、dense token-expert map、prefix sum、tile scan 与随机 gather 成为新成本。
在 token 数、Top-K 或 expert 数增加时，metadata 也会扩张；多节点时还必须与 All-to-All、load balance、
failure recovery 和 topology 联合设计。单卡单 MoE layer 的 kernel/activation 结果不能证明完整训练更快，
更不能证明收敛等价。

所以固定 capacity/padding 在负载可预测、模型较小或 portability 优先时仍合理；indexed execution 只在
省下的 activation traffic 大于 metadata、gather 与 recomputation 成本时成立。第21章拥有 router 语义，
第36章拥有训练并行与通信，本章只拥有从 routing result 到 executable data movement/kernel plan 的映射。

同一原则不限于 MoE：当算法语义只需要最终 reduction 或 winner，执行计划应先问能否避免构造完整 pairwise 中间量。
例如距离比较可以逐 tile 在线维护当前最优值与 index，后续 scatter/reduction 也可以通过 inverse index、排序和 segmented
reduction 改写为更规则的 gather/reduce：

```text
materialize full pairwise tensor
-> tiled online reduction with compact winner state
-> inverse-index gather / segmented reduce
```

这类改写获得较低 HBM traffic，却把代价转成 index build、排序、数值 tie-breaking、irregular gather 和 shape-specific tuning。
Flash-KMeans 的受限 kernel 实验说明该 transformation 在其 GPU、dtype、shape 与 clustering contract 下有效，不证明任意
reduction 或端到端训练都更快。完整中间 tensor 在规模小、需要复用全部 pairwise values、调试/portability 优先时仍合理；
online reduction 只有在被消除的读写大于 metadata 与不规则访问成本，并通过端到端数值和收敛验证时才应进入 engine plan。

### Learned Kernel 只是 Candidate Producer，Compiler 与 Verifier 仍拥有 Admission

手写 kernel 与 compiler template 在稳定 operator family 中可维护、可诊断；learned generator 能扩大
candidate coverage，却不能直接拥有 deployment authority。一条更可靠的演进链是先用约束生成可控
operator DAG，以 compile/correctness verifier 筛选 teacher pairs，再用 verifier-backed SFT/RL 产生候选；
对长 graph 则拆成 bounded fragments，逐个生成、验证和 benchmark，最后只把通过的 fragment 替换回
reference program：

```text
reference graph semantics
→ constrained synthetic curriculum
→ learned kernel proposal
→ compile + numerical checks
→ workload-bound benchmark
→ fragment-level hybrid artifact
→ registry admission and rollback
```

Generator、constraint solver、compiler、numerical verifier、benchmark harness 与 selector 必须分责。少量
随机 I/O、`torch.export` 成功或单机 speed reward 都不能覆盖 alias/mutation、极端 shape、数值 tolerance、
measurement noise 与 compiler drift。Fragment search 还会带来大量 compile work、artifact explosion 和
hardware coupling。旧 compiler/template 在 coverage、determinism、cold start 与维护成本优先时继续成立。

#### 从单候选到 Population：搜索档案也必须是可审计状态

单次生成—编译—benchmark 容易在局部最优、重复候选或偶然计时噪声上收敛。Population-based search 可把
高性能候选与结构多样候选同时保存在 archive，再通过 mutation/crossover/LLM edit 继续探索；但 archive
不是“最优 kernel 列表”，而是带 lineage 的实验数据库：

```text
semantic spec + reference implementation
→ candidate + parent lineage
→ compile and numerical verification
→ warmup / repeated benchmark under pinned contract
→ archive update by performance and diversity
→ selected artifact + fallback
```

Search controller 拥有 population、budget、feature descriptor 与 selection policy；compiler、correctness verifier
和 benchmark harness 分别拥有 admission，不应由生成模型自报成功。它新增 evaluator overfitting、benchmark
noise、compile cache contamination、driver/hardware drift 与巨额 search cost。规则库、vendor kernel 和小规模
human tuning 在稳定 shape、低搜索预算或高 assurance 场景仍更合理。

Kernel-Smith 的受限证据补充了 population/archive 与多阶段 evaluator，但 isolated-kernel speedup 不能外推为
serving throughput；只有 artifact 进入真实 graph、memory plan、batching 与 SLO contract 后，才构成系统收益。

硬件 portability 也不能只增加一个 fallback kernel。Architecture-exclusive symbol 可能在 build/link 阶段
失败，package installed 不等于 device capability，indexer、attention backend、paged-KV metadata 与 graph
capture 还可能分别不兼容。因而 portable backend 的最小 contract 是：

```text
build guard
→ runtime capability dispatch
→ indexer/logits kernel
→ attention and numerical merge
→ metadata / graph compatibility
→ long-sequence correctness tests
```

专用 backend 在支持硬件上可能更快、更成熟；portable Triton path 以更大 test matrix、JIT、数值 merge 与
address-width failure surface 换旧硬件可执行性。未合并 PR 只能作为 Experimental mechanism evidence，不能
写成当前框架保证；无法承担验证成本时，明确拒绝加载优于静默 fallback。

## Build-time 与 Runtime-time

更稳定的理解是把系统拆成两个阶段：

```text
model/checkpoint + config
-> conversion / build / optimization
-> engine or runtime-loadable artifact
-> executor
-> in-flight requests and KV state
```

Build-time 选择模型结构、precision、plugins、parallel mapping 和硬件适配；runtime-time 管理 requests、batch、KV Cache、sampling、streaming 与 collectives。具体版本可能把更多工作移到运行时，但“静态资产 identity”与“动态 request state”的区别不会消失。

当 collective 被编进 execution plan 后，它不再只是外部 launcher 的背景条件。每个 rank 仍拥有 local engine、
execution context、stream 与 buffers，但 collective progress 由整个 communicator group 共同拥有：所有参与 rank
必须以相同 order 进入对应 enqueue，communicator lifetime 必须覆盖 context lifetime，少一个 rank 就可能让其余
rank 无限等待。

```text
network graph + rank/group/root collective spec
→ per-rank engine build and compatible artifact set
→ communicator creation and lifetime binding
→ all-rank ordered enqueue / progress
→ group result or coordinated abort/rebuild
```

Graph-native collective 让 build-time optimizer 看见 communication，并支持 context-parallel Attention 等映射；
代价是 rank-synchronous failure、support matrix、NCCL/runtime version、cold initialization、engine duplication 与
hang diagnosis。TensorRT 11 的 official multi-device support 为这一 contract 提供版本化证据，不证明自动
partition、elastic membership 或 partial-rank recovery。单卡 engine 与外部 orchestration 在模型放得下、异构
设备、故障隔离或 unsupported precision/build 优先时仍合理。

Constrained decoding 还提供一个从动态 pointer structure 到 accelerator-friendly state machine 的例子。逐请求
trie traversal 控制清楚、增量更新自然，却包含分支与 pointer chasing；把 trie/vector constraint 编译成 dense
transition tables，可以让同批 requests 用向量化 gather/update 推进：

```text
constraint artifact / trie
→ compile immutable transition representation
→ pin representation version to request
→ vectorized state update per Decode step
→ rollback or finish under the same generation
```

这种执行映射用内存和 compile/rebuild 成本换 regular access；动态约束、高 sparsity 或频繁 schema 更新时，原始
trie/FSM 仍更合适。STATIC 的实验支持受限 constrained-decoding workload 中的 vectorization，不证明其表示适合
任意 grammar，也未自动解决增量 publication、request pinning 和 failure rollback。

这里的 parallel mapping 是 inference build/runtime 的选择，不是训练 layout 的
原样继承。一个以 ZeRO、training TP/PP/EP 保存的 checkpoint，可以在
consolidation/resharding 后构建成另一种 Serving topology。转换器必须从
global tensor identity 出发，而不是依赖源 rank 文件名；目标 artifact 还要
重新验证 logits、量化质量和多 rank collective correctness。

可部署 artifact 至少应绑定 model revision、tokenizer、quantization semantics、module mapping、structural rewrites、build/runtime version、kernel requirements、GPU compute capability、parallel degree 与支持的 shape/context limits。否则一次升级后即使 engine 能加载，也无法说明数值、graph semantics 和性能仍与原验证相同。

### Semantic Portability 不等于 Kernel Portability

Serving runtime 可以跨硬件复用 request lifecycle、token budget、prefix index 和 batching policy，
但不能假设 CUDA/NCCL/Triton kernel、graph capture 与 memory path 原样迁移到 JAX/TPU。更稳定的
分层是：

```text
shared serving semantics
→ backend compiler / executable and shape policy
→ hardware-specific kernels / collectives / memory path
```

SGLang-JAX 是这个边界的版本化案例：上层复用 scheduler/RadixCache contract，下层改用
JAX/XLA、`shard_map` 与 Pallas，并为离散 batch shapes 预编译 executable。它获得跨硬件的产品
语义复用，却新增 graph-cache miss、shape explosion、backend parity drift 和双栈 profiling 成本。
CUDA-only、kernel maturity 或 feature parity 优先时，专用 GPU path 仍更合理；portability 来自
明确隔离变化层，而不是消除硬件差异。厂商 Blog 中的 TPU 数字不能与 GPU 路径做无条件比较。

算法结构也会决定 compiler 能否真正接管热路径。若 state update 具有固定大小、静态 control flow，并能
表达成 batched contraction、scan 或 einsum，runtime 可以把 recurrent state 注册为设备端 tree，并让 `jit`/
loop primitive 在 device 上连续携带；host 不必逐 token 发起 round trip。此时 `O(1)` state 来自算法类别，
compiler 的贡献是把这个边界落实为 fused executable：

```text
chunkable recurrence + static state shape
-> standard tensor/loop primitives
-> backend legality, tiling and fusion
-> device-resident recurrent state
```

这条 compiler-first 分支换取 backend portability 与较低的 handwritten-kernel maintenance，却依赖 compiler
maturity、static shape 和 primitive expression power。Data-dependent gather/scatter、warp-level synchronization、
early exit 或极端专用 layout 仍可能需要 custom kernel；固定 chunk、batch=1 或单 accelerator 的结果也不能
外推 continuous batching。因而正确关系是 `Layering / Dependency`：算法先暴露合法的编译面，compiler 与
custom kernel 再按 workload 分工，而不是前者普遍取代后者。

## 专用加速器首先是一份 Workload Contract

把 kernel、compiler 或 accelerator 设计成“更专用”，本质上是在押注未来 workload：
哪些算子占主导、权重和 activation 使用什么精度、状态驻留在哪里、scale-up domain
多大，以及软件栈能否稳定生成对应 execution plan。若模型结构变化快于硬件交付周期，
理论峰值可能无法转化为 production goodput。

MTIA 的连续代际是一个版本化案例：Meta 描述了 workload 从
ranking / recommendation 扩展到 Generative AI 后，HBM bandwidth、低精度格式、
attention / FFN acceleration、chiplet 复用、scale-up communication 与
PyTorch / vLLM / Triton 软件支持如何共同变化。长期有效的结论不是某一代芯片规格，
而是以下闭环：

```text
production workload profile
-> operator / memory / communication contract
-> modular hardware and kernel design
-> framework lowering and runtime integration
-> observability under real traffic
-> next workload revision
```

这是 `Layering / Dependency`，不是专用 ASIC 对通用 GPU 的必然替代。通用 GPU 在
模型快速变化、算子多样和生态成熟度优先时仍有优势；专用加速器用更高的设计与部署锁定
成本，换取目标 workload 上的效率机会。

## In-flight Batching 的位置

TensorRT-LLM 当前官方栈同时包含 in-flight batching 和 paged KV caching。这并不意味着第46、47章被框架章节取代：

- Continuous Batching 定义 iteration-level work 如何变化。
- PagedAttention 定义 KV logical/physical mapping。
- TensorRT-LLM runtime 负责在 NVIDIA execution stack 中实现并组合这些机制。

同一个优化栈既可能改善 kernel time，也可能改变 batch construction。Benchmark 必须分开观察 TTFT、TPOT、tokens/s、KV capacity 和 engine build constraints。

## 一个执行选择例子

假设同一 checkpoint 有 BF16 与低精度两条路径。不能只比较“能否启动”，而要同时验证：

| 维度 | 问题 |
| --- | --- |
| Correctness | 固定 prompts 的 logits/token 是否在可接受边界内 |
| Capacity | weights、KV、workspace 各占多少 HBM |
| Latency | 不同 `T_p/T_o` 下 TTFT、TPOT 如何 |
| Throughput | 固定 SLO 下 goodput 是否提高 |
| Compatibility | 目标 GPU、driver、runtime 是否在支持矩阵内 |
| Integration | 通用 module replacement 还是模型专用 graph rewrite |

低精度减少 bytes 只是机制起点；若量化路径引入更多 launches，容量改善可能没有转化为 latency 改善。能否换成可交付能力取决于完整验证。

## Trade-off

TensorRT-LLM 这类优化栈的收益通常来自更深的硬件适配，代价是部署复杂度和调试复杂度上升。

它适合需要高吞吐、低延迟、NVIDIA GPU 深度优化的场景；如果团队只需要快速原型，直接使用通用 runtime 可能更简单。工程上要判断的是：当前瓶颈是否已经到了需要 engine build、kernel fusion、quantization 和分布式 runtime 的程度。

更深的硬件适配还意味着支持矩阵并非抽象问题。模型架构、GPU generation、precision、kernel 与 TensorRT-LLM 版本需要形成经过验证的组合。升级其中一项可能改变 engine build、数值质量和性能，平台必须把这些信息作为模型部署制品的一部分记录。

## 本章在知识树中的位置

```text
Model Linear / Attention semantics
→ GEMM / Attention operator contracts
→ cuBLASLt or specialized kernels such as DeepGEMM
→ TMA / MMA / fusion / quantization
→ TensorRT-LLM execution plan
→ Decode / Prefill runtime
→ GPU Memory
→ 推理调度
```

TensorRT-LLM 章节承担的是“从模型计算到 GPU 执行优化”的桥接。

沿 Compute 横线看，第 37 章处理训练中单层算子的分布式等价性，本章处理推理 graph、kernel 与目标硬件的执行映射；二者复用 operator partition、locality 与 topology 原则，但不是同一 runtime。第 54 章随后验证 execution plan 的 HBM budget，第 63 章验证所需设备与互联能否被实际 placement。

## 自检问题

1. 图优化为什么能在数学结果不变时提高推理效率？
2. operator fusion 主要减少什么开销？
3. FlashAttention 为什么是 memory IO 优化，而不只是 attention 算法名？
4. FP4/FP8 为什么要求软硬件协同？
5. Build-time artifact 与 runtime request state 为什么要分开理解？
6. In-flight batching 在机制层和框架层分别意味着什么？
7. Weight-only quantization 为什么可能降低显存却不降低 latency？
8. 通用 module replacement 与模型专用 structural fusion 各交换了什么成本？
9. 什么时候值得引入 TensorRT-LLM 这类优化栈？
10. 为什么 cuBLAS/cuBLASLt 不能被理解成一个固定 GEMM kernel？
11. GEMM tiling 如何用 shared-memory capacity 换取 A/B tile reuse？
12. `FFMA` 与 `wgmma.mma_async` 分别属于什么执行单元和语义层次？
13. TMA、multi-stage buffer 与 `mbarrier` 怎样形成 producer-consumer pipeline？
14. 为什么 DeepGEMM 与 cuBLAS 是可共存的执行分支，而不是简单替代关系？
15. 比较两个 GEMM kernel 时，为什么必须同时固定 scale semantics、layout、workspace 与 JIT 状态？
16. 多种 token families 共享同一 projection weight 时，为什么一组 quantization scale 可能不再成立？
17. Base family 的选择如何在 Prefill、Decode 与非文本输出之间迁移 correction 成本？
18. 为什么 MoE 的 token balance、activated-expert balance 与 topology-aware balance 各自只有条件成立区间？

## 小结

TensorRT-LLM 把模型、NVIDIA GPU 和 Serving runtime 联结成经过优化的 execution contract。GEMM 执行从 `M/N/K` 和 dtype/layout contract 出发：cuBLASLt 用广覆盖的 heuristic kernel space 交付通用路径，DeepGEMM 一类专用库用 JIT、TMA、MMA 和模型特定 layout 换取更深优化。二者可以在同一 runtime 中共存。MoE 还要求 execution plan 把 activated-expert weight floor、token/tile compute 与 communication 放入同一条件成本模型，不能把 token count 当成跨 regime 的固定时间代理。

Quantization 只有与明确的 graph mapping、可用 kernels 和目标硬件对齐，必要时再进行 structural rewrite，才可能把更少 bytes 转化为更低单步成本；in-flight batching 和 paged KV 则管理持续到来的 request state。

下一章转向 vLLM，观察另一个历史起点：如果首先把 KV allocation 与 scheduler 视为核心，完整 Serving engine 会怎样组织。

## Review notes

- Kernel-Smith（population/archive kernel search；Status: Experimental）: https://arxiv.org/abs/2603.28342

Primary-source 校验入口：

- NVIDIA TensorRT-LLM docs: https://docs.nvidia.com/tensorrt-llm/index.html
- NVIDIA cuBLAS / cuBLASLt documentation: https://docs.nvidia.com/cuda/cublas/
- NVIDIA CUDA Programming Guide, Asynchronous Data Copies / TMA: https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/async-copies.html
- NVIDIA Hopper Tuning Guide, Tensor Memory Accelerator: https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html#tensor-memory-accelerator
- NVIDIA PTX ISA, `mma.sync`, `wgmma.mma_async` and `tcgen05.mma`: https://docs.nvidia.com/cuda/parallel-thread-execution/
- DeepSeek-AI DeepGEMM repository（current implementation and version history）: https://github.com/deepseek-ai/DeepGEMM
- DeepGEMM SM90 FP8 JIT/TMA configuration path: https://github.com/deepseek-ai/DeepGEMM/blob/main/csrc/jit_kernels/impls/sm90_fp8_gemm_1d1d.hpp
- DeepGEMM cuBLASLt coexistence path: https://github.com/deepseek-ai/DeepGEMM/blob/main/csrc/jit_kernels/impls/smxx_cublaslt.hpp
- FlashAttention: https://arxiv.org/abs/2205.14135
- FlashAttention-2: https://arxiv.org/abs/2307.08691
- FlashAttention-3: https://arxiv.org/abs/2407.08608
- SVDQuant: https://arxiv.org/abs/2411.05007
- MoEBlaze（单卡 MoE layer 受限案例）: https://arxiv.org/abs/2601.05296
- TEMPO（calibrated makespan-aware expert dispatch；Status: Experimental；8/16-GPU serving evidence）:
  https://arxiv.org/abs/2608.13057
- FreeBalance（pre-routing expert migration；Status: Experimental；8×A800 prefill evidence）:
  https://arxiv.org/abs/2608.14205
- "MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models", 2026
  （Status: Experimental）: https://arxiv.org/abs/2603.04800
- MASQuant official implementation:
  https://github.com/alibaba/EfficientAI/tree/main/masquant
- Hugging Face Nunchaku Lite integration analysis: https://huggingface.co/blog/nunchaku-diffusers
- Diffusers Nunchaku Lite integration: https://github.com/huggingface/diffusers/pull/14100
- Meta, "Four generations of MTIA to power our AI workloads", 2026（版本化硬件案例）: https://ai.meta.com/blog/meta-mtia-scale-ai-chips-for-billions/
- SGLang-JAX（semantic/backend portability case）:
  https://www.lmsys.org/blog/2025-10-29-sglang-jax/
- Vectorizing the Trie / STATIC（constraint-state execution mapping；Status: Experimental）:
  https://arxiv.org/abs/2602.22647
- DRTriton（Status: Experimental；verifier-backed learned kernel artifact lifecycle）:
  https://arxiv.org/abs/2603.21465
- vLLM `TRITON_MLA_SPARSE` proposal（Status: Experimental；open PR，hardware portability contract）:
  https://github.com/vllm-project/vllm/pull/38476
- TensorRT 11 Multi-Device Inference（version-sensitive graph-native collective contract）:
  https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/multi-device-inference.html

本轮 Review 依据当前官方入口补充了 runtime、in-flight batching、paged KV caching 和分布式执行的边界，同时仍将章节主线限定为 NVIDIA GPU execution optimization。Daily Research 中的 SVDQuant/Nunchaku 只作为跨 runtime 的机制对照，用于推导通用 module replacement 与模型专用 fusion 的边界，不代表 TensorRT-LLM 的功能声明。具体支持矩阵与性能结论必须绑定版本、模型、精度和硬件，不能从通用图优化原理直接推出。

时效性边界：上述官方入口已在 2026-07 重新核验；由于 TensorRT-LLM 的
backend、quantization 和 hardware support matrix 持续变化，本章不把某个
具体 release 的 feature availability 写成长期结论。

2026-W10 的 MASQuant 案例用于补全 distribution-conditioned scales、shared base + conditional correction、
mask routing 与 modality-sliced deployment contract。其 theorem 只覆盖受限 calibration/reconstruction
假设，公开 fused kernel 也未形成完整可重放 release；正文不保留 benchmark 数字、固定 rank/base 配方，
也不把“decode 零开销”外推到非文本或 interleaved generation。

2026-08 的 GEMM refinement 进一步区分了 model-level GEMM contract、cuBLASLt
heuristic、specialized JIT kernel、PTX/SASS instruction 与 hardware pipeline。
DeepGEMM 的功能范围、SM90/SM100 支持和 FFMA scheduling history 都是版本化事实；
tiling、reuse、asynchronous producer-consumer pipeline 以及专用化与兼容性的交换才是
本章保留的长期机制。
