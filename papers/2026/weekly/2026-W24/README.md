# AI Research Weekly — 2026-W24

> Coverage Window: 2026-06-08～2026-06-14
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 38/38 final dispositions; 36/37 `20+` Full Source Reviews complete; 25 Refine, 9 No Change, 1 Weekly Only, 1 Emerging, 1 Withdrawn, 1 Unverified / Blocked; Source-Family Books Gate complete under blocked-skip; Archive/Discovery Gate open; Books cursor advances to W25

## Executive Summary

旧版 W24 只保留 Anthropic 同日两项研究，不能代表完整一周。重放 Hugging Face 的
“Jun 7～13”展示窗并以 arXiv v1 日期重归属后，本周首先恢复 21 个学术 Source Families，覆盖
trained sparse Attention、MoE routing、RL/distillation、context compression、speculative decoding、
Agent harness/environment、long-horizon evaluation 与 memory evolution。展示窗中另有 9 项属于
W22/W23，1 项 first-public 于 2025 年，均不以 curation date 重复计入 W24。随后重放 W25
展示窗又回收 10 个 v1 实际属于 W24 的 families；其中 FastContext 已撤稿，作为低分 provenance
record 保留，不能继续按原摘要视作可靠机制证据。

本检查点完成 MiniMax Sparse Attention 的 30 页论文、附录、作者代码与 Ch21～24、Ch39 邻接
审计。它补充的长期机制不是“稀疏 Attention 更快”，而是：selector 的训练目标、block/GQA
粒度、GPU loop order、hot-block load balancing 与迁移 schedule 必须共同成立，理论 FLOPs 才可能
转为 wall-clock 收益。论文的 H800 结果与当前开源仓库的 SM100 contract 也必须分开记录。

固定官方/Infra 重扫又恢复 KServe v0.19.0、AA-AgentPerf 与 NVIDIA FP8 checkpoint→ONNX→TensorRT
工程链。三者分别补足声明式 LLM control plane、Agent workflow serving workload contract 与低精度
artifact/compiler contract；都已联读直接官方材料。vLLM v0.23.0 的官方 release 页面实际显示 6 月 15 日，
归 W25 而不塞入 W24；Kubernetes v1.36.2 等普通 patch release 只进 noise boundary。

## Coverage and Source Coverage

- 模型与研究机构：保留 Anthropic 2026-06-08 两项官方研究；fixed source replay 新增 NVIDIA
  06-09 quantization deployment chain 与 06-12 AA-AgentPerf analysis，并与 benchmark owner methodology 联读。
- 论文与学术来源：完成 Hugging Face W24 首轮 recall、31 项 metadata/submission-history 检查和
  first-public 归周；首轮 21 项进入 W24，8 项回拨 W23、1 项回拨 W22、1 项归为 2025 cross-year
  node；W25 feed 又恢复 10 个 W24 spillbacks。
  MSA 已读 arXiv v2 全文、全部附录与作者公开 kernel repository；Scholar/OpenAlex/DBLP 交叉召回待做。
- AI Infra：MSA repository 已检查 public API、hardware/precision/layout、test/benchmark surface；
  其当前 SM100 实现不能倒写成论文 2026-06-11 的 H800 evaluation contract。其他 release/RFC/PR
  fixed list 已重扫，新增 KServe v0.19.0；vLLM v0.23.0 按官方日期归 W25。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Agents in biology | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Worth Watching |
| LLM impact on N-day exploits | 3 | 5 | 4 | 4 | 5 | 4 | 25/30 | Must Read |
| MiniMax Sparse Attention | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete |
| EvoArena | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch73 / Experimental |
| Hypothesis-Tree Refinement | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch77 / Experimental |
| WeaveBench | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full review complete — No Change Ch62 / Experimental case |
| MaxProof | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Refine Ch29 / Experimental |
| Manifold Power Iteration for MoE routing | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch21 / Experimental |
| FORT-Searcher | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — provisional Refine Ch23 / Experimental |
| Claw-SWE-Bench | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — No Change Ch62 / Experimental case |
| Agentic Environment Engineering survey | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Unverified / Blocked Backlog — score provisional |
| FlashMemory-DeepSeek-V4 | 5 | 5 | 5 | 3 | 5 | 2 | 25/30 | Full review complete — provisional Refine Ch22 / Experimental |
| Z-Reward | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch27 / Experimental |
| SearchSwarm | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — No Change Ch78 / Experimental case |
| VIA-SD | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Full Source Review complete — provisional Refine Ch44 / Experimental |
| DeNovoSWE | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — provisional Refine Ch23 / Experimental |
| Rethinking Divergence Regularization in LLM RL | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Integrate Ch29 / Experimental |
| EurekAgent | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — No Change Ch77 / Experimental case |
| End-to-End Context Compression at Scale | 5 | 5 | 5 | 4 | 5 | 2 | 26/30 | Full review complete — provisional Refine Ch22 / Experimental |
| On Subquadratic Architectures | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch22 / Experimental |
| Workflow-GYM | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — provisional Refine Ch62 / Experimental |
| MTP with Rejection Sampling | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full review complete — provisional Refine Ch44 / Experimental |
| EEVEE test-time prompt learning | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — provisional Refine Ch76 / Experimental |
| Data Journalist Agent | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — No Change Ch62 / Experimental case |
| Chatbot-to-Digital-Colleague survey | 3 | 4 | 4 | 3 | 5 | 3 | 22/30 | Full review complete — No Change Ch80 / secondary synthesis |
| FastContext | 4 | 4 | 4 | 1 | 4 | 1 | 18/30 | Withdrawn — provenance record |
| Ling and Ring 2.6 Technical Report | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full review complete — Emerging / Version-sensitive Ch29 |
| APPO | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Integrate Ch29 / Experimental |
| HarnessX | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full review complete — provisional Refine Ch80 / Experimental |
| RedAct | 4 | 4 | 5 | 4 | 5 | 2 | 24/30 | Full review complete — provisional Refine Ch68 / Experimental |
| Rethinking Efficient Attention in Hybrid Architectures | 5 | 4 | 4 | 4 | 5 | 3 | 25/30 | Full review complete — provisional Refine Ch22 / Experimental |
| Visual Repository Representations for LLM Agents | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch71 / Experimental |
| Cross-Lingual BrowseComp-Plus | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full review complete — provisional Refine Ch72 / Experimental |
| DailyReport Search-Agent Benchmark | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full review complete — No Change Ch62 / Experimental case |
| Notes2Skills | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Full review complete — provisional Integrate Ch80 / Experimental |
| KServe v0.19.0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Must Read — full review complete; versioned control-plane evidence |
| AA-AgentPerf | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Must Read — full review complete; live benchmark contract |
| ModelOpt FP8 → ONNX Q/DQ → TensorRT engine | 3 | 4 | 5 | 5 | 4 | 3 | 24/30 | Worth Watching — full review complete; bounded engineering case |

当前账目为 38 行：26 个 `25～30`、11 个 `20～24`、1 个 `<20`。36 个 `20+` families 已完成
Full Source Review，1 个仍为 `Unverified / Blocked Backlog`。逐项 Books disposition 已完成：25 Refine、
9 No Change、1 Weekly Only、1 Emerging、1 Withdrawn、1 Unverified / Blocked。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Baseline score rows | 2 | 2/2 `20+` Full Source Reviews retained |
| Recovered in-window families | 33 | MSA、VIA-SD 与后续恢复项完成 36 个 `20+` Full Source Review；1 Unverified / Blocked Backlog；0 current-review pending；FastContext withdrawn |
| Fixed official / Infra families | 3 | KServe v0.19.0、AA-AgentPerf、FP8→ONNX→TensorRT chain 均完成 direct primary-source review |
| Recorded `20+` candidates | 37 | 26 high / 11 mid；六维合计已复算 |
| Earlier-week spillbacks | 9 | 8 项按 v1 回拨 W23；ResearchClawBench v1 05-28 回拨 W22 |
| Later-feed spillbacks recovered | 12 | W25/W26 display feed 中 v1 06-09～06-13 的 families 已归 W24 |
| Cross-year publication node | 1 | psychometric-questionnaire paper v1 2025-09；不计为 2026 新事件 |
| Academic discovery window | Open | HF first pass complete；cross indexes pending |
| Official / Infra fixed checkpoint | Passed | fixed source lists replayed；三项新增 family 完成 Full Source Review |
| W24 forward Candidate Gate | Passed with explicit blocked ledger | 36/37 `20+` Full Source Reviews；1/37 Unverified / Blocked Backlog；0 current-review pending；post-forward cursor advances to W25 |
| W24 discovery / Historical Evidence Gate | Open | Agentic Environment Engineering survey 与 academic cross-index 未闭合 |

## Deep Analysis 1 — Dual-Use 风险属于 Execution Context

同一模型的 reasoning/coding 能力在授权实验环境中产生科研价值，在真实漏洞目标上形成安全
风险。控制面必须同时判断 actor、target、permission、tool、network、artifact 与 repeated
behavior；仅做 prompt keyword filter 会丢失执行上下文。代价是更强的 identity、sandbox、
policy evaluation、trace 和 human review。

## Deep Analysis 2 — 稀疏 Attention 是 Model–Kernel Joint Contract

### Why → Principle → Mechanism

Dense softmax 仍是信息完整、实现成熟的基线，但长序列将 pair compute 推向 `T²`。仅减少理论
连接数并不够：token-level/random access 可能让 GPU 无法形成高效 MMA，selector 自身也可能成为
新瓶颈。MSA 将约束收敛为 GQA-group shared、block-level Top-k：轻量 Index Branch 先为每个 query
和 GQA group 选择 KV blocks，Main Branch 再对选中 tokens 做 exact softmax。非可微 Top-k 由
Main Branch distribution 的 KL signal 训练；stop-gradient 防止辅助目标改写 backbone，full-attention
warmup 避免随机 selector 过早控制数据流，local self block 作为最小稳定边界。

Kernel 不按 query 外循环重复读取零散 KV，而按 KV block 外循环，反向收集选择该 block 的 queries；
hot blocks 被预切成多个 CTA，partial softmax 经 HBM buffer 和第二阶段 combine 合并，query rows 又被
拼接以填满 Tensor Core MMA。这是 `Layering / Dependency`：architecture 产生 block/GQA sparsity，
execution path 才把它转成 contiguous reuse；两层任一失配，FLOPs reduction 都不会自动成为 SLO 收益。

### Trade-off → Connection → Evolution

```text
dense exact Attention
→ inference-time sparse discovery（无需重训，但 discovery/selection 有成本）
→ natively trained multi-branch sparse Attention（训练分布一致，但机制和 kernel 更重）
→ GQA-group block selector + dedicated execution mapping
→ dense checkpoint 经 warmup/continued pretraining 迁移
```

MSA 不是替代 NSA/DSA 的单向终点：它以更少分支和较粗 block 换 GPU regularity，也新增
selector miss、block granularity、warmup tokens、KL isolation、reverse-index workspace、hot-block
load imbalance 与专用 kernel portability。短 context、严格 exactness、没有匹配 kernel 或无法承担
continued training 时，dense FlashAttention 仍合理；固定 local/window pattern 在信息主要局部且预算
要求确定时仍合理。

## Evidence Level

Anthropic 两项材料只能证明披露 workflow 中的能力/风险边界。MSA 的机制与实验来自作者论文和
artifact：109B/6B-active、41-layer MoE、3T-token matched training 与 H800 结果支持该具体设计的
feasibility，不证明所有模型/硬件/流量都同等受益。论文没有独立 Limitations/Threats section；
online concurrency、batch、power、端到端 serving SLO、H800 数量与部分 kernel measurement details
未披露。当前 repository 主要声明 NVIDIA SM100、BF16/FP8/NVFP4/FP4 与 paged decode surface，
不能据此补齐历史 H800 benchmark contract。

原 31 个 blocked candidates 已在 2026-08-13 以精确 arXiv v1 identity 重试；30 篇 HTML 全文恢复并完成
方法、实验、ablation、限制、关键 Appendix 与章节邻接审计。VIA-SD 已恢复；只有 Agentic Environment
Engineering survey 仍无法取得可验证正文，继续保留 `Unverified / Blocked Backlog`，不计 Full Source
Review，也不从标题或摘要反推机制。
FastContext 的 arXiv record 已标记 withdrawn 且 PDF 不再提供，因此保留来源/日期/撤稿事实，不把摘要
主张升级为机制证据或 Books 候选。

KServe v0.19.0 release 证明 `LLMInferenceService` control plane 同时推进 observed applied config/routing/
workload references、LocalModel cache、static LoRA reconciliation、precise-prefix identity、migration、readiness、
termination 与 autoscaling status；它不证明每项功能跨 runtime/cluster 一致。AA-AgentPerf 的 benchmark-owner
methodology 与 NVIDIA 被测方材料共同证明 trajectory replay、dynamic prefixes、tool-delay simulation、per-request
P25 output speed/P95 TTFT、steady-state concurrency search 与 measured accelerator power contract；live leaderboard
仍受 private test set、vendor-tuned configuration、model/software revision 与 CPU/network/cooling excluded power
boundary 限制。NVIDIA quantization tutorial 证明特定 CLIP/ModelOpt/ONNX opset 20+/TensorRT 10.16/RTX 6000 Ada/
batch 128 path 的 Q/DQ fusion 与 profile，不证明任意 LLM、shape、GPU 或 production SLO。

## Cross-Week Deduplication

N-day exploit 与 W21 exploit-development measurement 是同一 program 的后续，只记录 patch-window
impact 边界。MSA 与 W10 FlashPrefill 是 `Layering / Dependency`：前者把 sparsity 写入模型训练与
kernel contract，后者在现有 model 上做 invocation-level discovery，不能合并为同一机制。
MSA 与 Ch22 已有 NSA/DSA 演进属于同一 native/adaptive sparse family，但 group/block granularity、
warmup、gradient ownership 和 KV-outer execution 提供了新的可审计分支。

Agents' Last Exam、SWE-Explore、unembedding lens、on-policy distillation、retrospective harness、
LatentSkill、OpenSkill 与 When Tools Fail 的 v1 均落在 W23；ResearchClawBench v1 落在 W22。
Human Psychometric Questionnaires v1 为 2025-09，只记录 cross-year curation node。
W25 feed 中的 Data Journalist Agent、Chatbot-to-Digital-Colleague、FastContext、Ling/Ring 2.6、
APPO、HarnessX、RedAct、Hybrid Attention、visual repository Agent 与 Cross-Lingual BrowseComp-Plus
均按 v1 06-09～06-13 回填 W24；FastContext 后续撤稿不删除历史事件，但改变 Evidence Level。

## Knowledge Tree Position

Ch14/15 Attention/GQA → Ch22 Long Context（主 owner）→ Ch23/24 sparse pretraining/continued training
→ Ch39 Prefill execution handoff → Ch45 kernel mapping。已恢复 families 的 provisional mapping 还涉及
Ch21、Ch27～30、Ch44、Ch62、Ch68 与 Ch71～80；两项 blocked 不分配 Books owner。
新增 fixed-source owner：KServe v0.19.0 → Ch57（Ch49/55/58 handoff）；AA-AgentPerf → Ch62/66；
FP8→ONNX→TensorRT → Ch45（Ch50/55 handoff）。

## Recommended Action

Agentic Environment Engineering survey 保留 blocked ledger；VIA-SD 已恢复全文并完成审计。MSA 最终
`Refine — Existing Argument`：Ch22 已有 NSA/DSA 的联合设计主线，真实新增点是 selector gradient ownership、GQA-group
block granularity、KV-outer execution 与 migration contract；Ch39 只需短 handoff，不能重复论文。
KServe v0.19.0 最终由 `PLATFORM-KSERVE`（Ch61；Legacy Ch57）`Refine`：新增稳定点是 desired spec、
observed applied config、routing/workload references 与 readiness/termination state 必须形成可审计闭环，但不能
复制 release feature list。AA-AgentPerf 由 `PLATFORM-EVALUATION-SYSTEM`（Ch66；Legacy Ch62）`Refine`：把单 request
length benchmark 演进为 workflow trajectory + tool think-time + SLO-constrained concurrency + power normalization，
同时保留 private dataset/vendor tuning/live revision。FP8 deployment chain 为 Ch45 `No Change — Already Covered /
Bounded Engineering Case`，现有章节已经拥有 precision→graph rewrite→kernel→hardware→quality contract。

## Event-Date Daily Decision

2026-06-08～06-11：Weekly only；2025 first-public 的 psychometric paper 不建立 2026 Daily。

## Books Integration Decision

`Source-Family Books Gate Complete under blocked-skip`。25 个 Refine family 已逐项阅读 owner 与相邻章节，
其中 MSA、VIA-SD、DRPO/APPO、KServe、AA-AgentPerf 与 Notes2Skills 对长期机制形成实质 refine；其余
Refine family 用于增强或重新验证既有论证，不复制论文摘要。9 个 No Change 都有章节级去重依据；biology
只保留 Weekly domain evidence；Ling/Ring 保持 Emerging，FastContext 保持 Withdrawn，blocked survey 不进入正文。
Archive/Discovery Gate 因 blocked family 与 cross-index recall 继续开放，不影响已闭合 Source Family 的 Books Gate。

## Ignored Noise

- 以任务 domain 名称替代实际权限、目标与外部副作用评估。
- 把 `28.4x` FLOPs reduction、`14.2x` Prefill 或 `7.6x` Decode 写成跨模型/跨硬件通用速度。
- 把当前 SM100 repository contract 倒写成论文 H800 实验已经披露的实现条件。
- 以 Hugging Face 展示日替代 arXiv v1 / first-public date。
- 把 KServe release feature list 写成跨版本 control-plane guarantee；把 AA-AgentPerf vendor headline 当成
  模型能力或跨系统通用倍率；把单一 CLIP/RTX 6000 Ada profile 外推成所有 FP8/LLM workload 收益。

## 2026-07-31 Full Re-Audit Addendum

- N-day exploit 研究已全文复核；patch diff、target version、sandbox、trial count 与 executable
  grader 进入 Ch62 的 evaluation contract，不把 18 个 Firefox/21 个 Windows target 外推。
- Agents in biology 升级全文阅读：确定 domain tool、structured result 与 provenance 的
  分层写入 Ch74；具体工具和 benchmark 不进入长期正文。

## Full Source Review

### Agents in biology — 23/30

- **Source Family / Coverage**：`BIOLOGY-AGENT-WORKFLOW`；Anthropic 2026-06-08 full research report、
  tool/environment and task materials；已覆盖 domain tools、structured observations、expert review、
  benchmark/case limitations。
- **Mechanism / Evidence Boundary**：Agent 将 model reasoning 接到 database/code/domain tool 并保留
  structured result；证明受控 biology tasks 的 workflow potential，不证明 wet-lab execution、
  biological validity 或自治 discovery。
- **Trade-offs / Decision**：专业 tool 提高 grounding，也新增 schema/version、permission、cost、
  hazardous action 与 expert acceptance。Ch69/74/77 已读；`No Change — Already Covered`。

### LLM impact on N-day exploits — 25/30

- **Source Family ID / Type / Date**：`N-DAY-EXPLOIT-IMPACT`；Anthropic 2026-06-08 full report，
  联读 Firefox/Mozilla harness、Windows VM grader 和 W21 exploit-eval family。
- **Full-read Coverage**：已覆盖 18 SpiderMonkey patches、21 Windows kernel vulnerabilities、
  target selection、three/50-trial designs、3M-token budgets、tooling、fresh-VM verification、cost/time、
  exploit-chain grading、limitations 和 patch-window comparison。
- **Problem / Previous Design / Changed Constraint**：patch disclosure/release/deployment 存在时间差；
  人工 exploit development 成本曾使此 gap 可接受。模型把 diff→PoC→primitive→chain 的时间压缩后，
  defender 的旧 rollout cadence 可能不再匹配 attacker cycle。
- **Mechanism / Ownership / Flow**：Firefox 输入 public diff 与 vulnerable/patched ASAN jsshell；Windows
  输入 binaries、symbols、Ghidra/Ghidriff 与 live VM；artifact 在 fresh target 重编译重跑，以 nonce、
  differential behavior 和 human/agentic review 验证。target/version、harness、grader、artifact owner 分离。
- **Evidence Boundary**：报告证明所选 targets、models、budget 和 sandbox 中 PoC/chain capability；
  不证明 full-browser remote exploit、campaign deployment、所有 CVE 或 unrestricted internet setting。
  “几千美元”是该实验 API credit，不是通用攻击成本。
- **Trade-offs / Evolution**：更可执行 eval 提供真实风险证据，也产生 dangerous artifact、selection bias、
  grader attack 和披露风险；static capability screen 仍作为前置层。关系为 W21 的 `Direct Evolution`。
- **ROADMAP / Chapters / Decision**：Ch62 主 owner，已读 Ch61～63、Ch68、Ch74、Ch77；现有正文
  已吸收 target/version/trial/verifier contract。`No Change — Already Covered`。

### MiniMax Sparse Attention — 28/30

- **Candidate / Week / Source Family**：`MINIMAX-MSA-GQA-BLOCK-SPARSE`；W24；arXiv:2606.13392
  v1 2026-06-11，v2 2026-06-12。v2 为 30 页、14 figures；后续 repository state 只用于机制核验，
  不作为 W24 新事件。
- **Direct / Related Primary Sources**：arXiv metadata、完整 HTML/PDF 内容、论文全部 equations/tables/
  figures/Appendices B～C、MiniMax-AI/MSA repository README/API/test/benchmark layout。联读论文自述的
  GQA、NSA、DSA、MoBA、inference-time sparse 与 FlashAttention lineage；未以 Hugging Face 自动摘要
  代替正文。
- **Access / Full-read Coverage**：已覆盖 Abstract、Introduction、Preliminary、Architecture、Training、
  complexity、Index/TopK、KV-outer sparse Attention、sparse KL kernel、109B experiments、training
  dynamics、main/long-context/efficiency results、Related Work、Conclusion、selection visualization、
  pilot gradient-source experiments、detach/warmup/sink/sliding-window/block-size/value-head ablations和 EOF。
  论文没有独立 Limitations/Threats to Validity section，记为 `Not Provided`，未静默补造。
- **Original Problem / Previous Design / Changed Constraint**：Dense GQA 保留 exact global access 且有成熟
  kernel，在短/中 context 或 exactness 优先时合理；million-token workflow 使 `T²` pair compute 与 KV
  traffic 成为约束。Post-hoc token sparsification免重训，却可能留下 dense training cost、某阶段近 dense
  速度与不规则 memory access；固定 window 预算稳定，却会错过 content-dependent remote evidence。
- **Mechanism / State Ownership / Control Flow**：每个 GQA group 有一个 index-query head，所有 groups
  共享轻量 index-key head；token scores 经 block max-pool 得到 block scores，Top-k 选择每组最多
  `k×B_k` tokens，local self block 强制保留，Main Branch 在所选支持上做标准 softmax。Index Branch
  拥有 ephemeral selection，Main Branch 是 teacher/data path；KL teacher 和 index input 均 stop-gradient，
  因而辅助 loss 只更新 index projections，不允许 backbone 通过改变 teacher distribution 投机降 KL。
- **Training / Migration Details**：从头训练与 dense-to-sparse CPT 都先 full-Attention warmup indexer，再让
  selector 控制 Main Branch。主实验使用 41-layer、109B total/6B active MoE、64 Q heads、4 KV heads、
  head dim 128、`B_k=128`、`k=16`，总预算 3T tokens；MSA-PT warmup 40B，MSA-CPT 从 2.6T dense
  checkpoint 出发，以 40B warmup + 360B sparse CPT 完成 matched 3T budget，另做约 140B long-context
  extension。它说明迁移成本不是零，也不能把 400B CPT 称为“直接替换 kernel”。
- **Kernel / Data Flow**：exp-free Top-k 利用 softmax 的 order preservation；KV-outer loop 为每个 selected
  KV tile 收集 queries，reverse index 与 query concatenation 提高 reuse/MMA utilization。popular sink
  block 会形成极端 skew，预调度把 hot tile 切给多个 CTA；partial outputs/LSE 写入 HBM buffer，再由
  second-phase combine 归一化，避免 atomics。Sparse KL 的 LSE 与主 forward 融合，backward 以 persistent
  work queue 处理 data-dependent load imbalance。
- **Evaluation Contract**：quality 比较 Full、MSA-PT、MSA-CPT 的 matched 3T-token checkpoints，覆盖
  general/math/code/image/video、agent-task perplexity、RULER 与 HELMET；长上下文表只到 128K，不能用
  1M speed measurement 证明 1M task quality。Top-k microbenchmark 是 H800、fp32 scores、median of 50
  post-warmup iterations；headline efficiency 使用同一 64Q/4KV/head128、`k=16`、block128，在 1M
  context 报告 28.4x attention FLOPs、14.2x Prefill、7.6x Decode。GPU 数、batch/concurrency、完整 dtype、
  latency samples、功耗和 end-to-end TTFT/TPOT/SLO 未完整披露，故不得外推。
- **What the Evidence Proves**：在作者披露的 matched training 与 hardware contract 下，GQA-group
  block selector 可通过局部 KL supervision 稳定学习；从头 sparse pretraining 与有成本的 dense-CPT
  均可接近 dense baseline；co-designed loop order/load balancing 能把部分理论 sparsity 转成测得的
  wall-clock 改善。Ablations 支持 warmup/detach，且 dynamic selection 在 pilot agent PPL 上优于
  FLOP-matched sliding window。
- **What It Does Not Prove / Threats**：单一作者模型族与训练数据不能证明跨 architecture transfer；
  “broad GPU”是作者主张，当前公开 repository 要求 SM100，论文却在 H800 测量；没有独立 long-run
  production traffic、tail latency、failure recovery 或 selector calibration。Main results 多为单点 matched
  comparisons，统计方差、contamination、训练 compute/energy 与 dense baseline 复现细节有限；local
  block safety 不能保证所有远程 evidence 被选中。
- **Trade-offs / Failure Modes / Previous Design**：MSA 以 coarse block 和 group-shared selection 换
  regular access，可能浪费 block 内无关 tokens或合并不同 query-head需求；selector miss 是 silent semantic
  error。Warmup、KL、reverse index、workspace、two-phase combine、专用 precision/layout 和 model revision
  compatibility 是新增成本。Dense FlashAttention 在短 context、exactness和portable kernel优先时仍成立；
  sliding/local pattern 在局部任务和硬预算下仍成立；inference-only sparsity 在不能重训时仍成立。
- **Evolution / ROADMAP / Existing Coverage**：关系为 `dense → invocation-level sparse discovery → native
  sparse training → staged dense-to-sparse migration` 的 `Direct Evolution`，kernel 是 `Layering /
  Dependency`。已读 Ch21～24 与 Ch39；Ch22 已有 hybrid/NSA/DSA主线，Ch39 已有 discovery/selection/
  index-build 与 dense fallback。新增长期缺口是 gradient ownership、GQA-group block granularity 与
  KV-outer hot-block execution 的连接。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`，Ch22 主
  owner、Ch39 short handoff；Historical Books Gate 关闭，本轮不修改 Books。待验证：H800 headline 的
  batch/dtype/GPU count；SM100 artifact 与历史实现的 revision lineage；mixed-length/`q_len<k_len`、TP、
  scheduler 与 prefix-cache contract；selection recall 对真实 long-horizon tasks 的 failure distribution。

### KServe v0.19.0 — 29/30

- **Candidate / Week / Source Family / History**：`KSERVE-0.19-LLMISVC-CONTROL-STATE`；W24；official
  release v0.19.0 published 2026-06-14，signed tag `b0eda63`。它是 v0.18 后的 control-plane evolution node，
  不是推理 runtime 新版本。
- **Direct / Related Primary Sources**：KServe official release notes及 linked PR surface；现有 Ch49/57 的
  official architecture/docs 用于 ownership cross-check。release 含许多 fixes/features；只把相互构成长期
  contract 的 LLMISvc/LocalModel/routing/lifecycle changes 提升为 review focus。
- **Access / Full-read Coverage**：已读 release 全部 changes，重点覆盖 LLMInferenceService labels/annotations、
  observed applied config/routing topology/workload references、readiness conditions/events、LocalModel cache、
  static LoRA reconciliation、precise-prefix `sha256_cbor` identity、llm-d migration、WVA autoscaling tests/status、
  dual REST/gRPC routing、termination/preStop/shutdown timeout、gateway origin、protocol metrics、CRD conversion、
  deletion validation与 upgrade safety。未逐一读取所有 80+ linked PR diff，精确实现细节只按 release fact 记录。
- **Original Problem / Previous Design / Changed Constraint**：spec→Deployment/Service 的基础 reconciliation
  对单 runtime、单 topology 很合理；LLM serving 引入 shared/local model cache、prefix-aware routing、static
  adapters、heterogeneous GPU、multi-component llm-d migration、长 termination 与多层 Gateway 后，单一 Ready
  boolean 不能解释“desired、applied、observed、traffic-eligible 是否一致”。
- **Mechanism / State Ownership / Flow**：用户/spec owner 声明 desired service/config；controller 选择并记录
  applied config，status 回报 observed routing topology、workload references 与具体 conditions；LocalModel
  subsystem拥有节点侧 artifact cache lifecycle；adapter reconciler 管 static LoRA desired/observed state；router
  以 canonical precise-prefix identity 选择 path；Gateway origin/protocol、autoscaler condition 与 termination hook
  分别拥有网络、capacity 与 drain state。data plane runtime 仍拥有 token/KV execution，controller 不越权。
- **Implementation / Evaluation Contract**：release 包含 quick-install、autoscaling、endpoint、pipeline-health、
  migration 与 structured E2E improvements，但没有统一公开的 cluster size、GPU/model、traffic mix、length、batch、
  concurrency、TTFT/TPOT/goodput、upgrade duration 或 failure-injection结果。因而证明的是功能/测试 surface 与
  signed release identity，不证明 production reliability 或性能。
- **What the Evidence Proves / Does Not Prove**：证明成熟 LLM control plane 必须让 applied/observed topology、
  artifact/cache、adapter、routing、migration、readiness 与 termination 可见；不证明 v0.19 所有路径在任意
  Kubernetes/Gateway/runtime/accelerator组合成立，也不证明 precise-prefix hash 自动保证 semantic equivalence。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：更多 observed state 改善 explainability，也扩大
  status schema、controller write amplification、stale observation 与 upgrade compatibility；LocalModel 降低拉取
  延迟但新增 node cache capacity/eviction/digest authority；static LoRA reconciliation 新增 base/adapter
  compatibility；graceful drain 延长 replacement time。普通 `InferenceService` 在非 LLM、无复杂 topology 的服务
  仍更简单，v0.18 path 也不会因 v0.19 发布而失效。
- **Evolution Relationship**：`desired service → runtime/workload reconciliation → LLM topology → applied/observed
  state + cache/adapter/routing/migration lifecycle` 是 `Direct Evolution`；与 vLLM/llm-d data plane 是
  `Layering / Dependency`。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch49、Ch55、Ch57、Ch58。Ch57 已拥有 desired state、
  runtime compatibility、readiness/revision lifecycle，但缺少 applied/observed topology 与 artifact/adapter/cache/
  termination 的闭环表达；Ch49/58 已拥有 LLM topology/Gateway，Ch55 拥有 artifact identity。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Version-sensitive`，
  主 owner Ch57；Historical Books Gate 关闭，不修改 Books。待核验关键 linked PR code、status eventual consistency、
  migration rollback、cache/adapter garbage collection、prefix identity semantic collision、gateway failure、drain timeout
  与多 runtime E2E/SLO。

### AA-AgentPerf — 28/30

- **Candidate / Week / Source Family / History**：`AA-AGENTPERF-WORKFLOW-SERVING-BENCH`；W24；Artificial
  Analysis benchmark-owner article/methodology与 NVIDIA launch analysis均发布 2026-06-12。leaderboard 是 live
  artifact，event node 锁定 launch methodology，不把后续结果倒写为 W24。
- **Direct / Related Primary Sources**：Artificial Analysis launch article、AA-AgentPerf methodology、serving
  configuration browser；NVIDIA technical blog仅作 vendor submission/config/result cross-check。benchmark owner
  是方法权威，vendor headline 不能替代它。
- **Access / Full-read Coverage**：已读 dataset construction、OpenCode harness、model/language mix、ISL/OSL、
  tool-delay distribution、500-trajectory tuning subset/private test set、model-specific SLO、concurrency search、
  steady-state filter、server/local token count、accelerator power、normalization、submission verification与 live update；
  联读 NVIDIA 的 DeepSeek-V4-Pro/NVL72 system framing。private test samples与完整 per-run raw traces不可审计。
- **Original Problem / Previous Design / Changed Constraint**：固定 prompt/output length microbenchmark 适合隔离
  kernel/runtime capacity，却不能表达 Agent 百轮交互、5K～131K variable context、短 tool-call outputs、CPU tool
  think time、prefix reuse和 bursty scheduler pressure。约束从“每次 request 多快”变为“整个 workflow 在交互 SLO 下
  能同时维持多少 active sessions”。
- **Mechanism / State Ownership / Flow**：预录 coding-agent trajectories按 phase顺序 replay；dynamic prefixes
  抑制不受控 prefix-cache shortcut；tool calls按 tool-specific delay distribution模拟；系统经 exponential ramp+
  binary search找最大并发。每 request计算 P25 output speed与P95 TTFT，phase只在目标并发稳定至少30秒后计量；
  token usage由 server metadata与本地 tokenizer交叉验证，accelerator power现场测量。benchmark owner拥有 dataset/
  SLO/scorer，submitter拥有 serving config，system拥有运行时状态，不能混成一个“hardware score”。
- **Implementation / Evaluation Contract**：launch trajectories来自三种开源模型在 OpenCode 中解决真实 public
  repos，12+ languages；ISL约5K～131K、mean约27K，tool delays小于0.1s到5s、median约1s。DeepSeek-V4-Pro
  launch SLO与后续 current methodology已有变化，正说明 live revision必须固定。per-MW只计 measured GPU die+HBM，
  排除CPU、network、cooling；vendor-tuned和benchmark-owner-tuned configurations需分别解释。
- **What the Evidence Proves / Does Not Prove**：证明 Agent serving需要 trajectory-level arrival/length/tool-delay+
  per-request latency/speed SLO下的并发容量，而非单一 tokens/s；不证明 replay等于真实用户闭环、private set无偏、
  tool simulation代表所有环境，也不证明初始 vendor倍率能跨软件版本、model、power boundary或facility复现。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：realistic replay提高 workload relevance，却降低
  isolation与公开可复现性；private set防 tuning，也削弱第三方 audit；允许 production optimizations提高外部有效性，
  同时让framework/config/team tuning成为分数一部分。microbenchmark仍适合回归 kernel与定位 bottleneck；在线 trace
  shadow benchmark在真实arrival/tool distribution上更强，但隐私、漂移与成本更高。
- **Evolution Relationship**：`fixed-shape microbench → request-distribution serving benchmark → SLO-constrained
  workflow trajectory replay → live configuration/power-aware capacity benchmark` 是 `Direct Evolution`，不是替代
  correctness/e2e Agent task evaluation；它们是 `Layering / Dependency`。
- **ROADMAP / Chapters / Existing Coverage**：已读 Ch62、Ch65、Ch66与 Ch77。Ch62 已拥有 model/harness/
  environment/run identity，Ch66已有 cost-to-quality/SLO，但稳定缺口是 tool think time、workflow phase、steady-state
  concurrency和power boundary组成的 capacity contract；Ch77只需 arrival/trajectory handoff。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument / Live Benchmark`，
  Ch62/66 joint owner、Ch65/77 handoff；Historical Books Gate关闭，不修改Books。待验证 immutable launch spec/
  dataset digest、per-run raw traces、quality verifier、prefix policy、CPU/network/facility power、failure/queue tails、
  vendor tuning parity与跨模型/runtime复现。

### ModelOpt FP8 → ONNX Q/DQ → TensorRT engine — 24/30

- **Candidate / Week / Source Family / History**：`NVIDIA-FP8-ONNX-TRT-DEPLOYMENT`；W24；NVIDIA technical
  blog published 2026-06-09，是三篇 tutorial 的 deployment node，不是新的 quantization algorithm。
- **Direct / Related Primary Sources**：NVIDIA full tutorial、ModelOpt exporter、ONNX Q/DQ/TensorRT support links
  与文中 profiling contract。AI-generated page summary未作为证据；正文表/图之间不一致的数字不被引用为结论。
- **Access / Full-read Coverage**：已读 checkpoint restore/export、opset20+、weight-side Q/DQ folding、attention
  setup、dynamic batch axis、graph inspection、strong typing、FP32 scale workaround、`trtexec` build/profile、hardware/
  shape/dtype与 fusion explanation。没有 accuracy/evaluation dataset、concurrency/tail SLO或 long-run stability evidence。
- **Original Problem / Previous Design / Changed Constraint**：量化 checkpoint适合训练/存储语义，但 production
  runtime不能从“权重是 FP8”推断哪些 activation/attention边界低精度、哪些 Q/DQ可融合、哪个 kernel与GPU capability
  可执行。约束从 numerical compression变成 portable graph annotation + compiler specialization + engine identity。
- **Mechanism / State Ownership / Flow**：ModelOpt checkpoint经 exporter生成 ONNX opset20+ Q/DQ graph；weight-side
  Q→DQ可提前折叠成 FP8-stored DQ chain；TensorRT builder在 strongly typed contract下融合相邻Q/DQ并选择FP8 GEMM/
  attention kernels，生成 shape/hardware-specific engine。checkpoint拥有量化参数，ONNX拥有 graph precision boundary，
  builder/runtime拥有 fusion/kernel，Registry必须拥有完整 revision chain。
- **Implementation / Evaluation Contract**：CLIP text max length77，image 224×224；build/profile batch128；RTX 6000
  Ada、TensorRT10.16；median来自默认measurement window。FP8 matmul需要 Ada+。正文figure alt text与后续 prose的
  latency/size numbers不一致，故不保留speedup headline，只保留条件化 mechanism evidence。
- **What the Evidence Proves / Does Not Prove**：证明低精度收益需 checkpoint→graph precision annotation→builder
  fusion→hardware kernel 的闭环，也证明 strong typing可暴露 exporter dtype mismatch；不证明 CLIP accuracy保持、
  任意 dynamic shape/LLM可转换、任意 GPU提速或 production concurrency/SLO稳定。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：Q/DQ提高显式性与 portability，但 graph更复杂，
  exporter workaround可能漂移，engine与shape/GPU/runtime绑定；FP16在旧GPU、accuracy敏感、unsupported op或低维护
  预算下仍合理。ONNX artifact不能替代 engine artifact，也不能替代 golden-output regression。
- **Evolution / ROADMAP / Existing Coverage**：`quantized training checkpoint → Q/DQ interchange graph → compiled
  strongly typed engine → profiled runtime` 是 `Layering / Dependency`。已读 Ch45、Ch50、Ch55；Ch45 已具体拥有
  precision/graph rewrite/kernel/hardware mapping，Ch55拥有 artifact identity，因此没有新长期缺口。
- **Integration Decision / Files / Open Questions**：`No Change — Already Covered / Bounded Engineering Case`；
  主 owner Ch45，Ch50/55 handoff；不修改Books。待验证 accuracy contract、dynamic shapes、mixed precision fallback、
  engine portability、exporter/builder revision skew与完整 concurrency/tail-latency workload。

### EvoArena — 25/30

- **Source / Coverage**：已读 arXiv:2606.13681 的 metadata、method、三类 evolving environments、EvoMem、
  baselines、evaluation、ablation 与 limitations。它评测的是环境持续变化下的跨回合适应，不是普通静态
  memory benchmark。
- **Mechanism / Evidence Boundary**：EvoMem 用 append-only patches 记录变化前后 memory、rationale 与
  evidence，并以最新 memory 加检索 patch 参与下一回合。Terminal、SWE 与 persona 三类任务显示平均收益有限且
  不一致：部分链式任务改善，persona conflict/single-transfer 反而退化；证据不能外推为通用 lifelong learning。
- **Trade-off / ROADMAP / Decision**：patch provenance 提高可追溯与 rollback 能力，也增加冲突、检索污染、
  supersession 和 retention 成本。旧式静态 memory 在环境稳定、变化少时仍合理。主 owner Ch73，Ch62/77 handoff；
  provisional `Refine — Existing Argument / Experimental`，Historical Books Gate 关闭。

### Hypothesis-Tree Refinement / Arbor — 25/30

- **Source / Coverage**：已读 arXiv:2606.11926 的完整方法、系统结构、matched-budget baselines、六项任务、
  ablations 与关键附录。Artifact、development evaluator 与 held-out evaluator 的角色分别核验。
- **Mechanism / Evidence Boundary**：持久 coordinator 管理 hypothesis tree；隔离 worktree executor 修改 artifact，
  每个 node 绑定 hypothesis、artifact、evidence 与 insight，held-out merge gate 决定是否提升。实验只覆盖固定、可标量
  评分的有限 AI 工程任务，证明可审计搜索闭环的 feasibility，不证明开放科学发现的有效性。
- **Trade-off / ROADMAP / Decision**：相较一次性 Agent loop，tree 保留失败分支和证据，但引入 branch budget、
  evaluator overfitting、merge contamination 与 stale insight。已读 Ch77 及 Ch62/76；主 owner Ch77，provisional
  `Refine — Existing Argument / Experimental`。

### WeaveBench — 26/30

- **Source / Coverage**：已读 arXiv:2606.09426 的 114-task dataset、GUI/CLI protocol、trajectory-aware judge、
  model/harness split、evaluation 与 error analysis。任务中位数 76 次 tool calls、16 次 modality switches。
- **Mechanism / Evidence Boundary**：judge 会重新读取 artifact、screenshots 与 logs，并以 protocol violation
  清零；总分受 process 与 deliverable 的较低者约束。GUI-only/CLI-only 极弱而 hybrid 仍远未饱和，且 judge 对
  表面完成分数有大幅纠偏；但范围限 English/Linux 与有限 harness，不能代表所有 computer-use workflow。
- **Trade-off / ROADMAP / Decision**：trajectory grading 提升过程真实性，却依赖环境可重放、judge calibration
  与昂贵 artifact inspection。Ch62 已覆盖 environment+trace+artifact 三层证据，故 `No Change — Already Covered /
  Experimental Case`；Ch74/77 handoff。

### MaxProof — 25/30

- **Source / Coverage**：已读 arXiv:2606.13473 的 generator-verifier training、population test-time scaling、
  proof benchmarks、baselines 与 ablations；论文未提供独立 Limitations section，未披露项保持 `Not Disclosed`。
- **Mechanism / Evidence Boundary**：训练期让 generator 与 verifier 共同提高，推理期维护多个候选 proof population
  并用 verifier 选择/演化。结果支持作者 proof workload 下的互补性；MaxProof 未作为所有 standalone-base 对照，
  不能把提升归因于单一模块，也不能外推到无形式 verifier 的 reasoning。
- **Trade-off / ROADMAP / Decision**：更强 verifier 可提高 search efficiency，也会形成 reward exploitation、
  correlated verifier error 与 test-time compute cost。主 owner Ch29、Ch62 handoff；provisional `Refine — Existing
  Argument / Experimental`。

### Manifold Power Iteration for MoE Routing — 25/30

- **Source / Coverage**：已读 arXiv:2606.12397 的 router derivation、manifold power iteration、3B→11B scaling、
  implementation、baselines 与 ablations；实现栈包括 TorchTitan、FSDP、PyTorch SDPA 与 MegaBlocks。
- **Mechanism / Evidence Boundary**：router rows 不再只以 token-logit 训练，而是迭代对齐 expert feature geometry，
  试图让 routing boundary 与 expert 子空间共同演化。实验支持作者训练设置中的优化/质量变化，不证明 production
  dispatch、network locality 或 load balance 会自动改善。
- **Trade-off / ROADMAP / Decision**：几何自适应增加额外状态与优化计算，也可能放大 expert collapse、feature
  drift 和 routing/dispatch mismatch。传统 linear router 在规模较小或可观测/运维优先时仍合理。主 owner Ch21，
  provisional `Refine — Existing Argument / Experimental`。

### FORT-Searcher — 25/30

- **Source / Coverage**：已读 arXiv:2606.12087 的 entity/evidence graph、question synthesis、adversarial
  refinement、SFT、BrowseComp-family evaluation 与 ablations；没有独立 Limitations section。
- **Mechanism / Evidence Boundary**：数据流水线显式控制实体、证据路径和问题难度，再用对抗检查降低 shortcut，
  以训练 search trajectory 而非只生成答案。结果说明受控合成数据能改善所测 deep-search tasks；不能排除语料
  contamination，也不能证明对实时 Web、权限工具和多域事实同样有效。
- **Trade-off / ROADMAP / Decision**：shortcut resistance 提高任务质量，却引入 graph construction、judge bias、
  synthetic style 与维护成本。主 owner Ch23，Ch72/62 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Claw-SWE-Bench — 25/30

- **Source / Coverage**：已读 arXiv:2606.12344 的 adapter、workspace/patch pipeline、350-task benchmark、
  Lite-80 scale check、runtime contract 与 evaluation。相同 prompt/evaluator 下区分 model API 与 OpenClaw harness。
- **Mechanism / Evidence Boundary**：adapter 将通用 harness 放入 repository workspace，收集并清理 patch 后交给
  SWE grader；实验为单次运行，3600 秒上限、worker concurrency 3，不能把少量百分点差异视作稳定模型排名。
- **Trade-off / ROADMAP / Decision**：统一 adapter 提高 harness 可比性，却仍把 tool policy、repo state 与 model
  capability 绑定在观测结果中。Ch62 已有 model/harness/environment identity，故 `No Change — Already Covered /
  Experimental Case`。

### FlashMemory-DeepSeek-V4 — 25/30

- **Source / Coverage**：已读 arXiv:2606.09079 的 lookahead indexer、HCA/CSA attention、训练与三项 benchmark；
  “DeepSeek-V4”是作者系统命名，不是官方 DeepSeek release。项目已声明暂停 active development。
- **Mechanism / Evidence Boundary**：压缩 index 预测未来相关 KV，HCA 用近似检索缩小候选，局部 CSA 保留 exact
  window。作者明确承认 dual-encoder compressed index 在极端 recall/precision 间存在边界；证据不能证明任意
  长上下文、硬件或 serving SLO 的收益。
- **Trade-off / ROADMAP / Decision**：lookahead 降低访问量但新增 index freshness、miss、训练/推理 identity 与
  fallback 成本；dense/local exact attention 仍是高可靠基线。主 owner Ch22，provisional `Refine — Existing
  Argument / Experimental`。

### Z-Reward — 24/30

- **Source / Coverage**：已读 arXiv:2606.09076 的 distributional reward、teacher/student pipeline、text-to-image
  evaluation、ablations 与 limitations。实验使用 27B teacher、9B student；更广泛 reward modeling 仅是 future work。
- **Mechanism / Evidence Boundary**：reward model 不只输出 scalar，而是学习 score distribution 并利用 rationale
  supervision 表达不确定性。结果支持特定 text-to-image preference setting 的 calibration/selection，不证明 LLM
  RL、agent reward 或开放式 verifier 会同样受益。
- **Trade-off / ROADMAP / Decision**：distribution 保存更多 epistemic signal，也增加标注、teacher bias、计算与
  reward hacking surface。主 owner Ch27，Ch29/62 handoff；provisional `Refine — Existing Argument / Experimental`。

### SearchSwarm — 25/30

- **Source / Coverage**：已读 arXiv:2606.09730 的 delegation policy、multi-agent workflow、四项 benchmark、
  matched-cost evaluation 与 error discussion。训练/测试模型及 judge contract 已核验。
- **Mechanism / Evidence Boundary**：系统把长程 research 分解、委派并汇总证据，收益取决于可分解性、delegation
  quality 和共享证据。实验不能证明增加 Agent 数量是单向演进，也不能消除 communication tax、重复检索与 error
  amplification。
- **Trade-off / ROADMAP / Decision**：并行提高覆盖率但增加协调、provenance 合并和成本控制。Ch78 已明确
  single-agent headroom、task decomposability 与 coordination tax，故 `No Change — Already Covered / Experimental
  Case`；Ch72/77 handoff。

### DeNovoSWE — 25/30

- **Source / Coverage**：已读 arXiv:2606.10728 的 4,818 个 document-to-repository tasks、sandbox construction、
  draft/critic/repair workflow、trajectory filtering、evaluation 与 ablations；联读公开环境说明。
- **Mechanism / Evidence Boundary**：能力描述与 profiling 先在受限 sandbox 中生成 repository，critic/repair
  根据 tests 修复；source stripping、git/cache/network controls 用于降低 leakage。difficulty-aware trajectory threshold
  从 0.9 调到 0.6 的收益相对 modest，不能证明真实 brownfield engineering 或长期维护能力。
- **Trade-off / ROADMAP / Decision**：可执行 repository 提升训练信号，但 synthetic spec、grader completeness、
  contamination 与 environment cost 成为新边界。主 owner Ch23，Ch62/80 handoff；provisional `Refine — Existing
  Argument / Experimental`。

### Rethinking Divergence Regularization / DRPO — 25/30

- **Source / Coverage**：已读 arXiv:2606.09821 的 Binary-TV derivation、与 PPO/GRPO/DPPO/SPO 的梯度比较、
  bounded weighting、Qwen 4B/30B/35B experiments、ablations 与 sensitivity。
- **Mechanism / Evidence Boundary**：smooth trust region 在 policy ratio 越界后仍给出有界纠正信号，避免 hard mask
  丢弃样本或 unbounded weight 放大梯度。结果来自 DAPO 13K math、16 responses 及 AIME 类 rule-verifiable tasks，
  不证明开放 reward、tool use 或长期 on-policy drift 下同样稳定。
- **Trade-off / ROADMAP / Decision**：更连续的 divergence control 保留 corrective gradient，也新增 threshold/
  estimator bias 与 reference-policy identity 问题。主 owner Ch29，provisional `Integrate — New Mechanism /
  Experimental`，待 Historical Books Gate 后再判断正文强度。

### EurekAgent — 25/30

- **Source / Coverage**：已读 arXiv:2606.13662 的 prepare→propose→implement loop、persistent memory、resource
  limits、evaluator/human monitor、math/kernel/MLE tasks 与 ablations。
- **Mechanism / Evidence Boundary**：Agent 不只改 solution artifact，也调整可执行 environment，并依 evaluator
  反馈迭代。实验绑定 Claude Code/GLM-5.1 和 metric-driven tasks；不能证明开放式科学评价、权限安全或任意环境
  修改都可靠。
- **Trade-off / ROADMAP / Decision**：environment engineering 扩大 search space，也增加 evaluator overfit、
  authority escalation、artifact provenance 与 rollback 风险。Ch77 已有 evaluator-driven artifact optimization，故
  `No Change — Already Covered / Experimental Case`；Ch68/80 handoff。

### End-to-End Context Compression at Scale — 26/30

- **Source / Coverage**：已读 arXiv:2606.09659 的 LCLM soft-token encoder/decoder、训练目标、parallel encoding、
  RULER/LongBench/LongHealth evaluation、H200 profiling 与 ablations。
- **Mechanism / Evidence Boundary**：context 先被 query-independent encoder 压成 soft tokens，再由标准 decoder
  prefill；encoder windows 可并行并在多轮复用。作者 profiling 为单样本 H200、encoder batch 128、window 1024、
  Qwen3-4B，不能外推到多租户 concurrency、tail SLO 或不可容忍信息丢失的任务。
- **Trade-off / ROADMAP / Decision**：compression 减少目标 prefill 与重复上下文成本，却新增 lossy boundary、
  provenance、cache identity 和 query mismatch。短上下文或 exact-evidence workload 仍应保留原文/KV。主 owner
  Ch22，Ch71 handoff；provisional `Refine — Existing Argument / Experimental`。

### On Subquadratic Architectures — 24/30

- **Source / Coverage**：已读 arXiv:2606.12364 对 xLSTM、Mamba-2、Gated DeltaNet 的统一分析，覆盖 400M code、
  distillation、1～80M time-series、implementation 与 limitations。
- **Mechanism / Evidence Boundary**：论文把 efficient sequence model 区分为 information accumulation 与
  finite-state tracking，并指出 xLSTM 混合二者。比较支持所测规模/teacher 下的 inductive-bias 差异，不证明某一
  subquadratic family 在 frontier scale 或所有 long-context tasks 优于 attention。
- **Trade-off / ROADMAP / Decision**：有限状态降低复杂度但增加 state bottleneck、训练稳定性与 selective recall
  边界；dense/hybrid attention 仍适合随机访问和高保真检索。主 owner Ch22，Ch14/17 handoff；provisional
  `Refine — Existing Argument / Experimental`。

### Workflow-GYM — 25/30

- **Source / Coverage**：已读 arXiv:2606.11042 的 professional GUI tasks、isolated environments、expert atomic
  procedures、binary artifact/GUI criteria、model evaluation 与 failure analysis。
- **Mechanism / Evidence Boundary**：评分依据最终 artifact 与 GUI state，而非自然语言自报完成；结果揭示 stage
  omission、error propagation 与 objective drift。snapshot action 无法观测连续 GUI dynamics，任务/应用范围有限，
  因而不是完整 desktop autonomy 证明。
- **Trade-off / ROADMAP / Decision**：可执行环境提高真实性，也带来 reset、nondeterminism、version drift 与昂贵
  人工 rubric。主 owner Ch62，Ch74 handoff；provisional `Refine — Existing Argument / Experimental`。

### MTP with Rejection Sampling / Bebop — 27/30

- **Source / Coverage**：已读 arXiv:2606.12370 的 acceptance/TV derivation、multi-step loss、fused full-vocabulary
  kernel、SFT/RL integration、baselines、ablations 与 limitations。
- **Mechanism / Evidence Boundary**：target-only/greedy training 在高熵 rollout 中 acceptance 下降；论文以
  `1-TV` 对齐 proposal 与 target distribution，并将多步 TV loss 用 fused kernel 实现。Qwen3.5/3.6/3.7、
  SGLang+veRL async RL 的作者结果最高约 1.8×，只在披露 contract 下成立；top-K TV 与 entropy heuristics 不稳定。
- **Trade-off / ROADMAP / Decision**：distribution matching 提高 accepted draft length，却增加 full-vocab training
  cost、proposal staleness 与 verifier coupling。主 owner Ch44，Ch29 handoff；provisional `Refine — Existing
  Argument / Experimental`。

### EEVEE — 25/30

- **Source / Coverage**：已读 arXiv:2606.11182 的 prompt slots、learned router、router/prompt coevolution、
  adaptation data、四项 benchmark、three-repeat evaluation 与 ablations。
- **Mechanism / Evidence Boundary**：固定 target model 不更新权重，router 选择可学习 prompts，二者交替演化；
  adaptation 依赖 labeled/rule-based feedback，并非无监督在线 reflection。结果覆盖 Qwen3-4B/DeepSeek-V3.2
  与 API workers，不能证明跨域持续迁移或 production rollback。
- **Trade-off / ROADMAP / Decision**：test-time prompt learning 降低 weight update 成本，却新增 feedback bias、
  distribution feedback loop、prompt contamination 与 state lifecycle。主 owner Ch76，Ch73 handoff；provisional
  `Refine — Existing Argument / Experimental`。

### Data Journalist Agent — 25/30

- **Source / Coverage**：已读 arXiv:2606.11176 的 multi-agent HTML-report pipeline、Inspector claim-code-source
  binding、re-execution verifier、automated evaluation 与 53-person human study。
- **Mechanism / Evidence Boundary**：Inspector 将 atomic claim 绑定代码与来源并重跑生成过程；这证明 lineage
  可追踪，不等于 claim 正确。作者也报告 contamination 可能，且系统缺少在线 human feedback；human 对外部数据
  角度与设计的评价更强。
- **Trade-off / ROADMAP / Decision**：claim-level provenance 提高 reviewability，但增加粒度、re-execution 成本和
  source trust 问题。Ch62 已明确 claim→evidence→execution lineage，故 `No Change — Already Covered / Experimental
  Case`；Ch77/80 handoff。

### Chatbot-to-Digital-Colleague Survey — 22/30

- **Source / Coverage**：已读 arXiv:2606.14502 的 taxonomy、workspace/skill synthesis、system comparison 与
  future directions。它是 secondary survey，不是新机制或受控实验的 primary evidence。
- **Mechanism / Evidence Boundary**：survey 将 chatbot 到 digital colleague 的变化归纳为 persistent workspace、
  skills、tool use 与 collaboration，但不能为具体 product internals、可靠性或治理结论提供独立证明。
- **Trade-off / ROADMAP / Decision**：可作为术语导航和 source-family 索引；Ch80 已覆盖 Agent Platform 的
  workspace/skill/runtime 边界，故 `No Change — Already Covered / Secondary Synthesis`。

### Ling / Ring 2.6 Technical Report — 24/30

- **Source / Coverage**：已读 arXiv:2606.15079 的 MoE architecture、specialize-then-distill、multi-MTP、
  ASystem/ARouter rollout infrastructure、evaluations 与 disclosure boundary。它是厂商 technical report。
- **Mechanism / Evidence Boundary**：ARouter 迁移 tail rollout requests，并配合 checkpoint/failover；报告把模型、
  训练与 inference improvements 联合呈现，无法将 benchmark 增益唯一归因于某机制，也不能据 product capability
  反推未披露 internals。
- **Trade-off / ROADMAP / Decision**：尾部迁移可降低 straggler，但增加 rollout ownership、checkpoint consistency、
  migration waste 与 failure recovery。主 owner Ch29，Ch52 handoff；`Emerging / Version-sensitive`，不把 vendor
  benchmark 写成通用结论。

### APPO — 25/30

- **Source / Coverage**：已读 arXiv:2606.12384 的 procedural/decision branching、branching score、future
  advantage、dual groups、theorem assumptions、tool-use experiments 与 ablations。
- **Mechanism / Evidence Boundary**：rollout 在候选决策点分叉，比较共享前缀后的未来优势，以更细的 credit
  assignment 更新 policy。理论依赖作者假设，实验只说明特定 Llama/Qwen、ToolStar/STILL、veRL BF16 contract
  下的有效性；没有证明所有 split point 最优。
- **Trade-off / ROADMAP / Decision**：branching 增强反事实信号，但增加 environment replay、on-policy identity、
  sample correlation 与 compute。主 owner Ch29，provisional `Integrate — New Mechanism / Experimental`。

### HarnessX — 25/30

- **Source / Coverage**：已读 arXiv:2606.14249 的 typed harness primitives、substitution algebra、harness MDP、
  deterministic code-edit acceptance、trace store、co-evolution 与 off-policy buffer。
- **Mechanism / Evidence Boundary**：harness configuration 被当作可优化 artifact；只有不引入 regression 的代码
  edit 才接受，mixed buffer 保留 behavior-policy identity。实验复用 adaptation tasks、缺少 held-out evaluation，
  存在 selection bias 与 harness overfit。
- **Trade-off / ROADMAP / Decision**：可演化 harness 提高 task fit，也扩大权限、回归、版本和 trace retention
  surface。主 owner Ch80，Ch77/29 handoff；provisional `Refine — Existing Argument / Experimental`。

### RedAct — 24/30

- **Source / Coverage**：已读 arXiv:2606.10813 的 black-box threat model、selective trajectory rewrite、
  verifier-preserving evidence、behavioral watermark、75 tasks/154 skills 与多种 reuse evaluation。
- **Mechanism / Evidence Boundary**：公开 traces 可能泄漏可复用 procedure；RedAct 重写 action/context 以降低
  skill extraction，同时保留 verifier 所需证据。controlled tasks 支持作者攻击/防御比较；watermark 只是统计信号，
  不能证明 ownership，也不能覆盖所有 adaptive attacker。
- **Trade-off / ROADMAP / Decision**：减少 procedural leakage 会损害 audit/debug/reproducibility，并新增 rewrite
  policy 与 verifier mismatch。主 owner Ch68，Ch64/65/80 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### Rethinking Efficient Attention in Hybrid Architectures — 25/30

- **Source / Coverage**：已读 arXiv:2606.15378 的 full-attention/SWA/recurrent mixers、NoPE placement、
  training dynamics、retrieval evaluation、scaling controls 与 limitations。
- **Mechanism / Evidence Boundary**：efficient component 不只节省 FLOPs，也作为 optimization prior 改变 full
  attention 学会 retrieval 的速度。实验规模小于 1B、训练不超过 100B tokens、context 16K→32K；不能外推到
  frontier scale 或宣称最终能力必然提高。
- **Trade-off / ROADMAP / Decision**：hybrid prior 加快某些学习路径，但引入 layer allocation、state mismatch 与
  scaling uncertainty；足够训练下 full attention 仍可能收敛。主 owner Ch22，provisional `Refine — Existing
  Argument / Experimental`。

### Visual Repository Representations / SeeRepo — 24/30

- **Source / Coverage**：已读 arXiv:2606.14061 的 typed repository graph、visual rendering、text+vision layering、
  500 SWE-bench tasks、depth controls、localization/repair evaluation。
- **Mechanism / Evidence Boundary**：contains/imports/inherits/invokes graph 被渲染为视觉工作态，与源码文本联合输入；
  收益主要出现在 localization，accuracy/efficiency 随模型而变，不能证明视觉表示普遍优于 structured text。
- **Trade-off / ROADMAP / Decision**：视觉压缩 topology 但可能丢失 symbol semantics、增加 rendering/version/token
  cost。主 owner Ch71，Ch75 handoff；provisional `Refine — Existing Argument / Experimental`。

### Cross-Lingual BrowseComp-Plus — 24/30

- **Source / Coverage**：已读 arXiv:2606.15345 的固定跨语言 corpus、12-language translation、retrieval recall、
  agent integration、oracle comparison、translation review 与 limitations。
- **Mechanism / Evidence Boundary**：English query/answer 对应多语言 evidence，使 retrieval failure 与 evidence
  integration failure 可分开测量；oracle 暴露语言差距。专家 translation 评分较高但仍有 artifact，结论不代表
  live Web freshness、所有语言或 citation correctness。
- **Trade-off / ROADMAP / Decision**：固定 corpus 提高可复现性但弱化真实 Web drift；多语言 evidence 增加
  calibration 与 provenance 难度。主 owner Ch72，Ch62 handoff；provisional `Refine — Existing Argument /
  Experimental`。

### DailyReport — 24/30

- **Source / Coverage**：已读 arXiv:2606.12871 的 150 tasks、3,546 rubrics、10 domains/35 categories、freshness
  construction、17-system evaluation、priority aggregation 与 judge contract。
- **Mechanism / Evidence Boundary**：benchmark 以当前事件构造 open-ended daily report，并分 instruction、
  factuality 与 rationality；Gemini judge 与动态 freshness 增加现实性，也带来 revision drift、judge dependence 与
  难以复跑。它不能证明某系统在任意实时研究任务上可靠。
- **Trade-off / ROADMAP / Decision**：Ch62 已覆盖 live benchmark revision、judge calibration、evidence freshness，
  故 `No Change — Already Covered / Experimental Case`；Ch72/77 handoff。

### Notes2Skills — 25/30

- **Source / Coverage**：已读 arXiv:2606.11897 的 fact/judgment/suggestion extraction、deterministic MetaSkill
  compiler、SHA provenance、executor evidence gate、三类 corpora、149 directive checks 与 downstream study。
- **Mechanism / Evidence Boundary**：先保留 notebook statement 的 epistemic status，再编译为 governed skill；
  executor 只有在证据 gate 通过时执行。directive preservation 较广，但 downstream 仅三次 nanopore sessions、
  依赖专家，且 extraction error 会传递到 skill。
- **Trade-off / ROADMAP / Decision**：把不确定笔记直接变能力会产生 authority/provenance 风险；显式 compiler 与
  hash lineage 提高 review/rollback，却增加 lifecycle 管理。主 owner Ch80，Ch74/68 handoff；provisional
  `Integrate — New Mechanism / Experimental`。

### Recovered Full Source Review — VIA-SD — 26/30

- **Source / Coverage / Version**：已读 arXiv:2606.12243v1（2026-06-10）HTML 的 Introduction、Related
  Work、Method、公式与完整伪代码、T5/Gemma2/LLaMA2/Qwen experiments、routing/threshold/tier ablations、
  offline search-cost analysis 与关键 Appendices。作者 project page 已定位；当前结论只绑定 v1 的公开合同。
- **Original Problem / Previous Design / Changed Constraint**：两级 speculative decoding 用轻量 drafter 提案、
  target model 并行验证；对高接受率 workload 很合理。但其 ownership 只有“接受 draft”或“交给 full verifier
  重算”两档，中等置信 token 也支付最大模型成本。模型族中可复用的层与 output head 使 intermediate verifier
  可能低成本承接这部分 token。
- **Mechanism / State Ownership / Flow**：VIA-SD 将 verifier 的层保留 mask 作为离线搜索状态，以 KL-style
  margin cost 选择共享 embedding/output head 的 routed slim verifier。运行时 drafter 产生 block；slim verifier
  先并行检查，分别接受、自己重写或升级到 full verifier；最早重写位置拥有 rollback boundary，剩余 suffix
  作废。因而 control flow 从 binary fallback 变成 typed, hierarchical ownership，而非只增强 drafter。
- **Evaluation / What It Proves**：作者在 T5、Gemma2、LLaMA2、Qwen 的 summarization、translation、QA、
  reasoning/coding workload 上，与 speculative decoding 和 cascade baselines 比较 rejection、task metric 与
  speed；还报告 tier count、skip ratio、threshold、random-mask ablation 和每个 model pair 18～68 分钟的离线
  search。证据支持“在该模型、threshold 与硬件合同内，三层 routing 可减少 full-verifier invocation”。它不证明
  所有 backend 都能并发执行三层、不证明 lossless equivalence 在所有 lossy threshold 下成立，也未给出生产
  batching、multi-tenant、KV rollback、tail SLO 与 mask drift 合同。
- **Trade-offs / Failure Modes / Previous Design Boundary**：获得更细粒度 compute allocation，付出 mask search、
  多模型态 KV/activation 管理、两级阈值 calibration、rollback 与 backend integration。四层、五层实验反而变慢，
  说明 hierarchy 不是单调收益；model/domain drift 还可能让固定 mask 失效。短输出、高 drafter acceptance、或
  backend 无法高效承载 routed submodel 时，传统两级 SD 仍更简单可靠。
- **Evolution / ROADMAP / Decision**：`Direct Evolution`：binary draft/full verify → cascade decision → intermediate
  verifier participates in generation → routed multi-tier ownership。已读 Ch43～45；主 owner Ch44，Ch45 只保留
  backend contract handoff。provisional `Refine — Existing Argument / Experimental`；Historical Books Gate
  关闭，本轮不改 Books。

## Final Books Integration Ledger

| # | Candidate | Final disposition | Stable owner / chapter evidence |
| ---: | --- | --- | --- |
| 1 | Agents in biology | Weekly Only — Domain Evidence | Cross-owner domain case；不形成独立系统机制 |
| 2 | LLM impact on N-day exploits | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 target/version/harness/artifact contract |
| 3 | MiniMax Sparse Attention | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；补 selector gradient ownership 与 KV-outer execution |
| 4 | EvoArena | Refine — Existing Argument | `PLATFORM-PRODUCTION` Ch73；动态环境与 promotion boundary |
| 5 | Hypothesis-Tree Refinement | Refine — Existing Argument | `AGENT-WORKFLOW` Ch81；假设分支、证据与停止条件 |
| 6 | WeaveBench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 multi-stage artifact/state evidence |
| 7 | MaxProof | Refine — Existing Argument | `TRAIN-GRPO` Ch33；可执行 theorem verifier 下的 credit boundary |
| 8 | Manifold Power Iteration for MoE routing | Refine — Existing Argument | `MODEL-MOE` Ch21；router geometry 与 executable dispatch 分层 |
| 9 | FORT-Searcher | Refine — Existing Argument | `TRAIN-DATA` Ch27；verifier-first task synthesis 与 leakage boundary |
| 10 | Claw-SWE-Bench | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 repository/environment verifier contract |
| 11 | Agentic Environment Engineering survey | Unverified / Blocked | 无可验证正文；不分配 Books mechanism owner |
| 12 | FlashMemory-DeepSeek-V4 | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；有损 working-state 与 exact fallback |
| 13 | Z-Reward | Refine — Existing Argument | `TRAIN-RLHF` Ch31；reward distribution 与 uncertainty boundary |
| 14 | SearchSwarm | No Change — Already Covered | `AGENT-MULTI-AGENT` Ch82 已有 decomposability/coordination/error amplification |
| 15 | VIA-SD | Refine — Existing Argument | `INFER-SPECULATIVE-DECODING` Ch48；分层 verifier ownership 与 rollback |
| 16 | DeNovoSWE | Refine — Existing Argument | `TRAIN-DATA` Ch27；可执行 repository synthesis 与 sandbox identity |
| 17 | DRPO | Refine — Existing Argument | `TRAIN-GRPO` Ch33；越界后有界连续纠正信号 |
| 18 | EurekAgent | No Change — Already Covered | `AGENT-WORKFLOW` Ch81 已有 evaluator-driven artifact optimization |
| 19 | End-to-End Context Compression at Scale | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；latent working-set identity 与 exact-evidence fallback |
| 20 | On Subquadratic Architectures | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；accumulation 与 finite-state tracking 分支 |
| 21 | Workflow-GYM | Refine — Existing Argument | `PLATFORM-EVALUATION-SYSTEM` Ch66；GUI artifact/state verifier contract |
| 22 | MTP with Rejection Sampling / Bebop | Refine — Existing Argument | `INFER-SPECULATIVE-DECODING` Ch48；proposal-distribution alignment |
| 23 | EEVEE | Refine — Existing Argument | `AGENT-REFLECTION` Ch80；prompt/router mutable state 与 rollback |
| 24 | Data Journalist Agent | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 claim→code→source→execution lineage |
| 25 | Chatbot-to-Digital-Colleague survey | No Change — Already Covered | `AGENT-PLATFORM` Ch84；secondary synthesis 无新增 primary mechanism |
| 26 | FastContext | Withdrawn — Provenance Record | 撤稿记录；不进入 Books |
| 27 | Ling / Ring 2.6 Technical Report | Emerging / Version-sensitive | `TRAIN-GRPO` Ch33 handoff；不从厂商联合 benchmark 归因机制 |
| 28 | APPO | Refine — Existing Argument | `TRAIN-GRPO` Ch33；共享前缀后的 decision-branch counterfactual credit |
| 29 | HarnessX | Refine — Existing Argument | `AGENT-PLATFORM` Ch84；harness artifact revision 与 regression gate |
| 30 | RedAct | Refine — Existing Argument | `PLATFORM-SECURITY` Ch72；procedural leakage 与 auditability trade-off |
| 31 | Rethinking Efficient Attention in Hybrid Architectures | Refine — Existing Argument | `MODEL-LONG-CONTEXT` Ch22；optimization prior 与 final capability 分离 |
| 32 | Visual Repository Representations / SeeRepo | Refine — Existing Argument | `AGENT-CONTEXT` Ch75；typed topology view 与 source-text coexistence |
| 33 | Cross-Lingual BrowseComp-Plus | Refine — Existing Argument | `AGENT-RAG` Ch76；跨语言 evidence identity 与 oracle split |
| 34 | DailyReport | No Change — Already Covered | `PLATFORM-EVALUATION-SYSTEM` Ch66 已有 live revision/judge/freshness contract |
| 35 | Notes2Skills | Refine — Existing Argument | `AGENT-PLATFORM` Ch84；保留 epistemic status 的 note-to-Skill compilation |
| 36 | KServe v0.19.0 | Refine — Existing Argument / Version-sensitive | `PLATFORM-KSERVE` Ch61；desired/applied/observed lifecycle |
| 37 | AA-AgentPerf | Refine — Existing Argument / Live Benchmark | `PLATFORM-EVALUATION-SYSTEM` Ch66；workflow-capacity contract |
| 38 | ModelOpt FP8→ONNX→TensorRT | No Change — Already Covered | `INFER-TENSORRT-LLM` Ch49 已有 precision→graph→kernel→hardware chain |

逐行复算结果：38/38 final；25 Refine、9 No Change、1 Weekly Only、1 Emerging、1 Withdrawn、
1 Unverified / Blocked。Blocked family 没有获得机制 owner；`No Change` 均指向已读章节中的具体论点。

## Blocked Primary-Source Backlog

| Candidate | First-public Date | Blocked Primary Source | Claims explicitly not verified |
| --- | --- | --- | --- |
| Agentic Environment Engineering survey | 2026-06-10 | arXiv:2606.12191 | taxonomy evidence、environment ownership、synthesis/evaluation boundaries and missing systems evidence |

2026-08-13 以精确 arXiv identity 重试原 31 项：VIA-SD HTML 后续恢复并完成上述非模板化 Source Review；
Agentic Environment Engineering survey 仍无可验证正文。后者不计 Full Source Review、不分配 Books owner、
不从摘要推断机制；按用户 blocked-skip 规则 current-review queue 清零并推进 W25。W24 discovery/Historical
Evidence Gates 因该 family 和 academic cross-index 仍保持 Open。

## Repository Changes

- W24 从 2 个 baseline 扩展为 38 个 scored families；完成 MSA 全文、Appendix、artifact 与 Ch21～24/
  Ch39 邻接审计；原 31 项 blocked 中 29 项恢复全文并完成机制、证据边界、trade-off、章节邻接与 disposition，
  VIA-SD 已恢复，只有 Agentic Environment Engineering survey 保留 `Unverified / Blocked Backlog`；current-review
  pending 清零并推进 cursor 至 W25。8 个 W23、1 个 W22 spillback 已按 v1 回拨，W25/W26 feed
  共恢复 12 个 W24 families；2025 first-public paper 只记录 cross-year curation node。FastContext
  作为 withdrawn low-score record 保留。fixed official/Infra replay 新增并全文审计 KServe v0.19.0、
  AA-AgentPerf 与 FP8→ONNX→TensorRT engineering chain；前两项 provisional refine Ch57 与 Ch62/66，后一项
  Ch49 `No Change`。vLLM v0.23.0 按 official release date 归 W25。Books Integration 完成 38/38 final
  dispositions；正文 refine `MODEL-LONG-CONTEXT`、`TRAIN-GRPO`、`INFER-SPECULATIVE-DECODING`、
  `PLATFORM-KSERVE`、`PLATFORM-EVALUATION-SYSTEM` 与 `AGENT-PLATFORM`，并保留所有实验和版本边界。

## Open Questions

1. MSA 的 H800 headline measurement 能否获得完整 batch、dtype、GPU-count 与 latency/SLO contract？
2. 当前 SM100 artifact 与论文 H800 kernel 的 revision/porting lineage 如何界定？
3. Agentic Environment Engineering survey 的 primary source 恢复后，现有 provisional score 与
   source-family 边界是否需要修正？
4. KServe applied/observed state、LocalModel/static LoRA 与 termination/migration 在 failure injection 与 upgrade
   rollback 下是否保持一致，关键 linked PR 能否形成更强 code-level evidence？
5. AA-AgentPerf 的 immutable launch spec/dataset digest、per-run traces、quality verifier、whole-system power 与
   vendor tuning parity 能否公开，从而把 live leaderboard 变成可复现实验？
6. FP8 ONNX chain 能否补齐 accuracy、dynamic shape、mixed fallback、engine portability 与 concurrency/SLO contract？
7. DRPO/APPO、VIA-SD 与 Notes2Skills 的机制能否在独立 workload、held-out environment 和不同 runtime 下复现？

## Sources

- Anthropic Research index, “Paving the way for agents in biology” and
  “Measuring LLMs’ impact on N-day exploits,” dated 2026-06-08:
  https://www.anthropic.com/research
- Hugging Face Papers, 2026-W24 discovery index: https://huggingface.co/papers/week/2026-W24
- MiniMax Sparse Attention metadata: https://arxiv.org/abs/2606.13392
- MiniMax Sparse Attention HTML: https://arxiv.org/html/2606.13392
- MiniMax Sparse Attention artifact: https://github.com/MiniMax-AI/MSA
- KServe v0.19.0 release, published 2026-06-14:
  https://github.com/kserve/kserve/releases/tag/v0.19.0
- Artificial Analysis, “First results from AA-AgentPerf,” published 2026-06-12:
  https://artificialanalysis.ai/articles/aa-agentperf/
- AA-AgentPerf methodology:
  https://artificialanalysis.ai/methodology/agentperf
- NVIDIA AA-AgentPerf analysis, published 2026-06-12:
  https://developer.nvidia.com/blog/nvidia-achieves-leading-agentic-coding-performance-on-first-agentic-ai-benchmark/
- NVIDIA ModelOpt FP8 → ONNX → TensorRT tutorial, published 2026-06-09:
  https://developer.nvidia.com/blog/model-quantization-turn-fp8-checkpoints-into-high-performance-inference-engines-with-nvidia-tensorrt/
- EvoArena: https://arxiv.org/abs/2606.13681
- Hypothesis-Tree Refinement: https://arxiv.org/abs/2606.11926
- WeaveBench: https://arxiv.org/abs/2606.09426
- MaxProof: https://arxiv.org/abs/2606.13473
- Manifold Power Iteration for MoE routing: https://arxiv.org/abs/2606.12397
- FORT-Searcher: https://arxiv.org/abs/2606.12087
- Claw-SWE-Bench: https://arxiv.org/abs/2606.12344
- Agentic Environment Engineering survey: https://arxiv.org/abs/2606.12191
- FlashMemory-DeepSeek-V4: https://arxiv.org/abs/2606.09079
- Z-Reward: https://arxiv.org/abs/2606.09076
- SearchSwarm: https://arxiv.org/abs/2606.09730
- VIA-SD: https://arxiv.org/abs/2606.12243
- DeNovoSWE: https://arxiv.org/abs/2606.10728
- Rethinking Divergence Regularization in LLM RL: https://arxiv.org/abs/2606.09821
- EurekAgent: https://arxiv.org/abs/2606.13662
- End-to-End Context Compression at Scale: https://arxiv.org/abs/2606.09659
- On Subquadratic Architectures: https://arxiv.org/abs/2606.12364
- Workflow-GYM: https://arxiv.org/abs/2606.11042
- MTP with Rejection Sampling: https://arxiv.org/abs/2606.12370
- EEVEE: https://arxiv.org/abs/2606.11182
- Data Journalist Agent: https://arxiv.org/abs/2606.11176
- Chatbot-to-Digital-Colleague survey: https://arxiv.org/abs/2606.14502
- FastContext withdrawn record: https://arxiv.org/abs/2606.14066
- Ling and Ring 2.6 Technical Report: https://arxiv.org/abs/2606.15079
- APPO: https://arxiv.org/abs/2606.12384
- HarnessX: https://arxiv.org/abs/2606.14249
- RedAct: https://arxiv.org/abs/2606.10813
- Rethinking Efficient Attention in Hybrid Architectures: https://arxiv.org/abs/2606.15378
- Visual Repository Representations for LLM Agents: https://arxiv.org/abs/2606.14061
- Cross-Lingual BrowseComp-Plus: https://arxiv.org/abs/2606.15345
- DailyReport: https://arxiv.org/abs/2606.12871
- Notes2Skills: https://arxiv.org/abs/2606.11897
- W23 spillback, Agents' Last Exam: https://arxiv.org/abs/2606.05405
- W23 spillback, SWE-Explore: https://arxiv.org/abs/2606.07297
- W23 spillback, unembedding feature lens: https://arxiv.org/abs/2606.07502
- W23 spillback, On-Policy Distillation geometry: https://arxiv.org/abs/2606.07082
- W23 spillback, retrospective harness optimization: https://arxiv.org/abs/2606.05922
- W23 spillback, LatentSkill: https://arxiv.org/abs/2606.06087
- W23 spillback, OpenSkill: https://arxiv.org/abs/2606.06741
- W23 spillback, When Tools Fail: https://arxiv.org/abs/2606.05806
- W22 spillback, ResearchClawBench: https://arxiv.org/abs/2606.07591
- Cross-year psychometric paper: https://arxiv.org/abs/2509.10078
