# Lab 11 — Distributed Inference

## Lab Question

推理状态跨 engine、节点和 Prefill/Decode phase 后，怎样管理 locality、freshness、transfer、routing 与 failure recovery？

## Why This Lab Exists

单 Engine 拥有完整 request/KV state，简单但受单机 memory/compute 限制。Replica 扩展吞吐，prefix-aware routing
提高 reuse；PD 分离匹配 phase 资源需求，却让 request state、KV、selection summary 与 ownership 跨网络传播。

## Books / Stable Node Mapping

| Stable Node | Chapter | Role in This Lab |
| --- | --- | --- |
| `INFER-SGLANG` / `INFER-DYNAMO` | Ch51～52 | Structured/distributed runtime cases |
| `INFER-KSERVE-TOPOLOGY` | Ch53 | Declarative serving topology handoff |
| `INFER-PD-DISAGGREGATION` | Ch55 | Phase split 与 KV transfer owner |
| `INFER-SCHEDULING` | Ch56 | State-aware selection owner |
| `PLATFORM-GATEWAY` | Ch62 | Request policy boundary |

## Prerequisites

- 完成 Lab 10；理解网络延迟、membership、consistent identity 与 partial failure。

## System Under Test

多个 Engine worker、router/selector、KV transfer path、membership registry 和 recovery controller。Worker 拥有
authoritative KV payload；selector 只拥有 versioned summary；gateway 拥有 admission/policy，不拥有 cache truth。

## Baseline

Round-robin 到完整 model replicas，每个请求在单 worker 完成。它忽略 locality，但 failure domain 清楚、恢复简单。

## Step-by-Step Experiments

1. 启动两个 engine replicas，固定 model/tokenizer/revision 与 endpoint identity。
2. 比较 round-robin、queue/load-aware 与 prefix/KV-aware routing，验证 summary 可能 stale。
3. 分离 Prefill/Decode workers，定义 transfer manifest、generation、checksum 与 destination validation。
4. 模拟 KV transfer 与 overlap，比较 recompute、local hit、remote hit 的 cost region。
5. 加入 membership/freshness、retry、duplicate request、worker loss 与 partial transfer recovery。
6. 在 burst、long prompt、heterogeneous hardware 下联合测量 selection、network、memory 与 SLO。

## Expected Artifacts

- Distributed request trace、worker/summary identity、KV transfer manifest 与 recovery state machine。
- Lab 12 可复用的 serving topology desired/observed status。

## Invariants

- Selector summary 不替代 worker payload truth；destination 在消费前重新验证 identity/freshness。
- Retry/duplicate 不产生重复可见 token 或双重 side effect。
- Transfer、route、membership 与 request generation 可追溯。

## Failure Injection

- Worker crash、stale summary、network partition、partial/corrupt KV、route change、heterogeneous slowdown。
- 在 Prefill 完成但 Decode 未接管、stream 已开始、membership 更新并发时触发失败。

## Measurements

- TTFT/TPOT/E2E、route decision time、queue、KV hit/transfer/recompute、network bytes。
- Recovery time、duplicate/split-brain prevention、freshness miss 与 SLO goodput。

## Acceptance Criteria

- [ ] Round-robin、load-aware、state-aware routing 在同一 trace 下比较。
- [ ] Remote KV 只有通过 identity/freshness/checksum 后才能消费。
- [ ] Worker/transfer/selector failure 不产生静默错误或重复提交。
- [ ] 报告指出 PD/locality 何时不值得网络与控制面成本。

## Trade-offs and Alternatives

Replica 保持请求局部性但复制全部 weights；PD 匹配 phase，却增加 KV transfer 与跨池 failure。State-aware routing
提高 reuse，也会因 stale summary、hot prefix 和 fairness 产生新问题。低 QPS/短 prompt 下 round-robin 仍最稳健。

## Reflection Questions

1. Cache summary 应包含多少信息，才不把 control plane 变成第二份真相？
2. Remote hit 与 recompute 的决策需要哪些 workload/hardware 条件？
3. 请求跨 worker 后，谁拥有取消、stream 和 retry authority？

## Next Lab Handoff

向 Lab 12 交付 versioned serving topology、worker capability、desired/observed state、route evidence 与 recovery status；
平台将把这些机制包装为多团队可复用控制对象。

