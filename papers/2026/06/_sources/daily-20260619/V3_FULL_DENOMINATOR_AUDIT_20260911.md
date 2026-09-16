# 2026-06-19 V3 全量候选分母复核

## 审计范围

- canonical raw identities：590
- 旧 fresh-context 审计：67（47 retain / 20 close）
- 本轮补审：523
- 本轮全标题语义筛选：523 / 523
- 本轮完整摘要复核：82 个边界项
- 本轮初步恢复：23
- 独立反向剪枝：23 / 23
- 本轮最终恢复：18
- 本轮新增分母前关闭：505（初筛关闭 500 + 终审降级 5）
- 合并后的最终分母：64（旧最终 46 + 恢复 18）
- 全量分母前关闭：526（旧 21 + 本轮 505）

这份记录纠正旧报告把“审计 67 个旧边界项”误写成“完成 590 项候选分母”的问题。标题含义明确且属于范围外或仅应用增量的材料按合同在标题阶段关闭；标题含糊、可能改变模型/训练/推理/平台/Agent 设计判断的材料读取完整摘要。没有因为能映射 ROADMAP、出现系统术语或便于写入 Books 而准入。

## 恢复候选终审

| arXiv | 题摘显示的待核验增量 | 暂定 owner | 审阅深度 |
| --- | --- | --- | --- |
| 2606.19348 | 百万 token 场景把 hybrid compressed attention、异构 KV、context parallelism 与可恢复 rollout runtime 组成同一设计链 | `MODEL-LONG-CONTEXT` | 深入；保留；Existing |
| 2606.19354 | verifier 粒度随难度、准确率与 compute budget 变化，ORM/PRM 不再是静态二选一 | `INFER-SCHEDULING` | 标准；保留；Integrate |
| 2606.19388 | mobile agent 的 GUI/CLI interface 是 observation/action contract，而不是固定前提 | `AGENT-TOOL-CALLING` | 标准；保留；Existing |
| 2606.19453 | full-duplex 系统需要区分决策层、交互类型与逐时刻状态机，架构能力不能替代训练/评测覆盖 | `MULTIMODAL-REPRESENTATION` | 深入；保留；Existing |
| 2606.19475 | DLM 质量—效率结论必须绑定 denoising steps、block size、context 与 unmasking policy | `MULTIMODAL-GENERATIVE-PARADIGMS` | 标准；保留；Existing |
| 2606.19531 | world-action context 可由 image-editing denoising KV 提供，不必先生成完整未来视频 | `MULTIMODAL-EMBODIED-VLA` | 标准；保留；Existing |
| 2606.19558 | KLD/PPL 在明显退化区可作粗筛，却不能在 near-baseline quant silent zone 排序或路由 | `PLATFORM-EVALUATION-SYSTEM` | 深入；保留；Existing |
| 2606.19607 | preference-pair 标注预算应作为 sampling design，并通过信息矩阵连接到 DPO policy gap | `TRAIN-DPO` | 深入；保留；Integrate |
| 2606.19636 | pass@k=0 会把“普通采样未到达”误写成“模型不可解”，从而污染 curriculum 与 verifier data | `PLATFORM-EVALUATION-SYSTEM` | 深入；保留；Existing |
| 2606.19744 | sequential DPO 的遗忘依赖 objective compatibility、signal strength 与 order，不是统一衰减 | `TRAIN-DPO` | 标准；保留；Integrate |
| 2606.19919 | fast/slow reasoning 的效率 credit 可只作用于 mode-selection state，避免惩罚正确长轨迹 | `TRAIN-GRPO` | 标准；保留；Existing |
| 2606.20008 | policy-implied value 尝试在不训练独立 critic 时恢复 token-level credit，重画 GRPO/PPO 分支边界 | `TRAIN-GRPO` | 深入；保留；Integrate |
| 2606.20075 | latent reasoning 同时面临 optimization-path gradient attenuation 与 representation drift，需要区分 trajectory/space supervision | `TRAIN-PRETRAINING` | 标准；保留；Integrate |
| 2606.20092 | 长时 VLA memory 可按未来因果效用选择性保存视觉证据，而不是积累完整历史 buffer | `MULTIMODAL-EMBODIED-VLA` | 标准；保留；Integrate |
| 2606.20097 | hybrid attention 的选择粒度可从 layer 下沉到功能异质的 head，并把 retrieval-critical heads 留给 full attention | `MODEL-LONG-CONTEXT` | 深入；保留；Existing |
| 2606.20104 | inverse dynamics 可同时阻止 latent world state collapse 并保留 action-controllable information | `MULTIMODAL-WORLD-MODELS` | 深入；保留；Integrate |
| 2606.20225 | misalignment activation direction 的 within-model causal specificity 不能外推成 cross-model transferable monitor | `PLATFORM-SECURITY` | 深入；保留；Integrate |
| 2606.20560 | diffusion reasoning 的 variable transparency 与 algorithmic transparency 是两种不同 contract；token bottleneck 只恢复前者 | `MULTIMODAL-GENERATIVE-PARADIGMS` | 标准；保留；Integrate |

## 独立反向剪枝

| arXiv | 最终决定 | 分母前关闭理由 |
| --- | --- | --- |
| 2606.19549 | Close | MergeProbe 只在 MERGE-PEFT 的小规模 pilot 中预测 adapter pair/set 的后续 merge 结果；它复用 update、gradient、Fisher 与 activation overlap 作为特征，没有给出新的 merge state、正确性 contract 或跨规模可行性边界。现有 `TRAIN-LORA` 已要求 composition/merge 重新评估与保留 lineage。 |
| 2606.19616 | Close | `grite` 将 append-only signed log、CRDT projection、advisory lease 与 dependency graph 组合到 git ref；这些是成熟协调机制。定量结论来自 deterministic synthetic op-generators 与抽象 task pool，未提供真实 LLM coding-agent 的新增可靠性边界，不能把产品 artifact 的实现案例升级为长期新机制。 |
| 2606.19819 | Close | CREDENCE 在事实核查的 claim decomposition 上组合 LLM decomposer、rule verifier、一次 repair 与 embedding metric；oracle parser 下的 termination 和局部 benchmark 不改变本项目现有 claim-level evidence、typed claim 与 verifier/repair ownership。它是领域 pipeline 改良，不是新的通用 evaluation contract。 |
| 2606.19857 | Close | BabelTele 是 prompt 诱导的 symbolic compression empirical probe，效果依赖 compressor-reader pair、任务和特定 prompt family；没有稳定协议、训练机制或可审计的语义等价保证。当前证据不足以改变 `AGENT-CONTEXT` 的 context identity 或发布判断。 |
| 2606.20058 | Close | 论文用 mock agents 在 production-derived scenario 上比较 ReAct、DAG 与 Task Manager；agent-discovery noise 与 latency 数字没有真实 LLM execution、tool failure 或 production tail-SLO 支持，且 DAG/backlog/preemption 已是现有 owner 的成熟分支。该结果不能改变 multi-agent 设计判断。 |

## 边界项关闭校准

本轮另对 59 个可能相关但最终关闭的边界摘要进行了复核。代表性关闭理由如下：

- 仅提出局部 pruning、compression、prompt 或 schedule 变体，题摘没有显示会改变已有机制的适用边界；
- 仅在医疗、法律、自动驾驶、天气、硬件设计或其他领域应用现有模型，属于当前暂缓的领域增量；
- 只新增 benchmark/task 条目，没有暴露原评价遗漏的能力、混杂因素或 release condition；
- 只给出单一模型或单一 workload 的小幅结果，没有可定位的新状态、控制权或可靠反证；
- 理论对象与 LLM/LLM Infra 的连接只来自审阅者类比，原文没有建立直接机制关系。

具体 identity、标题、完整摘要和原始 family-specific closure reason 继续保存在 `canonical-raw-identity-inventory-v2.1.json.gz` 与 `canonical-semantic-screening-checkpoint-v2.1.json.gz`。本记录只保存 fresh-context 复核的变化和共同校准，不复制 590 行账本。

## 最终 Gate

- Coverage / raw denominator：590 / 590 已闭合；64 candidate / 526 pre-denominator close 已冻结。
- Evidence：18 个最终恢复候选均已核对 exact-v1 Method、Evaluation 与 limitations；5 个降级项保留已读证据与关闭理由。
- Books：9 个 owner-level 语义增量已进入 canonical owner 正文并通过独立 post-write audit；9 个恢复候选已定位到 Review notes 前的现有命题。
- Complete：是；22 Integrated / 42 Existing / 0 queued。
