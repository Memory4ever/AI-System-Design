#!/usr/bin/env python3
"""Build deterministic JSONL splits for the Qwen3.5-4B LoRA smoke test."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SYSTEM = (
    "你是一名严谨的 AI System 架构师。请直接回答，不展示隐藏思维过程。"
    "答案必须依次包含六个 Markdown 二级标题：问题、原理、机制、权衡、系统连接、演进。"
    "每节最多两句，总长度不超过500个汉字。"
    "区分模型语义、算法机制、Runtime 实现和工程推断，不编造性能数字。"
)
HEADINGS = ("问题", "原理", "机制", "权衡", "系统连接", "演进")


# topic, question, problem, principle, mechanism, tradeoff, connection, evolution
TRAIN_TOPICS = [
    ("AI System", "为什么 AI System 不能被简化成模型加 API？", "模型能产生输出，不等于能力能够稳定交付。", "生产能力来自数据、模型资产、Runtime、资源和治理的共同约束。", "数据生成 checkpoint，artifact 经评估进入 Runtime，再由 Serving、调度和观测形成反馈闭环。", "平台化提高复用与治理，却增加身份、策略和控制面的复杂度。", "它连接能力生产、能力交付、平台治理和 Agent 行动闭环。", "系统从单机实验演进到可复现 Pipeline、在线 Serving 和持续治理。"),
    ("经验风险", "经验风险下降为什么不等于真实任务一定泛化？", "训练只能观测有限样本，而真实输入来自更广的数据分布。", "优化最小化训练分布上的代理目标，泛化还取决于数据覆盖与归纳偏置。", "梯度根据 mini-batch loss 更新参数；held-out evaluation 再检测未参与更新的样本。", "更低训练 loss 可能伴随过拟合，更多正则又可能造成欠拟合。", "它连接数据分布、优化过程、Evaluation 与上线门禁。", "工程实践从只看训练 loss 演进为独立验证、分布切片和线上反馈。"),
    ("梯度下降", "为什么大模型训练通常使用 mini-batch 梯度下降？", "全量梯度代价过高，单样本梯度方差又很大。", "mini-batch 在计算并行度、估计方差和内存预算之间取折中。", "前向计算 loss，反向传播局部导数，多个 micro-batches 可累积成一次 optimizer update。", "更大 batch 提高吞吐并降低噪声，却可能增加显存和改变优化动力学。", "它连接模型学习、global batch、Data Parallel 和训练调度。", "训练从单样本 SGD 演进到加速器上的批处理与分布式梯度聚合。"),
    ("Tokenizer", "Tokenizer 为什么是模型能力边界的一部分？", "模型不直接读取字符串，而读取有限词表中的 token ids。", "切分方式决定序列长度、词表覆盖和不同语言的表示成本。", "文本经 normalization 和 subword/byte 规则映射为 ids，再由 special tokens 表达边界与角色。", "大词表缩短序列却扩大 embedding/output projection；小词表则增加计算长度。", "它位于原始数据、Embedding、训练目标和在线请求之间。", "接口从 word/character 演进到 subword、byte fallback 和多语言联合词表。"),
    ("Embedding", "Embedding lookup 为什么等价于 one-hot 乘矩阵却不这样实现？", "token id 是离散索引，模型需要连续 hidden state。", "选择 embedding matrix 的一行与 one-hot 乘矩阵数学等价。", "输入 `[B,T]` 通过 lookup 变为 `[B,T,d_model]`，避免构造巨大稀疏 one-hot tensor。", "更大词表提高覆盖，却增加参数、带宽和输出投影成本。", "它连接 Tokenizer、Position、Transformer hidden states 和 logits。", "表示从手工稀疏特征演进为端到端学习的稠密向量。"),
    ("RoPE", "RoPE 为什么能把相对位置信息带入 Attention？", "Self Attention 的内容匹配本身不能区分 token 顺序。", "对 Q/K 的二维子空间施加位置相关旋转，使点积包含相对角度差。", "位置 p 对每个频率旋转 Q/K，位置 p 与 q 的内积依赖 p-q。", "它避免显式相对位置矩阵，但长度外推仍受训练分布和频率设计限制。", "它连接 Position Encoding、Attention、KV Cache 和 Long Context。", "位置机制从绝对向量演进到相对偏置、旋转编码和长度扩展策略。"),
    ("Self Attention", "Self Attention 为什么可以理解为内容相关路由？", "每个 token 需要根据当前内容选择读取哪些上下文。", "Q/K 决定连接权重，V 承载被读取的信息。", "计算 `softmax(QK^T/sqrt(d_h)+mask)V`，mask 限制允许的信息流。", "短依赖路径和并行性换来二次 pair 计算与中间状态。", "它连接 Position、Multi-Head、KV Cache 和 Attention kernel。", "序列建模从递归状态演进到全局内容寻址，再出现稀疏和线性变体。"),
    ("GQA", "GQA 为什么能减少 KV Cache 而不减少 Query heads？", "Decode 中历史 K/V 容量和读取会随 head 数增长。", "多个 Query heads 共享较少的 KV heads，保留 Query 投影容量并减少状态。", "令 `H_kv < H`，每组 Query heads 读取同一组 K/V。", "它降低 KV bytes 和带宽，但共享过强可能损失表达能力。", "它连接 Multi-Head Attention、KV Cache、GPU Memory 和 Decode。", "执行形态从 MHA 演进到 MQA，再以 GQA 在质量与状态间折中。"),
    ("MLP", "Transformer 中为什么 Attention 之后仍需要 MLP？", "Attention 主要混合 token 信息，模型还需要逐位置构造非线性特征。", "MLP 先扩维、激活或门控，再压回 residual dimension。", "`[B,T,d_model]` 经 up/gate/down projections，执行层通常映射为 GEMM。", "更大的 `d_ff` 增加容量，也增加参数、FLOPs 和权重带宽。", "它连接 Attention、Transformer Layer、MoE 和 GEMM kernel。", "Dense FFN 从 ReLU 两层结构演进到 GELU、SwiGLU 和条件专家。"),
    ("Pre-Norm", "Pre-Norm 为什么更容易稳定堆叠深层 Transformer？", "深层网络中的梯度必须穿过大量子层和残差路径。", "把 Norm 放在子层前，使 residual path 保持更直接的恒等传播。", "每个 block 计算 `x + Attention(Norm(x))`，再计算 `x + MLP(Norm(x))`。", "Pre-Norm 改善优化稳定性，但末层尺度和表示行为与 Post-Norm 不同。", "它连接 LayerNorm、Residual、训练稳定性和 checkpoint 语义。", "Transformer 从原始 Post-Norm 广泛演进到深模型常用的 Pre-Norm 设计。"),
    ("Decoder-only", "Decoder-only 为什么能统一训练和生成接口？", "模型需要用一个目标同时学习语言分布并支持开放式条件生成。", "Causal mask 让每个位置只根据前缀预测下一个 token。", "训练并行计算所有 shifted labels；运行时按 Prefill 和逐步 Decode 执行。", "统一接口简化扩展，却保留自回归串行生成瓶颈。", "它连接 Pretraining、KV Cache、Sampling 和 Serving。", "架构选择从任务专用 encoder/decoder 演进到通用 causal language model。"),
    ("KV Cache", "KV Cache 为什么缓存 K/V 而不是全部历史 Q？", "每个新 token 都会重新读取历史上下文，重复投影历史状态代价高。", "历史 K/V 会被未来 Query 复用，而旧 Query 不再参与新的输出。", "Prefill 写入逐层 K/V；每个 Decode step 只追加新 K/V 并读取历史缓存。", "它减少重复计算，却让显存容量、生命周期和所有权成为 Runtime 问题。", "它连接 Attention、Decode、PagedAttention、PD 分离和调度。", "生成从无状态重算演进为持有请求级模型状态的 Runtime。"),
    ("Sampling", "Temperature 为什么不是简单的创造力开关？", "模型输出 logits 分布，而产品需要从中选择 token。", "Temperature 缩放 logits 间距，从而改变分布熵。", "先计算 `softmax(logits/T)`，再与 top-k/top-p 等过滤和重新归一化组合。", "较高温度增加多样性也增加错误概率；较低温度提高确定性但可能重复。", "它连接 logits、rollout、在线生成和 Evaluation。", "生成策略从 greedy 演进到受控随机采样和任务相关 stopping policy。"),
    ("MoE", "MoE 为什么能增加总参数却控制单 token 计算？", "Dense MLP 扩容会让每个 token 激活全部新增参数。", "Router 只选择少数 experts，使 total parameters 与 active parameters 部分解耦。", "token 经 top-k route、dispatch、expert GEMM、combine 恢复原顺序。", "稀疏计算换来负载均衡、All-to-All、expert placement 和小 GEMM 问题。", "它连接 MLP、Expert Parallel、通信和推理调度。", "模型容量从统一 Dense 参数演进到条件计算和更细粒度稀疏路径。"),
    ("Long Context", "为什么声明支持更长 context 不等于模型能有效使用它？", "可接受 token 数、位置外推、计算容量和信息利用是不同问题。", "有效长上下文要求 Position、Attention、KV state 和训练分布同时成立。", "系统需分别测 accepted length、retrieval accuracy、TTFT、KV bytes 和并发容量。", "扩大窗口增加能力上限，也增加计算、状态和噪声干扰。", "它连接 Position、Attention、KV Cache、Serving 和 RAG。", "长上下文从位置扩展演进到稀疏/线性机制、分层状态和检索组合。"),
    ("数据质量", "为什么增加训练 token 数不能自动提高模型质量？", "数据可能重复、污染、错误或与目标分布不匹配。", "有效学习量取决于覆盖、质量、配比和独立信息，而不只是字节数量。", "数据流水线执行采集、清洗、去重、过滤、配比、版本化和 lineage。", "严格过滤提高平均质量，却可能损失长尾知识和多样性。", "它连接 Pretraining、Evaluation、Checkpoint 和治理。", "数据系统从一次性语料准备演进为可追踪、可反馈的持续生产链。"),
    ("Pretraining", "Next-token Pretraining 如何形成通用能力？", "模型需要一个可大规模自动构造的监督目标。", "预测下一个 token 迫使模型压缩语言规律和数据中的可预测结构。", "对每个有效位置计算 cross-entropy，并通过大规模 batch 更新共享参数。", "目标通用且可扩展，但不会自动保证真实性、遵循指令或可靠推理。", "它连接数据、Decoder-only、Checkpoint、SFT 和后训练。", "能力生产从任务标注演进到自监督预训练，再由后训练塑造接口。"),
    ("SFT", "SFT 为什么主要塑造接口而不是凭空创造全部能力？", "预训练模型知道大量模式，却未必按用户期望组织输出。", "高质量 demonstrations 提高目标回答轨迹的条件概率。", "chat template 形成 inputs，loss mask 通常只监督 assistant tokens。", "SFT 稳定直接，但受 demonstrations 覆盖限制并可能产生风格过拟合。", "它连接 Pretraining、LoRA、偏好优化和线上 Prompt。", "训练从通用预测演进到 demonstration-based instruction interface shaping。"),
    ("LoRA", "LoRA 为什么能用较少可训练参数改变模型行为？", "全量更新和保存大模型参数的成本很高。", "将权重增量限制为低秩乘积 `DeltaW=(alpha/r)AB`。", "冻结 base weight，只训练 A/B，并在运行时叠加或离线 merge。", "它降低 optimizer state 和 artifact 大小，却引入 base-adapter 身份与兼容性。", "它连接 SFT、Checkpoint、Registry 和 multi-adapter Serving。", "适配从复制全量模型演进到参数高效分支和按需组合。"),
    ("RLHF", "RLHF 为什么需要区分 reward 与真实任务质量？", "人类偏好难直接写成可微分目标。", "Reward Model 或 verifier 提供代理信号，policy 根据该信号更新。", "收集 preference、训练 reward、生成 rollout、优化 policy，并用 reference/KL 限制漂移。", "偏好对齐提高可用性，也可能 reward hacking、模式收缩和能力回归。", "它连接 SFT、PPO/GRPO、Evaluation 和线上反馈。", "对齐从 demonstrations 演进到偏好建模和可验证环境反馈。"),
    ("PPO", "PPO 的 clipping 为什么不能消除 policy drift？", "直接使用高方差 policy gradient 可能造成过大的更新。", "Clipping 限制采样动作概率比的局部变化。", "根据 rollout 估计 advantage，优化 clipped surrogate，并常加入 value 与 KL 项。", "更新更稳但仍依赖 rollout coverage、advantage 质量和多轮训练状态。", "它连接 Reward Model、reference policy、trajectory 和 checkpoint。", "策略优化从无约束 policy gradient 演进到 trust-region 风格的受限更新。"),
    ("GRPO", "GRPO 为什么用组内相对奖励替代显式 value model？", "大模型 RL 中单独训练 value model 会增加显存和系统状态。", "同一 prompt 的多条回答形成比较组，用组内统计量估计相对优势。", "采样 group、计算 rewards、归一化相对 advantage，再更新 policy。", "它减少 value state，却依赖 group diversity、reward 尺度和采样成本。", "它连接 rollout engine、verifier、policy update 和推理资源。", "RL 训练从 actor-critic 分支演进出使用组内基线的简化路线。"),
    ("DPO", "DPO 为什么可以绕过显式 Reward Model rollout loop？", "有 preference pairs 时，完整在线 RL Runtime 可能过重。", "DPO 直接提高 chosen 相对 rejected 的 policy likelihood，并以 reference 约束。", "对 `(x,y_w,y_l)` 计算 policy/reference log-ratio 并优化分类式目标。", "训练简单稳定，但无法探索数据集中没有覆盖的新行为。", "它连接 preference data、reference checkpoint、SFT 和 Evaluation。", "偏好优化从 reward-plus-RL 演进出直接离线目标，同时保留在线 RL 分支。"),
    ("Checkpoint", "为什么 Checkpoint 不能只理解成权重文件？", "恢复训练和部署模型需要不同但可追踪的状态。", "训练轨迹由参数、optimizer、scheduler、RNG、data cursor 和并行 metadata 共同决定。", "保存时建立全局 tensor identity；恢复或转换时按目标 topology 重新分片并验证。", "保存更多状态提高可恢复性，却增加 IO、容量和一致性成本。", "它连接 Training Runtime、Registry、engine build 和 rollout recovery。", "资产从单文件权重演进为可恢复、可转换、可验证的版本化状态集合。"),
    ("Global Batch", "为什么 global batch 需要显式写出 micro-batch、累积和 DP degree？", "分布式训练中的 batch 语义容易被局部配置掩盖。", "一次 optimizer update 消费的样本数由三个独立维度共同决定。", "`B_global=B_micro*grad_accum*DP`，各 DP rank 处理不同样本并聚合梯度。", "增大 global batch 提高吞吐，却可能改变收敛、学习率和数据顺序。", "它连接 Data Parallel、优化器、吞吐和复现。", "训练扩展从单卡 batch 演进到多 rank 与梯度累积共同构成的更新契约。"),
    ("Tensor Parallel", "Tensor Parallel 为什么解决单层算子放不下一张卡的问题？", "单个矩阵权重或 activation 可能超过一张 GPU 容量。", "沿矩阵维度切分同一算子，并用 collective 恢复数学等价输出。", "Column/row parallel 分片 projections，在合适边界执行 All-Reduce 或 All-Gather。", "它降低单卡参数容量，却把通信带入每层关键路径。", "它连接 GEMM shape、NCCL、拓扑、Checkpoint 和推理 layout。", "并行从复制完整模型演进到算子内切分，并与其他维度组合。"),
    ("Pipeline Parallel", "Pipeline Parallel 的 bubble 从哪里产生？", "模型层可跨设备切分，但 micro-batch 必须按依赖依次通过 stages。", "不同 stages 并行处理不同 micro-batches，以流水线覆盖空闲时间。", "调度 warmup、steady state 和 drain，并在 stage 边界传输 activations/gradients。", "增加 micro-batches 降低 bubble 比例，却增加 activation state 和调度复杂度。", "它连接模型分层、micro-batch、通信和训练恢复。", "执行从整模型顺序运行演进到 GPipe、1F1B 和双向重叠调度。"),
    ("ZeRO", "ZeRO 为什么降低显存却不改变 Data Parallel 的数学语义？", "传统 DP 在每张卡复制参数、梯度和 optimizer state。", "ZeRO 分阶段切分这些训练状态，并在需要时通信重建局部计算视图。", "Stage 1 切 optimizer，Stage 2 加 gradients，Stage 3 再切 parameters。", "显存冗余下降，但通信、预取、offload 和 checkpoint 复杂度上升。", "它连接 DP、训练状态、DeepSpeed 和恢复。", "训练从全复制 DP 演进到按生命周期分片和分层存储。"),
    ("Prefill", "Prefill 为什么通常比 Decode 更接近 compute-bound？", "Prompt 中多个 token 已知，可以一次并行处理。", "大 `T_p` 形成较大的 GEMM 和 Attention tiles，提供较高并行度。", "对 prompt 执行全部层，生成首个 logits，并写入逐层 KV state。", "高吞吐计算换来 TTFT、长 prompt 干扰和较大瞬时 workspace。", "它连接 request admission、KV Cache、chunked prefill 和 PD 分离。", "Serving 从整请求串行执行演进到分块 Prefill 和独立资源池。"),
    ("Decode", "Decode 为什么常受权重和 KV 访存限制？", "自回归生成每步只能在前一个 token 完成后继续。", "每步计算量较小，却需要读取大量权重和不断增长的 KV。", "选择 token、构造新输入、执行单 token forward、追加 KV，循环直到停止。", "降低单步延迟与提高 batch throughput 往往互相牵制。", "它连接 Sampling、Continuous Batching、KV capacity 和 TPOT。", "执行从逐请求循环演进到动态 batch、speculation 和分离式部署。"),
    ("Continuous Batching", "Continuous Batching 为什么按 iteration 重组 batch？", "静态 batch 会被最慢请求占住，已完成位置造成 GPU 空洞。", "LLM request 在每个 Decode iteration 都有可重新组合的 token work。", "完成请求退出，新请求或 Prefill chunks 加入，并受 token budget 约束。", "提高利用率却增加排队、抢占和 Prefill/Decode 干扰。", "它连接 scheduler、KV ownership、TTFT、TPOT 和 goodput。", "批处理从固定 request batch 演进为按 token iteration 的动态执行集合。"),
    ("PagedAttention", "PagedAttention 为什么改变 KV 分配而不改变 Attention 语义？", "按最大长度连续预留 KV 会产生严重内部碎片和容量浪费。", "逻辑 token positions 可通过 block table 映射到离散物理 blocks。", "Runtime 分配 blocks、维护映射，并由 kernel 间接定位历史 K/V。", "分页提高利用率和共享能力，却增加 metadata、间接寻址和一致性。", "它连接 KV Cache、vLLM、prefix sharing 和调度。", "KV 管理从连续预留演进到按需分页、共享与分层存储。"),
    ("Speculative Decoding", "Speculative Decoding 为什么可以加速而保持目标分布？", "目标模型逐 token 串行调用限制生成速度。", "便宜 drafter 提议多个 tokens，target 一次批量验证并按校正规则接受。", "生成 candidates、计算 target probabilities、接受共同前缀，拒绝时按 residual distribution 重采样。", "减少 target steps，但收益依赖接受率、验证成本和 drafter compatibility。", "它连接 Sampling、artifact identity、Decode 和调度。", "生成从单模型逐步执行演进到提议-验证和模型内多 token prediction。"),
    ("GEMM Tiling", "GEMM tiling 为什么能减少 HBM 流量？", "逐 output element 计算会重复读取相同 A rows 和 B columns。", "将输出切成 tiles，使片上 A/B tile 被多个 multiply-accumulate 重用。", "TMA 或 load pipeline 搬运下一 tile，MMA 消费当前 tile，epilogue 写回结果。", "更大 tile 增加复用，也消耗 shared memory、registers 并可能降低 occupancy。", "它连接 Linear、cuBLASLt、DeepGEMM、Tensor Core 和量化。", "Kernel 从朴素循环演进到多级 tiling、异步流水和架构专用 MMA。"),
    ("量化", "为什么权重变成 4-bit 不保证端到端推理更快？", "减少存储 bytes 只是执行路径的一部分。", "性能取决于硬件是否原生支持低精度，以及 scale、dequant 和 epilogue 能否融合。", "转换 checkpoint、加载 scales、选择低精度 GEMM，并验证 logits/quality。", "容量和带宽改善可能被反量化、额外 launch 或不支持算子抵消。", "它连接 model artifact、kernel、GPU Memory 和 Evaluation。", "量化从 weight-only 压缩演进到 activation/KV、block scaling 和软硬件协同。"),
    ("vLLM", "为什么不能把 vLLM 简化成 PagedAttention？", "生产 Serving 需要协调请求、KV、执行 worker 和输出流。", "Paged KV 只是内存机制，完整 engine 还需要 request state contract。", "API 请求进入 scheduler，分配 KV，生成 Engine Core work，再由 workers 执行模型。", "集成提高吞吐与可用性，却扩大版本、状态和故障边界。", "它连接 Continuous Batching、PagedAttention、model runner 和分布式 Runtime。", "vLLM 从以分页为突破口演进为包含 scheduler、cache manager 和 workers 的 engine。"),
    ("SGLang", "SGLang 为什么把 program structure 带入推理 Runtime？", "复杂 LLM 应用包含共享前缀、分支和结构化输出，不只是独立请求。", "Runtime 可以利用 prefix tree、grammar state 和 program boundaries 调度。", "Radix cache 复用前缀 KV，constrained decoding 在每步限制合法 tokens。", "复用与可控性提高，却引入 cache identity、grammar CPU 成本和隔离问题。", "它连接 Serving Engine、Agent workflow、prefix state 和 Sampling。", "执行从单次 completion 演进为结构感知的语言程序 Runtime。"),
    ("Dynamo", "Dynamo 为什么位于单机 inference engine 之上？", "一个 engine 不能独自解决多节点请求路由、KV 移动和资源规划。", "分布式 Runtime 需要分离 request、control 和 state paths。", "入口选择 worker/pool，KV-aware routing 使用可验证摘要，planner 调整部署。", "扩大 scale 与弹性，却新增 state freshness、传输失败和跨池调度。", "它连接 vLLM/SGLang、NIXL、PD separation 和 Kubernetes。", "Serving 从单 engine 演进到持有跨 worker 控制与状态路径的分布式 Runtime。"),
    ("GPU Memory", "为什么推理容量不能只用模型权重大小计算？", "权重之外还有 KV、workspace、通信 buffer、碎片和安全余量。", "可接受并发由所有常驻和瞬时 allocations 的联合峰值决定。", "建立 `M_HBM >= M_weights+M_KV+M_workspace+M_comm+reserve` 并按 workload 验证。", "提高利用率减少浪费，却可能降低峰值容错和引发 OOM 抖动。", "它连接量化、KV Cache、batching、PD separation 和 autoscaling。", "容量规划从静态权重估算演进为按 phase 和 SLO 的动态预算。"),
    ("PD 分离", "Prefill/Decode 分离为什么不是免费的资源解耦？", "Prefill 与 Decode 的计算形态和 SLO 干扰不同。", "独立资源池允许分别扩缩容，但必须把 KV state 从 P 池交给 D 池。", "请求在 Prefill 完成后传输逐层 KV、建立 ownership，再进入 Decode queue。", "减少 phase interference，却增加网络、KV transfer、路由和故障恢复。", "它连接 Prefill、Decode、KV Cache、Dynamo 和调度。", "部署从同机聚合演进到 phase-aware disaggregation，并保留小规模聚合分支。"),
    ("推理调度", "为什么推理调度对象不是普通无状态请求？", "LLM 请求跨多个 iterations 持有 token progress 和昂贵 KV state。", "调度必须同时考虑 phase、剩余工作、KV ownership、SLO 和迁移成本。", "分层执行 admission、iteration scheduling、routing、placement 和 autoscaling。", "吞吐、尾延迟、公平性和 cache locality 不能同时最大化。", "它连接 Serving Runtime、GPU Memory、tenant policy 和平台 scheduler。", "调度从 request queue 演进到 state-aware、SLO-aware 的多时间尺度控制。"),
    ("AI Platform", "AI Platform 为什么不是工具列表？", "单点工具不能提供跨团队一致的身份、策略和证据。", "平台用稳定 contracts 组织资源、任务、模型、服务和治理。", "声明 desired state，经 controller 协调 Training、Registry、Serving、Evaluation 和 observability。", "抽象降低重复劳动，却可能产生平台锁定和过度统一。", "它连接能力生产、在线交付、治理和 Agent Platform。", "组织从脚本和工具拼接演进为产品化 control plane 与自助能力。"),
    ("Model Registry", "Model Registry 为什么必须管理 immutable identity 而不只是 latest 标签？", "可变文件名无法支持复现、审计和安全发布。", "模型版本应绑定内容、来源、转换、评估和兼容性证据。", "登记 digest、base/adapter lineage、tokenizer、precision、runtime requirements 和 promotion record。", "强身份提高追踪能力，却增加元数据和发布流程成本。", "它连接 Checkpoint、Evaluation、KServe、rollback 和 Adapter。", "模型管理从共享目录演进到不可变资产、alias 与策略化晋级。"),
    ("KServe", "KServe control plane 为什么不负责执行模型算子？", "平台需要声明和协调服务，而高性能 Runtime 需要靠近模型和 GPU。", "Control plane 管 desired state、revision、network 和 autoscaling；Runtime 管 token execution。", "CRD 被 controller reconcile 为 deployment、service、routing 和 runtime binding。", "声明式治理提高一致性，但不能替代 engine-level KV 和调度优化。", "它连接 Registry、Gateway、Serving Runtime 和 Kubernetes。", "部署从手写工作负载演进到模型服务专用声明式控制面。"),
    ("GPU Scheduler", "GPU Scheduler 为什么需要同时考虑 gang、locality 和 fairness？", "AI workload 需要多个相关设备，单 Pod 最优不代表作业可运行。", "调度需把资源准入、整体就绪、拓扑成本和租户份额联合决策。", "queue/admission 先判定资格，再按 gang 和 topology placement，运行中处理抢占与配额。", "提高集群利用率可能增加排队；追求公平可能牺牲 locality。", "它连接 Training Operator、Serving、quota、cost 和 cluster topology。", "资源分配从单 Pod bin packing 演进到队列化、拓扑感知的 AI workload 调度。"),
    ("Evaluation", "为什么 Reward、benchmark 和上线门禁不是同一个对象？", "训练代理指标可能改善而真实任务失败。", "Evaluation 必须绑定对象、数据、scorer、证据和决策阈值。", "EvalSpec 产生 Evaluation Run，保存原始 outputs、scores、版本和最终 verdict。", "更全面评估增加成本和延迟，但降低错误发布概率。", "它连接 Training、Registry、canary、observability 和 feedback。", "评估从单一离线分数演进到可追溯证据和持续发布决策。"),
    ("Observability", "为什么 GPU utilization 高不能证明 AI 服务有效？", "忙碌可能来自无效计算、排队、重试或不满足 SLO 的工作。", "系统应测量用户结果、阶段延迟、资源消耗和状态因果链。", "Metrics 看聚合趋势，logs 保存事件证据，traces 连接跨组件路径。", "高可观测性增加采集成本和 cardinality 风险。", "它连接 Runtime、scheduler、Evaluation、incident 和 cost。", "运维从主机指标演进到 request/model/artifact identity 贯通的证据系统。"),
    ("RAG", "RAG 为什么不能用更长 Context 完全替代？", "模型窗口扩大不解决知识 freshness、授权和证据定位。", "RAG 在请求时选择可访问的外部证据并注入 Context。", "query 经 authorization、retrieval、ranking、dedup 和 citation assembly 后送入模型。", "提高新鲜度和可追溯性，却引入索引一致性、召回错误和 prompt injection。", "它连接 Context、Embedding、Evaluation、Security 和 Memory。", "知识注入从参数记忆演进为参数能力与外部检索协同。"),
    ("Agent Memory", "Agent Memory 为什么不能只是无限追加聊天记录？", "原始历史会无限增长、相互冲突并包含过期或敏感内容。", "Memory 需要选择、来源、版本、合并和遗忘策略。", "事件经提取、验证、持久化和检索进入 Context；关键状态仍由权威系统持有。", "记忆提高连续性，却引入污染、删除传播和隐私风险。", "它连接 Context、RAG、Workflow、Security 和 user state。", "记忆从会话窗口演进到受治理的 episodic/semantic state 与 forgetting。"),
    ("Agent Workflow", "为什么可靠 Agent 需要 Workflow 而不只依赖模型 Planning？", "模型计划是概率输出，不能独自承担持久状态和副作用一致性。", "Workflow 用显式状态机、权限和恢复边界约束模型决策。", "模型提出 typed action，系统校验后执行、记录结果，并据此推进 authoritative state。", "可控性和恢复提高，却限制开放探索并增加编排成本。", "它连接 Planning、Tool Calling、Reflection、Evaluation 和平台治理。", "Agent 从单轮工具调用演进为模型决策与确定性工作流共同控制的闭环。"),
]

VALIDATION_TOPICS = [
    ("FlashAttention", "为什么 FlashAttention 是 exact Attention 的 IO 优化而不是近似算法？", "朴素实现会把大 score matrix 写回 HBM。", "通过 tiling 和 online softmax，在片上复用数据且保持相同数学结果。", "分块加载 Q/K/V、更新 row max 与归一化统计，再写最终 output。", "减少 HBM traffic，却增加 kernel、数值和硬件适配复杂度。", "它连接 Attention、TMA、Long Context 和 Prefill。", "实现从逐算子 materialization 演进到 IO-aware fused kernel。"),
    ("Adapter identity", "为什么 LoRA Adapter 必须绑定 base checkpoint？", "Adapter 只定义相对于特定 base weights 的增量。", "相同 A/B 应用到不同 base 不再代表同一个函数。", "资产记录 base digest、target modules、rank、alpha、tokenizer 和 merge state。", "强绑定降低误用，却增加版本和部署组合数量。", "它连接 LoRA、Registry、multi-adapter batching 和 rollback。", "资产从孤立 adapter 文件演进到 base-plus-delta 的复合身份。"),
    ("Expert Parallel", "Expert Parallel 为什么与 Tensor Parallel 解决不同问题？", "MoE experts 与单个大矩阵分别产生不同容量瓶颈。", "EP 分配不同 experts，TP 切分同一个算子。", "EP dispatch 使用 All-to-All，TP 通常在算子边界使用 Reduce/All-Gather。", "两者可组合，但 process groups、通信和恢复更复杂。", "它连接 MoE、Grouped GEMM、NCCL 和 topology。", "并行从单维切分演进为 TP/PP/DP/EP 多维组合。"),
    ("Goodput", "为什么 Serving 容量规划应关注 goodput 而不只是 throughput？", "大量超时 token 也能提高吞吐计数，却没有交付有效请求。", "Goodput 只统计满足质量和 SLO 的有效工作。", "按 workload distribution 测量 request/token throughput，并过滤违反 TTFT/TPOT 的结果。", "更严格 SLO 降低名义容量，却更接近用户价值。", "它连接调度、autoscaling、Evaluation 和 cost。", "性能管理从峰值吞吐演进为约束下的有效交付能力。"),
    ("Gateway", "Gateway 为什么不能替代 LLM inference scheduler？", "入口流量治理与 GPU 内 token 调度处于不同时间尺度。", "Gateway 管认证、限流和路由；engine scheduler 管 iteration 与 KV state。", "请求先经外部策略选择服务，再由 Runtime admission 和 batching 推进 token。", "分层提高职责清晰度，却需要传播 identity、deadline 和取消信号。", "它连接 KServe、tenant policy、Serving Engine 和 observability。", "入口从简单负载均衡演进到模型感知路由，但仍不拥有 GPU 执行状态。"),
    ("Security", "为什么模型安全分类器不能直接成为授权系统？", "概率 verdict 可能误判，且不拥有业务权限事实。", "模型可作为风险 sensor，确定性 policy 才能作最终授权。", "输入经身份与权限检查，模型信号参与策略，side effect 再由权威系统提交。", "多层防护降低风险，却增加延迟、误拒和策略维护。", "它连接 Gateway、Tool Calling、Evaluation 和 audit。", "安全从 prompt 约束演进到 policy-as-data 与可追踪执行边界。"),
    ("Tool Calling", "Tool Calling 为什么需要 typed schema 和执行后验证？", "自然语言意图不能安全地直接变成外部副作用。", "Schema 限定参数结构，授权和业务 invariant 仍在模型外验证。", "模型产生 tool intent，Runtime 校验、执行、记录 observation，再把结果返回 Context。", "工具扩大能力，也扩大注入、权限和幂等风险。", "它连接 Prompt、Workflow、MCP、Security 和 Reflection。", "Agent 从生成文本演进为受控地调用外部能力。"),
    ("Reflection", "Reflection 为什么不能被当成模型自动保证正确？", "再次生成仍可能重复原错误或迎合错误反馈。", "Reflection 只有消费独立 observation/verifier 时才形成新证据。", "保存原候选、反馈和修订，比较差异并由外部门禁决定是否接受。", "迭代可修复错误，也增加 token、延迟和自洽幻觉。", "它连接 Evaluation、Workflow、Memory 和 Planning。", "反馈从单次输出后人工检查演进为有预算、可回放的运行时修订。"),
    ("MCP", "MCP 为什么是连接协议而不是 Agent 智能本身？", "模型需要发现和调用外部能力，但各工具接口容易碎片化。", "协议标准化 capability discovery、resource 和 tool invocation contract。", "Client 与 server 协商能力，传递 typed request/result，并由 host 管权限和 Context。", "互操作性提高，却不自动解决授权、正确性和业务事务。", "它连接 Tool Calling、Context、数据源和 Agent Platform。", "工具集成从应用私有适配演进到标准协议与可治理能力目录。"),
    ("成本", "为什么单位 token 成本不能脱离 workload 和 SLO 比较？", "输入长度、输出长度、batch、cache hit 和硬件利用率都会改变成本。", "成本是资源时间与有效交付量的比值，不是固定模型属性。", "记录模型、precision、TTFT/TPOT、并发、失败率和 GPU-hours，再计算 goodput cost。", "追求最低成本可能损害延迟、质量、可靠性或租户公平。", "它连接容量、调度、Evaluation、autoscaling 和 FinOps。", "优化从单卡价格比较演进为质量与 SLO 约束下的单位价值成本。"),
]

TEST_CASES = [
    ("为什么 LoRA loss 下降不能证明模型获得了可靠的新知识？", ["代理目标", "held-out", "base", "评估"]),
    ("比较 Prefill 与 Decode 的计算、内存和 SLO 特征。", ["并行", "串行", "TTFT", "TPOT", "KV"]),
    ("为什么 SM120 支持 TMA 也不能直接运行 SM100 专用 GEMM kernel？", ["ISA", "MMA", "TMEM", "shared memory", "兼容"]),
    ("设计一次 LoRA 实验时，为什么必须保留 base model identity？", ["adapter", "base", "digest", "merge", "回滚"]),
    ("Continuous Batching 与 PagedAttention 分别优化什么瓶颈？", ["调度", "内存", "iteration", "block"]),
    ("为什么平均 TTFT 下降仍可能不满足生产 SLO？", ["分位数", "尾延迟", "workload", "goodput"]),
    ("Checkpoint 转换为推理 Engine 后需要验证哪些契约？", ["tokenizer", "logits", "量化", "layout", "runtime"]),
    ("为什么训练拓扑不能默认等同于推理拓扑？", ["reshard", "TP", "PP", "Serving", "artifact"]),
    ("RAG、Long Context 与 Agent Memory 为什么不是相互替代关系？", ["检索", "窗口", "状态", "freshness", "治理"]),
    ("MoE active parameters 少为什么不保证 Decode 更快？", ["All-to-All", "小 GEMM", "权重", "路由", "负载"]),
    ("为什么量化模型必须同时评估质量、容量和端到端延迟？", ["scale", "dequant", "kernel", "HBM", "质量"]),
    ("PD 分离在什么条件下可能反而降低性能？", ["KV transfer", "网络", "排队", "规模", "SLO"]),
    ("为什么 Evaluation verdict 必须能追溯到原始输出？", ["证据", "scorer", "版本", "审计", "复现"]),
    ("AI Platform 中 desired state 与 observed state 应如何连接？", ["controller", "reconcile", "identity", "status", "policy"]),
    ("为什么 GPU utilization 不能直接用作模型服务扩缩容指标？", ["SLO", "排队", "有效工作", "TTFT", "goodput"]),
    ("Tool Calling 如何避免模型直接执行未授权副作用？", ["schema", "authorization", "validation", "idempotency", "audit"]),
    ("为什么更大的 LoRA rank 不一定得到更好的模型？", ["容量", "数据", "过拟合", "alpha", "评估"]),
    ("如何区分模型知道某个事实与 Runtime 能可靠交付该事实？", ["概率", "检索", "评估", "SLO", "治理"]),
    ("Speculative Decoding 的 acceptance rate 为什么不是唯一性能指标？", ["draft", "verification", "batch", "latency", "target"]),
    ("为什么 Agent Workflow 的权威状态不应只保存在自然语言 Memory？", ["事务", "一致性", "权限", "恢复", "来源"]),
]

REGRESSION_CASES = [
    ("计算 17 乘以 23，只给出结果。", ["391"]),
    ("法国的首都是什么？只回答城市名。", ["巴黎"]),
    ("把英文 hello world 翻译成中文。", ["你好", "世界"]),
    ("给出 Python 列表反转的一个简短表达式。", ["[::-1]"]),
    ("用一句话解释光合作用。", ["光", "二氧化碳", "氧"]),
    ("列出水的三个常见物态，不要解释。", ["固", "液", "气"]),
    ("JSON 中布尔真值如何书写？", ["true"]),
    ("Kafka 中 consumer group 的主要作用是什么？用一句话回答。", ["消费", "分区", "负载"]),
    ("Kubernetes 中 Deployment 与 Pod 的关系是什么？用一句话回答。", ["管理", "Pod"]),
    ("写一个不超过两行的关于月光的中文短句。", ["月"]),
]


def render_answer(record: tuple[str, ...]) -> str:
    _, _, problem, principle, mechanism, tradeoff, connection, evolution = record
    values = (problem, principle, mechanism, tradeoff, connection, evolution)
    return "\n\n".join(f"## {heading}\n{value}" for heading, value in zip(HEADINGS, values))


def conversation(question: str, answer: str) -> dict[str, object]:
    return {
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer},
        ]
    }


def write_jsonl(path: Path, rows: list[dict[str, object]]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )


def main() -> None:
    train: list[dict[str, object]] = []
    for topic in TRAIN_TOPICS:
        name, question, *_ = topic
        answer = render_answer(topic)
        train.append(conversation(question, answer))
        train.append(
            conversation(
                f"在一次 AI System Design Review 中，请从第一性原理解释{name}，并说明机制、权衡、系统位置和演进。",
                answer,
            )
        )

    validation: list[dict[str, object]] = []
    for topic in VALIDATION_TOPICS:
        name, question, *_ = topic
        answer = render_answer(topic)
        validation.append(conversation(question, answer))
        validation.append(
            conversation(
                f"不要列功能清单。请解释{name}为什么出现、如何工作、付出什么代价，以及未来约束变化时会怎样演进。",
                answer,
            )
        )

    test = [
        {
            "id": f"test-{index:02d}",
            "system": SYSTEM,
            "prompt": prompt,
            "expected_concepts": concepts,
        }
        for index, (prompt, concepts) in enumerate(TEST_CASES, start=1)
    ]
    regression = [
        {
            "id": f"regression-{index:02d}",
            "system": "你是一个简洁、准确的助手。严格遵守用户要求，不添加用户没有要求的固定模板。",
            "prompt": prompt,
            "expected_concepts": concepts,
        }
        for index, (prompt, concepts) in enumerate(REGRESSION_CASES, start=1)
    ]

    write_jsonl(ROOT / "train.jsonl", train)
    write_jsonl(ROOT / "validation.jsonl", validation)
    write_jsonl(ROOT / "test.jsonl", test)
    write_jsonl(ROOT / "regression.jsonl", regression)
    print(
        f"train={len(train)} validation={len(validation)} "
        f"test={len(test)} regression={len(regression)}"
    )


if __name__ == "__main__":
    main()
