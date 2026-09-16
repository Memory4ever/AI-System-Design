# 2026-06-03 V3 Evidence batch 02

本批继续覆盖 8 个恢复 Candidate。`2606.03083v1` 的官方 HTML 在本轮反复超时，但官方 exact-v1 PDF 可访问，因此以 PDF 的 Method/Experiment/Limitations 标题作 locator，不把 HTML 渲染失败误记为论文不可访问。其余使用官方 exact-v1 HTML。

## Candidate evidence 与 Books comparison

### 2606.02981v1 — Predicting Inference-Time Scaling Gains

- Evidence：Method=`§3.1～§3.3 configuration/gain/features、predictor 与 theoretical analysis`；Evaluation=`§4.1～§4.6；Appendix C`；Limitations=`Limitations；Appendix C.4`。
- 边界：小 configuration grid 的 labeled validation statistics 可预测部分 Best-of-N gain 排序，但 LOSO residual、domain transfer、reward model 与 sampling budget 限制了 admission authority。
- Books：**Existing / `INFER-SCHEDULING`**。正文已有 cost-aware estimator、reasoning/sample budget、calibration 与 fixed-budget fallback；廉价 predictor 只能是 admission sensor。

### 2606.03075v1 — TGV-KV

- Evidence：Method=`§3.1～§3.3 text-grounded layer budget 与 eviction`；Evaluation=`§4.1～§4.5；Appendix B`；Limitations=`§4.5 Discussions；Appendix D`。
- 边界：所测 VLM/image/video tasks 支持 text-vision attention 作为 visual-KV importance signal，不证明跨模型、长文本/短视觉比例、任意 instruction 或生产并发下保持质量。
- Books：**Existing / `INFER-KV-CACHE`**。正文已把 modality/role、结构保护、importance selector、position/revision identity 与 FullKV fallback 写成同一 eviction contract；text grounding 是受限 sensor 实例。

### 2606.03083v1 — DeltaMem

- Evidence：官方 exact-v1 PDF；Method=`residual-tree memory construction、增量 write/prune 与 conflict handling`；Evaluation=`Experiments/ablation`；Limitations=`Limitations/Conclusion 的 task、memory 与 evaluator 边界`。
- 边界：residual tree 可减少重复 experience 并显式呈现冲突，但有限 Agent task/evaluator 不证明 tree summary 是 truth、跨 session 自动 merge 无漂移或所有历史都可无损压缩。
- Books：**Existing / `AGENT-MEMORY`**。正文已分离 raw evidence、derived memory、conflict/freshness、versioned merge 与 rollback；新结构没有改变 truth/commit authority。

### 2606.03087v1 — Correct-Set Turnover in RLVR

- Evidence：Method=`§3.1 turnover；§3.2 repair-window principle；§3.3 ReMind queue/batch/update`；Evaluation=`§4.1～§4.6；Appendix A～C`；Limitations=`Limitations`。
- 边界：两个 backbone、20 个 text/image/video math benchmark 支持 mastered-set acquisition/retention 分离与有限 review budget；不证明 zero extra rollout 等于 zero training cost，或 repair window 跨 task/domain 固定。
- Books：**Integrated / `TRAIN-GRPO`**。正文锚点“Mastered Set 需要 Acquisition–Retention Turnover Ledger”已写入顶层 Review notes 之前，包含 `mastered set → acquisition/retention turnover ledger → review delay/repair window → pre-rollout replacement queue`、预算约束与 replay/canary fallback。

### 2606.03092v1 — The Shadow Price of Reasoning

- Evidence：Method=`§3 objective；§4 shadow-price parity/equilibrium；§5 threshold prediction 与 global optimization`；Evaluation=`§6；§7.1～§7.4`；Limitations=`§9 Conclusion 与 controlled length-bin/model assumptions`。
- 边界：surge utility、threshold predictor 与 global shadow price 依赖所拟合任务/模型及 utility definition；rational abandonment 不能覆盖 safety-critical minimum service 或未校准长尾。
- Books：**Existing / `INFER-SCHEDULING`**。正文已有 resource shadow price、reasoning-budget allocation、future-recovery opportunity、hard reservation 与 fixed-budget fallback。

### 2606.03113v1 — Experience-Driven Dynamic Exits

- Evidence：Method=`§3.1 MDP；§3.2 offline RL；§3.3 dynamic exit/adaptive drafting`；Evaluation=`§4.1～§4.4`；Limitations=`§5 Conclusion；未披露 dedicated limitations`。
- 边界：Llama-2/3 与所测 tasks 上的 speedup 不证明 learned exit policy 跨 model/workload/hardware 稳定；内部 state 与 offline replay 也不是 correctness certificate。
- Books：**Existing / `INFER-SPECULATIVE-DECODING`**。正文已将 adaptive draft depth/length 作为 proposal policy，target verification 与 committed state frontier 仍独占 correctness，漂移时回退静态或普通 decode。

### 2606.03135v1 — Uncertainty-Aware Clarification

- Evidence：Method=`§3.1～§3.4 environment、data、Bayesian experimental design 与 DAPO`；Evaluation=`§4.1～§4.4`；Limitations=`Appendix §6.5 Failure Analysis；synthetic intent/user/judge scope`。
- 边界：information-gain reward 在受控 user/tool environment 中改善 clarification，但 ground-truth goal、simulated reply 与 judge 不证明生产用户意图可观测或 EIG 校准。
- Books：**Existing / `AGENT-PLANNING`**。正文已有 calibrated belief、ask/explore information gain、action/delay/failure cost、hard override 与 user-confirmation fallback。

### 2606.03136v1 — PsychoPass

- Evidence：Method=`§2 attack generation、trajectory construction、geometric profiling`；Evaluation=`§3.1～§3.3`；Limitations=`§5 Limitations/Future work`。
- 边界：7,525 个 Crescendo trajectories 中 near-perfect naive classifier 主要来自 turn-count confound；长度控制后只剩受模型、encoder、attack generator 与 judge 限制的早期 sensor，不能证明可阻断真实攻击。
- Books：**Existing / `PLATFORM-SECURITY`**。正文已将多轮 residual trajectory probe 限定为需校准的 sensor，并保留 policy/tool authorization/effect mediation 作为最终 authority。

## Batch result

- Evidence complete：8/8。
- Books：7 `Existing`，1 `Integrated`，0 `Only report`，0 `Deferred`。
- exact-v1 blocker：0。
