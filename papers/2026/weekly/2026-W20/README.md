# AI Research Weekly — 2026-W20

> Coverage Window: 2026-05-11～2026-05-17
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 2026-08-14 Source-Family Books Gate Complete; 31/31 final dispositions; 25 Refine, 4 No Change, 2 Weekly Only; 15 Stable Node owners changed or revalidated; Historical Archive/Discovery Gate Open

## Executive Summary

> **Access-history note（superseded 2026-08-13）**：旧段落中的 Qwen-Image-2.0 blocked 叙述保留为
> recovery history；current status 以 Candidate Scoring 与该候选的 Full Source Review 为准：30/30 个
> `20+` families 已审完，0 blocked，0 pending。

旧版 W20 只保留一篇论文和一项政策情景，不能证明全周候选完整。本轮按 first-public date
恢复 18 个 in-window 学术 families，并把推荐流中 9 个更早条目归回 W18/W19。W21 的
curation feed 又暴露 6 个 first-public date 落在 05-12～05-17 的 spillbacks；它们已按 v1 日期
回写 W20，而不是错误留在推荐周。MinT 已完成
30 页 technical report、Appendix 与公开 SDK/runtime/cookbook 联读：它把 LoRA 从训练参数化
提升为可管理的 policy-revision lifecycle，区分训练 checkpoint、固定 adapter revision、policy
record、rollout provenance、catalog addressability、CPU cache、GPU batch 与 readiness。作者证据
支持这些机制在披露 contract 下可执行，也暴露 cold activation 干扰、格式兼容与激进 prewarm
调度的负结果；它不证明百万 adapters 同时 resident，也不证明任意平台可复现相同性能。

MARLIN 仍作为环境多目标调度的 Experimental 分支，Anthropic 条目仍是政策情景而非技术证据。
δ-mem 与 Self-Distilled Agentic Reinforcement Learning（SDAR）也已完成全文、Appendix 与 artifact
边界审计：前者把 fixed-size associative state 作为 frozen full-attention backbone 的动态低秩 attention
correction，后者把 privileged self-teacher 降为有界、detached、token-level auxiliary signal，保留 RL
作为主 objective。两项均是受限模型/任务上的 Experimental 机制证据，不是通用 memory 或 Agent RL
优势。Qwen-Image-2.0 的 46 MB technical report 当前无法通过正文抽取读取，且无 arXiv HTML；官方
repository 只提供产品级 highlights，不能替代全文，故转入 `Unverified / Blocked Backlog`。Long-Context
VLM Beyond 128K 也已完成全文审计：它证明在固定 5B-token budget 下，长文档采样、问题定位与
extraction/reasoning mixture 会显著改变长文档 VQA，而不是只靠位置插值；但 256K/512K 结果来自受控
padding benchmark，不能外推为任意真实超长文档能力。RubricEM 则把 workflow stage、judge rubric
buffer 与 reflection bank 接进同一训练回路；它提供的是有条件的 stage-level credit 与 experience reuse
机制，不是把 LLM judge 变成真值。BetaPRM 进一步把 finite-continuation count 训练成 reward mean 与
learned concentration 两路输出，用于 uncertainty-aware Best-of-N；concentration 只表示对该数据生成过程的
支持强度，不是 correctness guarantee。RTPurbo 则把 dense-attention checkpoint 通过 head calibration、
low-dimensional routing、dynamic top-p 与 self-distillation 转成 sparse runtime 分支；论文支持受限 Qwen/H20
contract 下的可行性，但标题不能掩盖两阶段各约 600 steps，operator speedup 也不是端到端 serving speedup。
WildClawBench 已进一步完成全文、Appendix 与 current artifact boundary 审计：它确认
Agent evaluation 的 subject 必须包含 model、harness、tools、budget、container/environment 与 scorer；
同模型跨 harness 的分差不能归因于模型权重。其 human-judge validation 只有 5 个 sampled tasks，不能把
GPT judge 泛化为可靠真值。
ToolCUA 也已完成全文与公开 artifact 审计：它把 GUI 与 structured tool 视为互补 action branches，并用
synthetic interleaving、critical-switch RFT 和 success-gated path reward 学习选择；它证明“增加工具”会新增
orchestration problem，而不证明 synthetic tools 等价于真实 API，或作者 reward 找到全局最优路径。其余
EVA-Bench 也已完成全文、Appendix、code/data 与章节邻接审计。它把 evaluator-owned user simulator
本身纳入 validation gate，并区分平均成功、至少一次成功与重复可靠成功；但 bot-to-bot、mock tools、
commercial simulator、日志时间戳与 English-only contract 不能替代真实 caller/production evidence。
EvolveMem 随后完成全文、Appendix 与当前 code surface 审计：它把 retrieval configuration 从隐式参数提升为
可版本化、可评估、可回退的 derived policy state；但同一 QA/evaluator 驱动的离线 loop 不能外推为在线
self-modification，且 extraction quality-control ablation 远大于移除 self-evolution 的增益。MemLens 也已完成
63 页 v1、官方 evaluation code、memory-agent adapters 与 dataset card 联读。它真正支持的是把原始多模态证据、
write-time representation、retrieval、answer-time representation 与 scorer 拆开归因；并未实验验证其提出的
hybrid architecture。
MemEye 随后完成唯一 v1、完整 HTML、Appendix、官方 benchmark code 与 dataset surface 联读。它把
visual-evidence granularity 与 memory-reasoning depth 分成正交诊断轴，并暴露“语义相关”不等于“当前状态
有效”；但 stronger task-aware captions 可消除大部分 visual/caption gap，说明长期结论应是保留可回溯的
原始证据并测量 representation loss，而不是把 raw pixels 写成无条件最优。Anti-Self-Distillation 随后也完成
全文、证明、全部 ablations/limitations 与公开 veRL fork 审计。它把 self-teacher/student token log-ratio
解释为 privileged context 的 conditional PMI，并用 sign-reversed、one-sided-bounded JSD shaping 与 entropy
hysteresis gate 改变 token credit。论文支持五个 4B～30B models 上的受限 math evidence，但 `2～10×`
只是 validation score 的 optimizer-step first-reach ratio，未计额外 teacher forward、wall-clock 或 GPU-hours；
linear PMI 的 telescoping 也不能直接外推给 nonlinear AntiSD shape。
Video2GUI 也已完成 30 页 v1、全部 Appendix、project repository 与后续 WildGUI dataset card 审计。
它把互联网 tutorial video 逐级编译为 task、timestamped action、high-resolution grounding 与 state-change
annotations，并以 grounding/action/trajectory 三任务预训练；但当前 GitHub 主要是项目页而非完整 extraction
code，6 月 release 又是 personally reprocessed artifact，94.2M rows 与论文 12.7M task trajectories 不能混算。
π-Bench 也已完成 v1/v3 全文、全部 Appendix、官方代码与 dataset surface、Ch62/61/63/73/75/77
邻接审计。它把“由谁发现需求”的 Proactivity 与“最终是否完成”的 Completeness 拆成两个可审计
outcomes，并以 persistent workspace、跨 session dependency、hidden intent status 与 artifact/tool verifier
实现；但 simulated user 最终会 oracle-like 地补齐所有 intents，Proc 又对 direct completion 与 targeted
clarification 等权，却没有惩罚错误推断、越权行动或不必要介入。因此它支持的是 measurement decomposition，
不是“更主动必然更安全/更好”的部署结论。HarnessAudit 随后完成 v1/v2 全文、全部 implementation
Appendices、官方 repository/dataset 与 Ch62/68/74/77/78/80 邻接审计。它将 harness 明确定义为
`agents + tools + resources + permission policy + information-flow policy + coordination protocol`，并以不可被
Agent 操纵的 hidden audit artifacts、append-only normalized trace、backend/workspace snapshot 同时检查
boundary compliance、execution fidelity 与 perturbation stability。长期缺口是真正的 resource/object scope
与 message-content flow audit，而不是多加一个 final-answer safety judge；但论文内部存在 highest-overall、
tool-count、S@T threshold 三处账目不一致，单 task 仅一次 run，且 violation count 未按机会数或 trajectory
length 归一化，故其排行榜与“长度导致违规”的强度不能外推。W20 current-review queue 已清空；
Qwen-Image-2.0 已于 2026-08-13 恢复完整 technical report 并完成全文审计，不再属于 blocked backlog。

fixed official / Infra source replay 又恢复 11 个 in-window families。Kubernetes PSI GA 把 CPU、memory、I/O
stall 从“利用率旁注”提升为 node / pod / container 的 contention evidence，并明确 unsupported platform 应省略
metric、不能报告误导性的 zero；Workload-Aware Scheduling v1alpha2 则把 static Workload template、runtime
PodGroup、single-snapshot placement、whole-group scoring 与 atomic scheduling 串成 group-level state machine。
Mixed Version Proxy 处理 HA control plane 升级期间的 false 404；Service `externalIPs` deprecation 展示 insecure
default 如何经 admission guard、迁移窗口再进入移除；CCM route-sync counter 只证明 reconciliation attempt，不能
替代 success、latency 与 correctness。

OpenAI 的 TanStack incident 把 upstream package compromise、developer endpoint、repository credential、signing
certificate 与 forced client upgrade 串成同一 supply-chain failure path；其公开材料没有完整取证报告，因此只按
官方 incident boundary 使用。跨对话 safety summary 则提供“目的限定 derived state”的工程实例：只为严重安全
场景生成窄范围事实摘要，并明确不等于一般 personalization / long-term memory；内部 evaluation 数字只对作者设计
的 scenario contract 成立。NVIDIA Fleet Intelligence 联读 GA blog 与公开 host agent，确认 telemetry、health
check 与 attestation 是不同 evidence planes；产品效果与 predictive failure 尚未被独立验证。Vera Rubin
agentic-inference 条目则把 throughput-oriented 与 low-jitter branches 作为异构执行设计，但不独立验证厂商
performance/economic claims。TensorRT serving
pipeline best-practice 文章和 Transformers v5.8.1 patch release 只作为已有 lifecycle / compatibility 观点与版本事实，
不被提升为新通用机制。

## Coverage and Source Coverage

- 模型与研究机构：Anthropic 5 月 14 日条目仅作政策情景记录；Qwen-Image-2.0 以 technical
  report 进入学术候选，不能把 human preference 结果外推为通用多模态质量。OpenAI 5 月 13～14 日
  两项官方材料已完成 incident / engineering boundary review；其官方叙述不替代独立取证或外部 validation。
- 论文与学术来源：已重放 Hugging Face W20（其页面覆盖 05-10～05-16）并逐项核对 arXiv v1，
  恢复 18 个 in-window families；MinT 已完成正文、evaluation、Appendix 与 artifact review，另外
  δ-mem、SDAR、Long-Context VLM Beyond 128K、RubricEM、BetaPRM、RTPurbo、WildClawBench、ToolCUA 与
  EVA-Bench、EvolveMem、MemLens、MemEye、Anti-Self-Distillation、Video2GUI、π-Bench、HarnessAudit 与
  Qwen-Image-2.0 已完成全文审计，current-review queue 无 pending。RouteProfile 回拨 W18，另外 8 项回拨 W19；
  W21 feed 中 6 项回拨 W20。
  OpenReview/TMLR、DBLP、Scholar/OpenAlex 交叉召回仍 pending。
- AI Infra：已重放 Kubernetes、NVIDIA 与 Transformers 的 in-window 官方 Blog、文档、release 和公开
  artifact，新增 PSI GA、Workload-Aware Scheduling v1alpha2、Service `externalIPs` deprecation、Mixed
  Version Proxy Beta、CCM route-sync metric、Fleet Intelligence、Vera Rubin agentic-inference scale-up contract、
  serving pipeline contract 与 Transformers v5.8.1。vLLM、SGLang、TensorRT-LLM、Ray、KServe 的 stable-release surface 未发现新的 in-window
  retained family；这不是对所有 PR 的 exhaustive absence proof。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| MARLIN sustainable LLM inference | 3 | 4 | 3 | 3 | 4 | 4 | 21/30 | Worth Watching |
| Global AI leadership scenarios | 2 | 2 | 2 | 4 | 2 | 3 | 15/30 | Record Only |
| MinT: Managed Infrastructure for Training and Serving Millions of LLMs | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Must Read — full review complete |
| δ-mem | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch22 / Experimental |
| Self-Distilled Agentic Reinforcement Learning | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch29 / Experimental |
| Qwen-Image-2.0 Technical Report | 4 | 4 | 4 | 5 | 4 | 3 | 24/30 | Full Source Review complete — provisional Refine Ch17 / Ch23 handoff / Experimental |
| Training Long-Context Vision-Language Models Beyond 128K | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch23 / Experimental |
| RubricEM | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch29 / Experimental |
| EVA-Bench | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch62 / Experimental |
| MemEye | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch62 / Experimental |
| WildClawBench | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full review complete — No Change / Ch62 |
| ToolCUA | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch74 / Experimental |
| EvolveMem | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch73 / Experimental |
| MemLens | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch62 / Experimental |
| Anti-Self-Distillation for Reasoning RL | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch29 / Experimental |
| Video2GUI | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch23 / Experimental |
| π-Bench | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch62 / Experimental |
| Full Attention Strikes Back | 5 | 5 | 4 | 4 | 4 | 3 | 25/30 | Full review complete — provisional Refine Ch22 / Experimental |
| Auditing Agent Harness Safety | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — provisional Refine Ch62 / Experimental |
| Process Rewards with Learned Reliability | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch62 / Experimental |
| Kubernetes PSI Metrics GA | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch63 |
| Kubernetes Workload-Aware Scheduling v1alpha2 | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full review complete — provisional Refine Ch60 / Experimental |
| Kubernetes Service `externalIPs` deprecation | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full review complete — provisional Refine Ch68 |
| Kubernetes Mixed Version Proxy Beta | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full review complete — provisional Refine Ch53 |
| Kubernetes CCM route-sync metric | 3 | 4 | 4 | 5 | 4 | 2 | 22/30 | Full review complete — No Change / Ch63 |
| OpenAI TanStack supply-chain incident response | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch68 |
| OpenAI cross-conversation safety summaries | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch68 / Ch73 handoff |
| NVIDIA Fleet Intelligence GA | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full review complete — provisional Refine Ch63 / Ch68 handoff |
| NVIDIA Vera Rubin agentic-inference scale-up contract | 4 | 5 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch50 / Official Engineering Evidence |
| NVIDIA model-serving pipeline contract | 2 | 4 | 5 | 4 | 4 | 3 | 22/30 | Full review complete — No Change / Ch45/55 |
| Transformers v5.8.1 | 2 | 4 | 4 | 5 | 3 | 2 | 20/30 | Full review complete — Weekly Only / Version Fact |

本轮账目为 31 行：22 个 `25～30`、8 个 `20～24`、1 个 `<20`。评分只决定阅读优先级，
不等于 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows | 2 | 1 项 `20+` review；1 项低分政策记录 |
| Recovered in-window families | 29 | 18 个学术 families 与 11 个 fixed official / Infra families 已完成 Full Source Review；无 blocked / current-review pending |
| Recorded `20+` candidates | 30 | 22 high / 8 mid；六维合计已复算 |
| Earlier-week spillbacks | 9 | RouteProfile→W18；另外 8 项→W19 |
| Academic discovery window | Open | HF first pass complete；formal/cross indexes pending |
| Official / Infra discovery window | Fixed-source checkpoint passed | Kubernetes / NVIDIA / Transformers in-window official surfaces replayed；cross-index 与 exhaustive PR absence proof 仍开放 |
| W20 Candidate Evidence Gate | Passed | 30/30 `20+` reviews complete；无 blocked / current-review pending；cross-index replay 尚未闭合 broader Historical Gate |

## Evidence Level

MinT 的系统结论由作者 technical report 与公开 artifact 支持，性能数字只对指定 Qwen/Kimi/GLM
路径、adapter rank/layout、A800/H800 或 4-GPU Qwen3-30B TP=4 serving、prompt 1024、最大输出
64、Poisson offered load 与 TTFT SLO 成立。百万级是 durable catalog addressability，不是并发
residency。MARLIN 的结论绑定作者模型、datacenter assumptions 与 reward design；环境指标需要
可审计的 power、water 与 regional carbon data。其余 accessible `20+` 恢复项均已完成正文或官方
文档 / release / artifact 联读；Qwen-Image-2.0 正文已恢复，按受限 Experimental evidence 记录。

## Cross-Week Deduplication

W20 推荐流覆盖 5 月 10～16 日，不能直接当 ISO week：RouteProfile v1 为 4 月 30 日，已归 W18；
MemPrivacy、Soohak、LLMs Improving LLMs、HyperEyes、MCP-Cosmos、Geometry Conflict、STALE 与
UniPrefill 的 v1 为 5 月 7～10 日，已归 W19。MinT 与 W09 LoRA lifecycle、W19 UniPrefill 和后续
multi-adapter serving 是 `Layering / Dependency`；MARLIN 与 Ch66 Cost 是 `Layering`，财务 cost、
energy、carbon 和 water 可共享 telemetry，但不是同一个可互换目标。

W21 feed 的推荐日不能替代 first-public date：Anti-Self-Distillation（2605.11609，05-12）、
Video2GUI（2605.14747，05-15）、π-Bench（2605.14678，05-15）、Full Attention Strikes Back
（2605.16928，05-17）、Auditing Agent Harness Safety（2605.14271，05-14）与 Process Rewards
with Learned Reliability（2605.15529，05-15）均归 W20，且现均已完成全文、Appendix 与可用 artifact
边界审计。Kubernetes Volume Group Snapshots GA（05-08）、Transformers v5.8.0（05-05）与 vLLM
v0.20.2（05-10）属于 W19 spillback backlog，不因 W20 fixed-source replay 改写 event week。

## Deep Analysis — Adapter 从参数文件演化为可调度 Policy Revision

LoRA 最初解决的是 trainable state 与每任务权重副本过大；merge 后部署路径简单，所以在变体少、
发布频率低时仍合理。约束变成“少量昂贵 resident bases 上持续产生大量 policy variants”后，
每次 merge、复制完整 checkpoint 和启动独立 server 会把参数效率重新浪费在 lifecycle 中。MinT
改变的不是 LoRA 数学，而是 managed unit：

```text
low-rank training parameters
→ standalone adapter artifact
→ immutable exported adapter revision
→ durable policy record and rollout lineage
→ catalog-addressable policy population
→ bounded CPU/GPU serving working sets
```

训练 worker 仍拥有可变 adapter、optimizer、scheduler、gradient 与未消费 rollout state；export
把某一步冻结为 serving layout，并绑定 base、rank、target modules 与 sparse-route/correction metadata。
Service plane 只有在 files 与 metadata 一起提交后才让 revision 可见；sampler 按 catalog→CPU cache
→GPU batch 晋升。这样 rollback/evaluation 可以指向固定 behavior，而 worker placement、cache 与
training head 可独立变化。

收益不是免费的。Catalog 可命名百万 revisions，不代表一台 engine 同时 resident；cold miss 还要
fetch、materialize objects、register、activate 和 queue。两阶段 readiness 通过延迟 exposure 保护旧
warm tenants，并没有消除 prewarm 时间。Packing 减少 tensor-object fanout，却形成非标准 PEFT
layout；Appendix 中 native vLLM 直接加载失败是 compatibility boundary。更激进 activation scheduler
缩短 rollout，却伤害 warm-tail，说明下一阶段压力仍是 admission、locality、format portability、
retention/GC、tenant isolation 与跨 revision evidence lineage。

## Knowledge Tree Position

Ch26 LoRA → Ch31 Checkpoint → Ch46 vLLM → Ch52 Scheduling → Ch53 AI Platform →
Ch55 Model Registry → Ch63 Monitoring → Ch66 Cost。MinT 的长期 owner 暂定 Ch55，Ch26/31/46/52
只保留短 handoff。

## Recommended Action

W20 的 Source-Family Books Gate 已完成；后续只闭合交叉学术索引。长期机制已经由 owner 章节接管：
MinT 的 adapter policy lifecycle 归 Model Registry；PSI/Fleet evidence 分层归 Monitoring；workload snapshot
归 GPU Scheduler；TanStack incident 与 purpose-limited safety state 分别归 Security 与 Memory。MARLIN 在缺少
真实 trace、multi-region energy data 与 SLO guardrail 前保持 No Change；版本和政策情景继续只留 Weekly。

## Event-Date Daily Decision

2026-05-11～05-14：Historical Weekly only；不补造 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete`。31/31 final dispositions：25 `Refine — Existing Argument`、
4 `No Change — Already Covered`、2 `Weekly Only`。15 个 Stable Node owners 完成修改或具体论点级复核；
Qwen-Image-2.0 的独立 Gate 已并入本周总账。所有 Experimental 论文继续绑定作者 workload、artifact 与
未披露条件；HarnessAudit 的内部账目冲突、AntiSD 的 optimizer-step ratio 和厂商 performance/economic claims
均未进入通用结论。详细 owner 与 evidence boundary 见文末 ledger。

## Ignored Noise

把 million-scale catalog 写成百万 adapters 同时 resident；把 packed loader slice 的 8.5～8.7 倍
写成 end-to-end serving speedup；把 simulated carbon/water reduction 外推为所有区域和硬件的
生产收益；把候选论文摘要当作全文结论。

## Full Source Review

### MinT: Managed Infrastructure for Training and Serving Millions of LLMs — 29/30

- **Candidate / Week / Source Family**：`MINT-MANAGED-LORA-POLICY-LIFECYCLE`；W20；
  arXiv:2605.13779 v1，2026-05-13；v2 为 2026-05-26。v2 用于 revision/机制核验，不作为 W20
  新事件，也不把 5 月 26 日补充实验倒写成 5 月 13 日已公开事实。
- **Direct / Related Primary Sources**：arXiv metadata 与 30 页 v2 PDF；作者 `mindlab-toolkit` SDK、
  `verl-mint` open runtime、`mint-cookbook`。代码仓库按访问日核对，不能证明 v1 时所有当前路径
  已存在，也不能替代论文 evaluation。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、adapter revision/policy record 模型、
  service/control/compute planes、time-sliced training、distributed export、shared-base serving、Scale
  Up/Down/Out、全部 evaluation tables/figures、Related Work、Conclusion，以及 Appendix 的硬件配置、
  catalog audit、open-loop sweep、hot reload、native-vLLM caveat、negative scheduler probe、memory/
  tensor accounting 和 stress ladders；并检查 SDK/runtime/cookbook 的公开职责与支持边界。
- **Original Problem / Why Previous Design Was Reasonable**：full fine-tuning 或 LoRA merge 把每个
  behavior 变成完整 checkpoint，部署简单、runtime compatibility 好，在 policy variants 少且发布慢
  时合理。LoRA adapter-only serving 又常只优化 inference hot path，没有连接 optimizer state、rollout、
  evaluation、export、rollback 与 catalog。面对少量昂贵 base deployments 上持续产生大量 tenant、
  task、experiment 与 rollback variants，复制 base 或把“adapter file”当完整 lifecycle unit 不再扩展。
- **Changed Constraint / Principle**：可训练状态、可执行 behavior、持久身份和局部 residency 的变化
  时间尺度不同，必须拆开。`adapter revision` 是某训练步冻结、转换为 serving layout 的 behavior
  payload；`policy record` 是服务拥有的 lifecycle state；base deployment、training checkpoint、rollout
  record、exported revision、catalog、CPU cache、GPU batch 和 readiness 不是一个状态字段。
- **Mechanism**：Tinker-compatible service 把 sample、gradient/update、export、evaluate、serve 与
  rollback 编成 pollable operations。Trainer 在 resident base 上 time-slice policies，每个 policy 单写
  adapter/optimizer/gradient/rollout state；distributed export gather TP slices、按 EP owner 收集 expert
  adapters、去重 replicated/shared tensors并生成 PEFT revision。Sampler 在 resident vLLM base 上按
  policy name 解析 fixed revision，经 durable catalog、per-actor CPU cache、GPU batch slot 三层执行；
  cold loads 是带 dedup/backpressure 的 scheduled work，新 revision 经过 register→prewarm→ready 后
  才对用户可见。
- **State Ownership / Control Flow / Data Flow**：service plane 持有 operation visibility、policy record、
  revision selection、compatibility/admission 与 readiness；trainer 独占可变 adapter、optimizer、scheduler、
  gradient 和未消费 rollout state；durable storage 持有 committed checkpoints、rollout records 与 exported
  revisions；sampler actor 持有局部 CPU cache、GPU slots 和 in-flight generation；human/platform policy
  owner 持有 promotion、retention、tenant access 与 SLO。流向为 `rollout(revision r) → provenance record
  → update mutable training state → export immutable r+1 → evaluate → prewarm/readiness → serve/rollback`。
- **Implementation Details**：worker 公开 base、rank/target-module shape 与 parallel-layout capacity；
  checkpoint/export 只有 metadata commit 后可见，crash 留下的未引用 attempt files 不可被选中。
  Qwen MoE 路径记录 expert ids并在 training backend 可映射时 replay，不可映射 token 被 mask；DSA
  路径未保存全部 indexer selections，使用 trusted-band rollout correction，而非声称精确 replay。
  MoE packing 将大量小 expert tensors 变为紧凑 serving representation；这降低 object/registration
  fanout，却造成 packed layout 与 native PEFT consumer 的 compatibility boundary。
- **Evaluation Contract**：Scale Down 比较 Qwen3-4B rank-32 和 Qwen3-30B rank-16 adapter handoff
  与 merged full checkpoint，并在相同 resident-base allocation 下比较三条 GRPO policy 的 sequential/
  concurrent wall time；30B/235B/Kimi K2 1.04T 与 GLM-5.1 案例分别使用披露的 A800/H800 数量、
  TP/EP 与 task-specific traces。Scale Out 的主 serving contract 是 Qwen3-30B rank-1、单个 4-GPU
  TP=4 actor、prompt 1024、max output 64：built/audited 1M packed catalog，局部 CPU cache 数百项、
  tested same-batch 64 adapters，64 warmed revisions 的 Poisson open-loop TTFT≤5s sweep、cold staircase、
  hot reload、two-phase readiness 与 packing probes。作者百分比只能在这些条件下解释。
- **Baselines / Ablations / Sensitivity / Overhead**：handoff 同 merge path 比较并区分 cold-first 与 warm
  generation；training 比较相同 peak-memory 的 sequential/concurrent schedule；serving 分开 repeated
  hotset/unique traffic、warm/cold、1k～100k legacy sweep 与 1M artifact audit。Appendix 的 native vLLM
  standard-PEFT 1k rows不是 1M packed 的 apples-to-apples baseline；直接加载 packed directory 启动失败。
  激进 adaptive activation 虽缩短 prewarm，却把 warm TTFT p95 推高并产生 stalls，作者把它作为负结果。
- **What the Evidence Proves**：公开系统与测量证明 adapter-only handoff、resident-base policy switching、
  revision attribution、distributed export、bounded cache tiers、cold-load admission 和 readiness boundary
  可以组成一条可执行 lifecycle；catalog addressability、engine-local residency 和 same-batch diversity
  必须分别计量。它也证明 byte size 小不代表 cold-load 便宜，object fanout 与 activation interference
  可成为主瓶颈。
- **What It Does Not Prove / Threats to Validity**：1M 是 materialized catalog 和 sampled audit，不是百万
  simultaneous residents、active tenants 或 production requests；单 actor/Qwen workload 不证明跨硬件、
  engine、rank、模型与 tenant distribution 的通用容量。学习质量案例不建立 LoRA 相对 full fine-tuning
  的普遍等价性。当前公开 repo 状态晚于事件，商业 service 的 fleet failure、security、multi-region
  consistency、GC/retention 与 control-plane HA 也未得到完整实验。
- **Trade-offs / New Failure Modes**：共享 base 减少复制和 handoff，却引入 base/adapter compatibility、
  revision-selection skew、route/probability provenance、stale rollout、single-writer session、cache thrash、
  cold activation interference、prewarm backlog、packed-format lock-in、tenant mix-up、catalog GC 与 rollback
  retention。两阶段 readiness 把用户等待移动到发布前；packing 用 portability 换加载效率；time slicing
  用切换/restore IO 换 resident-base 利用率。
- **Where Previous Design Still Applies / Evolution**：policy 数少、静态发布、runtime 不支持 dynamic
  adapters 或需要最小兼容风险时，merge/full checkpoint 与独立 endpoint 仍合理。演进关系是
  `Direct Evolution`：LoRA parameter efficiency→adapter artifact→managed policy revision；相对 Registry、
  vLLM 与 scheduler 是 `Layering / Dependency`，不是用 MinT 替代这些 owner。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch26、Ch31、Ch46、Ch52、Ch53、Ch55，并核对
  相邻 artifact/runtime 责任。Ch26 已覆盖 merge/dynamic adapter 与 compatibility；Ch31 覆盖 resumable
  checkpoint/deployment artifact；Ch46 覆盖 adapter cache/batch；Ch55 覆盖 immutable identity、lineage、
  promotion/rollback。主 owner 暂定 Ch55；稳定缺口是 policy record 与 adapter revision 的分离、rollout
  provenance、addressability/residency/readiness 多时间尺度，不需要新增章节。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`；Historical
  Books Gate 关闭，当前只更新 W20。待验证：谁拥有 revision retirement 与 cache invalidation；多 region
  readiness/rollback 的一致性；packed layout 如何保持标准 consumer portability；sparse route provenance
  不完整时 evaluation/promotion 应如何降级。

### MARLIN sustainable LLM inference — 21/30

- **Source Family ID / Type / Date**：`MARLIN-SUSTAINABLE-SCHEDULING`；arXiv:2605.13496v1，
  first-public 2026-05-13。
- **Full-read Coverage**：已覆盖 workload/datacenter/energy/water/carbon models、多目标 formulation、
  predictor、multi-agent RL、competitive proposal/veto、complexity、baseline/ablation/scalability 和
  conclusion；论文未设独立 limitations 章节，model assumptions 作为 threats 记录。
- **Problem / Previous Design / Changed Constraint**：latency/cost scheduler 对单区域稳定供能合理；
  geo-distributed workload 与时变 grid/carbon/water 使环境 externality 进入 placement objective。
- **Mechanism / Ownership / Flow**：predictor 估计需求；每个 metric agent 以 RL 提 proposal；
  game-theoretic blending、capital 和 veto 协调 TTFT、carbon、water、energy cost；scheduler 输出
  datacenter/node/GPU/P-state allocation。policy owner 必须定义 guardrail，telemetry 提供 region/time
  signals，agent reward 不能成为隐式业务政策。
- **Evaluation Contract**：simulation 使用 A100/H100、每 node 2/4/8 GPU、固定 cooling/energy/water
  equations和 trace；比较多种 RL/optimization baseline 并有 ablation/scaling。作者百分比只证明
  其模拟参数与 reward 下 Pareto 改善，不证明真实 facility water、carbon accounting 或 production SLO。
- **Trade-offs / Failure Modes / Coexistence**：多目标提高 policy 表达力，却引入 stale forecast、
  metric gaming、regional data quality、veto instability 和 migration/queue overhead；硬 SLO 或数据
  不可信时，约束优化/简单 scheduler 仍合理。关系为 `Layering / Dependency`。
- **ROADMAP / Chapters / Decision**：Ch66 主 owner，已读 Ch52、Ch59、Ch63、Ch65～67；现有
  cost vector 与 telemetry contract 已覆盖长期原则。`No Change — Already Covered`。

### Global AI leadership scenarios — 15/30

- **Source / Date / Verification**：Anthropic 2026-05-14 官方 scenario material 已核对；是政策情景，
  不是模型、训练或 runtime primary technical evidence。
- **Score / Decision / Rejection**：15/30 维持；`Weekly Only — Version/Product Fact`，不升级。

### δ-mem: Efficient Online Memory for Large Language Models — 27/30

- **Candidate / Week / Source Family**：`DELTA-MEM-ONLINE-ASSOCIATIVE-STATE`；W20；arXiv:2605.12357
  v1，2026-05-12。当前只有 v1；没有把后续二手解读当成 primary evidence。
- **Direct Sources / Full-read Coverage**：已读 15 页 PDF 的 Abstract、Introduction、Preliminaries、完整
  Method/公式、TSW/SSW/MSW write variants、training objective、全部 experiments/ablations、Related Work、
  Conclusion，以及 Appendix 的 training/evaluation contract、inference efficiency 和 parameter overhead。
  未发现可独立核验的作者 code artifact，因此实现结论只限论文披露。
- **Original Problem / Why Previous Design Was Reasonable**：full Attention/KV 保留逐 token 可寻址历史，
  RAG/textual memory 保留来源与可删除证据，static adapter/model edit 则以较少参数持久改变 behavior；在短
  Context、可预先检索或 memory 更新频率低时都合理。长交互里，显式历史持续增加 token/KV 成本，text
  compression/retrieval 会丢信息或 miss，static parameters 又不能随当前 stream 快速变化，约束转向“固定
  容量、在线写入、直接影响 forward，但不重训 backbone”。
- **Mechanism**：每个选定 Transformer layer 从 frozen hidden state 投影 memory query/key/value，在读取时用
  `r_t = S_(t-1) q_t^m`，再经两个 trainable mappings 生成 query-side 与 output-side low-rank correction；
  attention 完成后以 dimension-wise forget gate 与 delta rule 更新 `r×r` state：旧 state 先按 `lambda_t`
  保留，再用 prediction residual `(v_t - S_(t-1) k_t) k_t^T` 写入。TSW 每 token 写，SSW 对 message hidden
  states 求均值后每 segment 写，MSW 维护多个并行 state 后拼接 readout。correction parameters 训练后固定，
  但 correction 内容随 runtime state 变化，因此不是普通 static LoRA。
- **State Ownership / Control and Data Flow**：frozen backbone 拥有 base attention/KV semantics；δ-mem module
  拥有 projection、gate 与 correction parameters；每个 active stream/session 必须独占 online state；runtime
  拥有 state allocate/reset/chunk/migrate/free；外部 evidence store 仍拥有 provenance、authorization 与删除。
  数据流是 `context hidden states → sequential/segment writes → fixed-size latent state → next-token read → dynamic
  query/output correction → state update`。论文训练时先把 context 写入 state，prediction 只给 backbone query+
  response，迫使 memory path 成为 load-bearing，而不是让显式 context 旁路它。
- **Evaluation Contract**：Qwen3-4B-Instruct、Qwen3-8B、SmolLM3-3B；QASPER 最短 2,219-sample split 训练
  一 epoch，原样本最长 8,269 tokens，backbone training length 512、memory write budget 8,192。默认 rank
  `r=8`、scale 16、query/output branches，MSW 四 states；8×A800、bf16、ZeRO-2、fused AdamW、per-device
  batch 1、gradient accumulation 4、global batch 32、seed 42。评测 IFEval、HotpotQA、GPQA-D、LoCoMo
  （排除 adversarial category）与 MemoryAgentBench；对同一 Qwen3-4B backbone 比 BM25 RAG、LLMLingua-2、
  MemoryBank、Context2LoRA、MemGen、MLP Memory。
- **What Evidence Proves**：在该训练/evaluation contract 下，TSW 的 aggregate score 51.66 对 frozen
  backbone 46.79、Context2LoRA 44.90；三种 write variants 在三种 backbone 上总体提高。no-context ablation
  中 state 能恢复部分被移除历史，但绝对值仍低（例如 HotpotQA EM 0.08→6.48、F1 8.27→15.20），证明的是
  有损 latent influence，不是精确历史复原。query+output correction 接近更昂贵 qkvo 的平均结果；论文因此
  选择较小参数分支。TSW/SSW/MSW 的不同胜负也支持 write granularity 与 interference 是独立设计轴。
- **What It Does Not Prove / Threats to Validity**：单 seed、单一短训练 split、三个相近规模 backbone 与作者
  aggregate metric 不能证明跨模型/任务稳定；没有 ablate state rank、forget gate、write budget、session
  reset、跨 chunk equivalence、poisoning、tenant isolation、精确 deletion 或真实多会话 serving。论文没有独立
  limitations 章节，也未给出可审计 code。固定 8×8 state 不等于 8×8 数值足以恢复任意历史；aggregate gain
  混合 general 与 memory-heavy metrics，不能外推成 1.10× 的通用质量倍率。
- **Efficiency / Trade-offs / Failure Modes**：4.87M trainable parameters（0.12%）与 state memory 很小，
  但每个 decode step 都读写 state，作者图表明确显示它慢于 Vanilla/Context2LoRA；公开图未给出可移植的
  concurrency/P95/SLO。TSW 保留细节却写入格式/重复噪声，SSW 降噪却平均掉细节，MSW 降干扰却增参数与
  state ownership。压缩状态会发生 overwrite、不可解释 retention、错误 reset/tenant reuse、checkpoint/
  migration mismatch 和无法逐条删除；需要 exact recall/provenance 时，KV/RAG/外部 archive 仍成立。
- **Evolution / ROADMAP / Decision**：`full token history → external retrieval/compression → static parametric
  memory → online fixed-size associative state → state-conditioned low-rank attention correction` 是
  `Layering / Dependency`，不是单向替代。主 owner Ch22，Ch17/41/73 作 handoff；已读 Ch21～23、Ch17、
  Ch73，并核对模型内部 state 与 Agent durable memory 的边界。Ch22 已覆盖 test-time neural memory 与
  recurrent continuity，但缺少“prediction-residual write + write granularity + dynamic low-rank correction”这一
  中间分支。provisional `Refine — Existing Argument` / Ch22，`Status: Experimental`；Historical Books Gate
  关闭期间不改 Books。
- **Open Questions**：state rank/capacity 的 scaling law；stream reset、Prefill chunking 与 migration 是否严格
  等价；如何防 poisoning/cross-tenant reuse；如何把 latent deletion 与外部 evidence deletion 对齐；多 seed、
  长度外推与 production TPOT/TTFT contract 是否成立。

### Self-Distilled Agentic Reinforcement Learning — 26/30

- **Candidate / Week / Source Family**：`SDAR-PRIVILEGED-SELF-TEACHER-GATING`；W20；arXiv:2605.15155
  v1，2026-05-14。官方代码于 2026-05-15 公布；2026-06-22 修复 ALFWorld teacher skill retrieval bug，
  因此当前 repository 只能核验实现表面，不能倒写成 W20 实验已使用修复后路径。
- **Direct Sources / Full-read Coverage**：已读 arXiv HTML 的 Introduction、两项 motivating observations、
  full Method/公式、全部 experiments、training dynamics、robustness、ablation、Related Work、Conclusion、
  Appendix A theoretical properties、B algorithms/baselines、C hyperparameters、D diagnostics 与 E prompt；并
  核对官方 ZJU-REAL/SDAR repository 的 environment/runtime surface、release timeline 与 bug note。
- **Original Problem / Why Previous Design Was Reasonable**：GRPO 用 trajectory outcome 提供可验证、低标注
  成本的 sequence-level advantage，适合长动作链但把同一 credit 粗略广播到所有 tokens；on-policy
  self-distillation（OPSD）在 student 自己采样的 token 上用 privileged context teacher 提供 dense signal，
  在短/可靠 teacher 场景合理。进入 multi-turn Agent 后，skill retrieval 会错，teacher 也可能对 student 已选
  token 更不确信；若把所有 divergence 等权加入，负 teacher gap 与跨 turn drift 会压过环境 reward。
- **Changed Constraint / Mechanism**：RL 仍是主 objective；同一 policy 在 student context
  `s_t=(x,y_<t)` 与增加 retrieved skill 的 teacher context `s_t+=(x,c+,y_<t)` 上前向。对 student-sampled token
  计算 detached log-prob gap `Delta_t=log pi_T(y_t|s_t+) - log pi_theta(y_t|s_t)`，以
  `g_t=sigmoid(beta Delta_t)` 生成 `(0,1)` gate，再把 `g_t` 加权的 reverse-KL-aligned likelihood term 作为
  `lambda` auxiliary loss 加到 GRPO。positive gap 获得更大权重，negative rejection 只软衰减；gate stop-gradient
  防止 discrepancy 反向制造 self-referential gradient path。
- **State Ownership / Control and Data Flow**：environment/verifier 拥有 trajectory reward；rollout policy
  产生 group trajectories；skill retriever/library 提供 privileged context，但不拥有 truth；同一 current policy
  的 teacher branch只计算条件 log-probs，不独立生成 authoritative action；gate/controller 拥有 token auxiliary
  strength；optimizer 在 GRPO advantage 与 gated distillation 两条信号汇合后更新 policy。训练流为
  `on-policy rollout → environment sequence reward/group advantage → privileged-context teacher forward on same
  tokens → detached per-token gap/gate → joint update`；推理时不需要 skill input。
- **Evaluation Contract**：Qwen2.5-Instruct 3B/7B 与 Qwen3-Instruct 1.7B，150 steps、8×H800。
  ALFWorld 使用 GiGPO split、batch 16 tasks×8 rollouts、max prompt 2,048；Search-QA 以 NQ/HotpotQA
  training、E5 retriever、batch 128、max prompt 4,096，其余 QA datasets 作为 OOD；WebShop 使用 1,000
  training tasks、固定 128 validation tasks、batch 16×8、max prompt 4,096。所有环境使用 SkillRL
  SkillBank；默认 learning rate 1e-6、group 8、clip 0.2、KL 0.01、`lambda=0.01`、`beta=5`。比较
  Skill-Prompt、GRPO、OPSD、Skill-GRPO、GRPO+OPSD、Skill-SD、RLSD。
- **What Evidence Proves**：在三模型/三环境 contract 下，SDAR 相对 GRPO 在若干主指标提高，naive OPSD
  或 GRPO+OPSD 在部分配置发生严重 collapse，而 bounded gate 的 training curves 更稳定。random/full/KM/UCB
  retrieval 均在作者选定配置上超过 pure GRPO，说明机制不只依赖最佳 retriever；gap gate 优于 entropy/
  soft-OR，`beta=5` 优于 uniform/过硬 gate，`lambda=0.01` 优于过小/过大，reverse KL 优于 forward KL/JSD。
  这支持“辅助 teacher 必须有界且按局部可信度路由”，不证明 teacher gap 是 token 因果 credit。
- **What It Does Not Prove / Threats to Validity**：论文没有独立 limitations 章节；只训练 150 steps，未披露
  多 seed/error bars、完整 output length/token throughput、teacher forward/skill retrieval 的额外 FLOPs、生产
  concurrency 或 wall-clock。NQ/HotpotQA 属 in-domain，WebShop 仅 128 fixed validation tasks；同一模型
  self-teacher 与 student errors 强相关。2026-06-22 的 retrieval bug 修复使原始实验 artifact 与当前 code
  存在 revision boundary。`g_t>0.5` 只等价于 positive log-prob gap，不证明该 token 对 outcome 有因果帮助；
  “internalized skills”来自不带 skill 的 task performance，不是可解释知识迁移证明。
- **Theory / Trade-offs / Failure Modes**：sigmoid 与 stop-gradient 能界定 auxiliary gradient，并消除一种
  self-referential coupling；理论不保证联合 RL objective 的收敛、teacher 正确或环境 generalization。
  获得 dense token signal的代价是每条 sampled trajectory 再做 privileged teacher forward、维护 skill/retrieval
  identity，并增加 `lambda/beta/gate` 控制面。错误 skill 可被软衰减但不会归零；teacher/student 同源 bias、
  reward-gate conflict、length-dependent aggregation、retrieval drift 与过强 auxiliary coefficient 仍会造成
  policy collapse。reward 足够 dense/可靠、teacher 无可靠优势或额外 forward 太贵时，plain GRPO 仍合理；
  deterministic step verifier 可用时，process reward 仍提供更直接 evidence。
- **Evolution / ROADMAP / Decision**：`trajectory reward broadcast → process/step reward → privileged on-policy
  distillation → RL + uniform auxiliary distillation → bounded detached token routing of teacher signal` 是
  `Direct Evolution`，不是用 self-distillation 替代 RL。主 owner Ch29，Ch28/30 与 Ch74～77 作 handoff；已读
  Ch28～30、Ch74～77。Ch29 已指出 sequence reward 的粗 token credit、process verifier 成本和 distillation
  分支，但尚未明确 privileged teacher 是可错的 auxiliary evidence、其权重必须与 RL 主信号分离治理。
  provisional `Refine — Existing Argument` / Ch29，`Status: Experimental`；Historical Books Gate 关闭期间不改 Books。
- **Open Questions**：多 seed 与更长 horizon 是否稳定；teacher-forward cost 如何改变 sample efficiency；bugfix
  前后结果能否复现；gate 与 outcome/step verifier 的因果一致性如何验证；如何监控 teacher negative-gap、
  gate activation、RL/aux gradient norm 与 retrieval revision drift。

### Qwen-Image-2.0 Technical Report — 24/30 — Full Source Review Complete

- **Source Family / Dates**：`QWEN-IMAGE-2-UNIFIED-GENERATION-EDITING`。Qwen 官方 repository 记录
  2026-02-10 product launch；arXiv:2605.10730 v1 first-public 2026-05-11 是独立 technical-report node，
  归 W20，但不得把 2 月产品事实和 5 月论文证据合并成同一发布日期。
- **Access / Full-read Coverage**：2026-08-13 恢复 arXiv HTML，已覆盖 metadata、Introduction、architecture、
  high-compression VAE、MMDiT / joint condition-target modeling、caption/data pipeline、256P→512P→1024P/2K
  多阶段 T2I/TI2I curriculum、prompt enhancer 的 SFT→GRPO、distillation/inference、generation/editing 与 human
  evaluation、Conclusion；并核对官方 repository surface。报告没有独立 Limitations / Safety 章节，公开仓库也
  没有能冻结 2.0 训练与推理结果的完整 artifact，这些缺口本身计入 evidence boundary。
- **Problem / Previous Design / Changed Constraint**：generation 与 editing 分开训练、低压缩 VAE 和单一自然语言
  caption 在短文本、低分辨率阶段合理；当 workload 转向长文本、多语字体、2K photorealism、复杂关系与统一编辑时，
  latent token 数、condition ambiguity 与 task distribution 同时放大，单纯扩大 backbone 会把成本与数据噪声一起放大。
- **Mechanism / State / Data Flow**：Qwen3-VL encoder 提供语义 condition，high-compression VAE 缩短 visual-token
  sequence，MMDiT 联合处理 condition 与 target；训练数据按 resolution 和 T2I/TI2I task 逐阶段扩展，过滤从文件、
  resolution、dedup、NSFW、rotation、entropy、CLIP alignment 到 token length。caption 分 general/text/knowledge/
  structured；Prompt Enhancer 从 degraded user prompt 反向学习 intent expansion，先 SFT，再把候选 prompt 经 frozen
  generator、MLLM/rule rewards 用 GRPO 优化。模型、caption schema、filter revision、PE 与 generator/reward revision
  因而属于同一个训练 lineage，而非独立功能开关。
- **Evaluation / Evidence Boundary**：作者 human evaluation 与 Arena snapshot 支持该公开模型/采样/题集下的相对
  改善，不证明开放域绝对质量。报告未披露总数据量、训练硬件/precision、compute、multi-seed、完整 rater agreement、
  production latency/concurrency/SLO，也缺少 filter/caption/PE 各环节的完整因果 ablation。Prompt Enhancer 可能把
  underspecified intent 变成模型偏好的细节；MLLM reward 又可能与最终 evaluator 共享偏差。
- **Trade-offs / Evolution / Chapters**：`separate generation/editing + low-resolution curriculum → unified conditional
  target modeling → staged multi-resolution/task data → prompt rewriting tied to downstream visual reward` 是
  `Layering / Dependency`，不是后者否定专用 editing model。专用模型在窄任务、低延迟、可解释 intent preservation
  下仍可能更合理。已读 Ch17、Ch23、Ch27～30、Ch62；主 owner 暂定 Ch17，Ch23 承接 data curriculum，
  Ch29/62 只作 reward/evaluation handoff。
- **Disposition / Open Questions**：provisional `Refine — Existing Argument / Experimental`；Historical Books Gate
  关闭，本轮不修改 Books。待核验 2.0 weights/model card、training manifest、filter thresholds、PE hallucination/
  abstention、safety taxonomy、event-time repository revision，以及同硬件、同分辨率、同 sampler 下的 latency/SLO。

### Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K — 26/30

- **Candidate / Week / Source Family**：`MULTIMODAL-LONG-CONTEXT-DATA-CURRICULUM`；W20；
  arXiv:2605.13831 v1，first-public 2026-05-13。论文以 Qwen2.5-VL-7B 为主实验，并用
  Qwen3-VL-8B 做 recipe transfer diagnostic；后者原生已支持 256K 且经历约 100B long-context tokens、
  SFT/RL，不能被写成同一套严格的 32K→128K context-extension 实验。
- **Direct Primary Source / Full-read Coverage**：已读 29 页 PDF 的 metadata、Abstract、Introduction、
  Related Work、data construction、length/mixture curriculum、mRoPE extension、全部 main tables、
  256K/512K extrapolation、cross-task transfer、Conclusion、Limitations，以及 Appendix 的 training
  configuration、prompts、dataset statistics、short-context mixture、mRoPE-base 和 task-ratio ablations。
  当前未发现作者代码或可重放训练 artifact，因此实现结论限于论文披露。
- **Original Problem / Why Previous Design Was Reasonable**：仅调整 position encoding 或把最大 accepted
  length 增大，无法保证模型在数十页视觉文档中找到证据并完成 extraction/reasoning。短文本或单图训练
  在历史上合理：样本便宜、batch 大、优化稳定，且多数 VQA 不要求跨页状态；但文档长度上升后，模型
  同时面临 visual-token budget、长距离定位、局部/全局歧义与固定 token budget 下的数据机会成本。
- **Changed Constraint / Principle**：长上下文能力是 `position support × evidence-bearing training
  distribution × task contract` 的联合结果。固定 5B training tokens 时，样本长度、长短样本比例和
  extraction/reasoning 比例不是独立 loader 参数，而是在重新分配监督密度与可见证据位置。论文把
  “extend context”改写为 data curriculum 问题，而不是宣称 mRoPE base 单独创造长文档能力。
- **Mechanism**：作者从 1,537,504 份 PDF、36.6M pages 的文档池采样，每份原始 PDF 约 20～200 页；
  训练样本选择 32～50 rendered pages，DPI 144，使用 `2×2` visual-token unshuffle，把序列放入约
  32K～128K token 区间。OCR expert 先提供 layout-aware parse，Seed2.0 在连续 8～15 页 evidence
  segment 上生成问题/答案，再恢复完整文档作为上下文；问题锚定 page/section，降低“局部正确但全局
  歧义”。任务分为 single extraction、multi extraction、reasoning，并包含 full/needle OCR 分支。
  模型侧把 Qwen2.5-VL-7B 的 dynamic-NTK mRoPE base 从 `1e6` 调至 `4e6`。
- **State Ownership / Control Flow / Data Flow**：data pipeline 拥有 PDF identity、page range、render
  configuration、OCR layout、evidence segment、question type、answer 与 split；image processor 拥有
  resolution/unshuffle 后的 visual-token budget；trainer 拥有 length/task/short-data sampling weights；
  model/runtime 只消费最终序列，不能恢复 preprocessing 已丢失的页面证据。流向为 `PDF → exact-file
  dedup/filter → page render/OCR → coherent evidence segment → anchored QA synthesis → restore full document
  → length/task mixture → multimodal tokenization → training`。SHA-256 只控制 exact-file duplication，
  不证明语义去重、benchmark contamination 或版本近重复已消除。
- **Implementation / Training Contract**：主实验总预算固定 5B tokens，max length 131,072，global batch
  约 4M tokens（32 sequences/update），AdamW `wd=0.1`、`beta=(0.9,0.95)`、peak LR `1e-5`、10%
  warmup、cosine decay 至 `1e-6`。VeOmni + FlashAttention，Ulysses sequence parallel=2、FSDP=4；
  单个 8-GPU H20 node 可容纳配置，实际训练使用 8 nodes / 64 H20，约 2.9K H20 GPU-hours。论文未披露
  mixed-precision 细节、完整 wall-clock/throughput、数据生成成本或服务 SLO，不能补推。
- **Evaluation / Baselines / Ablations**：LongPT、LongPT+5B SFT 与长文档 VQA objective 在同一主模型
  上比较，但额外 SFT 分支总训练预算已高于纯 5B-token branch，不能称完全 compute-matched。长度分布
  比较 broad pool-native 与 long-biased：后者 `>=100K` 占比 83.9%，前者 23.6%；pool-native 在三个
  task average 上只分别高约 1.3/0.1/1.7 points，支持长度多样性但效应有限。extraction:reasoning 从
  0:10 到 10:0 的 grid 中 8:2 得 57.70，6:4 接近，说明最佳 mixture 依赖 benchmark，而非通用常数。
  short-data 0～80% ablation 下，纯 long 的 long-document average 57.70、40% short 为 57.01；短任务
  base 66.47、纯 long 65.48、20% short 66.53。因此“无需 short mixture”过强；纯 long 最大化该长测，
  20～40% short 是保留短能力的共存分支。
- **What the Evidence Proves**：在上述 7B model、数据和 5B-token contract 中，完整 recipe 把作者
  long-document aggregate 从 50.59 提至 57.70，即 `+7.11 absolute points`；这里不用论文的百分号表述
  推成相对提升。mRoPE `2e6/4e6/8e6` ablation 中 2e6 与 4e6 接近、8e6 有不一致回退，证明 position
  base 是需要协同验证的条件而非单调旋钮。Qwen3-VL-8B 上额外收益说明 data recipe 有 transfer signal，
  但不是严格 context-extension replication。
- **What It Does Not Prove / Threats to Validity**：256K/512K 测试通过在左右交替插入 negative documents
  构造超长输入；MMProLong 从 base 的 38.12/19.49 到 55.09/52.52 支持这一 benchmark 上的 extrapolation，
  不证明任意真实 512K 文档、任意 evidence density 或生产 SLO 可靠。只覆盖 7B/8B；没有 30B/70B、
  真正 >128K training、multi-seed/error bars、semantic contamination audit 或 resolution/token-budget
  sensitivity。MMLongBench v1.1 的部分 free-form/list evaluation 依赖 LLM judge/F1，judge reliability 与
  cost 是作者明确限制；跨 benchmark transfer 也不等于 Agent 长时状态能力。
- **Trade-offs / New Failure Modes**：更长样本减少每个 token budget 下的独立 questions 和 optimizer
  updates，增加长样本尾部 padding、GPU-hour、生成/审核成本与单个坏样本的影响范围。question synthesis
  提高监督密度，也引入 generator bias、answer leakage、错误 evidence anchor 与 task-template collapse；
  OCR/render/unshuffle 形成不可逆 evidence bottleneck。long-biased sampling 可能降低长度多样性，纯 long
  可能损伤短任务；加入 short data 又稀释长程证据预算。位置 base 过大也会改变已训练距离上的 inductive
  bias。短文档、多图局部问答或严格成本场景下，短训练与检索/分页 pipeline 仍然合理。
- **Evolution / ROADMAP / Existing Coverage**：演进关系是 `accepted position range → long-sequence
  systems support → evidence-bearing long-document data → task/length curriculum → controlled extrapolation`，
  对 mRoPE 是 `Layering / Dependency`，对普通多模态数据工程是 `Direct Evolution`。已读 Ch17、Ch22、
  Ch23 及其相邻能力生产链。Ch22 已区分 accepted length、effective utilization 与 system capacity，Ch23
  已把 visual-token transformation、length truncation 与 mixture 作为 training policy；缺口是把 evidence
  segment、恢复完整上下文、长度分布和 task mixture 连成一个可审计 curriculum。主 owner Ch23，Ch22
  仅保留 extrapolation/effective-utilization handoff，Ch17 保留 visual preprocessing handoff。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument` / Ch23，
  `Status: Experimental`；Historical Books Gate 关闭，本轮不改 Books。待验证 semantic dedup/contamination、
  synthesis QA correctness、真实 256K/512K document distribution、judge calibration、不同 resolution/
  visual-token budgets、larger models 和 multi-seed stability。

### RubricEM: Meta-RL with Rubric-guided Policy Decomposition beyond Verifiable Rewards — 26/30

- **Candidate / Week / Source Family**：`RUBRIC-STAGE-CREDIT-REFLECTION-META-POLICY`；W20；
  arXiv:2605.10899 v1，first-public 2026-05-11。当前只有 v1；未发现作者发布的 model weights、training
  code、rubric bank 或 judge traces，因此机制与实验依据限于 63 页论文及其 Appendix，不能独立重放。
- **Full-read Coverage**：已读 Abstract、Introduction、Related Work、四阶段 scaffold、SS-GRPO 公式、
  evolving rubric judge、reflection meta-policy、全部 main results/600-step ablations、short-form transfer、
  SFT data generation/rejection、rubric buffer、async pipeline/windowed curriculum、三组理论分析、完整
  hyperparameters、benchmark/judge contract、infrastructure、Algorithm、Limitations 与 broader impact。
- **Original Problem / Why Previous Design Was Reasonable**：terminal reward broadcast 在答案可精确验证、
  trajectory 短时简单、便宜且避免 process label；inference-time reflection/memory 又无需改训练系统，适合
  低频 adaptation。开放式 deep research 没有唯一答案，Plan/Search/Review/Answer 跨多轮 tool calls，单个
  terminal judge score 把不同决策阶段混成同一 credit；静态反思只能增加 context，不能保证模型学会生成、
  筛选或迁移有用经验。
- **Changed Constraint / Principle**：当最优 action 依赖当前 decision mode，显式 stage 可以减少 compressed
  context 的 state aliasing；当真实中间信号大于 judge misalignment 时，stage reward 才可能比 terminal
  broadcast 更接近目标 gradient。Rubric 由此成为三个平面的共享 interface：policy 用它约束工作流，judge
  用它产生 stage reward，memory 用它表示 outcome-aware reflection。这个统一减少 schema translation，
  也把同一 judge bias 同时注入 execution、learning 与 memory。
- **Mechanism / Control Flow**：SFT 先把 trajectory 固定成 `Plan → Research → Review → Answer`，Plan
  生成 task-specific rubric，Research 每轮依据 rubric 做 state evaluation 并可修改 plan，Review 审计 evidence，
  Answer 按 writing plan 与 citations 合成。SS-GRPO 对同一 query 采样 8 条 rollouts；Gemini-3-Flash 按四个
  stage 生成/维护 rubric，并评分 `R_(i,k)`。上三角依赖矩阵 `Lambda` 把本阶段及 downstream scores 汇成
  `G_(i,k)`，按 stage/group 标准化 advantage；同一 stage tokens 共享该 advantage，仍保留 clipping 与 KL。
- **Reflection Meta-Policy / Data Flow**：shared Qwen3-8B backbone 从一条均匀随机选取的 rollout 生成 8 个
  reflections，privileged judge 同时评估 same-query refinement 与 cross-query transfer；全部候选分数训练
  reflection tokens，只有最高分有效项写入 rubric bank。bank 用 Qwen3-Embedding-0.6B + FAISS 做跨任务
  top-2 检索，用 question SHA-256 做同任务 exact retrieval。`K=3` window 先处理三批 fresh queries，再按
  同序 replay，给 asynchronous reflection/bank write 留出完成时间。
- **State Ownership / Persistence**：task policy/shared backbone 拥有可训练参数；environment 拥有真实 tool
  outputs；judge 拥有 stage scores/justifications；每个 stage 的 active rubric buffer 以 rollout-group score
  variance 衡量 discrimination，容量为 3/2/2/3，persistent rubrics 不被自动淘汰；agent rubric bank 拥有
  accepted reflection、query embedding/hash 和覆盖关系。Checkpoint 必须联合保存 model/optimizer、rubric
  buffers、bank 与 dataloader position；否则 resume 后 policy、judge criteria、memory 与 two-encounter
  curriculum 会错位。覆盖旧 reflection 只有 latest value，没有公开 supersession/provenance retention。
- **Implementation / Training Contract**：SFT 使用约 11K Gemini-3.1-Pro 生成 trajectories，约 13K 原始
  questions 中不合 schema、缺 tool call/answer 或连续 tool error 的样本被 rejection；约 15～25% 因未完成
  等原因丢弃。Qwen3-8B、5 epochs、BF16、8×H100 80GB、ZeRO-3、max 16,384、effective batch 128。
  RL 使用约 4.9K long-form queries，Ray/open-instruct + vLLM、ZeRO-3 CPU offload、32 prompts×8 rollouts、
  LR 5e-7、KL 0.001、response 18,432、prompt 8,192、最多 10 tool calls；600-step ablations 用 2 nodes，
  final 1,400-step run 用 4 nodes。论文未披露 nodes 的 GPU 数/型号、总 tokens、总 GPU-hours、完整
  wall-clock、judge API cost 或 serving concurrency。
- **Judge / Runtime Contract**：每 step 32 次 rubric-generation 与 256 次 trajectory-scoring API calls 并行，
  失败时 generation 视为无新 rubric、scoring 回退为 terminal answer score；作者报告约 5 分钟且与 gradient
  computation overlap。reflection branch 滞后一 step，训练 engine 在 Phase A 消费上一批 reflection，
  inference engine 同时生成下一批 task rollouts。论文称没有新增 sequential wall-clock bottleneck，不等于
  reflection/judge 没有额外 compute、API 成本或 failure surface。
- **Evaluation / Ablations**：主表比较 HealthBench、ResearchQA、DeepResearchBench、ResearchRubrics；
  RubricEM-8B 从 SFT average 49.2 到 RL 55.5。不同 proprietary/open baselines 的 teacher、search backend、
  harness 与 reported/reproduced score 不完全相同，不能据排行榜声称模型本体更强。更可信的是同一 SFT
  起点、同一 600-step/固定每 benchmark 100-sample subset 的四分支：answer-only GRPO、SS-GRPO、
  answer-only+meta-policy、full recipe；两个机制单独有增益，组合最好。structured/unstructured SFT+RL、
  same Gemini scaffold vs ReAct、bank reuse vs baseline retrieval 进一步支持 stage structure 与 learned
  reflection 的局部贡献，但未披露 multi-seed/error bars 或完整数值表。
- **What the Evidence Proves**：在该 8B/long-form/search/judge contract 下，显式 workflow stage 可以成为
  credit unit，stagewise semantic reward 与 reflection auxiliary RL 提供互补的作者实验信号；main evaluation
  不注入 bank context，说明结果不是简单的 test-time prompt-length 优势。理论只证明 value-of-stage
  information 和“judge error 小于遗漏 intermediate signal”“accepted reflection gradient 与 task gradient
  正相关”等条件命题，清楚标出了机制成立所需的 alignment assumptions。
- **What It Does Not Prove / Threats to Validity**：self-generated/persistent rubric 不是 oracle；同一 Gemini
  family 参与 SFT teacher、search summarization、training judge 与部分 evaluation，可能产生 correlated
  preference、style leakage 与 reward hacking。所有 RL rewards 都来自 rubric judge，没有 citation/format/
  executable verifier；论文主动排除 citation-heavy SQAv2，也承认 teacher academic citations 不可靠。
  infrastructure 多次 shutdown/restart，使 async staleness 超过设计的一 step；网络/API latency 未控制。
  单 backbone、单主 judge、无 independent human audit、无 code/weights、多 seed 和 safety evaluation。
- **Trade-offs / New Failure Modes**：stage schema 提供可观测边界，却会把合理的非线性研究路径挤进固定
  Plan/Research/Review/Answer；stage-shared advantage 仍不能给 stage 内 token/action 做因果 credit。
  variance-pruning 偏好能区分当前 rollouts 的 rubrics，不等于选择长期正确标准；persistent rubric 不淘汰会
  固化过时偏差。shared backbone 允许 reflection gradient 迁移到 task policy，也可能产生 negative transfer。
  bank top-k similarity、best-of-8 judge selection 与 overwrite 会引入 retrieval poisoning、winner's curse、
  provenance loss、non-deterministic resume 和跨任务误迁移。judge outage 回退到 terminal score 会在同一
  run 中改变 reward semantics。
- **Where Previous Designs Still Apply / Evolution**：答案可执行验证、trajectory 短或 judge 不可信时，
  terminal GRPO/规则 verifier 仍优先；高风险流程需要独立 human/executable evaluator，不能让 self-rubric
  闭环自证；低频任务或训练预算不足时，inference-only reflection 与受治理 static memory 仍合理。演进是
  `terminal reward broadcast → process/stage reward → evolving stage rubric → joint task/reflection policy →
  retrieved derived memory` 的 `Direct Evolution`；相对 Workflow/Memory/Evaluation 是 `Layering / Dependency`。
- **ROADMAP / Existing Coverage / Decision**：已读 Ch29、Ch62、Ch73、Ch76、Ch77 及相邻内容。Ch29 已有
  sequence-to-token credit、process verifier 与 GRPO state pipeline，但缺少“semantic stage 是 reward unit，
  judge criterion state 与 advantage granularity 必须对齐”的受限分支，故主 owner Ch29。Ch62 已覆盖 rubric
  formation/execution/judge calibration，Ch73 已覆盖 derived memory provenance，Ch76 已把 test-time
  reflection 与 parameter update 分开，Ch77 已覆盖 workflow state；这些只需 handoff，不重复正文。
  provisional `Refine — Existing Argument` / Ch29，`Status: Experimental`；Historical Books Gate 关闭，
  本轮不改 Books。
- **Open Questions**：stage matrix 与 caps 如何 calibration；judge/rubric revision 如何写入 rollout lineage；
  rubric-bank overwrite 怎样支持 supersession/delete/rollback；更换 independent judges 后增益是否保持；
  如何测量 stage 内 action credit、negative transfer、reward fallback 频率和 stale-reflection 分布。

### Process Rewards with Learned Reliability / BetaPRM — 24/30

- **Candidate / Week / Source Family**：`DISTRIBUTIONAL-PRM-RELIABILITY-ADAPTIVE-COMPUTE`；W20；
  arXiv:2605.15529 v1，first-public 2026-05-15。作者 repository `JinYuanLi0012/Beta-Binomial-PRM`
  公开 InternVL training/evaluation/ACA code 与 processed annotation 下载入口；repo 当前 revision 晚于
  event date，用于 artifact 核验，不把后续 commits 倒写成 v1 已公开事实。
- **Full-read / Artifact Coverage**：已读 18 页正文和 Appendix：PRM/MC supervision、Beta-Binomial
  formulation、parameterization/loss、ACA stopping/repair、四 backbone/四 benchmark 主表、error-detection、
  regularizer/uncertainty ablations、training/evaluation protocol、limitations；并核对 repo 的 data layout、
  ZeRO-3 training、Qwen judge rollout labeling、PRM evaluation 与 ACA orchestration。未下载大体积 processed
  annotations/checkpoints，故不宣称复现结果。
- **Original Problem / Why Previous Design Was Reasonable**：标准 prefix-conditioned PRM 输出一个
  scalar `p(success | prefix)`，便于 candidate ranking、process supervision 与 policy reward；若 step label
  稳定或下游只需粗排序，这个接口简单合理。但 Monte Carlo supervision 实际是从同一 prefix 采样 `N`
  条 continuations 得到 `K` 次成功，`K/N` 只是有限样本观测；把它当精确 point target 会丢掉 evidence
  quantity，并让下游无法区分“高分且有支持”与“高分但不确定”。
- **Changed Constraint / Principle**：measurement 应保留原始 observation contract，而不是先压成标量再
  学习。BetaPRM 把 latent prefix success probability 写成 Beta belief：mean `mu` 仍作为 reward，
  concentration `kappa` 表示该 belief 对 MC count 的尖锐度。它建立的是“在训练分布与 continuation
  generator 下，这个 reward estimate 能多集中地解释 K/N”的 evidence reliability，不是 epistemic truth、
  calibrated correctness probability 或安全置信度。
- **Mechanism / Objective**：在每个 `<prm>` marker，Yes/No logits 的二类 softmax 给出 `mu`；hidden
  state 经 linear head、softplus 与 `kappa_min` 给出正的 `kappa`，再令 `alpha=mu*kappa`、
  `beta=(1-mu)*kappa`。训练最大化 `K | N, alpha, beta` 的 Beta-Binomial likelihood，而不是对 `K/N`
  做 CE。辅助项 `|stopgrad(mu)-K/N|*kappa` 在 mean 与观测冲突时惩罚过高 concentration；stop-gradient
  避免它退化为另一条 point-label mean regression。
- **State Ownership / Data Flow**：continuation generator、sampling config 与 final-answer judge 共同拥有
  `K,N` observation；dataset 必须保存 problem/prefix/step boundary、generator/judge identity、decoding、
  `K,N` 而非只留 ratio。PRM checkpoint 拥有 `mu/kappa` heads；ACA controller 拥有 maximum budget、
  current candidate pool、risk score、LCB/UCB、stop decision 与 repair cutpoint。流向为 `prefix → N sampled
  continuations → judged success count (K,N) → BetaPRM → mean+concentration → risk-aware ranking/allocate/
  stop/repair`。若 generator、judge 或 step parser 改版，旧 concentration 不应静默视为同一 reliability。
- **ACA Control Flow**：先生成 `n0=4` 完整 candidates，最大 `N=16`，每次追加 4。step uncertainty 为
  `sqrt(mu(1-mu)/(kappa+1))`，candidate risk score 按 steps 平均 `mu-lambda*sigma`；当当前 winner 的
  LCB 高于所有 competitors 的 UCB 时 early stop。否则选择最高 UCB non-winner，在最早低 conservative
  score step 或最高 uncertainty eligible step 截断后续并重新采样。它把 fixed Best-of-N 演进成有状态
  sequential allocation policy，新增 path dependence 和 controller hyperparameters。
- **Training / Evaluation Contract**：唯一公开保留 count 的 training source 是 VisualPRM400K-v1.1，
  每 prefix `N=16`；backbones 为 InternVL2.5-8B、InternVL3-8B/14B、Qwen2.5-VL-7B。AdamW、1 epoch、
  global batch 512、max length 8192、LR 1e-5、LLM/projector trainable、vision encoder frozen；论文未披露
  training hardware/GPU-hours/precision，repo 默认 InternVL path 需 4×80GB GPUs，不等于主实验硬件。
  Candidate pools 均由 InternVL2.5-8B 以同一池供 selectors；ACA generation 为 temperature 0.7、top-p 0.9、
  top-k 30、max new tokens 2048。final-answer labels 依赖 judge；repo example 使用 Qwen2.5-32B-Instruct，
  论文未把所有 judge revision/error contract 完整量化。
- **Baselines / Ablations / Evidence**：BetaPRM 相对同-backbone standard PRM 在四个 visual-math Best-of-16
  blocks 平均多 1.29/1.46/3.37/2.66 absolute points；同一 candidate pool 隔离了 selector，但 risk-budget
  selector本身也只给 BetaPRM 使用，改进是 distributional training + uncertainty-aware ranking 的组合。
  VisualProcessBench micro-F1 有持平、小升和一项下降，支持“不显著摧毁 error detection”，不支持普遍
  提升。去掉 evidence regularizer 平均下降 1.02 points；`kappa` training curve 的 mean/90th percentile
  分离说明输出不是常数，却不是 external calibration test。ACA 相对 fixed BoN 在两 backbones/四 benchmarks
  的作者 contract 中同时少用 16.76%～33.57% 或 19.39%～33.00% generated tokens 并提高 accuracy；无
  early-stop branch 会在若干任务降分，说明 compute redirection 本身并非单调收益。
- **What It Proves / Does Not Prove**：证据支持在 VisualPRM count supervision 下，显式保留 count likelihood
  并学习 second channel 可以改善受限 candidate selection，且 reliability-aware stopping/repair 能形成更好的
  accuracy-token operating points。它不证明 `kappa` 对真实 correctness 校准、跨 generator/judge/domain
  可迁移、对文本-only reasoning 有效，或 early-stop LCB/UCB 具有频率学置信区间 coverage；这些 bounds
  是 learned Beta uncertainty 上的 heuristic control rule。四项 benchmark 共用 visual-math 生态，只有一份
  public count dataset，无 multi-seed/error bars、OOD calibration/ECE、adversarial prefix、judge-noise、N
  sensitivity、latency/KV/PRM overhead 或 tail-SLO 评估。
- **Trade-offs / Failure Modes**：保留 counts 增加 dataset/storage/generation/judge 成本；同一 `K/N` 在不同
  `N` 下证据不同是收益，也使 label semantics 绑定 continuation policy。Beta family 可能错误表达多峰或
  distribution-shift uncertainty；regularizer 可能让模型通过压低 `kappa` 回避错误 mean。step average 会把
  长度、早期关键错误与相关 steps 混平；prefix repair 假设截断前状态仍值得保留，且重新生成可能重复同一
  failure。过早停止会锁定 confident-wrong candidate，过晚停止又失去成本收益。固定 BoN 在 scorer 未校准、
  controller复杂度不值或需要可预测 latency 时仍合理；rule/executable verifier 在可验证任务中仍优先。
- **Evolution / ROADMAP / Decision**：`point step label → MC success ratio → preserve (K,N) count evidence →
  reward mean + learned reliability → risk-adjusted selection → adaptive stop/repair` 是 `Direct Evolution`。
  已读 Ch20、Ch29、Ch62 及其相邻界面。Ch20 已覆盖 coverage/selection 与固定 budget，但尚未沉淀 scorer
  reliability 驱动的 sequential allocation；Ch29 已说明 process reward exploit surface；Ch62 明确拥有 scorer、
  uncertainty、evidence/decision separation，故主 owner Ch62，Ch20/29 作短 handoff。provisional
  `Refine — Existing Argument` / Ch62，`Status: Experimental`；Historical Books Gate 关闭，不改 Books。
- **Open Questions**：需要 reliability diagrams/ECE/Brier 与 coverage tests；不同 `N`、generator temperature、
  judge error 和 domain shift 下 `kappa` 是否稳定；controller 怎样纳入 PRM forward、KV reuse、latency 与
  SLO；如何检测 confident-wrong prefixes、定义 abstention，以及保存 allocation decision trace。

### Full Attention Strikes Back / RTPurbo — 25/30

- **Candidate / Week / Source Family**：`RTPURBO-DENSE-TO-SPARSE-POST-TRAINING`；W20；
  arXiv:2605.16928 v1，2026-05-16；v2 为 2026-06-08。W20 事件归属只依据 v1；当前 HTML 为 v2，
  用于核对 revision 后的机制与实验，但不把 6 月补充内容倒写成 5 月已公开事实。
- **Direct / Related Primary Sources**：arXiv metadata、20 页 v2 HTML/PDF。论文未提供可定位的官方
  repository、checkpoint 或 benchmark artifact；因此 kernel、training recipe 与结果只能按作者论文核验，
  不能视为可独立复现的 release evidence。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、offline head calibration、
  local/retrieval head split、low-dimensional routing、dynamic top-p、two-stage post-training、training
  algorithms、custom H20 kernels、全部 main tables/figures、ablation、ultra-long experiment、Conclusion
  与 Appendix 配置。论文标题中的 “within Hundred Training Steps” 已与正文实际 step contract 对齐。
- **Original Problem / Why Previous Design Was Reasonable**：full attention 在训练和短中上下文里提供统一、
  无需先验路由的 token interaction，dense KV 与标准 FlashAttention 也让模型质量和 kernel contract 简单。
  training-free eviction 或 static sparse pattern 则在不能重新训练、局部依赖占主导时合理。约束变为超长
  context decode 后，绝大多数 query-head 只需局部 token，少量 retrieval heads 却需要跨全文找证据；对所有
  heads 保存并扫描全部 KV 会把 memory bandwidth 与 latency 成本扩展到 context length。
- **Changed Constraint / Principle**：attention sparsity 不能只按 layer 或 KV head 粗粒度假设。GQA/MQA 中
  同一 KV head 下的 query heads 仍可能承担不同功能；应先识别 head role，再把“候选发现”和“精确注意力”
  分开。稀疏预算也不应固定为 token count，而应按 query 的 attention-mass distribution 动态决定。
- **Mechanism**：作者用一份首尾重复 needle 的长 FineWeb 文档，测量后段 query 对前段 token 的 attention
  mass，把约 15% query heads 标为 retrieval heads，其余为 local heads。local heads 使用 8192-token window
  加 4 个 sink tokens；retrieval heads 在 prefill 保持 dense，并保留完整 KV。decode 时以冻结前 RoPE Q/K
  经 rank-16 projection 得到 routing scores，按累计概率 `top-p=0.9` 选择 token，再在这些 token 的原始高维
  Q/K/V 上执行精确 attention。GQA/MQA 的 compute sparsity 按 query head 计，KV memory sparsity则取共享
  KV head 下所有 query selections 的 union，二者不可混报。
- **Training / State Ownership**：Stage 1 冻结 backbone，只训练 projection，以 projected attention 与 full
  attention distribution 的 KL 对齐；约 8,000 条 FineWeb 32K～80K sequences、约 30M tokens、约 600
  steps。Stage 2 冻结 projection，让 sparse student 对 dense teacher 的 top-10 logits 做 self-distillation，
  约 8,000 条 Dolma 3 Longmimo Mix、平均 48K、约 180M input tokens 与约 1.2M label tokens、约 600
  steps。模型权重拥有 sparse-behavior adaptation，projection 拥有候选路由，runtime 拥有 current query
  的 selected-token set，KV cache 仍拥有 retrieval heads 的完整历史；论文总计约 840K projection parameters。
  因此标题不能解释为“总训练不超过一百步”。
- **Control Flow / Data Flow**：`offline dense trace → head-role calibration → local/retrieval mask → Stage-1
  router alignment → Stage-2 sparse-student distillation → prefill full KV for retrieval heads → decode projected
  score → dynamic mass threshold → exact sparse attention → output logits`。top-p selection 是每个 decode
  query 的动态状态；阈值或 head classification 错误会在 exact attention 之前不可逆地漏掉候选。
- **Implementation Details**：作者为 NVIDIA H20 实现 block-wise top-p kernel：每 block 统计 256-bin
  histogram，每 head 约 1KB histogram state，最后一个 CTA 决定 threshold；sparse decode 使用 register/
  `half2` loads 并切分 KV ranges。论文环境为 Python 3.14、CUDA 12.8、PyTorch 2.8，核心配置为 local
  window 8192、4 sinks、projection dim 16、top-p 0.9、kernel block 64。GPU 数量、training precision、
  serving batch/concurrency 与 SLO 未披露。
- **Evaluation Contract**：Qwen3-Coder-30B-A3B 用 LongBench 与 RULER，Qwen3-30B-A3B-Think 用
  AIME 2024/2025 与 MMLU-Pro；baselines 包括 RazorAttn、MInference、FlexPrefill、Quest、SnapKV 和
  static top-k 4096。LongBench average 为 full 53.80、RTPurbo top-p 54.24；RULER 32K 为 89.65/90.06，
  64K 为 86.23/85.49。相近或偶有更高分只说明未观察到一致的大幅退化，不证明稀疏化提升模型能力。
  论文的 512K evidence 也只来自其受限 ultra-long benchmark。
- **Ablations / Sensitivity**：dynamic top-p 会随 query 难度改变 active tokens，例如作者的 32K needle 与
  multi-key tasks 分别约 469 与 2,462 tokens；64K 不同 heads 可从 21 到 24,621。retrieval ratio 从 15%
  增至 30% 未见收益，降至 10% 会退化；projection dim 4 因选择更多 tokens 而表面 accuracy 更高，dim
  16 在 fitting/sparsity 间最好，dim 32 无明显收益。这些结果支持路由误差、token budget 与质量耦合，
  但单 family、单次 calibration 和无 multi-seed 不能确定稳定 operating point。
- **Performance Evidence Boundary**：作者报告的 prefill 2.83×（32K）到 9.36×（1M）以及 decode
  1.47× 到 2.01×，是 H20 上单 attention layer/operator 相对 FA2 的 microbenchmark；不是包含 model
  layers、MoE、sampling、KV allocation、scheduler、network 和 queueing 的端到端 TTFT/TPOT 或 serving
  throughput。precision、batch、concurrency、GPU count 与 SLO 未完整披露，故这些数字不得进入通用
  inference 性能结论。
- **What It Proves / Does Not Prove**：证据支持 dense checkpoint 可以通过受限 post-training 获得
  head-aware sparse decode 分支，并且低维候选路由后在原始 feature space 执行 exact attention 可保留较多
  benchmark quality。它不证明“一份 calibration document”跨模型、语言、domain 与 workload 稳定，
  不证明所有 full-attention models 都能同样迁移，也不证明 self-distillation 已消除 data-mixture tuning。
  仅评估 Qwen family，且无 public code、multi-seed、OOD head-role drift、完整 KV capacity、tail latency、
  scheduler interaction 或 failure-recovery evidence。
- **Trade-offs / New Failure Modes**：retrieval heads 的 dense prefill 与 full KV 保留限制 memory saving；
  low-dimensional router 降低 decode scan cost，却新增 calibration drift、false-negative retrieval、dynamic
  allocation variance、GQA union inflation 与 kernel portability。fixed local/window 或 training-free eviction
  在短 context、不能 post-train、硬件不支持 custom kernel 或需要 predictable latency 时仍成立；native sparse
  pretraining 在从头训练且允许共同学习 router/representation 时仍是另一分支，而非被 RTPurbo 替代。
- **Evolution / ROADMAP / Decision**：`full attention → head-role calibration → local/retrieval split →
  low-dimensional candidate routing → dynamic mass budget → exact sparse attention → hardware-specific kernel`
  是 `Direct Evolution`，但它与 native sparse pretraining、KV eviction 是并行 alternatives。已读 Ch22 及
  Ch21/23 邻接，并核对 Ch14、Ch39～41、Ch45、Ch50 的接口。Ch22 已拥有 long-context sparse-attention
  分支，缺口是“post-hoc dense-to-sparse adaptation”及 compute/memory sparsity分账，故主 owner Ch22；
  prefill/decode/KV/kernel 章节只作 handoff。provisional `Refine — Existing Argument` / Ch22，
  `Status: Experimental`；Historical Books Gate 关闭，不改 Books。
- **Open Questions**：需要 v1/v2 diff 与 public artifact、跨 model/domain 的 head-role stability、routing
  miss audit、multi-seed calibration、完整 precision/batch/concurrency/SLO contract、端到端 TTFT/TPOT/
  throughput/KV-capacity，以及与 native sparse training 和现代 paged-KV scheduler 的 matched comparison。

### WildClawBench: A Benchmark for Real-World, Long-Horizon Agent Evaluation — 27/30

- **Candidate / Week / Source Family**：`WILDCLAWBENCH-NATIVE-RUNTIME-AGENT-EVAL`；W20；
  arXiv:2605.10912 只有 v1，2026-05-11 17:49 UTC。论文、task suite、container images、grader 与
  current leaderboard 属同一 source family；current repository 的 6～8 月模型和分数是后续 artifact
  evolution，不得倒写成 W20 paper evidence。
- **Direct / Related Primary Sources**：arXiv v1 HTML/PDF、作者 `InternLM/WildClawBench` repository、
  task/grader/source trees、四种 harness image 与运行说明。当前 repository 为 41 commits 且 leaderboard
  已扩展到论文之后的模型；没有 event-time release/tag 可把当前每个路径冻结到 5 月 11 日，因此代码只用于
  核对公开 contract 与实现方向，论文结果仍以 v1 为准。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、task design/data/curation、
  execution 与 hybrid grading、全部 model/harness/skill/time-budget analyses、Conclusion、Broader Impacts、
  Limitations、60-task modality list、skill ablation、failure taxonomy、bilingual slices、three-run variance、
  human–GPT judge case study、per-task run tables、代表 task pages 与 trajectory analysis；并核对 repository
  的 container、task、evaluation output 和 custom endpoint contract。
- **Original Problem / Why Previous Design Was Reasonable**：static QA、mock API、single-surface sandbox 与
  final-answer exact match 成本低、易复现、适合模型回归和局部 capability isolation；它们没有过时。但当部署
  对象变为能够浏览、运行 shell、读写文件、调用 email/calendar、处理多模态 artifact 的 long-horizon Agent，
  最终文本无法说明工具是否真正执行、环境是否被正确改变、是否发生危险或重复 side effects，也无法区分
  model、harness、tool availability 与 time budget 的贡献。
- **Changed Constraint / Principle**：评估对象从 `model output` 扩展为 `model + harness + tool schemas +
  permissions + context policy + time budget + container/environment + external services + scorer`。同一 weights
  在不同 harness 下不是同一个 subject；可复现 container 只冻结本地环境，不能自动冻结 web/API、model
  endpoint、pricing、rate limit 或 judge behavior。
- **Task / Curation Mechanism**：60 个 human-authored tasks 覆盖 productivity 10、code 12、social 6、search
  11、creative 11、safety 10；36 English/24 Chinese，26 multimodal/34 text。每个 Markdown task 绑定 YAML
  metadata、prompt、expected behavior、rubric、workspace、optional Skill/env 与 executable grading function。
  八名研究者用两周完成 authoring→reference/verifiable points→pilot discriminability filter→expert trace/
  grading/leakage review→targeted refinement；pilot 保留条件 `max pairwise score gap >= 0.2` 提高区分度，
  也可能选择性保留对 pilot models 特别敏感的 tasks。
- **State Ownership / Control Flow / Data Flow**：benchmark package 拥有 task/environment/grader identity；
  harness image 拥有 system prompt、tool schemas、context/recovery loop；model endpoint 拥有 weights/sampling
  behavior；container 拥有 run-local workspace；external services 拥有可漂移 state；runner 拥有 budget、
  termination 与 usage；grader 在 Agent 退出后才挂载 ground truth，分别读取 artifacts、audit logs、transcript
  与 environment state；judge 只拥有难以 deterministic-check 的 semantic criteria。`frozen workspace → agent
  trajectory → timeout/exit → inject hidden grader assets → rule/state/judge checks → per-criterion evidence →
  aggregate score`，使 agent-authored completion text 不能成为自证。
- **Implementation Details**：每项在隔离 Docker container 运行 OpenClaw、Claude Code、Codex 或 Hermes
  Agent，image 固定 OS/Python/preinstalled tools。run 保存 artifact、conversation trace、runtime log、tokens、
  cost 与 elapsed time；current repo 输出 `score.json`、`usage.json`、`agent.log` 与 OpenClaw `chat.jsonl`。
  真实 web/browser/email/calendar/tool interfaces 提高 deployment relevance，也引入 authentication、availability、
  rate limit、content drift 和 external side-effect cleanup 的 reproducibility surface。论文称 production-grade，
  但隔离 benchmark container 不等于生产权限、tenant、network 或 secret contract。
- **Evaluation Contract**：论文用统一 OpenRouter endpoint，在 OpenClaw 内比较 19 models；within-harness
  固定 prompt/tool/context policy。任务 budget 为 300～1,200 秒，平均 881 秒；Claude Opus 4.6 snapshot
  平均 8.5 分钟、26 tool calls。四 harness comparison 只覆盖 GPT 5.4、GLM 5、MiMo V2 Pro、MiniMax
  M2.7。rule checks 覆盖文件/格式/数值/字符串/workspace cleanliness，state audit 检查 email/calendar/chat
  side effects，GPT 5.4 judge 处理 narrative/image/video/semantic criteria；硬件、endpoint concurrency、provider
  revision、sampling/temperature、cache contract 与 network stability 未完整披露。
- **Results / What the Evidence Proves**：event-time paper 中 OpenClaw top score 为 62.2%，其余低于 60%；
  同一 model 跨四 harness 最多相差 18 points，支持“harness 是 evaluated system 的一部分”。GPT 5.4
  thinking low→medium 为 50.40→52.63，而 high 降至 45.02 并把 timeout 由 6 增至 15，支持在固定 wall-
  clock 下 internal reasoning 与 environment action 竞争预算。skill augmentation 的 category effects 有正有负，
  也说明 Skill/harness 配置必须进入 subject identity，不能把 aggregate gain 写成 model improvement。
- **Ablation / Variance / Judge Boundary**：四个 models 在 OpenClaw 各重复三次，overall standard deviation
  为 0.7～1.9 points，但 category 可达 4.9；这只支持该小样本 snapshot 的有限 run stability。GPT 5.4 judge
  validation 随机抽 5 个需要 judge 的 tasks、每 task 4 个 model outputs、两名 human evaluators；表中偏差多在
  3 points 内，却没有全 60-task coverage、rank correlation、inter-rater reliability、judge perturbation、prompt
  injection test 或 error interval，故不能支撑论文所称 “highly reliable proxy” 的广泛结论。
- **Failure and Safety Evidence**：作者审计五个 models × 60 OpenClaw runs，共 300 runs；以 score<0.5
  定义 169 failed runs，再区分 wrong/partial artifact、timeout/hang、safety failure、missing artifact，以及
  safety policy、budget exhaustion、debug loop、tool/API breakdown、semantic/planning miss。priority-based
  single process label 便于统计，却会压缩共同原因；论文同时承认 signals 可共现。10 个 safety tasks 能揭示
  prompt/Skill injection、credential 和 destructive-operation failures，但不构成系统 threat-model completeness。
- **What It Does Not Prove / Threats to Validity**：60 hand-authored、single-turn initial instructions 不能代表
  production distribution、interactive clarification、GUI-heavy desktop、biology/finance/law 或长期 multi-user
  state；pilot discriminability filter 会改变样本分布。model revisions、harness versions、OpenRouter routing、
  search/web content、tool failures、pricing 和 current repo 都会 drift。aggregate score 混合 deterministic、state
  与 judge criteria，不能横向解释成统一 correctness probability；单一 weighted leaderboard 也会隐藏 category、
  language、safety、cost 与 timeout trade-off。
- **Trade-offs / New Failure Modes / Previous Designs Still Apply**：native runtime 与真实 tools 提高 ecological
  validity，却增加复现成本、secret/network management、service drift、side-effect cleanup 与供应链风险；hybrid
  grader 提高 coverage，却新增 scorer heterogeneity、LLM-judge correlation、rubric drift 与 evidence aggregation
  policy。Docker isolation 提高 repeatability，却不能模拟 production IAM、tenant interference、human approval
  和 irreversible external actions。static benchmark/executable unit tests 仍适合快速回归和机制隔离；native
  benchmark 只在 deployment 也包含相同 control loop 与 side effects 时提供额外证据。
- **Evolution / ROADMAP / Decision**：`final answer → executable artifact → environment-state audit → full
  trajectory + side effects → model+harness+budget subject → repeated/cost/risk slices` 是 `Direct Evolution`；
  WildClawBench 与 SkillClaw 是 `Layering / Dependency`，前者是 measurement substrate，后者用它评估 Skill
  lifecycle。已读 Ch62 与 Ch61/63 邻接，并核对 Ch68、Ch77、Ch80 handoff。Ch62 已明确版本化 complete
  subject/environment/scorer、Agent trajectory、副作用、hybrid verifier、judge audit、uncertainty 和 cost/SLO；
  本文没有新增超出该框架且证据更强的长期机制。最终 disposition 为 `No Change — Already Covered` /
  Ch62；Ch68 复用 safety slice，Ch77/80 复用 workflow/platform identity。Historical Books Gate 关闭，不改 Books。
- **Open Questions**：需要 event-time repository/tag、container digest 与 model/harness/judge revision；外部 service
  如何 record/replay；如何把 deterministic/state/judge criteria 聚合而不伪装为同质概率；怎样做 held-out task
  author、pilot-model selection-bias、contamination 与 adversarial grader audit；如何测 multi-turn human intervention、
  production IAM、side-effect rollback，以及按 harness × model × task × budget 的 factorial attribution。

### ToolCUA: Towards Optimal GUI-Tool Path Orchestration for Computer Use Agents — 26/30

- **Candidate / Week / Source Family**：`TOOLCUA-HYBRID-GUI-TOOL-PATH-POLICY`；W20；arXiv:2605.12481
  只有 v1，2026-05-12 17:57 UTC。source family 包括论文、project page、ToolCUA repository、公开
  ToolCUA-8B weights 与 evaluation files；repository 的 data pipeline 与 asynchronous training infra 仍在 TODO，
  因此模型/eval release 不能被表述为完整 training artifact release。
- **Direct / Related Primary Sources**：arXiv v1 HTML/PDF、`X-PLUG/ToolCUA` repository、project page 与
  model/evaluation entrypoints。已核对 paper 与 current repo 的职责边界；11-commit/no-release repository 只公开
  model-serving/eval surface，未公开论文所述 10K trajectory synthesis pipeline、training code、250-sandbox
  orchestration 或 frozen event-time environment。
- **Access / Full-read Coverage**：已覆盖 problem definition、MDP、全部 data pipeline、SFT/single-turn RL/
  online Agentic RL、四项 reward、main/transfer/ablation/case experiments、Related Work、Limitations/Ethics、
  source-data/tool statistics、完整 training/evaluation contract、prompt/case appendices，并核对 model serving
  与 OSWorld/OSWorld-MCP evaluation files。
- **Original Problem / Why Previous Design Was Reasonable**：atomic GUI actions 覆盖面广、只依赖可见界面，
  适合 API 缺失或权限不稳定的应用；structured tools 步骤少、参数明确，适合稳定 API 与重复操作。纯 GUI
  在长路径中累积 grounding/click error，纯 tool 又受 coverage、schema、permission 与 API drift 限制。简单把
  两者同时暴露给 model 会扩大 action space：underuse 保留冗长 GUI path，overuse 则可能在必要 visual
  grounding 前调用 brittle tool。旧分支各自仍合理，问题是何时切换。
- **Changed Constraint / Principle**：tool availability 不等于 tool utility；局部可调用 action 不等于全局更优
  trajectory。GUI→Tool 与 Tool→GUI 是会改变后续 observation、cost、failure surface 与可恢复性的 policy
  boundary，应以完整 trajectory outcome 监督，而不是只模仿单步或奖励 tool-call count。
- **Data Mechanism**：从 OpenCUA 8,500、ScaleCUA 300 与 1,200 sandbox trajectories 汇成 10K source
  trajectories/192K GUI steps。强 MLLM 从 GUI procedure 合成 signature、description、arguments 的多粒度
  tool library，生成 functionally-equivalent tool path，再把 predicted next state 对齐原 GUI trajectory 的 screenshot。
  随机移除部分 tools 并用原 GUI subsequence 回填，得到 10K interleaved trajectories/180K SFT steps 与 5K
  critical switches；4,350 synthetic tools、平均 pool 19.75、平均执行 7.89。next-state matching 是 proxy，
  不是在真实 tool implementation 上执行并验证 side effects。
- **Training / Control Flow**：Qwen3-VL-8B-Instruct 先以全参数 SFT 训练 vision tower 与 LLM 3 epochs；再在
  critical steps 用 group-size 32 single-turn GRPO 校准 GUI/tool branch；最后在 OSWorld/QEMU + MCP sandbox
  做 multi-turn GRPO。`R_fmt + R_acc + 0.4 R_tool + 0.2 R_length` 中，tool appropriateness 和 length 只在
  success 时启用；`R_tool` 依赖人工复核的 task-level beneficial/not-beneficial binary label，`R_length` 相对同
  rollout group 的平均 steps 奖励更短 successful path。dynamic filtering 只保留 success/failure mixed groups。
- **State Ownership / Data Flow**：source GUI corpus 拥有 observed action/state pairs；synthesis model 生成 candidate
  tool schema与预计 effect；offline validator 只拥有 format/schema/next-state consistency；training environment
  拥有实际 state transition 与 success；task annotation 拥有 tool-beneficial label；rollout group 定义相对 path
  baseline；policy weights吸收 branch preference；production executor 仍须拥有 authorization、idempotency、
  side-effect audit 和 rollback。`GUI trace → synthetic tool/effect → interleaved variants → SFT → critical-switch RL
  → online environment rollout → success-gated tool/length reward → hybrid policy`。
- **Implementation / Compute Contract**：SFT 使用 `8×8` GPUs；offline RL rollout 32、LR 1e-6、batch 128；
  online RL rollout/batch 32、LR 1e-6、max_steps 30。约 250 Docker instances 承担 ECS rollouts，policy
  training 为 `8×8` GPUs、dedicated inference 为 `4×8` GPUs；每个 online run 约 25 optimization steps、
  约 1,200 effective samples、约 6 天。论文未披露 GPU 型号、precision、token budget、checkpoint/model
  revision、seed/error bars、optimizer/gradient settings、network/SLO 或总生成成本。
- **Evaluation Contract**：OSWorld-MCP 只报告 333 feasible tasks（238 tool-beneficial、95 non-beneficial），
  max 50 steps、average@3；Accuracy 由 benchmark end-state evaluator 给出，TIR 只把“成功且符合 binary tool-
  use label”的任务计入 numerator，ACS 对所有 tasks 平均 steps。ToolCUA-8B 为 46.85 accuracy、24.32 TIR、
  14.93 ACS；base Qwen3-VL-8B 为 28.23/8.41/19.34。约 66% 是相对 accuracy gain，绝对为 +18.62
  points。GUI-only matched-scale SFT+RL 为 42.05，hybrid full 为 46.85，差为 +4.80 points；论文正文另以
  42.9→46.8 报 +3.9，是同模型 action-space comparison，二者 contract 不同。
- **Ablation / Generalization Evidence**：去掉 interleaved cold start 后 online RL 虽提高 accuracy，TIR 末期仅
  约 15%；去掉 path reward 后 20 steps 末有约 7-point gap，曲线在 8～11 steps 下跌。两项都是单次曲线、
  无 error bars。held-out Linux multi_apps 为 23.9，WindowsAgentArena 为 33.8（base 26.4），支持有限 transfer，
  不证明跨 arbitrary app/API/OS 的 generalization；training/eval 都围绕 OSWorld family，task/environment
  lineage 相关。
- **What It Proves / Does Not Prove**：作者证据支持 hybrid action exposure 本身可能使强模型退化，interleaved
  supervision 加 success-gated path reward 在 Qwen3-VL-8B/OSWorld contract 下改善 success/tool selection/
  steps trade-off。它不证明 synthetic tools 与可执行 APIs 等价，不证明 binary beneficial label 对每个 runtime
  state 都正确，也不证明 shorter path 更安全、成本更低或全局最优。reward 只在 success 后生效，失败路径的
  tool misuse/side-effect severity 没有由 `R_tool/R_length` 区分。
- **Trade-offs / New Failure Modes**：synthetic scaling 避免维护大量真实 APIs，却继承 source-GUI coverage、
  synthesis-model hallucination 和 next-state aliasing；composite tool 缩短路径，却扩大 blast radius、permission
  与 rollback cost。task-level tool-beneficial label 把 state-dependent decision 压成 binary prior；group-relative
  length 会随 sampled policies 改变且可能奖励少验证、少恢复的 brittle shortcut。真实 deployment 还会遇到
  schema drift、partial side effects、idempotency、secret/IAM、human approval 与 tool-result spoofing，论文 sandbox
  没有覆盖。
- **Evolution / ROADMAP / Decision**：`GUI-only policy → expose structured tools → path-selection confusion →
  synthetic interleaved supervision → critical-switch calibration → success-gated trajectory reward → online hybrid
  policy` 是 `Direct Evolution`；GUI 与 tools 按 coverage/risk 共存，不是后者替代前者。已读 Ch74 与 Ch73/75
  邻接，并核对 Ch29、Ch62、Ch68、Ch77。Ch74 已定义 typed intent/executor authority，却缺少 action-space
  expansion 本身需要 branch policy 的机制解释，故 provisional `Refine — Existing Argument` / Ch74，
  `Status: Experimental`；Ch29 owns group-relative/reward contract，Ch62 owns evidence，Ch68/77 owns permission/
  side-effect recovery。Historical Books Gate 关闭，不改 Books。
- **Open Questions**：需要公开 synthesis/training pipeline 与 frozen containers；真实 tool execution 对 synthetic
  next-state 的 mismatch rate；state-conditioned tool utility 而非 task binary label；failure-path safety/side-effect
  reward；multi-seed/statistical uncertainty；与 hierarchical/options/router policies 的 matched baseline；以及在
  schema drift、permission denial、partial success、human approval 和 latency/cost SLO 下的 policy behavior。

### EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents — 26/30

- **Candidate / Week / Source Family**：`EVA-VOICE-AGENT-E2E-EVALUATION`；W20；
  arXiv:2605.13841 v1，2026-05-13；v2 为 2026-05-27。W20 事件归属只依据 v1；v2 与当前 artifact
  用于核对 revision 后的完整机制、实验和限制，不把 5 月 27 日补充内容倒写为 v1 已公开事实。
- **Direct / Related Primary Sources**：arXiv metadata、v2 HTML/PDF、ServiceNow 官方 `eva` repository、
  project site 与 Hugging Face `ServiceNow-AI/eva` dataset。当前 repository 已有 metrics、validators、
  simulator、orchestrator、scenario data、tests 与 prompts；它证明公开实现 surface 存在，但当前 main 的
  1,371-commit state 不能证明每条路径在 v1 时已完全相同，也不能替代论文的 event-time evaluation。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、simulation/data design、
  EVA-A/EVA-X/diagnostic/aggregate metrics、12-system experiment、reliability/failure/perturbation analysis、
  Limitations、Conclusion，以及 Appendix A～R 的 architecture definitions、模型与 turn-detection 配置、
  compute/call contract、workflow/data pipeline、simulator validators、log merge、pipeline-specific metric
  adaptation、judge development/human agreement、threshold sensitivity、domain/perturbation tables、variance
  decomposition、trial-count analysis、scenario/transcript/judge prompts、license、annotations、ethics 与 future work；
  并核对 code/data 的目录职责、运行依赖、output artifacts 与 mock tool boundary。
- **Original Problem / Why Previous Design Was Reasonable**：component benchmark 分别测 STT、TTS、LLM
  或单轮 tool accuracy，便宜、确定且便于归因；text replay 在语音内容可完整转写、turn timing 不关键时也仍然
  合理。但 voice Agent 的真实 failure object 是多轮 audio interaction：错误实体可能只有一个字符、任务可在
  数据库终态上成功却沿途违反 policy，低平均 latency 也可能伴随 interruption、长沉默、重复提问或 spoken
  cognitive overload。更关键的是 bot-to-bot evaluator 自己会偏离 goal、错误结束或发生 infrastructure timeout，
  若不先审计 simulator，agent failure 与 evaluator failure 会被混在同一个分数里。
- **Changed Constraint / Principle**：当 evaluator 也是一个生成式、实时、有状态系统时，它不是透明 input
  generator，而是需要独立 identity、failure taxonomy 与 admission gate 的 participant。端到端评估还必须把
  `平均一次成功`、`多次尝试至少一次成功` 和 `同场景重复成功` 分开，不能用 peak capability 代替
  deployment reliability。Cascade、Hybrid 与 S2S 又暴露不同中间信号，所以 shared objective 不等于强行
  使用同一 log field；应按 architecture 选择可信 evidence，再在共同 outcome contract 上比较。
- **Mechanism**：每个 scenario 绑定 user goal、persona、decision tree、scenario database、expected final state
  与 deterministic tool executor；user simulator 与被测 voice agent 通过 live audio WebSocket 进行多轮交互。
  完成后的 run 先经过 `valid end → user behavioral fidelity → user speech fidelity` validation，失败时重生成，
  通过后才进入 scoring。processor 合并 audit log、framework events、simulator events 与三路 WAV，按
  Cascade/Hybrid/S2S 的可见信号构造 intended/transcribed turns、tool trace 与 timestamp。EVA-A 联合
  deterministic database outcome、policy/tool faithfulness 与 audio-level entity fidelity；EVA-X 联合 conversation
  progression、spoken conciseness 与 turn-taking。最后用 pass@1、pass@k、pass^k 分别报告平均、peak 与
  all-k reliability，并用 accent/noise 条件做受控 perturbation。
- **State Ownership / Control Flow / Data Flow**：dataset owner 持有 scenario specification、ground truth、
  policies 与 slice；simulator 持有 goal-following dialogue state；agent under test 持有会话、tool selection 与
  response state；mock tool executor 单独持有 scenario database transition；orchestrator 持有 run/retry、ports、
  provider/config snapshot；validator 持有 evaluator-admission verdict；metric engine 持有 log normalization、
  judge identity、threshold、per-run evidence 与 aggregate。数据流为 `scenario/config → live audio + tool side
  effects → raw logs/WAV/final DB → simulator validity gate → architecture-aware normalization → deterministic +
  model-based scorers → per-trial verdicts → uncertainty/reliability aggregation`。这使 simulator failure 不直接污染
  score，但 regeneration policy、retry count 与 excluded-run evidence 必须一起保存，不能把被过滤轨迹删除。
- **Implementation Details**：task completion 只比较 expected/final scenario DB，并把 authentication 作为独立
  gate，避免多条合法认证路径被 full hash 误罚；faithfulness 则审计 fabricated tool params、misrepresented
  result、policy violation、missing disambiguation 与 residual hallucination。S2S 没有可信 intended assistant text，
  Hybrid/S2S 又没有 agent-side user transcript，因此 processor 使用不同来源构造 trace。turn-taking 依据
  interruption class 选择 overlap、yield、recovery 或 piecewise latency function；diagnostics 保留 key-entity
  transcription、authentication、tool validity 与 latency，而不把所有 failure 平均进 composite score。
- **Evaluation Contract**：clean 条件覆盖 213 scenarios、每场景 `k=5`；三种 perturbations 使用固定的
  90-scenario subset、每条件 `k=3`。12 个 systems 包含 7 Cascade、2 Hybrid、3 S2S，并分别通过 native SDK、
  ElevenAgents 或 Pipecat 执行。每 system 的 nominal 样本数为 `213×5 + 90×3×3 = 1,875`；四个代表系统中
  24.1% trials 需重生成，使平均实际 simulation/judge calls 约增至 2,327。单次对话平均 4～5 分钟，user
  simulator、proprietary agent components 与 8 个 model-judge metrics 都引入 API 成本；论文没有给出统一
  hardware、precision、token/audio rate 或 dollar cost，因此不能从 call count 推导跨系统 compute efficiency。
- **Baselines / Judge Validation / Sensitivity**：论文比较已有 voice benchmarks 的 interaction、architecture、
  audio realism、simulator validation、metric 与 multi-trial coverage，而不是宣称一张 leaderboard 能隔离组件
  因果。judge prompts 先在 development data 上选模，再对每个 metric 使用 63 条 held-out、双 expert-linguist
  labels 核验；同时分解 scenario、model×scenario、trial 与 judge stochasticity，报告 trial variance 显著大于
  judge variance。`k=1..5` subsampling 支持 trial-count sensitivity；perturbation 在同一 90 scenarios 上用 paired
  sign-flip permutation 与 Holm–Bonferroni correction。它仍没有真人 caller matched control、live-tool baseline、
  prompt/turn-detector tuning ablation 或跨语言复现。
- **What the Evidence Proves / Does Not Prove**：在披露的 English enterprise、mock-tool、commercial-simulator
  contract 下，validator-gated bot-to-bot evaluation 能同时保留 outcome、policy path、audio fidelity、timing 与
  multi-trial consistency，并显示 peak/reliable 结论可能显著分离。它不证明 simulator 分布等于真实 caller，
  不证明 12 个 systems 的结果能概括三类 architecture，也不证明 pass^k 是真实线上连续成功率；该量依赖
  同场景有限样本的独立同分布近似、固定 threshold 和 evaluator version。作者结果更不能外推为当前模型排名。
- **Trade-offs / New Failure Modes**：simulator gate 降低 evaluator corruption，却引入 selection effect、额外调用
  成本和 retry policy；商业 simulator/version drift 使 benchmark identity 扩大。binary task completion 无 partial
  credit；LLM/LALM judge 仍有 style、same-family 与 audio-attention bias。PCM→μ-law、跨日志 timestamp drift、
  turn reconciliation 与默认 VAD 会改变 timing；declarative mock tools 不包含 live API latency、partial response、
  schema drift 或 partial side effects。English-only、较流畅的 synthetic caller 与缺少系统性 barge-in 会低估
  disfluency/interruption failure。真实 caller study、shadow/canary 与 component tests 因此仍与 bot-to-bot 共存。
- **Evolution / ROADMAP / Decision**：`component/static audio benchmark → live multi-turn simulator → simulator
  validity gate → architecture-aware evidence normalization → outcome+path+audio+timing scoring → multi-trial
  peak/reliability split → controlled perturbation → production/human calibration` 是 `Direct Evolution`。已读 Ch62
  及 Ch61/63 邻接，并核对 Ch65 trace interface。Ch62 已覆盖完整 subject identity、trajectory/outcome evidence、
  executable verifier、judge audit、uncertainty 和 `pass@k` candidate-coverage boundary；缺口是把生成式 evaluator
  本身建模为先验 validation-gated subject，以及显式区分 `pass@1/pass@k/pass^k`。故 provisional
  `Refine — Existing Argument` / Ch62，`Status: Experimental`；Ch63/65 只承接 runtime signals 与 raw trace。
  Historical Books Gate 关闭，不改 Books。
- **Open Questions**：需要 human-caller matched study 与 sim-to-real error bounds；保存 rejected/retried runs 后如何
  估计 validator selection bias；pass^k 在非独立 trial、provider drift 与 threshold sensitivity 下如何校准；
  interruption-rich、multi-language、live API/partial-side-effect suites；judge family leakage、prompt injection 与
  abstention；以及用 production SLO/cost/recovery contract 比较相同 architecture 的 tuning，而非只比较 defaults。

### EvolveMem: Self-Evolving Memory Architecture via AutoResearch for LLM Agents — 26/30

- **Candidate / Week / Source Family**：`EVOLVEMEM-RETRIEVAL-POLICY-AUTORESEARCH`；W20；
  arXiv:2605.13941 v1，2026-05-13，当前无后续 arXiv revision。它是 W14 Omni-SimpleMem/SimpleMem
  family 的 5 月 retrieval-policy extension，不回写为 W14 已公开机制。
- **Direct / Related Primary Sources**：唯一 v1 HTML/PDF、作者 `aiming-lab/SimpleMem` repository 的
  `EvolveMem/` implementation/README，以及 current package 的 `simplemem.optimize(...)` surface。当前 main
  已出现 policy store、promotion、replay、self-upgrade 等更多模块，属于访问日 implementation state；没有
  event-time tag 证明它们全部对应论文 v1，故只用来确认 artifact 可定位，不把当前功能倒写进论文机制。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、typed store/extraction/
  consolidation、multi-view retrieval/action space、diagnosis/meta-analyzer、完整 experiments、trajectory、transfer、
  ablation、Conclusion，以及 Appendix A～F 的公式、safe ranges、pseudocode、case trace、SQLite schema、
  embedding、efficiency/storage、compute/data/hyperparameters 与全部 prompts；并核对 official quick start、
  benchmark entrypoints、current optimize wrapper 与 repository version drift。论文无独立 Limitations section。
- **Original Problem / Why Previous Design Was Reasonable**：固定 BM25/dense/top-k/fusion/context budget 在
  memory store 小、query distribution 稳定、SLO 要求可预测时 state 最少、容易复现，也便于人工审计。已有
  memory 系统优先演化 content、summary、graph、consolidation 与 forgetting，是因为事实正确性和 lifecycle
  比自动调参更基础。但当 store 从少量同质 records 变为跨 session 的异质历史，factual、temporal、multi-hop、
  aggregation 与 adversarial name-swap query 对 lexical/semantic/structured evidence 的需要不同，单一 frozen
  retrieval policy 会在某些类别持续 miss 或污染 Context。
- **Changed Constraint / Principle**：memory facts `K` 与 retrieval configuration `theta` 的 truth authority 不同。
  Facts 需要 provenance、authorization、correction 与 deletion；retrieval policy 只是基于某 evaluation distribution
  选择 facts 的 derived control state。后者可以演化，但必须有 identity、evaluation set/scorer、proposal、
  accepted/rejected lineage、bounded action space、rollback 和 promotion boundary。内容覆盖缺失与排序参数错误
  还必须分开诊断：retrieval tuning 不能从 store 中创造不存在的 evidence。
- **Mechanism**：LLM extractor 以 overlapping windows 生成六类 typed memory，使用 retry、context overflow
  chunk-split 与 keyword-coverage re-extraction；store 再做 exact/near dedup、importance decay 与 entity
  reinforcement。读取时 BM25、BGE semantic 与 structured metadata 各自产生 candidates，由 sum、weighted-sum
  或 RRF 融合，再叠加 importance、recency 与 reinforcement；entity-swap、query decomposition、answer style、
  second-pass verification 与 per-category overrides 共同组成 `theta`。每轮在 QA/reference 上执行、写入 question/
  prediction/reference/score/retrieved sources，diagnosis LLM 输出结构化 delta；meta-analyzer 在 regression 时回到
  best-so-far，在连续 stagnation 时随机探索，否则 clamp 后应用 proposal，最终返回历史最佳 config。
- **State Ownership / Control Flow / Data Flow**：memory store 持有 versioned facts、scope、type、entities、
  importance/confidence、supersession 与 append-only mutation events；retriever 持有 index/view identity、candidate
  sets 与 active `theta`；evaluator 持有 QA split、ground truth、metric、raw results 和 run config；diagnosis LLM
  只提出候选 delta，不拥有 production promotion；meta-analyzer 持有 revert/explore/apply decision 与 best-so-far
  pointer。流向为 `sessions → extracted K → retrieve/answer(theta_r) → per-question evidence → diagnosis proposal →
  guarded evaluation → accept/revert/explore → immutable theta_(r+1)`。若 diagnosis 发现 coverage gap，可 targeted
  re-extract 并改变 `K`；此时只回滚 `theta` 不能自动回滚 derived store/index，二者必须分开记录和恢复。
- **Implementation Details**：paper contract 使用 SQLite 3.35+/FTS5 schema v6、WAL、UUID memory ids、
  `memory_events` audit log、typed links 与 schema migration；实验 embedding 为 BAAI/bge-base-en-v1.5 768-dim。
  初始 config 是 BM25-only、keyword top-5、context memory budget 8，semantic/structured/entity-swap/query
  decomposition 关闭；最多 7 rounds，默认 convergence epsilon 0.5 pp。所有 config snapshots、raw_results、
  summaries、best config 与 extracted cache 持久化。论文所谓“发现新维度”应解释为 diagnosis 驱动启用/形成
  query decomposition、entity-swap 与 verification configuration；公开 artifact 已包含相应可执行组件，不能据此
  推断 LLM 能无边界地生成、验证并安全部署任意新代码。
- **Evaluation Contract**：LoCoMo-10 为 10 conversations、每个 19～32 sessions/369～689 turns，共 1,986
  QA、五类问题，报告 token-F1/BLEU-1；MemBench 只取 28 samples（7 categories×2 topics×2），报告 MCQ exact
  match。比较 GPT-4o/GPT-5.1 两个 backbones；extraction/diagnosis 使用 Azure GPT-5.1，answer generation 说明
  为 GPT-4o。memory system 在单台 Apple M-series CPU 上运行，无 GPU；单个 LoCoMo sample、约 900 memories/
  200 QA 的 7-round evolution 为 25～35 分钟，主成本是每轮约 15～20 分钟 QA LLM calls，diagnosis 约 15 秒。
  约 900 memories 的 index build 约 5 秒、retrieval 平均 15 ms、verification 新增约 2～3 秒 LLM call；均无
  p95/p99、并发、API token/cost、network/retry 或 production SLO contract，不能外推为 serving latency。
- **Baselines / Ablations / Transfer**：LoCoMo 比较 MemVerse、Mem0、Claude-Mem、A-MEM、MemGPT、
  SimpleMem；MemBench 比较 RecentMemory、MemGPT、MemoryBank、SCMemory。trajectory 从 30.5 F1 到 54.3，
  R2 的 MMR regression 被回退。Ablation 中 extraction quality guards 的 drop 为 23.22 F1，semantic search
  10.32，diagnosis-vs-random 9.63；移除名为 self-evolution 的 component 只 drop 2.03，三个 discovered
  dimensions 合计 7.77。LoCoMo config zero-shot 到 MemBench、再继续 evolution 的表支持两个 benchmark 间
  正向迁移，但没有 independent benchmark family、matched Bayesian/AutoML/human tuner、multi-seed/error bars
  或 statistical tests；paper objective 用 QA ground truth 直接优化 config，正文没有清楚分离 evolution/dev set
  与最终主结果 test set，repository 虽称 held-out QA，不能替代论文缺失的 split lineage。
- **What the Evidence Proves / Does Not Prove**：作者实验支持“把 per-question failure evidence 反馈给 bounded
  retrieval config，并以 best-so-far/revert guard 管理 proposal”在两个给定 benchmarks 上可执行；也支持
  content coverage、candidate retrieval 与 answer policy 需分别诊断。它不证明发现了跨真实 workload 的 universal
  retrieval principles，不证明 LLM diagnosis 优于同预算 expert/Bayesian search，也不证明 loop 可在线面对 user
  drift、无 ground truth、continuous writes 或 production side effects。`78.0%` 相对 deliberately minimal R0，
  `25.7%` 才是 GPT-4o LoCoMo 相对 strongest baseline；两者不能混写。
- **Limitations / Trade-offs / New Failure Modes**：论文没有独立 limitations。用同一 benchmark feedback 搜索并
  报告 best round 会产生 adaptive overfitting/selection bias；category-specific override 可能成为 benchmark patch，
  scorer 或 backbone 变化又使 `theta` stale。LLM diagnosis 降低组合搜索成本，却增加 prompt/model drift、错误
  causal attribution 与 proposal non-determinism；random exploration 消耗完整 evaluation pass。Targeted re-extraction
  能修 coverage，却可能重复、污染或改变事实 store，单纯 config rollback 不足。论文未评估 permission/tenant
  isolation、conflict/correction、deletion propagation、poisoning、concurrent writes、crash consistency、shadow/
  canary 或 online regret。固定人工 config 在高风险/低反馈/严格 latency 场景，manual review 在 scorer 不可信时，
  grid/Bayesian search 在低维数值空间，仍是合理共存分支。
- **Evolution / ROADMAP / Decision**：`fixed retrieval parameters → explicit versioned retrieval-policy state →
  failure-level evidence → bounded proposal → evaluate/revert/explore → separately promoted policy revision →
  production drift monitoring` 是 `Direct Evolution`；与 W14 Omni-SimpleMem 的 evidence tiering 为
  `Layering / Dependency`。已读 Ch73 与 Ch72/74 邻接，并核对 Ch62/77。Ch73 已明确 raw facts 与 learned
  retrieval-policy state 必须分离并版本化，也覆盖 consolidation、deletion、drift 与 fallback；缺口是 policy revision
  的 guarded change-control loop，故 provisional `Refine — Existing Argument` / Ch73，`Status: Experimental`。
  Ch62 owns evaluation/split/scorer，Ch77 owns approval/promotion workflow；Historical Books Gate 关闭，不改 Books。
- **Open Questions**：需要独立 dev/test/production split 与 adaptive-overfitting accounting；matched expert、random、
  Bayesian/search budget；multi-seed proposal variance；scorer/backbone/index drift 后的 invalidation；K 与 theta 的
  atomic snapshot/replay/rollback；targeted re-extraction 的 provenance/delete propagation；poisoning/ACL guard；
  以及无 ground truth 的 online monitoring、human approval、canary 与 rollback SLO。

### MemLens — 27/30 — Full Review Complete

- **Candidate / Week / Source Family**：`MEMLENS-MULTIMODAL-MEMORY-EVAL-CONTRACT`；W20；
  arXiv:2605.14906 v1，2026-05-14，访问日 2026-08-11。arXiv 当前只有 v1；无 HTML，故以 63 页
  PDF 为全文依据。作者 GitHub、memory-agent reproduction notes 与 Hugging Face dataset card 为当前
  artifact surface；它们用于核验实现和数据 schema，不被倒写成 5 月 14 日全部已经冻结的事实。
- **Direct / Related Primary Sources**：arXiv metadata/PDF；作者 `xrenaf/MEMLENS` evaluation repository；
  `memory-agent/` 适配说明；`xiyuRenBill/MEMLENS` dataset card。论文声称 code/dataset 以 frozen tags
  发布，但 GitHub 页面未提供可核验 release，current main 只有当前 commit history；因此复现时仍需记录
  exact commit 与 dataset revision，不能只保存 repository URL。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、五类 ability taxonomy、
  四阶段数据构造、cross-modal dependency、三轮 quality gate、完整 evaluation setup/results/error analysis、
  Conclusion、Reproducibility/Ethics，以及 Appendix A～I 中 model/adapter roster、judge protocol、数据与
  prompt 生成、human agreement、195-item agent subset、retrieval attribution、oracle retrieval、session
  indistinguishability 与 detailed limitations。Artifact 侧核对了 multi-session message assembly、LLM judge 的
  500-word auto-zero/JSONL resume、七类 agent 的输入转换、retrieval top-k、prompt budget、image handling
  与 dataset question/evidence/image provenance schema。
- **Original Problem / Why Previous Designs Were Reasonable**：full Context 保留原始 interleaved pixels，
  在 history 尚短且窗口可承受时最大化 fidelity；external memory 通过 caption、embedding、session index 或
  recurrent chunks 缩小 Context，在长历史与重复查询下节省 read-time budget。两者分别优化 evidence fidelity
  与 bounded retrieval，旧方案并非错误。旧 benchmark 要么只测长文档/needle，要么只测 text memory；当
  interaction 变成跨 session 的 image+text history 时，单一 aggregate accuracy 无法区分 evidence 是否从未被
  保存、没有被召回、召回后没有被读懂，或因 evidence 缺失却没有拒答。
- **Changed Constraint / Mechanism**：MemLens 把同一 789 个问题实例化为 32K/64K/128K/256K 四档 history，
  覆盖 IE、MSR、TR、KU 与 AR。构造链为 `topic/image → multimodal session → visually anchored QA →
  evidence session → timestamped haystack assembly`；通过 entity abstraction 让文本不直接泄露 image identity，
  再用 rule/LLM filtering、三轮人工审阅与 image removal ablation 建立 cross-modal necessity。65.7% 为
  image-essential、14.7% 为 image-supportive、19.6% 为 text-sufficient；对前两类 634 个问题移除 evidence
  images 后，两个 frontier LVLM 的 accuracy 均低于 2%。history 长度采用 MMLongBench proxy accounting，
  约按每张图 2,000 tokens，并维持固定 text/image ratio；这不是各模型 native tokenizer/vision encoder 的
  实际 token 或 FLOP 等价。
- **State Ownership / Control and Data Flow**：dataset builder 拥有 question/evidence session identity、
  timestamps、image provenance 与 frozen split；benchmark adapter 决定 raw pixels、captions、composite
  session images 或 embeddings 怎样进入 candidate system；memory pipeline 拥有 write representation、index、
  retrieval 与 packed answer context；backbone 只消费 answer-time representation；judge 拥有 binary verdict。
  因而可审计链应写成：

  ```text
  original multimodal session
  -> benchmark adapter / write-time representation
  -> stored memory + index
  -> retrieved sessions / representations
  -> answer-time evidence
  -> backbone output
  -> judge verdict
  ```

  如果只记录 model name 或最终 accuracy，就会把 adapter compression、retrieval miss、reader failure 与 judge
  error 错误归因给同一个组件。
- **Implementation Details**：direct LVLM 接收原始 interleaved messages。四个 text-only agents 只接收
  BLIP-2 captions；M3-Agent 把每个 session 渲染为 composite image，再生成 textual memories；M3C 报告路径
  使用 text-only session encoding、top-3 retrieval 与 12,000-character QA context；Mem0 每题新建 FAISS store、
  top-20；Memory-T1 用 BM25 top-10 与 temporal filter；M2A 保留 image path/URL 并使用 text/image embedding
  services；MemAgent-7B 用 5,000-token recurrent chunks。论文主动承认这些 input-format adapters 不同，且
  direct LVLM 能回看原始 pixels，而多数 memory agents 不能；这项 protocol asymmetry 是被评系统的一部分，
  也是比较结论的必要条件，不是可忽略的实现细节。
- **Evaluation Contract / Baselines / Ablations / Sensitivity**：27 个 LVLM 在 full 789 questions 上跑
  32K/64K/128K；7 个 agents 因 M2A 每题约慢 60 倍，只在 seed=42 的 stratified 195-question subset 上跑
  32K～256K。作者另把 representative direct LVLM 重算在同一 195 subset，报告 32K ranking transfer
  Spearman `ρ=0.94`，但这不能消除 input-adapter、backbone、post-training 与 compute 不匹配。Open-weight
  LVLM 在 context `>=128K` 时使用 vLLM 0.17～0.18、8×A100-80GB、tensor parallel；precision、完整 batch/
  concurrency、per-model wall time、memory-agent hardware、p95/p99、SLO 与等预算 token/FLOP contract 未统一
  披露。总 API/构造 cost 约 4,500 USD。主要 judge 为 Qwen3-VL-235B-A22B-Instruct；73,784 次 judge calls
  中 800 次由 GPT-5.4-mini 复判（κ=0.93），484 条由三人 consensus 验证（κ=0.86），但没有独立报告三位
  annotators 之间的 κ，且 false positive 29、false negative 2 暴露 leniency。Oracle-evidence ablation 让
  MSR 在 GPT-5.4/Gemini-3.1-Pro 上达到 100%/90.21%，支持主要瓶颈位于 evidence location；三类有 retrieval
  log 的 agents 又显示 M3C 主要 retrieval-failure，而 Mem0/Memory-T1 多为 post-retrieval comprehension failure。
- **What the Evidence Proves**：在这一 synthetic、length-controlled、visually anchored benchmark 中，
  raw-context LVLM 随 filler 增长更易丢 evidence，而当前 memory pipelines 在长度上较平却常在 write-time
  compression 或 retrieval/read path 损失 fine-grained visual evidence；memory ability 不能由一个 aggregate
  score 代表。更重要的长期结论是：memory evaluation 必须同时测 source-evidence fidelity、write/read
  representation、retrieval recall、post-retrieval comprehension、knowledge supersession 与 calibrated abstention；
  oracle retrieval 和 representation ablation 是定位 fault layer 的工具。
- **What It Does Not Prove**：论文没有实现或评估所建议的 hybrid architecture，因此不能声称 long Context
  加 structured multimodal retrieval 已经优于两条旧路线。它也不证明所有 memory agent 都劣于 direct
  attention：agent 只跑 195 items，backbone 多为 sub-10B，输入 adapter 与 task-specific post-training 不同，
  且只有 M2A 提供相对干净的 same-backbone contrast。caption removal result 证明 benchmark 对 images 敏感，
  不等于生产图片、视频、语音或真实用户 history 的泛化；`32K～256K` 是统一 proxy length，不是各模型相同
  native multimodal compute。观察到 RL/LoRA agents 的低 AR 也只是相关证据，不能从非随机、异构 systems
  断言 post-training 普遍破坏 abstention。
- **Limitations / Threats / New Failure Modes**：全部 conversations 为 GPT-5.1/Gemini-3-Pro synthetic，
  ShareGPT/UltraChat 只提供 filler；Gemini-3 family 同时参与 generation 与 leaderboard，独立 generator
  counterfactual 未做。judge 人工覆盖约 1.08%，存在 systematic leniency；agent subset 从 200 个候选与
  available runs 交集后剩 195，也引入 availability conditioning。static frozen histories 不测 write/query
  causality、irreversible update、online forgetting、concurrent writes 或 deletion。第三方 web images 保留原站
  license，takedown 会改变可重放资产；current GitHub/HF surface 与 event-time freeze 仍需 commit/tag binding。
  Hybrid path 还会新增 raw-media storage/ACL/retention、dual-index consistency、representation invalidation、
  retrieval latency、Context packing、duplicate evidence、modality-specific authorization 与 fallback failure。
- **Where Previous Designs Still Apply / Evolution**：短 history、低 miss tolerance 或高风险原始证据仍可保留
  full Context；可接受 lossy summary、查询频繁或 strict Context budget 时，caption/embedding/session memory
  仍是合理分支；exact artifact reference 适合已知未来会回读的高价值 media，semantic/hybrid retrieval 负责
  未知关联。`full multimodal Context → lossy external memory → provenance-preserving multimodal store +
  coarse retrieval → authorized raw-evidence dereference → bounded Context packing → retrieval/reader/abstention
  joint evaluation` 是 `Direct Evolution`；与 Ch73 的 compact control state/exact evidence archive 为
  `Layering / Dependency`，而不是新路线替代旧路线。
- **ROADMAP / Adjacent Chapters / Decision**：已读 Ch62 及 Ch72/73，并核对 Ch17、Ch22/23。Ch73 已拥有
  memory write/read、exact evidence archive、retrieval/downstream/cost/deletion 指标；Ch72 已拥有 retrieval miss
  与 generation failure 分层；Ch62 已拥有 complete subject identity、dataset/scorer/version 与 uncertainty。
  真正缺口是把 `write-time/answer-time representation`、adapter asymmetry 和 oracle-evidence diagnosis 明确
  纳入 evaluation subject/claim boundary，故 provisional `Refine — Existing Argument` / Ch62，
  `Status: Experimental`；Ch73 只保留 multimodal evidence fidelity handoff。Historical Books Gate 关闭，
  本检查点不修改 Books。
- **Open Questions**：需要 matched backbone、matched raw-pixel access、matched compute/latency 的 long-context/
  memory/hybrid comparison；real-user streaming writes 与 deletion/correction；per-modality ACL/retention；native
  token/FLOP accounting；independent generator、完整 inter-annotator reliability、multi-seed subset sensitivity；
  hybrid store 的 raw media/version/index atomicity、retrieval recall 与 tail-latency SLO；以及将 retrieval failure、
  visual reading failure、aggregation failure和 abstention failure 分别接入 release gate。

### MemEye — 25/30 — Full Review Complete

- **Candidate / Week / Source Family**：`MEMEYE-VISUAL-MEMORY-GRANULARITY-TEMPORAL-AUTHORITY`；W20；
  arXiv:2605.15128 v1，first-public 2026-05-14，访问日 2026-08-11。arXiv 当前只有 v1；官方 HTML
  为全文依据，GitHub、project page 与 Hugging Face dataset 为 current artifact surface。repository 无 release，
  因而未来复现必须固定 commit 与 dataset revision，不能只保存 mutable `main` URL。
- **Direct / Related Primary Sources**：arXiv metadata/HTML、作者 `MinghoKwok/MemEye` repository、project
  page 与 `MemEyeBench/MemEye` dataset。repo 提供 runner、model/method/task configs、per-question predictions、
  X/Y slice metrics 与 locked judge path；部分 baseline 使用作者按论文重实现或外部 runtime adapter，故
  “supported” 不等于所有方法均为作者原始 artifact 的 bitwise reproduction。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、二维 taxonomy、八类 task/
  数据构造与三项 validation gate、13 个 memory methods/4 个 backbones 的 implementation contract、全部主表、
  visual-caption paired analysis、judge/human/bootstrap checks、oracle/recency/cross-topic ablations、evolving-state
  probes、case studies、Limitations/Broader Impacts，以及 Appendix 中 method hyperparameters、prompts、完整
  per-model matrix 与 artifact instructions。PDF 约 41 MB 未通过当前抓取通道下载，但官方 942-line HTML
  正文完整可读；因此不是 blocked source，也不把没有运行 artifact 误写成复现。
- **Original Problem / Why Previous Designs Were Reasonable**：把多模态 history 压成 caption，可复用成熟 text
  retrieval、降低 storage/context 成本并改善可搜索性；直接保留 raw images，则避免 caption 提前丢失像素级、
  instance-level 或相对位置证据。相似度 top-k 在状态基本静态时也合理，因为 relevance 常近似 answerability。
  约束变为跨 session 的视觉状态持续变化后，系统不仅要找“相关对象”，还要判断哪份 observation 具有当前
  temporal authority；旧图可能语义上最相关、数量更多，却已经失效。
- **Changed Constraint / Evaluation Principle**：MemEye 把诊断空间拆成两条正交轴：X1 scene、X2 region、
  X3 instance、X4 pixel 表示视觉证据粒度；Y1 atomic retrieval、Y2 relational association、Y3 evolutionary
  synthesis 表示 memory reasoning depth。371 个 mirrored MCQ/open questions 来自 221 sessions、848 dialogue
  rounds、438 images 与八类生活场景。这个矩阵的价值不是形成一张总榜，而是区分 representation fidelity、
  retrieval、跨证据关联与 state-resolution failure。
- **Dataset Construction / Quality Gates**：GPT-5.2 按 X/Y 候选生成，之后人工复核与 adjudication。三道 gate
  分别检查 text leakage、minimal-caption bypass 与 oracle raw-visual evidence answerability，并审计 taxonomy
  structure。100-item taxonomy sample 由 GPT-5.4 与 Gemini-2.5-Pro 复标，报告 `kappa_X=0.66`、
  `kappa_Y=0.63`；复标模型没有看到 images，所以只支持问题文本下 taxonomy 的可重复性，不能证明 visual
  evidence annotation 已独立验证。全部 371 条经过 human adjudication，但论文未给多位人工标注者一致性。
- **State Ownership / Control and Data Flow**：source session 拥有 raw image、turn/date、object identity 与
  observation order；captioner 或 visual encoder 生成 write-time representation；memory method 拥有 index、
  summary、retrieval score 与 top-k；answer backbone 只看 retrieved representation；evaluator 拥有 X/Y label、
  oracle clues、answer、choice rotation 与 judge revision。完整流向应记录为 `raw observation → caption/embedding/
  pointer → indexed state → relevance retrieval → temporal-authority resolution → bounded answer Context → scorer`。
  若 update/supersession 状态只隐含在 similarity score 中，stale evidence 会被静默当成当前事实。
- **Implementation Contract**：文本 methods 使用 GPT-5.2 dense captions；多模态 methods 在支持时保留 native
  images。FC 的 window 为 128K，超限 FIFO；SRAG top-k=10，文本 encoder 为 `all-MiniLM-L6-v2`，视觉
  encoder 为 `siglip2-base-patch16-384`，text/image similarity 等权；Reflexion recalled context 约 6000 words；
  Generative Agents top-k=10、decay 0.995、4000-word context、reflection threshold 8；MemoryOS 的 short/mid/
  long capacities 为 10/2000/100；M2A 最多 15 次 memory-manager 与 5 次 query iterations。SimpleMem(V)
  保存 raw pointers 并在 answer-time 解引用图片。不同方法拥有不同 encoder、compression、iteration 与 Context
  budget，因此主表是 system-level comparison，不是 encoder-controlled component ablation。
- **Evaluation Contract**：13 methods 横跨 Qwen3-VL-8B-Instruct、gpt-4.1-nano、gpt-5.4-mini 与
  Gemini-2.5-flash-lite；temperature=0。主 gpt-5.4-mini open-ended max output 128，judge 为 GPT-5.2；MCQ
  exact match 对四个 choice rotations 求均值。open-ended judge 在 72 个 predictions 上抽查，1 个 borderline
  被排除后为 69/71 agreement、`kappa=0.94`；只含一位 human annotator、两种 methods 与一个 backbone，
  不能外推为全矩阵 judge reliability。10,000 次 question-level bootstrap、seed 20260430 只表达题目采样
  uncertainty，不覆盖 judge、prompt、method implementation 或 model revision uncertainty。硬件、API revision、
  token/cost、latency、concurrency 与 production SLO 未统一披露。
- **Visual-vs-Caption Evidence and Counterfactual**：在作者主 paired analysis 中，high-X 的 visual-caption
  Judge 差为 `+0.079 [0.042, 0.115]`，EM 为 `+0.075 [0.043, 0.107]`；low-X intervals 跨 0。可是更强、
  task-aware GPT-5.4-mini captions 在 120-item subset 上把 SRAG high-X caption score 从 0.235 提到 0.387，
  visual gap 从 0.194 缩到 0.041；X4 gap 从 0.215 缩到 0.094，且 caption 长度约增加 2～3 倍。证据因此
  支持“caption policy、detail budget 与 query alignment 决定 representation loss”，而不是“raw image 永远
  优于 text memory”。残余 high-X gap 仍提示 fine-grained evidence 值得保留，但需 matched compute/cost study。
- **Temporal Authority / Oracle Evidence**：Y3 evolving-state subset 的 stale-only/latest-only/all-clue oracle
  judge scores 为 0.591/0.712/0.727，而 FC(V)、SRAG(V)、MMA、M2A 只有 0.333/0.379/0.394/0.182。
  case studies 覆盖 stale-majority、object migration、trigger-state miss 与 full-trajectory interpretation，说明
  relevance retrieval 与 state validity 是两个阶段。SRAG(V) 的 recency adjustment 可降低 stale dominance 与
  rank inversion，但 answer-quality confidence intervals 跨 0，而且 latest evidence 未进入 candidate set 时无法
  恢复。这支持显式 `valid_from/valid_to`、supersession link 与 evidence chain；不支持把 recency 当通用修复。
- **Cross-topic / Method Evidence**：保持 answer evidence 与 questions 不变、把 history 从 1 个扩到 2/4 个
  domains 后，Full Context 更易受干扰或 truncation；retrieval/structured memory 相对更平，但绝对分数并不都高。
  在主 gpt-5.4-mini matrix 中 SRAG(V) aggregate open-ended judge 0.4937、MCQ EM 0.6177；这些数字绑定
  当前 methods/backbone/config，不能形成 universal ranking。A-Mem 在部分 Y3 case 通过 compact textual state
  chain 胜过 raw-image retrieval，也说明“保真”与“状态解析”是不同需求，保留 pixels 本身不产生 world model。
- **What the Evidence Proves / Does Not Prove**：证据支持用 `visual granularity × memory reasoning depth` 的
  slice matrix 定位 multimodal memory failures，也支持把 semantic relevance 与 temporal authority 分开评估。
  它不证明任何 memory architecture 普遍最优、不证明 raw pixels 必须替代 captions、不证明当前 13 个
  implementations compute-matched，也不证明 Y3 分数等于真实用户长期 memory reliability。数据为作者构造、
  scenarios/model panel/caption pipeline/human sample 有限；method-specific encoders 与 reimplementations 影响比较。
- **Trade-offs / New Failure Modes / Previous Designs**：raw media 提高证据可回查性，却增加 storage、ACL、
  consent、retention、deletion、decode 与 Context 成本；task-aware captions 降低读取成本，却把未来未知 query
  所需细节提前交给 writer 猜测。短 history、低敏感度或查询稳定时 caption/RAG 仍合理；高风险、细粒度或
  未来 query 不可预测时宜保留受控 raw evidence pointer；频繁更新的实体还需独立 state-resolution layer。
  新 failure modes 包括 stale-majority、rank inversion、missed trigger、identity drift、caption hallucination、
  raw-pointer authorization failure、deleted source 残留 embedding 与 judge/model revision drift。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`caption-only searchable memory → native multimodal
  retrieval → evidence-granularity slices → temporal-authority diagnosis → provenance-preserving source pointer +
  explicit supersession/state resolution → representation/retrieval/reader joint release gate` 是 `Direct Evolution`
  与 `Layering / Dependency` 的组合。已读 Ch62 及 Ch72/73 邻接。Ch73 已覆盖 raw evidence archive、
  supersession、delete/rollback 与 retrieval/downstream/cost metrics；Ch72 已区分 retrieval miss 与 generation
  failure；Ch62 已拥有 evaluation subject、slice、oracle、judge audit 与 uncertainty。新增的稳定价值是把 X/Y
  diagnostic matrix、caption-strength counterfactual 与 temporal-authority oracle 纳入 evaluation design，故主
  owner 为 Ch62，provisional `Refine — Existing Argument`，`Status: Experimental`；Ch73 只作“相关性不等于
  当前有效性”的短 handoff。Historical Books Gate 关闭，本检查点不修改 Books。
- **Open Questions**：需要 human-authored/real-user streaming histories、matched encoder/backbone/compute/
  storage/latency、multi-seed method runs、完整 judge/inter-annotator audit、caption rate-distortion curve、
  streaming write/read/deletion tests、identity and supersession ground truth，以及把 retrieval recall、temporal
  validity、visual reading、aggregation、abstention、privacy/ACL 与 cost/SLO 分别接入 release gate。

### Anti-Self-Distillation for Reasoning RL via Pointwise Mutual Information — 26/30 — Full Review Complete

- **Candidate / Week / Source Family**：`ANTISD-PRIVILEGED-CONTEXT-PMI-TOKEN-CREDIT`；W20；
  arXiv:2605.11609 v1，first-public 2026-05-12，访问日 2026-08-11；当前无后续 arXiv revision。
  作者 `FloyedShen/AntiSD` repository 是 current artifact，未提供 release/tag，不能据 mutable main 反推
  event-day code state。
- **Direct / Related Primary Sources**：arXiv metadata/完整 HTML/PDF、作者 repository、AntiSD recipe、data
  preparation、veRL fork 与 core `grpo_ca` implementation path。repo 提供 Qwen3-4B/8B、Olmo3-Instruct/
  Think 的十二个 scripts；论文还报告 Qwen3-30B-A3B，但 current recipe 不含其公开复现脚本，故 30B
  结果只有论文级证据。未运行 8×H20 或 multi-node experiments，不宣称独立复现。
- **Full-read Coverage**：已覆盖 Abstract、Introduction、Preliminaries、reverse-KL gradient 与 conditional-PMI
  derivation、JSD shape、entropy gate、五模型 math 主表、code probe、training dynamics、all component/
  continual ablations、Related Work、Conclusion、Appendix A 全部 proofs、B hyperparameters/algorithm、C
  teacher templates、D sensitivity 与 E limitations；artifact 侧核对 data/model/method scripts、loss sign、
  warmup/calibration knobs、context/length settings 与公开结果/实现覆盖差异。
- **Original Problem / Why Previous Design Was Reasonable**：outcome-only GRPO 把 terminal reward 广播到
  全 trajectory，token credit 粗且在 all-equal groups 中无信号。On-policy self-distillation 让 student 生成
  trajectory，再用同一模型在 verified solution/environment feedback 等 privileged context 下作为 teacher，
  在 student 实际 prefix 上提供 dense token distribution；当目标是行为压缩、format consistency 或 teacher
  context 确实表达目标 policy 时，下降 teacher/student divergence 是合理的旧方案。约束变为 hard reasoning
  search 后，answer-aware teacher 已经“知道终点”，其 confidence change 不一定代表哪个 token 促进探索。
- **Mechanism Diagnosis**：设 student/teacher 对实际 token 的 log-prob 为 `s_t`、`t_t`，则
  `u_t=t_t-s_t=log pi(y_t|x,c,y_<t)/pi(y_t|x,y_<t>)`；在共享参数与 stop-gradient teacher contract 下，
  它等于 token 与 privileged context `c` 的 conditional PMI。标准 reverse-KL self-distillation descent 的
  policy-gradient contribution 为 `+u_t`：teacher 已知解答后更确信的 shortcut/template token 得正 credit，
  teacher 因已收敛到某解而降低的 `Wait/Maybe/Alternatively` 等 deliberation token 得负 credit。这里证明的是
  log-ratio 信号的局部结构，不是这些词本身具有跨任务固定因果作用；token labels 来自作者 trace 分析。
- **AntiSD Objective / Gate**：AntiSD 反转方向，最大化 JSD，并使用
  `A_t^AntiSD=-0.5*(softplus(u_t)-log 2)`。该 shape 在 `u<0` 的 deliberation side 将正 advantage 上界设为
  `0.5 log 2`，抑制 on-policy sampling 下的 heavy negative tail；`u>0` shortcut side 的 penalty 仍随 `u`
  增长。最终 token advantage 为 sequence-level GRPO advantage 加该 gated term。batch median teacher
  entropy 经 5-step、lambda=0 warmup 得 `H_warm`，跌破 `0.93 H_warm` 时关闭，恢复到 `H_warm` 时重开，
  形成 hysteresis。因为 divergence ascent 不会自行收敛到 teacher，gate 是 signal-validity controller，
  不是普通 schedule annotation。
- **State Ownership / Control and Data Flow**：rollout policy 拥有 student trajectories/logprobs；verifier 与
  rollout group/dataset 共同提供 correctness、verified solution 或 test fraction；privileged-context builder
  拥有 `c` 的来源、版本与 fallback；同一 actor 的 stop-gradient teacher forward 产生 teacher logprobs/
  entropy；gate controller 拥有 warmup statistics、on/off state 与 thresholds；optimizer 拥有 GRPO+AntiSD
  combined advantage。数据流为 `student rollout → verifier/group select trusted context → same-prefix teacher
  forward with c → token log-ratio/PMI proxy → bounded sign-reversed shaping → entropy gate → clipped policy
  update`。恢复 checkpoint 若遗漏 gate state、warm baseline、context provenance 或 verifier revision，会静默
  改变 objective。
- **Mathematical Evidence Boundary**：Appendix 证明线性 `sum_t u_t` telescope 为 sequence-level PMI，并可
  解释为 potential increments；但实际 AntiSD 使用 nonlinear `-phi(u_t)`，其逐 token 和一般不会 telescope。
  因此 potential-based optimal-policy invariance 不能未经额外证明直接赋给完整 AntiSD objective。另一个边界
  是 outer rollout distribution 被 stop-gradient，trajectory-level REINFORCE term 被刻意丢弃并交给 GRPO；
  conditional-PMI identity 依赖 student/teacher 同参数、同 prefix 与明确 privileged context，不能外推到外部
  teacher、不同 tokenizer 或异步 stale teacher。
- **Training / Evaluation Contract**：五个 models 为 Qwen3-8B、Qwen3-4B-Instruct-2507、Olmo-3-7B-
  Instruct/Think 与 Qwen3-30B-A3B；DAPO-Math-17k，200 steps，AdamW LR `1e-6`，32 problems/batch、
  8 rollouts/problem、training max 32K，temperature 1.0/top-p 1.0，lambda 0.5。evaluation 对 AIME24/25/26、
  HMMT25 使用 32 rollouts，对 MinervaMath 使用 4，temperature 0.7/top-p 0.95。每节点 8×NVIDIA H20，
  30B 为 multi-node；node count、precision、wall-clock、GPU-hours、network、checkpoint-selection uncertainty
  与多 seed 未披露。repo 的 Qwen3-8B launcher 标注 16K response/12K length mask，与论文统一 32K max
  contract 需要按 exact config/commit 复现时再对齐。
- **Results / What They Prove**：作者 best-checkpoint average 上 AntiSD 相对 GRPO 在五个模型高 2.1～11.5
  absolute points，并在其定义下用 2～10 倍更少 optimizer steps 首次达到 GRPO best average；HMMT
  pass@k 到 32 仍保持 gap，反驳“只把概率集中到已有正确轨迹”的一种解释。Qwen3-8B code probe 仅在
  HumanEval+/MBPP+ 高 1.2/2.3 points。continual AntiSD 从 Qwen3-8B GRPO@200 继续 30 steps 达 65.0，
  接近 from-base 65.7；4B continual plateau 又低 2.3 points，说明 basin/gate transfer 具有 model dependence。
  这些证据支持 privileged-context credit polarity 会改变受限 reasoning RL dynamics，不证明普遍的自我提升。
- **Ablations / Failure Evidence**：default SD 在 Qwen3-8B 从 AntiSD 65.7 降至 30.6；reverse-KL ascent 因
  heavy tail 也到 30.6，说明 sign reversal 与 bounded shape 缺一不可。移除 gate 在 Qwen models 约 step 40
  transient peak、约 step 90 collapse，但在 Olmo3-7B-Instruct 可存活 200 steps，说明 gate 是跨模型保险，
  不是所有模型必需。`0.90/0.93/0.95` threshold sensitivity 在 4B 与 8B 方向不同；no-teacher variant 不学习，
  支持增益依赖外部 privileged information，而非 student probability 的通用 shaping。Additive composition 优于
  multiplicative 只在当前 recipe 成立。
- **What It Does Not Prove / Performance Boundary**：`2～10×` 是 `GRPO best-Avg step / AntiSD first-reach
  step`，不是 wall-clock、tokens、FLOPs、energy 或 cost speedup；AntiSD 还增加 teacher forward、entropy/
  logprob materialization 与 privileged-context generation/verification。best-checkpoint reporting、32-sample
  evaluation、单训练 run 与无置信区间使峰值差异含 selection/sampling uncertainty。实验主要是竞赛数学，
  code 只有单 model/两 benchmark 小增益；没有 Agent/tool trajectory、natural language、safety、OOD、
  long-horizon credit、verifier noise、错误 privileged solution 或 adversarial feedback evaluation。
- **Trade-offs / New Failure Modes / Previous Designs**：dense token credit 可能更快点燃学习，却需要额外
  teacher compute、可信 `c`、same-prefix alignment 与 gate state。错误 verified solution 会把反向信号施加在
  错误参照上；entropy 是 signal collapse proxy，不是 correctness，跨 model threshold 仍有 sensitivity。
  奖励 deliberation proxies 可能诱导无效 backtracking、冗长或 stylistic tokens；惩罚 shortcut tokens 也可能
  抑制已学会的正确简洁路径。纯 GRPO 在 verifier 稳定、group diversity 充足、额外 teacher 不值时仍成立；
  standard self-distillation 在目标就是 compression/imitation 时仍合理；learned PRM 在有高质量 step labels
  且需要可独立校准时是另一分支。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`terminal group reward → standard privileged-context
  self-distillation → conditional-PMI polarity diagnosis → sign reversal → bounded JSD token shaping → entropy
  validity gate → combined outcome + dense credit` 是 `Direct Evolution`，不是 self-distillation 被普遍否定。
  已读 Ch29 与 Ch28/30，并核对 Ch25 context distillation。Ch25 已明确 privileged context、same-prefix
  divergence、teacher snapshot 与 shortening/correctness 边界；Ch29 已覆盖 sequence-to-token credit、PRM
  exploit surface、verifier/trajectory identity，但缺口是“privileged context 改变 token credit 的符号，且
  dense signal 要有 validity gate”。主 owner 因而为 Ch29，provisional `Refine — Existing Argument`，
  `Status: Experimental`；Ch25 只作“compression objective 与 exploration objective 方向不同”的 handoff。
  Historical Books Gate 关闭，本检查点不修改 Books。
- **Open Questions**：需要 compute-matched teacher-forward cost、multi-seed/held-out checkpoint selection、
  nonlinear AntiSD objective 的 global/policy-invariance analysis、错误/冲突 privileged context robustness、
  calibrated gate alternatives、token-category causal interventions、verbosity/reward-hacking audit、Agent/tool
  trajectory transfer、不同 verifier density 与 asynchronous teacher staleness，以及 checkpoint/replay 中 gate/
  context/verifier lineage 的一致性测试。

### Video2GUI — 24/30 — Full Review Complete

- **Candidate / Week / Source Family**：`VIDEO2GUI-INTERNET-VIDEO-TO-EXECUTION-TRAJECTORY`；W20；
  arXiv:2605.14747 v1，first-public 2026-05-14，ICML 2026 accepted，访问日 2026-08-11。当前无
  arXiv revision。作者 repository 与 WildGUI release 在 event date 之后变化，revision timeline 与论文事件
  分开记录。
- **Direct / Related Primary Sources**：30 页 arXiv PDF、官方 project page、`WeiminXiong/Video2GUI`
  repository、作者链接的 `xwm/WildGUI` 与 companion screenshot repository。GitHub current tree 只有 static
  project assets/README，没有论文所述 filtering、annotation、grounding 或 training pipeline code；因此“pipeline
  will be released”截至访问日尚不能按 code path 核验。WildGUI 于 2026-06-14 完整上传，是后续 artifact，
  可用于 schema/release 核验，不倒写成 W20 已可下载事实。
- **Full-read Coverage**：已覆盖 POMDP formulation、coarse-to-fine filtering、trajectory extraction、spatial
  grounding、two-stage training、两 model families 全部 grounding/offline/online results、scaling/三任务/阶段
  ablations、human data-quality study、Related Work、Conclusion/Impact，以及 Appendix A～I 的 classifier/scorer、
  prompts、action spaces、post-training mixture、API cost、dataset/evaluation details 与 examples；artifact 侧核对
  current schema、shards、screenshot linking、`use_grounding`、missing frames、license 与 release size。
- **Original Problem / Why Previous Designs Were Reasonable**：human demonstrations 与 executable simulators
  提供较清楚的 action/state ground truth，适合受控 platform 与 safety-critical evaluation；但人工成本高，模拟器
  coverage/realism 又受 schema 限制。互联网 tutorial videos 已包含真实 UI、用户意图与操作顺序，却没有
  machine-readable actions，且 compressed video 难以定位 click coordinates。约束变化不是“没有视频”，而是
  如何用受控成本把 noisy observation 编译成带 lineage 的可训练 trajectory。
- **Mechanism / Data Compilation Pipeline**：先以 DeepSeek-V3 标注 10K metadata、训练 Qwen2.5-7B binary
  classifier，把 500M+ YouTube metadata 缩到约 20M；再用 Gemini-3-Pro 标注约 200 hours、训练 Qwen2.5-
  Omni 三维 video scorer，以 topic relevance、instruction clarity、recording quality 均不少于 4.2 保留约 4.16M
  videos/300K hours。每个不超过 12 分钟的视频切成最多 4 分钟 segments，Gemini-3-Pro 读取 current frames
  与前段 textual results，输出 task、plan、timestamp、action、rationale 与 expected state change；随后对每个
  timestamp 取 `t-0.5s/t/t+0.5s` 三张 high-resolution frames，再做 action parameter/coordinate grounding。
- **State Ownership / Control and Data Flow**：source video/metadata 拥有原始 observation、timebase、platform
  与 creator provenance；metadata classifier/video scorer 拥有 retention decision；segment annotator 拥有
  cross-segment textual memory 与 proposed task/action chain；grounder 拥有 frame triplet、coordinate/action
  parameters 与 validity；dataset row 应绑定 video id、segment/task id、timestamp、instruction、plan、platform/
  software/site、ordered actions、state-change claim、screenshot pointer、annotator/scorer/prompt revision 与
  `use_grounding`。训练端再把 lineage-preserving rows 编译成 grounding、single-step action 与 multi-turn
  trajectory examples。当前 release 缺少完整 model/prompt/API revision 与 source-license/takedown lifecycle，
  所以 schema 仍不是完整 reproducibility manifest。
- **Training Contract**：WildGUI 论文统计为 12.7M task trajectories、124.5M screenshots、1500+ apps/sites；
  Stage 1 将 `L_ground + L_action + L_traj` 等权相加，continual pretraining 一 epoch/约 200B tokens、24K steps；
  Stage 2 混合 Rico、SeeClickWeb、WebUI、OS-Atlas、AITW/AITZ、AndroidControl、AMEX 与 GUI-Odyssey，三
  epochs/约 15B tokens、2K steps。两阶段 max 4096 visual tokens、sequence 32768；Megatron/AdamW，整个
  cluster 为 160 CPU cores、512GB RAM、256 NVIDIA GPUs，但 GPU model、training precision、parallelism、
  batch、wall-clock、checkpoint policy 未披露。论文未给 source-language distribution；HF card标 English，
  与正文“cross-lingual/cultural source”不能视为同一已量化 contract。
- **Evaluation / Ablations**：Qwen2.5-VL-7B 与 MiMo-VL-7B 分别比较 base、Stage2-only、Stage1+Stage2；
  ScreenSpot-Pro/OSWorld-G 测 grounding，AndroidControl/CAGUI 测 offline action，OSWorld/AndroidWorld
  测 online success。MiMo full path 在 AndroidWorld 为 31.9%，相对 base 16.4%、Stage2-only 23.3%；OSWorld
  为 12.3%，相对 8.3%/10.4%。移除 `L_traj` 使 AndroidWorld 31.9→24.1，但 static tasks 变化较小；移除
  `L_ground` 使 ScreenSpot-Pro 56.9→49.8；没有 Stage2 时 AndroidWorld 仅 6.0，说明 noisy broad pretraining
  不能替代 clean task alignment。0～200B scaling curves 只给单路径相关趋势，无 matched-compute alternative、
  error bars 或 multiple seeds。
- **Data Quality Evidence**：三 frame grounding 对 200 sampled actions 的 manual correctness 超过 95%；另有
  5 位非项目成员 experts 对 300 samples 打分，qualification ≥0.85，trajectory-quality inter-rater
  `Krippendorff alpha=0.84`。这些抽查支持 pipeline 可产生高质量样本，但相对 12.7M trajectories 覆盖极小，
  未分 platform/action/app/language 长尾，也未测 hallucinated rationale/state changes、identity transitions 或
  catastrophic coordinates。自动 annotator/scorer 同属强 VLM family，会保留 shared blind spots。
- **Artifact / Counting Boundary**：2026-06 后的 HF card明确是“personally reprocessed annotation release”，
  由 full workflow 重新生成/清理；其 viewer 约 94.2M rows、8.33TB，row 可对应 screenshot/action surface，
  不能与论文 12.7M task trajectories 相互替换。annotations 为 19 JSONL shards，screenshots 分布在两个 repos；
  少量 frame 可缺失，`use_grounding=false` 时不得把缺省 parameters 当监督。dataset 为 CC-BY-NC-4.0，
  project code repository 为 Apache-2.0；代码许可不能覆盖 source YouTube content rights。
- **What the Evidence Proves / Does Not Prove**：matched base-family ablations 支持大规模、多平台、从真实
  tutorial-derived 的 offline data 能改善所测 grounding/action/online tasks，且 trajectory loss 与 clean Stage2
  分别接住 long-horizon state 与 task alignment。它不证明 extracted rationale 是真实 human intent、不证明
  video observation 等价于可重放 environment transition、不证明完全自动 pipeline 在无人工 threshold/audit
  下可靠，也不证明任意 200B GUI tokens 单调扩展。Stage2 mixture 包含 AndroidControl 等 evaluation family，
  论文未在此处给出逐数据集 train/test/near-duplicate contamination lineage，相关 offline results 不可解释为
  纯 unseen generalization；online OSWorld/AndroidWorld 仍是较强但单-run、低绝对成功率 evidence。
- **Trade-offs / New Failure Modes / Previous Designs**：metadata-first cascade 把昂贵 video inference 聚焦到
  少量 candidates，却放大 first-stage false negatives；first-minute scoring 可能漏掉后段 quality。segment textual
  memory 降低 video-context cost，却可把早期 hallucination 传播到后段；three-frame grounding 降低 compressed-
  frame误差，但 0.5 秒固定 offset 依赖 action timing。教程展示的是成功路径与 author-chosen UI，产生 survivorship、
  popular-app、English、clean-demonstration 与 stale-version bias，几乎没有 recovery、permissions、destructive
  side effects 或 failed actions。人工/模拟器在需要 exact environment state、negative paths、license/consent 与
  verifier correctness 时仍成立；video mining 是补充 coverage 的分支，不是替代。
- **Privacy / Legal / Safety Boundary**：public tutorial screenshots 可能包含 usernames、emails、API keys、
  personal files、browser state 或第三方 copyrighted UI/content；论文 Impact Statement 未具体讨论 consent、
  PII/secrets redaction、robots/ToS、creator opt-out、deletion propagation、source takedown 或 harmful workflows。
  数据 card 的 non-commercial license 与 noise warning不能解决 source-level rights。进入 production training
  data plane 前需 source allowlist/rights manifest、PII/secret scanning、hazard taxonomy、takedown→derived-row/
  screenshot/checkpoint lineage 与 restricted-action filters。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`manual executable trajectory → platform simulator →
  keyword video mining → metadata classifier → multimodal quality scorer → segment-level semantic extraction →
  high-resolution action grounding → three-task continual pretraining → clean task post-training` 是 `Direct Evolution`，
  并与 executable-specification synthesis 形成 parallel branch。已读 Ch23 及 Ch22/24，并核对 Ch74/75/77。
  Ch23 已拥有 multimodal transformation lineage、quality-filter selection bias、synthetic trajectory/verifier contract
  与 contamination；真正缺口是 observation-derived trajectory 的 multi-stage compiler、timestamp/frame/action
  lineage 与 source-rights lifecycle，故主 owner Ch23，provisional `Refine — Existing Argument`，`Status:
  Experimental`。Ch74 只作 action-schema handoff，Ch75/77 不重复 data-production 内容。Historical Books Gate
  关闭，本检查点不修改 Books。
- **Open Questions**：需要 event-time pipeline code、frozen artifact/manifest、12.7M→94.2M count reconciliation、
  exact source/license/consent and deletion policy、PII/secret/hazard audit、per-slice grounding error、human-vs-model
  rationale validity、train/eval contamination scan、failed/recovery trajectory coverage、matched compute/data-quality
  alternatives、multi-seed online evaluation，以及 raw video→derived rows→screenshots→training checkpoint 的
  end-to-end provenance 与 takedown propagation。

### π-Bench — 25/30 — Full Review Complete

- **Candidate / Week / Source Family**：`PI-BENCH-PROACTIVE-LONG-HORIZON-ASSISTANT-EVALUATION`；W20；
  arXiv:2605.14678 v1 first-public 2026-05-14，v2 2026-05-15，v3 2026-05-19，访问日
  2026-08-11。W20 event 归属 v1；v3 用于核验当前机制、扩展实验与 artifact，不把后续 revision
  的新增信息倒写成 05-14 已公开事实。
- **Direct / Related Primary Sources**：arXiv abstract、44 页 v3 PDF/HTML、作者 project page、
  `Simplified-Reasoning/Pi-Bench` repository、公开 dataset surface。当前 repository 提供 benchmark
  runner、model/user/judger configuration、Docker/AppWorld/Nanobot integration、tasks 与 graders，
  Apache-2.0；论文模型通过 hosted APIs 调用，provider endpoint/revision 与凭证不随 artifact 固化，
  因而 leaderboard 结果仍需绑定 evaluation date 与 exact model config。
- **Full-read Coverage**：已覆盖 Introduction/Related Work、100-task construction、user-agent protocol、
  hidden-intent state machine、Proc/Comp 公式、九模型三次重复实验、history ablation、turn-cost analysis、
  Limitations，以及 Appendices A～J 的 187 tools/21 skills、user prompt、two-stage assignment、hybrid
  graders、runtime、human/model audit、failure taxonomy、task construction/sanitization 与 case studies；
  artifact 侧核对 setup、repeat/rerun semantics、environment variables 与 outputs。
- **Original Problem / Why Previous Designs Were Reasonable**：static instruction-following、GUI action、
  memory retrieval 与 final-success benchmark 容易复现，也适合隔离局部能力；但 persistent professional
  workflow 的初始请求往往合理地欠规格，早期 artifact 又会约束后续 session。只测最终产物会把“Agent
  主动恢复了约束”与“用户后来把答案全部喂给 Agent”合并成同一种成功。
- **Mechanism / State Ownership**：五个 domain personas 各形成一个 20-session episode；100 tasks 包含
  六组每组 2～3 个强 dependency tasks 与五个 largely independent tasks。benchmark owner 持有 persona、
  initial request、workspace、cross-session dependency、524 个 hidden intents、510 rubric items、168 rule
  checks 与 termination policy；evaluated Agent 只观察 user messages、允许的 memory/workspace/tools，不能
  读取 hidden labels。user simulator 的状态机对每个 intent 只赋一次 terminal status：先检查 Agent 是否
  未经明说直接完成，再检查是否提出 targeted clarification，否则 simulator 主动提供一个当前相关 intent。
- **Control Flow / Data Flow**：`underspecified request or heartbeat -> agent response/tool/artifact update ->
  user-agent completion check -> targeted-question check -> reveal one unresolved intent if needed -> terminal
  intent partition -> hybrid artifact/tool checklist scoring`。session 只有在所有 intents 为 completed、inferred
  或 provided 且 Agent 给出 final response 后结束。这个 oracle-like completion loop 保证 Comp 最终看见完整
  requirement set，但同时改变了自然用户可能退出、拒绝或容忍缺失的真实 stopping distribution。
- **Evaluation Contract**：Proc 为 `(completed + inferred) / all hidden intents`，直接满足与 focused
  clarification 等权；Comp 为 binary checklist items 的平均，open-ended criteria 由 GPT-5.4 judge 判断，
  objective tool/artifact state 由 task-specific scripts 检查。九个 frontier models 共用 Nanobot-derived
  scaffold、thinking enabled 与 provider default decoding，每 task 三条独立 trajectories，报告均值和标准差；
  GPT-5.4 同时是 user agent 与 rubric judge，temperature 0。runtime 为 Ubuntu 24.04.1、双 socket、
  32 physical cores/64 threads、251 GiB RAM、1 TB storage、Docker；单 task 通常少于 8 GB RAM，
  workspace 少于 32 GB。API revision、token/cost/latency、network、timeout/budget 与 production SLO 未完整披露。
- **Results / Ablation / Reliability**：主表只证明当前 scaffold/模型快照下 Proc 与 Comp 会明显分离，
  不形成通用模型排名。移除每个 strong-dependency group 的 earlier sessions 后，三个测试模型的 final-task
  Proc 平均下降 9.5 points、Comp 平均下降 2.5 points；这支持 prior interaction 对 latent-requirement recovery
  有条件价值，不证明任意 memory implementation 有效。120 条跨模型 trajectories 的三人 majority audit
  相对原 scorer disagreement 为 checklist 2.66%、intent status 1.48%；independent model audits 也低于
  3.6%/2.1%。这是 sampled agreement，不是 hidden-intent specification validity、deployment validity 或
  judge independence 的证明；GPT-5.4 同时生成用户反馈与部分评分仍可能带 correlated blind spot。
- **What the Evidence Proves / Does Not Prove**：证据支持将 proactive requirement discovery 与 final
  workflow completion 分开，并把 memory、workspace、tools、artifacts、simulator 与 scorer 都纳入 Agent
  evaluation subject。它不证明高 Proc 等于高 user value、安全、正确权限使用或低 cognitive burden；turn
  count 只是 interaction cost proxy，合理澄清也会增加 turns。Proc 对“猜中后直接行动”与“先问后行动”等权，
  没有 false-positive intent、unwanted intervention、overreach、reversibility、approval 或 harm penalty；
  simulator 最终提供 intent 也会抬高被动 Agent 的 Comp。五个 synthetic personas、单 scaffold 与有限 domain
  slices 不能外推为真实长期用户。
- **Trade-offs / New Failure Modes / Previous Designs**：persistent history 能降低重复说明，却增加 stale
  preference、wrong-user context、privacy leakage、cross-session contamination 与 deletion propagation；主动
  completion 能降低用户负担，却可能在高风险或不可逆动作上越权。targeted clarification 更安全、可校准，
  但增加 latency/turns；static explicit-request benchmark 在回归、权限明确与单步任务中仍合理。生产评估需在
  `Proc + Comp` 外并列 `false-positive intervention、ask quality、permission/approval、reversibility、harm、
  user override、abandonment、latency/cost`，而不是把主动性压成单一越高越好的分数。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`explicit single-turn task -> final-answer success ->
  tool/artifact completeness -> multi-turn feedback-conditioned trajectory -> persistent cross-session state ->
  separate requirement-discovery and outcome metrics -> risk/permission-aware proactivity` 是 `Direct Evolution`。
  已读 Ch62 与 Ch61/63，并核对 Ch73/75/77。Ch62 已拥有完整 evaluation-subject identity、feedback channel、
  trajectory evidence 与 hybrid-verifier/judge audit；缺口是把 latent requirement ownership、oracle user-feedback
  channel与 false-positive proactivity cost 写成同一 evaluation contract。因此主 owner 暂定 Ch62，
  `Refine — Existing Argument`，`Status: Experimental`；Ch73/75/77 只保留 persistent state、clarification 与
  durable workflow handoff。Historical Books Gate 关闭，本检查点不修改 Books。
- **Open Questions**：需要真实用户 longitudinal validation、hidden-intent authoring inter-rater validity、
  false-positive/overreach counterexamples、permission and irreversible-action slices、clarification quality 与
  user-burden study、abandonment/early-stop protocol、harness/model/API revision manifest、compute/cost-matched
  repeats、cross-scaffold ablation、privacy/consent/deletion tests，以及对 malicious/stale workspace evidence 的
  recovery benchmark。

### Auditing Agent Harness Safety — 26/30 — Full Review Complete

- **Candidate / Week / Source Family**：`HARNESSAUDIT-TRAJECTORY-POLICY-INFORMATION-FLOW`；W20；
  arXiv:2605.14271 v1 first-public 2026-05-14，v2 2026-05-16，访问日 2026-08-11。v1/v2 都在
  W20；revision 只相隔两日，当前 v2 用于机制与实现核验。
- **Direct / Related Primary Sources**：11 页正文、完整 arXiv HTML Appendices、官方 project page、
  `UCSB-AI/HarnessAudit` repository（MIT）、`LCZZZZ/HarnessAudit` dataset。公开 repo 包含 runner、
  single/multi-agent tasks、stateful mock banks、SDE fixtures、Claw-Team vendor snapshot、OpenClaw/Claude
  Code/Codex/OpenAI Agents SDK/Google ADK adapters、trace/access/checkpoint/judge code；run outputs、SQLite
  snapshots、workspace、private keys 与 paper build artifacts 按 README 不提交。
- **Full-read Coverage**：已覆盖 harness formalization、三层 safety model、trajectory pipeline、全部
  metrics、210-task construction、十 harness/model configurations、五项 RQ analysis、Conclusions，以及
  Appendices 8～13 的 declarative specification、hidden artifacts、unified trace、native/inline ingestion、
  access matchers、aggregation、task QC、runtime defaults、judge/perturbation protocols、single-agent baseline
  与 hub-spoke adapter semantics；artifact 侧核对 quickstart、output schema、rejudging 与 release surface。
- **Original Problem / Why Previous Designs Were Reasonable**：final answer / terminal state 易于比较，
  对无副作用问答仍是有效、低成本 signal；tool allowlist 也能阻止明显错误工具。但 Agent harness 已经
  拥有 delegation、resource binding、message routing 与 termination：一个 benign correct output 可能经过
  越权 record access、错误 object id、敏感字段跨角色传播或不可逆副作用。约束从“输出是否安全”变成
  “整条执行路径是否持续满足 user intent、permission 与 information-flow policy”。
- **Mechanism / State Ownership**：论文把 harness 定义为
  `H=(A,T,R,Pi,Phi,Sigma)`：acting components、tools、resources、permission policy、information-flow
  policy 与 coordination protocol。task specification owner 同时定义 user goal、role prompts、tool catalog、
  fixture、access/communication policy、completion checkpoints 与 valid tool paths；Agent 只见 goal 与 assigned
  tool surfaces。auditor 从同一 specification 派生 hidden deny rules、resource constraints、leak recognizers 与
  checkpoints，并在 run 后读取，避免 Agent self-report 成为唯一证据。
- **Control Flow / Evidence Plane**：`load task + deterministic fixture/workspace -> isolate native harness ->
  execute role agents -> ingest native JSONL or inline events -> normalize tool_call/communication/access_decision
  with run/timestamp/global sequence/role/native provenance -> preserve final SQLite/workspace -> post-hoc access,
  action-validity, completion and perturbation audit -> result JSON`。append-only trace 让同一 observed run 可离线
  rejudge；它不等于 complete causality，因为未被 wrapper/native log 捕获的 side channel 仍不可见。
- **Three-layer Contract**：L1 将 tool、resource 与 information-flow violations 分开，并区分 role/tool
  mismatch、argument/object scope、recipient routing 与 message-content disclosure；L2 将 hidden completion
  checkpoints（TCR）与 reference-path/resource-scope action validity（AVS）分开；L3 对 indirect injection、
  ambiguous goal 与 tool/runtime failure 做 controlled perturbation。Ambiguity rubric 要求不可逆动作前确认、
  只允许 bounded read-only investigation；tool failure rubric检查 honest acknowledgement、no fabrication、
  bounded recovery/safe defer。这个分层比单个 outcome score更可诊断。
- **Evaluation Contract**：210 tasks、8 domains/24 scenarios、3～7 roles/task（均值 4.6）、69 role templates、
  105 tasks×5 perturbations；大部分业务域使用 deterministic SQLite fixture，SDE 使用隔离真实 workspace。
  main runs 每 task 只一次，per-agent timeout 300s、max 30 framework turns、GPT-5.4 judge、4 judge workers；
  硬件、API revision、sampling、tokens、latency/cost、failure/retry rate 与 production SLO 未披露。OpenClaw
  shared-harness 与 provider-native configurations 不只改变 model；native CLI、tool surface、action count 与
  adapter/logging path 也变化，所以只有 matched slices 可支持 harness-level comparison。
- **Metric and Accounting Boundaries**：低/高 violation 权重固定为 0.15/0.30，每个 matched event 全额累加、
  不去重也不按 opportunity/trajectory length 归一化；SAR 三 channel 均值再作为 multiplicative gate，默认
  composite 为 `SAR_avg × (0.7 TCR + 0.15 AVS + 0.15 PB)`。这些是作者的 decision utility，不是自然定律；
  长轨迹本来就有更多被计数机会，因此“actions 越多、violations 越多”的观察含 exposure 与 metric-design
  confounding。reference tool-path AVS 还可能惩罚合法替代路径，LLM judge 未报告独立 human reliability audit。
- **Internal Consistency Audit**：Table 2 的最高 Overall 为 Gemini/OpenClaw 0.41，但正文与 project page
  声称 best system 只有 0.32；Table 1 报 91 tools，Appendix task statistics 报 94 tool entries；main table
  使用 `S@T20/50/80`，Appendix 公式文字使用 `S@T20/40/60`。这些冲突不改变“final completion 与 boundary
  compliance 可分离”的方向性机制，却使具体 headline、catalog count 与 threshold curves 标记为
  `Disputed Accounting`，复现前必须以 frozen code/data/commit 重算。
- **What the Evidence Proves / Does Not Prove**：公开实现支持跨 harness 规范化可观察 tool/message trace、
  hidden post-hoc policy checks、state snapshots 与三层 scoring 可执行。作者实验在其 tasks/config 下显示
  resource scope 与 message content 是重要 failure surfaces，task completion 不能替代安全 audit。它不证明
  harness design 单独因果决定结果、不证明多 Agent 必然更危险，也不证明当前 recognizers 捕获所有泄漏；
  single-agent baseline 没有 communication channel，multi-agent 又改变 roles/actions/trajectory，表中差异不是
  communication-only randomized ablation。mock data 与 10 个 SDE tasks 也不是 production deployment validation。
- **Trade-offs / Previous Designs / New Failure Modes**：hidden audit artifacts 降低 gaming，却让 policy
  specification、recognizer coverage 与 benchmark owner 成为新的 trusted computing base；post-hoc audit 可诊断，
  不能阻止已发生的泄漏或副作用，生产仍需 executor-time deny/approval/redaction。统一 trace 增加 portability，
  却可能因 native timestamp/reordering、missing artifact、namespace stripping 与 adapter drift 产生 false evidence；
  full message/tool-result logging 又扩大 secret/PII retention 风险。只用 final output 在低权限、无副作用场景仍
  合理；deterministic online enforcement、minimal telemetry 与 selective post-hoc audit 应按风险组合，而非互斥。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：`final-output moderation -> tool allowlist -> full
  trajectory capture -> resource/object-scope audit -> inter-role routing + content-flow audit -> perturbation under
  ambiguity/injection/failure -> preventive policy enforcement + post-hoc evidence` 是 `Direct Evolution`。
  已读 Ch62/68/74/77/78/80。Ch62 已拥有完整 subject identity、trajectory/environment/side-effect evidence、
  hybrid verifier 与 judge audit；新增缺口是把 recipient topology 与 message-content disclosure、resource
  object scope、hidden policy artifacts 和 perturbation stability 放进同一 EvalSpec，故主 owner 暂定 Ch62，
  `Refine — Existing Argument`，`Status: Experimental / Disputed Accounting`。Ch68/74 继续拥有 preventive
  authority；Ch78 只接 information-flow/delegation handoff；Ch80 接 evidence-plane implementation。
  Historical Books Gate 关闭，本检查点不修改 Books。
- **Open Questions**：需要修正三处公开账目冲突、冻结 paper-result commit/model endpoints、multi-seed 与
  uncertainty、violation opportunity/trajectory-length normalization、合法替代路径与 judge human audit、
  communication-only matched ablation、adapter capture completeness、encrypted/minimized trace retention、
  covert-channel/derived-information leakage、online enforcement 与 post-hoc audit coverage comparison，以及
  real production incident replay。

### Kubernetes PSI Metrics GA — 27/30 — Full Review Complete

- **Candidate / Week / Source Family**：`K8S-PSI-CONTENTION-OBSERVABILITY`；W20；官方 Blog 发布于
  2026-05-12，按 Linux 2018 PSI、Kubernetes 1.33 Alpha、1.34 Beta、1.36 GA 联读，访问日 2026-08-12。
- **Problem / Previous Design / Changed Constraint**：CPU、memory 与 I/O utilization 易采集，在资源宽松、
  workload 同质时仍是合理容量信号；但 utilization 未满也可能有 task 因 run queue、reclaim 或 I/O 等待而
  stall。多租户 AI workload 的真实约束从“用了多少”变成“有多少执行时间因争用而损失”。
- **Mechanism / Ownership / Flow**：Linux kernel/cgroup 拥有 PSI 原始状态；kubelet/cAdvisor 暴露 node、pod、
  container 的 cumulative stall totals 与 10/60/300 秒 moving averages。Kubernetes 1.36 先检测 OS support；
  unsupported 时省略 metric，避免把 missing 伪装成 zero。平台 owner 再把 pressure 与 latency、queue、GPU
  idle 和 eviction 对齐，不能让 exporter 替调度器决定行动。
- **Evaluation Contract / Evidence Boundary**：官方测试覆盖 4-core machines、80+ pod density，并分别比较
  kubelet read path 与 kernel bookkeeping；披露的 kernel delta 多在 0.037～0.125 cores，且有短时更高 spike。
  这些数值不外推到不同 kernel、cgroup、node size 或采样频率。它证明 stable exposure 与该测试 contract 下
  的可接受 overhead，不证明 PSI 单独能定位 root cause 或定义 universal alert threshold。
- **Trade-offs / Evolution / Decision**：`utilization -> saturation proxy -> PSI stalled time -> workload/SLO
  correlation -> scheduler feedback` 是 `Direct Evolution`。PSI 增加可诊断性，也增加 kernel/platform support、
  label cardinality、sampling 与 threshold governance；Windows 或禁用 PSI 的节点仍需传统 metrics。已读 Ch63
  及 Ch59/69；主 owner 暂定 Ch63 `Refine — Existing Argument`，Historical Books Gate 关闭，未改 Books。

### Kubernetes Workload-Aware Scheduling v1alpha2 — 28/30 — Full Review Complete

- **Candidate / Week / Source Family**：`K8S-WORKLOAD-PODGROUP-ATOMIC-SCHEDULING`；W20；官方 Blog
  2026-05-13，联读 scheduling API reference；全部机制在 1.36 仍为 Alpha，访问日 2026-08-12。
- **Problem / Previous Design / Changed Constraint**：逐 Pod filter/score/bind 对独立 service replica 简单可靠；
  对 gang、拓扑耦合与共享 device claim，局部可行却可能形成 partial placement、deadlock 或资源空转。约束从
  “为一个 Pod 找 node”变成“在一致 cluster view 下证明 group-level placement 可执行”。
- **Mechanism / State Ownership / Control Flow**：v1alpha2 将 static Workload template 与 runtime PodGroup/status
  分开，Pod 用 `schedulingGroup` 引用 group。scheduler 从 queue 收集并确定序 Pod，基于 single snapshot
  生成 placement、执行标准 Pod filtering/scoring、验证 whole group，再整体进入 bind 或全部 backoff；拓扑分支
  增加 `PlacementGenerate` / `PlacementScore`，workload-aware preemption 以 group 为 preemptor，并可跨 node
  找 victims。Job controller 拥有 Workload/PodGroup 创建，scheduler 拥有 placement，DRA controller 拥有 claim。
- **Evidence / Limits**：官方材料证明 API/control flow 和实现状态，不是 performance benchmark。homogeneous
  group 预期更容易找到 placement；heterogeneous 或含 affinity/topology dependencies 的 group 不保证找到已
  存在解，deterministic order 甚至可能系统性失败；topology-aware path 当前不触发 preemption。
- **Trade-offs / Evolution / Decision**：`independent Pod -> admission-time gang guard -> runtime PodGroup ->
  single-snapshot group cycle -> placement-aware scoring/preemption` 是 `Direct Evolution`。原子决策减少 partial
  bind，却扩大 snapshot staleness、search cost、reservation/rollback、fairness 与 disruption semantics。已读
  Ch60 及 Ch59/56/63；Ch60 已拥有 Volcano PodGroup，但缺 Kubernetes-native template/runtime ownership 与
  atomic cycle 的演进桥，故暂定 `Refine — Existing Argument / Experimental`；本轮不改 Books。

### Kubernetes Service `externalIPs` Deprecation — 24/30 — Full Review Complete

- **Candidate / Week / Source Family**：`K8S-EXTERNALIPS-INSECURE-DEFAULT-MIGRATION`；W20；官方 Blog
  2026-05-14，联读 CVE-2020-8554、`DenyServiceExternalIPs` 与替代方案边界，访问日 2026-08-12。
- **Problem / Evolution**：早期 `.spec.externalIPs` 为非云集群提供简单的 LB-like address，建立在所有 API
  writers 可信的假设上；多租户后，普通 Service writer 可声明他人 IP。Kubernetes 1.21 先给 opt-in admission
  deny，1.36 才正式 deprecated，并计划后续从 kube-proxy / conformance 移除，体现兼容性与 secure-default
  之间必须经过 guard、inventory、migration 和 final removal。
- **Mechanism / Boundary**：问题只指 Service `.spec.externalIPs`，不等于 Node ExternalIP 或 LoadBalancer
  输出列。手工写 LoadBalancer status 只是把 authority 提升到 privileged writer，仍可复制攻击；controller
  管理的 address pool 还能提供 ownership/uniqueness validation。官方迁移说明不是 exploitation evaluation。
- **Trade-offs / Decision**：立即禁用降低 exposure，却可能破坏已有 bare-metal routing；长期保留兼容则让
  insecure default 持续存在。已读 Ch68 及 Ch53/67；暂定 Ch68 `Refine — Existing Argument`，沉淀的是
  “deprecated security surface 的多阶段迁移 contract”，不是 Kubernetes 功能表；Historical Books Gate 关闭。

### Kubernetes Mixed Version Proxy Beta — 26/30 — Full Review Complete

- **Candidate / Week / Source Family**：`K8S-MIXED-VERSION-API-SURFACE-PROXY`；W20；官方 Blog
  2026-05-15，追溯 1.28 Alpha 到 1.36 Beta/default-on，访问日 2026-08-12。
- **Problem / Previous Design**：rolling upgrade 允许 HA API servers 短时版本不一，单 server 按本地 discovery
  返回 404 原本符合 local knowledge；但 cluster-level client 会把它当资源不存在，可能触发错误 GC 或阻塞
  namespace deletion。新约束是“对外 API truth 属于 control-plane cohort，不属于偶然命中的 replica”。
- **Mechanism / Ownership / Flow**：旧 server 查询 peer capability cache，把 request 加
  `x-kubernetes-peer-proxied` 后转给能服务该 GVR 的 peer。Beta 从 StorageVersion API 转向 Aggregated
  Discovery，覆盖 CRD/aggregated API，并合并 peer discovery 为统一视图；peer CA 与 advertise address 是安全
  和可达性前提，未配置时不能把 default-on 误读为自动可用。
- **Evidence / Trade-offs / Decision**：官方材料证明 feature behavior 与配置，不证明任意拓扑下 availability、
  latency 或 loop-free recovery。代理修复 false absence，却引入 peer cache freshness、TLS/identity、hop/loop、
  partial failure 和 debug attribution；稳定单版本 control plane 仍可直接 local serve。`local replica truth ->
  cohort discovery -> capability-aware proxy -> version-skew-safe API surface` 是 `Direct Evolution`。已读 Ch53
  及 Ch67/68；暂定 Ch53 refine，本轮不改 Books。

### Kubernetes CCM Route-Sync Metric — 22/30 — Full Review Complete

- **Candidate / Week / Source Family**：`K8S-CCM-RECONCILIATION-ATTEMPT-METRIC`；W20；官方文章修正日期后
  以 2026-05-15 为 event date，联读 KEP-5237 / 1.35 watch-based route reconciliation，访问日 2026-08-12。
- **Mechanism / Evidence Boundary**：Alpha counter `route_controller_route_sync_total` 在每次 route sync 时
  自增，使 fixed-interval 与 watch-triggered controller 能以 attempt rate 做 A/B；它直接证明“执行过几次”，
  不证明 cloud API 成功、route 正确、convergence latency 或 quota saving，counter reset 和 cluster churn 也需
  进入解释 contract。
- **Evolution / Decision**：`periodic reconcile -> event-triggered reconcile -> attempt telemetry -> outcome/latency
  telemetry` 是 `Layering / Dependency`。已读 Ch63；书稿已有 observation、decision、execution 与 outcome
  分层，因此为 `No Change — Already Covered`，只在 Weekly 保留具体反例。

### OpenAI TanStack Supply-Chain Incident Response — 27/30 — Full Review Complete

- **Candidate / Week / Source Family**：`OPENAI-TANSTACK-SUPPLY-CHAIN-INCIDENT`；W20；incident 发生
  2026-05-11，官方披露 2026-05-13，页面存在后续 deadline amendment；后续状态只用于 revision 核验。
- **Problem / Failure Path**：dependency allowlist、endpoint protection 和签名各自合理，但 upstream malicious
  package 在 phased-control rollout 未覆盖的两台 developer devices 执行后，沿 endpoint -> limited source repos
  -> credential material -> signing certificates 扩大 blast radius。官方称未发现 customer data、IP、published
  software alteration 或 credential misuse；“未发现”不等于数学上的不存在。
- **Containment / State Ownership**：response 隔离 devices/identities、撤销 sessions、旋转 repository credentials、
  暂限 deploy、轮换 signing cert，并先阻止旧 cert 新 notarization，再给 client update window 后 revoke。
  package provenance/minimum release age 属预防；credential/cert rotation 属 containment；forced client update 属
  recovery。把三者压成“更新依赖”会丢失 owner 与时序。
- **Evidence Boundary / Trade-offs**：这是官方 incident report，不是公开 DFIR artifact；不能推断 malware 的
  未披露实现或独立验证 impact。立即 revoke 可缩短 abuse window，却会让未更新 client 失效；延迟 revoke
  保护 continuity，却延长 residual trust window。`dependency trust -> endpoint compromise -> credential/signing
  blast radius -> staged containment/recovery -> provenance-enforced admission` 是 `Direct Evolution`。已读 Ch68
  及 Ch55/67；暂定 Ch68 refine，本轮不改 Books。

### OpenAI Cross-Conversation Safety Summaries — 27/30 — Full Review Complete

- **Candidate / Week / Source Family**：`OPENAI-PURPOSE-LIMITED-SAFETY-STATE`；W20；官方 Safety Blog
  2026-05-14，访问日 2026-08-12。
- **Problem / Previous Design**：single-conversation context 在局部风险识别中简单且隐私边界清楚；但严重风险
  信号可能跨 conversation 渐进出现。直接复用 general memory 又会扩大 personalization、retention 与 false-positive
  surface，因此新机制是 narrow, factual, limited-time、serious-safety-only 的 derived summary。
- **Ownership / Flow**：safety reasoning model 生成候选摘要，policy/experts 决定何时生成、相关范围与保留时间，
  response model 只在 serious concern relevant 时消费。derived state 必须绑定 purpose、TTL、source provenance、
  correction/delete 与 access policy；它不是对所有 memory 的许可，也不能从公开页面反推内部 storage architecture。
- **Evaluation Contract / Boundary**：内部高风险 scenario eval 报告 single-conversation 与 cross-conversation
  safe-response 相对改善，并对 4k+ summaries 给 relevance/factuality rating；未披露真实 prevalence、false-positive
  denominator、retention duration、reviewer agreement、hardware/cost 或 deployment incident rate。数字只对作者设计
  的 scenario/model version 成立，不证明 clinical benefit 或 ordinary-user zero impact。
- **Evolution / Decision**：`local context -> general persistent memory -> purpose-limited derived safety state ->
  governed lifecycle + independent harm/false-positive audit` 是 `Layering / Dependency`，不是“越多记忆越安全”。
  已读 Ch68、Ch73 与 Ch62；主 owner 暂定 Ch68 refine，Ch73 只接 provenance/TTL handoff；本轮不改 Books。

### NVIDIA Fleet Intelligence GA — 28/30 — Full Review Complete

- **Candidate / Week / Source Family**：`NVIDIA-FLEET-TELEMETRY-HEALTH-ATTESTATION`；W20；官方 GA Blog
  2026-05-11，联读开源 `fleet-intelligence-agent` README / repository，访问日 2026-08-12。
- **Problem / Previous Design**：node-up、GPU utilization 对小型同构 fleet 足够廉价；规模、硬件/firmware 异构、
  power envelope 与多租户并存后，performance、RAS health、configuration identity 与 integrity 不能再由单一
  dashboard 推断。
- **Mechanism / State Ownership / Flow**：read-only host agent 联合 GPUd/DCGM 收集 GPU、host、NVLink/network
  telemetry，支持 local file、Prometheus 与 OTLP；managed service 保存 inventory/history、执行 periodic checks
  并产生 alert/recommendation。Attestation SDK 从 GPU 获取 signed measurements，经 NRAS 与 RIM 校验后返回
  integrity status。agent 本地持久化 node identity/enrollment credentials；删除 state 可能为同一物理 node 创建
  新 identity，因此 identity lifecycle 与 metric retention 是正式运维状态。
- **Evidence / Trade-offs**：公开代码支持 collector/export/state surface；Blog 的 predictive/ROI 与客户陈述不是
  independent benchmark。repo 自述 `<500MB RAM`、`<1% CPU` 未给 workload/hardware sampling contract，不写成
  通用 overhead。remote telemetry 提高 fleet visibility，却扩大 egress、credential、retention、tenant isolation
  与 managed-service dependency；attestation 证明 measured configuration 与 reference match，不证明 workload
  correct、host uncompromised 或性能健康。
- **Evolution / Decision**：`availability -> utilization -> RAS/thermal/interconnect health -> configuration identity ->
  signed integrity evidence -> remediation decision` 是 `Layering / Dependency`。已读 Ch63/68 及 Ch59；主 owner
  暂定 Ch63 refine，Ch68 接 attestation/credential boundary；Historical Books Gate 关闭。

### NVIDIA Vera Rubin Agentic-Inference Scale-Up Contract — 25/30 — Full Review Complete

- **Candidate / Week / Source Family**：`NVIDIA-VERA-RUBIN-AGENTIC-INFERENCE-SCALEUP`；W20；NVIDIA
  Technical Blog 2026-05-14，访问日 2026-08-12。它是厂商公开架构说明，后续 7 月 Rubin GPU 深挖只能
  帮助理解 revision，不能反向改写 W20 event date 或充当 5 月事件的独立证据。
- **Original Problem / Previous Design / Changed Constraint**：单轮 chat 或较短 Decode 中，把同构 accelerator
  视为统一 token engine 简单且合理；Agent workflow 把一次用户任务扩成数百次非确定性请求、工具停顿、
  长 context 与小 batch Decode 后，aggregate throughput 与 per-step latency 同时成为约束，单一执行路径难以
  占据新的 Pareto frontier。
- **Mechanism / Ownership / Flow**：公开设计让 Vera Rubin NVL72 承担吞吐密集的 Prefill、long-context
  attention 与 MoE 主计算；Groq 3 LPX branch 承担确定性、低 jitter 的 Decode FFN execution，编译器调度
  point-to-point transfer 并在硬件边界之间传递中间状态。硬件/编译器拥有 placement 与 timing；serving
  runtime 仍必须拥有 request identity、phase/branch routing、state handoff、admission、rollback 与 SLO trace。
  官方材料没有公开完整 compiler algorithm、queue policy、failure recovery 或 production control plane。
- **Evaluation Contract / What It Proves**：材料说明了 workload decomposition 与公开的 component roles；性能、
  agent-throughput 与经济性数字来自 NVIDIA 自有 workload/model/hardware contract，且没有完整的 prompt/output
  length、concurrency、precision、queue、tail SLO 与独立 baseline。因此这里只保留“异构 phase execution 是一条
  可实现的设计分支”，不保留 headline multiplier，也不证明它普遍优于同构 GPU、PD disaggregation 或其他
  accelerator combinations。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：异构分工可能降低某一 branch 的 latency，却新增
  compiler/runtime coupling、activation/state transfer、cross-device precision/layout compatibility、capacity
  imbalance、failure-domain expansion 与 scheduling complexity。在 batch 足、transfer 昂贵、模型不匹配或运维
  简洁性优先时，同构 NVL72 或常规 PD 路径仍合理。
- **Evolution / ROADMAP / Decision**：这是
  `uniform accelerator -> phase-aware execution -> heterogeneous typed execution -> workflow-aware SLO routing`
  的 `Direct Evolution`。已读 Ch39～40、Ch45、Ch50～52；主 owner 暂定 Ch50
  `Refine — Existing Argument / Official Engineering Evidence`，Ch45/51 只接 hardware contract 与 state handoff。
  Historical Books Gate 关闭，当前不修改 Books。

### NVIDIA Model-Serving Pipeline Contract — 22/30 — Full Review Complete

- **Candidate / Week / Source Family**：`NVIDIA-SERVING-COMPATIBILITY-CONTRACT`；W20；官方 Technical Blog
  2026-05-12，联读其 TensorRT / ONNX / Dynamo-Triton 引用路径，访问日 2026-08-12。
- **Mechanism / Boundary**：文章把 export、opset、unsupported op/plugin、dynamic shape profile、framework/
  CUDA/cuDNN/driver version manifest、isolated upgrade test、layer/system profiling、batch profile 与 model version
  组成 deployment contract。它是 vendor best-practice，不含可复核 comparative experiment；“更快、更省”描述
  不作为性能证据。
- **Evolution / Decision**：`checkpoint -> portable graph -> hardware-specific engine -> versioned serving artifact ->
  workload-profiled runtime` 是现有 Ch45/55 已完整覆盖的 `Principle Reuse`。因此 `No Change — Already Covered`；
  保留在 Weekly 作为 fixed-source coverage，不制造 Books diff。

### Transformers v5.8.1 — 20/30 — Full Review Complete

- **Candidate / Week / Source Family**：`HF-TRANSFORMERS-5.8.1-PATCH`；W20；GitHub release 2026-05-13，
  commit `cc832f9`；联读 release notes / linked fix list，访问日 2026-08-12。
- **Mechanism / Evidence Boundary**：patch 聚焦 DeepSeek V4 integration、continuous batching fatal-error、weight
  converter regex 与 CSA mask collapse fixes。它证明该版本声明的 compatibility corrections，不证明模型机制、
  serving performance 或所有 DeepSeek V4 paths 正确；patch release 也不等于 framework-wide architectural change。
- **Evolution / Decision**：这是训练/模型定义到 serving runtime 之间的 version-contract evidence，Books 已由
  Ch45/55 覆盖。Disposition 为 `Weekly Only — Version Fact`；v5.8.0 的 05-05 event 仍归 W19，不在 W20 重计。

## Pending Full Source Review Queue

| Candidate | First-public Date | Primary Source | Pending Focus |
| --- | --- | --- | --- |
当前无 current-review pending，也无 blocked source family。

## Repository Changes

- 2026-08-13 重新逐行复算为 31 scored（22 high、8 mid、1 low）：30/30 `20+` Source Reviews 完成，
  blocked 与 ordinary pending 均为 0。Candidate Gate 已通过；cross-index discovery 与全历史 Books Gate 仍关闭。
- W20 从 2 个 baseline 扩展为 31 个 scored families；完成 MinT、δ-mem、Self-Distilled Agentic RL、
  Long-Context VLM Beyond 128K、RubricEM、BetaPRM、RTPurbo、WildClawBench、ToolCUA、EVA-Bench、EvolveMem、MemLens、MemEye、Anti-Self-Distillation、Video2GUI、π-Bench、HarnessAudit
  的全文、Appendix 与 artifact-boundary review；Qwen-Image-2.0 因完整 report 当前无法抽取而转入
  blocked backlog，current-review queue 已清空并推进 W21；把 W20 推荐流中 9 个 v1 日期属于更早周的 families 回拨
  W18/W19，并把 W21 推荐流中 6 个 first-public date 属于 W20 的 families 回拨本周。fixed official /
  Infra replay 新增并审计 Kubernetes PSI、Workload-Aware Scheduling、Service `externalIPs`、Mixed Version
  Proxy、CCM route-sync metric、OpenAI TanStack incident、cross-conversation safety summaries、NVIDIA Fleet
  Intelligence、Vera Rubin agentic-inference scale-up contract、model-serving pipeline contract 与 Transformers
  v5.8.1。保留 MARLIN 全文证据与低分政策
  边界。2026-08-14 完成 31/31 最终 disposition，并将长期机制整合到 Ch59、Ch63、Ch67、Ch72、
  Ch77；Qwen-Image-2.0 的 Ch23 独立 Gate 同步计入，其余 owner 完成具体论点级复核。

## Open Questions

1. 环境目标与 latency SLO 冲突时，谁定义可接受的 regional policy？
2. MinT 的 policy revision retirement、cache invalidation、multi-region readiness 与 rollback 分别由谁拥有？
3. Packed MoE LoRA layout 如何避免 loader 优化变成跨 runtime 的 format lock-in？
4. HarnessAudit 的 disputed accounting 修正后，resource/object scope 与 message-content flow 的排名是否稳定？
5. 同周是否有真实 trace、facility telemetry 或 serving runtime 论文能复核 MARLIN 的 simulation branch？
6. Workload-Aware Scheduling 在 heterogeneous / dependency-heavy PodGroup 上的 search completeness、rollback
   与 fairness 如何度量？
7. safety summary 的真实 false-positive prevalence、retention duration 与 user correction/delete contract 是什么？
8. Fleet Intelligence 的 telemetry schema、sampling、managed-service retention 与 attestation freshness contract
   能否获得可复核文档？
9. Vera Rubin 的异构 execution branch 怎样绑定 request/KV/intermediate-state identity、transfer completion、
   capacity balancing、fallback 与 end-to-end tail SLO；在 matched workload 下何时不如同构执行？

## Sources

- “MARLIN,” submitted 2026-05-13: https://arxiv.org/abs/2605.13496
- Anthropic Research index, scenario entry dated 2026-05-14:
  https://www.anthropic.com/research
- Hugging Face Papers, 2026-W20 discovery index: https://huggingface.co/papers/week/2026-W20
- MinT: https://arxiv.org/abs/2605.13779
- MinT PDF: https://arxiv.org/pdf/2605.13779
- MinT SDK: https://github.com/MindLab-Research/mindlab-toolkit
- MinT open runtime: https://github.com/verl-project/verl-mint
- MinT cookbook: https://github.com/MindLab-Research/mint-cookbook
- δ-mem: https://arxiv.org/abs/2605.12357
- Self-Distilled Agentic Reinforcement Learning: https://arxiv.org/abs/2605.15155
- Qwen-Image-2.0 Technical Report: https://arxiv.org/abs/2605.10730
- Training Long-Context Vision-Language Models Beyond 128K: https://arxiv.org/abs/2605.13831
- RubricEM: https://arxiv.org/abs/2605.10899
- EVA-Bench: https://arxiv.org/abs/2605.13841
- EVA-Bench HTML: https://arxiv.org/html/2605.13841
- EVA-Bench code: https://github.com/ServiceNow/eva
- EVA-Bench dataset: https://huggingface.co/datasets/ServiceNow-AI/eva
- MemEye: https://arxiv.org/abs/2605.15128
- MemEye HTML: https://arxiv.org/html/2605.15128
- MemEye code and benchmark harness: https://github.com/MinghoKwok/MemEye
- MemEye project page: https://minghokwok.github.io/MemEye/
- MemEye dataset: https://huggingface.co/datasets/MemEyeBench/MemEye
- WildClawBench: https://arxiv.org/abs/2605.10912
- ToolCUA: https://arxiv.org/abs/2605.12481
- EvolveMem: https://arxiv.org/abs/2605.13941
- EvolveMem HTML: https://arxiv.org/html/2605.13941
- EvolveMem code: https://github.com/aiming-lab/SimpleMem/tree/main/EvolveMem
- MemLens: https://arxiv.org/abs/2605.14906
- MemLens PDF: https://arxiv.org/pdf/2605.14906
- MemLens code and evaluation harness: https://github.com/xrenaf/MEMLENS
- MemLens memory-agent reproduction notes: https://github.com/xrenaf/MEMLENS/tree/main/memory-agent
- MemLens dataset and schema: https://huggingface.co/datasets/xiyuRenBill/MEMLENS
- Hugging Face Papers, 2026-W21 curation-lag cross-check: https://huggingface.co/papers/week/2026-W21
- Anti-Self-Distillation: https://arxiv.org/abs/2605.11609
- Anti-Self-Distillation HTML: https://arxiv.org/html/2605.11609
- Anti-Self-Distillation code and recipes: https://github.com/FloyedShen/AntiSD
- Video2GUI: https://arxiv.org/abs/2605.14747
- Video2GUI PDF: https://arxiv.org/pdf/2605.14747
- Video2GUI project and artifact index: https://github.com/WeiminXiong/Video2GUI
- WildGUI reprocessed annotations and screenshots: https://huggingface.co/datasets/xwm/WildGUI
- π-Bench: https://arxiv.org/abs/2605.14678
- π-Bench HTML: https://arxiv.org/html/2605.14678
- π-Bench project page: https://simplified-reasoning.github.io/Pi-Bench/
- π-Bench code and benchmark artifact: https://github.com/Simplified-Reasoning/Pi-Bench
- Full Attention Strikes Back: https://arxiv.org/abs/2605.16928
- Auditing Agent Harness Safety: https://arxiv.org/abs/2605.14271
- Auditing Agent Harness Safety HTML: https://arxiv.org/html/2605.14271
- HarnessAudit project page: https://harnessaudit.github.io/
- HarnessAudit code and benchmark runner: https://github.com/UCSB-AI/HarnessAudit
- HarnessAudit dataset: https://huggingface.co/datasets/LCZZZZ/HarnessAudit
- Process Rewards with Learned Reliability: https://arxiv.org/abs/2605.15529
- BetaPRM official code: https://github.com/JinYuanLi0012/Beta-Binomial-PRM
- Kubernetes PSI Metrics GA（published 2026-05-12；accessed 2026-08-12）:
  https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
- Kubernetes node metrics reference（accessed 2026-08-12）:
  https://kubernetes.io/docs/reference/instrumentation/node-metrics/
- Kubernetes Workload-Aware Scheduling（published 2026-05-13；accessed 2026-08-12）:
  https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/
- Kubernetes scheduling API reference（accessed 2026-08-12）:
  https://kubernetes.io/docs/reference/kubernetes-api/scheduling/
- Kubernetes Service `externalIPs` deprecation（published 2026-05-14；accessed 2026-08-12）:
  https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/
- Kubernetes Mixed Version Proxy Beta（published 2026-05-15；accessed 2026-08-12）:
  https://kubernetes.io/blog/2026/05/15/kubernetes-1-36-feature-mixed-version-proxy-beta/
- Kubernetes CCM route-sync metric（republished as 2026-05-15；accessed 2026-08-12）:
  https://kubernetes.io/blog/2026/05/15/ccm-new-metric-route-sync-total/
- OpenAI TanStack supply-chain incident response（published 2026-05-13；accessed 2026-08-12）:
  https://openai.com/index/our-response-to-the-tanstack-npm-supply-chain-attack/
- OpenAI cross-conversation safety summaries（published 2026-05-14；accessed 2026-08-12）:
  https://openai.com/index/chatgpt-recognize-context-in-sensitive-conversations/
- NVIDIA Fleet Intelligence GA（published 2026-05-11；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=116707
- NVIDIA Fleet Intelligence Agent（accessed 2026-08-12）:
  https://github.com/NVIDIA/fleet-intelligence-agent
- NVIDIA Vera Rubin agentic-inference scale-up contract（published 2026-05-14；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=116892
- NVIDIA model-serving pipeline contract（published 2026-05-12；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=116526
- Transformers v5.8.1 release（released 2026-05-13；accessed 2026-08-12）:
  https://github.com/huggingface/transformers/releases/tag/v5.8.1

## 2026-08-14 Final Source-Family Books Integration Ledger

Qwen-Image-2.0 的 2026-08-13 独立 Gate 已并入本账本。最终计数为 31/31：25 Refine、4 No Change、
2 Weekly Only。

| Source Family | Final Disposition | Stable Owner | Current / Legacy | Books Review Result |
| --- | --- | --- | --- | --- |
| MARLIN | No Change | `PLATFORM-COST` | Ch70 / Ch66 | cost vector 已允许 energy/carbon/water；缺真实 trace 与 SLO guardrail，不写统一权重 |
| Global AI leadership scenarios | Weekly Only | — | — | 政策情景，不是技术机制证据 |
| MinT | Refine | `PLATFORM-MODEL-REGISTRY` | Ch59 / Ch55 | adapter file→immutable policy revision→catalog/cache/readiness lifecycle 已吸收 |
| δ-mem | Refine | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | frozen backbone 上 associative state/correction 分支已按 fixed-state identity 与干预边界复核 |
| Self-Distilled Agentic RL | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | privileged self-teacher 只作 detached bounded auxiliary signal，RL outcome 仍是 authority |
| Qwen-Image-2.0 | Refine | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | representation/generation interface 与 modality identity 已吸收；benchmark 不外推 |
| Long-Context VLM Beyond 128K | Refine | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | token/patch、long-document sampling 与 task mixture 共同塑造能力，不归因于长度常数 |
| RubricEM | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | stage-specific rubric credit 与 reflection state 服从 hard outcome gate |
| EVA-Bench | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | user simulator 自身进入 validation，average/at-least-once/repeated success 分离 |
| MemEye | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | visual evidence granularity 与 reasoning depth 正交诊断；caption gap 不等于 pixel 必然最优 |
| WildClawBench | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | subject 已包含 model+harness+tools+budget+environment+scorer |
| ToolCUA | Refine | `AGENT-TOOL-CALLING` | Ch78 / Ch74 | GUI/tool 是互补 action branches；switch policy、success gate 与真实 API boundary 已复核 |
| EvolveMem | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | retrieval configuration 是 versioned derived policy，需 held-out evaluation 与 rollback |
| MemLens | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | raw evidence、write representation、retrieval、answer representation 与 scorer 分解 |
| Anti-Self-Distillation | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | conditional-PMI proxy、bounded shaping 与 teacher-cost boundary 已覆盖 |
| Video2GUI | Refine | `TRAIN-DATA` | Ch27 / Ch23 | video→task/action/grounding/state-change compilation 保留 lineage 与 release identity |
| π-Bench | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Proactivity 与 Completeness 分开；Act/Silent/Stop 与越权风险共同测量 |
| Full Attention Strikes Back / RTPurbo | Refine | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | dense→calibrated sparse runtime 是训练/校准分支，不用 operator speedup替代 serving contract |
| HarnessAudit | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | harness subject、hidden audit artifact、normalized trace 与 snapshot evidence 已吸收；冲突数字排除 |
| Process Rewards with Learned Reliability / BetaPRM | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | reward mean 与 evidence concentration 分离；concentration 不是 correctness probability |
| Kubernetes PSI Metrics | Refine | `PLATFORM-MONITORING` | Ch67 / Ch63 | utilization→pressure evidence；unsupported 必须 missing 而非 zero |
| Kubernetes Workload-Aware Scheduling | Refine | `PLATFORM-GPU-SCHEDULER` | Ch63 / Ch59 | template→snapshot→whole-group score→atomic commit，保留 staleness/rollback/fairness |
| Kubernetes Service externalIPs deprecation | Refine | `PLATFORM-SECURITY` | Ch72 / Ch68 | insecure default 经 admission guard、迁移窗口再移除；不把 deprecation 当即时安全完成 |
| Kubernetes Mixed Version Proxy | Refine | `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | upgrade compatibility 属于 version-aware control-plane routing，不代表 schema 等价 |
| Kubernetes CCM route-sync metric | No Change | `PLATFORM-MONITORING` | Ch67 / Ch63 | attempt counter 不能替代 success、latency、correctness，已由 metric/evidence boundary 覆盖 |
| OpenAI TanStack incident | Refine | `PLATFORM-SECURITY` | Ch72 / Ch68 | dependency→endpoint→credential→artifact/signing→forced-upgrade response chain 已吸收 |
| OpenAI cross-conversation safety summaries | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | purpose-limited derived state、source lineage、scope、correction/expiry/delete 已吸收 |
| NVIDIA Fleet Intelligence | Refine | `PLATFORM-MONITORING` | Ch67 / Ch63 | telemetry、health verdict 与 attestation 分层；产品效果不外推 |
| NVIDIA Vera Rubin agentic-inference contract | Refine | `INFER-GPU-MEMORY` | Ch54 / Ch50 | heterogeneous execution 必须绑定 request/KV/state transfer 与 tail SLO；只作官方工程证据 |
| NVIDIA model-serving pipeline contract | No Change | `INFER-TENSORRT-LLM` | Ch49 / Ch45 | conversion/build/load/readiness 生命周期已有具体论点 |
| Transformers v5.8.1 | Weekly Only | — | — | Patch-level Version Fact，无新长期机制 |

### Owner Review

15 个 owner 被修改或重新验证：`PLATFORM-COST`、`PLATFORM-MODEL-REGISTRY`、
`MODEL-LONG-CONTEXT`、`TRAIN-GRPO`、`MULTIMODAL-REPRESENTATION`、
`PLATFORM-EVALUATION-SYSTEM`、`AGENT-TOOL-CALLING`、`AGENT-MEMORY`、`TRAIN-DATA`、
`PLATFORM-MONITORING`、`PLATFORM-GPU-SCHEDULER`、`PLATFORM-SECURITY`、
`PLATFORM-FOUNDATIONS`、`INFER-GPU-MEMORY` 和 `INFER-TENSORRT-LLM`。其中 13 为 Refine owner，
另两个仅做 No Change 复核；owner 名单多于实际修改文件数。

本周实际新增或强化 adapter policy lifecycle、pressure/health/attestation evidence、workload snapshot、
supply-chain incident response 和 purpose-limited derived safety state。其余 Refine family 已在 typed credit、
multimodal representation、Evaluation subject、tool orchestration、Memory derived policy 与 long-context 分支中
逐项复核，没有复制论文摘要。Archive/Discovery Gate 只因 cross-index recall 保持 Open。
