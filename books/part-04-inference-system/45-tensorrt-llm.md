# 第45章 TensorRT-LLM

**Knowledge Tree:** Part IV Inference System：为什么推理是 AI Infra 的核心战场
**Status:** Draft

**Roadmap Intent:** 面向 NVIDIA GPU 的高性能推理优化。

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

## FlashAttention 在这里的位置

FlashAttention 不只是“更快的 attention”。它的核心思想是 IO-aware：通过 tiling 把 Q/K/V 的块搬到更快的 SRAM 中计算，减少 HBM 读写。

这正好对应 GPU memory hierarchy：HBM 容量大、带宽高，但相比 SRAM 仍然慢；如果 attention 把巨大的 score matrix 写回 HBM，就会被 memory IO 限制。

FlashAttention-2 进一步优化并行划分和 work partitioning；FlashAttention-3 则面向 Hopper 等新硬件利用异步数据搬运、WGMMA/TMA 和低精度能力。它们说明：kernel 优化不是只改数学公式，而是在适配硬件的 memory hierarchy 和执行单元。

## 量化和硬件协同

FP8、FP4、INT8、INT4 这类低精度路径的系统目标，是降低权重、activation 或 cache 的存储和带宽压力，并提高硬件 tensor core 的有效吞吐。

但量化不是免费午餐。低精度需要校准、scale 设计、kernel 支持和质量评估。硬件提供 FP4/FP8 能力，不等于业务模型自动可用；软件栈必须能把模型转换、执行和验证串起来。

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

这里的 parallel mapping 是 inference build/runtime 的选择，不是训练 layout 的
原样继承。一个以 ZeRO、training TP/PP/EP 保存的 checkpoint，可以在
consolidation/resharding 后构建成另一种 Serving topology。转换器必须从
global tensor identity 出发，而不是依赖源 rank 文件名；目标 artifact 还要
重新验证 logits、量化质量和多 rank collective correctness。

可部署 artifact 至少应绑定 model revision、tokenizer、quantization scales、build/runtime version、GPU compute capability、parallel degree 与支持的 shape/context limits。否则一次升级后即使 engine 能加载，也无法说明数值和性能仍与原验证相同。

## In-flight Batching 的位置

TensorRT-LLM 当前官方栈同时包含 in-flight batching 和 paged KV caching。这并不意味着第42、43章被框架章节取代：

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

低精度减少 bytes 只是机制起点；能否换成可交付能力取决于完整验证。

## Trade-off

TensorRT-LLM 这类优化栈的收益通常来自更深的硬件适配，代价是部署复杂度和调试复杂度上升。

它适合需要高吞吐、低延迟、NVIDIA GPU 深度优化的场景；如果团队只需要快速原型，直接使用通用 runtime 可能更简单。工程上要判断的是：当前瓶颈是否已经到了需要 engine build、kernel fusion、quantization 和分布式 runtime 的程度。

更深的硬件适配还意味着支持矩阵并非抽象问题。模型架构、GPU generation、precision、kernel 与 TensorRT-LLM 版本需要形成经过验证的组合。升级其中一项可能改变 engine build、数值质量和性能，平台必须把这些信息作为模型部署制品的一部分记录。

## 本章在知识树中的位置

```text
Decode / Prefill
→ 计算图与 kernel
→ FlashAttention / quantization
→ TensorRT-LLM
→ GPU Memory
→ 推理调度
```

TensorRT-LLM 章节承担的是“从模型计算到 GPU 执行优化”的桥接。

## 自检问题

1. 图优化为什么能在数学结果不变时提高推理效率？
2. operator fusion 主要减少什么开销？
3. FlashAttention 为什么是 memory IO 优化，而不只是 attention 算法名？
4. FP4/FP8 为什么要求软硬件协同？
5. Build-time artifact 与 runtime request state 为什么要分开理解？
6. In-flight batching 在机制层和框架层分别意味着什么？
7. 什么时候值得引入 TensorRT-LLM 这类优化栈？

## 小结

TensorRT-LLM 把模型、NVIDIA GPU 和 Serving runtime 联结成经过优化的 execution contract。Fusion、specialized kernels 与 quantization 降低单步成本，in-flight batching 和 paged KV 则管理持续到来的 request state。

下一章转向 vLLM，观察另一个历史起点：如果首先把 KV allocation 与 scheduler 视为核心，完整 Serving engine 会怎样组织。

## Review notes

Primary-source 校验入口：

- NVIDIA TensorRT-LLM docs: https://docs.nvidia.com/tensorrt-llm/index.html
- FlashAttention: https://arxiv.org/abs/2205.14135
- FlashAttention-2: https://arxiv.org/abs/2307.08691
- FlashAttention-3: https://arxiv.org/abs/2407.08608

本轮 Review 依据当前官方入口补充了 runtime、in-flight batching、paged KV caching 和分布式执行的边界，同时仍将章节主线限定为 NVIDIA GPU execution optimization。具体支持矩阵与性能结论必须绑定版本、模型、精度和硬件，不能从通用图优化原理直接推出。

时效性边界：上述官方入口已在 2026-07 重新核验；由于 TensorRT-LLM 的
backend、quantization 和 hardware support matrix 持续变化，本章不把某个
具体 release 的 feature availability 写成长期结论。
