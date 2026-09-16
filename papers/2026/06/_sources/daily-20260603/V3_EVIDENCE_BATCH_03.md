# 2026-06-03 V3 Evidence batch 03

本批覆盖恢复候选 17～24。所有 locator 来自官方 exact-v1 HTML；当前正文存在可区分长期机制差额的项目已完成 owner-level 写回，其余项目由精确命题级正文覆盖。

## Candidate evidence 与 Books comparison

### 2606.03143v1 — FederatedSkill

- Evidence：Method=`§3；§4.1 client execution/patch distillation；§4.2 server personalized evolution`；Evaluation=`§5.1～§5.5；Appendix E privacy audit`；Limitations=`Limitations；Appendix F`。
- 边界：semantic skill diff 减少 raw trajectory 上传并支持 per-client library，但不等同 formal privacy；模型/CLI/simulated client、server LLM 与重构/PII canary 不能证明生产隐私或无恶意 patch。
- Books：**Integrated / `AGENT-PLATFORM`**。正文锚点“跨用户演进时，这一边界还要求把 private episode 与 shared skill revision 分开”已写入顶层 Review notes 之前，包含 federation/ownership 链、恶意或冲突 patch gate 与 local-only fallback。

### 2606.03220v1 — WebRISE

- Evidence：Method=`§3.1～§3.4 Interaction Contract Graph construction`；Evaluation=`§4.1～§4.4；§5.1～§5.3`；Limitations=`Limitations；Appendix B/C`。
- 边界：442 tasks、5 input modalities 与 14 models 支持 requirement-induced observable state/transition/DOM-visual assertions；simulated browser agent、implicit requirement extraction 与 judge 不证明真实产品需求完备。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。当前 EvalSpec/evaluator admission 已要求 requirement→observable state/action/effect、deterministic oracle、visual diagnostic 与 non-vacuous meta-evaluation。

### 2606.03239v1 — ARBOR

- Evidence：Method=`§3.1～§3.4 contrastive rubric induction、memory lifecycle 与 process reward`；Evaluation=`§4.1～§4.6；Appendix C/D`；Limitations=`Limitations`。
- 边界：三个 Qwen3 scale、四个 multi-hop QA benchmark 与 LLM judge 支持 rubric reuse 可为 outcome-homogeneous groups 提供 process signal；不证明 rubric truth、跨 domain 稳定或 judge 无同源偏差。
- Books：**Integrated / `TRAIN-GRPO`**。正文锚点“Rubric Pool 还需要 Admission、Consolidation 与 Retirement”已写入顶层 Review notes 之前，包含 reward-asset lifecycle、terminal-verifier authority、drift quarantine 与静态 rubric fallback。

### 2606.03291v1 — Multilingual Unlearning

- Evidence：Method=`§3.1～§3.4 multilingual TOFU、objectives 与 NLI semantic score`；Evaluation=`§4.1～§4.4；Appendix F/J/K`；Limitations=`§5 Discussion；Appendix A/E`。
- 边界：五种语言、Qwen/Gemma 与 steering recovery 支持 cross-language forgetting transfer 非均匀且可能可逆；TOFU、NLI/judge 与 representation recovery 不证明真实隐私删除或所有语言均遗忘。
- Books：**Integrated / `PLATFORM-SECURITY`**。正文锚点“Unlearning Release 要测试跨语言迁移、可逆性与未知 Trigger Family”已写入顶层 Review notes 之前，覆盖 language/script transfer matrix、cross-language regain、reversibility 与受限删除结论。

### 2606.03318v1 — Realistic-Interaction Evaluation

- Evidence：Method=`§3 taxonomy；§4.1～§4.3 environment/user/verification`；Evaluation=`§5；§6.1～§6.3`；Limitations=`§8`。
- 边界：RUT-Bench 的 simulated ambiguity、uncooperative behavior 与 shifting intent 只代表构造分布；user simulator、reliability judge 与 environment coverage 不等于真实用户体验。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。当前正文已经把 realistic user state、bounded clarification、environment revision、outcome 与 user-experience diagnostics 分开，simulator 不能拥有 truth authority。

### 2606.03328v1 — Calibration Data Trade-offs for High-Sparsity Pruning

- Evidence：Method=`§3.1～§3.3 capability retention/profile/IGSP`；Evaluation=`§4；§5.1～§5.5；Appendix D/E`；Limitations=`Limitations`。
- 边界：15 calibration sources、Wanda/SparseGPT、LLaMA/OPT 与四个 capability slices 揭示 averaged score 掩盖 opposite-sign retention；不证明 taxonomy 完备、self-generated mix 取代真实数据或跨 pruning method 普适。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM`**。正文已要求 dense/pruned item-level transition、capability/calibration slices、真实 sparse runtime 与 rollback，平均 perplexity 不承担 release gate。

### 2606.03330v1 — FLIPS

- Evidence：Method=`§2 two-stage protocol；§3 fingerprint scheme；§4 discriminative power`；Evaluation=`§5.1～§5.3；Appendix E/F/K`；Limitations=`§6.2`。
- 边界：237 instances 上 pseudo-random sequence fingerprint 可区分部分 weights/prompt/sampling/quantization 组合；open-set errors、adversarial rerouting、tool/agent expansion 与 provider adaptation 不允许把 fingerprint 当身份真值。
- Books：**Existing / `PLATFORM-MODEL-REGISTRY`**。正文已将 instance identity 扩为 model、adapter、tokenizer、prompt/template、sampler、quantization/runtime，并要求 fingerprint 与 attestation/lineage 并存。

### 2606.03344v1 — RogueMerge

- Evidence：Method=`§III Threat Model；§IV-A～IV-C joint optimization、merge uncertainty 与 prompt heterogeneity`；Evaluation=`§V-A～§V-D`；Limitations=`§VII Conclusion；未披露 dedicated limitations`。
- 边界：六类 utility task、六种 merge algorithm 与 170+ merged models 支持第三方 task vector 可携带 merge-robust attack；不证明覆盖未知 merge、production defense 或 task-vector 检测完备。
- Books：**Integrated / `PLATFORM-SECURITY`**。正文锚点“Model Merge Input 是对权重的 Supply-chain Write Access”已写入顶层 Review notes 之前，覆盖第三方 merge component、隔离 composition、行为验收与 source-model fallback。

## Batch result

- Evidence complete：8/8。
- Books：4 `Existing`，4 `Integrated`，0 `Only report`，0 `Deferred`。
- exact-v1 blocker：0。
