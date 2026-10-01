# 2026-09-17 Books Queue

本文件记录已经执行并经独立终审核验的 Books 串行队列。13 项建议写入均已进入声明的唯一 owner，12 项核对项均由既有正文具体论点承载；没有把论文列表追加到章末。

## 建议写入（13）

| Source family | Canonical owner | 要补的最小长期命题 | 写入边界 |
| --- | --- | --- | --- |
| 2609.15994 | `PLATFORM-SECURITY` / Ch72 | hidden-state monitor 的输入稳定性与 suffix observation point | 仅采用 typo rotation/decay 与受限 probe 证据，不推广到全部 monitor |
| 2609.16179 | `TRAIN-PRETRAINING` / Ch28 | loss regularizer 必须沿 backward transport 判断真实 update；MoE router 只作 handoff | 不把 low-coefficient 小模型结果写成通用稳定保证 |
| 2609.16183 | `MODEL-LONG-CONTEXT` / Ch22 | fixed-state recall 的能力瓶颈需分解 convolution/transition/interference/curriculum | 合成 recall 只解释机制，不代替语言 workload |
| 2609.16244 | `INFER-TENSORRT-LLM` / Ch49 | diffusion static schedule 允许 VLIW/engine co-design，但验收必须跑真实 denoising trajectory | 区分 synthesis、局部 P&R 与未完成 full-chip P&R |
| 2609.16540 | `MODEL-LONG-CONTEXT` / Ch22 | gating 可阻止 memorization shortcut，使 recurrence 学到可泛化 retrieval | 受控任务证据，不写成所有 SSM 的充分条件 |
| 2609.16682 | `PLATFORM-GPU-SCHEDULER` / Ch63 | reclaimable sharing 需把 entitlement deficit、preemption risk 与 interference 合成 assurance | 保留预测误差和集群差异的 failure mode |
| 2609.16745 | `MULTIMODAL-EMBODIED-VLA` / Ch26 | action latent 的价值必须用使用率、训练预算和公平 ablation 证明 | 反证只否定特定 ACT ablation，不否定所有 latent controller |
| 2609.16875 | `AGENT-RAG` / Ch76 | embedding 升级是旧索引兼容与新任务增益的迁移 contract | adapter 结果绑定作者模型/数据，不承诺零回填 |
| 2609.16898 | `PLATFORM-SECURITY` / Ch72 | private inference 必须联合 protocol、encoding、memory 与 hardware design | threat model 和 HE/MPC 参数不可省略；执行 handoff Ch49 |
| 2609.16937 | `TRAIN-RLHF` / Ch31 | on-policy distillation 的 credit horizon 应与 sequence reward 对齐 | 理论与作者实验是条件分支，不覆盖普通 token KD |
| 2609.17346 | `AGENT-RAG` / Ch76 | 外部知识放在 context、KV representation 或 parameters 是 workload-dependent branch | 明确 compression/retrieval/forgetting trade-off；KV handoff Ch45 |
| 2609.17372 | `MULTIMODAL-EMBODIED-VLA` / Ch26 | joint world/action backbone 可把异质视频经验和 simulator-generated recovery 闭成 policy loop | 只引用披露机器人/任务，保留 sim-to-real 与 filter bias |
| 2609.17416 | `AGENT-WORKFLOW` / Ch81 | continuous-time Agent 需要 interruptible workflow state；可验证 reward provenance 决定是否真的改善任务 | voice latency 与 ReactiveBench 数字只作案例；RL handoff Ch31 |

## 优先核对已有覆盖（12）

| Source family | Owner | 预计承载位置 | 只有出现真实缺口才改写 |
| --- | --- | --- | --- |
| 2609.16073 | `AGENT-MEMORY` / Ch77 | valid-time、supersession、contradiction、derived memory | 补“majority-vote trap/semantic shadowing”只在现有论点未覆盖时 |
| 2609.16450 | `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 | diffusion block decoding、uncertainty-based commit | 不为单一吞吐论文再建分支 |
| 2609.16617 | `INFER-KV-CACHE` / Ch45 | eviction correctness、first-divergence/evidence contract | 已有逐 token/trajectory error 分解则 No Change |
| 2609.16697 | `MULTIMODAL-WORLD-MODELS` / Ch25 | plausible→controllable→actionable 与闭环评价 | taxonomy 已经等价表达则只补 Review note/引用 |
| 2609.17008 | `INFER-SPECULATIVE-DECODING` / Ch48 | early-exit draft/verify、KV compatibility、offload trade-off | 现有 lossless branch 已承载则 No Change |
| 2609.17081 | `PLATFORM-EVALUATION-SYSTEM` / Ch66 | evidence perturbation、support/conflict/abstention 分解 | 40-quartet benchmark 不单独入正文 |
| 2609.17274 | `PLATFORM-SECURITY` / Ch72，handoff `AGENT-PLATFORM` | skill admission、多 scanner 独立校验 | 当前 Ch72/83/84 已有同一机制与数字，预计 No Change |
| 2609.17306 | `AGENT-MULTI-AGENT` / Ch82 | ensemble/routing 的 diversity 与 weakest-link boundary | 若已说明 pool 扩大并非单调收益则 No Change |
| 2609.17376 | `MODEL-LONG-CONTEXT` / Ch22 | ICL 内部 state 与 probe/intervention 证据边界 | HMM toy evidence 不应膨胀成独立正文 |
| 2609.17414 | `MULTIMODAL-REPRESENTATION` / Ch23，handoff Ch25 | object-centric latent/state owner | 已有 patch→object/slot 演进链则只补受限证据 |
| 2609.17419 | `PLATFORM-EVALUATION-SYSTEM` / Ch66，handoff `AGENT-MEMORY` | trajectory/local-global mismatch/terminal metric boundary | 不采用 universal criticality 类比；现有 trajectory evaluation 足够则 No Change |
| 2609.17521 | `MULTIMODAL-WORLD-MODELS` / Ch25 | structured scene memory、streaming control、state transition | 已有 persistent/revisable world state 与 control loop 则 No Change |

## 队列完成记录

1. Daily 候选表已记录最终 `整合` / `已有覆盖`、Stable Node ID 与章节链接。
2. 13 项实际写入均有唯一 `source-family` binding，并通过相邻论证与证据边界检查。
3. 12 项 Existing Coverage 均定位到既有论点，没有为形成 diff 重复追加同义内容。
4. fresh-context 非作者终审已通过；报告可标记为完成。
