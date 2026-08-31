# 2026-05-03 Current-Books Fresh-Compare Challenge

本文件是给独立 reviewer 的 challenge set，不是最终 Books Decision，也不替代 274/274 screening 与 36/36 exact-v1 audit。作者队列中的 22 个 `Integrate` 不能直接写回；当前 Books 已吸收 2026 年 6—8 月机制，必须重新比较语义 owner，而不是只比较论文名。

## 明确需要降级复核

- `SF-DATA-CONSTRAINED-SCALING-LAW`：Ch28 已明确写入 unique-token volume、repetition、effective parameters、sparsity 与 data-saturation boundary；默认应为 `No Change — Existing Coverage`，除非 exact-v1 存在当前正文未覆盖的不同 state/control delta。
- `SF-LORA-COMPOSITION-RELIABILITY`：Ch30 已要求 adapter composition/merge/routing 重新 Evaluation，并覆盖 compatibility、组合分布与 promotion；需证明 multi-view reliability audit 改变了 canonical owner，而不是新增 evaluator 名称。
- `SF-AGENT-SAFETY-SEARCH-MEASUREMENT`：Ch66 已有 attack-budget risk curve、search/sampling coverage 与 residual-risk 语义；需证明 likelihood-mass accounting 仍有缺口，否则降级。
- `SF-AUTONOMOUS-TEST-REPAIR-VALIDATION-BOUNDARY`：Ch66 已把 Agent-authored tests 的 assertion/oracle strength、execution path 与 failure discriminativeness 纳入 release gate；需证明 test-intent inventory/scope-diff 是独立新机制，否则降级。
- `SF-SENTINEL-VLA-STATUS-CONTROL`、`SF-VLA-ADAPTIVE-TEST-TIME-COMPUTE`、`SF-TAIL-SAFE-RUNTIME-MONITOR`：Ch26 已有 uncertainty-aware controller、independent safety gate、same-state recovery、failure prediction 与 conservative fallback。必须逐项证明 status state machine、relative critic 或 empirical safe-set 改变不同状态所有权；不能把相近 VLA monitor 论文拆成三个重复段落。

## 可能存在真实增量，但必须与现有主线合并

- `SF-COMPUTE-OPTIMAL-TOKENIZATION`：比较 Ch11 已有 byte fallback 与 token lifecycle；只有把 byte 作为跨 tokenizer 的 information/scaling denominator，并连接 compute/latency，才构成 delta。
- `SF-VISUOMOTOR-EXECUTION-GUARANTEE`：与 Ch26 现有 safety envelope、trajectory alarm 和 corrective branch 合并；只保留 demonstration-derived safe-set、invariance check 与 minimally projected recovery 中尚未覆盖的部分。
- `SF-ACTIVATION-GRADIENT-COMPRESSION`：Ch36 当前未见 operator-aware activation-gradient compression；核验 linear/nonlinear exactness、variance、memory 与 rematerialization 边界后可保留。
- `SF-PIXEL-LEVEL-RAG-EVIDENCE-CHAIN`：Ch76 当前未见 page screenshot/region/bounding-box evidence identity；保留 locator 与 entailment/authority 分离。
- `SF-CONFOUNDED-LOG-EVALUATION`：Ch66 有 confound measurement trace，但需确认正文是否已有 OBS/EXP/SIM causal-identification Gate；只补未覆盖的 estimator assumptions 和 multi-round mediator state。
- `SF-VUDA-CUDA-VULKAN-SHARING`：Ch63 已有 MIG/MPS/time-slicing，但未见 cross-API spatial-sharing/address-space contract；可保留 API/driver/synchronization 边界，不保留产品 headline。
- `SF-LONG-FORM-LENGTH-VOLATILITY`：Ch44 当前未见 output-length distribution/variance 作为 SLO identity；可保留 mean quality 与 tail/stop contract 分离。
- `SF-AUTOREGRESSIVE-CREDIT-ATTRIBUTION-BARRIER`：Ch76 当前未见 token-level attribution 不可组合与 post-hoc retrofit cost；保留 negative result 及 provenance-at-admission 结论。
- `SF-NOTEBOOK-REPRODUCIBILITY-STATE-GATE`：Ch81 有 versioned notebook，但需补 clean-state top-to-bottom reference、cell read/write receipt 与 stale-state Gate；外部副作用未知时回退 clean rerun/container。
- `SF-MULTIAGENT-PARETO-COMPUTE-ALLOCATION`：Ch82 已有 coordination tax、single-agent baseline 与并行分支；仅在 equal-budget quality–token/latency/cost Pareto admission 未被覆盖时保留短 delta。
- `SF-AGENT-GENERATED-VERIFIED-COMPILER`：与 Ch66 executable evidence、test-strength 和 proof boundary 合并；分别冻结 tests、translation certificate、machine proof 的 authority，不重复“tests 不是证明”。
- `SF-DITRON-DISTRIBUTED-TILING`：Ch49 有单设备 tiling 与 execution plan；若 exact-v1 真正补足 compiler-plan/runtime-topology/health handoff，则保留 hierarchical distributed tiling。
- `SF-RECURSIVE-STATE-TERMINATION`：Ch80 已有 max-iterations；只保留 typed epistemic state/order-gap sensor 与 truth/evidence Gate 的新部分。
- `SF-PRUNING-BEHAVIORAL-REGRESSION`：与 Ch66 现有 compression/release evidence 比较，只保留 dense→pruned item-level transitions、fairness/calibration slice 与真实 sparse-kernel/storage Gate 的缺口。
- `SF-POLICY-CARRIAGE-INTEGRITY`：与 Ch75 现有 provenance/fail-closed Context policy 比较；只有 active-policy-set completeness 和 assembly-before-action invariant 未覆盖时保留。

## Independent acceptance

独立 reviewer 必须：

1. 重读每个 target 及相邻章节的当前版本；
2. 将重复项降级为 `No Change — Existing Coverage` 并引用具体段落；
3. 对保留项合并同 owner 的重叠机制，不按论文一项一段；
4. 只有 full-screen false-negative/false-positive、exact-v1 claim boundary 和 current-Books compare 全部无 finding，才把最终 queue 交给 root 串行写回。
