# Daily Research — 2026-08-19

**规范：** V3
**窗口：** 2026-08-18T09:00:00+08:00 ～ 2026-08-19T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T00:10:00+08:00

## 1. 结论

本窗 14 个每日来源完成重检。arXiv 官方 `new` 公告包含 475 个去重身份（`2608.16890`～`2608.18077`）；全批次标题已逐项语义筛选，含义不明确或可能形成长期增量的材料进一步读取摘要，最终冻结 18 个材料家族。旧报告只列 3 项，漏掉批次首尾的大量有效系统材料；本版已纠正。候选 exact-v1 均可取得，未发现 withdrawn。

本窗的长期主线是：Agent 的安全、恢复与审计从“相信生成文本”转向 action boundary、authorized context、durable receipt 与 versioned workspace；Training/Inference 的优化从单个算子推进到 harness ownership、状态表示与 runtime contract。8 项长期机制已经写入 Books，10 项已有实质覆盖。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 索引按本窗日期检查 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 公开入口按日期检查 | 已检查 | 无 |
| SRC-META-AI | 官方 publication 列表按日期检查 | 已检查 | 无 |
| SRC-QWEN | 官方文章目录按日期过滤并去重 | 已检查 | 无 |
| SRC-DEEPSEEK | 官方 Updates / Research 按日期检查 | 已检查 | 无 |
| SRC-MOONSHOT | 官方 Blog / Research / release 入口检查 | 已检查 | 无 |
| SRC-TENCENT-HUNYUAN | Research“全部”日期列表检查 | 已检查 | 无 |
| SRC-ZAI | 官方 Research 列表检查 | 已检查 | 无 |
| SRC-BYTEDANCE-SEED | Research / Blog / Publications 检查 | 已检查 | 无 |
| SRC-BAIDU-ERNIE | 官方技术博客与发布入口检查 | 已检查 | 无 |
| SRC-XIAOMI-MIMO | 官方 Paper / Blog 入口检查 | 已检查 | 无 |
| SRC-MINIMAX | 官方 Blog / Research 入口检查 | 已检查 | 无 |
| SRC-ARXIV | 官方 `new` owner 清单；475 个身份从首项到末项完成题摘筛选，保留 18 项 | 已检查 | 无 |

没有按需来源被触发。

## 3. 候选与判断

公开时间表示本批官方 `new` 公告时段，不是作者提交时间。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Runtime Governance for Agentic AI](https://arxiv.org/html/2608.16891v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | model output 只是 proposal，trusted runtime 才拥有执行权；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [Dynamic MoE Serving](https://arxiv.org/html/2608.16947v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | 在未知未来 workload 下联合支付服务瓶颈与 replica movement；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：INFER-SCHEDULING，[Ch56](../../../../books/part-05-inference-system/56-inference-scheduling.md) |
| [The Price of Thinking](https://arxiv.org/html/2608.16956v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | reasoning effort 是与模型、输出 rail、价格表共同冻结的 API contract；2 + 2 + 3 = 7 | 深入完成 | 整合：INFER-REQUEST-LIFECYCLE，[Ch42](../../../../books/part-05-inference-system/42-what-happens-during-inference.md) |
| [SkillEffect](https://arxiv.org/html/2608.17007v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | tool program 先 lower 到 bounded IR，经容量与后置条件检查再发布；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Cross-Model Memory Transfer](https://arxiv.org/html/2608.17050v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | frozen external memory 的可迁移性取决于 target-side reader adaptation；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Authorization Before Context](https://arxiv.org/html/2608.17148v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | audience authorization 必须先于 memory-to-context assembly；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [The Acknowledgment Point Is the System](https://arxiv.org/html/2608.17176v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | signed receipt 必须声明 durable sync boundary 是否完成；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-LOGGING，[Ch68](../../../../books/part-06-ai-infrastructure/68-logging.md) |
| [PlanPO](https://arxiv.org/html/2608.17289v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | 成功轨迹仍按 planning efficiency 产生 coarse-to-fine advantage；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [TileMix](https://arxiv.org/html/2608.17336v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | fused attention 内以 score-tile group 路由 FP16/INT8；3 + 2 + 2 = 7 | 深入完成 | 整合：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [LEGO-RL](https://arxiv.org/html/2608.17393v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | 以 in-process proxy 保留原 harness 控制流并捕获训练轨迹；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [FESC](https://arxiv.org/html/2608.17442v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | encrypted scan-contract 将私有长上下文从二次 attention 改为可组合 recurrent state；3 + 3 + 3 = 9 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [KeyPooling](https://arxiv.org/html/2608.17485v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | relay 客户隔离失效可由 upstream credential/cache identity 实测定位；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-MULTI-TENANT，[Ch71](../../../../books/part-06-ai-infrastructure/71-multi-tenant.md) |
| [Agent Lightning v1.0](https://arxiv.org/html/2608.17528v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | deploy-time harness 拥有交互环，trainer 只观察 endpoint pairs；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [MoNe](https://arxiv.org/html/2608.17616v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | frozen Transformer 外挂 layer-local fast-weight memory；2 + 3 + 2 = 7 | 深入完成 | 已有覆盖：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [rl-triton](https://arxiv.org/html/2608.17641v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | 七种 credit estimator 归一为 associative scan 并融合 kernel；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [D²ACCI](https://arxiv.org/html/2608.17756v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | memory failure 先 stage-local diagnosis，再进入外层 release gate；3 + 3 + 2 = 8 | 深入完成 | 已有覆盖：AGENT-MEMORY / PLATFORM-EVALUATION-SYSTEM，[Ch77](../../../../books/part-07-agent/77-memory.md)、[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [StagedWorkspace](https://arxiv.org/html/2608.18050v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | parsed view、native file、diff 与 submission 必须绑定同一 workspace version；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-WORKFLOW，[Ch81](../../../../books/part-07-agent/81-workflow.md) |
| [Hydra-0](https://arxiv.org/html/2608.18077v1) | 2026-08-19T08:00:00+08:00 ～ 2026-08-19T09:00:00+08:00 | action flow 作为跨 embodiment 的视觉 action/state interface；2 + 3 + 2 = 7 | 深入完成 | 整合：MULTIMODAL-WORLD-MODELS，[Ch25](../../../../books/part-03-multimodal-world-models/25-multimodal-world-models.md) |

## 4. 证据与知识整合

### [Runtime Governance for Agentic AI](https://arxiv.org/html/2608.16891v1)

Aegis 在 tool 前由 trusted runtime 解析 server-side provenance、读取 active policy、uncertain 时 fail closed，并可进入 quorum settlement。原型不证明所有工具真实执行同一策略；Ch72 已将 model proposal 与 executor authority 分离，已有覆盖。

### [Dynamic MoE Serving](https://arxiv.org/html/2608.16947v1)

理论模型在不知道未来 workload 时同时支付 bottleneck service cost 与 replica movement，证明 deterministic constant-competitive allocation 存在。抽象成本函数不等于真实 GPU kernel/网络性能。Ch56 已覆盖 placement churn 与 service tail 的联合目标。

### [The Price of Thinking](https://arxiv.org/html/2608.16956v1)

注册配对实验显示显式 high effort 与 omitted effort 在成本和准确率上都不是模型名可替代的属性，且区间很宽。**已整合：** Ch42 将 requested/served model、reasoning effort、output rail、service product、prompt 与 dated price schedule 一并纳入 request artifact；不把单一 AIME 结果外推。

### [SkillEffect](https://arxiv.org/html/2608.17007v1)

checker 从 immutable input 重建 bounded IR、容量 lease 和 postcondition，runtime 仅 staged publish；未知 relation 与不可逆远程 effect 不在保证内。Ch78 已完整承载 checked lowering。

### [Cross-Model Memory Transfer](https://arxiv.org/html/2608.17050v1)

论文冻结 hashed memory，只适配目标 backbone 的 reader，区分 knowledge artifact 与消费接口。**已整合：** Ch77 将 external memory identity 与 reader compatibility 分开；迁移后必须重新校准读取，不把表可复制误当成语义可迁移。

### [Authorization Before Context](https://arxiv.org/html/2608.17148v1)

memory item 记录写入时 audience，context assembly 读取当前 viewer set；通道含糊时回退 public，且 admission 对 audience anti-monotone。**已整合：** Ch72 在 retrieval 后、prompt 前增加 authorization boundary；相关性不能覆盖受众权限。

### [The Acknowledgment Point Is the System](https://arxiv.org/html/2608.17176v1)

决策绑定 policy source，在 caller-selected sync boundary 持久化后返回签名 receipt；重启校验 framing、manifest、sequence 与 replay identity。**已整合：** Ch68 区分 decision made、durably recorded、receipt acknowledged 三个时刻；低延迟异步写不能声称 crash-durable。

### [PlanPO](https://arxiv.org/html/2608.17289v1)

PlanPO 对成功 trajectory 继续按 interaction efficiency 排序，缓解只有 outcome reward 时的 advantage collapse；收益限于受测 multi-turn tasks。Ch33 已把 outcome、process、cost 与 group support 分开，已有覆盖。

### [TileMix](https://arxiv.org/html/2608.17336v1)

同一 fused attention 内，compact bitmask 决定 score-tile group 使用 FP16 还是 INT8，并共享后续 online softmax state。**已整合：** Ch49 将 precision routing 视为 execution-plan 状态；必须绑定 tile policy、scale、shape、hardware 与误差验证。

### [LEGO-RL](https://arxiv.org/html/2608.17393v1)

in-process proxy 捕获 raw generation，保持 harness 原控制流，并将 crash/reward hacking/train-inference mismatch 显式化。Ch33 已有 opaque harness boundary、trajectory reconstruction 与 verifier ownership，已有覆盖。

### [FESC](https://arxiv.org/html/2608.17442v1)

FESC 以 factorized scan-contract 跨 FHE/MPC 边界组合 selective SSM transition，避免 encrypted attention 的二次 pairwise work；结论受 threat model 和算子集合限制。Ch72 已承载 private inference 的 state/cryptographic contract。

### [KeyPooling](https://arxiv.org/html/2608.17485v1)

方法逐一改变 credential、pool、adapter 与 nested hop，追踪最终 cache lookup/write identity；五种 gateway 的结果不代表所有 relay。**已整合：** Ch71 把 tenant identity 传播到 upstream principal/cache namespace，并要求 relay 验证而非只认证入口。

### [Agent Lightning v1.0](https://arxiv.org/html/2608.17528v1)

harness 拥有 interaction loop，trainer 经 endpoint proxy 观察 request-response pairs；因此 credit assignment 和 replay 都不能假设 trainer 掌控环境。Ch33 已完整写出这条 ownership 边界。

### [MoNe](https://arxiv.org/html/2608.17616v1)

固定分段更新 layer-local fast weights，query 只由 memory 生成 K/V；128K 的结果受模型与任务限制。Ch22 已覆盖 external fast-weight memory、冻结 backbone 与 approximation boundary。

### [rl-triton](https://arxiv.org/html/2608.17641v1)

GAE、V-trace 等七种 estimator 表达为同一一阶 recurrence 的 associative scan，并明确 terminated/truncated mask。它是实现收敛而非新训练目标；Ch33 的 credit semantics 已完整，kernel 留作受限实现证据。

### [D²ACCI](https://arxiv.org/html/2608.17756v1)

outer gate 以 paired evidence 决定 promote/reject，inner loop 保留 ingestion/retrieval/filter/generation stage trace。Ch77/Ch66 已分别拥有 memory state 与 evaluation release gate，已有覆盖。

### [StagedWorkspace](https://arxiv.org/html/2608.18050v1)

paper 把 parsed view、native file、review diff、submitted artifact 的版本错位定义为 workspace-state contract。**已整合：** Ch81 增加 version-pinned view/read/edit/review/submit；发布必须验证 base version，冲突时 rebase/review 而非静默覆盖。

### [Hydra-0](https://arxiv.org/html/2608.18077v1)

action flow 用 pixel motion 表达 action consequences，支持跨 embodiment/world-model backbone；RoboLab correlation 不证明真实世界 causal sufficiency。**已整合：** Ch25 将 action representation 视为 transition interface，视觉共享换来精确控制语义和 calibration 损失。

## 5. 缺口与下一步

无

8 项 Books 增量已写入相应机制正文；其余候选均已终态处置，没有剩余可执行工作。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核检查了 475 个 official-announcement 身份的首尾覆盖、18 项准入与漏项、exact-v1/withdrawn、§3/§4 一致性及 Books 实际落点。8 项新增机制均进入对应 owner 的机制正文并保留证据边界；TileMix 的长期命题位于 Ch49 正文，章末 trace 仅作来源映射。机器校验与 diff 检查通过。
