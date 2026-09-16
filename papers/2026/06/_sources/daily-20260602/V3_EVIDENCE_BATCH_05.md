# 2026-06-02 V3 Evidence Batch 05

本批处理十项 V3 存续候选。公开时间使用 2026-06-02 官方 arXiv announcement batch 的北京时间范围；各条只绑定 exact v1，Books 比较以当前正文为准。

## Candidate evidence

### 2606.02011 — Extreme Low-Bit Quantization for Reasoning Models

- Primary / exact-v1: <https://arxiv.org/html/2606.02011v1>。
- Method: §4–§7 用 reasoning length、hit-limit、think-closed、time-to-first-answer 与 loop rate 区分 path-finding/commitment failure；按 model×benchmark regime 选择 FP16 planning、loop rescue 或 full-precision fallback，而非统一 2-bit 路径。
- Evaluation: §3–§8 在 Qwen reasoning 8B/32B、W4A16/W2A16、数学与常识 benchmark、4K/8K/32K budget 上联合测 accuracy、trace dynamics、per-token throughput 与 end-to-end latency。
- Non-proof: 只覆盖两种 Qwen scale、GPTQ-style weight-only quantization 和固定 decoding；loop detector/parseable answer 不适用于所有任务，FP16 intervention 增加切换与执行成本，作者结果不证明 production batching/tail。
- Books comparison / final: 差额已写入 `INFER-TENSORRT-LLM` 正文锚点“Reasoning Quantization 要验收 Commitment，而不只是 Token Cost”；precision、budget、termination 与 FP16 fallback 均可定位。

### 2606.02031 — OpenWebRL: Demystifying Online Multi-turn Reinforcement Learning for Visual Web Agents

- Primary / exact-v1: <https://arxiv.org/html/2606.02031v1>。
- Method: §3–§4 组合 live-browser rollout infrastructure、SFT initialization、multimodal context、trajectory-level success judge、invalid-sample filter 与 online multi-turn policy optimization；environment revision 与 browser state 是 rollout identity。
- Evaluation: §5–§6 在 Online-Mind2Web、DeepShop 等 live-web benchmark 上比较 SFT/filtered BC/online RL，并消融 reward、context、task difficulty 与 response length。
- Non-proof: live web 会漂移且 judge/format/status filter 有误差；2.2K training tasks、4B model 与所列 websites 不证明 production account safety、CAPTCHA/permission、长期 stability 或其他 Agent domain。
- Books comparison: `TRAIN-GRPO` 当前正文已要求 trajectory、environment state、behavior policy、reward/judge、invalid sample 与 off-policy identity；Agent Platform 也已有 browser sandbox/effect gate。该文是受限 web implementation，判 `已有覆盖`。

### 2606.02041 — SentGuard: Sentence-Level Streaming Guardrails for Large Language Models

- Primary / exact-v1: <https://arxiv.org/html/2606.02041v1>。
- Method: §3 在完整 sentence boundary 上增量判断 prefix safety，保留跨句 state 并输出风险类别/level；它在 full-response late block 与 token-level unstable block 之间选择可解释 commit unit。
- Evaluation: §4 与附录用 StreamSafe、Detection@K、mean first-detection sentence、streaming false-positive、full-response F1 和 latency 比较 token/sentence/response guardrails。
- Non-proof: sentence segmentation、taxonomy、语言与数据分布会漂移；句尾前已发送的 token 可能不可撤回，低延迟分类器也不证明任意多轮/tool effect 被阻断。
- Books comparison / final: 差额已写入 `PLATFORM-SECURITY` 正文锚点“Streaming Guard 的最小可解释 Commit Unit 可以是完整 Sentence”；buffer、segmenter revision、released bytes 与 abort/fallback 均可定位。

### 2606.02109 — BADGER: Bridging Agentic and Deterministic Evaluation for Generative Enterprise Reasoning

- Primary / exact-v1: <https://arxiv.org/html/2606.02109v1>。
- Method: §5 先让 LLM 抽取/对齐结构，再用 deterministic cell-level scoring 与 tolerance 做最终判定；§7 将 tool recall/order/excess、faithfulness、summary 与 intent 分 metric owner。
- Evaluation: §6 用 enterprise corpus、human labels、Cohen's kappa、complexity strata 与 competing frameworks 校准，§8 描述 longitudinal pipeline；生成 judge 与 deterministic scorer 不共享最终 authority。
- Non-proof: LLM structural stage仍非确定、human corpus/provider 有限，multimodal RAG 尚在进行中；高 agreement 不代表生产 construct validity 或所有 enterprise schema 可表达。
- Books comparison: `PLATFORM-EVALUATION-SYSTEM` 当前正文已要求 generative proposal/semantic parser 与 deterministic verifier 分层，metric provenance、abstention、human calibration 与 release gate 独立。判 `已有覆盖`。

### 2606.02240 — AgentRedBench: Dynamic Redteaming and Integration-Aware Defense for LLM Agents over SaaS Integrations

- Primary / exact-v1: <https://arxiv.org/html/2606.02240v1>。
- Method: §3–§4 把 connector/integration、tool argument、destination/content hijack 与 tool-family creep 编成动态 attack scenarios；guard placement 读取 integration/action context，而非只分类最终文本。
- Evaluation: §5 在多 SaaS connectors、no-guard/guard、held-out integration/attack type 上测 detection、ASR reduction、latency、over-refusal 和 task completion，并有 adaptive attacker 与 fixture cleanup。
- Non-proof: scenario selection、模拟 SaaS fixture 与五次 attacker budget 限制 coverage；guard finetune/judge 不是生产 policy，未覆盖真实 credential、provider drift 或全部 compound effects。
- Books comparison / final: 差额已写入 `PLATFORM-SECURITY` 正文锚点“Integration-aware Campaign 必须把 Connector 与 Effect Identity 编进 Case”；campaign identity、cleanup receipt 与 detector/executor 分权均可定位。

### 2606.02245 — When Knowledge Is Not Free: Cost-Aware Evidence Selection in Retrieval-Augmented Generation

- Primary / exact-v1: <https://arxiv.org/html/2606.02245v1>。
- Method: §3–§5 给 evidence 标注 access-cost tier，在 query/shared workload budget 下让 selector/agent选择购买、停止或回答；quality 与证据访问成本共同进入决策，不假设 top-k 文档免费。
- Evaluation: §4–§5 在多 RAG benchmark、不同 pricing/budget、selector 与 agent controller 上比较 answer quality、cost、evidence sufficiency 与 shared-budget allocation。
- Non-proof: §8 使用模拟价格和自动 tier annotation、简化 retrieval environment 与 zero-shot controller；没有真实许可、paywall、组织预算或 production latency，cost tier 不代表 evidence authority。
- Books comparison / final: 已写入 `AGENT-RAG` 正文“Evidence Access Right、Cost 与 Sufficiency 是联合检索状态”。Authorization/source authority 先于价格，budget owner 产生 purchase receipt，answer gate 在关键证据预算不足时 abstain。

### 2606.02282 — POIROT: Interrogating Agents for Failure Detection in Multi-Agent Systems

- Primary / exact-v1: <https://arxiv.org/html/2606.02282v1>。
- Method: §3 让系统内多个 role agent 互相 interrogation，再聚合局部故障判断，以 epistemic diversity 分散单一 evaluator；BLAME 提供 compound-fault attribution tasks。
- Evaluation: §4–§5 比较 single-LLM evaluator 与 POIROT，按 problem complexity、agent count 与 fault dimensionality 报 detection/attribution。
- Non-proof: 执行 agent 与诊断 agent 共享模型/上下文时错误相关，内部共识不是独立 truth；benchmark 不证明法规合规、安全关键 deployment 或真实 side-effect attribution。
- Books comparison: 该机制可作为 diagnostic proposal，但论文把“无需外部 oversight”外推过强；当前 Multi-Agent/Trace 已要求 independent verifier、provenance 与 correlated-error fallback。故不新增正文，判 `仅报告`。

### 2606.02304 — Unified Context Evolution for LLM Agents

- Primary / exact-v1: <https://arxiv.org/html/2606.02304v1>。
- Method: §3 把 trajectory 经验分为 Memory、Strategy、Workflow、Skill 四类 typed ECU，以 type-specific generation/retrieval、repeated-use outcome scoring、pruning 与 deficit-aware generation budget 演进外部 library。
- Evaluation: §4 在 ALFWorld/WebShop 上比较固定 context、untyped pool 与 UCE，并测各 type、budget scheduler、pruning 与跨 actor transfer。
- Non-proof: 两个 simulator benchmark 与 outcome-derived score 不证明真实工具/用户、长期 safety 或跨 model语义兼容；同一 library 自评会产生 selection bias，prune 可能不可逆丢失证据。
- Books comparison: Agent Memory/Platform 当前正文已要求 typed memory/strategy/workflow/skill 由唯一 owner、带 provenance/version/admission/usage/retirement，且派生状态不能成为事实 authority。判 `已有覆盖`。

### 2606.02357 — Do Multimodal Agents Really Benefit from Tool Use? A Systematic Study of Capability Gains

- Primary / exact-v1: <https://arxiv.org/html/2606.02357v1>。
- Method: §3 用同源 Tool-Free counterpart 与 Pure-Text Reasoner 冻结训练来源，对 tool-solved set 做交集/独占分解，并把调用结果区分为确认、修复、干扰等贡献类型。
- Evaluation: §4 在 OCR、chart、real-world understanding、math 上比较 aggregate accuracy、solved-set、token cost、call-format vs returned-result ablation 与 process attribution。
- Non-proof: 只覆盖两个 multimodal agents、给定 benchmark 与 judge；solved-set overlap 不是逐样本因果 proof，tool-free training差异与重复抽样仍可能混淆，不能外推所有工具无益。
- Books comparison / final: 已写入 `AGENT-TOOL-CALLING` 正文“Tool 出现不等于 Tool 对答案有贡献”，以 no-tool/call-shell/real-result counterfactual 区分 confirm/repair/harm/no-effect，并把 attribution 与最终 outcome authority 分离。

### 2606.02359 — MOC: Multi-Order Communication in LLM-based Multi-Agent Systems

- Primary / exact-v1: <https://arxiv.org/html/2606.02359v1>。
- Method: §3 不直接拼接一阶 neighbor responses，而构造 multi-order structured evidence stream，并用 semantic-topological merging 在 token budget 下保留多跳依赖与来源层级。
- Evaluation: §4 在六数据集、多种 LLM backbone/agent topology 上比较 task performance、communication token 与 ablation。
- Non-proof: benchmark 多为无副作用推理，合并 scorer 可能抹掉 minority/冲突；多跳表示不证明消息真实、独立或完整，开放网络 delivery/permission 未测。
- Books comparison / final: 已写入 `AGENT-MULTI-AGENT` 正文“多阶消息需要 Ordered Evidence DAG，而不是压平后的共识摘要”，覆盖 per-hop lineage、budgeted merge、omitted-node/consolidation-loss receipt、raw-message fallback 与独立 verifier。

## Batch result

- Evidence closed: 10 / 10。
- Books: 3 `已有覆盖`，6 `整合已写入`，1 `仅报告`，0 `整合 proposal`，0 `暂缓`。
- Proposal queue: 空。2606.02011、2606.02041、2606.02240、2606.02245、2606.02357、2606.02359 均已完成正文绑定。
