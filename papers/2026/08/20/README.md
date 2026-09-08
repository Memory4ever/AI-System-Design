# Daily Research — 2026-08-20

**规范：** V3
**窗口：** 2026-08-19T09:00:00+08:00 ～ 2026-08-20T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-09-08T00:45:00+08:00

## 1. 结论

本窗 14 个每日来源完成重检。arXiv 官方 `new` 公告得到 468 个身份（`2608.18078`～`2608.19197`）；全批次标题已逐项检查，歧义或可能改变长期大模型/Infra 判断者继续阅读摘要，冻结 21 个材料家族。旧报告的 3 项实际属于 8 月 21 日，已移出。候选 exact-v1 可取得，未发现 withdrawn。

本窗把三个常被混淆的对象分开：模型内部 recurrence 与 harness recurrence；application transcript 与 model-visible cached state；“工具调用成功”与跨 authority/evidence/resource gates 真正可提交。10 项长期机制已经写入 Books，10 项已有覆盖，1 项因受限训练证据仅保留日报。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | Research 索引按窗口检查；Privacy Filter model card 仅作版本事实，未以机制候选重复收录 | 已检查 | 无 |
| SRC-ANTHROPIC | Research 日期列表检查 | 已检查 | 无 |
| SRC-GOOGLE-AI | DeepMind / Google Research 入口按日期检查 | 已检查 | 无 |
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
| SRC-ARXIV | official-announcement owner 清单；468 个身份首尾完成题摘筛选，保留 21 项 | 已检查 | 无 |

没有按需来源被触发。

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Fractional Decay KV-Cache](https://arxiv.org/html/2608.18098v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | cumulative attention 与 recency decay 分离长期重要性/主题变化；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KV-CACHE，[Ch45](../../../../books/part-05-inference-system/45-why-kv-cache-speeds-up.md) |
| [Adversarial Review](https://arxiv.org/html/2608.18167v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | reviewer 的判断再由 critic 结构化反驳，最终编辑权仍归主 Agent；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：AGENT-REFLECTION，[Ch80](../../../../books/part-07-agent/80-reflection.md) |
| [Looped Language Models for Tool Calling](https://arxiv.org/html/2608.18171v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | recurrent depth 为依赖型 tool composition 提供可调 compute；2 + 3 + 2 = 7 | 深入完成 | 整合：AGENT-TOOL-CALLING，[Ch78](../../../../books/part-07-agent/78-tool-calling.md) |
| [Reversible Forgetting](https://arxiv.org/html/2608.18177v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | memory 从 active/retired 二元删除演进为 active/dormant/retired 可逆状态；2 + 2 + 3 = 7 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Allocating Recurrent Compute](https://arxiv.org/html/2608.18230v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 用 marginal influence 判断 mixer/FFN 中什么值得重复；2 + 1 + 2 = 5 | 标准完成 | 已有覆盖：MODEL-DECODER-ONLY，[Ch18](../../../../books/part-02-model/18-decoder-only.md) |
| [Cacheable by Design?](https://arxiv.org/html/2608.18261v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 预注册负结果显示 locality-aware MoE routing 难越过 edge SSD bandwidth wall；3 + 2 + 3 = 8 | 深入完成 | 已有覆盖：INFER-GPU-MEMORY，[Ch54](../../../../books/part-05-inference-system/54-gpu-memory.md) |
| [ComponentBench](https://arxiv.org/html/2608.18307v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 以 component-level verified tasks 填补 GUI atomic 与 long-horizon 评价断层；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [SingularClip](https://arxiv.org/html/2608.18319v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 将 continual/RL plasticity loss 关联到权重奇异值各向异性；2 + 1 + 2 = 5 | 标准完成 | 仅报告：实验范围不足以改变训练主线 |
| [Task-Conditioned Least Privilege](https://arxiv.org/html/2608.18351v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | post-training 学习 authority selection，但 deterministic verifier 仍拥有执行 gate；2 + 3 + 3 = 8 | 深入完成 | 已有覆盖：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [One Gate Is Not Enough](https://arxiv.org/html/2608.18360v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | remediation 会使先前 gate 失效，必须修改后重新执行所有受影响 controls；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [LEDGER](https://arxiv.org/html/2608.18398v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | execution events 组织成 claim→action→artifact→validation 的 evidence graph；3 + 3 + 3 = 9 | 深入完成 | 整合：PLATFORM-TRACE，[Ch69](../../../../books/part-06-ai-infrastructure/69-trace.md) |
| [SparsePR](https://arxiv.org/html/2608.18484v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 稀疏 support 与 residual reconstruction 联合决定 video attention 误差；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：MULTIMODAL-GENERATIVE-PARADIGMS，[Ch24](../../../../books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md) |
| [WhiteMatter](https://arxiv.org/html/2608.18486v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 每个 token 将所有层表示路由混合为可缓存 KV channels；3 + 2 + 2 = 7 | 深入完成 | 整合：MODEL-LONG-CONTEXT，[Ch22](../../../../books/part-02-model/22-long-context.md) |
| [FlashAttention-V](https://arxiv.org/html/2608.18656v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | blocked attention 适配可伸缩 CPU vector length 和 inter-head packing；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-TENSORRT-LLM，[Ch49](../../../../books/part-05-inference-system/49-tensorrt-llm.md) |
| [RTPO](https://arxiv.org/html/2608.18682v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | reverse-turn optimization 联合处理 context mismatch、稀疏 credit 与 policy drift；3 + 3 + 2 = 8 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |
| [Gradient Mirage](https://arxiv.org/html/2608.18767v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 打破 split-interface gradient 与真实 label objective 的可逆一致性；3 + 2 + 3 = 8 | 深入完成 | 整合：PLATFORM-SECURITY，[Ch72](../../../../books/part-06-ai-infrastructure/72-security.md) |
| [SMTrap](https://arxiv.org/html/2608.18921v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 无模型反馈地用 SMT conflict 放大 reasoning compute DoS；3 + 3 + 2 = 8 | 深入完成 | 整合：PLATFORM-GATEWAY，[Ch62](../../../../books/part-06-ai-infrastructure/62-gateway.md) |
| [Test-Time Scaling in the Wild](https://arxiv.org/html/2608.18931v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | 开放任务中额外 compute 的瓶颈转为 exploitation/evaluator；2 + 2 + 3 = 7 | 深入完成 | 已有覆盖：PLATFORM-EVALUATION-SYSTEM，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) |
| [Harness Continual Learning](https://arxiv.org/html/2608.19013v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | frozen model 外的 prompt/memory/tool/skill/routing 共同形成可漂移适应状态；3 + 3 + 3 = 9 | 深入完成 | 整合：AGENT-MEMORY，[Ch77](../../../../books/part-07-agent/77-memory.md) |
| [Pre-Compiled Pipeline Shards](https://arxiv.org/html/2608.19147v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | AI PC fleet 用预编译 OpenVINO layer shards 建 pipeline inference；2 + 2 + 2 = 6 | 标准完成 | 已有覆盖：INFER-KSERVE-TOPOLOGY，[Ch53](../../../../books/part-05-inference-system/53-kserve-llm.md) |
| [SPADE](https://arxiv.org/html/2608.19197v1) | 2026-08-20T08:00:00+08:00 ～ 2026-08-20T09:00:00+08:00 | environment designer 与 learner 共演化 executable reset/step environment；3 + 3 + 2 = 8 | 深入完成 | 整合：TRAIN-GRPO，[Ch33](../../../../books/part-04-training-system/33-grpo.md) |

## 4. 证据与知识整合

### [Fractional Decay KV-Cache](https://arxiv.org/html/2608.18098v1)

双通道 scorer 同时保留历史 attention 与 topic-shift recency；它仍是 lossy eviction，结果受 dialog/model/budget 限制。Ch45 已覆盖 salience、decay、budget 与 drift。

### [Adversarial Review](https://arxiv.org/html/2608.18167v1)

reviewer 给判断、critic 审核判断，主 Agent 再决定编辑，避免大团队无界协作；受测 coding benchmark 不证明通用正确性。Ch80 已有 proposal/review/counterevidence/final owner 链。

### [Looped Language Models for Tool Calling](https://arxiv.org/html/2608.18171v1)

matched-SFT 比较显示 recurrence 对 compositional dependency 的收益高于独立调用。**已整合：** Ch78 区分 action protocol 与模型内部 recurrent compute；后者增加思考深度但不替代 tool receipt、state 与权限检查。

### [Reversible Forgetting](https://arxiv.org/html/2608.18177v1)

active/dormant/retired 状态允许过期知识退出决策又可恢复。**已整合：** Ch77 把“遗忘”改写为带依据、版本和恢复条件的 lifecycle；法规删除仍不能用 dormant 代替真正擦除。

### [Allocating Recurrent Compute](https://arxiv.org/html/2608.18230v1)

ITR/marginal ITR 判断重复 mixer 或 FFN 是否带来可观察的新 influence。受限模型实验只提供结构诊断；Ch18 已将共享层 recurrence 与 depth/compute trade-off 分开。

### [Cacheable by Design?](https://arxiv.org/html/2608.18261v1)

Qwen3 MoE edge 实测显示 disk bandwidth 与 paging thrash 主导，router locality 训练并未稳定消除 wall。它支持 Ch54 的“语义稀疏不等于物理权重可驻留”，不需新结论。

### [ComponentBench](https://arxiv.org/html/2608.18307v1)

97 类 UI component、2,910 个可程序验证 tasks 与 reference trajectories 提供中层诊断，但不代表开放桌面任务。Ch66 已有分层 evaluation 与 failure localization。

### [SingularClip](https://arxiv.org/html/2608.18319v1)

周期 clipping singular values 在受测 continual/RL tasks 缓解 plasticity loss；尚不足以外推 LLM 规模、optimizer 或 layer-wise policy，保留日报。

### [Task-Conditioned Least Privilege](https://arxiv.org/html/2608.18351v1)

4B 模型学习选择较小 authority，但执行前后均由 deterministic verifier 检查 state/effect。Ch72 已明确模型可提议权限、不能授予自身权限。

### [One Gate Is Not Enough](https://arxiv.org/html/2608.18360v1)

一个 gate 的 remediation 会改变后续 gate 看到的 action/evidence/context。**已整合：** Ch72 加入 remediate-and-regate：修改后使受影响 verdict 失效；仅在 bounded、idempotent operator 下可自动重跑。

### [LEDGER](https://arxiv.org/html/2608.18398v1)

系统从 observed session 生成 layered trace graph，使 claim 能追到 action、artifact 与 validation。**已整合：** Ch69 将 correlation trace 提升为 claim-evidence view，同时保留原始事件，图推断不能冒充已验证因果。

### [SparsePR](https://arxiv.org/html/2608.18484v1)

block routing 同 residual reconstruction 联合优化，说明 retained mass 不足以界定 post-softmax error；仍是特定视频模型近似。Ch24 已覆盖稀疏提议、校正和质量边界。

### [WhiteMatter](https://arxiv.org/html/2608.18486v1)

router 将每个 past token 的所有 layer states 混为 k 个 cached channels，改变 cache identity 与训练结构。**已整合：** Ch22 增加 cross-layer feedback branch；收益换来更高写入、router coupling 与 checkpoint 不兼容。

### [FlashAttention-V](https://arxiv.org/html/2608.18656v1)

vector architecture 通过 head 并行、inter-head packing 和 blocked reduction 复用数据；结果绑定 CPU ISA/vector length。Ch49 已将同一 attention 语义映射到硬件专用 execution plan。

### [RTPO](https://arxiv.org/html/2608.18682v1)

reverse-turn order 从靠近 terminal reward 的回合开始更新，并控制不同长度 trajectory 的 policy version。**已整合：** Ch33 在 multi-turn credit 后加入 update order/version coherence；并非所有任务都应反向，dense turn reward 时传统顺序更简单。

### [Gradient Mirage](https://arxiv.org/html/2608.18767v1)

防御让暴露 gradient 仍可训练却不再对应可由 label sequence 解释的真实 objective。**已整合：** Ch72 把 split-learning gradient 视为敏感接口；privacy transformation 必须同时证明 optimization utility 与 label unidentifiability，不能只加噪。

### [SMTrap](https://arxiv.org/html/2608.18921v1)

SMT conflict 提供低成本 search-amplification signal，生成会诱发大 reasoning budget 的输入。**已整合：** Ch62 的 admission/cost guard 增加 compute-amplification risk：按请求预算、progress、并发和中止策略限制，而非只限 token length。

### [Test-Time Scaling in the Wild](https://arxiv.org/html/2608.18931v1)

compute-normalized 比较把 token budget 分为 exploration 与 exploitation；开放任务受 evaluator 质量限制。Ch66 已要求 evaluator/selection contract，论文名称作为受限证据即可。

### [Harness Continual Learning](https://arxiv.org/html/2608.19013v1)

即使 model frozen，prompt、memory、tools、skills 与 routing 的更新仍可能破坏旧行为。**已整合：** Ch77 将 harness snapshot 作为联合状态并做 protected-slice regression；单项更新不能独立宣称 continual improvement。

### [Pre-Compiled Pipeline Shards](https://arxiv.org/html/2608.19147v1)

OpenVINO per-layer shards 在普通网络传 activation，使 16GB AI PC fleet 容纳更大模型；平台和网络结果不能外推数据中心。Ch53 已有 pipeline placement、artifact compatibility 与 network tail。

### [SPADE](https://arxiv.org/html/2608.19197v1)

同一 LLM 交替生成 executable environment 与作为 learner 训练，reset/step/verifier 固化环境接口。**已整合：** Ch33 将 environment generation 与 policy optimization 分权；新任务必须经过 sandbox、verifier 与 held-out gate，避免自生成漏洞变成 reward。

## 5. 缺口与下一步

无

10 项 Books 增量已写入相应机制正文；其余候选均已终态处置，没有剩余可执行工作。

## 6. 复核

复核者：`/root/aug09_16`
结论：通过

独立复核检查了 468 个 official-announcement 身份的首尾覆盖、21 项准入与漏项、exact-v1/withdrawn、§3/§4 以及 Books 落点。10 项新增机制位于对应章节的 `Review notes` 之前，明确区分内部计算、外部 effect、训练状态与证据责任；机器校验与 diff 检查通过。
