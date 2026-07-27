# AI Research Weekly — 2026-W25

> Coverage Window: 2026-06-15～2026-06-21
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 35/35 final dispositions; 32/34 `20+` Full Source Reviews complete; 24 Refine, 7 No Change, 1 Weekly Only, 1 Emerging, 2 Unverified / Blocked; Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; Books cursor advances to W26

## Executive Summary

旧版 W25 的三行评分至少包含四个 Source Families，不能替代整周候选发现。baseline 中 OpenAI 发布
LifeSciBench 与 near-autonomous AI chemist 工作，Anthropic 发布 agentic coding / expertise 研究及
Project Fetch phase two。本轮重放 Hugging Face 的 “Jun 14～20” 展示窗，并以 arXiv v1 日期重新归周，
新增 14 个首轮窗口内 families；重放下一周 feed 后又恢复 14 个 v1 实际落在 06-15～06-21 的
spillback，包括 OpenRath、JetFlow（旧账名 JetSpec）、GateMem、PlanBench-XL 与 Agent context/memory candidates。另有
10 项回拨 W24、3 项回拨 W23、1 项回拨 W22。聚合页的展示日与后续 revision 均不替代
first-public date。

fixed-source scan 恢复 vLLM v0.23.0。官方 release 页面实际显示 2026-06-15，故归 W25；其
408 commits 不按功能列表写入，而聚合为 state/lifecycle contract：pluggable KV spec 与 multi-tier offload、
speculative/prefix correctness、PP-aware connector handshake、Model Runner/frontend/parser 演进及 untrusted-input
hardening。同周 NVIDIA MoE fused kernels 与 MLPerf Training v6.0 也完成联合核验：前者提供
`GEMM epilogue fusion + sync-free launch + communication headroom` 的受限机制证据；后者把 DeepSeek-V3
与 GPT-OSS-20B 两类 MoE workload 纳入有收敛门槛的 full-system training benchmark。两者都不能由
厂商百分比外推成跨模型、硬件、规模或 SLO 的通用结论。

本检查点全文阅读 TokenPilot 的正文、公式、实验、ablation、limitations、全部 Appendix 与作者仓库。
它揭示一个容易被 Weekly 摘要抹掉的系统关系：Context token 数量、prompt-prefix identity、cache
hit/miss 与 task utility 是相互耦合的控制变量。频繁压缩虽减少文本，却可能破坏 byte-identical prefix；
延迟 eviction 保住 cache，又可能扩大 active working set。真正机制是 ingestion-time canonicalization、
可恢复的原始 artifact、segment lifecycle 与 batch-gated eviction，而不是“摘要越短越省钱”。

## Coverage and Source Coverage

- 模型与研究机构：保留 Anthropic 6 月 16/18 日与 OpenAI 6 月 17 日官方研究；NVIDIA 6 月 15 日
  MoE fusion 技术文档完成 mechanism review；World-Action Models 长文属于既有研究路线综述，未作为
  独立新机制事件重复计分。
- 论文与学术来源：完成 Hugging Face W25 首轮 recall 与 27 项 metadata/submission-history 核验；
  14 项归 W25，13 项按 v1 回拨 W22～W24。TokenPilot 已读 arXiv v1 全文、全部 Appendix 与
  LightMem2 当前公开 artifact；Scholar/OpenAlex/DBLP cross-check pending。
- AI Infra：TokenPilot artifact 已核对 component/preset/adapter/recovery-tool 和 experiment surface；
  当前仓库在 06-28 后扩展的 Codex/Claude Code adapter 不能倒写为 06-15 论文的 evaluation contract。
  fixed list 重扫已完成 vLLM v0.23.0、NVIDIA MoE fusion 与 MLPerf Training v6.0；SGLang、
  TensorRT-LLM、DeepSpeed 与 Transformers 的官方 release 面未发现可可靠归入本周的独立 material release，
  搜索聚合页中的 later/current release 不倒写为 W25 事件。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Near-autonomous AI chemist | 4 | 4 | 4 | 5 | 4 | 4 | 25/30 | Must Read |
| LifeSciBench | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Worth Watching |
| Agentic coding and expertise | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Worth Watching |
| Project Fetch phase two | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Record Only |
| Looped World Models | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full review complete — provisional Refine Ch10 / Experimental |
| LoopCoder-v2 | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full review complete — provisional Refine Ch22 / Experimental |
| On-policy Self-distillation for dLLMs | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch25 / Experimental |
| Zone of Proximal Policy Optimization | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Integrate Ch29 / Experimental |
| GameCraft-Bench | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — No Change Ch62 / Experimental case |
| Predictive Validity for Agent Evaluation | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full review complete — No Change Ch62 / Position paper |
| OPD-Evolver | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch73 / Experimental |
| LLM-Designed Training Environment | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Unverified / Blocked Backlog — score provisional |
| EfficientRollout | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch44 / Experimental |
| Persistent-State World-Model Evaluation | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch62 / Experimental |
| SAE Post-Intervention Recovery | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch5 / Experimental |
| Variable-Width Transformers | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch17 / Experimental |
| Context-Aware RL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch29 / Experimental |
| TokenPilot | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Must Read — full review complete |
| MemSlides | 4 | 3 | 4 | 3 | 5 | 5 | 24/30 | Full review complete — provisional Refine Ch73 / Experimental |
| PlanBench-XL | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — No Change Ch62 / Experimental case |
| Grouped Query Experts | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch21 / Experimental |
| OpenRath | 5 | 5 | 5 | 3 | 5 | 4 | 27/30 | Full review complete — provisional Refine Ch80 / Reference Architecture |
| JetFlow | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch44 / Experimental |
| EvoEmbedding | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch72 / Experimental |
| GateMem | 5 | 5 | 5 | 3 | 5 | 4 | 27/30 | Full review complete — provisional Integrate Ch68 / Experimental |
| PerceptionDLM | 5 | 4 | 4 | 3 | 5 | 1 | 22/30 | Full review complete — Emerging / Experimental Ch17 |
| MobileForge | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full review complete — provisional Refine Ch29 / Experimental |
| MemGUI-Agent | 4 | 4 | 5 | 3 | 5 | 4 | 25/30 | Unverified / Blocked Backlog — score provisional |
| Confident Layer Decoding | 4 | 4 | 4 | 3 | 4 | 5 | 24/30 | Full review complete — provisional Refine Ch20 / Experimental |
| Discretizing Reward Models | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full review complete — provisional Refine Ch27 / Experimental |
| Micro-Reflective Self-Distillation | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full review complete — provisional Refine Ch25 / Experimental |
| Deep Research in Physical Sciences | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full review complete — No Change Ch62 / Domain case |
| vLLM v0.23.0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Must Read — full review complete; versioned runtime evolution |
| NVIDIA sync-free MoE fused kernels | 4 | 5 | 5 | 5 | 5 | 3 | 27/30 | Must Read — full review complete; bounded mechanism evidence |
| MLPerf Training v6.0 | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Must Read — full review complete; benchmark-contract evolution |

当前账目为 35 行：24 个 `25～30`、10 个 `20～24`、1 个 `<20`。32 个 `20+` families 已完成 Full
Source Review，2 个仍为 `Unverified / Blocked Backlog`。逐项 Books disposition 已完成：24 Refine、
7 No Change、1 Weekly Only、1 Emerging、2 Unverified / Blocked。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows / source families | 4 / 4 | 3/3 `20+` reviews；1 项低分 boundary review |
| Recovered in-window academic families | 28 | 首轮 14 + W26 feed spillback 14；26/28 完成 Full Source Review；2 Unverified / Blocked Backlog |
| Fixed official / Infra families reviewed | 3 | vLLM v0.23.0、NVIDIA MoE fusion、MLPerf Training v6.0 完成 primary-source review |
| Recorded `20+` candidates | 34 | 24 high / 10 mid；六维合计已复算 |
| Earlier-week spillbacks | 14 | 10 项回拨 W24、3 项回拨 W23、1 项回拨 W22 |
| Academic discovery window | Open | HF first pass complete；cross indexes pending |
| Official / Infra fixed checkpoint | Passed | 3 families complete；remaining fixed release surfaces reviewed with no additional material W25 event |
| W25 academic Candidate Gate | Passed with explicit blocked ledger | 32/34 `20+` Full Source Reviews；2/34 Unverified / Blocked Backlog；0 ordinary pending |
| W25 discovery / Historical Evidence Gate | Open | 2 blocked families 与 academic cross-index 未闭合；post-forward cursor advances to W26 |

## Deep Analysis — Artifact-Producing Agent 的成功是闭环属性

真实实验将模型输出连接到昂贵或不可逆外部动作。价值来自闭环：提出方案、选择工具、
执行、观测、修正和专家验收；新增问题是实验资源、权限、安全、measurement noise 与
recovery。关系是从 answer benchmark 到 executable workflow 的 `Direct Evolution`，但
“near-autonomous”不能省略 human selection 与验证边界。

## Deep Analysis 2 — Context Reduction 必须与 Prefix Identity 联合优化

### Why → Principle → Mechanism

长 Agent trajectory 的直观解法是删掉旧文本；原始 full history 在短任务中最忠实、最透明，
但在长 session 中会反复 Prefill、占用 KV capacity 并放大成本。问题在于，任意位置的删除、摘要或
tool schema 抖动会改变 token layout，使 provider 的 prompt cache 从变便宜的 cache read 退回昂贵的
cache miss。于是“token 更少”与“实际 inference 更便宜”不是同一个 objective。

TokenPilot 把控制拆成两层。Global ingestion layer 在内容进入 canonical history 之前替换 volatile
markers、移动易变 tool schemas、去重和缩减 environment observation；被裁剪原文写入按 content hash
索引的 artifact registry，并提供 recovery tool。Local lifecycle layer 为 segment 维护
`active → completed → evictable` 状态，只有 completion evidence 已出现且 residual utility 归零时，
才在 batch interval 执行一次 structural purge。State estimator 只提出 delta，registry 验证合法转换；
Context working set、artifact truth 与 cache identity 因而由不同 owner 管理。

### Trade-off → Connection → Evolution

```text
unbounded full history
→ token/sentence compression（减少文本，但可能打碎 prefix）
→ summary / demand paging（控制 working set，但引入信息损失与 mutation）
→ ingestion-time canonicalization + recoverable artifact
→ lifecycle-aware delayed eviction
→ 联合观测 token utility、prefix hit/miss、task score 与 recovery
```

这不是对旧方案的覆盖。短 trajectory 或 backend 不支持 prefix cache 时，full Context/简单截断仍可更
可靠；future query 不可预测时，semantic retrieval 仍有价值；写入时知道精确 artifact 的场景才适合
hash dereference。新机制引入 estimator misclassification、stale residual utility、artifact availability、
schema relocation semantics、batch tuning、delete propagation 与跨租户 cache identity。它与 Ch71
Context、Ch73 Memory 和 Ch41/43 prefix/KV cache 是 `Layering / Dependency`，不是同一层实现。

## Evidence Level

OpenAI 与合作方报告证明具体实验事件；LifeSciBench 是发布方 benchmark；Anthropic 报告受产品用户
样本限制。TokenPilot 的机制与结果来自作者 arXiv v1 和 artifact：论文比较 GPT-5.4-mini backbone、
Qwen3.5-35B-A3B estimator、PinchBench 123 tasks 与 Claw-Eval General 161 tasks，并用 provider API
返回的 cache-hit/miss token 与当时披露价格计算成本。它没有证明跨模型、跨 provider、GPU wall-clock、
任意混合 workload 或无 prefix-cache backend 的通用收益；连续模式把同类别 tasks 相邻排列，也可能高估
高度异构真实流量的 prefix reuse。其余 13 个新增候选只完成 metadata/abstract/submission-history 发现。

vLLM v0.23.0 的证据来自 signed official release 与 directly linked PR ledger。它证明 runtime state surface
继续从单层 GPU KV 扩展到 pluggable spec、object-store secondary tier、per-request offload policy、PP-aware
connector handshake、speculative/prefix correctness 与 parser/frontend protocol；不证明 release 中任一性能
百分比跨 model/shape/hardware/SLO 成立，也不证明 408 commits 形成单一架构跃迁。release 页面显示 06-15，
W24 搜索结果中的 repository badge 日期不能替代 tag event date。

NVIDIA MoE fusion 的证据来自 NVIDIA 技术文档、cuDNN Frontend grouped-matmul/dGLU API 与公开调用入口；
它证明特定 SM100/GB200 路径能够把 activation、quantize/transpose、部分 scale/clamp 与 grouped GEMM
epilogue 合并，并通过不依赖 host token-count synchronization 的调度支持 full-iteration CUDA Graph 与通信
overlap。1.3x/2.1x kernel 及 8%/93% end-to-end 数字只属于作者披露的 GB200、DeepSeek-V3/GPT-OSS
内部配置；缺少完整 global batch、parallel degrees、sequence、optimizer、network、convergence 与 power/SLO
contract，故不进入通用事实。

MLPerf Training v6.0 的 benchmark ownership 来自 MLCommons release、reference implementations、rules、
公开 submissions 与 supplemental statements。它证明 suite 新增 671B total/37B active 的 DeepSeek-V3 和
21B total/3.6B active 的 GPT-OSS-20B，并要求 run 到 target quality；不证明所有 submitter 结果可跨 division、
规模、软件栈或 workload 横向合并。submitter supplemental statement 明确不代表 MLCommons 观点，NVIDIA
结果只保留为特定 entry/configuration 的 version fact。

## Cross-Week Deduplication

与 W16 GPT-Rosalind 属同一 science-model 路线：W16 是 domain model，W25 是 evaluation 与
executed-workflow evidence，关系为 `Layering`。TokenPilot 与 W24 End-to-End Context Compression
属于同一 Context-management 演进链，但前者明确把 prefix cache identity 和 segment lifecycle 放进
objective，不能只按“压缩比例”合并。Data Journalist Agent、Chatbot-to-Digital-Colleague、withdrawn
FastContext、Ling/Ring 2.6、APPO、HarnessX、RedAct、Hybrid Attention、visual repository Agent 与
Cross-Lingual BrowseComp-Plus 的 v1 落在 W24；Graph Memory 与 Program-of-Layers 落在 W23；
Smaller Models Are Natural Explorers 落在 W22，均不按 W25 feed 展示日重复计分。W26 display feed
中的 MemSlides、PlanBench-XL、GQE、OpenRath、JetFlow、EvoEmbedding、GateMem、PerceptionDLM、
MobileForge、MemGUI、Confident Layer Decoding、Discretizing Reward Models、Micro-Reflective
Self-Distillation 与 Deep Research v1 都落在 W25，因此回到本周而不留在 W26。
vLLM v0.23.0 与 W23 v0.22.1 是同一 Source Family 的 `Direct Evolution`：前者是大版本 runtime-state
扩展，后者是 Ray endpoint lifecycle patch；不能把两者合并为一个事件，也不能把 patch 倒写成 0.23 feature。
MoE fused kernels 与 MLPerf Training v6.0 形成 `Layering / Dependency`：前者解释一个 vendor stack 怎样
降低 grouped-expert execution 的 memory/synchronization cost，后者定义整系统必须在指定模型、数据、质量
门槛与 run rules 下交付的 workload。microkernel gain 不是 benchmark result，benchmark result 也不能反推
某一 fusion 是唯一原因。

## Knowledge Tree Position

Ch14～22 architecture/interpretability → Ch29 RL → Ch41/43 cache semantics → Ch44 speculative decoding
→ Ch62 Evaluation → Ch71 Context（TokenPilot 主 owner）→ Ch73 Memory → Ch74/77 workflow → Ch80 Platform。
vLLM v0.23.0 主映射 Ch46，由 Ch41/44/51/53/58/68 承接 KV、speculative、PD connector、compatibility、
frontend 与 security handoff。
MoE fusion 主映射 Ch21 的 routing-to-executable-shape 边界，由 Ch36 承接 EP/communication overlap、Ch45
承接 kernel execution；MLPerf Training v6.0 主映射 Ch62 benchmark contract，由 Ch24/32 提供 convergence
与 full-system training handoff。

## Recommended Action

普通 Source Review pending 已清零；两项 blocked family 按 blocked-skip 保留。TokenPilot 最终
`Refine — Existing Argument`：`AGENT-CONTEXT`（Ch75；Legacy Ch71）已有 compression loss、artifact reference 与 cache identity，
但尚未把 canonical prefix、ingestion-time reduction、recoverable artifact 和 delayed lifecycle eviction
组织成联合 objective；`AGENT-MEMORY` 只需要短 handoff。vLLM v0.23.0 最终由 `INFER-VLLM`（Ch50；Legacy Ch46）
`Refine — Existing Argument / Version-sensitive`：现有章节已拥有 object-store
offload 主线，但 release 形成更完整的 state-owner 证据——KV spec/allocator、per-request policy、connector
handshake、scheduler accounting、frontend/parser identity 与 input validation 必须共同演进；不复制 release list。
NVIDIA MoE fusion 最终 `Refine — Existing Argument / Bounded Case`：Ch21 已说明 executable expert shape，
新证据补足 training-side fusion、host-sync removal 与 SM-margin/communication overlap 的耦合；MLPerf v6.0
最终 `Refine — Existing Argument / Benchmark Contract`：Ch66 已有 subject/distribution/environment/scorer，
新证据补足 training benchmark 必须绑定 model/dataset/quality target/division/run aggregation。

## Event-Date Daily Decision

2026-06-15～06-18：Weekly only；回拨条目不补造历史 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete under blocked-skip`。near-autonomous chemist、LifeSciBench、Agent coding、
GameCraft、predictive-validity、PlanBench-XL 与 physical-science case 均由现有具体论点去重；Project Fetch 只保留
Weekly domain fact。24 个 Refine families 逐项检查 owner 与相邻章节，其中 World Model 两项先前已吸收，本轮
新增/增强 canonical Context lifecycle、typed runtime request revision、MoE fusion/headroom、training convergence
benchmark、Memory ACL/forgetting 与 typed Agent Session。PerceptionDLM 保持 Emerging；两项 blocked 不进正文。

## Ignored Noise

- 忽略 human review、实验设施、失败次数与资源预算的“自主科学家”表述。
- 把论文在特定商业价格与 task ordering 下的成本下降外推为 GPU latency、吞吐或所有 Agent 流量收益。
- 把当前 LightMem2 repository 的后续 adapter/release state 倒写为 06-15 论文已经实验验证的机制。
- 把 vLLM 408 commits 当作单一机制，把 vendor kernel 百分比外推到未披露 workload，或把 experimental
  Rust frontend、new connector 与 deprecation path 写成稳定跨版本 API。
- 把 NVIDIA `clean sweep`、per-accelerator normalization 或特定规模 time-to-train 外推为所有集群的
  cost/energy/reliability 结论；把 MLCommons 收录新 workload 等同于 endorse 某个 vendor 实现。
- World-Action Models、low-precision training 与 AR/XR agent 教程属于概念综述或 recipe，本周未提供足以
  独立计分的新 primary mechanism/event，保留在 source scan 而不制造候选。

## 2026-07-31 Full Re-Audit Addendum

- near-autonomous chemist 的官方报告与论文已联合复核。model proposal、expert selection、
  physical execution、measurement 与 independent replication 被写成 Ch77 的不同 state
  owners；不声称端到端自主科研。
- LifeSciBench 升级全文阅读，并与 exploit/N-day 共同支持 Ch62 的 artifact-producing
  evaluation。Project Fetch 保留 Weekly only。

## Full Source Review

### Near-autonomous AI chemist — 25/30

- **Source Family ID / Type / Date**：`GPT54-MOLECULEONE-CHEMIST`；OpenAI/Molecule.one
  2026-06-17 report、paper、experiment protocol 与 supporting artifact。
- **Full-read Coverage**：已覆盖 reaction objective、proposal/search loop、human/expert selection、
  robotic/physical execution、measurement、iteration、baseline、resource budget、failures、limitations
  和 independent replication boundary。
- **Problem / Previous Design / Changed Constraint**：human-designed experiment cycles reliable but slow；
  model+automation can expand proposal throughput, yet physical chemistry makes unsafe/invalid actions and
  measurement noise materially different from answer generation。
- **Mechanism / Ownership / Flow**：model proposes conditions and interprets results；expert approves scope/
  safety；automation executes；instrument produces measurement；workflow chooses next experiment；final claim
  requires expert review/replication。proposal、approval、execution、measurement、claim 各有独立 owner。
- **Evidence Boundary**：证明一个 bounded medicinal-chemistry reaction 在该 facility/protocol 中被改善；
  不证明 general chemistry autonomy、无人工闭环、safe transfer、novel drug discovery 或可跨实验室复制。
- **Trade-offs / Evolution**：answer→proposal→approved execution→measured feedback→replication 提高
  ecological validity，新增 reagent/robot budget、safety interlock、measurement drift、partial failure、
  rollback 和 artifact lineage；human-led experimentation 在高危险/弱 verifier 场景仍成立。
- **ROADMAP / Chapters / Decision**：Ch77 主 owner，已读 Ch62、Ch69、Ch74、Ch76～80；现有 Ch77
  已分离这些 state owners。`No Change — Already Covered`。

### LifeSciBench — 24/30

- **Source Family / Coverage**：`LIFESCIBENCH`；OpenAI 2026-06-17 announcement、full preprint、task set
  与 expert-author/review protocol；已读 domains、harness、grading、baseline、limitations/appendix。
- **Evidence / Limits**：expert-authored/reviewed tasks提高 domain validity，但仍测离线任务决策，不等于
  lab execution、clinical outcome 或 deployment safety；expert consensus、data access 和 tool scaffold
  影响结果。
- **Decision**：Ch62 主 owner；`No Change — Already Covered`，当前 evaluation 章节已区分 answer、
  artifact、environment opportunity 与 external outcome。

### Agentic coding and expertise — 22/30

- **Source / Coverage**：Anthropic 2026-06-16 report 已全文核对；样本约 40 万 Claude Code sessions、
  约 23.5 万用户，观察窗口为 2025-10～2026-04。
- **Evidence / Limits**：privacy-preserving observational study 能描述 sample 中的 tool/session patterns；
  expertise 与 success 相关不构成因果，也不能估计未观测失败、用户选择或所有 coding workflows。
- **Decision**：Ch62/63/77/78 已读；`No Change — Already Covered`。

### Project Fetch phase two — 18/30

- **Source / Coverage**：Anthropic 2026-06-18 Project Fetch phase-two report 已核对；公开证据仅三次
  Opus 4.7 trials，且研究者仍负责接线/审批，任务子集相对旧实验发生变化。
- **Evidence / Limits**：它证明特定 robotics setup 的 bounded demonstration，不支持与旧 human group
  的直接普遍比较，也不证明通用 robotics autonomy、无人监督 side effects 或 recovery reliability。
- **Decision**：Ch62/74/77/78 已读；`Weekly Only — Domain Experiment Fact`。

### TokenPilot — 27/30

- **Candidate / Week / Source Family**：`TOKENPILOT-CACHE-CONTEXT-LIFECYCLE`；W25；
  arXiv:2606.17016 v1 2026-06-15。论文标为 Work in Progress；作者仓库 06-16 release 与 06-28
  adapter update 只用于核验公开实现演进，不作为 W25 的新增论文事件。
- **Direct / Related Primary Sources**：arXiv metadata、完整 HTML/PDF 内容、全部 equations/tables/
  figures/Appendix A、LightMem2 repository README、architecture、host adapter、recovery MCP 与 experiment
  entrypoints。联读论文自己的 compression、paging、memory/context-management baselines；未用聚合页摘要
  替代正文。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Background、objective、global/local
  mechanisms、state machine、implementation、PinchBench/Claw-Eval isolated 与 continuous setup、全部
  baselines、overall/ablation/sensitivity、Limitations、Related Work、Conclusion、dataset、native graders、
  pricing model、thresholds、model assignments、state-estimator prompts 和 HTML EOF。
- **Original Problem / Previous Design / Changed Constraint**：full history 最忠实且天然保留 prefix，
  适合短 session；静态 compression、summary 或 demand paging 可控制 token growth。长 horizon 和跨任务
  cache reuse 出现后，任意 context mutation 可能把 cache hit 变为 full Prefill miss，因此仅最小化文本
  长度会优化错系统目标。
- **Mechanism / State Ownership**：Context objective 同时计 utility 与 hit/miss cost。Harness 在 ingestion
  boundary canonicalize volatile path/time/session markers、下移易变 tool schemas、hash 去重并压缩 tool
  observations；原文由 artifact registry 按 content hash 持有，recovery tool 可回读。Framework registry
  持有 segment 的 `active/completed/evictable` state；Qwen estimator 只输出 completion evidence 与 residual
  utility delta，registry 验证 transition，backend cache 只拥有物理 prefix blocks。
- **Control / Data Flow**：raw instruction/tool observation → deterministic stabilization/reduction → canonical
  history；oversized payload → preview + artifact pointer；每 `B` turns 读取 compressed view → estimator delta
  → validated registry update；只有 `completed` 且 residual utility empty 才 purge，missing detail 则通过
  recovery tool reinject 并提升后续保留策略。
- **Implementation Details**：论文实验使用 GPT-5.4-mini 作为 Agent backbone、Qwen3.5-35B-A3B 作为
  zero-shot state estimator、`B=3`；Appendix 披露 tool-output thresholds、preview prefix/suffix、dedup/frequency、
  HTML/layout cleaning 与完整 estimator prompts。阈值是该实现参数，不是通用标准。当前 repository 已把
  stabilizer/reduction/eviction 组成 preset，并分离 OpenClaw/Codex/Claude Code adapters；这是后续版本事实。
- **Evaluation Contract**：PinchBench frozen snapshot 为 123 tasks，Claw-Eval General 为 161 tasks；均测
  isolated 与 continuous，continuous 将同类别 tasks 连续排列，并按 task boundary slice 后送原生 grader。
  task score、cache-read/miss/output tokens 与当时 commercial price 共同构成结果；未披露 GPU、server
  concurrency、batch、TTFT/TPOT、power 或端到端 SLO。论文比较 LLMLingua-2、SelectiveContext、LCM、
  Pichay、Summary、MemoBrain、AgentSwing、Keep-Last-N、MemOS，并做 global/local、recovery、batch interval
  与 residual-utility ablations。
- **What the Evidence Proves**：在上述 model、provider cache metadata、price、benchmark、task ordering
  与配置中，canonical prefix 明显把 miss 转为 read，ingestion reduction 和 delayed eviction 进一步降低
  token/cost，同时未使 aggregate task score 低于作者对照；removing recovery tool 与 immediate eviction
  分别暴露 retry inflation 和 re-exploration failure。
- **What It Does Not Prove / Limitations**：不证明所有模型/provider/自托管 GPU 都有相同经济收益，不证明
  cost reduction 等于 wall-clock latency/goodput 改善，也不证明 Qwen estimator 对开放、异构或 adversarial
  traces 可靠。作者明确指出 ambiguous/sparse interactions 会误分类，`τ/B` 需按 workload 调整，无 prefix
  caching backend 无稳定化收益；同类别连续排列对高度 shuffled workloads 的外推受限。
- **Trade-offs / New Failure Modes / Previous Design**：获得 prefix reuse、bounded working set 与原文恢复，
  新增 canonicalization compatibility、schema-relocation semantics、estimator drift、premature/stale eviction、
  artifact availability、pointer authorization、delete propagation 与 batch lag。短 session、strict full-fidelity、
  backend 无 cache 或 future relevance 无法判断时，full Context/保守截断仍合理；semantic retrieval 仍负责
  未知关联，exact hash dereference 只负责已知 artifact。
- **Evolution / ROADMAP / Chapters / Decision**：`Layering / Dependency`：Ch71 主 owner，Ch73 负责 durable
  artifact/memory lifecycle，Ch41/43 解释 prefix/KV cache，Ch66 负责 cost contract。已读 Ch70～73、Ch66
  及 cache handoff。`Refine — Existing Argument (provisional)`；Historical Books Gate 关闭，未改 Books。

### Looped World Models — 26/30

- **Source / Coverage**：已读 arXiv:2606.18208 v1 的 architecture、spectral stability、variable-depth training、
  early exit、deferred decoding、ScienceWorld/ALFWorld experiments、broader impacts 与全部结果附录；论文没有
  独立 Limitations section，hardware、并发、能耗与运行时实现细节记为 `Not Disclosed`。
- **Problem / Mechanism / Ownership**：固定深度 world model 每个 transition 支付同样计算，长 rollout 又会累积
  误差。LoopWM 用共享 Transformer block 反复更新 latent dynamics state，以负对角参数化约束线性 retention；
  halting policy 分配 inner-loop depth，deferred decoder 可先推进多个 latent steps 再解码 observation。encoder、
  action embedding、latent transition、exit policy 和 prediction heads 是不同 state owners。
- **Evidence Boundary / Trade-off**：ScienceWorld/ALFWorld 与约 1B model 的实验支持 parameter sharing、adaptive
  depth 和 deferred decoding 的 feasibility，不证明“谱约束”消除 nonlinear/outer-rollout error，也不证明真实
  robotics 或 video world models 获得相同收益。参数效率交换更多 sequential loop latency、halting calibration、
  latent drift 与 observability；固定深度在简单、低延迟、易编译 workload 仍合理。
- **Evolution / ROADMAP / Decision**：`fixed-depth transition → shared recurrent depth → variable-depth training
  → adaptive exit → deferred latent rollout` 是 `Direct Evolution`。已读 Ch10、Ch17、Ch22 及 Ch74；主 owner
  Ch10，Ch22 handoff。provisional `Refine — Existing Argument / Experimental`。

### LoopCoder-v2 — 26/30

- **Source / Coverage**：已读 arXiv:2606.18023 的 recurrent-depth background、parallel loop transformer、
  context-aware loop routing、training、coding evaluation、efficiency analysis 与 conclusion；未找到独立 Limitations
  或完整 systems SLO section。
- **Mechanism / Ownership**：旧 sequential loop 重算并为每轮保存 KV；PLT 让后续 loops 共享第一轮 KV，使用
  gated sliding-window attention，并以 cross-loop position offset 解除 loops 间依赖。LoopCoder-v2 再让 controller
  按 input/position 分配 loop computation。第一轮 KV 是 immutable shared context，当前 loop 保有 local KV，gate/
  controller 拥有 compute-routing state。
- **Evidence Boundary / Trade-off**：7B coding model 的 benchmark 支持作者训练配置中的 quality/compute 分支，
  与大模型/API 分数并列不能建立 matched comparison。共享 KV 将 memory 从随 loop count 线性增长变成 bounded，
  但可能形成 stale representation；并行 loop 降低串行依赖，却新增 gate、position-offset、compile 和 cache-layout
  contract。单轮模型在 latency 与 implementation simplicity 优先时仍合理。
- **ROADMAP / Decision**：主 owner Ch22，Ch13/45 handoff；provisional `Refine — Existing Argument /
  Experimental`，不把作者 coding leaderboard 外推为通用 test-time scaling。

### On-policy Self-distillation for dLLMs — 25/30

- **Source / Coverage**：已读 arXiv:2606.18195 的 dLLM preliminaries、self-future teacher、step-level divergence、
  d-OPSD、LLaDA-8B experiments、retaining-ratio ablations、appendices 与 conclusion；没有独立 Limitations section。
- **Mechanism / Ownership**：AR self-distillation 可在 prompt 注入 privileged answer；dLLM 的 arbitrary-order
  denoising 允许把同一次 on-policy sample 的未来已揭示 tokens 作为 teacher condition，再对当前 denoising step
  做 distribution divergence。student/teacher 共享 weights，差异来自 mask/condition state，而非独立 teacher
  checkpoint；sampling policy、teacher mask 和 loss reducer 必须保持同一 rollout identity。
- **Evidence Boundary / Trade-off**：LLaDA-8B 在 GSM8K、MATH500、Sudoku、Countdown 的结果支持特定 diffusion
  reasoning workload，不证明 AR LLM、开放 reward 或多轮 Agent。未来信息提高 dense supervision，但可能产生
  leakage-like train/inference mismatch、teacher self-confirmation 与 full-vocabulary cost；普通 SFT/RLVR 在输出顺序
  固定或只需 outcome reward 时仍合理。
- **ROADMAP / Decision**：主 owner Ch25，Ch29 handoff；provisional `Refine — Existing Argument /
  Experimental`。它是 `same-model privileged conditioning`，不能与 independent teacher distillation 合并。

### Zone of Proximal Policy Optimization — 25/30

- **Source / Coverage**：已读 arXiv:2606.18216 的 prompt-level teacher construction、replay、algorithm、
  LLM/VLM/video multi-scale experiments、bootstrap、component ablations、limitations 与 appendices。
- **Mechanism / Ownership**：小模型在 hard prompts 上可能所有 rollout 都失败而获得零 advantage；直接使用 teacher
  response 又破坏 on-policy。ZPPO 把 teacher 帮助放进 prompt，促使 student 自己生成成功 trajectory，再将这些
  prompt/trajectory 进入 replay 与 RL 更新。teacher 只拥有 prompt-side hint，student policy 拥有 action tokens，
  buffer 必须保存 behavior/prompt revision，reward/verifier 拥有 outcome。
- **Evidence Boundary / Trade-off**：作者跨 0.8B～9B 与多模态 benchmark 的 macro result 说明 hard-example
  recovery 可能改善；bootstrap 只衡量 benchmark-selection robustness，不是 per-run uncertainty。teacher hint 仍可能
  泄漏答案、改变任务、造成 curriculum lock-in；纯 on-policy RL 在 student 已有 nonzero success 时更干净，offline
  distillation 在部署不需探索时更便宜。
- **ROADMAP / Decision**：主 owner Ch29，Ch23/25 handoff；provisional `Integrate — New Mechanism /
  Experimental`，Books Gate 关闭。

### EfficientRollout — 27/30

- **Source / Coverage**：已读 arXiv:2606.18967 的 rollout roofline、quantized self-drafter、SD toggle、adaptive
  draft length、system implementation、full experimental appendix、baselines 与 failure analysis；无独立 Limitations
  section，未披露项不补造。
- **Mechanism / Ownership**：RL rollout 的长尾阶段 active batch 缩小，闲置 compute 可用于 speculative drafting；
  target policy 持续更新又使独立 drafter stale。系统从当前 policy 派生 weight-quantized self-drafter，按 roofline/
  runtime regime 决定是否启用 SD，并依据 acceptance history 调整 draft length。policy checkpoint、quantized draft
  revision、accept/reject state 与 scheduler toggle 必须同一训练 step 可追踪。
- **Evidence Boundary / Trade-off**：Qwen/Llama 多尺寸实验显示某些 baseline 加速、某些明显减速，直接证明
  “有 drafter”不等于收益；作者 acceptance 只在披露的 RL setup 有效。self-draft 降低 staleness，却增加 quantize/
  refresh、toggle misprediction、rollback 与 training-step coupling；高 occupancy 或低 acceptance 时普通 decoding
  仍合理。
- **ROADMAP / Decision**：主 owner Ch44，Ch29/52 handoff；provisional `Refine — Existing Argument /
  Experimental`。它把 speculative policy 从 static serving config 演进为训练中动态 runtime control。

### SAE Post-Intervention Recovery — 25/30

- **Source / Coverage**：已读 arXiv:2606.18322 的 threat model、valid-flip filtering、TPP、orthogonal/Jacobian
  recovery、multi-layer defense、behavior experiments、all appendices 与 Limitations。
- **Mechanism / Evidence Boundary**：SAE feature clamp 能改变行为，只证明它是 causal handle，不证明它形成完整
  bottleneck。攻击在 clamp 保持激活时寻找小 residual perturbation；多层版本用 defended-feature map 的 Jacobian
  将 recovery gradient 投影到一阶不改变被守特征的子空间。实验支持所测模型/behaviors 的 bypassability，不证明
  所有 SAE intervention 无效，也不证明优化攻击代表自然 deployment distribution。
- **Trade-off / Previous Design**：单特征干预易解释但有旁路；多层/Jacobian defense覆盖更广，却成本更高、仍只
  局部一阶，并扩大 false confidence。mechanistic evidence 应同时报告 intervention effect 与 adversarial recovery，
  旧 correlational probe 仍适合 hypothesis generation 而非控制保证。
- **ROADMAP / Decision**：主 owner Ch5，Ch62/68 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Variable-Width Transformers — 25/30

- **Source / Coverage**：已读 arXiv:2606.18246 的 width schedule derivation、residual resize、dense/MoE pretraining、
  compute/KV analysis、downstream evaluation、limitations 与 appendix。
- **Mechanism / Ownership**：constant width 易实现且 residual/KV layout 统一；论文用先收窄后扩宽的 `><` shape，
  由 bottleneck layer/index 解出各层 width，并在跨层边界显式 resize residual。每层 attention/MLP 拥有 local width，
  resize projection 拥有 representation handoff，KV cache 随 layer width 变化，checkpoint/runtime 必须记录 shape map。
- **Evidence Boundary / Trade-off**：200M～2B dense 与 3B/1B-active MoE、10B～100B tokens 支持作者规模下较低
  loss/FLOPs/average KV width，不证明 frontier scale、真实 kernel utilization 或 distributed serving latency。更小平均
  width 交换 irregular shapes、extra projections、kernel fragmentation 与 checkpoint complexity；constant width 在
  Tensor Core regularity/生态兼容优先时仍合理。
- **ROADMAP / Decision**：主 owner Ch17，Ch19/45 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Context-Aware RL — 25/30

- **Source / Coverage**：已读 arXiv:2606.17053 的 contrastive context objective、Agent/multimodal experiments、
  training setup、12 multimodal benchmarks、ablations、limitations 与 broader impacts。
- **Mechanism / Evidence Boundary**：outcome-only reward 可能让模型猜对答案却忽略 observation/context；方法加入
  matched positive/negative context pairs，使 policy 对 context-grounded trajectory 建立相对偏好。证据覆盖特定
  VLM 与 Agent tasks，不能证明真实 tool state 的 provenance、因果 grounding 或 adversarial context robustness。
- **Trade-off / Previous Design**：contrastive pairs 增强 context sensitivity，也增加 negative construction bias、
  leakage、reward scaling 与 rollout length sensitivity。纯 outcome RL 在 verifier 完整且 context 不关键时更简单；
  process supervision 在能可靠标注中间 grounding 时更直接。
- **ROADMAP / Decision**：主 owner Ch29，Ch71/74 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Grouped Query Experts — 25/30

- **Source / Coverage**：已读 arXiv:2606.20945 v1 的 GQA/MoE formulation、query-head experts、compute profile、
  30B-token experiment、routing/output ablation、throughput、limitations 与 appendix。
- **Mechanism / Ownership**：GQA 共享 KV heads 以减少 cache；GQE 在每个 KV group 内保留 shared K/V，却让 router
  为 query representation 选择少量 query/output experts。KV identity 因而不随 expert 选择复制，router 只改变
  Q/O compute path；runtime 必须把 group assignment 映射成 irregular head batches。
- **Evidence Boundary / Trade-off**：小规模 pretraining 支持 capacity-without-KV-duplication 的可行性，不证明
  frontier quality、load balance、All-to-All 或 decode latency。它减少 KV growth，却新增 head routing、expert
  imbalance、grouped kernel 与 checkpoint mapping；标准 GQA 在稳定吞吐、可移植实现优先时仍合理。
- **ROADMAP / Decision**：主 owner Ch21，Ch15/19/45 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### JetFlow — 27/30

- **Source / Coverage**：已读 arXiv:2606.18394 v1 的 scaling model、parallel tree drafting、training objective、
  verification flow、GSM8K/MATH-500 evaluation、learning-rate/loss-weight ablations 与 appendix；没有独立末尾
  Limitations section。
- **Mechanism / Ownership**：传统 tree speculation 常串行扩展 draft branches，tree 越宽 drafting critical path 越长。
  JetFlow 并行生成树节点并训练 branch distribution，使 verifier 一次处理候选 tree；drafter 拥有 proposal topology，
  target 拥有 acceptance 与 residual sampling，KV manager 必须按 accepted path commit、按 rejected branches 回收。
- **Evidence Boundary / Trade-off**：作者数学/小模型 setup 的 speedup 与 accepted length 支持 parallel tree 的
  feasibility，不证明 production batch、long context、GPU utilization 或任意 target distribution。并行树减少 depth
  latency却增加 width compute、KV workspace、verification padding 与 rollback；单链 speculation 在 batch/显存受限
  时仍合理。
- **ROADMAP / Decision**：主 owner Ch44，Ch41/45/52 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### PerceptionDLM — 22/30

- **Source / Coverage**：已读 arXiv:2606.19534 的 diffusion-LM background、parallel region perception、training
  data、DLC-Bench/multimodal evaluation、single-region regression ablation、limitations 与 appendix。
- **Mechanism / Evidence Boundary**：AR VLM 顺序描述 regions；diffusion language model 可同时去噪多个 masked
  region slots并交换 global context。实验支持所测 perception tasks 的 parallel coordination，不证明生成 latency、
  general reasoning 或任意 vision backbone 优势；作者承认单-region quality 仍与 AR 存在差距。
- **Trade-off / Previous Design**：parallel regions 减少串行依赖，却新增 denoising schedule、region collision、
  stopping 与 serving support；AR 在高质量单对象、成熟 KV/runtime 生态中仍合理。
- **ROADMAP / Decision**：主 owner Ch17，Ch38/42 handoff；`Emerging / Experimental`，不预设 Books 必改。

### Confident Layer Decoding — 24/30

- **Source / Coverage**：已读 arXiv:2606.21906 的 alignment-tax hypothesis、entropy-trough selection、fallback、
  graph-safe/continuous-batching implementation、experiments、ablations、limitations 与 appendix。
- **Mechanism / Evidence Boundary**：系统保留完整 forward pass，但在当前 token 的 intermediate layer 出现可信
  entropy trough 时，从该层 unembedding 读取 next-token distribution；可选 fallback 回到 final layer。实验支持
  所测 instruct/base models 的 inference intervention，不证明浅层 vocabulary alignment 普遍可靠，也未分离 MoE
  routing 与 depth confound。
- **Trade-off / Previous Design**：不提前停止 compute，主要改变 logits owner，因此不是传统 early exit；收益是
  绕开后层 alignment drift，代价是多层 logits/entropy、buffer、calibration 与 batch divergence。final-layer decoding
  仍是最稳定语义；训练期修复比 inference workaround 更根本。
- **ROADMAP / Decision**：主 owner Ch20，Ch42/52 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Discretizing Reward Models — 24/30

- **Source / Coverage**：已读 arXiv:2606.21795 的 predictive-variance estimation、reward clustering/discretization、
  preference evaluation、MC-dropout ablations、limitations 与 appendix。
- **Mechanism / Evidence Boundary**：连续 reward score 的微小数值差可能低于 model uncertainty，却在 policy update
  中被当作精确间隔。方法用 MC-dropout 估计 predictive variance，再把不可可靠区分的 score 区间离散成 ordinal
  levels。实验支持所测 reward models 的 robustness，不证明离散 level 是真实 human utility，也不覆盖在线 policy
  shift。
- **Trade-off / Previous Design**：discretization 降低虚假精度和 scale sensitivity，却牺牲细粒度 ranking，并新增
  uncertainty estimator、bin revision 与 tie handling。连续 reward 在 calibration 可靠、需要微小排序时仍合理。
- **ROADMAP / Decision**：主 owner Ch27，Ch29/62 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Micro-Reflective Self-Distillation — 24/30

- **Source / Coverage**：已读 arXiv:2606.18844 的 error localization、micro-reflective trajectory synthesis、
  decoupled advantage、training stabilization、experiments、internalization analysis、ablations 与 conclusion；没有
  独立末尾 Limitations section。
- **Mechanism / Evidence Boundary**：不是让 student 模仿单一 teacher trajectory，而是从自身失败中定位局部错误，
  构造“错误→反思→修正”短片段并估计其局部 advantage。实验支持作者 math/reasoning setup 的 capability transfer，
  不证明 self-generated diagnosis 正确、跨域稳定或免于 self-confirmation。
- **Trade-off / Previous Design**：局部反思降低长轨迹 imitation burden，却依赖 error segmenter/verifier，并新增
  trajectory selection bias。完整 teacher distillation 在 teacher 显著更强时仍合理，outcome RL 在局部错误不可标注
  时更直接。
- **ROADMAP / Decision**：主 owner Ch25，Ch76/29 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### GameCraft-Bench — 25/30

- **Source / Coverage**：已读 arXiv:2606.17861 的 Godot task construction、140 tasks/15 families、quality
  control、execution/replay protocol、seven agent configurations、judge reliability、diagnostics 与 limitations。
- **Mechanism / Evidence Boundary**：Agent 交付完整 game project，并提交可重放 gameplay traces；evaluator 将 build
  success、valid replay、mechanics、content depth、visual function 与 presentation 分开。它证明可执行 artifact 加
  interaction evidence 能揭示“项目能启动但不可玩”的失败，不证明 Godot 覆盖所有 software engineering，也不能将
  harness+model 分数当纯模型能力。
- **Trade-off / Previous Design**：静态 unit tests 易重复却难验证交互体验；replay/rubric 更贴近 outcome，但增加
  engine nondeterminism、trace selection、judge variance 与昂贵环境 reset。主 owner Ch62，Ch77 handoff；现有章节
  已拥有 artifact+environment+trace 证据链，`No Change — Already Covered / Experimental Case`。

### Predictive Validity for Agent Evaluation — 24/30

- **Source / Coverage**：已读 arXiv:2606.19704 的 twelve-tier measurement space、七项 benchmark/deployment
  synthesis、十四项 industrial implementations、proposed predictive-validity experiment、limitations 与 appendices。
- **Evidence Boundary**：核心主张是 deployment decision 应关注 benchmark ranking 能否预测 out-of-sample ranking，
  而不只是 in-sample mean。但作者明确没有执行该大规模验证，证据只来自 asset-operations domain 的 cross-study
  synthesis；因此它是 position/hypothesis，不是实证结论。
- **Trade-off / ROADMAP / Decision**：predictive validity 可暴露 benchmark overfit，却需要多个真实 deployment
  distributions、时间切片和足够样本，成本高且可能泄漏线上数据。Ch62 已覆盖 external validity、ranking drift 和
  online feedback，故 `No Change — Already Covered / Position Paper`。

### OPD-Evolver — 25/30

- **Source / Coverage**：已读 arXiv:2606.17628 的 experience lifecycle、fast/slow policies、on-policy
  distillation、selection/action/write/maintenance heads、MiniHack/InterCode evaluation、ablations 与 conclusion；没有
  独立 Limitations section。
- **Mechanism / Ownership**：fast policy 执行并产生 trajectories，slow evolver 分别学习选择 experience、基于
  experience 行动、写新 experience 与维护 repository；logged outcome 估计 memory value，同一 policy 的 on-policy
  samples降低 teacher/student mismatch。repository truth、retriever decision、behavior policy 与 slow update revision
  必须分离。
- **Evidence Boundary / Trade-off**：有限 game/shell/SQL tasks 支持联合 lifecycle training，不证明长期 repo 不会
  污染，也不能将官方 task score 归因于某一 head。统一 evolver 减少手写 heuristic，却增加 delayed attribution、
  policy-memory feedback loop 与 destructive maintenance。主 owner Ch73，Ch29/80 handoff；provisional
  `Refine — Existing Argument / Experimental`。

### Persistent-State World-Model Evaluation / WRBench — 25/30

- **Source / Coverage**：已读 arXiv:2606.20545 的 persistence definition、occlusion/re-observation interventions、
  model-family matrix、camera/subject controls、metric validation、system cards、limitations 与 extensive appendices。
- **Mechanism / Evidence Boundary**：普通 video metrics 只测可见 pixels；WRBench 隐藏对象、改变 camera 或让对象
  离开/返回，分别测 endpoint support 与 re-observed state consistency。跨版本/规模结果显示 visible quality 提升
  不必提高 hidden-state persistence；但这是 evaluation evidence，不证明模型内部不存在 latent state，也不能将
  synthetic interventions 等同真实物理因果。
- **Trade-off / ROADMAP / Decision**：干预式 benchmark 分离观察质量与持久状态，代价是场景控制、metric
  coverage 和生成器偏差。主 owner Ch62，Ch10 handoff；provisional `Refine — Existing Argument /
  Experimental Evaluation`。

### MemSlides — 24/30

- **Source / Coverage**：已读 arXiv:2606.17162 的 profile/working/tool memory、multi-turn localized revision、
  profile bank、matched-pair evaluation、blind judging、compute summary、limitations 与 appendices。
- **Mechanism / Ownership**：profile memory 保存长期 persona/style，working memory 保存当前 job preference/state，
  tool memory 保存局部操作链与验证经验；job end 后只有可迁移 execution experience 被 consolidate。三者 retention、
  consent、delete 与 conflict semantics 不应合并。
- **Evidence Boundary / Trade-off**：controlled personas 与 diagnostic edits 支持分层 memory 的特定价值，不是
  真实用户 deployment；作者明确缺少更广 human study、consent/deletion/sensitive-preference safeguards。分层提高
  localized revision，却新增 preference staleness、cross-job contamination 与 privacy。主 owner Ch73，Ch77/80
  handoff；provisional `Refine — Existing Argument / Experimental`。

### PlanBench-XL — 25/30

- **Source / Coverage**：已读 arXiv:2606.22388 的 large tool ecosystem generation、retriever、blocked path
  variants、minimal-path control、model/harness evaluation、robustness、case studies、limitations 与 appendices。
- **Mechanism / Evidence Boundary**：benchmark 隐藏、显式阻断或用语义干扰破坏部分 tool paths，要求 Agent 从
  大工具集合检索并规划剩余可行路径；更长 exploration 并不自动修复 blocker。证据支持“retrieval success ≠
  feasible plan ≠ execution success”的分层，不证明真实 API schema drift、side effects 或任意 tool graph。
- **Trade-off / ROADMAP / Decision**：controlled blockers 提高诊断力，却依赖 synthetic graph/retriever 和已知
  solution paths。Ch62 已有 failure-stage evaluation，Ch75 已有 planning/backtracking；`No Change — Already
  Covered / Experimental Case`，主证据 owner Ch62。

### OpenRath — 27/30

- **Source / Coverage**：已读 arXiv:2606.19409 的 typed Session programming model、runtime architecture、
  branch/merge/persist/replay、multi-Agent multi-session、release evidence protocol、limitations 与 case packets。
- **Mechanism / Evidence Boundary**：messages、tool calls/errors、workspace effects、memory interactions、usage、
  branch lineage 与 evidence 被放进同一个可传递 Session value；它可 place、transform、branch、merge、persist、
  release。作者有 audit packets 与 focused tests，但明确不声称 benchmark superiority 或 human preference；这是
  reference architecture/implementation evidence，不是性能证明。
- **Trade-off / Previous Design**：typed session 提高 lineage/replay，却增加 schema evolution、large-state
  serialization、merge conflict、sandbox lifetime 与 privacy retention。轻量 prompt loop 在短、无分支任务仍合理。
  主 owner Ch80，Ch71/77/78 handoff；provisional `Refine — Existing Argument / Reference Architecture`。

### EvoEmbedding — 25/30

- **Source / Coverage**：已读 arXiv:2606.21649 v1 的 latent memory queue、joint representation generation、
  EvoTrain-180K、10 retrieval/memory benchmarks、ablations、efficiency、limitations 与 appendices。
- **Mechanism / Ownership**：每次输入与 bounded latent memory 共同生成 retrieval vector 和新 latent tokens；FIFO
  queue 只保留最近 `L` steps，使旧 memory 至多被 loop-encoded `L` 次。embedding identity 因历史 state 而变化，
  index 必须保存 encoder/memory revision，不能把 vector 当 timeless fact。
- **Evidence Boundary / Trade-off**：结果支持作者 long-doc/conversation benchmarks 的 evolving representation，
  不证明在线 corpus mutation、跨租户 isolation 或 long-term factual supersession。context-aware embedding提高历史
  敏感度，却破坏静态 cache/index stability并新增 order dependence。主 owner Ch72，Ch73/55 handoff；provisional
  `Refine — Existing Argument / Experimental`。

### GateMem — 27/30

- **Source / Coverage**：已读 arXiv:2606.18829 的 multi-principal episodes、hidden checkpoints、ACL/forgetting
  categories、utility/leak metrics、four-stage quality control、baselines、judge-human agreement 与 appendices；没有
  独立 Limitations section。
- **Mechanism / Evidence Boundary**：memory evaluation 同时检查对授权 requester 有用、对未授权 principal 不泄漏、
  删除后不被恢复。dataset 验证 evidence chain、delete chain closure 与 leak-target；同一 checkpoint/order/backbone
  比较 full history、naive/policy RAG 和 external memory。证据支持现有 memory systems 在 shared deployment 中的
  governance gap，不证明自动 judge 覆盖隐式泄漏或现实法律删除义务。
- **Trade-off / ROADMAP / Decision**：ACL-aware retrieval可能牺牲 recall，active forgetting 与 audit/recovery 又有
  张力；这是 utility-only memory benchmark 的 `Direct Evolution`。主 owner Ch68，Ch73 handoff；provisional
  `Integrate — New Mechanism / Experimental Evaluation`。

### MobileForge — 24/30

- **Source / Coverage**：已读 arXiv:2606.19930 的 real-app task generation、multi-attempt rollout、corrective
  hints、step extraction、HiFPO/GRPO、AndroidWorld/MobileWorld evaluation、all numerical ablations、limitations 与
  appendix prompts。
- **Mechanism / Ownership**：Agent 与真实 app 交互生成任务/trajectory，evaluator 产生 outcome 和局部 corrective
  hints；HiFPO 在 prior-attempt hints 条件下对 feedback-selected local decisions 做 group-relative update。app state、
  hint provenance、behavior-policy revision 与 step reward 必须绑定，否则跨 attempt credit 错位。
- **Evidence Boundary / Trade-off**：matched 200-task ablation 支持 hints 不只是额外 sampling，但范围限 AndroidWorld
  apps、短 workflow；persistent user state、多 app 和 unusual rules 未覆盖。无人工 annotation 降低成本，却把
  evaluator/hint bias 带入 policy。主 owner Ch29，Ch74/76 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Deep Research in Physical Sciences — 24/30

- **Source / Coverage**：已读 arXiv:2606.18648 v1 的 200-question PhySciBench、three cognitive stages、
  expert rubrics、DelveAgent planning/memory/reflection、three additional benchmarks、cost、failure analysis、
  ablations 与 limitations。
- **Mechanism / Evidence Boundary**：framework 根据 execution state replans，用 dual-granularity memory 复用
  domain experience，以 physics-grounded reflection 检查 evidence/formula/code/output constraints。作者报告相对
  baselines 的有限提升和组件 ablation，但 200 questions、LLM-as-judge/expert rubric 与单一实现不证明 autonomous
  science，也不能将 cost ratio跨 provider revision 外推。
- **Trade-off / ROADMAP / Decision**：领域 verifier 提高 scientific validity，却增加 specialist prompt/rubric、
  tool timeout 与 shared error；多 Agent 只有任务可分解时值得通信成本。Ch62/78 已覆盖 capability/harness/
  verifier 与 coordination tax，故 `No Change — Already Covered / Domain Case`；Ch77 handoff。

### vLLM v0.23.0 — 29/30

- **Candidate / Week / Source Family / History**：`VLLM-0.23-RUNTIME-STATE-EVOLUTION`；W25；official
  signed release v0.23.0 page显示 2026-06-15，tag `0fc695f`。它承接 W22 v0.22.0、W23 v0.22.1，
  但按独立 major/minor release event 计一次。
- **Direct / Related Primary Sources**：vLLM official full release notes与全部 linked PR ledger；本轮以 release
  作为 version-fact authority，并按 mechanism families联读 PR intent。没有把 repository landing page 的
  badge日期、第三方 digest或 benchmark headline当 event/proof。
- **Access / Full-read Coverage**：已读 408-commit release 的 Highlights、Model Support、Engine Core、
  Large Scale Serving、Hardware/Performance、Quantization、API/Frontend、Security、Dependencies、Deprecations。
  深入聚合 Model Runner V2、speculative/prefix fixes、pluggable KVCacheSpec、multi-tier offload、KV connector/
  PP handshake、async EPLB、Rust frontend、unified parser、trace replay benchmark与 input/config hardening；未逐一
  读取所有 408 个 diff，未审计项只保留 version fact。
- **Original Problem / Previous Design / Changed Constraint**：单一 model runner、HBM KV、统一 frontend与
  少量 backend对早期 homogeneous serving合理；hybrid/Mamba、sliding-window、multimodal、speculative、PD、
  tiered KV、DP/PP、multiple frontends与 heterogeneous hardware使“一个 cache/runner/parser config”不能表达真实
  state。约束从单 engine correctness变成多个 typed state owners在同一 request lifecycle协作。
- **Mechanism / State Ownership / Control and Data Flow**：`KVCacheSpec`/manager拥有 layout/block semantics；
  per-request `on_new_request` policy与 `on_schedule_end` hook决定 offload lifecycle，object-store/CPU/HBM各自是
  physical tier而非 truth owner；connector handshake聚合 PP ranks与 intermediate outputs，scheduler将 transfer
  tokens从 local iteration accounting分离。speculative drafter拥有 proposal/lookahead，target/prefix cache拥有
  accepted state；frontend/parser统一 semantic interface，同时 request-id、tool/reasoning parser与 validation拥有
  protocol identity。DP supervisor TLS和untrusted token/UTF-8/config checks在GPU前形成 trust boundary。
- **Implementation Details**：MRv2默认扩至 Llama/Mistral，并加入 breakable CUDA graphs、PP bubble handling、
  hybrid block-size support；multi-tier KV加入 object-store、HMA、token-offset selective offload、page alignment与
  small CPU→GPU fast path；connector加入 PP-aware handshake、async-load deadlock fix、Mamba prefix mode、role
  deprecation与 shutdown/nonblocking lookup；async EPLB成为默认并加入 zero-copy transfer。每项是 release-scoped
  behavior，不外推为未来 API guarantee。
- **Evaluation Contract**：release列出许多作者/贡献者 microbench百分比与 fixes，但没有统一 model、hardware、
  precision、length、batch、concurrency、traffic、TTFT/TPOT/goodput、power或SLO contract。`vllm bench serve`
  新增 timed Moonshot/Alibaba trace replay只是 benchmark surface；没有随 release提供可统一解释的完整结果。
  因此本 review不引用任何 performance headline。
- **What the Evidence Proves / Does Not Prove**：证明现代 serving runtime 的优化单元已扩展为 model runner、
  scheduler/cache spec、tier policy、connector protocol、frontend parser与 security gate的联合 revision；不证明
  任意组合已 production-safe，不证明 object-store offload总是更快，也不证明 MRv2、Rust frontend、async EPLB
  或新 connector在所有 workload优于旧路径。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：typed/pluggable state提高 extensibility，
  也新增 compatibility matrix、hook ordering、stale tier、page/layout mismatch、PP handshake partial failure、
  async deadlock、parser drift与 deprecation migration。HBM-only、Python frontend、MRv1、同步 EPLB或无 connector
  的旧路径在小规模/稳定 workload仍更简单；fail-fast validation与 feature gating比强行启用新路径更重要。
- **Evolution Relationship**：`single runner/HBM cache → token-budget scheduler + typed KV spec → multi-tier
  request policy → PP-aware connector/PD → protocol-unified multi-frontend + hardened trust boundary` 是
  `Direct Evolution + Layering / Dependency`。它不替代 Ch41 KV identity、Ch44 acceptance或Ch51 PD ownership。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch41、Ch44、Ch46、Ch51、Ch53、Ch58、Ch68。Ch46已有
  scheduler/runtime decomposition与object-store offload演进；新增长期缺口是把 cache spec、policy hook、connector
  handshake、scheduler accounting、frontend/parser与security gate明确为同一 request revision contract。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Version-sensitive`，
  主 owner Ch46；Historical Books Gate关闭，不修改Books。待 code-level核验 selected PRs、cross-feature matrix、
  failover/rollback、tier consistency、PP partial failure、parser conformance、TLS identity、trace-replay artifact与
  complete workload/SLO evidence。

### NVIDIA sync-free MoE fused kernels — 27/30

- **Candidate / Week / Source Family / History**：`NVIDIA-CUTE-MOE-FUSION-SM100`；W25；NVIDIA Technical
  Blog 首发 2026-06-15。它是 grouped expert execution 的实现演进，不是新 MoE architecture；与 MLPerf
  Training v6.0 同周出现，但分别作为 mechanism evidence 与 benchmark evidence 计数。
- **Direct / Related Primary Sources / Coverage**：已读 NVIDIA 技术文档的 problem profile、三类 fused
  kernels、weight layout、forward/backward dataflow、MXFP8/NVFP4、dynamic scheduling、cluster margin、
  micro/end-to-end evaluation、software-stack integration 与 future work；联读 cuDNN Frontend MoE grouped
  matmul、grouped GEMM+dGLU/Wgrad API 和 support matrix。API 标注 experimental 的部分不写成稳定 contract。
- **Original Problem / Previous Design / Changed Constraint**：逐 expert/grouped GEMM 加独立 activation、
  transpose 与 quantize kernels 易理解、便于替换，在 dense 或不需 aggressive overlap 的 workload 合理；
  dropless routed MoE 使每个 expert 的 `M_e` 运行时变化，中间 BF16 tensor 往返 HBM、CPU token-count
  synchronization 与过满 SM occupancy 会暴露在 critical path，并阻碍 full-iteration graph capture 与 EP/DP
  communication overlap。
- **Mechanism / State Ownership / Control and Data Flow**：router/dispatch 仍拥有 token→expert identity；
  `first_token_offset`、token index/ks 与 top-k 描述 grouped layout；kernel 通过预先 repack 的 input/gate weight
  layout让同一 thread block 在 GEMM epilogue 完成 SwiGLU/GeGLU/sReLU、clamp/scale/bias，并在低精度路径直接
  生成 quantized/transposed output 或 amax。dynamic scheduler 与 configurable cluster margin限制占用 SM，
  为通信及其他 kernels保留并发资源；cuDNN Frontend wrapper拥有首次 compile 与 subsequent object cache。
- **Implementation Details**：公开 family 包含 `GroupedGemm + Quantize`、`GroupedGemm + Activation +
  Quantize/Transpose`、`GroupedGemm + dActivation + Quantize/Transpose`；backward epilogue读取 GEMM output 和
  forward `C`/interleaved gate layout计算 dGLU。cuDNN 文档将 gather/scatter/none routing mode、tensor shape、
  datatype与 minimum version独立列出，说明 fusion 必须在 layout/support matrix内选择，不能只按名称启用。
- **Evaluation Contract**：作者披露 GB200 上相对 Transformer Engine optimized unfused baseline 的 up to
  1.3x forward / 2.1x backward microkernel speedup，以及内部 DeepSeek-V3 up to 8%、GPT-OSS pretraining
  up to 93% end-to-end uplift。公开材料未给出统一 model revision、token/expert distribution、sequence、global
  batch、parallel degrees、optimizer、precision recipe细节、network topology、convergence、run variance、power
  或 SLO；故数字仅记录为 vendor bounded claim，不用于跨系统比较。
- **What the Evidence Proves / Does Not Prove**：证明 MoE kernel optimization 要联合处理 memory traffic、
  host synchronization、layout 与 communication headroom，且 kernel fusion收益可能来自 graphability/overlap，
  不只是 launch count；不证明所有 MoE、GPU、expert shape或框架都获益，也不证明 93% 来自单一 fusion。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：收益交换 weight repack、specialized layout、
  dtype/support matrix、JIT/AOT compile cache、heuristic selection、SM-margin tuning与更大的 correctness matrix；
  fusion可能因小 `M_e`、极端 imbalance、unsupported activation/precision、compile cold start或抢占通信资源而失效。
  unfused/composable path在 portability、debug、rare shape、非 SM100或需要独立数值验证时仍合理。
- **Evolution / ROADMAP / Chapters / Decision**：`Direct Evolution + Layering / Dependency`：
  `per-expert ops → grouped GEMM → epilogue fusion → sync-free graphable execution → resource-aware compute/
  communication overlap`。已读 Ch21、Ch36、Ch45及相邻 training/runtime论点；主 owner Ch21，Ch36/45短接。
  provisional `Refine — Existing Argument / Bounded Case`；Historical Books Gate关闭，不改 Books。

### MLPerf Training v6.0 — 26/30

- **Candidate / Week / Source Family / History**：`MLCOMMONS-TRAINING-6.0-MOE-CONTRACT`；W25；MLCommons
  2026-06-16 official results event。NVIDIA 结果说明是 submitter evidence，不是 suite owner；supplemental
  discussion 本身明确各组织文字不代表 MLCommons 观点。
- **Direct / Related Primary Sources / Coverage**：已读 MLCommons release、Training v6.0 reference suite、
  training rules、public results repository/entry surface、25 页 supplemental discussion，并联读 NVIDIA
  submission mechanism narrative。覆盖 workload/model/dataset、Closed/Open division、target quality、run count、
  result aggregation、evaluation cadence、system/framework definition、submission diversity与 v6.0 exception。
- **Original Problem / Previous Design / Changed Constraint**：旧 Llama dense pretraining、LoRA、FLUX 与 DLRM
  workloads仍适合比较对应系统；但现代训练的 sparse routing、expert imbalance、All-to-All 与小/大规模 MoE
  已成为独立压力，dense benchmark 无法代理。变化不是“旧 benchmark 错了”，而是 workload population扩大。
- **Mechanism / State Ownership / Control and Data Flow**：MLCommons/rules拥有 benchmark identity、reference
  implementation、dataset、quality target、allowed hyperparameters、division与 aggregation；submitter拥有系统、
  framework、optimization与 run artifacts；review/verifier判断合规。clock在系统首次构造/执行模型或接触数据前
  启动，达到 target quality后停止；benchmark result由多次 independent runs 去除 fastest/slowest 后取均值，
  再按 reference result normalization，不能只挑最快一次。
- **Implementation / Workload Contract**：v6.0 新增 DeepSeek-V3 671B-total/37B-active 与 GPT-OSS-20B
  21B-total/3.6B-active；reference implementation分别使用 NeMo/C4 与 Primus/C4，submitters 可在规则内用其他
  framework。large MoE最少 3 runs，small MoE最少 10 runs；GPT-OSS v6.0 对 `opt_end_learning_rate` 有一次性
  compatibility exception，提醒 benchmark contract也有 versioned implementation debt。
- **Evaluation Contract / Vendor Case**：NVIDIA列出的 GB300/GB200 entry、GPU count与 time-to-train只属于
  指定 submission。其 full-iteration CUDA graph、MoE fusion、router/EP、hybrid parallelism、network routing/
  congestion-control narrative解释可能的 system co-design，但没有把每项改动做独立 causal ablation。不得将
  per-accelerator normalization与不同 scale/division配置混成跨平台普遍排名。
- **What the Evidence Proves / Does Not Prove**：证明标准训练 benchmark的 evaluation subject 是
  `model + dataset + quality target + system/framework versions + division + repeated runs`，并正式扩大到两类
  MoE；不证明 benchmark覆盖真实生产训练的可靠性、故障恢复、checkpoint cost、power/energy、所有 topology、
  hyperparameter探索成本或 model quality beyond target。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：固定规则提高可比性，却鼓励 benchmark-
  specific optimization，并可能隐藏 initialization、recovery、data pipeline、long-horizon quality与运营成本；
  Open/Closed division、不同规模与不同 workload仍不能直接合并。旧 dense/LoRA/vision/recommendation workloads
  在各自 intended use仍成立，新 MoE workload是补层而非替代。
- **Evolution / ROADMAP / Chapters / Decision**：`Layering / Dependency`：
  `single-op microbench → model-to-target training run → full-system repeated benchmark → versioned sparse-
  workload suite`。已读 Ch24、Ch32、Ch62及相邻 evaluation/monitoring边界；主 owner Ch62，Ch24/32短接。
  provisional `Refine — Existing Argument / Benchmark Contract`；Historical Books Gate关闭，不改 Books。

## Final Books Integration Ledger

| # | Candidate | Final disposition | Stable owner / chapter evidence |
| ---: | --- | --- | --- |
| 1 | Near-autonomous AI chemist | No Change — Already Covered | `AGENT-WORKFLOW` Ch81 已有 proposal→approval→physical effect→replication |
| 2 | LifeSciBench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 executable domain-artifact contract |
| 3 | Agentic coding and expertise | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已分离 model/harness/user/workload evidence |
| 4 | Project Fetch phase two | Weekly Only — Domain Experiment Fact | 三次受控 trial；不形成通用 robotics autonomy 机制 |
| 5 | Looped World Models | Refine — Existing Argument | `MULTIMODAL-WORLD-MODELS` Ch25；recurrent transition 与 adaptive depth |
| 6 | LoopCoder-v2 | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；shared first-loop KV 与 local loop state |
| 7 | On-policy Self-distillation for dLLMs | Refine — Existing Argument | `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 / training handoff；same-policy future conditioning |
| 8 | Zone of Proximal Policy Optimization | Refine — Existing Argument | `TRAIN-GRPO` Ch33；prompt-side scaffold 与 on-policy action ownership |
| 9 | GameCraft-Bench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 persistent environment/state evidence |
| 10 | Predictive Validity for Agent Evaluation | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 benchmark→deployment validity boundary |
| 11 | OPD-Evolver | Refine — Existing Argument | `AGENT-MEMORY` Ch77；experience distillation 与 supersession evidence |
| 12 | LLM-Designed Training Environment | Unverified / Blocked | 无可验证正文；不分配 Books mechanism owner |
| 13 | EfficientRollout | Refine — Existing Argument | `INFER-SPECULATIVE-DECODING` Ch48；training-step-aware self-drafter toggle |
| 14 | Persistent-State World-Model Evaluation | Refine — Existing Argument | `MULTIMODAL-WORLD-MODELS` Ch25 / Ch66 handoff；persistent transition evidence |
| 15 | SAE Post-Intervention Recovery | Refine — Existing Argument | `MODEL-INTERPRETABILITY` Ch5；intervention 后恢复轨迹不等于 causal feature |
| 16 | Variable-Width Transformers | Refine — Existing Argument | `MODEL-ARCHITECTURE` Ch17；input-conditioned width 与 execution identity |
| 17 | Context-Aware RL | Refine — Existing Argument | `TRAIN-GRPO` Ch33；Context revision 与 behavior-policy identity |
| 18 | TokenPilot | Refine — Existing Argument | `AGENT-CONTEXT` Ch75；canonical prefix、artifact recovery、delayed eviction |
| 19 | MemSlides | Refine — Existing Argument | `AGENT-MEMORY` Ch77；bounded presentation/state consolidation |
| 20 | PlanBench-XL | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已分离 retrieval/plan/execution failure |
| 21 | Grouped Query Experts | Refine — Existing Argument | `MODEL-MOE` Ch21；query experts without KV duplication |
| 22 | OpenRath | Refine — Existing Argument | `AGENT-PLATFORM` Ch84；typed Session branch/merge/persist/replay |
| 23 | JetFlow | Refine — Existing Argument | `INFER-SPECULATIVE-DECODING` Ch48；parallel tree proposal 与 path commit |
| 24 | EvoEmbedding | Refine — Existing Argument | `AGENT-RAG` Ch76；history-conditioned embedding/index identity |
| 25 | GateMem | Refine — Existing Argument | `PLATFORM-SECURITY` Ch72；Memory utility/ACL/forgetting Gate |
| 26 | PerceptionDLM | Emerging / Experimental | `MODEL-ARCHITECTURE` Ch17 handoff；单-region质量与 serving contract 未闭合 |
| 27 | MobileForge | Refine — Existing Argument | `TRAIN-GRPO` Ch33；attempt/hint/policy identity |
| 28 | MemGUI-Agent | Unverified / Blocked | 无可验证正文；不分配 Books mechanism owner |
| 29 | Confident Layer Decoding | Refine — Existing Argument | `MODEL-OUTPUT-LAYER` Ch20；intermediate-logit intervention boundary |
| 30 | Discretizing Reward Models | Refine — Existing Argument | `TRAIN-RLHF` Ch31；uncertainty-aware ordinal reward boundary |
| 31 | Micro-Reflective Self-Distillation | Refine — Existing Argument | `TRAIN-SFT` Ch29；self-generated correction 与 evidence boundary |
| 32 | Deep Research in Physical Sciences | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 domain verifier 与 coordination tax |
| 33 | vLLM v0.23.0 | Refine — Existing Argument / Version-sensitive | `INFER-VLLM` Ch50；typed request-state revision contract |
| 34 | NVIDIA sync-free MoE fused kernels | Refine — Existing Argument / Bounded Case | `MODEL-MOE` Ch21；fusion、host-sync removal、communication headroom |
| 35 | MLPerf Training v6.0 | Refine — Existing Argument / Benchmark Contract | `PLATFORM-EVALUATION-SYSTEM` Ch66；convergence/division/run aggregation |

逐行复算结果：35/35 final；24 Refine、7 No Change、1 Weekly Only、1 Emerging、2 Unverified / Blocked。
两个 blocked family 没有机制 owner；所有 `No Change` 均引用已读章节中的具体论点。

## Blocked Primary-Source Backlog

2026-08-13 精确 identity 重试恢复了原 27 项中的 25 篇 HTML 正文，现均已完成 method、evaluation、
limitations、关键 Appendix 与相邻章节审计。只有 LLM-Designed Training Environment 与 MemGUI-Agent 继续
blocked。

| Candidate | First-public Date | Blocked Primary Source | Claims explicitly not verified |
| --- | --- | --- | --- |
| LLM-Designed Training Environment | 2026-06-16 | arXiv:2606.17682 | environment revision、failure evidence、policy/environment coupling and testbed validity |
| MemGUI-Agent | 2026-06-18 | arXiv:2606.19926 | proactive Context management、long-horizon GUI state |

这两项仍不计 Full Source Review、不分配 Books owner、不修改 Books，也不从标题或摘要推断机制。普通 pending
已清零，因此 post-forward cursor 进入 W26；W25 discovery/Historical Evidence Gates 仍保持 Open。

## Repository Changes

- W25 从 4 个 baseline families 扩展为 35 个 scored families；完成 TokenPilot 全文、Appendix、artifact
  与 Ch70～73/Ch66/cache 邻接审计；2026-08-13 重试恢复并完成 25 项 Full Source Review，仅 2 项保留
  `Unverified / Blocked Backlog`，普通 pending 清零，post-forward cursor 进入 W26。14 个 W22～W24 spillbacks 已按 v1
  回拨；fixed-source scan 新增并完成 vLLM v0.23.0、NVIDIA MoE fusion 与 MLPerf Training v6.0 review，
  provisional owners分别为 Ch46、Ch21、Ch62。remaining fixed release surfaces未发现可可靠归周的独立 material
  event，fixed checkpoint 通过并推进 W26。Books Integration 完成 35/35 dispositions；World Model 两项既有
  Source-Family integration 保留，本轮 refine `AGENT-CONTEXT`、`INFER-VLLM`、`MODEL-MOE`、
  `PLATFORM-EVALUATION-SYSTEM`、`PLATFORM-SECURITY` 与 `AGENT-PLATFORM`。两项 blocked 未进入正文。

## Open Questions

1. 外部实验的 partial failure、rollback 与 artifact lineage 应怎样进入 Agent evaluation？
2. 同周还有哪些 physical/executable Agent evaluation 或 workflow runtime 研究可作为独立复核？
3. TokenPilot 的 provider-token cost 能否在公开 self-hosted serving 上重建 TTFT/TPOT、GPU memory、
   concurrency、cache eviction 与 goodput contract？
4. 两项 blocked source 恢复后是否会改变当前 architecture/training/runtime 演进链与章节 owner 判断？
5. vLLM v0.23.0 中 multi-tier KV、PP connector、speculative/prefix、MRv2 与 frontend/parser 的 selected PR
   能否完成 code-level cross-feature/failure matrix 核验？
6. NVIDIA fused kernels 的 compile/heuristic、expert-shape sensitivity、communication overlap 与 end-to-end
   causal contribution能否用公开 artifact重建？
7. MLPerf Training v6.0 public submissions能否进一步抽取 checkpoint/recovery、power与 fabric failure contract，
   而不越过 division/scale/workload可比性边界？
8. OpenRath typed Session、GateMem multi-principal Memory 与 TokenPilot lifecycle 能否在同一长期 Agent runtime
   中形成不冲突的 branch、ACL、delete、replay 与 cache identity？

## Sources

- OpenAI Research publication index, entries dated 2026-06-17:
  https://openai.com/research/index/publication/
- Anthropic Research index, entries dated 2026-06-16 and 2026-06-18:
  https://www.anthropic.com/research
- Hugging Face Papers, 2026-W25 discovery index: https://huggingface.co/papers/week/2026-W25
- TokenPilot metadata: https://arxiv.org/abs/2606.17016
- TokenPilot HTML: https://arxiv.org/html/2606.17016
- TokenPilot / LightMem2 artifact: https://github.com/zjunlp/LightMem2
- vLLM v0.23.0 release, published 2026-06-15:
  https://github.com/vllm-project/vllm/releases/tag/v0.23.0
- NVIDIA, "Boosting MoE Training Throughput with Advanced Fusion Kernels," published 2026-06-15:
  https://developer.nvidia.com/blog/boosting-moe-training-throughput-with-advanced-fusion-kernels/
- NVIDIA cuDNN Frontend, MoE Grouped Matmul:
  https://docs.nvidia.com/deeplearning/cudnn/frontend/latest/operations/MoeGroupedMatmul.html
- NVIDIA cuDNN Frontend, Grouped GEMM + dGLU:
  https://docs.nvidia.com/deeplearning/cudnn/frontend/latest/fe-oss-apis/gemm_fusions/grouped_gemm_dglu.html
- MLCommons, MLPerf Training v6.0 results, published 2026-06-16:
  https://mlcommons.org/2026/06/mlperf-training-v6-0-results/
- MLCommons Training reference implementations and v6.0 workload table:
  https://github.com/mlcommons/training
- MLCommons Training rules:
  https://github.com/mlcommons/training_policies/blob/master/training_rules.adoc
- MLCommons Training v6.0 public results:
  https://github.com/mlcommons/training_results_v6.0
- MLCommons Training v6.0 supplemental discussion:
  https://mlcommons.org/wp-content/uploads/2026/06/Final-MLPerf-Training-v6.0-Supplemental-Discussion-UNDER-EMBARGO-UNTIL-6_16_26-8_00-AM-PT.pdf
- NVIDIA MLPerf Training v6.0 submission analysis, published 2026-06-16:
  https://developer.nvidia.com/blog/nvidia-blackwell-tops-mlperf-training-6-0-with-industry-leading-scale-and-performance/
- Looped World Models: https://arxiv.org/abs/2606.18208
- LoopCoder-v2: https://arxiv.org/abs/2606.18023
- On-policy Self-distillation for dLLMs: https://arxiv.org/abs/2606.18195
- Zone of Proximal Policy Optimization: https://arxiv.org/abs/2606.18216
- GameCraft-Bench: https://arxiv.org/abs/2606.17861
- Predictive Validity for Agent Evaluation: https://arxiv.org/abs/2606.19704
- OPD-Evolver: https://arxiv.org/abs/2606.17628
- LLM-Designed Training Environment: https://arxiv.org/abs/2606.17682
- EfficientRollout: https://arxiv.org/abs/2606.18967
- Persistent-State World-Model Evaluation: https://arxiv.org/abs/2606.20545
- SAE Post-Intervention Recovery: https://arxiv.org/abs/2606.18322
- Variable-Width Transformers: https://arxiv.org/abs/2606.18246
- Context-Aware RL: https://arxiv.org/abs/2606.17053
- MemSlides: https://arxiv.org/abs/2606.17162
- PlanBench-XL: https://arxiv.org/abs/2606.22388
- Grouped Query Experts: https://arxiv.org/abs/2606.20945
- OpenRath: https://arxiv.org/abs/2606.19409
- JetFlow (previous ledger label: JetSpec): https://arxiv.org/abs/2606.18394
- EvoEmbedding: https://arxiv.org/abs/2606.21649
- GateMem: https://arxiv.org/abs/2606.18829
- PerceptionDLM: https://arxiv.org/abs/2606.19534
- MobileForge: https://arxiv.org/abs/2606.19930
- MemGUI-Agent: https://arxiv.org/abs/2606.19926
- Confident Layer Decoding: https://arxiv.org/abs/2606.21906
- Discretizing Reward Models: https://arxiv.org/abs/2606.21795
- Micro-Reflective Self-Distillation: https://arxiv.org/abs/2606.18844
- Deep Research in Physical Sciences: https://arxiv.org/abs/2606.18648

## 2026-08-13 Source-Family Books Integration

Looped World Models 与 Persistent-State World-Model Evaluation 已通过 Source-Family Books Gate，分别以 `MULTIMODAL-WORLD-MODELS` / Ch25 的 recurrent transition 与 persistent-state evidence contract 融入 `books/part-03-multimodal-world-models/25-multimodal-world-models.md`。它们不证明 video plausibility 等于 causal correctness，也不关闭 LLM-Designed Training Environment、MemGUI-Agent 等材料缺口；Archive Completion Gate 仍 Open。
