# 2026-05-09 Books Writeback Queue — Independent Reconciliation

状态：`Evidence-dependent / root-serialized`。本文件不是已完成的 Books 写回，也不授权本审计 lane 修改共享 Books。

独立复核把 author queue 的 24 项收紧为 21 项可继续进入 root 写回审查；另有 3 项 false negative 必须先完成 exact-v1，不能以 abstract 直接进入 Books。

## 可继续进入 root 写回审查的 21 项

| Source Family | Corrected Owner | 为什么不是已有论点的简单重复 | 写回边界 |
| --- | --- | --- | --- |
| `SF-2026-ARXIV-2605-07135` | `PLATFORM-SECURITY` | AWI 把不可信事件文本到 agent prompt、agent-derived output 与后续 script sink 串成同一条 authority-bearing taint path。 | 只沉淀 P2A/P2S 边界、deterministic sink 与 effect-time authorization；不外推论文样本之外的 prevalence。 |
| `SF-2026-ARXIV-2605-07238` | `INFER-SCHEDULING` | FATE 将当前 placement 对 model residency、parent-output locality、prefix reuse 与 downstream reachability 的影响加入 scheduling objective。 | 保留 bounded-frontier planner 的 cost-model/solver overhead；小 DAG 或模型失配时回退简单 heuristic。 |
| `SF-2026-ARXIV-2605-07242` | `AGENT-MEMORY` | MemoRepair 把 derived-memory invalidation 从“覆盖可见条目”升级为 barrier-first descendant withdrawal、staged successor 与 validated republish。 | 完整 provenance 不可得时不得宣称 cascade 已修复，回退到隔离/重建。 |
| `SF-2026-ARXIV-2605-07330` | `TRAIN-DISTRIBUTED-TRAINING` | SparseRL-Sync 让 RL policy weight synchronization 的传输对象从完整 checkpoint 变为可证明无损的 sparse update。 | 必须绑定 topology、optimizer/update identity 与重构正确性，不能把压缩率外推为任意训练吞吐。 |
| `SF-2026-ARXIV-2605-07569` | `TRAIN-DISTRIBUTED-TRAINING` | HexiSeq 让 sequence length、heterogeneous device capacity 与 pipeline assignment 共同决定长上下文训练 plan。 | 保留 topology/sequence-mix sensitivity 与 plan reconfiguration cost。 |
| `SF-2026-ARXIV-2605-07594` | `AGENT-MEMORY` | MemCompiler 将 raw memory injection 改为按 current state 编译、验证并 materialize 的 memory view。 | 编译分析不完备或 environment revision 改变时回退 raw evidence retrieval。 |
| `SF-2026-ARXIV-2605-07689` | `TRAIN-GRPO` | binary-reward group mean centering 会在组内全同结果时饿死梯度，修正项改变 advantage 可用性的成立条件。 | 只在披露 reward/model/task 下成立；不能把局部修复当成 GRPO 的普遍最优版本。 |
| `SF-2026-ARXIV-2605-07836` | `AGENT-MCP` | MCP 风险不是单向 prompt injection，而是 tool result 与 derived state 沿双向 data flow 穿越 client/server trust boundary。 | 绑定采样 ecosystem 与 threat model；detector 仍是 sensor，不拥有授权 commit。 |
| `SF-2026-ARXIV-2605-07935` | `AGENT-MULTI-AGENT` | TraceFix 将 coordination failure 从自然语言 trace diagnosis 提升为 TLA+ counterexample 驱动的 protocol repair proposal。 | spec completeness 与 repaired implementation validation 仍是独立 Gate。 |
| `SF-2026-ARXIV-2605-08317` | `INFER-KV-CACHE` | RDKV 用共同 rate-distortion budget 联合选择 eviction 与 quantization，而非让两个局部策略各自消费 memory。 | prefill 后冻结 allocation 的假设在长 decode 或 attention shift 下可能失效。 |
| `SF-2026-ARXIV-2605-08374` | `AGENT-MEMORY` | MemQ 把 memory item、provenance DAG 与 temporal-difference credit 绑定，使 utility 可以沿 derived-state dependency 回传。 | reward/embedding locality 与 DAG 单调增长会引入陈旧 credit 和存储债务。 |
| `SF-2026-ARXIV-2605-08460` | `AGENT-MULTI-AGENT` | subagent spawn 同时复制或扩大 identity、authority、isolation 与 resource state，不能仅视为消息并行。 | role-level model 不证明实际 runtime containment；effect-time authorizer 仍须独立。 |
| `SF-2026-ARXIV-2605-08513` | `PLATFORM-SECURITY` | 单神经元干预能绕过 safety alignment，说明白盒 activation signal 只能是 sensor，不能等同安全边界。 | 七模型/两 family/单概念结果不能外推全部架构；生产控制仍需 reference monitor。 |
| `SF-2026-ARXIV-2605-08524` | `TRAIN-DISTRIBUTED-TRAINING` | FCP 将 context parallelism 从固定相邻通信推进为 topology-aware fully connected data exchange。 | arbitrary P2P/all-to-all 的 fabric 假设、buffer capacity 与 topology cost 必须进入 plan。 |
| `SF-2026-ARXIV-2605-08527` | `TRAIN-GRPO` | MARLaaS 将多租户异步 RL 拆成 rollout/service/update state，并显式暴露 policy freshness 与 KV capacity。 | serialized update 与 staleness 仍限制可扩展性，不外推作者任务集之外的稳定性。 |
| `SF-2026-ARXIV-2605-08541` | `TRAIN-PRETRAINING` | scaling-law extrapolation 还依赖 tokens-per-parameter coverage，不能只拟合 loss 与 parameter count。 | 结论受小模型、单架构与 pretraining corpus 约束；不替代真实目标规模验证。 |
| `SF-2026-ARXIV-2605-08545` | `PLATFORM-EVALUATION-SYSTEM` | final score 会掩盖 agent 在 observation、tool execution、retry 与 recovery 上的不同失败；log schema 因而属于 evaluation contract。 | tau-Bench case study 是受限示例，不能证明该 taxonomy 覆盖所有 agent runtime。 |
| `SF-2026-ARXIV-2605-08563` | `AGENT-WORKFLOW` | retry 会把失败轨迹写回 context，后续尝试不再独立；context contamination 必须进入 retry/compensation state。 | 二元 contamination 与独立性假设失效时，理论边界需重估；可回退 clean checkpoint restart。 |
| `SF-2026-ARXIV-2605-08580` | `AGENT-MEMORY` | Slipstream 让 compaction proposal 与原 context 上继续执行的轨迹并行，再以未来行为验证摘要是否可 commit。 | 独立 validator/judge 不可靠或预算不足时保留原 context、拒绝 commit。 |
| `SF-2026-ARXIV-2605-08581` | `INFER-SCHEDULING` | PRISM 联合 queue admission/scheduling 与 memory layout，证明 scheduling 和 KV/memory state 不能分别局部优化。 | 单 A800、固定模型/workload 不支持外推多 GPU 或异构 fleet。 |
| `SF-2026-ARXIV-2606-20582` | `TRAIN-DISTRIBUTED-TRAINING` | collective-aware RDMA recovery 让 packet-loss handling 理解 collective message semantics，而不是只恢复 transport bytes。 | 绑定披露 testbed/ns-3、fabric/load/topology；模拟结果不是生产 tail guarantee。 |

## 独立复核后降级为 No Change 的 3 项

- `SF-2026-ARXIV-2605-07442`：runtime-state injection 是有价值的 verifier 实现案例，但 `PLATFORM-EVALUATION-SYSTEM` 已有 stateful counterfactual、reference artifact 与 executable evidence contract。
- `SF-2026-ARXIV-2605-08346`：Force/Remove sanity checks 属于 claim sensor 的必要非充分检查；现有 Evaluation 章节已经明确 sensor、calibration 与 claim graph 边界。
- `SF-2026-ARXIV-2605-16354`：two-stage human/LLM doubly robust estimator 的样本分配问题已由 Evaluation 章节的方差分解与 rater-budget 路线承载。

## 必须先补 exact-v1 的 3 项

- `SF-2026-ARXIV-2605-08363` → `PLATFORM-SECURITY`：需要 Method、attestation/provenance verification、threat model 与 limitations。
- `SF-2026-ARXIV-2605-08565` → `INFER-TENSORRT-LLM`：需要 scale underflow、4-over-6、brute-force baseline、format/hardware scope 与 limitations。
- `SF-2026-ARXIV-2606-27379` → `PLATFORM-EVALUATION-SYSTEM`：需要 unlearning guarantee definition、reference retraining/equivalence、counterexamples 与 limitations。

这三项在 exact-v1 之前没有 Score V2 最终值，也不进入 root Books writeback。
