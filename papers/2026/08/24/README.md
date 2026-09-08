# Daily Research — 2026-08-24

**规范：** V3
**窗口：** 2026-08-23T09:00:00+08:00 ～ 2026-08-24T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T02:15:00+08:00

## 1. 结论

本窗 14 个每日来源完成重检。arXiv official-announcement owner 清单包含 466 个身份（`2608.20341`～`2608.21360`）；全批次标题逐项语义筛选，对可能改变大模型/Infra 长期判断者阅读摘要，冻结 26 个材料家族。旧报告将实际属于 8 月 25/26 日的 SAEM、ClawProBench、NeuroPrefetcher、ToolRobustBench 错放本窗，本版全部移除；Action-JND 正确归属本窗。候选 exact-v1 均可取得，未发现 withdrawn。

本窗最重要的变化不是单项 benchmark，而是 state/identity contract 的扩展：RAG 在检索前就可能因 retention 失败；memory provenance 不能证明内容真实；模型、optimizer、quantized cell、KV、workspace artifact 与 provider effect 都有不同 commit/rollback 语义。12 项长期机制已经写入 Books，12 项已有覆盖，2 项仅保留日报。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 索引按窗口检查 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 入口检查 | 已检查 | 无 |
| SRC-META-AI | publication 列表检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录过滤并去重 | 已检查 | 无 |
| SRC-DEEPSEEK | Updates / Research 检查 | 已检查 | 无 |
| SRC-MOONSHOT | Blog / Research / release 检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表检查 | 已检查 | 无 |
| SRC-ZAI | Research 列表检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research / Blog / Publications 检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与发布入口检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 检查 | 已检查 | 无 |
| SRC-MINIMAX | Blog / Research 检查 | 已检查 | 无 |
| SRC-ARXIV | official owner 清单；466 个身份首尾完成题摘筛选，保留 26 项 | 已检查 | 无 |

没有按需来源被触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [XPerf](https://arxiv.org/html/2608.20370v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | trace replay 稳定复现 nondeterministic Agent serving workload；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Nexus](https://arxiv.org/html/2608.20397v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | tool routing 与 schema-prefill/KV splicing 解耦；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Prerequisite Eviction](https://arxiv.org/html/2608.20400v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 检索前的 retention 已可能删除语义弱相关但结构必要的前置证据；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Optimizer-State Trait Transfer](https://arxiv.org/html/2608.20442v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | state surgery 指出 first moment 可携带后续行为偏置；2 + 1 + 2 = 5 | 标准完成 | 仅报告：受限模型的因果结果 |
| [Diagnosing Long-Horizon Security Agents](https://arxiv.org/html/2608.20563v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | capability exposure 前后 checkpoint 分离 upstream failure；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Open-Weight Masked Introspection](https://arxiv.org/html/2608.20569v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 八个模型对受控内部干预的自我报告不优于 chance；2 + 1 + 3 = 6 | 标准完成 | 仅报告：负结果，不赋予模型自证权 |
| [ACES](https://arxiv.org/html/2608.20614v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | paired live trials 验证 skill package 是否真实改善同一 Agent；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [AgenticRAG-FP](https://arxiv.org/html/2608.20627v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 指定 hop 注入可认证 retrieval fault 并重放 suffix 做因果归因；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Unauthorized Context Disclosure](https://arxiv.org/html/2608.20658v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 合法读取不等于可向当前 tool destination 传输；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [DreamBench-SWE](https://arxiv.org/html/2608.20664v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | hidden oracle 评价跨 session memory hygiene 与 successor validity；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Temporal Validity on Software Histories](https://arxiv.org/html/2608.20685v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | supersession relation 使 code memory 区分旧事实与当前事实；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [AsmEvo](https://arxiv.org/html/2608.20711v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 以已部署 AMDGPU binary 为 oracle 优化 assembly 并检查 functional equivalence；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [CacheTracer](https://arxiv.org/html/2608.20732v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | prefix-cache side channel 推断 LLM reseller 的隐藏 upstream dependency；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-MULTI-TENANT，[Ch71](../../../../books/part-06-ai-infrastructure/71-multi-tenant.md) |
| [ForeTime-VLA](https://arxiv.org/html/2608.20735v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 将未来 world-action latent 蒸馏进 causal VLA 表示；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Multi-Turn Certified Robustness](https://arxiv.org/html/2608.20820v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 将 jailbreak robustness 表为带 safety persistence 的 state-adversarial composition；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [RAG Deserves an Index](https://arxiv.org/html/2608.20845v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 将 query-time 解释改为 ingest-time compilation 与可维护 index；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-RAG，[Ch76](../../../../books/part-07-agent/76-rag.md) |
| [In-Cell Learning](https://arxiv.org/html/2608.20873v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 在 quantization cell 内更新高精度权重，重量化后整数 artifact 不变；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [UpgradeBench](https://arxiv.org/html/2608.20918v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 跨 base release 比较 retain/port/refresh/retrain specialist；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MODEL-REGISTRY，[Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [Quantization-Aware Healing](https://arxiv.org/html/2608.20953v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 压缩+4bit 后 recovery 必须使用 teacher behavior 而非只拟合 hard label；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-LORA，[Ch30](../../../../books/part-04-training-system/30-lora.md) |
| [Comparison-Only Tiny Advisor](https://arxiv.org/html/2608.21027v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | 小 advisor 只比较恢复方向，不承担完整任务求解；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [AID-Guard](https://arxiv.org/html/2608.21159v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | authorization 从 admission 延伸到 provider effect commit/retry/recovery；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Exact Reference Caching for Diffusion Transformers](https://arxiv.org/html/2608.21229v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | mask 结构使 reference K/V 与 denoising target 独立，可精确缓存；3 + 2 + 3 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Utility Under Attack](https://arxiv.org/html/2608.21230v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | content screening/provenance ranking 无法证明持久记忆的事实真实；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [SPICE](https://arxiv.org/html/2608.21240v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | low-rank expert surrogate 预测并以 confidence 调度 CPU-GPU prefetch；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Action-JND](https://arxiv.org/html/2608.21247v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | token compression budget 由 action deviation 而非视觉相似度约束；3 + 3 + 3 = 9 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Artic](https://arxiv.org/html/2608.21341v1) | 2026-08-24T08:00:00+08:00 ～ 2026-08-24T09:00:00+08:00 | natural-language workflow 编译为显式 read/write artifacts 与 constraints；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |

## 4. 证据与知识整合

### [XPerf](https://arxiv.org/html/2608.20370v1)

XPerf 记录真实 Agent trace，再回放 LLM/control-flow/hardware profile 以压低 nondeterminism；回放仍不能代表未记录分支。Ch66 已要求 workload trace、replay 和 SLO identity。

### [Nexus](https://arxiv.org/html/2608.20397v1)

INT8 lookaside + margin gate 先选 tool，再用短 signature 生成参数，KV splice 仅用于适用深度。Ch78 已把 semantic routing、schema identity 与 argument validation 分开，已有覆盖。

### [Prerequisite Eviction](https://arxiv.org/html/2608.20400v1)

固定预算下，query 语义弱相关的 upstream block 可能在 retrieval 前被删，使下游永远无法恢复。**已整合：** Ch77 将 retention correctness 与 retrieval quality 分开；eviction 必须保留 dependency closure，graph heuristic 不确定时回退原证据。

### [Optimizer-State Trait Transfer](https://arxiv.org/html/2608.20442v1)

state surgery 在受测模型中把 first moment 识别为偏置载体，说明 trainer state 不只参数；规模与行为 readout 很窄，暂不改变 Books。

### [Diagnosing Long-Horizon Security Agents](https://arxiv.org/html/2608.20563v1)

checkpoint 标记 capability exposure，以 controlled intervention 区分上游未到达与能力失败。Ch66 已有 stage-local diagnosis、counterfactual intervention 与 end-to-end gate。

### [Open-Weight Masked Introspection](https://arxiv.org/html/2608.20569v1)

对 residual/head/SAE feature 做 masked intervention，八个模型自报不高于 chance。它只证明受测自我报告不可靠，支持但不新增“模型不能自证内部状态”的边界。

### [ACES](https://arxiv.org/html/2608.20614v1)

同 model/sandbox/grader 下比较装载与未装载 skill 的 live trials，并检查失败 slice。Ch66 已把 package evaluation 与 Agent/model identity、paired control、security gate 绑定。

### [AgenticRAG-FP](https://arxiv.org/html/2608.20627v1)

指定 hop 注入 certified fault，再重跑改变后的 suffix，评价诊断器能否识别真正 causal hop。Ch66 已覆盖 intervention-grounded diagnosis，已有覆盖。

### [Unauthorized Context Disclosure](https://arxiv.org/html/2608.20658v1)

Agent 对信息有读取权，却可能无权把它写入特定 tool arguments/destination。**已整合：** Ch72 将 read、use、transmit 分权；tool proposal 必须对字段、目的、受众和用途重新授权。

### [DreamBench-SWE](https://arxiv.org/html/2608.20664v1)

跨 session 软件任务用 hidden executable oracle 区分 retained evidence、stale carryover 与 hygiene。Ch77 已有 supersession、commit 与 protected-slice evaluation。

### [Temporal Validity on Software Histories](https://arxiv.org/html/2608.20685v1)

真实 GitHub fixes 给出 subject-relation-object supersession；相似度 retrieval 无法区分旧新。**已整合：** Ch77 将 valid-time、transaction-time 与 supersedes edge 纳入 memory identity，冲突时返回版本链而非最高相似度。

### [AsmEvo](https://arxiv.org/html/2608.20711v1)

agent 重建 AMDGPU binary 的可汇编表示并生成优化，以 deployed code object 作唯一 behavior oracle。Ch49 已规定 lower-level artifact optimization 必须有 functional/numerical equivalence gate。

### [CacheTracer](https://arxiv.org/html/2608.20732v1)

prefix-cache reuse side channel 测 reseller 间 dependency；只能说明可观测 cache reach，不能证明所有数据流。Ch71 已通过 KeyPooling 写入 upstream principal/cache namespace 与 relay supply-chain 风险。

### [ForeTime-VLA](https://arxiv.org/html/2608.20735v1)

离线 world-action teacher 将 future latent 蒸馏到 causal policy，部署不生成未来帧。Ch26 已覆盖 teacher imagination→policy representation 的蒸馏与 distribution-shift 边界。

### [Multi-Turn Certified Robustness](https://arxiv.org/html/2608.20820v1)

State-Adversarial MDP 与 safety persistence 避免 naive turn-wise bound 指数退化；保证依 embedding threat model。Ch72 已要求多轮 stateful guarantee 和 assumption ledger。

### [RAG Deserves an Index](https://arxiv.org/html/2608.20845v1)

把可预知 read pattern 在 ingest 时编译成维护结构，避免每个 query 重做语义解释。**已整合：** Ch76 增加 ingest compiler/index lifecycle：写放大和 freshness 换低读成本，query pattern 未知或 corpus 小时 query-time 解释仍合理。

### [In-Cell Learning](https://arxiv.org/html/2608.20873v1)

更新被限制在 4-bit quantization cell，重数量化保持 integer codes/scales 完全相同，delta 作为可撤销文件。**已整合：** Ch30 区分 served integer artifact 与 cell-internal adapter；同码不等于同行为，仍需完整 evaluation/rollback。

### [UpgradeBench](https://arxiv.org/html/2608.20918v1)

跨连续 base releases 比较保留、移植、行为刷新和重训 adapter。**已整合：** Ch59 将 model upgrade 变为 lineage-aware decision；artifact compatibility、preserved behavior 与 target evaluation 分开。

### [Quantization-Aware Healing](https://arxiv.org/html/2608.20953v1)

结构压缩+4bit 后用 teacher behavior 恢复，避免 hard-label QAT 过峰坍缩；结果依模型、数据和 recipe。Ch30 已覆盖量化后 adapter recovery、teacher distillation 与 rollback。

### [Comparison-Only Tiny Advisor](https://arxiv.org/html/2608.21027v1)

advisor 不生成完整解，只在候选恢复方向间比较，降低 critic capacity。**已整合：** Ch80 分离 detector、direction comparator 与 actor；小 comparator 的收益依候选质量，不能独自保证恢复。

### [AID-Guard](https://arxiv.org/html/2608.21159v1)

在 provider commit 前重验 request/state，response ambiguity 时保留 reservation，只有 terminal result 或 certified no-effect 才释放/建 successor。**已整合：** Ch72 把 authorization 延伸到 effect lifecycle，delivery fence 防止 retry 产生双重副作用。

### [Exact Reference Caching for Diffusion Transformers](https://arxiv.org/html/2608.21229v1)

structured mask 使 reference K/V 不依 denoising target，可一次计算并精确复用。**已整合：** Ch45 将 cacheability 归因于依赖图；identity 包含 reference、instruction、mask、position 与 layer，mask 改变即失效。

### [Utility Under Attack](https://arxiv.org/html/2608.21230v1)

少量朴素假事实即可污染未来 session，content-only detector 即使能识别 injection 也不识别事实真假。**已整合：** Ch77 将 provenance/authorization 与 epistemic verification 分开；未验证内容只能隔离、询问或带不确定性使用。

### [SPICE](https://arxiv.org/html/2608.21240v1)

low-rank surrogate 预测未来 experts，confidence 决定 CPU/GPU prefetch；错预测浪费 PCIe/slots。Ch54 已有预测式 expert residency、confidence fallback 与 immutable weight identity。

### [Action-JND](https://arxiv.org/html/2608.21247v1)

压缩按 token removal 对 action distribution/trajectory 的可感知影响分配，而非只看视觉 redundancy。**已整合：** Ch26 把 compression evaluation 从视觉质量提升为 closed-loop action deviation，并绑定 latency/control frequency/safety envelope。

### [Artic](https://arxiv.org/html/2608.21341v1)

compiler 将自然语言步骤改成显式 artifact reads/writes，constraints 在每步产物发布前检查。**已整合：** Ch81 区分 prose intent 与 executable workflow IR；编译结果需类型、dependency、version、approval 与 failure transition。

## 5. 缺口与下一步

无

12 项 Books 增量已写入相应机制正文；其余候选均已终态处置，没有剩余可执行工作。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核检查了 466 个 official-announcement 身份的首尾覆盖、26 项准入与漏项、exact-v1/withdrawn、§3/§4 及 Books 实际落点。12 项新增机制均进入对应 owner 的机制正文，保持适用条件、代价、failure boundary 与作者实验范围；机器校验与 diff 检查通过。
