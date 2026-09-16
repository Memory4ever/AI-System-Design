# 2026-06-03 V3 Evidence batch 04

本批覆盖恢复候选 25～32，全部使用官方 exact-v1 HTML。Books comparison 以当前正文机制为 authority；source-specific 名称只用于证据定位。

## Candidate evidence 与 Books comparison

### 2606.03354v1 — ImageAuditor

- Evidence：Method=`§2 Threat Model；§3.2 retrieval segment；§3.3 extraction segment；§3.4 multi-query aggregation`；Evaluation=`§4.1～§4.3`；Limitations=`Appendix A additivity assumption；Appendix E`。
- 边界：黑盒 image-RAG 的跨模态 membership signal 只在所测 retriever/generator/dataset 与少量 query budget 下成立；multi-query aggregate、caption/embedding search 与生成差异不证明法律权利或完整 datastore membership。
- Books：**Existing / `PLATFORM-SECURITY`**。当前正文已把 retrieval/example-store membership、query-family identity、multi-query correlation、sampling false positive 与 disable/isolate fallback 写入威胁合同；图像只是 modality-specific probe。

### 2606.03391v1 — When Model Merging Breaks Routing

- Evidence：Method=`§3.1～§3.2 routing/non-linearity mismatch；§4.1～§4.4 HARC`；Evaluation=`§5.1～§5.4；Appendix C/D`；Limitations=`§4.5 Discussion；§6 Conclusion`。
- 边界：OLMoE math/code merge、所测 algorithms 与 calibration data 支持 merge 后 router breakdown 与 training-free correction；不证明 source routing 是唯一正确目标、跨 MoE/topology 普适或 production load balance 已恢复。
- Books：**Integrated / `PLATFORM-MODEL-REGISTRY`**。正文锚点“MoE Merge 的发布身份还要包含 Router Calibration”已写入顶层 Review notes 之前，覆盖 merged weights、calibration revision、expert-assignment/load regression 与 source-model fallback。

### 2606.03458v1 — KVarN

- Evidence：Method=`§3.1 magnitude/directional error；§3.2 autoregressive accumulation；§3.3 variance-normalized quantization；§3.4 proxy test`；Evaluation=`§4.1～§4.2；Appendix F/G/I`；Limitations=`Appendix E`。
- 边界：AIME/MATH/HumanEval/IFEval 与所测 models/kernels 支持 per-token scale error 会在 decode 累积；proxy reconstruction、Hadamard/dual scaling 不证明任意 long reasoning 或硬件保持 quality/speed。
- Books：**Existing / `INFER-KV-CACHE`**。命题锚点“Quantization Objective 应对齐 Attention Distortion”已明确 repeated state feedback，并直接以 KVarN 的 pseudo-decode 证据约束 autoregressive accumulation；无须重复写入。

### 2606.03461v1 — Effective Training Trajectories for Terminal Agents

- Evidence：Method=`§2 matched-task distillation；§3 Terminal-Lego；§4.3 Environment-Grounded Supervision`；Evaluation=`§5；Appendix C/D`；Limitations=`Limitations and Future Work`。
- 边界：固定 harness/task/student 下，teacher raw ability 不等于 teachability；inspect-act-verify/TOR 与 Docker round-trip 是有限 proxy，不证明所有较长或有错误 trajectory 更优。
- Books：**Existing / `TRAIN-DATA`**。正文已要求 teacher trajectory 绑定 environment/harness/verifier/observation-action lineage、executable filtering 与 outcome canary；teacher 只提供候选监督。

### 2606.03463v1 — DMF

- Evidence：Method=`§3 architecture；§4～§8 deterministic signals/score/decay/pruning；§9 lifecycle/lineage`；Evaluation=`§11 LoCoMo/LongMemEval-10`；Limitations=`§12～§13；无 dedicated limitations`。
- 边界：CPU-first deterministic scoring 可复算写入/驱逐，但 classical features、binary LLM judge 与 two benchmarks 不证明 semantic truth、个性化价值或跨域 memory quality。
- Books：**Existing / `AGENT-MEMORY`**。当前正文已经分离 raw event、deterministic/derived memory、lineage、decay/prune policy、conflict/freshness 与 full-history fallback。

### 2606.03467v1 — StepFinder

- Evidence：Method=`§4.1～§4.5 trajectory encoding、temporal features、agent-aware scoring`；Evaluation=`§5～§7；Appendix B/D`；Limitations=`§8 Conclusion；无 dedicated limitations`。
- 边界：Who&When 的 algorithm/hand-crafted subsets 支持 learned step ranking，不证明 earliest high score 是 causal root cause，且 embedding/classifier 与 benchmark label 限制外推。
- Books：**Existing / `PLATFORM-TRACE`**。正文已有 earliest evidence-backed failure span、agent/step responsibility、propagation 与 outcome binding，并要求 counterfactual/repair 验证而非把 scorer 当因果真值。

### 2606.03544v1 — SAGE

- Evidence：Method=`§2.1～§2.3 SocialEvo/SelfEvo compute-matched design 与 history representations`；Evaluation=`§3；§4.1～§4.4`；Limitations=`§6；§8`。
- 边界：五个 model family、三个 arena 与 matched rollout budget 支持 peer-history effect 可与 self-iteration 分离；public-history representation、ranked game/task 分布与有限 rounds 不证明通用社会学习。
- Books：**Existing / `PLATFORM-EVALUATION-SYSTEM` + `AGENT-MULTI-AGENT`**。正文已要求 compute-matched counterfactual、history-channel identity、coordination tax 与 task outcome，不能把更多 peer exposure 计为独立能力。

### 2606.03565v1 — R3-Skill

- Evidence：Method=`§1.3 query-conditional set compatibility；§2 dataset；§3 two-stage retriever`；Evaluation=`§4.1～§4.5；Appendix A/B`；Limitations=`§5 Limitations and future work`。
- 边界：R3-Skill/SkillRet、synthetic annotation 与 Set-Compat 支持 joint skill compatibility 不等于独立 relevance；不证明 retrieved set 安全、可执行或跨 skill pool/语言普适。
- Books：**Existing / `AGENT-PLATFORM`**。当前正文已要求 task/skill compatibility、dependency/conflict graph、permission hard gate 与 executable-set validation；retriever 只拥有候选集合。

## Batch result

- Evidence complete：8/8。
- Books：7 `Existing`，1 `Integrated`，0 `Only report`，0 `Deferred`。
- exact-v1 blocker：0。
