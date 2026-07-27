# AI Research Weekly — 2026-W21

> Coverage Window: 2026-05-18～2026-05-24
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 2026-08-14 Source-Family Books Gate Complete; 31/31 final dispositions; 22 Refine, 6 No Change, 3 Weekly Only; 17 Stable Node owners changed or revalidated; Historical Archive/Discovery Gate Open

## Executive Summary

> **Access-history note（superseded 2026-08-13）**：旧段落中 SkillsVote、LongLive-2.0、WorldKV 与
> QUEST 的 blocked 描述保留为 recovery history；current status 以 Candidate Scoring 和四项 Full Source
> Review 为准：30/30 个 `20+` families 已审完，0 blocked，0 pending。

旧版 W21 只保留三项机构研究，不能证明完整论文和工程候选池。本轮恢复 21 个 in-window
学术 families，并识别 6 个应回拨 W20 的 curation-lag spillbacks；W22 feed 又补回 6 个
first-public date 落在 05-20～05-22 的条目，W23 feed 再补回 NITP v1 05-24。本周 baseline 集中出现“从 benchmark 到真实任务”的证据：Google ERA 继续推进 computational
discovery；OpenAI 报告模型参与离散几何 conjecture 反例；Anthropic 公开 exploit-development
能力测量与 Project Glasswing 更新。共同趋势是能力评测逐步要求可执行 artifact、专家复核
和风险控制，但不能由少数成功案例推断普遍自治能力。

OpenComputer 已完成论文、全部主要实验、self-evolving verifier ablation、limitations、Appendix
case studies、公开仓库入口与 Ch62/77/80 邻接审计。HRM-Text 也已完成全文、Appendix、训练与
evaluation contract、公开实现入口及 Ch16～18/23～25 邻接审计。前者把 benchmark construction 的主约束从
“先生成任务，最后找 judge”反转为“先定义可检查状态，再生成可执行环境和任务”。这是对
Ch62 executable evidence 的重要机制补强；后者把固定、逐层独立的 depth 扩展为参数共享的双时间尺度
recurrence，但结果同时依赖 task-formatted data、response-only loss、PrefixLM 与 credit-horizon policy，
暂定补强 Ch17 而不是证明 recurrence 普遍优于标准 Transformer。两者在全历史 Gate 关闭期间均不写
Books。Code as Agent Harness 的全文与 companion bibliography 也已审计；它提供了有用的 interface /
mechanism / multi-agent taxonomy，但没有 systematic-review protocol、独立实验或可执行 harness artifact，
且其稳定系统主张已由 Ch62、Ch74～75、Ch77～78、Ch80 具体拥有，故为章节级 `No Change`。DelTA 已完成唯一 v1、全部方法与
Appendix、主实验/消融/敏感性/开销、当前代码仓库 surface 及 Ch28～30 邻接审计；它把 sequence-level
advantage 下的 token 权重从长度/熵/未来影响扩展为正负 reward-side 的相对梯度几何，但 proxy、batch
composition、额外前向和单次训练 run 限制使其只能暂定 Ch29 refine / Experimental。SkillsVote 与
LongLive-2.0 的 primary text 当前均不可访问，已转入 blocked backlog；OSCAR 已完成 35 页 v1、全部理论/系统/实验附录、
官方 SGLang-based artifact 与 Ch40～43/45/50 邻接审计；它把 KV quantization 的优化目标从 raw tensor
reconstruction 前移到 downstream attention distortion，并用 mixed-precision page lifecycle 与 fused kernel
保持 serving compatibility，暂定 Ch41 refine / Experimental。EnvFactory 也已完成唯一 v1、全部附录、
公开生成/训练 artifact surface 与 Ch62/74/77/79/80 邻接审计；它把真实 API、LLM simulator 与 document-seeded
synthetic environment 之间的折中推进为 source-grounded executable state、dependency-aware trajectory synthesis、
SFT cold start 与 composite-reward RL 的联合数据链，但内部 tests 不证明真实 API behavior conformance，暂定
Ch77 refine / Experimental。Mix-Quant 已完成唯一 v1、完整方法/实验、phase-wise ablation、当前 two-commit
repository、pinned vLLM submodule 与 NIXL launch path 审计；它把 phase differentiation 从不同 batch/SLO
扩展为不同 execution precision，并要求 initial KV storage/layout 对 Decode 兼容，但作者约 3× 数字只属于
RTX 5090 Prefill latency，不含 TTFT、transfer、queue 或 goodput，暂定 Ch51 refine / Experimental。ACC
随后完成 v1/v2 全文、全部附录、dataset/model cards 与 Ch22～25/62/77 邻接审计：它不是在原始交互
轨迹上补一次 observation loss，而是把 answer-verified trajectory 编译成另一份 direct-answer long-context
SFT data。该分支能加强 evidence integration，却会丢失 action/observation temporal structure，并引入成功
轨迹选择、teacher rationale、SWE privileged patch、provenance 与 contamination 风险；暂定 Ch23 refine /
Experimental，Ch22/25/62/77 只做短 handoff。其余 12 项保持 current-review pending，不能把 discovery
feed 摘要算作全文审计。GoLongRL 随后完成唯一 v1 的 39 页全文、全部相关 Appendix、公开训练代码、
evaluation harness、dataset/checkpoint cards 与 Ch22/23/28～30/62 邻接审计。它把长上下文 RLVR 从
retrieval-centric binary reward 扩展到九类 capability-native metrics，再以 task-level variance normalization
与 within-task difficulty weighting 控制异构 reward 的梯度尺度；但 task-level normalization 不会修复样本量
失衡，且 benchmark-guided dataset refinement、model-solvability filtering、query-only 13-gram 去重、单次训练
与无独立 validation 的 alpha 选择限制了外推。暂定 Ch29 refine / Experimental。其余 11 项保持
current-review pending，不能把 discovery feed 摘要算作全文审计。WorldKV 的 official project page 与
two-commit Apache-2.0 repository 已完成 artifact-level 核验，但 15 MB primary paper full text 在当前路径
无法完整读取；约 2× throughput、full-KV fidelity、evaluation/ablation/limitations 均不据摘要外推，转入
`Unverified / Blocked Backlog`，不计 Full Source Review 且不阻塞 forward cursor。其余 10 项保持
current-review pending。PlanningBench 随后完成 v1/v2 metadata、27 页 v2、全部 Appendix、official
one-commit repository、467-row evaluation dataset/license 与 Ch23/24/61～63/76～78 邻接审计。它把
planning benchmark 从 fixed instances 推进到 task/constraint taxonomy、closed-loop difficulty 与 checklist
verification，但 generator/checklist/judge 的共享 ontology、未发布的 300-row training data、单 critic、默认
推理参数、未披露 hardware/seed 及 benchmark 兼作 reward source 限制了外推。Ch23 与 Ch62 已分别覆盖
constraint-derived data 和 rubric/global-validity contract，故为 `No Change — Already Covered`。Gated
DeltaNet-2 随后完成唯一 v1、完整正文与 Appendix A～E、official seven-commit implementation surface 及
Ch14～15/17/22/39～40/45 邻接审计。它把 fixed-state linear attention 的全局 decay、key-side erase/read
与 value-side write 拆成三个控制面，并给出 compact-WY chunk training、gate-aware backward 与 recurrent
Decode 的实现闭环；但证据只覆盖 1.3B、100B-token、4K-training / 2K-SWA、single-H100 throughput 与单次
训练，不能推出普遍替代 dense Attention。暂定 Ch22 `Refine — Existing Argument / Experimental`，其余 8 项
current-review pending。Post-Trained MoE / ZEDA 随后完成 v1/v2、全文与 Appendix A～D、official
16-commit training/evaluation surface、两份 checkpoint cards 及 Ch21/25/40/45/52 邻接审计。它把已完成
post-training 的 static top-k MoE 转为 dynamic compute：注入 parameter-free zero-output experts，以 frozen
original model 做 SFT→on-policy distillation，再用 normal/zero 两组间的 balancing constraint 控制 compute，
而不把 normal-expert routing 强行均匀化。约 20% 只属于单 H200、8192 sequence、concurrency 32 的作者
phase-throughput contract；暂定 Ch21 `Refine — Existing Argument / Experimental`，其余 7 项 pending。
SkillOpt、Foundation Protocol 与 SciAtlas 随后逐项完成全文、appendix、official artifact surface 与目标/
相邻章节审计。SkillOpt 暂定 Ch80 refine / Experimental；Foundation Protocol 的稳定机制已由 Ch68/69/
77～80 具体拥有，故为 `No Change`；SciAtlas 的 tri-path recall、typed graph expansion 与 RWR 暂定 Ch72
refine / Experimental，但没有 quantitative retrieval benchmark、baseline/ablation、hardware/cost/load/
freshness SLO，且 11/12 edge schema 与 current repository revision 不能消解。QUEST 又因 28.7 MB full paper
无 HTML、当前 permitted path 无法完整取得而转入 blocked backlog；official project/repository/model/data
surface 不代替全文。ThriftAttention 随后完成唯一 v1、完整方法、kernel 设计、全部 benchmark / ablation /
limitations、official artifact surface 与 Ch39～41/45/50 邻接审计。它不是把 FP4 或 sparse attention 写成
FP16 的替代，而是在保持全部 attention support 的 FP4 路径上，为每个 query block 动态提升少量 key
blocks 到 FP16，再把两条路径合并进同一 online-softmax state；这使 precision policy、paired cache identity、
selector 与 fused kernel 成为一个系统 contract。作者结果仅证明单 RTX PRO 6000、指定模型/长度/任务下的
quality recovery 与 latency，不证明生产 goodput、SLO 或跨硬件可迁移；dual cache 还增加 28% KV footprint，
可能反向压缩并发。因此暂定 Ch45 refine / Experimental，Ch39～41/50 只作 handoff。当前为 `19/21`
accessible Full Source Reviews、4 项 blocked backlog、2 项 current-review pending。SkillEvolBench 又完成唯一
v1、完整 protocol/results/capacity/cost/family catalog、current runnable benchmark surface 与 Ch62/73/76/80
邻接审计。它把 replay/local repair 与 frozen deployment transfer 分开，并用 No-Skill、Raw-Trajectory、
curated/self-generated、failure-only/always-update 与 forced Tier-3 controls 暴露 selective abstraction bottleneck：
更多更新和更大 library 既可能扩大覆盖，也可能固化 episode-specific drift 与 retrieval burden。暂定 Ch73
refine / Experimental，Ch62/76/80 只作 handoff；没有 seed/variance/significance、hardware/token/runtime contract，
且 benchmark family、curated seed 与 verifier 由同一团队设计，不能把平均百分点外推为通用 Agent 规律。
在 NITP 审计前为 `20/21` accessible Full Source Reviews、4 项 blocked backlog、1 项 current-review pending。NITP 最后
完成 v1～v3、全文/附录、official repository 与 Ch23～25 邻接审计：它在标准 token-level NTP 之外增加
`t -> t+1` 的 shallow-state stop-gradient cosine target，把 representation geometry 变成可训练约束；但
理论只在 fixed target、局部高 alignment、GGN 与 well-conditioned projector 假设下成立，训练实验也缺少
硬件/精度/multi-seed/置信区间。尤其 v1 的 45B MoE Appendix 已从 v2/v3 移除，当前 repository 仍声明代码
尚未发布，因此 45B 与可复现实现均不得作为当前证据。NITP 暂定 Ch24 `Refine — Existing Argument /
Experimental / Revision-sensitive`，Ch17 只承接 representation handoff。至此 `21/21` accessible Full Source
Reviews 完成、4 项 blocked backlog、0 项 current-review pending；W21 forward Evidence Gate 通过，游标进入
W22；全历史 Evidence Gate 与 Historical Books Gate 继续保持打开/关闭状态。

本段前文保留了 Source Review 逐项完成时的 count-down 轨迹；其中“其余 N 项 pending”是中间
检查点，不是本周最终状态。fixed official / Infra replay 又恢复 6 个 in-window families：OpenAI content
provenance 把可剥离的 C2PA metadata、较耐变换的 SynthID 与 public verifier 分成互补 signals，并明确
negative result 不能证明内容非 AI；NVIDIA verified skills 把 capability artifact 的 source、scan、skill card、
signature、catalog 与 sync 串成 pre-admission chain，但签名与扫描均不等于运行时安全。NVIDIA Slurm
topology-aware scheduling 则把 W18 的 block-topology mechanism 推进到 5,000-node simulator 中的 segment
policy；仿真结果只能在 20,000 GPUs、15,000 jobs、七天与 2.5% nodes-down contract 下成立。Agent evaluation
guide 与 Transformers v5.9.0 只强化已有 trajectory/version-contract 观点；token-metered reference architecture
是低分商业部署叙事。至此 W21 当前队列为 0，fixed-source checkpoint 通过，Historical Books Gate 仍关闭。

## Coverage and Source Coverage

- 模型与研究机构：保留 Google 5 月 19 日、OpenAI 5 月 19～20 日、Anthropic 5 月 22 日；新增的
  content-provenance 条目已联读官方 verification boundary，不从信号缺失推导 negative conclusion。
- 论文与学术来源：重放 Hugging Face W21（页面覆盖 05-17～05-23），逐项以 arXiv v1 日期归周；
  恢复 21 个 W21 families，6 项回拨 W20。OpenComputer、HRM-Text、Code as Agent Harness、DelTA、OSCAR、EnvFactory 与 Mix-Quant 完成全文及
  artifact/repository-surface 审计；ACC 另完成 v1/v2、Appendix A～F 与 Hugging Face dataset/checkpoint
  surface 审计；GoLongRL 完成 39 页唯一 v1、全部相关 Appendix、official code/data/checkpoint 与 evaluation
  surface 审计；PlanningBench、Gated DeltaNet-2、Post-Trained MoE/ZEDA、SkillOpt、Foundation Protocol 与
  SciAtlas 也完成 primary text/artifact/章节邻接审计；WorldKV 只完成 official project/repository
  artifact-level 核验，paper full text blocked；Scholar、
  OpenAlex、DBLP 与 formal publication cross-check 仍 pending。
- AI Infra：已重放 NVIDIA 与 Transformers 的 in-window official Blog/release surfaces，新增 verified skills、
  Slurm topology-aware scheduling、Agent evaluation、Transformers v5.9.0 与 token-metered reference
  architecture；后者低于长期 retained threshold。Kubernetes/vLLM/SGLang/KServe 未发现需要新增的
  in-window retained stable-release family；这不是所有 PR 的 exhaustive absence proof。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Model-assisted discrete-geometry result | 4 | 3 | 3 | 5 | 3 | 4 | 22/30 | Scientific milestone |
| Exploit-development capability measurement | 3 | 5 | 4 | 4 | 5 | 4 | 25/30 | Must Read |
| Empirical Research Assistance | 3 | 3 | 4 | 4 | 3 | 4 | 21/30 | Worth Watching |
| HRM-Text | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Must Read — full review complete |
| Code as Agent Harness | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Worth Watching — full review complete / No Change |
| DelTA | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Must Read — full review complete / Experimental |
| SkillsVote | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Source Review complete；provisional R / Ch80 / Experimental |
| LongLive-2.0 | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Full Source Review complete；provisional R / Ch32 / Ch34 handoff / Experimental |
| OpenComputer | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete |
| OSCAR | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete / Experimental |
| EnvFactory | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read — full review complete / Experimental |
| Mix-Quant | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read — full review complete / Experimental |
| ACC | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Must Read — full review complete / Experimental |
| GoLongRL | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Must Read — full review complete / Experimental |
| WorldKV | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch41 / Experimental |
| PlanningBench | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Worth Watching — full review complete / No Change |
| Gated DeltaNet-2 | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Must Read — full review complete / Experimental |
| Post-Trained MoE Can Skip Half Experts | 5 | 5 | 4 | 4 | 5 | 2 | 25/30 | Must Read — full review complete / Experimental |
| SkillOpt | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review complete；provisional R / Ch80 / Experimental |
| Foundation Protocol | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Source Review complete；No Change / Ch80 |
| SciAtlas | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch72 / Experimental |
| QUEST | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Source Review complete；provisional R / Ch23 / Experimental |
| ThriftAttention | 5 | 5 | 4 | 4 | 5 | 2 | 25/30 | Full Source Review complete；provisional R / Ch45 / Experimental |
| SkillEvolBench | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Source Review complete；provisional R / Ch73 / Experimental |
| NITP | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full Source Review complete；provisional R / Ch24 / Experimental / Revision-sensitive |
| OpenAI layered content provenance | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch68 |
| NVIDIA-verified Agent Skills | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full review complete — provisional Refine Ch80 / Ch68 handoff |
| NVIDIA Slurm topology-aware scheduling simulation | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full review complete — provisional Refine Ch59 / Official Engineering Evidence |
| NVIDIA Agent evaluation guide | 2 | 4 | 4 | 4 | 5 | 3 | 22/30 | Full review complete — No Change / Ch62 |
| Transformers v5.9.0 | 3 | 4 | 4 | 5 | 3 | 2 | 21/30 | Full review complete — Weekly Only / Version Fact |
| NVIDIA token-metered AI services reference architecture | 2 | 3 | 3 | 4 | 3 | 3 | 18/30 | Low-score boundary complete — Record Only |

当前账目为 31 行：19 个 `25～30`、11 个 `20～24`、1 个 `<20`。评分只决定阅读优先级，
不等于最终 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows | 3 | 3/3 `20+` Full Source Reviews retained |
| Recovered in-window families | 28 | 27 个 `20+` academic/official/Infra families 已完成 Full Source Review；1 项低分边界完成；0 blocked / current-review pending |
| Recorded `20+` candidates | 30 | 19 high / 11 mid；六维合计已复算 |
| Earlier-week spillbacks | 6 | 按 arXiv v1 date 回拨 W20，不在 W21 重复计分 |
| Academic discovery window | Open | HF first pass complete；Scholar/OpenAlex/DBLP/formal cross-check pending |
| Official / Infra discovery window | Fixed-source checkpoint passed | OpenAI / NVIDIA / Transformers in-window official surfaces replayed；cross-index 与 exhaustive PR absence proof 仍开放 |
| W21 Forward Evidence Gate | Passed | 30/30 `20+` Full Source Reviews complete；1/1 low-score boundary complete；0 blocked / current-review pending；academic cross-index replay 仍使全历史 Evidence Gate 保持 Open |

## Deep Analysis — Security Evaluation 必须测量可执行链

漏洞知识问答只测 recall；exploit development 要求 reconnaissance、environment setup、
code generation、execution、debugging 与 validation。能力提高的同时，sandbox、target
identity、authorization、artifact retention 和 misuse control 都进入 evaluation contract。
这是从 static benchmark 到 executable workflow 的 `Direct Evolution`，但具体成功率仍绑定
目标软件、工具、时间预算与模型版本。

### OpenComputer：先确定可验证状态，再合成任务

GUI benchmark 早期依赖人工编写 task 与 screenshot/LLM judge，在任务少、界面状态可见时合理；
当任务扩展到 office、IDE、terminal、browser 与 creative software 时，真实成功往往藏在文件、
metadata、SQLite、application API 或持久 side effect 中，像素“看起来正确”不再等于状态正确。
OpenComputer 将设计顺序反转：每个应用先建立 typed inspection endpoints 和 executable checkers，
经过 unit/integration test；再用固定 calibration trajectories 对比 programmatic verdict 与 reference
judgment，只允许修 verifier/checker/documentation，不允许改 trajectory、task objective 或 final state；
最后才生成 `task = instruction + environment initializer + success criteria`。

```text
human-curated task + visual judge
→ executable state checker
→ verifier-aware environment/task synthesis
→ fixed-trajectory disagreement diagnosis
→ bounded verifier repair with versioned evidence
```

收益是 task success 与 partial credit 都能回溯到具体 application state，且 verifier 也成为可测试
artifact；代价是 checkable-state bias、application schema drift、checker bugs 与 visual/geometric criteria
覆盖不足。论文在 120-task human comparison 上看到 hard-coded verifier 更一致，并在 450 个 calibration
tasks 中报告 verifier repair，但这些数字只属于 33 apps、作者任务生成器和指定 agents；不能证明
programmatic checker 等于 ground truth，也不能外推 Agent 的生产自治能力。旧的人工/visual branch
仍适用于无法稳定表达成结构化状态的任务。关系是 `Direct Evolution`，主 owner 暂定 Ch62，Ch77/80
只需说明 environment、verifier 和 run identity 的接口。

## Evidence Level

机构报告与公开 artifact 能证明具体研究事件；OpenComputer 的全文和 artifact 证明一个具体
verifier-grounded synthesis/evaluation pipeline，不证明所有 desktop state 可程序化、所有 verifier
正确或所有 Agent 能力。HRM-Text 的论文和公开实现支持一个 1B、4,096 context、task-formatted
pretraining contract 下的层级递归分支；它不证明相同收益能扩展到更大模型、更长上下文、通用 raw-text
pretraining 或生产 serving。Code as Agent Harness 是 narrative survey：它能建立分类、术语和研究问题，
不能证明所列系统在同一 workload 上的因果优劣；companion repository 是持续更新的 bibliography，
不是论文机制的可执行复现。DelTA 的论文与当前代码仓库支持一个基于 batch reward-side 梯度 proxy 的
token reweighting 机制，以及在指定 Qwen3/Olmo3、数学与代码合同下相对所列 baseline 的作者实验；它不
证明得到真实 causal/process credit，也没有多 seed 训练证据。OSCAR 的证据绑定指定模型、H100、
layout 与 kernel contract；EnvFactory 的证据绑定作者生成的 85 个 executable environments、Qwen3
post-training 与四个 benchmark/harness，它只证明内部 artifact tests、state transition 和所列训练合同下的
作者结果，不证明 synthetic environment 与真实 API 语义等价，也没有多 seed 或完整真人 intent-distribution
证据。Mix-Quant 证明在指定 Blackwell/vLLM、model/benchmark 与三次运行合同中，Prefill-only NVFP4
通常比 full-pipeline NVFP4 保留更多质量，并在 RTX 5090 的 isolated Prefill latency 上加速；它不证明
end-to-end TTFT、TPOT、goodput、transfer economics、其他硬件或所有 Agent workload，同样没有显式
Limitations/Threats section。ACC 的作者实验支持在 Qwen3-30B-A3B-Thinking、10,802 条编译样本、
131,072 sequence length 和 avg@3 harness 下，混合 Search/SWE/SQL 的 direct-answer SFT 改善指定
long-range dependency tasks；它不证明 masked observation 是唯一因果瓶颈，不证明通用 Agent policy
改善，也不能用 question-only embedding separation 排除 evidence、answer、template 或 benchmark leakage。
其 attention/router heatmap 是 post-hoc observation，不是获得能力的因果机制证据。其余 accessible
`20+` 候选均已有后文非模板化 Full Source Review；四项无法取得 primary text 的候选继续明确标记
`Unverified / Blocked Backlog`，不从摘要或 project page 推导机制。

## Cross-Week Deduplication

6 月 N-day exploit 研究是同一 security-evaluation program 的后续，不重复记录为新问题。W21 feed
中的 Anti-Self-Distillation、Video2GUI、π-Bench、Full Attention Strikes Back、Auditing Agent
Harness Safety 与 Process Rewards with Learned Reliability 按 v1 date 归 W20；推荐日期不建立新事件。
W22 feed 中 SkillOpt（2605.23904，05-22）、Foundation Protocol（2605.23218，05-22）、
SciAtlas（2605.22878，05-20）、QUEST（2605.24218，05-22）、ThriftAttention（2605.23081，
05-21）与 SkillEvolBench（2605.24117，05-22）也属于 W21，已回拨并按各自可访问范围完成 Full
Source Review 或 blocked boundary；推荐日期不建立第二个事件。
W23 feed 中 NITP（2605.24956）v1 为 05-24，归 W21；其 07-02/07-12 revisions 不建立新事件。

## Knowledge Tree Position

Ch14/16/17/18 Model Architecture → Ch23/24/25 Data/Objective → Ch21/22 Long Context/MoE → Ch29 RLVR → Ch39/41 Prefill/KV →
Ch62 Evaluation → Ch68 Security → Ch74 Tool Calling → Ch77 Workflow → Ch80 Agent Platform。

## Recommended Action

W21 Source-Family Books Gate 已完成；后续只处理 cross-index Archive backlog。新增长期机制由 owner 章节维护：
Ch17 双时间尺度 recurrence；Ch21 post-trained zero-route MoE；Ch45 attention-aware/mixed-precision KV；Ch55
phase-aware precision handoff；Ch66 verifier-first benchmark synthesis；Ch72 layered content provenance；Ch84
Skill pre-admission；Ch63 topology segment scheduling。其余已验证论文按最终账本复核现有论点；survey、guide、
scientific milestone 和版本事实不为制造 diff 强行写入。

## Event-Date Daily Decision

2026-05-19、05-20、05-22：Weekly only。

## Books Integration Decision

`Source-Family Books Gate Complete`。31/31 final dispositions：22 `Refine — Existing Argument`、
6 `No Change — Already Covered`、3 `Weekly Only / Record Only`。17 个 Stable Node owners 完成修改或具体
论点级复核；WorldKV 的独立 Gate 已并入本周总账。所有 Experimental/Revision-sensitive 机制保持 model、
hardware、precision、length、artifact 与 SLO 边界；作者 benchmark、simulation 和被后续 revision 移除的
NITP 45B Appendix 均未写成通用事实。详细 disposition 见文末 ledger。

## Ignored Noise

把单个数学成果归因于“完全自治”，或忽略 human selection、verification 与工具环境。

## 2026-07-31 Full Re-Audit Addendum

- Exploit-development evaluation 已全文复核。能力证据从 textual answer/PoC 演进为分层、
  可执行 artifact 与 programmatic grader；verifier、sandbox 和 target version 也成为评估
  对象，已写入 Ch62。
- discrete geometry 与 Empirical Research Assistance 仍是科研里程碑/使用证据，不改变
  Books 的系统机制。

## Full Source Review

### Model-assisted discrete-geometry result — 22/30

- **Source Family / Date / Coverage**：`MODEL-ASSISTED-DISCRETE-GEOMETRY`；OpenAI 2026-05-20
  milestone、关联 proof/artifact 与作者说明已核对；覆盖问题、模型建议、人类筛选、形式化论证和
  独立数学验证边界。
- **Evidence Boundary / Decision**：可证明模型参与了一个具体反例/证明工作流，不能估计跨数学
  领域自治能力或将人类 problem selection/verification 隐去。Ch62/77 已读；
  `No Change — Already Covered`。

### Exploit-development capability measurement — 25/30

- **Source Family ID / Type / Date**：`EXPLOITBENCH-EXPLOITGYM-SCONE`；Anthropic
  2026-05-22 full research report，联读 ExploitBench、ExploitGym、SCONE-bench 与 Glasswing
  方法/安全说明。
- **Full-read Coverage**：已覆盖 V8/smart-contract targets、16-tier capability ladder、Baseline/
  Nudged harness、300-turn budget、randomized replay、programmatic grader、model comparisons、
  cheating checks、limitations 与 artifact-handling boundary。
- **Problem / Previous Design / Changed Constraint**：knowledge QA 和 crash PoC 对早期模型便宜且
  安全，但无法区分“知道漏洞”与“能组合 exploit primitives”；能力上升后 evaluation object 必须
  是可执行 chain，而非文本答案。
- **Mechanism / Ownership / Flow**：固定 vulnerable/patched target 和 harness；agent 迭代代码；
  differential execution、challenge-response、random heap layout 与 static transcript scan 分层验收。
  benchmark owner 拥有 target/version，sandbox 拥有权限，grader 拥有 capability state，security
  owner 决定 artifact retention/disclosure。
- **Evaluation Boundary**：报告证明相同 harness/turn budget 下的特定 target capability；不证明
  internet-connected 攻击、所有 vulnerability classes、真实 campaign success 或一般自治。Nudging、
  scaffold、toolchain 和 target selection 都是 capability 的组成部分。
- **Trade-offs / Evolution**：text→PoC→primitive→end-to-end exploit 提高 ecological validity，
  同时增加危险 artifact、sandbox escape、grader gaming、版本漂移与复现访问控制。旧静态 eval
  仍适合早期筛查。关系为 `Direct Evolution`。
- **ROADMAP / Chapters / Decision**：Ch62 主 owner，已读 Ch61～63、Ch68、Ch74、Ch77；当前
  Ch62 已写入 executable artifact ladder。`No Change — Already Covered`。

### Empirical Research Assistance — 21/30

- **Source / Coverage**：Google Research 2026-05-19 official program report、case artifacts 与
  human-review description 已核对。
- **Evidence / Decision**：具体研究 case 证明 workflow 可提供辅助，不提供统一 baseline、失败率或
  autonomy definition。Ch55/62/77 已读；`Weekly Only — Version/Product Fact`。

### OpenComputer — 28/30

- **Candidate / Week / Source Family**：`OPENCOMPUTER-VERIFIER-GROUNDED-SOFTWARE-WORLDS`；
  W21；arXiv:2605.19769v1，2026-05-19。当前只有 v1；Hugging Face 推荐日 05-20 不替代
  first-public date。
- **Direct / Related Primary Sources**：arXiv metadata、HTML/PDF 正文与 Appendix；作者公开
  `echo0715/OpenComputer` 仓库的 `verifiers/`、`smoke/`、`task_generator/`、`computer_env/`、
  `evaluation/` 结构、backend/agent contract 和运行说明。仓库当前状态用于机制/artifact 可访问性
  核验，不能证明所有文件在 v1 发布瞬间均为相同 revision。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、problem setup、
  verifier generation、inspection channels、test protocol、self-evolving verification、task synthesis、
  evaluation harness、release、全部 main experiments、GUI/CLI analysis、verifier ablation、Conclusion、
  Limitations，以及 Appendix A 的 schema-drift repair、Appendix B 的 visual/terminal failure cases、
  Appendix C task examples；并核对公开仓库的执行顺序、sandbox backends、run artifacts 和 limits。
- **Original Problem / Why Previous Design Was Reasonable**：人工任务与 screenshot/LLM judge 在任务少、
  UI 结果可见且人工复核可承担时合理；它保留开放语义和视觉判断。但跨 33 类 desktop apps 扩展时，
  task initialization、persistent files、metadata、hidden application state 与 custom verification 同时
  成为 bottleneck，像素近似正确会掩盖单元格、数据库、terminal scrollback 与 side-effect 错误。
- **Changed Constraint / Principle**：环境只有在 target state 可重建且 success criteria 可审计时才是
  可扩展的 training/evaluation substrate。Verification 不应是任务生成后的附加 judge，而应约束
  environment 和 task synthesis；同时 verifier 自身也是可能漂移、失效和被 reward-hack 的版本化程序。
- **Mechanism**：每个 application 先枚举 state surfaces，经 CDP、D-Bus、UNO、AT-SPI、SQLite、
  file parser 等稳定 channel 生成返回 JSON 的 query/check endpoints，并执行 positive/negative unit 与
  live integration tests。约 15 个 easy/medium calibration tasks 让强 agent 产生固定 final states；LLM
  reference 与 programmatic verdict 按 criterion 对齐，只把 verifier-attributed disagreements 送入最多
  三轮 bounded repair。之后 generator 先提出 user goal，再按 complexity/data-generatability 过滤、与
  verifier 对齐并生成 `task = instruction x + initializer e + checks c`。Fresh sandbox 执行 screenshot-
  action loop，最终 reward 为 passed checks 的比例，并保存完整 trajectory/artifacts。
- **State Ownership / Control Flow / Data Flow**：benchmark owner 持有 app/version、task schema、verifier
  interface 与 release policy；sandbox backend 持有 initial/final application state 和 isolation；agent 只
  提交 actions；checker 持有 machine verdict；reference judge 只为 verifier debugging 提供 signal，不能
  在固定 trajectory 上改写目标；repair loop 只修改 checker/endpoint/docs。数据流为 `goal proposal →
  verifier-aware task/initializer → fresh sandbox run → final state → executable checks → criterion evidence →
  bounded verifier diagnosis/repair`。
- **Implementation Details**：公开 artifact 保持 `verifier → smoke → task generation → evaluation` 顺序；
  E2B、local Docker 与 remote Docker 共享 Ubuntu/XFCE app stack。Run 保存 trajectory、screenshots 与
  report，agent registry 和 environment backend 通过接口扩展。论文 case 显示 darktable schema 从单库
  假设漂移为跨 `library.db`/`data.db` join；修复保持 public checker interface 与固定 trajectory 不变，
  说明 schema identity 和 checker internals 必须分开版本化。
- **Evaluation Contract**：1,000 finalized tasks、33 apps、平均 17.7 verifier endpoints/app、6.9 checks/task；
  proprietary agent 走官方 API，公开模型除 Kimi-K2.6 外使用 2×H100。主表同时报告 full success、平均
  criterion reward、steps 与 seconds/step；OSWorld-Verified 只是外部 reference，并非 matched task set。
  verifier comparison 使用 120 trajectories 的 human labels；repair ablation 对 450 calibration executions、
  最多三轮，159 个 disagreement 中 76 个判为 checker-side，68 个在预算内修复。
- **What the Evidence Proves**：作者系统证明 inspectable application state 可以联合约束 verifier、task
  generation、sandbox initialization 与 evaluation，且固定 trajectory 上的 disagreement 可暴露一类
  checker defect。它也证明 full success 与 partial progress、visual plausibility 与 underlying state、
  agent failure 与 verifier failure 必须分开记录。
- **What It Does Not Prove / Threats to Validity**：human comparison 只有 120 tasks，reference judgment
  本身可能错；生成器偏向已有 endpoints 可检查的任务，形成 checkability bias。17 个含不可程序化
  visual criteria 的 tasks 被排除主 benchmark；因此结果不覆盖 layout/geometry 等开放视觉目标。
  OSWorld 数值没有 matched environment，不能作严格模型退化因果证据。公开 repo 可执行性不等于
  论文所有数字已由本轮独立复现，也不证明 checker 对 adversarial reward hacking 完备。
- **Trade-offs / New Failure Modes**：programmatic state inspection 提高可重复性，却引入 app/schema
  version drift、endpoint privilege、cross-database consistency、checker regression、secret/PII capture、
  task distribution 被 verifier coverage 塑形，以及 repair loop 过拟合固定 calibration states。LLM judge
  从 final oracle 降为 diagnostic signal，降低不可审计性，但仍可能错误归因 verifier/agent failure。
- **Where Previous Design Still Applies / Evolution**：视觉审美、几何关系、开放语义或不可访问内部状态
  仍需 human/LLM judgment；低风险小任务也可能不值得维护 application-specific verifier。演进关系为
  `Direct Evolution`：hand-authored task/visual judge→executable final-state checker→verifier-aware task and
  environment synthesis→bounded checker evolution；相对 Workflow/Agent Platform 是 `Layering / Dependency`。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch77、Ch80 及其相邻接口。Ch62 已拥有
  `artifact + environment + trace`、versioned verifier 和 evaluator failure；缺口是 verification-first
  synthesis、固定 trajectory 上只修 checker 的 ownership boundary、checkability bias 与 schema-drift
  repair。Ch77 已拥有 deterministic spine，Ch80 已拥有 run/environment identity，不应重复主论证。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`，主 owner
  Ch62，Ch77/80 只需短 handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：如何为 verifier
  release 建立 regression corpus；怎样组合 structured state 与 visual judgment 且保持 calibration；repair
  authority 如何防止“修 checker 迎合 agent output”；跨 app/version 的 task identity 怎样 supersede。

### HRM-Text — 26/30

- **Candidate / Week / Source Family**：`HRM-TEXT-HIERARCHICAL-RECURRENT-PRETRAINING`；W21；
  arXiv:2605.20613v1，first-public 2026-05-20，当前无后续 revision。联读作者 `sapientinc/HRM-Text`
  repository、1B checkpoint/model surface 与此前 HRM 架构来源；后发 artifact 用于核对公开实现，不能
  反推 v1 当日每个文件的 revision。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Related Work、完整 Methods、MagicNorm、
  truncated backpropagation 与 warmup、task-completion objective、PrefixLM、训练数据、主结果、matched-
  compute architecture/objective ablations、representation/gradient diagnostics、contamination、Discussion、
  Conclusion、Appendix A～D；并核对公开代码中的 dual-module recurrence、PrefixLM two-pass attention、
  FSDP2 training path、checkpoint/config surface 与 Apache-2.0 license。
- **Original Problem / Why Previous Design Was Reasonable**：标准 Transformer 用互不共享参数的 layer
  depth 换取单次 forward 内的表达容量，数据充分、硬件擅长规则 dense stack、Serving 需要固定 latency
  时非常合理；单时间尺度的 shared-weight loop 又能以较少参数增加 compute。约束变化在于：小模型、
  固定训练 FLOPs 与 task-formatted data 下，希望把更多计算深度放进 recurrent state，而不是继续扩大
  参数量，但必须控制重复 Jacobian 带来的 activation/gradient instability 和 credit horizon。
- **Mechanism / State Ownership**：模型把约一半参数放在 slow high-level module `H`，另一半放在 fast
  low-level module `L`；每个 high-level cycle 内先执行三次 `L` update，再执行一次 `H` update，总共两个
  cycles。`H/L` hidden state 是同一 sequence 内的 latent recurrent state，由 model forward 拥有，不是
  KV Cache、跨请求 memory 或可持久化 reasoning trace。MagicNorm 在 recurrent step 的 forward 边界
  归一化 state，同时只让 backward 穿过长度为 `K` 的截断窗口；训练先用 `K=2`，再线性 warm up 到
  `K=5`，以偏置梯度估计换取稳定性与显存上界。
- **Control Flow / Data Flow / Objective**：`task-formatted prompt → bidirectional PrefixLM prompt encoding →
  H/L recurrent updates → causal response generation → response-only NLL`。Prompt tokens 提供条件但不计
  loss；response tokens causal。Prefix 区域的双向 attention 与 response 区域的 causal attention 需要
  两段 attention path，因此架构收益与 loss-mask、attention-mask 和数据格式是联合结果，不能只归因于
  recurrence。公开实现用内部 Pre-Norm blocks、module-final norm、RoPE、SwiGLU 和 static KV helper
  映射该合同。
- **Training / Implementation Contract**：论文区分 40B unique tokens 与因重复/分层采样形成的 60B
  actual training tokens；初始 corpus 为 176.5B tokens、593.7M documents，并以 reasoning、math、code、
  instruction-response 与 synthetic data 为主。1B 配置由两个 16-layer modules、hidden size 1,536、head
  size 128、vocab 65,536、context 4,096 组成，bf16、global batch 196,608 tokens、Adam-atan2、2,000-step
  warmup 后常数 `2.2e-4`，16×H100 上连续训练约 46 小时。作者按每 H100-hour 2 美元估算约 1,472 美元；
  这不是经审计的全栈成本，也不包含数据生成、teacher、清洗、失败实验或工程人力。
- **Evaluation Contract / Baselines / Ablations**：主实验在约 `1e21` FLOPs 下比较 HRM、Looped
  Transformer、RINS 与 Transformer branches；recurrent models 使用 60B actual tokens，而 1B Transformer
  因单 token compute 较低在同 FLOPs 下使用 170B tokens。评估 context 上限 3,072、temperature 0、无
  system prompt；部分 baseline 来自论文、部分来自公开权重重跑，因而不是完全统一的 data、tokenizer、
  objective、harness 与 training pipeline。architecture、attention-mask、loss-mask ablations 显示
  response-only objective 与 PrefixLM 自身贡献显著，HRM 再提供增量；只发布一个 final checkpoint，
  没有多 seed、error bar 或训练轨迹 checkpoint。
- **What the Evidence Proves**：在作者公开的 1B、窄 task-formatted distribution、固定 FLOPs 与评估
  harness 中，层级递归可以与 forward-state normalization、截断 credit horizon、PrefixLM 和 response-
  only objective 共同形成一个优于所列 matched-compute baselines 的点。representation-difference、cosine
  和 logit-lens KL diagnostics 说明 recurrent steps 的 hidden states 确有变化；full-BPTT diagnostics 也显示
  少数 gradient-tail spikes，使截断策略具有直接动机。
- **What It Does Not Prove / Threats to Validity**：它不证明 hidden-state 变化等于可解释的“planning”，
  不证明 biological hierarchy，不能把与外部大模型相差 96～432× compute、100～900× tokens 的异构比较
  当作相同训练合同下的效率结论。task-formatted/synthetic distribution、移除部分 `<think>` 内容和
  teacher-produced data 可能转移上游计算成本；DROP 在较短 n-gram 检查出现 contamination signal。
  结果未覆盖大于 1B、长于 4,096 context、广泛 factual/code/Agent/tool/safety workloads、线上 TTFT/TPOT、
  吞吐、KV reuse 或 failure recovery。
- **Trade-offs / New Failure Modes**：参数共享用更少 parameters 购买更多 sequential recurrent compute，
  但增加固定 inference work、难以按请求提前结束、state numerical drift、截断梯度 bias 与 horizon tuning。
  PrefixLM 提高 prompt 内双向可见性，却改变常规 decoder-only mask，并可能削弱标准 causal prefix/KV
  cache 的复用兼容性。连续单次 run 没有中间 checkpoint/crash recovery；若发生故障或 loss spike，训练
  trajectory 的可恢复性弱。Appendix 的 auto-guidance 只在 benchmark grid-search 后取得很小增益，不能
  当作无选择成本的默认推理策略。
- **Where Previous Design Still Applies / Evolution**：规则 independent-layer Transformer 在规模化训练、
  固定 serving graph、成熟 kernel/parallelism 和广域数据上仍是主分支；单时间尺度 loop 在不需要显式
  slow/fast state 时更简单。关系暂记 `Direct Evolution`：`independent layer depth → shared looped depth →
  dual-timescale recurrence + bounded credit horizon → future adaptive recurrent depth`。PrefixLM/objective
  相对 recurrence 是 `Layering / Dependency`，不是同一演进轴。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch16～18 与 Ch23～25。Ch17 已拥有可堆叠 layer、
  normalization/residual/gradient-path contract，却假设不同 layers 通常不共享参数，尚未解释参数共享
  recurrence、multi-timescale state 与 forward/backward horizon 分离；故主 owner 为 Ch17。Ch18 已拥有
  causal mask 与 loss-mask interface，Ch24 拥有 pretraining objective/compute contract，Ch25 拥有 response-
  only loss，三章只需短 handoff；Ch22 的 recurrent context state 是跨 token/context continuity，不应与
  本论文同一 forward 内的 latent recurrence 混写。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch17，Ch18/24/25 仅短 handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：大模型
  scale 与多 seed 是否保留收益；adaptive depth 如何定义 stop/rollback；PrefixLM 与 production prefix/KV
  cache 如何共存；truncated credit bias、task-formatted distribution 与 upstream synthetic-data cost 如何
  单独归因。

### Code as Agent Harness — 23/30

- **Candidate / Week / Source Family**：`CODE-AS-AGENT-HARNESS-SURVEY`；W21；arXiv:2605.18747v1，
  first-public 2026-05-18，当前无 revision。联读作者 companion repository
  `YennNing/Awesome-Code-as-Agent-Harness-Papers`；该仓库是持续更新的 curated bibliography，包含
  `TODO`/`MISSING_URLS` 等维护面，不是可执行 harness、benchmark 或实验 artifact。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、scope boundary、Harness Interface 的
  reasoning/acting/environment 三类角色、Planning/Memory/Tool/PEV Control/Adaptive Harness Engineering、
  single-to-multi-agent scaling、shared representation/convergence、五类 application domain、全部 seven open
  problems 与结尾 research agenda，并核对 companion taxonomy。论文无独立 Method、Implementation、
  Evaluation、Ablation、Limitations 或 Appendix；正文也未披露检索式、时间/venue window、纳入排除规则、
  双人编码或 inter-rater agreement，故不能把“representative systems”视为系统性文献 census。
- **Original Problem / Why Previous Design Was Reasonable**：把 code 视为 model output 足以研究单次程序
  生成；把 prompt、tools、memory、sandbox 视为外围 glue，也适合短任务和人工兜底。当 Agent 跨多步修改
  repository、执行工具、接收反馈、持久化状态并由多个角色协同时，输出程序、执行环境、验证器和共享
  workspace 开始共同决定行为；只评模型或 final patch 会隐藏 runtime/state failure。
- **Mechanism / Taxonomy**：论文将 `code` 限定为 executable 或 machine-checkable artifacts，包括程序、
  API/schema、tests、formal spec、repository、simulator、config 与 execution-produced traces/logs；明确排除
  raw perception、physical state、human intent 和 latent reasoning 本身。三层 taxonomy 是：`interface`
  将 reasoning/action/environment 映射为可执行对象；`mechanisms` 用 planning、memory、tools 与 Plan–Execute–
  Verify 调节长期 trajectory；`scaling` 用 repository、tests、traces、blackboard 和 workflow state 组织
  multi-agent roles、feedback 与 convergence。
- **State Ownership / Control Flow / Data Flow**：作者主张 plan 应成为带 files/invariants/checks/rollback
  points 的 contract；sandbox 拥有 bounded execution state，policy gateway 拥有 permission tier，deterministic
  sensors 提供 evidence，workflow/harness 拥有 termination 和 repair routing，human approval 拥有跨越
  safety boundary 的 authority。多 Agent 共享的是 versioned program artifacts 与 execution evidence，
  message 只能传递 proposal；论文进一步提出 future transactional state 应声明 read/write set、assumptions、
  version dependencies、verifier obligations 与 conflict policy。
- **Implementation / Evaluation Contract**：这是 position-oriented survey，不提供统一 implementation 或
  evaluation contract。各表把不同年代、模型、任务、工具、sandbox 和 scorer 的系统并列分类，不能做
  matched comparison；个别引用系统的 benchmark 数字只是二手汇总，本 Source Review 不将其提升为本
  论文实验。companion repository 能核对 taxonomy 对应的 paper links，但不能验证引用研究的 claims、
  completeness、发布日期或可复现性；这些若进入 Books 仍需回到各自 primary sources。
- **What the Evidence Supports**：论文支持一套有用的概念边界：base-model capability、system-provided
  harness 和 agent-created executable artifact 是三个不同对象；code-mediated state 可以比纯对话更可执行、
  可检查、可持久化；最终成功率会混合 retrieval、tools、retry、sandbox、verifier 与 environment；自演化
  harness 应像 safety-critical code change 一样拥有 change contract、held-out regression、canary 和 rollback。
  这些是跨文献综合和研究议程，不是新系统的实验性证明。
- **What It Does Not Prove / Internal Tensions**：论文不能证明 code 是所有 Agent domain 的充分或唯一
  substrate，也不能证明更 formal shared state 必然导致更简单 topology。正文一处把 execution-grounded
  signals 描述为不会 hallucinate，后文又正确承认 tests、static analyzers、GUI checkers、simulators 和
  generated tests 都可能是不充分 oracle；稳定结论应是 execution 产生可重放 evidence，而非自动产生
  ground truth。其“topology complexity 与 state formality 负相关”等观察没有 census denominator、控制
  变量或统计检验，只能视为作者 hypothesis。
- **Trade-offs / New Failure Modes**：code 将语义压缩为 schema、test 或 pass/fail 时会丢失 intent、开放
  质量与物理风险；repository/log/blackboard 分别在 fidelity、latency、context cost、authority、staleness
  和 merge conflict 上付费。Agent-created tools/skills/verifiers 又扩大 supply-chain、权限升级、reward
  hacking 与 self-modification 风险。复杂任务需要 code 与 perception、human goal、policy、semantic review
  和 physical feedback 分层，而不是用 executable artifact 覆盖这些 owner。
- **Where Previous Design Still Applies / Evolution**：短、低风险、无副作用且可人工复核的任务仍可用
  prompt + simple tool loop；open-ended semantics 仍需要 human/model judgment。演进关系是 `Layering /
  Dependency`：`model output → executable artifact → artifact inside governed PEV loop → shared versioned
  substrate → transactional semantic state (research agenda)`；它不是单一产品替代史，也没有实验支持最后
  一步已经实现。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch68、Ch74、Ch75、Ch77、Ch78、Ch80。
  Ch74 已规定 model output 只是 proposal、tool contract 与 side-effect class；Ch75 已把 plan 定义为带
  precondition/evidence 的状态转移假设；Ch77 已拥有 deterministic spine、durable state、evaluator-driven
  loop、retry/approval/replay；Ch78 已区分 message 与 authoritative shared state、typed handoff 与 delegation；
  Ch62 已拥有完整 subject/harness identity 与 oracle boundary；Ch80 已用 control/execution/evidence planes
  收束完整 Agent runtime。survey 没有暴露这些章节尚未覆盖的新机制。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered`，主去重位置 Ch80，
  机制 owner 保持 Ch62/74/75/77/78，不在 Books 重复增加“code as harness”总括段。Historical Books Gate
  继续关闭。未来若有实现 transactional semantic state、量化 conflict/rollback cost 或 controlled harness
  mutation 的 primary research，再按具体机制 owner 复审，而不是引用 survey 作为证明。

### DelTA — 26/30

- **Candidate / Week / Source Family**：`DELTA-DISCRIMINATIVE-TOKEN-CREDIT-RLVR`；W21；
  arXiv:2605.21467v1，first-public 2026-05-20，当前无后续 revision。联读作者 `RUCBM/DelTA`
  repository；仓库当前公开 9 commits、基于 veRL 的实现目录与 `run_DelTA.sh` 训练入口，但无 tag/release，
  因而只能作为 current artifact surface，不能反推 v1 发布日的精确 code revision。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、Preliminaries、完整 local
  first-order derivation、centroid/refinement/temperature/coefficient 算法、weighted DAPO objective、全部主
  实验、training dynamics、显著性、within-side/top-bottom/component/proxy ablations、Related Work、
  Conclusion、Appendix A～L 的统一 gradient view、proof、complexity、implementation、完整训练/evaluation
  settings、baseline details、overhead、Olmo3/code/OOD/sensitivity/token-cloud 分析，并核对当前仓库的安装、
  veRL/SGLang 依赖和训练入口。仓库网页未暴露 versioned release 或完整 artifact manifest，故不把代码
  surface 当作独立复现实验。
- **Original Problem / Why Previous Design Was Reasonable**：GRPO/DAPO 在只有 response-level verifier
  reward 时，把同一个 group-relative advantage 广播到 response tokens；这在没有 process labels、希望保留
  简单 on-policy objective 时合理。response-balanced GRPO 防止长回答支配每个 response 的权重，token-
  balanced DAPO 又允许长 CoT 中每个有效 token 直接贡献梯度。约束变化是长 trajectory 内的大量格式、
  共享背景和低信息 token 也会得到相同 advantage，sequence correctness 无法说明哪些 token-gradient
  directions 真正区分成功与失败。
- **Mechanism / Math**：论文在旧策略附近把 DAPO update 写成 advantage 加权的 token-gradient vector
  之和。对正、负 advantage tokens 分别建立 centroid；一个 token 到自身侧与对侧 centroid 的相对平方
  距离形成 discriminative score，再用 entropy-regularized sigmoid soft assignment 和 side-specific adaptive
  temperature 得到权重。默认执行一次 stop-gradient centroid refinement，随后把系数约束到 `[0.8,1.2]`
  并 self-normalize 总系数质量，再代入 weighted DAPO surrogate。它估计的是 batch 内 reward-side 的
  相对 gradient geometry，不是 token 的语义重要性、因果 process reward 或忠实 reasoning trace。
- **State Ownership / Control Flow / Data Flow**：rollout batch 拥有 sampled tokens、binary rewards 与
  group advantages；old-policy actor pass 提供 log-probability 及 final-layer hidden state；DelTA estimator
  拥有 stop-gradient proxy、正负 centroid、adaptive temperature 和 coefficient snapshot；trainer 在同一批
  optimization epochs 中固定使用该 snapshot，新 rollout 使其失效并重算。可扩展 proxy 用
  `(1-p_t(y_t))h_t` 近似 final LM-head-row gradient，避免保存完整 parameter gradient；这是 frozen-
  representation approximation，不等价于 full-gradient credit。
- **Implementation / Evaluation Contract**：主实验以 DeepMath-103K、VeRL、SGLang、binary
  `math-verify` reward 训练 Qwen3-8B/14B-Base；8×B200，global batch 128、microbatch 32、每 prompt 16
  rollouts、prompt/response 上限 2,048/20,480、bf16、temperature/top-p 1/1、learning rate `1e-6`、KL
  coefficient 0。8B/14B 分别训练 220/300 steps，checkpoint 由 AIME25 avg@8 最高值选择；评估最大长度
  30,000、temperature 1、top-p 0.7，每题 16 samples。作者还以 Olmo3-7B、code dataset 与 OOD tasks 做
  补充，但并未披露 production SLO、跨节点 topology 或完整能耗/成本合同。
- **Baselines / Ablations / Sensitivity / Overhead**：baseline 包括 DAPO、high-entropy Forking Tokens、
  smooth-clipping SAPO 与 future-influence FIPO。within-side-only 低于 DAPO，top-half coefficients 优于
  full-token、bottom-half 退化，支持“对侧比较”在该实验中的必要性；adaptive temperature、entropy
  regularizer、self-normalization、bounded mapping 和 one-step refinement 均有 component ablation。扩大
  coefficient range 变化较小，而 `K=2/3` 低于默认 `K=1`，提示多轮 refinement 可能过拟合 batch geometry。
  因长 response hidden-state cache 显存过高，默认 `K=1` 需要 `K+2=3` 次额外 actor forwards 估计系数；
  作者仅在 8×B200 的首个 training step 报告额外 37 秒、约占 DelTA 首步 10.2%，不能外推稳态吞吐。
- **What the Evidence Proves**：在作者给定模型、数据、二值 verifier、rollout、checkpoint-selection 与
  evaluation contract 下，reward-side relative gradient-proxy reweighting 相对所列 same-scale baselines
  提高作者报告的数学 aggregate，并在 Olmo3、code 与 OOD 补充实验保持同方向；top/bottom 与 component
  ablations 说明收益并非由任意随机 token weight 产生。它建立了 outcome reward 下不依赖 process labels
  的一条 token weighting 设计分支。
- **What It Does Not Prove / Threats to Validity**：没有多次独立训练 seed；16 次 Mann–Whitney test 只
  测 repeated-generation randomness，不测 training-run variance。checkpoint 用 AIME25 选择，而 AIME25
  同时进入报告 suite，使该项并非纯 held-out selection。proxy 忽略 representation 对参数的完整导数，
  coefficient 依赖当前 batch 的正负组成和 centroid quality；数学主实验、binary reward 与 task-specific
  verifier 不能证明开放领域、learned reward、multi-turn Agent 或生产训练同样成立。token cloud 是忽略
  context 的定性聚合，也不能将高权重 token 解释为真实“关键推理步骤”。
- **Trade-offs / New Failure Modes**：相对直接 DAPO，DelTA 增加 hidden-state cache 或额外 actor passes、
  centroid/temperature state、batch composition sensitivity、proxy bias 和 denominator/clamp edge cases；某一
  reward side 样本少或方向多峰时，单 centroid 会压缩结构。bounded weights 控制方差却限制 credit contrast，
  多轮 refinement 又可能追随 batch noise。coefficient snapshot 必须和 rollout/old-policy identity 对齐，
  否则表面正常的 loss 会混用不同 gradient geometry。
- **Where Previous Design Still Applies / Evolution**：GRPO 在 response-level fairness、低附加状态和实现
  简洁优先时仍成立；DAPO 在长 CoT 需要 token-balanced aggregation 且不愿承担 proxy passes 时更直接；
  Forking Tokens 与 FIPO 分别编码 uncertainty fork 和 future influence，不是 DelTA 的落后版本。演进关系
  暂记 `Direct Evolution`：`response-level group advantage → response-balanced token averaging → token-
  balanced long-CoT aggregation → entropy/future-influence token selection → own-vs-opposite reward-side
  gradient-proxy weighting`。这些分支可以按 workload 共存，而不是线性替代。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch28～30。Ch28 已拥有 terminal reward 的 token credit
  问题和 value baseline；Ch29 已解释 GRPO group advantage、sequence reward 广播、token/response
  normalization 与 verifier contract，但更细粒度 credit 只作为概念入口，尚未拥有 batch reward-side
  gradient geometry、coefficient lifecycle 与 proxy-cost 边界；故主 owner 为 Ch29。Ch30 的 offline pair
  margin 不使用 on-policy rollout，不应承接该机制。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch29；Historical Books Gate 关闭，本轮不修改 Books。待验证：多 seed 与 held-out model
  selection；learned/noisy reward 下 centroid 是否稳定；混合正负稀疏 batch 的 empty-side policy；proxy 与
  full gradient 的误差；额外 actor passes 在多节点长 CoT 训练中的 memory/throughput 成本。

### SkillsVote — 23/30 — Full Source Review Complete

- **Candidate / Week / Source Family**：`SKILLSVOTE-SKILL-LIFECYCLE`；W21；候选索引指向
  arXiv:2605.18401，记录的 first-public date 为 2026-05-18。
- **Access / Full-read Coverage**：2026-08-13 恢复 arXiv HTML，覆盖 collection、profile、recommendation、
  task attribution、evolution、evaluation、ablations、schemas、prompts 与 limitations；并核对 Agent Skill / ClawHub
  等外部 skill formats 作为 compatibility boundary。当前实现 artifact 与 immutable event-time snapshot 未披露。
- **Problem / Mechanism / State Ownership**：静态 skill directory 适合人工维护的小库；当 skill 数量、框架差异和
  trajectory 数增长时，目录发现、环境适配与错误 credit assignment 会使“成功一次”被错误升级成通用 procedure。
  SkillsVote 把 lifecycle 拆成 collection→profiling→recommendation→subtask attribution→evolution：profile 保存 OS、
  write scope、privilege、dependency、quality 与 verifiability；recommendation 只输出真实 skill identity 与 usage boundary；
  attribution 以 semantic subtask 而非 command/trajectory 为单位，区分 environment/human/unknown judge、主要责任与
  reusable delta；只有成功且可复用的 attributed evidence 才能修改 library，失败/不确定证据只用于 diagnosis。
- **Evaluation / Boundary / Trade-offs**：Terminal-Bench 2.0 与 SWE-Bench Pro 在指定 Codex/GPT harness、模型、
  skill library 和 evaluator 下支持 lifecycle 组件的相对收益，不证明不同框架、权限或领域迁移。LLM profiling 与
  attribution 会引入成本、self-confirming bias、skill contamination、版本漂移与错误 supersession；unknown/human
  outcomes 仍需要人工门禁。旧的人工 curated 小库在高风险、低变更率场景更透明。
- **Evolution / Chapters / Decision**：`static directory → retrieval/recommendation → execution evidence attribution →
  validation-gated evolution` 是 Ch80 的 `Direct Evolution`，Ch62/73/77 作 evaluation/memory/workflow handoff。已读
  Ch62、Ch73、Ch77、Ch80；provisional `Refine — Existing Argument / Experimental`。Historical Books Gate 关闭，
  不修改 Books。待核验 runnable artifact、event-time revision、multi-run uncertainty、adversarial skill、rollback/delete
  与跨 framework identity translation。

### LongLive-2.0 — 26/30 — Full Source Review Complete

- **Candidate / Week / Source Family**：`LONGLIVE-2-NVFP4-PIPELINE-TRAINING`；W21；候选索引指向
  arXiv:2605.18739，记录的 first-public date 为 2026-05-18。
- **Access / Full-read Coverage**：2026-08-13 恢复 arXiv HTML，已读 AR video / DMD background、NVFP4-aware
  LoRA training、Balanced Sequence Parallel、VAE halo、parallel KV quantization/dequantization、training/inference
  experiments、ablations、dataset construction 与 Appendix；未发现可冻结 event-time code/config 的官方 artifact。
- **Problem / Previous Design / Changed Constraint**：Ring/Ulysses 为规则长序列切分通信与 activation 很合理；但
  teacher-forced AR video 让同一 temporal chunk 同时出现 clean context 与 noisy target，block-sparse mask 又使 naive
  Ulysses 把 clean/noisy 分到不同 rank、复制 VAE preparation，Ring 的平衡假设也不再成立。瓶颈从“序列太长”变成
  workload-specific state placement、mask compilation、VAE halo 与低精度 KV 的联合问题。
- **Mechanism / State / Flow**：Balanced SP 让 rank 按 temporal chunk 共同构造 paired clean/noisy latent，在
  post-All-to-All order 构造 teacher-forcing mask，并以 exact left halo 分片 VAE；NVFP4-aware DMD 只训练 LoRA，
  backbone/score models 与 W4A4 execution co-design；inference 对 weights 与 frame-chunk KV 使用 NVFP4 micro-block，
  K smoothing 后并行 dequantize。通信 topology、temporal ownership、quant scale、master-weight/drop policy 与 KV
  chunk identity 必须共同版本化。
- **Evaluation / Boundary / Trade-offs**：作者在 LongLive-2.0-5B、720p、指定 GPU/steps/VBench/MovieGenBench
  contract 下报告最高 2.1× training、1.8× inference 与 2/3-step FPS；不能外推至其他 DiT、硬件、sequence/mask、
  quality evaluator 或 production SLO。VBench resize/sampling 会改变 resolution 比较；W4A4 与 KV quantization 增加
  scale calibration、kernel portability、quality drift、rollback 与 hardware lock-in。BF16/常规 Ulysses 在短视频、
  规则 mask、可复现优先时仍合理。
- **Evolution / Chapters / Decision**：这是 `generic sequence parallel → workload-shaped balanced ownership →
  quantized compute/KV co-design` 的 `Direct Evolution`。已读 Ch32～36、Ch45/50；主 owner Ch32（communication/
  layout contract），Ch34 与 Ch45/50 handoff。provisional `Refine — Existing Argument / Experimental`；不修改 Books。
  待核验 code、failure recovery、multi-node topology、optimizer/master state、quality confidence intervals 与端到端 SLO。

### OSCAR — 28/30

- **Candidate / Week / Source Family**：`OSCAR-ATTENTION-AWARE-INT2-KV`；W21；
  arXiv:2605.17757v1，first-public 2026-05-18，当前无后续 revision。联读作者
  `FutureMLS-Lab/OSCAR` repository、project page 与 RotationZoo 入口；当前仓库已有 40 commits 和 5 月
  18 日之后的 llama.cpp、vLLM/新模型分支进展，后发内容仅用于识别 artifact 演进，不能归入 v1 事件。
- **Access / Full-read Coverage**：已覆盖 35 页论文的 Abstract、Introduction、Preliminaries、完整离线
  covariance/rotation/clipping 算法、frozen-error theorem 与 proof、SGLang online layout/prefill/decode kernel、
  全部 accuracy/long-context/system experiments、rotation/window/clip/calibration ablations、Conclusion、
  Related Work、Limitations、Broader Impact、Appendix A～E 的数学推导、worked example、algorithm flow、
  full per-run tables；并核对官方仓库的 dump→fit→serve 流程、vendored SGLang snapshots、rotation files、
  runtime flags、model/backend matrix、MIT license 与无正式 tag/release 的 current surface。
- **Original Problem / Why Previous Design Was Reasonable**：BF16 KV 保存完整数值、kernel/layout 成熟且
  不需 calibration，在短 context、低并发或质量风险高时合理。直接 INT2 或 Hadamard/random rotation 继续
  保持固定 shape 和 paged layout，能散布 outliers，也比 channel promotion、residual buffers 或动态 bit
  allocation 更容易融合；但只有四个量化 levels 时，最小化 raw `K/V` reconstruction error 没有区分
  downstream attention 真正敏感的方向，长 history 会累积 logit/output distortion。
- **Mechanism / Math**：key-side 目标由 query second moment `C_Q=Σqᵀq/N` 给出，因为 key error 经
  `QKᵀ` 进入 logits；value-side 用 `C_S=VᵀSᵀSV/N` 近似 attention-weighted output distortion。每层每 KV
  head 对目标矩阵 eigendecompose，分别形成 `U_Q/U_S`，再组合 Hadamard 与 bit-reversal permutation：
  `R_K=U_Q H P_br`、`R_V=U_S H P_br`；per-layer percentile clipping 后做 asymmetric INT2。theorem 只在
  ambient-basis diagonal、rotation/input-independent frozen residual covariance 和 surrogate objective 下给出
  minimizer，不是完整 autoregressive decode 的全局最优证明。
- **State Ownership / Control Flow / Data Flow**：offline calibrator 拥有与 model revision、layer/head shape、
  group size 和 calibration corpus 绑定的 rotations、eigenspectra 与 clip thresholds。runtime 的 logical cache
  被分成 `BF16 sink | INT2 history | BF16 recent`：Prefill 用 fused Triton path 旋转、clip、pack history；
  Decode 新 token 先进入 rotated BF16 staging/recent window，窗口滑动时最老 token demote 到 INT2 page；
  attention kernel 分别读取高/低精度 segments，在浮点累积后复用 online-softmax merge。`R_V` 可吸收到
  projection weights。cache identity 因而必须新增 quant scheme、rotation artifact、clip/group/layout 和 kernel
  version；不同 identity 的 prefix pages 不得误复用。
- **Implementation / Evaluation Contract**：论文主路径使用 SGLang，Qwen3-4B-Thinking/8B 在单张 H100
  80GB、Qwen3-32B 在 2×H100、GLM-4.7-FP8 358B 在 8×H100 TP。accuracy suite 为 AIME25、GPQA-Diamond、
  HumanEval、LiveCodeBench v6、MATH500，max generation 32,768；Qwen3 temperature 0.6、GLM 1.0，top-p
  0.95、top-k 20，Qwen 默认 5 seeds、GLM 3 runs。OSCAR 主配置为 sink 64、recent 256、group 128，
  effective 2.28 BPE 在 128K context 计入 INT payload、scale/zero metadata 和 BF16 windows；因此“约 8×”是
  BF16→INT2 的近似 payload/footprint表述，不等于所有端到端 HBM 都缩小 8×。
- **Baselines / Ablations / Sensitivity**：serving-compatible Group B 比较 BF16、naive INT2/INT4、QuaRot-
  style Hadamard、Saw-INT4 与 TurboQuant；KIVI/Kitty 因缺少作者可用的 paged/fused 32K path，只在共同
  AIME25 setting 引用报告值。TurboQuant 被关闭 mixed precision 且仅单 run，不能当严格 matched baseline。
  `U/H/P_br` decomposition、raw-covariance/random/no-rotation targets、sink/recent window、clip grid 与
  calibration volume/domain 都有消融；其中无高精度窗口的配置在该任务上崩溃，说明结果属于
  attention-aware rotation + clipping + boundary windows + kernel 的联合系统合同，不是 rotation 单因素。
- **Internal Consistency / Artifact Boundary**：正文称参数来自一次约 8,878-token MMLU-style calibration，
  Table 7 却把 8k GPQA-Diamond 标作 default；当前仓库 quick-start 又默认 GPQA、30k dump budget。三者可能
  来自实验/实现演进，但 v1 未解释差异，故 calibration identity 记为 `Disputed Documentation`，不能把
  某一默认值写成稳定事实。仓库 `main` 的 later models、Metal/llama.cpp、preview branches 和 headline
  results 都晚于 v1，不进入本周证据结论。
- **What the Evidence Proves**：在作者的四个 model configurations、H100/SGLang、32K-generation accuracy
  与 100K/128K context serving contracts 内，attention-induced covariance target 相对 raw/data-oblivious
  rotations 显著改善 INT2 quality；decomposition 和 target ablations 直接支持“优化下游 attention distortion，
  而非只重建 cache”这一机制。fused mixed-precision paged path 证明该表示至少能在公开 artifact 中与 prefix
  cache、分页和 decode kernel 共存，并在给定 batch/context 下把降低 KV traffic 转成 latency/capacity收益。
- **What It Does Not Prove / Threats to Validity**：不证明 INT2 在任意 model、RoPE/GQA/MLA/linear-attention、
  dataset、hardware 或 SLO 下保持质量；RULER-NIAH 只测显式 needle retrieval，不覆盖完整 long-context
  reasoning。theory 的 frozen diagonal residual 与全 decode 有缺口；calibration shift、rotation-file corruption、
  multi-tenant prefix identity、failure recovery 和线上 tail latency 未评估。prefix warmup/full-hit 与极长
  100K stress tests 有意隔离 decode/cache capacity，不能直接代表真实到达率、TTFT 或 mixed prefill/decode
  goodput。作者 benchmark、有效 BPE 与 throughput 倍数不进入 Books 通用结论。
- **Trade-offs / New Failure Modes**：OSCAR 用一次 offline QKV dump/eigendecomposition、per-model artifact
  lifecycle、混合精度 page state、demotion path 和专用 Triton kernel 换取容量/带宽收益。calibration drift、
  错 rotation/head mapping、clip mismatch、staging/window off-by-one、BF16/INT2 partial-softmax merge、page
  reuse identity 与 kernel/hardware port 都会产生 silent numerical corruption。固定 uniform history layout
  保持 paging 友好，却牺牲 per-token/channel adaptive precision；更大的 sink/recent window提高质量但侵蚀
  effective bits 和并发容量。
- **Where Previous Design Still Applies / Evolution**：BF16 在质量/可移植性/简单性优先时成立；INT4 或
  channel/mixed-precision paths 在有对应 kernel 且愿意承担复杂 layout 时仍可能更稳；Hadamard-only 在不能
  校准或需要 data-free deploy 时更简单。关系暂记 `Direct Evolution`：`full-precision KV → direct low-bit
  quantization → data-oblivious outlier rotation → attention-aware offline rotation + protected boundary windows
  + page-compatible fused kernel → future adaptive precision / broader hardware`。最后一项仍是研究方向，
  不是 OSCAR 已证明的替代。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch40～43、Ch45 与 Ch50。Ch41 已拥有 KV logical
  bytes、lifecycle、dtype/layout/kernel invariant，却只把 quantization 当容量变量，尚未解释表示误差目标、
  mixed-precision lifecycle 和 calibration artifact identity，故主 owner 为 Ch41。Ch43 拥有 logical-to-
  physical page mapping，只需补充“压缩格式必须保持 page/kernel contract”；Ch45 已拥有 quant/dequant/fusion
  成本清单；Ch50 已区分 reduce bytes 与 improve utilization，二者均只需短 handoff，不重复算法。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch41，Ch43/45/50 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：统一
  calibration contract；非 H100 与不同 attention architecture；真实 prefix-hit/mixed traffic 下 TTFT/TPOT/
  goodput；artifact versioning/rollback 与 corrupted-rotation detection；多租户 cache identity；adaptive precision
  如何在不破坏 paged/fused layout 的前提下加入。

### EnvFactory — 27/30

- **Candidate / Week / Source Family**：`ENVFACTORY-EXECUTABLE-ENVIRONMENT-AND-AGENTIC-RL`；W21；
  arXiv:2605.18703v1、official `LARK-AI-Lab/EnvFactory` repository、公开 models/datasets 与生成/训练入口。
  arXiv 仅有 v1，提交与 first-public date 均为 2026-05-18；当前 repository 是持续演进 artifact，没有
  release/tag，因此只把 paper v1 声明与可定位的公开 surface 视为 W21 evidence，后续代码和数据规模不
  反向改写历史 event。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、Related Work、完整 Method、
  experiments、environment-scaling、direct-RL/query-refinement/reward-weight ablations、Conclusion、Broader
  Impact、Limitations、compute、implementation、data statistics、algorithms 与 prompts；同时核对 repository
  的 environment discovery、schema/metadata/tool/intermediate artifacts、validation/recovery、trajectory
  synthesis、SFT/RL processing 与 serving prerequisites。当前 README 展示的 26.5k/53.4k SFT records 和
  3.09k RL records 与论文 1,622 SFT conversations、953 RL conversations 不是同一计量/版本合同，故标为
  `Versioned Artifact Difference`，不混合成一组训练规模。
- **Original Problem / Why Previous Designs Were Reasonable**：production API/MCP 能提供真实副作用与
  语义，但认证、费用、限流、网络抖动和不可控 drift 不适合高频 RL rollout；LLM simulator 便宜、容易扩展，
  但会 hallucinate state transition；基于文档或已有 task 的 sandbox environment 介于两者之间，在工具集合
  稳定时合理，却受预收集 specification、stateless task 与过度明确 instruction 限制。EnvFactory 不是把
  这些分支判为过时，而是尝试在低延迟、可复现和外部语义 grounding 之间增加新折中。
- **Changed Constraint / Mechanism**：工具 Agent 的瓶颈从“会不会生成 JSON call”移动到可扩展、stateful、
  可重复的 interaction environment 和能表达隐式 intent 的训练 trajectory。每个 environment 定义为
  `e=(metadata, database schema, executable Python implementation, tool interface)`：Search Agent 从公开来源
  建议工具生态；Code Agent 生成 Pydantic state/schema、实现和默认 MCP surface；Test Agent 检查 metadata-
  interface 一致、import/execute、expected result 与 state transition，并在 revision budget 内迭代。参数
  embedding 先建立 tool dependency edges，LLM 再补/删 logical edges；sampler 区分 user-provided external
  parameters 与 tool-derived internal parameters，向后递归补齐依赖（`D_max=3`），再向前扩展 tool chain。
  QueryGen 将 chain 分为每轮 1～5 个 tools，先生成 scenario/profile/database state，再执行 subgoal
  decomposition、goal articulation、implicit reference、action compression、ambiguity 与 related-goal
  expansion；sandbox agent 与 simulated user 产生多个候选，以 trajectory 与 final-state evidence 选择并
  清理冗余调用、标注 non-essential arguments。
- **State Ownership / Control and Data Flow**：外部 source 只拥有参考语义，不拥有 generated behavior；
  environment artifact 拥有本地 schema、database state 与 executable transition；每个 conversation 的
  isolated session/transport 拥有 rollout snapshot；dependency graph 拥有可满足性 proposal；QueryGen 拥有
  scenario、intent 和 planned chain；sandbox execution 才拥有实际 trajectory 与 final state；evaluator 拥有
  trajectory/state/length reward；dataset revision 和 training run 拥有筛选后的 examples、model checkpoint
  与 provenance。控制流为 `source discovery → schema/tool generation → tests/revision → dependency graph →
  topology-aware sampling → query refinement → isolated execution → evidence selection/filtering → SFT → RL`。
  MCP 在这里是 interface/transport，不承担 real-API conformance、authorization 或 workflow correctness。
- **Training / Evaluation Contract**：论文生成 85 environments、842 tools、七个 domains、1,622 SFT 与
  953 RL conversations，平均每个 conversation 4.82 turns、每 turn 3.29 steps。SFT 使用 LlamaFactory，
  Qwen3-4B contract 为 8×80GB、batch 256、LR `1e-6`、三 epochs；后续 RL 从第一 SFT epoch checkpoint
  初始化。RL 使用 VeRL/GRPO，8×80GB、rollout 8、batch 256、max trajectory 16k、max generation 4k、
  十 epochs，每个 interaction turn 作为 sample。reward 同时保留 trajectory match、final-state equivalence
  与 length penalty；`alpha=0.5` 只是在作者 BFCL ablation 中达到最佳峰值，不是通用常数。评估覆盖
  Qwen3 1.7B/4B/8B、BFCLv3、tau2-Bench、VitaBench 与 MCP-Atlas；SGLang inference 默认 TP2，
  non-thinking temperature 0、thinking 0.7。MCP-Atlas 因网络只运行 30/36 servers、291/500 tasks；
  tau2/VitaBench 的 simulated user/evaluator 使用 DeepSeek-V3.2-Chat。
- **What the Evidence Proves**：在作者生成、筛选和评估合同中，SFT cold start 是多数相对增益的主要
  来源，SFT 后 RL 进一步提高聚合结果；direct RL 在部分指标改善但更不稳定。50→75→85 environments
  的 BFCL 曲线支持该受限范围内的正向 scaling trend；250-trajectory refinement ablation 只支持小幅、
  非逐 slice 一致的收益；trajectory-only/state-only reward 均不如作者的混合 operating point。公开仓库
  证明 schema sketch、metadata、executable MCP tools、intermediate checkpoint/resume、graph sampler 与
  data-processing/training surface 存在。
- **What It Does Not Prove / Threats to Validity**：source-grounded design 与内部 generated tests 不证明
  synthetic implementation 和真实 API 在错误码、权限、并发、rate limit、transaction、latency、partial
  failure 或长期 drift 上 behaviorally conformant；“verified”只表示作者定义的 metadata/code/state checks
  通过。LLM 生成的 ambiguity 没有真人 request-distribution validation；tool graph 只保证 schema/LLM 所认定
  的参数可满足性，不保证 semantic task validity。失败 tool calls 在 SFT 前被过滤，削弱 failure recovery
  学习证据；没有披露多 training seeds、显著性检验或 data-matched baseline，AWM/EnvScaler 的 environment、
  task 和 checkpoint contracts 不相同。RL trajectory generator 与部分 benchmark user/evaluator 共享
  DeepSeek-V3.2 family，存在 correlated simulator/judge bias；MCP-Atlas subset 也限制横向比较。Appendix H
  的 prose 称 0.1 概率为 valid parameter 额外引入 prior，但 Algorithm 2 的 condition/comment 组合无法从
  公开文字唯一还原该语义，记为 `Disputed Documentation`，不据此推断实际代码路径。
- **Trade-offs / New Failure Modes**：可执行 synthetic state 换来低延迟、replay 和可程序评分，却新增
  source drift、generated-spec bug、test-oracle co-generation、session cross-contamination、simulator bias、
  synthetic-to-real transfer gap 与 artifact/version sprawl。stateful write tools 要求每个 conversation 独立
  transport/session，限制单 session 并行调用；async 并发只能提高整体吞吐，不能消除该约束。dual reward
  减少“有效路径非唯一”造成的误罚，却引入 trajectory/state 权重、state-equivalence checker、length penalty
  与 reward hacking surface。真实 API 仍适合 final conformance/high-risk validation，LLM simulator 仍适合
  低成本 early exploration，document-seeded sandbox 仍适合 specification 稳定且可人工审阅的领域。
- **Evolution Relationship**：`Layering / Dependency`，不是线性替代：`production API authenticity + LLM
  simulator scalability + document-seeded sandbox repeatability → source-grounded executable stateful artifact
  → dependency-aware multi-turn synthesis → SFT cold start → composite-reward RL → future conformance-tested
  synthetic/real hybrid`。下一阶段压力是把 external-source revision、generated code/tests、session snapshot、
  trajectory、reward/scorer 和 model checkpoint 绑定到同一 lineage，并用真实 API differential/conformance
  tests、failure-containing data、held-out human intents 与 cross-judge evaluation 检查 transfer。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch74、Ch77、Ch79、Ch80 及相邻 handoff。Ch77
  已拥有 deterministic spine、evaluator-driven search、artifact lineage、durable execution 与 held-out
  verification，但尚未把“environment 也是可生成、可测试、可版本化的 training artifact”及其
  synthetic-to-real gap 串入 workflow，故主 owner 为 Ch77。Ch62 只承接 environment/verifier identity 与
  co-generated-oracle bias；Ch74 只承接 external/internal parameter、action semantics 和 permission；Ch79
  只说明 MCP 是 transport/interface 而非 semantics；Ch80 只承接 dataset/model/environment lineage policy。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch77，Ch62/74/79/80 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：真实
  API differential tests、human-intent distribution、failed-call/failure-recovery training、跨模型 generator/judge
  解耦、多 seed variance、完整 MCP-Atlas、session-isolation throughput、paper/repository dataset unit 对齐、
  Appendix H 伪代码与实现一致性，以及 artifact license/security policy 的可核验版本。

### Mix-Quant — 27/30

- **Candidate / Week / Source Family**：`MIX-QUANT-PHASE-AWARE-PRECISION-AND-PD-HANDOFF`；W21；
  arXiv:2605.20315v1、official `haiquanlu/Mix-Quant` repository、其 pinned `haiquanlu/vllm` submodule 与
  launch/evaluation scripts。arXiv 仅有 v1，提交与 first-public date 均为 2026-05-19；repository 当前只有
  2 commits、无 release/tag，vLLM submodule 固定在 `4078447`，故 public main HEAD 是可复核 artifact
  surface，不等于经过 release governance 的生产版本。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、Related Work、完整 Method、NVFP4
  公式、PD deployment、全部 experiment tables/phase ablation、Conclusion 与 references；论文没有单列
  Limitations、Threats to Validity、appendix 或实现细节附录。代码侧核对了两模型 worker、一 proxy、NIXL
  side channel、KV connector、model/tokenizer/RoPE arguments、evaluation entry points 和 pinned fork；公开
  scripts 当前主要覆盖 Qwen3-8B reasoning、LongBench-v2 与 LongMemEval，不是 paper 中 Gemma-4、Qwen3.5、
  BFCLv4、AA-LCR、tau2、所有 quality tables 与 Prefill latency 的完整 reproduction package。
- **Original Problem / Why Previous Designs Were Reasonable**：uniform BF16 给 Prefill 与 Decode 一致数值路径、
  单一 artifact 和简单 cache identity；在短 prompt、co-located serving 或质量优先时仍合理。weight-only
  INT4/FP4 主要减少权重 bytes、适合 memory-bandwidth-sensitive Decode，但 activation 仍高精度，难充分加速
  compute-heavy Prefill。uniform W4A4 能直接使用低精度 Tensor Core，在同一 worker/precision path 最简单，
  但 Decode 的逐 token decision 会把数值扰动变成不同 token history。PD disaggregation 过去主要按 batch、
  hardware、TTFT/TPOT 与 capacity 分相，不必然要求两个阶段使用不同 model artifact 或 precision。
- **Changed Constraint / Mechanism**：Agent loop 反复把 system prompt、tools、retrieved evidence、memory、
  observations 与 previous actions 重新带入输入，使 `T_p/T_o` 增大，Prefill projection/GEMM 占比上升；同时
  tool call/code/action 的一个 token divergence 可能改变后续 environment state。Mix-Quant 因而维护同一 base
  model 的两条执行路径：Prefill worker 使用 Blackwell-native NVFP4 W4A4，block size 16、E2M1 values、
  FP8 E4M3 local scales 与 tensor-level scale，采用 RTN；Decode worker保留 BF16。Prefill 生成首 token 所需
  logits 和初始 KV，并把 KV 写成 Decode engine 预期的 storage precision/layout；Decode 读取它，之后每个
  generated position 的 KV 由 BF16 path 追加。论文用 attention-mass concentration 解释长 Context 冗余，
  但该观察只是经验动机，不是 Prefill error bound。
- **State Ownership / Control and Data Flow**：quantized Prefill artifact 拥有 prompt compute 与 initial-KV
  provenance；high-precision Decode artifact 拥有 autoregressive token distribution 和新增 KV；tokenizer、
  chat template、position/RoPE 与 base-model lineage 是两路径共享 identity；KV connector/NIXL 拥有 request-
  scoped bytes transfer，不拥有模型语义；proxy 拥有 phase routing；scheduler 分别拥有 Prefill admission、
  Decode iteration 与 handoff placement；request state 只有在 destination 验证 KV identity/availability 后才能
  进入 Decode。公开 script 启动独立 quantized Prefill server、BF16 Decode server 和 vLLM test-tree 的
  lightweight proxy，双方均使用 `NixlConnector` / `kv_role=kv_both` 与 load-failure=`fail`。
- **Implementation Contract**：README 默认 Qwen3-8B quantized Prefill artifact `RedHatAI/Qwen3-8B-NVFP4`、
  Decode artifact `Qwen/Qwen3-8B`、相同 tokenizer、单 GPU per role、TP1、131,072 max length 与 YaRN factor 4；
  model server 支持参数覆盖，不能把默认例子等同全部论文配置。公开 path 没有在一个 worker 内逐 layer 切换
  precision，而是用 PD topology 避免 per-step kernel switching 和 KV-layout conversion；这用额外 worker、
  transfer、proxy、failure states 与 duplicated model residency 换取 stage specialization。
- **Evaluation Contract**：quality 覆盖 Qwen3-8B、Qwen3.5-9B、Gemma-4-26B-A4B-it、Gemma-4-31B-it，
  比较 BF16、uniform NVFP4、Prefill-only NVFP4 与部分 Decode-only FP4；benchmarks 为 BFCLv4、LongMemEval、
  tau2-Bench、LongBench-V2、AA-LCR、MATH500、AIME24/25。serving 基于 vLLM，在 RTX 5090 与 B200 上运行
  quality workloads，但公开文字未逐表绑定 model→hardware、judge、prompt/output、concurrency 和完整 sampling
  contract；每项 benchmark 独立三次取 mean。speed 只测 RTX 5090 上 Qwen3-8B/Qwen3.5-9B 的 end-to-end
  **Prefill stage latency**，FlashInfer attention、Blackwell NVFP4 W4A4 linear kernels，固定同一 batch、prompt
  length、KV dtype 与 backend；Figure 4 变动 sequence length（batch 1）或 batch（length 2K），报告接近 3×，
  不含 frontend、queue、first-token sampling、NIXL handoff、Decode、streaming 或集群 goodput。
- **What the Evidence Proves**：在作者合同内，uniform NVFP4 的 quality 低于 BF16；保留 BF16 Decode 通常能
  恢复较多损失，且 phase ablation 中 Prefill-only 通常好于 Decode-only，但两者均未完全等同 BF16、差距也
  非逐 benchmark 单调。RTX 5090 isolated Prefill path 支持 NVFP4 compute 在给定 kernels/shapes 上加速。
  repository 证明两条 model servers、NIXL connector、proxy 与若干 Qwen3 evaluation paths 可执行组织方式，
  不证明论文所有表格都可一键复现。
- **What It Does Not Prove / Threats to Validity**：三次 benchmark run 没有报告 training-independent seeds、
  confidence interval 或显著性；LongMemEval 当前 repository 使用可配置 LLM judge，而论文未完整披露 judge
  identity。attention top-4096/128K 的 95.8% mass 没有足够 workload/model/sampling 细节，不能外推为所有
  Context 冗余，也不能证明 low-attention token 的 KV error 无语义影响。Prefill token ids 虽固定，量化误差
  仍会跨 layer、attention 和 MLP 传播并改变全部 initial KV 与 first-token logits；它只是不通过 sampled token
  递归改变同次 prompt。论文没有测 TTFT/TPOT/goodput、NIXL bytes/time、queueing、failure recovery、prefix
  cache hit、chunked Prefill、mixed-length/concurrent traffic、功耗、两池总 GPU budget或 co-located best-vs-best。
  也没有证明 non-Blackwell、非 NVFP4、不同 MoE/attention/KV format 或 production SLO 下成立。
- **Trade-offs / New Failure Modes**：阶段专用 precision 把一个 artifact 变成 `base lineage + Prefill quantized
  artifact + Decode artifact + shared tokenizer/RoPE + compatible KV contract + connector/runtime versions`。
  Initial prompt KV 与 later Decode KV 即使 storage dtype 相同，也有不同 compute provenance；prefix reuse、
  deterministic regression 与 cache key 必须记录 Prefill precision/artifact，不能只按 token ids/model alias 命中。
  两份 model residency 与 role-specific capacity减少 request-bearing flexibility；handoff 增加 transfer queue、
  orphaned KV、source/destination version skew、partial failure、cancellation fencing 与 rollback。低精度 Prefill
  仍可能在长尾 task 造成 silent quality loss；quality gate 应能按 request class 回退 BF16 Prefill，而不是只
  保留全局平均。
- **Evolution Relationship**：`Layering / Dependency`：`uniform BF16（simple/quality baseline） → weight-only
  low-bit（decode-byte branch） / uniform W4A4（single-path compute branch） → PD resource separation →
  phase-specific precision and artifact identity → compatible KV handoff → future request/model-aware precision
  routing with measured fallback`。这不是“Prefill 永远 FP4、Decode 永远 BF16”的替代史；短 prompt、链路受限、
  非 Blackwell、cache-heavy 或单池利用率优先时 co-located BF16/FP8/weight-only 仍可能更优。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch39～41、Ch45、Ch50～52。Ch39/40 已拥有 phase compute/
  error/cadence 差异，Ch45 已拥有 `precision + graph + kernel + hardware + artifact` contract，Ch41 已拥有 KV
  identity；Ch51 已拥有阶段资源分化、KV handoff、break-even 与 failure state，但尚未明确“precision/model
  artifact 也可按 phase 分化，且 compute provenance 必须进入 transfer/cache identity”，故主 owner 为 Ch51。
  Ch39/40/41/45 只需短 handoff，Ch50/52 已有 memory/admission 约束，无需重复机制。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch51，Ch39/40/41/45 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：同总
  GPU budget的 best co-located vs best PD goodput、NIXL transfer与 queue breakdown、prefix/chunked/mixed traffic、
  failure/cancellation recovery、KV compute-provenance identity、完整 paper benchmark artifact、judge/sampling
  contract、B200/RTX model mapping、功耗，以及 BF16/FP8/NVFP4 的 request-class fallback threshold。

### ACC — 25/30

- **Candidate / Week / Source Family**：`ACC-AGENT-TRAJECTORY-TO-LONG-CONTEXT-DERIVATIVE`；W21；
  arXiv:2605.21850v1 first-public 2026-05-21，v2 于 2026-06-14 修订。W21 的事件日期锁定 v1；v2
  用于核对后续披露，尤其是新增 Appendix F 的 SWE answer-conditioned rationale，不建立新的 W21 event。
  联读官方 Hugging Face dataset 与 checkpoint cards；未找到作者代码仓库，因此不能把数据/模型可下载
  等同于 compilation pipeline 可复现。
- **Access / Full-read Coverage**：已读 v1 与 v2 的 metadata、Abstract、Introduction、Related Work、完整
  Method/公式/context construction、training setup、main/general/long-context results、agent-type 与 distractor
  ablations、attention/expert analysis、Conclusion、Limitations，以及 Appendix A～F 的 trajectory cases、扩展
  benchmark、overlap test、attention/router statistics 与 SWE rationale synthesis；并核对 dataset 三个 config、
  schema/row counts/license/preview boundary，以及 checkpoint architecture、dtype、training summary 与 usage
  surface。未披露 training hardware、wall-clock/energy、完整 generation/evaluation prompts、checkpoint seeds
  或 executable pipeline，统一记为 `Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable**：原始 Agent SFT 保留完整多轮 history，将 tool
  observations 作为条件输入但从 loss 中 mask，只监督 reasoning/actions 与 final answer。这样做在 tool output
  不受模型控制、不能要求模型复现环境 bytes、目标是学习下一步 action policy 时合理；它也保留原始
  temporal/action structure。约束变化在于：成功 trajectory 中的远距离证据已由工具收集，但 final-answer
  supervision 经多轮 local action objective 间接传播，可能不足以专门训练跨段 evidence integration；重新
  人工标注长文档又昂贵。
- **Changed Constraint / Mechanism**：ACC 先选择 answer-verified trajectories，再派生新的训练对象。Search
  收集 visited full pages 并加入 unvisited search results，SWE 收集 correct-patch files 与 debugging 中查看的
  context files，SQL 展开 queried tables；evidence pieces 在 token budget `B` 内随机打乱并拼接为 `C`。原始
  `L_agent` 监督逐轮 `r_t/a_t` 与 final `r_k/y`，派生的 `L_ACC` 则删除 intermediate actions，只对
  `q + C -> rationale r + answer y` 的输出 tokens 计算 cross-entropy。因而它改变的是 data/objective 与
  task form，不是在同一 interactive objective 内“给 observation token 加 loss”。
- **State Ownership / Control and Data Flow**：source environment/tool 拥有原始 observations；trajectory
  runner 与 verifier 拥有 action order、success 与 final answer；compiler 拥有 evidence extraction、distractor、
  shuffle、truncation 和 schema；teacher 拥有派生 rationale；dataset revision 应拥有 source trajectory、
  environment/version、compiler policy、teacher/model/prompt、verified answer 与 output sample 的 lineage；
  training run 拥有 checkpoint。控制流是 `interactive rollout -> answer verification -> evidence extraction ->
  distractor inclusion -> shuffle/truncate -> rationale synthesis/filter -> direct-answer SFT`。原轨迹并未被
  替代，它仍是 interactive policy 和可追溯 provenance 的 source artifact。
- **Implementation / Data Contract**：数据共 10,802 条：Search 3,369、SWE 4,368、SQL 3,065，context
  为 2K～128K。三个 config schema 不同；公开 viewer 当前显示 7,737 rows，card 总数为 10,802，且提示
  超长内容可能触发 preview error，因此 card-level total 与 viewer-visible rows 必须分开。基础模型为
  Qwen3-30B-A3B-Thinking；sequence length 131,072、global batch 16、LR `1e-5` 到 `1e-6` cosine / 5%
  warmup、AdamW、CE chunk 1,024、sequence parallel 8、EP1、4 epochs。checkpoint card 显示约 31B
  parameters、BF16；未公开 training hardware 与可定位 source snapshot digest。Search rationale 直接 rollout
  约 100% pass，SQL 约 50%；SWE 直接 rollout 约 10%，v2 Appendix F 改为把 compiled context 与 verified
  patch 同时给 DeepSeek-V3.2-Thinking、temperature 0，只保留 final response，并因 patch 已 verified 而
  100% 接受，不再执行 rationale correctness filter。
- **Evaluation Contract / Baselines / Ablations**：主测试为 MRCR 与 GraphWalks，统一报告 avg@3；general
  checks 为 GPQA-Diamond、MMLU-Pro、AIME24/25、IFEval，扩展项为 LongBench-V2、HotpotQA、MuSiQue、
  NarrativeQA。作者 own baseline/ACC 共享 Qwen3-30B-A3B family，但 strong baselines 与 long-context
  methods 使用不同模型、active parameters、context 上限和 inference contracts；GPT-OSS MRCR 还受 harmony
  parsing failure 影响。single-source ablation 不支持“任意 trajectory compilation 都单调受益”：Search/SWE
  虽提高 MRCR，却显著降低 GraphWalks，只有 SQL 同时提高；Search/SWE distractors 对 MRCR 有益，却对
  GraphWalks 有害，full mixture 才在作者组合中同时较强。没有 data-volume-matched、same-token-compute、
  direct unmasked-observation-loss 或 multi-seed training control。
- **What the Evidence Proves**：在上述单一 base model、训练 mixture 与 harness 内，把成功 Agent trajectories
  编译为 direct-answer long-context QA 可以形成有用的 SFT data，并改善作者选择的 long-range dependency
  tasks；agent-type 与 distractor ablations 说明 data structure/mixture 是效果的一部分，不能只归因于 loss
  path。它还证明一份 trajectory 可以经有 lineage 的 transform 成为不同能力目标的派生 dataset。
- **What It Does Not Prove / Threats to Validity**：Search Agent SFT 的单点下降不能证明 observation masking
  是唯一原因，因为 compiled data 同时改变 action tokens、context ordering、distractors、rationale、sample
  selection 与 objective。ACC 把 interactive tool-use 问题改写为 closed-context direct answering，不证明
  tool selection、error recovery、online state tracking 或 production Agent quality 改善。只比较 cleaned
  user questions、截断 3,000 chars、由 all-MiniLM-L6-v2 读取前 256 tokens 的 embedding separation，不能
  排除 evidence/code/table、answer、teacher rationale、template 或 benchmark-instance leakage；高 AUC 只说明
  两集合可分。answer-verified selection 排除失败轨迹；SWE privileged patch 生成的 hindsight rationale 可能
  不 faithful，100% retain 也没有检查其证据归因。随机 shuffle 破坏 temporal/provenance/action dependency，
  `|C| <= B` 又未充分披露超长 evidence 的截断与优先级策略。
- **Mechanism-analysis Boundary**：attention analysis 先选每个 task 变化最大的三层，再画 32 distance bins；
  expert analysis 只随机取每个 split 32 个 examples，也先选变化最大的三层和 top-20 experts。两者是在相同
  evaluation data 上按观察到的 delta 选择后进行的 post-hoc visualization，没有 causal intervention、held-out
  layer selection 或 uncertainty，故只能说 routing/attention statistics 发生关联变化，不能证明
  “task-adaptive restructuring / expert specialization”导致 benchmark gain。
- **Trade-offs / New Failure Modes**：派生 long-context QA 复用已有 rollout，降低重新人工标注成本，却
  复制原环境、retriever、verifier、成功选择与 teacher 的 bias；完整页面/表/源码显著增加 token 与 training
  cost；random distractor 提高 evidence localization 难度，却可能制造与 production 不同的噪声分布；直接
  answer objective 强化 synthesis，但移除 action/observation policy、失败恢复和 tool authorization。raw
  trajectories 还可能带有 PII、secret、版权或 proprietary code，compiled derivative 需要沿 lineage 支持
  license、delete、supersession 与 checkpoint impact analysis。
- **Where Previous Design Still Applies / Evolution**：原始 Agent SFT 在目标是下一步 tool/action policy、
  observation 由环境提供且要保留 temporal state 时仍成立；人工长文档、知识图谱/heuristic synthesis、RL
  与 preference training 也服务不同 supervision contract。演进为 `Layering / Dependency`：`raw interactive
  trajectory + masked environment observations -> answer-verified trajectory -> evidence/distractor compilation ->
  teacher or answer-conditioned rationale -> direct long-context QA SFT -> future provenance-preserving multi-objective
  training that keeps both policy and evidence integration`，不是 `Direct Evolution` 或单向替代。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch22～25、Ch62 与 Ch77。Ch22 已区分 accepted length 与
  effective utilization，但不拥有 derived-data lineage；Ch25 拥有 response-only/loss-mask contract，却不应
  重复整个 data pipeline；Ch62 拥有 leakage/evaluation boundary；Ch77 拥有 trajectory lineage。Ch23 是主
  owner，因为稳定增量是“把运行轨迹转成另一类训练数据时，transform/acceptance/teacher/provenance 共同
  定义 `q(x)`”；Ch22/25/62/77 只需短 handoff。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch23，Ch22/25/62/77 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：
  matched-compute 的 raw Agent SFT、unmasked-observation 或 dual-objective control；failed-trajectory value；
  evidence/answer-level contamination audit；shuffle/truncation policy；teacher/patch-conditioned rationale
  faithfulness；training hardware/energy、多 seed 与真实 Agent downstream transfer；dataset 10,802 与 viewer
  7,737 rows 的 immutable manifest reconciliation。

### GoLongRL — 26/30

- **Candidate / Week / Source Family**：`GOLONGRL-HETEROGENEOUS-LONG-CONTEXT-RLVR`；W21；
  arXiv:2605.19577v1 first-public 2026-05-19，当前只有一个公开版本。联读 official repository、verl training
  extension、QwenLong evaluation harness、22,965-row dataset 与 4B/30B-A3B checkpoints。仓库当前为持续变化
  surface、无 release/tag，因此不能把 2026-08-11 所见 17 commits 反写成 event-time artifact snapshot。
- **Access / Full-read Coverage**：arXiv HTML 不可用，已完整阅读 39 页 PDF：metadata、Abstract、Introduction、
  Background/Related Work、capability taxonomy、data construction/refinement、TMN-Reweight 公式与理论动机、
  implementation、主实验、algorithm/data/alpha ablations、1M extension、general/memory checks、Conclusion、
  Future Work，以及与核心结论相关的全部 Appendix；并核对训练 README、evaluation code surface、dataset
  schema/license/row count 与 checkpoint architecture/dtype/cards。GPU 型号与显存、interconnect、wall time、
  energy、完整 judge identity/config、multi-seed uncertainty 和 event-time source digest 均为 `Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable**：早期 long-context RLVR 用 retrieval path complexity、
  multi-hop/UUID/chunk QA 与 binary exact-match 建立可验证 reward；在目标主要是精确定位、答案短且 verifier
  必须低歧义时，这种设计合理，也让 same-prompt GRPO 的组内标准化拥有一致量纲。约束变化是长上下文
  能力已扩展到 comprehension、exhaustive retrieval、numerical reasoning、structured extraction/matching、ranking、
  ordering 与 summarization；不同 task 的 reward range、variance、答案形式和难度分布不再可直接混合。
- **Changed Constraint / Data Mechanism**：GoLongRL 建立九类 task-native reward dataset，共 22,965 条、context
  0.1K～256K：T1～T4 共占 92.4%，T6～T9 合计仅 3.4%，所以“九类任务”不等于均衡覆盖。约 14K 来自
  curated open datasets，约 9K 由 real documents 合成；DeepSeek V3.2 / Gemini-2.5-Pro 生成与核验，随后用
  Qwen3-4B、Qwen3-30B-A3B 各 `G=8` 做 solvability calibration。4B pass rate >0.75 被视为 easy，0.5～0.75
  medium；30B 0.25～0.75 为 hard，<0.25 被丢弃为 quality-insufficient。这提高可学性，却可能把真实、有效但
  超出当前 model family 能力的 hardest tail 当成噪声删除。
- **Iterative Refinement / Provenance**：V1/V2/V3 分别有 9,630、17,729、22,965 条；每版都以随机 8K 在
  4B 上训练、回看 benchmark weakness 与 reward hacking/ambiguity/format shortcut，再增删数据。query-level
  13-gram overlap 只核验 benchmark query，不能排除 document、answer、semantic 或 transformed leakage；
  benchmark 同时充当 dataset diagnostic 与最终 evidence，又未披露独立 held-out development set，存在
  evaluation-guided adaptive overfitting 风险。UMAP cluster separation 只支持 task text 的语义可分，不证明
  capability coverage、数据独立性或无污染。公开 dataset 为 CC-BY-4.0、2.66 GB，但 card license 不能自动
  证明每个上游文档和 derivative 的许可链；需要 row-level source/transform/delete provenance。
- **Optimization Mechanism**：标准 GRPO 对同 prompt rollout 计算
  `A_i=(r_i-mu_u)/(sigma_u+delta)`；论文实现省略 KL penalty，并采用 group-token mean。TMN 先在 task 内汇总
  `sigma_task=sqrt(mean_u sigma_u^2)`，再用 `Ahat_i=(r_i-mu_u)/(sigma_task+delta)`，使同 task 的 reward-scale
  normalization 一致，同时保留 prompt difficulty 的相对差异。随后以
  `mu_tilde_u=alpha*mu_u+(1-alpha)*mu_task`、`p_hat=count(r_i>mu_tilde_u)/G` 和
  `w=exp(0.5-p_hat)`估计难度：正 advantage 乘 `w`，非正 advantage 除 `w`，从而放大 hard prompt 的稀有
  正样本、减弱其负样本，easy prompt 反向处理。`alpha=0.8` 来自 0/0.5/0.8 sweep；这是任务混合下的
  scale/difficulty policy，不改变 task sampling probability。
- **State Ownership / Control and Data Flow**：dataset revision 拥有 source document、task、native reward、
  generator/verifier、solvability band、decontamination 与 removal reason；sampler 仍按完整 dataset 均匀抽 prompt，
  所以 task mass 与 row count 成比例；rollout engine 拥有同 prompt 的 16 responses；task verifier 产生 raw
  reward；trainer 以 task label 聚合 variance/difficulty statistics，再生成 token-level policy loss；checkpoint
  revision 绑定 dataset、reward implementation、sampler、normalization、base model 与 context policy。控制流是
  `source/curation -> task-native reward -> model-solvability filter -> benchmark-guided revision -> task-proportional
  prompt sampling -> on-policy grouped rollout -> per-task normalization/difficulty reweight -> policy update`。
- **Implementation Contract**：Qwen3-4B-Thinking-2507 训练随机 8K，Qwen3-30B-A3B 训练完整约 23K；严格
  on-policy verl，16 nodes × 8 GPUs、global batch 128、group 16、LR `2e-6`、warmup 5、temperature/top-p 1、
  max prompt 160K、response 16K、10 epochs、PPO epoch 1、weight decay 0.1、gradient clip 1、token-mean loss 与
  IcePop。算法消融只在 4B 做，作者明确避免 30B MoE confound；因此不能从 4B 的 TMN gain 推断 30B。
  当前 repository 把实现称作 `tmn_grpo`，README 写“Task-Mixed Normalization”，论文写“Task-level Mean
  Normalization / TMN-Reweight”，记为 `Versioned Documentation Difference`，不静默合并术语。
- **Evaluation Contract / Baselines / Sensitivity**：long-context suite 包括 LongBench-V2、MRCR、Frames、
  LongBench QA、DocMath、CorpusQA；另测 MMLU-Pro、AIME24/25、GPQA、BFCL-V4 subset 与 LongMemEval。1M
  extension 使用 YaRN factor 2/4 与 `max-num-seqs=4`，所以超长结果是 model + RL data/algorithm + position
  extension 的联合合同。4B GRPO average 62.2、TMN 63.0；TMN 提高 CorpusQA/LBV2，却把 MRCR 67.5 降到
  65.5，不是所有 workload 单调获益。evaluation-alignment Appendix 还显示 published/ours 的显著差异，
  如 Qwen3-30B MRCR -9.7、GPQA -5.8/-4.2、Mem-Rec_Sum -10.9；部分 QwenLong 数字来自原论文，未全部
  统一重跑。未报告独立 seed、error bar、confidence interval 或 significance，alpha 也在同一 benchmark
  surface 上选择。
- **What the Evidence Proves**：在作者公开的 4B base、固定 dataset mixture、rollout/reward/harness 下，
  heterogeneous capability-native rewards 可以共同用于 on-policy long-context RL；task-level denominator 确实
  降低单次推理中 normalized mean `|A|` 的 task 间 CV（作者报告 DrGRPO 0.54、GRPO 0.34、TMN 0.18），且
  作者组合在平均指标上略优于其 GRPO control。它还清楚暴露了“reward scale alignment”与“task/data
  distribution design”是两个不同控制面。
- **What It Does Not Prove / Threats to Validity**：单次训练和平均值不证明 TMN 普遍优于 GRPO；CV 是
  gradient-scale proxy，不是 causal downstream proof。task normalization 不会补偿低频 task 的采样质量，
  也不会让不同 native metric 与真实 user utility 可比。30B 没有算法消融；1M 结果混入 YaRN，且 4B
  CorpusQA 1M 在 GRPO/TMN 下反而低于 base。paper 没有专门 Limitations/Threats section；其 Future Work
  只承认 difficulty scale 在 4B 更明显、larger-scale effect 未定、CorpusQA gap 与 token weighting/RLVR
  仍待研究。结合全文还需标记：model-solvability selection、benchmark-guided revision、parser/format reward、
  judge配置、上游许可、same-family calibration/training correlation 与重复 10 epochs 的风险。这些为审计
  推断，不是作者实验结论。
- **Trade-offs / Where Previous Designs Still Apply**：binary EM 在 exact retrieval、低歧义 verifier 下仍是
  更简单可靠的选择；same-prompt GRPO 适合单 task/同量纲 reward，Dr.GRPO 适合较同质 mixture。TMN 增加
  task taxonomy、reward implementation、running statistics 与 batch-composition dependency；如果 task rows
  极不平衡，仍需 explicit task sampling/curriculum，不能靠 denominator 修复。更多 task-native metrics 扩展
  能力面，却新增 parser fragility、metric gaming、judge correlation 与跨 task operating-point drift。
- **Evolution Relationship**：`Layering / Dependency`：`retrieval-centric long-context RLVR + binary reward ->
  capability taxonomy + task-native metrics -> heterogeneous reward scale/difficulty coupling -> task-level variance
  normalization + within-task difficulty weighting -> future controlled task sampling, held-out capability diagnostics
  and token-level credit`。这是新增分支而非取代旧方案。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch22、Ch23、Ch28～30、Ch62。Ch29 已拥有 same-prompt
  grouping、reward normalization、credit assignment 与跨任务 raw reward 不可比的警告，但还缺“scale、difficulty、
  sample mass 是三个独立变量”；故主 owner 为 Ch29。Ch23 只 handoff capability-driven data distribution 与
  benchmark-guided revision，Ch22 只 handoff effective context utilization，Ch62 只 handoff evaluation/decontamination
  contract；Ch28/30 不重复机制。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch29，Ch23/22/62 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：独立
  validation 与 held-out task family、多 seed / 30B algorithmic ablation、task-balanced sampler 与 normalization
  的因果拆分、judge/reward/parser contract、per-row provenance、同预算 wall-clock/energy，以及在不借助 YaRN
  混杂时的 160K→1M generalization。

### WorldKV — 24/30 — Full Source Review Complete

- **Access / Full-read Coverage**：2026-08-13 恢复 arXiv HTML，覆盖 related work、view-revisit observation、
  camera/action 与 attention retrieval、sink/retrieved/recent/denoising regions、key-similarity compression、GPU/CPU
  storage、两种 world model 的 fidelity/throughput/memory experiments、compression/retrieval ablations、Appendix；并
  联读 project/repository。仓库无 event-time tag，current flags 只作 artifact boundary。
- **Problem / Mechanism / Ownership**：full-history KV 最忠实但 state 随 rollout 线性增长；sliding window 的 bounded
  memory 在只依赖近期状态时合理，却在 scene revisit 时丢失对应 viewpoint。WorldKV 不训练新 memory module，而把
  evicted chunk 存入 GPU/CPU bank，以 camera/action state 或 attention score 建索引；active window 保留 sink、Top-k
  retrieved、recent 与 denoising regions。chunk 内以 Key-Key similarity 保 anchor 与 novelty，扩大同预算历史覆盖。
  runtime 必须拥有 chunk/position/model revision、retrieval index、tier location、eviction 与 RoPE correction。
- **Evaluation / Boundary / Trade-offs**：Matrix-Game-2.0 1.3B/4×H200 与 LingBot-World-Fast 14B/4×B200、作者
  trajectories 与 LPIPS/PSNR/SSIM/FID/FPS contract 支持 training-free branch 的相对结果，不证明语义/因果 world
  consistency 或任意 camera/action space。`6→3` 优于 `3→3` 只在披露预算；`9→3` 已出现过度压缩退化。CPU offload
  新增 transfer/freshness，pose error、retrieval miss、attention dilution 与 stale chunk 是新 failure modes。
- **Evolution / Chapters / Decision**：`full KV → sliding window → off-window tiered bank + retrieval → retrieval-aware
  compression` 是 Ch41 的 `Direct Evolution`，Ch43/50/10 handoff；不覆盖 full KV/sliding-window 的适用场景。
  provisional `Refine — Existing Argument / Experimental`；Books Gate 关闭。待核验 event-time code、pinned memory/
  bandwidth、concurrency、bank GC、position correction、longer horizon 与 human/semantic evaluation。

### PlanningBench — 24/30

- **Candidate / Week / Source Family**：`PLANNINGBENCH-CONSTRAINT-DERIVED-PLANNING-DATA`；W21；
  arXiv:2605.20873v1 first-public 2026-05-20，v2 于 2026-05-29 修订。事件日期锁定 v1，当前 27 页 PDF
  为 v2。联读 official one-commit repository、467-row Hugging Face test split 与 CC-BY-4.0 dataset license；
  仓库无 release/tag，current surface 不等于 event-time immutable snapshot。
- **Access / Full-read Coverage**：已读 metadata/revision、Abstract、Introduction、Related Work、完整 taxonomy、
  synthesis/difficulty equation、automatic verification/quality control、determinacy argument、evaluation/training
  experiments、failure analysis、Conclusion，以及 Appendix A～G 的 task/constraint tables、sampling projection、
  human audit categories、failure case、GRPO hyperparameters 与 generator/critic prompts；并核对公开 dataset
  schema、row count、license 与 repository disclosure。无 dedicated Limitations/Threats section；generation model
  identity、训练 hardware/precision/context/batch tokens、wall time/energy、random seeds、完整 statistical method、
  300-row training set 和 executable verifier code 均为 `Not Disclosed / Not Released`。
- **Original Problem / Why Previous Design Was Reasonable**：fixed planning benchmarks 在 domain/constraint
  稳定、人工能逐题构造 reference、目标只是比较少数 planner 时合理，也能保留真实案例语义；但数量难扩展，
  difficulty 常被 prompt length/requirement count 代理，且局部正确不保证 resource/time/dependency/priority
  共同成立。约束变化是 evaluation 与 RL 都需要大量、可调难度、可核验的 complete-plan instances。
- **Mechanism / State Ownership**：20 名有 planning experience 的 annotators 与 researchers 从代表性场景抽象
  六类、30+ tasks、每 task 平均 5～10 subtasks；constraints 分 general、task-specific 与 optional stateful。
  Generator 为 task/subtask 抽取 basic/medium/hard counts，初始 priors 分别为 `{1:.2,2:.6,3:.2}`、
  `{0:.25,1:.55,2:.2}`、`{0:.7,1:.3}`，生成 self-contained problem 与 checklist；Qwen-A3B-30B Responder
  求解，GPT-OSS-120B Critic 输出 `rho in [0,1]` 与 all-pass `u`。当 `u=1`，sampling distribution 以
  `Normalize(p * exp(eta[-alpha,beta,gamma]))`向中/高难 constraints 移动并投影回合法 count。
  taxonomy owner 定义 feasible design space，generator 拥有 instance/checklist draft，responder 只产生 probe，
  critic 拥有 difficulty feedback，human audit 拥有修订/保留，dataset revision 拥有最终 question/checklist；
  这些 state 不能压成一个“synthetic”标签。
- **Verification / Quality Contract**：checklist 把 input、resource/time、format 与 determinate objective 转成
  instance-level criteria；20 名 annotators 将样本分为 direct retain、minor revision、source correction、discard。
  audited batch 中 86.15% 属于前两类，13.85% 要 source correction，0 discard；这只说明被审 batch 可修复，
  未披露 audit sample size、sampling、inter-annotator agreement 或盲审，不能外推全部 generation precision。
  同一 checklist 同时参与 difficulty feedback、benchmark scoring 与 RL reward，会形成 measurement channel；
  若 taxonomy/checklist 漏掉真实约束，generator 与 critic 可一致地制造“可验证但不真实”的样本。
- **Evaluation Contract**：公开 evaluation set 467 条、schema 为单 user message + checklist；GPT-OSS-120B
  judge 逐 criterion 评分，`All-pass` 要一次回答全部通过，`Avg-pass` 是通过 checklist item 比例。模型使用
  “default inference parameters unless otherwise specified”，未披露统一 max tokens、sampling、retries、API
  version、cost/latency 或 judge calibration。All-pass 与 Avg-pass 的差距支持“局部满足不等于全局可行”；
  但 model ranking 是 single judge + checklist 的结果，不是 executable solver proof。error taxonomy 每个失败
  只分配一个 primary semantic type，排除 refusal/blank，又无 annotation agreement，不能当完整因果诊断。
- **Training Contract / Ablations**：Qwen-A3B-30B 以 GRPO 训练 300 instances，batch 128、50 epochs、actor
  LR `2e-6`、KL `0.001`、8-way rollout；inference temperature 0.7、top-p 0.6、top-k 20。比较 Base、
  comparable-size Human-Authored、Syn-NotDetOptimal 与 Syn-PlanningBench；后者在 ChinaTravel、TravelPlanner
  与部分 instruction-following tasks 上较 Base/Human 较强，并报告 `p<0.05` 标记。但未披露 multi-seed
  training、test family decontamination、统计检验细节、training sample release 或 compute matching；50 epochs
  over 300 items 也放大 template/reward memorization 风险。早期约 1K loose-optimum batch 导致 general
  degradation 的叙述是作者 retrospective conjecture，不是受控 ablation。
- **What the Evidence Proves**：在作者 taxonomy、467-item set、single-judge harness 与 Qwen-A3B-30B
  training setting 中，constraint-derived instances 可作为 evaluation 和 RL data；All-pass/Avg-pass 双指标能
  暴露“多数局部 criterion 通过、完整计划仍失败”的现象；determinate/well-specified optima 与结构化 synthesis
  在作者对照中相关于更清晰 reward dynamics 和更强 transfer。
- **What It Does Not Prove / Trade-offs**：不证明 synthetic plan 等同真实 operational plan，不证明 GPT-OSS
  judgment 等同 constraint solver，也不证明 determinate answer 普遍优于多解 planning。确定解让 reward 更
  directional，却可能收窄合法 solution diversity、把 reference-specific tie-break 当 correctness；更严格
  checklist 提高 auditability，同时增加 checklist omission、flat criterion weighting、critical-constraint dilution、
  judge correlation 与 reward hacking。tool-free closed-context tasks 不测 observation、tool execution、dynamic
  replanning、authorization 或真实副作用。公开 467 条只用于 test，论文 300 条 training data 未公开，复现实验
  仍不闭合。
- **Where Previous Designs Still Apply / Evolution**：人工 fixed benchmark 在高风险、低 volume、开放目标或
  需要专家合法替代解时仍合理；executable solver/simulator 比 model checklist 更适合硬 feasibility；human
  review 仍处理 ontology 外约束。演进为 `Layering / Dependency`：`fixed human cases -> task/constraint taxonomy
  -> constraint-derived instance + checklist -> responder/critic difficulty loop -> human correction -> separate local
  criterion and global all-pass evidence -> future hidden executable verifier, alternate-solution acceptance and
  held-out reward/eval channels`，不是 synthetic 单向替代 human data。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch23/24、Ch61～63、Ch76～78。Ch23 已明确写出
  `task/verifier from executable specification`、outcome rather than unique action sequence、generator/verifier shared
  ontology 与“同 verifier 筛 data/供 reward/做 eval”的 measurement-channel 风险；Ch62 已拥有 rubric formation、
  criterion execution、global ranking、hard constraints 与 judge calibration，直接覆盖 All-pass/Avg-pass 的稳定
  认知。Ch77 的 workflow 是部署执行状态机，而 PlanningBench 是 tool-free closed-context data pipeline，不应
  混为 Agent workflow；其余相邻章节无机制所有权。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered`；主去重 owner Ch62，Ch23
  为 data-pipeline handoff。本轮不修改 Books。若未来出现 executable constraint solver、alternate-plan
  equivalence、independent hidden verifier、released training set 与 multi-seed causality evidence，再评估是否
  refine。待验证：v1→v2 具体 diff、467/300 split provenance、generator model/version、audit sampling/agreement、
  p-value method、judge calibration、data contamination、hard/soft criterion weighting 与 dynamic-tool planning transfer。

### Gated DeltaNet-2 — 26/30

- **Candidate / Week / Source Family**：`GATED-DELTANET-2-DECOUPLED-STATE-EDIT`；W21；
  arXiv:2605.22791 只有 v1，submitted 2026-05-21、first-public/discovery node 2026-05-22。本轮读取完整
  HTML/PDF 对应正文、Appendix A～E、作者 derivation/implementation/evaluation contract，以及 NVIDIA
  official PyTorch repository。当前 repository 显示 7 commits、训练入口与 Triton implementation，README
  记录 05-21 code release；未观察到 immutable GitHub Release，且代码采用 NVIDIA Source Code License-NC，
  所以 current main 是可核验 implementation surface，不等于固定的 event-time artifact。
- **Original Problem / Why Previous Design Was Reasonable**：dense softmax Attention 保留逐 token 可寻址历史，
  但 Prefill pair cost 与 Decode KV state 随长度增长；linear attention / linear RNN 将历史压入 fixed-size
  matrix state，换取 chunk-parallel training 与 token-recurrent Decode。普通 linear update 只追加
  `k_t v_t^T`，容易让新 association 覆盖旧 association；DeltaNet 用当前 key 读取 residual 再擦除/重写，
  Gated DeltaNet 用同一 scalar `beta_t` 控制 erase 与 write，KDA 再把全局 decay 从 scalar 扩为 channel-wise。
  在 gate 数量、参数和 kernel 简洁性优先时，共享 scalar 是合理约束；边界是 erase 作用于 key/read
  coordinates，write 作用于 value coordinates，二者被一个 scalar 耦合并非 delta-rule 的数学必需条件。
- **Changed Constraint / Mechanism**：Gated Delta Rule-2 定义独立的 key-side erase gate
  `b_t in [0,1]^{d_k}` 与 value-side write gate `w_t in [0,1]^{d_v}`：

  ```text
  e_t = b_t * k_t
  z_t = w_t * v_t
  S_t = (I - k_t e_t^T) D_t S_(t-1) + k_t z_t^T
  o_t = S_t^T q_t
  ```

  其中 `D_t` 是 KDA-style channel-wise decay。`b_t` 选择从 decayed state 的哪些 key coordinates
  读取并擦除，`w_t` 选择哪些 value coordinates 被提交；两者退化为同一 scalar 时恢复 KDA，decay 再退化
  为 scalar 时恢复 Gated DeltaNet。允许 negative eigenvalue 的实验分支只把 erase gate 扩到 `[0,2]`，
  write gate 仍为 `[0,1]`；该扩展在当前规模没有稳定收益。
- **State Ownership / Control and Data Flow**：每层、每个 request/batch element 拥有 recurrent matrix state
  `S_t`；model parameters 产生 `q/k/v`、decay、erase 与 write gates，layer update 是 state authority。训练时
  chunk boundary state 跨块传递；packed variable-length layout 在每条 sequence boundary reset state；Decode
  kernel 逐 token decay、erase/read、write，再以 query 读取新 state。它不是可逐 token 回读、有 provenance
  或 delete semantics 的 KV archive，也不是 Ch73 的 durable Agent memory；Runtime 必须把 state 与
  model revision、layer、request/session、dtype、reset/checkpoint/migration 生命周期绑定。
- **Parallelization / Implementation Details**：论文以累计 decay 对 state 做 normalization，把 channel-wise
  decay 吸收到 asymmetric rank-one erase factors，再用 compact WY 表示 chunk 内多个 edits。固定 chunk size
  `C=64`；triangular solve 产生共享 inverse，分别构造 erase auxiliary `Y` 与 write auxiliary `U`，随后完成
  inter-chunk recurrence 和 output。write/erase gates 是逐 channel diagonal operators，不能像 KDA scalar
  一样在 dot product 后统一缩放；gate-aware backward 必须把 `W*V` 与 `B*K` 烘进 dot products。Hopper
  fused backward 只搜索 2/4-warps，避开 8-warp WGMMA layout assertion；Ampere 保留完整 search space。
  forward-only recurrent Decode kernel 与 chunk training kernel 是两个 execution branches，不应把训练吞吐
  直接外推为在线 TPOT。
- **Numerical / Correctness Contract**：log-decay、跨 chunk/Decode recurrent state 与 GEMM accumulators 使用
  fp32，layer output 再 cast 回 model dtype；precision-sensitive WY triangular solve 可退回 conservative IEEE
  fp32，其余 matmul 仍可走 Tensor Core。论文将 chunk forward 对照 tokenwise recurrent reference、backward
  对照 autograd，并在 fp64 随机配置上报告相关 gradients 达 machine precision；production fp32/bfloat16
  仍存在预期 accumulation/mantissa error。L2-normalized q/k、RMSNorm+SiLU output gate 与较小初始化共同
  构成稳定性 contract，不能把 update equation 与这些数值选择拆开评价。
- **Evaluation Contract / Ablations / Throughput**：所有主要模型约 1.3B parameters、`d_model=2048`，在
  FineWeb-Edu 训练 100B tokens；global batch 0.5M tokens、sequence 4K、AdamW peak LR `4e-4`、1B-token
  warmup，hybrid branch 使用 2K SWA。GDN/KDA/GDN-2 与 Mamba-2/3 matching main recurrent state 为每层
  262,144 floats/batch element；比较 recurrent-only 与 hybrid families。作者在 language-model/common-sense、
  RULER NIAH 1K～8K 和截断到 2K 的 real-world retrieval 上报告 GDN-2 最佳 family average，但 DROP 等
  individual tasks 并非最佳，hybrid SWA 对 local aggregation 明显重要。固定 projections、runtime scalarize
  gate 的 ablation 显示 b-only 比 w-only 更接近 full model，说明 erase-side channel freedom 在当前设置贡献
  更大；它没有隔离额外 projection capacity、不同 seed 或规模交互。单 H100、hybrid 1.3B training
  throughput 从短到长序列约由 38.0 降至 36.1 Ktokens/s，只证明该 implementation/workload 的近似平坦
  scaling 与相对 KDA 的小 constant cost，不证明 Decode latency、TTFT/TPOT、multi-GPU scaling 或端到端
  serving goodput。
- **What the Evidence Proves**：在作者 matched-parameter、matched-main-state、1.3B/100B-token contract 下，
  erase/write channel decoupling 可与 channel-wise decay 共存，并能通过 compact-WY chunk algorithm 与
  gate-aware Triton kernels 训练；受控 scalarization ablation 支持两类 gate 均使用 channel freedom，erase
  分支贡献更强。论文也证明模型语义新增的 state-edit freedom 必须进入 backward、precision 与 hardware
  schedule，而不是只改一条数学公式。
- **What It Does Not Prove / Limitations / Threats**：不证明 fixed-state recurrent memory 等价 full Attention，
  不证明 GDN-2 在更大模型、更长训练长度、生成任务或生产 SLO 下普遍优于 Transformer/KDA/Mamba。论文无
  独立 Limitations section，未披露训练 GPU 数/总 compute、multi-seed/error bars、checkpoint selection、
  tokenizer/data filtering、Decode benchmark、memory footprint、multi-GPU communication、failure recovery 或
  long-sequence numerical sensitivity。RULER/2K retrieval 主要测 association/recall，不覆盖多证据推理、
  exact citation、state corruption 或 adversarial interference。fixed state 的收益伴随有损 compression、
  overwrite/forgetting、opaque provenance 和 state migration/isolation failure modes。
- **Where Previous Designs Still Apply / Evolution**：dense Attention 仍适合要求 exact token addressing、引用与
  高 fidelity retrieval 的窗口；sliding-window + recurrent hybrid 在 local evidence aggregation 与长历史压缩
  并存时合理；共享 scalar gate 在模型/实现预算更紧、channel freedom 收益未证实时仍成立。演进关系是
  `Direct Evolution + Layering / Dependency`：`append-only linear state -> residual delta edit -> scalar gated
  erase/write -> channel decay + scalar residual (KDA) -> decoupled key erase and value write (GDN-2) -> hybrid
  SWA + recurrent state -> future state lifecycle, checkpoint/migration and serving-SLO evidence`，不是 GDN-2
  单向替代 dense Attention 或 KDA。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch14～15、Ch17、Ch22、Ch39～40、Ch45。主 owner 为
  Ch22：现有章节已拥有 `dense -> linear/recurrent fixed state -> hybrid softmax` 方向，但尚未具体解释 compressed
  state 的 read/erase/write controls 及其与 chunk-parallel implementation 的耦合，因而存在真实 refine 缺口。
  Ch17 只接收 token mixer/stateful layer 的结构 handoff；Ch39/40 区分 chunk training/Prefill 与 recurrent
  Decode state；Ch45 只接收“模型自由度必须落到 gate-aware kernel、dtype 与 hardware dispatch”的 execution
  handoff，不重复拥有架构机制。
- **Integration Decision / Files / Open Questions**：`Refine — Existing Argument / Experimental`；provisional
  main owner Ch22，handoff Ch17/39/40/45。本轮 Historical Books Gate 关闭，不修改 Books。待验证：多 seed、
  更大规模与更长 training distribution；matched projection/parameter ablation；Decode TPOT、state bytes、
  checkpoint/migration/reset/isolation；多 GPU/compile portability；long-horizon numerical drift；与 dense/SWA
  在相同 TTFT/TPOT/goodput 与质量预算下的 Pareto frontier。

### Post-Trained MoE Can Skip Half Experts / ZEDA — 25/30

- **Candidate / Week / Source Family**：`ZEDA-POST-TRAINED-MOE-DYNAMIC-COMPUTE-MIGRATION`；W21；
  arXiv:2605.18643v1 first-public 2026-05-18，v2 revised 2026-06-08。本周事件锁定 v1；v2 的章节、方法、
  tables 与 appendices 经复核未形成新的 W21 event。已读取全文、Appendix A～D、official 16-commit
  repository 的 conversion/SFT/OPD/evaluation surfaces、MIT license，以及 05-21 更新的 Qwen3-30B-A3B 与
  GLM-4.7-Flash checkpoint cards。current main、model cards 与后续 v2 用于 artifact/revision 核验，不能倒写成
  05-18 已存在的 immutable release。
- **Original Problem / Why Previous Design Was Reasonable**：static MoE 用固定 top-k normal experts 把 total
  capacity 与 per-token active compute 分开；pretraining、SFT、RL/OPD 又共同校准 router、expert specialization
  与 residual scale。若从头设计 dynamic MoE，可以让不同 tokens 使用不同 expert count；但直接修改一个已
  post-trained checkpoint、硬截断 top-k 或施加普通 expert-level uniform loss，会破坏原 router 与 experts 的
  co-adaptation。保持固定 top-k 因此仍是可靠旧方案：artifact 清晰、dispatch shape 较稳定、能力已验证；其
  边界是 easy tokens 也支付同样的 expert FFN compute，部署后没有独立 quality/compute knob。
- **Changed Constraint / Architecture Mechanism**：ZEDA 在每个 MoE layer 的 `N` 个 normal experts 之外加入
  `N_Z` 个 parameter-free zero experts，router 仍选 top-k `K` 个候选；zero expert 被选中时输出严格为零，
  所以本 token 的 active normal-expert count 变为 `K * (1-r_ZE)`。Qwen 配置由 128 normal + 64 zero、top-8
  构成，GLM 为 64 normal + 32 zero、top-4。normal router rows 保留，新 zero-router rows 按原 router
  parameter mean/variance 初始化。copy expert 虽也近零 compute，却额外写入 scaled identity residual，作者
  matched SFT ablation 显示明显 scale/direction mismatch；zero output 才是真正的 expert omission。
- **Training / State Ownership**：original post-trained MoE 是 frozen teacher；augmented dynamic MoE 是 student
  artifact。Stage 1 用 teacher-sampled responses 做 SFT，先稳定新 router/expert-allocation state；Stage 2 在
  student-sampled trajectories 上由 teacher 提供 token-level reverse-KL targets，以 Sampled-Token OPD 缩小
  on-policy distribution gap。60K prompts 由 17K math、15K code、28K chat 构成；OPD 320 steps、batch
  `16 prompts * 2 responses`、temperature 1.0、max generation 32K。teacher checkpoint/version、student
  checkpoint、zero-router initialization、SFT rollout manifest、OPD policy version 与 group-loss policy 是
  一份迁移 lineage；只保留最终 student weights 会丢失可重放的 architecture-conversion contract。
- **Routing Constraint / Control Flow**：普通 auxiliary load-balancing loss 在所有 `N+N_Z` experts 间追求
  uniformity，会重写 post-trained normal-expert specialization。ZEDA 只把 normal experts 与 zero experts 分成
  两组，在 group level 控制 `r_ZE`；relative weight `w` 决定目标 skip ratio，coefficient `alpha` 决定约束强度，
  task loss 负责质量。论文默认 `w=2`、`alpha=0.1`，目标约 50% zero activation；w 增大时 skip ratio 上升、
  quality 逐步下降。zero experts 从 top-k 中移除后，normal-expert probabilities 默认不重新归一化；renorm 会
  放大剩余 residual branch，matched ablation 反而降低精度。这说明 routing weights 同时拥有 selection 与
  magnitude semantics，不能把“跳过 path”实现为 runtime 随意删除 route。
- **Implementation / Deployment Surface**：公开仓库基于 modified SGLang、slime、Megatron-LM 与 Transformers，
  提供 HF↔distributed checkpoint conversion、teacher server、Qwen/GLM SFT/OPD scripts 和 evaluation runner；
  两份 checkpoint 已公开。作者报告 Qwen adaptation 30.12 h、GLM 61.37 h，均为 8 H200，且分别拆出 teacher
  rollout、SFT 与 OPD 时间；这证明 migration 仍需要 teacher serving、训练与 artifact conversion，不是
  serving 时打开一个 skip flag。repository 当前 16 commits、无 immutable release/tag 证据，且依赖 modified
  framework forks，production compatibility、rollback 与 upstream drift 仍需独立验证。
- **Evaluation / Efficiency Contract**：两款约 30B post-trained MoE 在 math/code/instruction 11 benchmarks
  上比较 original、AdaMoE、Dynamic Skipping、naive expert truncation、SFT-only 与 SFT→OPD variants；AIME
  avg@32、coding avg@8，其余 avg@1，sampling `temperature=0.6/top-p=0.95/top-k=20/max 38K`。作者还在
  MMLU-Redux/GPQA-Diamond 做 OOD probe，并用 stage、w、alpha、renormalization、zero-vs-copy、group-vs-global
  auxiliary loss 做消融。推理测量从 training prompts 随机取 256 examples，在单 H200、SGLang、max
  concurrency 32 下固定 input/output token totals，分别测 2K～8K Prefill/Decode throughput；未披露 serving
  precision/quantization、warmup、重复次数、置信区间、batch composition、queueing、TTFT/TPOT 或功耗。
- **What the Evidence Proves**：在这两款 checkpoint、60K adaptation prompts 与作者 framework contract 下，
  post-trained static MoE 可以通过 explicit no-op paths 与 teacher-guided re-calibration 转为 token-dependent
  active-expert count；group-level constraint 比全 expert uniformity 更能保留 normal routing structure，SFT→OPD
  比 matched/exceeding-cost single stage 更稳定。理论 FLOPs 也明确：expert FFN 项乘以 `(1-r_ZE)`，但 router
  从 `N` 扩为 `N+N_Z`，Attention/shared compute 不变；因此“少一半 expert FLOPs”不会变成 2x 端到端收益。
- **What It Does Not Prove / Limitations / Threats**：不证明 zero activation 是 token/task difficulty 的因果估计；
  110-prompt correlation 显示它更接近 response pattern、entropy 与 teacher-student gap，MATH difficulty slice
  反而近似不变。两款 30B models、single adaptation run、公开 benchmark、training-data-derived throughput set、
  无 agentic/long-horizon tasks，不能证明更大模型、不同 expert topology、online serving distribution 或多轮
  reliability。论文承认随 sequence length 增长 speedup 衰减；作者约 1.2x 是 phase throughput，不是完整
  frontend/queue/stream SLO。没有 per-expert load tail、All-to-All bytes/imbalance、kernel occupancy、multi-GPU
  topology、failure recovery、teacher/checkpoint hash、data contamination、multi-seed 或 rollback study。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：获得的是 post-training 后可调 compute，
  付出新 router rows、teacher compute、两阶段 adaptation、更多 artifact identity 与 token-dependent expert batch。
  zero routes 可能造成某 token/layer information loss，group average 达标不保证 tenant/task/layer tail；dynamic
  normal-expert count 还会改变 grouped-GEMM shape、dispatch/All-to-All utilization 与 scheduler predictability。
  固定 top-k 在低 latency variance、无需额外 adaptation、强可复现和专用 static kernels 时仍成立；从头训练的
  dynamic MoE 在能重新塑造全程 routing 时仍成立；hard truncation 只适合 quality loss 可接受的受控场景。
- **Evolution Relationship**：`Direct Evolution + Layering / Dependency`：`static top-k conditional compute ->
  dynamic expert count trained from scratch -> post-trained hard truncation/task adaptation -> zero-output routing
  option -> SFT stabilization -> on-policy teacher correction -> group-level quality/compute control -> runtime-aware
  dispatch, SLO and rollback contract`。ZEDA 没有否定 static MoE；它在既有 checkpoint 与 serving runtime 之间
  增加一个架构迁移层。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch21、Ch25、Ch40、Ch45、Ch52。Ch21 已拥有 top-k routing、
  active/total compute、load balance、All-to-All 与“active FLOPs 不等于 latency”，但尚未拥有 post-trained
  static→dynamic conversion、no-op route 的 residual semantics、group-level preservation 或 quality/compute knob，
  因此主 owner 为 Ch21。Ch25 只接收 two-stage/on-policy distillation 与 lineage handoff；Ch40/45/52 只接收
  variable expert batch、kernel/communication efficiency 与 scheduling predictability，不重复拥有模型机制。
- **Integration Decision / Files / Open Questions**：`Refine — Existing Argument / Experimental`；provisional
  main owner Ch21，handoff Ch25/40/45/52。本轮 Books Gate 关闭，不修改 Books。待验证：可复现的 v1 artifact
  boundary、teacher/student checkpoint hashes、multi-seed、independent held-out serving traffic、per-layer/task
  `r_ZE` tails、EP topology/communication、TTFT/TPOT/goodput、larger MoE、agentic long horizon、framework
  upstream compatibility，以及 adaptation/rollback 是否能保持 router/expert/optimizer/checkpoint identity。

### SkillOpt — 27/30

- **Candidate / Week / Source Family**：`SKILLOPT-VALIDATION-GATED-SKILL-ARTIFACT-OPTIMIZATION`；W21；
  arXiv:2605.23904v1 first-public 2026-05-22，v2 revised 2026-05-25。本周事件锁定 v1；v2 的 Appendix
  编排与 protocol clarification 只用于 revision 核验，不产生新的 W21 event。已读 v1/v2 全文、Method、
  Experiments、Ablations、Transfer、Limitations、Appendix A～C 的 executable algorithm 与 optimizer prompt
  contracts，并联读 Microsoft official repository、versioned documentation、MIT license 与 release history。
  当前 repository 已演进到数百 commits，并在 06-02/07-02 发布 v0.1.0/v0.2.0；这些后续工程事实不能
  倒写成 05-22 event-time artifact，论文实验与 current SkillOpt-Sleep 也必须分开。
- **Original Problem / Why Previous Designs Were Reasonable**：人工 Skill、一次性 LLM 生成和从成功 trajectory
  抽取规则，在任务少、失败便宜、更新频率低时简单、可读，也不会引入额外搜索控制面；weight fine-tuning
  在拥有稳定数据、算力和 checkpoint lifecycle 时能把能力内化。约束变化是 tool-backed Agent 的失败往往
  暴露为可复用程序性规则，但频繁改权重成本高，单次反思又容易把个例、grader shortcut 或破坏性重写
  直接发布。需要优化的是独立、紧凑、可审计的 Skill artifact，而不是让模型在生产中自行改写 policy。
- **Mechanism / Text-Space Update**：target model 与 harness 在一次 optimization run 内冻结；optimizer model
  分别读取 success/failure rollout minibatches，提出 `append / insert_after / replace / delete` JSON patches，
  再经 failure/success merge、冲突消解和 failure-prioritized ranking。`textual learning rate L_t` 只是每步最大
  edit count，支持 constant/linear/cosine/autonomous schedule；它限制 update surface，却不是可微 gradient、
  smooth loss 或 convergence guarantee。candidate skill 只有在 disjoint selection split 上严格高于 current
  score 才接受，tie 也拒绝；最终只在 test split 上评估 best validation-gated artifact。
- **State Ownership / Control Flow / Data Flow**：runtime state 至少包含 current skill `s_cur`、best skill
  `s_best`、以 skill hash 为 key 的 selection-score cache、epoch-local rejected-step buffer，以及只供 optimizer
  使用的 meta skill。控制流为 `train rollout -> success/failure partition -> minibatch reflection -> merge/rank ->
  bounded patch -> selection evaluation -> accept/reject -> best artifact`。rejected buffer 保存失败模式、尝试的
  edits 与 score drop，帮助同一 epoch 避免重复失败；epoch-end slow update 对相同 sampled tasks 比较前后 skill，
  生成 protected longitudinal guidance，也必须再过 selection gate。meta skill 不随 `best_skill.md` 部署，target
  inference 只消费最终静态 Skill。
- **Implementation / Artifact Contract**：论文 default 为 4 epochs、rollout batch 40、reflection minibatch 8、
  16 analyst workers、merge batch 8、`L_t=4` cosine decay 到 2、slow update 每 epoch 20 sampled tasks、
  `split_seed=42`。prompt contracts 要求 structured JSON、跨 trajectory prevalence、去重/冲突消解，并保护
  slow-update marker；`edit_apply_report.json` 记录每项 edit 的 applied/skipped，`best_skill.md` 是部署物。
  current official code 提供 benchmark adapters、YAML config、research train/eval CLI 与 tests；但 later
  SkillOpt-Sleep 是另一入口，其 session harvesting、replay、plugin 与 safety boundary 不属于 W21 论文证据。
- **Evaluation Contract / Baselines / Ablations**：作者覆盖 SearchQA、SpreadsheetBench、OfficeQA、DocVQA、
  LiveMathematicianBench 与 ALFWorld，七个 target models、direct/Codex/Claude Code 三种 execution modes；
  baseline 复用同一 target、test split 与 scorer，包括 no skill、human/one-shot LLM skill、Trace2Skill、
  TextGrad、GEPA 与可用的 EvoSkill。component ablation 在三个 benchmarks 检查 data fraction、batch/minibatch、
  edit budget/schedule、rejected buffer、slow/meta update；transfer 只覆盖若干 model-size、harness 与相邻 math
  benchmark 方向。作者还报告 final skills 为 379～1,995 tokens、1～4 次 accepted updates，以及每点提升所耗
  training tokens；hardware、API model snapshot、temperature、latency、monetary cost、energy、独立重复、
  confidence interval 与 production SLO 均 `Not Disclosed`。
- **What the Evidence Proves**：在作者六个 benchmark、固定 scorer/harness/model 与 deterministic split
  contract 下，外部 Skill 可以成为独立 optimization state；bounded patch、selection gate、rejected evidence
  与 slow/meta state 能共同形成比一次性反思更可审计的 artifact-update loop。ablation 支持这些组件在所测
  三个任务上的增量作用，有限 transfer 说明部分程序性规则可跨近邻 setting 复用。它还证明 optimizer 可以
  只在 offline training path 出现，部署不需要额外 optimizer call；这不等于 Skill 对 target inference 没有
  prompt-token、行为或安全成本。
- **What It Does Not Prove / Threats to Validity**：`52/52` 是作者选定的 model×benchmark×harness cells，
  不是跨任务普遍优势；single split seed、未报告 multi-run variance，以及同一 benchmark scorer 驱动
  candidate gate 与 final evidence，使 search-level overfitting、grader shortcut 与 adaptive method tuning
  仍可能存在。Figure 中反复观察 test trajectory 来论证 validation checkpoint，也不能当作完全隔离的最终
  test protocol。strict improvement 只能保护 selection operating point，不是 security boundary；open-ended、
  multi-objective 或 expensive-to-judge tasks 仍缺可靠 verifier。跨 model/harness/benchmark transfer 样本少，
  成功方向不能推出任意迁移；单一 Skill 也不足以覆盖异构 domain。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：获得的是 compact、inspectable、
  rollback-friendly adaptation layer；付出 offline rollout/optimizer cost、dataset split、scorer ownership、artifact
  lineage 与额外 review surface。finite selection set 会被重复查询，Skill 可能编码 benchmark-specific heuristic；
  rejected buffer 只在 epoch 内存活，slow/meta guidance 又可能固化 correlated error。target model、harness、tool、
  evaluator 或 policy 任一升级都会改变 Skill validity，因此必须 pin dependencies、shadow/canary、记录
  supersession/revocation，并由独立 authority 发布。一次性人工 Skill 在稳定低频任务仍合理；weight adaptation
  在需要内化能力或部署不允许额外 context 时仍合理；高风险、不可逆任务不能让自动 gate 代替人审。
- **Evolution Relationship**：`Layering / Dependency`：`hand-written/one-shot skill -> trajectory lesson extraction ->
  repeated free-form reflection -> bounded patch search -> held-out acceptance + rejected evidence -> slow/meta
  longitudinal state -> versioned skill registry, independent evaluation, canary and rollback`。这不是“文本优化替代
  fine-tuning”，而是在 model weights 与 runtime policy 之间增加可治理的 procedural artifact layer。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch73、Ch76、Ch77、Ch80 及相邻 Agent chapters。
  Ch77 已拥有 evaluator-driven candidate search、held-out verification、lineage 与 failed-run retention；Ch76 已
  拥有 evidence-backed bounded reflection；Ch73 拥有 procedural memory provenance；Ch62 拥有 scorer/
  decision contract。真实缺口是 Ch80 的 Skill registry 已定义 identity、evaluation、supersession/revocation，
  但尚未把“Skill 如何经过可拒绝的 offline optimization 成为新 revision”写成完整 lifecycle，因此主 owner
  为 Ch80，Ch77/76/73/62 只短 handoff。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`；
  主 owner Ch80，handoff Ch77/76/73/62。Historical Books Gate 关闭，本轮不修改 Books。待验证：真正独立的
  final test 与 repeated-selection correction、多 seed、matched rollout/token/cost budget、frozen model/API
  snapshot、skill security/policy review、tool/harness upgrade invalidation、open-ended multi-objective evaluator、
  cross-domain negative transfer，以及 artifact registry 如何执行 provenance、canary、revocation 与 rollback。

### Foundation Protocol — 24/30

- **Candidate / Week / Source Family**：`FOUNDATION-PROTOCOL-GRAPH-NATIVE-AGENT-COORDINATION`；W21；
  arXiv:2605.23218v1 submitted/first-public 2026-05-22，未观察到后续 arXiv revision。已读完整 main text、
  scenario、Conclusion 与 Appendix A reference implementation，并联读 authors' official `foundation-protocol`
  与 `ai-link-net` repositories。论文明确 main text 是 protocol proposal、两个 released repositories 均为
  non-normative reference stack；当前 repos 分别为约 11/20 commits 且继续活跃，不能把 6 月后的 code/docs/
  PyPI 状态倒写成 05-22 immutable specification 或 adoption evidence。
- **Original Problem / Why Existing Point Protocols Were Reasonable**：MCP、A2A、A2UI、DIDComm、ANP、UCP
  分别标准化 tool、agent task、UI delegation、secure messaging、discovery/negotiation 与 commerce 边界；在参与方
  少、责任域单一、同一平台拥有 identity/session/logging 时，专用协议的语义更窄、实现更小，也更容易独立演进。
  当一个跨组织 workflow 同时经过 agent、human、tool、resource、service 与 payment rail 后，每层各自定义
  identity、authority、session、trace 与 evidence 会造成语义漂移和 provenance 断裂。FP 的目标不是替代这些
  wire/domain protocols，而是增加统一 coordination control surface。
- **Mechanism / Object and Plane Model**：graph 中 Entity 是 node，relationship/membership/session 是 edge，
  interaction 是 Activity；最小 vocabulary 为 `Entity / Session / Activity / Envelope / Event /
  Receipt-Settlement / Provenance`。四个 core planes 分别拥有 Entity & Trust、Transport & Routing、Interaction &
  Organization、Regulation & Oversight，Configuration & Profiles 把 identity method、transport、schema/event
  registry、pattern 与 bridge 留在 core 外。轻量 EntityCard 先披露 purpose/risk/schema hash/pricing hint，完整
  schema 只在 selection/authorization 后取得；这是 context/token optimization，也是缩小默认暴露面。
- **State Ownership / Control and Data Flow**：EntityCard/keys/version 定义 actor identity；Session 绑定 participants、
  roles、policy references 与 budget；Activity 拥有 explicit state transition 和 typed input/output pointers；signed
  Envelope 携带 intent、routing/correlation 与 policy references；append-only Event stream 拥有 replay/backpressure；
  Receipt/Settlement 记录 meter/value rail；Provenance 记录 approval/revocation/policy evidence。reference runtime
  以 `HostUid:EntityUid` 寻址，Host 拥有 registry/tree routing，Server 拥有 WebSocket presence、heartbeat、bounded
  offline queue 与 REST binding；handler 只有在 ordered checkpoint pipeline 通过后才能执行业务行为。
- **Policy / Failure / Economic Semantics**：checkpoint 可执行 friend/session/rate/length/payment/contract checks，
  也可把原 message 挂入 pending queue 等待 owner approval；拒绝和人工决定都写 trace。contract state machine
  由 arbiter 验证 typed transition，term amendment 会增加 version 并使旧 approval 失效；escrow 与 external
  direct settlement 共用 receipt/dispute surface。signed snapshots 以 previous hash 串链，EntityCard snapshot、
  delivery、cost 与 settlement references 绑定同一 evidence spine。它提供 tamper-evidence 与 accountability
  hooks，不自动证明 delivery 正确、arbiter 公正、meter 真实或 policy 完备。
- **Implementation Contract**：protocol core 不依赖 web/database/persistence；application layer 提供 async server、
  host management 与 schemas；CLI/UI 只消费 application API。current reference profile 用 single event loop、
  tree routing、WebSocket heartbeat/reconnect/offline queue 与 HTTP REST；论文声称可换 QUIC/gRPC/IPC 或增加 mesh
  route，但没有实现/实验这些 alternatives。MCP bridge 把 FP `INVOKE` 映射为 JSON-RPC `tools/call`，CLI bridge
  把 trust/output/budget/tool policy 映射到 provider-specific flags；bridge 不能凭映射补全被包装协议的 business
  semantics、authorization、idempotency 或 side-effect recovery。
- **Evaluation / Evidence Contract**：论文没有 benchmark、load/failure test、formal safety proof、interop test
  matrix、deployment trace、hardware、latency/throughput、scale、SLO、attack evaluation 或 independent adoption
  evidence；AI-company lifecycle 是 illustrative scenario，不是实验。Appendix 与 current repositories 支持
  “这些 objects/checkpoints/bridges 可实现”的 feasibility evidence，不能支持大规模 agent society、portable
  audit、secure federation、economic fairness 或 protocol stability 已成立。正文也没有独立 Limitations/Threats
  section；这些缺口必须由审计补出，不能被 `working stack` 一词覆盖。
- **What the Evidence Proves / Does Not Prove**：它清晰给出一种 narrow-waist 尝试：统一 actor/session/activity/
  evidence identity，把 transport/identity method/domain pattern 放入 profiles，并让 policy decision 位于 handler
  之前。这是可讨论的 architecture blueprint 与 early implementation surface。它不证明 FP 优于组合
  MCP+A2A+Workflow+IAM/event log，也不证明七个 objects 足够表达所有 protocol semantics；更不证明 friend-list、
  signature、hash chain、reputation 或 human approval 构成 zero-trust security。tree root、arbiter、checkpoint
  order、offline queue、key rotation、revocation propagation、schema negotiation、partition/duplicate delivery、
  Byzantine entity 与 cross-domain policy conflict 都缺系统性证据。
- **Trade-offs / Where Previous Designs Still Apply**：统一 graph/evidence surface 降低 cross-protocol correlation
  成本，却新增 global identity mapping、schema/version registry、bridge semantic gap、checkpoint latency、metadata
  privacy、root/arbiter concentration、cross-domain governance 与 evidence-retention cost。progressive disclosure
  省 token，但 discovery summary 可能过期或误导；append-only trace 方便 audit，却不等于 authoritative state，
  也会产生删除/privacy conflict。专用 point protocol 在单边界、低协调复杂度下仍更简单；enterprise IAM +
  durable Workflow 在封闭组织内可能已足够；开放 marketplace 才更需要 settlement/dispute，但同时需要更强
  economic、legal 与 adversarial model。
- **Evolution Relationship**：`Layering / Dependency`：`point integration protocol -> shared workflow identity/trace ->
  cross-protocol envelope and correlation -> graph-native entity/session/organization -> policy checkpoint + portable
  evidence hooks -> future conformance, federation, fault, privacy and governance proofs`。它是上层 coordination
  proposal，不是 MCP/A2A 或 application Workflow 的 direct replacement。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch68/69、Ch77～80。Ch77 已拥有 durable state、typed events、
  approval、budget、idempotency/recovery；Ch78 已拥有 independent runtime identity、scoped delegation、shared state、
  coordination failure；Ch79 已明确 protocol interoperability 不等于 tool semantics/authorization/workflow；Ch80
  已统一 Agent definition/run、Control/Execution/Evidence planes、identity/policy/evidence graph；Ch68/69 已拥有
  trust boundary、provenance、recovery。故 FP 的稳定观点均有更具体 owner，paper 又没有新 evaluation evidence。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered`；主去重 owner Ch80，
  Ch77/78/79/68/69 为具体机制 owners。本轮不修改 Books。若未来出现 normative spec、version/compatibility
  contract、independent implementation、MCP/A2A conformance suite、partition/duplicate/replay/key-revocation tests、
  formal threat model 与跨组织 deployment evidence，再评估是否 refine。当前只保留 Weekly architecture proposal。

### SciAtlas — 24/30

- **Candidate / Week / Source Family**：`SCIATLAS-SCIENTIFIC-KG-AND-GRAPH-RERANKING`；W21；
  arXiv:2605.22878v1 submitted/first-public 2026-05-20，当前仅观察到 v1，论文自标 `Ongoing Work`。
  已联读完整 HTML、schema/index/prompts appendices、official `zjunlp/SciAtlas` repository 与 OpenAlex
  source contract。当前 repository 的 pip client、CLI、hosted API、editable workflow/Skill 与 58-commit
  surface 包含事件日之后的演进；无 event-time tag/release，故只能辅助核验今天可见的 interface，不能倒写成
  05-20 的 immutable backend artifact 或 deployment evidence。
- **Access / Full-read Coverage**：已读 metadata、Abstract、Introduction、KG schema/statistics、完整 construction、
  online/offline update proposal、tri-path recall、local graph expansion、edge weighting、RWR/final ranking、六类
  qualitative applications、Limitations/Future Work、Appendix A schema/indexes 与 Appendix B prompts，并审计
  current client/CLI/API surface。论文没有 retrieval benchmark、baseline、ablation、sensitivity、hardware、
  build/query cost、concurrency、freshness SLO、formal threat model 或独立 artifact validation；这些字段统一为
  `Not Disclosed`，不能由“43.30M papers / 3B triplets”规模反推质量或可服务性。
- **Original Problem / Why Previous Designs Were Reasonable**：keyword/lexical search 对术语、paper title 与 exact
  identifier 可解释且便宜；dense retrieval 能跨表述召回；citation index、author graph 与 taxonomy 又分别保留
  结构线索。在小 corpus、低延迟或只需已知项查找时，分离这些 indexes、top-k 后 rerank 最简单，也避免把
  noisy social/citation topology 直接注入 relevance。约束变化是跨学科 research task 需要从一个 seed 继续发现
  citation、concept、author 与 field 邻域，而单次 text similarity 难以表达多类关系和 global topology。
- **Construction / State Ownership**：OpenAlex 拥有 source metadata 与 IDs；SciAtlas 过滤非英语、短 abstract、
  缺 critical attributes（例 PDF URL）的记录，标准化并去重 title/institution，但因同名歧义明确不去重 author。
  Qwen3-30B-A3B-Instruct-2507 从 abstract 抽取 3～8 个 keyword 及 importance，`bge-large-en-v1.5` 生成 title/
  abstract/keyword vectors，Neo4j 持有 9 类 nodes、raw/derived edges 与 indexes。raw OpenAlex fact、LLM-derived
  keyword、embedding、`RELATED_TO`、co-occurrence 与 retrieval score 必须拥有不同 provenance；论文未充分披露
  `RELATED_TO` construction，也未给 keyword/entity-resolution precision audit。正文称 12 类 edges，statistics
  与 Appendix schema 只列 11 类，是明确的 documentation conflict，不自行补出第 12 类。
- **Control and Data Flow / Retrieval Mechanism**：query 先走三条 recall path：LLM keyword importance 驱动
  exact/vector keyword matching（threshold 0.7、每词 top-3）；query embedding 分别召回 title/abstract top-60，
  `bge-reranker-large` 各留 top-15 并以 0.4/0.6 融合；若输入含 title/reference，则 GROBID+LLM 抽 title，
  exact/fuzzy matching 以 LCS/Jaccard、threshold 0.88、每 title top-5 形成 anchors。候选信号经 candidate-set
  dependent MinMax normalization 合并，再扩展两 hop、每 entity type/hop 至多 500 nodes；所有 edges 按无向边
  处理，以人工 base weights、keyword/coauthor frequency 与 citation importance 构造 transition，RWR 以
  `epsilon=1e-6`、最多 50 steps 收敛。最终将 pre-score、graph score 与 citation importance 按作者固定权重
  排序，返回 top-20 与 traversal path。对固定 graph/parameters，RWR 是 deterministic ranking；它不是
  deterministic logical reasoning，更不证明 path 上的关系 entail query 或 source claim。
- **Update / Consistency Contract**：论文提出 online OpenAlex API、用户 PDF/GROBID import、每两月 changefile
  三条 update path，但 Limitations 明确 current KG 主要依赖 periodic manual scripts，daily automatic update 是
  future work。production contract 因而必须为 source snapshot、derived-edge/model version、index generation、
  citation correction、author merge/split、delete/tombstone、partial rebuild 与 query trace 定义 ownership；只在
  node 上保留 `updated_date` 不能证明 vectors、keywords、graph edges 与 cached result 已原子更新。
- **Evaluation Contract / What the Evidence Proves**：论文证明一个大规模、paper-centric heterogeneous schema
  与明确的 graph-reranking algorithm 被完整描述，并以 literature review、idea grounding/generation、trend、
  author retrieval/profile 展示 end-to-end qualitative examples；current repository 证明 hosted-client、CLI 与
  machine-readable run artifacts 当前存在。它没有 dedicated quantitative benchmark，作者也把 benchmark 与
  daily update 列为 future work。因此“under two minutes”、topological support 或 qualitative case 不证明相对
  lexical/dense/hybrid baselines 的 recall/precision、claim correctness、cost、load、freshness 或 researcher value，
  也不证明 public raw KG、event-time backend implementation 与所有 downstream workflows 可复现。
- **Threats / Trade-offs / Failure Modes**：graph expansion可发现 text similarity 之外的 papers，却引入 source
  noise、author ambiguity、English/PDF-availability selection bias、citation/prestige Matthew effect、手工 edge
  weight 与 threshold bias、无向 citation 导致时间/因果方向丢失、two-hop/top-500 truncation、MinMax zero-range/
  candidate-set dependence，以及 LLM keyword drift。graph path 是 algorithm trace，不是 claim-level citation；
  citation/author popularity 还可能压低新颖、低资源或新领域 work。snapshot lexical/dense retrieval 在明确术语、
 低延迟、严格 ACL/freshness 或 topology 不可信时继续合理；graph branch 应作为可消融的 candidate generator/
  reranker，而不是替代 source-grounded verification。
- **Evolution Relationship**：`Layering / Dependency`：`lexical exactness + dense semantic recall + structured
  citation/taxonomy indexes -> multi-path seed recall -> typed graph expansion -> graph-aware reranking ->
  provenance/freshness-aware graph retrieval -> benchmarked, direction/policy-aware scientific evidence system`。
  下一阶段压力是把 raw/derived identity、edge direction、ACL/license、correction/deletion、index generation 与
  query decision trace 闭环，并以 time-sliced、cross-domain、new-paper/low-citation slices 做 retrieval、claim
  support、latency/cost 和 bias evaluation。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch72 及 Ch71/73 handoff，并核对 Ch23 data lineage 与 Ch62
  evaluation ownership。Ch72 已覆盖 ingestion→index→hybrid retrieval→rerank→packing、source-of-truth、freshness、
  deletion、claim entailment 与 multi-step retrieval，但尚未把 heterogeneous graph 当作独立 retrieval branch，
  也未明确 raw facts 与 model-derived nodes/edges 的 identity、无向 projection 和 popularity bias。故主 owner
  为 Ch72；Ch23 只承接 source/derived-data lineage，Ch62 只承接 slice-level retrieval/claim evaluation，Ch73
  不接收该 external corpus，避免把 scientific KG 误写成 Agent memory。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  主 owner Ch72，Ch23/62 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证 quantitative
  baseline/ablation、build/query hardware and cost、API load/SLO、edge-weight sensitivity、keyword/entity quality、
  `RELATED_TO` provenance、directed-edge alternative、freshness/delete behavior、public KG snapshot/license、
  low-citation/非英语 bias、12-vs-11 schema conflict 与 event-time repository revision。

### QUEST — 27/30 — Full Source Review Complete

- **Candidate / Week / Source Family**：`QUEST-SYNTHETIC-DEEP-RESEARCH-TRAINING`；W21；arXiv:2605.24218v1，
  submitted/first-public 2026-05-22，当前仅 v1，作者标记 `Work in Progress`。arXiv metadata、authors' official
  project page、`OSU-NLP-Group/QUEST` repository、Hugging Face collection/model/data entrances 均可访问。
- **Access / Full-read Coverage**：2026-08-13 恢复 1657-line arXiv HTML，已读 rubric-tree synthesis、objective/
  open-ended evaluator construction、mid-training/SFT/RL、session-level training、context condenser、八类 benchmark、
  ablations、task filtering、human script check、prompts 与 examples；并联读 repository/model/data collection。
- **Problem / Previous Design / Mechanism**：人工 deep-research task/answer 难扩展，answer-centric QA 又不能表达多解
  report；在窄 fact lookup 上训练的 Agent 难覆盖 citation 与 synthesis。QUEST 用 query-specific rubric tree 表达约束，
  objective branch 从 web evidence 生成 Python verifier，open-ended branch用 rubric judge；17K objective 逐级过滤至
  5,934，3K open-ended 至 2,227。MT→SFT→RL 将 task、rubric、tool trajectory 与 reward lineage 串联；Context
  Condenser 把 claim 分 trusted/untrusted/uncertain，并要求 source 与 next action，避免 discard-all/keep-last-N 的信息损失。
- **Evaluation / Boundary / Trade-offs**：2B～35B Quest、8K synthetic tasks、八 benchmark 与公开 harness 支持作者
  training recipe 下的相对能力，不证明 synthetic rubric 等价真实用户标准或 frontier closed-agent comparison 完全同构。
  50 个 Python scripts 的四人检查发现 2 个不可执行，只能界定 sample；generator/judge/evaluator 共享模型会产生盲点，
  trend-derived task 有时间/语言/地区偏差。Structured condenser 增加 source-bound state，却新增错误 promotion、context
  loss、evaluator revision 与 web freshness failure modes。
- **Evolution / Chapters / Decision**：`answer QA → constraint/rubric tree → executable/open judge → MT/SFT/RL +
  source-aware context state` 是 Ch23 的 `Layering / Dependency`，Ch29/62/71/77 handoff；不是用 synthetic data 替代
  human validation。provisional `Refine — Existing Argument / Experimental`；Books Gate 关闭。待核验 event-time
  artifact、judge independence、script sandbox/security、citation correctness、real-user transfer、cost/SLO 与 data license。

### Post-forward blocked retry — 2026-08-12

2026-08-13 四项 arXiv HTML 均恢复；已按上文覆盖 Method、state/control/data flow、evaluation、ablations、
Appendix/limitations 与可用 artifact，并复核相邻章节和 provisional disposition。旧的 access-failure 只作为恢复历史，
不再是当前 blocker；W21 blocked/current-review queue 清空，Historical Books Gate 仍关闭。

### ThriftAttention — 25/30

- **Candidate / Week / Score / Source Family**：ThriftAttention；W21；25/30；
  `THRIFTATTENTION-MIXED-PRECISION-ATTENTION`。arXiv:2605.23081v1 submitted/first-public
  2026-05-21 22:28 UTC，当前仅 v1；论文 CC BY 4.0。Direct primary sources 为 arXiv metadata、完整 HTML
  正文/公式/表格/limitations 与作者 official Apache-2.0 repository。当前 repository 为 `master`、65 commits、
  未见 event-time tag/release，因此只核验 current artifact surface，不把当前代码状态倒推为 05-21 artifact。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Related Work、Method、error analysis、NVFP4
  representation、block selector、mixed-precision online-softmax merge、CUDA kernel、LongBench/RULER/HELMET/
  PG19 evaluation、latency、sparse/selector ablation、Limitations 与 Conclusion；并核对 README requirements、
  tensor contract、Transformers integration 与 `csrc/cuda/sm120` surface。未发现 Appendix；未披露项按
  `Not Disclosed` 保留。
- **Original Problem / Why Previous Designs Were Reasonable**：FP16 exact attention 语义简单、无需第二份
  cache 或 precision routing，在短上下文、质量边界严格和 unsupported hardware 上仍合理，但长序列使
  QK/AV arithmetic、KV traffic 与容量成本快速增长。uniform FP4 在 Blackwell tensor core 上能同时压缩
  arithmetic/storage/traffic，却把不同 block 的量化误差一视同仁；sparse attention 直接移除低分 support，
  对训练过的 sparsity 或强算力预算合理，但 aggressive sparsity 漏掉的 interaction 不可恢复。新问题不是
  “低精度是否可用”，而是如何按 attention output sensitivity 分配有限高精度预算，同时保持可融合执行。
- **Principle / Mechanism**：论文由一阶扰动界
  `||delta o|| <= sum_j |epsilon_j| p_j ||v_j - o||` 说明同样的 score error 对 output 影响并不均匀。
  Q/K/V 先用 NVFP4（E2M1 values + E4M3 microscales，每 16 values 一组）表示，再按
  `Bq=Bk=64` 划块；selector 用 query/key token means 的乘积为每个 query block 排序，提升 top-k key
  blocks 到 FP16，其余 blocks 保留 FP4。FP4 probability path 采用 SageAttention3 两级 scaling；FP16 与
  FP4 partial outputs 共享 online-softmax normalization state，causal mask 在对应路径生效。它因此是
  **precision allocation**，不是 support pruning，也不是 uniform quantization 的同义词。
- **State Ownership / Control Flow / Data Flow**：模型与 QKV projection 拥有语义；selector 为每个 query
  block 产生 ephemeral precision-routing map；KV manager 必须同时维护位置、block、lifetime 一致的 FP16 /
  FP4 K/V views；kernel 才拥有 two-path online-softmax merge。routing map 不能被误当成 reusable cache
  identity。论文 Limitations 明确 dual cache 比 FP16 cache 多 28% footprint，因此 cache identity、eviction、
  admission、rollback 与两份 view 的一致性是系统成本，不是 kernel 外的免费细节。
- **Implementation Details**：作者实现为单个 CUDA C++ fused kernel：先执行 non-selected FP4 path，再调用
  FP16 helper 处理 promoted blocks；FP16 query fragments 缩小 register lifetime，共享内存在两条 K/V 路径间
  alias，FP4 K/V double-buffered，未命中 promoted block 的 CTA/warp 可跳过 FP16 路径。当前 artifact 要求
  CUDA >=12.8、PyTorch >=2.8、Transformers >=4.52，并提供 batch/query-head/query-length/head-dim 与
  KV-head/KV-length tensor contract；论文只在 consumer Blackwell 上验证，data-center SM100 属 future work。
- **Evaluation Contract**：单 NVIDIA RTX PRO 6000 Blackwell 96GB，CUDA 12.8、PyTorch 2.8.0；作者披露约
  600 GPU-hours downstream benchmark 与约 5 GPU-hours NLL。模型为 Llama-3.2-3B、Llama-3.1-8B、
  Qwen3-4B/8B、Ministral-3-8B-Base-2512，最大 131,072 tokens，greedy decoding；所有 block 64×64，
  FP16 budgets 5%/10%/25%。LongBench v1 English 通过 lm-eval-harness；RULER 13 tasks、每 task-length
  100 samples、4K～131K；HELMET 每 task-length 50 samples、8K～131K；PG19 NLL 只用 Qwen3-8B、
  300 packed sequences、seed 42、teacher-forced cross entropy、2K～131K。latency micro/e2e contract 为
  batch 1、32 heads、head dim 128，end-to-end 用 Qwen3-8B；未披露 output length、concurrency、queueing 或 SLO。
- **Baselines / Ablations / Sensitivity / Overhead**：作者报告 5%/10%/25% budgets 平均恢复 uniform FP4→FP16
  gap 的 89.1%/91.8%/92.4%；但 individual cells 非单调，部分 recovery >100%，且 Llama-3.2 131K 在 5%
  budget 仅 64.2%，说明该 aggregate 不能外推为“普遍接近 FP16”。sparse comparison 只覆盖 HELMET 的
  `json_kv`、`kilt_popqa_3`、`long_narrative_qa`、65,536 tokens，并以 FP16-equivalent FLOPs 匹配
  Thrift 5% 与 Quest 71.3% sparsity；这不是 measured latency 对齐。selector ablation 同一子集上为
  Thrift .599、random .407、diagonal .521；没有 learned/oracle selector、block-size sensitivity、置信区间
  或 downstream multi-seed。kernel headline 为 Prefill 最多 1.7×、131K end-to-end Prefill 约 1.2×、Decode
  kernel 3×～5.5×、131K generation 接近 2×，均受上述单卡/单 batch contract 限定。
- **What the Evidence Proves**：在作者公开的五模型、指定 long-context tasks 与单 consumer Blackwell contract
  内，small FP16 promotion budget 能显著恢复相对 uniform FP4 的质量，且 fused implementation 能利用硬件
  low-precision path。heuristic ablation 支持 token-mean selector 优于 random/diagonal 规则。证据证明的是一个
  workload-conditioned design branch，而非 precision hierarchy 的通用最优解。
- **What It Does Not Prove / Threats to Validity**：不证明所有模型/任务“近似 FP16”、跨硬件可移植 speedup、
  sparse attention 被替代，或 production TTFT/TPOT/goodput/SLO 改善。没有 concurrent/ragged/mixed-length、
  paged KV、prefix cache、chunked Prefill、TP/PP、failover、eviction/admission 与 recovery 测试；dual-cache
  footprint 可能降低并发，selection/index overhead 与 capacity loss 未进入端到端服务 contract。PG19 只有
  一模型一 seed，下游无 confidence interval/multi-seed；作者 benchmark 与 matched FLOPs 不得外推。
- **Trade-offs / Where Previous Designs Still Apply**：FP16 仍适用于 exactness-first、短上下文或无 FP4 hardware；
  uniform FP4 适用于容量/吞吐优先且质量损失可接受；sparse attention 适用于 trained sparsity、明确 skip
  semantics 或更严格 compute budget；mixed precision 适用于能够承担 selector、dual cache 与更复杂 rollback
  的部署。收益来自把精度预算集中到敏感 block，代价是第二份 state、selection latency、identity/eviction
  复杂度和新的 precision-routing failure mode。
- **Evolution Relationship**：`Layering / Dependency`：`uniform FP16 exact -> uniform low-bit -> sparse support
  removal / mixed-precision branch -> block-wise precision allocation -> fused online-softmax execution -> future
  request/head/layer-aware precision policy with memory/admission feedback`。这是由 workload 与 hardware 约束变化
  产生的分支共存，不是后者覆盖前者。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch45 及 Ch39～41/50 handoff。Ch45 已拥有 quantization、
  precision/kernel/graph/hardware contract 和“量化不自动等于加速”，但缺少 attention 内部 precision allocation
  与 paired-cache lifecycle，故主 owner 为 Ch45；Ch39 只承接 Prefill shape/TTFT，Ch40 承接 Decode bandwidth/
  TPOT，Ch41 承接 KV identity/lifecycle，Ch50 承接 memory/admission。避免把相同机制复制到五章。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  owner Ch45，Ch39～41/50 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证 data-center
  Blackwell/其他硬件、matched-memory comparison、production concurrent serving、dual-view cache lifecycle、
  selector sensitivity/learned policy、multi-seed confidence、paged/prefix/chunked compatibility 与 event-time code。

### SkillEvolBench — 24/30

- **Candidate / Week / Score / Source Family**：SkillEvolBench；W21；24/30；
  `SKILLEVOLBENCH-EPISODIC-TO-PROCEDURAL-EVALUATION`。arXiv:2605.24117v1 submitted/first-public
  2026-05-22 18:23:31 UTC，当前仅 v1，CC BY 4.0。Direct primary sources 为 arXiv metadata/完整 HTML、
  official project page、`AIoT-MLSys-Lab/SkillEvolBench` repository 与 official 12.2 MB Hugging Face runnable
  dataset bundle。current repository 为 `main`、12 commits，未见 event-time tag；当前 code/config surface 只作
  artifact 可运行性核验，不倒推为 05-22 immutable revision。
- **Access / Full-read Coverage**：已读 Abstract、Introduction、Related Work、benchmark/task construction、
  complete protocol/equations、all result tables、Raw-Trajectory comparison、Tier-3 capacity ablation、environment-
  level slices、cost-success analysis、Conclusion、references 与 Appendix A complete family catalog；并核对
  dataset card 的 180 task assets/verification bundle、repository scheduler/runtime/stores/retrieval/metrics/schema、
  baseline configs、provider presets、run outputs 与 validation/preflight surface。论文没有独立 Limitations / Threats
  section，未披露项不从 leaderboard 或 current code 反推。
- **Original Problem / Why Previous Designs Were Reasonable**：直接 replay episode 保留 tool calls、files、tests、
  observations、失败假设与 verifier feedback，近邻任务上信息最完整，但会积累长 trace、偶然 fixture 与错误；
  compact Skill 把 know-how 外化成可加载 procedure，降低 context/retrieval burden，却可能在压缩中丢失何时调用、
  如何验证与怎样组合的 cues。旧路线各自合理，缺口是过去 benchmark 常只测 Skill use 或 cold-start generation，
  没有区分“原任务修好了”与“形成了可迁移程序”。
- **Benchmark Construction / Mechanism**：180 tasks = 6 environments × 5 latent procedural families × 6 roles。
  前三角色 canonical/enriched/variant 用于 acquisition，后三角色 context-shift/adversarial/composition 用于 frozen
  deployment。每 task 有 instruction/fixture、public tests、hidden tests、process verifiers 与 rubric；curated seed
  被刻意设计为能做 canonical、但保留 enriched/variant/adversarial/composition gaps。每个 environment 是独立
  lifelong episode，换 environment 时 active library reset，防止跨环境泄漏。
- **State Ownership / Control Flow / Data Flow**：harness 拥有 run artifacts 与 compacted trajectory
  `tau_tilde`；verifier 拥有 outcome/process/reward/diagnostics；host-side Skill Author 只接收 same-family history
  与 skills，并对 environment-scoped library 产生 structured edit `L_(k+1)=U_c(L_k,H)`；task-solving Agent 可读
  environment library，但不能在 frozen deployment 创建、修订、retire。原始 episodes、compacted trajectory、
  verifier evidence、derived Skill 与 library revision 必须是不同 identity；否则无法判断信息丢失或回滚。
- **Controls / Update Policies**：No-Skill 隔离 base capability；Raw-Trajectory 直接检索 same-family compacted
  episodes；Curated-Static/Revision/Always 区分人工 prior 与更新策略；SelfGen-Zero-Shot/Revision/Always 区分
  metadata prior、failure-triggered induction 与 dense updates。Replay 用 final frozen library 重跑 acquisition tasks，
  是 local recovery counterfactual；它不更新 library，也不等于 transfer。Tier-3 forcing 要求每次 eligible
  revision 必须新增/修改 `scripts/`、`references/` 或 `assets/`，用于区分 capacity shortage 与 selective
  abstraction failure。
- **Scoring / Evaluation Contract**：十个 model configurations、三个 harnesses（Claude Code、Codex CLI、
  Gemini CLI）；论文报告 LSR acquisition、RSR frozen replay、ESR frozen deployment，并将 ESR 分解为 CSSR
  context-shift invocation、ARSR adversarial shortcut resistance、CompSR composition。official artifact 公开 180
  tasks、30 curated gap-exposed skills、deterministic environment orders A/B/C、Harbor/Docker runtime、model/provider
  configs、frozen run config、events/retrieval/replay stores 与 report generator。论文未披露实际使用的 order seed
  数、generation seed/temperature、hardware、token budget、wall time、并发、重复 runs 或置信区间；USD cost
  也未绑定 provider snapshot/discount/caching 与 token breakdown。
- **What the Evidence Proves**：在作者构造的六环境/三 harness/十配置 contract 内，Skill-based conditions
  常改善 acquisition 或 replay，却不稳定迁移到 context shift、shortcut resistance 与 composition；Raw-
  Trajectory 的 mean RSR/ESR/ARSR/CompSR 在论文聚合中最强，说明现有 Skill authoring 存在 lossy abstraction
  bottleneck。forced Tier-3 通常增加文件却不稳定提高 ESR，证明“写得更多”与“保留正确的 procedural cues”是
  两个不同变量。environment slices 还表明 invocation、robustness 与 composition 不是同一能力。
- **What It Does Not Prove / Threats to Validity**：不证明 raw trajectory 普遍优于 Skill，也不证明 always-update
  应成为生产默认。180 tasks、30 families、gap-exposed seed、role progression 与 verifier 由同一团队共同设计，
  family procedure、hidden tests 和 process rules 可能共享 ontology；没有 independent human audit agreement、
  contamination analysis、cross-environment transfer、长期多轮 drift、tool/API version change、security/permission
  attack 或 production rollout。缺少 multi-seed/uncertainty/significance 时，10-model win/tie/loss 与平均百分点
  只能作为作者实验；不同 model/provider snapshot 与 harness 实现也构成 confound。论文没有正式 Limitations
  section，以上边界属于本次 evidence audit，不能冒充作者声明。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：raw trajectory 保真度高但 context、
  privacy、retrieval 与 cost 大；compact Skill 便于 inspection/version/reuse，却可能产生 compression loss、
  episode-specific drift、stale validator、weak activation、library clutter 与 composition conflict。failure-only
  update 减少写入和污染，却可能过稀；always-update 增加 evidence opportunities，也增大 revision churn。小型、
  同构、近邻任务仍可 replay；稳定、可验证的跨任务 procedure 才值得升级为 Skill；高风险规则仍应由人工/
  policy owner 管理，而不是从一次成功 episode 自动生成。
- **Evolution Relationship**：`Direct Evolution`：`full episode replay -> retrieved compacted trajectory ->
  distilled procedural lesson -> versioned Skill artifact -> verifier-grounded revision -> frozen transfer evaluation ->
  selective consolidation with provenance, supersession and rollback`。新一代不覆盖旧一代：exact evidence archive
  仍是 derived Skill 的 provenance 与 repair source，Skill 只是带适用范围的 advisory state。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch73 及 Ch62/76/80 handoff。Ch73 已拥有 raw episode→derived
  strategy、source episodes、judge/extractor version、适用范围、supersession 与“procedural state 不自动成为
  Workflow policy”，但缺少 replay/local recovery 与 frozen deployment transfer 的明确分层，以及 raw-
  trajectory control / capacity diagnostic。故主 owner 为 Ch73；Ch62 只承接 EvalSpec/slices/uncertainty，Ch76
  承接 feedback attribution，Ch80 承接 Skill registry/version/rollout，不重复机制。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental`，
  owner Ch73，Ch62/76/80 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证多 seed 与
  uncertainty、independent task/verifier audit、cross-environment/domain transfer、长期 revision/supersession、
  retrieval activation quality、library conflict、privacy/security、matched token/latency/cost、tool-version drift、
  immutable event-time artifact 与 raw episode deletion propagation。

### NITP — 25/30

- **Candidate / Week / Score / Source Family**：NITP: Next Implicit Token Prediction for LLM Pre-training；W21；
  25/30；`NITP-LATENT-NEXT-TOKEN-OBJECTIVE`。arXiv:2605.24956 v1 submitted/first-public 2026-05-24
  09:13:12 UTC；v2 2026-07-02，v3 2026-07-12，后续标记 ICML 2026 accepted。W21 只拥有 v1 event，
  v2/v3 用于 revision 核验，不建立新事件。Direct primary sources 为 v1/v2/v3 full HTML、当前 official
  repository 与其随附论文 PDF；repository 目前只有 assets/PDF/README 两次提交，并明确写着 implementation
  code `Coming soon`，故不能把 abstract 的“实现可用”理解为已有可复现代码。
- **Access / Full-read Coverage**：已读 v1 与当前 v3 的 metadata、Abstract、Introduction、Related Work、完整
  Method/公式/理论、MoE/Dense/MTEB experiments、全部 ablations、Conclusion/Limitations、Appendix A～F、
  training hyperparameters、representation dynamics、training-overhead derivation 与 official repository surface；
  并对 v2/v3 做 45B/Table/Appendix revision diff。已读 Ch24 及 Ch23/25 adjacency，并核对 Ch17 的
  representation owner boundary。训练 data provenance、GPU type/count/topology、precision、random seeds、
  confidence interval/significance 均未披露，不从 benchmark 或仓库 README 反推。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：标准 NTP 直接优化下一 token
  likelihood，目标简单、与 autoregressive generation 一致，并让同一 forward 同时监督所有位置；它仍是可靠的
  base objective。作者关注的边界是：相近 token likelihood 不保证 last hidden states 拥有相近的几何结构或
  transfer utility。随着 representation reuse、retrieval/classification probe 与更强 downstream reasoning 成为
 关注点，只测 token-space loss 可能遗漏 latent-space 差异；这不是证明 NTP 错，而是提出另一个可组合监督面。
- **Principle / Mechanism**：对位置 `t` 的 final hidden state `h_t`，从同一模型 shallow layer 取得位置
  `t+1` 的 contextual state，并 stop-gradient：

  ```text
  z_(t+1) = sg[E_shallow(x_<=t+1)^(t+1)]
  L_NITP  = 1 - cosine(P(h_t), z_(t+1))
  L_total = L_NTP + lambda * L_NITP
  ```

  `P` 是 intermediate width `4d` 的 SwiGLU projection head，只在训练期存在。关键不是普通 layer matching，
  而是 temporal shift `t -> t+1`、self-generated shallow target、stop-gradient 与 scale-invariant cosine loss 的
  组合；same-position alignment、no-stop-gradient、no-projector、MSE、KL 与 generic cosine regularization 都是
  不同设计分支。
- **Theory Boundary**：论文在 fixed target、直接对 `h` 分析或 GGN approximation、projector Jacobian
  locally full-rank/well-conditioned、alignment `s > 0` 且接近 1 的条件下，给出 cosine loss 对 angular tangent
  directions 增加正曲率、同时保留 radial null direction 的推导。这说明辅助 loss 在该局部模型中如何约束角向
  自由度；它不证明真实大模型的 NTP Hessian 全局 rank-deficient，也不证明下游增益由该曲率变化单独因果产生。
- **State Ownership / Control Flow / Data Flow**：backbone 拥有 shallow target 与 predictive state；objective
  builder 负责一位 temporal shift、mask 与 stop-gradient；projection head/optimizer 拥有训练期新增参数和状态；
  checkpoint 必须记录 target-layer、`lambda`、projector version 与 loss schedule 才能恢复同一 trajectory。
  serving artifact 丢弃 projector，仍需把“以 NITP 训练的 backbone revision”与普通 NTP checkpoint 区分；
  无 inference head FLOPs 不等于两种模型具有相同生成 latency、quality 或 deployment SLO。
- **Implementation / Training Contract**：作者训练 DeepSeek-V2-style MoE（144 routed + 1 shared expert、top-8）
  1.9B-A0.3B/3B-A0.5B/9B-A1B，token budgets 105B/200B/330B；Dense 0.5B/2B/3B，token budgets
  200B/330B/330B。全部 context 8192、Qwen2 tokenizer、AdamW beta=(0.9,0.95)、weight decay 0.1、
  grad clip 1.0、WSD schedule、2000 warmup steps、decay ratio 0.2；global batch 256～1024，target layer
  约位于 16%～21% depth，`lambda` 0.8～1.0。语料只描述为 English/Chinese/code/math/reasoning 混合，
  没有足够 provenance、dedup、contamination 或 license contract。
- **Evaluation / Baselines / Ablations**：MoE 13-task average 在 1.9B/3B/9B 分别提高 0.81/2.12/2.67
  points；Dense 七任务 average 在 0.5B/2B/3B 分别提高 1.02/1.79/1.35 points，但个别 C-Eval、AGIEval、
  LCBench、BBH cells 回退。3B MoE frozen last-state 的 25-task MTEB overall 从 39.24 到 41.56，23/25
  tasks 改善；Pile validation cross-entropy 近似持平。3B MoE 200B-token ablation 支持 shallow target、
  next-step shift、stop-gradient、projector 与 cosine branch；same-position average 18.75、NITP 23.58、NTP
  21.10，说明低 alignment loss 本身不足。未报告 repeated training runs、multi-seed、置信区间或显著性。
- **Overhead Contract**：9B MoE 的 analytical projection/loss FLOPs 为约 `1.18e8/token`，相对作者估算
  baseline `5.06e9/token` 约 2.3%；同 GPU 数、global batch 1024、5000 steps 的 wall clock 为 NTP
  16h01m、NITP 16h18m，约 +1.8%。GPU 数量/型号/topology、precision、communication breakdown 未披露，
  因而这些数字只属于作者训练配方，不能外推为通用成本或大规模集群开销。
- **Revision Integrity**：v1 Appendix C 曾加入 `45B-A5.5B`、240B-token、`lambda=0.6` 的 Table 5，报告
  average 52.36→54.02；该 scaling section 与数字在 v2/v3 均被移除，当前正文只覆盖 0.5B～9B。
  因此 45B 结论视为 withdrawn/revision-sensitive evidence，不用于评分、机制强度或 Books 判断。后续版本
  添加 MTEB、language-modeling preservation、geometry dynamics 与 overhead analyses，只能作为 current
  revision evidence，不能反向伪装成 05-24 已公开内容。
- **What the Evidence Proves**：在作者披露的六个 0.5B～9B Dense/MoE training pairs 与指定 benchmarks 内，
  next-step shallow-state cosine objective 能在大致匹配 token/recipe 的 NTP baseline 上改变 representation
  geometry，并在多数报告任务上提高平均分；组件 ablation 支持 temporal prediction 而非 arbitrary alignment
  是关键。证据足以建立“token identity supervision 与 latent predictive supervision 可分层组合”的受限分支。
- **What It Does Not Prove / Threats to Validity**：不证明 NTP 普遍导致有害 collapse、NITP architecture-
  agnostic、跨数据/规模/硬件稳定，或更好 representation 必然改善 generation。作者未披露 data manifest、
  contamination、hardware/precision、seed/variance/significance、完整 prompt/few-shot contract；多个 benchmark
  与任务均有回退。理论含局部假设，代码尚未发布，45B evidence 已撤下，target layer/weight 仍是新增调参面。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：纯 NTP 状态少、实现成熟、objective
  与 serving likelihood 直接对齐，仍适合成本/可复现性优先或无明确 latent-use 需求的训练；NITP 用额外
  projector compute/memory、target-layer/weight selection、checkpoint identity 与潜在 moving-target dynamics 换取
  representation constraint。过浅 target 可能语义不足，过深 target 可能复制已有 degeneration；错误 shift/mask、
  missing stop-gradient、projector mismatch 或 resume 配置漂移会静默改变训练语义。
- **Evolution Relationship**：`Layering / Dependency`：`discrete next-token likelihood -> token-space future-target
  auxiliary heads -> self-generated latent future target -> geometry-aware dual supervision -> future objective routing
  by layer/task/phase with independent representation and generation evaluation`。它是 NTP 之上的训练分支，不是
  后发方案覆盖旧方案；下一阶段压力是 matched-data/matched-compute multi-seed replication、larger scales、
  objective interaction、artifact release 与 trajectory-level observability。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch24 及 Ch23/25，相邻边界清楚；Ch24 已拥有 NTP、loss、
  optimizer/precision/trajectory contract，却仍把 objective 基本写成 token cross-entropy，缺少“相同 likelihood
  不唯一决定 hidden geometry”以及 auxiliary objective 必须带独立 state/evidence contract。故主 owner 为 Ch24；
  Ch17 只承接 hidden representation geometry，Ch23/25 不重复写入。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Experimental /
  Revision-sensitive`，owner Ch24，Ch17 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证
  公开实现、immutable training manifest、hardware/precision/topology、multi-seed/CI、matched-compute larger-scale
  replication、MTP/knowledge-distillation/objective interaction、长期 training stability，以及 45B section 被撤下的
  原因与后续正式版本是否恢复。

### OpenAI Layered Content Provenance — 27/30 — Full Review Complete

- **Candidate / Week / Source Family**：`OPENAI-CONTENT-PROVENANCE-C2PA-SYNTHID`；W21；OpenAI official
  post 2026-05-19，访问日 2026-08-12。Direct source 说明 C2PA conformance、SynthID partnership 与 public
  verification preview；没有公开通用 detector paper、跨平台 false-positive/negative benchmark 或 production
  incident study。
- **Problem / Previous Design / Changed Constraint**：只保存文件 metadata 对自有生成/分发链便宜、可解释，
  但转码、截图、平台 stripping 与编辑会丢失；只做 pixel detector 又难表达“谁在何时用哪个 tool 做了哪次
  edit”。内容跨平台复制和变换后，provenance 必须同时考虑 detailed context 与 signal durability。
- **Mechanism / State Ownership / Flow**：generator 把 C2PA Content Credentials 与 cryptographic signature
  写入内容；SynthID 提供更耐常见变换的 invisible watermark；public verifier 检查二者并返回存在/可解释的
  signal。generator/publisher 拥有 signed assertion，watermark detector 拥有 probabilistic detection，verifier
  拥有解析结果与 evidence presentation；下游 policy 才能决定如何展示或处置。
- **Evidence / Non-proof / Trade-offs**：官方页面证明 C2PA conforming-generator status、SynthID adoption 与
  preview tool 的 intended behavior。它同时明确：未发现 metadata/watermark 时不作“非 OpenAI 生成”结论，
  因为 signals 可被剥离。材料未披露 attack suite、编辑强度、operating point、calibration、false-positive
  denominator、跨 provider coverage 或 adversarial removal cost；因此不能把 preview 写成 origin oracle。
- **Evolution / ROADMAP / Decision**：`unsigned bytes -> signed detailed metadata -> durable watermark ->
  multi-signal verifier -> policy-bound interpretation` 是 `Layering / Dependency`。已读 Ch62/68 及 Ch55；
  主 owner 暂定 Ch68 `Refine — Existing Argument`，补充“signal absence is not negative proof”与多层 signal
  contract；Ch62 只接 verifier calibration。Historical Books Gate 关闭，本轮不改 Books。

### NVIDIA-Verified Agent Skills — 28/30 — Full Review Complete

- **Candidate / Week / Source Family**：`NVIDIA-VERIFIED-AGENT-SKILLS`；W21；NVIDIA Technical Blog
  2026-05-19，联读公开 `NVIDIA/skills` catalog、Skill Card / signing / SkillSpector surface，访问日
  2026-08-12。当前仓库状态可核验机制 surface，但后续 catalog size/roadmap 不反向改写 W21 event fact。
- **Original Problem / Previous Design / Changed Constraint**：单团队内手工审查 prompt/script bundle 简单且
  可追责；Skill 跨团队、catalog 与 Agent runtime 复用后，一个可安装 capability 同时携带 instructions、code、
  dependencies、tools 与 resource flow，publisher 名称或 repository location 不足以证明内容未变、权限与声明一致。
- **Mechanism / Ownership / Flow**：product source repository 经 human/automated review、SkillSpector scan、
  evaluation stage、machine-readable Skill Card、detached OMS signature、catalog 与 daily sync；Skill Card 记录
  owner、license、dependencies、limitations、risks/mitigations 与 verification status。Publisher 拥有 source，
  scanner/evaluator 产生 versioned evidence，signer 绑定完整 directory bytes，catalog 发布 revision，deployment
  admission 验证 signature/card/policy 后才允许 Agent definition 引用。
- **What It Proves / Does Not Prove**：官方文档与公开 repo 支持 publishing surface、signature verification 与
  card schema；Blog 明确 evaluation 是逐步加入的 layer。因此 `verified` 只表示 cataloged/scanned/signed/
  documented（以及按具体 revision 可用的 evaluation evidence），不证明无 malicious semantics、无 vulnerable
  dependency、任务有效、权限最小或运行时不会被 prompt injection。scan coverage 与 card 自述都可能漏报。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：获得 provenance、tamper evidence 与 centralized
  review，却新增 root-certificate/key rotation、revocation、scanner/schema drift、unsigned extra files、stale
  mirrors 与 publisher compromise。封闭、单一 owner、低风险的本地 Skill 仍可用更轻的 manual review；高风险
  执行仍需 sandbox、least privilege、runtime policy 与 trajectory audit。
- **Evolution / ROADMAP / Decision**：`prompt snippet -> reusable mixed artifact -> signed capability package ->
  policy-gated catalog entry -> runtime-observed capability` 是 `Direct Evolution`。已读 Ch68、Ch79、Ch80；
  主 owner 暂定 Ch80 refine，Ch68 接 supply-chain enforcement，Ch79 不承担 authorization。Historical Books
  Gate 关闭，本轮不改 Books。

### NVIDIA Slurm Topology-Aware Scheduling Simulation — 28/30 — Full Review Complete

- **Candidate / Week / Source Family**：`NVIDIA-SLURM-NVL72-TOPOLOGY-SCHEDULING`；W21；NVIDIA Technical
  Blog 2026-05-21，联读 2026-05-07 block-scheduling mechanism 文章。5 月 7 日 event 仍归 W18；本周只记录
  segment-policy simulation 与 scale evidence，不重复发明 topology/block plugin。
- **Problem / Previous Design / Changed Constraint**：Slurm `topology/tree` 的 best-effort locality 在 uniform
  InfiniBand 下用少量跨 leaf 性能换更早启动是合理的；NVL72 形成 18-node scale-up domain 后，跨 domain
  bandwidth cliff 使这种 trade-off 可能从“稍慢”变成不可接受，而 rigid blocks 又可能放大 fragmentation。
- **Mechanism / Ownership / Flow**：`topology/block` 把 NVLink domain 暴露为 blocks；job 的 segment size
  表达需要共同位于高速 domain 的 node subgroup。Scheduler 以 job size/workload I/O demand、available blocks、
  failure state 与 fragmentation 为输入，为大 job 分配较大 segments、小 job 分配较小 segments；operator
  监控 fragmentation 并在 simulator 中 replay arrivals 与 node failure/recovery，再修改 policy。hardware
  inventory 拥有 topology truth，job spec 拥有 requirement，scheduler 拥有 placement，simulator/evidence plane
  拥有 policy comparison。
- **Evaluation Contract / Evidence Boundary**：作者模拟 5,000 GB200 nodes（20,000 GPUs）、15,000 jobs、
  七天、平均 2.5% nodes down，并报告 occupancy 接近 theoretical maximum。该结果是 vendor simulation，
  workload distribution、application slowdown curves、queue/fairness tails 与完整 trace 未公开；“within 1%”不能
  外推到任意 cluster 或证明 performance SLO。文章自己要求按 workload 验证 segment size。
- **Trade-offs / Previous Design / Failure Modes**：更大 segment 保住 scale-up locality，却减少 placement
  flexibility、延长等待或产生 stranded capacity；更小 segment 提高 bin-packing，却可能跨域并伤害
  communication-heavy MoE。traditional tree 对 locality cliff 较缓、start-time 更重要的 fabric 仍成立。新增
  failure modes 包括 stale topology、wrong job annotation、policy oscillation、priority/fairness starvation 与
  simulation-to-production drift。
- **Evolution / ROADMAP / Decision**：`best-effort tree locality -> hard block feasibility -> workload-sized segment
  policy -> failure-aware replay/monitoring` 是与 W18 source family 的 `Direct Evolution`。已读 Ch32、Ch56、
  Ch59～61/63；主 owner 暂定 Ch59 `Refine — Existing Argument / Official Engineering Evidence`，Ch32/60/63
  只接 handoff。Historical Books Gate 关闭。

### NVIDIA Agent Evaluation Guide — 22/30 — Full Review Complete

- **Candidate / Source / Coverage**：`NVIDIA-AGENT-EVALUATION-GUIDE`；NVIDIA Technical Blog 2026-05-19，
  覆盖 model-vs-agent object、task success、tool accuracy、trajectory quality/efficiency 与 production feedback。
- **Evidence Boundary / Decision**：这是工程教程，没有新 benchmark、scorer calibration、uncertainty、ablation
  或 comparative evidence。其 `model != harness != trajectory != outcome` 与 Ch62 已有四层 evaluation object、
  executable evidence 和 trajectory judge contract 完全重复；`No Change — Already Covered` / Ch62。

### Transformers v5.9.0 — 21/30 — Full Review Complete

- **Candidate / Source / Coverage**：`HF-TRANSFORMERS-5.9.0`；GitHub signed release 2026-05-20，commit
  `0a2757d`；已核对 release notes、Cohere2Moe addition、continuous-batching CUDA graph pool、initial TPU
  backend、reasoning-field chat-template 与 CI supply-chain fixes。
- **Evidence Boundary / Decision**：release 证明这些 versioned changes 被纳入 v5.9.0，不证明 continuous
  batching/TP/CUDA-graph 的 production goodput、所有 model compatibility 或供应链无风险。模型 addition、bugfix、
  backend preview 与 CI hardening 也不是单一稳定机制。Ch45/46/55 已覆盖 runtime/compatibility/versioned
  artifact contract，故 `Weekly Only — Version Fact`；实际部署时需重新核对 exact release/PR/code。

### NVIDIA Token-Metered AI Services Reference Architecture — 18/30 — Low-score Boundary Complete

- **Candidate / Source / Boundary**：`NVIDIA-TOKEN-METERED-TELCO-AI-SERVICES`；NVIDIA Technical Blog
  2026-05-21。文章提出从 GPU-hour resale 到 token-metered service、developer studio 与 marketplace 的商业/
  reference architecture，没有披露 metering correctness、tokenizer/model revision、tenant attribution、SLO、
  cost experiment、billing dispute、privacy/sovereignty audit 或 comparative implementation。
- **Decision**：它能提醒 billing unit 必须绑定 model/tokenizer/request identity，但 Ch64～66 已拥有 usage/cost
  attribution；缺少新技术机制与 primary engineering evidence，18/30 `Record Only`，不进入 Books。

## Pending Full Source Review Queue

No current-review pending or blocked candidates.

## Repository Changes

- 2026-08-13 重新逐行复算为 31 scored（19 high、11 mid、1 low）：30/30 `20+` Source Reviews、
  1 个低分边界、0 blocked / ordinary pending。fixed checkpoint 继续有效；academic cross-index 使 Historical
  Evidence Open，Books Closed。
- W21 从 3 个 baseline 扩展为 31 个 scored families；完成 OpenComputer、HRM-Text、Code as Agent Harness、
  DelTA 全文、Appendix（如有）、公开 artifact/repository surface 与相邻章节审计；SkillsVote 因 primary
  text 当前不可访问转入 blocked backlog；LongLive-2.0 同样无法取得 primary text，也转入 blocked backlog；
  OSCAR 完成 35 页 v1、Appendix A～E、official repository/project surface 与 Ch40～43/45/50 邻接审计；
  EnvFactory 完成唯一 v1、全部 appendices、official artifact/data/model/training surface 与 Ch62/74/77/79/80
  邻接审计，并把 paper/repository data-unit 差异与 Appendix H 伪代码歧义保留为版本/文档边界；Mix-Quant
  完成唯一 v1、全部 method/experiments/phase ablation、two-commit official repository、pinned vLLM/NIXL
  launch path 与 Ch39～41/45/50～52 邻接审计，并把 isolated Prefill latency 与端到端 SLO 证据分离；ACC
  完成 v1/v2、Appendix A～F、dataset/checkpoint cards 与 Ch22～25/62/77 邻接审计，明确 derived
  long-context data 与 interactive policy 的分支关系，以及 answer-conditioned rationale、selection 与
  leakage 边界；GoLongRL 完成唯一 v1 的 39 页全文、全部相关 Appendix、official training/evaluation
  repositories、dataset/checkpoint cards 与 Ch22/23/28～30/62 邻接审计，区分 reward scale、difficulty 与
  task sampling mass，并保留 solvability filter、benchmark-guided refinement、evaluation alignment、YaRN、
  single-run 与 license/provenance 边界；WorldKV 完成 official project/repository artifact-level 核验，但 full
  paper 超过当前 primary-source access 上限，转入 blocked backlog，不外推性能、实验与限制；PlanningBench
  完成 v1/v2、27 页 v2、全部 Appendix、official repository、
  467-row evaluation data/license 与 Ch23/24/61～63/76～78 邻接审计；因 Ch23/62 已具体覆盖 constraint-derived
  data、shared verifier blind spot、rubric formation、criterion execution 与 global-validity boundary，最终为
  `No Change — Already Covered`，并保留 unreleased training data、single judge、default inference、hardware/
  seed 与 benchmark-as-reward channel 限制；Gated DeltaNet-2 完成唯一 v1、Appendix A～E、official seven-commit
  repository 与 Ch14～15/17/22/39～40/45 邻接审计；其 erase/write decoupling、compact-WY chunk training、
  gate-aware backward 与 recurrent Decode 形成完整机制链，暂定 Ch22 refine / Experimental，同时保留
  1.3B/100B-token、4K training、2K SWA、single-H100、无 multi-seed/Decode-SLO 的证据边界；保留 8 项
  current-review pending queue；Post-Trained MoE/ZEDA 完成 v1/v2、Appendix A～D、official 16-commit
  training/evaluation surface、两份 checkpoint cards 与 Ch21/25/40/45/52 邻接审计；zero-output routes、
  frozen-teacher SFT→OPD、group-level balancing 与 no-renormalization 构成 post-trained static→dynamic MoE
  conversion，暂定 Ch21 refine / Experimental，并将单 H200、8192 sequence、concurrency 32、256 training-
  prompt examples 的 phase throughput 与生产 SLO 分离；SkillOpt 完成 v1/v2、Limitations、Appendix
  executable algorithm/prompt contracts、official repository/docs/releases 与 Ch62/73/76/77/80 邻接审计；
  它把 Skill 定位为 validation-gated、versioned external optimization state，暂定 Ch80 refine / Experimental，
  并明确 selection gate 不等于 security/final-test independence；Foundation Protocol 完成唯一 v1、完整
  architecture/scenario/Appendix reference stack、official protocol/application repositories 与 Ch68/69/77～80
  邻接审计；它是缺少 benchmark、formal threat model、conformance/fault/scale evidence 的 early protocol
  proposal，其 object/plane/checkpoint/evidence 观点已由现有章节具体拥有，故为 `No Change — Already
  Covered` / Ch80；SciAtlas 完成唯一 v1、schema/index/prompts appendices、current official client/CLI/API
  surface 与 Ch72/23/62 邻接审计；其 tri-path recall、typed graph expansion 与 RWR 是可定位的 retrieval
  branch，暂定 Ch72 refine / Experimental，但 current manual update、11/12 edge 文档冲突、raw/derived
  provenance、无 benchmark/ablation/hardware/cost/SLO 与 popularity/language/PDF bias 保持显式边界；保留
  QUEST 的 official project/repository/model/data surface 可读，但 28.7 MB full paper 无 HTML 且当前 permitted
  path 无法完整取得，故转入 `Unverified / Blocked Backlog`，不把 8K-task/closed-agent headline 或公开代码
  surface 误算为 Full Source Review；ThriftAttention 完成唯一 v1、mixed-precision selector、NVFP4/FP16
  online-softmax merge、CUDA kernel、全部 benchmark/ablation/limitations、current official artifact surface 与
  Ch39～41/45/50 邻接审计；它暂定 Ch45 refine / Experimental，并把 5% budget 的 aggregate recovery、单卡
  latency 与 production SLO 分离，同时保留 dual cache 28% footprint、selector/identity/eviction、single-seed/
  no-CI 与 hardware portability 边界；SkillEvolBench 完成唯一 v1、full protocol/results/family catalog、official
  project/repository/dataset/runtime surface 与 Ch62/73/76/80 邻接审计；其 replay/frozen-transfer separation、
  Raw-Trajectory control 与 Tier-3 capacity diagnostic 暂定 Ch73 refine / Experimental，同时保留 co-designed
  family/seed/verifier、无 multi-seed/uncertainty、provider/harness confound 与长期 drift/production 边界；NITP
  完成 v1～v3、完整 method/theory/experiments/Appendix、official repository 与 Ch23～25/17 邻接审计；其
  token-space NTP + latent next-state supervision 暂定 Ch24 refine / Experimental / Revision-sensitive，同时将
  local-theory assumptions、未披露 hardware/precision/multi-seed、未发布 implementation code 与 v1 45B
  Appendix 在 v2/v3 被移除的证据边界写入；current-review queue 归零，W21 forward Evidence Gate 通过；
  6 个 curation-lag spillbacks 回拨 W20，并从 W22 feed 回收 6 个、从 W23 feed 回收 1 个 v1 date 属于 W21
  的条目。fixed official / Infra replay 新增并审计 OpenAI content provenance、NVIDIA verified skills、Slurm
  topology-aware scheduling simulation、Agent evaluation guide、Transformers v5.9.0 与 token-metered reference
  architecture；其中 5 项为完整 `20+` Source Review，1 项为低分边界。既有 Ch62
  executable-evaluation 内容作为章节级输入。2026-08-14 已完成 31/31 最终 disposition，并将长期机制整合到
  Ch17、Ch21、Ch45、Ch55、Ch63、Ch66、Ch72、Ch84；WorldKV 的 Ch25 独立 Gate 同步计入。

## Open Questions

1. executable capability eval 怎样隔离 dual-use artifact，同时保留可复现证据？
2. OpenComputer 的 verifier repair 如何防止 checker 被改成迎合固定 trajectory，而不是修复真实 specification？
3. W22 的 blocked / accessible candidates 中，哪些能形成新的长期机制，哪些只会强化已有章节论证？
4. HRM-Text 的收益中，recurrence、PrefixLM、response-only loss 与 task-formatted data 各自能贡献多少，
   能否在多 seed、更大规模和 production serving contract 下保持？
5. fixed official/infra release source replay 是否会恢复改变 runtime contract 的同周事件？
6. SkillsVote、LongLive-2.0、WorldKV 与 QUEST 的 primary text 何时可恢复；其 arXiv metadata、核心 mechanism 与公开
   artifact 是否能在 post-forward retry 中完成独立核验？
7. OSCAR 的 MMLU-style 8,878 tokens、Table 7 default GPQA 8k 与当前仓库 GPQA 30k 三种 calibration
   contract 如何归一；rotation artifact 怎样进入 cache identity、compatibility check 与 rollback？
8. EnvFactory 的 generated environment 怎样和真实 API 做 differential/conformance test；失败调用与 session
   isolation cost 怎样进入训练数据；paper/repository dataset unit 与 Appendix H sampling 语义怎样归一？
9. Mix-Quant 在同总 GPU budget、真实 NIXL handoff、prefix/chunked Prefill、mixed traffic 与 TTFT/TPOT SLO 下
   是否仍有正 goodput；initial-Prefill 与 Decode-added KV 的 compute provenance 怎样进入 cache identity？
10. ACC 的 raw Agent SFT、observation-visible/dual-objective 与 compiled direct-answer SFT 在 matched compute
    下怎样归因；SWE privileged-patch rationale 是否 faithful；dataset card 的 10,802 与 viewer 的 7,737 rows
    怎样绑定 immutable manifest、source trajectory 与删除/版权 lineage？
11. GoLongRL 的 TMN gain 在独立 validation、多 seed、30B non-MoE control 与 task-balanced sampler 下是否仍成立；
    benchmark-guided dataset revision 怎样隔离 final evaluation；native reward、parser/judge 与 row-level license/
    provenance 如何版本化？
12. PlanningBench 的 467 evaluation / 300 training provenance、generator version、human-audit sampling/agreement、
    judge calibration 与 p-value method 能否公开；怎样用 executable solver 接受多个等价 plan，并隔离
    data filter、RL reward 与 final evaluation channel？
13. Gated DeltaNet-2 的 erase/write freedom 在 matched projection capacity、多 seed、更大规模与更长训练长度下
    是否仍成立；recurrent state 怎样获得 checkpoint、migration、reset、isolation 与 serving-SLO contract？
14. ZEDA 的 group-average zero activation 怎样约束 per-layer/task/tenant tails；在真实 EP topology、mixed traffic、
    TTFT/TPOT/goodput 与 rollback 下，约 50% expert-FLOP reduction 还能转化为多少可交付收益？
15. SkillOpt 在 repeated selection queries、多 seed、独立 final test 与 target/harness/tool revision 下能否保持收益；
    Skill registry 怎样把 optimizer、rollout、scorer、rejected evidence、canary 与 rollback 绑定为可审计 lineage？
16. Foundation Protocol 如何把 proposal 推进为 normative/versioned spec；跨 MCP/A2A bridge 的 conformance、
    partition/duplicate delivery、key rotation/revocation、checkpoint ordering 与 cross-domain policy conflict 怎样验证？
17. SciAtlas 的 11/12 edge schema、`RELATED_TO` provenance、author identity、raw/derived revision、directed citation、
    deletion/freshness 与 low-citation/non-English slices 怎样闭环；graph branch 在 matched lexical/dense hybrid、
    fixed corpus 和完整 latency/cost contract 下是否真正改善 retrieval 与 claim support？
18. ThriftAttention 在 matched cache capacity、并发和 TTFT/TPOT/goodput SLO 下是否仍优于 uniform FP4、FP16
    与 sparse branch；paired FP16/FP4 KV views 怎样绑定 prefix identity、eviction、migration 与 rollback，selector
    怎样适配 layer/head/request 而不放大 policy latency 和 precision thrashing？
19. SkillEvolBench 的 raw-trajectory advantage 在 independent task/verifier design、多 seed、matched tokens/latency/
    cost、cross-environment transfer 和长期 tool/version drift 下是否保持；derived Skill 怎样记录 source episodes、
    activation evidence、conflict、supersession 与 delete propagation，避免 capacity growth 变成 procedural clutter？
20. NITP 能否发布可复现 implementation 与 immutable training manifest；在 matched compute、multi-seed、更多
    architecture/data/scale 上，latent objective 是否仍改善 generation 与 representation；v1 45B section 为何在
    v2/v3 移除，正式版本会如何处置该证据？
21. content-provenance verifier 的 operating point、transform/attack suite 与跨 provider interoperability 如何公开，
    才能让 signal absence 与 false-positive risk 被正确解释？
22. Agent Skill 的 signer/revocation、scanner/card schema drift、mirror freshness 与 runtime least-privilege policy
    怎样组成同一个 admission contract，而不把 `verified` 误解成 `safe`？
23. Slurm segment policy 在公开/真实 trace、application slowdown curve、queue/fairness tail 与故障恢复下，是否仍能
    同时保住 locality 和 occupancy；何时应退回 tree/best-effort placement？

## Sources

- Google Research May 2026 archive: https://research.google/blog/2026/05/
- OpenAI Research milestone index, entry dated 2026-05-20:
  https://openai.com/research/index/milestone/
- Anthropic Research index, entries dated 2026-05-22:
  https://www.anthropic.com/research
- OpenAI layered content provenance（published 2026-05-19；accessed 2026-08-12）:
  https://openai.com/index/advancing-content-provenance/
- NVIDIA-verified Agent Skills（published 2026-05-19；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/nvidia-verified-agent-skills-provide-capability-governance-for-ai-agents/
- NVIDIA Skills catalog and verification surface（accessed 2026-08-12）:
  https://github.com/NVIDIA/skills
- NVIDIA SkillSpector（accessed 2026-08-12）:
  https://github.com/NVIDIA/SkillSpector
- NVIDIA Agent evaluation guide（published 2026-05-19；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=116877
- NVIDIA Slurm topology-aware scheduling simulation（published 2026-05-21；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=117052
- NVIDIA Slurm block-scheduling mechanism（published 2026-05-07；related W18 node；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=116606
- Transformers v5.9.0 release（released 2026-05-20；accessed 2026-08-12）:
  https://github.com/huggingface/transformers/releases/tag/v5.9.0
- NVIDIA token-metered AI services reference architecture（published 2026-05-21；accessed 2026-08-12）:
  https://developer.nvidia.com/blog/?p=117097
- Hugging Face Papers, 2026-W21 discovery index: https://huggingface.co/papers/week/2026-W21
- OpenComputer paper: https://arxiv.org/abs/2605.19769
- OpenComputer HTML: https://arxiv.org/html/2605.19769
- OpenComputer artifact: https://github.com/echo0715/OpenComputer
- HRM-Text: https://arxiv.org/abs/2605.20613
- HRM-Text HTML: https://arxiv.org/html/2605.20613
- HRM-Text artifact: https://github.com/sapientinc/HRM-Text
- HRM-Text checkpoint/model surface: https://huggingface.co/sapientinc/HRM-Text-1B
- Code as Agent Harness: https://arxiv.org/abs/2605.18747
- Code as Agent Harness HTML: https://arxiv.org/html/2605.18747
- Code as Agent Harness companion bibliography: https://github.com/YennNing/Awesome-Code-as-Agent-Harness-Papers
- DelTA: https://arxiv.org/abs/2605.21467
- DelTA HTML: https://arxiv.org/html/2605.21467
- DelTA artifact: https://github.com/RUCBM/DelTA
- SkillsVote: https://arxiv.org/abs/2605.18401
- LongLive-2.0: https://arxiv.org/abs/2605.18739
- OSCAR: https://arxiv.org/abs/2605.17757
- OSCAR HTML: https://arxiv.org/html/2605.17757
- OSCAR artifact: https://github.com/FutureMLS-Lab/OSCAR
- OSCAR project page: https://oscar-quantize.github.io/
- EnvFactory: https://arxiv.org/abs/2605.18703
- EnvFactory HTML: https://arxiv.org/html/2605.18703
- EnvFactory artifact: https://github.com/LARK-AI-Lab/EnvFactory
- Mix-Quant: https://arxiv.org/abs/2605.20315
- Mix-Quant HTML: https://arxiv.org/html/2605.20315
- Mix-Quant artifact: https://github.com/haiquanlu/Mix-Quant
- Mix-Quant pinned vLLM fork: https://github.com/haiquanlu/vllm/tree/407844713d8628c5c81ed453e57e29b44b072280
- ACC metadata and revision history: https://arxiv.org/abs/2605.21850
- ACC v1 HTML: https://arxiv.org/html/2605.21850v1
- ACC v2 HTML: https://arxiv.org/html/2605.21850v2
- ACC dataset: https://huggingface.co/datasets/groundhogLLM/ACC-dataset
- ACC checkpoint: https://huggingface.co/groundhogLLM/ACC-Qwen3-30B-A3B
- GoLongRL: https://arxiv.org/abs/2605.19577
- GoLongRL PDF: https://arxiv.org/pdf/2605.19577
- GoLongRL artifact: https://github.com/xiaoxuanNLP/GoLongRL
- GoLongRL training extension: https://github.com/xiaoxuanNLP/GoLongRL/tree/main/Train/verl
- GoLongRL evaluation harness: https://github.com/xiaoxuanNLP/GoLongRL/tree/main/Eval/QwenLong-Benchmarks
- GoLongRL dataset: https://huggingface.co/datasets/Kwai-Klear/GoLongRL
- GoLongRL 4B checkpoint: https://huggingface.co/Kwai-Klear/GoLongRL-4B
- GoLongRL 30B-A3B checkpoint: https://huggingface.co/Kwai-Klear/GoLongRL-30B-A3B
- WorldKV: https://arxiv.org/abs/2605.22718
- WorldKV project page: https://cvlab-kaist.github.io/WorldKV/
- WorldKV artifact: https://github.com/cvlab-kaist/WorldKV
- PlanningBench: https://arxiv.org/abs/2605.20873
- PlanningBench PDF: https://arxiv.org/pdf/2605.20873
- PlanningBench artifact: https://github.com/Tencent-Hunyuan/PlanningBench
- PlanningBench dataset: https://huggingface.co/datasets/tencent/PlanningBench
- PlanningBench dataset license: https://github.com/Tencent-Hunyuan/PlanningBench/blob/main/LICENSE.txt
- Gated DeltaNet-2: https://arxiv.org/abs/2605.22791
- Gated DeltaNet-2 HTML: https://arxiv.org/html/2605.22791v1
- Gated DeltaNet-2 PDF: https://arxiv.org/pdf/2605.22791
- Gated DeltaNet-2 artifact: https://github.com/NVlabs/GatedDeltaNet-2
- Post-Trained MoE Can Skip Half Experts: https://arxiv.org/abs/2605.18643
- Post-Trained MoE v1 HTML: https://arxiv.org/html/2605.18643v1
- Post-Trained MoE v2 HTML: https://arxiv.org/html/2605.18643v2
- ZEDA artifact: https://github.com/TsinghuaC3I/ZEDA
- ZEDA models/data collection: https://huggingface.co/collections/TsinghuaC3I/zeda
- SkillOpt metadata and revision history: https://arxiv.org/abs/2605.23904
- SkillOpt v1 HTML: https://arxiv.org/html/2605.23904v1
- SkillOpt v2 HTML: https://arxiv.org/html/2605.23904v2
- SkillOpt official artifact: https://github.com/microsoft/SkillOpt
- SkillOpt versioned documentation: https://github.com/microsoft/SkillOpt/blob/main/docs/index.md
- SkillOpt release history: https://github.com/microsoft/SkillOpt/releases
- Hugging Face Papers, 2026-W22 curation-lag cross-check: https://huggingface.co/papers/week/2026-W22
- Foundation Protocol metadata: https://arxiv.org/abs/2605.23218
- Foundation Protocol HTML: https://arxiv.org/html/2605.23218v1
- Foundation Protocol reference runtime: https://github.com/FoundationAgents/foundation-protocol
- Foundation Protocol application network: https://github.com/FoundationAgents/ai-link-net
- SciAtlas metadata: https://arxiv.org/abs/2605.22878
- SciAtlas v1 HTML: https://arxiv.org/html/2605.22878v1
- SciAtlas official artifact/current client surface: https://github.com/zjunlp/SciAtlas
- OpenAlex source documentation: https://docs.openalex.org/
- QUEST metadata: https://arxiv.org/abs/2605.24218
- QUEST official project page: https://osu-nlp-group.github.io/QUEST/
- QUEST official artifact: https://github.com/OSU-NLP-Group/QUEST
- QUEST official model/data collection: https://huggingface.co/collections/osunlp/quest
- ThriftAttention metadata: https://arxiv.org/abs/2605.23081
- ThriftAttention v1 HTML: https://arxiv.org/html/2605.23081v1
- ThriftAttention official artifact: https://github.com/joesharratt1229/ThriftAttention
- SkillEvolBench metadata: https://arxiv.org/abs/2605.24117
- SkillEvolBench v1 HTML: https://arxiv.org/html/2605.24117v1
- SkillEvolBench official project page: https://skillevolbench.github.io/
- SkillEvolBench official artifact: https://github.com/AIoT-MLSys-Lab/SkillEvolBench
- SkillEvolBench official runnable dataset: https://huggingface.co/datasets/SkillEvolBench-Team/Skill-Evol-Bench
- Hugging Face Papers, 2026-W23 curation-lag cross-check: https://huggingface.co/papers/week/2026-W23
- NITP metadata and revision history: https://arxiv.org/abs/2605.24956
- NITP v1 HTML: https://arxiv.org/html/2605.24956v1
- NITP v2 HTML: https://arxiv.org/html/2605.24956v2
- NITP v3 HTML: https://arxiv.org/html/2605.24956v3
- NITP official artifact/status: https://github.com/aHapBean/NITP

## 2026-08-14 Final Source-Family Books Integration Ledger

WorldKV 的 2026-08-13 独立 Gate 已并入本账本。最终计数为 31/31：22 Refine、6 No Change、
3 Weekly Only / Record Only。

| Source Family | Final Disposition | Stable Owner | Current / Legacy | Books Review Result |
| --- | --- | --- | --- | --- |
| Model-assisted discrete-geometry result | Weekly Only | — | — | Scientific milestone；human selection、verification 与工具环境不可折叠为自治机制 |
| Exploit-development capability measurement | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | 已有 target/environment/artifact/trace 与 dual-use retention contract |
| Empirical Research Assistance | No Change | `AGENT-WORKFLOW` | Ch81 / Ch77 | research workflow 的 human authority、claim evidence 与 artifact boundary 已覆盖 |
| HRM-Text | Refine | `MODEL-TRANSFORMER-LAYER` | Ch17 / Ch17 | fixed depth→shared recurrence→双时间尺度 recurrence；联合训练配方不归因于结构单项 |
| Code as Agent Harness | No Change | `AGENT-PLATFORM` | Ch84 / Ch80 | taxonomy 没有新增可执行机制；三平面与 owner 边界已有具体论点 |
| DelTA | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | token weighting 保持 reward-side gradient proxy，不升级为 causal process credit |
| SkillsVote | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | collection→profile→recommend→attribution→validation-gated evolution 生命周期已复核 |
| LongLive-2.0 | Refine | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | sequence ownership、mask compilation、halo 与 quantized KV identity 联合为 workload-shaped layout |
| OpenComputer | Refine | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | verifier-first synthesis、fixed-trajectory disagreement 与 bounded checker repair 已吸收 |
| OSCAR | Refine | `INFER-KV-CACHE` | Ch45 / Ch41 | tensor reconstruction→attention distortion objective→mixed-precision page lifecycle |
| EnvFactory | Refine | `AGENT-WORKFLOW` | Ch81 / Ch77 | source-grounded executable state 与 real-API conformance gap 已由 environment/artifact contract 承接 |
| Mix-Quant | Refine | `INFER-PD-DISAGGREGATION` | Ch55 / Ch51 | uniform→phase-aware precision→Decode-compatible KV handoff；局部 kernel 不等于 SLO |
| ACC | Refine | `TRAIN-DATA` | Ch27 / Ch23 | interactive verified trajectory→derived compiled context→direct-answer SFT，保留 lineage |
| GoLongRL | Refine | `TRAIN-GRPO` | Ch33 / Ch29 | heterogeneous reward normalization 与 task sampling mass 分开；solvability/eval leakage 保持边界 |
| WorldKV | Refine | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | world-state pressure handoff 给 KV tiering；cache placement 不拥有 world semantics |
| PlanningBench | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | constraint-derived tasks、shared verifier blind spot 与 rubric/global validity 已覆盖 |
| Gated DeltaNet-2 | Refine | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | fixed recurrent state 的 erase/read/write control 与 chunk training 分支已复核 |
| Post-Trained MoE / ZEDA | Refine | `MODEL-MOE` | Ch21 / Ch21 | static top-k→zero route→distilled dynamic compute；保留 original-expert fallback |
| SkillOpt | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | Skill 是 validation-gated external optimization state，不是自动权威 |
| Foundation Protocol | No Change | `AGENT-PLATFORM` | Ch84 / Ch80 | object/plane/checkpoint/evidence 已由具体章节拥有；early protocol 无新验证机制 |
| SciAtlas | Refine | `AGENT-RAG` | Ch76 / Ch72 | tri-path recall、typed graph expansion 与 RWR 归 retrieval policy；无 benchmark 不写收益 |
| QUEST | Refine | `TRAIN-DATA` | Ch27 / Ch23 | rubric tree、executable/open judge 与 source-aware context state 形成 synthetic data chain |
| ThriftAttention | Refine | `INFER-KV-CACHE` | Ch45 / Ch41 | low-precision base + selective high-precision promotion；paired cache/footprint/fallback 已吸收 |
| SkillEvolBench | Refine | `AGENT-MEMORY` | Ch77 / Ch73 | replay/local repair 与 frozen transfer 分开；更新量不等于可迁移 abstraction |
| NITP | Refine | `TRAIN-PRETRAINING` | Ch28 / Ch24 | NTP + stop-gradient next-state latent supervision；revision/theory/code-missing boundary 保留 |
| OpenAI layered content provenance | Refine | `PLATFORM-SECURITY` | Ch72 / Ch68 | C2PA metadata + embedded signal + verifier；negative detection 不能证明非 AI |
| NVIDIA verified Agent Skills | Refine | `AGENT-PLATFORM` | Ch84 / Ch80 | source/scan/card/signature/catalog/sync pre-admission chain；不等于 runtime safety |
| NVIDIA Slurm topology scheduling | Refine | `PLATFORM-GPU-SCHEDULER` | Ch63 / Ch59 | inventory→segment→gang feasibility→placement；simulation 不外推 production |
| NVIDIA Agent evaluation guide | No Change | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | trajectory/evidence/environment identity 已具体覆盖 |
| Transformers v5.9.0 | Weekly Only | — | — | Version Fact，无新长期机制 |
| NVIDIA token-metered architecture | Weekly Only | — | — | Low-score commercial reference；metering correctness 与 SLO mechanism 未披露 |

### Owner Review

17 个 Stable Node owners 被修改或重新验证：`MODEL-TRANSFORMER-LAYER`、`TRAIN-GRPO`、
`AGENT-PLATFORM`、`TRAIN-DISTRIBUTED-TRAINING`、`PLATFORM-EVALUATION-SYSTEM`、
`INFER-KV-CACHE`、`AGENT-WORKFLOW`、`INFER-PD-DISAGGREGATION`、`TRAIN-DATA`、
`MULTIMODAL-WORLD-MODELS`、`MODEL-LONG-CONTEXT`、`MODEL-MOE`、`AGENT-RAG`、
`AGENT-MEMORY`、`TRAIN-PRETRAINING`、`PLATFORM-SECURITY` 和 `PLATFORM-GPU-SCHEDULER`。
其中 17 个均承接至少一项 Refine，No Change family 复用其中已有具体论点。

本周实际新增或强化 recurrence、dynamic MoE compute、KV quantization objective、phase precision、
verifier-first task synthesis、content provenance、Skill pre-admission 与 topology segment scheduling。其他
Refine family 已在当前 Data、GRPO、Workflow、RAG、Memory、Evaluation 与 World Model 演进线中逐项复核，
没有复制论文摘要。Archive/Discovery Gate 只因 cross-index recall 保持 Open。
