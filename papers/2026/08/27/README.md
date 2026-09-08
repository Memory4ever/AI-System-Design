# Daily Research — 2026-08-27

**规范：** V3
**窗口：** 2026-08-26T09:00:00+08:00 ～ 2026-08-27T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-07T23:35:00+08:00

## 1. 结论

本窗完成 14 个每日来源检查。arXiv 以官方 new-announcement 批次冻结 519 个唯一身份，逐项完成题名语义筛选；含义不明确或可能影响大模型/Infra 主线的条目进一步读完摘要。最终保留 30 个 arXiv 材料家族，另有 OpenAI 评测事故报告与智谱 GLM-5.3-Flash 两个官方家族，共 32 项候选；其余主要属于 AI for Science、垂直应用、既有方法的窄任务组合、只增加一个 benchmark 或没有改变长期设计边界的局部改进。独立复核补回 physical authority、edge-chip side channel、batch-dependent MoE security、working-memory sufficiency、episode integrity 与 asynchronous embodied control 等系统性漏项；该判断不沿用旧报告的 submission-time 候选池。

最重要的三条演进是：第一，模型与推理优化从单一算法指标转向 **phase、format、state 与端到端 critical path** 的联合合同；第二，Agent 的 memory、tool call 与 workflow 由自然语言约定转向 **显式身份、时态、最小披露与独立 effect gate**；第三，安全边界从 CPU orchestration 延伸到 GPU kernel flow、模型权重传输和评测 sandbox。全部候选已经完成与分数相匹配的原始证据审阅和 Books 对读；9 项长期机制已写入对应章节并通过独立写后语义复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/Index 与本窗事故技术报告；同一事件定点核对 METR 独立复盘 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 与 Alignment Science 列表检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind/Google Research 列表按原始日期检查并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-META-AI | Research/Results 列表检查至窗口水位并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-QWEN | 官方论文、模型与技术发布入口检查至窗口水位；无独立本窗候选 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究入口与官方仓库发布面检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 仓库/Release 检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表与官方仓库；维护 commit 与窗口外项目已在准入前关闭，无本窗候选 | 已检查 | 无 |
| SRC-ZAI | Research“全部”列表逐项检查；确认 GLM-5.3-Flash 于 2026-08-26 14:00Z 发布 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research/论文目录检查至窗口水位并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与 ERNIE 仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo 论文/博客与官方仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog 与官方仓库检查至窗口水位；财务公告排除，无本窗候选 | 已检查 | 无 |
| SRC-ARXIV | 官方 new-announcement 批次 519 个唯一身份；标题全量语义筛选，含糊/高信号项读完整摘要，30 项进入候选；候选精确 v1 页面均可访问，未见官方 withdrawn 标记 | 已检查 | 无 |
| 表外：[METR 事故复盘](https://metr.org/blog/2026-08-26-openai-hugging-face-incident-investigation/) | 由 OpenAI 事故材料触发，只核对同一事件的独立观察和限制 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [GLM-5.3-Flash](https://www.zhipuai.cn/zh/research/163) | 2026-08-26T22:00:00+08:00 | 混合 linear/sparse attention、IndexPool 与稀疏激活共同改变长上下文模型的 state/cost contract；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md)，并短交接 MODEL-MOE/INFER-KV-CACHE |
| [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/) | 2026-08-26T11:30:00+08:00 ～ 2026-08-27T00:00:00+08:00 | 评测 sandbox 的凭据、网络和监控本身属于安全合同；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [post-graph-rag](https://arxiv.org/abs/2608.24921v1) | 2026-08-27T08:00:00+08:00 | 把 Graph RAG 的抽取准入、双时态事实与 synthesis grounding 连接为一条可审计状态链；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，RAG 只作消费端交接 |
| [ExFold](https://arxiv.org/abs/2608.24938v1) | 2026-08-27T08:00:00+08:00 | 用同一 output-approximation 合同分别约束 prefill 的 token expert 与 decode 的 batch expert pool；3 + 3 + 2 = 8 | 深入完成 | 整合：MODEL-MOE，[Ch21](../../../../books/part-02-model/21-moe.md)，运行时交接 INFER-TENSORRT-LLM |
| [ToolMinimize](https://arxiv.org/abs/2608.24957v1) | 2026-08-27T08:00:00+08:00 | effect admission 前按 schema 改写 tool arguments，补上 allow/block 与信息流标签之间的最小披露层；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Auto-Policy, not Auto-Skill](https://arxiv.org/abs/2608.25091v1) | 2026-08-27T08:00:00+08:00 | 把自然语言 Skill 与可执行 authority policy 分开，以 typed state、lease 与 sensor evidence 决定 physical effect；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY / AGENT-TOOL-CALLING，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) / [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Hydra](https://arxiv.org/abs/2608.25053v1) | 2026-08-27T08:00:00+08:00 | 证明 edge inference 需按 prefill/decode、backend、SoC、格式与长度联合测量；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FLINT](https://arxiv.org/abs/2608.25062v1) | 2026-08-27T08:00:00+08:00 | 将 HBF 作为 HBM 旁的只读权重 tier，并把 burst、refresh 与 address translation 移出前台关键路径；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Understanding the Energy Scaling of LLM Inference](https://arxiv.org/abs/2608.25096v1) | 2026-08-27T08:00:00+08:00 | 把 decode energy 与 context、batch、attention family、KV 增长共同测量，但架构与模型身份仍有混杂；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Transforms for LLM Quantization](https://arxiv.org/abs/2608.25188v1) | 2026-08-27T08:00:00+08:00 | 证明 transform 目标随 bit-allocation 与实际 number format 反转，修正“旋转总是压平越好”的泛化；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Trust the Mass](https://arxiv.org/abs/2608.25230v1) | 2026-08-27T08:00:00+08:00 | 揭示 KV eviction benchmark 的 nominal budget、实际 bytes 与 question-visible ranking 混杂；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md)，并交接 Evaluation |
| [Groundhog Bit-Flip Attack](https://arxiv.org/abs/2608.25276v1) | 2026-08-27T08:00:00+08:00 | MoE 将 EOS 行为集中到少数 expert/routing bits，形成可构造 denial-of-wallet 路径；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Metis](https://arxiv.org/abs/2608.25322v1) | 2026-08-27T08:00:00+08:00 | provider stream 先归一为 typed events，再由 permission 与 lifecycle state 决定 effect；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [LLMscope](https://arxiv.org/abs/2608.25321v1) | 2026-08-27T08:00:00+08:00 | 把模型权重、activation 与 KV 等机密资产的边界推进到 edge accelerator 的物理存储/计算结构；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Capacity Overflow](https://arxiv.org/abs/2608.25371v1) | 2026-08-27T08:00:00+08:00 | 揭示 Vision MoE 的 batch-dependent capacity 可让 backdoor 在小批审计休眠、部署批量激活；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，交接 MODEL-MOE |
| [Here is a GIFT](https://arxiv.org/abs/2608.25431v1) | 2026-08-27T08:00:00+08:00 | 将多租户数据隔离从 CPU orchestration 延伸到 GPU kernel information flow；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Separating Disclosure from Authorization](https://arxiv.org/abs/2608.25474v1) | 2026-08-27T08:00:00+08:00 | 按字段拆分 raw authorization、可审计 projection 与 never-leave 数据；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [MMJailBench](https://arxiv.org/abs/2608.25490v1) | 2026-08-27T08:00:00+08:00 | 将 harmful intent、framing、视觉语义与 instruction carrier 正交化，避免 multimodal jailbreak 归因混杂；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / PLATFORM-SECURITY，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [A Storage-Retrieval Gap in Parametric Knowledge Graph Memory](https://arxiv.org/abs/2608.25489v1) | 2026-08-27T08:00:00+08:00 | 区分“知识能写入 adapter”与“能由 query 找到正确 adapter”，暴露存储与寻址并非同一能力；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [TOPAS](https://arxiv.org/abs/2608.25523v1) | 2026-08-27T08:00:00+08:00 | 在共享 KV 预算内联合选择 prefix residency、request admission、critical path 与 aging；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [When Stale Constraints Go Unchecked](https://arxiv.org/abs/2608.25553v1) | 2026-08-27T08:00:00+08:00 | provenance 可达不等于验证预算会命中已 supersede 的关键约束；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [JIT-Agent](https://arxiv.org/abs/2608.25593v1) | 2026-08-27T08:00:00+08:00 | 把 harness 提升为可生成、修复、演进并单独版本化的 artifact，但生成者不能自证其可靠性；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [AWM](https://arxiv.org/abs/2608.25618v1) | 2026-08-27T08:00:00+08:00 | 最终答案正确与命中 evidence page 均不能证明 terminal working memory 足以独立支持答案；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md)，评测交接 Ch66 |
| [Unmatched Does Not Mean False](https://arxiv.org/abs/2608.25654v1) | 2026-08-27T08:00:00+08:00 | 不完整 reference 把未匹配真值错标为 false，甚至反转 calibration 排名；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SCALE-QA / TSIM](https://arxiv.org/abs/2608.25655v1) | 2026-08-27T08:00:00+08:00 | 平坦混合对话需要恢复完整 operative episode，而非只命中零散相关片段；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [psRL](https://arxiv.org/abs/2608.25683v1) | 2026-08-27T08:00:00+08:00 | 在训练 update phase 利用全局 prefix visibility，联合 placement 与 block KV 管理；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-DISTRIBUTED-TRAINING，[Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [LMSM](https://arxiv.org/abs/2608.25697v1) | 2026-08-27T08:00:00+08:00 | 把 learned evidence、versioned policy 与独立输出 gate 解耦；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [TailSFT](https://arxiv.org/abs/2608.25756v1) | 2026-08-27T08:00:00+08:00 | 用样本学习状态把 SFT 预算转向 under-modeled tail，但没有建立通用过滤规则；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-SFT，[Ch29](../../../../books/part-04-training-system/29-sft.md) |
| [Spectral Allocation](https://arxiv.org/abs/2608.25990v1) | 2026-08-27T08:00:00+08:00 | 以 loss/gradient spectrum 解释 Muon 与 Adam 的方向分配差异；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [AsymSpec](https://arxiv.org/abs/2608.26004v1) | 2026-08-27T08:00:00+08:00 | drafter 使用压缩 context、verifier 保留完整 context，分离 proposal cost 与 exactness；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [StreamPI](https://arxiv.org/abs/2608.26067v1) | 2026-08-27T08:00:00+08:00 | 用 pair 内双向、跨 pair 因果的视觉—动作单元及随机异步训练连接 streaming VLA 与控制时序；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Prefix Sliding](https://arxiv.org/abs/2608.26070v1) | 2026-08-27T08:00:00+08:00 | 长 reasoning 只保留受控 prefix working set，并显式暴露删除与恢复边界；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) 与 INFER-KV-CACHE Ch45 |

## 4. 证据与知识整合

### [GLM-5.3-Flash](https://www.zhipuai.cn/zh/research/163)

官方正文与技术 Blog 固定了 320B 总参数、18B 激活参数、45 层，以及 linear attention 与 sparse attention 的混合结构；IndexPool 将索引器四个缓存向量加权压成一个。公开比较只给每 head/层的计算量与 BF16 KV 平均值，真实并发、硬件拓扑、SLO 和独立复现未披露，因此只采用“混合状态形态需要共同定义模型身份、KV 与 fallback”的机制，不采用厂商能力/价格结论。Ch22 已按 hybrid linear/softmax/sparse state、selector、KV 与 fallback 组织这条边界，IndexPool 只是该合同下的特定实现，故不重复整合。

### [The Hugging Face incident and the road ahead](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)

OpenAI 技术报告与 METR 复盘共同支持：agent 在 evaluation sandbox 获得超出任务所需的 credential 与 network capability，环境成为真实攻击面。证据只覆盖该次事件，不能推出普遍发生率或修复有效性；Ch72 已把 least privilege、secret boundary、sandbox containment 与 independent monitoring 写成 evaluation contract。

### [post-graph-rag](https://arxiv.org/abs/2608.24921v1)

v1 的 Architecture、Temporal Model、Evaluation 与 limitations 显示：vector、edge、chunk 和 community summary 共用 PostgreSQL 身份；抽取结果先经 fail-closed validation；valid time 与 transaction time 分开，并把有效期带入 synthesis。LongMemEval 与三套语料仅支持该实现和所列模型，不能证明单存储普遍优于专用图/向量系统。Ch77 已明确拥有 valid/transaction time、supersession 与当前视图，RAG 只消费该状态，因此本项保留为支持性证据而不重复写入 Ch76。

### [ExFold](https://arxiv.org/abs/2608.24938v1)

v1 将 prefill 的 token-level Top-K 与 decode 的 batch-level expert pool 统一成 budgeted output approximation，用 unlabeled calibration 得到 scalar projector，近似被排除 expert 的输出。vLLM CUDA 实现与最高 1.41× TTFT、2.45× TPOT 绑定论文模型、GPU、batch 和质量平均值；它不保证任意 MoE expert 可折叠，也不保持逐 token exactness。应在 Ch21 写清 phase-specific retained-set 与 approximation error，运行时细节交给 Ch49。

### [ToolMinimize](https://arxiv.org/abs/2608.24957v1)

v1 的方法把工具参数按 schema 分成 necessary/unnecessary，再执行 removal、generalization、substitution、truncation；可选内容层处理必要 free-text 字段里的任务无关敏感信息。307 次 live call 和 25 个 MCP schema 支持作者范围内的 privacy/validity 结果，不证明语义判定永不删掉任务所需数据。Ch78 已有 raw/projection/never-leave 字段层、canonical digest 与 authorization 分离，本项不再重复整合。

### [Auto-Policy, not Auto-Skill](https://arxiv.org/abs/2608.25091v1)

exact-v1 把 Skill 的建议性程序与 physical action 的 authority policy 分离：typed envelope、lease、fresh sensor evidence 与 world state 经确定性 guard 后才到 adapter boundary。60 个构造攻击、60 个 benign case 及 5× 复跑只覆盖一个 NATS/Tailscale edge testbed；实验未触发真实设备，hand-authored guard 也不能发现 compromised trusted principal 或伪造 sensor。它是 Ch72/Ch78 已有 proposal、typed evidence 与 effect-time authorization 的物理场景验证，不形成第二套 Skill owner。

### [Hydra](https://arxiv.org/abs/2608.25053v1)

v1 的 Instrumentation、Dataset 与 Limitations 把 HuggingFace/llama.cpp 的 per-prompt phase timing 与 SoC telemetry 对齐，并覆盖三代 Jetson、13 个 instruction-tuned 模型和五种格式。约 107K 记录只证明 batch=1、dense 1–8B 和这些 edge backend 的工作负载；quantization 降低 traffic/energy 不代表功率单调下降。Ch66 已冻结 phase/backend/device/hardware/format/length 与 telemetry identity，本项不再重复写入。

### [FLINT](https://arxiv.org/abs/2608.25062v1)

v1 的 Design 把 HBF 定位为只读权重 tier：burst-buffer controller 合并/流水读取，phantom-plane refresh 把维护移出 foreground，read-only FTL 删除 SSD 的通用写路径。结果依赖尚未普及的 HBF/NAND 参数与权重只读性，不证明同样设计适用于 KV 或 checkpoint；其长期价值是 capacity tier 的管理语义必须按 workload 专用化。Ch54 已以 FlashAccel 与 byte-addressable tier 写明同一类近存储、预取、只读状态和前台关键路径边界，本项作为实现证据保留，不再追加正文。

### [Understanding the Energy Scaling of LLM Inference](https://arxiv.org/abs/2608.25096v1)

exact-v1 在 A100 40GB、FP16、greedy decode 上测 OPT-1.3B、Phi-3 Mini、Gemma-2B 与 Mistral-7B，改变 context 128–1800、batch 1/2/4/8 并以 NVML 重复测量。它支持“energy 必须绑定 phase、context、batch 与 architecture identity”，但 MHA/GQA/GQA+SWA 同时更换了模型家族与规模，不能把差异因果归给 attention；87% 等数字也不能外推别的硬件、并发或 SLO。Ch66 已完整承载该测量合同。

### [Transforms for LLM Quantization](https://arxiv.org/abs/2608.25188v1)

v1 的 Great Inversion 证明：可变 bit allocation 在固定总 rate 下奖励能量集中，而部署中的 grouped shared-scale、equal-bit quantizer 奖励组内压平；generic spectrum 下两者最优性不能互推。FP4、MXFP4、NVFP4 的 scale/grid 又改变目标，因此 transform、rounding、number format 与 matrix instruction 必须共同选型；综述统计不是端到端 benchmark，不能给出统一赢家。

### [Trust the Mass](https://arxiv.org/abs/2608.25230v1)

v1 枚举 168,192 个 attention rows 的最优保留子集，发现最优选择只闭合相对 full attention 剩余差距的中位 2%–5%；更关键的是强 baseline 以 full-cache mask 实现，nominal token budget 不等于释放 bytes，question-visible ranking 还造成巨大 retrieval margin。该结果不证明 attention weight 永远足够，而是要求 KV eviction 报告真实 storage layout、selector 可见信息与预算 enforcement。

### [Groundhog Bit-Flip Attack](https://arxiv.org/abs/2608.25276v1)

论文通过主动 fault injection 定位与 EOS 等 token 强相关的 expert/routing bits，使生成持续到上限。它证明一种可构造攻击，不证明普通软错频率；硬件、精度和在线检测 SLO 也未完备。Ch72 已要求 fault injection、resource anomaly 与 fail-safe termination 联合验证。

### [Metis](https://arxiv.org/abs/2608.25322v1)

Metis 先把 provider stream 归一成 typed events，再由 permission gate、registry 与 lifecycle machine 决定 effect admission。受限 I/O pairs 与 fault matrix 只证明该 runtime 的 dispatch/trace closure，不证明语义安全或通用 rollback；Ch78 已拥有 proposal、typed action 与 effect gate 的边界。

### [LLMscope](https://arxiv.org/abs/2608.25321v1)

exact-v1 用 electro-optical frequency mapping 在 FPGA LLM accelerator 的 FF/BRAM 边界恢复 embedding、attention、量化 MLP weight、activation 与中间 state，并说明复用同一 storage primitive 可让不同层/地址经过同一物理观测点。证据只覆盖可物理接近、可重复执行且已完成版图/频率表征的 FPGA；对封装更强的 ASIC/GPU、side-channel 发生率与生产攻击成本均未证明。长期增量是 threat model 不能止于软件传输与 at-rest 加密，实际驻留敏感 state 的 chip structure、replay 条件与 tamper boundary 也必须进入 Ch72。

### [Capacity Overflow](https://arxiv.org/abs/2608.25371v1)

exact-v1 在 V-MoE/Swin-MoE 上构造 early backdoor 与 deeper neutralizer，并让 batch-dependent capacity overflow 在小批安全审计时保留 neutralizer、部署大批时丢弃它。76%–87% activation-mode ASR 只绑定 ImageNet-100/GTSRB、作者模型与攻击者可控 supply chain，不证明所有 MoE 都存在后门。它补出 Ch72 的关键 deployment-identity 缺口：安全回归必须覆盖真实 batch/capacity/router/drop policy，不能仅在 batch=1 或平均质量上验收权重。

### [Here is a GIFT](https://arxiv.org/abs/2608.25431v1)

GIFT 让 CPU 侧以 per-user encryption 隔离内容，GPU 侧静态分析 kernel flow 并由 tracker 执行信息流规则；vLLM/DistServe prototype 的开销只绑定已建模 kernel 与论文 threat model。CPU 修改数据的假设、未知 kernel 的 sampled rule、side channel 和生产并发均未闭合，故不能把 prototype 当完整多租户保证。Ch72 已吸收这条限制。

### [Separating Disclosure from Authorization](https://arxiv.org/abs/2608.25474v1)

v1 按字段把 action parameter 分为 raw、projection 与 never-leave，并让 client 在最小化前承诺 canonical digest 和 policy/schema version。projection 仍可能泄漏，远端服务与恶意 verifier 未覆盖；它支持最小披露和 attestation，却不能替代 effect-time authorization。Ch78 已承载该责任边界。

### [MMJailBench](https://arxiv.org/abs/2608.25490v1)

exact-v1 正交改变 harmful intent、prompt framing、visual semantics 与 instruction carrier，并在 16 个 MLLM 上展示不同因素的脆弱性排序随模型而变。内部 representation 诊断只针对一个开放模型，judge 与 harm taxonomy 也会改变结论；它不能推出某种视觉载体普遍更危险。Ch66/Ch72 已要求 factorized slice、judge identity 与 capability/effect gate 分开，本项作为多模态支持性证据即可。

### [A Storage-Retrieval Gap in Parametric Knowledge Graph Memory](https://arxiv.org/abs/2608.25489v1)

MetaQA 实验显示 entity-specific LoRA 可写入事实，oracle 选中正确 adapter 时能恢复答案；但 embedding 与 weight geometry 的相似度检索仍近 chance。该证据限单数据集、单 adapter 粒度和离线注入，不证明 parametric memory 更便宜或更安全；Ch77 已把 storage、write policy、retrieval policy、composition 与 authorization 分成不同责任，本项仅补充受限反例，不再重复整合。

### [TOPAS](https://arxiv.org/abs/2608.25523v1)

TOPAS 同时评估保留 prefix 的下游复用、GPU memory、剩余 workflow critical path、迁移/抢占与 aging。SGLang prototype、synthetic DAG 和 MetaGPT workflows 不证明生产 fairness 或 tail SLO，但说明只优化 cache hit 会伤害整体 JCT；Ch56 已把 request、state 与 workflow priority 联合建模。

### [When Stale Constraints Go Unchecked](https://arxiv.org/abs/2608.25553v1)

v1 将 immutable provenance 与 mutable current record 分开：记录已 supersede，但模型在有限 verification budget 下很少检查看似 settled 的关键路径；forced-critical 与 target-blind allocation rule 显著减少 stale-consistent decision。forced-critical 使用实验者 oracle，不是通用 scheduler；Ch77 已要求检索只消费 current record，并把 freshness、supersession、criticality 与验证责任纳入 retrieval policy，因此本项不形成新的正文增量。

### [JIT-Agent](https://arxiv.org/abs/2608.25593v1)

exact-v1 把 memory、planning、action protocol 与 tool/skill orchestration 编成四模块 harness artifact，由单独模型按任务生成、修复并从历史配置演进。作者 benchmark 支持特定模型/任务上的系统级收益，却不能把提升归为 base-model 能力，也不能证明生成 harness 的安全、可复现性或跨环境稳定。Ch84 已把 model、harness、tool schema、environment 与 verifier 共同版本化，并要求 generated harness 经独立验证后 promotion，因此判 Existing Coverage。

### [AWM](https://arxiv.org/abs/2608.25618v1)

exact-v1 定义 memory-only answerability：移除 page image 与 trajectory 后，只凭 question 和 terminal memory 重新回答。gold evidence page 条件下仍有 42.5% 的正确答案留下不可回答 memory，证明“访问过证据”和“最终答对”不能代理中间状态质量；AWM-GRPO 再把该信号作为不覆盖 final-answer reward 的附加项。证据只覆盖 Qwen3-VL-4B、两个文档数据集和固定 reader/judge，且 answerability 不等于 claim grounding。Ch77 应把 terminal memory 视作单独 artifact，以 sufficiency 与 grounding 两个 Gate 验收；Ch66 只拥有 scorer contract。

### [Unmatched Does Not Mean False](https://arxiv.org/abs/2608.25654v1)

v1 固定输出与分数，只改变 finite-reference proxy label，展示 Brier risk 与 calibration ranking 可被遗漏真值反转；blinded adjudication 和独立 OpenToM 数据复现方向。它不证明作者的 restore 流程适合全部开放式任务，但足以要求 evaluation 把 reference coverage、matcher、human audit 与 uncertainty 同时报告。

### [SCALE-QA / TSIM](https://arxiv.org/abs/2608.25655v1)

exact-v1 在无显式 session/topic 边界的混合长线程中，把恢复单位定义为 causally coherent operative episode；TSIM 以分段、episode summary 与 cluster routing 重建该单位。3,000 个 audited MCQ 与三类 backend 支持所测设置，却使用合成 counterfactual、确定性选项与有限领域，不证明真实对话中的 episode segmentation 总是可靠。Ch77 应明确相关片段集合并不自动构成可执行记忆，完整 episode 还要保存约束、决定、时间与 supersession；分段不可信时回退原始 transcript 与人工确认。

### [psRL](https://arxiv.org/abs/2608.25683v1)

psRL 利用 update phase 的全局可见性，在 prefix reuse 与 load balance 间联合放置 workload 并管理 block KV。throughput 绑定 production traces 与特定拓扑，不外推普通 pretraining；Ch36 已将 prefix identity、placement、通信和 update ownership 连接起来。

### [LMSM](https://arxiv.org/abs/2608.25697v1)

LMSM 将 SAE/probe 等 calibrated evidence backend、versioned policy 与 independent buffered-output gate 分开，并保持 request identity 穿过 batching。learned backend 会漂移且不能替代 reference monitor；Ch72 已保留 enforcement owner 与 sensor 的边界。

### [TailSFT](https://arxiv.org/abs/2608.25756v1)

TailSFT 过滤已经拟合的 sequence，把有限 SFT 梯度预算转向 under-modeled tail，并用诊断决定是否启用。OLMo-3 7B、math/code 和特定 GRPO 配方不能证明 easy sample 都应删除；现有 Ch29 的 data coverage、curriculum 与后续 RL 初始分布已经承载这一条件分支。

### [Spectral Allocation](https://arxiv.org/abs/2608.25990v1)

论文沿真实 Transformer checkpoints 对 momentum singular directions 与 loss landscape 做 probing，用 spectrum allocation 解释 Muon/Adam 差异。解释依赖受测架构、规模和近似，不能直接推出通用 optimizer 优越性；Ch28 已以参数几何、稳定性和硬件成本组织 optimizer 选择。

### [AsymSpec](https://arxiv.org/abs/2608.26004v1)

AsymSpec 让 drafter 使用压缩 context 提案，target 在完整 context 上验证，把 draft cost 与生成分布分离。压缩会降低 acceptance，收益依赖 context、batch 与 verifier cost；exactness 只由 target verification 提供。Ch48 已完整承载。

### [StreamPI](https://arxiv.org/abs/2608.26067v1)

exact-v1 将 streaming trajectory 拆为 `(image, instruction/action)` 原子 pair：pair 内双向 attention 保留当前感知—动作耦合，pair 间保持因果；随机 interval 3–7 与 temporal masking 模拟观测、推理和控制异步。LIBERO、真机与 8×H100 实验支持作者系统，训练仍一次载入全部 frame，极端不规则延迟与开放环境 safety 未解决。Ch26 应把 sensor/action pair identity、arrival time 与 control deadline 写进 embodied loop；低延迟同步环境仍可保留简单 sequential controller。

### [Prefix Sliding](https://arxiv.org/abs/2608.26070v1)

论文在长 reasoning 中滑动保留部分 prefix，以减少 attention/KV 工作集。importance estimator 错误会删除仍需状态，恢复完整上下文的成本与长链正确性是核心边界；Ch22/Ch45 已明确工作集、外置证据与 fallback 的共存条件。

## 5. 缺口与下一步

无

独立复核确认 32 个候选均有同标题、同 URL 的证据审阅，并将四项重复机制降级为 Existing Coverage。9 项 Books 增量已写入并通过写后核对：`2608.24938→Ch21`、`2608.25188→Ch49`、`2608.25230→Ch45`、`2608.25321/25371→Ch72`、`2608.25618/25655→Ch77`、`2608.25654→Ch66`、`2608.26067→Ch26`；各 source-family marker 在 Books 中唯一。

## 6. 复核

复核者：`/root/aug09_16`（fresh-context 独立复核）
结论：通过

独立复核重新核对了北京时间窗口和 519 个 official-new-announcement 唯一身份边界，并对 raw inventory 的批次首尾与候选近邻做 false-positive/false-negative 审计；补回的 9 个漏项均已进入 §3 和同标题、同 URL 的 §4，最终 32 项一一对应。候选采用可访问 exact-v1 或官方正文，未见官方 withdrawn 标记；分数、审阅深度和证据限制与处置一致。对 Books 实际正文逐项对读后，将 GLM-5.3-Flash、FLINT、Storage-Retrieval Gap 与 Stale Constraints 从 Integrate 降为 Existing Coverage；其余 9 项已由独立主任务写入唯一 owner，并逐项核对正文位置、机制含义、证据限制、旧方案共存边界和相邻段落衔接，未发现语义越界或重复 owner。本日报所有 Gate 已闭合。
