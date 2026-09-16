# 2026-06-23～28 Books post-Review block fresh audit

审计日期：2026-09-10（Asia/Shanghai）

审计对象：Books 中位于各章 `## Review notes` 之后的 85 个 `recovered-daily-20260623/24/25` 与 `daily-20260627/28` 块。

审计约束：只以保存的 title + abstract、现有 exact-v1 Method/Evaluation/Non-proof locator 与 `## Review notes` 之前的当前正文语义判断；marker、trace、报告中的旧 `Integrate` 字样均不自证正文完成。本文件不授权修改 Books 或 Reports。

## 结论

- 85 个后置块全部是结构违规的“伪正文”：无论其中 family 最终为 A、B 或 C，块本身都应从 `## Review notes` 之后删除；必要的 source-specific locator 与 trace 可留在 Review notes。
- 共核对 182 个 Source Family：**A Existing Coverage 149**、**B 真正正文缺口 11**、**C 不应进入 Books 22**。
- A 的含义是 `## Review notes` 之前已有等价的长期机制；删除后置块不会丢失知识链。若原块 owner 错误，下表给出正确消费 owner，Review note 不应继续冒充该错误 owner 的正文。
- B 的含义是 title/abstract 与 exact-v1 支持一条当前正文尚未完整拥有的长期机制；必须先按下文 proposal 合并进 canonical owner 的正文，再删后置块。
- C 的含义是论文主要贡献是垂直应用、通用非大模型系统、局部 recipe/benchmark 或不改变长期设计选择；删除后置块，并撤销该 family 的 Books `Integrate`，而不是把它搬到另一章。

## 逐块审计

说明：标题为可识别短名；`A→X` 表示现有等价机制由节点 X 拥有，原后置块可删；`B→X` 表示需合并到 X；`C` 表示 de-admit from Books。

### recovered-daily-20260623（24 blocks / 57 families）

| 后置块 | Source Family 逐项结论 | 块级处置 |
| --- | --- | --- |
| `MODEL-MOE` | **A→MODEL-MOE** `2606.22798` *Does the Same Token Mean the Same State?*；正文已明确 token identity 不等于 route/state identity，routing pattern 只是诊断信号。 | 删除块，保留 locator。 |
| `MODEL-LONG-CONTEXT` | **A→MODEL-LONG-CONTEXT** `2606.22874` *SpotAttention*；正文已拥有 selector responsibility、局部/全局 state、校准与 dense fallback。 | 删除块。 |
| `MULTIMODAL-WORLD-MODELS` | **A→MODEL-LONG-CONTEXT / INFER-DYNAMO** `2606.22804` *CoVStream*，edge/cloud 压缩只是已覆盖的有界上下文选择、状态迁移与本地 fallback；**A→PLATFORM-SECURITY** `2606.22966` *Attacking the Trusted Imagination*，正文已把 imagined rollout 限定为 proposal 并保留 environment/controller authority；**A→PLATFORM-EVALUATION-SYSTEM** `2606.28385` *RoboGaze*，正文已区分视觉逼真、物理/时序/任务约束与 learned judge authority。原块把三类机制挤进 World Model owner，owner 不成立。 | 删除块；必要 Review note 按正确 owner 保留/消费，不新增 World Model 正文。 |
| `MULTIMODAL-EMBODIED-VLA` | **A** `2606.22794` *UniFS*，fast/slow freshness 与 control cadence 已覆盖；**B→MULTIMODAL-EMBODIED-VLA** `2606.23589` *KEMO*，event-triggered keyframe retention 尚无正文 owner；**A** `2606.23617` *RECALL*，uncertainty-triggered recovery、continual adapter/replay frontier 已覆盖；**A** `2606.23686` *LIBERO-Safety*，procedural safety scenarios、physical/semantic slices 与 controller gate 已覆盖。 | 先合并 KEMO proposal，再删除整块。 |
| `TRAIN-DATA` | **A** `2606.22883` *CLI-Universe*，environment/task/verifier/data lineage 已覆盖；**A** `2606.28386` *Data Provenance for Image AR Generation*，sample/transform/derivative lineage 与 publish gate 已覆盖。 | 删除块。 |
| `TRAIN-LORA` | **A** `2606.22878` *Priority-Aware Learning-Unlearning Correction...*；正文已拥有 contribution identity、动态参与者、unlearning correction 与 adapter lifecycle。 | 删除块。 |
| `TRAIN-RLHF` | **A** `2606.23038` *EvoRubrics*；**A** `2606.24004` *Specification Learning*；rubric/spec revision、judge/evidence 分权与发布 gate 已在 RLHF/Evaluation 正文成立。 | 删除块。 |
| `TRAIN-DISTRIBUTED-TRAINING` | **A** `2606.22768` *Factored Gossip DiLoCo*，gossip/staleness/consensus/recovery 已覆盖；**B** `2606.22932` *FORGE*，backward 内消费 gradient、避免全量 materialization 的机制尚未展开；**C** `2606.23017` *Nautilus*，核心是 vehicular-edge-cloud federated scheduling/verification，title/abstract 未形成大模型训练特有贡献。 | 合并 FORGE 后删除块；Nautilus 撤销 Books Integrate。 |
| `INFER-PREFILL` | **A** `2606.22968` *MOCAP*；chunked prefill、memory hierarchy、admission 与 exactness 已覆盖。 | 删除块。 |
| `INFER-DECODE` | **A** `2606.23521` *Concordia*；persistent decode kernel 的 checkpoint/恢复、commit boundary 与 fallback 已覆盖。 | 删除块。 |
| `INFER-KV-CACHE` | **A** `2606.23581` *Kamera*；**A** `2606.23961` *Nexus Sampling*；**A** `2606.24033` *RoPE-Aware Bit Allocation*；正文已覆盖 semantic/position-aware eviction、sampling/retention 分权、RoPE 与分层 bit budget。 | 删除块。 |
| `INFER-SPECULATIVE-DECODING` | **A** `2606.22840` *RLM-Cascade*；response cascade、稀疏目标、acceptance 与 fallback 已覆盖。 | 删除块。 |
| `INFER-SCHEDULING` | **A** `2606.22983` *LiveServe*；**A** `2606.23181` *DART*；**A** `2606.23370` *FlexServe*；phase/workload/SLO-aware routing、抢占与保守路径已覆盖。 | 删除块。 |
| `PLATFORM-MODEL-REGISTRY` | **A** `2606.22875` *FedOT*；model ownership、watermark/provenance、client identity 与 leakage trace 已由 registry/security 边界覆盖，具体 watermark 不构成新主线。 | 删除块。 |
| `PLATFORM-EVALUATION-SYSTEM` | **B** `2606.22783` *VERITAS*；**B** `2606.22826` *MINCE*；正文分别缺少“无完整 ground truth 的约束可验收遍历”和“先校准子集误差预算再冻结随机子集”两条机制。 | 两项合并后删除块。 |
| `PLATFORM-COST` | **A** `2606.23546` *The Energy Consumption of Transformer Fine-Tuning...*；正文已有 hardware/parallelism/utilization/quality 联合的 roofline-style cost contract 与实测回校。 | 删除块。 |
| `PLATFORM-SECURITY` | **C** `2606.22827` *Runtime SBOM Generation*，贡献是通用 Python memory-forensics/SBOM，不是大模型或大模型基础设施特有机制；**A** `2606.22873` *SingGuard*；**A** `2606.22916` *Intent-Governed...*；**A** `2606.23003` *VCT*；**A** `2606.23277` *GIF*；**A** `2606.23416` *Malicious Agent Skills...*；**A** `2606.23969` *Blackwell Confidential Computing*；后六项的 trust boundary、intent/effect authorization、prompt/tool/memory provenance、TEE/attestation 非充分性均已有正文。 | 删除块；MEM-SBOM 撤销 Books Integrate。 |
| `AGENT-CONTEXT` | **A** `2606.22906` *From Fragments to Paths*；**A** `2606.22953` *Plans Don't Persist*；task-level context reconstruction、plan/commitment persistence 与 compaction failure 已覆盖。 | 删除块。 |
| `AGENT-RAG` | **A** `2606.22778` *HAKARI*；**A** `2606.23642` *Multi-Prefix Embedding*；retrieval proposal/acceptance、prefix identity、index budget 与 fallback 已覆盖。 | 删除块。 |
| `AGENT-MEMORY` | **A** `2606.22844` *RaMem*；`2606.23195` *Memory Contagion*；`2606.23283` *RootMem*；`2606.23525` *Self-Compacting Memory*；`2606.23752` *ESAA*；`2606.24040` *Version-aware Transaction Memories*；正文已覆盖 read/write authority、provenance、contagion、compaction、version/transaction 与回滚。 | 删除块。 |
| `AGENT-TOOL-CALLING` | **A** `2606.23049` *PhoneBuddy*，tool/GUI state、handoff 与 completion receipt 已覆盖；**B→TRAIN-DPO** `2606.23112` *Divergence-point Preference Learning*，这是 preference-pair construction，不应由 Tool Calling 持有；**A** `2606.24551` *GUI vs CLI*，tool surface、typed result 与 environment contract 已覆盖。 | 将 `23112` 合并到 Ch34 后删除块。 |
| `AGENT-PLANNING` | **A** `2606.22948` *ENVS*；动态环境扰动、replan、恢复证据与 benchmark identity 已覆盖。 | 删除块。 |
| `AGENT-WORKFLOW` | **A** `2606.22741` *GRADE*；**A** `2606.23797` *GODR*；workflow graph、stage verifier、artifact/commit 与 fallback 已覆盖。 | 删除块。 |
| `AGENT-PLATFORM` | **A** `2606.22902` *Agent-as-Router*；**C** `2606.23321` *Tmax*，是 terminal-agent data/model/RL recipe 与 benchmark baseline，不是 Agent Platform 长期机制；**A** `2606.23449` *AOHP*；**A** `2606.23983` *Maestro Order*；后两项的 harness/experiment orchestration、stateful control plane 与证据边界已覆盖。 | 删除块；Tmax 撤销 Books Integrate。 |

### recovered-daily-20260624（19 blocks / 42 families）

| 后置块 | Source Family 逐项结论 | 块级处置 |
| --- | --- | --- |
| `MODEL-LONG-CONTEXT` | **A** `2606.25156` *ATMA*；parametric/recurrent state、selector 与 dense fallback 已覆盖。 | 删除块。 |
| `MULTIMODAL-EMBODIED-VLA` | **A** `2606.25215` *Reflective VLA*；proposal/critic/controller 分权、反思反馈与物理 commit gate 已覆盖。 | 删除块。 |
| `TRAIN-DATA` | **A** `2606.24133` *HDS*；**A** `2606.24998` *Repetition Destroys Language Models*；mixture/duplication/retention 与 compute-to-unique-data regime 已覆盖。 | 删除块。 |
| `TRAIN-GRPO` | **A** `2606.25178` *Transfer-aware Curriculum*；curriculum、policy-relative difficulty、collapse 与 supervisor repair 已覆盖。 | 删除块。 |
| `TRAIN-DISTRIBUTED-TRAINING` | **A** `2606.24143` *AsyncOPD*；bounded staleness、queue/cache identity 与同步 fallback 已覆盖；**B** `2606.24722` *BlockTrain*，独立 block-local objective、组装式模型与端到端 credit-assignment 损失尚未进入正文。 | 合并 BlockTrain 后删除块。 |
| `INFER-KV-CACHE` | **A** `2606.24467` *CompressKV*；分层压缩、query/position sensitivity 与 full-cache fallback 已覆盖。 | 删除块。 |
| `INFER-SPECULATIVE-DECODING` | **A** `2606.24957` *Dustin*；`2606.25091` *Edge-cloud Speculative Decoding*；`2606.25097` *Temperature-zero Safety*；draft/target acceptance、边云状态与 deterministic edge case 已覆盖。 | 删除块。 |
| `INFER-GPU-MEMORY` | **A** `2606.24506` *CrossPool*；weights/KV/activation tiering、lease/ownership 与 fallback 已覆盖。 | 删除块。 |
| `INFER-SCHEDULING` | **A** `2606.25040` *Chorus II*；multimodal generation 的 phase/state scheduling 与端到端 SLO 已覆盖。 | 删除块。 |
| `PLATFORM-GPU-SCHEDULER` | **A** `2606.25082` *Dynamic MIG Repartitioning*；**A** `2606.25098` *Power-flex AI Datacenters*；MIG slice、repartition cost、power cap/grid signal 与 SLO guard 已覆盖。 | 删除块。 |
| `PLATFORM-EVALUATION-SYSTEM` | **A** `2606.24074` *Token Complexity of Certifying Stochastic-Oracle Reliability*；`2606.24081` *PixJail*；`2606.24124` *VeryTrace*；`2606.24996` *Fail-closed Leaderboard*；顺序检验、attack/evaluator identity、typed trace 与 release gate 已覆盖。 | 删除块。 |
| `PLATFORM-MONITORING` | **A** `2606.24119` *LoRA Monitor for MDLMs*；短程 probe、family calibration、abstain 与 loss/SLO fallback 已覆盖。 | 删除块。 |
| `PLATFORM-TRACE` | **A** `2606.24626` *SAFARI*；event/claim/trace provenance、sampling 与因果非充分性已覆盖。 | 删除块。 |
| `PLATFORM-SECURITY` | **A** `2606.24245` *AutoSpec*；`2606.24322` *Origin-bound Memory*；`2606.24402` *Poisoned Playbooks*；`2606.24408` *Natural Identifiers*；`2606.24774` *VLM Gradient Data Exposure*；`2606.25189` *ActPlane*；policy compilation、memory/tool provenance、data exposure 与 action-plane authorization 已覆盖。 | 删除块。 |
| `AGENT-RAG` | **C** `2606.24204` *Unified Dominance Graph for Interval-Predicate ANN*，核心贡献是通用 ANN 数据结构，RAG 只是应用例；**A** `2606.25191` *Multi-agent RAG*，reasoning-score coupling 与 isolation fallback 已覆盖；**A** `2606.28387` *Schema-First Retrieval*，typed retrieval operator、catalog/source lineage、ACL-before-retrieval 与 rerank 已覆盖。 | 删除块；UDG 撤销 Books Integrate。 |
| `AGENT-MEMORY` | **A** `2606.24151` *Metis*；`2606.24428` *Execute-Distill-Verify*；`2606.24535` *Governed Shared Memory*；`2606.24775` *Agent-native Memory*；`2606.25115` *Budget-curated Memory*；`2606.25161` *TRUSTMEM*；正文已拥有 typed memory、shared authority、curation budget、verification 与 rollback。 | 删除块。 |
| `AGENT-WORKFLOW` | **A** `2606.24177` *Agon*；`2606.25198` *Heuresis*；`2606.25207` *Auto HPO*；workflow state、verifier、experiment budget 与 promotion 已覆盖。 | 删除块。 |
| `AGENT-MULTI-AGENT` | **A** `2606.24437` *ReM-MoA*；**A** `2606.26156` *Kiko*；role/topology、shared state、coordination cost、disagreement 与 single-agent fallback 已覆盖。 | 删除块。 |
| `AGENT-PLATFORM` | **A** `2606.24311` *LemonHarness*；harness/runtime identity、tool/environment isolation 与 replay 已覆盖。 | 删除块。 |

### recovered-daily-20260625（25 blocks / 63 families）

| 后置块 | Source Family 逐项结论 | 块级处置 |
| --- | --- | --- |
| `MODEL-LONG-CONTEXT` | **A** `2606.25342` *Lifelong Parametric Attention*；persistent/recurrent state、write admission、drift 与 fallback 已覆盖。 | 删除块。 |
| `MULTIMODAL-EMBODIED-VLA` | **A** `2606.25575` *Variable-autonomy Robot Hand*；human takeover、controller authority 与 safety envelope 已覆盖。 | 删除块。 |
| `TRAIN-DATA` | **C** `2606.25388` *TabClean*，主要是表格清洗垂直应用；**C** `2606.25871` *AutoRelAnnotator*，主要是 sponsored-search 标注业务；**A** `2606.25996` *Autodata*，数据生成/过滤/lineage/admission 已覆盖。 | 删除块；前两项撤销 Books Integrate。 |
| `TRAIN-GRPO` | **A** `2606.26027` *Tool-use RL Collapse*；policy-relative curriculum、collapse diagnosis 与 fallback 已覆盖。 | 删除块。 |
| `TRAIN-DISTRIBUTED-TRAINING` | **A** `2606.25759` *NEURON-Fabric*；typed communication、topology/transport plan、completion 与 fallback 已覆盖。 | 删除块。 |
| `INFER-REQUEST-LIFECYCLE` | **A** `2606.25838` *Blur Gate V-L Pipeline*；request-level routing confidence 只拥有 proposal，canonical backend/fallback 已覆盖。 | 删除块。 |
| `INFER-PREFILL` | **A** `2606.25353` *Cache-resident L3*；**A** `2606.25426` *M1 AMX Prefill GEMM*；shape-resolved GEMM、weight prepack、hardware identity、bit exactness 与端到端验收均已有正文抽象。 | 删除块。 |
| `INFER-KV-CACHE` | **A** `2606.26472` *Epiphany Eviction*；eviction proposal、query-sensitive value、state identity 与 full-cache fallback 已覆盖。 | 删除块。 |
| `INFER-TENSORRT-LLM` | **C** `2606.25453` *EmuGEMM*，目标是科学计算高精度 GEMM 仿真，不是大模型系统；**A** `2606.26344` *Axon*；**A** `2606.26453` *KernelPro*；tensor compiler、generated kernel、differential correctness 与 promotion gate 已覆盖。 | 删除块；EmuGEMM 撤销 Books Integrate。 |
| `INFER-GPU-MEMORY` | **A** `2606.25285` *EPTS*；`2606.25519` *Token Inflation*；`2606.26488` *Recursive Reasoner Compression*；正文已覆盖 state lifetime、token/KV inflation、compression/error feedback 与容量 fallback。 | 删除块。 |
| `INFER-SCHEDULING` | **C** `2606.25467` *RQ-SAFE Edge SFC-DAG*；贡献是通用 VNF/SFC 边缘编排，未形成大模型 inference 特有机制。 | 删除块并撤销 Books Integrate。 |
| `PLATFORM-FOUNDATIONS` | **C** `2606.25532` *Agentic Evolution of Physically Constrained Foundation Models*；主要 claim 是 AI-for-Science/agentic discovery engine，压缩案例不足以把该垂直路线提升为 Platform Foundations 正文。 | 删除块并撤销 Books Integrate；可留 Weekly context。 |
| `PLATFORM-GPU-SCHEDULER` | **C** `2606.26341` *Many Problems One GPU*；是机器人 nonlinear-program solver batching，不是大模型 GPU scheduler。 | 删除块并撤销 Books Integrate。 |
| `PLATFORM-EVALUATION-SYSTEM` | **A** `2606.25487` *Jailbreak Judge*；**C** `2606.25622` *German IT-Grundschutz Audit*，垂直合规应用；**A** `2606.25760` *GUI Uncertainty*；`2606.25782` *Encoder/Decoder Judge*；`2606.26071` *Model Forensics*；`2606.26185` *Temperature/Reproducibility*；`2606.26300` *Verification Horizon*；`2606.26429` *DualEval*；**C** `2606.26456` *Autonomous-driving Mutation Testing*，垂直 ADS vision paper；**C** `2606.26492` *DL Program Fault Diagnosis*，generic DL diagnosis benchmark，未满足 large-model contribution gate。其余七项的 judge calibration、uncertainty、execution identity、verification horizon 与 release gate 已覆盖。 | 删除块；三项 C 撤销 Books Integrate。 |
| `PLATFORM-MONITORING` | **A** `2606.26383` *SOLAR*；speed-of-light upper bound、calibration、observed gap 与 direct-profile fallback 已覆盖。 | 删除块。 |
| `PLATFORM-TRACE` | **A** `2606.26449` *ProvenAI*；claim/evidence/lineage/attestation authority 已覆盖。 | 删除块。 |
| `PLATFORM-SECURITY` | **C** `2606.25296` *SafeGen*，汽车 functional-safety assertion 应用；**A** `2606.25349` *FHE Transformer*；**C** `2606.25366` *Spacecraft Autonomy*；**C** `2606.25371` *Recovery-deadline Certificates for Controllers*；**A** `2606.25592` *I2V Visual Prompt Attack*；**A** `2606.25721` *Poisoned RAG*；**C** `2606.25863` *PatchLens*，通用 C/C++ patch/config security；**C** `2606.26021` *Tabular Foundation Model Privacy*，不属 large-language/multimodal-model主线；**A** `2606.26028` *Decentralized Agents*；`2606.26057` *Safety Kernel*；`2606.26257` *Dataset Usage Inference*；`2606.26298` *Institutional Attestation*；`2606.26377` *Prompt + Response Harm*；`2606.26479` *Prompt-injection Defense Eval*。A 项的 provenance、confidential execution、RAG/tool/prompt threat boundary、effect authorization 与 evidence gate 已覆盖。 | 删除块；五项 C 撤销 Books Integrate。 |
| `AGENT-PROMPT` | **A** `2606.26356` *Instruction Bleed*；instruction/source boundary、context propagation、prompt/tool authority 与 isolation 已覆盖。 | 删除块。 |
| `AGENT-RAG` | **A** `2606.25656` *When Is GraphRAG Needed?*；`2606.25674` *BitNet Text Embeddings*；`2606.26439` *TileMaxSim*；`2606.26441` *GPUSparse*；representation/index/operator identity、storage/precision budget、late interaction 与 sparse fallback 已覆盖。 | 删除块。 |
| `AGENT-MEMORY` | **A** `2606.25449` *Reclaim*；**A→MODEL-LONG-CONTEXT** `2606.25658` *Dynamic Fixed-budget Memory for Streaming Video*；后者是 MLLM streaming context，不是 Agent memory，正文已有 fixed-budget selection/recurrent state/dense fallback。 | 删除块；`25658` 的 Review note 不应继续宣称 AGENT-MEMORY 正文 owner。 |
| `AGENT-TOOL-CALLING` | **A** `2606.25605` *Structured Output Suppresses Tools*；`2606.25705` *User-sensitive GUI Screens*；`2606.25819` *Unreliable Tool Environments*；`2606.25987` *Weave Formal Thought*；tool schema/availability、handover、environment failure 与 deterministic verifier 已覆盖。 | 删除块。 |
| `AGENT-PLANNING` | **C** `2606.25274` *Delayed Time-series Control*；**C** `2606.26463` *Real-time RL Games*；两者是通用 control/RL 机制，title/abstract 未形成 LLM Agent planning 的直接贡献。 | 删除块并撤销 Books Integrate。 |
| `AGENT-WORKFLOW` | **A** `2606.25447` *Harness Design*；**C** `2606.26442` *AXLE Lean 4 Cloud*，是 AI-for-mathematics 垂直基础设施；通用 isolation/version/tooling 已有覆盖。 | 删除块；AXLE 撤销 Books Integrate，可留 Weekly context。 |
| `AGENT-MULTI-AGENT` | **A** `2606.25514` *Adaptive Issue Resolution*；coordination topology、role/state ownership、escalation 与 single-agent fallback 已覆盖。 | 删除块。 |
| `AGENT-MCP` | **A** `2606.26211` *Data Facts*；typed resource/tool result、provenance、authorization 与 host-side validation 已覆盖。 | 删除块。 |

### daily-20260627（11 blocks / 14 families）

这些 family 的 canonical first-public owner 实际属于后续 06-29/30 批次；当前 06-27 报告为零候选。下表仍对残留块的语义作独立判断，但 `daily-20260627:*` 标签本身是错误 provenance，不能留下。

| 后置块 | Source Family 逐项结论 | 块级处置 |
| --- | --- | --- |
| `MULTIMODAL-GENERATIVE-PARADIGMS` | **A** `2606.27732` *Bifocal / R2LM*；正文现已在 conditional branch 写明 asymmetric bidirectional sidecar、causal cache、代价与 AR/full-bidirectional fallback。 | 删除块。 |
| `MULTIMODAL-WORLD-MODELS` | **B** `2606.27681` *Textual Belief under Strict Mediation*；现有“可规划表示的可识别条件”不等于禁止 predictor 绕过 belief 重读 history，strict mediation 仍是缺失机制。 | 合并到 Ch25 后删除块。 |
| `MULTIMODAL-EMBODIED-VLA` | **A** `2606.28276` *SimFoundry*；正文已版本化 generated environment、scene/task/seed/policy lineage，并明确 simulation coverage 不拥有 sim-to-real authority。 | 删除块。 |
| `TRAIN-LORA` | **A** `2606.28479` *Privacy Fine-tuning with Matched Controls*；正文已保存 matched-update controls，把 DP guarantee、pseudonymization 与 optimizer-step memorization effect 分开；章内 Evaluation/Review note 保留 empirical attack 非证明边界。 | 删除块。 |
| `TRAIN-DISTRIBUTED-TRAINING` | **A** `2606.27797` *Teacher-Student Partitioning*；本轮 post-write 正文已通过，详见末节。 | 删除块。 |
| `INFER-REQUEST-LIFECYCLE` | **A** `2606.27906` *Phase Matters*；`2606.28529` *Speedup Paradox*；`2606.28565` *KernelSight*；正文已拥有 request phase、component vs E2E/task success、hardware/workload identity 与实测 promotion。 | 删除块。 |
| `PLATFORM-EVALUATION-SYSTEM` | **A** `2606.28013` *Signal-Coverage Formalization*；type acceptance、semantic equivalence、unknown 与 independent verification 已覆盖；**A** `2606.28661` *Modal/Correlation Ceiling*，本轮 post-write 正文已通过。 | 删除块。 |
| `PLATFORM-MONITORING` | **A** `2606.28116` *Mechanism-Driven Monitors*；正文已把 attention/router/update statistics 放在 calibrated sensor、abstain、checkpoint/rollback 与 SLO 框架内。 | 删除块。 |
| `PLATFORM-COST` | **A** `2606.27841` *WattLayer*；正文已有 layer-wise measurement contract，且相邻 roofline/whole-run 校准段给出 fusion、hardware、utilization 与 fallback 边界。 | 删除块。 |
| `PLATFORM-SECURITY` | **A** `2606.28649` *RIPA / ROS 2*；正文已覆盖 embodied sensor→middleware→prompt provenance、cross-modal validation 与 controller-side fail-closed authority。 | 删除块。 |
| `AGENT-PLANNING` | **A** `2606.27806` *Hybrid-WM*；本轮 post-write 正文已通过，详见末节。 | 删除块。 |

### daily-20260628（6 blocks / 6 families）

这些 family 的 canonical first-public owner 为 06-30；当前 06-28 报告为零候选。`daily-20260628:*` 是错误 provenance。

| 后置块 | Source Family 逐项结论 | 块级处置 |
| --- | --- | --- |
| `AGENT-MCP` | **A** `2606.28690` *Formal Security Analysis of Agent Protocol Composition*；正文现已写入 finite-state IR、source/type evidence、pairwise composition/trace replay 与 isolation fallback。 | 删除块。 |
| `INFER-DECODE` | **B** `2606.29066` *x-Prediction Flow*；token-mixture state 跨 masked-diffusion step 保留、异步 progress 与 visible commit frontier 尚只在后置块。 | 合并到 Ch44 后删除块。 |
| `MULTIMODAL-EMBODIED-VLA` | **C** `2606.28995` *HJ-SafeDMP*；title/abstract 是 HJ/CBVF + DMP 的机器人 controller 安全方法，不包含大模型/VLA 机制；不能因被路由到 VLA 就取得准入。 | 删除块并撤销 Books Integrate。 |
| `PLATFORM-EVALUATION-SYSTEM` | **B** `2606.29038` *Metric Aggregation Divergence*；optimizer/evaluator/champion selector 共享同一 callable aggregation contract 的机制尚只在后置块。 | 合并到 Ch66 后删除块。 |
| `TRAIN-DATA` | **B** `2606.28772` *Majority Vote Silences Minority Values*；per-annotator distribution、aggregation revision 与 contested boundary 尚只在后置块。 | 合并到 Ch27 后删除块。 |
| `TRAIN-RLHF` | **B** `2606.28955` *Modification-Considering Value Learning*；equal-budget cloned-policy counterfactual 作为 transition-admission gate 尚只在后置块。 | 合并到 Ch31 后删除块。 |

## B 类合并提案（11 families）

### B1 — `2606.23589` KEMO

- Canonical owner：`MULTIMODAL-EMBODIED-VLA`，`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。
- 建议 heading/位置：在 `## State ownership 与 freshness` 中，接在“Policy 内部的 Latent Memory 是 Episode State，不是 Agent Memory”之后，新增 `### Event 是 VLA 长时记忆的保留边界`。
- 合并论证：固定短窗口便宜且 freshness 清楚，却会遗失早期任务转折；保存全部视觉历史保留 recall，却使 token/memory 成本随 episode 增长。VLA 可以让 event detector 只对有任务意义的状态变化提交 keyframe，并把 observation/action/task-phase/timestamp、detector revision 与原始帧 locator 绑定成 episode memory；短 recent window 仍负责连续接触与瞬态细节。代价是 event miss 会永久丢失渐变或接触信号，false positive 会重新造成膨胀，旧 keyframe 也可能在新 observation 后失效；高风险动作、detector 未校准或状态快速变化时回退密集 recent context/原始轨迹与 controller observation。exact-v1 只支持披露的 2～6 subtask、830～2846-step 双臂任务，不给跨 embodiment 保证。

### B2 — `2606.22932` FORGE

- Canonical owner：`TRAIN-DISTRIBUTED-TRAINING`，`books/part-04-training-system/36-distributed-training.md`。
- 建议 heading/位置：接在 `### 从 Layer Collective 到 Minibatch Commit` 后，新增 `### Gradient 不必在 Backward 与 Optimizer 之间完整物化`。
- 合并论证：传统 reverse-mode 先把每层 weight gradient 写入全局内存，再由 optimizer 读回；它让 backward/optimizer 分工清楚，却在二者交界使大量 gradient 同时存活。条件允许时，可在 backward 产生 gradient 时由 fused optimizer path 立即消费、更新并释放，register/on-chip state 只拥有本层临时值，optimizer/step coordinator 仍拥有全局 step commit；TP shard、overflow、clipping、accumulation 与 checkpoint identity 必须共同版本化。收益是降低 gradient materialization 与 memory traffic，代价是 optimizer 支持面、kernel fusion、debuggability 和累积/低精度顺序更复杂；需要完整 gradient inspection、非兼容 optimizer、数值分歧或 recovery 无法复现时，回退 materialized-gradient 两阶段基线。作者的内存/速度结果只绑定披露 optimizer、batch、GPU 与 Megatron 路径。

### B3 — `2606.22783` VERITAS

- Canonical owner：`PLATFORM-EVALUATION-SYSTEM`，`books/part-06-ai-infrastructure/66-evaluation-system.md`。
- 建议 heading/位置：接在 `### 验证“没有遗漏”必须先建立应出现事实的 Inventory` 后，新增 `### 没有完整 Ground Truth 时，用不可优化约束验收遍历`。
- 合并论证：高熵枚举任务若依赖人工列出全部答案，验证成本与生成完整 ground truth 同阶；只检查少量已知答案又无法证明 completeness。可把任务构造成具有独立、可机械检查的不可约约束：generator 提交候选遍历与顺序/覆盖证据，deterministic verifier 只判断每项合法性、重复、约束违反与停止条件，而不把候选模型或 judge 变成 truth owner。它把“造完整答案集”换成“造可检查约束”，但只适用于可形式化、verifier 独立且约束不会泄漏捷径的任务；约束不完备、候选空间被人为缩窄或 verifier 成为训练目标时，应保持 inconclusive，回到人工 anchor、完整小规模实例与多种任务证据。

### B4 — `2606.22826` MINCE

- Canonical owner：`PLATFORM-EVALUATION-SYSTEM`。
- 建议 heading/位置：接在 `## 部分评测必须预先声明停止与淘汰状态` 后，新增 `### 子集大小必须先用误差预算校准，再冻结样本`。
- 合并论证：每个 model revision 运行完整 benchmark 最容易比较，却会在量化/微调/部署变体增多后重复支付大量成本；按难度挑“代表题”又容易把 selector 偏差写入分数。先用少量 calibration models 的 per-item log 做 Monte Carlo，寻找满足声明 accuracy-drift/error budget 的最小样本数，再从冻结总体中随机抽取一次并版本化，可将 subset size 的选择与待评模型分开。代价是保证只相对于 calibration roster、metric 与分布，模型族漂移或 slice/rare failure 未覆盖时误差会放大；高风险 release、超出校准域或阈值敏感时恢复完整 benchmark/关键 slice，不能把 compact subset 当成新真值。

### B5 — `2606.23112` Divergence-point Preference Learning

- Canonical owner：`TRAIN-DPO`，`books/part-04-training-system/34-dpo.md`；不是 `AGENT-TOOL-CALLING`。
- 建议 heading/位置：接在 `## DPO 保留了什么难题` 后，新增 `### Preference Pair 应截断到最早可归因分歧点`。
- 合并论证：用完整成功/失败 trajectory 构造 chosen/rejected pair 最简单，却让相同 prefix、失败后的补救与多次 tool effect 同时进入 sequence-level preference，credit 无法定位。若 replay/effect log 能找到双方最早可归因 divergence，可冻结共同 prefix，只比较从该 state 出发的候选 action/suffix，并把 environment revision、tool result、judge/label 与 divergence locator 写入 pair identity；DPO 仍只消费离线 pair，不拥有环境真值。更局部的 pair 降低无关 token 与错误 credit，却依赖可重放状态和可靠 attribution；多因交互、隐藏副作用或 divergence 不确定时保留完整 trajectory、降权/拒收该 pair，或回到 online evaluator/人工裁决。

### B6 — `2606.24722` BlockTrain

- Canonical owner：`TRAIN-DISTRIBUTED-TRAINING`。
- 建议 heading/位置：接在 `### Federated Tensor Type 定义一轮协议能表达什么` 后，新增 `### Block-local Training 用全局 Credit Assignment 换去中心化 State`。
- 合并论证：端到端 backprop 保留跨层 credit assignment，却要求 worker 同时持有全模型 activation/optimizer state 并持续同步。Block-local 路线把模型切为可独立训练的 blocks，各 worker 只对共享目标派生的 local objective 更新自己负责的 block，publisher 再按 block revision 组装可推理模型；block identity、邻接接口、目标版本与 assembly gate 必须显式。它减少单 worker state 并允许低带宽/异步协作，却牺牲端到端梯度和跨 block 协同，组装版本不一致还可能产生局部都收敛、整体失效；acceptance 失败时回退同步端到端训练或冻结部分 blocks。exact-v1 的 small real-text、virtual workers、WAN smoke test 与 logical 75.8B inference shape 不证明 frontier-scale 收敛、Byzantine robustness 或生产 serving。

### B7 — `2606.27681` Strictly Mediated Textual Belief

- Canonical owner：`MULTIMODAL-WORLD-MODELS`，`books/part-03-multimodal-world-models/25-multimodal-world-models.md`。
- 建议 heading/位置：接在 `## State ownership` 的 owner 列表后，新增 `### 可识别 Belief 必须成为唯一受控预测输入`。
- 合并论证：让 predictor 同时读取声明的 belief 与原始 history，短期更准确，也能在 belief 丢信息时自救；但模型可完全绕过 belief，重建/预测成功便无法证明该 state 接口对 planner 有用。需要审计 state representation 时，应让版本化 belief 成为 transition/prediction path 的唯一受控输入，并用下游 query/action/transition recovery 验收其 sufficiency；原始 observation/history 仍由 ingestion 持有，只能经显式 correction 产生新 belief。Strict mediation 会放大有损 textual state、增加训练难度并可能降低性能；无需可识别接口、任务低风险或 belief capacity 不足时，直接 latent/history access 仍是合理分支，失败时回退原始 observation 与非线性 belief store。

### B8 — `2606.29066` x-Prediction Flow

- Canonical owner：`INFER-DECODE`，`books/part-05-inference-system/44-decode.md`。
- 建议 heading/位置：接在 masked-diffusion decode 的 request-local state 讨论后、`## Decode 的结束条件` 前，新增 `### Continuous Mixture 在 Commit 前可以跨 Step 延续`。
- 合并论证：标准 mask/unmask decode 每步把位置压成离散 token 或 mask，状态简单且 kernel 友好，却丢掉本轮对多个 token 的连续置信结构。Request 可为每个位置保存 versioned x-prediction mixture、异步 progress 与 bounded re-edit state，step policy 只提交通过 commit rule 的离散 token 到 visible frontier；cache 与 sampler 必须绑定 mixture revision。它减少重复丢失 refinement information，却增加 request memory、pretrained-model alignment、kernel 与 termination complexity；作者只在两组模型/代码任务中验证。质量下降、mixture 解释不稳定或硬件不支持时回退标准 mask/unmask decoder 与 full refresh。

### B9 — `2606.29038` Metric Aggregation Divergence

- Canonical owner：`PLATFORM-EVALUATION-SYSTEM`。
- 建议 heading/位置：接在 `## Evaluation Run 的平台对象模型` 对象 schema 后，新增 `### Metric Aggregation 必须作为可调用 Contract 复用`。
- 合并论证：optimizer、离线 evaluator 与 champion selector 各自重写同名 outcome metric，在单一实现时便宜，却会因 extraction、missing value、normalization 或 aggregation 顺序不同而发生 selection inversion。Evaluation owner 应发布版本化 callable metric artifact，使三阶段消费同一 raw-trajectory extraction 与 aggregation code，并保存 contract revision、inputs 与可重算 verdict；selector 只消费结果，不重新解释指标。统一实现增加迁移、依赖与历史重算成本，也不能修复错误目标或缺失 trajectory；schema/semantic 不兼容时 release Gate 保持 Open，用旧 revision 对 raw evidence 重算并并列新旧结果。

### B10 — `2606.28772` Annotator Disagreement

- Canonical owner：`TRAIN-DATA`，`books/part-04-training-system/27-data.md`。
- 建议 heading/位置：接在 label/provenance 讨论后、`### 从 Sample Dedup 到 Typed Lineage Graph` 前，新增 `### Majority Label 只能是可重建视图，不能抹去 Annotator 分歧`。
- 合并论证：majority vote 把多标注压成单 label，训练接口简单，却会在 hate/offensive 等价值边界把 minority judgement 静默改写为真值。Data owner 应保存 per-annotator label、annotator/threshold identity、disagreement 与 aggregation revision；majority/soft label 只是由原始标注 materialize 的训练视图，evaluation 与 policy review 必须能恢复 contested boundary。多视图增加存储、训练与治理成本，三位标注者和单一 HateXplain/BERT slice 也不能区分稳定价值差异与噪声；高分歧时保留多视图/转人工，低风险一致样本仍可使用多数聚合。

### B11 — `2606.28955` Reward-hacking Transition Admission

- Canonical owner：`TRAIN-RLHF`，`books/part-04-training-system/31-rlhf.md`。
- 建议 heading/位置：接在 `## Reward hacking 与 Goodhart's Law` 后，新增 `### Reward-hacking 防线应前移到 Transition Admission`。
- 合并论证：只在训练结束后比较 return 容易发现 hacking 太晚；直接让同一个 policy/reward 提交 environment/replay 修改又会把 proposal 与 gate 合并。可在提交 transition 前冻结 current policy、candidate modified policy、seed/state 与 return evaluator，执行 equal-budget counterfactual forecast；只有独立 evaluator 接受，修改才进入 environment/replay，原始 true-objective evidence 保留为 authority。它能前移拦截，却依赖 evaluator 已能把 hacking trajectory 排低、clean seed 可复现，并引入论文披露约 1.8×–4.2× 额外成本；evaluator misspecification、长程副作用或不可回滚环境下回退人工/真实目标审阅，不把 forecast 当作安全证明。

## C 类 removal / de-admit 清单（22 families）

- 通用非大模型系统：`2606.23017` Nautilus、`2606.22827` runtime SBOM、`2606.24204` interval-predicate ANN、`2606.25453` EmuGEMM、`2606.25467` edge SFC-DAG、`2606.26341` batched robotics NLP solver、`2606.25371` controller recovery certificate、`2606.25863` PatchLens、`2606.26492` generic DL fault diagnosis、`2606.25274` time-series control、`2606.26463` real-time RL games、`2606.28995` HJ/CBVF-DMP robot control。它们可作为邻域阅读，不满足大模型/大模型基础设施的直接贡献门槛。
- 垂直应用或 AI-for-Science：`2606.25388` TabClean、`2606.25871` sponsored-search annotation、`2606.25532` agentic scientific discovery、`2606.25622` German IT-Grundschutz audit、`2606.26456` autonomous-driving mutation testing、`2606.25296` automotive functional safety、`2606.25366` spacecraft autonomy、`2606.26021` tabular foundation-model privacy、`2606.26442` Lean 4 cloud。可保留 Weekly context；不得因能映射某章而成为 Books 正文。
- 局部 recipe/benchmark：`2606.23321` Tmax。数据集、训练 recipe 与 benchmark baseline 可在 Report 中保留，但没有形成 Agent Platform 独有且可迁移的长期机制。

## 报告 reopen / closure 影响

| 日期 | 当前报告状态与本审计影响 | 结论 |
| --- | --- | --- |
| 2026-06-23 | README 已声明旧 `44 Integrate / 6 Existing` 中有后置伪正文并保持进行中。本审计在其相关残留中判定 5 个 B、3 个 C。 | **保持 reopen**：完成 5 个正文合并、3 个 Books de-admit，并将其余 A 改为 Existing Coverage 后才能 Complete。 |
| 2026-06-24 | README 已保持进行中；相关残留中 1 个 B、1 个 C。 | **保持 reopen**：完成 BlockTrain 合并、UDG de-admit，其余 A 回写为 Existing Coverage。 |
| 2026-06-25 | README 已保持进行中；相关残留无 B、17 个 C。 | **保持 reopen**：无需搬正文；删除伪正文、撤销 17 个 Books Integrate，并把 46 个 A 纠正为 Existing Coverage 后再独立复核。 |
| 2026-06-27 | 当前 README 为 canonical owner 0、候选 0、无 Books 对象；残留 `daily-20260627` 实为 06-29/30 family 的错误标签。 | **06-27 报告本身不需因语义重开**；删除错误 provenance block 即可。B `2606.27681` 的真实 owner 报告应在其 canonical 日期闭环。 |
| 2026-06-28 | 当前 README 同样为 0 候选；残留 `daily-20260628` 实为 06-30 family。 | **06-28 报告本身不需因语义重开**；删除错误 provenance block。四个 B 与一个 C 应在 canonical 06-30 报告闭环。 |

因此，在限定的 06-23～28 五份报告中，需要继续保持 reopen 的是 **06-23、06-24、06-25**；**06-27、06-28 不应为不属于本窗口的 family 重新制造候选**。后者的污染修复发生在 Books，真实 Books Decision 由 06-29/30 canonical owner 报告承担。

## 追加：`27797` / `27806` / `28661` fresh post-write audit

以下检查只看本轮新写入的 `## Review notes` 之前正文及 exact-v1 title/abstract/locator，不用 marker 自证。

| Family | Owner 与相邻衔接 | Authority / factual boundary | Trade-off / fallback | 结论 |
| --- | --- | --- | --- | --- |
| `SF-2026-ARXIV-2606-27797` *Optimizing Teacher-Student Partitioning...* | `TRAIN-DISTRIBUTED-TRAINING` 正确；“Teacher 与 Student 不应共享一份并行 Plan”位于 topology mapping 之后、global batch/收敛语义之前，先说明非对称 workload 如何改变布局，再回到 batch semantics，衔接成立。 | 正文把 teacher inference、student backward/optimizer state 与版本化 teacher-output handoff 分开；没有把作者最高吞吐外推为通用结论，promotion 仍由目标集群吞吐/显存/收敛共同验收。 | 明确列出 topology search、buffering、版本一致性与错误成本模型；teacher/student footprint 接近或证据不足时回退共享布局。 | **PASS** |
| `SF-2026-ARXIV-2606-27806` *Hybrid-WM* | `AGENT-PLANNING` 正确；插在部分可观测/commitment ledger 后、decomposition 前，把“想象状态不可提交”自然推进到 hybrid verifier。 | 明确 LLM 只拥有 semantic proposal，parametric transition model 只拥有 validity/risk/value sensor，environment observation/controller 保留事实与动作 commit authority；未把四个 graph benchmark 外推成 physics oracle。 | 明确额外调用、共享盲点、distribution shift、false rejection；低风险可回退纯 LLM proposal，高风险/OOD 回到规则、真实 rollout、tool observation 或人工。 | **PASS** |
| `SF-2026-ARXIV-2606-28661` *Modal/Correlation Ceiling* | `PLATFORM-EVALUATION-SYSTEM` 正确；紧接“Sampling Failure 与 Selection Failure”并在 Adaptive Evaluation 之前，形成 coverage→selection→adaptive budget 的连续论证。 | 把 candidate coverage、selection accuracy、相关性与 effective decision information 分开；没有把论文 ceiling 写成跨模型固定常数，release authority 仍由 verifier/selector calibration 与 abstention 持有。 | 明确估计漂移、样本不足与 selector mismatch；边际 selection gain 非正时停止增大 k，回退独立 verifier、多样 proposal source 或 abstain，同时保留少量独立采样的共存边界。 | **PASS** |

三项均通过 owner、相邻叙事、事实 authority、trade-off/fallback 四轴检查；无需额外正文修订。它们各自的旧 `daily-20260627:*` 后置块仍应删除，因为新正文已经承担知识 owner，后置块不能继续作为第二份正文。
