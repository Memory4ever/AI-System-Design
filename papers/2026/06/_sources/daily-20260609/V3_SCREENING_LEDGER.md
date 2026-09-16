# 2026-06-09 V3 strict screening ledger

> **Final authority（2026-09-11）：** 作者侧 `125 / 1,110` 与第一轮非作者 `115 / 1,120` 均保留为审计历史。第二轮 full-table audit 进一步关闭 2606.07909、2606.08300、2606.08702，最终 authority 为 **1,235 = 112 Candidate + 1,123 Close**。三项分别是既有 memory 组合、LLM 生成依赖图加 DFS 的薄封装、既有 graph-memory pattern 的局部实现，均未形成新的 state/control/evaluation contract。权威结论见 [`../JUNE_09_SECOND_FULL_TABLE_AUDIT.md`](../JUNE_09_SECOND_FULL_TABLE_AUDIT.md)。112 项均为已有覆盖，new Integrate = 0，正文缺口 = 0。

## Authority and baseline

本记录按当前 V3 合同重冻题摘分母，不继承旧 `Complete`、candidate disposition 或 Books 决定。可读 canonical packet 包含 1,235 个去重 identity：99 个 old prior 与 1,136 个 closure proposal。逐项 title、完整 abstract 与旧 family-local reason 位于两个 canonical gzip packet。

准入只看完整摘要能否证明可迁移的长期 design delta：改变 state/data/control ownership、execution/evaluation/release contract、系统级机制取舍，或修正 Books 既有结论。大模型对象、章节映射、局部模型/adapter/benchmark/单任务性能不构成准入。

## Author-side prior frontier reaudit（历史 checkpoint）— 77 retain / 22 close

以下 77 项满足严格门槛；旧 Books disposition 不继承：

| 机制族 | IDs | 严格准入依据 |
| --- | --- | --- |
| training/inference/runtime data plane | 2606.07632、2606.07684、2606.07703、2606.07710、2606.07713、2606.07726、2606.07846、2606.07878、2606.07881、2606.07923、2606.08094、2606.08197、2606.08317、2606.08382、2606.08411、2606.08476、2606.08635、2606.08761、2606.08891、2606.08950、2606.09061、2606.09441、2606.09613、2606.09643、2606.09682、2606.09686 | lifecycle resource accounting、semantic cache、sparse prefill、speculative routing、memory-optimal kernels、evaluation-cost bandit、workflow speculative execution、KV compaction、async pipeline、semantic query optimizer、VLA runtime、federated fine-tuning、AI-ready database、KV/rank、diffusion decode、context parallel、PD KV transfer、W4A4、PIM、vector DB scaling、chunked-prefill scheduling、RAG prefill、Agent serving simulation、model virtualization、checked megakernel 与数值 conformance 都给出可执行资源/通信/兼容合同。 |
| Agent state/control、memory、workflow 与 platform | 2606.06545、2606.07631、2606.07904、2606.08049、2606.08106、2606.08348、2606.08367、2606.08539、2606.08590、2606.08671、2606.08702、2606.08755、2606.08790、2606.08806、2606.08867、2606.08919、2606.09692 | governed MCP、finetuning monitoring、tool precondition/effect、formalized skill execution、anytime acceptance、Bayesian skill evolution、long-horizon autonomy、trust layer、Kubernetes RCA、persistent decision history、structured multi-agent memory、skill/policy co-evolution、commerce clearing、test-artifact governance、100M-user Agent framework、human oversight capacity 与 delegated-execution observability 均明确分配持久状态、控制或验收责任。 |
| evaluation/release/security contract | 2606.06529、2606.07783、2606.07790、2606.07805、2606.07808、2606.07822、2606.07833、2606.07834、2606.07845、2606.07867、2606.07874、2606.07889、2606.07936、2606.07943、2606.07968、2606.07992、2606.08200、2606.08340、2606.08372、2606.08381、2606.08403、2606.08417、2606.08433、2606.08529、2606.08531、2606.08625、2606.08661、2606.08679、2606.08831、2606.08840、2606.08893、2606.08960、2606.09005、2606.09084 | 覆盖 RAG evidence、Byzantine coordination、dynamic compliance、instruction hierarchy、activation calibration、process-mined attacks、judge mixed evidence、coordination negative result、cold-start、contextual judge、trajectory pre-failure、human-eval protocol、skill injection、runtime consumption、authority mutation、online judging、open coordination、reconstruction/privacy、alignment audit、steganographic carrier、distributional perplexity、sandbox security、scaffold effect、scenario safety、rubric evolution、data-Agent security、leaderboard interval、conformal factuality、execution-grounded code eval、reward-hacking detector、benchmark hardening、RAG control-signal attack 与 provenance-fracture attack。 |

以下 22 项严格关闭：2606.07687、2606.07720、2606.07856、2606.07950、2606.07957、2606.07970、2606.08302、2606.08346、2606.08432、2606.08446、2606.08483、2606.08486、2606.08517、2606.08574、2606.08610、2606.08615、2606.08769、2606.08779、2606.08813、2606.08869、2606.08892、2606.09774。它们分别停留在局部 world-model/latent/reward/finetuning/KV/decoder 方法、非大模型 cloud security/ANN/network estimator、robot/video/health/radiology垂直任务或通用 conformal/data pruning；没有跨 workload 合同。2606.09774 是 AI-for-Science simulator 配置的轻量 coding adapter，按当前范围延后，因此即使旧 Books 已有正文也必须撤回采用链。

## Author-side closure proposal reaudit（历史 checkpoint）— 48 recover / 1,088 close

1,136 项 closure proposal 均按 title-first 复审；边界不清时读取 canonical raw inventory 的完整 abstract。恢复项按其真实合同分组如下：

| 恢复族 | IDs | 严格恢复理由 |
| --- | --- | --- |
| training/inference/runtime（16） | 2606.07571、2606.07577、2606.07581、2606.07586、2606.07587、2606.07665、2606.08090、2606.09079、2606.09080、2606.09138、2606.09200、2606.09508、2606.09514、2606.09537、2606.09551、2606.09659 | 分别新增 DLM shared-prefix KV、流式多模态 memory budget、train/infer kernel contract、NPU deployment skill gate、router predictability ceiling、checked CUDA compiler、semantic filtering execution、超长上下文索引、真实 pruning acceleration、Agent-RL step data middleware、multi-GPU overlap、head/context adaptive inference、budgeted depth、semantic scheduling、secure-inference compiler 与可扩展 context compression。 |
| Agent state/control/memory/workflow（14） | 2606.07711、2606.07909、2606.08151、2606.08275、2606.08300、2606.09090、2606.09122、2606.09316、2606.09421、2606.09447、2606.09483、2606.09549、2606.09730、2606.09751 | 分别处理 cross-LLM memory、user/environment-feedback memory、decision-aware memory cards、counterfactual failure attribution、multi-tool plan、configuration context rot、闭环 incident resolution、knowledge-to-skill compiler、skill quality-cost、real-cloud rollout isolation、dual-process memory、双边界 Agent security、delegation context budget 与可签名 human-agent handoff。 |
| evaluation/release（12） | 2606.07595、2606.07623、2606.07624、2606.07682、2606.08044、2606.09046、2606.09071、2606.09376、2606.09426、2606.09461、2606.09748、2606.09764 | 分别把 visual-to-tool boundary、finite semantic certificate、sequential monitoring、超长 SWE、representation-level safety、decoy+holdout audit、replay-verified attribution、faithfulness+coverage、hybrid-interface CUA、human-human multimodal memory、process-feedback deep research 与 persistent-personal iOS 环境变成可复验验收合同。 |
| security/data provenance（6） | 2606.07937、2606.07963、2606.07996、2606.09060、2606.09401、2606.09411 | 分别覆盖多 Agent hallucination 传播、共享 latent backdoor、black-box pretraining data detection、trace-driven CVE version attribution、DP adaptation empirical privacy 与 evasive steganography，均修正安全/数据审计边界。 |

其余 1,088 项维持 pre-denominator Close。canonical checkpoint 已为每项保存 title、abstract evidence 与 family-local reason；本轮逐题确认后归入实际缺口：非大模型系统或 AI-for-Science/垂直应用；局部 model/adapter/quant/reward/generation/VLA 方法；单一 benchmark/data set；或只有风险/taxonomy 而没有长期 owner、控制点与可执行验收协议。

## Fresh-context FP/FN sample

遮蔽旧标签抽查 12 retain：2606.07581、2606.07586、2606.07665、2606.07881、2606.08106、2606.08635、2606.09046、2606.09122、2606.09316、2606.09549、2606.09659、2606.09751。完整摘要均可定位到 kernel/state/control、通信、调度、评测或发布合同。

抽查 12 close：2606.07527、2606.07603、2606.07687、2606.08048、2606.08068、2606.08092、2606.08302、2606.08736、2606.08998、2606.09380、2606.09740、2606.09774。它们分别是局部训练/模型/coordination/benchmark/tutorial/AI-for-Science adapter，未证明跨 workload 合同。本轮样本未发现新的 FP/FN；该自检不替代主任务非作者复核。

## Author-side frozen checkpoint（已被独立复核覆盖）

- raw identities：1,235
- Candidate：125 = prior 77 + closure 恢复 48
- Close：1,110 = prior 严格关闭 22 + closure 维持 1,088
- 旧 1,136 closure proposals 的 false-negative：48/1,136（4.2%）
- 旧 99 prior 的 false-positive：22/99（22.2%）

这组 `125 / 1,110` 只保留为作者侧 checkpoint，且含 wrong-owner identity；第一轮独立结果 `115 / 1,120` 也已被第二轮覆盖。旧 exact-v1 仅在 identity/claim 不变时复用。

## Final independent denominator and Books disposition

- raw identities：1,235。
- Candidate：112。
- Close：1,123。
- identity 修正：移除 2606.06529、2606.06545；恢复 2606.09711、2606.09809。
- 相对纠正 identity 后的作者侧集合：第一轮 12 项 de-admit、2 项 restore；第二轮再 de-admit 07909、08300、08702。
- 最终 112 项：112 项已有覆盖，0 项整合，0 项仅报告，0 项正文缺口。
- 2606.09774 的 body/trace adoption chain 已由 root 清理。
