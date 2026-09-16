# 2026-06-19 恢复候选 Evidence 与反向剪枝审计

## 审计身份与边界

- 复核者：`june_19_recovered_candidates`
- 审计日期：2026-09-11（Asia/Shanghai）
- 输入：590 个 canonical raw identities、上一轮最终 46 个候选、523 个补审身份中的 23 个初步恢复项。
- 日期边界：本批 identity 保持 official listing batch 的 2026-06-19 owner；未用 arXiv `submitted` / v1 timestamp 或正常发布时间表推算 actual first-public，也未迁移日期。
- 版本边界：23 项均从 `/private/tmp/j19-<id>.html` 核对 `arXiv:<id>v1`；无 withdrawn 标记，无正文受阻。
- 复核方法：先逐项重读 title + full abstract，再按准入命题定点读取 exact-v1 Method、Evaluation 与 limitations；最后对读 owner 正文并执行“删除论文名后是否仍改变既有设计结论、状态或控制权”的反向剪枝。
- 限制：本 Evidence 复核者处于 subagent 上下文；Books 写入后已由 `june_19_postwrite` 进行独立正文级复核。

## 最终保留 18 项

| arXiv | Evidence locator | 证明边界 | V2 | Owner | Books |
| --- | --- | --- | --- | --- | --- |
| 2606.19348 | §2 Architecture；§3 General Infrastructures；§4–§6 training/evaluation | 百万 token 是 attention、communication、KV placement 与 runtime 的联合合同；不证明任意位置有效利用或生产 SLO | 3+3+3=9 | `MODEL-LONG-CONTEXT` | Existing |
| 2606.19354 | §3 Problem Formulation/Assumptions/Theorems/GRACE-Adapt；§4 Experiments | verification granularity 随难度、准确率、预算变化；依赖单调性/log-concavity 等假设，未验证生产延迟 | 2+2+2=6 | `INFER-SCHEDULING` | Integrate |
| 2606.19388 | §3–§4 setup/suite；§5 results；§6 limitations | GUI/CLI 是不同 observation/action contract；只覆盖 terminal-reachable state | 2+2+2=6 | `AGENT-TOOL-CALLING` | Existing |
| 2606.19453 | §4 architecture hierarchy；§5 ontology；§6 state machine | 分离 full-duplex 决策层、交互类型与时序状态；survey 无统一受控 benchmark，L3 未实现 | 2+2+3=7 | `MULTIMODAL-REPRESENTATION` | Existing |
| 2606.19475 | §4 setup；§5 analysis；§6 conclusion | DLM 排名依赖 steps/block/context/unmasking；跨模型训练配置不能支持无条件范式结论 | 2+2+2=6 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Existing |
| 2606.19531 | §3 architecture/action/inference；§4 experiments | denoising KV 可在 final frame decode 前 handoff 给 action expert；不证明安全或普遍 sim-to-real | 2+2+2=6 | `MULTIMODAL-EMBODIED-VLA` | Existing |
| 2606.19558 | §3 methodology；§4 silent zone；§5 direction；§6 limitations | KLD/PPL 在 near-baseline 区不能稳定排序下游质量；阈值只对所测 cohort 有效 | 3+2+3=8 | `PLATFORM-EVALUATION-SYSTEM` | Existing |
| 2606.19607 | §2 problem/assumptions；§3 design/theory；§4 experiments；§5 limits | pair sampling design 改变 DPO information coverage；只在理论前提与离线设计内成立 | 2+2+3=7 | `TRAIN-DPO` | Integrate |
| 2606.19636 | §3 setup；§5 blind spot；§6 mechanism；§7 utility；§8 limits | pass@k=0 不等于不可解；residual intervention 不是普通 decoding，且多数项仍未恢复 | 3+2+3=8 | `PLATFORM-EVALUATION-SYSTEM` | Existing |
| 2606.19744 | §2 sequential DPO；§3 protocol；§4 results；§5 limits | preference change 依赖 objective/order/signal，需 pair-level ledger；只覆盖一个 8B LoRA 设置 | 2+2+2=6 | `TRAIN-DPO` | Integrate |
| 2606.19919 | §3 SFT/GRPO；§4 experiments；§7 limitations | efficiency reward 可只绑定 mode-selection token；只验证二元模式与有限模型/任务 | 2+2+2=6 | `TRAIN-GRPO` | Existing |
| 2606.20008 | §3 policy-implied value；§4 experiments；§5 limitations | log-ratio recurrence 形成 critic-free value 分支；fixed reference、beta 与 exact-KL 仍是风险 | 2+2+3=7 | `TRAIN-GRPO` | Integrate |
| 2606.20075 | §3 optimization barrier；§4 supervision；§5 information view；Appendix A | latent-CoT 有 optimization-path 与 representation-space 两个失败轴；非通用可解释性定理 | 2+2+2=6 | `TRAIN-PRETRAINING` | Integrate |
| 2606.20092 | §3 EventVLA/KEM；§4 benchmark；§5 experiments；§6 limits | predictive keyframe write 要早于 evidence loss；threshold/FIFO/label pipeline 可漏写或覆盖 | 2+2+2=6 | `MULTIMODAL-EMBODIED-VLA` | Integrate |
| 2606.20097 | §4 head selection/hybrid transfer；§5 experiments；Appendix C caveats | head-level full/linear allocation 可行；主要证据只来自一个 compact dense model | 2+2+3=7 | `MODEL-LONG-CONTEXT` | Existing |
| 2606.20104 | §3 method；§4 latent structure；§5 planning；§6 discussion；Appendix A | inverse dynamics 抗 collapse，但要求 action 可由相邻观察恢复并受 offline coverage 限制 | 2+2+3=7 | `MULTIMODAL-WORLD-MODELS` | Integrate |
| 2606.20225 | §3 methodology；§4 results；§5 implications；§6 limits | within-model direction 可有因果 specificity；cross-model 映射未通过同等 control specificity | 3+2+3=8 | `PLATFORM-SECURITY` | Integrate |
| 2606.20560 | §2 serial depth；§3 bottleneck；§4–§5 monitor/reasoning；§8.1 limits | variable transparency 不等于 algorithmic transparency；serial depth 只是 bound | 2+2+2=6 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate |

## 反向剪枝关闭 5 项

| arXiv | 决定 | Family-specific closure |
| --- | --- | --- |
| 2606.19549 | Pre-denominator Close | MergeProbe 只在小规模 MERGE-PEFT pilot 中用 overlap 特征预测 merge 结果；没有新的 merge state、正确性 contract 或跨规模边界。`TRAIN-LORA` 已要求 composition/merge 重评与 lineage。 |
| 2606.19616 | Pre-denominator Close | `grite` 将 signed append-only log、CRDT projection、advisory lease 与 dependency graph 组合进 git；定量结果来自 deterministic synthetic operations 和抽象 task pool，没有真实 LLM coding-agent 的新增可靠性边界。 |
| 2606.19819 | Pre-denominator Close | CREDENCE 是 fact-check 领域的 claim decomposition + rule verifier + 一次 repair + embedding metric；oracle-parser termination 与局部 benchmark 不改变现有 typed claim/evidence/verifier ownership。 |
| 2606.19857 | Pre-denominator Close | BabelTele 是 prompt-induced symbolic compression probe，结果依赖 compressor-reader、任务和 prompt family；没有稳定协议、训练机制或可审计语义等价保证。 |
| 2606.20058 | Pre-denominator Close | mock agents 上的 DAG/backlog/preemption 比较没有真实 LLM execution、tool failure 或 production tail-SLO；成熟协调原则的应用实例不足以改变现有 multi-agent owner。 |

## Gate

- Coverage：590 / 590 raw identities 已获得候选或分母前关闭终态。
- Candidate denominator：64（旧最终 46 + 恢复 18）。
- Pre-denominator closure：526（旧 21 + 本轮初筛 500 + 终审降级 5）。
- Evidence：18 / 18 恢复候选完成 exact-v1 定点审阅；blocked=0，withdrawn=0。
- Books：9 Integrate 已写入并通过独立 post-write audit；9 Existing 已对读 Review notes 前正文。
- Daily Complete：是；queue=0。

## Independent Books Gate（2026-09-11）

独立 reviewer `june_19_books_gate` 重新读取 12 个 proposal 的 exact-v1 题摘/Method/Evaluation/limitations，并对读 9 个 owner 章节在 `## Review notes` 前的正文。三项不是新增长期结论：`2606.19531` 已由 Ch26 `World-action model` 的 latent predictive interface 与 physical commit boundary 覆盖；`2606.19558` 已由 compression release 与 threshold-adjacent evidence contract 覆盖；`2606.19919` 是 GRPO 章 typed credit / state-action boundary 的二元实现案例。其余 9 项保留 Integrate，并已由 root 写入、由 `june_19_postwrite` 完成另一轮独立复核。

## Post-write Gate（2026-09-11）

9/9 marker 精确唯一并位于 canonical owner 的首个 `Review notes` 前；正文均形成旧路径、约束变化、机制与 owner/state flow、收益、trade-off/failure、fallback 和 exact-v1 non-proof boundary。`2606.20075`、`2606.20092`、`2606.20104`、`2606.20225` 的初始落点破坏章节顺序，已移回对应核心机制主线。最终为 22 Integrated / 42 Existing / 0 queued。
