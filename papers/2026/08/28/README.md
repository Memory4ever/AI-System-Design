# Daily Research — 2026-08-28

**规范：** V3
**窗口：** 2026-08-27T09:00:00+08:00 ～ 2026-08-28T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T00:35:00+08:00

## 1. 结论

本窗完成 14 个每日来源检查。arXiv 以官方 new-announcement 批次冻结 584 个唯一身份，逐项完成题名语义筛选；标题含义不明确或可能改变模型、训练、推理、平台与 Agent 设计的条目均读完整摘要。最终保留 39 个材料家族（6.7%）进入候选；其余条目主要是 AI for Science、垂直应用、局部任务指标提升、同类组件的新组合、只增加案例而未改变评价合同的 benchmark，或无法指出相对既有知识的具体设计增量。独立复核补回了 multilingual prompt compression、confidential GPU、audio-native Agent RL、real-PLC HIL 与 persistent skill knowledge 等漏项；旧报告的 submission-time 池及其排除结论不作为本轮依据。

本日新增最强信号不是某个单点性能数字，而是四类 state contract 被重新画清：speculative/diffusion inference 中 proposal、mutable cache 与 commit 的边界；Agent 中 immutable skill、mutable execution state 与 durable record 的分离；安全中 approval/weight/context provenance 从 check-time 保持到 use-time；Evaluation 中 harness、reference、metric 与 hidden obligation 本身都属于被测系统。39 项均完成与分数相匹配的原始证据审阅和 Books 对读。独立复核已纠正“高分即整合”的过度吸收；11 项实际缺少的长期命题已写入唯一 owner 并通过写后语义复核。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research/Index 检查至窗口水位；教育研究公告按领域语境在准入前关闭，无本窗候选 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 与 Alignment Science 日期列表检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind/Google Research 列表按原始日期检查并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-META-AI | Research/Results 日期列表检查至窗口水位并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-QWEN | 官方论文与模型列表检查至窗口水位并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-DEEPSEEK | 官网研究入口与官方仓库发布面检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-MOONSHOT | Kimi Blog 与 MoonshotAI 仓库/Release 检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表与官方仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-ZAI | Research、发布说明与官方仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research/论文目录检查至窗口水位并与 arXiv 去重；无独立本窗候选 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与 ERNIE 仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | MiMo 论文/博客与官方仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-MINIMAX | 中英文 Research/Blog 与官方仓库检查至窗口水位；无本窗候选 | 已检查 | 无 |
| SRC-ARXIV | 官方 new-announcement 批次 584 个唯一身份；标题全量语义筛选，含糊/高信号项读完整摘要，39 项进入候选；候选精确 v1 页面均可访问，未见官方 withdrawn 标记 | 已检查 | 无 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [TreeGraft](https://arxiv.org/abs/2608.26112v1) | 2026-08-28T08:00:00+08:00 | 多成本 drafter 在共享树上非破坏 graft，并由在线 state 决定是否调用强 drafter；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-SPECULATIVE-DECODING，[Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Label-Free Doubt Signals for Abstention](https://arxiv.org/abs/2608.26121v1) | 2026-08-28T08:00:00+08:00 | 用冻结模型的 answer log-prob 训练 abstention，并明确 confidently-wrong ceiling；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Lost in Compression](https://arxiv.org/abs/2608.26175v1) | 2026-08-28T08:00:00+08:00 | 证明 English-trained compressor 与目标 tokenizer 在跨语言预算下会形成非对称信息损失；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-CONTEXT，[Ch75](../../../../books/part-07-agent/75-context.md)，交接 MODEL-TOKENIZER / Evaluation |
| [Harness Engineering](https://arxiv.org/abs/2608.26197v1) | 2026-08-28T08:00:00+08:00 | deterministic wrapper、schema-constrained plan 与 retry 改变执行方差，但延迟收益依赖模型；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Agents Don't Paginate](https://arxiv.org/abs/2608.26130v1) | 2026-08-28T08:00:00+08:00 | 否定“首位命中率提高就会改善 Agent 结果”，把目标改为预算内 inclusion；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Reward-Informed Sparse Autoencoders and the Solution-Completeness Confound](https://arxiv.org/abs/2608.26136v1) | 2026-08-28T08:00:00+08:00 | 识别 reward 与 activation feature 的相关可能只是 solution completeness 混杂；3 + 2 + 2 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Affix Cache](https://arxiv.org/abs/2608.26140v1) | 2026-08-28T08:00:00+08:00 | diffusion LM 的双向依赖使 prefix cache 失效，需复用 affix 并重算 request-specific anchors；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，交接 INFER-KV-CACHE |
| [Same Model, Different Harness](https://arxiv.org/abs/2608.26218v1) | 2026-08-28T08:00:00+08:00 | 保持模型和任务不变，仅改 context compaction/stall response 就改变 coding-agent 结果；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [MeshReduce-U](https://arxiv.org/abs/2608.26220v1) | 2026-08-28T08:00:00+08:00 | 在 NoC routing 前先利用 reduction 结合律重写通信图，改变可路由对象；3 + 2 + 2 = 7 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Agent Mesh](https://arxiv.org/abs/2608.26225v1) | 2026-08-28T08:00:00+08:00 | 证明服务网格 retry/circuit breaker 不能直接套到非幂等 delegation，需 delegation identity 与可移动证据；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [SKILL.state](https://arxiv.org/abs/2608.26263v1) | 2026-08-28T08:00:00+08:00 | 将 append-only transcript 改为 immutable skill + mutable validated state + latest observation；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Approved Too Late](https://arxiv.org/abs/2608.26306v1) | 2026-08-28T08:00:00+08:00 | 把 guardrail approval 从 check-time correctness 扩展为 use-time freshness contract；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LowRankArena](https://arxiv.org/abs/2608.26389v1) | 2026-08-28T08:00:00+08:00 | 对齐 backbone、keep ratio、task 与 serving measurement 后，SVD 排名和 nominal savings 会反转；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / INFER-TENSORRT-LLM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) / [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [SILK](https://arxiv.org/abs/2608.26402v1) | 2026-08-28T08:00:00+08:00 | 将权重完整性验证从 load-time RoT 推到 final pre-compute stream boundary；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Vowel Signs Are Not Letters](https://arxiv.org/abs/2608.26449v1) | 2026-08-28T08:00:00+08:00 | 证明 pre-tokenizer regex 可形成 BPE 训练无法突破的多语 fertility 下界；3 + 3 + 3 = 9 | 深入完成 | 整合：MODEL-TOKENIZER，[Ch11](../../../../books/part-02-model/11-tokenizer.md) |
| [SpeechGym](https://arxiv.org/abs/2608.26432v1) | 2026-08-28T08:00:00+08:00 | audio-native observation/action 暴露听觉参数错误与 outcome-only RL 的同组零方差，需 per-turn tool evidence；3 + 3 + 3 = 9 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md)，交接 MULTIMODAL / Tool Calling |
| [VPP](https://arxiv.org/abs/2608.26523v1) | 2026-08-28T08:00:00+08:00 | 固定 chunk 的 attention cost 随 prefix 增长，需 virtual-stage traversal 修复 pipeline imbalance；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-PREFILL，[Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [DuMateBench](https://arxiv.org/abs/2608.26546v1) | 2026-08-28T08:00:00+08:00 | 将 history、persistent config、workspace state 与 insufficient/unstable/noisy environment 纳入 Agent evaluation identity；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / AGENT-PLATFORM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) / [Ch84](../../../../books/part-07-agent/84-agent-platform.md) |
| [Benchmarking Confidential Computing on Blackwell GPUs](https://arxiv.org/abs/2608.26575v1) | 2026-08-28T08:00:00+08:00 | 将 CC 开销拆成可摊销 host-operation cost 与随 encrypted NVLink traffic 变化的 collective cost；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，交接 Evaluation / Cost |
| [Dependency-Aware Revocable Decoding](https://arxiv.org/abs/2608.26574v1) | 2026-08-28T08:00:00+08:00 | diffusion decoding 分离 masked、candidate 与 committed，并避免低可信 token 污染验证上下文；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [Unsaid, Unsafe?](https://arxiv.org/abs/2608.26588v1) | 2026-08-28T08:00:00+08:00 | 功能 specification 未包含的 security obligation 必须从独立 ontology/evidence 恢复；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / PLATFORM-SECURITY，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) / [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Launch-Bound and Substitutable](https://arxiv.org/abs/2608.26612v1) | 2026-08-28T08:00:00+08:00 | 证明 MoE isolated-kernel 加速、route overlap 与端到端收益/质量可彼此脱钩；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Risks and Controls for Multi-Agent Systems](https://arxiv.org/abs/2608.26626v1) | 2026-08-28T08:00:00+08:00 | 按 shared governance owner 区分 singular、federated 与 open multi-agent control gaps；2 + 2 + 2 = 6 | 深入完成 | 已有覆盖：AGENT-MULTI-AGENT，[Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [Prediction-Powered Evaluation and Meta-Evaluation](https://arxiv.org/abs/2608.26638v1) | 2026-08-28T08:00:00+08:00 | 用少量人工标签校正自动指标偏差，并把点估计改成区间合同；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Beyond Execution](https://arxiv.org/abs/2608.26753v1) | 2026-08-28T08:00:00+08:00 | 将“代码可运行”与实现忠实、实验可检验和结论受支持分开；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Ring Forcing](https://arxiv.org/abs/2608.26794v1) | 2026-08-28T08:00:00+08:00 | 将长视频记忆拆为 object permanence 与 addressable history capacity，并用 ring training 强制远距检索；3 + 3 + 2 = 8 | 深入完成 | 整合：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md)，交接 World Models |
| [PLCBench](https://arxiv.org/abs/2608.26882v1) | 2026-08-28T08:00:00+08:00 | real-PLC HIL 把 tool access、accepted write、process-linked effect 与 sustained physical impact 分阶段验收；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY / PLATFORM-EVALUATION-SYSTEM，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) / [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Disentangling Optimization Scale from Preference Scale in DPO](https://arxiv.org/abs/2608.27032v1) | 2026-08-28T08:00:00+08:00 | 拆开 beta 的偏好噪声语义与梯度尺度，修正跨 beta loss 比较；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：TRAIN-DPO，[Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [The Framing Gap](https://arxiv.org/abs/2608.27092v1) | 2026-08-28T08:00:00+08:00 | 语义 framing 可绕过表面内容防御，控制点必须落到 destination/capability；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [TwinKV](https://arxiv.org/abs/2608.27128v1) | 2026-08-28T08:00:00+08:00 | 固定 KV budget 内以 pairwise key redundancy 修复 retained-set membership；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Safety Does Not Compose](https://arxiv.org/abs/2608.27141v1) | 2026-08-28T08:00:00+08:00 | trajectory-scoped monitor 无法组合跨轮证据，loop safety state 必须持久并显式 reset；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Tool Outputs Become Commands](https://arxiv.org/abs/2608.27146v1) | 2026-08-28T08:00:00+08:00 | 分离 action induction 与 execution authorization，防止来源在历史中被“洗白”；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Calibrated Enough to Know, Not Calibrated to Act](https://arxiv.org/abs/2608.27167v1) | 2026-08-28T08:00:00+08:00 | fabricated evidence 的权威包装能触发 commitment，而 belief probability 几乎不变；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM / AGENT-TOOL-CALLING，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) / [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [SPA](https://arxiv.org/abs/2608.27234v1) | 2026-08-28T08:00:00+08:00 | plan-first DSL、dual-lattice flow 与带标签 artifact 管理跨 query 污染；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Making Latent Evolution Explicit](https://arxiv.org/abs/2608.27259v1) | 2026-08-28T08:00:00+08:00 | 将 latent WAM 的 transition realization 从 token interaction 中分离为 operator propagation + forcing；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [When Context Gets Root](https://arxiv.org/abs/2608.27299v1) | 2026-08-28T08:00:00+08:00 | harness 重建 context 时可把 tool 内容提升为 user/system-effective 权限；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md)，交接 Agent Platform |
| [PAWBench](https://arxiv.org/abs/2608.27345v1) | 2026-08-28T08:00:00+08:00 | 将 World Model 从单次 plausible video 推进到固定 action 下 repeated-rollout outcome distribution；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |
| [Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?](https://arxiv.org/abs/2608.27443v1) | 2026-08-28T08:00:00+08:00 | 用户提前写 policy 降低 prompt 次数，却未必降低 overreach；preference 与 runtime commitment 必须分开；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [WikiSkill](https://arxiv.org/abs/2608.27454v1) | 2026-08-28T08:00:00+08:00 | 将 raw trajectory、可持续累积的 declarative knowledge 与 executable skill artifact 分为三种 promotion state；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-PLATFORM，[Ch84](../../../../books/part-07-agent/84-agent-platform.md)，交接 AGENT-MEMORY / Workflow |

## 4. 证据与知识整合

### [TreeGraft](https://arxiv.org/abs/2608.26112v1)

v1 的 Shared-Tree Construction、Online Scheduling、Experiments 与 Limitations 显示：强 drafter 可重新打分旧节点并非破坏式 graft，最终仍裁剪到同一 verification budget；离线 value system 再蒸馏为轻量 call/skip scheduler。10 个 model pairs、6 个 benchmarks 支持论文范围内的平均改进，不能外推不同 target、tree budget、batch 或服务 SLO；target-side verification 才维持输出分布。

### [Label-Free Doubt Signals for Abstention](https://arxiv.org/abs/2608.26121v1)

v1 用冻结模型自身答案 token 的平均 log-prob 作为信号，把低信号样本的 LoRA target 改为 abstention。六个 1B–8B 模型、英文短事实 QA、约匹配 coverage 下未检测到相对有标签方法的差异，但 36% confidently-wrong 样本不被信号发现，且只有单一 judge、单次训练。Ch66 已明确内部 confidence 只能作为需校准的 sensor，外部证据、risk–coverage 与 abstention policy 才组成 Gate，本项不重复整合。

### [Lost in Compression](https://arxiv.org/abs/2608.26175v1)

exact-v1 以十种语言的平行内容、目标模型 tokenizer 上的 achieved-budget matching、四种 learned compressor、四种 deterministic control 与十一种 target model 分离语言、预算和模型混杂；超过 25 万次调用显示 English-supervised compressor 在激进预算下系统性损失非英语信息，而 multilingual supervision 也会因 segmenter 与 per-language calibration 失败。结论不证明翻译后压缩普遍最优，且多重比较、task/domain 与生产 latency 仍有限。Ch75 应将 compression artifact 的 supervision language、segmenter/tokenizer、目标语言与实际保留预算共同写入 context policy identity；未校准 slice 回退原文或保守预算。

### [Harness Engineering](https://arxiv.org/abs/2608.26197v1)

exact-v1 把 finite-state execution、forced tool choice、output validation、bounded retry 与 schema-constrained planning 分开；前四项在四个 model×task cell 中产生混合效果，最后一项才消除被 free-text plan 污染的 trace variance。任务仅为两个合成线性 workflow、两种开放模型，`N=100` 的完美 reproducibility 也不等于生产正确性。Ch84 已把 model、harness、state/tool schema 与 verifier 分开版本化，本项作为“确定性约束可能改变被测量对象”的支持证据。

### [Agents Don't Paginate](https://arxiv.org/abs/2608.26130v1)

日志显示受测 agent 不主动取第二页；预注册实验又否定了 `p@1` 提升会带来下游 file-localisation 提升，真正相关的是 gold 是否进入首 chunk。500 个 SWE-bench Verified task 与单轮 probe 不是端到端修复率，外部日志也不证明所有 Agent 都不翻页。Ch78 已把工具结果视为有预算的受控 observation，并要求按当前决策所需证据选择、保留恢复路径；本项是该 inclusion contract 的受限实证，不再追加新机制。

### [Reward-Informed Sparse Autoencoders and the Solution-Completeness Confound](https://arxiv.org/abs/2608.26136v1)

v1 的受控分析显示 reward-aligned SAE feature 可能主要区分“答案是否完整展开”，而不是可独立解释的推理机制。该结论限受测模型、任务与 feature selection，不能否定所有 activation analysis；Ch66 已要求分离观测相关、混杂与因果主张，并把 slice、counterfactual 与外部 outcome 纳入证据合同，本项只提供新的混杂案例。

### [Affix Cache](https://arxiv.org/abs/2608.26140v1)

DLLM 的全局双向 attention 让共享 prefix KV 随生成 token 演化而 stale。ACache 把复用范围扩展为任意连续 affix，只重算由 masked-token cross-attention 选出的 Anchor Tokens；Fast-dLLM 与 Nano-vLLM 结果支持论文设置下约 20% 重算和最高 1.68× throughput，但不保证 anchor selector、质量或收益跨模型成立。需要在 Ch24 先定义 mutable cache，再由 Ch45 接手实现。

### [Same Model, Different Harness](https://arxiv.org/abs/2608.26218v1)

v1 保持模型、任务和 endpoint 不变，对照完整 chronological transcript 与机械压缩旧 tool results/响应 stall 的 closed-loop harness；紧 context 下三个比较方向一致，wide context 则并非全部改善。它没有证明某条 compaction rule 普适最优；Ch84 已明确 `(model, harness, revision, environment)` capability profile 与 context lifecycle identity，本项不重复写入。

### [MeshReduce-U](https://arxiv.org/abs/2608.26220v1)

v1 先用 reduction associativity 做 source coalescing、aggregation islands 与 channel blocking，再对减少后的 carrier graph 路由；deterministic replay 分开报告 latency、total link usage 与 fused usage。结果绑定 mesh-NoC spatial accelerator、lowerable workload 和 replay model，不证明训练/推理集群网络同样获益；长期机制是 compiler 可在 routing 前改变通信问题本身。

### [Agent Mesh](https://arxiv.org/abs/2608.26225v1)

147 个 incident/81 runs 的 failure study 显示：message-level retry、timeout 与 error-rate breaker 在有副作用、跨 invocation 累积和错误归因时会制造重复 mutation 或 false trip。论文从 observation 推导七类 delegation primitive，但没有受控实验验证最终架构；Ch82 已拥有 delegation chain、幂等 commit、retry 与 evidence handoff，本项仅支持其 failure boundary。

### [SKILL.state](https://arxiv.org/abs/2608.26263v1)

v1 将每步输入限制为 immutable procedure `P`、mutable structured state `Σ_t` 和 latest observation `O_t`，reasoning 只生成经确定性 schema 校验的 state delta 后即丢弃。SkillExecBench、InterCode 与 τ-Bench 显示 token/accuracy 改善，但 schema 由域作者设计，错误压缩会永久丢状态，外部世界漂移仍需 observation 修正；这不是“状态已成为充分统计量”的普遍证明。Ch81 已明确稳定 procedure、mutable workflow state、latest observation、schema validation 与 fallback 的责任分离，本项不重复整合。

### [Approved Too Late](https://arxiv.org/abs/2608.26306v1)

v1 区分 fixed-action verdict change、oracle-labelled approval expiry 与 judge-conditioned use-time invalidity，避免把三者混成一个准确率。Freshness-Bounded Shield 以 safe-side margin 与近期 feature volatility 估计有效 horizon，在五个模拟环境降低 expiry；它依赖被观测 feature、shift 和 oracle，不是物理系统安全证明。Ch72 已要求 evidence identity/freshness、expiry 与 effect-time revalidation，本项不再重复整合。

### [LowRankArena](https://arxiv.org/abs/2608.26389v1)

exact-v1 对齐 task version、uniform-precision keep ratio、comparison regime 与 inference measurement，并发布 3 TiB 以上压缩 checkpoint；统一条件后五种 SVD 方法的排名随 backbone/ratio 变化，nominal low-rank savings 也未稳定转为端到端 speedup。该结果受所选模型、kernel、硬件与 workload 限制，不能判定低秩压缩普遍无效。Ch66/Ch49 已要求 artifact、format、kernel、workload 与端到端 SLO 联合比较，本项作为标准化审计证据。

### [SILK](https://arxiv.org/abs/2608.26402v1)

v1 指出 RoT 只在 load time 验证 image，权重随后穿过 DRAM/DMA/interconnect/prefetch 仍可被篡改。SILK 复用量化权重 LSB 形成 chained integrity bits，在 final pre-compute boundary streaming check 并 commit-gate；FP4/INT4 质量与 security trade-off、FPGA throughput 均绑定论文实现，不等于生产 accelerator 已支持。应吸收“artifact identity 必须延续到实际消费字节”。

### [Vowel Signs Are Not Letters](https://arxiv.org/abs/2608.26449v1)

v1 从 GPT-2/HuggingFace ByteLevel 的 `\\p{L}+` pre-tokenizer 推导结构下界：abugida 的 combining marks 在 BPE merge 前被切开，扩大词表或数据无法跨 pre-token boundary 修复。26 种语言、matched tokenizers、268M 模型和 3,479 仓库 census 支持该范围；不证明所有 tokenizer 都受影响。Ch11 应明确 pre-tokenization 是不可由后续 merge 学回的硬边界。

### [SpeechGym](https://arxiv.org/abs/2608.26432v1)

exact-v1 保持任务、工具与 success check 不变，把两端交互改为本地 audio-native omni model，观察到正确 tool/slot 仍会因 waveform 值误听而失败并重复调用；outcome-only GRPO 又因组内几乎全失败而失去相对 credit，逐 turn 的 successful-tool-call reward 恢复训练信号。结果只覆盖作者环境、模型与独立 voice benchmark，process reward 也可能奖励局部正确却危险的动作。Ch33 应把 modality-specific observation error 与 reward density 纳入 trajectory identity，并保留 outcome verifier、authorization 与终局 Gate。

### [VPP](https://arxiv.org/abs/2608.26523v1)

固定 chunk 的计算量随 prefix 增长，均匀 chunk 不等于均匀 stage latency；VPP 以 virtual-stage traversal 重排控制流。收益只在论文长序列、Ascend 拓扑与模型成立，短请求或调度开销主导时固定 pipeline 更简单；Ch43 已承载该边界。

### [DuMateBench](https://arxiv.org/abs/2608.26546v1)

exact-v1 从匿名化生产 session 重建 200 个任务，把 pre-solution history、persistent config 与 workspace state 一并注入隔离容器，并分别施加 insufficient、unstable、noisy environment。五类 framework×四类模型的结果支持 harness/environment 共同决定完成率，但 hybrid LLM judge、隐私筛选与有限任务不能给出生产总体失败率。Ch66/Ch84 已把 environment state、harness 与 scorer 绑定同一 run identity，本项不新增 owner。

### [Benchmarking Confidential Computing on Blackwell GPUs](https://arxiv.org/abs/2608.26575v1)

exact-v1 在同一物理 B200 host 上成对改变 TDX guest 与 GPU CC bit，把性能代价分为随 batch 摊销的 host operation 固定成本，以及随 encrypted NVLink traffic 占比变化的 collective 成本；作者调优栈的 1%–3% 与 stock 栈的 30%–40% 不是可互换结论。证据不覆盖其他 GPU、firmware、拓扑、模型或完整安全证明。Ch72 应将 CC mode、CPU TEE、GPU firmware/attestation、NVLink collective share 与软件配置绑定同一 deployment/evaluation identity；Ch66/Ch70 只消费该身份做测量与成本决策。

### [Dependency-Aware Revocable Decoding](https://arxiv.org/abs/2608.26574v1)

候选 token 在 commit 前可撤销，verifier 不让低可信 token 污染自身上下文；十二个文本/多模态 benchmark 支持作者 speed-quality 结论，不证明所有 diffusion model 或硬件都获益。Ch24 已把它放入 proposal—verification—rollback 演进。

### [Unsaid, Unsafe?](https://arxiv.org/abs/2608.26588v1)

SecRTL-Gen 故意只给 functional specification，把真实 SoC IP 中另存的 security obligation 留给独立 testbench；五个模型出现明显 functional/security gap。RTL-Obliger 先抽 functional-semantic graph，再以 CWE ontology 找 mitigation-evidence gap，最后局部修订。392 个 task、五类 CWE 与 port-observable black-box checks 不能证明所有硬件安全；Ch66/Ch72 已要求把外部 obligation、独立 verifier 与 release/security Gate 分离，不能期待模型“自行想到”，因此本项不形成新的 owner 命题。

### [Launch-Bound and Substitutable](https://arxiv.org/abs/2608.26612v1)

论文表明 isolated kernel 倍数不能代替端到端请求收益；MoE critical path 可能被 launch、routing、memory 与 communication 共同控制，route overlap 也不能直接解释质量。实验绑定作者模型、硬件和执行栈；Ch49 已将 kernel choice 放回 execution plan。

### [Risks and Controls for Multi-Agent Systems](https://arxiv.org/abs/2608.26626v1)

119 页 v1 报告按交互双方共享的最小 governance binding 区分 singular、federated 与 open environment。singular tier 中同一部署组织能够同时拥有 agent、substrate 与 control；federated tier 把责任拆为部署方控制和共同协议/基础设施控制；open tier 则可能没有共同 identity issuer、全局监控者或可强制执行的协议。报告逐层保留上一层风险，并明确 federated joint evaluation、population monitoring、shared identity 等机制在 open environment 中失去默认执行者；Ch82 已按 topology、delegation scope、identity 与协议责任组织 owner，本项不另建治理路线。

这是一份由澳大利亚政府相关机构发布的风险与控制分析框架，材料综合案例、既有文献和设计建议，并非对所列控制做统一实验验证；作者也明确指出开放环境中的 population monitoring、去中心化治理与 agent-shaped substrate 尚未规模部署。可吸收的是 governance topology 改变时 authority、visibility、attribution 与 incident response owner 的迁移；不能把表中的控制当成已验证 effectiveness，不能从案例推导发生率，也不能假设自愿标准覆盖整个开放生态。

### [Prediction-Powered Evaluation and Meta-Evaluation](https://arxiv.org/abs/2608.26638v1)

自动指标作为低成本 predictor，有限人工标签校正其偏差并给出不确定区间，而不是把自动分数当 ground truth。WMT 实验支持该估计合同，不证明相同 annotation savings 在所有任务成立；Ch66 已拥有该边界。

### [Beyond Execution](https://arxiv.org/abs/2608.26753v1)

30 次复现实验显示可运行代码仍可能缩小数据、替换组件或让实验不再检验原命题。样本不支持通用失败率，却足以把实现忠实、协议忠实、结果与结论分成独立 Gate；Ch66 已明确 execution success 不是 Evidence Gate。

### [Ring Forcing](https://arxiv.org/abs/2608.26794v1)

exact-v1 把 autoregressive video diffusion 的长程记忆拆为两种不同失败：object permanence 要求对象离开后重现 identity，memory capacity 要求在固定 sequence length 下仍能访问远距 history。ring-structured training 强制远距 retrieval，compression/timestep composition 与 sparse RoPE 扩大历史跨度；作者视频结果不证明生成 state 是 causal world state，也未闭合真实时间 latency 与跨分布身份。Ch24 应保存“可寻址历史”和“身份重现”两个独立 Gate，Ch25 只在 action-conditioned transition 可验证时接手。

### [PLCBench](https://arxiv.org/abs/2608.26882v1)

exact-v1 用四种商用 PLC×四类闭环 workload、vendor-native interaction、reduced-order process simulation 与独立 deterministic evaluator，沿 usable access、native read、process-linked write 到 sustained physical objective 输出六个隐藏 stage flag。240 次 real-PLC episode 中 accepted write 并不等于最终物理影响；这些数字只绑定该配置、模型和安全披露 artifact。Ch72/Ch66 应把 cyber-to-physical evaluation 的 outcome 定义为可持续 process effect，并保留 stage-local failure/defense evidence；网络可达或单次写入不能替代最终 impact Gate。

### [Disentangling Optimization Scale from Preference Scale in DPO](https://arxiv.org/abs/2608.27032v1)

DPO 的 beta 同时控制 preference noise interpretation 与 gradient scale，使固定 learning rate 下 policy drift 非单调、跨 beta loss 失去可比语义。reformulation 的价值是分离 objective meaning 与 optimization dynamics，不证明新 objective 全面优于 DPO；Ch34 已吸收。

### [The Framing Gap](https://arxiv.org/abs/2608.27092v1)

相同泄露意图经可信主机、签名或完整性 framing 包装后可绕过表面防御，说明控制点应是 destination allow-list 与 capability isolation。安全实验是合成环境，不外推生产攻击率；Ch72 已拥有行为 authority boundary。

### [TwinKV](https://arxiv.org/abs/2608.27128v1)

TwinKV 保留原 eviction policy，只在固定预算内用 pairwise key redundancy 交换 orphan 与 redundant donor，不重建被驱逐 K/V。它证明 composable membership repair，不证明 attention score 普遍无用；Ch45 已承载。

### [Safety Does Not Compose](https://arxiv.org/abs/2608.27141v1)

跨轮攻击把证据拆到多个 trajectory 后，单轮 monitor 无法可靠组合；简单 decay 还允许等待风险归零。理论边界依赖 arbiter 假设，Ch72 已保留 non-decaying loop state、mediated commit 与显式 reset。

### [When Tool Outputs Become Commands](https://arxiv.org/abs/2608.27146v1)

Tool output 只能诱导 action proposal，不能提供 execution authority；effect-time gate 必须独立核对用户目标、来源 provenance 与已执行事实。AgentDojo/AgentDyn 不能替代生产验证，Ch78/Ch72 已分别拥有 proposal interface 与 enforcement。

### [Calibrated Enough to Know, Not Calibrated to Act](https://arxiv.org/abs/2608.27167v1)

12 个模型在 provably unknowable 问题上，随专业化 evidence panel 包装显著增加 directional commitment；全量 fabricated panel 也产生相近诱导，而 stated probability 几乎不随之变化。3B SFT 只在允许 reasoning 的格式迁移，rigid output format 下失效。Ch66/Ch78 已明确 epistemic estimate 与 action Gate 是不同状态、权威外观不是执行证据，本项不重复写入。

### [SPA](https://arxiv.org/abs/2608.27234v1)

SPA 用 plan-first DSL、dual-lattice information flow 与带标签 persistent artifact 防止不可信内容跨 query 获得 authority。严格 integrity 会牺牲 utility，保证依赖 planner/spec 完整性；Ch72 已将它作为 persistent provenance flow 的受限实现。

### [Making Latent Evolution Explicit](https://arxiv.org/abs/2608.27259v1)

LEON 保持 predictive representation 与 policy coupling 不变，只将 transition realization 改为 shared operator basis 上的 context-modulated propagation，加上 additive forcing。controlled dynamics 与两种 WAM formulation 支持该架构变量在作者任务中的作用，不证明 Koopman-style operator 普适优于 Transformer；Ch25 已区分“表示什么状态”和“怎样推进状态”，并已有 operator propagation + forcing 段落，本项不重复整合。

### [When Context Gets Root](https://arxiv.org/abs/2608.27299v1)

v1 证明 context reconstruction 会丢失内容的 origin privilege：tool-level 内容经 delegation、persistent goal、scheduled task 或 custom subagent 可能以真实 user/system-effective role 进入新调用，permission reviewer 因而基于错误 provenance 授权。六个 coding harness、13 个 attack objectives 证明所测配置存在路径，不证明所有版本持续脆弱；修复应保留 origin principal/role 与 transform chain，而非仅增强模型拒绝。

### [PAWBench](https://arxiv.org/abs/2608.27345v1)

同一 observation/action 下重复 rollout 形成 outcome distribution，再与 reference transition 比较，补上单个 plausible video 无法证明动力学分布正确的缺口。场景、离散 outcome 与外部 evaluator 限制外推，也不直接证明 policy 改善；Ch25 已承载。

### [Do User-Authored Permission Policies Improve Protection Against AI Agent Overreach?](https://arxiv.org/abs/2608.27443v1)

113 位非专业参与者在 HITL、自动审阅与 user-authored policy 三组中处理模拟 action。policy 降低 runtime prompts，但多数用户选择 ask，且 overreach 阻断不如另外两组；样本与模拟日不能证明生产效果。Ch78 已把 preference capture、standing rule 与 use-time commitment 分开，并明确 ask 不等于授权，本项不重复整合。

### [WikiSkill](https://arxiv.org/abs/2608.27454v1)

exact-v1 把 execution trajectory、跨轮累计的 declarative wiki 与真正可调用的 executable skill 分成三类 artifact；新的 experience 先 consolidation 到知识层，后续 skill update 才消费它。跨 benchmark/model 的收益与 ablation 支持作者流程，但不能证明 wiki 条目真实、跨模型 transfer 安全或自演化 promotion 可免审。Ch84 已把 raw trajectory、knowledge artifact 与 versioned executable Skill 的 compilation、validation、promotion 和 rollback 分开，Ch77/Ch81 分别拥有记忆与 workflow state；本项作为三段实现证据保留，不重复写入。

## 5. 缺口与下一步

无

独立复核确认 39 个候选均有同标题、同 URL 的证据审阅，并将多项重复机制降级为 Existing Coverage。11 项 Books 增量已写入并通过写后核对：`2608.26112→Ch48`、`2608.26175→Ch75`、`2608.26140/26794→Ch24`、`2608.26220→Ch49`、`2608.26402/26575/26882/27299→Ch72`、`2608.26449→Ch11`、`2608.26432→Ch33`；各 source-family marker 在 Books 中唯一。

## 6. 复核

复核者：`/root/aug09_16`（fresh-context 独立复核）
结论：通过

独立复核重新核对了北京时间窗口和 584 个 official-new-announcement 唯一身份边界，并对 raw inventory 的批次首尾与候选近邻做 false-positive/false-negative 审计；补回的 9 个漏项均已进入 §3 和同标题、同 URL 的 §4，最终 39 项一一对应。候选采用可访问 exact-v1，未见官方 withdrawn 标记；分数、审阅深度和证据限制与处置一致。对 Books 实际正文逐项对读后，将 Agents Don't Paginate、Reward-Informed SAE、SKILL.state、Unsaid Unsafe 与 WikiSkill 等重复机制降为 Existing Coverage；其余 11 项已由独立主任务写入唯一 owner，并逐项核对正文位置、机制含义、证据限制、旧方案共存边界和相邻段落衔接，未发现语义越界或重复 owner。本日报所有 Gate 已闭合。
