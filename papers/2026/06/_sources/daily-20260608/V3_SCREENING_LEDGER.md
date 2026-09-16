# 2026-06-08 V3 strict screening ledger

> **Authority override（2026-09-11）：** 本文件下方 `50 / 448` 是作者侧 checkpoint。非作者 fresh audit 又关闭 2606.06818、2606.07017、2606.07119、2606.07190、2606.07412，并从 Close 恢复 2606.06915、2606.06991、2606.07054；最终 authority 为 **498 = 48 Candidate + 450 Close**。完整理由见 [`../JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md`](../JUNE_04_05_08_09_FRESH_FINAL_AUDIT.md)。旧 13 个 `Integrate` 重判为 10 项 `已有覆盖` 与 3 项撤回；root 已删除 2606.06818、2606.07067、2606.07470 的采用链，new Integrate = 0，正文缺口 = 0。post-write 终审又纠正 canonical owner：06915→`INFER-SCHEDULING`、06991→`MULTIMODAL-REPRESENTATION`、07054→`PLATFORM-EVALUATION-SYSTEM`、06502→`PLATFORM-SECURITY`、07404→`TRAIN-PRETRAINING`；均有 Review notes 前正文锚点。

## Authority and baseline

本记录按当前 V3 合同重冻题摘分母，不继承 V2.1 的 `Complete`、Candidate disposition 或 Books 决定。可读 canonical packet 有 498 个去重 identity：44 个 old prior 与 454 个 closure proposal。逐项 title、完整 abstract 与旧 family-local reason 分别保存在 `canonical-raw-identity-inventory-v2.1.json.gz` 和 `canonical-semantic-screening-checkpoint-v2.1.json.gz`。

准入只看摘要能否证明可迁移的长期 design delta：改变 state/data/control ownership、execution/evaluation/release contract、系统级机制取舍，或修正 Books 既有结论。论文对象、章节可映射性、局部模型/adapter/benchmark/单一任务性能本身不构成准入。

## Prior frontier reaudit — 34 retain / 10 close

以下 34 项满足严格门槛，但旧 Books disposition 不继承：

| 机制族 | IDs | 严格准入依据 |
| --- | --- | --- |
| 训练、推理与硬件 data plane | 2606.06515、2606.06521、2606.06697、2606.06747、2606.06751、2606.06818、2606.06820、2606.06888、2606.06892、2606.06924、2606.07001、2606.07019、2606.07205、2606.07248、2606.07362、2606.07392 | constraint-aware accelerator DSE、FP8 attention sink、protected CUDA service、compiler property test、stage accounting、heterogeneous scheduling、workflow scheduling、data-constrained scaling、subset attribution、capability-distribution routing、data preparation pipeline、collective synthesis、streaming-attention bound、admission control、vLLM cold-start 与 contextual cascade 均明确改变资源、通信、数据或执行合同。 |
| Agent state/control、workflow 与 security | 2606.06523、2606.06545、2606.06708、2606.06726、2606.06741、2606.06767、2606.06880、2606.06893、2606.07017、2606.07150、2606.07412 | workflow verification、MCP governance、signal observation、access control、open-world skill/verifier bootstrap、artifact custody、bounded interaction space、workflow-to-skill、sim-to-real MDP、communication metadata 与 trace-derived skill lifecycle 均分配了长期状态或控制责任。 |
| evaluation/release contract | 2606.06529、2606.06758、2606.07131、2606.07157、2606.07190、2606.07379、2606.07462 | attack selection、matched evidence、runtime-verified malicious skills、time horizon、prefix utility、coding-agent cheating 与 research lifecycle 直接修正评测/发布口径。 |

以下 10 项严格关闭：2606.06556、2606.06660、2606.06687、2606.06832、2606.06915、2606.06991、2606.07054、2606.07067、2606.07431、2606.07470。前三组主要是 robot/physical-AI 或通用 FL，随后为 image-to-STRIPS、局部 test-time scaling、online video synchrony、cross-step aggregation、自动驾驶 offloading、AI 眼镜和低端设备通用 DNN inference；完整摘要未证明跨 workload 的大模型/Infra 合同。尤其 2606.07067 与 2606.07470 虽被旧报告标为 Integrate，前者只在 AD service 的 RSS/fallback 验证，后者只针对低端设备通用 DNN/TrustZone-M，因此撤回旧采用链。

## Closure proposal reaudit — 16 recover / 438 close

454 项 closure proposal 逐项 title-first，边界不清时读取完整 abstract。严格恢复以下 16 项：

| ID | 严格恢复理由 |
| --- | --- |
| 2606.06502 | 用 canary 与 Neyman-Pearson FPR control 把训练数据 ownership 变成可取证、可验收的合同。 |
| 2606.06560 | 原生虚拟化和跨平台任务使 GUI Agent 的环境差异可复验，并直接修正从 Linux benchmark 外推 macOS competence 的结论。 |
| 2606.06698 | 用 proactive adapt-then-test、constraint-level regression/forgetting 定义生产 constraint 更新后的 release gate。 |
| 2606.06752 | 工业部署中用扫描 backlog、小 PR、review/merge 证据构成低风险连续 Agent 发布循环。 |
| 2606.06787 | 以 actor/memory/critic 分离 semantic/episodic/procedural、短期/长期状态，并定义 merge/prune owner。 |
| 2606.06923 | 在统一 POMDP 中比较 declarative skill 与 imperative state machine，揭示 retrieval quality 对 orchestration 的控制边界。 |
| 2606.06946 | 用 membership inference 审计 LoRA/domain-adapted model 的训练数据暴露，进入 data provenance contract。 |
| 2606.06960 | 将低重复任务、延迟 noisy outcome 与 experience update 对齐，给自演化 Agent 的在线反馈/评测合同及负结果。 |
| 2606.07020 | 把 8.66M evaluation records 分解为 plan、aggregate、instance、culture 与 grounded report，形成可复用诊断流水线。 |
| 2606.07040 | 将 per-query rubric 改成可演化、可复用并直接注入 judge context 的 evaluation skill state。 |
| 2606.07119 | 以生产、federation/control、frontier intelligence 三层分配权限、恢复与非确定性风险；作为 Structural Candidate，不把其部署宣传当效果证明。 |
| 2606.07297 | 在固定 line budget 下把 repository exploration 分成 coverage、ranking、context efficiency，并与 downstream repair 对齐。 |
| 2606.07299 | 解耦 Agent Core/Tool Ecosystem、外层规划/内层搜索，并使中间决策和工具调用显式可审计。 |
| 2606.07316 | 用 typed commit/verdict/abort certificate 明确多 Agent 语义共识，并给出 coverage 无优势与 tie-break 漏洞的负结果。 |
| 2606.07402 | 将多模态 memory 拆成 grounding、cross-session reasoning 与 index/token cost，并按需读取 raw visual source。 |
| 2606.07404 | 120B MoE 单节点训练以 reversible activation、state-preserving growth 与 quantized-expert/adapter optimizer state 形成端到端系统合同。 |

其余 438 项维持 Close。逐项旧记录已保存 title、abstract evidence 与 family-local reason；本轮逐题确认后归入以下实际缺口：非大模型系统或 AI-for-Science/垂直应用；局部模型、quant、adapter、reward、生成/机器人方法；单一 benchmark/data set；或只有风险/taxonomy 而没有长期 owner、控制点与可执行验收协议。

## Fresh-context FP/FN sample

遮蔽旧标签抽查 10 retain：2606.06523、2606.06698、2606.06751、2606.06880、2606.06888、2606.07019、2606.07248、2606.07316、2606.07379、2606.07404。完整摘要均能定位到 state/control、通信、调度、评测或发布合同。

抽查 10 close：2606.06547、2606.06574、2606.06660、2606.06832、2606.06915、2606.07054、2606.07067、2606.07175、2606.07431、2606.07470。它们分别只给 diffusion-LLM PTQ、program-of-layers、physical AI、局部 world model/reasoning/trace、AD offloading、image privacy、wearable/edge DNN，未证明跨 workload 合同。本轮样本未发现新的 FP/FN；该自检不替代主任务非作者复核。

## Author-side frozen checkpoint（已被独立复核覆盖）

- raw identities：498
- Candidate：50 = prior 34 + closure 恢复 16
- Close：448 = prior 严格关闭 10 + closure 维持 438
- 旧 454 closure proposals 的 false-negative：16/454（3.5%）
- 旧 44 prior 的 false-positive：10/44（22.7%）

这组 `50 / 448` 只保留为作者侧 checkpoint。最终独立 authority 是 `48 / 450`；旧 exact-v1 仅在 identity/claim 不变时复用。

## Final independent denominator and Books disposition

- raw identities：498。
- Candidate：48。
- Close：450。
- 相对作者侧 checkpoint：5 项 de-admit，3 项 restore。
- 旧 13 项 Integrate：10 项已有覆盖，3 项撤回，0 项整合，0 项正文缺口。
- 2606.06818、2606.07067、2606.07470 的 body/trace adoption chains 已由 root 清理。
