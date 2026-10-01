# Daily Research — 2026-09-15

**规范：** V3
**窗口：** 2026-09-14T09:00:00+08:00 ～ 2026-09-15T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-21T12:08:40+08:00

## 1. 结论

本窗真正值得长期保留的增量集中在四条链路：一是 KV 从“单一、固定驻留的 token state”演进为可检索、可重构、可跨副本共享且必须携带 identity/同步语义的状态；二是跨机房 PD、MoE 权重/KV/host/flash 与 operator placement 共同把推理资源边界从静态拓扑改为运行时控制；三是 Agent 的 memory、handoff、授权、工具选择与 external effect 不能继续交给模型自觉；四是模型升级、GRPO filtering、预算、persistent identity、guardrail 与 speculative exactness 的评价对象必须从平均分扩展到可证伪的发布合同。

arXiv 官方 `Tue, 15 Sep 2026` 单日公告在 12 个项目相关分类中共有 1,064 个跨分类去重身份。其中 12 个是既有论文的 cross-list/replacement 事件，不改变首次公开归属；其余 1,052 个中，737 个由标题即可明确关闭，315 个读取完整题摘后保留 45 个候选、关闭 270 个。13 个模型机构日源另发现 1 个影响部署版本语义的 DeepSeek 事件。因此本窗候选分母冻结为 46 个材料家族；45 项 exact-v1 与 1 项官方说明均已完成相应 Evidence Review。逐身份闭合见 [`denominator-closure.tsv`](./_sources/denominator-closure.tsv)，恢复项审阅见 [`evidence-review.md`](./_sources/evidence-review.md)。

作者侧 Books 判断已经完成：30 项需要在现有 owner 中补充语义增量，16 项由现有正文充分承载。30 项均已按唯一 owner 合并写入机制正文；本次定点返修恢复的 7 项中，ForgeTrain、IntentCap、BigMoMo 与 Loop-Back Authority 四项完成新增写入，另外三项由现有正文覆盖。精确输入见 [`books-queue.md`](./_sources/books-queue.md)。非作者独立语义复核已核对候选账目、证据边界、关闭理由和实际正文绑定，本日报完成。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| `SRC-OPENAI` | [Research Index](https://openai.com/research/index/) 相邻发布日期；窗口前最近条目为 9 月 10 日，本窗 0 项 | 已检查 | 无 |
| `SRC-ANTHROPIC` | [Research](https://www.anthropic.com/research) 发布列表；相邻条目为 9 月 10 日与 17 日，本窗 0 项 | 已检查 | 无 |
| `SRC-GOOGLE-AI` | [DeepMind Publications](https://deepmind.google/research/publications/) 与 Google Research 目录相邻日期，本窗 0 项 | 已检查 | 无 |
| `SRC-META-AI` | [Meta AI Research Results](https://ai.meta.com/results/) 日期列表；窗口前最近条目为 9 月 7 日，本窗 0 项 | 已检查 | 无 |
| `SRC-QWEN` | [Qwen Blog](https://qwenlm.github.io/) 与官方更新目录；窗口前最近研究/更新为 9 月 10 日，本窗 0 项 | 已检查 | 无 |
| `SRC-DEEPSEEK` | [V4.1-Flash 官方说明](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) 的生效时刻：2026-09-14T04:00:00Z；1 个当窗部署合同事件 | 已检查 | 无 |
| `SRC-MOONSHOT` | [Kimi Platform Blog](https://platform.kimi.com/blog) 与 MoonshotAI 官方组织发布入口，本窗 0 项 | 已检查 | 无 |
| `SRC-TENCENT-HUNYUAN` | [Hunyuan Research](https://hunyuan.tencent.com/research)“全部”列表及官方仓库；相邻公开项不落窗，本窗 0 项 | 已检查 | 无 |
| `SRC-ZAI` | [智谱 Research](https://www.zhipuai.cn/zh/research) 时间排序列表与官方发布说明，本窗 0 项 | 已检查 | 无 |
| `SRC-BYTEDANCE-SEED` | [Seed Research](https://seed.bytedance.com/en/research) Blog 与 Publications 列表，本窗 0 项 | 已检查 | 无 |
| `SRC-BAIDU-ERNIE` | [ERNIE Blog](https://ernie.baidu.com/blog/zh/) 时间列表与官方仓库发布入口，本窗 0 项 | 已检查 | 无 |
| `SRC-XIAOMI-MIMO` | [MiMo](https://mimo.xiaomi.com/) 与 XiaomiMiMo 官方组织发布入口，本窗 0 项 | 已检查 | 无 |
| `SRC-MINIMAX` | [MiniMax Research](https://www.minimax.io/blog) 中英文时间列表与官方组织入口，本窗 0 项 | 已检查 | 无 |
| `SRC-ARXIV` | 官方 `Tue, 15 Sep 2026` 公告块；`cs.CL/LG/DC/AI/CV/RO/AR/PL/OS/PF/IR/MA`；跨分类去重 1,064，12 个旧 ID 事件剔除；1,052 个本窗身份全部完成标题筛选，315 个含义不明确/可能贡献项完成完整摘要语义筛选；冻结 45 个候选，45/45 exact-v1 证据审阅完成 | 已检查 | 无 |

原始题摘集合、exact-v1 HTML 与被关闭项身份保存在 [`_sources/`](./_sources/)；这些过程材料不替代下文证据判断。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [DeepSeek V4.1-Flash alias migration](https://www.deepseek.com/en/news/deepseek-v4-1-flash/) | 2026-09-14T12:00:00+08:00 | 旧模型名在不变请求接口下开始解析到新模型，说明 mutable alias 本身是部署状态而非模型身份；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-MODEL-REGISTRY` [Ch59](../../../../books/part-06-ai-infrastructure/59-model-registry.md) |
| [PDD（arXiv:2609.13161v1）](https://arxiv.org/html/2609.13161v1) | 2026-09-15T08:00:00+08:00 | 跨机房 KV 传输从阻塞依赖变成 relay decode 可遮蔽流水，并以 token-only handoff 转移控制权；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-PD-DISAGGREGATION` [Ch55](../../../../books/part-05-inference-system/55-pd-disaggregation.md) |
| [Self-Indexing Attention（arXiv:2609.13205v1）](https://arxiv.org/html/2609.13205v1) | 2026-09-15T08:00:00+08:00 | 同一 sign-magnitude 表示同时承担 prefill/decode 稀疏检索索引与外部压缩载体，改变“索引是额外 metadata”的假设；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Grouped Value Attention（arXiv:2609.13285v1）](https://arxiv.org/html/2609.13285v1) | 2026-09-15T08:00:00+08:00 | 把 content key 改为从 value 重构的派生状态，只单独缓存 positional key，改变 KV 的逻辑最小状态；3 + 2 + 2 = 7 | 深入完成 | 整合：`MODEL-KV-CACHE` [Ch19](../../../../books/part-02-model/19-kv-cache.md) |
| [VAMP（arXiv:2609.13537v1）](https://arxiv.org/html/2609.13537v1) | 2026-09-15T08:00:00+08:00 | MoE expert weights 与会话 KV 不再静态分区，运行时按未来工作成本重映射 HBM page；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [mKernel（arXiv:2609.13585v1）](https://arxiv.org/html/2609.13585v1) | 2026-09-15T08:00:00+08:00 | tile 级 compute/NVLink/RDMA pipeline 与自适应 SM 分权把跨节点通信带进同一 kernel execution contract；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Recoverability as a System Primitive（arXiv:2609.13672v1）](https://arxiv.org/html/2609.13672v1) | 2026-09-15T08:00:00+08:00 | checkpoint 存在不等于可恢复；起点、动作权限、证据与执行后验证必须共同提交；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Prefix Sharing Is a Sorting Problem（arXiv:2609.13692v1）](https://arxiv.org/html/2609.13692v1) | 2026-09-15T08:00:00+08:00 | 可交换 prompt blocks 的顺序本身成为 KV 复用控制量，global order 在三块以上可结构性次优；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Certifying Model Upgrades（arXiv:2609.13714v1）](https://arxiv.org/html/2609.13714v1) | 2026-09-15T08:00:00+08:00 | “未发现退化”不能替代 slice-wise non-inferiority；候选搜索与独立 paired certification 必须分离并保留 incumbent fallback；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [The Filter Metric is Safety-Critical（arXiv:2609.13866v1）](https://arxiv.org/html/2609.13866v1) | 2026-09-15T08:00:00+08:00 | GRPO 的 shaped score 若兼任 no-contrast filter，会把全失败组的 shaping 差异放大成 phantom advantage；3 + 2 + 3 = 8 | 深入完成 | 整合：`TRAIN-GRPO` [Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [AcquireBound（arXiv:2609.14744v1）](https://arxiv.org/html/2609.14744v1) | 2026-09-15T08:00:00+08:00 | 支付/创建成功不等于获得的资源可转为 authority，必须先 quarantine、解析实际 capability，再原子激活；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Fabrication After Tool Failure（arXiv:2609.14758v1）](https://arxiv.org/html/2609.14758v1) | 2026-09-15T08:00:00+08:00 | `status:ok` 但 payload 不可用会把 retrieval failure 伪装成可回答状态；工具协议需要显式失败语义而非只靠 prompt 忠诚；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [The Stochastic Deputy（arXiv:2609.14780v1）](https://arxiv.org/html/2609.14780v1) | 2026-09-15T08:00:00+08:00 | 让模型填写 tenant ID 即使服务端验证也会授予越权表达能力；scope 应从 tool schema 移除并由凭据在模型下方绑定；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-MULTI-TENANT` [Ch71](../../../../books/part-06-ai-infrastructure/71-multi-tenant.md) |
| [Shared KV Caching for Replicated 27B Inference（arXiv:2609.15021v1）](https://arxiv.org/html/2609.15021v1) | 2026-09-15T08:00:00+08:00 | 跨副本共享 KV 的收益以 locality 为前提，正确性还依赖 allocator/page layout/CUDA stream ordering；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [How Lossless Is Lossless Speculative Decoding?（arXiv:2609.15504v1）](https://arxiv.org/html/2609.15504v1) | 2026-09-15T08:00:00+08:00 | 算法层 trajectory equivalence 会被有限精度执行破坏；downstream 分数未降不等于 speculative path “lossless”；3 + 2 + 3 = 8 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [BudgetBench（arXiv:2609.13149v1）](https://arxiv.org/html/2609.13149v1) | 2026-09-15T08:00:00+08:00 | 把 per-call token budget 变成 memory-strategy evaluation 的独立变量，并把 violation rate 纳入一等结果；2 + 2 + 3 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [PEAT（arXiv:2609.13544v1）](https://arxiv.org/html/2609.13544v1) | 2026-09-15T08:00:00+08:00 | pseudo-error campaign 将 GPU kernel fault 绑定到算子、signature、传播位置与 task outcome；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [BOOST（arXiv:2609.13592v1）](https://arxiv.org/html/2609.13592v1) | 2026-09-15T08:00:00+08:00 | coherent heterogeneous memory 允许 weights/KV 从 HBM 与 host 并发取数，改变只靠冷热搬运的 tiering 假设；2 + 3 + 2 = 7 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [AttnFuse（arXiv:2609.13612v1）](https://arxiv.org/html/2609.13612v1) | 2026-09-15T08:00:00+08:00 | attention DSL 把 RoPE 等 pre-matmul transform、layout 与 GPU-specific fusion 编入同一 execution plan；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [Identity Is More Than Recall（arXiv:2609.13637v1）](https://arxiv.org/html/2609.13637v1) | 2026-09-15T08:00:00+08:00 | persistent identity 不能只测 recall，必须绑定 profile revision/session lineage 并分测 enactment、resistance、persistence；2 + 2 + 3 = 7 | 深入完成 | 整合：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [When Compliance Data Masquerades as Evaluation（arXiv:2609.13642v1）](https://arxiv.org/html/2609.13642v1) | 2026-09-15T08:00:00+08:00 | monitoring/compliance data 只有在 claim、exposure、domain、capture 与 comparator 对齐时才取得比较证据权限；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Do Not Restart（arXiv:2609.13800v1）](https://arxiv.org/html/2609.13800v1) | 2026-09-15T08:00:00+08:00 | stateful handoff 只补 residual work，并保留 accepted choices、effects、unfinished obligations 与 action set；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Persistent Memory Poisoning（arXiv:2609.13889v1）](https://arxiv.org/html/2609.13889v1) | 2026-09-15T08:00:00+08:00 | memory/skill write 可让攻击跨会话延迟触发，prompt-only defense 不能替代 write/read/effect provenance gate；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [FlowSeal（arXiv:2609.14003v1）](https://arxiv.org/html/2609.14003v1) | 2026-09-15T08:00:00+08:00 | 模型下方的 tool interceptor 传播 provenance/IFC label，并只通过显式 declassification 释放数据；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [When Tools Get in the Way（arXiv:2609.14157v1）](https://arxiv.org/html/2609.14157v1) | 2026-09-15T08:00:00+08:00 | 即便没有调用，无关工具的可见性也会改变 closed-answer 策略；tool catalog 是需 admission 的推理输入；2 + 2 + 2 = 6（Books 缺口触发深入审阅） | 深入完成 | 整合：`AGENT-TOOL-CALLING` [Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [OpWeave（arXiv:2609.14237v1）](https://arxiv.org/html/2609.14237v1) | 2026-09-15T08:00:00+08:00 | serving disaggregation unit 从 model/stage 下沉到 operator，并分离 planner placement 与 runtime topology truth；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [Flattening Every Memory Peak（arXiv:2609.14306v1）](https://arxiv.org/html/2609.14306v1) | 2026-09-15T08:00:00+08:00 | 长上下文 MoE training 必须分别约束 dispatch、vocab projection、checkpoint 与 optimizer 的峰值及组合顺序；3 + 3 + 3 = 9 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [InplaceKVCache（arXiv:2609.14507v1）](https://arxiv.org/html/2609.14507v1) | 2026-09-15T08:00:00+08:00 | 写入时固定 CPU/GPU physical region map，让 scheduler 选择访问位置而非事后搬迁；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Carryover Drafting（arXiv:2609.14717v1）](https://arxiv.org/html/2609.14717v1) | 2026-09-15T08:00:00+08:00 | 被拒 verifier states 可成为下一轮只读 proposal state，但不得越过 target commit frontier；2 + 2 + 3 = 7 | 深入完成 | 整合：`INFER-SPECULATIVE-DECODING` [Ch48](../../../../books/part-05-inference-system/48-speculative-decoding.md) |
| [Pull（arXiv:2609.14773v1）](https://arxiv.org/html/2609.14773v1) | 2026-09-15T08:00:00+08:00 | working memory 以 deterministic directory 懒惰 materialize 原始 evidence，避免不可逆 summary 接管 source state；2 + 2 + 3 = 7 | 深入完成 | 整合：`AGENT-MEMORY` [Ch77](../../../../books/part-07-agent/77-memory.md) |
| [AgentKV（arXiv:2609.14872v1）](https://arxiv.org/html/2609.14872v1) | 2026-09-15T08:00:00+08:00 | think/act/tool phase 与未来 query mixture 进入 KV eviction identity，classifier 只提交 hint；2 + 3 + 3 = 8 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ActGuard（arXiv:2609.14987v1）](https://arxiv.org/html/2609.14987v1) | 2026-09-15T08:00:00+08:00 | local tool prior、evidence localization 与 verifier sanitization 组成 pre-execution sensor，但不接管 deterministic authorization；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Overflip（arXiv:2609.15013v1）](https://arxiv.org/html/2609.15013v1) | 2026-09-15T08:00:00+08:00 | benign repetition 可能让长输入 guardrail label 翻转，release matrix 需显式扫描 length × repetition；2 + 2 + 2 = 6（安全约束触发深入审阅） | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Hybrid-state Cache Recovery（arXiv:2609.15030v1）](https://arxiv.org/html/2609.15030v1) | 2026-09-15T08:00:00+08:00 | cache recovery 同时校验 token credit、strict-prefix hit、transfer/save completion 与 numerical path；2 + 3 + 2 = 7 | 深入完成 | 整合：`INFER-KV-CACHE` [Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [ETCInfer（arXiv:2609.15230v1）](https://arxiv.org/html/2609.15230v1) | 2026-09-15T08:00:00+08:00 | cooling setpoint、GPU frequency 与 microbatch 共同成为带 thermal dynamics 的 inference schedule；2 + 3 + 2 = 7 | 深入完成 | 整合：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [MAPS（arXiv:2609.15359v1）](https://arxiv.org/html/2609.15359v1) | 2026-09-15T08:00:00+08:00 | output-length upper bound 可与 prefill overlap 并驱动分层调度，但需持续与实际 progress 对账；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：`INFER-SCHEDULING` [Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [When Tool Calls Succeed but Workflows Fail（arXiv:2609.15397v1）](https://arxiv.org/html/2609.15397v1) | 2026-09-15T08:00:00+08:00 | tool observation success 与 world effect commit 必须分离，并以 effect history 支持 reconciliation/rollback；3 + 3 + 3 = 9 | 深入完成 | 整合：`AGENT-WORKFLOW` [Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Can We Trust the Judges?（arXiv:2609.15561v1）](https://arxiv.org/html/2609.15561v1) | 2026-09-15T08:00:00+08:00 | 用受控 answer corruption 形成已知事实退化序列，检查 factuality metric 是否能追踪损坏；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Trillion-Parameter MoE in a Box（arXiv:2609.15636v1）](https://arxiv.org/html/2609.15636v1) | 2026-09-15T08:00:00+08:00 | MoE provisioning 必须分开 internal storage bandwidth 与 host-link bandwidth 的两个 knee；3 + 3 + 3 = 9 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [QCAR（arXiv:2609.13489v1）](https://arxiv.org/html/2609.13489v1) | 2026-09-15T08:00:00+08:00 | 把 fixed top-k 改为 query-conditioned retrieval depth，并用离线 saturation/cluster state 将在线选择约束为常数时间 proposal；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`AGENT-RAG` [Ch76](../../../../books/part-07-agent/76-rag.md) |
| [ForgeTrain（arXiv:2609.13645v1）](https://arxiv.org/html/2609.13645v1) | 2026-09-15T08:00:00+08:00 | golden reference、冻结 Harness 与单调放宽的 equivalence chain 把 AI 生成训练引擎的优化权和验收权分离；3 + 3 + 2 = 8 | 深入完成 | 整合：`TRAIN-DISTRIBUTED-TRAINING` [Ch36](../../../../books/part-04-training-system/36-distributed-training.md) |
| [Synthetic–Authentic RAG Evaluation（arXiv:2609.14579v1）](https://arxiv.org/html/2609.14579v1) | 2026-09-15T08:00:00+08:00 | synthetic 与 authentic query distribution 会选择不同的 retriever/latency 方案，RAG release contract 必须同时拥有两类 workload；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：`PLATFORM-EVALUATION-SYSTEM` [Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [IntentCap（arXiv:2609.14631v1）](https://arxiv.org/html/2609.14631v1) | 2026-09-15T08:00:00+08:00 | user/workflow/tool/runtime 按字段 owner 合成短时 capability lease，任何来源只可缩权，副作用前由 deterministic checker 提交；3 + 3 + 3 = 9 | 深入完成 | 整合：`PLATFORM-SECURITY` [Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [BigMoMo（arXiv:2609.14643v1）](https://arxiv.org/html/2609.14643v1) | 2026-09-15T08:00:00+08:00 | speculative verification window 成为 mobile MoE expert staging 的 bounded lookahead，但最终 router/verification authority 不变；3 + 3 + 2 = 8 | 深入完成 | 整合：`INFER-GPU-MEMORY` [Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [Loop-Back Authority（arXiv:2609.14767v1）](https://arxiv.org/html/2609.14767v1) | 2026-09-15T08:00:00+08:00 | manager 只有能独立验证时才应拥有 reject/revision authority；只能 opine 的层级会增加 hedging、成本与时延；3 + 2 + 3 = 8 | 深入完成 | 整合：`AGENT-MULTI-AGENT` [Ch82](../../../../books/part-07-agent/82-multi-agent.md) |
| [DeepSeek-V4-Flash on AMD gfx90a（arXiv:2609.15627v1）](https://arxiv.org/html/2609.15627v1) | 2026-09-15T08:00:00+08:00 | mixed-precision fast path 要先过 component oracle 与 bounded semantic checks；不同 workload/protocol 的性能数字不得相乘或互除；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：`INFER-TENSORRT-LLM` [Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |

## 4. 证据与知识整合

### [DeepSeek V4.1-Flash alias migration](https://www.deepseek.com/en/news/deepseek-v4-1-flash/)

官方说明在 9 月 10 日发布，但明确规定 9 月 14 日 04:00 UTC 起，`deepseek-v4-pro` 请求开始路由到 V4.1-Flash；该生效事件落入本窗。它只证明 API alias 的解析目标与价格/兼容行为改变，未披露内部迁移机制，也不能用伙伴评价证明模型普遍更优。第 59 章已经把 mutable alias 与 immutable ModelVersion 分开，并要求部署时解析、固化 digest/revision 与保留 rollback target，故无需重复写入。

### [PDD（arXiv:2609.13161v1）](https://arxiv.org/html/2609.13161v1)

exact-v1 §3 将跨机房 PD 拆成 Prefill、同机房 Relay Decode 与远端 Main Decode：RLD 用本地 RDMA 立即接管首批 decode，与 WAN KV 传输重叠；MD 收到 KV 后只接收 RLD 产生的 token IDs，以 Extend-Decode 重算增量 KV 并接管。§4 的收益绑定 H100/H200、作者网络与长输入/短输出 agent workload，BCR 不能外推任意价格与 SLO。Books 增量应放在 Ch55 的 PD 数据流之后：把 relay 定义为临时 authority、handoff 绑定 KV/token boundary 与重复输出防护；WAN 不经济或输出较长时保留同机房 PD。

### [Self-Indexing Attention（arXiv:2609.13205v1）](https://arxiv.org/html/2609.13205v1)

exact-v1 的 Shared Transform-Domain Representation 与 System Implementation 表明，key signs 同时作为 1-bit 检索索引和压缩表示的一部分，prefill/decode 共用同一 token identity；sign-magnitude cache 仍保存 magnitude，外部 compressor 也须兼容同一 transform。LongBench/RULER 与 operator speedup 只覆盖作者密度、模型、GPU 与 kernel，不证明 5% density 普遍近似 dense。Ch45 应补入“索引与压缩 representation 共享 identity”分支：transform、sign index、magnitude codec、RoPE 顺序、selector 与 kernel 任一变化都使缓存失效；检索置信不足回退 FullKV。

### [Grouped Value Attention（arXiv:2609.13285v1）](https://arxiv.org/html/2609.13285v1)

exact-v1 §3 把 content key 定义为 grouped value 的线性映射，并把映射吸收到 query；位置语义由独立的小型 RoPE key channel 保存。§4–6 只在 350M、30B tokens、作者配置上接近 GQA，end-to-end decode kernel 尚未完成，因此 45–47% persistent scalar reduction 不能写成吞吐收益。Ch19 应把 KV 的逻辑状态从固定 `K+V` 扩展为“可从另一缓存状态重构的 content key + 不可省略的 position key”，并保留 GQA/MQA 作为无需重训和专用 kernel 的旧路径。

### [VAMP（arXiv:2609.13537v1）](https://arxiv.org/html/2609.13537v1)

exact-v1 §III–V 指出 multi-turn MoE serving 会在 KV pool 饱和后产生 prefix-cache cliff；VAMP 在 expert staging、prefix eviction 与 request preemption 间估计未来工作，以 CUDA VMM page remap 把有界 expert region 改作 KV capacity。§VI 的 23.6× TTFT-p90 与 +31.1% TPOT 是 Qwen3-Next-80B、作者 H100/H200 和记录 workload 的一组取舍。Ch54 应加入 typed HBM repartition controller：KV、expert、workspace 仍有不同 owner；决策同时记录 re-prefill、PCIe expert load、TTFT/TPOT SLO，预测不可靠或 interconnect 无法隐藏搬运时回退静态分区。

### [mKernel（arXiv:2609.13585v1）](https://arxiv.org/html/2609.13585v1)

exact-v1 §3–5 用 persistent kernel 将 SM 分成 compute/communication roles，按 tile 逐级经过 GPU、NVLink 与 RDMA，并由 on-GPU controller 随 shape 调整分区；五种 TP/EP/SP kernel 的结果绑定两个 16×H200 集群与所测网络。Ch49 已经明确：通信下沉 kernel 后，backend、issuer granularity、chunk、SM allocation 与同步共同构成 execution contract，且 tile、persistent kernel、RDMA 与回退边界均已承载。该论文作为新的受限实现证据，不再扩写正文。

### [Recoverability as a System Primitive（arXiv:2609.13672v1）](https://arxiv.org/html/2609.13672v1)

exact-v1 §3–5 把 recovery point、允许的 recovery action、支持证据、enactment 与 independent check 分成不同责任；§6 的 deterministic/paired file challenges 证明“最终完成”可掩盖不允许的起点。它没有覆盖开放网络、并发外部副作用或完整生产 trust model。Ch81 已有 Context/Environment 联合 checkpoint、effect ledger、policy graph 变更后重新 admission、resume evidence 与 independent verifier，已承载相同长期命题，无需重复加入论文术语。

### [Prefix Sharing Is a Sorting Problem（arXiv:2609.13692v1）](https://arxiv.org/html/2609.13692v1)

exact-v1 §2–6 证明当请求由三个以上可交换 blocks 组成时，单一 global order 可渐近次优；request hierarchy 决定每个 block 的 canonical placement。§7–8 在 BEIR traces 上还显示 cache capacity 与有限 reorder window 可互换，但语义不可交换的 system/tool blocks不能因此移动。Ch45 应在 exact prefix identity 之后增加“布局优化必须受语义偏序约束”：scheduler 可在可交换集合内按请求层次排序，同时把 composition order 纳入 cache identity；约束不足时回退固定 order。

### [Certifying Model Upgrades（arXiv:2609.13714v1）](https://arxiv.org/html/2609.13714v1)

exact-v1 §3 把 development candidate search 与冻结候选的独立 paired non-inferiority test 分开，任一关键 slice 不能认证就返回原 incumbent；§5 的模拟展示 no-detected-harm gate 与 certification 的行为差异，但 public digits study 因功效不足始终回退，作者明确未证明 foundation model 收益。Ch66 应把 release gate 从“平均分+未检出退化”推进为 prespecified slice tolerance、paired evidence、candidate-search multiplicity 与 exact incumbent fallback；代价是 slice 增多会降低 power，而不是用 Bonferroni 机械惩罚 slice 数。

### [The Filter Metric is Safety-Critical（arXiv:2609.13866v1）](https://arxiv.org/html/2609.13866v1)

exact-v1 §3–9 隔离了 metric–predicate mismatch：用 shaped score 判断 group 是否有对比，会让 all-fail group 的 shaping spread 通过过滤，再被标准差归一化放大；只改 verl/DAPO filter metric 的对照复现了 collapse 方向。结果限于 GSM8K/MATH、Qwen2.5 1.5B/7B、LoRA、短训练与披露 shaping。Ch33 应明确区分 `task outcome`、`training reward` 与 `sampling/filter predicate` 三种状态所有权；composite reward 可训练 policy，但 no-contrast filter 应使用不受 shaping 项影响的 task outcome，条件不满足时关闭动态过滤。

### [AcquireBound（arXiv:2609.14744v1）](https://arxiv.org/html/2609.14744v1)

exact-v1 §4–6 把 acquisition result 放入 quarantine，经 authenticated provider evidence 与 versioned resolver 得到 capability manifest，再以 typed resource–capability hypergraph 检查 relational envelope 后原子激活；effect permit 在提交点再次验证和消费。§7–10 的形式性质与 staged MCP/Docker cases 只在明确 assumptions、fixture 与 observation boundary 内成立。Ch72 应补“post-fulfillment activation gap”：payment/OAuth/creation success 不能授予 runtime authority；resolver/epoch/provenance 不完整时资源保持隔离，旧的静态 allowlist 在不产生新 authority 的短任务仍成立。

### [Fabrication After Tool Failure（arXiv:2609.14758v1）](https://arxiv.org/html/2609.14758v1)

exact-v1 §3–6 在强制 tool call 且 payload 必然不可用的 1,024 个受控条目上发现：显式 `status:error` 与“`status:ok` 但 redacted/stale/empty”触发完全不同的虚构率；要求先声明 `retrieval_status` 在作者条件下显著降低不诚实输出。它不证明正则 detector 等价于事实验证，也未覆盖开放工具链。Ch78 应将 tool response 定义为 `transport status + semantic usability + provenance`；payload 不可用必须成为 typed failure 并阻断事实提交，prompt 句子只作兼容 fallback。

### [The Stochastic Deputy（arXiv:2609.14780v1）](https://arxiv.org/html/2609.14780v1)

exact-v1 §3–5 的核心不是“加强 tenant_id 校验”，而是模型不应拥有表达任意 tenant scope 的接口：从 MCP schema 移除 tenant 参数，把 scope 绑定可信 credential 并在工具下方执行。§8 同时暴露 writable scope forgery、query-planner cliff 与索引依赖。Ch71 已明确不能信任用户/Agent 提交 tenant label，identity translation 必须由可信控制面完成，并覆盖 cache、credential 与共享状态；现有正文已承载这条机制及性能代价，无需重复扩写。

### [Shared KV Caching for Replicated 27B Inference（arXiv:2609.15021v1）](https://arxiv.org/html/2609.15021v1)

exact-v1 §3 把 packed-page compatibility、CUDA stream dependency、allocator pinning 与 layered validation 都列为 correctness gate；§5 显示只有跨 replica、长 prefix 且 locality 丢失时收益显著，固定 placement 几乎无收益。性能数字只属于两个单 H100 27B vLLM replicas、256 GiB host pool、作者长度/并发。Ch45 应补入 shared-cache commit protocol：producer stream completion、page/layout/version、consumer visibility 与 request placement 必须联合验证；不能证明时回退本地 KV 或重算。

### [How Lossless Is Lossless Speculative Decoding?（arXiv:2609.15504v1）](https://arxiv.org/html/2609.15504v1)

exact-v1 §3–5 独立复现 Orthrus：BF16 下 exact trajectory match 约 43–45%，FP32 才在所测 prompts 全匹配；同时 downstream harness 未见系统退化。它证明“相同任务分数”和“逐 token trajectory equivalence”是不同合同，不证明 FP32 在任意硬件/并发都完全相同。Ch48 应把 lossless 定义绑定 logits/acceptance arithmetic、dtype、kernel 与 deterministic execution；若产品只需质量非劣，另立 statistical-quality contract，不能继续称 exact。

### [BudgetBench（arXiv:2609.13149v1）](https://arxiv.org/html/2609.13149v1)

§2/§4/§6/§7/§9 支持把 per-call token budget 作为 memory strategy 的独立评价变量，同时记录质量、预算利用、延迟和 violation rate。三个 pilot 能证明单预算会隐藏非单调曲线，不能给出策略最终排序；早期 tokenizer approximation 的违规行只作诊断。Ch66 需要把这一变量接到 resource-constrained evaluation，而 exact tokenization 不可用时回退 full-context baseline。

### [PEAT（arXiv:2609.13544v1）](https://arxiv.org/html/2609.13544v1)

§IV–V 支持把 pseudo-error 绑定注入算子、错误 signature、传播位置和 task outcome；V100/MI250 与所测 workloads 不证明生产 fault prevalence 或跨架构阈值。Ch66 已在“数值 Fault 要沿 Layer、Operation、Token 与 Task 观察传播”完整承载该命题，因此只保留受限证据。

### [BOOST（arXiv:2609.13592v1）](https://arxiv.org/html/2609.13592v1)

§3–6 支持在 coherent heterogeneous memory 上让 HBM 与 host 访问并发，改变仅按冷热搬运的 tiering 选择。作者数字绑定 Grace Hopper、vLLM、静态 weights/KV 与披露 batch；Ch54 应加入 overlap-aware branch，平台不支持 coherence 或 contention 超界时回退显式迁移/固定驻留。

### [AttnFuse（arXiv:2609.13612v1）](https://arxiv.org/html/2609.13612v1)

§3–6 与 §9.1 支持 attention DSL 把 RoPE 等 pre-matmul transform、layout、tile 和 GPU fusion 编入同一 plan，并显示 fusion crossover 依架构而变。RTX3090/H100、Llama3-8B 与作者 pattern 不代表端到端 serving；Ch49 已有 transform/fusion/backend identity 与 fallback，不重复扩写。

### [Identity Is More Than Recall（arXiv:2609.13637v1）](https://arxiv.org/html/2609.13637v1)

§2–4/§6 支持把 persistent identity 拆成 recall、composition、enactment、resistance、persistence，并绑定 profile revision 与 session lineage。16 synthetic profiles、32 probes、3 configurations、1,536 responses 受 single sample 和 judge sensitivity 限制；Ch66 只吸收 evaluation-object 边界，不采用真实用户长期稳定性结论。

### [When Compliance Data Masquerades as Evaluation（arXiv:2609.13642v1）](https://arxiv.org/html/2609.13642v1)

§IV–VII 说明 monitoring/compliance data 只有在 claim、exposure、domain、capture 与 comparator 对齐时才支持比较。它主要提供测量合同和 automated-driving case，没有 foundation-model causal benchmark；Ch66 已由 Evaluation Identity、Measurement Identity 与 Evidence Chain 承载该权限边界。

### [Do Not Restart（arXiv:2609.13800v1）](https://arxiv.org/html/2609.13800v1)

§3–4 支持 handoff 保存 accepted choices、已发生 effects、未完成 obligations 与受限 action set，使接手者只补 residual work。五个环境与两个 same-provider pairs 未覆盖开放网络/并发副作用；Ch81 的 checkpoint、effect ledger、resume evidence、action binding 与 independent verifier 已覆盖。

### [Persistent Memory Poisoning（arXiv:2609.13889v1）](https://arxiv.org/html/2609.13889v1)

§3–4 支持恶意内容写入 memory/skill 后延迟触发，并显示 prompt-only defense 在持久写入之后能力有限。OpenClaw/Claude Code 与作者 triggers 不给出开放世界攻击率；Ch72 已要求 write 保存 origin/trust/taint/policy generation，read/effect 前重验与 quarantine。

### [FlowSeal（arXiv:2609.14003v1）](https://arxiv.org/html/2609.14003v1)

§V–IX 支持在模型下方的 tool interceptor 传播 provenance/IFC labels，并由显式 declassification 释放信息；三 benchmarks、八 attacks 和 live MCP 仍依赖标签与 interceptor coverage。Ch72 已有 value-bound authority、label propagation、sink policy 与 deterministic commit，故不再新增一份同义控制链。

### [When Tools Get in the Way（arXiv:2609.14157v1）](https://arxiv.org/html/2609.14157v1)

§3–6 在 500 query pairs、10 domains、6 LLMs 中观察到：仅暴露无关工具就可能降低 closed-answer correctness，即使工具没有被调用。模型/工具配置限制外推；Ch78 应把 tool catalog 视为需 scope-aware admission 的 inference input，漏掉必要工具时允许显式扩权或重试。

### [OpWeave（arXiv:2609.14237v1）](https://arxiv.org/html/2609.14237v1)

§3–7 支持把 heterogeneous serving 的 disaggregation unit 下沉至 operator，并分开 planner placement 与 runtime topology/state-transfer truth。vLLM、作者集群和 cost model 不证明任意网络或生产尾延迟；Ch56 应在 operator-DAG 弹性后加入该分支，成本/拓扑失真时回退 stage/model placement。

### [Flattening Every Memory Peak（arXiv:2609.14306v1）](https://arxiv.org/html/2609.14306v1)

§2–4/§7 及附录支持分别约束 expert dispatch、vocab projection、checkpoint boundary、optimizer state 四类 memory peak，再用 bounded streaming schedules 组合。收益绑定模型、parallel layout 与 hardware，组合还增加 host traffic、recompute 与 ordering；Ch36 应吸收“峰值 owner 不能被 steady state 替代”的长期机制。

### [InplaceKVCache（arXiv:2609.14507v1）](https://arxiv.org/html/2609.14507v1)

§3–7/§9 支持在写入时把 CPU/GPU residency 固化为 four-region physical layout，使 scheduler 选择消费位置而非事后搬迁。三 MoE、A100/V100、32 GB 与最高 1M aggregate context 不证明通用 portability；Ch54 应绑定 logical identity 与 region map，不兼容时回退迁移式 tiering。

### [Carryover Drafting（arXiv:2609.14717v1）](https://arxiv.org/html/2609.14717v1)

§2–6 支持把被拒 verifier hidden states 转为下一轮仅供 proposal 的临时 drafter KV，并保持 target commit frontier。作者两 target/drafters 与 vLLM 加速不外推任意 workload；Ch48 应明确 rejection 后可复用 state 与 committed token/KV 分离，漂移时丢弃临时状态。

### [Pull（arXiv:2609.14773v1）](https://arxiv.org/html/2609.14773v1)

§3–6 支持以 deterministic metadata directory 懒惰 materialize working memory，保留原始 evidence 而非提交不可逆 summary。LoCoEval/BEAM1M 受 selector、missing evidence 与 judge 限制；Ch77 应把它放在 Raw/Summary Visibility 后，路由不确定时回退直接 evidence retrieval。

### [AgentKV（arXiv:2609.14872v1）](https://arxiv.org/html/2609.14872v1)

§3–4 与 Limitations 支持按 think/act/tool phase 建立 query buffer，并把 phase-aware future query mixture 用作 eviction hint。两个模型、六域、三 budgets 不证明 phase classifier 稳定；Ch45 应让 exact KV owner 保留 identity 与 conservative/LRU fallback。

### [ActGuard（arXiv:2609.14987v1）](https://arxiv.org/html/2609.14987v1)

§3–4 与附录支持 local tool prior、evidence localization、verifier sanitization 的 pre-execution sensor。AgentDyn/AgentDojo 不关闭 adaptive attacks，且新增 trusted component/latency；Ch72 已把 model prediction 放在 deterministic IAM/schema/policy/approval 之前并在执行后 reconcile，故判已有覆盖。

### [Overflip（arXiv:2609.15013v1）](https://arxiv.org/html/2609.15013v1)

§3–6 在 9 个 guardrails、100 prompts 中观察到 5 个会因 benign repetition 在 2.6k–9.4k tokens 首次翻转，说明短输入 verdict 不是稳定属性。结果非普遍定律且 attention dispersion 不是完整因果证明；Ch72 应增加 length × repetition release slice，超界时回退外置 policy/abstain/人工审批。

### [Hybrid-state Cache Recovery（arXiv:2609.15030v1）](https://arxiv.org/html/2609.15030v1)

§2–6 支持恢复时联合校验 scheduler token credit、strict-prefix lookup、transfer/save completion 与 numerical path；cache hit 不等于同一可继续状态。GLM-5.3-Flash NVFP4、vLLM+LMCache、TP4 和串行 tests 未覆盖并发与容量；Ch45 应在失败时要求 full-prefix recompute。

### [ETCInfer（arXiv:2609.15230v1）](https://arxiv.org/html/2609.15230v1)

§III–VII 支持把 cooling setpoint、GPU frequency 与 microbatch 联合为带 thermal dynamics 的 schedule。作者 energy/throttling/SLO 数字主要来自 simulation 与有限 validation，依赖 facility/GPU calibration；Ch56 应让统一 scheduler 持有 SLO slack，模型漂移时回退固定 cooling/DVFS 和保守 admission。

### [MAPS（arXiv:2609.15359v1）](https://arxiv.org/html/2609.15359v1)

§3–5 支持把 speculative output-length prediction 与 prefill overlap，并用 calibrated upper bound 驱动 global/local scheduling。两个 workloads/LLMs 不证明漂移下稳定；Ch56 已有 output-length uncertainty、future reservation、hierarchical scheduling 和 predicted/observed progress reconciliation，因此只保留案例。

### [When Tool Calls Succeed but Workflows Fail（arXiv:2609.15397v1）](https://arxiv.org/html/2609.15397v1)

§2–5 区分 world events 与 observations，列出八类 agent-tool boundary anomaly，并用 98,291 个 MCP tools 的 survey 说明 transaction annotations 缺口。Survey 不证明 black-box tool 已具备语义；Ch81 应把 effect history、idempotency、reconciliation、rollback/compensation 放在 durable execution 与 retry 之间，缺少 receipt 时 fail closed。

### [Can We Trust the Judges?（arXiv:2609.15561v1）](https://arxiv.org/html/2609.15561v1)

§3–6 用受控 answer corruption 构造已知事实退化序列，检查 factuality metric 是否随损坏变化。Perturbation validity、数据集、模型与 pipeline 仍受 learned judge 影响；Ch66 已有 clean/noisy twin、transformation stability 与 sensor-not-truth 边界，因此不重复正文。

### [Trillion-Parameter MoE in a Box（arXiv:2609.15636v1）](https://arxiv.org/html/2609.15636v1)

§II–IV 支持把 HBM/DRAM/high-bandwidth flash provisioning 拆成 internal storage bandwidth 与 host-link bandwidth 两个 knee。两 trillion-parameter MoE 的分析、一个 routing trace 与 agent traces 主要是 modeled evidence；Ch54 应吸收双 knee 决策，条件不满足时回退 DRAM/host offload 或更小 resident model。

### [QCAR（arXiv:2609.13489v1）](https://arxiv.org/html/2609.13489v1)

exact-v1 §3～§5 把固定 top-k 的 over/under-retrieval 压力改写为 query-conditioned retrieval budget：离线从 NDCG-k curve 求 per-query saturation，再将 query cluster 映射为保守 depth，在线 controller 只提交查多少的 proposal。法律查询数据、相关性标签、embedding/cluster 稳定性和约 6,820 条清洗 query 限定了证据，摘要所述 F1/token 收益不能外推其他域。Ch76 已有 bounded query policy、budget、revision identity 与 fixed-retriever fallback，故无需重复写入。

### [ForgeTrain（arXiv:2609.13645v1）](https://arxiv.org/html/2609.13645v1)

exact-v1 §3.1～§3.4 以 golden reference 和冻结 Harness 捕获 activation、gradient、optimizer、loss-scaling 与 collective anchors，先要求 bit-for-bit，再经真实训练 Gate 单调放宽到 trajectory/downstream parity；优化 agent 无权改验收脚本或让失败探索进入下一 baseline。§4 的七个 H100/Ascend 设置与三个长程 engine 支持 4.7%～33.2% MFU 的作者条件，不证明任意 AI 生成框架或 training-quality parity 等于数值等价。Ch36 应吸收“AI-generated execution plan 的 oracle/优化权分离”；reference 不可信或无法承担长程重验时仍回退成熟通用框架。

### [Synthetic–Authentic RAG Evaluation（arXiv:2609.14579v1）](https://arxiv.org/html/2609.14579v1)

exact-v1 §3～§5 比较 1,851 个 synthetic queries 与 322 个学生 survey queries，展示长度、intent/source concentration 与 off-corpus/evaluability 差异会让 synthetic-optimal 的 hybrid retriever 在真实短 query 中付出最高约 8× latency。该单一大学系统和 survey 不是生产流量，也不证明 sparse retrieval 普遍无益。Ch66 已要求 Evaluation Identity 绑定 workload/traffic distribution、slice、environment 与 latency/cost，并禁止 synthetic evidence 替代 production distribution，因此只保留为受限佐证。

### [IntentCap（arXiv:2609.14631v1）](https://arxiv.org/html/2609.14631v1)

exact-v1 §1～§3 将 task intent 与 context source trust 变成 field-level capability composition：user、workflow、tool schema 与 runtime environment 各自拥有字段，所有输入只可 monotonic narrowing；LLM 生成短时 lease 后，deterministic checker 在 side effect 前裁决，并由 tool/OS policy 执行。初步实验只覆盖论文的 tool、execution、placement、delegation cases，checker 和字段配置本身成为可信面。Ch72 应补入多来源能力合成和 lease 生命周期；合成不可靠时回退静态最小权限、显式审批和短会话隔离。

### [BigMoMo（arXiv:2609.14643v1）](https://arxiv.org/html/2609.14643v1)

exact-v1 §3～§5 将 speculative decoding 的 multi-token window 用作 storage-backed MoE 的 bounded lookahead：runtime 依据 acceptance、routing impact 与 movement cost筛 staging proposal，按 co-load pattern 重排 flash layout，并批量执行 ready experts；router 与 target verification 仍拥有真实选择/提交权。四个 MoE、五个 benchmark、两个 mobile platform 中 4.83×/1.82× 是作者 workload 结果，不证明任意 flash/NPU 或 thermal SLO。Ch54 应把 speculation 作为 expert movement 的新时序信号；locality/acceptance 不足时回退 on-demand load 或小型 resident model。

### [Loop-Back Authority（arXiv:2609.14767v1）](https://arxiv.org/html/2609.14767v1)

exact-v1 §3 只改变 manager 的 reject/revision link，保持五个 agents、角色、prompt、tools、models 与 data 不变；§4 的 43 paired products/86 runs 显示在该开放式 BI 任务中 flat utility/clarity 更高，而 hierarchy 多用 51.5% tokens、40.5% generation cost、20.2% total cost 并慢 34.3%。单任务、模型 judge 与 loop-count 相关性不允许外推所有团队。Ch82 应将 verifier strength 设为 hierarchy admission 条件：supervisor 不能独立核验时保留 flat fallback；有可执行 verifier、合规审批或可检查答案时层级仍成立。

### [DeepSeek-V4-Flash on AMD gfx90a（arXiv:2609.15627v1）](https://arxiv.org/html/2609.15627v1)

exact-v1 §5 将错误 W2 permutation 的早期约 60 tok/s 路径明确判无效，§8～§10 再把 TP8 native-AR、prefill、HTTP、speculation 与独立 ABBA 协议分开。MI250/SGLang 条件下 C1/C32/C64 resident decode 为 87.60/1044.32/1334.24 tok/s；3.60×、10.32% 与 1.54% 来自不同实验，不能相乘。component equality 和 bounded semantic checks 不证明 universal numerical equivalence，dynamic batching、cold-shape compilation 与 million-token occupancy 未闭合。Ch49 已有 execution-plan identity、oracle/differential checks、fast-path admission 与 fallback，故作为窄硬件案例保留，不新增正文。

### False-negative audit 总结

恢复性口径检查先发现，初版把“Books 已有相近原则”误当成“材料没有新增贡献”，恢复 24 项；随后独立复核又定位到 13 个首句解析错误，其中 7 项在修复完整摘要后恢复。因此受影响的 315 项完整题摘最终保留 45、关闭 270，共有 31 项来自 false-negative repair。更完整的证据定位与不证明事项见 [`evidence-review.md`](./_sources/evidence-review.md)。作者侧比较后，19 项形成应进入现有论证的长期增量，12 项是新增受限证据但现有正文已经完整承载机制；精确正文输入与现有覆盖锚点见 [`books-queue.md`](./_sources/books-queue.md)。已有覆盖项没有重复追加，全部整合项均由 writer 阅读相邻正文后嵌入旧约束 → 新机制 → 代价/失败/回退链路。

`arXiv:2609.13285` 的官方 version history 还修正了一项 checkpoint 误读：v1 首次公开属于本窗；v2 提交时间为 `2026-09-15T23:00:18+08:00`，已经晚于本窗终点。因此本日报采用并评分 exact-v1；v2 不能倒灌为本窗 revision，也没有进行无关的新旧版本比较。

## 5. 缺口与下一步

无

13 个摘要首句解析错误已定点修复：7 项恢复为候选并完成 exact-v1 Review，6 项以具体理由关闭；未重跑其余 1,051 个身份。Books 写入与独立复核均已完成。

## 6. 复核

复核者：独立非作者终审（未参与本日报作者筛选、定点返修或 Books 写入）

结论：通过

fresh-context 终审核对了 `1,064 = 12 + 737 + 270 + 45`：12 个 identity/date 事件、737 个 title closure、270 个完整题摘 closure 与 45 个 arXiv 候选在逐身份 ledger 中闭合；加上 1 个官方模型事件后，46 个候选均有评分、Evidence Review 与唯一 Books disposition，账目为 30 个 `Integrate`、16 个 `Existing Coverage`。抽查未重新扫描来源，而是针对题名关闭、完整题摘关闭与恢复项检查 false-negative/false-positive；7 个恢复项的 exact-v1 证据边界成立，6 个解析后关闭项均以论文自身完整摘要给出具体且可复核的关闭理由。

30 个 `Integrate` 的 Source Family 标记均在声明的 owner 章节唯一出现，正文实际承载机制、状态或控制权变化、证据边界与失败回退；`2609.13645`、`2609.14631`、`2609.14643`、`2609.14767` 四个新增绑定分别落在 `TRAIN-DISTRIBUTED-TRAINING`、`PLATFORM-SECURITY`、`INFER-GPU-MEMORY` 与 `AGENT-MULTI-AGENT`。16 个 `Existing Coverage` 的 queue 也指向现有具体命题，而非仅凭章节名称判重。本终审未修改 Books。
