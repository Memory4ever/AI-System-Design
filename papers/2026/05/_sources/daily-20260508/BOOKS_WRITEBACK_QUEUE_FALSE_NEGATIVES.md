# 2026-05-08 Books writeback queue — closure false negatives

> 2026-09-14 root 状态：以下 7 项已按唯一 owner 写回，队列关闭；等待新的非作者 post-write semantic audit。

本队列只交给 root 串行修改共享 Books。它不授权本修复 lane 写 Books，也不把 queued 状态冒充 applied。每项写回后必须对读 owner 的前后段与相邻章节，再由新的独立 reviewer 验收。

## 1. SF-2026-ARXIV-2605-05594

- **Owner / path：** `AGENT-RAG` / `books/part-07-agent/76-rag.md`
- **插入位置：** evidence admission、retrieval support 与 answer confidence 的主线中；向 `MULTIMODAL-REPRESENTATION` 作短 handoff。
- **最小语义增量：** “检索到 oracle 文本”不等于“新增证据只会改善回答”。跨模态 RAG 中，文本可在 prefill 压低视觉 attention mass/sharpness 并产生位置偏置，使原本正确答案 recorrupt。evidence controller 应观测 modality-specific evidence use，而不是只检查 retrieval relevance。
- **状态与控制权：** retriever 拥有候选证据；multimodal model 形成融合状态；evidence gate 负责检测 modality suppression；答案仍由 generator 产生，不能把 attention diagnostic 当 correctness certificate。
- **代价 / failure / fallback：** auxiliary reference pass 增加 prefill 成本且阈值任务相关；错误 retrieval、歧义图像、强模型先验仍可能失败。无稳定诊断时回退到显式 image-only/text-only counterfactual 与人工复核。
- **证据边界：** 只引用论文披露的 6 个模型、3 个数据集与 RTX A5000 配置；不写成通用准确率保证。

## 2. SF-2026-ARXIV-2605-05657

- **Owner / path：** `AGENT-MULTI-AGENT` / `books/part-07-agent/82-multi-agent.md`
- **插入位置：** task-topology matching 与 budgeted fan-out 之间。
- **最小语义增量：** topology selector 可以先从 code/retrieval structure 形成 complexity vector，再选择 DAG；若 action/tool cost 可静态界定，可在任何 LLM call 前以 resource algebra 验证预算守恒。
- **状态与控制权：** selector 只提议 topology；budget authority 签发预算；scheduler 执行 read-parallel/write-serialized graph；artifact handoff 必须单独验收。
- **代价 / failure / fallback：** deterministic-cost、bounded-depth、finite-action 假设不成立时，静态 certificate 不能替代运行时计费与取消；真实软件质量证据不足。
- **证据边界：** sub-ms DAG 与 synthetic issue 只证明编排开销/可执行性，不证明代码质量普遍提升。

## 3. SF-2026-ARXIV-2605-05818

- **Owner / path：** `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md`
- **插入位置：** RAG data leakage / prompt injection threat model。
- **最小语义增量：** RAG extraction 攻击应拆成 query-generation 与 adversarial-instruction 两个可组合控制变量，并把跨轮已泄露内容作为攻击状态。faithfulness/rewriting/reranking 组件可能改善回答却扩大泄露，安全 release 不能只看答案质量。
- **状态与控制权：** attack harness 拥有 query/state；retriever 与 generator 分别记录暴露面；privacy gate 以累计 unique leakage 和预算验收，不由 faithfulness metric 代签。
- **代价 / failure / fallback：** 结果限于论文的 6 attacks、14 LLMs、4 datasets、英文与固定预算；未覆盖的 pipeline 需重新校准。高敏感语料回退到最小权限检索、输出过滤和不可逆 secret boundary。

## 4. SF-2026-ARXIV-2605-05838

- **Owner / path：** `MODEL-LONG-CONTEXT` / `books/part-02-model/22-long-context.md`
- **插入位置：** 一阶 gated/delta recurrent state 之后、serving cache handoff 之前。
- **最小语义增量：** 二阶 momentum 是对 delta-state update 的直接演进：训练时通过 coefficient reordering 获得 causal chunk parallelism，推理时保留 recurrent decode；正确性 contract 是两条执行路径实现同一 state recurrence。
- **状态与控制权：** recurrent core 拥有 primary state 与 momentum state；chunk trainer 只改变计算顺序；backward reconstruction 物化 correction values，而不是重新定义 forward state。
- **代价 / failure / fallback：** 增加 state/activation，训练吞吐可能落后于优化 GDN/Comba，TP 尚未验证；无匹配 kernel 或大模型证据时保留一阶 delta/GDN/attention branch。
- **证据边界：** 只写 400M/1.3B 和披露 benchmark；不外推 7B+ 或通用吞吐优势。

## 5. SF-2026-ARXIV-2605-06014

- **Owner / path：** `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md`
- **插入位置：** quantization rotation / group-size / execution-plan contract。
- **最小语义增量：** rotation 次数不是固定 heuristic，而应由 downstream quantizer 的分布假设决定：scalar quantization 可由两次 RHT 的固定坐标近高斯保证支持；block VQ 还需要消除 block 内相关，可能需要三次。`l3`/`linfinity` moment check 可选择最低充分变换次数。
- **状态与控制权：** quantizer specification 声明 scalar/block 与 codebook；planner 选择 transform count；kernel 实现必须验证 layout、dimension 与成本，不能由 theorem 直接宣称 acceleration。
- **代价 / failure / fallback：** Hadamard-compatible dimension、fixed bounded block 与渐近项限制适用范围；额外 transform 消耗算力/带宽。检查失败或 block 自适应时回退更多 transform 或保守 quantization。
- **证据边界：** 这是 theorem/algorithmic evidence，无经验 throughput 和第一方实现。

## 6. SF-2026-ARXIV-2605-06326

- **Owner / path：** `TRAIN-SFT` / `books/part-04-training-system/29-sft.md`
- **插入位置：** tool-use demonstration、mixture 与 forgetting 主线；向 Ch33 `TRAIN-GRPO` 和 Ch78 `AGENT-TOOL-CALLING` 作短 handoff。
- **最小语义增量：** tool-use SFT 的准入单位不是“包含 tool call 的轨迹”，而是 tool-suited task × 可学习 teacher trajectory。混合 text-only trajectory 保留原推理能力；checkpoint 同时看 `pass@k` 与 response length，避免 loss 继续下降却从 substance 进入 noise；通过后才交 RLVR。
- **状态与控制权：** data curator 拥有 task/trajectory admission；trainer 拥有 mixture；evaluator 选择 checkpoint；RL stage 接收已签发 artifact，不能用后续 reward 掩盖 SFT mode collapse。
- **代价 / failure / fallback：** 数学、4B/30B 范围有限；teacher trace 不透明、任务并不适合工具或 response length 异常时回退 no-tool/SFT branch，并要求人类或领域 verifier。

## 7. SF-2026-ARXIV-2605-06631

- **Owner / path：** `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`
- **插入位置：** 现有 `Compression Release = Accuracy + Calibrated Uncertainty` 段落内扩展，不新建音频方法列表。
- **最小语义增量：** compression release 应报告相对 raw input 的 excess answer error，并以 worst semantic/query family 作为 guardrail；aggregate average 不能抵消局部严重伤害。family partition 本身是 measurement instrument，需要版本化、验证与置信区间。
- **状态与控制权：** compressor 产生候选 artifact；fixed downstream model/evaluator 产生 paired outcome；release gate 基于 family-wise upper confidence bound 签发 budget，不能由平均 accuracy 代签。
- **代价 / failure / fallback：** family 太细导致方差大、太粗会隐藏 harm；selector/backbone 改变即需重测。证据不足时回退 raw/higher-bitrate input 或拒绝 release。
- **证据边界：** 仅限 5 个英文 prompted MC audio-QA 数据集和 Qwen2-Audio-7B/Qwen2.5-Omni-7B；真实 rate-theoretic frontier 未测量。

## 写回后的必做检查

1. 每项只有一个 source-family marker 和一个 canonical owner。
2. 正文能在删除论文名后仍形成“旧路径 → 约束变化 → 新机制 → 代价/failure → fallback”的推理链。
3. 不把作者 benchmark、theorem 或 correlation 扩写为通用性能/正确性结论。
4. 同步 05-08 ledger/report 为 `Applied`，然后由未参与本修复和写回的 reviewer 做 post-write semantic audit。
