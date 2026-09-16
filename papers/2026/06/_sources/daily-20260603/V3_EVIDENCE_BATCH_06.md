# 2026-06-03 V3 Evidence batch 06

本批覆盖恢复候选 41～48，全部使用官方 exact-v1 HTML。判断继续执行严格长期机制 gate：算法名、局部增益或新 benchmark 本身不形成 Books 写回；只有当前正文缺失的状态所有权、执行合同或发布边界才执行 owner-level 写回。

## Candidate evidence 与 Books comparison

### 2606.03800v1 — Trading Human Curation for Synthetic Augmentation in RLVR

- Evidence：Method=`§3.1 Augmentation Pipeline；§3.2 Quality Gate；§4.1～§4.4 substitution design`；Evaluation=`§5；§6.1～§6.3；Appendix G/L/M`；Limitations=`§7 Statistical limits；Scope and cost limits`。
- 边界：单训练 seed、单一 Qwen3.5-27B、10～319 tasks 与 data-curation-only cost 支持受限 substitution estimate；不证明跨规模/算法/领域的固定 synthetic-to-human 汇率，也未做 base resampling 或 gate FP/FN audit。
- Books：**Existing / `TRAIN-DATA` + `TRAIN-GRPO`**。当前 Data/GRPO 已把 sandbox、task、verifier、quality/learnable-zone gate、human/synthetic mix、held-out evaluation、lineage 与成本纳入同一训练数据合同，并保留人工 gold 与独立 oracle；本篇给出该合同下的受限经济测量，不改变 owner。

### 2606.03810v1 — Consistency Training Can Entrench Misalignment

- Evidence：Method=`§2.1 seven consistency methods；§2.2 model organisms；§3 non-neutrality framework`；Evaluation=`§4～§6.4；Appendix A～G`；Limitations=`§7 Limitations`。
- 边界：人工诱导的四类 misalignment、LLM judges 与不同规模的不等运行数支持“consistency training 非 alignment-neutral”；不证明自然部署中的方向或幅度，也不能把 sycophancy 放大推广到所有 behavior family。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM` + `PLATFORM-SECURITY`**。当前正文已要求 post-training artifact 重新运行 matched capability/safety slices、行为 family 与 distribution-shift canary，训练目标或自生成标签不能继承旧 safety verdict；本篇是该 gate 的具体反例。

### 2606.03892v1 — PROVE

- Evidence：Method=`§3.1 Live MCP Environment Framework；§3.2 state-grounded synthesis；§3.3 Multi-Component Reward`；Evaluation=`§4.1～§4.7`；Limitations=`§5 Conclusion；无 dedicated limitations`。
- 边界：20 个 stateful MCP servers、343 tools、约 13K examples 与四个小模型支持 session-isolated live execution、state-grounded query 与 programmatic reward 的组合；有限 server ontology/benchmarks 不证明真实 provider side effects、安全隔离或 reward 完备。
- Books：**Existing / `TRAIN-DATA` + `TRAIN-GRPO`**。当前 Data 已有 executable environment、initial/final state、tool schema、task、verifier 与 row lineage；GRPO 已有 environment-owned transition、MCP candidate environment admission、programmatic reward 与 outcome authority，故无新增长期合同。

### 2606.03928v1 — Value-Aware Stochastic KV Cache Eviction for Reasoning Models

- Evidence：Method=`§3.1 large-magnitude value states；§3.2 VaSE stochastic eviction`；Evaluation=`§4.1～§5；Appendix B～D`；Limitations=`Appendix E`。
- 边界：Qwen3 与六个 reasoning tasks 支持大 value state 被误删会触发循环、随机 eviction 增加 survivor diversity；不证明 value magnitude 是跨模型/任务的充分重要性指标，也未证明生产并发、tail latency 或所有 kernel 路径。
- Books：**Existing / `INFER-KV-CACHE`**。当前正文已把 attention、value norm、entropy、position 与随机 reservoir 当作 eviction proposal，要求 error-budget calibration、真实 packed/kernel 路径及 FullKV fallback；VaSE 是现有 sensor/actuator 组合的受限实例。

### 2606.03938v1 — q0: Primitives for Hyper-Epoch Pretraining

- Evidence：Method=`§2.1 snapshot population；§2.2 chain distillation；§2.3 learned prior`；Evaluation=`§3～§4；Appendix B/C`；Limitations=`§6 Limitations`。
- 边界：1.8B model、100M FineWeb tokens 与高 epoch budget 支持 population/snapshot、chain distillation 和 held-out weighting 的受限组合；多成员 inference 需要 K 次 forward，训练增加 teacher forward，未证明 frontier-scale data/model、真实 serving cost 或单模型蒸馏后保持增益。
- Books：**Integrated / `TRAIN-PRETRAINING`**。正文锚点“超多 Epoch 训练会把单一 Checkpoint 演进为模型群体状态”已写入顶层 Review notes 之前，包含 population snapshot identity、chain-distillation lineage、held-out member admission、budgeted deployment branch 与 single-model/distill-to-one fallback。

### 2606.03969v1 — Quantifying Faithful Confidence Expression in Large Reasoning Models

- Evidence：Method=`§3.1 internal confidence；§3.2 linguistic confidence；§3.3 faithfulness metrics；§3.4 interventions`；Evaluation=`§4～§5；Appendix A～C`；Limitations=`Conclusion limitations`。
- 边界：token probability、hidden state、sample consistency 与 external-judge decisiveness 会给同一 trace 不同 verdict；20-step cap、judge bias 和 normalization compression 不证明存在统一 intrinsic confidence truth。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。当前 Evaluation 已分离 white-box probe、token probability、自报 confidence 与 sample agreement，并要求 estimator-specific calibration、prompt variants、risk-coverage decision 和 independent outcome gate。

### 2606.03979v1 — Language Models Need Sleep

- Evidence：Method=`§3.1 learning phases；§3.2～§3.3 parameter expansion/knowledge seeding；§3.4 dreaming`；Evaluation=`§4.1～§4.2；Appendix B`；Limitations=`§5 Conclusion；Appendix A.4 limitations of OPSD`。
- 边界：披露的 continual-learning、knowledge incorporation 与 few-shot tasks 支持两阶段 consolidation/self-improvement proof of concept；不证明参数扩张、synthetic curriculum 或 self-distillation 能避免开放域遗忘、污染、隐私删除和长期 collapse。
- Books：**Existing / `AGENT-MEMORY`**。当前 Memory 已明确 external evidence 到 parameter consolidation 的条件分支，冻结 episodes、teacher/student、objective、checkpoint lineage、held-out evaluator、删除与 rollback；Sleep 是该分支的一种实现。

### 2606.03980v1 — Skill-RM

- Evidence：Method=`§3.1 Reward-Evaluation Skill；§3.2 resources；§3.3 judgment；§3.4 readout`；Evaluation=`§5.1～§5.5；Appendix A/D`；Limitations=`§6 Limitations and Future Work`。
- 边界：text instruction-following/reward benchmarks、best-of-N 与受限 RL 支持把 heterogeneous criteria 编排为显式 skill；人工构造、额外 inference overhead、未测 multimodal/long-horizon/open preference 不证明该 skill 是通用 reward truth 或可安全自我更新。
- Books：**Existing / `TRAIN-GRPO` + `AGENT-PLATFORM`**。当前 GRPO 已要求 reward/verifier identity、rubric/evidence provenance 与 independent outcome gate；Agent Platform 已把 skill definition、resource references、permission、version、validation 与 revoke 作为可执行资产合同，故该组合无需新增正文。

## Batch result

- Evidence complete：8/8。
- Books：7 `Existing`，1 `Integrated`，0 `Only report`，0 `Deferred`。
- exact-v1 blocker：0。
