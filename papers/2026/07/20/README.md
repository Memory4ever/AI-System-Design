# Daily Research — 2026-07-20

**规范：** V3
**窗口：** 2026-07-19T09:00:00+08:00 ～ 2026-07-20T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-10T17:30:00+08:00

## 1. 结论

本窗口按 first-public owner 得到 357 条 arXiv 原始身份。逐条读取标题与完整摘要后，冻结 5 个候选；旧稿的 62 个候选不作为新分母，其中 57 个旧候选因只提供局部方法/benchmark、垂直应用或没有改变长期系统判断而降回准入前关闭。原始证据保留，但不在正文候选表继续制造重要性错觉。

保留材料集中在可迁移状态、训练/推理执行计划、跨层资源约束、证据与安全边界。每项都已用旧稿保存的 exact-v1 primary evidence 重新核对机制与反证；没有用标题关键字替代语义判断，也没有把能映射 ROADMAP 当作准入理由。独立复核已经把“来源存在”和“正文已承载”分开，并确认两项正文增量已进入各自 owner 章节且保留旧方案与回退边界。

## 2. 来源覆盖

当前登记的机构日源在 2026-09-07 才纳入合同；按历史生效边界不倒推本窗口。表中仍逐项列出，避免把‘不适用’误读为已扫描。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ANTHROPIC | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-GOOGLE-AI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-META-AI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-QWEN | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-DEEPSEEK | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-MOONSHOT | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-TENCENT-HUNYUAN | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ZAI | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-BYTEDANCE-SEED | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-BAIDU-ERNIE | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-XIAOMI-MIMO | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-MINIMAX | 登记生效晚于本历史窗口；历史重建不倒推新入口 | 不适用 | 无 |
| SRC-ARXIV | [exact-v1 HTML](https://arxiv.org/)；本窗 357 条 identity 逐条 title + 完整摘要语义筛选；旧稿 exact-v1 Method / Evaluation / Limitations 仅作可核实证据种子 | 已检查 | 无 |

本次排除 AI for Science、纯垂直应用、只改局部任务指标以及没有系统状态/控制/评价契约增量的工作。withdrawn 身份不进入候选；本组没有保留 withdrawn family。

## 3. 候选与判断

评分依次为 Design Delta + System Reach + Durability；7～9 分深入审阅，5～6 分标准审阅。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers](https://arxiv.org/html/2607.15456v1) | 2026-07-20T08:00:00+08:00 | `INFER-KV-CACHE`；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[目标章](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving](https://arxiv.org/html/2607.15621v1) | 2026-07-20T08:00:00+08:00 | `MULTIMODAL-EMBODIED-VLA`；2 + 3 + 2 = 7 | 深入完成 | 仅报告：受限机制案例，不单独改变当前章节主结论 |
| [ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing](https://arxiv.org/html/2607.15899v1) | 2026-07-20T08:00:00+08:00 | `PLATFORM-GATEWAY`；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-GATEWAY，[目标章](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [Every Microsecond Matters: Achieving Near Speed-of-Light Latency in GPU Collectives](https://arxiv.org/html/2607.16100v1) | 2026-07-20T08:00:00+08:00 | `INFER-TENSORRT-LLM`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM`，[目标章](../../../../books/part-05-inference-system/49-tensorrt-llm.md) 已有 latency floor、barrier 与 failure contract |
| [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/html/2607.16184v1) | 2026-07-20T08:00:00+08:00 | `INFER-GPU-MEMORY`；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：`INFER-GPU-MEMORY`，[目标章](../../../../books/part-05-inference-system/54-gpu-memory.md) 已有 bit-plane、desired/committed precision 与 KV pressure 正文 |

## 4. 证据与知识整合

### [Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers](https://arxiv.org/html/2607.15456v1)

**机制。** 权重共享的 looped Transformer 不增参数，却为每次迭代生成不同 K/V；保存全部 loop state 使 memory 随推理深度增长，简单复用最后一轮又丢掉 loop-specific 信息。Looped Latent Attention 存低维 K/V latent，读取时按 loop 重建。

**证据边界。** 在论文模型、cache budget 与任务上，per-head codec 优于 head-axis MLA、跨层共享、KV 量化和 final-loop reuse，支持“跨 loop 状态低秩但不能坍缩为单一状态”。未证明相同秩/误差边界适用于普通 Transformer、所有长度或生产并发。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.15456v1#A5 — Appendix E Design-ablation detail; https://arxiv.org/html/2607.15456v1#S5.SS0.SSS0.Px5 — Design ablations.。Evaluation：https://arxiv.org/html/2607.15456v1#A1 — Appendix A Experimental details; https://arxiv.org/html/2607.15456v1#A1.SS0.SSS0.Px4 — Evaluation suite and protocols.。Limitations / counterevidence：https://arxiv.org/html/2607.15456v1#S8 — 8 Discussion; https://arxiv.org/html/2607.15456v1#S9 — 9 Conclusion。

**Trade-off。** 压缩降低 footprint，却增加重建 compute、codec 校准和近似误差；loop 差异大时需升 rank 或保留原 K/V。

**Books：已整合。** `INFER-KV-CACHE` 的误差预算主线已将 cross-loop reuse 限定在受校准的 latent 共享：loop/iteration identity 与读出误差共同决定能否提交旧状态，越界时回退 FullCache/重算。

### [Think at 5 Hz, Act at 20 Hz: Asynchronous Fast-Slow Vision-Language-Action Inference for Closed-Loop Driving](https://arxiv.org/html/2607.15621v1)

**机制。** 大模型语义推理可低频刷新，底层控制却需高频反应；同一模型承担两种时钟会阻塞控制。论文将慢速语义/轨迹更新与快速动作控制解耦，后者以固定成本消费最近高层状态。

**证据边界。** 作者在 driving workload 和单张消费 GPU 上报告 waypoint error 降低与约 32ms/tick。未证明 open-loop error 等于道路安全，也未覆盖传感延迟、状态过期和极端场景。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.15621v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.15621v1#S4 — 4 Experiments; https://arxiv.org/html/2607.15621v1#S4.SS6 — 4.6 Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.15621v1#S5 — 5 Conclusion。

**Trade-off。** 快慢分层提高频率，却新增 plan version/freshness 与切换瞬态；过期时应减小 action horizon 或回退安全控制。

**Books：仅报告。**`MULTIMODAL-EMBODIED-VLA` 已有 fast/slow 与 freshness contract；这是 driving-specific 实例。

### [ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing](https://arxiv.org/html/2607.15899v1)

**机制。** 多供应商 failover 若只重发当前请求，备端不拥有原对话、工具与策略状态，HTTP 成功仍会语义断链。论文用 history-forwarding proxy 显式转移 conversation state，并以 context preservation 衡量切换。

**证据边界。** 750 次论文设定的 failover 中，stateful proxy 报告 99.20% preservation，stateless baseline 近零。结果依赖作者对话集和 LLM judge；未证明 tool state、provider policy、隐私许可或长历史截断时无损迁移。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.15899v1#S3 — 3 System Design; https://arxiv.org/html/2607.15899v1#A1 — Appendix A LLM Judge System Prompt。Evaluation：https://arxiv.org/html/2607.15899v1#A2 — Appendix B Extended Results: Per-Run CPR Stability; https://arxiv.org/html/2607.15899v1#S2.SS2 — 2.2 LLM Evaluation and LLM-as-Judge。Limitations / counterevidence：https://arxiv.org/html/2607.15899v1#S6 — 6 Discussion and Systems Failure Modes; https://arxiv.org/html/2607.15899v1#S7 — 7 Limitations。

**Trade-off。** 状态转移提高连续性，却增加数据暴露、token、schema 兼容和重复副作用风险；不可迁移时应显式降级而非假装透明。

**Books：已整合。** `PLATFORM-GATEWAY` 的 “Stateful Failover” 正文已把 conversation、tool、policy 与 provider-specific serialization 纳入可迁移状态和授权边界；不兼容时拒绝透明切换、显式重建 Context 或要求用户确认。

### [Every Microsecond Matters: Achieving Near Speed-of-Light Latency in GPU Collectives](https://arxiv.org/html/2607.16100v1)

**机制。** Decode 每 token 触发多个小 collective；payload 小时固定同步/barrier 开销主导，峰值带宽优化无效。论文以 barrier-free protocol 和低延迟 API 减少启动协调，使控制流接近互联传播下界。

**证据边界。** 微基准在论文硬件/消息范围将延迟压到其 speed-of-light 下界的 7% 内，支持固定协议开销是瓶颈。未证明端到端吞吐或 tail latency 同比改善，也未覆盖跨拓扑拥塞与故障。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16100v1#S4 — IV Designing Barrier-Free Collectives; https://arxiv.org/html/2607.16100v1#S5 — V Low-Latency API Design。Evaluation：https://arxiv.org/html/2607.16100v1#S7 — VII Microbenchmarks; https://arxiv.org/html/2607.16100v1#S7.SS1 — VII-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.16100v1#S10 — X Conclusion; https://arxiv.org/html/2607.16100v1#S9 — IX Related Work and Discussion。

**Trade-off。** 去 barrier 降延迟，却把 ordering、progress 与错误处理交给协议/调用者；复杂 collective 或强同步需求下成熟路径仍合理。

**Books：已有覆盖。** `INFER-TENSORRT-LLM` 已明确小 payload Decode 的固定同步成本可主导、barrier-free path 必须承担 ordering/progress/failure contract，并保留常规 collective 回退；本材料只增加硬件受限实证。

### [PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization](https://arxiv.org/html/2607.16184v1)

**机制。** MoE expert weights 与 KV cache 争用 HBM；静态量化把质量损失固定在 artifact 上，无法随 KV 压力变化。PagedWeight 把 expert weight 组织为可切换精度页，以 desired precision 控制计划，以 committed precision 表示 kernel 可消费状态。

**证据边界。** 作者在所测 MoE/硬件上报告最高 72% memory 节省、1.94× throughput 和同预算质量改善；均为配置绑定结果。未证明 prompt-wise sensitivity 可稳定预测，也未覆盖所有格式、并发/SLO 或频繁切换抖动。

**审阅定位。** Method / identity：https://arxiv.org/html/2607.16184v1#S2.SS1 — 2.1 Mixture-of-Experts Architecture and Routing Imbalance; https://arxiv.org/html/2607.16184v1#S3 — 3 PagedWeight System。Evaluation：https://arxiv.org/html/2607.16184v1#S4 — 4 Experimental Methodology; https://arxiv.org/html/2607.16184v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.16184v1#S7 — 7 Conclusion。

**Trade-off。** 动态精度把 HBM 转给 KV，却增加转换开销、估计误差和 desired/committed race；不稳定时应固定保守精度或拒绝超量 admission。

**Books：已有覆盖。** `INFER-GPU-MEMORY` 已把 MoE expert bit-plane 建模为 page，并区分 desired/committed precision：降精度先提交再释放，升精度先加载再提交，kernel 只读 committed state；该 family 已真实进入正文。

## 5. 缺口与下一步

无

无 external Materials Request。全部保留候选均可访问 exact-v1；旧候选降级不会删除原始证据。本日所需 Books 写入和写后语义审计均已完成；若后续出现具体 false positive、false negative 或来源更正，只重开对应 family。

准入闭合账目：raw identities=357；旧候选=62；V3 候选=5；本轮从旧候选降级=57。准入前关闭的共同原因是：局部指标或单任务方法没有持久系统增量、垂直应用/AI for Science 越界、benchmark 未改变 evaluation/deployment contract，或机制已被同日更强材料覆盖。

## 6. 复核

复核者：非作者独立复核（/root/aug11_20，2026-09-10）。

结论：通过

写后复核确认 `SF-2026-ARXIV-2607-15456` 已进入 `INFER-KV-CACHE` 的跨迭代误差预算正文，`SF-2026-ARXIV-2607-15899` 已进入 `PLATFORM-GATEWAY` 的 Stateful Failover 正文；两处均有机制、未证明边界、代价和显式回退，不是 trace 或 Review notes 冒充整合。
