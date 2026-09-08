# Daily Research — 2026-08-21

**规范：** V3
**窗口：** 2026-08-20T09:00:00+08:00 ～ 2026-08-21T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T01:25:00+08:00

## 1. 结论

本窗 14 个每日来源完成重检。arXiv 官方 `new` 公告得到 409 个身份（`2608.19199`～`2608.20338`）；全批次标题逐项语义筛选后，对可能改变大模型/Infra 长期判断的条目阅读摘要，冻结 20 个材料家族。旧 8 月 20/21 报告按 submitted time 错分候选；本版将 Outcome Monitors、Beyond Imitation、Lazy Pod 归回本窗，并删除未出现在任何 official owner inventory、当前也无法取得原始身份的 `2608.20290`。候选 exact-v1 可取得，未发现 withdrawn。

长期增量集中在三条线上：调度决策必须对测量成本、SLO、cache locality 与部署状态共同负责；Agent 的 memory/tool/workflow 需要 terminal state、commit、recovery 和 policy graph；算法原型若要进入生产，必须补齐 kernel、precision、paged state 与 batching contract。11 项长期机制已经写入 Books，8 项已有覆盖，1 项仅保留日报。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 索引按本窗检查 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 入口检查 | 已检查 | 无 |
| SRC-META-AI | publication 列表检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录过滤并去重 | 已检查 | 无 |
| SRC-DEEPSEEK | Updates / Research 检查 | 已检查 | 无 |
| SRC-MOONSHOT | Blog / Research / release 检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”列表检查 | 已检查 | 无 |
| SRC-ZAI | Research 列表检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research / Blog / Publications 检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 技术博客与发布入口检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | Paper / Blog 检查 | 已检查 | 无 |
| SRC-MINIMAX | Blog / Research 检查 | 已检查 | 无 |
| SRC-ARXIV | official-announcement owner 清单；409 个身份首尾完成题摘筛选，保留 20 项 | 已检查 | 无 |

没有按需来源被触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Evaluation Context Protocol](https://arxiv.org/html/2608.19263v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 以 portable context contract 绑定 Agent evaluation 的环境、trace 与版本；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [HyperCut](https://arxiv.org/html/2608.19296v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | inter-layer DSE 先用可证明 bound 剪掉不可行 schedule；2 + 3 + 2 = 7 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Outcome Monitors](https://arxiv.org/html/2608.19303v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 对格式合法但语义失败的 tool result 发可恢复 receipt；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [HYDRA Chiplet DSE](https://arxiv.org/html/2608.19395v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 联合 chiplet composition、placement、bandwidth、batching 与 runtime policy；2 + 2 + 2 = 6 | 标准完成 | 仅报告：DSE 模型尚非可部署硬件证据 |
| [Beyond Imitation](https://arxiv.org/html/2608.19408v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 以 reasoning-progress filter 约束 teacher reward；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [The Lazy Pod That Lies](https://arxiv.org/html/2608.19412v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | lazy image pull 将启动成本后移并引入运行中 cache exhaustion；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-KSERVE，[Ch61](../../../../books/part-06-ai-infrastructure/61-kserve.md) |
| [Remember, Verify, or Ask?](https://arxiv.org/html/2608.19564v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 将 memory update 分成 persist/use-once/reverify/clarify 四种 action；3 + 2 + 3 = 8 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [FleetSieve](https://arxiv.org/html/2608.19659v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | profiling 只测会改变 resource-coupled SLO allocation 的配置；3 + 3 + 3 = 9 | 深入完成 | 整合：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [ReCache](https://arxiv.org/html/2608.19662v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | tool/skill schema 变为 composition-invariant resource KV blocks；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [CacheRoute](https://arxiv.org/html/2608.19677v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 周期计划平衡 prefix affinity 与 server load skew；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-DYNAMO，[Ch52](../../../../books/part-05-inference-system/52-dynamo.md) |
| [SafeBranch](https://arxiv.org/html/2608.19729v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | same-state branch pair 分离 embodied safety 与 task success；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：MULTIMODAL-EMBODIED-VLA，[Ch26](../../../../books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md) |
| [Thinkingbox](https://arxiv.org/html/2608.19741v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 评价 terminal backend state、依赖工具与 collateral effects，而非单次成功；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [FlashPrefill V2](https://arxiv.org/html/2608.19758v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | sparse prefill 补齐 FP8、paged KV 与 continuous batching；3 + 3 + 2 = 8 | 深入完成 | 整合：INFER-PREFILL，[Ch43](../../../../books/part-05-inference-system/43-prefill.md) |
| [Credit Without Ground Truth](https://arxiv.org/html/2608.19760v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | executed replay 显示常用 step credit 未优于匹配边际的 shuffled control；3 + 2 + 3 = 8 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [PolicyGuide](https://arxiv.org/html/2608.19861v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | policy 编译为持久图，在 user-turn boundary 主动校验进度与遗漏步骤；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [EnvHarness](https://arxiv.org/html/2608.19880v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 以 programmable wrapper 改变静态环境难度而不修改底层逻辑；2 + 3 + 2 = 7 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Manifold Drift in Flow Preference Optimization](https://arxiv.org/html/2608.20011v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | preference update 的法向位移会把 flow 终点推离 pretrained manifold；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-DPO，[Ch34](../../../../books/part-04-training-system/34-dpo.md) |
| [MidTool](https://arxiv.org/html/2608.20314v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | mid-training 数据显式覆盖 affordance、arguments、workflow 与 recovery；2 + 3 + 2 = 7 | 深入完成 | 整合：TRAIN-PRETRAINING，[Ch28](../../../../books/part-04-training-system/28-pretraining.md) |
| [Pandora's AI Model Routing Box](https://arxiv.org/html/2608.20316v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 将 specialist value estimate 的成本纳入 routing search；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Inducing Task Models from Computer-Use Traces](https://arxiv.org/html/2608.20319v1) | 2026-08-21T08:00:00+08:00 ～ 2026-08-21T09:00:00+08:00 | 从交错低层 events 恢复可审计、可复用的 symbolic task model；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |

## 4. 证据与知识整合

### [Evaluation Context Protocol](https://arxiv.org/html/2608.19263v1)

ECP 建议把 environment、tools、model、policy、trace 与 scorer 作为可移植上下文；论文偏协议提案，未证明互操作实现。Ch66 已要求冻结 evaluation artifact 与运行环境，已有覆盖。

### [HyperCut](https://arxiv.org/html/2608.19296v1)

directed hypergraph 表示跨层资源与依赖，以 coarse bound 在昂贵 intra-layer scheduling 前剪枝。**已整合：** Ch49 将 DSE 分为 feasibility bound 与 exact schedule 两阶段；早筛只能证明不值得继续，不能替代最终编译/测量。

### [Outcome Monitors](https://arxiv.org/html/2608.19303v1)

monitor 对结构合法但违反 outcome contract 的结果保留原值并发 nonbinding recovery receipt；它不执行恢复。Ch78 已写明 post-tool semantic validation、receipt 与 recovery ownership。

### [HYDRA Chiplet DSE](https://arxiv.org/html/2608.19395v1)

framework 联合 chiplet composition、placement、bandwidth、batch 与 routing policy；结果主要来自设计空间模型，不能当作量产硬件证明，故仅报告。

### [Beyond Imitation](https://arxiv.org/html/2608.19408v1)

独立 progress rank 过滤与 teacher output 相似却不推进推理的 token reward；其判断器仍可能偏置。Ch33 已将 teacher signal、environment outcome 与 process evidence 分权。

### [The Lazy Pod That Lies](https://arxiv.org/html/2608.19412v1)

KServe 上 lazy mount 缩短 first prediction，但完整读取更慢且可能在运行中耗尽 cache。Ch61 已将 mount-ready、model-readable、resident 与 steady-state 分开，已有覆盖。

### [Remember, Verify, or Ask?](https://arxiv.org/html/2608.19564v1)

140 primary cases 将 interaction-derived fact 的动作分为 persist、current-only、reverify、clarify。**已整合：** Ch77 的 commit gate 不只判断真假，还判断 durability 和用户授权；不确定时保留 session state 或追问。

### [FleetSieve](https://arxiv.org/html/2608.19659v1)

profiling 比较 conservative/optimistic fleet allocation，只继续测量会缩小决策 gap 的 TP/replica 配置。**已整合：** Ch56 把 profiling 作为 sequential decision；停止条件绑定 SLO/resource allocation 稳定，而非遍历完整网格。

### [ReCache](https://arxiv.org/html/2608.19662v1)

resource-local positions 与 resource-wise attention 产生可跨顺序组合的 tool/skill KV blocks，再按 layer/head route 和字段裁剪。**已整合：** Ch45 增加 composition-invariant cache branch；换取 cross-resource interaction 限制，identity 必须含 schema/version/position policy。

### [CacheRoute](https://arxiv.org/html/2608.19677v1)

周期计划把热 prefix 放入稳定 warm set，并在 affinity 与 expected load 间选择目标；60 H100 结果受 workload 限制。Ch52 已完整承载 warm-set、shadow replay 与 fallback。

### [SafeBranch](https://arxiv.org/html/2608.19729v1)

从同一 safety-critical state 配对原 action 与安全替代，避免任意轨迹差异污染信号。Ch26 已保留 simulator rollback、单 seed 与物理不可逆边界。

### [Thinkingbox](https://arxiv.org/html/2608.19741v1)

sandbox 保存完整 MCP trace，并以 terminal backend state、policy steps 与 collateral effects 验收。**已整合：** Ch66 将一次 success 扩展为 repeat reliability + final state + side-effect contract。

### [FlashPrefill V2](https://arxiv.org/html/2608.19758v1)

V2 在稀疏 pattern 上增加 mean correction，并补 FP8、paged KV 与 continuous batching。**已整合：** Ch43 区分算法 sparsity 与 production path；index/discovery、layout、precision、batch compatibility 和 fallback 缺一不可。

### [Credit Without Ground Truth](https://arxiv.org/html/2608.19760v1)

ALFWorld executed replay 估计 step contribution；judge/logprob/confidence 在可靠性修正后未显示稳定增量。**已整合：** Ch33 要求 credit signal 与 marginal-matched shuffled control 比较，step correctness 不等同 counterfactual contribution。

### [PolicyGuide](https://arxiv.org/html/2608.19861v1)

policy 编译为 workflow graph，verifier 在每个 user turn 依据 persisted state 指出禁止动作和遗漏前置。**已整合：** Ch81 将 policy compliance 变为 graph state，不由 action-local guard 独自承担。

### [EnvHarness](https://arxiv.org/html/2608.19880v1)

wrapper 通过标准接口改变 static environment 的任务、扰动与反馈，同时保留底层逻辑。**已整合：** Ch33 分离 base environment identity 与 harness transformation；训练/评价必须记录两者及 verifier。

### [Manifold Drift in Flow Preference Optimization](https://arxiv.org/html/2608.20011v1)

理论指出 preference displacement 的 normal component 会离开 pretrained support，并以 temperature anchor 缓解；仅覆盖 flow matching。Ch34 已写明 preference optimization 的 support drift 与 anchoring，已有覆盖。

### [MidTool](https://arxiv.org/html/2608.20314v1)

数据管线把 web/PDF/code 与真实 API、MCP skill、document workflow 合成 affordance、argument 和 recovery supervision。**已整合：** Ch28 将 tool use 作为 mid-training capability，而非只在 SFT 学格式；数据 contamination 与 executable verification 必须单列。

### [Pandora's AI Model Routing Box](https://arxiv.org/html/2608.20316v1)

formalization 把 specialist value 与获得该 estimate 的 inspection cost 一并优化；Gaussian assumption 限制实际部署。Ch56 已覆盖 staged estimator、routing cost 与 stop decision。

### [Inducing Task Models from Computer-Use Traces](https://arxiv.org/html/2608.20319v1)

TMI 从 interleaved screenshots/actions 恢复 task boundary、state 和 reusable symbolic process。**已整合：** Ch81 区分 observed trace 与 induced workflow；后者必须带 provenance、confidence 和人工/执行验证，不能直接获得执行权。

## 5. 缺口与下一步

无

`2608.20290` 未出现在官方 owner inventory，已按伪身份线索从候选移除，不支持任何结论。11 项 Books 增量已写入相应机制正文，没有剩余可执行工作。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核检查了 409 个 official-announcement 身份的首尾覆盖、20 项准入与漏项、exact-v1/withdrawn、§3/§4 及 Books 实际落点。确认 11 项而非 10 项需要并已完成整合，且所有新增机制位于对应章节 `Review notes` 之前；机器校验与 diff 检查通过。
