# 2026-05-08：十项 false negative 作者限定返修

## 范围与状态

本轮只重开 `V3_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_NINE_20260915.md` 点名的 10 项，不重枚举 619 个 identity，不重审已通过的 141 项 Evidence 或 6 个 Books 段，也不编辑共享 Books。`2605.05709` 已由 root 写入 Ch72，本轮只同步其状态。

10/10 exact-v1 HTML 可访问且未见 withdrawal banner；8 项 Deep、2 项 Standard。`2605.05676` 虽为 6 分，但因 Books Integration Gate 已提升为 Deep。返修后机械账为 `619 = 151 retained + 468 closure`，Evidence 为 151/151 complete。10 项中 5 项形成精确 root 写回队列且已由 root 落入对应 Books 主正文，另 5 项由当前正文的具体命题承载；`2605.05709` 也已由 root 补入 Ch72 并从 No Change 改为 `Integrate — Applied`。作者不能自签最终 Gate，日报保持 `Ongoing`。

## 十项 Evidence 与 Books Decision

### 2605.05566 — LoPE

LoPE 针对 GRPO 全失败 group 的 zero-advantage 与重复采样低收益，把探索 actuator 从 logit temperature 扩展到 prompt-space perturbation，再通过 response regrouping、importance-ratio shaping 与 advantage shaping恢复稀有成功轨迹的训练信号。作者只在 Qwen3-1.7B/4B、Qwen2.5-Math-7B、OpenR1-Math 与所列数学 benchmark 上比较，并使用 4/8 张 80GB A100；随机 Lorem、off-policy correction、取消 KL 与任务理解损伤都进入方法边界。

**Score / owner：** `2+2+2=6`，Standard；`TRAIN-GRPO`。Ch33 已明确区分入口收窄与进入后的完成能力，并要求 exploration signal 只控制采样、group builder 固定 membership、outcome verifier 保留真值权以及重采样收益递减时使用 bounded intervention/fallback。结论：`No Change — Existing Coverage`。

### 2605.05602 — Nearly Optimal Attention Coresets

论文在 unit-norm keys/values、bounded query radius 与 additive error 下证明 softmax attention 存在与序列长度无关的 subset coreset，并给出 matching communication/coreset lower bounds。它直接限定“attention state 能压到多小”，但主要是存在性/理论边界，不是生产可执行的 causal KV eviction 算法，也不保留逐 token provenance。

**Score / owner：** `3+2+3=8`，Deep；`MODEL-LONG-CONTEXT`。Ch22 已比较完整 KV、recurrent state 与 compressed checkpoint，却没有这条带 upper/lower bound 的 attention-subset 可行性边界。结论：`Integrate — Applied`。

### 2605.05676 — Badit

Badit 用高奇异值方向初始化多个 LoRA experts，再按 rank-1 component 的当前梯度方向做动态分组，使 expert 间近似正交、expert 内更一致，从而缓解 multi-task instruction tuning 的共享参数干扰。SuperNI、六个 LLM、五 seed 与 gradient-angle/ablation 支持受限机制；DOG 包含 CPU spherical clustering 与 integer optimization，作者报告相对 LoRAMoE 平均约 `1.22×` 训练时间，不能外推为通用能力分解。

**Score / owner：** `2+2+2=6`；因进入 Books，按 Integration Gate 提升为 Deep；`TRAIN-LORA`。Ch30 已有静态奇异子空间解除 expert cold-start，却未说明训练会重新破坏正交性及如何维护动态 grouping state。结论：`Integrate — Applied`。

### 2605.05781 — UNO

UNO 冻结 understanding expert，让它从 noised generative representation 解码语义重述或回归视觉 encoder 特征，使理解损失的梯度进入生成路径；prompt masking、semantic re-caption 与 metaquery 用于限制条件复制和目标泄漏。证据限 BAGEL-7B、5K iterations、作者图像生成/编辑数据与 benchmark，PCA 可视化和 judge 分数不能证明一般表征因果或所有模态收益。

**Score / owner：** `3+2+2=7`，Deep；`MULTIMODAL-GENERATIVE-PARADIGMS`。Ch24 已有 unified generation 的共享状态与 modality interference，但没有 frozen understanding expert → generative representation 的监督路径及 leakage boundary。结论：`Integrate — Applied`。

### 2605.05826 — AGPO

AGPO 用 group variance 约束正向相对 advantage，并为错误路径保持 gated negative signal，试图减缓 RLVR 对 base-policy reasoning support 的收窄。作者在三类 LLM、五个数学 benchmark 与一个 JD search-ads teacher pipeline 上报告 pass@k、entropy、PIR 和两天 A/B 指标；这些数字受 reward、group size、KL、256-sample evaluator 与业务分布约束，不构成通用边界保持保证。

**Score / owner：** `3+2+2=7`，Deep；`TRAIN-GRPO`。Ch33 已把 zero-positive group、negative update、入口概率与条件完成率、pass@k coverage、entropy 与 verifier authority 分开，并保留普通 group sampling/regularization。结论：`No Change — Existing Coverage`。

### 2605.05893 — LoVer

LoVer 从白盒 LLM hidden state 训练二层 MLP verifier，以 negation、同答案组内一致性和答案组间唯一正确三类逻辑约束替代人工标签。该 sensor 假设候选中至少有一个正确答案，且同一 final answer 的 reasoning truth 可合并；实验覆盖 GSM8K、MMLU-Pro、HotpotQA、BIG-Bench Hard/iGSM 与若干 OOD split，但没有外部 correctness oracle，也不适用于黑盒模型。

**Score / owner：** `3+2+2=7`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 已明确 hidden-state probe、self-consistency 与 learned verifier 只能形成校准 sensor，不拥有 truth，漂移或白盒状态不可得时必须回退外部证据、deterministic verifier 或 abstention。结论：`No Change — Existing Coverage`。

### 2605.06460 — MINER

MINER 冻结视觉文档 retriever backbone，以逐层 probe、validation-driven neuron mask 与多层 fusion 形成单一 compact embedding，在不改变向量维度与搜索复杂度的前提下利用内部层信号。ViDoRe、三个 backbones 与 Qdrant 对照只支持所列 retrieval/index 条件；训练数据可用性、layer/mask 选择、validation overfit 与未披露生产并发限制外推。

**Score / owner：** `2+2+2=6`，Standard；`AGENT-RAG`。Ch76 已把 late-interaction 质量、multi-vector storage/memory traffic、single-vector 吞吐与 budgeted compression/fusion 统一为 persisted index frontier，并要求 encoder/vector budget/distance rule/rebuild provenance。结论：`No Change — Existing Coverage`。

### 2605.06507 — MARBLE

MARBLE 保留每个 reward 的独立 advantage 与 policy gradient，再用约束优化选择共同 update direction；为避免每步 `R+1` 次 backward 和单 batch 系数抖动，周期性求解并用 EMA 平滑、其余 step 复用标量系数。实验限 SD3.5-M、rank-32 LoRA、五个 reward、16 H200 与作者图像指标，未证明更大 reward set、视频/world model 或生产稳定性。

**Score / owner：** `3+2+3=8`，Deep；`TRAIN-RLHF`。Ch31 已有根据梯度方差/方向分歧调整混合权重的原则，但没有 per-reward advantage/gradient ownership、QP harmonization 与 amortized coefficient state。结论：`Integrate — Applied`。

### 2605.06557 — Coordination Matters

STAT 在 commitment-constrained spatial task allocation 中把 return 与 conflict count/rate、conflicts per task、assignment diversity、throughput 分账，并沿 agent/task/environment 三个轴做 matched scaling。五 seed、A100、2M/20M timestep 与 95% CI 支持该受控诊断；环境刻意排除 partial observability、通信、异构 Agent、拥塞与复杂路径，不能外推开放式 LLM Agent。

**Score / owner：** `3+2+3=8`，Deep；`AGENT-MULTI-AGENT`。Ch82 已要求 outcome 与 overlap/conflict/commit/rebase/tests/executable result/coordination cost 同时记录，并明确 throughput、重复动作、handoff 和恢复属于不同证据。结论：`No Change — Existing Coverage`。

### 2605.06643 — MMDG-Bench

MMDG-Bench 固定 splits、batch、optimizer、training-domain model selection 与 search budget，对六数据集、三任务、六 modality configurations、九方法进行统一比较，再单独测试 corruption、missing modality、MisD 与 OOD。结果显示 clean ranking、故障鲁棒性和不同 trustworthiness 指标会互相反转；论文只覆盖 discriminative/regression、两种 corruption 与所列 backbone，不能外推生成任务或生产 sensor failure。

**Score / owner：** `3+2+3=8`，Deep；`PLATFORM-EVALUATION-SYSTEM`。Ch66 有通用 distribution/slice 与 calibration 原则，但没有把 clean multimodal ranking、missing-modality/corruption、MisD 与 OOD 明确列为不可替代的证据轴。结论：`Integrate — Applied`。

## 同错误理由的有界 sibling challenge

未扩大 raw set。本轮重放此前已经题摘审阅的 11 个同类高风险 closure：`2605.05662`、`2605.05668`、`2605.05742`、`2605.05758`、`2605.05914`、`2605.06070`、`2605.06170`、`2605.06201`、`2605.06318`、`2605.06509`、`2605.06667`。它们分别因为 benchmark/data asset 没有新增长期 contract、诊断或线性理论没有部署 control delta、领域/单点 adapter 缺可迁移边界、现有 reward/evaluation owner 已有等价命题，继续保持 family-specific pre-denominator closure；没有发现第 11 个新增 false negative。

## `2605.05709` root-applied 同步

Root 已在 `books/part-06-ai-infrastructure/72-security.md` 的主正文、真正 `## Review notes` 前写入 `SF-2026-ARXIV-2605-05709`，覆盖 raw-view concealment → trusted reconstruction → model context、data/reconstruction 双层检查、作者 benchmark 边界与 fallback。其 Books disposition 改为 `Integrate — Applied`；写回证据为 `ROOT_BOOKS_WRITEBACK_2605_05709_20260915.md`。

## 作者检查点

- 10/10 exact-v1 可访问；withdrawn 0、blocked 0、disputed 0。
- `619 = 151 retained + 468 closure`；151/151 Evidence complete，109 deep + 42 standard，`Review Pending = 0`。
- Books 当前为 76 Applied、5 项 root writeback required、70 No Change；合计 151。
- 作者未编辑 Books，未自签 final Gate。Root 完成 5 项精确写回后，仍须由新的 non-author reviewer 复核本轮变化范围。
