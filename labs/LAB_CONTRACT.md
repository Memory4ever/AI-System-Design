# Lab Contract：怎样把实践变成可信认知

## 核心原则

一次 Lab 不是 Demo，也不是 benchmark 截图。它必须把一个设计判断变成可复现、可比较、可失败的证据链：

```text
假设
→ 可复现 Baseline
→ 最小机制实现
→ correctness 检查
→ measurement
→ failure injection
→ 与替代方案比较
→ 写下证据边界
→ 进入下一 Lab
```

## Workload Contract

任何性能、质量或可靠性结论都必须绑定：

- code revision、依赖与随机种子；
- dataset / prompt / trace identity 与 split；
- model、tokenizer、precision、quantization 与 checkpoint identity；
- hardware、topology、driver/runtime 与 device count；
- input/output length、batch、concurrency 与 arrival pattern；
- warmup、重复次数、统计量与置信区间；
- quality threshold、correctness invariant 与 SLO；
- timeout、retry、cache、failure injection 与恢复策略。

未披露字段写 `Not Disclosed` 或 `Not Controlled`，不能用默认值补猜。

## 每次实验的八步循环

### 1. 写下可证伪假设

假设必须指出改变的机制、预期方向和成立条件。例如：“在 consumer 只需要充分统计量时，减少 collective payload
可降低通信字节；若固定 latency 主导，则 wall-clock 未必改善。”不要写“方案 B 更快”。

### 2. 建立最简单 Baseline

Baseline 优先选择容易解释、容易验证的旧方案。它必须是有效设计分支，而不是故意写慢的稻草人。

### 3. 实现最小机制差异

一次实验只改变一个主要变量。若同时改变 model、kernel、batch 和 scheduler，结果只能证明联合 recipe，不能归因
于其中一个组件。

### 4. 先证明 Correctness

性能测试前至少包含 reference output、shape/dtype、数值误差、state transition、ordering、idempotency 或 rollback
检查。近似算法还要声明 quality envelope。

### 5. 测量而不是挑选数字

同时报告中心趋势、尾部、方差、资源使用和质量。保留失败运行及排除理由，不只挑最好的一次。

### 6. 主动破坏假设

改变 scale、length、concurrency、topology、data distribution 或 injected failure，寻找新机制失效的位置。

### 7. 比较收益与新债务

记录新增 state、metadata、copy、synchronization、calibration、security、observability 与 recovery 成本，并指出旧方案
在哪些条件下仍然更合理。

### 8. 写下 Handoff

明确下一 Lab 能消费的 artifact、contract 与 open questions。不可复用的截图不算 handoff。

## Evidence Level

| Level | 含义 | 可支持的结论 |
| --- | --- | --- |
| E0 | 想法或未运行草图 | 只能记录问题 |
| E1 | 单次可运行结果 | 证明路径可能可行 |
| E2 | 可复现 correctness + controlled comparison | 支持该 workload 下的机制判断 |
| E3 | 多条件 sensitivity + failure/recovery evidence | 支持适用边界与 trade-off |
| E4 | 独立复现或生产观测 | 支持更稳定的工程结论，仍不能无条件外推 |

## 推荐实现边界

- 默认 Python 3 + PyTorch，先提供 CPU reference path。
- GPU 优化在 correctness 固定后引入；Triton/CUDA 属于 execution branch，不改变模型语义。
- 分布式实验先在单机多进程验证 state/collective contract，再扩展到多节点。
- Docker/Kubernetes/Go 只在 Lab 12 以后、或确实需要控制面语义时引入。
- 不把云厂商账号、专有硬件或大模型 API 作为完成基础 Lab 的必要条件。

## 完成门禁

一个 Lab 只有同时满足以下条件才完成：

- Baseline 与新机制都能从干净环境复现；
- correctness invariants 有自动或明确的人工验证证据；
- 至少一个预期收益和一个 failure boundary 被观测；
- 报告区分事实、测量、推断和未证明内容；
- 旧方案的成立条件和新方案的新增债务均被记录；
- 产物满足 Next Lab Handoff。

