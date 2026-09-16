# 2026-05-15 V3 Root Semantic Repair Queue

- 生成者：`fresh-nonauthor:may15-final-gate-20260915`
- 状态：12/12 已应用并通过另一位 fresh non-author 写后验收；queue 已关闭，05-15 为 Complete。
- 范围：只处理下列 12 个 Books 动作和对应报告/状态同步；不得扩窗、扩源、重审 679 分母、95 Evidence、14 source slots 或改动已通过的 13 个 root 写回。

## A. 保留 Integrate，但修复现有 binding（5 项）

### `SF-2026-ARXIV-2605-13981`

- Target：`books/part-06-ai-infrastructure/70-cost.md`
- 唯一边界：标题 `### 成本分母要覆盖优化链，而不只看最终服务` 下、marker `<!-- source-family:SF-2026-ARXIV-2605-13981 -->` 前的 distillation lifecycle 段；不得触碰其后的 EnergyLens 段。
- 缺失命题：当 lifetime、allocation、reuse assumptions 失效或 upstream cost 不可得时，lifecycle total 必须标 Unknown/分项报告；若问题明确是已部署且 upstream sunk/out-of-scope 的 student，则 marginal per-request serving cost 仍是合法共存基线，不能被强行改成全生命周期结论。
- exact-v1 locator：Method=`3.2 Models and Tasks`；Evaluation=`5 Experimental Design`；Non-proof=`8 Limitations and Future Work`。

### `SF-2026-ARXIV-2605-14786`

- Target：`books/part-06-ai-infrastructure/72-security.md`
- 唯一边界：`### Security Gate 必须覆盖 Defense Interaction、审计通道与部署变换` 下，`2605.14591` marker 后、`<!-- source-family:SF-2026-ARXIV-2605-14786 -->` 前的 browser-agent fingerprint 段。
- 缺失命题：证据只覆盖 passive co-located site operator、单一 Midscene.js harness、14 个 frontier models 与四个 web environments；single-task transfer 较弱，open-set detection 不完美，不证明 harness-invariant、任意生产浏览 Agent 都可识别或防御已完备。
- exact-v1 locator：Method=`3.2 Threat Model`；Evaluation=`4 Experimental Setup`；Non-proof=`8 Conclusion`。

### `SF-2026-ARXIV-2605-15053`

- Target：`books/part-04-training-system/28-pretraining.md`
- 唯一边界：标题 `### Continual Pretraining 可以减少 Replay，但不能宣称消除遗忘` 内建立独立 `:start/:end` binding；必须在 `SF-2026-ARXIV-2605-09608:start` 之前闭合，不能让 marker 落在 09608 block 之后。
- 缺失/错误命题：不得把论文写成已披露的“新旧任务读写梯度分量分解器”。exact-v1 只支持 TFGN internal overlay/capability-level mechanism：无 replay、无 task ID/phase boundary、forward read 保持 dense，task-driven update signals 自动落入结构上不同的 trainable subspaces；内部 lever/specification 受 NDA 限制。保留 acquisition/retention/transfer Gate、capacity/compute 与 replay/adapter fallback。
- exact-v1 locator：Method=`3.1 What TFGN is; 3.2 Mathematical foundations and gradient protection`；Evaluation=`4 Experimental Setup`；Non-proof=`9 Limitations; 9.2 Architecture access and NDA terms`。同时修正 `exact-v1-locator-audit-v3.json` 中错误的 `6.1 Extension A...` method locator。

### `SF-2026-ARXIV-2605-15138`

- Target：`books/part-06-ai-infrastructure/72-security.md`
- 唯一边界：`2605.14786` marker 后、`<!-- source-family:SF-2026-ARXIV-2605-15138 -->` 前的 post-quantization unlearning 段。
- 缺失命题：trade-off 必须同时报告 target removal、control retention/clean utility、PTQ recipe/bit-width matrix 与额外 optimization/evaluation cost；若没有 quantized deployment，fp32 evaluation 仍可作阶段证据，但不能签发最终量化 artifact。
- exact-v1 locator：Method=`4 Method`；Evaluation=`6 Experiments`；Non-proof=`7 Discussion`。

### `SF-2026-ARXIV-2605-15152`

- Target：`books/part-06-ai-infrastructure/72-security.md`
- 唯一边界：`2605.15138` marker 后、`<!-- source-family:SF-2026-ARXIV-2605-15152 -->` 前的 quantization outlier 段。
- 缺失命题：补 anomaly detector false positive、clean accuracy、precision/memory、calibration burden；把证据收窄到作者受测 models、attacks 与 targeted quantizers，不得只写“不是任意格式”。
- exact-v1 locator：Method=`C.1 Details on the Targeted Quantization Methods`；Evaluation=`4 Experimental Evaluation`；Non-proof=`Appendix A Limitations and Future Work`。

## B. 删除 false-positive / 孤悬 marker（2 项）

### `SF-2026-ARXIV-2605-14249`

- Target：`books/part-06-ai-infrastructure/70-cost.md`
- 唯一边界：`2605.13981` marker 后，以“多 GPU inference 调优同样不能只在小样本上盲搜最低能耗”开头、以 `<!-- source-family:SF-2026-ARXIV-2605-14249 -->` 结束的完整段落。
- 动作：删除重复正文与 marker；将 disposition 改为 `No Change — Existing Coverage`。
- 具体既有命题：同章 `### Adaptation 不是单一路径，而是受预算约束的组合决策` 已冻结 task/quality/data/model/hardware/training/retrieval/serving price/eval contract，预测模型只拥有 proposal，实际 Evaluation/resource ledger 提交，校准/价格/负载漂移时回退 direct measurement；`### Generation Energy 不是 Token 数的线性函数` 又要求 analytical model 由当前 runtime energy/quality/SLO 校准，窄稳定 workload 才保留线性基线。
- exact-v1 locator：Method=`4.1 Evaluation Methods`；Evaluation=`Appendix M Experimental Setup and Compute Resources`；Non-proof=`Appendix J Limitations`。

### `SF-2026-ARXIV-2605-15132`

- Target：`books/part-07-agent/81-workflow.md`
- 唯一边界：`<!-- semantic-body-binding:SF-2026-ARXIV-2606-14672 -->` 后、标题 `#### Resource Lease 不能隐藏在 Agent 的控制流里` 前的单独一行 canonical marker。
- 动作：删除孤悬 marker；维持 `No Change — Existing Coverage`，不得把上一段 latent handoff 或下一段 Resource Lease 冒充 APWA binding。
- 具体既有命题：Ch81 `## Deterministic Spine，Agentic Nodes` 已把 identity、authorization、budget、retry/state transition/side effect/cancellation 放在 deterministic spine，把解释、draft、plan/tool proposal 留给 model-driven node；APWA 的并行编排实例不改变该 owner/control 边界。
- exact-v1 locator：Method=`2.1 Architectures for Multi-Agent Systems`；Evaluation=`4.1 Main experiments`；Non-proof=`Appendix A Limitations`。

## C. No Change false-negative，需要新增唯一 binding（5 项）

### `SF-2026-ARXIV-2605-14305`

- Target：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 建议边界：`## Draft、Verify 与 Correct 不是同一件事` 的 `### Draft + exact verification` 附近建立唯一 binding。
- 缺失命题：普通 DLLM 以同一 corrupted input 对 clean tokens 做独立预测会产生 posterior factorization error；prefix-conditioned clean-token factorization 改变 target distribution construction，speculative verifier 只加速且保持 target distribution，不能把两者混成一个 correctness owner。
- exact-v1 locator：Method=`3 Methodology`；Evaluation=`4 Experiment`；Non-proof=`5 Limitation and Conclusion`。

### `SF-2026-ARXIV-2605-14368`

- Target：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- 建议边界：`## Diffusion：用迭代修正换并行状态更新` 后、`Review notes` 前建立唯一 binding。
- 缺失命题：geometry proxy 只负责选择 diffusion-friendly hidden interface；conditional diffusion bridge 替换 transformer lower layers，retained suffix/LM head 继续拥有 token recovery。它不是 standalone diffusion LM；bridge size/depth/compute 与 suffix coupling 失败时回退原 transformer 或更浅 replacement。
- exact-v1 locator：Method=`3 Method`；Evaluation=`4 Experiments`；Non-proof=`6 Limitations`。

### `SF-2026-ARXIV-2605-14621`

- Target：从错误的 `PLATFORM-MONITORING`/Ch67 重路由到 `books/part-03-multimodal-world-models/23-multimodal-representation.md`，靠近 `### Object Hallucination 需要分开视觉写入与语言读取`，并在 `Review notes` 前建立唯一 binding。
- 缺失命题：同一 LVLM 的 shared early prefix 保留 prompt/history/position/early grounding，late counterfactual branch 屏蔽 image-token access，internal contrastive decoder 用视觉证据是否继续写入的差异提出 token proposal；它减少 external perturbation/second full forward，但增加 late-layer overhead，且需要 white-box hidden state/mask/cache。decoder 不拥有事实真值，失配时回退外部 grounding/verifier。
- exact-v1 locator：Method=`3 Method`；Evaluation=`4 Experiments`；Non-proof=`6 Conclusion and Limitations`。

### `SF-2026-ARXIV-2605-15041`

- Target：`books/part-07-agent/78-tool-calling.md`，靠近 `## Tool Necessity 与 Execution Admission 是两个 Gate` 或本章条件化机制分支，并在 `Review notes` 前建立唯一 binding。
- 缺失命题：把历史 execution trajectories 压成 complexity profile 与 failure profile；前者只提议 reasoning budget，后者为 schema-level reward 提供 failure attribution，真实 execution/outcome 仍由 runtime verifier 提交。收益是避免 uniformly over/under-think，代价是 case-base drift、profile 误归因、reward shaping 与长程规划不足；失配时回退固定 budget、普通 SFT/GRPO 与 deterministic schema gate。
- exact-v1 locator：Method=`4 Method`；Evaluation=`5 Experiments`；Non-proof=`6 Conclusion`。

### `SF-2026-ARXIV-2605-15157`

- Target：`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`，靠近 `### 从视觉 Action Chunk 到快慢分层的 Contact Feedback Loop` 或 Fleet intervention loop，并在 `Review notes` 前建立唯一 binding。
- 缺失命题：高 DoF 接管时，human hand pose 与 policy command 的 identity mismatch 会造成 gesture jump；relative hand retargeting 与 arm residual shared control 只拥有连续 correction proposal，低层 controller/safety owner 继续提交动作。代价包括 retarget calibration、latency/contact drift 与人类负担；不连续、跟踪丢失或 safety margin 不足时回退 full takeover/stop/reinitialize。
- exact-v1 locator：Method=`3 Methodology`；Evaluation=`4 Experiments`；Non-proof=`5 Conclusion and Limitations`。

## D. 仅报告/状态的机械同步

1. 把 `2605.14241/14421/15051/15079/15109/15185` 从 No Change 改为 `Applied — current main-body binding verified`，并复制各自 canonical marker 前的真实正文命题作为 comparison excerpt。
2. 为仍是 No Change 的 `2605.15141/15153/15178/15190` 填入具名现有命题，禁止保留空白 `existing_proposition_excerpt`。
3. 按 A/B/C 完成后的确定性目标重算：`95 = 11 Applied + 23 Integrate + 61 No Change`；同步 README、`books-comparison-v3.json`、root queue、author checkpoint 与 active independent audit。
4. 修正 `2605.15053` 的 exact-v1 method locator；任何其他 locator 只在发现确切错误时定点修正，不重建 95 项 Evidence。

## 写后 Gate

- root repair 已完成，但不等于 Complete；application receipt 见 `V3_ROOT_POSTWRITE_CHECKPOINT_20260915.md`。
- 另一位未参与这些修复的 fresh non-author 只需复核本队列 12 个 Books 动作、10 个机械 disposition/excerpt 修复、marker 唯一与 95 项分区集合；不得重开已通过的分母、来源、Evidence 或 13 个原写回。
- 全部通过前，README、checkpoint 与 active audit 必须保持 `Ongoing` / `completion_allowed=false`。
