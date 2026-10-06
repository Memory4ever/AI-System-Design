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

图优化不应在“代数等价”和“硬件 schedule”之间过早提交。Typed equality space 可以先保留多种等价 tensor expression，再让 tile、layout、fusion 与 cost model 选择 implementation；这比固定图后的局部 autotune 搜索更广，却带来 e-graph 膨胀、编译时延和 cost-model 偏差。长期 contract 是让 algebra、shape、dtype、layout 与 target hardware 共享同一 typed state，而不是把某个搜索器的速度数字当成通用结论。

<!-- source-family:SF-2026-ARXIV-2609-12330 -->

不过，保留等价表达式还不等于能让它们跨越多个编译阶段。一个替代分支把 e-class/e-graph 作为原生 IR 状态：constructive rewrite 增加候选而不销毁旧表达式，rebuilding 恢复 congruence；阶段性的 extraction 将选择与替换分开，只提交已确定的部分，让未抽取的候选继续交给后续 analysis 或 cost model。这要求参与的 pass 保持声明的等价关系与数值前置条件，而不是任意 lowering 后候选仍自动有效。[Persistent E-Graph v1](https://arxiv.org/pdf/2602.16707v1) 的实现仅覆盖 pure straight-line，尚未解决 control flow、scope 或 side effects；实数恒等式也不授权浮点 bitwise 等价。其 31 个 FPBench 单轮样例全部触及 4000-node 上限，高精度求值与匹配成本使整体比所用 Herbie 对照约慢 401 倍，局部 matcher 改善并非端到端编译或 LLM kernel 加速。持续携带状态适合仍需跨阶段比较候选的场景，但要计入增长、重建、匹配和验证费用；pass 不兼容或预算不足时，显式抽取并回到既有固定图 pipeline 仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-16707 -->

扩大搜索空间以后，还要判断哪些局部计划能安全地裁剪。若两个 partial mapping 对未来组合暴露的 tensor tile、dataflow、执行顺序或 backing memory 不同，仅比较当前 latency 与占用就可能删掉后来更好的计划。一个条件分支先按这些接口划分 compatible groups，再在组内保留 Pareto 前沿；中间 tensor 的 reservation 保留整个 lifetime，包括未来尚未确定的消费关系，只有条件充分时才 collapse。资源计数也不能统一相加：同一 branch 内可并存的 reservation 求和，不同互斥 branch 取最大值，未知未来分支不能提前折叠。这是资源 lifetime 的合成条件，不是执行 latency 的串行或并行公式。这让局部裁剪与后续组合共用明确条件，但所谓最优仍仅针对声明的 mapspace 和 cost model，而不是所有可执行 kernel。<!-- source-family:SF-2026-ARXIV-2602-15166 -->

这类搜索还须与目标硬件测量分账。[Fast Fusiest v1](https://arxiv.org/html/2602.15166v1)主要在 TPUv4i-like 解析模型下比较，复用缓存的 baseline 查询时间及给予其他方法更大搜索预算都影响所报速度与质量；它没有证明端到端 GPU serving 加速。接口不兼容、reservation 分支过多或 cost model 偏差较大时，应扩大保留集合或回到已有 backend 的局部 autotune 与实机 profiling，不能凭一个局部 Pareto 标签跳过正确性和质量验收。

另一个独立问题是 dataflow 不能独占数据放置的语义。显式 storage node 指定 tensor 在哪一级 memory 保存以及跨哪些循环存活，循环顺序表达消费方式；二者分开才能区分“重复计算以免存储”与“保留数据以减少搬运”。在相应表示中，同一组 storage nodes 之间的 loop 顺序可按声明条件作等价裁剪；但 convolution 的 partially relevant rank 直接位于 storage node 之下时会改变 line-buffer 行为，必须保留相应顺序分支，这不授权跨 storage node 重排。先对符号化维度求出可复用的条件函数，再代入具体 shape 的 currying，可以减少每种 shape 从头重复搜索，却仍依赖维度相关性、整除条件和硬件模型。<!-- source-family:SF-2026-ARXIV-2602-15172 -->

[TCM v1](https://arxiv.org/html/2602.15172v1)在 TPU-like 与 NVDLA-like 解析评价里展示这种分离；其中大型 QK 负载的 37 秒是单 CPU 线程的映射搜索时间，不是 GPU kernel latency，给予对照的 1000 倍搜索预算也不等于匹配预算的真实吞吐实验。部分配置依靠 heuristic 限制 PE 空间，不能把该配置的最优性推广到被排除的计划。符号条件失效、shape 或 memory 层级变化时，须重新求值或搜索；这与前面的等价表达式探索、兼容性裁剪和局部 autotune 是可共存的分工，而非同一条最优性证明。

朴素执行方式会产生很多额外开销：

- 多个小算子分别 launch kernel。
- 中间结果频繁写回 HBM 再读出。
- 常量表达式运行时重复计算。
- 独立算子没有被合理并行调度。

图优化的第一性原理是：数学结果不变的前提下，减少运行时不必要的计算、访存和调度开销。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-20706:start -->
同一 execution contract 也适用于浏览器等受限 backend。WebGPU 路径可以为 llama.cpp 风格模型提供跨 weight
format 的加载、内存管理与 kernel 映射，使本地推理不依赖服务器 GPU；但 browser sandbox、operator coverage、
shader/compiler 差异和设备内存会显著缩小可执行图。作者模型、浏览器和设备上的性能不证明跨平台 portability。
构图、dtype、layout 或精度验收失败时，应回退 CPU/WASM、原生 GPU backend 或远端 serving，而不能仅因权重
成功加载就宣称模型可正确高效执行。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-20706:end -->

### 冷启动的执行计划要包含加载和解包

常驻 GPU 上优化 kernel 通常从已加载的权重开始；端侧模型被回收、每次从 flash 重启时，编译图、加载、解包与 prefill 共同决定首 token 关键路径。先物化图并按层重叠加载是合理基线；若 flash 读取仍主导，存储 bit 数可以低于 NPU 原生计算 bit 数，但必须把转换成本一起编入计划。一个条件分支按 NPU 允许的 output-channel 分配存储精度，将可变 bit 权重拆为 1/2/4-bit 片段并交错存储，CPU 用 SIMD 解包成 INT8 再交给 NPU，而不是要求 NPU 直接执行任意低 bit 格式。

更小文件不必然更快：padding 产生 read amplification，过紧编码又可能让解包成为新瓶颈；分配 bit 所优化的局部误差代理也不是端到端质量保证。执行侧把整数 matmul 留给 NPU、其他算子留给 CPU，并在依赖已满足的队列内优先推进较早 prompt chunk，空闲 CPU 只在 NPU 队列足够长时 steal 任务，避免反过来饿死 NPU。收益因此取决于 flash 带宽、prompt 长度、operator placement 和质量门槛，而非压缩比。受限 [EdgeFlow 实现](https://arxiv.org/html/2604.09083v1)还逆向使用 QNN 图格式，新增兼容性风险；平台不匹配、短常驻负载或质量不满足时，原生格式和静态图仍更简单。<!-- source-family:SF-2026-ARXIV-2604-09083 -->

### 静态图可以固定接口，而不必固定每个 Adapter 值

静态 NPU 把算子与 shape 提前编译，按任务分别构图并共享 base 权重是最直接的基线；将所有 adapter 常驻再用选择 mask 切换，则用容量换更少重编译。还有一个窄分支把同尺寸 LoRA 矩阵变成 runtime 输入：固定图保留低秩更新的算子与 placeholder shape，请求只提供对应的 adapter 值。编译计划因而拥有接口、精度与 layout，adapter artifact 拥有具体参数；换值不等于换 shape，也不能把 adapter 训练方式与执行 ABI 混为一谈。<!-- source-family:SF-2026-ARXIV-2604-18655 -->

输入化仍有搬运、显存与后端 operator coverage 的成本。多输出路径共同 prefill 后隔离 suffix 的 KV，是另一项状态条件，不授权任意 adapter 共用 prefix cache；第45章仍负责 base/adapter/KV 身份，第30章负责低秩训练。[受限手机 NPU 实现](https://arxiv.org/html/2604.18655v1)只支持披露的1B/3B模型、固定接口与设备分支，其不同精度配置、相对评分与吞吐算式不能拼成统一加速证明。尺寸、精度或状态不兼容时应重编译、拆成独立图，或回到已验证的通用执行路径；运行时输入并不消除质量和端到端验收。

在模型 base 长期固定、单流低延迟且允许为该权重制专用逻辑时，可以进一步把不可变参数从存储 artifact 固化成 ROM 地址到权重 bit 的组合函数：ternary 零 bit 接地、共享布尔子表达式，非零值再进入本地 matrix-vector 计算。与可换值的静态图不同，存储布局直接依赖该 base 的 bit pattern；分布式 weight bank 配合本地计算和全局 reduction，用面积与版本灵活性换片上带宽，参数稀疏不必经通用 index 解码。但稀疏率、bank 尺寸和 routing 共同决定密度，不能从零参数比例推出同比面积节省或任意模型收益。<!-- source-family:SF-2026-ARXIV-2602-20662 -->

保留可写 SRAM adapter 能在 fixed base 外叠加低秩更新，并复用同一计算阵列后求和，却不能把 adapter 训练或纠错能力当作 base 已可重写：改变固化的 base 需要新的逻辑或芯片 revision。Adapter 与 KV 共享容量，更多低秩投影和更长 context 会增加 SRAM、面积与功耗。[TOM 的有限 BitNet-2B/FP8 证据](https://arxiv.org/html/2602.20662v1)来自 cycle 模拟、EDA 与 ROM 模块 P&R，只支持该存储执行分支，不是 fabricated whole chip、任意量化质量或零 wake 开销证书；跨 node 归一化也不等同硬件实测。Base 频繁变更、质量未经验证、SRAM 预算或芯片生产成本不合算时，可写 SRAM、外存权重及通用 backend 仍合理，冷启动和完整 request 成本另验。

### 静态图还要容纳不规则 KV 重算

固定 shape 的静态图并不要求选择性 KV 重算只能回到全量 prefill：动态输入可以切成固定容量 chunk，padding 后用 valid mask 排除无效位置，并强制选择真正末 token 以形成生成 logits；选中位置经过 gather、计算与 scatter 更新原 cache。比较 KV deviation 所需的数值范围又与普通 activation 不同，必要时让差值和 Top-K 使用较高精度，而非沿用一套整数校准。此处的 non-prefix 选择性复用仍是近似分支，静态形状适配本身不授予状态等价保证。

各类 token 分别调用图最简单，却可能产生大量半空调用；新 token 总须重算，因而可以在容量与重算比例约束内并入相邻选择性重算图，再按实测 per-call latency 用动态规划选择 chunk 组合。目标是在 padding 与调用的取舍中最小化所测 graph latency，而不只是最大化复用率。[Dynamic Flow, Static Graph v1 §4/7](https://arxiv.org/html/2609.34727v1)的有限 Qualcomm/小模型结果仍有 QA 质量下降，完全复用虽快却更差；线上须计 KV 搬运和 pipeline，离线 graph compilation、profiling 与跨平台重校准则另作摊销。形状或比较精度不支持、质量门失败、收益不足时，保留 exact prefix reuse、full prefill 或已验证的动态 backend。<!-- source-family:SF-2026-ARXIV-2609-34727 -->

## 三类基础优化

第一是 operator fusion。把连续的小算子合并成更大的 kernel，减少中间 tensor 的 HBM 往返，也减少 kernel launch overhead。

第二是 constant folding。在编译或构图阶段把只依赖常量的表达式提前算掉，避免每次请求重复执行。

第三是 scheduling optimization。根据依赖关系安排算子执行顺序，让可并行的工作更充分地利用 GPU。

这些不是 TensorRT-LLM 独有思想，而是高性能推理系统的通用原则。TensorRT-LLM 的意义在于把这些原则和 LLM 特有结构结合起来：attention、KV Cache、GEMM、collective communication、quantization、batching。

### Lowering 与低精度执行都需要可回归的 Commit Boundary

手写 GPU kernel 把语义、schedule 与目标硬件揉在同一份代码里，局部极致却难复用。受约束的 source-to-source
lowering 让高层程序保留语义，变换规则逐步提交 layout、memory 与 CUDA 实现；编译通过只是第一关，数值等价和真实
workload 性能回归才拥有 artifact commit。收益是复用与可移植性，代价是目标相关假设、变换交互和验证矩阵扩大；
规则无法证明或 regression 失败时，应回退已知 kernel。exact-v1 只支持作者 §5–7 的变换与评测，不构成通用编译收益。

<!-- source-family:SF-2026-ARXIV-2605-13864 -->

回归身份还必须包含实际 compiler 与 CUDA library component，而不止高层模型、dtype 和 source。源程序合法、scale 已写入 descriptor，并不保证生成的二进制忠实执行它：[CUDA 13.2 Update 2 的具名纠错](https://docs.nvidia.com/cuda/archive/13.2.2/cuda-toolkit-release-notes/index.html#resolved-issues)包括两层以上嵌套 divergence 中被省略的 reconvergence 导致旧 register 值残留，以及 cuBLASLt 的特定 NVFP4 输出算法忽略 tensor-wide scale。后者仅涉及算法 ID 66、compute capability 10.x/11.x 与该 scale pointer 设置，不能改写成所有 FP4 运算都错误。运行 artifact 因而要把 compiler、cuBLAS、目标架构与算法选择一起绑定，再在相关分支和非单位 scale 下对照 reference；框架发布采用新组件只是修复交付事件，不等于已有二进制已重新构建或服务实例已替换。<!-- source-family:SF-2026-PYTORCH-2141 -->

这扩大了构建与数值回归矩阵，也增加 canary 和重新编译成本；不受影响的成熟路径仍合理。更新一个 toolkit 更不能取得全体 kernel 的安全证明：同版仍列有特定 WGMMA wait/copy-propagation 的已知竞态。受影响路径尚未验收时应禁用、重建或回退已验证 kernel，保留具体未知范围；官方修复说明与本书的执行合同推论，不是本项目已复现该错误或测得生产性能。

这个 commit boundary 也适用于 RTL 的 source 改写：较强的后端优化可能把原表达式与改写版本归一到相近实现，较弱的优化配置下保留的 source 收益便会消失。因此比较对象必须绑定 compiler、优化模式、目标 library、clock constraint 与成功通过转换的人口，不能沿用 source 排名预测另一后端的 PPA。功能等价检查、有限时序模拟与综合后的面积/时延估计是不同验收，不共同构成所有硬件上的证明或实芯表现。新增搜索、编译、验证成本与失败转换都应计入；后端切换或回归后，应重新评测最终 artifact，收益消失时保留原 RTL 和已验收的编译配置。<!-- source-family:SF-2026-ARXIV-2601-01765 -->

在语义验收之后，按算子名称选择执行介质，在算子与 kernel 一一对应时足够简单；融合、分解和逐步 lowering 后，一个 softmax 或 attention 却可能变成性质不同的多个循环。放置候选应绑定实际 parallel loop nest，而不是沿用原 operator 标签：bufferization 保留 allocation、alias 与读写集合，进入低层 IR 前记录并行量和嵌套 trip count，再以 host profile 区分读带宽瓶颈与 store-bound 路径。只看 off-core read 会漏掉绕过 cache 的写流。足够工作量与理想执行下界只能排除明显不值得搬的候选，不能自行证明真实加速。

逐 nest 决策增加 profiling 与 metadata；继续细化到 basic block，还可能增加 host/PIM 切换与边界物化成本。搬运、切换和同步须另计，不能因多个 region 共用 buffer 就把每次完整移动的保守模型称为实测流量。[Torch-PIM v1 §4–5](https://arxiv.org/html/2609.34657v1)组合真实 CPU 时间与模拟 PIM，阈值由有限 loop 集校准；部分配置更慢，更多 core 或更大输入也不单调有利。证据支持候选粒度与测量权限的分工，不证明实芯服务吞吐或质量。Profile、alias、shape 或目标硬件不匹配时，原 host、粗粒度放置与已验证 kernel 仍是可用分支。<!-- source-family:SF-2026-ARXIV-2609-34657 -->

低精度执行中，逐次 dequantization 也可能成为固定前置开销。按 activation 数值范围分解并让不同尺度走不同执行路径，
可以减少共同 dequant bottleneck；controller 必须版本化分解规则、scale、融合 kernel 与未命中路径。它用更复杂的 kernel
和额外数值误差换吞吐，硬件适配、outlier 或融合失败时应回退标准 dequant/高精度路径。论文只证明作者 Method 与数值
实验范围，未证明任意模型、GPU 或并发 SLO 都获益。

<!-- source-family:SF-2026-ARXIV-2605-13915 -->

### 顺序程序拥有语义，Parallel Annotation 拥有 Schedule

共享语义还可以前移到模型定义：同一份 shape-indexed operator DAG 同时驱动 eager execution、反向 AD 与导出的 bound checker，避免训练、执行和验证各自重写网络后悄悄换了对象。但“共享图”不等于三个数值域已经相同：实数上的梯度定理、明确的 IEEE binary32 executable model、以及具体 compiler/kernel/hardware 的结果需要分别建立关系。NaN/subnormal、FTZ、FMA contraction、reassociation、reduction order 与 transcendental policy 都是目标执行合同；有限 interval/CROWN enclosure 也不是完整可判定的 verifier。[TorchLean v1](https://arxiv.org/html/2602.22631v1) 提供这种 shared artifact 分支，却将真实硬件 refinement 留作后续工作，部分外部数值库仍是显式信任边界。构建图、导出和检查增加费用，原文控制器切片的慢 checker 不能藏在轻量证书回放之后；GPU 一致性未建立或检查成本无法摊销时，保留成熟 runtime 与独立数值回归，不把 prover 接受解释成已经证明线上执行安全。<!-- source-family:SF-2026-ARXIV-2602-22631 -->

异步 copy、tensor-core schedule 与 synchronization 若散落为 imperative side effects，很难证明优化前后同义。更可审计的 compiler contract 以 sequential specification 作为语义与 fallback，把 parallel annotation、unsafe rewrite 与 equivalence check 共同版本化；compiler 只有在证明条件成立时才能提交并行计划。<!-- source-family:SF-2026-ARXIV-2609-16389 -->

这种分权牺牲一部分手工自由并增加证明成本。当前证据限 H100 concrete-size GEMM，且存在 TMA unsafe rewrite、无完整 CUDA semantics；Blackwell、非 CUDA 或动态 shape 必须重新验证，失败时回退顺序/已知 kernel。

### 融合决策与数据搬运可以分层表达

在规则算子中，直接用一套 loop、tile 和 memory-access schedule 表达融合，最便于接成熟 backend；复杂 reduction 链却会让早选 layout 妨碍后续表达式重写。一个分支先在 scalar IR 决定 loop 与 fusion，再用值级的 virtual-register tile IR 保留计算表达式，最后 lower 为显式 memory-access tile IR，交给 backend 决定搬运与执行布局。前一层拥有表达式变换，后一层拥有数据移动；延后 layout 不等于省略 tensor lifetime 或数值验收。

跨 reduction 的融合还可能先改写依赖，再通过额外的 repair 运算恢复计算关系；因此不能只计减少的 launch 和 HBM bytes。Scheduler 需要 look-ahead 找到可一起捕获的 reduction/elementwise 链，并结算 repair、scan/split-buffer 与 local-memory live range。搜索、编译和 backend 覆盖也进入成本：受限 [Nautilus v1](https://arxiv.org/html/2604.14825v1) 的 GH200/RTX5090、FP16/FP8、batch 1/8、序列1K～32K kernel 比较中，RTX5090 对 TileLang 的几何平均仅1.01，部分模型1.00，不构成整套服务或并发SLO收益。Repair 或搜索成本不能摊销、backend 不支持或数值回归时，普通 fusion、静态成熟 kernel 与手写 tile 仍共存。<!-- source-family:SF-2026-ARXIV-2604-14825 -->

按循环轴选择 tile，在矩阵乘法等复用已沿轴对齐的算子中最简单；数字 CIM 的阵列形状固定后，卷积等算子的同一 operand 复用却可能落在斜向 hyperplane 上，原坐标会掩盖可共享访问。编译器可以从 access matrix 的零变化方向识别复用，先用 pre-tiling 限制坐标变换的边界膨胀，再以合法 affine 变换把这些方向重新对齐；随后才合并虚拟复用空间、按有限 macro 数 post-tile，并确定实际 operand layout、搬运与缓冲。复用被表达出来与阵列能高效执行是两步，不应只按 operator 名或逻辑 tile 大小判断映射。

这条分支增加变换搜索、索引/layout 转换、缓冲与边界处理；提高 macro utilization 或降低一个 traffic 代理，不等于完整执行时间最短。[PolyCIM v1 §3–4](https://arxiv.org/html/2609.34351v1) 的有限数字 CIM 模拟与 CNN/单算子对照支持这种复用暴露，group/3D 算子收益较小，离线准备也不能从账本消失。合法迭代域与依赖保持还不自动保证浮点 accumulation 逐 bit 相同，完整任务质量和服务 SLO 需另验。原复用已对齐、搜索难摊销或目标阵列/数值检查不支持时，保留常规 tiling、im2col 或已验证 kernel，而不是为追求阵列填充继续重排。<!-- source-family:SF-2026-ARXIV-2609-34351 -->

### 从逐 Kernel Launch 到 Persistent Executor

压缩 artifact 只有进入真实 load/decode 数据流才形成系统收益。Weight codebook、KV precision、contextual sparsity 与 prefill/decode schedule 必须共同编译；否则更少 bits 可能被解码、随机访存或不规则稀疏抵消。联合设计提高专用 operating point 的效率，却降低 portability，并可能只在模拟架构上成立；通用 GPU kernel 与较高精度仍是覆盖面更广的 fallback。

<!-- source-family:SF-2026-ARXIV-2609-12208 -->

独立 kernel launch 对大算子、稳定 control flow 和容易 capture 的 shape 最透明，CPU submission 开销相对计算也很小；CUDA Graph 进一步把重复 DAG 的准备成本移出 hot path。动态 inference、attention 辅助操作和 micro-batch 中出现大量短小算子后，单次 CPU→GPU launch 可能比算子本身更贵，而 graph 又要求可重复的结构，此时静态 fusion 与 graph capture 之间出现一个运行时分支。

已知且高频的 shape 可以启动时预捕获 graph；未覆盖的长度却不必永远回退逐 kernel launch。一个条件分支让本次 cache miss 先沿 JIT 路径执行可静态化的计算段，同时在另一 stream 为该 shape 异步 capture；只有完成事件确认 graph 可用后，才插入带容量与淘汰策略的 rolling cache，供后续同 shape 请求 replay。动态预处理和采样仍由 JIT 路径承担，graph 只拥有已捕获的静态子图，而不接管任意动态控制流。<!-- source-family:SF-2026-ARXIV-2604-23467 -->

计划准备成功也不保证 replay 时其元数据仍活着。重复 attention 调用若复用 prepared graph，query-length storage、descriptor 的 layout/device key 与当前 scale/sink binding 必须由 wrapper 在整个 capture/replay 生命周期持有；重新 plan 不能释放旧 capture 仍引用的对象，也不能以兼容 shape 沿用不同 strides 或语义。回归因此应加入 `capture → replan → allocator poison → replay`，并与 output/LSE reference 比较，而非仅断言能 launch。[FlashInfer 的 cuDNN adapter 纠错](https://github.com/flashinfer-ai/flashinfer/pull/5350)支持这条窄寿命与绑定边界，且明确拒绝仍不支持的 masking/scaling 与单 token GQA prefill LSE 路径；局部 B200 回归不证明所有 backend 或服务 SLO。保留 prepared state 用内存驻留、完整 cache key 和更多测试换更少准备成本；兼容性无法证明时，重新 plan 或不捕获的已验证路径仍是正确分支。<!-- source-family:SF-2026-FLASHINFER-071RC -->

这把重复 shape 的 host submission 成本换成首次 miss 的 JIT/capture 延迟、额外 workspace 与 graph 驻留、事件同步和缓存失效处理；异步 capture 还可能被 cuBLAS 调用串行化，不能按两条 stream 推断完全重叠。shape 稳定时预捕获仍简单，低重复率或显存紧张时独立 launch、JIT 与受控 padding 仍有位置。受测证据仅为单 H100、FP16、LLaMA-2 7B、batch 1、预热后的长度 10～500；论文文字称全部长度有最低 P99，但 Table II 的逐 token P99 在 350/500 token 分别为 18.90/23.68 ms，高于 TensorRT-LLM 的 16.53/16.65 ms。不能据此承诺并发服务或整请求 tail SLO。

Graph 路径把重复的 shape 固化为可重放计划；若短 task 的依赖和 shape 持续变化，则需要另一种减少 host launch 的执行契约：让受限任务在设备端队列中被领取。这个分支不继承 graph 的静态重放保证，生成执行器时尤其要验证中间状态。

Agent 生成 persistent megakernel 时，最终 token 正确仍可能掩盖中间 state corruption。更安全的演进是先把候选限制在 progressive typed milestones，再用独立 mid-state oracle 检查各阶段，并在目标 shape/precision 上做性能 admission。它缩小了搜索自由度并增加验证成本，却把 silent error 转成可定位失败；oracle 只能证明所测状态，不等于形式验证或跨架构正确。

<!-- source-family:SF-2026-ARXIV-2609-12379 -->

Persistent executor 在进程启动时常驻少量 GPU resources，由 host 把 typed operator descriptor 写入 ring buffer；常驻 warps 原子领取任务、分派受支持的 operator，再回到队列。Runtime 拥有 descriptor schema、operator registry、queue ordering、resource admission 和错误传播，常驻 kernel 只消费已验证任务，不能自行改变 execution plan。这样避免每个小算子都经过完整 launch path，同时保留比固定 graph 更动态的注入能力。

代价是常驻 thread blocks 会与大 kernel 竞争资源，spin polling 消耗功率，backoff 又可能抬高 tail latency；ring buffer saturation、unsupported operator、顺序依赖和 persistent-kernel failure 也需要显式恢复。规则 shape 继续优先 graph capture，粗粒度算子继续独立 launch；只有 profile 证明 launch-bound 且 coexistence 不破坏目标 SLO 时，persistent executor 才值得进入 plan。

常驻队列解决了谁领取任务，却不自动解决动态任务依赖怎样生成。一个编译分支把 wait-count、notify 和 trigger 表达为可随 symbolic shape 变化的 event tensor，再 lower 为整数 counter、等待与通知操作；例如 MoE 的 top-k 结果改变 expert 的就绪计数，实际分配边界决定可启动的 GroupGEMM tiles。编译器拥有依赖表达与 lowering，执行器只推进已满足依赖的工作；这是 shape/data-dependent 图与 megakernel 的接口，不是 host descriptor 换一个名字，也没有给任意操作补出内存可见性证明。

静态 per-SM queue 减少全局争用，但要用代表 shape 生成计划，并可能选择下一个更大容量；数据依赖无法静态分解时，保守共同 event 会损失细粒度并行。动态 centralized queue 更灵活，却增加 global-memory push/pop 与争用，作者部分 dense/单 token 配置反而慢于基线。离线编译、warmup、常驻资源和端到端框架开销应一起计费，不能只从更快的单段推普遍 SLO 收益。Shape 规则时保留 graph/static 路径，粗算子或数据依赖调度收益不足时保留独立 kernel；只在实际 profile 与数值验收支持时切换。<!-- source-family:SF-2026-ARXIV-2604-13327 -->

常驻任务领取还留下一个资源问题：MoE routing 改变本层实际跨 GPU token 量，固定通信 SM 与计算 SM 比例可能让一边闲置。可在 routing 完成后按每 GPU 实际工作量，在设备内联合选择通信 SM 数和 GEMM/combine 的 chunk 数；dispatch 保持完整，通信 worker 完成 dispatch 后先领取一段 GEMM，再回到分块 combine，最后 combine 让所有 SM 参与。这里运行时改变的是本层资源角色与工作粒度，不是重新决定 expert 路由或全局 placement；重复远端 token 可在 dispatch 复用一次传输，combine 仍须处理 expert 贡献。

分块缩短尾部却降低小 GEMM 效率，抢占计算也须遵守依赖与内存可见性。受限 4×H100 SXM、EP4、BF16、batch 1 prefill 实验中，模型挑选配置距实测最优仍有平均 8.2% 差距；MoE 层收益不能直接等同完整请求收益。它依赖目标硬件吞吐校准，不证明 decode、故障恢复或生产尾延迟；workload 稳定或收益不足时保留固定 partition 与普通 kernel。 [必要机制与反证](https://arxiv.org/html/2609.21483v1)。<!-- source-family:SF-2026-ARXIV-2609-21483 -->

Per-SM queue 的局部性还取决于哪些 SM 实际共享缓存。单 die 的统一 L2 下，平坦任务领取可以继续保持简单；多个 chiplet 各有私有 L2 后，任意领取会把同一 weight tile 的并发访问分散到不同 cache partition。此时 execution plan 可以显式增加 chiplet 级 task：按输出列分配 weight slice，再让 chiplet 内的 workers 先遍历共享同一 weight tile 的 batch tiles，使短暂工作集在同一个 L2 内复用。完成责任也随硬件作用域分层：局部 workers 累积本 chiplet 的完成计数，由最后一个 worker 负责必要的 L2 writeback 和 GPU-scope global event，只有跨 chiplet 的完成条件满足才放行下游 task。局部计数不能被误写成任意 memory model 下都免 fence；不可变 task descriptor、cache partition、可见性操作与事件阈值必须共同成为 plan 的条件。

这条分支以常驻 scheduler 资源、cache 策略和 task 粒度维护换取局部复用，不是把所有 persistent-kernel 加速归因于 chiplet。受限 [Fleet v1](https://arxiv.org/html/2604.15379v1) 的单 MI350X、Qwen3-8B BF16、64 输入/1024 输出、batch 1～64 decode-only 测量中，8 个 scheduler 占 256 CU 的 3.1%；低 batch 没有额外 weight tile 共享，SiLU fusion 在 CU-task 中也有效。batch 32/64 的 cooperative traversal 对 chiplet-unaware megakernel 为 1.27/1.30 倍、HBM read 为基线的 0.82/0.63，但另一种 M-split 在 batch 64 的 read 反增至 1.20。batch 64 的 M-tile 18.61ms 又慢于成熟 vLLM 的约 11～12ms，作者说明尚未加入 K-split 和 attention 优化；对 Mirage 的改善不等于相对成熟 serving engine 或端到端普遍获益。prefill、tensor parallel、多模型及其他 GPU 并未得到同样证明，短 task、寄存器压力或 tile 窗口不能摊销时，应保留原有 static graph、独立 kernel 或较简单的 persistent plan，并重新测完整请求成本与数值正确性。<!-- source-family:SF-2026-ARXIV-2604-15379 -->

在决定使用 graph capture、persistent executor 或继续逐 kernel launch 之前，必须先知道 host overhead 落在哪一层。只看总 “framework tax” 会把执行栈压成一个残差；TaxBreak 把每个 kernel 的 host orchestration 精确拆为 framework translation、CUDA-library front-end translation 与 kernel-launch floor，再用 HDBI 对照 host orchestration 和 device-active time。它是 execution-stack diagnosis，不是 scheduler protocol：profile 可以说明应优化哪一层，却不拥有 request admission、placement 或 plan revision。更细归因会引入 instrumentation cost，且各分量比例随模型、硬件和软件版本改变；大算子已经 device-bound 时，粗粒度 profile 仍可能足够。`arXiv:2603.12465v1` 的证据只覆盖 §III 的三段分解与 HDBI，以及 §IV–§VI 所披露的测试条件，不支持把 request/stage identity 或其他 profiler taxonomy 归因给该论文。<!-- source-family:SF-2026-ARXIV-2603-12465 -->

浏览器后端把这条归因链进一步暴露出来：每个小算子既经过 framework 编排，也经过受安全验证约束的 WebGPU dispatch，再执行 shader。Fusion 前后的端到端差值除以减少的操作数，得到的是**每操作的总开销估计**，不是底层 API dispatch 的直接测量；而异步 queue submission 的 CPU 时间也不能简单相加为 GPU wall time。因而应分别保留顺序 dispatch 对照、host 分层 trace 与相同 kernel 的 fusion 对照，明确哪些量直接测得、哪些只是有重叠的推导残差，再决定优化 API、框架还是 shader。

更细的实验增加 profiling 成本，受限 backend 还可能无法取得逐 kernel 的设备时间；跨精度、跨设备对照不能用来唯一归因。[WebGPU Dispatch 的受限研究](https://arxiv.org/html/2604.02344v1)的端到端开销分账主要绑定 RTX5090/Dawn/Vulkan、Qwen2.5-0.5B、float32、batch=1、5输入/50输出 token；多厂商直接 dispatch 与端到端测试扩大了观察范围，却没有证明完整分解跨平台不变。算子已足够大、device-bound 或诊断成本无法摊销时，较粗的端到端 profile 仍合理。<!-- source-family:SF-2026-ARXIV-2604-02344 -->

当分层测量已确认瓶颈在设备 kernel，stall 样本标出的仍只是等待发生处，不一定是可以修改的起因。可从该机器指令沿寄存器、谓词及目标 GPU 的 wait/barrier 依赖反向追踪，提出源代码层面的候选原因，再在相同 shape、精度与硬件配置下改变 tile、访存或流水安排，以数值回归和实际 kernel 时间检验。这样的切片把“该优化执行栈哪一层”推进到“哪条依赖可能阻塞执行”，却不把启发式 blame 权重当作已证明的因果关系；没有可行动瓶颈或采样会显著改变并发行为时，原有 vendor profiler 与较粗测量仍更合适。<!-- source-family:SF-2026-ARXIV-2604-20032 -->

更细的归因需要 PC 采样、指令映射与事后分析，也会受 vendor 同步语义、样本稀疏和分支近似限制。受限的 GPU stall 案例中，专家根据诊断修改过 llama.cpp 的量化矩阵 kernel 和 HipKittens 的 RMSNorm；一个配置上的局部 kernel 改善并不证明工具能自动优化，更不证明 Prefill/Decode、batch 与服务尾延迟同时改善。只有在请求关键路径确实包含该 kernel，且部署配置下的正确性与端到端收益均通过时，才把修订后的 kernel 提交到 execution plan。<!-- source-family:SF-2026-ARXIV-2604-20032 -->

<!-- source-family:SF-2026-ARXIV-2604-17861 -->

### 固定部署可以把 MegaKernel 调度上提到编译期

普通 runtime 根据动态 DAG 在执行时分支调度，适合 shape 和配置变化；固定 deployment configuration 下，反复支付分支与 launch 开销并不必要。编译期 search 可以在 shared-memory、K-splitting 和目标 GPU 约束下选择 MegaKernel execution path，runtime 只执行已验收计划。它减少在线控制，却增加离线搜索、架构耦合和配置漂移风险；shape、精度或资源约束变化即使旧计划失效。无法冻结 workload 或搜索证据不足时，应回退普通 kernel graph 与 runtime scheduling。exact-v1 的作者 benchmark 只绑定披露的 Ada GPU 和配置，不构成跨硬件生产承诺。

<!-- semantic-body-binding:SF-ADA-MK-ADAPTIVE-MEGAKERNEL-OPTIMIZATION-VIA-AUTOMATED-DAG-BASED-SEARCH-F -->

### Execution Plan 可以修订，但只能在安全边界 Commit

静态 build artifact 在 workload 与硬件稳定时最可预测；长会话和 Prefill/Decode shape 分化后，同一 request 可能
需要不同 device placement 或 kernel plan。此时 plan 可以由 runtime 提议修订，但不能在任意 token 中途生效：

```text
model artifact + hardware profile + phase/shape
→ prefill plan / decode plan
→ preload resources and validate compatibility
→ commit at token or phase boundary
→ execute under one plan revision
→ fallback without changing committed outputs
```

Plan identity 必须绑定 model、precision、KV layout、parallel topology、kernel set 与 revision；scheduler 只能在旧 plan
完成的状态边界切换，并保持 committed-token frontier 不回退。动态 plan 用 adaptation 换 preload、迁移、预测错误和
recovery 复杂度；shape 稳定、graph capture 或 tail 可预测性优先时，单一静态 plan 仍更好。Fleet admission 与跨
worker routing 由第 56 章负责，本章只拥有单个 execution runtime 内的安全 commit。

原位更新模型时，checkpoint representation 与 kernel representation 也不能被当作同一个完成状态。低精度权重可能经过 repack/swizzle，甚至改变参数 shape；直接把 checkpoint 值写进已打包 tensor，或 load 后不再执行 postprocess，会让新权重仍被旧布局 kernel 解释。一次更新 session 应先恢复可加载表示，再装入各 bucket，最后完成 post-load 转换；target 与 speculative draft 的 runner 集合和选择条件也必须由同一更新入口显式枚举，不能靠不同路径各自猜测。[SGLang 的具名 refit 纠错](https://github.com/sgl-project/sglang/pull/40777)支持这条表示与 finalize 边界：从 engine 装入和外部 P2P/RDMA 写入的 finalize 路径需要区分，不把 begin/end API 自身称作跨全 fleet 的原子发布。<!-- source-family:SF-2026-SGLANG-0521 -->

额外 session 状态、restore/finalize、暂停与 draft 协调增加更新延迟和恢复复杂度；普通高精度、无打包路径仍可更简单。session 结束只能证明所覆盖 runner 的转换与提交条件，不能自行证明外部写全部退役、所有服务已切换、模型质量或 KV 兼容。相关表示、runner 或 completion 条件无法核实，应保持暂停、重新载入完整已验证 artifact 或回退旧 revision；不能因 checksum 匹配就跳过布局验收。

#### Near-free Parallelism 只能消费不进入 Critical Path 的 Slack

串行 decoding 或每次只执行一个候选分支，在 kernel 已饱和、额外工作必然拉长 step 时最可预测；memory-bound module
与离散 kernel granularity 会留下 compute/resource slack，使少量并行候选的增量工作在特定 shape 下不进入 critical path。
Execution runtime 可以按 module profile、batch/sequence shape、resident weights、SM/HBM 与 kernel variant 估计安全宽度，
只在预计额外工作可被当前 slack 覆盖时 admission，并以实际 step latency 修订 plan。这里 runtime 拥有 overlap 和 resource
admission；第 48 章仍拥有 draft/verify、acceptance 与 committed-token correctness，二者不能因都叫 parallel decoding 而合并。

利用 slack 可降低部分候选生成的边际延迟，却增加 profile drift、resource contention、tail regression 和为探测 slack
支付的无效 compute；“near-free”也不等于 zero-cost。Kernel fusion、并发、MoE routing 或硬件变化都会改变安全宽度，
超出 latency guard 时必须退回串行/更窄并行。`arXiv:2605.30851v1` 的 §3 与 Appendix C 只支持作者对 Dense FFN、
MoE FFN、Attention 和披露硬件的 module-level NFP 分析；Limitations 与 Appendix J 不证明任意 engine、workload 或
production tail SLO 都存在相同免费并行区间。

<!-- source-family:SF-2026-ARXIV-2605-30851 -->

跨节点 fused/megakernel plan 还必须区分 **data movement completion** 与 **全局执行栅栏**。为每次传输等待统一 fence 最容易证明顺序，却会把 NIC、GPU kernel 和 expert compute 串行化；完全删除 fence 又可能让消费者读取尚未可见的数据。更细粒度的执行合同是让 producer 发布带 sequence/epoch 的 completion signal，consumer 只等待其真实依赖，并由 communicator owner 维护跨 rank ordering 与 coordinated abort：

```text
dependency graph + transfer epoch
→ enqueue communication and local compute
→ publish fine-grained completion signal
→ dependent consumer advances
→ group commit or coordinated fallback
```

这种 overlap 用 signal state、wraparound/late-message 处理和更难的 hang diagnosis 换吞吐；它没有把网络语义交给 kernel 自由猜测。通信库、内存可见性或故障恢复不支持精确 signal 时，粗粒度同步仍是正确且可审计的旧分支。

<!-- source-family:SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING -->

MoE 的 collective layout 还与 attention 的 TP/DP、expert 的 TP/EP 和 pipeline 切分共同决定可用 overlap。固定并行组与库 All-to-All 在拓扑稳定时最容易验证；跨节点带宽弱于节点内互连时，可以按隐维度重排 dispatch 为节点间分片移动后节点内 AllGather，将 combine 拆成异步节点间 All-to-All 与节点内 ReduceScatter、top-k 加权组合。这样暴露可独立等待的搬运/归约依赖，再由 joint planner 比较模型 shape、并行度、拓扑和 layer placement，而不是先分别选好 attention 与 expert 计划。[MixServe exact-v1 §III](https://arxiv.org/html/2601.08800v1) 提供这条分解；通信轮数阶数降低不是总工作或端到端延迟保证。

额外 temporary buffers、重排、节点内 gather/reduce 和真实 completion 依赖必须进入计划成本。相同 DP/EP 的“平衡”也不是硬件无关最优点：作者 §IV-C 的 Ascend910B 对照偏好 DP=EP，而 H20 对照偏好 DP<EP；sync/async 消融只支持其局部 overlap。不同 backend 的候选空间和执行路径不能拼成统一因果倍率，有限两/四节点负载也不授生产 SLO。Profile 陈旧、workspace 不足或没有可隐藏的通信时，回退固定库 collective/更保守并行映射；模型 expert routing 的语义仍由第21章拥有，本章仅解释其可执行布局与依赖。
<!-- source-family:SF-2026-ARXIV-2601-08800 -->

#### 从手写 Host Collective 到可验证的 Device-initiated Kernel

host 驱动的 NCCL collective 把同步边界留在 kernel launch 之间，在拓扑固定、overlap 需求有限时最容易审计；把通信下沉进 kernel 后，backend、communication placement、同步范围、issuer granularity 与 chunk size 会共同决定程序是否合法和是否真正隐藏了通信。此时分别调 compute 与 communication 已不再拥有封闭的可实现域，靠通用模型从训练记忆直接生成代码也容易混淆新 API 的内存与同步语义。

一个更强但更昂贵的 execution-plan pipeline 先把这些维度写成显式 directive，并注入 backend API、硬件拓扑和 correctness rules；correctness-first fast path 从静态依赖图生成可编译、可对照 host baseline 的保守 seed，performance slow path 再在带历史测量的有界空间中演化 fusion、stream overlap 与 split put/wait。Compiler/runner 拥有代码生成、编译、正确性判定和测量，Agent 只提出候选，不能因为代码通过编译就提交语义真值。

这种路径减少手工 co-design，却增加搜索预算、judge/测试盲区、测量噪声、工具链版本耦合和错误 kernel 的隔离责任。API 成熟、shape/拓扑稳定或可靠规则已经覆盖时，手工模板与库 collective 仍更可预测。exact-v1 的四组 multi-GPU workload 同时包含训练与推理算子，只支持作者公开环境中的候选生成与延迟结果；不证明 Agent 搜索对任意集群优于专家规则，也不替代训练收敛、故障恢复或 production SLO 验证。第 36 章提供训练 collective 的语义输入，本章拥有从该输入到 executable fused-kernel plan 的验证与 admission。

<!-- source-family:SF-2026-ARXIV-2603-02376 -->

#### 异步工作不必永久绑定固定 Physical Core

传统 GPU execution 把 block/warp 放到 physical SM 后，由硬件在固定资源上推进，适合规则 kernel 与生命周期较短的
同步工作。异步、细粒度且等待关系复杂的执行图会改变这个前提：一个 work unit 在等待依赖或 memory 时仍可能占住
它最初绑定的资源，局部 oversubscription 又难以表达跨 kernel 的资源重配。

Resource-decoupled execution 增加一层 virtual execution-resource identity：program 表达尚未绑定特定 core 的工作与
continuation，runtime 根据 readiness、locality 和可用 physical cores 动态绑定；completion、memory visibility 与
committed output 仍由原 execution plan 管理。

```text
asynchronous work + dependency state
→ virtual execution resource
→ readiness-aware physical-core binding
→ dependency-driven issue and dynamic flow-to-unit mapping
→ completion signal and plan commit
```

这用更灵活的 occupancy 和 latency hiding 换 runtime scheduler、context/state storage、fairness、deadlock diagnosis 与
架构耦合；虚拟资源数量过大也可能制造 metadata 和 contention。规则 GEMM、graph capture 已稳定或 runtime 无法证明
suspend/resume state 时，固定硬件调度仍更容易验证。VDCores 的 exact-v1 结果绑定其四类 LLM inference workload 与
GH200/H100/RTX 6000 Pro 环境；本章只吸收 resource binding 变成 runtime decision 的机制，不外推 headline 吞吐。

<!-- source-family:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING -->

#### 从粗粒度 Offload 到负载观测的 Tensor Placement

按 layer 或 expert 固定切分设备，在 dedicated host、tensor 行为相近且 workload 稳定时仍是最简单、最可预测的
方案。消费级设备和混合 CPU–GPU runtime 改变了这个前提：同一层内不同 tensor 的 GPU 加速收益与传输字节并不
相同，Prefill 与 Decode 的最佳 placement 也可能不同；后台 CPU/GPU 负载、PCIe 竞争和 thermal throttling 还会让
离线最优计划在请求过程中失效。

因此 execution plan 可以把 placement 从粗粒度规则推进为受约束的反馈过程：先按 model、dtype、layout、kernel、
hardware profile 测量每个 tensor 的 CPU/GPU 执行与传输成本，在容量约束下生成 phase-specific placement；再用
pinned host state、异步 copy 与计算重叠执行。Runtime 只观测实际 transfer/compute deviation 并提出新计划；只有
偏差超过 hysteresis、满足 rate limit，且新资源已 preload/校验后，才能在 phase 或 token 边界 commit：

```text
coarse static layer/expert offload
→ profiled per-tensor placement
→ asynchronous transfer / compute overlap
→ observed runtime deviation
→ hysteresis + rate-limited proposal
→ boundary commit or safe fallback
```

这个分支用更高的 profiling、pinned-memory、temporary-buffer、graph rebuild 与 plan-version 成本换取对瞬时负载的
适应。错误 profile、过快重排会把收益还给迁移与控制开销，过慢重排又会长期执行 stale plan；in-flight execution
不得看到半切换地址。第 54 章拥有物理 memory budget，第 56 章拥有 fleet admission/routing；本章只拥有单 runtime
内 tensor placement 的计划身份与安全切换。对于稳定主机、小模型、严格可预测性或遥测不足的 workload，静态
layer placement 仍然更合理。

视觉 MoE 的 offload 还暴露了“输入压缩改变 expert working set”这一特殊分支。固定驻留或只看历史 token 热度在文本
MoE 中容易复算；视觉 token 经压缩后，后续路由访问集合可能更集中，runtime 可以从已压缩表示生成短期 expert-access
lookahead，用它驱动 expert cache 和异步 CPU→GPU prefetch。预测器只拥有 placement hint，真实 router 仍拥有 expert
选择，cache miss 必须回退 host 执行或同步装载，不能改变模型输出语义。

这条分支用较低传输等待换取预测器误差、额外 cache metadata、host 带宽和错误预取污染；收益只在视觉 MoE、给定压缩
策略和 PCIe/内存条件下成立，也没有自动给出 tail-latency SLO。预测命中率或 overlap 不足时，固定热 expert 驻留和
同步 fault-in 仍是可审计 fallback。<!-- source-family:SF-2026-ARXIV-2605-05899 -->

异构 SoC 上，placement 还可以从独立算子成本推进到 **dependency-preserving microbatch critical path**。单独把
每个 operator 放到局部最快 backend，可能因 CPU/GPU/NPU 间同步与统一内存争用拉长整条路径；更完整的 plan
需要先保留 graph dependency，把可并行 microbatches 和 transfer edge 一起调度，再用 trace 修订关键路径：

```text
operator profile + dependency graph
→ bounded microbatch partition
→ heterogeneous placement and transfer plan
→ trace-observed critical path
→ boundary-safe replan or coarse fallback
```

它获得 overlap 机会，却新增 microbatch search、同步、trace 归因和运行时调参成本；局部 profile 也可能在统一
内存压力或 host load 变化后失效。模型小、拓扑稳定或 tuning 成本高于收益时，coarse layer placement 仍更容易
验证。该分支只说明 execution-plan owner 必须看到依赖和真实 trace，不证明某个异构调度器对所有设备最优。

长上下文推理还需要先辨认被优化的“memory”究竟是语义信息，还是设备 RAM/KV。稀疏 Attention、RAG 和压缩上下文虽然保留信息的位置不同，都可能经历准备索引、计算相关性、选取信息、送入生成四段；它们不是四个必须连续执行的统一 API，而是定位瓶颈的分解。只加速最后的模型算子，可能忽略前面的不规则检索与数据搬运。执行计划应逐段测算计算密度、访问模式、执行频率和跨设备 transfer，再决定哪些阶段保留 GPU、哪些才值得放到 FPGA 等异构设备；跨设备复制若吃掉节省，仍应回退同设备路径。作者的 MI210+U55C 与所测稀疏 Attention/RAG/压缩记忆实验只支持这组条件下的端到端收益，A100 异构对照未在同机直接实测，不能外推为所有长上下文服务的最佳放置。

<!-- source-family:SF-2026-ARXIV-2603-29002 -->

#### Backend Choice 必须携带 Previous-backend State

按 shape 为每个 operator 选择局部最快 backend，比整图静态 placement 更灵活；但连续两个局部最优若跨 device 或 framework，会支付 synchronization、tensor conversion 与 context-switch cost。最小的 transition-aware plan 因而把 previous backend 加入决策状态：只有当前算子的局部收益超过有向切换成本，才提交新 backend；否则延续旧 backend。

这条规则介于静态整图与全局序列优化之间。它是 causal greedy policy，成本表必须绑定 phase、exact shape、dtype、device/runtime revision 与测量条件，unsupported operators 继续走静态 fallback。它减少无收益切换，却新增 profile coverage、cost drift 与 classifier regret；新模型 shape 分布变化时还可能比静态策略更慢。稳定单 backend、fused graph 或 framework switch 无法安全实现时，静态 execution plan 仍更合理；只有 integrated runtime 证明转换、dispatcher 与端到端 SLO 后，measurement-backed replay 才能升级为部署结论。

在 FHE 与 MPC 混合执行中，切换成本还由加密表示决定。相邻 FHE kernels 若约定相容 packing，可以避免独立 repack；进入或离开 MPC 时使用紧凑 ciphertext packing，则可减少转换 payload。但最少 ciphertext 或转换次数不是最小端到端时间：expanded packing 若减少后续计算，仍可能值得额外通信。计划必须同时声明输入/输出 layout、CKKS scale 与 modulus level、转换的 fixed-point mapping，并把转换、两侧计算及网络成本共同结算，不能从普通 tensor shape 推出密文边界可自由重排。

Compiler 拥有这份表示和成本计划，Security 继续拥有密钥、明文暴露与参与方威胁模型。数值 round-trip 实测不等于任意输入误差保证，近似非线性也不保持原 Transformer 的精确行为；作者 A100、GPT2/BERT 与 LAN/WAN overlay 的受限结果不能冒充真实跨网生产服务，排除 conversion 的通信表也不能与包含它的 latency 直接混用。packing、数值映射或信任前提不成立时，保留静态加密计划、纯 MPC 或经授权的受信计算路径，而不是让较小 payload 替代安全与质量验收。

<!-- source-family:SF-2026-ARXIV-2604-09975 -->

### Accelerator Readiness 是 Phase × Shape × Offload × Host-control Contract

把整张模型图放到标称 TOPS 更高的 accelerator 上，在 graph 规则、offload coverage 完整、host control 便宜且
Prefill/Decode shape 相近时最简单。LLM 改变了这个前提：Prefill 的大矩阵与 Decode 的小 batch、逐 token
控制可能偏好不同 backend；unsupported operators、tensor/KV conversion、wake/sleep、polling 和 host-device
synchronization 又可能吞掉计算收益。

```text
model graph + phase + shape range
→ supported/offloaded operator coverage
→ backend-specific kernel and memory plan
→ host control + synchronization cost
→ tensor/KV placement and conversion boundary
→ phase-aware backend choice
→ end-to-end correctness, latency, energy and SLO validation
```

因此 NPU/GPU/CPU 的选择不能由单个峰值指标拥有。Prefill 与 Decode 可以选择不同 backend，但切换只有在
tensor/KV identity、layout conversion、handoff completion 和 control latency 都进入 execution plan 后才成立。
单 backend 在切换代价高、offload coverage 不足、模型较小或可预测性优先时继续合理；hybrid plan 用更复杂的
placement、conversion、power-state 和 failure recovery 换取 phase-specific efficiency。

当前公开移动端研究只支持若干 Qualcomm 系统上的 cross-layer 诊断：它没有证明 NPU 普遍优于或劣于其他
backend，也没有提供可复现的完整 PowerBench artifact，部分最佳组合仍是估算而非同一产品合同下的实测。
本章因而只沉淀 phase-aware accelerator contract，不吸收跨设备 headline 百分比。

### 异构 Kernel Placement 先证明依赖，再决定放置

按 Prefill/Decode 选择设备仍是较粗的计划；同一阶段内部也可能包含偏好不同设备的 kernels。进一步拆分时，不能只把每个 kernel 送到局部最快的 GPU：compiler 必须先从可解析的 PTX 访存区间与已知库语义建立保持原顺序的 read-after-write 依赖，再把跨设备边转成 send/receive、event 与等待。跨迭代复用的 KV 副本还需要明确 delta 的传播与消费顺序；它们是执行计划维护的派生副本，不是改变 token 因果语义的授权。高负载吞吐可以尝试重叠计算与传输，低负载关键路径却常需按相加成本判断，不能用一份离线局部最优表覆盖所有队列状态。

这条分支增加图提取、复制、同步与计划切换成本，并受可证明的访问范围限制。间接地址无法解析时留在同 GPU，collective 留在原同构并行组；权重完整复制与显存余量也必须单独验收，不能因为 placement 求解器未建模容量就假定能装下。[Tessera v1](https://arxiv.org/html/2604.10180v1) 的有限异构 GPU、网络与模型配置支持这一依赖驱动设计，不证明所有 CUDA 图、任意地址或服务 SLO 都适用。依赖不透明、复制过贵或容量不足时，固定同构执行继续合理；跨服务阶段的 PD 状态交接仍由[第55章](55-pd-disaggregation.md)负责。

<!-- source-family:SF-2026-ARXIV-2604-10180 -->

## 从 Linear 语义到 GEMM 执行

第16章已经把 MLP projection 写成 GEMM。这里将符号冻结为：

```text
C = alpha * op(A) op(B) + beta * C

op(A) [M,K]
op(B) [K,N]
C     [M,N]
```

Attention 的 Q/K/V/O projections、MLP 的 up/gate/down projections，最终都会产生不同 `M/N/K`、dtype、layout 和 epilogue 的矩阵乘。数学式相同，不代表执行成本相同：大 `M` 的 Training/Prefill、很小 `M` 的 Decode、多个不同 `M_e` 的 MoE experts，会形成不同 kernel search spaces。

### Execution Plan 先拥有 State，再选择 Kernel

序列形式的算子在 Training/Prefill 阶段便于并行，Decode 若每个 token 都从片外重新装载完整历史或递归状态，瓶颈首先是 state traffic，而不是算术单元。状态可放入片上容量时，一个专用分支把 recurrent state 变成长寿命对象，并围绕单 token update dependency 组织 dataflow；每步只搬运新输入和必要输出：

```text
versioned recurrent state layout
→ keep authoritative state on chip
→ ingest one-token inputs
→ execute dependent update stages
→ atomically publish next state and output
```

Executor 拥有 state layout、lifetime 与 commit frontier，kernel 只推进一次合法更新。它减少片外带宽，却受片上容量、固定布局与 operator coverage 限制；短序列、状态过大或模型经常变化时，通用外存路径仍更灵活。`arXiv:2603.05931v1` 只在 §IV-E System Overview、§VI-E Ablation Analysis 与 §VIII Conclusion 所披露的 FPGA、算子和精度上支持这条边界，不证明 GPU 或其他线性 Attention 有相同比例收益。<!-- source-family:SF-2026-ARXIV-2603-05931 -->

手写 recurrent kernel 能利用上述状态生命周期，但每个模型特例都要重新证明序列形式与递归形式等价。若算子满足可推导的 state-space duality，编译器可以从 sequence semantics 生成固定大小的 autoregressive state、初始化和 update program；Build-time verifier 保存变换、数值假设与 fallback，Runtime 只实例化通过验证的 plan：

```text
sequence operator semantics
→ derive equivalent recurrent form
→ lower state / init / update into backend IR
→ differential and numeric validation
→ portable autoregressive execution
```

这不是 Speculative Decoding：没有 proposal/acceptance 分支。正确性责任也不是一个由论文提供的形式化 transformation verifier，而是 build/test contract：记录 sequence→recurrent 改写成立的假设，再把 JAX/XLA lowering 与 reference 做 token-for-token greedy decoding 和数值容差下的 differential validation。收益是减少手写特化并复用后端，代价是 IR 语义、数值漂移、unsupported operator 与 compiler-version lifecycle；duality 不成立或验证 Gate 失败时必须回退原始序列执行。Exact-v1 证据只支持 `arXiv:2603.09555v1` §3 的 compiler-suitability 条件、§4.2–§4.3 的 recurrent state/cache 实现与 §5.2–§5.7 的数值和性能评测；§5.8 之外不证明未覆盖精度、算子族或编译目标。<!-- source-family:SF-2026-ARXIV-2603-09555 -->

### Recurrent Kernel 的全融合与 Context Parallel 可能互相牵制

融合减少 launch 和中间 HBM 往返，在单个 recurrent-state 工作集能够充分占用设备时合理；batch 与 head 数很少、长序列却增加串行依赖时，更大 fused kernel 也可能只让少量 CTA 工作。此时把序列切成 context chunks 可扩大并行度，却须传播边界状态与跨 chunk 校正；这些依赖可能要求在两个 fused kernel 中间保留 preprocessing，而非继续追求“一次全融合”。Execution plan 应共同选择 head/batch occupancy、chunk layout、边界状态、校正与 backward 路径，不能把少 launch 单独当作收益。

若 gate decay 确实让旧状态收缩，一条近似分支可在有限 warm-up 后省掉部分校正；恒一或不收缩的 head 仍须走原校正，数值容差和逐 head 验收不可省略。FlashQLA 的[首发实现快照](https://github.com/QwenLM/FlashQLA/blob/59849a34dc0baeae5f56012f25f3f5726fc3fabc/README.md)与[H200 测例](https://github.com/QwenLM/FlashQLA/blob/59849a34dc0baeae5f56012f25f3f5726fc3fabc/benchmark/benchmark_results_H200.txt)只支持相应 GDN/head/shape 的局部选择；噪声阈下近似不是所有 head 的严格等价，短批也有成熟 kernel 更快的反例。CP/校正不能摊销、gate 条件不符或质量回归时，保留非 CP、完整校正和已验 fusion 路径，而不推端到端服务加速。<!-- source-family:SF-QWEN-FLASHQLA-20260428 -->


固定片上 layout 在矩阵 shape 稳定时最容易达到高复用；但仅让算子换到另一组计算单元，不一定消除尾块 padding。一个 FPGA/AIE 上的替代分支同时开放计算 tile 和存储视图：将固定大小的矩阵乘原子操作包在边界可由指令配置的循环内；片上 memory unit 保存一维双缓冲，再按 tile 索引解释成不同矩阵视图，并按指令承担 operand 或 result 的角色。计算侧 buffer 的 block partition 与宽口 I/O 侧的 cyclic partition 分层，避免同一布局被两个访问模式拉扯。这改变的是预编译硬件允许 runtime 配置的范围，不是每次重新加载 bitstream，也不是把物理布线变成任意可变连接。<!-- source-family:SF-2026-ARXIV-2604-07523 -->

收益来自减少无效 padding 和重复片外搬运，代价是指令解码、地址生成、预布线 stream、双缓冲及联合调度。计算与存储单元的数量、容量和内部连接仍在编译前固定；有效 tile、总 operand/result 容量和依赖顺序必须同时满足。作者在 VCK190、FP32 矩阵及不同长度 BERT 中的比较支持这一条件分支，部分基线使用自建解析模型、单 AIE 用 SystemC 计时，不能外推 GPU、LLM Decode 或生产 SLO。shape 大且稳定、控制开销支配或现有库已消除 padding 时，固定 tile/布局仍合理；搜索器的最优性宣传也不能替代合法 schedule 与实测验证。

投机解码还让同一个模型在少量 draft rows 与一组 verification rows 间交替；固定 tile 形状之外，计算 dataflow 本身也可能成为约束。另一条 FPGA 分支在同一个 8×8 PE、64 MAC 阵列中，令单行矩阵乘使用八条 dot-product lanes，多行矩阵乘使用 output-stationary systolic mode；变化由预编译的控制与 memory indexing 完成，而不是每轮换 bitstream。离线、经原型 profiling 的 mapping flow 再共同选择 tile 数、M/N/K sharding、multicast/reduction 和 producer-consumer pipeline，runtime 只执行合法 recipe；target acceptance 与已提交 token 的语义仍由第48章定义。<!-- source-family:SF-2026-ARXIV-2609-24847 -->

切换模式避免一类 kernel 的闲置，却新增 routing/control、banking 与配置成本；增加 tile 也可能因复制和 reduction 降低有效算术强度。SPECTRA 的证据限于 100 MHz XCVU19P、20 tiles 中14个 accelerator、三组70M～774M draft/target配对与短 prompt 的作者实验；相对固定 systolic 原型，LUT/FF 分别增加约82%/79%，不是“同资源免费适配”。正文仅在 roofline 推导假设32-bit weights，实验计算精度未披露，Jetson 对照来自文献 latency，不能推出同硬件优势或生产 SLO。固定 phase、已有高效库、控制开销不能摊薄时，专用 datapath 与静态映射仍合理；搜索 recipe 也不能绕过数值正确性和完整端到端成本验收。

存储视图还有另一种职责划分：不把计算搬进 memory engine，而让 CPU 保留原有计算，只把张量视图的地址解释移到访存路径。消费者访问一个 alias 地址空间，硬件按配置的 shape、stride 和索引规则拆分请求，从原始存储分散读取，再聚合为消费者需要的 cache line；这样可以避免先物化一份转置或展开后的中间张量。配置 owner 必须共同冻结 alias、物理来源与消费者的布局约定，这不是零成本的软件 transpose，也不是 PIM 计算。<!-- source-family:SF-2026-ARXIV-2604-13319 -->

减少中间副本并不等于减少 DDR 流量：一条 cache line 的 useful bytes 很少时，分散请求仍可能触发完整 burst，地址解码、配置和一致性管理也有成本。卷积中的重复取数、访问方式破坏 SIMD，以及矩阵乘计算掩盖布局转换耗时，都可能让更小的 working set 没有延迟收益。该机制的证据限于 Kria KR260、Cortex-A53、300 MHz FPGA 与 DDR4 上的作者张量算子比较，不能推到 GPU、LLM Serving 或生产 SLO；当碎片化访存更贵、消费者要求连续布局或配置成本无法摊薄时，先物化布局、CPU 变换与成熟连续访问库仍是合理分支。

### Architecture Search 需要 Typed System IR，而不是自由改写配置

手工维护 compute graph、parallel plan 与 hardware placement，在模型和拓扑稳定时最透明；当设计空间同时包含算子分解、并行方式、expert placement 与硬件层级时，分别修改配置会让一次收益无法归因，也无法确认两个候选是否保持相同模型语义。更强的 execution-plan builder 先把 compute graph、hardware graph、placement 与 transformation contract 放进同一个 typed IR，再让搜索器只提交满足前置条件的变换：

```text
typed compute graph + tensor semantics
+ hardware graph + capacity / topology
+ explicit placement
→ semantics-preserving transformation proposal
→ analytical / discrete-event simulation
→ compile, capacity and numerical verification
→ measured replay
→ admit | reject | fallback
```

搜索 Agent 只拥有 candidate proposal；IR/type checker 与 compiler 拥有语义和可实现性判定，simulator 只提供性能估计，真实 runtime measurement 才能支持部署选择。这个分层扩大了 architecture search 的可审计范围，却新增 graph 建模、变换证明、cost-model calibration 与大规模模拟成本；遗漏 KV append、speculation、multimodal path 或真实负载不均衡时，模拟 Pareto frontier 可能合法但错误。稳定小规模部署、模型无法完整表达或 simulation 未校准时，应回退人工计划与真实硬件基线。

RoofLang 的 exact-v1 §2 支持 typed compute/hardware/placement graph、受约束 transformation 与 simulation 的实现，§3 的百分比只来自作者模拟的代表性模型和硬件；§5 明确披露理想 MoE load balance、遗漏运行路径及大模型模拟的时间/内存压力。因此这里吸收 architecture artifact 和 authority boundary，不把模拟收益写成 runtime speedup。<!-- source-family:SF-2026-ARXIV-2609-12551 -->

即使数学与状态形式已确定，稀疏 Attention 的工作量仍可能随 head 改变。按 head 数静态切分在 token budget 均匀时控制成本最低；S-HPLB 先用 calibration 为不同 head 冻结差异化 token budget，这一步已经选择了 approximation/accuracy trade-off，再以这些预算的估计工作量做 greedy head-to-device assignment，后一步只负责 load balance，不能在运行时悄悄改写预算。收益来自减少 straggler，但代价是 calibration artifact、预算漂移和跨设备通信；负载均匀时静态并行更简单，而分布漂移、互联退化时需要重新校准或回退——这是系统设计推论，不是论文单独证明的 failure guarantee。`arXiv:2603.10353v1` 只在 §3.2–§3.3 和 §5.1–§5.4 所披露的模型、稀疏配置与实验环境中支持预算和放置机制。<!-- source-family:SF-2026-ARXIV-2603-10353 -->

同一条原则也适用于跨 NUMA GPU 的不规则算子，但此时“工作量相等”仍不等于“数据代价相等”。若多个 task 对 operand 的共享范围不同，把它们只按 FLOPs 均分会让全局共享、局部共享和私有数据在互联上反复迁移；execution plan 应先根据共享域与拓扑估算 data movement，再把 task 放到能复用 operand 的 GPU，并把调度决策与 operand generation、layout 和拓扑版本共同冻结。这样用更复杂的全局放置换取较少的远端读和更高 locality，却会增加 profiling、调度开销与拓扑漂移风险；矩阵规则、共享模式均匀或单设备已足够时，静态切分仍更稳妥。`arXiv:2607.28824v1` 只用作者构造的内存访问 trace 与 cycle-level simulation 支持该 NUMA placement 机制，未在真实多 GPU 系统上证明端到端收益、容错行为或生产调度成本。

<!-- source-family:SF-2026-ARXIV-2607-28824 -->

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

### Irregular Compute 要先归一为 GEMM + Epilogue Contract

为每个 fused operator 手写 kernel，在 shape 稳定、目标硬件单一时可获得最直接的控制；attention、state-space、quantized block 或自定义 reduction 增多后，kernel surface 会随组合爆炸。一个中间抽象是把可表达部分归一为 `GEMM + versioned epilogue`：compiler 拥有 tile、layout 与 epilogue lowering，runtime 只提交已验证的 shape/precision instance，custom kernel 保留给无法合法表达的 control flow。

统一表示扩大 autotuning 与 fusion 复用，却可能为特殊算子引入中间状态、冗余计算或寄存器压力；抽象未覆盖的同步和 sparse access 不能伪装成普通 epilogue。固定热点或抽象开销超过维护收益时，专用 kernel 仍是合理旧路径。`arXiv:2605.19269v1` 的 §3 与 §4 只支持其 GEMM-epilogue representation、kernel 与端到端实验，§5 不证明跨 GPU、跨 operator 或任意 dynamic shape 的 portability。

<!-- source-family:SF-2026-ARXIV-2605-19269 -->

Execution plan也可能消费一个先经质量恢复的更小稠密模型，而不只是把原图编译得更快。只删整层或只删head/neuron，各自保持一种结构粒度，容易控制；混合两种删除时，应先按当前待删层的参数数匹配width分支的删除量，再比较或选择下一结构，不能把不同预算的候选当作同一选择题。若用短恢复后的质量proxy评分，该更新可以只服务于候选比较，选中后保留未短更新的剪枝模型，最后再做完整恢复；结构搜索与恢复预算因此是两个独立成本，而非无损图优化。<!-- source-family:SF-2026-ARXIV-2602-06127 -->

混合搜索空间有效，也不证明复杂选择器必要。[MoP的受限对照](https://arxiv.org/html/2602.06127v1)中，等参数深宽混合优于同pipeline的单轴路径，而随机路径与PPL等proxy相近，后续实验实际使用随机选择。新增证据支持先检验结构互补，再决定是否支付选择器成本；三条随机路径不是稳健性定理，跨论文baseline预算也不完全一致。删除后仍有质量损失，恢复数据、shape与目标硬件的墙钟必须另验；单卡短prompt、batch1的局部延迟不能外推服务SLO。恢复不足、搜索或布局成本抵消收益时，固定单轴剪枝和未压缩模型仍应保留，不能用参数减少替代质量与执行验收。

缩小宽度也不必只删除坐标：将相似参数行聚成簇、替换为簇均值，再合并重复输出并适配下一层，可以得到另一种更小稠密 artifact。参数空间中，这是投影到“同簇行相等”的子空间，而不是把被删行置零的坐标投影；聚类、下一层适配、normalization reset 与恢复预算都需绑定最终 artifact。[受限投影分析](https://arxiv.org/html/2602.18116v1#S2.SS3)以比剪枝多一个 rank 的构造给更小参数偏差，并在参数-Lipschitz假设下得到更紧的损失偏差上界，不证明相同 rank 的实际任务损失总更小，更不保证改写非线性网络后严格保留原函数。匹配保留规模的局部实验仍有学习率/训练状态依赖和小 LLaMA 反例，投影误差也不是 runtime 收益。聚类搜索、重置、恢复训练、真实布局和 kernel 验收继续计费；簇结构不清、质量失败或适配成本不能摊销时，坐标剪枝、原深宽删除搜索与未压缩稠密模型仍是合理分支。<!-- source-family:SF-2026-ARXIV-2602-18116 -->

### 两种稀疏性必须共享地址合同，却不必共享 Kernel

非结构化小权重剪枝能直接表达“哪些参数不重要”，却不一定生成硬件可消费的稀疏布局。一个中间演进是联合优化权重与
soft mask，用局部二阶敏感度定义保留目标，再通过 progressive annealing 把连续 mask 收敛到明确的 `2:4` pattern。
训练侧拥有 mask 演化和最终权重，compiler 只接收冻结的结构化 artifact；runtime 还必须证明目标设备确实选择了对应
sparse kernel，否则参数稀疏只是文件属性而不是执行收益。

逐步硬化减少一次性剪枝的质量冲击，却增加 Hessian 近似误差、annealing schedule、重训练成本和 pattern lock-in。
作者实验支持其模型与稀疏设置下的质量恢复，不证明所有 layer 都应共享敏感度或任意硬件都能提速。若目标 backend
没有成熟 `2:4` 路径、恢复失败或 shape 太小，稠密权重与稠密 kernel 仍是正确 fallback；训练过程的 mask/optimizer
状态归第 28 章，本章只拥有可执行 artifact 与 kernel admission。<!-- source-family:SF-2026-ARXIV-2605-06402 -->

选择可执行稀疏 pattern 之前，局部剪枝目标本身也需要明确：保持 layer output 的重构损失与基于校准样本梯度的 empirical-Fisher 损失，不一定给出相同的重要性排序。一种离线分支先分别按全零权重下的损失归一化，再加权混合两者；在行或 block 近似中，重构项提供共享的输入二阶矩基底，样本梯度项提供低秩修正，因而可用 Woodbury 更新复用共享逆矩阵。这里精确的是所选近似矩阵的求逆关系，不是全模型 Hessian 或全局最优剪枝；empirical Fisher 的近似还依赖参考点梯度等条件，混合权重改变或共享基底不可逆时，不能照搬同一求逆路径。<!-- source-family:SF-2026-ARXIV-2604-13287 -->

这个分支把 calibration loss、归一化基准、混合权重和 block 划分纳入稀疏 artifact 的身份，用额外梯度采集、矩阵状态与超参数选择换取更丰富的敏感度信号。作者在 LLM attention 与其他受测层上的目标选择并不相同，部分 2:4 结果也退步，因此不能把混合目标写成普遍优于单目标，更不能由离线质量推出 runtime 加速。校准证据不足、低秩近似不稳或质量 Gate 失败时，应回退单一重构目标、更保守的剪枝或稠密权重；冻结 artifact 后的布局与 kernel admission 仍独立验收。

校准输入的生成时钟也会改变离线 importance：AR 中长期稳定的 prefix sink 经验，不能直接迁移到各去噪步输入不同的 diffusion model。一条[noise/time-conditioned 剪枝分支](https://arxiv.org/html/2602.17664v1)在多组加噪校准时刻汇总各层/各 head 的 attention mass，得到跨步平均 soft-sink score，再以其补数重权 activation rows，用于原 importance norm 或重构二阶矩；冻结后仍交付权重剪枝 artifact，不是在请求期间删除 token。平均 soft-sinkness 不是按 temporal variance 选择位置，attention mass 也不是 semantic importance 真值；它改变的是校准统计，不能由此宣称所有 sink 无用。相同 WikiText-2 的128条、长度2048校准及既有 Wanda/SparseGPT 协议提供有限对照，但 LLaDA1.5 的75% SparseGPT平均质量仍反退，低稀疏度也有退步。多时刻前向与 attention map 采集增加离线成本，硬件、precision、完整 runtime 和 timestep 采样细数未披露；稀疏率不替目标 kernel 或服务 SLO 验收。noise schedule、输入域或统计支持改变时重新校准，质量失败则回退原校准/更保守剪枝或稠密权重，不能把生成范式差异写成普遍压缩保证。<!-- source-family:SF-2026-ARXIV-2602-17664 -->

局部结构惩罚还要先决定参数尺度代表什么。对正齐次激活，放大一个神经元的输入行、相应缩小输出列，可以保持模型函数不变，却改变只罚输出列的代价；不能把更小的列范数直接解释为更不重要。一个受限分支先把输入行连同bias归一，再对输出列施加组惩罚，以消除这项尺度自由度，并在相邻两层、其余网络冻结的子问题中筛选神经元。其全局最优与特定joint惩罚的等价，只说明目标的最优函数关系，不等于两种有限优化过程会走同一轨迹；实验中的incoming-row Group Lasso也不是该等价定理的同目标对照。

实践中只在每块开始归一一次、再进行梯度与proximal更新，和每步重新投影的约束算法不同；受限对照中频繁归一反而失稳，删除后的恢复还依赖额外fine-tuning。归一规则、惩罚窗口、物理删行列与恢复预算因此都属于剪枝artifact的身份，参数/FLOPs减少仍不证明kernel或请求提速。现有ReLU/OPT1.3B证据在激进预算也有质量反退，不能搬到不满足正齐次性的GELU或gated FFN；条件或质量门未通过时，保守剪枝、独立目标对照和稠密权重仍应保留。 [必要机制与边界](https://arxiv.org/html/2609.21126v1) <!-- source-family:SF-2026-ARXIV-2609-21126 -->

剪枝 artifact 还需把 importance score 与 protected set 分开记录：前者决定可剪位置的排序，后者规定哪些位置不参与剪除。使用 activation 来保护一组权重，并不等于把 activation-L2 当作全部权重的剪枝评分；两者交换会改变实际算法。作者对照中，LP-held score 加 activation protected set 的 perplexity 仍为 10.71，而 activation-L2 score 为 26.84，支持的是这个角色区分，不是任意 activation 保护都可靠。<!-- source-family:SF-2026-ARXIV-2604-23475 -->

保护集引入额外校准统计、保留预算和分布依赖，应与 score、mask、校准数据及模型版本共同冻结；域漂移后既有保护集可能不再代表关键位置。该证据属于作者离线剪枝配方，不能由 perplexity 推出稀疏 kernel 加速；保护收益不稳或保留预算过大时，回退原 score、更保守 mask 或稠密执行，再分别验收质量与 runtime。

只做 static weight pruning，layout 稳定、容易提前编译，但不会利用 input-dependent activation sparsity；只做 dynamic
activation pruning，能随请求选择，却仍要读取 dense weights，且索引与分支开销可能吞掉收益。当 small-batch Decode
进入 memory-bound 区域，两者可以组合为同一 column-addressable sparse format：静态 mask 决定哪些 weight blocks
存在，动态 mask 决定本轮哪些 activation columns 参与，再由共同地址合同定位有效数据。

```text
static weight sparsity
→ input-dependent activation sparsity
→ shared addressable sparse representation
→ Decode: sparse matrix-vector path
→ Prefill: Tensor-Core sparse matrix-matrix path
```

动态 activation mask 的评分也不必只看输入幅值：可用当前 token 的 activation 与相应 weight-column norm 的幂共同决定保留位置，再在离线校准中选择逐层指数与 score quantile 阈值。阈值冻结并不等于 support 冻结；每个 token 的输入仍改变实际参与的 columns，因而校准 artifact 拥有评分与阈值，runtime 拥有本轮 support、索引生成及稀疏执行。这个 weight/activation 联合选择用额外 block-MSE 搜索、校准样本和动态 metadata 换取更有针对性的跳算，不能把纯 weight 重要性或 activation 幅值直接当成同一算法。作者 H20、短输入/200-token 输出的局部结果从 153.5 到 179.9 tokens/s，远小于所报约 46% FLOPs 降幅；batch/precision/SLO 未充分披露，也不覆盖大 batch 的索引摊销。质量漂移、support 太密或动态开销抵消收益时，仍应回退静态 mask、structured-sparse 或 dense 路径，分别验收质量与净请求成本。<!-- source-family:SF-2026-ARXIV-2602-14452 -->

共享 representation 不意味着共享实现。Decode 的小 `M` 更关心权重字节和 metadata decoding；Prefill 的大 `M`
更需要 tile reuse 与 Tensor Core utilization。为了同时服务两阶段，runtime 往往要维护不同 kernel、packing rule 与
fallback。获得更高有效稀疏率的代价是 bespoke layout、索引解码、质量校准、phase dispatch 和 portability；batch 增大、
稀疏度不足、量化/硬件组合未验证时，dense 或 structured-sparse GEMM 仍可能更快、更容易证明正确。本节拥有的是
execution-plan 分支，不把特定作者在 A10G/L4/L40S、LLaMA-2-7B 与 matched-perplexity workload 上的结果外推为通用加速。

若 weights 与 activations 同时稀疏，单独优化压缩率或跳零率仍可能让 SIMD lanes 消耗在格式解码、索引交汇和冲突累加上。双稀疏 SpMspV 的 execution identity 因而还要包含双方格式、SIMT decoder、operand-sharing domain 与 shared accumulation protocol；格式不是离线存储细节，而是决定 kernel control flow 的一部分。联合设计可以减少无效读取和重复累加，却用更复杂的 metadata、分支与 shape-specific tuning换取收益；稀疏度不足、索引分布不规则或 batch 已适合 dense GEMM 时，应回退 dense/structured-sparse kernel。`arXiv:2608.01536v1` 只以作者 kernel、模拟或微基准支持该机制，不证明生产端到端延迟、跨硬件 portability 或模型质量保持。

<!-- source-family:SF-2026-ARXIV-2608-01536 -->

稀疏索引控制流也改变了工作分区的成本模型。dense tensor 常按坐标范围或元素数平分，coiteration 却可能为寻找交集、跳过子树与匹配有效坐标支付不同访问量；相同坐标宽度不等于相同工作。一个条件分支用满足单调与层次一致性条件的累计访问成本选择分区边界，outer intersection 先发现有效坐标，再把过滤后的序列 remap/prefix 成可分区对象。partition identity 因而包含实际 coiteration 算法、格式与访问成本函数，不可把 union 的坐标划分直接充作 intersection 的等负载计划。<!-- source-family:SF-2026-ARXIV-2604-17198 -->

成本界约束的是所选函数，不是 wall-clock：发现/重映射、partition、输出 assembly、scatter 排序与 reduction 都可能返还收益。原文部分 SpGEMM 比 cuSPARSE 更慢，也未给 LLM 端到端证据；低 skew、稳定格式或分区难摊销时，静态分区、vendor kernel 与 dense 路径仍合理。稀疏计划须在正确坐标归属之外验证总执行时间及 metadata 成本，不能从数学边界直接签发后端选型或服务 SLO。<!-- source-family:SF-2026-ARXIV-2604-17198 -->

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

这个边界还会向上游传播到模型压缩：按重要性直接分配每层保留维度，容易得到参数更少、但落在低效 tile 或 kernel 路径上的不规则矩阵。统一向上取整最简单，却会消耗额外参数预算，也未必选中目标设备上更快的形状。另一条分支是先为各层生成满足硬件对齐条件的候选压缩维度，实测它们的执行成本，再在全局参数预算下联合选择每层形状。这样，压缩器拥有质量与预算约束，执行计划提供设备和 workload 相关的成本；两者不能各自局部最优后再假定收益可直接相加。

联合选择增加 profiling、离散搜索和跨设备重新校准的成本，也可能为了速度分配较不利的压缩比例。离散化后的预算搜索不等于连续空间的全局最优，更不保证质量不变；验收必须同时报告压缩质量与实际执行时间。现有 GAC v1 的受限实验支持 FP16、batch 1、长度 1,024 的 Prefill 形状选择，不证明 Decode、高并发服务或优化引擎下仍有相同收益。形状差异影响小、预算宽松或 profiling 无法摊销时，固定对齐和原有压缩方案仍更合理。<!-- source-family:SF-2026-ARXIV-2604-09595 -->

更细的 kernel 选择还会遇到离散 wave 边界：增大 tile 减少 block 数量，却可能改变资源占用与最后一波的空闲；同一 macro tile 下的 micro loop 又影响寄存器与指令流水。一条近似路线按 wave 分桶拟合宏观成本，同时用少量 loop anchor 校准微观残差，再在共同的资源可行域内选择组合。两层表便于减少搜索，但不是两个相互独立的最优问题；分桶、anchor、设备、精度、实现版本与 shape 范围都属于成本模型身份，切换 GPU 或 kernel 后需要重新校准。

代价从逐 shape 搜索移到离线 profiling 和近似误差管理，只有复用足够多次才能摊销。[WaveTune v1](https://arxiv.org/html/2604.10187v1) 在五种 GPU 分别校准，并借用 MHA/单组代理估计部分变体；这些映射与区间外外推都不是普遍保证，Step 在 MI355X 的退步也不能被平均收益抹掉。其 SGLang、Qwen3-30B-A3B、单 GPU、batch 4 的 Prefill 结果不覆盖 Decode、高并发或生产 SLO。近似不准、shape 很少或 profiling 难以摊销时，实际测量、库 heuristic 与固定实现仍是有效选择，而不是被新成本模型淘汰。

<!-- source-family:SF-2026-ARXIV-2604-10187 -->

### 硬件行为代理可以选 Kernel，但不认证执行

Vendor heuristic 和实测 autotuning 在候选不多、平台固定时合理；问题是候选变大或每个新 shape 都测量过贵。一个不用执行候选的分支，是从 problem、kernel 配置与硬件常量推导它将诱发的 wave/tail、cache working-set、occupancy 和 pipeline 开销，再学习候选排序，而不是让模型从 raw tile knobs 猜物理后果。这里输出只是在经过静态合法性筛选的有限 catalog 中提出选择，实际可执行性仍须验收，不是绝对运行时间或开放候选空间的最优性；部署免测也不等于训练／profiling 免费。

[Hardware-Aware CUTLASS v1 §3–5](https://arxiv.org/html/2609.35587v1)还要求把同 base shape 的 layouts 共同留出，区分训练 shortlist-best 与近全量 oracle，并将选择 regret、实际 execution coverage 一起验收。特征 schema、硬件常量、dtype／fusion 和 catalog 改变时，需要绑定 revision 与目标域测量；success-only speedup 不能掩盖所选 kernel 未成功编译/执行的请求，迁移与 fusion 也并非总胜出。离线测量、合法性过滤和模型维护仍有成本，缺覆盖、漂移或预测退步时回 vendor heuristic／有 provenance 的实测 autotune，不授 learned selector 跨精度无条件选择权。

<!-- source-family:SF-2026-ARXIV-2609-35587 -->

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

异步流水还受计算侧存储生命周期限制，不能只计算 shared-memory stages。以某个 Blackwell D128 Attention
布局为例，两组各128列的 score/P 复用区与两组各128列的 FP32 output 已占满512列 TMEM。Score 转成
probability 后，该区域仍由后续 PV 消费；最后一个消费者结束前，下一轮 QK 没有合法的新写入区。
加 barrier 可以保证顺序，却不能凭空增加容量。Execution plan 必须共同安排 score、P、output 的空间与
最后使用时刻，再判断双缓冲是否真的允许 overlap，而非把 SMEM 节省直接折算成并行度。

这个布局例子也提醒我们：同一论文中的 forward kernel 与训练路径未必使用同一精度。
[Direct-P 的精确版本](https://arxiv.org/html/2609.04105v1) 给出了低精度概率表示的前向方案，但其受测
MXFP4 P/V 长训练路径发散，保留的训练路线使用 FP8 P/V，且仍有 validation-loss 差距。因此，前向内核
变快不能自动支持低精度训练收敛；回退精度、数据布局转换及端到端质量都必须分别验收。上述 TMEM 数量
只描述该 D128 布局，不外推到其他 head dimension 或全部 Blackwell GPU。

### 跨 Block 共享先改变协作范围，再判断是否值得

TMA 解决怎样搬运，另一条正交问题是搬入后的数据能由谁保存和复用。单个 CTA（thread block）把一行数据保留在自己的 shared memory 中，局部同步和生命周期最简单；但某些算子需要先求整行统计量，再多次遍历原数据。行宽超过一个 CTA 的保留能力时，全局内存重读仍是正确而通用的基线，只是开始重复支付数据移动成本。

支持 thread block cluster 的硬件提供了一个中间协作范围：多个 CTA 各自保存不相交的 bulk slice，用 distributed shared memory（DSMEM）交换少量 reduction partials，得到整行统计量后，各 CTA 继续本地读取自己的 slice。这里扩展的是协作容量，而不是得到一块无成本、物理统一的缓存；不应把每次 bulk read 都改成 remote read。

这条路径把原来的“重读整行”换成“局部保留 + 紧凑统计量复制 + cluster 同步”。在向每个 peer 推送 partials 的具体实现中，远端复制量随 CTA 数 P 按 P(P−1) 增长；同一轮的 scratch 只有在 peer 已消费完毕后才能复用，owner 也不能提前退出。更大的 cluster 虽能缩小每个 CTA 的 slice，却可能增加同步、资源占用和调度波次。Kernel plan 因而要共同决定 slice ownership、统计量布局、可见性、生命周期与资源可行性，而不只是打开硬件功能。

收益判断应先比较同 shape 的非 cluster 路径：可消除的重复读取时间，是否大于新增的控制、局部 replay、未被隐藏的 staging 与远端统计量写入成本。已有基线可能命中 cache，也可能已经采用 CTA-local staging，不能一律按峰值 HBM 带宽估算收益。匹配资源布局的 control microbenchmark 可以帮助估计代价，但成本模型仍只是筛选器，不能替代 correctness、实际 cluster 配置搜索和上层 runtime 测量。

因此它与单 CTA tiling、fusion、TMA 是有条件组合，不是线性替代。小行宽、无需重读、统计量不紧凑或资源竞争强时，旧路径仍可能更快；DRAM bytes 下降也不保证同比例延迟收益。现有受限算子实验只能支持这种选择边界，不能直接升级为训练收敛、完整推理吞吐或生产 SLO 的保证。

<!-- source-family:SF-2026-ARXIV-2609-01864 -->

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

Router 已经确定各 expert 的 token 后，同一个 compiled grouped-GEMM binary 仍可能需要不同执行配置。Batch histogram 不改变 expert placement 或路由，只用于选择 CTA grid、tile 与 wave 配置，使小 expert batch 的 occupancy 和 tail tiles 不必沿用大 batch 的计划；配置选择与模型选择是两个 owner。<!-- source-family:SF-2026-ARXIV-2604-26039 -->

Histogram、profile 和配置调度增加开销，batch 分布变化会使旧计划失效。作者 H200、vLLM0.9 eager、串行请求/full restart 对照不证明并发 SLO；profile 不可靠、小 shape 选择成本超收益或新硬件未验时，应保留固定配置/通用 kernel，并把 dispatch、GEMM 和端到端质量一起核。

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


#### Expert Placement 必须跟随热度演化

把 expert 静态放在 GPU 或 PIM 上，在 token-to-expert 分布稳定时可提前编译并减少迁移；MoE 服务的 expert 热度随任务和层变化后，会形成热点与冷门路径，静态 placement 可能让执行位置与真实负载错配。动态分支把 recent routing histogram、迁移成本和位置容量作为 placement state，由调度器决定 expert 在何处执行，router 仍只决定 token 路由。

动态放置用监控和迁移换更低的热点等待，却新增分布滞后、thrashing、PIM/GPU 数值差异和恢复复杂度。负载稳定、迁移昂贵或观测窗口不足时，静态 placement 仍是正确回退。`arXiv:2605.11277v1` 的 §3–§7 只证明受测 PIM、MoE 与 trace 下的设计，不允许把作者加速数字外推到其他硬件、精度或并发。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11277 -->

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

### 调优结果也是带执行条件的可复用资产

比较过候选 kernel，并不意味着得到的 winner 可以脱离测量路径复用。只计 device time，在各方案 host 开销近似相同、或摊销后的差异不足以改变排序时是合理基线；eager 执行若包含不同的 dispatch、参数准备与 launch 成本，device 更快的方案却可能整体更慢。CUDA Graph 又可能改变这种排序：测量对象应是 captured replay，而不是用重复 eager 调用代替。因此，缓存的不只是“这个 shape 选哪个 kernel”，还包括测量策略与执行环境：GPU、软件/编译版本、cache schema 和显式策略共同限定环境身份，operation key 则区分 runner、shape bucket 以及 layout、量化等影响语义或执行的额外参数。默认兼容策略也不能被悄悄解释成新策略。

持久化 tactic 可以让后续进程少做重复测量，但完整文件不等于结果仍然可用。临时文件到原子 rename 可防止半写入被读取，却不能防止重复调优或最后写入者覆盖；恢复时仍需检查当前 runner 的可用性。若 runner 提供 validation hook，可以拒绝失效候选；没有 hook 时仍依赖原有信任条件，不能声称每个缓存命中都经过数值验证。分布式执行还新增一致性问题：各 rank 独立测量产生不同 winner，可能令依赖共同 collective plan 的路径失配。在同构 rank、共享存储和框架 barrier 的条件下，等待发布后清除本地选择并重载同一结果可恢复一致性；这不证明该结果对所有 rank、尾延迟或其他 workload 最优。

因此调优资产的复用需要同时满足执行身份、有效性与参与者一致性，而不是简单增加 profiling 次数。它用启动测量、存储、失效管理和同步换取重复运行收益；shape 多变、复用少、环境不匹配或无法协调 rank 时，保守固定 tactic 与重新测量仍是适当回退。这一分支承接上面的真实 workload 比较，下一节再讨论 collective 本身如何减少同步成本；两者分别拥有 tactic 选择与执行协议，不应混为同一种加速。

<!-- source-family:SF-2026-FLASHINFER-AUTOTUNER-V2 -->

### 低 Batch Decode：当 All-Reduce Barrier 成为执行瓶颈

在较大 batch 中，Tensor Parallel collective 的固定同步成本可能被 GEMM 覆盖；常规 oneshot/twoshot All-Reduce 和 communication-compute overlap 因此是合理基线。低 batch、低 TPOT Decode 把单步计算压得很短，payload 也变小，此时 barrier 而不是 bytes 本身可能成为主成本，继续增加 overlap 已没有足够计算可藏。

一种实验性分支把 collective 从“所有 rank 到齐后统一推进”改成带 generation 的 speculate/verify/commit protocol：dual buffers 消除上一轮与下一轮的写读冲突，switch-assisted redundant pull 减少传输，而 speculative fetch 先读取预期 buffer，再通过归约后的 validation flag 判断是否可提交；预测错误必须在 collective result 对上层可见前重试。

```text
buffer generation + expected producer progress
→ speculative fetch
→ reduced validation flag
→ valid: commit collective result
→ invalid: retry from authoritative generation
```

同步没有消失，而是从全量 readiness barrier 迁移到 buffer generation、memory ordering、validation 和 retry。负载不均会提高误判与重试；额外 buffers 增加 HBM 占用；switch reduction 与 Megakernel integration 也限制了 portability。作者 headline 绑定单节点 8×H200、NVSwitch、TP=8、FP8、ISL=1000、OSL=1000 的端到端配置，16K 只属于输入长度 sensitivity；不能把延迟和吞吐数字外推到跨节点 fabric、较大 batch 或其他 runtime。不支持该 commit protocol 时，传统 collective 仍是更稳健的分支；TP algebra 与 collective 语义回指第 36、37 章，本章只拥有 inference execution commit。

Switch offload 还可以从“GPU 发起、交换芯片协助归约”推进为“交换芯片拥有 collective schedule”。前者复用 accelerator load/store 语义，部署边界较小，但归约结果可能先返回发起 GPU 再广播，并且难以承载不可分解为既有 memory semantic 的算子。Switch-centric controller 若能直接访问共享地址空间，可以由网络侧发起 load/reduce/writeback，消除冗余回程，并把 quantize–reduce–dequantize 之类的数据面变换纳入 collective plan。

控制权下沉并没有免费消除同步：participant set、buffer generation、completion、数值格式与 fallback 必须共同版本化，交换芯片也成为新的容量、可编程性和故障域。小消息 Decode 可能受益于更低 launch/同步开销，大消息 Prefill 更依赖带宽；传统 NCCL/NVLS 在通用部署、故障隔离或算子不适合网络内执行时仍成立。`arXiv:2603.28239v1` 的证据只覆盖 §3、§4.5 与 §6 的 FPGA prototype、simulator、8-GPU LLaMA-2 配置及所披露量化，不证明生产交换芯片、多租户、跨节点或其他精度的收益。<!-- source-family:SF-2026-ARXIV-2603-28239 -->

## FlashAttention 在这里的位置

FlashAttention 不只是“更快的 attention”。它的核心思想是 IO-aware：通过 tiling 把 Q/K/V 的块搬到更快的 SRAM 中计算，减少 HBM 读写。

这正好对应 GPU memory hierarchy：HBM 容量大、带宽高，但相比 SRAM 仍然慢；如果 attention 把巨大的 score matrix 写回 HBM，就会被 memory IO 限制。

FlashAttention-2 进一步优化并行划分和 work partitioning；FlashAttention-3 则面向 Hopper 等新硬件利用异步数据搬运、WGMMA/TMA 和低精度能力。它们说明：kernel 优化不是只改数学公式，而是在适配硬件的 memory hierarchy 和执行单元。

全序列或窗口内 attention 可以把片段状态写为 `(m, S, W)`：最大值、相对该最大值的指数和、以及加权 value 和。各 block 独立归约后，通过解除归一、合并 sum/max、再重归一（un-sum-renorm）组合状态；实数运算下这一合并构成 monoid，可让所有 query 的 block 状态通过 parallel scan 组织。Monoid 不提供移除旧项的减法逆元；它改变的是执行依赖与中间状态复用，不把完整 attention 的总计算量变成线性，也不保证浮点重排后的 bitwise equality。<!-- source-family:SF-2026-ARXIV-2604-23798 -->

Scan 需要额外 workspace、状态读写与数值稳定处理，短窗口或小 shape 下这些代价可能超过并行收益；窗口、精度与状态布局应作为 kernel admission 的条件。作者受限窗口实验不能推出任意序列、设备或精度都更快；收益不成立或数值检查失败时，保留普通滑动窗口/FlashAttention 路径。

这个 IO-aware 原则在 tile-based accelerator 上会出现另一条分支。每个 tile 独立做 FlashAttention，最容易保持 head 隔离、无需 tile 间同步，但可复用的块仍受单 tile scratchpad 限制；若多个 tiles 协作保存更大的 attention block，HBM 往返可减少，代价是 Q/K/V multicast、Softmax row-max/sum reduction 和 tile 间同步进入关键路径。只有 NoC fabric 真能以低成本提供这些 collective，且每 tile 的矩阵切片仍足够大时，“以片上通信换片外 IO”才可能获益；软件多跳复制可能比原独立 tile 路径更慢。<!-- source-family:SF-2026-ARXIV-2604-02110 -->

Execution planner 因而应先按 MHA/GQA/MLA 的 score shape、序列长度、tile SRAM、matrix occupancy 与 fabric 能力选择 block/group，再决定异步 overlap；不能单调增大 group 来追求最少 HBM bytes。短序列过度分组会使每 tile 工作切片过小、矩阵单元闲置，跨 die Expert Parallel 还可能让通信重新成为端到端瓶颈。当前证据来自作者用 RTL 校准的模拟 tile/wafer-scale 系统和指定模型、精度、batch、拓扑的对照，不是商品芯片或生产尾延迟实测；没有 fabric collective、shape 太短或片上争用不可控时，独立 tile / GPU FlashAttention 仍是正确分支。<!-- source-family:SF-2026-ARXIV-2604-02110 -->

降低片外 IO 后，继续融合不一定继续提速。对分层 tile accelerator，应分别计算 shim/片外、共享片上 memory 和 compute-tile local memory 的流量与 operational intensity，再对照指令组合实际可达的 compute ceiling，而不只用硬件峰值画一条 roofline。Attention score 从 DDR 经 shared memory 移到 tile-local，会改变 staged 与 fused 方案的状态所有权；Q/K 共用 DMA 路径、V 的独立路径、broadcast 与 cascade summary 都须能按真实布局工作，不能仅以 score bytes 最少决定 fusion。

两代 XDNA 的受限案例说明停止条件也由该层级决定：staged 已 compute-bound 时，更深 fusion 收益很小；ridge 更高的设备则可能仍需把 score 留在 tile-local。编译、buffering 与同步共同变化，不能将跨代差异全部归于 fusion；attention 总时间包含 dispatch 和 softmax，GEMM FLOPs 分子也不是全部计算量。BF16 输入与内部 cast、随机输入方差下的数值误差都要独立核对，相关性不证明任务质量无损；warm-up 后取 minimum 不是 tail latency 或生产 SLO。通信可行性、数值预算或收益不成立时，保留已验收 staged kernel、独立 tiles 或 GPU FlashAttention，而不继续为最少 IO 付出更高控制成本。 [必要机制与反证](https://arxiv.org/html/2609.21264v1)。<!-- source-family:SF-2026-ARXIV-2609-21264 -->

片上计算的驻留选择还取决于写入代价，而不只是HBM bytes。CIM写权重或转置昂贵时，KV-stationary和Q/O-stationary会以不同方式支付多query重载、KV stream、partial sum与转置；应按真实memory-write与通信代价选择，而非认为固定KV永远是最优驻留。已有row-max/Softmax数据流原则仍保留，不因换硬件重复推导。

模拟CIM中的INT8矩阵计算仍可能由FP16特殊函数单元完成归一，不能称整条attention全整数。受限28nm模拟/综合不是硅片，macro指标与整系统指标不能直接公平比较，缺少任务质量消融也不允许保证无损；写/流成本或质量优势未立时，KV-stationary、数字执行及GPU FlashAttention继续成立。 [原文必要机制与限制](https://arxiv.org/html/2604.25317v1)。
<!-- source-family:SF-2026-ARXIV-2604-25317 -->

固定模型、短非自回归序列还提供另一种驻留边界：投影与 FFN 的静态权重长期留在模拟阵列，QK、Softmax/SV 与归一等动态运算交给数字路径，使一次输入沿各层物理 pipeline 流动，而不把全部 attention 都写进模拟存储。[MXFormer 的受限设计](https://arxiv.org/html/2602.12480v1)在投影到 attention 的交接保留 full-sequence double buffer，其余多按 token 流动；吞吐因而受线性静态路径与二次 attention 路径的较慢者限制，序列改变会移动平衡点。有限共享 exponent/mirror 范围又需离线校准和 underflow 的第二 pass，扩大可表示范围以模拟吞吐与效率减半为代价；原 MXFP4 reference 已经 QAT，不因无需 hardware-specific retrain 就称无需量化适配。这里的 RTL/器件及 macro 建模、解析稳态和受限 ViT/BERT 质量不是整芯片实硅或长变长 LLM decode 的验收，外部 activation I/O、model reload、队列与尾延迟仍应计费。模型不固定、sequence buffer/校准支持失配或质量成本回归时，保留原数字驻留、普通低比特/GPU 执行，不由片上静态权重推断全系统无 I/O。<!-- source-family:SF-2026-ARXIV-2602-12480 -->

若数字路径不是专用特殊函数单元，而是通用 Boolean 存内运算阵列，模拟/数字交接还必须约束一条矩阵运算的中间状态：partial products 可边传输边 shift，但相加要等待传输完成，ADC 产率须匹配数字阵列的 row-write 速率；arbiter 不让较新的数字指令穿插正在进行的 MVM reduction，pipeline-reserve 防止临时 buffer 覆盖仍存活的寄存器。这样才可能用可编程数字路径承接动态 attention，而不是反复把动态矩阵写回模拟阵列；转置、shift/add、调度与中间驻留仍需付费。[受限模拟架构](https://arxiv.org/html/2602.16075v1)的 encoder 实验中，non-MVM 仍占执行时间的 71%，不能把灵活性等同专用 SFU 效率，更不能外推 GPU 自回归 decode；器件噪声只部分建模，完整可靠性尚待芯片测量。输入长度、数值质量或交接速率不匹配时，专用 SFU、普通数字驻留与 GPU 路径仍应保留。<!-- source-family:SF-2026-ARXIV-2602-16075 -->

缓存刷新与验证也会改变 IO 计划。Masked diffusion 模型复用近似 KV 时，省下重复前向并不意味着省下状态写回；执行器可以将本次 Q/K/V 投影、位置变换与 cache write 在 SRAM 中融合，只把最终 KV 写回 HBM，再让 tracked 与仍 masked 的 query 读取完整 cache。若同一步还用两种 mask 视图检查候选，刷新 query 集合、视图可见性与 block 工作划分就要共同冻结，不能只优化一个静态 attention kernel。两视图必须隔离各自的可见 token，但它们仍来自同一模型，不是统计独立的验证者。

逐位置 agreement 可以决定这次保留到哪里，却不能证明答案真值、原联合采样分布或未刷新 KV 的精确性；窗口、confidence 门槛和 cache 近似共同承担质量预算。[Flash-dLLM 的必要机制与反证](https://arxiv.org/html/2609.26796v1)支持受测 masked 模型中的这一执行分支，也观察到 confidence-only 的峰值准确率略高；局部 kernel 与端到端设备配置不同，不能换算为任意设备或生产 SLO。新增验证流量、metadata 或门槛漂移使收益不成立时，全量刷新和普通 attention 继续有效，cache freshness 与采样语义仍分别由相应 owner 管理。
<!-- source-family:SF-2026-ARXIV-2609-26796 -->

同一 logical mask 也可能有多种物理执行计划。动态 block-sparse attention 可以在不改变允许的 token pairs 与归一域的前提下，将 blocks 直接执行、合粗后保留内部 membership mask，或拆细再组织任务；选择哪种 retile 与如何分配 work 是两层决定。若在线穷举每个 eligible kernel，得到的最短 kernel 时间可能反而增加 cold request 的准备时间，因此可以离线建立带 feature schema、硬件/profile 和数值格式版本的候选 portfolio，在线先核 layout、workspace 与 metadata 条件，再只准备一份计划。

这个分支增加离线 profiling、目录维护与输入分布覆盖成本，计划排名也不拥有语义正确性。[Tessera 的受限证据](https://arxiv.org/html/2609.25869v1)保持 logical interaction 与 softmax 域，但浮点重排只经 reference 数值检查，不保证 bitwise equality；冷请求对照不含免费的离线搜索，也不能推广为任意 mask、硬件或生产 SLO 的最优计划。条件不匹配时应选已验证的 eligible base plan，无可用计划则返回 no-plan 并交给普通路径，而不是勉强执行排名第一的 kernel；shape 少、重复负载稳定时，静态 native plan 仍更简单。
<!-- source-family:SF-2026-ARXIV-2609-25869 -->

### Heterogeneous Batch Packing 必须同时守住 Attention 语义与 I/O Locality

按最长序列 padding 成矩形 batch，在长度相近、batch 稳定时拥有简单 shape 与成熟 kernel；在线 serving 的 prefill/decode 长度持续变化后，padding 会让大量线程处理无效 token，而仅把请求压平又可能破坏 causal boundary、prefix reuse 和 KV locality。一个 execution-plan 分支先由 scheduler 冻结 request membership、token range、mask 与 KV generation，再把不同长度请求组合为负载更均衡的 execution units，并让 kernel 以 padding-free layout 执行 exact attention；grouping 可以利用 prefix/I/O locality，但不能跨 request 改写可见 token。

packing 减少无效计算并改善 thread-block balance，却增加 metadata、重排、KV layout、group-search 与动态 shape 成本；长度均匀、batch 小或重排开销支配时，普通 padded/continuous batch 仍更稳妥。`arXiv:2602.06072v1` 的 exact-v1 只支持 §3 的 PackInfer grouping、lossless attention、I/O locality 与 prefill/decode integration，以及 §4.3 等作者实验，不证明任意模型、kernel、prefix 分布或 SLO 下都应使用同一 packing policy。

<!-- source-family:SF-2026-ARXIV-2602-06072 -->

### Output Projection 也有精确与近似两条执行路径

标准输出层计算全部 vocabulary logits，再执行 Top-K/Top-P；它在 batch 足够大、GPU GEMM 高效或任务要求完整分布时最简单，也保留精确采样语义。小模型保留十万级多语言词表、且交互式 decode 的 batch 很小时，输出矩阵却可能从“普通尾层”变成 memory-bandwidth critical path。此时可以把 `hidden state × token embedding` 的最大内积选择改写成近似 MIPS：静态索引只召回少量候选 token，再由既有 logit processor 消费稀疏结果。

该分支用近似检索误差、非连续访存和额外索引内存换掉全词表扫描；索引参数与模型 revision 必须共同版本化，并以真实 token states 检查 Top-K recall 与生成质量。batch 变大后，连续 GEMM 的复用会重新胜过图遍历；量化、GPU 索引和完整 softmax 需求也会移动交叉点。`arXiv:2608.27460v1` 只在 CPU FP32、batch 1 为主的 Gemma/Llama/Qwen 小模型上证明这一受限 operating point，且使用 LLM judge 检查生成质量；它不证明近似 head 保持原分布、适合高吞吐 GPU serving，或 82% 的端到端提升可迁移。

<!-- source-family:SF-2026-ARXIV-2608-27460 -->

完整词表扫描也不等于跨精度决定相同：greedy 只排除采样随机性，前两名 logit 的差距很小时，数值扰动仍可能交换 argmax。一个受限执行分支先按原 precision plan 计算 top-two margin，再只对低 margin 的 step 以 FP32 重算输出 head；触发条件与修复范围必须分别版本化。它不改变第 20 章的 argmax/tie 语义，也不保证高 margin 就正确；将低精度存储的权重 cast 成 FP32 只能改变后续算术，不能恢复已经截断的值。

局部保护用额外 head 计算和临时缓冲换逐例一致性，但扩大到 RMSNorm 或更多 body 运算并不单调改善结果，margin gate 仍是经验启发而非安全证书。[受限实验证据](https://arxiv.org/pdf/2609.26621v1)以 A10G、TinyLlama、greedy 短生成为主，较大 batch 与全流程 FP8 的修复有限，实测 peak memory 也有增加；它不证明 hidden 相同与输出决定相同互为必要充分条件，更不证明任意模型或硬件的重放等价。触发成本过高、任务回归失败或误差已来自 body 时，应保留完整既定 precision plan，或从原始权重构建更高精度 artifact 后重新验收，而非继续扩大未经验证的保护范围。<!-- source-family:SF-2026-ARXIV-2609-26621 -->

输出 head 还有不改变标准 softmax 分布的表示自由度：把每行权重都减去同一向量，只会从全部 logits 减去相同标量。Full precision 下分布相同，量化后却可能因为网格不与这个变换交换而有不同误差；因此可在冻结校准集上沿 row-mean 方向搜索公共平移，以输出分布偏差而非仅 weight MSE 选择 artifact。候选包含零平移，只保证该 validation 目标不会因网格搜索而变差，不保证未见输入或其他量化器的最优性。

这一恒等式要求公共量真正进入 softmax：tanh softcap 等前置非线性会破坏它，必须在非线性前用额外 dot/broadcast 还原相应公共量，再独立验收量化误差与成本。Tied embedding 若为保持输入表而另存量化输出 head，整模型驻留内存反而可能增加；作者 Phi/A10G 的 packed-head 局部计时也不能替其他模型的修正路径宣称免费。分布漂移、格式切换或任务回归失败时，保留原 head／更高精度并重新校准；不能以公共平移等价证明量化分布等价。[原文 §2–5／Appendix B](https://arxiv.org/html/2609.31291v1) <!-- source-family:SF-2026-ARXIV-2609-31291 -->

### Exact Top-K 可以复用时间相关性，但必须保留验证权

每个 decode step 从头扫描并排序全部候选，是最稳妥的 exact Top-K；context 很长且稀疏 attention 的 indexer 已经足够快时，这个选择阶段本身会进入 critical path。相邻 decode step 的重要位置常有相关性，因此上一轮 Top-K 可以成为 proposal，但不能直接成为下一轮答案。

<!-- semantic-body-binding:SF-2026-ARXIV-2604-22312:start -->
受限演进是保存 previous Top-K 与预索引统计，用少量全局 counting pass 收缩 threshold；找到容纳真实 Top-K、且候选数不超过容量上限的阈值后，先收集并验证候选，再在 shared memory 内 refine 到恰好 K 个。阈值搜索不能满足容量条件时走显式回退，而非把一次验证失败当作正常 refine 路径。Temporal state 只拥有猜测，exact selection 仍拥有提交权；收益来自跳过不必要的全量排序，代价是 previous Top-K 与 scratch 的 HBM 状态、约 60 KB/CTA 的 shared-memory footprint，以及 single-CTA 设计对并行度的约束。Short context、large batch、低时间相关输入和跨 GPU 路径尚未得到同等验证，可能使额外统计与 pass 反而占主导。

相关性不足、索引失效、SMEM/occupancy 不合适或硬件/shape 不匹配时应回退常规 exact Top-K。作者结果绑定 NVIDIA Blackwell、披露的 sparse-attention decode workload 和 1–2 pass 实现，不证明其他 accelerator、prefill、cross-GPU 或生产 SLO 获得同样收益。
<!-- semantic-body-binding:SF-2026-ARXIV-2604-22312:end -->

当稀疏attention的精确排名不是最终合同、而选择器本身已成为瓶颈时，可以用低比特Q/K近似打分，再由score histogram寻找覆盖目标预算的阈值，最后在原始K/V上计算被选集合内的attention。它与前面的exact Top-K是不同分支：threshold bucket中的并列项可能使实际集合超过K；选中项计算精确也不证明漏掉的项无影响，选择、gather及数据供给必须共同预算。

低比特格式、heavy-channel处理和阈值预算应绑定模型/shape，并用完整输出质量验收；质量或供给成本不合算时回退exact selector或dense attention。受限RTL、综合与FPGA功耗证据不等于流片或Serving端到端测量，设计点的稀疏率也不能与另一质量协议混算；作者局部任务存在质量反退，不能称近似选择普遍无损。 [原文必要机制与限制](https://arxiv.org/html/2604.24820v1)。
<!-- source-family:SF-2026-ARXIV-2604-24820 -->

## 量化为什么不自动带来加速

FP8、FP4、INT8、INT4 这类低精度路径的系统目标，是降低权重、activation 或 cache 的存储和带宽压力，并提高硬件 tensor core 的有效吞吐。

### 先定义低比特表示，再讨论 Kernel

最简单的起点是均匀整数网格。令 `x` 为原始实数，`s > 0` 为 scale，整数 `z` 为实数零对应的 zero-point，`q_min/q_max` 为编码范围；量化 Q 和反量化 DQ 可以写成：

```text
q = clip(round(x / s) + z, q_min, q_max)
x_hat = s * (q - z)
```

`round` 的规则也是格式契约，例如 nearest-even；DQ 得到的是网格上的近似值 `x_hat`，不是恢复原始 `x`。未发生 clipping 时，理想实数算术下的最近舍入误差不超过 `s/2`；超出范围后还会叠加饱和误差，不能继续用这一界保证质量。对称方案通常取 `z=0`，非对称方案允许偏移网格，以覆盖偏向一侧的分布；偏移也会增加 metadata 或算术处理。这里是通用 affine integer quantization，[ONNX QuantizeLinear](https://onnx.ai/onnx/operators/onnx__QuantizeLinear.html)给出对应接口；不能据此推断每个 backend 都支持任意 zero-point。TensorRT 的[量化方案](https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/quantized-types-schemes.html)采用对称路径，FP8/FP4 则舍入到各自非均匀浮点可表示值，不能直接套用整数网格的固定步长误差界。

一个手算例子是用 INT4 编码 `[-1, -0.2, 0.2, 1]`，取 `s=1/7`、`z=0` 和编码范围 `[-8, 7]`：整数码为 `[-7, -1, 1, 7]`，重构为 `[-1, -1/7, 1/7, 1]`。若同组再出现 `100`，仅按最大绝对值扩大 scale，会让原来这些小值都舍入为零；主动裁剪大值又会增加它自身的误差。这正是 calibration 要在范围、分辨率与实际输出质量之间选择，而不是只寻找最小文件的原因。

### 粒度与校准决定谁共享同一份误差预算

Per-tensor 用一个 scale 覆盖整块张量，接口最简单；per-channel 沿指定轴使用不同 scale，避免幅度大的通道拖累所有通道；group/block-wise 再把轴上的元素分成更小的共享组。粒度越细，通常越容易贴近局部分布，却需要更多 scale、可能的 zero-point、解包和 kernel 索引。轴、group size 与物理 layout 必须一同约定，不能把同为“4-bit”的 artifact 直接互换。若每组 `g` 个 `b`-bit 值另存 `m` bits metadata，忽略 padding 时每值实际成本为 `b + m/g` bits；例如每 128 个 4-bit 值保存一个 FP16 scale，是 `4.125` bits/value，而非恰好 4 bits。这只是容量算式，不是吞吐结论。

共享 exponent 的 MX block 还使量化轴成为算子语义，而不只是存储 layout：普通 activation transpose 若改变共享组，不能仅换 stride 后沿用旧 exponent，通常还需高精度转换、重分组与重新量化。一个受限执行分支把整数投影权重的转置放到编译期，利用 `V=X W_INT S_W` 的维度关系，把 per-channel scale 留到 attention 输出端，以两次消费转置输入的 matmul 避免显式转置 V；这是该线性投影与 scale 位置下的代数重排，不是任意矩阵可交换，更不能把 scale 穿过 softmax。[TriGen 的必要原式与执行对照](https://arxiv.org/html/2602.12962v1)中，此 transpose 优化只在已有方案上增益约 1.77%，全组合的 2.73×还包含格式、LUT 和其他优化；cycle simulator/RTL 综合不等于生产服务测量。Backend 必须另验实际共享轴、量化顺序、数值误差与端到端成本，条件不相容或重排净成本不利时，保留 materialize 后的高精度转换/重分组、普通 layout 或更高精度路径。<!-- source-family:SF-2026-ARXIV-2602-12962 -->

粒度更细也不保证单块误差更小，因为 scale 本身同样是有限精度的数。以 block 最大值定标时，缩小组会改变 scale 舍入误差在整组误差中的权重；若局部分布较窄，scale 的最小非零值还可能使小 scale 下溢。真实 LLM 权重中的有限对照发现，UE4M3 scale 配合 FP4 时，一些模型的小 block 反而有更大误差，另一些模型如 Llama2 没有这种反退。因而 group size、scale 的 dynamic range 与有效位宽要共同选型，不能由“局部范围更贴近数据”直接推出质量单调改善。

格式选择还要按张量角色与层段验收，不能把 weight 上较高的 SQNR 顺序原样授给 activation、Key 或 Value。[HiFloat 的受限同位宽对照](https://arxiv.org/html/2602.12635v1)中，HiF4 的 weight 重构较好，activation 却由 NVFP4 更好，Key 的格式顺序随早晚层改变；共享 scale 的层级、实际 metadata 成本和不同角色的分布因而须共同进入 artifact，而非全模型只标一个“4-bit”。这些有限 PTQ 结果没有证明哪个格式普遍最优，局部 SQNR 更不能替下游质量或原生 NPU kernel 验收；表中 INT8 的 GSM 退步也不支持笼统的近乎无损宣传。新增分角色 profiling、格式组合与转换都需计费，并联验 W/A/K/V 的任务质量与真实执行预算；校准人口、backend 或质量失配时，保留成熟整数/浮点格式、weight-only、较高 KV 精度或高精度路径。<!-- source-family:SF-2026-ARXIV-2602-12635 -->

一条格式分支把 unsigned scale 原先未使用的 sign 位转作 exponent 位，UE5M3 因此扩展可表示的低端范围；另一条分支保留 UE4M3，先做动态全局 prescale。这两种方案各有局部质量与实现代价，并不互相普遍替代，也没有恢复 BF16 的无损保证。扩大 scale 范围需要重新设计 quantizer 与 scale-processing 硬件，逻辑综合中的低面积开销不等于现成 GPU 已支持或 serving 已加速；输入分布、模型或硬件不匹配时，更保守的 block、scale 格式与高精度路径仍是必要基线。[有限格式与模型对照](https://arxiv.org/html/2601.19026v1)支持这一非单调边界，不采用原文变量变换不一致的精确下溢阈值与概率公式。<!-- source-family:SF-2026-ARXIV-2601-19026 -->

粒度细化还可能破坏原本相关的输出：视频 diffusion 中，相近空间 token 或同一区域跨帧的 activation 可因局部统计略变而选到不同数值格式；逐块重构误差较小，不保证整体时空一致。一条受限分支以 attention 作为相关性代理，让 anchor 与相关 token 共享覆盖不同动态范围的 **sub-formatbook**，但仍各自选择 dialect，而非强迫它们使用同一网格。它用跨块选择约束换取格式一致性，同时增加 attention profiling、关联窗口、覆盖冲突和随 denoising step 更新的状态；窗口过大或更新过密也可能退步。[SemanticDialect exact-v1](https://arxiv.org/html/2603.02883v1)只在两种 Open-Sora 架构中验证该分支，多个质量指标不单调改善，attention 也不等于语义真值。相关性不可靠时保留独立块选择或提高精度；v1 的 CUDA kernel 与 RTL 成本评估仍属未来工作，不能由四比特表示推部署吞吐。<!-- source-family:SF-2026-ARXIV-2603-02883 -->

静态 calibration 提前用代表性数据确定 activation 范围或重构目标，运行时路径较轻，但分布漂移会使旧 scale 失配；动态量化根据当前输入计算 scale，降低对固定范围的依赖，却把 reduction、转换和 metadata 带入热路径。Weight-only 的最简单方案也可以直接从权重统计定标；是否需要校准样本取决于量化目标，不能把所有 PTQ 都写成同一种准备流程。

下游算子保留浮点，不代表它仍消费原来的输入分布。量化language backbone后，送往action DiT的feature偏差可改变Q/K logits的离散程度与output projection后的residual能量；因此层选择不能仅按各层孤立重构误差决定。一个受限layout保留DiT attention projections为浮点，只量化上游LLM和DiT MLP，再将接口的logits统计、输出RMS与实际action结果分别校准；calibration buffer、teacher与模块边界必须同artifact绑定。<!-- source-family:SF-2026-ARXIV-2602-20309 -->

[有限VLA仿真对照](https://arxiv.org/html/2602.20309v1#S4)支持上述layout与统计诊断，不把统计匹配等同动作正确：部分long-task和更低位宽仍退步。原文scalar比例与施加式、clip规格未完全一致，未核实现时不能直接复制exact修正配方或宣称零运行时成本；所报LLM+DiT内存下降也不是完整服务memory、延迟或物理安全保证。代表性轨迹、离线统计与逐任务回归有成本，接口漂移、artifact或行为验收失败时，保留更高精度模块、重新校准或原浮点policy，而不由平均成功率放行所有control阶段。

校准目标还可以显式加入行为条件，而不只重构无条件 activation：先在已对齐模型各层冻结 benign/harmful 的 sparse-logistic probe，再调整量化 scale/clipping，使 benign 样本保持局部重构、另一类样本向该 probe 的指定 margin 分离。[Q-realign 的受限分支](https://arxiv.org/html/2601.08089v1)以几何 probe 作为训练代理，不需要把安全回复当逐 token target；proxy、两类校准人口、loss 与来源 checkpoint 因而都属于 artifact 身份。分类可分不证明拒绝或最终输出安全，更不能从类间距离恢复“真实安全机制”。<!-- source-family:SF-2026-ARXIV-2601-08089 -->

同格式 reconstruction-only 对照支持局部行为目标的作用，但只用另一类目标、不保 benign 重构时，低 harmful score 可伴随 incoherent 输出；激进 W4A4 也出现质量坍塌。证据限 LoRA 更新后的有限模型、三次运行与 A6000 校准，accuracy 仍有代价，不能授普遍恢复或端到端安全。Probe 构造、类条件校准与回归有额外预算，实际 kernel 吞吐另验；模型/人口漂移或质量失败时，保留原已对齐 checkpoint、更保守位宽、常规校准和独立行为测试，不把更低分数当可用产物。

<!-- semantic-body-binding:SF-2026-ARXIV-2609-33923:start -->
无校准数据时，随机probe可以给线性量化误差Δ的平方Frobenius范数作无偏trace估计；误差谱分散时其方差较小，却仍只测isolated tensor。把输入secondmoment与后续固定线性映射加入，估计目标才变为加权误差能量；实际网络的非线性、残差和cosine归一又改变所测对象。因而“isolated估计准”“层重构目标准”与“按该分数分位宽得到完整模型质量好”须分别验证，不能用同一个calibration标签授三种结论。

[ProbeQuant v1 §3–4.6](https://arxiv.org/html/2609.33923v1)中，输入传播与独立重采probe给不同排序，切换后可能损坏目标估计；即使realactivation局部目标更准确，同预算分配仍可输给包含block下游权重的信号。结果仅属有限模型/格式对照，不证明block代理普遍最佳。Probe、逐候选层执行、manifest与guardrail都有离线成本，保留embedding/head/metadata的比例预算也可能低估实际大小；近似greedy不授全局最优或HBM保证。目标/统计不稳或质量失败时扩大代表性校准、提高局部精度或回uniform/成熟PTQ，并按实际文件、完整成本和held-out质量验收。
<!-- semantic-body-binding:SF-2026-ARXIV-2609-33923:end -->

代表性 calibration pool 已固定时，小预算样本选择仍有两个不同目标：单个样本的 variance/PPL 高，不保证多个样本共同暴露量化最敏感的通道。一个分支先 profile 候选池的 outlier-channel 激活，再按参考幅度与 weight-column norm 加权，贪心选择能够增加互补 channel coverage 的样本。通道 scale 决定怎样编码已见范围，样本选择决定校准过程看见哪些范围；两者应分别版本化 pool、threshold、coverage weights、sample membership 与目标量化 artifact。<!-- source-family:SF-2026-ARXIV-2604-24008 -->

覆盖更多已知通道不能创造池中缺失的部署切片，也不能保证 downstream accuracy。[exact-v1 §3–7/Appendix I–J](https://arxiv.org/html/2604.24008v1)的 `1−1/e` 只约束带基数限制的 weighted-cover 目标，stylized channel surrogate 不是实际 loss/Frobenius 上界；mean+6σ 阈值也是启发式。作者 10k pool 的 profile 约 15 分钟 A100，随后 CPU 选择虽短仍不是免费；INT4 AWQ/GPTQ、有限 7B/8B 模型和预算结果不支持任意位宽/数据。Pool 或通道权重漂移、敏感切片不达标时，扩大/分层校准、重新 profile 或局部高精度回退；简单稳定分布仍可沿用随机代表性样本。

校准目标还留下一个统计问题：量化误差向量本身由校准样本决定，不能把小 empirical reconstruction loss 直接当成未见输入的 population 保证。OPTQ 的受限分析把校准矩阵增广为 `[X; sqrt(λ) I]`，为样本没有覆盖的方向加入正则预算，并使逐列补偿的 tail least-squares 满秩。其同分布结论要求独立同分布的校准与测试输入、几乎处处有界范数以及足够大的 `λ`；另一结论针对固定 `X` 的随机舍入，只要求测试分布有限二阶矩，概率来自舍入而非校准抽样。这两种证据权限不能合并为 deterministic OPTQ 在任意分布漂移下的保证。[必要假设：Theorem 3.1／Corollary 3.4／§4.1](https://arxiv.org/html/2609.31560v1)

正则保护未见方向，也会加入新的误差项；过大并非免费，经验 `β` 与用样本二阶矩替代 population moment 仍依赖选择和浓缩条件，不能直接得出通用 optimal `λ`。该理论使用无 clipping 的舍入网格，有限维 Hadamard／ReLU 实验中的误差代理也不是完整 LLM 任务质量或硬件吞吐。实际 artifact 仍要独立检查 clipping、分布、格式与敏感任务；条件失配时扩大／分层校准、重新定标或提高局部精度，而不是用理论界代替真实质量验收。它细化校准的可外推条件，不取代前面的 coverage 选择，也不承诺新的低比特 kernel 收益。
<!-- source-family:SF-2026-ARXIV-2609-31560 -->

同一组权重在 recurrent depth 中反复使用时，校准还要覆盖“第几次进入运行图”，而不只是输入来自哪个数据集。残差 core 的 identity path 与没有这条保护的 loop entry 对舍入反馈不同：entry 的 state/embedding 误差可以在后续循环重新进入，局部 Jacobian 只诊断附近传播，不能证明整个非线性循环收敛；状态有界甚至到达固定点，也可能稳定在错误答案。只用 step 0 的 Hessian 看不到后步激活方向，固定高精度参考轨迹上的跨步 `Σ H_t` 可以扩大重构目标的覆盖，却仍不是实际量化闭环的可靠性保证。[LoopPTQ §2–6 的运行图与受控反例](https://arxiv.org/html/2609.30820v1)

增加 step-0 样本或 damping 不会自动创造后步 covariance，后步 rank 更高也不等于任务质量更好：阈值、样本数和参考状态共同决定这个诊断。跨步采样须计额外前向与统计成本，并区分固定 bf16 trajectory、量化 trajectory 和真正部署 artifact；不同 PTQ 目标及 loop 架构不能套用同一病因。作者多架构模拟与 Huginn/A100 的有限 Marlin 短 forward 支持局部质量/成本取舍，不支持生产 serving SLO 或全闭环修复。Entry 保持高精度、重新采样实际可达状态、简单 RTN 或 bf16 回退都应保留，rotation 与局部精度策略也要重新验收，而不是按 rank 单指标自动放行。<!-- source-family:SF-2026-ARXIV-2609-30820 -->

固定全精度参考一次得到的curvature，不一定继续代表逐块量化后的模型。一条局部重构分支以当前partial-quantized输入为起点，在每个Transformerblock重新采集gradient与近似Hessian；多数block对齐输出MSE，末block对齐分布KL，再把逐列舍入补偿与first-order更新合用。通过Cholesky递推维护gradient–inverseHessian积，可避免每列重新反演，lazybatch则摊薄后续列写回；这增加backward、gradient统计与辅助矩阵成本，不是部署runtime的免费精度恢复。

直接first-order补偿可能离开局部Taylor近似可用区域，因此可按估计loss预算缩小该分量，再在当前block校准阈值；估计预算、近似Hessian和row-wise共享scale都不能认证真实非线性loss有界。更多刷新阶段也可能质量反退，作者校准显存和时间高于GPTQ，局部质量改善不证明Serving收益。刷新、分组、tuning数据及预算须随artifact绑定；代理失配、校准成本过高或任务回归失败时，保留较简单GPTQ/RTN或局部高精度，而不借trust-region名称签发全模型稳定保证。[方法与反例](https://arxiv.org/html/2609.31009v1) <!-- source-family:SF-2026-ARXIV-2609-31009 -->

对扩散/Flow 的跨时步执行，activation 精度选择与静态 weight 校准还应分责。一条受限分支以 gradient-squared Fisher 为 signal，在 layer/timestep 上选择不同 activation bit；有限 beam 先筛候选的 bit-average 与重构误差，再用小 batch 生成质量选方案。权重不按时步保存多套，而用 Fisher 的时间权重聚合 `Σ α_t X_t X_tᵀ`，或等价的 `√α_t X_t` 特征，形成静态校准矩阵。这个接口让“哪些时步采用什么 activation 精度”与“同一 weight 如何覆盖时步人口”成为不同 artifact 字段，不等于只把每步 Hessian 无权求和。 [必要机制与对照](https://arxiv.org/html/2602.09883v1)。<!-- source-family:SF-2026-ARXIV-2602-09883 -->

Fisher 和 beam 都是代理：平均 bit 未按参数/FLOPs 或物理 bytes 加权，有限非支配筛选不保证全空间最优，最终质量选优调用仍计成本。部分质量维度和组件对照反退，理论 model-size/FLOPs 也不能认证 runtime kernel 吞吐；原文 bit 比例的字面平均3.6与声称3.1不一致，不采用精确节省换算。校准、选型、metadata 与部署执行须联合验收；时步统计漂移、低位 kernel 不支持或净质量/费用退步时，保留较简单跨时步校准、统一精度或局部高精度，而不把搜索成功当作实际 serving 保证。<!-- source-family:SF-2026-ARXIV-2602-09883 -->

### PTQ 与 QAT 是产物形成方式，不是两类推理 Kernel

Post-training quantization（PTQ）从已有 checkpoint 出发，在训练之后选择网格、校准或做局部重构，避免重新执行完整训练；quantization-aware training（QAT）则在训练/微调中让 forward 感受到目标 Q/DQ 误差，并通过相应梯度近似调整参数。前者准备成本较低但可能无法恢复敏感层，后者支付训练数据与优化成本，也不能保证任意低位宽都满足质量要求。两条路线最终都要导出具体格式、scale、图与 kernel 可消费的 artifact；训练中的 fake quantization 不等于部署时已经在运行低比特指令。[TensorRT 工作流文档](https://docs.nvidia.com/deeplearning/tensorrt/latest/inference-library/quantized-types-workflows.html)区分了这两条准备路径与显式 Q/DQ 图。

还可在 PTQ/QAT 之前单独改变 checkpoint 的谱 conditioning：训练中按少数主奇异值占平方谱质量的比例选择层与分量，以更高次谱惩罚抑制大奇异值，再把形成的完整精度 checkpoint 交给原量化流程；这不是已在 forward 模拟低位误差的 fake-QAT。`‖Wx‖≤σmax(W)‖x‖` 只给放大上界，不能唯一归因全部 outlier，也不证明大 activation 没有功能。[受限 S²D 对照](https://arxiv.org/html/2602.14432v1)采用 top≤3、阈值.95与每100步刷新缓存的谱分量，陈旧分量随权重更新会失配。SVD、训练和刷新均有成本：作者8×A100报告约18秒SVD与6秒gradient pass，提前3次迭代重叠不等实测端到端零费。部分PTQ切片反退，量化产物仍须独立质量/执行验收；谱代理、缓存或净费用不合算时，保留普通校准、QAT或敏感层较高精度，而非把训练conditioning当低位部署保证。<!-- source-family:SF-2026-ARXIV-2602-14432 -->

固定 weight-memory 预算时，QAT 还允许把位宽换成更多参数，但这不是固定 compute 或固定速率的比较：格式包含 scale/centroid metadata，embedding、输出层及 backward 仍可用高精度，KV/activation 也不包含在 weight bytes 内。[1-Bit Wonder 的有限 generative 对照](https://arxiv.org/html/2602.15563v1#S4)在相近 weight-memory 下比较不同容量与位宽，显示任务质量的局部取舍，1-bit 并未支配全部任务；更大低位模型的 batch-1 decode 又可慢于小高位模型，大 batch/prefill 也不保证加速。低比特 kernel 的有限测量不能替代完整 SLO/quality-matched 服务验收，QAT 训练与高精度反传也有成本。因此 artifact owner 要共同冻结容量、实际编码格式与未量化部分，分别比较质量、总驻留内存和执行路径；质量或净成本不合算时，4-bit、混合精度及小 dense 仍是合理分支，不能把“同内存更大”解释成全面更省。<!-- source-family:SF-2026-ARXIV-2602-15563 -->

混合精度还可把敏感容量做成独立训练分支，而不是只在同一矩阵中提高若干元素的位宽：低位 FFN 与窄高精度 FFN 消费同一输入，输出以可学习 feature scale 合成，额外的高精度分支再由训练所得 router 做 top-1 选择。这样减少单步激活的高精度工作，却仍需常驻全部候选分支；active parameters、读取流量和 physical memory 不能共用一个“模型大小”。[pQuant v1 §3–4](https://arxiv.org/html/2602.22592v1) 的 QAT-from-scratch 分支在有限、匹配训练预算的局部对照中优于朴素混精，但八分支配置的常驻内存高于相近 BitNet 对照，未建立任意大模型或服务 SLO 的收益。训练的高精度 master/梯度、router、scale、导出和部署 kernel 均有费用，Apple M2 单算子测量也不是整套服务加速；敏感分支、容量或净成本不合算时，普通 QAT/PTQ、固定混精与较高位宽仍应保留。<!-- source-family:SF-2026-ARXIV-2602-22592 -->

PTQ/QAT 还可以改变被优化的压缩结构：量化网格相同，不表示权重串中的重复 pattern 相同。一种受限训练分支将多个矩阵的 row-wise codes 序列化，在不跨 row 的规则下，以 code-space distortion 预算将近似重复片段改写为共享片段，再做 lossless grammar 合并；展开回权重执行 forward，直通梯度仍更新原参数。它优化重复结构而非单值位宽，增加序列化、近邻 rewrite 与周期性重建成本，也不同于运行时直接消费 centroid 的 lookup kernel。

更少 grammar symbols 不自动等于更少编码 bytes、HBM 或更快计算；规则、symbol宽度、解包和执行路径还未计入。作者两种 ViT 的 MLP 微调与匹配 int8QAT支持有限 grammar–质量取舍，但保留精度退步与额外训练开销，shared-cluster wallclock也不隔离算子成本。缺乏匹配 grammar consumer 或任务回归失败时，保留普通量化/码本与高精度方案；只有真实 artifact 同时通过质量、存储和执行验收，才把可重复结构当部署收益。[方法与限制](https://arxiv.org/html/2609.31564v1) <!-- source-family:SF-2026-ARXIV-2609-31564 -->

`W4A16`、`W8A8` 分别描述 weight/activation 的目标位宽，不完整规定 accumulator、输出 dtype、KV 精度和未量化算子。Q/DQ 表达数值边界，执行器可以在合法条件下融合转换；是否真的少搬 bytes、用到低精度计算单元并提高端到端速度，仍需检查实际 kernel。下面因此先算执行成本，再讨论码本、误差恢复与分布相关的条件分支。

### 从表示压缩到可执行路径

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

低位宽表示也未必对应整数乘法。非均匀 weight centroids 与 assignment codes 保留更灵活的重构自由度，却要求执行器理解码本；若 activation 也编码，可以预计算 activation code×weight centroid 的乘积表，再以 lookup 和累加替代部分乘法。Rotation 或 permutation 只有能合法折入相邻算子时才免去显式转换；MoE 的聚合输出与 router-KL 校准也不能证明专家选择完全不变。因此 checkpoint 的码本、assignment layout、变换和 product-LUT kernel 必须共同进入 execution plan，而不是把它当普通 INT4 文件交给任意 tensor core。<!-- source-family:SF-2026-ARXIV-2604-10496 -->

该分支增加离线校准、解码、表布局、存储/银行冲突和未覆盖算子的成本。[受限实现证据](https://arxiv.org/html/2604.10496v1)区分 CPU 执行与修改 tensor-core/shared-memory 的 Accel-Sim GPU 路径，后者不是新 kernel 已在 A100 实机验证；若干质量切片仍低于 BF16，不采用无损或生产 SLO 保证。稳定码本且硬件确有 lookup 支持时可测试这条路径；没有对应实现、activation 编码成本过高或路由/质量失配时，常规反量化、均匀低精度 GEMM 或高精度计算继续成立。

MoE在同一token上给多个experts同一输入，还允许把格式的共享工作与路由后私有工作分开。一个scratchpad分支让gate/up由共享码本和低秩basis加expert-private索引/系数组成：先把input投影成码本读出表及低秩特征，再按路由取private部分。共享格式传输可与router并行，private加载可与共享投影并行，lookup与dense correction又可分配给不同engine；down输入已expert-specific，不能直接继承同样复用。

这不仅减少bytes，也重排哪些工作暴露在criticalpath，却支付scratchpad驻留、gather、格式校准/蒸馏和跨engine同步。相同bits下更细VQ可少搬bytes却增加selection而比BF16更慢；单步PSUM累加变快也可能占用共享bank、使整decode变慢。受限Trainium结果不证明GPU/任意batch同样成立，PPL恢复不等所有任务无损；profile/质量不通过时保留原dense或常规量化路径，分别验收格式、kernel与完整请求成本。 [必要机制与反证](https://arxiv.org/html/2609.21137v1)。<!-- source-family:SF-2026-ARXIV-2609-21137 -->

二值factor的容量也不能只看内层rank。若去除固定sign mask后的factor magnitude只能写成两向量外积，它的envelope仍为秩一；增加两个二值factor乘积的inner rank，只增加另一种自由度，不自动解除每个factor的幅度约束。多个envelope可以扩展这条表示分支，但固定mask下的截断SVD只优化对应factor的Frobenius近似，不是全模型任务最优；当mask也由ADMM自适应选择时，更不能继承同一投影或全局收敛保证。<!-- source-family:SF-2026-ARXIV-2512-24545 -->

共享二值primitive并不把执行化成两次固定成本matmul：令inner rank为l，执行式还含l²项，以及envelope系数、sign mask、scale与未量化层的读取。目标BPW不是整模型resident bits，更大l在若干PPL切片反而退步，局部重构误差改善也不保证任务质量。该路径需要额外量化求解、校准和对应kernel，原始矩阵或更温和量化在质量/成本验收失败时继续成立；没有实际端到端计时，不凭二值表示或操作数计数宣称真实加速。

sign 与 magnitude 的另一种分解，把“符号不用逐项存储”的条件直接加入训练：由 seed/生成器构造固定 sign template，使用 template-aware initialization 与非零 gap，并在更新后硬投影回其支持域；非负幅度再由低秩 factors 重构。[受限 sign-template codec](https://arxiv.org/html/2602.17063v1)并不是训练完后任意删除已有权重的 sign；`sign(GHᵀ)` 也不继承内层乘积的低秩。朴素 SVD 的幅度重构可出现负值，需要实际非负约束或 clamp，目标 bpw 只覆盖指定 tensors 的 factor 预算，seed、shape、generator、scale、未压缩参数及物化成本仍存在。训练中符号稳定的理论依赖累计更新有界与罕见 re-entry 等假设，不证明通用 AdamW 或所有参数自然锁定符号；单步 flips、累计 flips 与终态差异也不能混为同一量。受限实验把 gap/正则挑选、硬投影与压缩共同改变，基线恢复预算未全匹配，不授普遍质量或零存储/零解码成本。符号支持不可保留、非负幅度恢复不足或实际质量—执行费用不合格时，保留显式 sign、常规低位格式或原矩阵，不从训练规律直接跳到部署收益。<!-- source-family:SF-2026-ARXIV-2602-17063 -->

码本 lookup 之外，极低位宽也可以选择不建 LUT 的条件加减路径：ternary 权重的正、负 bit mask 控制 SIMD accumulator 对 activation 加减，末端再应用 scale。在一组共享输入的子 GEMV 中，复用同一次 packed-weight 解码、activation 和寄存器累加，可以减少重复解析与访存。这是 execution plan 的另一条分支，不是“只要权重 ternary 就没有乘法”；scale、非 ternary 算子和模型质量仍须共同验收。<!-- source-family:SF-2026-ARXIV-2604-20913 -->

这条路径依赖目标 ISA、shape、packing 与寄存器压力，也可能把带宽瓶颈转成指令和控制开销。[受限实现](https://arxiv.org/html/2604.20913v1)用 AVX-512/BMI2 处理 widely-linear 的八个子 GEMV，证据限定于 Xeon 8558P、FP32 累加和对应低位模型；单线程 dense 与48线程 ternary 的比较不能当作同资源因果加速，自写 CUDA 的退步也不证明所有 GPU 低位实现不可行。规则 GEMM、反量化或 LUT 在其他 batch、ISA 与质量预算下继续成立；本章选择执行路径，第50章仍负责请求与 worker 协调，不能把局部融合结果外推为在线吞吐或 SLO。

Activation 码也可以沿时间展开，而不只是在一次算子调用中解码成 dense 乘法。在码本、符号和 scale 已约定时，一个替代分支把指定整数码展开成带时间权重的 binary activation spikes，以多个时步累积实现对应线性算子的输入；输入事件二进制不代表矩阵权重全部 binary，也不把任意浮点模型变成精确等价的 spiking 模型。压缩可先移除特定对称 scale 下不可达的负端码，再共同选择模态与层的时步预算；非线性和跨层 scale 仍需各自验证，时间一致性 proxy 不拥有最终质量判定权。<!-- source-family:SF-2026-ARXIV-2604-18610 -->

这用重复累积、时间状态和专用执行器换取局部低成本计算，预算越少越可能损伤表示。MAC/AC 计数与工艺综合、cycle 模拟应和实板端到端延迟分开：[受限多模态对照](https://arxiv.org/html/2604.18610v1)尚不能证明同硬件、所有序列及线上 SLO 的部署收益。已有 dense GPU、低位 LUT 和较大时间预算仍应共存；质量或 scale 接口不满足时回到原整数或 dense 执行，不以 headline 模拟倍率决定替代。第23章继续拥有模态表示及其质量目标，Serving 层再验收请求完成成本，不能从时间编码本身推出端到端收益。

### 浮点收敛与低位宽 Probe 必须分开验收

浮点 loss 趋稳是当前训练目标的有效信号，但不是所有量化网格的发布证书。沿训练轨迹比较量化行为时，应把 checkpoint revision、probe 的 group、scale/zero-point、是否校准及评估样本一起固定，分别检查浮点质量与低位宽变化；未校准的 weight-only probe 可以观察直接 grid compatibility，不能代替后续恢复算法或真实 kernel 的验收。

受限 [Pythia-160M v1研究](https://arxiv.org/html/2604.15167v1)在154个 checkpoint、同一组32批 `4×512` Pile validation tokens 上发现浮点趋稳与 INT4 probe 明显退化并存。其 INT4 是 group128 非对称、INT8 是 per-output-channel 对称，不能把差异全部归于位宽；训练 fork 的低位宽改善也可伴随浮点 PPL 退步，不支持通用 cooldown 配方或“flatness/kurtosis 是唯一原因”。独立 probe 增加评估成本，失配时可重新校准、保留更高精度或转向 GPTQ/AWQ/QAT；这些修复分支不被该探针否定，最终仍须通过实际格式的质量与执行 Gate。<!-- source-family:SF-2026-ARXIV-2604-15167 -->

静态校准或固定语料的 QAD 在短序列质量与准备成本优先时仍合理；长自回归生成却会让量化误差改变后续 student prefix，原语料不一定覆盖部署策略自己走到的状态。恢复训练可先取得能够采样的低位 policy，再让目标量化 forward 产生 rollout，冻结高精度 teacher 在同一 student prefix 上提供指导，配合任务 verifier 训练。这里 BF16 master weights 的梯度更新不等于 BF16 rollout，teacher 也不是真值；本节拥有目标格式产生的状态分布，第29章仍拥有通用 on-policy distillation 目标。

[低位 on-policy distillation 的受限实验](https://arxiv.org/html/2609.26708v1)匹配起点、语料、steps 与 samples，不等于匹配训练 FLOPs、墙钟或最终质量；报告中的追加 OPD GPU 时间也不能吞掉 QAD 初始化费用。teacher/verifier 与状态分布共同变化，未隔离各自唯一因果；部分 baseline 的 embedding/head 精度及实现不同，个别代码与 QA 任务仍退步。新 rollout、teacher 评估和独立长生成回归都有成本，训练中的量化 forward 更不证明部署低比特 kernel 已验收。终止、重复或任务质量恶化时，继续比较普通 QAD/PTQ、更高精度与已验证生成路径，并对实际 artifact 单独执行质量和执行 Gate。<!-- source-family:SF-2026-ARXIV-2609-26708 -->

### Post-quantization Recovery 必须同时通过质量与执行 Gate

极低位宽的 additive codebook 量化还要区分两种自由度：在固定 centroids 上搜索更好的 assignment，以及改变 centroids 本身。逐码本拟合残差便于初始化；容量很有限时，早期 centroids 已限制后续表示，增加 assignment 搜索宽度未必能修复它。一个条件分支仍沿残差顺序处理码本，但按 activation 二阶统计定义加权重建误差，在 E-step 重分配索引、M-step 更新 centroids；这是离线表示选择，不是 runtime 自动纠错。<!-- source-family:SF-2026-ARXIV-2604-08118 -->

该分支增加二阶统计、交替优化与校准时间，block-diagonal/damping 近似也限定了目标；不能把容量 proxy 当作进入良好盆地的充分条件。作者少量 2/3-bit 模型、单 seed 与有限 C4 校准只支持受限质量取舍，其中 perplexity 改善并不处处伴随下游分数提高，校准后选择又使用了 WikiText 指标。它没有证明 lookup runtime 加速；普通 residual 初始化、固定码本搜索、更高位宽和其他 PTQ 路线仍应依据独立质量与实际执行成本共存。<!-- source-family:SF-2026-ARXIV-2604-08118 -->

离线逐列量化也要先冻结“要恢复的输出”。未量化列随补偿步骤不断改变时，用当前已补偿权重产生参照，虽然便于局部更新，却会让参照跟着误差走；若目标是保留原始模型行为，应保存原始浮点权重与浮点输入的输出，将残差分成上游输入量化误差和本层补偿权重偏离原权重的误差。后者不是又一份上游误差，而是迭代过程自身改变了校准坐标。可以预计算相应矩阵并在逐列更新时带入这项残差，不必把恢复变成在线 controller。<!-- source-family:SF-2026-ARXIV-2604-07955 -->

固定原始目标增加校准计算、矩阵状态与峰值内存，并不改变低比特 kernel 的发布条件。作者在 GPTQ/GPTAQ 与所测 Llama 配置中得到质量改善，但旋转、位宽与模型的组合仍可能严重退化；单卡 H20 的校准时间也增加，不能把离线补偿直接称为推理加速。输入分布、原始坐标或目标格式不相容时，重新校准、更高精度和普通 PTQ/QAT 仍是合理回退。<!-- source-family:SF-2026-ARXIV-2604-07955 -->

固定原始浮点输出后，还要问输入量化误差中哪些部分能由本层权重补偿。冻结校准输入及变换，记量化后的输入矩阵为 Z̃，它的列空间投影为 Π；相对于最小二乘补偿权重，输出误差可精确拆成落在该列空间中的权重拟合误差，以及与其正交的输入残余。后者对这个固定输入矩阵不能靠继续改变权重消除；前者的无约束最优也未必落在低比特可表示集合内。因此补偿搜索与改变输入表示是两种自由度，不应把所有残余都交给更宽的权重搜索，也不把一次最小二乘解当作低比特无损保证。

选择输入变换时，persistent outlier 与普通通道统计可分别进入残余上界；据此选择符号旋转和缩放，是界引导的校准分支，不是精确误差再多出两个独立项。L2 与最大幅度缩放来自不同放宽，实际以完整输入近似普通通道统计也须另验；无 clipping 的理论条件不能静默继承给带 clipping 的实验。更低 perplexity 并未使所有任务准确率更好，候选旋转、teacher/scoring 与补偿筛选均付校准成本，低位模拟结果不证明目标 kernel 更快。统计失配、下游质量回退或执行成本不合适时，保留原始目标补偿、较简单变换与更高精度。 [必要机制与反证](https://arxiv.org/html/2609.21450v1)。<!-- source-family:SF-2026-ARXIV-2609-21450 -->

静态 correction 在量化误差近似由 layer 决定时简单；若误差随 token 和输入变化，同一补偿对所有请求都会浪费容量或过度修正。一个条件分支先用诊断器定位高敏感层，再由 per-token gate 提出 error compensation，runtime 通过 fused kernel 执行；gate 只拥有补偿 proposal，量化回归与 serving SLO 共同决定该 artifact 是否可发布。

这种恢复能缩小低比特质量差距，却增加补偿参数、动态分支、kernel shape 和 TP 同步状态。未覆盖 shape、并行布局或延迟抖动超界时，应回退原 W4 或更高精度路径。作者结果只覆盖披露的 per-channel 量化、模型与 serving 设置，不能把质量恢复率或低于 1% 的内存开销外推为任意 engine 的生产收益。
<!-- source-family:SF-2026-ARXIV-2606-11244 -->

恢复也有纯离线的替代分支：如果两个任务共享同一 pretrained 初始化与参数坐标，可以在 donor 上比较普通微调与 QAT 的权重差，再把缩放后的差分加到 receiver，最后按目标格式量化。这里转移的是在该坐标系中学得的补偿方向，不是动态 token controller；同架构、同初始化和相容的量化配置因此是适用前提，不能把任意两个 checkpoint 的相减解释为可移植知识。<!-- source-family:SF-2026-ARXIV-2604-03420 -->

这种做法减少 receiver 专门训练的需求，却把风险转为任务负迁移和差分幅度选择。幅度为一也可能比不转移更差；在 receiver test set 上扫描幅度只给出经验上界，不能称部署时已经零样本选好了参数。现有 ViT、3-bit weight-only 模拟量化证据没有证明 LLM 或真实低比特 kernel 更快。缺少独立 calibration、坐标兼容或逐目标质量验收时，应保留普通 PTQ/QAT，而不是把 donor 的成功当成 receiver 的发布证书。

### 一个 Anchor Artifact 支撑多格式，不等于一次验收覆盖所有格式

目标位宽和硬件固定时，为每种格式分别训练或校准 artifact，边界最清楚；代价是 checkpoint、训练与发布组合随格式数增长。弹性推理希望根据设备、负载或质量预算在多种 MXINT/MXFP 格式间切换后，可以用 multi-format QAT 产生一个较高精度 anchor，再通过确定的 slice-and-scale 规则派生低精度 artifact。

这减少重复训练，却把责任转移到 artifact identity：registry 必须同时记录 anchor revision、转换规则、目标格式、backend/kernel compatibility 和逐格式 acceptance evidence。转换器只产生 proposal；每个目标格式仍要分别验证质量、实际 kernel 路径、内存和端到端 latency，scheduler 不能因为共享 anchor 就假设不同格式等价。

QAT 增加训练约束，运行时转换增加 kernel 与缓存组合，未见模型、格式和硬件仍可能出现精度或性能回归。任一 acceptance gate 失败时应回退 anchor 或已验证的高精度 artifact，而不是在请求路径继续试探未知格式。

<!-- source-family:SF-2026-ARXIV-2604-00529 -->

共享 anchor 也有无需 QAT 的离线 PTQ 分支：固定 parent 整数网格、scale 和 zero-point，对同一候选同时计算多个目标位宽切片的校准误差，再把各位宽残差的平均值传给尚未量化的权重；候选投影中的位宽权重与误差传播的平均规则是不同操作。格式支持低位切片，不等于把独立高位 PTQ 直接截断后仍保持低位质量；目标位宽、整数切片的舍入和 clamp 规则以及跨 bit 误差更新，都需成为 artifact 身份，不能沿用为任意浮点格式的截位规则。额外校准与非均匀 per-layer 预算搜索换来单 parent 的部署选择，但未直接优化的位宽仍需单独验收；可切片也不授权逐 token 动态路由，受限反侧中静态配置已占优。实际 kernel、batch 区间或质量验收失败时，独立 PTQ/QAT 与已验证高位格式继续成立，单 token 测量更不提供生产吞吐保证。<!-- source-family:SF-2026-ARXIV-2602-03537 -->

离线多位宽校准还可以共享补偿容量，而不只共享整数 parent：较高位宽先使用小 rank 的 adapter，较低位宽再追加嵌套 rank slice，并分别优化 clipping；校准后继 block 时，还按不同位宽输出的 token 相似性选择高位 feature 或混合 feature。这改变的是补偿容量与校准输入的跨位宽耦合，因此 rank 切片、clipping、混合规则和校准人口都须绑定 artifact，不能解释成逐 token 免费切换。[QuEPT 的必要机制与对照](https://arxiv.org/html/2602.12609v1)在固定总 rank 的局部比较中改善低位质量，却有高位略逊独立 adapter 的反侧；额外 adapter、feature 生成与逐格式回归均有成本，单设备校准时间也不证明 LLM kernel 更快。跨位宽干扰、质量或实际 kernel/SLO 失配时，独立 PTQ/QAT 与已验收的高位格式仍是合理回退。<!-- source-family:SF-2026-ARXIV-2602-12609 -->

#### 同一量化网格也可按 Bit 与 Memory Tier 分工

独立 draft/target 副本便于分别治理格式；容量受限且数据通路支持共同整数网格时，也可让两者共用一份 bit-nested 表示。高位驻留快存，低位留在外存；draft 只读取驻留高位与 hot-expert 子集，target 则恢复完整 router 和量化权重。表示合同须包含共同 scale、bit 解释和高位舍入规则，不能把任意格式截断都叫相容。执行侧可在每个 projection 上分别计算两 tier 的 partial sum，在依赖的非线性/下一 projection 前合并和重排；输出验证与提交仍由完整量化 target 拥有，而非 draft。

这节省独立副本，却增加低位搬运、partial-sum 同步、expert-pool 更新与 KV 争用，不能从存储节省推出加速。[ELMoE-3D v1](https://arxiv.org/html/2604.14626v1)的 INT8/G32、MSB4/LSB4 分支只相对该量化 target 建立验证合同，非原始浮点模型无损；GPT-OSS 的 MXFP4 experts 不使用相同 bit 轴。证据来自 ASAP7 synthesis 与 Duplex/Ramulator cycle simulation，非硅或生产SLO测量，量化 SD 也有低于1×的配置。格式不相容、快存不足或合并成本超出收益时，独立 artifact 与 target-only 路径仍合理；第48章继续拥有 proposal/acceptance 原理，本节只拥有存储表示与执行数据通路。<!-- source-family:SF-2026-ARXIV-2604-14626 -->

### NPU Static Quantization 需要把 Integer-only Boundary 编进 Artifact

高保真 PTQ 若依赖 runtime calibration、动态 scale 或浮点 fallback，在通用 GPU/CPU 上容易部署，却可能不符合只接受静态 integer graph 的 NPU。对应分支要在 build-time 固化 scale、zero-point、operator coverage、requantization 与 layout，使 runtime 不再猜测量化状态；converter 拥有整数图与 unsupported-op report，device runtime 只执行已签署 artifact。

这用更窄的动态范围、校准偏差和 backend-specific graph 换可预测的 NPU 执行；任一算子回退浮点、scale overflow 或图重写不一致，都可能让“全静态”声明失真。GPU 浮点或 mixed-precision path 在模型变化快、NPU coverage 不足时仍更稳。`arXiv:2605.20295v1` 的 §4、§5 与 Appendix H 只支持其 fully static integer quantization 和受测 on-device NPU，不证明其他 NPU、模型或 workload 获得相同质量、内存或 latency。

<!-- source-family:SF-2026-ARXIV-2605-20295 -->

### MoE 的 Calibration Identity 必须覆盖 Expert Activation Distribution

Dense 模型用 token-average calibration 估计一组层级 scale，在 activation 分布均匀时最简单。MoE 改变了采样单位：router 让不同 expert 以不同频率接收 token，平均校准集会被高频 expert 支配，低频 expert 的 outlier 与误差可能在离线均值中消失，却在特定领域请求中集中暴露。

<!-- semantic-body-binding:SF-2025-ARXIV-250503804-MOEQUANT:start -->
因此 quantization artifact 除了 bit-width、scale 与 calibration corpus，还应绑定 router/expert identity、per-expert activation count 和覆盖阈值。Expert-balanced sampling 可以提高低频路径覆盖，affinity grouping 可以共享相近 expert 的 scale/kernel，但二者分别增加校准成本、grouping drift 与 layout complexity；统一 bit-width 在 expert 行为接近或证据不足时仍是更容易验收的 baseline。MoEQuant 的实验只证明作者模型族、数据集、bit-width 与硬件合同中的质量—内存结果，不证明所有 expert 都应使用同一策略，也不证明端到端 serving 必然加速。
<!-- semantic-body-binding:SF-2025-ARXIV-250503804-MOEQUANT:end -->


#### Analog CIM 的 MoE 校准要同时修 Expert 与 Router

在数字执行上沿用 clean-trained router，只校准权重或 activation scale，默认噪声不会改变 expert 相对选择；analog CIM noise 会同时扰动 expert 输出和 router logits，进而放大 load imbalance。部署 artifact 因而需要把噪声模型、expert replacement、router calibration、placement 和 routing histogram 绑定在一起，校准器只能提出补偿，release gate 仍根据质量与负载证据决定启用。

联合补偿提高受测噪声下的稳定性，却增加备用 expert、校准数据和硬件特定状态，也可能随芯片老化或 workload 漂移失效。噪声低、数字 fallback 充足或 router 稳定时，普通 per-expert calibration 仍更简单。`arXiv:2605.11800v1` 的 §2–§4 与结论只支持其 real-chip-calibrated noise、模型和实验，不代表所有 CIM 或生产流量。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-11800 -->

### Fractional Precision 只有落到 Physical Layout 才是部署预算

整层统一 bit-width 在模型、shape 与设备稳定时仍是最容易验证和部署的方案；问题出现在内存预算落在 W3 与 W4 之间，而少量 activation-salient channel 又确实需要更高精度时。只给每个 channel 分配 2/3/4/8/16 bit，得到的只是逻辑预算：若 Runtime 需要逐元素分支、反复 requantize 或搬运不规则 layout，理论节省会被控制流和内存流量返还。

因此 fine-grained quantization 必须继续经过一个物理实现链：`saliency + average-bit budget → CPU-aligned precision palette → bit-homogeneous block clustering → compatible permutation propagation → generated SIMD/LUT kernel → measured bytes, latency and energy`。Compiler 拥有 permutation、block layout 与 kernel selection，量化 artifact 必须同时版本化 calibration、bit map、layout 与 target ISA；只有实际 backend 能直接消费该 layout 时，fractional bit budget 才成为可执行的部署预算。

这条路线用更精确的 capacity fitting 换取 compiler complexity、专用 kernel surface 与跨 operator permutation 约束。规则 shape、预算充足或缺少异构低 bit kernel 时，uniform per-layer precision 仍更稳健。作者在三类 CPU、batch=1 与给定模型/任务上的结果只支持该 contract 下的可行性；nominal average bits 不能外推为任意硬件上的物理 footprint、latency 或 energy 收益。

Recurrent state 的精度预算还取决于误差写入之后会存活多久、怎样被未来 query 读出。同样的单次舍入误差，较弱 decay 或更频繁 writeback 可能使累积压力不同；在 stationary、外生输入和独立零均值噪声等条件下，可用 observability Gramian 描述未来 readout 的 expected error，再与归一化数值 range 共同提出逐行 bit allocation。它细化误差预算的来源，不改变前面的物理 layout 契约；连续高率解经过取整、截断与范围估计后，仍只是低位整数分配的代理。

平均 erase 率不能代表每个误差方向：与反复写入 key 正交的误差可能长期不被擦除，deterministic rounding 的相关性也违反独立噪声前提。EMA、scale 与 bit-map metadata 必须计入存储和执行；作者 fake-quantized state 在部分 model–budget 切片不如 range-only 或其他格式，检索仍低于 FP32，而且没有真实 packed kernel 计时。因此不以 Gramian 分数认证任务质量或 serving 加速；工作负载、writeback cadence 或敏感方向失配时，保留 uniform precision 或高精度状态，并以实际质量与物理成本共同验收。[原文 §2–6](https://arxiv.org/html/2609.30950v1) <!-- source-family:SF-2026-ARXIV-2609-30950 -->

### 量化验收不能只看平均分：逐例一致性与分布漂移

当上线判断只关心平均 perplexity 或 task accuracy 时，aggregate metric 是便宜且合理的 baseline。但相同平均值可能来自不同样本的正确与错误互相抵消；对于需要可重放、路由或安全审计的系统，“总体分数没变”并不能证明量化前后的逐例行为等价。

量化 acceptance contract 因此应从单一 aggregate score 演进为三层证据：

```text
aggregate quality / perplexity
→ per-example correctness agreement
→ internal distribution drift + workload-slice release gate
```

逐例 agreement 说明决策是否发生交换，attention/logit 等 distribution diagnostics 帮助定位漂移发生在哪里；二者都不是普适安全证明。Release evidence 必须绑定 checkpoint、quantizer 与 scale semantics、runtime/hardware、输入输出 slice 和 evaluator。不同 checkpoint、校准集或 kernel 更换后，旧阈值需要重新验证。

更多诊断带来额外推理、存储和 evaluator 成本，也可能在未覆盖 slice 上漏检。作者对四个模型、llama.cpp 量化配置和离线数据集的结果不能推出通用“安全 bit-width”；低比特方案仍可在自己的 workload contract 内通过独立校准后成立。量化机制与 execution artifact 由本章拥有，跨 slice calibration、证据保留与 release governance 交给第 66 章。

逐例退化被发现后，还要分清是信号仍可被读出、只是沿层传播衰减，还是接收较精确信号的组件也不能正常处理。层内线性 probe 只能给出“在该位置可解码”的线索，不能证明模型实际使用了它；需要在同一失败样本集合上配合参考 activation 局部替换、消融与敏感层精度保护，检验输出是否随干预恢复。前一种情形可尝试局部提高精度或校准，后一种情形不能靠无条件叠加补偿放行，应回退更高精度，或另行训练、重建执行 artifact 后重新验收。这比只看总分或统一加 bit 更能定位修复责任，但增加逐层实验成本，也可能把 probe 的相关性误判为因果。<!-- source-family:SF-2026-ARXIV-2604-19884 -->

受限研究中的“4-bit 错误样本基线为零”来自事先选取 FP16 正确而 4-bit 错误的条件分母，不是总体准确率；部分修复还提高了平均 bit 数并调整放大系数。所测 2-bit 干预失败不能推成所有 2-bit 格式不可修复。发布时仍应把模型、量化法、校准集、条件样本与实际存储/执行预算一起记录；未在同预算、同 workload 上复验的补偿只是一条实验分支。<!-- source-family:SF-2026-ARXIV-2604-19884 -->

输出分布也可以反过来指导离线精度分配，而不只充当发布后的漂移诊断：在固定参考模型与校准输入上，逐次只量化一层，比较参考与候选的 softmax 分布，再按该扰动排序给敏感层更高位宽。原始 logit 的 SQNR 与概率分布距离不是同一对象；KL 的方向、参考分布及比较的 layer 配置必须冻结。交叉熵等于参考熵加正向 KL 的身份，只在采用同一个参考分布的期望下成立，不能直接把真实测试标签分布替换成 teacher 分布，也不能据此证明反向 KL 的经验排序必然最优。<!-- source-family:SF-2026-ARXIV-2604-13440 -->

逐层扰动扫描增加离线前向、输出统计和缓冲成本，却可能在混合架构中提供比统一位宽更细的质量预算。它仍只是 allocation proposal：校准集之外的逐例行为与实际 kernel 必须各自验收，Q/DQ 图也不证明设备执行了对应的原生低位宽指令。作者的混合 SSM/Transformer 与 Lunar Lake/OpenVINO 配置比较存在模型和执行配置差异，不能把其结果解释成纯位宽因果或普遍 Serving 收益；输入输出长度、并发和 SLO 未披露时不补造在线合同。扫描预算不足或排序不稳定时，统一精度、较粗敏感度分组及更高精度回退仍合理。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-22237:start -->
加密推理又会改变验收目标：FHE-only runtime 只能高效执行加法与乘法，因而常在 activation interval 上局部拟合 ReLU；但当主要成本来自 polynomial depth、发布真正关心的是冻结 classifier 的最终 logit order 时，可以在声明的 calibration set 上直接拟合 decision inequalities。Calibration owner 版本化样本、margin 以及 exact、reduced-hull 或 soft regime，compiler/FHE runtime 拥有 coefficient quantization、CKKS precision 与 circuit cost，release owner 仍需检查 unseen slices 和 ground-truth quality。

只有 positive-margin regime 能对 calibration decisions 给出 exact certificate；reduced-hull 与 soft-margin 是近似替代，calibration agreement 也不是未见输入正确性或端到端 confidentiality。二次多项式可以减少 encrypted multiplication 与 modulus levels，却增加 calibration dependence、margin/outlier sensitivity、系数量化和 CKKS 数值状态。可行性、未见切片、量化或数值 Gate 失败时，应回退高阶近似、hybrid MPC/comparison、重训，或拒绝发布，不能把浅层 frozen head 的证明外推到任意深网。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-22237:end -->

逐例交换还需要一个能解释风险变化、但不冒充正确性证明的局部量。量化前的 decision margin 在同一模型、同一位宽与同一 decision family 内，可用于估计扰动把原决定推过边界的概率；不同 family 还可能存在方向性偏移，因此 tool call、拒答与普通选择不能共享一个阈值。Margin 只是经本模型本配置校准的 risk sensor，不是跨模型 certificate；极低位宽下表示本身失真时应回退逐例回归和端到端 effect 测试。

<!-- source-family: arxiv:2608.06564v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: quantization-margin-as-calibrated-decision-risk -->

### 规则码流与自适应重建可以分离

非均匀量化不必要求物理码流也完全不规则。部署 artifact 可以保存规则 packed magnitude codes，再用少量 shape/scale metadata 将它们映射到单调、可自适应的重建 levels；这样在保留直接 kernel 消费能力的同时，适配权重分布。代价是重建参数、group size、activation path 与 kernel shape 一起进入版本身份，而且规则码并不自动保证 downstream quality。硬件缺少对应 kernel、shape crossover 不成立或质量回归失败时，uniform quantization 仍是更简单的分支。

<!-- source-family: arxiv:2608.06763v1; daily-trace: papers/2026/08/10/README.md; semantic-body-binding: regular-packed-codes-adaptive-reconstruction -->

数值验收还要区分“允许的误差”与“能检测出的错误”。两个 kernel 即使各自可复现，也可能因 epilogue 的
scale 运算与舍入顺序产生不同输出；若合法差异与错误舍入都落在一个 BF16 相邻值间距内，容差检查会同时
放过二者。通过只说明已测输入上的差异受限，不证明 bitwise equality 或 kernel interchangeability。
因此应向 verifier 注入已知故障，分别记录适用条件、检测能力与未覆盖情形，而不只用正确实现测试它。

若业务确实要求逐位一致，可以收紧数值实现合同，而非把容差机械改为零。例如，在整数累加无溢出、进入
浮点时可精确表示、缩放不进入异常数值范围等前提下，power-of-two scales 可消除特定 epilogue 的运算自由。
但修改 scale 必须从原始权重重新量化，不能留下按旧 scale 编码的整数权重；除法 dtype、scale 生成规则和
kernel identity 也要共同冻结。该分支在受测 Qwen3 与 CUTLASS/Triton 配置中支持确定性，不保证其他实现或
所有输入；质量代价与吞吐仍须另测。[对应纠错研究](https://arxiv.org/html/2609.00363v1) 已撤回其前作
“容差检查决定可互换性”的强表述，不能继续把错误的 weight–scale 配对当作约束本身的质量成本。

单个 kernel 的逐位一致仍不足以保证整个服务引擎不受调度影响。更强的执行合同是：固定权重、dtype、部署环境与每请求 sampler 初态，同一 prompt 在不同 batching、chunking 或 cache-hit 路径下，输出的每请求 logits/token trace 应前缀可比较；它不要求不同终止时刻完成同样多的工作。为此，kernel 特化与 tile 选择只依冻结环境，engine 同时维护等价于 cold-prefix 计算的 retained KV、逻辑位置到物理 slot 的映射以及共享 prefix 不可变、私有 suffix 写隔离。hash 只提出 cache 候选，真实 token、depth 与 parent lineage 还须验核；lookup 要在本轮新页发布之前，避免当前调度改变可见缓存集合。

只有 relational kernel 合同与 engine 状态归纳合同相接，才能把调度自由与数值自由分开。[Vosti 的有限验证](https://arxiv.org/html/2609.38981v1)依赖 translator、合同对应、编译/GPU 执行等可信边界，其 input-dependent finite 假设没有运行时检查；determinism 也不是完整数值正确性、liveness 或跨硬件、dtype、compiler 的通用保证。冻结特化、禁用未验证 autotune/fallback 可以限制优化空间，适合 Decode 的小 tile 还可能损失 Prefill 性能。若需新 dispatch，应先验证合同而不是从局部无 mismatch 推全输入保证；要求不成立时保留原实现及明确的容差/重复性验收，不把它们混称已认证的逐位确定引擎。<!-- source-family:SF-2026-ARXIV-2609-38981 -->

调度确定性还没有限定一个 output 允许依赖哪些输入。即使执行 plan、shape 与重复结果固定，较早位置仍不应因替换未来 text 或另一请求的 text 而改变；这是 causal prefix invariance，不只是相同输入的重复性。跨 token row 的 fast matrix multiplication 在实数算术中可以混合再消项，但中间低精度舍入可能留下其他 row 的残差，Attention 的 causal mask 无法约束此前 linear path。因此 accuracy 或 perplexity 恢复、固定输入逐位复现都不能认证这项隔离，也不能从某种受测 FP8 schedule 的反例推所有低精度 kernel 都失效。

可先定义 row-local 的量化 reference：每 row/column 的 scale group、code bounds、输出 rescale 与累加顺序都是 operator 身份。一个条件分支用 exact integer mix/cancel 保持该 reference，但 code/block sums、所有 partial sums 均须落在 accumulator 的精确范围，每次 call 不能跨不同 scale group，最终转换和顺序也不能改变。[受限有界整数证书](https://arxiv.org/html/2609.39816v1)支持的是同量化 operator 逐位相同，不是与原 BF16 模型等价；缩小 code range 可能损伤质量，扩范围的 overflow correction 又增计算。作者受测 H20 kernel 还比经典 int8 更慢，乘法数量减少不是墙钟收益；row/prefix 依赖、overflow 或 scale-group 条件不满足时，保留经典 row-local kernel 并独立验质量、隔离与运行成本。<!-- source-family:SF-2026-ARXIV-2609-39816 -->

数值误差可容忍的生成任务还产生另一种恢复分支，但不能与精确重算混为一谈。在假定 memory 读取无错误、计算 bit-flip 符合给定模型的 diffusion accelerator 中，可以保护敏感 timestep/layer，只在其余位置采用较激进的电压/频率；ABFT checksum 检测大误差后，用较早 timestep 的 activation 覆盖被标位置，而不是重算当前正确值。稀疏恢复再配合周期性 offload 与按 tile 连续 repack，减少 checkpoint 写入和零散读取。

这是一种依靠生成过程容错的近似恢复：checksum 可能漏掉相消错误，旧 activation 不是当前真值，较大检测阈值和较长保存间隔可能损害质量。其 [DRIFT 证据](https://arxiv.org/html/2604.09073v1)来自 error injection、14nm 综合与 cycle simulation，不是生产 GPU 上已验证的 DVFS 收益；存储故障、严格数值正确或容错模型不满足时，名义运行点与精确重算仍更可靠。只有把保护区、错误模型、恢复语义、质量与真实端到端成本共同验收，执行计划才可选择这一近似分支。<!-- source-family:SF-2026-ARXIV-2604-09073 -->

数值计划还可能改变 Attention 内部的瓶颈分工。tile matmul 已高效时，每块重复 rowmax 与 rescale 会形成 vector 工作；一个分支先预计算 key-block 的 signed-absmax 摘要，为各 query row 初始化 shift，再优先处理 sink/local 块更新真实最大值，其余块冻结 shift，仍累计所有块的 softmax 分母与 PV。它减少的是统计重算，不是删除 Attention 证据；若另加 block skipping，就必须作为另一份有损合同验收。

实数算术中共同 shift 可以抵消，不意味着有限精度下指数范围和累加误差安全：signed 摘要并非 score 最大值的保证上界，预计算、重排及摘要维护也有成本。作者受限模型任务存在 HumanEval 退步，未披露设备型号与生产 SLO，不能由算子吞吐推普遍等质量或端到端收益。数值范围或任务回归不通过时，逐块更新 rowmax 的原 online softmax 仍是可靠基线；只有把 dtype、输入范围、输出质量和真实运行成本共同冻结，才允许选择这种 vector-statistics 分支。<!-- source-family:SF-2026-ARXIV-2604-12798 -->

共享 latent 同时用于 K 与 V 时，scale 的归约位置还会改变数值计划。MLA 可让 content latent 采用 per-token FP8，而 RoPE 分量保留 BF16；QK 路径先把两个分量放入同一 score 单位，再反量化后进入 softmax。但 V 的 per-token scale 位于 PV 的 sequence reduction 轴上，不能在 GEMM 后用一个公共 scale 还原。一个分支把该 scale 乘入对应 probability，再重新量化供 PV 消费，同时保留真实 softmax 分母；scaled probability 不是新的归一概率分布。

跨 tile 的 online maximum、分母和输出 accumulator 因而必须各自维持一致单位，rescale 也要覆盖新引入的量化因子；双 buffer 可以隐藏转换，却须保证下一块 probability、scale 与 PV 消费的 readiness 对齐。更多转换和状态增加 rounding、同步与实现成本。受限 [SnapMLA exact-v1 §3–4/Appendix C](https://arxiv.org/html/2602.10718v1) 仍有任务质量退步，BF16 RoPE 不意味着整个 MLA 无损，较大允许 batch 的吞吐也不是同 concurrency/SLO 提升。质量、单位一致性或转换净收益不通过时，保留原 BF16/mixed MLA；粒度、scale 轴、softmax 状态与 buffer 调度应共同进入 artifact，而不能只更换 KV dtype。<!-- source-family:SF-2026-ARXIV-2602-10718 -->

### 量化前先诊断分布：保持代数等价不等于保持量化结果

对 Attention 的 Q、K 使用同一套对称量化路径，前提是二者的 channel distribution 与 outlier structure 足够
接近。这个基线实现简单，在 outlier 不稳定、calibration 样本不足或目标硬件没有专用低精度路径时仍然合理。
约束变化发生在某些 QK-RMSNorm 模型中：K 出现跨 head 较稳定的 channel outliers，而 Q 没有同样结构。
此时直接降低 QK 精度，会让少数 K channels 主导 scale，同时压缩大量正常值的有效分辨率。

更稳妥的演进顺序是先诊断，再决定是否进入专用路径：

```text
calibrate Q/K channel statistics
→ gate on the observed asymmetric K-outlier regime
→ apply a diagonal transform to Q and the inverse transform to K after RoPE
→ preserve the unquantized QK score algebraically
→ quantize Q/K with the target low-precision path
→ make softmax numerator and denominator consume the same quantized P
→ fuse normalization into the PV path where the backend supports it
```

若对同一 channel 使用 `Q' = QD`、`K' = KD^-1`，则未量化时 `Q'K'^T = QK^T`。这个恒等式只说明
paired transform 不改变原始 score，**不说明量化后的 Q、K 或最终 attention output 与高精度完全相同**。
同理，让 softmax numerator 与 denominator 复用同一 quantized probability tensor，可以消除一种 coherent
radial error，却不能证明 Q/K/V 的剩余误差彼此独立或对模型质量无害。

这条分支新增 calibration dataset、gate threshold、paired-transform revision、P data-flow semantics 和 backend
fusion 作为 artifact identity；条件不成立时必须回退到普通量化或更高精度。现有公开案例只覆盖五个模型，
目标为 Ascend HIF4，尚无公开 on-hardware kernel timing、实现 artifact、batch/concurrency 或生产 SLO，因此
应保持 `Experimental`：它提供的是“分布诊断 → 代数等价变换 → 校准门控 → 量化数据流一致性”的长期机制，
不是已经证实的通用 serving 加速结论。

分布诊断还有另一条轴：**channel 统计与 sequence tile 的误差敏感性不是同一件事**。在所测 causal attention 中，近对角 tile 可以保留较高精度的 QK，远处 tile 采用更低精度，V 仍保留高精度；但距离只是一种局部敏感性代理，不能保证远距离检索不受损。量化、双格式 packing、scale 转换和 attention kernel 需要联合安排，否则为了省下 QK 计算而增加的预处理会吃掉收益；继续使用 online softmax 也不使量化后的结果精确等价。<!-- source-family:SF-2026-ARXIV-2604-03950 -->

因此 Numeric Plan 要分别声明位置分区、精度和转换成本，并以长距检索等敏感 slice 验收，而不只看平均分。作者 B200/Triton、两款 Llama 和 2.5K～30K LongBench 输入中的部分检索任务明显退步；这些 kernel 与质量结果没有建立生产 batch、concurrency 或 SLO 保证。位置代理不适用、转换未融合或关键质量受损时，同精度 attention 仍是更稳健的分支。

整数attention的执行计划不能只把QK与PV换成低精度dtype：跨tile的row maximum必须处于可比较单位，指数近似、累加器范围和scale释放/重标定也要共同定义。否则每个局部tile看似合理，online softmax的全局归一却可能使用不一致的数值状态；scale生成、转换和查表成本必须进入kernel预算。

更少位数以校准和近似误差换吞吐，整数指数或累加不能借实数monoid得到无误差保证。受限QFlash只验证单设备视觉attention若干shape，其余层仍是浮点，质量存在退步，不能外推LLM服务SLO或把对整数基线的倍率当对FlashAttention的倍率。数值检查、目标任务质量或转换成本不合适时，保留FP16/mixed attention。 [原文必要机制与限制](https://arxiv.org/html/2604.25306v1)。
<!-- source-family:SF-2026-ARXIV-2604-25306 -->

#### Rotation Scope 与 Quantization Group 必须共同进入 Numeric Plan

选择旋转之前，应先区分优化依据来自 weight 还是 activation。一个可融合的权重变换分支，用旋转后权重的第四次矩作为极值的平滑代理，离线优化部分正交变换，而不为这个旋转学习步骤收集输入或执行模型 forward。它减少的是该步骤的数据依赖，不表示接下来的 GPTQ 重构、activation 定标或整套 PTQ 都无需 calibration；低阶统计与局部误差界也不能自动授予全网络质量。

代理目标是否有效，还取决于目标位宽：减小 weight outlier 的旋转在所测 W4A8 中可改善质量，但 W4A4 的 activation 误差可改变甚至反转选择，简单 RTN 的对照也不必沿用同一排序。[OptRot 的必要机制与反例](https://arxiv.org/html/2512.24124v1)因此支持把旋转目标、weight/activation 位宽、quantizer 与实际 calibration 一起绑定，而非先选“最小 outlier”再任意换格式。优化步数、可选学习率搜索及后续校准仍有准备成本，作者质量结果不证明硬件吞吐。代理或关键任务不匹配时，保留原旋转、代表性校准与局部高精度，不用 data-free 名称跳过 artifact 验收。<!-- source-family:SF-2026-ARXIV-2512-24124 -->

在选择 rotation scope 之前，还要确认所有 token 是否适合同一个 activation 变换。图像与文本、masked 与已揭示 token 可以共享静态 weight，却具有不同的 activation 子空间。常规可逆变换要求 activation 侧与 weight 侧互为逆矩阵；一个更窄的替代分支保留共同基底，为两类 activation 分配不同的专用基底、屏蔽另一类的部分，weight 只保存合并后的统一变换。未量化等价要求相互专用子空间确实位于另一类 activation 的零空间；这不是仅靠 token 标签就成立的恒等式。

实际量化将严格投影条件转成需要校准的近似，专用维度、token 分类和 clipping 共同影响误差。删除过多维度会损害质量，对所有层强制同一隔离比例也可能劣于统一变换；未量化的代数等价更不授予量化后的无损保证。[FreeAct v1 §3–4](https://arxiv.org/html/2603.01776v1)仅支持所测扩散语言与多模态模型中的这一条件分支，clipping 消融还显示收益不能全部归于变换，硬件 kernel 共设计仍属后续工作。分布难以分离、类型路由失准或专用执行成本过高时，统一 rotation、较高精度与原 calibration path 应继续保留。<!-- source-family:SF-2026-ARXIV-2603-01776 -->

变换选择还应先分开两个误差来源：数值是否集中在少数极端坐标，以及 activation 与 weight 的二阶变化方向是否匹配。对 uniform integer quantization 且 clipping 可忽略的近似分析，二者共同影响线性层 SQNR；正交旋转可以改善前者，却不改变该分析中的 alignment。因此压低 outlier 不代表已修复所有误差。一条条件分支先依据两侧协方差构造非正交的方向对齐变换，再用 Hadamard 改善浓度，同时对 weight 使用逆变换以保持量化前的线性运算。

协方差最优的全秩变换增加昂贵的在线矩阵乘法，实际可用 block-diagonal 近似，但这牺牲了全局对齐，block size、校准分布和变换开销必须进入 Numeric Plan。[CAT v1 §2–4、§6–7](https://arxiv.org/html/2603.04359v1) 在统一校准与低比特配置下支持有限模型质量对照，明确未证明最优的 speed–accuracy 取舍；SQNR 也不是下游质量或端到端 serving 时间。方向收益不足、协方差漂移或变换难以融合时，较简单 rotation、固定量化或较高精度仍是合理分支。<!-- source-family:SF-2026-ARXIV-2603-04359 -->

全局 rotation 在 coarse group 下简单且稳定；group 变细后，跨组扩散的 outlier 可能反而破坏局部分布。执行计划应把 rotation scope、group size、outlier permutation、scale/zero-point dtype、accumulator 与 output dtype 一起版本化。局部 rotation 或 scope/group 解耦只在校准收益覆盖 permutation、metadata 和专用 kernel 成本时成立；缺少目标硬件实现时，RTL/model 结果不能外推为 GPU 或生产 tail latency。

Rotation 次数也不能脱离 quantizer 的统计假设单独选择。对 scalar quantization，连续两次带随机符号的 Hadamard transform
可在给定理论条件下让固定坐标更接近高斯；对固定有界 block 的 vector quantization，两次变换仍可能保留块内条件相关，
需要第三次变换才得到更强的 covariance 衰减保证。执行计划因此应把 quantizer family、block boundary、transform count、
随机种子和适用维度共同冻结，并可用 `l3` 与 `linfinity` moment check 决定是否升级变换次数。

额外 transform 会增加搬运、随机状态和 kernel 成本，theorem 也只约束声明的 fixed block/codebook 与渐近误差项；它不证明
任意 adaptive codebook 或真实 backend 更快。统计检查不通过、维度不兼容或执行成本无法摊薄时，应回退更高精度或较简单
rotation，而不是为了满足高斯假设继续堆叠算子。这里沉淀的是“数值假设必须进入 Numeric Plan”，不是未经实现验证的
Serving 加速结论。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06014 -->

共享 scale 还使误差不只属于 outlier 本身：它抬高一组的量化步长后，同组普通值也会失去分辨率。因而在格式与
group size 固定时，可以用校准统计为 outlier 选择低幅度 companions，对 activation 与 weight 做配对 channel
permutation，再在新顺序下修复 weight 误差。高精度线性运算仍等价，低精度舍入却已改变；RMS 只是低成本选择
代理，偏好 activation 的顺序可能损害 weight 量化。只有重排能与 normalization/quantization 融合、额外 gather
没有吃掉访存节省时，这条分支才值得采用；分布不稳定或缺少相应 kernel 时，固定分组仍更简单。现有 NVFP4
实验只支持受测 Llama/Qwen、原生 16 值分组及 RTX 5090 实现，不证明其他 group 的模拟结果有同样硬件收益。

旋转还应服务于具体 quantizer，而不只是压低最大值。对 uniform scalar bins，重构值位于 bin 中点；非均匀输入在 bin 内的条件均值未必等于中点，因此没有明显 outlier 也可能存在重构偏差。可先用 block-wise 正交变换调整分布，再选择是否用 block-output reconstruction loss 学习额外全局反射；前者是统计整形，后者支付校准训练成本，二者不能混称无需优化的一次变换。<!-- source-family:SF-2026-ARXIV-2604-04013 -->

该分支把目标从“压小极值”推进到“匹配重构假设与输出损失”，同时引入校准失配、额外变换和硬件融合成本。作者 Llama、W4A4/W6A6 的质量结果和 RTX3090 的 layer-wise prefill 计时不证明完整 Serving 加速；无需训练的版本与 fine-tune 版本也不能共享同一准备成本。校准收益小、部署变换昂贵或输入分布漂移时，较简单 rotation、固定量化或较高精度仍合理。

### 二阶敏感度把 Output Gradient 带进量化 Artifact

只根据 activation range 或 weight magnitude 分配 bit，假设输入统计足以代表输出损失敏感度；当不同输出方向的
误差代价差异很大时，这个近似会把相同幅度的扰动视为等价。一个更昂贵的分支用 Kronecker-factorized curvature
分别近似 activation covariance 与 output-gradient covariance，再对 weight 做两侧预处理并按 trace/sensitivity
分配 mixed-bit budget：

```text
calibration activations + output gradients
→ input/output covariance factors
→ two-sided weight preprocessing
→ block-wise sensitivity and bit allocation
→ quantized artifact
→ executable-kernel and end-to-end validation
```

它把 calibration dataset、loss/objective、gradient capture、factorization 与 bit map 都纳入 artifact identity，成本和
数值风险显著高于 activation-only 方法。Artifact perplexity 改善不等于目标 backend 已有更快 kernel；若 gradient
采集或矩阵分解成本无法摊薄，简单 channel-wise/activation-aware quantization 仍更合适。

Weight 与 activation 都量化时，保护对象还可以是共同的高精度输入子空间，而非只给敏感 weight block 更多 bit。联合输出误差 surrogate 将 activation covariance 与 weight 方向一起用于选定固定 rank 的共享子空间；W/A 残差由低精度路径消费，受保护分量单独保留高精度。这与曲率 bitmap 的精度分配是不同条件分支，不能把联合误差当成两侧误差互不影响。<!-- source-family:SF-2026-ARXIV-2604-26378 -->

该推导依赖 AQNM、零均值/各向同性和小误差一阶近似，丢掉的高阶 W/A 交互不能靠 surrogate 消失。子空间拟合、rank、额外高精度状态和运算均计入预算；作者质量实验没有专门 kernel 就不称实际 Serving 加速。校准漂移或 rank 不足时，应扩大保护、提高精度或回退较简单的 W-only/activation-aware 方案。

保留更多二阶相关性还会引入有限校准样本下的估计方差：更完整的矩阵可能减少结构偏差，却不一定让不同 calibration batches 给出稳定选择。一个更简单的收缩分支只保留各输入通道的平方和作为对角权重，在固定整数码的条件下，用加权 ridge 回归拟合重建 scale 与 offset，再交替执行舍入、裁剪和回归。闭式解只针对固定码的连续子问题，不证明离散码与参数联合优化的全局最优，也不提供任意初始化下的普遍收敛保证。<!-- source-family:SF-2026-ARXIV-2604-13806 -->

因此校准验收要把估计稳定性与最终质量分开：跨批次敏感度排序更稳定是有用诊断，不等于输出质量必然更好；对角化省掉的通道相关性也可能正是重要误差来源。作者的局部相关性观察和受测模型结果只支持这一受限取舍，离线量化时间与质量不等于 Serving 吞吐。额外统计与交替更新应进入校准预算；样本不足或波动大时可采用对角收缩，相关性确实重要且预算允许时仍可扩大校准集、保留更完整曲率或提高精度，不能把低成本近似变成唯一正确路径。

二阶近似也不必与更新策略一起冻结。固定曲率下的解析补偿计算便宜，误差较小且局部近似可靠时仍合理；顺序量化
不断改变当前 residual 后，可以保留粗粒度解析补偿，再用当前 surrogate loss 的梯度调整尚未量化的列，已经量化的
列则保持固定。滑动相邻 block 的损失能纳入有限下游效应，却增加反向计算、optimizer 状态和校准成本。这里动态
更新的是 residual 梯度，不是每步重建 Fisher；SGD 的下降方向分析也不自动保证 Adam 收敛。受测 W4A16 案例支持
改善相对参考模型的分布保真，但 KL 更小不等于任务质量最优，更不等于推理更快；离线预算不足时，原来的静态补偿
仍是有效选择。

### 未来补偿能力决定当前舍入的代价

顺序量化还要区分“尚未量化的列保持不变”与“它们仍可补偿当前误差”。设当前列组为 `G`、未来列为 `F`，局部二阶曲率为 `H`，允许未来列自由作连续补偿时，当前误差 `delta_G` 的最小代价由 `S=H_GG-H_GF H_FF^-1 H_FG` 衡量，而非直接用 `H_GG`；后者会把未来可以抵消的部分也收费。这个 Schur complement 只对 stated 曲率、可逆/正则化及连续补偿子问题成立，未来真实离散舍入并不保证达到该最小值。

因此 scale search 可进一步变成私有轨迹回放：每个候选从同一个 group-entry residual 状态出发，执行实际 GPTQ 顺序舍入与补偿，评估自己的结果，最后只提交 winner 的 scale 和 residual。并行的是候选和独立 rows，不是随意交换具有依赖的列；败选候选不得污染共享状态。它用额外校准回放换取与真实离散轨迹更相符的选择，仍受代理损失、校准漂移与搜索预算限制；搜索更宽也不必质量更好。[SchurReplay 的指定 W4A4 对照](https://arxiv.org/html/2609.36654v1)不证明全网络最优或运行时加速。预算不足、曲率不稳定时，静态 scale 与原解析补偿仍合理。
<!-- source-family:SF-2026-ARXIV-2609-36654 -->

### Quantization Bit Budget 应按矩阵方向敏感度分配

对所有矩阵和方向使用同一 bit width 最容易部署，却会在低敏感方向浪费码率、在高敏感方向造成误差。Waterfilling-style allocation 可依据方向敏感度分配精度，使 quantization policy 与具体 weight matrix、分解和目标硬件绑定，而不是只记录一个全局 INT4 标签。<!-- semantic-body-binding:SF-2026-ARXIV-2605-13768 -->

敏感度估计、非均匀 layout 和专用 kernel 会增加编译与运行时复杂度；Llama-3-8B 的 weight-only 结果不构成跨模型硬件结论。没有可执行 kernel、校准漂移或端到端质量退化时，应回退统一量化、提高 bit width 或保留关键矩阵高精度。

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

#### Embodied phase 可以选择精度，但不能接管物理安全

量化 policy 还可以消费 embodied workload 的阶段信号，但该信号只能决定 execution plan。一个受限分支用上一时刻 action magnitude 区分大幅转场与近目标精细操作，并在预构建的高、低精度 codebook 间切换；只有 indexed GEMM 与 centroid-reuse kernel 直接消费相同 layout 时，名义 bit 数才可能转化为真实带宽收益。

它新增 phase calibration、双 codebook artifact、切换边界和专用 accelerator 依赖。Action magnitude 不是环境真值，也不是物理风险证明；安全关键阶段、相关性不足或缺少匹配 kernel 时仍应回退固定精度。第 26 章继续拥有 environment transition 与 physical safety，本章只拥有精度、layout、kernel 与 backend contract。

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

补偿分支也不一定要使用更高精度或低秩矩阵。在同格式矩阵乘可高效执行、少数激活通道主导量化误差时，另一分支先量化主激活，再把选中通道的激活残差量化成同一格式，并复制这些通道对应的权重列。这样把 reduction 维从 `K` 扩为 `K+S`，用一次同格式 GEMM 累加主路径与补偿路径；它补的是激活误差，不会自动消除权重量化误差。逻辑拼接仍须匹配真实 packing：主通道与补偿通道的交错布局、scale 和权重排列必须一致，不能直接交给任意支持 FP4 的 kernel。<!-- source-family:SF-2026-ARXIV-2601-07475 -->

这条分支把高精度修正的成本换成额外权重列、校准选择、在线 reorder 与残差量化；相对未补偿的同格式基线，内存与延迟也可能增加。有限 prefill 矩阵和模型质量对照不能授予 decode、并发或完整 Serving SLO；激活标量误差界也不是整网任务等价保证。分布、通道布局或硬件改变时应重新校准并验证质量；补偿不值得、packing 不兼容或质量回归时，未扩展的量化路径、已有高精度修正分支和 dense matmul 都仍是合理回退。

在考虑输入相关的动态 rank 之前，静态低秩压缩也应先问“哪些通道不应该被一同近似”。非零激活函数使低幅度通道并非恒为零；直接硬剪与低秩重构不是同一个误差假设。一个条件分支保留少量高贡献 FFN 通道的原权重，剩余块再按校准 activation statistics 做 whitening 与 SVD；在共同内存预算下，给不同矩阵分配 rank，而不是每层机械使用同一比例。<!-- source-family:SF-2026-ARXIV-2604-03258 -->

分层预算需要记录原块/近似块的切分、校准分布和可执行 rank 粒度；按奇异值能量贪心分配只是声明代理目标的次优策略，不能保证任务质量全局最优。受测配置也有自适应 rank 比均匀 rank 的 perplexity 更差的反例。保留原块会新增双路径和融合压力，校准、分解及矩阵微基准不证明完整服务更快；各通道敏感性相近、预算分配不稳定或 backend 无法有效执行时，统一 rank 或原始 dense matmul 仍更简单。

单一 SVD 子空间便于固定 rank 和执行布局；若希望同一字典承载不同矩阵的稀疏组合，另一离线分支是在 activation-whitened 空间约束字典正交。固定字典时，系数投影后 hard threshold 给出稀疏重构子问题的解；固定系数时，字典由薄 SVD 的 Procrustes 更新得到。这两个条件子问题各自可解析求解，不表示联合目标凸、全局最优或整个压缩一次完成：[受限正交字典实验](https://arxiv.org/html/2602.15200v1)主配置仍交替20轮。原坐标归一化权重的全局奇异值池用于分配预算，whitening 中的谱用于重构误差，两者不能当作同一个重要性指标。

字典路线新增校准 Gram、正交约束、稀疏系数与 mask 的状态，预算要同时计字典、非零值和表示开销，而非只数保留参数。Gram 不稳定或校准分布失配会使局部重构目标失去代表性；不同压缩论文的 remapping、复现与评价协议也不能合为普遍获胜。离线质量改善并未证明有适配 kernel 的端到端加速，字典驻留、稀疏访存与组合执行仍须单独验收。没有匹配 backend、质量 Gate 失败或优化收益不足时，原有 SVD、保守压缩与 dense matmul 继续成立，不由两个闭式更新消除执行成本。<!-- source-family:SF-2026-ARXIV-2602-15200 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-08568:start -->
静态 SVD rank 在 workload 稳定时简单、可复现；若不同 prompt 实际需要的子空间秩差异很大，固定 rank 会在质量与内存带宽之间长期浪费。一个条件分支让 router 只在 prefill 根据输入提出 rank pattern，decode 复用带模型、prompt family 和版本的已提交 pattern；execution-plan owner 验证 pattern 后才能选择对应聚合与 fused kernel，router 本身不拥有质量 verdict。

动态 rank 用更细的计算分配换来路由误判、pattern-cache 失效、额外 metadata 和聚合开销；这些成本可能完全抵消矩阵压缩收益。现有证据只覆盖作者披露的模型、实现、数据和 evaluator，不证明跨硬件、并发或生产尾延迟的普遍收益。输入漂移、cache identity 不完整或 kernel 没有稳定 pattern 支持时，应回退静态 rank 或原始 dense matmul。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-08568:end -->

### 从 Routed Activation Materialization 到 Indexed Execution

MoE 的逻辑语义是 token 选择 expert，但最直接的执行会把 routed activations 按 expert 排列成新的
buffer，再执行 expert GEMM，最后根据 inverse mapping 合并。Padding 或固定 capacity 让 shape 稳定，
实现简单；dropless path 保留全部 assignment，却常把 compact、sort、materialize 和中间激活流量带入
critical path。模型越稀疏，并不意味着这些数据搬运也会自动变少。

固定 capacity 还有一种不由负载预测单独决定的成立条件：后端只接受静态 shape 的执行图。此时 host 可以先把本轮 token–expert assignment 映射到经校准的容量等级，将同等级专家组成固定切片的 dense graph，执行后再按原 routing weight scatter 合并；图的驻留则另按冷热选择 NPU 或预置的 CPU 路径。容量等级、组粒度和图驻留必须联合选择：细组减少 padding，却增加 launch；大组摊销 launch，却可能使图超出后端容量并回退。这里的 CPU fallback 是图的预定 placement，不意味着超出容量的 token 可以临时 spill 到另一处理器。<!-- source-family:SF-2026-ARXIV-2604-18788 -->

静态图容纳不下全部 assignment 时，按 activation saliency 丢弃 overflow 是改变有效计算的有损分支，而不是 dropless 优化；校准分布漂移也会改变 padding 与丢弃率。受测 Apple Silicon / CoreML 的 FP16 MoE 配置中，最佳平均 latency 与最佳 energy 属于不同组合，短 decode 和质量指标的可接受退步不构成并发尾延迟或无损保证。因此采用前应把容量、图大小、校准成本和质量验收共同交给 execution-plan owner；不容忍丢弃或无法维持校准时，保守 padding、较小的静态组或支持动态 shape 的通用后端仍是合理回退。第21章继续拥有 routing 语义，第50章接手 request state 与在线调度，不能由静态图局部收益推断整个 serving 系统更优。

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

#### Token-level Width Routing 也必须编译成 Metadata-aware Kernel

Router 产生的 token×group mask 不应先物化 compact activation。可按 routing column 排序 mask/index，让 kernel 从原始 layout indexed read，并在 block admission、load/MMA skipping 与 scatter epilogue 中消费同一 metadata。Router、indices、kernel config 与 model revision 共同构成 execution identity；unsupported shape、metadata cost 或稀疏度不足时回退 dense kernel。

### Query-specific Approximation Risk 决定稀疏路径是否可提交

固定稀疏率在 query 分布稳定、误差预算宽松时容易编译和复现；同一 context 上，不同 query 的 attention sharpness 与被省略 K/V 的影响却可能差异很大。一个条件执行分支可以先对 context K/V 做 saliency 预选，再由 query-specific sharpness 或 error proxy 提议走 full attention，或走 blockwise zeroth-order Taylor sparse attention。proxy 只拥有路径 proposal；runtime 必须同时检查 shape/kernel support、质量预算与 artifact revision，并由 full attention 保留 correctness fallback。<!-- semantic-body-binding:SF-2026-ARXIV-2605-04569 -->

动态路由把计算留给高风险 query，但新增 proxy calibration、双路径维护、切换开销与漂移后的隐性质量损失。作者报告的 attention-module latency 占比与端到端加速只属于 LIVEditor-14B、其视频编辑 workload、硬件和阈值；“near-lossless”不是跨模型保证。proxy 漂移、unsupported shape、误差预算越界或分支成本超过节省时，应立即回退 full attention。模型章节负责 attention 语义，本章只负责 lowering、kernel path 与最终执行提交。

### Token-level 预算不能由三个独立近似器分别消费

activation sparsity、structured pruning 与 low precision 分别优化时最容易实现，但三者都在消耗同一 token 的质量
余量：attention 少看哪些位置、MLP 跳过哪些结构、剩余计算采用何种精度会相互改变误差。三个局部 controller 即使
各自满足阈值，也可能叠加成不可接受的输出漂移。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-10875:start -->
联合路径把 token/context state、目标 SLO 与可校准 quality budget 交给一个 proposal policy，同时选择 attention
sparsity、structured width/pruning 与 precision；compiler/runtime 只接受硬件支持、metadata 成本可控且通过
reference check 的 plan。policy 拥有候选，不拥有正确性；verifier 和 dense/full-precision fallback 仍拥有 admission。

联合控制能把算力投入更敏感 token，却新增组合 action space、online decision overhead、calibration drift 与难以隔离
的误差来源。训练分布外输入、预算传感器失准、硬件不支持动态 plan 或 tail latency 受 controller 本身支配时，应
回退独立的静态 sparsity/quantization artifact，必要时执行 dense full precision。论文结果只支持其模型、accelerator
与 policy action space，不能把作者质量—算力曲线外推为生产常数。[受限证据：arXiv:2605.10875v1]
<!-- semantic-body-binding:SF-2026-ARXIV-2605-10875:end -->

加密执行会进一步改变 layout 的合法性与通信轴。普通 tensor parallel 可以按数学维度切分；同态 ciphertext 还受 slot packing、RNS modulus 分片与加密算子语义约束。一个受限 Transformer 执行分支先满足 modulus-chain dependency 的一致放置，再在这个前提下保持 token coherence，按这组严格层级联合安排 slice reduction、operator reorder 与跨 GPU 通信；它不是两种布局可任意互换，也不是把明文 graph 的切分原样搬入密文。Compiler 拥有这组物理计划，Security 仍拥有 key、明文边界与威胁模型；二者不能用一个“加密”标志替代。<!-- source-family:SF-2026-ARXIV-2604-03425 -->

这种共同编译用布局转换、密文容量、额外同步与复杂 toolchain 换取通信隐藏，不能推导加密推理已经接近明文服务。作者 CKKS/BERT-Base、2×A6000或4×A100的实验限长序列同态执行，2048输入的端到端成本仍很高；将 ASIC 方法移植到 GPU 的对照也未保留原 ISA/interconnect。密文布局、安全参数或硬件不匹配时，应保留单设备/静态加密计划，或在明确的信任模型下选择TEE、客户端执行等替代；本章不授予任何额外隐私保证，具体责任交给Ch72。

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

这里的 correctness 还要按输出语义分开。确定性 tensor 可以对固定 reference、dtype 与输入合同检查逐元素数值偏差，并拒绝 NaN/Inf；允许局部不匹配的低精度路径则须明确匹配比例等策略，不能只放宽一个全局 tolerance。随机 sampling kernel 的一次 token 输出没有逐元素相等的含义，应另用相同输入下的多次输出估计经验分布、检查 TVD，并拒收本应被 mask 排除的 token。样本数、阈值和合法输出集合必须随验收版本固定；有限频率测试仍不是分布相等证明，失败或合同未覆盖时保留 reference fallback。<!-- source-family:SF-2026-ARXIV-2601-00227 -->

测试的进程与 GPU context 生命周期也是合同的一部分。独立 subprocess 并销毁 context 能缩小状态污染和故障延续范围，却增加 setup/teardown 成本；常驻同一 context 复用更便宜，但必须记录共享状态及恢复边界，而非默认获得同样隔离性。Benchmark 因而应声明 warmup、重复、dispatch/backend state，以及哪些成本被排除；microkernel、harness 开销和真实 model 端到端时间分别验收。通过有限输入测试或观测到很小的 dispatch 开销，都不能推出未知输入正确、任意 kernel 更快或生产 SLO 保证。

### Kernel Verification 需要从孤立输入扩展到 Model–Kernel Interface

只给 CUDA kernel 生成随机 tensor 能发现局部越界，却不知道真实模型会传入哪些 shape、stride、launch config 和动态 buffer extent；只跑端到端模型又难以穷举线程交错和边界条件。更完整的 admission path 先在无 GPU 模型执行中恢复 call graph，把配置决定的固定参数与请求决定的变量分开，再把这些 interface constraints 交给面向 CUDA memory/thread semantics 的 symbolic executor：

```text
model revision + operator call graph
→ model-side shape / buffer / launch constraints
→ kernel symbolic paths and thread-memory checks
→ concrete counterexample replay
→ versioned kernel admission or reference fallback
```

Model probe 拥有可达调用与输入合同，symbolic executor 拥有路径探索，compiler/runtime 最终拥有 admission；任何一层都不能把“未找到 bug”宣称成完备证明。该组合扩大了真实边界覆盖，却受 path explosion、unsupported tensor method、动态控制流和模型配置采样限制；接口简单或 reference kernel 已充分验证时，常规 unit/fuzz test 仍更便宜。`arXiv:2603.24595v1` 的证据只覆盖 §4.1、§4.2、§5 与 §6 所披露的 HFProbe/cuKLEE 实现及缺陷实验，不证明所有 CUDA kernel 或模型调用路径均安全。<!-- source-family:SF-2026-ARXIV-2603-24595 -->

接口合同还不能只写各参数独立的取值区间。例如 host 保证 `rows == cols`，或 grid dimension 与 kernel width 来自同一变量，这些关系会改变一对线程访问是否真的可达。静态检查可把 host 的断言、launch 参数、分配尺寸和循环边界转成联合约束，并让同一程序变量在 solver 中保持同一身份；再与地址相等、线程身份不同的条件一起求解，避免把不可能的参数组合报为 race。存在 acquire/release 指令也不够，还须检查控制流包围关系与同步地址是否匹配。这是现有 model–kernel interface 检查的关系约束分支，不是另一个独立的 correctness owner。它增加 host 分析与求解成本，保证仍受可建模的程序语义限制；提取不到的关系不能臆造为前提，应保守保留可能冲突并结合运行时检测。`arXiv:2604.02106v1` §6–7 的 22 个 CUDA 程序支持这一受限实现的缺陷检出与误报对照，不证明任意模型、驱动或所有执行路径安全。<!-- source-family:SF-2026-ARXIV-2604-02106 -->

Shape、dtype与访问合法，还不能证明layout重排后乘加的两个元素承担正确角色。一个编译反馈分支为元素附加关系标签，让它们随tile、transpose与layout代数传播，再用solver在实际访问位置检查角色配对，返回违反关系的具体元素作为修复线索。标签检查拥有可表达的数据关系，不替代运行时功能测试、数学等价或profiling；编译通过、测试正确和真正更快仍是三个验收对象。

这增加标签规则、布局知识库、求解与修复循环的成本。保守合流为未知、未覆盖global-write/heap、循环与形状限制，都可能使检查失去精度；受测反馈消融还共同改变编译信息，不能把全部改进归给solver。作者的MI300X kernel比较仍有慢于参考和PyTorch回退的任务，不构成任意kernel安全或Serving收益保证。表达能力不足、求解成本过高或目标库已经成熟时，应保留保守检查、独立测试及原backend，而不是凭关系标签越过功能Gate。<!-- source-family:SF-2026-ARXIV-2604-18616 -->

随机数值对照还可能漏掉 DMA、vector、matrix 与 scalar pipeline 之间的可见性 race。执行计划需要声明 program order、sync order、barrier scope 和硬件 happens-before；verifier 检查 barrier 是否足以让 producer 写入对 consumer 可见，compiler/runtime 只接纳通过该内存模型的计划。<!-- semantic-body-binding:SF-2026-ARXIV-2605-07881 -->

形式化检查扩大并发错误覆盖，却只相对参数化硬件模型 sound/complete，并承受模型缺项与状态空间成本。硬件或驱动语义不完整时，应回退保守 barrier、sanitizer、stress test 与 reference kernel。exact-v1 的 CANN/generated kernels 与 mutation 实验不能证明覆盖所有驱动、指令和真实 pipeline。

### Kernel 能加速多少，先取决于它拥有多少端到端时间

在独立 microbenchmark 上寻找更快 kernel，适合已知热点且该 operator 占比稳定的 workload；把每个能加速的 benchmark task 当成同等产品价值，则会忽略大模型的大部分时间可能已在 vendor GEMM 或 FlashAttention 内。进入搜索前应先 profile 真实 model graph，把候选 operator 在目标 shape/batch 下的 wall-clock share 定义为 addressable fraction，再将 verified kernel speedup 投影为端到端上界；上界不足以改变 SLO 时，应停止搜索并把预算转向真正的 critical path。

同时，“通过 benchmark correctness”必须与“在 model–kernel interface 上正确”分开。只用绝对 tolerance 的随机对照会在输出尺度较小时接受接近全零的结果，甚至让局部未写 output buffer 的程序获得虚高 speedup。Admission 至少需要 scale-invariant relative error、按 tensor magnitude 归一化的 max error、sentinel/complete-write 检查与真实 shape/stride replay；对 nondeterministic reduction 还要单独声明数值容差。更强 verifier 会增加运行和调试成本，但没有它时不得把 compile/run success 当作语义正确。

`arXiv:2609.21058v1` 的证据只绑定 A100-80GB、披露的 PyTorch/CUDA/Triton 版本、BF16、KernelBench level 1 与七个作者 workload；它支持“先算可影响份额，再优化”与 evaluator flaw 的存在，不支持其百分比外推到其他 GPU、shape 或生产并发。

<!-- source-family:SF-2026-ARXIV-2609-21058 -->

这些数值测试也需要一个可跨硬件裁决的目标，而不只是“某个 kernel 名称在一组输入上通过 smoke test”。同一算子在 dtype、shape、layout、归约顺序和异常输入变化后，允许的数值偏差、确定性要求与输出完整性可能不同。发布候选前，应把适用范围与前置条件、输出后置条件、reference 及其独立来源、tolerance 的依据、measurement 方法和违约特征固定为同一版本化合同；再分别准备明显失败、常规 smoke 会放行但仍违约、以及符合 reference 的控制样本，确认 verifier 真能区分三种状态。<!-- source-family:SF-2026-ARXIV-2604-22032 -->

违约特征可以指导在 chip、compiler stack 和 shape 上选择更有针对性的测试切片，但这只是在有限预算内提高反例检出，不是通过少数切片就证明全部配置正确。合同编写、独立 oracle、容差校准和异构环境重测都有成本；成熟固定 kernel 可以继续采用较小的 reference/differential regression，硬件或实现身份改变时才重开相应切片。[受限的 kernel-contract 研究](https://arxiv.org/html/2604.22032v1)把多类历史故障组织成测试示例，部分容差仍是占位值，也没有验证完整训练组合或分布式算子；这些示意语法不能充当形式证明，更不是当前厂商故障率。

#### 搜索 Candidate 之前，先选择 Implementation Space

即使 compiler 与 verifier 分责，默认“所有任务都直接搜索 custom CUDA”仍把最重要的先验藏起来：单算子、
fused operator 与完整 model graph 适合的 abstraction level 不同。纯 CUDA 提供最大的 layout、fusion 与 memory
control，却让组合 workload 先花大量 budget 重建 operator dependency；只用 PyTorch operator 或 vendor library
更容易获得正确候选，却可能错过 shape specialization。更稳健的控制流先冻结 semantic contract，再显式选择
implementation space：

```text
reference semantics + callable/interface contract
→ choose PyTorch operator | optimized CUDA library | custom CUDA
→ choose bottleneck-specific optimization direction
→ generate candidate under that space
→ compile + numerical verification
→ pinned profiling and measured selection
→ artifact admission or reference fallback
```

这里 implementation-space selector 只拥有搜索策略，不拥有 correctness 或 deployment authority。它应读取 workload
granularity、shape/dtype、target hardware、当前 candidate、profiling evidence 与剩余 search budget，并把每轮选择、
source、compile result、correctness result 和 timing 写入可重放 lineage。Profiler 只能指导所选空间内部的 refinement；
若空间本身不合适，继续增加 candidate 数只会更稳定地搜索错误边界。

HIERA 在 A100、KernelBench FP32、固定最多 18 个 candidates 的合同，以及一个 FP64 stencil case 中支持这种
coarse-to-fine planning；其生成仍是 stochastic，未覆盖其他 GPU、precision、multi-GPU 或真实 Serving graph。
因此正文吸收的是“abstraction level 也是 execution-plan decision”，不是作者 speedup。稳定单算子、成熟 vendor
kernel 或低搜索预算下，固定 library/template 仍更可预测；只有 reference graph、end-to-end memory plan 与 SLO
复验通过后，搜索到的 isolated kernel 才能进入 engine。

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

MoE 还会让这条边界更尖锐：单个 expert kernel 的算术加速若低于 forward pass 的 launch、dispatch、route 与
communication floor，isolated speedup 可以很大而端到端几乎不变。正确的优化顺序应先用 end-to-end profile 建立
可偿还上限，再决定是否改 kernel、融合 graph、调整 routing/placement 或减少同步边界：

```text
request-level latency / throughput trace
→ route + launch + memory + communication attribution
→ counterfactual ceiling for the target operator
→ local optimization
→ end-to-end replay with route and quality checks
```

Route drift 本身也不是 quality loss 的充分解释；量化可以改变 expert selection，却可能主要由 weight error 而非 routing
变化造成质量退化。因而 route overlap、output quality 与系统性能必须分别测量，不能用任一代理替代另外两项。
这条诊断用更多 trace、replay 与 intervention 成本换取不把局部数字误写成系统收益；当算子已被 profile 证明占据关键路径、
shape 稳定且 route 不变时，旧的 kernel-first 优化仍然合理。

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

### Microsecond Inference 先暴露非 Matmul Overhead

模型较大时 GEMM 主导，逐层框架调度和 synchronization 常可忽略；极小模型或 microsecond 目标下，launch、inter-layer handoff、sync 与非 matmul operator 会成为主要延迟。Execution plan 需要联合决定直接层间连接、fusion、buffer lifetime 与同步边界。

更激进的 plan 降低 overhead，却增加静态 shape、backend 专用性、调试和数值等价风险。工作负载动态、batch/shape 经常变化或 latency 不到该量级时，通用 runtime 仍更经济；所有结果必须绑定 model、hardware、precision、shape 与端到端计时。

<!-- source-family:SF-2026-ARXIV-2605-17683 -->

### MoE Quantization 必须把 Router 放进全局误差预算

逐层独立选择 bit width，在 dense network 中可用局部 reconstruction error 近似质量损失；MoE 中 quantization 还会扰动 router logits，使 expert selection 和通信路径发生离散变化。Execution-plan builder 因而要联合记录 expert bit allocation、global error budget、router calibration set 与 placement revision，局部 kernel 只能报告误差和成本，不能独自提交最终量化计划。

全局优化获得更低显存或带宽占用，代价是求解、校准和部署矩阵更复杂，且路由漂移可能放大少数 expert 的误差；模型较小或 router 对扰动不敏感时，统一量化仍更简单。arXiv:2605.23078v1 的方法与实验只支持其 MoE、量化配置与评估条件，不证明同一 bit allocation 在其他模型、硬件或 SLO 下最优。

<!-- source-family:SF-2026-ARXIV-2605-23078 -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-09281:start -->
逐 expert、逐矩阵做低秩量化最容易归因；当 expert 数量扩大后，相同子空间、量化 metadata 和大量小 kernel 会重复出现。二维 tiling 分支先按 activation 统计把 experts 聚成可共享的 input/output subspace，再由 fused sparse kernel 一次完成投影、routing-weighted accumulation 与 reconstruction。Calibration 只提出 cluster、tile 和 rank，execution-plan owner 绑定 router、layout、precision 与 kernel revision 后才提交。

共享子空间减少 metadata 和 launch，却会引入 cluster 错配、tile/rank 选择错误、expert 间误差耦合与硬件专用 fusion。现有结果只支持作者披露的 MoE、GPU、模型和 evaluator，不能外推到其他 shape、SLO 或生产负载。Experts 差异大、路由漂移或目标硬件缺少 fused path 时，应回退逐 expert 量化或未量化 expert。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-09281:end -->

### Layout Plan 必须跨算子优化，并单独验证 Cost Model

逐算子选择局部最快 layout，在单 operator 或转换很少时简单有效；dataflow graph 中相邻算子偏好的 layout 不同时，局部最优会累积 conversion cost。Build owner 应把 operator execution、tensor layout 与 conversion edge 组成全局 plan，并把 solver optimality 与 cost-model accuracy 分开验收：求解器已优化声明目标却在线上落后，说明估价或 workload identity 错了，不能继续调搜索器掩盖。全局求解用编译时间、profile revision 与动态 shape 适配换取更少转换；图很小或 workload 漂移快时，局部 heuristic 仍合理。`arXiv:2608.21555v1` 只支持其困难性结果、bounded-treewidth exact algorithm、MaxSAT 近似与作者生产编译器 workload，不证明任意后端都获益。

<!-- source-family:SF-2026-ARXIV-2608-21555 -->

跨算子计划还必须联合决定 **buffer 保留与计算顺序**。仅说“融合后复用 tensor”并不充分：保留下游暂时不能消费的 tile 仍会挤占 buffer，而改变 loop order 又可能使先前计划的复用消失。可以把 tile、顺序、buffer 层级和选择性重算写入同一 loop representation，再在声明空间内搜索；例如 softmax 前尚未完成的 partial sum 不能任意跨算子传播，需作为合法性限制，而不是由成本模型猜测。<!-- source-family:SF-2026-ARXIV-2604-03446 -->

这种共同搜索以编译预算和模型复杂度换取减少 DRAM 重读的可能性；“最优”只相对于枚举空间与分析模型，模型内最优不证明真实 accelerator 最优。所测 BERT/GPT/PaLM training 或 prefill 模拟中，重算收益随模型和 buffer 容量变化；intra-operator cost-model 对照也不能充当 fusion 实机验证。buffer 足够装下关键矩阵、图较简单或估价不可靠时，局部 layout 与保守 fusion 仍合理，端到端测量不能省略。

### Intended Placement 必须由硬件计数器复核

Compiler graph 标注某 accelerator，不等于该算子和权重真的在那里执行；等价 graph expression、encoding 或 runtime fallback 都可能改变 residency 与 byte stream。Execution-plan validation 因而要同时保存 intended graph、编译产物和 measured placement evidence，例如 memory-controller/driver counter，并按真实 decode bytes 与 latency 判断是否命中目标路径。测量增加平台专用探针和反向工程不确定性；官方支持路径稳定且可由 runtime receipt 直接证明时，不必每次做同等深度 sweep。`arXiv:2608.22110v1` 的证据只覆盖作者 CoreML/Apple Neural Engine 与小模型，不能外推 CUDA、其他 accelerator 或大模型性能。

<!-- source-family:SF-2026-ARXIV-2608-22110 -->

## Build-time 与 Runtime-time

### Diffusion Decode Granularity 也是运行时调度状态

固定 denoising chunk 便于编译与容量规划，但负载变化时会在并行度和响应时间之间失衡。Serving engine 可以把当前队列、饱和度与剩余步骤作为控制状态，动态选择本轮更新粒度；executor 拥有可执行 chunk，scheduler 只提交满足 memory 与 latency contract 的计划。收益是适应运行负载，代价是调度开销、cache/state 一致性与尾延迟振荡；稳定离线 workload 仍适合固定粒度。现有证据绑定披露 diffusion LLM、A100 与负载，不能外推为通用 SLO 改善。

<!-- source-family:SF-2026-ARXIV-2605-24832 -->

运行时改变 chunk 之外，还有适合固定 diffusion 部署的**离线预算分配**。先学习不同 layer、denoising step 和候选稀疏率对应的重构代价，再在共同稀疏率/跳算预算约束下选择各位置的稀疏率，使预测重构代价尽量小；训练可从保留 full step 的 warm start 进入联合 layer/step 分配，最终输出静态 sparse schedule。Token ranking 是可替换的执行组件，求解器并不拥有质量真值；动态规划最优仅针对预测代价和离散候选空间。<!-- source-family:SF-2026-ARXIV-2604-03674 -->

这条分支把控制开销前移到校准训练与 build-time，不是推理中每步重新求解。它增加 teacher/student 训练、配置管理和模型迁移成本，预测更细也可能使实际质量更差；所测图像/视频模型有 FID 退步，Wan 方法设置与结果表的 step 数也不能合并为同一条件。只有目标模型、step 数、精度和质量 slice 验收后，静态 schedule 才能进入 engine；缺少稳定校准或 workload 经常变化时，固定较保守稀疏率/full attention，以及前述运行时 chunk 调度，仍是不同责任的共存分支。

### 同一 Timestep 的跨迭代缓存是一条近似执行分支

固定 diffusion schedule 还可以暴露另一种复用机会：并行时间积分在迭代求解时，可能反复请求同一个 timestep 的 denoiser。缓存该 timestep 的 latent 与预测输出，仅在新 latent 与缓存 latent 的距离超过阈值时重新计算，可以减少重复 UNet 调用；但缓存阈值与 solver 收敛阈值负责不同判断，不能共用一个“已收敛”标签。即使 solver 保持原更新公式，复用近邻 latent 的预测也已引入近似，不保持原轨迹精确等价。模型、conditioning 或 timestep 语义改变时使缓存失效，是部署正确性的要求。

收益必须跨过 hit 检查、协调和通信的开销；较保守的阈值可能减少网络计算次数却让墙钟时间更长，较宽阈值则可能损害质量。[ParaAnya 在固定 SD1.5 图像生成上的对照](https://arxiv.org/html/2609.36522v1)将同资源缓存/未缓存比较与多 GPU 对单 GPU 比较分开；后者不能当作免费算法收益。有限 CLIP/LPIPS 结果不证明所有感知质量或并发 SLO。负载变化快、命中少、通信昂贵或质量敏感时，未缓存求解和更小并行窗口仍是共存基线。
<!-- source-family:SF-2026-ARXIV-2609-36522 -->

### Microscaling Format 也有阶段身份

固定一种低比特格式便于 kernel 与 artifact 管理，但训练和 direct-cast inference 对 exponent range 与 mantissa precision 的压力并不相同。可切换模式的 microscaling block 让同一量化家族在训练阶段保留更细尾数、在推理阶段扩大动态范围；因此执行计划必须把 block size、shared scale、mode、目标硬件和转换阶段共同写入 format identity。收益是减少重复校准路径，代价是 kernel 分支、验证矩阵与跨设备可移植性变复杂；模式判断错误会把局部溢出或舍入误差扩散到整块。硬件不支持该布局或 workload 分布稳定时，单一格式仍是更可审计的选择。当前证据只覆盖作者披露的格式与任务，不能外推为任意模型上的通用精度收益。

<!-- source-family:SF-2026-ARXIV-2605-24391 -->

更稳定的理解是把系统拆成两个阶段：

```text
model/checkpoint + config
-> conversion / build / optimization
-> engine or runtime-loadable artifact
-> executor
-> in-flight requests and KV state
```

Build-time 选择模型结构、precision、plugins、parallel mapping 和硬件适配；runtime-time 管理 requests、batch、KV Cache、sampling、streaming 与 collectives。具体版本可能把更多工作移到运行时，但“静态资产 identity”与“动态 request state”的区别不会消失。

### Block Scale 也是可搜索的执行状态

BFP/NVFP4 常用 block max 直接确定 scale，成本低且确定，但 outlier 会让多数值浪费量化区间。ScaleSearch 把 scale 从
固定 heuristic 变成受误差与执行约束限制的候选搜索；搜索器只提出 scale，真实 kernel 的数值回归、模型质量和 latency
测试才拥有 artifact commit。收益是更好利用低精度范围，代价是校准搜索、硬件/格式耦合和额外发布矩阵。未命中受测
分布、kernel 不支持或回归失败时，应回退 max scale、更高精度或已有量化路径；论文只覆盖特定模型、PTQ 与 NVFP4 设置。

<!-- source-family:SF-2026-ARXIV-2605-12464 -->

### Block Scale 的格式选择也是执行 Artifact

microscaled FP4 为每组固定一张 grid，接口简单但可能浪费局部分布适配空间。允许多 grid 时，quantizer 为每组提出格式，artifact 必须保存 grid/scale identity，runtime 与 kernel 负责忠实解码，质量和端到端性能 gate 才能批准发布。更低量化误差换来 metadata、搜索与 backend coupling；选择错误或 kernel 不支持时，理论收益不会变成速度。系统应能回退单一 NVFP4/MXFP4、较高精度或静态 max-scale，并分别验收模型质量与 latency。exact-v1 只覆盖作者模型、group size 和硬件实现，不证明多 grid 总优于单 grid。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-12327 -->

格式 identity 还必须包含分组轴与增长阶段。K 沿每个 token 的 channel 分组，V 沿每个 channel 的 sequence 分组时，后者的新 token 可能尚未凑满尾组，不能把临时共享 exponent 当作已经提交的 cache。一条 BFP 执行分支暂存这个残组，每轮加入新值后作临时转换供 attention 使用，组满后才作最终转换并提交到 V cache；converter 因而要匹配输出次序与 group 完成状态。由此得到的工程合同是区分临时与已提交组，不能让动态 scale 静默改变已提交组的数值身份，而不是宣称作者已验证所有 cache 生命周期。这用残组缓冲、重复转换与格式/PE 协同换低精度执行，不等于把所有 KV 简单 cast 成固定 bit；长上下文质量退步或目标 kernel 不支持时，保留更高精度 cache。作者硬件收益来自综合、时序/功耗与 cycle 模拟，不提供实芯片 Decode 或生产 SLO 证据。[必要格式、转换与评价边界](https://arxiv.org/html/2602.04595v1)。<!-- source-family:SF-2026-ARXIV-2602-04595 -->

### Diffusion Block 内的 Expert Stability 可以变成受限 I/O Hint

普通 MoE offload 按每一步独立 router 结果搬运 experts，语义清楚，也能适应快速变化；在 block-diffusion 推理中，若同一 block 内相邻 denoising step 的 expert activation 足够稳定，runtime 可以把这个 temporal locality 编译成 prefetch/retain hint，减少反复 host-device I/O。Router 仍拥有真实 activation，cache manager 只能基于版本化预测保留或预取，不能把历史 expert set 当作正确路由。

该分支以 expert cache、预测错误与额外调度状态换 I/O 降低；block 边界、prompt shift 或 routing entropy 上升时会误预取并挤占热 expert。无法观测稳定性或模型不是所测 diffusion-MoE 时，应回退逐步 routing/offload。`arXiv:2605.20179v1` 的 §3、§4 与 §5 只支持其 LLaDA2.0、block 内 activation stability 与有限硬件实验，不证明 causal decoder、其他 MoE 或生产并发中的通用收益。

<!-- source-family:SF-2026-ARXIV-2605-20179 -->

Early-exit 把两阶段边界向训练目标再推进一步。事后在若干 layer 上蒸馏 classifier，适合固定 exit head 和近似任务；当 runtime 的退出条件是 hidden state 已收敛、增量收益不足或 SLO budget 用尽时，训练目标若没有塑造与该 sensor 一致的中间表示，exit policy 会在未完成推理时过早提交。更完整的 contract 是：pretraining/fine-tuning 明确优化可用的中间状态，build artifact 绑定 exit head/sensor，runtime controller 只提出退出，最终校验按任务风险决定是否接受或回退 full depth。

这条路径用额外训练 loss、多个中间输出和 calibration/drift 监控换平均计算节省；它不证明浅层输出与完整深度等价。高风险生成、分布漂移、校准不足或 backend 不支持稳定中间状态时，完整 depth 仍是默认；early exit 只能作为受 SLO 与 evidence 约束的执行分支。

<!-- source-family:SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT -->

提前退出只决定何时停止向更深层推进；另一条条件计算分支允许不同 token 穿过不同的中间层。固定首尾层后，可以用首层 KV 汇总当前 prefix，由 scorer 与离线 prior 提议在给定层数预算内执行哪些中间层；预算未指定时，另一个训练过的 predictor 再提出执行深度。模型权重没有因此消失，层数比例也不是 wall-clock SLO。Planner 拥有路径选择，runtime 仍须明确每层每个历史 token 的 KV 是否真实产生：路径改变后，先前跳过的层没有可直接复用的完整历史，不能把“现在重新选中”当作 cache 已经有效。

这比固定浅层或固定跳层更灵活，却增加 router、gather/scatter、异路径 batching 和缺失状态管理成本。[受限动态深度实验](https://arxiv.org/html/2606.09514v1)使用零向量标记未执行状态、保持全部权重驻留，并不恢复与完整深度相同的 KV 或减少权重显存；轻剪枝可能被路由成本抵消，固定路径在 Decode 中仍可能更快，较难推理任务也会显著退化。缓存补全、路径分组或受限重算必须另有正确性与质量证据，不能从这一实验推定已经实现。若跨请求路径不兼容、质量下降或节省不足，应回退经验证的固定路径或完整深度；具体 KV 有效性与留存状态由[第45章](./45-why-kv-cache-speeds-up.md)接手，不让动态 scorer 获得正确性授权。<!-- source-family:SF-2026-ARXIV-2606-09514 -->

动态深度与低比特量化叠加时，执行率不是可以独立相乘的节省项。原训练若只约束平均执行比例，router 可能固定跳过少数层，丢失替代路径的训练经验；一个分支用 entropy 维持训练 path diversity，再在 PTQ 后调整全局 execute threshold，用更多层执行补回部分量化质量。它改变的是探索覆盖与低比特误差的联合控制，不意味着每个 token 的少执行都同样耐受量化。<!-- source-family:SF-2026-ARXIV-2602-10431 -->

[必要量化/执行率对照](https://arxiv.org/html/2602.10431v1)中，PPL 恢复常伴执行率上升，单 A6000 的 W4 配置也可比原动态层模型更慢；不能把名义少层或4-bit推为同质量/同FLOPs免费恢复。部署 threshold、router、路径与量化 artifact 应一起验收，原文 threshold 分支展示有歧义，不照录为可执行公式。缺少路径覆盖、回归退化或总成本无净收益时，完整深度、更高精度与已验证固定路径继续成立，KV 缺失状态仍按第45章处理。

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

### Startup overlap 必须守住 Graph-visible Storage Identity

最直接的启动流程是先把真实 weights 完整加载、转换和放置，再初始化 runtime 并 capture CUDA graphs。它把
artifact commit 放在 graph construction 之前，状态边界清楚；代价是 checkpoint I/O、page-cache staging 与
graph capture 串行支付。模型和 capture 成本同时增长后，可以把 storage staging 与 graph capture 重叠，但不能
简单地“先用假权重 capture、稍后换 tensor”：captured graph 可能已经绑定 tensor object、data pointer、shape、
stride、dtype、device 与 storage offset。

更安全的演进是：

```text
load real weights, then capture graphs
→ prefetch checkpoint pages, then load and capture serially
→ allocate final storage and capture with compatible sentinel values
→ stage checkpoint pages concurrently
→ commit real weights in place
→ verify graph-visible storage identity
→ synchronize, join staging lifecycle and enter serving barrier
```

这里至少有三个不同 owner：checkpoint loader 拥有 shard resolution 与 page staging，model runner 拥有最终 tensor
storage，graph runtime 拥有 captured pointer contract。Overlap manager 只能改变这些阶段的排序，不能转移最终
weight identity 或跳过 post-load processing。若目标 loader、mmap path、model family、precision、TP degree 或
checkpoint source 不在已验证矩阵中，显式回退到 serial path 比静默 overlap 更安全。

SGLang v0.5.18 的 opt-in 路径为该 contract 提供了版本化案例：它把 safetensors pages 搬入 OS page cache 的工作
与 CUDA graph capture 重叠，真实 weights 仍在 capture 后原位 commit，并在服务前检查 storage identity。其
Qwen3-32B BF16、H100、TP1/TP2、local-NVMe、三次采样结果只能说明该受限路径的启动时间；不证明 NFS、其他
loaders、量化模型、不同 GPU 或更大 TP 会获得同样收益。该路径还把 cancellation、join、barrier ordering 与
startup-terminal failure 变成新的 lifecycle contract；当 overlap window 小、storage 已热或验证矩阵不足时，
serial startup 仍是更稳健的分支。

### 跨进程恢复 Graph 要恢复 Execution Context，而不只保存拓扑

上面的启动重叠仍在同一进程里维持最终 storage identity。若要把离线 capture 结果交给新进程，保存节点和边还不够：kernel 参数可能嵌入设备地址或库的 opaque pointer struct，节点还引用该进程加载的 kernel function。重新分配 weights/KV 后照搬拓扑，会得到形状正确却地址失效的图；逐 kernel 手写参数修补在执行栈稳定时可行，但私有布局、新 kernel 和不同层结构会使它脆弱。

一个条件性恢复分支把 execution context 与拓扑一起归档：离线记录单调的虚拟地址分配、capture 期间临时 allocation、实际 kernel binary 及其 hash/function-name 身份；新进程保留同一虚拟地址范围并重放必要 allocation，加载对应 binary 后再解析 kernel handle。这不是从地址猜 tensor，也不是冻结整个 worker 的活跃请求；weights、KV 内容及通信组仍要按各自 owner 正确建立。固定 KV pool 与相容的分配序列是该方法成立的前提，地址占用、库/driver/模型变更或分配路径偏离时，应重建 archive 或回退正常 warmup/capture。这里的兼容验收是由机制推导的工程要求，不是所有变化都已被作者验证自动恢复。

多个 batch shape 可以只共享**拓扑相同**的 executable template，再按目标 shape 更新节点参数；节点类型、依赖和影响执行的 attributes 都属于这个等价条件，不能只比节点数。跨 rank 共享更窄：只有 SPMD ranks 的执行结构相同，才可在离线用通信 stub 记录模板，部署时绑定实际 rank、communicator 和相应设备状态。不同 pipeline stage 并不自动属于同一模板，stub capture 也不是多 rank collective correctness 的验证。Graph runtime 拥有 archive/context 重建，model/communication owner 提交真实状态；第50章的服务入口只有在二者都 ready 后才能接受请求。

这用一次离线 capture、archive 容量、确定性 allocator 和库拦截换取冷启动少做重复工作，同时引入 archive 失配、地址冲突、binary/driver 耦合与 lazy initialization 遗漏等失效路径。短启动、小模型、动态分配或频繁更换 backend 时，普通 capture 更透明；共享模板也不能替代端到端输出对照。Foundry 的 exact-v1 只在其 vLLM 0.11.2/PyTorch2.9/CUDA13.1、DGX H200/B200、所测 dense DP 与 MoE EP、固定 KV 大小和 batch 1～512 archive 下验证该分支；decode-only PD 的启动/TPOT及所测 token 一致不证明所有 serving 阶段、任意硬件或 PP 恢复。<!-- source-family:SF-2026-ARXIV-2604-06664 -->

### Quantized Artifact 的 Portability 必须包含 Scale Semantics 与 Kernel Path

同一 ONNX/权重文件、compile success 或 top-1 保持，都不足以证明跨 kernel、ISA、vendor compiler 的 INT8 行为一致。Execution plan 应联合绑定 artifact、scale semantics、integer kernel/ISA、compiler path、target hardware 与 behavioral/latency validation；runtime 静默忽略或重解释 scale 时必须 fail closed。<!-- source-family:SF-2026-ARXIV-2609-16085 -->

跨硬件验证增加 build matrix 和发布成本，作者七类硬件也只有有限设备与测量；没有等价证据时应保留设备专属 artifact 或高精度 fallback。

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

后端预编译需要固定 tensor capacity，却不代表有效请求长度也固定。对有 tiled memory 和静态 vector-register compute blocks 的 TPU，可以把 ragged 维移出被硬件平铺的末维，增加 packing 维并合并 K/V，让有效页数据由动态 DMA 取得，再把 KV 更新与 Attention 流水线重叠。Compiler 的 layout assignment 仍可能重排投影后的中间张量，因而离线 weight reshape 不当然消除在线 preprocessing；plan 必须验证 custom-kernel 边界的真实 layout，并保留转换成本，而不只保存逻辑 shape。

启动时将最大 token/sequence 数作为 capacity envelope，padding 到静态 shape 可避免 JIT 重编译进入请求关键路径，但动态 DMA 不会消除静态 compute tile 的浪费。同一 capacity 下，不同有效长度分布仍需不同 decode、fixed-chunk prefill 或 mixed block 配置，调优与预编译应共同绑定该分布。受限 [RPA v1](https://arxiv.org/html/2604.15464v1) 的 TPU7x/Llama3-8B/BF16 测量只在足够长 context 或 prefill 饱和时取得高利用率；prefill preprocessing 仍占约2%～8%，其 d=128 MFU 分母还按50%最大MXU使用率调整，不能当成全芯片或全请求收益。高度 ragged、未覆盖shape或layout改变时，成熟 padded/general kernel 与重新编译验证仍是回退，不从历史后端吞吐演进推通用生产SLO。<!-- source-family:SF-2026-ARXIV-2604-15464 -->

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

### CPU Decode 可以把模型依赖图改写为 Stage-major Dataflow

传统 layer-major Transformer 在 GPU compute-bound 路径上最成熟；CPU 或 storage-tier Decode 若被 weight bandwidth 支配，逐层读取完整权重会让 cache reuse 很差。一条受限 co-design 分支修改 inter-layer dependency，使 runtime 以 vertical stage-major 顺序复用 L2-sized weight tiles，并只流过已选 experts。它用模型重训、非标准依赖和复杂验证换取 weight locality；模型不可重训、GPU compute-bound 或 batch 足够大时，传统 layer-major 仍更合理。`arXiv:2608.23841v1` 的 TinyStories 与 30.9B CPU/disk-tier 结果只支持可行性，不证明主流 GPU、通用模型质量或任意 MoE 收益。

<!-- source-family:SF-2026-ARXIV-2608-23841 -->

### 层间依赖也可以成为受限的并行分支

常规 decoder 严格按层推进，因为后一层消费前一层完整 hidden state；这种顺序执行正确、稳定，也最容易与 kernel fusion 和 KV 生命周期对齐。另一条实验分支把整条 hidden-state trace 写成 nonlinear residual equation，再用 structured Newton-style correction 并行更新多个层。它改变的不是 tensor parallel 的切分维度，而是把“层序列”从既定控制流变为待收敛状态。

潜在收益是暴露 layer parallelism；代价是 correction 迭代、Jacobian/近似结构、额外激活状态与收敛失败。残差不降、数值条件恶化或 correction 成本超过顺序执行时，必须回退标准 layer order。现有 exact-v1 只支持其披露模型、近似、任务和硬件上的实验结果，不证明任意 decoder 都能保持质量、降低端到端尾延迟或适合生产 serving。

<!-- source-family:SF-2026-ARXIV-2605-17842 -->

### Software-defined Dataflow 仍需明确 Placement Authority

Thread-centric accelerator 把大部分调度隐含在硬件；software-defined locally accessed dataflow 则让编译器显式安排数据移动与局部执行，引入可编程 data-movement engine。它可能让 layout、placement 与通信更贴近模型图，却把正确性和性能责任转给 compiler schedule、memory dependency 与 fallback；通用 kernel/线程模型在动态 workload 和 portability 优先时仍成立。`arXiv:2608.24664v1` 可支持 Maia 200 的架构与 placement 思路，但 10,145 TFLOP/s FP4、7 TB/s HBM、750W 等是厂商披露，不能作为跨系统优势证明。

<!-- source-family:SF-2026-ARXIV-2608-24664 -->

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

### KV 可以成为 Packetized Fabric State，而不再属于单个 Accelerator

单卡 runtime 把 KV 视为本地 SRAM/HBM 地址，路径最短且一致性简单；当 decode state 超过单 accelerator 容量或多个 compute tile 需要共享时，可以把 KV request/response packetize，经片上网络访问独立 memory tiles。此时 execution plan 必须同时拥有 KV block identity、destination、credit/flow control、ordering 与 backpressure，compute kernel 不能假设 load 一定本地命中。<!-- source-family:SF-2026-ARXIV-2609-19207 -->

共享 fabric 提高容量与复用，却增加 packet latency、NoC contention、head-of-line blocking 和故障域；作者 architecture/simulation 不证明商品 GPU、任意模型或生产 tail latency。工作集可常驻或流控无法闭合时，应回退本地 KV、显式 sharding 或 host tier，而不是把远程状态当透明内存。

### Static Denoising Schedule 才允许更激进的 Engine Co-design

Diffusion workload 的 shape、step count 和 memory access 若在部署前固定，VLIW/专用 engine 可以把控制流编译进 schedule；但 synthesis 或局部 place-and-route 只证明组件可实现，不能替代真实 denoising trajectory、full-chip timing、memory stall 与数值质量验收。<!-- source-family:SF-2026-ARXIV-2609-16244 -->

专用化换来吞吐和能效潜力，也牺牲动态 shape、模型迭代与故障回退。schedule 或 model revision 改变、full-chip P&R 未闭合时，应回退可编程 GPU/compiler path；作者 accelerator 设计不能被写成 production silicon 证明。

### 把 SLO Slack 下沉为 NPU 组件级 DVFS 控制

chip-wide DVFS 用单一频率域换 timing closure、控制简单和可预测性，在各组件利用率同步时仍合理。LLM operator 的约束变化是 phase 与组件瓶颈分离：某段更依赖 systolic array，另一段更依赖 vector unit、SRAM 或 communication；全芯片一起降频会拖慢真正的 critical component，也浪费非关键组件的 slack。

更细粒度的 execution plan 可以为组件建立独立 voltage/frequency domain 与异步边界，由 compiler/runtime 在 operator schedule、request phase 和剩余 SLO budget 下共同选择频率。这里 slack 是 deadline accounting 的一部分，不能由硬件局部 controller 猜测；transition latency、cross-domain synchronization 和 power model version 都必须进入 plan identity。

收益是只回收非关键组件的能耗，代价是 area、level shifter/FIFO、搜索空间和预测误差。slack 很小、operator bottleneck 均匀或 power model 未校准时，global DVFS 仍更稳。现有证据是 TPUv5p-spec simulator 与 Coral NPU RTL/ASAP7 prototype；其 energy/SLO 数字不是 TPU production silicon 测量。

组件级 DVFS 保持数值格式时只分配频率；跨设备预算还可联合选择量化位宽与 clock，用模型误差或 rate–distortion proxy 比较候选，但这多了一层数值与执行可行性责任。[一个受限 bit–clock 分支](https://arxiv.org/html/2602.13052v1)的误差推导依赖 FC、输入范数与 Lipschitz 条件，去掉层系数和 Taylor 近似后不自动成为真实 Transformer 输出或任务质量硬界；抽象 channel 的 RD gap 也不证明某个有限整数 codebook 可达。连续优化结果 round 到可用位宽后，必须重验实际 backend 的质量、延迟和能耗约束，不能继承未取整解的可行性。Orin/3090 的三个实测档位不是任意细粒度频率可实施的证据，模拟 clock 与真实 profile 分开；校准、量化、传输与频率切换均计费，proxy 失配或 deadline 不成立时，回退已验收静态格式、可执行粗档和原 global/component DVFS，而不由代理最优签发生产 SLO。 <!-- source-family:SF-2026-ARXIV-2602-13052 -->

### MoE Offload 要同时决定 Expert 聚合与执行位置

逐 expert 把小 token group 往返 CPU/GPU，能够突破显存容量，却容易被 launch、搬运和碎片化执行吞噬。coalesced execution 先把可共同执行的 expert 工作合并，再由 runtime 决定 AMX CPU 与 GPU 的 placement，使 micro-batch、intermediate buffer 和 transfer plan 由同一 owner 管理。

它用额外调度、packing、CPU 资源和一致性状态换取更高吞吐；路由偏斜、token group 太小、互连拥塞或 CPU 抢占都可能反向放大尾延迟。模型可完全驻留 GPU 或单设备执行已足够时，旧路径仍更简单。exact-v1 证据仅覆盖所披露 MoE、AMX/GPU 平台、batch 与吞吐设置，不证明跨硬件或 latency-sensitive workload 的普遍收益。

<!-- source-family:SF-2026-ARXIV-2605-17889 -->

低 batch MoE 在另一类硬件上会遇到相反约束：不是 expert group 太碎需要聚合，而是单个 expert 权重太大，无法在 chiplet 的局部 SRAM 中常驻。把 expert 完全分片后按层同步搬运最容易保证正确，却会让 die-to-die transfer 串在每个 sparse layer 前。若相邻层的 router trajectory 具有可预测性，runtime 可以把 expert shard 切成 micro-slices，沿预测的 expert path 提前流式搬运，并让 transfer 与当前 expert execution 重叠。

Router 仍拥有 token→expert 真值；trajectory predictor 只拥有 prefetch 顺序，执行前必须验证所需 shard 已到达，误预测则等待 authoritative transfer 而不能跳过 expert。收益是把低 batch 的 weight movement 藏进执行，代价是额外 shard metadata、chiplet synchronization、预测器和片间带宽占用；batch 足够大、expert 可驻留或路由剧烈漂移时，标准 Expert Parallel/常驻权重仍更稳。`arXiv:2603.27624v1` 的证据只覆盖 §IV 的 FSE-DP/Micro-Slice Flow、§V 的 MoE trajectory scheduler，以及 §VI-C–§VII 所披露架构和实验，不证明其他 chiplet、互连或大 batch workload。<!-- source-family:SF-2026-ARXIV-2603-27624 -->

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

### 执行计划的下一阶段：可移植语义、局部精度与闭环验证

CUDA 专用栈用成熟 kernel、graph capture 和 profiling depth 换取更高性能；Vulkan/Metal 一类可移植栈则需要把计算图、自动微分、图重写、kernel 选择和静态内存规划显式化，才能在不同设备保持同一 operator contract。可移植不等于性能等价：不完整算子覆盖、驱动差异和第三方 kernel 生态都会限制它，成熟单一硬件部署仍应优先采用经验证的专用路径。

混合精度也从“整层一个 dtype”推进到 tile-group 级 precision assignment，使量化敏感性与实际 kernel 执行粒度对齐。它能减少不必要的高精度计算，却新增校准 artifact、irregular tile layout 和硬件专用 lowering；迁移模型、Context 或 GPU 后必须重新验证。

最后，standalone kernel benchmark 不能证明模型端到端收益。闭环优化应从目标推理脚本抽取 phase-aware task，候选 kernel 只有在重新集成模型、固定 correctness/SLO 合同并复测后才发布。这个过程用昂贵的 in-model validation 换更少的 benchmark illusion；静态、成熟 workload 仍可由人工 kernel library 与离线 autotuning 更经济地维护。

Mixed-precision policy 也需要进入同一闭环。Analytical proxy 可以先用 cache bound、表示几何与算子约束排除
明显无效组合，但只有 compiler IR 看得到 lowering、vector width、tensor-core path 与 layout 对真实成本的影响；
因此强候选仍需在目标硬件测量，并用结果校准 cost model。它减少 exhaustive hardware-in-the-loop search，
却引入搜索预算、校准过拟合和 compiler/hardware version drift。固定硬件且代价模型成熟时，离线静态 policy
仍更简单；跨设备复用一份 mixed-precision policy 不能默认保持 Pareto 关系。

配置搜索还应分成 feasibility 与 ranking 两阶段。第一阶段由显存、shape、kernel support、并行整除与通信拓扑等硬约束排除不可构建计划；第二阶段才用 cost model 或实测在可实现域内排序。若把二者混成单一预测分数，模型可能把“预测很快但无法部署”的配置排到最前，也难以解释失败来自约束还是估计误差。分阶段会增加 constraint model 维护，但能让 fallback 回到已验证 plan。<!-- semantic-body-binding:SF-2026-ARXIV-2608-19296 -->

<!-- source-family:SF-2026-ARXIV-2605-28704 -->

浮点执行语义还包含 reduction order 与 activation approximation，而不只是“BF16/FP16”标签。并行度、batch shape 或 kernel plan 改变后，结合律失效会让同一输入走到不同舍入路径；若 activation 用近似实现，其 bounded-ULP contract 也必须进入 engine artifact。要声明可重放，需共同绑定 precision、reduction topology、kernel/activation implementation、compiler/runtime 与硬件目标，并在这些条件变化时重新验证。

有限浮点域上能表示某个函数，不等于实现会产生确定 token，更不证明部署质量。固定顺序和更精确 activation 可换复现性，却可能损失吞吐；允许数值容差的线上服务仍可采用更快 kernel，审计/回归路径才启用确定性 plan。exact-v1 的构造性结果只支持其数学与实现条件，不能外推为所有 GPU engine 的 bitwise guarantee。

TensorRT-LLM 这类优化栈的收益通常来自更深的硬件适配，代价是部署复杂度和调试复杂度上升。

它适合需要高吞吐、低延迟、NVIDIA GPU 深度优化的场景；如果团队只需要快速原型，直接使用通用 runtime 可能更简单。工程上要判断的是：当前瓶颈是否已经到了需要 engine build、kernel fusion、quantization 和分布式 runtime 的程度。

更深的硬件适配还意味着支持矩阵并非抽象问题。模型架构、GPU generation、precision、kernel 与 TensorRT-LLM 版本需要形成经过验证的组合。升级其中一项可能改变 engine build、数值质量和性能，平台必须把这些信息作为模型部署制品的一部分记录。

### Reasoning Quantization 要验收 Commitment，而不只是 Token Cost

weight-only 低比特量化可以降低 memory traffic，在短输出、非推理任务中仍是成熟基线；reasoning workload 会把小的
数值误差累积为 loop、迟迟不提交答案或在中间正确后最终改错。量化 release identity 因而需要联合 precision、
generation budget、termination parser、first-answer/commit gap、hit-limit 与 loop rate，并把 per-token throughput 与
end-to-end completion 分开。低比特路径只拥有快速 proposal，release gate 根据任务 regime 选择继续、阶段性切回高精度，
或完全使用 reference plan。

这种 phase-selective fallback 用双执行路径、切换状态与更大的测试矩阵换取对关键 commitment 的保护；loop detector 和
parseable-answer heuristic 本身会漂移。作者实验绑定特定 Qwen reasoning models、GPTQ-style W4/W2 路径与固定预算，
不证明任意模型的安全 bit-width，也不覆盖 production batching/tail。无法校准时保留较高精度或 full-precision plan。

<!-- source-family:SF-2026-ARXIV-2606-02011 -->

### 条件化机制分支与共存边界

主线之外仍存在若干只在特定前提下成立的设计分支。下面按状态与控制权的变化说明它们解决的问题、新增代价及回退边界；来源身份和实验限制统一留在章末 Review notes。

<!-- semantic-body-binding:SF-2026-ARXIV-2606-15682:start -->
#### W/A/KV 联合量化必须保护关键 Reasoning Commitment

统一 W4A4KV4 可以显著缩小权重、activation 与 KV 的执行 footprint，但 reasoning failure 往往集中在少数低熵 symbolic commitment，平均困惑度或最终准确率会掩盖这些不可恢复转折。Quantization plan 因而需要把 trace-aligned QAT、对关键 commitment 的 selective entropy objective 与 RoPE-consistent KV calibration 放入同一 artifact，并在校准分布、kernel layout 和 Decode 路径上联合验收；QAT 负责提出低比特参数，release gate 才决定是否替换高精度路径。

这种联合计划用训练与校准成本换取更完整的 W/A/KV 压缩，却依赖可识别的 reasoning trace 和任务分布；错误的关键步骤标签会把优化预算投向无关位置。作者结果不证明 4-bit 组合对任意模型、语言或长上下文都保持 full-precision 语义，证据不足时应保留 weight-only、较高 KV 精度或完整高精度 fallback。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-15682:end -->

<!-- semantic-body-binding:SF-2026-ARXIV-2606-17566:start -->
#### 分布式 DiT Plan 必须经过编译后拓扑复排

只在 logical mesh 上搜索 DiT sharding 容易把编译器改写、collective lowering 和真实互连成本留到最后，得到语义可行却物理低效的计划。更稳健的 planner 先在 pre-compilation IR 上做高召回可行域剪枝，再用 compiled HLO、设备内存和物理互连拓扑复排候选；compiler 拥有 lowering 后的 execution identity，planner 只在通过 correctness 与容量检查的候选中选择 placement。

两阶段搜索减少完整编译次数，却引入 cost-model 偏差、编译缓存和拓扑版本状态；IR 估计过强会提前删掉优解，物理 profile 过旧又会错误排序。作者实验只覆盖其 DiT 图、编译栈和硬件，动态 shape、故障或未建模通信出现时，应回退已验证的静态计划或扩大搜索，而不能把 logical mesh 名称当作性能证明。
<!-- semantic-body-binding:SF-2026-ARXIV-2606-17566:end -->

### Binary Lifting 的核心是恢复 Typed State

GPU binary 到可分析 IR 的迁移不是指令文本替换：统一 register file 必须恢复 typed state，分支要重建显式 control flow，多指令 pattern 还要恢复组合语义。类型或控制流冲突时，生成貌似可执行的 IR 会把未知语义静默固化，因此 lifter 必须 fail closed 并保留 unsupported instruction surface。Typed LLVM IR 可成为审计和迁移的中间证据，但受支持架构、MUFU/texture 与完整 SIMT 语义限制；原生二进制验证仍不可删除。

<!-- source-family:SF-2026-ARXIV-2604-27486 -->

### Compiler Frontend 是独立的语义故障层

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06052:start -->
### Mixed Precision 可以共享乘法数据通路，但不能共享数值语义

为每种 INT/FP 格式保留独立 MAC，在格式少且资源充足时最容易证明正确；LLM execution plan 需要频繁切换精度时，固定数据路会浪费面积或周期。一条硬件分支把 INT 与 FP mantissa 统一到 shared integer-product datapath，再由 datatype-specific sign、exponent、accumulation 和 dynamic packing 恢复各格式语义。Compiler 选择 dtype/packing，datapath 执行乘积，数值 gate 仍要按算子和模型 slice 验收误差，不能把资源共享当作语义等价。

共享数据路提高 DSP 利用率并支持 cycle-level switching，却增加控制复杂度、累加边界和格式组合验证。现有证据只绑定 AMD Xilinx U55c、披露 formats/kernels 与仿真；component density 不等于 serving goodput，也不能外推 GPU/NPU。shape、dtype 或误差合同越界时，应回退固定精度 MAC 或成熟 backend plan。

<!-- semantic-body-binding:SF-2026-ARXIV-2605-06052:end -->

低层 operator tests 通过，只证明已形成的 IR 或 kernel 在其输入合同下工作；Python control flow、dynamic shape、alias、side effect 与 graph break 在 frontend capture 时就可能被误翻译，随后每一层都只是稳定地执行错误图。Compiler 验收应把 `eager/reference program → captured graph → lowered IR → kernel/runtime` 分阶段做 differential test，并用 root-cause taxonomy 生成 targeted regression；frontend 无法证明等价时回退 eager 或已验证 graph path。

分层测试提高定位性，却增加多表示维护、输入生成和 reference execution 成本；已冻结静态图可把重点留在 lowering/kernel，新模型、dynamic control 或 compiler upgrade 则必须重开 frontend gate。对 TorchDynamo 123 个历史 bug 的分类及由此生成的新 tests 只证明所测 frontend 中该层具有独立 failure surface，不能保证 taxonomy 覆盖未知类别，LLM 也只是归类与生成 proposal，不是 correctness oracle。

<!-- source-family:SF-2026-ARXIV-2607-25651 -->

同一次调用的eager/compiled对照仍可能漏掉cache或context状态引起的错误：第一次结果相同，不代表同一compiled artifact在下一次不同输入、不同execution context下仍保持语义。测试因此需要覆盖调用序列和状态变化，再把alias/view上的in-place写入、layout变换、非计算Python操作与边界数值组合纳入oracle。增加operator种类不是充分替代，因为相同算子只有在特定view关系、优化序列或复用条件下才触发错误。

这种targeted testing增加状态重建与reference成本，也可能被历史taxonomy引导而漏掉未知模式。作者77个可回放correctness case中五套测试合计只检出26例、所有15个graph相关例均漏掉，说明单回调用oracle的覆盖缺口；它不是全部PyTorch部署的错误率。LLM mutation可以提出测试，最终assertions、去重与开发者确认才形成bug证据；静态冻结图可以保持较小回归集，动态capture、context变更或compiler升级时则重开调用序列验收。<!-- source-family:SF-2026-ARXIV-2604-08720 -->

### Distributed Tiling 把 Execution Plan 扩展到层次化拓扑

单设备 kernel tiling 解决寄存器、shared memory 与 tensor core 的局部匹配；模型跨设备后，同一个逻辑算子还要决定 tile 在节点、GPU、通信域与本地 kernel 之间如何分层展开。compiler 应拥有静态依赖、候选 tile 与合法性，runtime 则拥有当前 topology、health、带宽和安全 commit。把两者混在离线计划里，会在设备故障或拓扑变化时留下无法修订的执行假设。

层次化 tiling 可以减少不必要通信并提高 locality，但会增加搜索空间、计划缓存身份和跨层 cost model 误差。运行时证据不足、健康状态变化或验证失败时，应回退到稳定库路径或较粗粒度并行，而不是继续执行未经验证的新计划。传统库仍是常见 shape 与高可靠场景的基线。

<!-- source-family:SF-DITRON-DISTRIBUTED-TILING -->

层次化计划还需要把逻辑张量的 ownership 变成可计算的物理坐标。只给张量 shape 或一组线性 stride，在单份存储时足够；同一个元素在多个设备或线程上复制后，物理位置不再是单值函数。一条布局分支把 device、thread、bank 等资源表达为 named resource axes：D 把逻辑索引映射为所有相关轴上的 base coordinate tuple，可同时包含 lane、warp、register 或 device 坐标；R 枚举与逻辑索引无关的复制 offset 组合；O 则是加到所有结果上的固定轴向 offset。每个逻辑索引 x 的物理位置集合是 `L(x) = {D(x) + r + O | r ∈ R}`，这个集合显式保留同一逻辑元素的多个物理副本。load 或 collective 再从合法副本中选择实际来源，而不是把复制误写成额外的逻辑元素。

这样的 layout 让 compiler 可以在明确的 scope 内推导索引、tile 分布与数据移动，统一单设备 kernel 和跨设备 collective 的坐标语义；它没有接管 runtime 对当前 topology 与 health 的判断，也不自动找到最优 schedule。FP16 GEMM 的 warp 角色、流水线和同步仍需程序员指定，scope lowering 的合法性与执行效率是两个 gate。已有 stride/布局工具在规则 shape 上仍合理，新表示是复制和多资源映射的扩展分支，而非所有 backend 的替代。

统一表示也不保证每种格式都胜过成熟库。作者在 DGX B200 的指定 FP16 GEMM 上接近 cuBLAS，但 block-scaled FP8 仍低于 DeepGEMM；GEMM 与 ReduceScatter 融合的优势又同时包含 fused/non-fused 和 backend 差异，不能全归因于布局语言。采用时应分别验证索引及副本选择的正确性、人工调度成本和匹配 workload 的性能；格式、shape 或通信边界变化后，成熟库路径仍是必要的比较与回退基线。<!-- source-family:SF-2026-ARXIV-2601-19092 -->

### Hardware Fault Recovery 可以从 Bit-exact 降为 Bounded-value

传统 ECC 试图恢复原始 bit，在控制状态、索引或高敏感参数上仍是最清楚的正确性合同；但它的冗余与解码成本会随保护强度增加。神经网络张量的部分数据允许小幅数值偏差，却不能容忍任意 bit flip 把指数位或高位改成极端值。一条受限分支先由数据计算 Range Identifier（RID），再按 RID 生成并保存 ECC 冗余；显式 RID 随后丢弃。读出时从受损数据重新生成 RID、结合冗余解码，在无法 bit-exact 恢复时把结果替换为该范围的代表值，从而把合同改成 bounded approximate recovery。

该机制证明的是指定 fault model 与张量范围下的有界恢复，不是 kernel 数值误差的在线检测，也不包含“超界后局部重算或自动提高精度”的通用执行路径。它用更少保护开销换取非 bit-exact 结果，并新增 RID 重建错误、范围失配、敏感张量误分类与多错误累积风险。范围无法稳定校准、数据不具容错性或请求风险较高时，应回退完整 ECC、冗余校验或重新执行；部署验收仍要把硬件 fault injection 与模型质量共同测量。

<!-- source-family:SF-RANGEGUARD-EFFICIENT-BOUNDED-APPROXIMATE-ERROR-CORRECTION-FOR-RELIABLE-D -->

运行时检测与回退并非在所有执行合同中都可用。若加密推理要求计算电路不根据密文内容改变工作量，直接把明文侧的动态 early exit 搬过去就会破坏这一前提；近似预算可以改在离线分配：训练时为不同算子位置学习迭代深度的松弛分布，同时调整模型权重，随后为每个位置选择固定迭代次数，并在这一离散电路下继续适应权重。部署时所有输入执行同一位置预算，而不是在服务器上读取密文状态后决定是否退出。这里变化的是近似计算的控制权从在线请求迁移到训练与编译产物；低深度先验只是成本代理，不能直接充当实际 bootstrap 次数或端到端时延。

这种分支用训练、校准和权重—电路耦合换取较少的固定计算，但没有消除误差验收。训练中的范围限制不等于部署输入始终落在收敛域，部分非线性还可能在训练与部署使用不同实现；packing、密码参数和输入分布改变后，都需要重新验证。参数复用、训练预算不足或校准域不稳定时，较保守的固定近似仍更易审计；明文执行允许可靠检测时，在线 correction 仍是另一条成立的路径。单一小模型的 teacher-forced 加密链只能支持这种有限机制，不能证明自由生成质量、通用低延迟服务或密码安全认证。
<!-- source-family:SF-2026-ARXIV-2609-01730 -->

### Quantization Correctness 不能只看 Accuracy

模型量化保持 aggregate accuracy 时，通常被视为语义等价；对会给出 counterfactual recourse 的系统，同一个建议在 full-precision 模型上有效，却可能在 quantized decision boundary 上失效。执行计划验收因此应加入 Validity Drop 与 minimal Recourse Cost Gap 等 task-specific invariants，而不是只测输出一致率。

这些指标揭示决策边界漂移，却依赖可计算的 recourse oracle，作者在表格分类任务上的结果不能外推到 LLM serving。若产品不提供 recourse，可继续使用常规质量切片；一旦输出会驱动可行动建议，就必须在目标 dtype/kernel 上重验，失败时提高精度或回退原 engine。

<!-- source-family:SF-2026-ARXIV-2605-17160 -->

## Kernel Agent 应生成 Typed Schedule，而不是自由文本 Patch

自由文本 kernel 代码很难表达 tile、memory hierarchy、synchronization 和 target hardware 的约束，错误也只能在最终编译或 benchmark 暴露。typed schedule IR 把这些选择变成可验证对象，由 verifier 检查语义、成本模型估计候选，再用局部诊断驱动修正。

该闭环把 Agent proposal 与 compiler/runtime commit 分开，却依赖 IR 对算子和架构的表达能力；无法表示的新 pattern 仍需人工或回退成熟 kernel。收益必须在完整 model execution plan 中验证，不能用 standalone kernel speedup 替代端到端结果。

### Execution Plan 必须联合逻辑稀疏、Tensor Lifetime 与硬件数据流

模型层声明量化、稀疏或局部依赖，并不自动产生更快执行。权重解量化若仍在通用 compute path materialize 大张量，会把节省重新付给 HBM 流量；sparse attention 若把 indexer 与 TopK 分成多个 kernel，也会被中间写回与 launch 吞噬。更完整的 lowering 把解量化贴近 HBM 读取，把 index generation、selection 与 gather 融合，同时保留 reference kernel 和形状/稀疏度阈值作为 fallback。

Diffusion workload 进一步暴露跨 step 的 tensor lifetime。template-static graph 可提前联合规划 memory mitigation、layout、parallelism、concurrency 与 SLO；区域依赖允许只更新活跃块，但 stale state 必须有误差 guard 和 full-recompute 回退。静态模板与稳定 denoising schedule 能获得最大收益，data-dependent shape 或误差界失效时动态执行仍更正确。

### Chiplet Pool 与 Execution Plan 必须联合演化

同构加速器池在 workload 稳定、采购规模足以摊薄设计成本时，故障域和编译目标都最简单；为每个模型设计专用芯片又会把
非经常性工程成本和库存碎片放大。模型族同时包含 dense/MoE、Prefill/Decode 与不同 memory/compute ratio 后，固定 chiplet
pool 仍可能把某个 stage 的瓶颈固化。更完整的 co-design 让平台拥有长期 pool/inventory identity，而 compiler 为每个
workload 生成可变 execution plan：先联合选择 compute/memory/interconnect chiplet，随后决定 fusion、tensor lifetime 与
数据搬运，再把 stage 映射到满足等延迟的 pipeline，最后才进行物理布局和布线。Pipeline bottleneck 是两层共享状态，
不能由芯片 catalog 或单个 kernel 独自决定。

这种联合搜索用更高 compiler、profiling、P&R、热设计和供应链复杂度换取跨 workload 复用；未来模型漂移、cost model 失真
或布局不可实现会让纸面 Pareto 失效。稳定工作负载或同构器件已满足 SLO 时，成熟单芯片/固定 pool 仍是更可验证的基线；
新 family 不在支持域时，应增加可替换 chiplet 或回退通用执行路径。`arXiv:2609.10970v1` 的收益来自 Timeloop、Accelergy、
CENT 与 CACTI 驱动的模拟和所列 Llama/Qwen workloads；相关性与消融支持 co-design 机制，但不等于已制造 silicon 的绝对
latency、能耗或可靠性证明，Qwen Decode 的有限收益也说明该分支并非处处优胜。

<!-- source-family:SF-2026-ARXIV-2609-10970 -->

### 架构收益必须贯穿完整 Serving Pipeline

Hybrid SWA 的较低理论复杂度只有在 Full/SWA dual KV pool、window-safe prefix identity、layerwise prefetch、跨 tier 一致性和 affinity/load-aware routing 同时成立时才变成生产收益。MoE placement、length bucketing、NUMA 与 multimodal preprocessing 也会重新定义 Prefill/Decode 的 critical path。单独优化 kernel 或 cache 命中率会把瓶颈推给下一阶段，因此 execution plan 的身份必须覆盖模型结构、KV semantics、router、distributed cache、host topology 和 modality pipeline。

硬件选择也不能只比较峰值 FLOPs。Decode 应联合计算强度、权重/KV capacity、memory/fabric bandwidth 与 service arrival shape，并把候选计划放回完整请求生命周期验证；稳定模型和单一平台继续适合人工维护的保守 plan。

这些 source-specific 结果均绑定作者模型、GPU、精度、长度、batch/concurrency 与披露 SLO；未披露项不能被补成通用性能结论。

<!-- source-family:SF-2026-ARXIV-2607-08993 -->
<!-- source-family:SF-2026-ARXIV-2607-11136 -->
<!-- source-family:SF-2026-ARXIV-2607-11976 -->
<!-- source-family:SF-2026-ARXIV-2607-12121 -->
<!-- source-family:SF-2026-ARXIV-2607-13068 -->
<!-- source-family:SF-2026-ARXIV-2607-13095 -->

### 量化算法必须区分“选择误差度量”与“忠实执行更新轨迹”

二阶量化常把重点放在 Hessian 或左右 basis 怎样近似误差，却容易把随后 rounding sweep 当成无关实现细节。若矩阵更新彼此依赖，遍历顺序本身就是算法语义；并行化只有在能证明与既定 fixed-order trajectory 等价时，才是安全的 execution-plan 变换。

双侧 Kronecker 度量下的 anti-diagonal sweep 展示了一个受限例子：它可以降低理论执行复杂度，同时保持指定更新序列的等价结果。但该证明不负责 basis 估计，也没有给出 LLM quality、GPU kernel 或端到端 latency 证据；临时状态、数值顺序和硬件映射仍可能吞掉理论收益。因此 compiler/runtime 应分别记录 metric identity、rounding order、arithmetic 与 kernel evidence，缺少端到端验证时回退 reference quantization path。

<!-- source-family:SF-2026-ARXIV-2607-27042 -->

### 代数等价变换可以成为 data-movement 优化，但必须单独验收执行语义

在 PIM 上直接 materialize `N x N` attention intermediate，会让跨 bank traffic 随序列长度二次增长；重排等价算式、只交换 `d x d` 局部聚合可以把通信压力降到线性量级。这里的收益来自改变 materialization 和数据流，而不是减少模型语义工作。

专用组织和模拟结果不能外推 GPU 或现有 PIM 产品；运算重排还会改变舍入、layout、bank capacity 与同步。execution plan 必须同时验证数值等价、bank/interconnect 约束和端到端 workload，超界时保留 dense GPU path。

<!-- source-family:SF-2026-ARXIV-2607-21731 -->

### 数学表示决定 state materialization 与异构硬件划分

矩阵化 state-space duality 便于训练和 dense accelerator，却可能 materialize 大中间量；代数等价的 streaming recurrence 可以让 dense projection 留在 in-memory units，而把有序 state update 交给专用 stream engine。优化对象因而是“同一模型计算采用哪种状态表示”，而不只是把算子搬到新硬件。

模拟/专用 accelerator 假设没有证明可制造性或通用端到端 latency，递归顺序、数值误差、fabric 和 state lifetime 都是新增约束。只有 reference equivalence 与真实 workload 通过时才采用；成熟 GPU 路径仍是兼容、调试和故障回退。

<!-- source-family:SF-2026-ARXIV-2607-22022 -->

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

### 从局部结果到可执行的系统边界

<!-- body-source:SF-2026-ARXIV-2606-23743 -->
video inference optimization 应把 graph transformation、kernel/execution plan、memory schedule 与 serving config 绑定同一可重建 artifact；agent 只能提出/搜索 plan，validator 才能提交。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；收益 instance-specific 于模型、硬件和 serving config，最终 visual quality 仍需人评；不能把单次搜索结果外推通用 engine。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。

## 从机制演进到系统设计

Execution engine 从调用通用 kernel library 演进到 JIT、superoptimization 和 profile-guided search 后，搜索器只能提出 plan，correctness validator 与 target hardware measurement 才能提交 plan。模型 graph、dtype/layout、kernel、memory schedule 与 serving config 必须形成同一可重建 artifact。

专用 plan 能压低局部 kernel 成本，却增加搜索时间、shape specialization、数值偏差和 artifact explosion。硬件、batch、precision 或模型 revision 变化后必须失效并重新验证；通用 library 路径始终作为 coverage 和 correctness fallback。单次 benchmark 的最快 kernel 不能外推为完整 Serving engine 的最优计划。

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

### 异构执行计划要按算子的数据移动特征分配位置

Attention、状态空间层与 MoE 的瓶颈并不相同：有的受复用和带宽约束，有的受稀疏权重搬运与路由约束。统一把它们放到同一计算层会让局部 kernel 优化被跨层数据移动抵消。执行计划应以算子状态、可复用性、互联成本和回退路径决定 placement；near-memory 或专用单元的模拟结果只能说明一个候选 operating point，不能替代真实硬件上的端到端验证。
<!-- source-family: arxiv:2608.22613v1; semantic-body-binding: heterogeneous-operator-global-placement -->

### Quantization Transform 与 Number Format 必须共同选型

旋转、缩放或其他 transform 的排序并不独立于量化格式：variable-bit allocation、group shared scale 和数值编码会改变 transform 要优化的误差形状，甚至反转原先更优的选择。编译器因此不能先固定 transform 再替换 format；它要把校准数据、grouping、bit allocation、kernel 支持和质量目标编成同一个 plan，并为超出校准分布的层保留回退。
<!-- source-family: arxiv:2608.25188v1; semantic-body-binding: quantization-transform-format-joint-plan -->

### Communication Lowering 应先利用 Reduction Algebra

collective 的物理 routing 之前仍有一层逻辑优化空间：根据 reduction 的结合性、交换性和 carrier 结构，编译器可以重写依赖图、缩小中间状态，再映射到 mesh。收益来自少搬数据而不只是寻找更短路径；代价是必须证明重写保持数值与同步语义，并把 precision、chunking 和失败恢复纳入 plan identity。
<!-- source-family: arxiv:2608.26220v1; semantic-body-binding: reduction-algebra-before-routing -->

### Generated Kernel 必须先进入 Typed Schedule IR

模型生成的 kernel 或 schedule 不应直接进入性能竞争。先把 shape、dtype、layout、memory effect 和并行决策编成 typed IR，再由 verifier 检查正确性，并用局部 cost feedback 指向需要修改的节点，才能形成可恢复的 compiler loop。验证与 IR 限制会降低搜索自由度，却把“能编译”和“在目标 contract 下正确且更快”分开。
<!-- source-family: arxiv:2608.12629v1; semantic-body-binding: generated-kernel-typed-schedule-ir -->

<!-- semantic-body-binding:SF-2026-ARXIV-2605-05023:start -->
从空白生成完整 CUDA kernel 给模型最大自由度，却让正确性、低层语义和性能搜索同时失控。对已有高质量 kernel 的新 attention 变体，更窄的分支是先把 source kernel 提升为可执行 IR，显式保存 tile、memory movement、同步与 orchestration；模型只迁移语义差异，再由 lowering 和数值 verifier 生成目标实现。这样 source artifact 与 IR owner 保留执行事实，模型只拥有 transformation proposal，benchmark runner 才拥有 acceptance。

该路径把搜索空间缩小为可验证变换，代价是依赖可信 expert kernel、IR 表达力与 target backend lowering；source 不存在、语义超出 IR 或新硬件缺少映射时，仍需通用 compiler、模板或人工实现。`arXiv:2605.05023v1` 的 §3–§4 与 A100/H100 attention 评测支持 CuIR 的 lift–transfer–lower 案例；§Limitations 明确未验证非 attention HPC workload，且非主流硬件缺少源 kernel 时能力受限，因此不能把作者 TFLOPS 外推任意 shape、GPU、并发或生产 SLO。
<!-- semantic-body-binding:SF-2026-ARXIV-2605-05023:end -->

### MoE 量化损伤要拆成 Compute Error 与 Routing Mediator

router 的 margin 只能说明路由是否容易翻转，不能说明翻转后的 expert 会造成多大输出误差。诊断应分别运行量化、冻结原路由、只替换路由和参考路径，把计算误差与 routing-mediated error 拆开，再决定保护 gate、expert 或执行格式。更细的因果 profiling 增加成本，却避免把高精度预算浪费在无害 route flip 上。
<!-- source-family: arxiv:2608.11212v1; semantic-body-binding: moe-quantization-routing-mediated-error -->

### 量化发布必须按语言与任务切片

总体平均质量相近，仍可能掩盖某些语言、文字体系或 tool/safety decision family 的非对称退化。量化 artifact 的身份应同时绑定模型、位宽、校准集和执行格式，并以语言、typology 与任务切片设置 release gate；切片样本不足时标记未知，而不是用总均值放行。更细评测增加成本，但能把格式收益与不可接受的局部行为翻转分开。
<!-- source-family: arxiv:2608.09941v1; semantic-body-binding: quantization-release-by-language-and-task-slice -->

### 离线权重重建是量化的一条条件分支

直接舍入把每个权重独立映射到低比特网格，简单且容易复现；当层间误差累积成为主要约束时，可用生成式或迭代式重建在离线阶段联合选择 rounding。它不改变运行时格式，却把成本移动到校准、层选择与离线搜索，并可能过拟合重建分布。采用前必须在同一 runtime format 下同时验收离线成本、目标任务质量和未重建层的回退路径。
<!-- source-family: arxiv:2608.11045v1; semantic-body-binding: offline-generative-weight-reconstruction-quantization-branch -->

## 小结

TensorRT-LLM 把模型、NVIDIA GPU 和 Serving runtime 联结成经过优化的 execution contract。GEMM 执行从 `M/N/K` 和 dtype/layout contract 出发：cuBLASLt 用广覆盖的 heuristic kernel space 交付通用路径，DeepGEMM 一类专用库用 JIT、TMA、MMA 和模型特定 layout 换取更深优化。二者可以在同一 runtime 中共存。MoE 还要求 execution plan 把 activated-expert weight floor、token/tile compute、expert placement 与 communication 放入同一条件成本模型，不能把 token count 当成跨 regime 的固定时间代理。

Quantization 只有与明确的 graph mapping、可用 kernels 和目标硬件对齐，必要时再进行 structural rewrite，才可能把更少 bytes 转化为更低单步成本；层并行 correction 与 CPU-GPU expert co-execution 都只是带收敛、硬件和 workload 条件的执行分支。in-flight batching 和 paged KV 则管理持续到来的 request state。

下一章转向 vLLM，观察另一个历史起点：如果首先把 KV allocation 与 scheduler 视为核心，完整 Serving engine 会怎样组织。

## Review notes

- `SF-2026-ARXIV-2602-18116` — Daily `2026-02-24`；[exact-v1](https://arxiv.org/html/2602.18116v1) §2.2–2.3/Theorem2.1、§3/Table1、§4及§5。2+1+2=5，clustermean投影/下一层适配具体缺口深入；one-rank slack、parameter-Lipschitz上界非matchedrank质量定律，small60M/130M与学习率反侧、reset/恢复/kernel成本近正文，不授function精确等价或部署加速。root必要源/actualowner PRE通过，作者实际正文/完整邻接及自身末注顺读、limiteddiffcheck通过，root非作者实际POST通过，窄锁释放。未核实现/复现，非日级验收。

- `SF-2026-ARXIV-2602-14432` — Daily `2026-02-18`；[S²D exact-v1](https://arxiv.org/html/2602.14432v1) §4谱式/PCDR、§5必要配置/反侧/5.5成本。2+2+2=6，training conditioning→PTQ/QAT具体差额深入；范数上界非唯一outlier归因，top3/.95/100步缓存与8×A100 18s/6s明确，PTQ4ViT512 W4A4 4.2→3.8反侧保留，不采用隐藏3iter等于零费用。root必要源/actual owner PRE及实际正文/完整邻接与末注非作者POST通过，窄锁释放；未核artifact或复现，非日级。

- `SF-2026-ARXIV-2602-14452` — Daily `2026-02-18`；[WiSparse exact-v1](https://arxiv.org/html/2602.14452v1) Eq4–7、§4及必要 calibration/runtime 段。2+1+2=5，weight/activation 联合 score 与动态 support 的具体差额深入；固定阈值不固定人口，搜索/索引计费及 FLOPs/速度、batch/precision/SLO 边界近正文。root 必要原源/实际 owner PRE通过并授窄锁；实际正文/完整邻接/本末注经root非作者POST通过，锁释放。未核代码或复现，非日级Gate。

- `SF-2026-ARXIV-2602-12962`，Experimental：[exact-v1](https://arxiv.org/html/2602.12962v1) V-A/Eq6–10与VII/TableIV–VI；采用MX共享exponent轴、compile-time整数weight转置及合法scale后移的consumer合同，不采用任意矩阵交换/scale穿softmax或全部2.73×单因果。保留trans.opt局部1.77%、PPL反退、固定模拟/RTL14nm与格式/带宽条件；必要源和actual owner PRE已root实核，一段移至粒度定义之后，实际正文/完整邻接/末注已root非作者最终POST通过，锁释放，不授日级完成。

- `SF-2026-ARXIV-2602-12609`，Experimental：[exact-v1](https://arxiv.org/html/2602.12609v1) §3–4、Table4/6；采用嵌套补偿容量与跨位宽校准输入耦合，不采用逐格式均优、免费动态切换或真实LLM kernel加速。固定rank48/高位反退、feature merge与MAE混杂、adapter与逐格式验收成本保留；作者必要源和owner PRE已root独核，实际一段与完整邻接/末注已root非作者POST通过，锁释放，不授日级完成。

- `SF-2026-ARXIV-2602-10718` — Daily `2026-02-13`；[SnapMLA exact-v1](https://arxiv.org/html/2602.10718v1) §3–4、Table2 与 Appendix C。2+2+2=6，共享 KV scale 在 PV reduction 轴及 online state 差额深入；QK 同域、scaled P/真实分母、输出 rescale 与双 buffer readiness 分责，不授 BF16 RoPE 无损或同 batch/concurrency 的倍率。作者有限 Hopper/DS-v3.1/LongCat 结果，未核代码或复现；root必要源/owner及相邻章节写前通过，root实际正文/前后邻接及末注非作者POST通过，窄锁释放，不授日级Gate。

- `SF-2026-ARXIV-2602-06127` — Daily `2026-02-10`；[MoP exact-v1](https://arxiv.org/html/2602.06127v1) §3.2–3.3、§4.1.1/Figure2、§4.2–4.4。2+1+2=5标准，采用等参数结构粒度与选择器分账及random≈proxy反侧；不授PPL选择优越、三seed稳健保证或跨baseline匹配。LLaMA2-7B、RTX4090、输入12/输出128、batch1，20runs弃10warmup；precision/concurrency/SLO未披露，不采用39%通用收益。未核代码或复现；root必要原源与owner写前通过，实际正文及前后邻接写后非作者复核通过，日级Gate未授。

- `SF-2026-ARXIV-2601-01765` — Daily `2026-01-07`；[RTL优化 exact-v1](https://arxiv.org/html/2601.01765v1) §2.1–2.3/3.3.1–3/4.1。3+1+2=6，后端优化抹掉source改写收益的具体设计反证gap深入；DC/Yosys、clock/library与43/54成功转换人口保留，Formality功能等价与VCS有限时序不作all-hardware proof或实芯PPA。feb01_v3实际必要原源/Ch49 owner非作者写前核通过，root授权窄写；root实际新增段/邻接/末注非作者POST通过，未运行代码或复现。

- `SF-2026-ARXIV-2601-00227`（Experimental）：[FlashInfer-Bench exact-v1](https://arxiv.org/html/2601.00227v1)，§3.3、§4.5。只采用 deterministic/low-precision 与 stochastic sampling 的不同验收对象，以及 isolated/persistent context 的测量边界；有限 TVD 不等 exact 分布证明。2025-10-21 官方 Blog 已有 typed Trace/apply/fallback，本次不重复作为新机制。§4.5 的有限 SGLang/Llama3.1-8B、RMSNorm/h4096、concurrency1/16/64 对照不证明生成解优于 native 或生产 SLO；长度/统计不确定性=`Not Disclosed`。root 必要 source→具体 owner 及实际新增正文/邻接的非作者写后复核通过；未运行 artifact。

- `SF-2026-ARXIV-2603-02883` — [SemanticDialect exact-v1](https://arxiv.org/html/2603.02883v1)，Daily `2026-03-05`；必要 §3.1–3.4、§4.1–4.7/Table4、Appendix D/F。6分，因跨块选择耦合的具体知识缺口深入必要命题；仅采用8-dialect sub-formatbook关联约束，不强制同一dialect。Table4的FVD-FP16是相对FP16特征分布，不是人工真实性；加SeDA后部分CLIP/Flow维度退步，AppF窗口与更新频率非单调。v1硬件/RTL为future，不采用后续v3性能事实；未复现。root已实际对读必要源、新增正文与邻接，非作者 POST 通过。

- Daily 2026-04-30：RaMP [exact-v1 §IV–V](https://arxiv.org/pdf/2604.26039v1) 与 CoQuant [exact-v1 §3.2/§4–5](https://arxiv.org/html/2604.26378v1)，apr29_close 独立窄 source→owner 通过；作者实际写入配置选择/共享高精度子空间，root已实际读取正文及前后衔接，非作者写后通过。不采用并发 SLO 或无专 kernel 的加速结论。

- [SchurReplay v1](https://arxiv.org/html/2609.36654v1) §4.1–4.2.1、§5.1/5.3；Daily 2026-09-30。连续 future-compensation metric 与实际离散候选回放分开；不证明全模型最优或 Serving 提速。
- [ParaAnya v1](https://arxiv.org/html/2609.36522v1) §2–4；Daily 2026-09-30。同 timestep 跨迭代近似缓存；低阈值减少NFE仍可能变慢，多设备对单设备不是同资源收益。未复现实验。

- `SF-2026-ARXIV-2604-23467`：[exact-v1](https://arxiv.org/html/2604.23467v1) §III Algorithm 1、§IV–VI、Tables I–II；04/28 arXiv v1 归窗按官方公告、连续 ID、OAI 与 08:42 Updated 作 08:00～09:00 有据推断，非逐篇秒级时刻。只采用预捕获→miss 时 JIT 执行并异步 capture→事件完成后 rolling-cache replay 的生命周期；动态段保留 JIT，首次 capture、显存、淘汰与 cuBLAS 串行成本不能忽略。Table II 350/500-token 逐 token P99 反于“全部长度最低”的正文叙述；受测单 H100/FP16/LLaMA-2 7B/batch 1/warm-start 不证明并发或整请求 SLO。root 已完成必要 exact-v1、日期、Ch49 写前核及实际正文/相邻交接的非作者写后复核；未复现实验，不替代 04/28 整日 Gate。

- `SF-2026-ARXIV-2604-19884`（Experimental）：[exact-v1](https://arxiv.org/html/2604.19884v1) §3.1–3.4、§4.1–4.3、Appendix A/C–E；04/23 Daily 仍待整日日期/覆盖 Gate。采用同一失败 cohort 上的可读信号与处理路径失效辨别及局部干预—回退机制；`Failure Subset` 预选 FP16 正确/4-bit 错误，Table1 的 0% 是条件分母；修复为约4.1/4.25平均 bit 加放大，不是同存储预算；2-bit 负例限作者四个7–9B模型、GPTQ/AWQ、Pararel及所测干预，不推一般不可逆。apr01 已做 exact-v1→实际 Ch49 的有限非作者采用核，root 已顺读本次正文及量化验收前后交接并作写后核验；未复现实验。

- `SF-2026-ARXIV-2604-20032`（Experimental）：[exact-v1](https://arxiv.org/html/2604.20032v1) §III-B～E、§V、§VI-D、§VIII；04/23 Daily 待整日日期/覆盖 Gate。只采用 PC stall 症状→register/predicate/vendor wait 依赖→可测试 source 假设的诊断链；四阶段剪枝与 blame 是启发式，不是逐链因果证明。21 workload 几何平均含大量 HPC 和专家人工修改；llama.cpp Qwen2.5-1.5B/Q4_K_M 在 MI300A 的 `mul_mat_q` 为 1.12×、GH200 为 1.00×，HipKittens MI300A RMSNorm 为 1.07～1.24×，均非整服务 SLO。apr20_resume 已做必要来源→实际 Ch49 的有限非作者采用核；root 已顺读本次正文及 TaxBreak/WebGPU 前后交接并作写后核验，未复现实验。

- `SF-2026-ARXIV-2604-22032`（Experimental / Specification proposal）：[exact-v1](https://arxiv.org/html/2604.22032v1) §3.1、§3.4、§5.1–5.3、§8.2–8.3 与附录 B；Daily `2026-04-27`。采用 per-kernel scope/pre/post/tolerance/reference/measurement/violation 的合同与三态控制样本，将一次 smoke pass 与跨环境 admission 分离；12 类多为已发表案例，示意测试、占位容差、未覆盖组合/分布式语义不能宣称完整证明或厂商故障率。root 必要来源→实际 owner 写前独立复核与实际正文/相邻写后复核均通过；未复现实验，不代替整日报 Gate。

- `SF-2026-ARXIV-2604-15464`（RPA；Experimental）：[exact-v1](https://arxiv.org/html/2604.15464v1) §3.1–3.7/Algorithm1、§4.1–4.4。仅采用静态 capacity、有效 ragged 分布及 compiler layout survival 分责；TPU7x/Llama3-8B/BF16、d=128 MFU 的50%最大MXU调整、prefill preprocessing约2%～8%均限作者协议。mixed配置优化未全支持，不采全请求/质量/CI/生产SLO保证；2025 artifact release不重复算首次论文。root必要源→实际owner与literal有限独立采用通过；root 实际顺读新正文与前后编译执行分支后，非作者写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-15379`：[Fleet v1](https://arxiv.org/html/2604.15379v1)，§3.1/4.1/5.1–5.3/6.1–6.4/Table4–5/8。仅采用 partitioned-L2 中的 chiplet task placement、局部计数和 last-worker 跨 die 可见性分责；保常驻资源、低 batch/fusion 非局部性归因、M-split HBM 反增及 batch64 对 vLLM 反退，不采摘要替代 Table4 或任意 memory model 免 fence。6分实际owner缺口深入，root必要源→实际owner/literal独立通过；root真实两段及相邻衔接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-18610`：[official v1](https://arxiv.org/html/2604.18610v1)，§2.2–2.3/3.1–3.4/Eqs3–14、§4.2 Tables4–5及§4.3。采用指定activation整数码的binary spike时间加权累积及scale/时间预算执行接口，不称weights全binary或任意浮点等价。Qwen2VL7B MAC/AC与SMIC28nm综合/ARM SRAM/HBM/cycle模拟对A800 FP16/batch1分开；不采用同硬件部署倍率/生产SLO。6分真实知识缺口深入，root必要source→actual owner及literal非作者通过；本次实际正文与相邻衔接写后独立复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-18655`：[exact-v1](https://arxiv.org/html/2604.18655v1)，§3.1–3.5/Tables2–6/Limitations及A.1。正文只采用同shape adapter runtime输入ABI与graph/adapter/KV分责；CTG suffix隔离非任意prefix共享、INT8/INT16不同分支、Table3算式与相对G-Eval边界保留。root必要source→actual-owner及实际正文/相邻衔接非作者写后通过；未复现。

- `SF-2026-ARXIV-2604-20913` — [FairyFuse v1](https://arxiv.org/html/2604.20913v1)，§3/Alg1、§5.1/§5.4–5.5/Table6：无LUT ternary条件加减与多子GEMV共享解码；scale仍乘法，不采用跨线程宣传倍数或GPU普遍反收益。5分真实长期缺口必要深入，source→actual-owner及实际正文/相邻衔接写后非作者root通过；未复现实验。

- `SF-2026-ARXIV-2604-18616`：[官方PDF-v1](https://arxiv.org/pdf/2604.18616v1) §3–7/9.3–9.4。仅采用layout传播的逐元素关系标签/反例反馈，不采任意kernel等价；path-insensitive/top、memory/loop限制与MI300X质量/速度分账保留。6分具体缺口深入，apr20_resume必要来源/实际owner独立采用通过，root literal采用通过；root非作者实际正文及相邻衔接写后核验通过，未复现实验。

- `SF-2026-ARXIV-2604-10496`（Experimental）：[v1 §3.1–3.4、§4.1/4.3–4.4](https://arxiv.org/html/2604.10496v1)。采用 nonuniform centroid/assignment 与 activation-product LUT 的表示/执行接口共同计划，保留变换合法性、router变化、校准、decode/布局成本。GPU新路径为Accel-Sim，不称A100实机kernel收益；CPU与GPU证据分开，不采无损或生产SLO。apr01 必要源→实际 owner 写前通过，apr01 已顺读实际正文和相邻衔接，写后独立通过；未复现实验。

- `SF-2026-ARXIV-2604-18788`：[arXiv:2604.18788v1 §3.1–3.3、§4.1–4.3、§5.1/5.6–5.8](https://arxiv.org/html/2604.18788v1)。正文采用静态 shape 后端的 capacity tier×expert group×graph residency 条件分支，明确预置 CPU graph placement 与 overflow pruning 不同。M2 Max 64GB / M2 Ultra 192GB，Phi-3.5-MoE / Phi-tiny / Qwen3-30B-A3B，FP16，prompt 1024/4096、chunk 256/512/1024、平均 decode 8 tokens；并发和生产 tail SLO 未披露。root 已完成必要来源及当前 owner 写前非作者核，并实际顺读正文与相邻衔接，写后独立复核通过；未复现实验，不采用效率无质量代价或 latency/energy 同时最优保证。

- `SF-2026-ARXIV-2604-17198`：[official PDF v1](https://arxiv.org/pdf/2604.17198v1)，Daily 2026-04-21；§3.1–3.3/Theorem3.1/§4.2–4.4/§5。采用实际 sparse coiteration cost 的分区身份，outer intersection 先有效坐标发现/重映射，成本界非 wall-clock；assembly/scatter/metadata 与 SpGEMM 反例保留。apr02 必要 official PDF→当前 owner 独立通过，截断本地下载不作证据；实际正文及相邻衔接写后非作者复核通过（root），未复现实验。

- `SF-2026-ARXIV-2604-09975`，Experimental：[exact-v1](https://arxiv.org/html/2604.09975v1) §III、§V–VII及IX。仅采用FHE/MPC stage-compatible packing与数值/转换payload共同计划；不采用最少转换次数即最优、通用round-trip误差或真实WAN服务保证。semi-honest及近似算子边界保留，Security仍为安全owner。apr02必要来源→实际owner及真实正文/相邻衔接写后复核通过，未复现实验。

- `SF-2026-ARXIV-2604-13287`（Experimental）：[MOONSHOT exact-v1](https://arxiv.org/html/2604.13287v1) §2.1–2.3/Algorithm1、§3.3/Table3、Appendix A.3/A.7；只采用归一化重构/empirical-Fisher 混合目标与共享基底低秩求逆，保留梯度近似、可逆性、离线成本及 2:4 质量退步，不采用全局最优或 runtime 提速。apr01 与 root 必要源→实际 owner 独立采用通过；root已实际顺读本次正文及相邻交接，非作者写后通过，未复现实验。
- `SF-2026-ARXIV-2604-13319`（Experimental）：[Tensor Memory Engine exact-v1](https://arxiv.org/html/2604.13319v1) §3/Eq1–4、§6.1–6.3；只采用 CPU 计算与 alias-view 访存重组职责，保留 burst 放大、SIMD/Conv2D 反例、Kria KR260/Cortex-A53/300 MHz FPGA/DDR4 平台及物化回退，不推 GPU/LLM/SLO。apr01 与 root 必要源→实际 owner 独立采用通过；root已实际顺读本次正文及相邻交接，非作者写后通过，未复现实验。
- `SF-2026-ARXIV-2604-13440`（Experimental）：[KLQuant exact-v1](https://arxiv.org/html/2604.13440v1) §3/Algorithm1、§4.1/Eq1–6、§5.2/§6.1/§7.1/Table4；只采用逐层输出分布扰动指导混合位宽 proposal，teacher-law/测试标签分布与 KL 方向分开；Q/DQ 不冒充原生 kernel，模型/配置混杂和在线合同未披露保留。apr01 与 root 必要源→实际 owner 独立采用通过；root已实际顺读本次正文及相邻交接，非作者写后通过，未复现实验。
- `SF-2026-ARXIV-2604-13806`（Experimental）：[DASHQ exact-v1](https://arxiv.org/html/2604.13806v1) §3–5/Eq8–11/Algorithm1、§6/Table1/§7.2；只采用有限样本曲率偏差/方差取舍与固定整数码下的对角加权 ridge 拟合，保留相关性丢失、离散联合优化未证和校准成本，不推 Serving 吞吐。apr01 与 root 必要源→实际 owner 独立采用通过；root已实际顺读本次正文及相邻交接，非作者写后通过，未复现实验。

- `SF-2026-ARXIV-2604-12798`（Experimental）：[exact-v1](https://arxiv.org/html/2604.12798v1) Algorithm1/§3.1、§5.2–5.4/Table2。采用 key summary→局部真 max→冻结 shift 仍累计所有块的执行分工；实数 shift 抵消不作有限精度证明，HumanEval 反例及预计算/重排成本保留。root 必要源/owner 与实际两段及相邻交接写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-14825`（Experimental）：[Nautilus exact-v1](https://arxiv.org/html/2604.14825v1) §4.2–4.4/§5/§8/Table4；采用 scalar→VR-tile→MA-tile 的职责分离与 repair/live-range 成本，不采用全栈普遍更快。必要 source→owner 已通过，root实际重开必要原文、正文及相邻交接，写后独立通过，未复现实验。
- `SF-2026-ARXIV-2604-15167`（Experimental）：[exact-v1](https://arxiv.org/html/2604.15167v1) §3–5.2/Appendix A/B；采用 checkpoint×probe 独立质量检查，INT4/INT8 grouping 与对称性混杂、浮点质量代价就近保留，不采用唯一原因或通用训练配方。必要 source→owner 已通过，root实际重开必要原文、正文及相邻交接，写后独立通过，未复现实验。
- `SF-2026-ARXIV-2604-14626`（Experimental）：[ELMoE-3D exact-v1](https://arxiv.org/html/2604.14626v1) §4.1–5.2/Algorithm1/§6–7/Table3；采用共同整数网格的 bit/tier 分工与 projection-boundary partial-sum 合并，不把模拟或量化-target verification 推成实机收益/浮点无损。必要 source→owner 已通过，root实际重开必要原文、正文及相邻交接，写后独立通过，未复现实验。

- `SF-2026-ARXIV-2604-13327`（Experimental）：[Event Tensor exact-v1](https://arxiv.org/html/2604.13327v1) §2.1–2.4、§3.1–3.4、§4/Tables1–3。采用 symbolic-shape/event IR→counter/notify/wait 与 static/dynamic 调度分支；static shape 采样及共同E[0]保守依赖、dynamic集中队列、Table2单token .95/Table3动态dense .82–.89和端到端SGLang反向均保留；warmup35s另有离线107s编译。8B200/NVLink/torch2.8/CUDA13/driver580.82，Qwen3 input512/output100/batch1–128；precision/concurrency/SLO未披露，不采普遍收益或形式可见性保证。2+2+2=6、缺口深入；root必要原文/owner独立通过，实际写后待非作者核，未复现实验。

- `SF-2026-ARXIV-2604-08118`：[exact-v1](https://arxiv.org/html/2604.08118v1) §3.1–3.4/§4–6，固定码本 beam assignment 与 Hessian-weighted sequential E/M centroids 更新是不同自由度；OA-EM 仍顺序拟合 residual。采用校准目标/初始化分支，不采 basin 不跨越定理、ρ 充分条件或未测 LUT 速度。三模型、单 seed、128 条 C4/4096 校准、WikiText 选 checkpoint 与下游反向均保留；6 分知识缺口深入；root 必要原文/实际正文及相邻衔接复核通过。

- `SF-2026-ARXIV-2604-07955`：[ResComp exact-v1](https://arxiv.org/html/2604.07955v1)，已读 §3–4 原始/补偿权重的目标差异、Eq10–14/Algorithm 1 与 §5 Tables 3–6 的消融、旋转退化、校准内存和时间。仅采用离线校准目标与残差分解；不采普遍质量或推理加速保证。V2 2+2+2=6，长期知识缺口深入；root 已独立核必要原文、实际正文及相邻交接，通过，未复现实验。

- `SF-2026-ARXIV-2604-09073`，Experimental：[exact-v1](https://arxiv.org/html/2604.09073v1) §3–5/§6.1–6.6。INT8输入/权重、INT32输出bit-flip且memory读取无错，ABFT mask→earlier activation覆盖是近似恢复。14nm PDK/synthesis、64 systolic arrays/HBM2、SCALE-Sim及DiT/PixArt/SD1.5，非实机GPU；energy与latency来自不同DVFS点，paired-error cancellation仍可能漏检，质量指标平均接近不等逐图正确。未采用36%/1.7×为production保证。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- `SF-2026-ARXIV-2604-09083`，Experimental：[exact-v1](https://arxiv.org/html/2604.09083v1) §4.1–4.3、§5.1–5.5 支持 storage precision → SIMD unpack → CPU/NPU schedule 协同。全部设备实验为 Xiaomi 15 Pro/Snapdragon 8 Elite/16GB RAM/512GB flash；Llama 3-8B/Mistral 7B/Phi 3-3.8B/Qwen 1.5-1.8B，平均 4–7 bit、基线 INT8、五任务输入 59–1086 token，并非同精度 GPU 对照。默认 5 bit 仍有质量代价；decode 512/512 在 CPU 上比较，不能据 TTFT 写通用 decode 加速或 tail-SLO。未采用摘要 4.07× 生产承诺。root 已完成必要原文与实际正文/相邻链路的写后独立复核，通过，本地实验未复现。

- `SF-2026-ARXIV-2604-07523`：[FILCO exact-v1](https://arxiv.org/pdf/2604.07523v1)，实际核 §2.1–2.5、§3 与 §4.1–4.4：动态 loop bounds、1-D FMU view/role、CU block vs FMU cyclic partition 与 pre-routed stream；VCK190 PL150MHz/AIE1GHz、Vitis2023.1、FP32与BERT32–512。RSN为作者自建解析模型、单AIE用SystemC；不把kernel周期或模型吞吐推广为LLM服务。MILP Eq2的结束时刻表达未显式加起点，故不采用无条件global optimal保证；只采用硬件配置分支。作者审阅/实际正文已落实，待非作者写后复核，未运行实现。

- `SF-2026-ARXIV-2604-08720`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.08720v1) §3、§4.5、§5–6。116人工筛选correctness bugs、77可回放、五fuzzers合计26检出与15graph全漏不代表生产failure prevalence；跨调用distinct input/context oracle、alias/view/in-place/layout与参数边界不是operator count替代。AlignGuard以条件→mutation生成四组件测试，341有效seed来自PyTorch2.8.0的475项，gpt-4o/mini温度0.2，32CPU/500GB；23新bug开发者确认与10修复为作者当时状态，当前版本行为需另核。人工分类、样本选择和历史测试族限制保留；未复现实验，本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-06664`，Status: Experimental：[exact-v1](https://arxiv.org/html/2604.06664v1) §2.3/§3–5 是拓扑之外的跨进程 execution-context 恢复、deterministic allocation/capture-buffer replay、binary hash/function name、模板和 rank stub；§4.2.2 明确不含 PP，§5.4 需固定 KV pool。§6 限上述 DGX/版本/模型与 DP/EP、PD decode-only、随机 prompts 生成128 token的10次 TPOT/输出对照，不采用99%启动改善为通用冷启动收益。正文将兼容失败回退与 archive 身份作为工程推论而非作者已验防御；root 已实际核必要原文、正文和邻接，写后独立通过。

- `SF-2026-ARXIV-2604-03425`（Experimental）：[exact-v1](https://arxiv.org/pdf/2604.03425v1) §4–5支持token/modulus-coherent ciphertext layout、RNS reduction与混合并行通信计划；BERT-Base/SST-2、128-bit CKKS、N=2^16、Q35/P4/boot14，4×A100-40GB的2048输入约5036s。移植Cinnamon/Hydra不包含原ASIC整体优势，不外推LLM decode/SLO或改变威胁模型。未复现实验；本次写后独立复核通过（root）。

- `SF-2026-ARXIV-2604-03258`（SoLA；Experimental）：[exact-v1](https://arxiv.org/html/2604.03258v1) Method、Table4、Prime Neurons 消融及效率实验支持保留高贡献原通道与其余 whitening/SVD、同预算 rank 分配；贪心次优且 Llama2-13B/20% 自适应 PPL 6.52 弱于均匀 6.18。RTX4090 的序列2048矩阵微基准不证明完整 Serving、并发或 SLO；未复现实验。
- `SF-2026-ARXIV-2604-03420`（Experimental）：[exact-v1](https://arxiv.org/html/2604.03420v1) §4–7 支持同初始化 ViT donor 的 QAT 差分迁移及 lambda 负迁移；receiver test-set 幅度扫描是 oracle 上界，3-bit weight-only 模拟不证明 LLM 或真实 kernel 性能，未复现实验。
- `SF-2026-ARXIV-2604-03950`（DMA；Experimental）：[exact-v1](https://arxiv.org/html/2604.03950v1) §4–6、Algorithm1/Table3/tile 消融支持近 MXFP8/远 MXFP4 QK、FP16 V 与双格式融合；B200、Llama3.1-8B/3.2-3B、LongBench2.5K～30K 条件中 passage_retrieval_en/3B 为80→37，不称无损或通用 Serving/SLO 改善。
- `SF-2026-ARXIV-2604-04013`（RUQuant；Experimental）：[exact-v1](https://arxiv.org/html/2604.04013v1) §3–5/Eq13/Tables4–6 支持 uniform centroid 假设、block rotation 与可选 output-loss reflection；无需优化版本和 fine-tune 版本准备成本分开，RTX3090 layer-wise prefill2048/batch1/4/16 不等于端到端服务，未复现实验。
- `SF-2026-ARXIV-2604-03446`（MMEE；Experimental）：[exact-v1](https://arxiv.org/html/2604.03446v1) III–VI/VII-A–E 支持 tiling/order/buffer/recompute 共同表示及声明空间搜索；1410 Timeloop 对照为 intra-operator model 验证，NVDLA/TPU-like 模拟、BERT/GPT/PaLM training/prefill 未证明真实 fusion 硬件或 production decode/SLO。
- `SF-2026-ARXIV-2604-03674`（DiffSparse；Experimental）：[exact-v1](https://arxiv.org/html/2604.03674v1) §3.2/4.1–4.3/A.4–A.6 支持 learned layer×step×rate cost 与离线 DP 静态 schedule；训练4～10小时和约30秒 DP 不算在线延迟，DiT FID2.26→2.81 及 Wan25/20step 口径差异保留，不外推通用 quality/SLO，未复现实验。

- [2604.02344v1](https://arxiv.org/html/2604.02344v1)，Experimental；§3.3–3.6、§4.3–4.4、§5.1、§7。采用直接 dispatch 与 framework/per-operation 推导量分账、异步提交不可简单相加的测量边界；不采用跨精度 CUDA 差距的唯一因果解释。约30%误差的分解和 CPU/GPU overlap 残差不是精确可加账目，未建立生产并发/SLO 保证。

- `SF-2026-ARXIV-2604-02110`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2604.02110v1) §III–V 支持 tile-group attention dataflow、NoC multicast/reduction、过度分组的矩阵利用率反转与受限模拟对照；GVSoC/RTL 校准不等于真实 wafer-scale 芯片量测，GH200 对照也跨硬件。仅吸收 IO/片上通信/occupancy 的条件设计原则，不移植作者 headline 到一般 GPU Serving。

- `SF-2026-ARXIV-2605-07881`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.07881v1) 支持参数化并发语言、barrier-sufficiency 检查与受限 CANN/generated-kernel mutation 结果；sound/complete 只相对其硬件模型，不覆盖所有驱动、指令或真实 pipeline。

- `SF-2026-ARXIV-2605-04569`（Status: Experimental）：[exact-v1](https://arxiv.org/html/2605.04569v1) 支持 K/V saliency 预选、query-risk proxy 与 full/Taylor sparse attention 的动态分支；作者约 60% attention-module latency 与约 1.47× end-to-end 结果绑定 LIVEditor-14B、披露视频编辑 benchmark、硬件和阈值，不证明跨模型质量或生产 SLO。

- [Quantizing With Randomized Hadamard Transforms](https://arxiv.org/html/2605.06014v1)（Theoretical Evidence）：支持 scalar 与 fixed-block vector quantizer 的不同变换次数及 moment-based gate；没有 runtime artifact 或实际加速证据。

- `SF-2026-ARXIV-2609-01730`（HEAT；Status: Experimental）：[exact-v1](https://arxiv.org/html/2609.01730v1) §3–5、Appendix A–F 支持离线 site-wise 迭代预算、固定 mode 与 weight consolidation；训练松弛、range guard 和实际部署电路不是同一对象。作者使用 GPT-2 124M、OpenWebText 与 128 条各 128 token 的 teacher-forced 加密链；正文不采用速度数字，不外推生产 concurrency、SLO、自由生成质量或正式密码安全。精确缓存及作者/独立审阅保存在 Sep03 的 `_sources`；本轮未复跑 artifact。

- `SF-2026-ARXIV-2609-01864`（CREDIT；Status: Experimental）：[exact-v1](https://arxiv.org/html/2609.01864v1) §II–IV 支持 owner-local bulk、compact partial replication 与 shape/device-conditioned profitability。作者实验为 H100 SXM / RTX 5090、CUDA 13、PyTorch 2.11、Triton 3.6、六类 reduction-reuse 算子；FP32 input，row quantization 输出 int8，N=4K…64K，M=2048 或 4096，P∈{2,4,8} 实测选优。小形状存在负收益，不含完整模型、在线 concurrency 或 SLO 验证。代码对读固定在 [9169b43](https://github.com/zhengxiongli08/CREDIT/tree/9169b43b8538611c16e06ff6c9f074dcefc1fb30)，核对代表性 LayerNorm backward、cost model、control 和结果汇总；未复跑 GPU，commit 时间不证明首次公开时间。正文不引用 headline speedup，不宣称成本模型免除了 tuning。

- `SF-2026-ARXIV-2602-06072`（Status: Experimental）：exact-v1 §3 支持 heterogeneous request packing、lossless attention 与 I/O-local execution，§4.3 提供作者 ablation，Appendix C 记录 solver overhead；不证明所有模型、序列分布、KV layout、hardware 或 production SLO 上的通用收益。https://arxiv.org/html/2602.06072v1

- `SF-2026-ARXIV-2604-22312`（Status: Experimental）：exact-v1 支持以 previous-step Top-K、预索引统计、threshold counting 与最终验证组成 Blackwell sparse-decode 的 exact selection 分支；不支持跨硬件或低时间相关 workload 的普遍加速结论。https://arxiv.org/abs/2604.22312v1

- **MF-QAT（arXiv:2604.00529v1；Status: Experimental）**：exact-v1 支持 multi-format QAT、anchor checkpoint 与 Slice-and-Scale 派生路径，以及作者公开模型/格式中的质量结果；不证明未测硬件、kernel、模型或生产 workload 可共享同一 acceptance 结论。https://arxiv.org/abs/2604.00529v1

- **GPUOS（arXiv:2604.17861v1；Status: Experimental）**：支持 host-managed ring buffer、persistent kernel executor 与 runtime operator injection 的机制分支，并对比 CUDA Graph 的规则 workload 边界。作者实验不证明任意 operator、GPU、并发或生产 tail-SLO 均能受益。https://arxiv.org/abs/2604.17861v1

- MoEQuant（activated-expert-aware calibration；Status: Experimental）：https://arxiv.org/html/2505.03804v1
  - 证据边界：结论绑定作者模型族、数据集、bit-width 与硬件；不证明所有 expert 应使用同一精度或校准策略，也不证明端到端 serving 加速。

- `SF-2026-ARXIV-2606-23743` — primary `arXiv:2606.23743v1`；Method=`arXiv:2606.23743v1 §3 Sol Architecture; §4 Agent-Native Optimization`；Evaluation=`arXiv:2606.23743v1 §5 Experiments`；Non-proof=`arXiv:2606.23743v1 §6 Limitations and Future Work`；Artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

- Launch-Bound and Substitutable（MoE local optimization 与 end-to-end ceiling；Status: Experimental）：
  https://arxiv.org/abs/2608.26612v1
  - 证据边界：作者只在 OLMoE-1B-7B、DeepSeek-V2-Lite、Qwen3-30B-A3B 与 A100 80GB serverless
    合同中验证 kernel/quantization/compile intervention；不支持把 headline speedup、route drift 或 ceiling 外推到其他
    topology、batch、precision 与 production SLO。

- GyRot（arXiv:2607.27694v1；Status: Experimental）：https://arxiv.org/html/2607.27694v1
  - 证据边界：exact-v1 支持作者配置中 rotation/group 解耦、outlier alignment 与 integer metadata/datapath co-design；实验包含模型精度和 28nm RTL/model evaluation，不证明 GPU kernel、silicon、在线并发或生产 tail-SLO 收益。
- WIDE（arXiv:2607.28418v1；Status: Experimental）：https://arxiv.org/html/2607.28418v1
  - 证据边界：exact-v1 支持 token-level width routing、mask reordering 与 intra-kernel skipping 在作者 CUDA/模型合同中的实现；不证明 unsupported shape、其他 GPU、量化组合或生产 tail-SLO 下仍优于 dense fallback。

- Action-conditioned VLA quantization（阶段条件 codebook 与 centroid-reuse execution co-design；Status: Experimental）：https://arxiv.org/html/2607.24148v1

- Unified Static-Dynamic Pruning（arXiv:2607.21985v1；Status: Experimental）：https://arxiv.org/html/2607.21985v1
  - 证据边界：支持 paper-defined small-batch Decode/Prefill 中的 shared sparse representation 与 phase-specific kernels；不证明高 batch、量化组合、现代 GPU 或生产 tail-SLO 下普遍优于 dense/structured paths。

- Heterogeneous dependency-preserving microbatch placement（Status: Experimental）:
  https://arxiv.org/abs/2607.12839v1

- Voltron（runtime-revisable phase/device execution plan；Status: Experimental）:
  https://arxiv.org/abs/2607.07046v1
- KronQ（Kronecker-factorized curvature quantization；Status: Experimental）:
  https://arxiv.org/abs/2607.07964v1
- SiFAR（low-batch speculate/verify All-Reduce；Status: Experimental；单节点 H200/NVSwitch 证据）:
  https://arxiv.org/abs/2607.08973v1
- The Illusion of Equivalency（quantization per-example agreement 与 distribution drift；Status: Experimental）:
  https://arxiv.org/abs/2607.08734v1

- Meganeura（Vulkan/Metal typed-graph portable runtime；Status: Experimental）: https://arxiv.org/abs/2608.01563
- TileMix（tile-centric mixed-precision attention；Status: Experimental）: https://arxiv.org/abs/2608.17336
- LLM4LLM（kernel benchmark 到 in-model closed-loop validation；Status: Experimental）: https://arxiv.org/abs/2608.21836

- Kernel-Smith（population/archive kernel search；Status: Experimental）: https://arxiv.org/abs/2603.28342
- HIERA（workload-aware implementation-space planning；Status: Experimental）:
  https://arxiv.org/abs/2608.21157

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
- SGLang v0.5.18（startup overlap release boundary）:
  https://github.com/sgl-project/sglang/releases/tag/v0.5.18
- SGLang PR #32017（capture-safe checkpoint staging and in-place commit contract）:
  https://github.com/sgl-project/sglang/pull/32017

- Evidence boundary：当前官方入口只支持版本化的 runtime、batching、paged KV、quantization 与 hardware
  feature availability；SVDQuant/Nunchaku 和 MASQuant 仅作为跨 runtime 的受限机制证据。具体支持矩阵与性能
  结论必须重新绑定版本、模型、精度、硬件与 workload，不能由通用 execution 原理推出。

- ATSInfer（tensor-granularity placement 与 load-aware plan transition；Status: Experimental；batch=1 consumer-device evidence）：
  https://arxiv.org/abs/2607.10183v1

- Evidence boundary：DeepGEMM 的功能范围、SM90/SM100 支持和 FFMA scheduling history 均为版本化事实；
  复用、异步 pipeline 与专用化 trade-off 的稳定机制已在正文拥有唯一 owner。

- PolyQ（fractional per-channel precision → compiler-regularized CPU layout；Status: Experimental）:
  https://arxiv.org/abs/2607.14618
- eNPU（component-level DVFS、compiler schedule 与 SLO slack；Status: Experimental）:
  https://arxiv.org/abs/2607.16473v1
- Transition-Aware Backend Dispatch（previous-backend state 与切换成本；Status: Experimental；Jetson FP32 batch-1 trace replay，无 integrated mixed-backend runtime）:
  https://arxiv.org/abs/2607.17415v1
- CONQuER（compiler-integrated mixed-precision search 与 selective hardware calibration；Status: Experimental）:
  https://arxiv.org/abs/2607.25884v1

### Daily integration evidence trace

- `2026-05-02 / SF-PERSEUS-MEGAKERNEL-SIGNAL-ORDERING` — exact-v1 `arXiv:2605.00686v1`；正文吸收 transfer signal、NIC ordering 与 group fallback 的 ownership 边界，未保留未绑定 workload 的性能 headline。
- `2026-05-05 / SF-LEAP-EARLY-EXIT-PRETRAINING-CONTRACT` — exact-v1 `arXiv:2605.01058v1`；正文吸收 objective/exit-sensor 对齐与 full-depth fallback，不把 early-exit 近似写成完整深度等价。

#### 2026-06-25 source-specific Review notes

- **SF-2026-ARXIV-2606-26344**：Primary `arXiv:2606.26344v1`；Method `https://arxiv.org/html/2606.26344v1 — §Axon synthesizing superoptimizer; tensor-program search and verification`；Evaluation `https://arxiv.org/html/2606.26344v1 — §Kernel synthesis evaluation and generated-program performance`；未证明边界 `https://arxiv.org/html/2606.26344v1 — §Covered tensor operators/hardware only; verifier does not prove arbitrary numerical equivalence`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。
- **SF-2026-ARXIV-2606-26453**：Primary `arXiv:2606.26453v1`；Method `https://arxiv.org/html/2606.26453v1 — §Micro-profiling tools as expert surrogates for LLM CUDA optimization`；Evaluation `https://arxiv.org/html/2606.26453v1 — §Generated-kernel correctness, profiling and speed evaluation`；未证明边界 `https://arxiv.org/html/2606.26453v1 — §Evaluated CUDA tasks and toolchain only; profile-guided generation needs deterministic correctness fallback`；Artifact `Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review`。

### Daily Books delta trace（2026-06—08）

<!-- daily-books-trace:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:start -->
- `SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING` — Daily `2026-05-06`；primary `arXiv:2605.03190v1`；Books review `books-review:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING`。

  **已吸收的语义增量：** asynchronous work 可先拥有 virtual execution-resource identity，再由 runtime 按 readiness 绑定 physical cores；completion、memory visibility 与 output commit 仍属于 execution-plan contract。
<!-- daily-books-trace:SF-VDCORES-ASYNC-GPU-RESOURCE-DECOUPLING:end -->

<!-- daily-books-trace:SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED:start -->
- `SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED` — Daily `2026-06-08`；primary `arXiv:2606.06521v1`；Books review `books-review:SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED`。

  **已吸收的语义增量：** We consider a single attention head with query length q q , KV length N N , and head dimension d d . KV blocks have size B B (typically 64 or 128). The first k sink k_{\text{sink}} positions are sink tokens with logit scores Δ \Delta above the mean. Boundary: Both optimizations address the identical failure mode: P values falling below E4M3’s representable range. Once either fix is applied, P-collapse is eliminated and the residual MSE is set by the inherent E4M3 quantization noise on representable values. Paired t t -tests over 100 instances confirm that Forward+S=256 and Reverse+S=256 are statistically indistinguishable wherever P-collapse is active ( Δ ≤ 9 \Delta\leq 9 ); for Δ ≥ 10 \Delta\geq 10 the residuals diverge with reverse marginally better, but the absolute gap is ∼ 10 − 8 \sim 10^{-8} , three orders of magnitude below the MSE itself, so the practical conclusion is unchanged (Appendix B ).
<!-- daily-books-trace:SF-P-CAST-PRECISION-FP8-ATTENTION-SINK-INDUCED:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09682:start -->
- `SF-2026-ARXIV-2606-09682` — Daily `2026-06-09`；primary `arXiv:2606.09682v1`；Books review `books-review:SF-2026-ARXIV-2606-09682`。

  **已吸收的语义增量：** agent 生成 megakernel 必须经过 typed IR、静态 shape/layout/resource checks、编译与数值验证门，失败后才允许 self-retarget；自然语言计划不直接获得 kernel authority。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09682:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-09686:start -->
- `SF-2026-ARXIV-2606-09686` — Daily `2026-06-09`；primary `arXiv:2606.09686v1`；Books review `books-review:SF-2026-ARXIV-2606-09686`。

  **已吸收的语义增量：** 低精度 format contract 需要 vendor-neutral、bit-exact 的 encode/decode、rounding、overflow、NaN/Inf/subnormal 与 microscaling conformance vectors；格式名相同不代表语义相同。
<!-- daily-books-trace:SF-2026-ARXIV-2606-09686:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-13740:start -->
- `SF-2026-ARXIV-2606-13740` — Daily `2026-06-12`；primary `arXiv:2606.13740v1`；Books review `books-review:SF-2026-ARXIV-2606-13740`。

  **已吸收的语义增量：** 移动 NPU 上的 dLLM runtime 必须联合处理 shrinking block workload、可修订token、NPU可见地址映射与CPU/NPU data path
<!-- daily-books-trace:SF-2026-ARXIV-2606-13740:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15652:start -->
- `SF-2026-ARXIV-2606-15652` — Daily `2026-06-15`；primary `arXiv:2606.15652v1`；Books review `books-review:SF-2026-ARXIV-2606-15652`。

  **已吸收的语义增量：** 4-bit runtime可把dense base与sparse 4-bit residual同时压进single fused GEMM pipeline，避免mixed-precision conversion破坏实际speedup
<!-- daily-books-trace:SF-2026-ARXIV-2606-15652:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15682:start -->
- `SF-2026-ARXIV-2606-15682` — Daily `2026-06-15`；primary `arXiv:2606.15682v1`；Books review `books-review:SF-2026-ARXIV-2606-15682`。

  **已吸收的语义增量：** W4A4KV4 reasoning质量gate应聚焦low-entropy symbolic commitments，并联合trace-aligned QAT、selective entropy loss与RoPE-consistent KV calibration
<!-- daily-books-trace:SF-2026-ARXIV-2606-15682:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15859:start -->
- `SF-2026-ARXIV-2606-15859` — Daily `2026-06-15`；primary `arXiv:2606.15859v1`；Books review `books-review:SF-2026-ARXIV-2606-15859`。

  **已吸收的语义增量：** embodied AR glasses runtime要联合egocentric workload phase、sensor/compute pipeline、latency/energy budget与offload/edge placement，而非只比较model accuracy
<!-- daily-books-trace:SF-2026-ARXIV-2606-15859:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-15991:start -->
- `SF-2026-ARXIV-2606-15991` — Daily `2026-06-15`；primary `arXiv:2606.15991v1`；Books review `books-review:SF-2026-ARXIV-2606-15991`。

  **已吸收的语义增量：** GPU kernel authoring可把tile-levelownership、host launch lifetime、async pipeline与CUDA graph replay纳入Rust type boundary，并保留显式unsafe escape
<!-- daily-books-trace:SF-2026-ARXIV-2606-15991:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-16332:start -->
- `SF-2026-ARXIV-2606-16332` — Daily `2026-06-16`；primary `arXiv:2606.16332v1`；Books review `books-review:SF-2026-ARXIV-2606-16332`。

  **已吸收的语义增量：** CPU matrix extension 不是全算子默认后端；runtime 应按 operator shape 在 CPU/SME/cooperative path 间选择并保留 packed-layout state
<!-- daily-books-trace:SF-2026-ARXIV-2606-16332:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17518:start -->
- `SF-2026-ARXIV-2606-17518` — Daily `2026-06-17`；primary `arXiv:2606.17518v1`；Books review `books-review:SF-2026-ARXIV-2606-17518`。

  **已吸收的语义增量：** Agentic kernel search 可在主 reasoning 继续时 speculative 生成候选，并行执行 validation/profile；控制面还必须协调 GPU pool、候选 lineage 与远端 KV/temporary state。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17518:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-17566:start -->
- `SF-2026-ARXIV-2606-17566` — Daily `2026-06-17`；primary `arXiv:2606.17566v1`；Books review `books-review:SF-2026-ARXIV-2606-17566`。

  **已吸收的语义增量：** 分布式 DiT compiler planner 需先在 pre-compilation IR 高召回剪枝，再用 compiled HLO 与物理互连拓扑排序 sharding/placement；logical mesh 不是最终性能身份。
<!-- daily-books-trace:SF-2026-ARXIV-2606-17566:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2606-18421:start -->
- `SF-2026-ARXIV-2606-18421` — Daily `2026-06-17`；primary `arXiv:2606.18421v1`；Books review `books-review:SF-2026-ARXIV-2606-18421`。

  **已吸收的语义增量：** DL compiler release testing 应抽取跨 model semantics、IR pass 与 hardware feasibility 的 full-stack constraints，并把 assertion pattern作为 behavior-equivalence oracle。
<!-- daily-books-trace:SF-2026-ARXIV-2606-18421:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-04302:start -->
- `SF-2026-ARXIV-2607-04302` — Daily `2026-07-07`；primary `arXiv:2607.04302v1`；Books review `books-review:SF-2026-ARXIV-2607-04302`。

  **已吸收的语义增量：** 新增证据边界：Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L441`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-04302:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-05475:start -->
- `SF-2026-ARXIV-2607-05475` — Daily `2026-07-08`；primary `arXiv:2607.05475v1`；Books review `books-review:SF-2026-ARXIV-2607-05475`。

  **已吸收的语义增量：** 新增证据边界：Mobile backend choice is phase dependent: prefill exposes large compute-dense shapes that can fit NPU strengths, while single-token decode exposes small dynamic kernels and memory traffic that can favor CPU. Framework offload coverage, graph/static-shape constraints, quantization support, tensor-layout conversion, host polling, sleep latency, DVFS and affinity determine whether nominal NPU capability becomes end-to-end efficiency. The framework owns operator partition/offload and layout conversions; backend runtimes own executable graph/quantization constraints; host CPU owns polling, wake/sleep and thread scheduling; request phase and KV state determine current shape. A backend switch is therefore a state-transfer/control decision, not a free dispatch choice. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L109`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-05475:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07046:start -->
- `SF-2026-ARXIV-2607-07046` — Daily `2026-07-09`；primary `arXiv:2607.07046v1`；Books review `books-review:SF-2026-ARXIV-2607-07046`。

  **已吸收的语义增量：** 新增证据边界：Voltron first builds distinct per-layer execution plans for prefill and decode, choosing model/tensor parallel placement and precision according to layer/task sensitivity. At runtime it observes memory, KV growth and wireless conditions, then revises device participation, precision and pruning at token boundaries while preloading the next plan to hide reconfiguration. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L41`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07046:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-07964:start -->
- `SF-2026-ARXIV-2607-07964` — Daily `2026-07-10`；primary `arXiv:2607.07964v1`；Books review `books-review:SF-2026-ARXIV-2607-07964`。

  **已吸收的语义增量：** 新增证据边界：KronQ approximates second-order weight sensitivity as output-gradient covariance Kronecker activation covariance, then uses two-sided incoherence transforms and Hessian-trace sensitivity for mixed-bit allocation. After preprocessing, the output-gradient factor cancels from the column update algebra, but it still influences the transformed representation and layer sensitivity decision. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L475`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-07964:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08734:start -->
- `SF-2026-ARXIV-2607-08734` — Daily `2026-07-10`；primary `arXiv:2607.08734v1`；Books review `books-review:SF-2026-ARXIV-2607-08734`。

  **已吸收的语义增量：** 新增证据边界：Evaluate quantization as a possible behavioral transformation, not only a storage reduction: compare internal distribution shift and per-example correctness agreement alongside aggregate perplexity/accuracy. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L425`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08734:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-08973:start -->
- `SF-2026-ARXIV-2607-08973` — Daily `2026-07-13`；primary `arXiv:2607.08973v1`；Books review `books-review:SF-2026-ARXIV-2607-08973`。

  **已吸收的语义增量：** 新增证据边界：For small-payload low-batch TP decode, remove the bottom barrier with dual buffers, reduce transfer with switch-assisted redundant pull, and replace the top readiness barrier with speculative fetch plus a reduced validation flag; retry on mis-speculation before committing the collective result. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L370`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-08973:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-10183:start -->
- `SF-2026-ARXIV-2607-10183` — Daily `2026-07-12`；primary `arXiv:2607.10183v1`；Books review `books-review:SF-2026-ARXIV-2607-10183`。

  **已吸收的语义增量：** 新增证据边界：Profile per-tensor CPU/GPU execution and transfer costs, solve a memory-constrained static placement using measured performance density, keep nonresident tensors in pinned host memory, overlap Copy-Engine and SM-driven Zero-Copy transfers with computation, then observe realized transfer/compute time and re-run dynamic placement only after deviation and rate-limit thresholds are crossed. Prefill and decode retain distinct plans because their compute/memory balance differs. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L60`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-10183:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-12839:start -->
- `SF-2026-ARXIV-2607-12839` — Daily `2026-07-15`；primary `arXiv:2607.12839v1`；Books review `books-review:SF-2026-ARXIV-2607-12839`。

  **已吸收的语义增量：** 新增证据边界：A heterogeneous roofline predicts opportunity; dependency-preserving microbatches expose overlap; trace-guided latency shaping jointly tunes assignment and schedule, with NPU-aware queues and custom GPU kernels. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-12839:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-14618:start -->
- `SF-2026-ARXIV-2607-14618` — Daily `2026-07-17`；primary `arXiv:2607.14618v1`；Books review `books-review:SF-2026-ARXIV-2607-14618`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: uniform integer quantization -> fractional per-channel precision compiled into regular ISA quanta 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-14618:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-16473:start -->
- `SF-2026-ARXIV-2607-16473` — Daily `2026-07-18`；primary `arXiv:2607.16473v1`；Books review `books-review:SF-2026-ARXIV-2607-16473`。

  **已吸收的语义增量：** 新增证据边界：DVFS can move from chip-wide frequency to component-level control when tensor operators stress different NPU units. The compiler must co-schedule instructions and voltage/frequency domains under request slack; otherwise synchronization and transition cost erase the energy benefit. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-16473:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-17415:start -->
- `SF-2026-ARXIV-2607-17415` — Daily `2026-07-20`；primary `arXiv:2607.17415v1`；Books review `books-review:SF-2026-ARXIV-2607-17415`。

  **已吸收的语义增量：** 新增证据边界：static/operator-local backend -> previous-backend transition-aware plan 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-17415:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-21985:start -->
- `SF-2026-ARXIV-2607-21985` — Daily `2026-07-27`；primary `arXiv:2607.21985v1`；Books review `books-review:SF-2026-ARXIV-2607-21985`。

  **已吸收的语义增量：** 新增证据边界：Static weight sparsity and input-dependent activation sparsity become composable through a shared column-addressable representation with phase-specific decode and prefill kernels. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L172`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-21985:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-24148:start -->
- `SF-2026-ARXIV-2607-24148` — Daily `2026-07-28`；primary `arXiv:2607.24148v1`；Books review `books-review:SF-2026-ARXIV-2607-24148`。

  **已吸收的语义增量：** 新增证据边界：Layering / Dependency: fixed precision -> offline dual codebooks -> action-derived runtime phase signal -> codebook-index execution and centroid reuse on a matching accelerator. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L549`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-24148:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607.25884:start -->
- `SF-2026-ARXIV-2607.25884` — Daily `2026-07-29`；primary `arXiv:2607.25884v1`；Books review `books-review:SF-2026-ARXIV-2607.25884`。

  **已吸收的语义增量：** 新增证据边界：Direct Evolution: framework-side bit assignment -> compiler-visible quantization IR -> surrogate-prescreened search -> selective hardware calibration. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607.25884:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-27694:start -->
- `SF-2026-ARXIV-2607-27694` — Daily `2026-07-31`；primary `arXiv:2607.27694v1`；Books review `books-review:SF-2026-ARXIV-2607-27694`。

  **已吸收的语义增量：** 新增证据边界：CoRFiG decouples rotation R from group G; HAP aligns outliers; asymmetric scale/zero-point become INT8. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-27694:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2607-28418:start -->
- `SF-2026-ARXIV-2607-28418` — Daily `2026-07-31`；primary `arXiv:2607.28418v1`；Books review `books-review:SF-2026-ARXIV-2607-28418`。

  **已吸收的语义增量：** 新增证据边界：Routers select head/channel groups; columns sort masks/indices; fused CuTe kernels skip blocks/loads/MMA and scatter epilogue; separate phase kernels and dense fallback. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。
<!-- daily-books-trace:SF-2026-ARXIV-2607-28418:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-01563:start -->
- `SF-2026-ARXIV-2608-01563` — Daily `2026-08-03`；primary `arXiv:2608.01563v1`；Books review `books-review:SF-2026-ARXIV-2608-01563`。

  **已吸收的语义增量：** Meganeura 以 typed graph、自动微分、图重写、kernel 选择和静态内存规划组成可移植 GPU 栈，并通过 Vulkan/Metal 跨设备执行。其五类 workload 与 synthetic input 说明设计可行，但覆盖范围和第三方 kernel 生态仍不能与成熟 CUDA 栈等同。
<!-- daily-books-trace:SF-2026-ARXIV-2608-01563:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-17336:start -->
- `SF-2026-ARXIV-2608-17336` — Daily `2026-08-19`；primary `arXiv:2608.17336v1`；Books review `books-review:SF-2026-ARXIV-2608-17336`。

  **已吸收的语义增量：** TileMix 以 tile group 为精度分配单位，使 attention 量化同时考虑局部敏感性和 kernel 执行。LongEval/LV-Eval 与 Llama/Qwen/Vicuna 支持作者范围内的质量—性能比较；校准迁移、极长 Context 和不同硬件 kernel 仍未闭合。
<!-- daily-books-trace:SF-2026-ARXIV-2608-17336:end -->

<!-- daily-books-trace:SF-2026-ARXIV-2608-21836:start -->
- `SF-2026-ARXIV-2608-21836` — Daily `2026-08-25`；primary `arXiv:2608.21836v1`；Books review `books-review:SF-2026-ARXIV-2608-21836`。

  **已吸收的语义增量：** LLM4LLM 从目标推理脚本提取 phase-aware kernel task，由 episodic agent 搜索 patch，再以集成后的 in-model validation 决定接受，而不是只信 standalone KernelBench。十个 workload、A100/H100 结果支持其 benchmark-to-deployment gap；未披露的并发、模型更新和长期维护成本限制外推。
<!-- daily-books-trace:SF-2026-ARXIV-2608-21836:end -->

<!-- daily-books-trace:SF-2026-MOE-INFERENCE-OPT-LIMITS:start -->
- `SF-2026-MOE-INFERENCE-OPT-LIMITS` — Daily `2026-08-28`；primary `arXiv:2608.26612v1`；Books review `books-review:SF-2026-MOE-INFERENCE-OPT-LIMITS`。

  **已吸收的语义增量：** 补足 route、launch、memory、communication 同时决定端到端收益的上限，并保留模型、拓扑与 workload 边界。
<!-- daily-books-trace:SF-2026-MOE-INFERENCE-OPT-LIMITS:end -->

- `SF-2026-ARXIV-2609-00049`，REAL-Q（Status: Experimental）：[exact-v1 §4–7](https://arxiv.org/html/2609.00049v1)。采用冻结二阶近似与当前 residual 梯度补偿的区分；W4A16、Llama3.1/Qwen3、WikiText2校准，KL/PPL与下游任务分报。SGD分析不构成Adam保证，离线成本不等于serving收益。
- `SF-2026-ARXIV-2609-00066`，OCGQuant（Status: Experimental）：[exact-v1 §3–5](https://arxiv.org/html/2609.00066v1)。采用共享scale的collateral error、配对permutation、weight重建与融合执行链；原生NVFP4 group16、单RTX5090，其他group的pseudo-quantization不证明相同硬件收益，RMS与activation优先顺序仍有局限。

<!-- daily-books-trace:SF-2026-ARXIV-2607-25651:start -->
- `SF-2026-ARXIV-2607-25651` — Daily `2026-07-29`；primary `arXiv:2607.25651v1`；正文锚点“Compiler Frontend 是独立的语义故障层”。
  证据限 TorchDynamo 的 123 个历史 bug、七类 root cause 与作者生成的新 tests；不保证 taxonomy 覆盖未知类别，LLM 也不是 correctness oracle。
<!-- daily-books-trace:SF-2026-ARXIV-2607-25651:end -->

- `SF-2026-FLASHINFER-AUTOTUNER-V2`：官方 [Autotuner v2 §1–3、§5](https://flashinfer.ai/2026/09/22/autotuner-v2.html) 与 [v0.7.0 release](https://github.com/flashinfer-ai/flashinfer/releases/tag/v0.7.0)，精确发布 commit `4d75a33f19aaf48b44d5b1c5dbca33bc1eca5c58`。正文只采用测量策略身份、可选 runner validation、原子发布及 rank convergence 的边界；后者依赖同构参与者、共享存储与框架 barrier，不是全局最优或任意故障恢复保证。未复现实验，不采用宣传倍数；默认兼容策略不等于所有调用都启用新策略。

- `SF-2026-ARXIV-2603-04359`：[CAT exact-v1](https://arxiv.org/html/2603.04359v1) §2–4、§6–7；采用 negligible-clipping uniform-integer 近似下 concentration/alignment 分账及 block 近似成本，不复制公式显示中的易混记号，不采用端到端加速保证。Daily 2026-03-06，实际写后非作者 root 复核通过；未复现实验。

- `SF-2026-ARXIV-2512-24124` — Daily `2026-01-02`；[OptRot exact-v1](https://arxiv.org/html/2512.24124v1) §3.1–3.2、§4.1–4.2、§5.1–5.2/Tables2–4。8分深入只采用权重第四次矩旋转代理、data-free步骤权限及W4A8/W4A4/RTN反例；constrained-LDL/stochastic/clamping条件的界不授ordinary LDL或整网质量保证。不写未核附件细节数、不采Serving倍率，硬件与端到端延迟未披露，未复现；root必要原源与owner写前核通过，root实际正文/前后邻接及末注写后非作者复核通过。

- `SF-2026-ARXIV-2602-03537`：[MatGPTQ exact-v1](https://arxiv.org/html/2602.03537v1) §3–6/C，采用单整数 parent 的多目标 PTQ 投影和等权跨 bit 残差传播，区别于独立高位量化后直接截断。目标集合、未优化位宽、Qwen/Phi 反侧分别验收；C 仅 Llama3.1-8B-Instruct 的逐 token/block MSE 比较，不证明所有动态精度路由无效。Ampere/RTX A6000、单 token 及 kernel 高 batch 退步不授生产吞吐；§5.7 integration 与 §6 future integration 措辞冲突留报告，不凭此授部署完成。必要源/具体 owner 差异 root 非作者核通过，root 实际写后复核通过，日级 Gate 待验；未核代码或复现。

- `SF-2026-ARXIV-2512-24545` — Daily `2026-01-02`；[More Than Bits: Multi-Envelope Double Binary Factorization for Extreme Quantization exact-v1](https://arxiv.org/html/2512.24545v1) §3.2/§4.1–4.4/Theorem4.2、Eq12与Table1。5分factor-envelope知识缺口深入，固定mask factor近似与adaptive-mask ADMM保证分开，inner rank不解除envelope秩一，执行l²/metadata与更大l退步边界；不授整模型resident bits或真实加速。未运行代码；root必要原源/owner通过，实际正文/邻接写后经root非作者实际复核通过。

- `SF-2026-ARXIV-2602-04595` — Daily `2026-02-06`；[Harmonia exact-v1](https://arxiv.org/html/2602.04595v1) III-A 残组临时转换/最终 V-cache commit、IV-C converter 与 V-A 评价及质量反侧。6分具体格式生命周期 gap 深入；仅采用 grouping axis/残组消费与最终提交的分责，不声称残组特定高精度存储实现、任意 RoPE 下 QK folding 或作者已证明全部 cache 不变量。RTL 仿真、TSMC28nm/300MHz/0.9V 综合与 PrimeTimePX VCD、HBM2 bandwidth/cycle 模拟不是实芯片或部署收益；不采 headline 数字。未运行代码；root 必要原源与 owner 提案及实际正文/邻接/末注 POST 通过；日级 Gate 未验收。

- `SF-2026-ARXIV-2601-07475` — Daily `2026-01-14`；[ARCQuant exact-v1](https://arxiv.org/html/2601.07475v1) §3、Tables1–3 与 Appendix D。原2+2+2=6，具体同格式补偿执行计划缺口深入，仅采用激活残差通道、权重列复制及匹配 interleave；scalar bound 不授 GEMM/任务等价。作者有限 RTX5090/PRO6000 prefill 测量不授 decode 或生产 SLO，校准、额外列和在线转换另计；未运行代码或复现。root 必要原源与具体 owner 写前通过；jan01_v3 实际正文1316–1318/前后邻接及2619末注非作者写后复核通过，日级 Gate 未授。

- `SF-2026-ARXIV-2601-08800` — Daily `2026-01-15`；[MixServe exact-v1](https://arxiv.org/html/2601.08800v1) §III-A–D、§IV-A–C。2+2+2=6，collective layout owner 缺口深入；采用 hierarchical A2A/RS/AG 与联合并行计划、H20/910B 相反 DP/EP 反侧，不采用普遍 balanced 最优或生产收益。精度/实际输入输出切分/concurrency/SLO 未披露，未核代码或复现；root 必要原源/owner 写前核通过，root 实际正文/前后衔接及末注非作者 POST 通过，日级 Gate 未授。

- `SF-2026-ARXIV-2601-08089` — Daily `2026-01-15`；[Q-realign exact-v1](https://arxiv.org/html/2601.08089v1) §3.1–3.2/Eq3–5、4.1–4.6及Appendix D/E。2+2+2=6，行为条件PTQ校准差额深入；冻结SLR只是几何proxy，低harmful分不等可用，W4A4/100%单类坍塌和LoRA局部人口保留，不授kernel吞吐。未运行代码或复现实验；root实际必要原源/现owner写前核通过，实际正文与前后邻接非作者POST通过；日级Gate未授。

- `SF-2026-ARXIV-2602-09883` — Daily `2026-02-12`；[AdaTSQ exact-v1](https://arxiv.org/html/2602.09883v1) §3–4/Tables1–4。2+1+2=5，具体owner差额深入：temporal activation allocation与static Fisher-timeweight校准分责，bit-average非物理budget、FLOPs非吞吐，3.6/3.1不采用；未核实现或复现。必要source独立通过、root实际owner写前通过；实际正文、邻接与末注经root非作者POST通过，窄锁释放；非日级Gate。

- `SF-2026-ARXIV-2601-19092` — Daily `2026-01-29`；[Axe exact-v1](https://arxiv.org/html/2601.19092v1) §2.1–2.3、§3.2/3.4、§4.1–4.3及§5。2+2+3=7，评分对象是集合值统一布局这一基础语义而非旧 stride 原则；采用 named resource axes、集合值 D/R/O 映射和 scope lowering，保留人工 warp/pipeline/synchronization、FP8 不及 DeepGEMM 及融合比较 backend 混杂。作者条件为 DGX B200/CUDA13、FP16 GEMM 指定模型权重形状；Trainium 局部结果不外推任意硬件。未运行代码或复现；root 必要原源与 owner 写前核通过，实际正文/邻接/末注经 root 非作者 POST 复核通过，不授日级 Gate。

- `SF-2026-ARXIV-2601-19026` — Daily `2026-01-29`；[Is Finer Better exact-v1](https://arxiv.org/html/2601.19026v1) §3–5、Table1、AppendixF.2–F.3/K。2+1+2=5，具体知识反证深入：有限scale范围/舍入使小block非单调，保留Llama2无inversion、UE4M3动态prescale与UE5M3格式分支共存及硬件改造代价。Eq9/40的zero-scale条件与s=xmax/6变量关系不一致，不采用其精确阈值/概率；4nm八SIMD lane PE综合不是GPU吞吐。未运行代码或复现；root必要source/owner PRE通过，实际正文、邻接与末注经root非作者POST复核通过；非日级Gate。

- `SF-2026-ARXIV-2602-10431` — Daily `2026-02-13`；[exact-v1](https://arxiv.org/html/2602.10431v1) §3–4 entropy/path与PTQ执行率联合控制、Table3/4质量/耗时反侧；Eq9 branch不采用，不授通用加速或同FLOPs恢复。root必要源与实际owner PRE通过，具体差额受影响深入；实际正文/完整邻接与末注已经root非作者实际POST通过，窄锁释放，不授日级。未核代码或复现。

- `SF-2026-ARXIV-2602-15200` — Daily `2026-02-19`；[COMPOT exact-v1](https://arxiv.org/html/2602.15200v1) §3/Eq4–11、§4/Table3/5/7、§5。2+1+2=5，具体字典两个条件子问题差额深入；联合非凸/交替20轮不授one-shot/global optimum，原预算谱与whitening重构谱分开。字典/系数/mask计费、Gram/校准与protocol反侧近正文，无kernel/E2E加速采用。root必要源/实际49及48/50邻接PRE通过并授窄锁；root已实际核两段正文、完整邻接及末注，非作者POST通过，窄锁释放；未核代码或复现，未授日级Gate。

- `SF-2026-ARXIV-2602-15166` — Daily `2026-02-19`；[Fast Fusiest exact-v1](https://arxiv.org/html/2602.15166v1) §III–V、VII-A–G。2+1+2=5，compatible pmapping 与全 lifetime reservation 具体差额深入；只在 mapspace/解析 cost model 下采用安全裁剪条件，cached baseline 时间估算、1000倍搜索预算和未测 GPU execution 反侧保留。root 必要原源与实际 owner PRE 通过并授窄锁；root已实际核正文/完整邻接及末注，非作者POST通过，窄锁释放；未核实现或复现。

- `SF-2026-ARXIV-2602-15172` — Daily `2026-02-19`；[TCM exact-v1](https://arxiv.org/html/2602.15172v1) §III–VI-E。2+1+2=5，storage placement/dataflow 分离及 symbolic currying 具体差额深入；loop reorder 的 storage/partial relevance 条件、shape/divisibility 与 heuristic mapspace 边界保留。37秒单线程是解析映射搜索，不是 GPU kernel latency；root 必要原源与实际 owner PRE 通过并授窄锁，root已实际核正文/完整邻接及末注，非作者POST通过，窄锁释放；未核实现或复现。

- `SF-2026-ARXIV-2602-15563` — Daily `2026-02-19`；[exact-v1](https://arxiv.org/html/2602.15563v1) §3–4与Table2/资源和kernel反侧；2+1+2=5，QAT格式×容量的同weight-memory条件取舍深入，同memory非同compute/速率，总memory/高精度反传和任务反侧保留。root 必要源/actual owner PRE 通过并授窄锁；作者正文/完整邻接已顺读，root 非作者正文/完整邻接及末注 POST 通过，窄锁已释放。未核实现/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-12480` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12480v1) §3.2/4/5，2+1+2=5；固定模型短非AR analog静态线性/digital动态attention与seqbuffer、有限exponent2pass具体差额深入；QAT reference、模拟/解析非整硅片、吞吐减半和外部I/O/变长decode回退近正文。root必要源/actualowner PRE通过并授窄锁，作者实际单段/完整邻接已读，root非作者实际正文/完整邻接/末注POST通过；未运行artifact或复现，非日级Gate。

- `SF-2026-ARXIV-2602-12635` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.12635v1) 必要方法、关键对照及直接限制；2+1+2=5，实际 owner 差额定点深入。root 必要原源/owner PRE 通过并授一段窄锁；仅采用正文的条件分支，不授泛化性能、正确性或安全保证。作者正文及完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST 通过，窄锁释放；未核 artifact 或复现，非日级验收。

- `SF-2026-ARXIV-2602-13052` — Daily `2026-02-17`；[exact-v1](https://arxiv.org/html/2602.13052v1) 必要方法/关键反侧/直接限制；2+1+2=5，实际 owner 差额定点深入。RD proxy/实际整数format/profile分验，不授一般Transformer误差硬界或生产SLO；root PRE 通过并授窄锁，作者完整邻接已顺读，root 非作者实际正文/完整邻接/末注 POST通过，窄锁释放；未核 artifact/复现，非日级 Gate。

- `SF-2026-ARXIV-2602-16075` — Daily `2026-02-20`；[DARTH-PUM exact-v1](https://arxiv.org/html/2602.16075v1) §4.1/4.2/5.2/6/7.1/7.5。2+2+2=6，实际 Boolean-array 交接差额深入；只采用 partial transfer/shift/add、rate 与 live-buffer reserve 条件，71%绑定作者 encoder 模拟，不采 headline 或 GPU decode/芯片质量保证。root 必要原源/actual owner PRE及实际正文/完整邻接/末注非作者POST通过，窄锁释放。未核代码或复现，非日级验收。

- `SF-2026-ARXIV-2602-17063` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17063v1) §3/Assumptions3.3–3.4/Theorem3.6、§4/C4、E3.1–3.6及§6。2+1+2=5，固定sign template的初始化/硬投影/非负幅度codec差额深入；bounded/re-entry假设、sign非低秩、负幅度clamp及target-bpw非全模型费用近正文。root必要原源/actual owner PRE通过并授一段/自身末注窄锁；作者正文/完整邻接已顺读，root非作者实际正文/完整邻接及自身末注POST通过，窄锁释放。未核实现/复现，不授通用锁符号/零存储或加速，非日级验收。

- `SF-2026-ARXIV-2602-16707` — Daily `2026-02-20`；[exact-v1 PDF](https://arxiv.org/pdf/2602.16707v1) §4.1–4.2/5。2+1+2=5，跨 pass equality-state 与 partial extraction 生命周期差额深入；pure straight-line、数值前提、4000-node 截断与整体慢约401倍反侧近文，不授控制流、bitwise 或 LLM 性能保证。root 必要源/actual owner PRE 通过；作者正文/完整邻接已读，root 非作者实际正文/完整邻接/自身末注 POST 通过，窄锁释放。未核实现或复现。

- `SF-2026-ARXIV-2602-20309` — Daily `2026-02-26`；[exact-v1](https://arxiv.org/html/2602.20309v1) §3.2–3.3/4.1–4.4/Table1–4/AppD。2+2+2=6具体interface gap深入；仅layout、接口双统计与action分账，不采用Eq12/17比例施加及clip不一致的exact recipe/零operator保证。LIBERO long/W4A4反侧、模块memory非E2E及物理scope近正文。root必要原源/actual owner PRE通过并授两段+自身末注窄锁；作者actual正文/完整邻接/本末注已顺读，root非作者actual正文917–929/自身末注2752 POST通过，锁释放。未核artifact/复现，非日级验收。

- `SF-2026-ARXIV-2602-17664` — Daily `2026-02-21`；[exact-v1](https://arxiv.org/html/2602.17664v1) §3 Eq8–14、§4相同校准/反退与limits。2+1+2=5，noise/time校准activation重权缺口深入；非按variance选择/非runtime删token/非semantic真值，attention采集成本、反退与原校准/稠密回退近文。root必要原源/actual owner PRE通过并授窄锁；作者实际正文/完整邻接已顺读，root非作者实际正文/完整邻接/自身末注POST通过，窄锁释放。未核实现或复现，非日级Gate。

- `SF-2026-ARXIV-2602-20662` — Daily `2026-02-26`；[TOM exact-v1](https://arxiv.org/html/2602.20662v1) §IV-B–E、V-A–B/V-E。2+2+2=6，固定 base 的 bit-pattern ROM/组合逻辑与可写 adapter/KV 共用容量差额深入；bank/routing 非单调、base revision 及 EDA/Verilator/ROM模块 P&R 非实片边界近正文。root必要原文/actual owner PRE通过并授权两段+自身末注窄写；作者正文/完整邻接已顺读，root非作者实际65/67正文、完整55–75邻接和自身末注POST通过，窄锁释放。未核artifact/复现，不采用 headline能耗、零wake或量化质量普遍保证，非日级验收。

- `SF-2026-ARXIV-2602-22631` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22631v1)，必要原证与实际 owner 差额见当日对应 core/owner packet。新执行者非旧packet作者定点独核后在获锁 owner 窄写；作者已顺读正文与完整前后邻接，root 非写入者实际正文、完整邻接与自身末注 POST通过，窄锁释放。仅采用正文限定机制与反侧，不授代码核验、实验复现或日级 Gate。
- `SF-2026-ARXIV-2602-22592` — Daily `2026-02-28`；[exact-v1](https://arxiv.org/html/2602.22592v1)，必要原证与实际 owner 差额见当日对应 core/owner packet。新执行者非旧packet作者定点独核后在获锁 owner 窄写；作者已顺读正文与完整前后邻接，root 非写入者实际正文、完整邻接与自身末注 POST通过，窄锁释放。仅采用正文限定机制与反侧，不授代码核验、实验复现或日级 Gate。
