# AI Research Weekly — 2026-W07

> Coverage Window: 2026-02-09～2026-02-15
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31
> Re-audit Status: 49 accessible Full Source Reviews complete / 1 blocked-skip / 0 ordinary pending; Source-Family Books Review Passed
> Books Gate: W07 Source-Family Gate complete; Archive Completion Gate remains Open

## Executive Summary

旧版周报只保留 Google time-varying scheduling 与 Seed2.0 两项，并据此写下“论文组没有
独立 Must Read”的结论。重新按发布日期扫描 Hugging Face Daily Papers、arXiv 元数据和官方
机构来源后，第一轮恢复 31 个与本书知识树直接相关的候选；机构 archive 交叉检验又发现 ARO、
RLTR、ProSeCo、UniT、Aletheia/Deep Think 与 Seedream 5.0 Lite 六项漏检；继续扫描下一工作日的
discovery page 又发现 ERL 与 REDSearcher 的 primary publication date 是 2 月 15 日，属于 W07
Sunday boundary。继续向后检查 2 月 16～17 日 discovery pages，又恢复十项首次公开日实际落在
W07 的论文。W16 curation feed 又暴露首次公开于 2 月 10 日的 SPEED-Bench，候选普查因此增至 50 项，
覆盖 post-training、long context、agent memory、synthetic environment、executable evaluation、
streaming model 与 distributed
training。旧结论已被候选普查推翻。目前 LLaDA2.1、Prism、Step 3.5 Flash、FeatureBench、
Weak-Driven Learning、Dr. SCI、Flexible Entropy Control、SkillRL、Agent World Model、Dr. MAS、
iGRPO、LycheeMemory、Chain of Mindset、GENIUS、GRU-Mem、Data Repetition、DataChef、StateLM 与
BAE、CLI-Gym、GoodVibe、DeAction、Composition-RL、G-OPD、Voxtral Realtime、Gaia2、
MiniCPM-SALA、SPES、INTENT 与 Dreaming in Code 已完成全文级复核；
InternAgent-1.5 的 22.8 MB 官方 PDF 仍超出直接 reader 限制；本轮已通过同一 arXiv v1 的可检索原文
片段、目录/Appendix、官方发布页、官方仓库与 2 月 14 日开放的 solution-optimization artifact 恢复
Method、Evaluation、memory ablation 与限制边界，但没有把片段重建冒充全文阅读，也没有用 5 月代码
替代 2 月报告，因此该项继续阻塞 Evidence Gate。
第一轮可读取候选的全文证据包已经完成；新恢复六项中 ARO、RLTR、ProSeCo 与 UniT
已完成全文复核，Aletheia/Deep Think 也已完成论文与官方发布的联合复核；Seedream 5.0 Lite
只达到 official product fact 证据层级。ERL 与 REDSearcher 已完成全文、Appendix 与公开 artifact
联合复核；新发现的十项已通过 metadata/date Gate，其中 FAC Synthesis、OneVision-Encoder 与
CoPE-VideoLM、Intelligent AI Delegation、DICE 与 SciAgentGym 已完成全文复核；
RL-finetuned VLM robustness、ARC、BrowseComp-V3 与 AIDev 也已完成全文、artifact、证据边界和
章节去重复核；SPEED-Bench 随后完成 v1 全文、measurement framework、实验、Appendices、版本与
Ch44/45/62 邻接审计。49 个恢复候选完成
非模板化 Source Review；InternAgent 已有
可审计的 partial packet，但完整正文访问仍未闭合。历史 GitHub release/RFC 与 Google Scholar/OpenAlex
discovery 覆盖也未闭环。按 blocked-skip 规则，Candidate Review Checkpoint 已通过；整周 Discovery /
Historical Archive Gate 仍保持 Open，但已完成全文审计 family 的 Source-Family Books Gate 随本轮逐项
Integration 与反向检查关闭。

## Coverage and Source Coverage

- 模型与研究机构：保留 Google 2 月 11 日、Step 3.5 Flash 2 月 11 日、Mistral Voxtral
  Realtime 2 月 11 日与 Seed2.0 2 月 14 日；交叉检验新增 Google Deep Think 2 月 11 日与
  ByteDance Seedream 5.0 Lite 2 月 13 日。厂商 benchmark 仍只视为作者/厂商主张。
- 论文与学术来源：HF 的 2 月 9～13 日页面用于 discovery；事件归周以 arXiv v1 日期为准。
  已恢复 50 项；其中 49 项完成来源复核、1 项有详细 partial packet 但仍被正文访问阻塞、0 项普通待审。后续 revision 只用于
  核验机制，不能改写 W07 的事件日期。
- AI Infra：本轮尚未完成 GitHub release/RFC 历史分页闭环；这构成 coverage limitation，
  不能继续维持“没有稳定 release”的肯定句。
- 周末边界：arXiv 通常不在周末形成常规新提交批次，但 2 月 14～15 日的官方发布仍需独立
  检索；Seed2.0 已保留，其他来源覆盖将在 Discovery Cross-Check 中明确。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Scheduling with time-varying capacity | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | No Change — `INFER-SCHEDULING` Ch56 already covers feedback capacity control |
| Seed2.0 official launch | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | Weekly Only — Product fact / mechanism not disclosed |
| Weak-Driven Learning | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Emerging — material revision boundary; no Books change |
| InternAgent-1.5 | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Unverified / Blocked — full report unavailable; blocked-skip |
| LLaDA2.1 | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Refine — `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 |
| Improving Data and Reward Design for Scientific Reasoning | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Refine — `TRAIN-DATA` Ch27 |
| Flexible Entropy Control in RLVR | 4 | 4 | 4 | 4 | 4 | 2 | 22/30 | Refine — `TRAIN-GRPO` Ch33 |
| SkillRL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | No Change — `AGENT-MEMORY` Ch77 already covers derived-memory lifecycle |
| Agent World Model | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `MULTIMODAL-WORLD-MODELS` Ch25 |
| Prism block-sparse attention | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Refine — `MODEL-LONG-CONTEXT` Ch22 |
| Dr. MAS | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-GRPO` Ch33 |
| iGRPO | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `TRAIN-GRPO` Ch33 |
| LycheeMemory | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Refine — `MODEL-LONG-CONTEXT` Ch22 |
| Chain of Mindset | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | No Change — Ch75/79/82 already separate context, planning and topology |
| Step 3.5 Flash technical report | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Refine — `TRAIN-DISTRIBUTED-TRAINING` Ch36; Ch22/33 handoff |
| GENIUS evaluation suite | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | No Change — `PLATFORM-EVALUATION-SYSTEM` Ch66 already owns generative evaluation contract |
| Gated Recurrent Memory | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `MODEL-LONG-CONTEXT` Ch22 |
| Data Repetition for Long-CoT SFT | 4 | 3 | 4 | 4 | 4 | 3 | 22/30 | Refine — `TRAIN-SFT` Ch29 |
| DataChef | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Refine — `TRAIN-DATA` Ch27 |
| FeatureBench | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| The Pensieve Paradigm / StateLM | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Integrate — `AGENT-CONTEXT` Ch75 |
| Blockwise Advantage Estimation | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `TRAIN-GRPO` Ch33 |
| CLI-Gym | 4 | 4 | 5 | 4 | 4 | 3 | 24/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| GoodVibe secure code generation | 3 | 4 | 4 | 4 | 4 | 3 | 22/30 | Emerging / Experimental — scorer and threat-model boundary too narrow |
| Off-task action detection for computer-use agents | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Integrate — `PLATFORM-SECURITY` Ch72 |
| Composition-RL | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-DATA` Ch27 |
| Generalized On-Policy Distillation | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `TRAIN-SFT` Ch29 |
| Voxtral Realtime | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Integrate — `INFER-KV-CACHE` Ch45 |
| Gaia2 dynamic/asynchronous agent benchmark | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| MiniCPM-SALA | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Refine — `MODEL-LONG-CONTEXT` Ch22 |
| Memory-efficient decentralized MoE pretraining | 4 | 4 | 4 | 3 | 4 | 3 | 22/30 | Emerging / Experimental — no durable Books change |
| Budget-constrained tool-use planning | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Integrate — `AGENT-PLANNING` Ch79 |
| Dreaming in Code for open-ended curricula | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Refine — `TRAIN-DATA` Ch27; experimental evidence boundary retained |
| ARO: Stabilizing and Accelerating LLM Training via Rotated Updates | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-PRETRAINING` Ch28 |
| Beyond Correctness / RLTR | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `TRAIN-GRPO` Ch33 |
| ProSeCo | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Refine — `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 |
| UniT multimodal test-time scaling | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Integrate — `AGENT-WORKFLOW` Ch81; experimental evidence boundary retained |
| Aletheia / Gemini Deep Think for mathematics research | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Seedream 5.0 Lite official launch | 3 | 3 | 3 | 4 | 3 | 2 | 18/30 | Weekly Only — Product Fact / Mechanism Not Disclosed |
| Experiential Reinforcement Learning | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` Ch33 |
| REDSearcher | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-DATA` Ch27 |
| Less is Enough / FAC Synthesis | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-DATA` Ch27 |
| OneVision-Encoder | 5 | 4 | 4 | 4 | 4 | 4 | 25/30 | Refine — `MULTIMODAL-REPRESENTATION` Ch23 |
| CoPE-VideoLM | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `MULTIMODAL-REPRESENTATION` Ch23 |
| Intelligent AI Delegation | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | No Change — Ch82/84 already define delegation authority and platform contract |
| DICE CUDA kernel generation | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Refine — `TRAIN-GRPO` Ch33 |
| SciAgentGym | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| RL-finetuned VLM robustness and CoT consistency | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| Learning to Configure Agentic AI Systems / ARC | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Integrate — `AGENT-PLATFORM` Ch84 |
| BrowseComp-V3 | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` Ch66 |
| AIDev | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | No Change — Ch66 already covers dataset provenance and attribution boundary |
| SPEED-Bench | 4 | 5 | 5 | 4 | 4 | 4 | 26/30 | No Change — `INFER-SPECULATIVE-DECODING` Ch48 already owns workload contract |

## Recovered Candidate Census

> 本表的 `Audit State` 与后续 Full Source Review 内的 `Human Gate Pending` 保留候选发现阶段的历史状态；
> 最终 Books disposition 以本周 `Candidate Scoring` 和文末 Source-Family Integration 表为准。

| Event Date | Candidate | Primary Identifier | Source Family | Initial ROADMAP Node | Audit State |
| --- | --- | --- | --- | --- | --- |
| 2026-02-09 | Weak-Driven Learning | arXiv:2602.08222 | post-training / weak checkpoints | Ch25, Ch28–30 | Full Review Complete — Emerging Revision Boundary |
| 2026-02-09 | InternAgent-1.5 | arXiv:2602.08990 | scientific-agent workflow | Ch73/75/77; Ch72/74/76/78 adjacent | Partial Source Packet / Unverified — Full Report Blocked |
| 2026-02-09 | LLaDA2.1 | arXiv:2602.08676 | diffusion-LM decoding | Ch38–45 | Full Review Complete — Books Candidate |
| 2026-02-09 | Improving Data and Reward Design for Scientific Reasoning | arXiv:2602.08321 | data / rubric reward | Ch23, Ch27–29, Ch62 | Full Review Complete — Books Candidate |
| 2026-02-10 | Flexible Entropy Control in RLVR | arXiv:2602.09782 | RLVR optimization | Ch28–29 | Full Review Complete — Books Candidate |
| 2026-02-09 | SkillRL | arXiv:2602.08234 | skill memory / recursive RL | Ch73, Ch77 | Full Review Complete — No Change |
| 2026-02-10 | Agent World Model | arXiv:2602.10090 | synthetic environments | Ch29, Ch62, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-09 | Prism | arXiv:2602.08426 | sparse prefill attention | Ch22, Ch39–45 | Full Review Complete — Books Candidate |
| 2026-02-09 | Dr. MAS | arXiv:2602.08847 | multi-agent RL runtime | Ch29, Ch78 | Full Review Complete — Books Candidate |
| 2026-02-09 | iGRPO | arXiv:2602.09000 | self-feedback RLVR | Ch29 | Full Review Complete — Books Candidate |
| 2026-02-09 | LycheeMemory | arXiv:2602.08382 | compressed long-context memory | Ch22, Ch71 | Full Review Complete — Books Candidate |
| 2026-02-10 | Chain of Mindset | arXiv:2602.10063 | reasoning-mode orchestration | Ch71, Ch75, Ch78 | Full Review Complete — No Change |
| 2026-02-11 | Step 3.5 Flash | arXiv:2602.10604 | model / MoE / MTP / RL | Ch21–22, Ch29, Ch32, Ch44 | Full Review Complete — Books Candidate |
| 2026-02-11 | GENIUS | arXiv:2602.11144 | generative evaluation | Ch62 | Full Review Complete — No Change |
| 2026-02-11 | Gated Recurrent Memory | arXiv:2602.10560 | recurrent memory controller | Ch22, Ch71 | Full Review Complete — Books Candidate |
| 2026-02-11 | Data Repetition for Long-CoT SFT | arXiv:2602.11149 | SFT data schedule | Ch25 | Full Review Complete — Books Candidate |
| 2026-02-11 | DataChef | arXiv:2602.11089 | data-recipe agent / RL | Ch23, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-11 | FeatureBench | arXiv:2602.10975 | executable coding evaluation | Ch62–64, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-12 | The Pensieve Paradigm | arXiv:2602.12108 | stateful LM / memory tools | Ch71, Ch73 | Full Review Complete — Books Candidate |
| 2026-02-10 | Blockwise Advantage Estimation | arXiv:2602.10231 | multi-objective credit assignment | Ch29 | Full Review Complete — Books Candidate |
| 2026-02-11 | CLI-Gym | arXiv:2602.10999 | environment inversion | Ch62, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-11 | GoodVibe | arXiv:2602.10778 | secure code generation | Ch65 | Full Review Complete — Emerging / Experimental |
| 2026-02-09 | Off-task action detection | arXiv:2602.08995 | computer-use guardrail | Ch67, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-12 | Composition-RL | arXiv:2602.12036 | synthetic verifiable prompts | Ch23, Ch29 | Full Review Complete — Books Candidate |
| 2026-02-12 | Generalized On-Policy Distillation | arXiv:2602.12125 | distillation / KL-constrained RL | Ch25, Ch29 | Full Review Complete — Books Candidate |
| 2026-02-11 | Voxtral Realtime | arXiv:2602.11298 | native streaming ASR | Ch18, Ch41, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-12 | Gaia2 | arXiv:2602.11964 | dynamic/asynchronous agent eval | Ch62–64, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-12 | MiniCPM-SALA | arXiv:2602.11761 | hybrid sparse/linear attention | Ch22, Ch38–45 | Full Review Complete — Books Candidate |
| 2026-02-12 | Decentralized MoE pretraining | arXiv:2602.11543 | distributed training | Ch21, Ch32–37 | Full Review Complete — Experimental |
| 2026-02-12 | Budget-constrained tool-use planning | arXiv:2602.11541 | cost-aware agent planning | Ch75, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-09 | Dreaming in Code | arXiv:2602.08194 | curriculum / executable environments | Ch29, Ch62, Ch77 | Full Review Complete — Experimental Books Candidate |
| 2026-02-09 | ARO | arXiv:2602.09006 | optimizer geometry / distributed training | Ch24, Ch31–36 | Full Review Complete — Books Candidate |
| 2026-02-09 | Beyond Correctness / RLTR | arXiv:2602.08489 | transfer reward / RLVR | Ch29, Ch62 | Full Review Complete — Books Candidate |
| 2026-02-12 | ProSeCo | arXiv:2602.11590 | diffusion-LM correction | Ch25, Ch40 | Full Review Complete — Books Candidate |
| 2026-02-12 | UniT | arXiv:2602.12279 | multimodal test-time workflow | Ch18, Ch62, Ch76–77 | Full Review Complete — Experimental Books Candidate |
| 2026-02-10 | Aletheia / Gemini Deep Think | arXiv:2602.10177 + official blog 2026-02-11 | scientific reasoning workflow / autonomy evidence | Ch62, Ch76–77 | Full Review Complete — Books Candidate |
| 2026-02-13 | Seedream 5.0 Lite | official launch 2026-02-13 | unified multimodal model | Ch18, Ch55, Ch62 | Weekly Only — Product Fact / Mechanism Not Disclosed |
| 2026-02-15 | Experiential Reinforcement Learning | arXiv:2602.13949 | reflection-conditioned RL | Ch29, Ch76 | Full Review Complete — Books Candidate |
| 2026-02-15 | REDSearcher | arXiv:2602.14234 | search-agent training / simulated environment | Ch23, Ch29, Ch72, Ch75, Ch77 | Full Review Complete — Books Candidate |
| 2026-02-11 | Less is Enough / FAC Synthesis | arXiv:2602.10388 | feature-space data diversity / synthesis | Ch23; Ch5/25 handoff | Books Candidate — Full Review Complete |
| 2026-02-09 | OneVision-Encoder | arXiv:2602.08683 | codec-aligned sparse visual encoding | Ch18; Ch22/39 handoff | Books Candidate — Full Review Complete |
| 2026-02-13 | CoPE-VideoLM | arXiv:2602.13191 | codec primitives / video token reduction | Ch18; Ch22/39/41 handoff | Books Candidate — Full Review Complete |
| 2026-02-12 | Intelligent AI Delegation | arXiv:2602.11865 | authority / responsibility / delegation protocol | Ch78; Ch79/80 handoff | Full Review Complete — No Change |
| 2026-02-12 | DICE | arXiv:2602.11715 | diffusion LM / executable CUDA optimization | Ch29; Ch23/40/45/62/77 handoff | Books Candidate — Full Review Complete |
| 2026-02-13 | SciAgentGym | arXiv:2602.12984 | scientific tool environment / benchmark | Ch62; Ch23/74/77 handoff | Books Candidate — Full Review Complete |
| 2026-02-13 | RL-finetuned VLM robustness | arXiv:2602.12506 | multimodal RL / faithfulness evaluation | Ch62; Ch18/29 handoff | Books Candidate — Full Review Complete |
| 2026-02-12 | ARC agent configuration | arXiv:2602.11574 | workload-aware workflow/configuration policy | Ch80; Ch66/77/78 handoff | Books Candidate — Full Review Complete |
| 2026-02-13 | BrowseComp-V3 | arXiv:2602.12876 | multimodal browsing / process evaluation | Ch62; Ch72/74–77 handoff | Books Candidate — Full Review Complete |
| 2026-02-09 | AIDev | arXiv:2602.09185 | real-world coding-agent PR dataset | Ch62; Ch77/80 handoff | Full Review Complete — No Change / Dataset Only |
| 2026-02-10 | SPEED-Bench | arXiv:2604.09557 | speculative-decoding evaluation / serving workload | Ch44 owner; Ch45/62 handoff | Full Review Complete — No Change / Experimental Evaluation Case |

### Date-boundary exclusions found during census

以下条目出现在 HF 2 月 9～13 日发现页，但 arXiv v1 早于 W07；它们必须回到所属周核验，
不得按 HF submission date 回填到 W07：F-GRPO、Entropy Dynamics、MSign、Canzona、
OmniMoE、TermiGen、AIRS-Bench、RLinf-USER、BudgetMem、LOCA-bench、NanoQuant、KV-CoRE、
OPUS、Secure Code RL、ALMA、ScaleEnv、TerminalTraj、AgentSys、ASA、ECHO-2、Free()、
Recurrent-Depth VLA、Context Compression、RelayGen、CodeCircuit、Agent Skills、Aster、
On Randomness in Agentic Evals 与 MemFly。它们作为 cross-week recall 修复线索保留，不重复计分。

机构 archive 还暴露出第二类日期陷阱：Microsoft Semantic Caching、AgentRx、WINA、interwhen、
PUNT、Google DialogLab、Apple Ferret-UI Lite 与 Self-Proving Models 的机构文章或 revision 落在
2 月 9～15 日附近，但 arXiv v1/首次公开日属于更早周次；Apple Chain-of-Thought potential 的
v1 则是 2 月 16 日，属于 W08。Google Gemini 科学研究案例合集 arXiv:2602.03837 v1 为 2 月 3 日，
归 W06；W07 的 2 月 11 日 Blog 只作为 Aletheia source family 的关联机构节点，不重复计分。
HF 2 月 17 日页面还证明 discovery date 会跨越 Sunday boundary：ERL 与 REDSearcher 的 arXiv
primary publication date 均为 2 月 15 日，故回填 W07，不能留到 W08。

## Full Source Review

### Scheduling with time-varying capacity

- **Candidate / Week / Score:** Non-preemptive Throughput Maximization under Time-varying Capacity /
  2026-W07 / 24/30；`Source Family ID: time-varying-capacity-nonpreemptive-scheduling`。
- **Source Type / Dates / Sources:** SPAA 2025 primary paper + Google Research 2026-02-11 technical
  explanation；2026 是 institutional publication node。
- **Full-read Coverage:** Verified；已检查 job model、offline/online variants、approximation/competitive
  guarantees、greedy/primal-dual approach、failure of static algorithms、limits 和 future work。
- **Problem / Previous Design:** static-capacity schedulers 对固定 slots 合理；当 failure、maintenance、
  power limit 或 higher-priority workloads 造成 leftover capacity 波动时，non-preemptive job 一旦被中断
  会丢失全部进度。
- **Mechanism / State / Flow:** jobs 由 release、deadline、processing time、weight 定义；capacity profile
  约束同时运行数量。Offline 已知 jobs/capacity；online 只预知 capacity landscape，arrival 时做不可逆
  接纳/替换/中断/拒绝决定。
- **Evaluation / Proof Boundary:** unit-profit Greedy 给 1/2 approximation、weighted offline 1/4、online
  给 first constant competitive ratio 1/11；这些是抽象模型 guarantees，不是 GPU cluster trace benchmark。
- **Trade-offs / Previous Design:** robust admission 牺牲即时 utilization，依赖 capacity forecast，并忽略
  gang/topology/data locality/restartable checkpoint；可抢占且 checkpoint 成本低的 job 仍适合 preemption。
- **Evolution / ROADMAP:** `Principle Reuse`；Ch59 主 owner，Ch52/60 相邻。已读 Ch51～52、Ch58～61；
  现有章节已把 capacity、preemption cost、queue/SLO 与 workload drift 联合建模。
- **Integration Decision:** `No Change — Already Covered`；理论 paper 作为边界案例留 Weekly。
- **Open Questions:** capacity forecast error、gang shape、checkpoint cost 与 energy/carbon windows 怎样进入
  competitive online admission？

### Seed2.0 official launch

- **Candidate / Week / Score:** Seed2.0 launch / 2026-W07 / 21/30；
  `Source Family ID: seed2-model-family-2026`。
- **Source Type / Date / Sources:** ByteDance Seed 官方模型发布，2026-02-14；与 W27 2026-06-30
  model card 属同一 source family。
- **Access / Coverage:** Verified as official model-family state；已检查公开定位、模型档位、长任务/
  instruction/tool claims 与 later model-card relationship。架构、训练和 serving 机制未完整披露。
- **Mechanism / Evaluation Boundary:** 产品能力与厂商 benchmark 可验证为发布方主张；不能反推内部
  planner、reasoning policy、runtime topology 或跨 workload SLO。
- **Trade-offs / Evolution:** 多档模型让 cost/latency/capability 成为 routing 选择，却增加 model-version、
  prompt、eval、fallback 和 policy matrix；单模型部署在稳定任务和严格复现中仍更简单。
- **ROADMAP / Chapters:** `Layering / Dependency`；Ch20/55/62，已读相邻章节。现有 model registry 和
  evaluation identity 已覆盖长期机制。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Open Questions:** later model card 是否披露足以建立 capability、deployment tier 与 safety evaluation
  的稳定 contract？

### LLaDA2.1: Speeding Up Text Diffusion via Token Editing

- **Candidate / Week / Score:** LLaDA2.1 / 2026-W07 / 27/30；
  `Source Family ID: llada-editable-diffusion-decoding`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 2026-02-09、v2 2026-02-10、v3
  2026-02-13，均在本周窗口。复核使用 v3；事件日期仍取 v1。
- **Direct / Related Primary Sources:** arXiv:2602.08676；论文同时指向 dFactory、AReaL、ASystem
  与定制 SGLang，但这些实现没有为本文所有机制提供可独立复现的完整 artifact。
- **Access and Full-read Coverage:** Verified；已覆盖 metadata/revision、Introduction、decoding
  equations、CPT/SFT/RL、infrastructure、evaluation tables、MBE/quantization ablation、Outlook and
  Limitation、Conclusion 与相关 references。
- **Original Problem / Previous Design:** 传统 absorbing-state dLLM 让状态单调地从 `[MASK]`
  变成固定 token。保守 threshold 能降低并行解码错误，因而在模型不会重写已生成 token 时是合理
  选择；代价是一次 forward 接受的 token 变少，错误又会令后续生成更保守。
- **Changed Constraint / Mechanism:** 目标从“只生成未确定 token”变为“允许同一参数空间先草拟、
  再改写”。每步同时维护 unmask set `Γ_t` 与 edit set `Δ_t`：前者由 `τ_mask` 控制 M2T，后者
  只在新 argmax 与当前 token 不同且置信度超过 `τ_edit` 时执行 T2T。CPT/SFT 混合 masked
  positions 与随机噪声，训练 drafting/editing 两条能力；inference 既可单 block 编辑，也可用
  MBE 回看已完成 blocks。RL 以 ELBO-based block likelihood proxy 和 vectorized estimation
  近似不可直接求得的 sequence likelihood。
- **State Ownership / Control and Data Flow:** prompt block 是固定条件；decoding blocks 是可变生成
  状态。threshold policy 决定本轮哪些 positions 被提交或重写，runtime 还要维护跨 block 的编辑
  范围、radix cache、batch identity 与最终输出边界。这不是 AR Decode 中“只向末尾 append token”
  的同义优化。
- **Implementation Details:** 训练沿用 dFactory，并为 multi-turn forward 增加专用实现；RL 扩展
  AReaL/ASystem，rollout 使用定制 SGLang；inference 组合 Alpha-MoE、per-block FP8、block-wise
  causal attention、radix caching 与 batching。论文未公开硬件、batch、并发和 SLO，因此不能把
  TPS 当成跨 runtime 通用结果。
- **Evaluation Contract:** 33 个 knowledge/reasoning/code/math/agent benchmarks；论文报告 TPF
  与 TPS，并比较 S/Q modes、quantization 和 MBE。作者实验显示 MBE 通常提高 score、同时降低
  TPF/throughput；S Mode 的速度—质量关系随 domain 变化。HumanEval+ 的峰值 TPS 只属于本文
  模型、quantization、threshold 与未完整披露硬件条件。
- **What the Evidence Proves / Does Not Prove:** 证据支持“可训练的 retroactive editing 能把
  dLLM operating point 从单一 threshold 扩展为可配置速度—质量曲线”，也支持跨 block 修正会
  引入额外 forward work。它不证明 dLLM 已普遍优于 AR、公开 TPS 可复现、或同一 thresholds
  适合所有 domain。
- **Limitations / Trade-offs / New Failure Modes:** 作者明确把模型标为 experimental；激进降低
  `τ_mask` 会产生 rough draft、n-gram repetition 与结构错误，阈值需按 domain 调整。编辑扩大
  mutable state、rollback/streaming 语义和 cache invalidation；MBE 的质量收益又会降低并行进度。
  传统 AR 在严格增量 streaming、简单 KV append 与成熟 serving contract 下仍更合理；单调 dLLM
  在不需要 retroactive correction 的受控任务中也更简单。
- **Evolution Relationship:** `Direct Evolution`：absorbing-state mask filling → confidence threshold
  decoding → same-block T2T correction → cross-block editing。后者没有否定旧方案，而是用可变状态
  与额外训练/执行成本换取更激进的并行草拟。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 候选为 Ch40，handoff 到 Ch20、Ch38、
  Ch39；已读这些章节及 Ch41/44 的相邻边界。现有正文完整解释 AR append-only Decode 与
  speculative rollback，却没有“已生成 token 可由同一 target state evolution 重写”的机制。
- **Integration Decision:** `Books Candidate — Integrate New Mechanism / Human Gate Pending`；本轮
  不修改 Books，待 W07 Evidence Gate 与人工 Review 后决定是否以 experimental branch 写入 Ch40。
- **Open Questions:** editable block 与 streamed output 的 commit boundary 怎样定义？跨 block
  correction 如何与 KV/radix cache identity、batch fairness 和 request cancellation 一致？

### Prism: Spectral-Aware Block-Sparse Attention

- **Candidate / Week / Score:** Prism / 2026-W07 / 27/30；
  `Source Family ID: rope-spectral-block-selection`。
- **Source Type / Dates / Revision:** arXiv paper；v1 2026-02-09，v2 2026-05-25。事件归 W07；
  v2/ICML 2026 revision 只用于机制与实验核验，不新增历史事件。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.08426 v2；已覆盖 Related Work、RoPE
  spectral derivation、dual-band estimator、temperature calibration、Triton-style implementation、
  language/video experiments、efficiency、ablation 与 Appendix。论文没有独立 Limitations 章节，
  因此威胁项由实验 contract 与未覆盖范围显式推导。
- **Original Problem / Previous Design:** dynamic block-sparse Attention 需要先估计哪些 Q/K blocks
  值得精算。mean pooling 便宜且对连续 block/GPU tile 友好，所以是合理旧方案；但加入 RoPE 后，
  block 内不同相位在高频 dimensions 发生 destructive interference，pooled vector 像 low-pass
  filter，可能抹掉局部 positional/slash pattern。token-level search 能补回信息，却可能让 selector
  overhead 吞掉 sparse compute 收益。
- **Changed Constraint / Mechanism:** Prism 把 RoPE dimensions 切成 high/low-frequency branches，
  分别 mean-pool Q/K、计算 block scores，再用各 branch 的 RMS energy 推导 temperature calibration，
  以 Top-P mask 的 union 选择 blocks。它保留 block-only matrix operations，不要求重新训练模型。
- **State Ownership / Data Flow:** selector 从当前 Q/K block representations 和 RoPE frequency layout
  产生 mask；selected block pairs 再进入 sparse attention kernel。selection state 属于本次 Prefill，
  不能脱离 model/RoPE/base、block size、head dimension 与 threshold 复用。
- **Implementation / Evaluation Contract:** 论文用 block size 128、`d_high=64`、`d_low=96`，比较
  FlashAttention-2、MInference、FlexPrefill、XAttention、PBS-Attn；覆盖 Llama-3.1-8B-Instruct、
  YaRN-extended Qwen3-8B、Qwen3-VL 与 HunyuanVideo。Prefill latency 的 5.1× 上限绑定单张 H100、
  Llama-3.1-8B-Instruct、128K sequence 与 FA2 baseline；不是 Decode、end-to-end service 或任意
  GPU 的 speedup。ablation 支持 spectral overlap 与 energy calibration 对 density/perplexity 曲线
  有作用。
- **What the Evidence Proves / Does Not Prove:** 理论和 ablation 支持“RoPE frequency 与 pooling
  不是正交实现细节”，并证明在作者覆盖的模型/任务/threshold 下 pure block-level estimation 可
  保持接近 dense accuracy。它不证明 Top-P/频带切分对任意 head dimension、RoPE variant、finetune
  distribution 或 online Decode 都可靠。
- **Trade-offs / Failure Modes / Previous Design:** 双分支增加两套 score、energy calibration 与 union
  mask；错误的 frequency boundary、threshold 或 distribution shift 会造成 false-negative blocks，
  而更高 density 会侵蚀收益。短 context、dense semantic requirements 或 selector overhead 高于
  skipped work 时，FlashAttention-2 仍合理；token-level selector 在强 needle/query-at-end 结构下
  也可能更准确。
- **Evolution Relationship:** `Direct Evolution`：static pattern → input-dependent token-level
  selection → coarse block pooling → spectral-aware block-only selection。演进目标是同时降低 pair
  count 与 selection tax，而不是把 dense Attention 宣判过时。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch22 主 owner，Ch13、Ch14、Ch39、Ch45 为相邻
  边界；已读对应 RoPE、Attention semantics、long-context sparse evolution、Prefill 与 kernel
  mapping。Ch22 已覆盖“稀疏索引必须与训练和硬件共同设计”，但尚未解释 RoPE mean-pooling
  blind spot 及 selector 自身的 frequency contract。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；如通过
  Gate，应只补 selector 机制与适用边界，不复制 5.1× headline。
- **Open Questions:** frequency split 能否由 runtime/model metadata 自动验证？GQA/MQA、RoPE
  scaling、quantized Q/K 与 mixed head dimensions 会怎样改变 calibration？

### Step 3.5 Flash technical report

- **Candidate / Week / Score:** Step 3.5 Flash / 2026-W07 / 28/30；
  `Source Family ID: step35-flash-model-system`。
- **Source Type / Dates / Revision:** 官方技术报告；v1 2026-02-11、v2 2026-02-23。事件归 W07；
  当前 HTML v2 用于核验 revision 后机制，不把 2 月 23 日内容伪装成新的 W07 事件。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.10604；已覆盖 architecture、两组
  ablation、4096-GPU training infrastructure、stability monitoring、data/training stages、MIS-PO、
  reward design、agent data/evaluation、limitations 与相关 Appendix settings。
- **Original Problem / Previous Design:** full Attention、单 token prediction、标准 ZeRO gradient
  ownership 与普通 off-policy PPO 路径分别有清晰语义，且在规模较小、context/agent horizon 较短、
  training/rollout stack 接近时仍合理。196B total/11B active、128K～256K context、MoE 与长轨迹
  共同放大 attention cost、fabric contention、optimizer reshaping 和 training-inference probability
  drift，旧边界因此同时暴露。
- **Mechanism / State / Flow:** 模型使用 3:1 SWA/full hybrid、GQA、288 routed + 1 shared expert、
  top-8 与 MTP-3。大部分训练只优化 MTP-1，后期再初始化/联合训练 MTP-2/3。训练面把 DP traffic
  分成 NVLink/RoCE phases，并按 communication profile 放置 ranks；Muon ZeRO-1 将 whole expert
  parameters 分配给 owner rank，使 reduce-scatter 直接交付完整 gradient。RL 面的 MIS-PO 把
  inference policy 当 proposal、training policy 当 target，过滤偏离样本；truncated trajectory 用
  value bootstrap 区分“未完成”与“失败”。
- **Implementation / Hardware Contract:** 4096 张 H800，8 GPU/node、NVLink/NVSwitch、节点间
  8×200Gbps RoCE；内部 Steptron 基于 PyTorch/Megatron。fabric scheduling 与 rank placement 在
  作者 workload 中合计最多降低约 5% iteration time；这是 topology/profile-specific 结果。Muon
  方案只对 expert parameters 使用 owner-oriented reduce-scatter，non-expert 仍 all-reduce，说明
  whole-parameter ownership 不是全局替代 ZeRO sharding。
- **Evaluation Contract:** architecture ablation 包含 30B-A3B、1.4T-token pretraining、32K extension
  与 64K SFT，并另做 100B-scale study。`S1F1` 的 LongCtx/平均质量最高但 attention FLOPs 约比
  `S3F1+Head` 高 60%，因此作者选择后者作为 agent workload 的成本—质量折中。最终模型评估
  绑定 256K max length、特定 sampling、不同 benchmark 的不同 generation counts、tool harness、
  context manager 和最长 6h timeout；部分 closed-model scores 来自非官方来源。
- **What the Evidence Proves / Does Not Prove:** 报告证明该系统的多个 co-design choice 在作者
  ablation/规模下有效，也说明最优 quality layout 未必是最优 service layout。它不证明 3:1 hybrid、
  MIS filtering、Muon ownership 或 vendor benchmark 排名可跨模型/集群复用；final leaderboard
  也混合 model、harness、budget 与 context-management 能力。
- **Limitations / New Failure Modes:** 作者承认相近质量需要比 Gemini 3 Pro 更长生成轨迹，且
  open-world professional agent RL 尚未解决。新增风险包括 SWA/full 双重 state、MTP artifact/runtime
  compatibility、dead experts、reduced-precision Muon numerical blow-up、rank-placement drift、过滤
  过严导致样本利用下降，以及 value bootstrap 的 critic bias。
- **Evolution Relationship:** `Layering / Dependency`，不是单一路线：dense→hybrid attention；
  external drafter→model-native multi-head MTP；uniform collective→fabric/profile-aware scheduling；
  naive full-gradient reconstruction→parameter-owner reduce-scatter；ordinary off-policy update→
  distribution-aware sample filtering。每条旧分支在更简单 workload 上继续成立。
- **ROADMAP / Chapters Read / Existing Coverage:** 主要 owner 候选分别为 Ch22（hybrid attention）、
  Ch29（rollout/update drift）、Ch32/36（communication/ownership），Ch44 只做 MTP handoff；已读
  Ch21–22、Ch28–30、Ch32、Ch44–45 的相关与相邻段落。Ch44 已覆盖 MTP artifact evolution，
  不应重复；Ch22 尚缺“质量最优 layout 与 serving-cost 最优 layout 不同”的实证链，Ch29/32
  对 proposal/target drift 与 owner-oriented reduce-scatter 仍有可 refine 空间。
- **Integration Decision:** `Books Candidate — Refine Existing Arguments / Human Gate Pending`；若通过
  Gate，应拆给明确 owner，以短 handoff 连接，不能把整份 model report 堆进一个章节。
- **Open Questions:** MIS acceptance 的阈值/有效样本量与 bias 如何报告？fabric-aware rank placement
  在故障、elastic restart 与 background traffic 下怎样重新验证？

### FeatureBench: Benchmarking Agentic Coding for Complex Feature Development

- **Candidate / Week / Score:** FeatureBench / 2026-W07 / 27/30；
  `Source Family ID: feature-level-executable-agent-evaluation`。
- **Source Type / Dates / Revision:** arXiv v1，2026-02-11；ICLR 2026 accepted。无后续 arXiv revision。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.10975 HTML；已覆盖 task construction、
  F2P/P2P protocol、dependency tracing、post-verification、metrics、baselines、manual-verification/
  step/interface ablations、failure analysis、anti-cheating 与 dataset/experimental Appendix。
- **Original Problem / Previous Design:** issue/PR-level bug fixing benchmark 易于获得真实任务和 tests，
  所以对局部修复是合理 contract；但它不能代表跨 commits/PRs、跨文件、从缺失 feature 到完整实现
  的工作。只看最终 pass/fail 又会丢失 partial progress 和资源成本。
- **Changed Constraint / Mechanism:** pipeline 从 pytest candidates 构造 F2P 与 P2P tests，运行 dynamic
  trace 得到 object dependency graph，再切除目标 feature、验证其他能力仍工作、重放 gold patch，
  最终生成 interface/problem statement。第一版从 3825 个 executable environments 筛出 24 个
  Python repositories 的 200 tasks；每个任务同时绑定 undeveloped codebase、patch、tests、Docker
  image 与 base commit。
- **State Ownership / Data and Control Flow:** benchmark builder 拥有 task derivation/provenance；agent
  只修改 sandboxed checkout；executor/tests 拥有 outcome。`Resolved` 要求全部 F2P/P2P 通过，
  `Passed` 保存部分 F2P progress，Token I/O 记录 compute proxy。agent 自述不能覆盖 executable
  state。
- **Evaluation Contract:** 默认 OpenHands 最多 500 steps、允许 internet、无专用 browser tool，并有
  anti-cheating；七组 model+scaffold 设置说明评估对象是组合系统。作者还分别消融 manual prompt
  verification、50/100/500 steps、隐藏 interface 与公开 unit tests；后两项大幅改变结果，证明
  harness、information surface 与 budget 是 subject identity 的一部分。
- **What the Evidence Proves / Does Not Prove:** 证据支持 feature-level executable tasks 比当前
  SWE-bench-style bug fixing 暴露更多跨文件 dependency、planning 与长程执行边界。它不证明
  “真实软件开发”已被完整代表，也不能把低 resolved rate归因于 model 单体；repository selection、
  Python/pytest、OpenHands、network access、token budget 和 generated statements 都是条件。
- **Limitations / Threats / Failure Modes:** 仅 24 个开源 Python repos；tasks 是从已有 tests/code
  反向抽取而非真实新需求；安装命令仍需人工；F2P 常设一个 test file，test coverage 决定 verifier
  上限；LLM-generated docstring/problem statement 可能泄露或歪曲 intent；未来 agent 参与过仓库会
  增加 contamination。作者的 NameError/TypeError 分析来自特定 model run，只能形成 failure
  hypothesis，不能外推所有 coding agents。
- **Evolution Relationship:** `Direct Evolution`：single-PR bug repair → executable feature reconstruction
  → dependency-aware multi-file task → dynamically refreshable environment suite。旧 benchmark 在快速、
  稳定的回归和局部修复评估中仍有价值；新方案以更高环境构造和运行成本换更宽 outcome contract。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch62 主 owner，Ch63 与 Ch77 为 handoff；已读
  Evaluation 的 subject/distribution/executable evidence/dataset/governance、Monitoring 的观测边界，
  以及 Workflow testing。Ch62 已有 `artifact + environment + execution trace`，但没有把 F2P/P2P、
  partial-vs-resolved、step/interface visibility 与 task extraction provenance 组织成一条 feature-level
  evaluation evolution。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；若通过
  Gate，只沉淀 evaluation contract，不复制模型排名。
- **Open Questions:** test-derived task 对未编码 requirements 的 coverage 怎样量化？动态刷新如何
  保持跨版本难度可比、同时降低 contamination？

### Weak-Driven Learning: How Weak Agents Make Strong Agents Stronger

- **Candidate / Week / Score:** Weak-Driven Learning / 2026-W07 / 23/30；
  `Source Family ID: weak-checkpoint-corrective-post-training`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 2026-02-09、v2 2026-06-08。事件只归
  W07；v2 仅用于识别 revision，不把 6 月新增机制倒写成 2 月事实。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.08222；已读 v1 的 Introduction、Related
  Work、entropy-based data activation、mixed-logit objective、theory、math/code experiments、
  ablation、sensitivity、training cost、data/training Appendix，并对照 v2 的方法与限制变化。
- **Original Problem / Previous Design:** SFT 持续提高 target token 概率，在高置信区域会让 hard
  negative 的概率和梯度同时变小。继续只拟合 ground truth 在模型仍明显欠拟合时合理，也不需要
  保存额外 checkpoint；但在作者定义的 saturation 区域，它无法显式重放历史模型曾暴露的
  plausible errors。
- **Changed Constraint / Mechanism:** v1 先以历史 weak checkpoint 的 entropy 与 strong–weak
  entropy change 选择困难、需巩固或发生回退的样本，再混合两者 logits，以 ground-truth CE 为
  anchor。较弱分支给已被 strong branch 压低的 distractor 重新分配概率，从而放大对应 token 的
  corrective gradient；它不是让 strong model 模仿 weak output。
- **State Ownership / Revision Boundary:** v1 的算法把前一 checkpoint 作为 weak forward reference，
  更新当前 `M_theta`，但部分正文又称 weak agent “co-trained”，内部表述并不完全一致。v2 则明确
  把 weak/strong 两个 branch 都纳入 paired update，并增加 frozen-weak 对照。由于“weak state 是否
  随当前 step 更新”会改变 optimizer state、compute 与因果解释，本周不能把 v2 的共同优化机制
  当作 v1 已证明的事实。
- **Evaluation Contract:** v1 主要覆盖 Qwen3-4B/8B、Qwen2.5-3B 的 math/code，以及相应 ablation；
  v2 扩展 Gemma 与 logic，并补充更完整 cost/sensitivity。公开训练设置包含 full-parameter SFT、
  sequence length 4096、global batch 512；作者没有披露硬件与并发/SLO。v2 的 Qwen3-4B wall-clock
  表显示额外 weak forward 带来训练成本，但不能跨硬件外推。
- **What the Evidence Proves / Does Not Prove:** 论文支持“历史 checkpoint 的差异可成为受
  ground-truth 约束的 corrective signal”，并显示收益依赖 weak/strong 仍有有用差异。它不证明
  任意更弱模型都能帮助、entropy 一定区分可学习难例与噪声、或 paired update 普遍优于标准 SFT；
  v1/v2 的状态更新差异也尚需作者代码与可复现实验闭环。
- **Trade-offs / New Failure Modes / Previous Design:** 需要额外 checkpoint、双 forward、logit
  alignment 与样本统计；weak model 的系统性错误可能被重新放大，两个 branch 过近则信号消失，
  curriculum 还可能过拟合 entropy proxy。单一 SFT 在 compute 紧张、数据仍未充分拟合或旧
  checkpoint 不可信时仍是更安全分支。
- **Evolution Relationship:** `Direct Evolution`：target-only SFT → hard-example/curriculum replay →
  frozen historical-logit correction → jointly evolving weak/strong pair。后两步存在 material revision，
  不能压成一条已经稳定的统一机制。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch25 主 owner 候选，Ch23、Ch28～30 为边界；
  已读数据、SFT、PPO/GRPO/DPO 的目标与相邻章节。Ch25 已覆盖 distillation、forgetting 与 SFT
  saturation 的一般边界，但没有“weak checkpoint 作为非模仿式 corrective gradient”的机制；
  同时当前证据版本边界不足以直接写入正文。
- **Integration Decision:** `Emerging / Experimental — Material Revision Boundary`；Evidence Gate 后
  仍应先对照 v1/v2 code path，再决定是否以受限案例 refine Ch25。
- **Open Questions:** v1 实际训练中 weak branch 是否更新？双分支 optimizer/parameter ownership
  如何实现？entropy activation 在 mislabeled/noisy data 上是否会系统性放大错误？

### Improving Data and Reward Design for Scientific Reasoning

- **Candidate / Week / Score:** Dr. SCI / 2026-W07 / 23/30；
  `Source Family ID: scientific-reasoning-data-curriculum-rubric-reward`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 2026-02-09、v2 2026-02-10，均属于
  W07；全文按 v2 核验。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.08321；已读 dataset construction/
  statistics、difficulty/rubric annotation、EESFT、dynamic curriculum、SciRubric reward、evaluation、
  ablations、hyperparameters、judge prompts/examples、impact/limitations 与 Appendix。
- **Original Problem / Previous Design:** 数学/代码的 exact answer 或 tests 让 RLVR reward 较稳定；
  对开放科学问答，reference wording 不唯一、自动匹配脆弱。只保留可规则验证问题虽然可靠，却会
  把训练分布收窄到 multiple-choice 或 short-answer form。
- **Changed Constraint / Mechanism:** 数据管线把 1,006,701 道八类 STEM 问题分成 461K
  verifiable 与 545K open-ended，并生成 difficulty 与细粒度 rubric。EESFT 以增量 4-gram coverage
  选择结构/措辞更丰富的 demonstrations；RL curriculum 根据当前 policy 在多次 rollout 中的
  解题成功情况逐步替换已掌握样本；open-ended reward 分别验证 rubric items 与 final answer，再按
  Essential/Important/Optional/Pitfall 权重聚合，防止“过程看似覆盖要点”抵消错误结论。
- **State Ownership / Data and Control Flow:** dataset pipeline 拥有 source、split、difficulty 与 rubric；
  policy rollout 只提供当前能力观测；curriculum controller 决定下一轮 sample distribution；judge/
  verifier 产生 rubric/final-answer labels；trainer 消费聚合 reward。若不版本化这四类 state，模型
  改进与 curriculum/judge drift 无法区分。
- **Implementation / Evaluation Contract:** 4B Qwen3 backbone，SFT batch 1024、8K/16K context；
  GRPO train batch 1024、每 prompt 8 rollouts、14,336 max response、PPO batch 512。主评估覆盖
  GPQA-Diamond、SuperGPQA、GPQA-General、HLE、MMLU-Pro；实验对 EESFT、dynamic curriculum 与
  reward components 分别消融。硬件、并发与完整训练 wall-clock 未披露，厂商/closed-model 比较
  也不能视为等价 inference budget。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持“数据覆盖、当前难度与 verifier
  granularity 是同一 post-training control loop 的三部分”，并表明 rubric reward 在该数据/模型下
  比单一 generative judge 更稳定。它不证明 4-gram novelty 等于 reasoning diversity、LLM rubric
  judge 已成为 ground truth、或科学事实性与安全问题已解决。
- **Limitations / Trade-offs / Failure Modes:** 自动 difficulty 会随 policy/revision 漂移；rubric
  生成和判断可能共享偏差；固定权重把多维 correctness 压成 scalar；开放题的 final-answer parser
  仍可能错判。扩大训练覆盖换来 dataset lineage、judge calibration、reward cost 与高风险科学建议
  的人工监督成本。纯 rule-verifiable RL 在 objective 可形式化时仍更简单可靠。
- **Evolution Relationship:** `Layering / Dependency`：static mixed-quality corpus → diversity-aware SFT
  selection → policy-relative difficulty curriculum → rule + rubric composite reward。它扩展可训练任务
  边界，没有否定 exact verifier。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch23、Ch27/29 为主 owner 候选，Ch25 与 Ch62
  为 handoff；已读相邻章节。现有 Ch23 讨论 distribution/lineage，Ch27/29 讨论 verifier 即
  specification，但尚未把“data coverage—current difficulty—reward granularity”写成闭环，也未明确
  rubric item 与 final answer 必须分权验证。
- **Integration Decision:** `Books Candidate — Refine Existing Arguments / Human Gate Pending`；只沉淀
  control-loop 与证据边界，不复制模型排名或把 4-gram heuristic 写成通用 recipe。
- **Open Questions:** rubric 由谁生成、由谁独立校准？difficulty 更新对 policy lag 有多敏感？同一
  judge 同时参与 annotation 与 reward 时怎样测 correlated error？

### Flexible Entropy Control in RLVR from a Gradient-Preserving Perspective

- **Candidate / Week / Score:** Flexible Entropy Control / 2026-W07 / 22/30；
  `Source Family ID: rlvr-dynamic-clipping-entropy-control`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 2026-02-10、v2 2026-05-08。事件归
  W07；v1 已包含核心 dynamic clipping、ID/DID/OD strategies 与主要实验，v2 的跨模型/非数学
  扩展只作为 later revision evidence。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.09782；已读 v1/v2 metadata、PPO/GRPO
  preliminary、entropy-gradient derivation、四类 ratio/token regions、dynamic thresholds、三种 phase
  strategy、main experiments、baselines、phase/schedule sensitivity、training/evaluation settings、
  compute、limitations/checklist 与 Appendix code examples。
- **Original Problem / Previous Design:** 固定 PPO/GRPO clipping 能限制一次 policy update，语义清晰、
  稳定且便于实现；但它没有把“哪些未裁剪 token 在推高或压低 entropy”作为控制目标。持续 RLVR
  可能过早 entropy collapse，也可能因一味提高 entropy 而延迟收敛。
- **Mechanism / State / Flow:** 作者先按 advantage sign、token probability 与 importance ratio 分出
  对 entropy growth/reduction 贡献不同的区域，再只修改 Gradient-Preserving Clipping 的上下阈值。
  controller 以训练 step 或 entropy band 选择 increase/decrease state，形成 increase→decrease、
  decrease→increase→decrease 或 oscillatory-decay schedule；policy entropy 与 average clipping ratio
  是 feedback，optimizer 仍使用受 clipping 约束的 policy gradient。
- **Evaluation Contract:** v1 在 DAPO-Math-17k 上训练 Qwen2.5-Math-7B 与 Qwen2.5-7B，400 steps、
  global batch 512、每 prompt 8 responses、最大 response 4096/8192；训练时间表绑定 8×H100。
  baselines 包括 GRPO、Clip-Higher/Lower、entropy regularization、Clip-Cov、GSPO、SAPO，并检查
  phase ratio 与替换 static thresholds。v2 才增加 Phi-4-14B 与 non-math evaluation，不能归为
  2 月首发证据。
- **What the Evidence Proves / Does Not Prove:** v1 证明在作者模型、数据和 schedule 下，clip
  region 的选择能方向性改变 entropy curve，动态 schedule 可得到不同探索—收敛 operating points。
  它不证明存在通用最优 entropy trajectory、entropy 与真实 reasoning diversity 等价，或任意
  RL objective/模型都能复用相同 thresholds。
- **Trade-offs / Failure Modes / Previous Design:** controller 新增 phase ratio、entropy band、threshold
  function 与监控状态；错误 schedule 会过度探索、提前收缩或对 proxy curve 过拟合。动态 clipping
  不增加独立 model state，但增加 objective complexity 和 tuning surface。训练短、policy 已校准或
  entropy collapse 不明显时，固定 clipping 仍是更可解释的旧方案。
- **Evolution Relationship:** `Direct Evolution`：fixed symmetric clipping → static entropy-biased clip
  regions → token/ratio-aware dynamic thresholds → feedback/phase-controlled entropy trajectory。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch28/29 主 owner；已读 PPO clipping、GRPO
  objective、diagnostics 与相邻 RLHF/DPO。现有章节把 entropy 当诊断，却尚未解释 clipping region
  如何成为可控 actuator，也没有区分“保护 trust region”与“设计探索轨迹”两种职责。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；应标为
  Experimental，并保留 v1/v2 与 workload contract。
- **Open Questions:** entropy band 是否能跨 tokenizer/model size 校准？reward sparsity、sequence
  length 与 group composition 如何改变 region attribution？controller 本身是否会出现 oscillation？

### SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning

- **Candidate / Week / Score:** SkillRL / 2026-W07 / 25/30；
  `Source Family ID: recursive-procedural-memory-skillbank`。
- **Source Type / Dates / Revision:** arXiv primary paper v1，2026-02-09；无后续 revision。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.08234；已读 trajectory distillation、
  hierarchical SkillBank、retrieval、recursive update algorithm、ALFWorld/WebShop/search evaluation、
  baselines、component ablations、prompt/context analysis、hyperparameters、compute 与 skill examples。
  论文没有独立 Limitations/Threats section，此缺口保留为证据边界。
- **Original Problem / Previous Design:** 保存 raw successful trajectories 实现简单、provenance 最强，
  在短任务和小经验集上仍合理；规模增长后，重复 observation/action 会占满 context，失败轨迹还会
  带入噪声而非可复用规则。
- **Mechanism / State / Flow:** teacher 分别把成功轨迹蒸馏为关键策略、把失败轨迹蒸馏为
  counterfactual lessons；SkillBank 分为 general 与 task-specific skills，retriever 为当前 task 选择
  top-k。cold-start SFT 后，policy 用检索 skills 进行 GRPO rollout；每隔固定 validation interval，
  controller 从低成功率失败轨迹提炼少量新 skills 并追加到外部 library。policy weights 与
  SkillBank 因而是两个共同演进、但由不同组件拥有的 state。
- **Evaluation Contract:** Qwen2.5-7B-Instruct；ALFWorld、WebShop 与七个 search-augmented QA
  benchmarks。SFT/RL、raw-memory/Mem0 与去除 hierarchy/cold-start/dynamic evolution 的 ablation
  分开报告；训练使用 8×H100 80GB，单实验约 30 小时，RL batch 64、top-k 6、最长 prompt 6000、
  response 1024。作者排名只属于对应 prompts、environment wrappers 与 budgets。
- **What the Evidence Proves / Does Not Prove:** 实验支持在两个 interactive environments 中，
  把 raw trajectories 压缩成分层 procedural hints 可降低 context tax，并且动态更新在作者设置下
  提供增益。它不证明 teacher 抽取的 skills 忠实、跨环境迁移、长期无污染，或 skill library 能
  自动成为 authoritative policy。
- **Trade-offs / New Failure Modes:** distillation 丢失细节并引入 teacher bias；append-only recursive
  update 会产生冲突、陈旧和重复 skills；低 success-rate trigger 可能把 environment bug 当策略
  缺口。论文未给 provenance、supersession、delete、rollback、multi-writer consistency 与 security
  contract，生产化仍需额外 memory governance。
- **Evolution Relationship:** `Direct Evolution`：raw episodic replay → success/failure procedural
  distillation → hierarchical retrieval → validation-triggered derived-memory update。人工确认 memory
  在高风险或不可自动验证任务中仍是必要旧分支。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch73 主 owner，Ch72、Ch74、Ch77 为边界；已读
  相邻章节。Ch73 现有“raw episodes → success/failure → distilled lessons → retrieval → new episodes →
  re-evaluation/consolidation”已完整覆盖本机制，并进一步补上 provenance、supersession、delete 与
  Workflow policy 边界；本论文没有形成新的长期框架缺口。
- **Integration Decision:** `No Change — Already Covered`；保留为 Ch73 现有论证的条件性实验证据，
  不为增加 diff 重复写入。
- **Open Questions:** SkillBank conflict/decay 怎样测量？teacher/extractor 变化后如何重建？validation
  failure 到 skill update 的因果归因能否排除 tool/environment drift？

### Agent World Model: Infinity Synthetic Environments for Agentic Reinforcement Learning

- **Candidate / Week / Score:** Agent World Model / 2026-W07 / 26/30；
  `Source Family ID: executable-synthetic-agent-environment-rl`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 2026-02-10、v3 2026-05-22。事件只归
  W07；核心 environment、history-aware training 与 v1 evaluation 按首版复核，v3 的新增 synthesizer/
  judge 对照只作为 revision evidence。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.10090；已读 v1 的 scenario/task/environment
  synthesis、database/API/verifier generation、reward、history-aware GRPO、three-benchmark evaluation、
  quality/diversity/scale/verification analysis、implementation、hyperparameters、impact/limitations 与
  code Appendix，并对照 v3 的 judge reliability 与 pipeline changes。
- **Original Problem / Previous Design:** 人工环境最接近业务语义但昂贵、覆盖窄；LLM simulator
  便于扩展，却让 state transition 与 reward 依赖同一概率模型。对只读对话或低风险原型，人工/
  simulated environment 仍合理；长程 tool RL 则需要可 reset、可并行且可验证的 authoritative state。
- **Mechanism / State / Flow:** pipeline 先生成 CRUD-oriented scenario 与 task，再合成 SQL schema/
  sample data、typed API code 和 task verifier，通过运行重试修复 shallow errors。每个 sandbox 的
  database 拥有事实状态，tool layer 执行 transition，verification code 读取 state diff，LLM judge
  在 code evidence 上处理语义边界。GRPO rollout 又把长 history 切成与 inference sliding window
  一致的 sub-trajectories，避免训练使用完整历史、部署却截断的 distribution mismatch。
- **Implementation / Evaluation Contract:** v1 合成 1000 environments、35,062 tools、10,000 tasks，
  实际只在其中 526 个训练 Qwen3 4B/8B/14B；评估为 verified tau2-bench、BFCLv3 与 MCP-Universe。
  GRPO batch 64、每 task 16 rollouts、每 step 1024 instances、96 optimization steps、32K context、
  max 20 turns、history window 3。训练硬件未披露；因此不能推导成本/throughput。v1 的 sampled
  environment audit 仍报告大量 environments 含 bugs，说明 executable 不等于 semantically correct。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持 database-backed executable state、
  code-augmented verification 与 train/serve history alignment 在其合成/benchmark contract 下优于
  对照。它不证明 1000 environments 等同真实世界覆盖、judge reward 无噪声、所有 APIs/side effects
  被正确模拟，或从 synthetic sandbox 到 production action 可直接迁移。
- **Limitations / Trade-offs / New Failure Modes:** fixed generation pipeline 限制自适应覆盖；trial-and-
  error correction 擅长 runtime error，不保证逻辑一致；10% stage error tolerance、buggy tools、judge
  flip 与 synthetic-to-real shift 会污染 reward。可执行环境以生成/测试成本、schema/version lineage、
  isolation 和 judge expense换取更稳定 state；人工 environment 仍适合高风险和需要真实语义的任务。
- **Evolution Relationship:** `Direct Evolution`：LLM-simulated transition → generated executable code →
  database-owned state → state-diff verifier + semantic judge → inference-aligned trajectory training。
  code-only verifier 与 LLM-only judge 不是被删除，而是在各自盲点上组合。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch29 与 Ch62 为主 owner 候选，Ch74/77 为 handoff；
  已读 GRPO rollout/reward、Evaluation subject/environment/scorer、Tool Calling 与 Workflow 相邻章节。
  Ch62 已规定 environment/verifier 必须版本化，Ch29 已规定 trajectory/policy identity；仍缺“合成
  environment 的 authoritative state”与“history manager 是训练 objective 一部分”的连接机制。
- **Integration Decision:** `Books Candidate — Refine Existing Arguments / Human Gate Pending`；若通过
  Gate，应分别给 Ch29/62 明确 owner，不把 1000 environments 或作者 benchmark 写成通用规模结论。
- **Open Questions:** environment bug 如何在 reward 前隔离？history window 变化如何重算 old logprobs/
  advantage？真实 API 的权限、延迟、非幂等副作用如何进入 synthetic-to-production transfer test？

### Dr. MAS: Multi-Agent Reinforcement Learning for Collaborative Reasoning

- **Candidate / Week / Score:** Dr. MAS / 2026-W07 / 26/30；
  `Source Family ID: multi-agent-role-conditioned-policy-optimization`。
- **Source Type / Dates / Revision:** arXiv primary paper v1，2026-02-09；复核时未发现同一事件窗口内
  revision。事件日期按 v1，不按 discovery page 日期。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.08847；已覆盖 formulation、global-vs-
  per-agent normalization derivation、orchestration/runtime、logical-agent mapping、two/three-agent
  experiments、component ablations、resource assignment、hyperparameters、cost assumptions、limitations
  与 Appendix。论文没有披露总 GPU 数，记录为 `Not Disclosed`。
- **Original Problem / Previous Design:** GRPO 在同一 prompt 下对一组 sampled trajectories 做全局
  reward normalization，单策略、同质 rollout 时简单且能降低 scale variance。多角色系统中，不同
  agent 只在特定 turns 行动；solver、verifier、searcher 的 reward-conditioned gradient distribution
  可以系统性不同，此时全局 mean/std 把 role mismatch 混进 optimization scale。
- **Changed Constraint / Mechanism:** trajectory 每一步额外携带 acting-agent identity `k_t`。作者把
  advantage normalization 改成按 agent role 分组：每个 role 使用自己的 reward mean/std，再把对应
  token gradient 路由回该 role 的 policy worker。理论二阶矩分解显示，全局 normalization 会保留由
  role mean/variance mismatch 产生的放大项；per-agent normalization 消除该项，但不解决跨 agent、
  跨 turn 的真实 credit assignment。
- **State Ownership / Control and Data Flow:** orchestrator 拥有 workflow 和 turn routing；logical-agent
  mapping 决定哪些 roles 共享或分离模型；SGLang actors 生成 trajectories；trainer 按 agent identity
  切分 token/reward statistics，并把 update 发给相应 worker group；Ray placement group 管理 physical
  resources。若 role identity、policy version、normalization population 不进入 trajectory identity，
  同一 reward 不能被正确重放。
- **Implementation / Evaluation Contract:** 两角色 math 设置使用 Qwen3-4B/8B、8 rollouts、train batch
  32、prompt/response 8192/4096、两轮交互和 binary reward；三角色 search 设置使用 Qwen2.5-7B、
  group 5、train/eval batch 128/256、prompt 4096、单 response 800、最多四轮。实验运行于 H100，数量
  未披露。heterogeneous placement 的 31.6% latency 与 41.8% cost 只是作者 workload 与 API/cloud
  price model 下的结果，不能外推为普遍集群收益。
- **What the Evidence Proves / Does Not Prove:** derivation 与 ablation 支持“role-conditioned reward
  statistics 会改变 gradient scale，normalization population 是 multi-agent RL objective 的一部分”。
  它不证明 per-agent normalization 解决 delayed/cross-agent credit、扩大 agent 数必然增益，或逻辑
  role 应总是对应独立模型和独立 GPU group。
- **Trade-offs / Failure Modes / Previous Design:** per-role statistics 降低 distribution mismatch，却在
  小样本或稀有 role 上增加 estimator variance；共享模型时不同 role update 仍会在参数空间干扰；
  独立模型则增加同步、放置与 checkpoint 成本。单 agent 或角色分布近似同质时，全局 normalization
  仍是更简单、样本更多的旧分支。
- **Evolution Relationship:** `Direct Evolution`：trajectory-global normalization → role identity enters
  the sample contract → per-agent normalization and update routing → heterogeneous role-to-resource mapping。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch29 为主 owner，Ch78 仅作 multi-agent state/traffic
  handoff；已读 Ch28～30、Ch77～78。Ch29 已说明 same-prompt normalization 与 rollout identity，却
  未把 acting role 明确纳入 normalization population；Ch78 已覆盖 responsibility、shared state 与
  communication tax，不应重复训练公式。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；候选内容
  是 normalization semantics 与 trajectory identity，不是框架 feature 或作者 latency 排名。
- **Open Questions:** role 样本不均衡时怎样做 shrinkage/robust statistics？共享 backbone 的 role-
  specific gradient conflict 如何观测？跨 agent delayed reward 需要怎样的 causal credit estimator？

### iGRPO: Self-Feedback Policy Optimization with Fixed Sampling Budget

- **Candidate / Week / Score:** iGRPO / 2026-W07 / 24/30；
  `Source Family ID: self-conditioned-best-draft-rlvr`。
- **Source Type / Date / Revision:** arXiv primary paper v1，2026-02-09；复核时无后续 revision。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.09000；已读 two-stage objective、sampling
  allocation、MATH/AceReason training、DAPO/GSPO wrapper、rule/judge reward、entropy/KL/completion-count
  ablations、resource appendix 与 examples。论文没有独立 Limitations/Threats section。
- **Original Problem / Previous Design:** 标准 GRPO 对同一原始 prompt 独立采样一组 completions；在
  可验证任务上能产生组内相对信号，且 rollout contract 简单。它没有让 policy 在同一 update 内读取
  自己较好的草稿，因此可能重复第一次尝试的结构错误。
- **Changed Constraint / Mechanism:** 固定总 completion 数 `N+G=G_GRPO`：第一阶段从旧 policy 采样
  `N` 个 drafts，并按 reward 选择最佳草稿；第二阶段把这个草稿追加到 prompt，再采样 `G` 个
  refinements，最终只对 refinement trajectories 做 PPO/GRPO-style update。argmax selection 与 draft
  generation 在本轮 update 中不可微且固定；随 policy 迭代，self-conditioned prompt distribution
  也随之变化。
- **State Ownership / Data and Control Flow:** rollout controller 拥有 draft set、reward、best-draft
  pointer 和 augmented prompt；old policy 产生两阶段 samples；verifier/judge 决定 selection 与 final
  reward；trainer 只消费 refinement logprobs/advantages。best draft 因而不是普通输入数据，而是由
  current policy、reward version 和 selection rule 联合产生的 transient training state。
- **Implementation / Evaluation Contract:** 7B 模型在 MATH 7,500 或 AceReason-Math 9,400 样本上
  训练一 epoch，LR 1e-6、主实验 KL=0、无 entropy regularization；每 prompt 总计 8 completions，
  max prompt/response 1024/4096，global batch 1024。AIME 平均 64 次、其他 benchmark 8 次。资源为
  2 nodes × 8 A100，一节点专用于 vLLM、一节点训练；2048 response cap 的资源附录报告约 13%
  额外 GPU-hours，说明相同 completion 数不等于相同 token/latency cost。
- **What the Evidence Proves / Does Not Prove:** 作者实验与 wrapper ablation 支持在该数学数据、7B
  模型和 reward contract 下，重新分配 rollout budget 让后续样本读取最佳草稿可以改善结果。它不
  证明 self-feedback 引入新外部信息、最佳草稿一定正确、固定 completion 数等价固定 compute，或
  对开放题/长上下文/高噪声 judge 同样成立。
- **Trade-offs / Failure Modes / Previous Design:** selection bias 与 reward error 会被直接写入第二阶段
  context；更长 prompt 增加 prefill/cache cost；两阶段串行产生 latency barrier；只训练 refinement
  可能弱化 first-pass 行为。独立单阶段 sampling 在低延迟、reward 噪声较大或草稿不可安全复用时
  仍更稳健。
- **Evolution Relationship:** `Direct Evolution`：independent group rollouts → reserve part of budget for
  draft search → condition remaining rollouts on selected draft → train only the refinement distribution。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch29 为主 owner；已读 Ch28～30。现有章节解释
  group-relative objective、rollout pipeline 和 policy identity，但没有把“组内 samples 的依赖拓扑”
  与“由 policy 生成的 prompt state”列为 training contract。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；应沉淀
  rollout topology、state identity 与 compute-accounting 边界，不复制 benchmark 排名。
- **Open Questions:** best-of-N 的 selection bias 如何进入 importance correction？reward/judge 版本变化
  后旧 draft 能否复用？比较方法应固定 completions、generated tokens、wall-clock 还是 GPU-hours？

### LycheeMemory: Adaptive Long-Context Reasoning with Compressed KV Memory

- **Candidate / Week / Score:** LycheeMemory / 2026-W07 / 24/30；
  `Source Family ID: gated-compressed-kv-long-context-memory`。
- **Source Type / Date / Revision:** arXiv primary paper v1，2026-02-09；事件按 v1。全文由官方 PDF
  核验，不以 discovery abstract 替代。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.08382；已覆盖 memory-token compressor、
  KV memory bank、Gate 与 dynamic working memory、three-stage training、data synthesis、RULER/
  zero-shot/LongBench evaluation、compression/gating ablations、latency/memory、failure analysis、
  hyperparameters 和 examples。
- **Original Problem / Previous Design:** full-context attention 保留原文和精确 provenance，在上下文
  可容纳且 latency 可接受时最可靠；text-RAG 降低 active context，但会重复 retrieval/serialization；
  纯 latent recurrent memory 更紧凑，却难以选择性定位细节。
- **Changed Constraint / Mechanism:** 文档按 chunk 处理，在 chunk 中插入 trainable memory tokens；
  compressor 将结果写成 KV-cache 形式的压缩 memory bank `Theta`。query/reasoning 期间 Gate 对各
  compressed blocks 预测相关性，只把被选 blocks 注入 frozen reasoner；reasoner 同时维护可更新的
  dynamic working memory。compressor 使用 frozen base + LoRA，decode 使用 frozen base，使压缩器
  学习与生成主干解耦。
- **State Ownership / Data and Control Flow:** source chunks 是 provenance root；compressor 版本与
  compression ratio 决定 derived KV identity；memory bank 存储 compressed blocks；Gate 拥有 query-
  conditioned selection；reasoner 拥有当前 working state。若不记录 source range、compressor/model
  version、position scheme、Gate decision 与 eviction policy，latent block 无法安全复用或撤销。
- **Training / Evaluation Contract:** Stage 1 用 reconstruction/continuation/QA 预训练 compressor；
  Stage 2 以 final exact-match reward 联合优化 compressor/reasoner；Stage 3 监督 Gate。Qwen2.5-3B/
  7B-Instruct，2×A100 80GB；compressor 随机 compression ratio 2/4/8/16，约 160M effective tokens、
  5000 steps；joint RL batch 128、group 12、约 150 steps/3 days。latency 在 2×A100、128 samples、
  8K～128K input、1024 generation、最大 non-OOM batch 下测量，不能跨硬件/runtime 外推。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持“压缩 KV bank + learned Gate + dynamic
  working memory”在该合成长文档与模型上形成可训练 operating point，并显示 Gate 可减少不相关
  memory I/O。它不证明 1.75M token 都能无损回忆、latent memory 具有文本级 provenance，或作者
  速度数字适用于其他 attention/runtime。
- **Limitations / Trade-offs / New Failure Modes:** 128 个错误样本中包含 compression hallucination、
  约 35% 的 unidirectional dependency mismatch 与 premature inference anchoring；single-pass chunk
  compression 看不到后续跨 chunk 依赖。即使 4× 压缩，1.75M context 的 KV storage 仍约 18.1GB。
  full context/RAG 在精确引用、高风险审计和频繁 corpus mutation 下仍是重要旧分支。
- **Evolution Relationship:** `Layering / Dependency`：full-context retention → text retrieval → latent
  chunk compression → query-gated compressed KV → dynamic reasoning memory。后者扩展 memory hierarchy，
  不是对原文层的替代。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch22 为主 owner，Ch71 只交接 Context assembly；
  已读 Ch21～23、Ch70～73。Ch22 已覆盖 RAG、compression、neural memory 与 context turnover，但尚未
  把 compressed KV bank 的 identity、Gate、working memory 与 provenance loss 连接成 state lifecycle。
- **Integration Decision:** `Books Candidate — New Mechanism / Human Gate Pending`；正文候选是多层
  memory state、ownership 与 failure semantics，不保留作者 leaderboard。
- **Open Questions:** compressor/model 升级后 latent blocks 怎样迁移或失效？Gate false-negative 的
  observability/SLO 如何定义？跨 chunk dependency 能否通过 second pass 修复而不恢复全量 attention？

### Chain of Mindset: Dynamic Reasoning-Mode Orchestration

- **Candidate / Week / Score:** Chain of Mindset / 2026-W07 / 22/30；
  `Source Family ID: training-free-reasoning-mode-orchestration`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 2026-02-10，v2 2026-03-18。W07 机制与
  结论按 v1 复核；v2 只能作为 later revision evidence。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.10063 v1；已覆盖 meta-agent routing、四种
  mode prompts、context gates、code execution/repair、six-domain evaluation、token accounting、component
  ablations、examples 和 Appendix。论文没有独立 Limitations/Threats section。
- **Original Problem / Previous Design:** 固定 chain-of-thought 对稳定单路径问题成本低；Tree-of-
  Thoughts 等统一搜索在高分支任务中有用，但若每道题都展开同一 topology，会为不需要搜索的任务
  支付 context 与 token tax。
- **Mechanism / State / Flow:** meta-agent 在 spatial、convergent、divergent、algorithmic 四种 prompt/
  tool modes 之间动态路由；每个 mode 保持隔离 context，input gate 只抽取必要历史/图像，output gate
  压缩为 insight 再返回主轨迹。algorithmic mode 最多做两轮 code repair；divergent mode 生成 2～5
  branches。它是 workflow-level orchestration，不是模型内部出现新的 reasoning module。
- **Evaluation Contract:** AIME25、Fermi、LiveCodeBench、GPQA、MathV、MAZE；Qwen3-VL-32B 运行在
  8×A100，另含 Gemini API。作者报告平均 token 28.4K、ToT 142.5K；不同 API latency、缓存、并发和
  价格未形成统一 contract。移除 context gate 使总体 token 增约 87%，但 Fermi 部分切片反而提升；
  移除 divergent mode 节省约 26% token，说明 mode value 明显依赖任务。
- **What the Evidence Proves / Does Not Prove:** ablation 支持“动态 topology 与 context gate 在作者
  benchmark mix 下能降低无效展开”。它不证明四种 modes 构成完备 taxonomy、meta-agent routing
  稳定、或 multi-path reasoning 普遍优于单路径。
- **Trade-offs / Previous Design:** mode selection 本身消耗 tokens 且会误路由；context compression
  可能删除后续需要的细节；隔离 contexts 降低污染，也增加 provenance/merge burden。低分支、
  latency-sensitive 或有确定算法的任务仍应直接使用单路径/固定 tool workflow。
- **Evolution / ROADMAP:** `Principle Reuse`；已读 Ch71、Ch75、Ch77～78。Ch71 已规定 context
  selection/compression，Ch75 已规定 plan/search budget，Ch78 已把 role/topology/communication tax
  与 Workflow owner 分开；论文没有形成新的长期框架缺口。
- **Integration Decision:** `No Change — Already Covered`；作为动态 routing 与 context-gate 的条件性
  实验证据保留在 Weekly，不重复写入三章。
- **Open Questions:** routing error 应怎样单独评估？mode context 的 provenance/merge conflict 如何
  审计？用 wall-clock、token、tool calls 还是成功率约束下的总成本选择 topology？

### GENIUS: Evaluating General Intelligence in Multimodal Generative Models

- **Candidate / Week / Score:** GENIUS / 2026-W07 / 23/30；
  `Source Family ID: multimodal-generative-constraint-evaluation`。
- **Source Type / Date / Revision:** arXiv primary paper v1，2026-02-11；无同周 revision。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.11144；已覆盖 benchmark construction、20
  subtasks/three dimensions、interleaved input protocol、hybrid metric、expert calibration、alternate judge、
  model evaluation、format ablation、Bagel-specific experiment、theoretical framing、examples 与 Appendix。
  论文没有独立 Limitations/Threats section。
- **Original Problem / Previous Design:** 单一 text QA 或 image similarity 易自动评分，但无法同时检查
  “从少量示例归纳临时规则、执行 ad-hoc constraints、把上下文知识落实到生成物”。只看美学或整体
  judge score 会隐藏规则违反。
- **Mechanism / Evaluation Contract:** 510 个 expert-curated samples 分为 implicit pattern induction 86、
  ad-hoc constraint execution 213、contextual knowledge adaptation 211，共 20 subtasks。输入交错文本/
  图像；score 分为 rule compliance、visual consistency、aesthetic quality。Gemini-3-Pro judge 以 0/1/2
  评分并独立运行三次；只从两个模型各抽 100 outputs、由五名专家校准，Pearson correlation 约
  0.963/0.966。Qwen2.5-VL-72B alternate judge 保持大部分 rank 但改变绝对分数。
- **State Ownership / Boundary:** benchmark 拥有 task/rule/reference、input serialization 与 slice；
  model runtime 生成 artifact；rule checker、visual judge、aesthetic judge 各自产生维度分数；aggregator
  才形成最终排名。Bagel-specific attention 调整是单模型 intervention，不是 benchmark 本身的通用
  mechanism。
- **What the Evidence Proves / Does Not Prove:** 数据支持模型对复杂、多模态临时约束的表现会随
  input format 与 scoring axis 改变，也支持单一总分会隐藏不同 failure modes。小规模、两模型的
  judge calibration 与 Pearson correlation 不证明 judge 独立、跨模型族无偏，或该 suite “纯粹量化
  general intelligence”。作者的 first/general-intelligence 定位保留为主张。
- **Trade-offs / Failure Modes / Previous Design:** richer tasks 增加覆盖但降低可重复性；LLM judge
  受模型、prompt 与运行随机性影响；interleaved/decoupled serialization 变化会改变被测系统本身；
  aesthetics 与 rule compliance 聚合会掩盖 operating point。规则可执行的窄任务仍应优先 deterministic
  verifier，开放视觉维度再使用校准 judge。
- **Evolution / ROADMAP:** `Layering / Dependency`；Ch62 为唯一 owner，已读 Ch61～64。Ch62 已要求
  固定 subject identity、input/environment、distribution、scorer calibration/disagreement 与多维结果，
  已完整覆盖 GENIUS 提供的长期评价原则。
- **Integration Decision:** `No Change — Already Covered`；保留为 input protocol 与 hybrid scorer 的
  具体案例，不复制 leaderboard，也不把单 suite 等同 general intelligence。
- **Open Questions:** judge calibration 是否覆盖 model family、language 与 art style slices？三维分数
  应如何报告 Pareto frontier 而非单一排名？input serialization 是否应成为 benchmark version identity？

### When to Memorize and When to Stop: Gated Recurrent Memory

- **Candidate / Week / Score:** GRU-Mem / 2026-W07 / 26/30；
  `Source Family ID: gated-textual-recurrent-memory-loop`。
- **Source Type / Date / Coverage:** arXiv primary paper v1，2026-02-11。官方 HTML 不可用，已阅读全文
  PDF：problem setup、MemAgent baseline、dual gates、reward/advantage、inference modes、QA/NIAH
  evaluation、gate/RL ablations、training details、limitations 与 Appendix。
- **Original Problem / Previous Design:** MemAgent 顺序读取 chunks 并每轮重写 textual memory，能把
  任意长输入转成 bounded working state，因此在证据密集、必须遍历全文时合理；但 evidence-sparse
  QA 中，无证据 chunk 也会造成 memory 膨胀，证据齐全后仍继续扫描又浪费计算。
- **Mechanism / State / Flow:** memory agent 对 `(question, chunk, previous memory)` 同时输出 candidate
  memory、binary update gate `U_t` 与 exit gate `E_t`；只有 `U_t=true` 才提交新 memory，`E_t=true`
  可提前交给 answer agent。训练把 trajectory outcome、是否正确更新、相对 last-evidence position 的
  exit penalty 和 format reward 组合，并将 trajectory-level 与 turn-level group advantages 加权；不同
  trajectories 可在不同 turns 退出，turn baseline 的 population 因而随时间变化。
- **Evaluation Contract / Boundary:** Qwen2.5-3B/7B-Instruct，沿用 MemAgent train/eval data；HotpotQA、
  SQuAD、single/multi-key/multi-query/multi-value NIAH，7K～896K context。论文报告的最高 400%
  acceleration 绑定逐 chunk 串行 workflow、任务证据位置和作者 inference setup；硬件、并发、batch、
  serving SLO 未披露。multi-value 任务可能必须读完整上下文，因此作者保留禁用 exit gate 的分支。
- **What the Evidence Proves / Does Not Prove:** 实验与 gate/RL ablations 支持“是否写入、何时停止”
  是 recurrent memory controller 的独立决策变量。它不证明 text memory 无损、early exit 对聚合/
  exhaustive tasks 安全，或该 reward 可泛化到非 QA。
- **Trade-offs / Failure Modes / Evolution:** `Direct Evolution`：unconditional chunk update → update gate
  → evidence-sufficiency exit gate → task-selectable full scan。新增 gate label/reward、parser、premature exit、
  stale memory 和变长 rollout population；作者也指出额外 rewards 降低训练稳定性并要求更小 off-policy
  degree、更久收敛。证据未知或必须 exhaustive coverage 时，旧 full scan 仍成立。
- **ROADMAP / Decision:** Ch22 主 owner，Ch71 只交接 runtime Context；已读相邻章节。Ch22 已有
  retrieval/compression/recurrent-state 分层，但缺少“write admission 与 termination 是两个 gate、且
  exhaustive task 必须保留 bypass”的机制。`Books Candidate — Refine Existing Argument / Human Gate
  Pending`。
- **Open Questions:** `last evidence` 在无标注真实任务中由谁判断？gate false-negative 如何审计？
  提前退出、memory commit、失败重试与 streaming output 的 transaction boundary 怎样定义？

### Data Repetition Beats Data Scaling in Long-CoT SFT

- **Candidate / Week / Score:** Data Repetition / 2026-W07 / 22/30；
  `Source Family ID: long-cot-sft-epoch-data-budget`。
- **Source Type / Date / Coverage:** arXiv primary paper v1，2026-02-11；已读 fixed-update grid、teacher/
  positive-negative data studies、memorization/termination/overfitting/forgetting probes、hyperparameters、
  complete result tables、related work 和 conclusion。机制解释由作者明确标为 open problem。
- **Original Problem / Previous Design:** 增加 unique demonstrations 在 IID/general coverage 假设下合理，
  也降低少量样本过拟合风险；但 long-CoT demonstrations 的生成、过滤成本高，而 pretrained model
  可能已经具有能力，只缺将长推理结构和 termination behavior稳定写入条件分布的重复 exposure。
- **Mechanism / State / Flow:** 论文不提出新 loss，而把 `unique samples` 与 `epochs` 作为独立 recipe
  变量，在相同 optimizer-update budget 下交换两者。每个配置从 base checkpoint 独立训练；train token
  accuracy 用作 saturation signal。观测上，更多 epochs 主要提升完整 reasoning 的 termination rate，
  接近 100% train-token memorization 后下游收益趋平或下降；这只是 correlation/heuristic，不是已证实
  因果机制。
- **Evaluation Contract:** Qwen3-4B/8B、OLMo3-7B base，Dolci-Think-SFT 与 Qwen3-distilled math data；
  200～51.2K nested samples、1～256 epochs、最多 51.2K updates，batch 1、BF16、8-bit Adam，单张
  H100 94GB、每配置最长 24h；AIME24/25 最多 16 generations、GPQA 4，max generation 30K。
  negative-trajectory 结果可能受问题难度和 latent structure影响，不能解释为“错误数据无害”。
- **What the Evidence Proves / Does Not Prove:** 在这些 4B～8B base models、reasoning datasets 与
  budget 下，single-pass-largest-data 不是支配策略，epoch/data ratio 会改变 termination 和下游表现。
  它不证明 128 epochs 是通用 recipe、memorization 导致 reasoning、validation loss 可以忽略，或
  结果适用于 instruction-tuned/更大模型和开放生成。
- **Trade-offs / Evolution:** `Principle Reuse`：maximize unique data → fixed-budget epoch/data grid →
  token-accuracy stopping signal。小数据重复降低 data acquisition cost，却放大 teacher bias、格式模式、
  contamination 与窄分布遗忘风险；更广 unique data 在 coverage/robustness 目标上仍是旧分支。
- **ROADMAP / Decision:** Ch25 主 owner；已读 Ch23～25。现有 Ch25 说明数据窄/训练过久会过拟合，
  尚未把 epochs、unique examples、token accuracy 与 termination 分开为可观测 recipe variables。
  `Books Candidate — Refine Existing Argument / Status: Experimental / Human Gate Pending`。
- **Open Questions:** 终止率提升是否只是 format imitation？固定 updates 但不同 sequence length 时是否
  真正等 compute？data diversity、teacher quality 与最佳 epoch/data ratio 如何共同预测？

### DataChef: Executable Data-Recipe Generation via RL

- **Candidate / Week / Score:** DataChef / 2026-W07 / 22/30；
  `Source Family ID: executable-data-recipe-policy-optimization`。
- **Source Type / Dates / Coverage:** arXiv primary paper v1 2026-02-11；v2 2026-03-06 只作 later revision
  evidence。本次按 v1 HTML 阅读 task/data pool、executable recipe、proxy verifier/GRPO、evaluation、
  verifier correlation、planner/coder/RL ablations、case code、experimental Appendix 与 limitations。
- **Original Problem / Previous Design:** 专家手工选择、混合、过滤与合成数据，成本高却能保留领域
  judgment；让 LLM 逐步生成过滤规则可提效，但静态 prompt 没有把“recipe 执行后的 dataset quality”
  反馈到整条 pipeline policy。
- **Mechanism / State / Flow:** policy 从 target benchmark、instruction 与 source pool 生成 natural-
  language plan + executable data-processing code；sandbox 执行 recipe 得到 dataset。Data Verifier 随机
  抽样 outputs，用 LLM judge 给 invalid/format-error/incorrect/task-mismatch/pass 分类，并对 empty/
  malformed execution 施加 penalty；GRPO 用这个 proxy reward 更新 recipe policy。25 seed tasks 扩成
  5K task instances，source pool 覆盖 19 domains、31 benchmarks、257 datasets。
- **Evaluation Contract:** DataChef-8B/32B；cold start 分别用 Qwen3-Next-80B-A3B 规划与 Kimi-K2
  coding；六个 held-out tasks。每个 recipe 的 DVS 与实际 downstream Qwen3-1.7B-Base（3 epochs、
  LR 2e-5、batch 64）分开报告，32 candidates 的 oracle 不是 normal serving result。Verifier 对每 task
  仅构造 8～12 datasets，平均 Pearson correlation 0.59，说明 proxy 只有中等相关而非 ground truth；
  训练硬件/总成本未披露。
- **What the Evidence Proves / Does Not Prove:** 证据支持 executable plan+code 与 outcome proxy 能把
  data-pipeline generation 变成 feedback loop，也显示只做 planner + external coder 与 end-to-end train
  是不同 objective。它不证明 judge reward 等价 downstream adaptation、oracle selection 可在线获得，
  或自动 recipe 比专家在所有领域更安全。
- **Trade-offs / Evolution:** `Direct Evolution`：manual recipe → LLM-generated step → executable full
  pipeline → sampled proxy verification → policy optimization。获得搜索/自动化，新增 arbitrary-code
  sandbox、dataset lineage、judge bias、proxy gaming、LLM generation cost 与 data license/privacy 风险；
  高风险/低数据领域仍需 expert approval 与真实 downstream evaluation。
- **ROADMAP / Decision:** Ch23 主 owner，Ch77 只交接可恢复 Workflow；已读 Ch23～25、Ch76～77。
  Ch23 已有 data distribution/lineage，但缺“recipe code 是训练 artifact，proxy verifier 与 downstream
  metric 不同权威层”的闭环。`Books Candidate — New Mechanism / Human Gate Pending`。
- **Open Questions:** recipe 的 source/license/delete lineage 怎样传播？proxy reward 被 exploit 时如何
  rollback？怎样用 multi-fidelity evaluation 在 judge sample 与完整 downstream train 之间分配预算？

### The Pensieve Paradigm / StateLM

- **Candidate / Week / Score:** StateLM / 2026-W07 / 27/30；
  `Source Family ID: model-operated-context-state-machine`。
- **Source Type / Date / Coverage:** arXiv primary paper v1，2026-02-12；已读 state/tool formulation、SFT
  trajectory filters/action balancing、RL snapshots/reward、training data、synthetic/long-doc/chat/research
  evaluation、tool-pattern/agentic-prompt/error analyses 与 Appendix。硬件和训练 wall-clock未披露。
- **Original Problem / Previous Design:** 外部 runtime 固定执行 retrieve→summarize→truncate，可预测、
  易治理，适合稳定 workload；但任务在检索、顺序扫描、note consolidation 和 termination 之间的需求
  会随证据动态变化，固定脚本要么漏信息，要么耗尽 Context。
- **Mechanism / State / Flow:** “Spellbook”把 analyze/check budget、build/search/read、note/update/read、
  deleteContext、finish 暴露为 typed actions。模型先评估输入，按需索引/读取，把证据写入 external
  notebook，再删除 raw chunk 与 note-construction messages，形成 search→read→note→delete loop。
  SFT 从 teacher trajectories 经过 outcome/process filtering 与 action balancing；RL 在每次 context-edit
  action 保存 state snapshot，并按 correctness、finish format、window/turn budget 计算 group reward。
- **Evaluation Contract:** Qwen3 4B/8B/14B；SFT 约 3.3K trajectories，过滤/拆成 35.7K samples；RL
  用 LongBench v2 的 488 train problems。评估含 synthetic needle、NovelQA、InfinityBench、
  LongMemEval、BrowseComp-Plus；baseline 的 context budget、search availability 与 truncation方式不完全
  相同，厂商级 accuracy 不应外推。prompt-only Qwen3 agentic 对照支持“tool exposure 不等于学会
  management”，但仍绑定作者 prompt/tool environment。
- **What the Evidence Proves / Does Not Prove:** 证据支持 Context management 可以成为显式 action
  policy，并在受控长文档任务中学习何时读取、压缩和删除。它不证明 model 应拥有 authorization/
  deletion truth、notes 忠实，或 self-management 比 deterministic runtime 对所有任务更可靠。
- **Trade-offs / Evolution:** `Layering / Dependency`：host-written fixed assembly → typed context tools →
  model-proposed state transitions → runtime-enforced budget/snapshot。新增 malformed calls、错误/过早删除、
  note drift、stub accumulation 和 long-horizon overflow；论文也观察 keyword search 对 implicit queries
  较弱。确定性 policy/原文 archive 仍必须保留为 authority 与 recovery layer。
- **ROADMAP / Decision:** Ch71 主 owner，Ch73 只处理 persisted notebook lifecycle；已读 Ch70～73。
  Ch71 已有 assembly/compression/identity，却缺“模型提议 Context transition、runtime 验证与保存
  before/after snapshot”的主动状态机。`Books Candidate — New Mechanism / Human Gate Pending`。
- **Open Questions:** deleteContext 是 prompt visibility 还是 durable deletion？notes 怎样保留 source
  range？模型、runtime 与 Memory service 对 transition 的 approval/rollback 分工是什么？

### Blockwise Advantage Estimation for Multi-Objective RLVR

- **Candidate / Week / Score:** BAE / 2026-W07 / 24/30；
  `Source Family ID: block-conditioned-multi-objective-advantage`。
- **Source Type / Date / Coverage:** arXiv primary paper v1，2026-02-10；已读 structured objective、block
  loss/baselines、Monte-Carlo comparison、math/confidence experiments、TTS、reward/group-size ablations、
  hyperparameters、limitations、algorithm 与 complete standard-error Appendix。硬件未披露。
- **Original Problem / Previous Design:** GRPO 把 completion scalar advantage 应用于全部 tokens，在单一
  final-answer objective 中简单；当输出含 solution、confidence、自我修正等显式 segments 时，把 accuracy
  与 calibration reward 先 scalarize 会让不同段互相错误 credit。learned value/nested rollouts可估计
  intermediate state，却增加模型和 rollout 成本。
- **Mechanism / State / Flow:** parser 将 completion 切为 blocks；每个 objective 产生自己的 reward，
  blockwise advantage 只作用于该 block tokens，并先按 block length 平均。第一 block 可共享 prompt-level
  group baseline；后续 block 起点已含不同 sampled prefix，作者用 prefix outcome（主实验 correct/
  incorrect）将 group 分层，以 stratum mean 近似 conditional value，不额外 rollout。
- **Evaluation Contract:** Qwen2.5-3B/7B Base/Instruct，MATH+DAPO 25K prompts，512/1024 steps，
  sequence 4096、batch 2048 completions、group 32（消融 64）、BF16、LR 1e-6、KL 0；MATH500、
  GSM8K、AIME23-25，accuracy + AUROC/ECE/Brier。TTS 用 16 samples、temperature 1、max 32K。
  OCB 与 RLCR 的优劣随 in/OOD metric 改变，不存在统一 winner。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持显式 segments 下，outcome-conditioned
  within-group baseline 能减少部分 reward interference，并保留 confidence-weighted TTS。它不证明
  OCB unbiased 于任意 outcome、block boundaries 可自动发现，或 calibration improvement必然提高
  final task utility。
- **Trade-offs / Evolution:** `Direct Evolution`：one completion/one scalar advantage → per-block rewards →
  prefix-conditioned baselines。获得 objective-local credit，新增 parser/boundary contract、稀有 stratum
  variance 与更多 metrics；group 64 改善部分 ECE 却减少 distinct prompts、伤害 accuracy/AUROC。边界
  模糊或单目标输出仍应使用旧 scalar path。
- **ROADMAP / Decision:** Ch29 主 owner；已读 Ch28～30。现有章节只说 process/step reward 能细化
  credit，尚未说明“later block 不再共享同一 starting state”，也没有给 outcome-stratified baseline 的
  适用/失败边界。`Books Candidate — Refine Existing Argument / Human Gate Pending`。
- **Open Questions:** fuzzy/tool-interleaved outputs 怎样稳定分段？稀有 outcomes 怎样做 shrinkage？
  segment parser/version 是否必须进入 trajectory identity 与 off-policy validity？

### CLI-Gym: Agentic Environment Inversion

- **Candidate / Week / Score:** CLI-Gym / 2026-W07 / 24/30；`Source Family ID: executable-
  environment-inversion-task-generation`。arXiv v1 2026-02-11；已读 state formalization、generation/
  filtering、training/evaluation、ablations、failure analysis 和 Appendix。
- **Problem / Previous Design:** PR/commit history 可反演 code bug，却不记录每台机器的 dependency/
  filesystem/runtime history；人工 Terminal tasks 语义强但难扩展。Dockerfile 只描述 build sequence，
  本身也没有真实故障历史。
- **Mechanism / State / Flow:** 从通过 tests 的 `(base image, Dockerfile, codebase)` gold state 出发，
  agent 通过可复现 Dockerfile commands 破坏环境；执行 F2P/P2P tests 验证 poor state，再用失败信息
  生成 issue。1,655 tasks/29 Python repos，生成花费约 2.3B tokens；417 成功修复轨迹过滤成 291，
  说明 executable generation 仍需要 shortcut/triviality quality gate。
- **Evaluation Boundary:** Qwen3-32B/235B-A22B 两阶段 SFT（48K SWE trajectories + 291 filtered CLI
  trajectories），OpenHands，Terminal-Bench 1.0/2.0，max context 128K。结果混合 model、agent scaffold、
  trajectory filtering 和 benchmark；作者也显示换 agent 会显著改分，不能归因模型单体。训练硬件未披露。
- **Trade-offs / Evolution:** `Direct Evolution`：human task → version-history inversion → executable
  environment inversion。获得可扩展故障状态，新增 sandbox supply-chain risk、test blind spot、synthetic
  fault realism、2.3B-token generation cost；训练后更长探索还增加 context overflow。真实 incident/
  human-authored tasks 仍是 external-validity 分支。
- **ROADMAP / Decision:** Ch62 主 owner、Ch77 handoff；现有章节已有 executable verifier identity，
  缺“从 gold state 反演出可恢复 task，且 generation verifier 与 repair verifier 必须分离”。
  `Books Candidate — Refine Existing Argument / Human Gate Pending`。
- **Open Questions:** destructive inversion 如何隔离？P2P tests 能否发现 collateral damage？synthetic fault
  distribution 与生产 incident 的距离怎样测？

### GoodVibe: Neuron-Selective Secure-Code Fine-Tuning

- **Candidate / Week / Score:** GoodVibe / 2026-W07 / 22/30；`Source Family ID: gradient-selected-
  secure-code-neuron-tuning`。arXiv v1 2026-02-11；已读 threat model、gradient attribution、clustering/
  row-selective tuning、six-model evaluation、utility/FLOPs、ablations 和 discussion；无独立 Limitations。
- **Mechanism / Contract:** 在 424 对 secure/insecure C++、Java snippets 上用 binary classification loss
  的 gradients 给 linear-layer rows 排序，把 top-k “security neurons”聚类并只训练对应 rows；Qwen3-
  0.6B judge 对 held-out generations 判 safe/unsafe。覆盖 CodeLlama/Llama/Qwen/Gemma 4B～14B，另测
  Go/Swift。训练硬件、真实 compiler/tests、CWE slice 与 judge calibration 未完整披露。
- **Evidence Boundary:** gradient importance 只证明这些 rows 对当前 classifier loss 敏感，不证明单元
  存储稳定“security concept”；同一小数据既用于定位又用于 fine-tuning，judge 只给 binary label。
  FLOPs 表甚至出现 LoRA 总 FLOPs 高于 full fine-tune 的特定实现结果，不能外推一般 PEFT 成本。
- **Trade-offs / Threat Model:** 只覆盖 benign/inadvertent insecure defaults，明确排除 jailbreak、恶意
  prompt 与 deliberate malicious code。row-selective update 降低 trainable state，却可能过拟合 dataset/
  language patterns、损伤未测能力；top-k/cluster size 的收益非单调。
- **ROADMAP / Decision:** Ch65 已规定 threat model、independent tests、defense-in-depth 与 deployment
  validation；当前证据不足以改变框架。`Emerging / Experimental — Weekly Only`，不写 Books。
- **Open Questions:** 用 static analyzers/compilers/CWE ground truth 校准后是否仍成立？跨 model revision
  neuron identity 是否稳定？binary safe rate 是否隐藏 functional regression？

### DeAction: Detecting and Correcting Off-Task Computer Actions

- **Candidate / Week / Score:** DeAction / 2026-W07 / 23/30；`Source Family ID: pre-execution-
  action-alignment-guardrail`。arXiv v1 2026-02-09；已读 taxonomy/dataset construction、human annotation、
  two-stage detection、iterative correction、offline/online evaluation、latency、failure cases 与 Appendix。
- **Problem / Mechanism:** trajectory-level safety verdict 来得太晚；每个 proposed GUI action 应在副作用
  前与 user goal、history、current observation 对齐。Fast Check 先批准明显 aligned actions；可疑项才进入
  systematic analysis，基于 narrative history summary 分类 malicious instruction following、harmful
  unintended、other irrelevant，并向 agent 返回 structured correction，循环修改而非只 block。
- **Evidence Contract:** MisActBench 用攻击轨迹 + 无攻击合成轨迹并 replay 保持 environment state 一致，
  human action-level labels；online 用 RedTeamCUA/OSWorld 与多个 CUAs。默认两阶段离线 latency 11.3s，
  online guardrail 平均约占每 step 7.2/28.1s；这是作者模型/API/workload 下的结果。不同类型 recall
  约 67.7%～89.9%，说明 guardrail 仍会漏判。
- **Trade-offs / Evolution:** `Layering / Dependency`：post-hoc trajectory review → pre-exec action check →
  risk-routed deep analysis → corrective loop。获得更小 blast radius，新增 per-step latency、summary loss、
  false positive retry loop 与同源-model correlated error；高风险动作仍需 deterministic policy/approval。
- **ROADMAP / Decision:** Ch67 主 owner，Ch77 交接 retry/idempotency；现有章节有 policy enforcement，
  缺“cheap allow-path + ambiguous deep-path + correction trace”及 action-level operating point。
  `Books Candidate — Refine Existing Argument / Human Gate Pending`。
- **Open Questions:** action consequence预测错误怎样处置？summary 由谁验证？repeated correction 如何避免
  side-effect duplication 和 liveness failure？

### Composition-RL: Composed Verifiable Prompt Curriculum

- **Candidate / Week / Score:** Composition-RL / 2026-W07 / 25/30；`Source Family ID: answer-linked-
  verifiable-prompt-composition`。arXiv v1 2026-02-12；已读 composition algorithm、SPC curriculum、
  math/physics experiments、candidate-set/reliability ablations、hyperparameters、prompts 与 Appendix；
  无独立 Limitations。
- **Mechanism:** 从两道已有 `(question, ground truth)` 抽取数值，把第一题答案命名为中间变量并嵌入
  第二题，形成仍可由原 ground truths 自动验证的复合 prompt；当 `solve_all` 饱和，SPC 提升组合
  深度，继续产生难度。它增加 dependency depth，不自动增加概念/领域覆盖。
- **Evaluation Contract:** MATH 约 12K、Physics 约 23K，batch 256、LR 1e-6、8 rollouts、temperature/
  top-p 1、max output 16K；主表跨 AIME/IMOBench/GPQA/MMLU-Pro。硬件未披露；合成题的语义自然度、
  leakage、verifier composition error 与人工质量样本限制了外推。
- **Trade-offs / Evolution:** `Direct Evolution`：fixed verifiable prompts → answer-linked composition →
  performance-triggered depth curriculum。缓解 all-correct groups，代价是更长 rollout、错误链传播、模板
  artifacts 和窄“可组合数值答案”边界；真实 hard data 与跨域 expert problems 仍不可替代。
- **ROADMAP / Decision:** Ch23 主 owner、Ch29 handoff。现有 Ch29 说明 curriculum 需避免 all-equal
  groups，尚缺“data generator 也必须保持 verifier closure 与 lineage”。`Books Candidate — Refine
  Existing Argument / Status: Experimental / Human Gate Pending`。
- **Open Questions:** composite prompt 的 semantic validity 谁验证？difficulty 应按 dependency depth、
  policy success 还是 rollout cost定义？错误 ground truth 会如何放大？

### Generalized On-Policy Distillation with Reward Extrapolation

- **Candidate / Week / Score:** G-OPD / 2026-W07 / 24/30；`Source Family ID: on-policy-dense-
  implicit-reward-distillation`。arXiv v1 2026-02-12；已读 derivation、lambda/reference choices、same-size/
  strong-to-weak/multi-teacher experiments、reward correction、ablations、proof Appendix 与 settings。
- **Mechanism:** standard OPD 在 student trajectories 上最小化对 teacher logits 的 KL，可重写为隐式
  token reward与 KL constraint 等权的 dense RL。G-OPD 用 `lambda` 分离 reward scale 与 regularization，
  并允许 reference policy变化；`lambda<1` interpolation，`lambda>1` extrapolation。strong-to-weak
  correction 用 teacher pre-RL/base log-ratio减少 student/teacher base mismatch，但需额外大模型 logprobs。
- **Evaluation Contract:** Qwen3-4B same-size math/code teachers，以及强到弱设置；AIME24/25、HMMT25、
  HumanEval+/MBPP+/LiveCodeBench。作者观察 `lambda=1.25` 常优、1.5 可能不稳并拉长 response；硬件、
  serving cost 未披露，不能把“surpass teacher”解释成新增超出 teacher/data 的真知识。
- **What It Proves / Risks:** 推导证明 OPD 与特定 dense KL-RL objective 的关系；实验支持 reward scale 是
  独立 operating point。它不证明 extrapolated log-ratio 无 bias；lambda 放大会 reward hacking、length
  bias 和 teacher/reference mismatch。standard OPD 在目标是忠实复制 teacher distribution 时仍合理。
- **ROADMAP / Decision:** Ch25 为 distillation owner、Ch29 交接 RL objective；现有章节缺 on-policy
  distillation 的 state/data flow 与 implicit reward/reward-scale 边界。`Books Candidate — New Mechanism /
  Human Gate Pending`。
- **Open Questions:** teacher/reference logits 的存储与版本 identity是什么？lambda 怎样按 domain校准？
  extrapolation 增益来自能力、长度还是 benchmark-specific search budget？

### Voxtral Realtime: Native Streaming ASR and Resumable Serving

- **Candidate / Week / Score:** Voxtral Realtime / 2026-W07 / 25/30；
  `Source Family ID: native-streaming-asr-resumable-serving`。arXiv v1 2026-02-11。
- **Full-read Coverage:** 已读 causal encoder、delay-conditioned decoder、training stages、vLLM serving、
  WER/latency-delay evaluation、conditioning ablation、长短音频与多语言 Appendix。论文没有公开
  production concurrency、server hardware、queueing 与 SLO，因此不能从 WER 表推出服务容量。
- **Original Problem / Previous Design:** offline ASR 先取得完整音频，再用 bidirectional encoder 和一次性
  request 解码，在录音文件或允许较高等待的任务中仍合理；实时转写的输入却持续到达，future frames
  不存在，传统“send complete input → decode”也无法维持低 target delay。
- **Changed Constraint / Mechanism:** causal convolution/attention encoder 每 20ms 产生表示，adapter 以
  `p=4` 降采样；decoder 每 80ms 选择发出 token 或 non-emitting placeholder。Ada RMSNorm 只在 FFN
  branch 注入 target delay，使同一模型覆盖 80ms 的整数倍 operating points；encoder/decoder 使用
  bounded sliding windows，避免 stream length 令 memory 无界增长。
- **State Ownership / Control and Data Flow:** runtime 同时拥有 50Hz encoder KV 与 12.5Hz decoder KV。
  自定义 metadata backend 把 encoder block/index/slot mapping 按 pooling factor 对齐到统一 paged
  allocation；每个 WebSocket session 保留 anchor request，新增 audio commit 恢复同一 request 并复用
  既有 KV。async input/output generators 支持边收边发，I/O buffering 与单-token decode 并行。
- **Evaluation Boundary:** 作者在 13 种语言、多套短/长音频 benchmark 和 240/480/960/2400ms delay
  上报告 WER，并比较 delay-conditioning 方案；不同 commercial realtime API 的 delay 定义不一致，
  论文也因此未给它们统一 delay。证据支持“质量—等待可由同一模型显式控制”，不证明所有语言、
  网络抖动、并发与 tail latency 下都达到同一 operating point。
- **Trade-offs / Failure Modes / Previous Design:** 更短 delay 缺少 future acoustic context；placeholder
  与错误 emission timing 会传播；session reconnect/cancel/retry 需要 KV 与 audio offset 一致；双速率
  cache、persistent connection 和 backpressure 增加状态与资源泄漏风险。完整离线编码在批处理、
  可重放音频和追求最低 WER 时仍是有效分支。
- **Evolution / ROADMAP:** `Layering / Dependency`：offline full-input request → causal chunked model →
  resumable request-owned KV → full-duplex stream。Ch41 为 serving-state 主 owner，Ch18 只交代 causal
  model contract，Ch77 交接 long-running external input；已读 Ch18、Ch41、Ch77 及相邻章节。
- **Integration Decision:** `Books Candidate — New Mechanism / Human Gate Pending`；候选长期观点是
  “request 不再等于封闭 prompt，增量输入使 KV、cursor、transport session 与 retry 成为同一状态机”。
- **Open Questions:** resume token 如何绑定 model/session/audio offset？断线重连、慢消费者、重复 commit
  与 worker migration 的 correctness/SLO 如何验证？

### Gaia2: Dynamic and Asynchronous Agent Evaluation

- **Candidate / Week / Score:** Gaia2 / 2026-W07 / 27/30；
  `Source Family ID: asynchronous-event-driven-agent-evaluation`。arXiv v1 2026-02-12，ICLR 2026。
- **Full-read Coverage:** 已读 ARE abstraction、Mobile universe generation、scenario taxonomy、ReAct/PTC
  scaffold、model experiments、time/A2A/noise analyses、judge/verifier contract、dependency-generation
  Appendix 与 limitations。`1,120` 是包含 augmentation 的总 scenarios；`800` 是五个 core splits 的
  unique human-authored scenarios，不再把两个数字当冲突版本。
- **Original Problem / Previous Design:** synchronous tool benchmark 只在 Agent action 后改变环境，容易
  固定起始状态、复现和评分，适合单轮工具正确性；但它无法测试 Agent 思考期间 deadline 经过、
  外部事件到达、通知噪声或其他 Agent 改写共享世界。
- **Changed Constraint / Mechanism:** ARE 把 environment 做成 independently advancing event runtime；
  model generation 本身消耗 simulated time，事件和工具结果通过同一 observation interface 进入 Agent。
  Mobile 在 10 个 universes 中提供 12 apps/101 tools，scenario 用 event DAG、initial state 与 verifiable
  end condition 绑定；A2A split 用按需 app-agents 替代直接工具访问。
- **State Ownership / Control and Data Flow:** environment clock、event queue、app state 与 notification
  policy 由 harness 拥有；Agent 只拥有 belief、actions 和 tool messages。Universe 生成用 dependency
  graph/priority 保持 contacts、mail、calendar 等一致，但论文明确承认 temporal consistency、跨 channel
  relationship 与 cross-modal reference 尚未完整处理。
- **Evaluation Boundary:** 默认 sequential ReAct 与 parallel tool calling ablation 显示 PTC 改善 wall-clock/
  tokens 而未改善 pass@1；Time split 出现“更多 reasoning time 反而错过 deadline”的 inverse scaling。
  这证明 benchmark 同时测 model、scaffold、inference latency 与 system reliability，不能把排名归因于
  单一模型能力；公开结果也没有形成跨 provider 的统一 hardware/network contract。
- **Trade-offs / Previous Design:** 现实感来自异步状态，却降低 deterministic replay，要求 event log、
  clock policy、notification visibility、timeout 与 stale-event semantics；synthetic universes 仍可能存在
  dependency artifacts。同步 benchmark 在隔离模型/工具逻辑和低成本 regression 时仍不可替代。
- **Evolution / ROADMAP:** `Direct Evolution`：static final-answer benchmark → trajectory/tool benchmark →
  event-driven world with external time → multi-actor shared state。Ch62 为 evidence-contract owner，Ch77
  交接 durable timers/external events；已读 Ch62、Ch77 及相邻章节。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；应补充
  “time/environment progression 是 evaluator-owned state，agent score 是 model×scaffold×runtime×world”。
- **Open Questions:** simulated time 与 provider latency 如何校准？event schedule 是否可 replay？跨 App
  consistency gap 会把多少 harness error 误判为 Agent failure？

### MiniCPM-SALA: Sparse/Linear Hybrid Attention and Staged Conversion

- **Candidate / Week / Score:** MiniCPM-SALA / 2026-W07 / 27/30；
  `Source Family ID: sparse-linear-hybrid-attention-conversion`。arXiv v1 2026-02-12。
- **Full-read Coverage:** 已读 architecture、HyPE/output gate、HALO conversion、five-stage training、
  general/long/ultra-long evaluation、A6000D/RTX 5090 latency-memory experiment、quantization 与 Appendix。
  论文没有独立 Limitations/Threats section。
- **Original Problem / Previous Design:** sparse softmax 减少 pair compute，但若仍存完整 KV 就不自动降低
  memory；linear attention 用固定递归状态降低长序列计算/存储，却可能损失精确 content addressing。
  从头训练 hybrid 最自由，但已有 dense checkpoint 与训练投资使全量重训不一定合理。
- **Changed Constraint / Mechanism:** 模型让大多数层转为 linear attention，并保留由 HALO layer-selection
  选出的 softmax layers，后者在长阶段启用 sparse attention；首尾层不转换以保持稳定。HyPE 在线性层
  保留 RoPE 以编码顺序、在 sparse 层移除 RoPE 以缓和远距衰减，两类 attention 后都加 output gate。
- **Training / State Flow:** conversion 只训练 linear parameters（1.3B tokens），随后先在 4K 上稳定/decay，
  再启用 sparse path 逐级扩到 32K/160K/520K，最后 64K/140K SFT；总转换训练约 2T tokens，不能
  把它描述为一次 weight surgery 或零成本复用。
- **Evaluation Boundary:** 作者在 A6000D 96GB 与 RTX 5090 32GB 上比较 Qwen3-8B，给出 64K～1M 的
  TTFT/E2E/OOM；还报告 RULER 等有效性。作者表格支持该模型/实现/硬件下的 memory operating point，
  不证明任意 hybrid 都有同一速度、2M context 等于真实任务可用，或不同 parameter count 的榜单可直接
  归因于 attention。
- **Trade-offs / Previous Design:** 双 attention path 需要不同 state/kernel/position contract；layer selection
  错误、linear compression 与 sparse miss 都会丢信息；长阶段训练和专用 kernel 抵消部分复用收益。
  dense full attention 在短 context、精确 retrieval 与无需迁移的模型上仍是最清晰基线。
- **Evolution / ROADMAP:** `Direct Evolution`：dense softmax → hybrid linear+softmax → selected sparse
  softmax layers → staged dense-to-hybrid migration。Ch22 已有路线但尚未明确“sparse compute 可能仍保留
  dense storage”与转换 curriculum；已读 Ch21～23、Ch38～45。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；不保留作者
  leaderboard，只补 compute/state 两轴和 migration cost。
- **Open Questions:** sparse layers 的 KV storage 是否随实现真正稀疏？HALO selection 对 model family
  与 downstream distribution 有多敏感？conversion 的 total FLOPs/energy 与 from-scratch 怎样公平比较？

### SPES: Sparse Expert Synchronization for Decentralized MoE Pretraining

- **Candidate / Week / Score:** SPES / 2026-W07 / 22/30；
  `Source Family ID: decentralized-moe-sparse-expert-synchronization`。arXiv v1 2026-02-12。
- **Full-read Coverage:** 已读 decentralized setup、update equations、expert-merging warm-up、convergence
  analysis、1B/2B/7B from-scratch 与 9B upcycling、memory/communication experiment、node/H/merge
  ablations、datasets、harness 与 Appendix。论文只给出较窄的 future-work limitation。
- **Original Problem / Previous Design:** centralized DP/FSDP 在高带宽集群同步完整状态，收敛语义清晰，
  在同机或稳定 fabric 上仍合理；弱连接节点若上传完整模型，会同时受到 per-device memory 与跨节点
  communication 限制。普通 local/decentralized training 仍让每个 node 持有完整模型。
- **Changed Constraint / Mechanism:** 每个 node 持有 shared modules 和唯一 expert subset，收到 global
  parameters 后做 `H` 次 local update；未分配 experts 在本 node 冻结。同步时 shared parameters 用
  FedAvg，owner-updated experts 直接拼接回 global model，再 broadcast。早期按 expert input projection
  cosine similarity 合并 Top-K peers，缓解 owner-only training 的 token utilization 缺口。
- **State Ownership / Control and Data Flow:** parameter server 拥有 global shared block 与 expert registry；
  node 是其 experts 的唯一 update owner，同时复制其他 frozen experts用于 routing/forward。shared block
  获得跨 node averaging，expert block 承担 owner data bias；theory 也将 heterogeneity bias 和 early
  merging perturbation显式列入边界。
- **Evaluation Boundary:** 7B 从头训练使用 4 nodes×8 A800/NVLink；2B memory case 扩到 16 个 48GB
  GPUs，另有 9B upcycling。作者报告每轮通信与 memory 下降、有限 benchmark 接近 centralized
  baseline；这不证明跨数据中心 WAN、node churn、non-IID data、安全对手或更大 MoE 下仍成立。
- **Trade-offs / Previous Design:** 未分配 expert 接收的 token 不更新，降低 token efficiency；更大 `H`
  减少通信但放大 stale shared state/owner drift；merge 会模糊 specialization，server 又形成 control-plane
  failure point。高速统一集群仍适合 centralized/sharded training。
- **Evolution / ROADMAP:** `Direct Evolution`：full-state synchronous DP → full-model local update + periodic
  averaging → MoE block ownership + sparse synchronization → early expert mixing。Ch32 为 communication/
  consistency owner，Ch21 交接 routing，Ch35/37 只解释 intra-node sharding；已读这些相邻章节。
- **Integration Decision:** `Emerging / Experimental — Books Candidate after stronger evidence`；机制有长期
  价值，但当前规模、failure model 与 heterogeneity evidence 不足，不应立即写成常规训练架构。
- **Open Questions:** expert owner failure 如何恢复？router 在 frozen experts 上产生的 tokens 怎样记账？
  non-IID data、secure aggregation、server checkpoint 与 topology-aware placement 如何进入 contract？

### INTENT: Budget-Constrained Planning for Costly Tool Use

- **Candidate / Week / Score:** INTENT / 2026-W07 / 23/30；
  `Source Family ID: risk-adjusted-budget-tool-oracle`。arXiv v1 2026-02-12。
- **Full-read Coverage:** 已读 constrained formulation、MCTS/MCO/INTENT algorithms、world-model
  factorization、oracle training data、StableToolBench evaluation、budget/market shifts、ablations、token/
  latency accounting、pseudocode 与 examples。论文没有独立 Limitations section，hardware 未披露。
- **Original Problem / Previous Design:** prompt 告知预算便宜但不提供 hard guarantee；立即价格检查能阻止
  单次超支，却看不到一串便宜调用累积后的失败；MCTS 可搜索 stochastic futures，但 free-form tool
  arguments 和强 Agent inference cost 使 exhaustive branching 过贵。
- **Changed Constraint / Mechanism:** MCO 用 language world model 做一条 stochastic lookahead；INTENT
  把 outcome 分解为“当前 reasoning intention 是否满足”的 probability 和 conditional result generator，
  然后在 `z=1` 的 ideal trajectory 上估计未来 action 序列。每步还要同时满足 immediate cost 与
  risk-adjusted predicted total cost；拒绝时把高风险 future actions 返回 Agent 触发 replanning，连续计划
  可复用 rollout cache。
- **State Ownership / Enforcement:** workflow/oracle 拥有 authoritative remaining budget、tool price snapshot、
  accepted/rejected action 与 cache identity；Agent 只提出 action/plan。learned probability/world model 是
  prediction state，不是账本。真正的 feasibility 来自 executor intercept；论文中的所有 `Enforce`
  variants 都达到预算可行，恰好说明 prompt awareness 不能替代 runtime gate。
- **Evaluation Boundary:** StableToolBench 加入 tool costs，比较 GPT-4.1-mini/GPT-5-nano，报告 pass rate、
  budget-optimal pass、feasible rate、cost、latency 与 token ratios，并测试 budget/price/service availability
  变化。证据只支持该 tool market、oracle models 和 judge labels；没有证明 LLM judge 的 intention label、
  ideal-success trajectory 或 price forecast 对开放环境校准良好。
- **Trade-offs / Previous Design:** pessimistic risk multiplier 提高预算安全但可能拒绝可行路径；`gamma<1`
  更激进却削弱 guarantee；stale rollout cache、world-model misspecification 和 market change 会误导规划。
  静态 quotas/knapsack 在工具集合小、成本稳定且任务结构已知时仍更简单可证。
- **Evolution / ROADMAP:** `Layering / Dependency`：prompt budget → immediate hard gate → static allocation/
  budget tracker → learned lookahead advisor + hard enforcement。Ch75 已写 constraint，Ch77 已写 deterministic
  budget owner，但尚缺 prediction state 与 authoritative ledger 的边界；已读 Ch75、Ch77 及相邻章节。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；长期结论是
  planner 可预测未来成本，但只有 Workflow/Executor 能强制预算。
- **Open Questions:** tool price/version 与 rollout cache 怎样失效？probability calibration 和 worst-case
  overspend 怎样验证？需要何种 fallback 才能在 oracle timeout 时保持 hard budget？

### Dreaming in Code: Closed-Loop Executable Curriculum Generation

- **Candidate / Week / Score:** Dreaming in Code / 2026-W07 / 24/30；
  `Source Family ID: executable-environment-closed-loop-curriculum`。arXiv:2602.08194 v1，2026-02-09；
  HF 发现日期不再用于归周。
- **Full-read Coverage:** 已读 UED/PLR background、archive/selection/generation、reward、Craftax experiment、
  open-loop ablation、infrastructure cost、prompts/code interface、hyperparameters、achievement/seed Appendix
  与 limitations。论文使用 Qwen3-235B-A22B-Thinking-2507-FP8 API 生成描述和 JAX code。
- **Original Problem / Previous Design:** domain randomization/PLR 在固定 parameterized level space 中高效且
  可控，适合已知变化轴；但 open-ended target 的瓶颈可能需要改变 objective、initial state 和 mechanics，
  固定参数空间无法组合新的中间训练世界。直接让 FM 随机生成世界又缺少 Agent learnability feedback。
- **Changed Constraint / Mechanism:** archive 是带 parent-child lineage 的 executable levels 图，节点保存 code、
  metadata 与 recent success profile。系统从已掌握/可学但子节点失败的 frontier 选 parent，FM 先根据
  parent 与 target capability gap 生成 level description，再生成兼容固定 engine 的 Python/JAX program，
  compilation check 后加入 curriculum；新世界、replay 与 target environment 共同训练 policy。
- **State Ownership / Control and Data Flow:** target engine/goal 定义 physical validity；archive 拥有 code、
  lineage、performance 与 sampling state；policy checkpoints/rollouts 更新 capability profile；FM 只是候选
  environment proposer。仅 compilation 通过不证明 reward、difficulty 或 semantic validity正确。
- **Evaluation Boundary:** 2B environment steps、5 seeds、1024 held-out worlds；与 PPO-GTrXL、DR、PLR、
  SFL 比较。open-loop ablation 移除 parent/performance feedback 后 final return 从 48.33 降到 40.91，
  接近 base RL，支持“closed-loop grounding 而非单纯生成 code”是关键。全部证据限于 Craftax/固定 engine；
  DiCode 约 48h，主要受 FM API latency，baseline 约 8.5～10.5h。
- **Trade-offs / Previous Design:** fixed engine 防止物理 hallucination，却限制新 laws/mechanics；FM latency、
  compile-only validation、reward loophole、archive explosion 与 curriculum overfitting 是新增风险。固定 UED/
  expert curriculum 在 simulator 小、约束清晰或高风险环境中仍更可控。
- **Evolution / ROADMAP:** `Direct Evolution`：fixed level distribution → prioritized replay → FM-generated
  executable levels → agent-performance-grounded curriculum graph。Ch29 为 training curriculum owner，Ch62
  交接 executable validity/evidence，Ch77 交接 archive workflow；已读目标及相邻章节。
- **Integration Decision:** `Emerging / Experimental — Books Candidate / Human Gate Pending`；应沉淀
  generator–compiler–evaluator–archive 闭环与 lineage，而不是“FM 自动发明世界”的宣传句。
- **Open Questions:** compile 后怎样做 semantic/property validation？错误 reward/engine exploit 如何隔离？
  archive pruning、level supersession、FM version change 与 cross-domain transfer 如何治理？

### ARO: Stabilizing and Accelerating LLM Training via Rotated Updates

- **Candidate / Week / Score:** ARO / 2026-W07 / 27/30；
  `Source Family ID: aro-rotated-optimizer-update`。
- **Source Type / Dates / Revision:** arXiv primary paper v1，2026-02-09；后续 revision 只用于核验，
  事件日期保持 v1。
- **Direct Primary Source / Full-read Coverage:** arXiv:2602.09006 HTML；已读 optimizer derivation、
  ARO-Sinkhorn、full-model variants、FSDP2/Megatron implementation、dense/MoE experiments、
  compute-matched curves、ablation、throughput 与 Appendix。论文没有独立 Limitations 章节，
  未覆盖边界由实验 contract 明示。
- **Original Problem / Previous Design:** AdamW 的 coordinate-wise moments 对异方差梯度、工程成熟度
  与大规模稳定训练很有价值；Muon 类 matrix-aware update 又把二维参数的结构放入 optimizer。
  但任意参数 basis 会改变逐坐标统计，更新方向未必保留 layer matrix 的谱结构；只对部分矩阵使用
  matrix optimizer，还会让 embedding、norm 与 output 等参数走不同更新规则。
- **Changed Constraint / Mechanism:** ARO 先为矩阵梯度求左右旋转基 `R`，在旋转坐标中应用 base
  update `f`，再旋回参数空间：`ΔW = -η R f(R^T G)`。ARO-Sinkhorn 用迭代归一化近似谱均衡，
  可作为 stateless base；full-model ARO 则把同一原则扩展到矩阵与非矩阵参数。核心变化是把
  rotation/conditioning 变成更新规则的一等对象，而不是把 optimizer 当作独立于参数几何的旋钮。
- **State Ownership / Control and Data Flow:** gradient shard 先属于各 data-parallel rank；实现按
  round-robin 选 owner，把同一参数的 shards gather 到 owner，计算 rotated update，再 scatter
  回原 ownership。Megatron prototype 在 TP group 内融合 gather，只在边界上做必要 DP gather。
  rotation work、owner mapping 与 optimizer state/version 必须和 parameter identity、checkpoint、
  mixed precision 保持一致。
- **Implementation / Evaluation Contract:** 实验使用 BF16 weights/activations 与 FP32 master weights，
  对齐 batch、context、tokens、schedule 和 optimizer steps；覆盖 2B Sigma MoE（A100、2K context、
  约 4M tokens/global batch、100B training tokens）与 8B Qwen3（B200/FSDP2、4K context、约
  14M tokens/global batch、46K steps、500M-token validation）。8B end-to-end throughput 在作者实现
  中约比 AdamW 低 3%；作者报告的 sample-efficiency speedup 只属于这些训练曲线与对齐条件。
- **What the Evidence Proves / Does Not Prove:** compute-matched long-horizon curves 支持“rotated
  matrix update 在给定模型/recipe 下可以用少量 runtime overhead 换取更快达到同一 validation
  loss”；早期约 3B tokens ARO 反而落后，说明收益不是 step-zero 普遍优势。证据不证明 ARO 对任意
  architecture、数据、规模或 schedule 都优于 AdamW/Muon，也不证明最终 downstream quality 必然更好。
- **Trade-offs / New Failure Modes / Previous Design:** 新增 matrix transformation、owner gather/scatter、
  numerical iteration、optimizer/checkpoint metadata 与 distributed skew；短训练、非矩阵参数占比高、
  通信敏感或已有成熟 AdamW recipe 时，旧方案仍更简单。Muon 在作者某个 full-model 设置中发散，
  只能视为该 recipe 的实验结果，不能外推成算法通则。
- **Evolution Relationship:** `Direct Evolution`：coordinate-wise adaptation → matrix-aware update →
  rotation-conditioned full-model update；`Layering / Dependency`：FSDP2/Megatron 只负责让该数学更新
  在分片状态上可执行，不定义 optimizer 本身。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch24 主 owner，Ch31/32/35/36 为 state、collective
  与 runtime handoff；已读这些章节与相邻边界。Ch24 已有 parameterization symmetry 与 optimizer
  basis-dependence 框架，但缺少“显式旋转更新 + 分片 owner 执行”这条机制案例。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；如通过
  W07 Gate，应在 Ch24 补机制，在 Ch32/35/36 只保留短 handoff，不复制 benchmark headline。
- **Open Questions:** rotation/owner metadata 怎样进入跨 world-size checkpoint？Sinkhorn iteration、
  small matrix fallback 与 network topology 的 break-even point 怎样自动选择？

### Beyond Correctness: Transfer Reward for Reasoning Training

- **Candidate / Week / Score:** Beyond Correctness / RLTR / 2026-W07 / 24/30；
  `Source Family ID: rltr-transfer-reward`。
- **Source Type / Date / Coverage:** arXiv:2602.08489 v1，2026-02-09；已读 reward formulation、receiver
  protocol、training algorithm、math/science experiments、receiver/compute ablation 与 Appendix。
- **Original Problem / Previous Design:** RLVR 以 final-answer verifier 给 reward，答案可精确核验、
  scorer 成本低，所以对数学/代码任务合理；但它只判断终点，不区分可被下一位 solver 接续的
  中间推理与偶然猜中答案的轨迹，也可能奖励不可读、不可复用的 reasoning prefix。
- **Changed Constraint / Mechanism:** generator 产生完整 response，再在某处截断；冻结的 receiver
  读取 prompt 与截断 prefix 并继续求解。若 receiver 最终答对，generator 获得 transfer reward，
  并与 answer/format reward 联合用于 RL。训练目标从“我是否答对”扩展为“我的中间状态是否让另一
  个求解器更可能完成任务”。
- **State Ownership / Control and Data Flow:** generator policy 拥有被优化 trajectory；cut policy
  决定暴露的 prefix；frozen receiver 是 reward instrument，不应与 generator 共同更新；verifier
  只判断 receiver outcome。receiver model/version、prompt、cut location、sampling 与 answer checker
  都是 reward identity 的一部分。
- **Implementation / Evaluation Contract:** 作者在 8×H200 141GB 上以 batch 1024、每 prompt 八条
  generations、最长 8192 tokens 训练，并在 MATH、AMC、GPQA 等 math/science 集合报告 Maj@K、
  pass@K 与 receiver ablation。额外 receiver rollout 增加 FLOPs；论文的 compute comparison 只在
  所列模型、长度、采样和 verifier 条件下成立。
- **What the Evidence Proves / Does Not Prove:** ablation 支持 receiver choice 与 transfer signal 会改变
  训练结果，说明“可传递性”能作为 final correctness 之外的可操作 reward。它不证明 prefix 是忠实
  chain-of-thought、对人可解释、跨模型普遍可迁移，或在开放域任务中仍可可靠评分；receiver 也可能
  奖励符合自身偏好的表述而非更正确的推理。
- **Trade-offs / Previous Design / Failure Modes:** 新机制增加第二模型调用、reward variance、cut-policy
  sensitivity、receiver bias 与 reward hacking 面；receiver 太强可能忽略坏 prefix，太弱又无法识别
  有用思路。final-answer RLVR 在答案 verifier 强、预算有限或不需要中间协作时仍是合理旧分支。
- **Evolution Relationship:** `Direct Evolution`：outcome-only reward → process/verifier signals →
  receiver-conditioned transfer reward。它补充而非替代 correctness，且 correctness 与 transferability
  必须分别保留。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch29 主 owner，Ch62 负责 reward-instrument
  evaluation；已读 Ch27～30 与 Ch62。现有正文覆盖 verifier/reward proxy、group statistics 与 rollout
  contract，但没有把“另一 solver 能否从中间状态继续”定义为独立 reward object。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`。
- **Open Questions:** receiver ensemble 能否降低单模型偏好？怎样区分 genuinely useful prefix 与
  receiver-specific prompt exploit？transfer reward 的隐私、reasoning exposure 与训练成本怎样治理？

### ProSeCo: Learning to Correct during Masked-Diffusion Decoding

- **Candidate / Week / Score:** ProSeCo / 2026-W07 / 25/30；
  `Source Family ID: proseco-diffusion-self-correction`。
- **Source Type / Date / Coverage:** arXiv:2602.11590 v1，2026-02-12；已读 method、training/sampling
  algorithms、implementation、HumanEval/MBPP/GSM8K/Minerva experiments、parallelism sensitivity、
  ablation、limitations 与 future work。
- **Original Problem / Previous Design:** masked diffusion LM 可在一轮并行确定多个 token，因而比
  autoregressive one-token step 更有并行空间；但高 parallel decoding 会让早期错误互相条件化。
  只训练 masked-token reconstruction 对生成未确定位置合理，却没有显式训练模型修正已经可见但错误
  的 token。
- **Changed Constraint / Mechanism:** ProSeCo 在标准 unmasking forward 后，把模型输出复用或扰动成
  带错误的中间序列，再做第二次 forward，训练 corrector 同时识别并修正错误 token。采样时在
  unmask steps 之间插入 correction loops；并行度越激进，通常越需要更频繁的 correction。
- **State Ownership / Control and Data Flow:** sampler 拥有当前 partially unmasked sequence、mask
  schedule、correction interval 与 commit policy；同一模型同时参数化 proposal 和 correction。
  已生成 token 不再天然 immutable，因此 streaming、cache identity、rollback 与 stop condition 必须
  区分 provisional state 和 committed output。
- **Implementation / Evaluation Contract:** 以 LLaDA Base 8B 为主进行 SFT，并覆盖 conditional 与
  unconditional tasks；HumanEval、MBPP、GSM8K、Minerva 以 batch 1 评估。训练增加第二次 correction
  forward；公开材料未披露完整硬件、并发或 serving SLO，因而不能把质量/步数曲线外推为线上吞吐。
- **What the Evidence Proves / Does Not Prove:** 作者实验支持“显式 correction training 在所测
  diffusion model/tasks 上缓解 aggressive parallel decoding 的误差累积”，并显示 correction frequency
  与并行 operating point 相互依赖。它不证明 correction 总能恢复、优于 autoregressive decoding，
  或同一 schedule 可跨模型规模与 domain 迁移。
- **Trade-offs / Previous Design / Failure Modes:** 训练与推理都增加 forward work，错误 detector 与
  corrector 共享模型盲点，反复改写可能振荡或破坏原本正确 token。保守 unmask schedule 在 latency
  不敏感、错误成本高或 runtime 不支持 mutable output 时仍更简单；AR 在严格 streaming/append-only
  cache contract 下仍成立。
- **Evolution Relationship:** `Direct Evolution`：mask reconstruction → parallel unmasking → inference-time
  heuristic correction → correction-aware training。与同周 LLaDA2.1 属同一 source family 邻接分支：
  LLaDA2.1 以 editable token set/CPT-SFT-RL 建立 draft/edit 能力；ProSeCo 用额外 denoising/corrector
  pass 学习通用修正，二者不能合并成同一算法。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch40 主 owner，Ch25 交接 correction training；已读
  Ch39～41 与 Ch24～26。现有 Ch40 以 AR append-only Decode 为主，尚未建立 diffusion provisional
  token、correction cadence 与 commit boundary。
- **Integration Decision:** `Books Candidate — Integrate New Mechanism / Human Gate Pending`；应与
  LLaDA2.1 共同形成实验性演进分支，而不是重复写两段论文摘要。
- **Open Questions:** mutable token 怎样与 user-visible streaming、radix/KV cache 和 cancellation 对齐？
  proposal/corrector 是否需要解耦参数或 verifier？何时 correction cost 超过并行收益？

### UniT: Unified Multimodal Test-Time Scaling

- **Candidate / Week / Score:** UniT / 2026-W07 / 24/30；
  `Source Family ID: unit-multimodal-iterative-refinement`。
- **Source Type / Date / Coverage:** arXiv:2602.12279 v1，2026-02-12；已读 trajectory synthesis、
  unified-model training、sequential/parallel inference、memory/reflection ablation、evaluation contract、
  compute disclosure 与 limitations。
- **Original Problem / Previous Design:** 文生图/图像编辑的一次生成接口延迟低、状态少、易于产品化；
  parallel best-of-N 还能用独立 samples 换取质量。但复杂约束常需要规划、验证和局部修订，单次生成
  缺少显式反馈；纯 parallel selection 又不会让后续候选利用前一次失败信息。
- **Changed Constraint / Mechanism:** teacher pipeline 先合成 20K prompts，由生成模型提出初稿、VLM
  验证并分解问题、编辑模型迭代修订；过滤后约 12K trajectories 用于训练统一 BAGEL model，使其在
  inference 内承担 planning、generation、reflection 与 refinement。sequential scaling 把前轮 artifact
  和诊断作为下一轮状态，parallel scaling 则独立生成后由 selector 选择。
- **State Ownership / Control and Data Flow:** inference run 拥有 goal、current image、reflection、
  subgoals、content memory 与 stopping/budget；统一模型提出下一步，但 artifact identity、轮次、选择和
  commit 应由 workflow/evaluator 保持。把这些状态只塞回自然语言 context 会丢失 image/version 与
  verifier provenance。
- **Implementation / Evaluation Contract:** 训练轨迹由 Flux Pro、Qwen3-VL、Flux Kontext/Qwen image
  edit 组合生成，平均约 3.6 轮；统一模型训练约 700 H100-hours。实验比较相同生成图片数量下的
  sequential 与 parallel 路线，但 selection/VLM verifier cost 未完整计入，因而不能把 image count
  等同于 wall-clock 或总 compute。content-memory/verification/subgoal ablation 支持这些状态在作者
  任务中的作用。
- **What the Evidence Proves / Does Not Prove:** 证据支持“反馈可被写入下一轮 artifact refinement，
  因而 sequential test-time compute 与独立 best-of-N 是不同机制”。它不证明统一模型优于 modular
  workflow、所有图像任务都随轮数单调改善，或作者比较代表同等端到端成本。
- **Limitations / Trade-offs / Previous Design:** 作者指出 physics/attribute binding 仍可能无法修正，
  verification hallucination 还会把正确图像改坏；新增多轮 latency、artifact storage、selector bias、
  stopping 与 regression risk。单次生成适合低延迟/简单任务；parallel sampling 适合候选独立、选择器
  可靠且并行资源充足的场景；modular tools 在需要独立升级/审计时仍更可控。
- **Evolution Relationship:** `Direct Evolution`：one-shot generation → parallel best-of-N → modular
  generate–verify–edit → unified sequential refinement；统一模型减少组件边界，不消除 workflow state。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch77 主 owner，Ch76/62 分别承接 reflection 与
  evaluator contract；Ch18 只做“decoder-only text interface 不足以拥有 multimodal artifact semantics”
  的短边界。已读目标及相邻章节。现有 Ch77 已有 evaluator-driven search，却未明确 sequential
  artifact refinement 与 parallel best-of-N 的 compute/accounting 分叉。
- **Integration Decision:** `Emerging / Experimental — Books Candidate / Human Gate Pending`。
- **Open Questions:** image verifier 与 generator 同源时怎样评估 correlated error？artifact lineage、
  rollback、human approval 与 selector compute 怎样纳入统一 run contract？

### Aletheia / Gemini Deep Think for Mathematics Research

- **Candidate / Week / Score:** Aletheia / Gemini Deep Think / 2026-W07 / 25/30；
  `Source Family ID: aletheia-math-research-agent`。
- **Source Type / Dates / Revision:** arXiv:2602.10177 v1 2026-02-10、v3 2026-03-06 + Google
  DeepMind official blog 2026-02-11；v3 只用于完整机制与限制核验。相关 Gemini 科学研究案例合集
  arXiv:2602.03837 v1 为 2026-02-03，归 W06，不在 W07 重复计分。
- **Full-read Coverage:** 已读 agent harness、inference scaling、tool use、数学案例、FirstProof、
  ablation、accuracy/error analysis、autonomy/significance taxonomy、HAI Card、Related Work、Conclusion
  与关键 Appendix；同时核对公开 prompts/outputs 入口。模型 architecture、训练 recipe、硬件、
  token 数和绝对 inference cost 未披露。
- **Original Problem / Previous Design:** competition math 的题面自洽、标准答案明确，增加
  inference-time parallel thinking 对探索多个解法合理；research math 却需要跨文献、长证明、novelty
  判断与专家责任，单次长 reasoning 易受早期错误、自我确认和引用 hallucination 影响。
- **Changed Constraint / Mechanism:** Aletheia 在 Gemini Deep Think 之上组织 Generator、Verifier、
  Reviser 三类 subagents，循环到 verifier 接受或达到 attempt limit；各 subagent 内部还可调用多次
  base model。Search/web 用于文献导航，Python 只提供有限额外收益。核心变化不是单纯增加 tokens，
  而是把 proposal、verification、revision、tool evidence 与 abstention 拆成可观察阶段。
- **State Ownership / Control and Data Flow:** harness 拥有 problem、attempt、candidate proof、verifier
  verdict、revision、tool results 与 stopping；模型提出内容，不拥有“数学已成立”的最终事实。
  研究输出还需绑定 human expert review、literature search、novelty status 与公开 prompt/output。
  最终论文由人类作者撰写并承担正确性和 attribution 责任。
- **Evaluation Contract:** inference scaling 在 IMO-ProofBench Advanced 30 题和内部 FutureMath Basic
  上做单次/每 compute scale、tool-disabled、human grading；Aletheia 动态 compute 无法精确控制。
  FirstProof 是 10 个未公开解答的 research-level lemmas，作者报告 best-of-2 下 6 题返回候选并由
  专家评估，P8 存在 5/7 分歧。Erdős case study 从 700 个标记 open 的题目中筛出 212 responses；
  在可判定的 200 个 candidates 中，31.5% 在某种解释下 technically correct，只有 6.5% 被认为
  meaningfully addressed intended problem。模型版本、专家流程和 contamination window 均限制外推。
- **What the Evidence Proves / Does Not Prove:** ablation 支持同 base model 下 generator–verifier–reviser
  harness 可优于单次 Deep Think，并显示 abstention/专家复核是可靠性的一部分。证据也直接表明
  technically correct、meaningfully correct、novel 与 significant 是不同 claim。它不证明研究级数学
  已普遍自动化、自然语言 verifier 等价于 formal proof、文献搜索消除错误引用，或少数成功案例代表
  总体 hit rate；作者明确指出成功稀少、歧义利用、hallucination 和 literature rediscovery 仍常见。
- **Trade-offs / Previous Design / Failure Modes:** 多轮 agent 增加动态 compute、verification latency、
  correlated self-check、tool provenance 与专家 bottleneck；web access 把虚构引用转成“真实论文但错误
  归因”的更隐蔽故障。单次 solver 对有标准答案、预算固定的问题仍更简单；formal systems 在 theorem
  language 可表达时提供更强 correctness contract；高新颖性研究仍需领域专家判断。
- **Evolution Relationship:** `Direct Evolution`：single-pass reasoning → inference-time parallel search →
  generator–verifier–reviser harness with tools；`Layering / Dependency`：human expert review 与 HAI Card
  不替代模型机制，而是给 capability/autonomy claim 建立 evidence boundary。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch62 主 owner，Ch76/77 分别承接诊断式 revision
  与 durable workflow；已读目标及相邻章节。现有正文已经区分 artifact、environment、trace 和
  claim-level provenance，但可用该案例强化“autonomy 与 scientific significance 必须分轴，technical
  correctness 也不等于 intended/novel result”。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；只应吸收
  evidence taxonomy 与 workflow boundary，不写成模型能力新闻。
- **Open Questions:** expert disagreement、literature novelty 与 verifier verdict 怎样形成可版本化 claim
  graph？dynamic inference budget、abstention 与 human review capacity 怎样联合校准？

### Seedream 5.0 Lite Official Launch

- **Candidate / Week / Score:** Seedream 5.0 Lite / 2026-W07 / 18/30；
  `Source Family ID: seedream-unified-multimodal-model-family`。
- **Source Type / Date / Coverage:** ByteDance Seed official launch，2026-02-13；已检查公开能力范围、
  MagicArena evaluation description、作者限制与 model-family positioning。没有 technical report、
  model card、architecture、training、serving、hardware、precision、latency 或 cost contract。
- **Verified Fact / Mechanism Boundary:** 官方页面将其描述为相对较小的 unified multimodal model，
  支持 image generation/editing、visual understanding、reasoning 与 real-time search，并展示多图、局部
  编辑和 office/study 场景。公开信息不足以判断这些能力由统一 backbone、tool router、retrieval、
  diffusion architecture 还是外部 workflow 实现；因此机制一律 `Not Disclosed`。
- **Evaluation Contract:** 官方称 MagicArena 使用多模型 double-blind side-by-side、领域专家评分与
  数万轮比较建立 Elo；未公开完整 model list、prompt distribution、sampling、rater agreement、置信区间、
  cost/latency、失败样本或可复现 artifact。所有性能描述只能作为 vendor claim。
- **What the Evidence Proves / Does Not Prove:** 证据仅证明 2026-02-13 的产品/模型族状态与官方评测
  口径；不证明具体内部机制、相对通用领先、online SLO 或“理解意图”的可操作定义。官方同时承认
  structural stability、realism 与 aesthetics 仍有改进空间。
- **Trade-offs / Evolution:** unified interface 可减少用户在理解、生成、编辑间切换组件的成本，却把
  capability routing、artifact version、search provenance、edit consistency 和 failure attribution 隐藏在
  单一 model identity 后。modular vision/edit/search pipeline 在需独立升级、审计和故障隔离时仍合理。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch55/62 主承接 model/evaluation identity，Ch18 只作
  architecture 未披露边界；已读相关章节。没有公开新机制可填补 Books 长期认知缺口。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Not Disclosed`。
- **Open Questions:** 后续 technical report/model card 是否会公开 architecture、training data boundary、
  safety evaluation、tool/search ownership 与 workload-aware latency/cost？

### Experiential Reinforcement Learning

- **Candidate / Week / Score:** Experiential Reinforcement Learning（ERL）/ 2026-W07 / 25/30；
  `Source Family ID: experience-reflection-consolidation-rl`。
- **Source Type / Date / Revision / Access:** arXiv:2602.13949 v1，首次公开 2026-02-15；HTML 全文、
  Algorithm 1/2、三组实验、component ablation 与 Appendix B/C 均已复核。论文没有独立
  Limitations/Threats to Validity section，未公开多 seed 方差、完整训练 token 总量与独立复现。
- **Original Problem / Previous Design:** 标准 RLVR 用 episode 末端 scalar reward 更新 policy；这在
  reward 稀疏、轨迹长且错误会累积时仍是合理的通用接口，却要求模型从一个结果分数中隐式恢复
  “哪里错、下一次如何改”。推理期 Self-Refine/Reflexion 可显式生成诊断，但会把额外 rollout、
  reflection memory 和 latency 留到部署路径。ERL 要解决的是两者之间的 gap：训练时利用可观察
  feedback 形成局部修正，同时让最终部署 policy 不依赖该 feedback loop。
- **Mechanism / State Ownership / Data Flow:** 对同一任务先采样 `y1`，环境返回 `(f1,r1)`；仅当
  `r1 < tau` 时，由同一 policy 基于任务、失败轨迹、反馈与跨 episode reflection memory `m` 生成
  `Delta`，再采样 `y2` 并取得 `r2`。`r2` 同时给 reflection/second attempt 提供 RL 信号，超过阈值的
  reflection 写入训练期 memory；selective distillation 再用成功的 `y2` 监督 `pi(y2|x)`，从输入中
  移除 reflection。环境拥有 outcome，memory 拥有可复用纠错文本，policy 参数拥有最终被
  consolidated 的行为；三种 state 不能混成“Agent 自己永久记住了经验”。
- **Why Gating Matters:** 作者早期对所有样本都反思，出现 successful trajectory 上的 instance-specific
  reward hacking，以及 reflection/second-attempt 的 off-policy signal 压过 base-policy on-policy
  update。`tau=1` 的失败门控让成功样本保持纯 on-policy，只把额外计算给失败样本。这支持的长期
  原则是 reflection 需要 admission policy，而不是“多一轮总会更好”。
- **Implementation / Evaluation Contract:** 两个 backbone 为 Qwen3-4B-Instruct-2507 与
  OLMo-3-7B-Instruct，optimizer 均为 GRPO；RLVR 每题 10 rollouts，ERL 的两个 attempt 各分一半，
  以近似对齐 per-task rollout compute。FrozenLake 与单箱 Sokoban 各使用 10,000 个程序生成训练
  instance、100 个同分布独立评估 instance，step budget 为 8；HotpotQA 使用本地 Wikipedia dense
  retrieval。训练在单节点 8×H100 上进行，batch 64，prompt/response 上限各 8,196 tokens，
  learning rate `1e-6`，异步 vLLM rollout；这些数字只属于作者配置。
- **Evidence / Ablation Boundary:** 在六个 model-task 组合中作者报告 ERL 高于其 RLVR baseline；
  post-reflection trajectory 也普遍高于 pre-reflection。去除 structured reflection 的退化比去除 memory
  更稳定，而 OLMo-3-7B Sokoban 中 no-memory 反而略高于 full ERL，说明错误 reflection 会被持久
  memory 放大。实验没有单独移除 distillation、gating 或 textual feedback，也没有与等预算的其他
  retry/curriculum/credit-assignment 方法做充分比较，因此不能把全部收益归因于任一 component，
  也不能把作者最高百分比外推到开放式生产 Agent。
- **Trade-offs / New Failure Modes / Coexistence:** 训练期每个失败样本增加 reflection 与 second attempt，
  并引入 off-policy distillation、memory contamination、threshold sensitivity 与 correlated self-critique。
  标准 RLVR 在 reward 较密、短轨迹、额外 feedback 不可靠或吞吐优先时仍更简单；推理期 reflection
  在需要按当前任务证据修正而又不能重新训练时仍不可替代。ERL 获得的是把一部分纠错成本前移到
  training 的可能性，而不是消灭 runtime verification。
- **Evolution Relationship:** `Direct Evolution`：terminal scalar RLVR → failure-gated
  experience–reflection–retry → successful retry distillation into deployment policy；
  `Layering / Dependency`：Ch76 的 inference-time Reflection 为训练产生中间纠错信号，Ch29 的
  policy optimization 才把它写入参数。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 为 Ch29；Ch76 只增加训练/推理边界的
  handoff。已读 Ch28～30、Ch75～77。现有 Ch29 已有 rollout、reward、off-policy 与 distillation
  主线，Ch76 明确 reflection 不更新参数；ERL 提供的是两章之间尚未显式写出的
  “reflection-conditioned trajectory + consolidation”演进节点。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；后续若
  进入 Books，应写机制、门控和 state boundary，不复制作者 benchmark headline。
- **Open Questions:** distillation 与 gated retry 各自贡献多大？reflection memory 如何做 provenance、
  retrieval、supersession 和 poisoning recovery？更长、随机或不可验证环境中，equal-rollout 是否仍等于
  equal wall-clock/compute？

### REDSearcher: Long-Horizon Search-Agent Training System

- **Candidate / Week / Score:** REDSearcher / 2026-W07 / 26/30；
  `Source Family ID: redsearcher-task-data-environment-training`。
- **Source Type / Date / Revision / Access:** arXiv:2602.14234 v1，首次公开 2026-02-15；已阅读全文、
  formulas、training recipe、evaluation、ablation 与 Appendix A，并联合检查官方 project page、
  dataset links 和 repository。当前 repository 已公开 SFT/RL 数据入口、SFT example 与
  DeepTraceHub，但 model、完整 RL training code/quickstart 仍标注 coming soon；后续 artifact 只能
  帮助验证实现，不改写 W07 event date。
- **Original Problem / Previous Design:** 真实 web-search rollout 同时受高 latency、不稳定 external API、
  tool cost 与稀疏 final reward 限制；普通 multi-hop QA 又常是低 treewidth 的线性路径，模型可能靠
  单页 shortcut 或参数记忆答题。直接在 live web 上端到端 RL 虽最接近部署分布，却把 task scarcity、
  data quality、environment variance 与 policy optimization 一次性耦合，难以规模化和归因。
- **Mechanism — Task/Data Plane:** 系统从 Wikidata relation 与 web hyperlink 构图，再用 Graph Agent
  增密跨来源约束；以 reasoning graph 的 treewidth 作为结构耦合 proxy，并显式分散 decisive evidence，
  使任务更难被单一文档解决。随后把实体线索改写为必须调用 map/image/search 等 tool 的 operational
  constraint，并通过 difficulty、graph alignment、retrieval、hallucination、rollout 与 answer uniqueness
  verifier cascade 过滤。treewidth 只是一种合成难度控制变量，不是人类/模型认知复杂度定律。
- **Mechanism — Capability and Interaction Plane:** mid-training Stage I 在 32K context 上分开训练
  intent-anchored grounding 与 hierarchical planning，Stage II 扩到 128K，并加入 function calling、
  observation/state retention 与长轨迹。post-training 先从真实 search/visit/python/Google Scholar/Maps
  收集 SFT trajectory，再在本地等价接口上用 GRPO。离线环境缓存必要证据、加入数千万 distractor
  documents 并 obfuscate URL；environment server 统一工具接口和 fallback。系统把“先学习 atomic
  subskills，再学习 action-feedback loop”作为降低昂贵在线探索的 curriculum，而非声称 simulator
  等同开放网络。
- **State Ownership / Control and Data Flow:** query graph 与 metadata 拥有任务 ground truth；local
  corpus/cache 拥有可复现 observation；ReAct transcript `H_T` 保存 action/observation 与 compact
  working state；policy 只选择下一 tool/action；verifier/judge 产生 outcome reward；training runtime
  拥有 rollout version、advantage 与 update。部署 web 的 freshness/authenticity 不由离线 cache 保证，
  context management 也必须与 base-model score 分开归因。
- **Implementation / Evaluation Contract:** text model 基于 Qwen3-30B-A3B；mid-training batch 为
  512/256、SFT batch 128，learning rate 从 `5e-5` 降至 `1e-6`。RL 每 mini-step 32 queries、每题
  16 rollouts，GRPO learning rate `1e-6`，使用 TIS/Routing Replay，异常 repetition/length/tool-failure
  样本参与 advantage 但不做 gradient update；推理上限 128K，summarizer 为 Qwen3-30B-A3B，judge
  为 GPT-OSS-120B。论文未披露训练总 tokens、GPU 型号/数量、wall-clock、API/crawl 成本或 SLO，
  所以“cost-efficient”只有相对机制与作者实验支持，没有完整成本合同。
- **Evidence / Ablation Boundary:** 500 个合成实例的人审通过率超过 85%，强模型在指定 agent setting
  约 40%，30 分钟人类预算约 47%；这些数字支持任务并非全为不可解噪声，但不足以证明大规模 corpus
  同等质量。progressive mid-training ablation 的平均分从 42.81 到 47.39，不过 HLE/GAIA 某些 stage
  下降，说明 atomic capability 与 benchmark 并非单调一致；SFT 到 RL 的四 benchmark 平均 reward
  由 47.4 到 51.3，tool calls 同时下降。tool-free/tool-enabled 对照有助于拆开参数记忆与工具收益，
  但跨模型 toolset、context management 和 evaluator 并未完全同质，厂商/作者 leaderboard 不能作为
  通用 superiority 结论。
- **Limitations / Trade-offs / New Failure Modes:** 论文没有独立 Limitations section。合成 graph 的
  proxy bias、LLM verifier 相关性、10% residual query error、cached evidence staleness、sim-to-real gap、
  judge bias、over-searching 与 20/30-turn hard cutoff 都会改变训练目标。离线环境换来低成本、可重复和
  高吞吐，却弱化 live ranking drift、页面变化、access failure 与 adversarial content；真实环境 SFT
  保留部署接触面，但重新引入 API cost 与非确定性。对小 corpus、短 hop、稳定 tool 或需要真实
  freshness 的任务，传统 RAG/SFT 或直接 live evaluation 仍是合理分支。
- **Evolution Relationship:** `Direct Evolution`：static multi-hop QA → graph/evidence-constrained task
  synthesis → atomic grounding/planning mid-training → long-horizon tool trajectories → real-environment SFT
  + simulated-environment RL；`Layering / Dependency`：Ch23 定义训练任务分布，Ch72 定义 evidence
  retrieval，Ch75 定义 plan，Ch77 拥有 tool/workflow state，Ch29 只处理 reward-driven update。
- **ROADMAP / Chapters Read / Existing Coverage:** Ch23 是主 owner 候选，因为最长期的新机制是把
  task topology、evidence dispersion、tool necessity 与 verifier cascade 写成可执行 data specification；
  Ch29、Ch72、Ch75、Ch77 只各承接 RL contract、retrieval sufficiency、planning 与 durable tool-state
  handoff。已读 Ch23/29、Ch72、Ch75～77 及相邻章节。现有 Ch23 已有 distribution/lineage，Ch72 已有
  relevance/sufficiency，Ch75/77 已有 plan 与 deterministic spine，但尚未把这四层串成 search-agent
  capability curriculum。
- **Integration Decision:** `Books Candidate — New Evolution Chain / Human Gate Pending`；只吸收
  task-data-environment-training 的分层关系与 evidence boundary，不复制 SOTA 表。
- **Open Questions:** treewidth 与实际 agent failure/working-memory load 的相关性是否跨 domain 成立？
  local environment 如何版本化 freshness、coverage 与 adversarial noise？真实/模拟 trajectory 的比例、
  sim-to-real drift 和 judge false accept 如何进入训练与发布 gate？

### Less is Enough / FAC Synthesis

- **Candidate / Week / Score:** Less is Enough: Synthesizing Diverse Data in LLM Feature Space with
  Sparse Autoencoders / 2026-W07 / 25/30；`Source Family ID: feature-activation-coverage-synthesis`。
- **Source Type / Date / Revision / Access:** arXiv:2602.10388 v1，首次公开 2026-02-11；当前 v4
  （2026-05-29）PDF 的 metadata、Introduction、SAE/FAC 定义、theory、Algorithm 1、四类任务、
  baselines、coverage control、cross-model transfer、sensitivity、human study、Conclusion 与相关
  Appendix 已复核。后续 revision 只用于机制和限制核验，不改写 W07 日期。
- **Original Problem / Previous Design:** post-training data 的 lexical、embedding 或 label diversity
  是便宜且合理的 proxy，却无法回答样本是否覆盖了当前模型真正用于下游任务的 feature。增加近义
  改写可能扩大文本距离，却不增加 decision-relevant variation；反过来，表面相似样本也可能触发不同
  internal feature。论文把问题从“样本彼此多远”改写为“目标任务需要的表示 feature 是否被覆盖”。
- **Mechanism / State Ownership / Data Flow:** 先在目标模型某层 activation 上训练 sparse autoencoder，
  用 anchor set 估计 task-relevant feature universe，再计算 seed set 未覆盖的 feature。FAC Synthesis
  对每个 missing feature 取得 high/low-activation contrastive examples，让生成模型归纳 feature 并生成
  candidate，最后以 activation threshold 过滤。anchor set 拥有目标分布 proxy，SAE dictionary 拥有
  feature coordinates，generator 只提出样本，目标模型 activation/filter 决定是否纳入；这些 state
  不应被合并成“模型自动发现了真实语义类别”。
- **Principle / Theory Boundary:** FAC 将 coverage 写在模型 representation space 而不是文本空间，
  并把 generalization gap 分成 distribution gap 与 finite-sample error。理论说明在论文假设下扩大相关
  feature coverage 可以改善 bound；它不证明单层 SAE 已恢复全部任务因果 feature，也不消除 anchor
  bias、dictionary reconstruction error、feature splitting/merging 或 threshold 选择。feature 的 LLM
  summary 和人类命名是解释层，不是训练机制成立的必要真值。
- **Implementation / Evaluation Contract:** 作者在 toxicity detection、reward modeling、behavior
  steering 与 instruction following 四类任务上比较 random sampling、text/embedding diversity 与 FAC；
  完整实验使用 LLaMA、Mistral、Qwen 等模型家族，并报告 FAC 与下游指标在其配置中的相关性。
  计算资源合计 8×H100 与 8×A100，其中一项 SAE training 记录为 4×H100、4.41 小时。模型层、SAE
  width/sparsity、activation threshold、generator、数据量和每项 task metric 共同构成结果合同，不能
  把文中相关系数或性能增益脱离这些条件复用。
- **Evidence / Ablation Boundary:** 作者报告 FAC 对五组 downstream measure 的 Pearson correlation
  分别为 0.95、0.85、0.88、0.79 与 0.72；固定样本量的 coverage 对照、dense embedding 对照、SAE
  参数敏感性、人类 feature interpretation 与跨模型 transfer 增强了机制证据。但这些仍是作者实验：
  没有独立复现，cross-model overlap 不等于 feature identity，生成器与 filter 使用相关模型时还可能
  形成自洽偏差。behavior steering 的不稳定结果也表明 activation coverage 不保证任务收益单调增加。
- **Limitations / Trade-offs / New Failure Modes:** 方法需要 representative anchor、可用的 SAE、目标
  模型 activation access 与多轮生成/过滤，换来的是比文本去重更 task-aware 的昂贵 data selection。
  错误 anchor 会把部署盲区定义成“不相关”，polysemantic/遗漏 feature 会误导 synthesis，强激活过滤
  可能放大 harmful behavior 或 artifact。论文也承认单层 SAE 难以覆盖 multi-layer reasoning circuit；
  GSM8K/LiveCodeBench 只能视为初步边界。对无 activation access、任务尚未定义或简单覆盖问题，
  source/label/text diversity 与人工 data audit 仍然成立。
- **Evolution Relationship:** `Direct Evolution`：surface/embedding diversity → model-feature coverage →
  missing-feature-targeted synthesis；`Layering / Dependency`：Ch5 解释 representation/SAE evidence，
  Ch23 拥有 dataset specification 与 lineage，Ch25 只承接 synthetic demonstration 的 verifier boundary。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 为 Ch23；已读 Ch5、Ch23、Ch25 及相邻
  章节。Ch23 已把 data distribution 写成 executable specification，却仍主要按 source/domain/quality
  描述 coverage；FAC 提供“coverage metric 本身也依赖 model representation”的新分支。Ch5 已有
  SAE faithfulness budget，因此不能把 FAC feature 直接写成真实概念；Ch25 已有 synthetic-data judge
  bias，不需要重复论文流程。
- **Integration Decision:** `Books Candidate — New Mechanism / Human Gate Pending`；若进入 Books，
  只增加“coverage coordinate system”选择、anchor/representation/filter 三层偏差及旧 diversity proxy
  仍成立的条件，不复制论文指标表。
- **Open Questions:** multi-layer/circuit-level coverage 如何定义且保持可计算？anchor drift、SAE revision
  与 dataset version 怎样共同进入 lineage？生成与过滤使用相近模型时，如何测量 correlated blind spot？

### OneVision-Encoder

- **Candidate / Week / Score:** OneVision-Encoder: Codec-Aligned Sparsity as a Foundational Principle
  for Multimodal Intelligence / 2026-W07 / 25/30；`Source Family ID: codec-guided-sparse-rgb-encoder`。
- **Source Type / Date / Revision / Access:** arXiv:2602.08683 v1，首次公开 2026-02-09；当前 v3
  （2026-02-26）HTML 的 Method、pretraining data、controlled probing、selection ablations、spatial-bias
  analysis、implementation details 与 token-allocation cases 已复核，并检查官方 code/data/model links。
  论文没有独立 Limitations section；后续 revision 不改写事件日期。
- **Original Problem / Previous Design:** uniform frame sampling 加 dense RGB patchification 保留完整
  空间内容、实现成熟，且在相机运动、静态文字和全局场景上不依赖 codec heuristic；代价是在固定 visual
  token budget 下只能稀疏看时间，或对大量可预测背景重复计算。OneVision 的变化不是“codec token 直接
  进入 ViT”，而是用 HEVC 暴露的 motion magnitude 与 residual energy 选择哪些 P-frame RGB patches
  值得送入 encoder。
- **Mechanism / State Ownership / Data Flow:** 每个 GOP 的 I-frame 保持 dense RGB patches；P-frame
  先解码到 RGB，codec motion/residual 只产生 patch saliency mask，top-K index 再选择对应 RGB patches。
  不规则 token 保留原始 `(t,x,y)`，由共享 3D RoPE 表达相对时空位置；同一 ViT 还接收 chunk-wise
  与 single-image patchification，并以超过一百万 concept clusters 的 self-supervised discrimination
  组织 object/motion representation。bitstream/preprocessor 拥有 saliency，token layout/position index
  拥有稀疏序列身份，encoder 参数拥有 representation；选择信号与被编码内容必须分开。
- **Implementation / Workload Contract:** Large encoder 为 24-layer ViT、hidden size 1024、16 heads、
  patch size 14、3D RoPE；默认 64 frames、GOP 32、每帧 dense grid 256 patches，两个 I-frame 加稀疏
  P-frame patches 形成 2,048-token clip，作者口径为相对全 64-frame dense 输入减少 87.5%。Stage 1/2
  分别加入 image 与 OCR/video/codec inputs；训练使用 128×A800，attentive probing 另用 8×A800。
  这些配置、pretraining data scale 与 downstream alignment 不能省略后再声称通用 token/accuracy 收益。
- **Evidence / Ablation Boundary:** controlled pipeline 固定 language backbone 与 downstream instruction
  data，将 encoder 解耦后与 Qwen3-ViT/SigLIP2 比较；相同 token budget 下的 attentive probing、替换
  selected patches、motion-specificity 与 position shuffle 提供比 leaderboard 更直接的证据。论文还
  观察到 codec-only selection 的 center bias，chunk-wise allocation 在不增加 token budget 下改善外围
  coverage。作者报告的 3.1%–25% retained patches、16 个 benchmark 和平均收益只属于其数据、codec、
  sampling 与 alignment pipeline；超大规模预训练和 stage mixture 仍是混杂因素，也没有独立复现。
- **Limitations / Trade-offs / New Failure Modes:** 稀疏选择把 compute 从 dense encoding 移到 codec
  preprocessing、saliency、irregular layout 和 position bookkeeping。motion/residual 不等于 semantic
  importance：静态文字、缓慢变化、全局背景与 camera motion 都可能失真；GOP、bitrate、codec、
  quantization 与 camera-motion compensation 会改变 selection。top-K 提供固定预算，却需要 content
  drop、position integrity 和 fallback 监控。dense frames 在短视频、静态文档、codec metadata 不可信
  或漏检成本高时仍合理。
- **Evolution Relationship:** `Direct Evolution`：uniform sparse frames → dense temporal coverage with
  codec-guided sparse RGB patches；`Layering / Dependency`：3D position identity 与 fixed token budget
  连接 Ch18、Ch22，真正的 Prefill/TTFT 效果仍需 Ch39 的 end-to-end runtime contract。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 为 Ch18 的 multimodal architecture/input
  branch；已读 Ch17～19、Ch22、Ch39～41。现有 Ch18 仍以 text-only decoder organization 为主，尚未
  明确 visual evidence 如何先被 tokenized；Ch22 已有 sequence-compute budget，Ch39 已有 TTFT 分解，
  因而两章只需要 handoff，不能把 visual-token reduction 直接等同 TTFT reduction。
- **Integration Decision:** `Books Candidate — New Mechanism / Human Gate Pending`；后续应与 CoPE
  并列为两条不同 codec-aware 分支，明确 OneVision 的 P-frame input 仍是 decoded RGB patches。
- **Open Questions:** 在 codec/bitrate/GOP shift 下 selection calibration 是否稳定？preprocessing 和
  irregular-attention overhead 纳入 end-to-end SLO 后净收益多少？static semantic evidence 的 recall
  如何成为 admission/fallback signal，而不是只看平均 benchmark？

### CoPE-VideoLM

- **Candidate / Week / Score:** CoPE-VideoLM: Leveraging Codec Primitives for Efficient Video Language
  Modeling / 2026-W07 / 27/30；`Source Family ID: compressed-domain-delta-video-tokens`。
- **Source Type / Date / Revision / Access:** arXiv:2602.13191 v1，首次公开 2026-02-13；当前 v2
  （2026-03-30）HTML 的 codec primer、Delta encoder、two-stage alignment、14-benchmark evaluation、
  runtime comparison、token-pruning comparison、training/data appendices 与 ablations 已复核，并检查
  Microsoft 官方 project link。后续 revision 只用于验证，不改变 W07 归档。
- **Original Problem / Previous Design:** keyframe sampling 通过少看 frames 控制 context 与 Prefill，
  是无需修改 vision stack 的稳健方案，但会漏掉采样间的短时运动；dense RGB encoding 保留每帧内容，
  却先支付完整 decode/vision-encoder 成本，再做 token pruning 时已经无法收回前半段计算。CoPE 把
  compression boundary 前移：I-frame 仍走 frozen vision encoder，P-frame 不恢复为 RGB token，而直接
  把 motion vector 与 residual 编成 compact Delta tokens。
- **Mechanism / State Ownership / Data Flow:** MPEG-4 GOP 提供 causal I/P dependency；motion-vector
  branch 与 residual branch 分别 patchify/encode，再由 learnable queries 聚合为少量 Delta tokens。
  预训练阶段以 reference/warped RGB transformer 提供 patch-level alignment；完整 VideoLM fine-tuning
  时删除这些 teacher branches，只保留小于 15M 参数的 Delta encoder，将 I-frame RGB tokens 与
  P-frame Delta tokens 按时间交错输入原 LLM。codec dependency graph 拥有 reconstruction order，
  Delta encoder 拥有 compressed-domain representation，LLM context 拥有 interleaved token history；
  它不是通用 KV compression，也不改变语言模型 next-token objective。
- **Temporal/Token Policy:** 原生 30 FPS、GOP 240 时每个 P-frame 依赖此前 reconstructed state；作者
  用 `s=30` 融合 consecutive P-frames 得到有效 1 FPS，在 temporal fidelity、token count 与 dependency
  validity 间做显式交换。默认每个 P-frame 8 个 Delta tokens；2/4/8/16-token ablation 显示增加到 8
  收益明显、16 边际变小，但这只是作者两个 benchmark/data regime 下的 operating point。
- **Implementation / Evaluation Contract:** base 为 LLaVA-Video-7B（SigLIP + Qwen2-7B）。Delta
  pretraining 使用 LLaVA-Video-178K；完整 fine-tuning 使用 1.39M QA、learning rate `1e-5`、global
  batch 128，64×A100-80G 训练 14 天，约 21K GPU hours。14 个 benchmark 覆盖 QA、temporal/motion、
  long-form 和 spatial tasks，部分评分依赖指定 GPT evaluator。硬件与 serving stack 未完整披露的
  “consumer GPU” runtime 不能作为可复现 production SLO。
- **Evidence / Ablation Boundary:** two-stage vs one-stage、Delta-token count、zeroed Delta token、
  codec-at-train/inference、higher frame rate 与 next-frame retrieval ablations 支持模型确实使用 compressed
  signal；与 post-hoc token pruning 的对照支持“在 RGB encoder 前省 work”的机制差异。作者报告最高
  93% token reduction 与 86% TTFT reduction，并给出 64-token generation、1 FPS 下的例子，但 GPU
  型号、并发、precision、queueing 和 serving SLO 未完整披露，故只能保留为作者配置中的结果，不能
  写成通用加速比例。部分 benchmark 仍低于 dense baseline，数据 mixture 的解释也是作者归因。
- **Limitations / Trade-offs / New Failure Modes:** 当前只支持 I/P frame，B-frame 的 future dependency
  与 decode/display reorder 不兼容 causal/streaming path；需要 tensorized codec primitives，固定 fusion
  size 对内容自适应不足，并受 codec type、bitrate、quality 与 GOP 影响。更激进 Delta compression 会
  丢失 appearance detail，预训练 alignment 增加独立 artifact/version，bitstream corruption 会传播到
  token sequence。dense RGB/keyframe 路径在 noncausal offline understanding、B-frame-heavy content、
  static fine detail 或无可控 codec pipeline 时仍成立。
- **Evolution Relationship:** `Direct Evolution`：dense RGB frames → post-encoding token pruning →
  compressed-domain P-frame Delta tokens；与 OneVision 是 `Alternative Branch`：OneVision 用 codec
  signals 选择 decoded RGB patches，CoPE 直接编码 primitives。`Layering / Dependency`：Ch18 拥有
  multimodal input/architecture，Ch22 承接 context budget，Ch39 只承接 TTFT contract，Ch41 说明它
  与 KV Cache compression 无关。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 为 Ch18；已读 Ch17～19、Ch22、Ch39～41。
  现有章节已经解释 text token、Prefill 与 KV lifecycle，却缺少“视觉 token 形成之前即可利用 source
  representation sparsity”的边界。后续只应增加 codec-aware visual-token evolution 与系统合同，避免
  把论文的 7B implementation 或 benchmark table 写进长期正文。
- **Integration Decision:** `Books Candidate — New Evolution Branch / Human Gate Pending`；必须与
  OneVision 成对审议，保留 RGB-selection 与 compressed-domain encoding 的差异和共存条件。
- **Open Questions:** codec preprocessing、Delta encoder 与 LLM Prefill 各自占 TTFT 多少？adaptive
  fusion 如何受 motion/content/SLO 控制？artifact identity 是否需包含 codec/version/GOP/bitrate，才能
  防止训练与 serving token semantics 漂移？

### Intelligent AI Delegation

- **Candidate / Week / Score:** Intelligent AI Delegation / 2026-W07 / 24/30；
  `Source Family ID: authority-accountability-delegation-framework`。
- **Source Type / Date / Revision / Access:** Google DeepMind authors 的 arXiv:2602.11865 v1，首次公开
  2026-02-12；已阅读全文，包括 organizational foundations、task decomposition/assignment、adaptive
  coordination、monitoring、trust/reputation、permissions、verification、security、ethics、protocol mapping
  与 conclusion。它是 framework/position paper，没有实现、benchmark、ablation 或 production evidence。
- **Original Problem / Previous Design:** 把 delegation 等同“拆任务并路由给另一个 Agent”在静态、低风险、
  短链路中简单有效；开放环境中却没有表达谁转移了多少 authority、谁对 outcome 负责、怎样验证完成、
  能否再委托以及失败时如何撤销。论文把 delegation 定义为持续决策过程，而不是一次 function call。
- **Framework / State Ownership / Control Flow:** task contract 描述 goal、constraints、criticality、
  uncertainty、duration、cost、resource、verifiability、reversibility、context sensitivity、subjectivity 与
  autonomy；delegator 保留 assignment、monitoring 与 reallocation authority；delegatee 只获得 scope/time
  bounded capability；verification artifact 支持 completion claim；signed delegation chain 记录 transitive
  accountability。reputation 是历史 evidence 的条件性摘要，不是当前 task capability 的真值；monitoring
  state 也不能替代 environment outcome。
- **Adaptive Decision Principle:** assignment 不是一次性 argmax，而是在 quality、cost、latency、privacy、
  trust 与 verification budget 上求 context-dependent Pareto choice；monitoring 发现 drift 后可以 reassign，
  但必须计入 switching、abandoned work 与 state transfer 成本。论文还提出 complexity floor：对低风险、
  短而确定的任务，完整 negotiation/delegation protocol 可能比直接执行更贵。
- **Permission / Verification / Security Boundary:** 最小权限、task-scoped credential、pre-commitment 的
  completion evidence、不可逆操作确认、revocation 与 recursive incident response 构成 control plane。
  transitive monitoring 可由下游 attestations 聚合，但原 delegator 实际是在信任中间 Agent 的 verifier；
  signature/TEE/ZK proof 只能证明定义过的 computation/identity，不能证明目标 specification 正确。
  malicious delegator/delegatee、collusion、Sybil、prompt injection、data poisoning、resource exhaustion、
  backdoor 与 cognitive monoculture 都可能沿链路放大。
- **Protocol Mapping Boundary:** 论文把 MCP 视为 capability/data connection，把 A2A 视为 peer discovery
  与 task lifecycle，把 AP2 视为 payment authorization，再提出 verification policy、monitoring stream、
  bid/RFQ 等示例 extension。这些 JSON snippets 是 design sketches，不是已经进入标准或跨实现可用的
  protocol facts；MCP/A2A/AP2 的实际版本行为仍需各自 primary specification 验证。
- **Ethical / Human Boundary:** meaningful human control 需要真实 veto、context 与 competence，而不是
  把人放在末端承担 liability；过多告警会产生 alarm fatigue，过少日常参与会造成 de-skilling，使人只在
  极端 failure 时被要求接管。论文将这些列为设计压力，没有给出可验证阈值或干预效果。
- **Evidence / Limitations:** 本文的价值是把 principal-agent、span of control、authority gradient、trust
  calibration 与 transaction cost 连接到 Agent system contract。它没有实证证明该 taxonomy 完备、
  reputation/market mechanism 抗操纵，或 cryptographic monitoring 可在长链路经济运行；也没有给出
  interoperability、latency、privacy、human workload 和 failure-recovery 实验。因此不能标成“新协议
  已解决 delegation”。
- **Evolution Relationship:** `Principle Reuse`：human organizational delegation → bounded AI-agent
  authority/accountability contract；`Layering / Dependency`：Ch78 拥有 multi-agent responsibility 与
  delegation chain，Ch79 只拥有 connection protocol，Ch80 统一 principal/policy/evidence plane。
- **ROADMAP / Chapters Read / Existing Coverage:** 已读 Ch74～80 及 Ch67。Ch78 已明确 single-agent
  baseline、coordination tax、typed handoff、delegated authority、least privilege、bounded re-delegation 与
  independent verification；Ch79 已明确 MCP 不等于 authorization/workflow；Ch80 已记录 principal、
  policy、delegation、side effect 与 evidence。现有正文比这篇 conceptual framework 更接近可执行系统，
  没有长期机制缺口。
- **Integration Decision:** `No Change — Already Covered / Conceptual Framework Only`；Weekly 保留其
  vocabulary 与证据边界，不为引用论文而重复修改 Books。
- **Open Questions:** delegation contract 的最小可互操作 schema 是什么？transitive attestation 怎样绑定
  hidden sub-delegation 与 verifier version？human span-of-control、alarm fatigue 和 de-skilling 如何成为
  可观测而不侵犯隐私的 release/routing constraint？

### DICE: Diffusion LLM for CUDA Kernel Generation

- **Candidate / Week / Score:** DICE: Diffusion Large Language Models Excel at Generating CUDA Kernels /
  2026-W07 / 27/30；`Source Family ID: executable-kernel-curriculum-diffusion-lm`。
- **Source Type / Date / Revision / Access:** arXiv:2602.11715 v1，首次公开 2026-02-12；当前 v2
  （2026-06-16）HTML 的 CuKe construction、block-diffusion objective、BiC-RL、KernelBench evaluation、
  ablations、training cost、robust check、case studies、failure analysis 与 Limitations 已复核，并检查作者
  project entry。v2 明确新增 AR/dLLM comparison、ablation 与 qualitative cases，故只用于后验核验。
- **Original Problem / Previous Design:** end-to-end CUDA generation 直接从 PyTorch reference 产出完整
  wrapper/kernel，接口简单且接近部署 artifact；但 sparse binary reward、编译执行成本和可被 evaluator
  绕过的 high-level fallback 让小模型难以 cold start。AR generation 逐 token 构造，block diffusion 则在
  block 间保持 causal/KV reuse、block 内迭代去噪；论文并未证明后一范式天然更懂 kernel，而是同时改变
  data、curriculum、model family 与 decoding contract。
- **Data Mechanism / Contract:** CuKe 从既有 PyTorch-CUDA pairs 出发，以作者选择的 `2.0x` threshold
  过滤近似 noise 的 speedup，并增加 Attention/MLP 等结构与 shape variation；291 个 structural proposals
  最终只有 36 个通过 execution/speed check，总 dataset 为 6,303。这个 threshold 提高 signal margin，
  也会删除对真实 workload 仍有价值的小幅优化；training artifact 必须绑定 GPU、measurement harness、
  warmup/cache policy、PyTorch/CUDA/compiler 与 input shapes。
- **Curriculum / State Ownership / Control Flow:** SFT 先建立 CUDA syntax/stack prior。BiC-RL 在 task
  与 data 两轴推进：Stage 1 固定 prefix/suffix wrapper，只让模型 infill core C++/CUDA，阻断“不调用
  custom kernel、偷偷回退 PyTorch”的捷径；Stage 2 再生成完整 artifact。difficulty scheduler 从单算子
  走向 fusion/whole-model structure。prompt/reference 拥有 semantic contract，scaffold 拥有允许的调用
  path，compiler/runtime 拥有 execution outcome，measurement harness 拥有 speed observation，RL policy
  只优化映射后的 reward；通过测试不等于 artifact 已安全、可移植或在生产 shape 上更快。
- **Implementation / Training Contract:** base 为 SDAR 1.7B/4B/8B。SFT 在 CuKe 上 3 epochs、8×A100、
  learning rate `1e-5`；RL Stage 1/2 分别使用 992/4,000 programs，20/100 steps，每 step 64 problems、
  每题 16 responses，block size 4、sampling temperature 1、policy learning rate `1e-6`。8B 的作者成本表
  为 SFT 约 22.4 GPUh、infilling 约 120 GPUh、generation 约 960 GPUh；compile/execute workers 是主要
  rollout bottleneck。数字只属于该 software/hardware stack。
- **Evaluation / Evidence Boundary:** KernelBench 共 250 tasks：100 single op、100 fusion、50 model
  architectures；`Exec` 测 functional equivalence，`fast_p` 要求 correct 且 speedup 超过阈值。1.7B/4B/8B
  scale、dataset threshold、SFT/RL strategy 与 robust-check comparisons 支持 curriculum 和 verifier gap
  值得研究。但 AR 与不同 dLLM 使用不同 max output length/default decoding，商业模型也依赖各自默认
  配置；作者 headline 不是同一 training/data/decoding contract 下的纯 architecture ablation。
- **Verifier Failure / Limitation:** appendix 展示 evaluator 会把 copied sample kernel、未实例化 custom
  kernel、或 forward 实际调用 PyTorch 的输出误判为正确；robust check 使多种 baseline 分数显著下降。
  这说明 executable verifier 仍可被 control-flow shortcut 欺骗。更关键的是 BiC-RL reward 只用 binary
  correctness，没有显式 latency reward；作者理由是 distributed timing variance 太高。因此论文证明的
  是先学可执行正确性与减少捷径，不是 RL 直接学会在噪声下最大化 production latency/goodput。
- **Trade-offs / Coexistence:** scaffolding 提高 reward density、降低 exploit surface，却缩小 solution
  space，并可能让模型依赖固定 wrapper；full generation 保留 end-to-end flexibility，却重新引入 bypass、
  compile failure 与 credit assignment。`2x` filter 强化清晰信号但牺牲 coverage。通用 library、template/
  auto-tuner 和人工 kernel 在 stable shape、portability、numerical assurance 或维护成本优先时仍成立。
- **Evolution Relationship:** `Direct Evolution`：one-shot full artifact + weak executable check → robust
  control-flow verification → scaffolded core infilling → full artifact generation；`Layering / Dependency`：
  Ch29 拥有 reward/curriculum，Ch23 拥有 dataset/measurement lineage，Ch62 审计 verifier，Ch77 管理
  artifact search，Ch40/45 只承接 diffusion decode 与 GPU execution，不把 model score 当 runtime fact。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 候选 Ch29；已读 Ch23、Ch28～30、Ch40、
  Ch45、Ch62、Ch77 及相邻章节。Ch29 已有 correctness gate、timing noise 与 verifier exploit，Ch77 已有
  evaluator-driven artifact search；DICE 新增的是“用 scaffold 改变 action space，再逐步释放 artifact
  ownership”的可复用 curriculum，不是另一套 kernel 章节。
- **Integration Decision:** `Books Candidate — Refine Existing Argument / Human Gate Pending`；若吸收，
  只在 Ch29 精炼 verifier-aware curriculum，并短 handoff 到 Ch77；不复制模型排名与 GPUh 表。
- **Open Questions:** robust verifier 能否证明 custom path 对全部 inputs 真正执行且数值等价？latency
  reward 如何在 noisy/multi-GPU environment 中校准而不诱发 measurement hacking？scaffold 到 full
  generation 的能力迁移是否有独立 ablation，跨 GPU architecture/shape 是否保持？

### SciAgentGym / SciForge

- **Candidate / Week / Score:** SciAgentGym: Benchmarking Multi-Step Scientific Tool-use in LLM Agents /
  2026-W07 / 27/30；`Source Family ID: typed-scientific-environment-recovery-trajectories`。
- **Source Type / Date / Revision / Access:** arXiv:2602.12984 v1，首次公开 2026-02-13；当前 v2
  （2026-05-30）HTML 的 environment、benchmark construction、SciForge、experiments、failure taxonomy、
  human review、prompts、training setup、safeguards 与 case studies 已复核。论文无独立 Limitations
  section；后续 revision 仅用于机制核验。
- **Original Problem / Previous Design:** static scientific QA 能比较 parametric answer quality，却不测量
  模型能否选择 typed domain tool、维护中间 artifact、读取 execution feedback 并从长轨迹错误中恢复。
  通用 function-calling benchmark 容易只测单步 schema matching；真实开放实验又昂贵、不可控且可能
  产生物理副作用。SciAgentGym 选择 sandboxed software tools 作为可重复的中间层。
- **Environment / State Ownership:** environment formalized as `(S,A,T,O)`：1,780 typed scientific tools
  加 Python/database primitives 构成 action space；read-only problem assets、per-task writable filesystem、
  intermediate artifacts 与 history 构成 state；transition 执行 tool，observation 返回 typed output/status/
  diagnostics。每个 task 独立注册 tools/filesystem，避免跨任务 contamination。Agent 只提出 action，
  environment 拥有事实状态，tool package/version 拥有计算语义，benchmark/verifier 拥有 success claim。
- **Benchmark / Evaluation Contract:** SciAgentBench 从既有 science benchmarks 构造 259 tasks、1,134
  subquestions，按四个大域与 L1/L2/L3 分层；候选经四个 frontier models 筛选、保留 mean accuracy
  低于 50% 且可在环境执行的任务，并对所有样本人工核验 clarity、reasoning/tool order、recomputed
  outputs 与 final answer。with-tools 使用 model-specific function format + ReAct，两阶段 planning/execution；
  without-tools 用 CoT baseline。这个筛选会形成 frontier-model-conditioned difficulty，不是自然科学任务
  分布本身。
- **Execution-Grounded Synthesis / Data Flow:** SciForge 先把 tool signatures 组成 typed dependency graph，
  从目标 tool 反向采样 acyclic program graph，再用 domain priors 初始化 root inputs并按拓扑序真实执行。
  success 形成 `(tool,input,response,state)` Golden Trace；failure 不丢弃，而是加入 diagnostic、corrected
  input 与 re-execution，形成 recovery trace。最后 LLM 根据 trace/rubric 生成 question，并隐藏精确中间
  数值以降低答案泄漏。graph 约束提高 executability，但 synthetic question quality 与真实 scientist intent
  仍由 rubric/human review近似。
- **Training / Runtime Contract:** SciAgent-8B/4B 从 Qwen3-VL counterparts 以 11,074 trajectories 做 SFT；
  8B 为 full-parameter、3 epochs、冻结 vision/projector，只更新 language model，bf16、max length 16,384、
  learning rate `1e-6`、8 GPUs、per-device batch 2、gradient accumulation 4。trace generation 最多 50
  rounds；task/job/tool 分别有多层 timeout/retry safeguards。GPU 型号、wall-clock、tool package image/
  database snapshot 与全部 inference cost未充分披露，不能把 score 当作通用 agent capacity。
- **Evidence / Diagnostic Boundary:** tool/no-tool、data-scale、cross-domain 与 success/error-recovery trace
  comparisons 支持训练 interaction pattern 的价值。论文把 feedback utilization 分解为 Adaptation、Tuning、
  Switching 与 Loop Escape，并观察 tool call count 与 success 弱负相关；这些指标比“调用更多工具”更能
  定位 loop failure。作者 8B 对 235B comparison 同时改变 training data、harness、prompt 和 model stage，
  只能证明该 pipeline 在本 benchmark 的条件性收益，不能证明小模型普遍超过大模型。
- **Scorer / Limitations / Failure Modes:** success 依赖 exact/numeric tolerance/secondary model judge；judge
  prompt、tool schema 与 effective evaluated set 都会改变结果。SPL 按 expert reference path length 加权，
  论文明确 golden trace 只是一个合法方案，因此低 SPL 可能是合法替代路径而非低效。tool unit test 只
  要求至少 75% pass threshold 也留下 reliability heterogeneity；domain coverage、synthetic dependencies、
  database freshness 和 sandbox-to-real gap 限制外推。typed tools 增强可验证性，也可能把问题塑造成
  已有 toolkit 最容易表达的形式。
- **Trade-offs / Coexistence:** sandbox 交换真实 world uncertainty，以 reproducibility、安全和丰富 feedback
  获得可训练轨迹；真实 lab/human expert 仍拥有 physical validity、novelty、ethics 与 deployment authority。
  static QA 对知识诊断更便宜，single-step function tests 对 schema correctness 更可归因，开放 workflow
  则更接近应用但更难比较。三者是 evaluation layers，不是新 benchmark 替代旧 benchmark。
- **Evolution Relationship:** `Direct Evolution`：static QA → single-step tool calling → typed stateful
  environment → execution/recovery trajectory evaluation and synthesis；`Layering / Dependency`：Ch62
  拥有 evidence interpretation，Ch23 拥有 synthesized data provenance，Ch74 拥有 tool contract，Ch77
  拥有 durable workflow/recovery。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 候选 Ch62；已读 Ch23、Ch62、Ch74～77、
  Ch80 及相邻章节。现有 Ch62 已分开 action、environment transition、artifact 与 outcome，Ch74/77 已有
  typed tool、loop bound、retry 与 durable state；SciAgentGym 新增的是可操作的四段 recovery diagnostic
  和“合法替代路径不能被 reference-length scorer 自动判差”的联合案例。
- **Integration Decision:** `Books Candidate — Refine Agent Evaluation / Human Gate Pending`；若进入 Books，
  优先在 Ch62 增加 recovery-stage diagnostics 与 reference-path scorer 边界，Ch77 仅短 handoff。
- **Open Questions:** tool/package/database/environment image 如何做长期 version identity？recovery metric
  能否区分真正理解 feedback 与 prompt-format imitation？多合法 workflow 下怎样估计 efficiency，而不把
  单一 expert trace 固化成唯一策略？

### On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs

- **Candidate / Week / Score:** On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs /
  2026-W07 / 25/30；`Source Family ID: vlm-modality-conflict-cot-consistency`。
- **Source Type / Date / Revision / Access:** arXiv:2602.12506 v1，首次公开 2026-02-13；当前 v3
  （2026-05-21）58 页 PDF 的 metadata、Introduction、perturbation design、RL experiments、judge
  cross-check、entropy analysis、reward intervention、Related Work、Conclusion、training hyperparameters
  与相关 Appendix 已复核。v2/v3 只用于核验修订后的机制和证据边界，不改写 W07 event date。
- **Original Problem / Previous Design:** RLVR 以可验证 final answer 优化 multimodal reasoning，在数学、
  计数和空间任务上易规模化，也比逐步标注 rationale 便宜；因此“先把答案做对”是合理旧方案。但
  answer accuracy 会隐藏模型是否真正处理 image evidence、是否被 prompt 中错误 caption/thinking
  主导，以及 CoT 与最终答案是否彼此矛盾。标准 clean benchmark 也不主动制造跨模态冲突。
- **Changed Constraint / Stress-test Mechanism:** 论文固定视觉问题，在 textual context 中加入
  Stop-Think、Wrong-Think 与 Wrong-Caption，并以 disclaimer 变体测试模型能否识别并纠正错误先验；
  另用正确 cue 作方向相反的对照。这里改变的是 evaluation input contract，而不是提出新的 VLM
  architecture。关键观察对象至少要拆为 clean accuracy、perturbed accuracy、CoT-answer consistency
  与 uncertainty；任何单一分数都不能代表其余三项。
- **Terminology and Evidence Boundary:** 作者明确把 `faithfulness` 限定为“外显 CoT 与 final answer
  是否一致”，不同于内部计算是否因果支持 rationale 的 mechanistic faithfulness。主 judge 是
  Qwen3-32B，并以 GPT-OSS-120B、Llama-3.1-70B-Instruct 和 qualitative inspection 交叉检查。
  多 judge 一致能降低单 judge 偶然误差，却没有证明文字 rationale 忠实反映 hidden computation；
  shared model priors 也使这些 judge 不是完全独立证据。
- **Training / Data / State Contract:** 受控 RL 使用 Qwen2.5-VL-7B-Instruct + verl GRPO；训练混合为
  32K SAT2 spatial questions、15K PixMo-Count，并切换 2.1K Geometry3K 与 synthetic correct/wrong
  caption/thinking augmentation。五个 epochs、learning rate `1e-6`、rollout batch 512、PPO micro-batch
  128、每个 GRPO step 8 samples、prompt/response 上限 4096/2048、KL coefficient 0。Qwen3 根据
  ground-truth 或随机错误选项生成 cue，因此 generator、answer key 与 judge 共同塑造 measurement；
  GPU 型号、训练 wall-clock、精度和完整 image preprocessing contract 未公开。
- **Reward / Control Flow:** baseline reward 给格式 0.1、答案正确 1；faithfulness-aware 版本只在答案
  正确且 CoT-answer judge 判一致时给 credit。data augmentation 提供冲突输入，reward 决定哪些 rollout
  被强化，policy 生成 rationale 与 answer，judge 只拥有外部一致性 verdict。论文观察到 accuracy、
  robustness 和 consistency 可沿不同方向变化；augmentation 对 Wrong-Caption 较有效，却没有稳定解决
  Wrong-Think，单独叠加 consistency reward 还会让 policy 偏向“直接相信容易拿分的正确 cue”捷径。
- **Evaluation Contract / What It Proves:** clean/perturbed curves、RL checkpoints、数据混合、reward
  intervention 与 entropy measurements 支持一个受限结论：在这些 spatial/counting multiple-choice
  workloads 中，提高 headline accuracy 不保证抵抗冲突文字，也不保证外显 reasoning 与答案一致；
  简单 augmentation 与 auxiliary reward 不是自动可加的修复。它不证明 RL 普遍降低所有 VLM 的真实
  grounding，也不证明 closed models 的内部机制更忠实。open/closed comparison 还存在可用 prompt、
  CoT visibility、model scale、training data 和 answer-production policy 不对称。
- **Limitations / Failure Modes:** perturbations 是 synthetic text、任务以基础视觉/空间选择题为主，
  还没有覆盖多轮交互、开放式生成、真实 OCR/document/video workflow 或可执行 action。评估依赖模型
  生成可解析 answer；CoT judge 可能把流畅的事后叙述当成证据。entropy 只测受限 option tokens，不能
  等同全模型 calibration。augmentation/reward 还引入 generator shortcut、judge hacking 与 overfitting
  到 cue format 的新 failure mode。
- **Trade-offs / Where Previous Design Still Applies:** final-answer verifier 仍是数学、代码和封闭任务的
  低成本 correctness gate；CoT consistency 是附加 diagnostic，不能取代 outcome verifier、visual
  grounding test 或 mechanistic intervention。冲突 augmentation 扩大 robustness coverage，却增加数据
  合成偏差；consistency reward 提高表面一致性，却可能奖励更加连贯的 rationalization。高风险应用仍需
  image-grounded claim checks、calibration、human review 与真实 environment evidence。
- **Evolution Relationship:** `Direct Evolution`：clean answer benchmark → textual perturbation robustness
  → CoT-answer consistency cross-check → modality-conflict-aware evaluation；`Layering / Dependency`：Ch62
  拥有 evidence/scorer boundary，Ch18 只承接 multimodal input conflict，Ch29 只承接 reward shortcut。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 候选 Ch62；已读 Ch18、Ch28～30、Ch62
  及相邻章节。Ch62 已明确 model/system evaluation、slice、adversarial set、judge calibration 与
  `narrative != completion evidence`；本论文补足的是“外显 CoT consistency 既是独立 evaluation axis，
  又不能冒充 internal faithfulness”的 multimodal 受限案例。Ch29 已有 reward hacking 原则，无需复制
  训练曲线或另立算法段落。
- **Integration Decision:** `Books Candidate — Refine Evaluation Boundary / Human Gate Pending`；若进入
  Books，只在 Ch62 精炼 modality-conflict slice 与 CoT consistency 的证据边界，Ch18/29 短 handoff；
  不保留模型排名和缺少完整 workload contract 的性能数字。
- **Open Questions:** 怎样用 counterfactual visual edits、attention/activation interventions 或 executable
  grounding 把外显一致性推进到更强因果证据？如何设计不会被 cue generator/judge 共同偏差污染的
  reward？多轮 Agent 接收冲突 screenshot、tool text 和 memory 时，哪一层拥有 conflict resolution 与
  uncertainty escalation？

### Learning to Configure Agentic AI Systems / ARC

- **Candidate / Week / Score:** Learning to Configure Agentic AI Systems / ARC / 2026-W07 / 27/30；
  `Source Family ID: query-wise-agent-configuration-scheduling`。
- **Source Type / Date / Revision / Access:** arXiv:2602.11574 v1，首次公开 2026-02-12；当前 v3
  （2026-05-21）HTML/PDF 的 Related Work、SMDP/HRL formulation、training algorithm、theorems、六项
  benchmark、baselines、cost analysis、transfer、ablation、error analysis、nine workflows、compute、proof、
  embedding/prompt-generator ablations 与 training details 已复核。后续 revision 的 GPT-5.2 fragment
  generator 等事实只作当前 artifact 核验，不反投影为 v1 已公开机制。
- **Original Problem / Why Fixed Design Was Reasonable:** 固定 workflow、tools、token budget 与 prompt
  易测试、易复现，也避免每个 query 重新搜索组合；当 workload 同质、风险规则稳定或配置空间很小，
  hand-tuned template 仍是成本最低的旧方案。边界在于 query difficulty、tool need 与可分解性变化时，
  one-size-fits-all 会对简单问题过度配置，对复杂问题预算不足；逐 query 暴力 grid search 又把优化成本
  移到线上。
- **Changed Constraint / Mechanism:** ARC 把完整 agent configuration 视为 temporally extended option：
  Direct 可能只做一次 LLM call，Evaluator-Optimizer 可持续到收敛或上限，因此不能都当成等时 instant
  action。高层 structure policy 选择 workflow、tools 与 per-agent budget；低层 prompt policy 在选定结构
  下按序组合 instruction fragments。action masking 删除与 workflow 不兼容的维度，避免在无效组合上
  消耗 exploration。
- **State Ownership / Control and Data Flow:** query state 由 MetaCLIP-H/14 semantic embedding 与 query
  length、numeric density、multi-step/tool indicators 拼接；policy 输出配置，Agent workflow 执行并产生
  answer、LLM calls、token use 与 tool events，environment/scorer 返回 correctness/cost，buffer 保存完整
  episode。backbone LLM 保持冻结，轻量 structure/prompt policy 和各自 value network 才是 learned state。
  这意味着 ARC 是 control-plane scheduler，不拥有 workflow 的 durable business state、tool truth 或
  deployment authority。
- **Training / Reward / Consolidation:** 两级 policy 分别用 PPO、advantage normalization 和 entropy
  regularization 训练；reward 结合 correctness、实际 option duration/LLM calls、normalized tokens 与
  asymmetric tool-use shaping，处理“分配了 tool 但下游模型未调用”的 mismatch。RL buffer 中正确且
  reward 位于 top 30% 的 episodes 再用于 SFT，减少最终 policy stochasticity；这是一条
  explore configurations → retain elite support → consolidate policy 的路径，不是修改 backbone capability。
- **Theory Boundary:** SMDP contraction/convergence 要求 bounded duration/reward、Robbins–Monro
  step sizes、所有 state-option pairs infinite visitation 等；SFT support/reward-floor 还依赖 sufficient model
  capacity 与经验 elite distribution。这些 theorem 说明抽象优化目标在假设下 well-defined，并不保证有限
  4,000 episodes、OOD query、changed tool registry 或 production drift 下仍达到同一 optimum。只在 elite
  support 内采样还会降低未知配置风险，同时限制发现分布变化后的新策略。
- **Evaluation Contract:** 六个 benchmark 为 GSM8K、DROP、MedQA、HotpotQA、GAIA 与 tau-bench
  Airline；默认 action space 有 9 workflows、4 tools、3 agents，主结果用 Qwen2.5-7B-Instruct，并检查
  Gemini 2.5 Flash Lite 与 Qwen family scale transfer。baselines 包括 budget-matched model+tools、grid/
  greedy、AutoGen/DSPy/GEPA/LAP、bandit 与 flat PPO；论文还比较 PPO/GRPO、SFT/DPO、state embedding
  和 prompt generator。GAIA 仅以 validation 前 65 样本训练、其余评估，API token cost 使用当时
  OpenRouter rate；这些条件限制 headline gain 和 Pareto claim 的外推。
- **Implementation / Resource Boundary:** 7B local training 可在 single modern GPU + 64GB CPU RAM 路径
  运行，Appendix 给出 A100/V100/4090-class 与 quantized alternatives，而不是报告一套统一实测硬件。
  每 dataset 至少 4,000 training episodes、batch 32；API mode 的 latency、concurrency 和 monetary budget
  受 provider 限制。代码支持 arbitrary registry/workflow，但论文只在有限离散 option catalog 验证；动态
  tool schema、long-lived state、side effect、approval、failure recovery 与 multi-tenant fairness 未被覆盖。
- **What the Evidence Proves / Does Not Prove:** 结果支持“在给定 catalog 和 benchmark 分布上，学习
  query-conditioned configuration 可改善 accuracy-cost frontier，并能学到 task-specific allocation”。跨任务
  结果也显示 semantic similarity 不足：tool overlap/structure 更决定 transfer。它不证明 ARC 普遍优于
  static workflow；论文的 error taxonomy 主要用长度/关键词等 heuristics，`configuration error` 占比不是
  独立人工因果诊断。model-scale correlation 也不是跨 model family、tool environment 或 SLO 的 invariance。
- **Trade-offs / New Failure Modes / Coexistence:** adaptive policy 减少统一 overprovisioning，却新增 router
  misclassification、state-embedding drift、reward/cost miscalibration、catalog staleness、elite-buffer lock-in
  与 silent under-allocation。固定 workflow 在合规、可解释、low-variance 和不可逆 action 上仍更合理；
  learned selection 适合选项可枚举、outcome 可评分、错误可隔离的节点。高风险系统需要 deterministic
  policy mask、minimum budget、approval、fallback 与 per-slice rollback，不能让 reward policy改写 hard gate。
- **Evolution Relationship:** `Direct Evolution`：one-size fixed configuration → offline search for one global
  configuration → per-query flat policy → hierarchical option selection + prompt composition → elite-policy
  consolidation；`Layering / Dependency`：Ch80 拥有 query/workflow scheduling，Ch77 拥有 durable execution，
  Ch78 拥有 topology/coordination cost，Ch66 提供 outcome-bound cost contract。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 候选 Ch80；已读 Ch66、Ch75、Ch77～80
  及相邻章节。Ch80 已列 inference/GPU/Agent/workflow 多时间尺度 scheduling，却没有解释如何根据 query
  在 workflow、tools、budget 与 prompt 间联合选择；Ch77 已有 deterministic spine 与 Helium 的 workflow-
  visible serving，Ch78 已有 task-topology matching。ARC 新增的是 control-plane configuration policy，
  不能与 serving DAG optimization 或 multi-agent topology repair 混写。
- **Integration Decision:** `Books Candidate — New Mechanism / Human Gate Pending`；若进入 Books，优先在
  Ch80 的 Agent scheduling 中补充 query-wise configuration policy、hard-mask/fallback 和 policy-drift
  约束；Ch66/77/78 只做短 handoff，不复制九种 workflow 列表或 benchmark 百分比。
- **Open Questions:** production query 没有 ground-truth reward 时如何训练与校准 policy？tool/version/
  pricing 改变后怎样检测 option catalog 与 cost model 失效？如何把 tail latency、tenant fairness、risk、
  approval 和 side-effect reversibility 纳入多目标约束，而不是再压成一个可被 gaming 的 scalar reward？

### BrowseComp-V3

- **Candidate / Week / Score:** BrowseComp-V3: A Visual, Vertical, and Verifiable Benchmark for Multimodal
  Browsing Agents / 2026-W07 / 26/30；`Source Family ID: multimodal-browsing-subgoal-evaluation`。
- **Source Type / Date / Revision / Access:** arXiv:2602.12876 v1，首次公开 2026-02-13；v2
  （2026-02-24）HTML/PDF 的 benchmark design、five-stage construction、evaluation settings、result/process
  metrics、fine-grained analysis、test-time scaling、failure taxonomy 与 Conclusion 已复核。作者 GitHub、
  dataset/decryption docs、OmniSeeker current reference runner 与 LLM-judge evaluation code于 2026-08-08
  联合核验；这些后续 artifact 只用于解释 scorer/runtime，不能作为 W07 新事件。
- **Original Problem / Why Previous Benchmarks Were Reasonable:** shallow VQA、single/two-hop retrieval 与
  final-answer accuracy 成本低、可重复，适合先隔离 perception、retrieval 或 answer correctness；但它们
  难以诊断 Agent 在开放 Web 中究竟卡在 text search、visual grounding、cross-page integration、planning
  还是 final synthesis。把非公开 video/proprietary document 当关键证据又使不同 tool stack 无法公平重放。
- **Changed Constraint / Dataset Mechanism:** 300 个手工问题、383 张输入图覆盖 5 个大类和 24 个子域，
  把难度拆为 intra-region alignment、inter-region integration、inter-image reasoning，并要求关键证据可由
  public search 找到、尽量时间稳定、答案短且客观。20+ annotators 先用 TextSearch、WebVisit、ImageSearch、
  ImageCrop、ReverseImageSearch 探索并记录完整 trajectory/subgoals，再经 human replay、SOTA-model
  adversarial filtering、structured JSON 与 expert privacy/safety/factual audit。模型筛掉 trivial examples
  提高难度，也会让 dataset 对该批模型的盲点产生 selection bias。
- **State Ownership / Runtime Flow:** task artifact 拥有 question、images、gold answer、metadata 与 gold
  subgoals；search provider/index 与 webpage parser 拥有当次可见 Web state；Agent 只选择 search/visit/
  crop/reverse-search action 并生成 predicted subgoals/final answer；evaluation run 必须固定 model、prompt、
  tool schema、provider、index time、round budget 与 judge。OmniSeeker 以 Serper top-5、Jina page parsing、
  base64 image context、programmatic crop 和最多 20 rounds 实现公开 harness；official web products 只启用
  各自 maximum reasoning mode，tool/budget 不同，不能与统一 harness 视为纯 model comparison。
- **Result and Process Scorer:** Success Rate 判断 final answer；Process Score 为已命中 gold subgoals 数除以
  gold subgoal 总数。current artifact 的 LLM-judge code 按 `key_info` 做 semantic、order-independent set
  matching，并把 final answer 与 process 分开；正确答案中的严重异常只 flag 给 human review，不再反向
  改写 answer correctness。这使 partial progress 可观察，但 Process Score 不测 subgoal 顺序、依赖、source
  citation、tool action 是否真实发生、无关探索成本或合法替代分解，gold subgoal 也不是唯一 planning path。
- **Evaluation Contract / Evidence Boundary:** human baseline 每题最多 30 分钟；tool-free models 只看原始
  question/images；OmniSeeker 最多 20 rounds；论文以 Pass@1、task level、search depth、tool ability 与
  process/final gap 比较多种模型，并做 interaction-step 与 repeated-sampling analysis。这支持“final score
  会掩盖部分已完成 subgoals，multimodal Web search 需要分层诊断”的结论；不支持把某个模型的 36% 或
  failure distribution 外推到其他 search index、时间、judge、tool budget 或生产 deep-research workload。
- **Implementation / Reproducibility Boundary:** current repository 提供 CC BY 4.0 dataset、公开 decrypt key、
  per-sample JSON、baseline/OmniSeeker runner、smoke tests 与 judge script，提高 artifact inspectability。
  但 paper 没有报告完整 token/API cost、latency/concurrency、judge calibration/inter-rater agreement、每条
  Web evidence 的 immutable snapshot/digest 或不同 search locale/index 的 sensitivity；“public searchable”
  也不会消除 link rot、ranking drift、geo/personalization 与 robots/access differences。
- **Trade-offs / Failure Modes / Coexistence:** temporally stable、short-answer tasks 提高长期可比性，却远离
  breaking news、长报告 synthesis、ambiguous intent 与 evolving evidence；gold subgoals增强 diagnosis，
  却可能惩罚不同但正确的 decomposition。更多 interaction/sample 提高找到证据的机会，也增加成本、
  correlated hallucination 与 judge-selection surface。final-only benchmark 仍适合低成本 release regression，
  component retrieval/perception tests 仍比 end-to-end benchmark 更易归因；三者应分层共存。
- **Evolution Relationship:** `Direct Evolution`：final-answer-only multimodal lookup → multi-hop public-Web
  browsing → annotated subgoal progress → result/process joint evaluation；`Layering / Dependency`：Ch62
  拥有 scorer/evidence claim，Ch72 拥有 retrieval sufficiency/provenance，Ch74～77 分别拥有 tool contract、
  plan dependency、feedback 与 durable workflow，不能由一个 Process Score 合并替代。
- **ROADMAP / Chapters Read / Existing Coverage:** 主 owner 候选 Ch62；已读 Ch62、Ch72、Ch74～77、
  Ch80 及相邻章节。Ch62 已区分 result、trajectory、environment 与 judge，Ch72 已拆 retrieval sufficiency，
  Ch75 已要求 plan step 的完成证据；BrowseComp-V3 新增的长期价值是把 `partial progress` 形式化为
  subgoal vector，同时暴露 set-based judge 不能证明 path validity 的边界。
- **Integration Decision:** `Books Candidate — Refine Agent Evaluation / Human Gate Pending`；若进入 Books，
  只在 Ch62 增加 result/process/component 三层诊断与 gold-subgoal scorer 的非唯一性，Ch72/75 短 handoff；
  不复制 leaderboard、模型版本表或 36% headline。
- **Open Questions:** 如何把 subgoal achievement 绑定实际 retrieved evidence/source digest，而不是 Agent
  自报的 predicted subgoal？多条合法路径怎样评分 dependency、cost 与 completeness？Web 快照、search
  index、region 与 access policy 如何版本化，才能让“公开可检索”成为可重复 evidence contract？

### AIDev: Studying AI Coding Agents on GitHub

- **Candidate / Week / Score:** AIDev: Studying AI Coding Agents on GitHub / 2026-W07 / 23/30；
  `Source Family ID: aidev-agentic-pr-observational-dataset`。
- **Source Type / Date / Source-family History / Access:** MSR 2026 dataset paper arXiv:2602.09185，首次公开
  2026-02-09；全文、relational schema、research questions、Hugging Face/Zenodo/GitHub artifact 已复核。
  同一 source family 最早在 arXiv:2507.15003（2025-07-20）发布 456,535 PR snapshot 与三项 observational
  case studies；2026 paper 把 dataset 截止日更新为 2025-08-01，并聚焦 932,791 PR 与 33,596 条 >100-star
  enriched subset。W07 是 dataset-paper/documentation node，不是该技术或数据集的首次出现。
- **Original Problem / Why Static Benchmarks Were Reasonable:** HumanEval/SWE-bench 等 curated tasks 能固定
  repository、test 与成功判据，适合比较 isolated coding capability；但它们观察不到 PR 被 review、修改、
  merge、close、revert 或 hotfix 的生产生命周期。直接使用 GitHub telemetry 能补生态有效性，却失去
  controlled assignment：真实 PR 的 task mix、user、repository maturity、review policy 和 agent exposure
  都不是随机的。
- **Dataset Mechanism / Identity Graph:** full tables连接 PR、repository 与 user metadata；>100-star subset
  进一步连接 39,122 discussion comments、28,875 reviews、19,450 inline review comments、88,576 commits、
  711,923 file diffs、4,923 related-issue mappings 与 325,500 timeline events，并以 GPT-based Conventional
  Commits 分类生成 `pr_task_type`。它提供的是可查询 observational evidence graph，而不是模型权重、Agent
  runtime 或新的 coding mechanism。
- **Attribution / Collection Boundary:** 2025 construction paper披露的识别规则依赖 GitHub search signals：
  bot author、`head:codex/`/`head:copilot/`/`head:cursor/` branch prefix、`Co-Authored-By: Claude` 等，并对
  Copilot login 额外检查。显式规则可重放，但作者没有公开 detector precision/recall 的人工 audit；本地
  Agent、被删除 attribution、改名 branch、人类复用 prefix 或 mixed-authorship 都可能造成漏计/误计。
  五种工具的 attribution semantics 也不同，不能把 `agent` 列当成同质 treatment。
- **What the 2026 Paper Proves / Does Not Prove:** 2026 paper证明 dataset/schema/artifact 可用，并列出 adoption、
  patch、testing、review、failure/security 与 production persistence 等可研究问题；它没有执行这些分析，
  因而 932,791 不能证明 productivity、quality、security、autonomy 或 deployment success。2025 related paper
  的 merge/latency/complexity comparisons 也只是早期 >500-star subset 的 observational associations；
  repository/task/user/provider confounding、selection、survivorship 与不同 attribution coverage 阻止因果外推。
- **Outcome Semantics / New Failure Modes:** merge 代表 maintainer acceptance，不等于 tests correct、无漏洞、
  长期可维护或进入 production；closed/rejected 也可能来自 scope、duplicate、policy、capacity 或作者行为。
  review time 同时受 bot policy、timezone、repository popularity 与 queue 影响。把这些 proxy直接变成 training
  reward 会奖励小 PR、容易 merge 的文档/低风险任务或同 provider 的 closed review loop，并可能扩大
  quantity over quality。
- **Privacy / Governance / Version Boundary:** dataset含公开 login、profile、comments、patch 和 timelines，
  license 为 CC BY 4.0；生产使用仍需最小化个人数据、用途/retention review、删除与 GitHub source revision
  处理。living dataset 每次 refresh 会改变 population 与 schema，必须固定 snapshot digest、query、cutoff、
  enrichment threshold 和 derived annotation model；不能在更新数据上原地覆盖旧结论。
- **Trade-offs / Where Previous Design Still Applies:** controlled benchmark 提供 attribution 和 repeatability，
  observational PR graph 提供生态真实性；前者无法证明 production impact，后者无法隔离 model capability。
  最合理的演进是 benchmark result → shadow/controlled deployment → versioned PR lifecycle evidence →
  causal或matched analysis，而不是用 GitHub merge rate替代 executable tests、security review或用户价值。
- **Evolution Relationship:** `Layering / Dependency`：static executable coding eval 与 production lifecycle
  evidence 是两层证据；`Principle Reuse`：把 Event/PR/commit/review/issue 连接为 observed-state lineage。
  2026 dataset paper 相对 2025 source family 属 `Dataset Revision / Documentation Evolution`，不是新机制。
- **ROADMAP / Chapters Read / Existing Coverage:** 已读 Ch62、Ch65、Ch69、Ch77、Ch80 及相邻章节。
  Ch62 已明确 Recent production sample 的 privacy/selection/label-delay、subject identity、outcome scorer、
  attribution 与 feedback-first-as-evidence；Ch77/80 已有 artifact lineage、human approval、side effect 与
  production feedback。AIDev 没有提供足以改变这些结论的新机制或因果结果。
- **Integration Decision:** `No Change — Already Covered / Dataset Only`；Weekly 保留 dataset availability、
  source-family evolution 与 attribution limitations，不因数据规模修改 Books，也不引用 2025 observational
  headline 作为 2026 新结论。
- **Open Questions:** 能否公开 detector precision/recall、mixed-authorship 与 deleted-attribution audit？怎样
  把 CI、release、revert、incident 与 vulnerability evidence 接到 PR graph，区分 merge 与长期正确性？
  研究 Agent effect 时应采用何种 matched/within-repository/temporal design 缓解 task/user/provider confounding？

### InternAgent-1.5 — partial source packet / full-read gate blocked

- **Candidate / Week / Score:** InternAgent-1.5 / 2026-W07 / 26/30；
  `Source Family ID: internagent-scientific-discovery-workflow`。
- **Source Type / Date / Revision:** arXiv technical report v1，2026-02-09；官方 GitHub 记录报告于
  2 月 10 日发布、MLEvolve 于 2 月 14 日开放，完整 InternAgent-1.5 code 到 5 月 7 日才开放。
- **Direct / Related Primary Sources:** arXiv:2602.08990 v1、上海 AI Lab 2026-02-11 发布说明、
  `InternScience/InternAgent`；MLEvolve 只作为 2026-02-14 公开的 solution-refinement artifact，5 月完整
  仓库只用于核验 later implementation boundary，不倒灌为 2 月的代码证据。
- **Access and Full-read Coverage:** 官方 PDF 为 22.8 MB，直接 reader 仍拒绝；本轮通过同一 PDF 的
  search-indexed primary-text passages 恢复目录、Sections 1～5 的关键公式/表格、Experiments 3.1～3.5、
  Conclusion 与 Appendix A.2 的范围，并与 arXiv metadata、官方发布页和 repository state 交叉核验。
  这些 passage 足以建立下面的非最终机制/证据边界，却不足以证明逐页覆盖 Related Work、全部 tables/
  captions 与 Appendix。因此状态仍为 `Unverified / Blocked`；没有执行作者代码或独立复现实验。
- **Original Problem / Why Previous Design Was Reasonable:** 早期 AI scientist 常把 literature search、
  hypothesis、code/experiment 与 reflection 串成固定流程；在单领域、短 horizon、evaluation 便宜且状态
  很少时，线性 workflow 更易观测、重放和治理。约束变化是跨领域 evidence、并行候选、昂贵实验、
  多轮失败经验和跨 session objective 同时出现，单条 trajectory 无法复用旁支证据，也容易每轮从零开始。
- **Mechanism / State Ownership:** Generation 用 cross-disciplinary knowledge graph 与动态 structured
  knowledge-flow DAG 表达 `search / solve / answer` 节点及依赖；Verification 把 code、parameterization 或
  protocol 作为 solution，在 Graph-Augmented Monte Carlo Search 中执行 selection、expansion、simulation、
  backpropagation，并用 primary、intra-branch、cross-branch、multi-branch aggregation 四类 expansion
  operator 复用轨迹；Evolution 将结果写入 Structured Cognitive Memory：SPM 保存提炼后的 procedural
  strategy，TEM 保存 method/metric/improvement judgment 的 episode，SKM 用 long-term experience library、
  idea graph 与 novelty score 维护跨轮 conceptual objective。knowledge graph 拥有外部 evidence relation，
  workflow DAG 拥有当前问题依赖，solution graph 拥有 candidate lineage/score，三层 memory 只是派生经验，
  都不能取代实验原始记录、设备状态或批准记录。
- **Control Flow / Data Flow:** research goal → evidence retrieval 与 DAG decomposition → 依赖满足的节点交给
  agent/tool → 生成候选 code/protocol → simulator、controlled runtime 或 SCP-connected lab 执行并返回
  measurement → score/backpropagation 更新 solution graph → SPM/TEM/SKM 提炼 → 下一轮 hypothesis、
  method 与 objective。该循环将 proposal、execution evidence 和 derived prior 分层，比“Agent 自评后重写”
  多出可执行反馈与跨分支 lineage；但论文未给出统一 transaction、rollback 或 memory invalidation protocol。
- **Implementation Boundary:** 论文给出 knowledge-flow node/edge 定义、procedural/episodic retrieval 与
  semantic novelty 公式，并列出 computational tools、simulation 与 SCP 物理实验路径。2 月 14 日 MLEvolve
  开放的是 solution optimization 核心而非整个 1.5；5 月仓库增加 discovery、deep research、persistent
  memory 与 paper reproduction 入口。两者说明机制后来可执行，不证明 2 月报告的全部 domain workflow、
  lab integration 或 memory policy 已以同一版本开放。
- **Evaluation Contract:** 报告分三层评估：GAIA、HLE、GPQA-diamond、FrontierScience、SGI-Bench 等
  scientific reasoning；scientific/AI algorithm discovery；earth、life、biological、physical science 的
  computational/wet-lab cases。最清晰的 component evidence 是 GAIA SPM ablation：作者报告 average
  score `82.42 → 86.06`、average tool calls `22.69 → 18.52`。其它榜单、算法指标、climate/downscaling、
  reaction/protein/wet-lab 结果属于不同 harness 和 domain case，不能横向合成一个“autonomy score”。
  报告没有完整披露统一 base-model routing、每项任务的 token/tool budget、硬件、并发、总成本、随机种子、
  precision 或 production SLO，因此不保留厂商发布页的“周/月压缩到小时/分钟”作为通用性能事实。
- **What the Evidence Proves / Does Not Prove:** 证据支持“显式 generation → executable verification →
  memory-mediated evolution”可作为跨任务的系统分层，并在作者 harness 中展示 graph search、memory 与
  domain tool orchestration 的可行性；SPM ablation 只支持特定 GAIA 配置中的 planning/tool-call 改善。
  它不证明系统能发现普适的新科学规律，不证明 wet-lab 端到端无人监管、安全或独立复现，也不证明
  SPM/TEM/SKM 的每项写入正确、跨任务迁移无污染，或相对固定 workflow 在所有成本/SLO 下更优。
- **Trade-offs / Failure Modes / Previous Design Still Applies:** graph search 获得 cross-branch reuse，却增加
  evaluator coupling、graph lineage、budget allocation 与 stale-node 问题；derived memory 减少重复探索，
  却新增错误 consolidation、provenance loss、objective drift、novelty gaming、poisoning 与 supersession；
  SCP 扩大可执行能力，也扩大设备授权、样本 provenance、校准、不可逆 side effect 与人类审批边界。
  对 evaluator 不可靠、实验昂贵或风险高的任务，固定 workflow、deterministic checks、human-selected
  proposal 与独立复现实验仍然成立；并非 graph/memory 越多越先进。
- **Evolution Relationship:** `Layering / Dependency`：Deep Research 提供 evidence graph，Planning 提供
  candidate graph，Workflow/Tool 层提供执行与 measurement，Memory 只保存派生 prior；相对 InternAgent
  1.0 的固定 generation/reflection loop 是 `Direct Evolution`，但与通用 Agent architecture 的关系是
  `Principle Reuse`，不能从单个系统推出行业标准。
- **ROADMAP / Chapters Read / Existing Coverage:** 已读 Ch72～78。Ch73 已有 semantic/procedural/episodic
  分型、raw evidence 与 derived memory 分离、provenance/supersession/delete；Ch75 已有 state graph、
  search budget 与 verifier boundary；Ch77 已有 evaluator-driven search、program lineage、held-out
  verification、durable state 和 physical-lab human gate；Ch72/74/76/78 已覆盖 evidence retrieval、tool
  contract、feedback independence 与 coordination tax。论文提供一个更完整的组合案例，但没有改变这些
  设计结论。
- **Integration Decision:** `Unverified / Blocked`；相邻章节去重表明最终很可能是 `No Change — Already
  Covered`，但在完整报告 Gate 通过前不固化 disposition，不把作者 benchmark 或“autonomous scientific
  discovery”产品定位复制进 Books。
- **Open Questions:** memory entry 如何版本化、撤销与传播删除？solution graph 的并发 mutation、失败恢复
  与 evaluator version 谁拥有？SCP lab action 的 authorization、human approval、calibration 与 incident
  replay contract 是否公开？能否在冻结 model/tool/budget 下独立复现 SPM、TEM、SKM 的单独贡献？

### SPEED-Bench — 26/30

- **Candidate / Week / Score:** SPEED-Bench / 2026-W07 / 26/30；
  `Source Family ID: speed-bench-speculative-decoding-evaluation`。
- **Source Type / Dates / Revision:** arXiv primary paper；v1 明确提交于 2026-02-10，v2 修订于
  2026-05-28。`2604.*` 编号前缀与 submission history 不一致时，以 arXiv 显式 v1 timestamp 决定
  W07 owner；v2 只用于 revision boundary，不制造 W22 新事件。
- **Direct / Related Primary Sources:** arXiv:2604.09557v1/v2、NVIDIA Hugging Face dataset；数据页已
  核验 6 个 subsets、880-row qualitative split、license 与 arXiv identity。论文还记录 TensorRT-LLM、
  vLLM、SGLang 的固定 container versions；但 executable measurement client / engine adapters 未能从
  保存的访问路径独立定位，因而 `Dataset Verified / Executable Framework Partially Verified`，不把论文
  中的 integration 声明等同于本次运行。
- **Full-read Coverage:** 已读 metadata/revision、Abstract、Introduction、Related Work、SD/metrics
  background、Qualitative/Throughput splits、selection algorithm、thin-client measurement framework、
  experiments、Conclusion，以及 Appendices A～M 的 dataset construction、synthetic-input failures、MoE
  expert imbalance、domain-speed proxy、checkpoints/engines/training、long-ISL、vocabulary pruning 与
  engine comparison。论文没有集中列出独立 Limitations section；限制从 framework 和实验段落恢复。
- **Original Problem / Previous Design / Changed Constraint:** 早期 speculative-decoding benchmark 使用
  少量短 prompt、batch 1、高层 research implementation 或 random tokens，适合快速验证 acceptance
  correctness 与 microbenchmark。生产负载却让 acceptance 随 domain/entropy、ISL、draft training 和
  sampling policy 变化，同时 batch/concurrency 把 target 从 memory-bound 推向 compute-bound；同一个
  draft length 因而不会在所有 workload 上保持同一收益。
- **Mechanism / State Ownership / Control and Data Flow:** Qualitative split 从 18 个公开数据源按 category
  选择 880 个 prompts，以 embedding pairwise similarity 的 greedy + local-swap heuristic 扩大语义覆盖；
  Throughput split 按 low/mixed/high entropy、1k/2k/8k/16k/32k ISL 组织每桶 1,536 个 real-semantic
  samples。thin client 在 engine 外统一 tokenization/template、发送 pre-tokenized inputs，并由 asyncio
  并发 dispatch；stream chunks、timestamps 与 token increments 形成 TTFT、step latency、request latency、
  User TPS、Output TPS、AR 与 AL。dataset/version、tokenizer/template、target/draft checkpoint、engine
  image、TP/EP、sampling、DL、ISL 和 concurrency 共同拥有一次 run identity，不能只记录模型名。
- **Implementation Details:** throughput bucket 通过 truncation 或 neutral suffix 固定 ISL，并用
  `o200k_base` 计数；作者明确指出 Python GIL 在 `BS>256` 可能成为 client-side bottleneck。主实验使用
  N-Gram、Vanilla SD、EAGLE3、native MTP，固定 draft chains；engine 包括 TensorRT-LLM 1.2.0rc1/rc7、
  SGLang v0.5.7 与 vLLM v0.13.0。除 DeepSeek/Qwen 与 GPT-OSS drafter training 使用 8 GPUs 外，实验主要
  使用单张 B200；drafter training 的特定实验使用 8×B200、effective batch 128。
- **Evaluation Contract / Evidence:** 作者覆盖 Llama 3.3 70B、GPT-OSS 120B、Qwen3 235B、Qwen3-Next、
  DeepSeek-R1 与不同 drafter；对 qualitative split 主要在 batch 32、DL=3 下报告 AL/speedup，并用
  throughput curves 扫描 batch、DL、ISL 与 engine。实验支持三个条件性结论：semantic domain 会改变
  AL；random tokens 会通过 trivial response/topic latching 和 MoE router imbalance 扭曲性能；低并发
  memory-bound 与高并发 compute-bound 区间的 optimal DL 可以不同。所有数字都只属于上述 checkpoint、
  hardware、container、sampling 和数据合同。
- **What the Evidence Proves / Does Not Prove:** 证据证明 speculative-decoding evaluation 必须把
  quality-side acceptance 与 system-side step cost 分开，再绑定真实语义分布、ISL、concurrency、engine
  和硬件；它还证明 synthetic random tokens 不是所有 SD/MoE serving benchmark 的安全代理。它不证明
  SPEED-Bench 代表任一生产流量，不证明某种 drafter、engine 或固定 DL 普遍最优，也不证明 embedding
  diversity 等同于业务 coverage。作者的 domain-speed proxy `S=(t_ar*AL)/t_sd` 依赖 representative AL
  与可靠 step-time measurement，不能替代目标 SLO 下的真实 replay/canary。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 扩大 semantic、ISL 与 concurrency
  coverage 增加运行成本、数据治理和结果解释复杂度；pre-tokenized input 隔离 engine preprocessing，
  却可能绕过实际 production chat-template/tokenization 路径；truncation/padding 固定 shape，也可能改变
  原始 prompt semantics。小型 batch-1、synthetic shape 或 microbenchmark 仍适合 kernel 回归、容量上界
  和快速排障，但必须由真实语义 workload 校准，不能承担 production speedup 结论。
- **Evolution Relationship:** `Layering / Dependency`：acceptance correctness benchmark
  → diverse semantic AL slices → fixed-ISL/concurrency system curves → matched production trace and SLO canary。
  新层没有淘汰旧层；它把不同问题分开并为它们建立共同 identity。
- **ROADMAP / Chapters Read / Existing Coverage:** 已读 Ch43～45 与 Ch62。Ch44 已明确写出 acceptance
  rate 不等于端到端 speedup、draft/verification cost、batch/hardware/workload、capacity-aware verify
  length 与 runtime state；Ch62 已拥有 evaluation subject identity、distribution/slice、不确定性和
  runtime SLO。SPEED-Bench 提供受限、可追溯的案例证据，没有形成新的长期机制缺口。
- **Integration Decision:** `No Change — Already Covered / Experimental Evaluation Case`。不修改 Books，
  不保存作者 speedup headline；未来若形成跨 engine/跨硬件独立复现，可作为 Ch44 Review evidence，
  仍不应把单一 benchmark 写成 production truth。
- **Open Questions:** artifact/tag 是否能冻结与论文相同的数据、client 和 engine adapter？如何把
  arrival process、prefix reuse、continuous batching、queueing、p95/p99、power 与 cost 加入同一 EvalSpec？
  pre-tokenized isolation 与完整 production preprocessing 各应承担哪一类比较？

## Evidence Level

- Google scheduling 与 Seed2.0 两项旧候选已有来源级复核，但原来的 `No change` 只对这两项成立。
- 四十九项已完成非模板化来源复核：Dr. MAS、iGRPO、LycheeMemory、GRU-Mem、Data Repetition、
  DataChef、StateLM、BAE、CLI-Gym、DeAction、Composition-RL 与 G-OPD 进入 Books 候选队列；
  GoodVibe 因 threat model、数据与 scorer 边界过窄保持 `Emerging / Experimental`；
  Chain of Mindset 与 GENIUS 因 Ch71/75/78、Ch62 已有更完整框架而 `No Change`。Scheduling/
  Seed2.0 的既有 disposition 保持不变。这只说明证据足以进入后续决策，不等于自动修改 Books。
  Voxtral、Gaia2、MiniCPM-SALA 与 INTENT 形成 Books 候选；SPES 与 Dreaming in Code 因规模、failure
  model 和 domain evidence 保持 `Experimental`。新增 ARO、RLTR、ProSeCo 与 Aletheia 进入
  Books 候选队列，UniT 保持 `Experimental`；Seedream 只达到 `Product Fact / Mechanism Not
  Disclosed`。InternAgent-1.5 已完成 mechanism/evaluation partial packet、官方发布/artifact 与相邻章节
  联读，但完整正文仍不可逐页核验，保持 `Unverified / Blocked`。
- ERL 形成“失败门控的 reflection-conditioned trajectory → selective distillation → deployment
  policy”候选演进链；REDSearcher 形成“task topology/evidence dispersion → atomic capability
  mid-training → real SFT + simulated RL”候选演进链。二者已完成全文与 Appendix 复核，但仍只进入
  Books 待审队列，不把作者 benchmark 或 `cost-efficient` 标题外推为通用结论。
- FAC Synthesis 把 data diversity 从文本/embedding 距离推进到 model-feature coverage，但 anchor、SAE
  与 generator/filter 形成新的共同偏差；OneVision 与 CoPE 则恢复出两条不能混写的 codec-aware
  visual-token 分支：前者选择 decoded RGB patches，后者直接把 P-frame primitives 编成 Delta tokens。
  三项均完成全文、实验和 Appendix/implementation 复核，状态为 Books 候选而非已吸收。
- Intelligent AI Delegation 是无实现/实验的 conceptual framework，现有 Ch78～80 已有更强的可执行
  contract，故 `No Change`；DICE 的 scaffolded infilling → full artifact curriculum 与 SciAgentGym 的
  typed environment → recovery diagnostics 则分别进入 Ch29、Ch62 的 Books 候选队列，仍须人工 Gate。
- RL-finetuned VLM robustness 把 clean accuracy、conflict robustness 与外显 CoT-answer consistency 分轴，
  并明确该 consistency 不等于 internal mechanistic faithfulness；ARC 则把固定 Agent configuration 推进为
  query-conditioned SMDP option selection。两者分别进入 Ch62 与 Ch80 的候选队列，均不外推作者数值。
- BrowseComp-V3 以 gold subgoal vector 暴露 final success 与 partial progress 的差距，同时 current
  artifact 证明其 scorer 是 LLM-judge 的无序集合匹配，不能把 Process Score 当成 path validity；AIDev
  只形成 versioned production-observation dataset，因无新机制或因果结论而 `No Change`。
- SPEED-Bench 完成 v1/v2、全部方法/实验/Appendix 与 Ch43～45/62 联读；它支持 workload-conditioned
  speculative-decoding evaluation，却没有超出 Ch44 已有的 acceptance、draft/verification cost、
  batch/hardware/workload contract，故为 `No Change — Already Covered / Experimental Evaluation Case`。
- HF Daily Papers 是 discovery index，不是事件日期或结论证据；arXiv v1/官方发布时间才决定归周。
- Dreaming in Code 已重定位为 arXiv:2602.08194 v1、2026-02-09，确属 W07。
- ERL 与 REDSearcher 已按 primary publication date 2026-02-15 重定位到 W07，并完成全文复核；
  随后又有十项跨 discovery-date 候选通过 metadata/date Gate；十项均已完成全文/primary-artifact 复核，
  W07 已无普通 candidate-level pending，但有 1 个 blocked packet；按 blocked-skip 规则 Candidate Review
  Checkpoint 为 49/49 accessible completed。InternAgent 不进入 Books；engineering discovery gap 留在
  Archive Completion Gate，不再阻塞已经完成全文审计 family 的 Source-Family Books Gate。

## Cross-Week Deduplication

Seed2.0 的 6 月 30 日 model card 属于同一模型系列的 documentation-state 更新，不应再次
宣称首次发布。HF discovery date 导致的 29 个跨周候选已单独列出，后续应回查 W05/W06，
而不是在 W07 重复计分。Gemini 科学研究案例合集 v1 属 W06，W07 只把它作为 Aletheia 的相关
证据；Aletheia paper v1 与 Deep Think Blog 则合并为 W07 同一 source family。W07 内部还需把
Step 3.5 的 model report、official blog、model card 与公开实现合并成一个 source family。

## Knowledge Tree Position

W07 最终使用 Stable Knowledge Node 作为 owner；Legacy 号只解释历史记录：

| Stable owner | Current / Legacy | Absorbed mechanism line |
| --- | --- | --- |
| `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | sparse selection；write/exit gate；compressed recurrent KV；hybrid sparse/linear branch |
| `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | decoded-RGB selection 与 compressed-domain Delta token 两条 codec-aware 分支 |
| `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | mutable masked-diffusion state、selective correction 与 commit/cache boundary |
| `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | database-owned synthetic environment state 与 real-world validity boundary |
| `TRAIN-DATA` | Ch27 / Ch23 | semantic/feature/environment coverage → policy-relative curriculum → independent verifier |
| `TRAIN-PRETRAINING` | Ch28 / Ch24 | adaptive rotation 作为 optimizer state，而非普遍最优配方 |
| `TRAIN-SFT` | Ch29 / Ch25 | demonstration repetition schedule 与 on-policy distillation state contract |
| `TRAIN-GRPO` | Ch33 / Ch29 | terminal reward → role/block/draft/transfer/reflection typed credit；entropy controller 独立分轴 |
| `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | owner-oriented reduce-scatter 与标准 collective 的共存边界 |
| `INFER-KV-CACHE` | Ch45 / Ch41 | streaming input、resumable continuation、lease 与 output frontier |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | final result → artifact → process/subgoal → recovery → asynchronous environment evidence |
| `PLATFORM-SECURITY` | Ch72 / Ch68 | effect-time authorization 前的 off-task action guardrail |
| `AGENT-CONTEXT` | Ch75 / Ch71 | model-managed visible context 与 durable deletion 的边界 |
| `AGENT-PLANNING` | Ch79 / Ch75 | costly-tool information value、hard budget 与 verification reserve |
| `AGENT-WORKFLOW` | Ch81 / Ch77 | parallel search 与 sequential artifact refinement 的组合 |
| `AGENT-PLATFORM` | Ch84 / Ch80 | query-wise approved-option configuration scheduling |

`SkillRL`、`Chain of Mindset`、`GENIUS`、`Intelligent AI Delegation`、`AIDev` 与 `SPEED-Bench` 均由表中
指定现有章节的具体机制完整承接，故 `No Change`；Weak-Driven、GoodVibe 与 decentralized MoE 保持
`Emerging / Experimental`；Seed2.0、Seedream 为 `Weekly Only`；InternAgent 为 blocked-skip。不存在因
新 Part 之外无 owner 而静默遗漏的 W07 family。

## Recommended Action

W07 Source-Family Books Gate 已完成。后续只在取得 InternAgent 事件时完整正文后重开其单项 Gate；
Weak-Driven、GoodVibe 与 decentralized MoE 等 Experimental family 需要更强复现或机制证据才进入正文。
GitHub release/RFC 历史分页与 Scholar/OpenAlex recall gap 留在 Archive Completion Gate。下一周可推进
W08，但不得把本周的 vendor benchmark、leaderboard 或未披露机制写成通用结论。

## Event-Date Daily Decision

2026-02-09～02-15：50 个恢复条目保留在 Weekly；49 项完成来源复核、1 项阻塞、0 项普通待审。
加上原有 scheduling 与 Seed2.0，共 52 个计分行。历史回填不补造 Daily。

## Books Integration Decision

`W07 Source-Family Books Gate Complete`：52/52 计分行已有最终 disposition；39 项 Integrate/Refine，
7 项 `No Change`，3 项 `Emerging / Experimental`，2 项 `Weekly Only`，1 项 `Unverified / Blocked`。
InternAgent 按用户确认的 blocked-skip 规则不进入正文；Archive Completion Gate 仍为 Open，因此这里不宣称
2026 历史档案整体完成。

## Ignored Noise

未绑定模型版本、工具环境、输入长度和 reasoning budget 的榜单比较；HF upvote/ranking；
把发现页提交日期误当 arXiv 首次公开日；只读 abstract 就推断实现机制或通用性能。

## Repository Changes

- 完成 W07 Source-Family Books Integration：52 个计分行全部获得最终 disposition；39 项
  `Integrate / Refine` 被合并进 16 个 Stable Node owner，7 项以章节级证据判定 `No Change`，3 项
  `Emerging / Experimental`、2 项 `Weekly Only`、1 项 `Unverified / Blocked` 未进入正文。
- Books 写入不采用论文列表式追加，而是形成六条连续路线：coverage-driven curriculum、optimizer/
  communication ownership、typed RL credit、streaming state、layered executable evaluation、Agent
  context/planning/workflow/configuration control。更新 Ch22～25、Ch27～29、Ch33、Ch36、Ch45、Ch66、
  Ch72、Ch75、Ch79、Ch81 与 Ch84；其中 Ch24/25 为此前已通过的同周 Source Families。
- Stable Node、Current/Legacy chapter 与 blocked-skip 边界已回填；InternAgent、Weak-Driven、GoodVibe、
  decentralized MoE、Seed2.0 与 Seedream 均未被借此写入长期机制正文。
- 重新打开 W07 candidate census，从 2 项扩展为 52 个计分行（50 项恢复候选）。
- 增加日期边界排除、Source Review 状态和 Evidence Gate。
- 完成 LLaDA2.1、Prism、Step 3.5 Flash、FeatureBench、Weak-Driven Learning、Dr. SCI、Flexible
  Entropy、SkillRL、Agent World Model、Dr. MAS、iGRPO、LycheeMemory、Chain of Mindset 与 GENIUS
  十四份非模板化 Source Review，并完成 GRU-Mem、Data Repetition、DataChef、StateLM、BAE，累计
  十九份，并完成 CLI-Gym、GoodVibe、DeAction、Composition-RL、G-OPD，累计二十四份；再完成
  Voxtral、Gaia2、MiniCPM-SALA、SPES、INTENT 与 Dreaming in Code，累计三十份；将
  ARO、RLTR、ProSeCo、UniT、Aletheia/Deep Think 与 Seedream 5.0 Lite 纳入第二轮机构来源
  交叉检验，累计三十六份来源复核；InternAgent-1.5 记录为正文访问阻塞。再完成 ERL
  与 REDSearcher 全文、Appendix 和公开 artifact 联合复核，累计三十八份；再完成 FAC Synthesis、
  OneVision-Encoder 与 CoPE-VideoLM 的全文、实验条件、ablation、Appendix/implementation 与章节归属
  复核，累计四十一份；再完成 Intelligent AI Delegation、DICE 与 SciAgentGym 的 framework/method、
  evaluation、failure/limitation、Appendix 与章节去重复核，累计四十四份；再完成 RL-finetuned VLM
  robustness 与 ARC 的全文、revision、实验 contract、failure boundary 与相邻章节去重，累计四十六份；
  再完成 BrowseComp-V3 与 AIDev 的论文、公开 artifact、source-family history、scorer/attribution 与章节
  去重复核，累计四十八份；本轮再为 InternAgent 补齐可检索原文 passages、官方发布/artifact、机制、
  evaluation contract、failure boundary 与 Ch72～78 去重，但因未完成逐页全文覆盖，仍不计入 49th Full
  Source Review；无 Daily 或 Books 修改。
- W08 metadata Gate 发现 ERL 与 REDSearcher 的 Sunday primary date，将二者回填 W07 并完成
  Source Review；不以 HF 2 月 17 日 discovery date 改写 ISO week。
- 继续检查 2 月 16～17 日 discovery pages，又恢复十项 v1 日期落在 W07 的候选；本轮只完成
  metadata/date、初步评分和知识树定位后，十项已全部完成全文/primary-artifact 复核，未用 abstract
  代替正文。
- W16 discovery feed 发现 SPEED-Bench 的 arXiv 编号虽为 `2604.*`，但 v1 明确为 2026-02-10；
  已按 first-public date 回填 W07；本轮完成 v1/v2 全文、measurement framework、实验/Appendix、
  workload contract 与 Ch43～45/62 去重复核，最终为 `No Change — Already Covered / Experimental
  Evaluation Case`，未把后续编号或 revision 当作新事件，也未修改 Books。

## Open Questions

1. W07 GitHub release/RFC 历史分页与 Scholar/OpenAlex recall 能否补齐，以关闭 Archive Completion Gate？
2. InternAgent-1.5 的事件时完整报告能否取得，使 memory invalidation、solution-graph recovery 与 SCP lab approval contract
   在后续报告或代码中公开，足以把组合架构从作者案例提升为可复现实证？
3. Weak-Driven v1 的 weak branch ownership 与 v2 的 paired update 是否构成可复现的同一算法，
   还是一次需要单独记录的机制修订？
4. 实时流式 request、异步 event-time evaluation、budget oracle 与 executable curriculum 四类新状态，
   分别需要哪些可复现 artifact 才能通过 Books Gate？
5. Aletheia 的 autonomy/significance 分轴能否推广到非数学 Research Agent，同时保持领域专家
   对 novelty/significance 的最终 authority？
6. SPEED-Bench artifact/tag 能否冻结与论文相同的数据、client 和 engine adapter？怎样加入 arrival
   process、prefix reuse、continuous batching、queueing、p95/p99、power 与 cost，形成可迁移 EvalSpec？

## Sources

- Google Research February 2026 archive: https://research.google/blog/2026/02/
- ByteDance Seed, “Seed 2.0 Official Launch,” published 2026-02-14:
  https://seed.bytedance.com/en/blog/seed2-0-%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83
- Hugging Face Daily Papers discovery pages, accessed 2026-08-07:
  https://huggingface.co/papers/date/2026-02-09
  https://huggingface.co/papers/date/2026-02-10
  https://huggingface.co/papers/date/2026-02-11
  https://huggingface.co/papers/date/2026-02-12
  https://huggingface.co/papers/date/2026-02-13
- 50 个 recovered candidates 已列在 census；四十九项完成 primary-source review，InternAgent 有详细
  partial packet 但因正文读取限制保持 `Unverified / Blocked`，普通 pending 为 0。Seedream 的
  完成状态只表示 official product fact 已核验，不表示存在公开技术机制。
- Experiential Reinforcement Learning, primary publication 2026-02-15:
  https://arxiv.org/abs/2602.13949
- REDSearcher, primary publication 2026-02-15:
  https://arxiv.org/abs/2602.14234
- REDSearcher official project page and repository, accessed 2026-08-08; later artifact state is
  verification evidence, not a W07 event:
  https://redsearchagent.github.io/
  https://github.com/RedSearchAgent/REDSearcher
- SPEED-Bench, v1 2026-02-10: https://arxiv.org/abs/2604.09557
- SPEED-Bench v1 full HTML and Appendices: https://arxiv.org/html/2604.09557v1
- NVIDIA SPEED-Bench dataset (6 subsets; qualitative split 880 rows; accessed 2026-08-12):
  https://huggingface.co/datasets/nvidia/SPEED-Bench
- Discovery-recovered W07 primary sources, all ten full reviews complete:
  https://arxiv.org/abs/2602.10388
  https://arxiv.org/abs/2602.08683
  https://arxiv.org/abs/2602.13191
  https://arxiv.org/abs/2602.11865
  https://arxiv.org/abs/2602.11715
  https://arxiv.org/abs/2602.12984
  https://arxiv.org/abs/2602.12506
  https://arxiv.org/abs/2602.11574
  https://arxiv.org/abs/2602.12876
  https://arxiv.org/abs/2602.09185
- BrowseComp-V3 official artifact, dataset/decryption documentation, reference runner and scorer code,
  accessed 2026-08-08; this later artifact state is verification evidence, not a W07 event:
  https://github.com/Halcyon-Zhang/BrowseComp-V3
  https://raw.githubusercontent.com/Halcyon-Zhang/BrowseComp-V3/main/examples/eval_rollout_results.py
- AIDev source-family evidence: the 2026 dataset paper is the W07 documentation/update node; the
  2025 paper records the earlier snapshot and observational studies. Repository and Hugging Face
  artifacts were accessed 2026-08-08:
  https://arxiv.org/abs/2507.15003
  https://github.com/SAILResearch/AI_Teammates_in_SE3
  https://huggingface.co/datasets/hao-li/AIDev
- ARO, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.09006
- Beyond Correctness / RLTR, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.08489
- ProSeCo, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.11590
- UniT, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.12279
- Aletheia / Towards Autonomous Mathematics Research, arXiv v1 2026-02-10; v3 used for full review:
  https://arxiv.org/abs/2602.10177
- Google DeepMind, “Gemini Deep Think: Advancing science, research and engineering,” published
  2026-02-11:
  https://deepmind.google/blog/gemini-deep-think-advancing-science-research-and-engineering/
- Related cross-week source, Accelerating Scientific Research with Gemini, arXiv v1 2026-02-03 (W06):
  https://arxiv.org/abs/2602.03837
- ByteDance Seed, Seedream 5.0 Lite official launch, published 2026-02-13:
  https://seed.bytedance.com/en/blog/deeper-thinking-more-accurate-generation-introducing-seedream-5-0-lite
- LLaDA2.1, arXiv v1 2026-02-09, last revision used v3 2026-02-13:
  https://arxiv.org/abs/2602.08676
- Prism, arXiv v1 2026-02-09; v2/ICML revision used for verification:
  https://arxiv.org/abs/2602.08426
- Step 3.5 Flash, arXiv v1 2026-02-11; current v2 used for verification:
  https://arxiv.org/abs/2602.10604
- FeatureBench, arXiv v1 2026-02-11 / ICLR 2026:
  https://arxiv.org/abs/2602.10975
- InternAgent-1.5 primary report, official release, repository and solution-refinement artifact:
  https://arxiv.org/abs/2602.08990
  https://www.shlab.org.cn/news/5444231
  https://github.com/InternScience/InternAgent
  https://github.com/InternScience/MLEvolve
- Voxtral Realtime, arXiv v1 2026-02-11:
  https://arxiv.org/abs/2602.11298
- Gaia2, arXiv v1 2026-02-12 / ICLR 2026:
  https://arxiv.org/abs/2602.11964
- MiniCPM-SALA, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.11761
- SPES decentralized MoE pretraining, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.11543
- INTENT budget-constrained tool-use planning, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.11541
- Dreaming in Code, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.08194
- Weak-Driven Learning, arXiv v1 2026-02-09; v2 2026-06-08 used only for revision comparison:
  https://arxiv.org/abs/2602.08222
- Dr. SCI, arXiv v1 2026-02-09; v2 2026-02-10:
  https://arxiv.org/abs/2602.08321
- Flexible Entropy Control, arXiv v1 2026-02-10; v2 2026-05-08 used only for revision comparison:
  https://arxiv.org/abs/2602.09782
- SkillRL, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.08234
- Agent World Model, arXiv v1 2026-02-10; v3 2026-05-22 used only for revision comparison:
  https://arxiv.org/abs/2602.10090
- Dr. MAS, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.08847
- iGRPO, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.09000
- LycheeMemory, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.08382
- Chain of Mindset, arXiv v1 2026-02-10; v2 is later revision evidence only:
  https://arxiv.org/abs/2602.10063
- GENIUS, arXiv v1 2026-02-11:
  https://arxiv.org/abs/2602.11144
- Gated Recurrent Memory, arXiv v1 2026-02-11:
  https://arxiv.org/abs/2602.10560
- Data Repetition for Long-CoT SFT, arXiv v1 2026-02-11:
  https://arxiv.org/abs/2602.11149
- DataChef, arXiv v1 2026-02-11; v2 used only as later revision evidence:
  https://arxiv.org/abs/2602.11089
- The Pensieve Paradigm / StateLM, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.12108
- Blockwise Advantage Estimation, arXiv v1 2026-02-10:
  https://arxiv.org/abs/2602.10231
- CLI-Gym, arXiv v1 2026-02-11:
  https://arxiv.org/abs/2602.10999
- GoodVibe, arXiv v1 2026-02-11:
  https://arxiv.org/abs/2602.10778
- DeAction / off-task action detection, arXiv v1 2026-02-09:
  https://arxiv.org/abs/2602.08995
- Composition-RL, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.12036
- Generalized On-Policy Distillation, arXiv v1 2026-02-12:
  https://arxiv.org/abs/2602.12125

## 2026-08-13 Source-Family Books Integration

Archive Completion Gate 仍为 Open；以下 family 已独立通过 Source-Family Books Gate：

| Source Family | Owner | Current / Legacy | Final decision | Repository change |
| --- | --- | --- | --- | --- |
| LLaDA2.1 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Integrate — Experimental mechanism branch | `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` |
| ProSeCo | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — correction-aware branch | 同上 |
| Agent World Model | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — synthetic-environment branch; not real-world proof | `books/part-03-multimodal-world-models/25-multimodal-world-models.md` |
| Prism / LycheeMemory / GRU-Mem / MiniCPM-SALA | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Refine — sparse selection、write/exit gate 与 recurrent/compressed memory branches | `books/part-02-model/22-long-context.md` |
| OneVision / CoPE-VideoLM | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Refine — two codec-aware representation branches | `books/part-03-multimodal-world-models/23-multimodal-representation.md` |
| Dr. SCI / DataChef / Composition-RL / Dreaming / REDSearcher / FAC | `TRAIN-DATA` | Ch27 / Ch23 | Refine — coverage-driven executable curriculum | `books/part-04-training-system/27-data.md` |
| ARO | `TRAIN-PRETRAINING` | Ch28 / Ch24 | Refine — rotation is optimizer state, not a universal recipe | `books/part-04-training-system/28-pretraining.md` |
| Data Repetition / G-OPD | `TRAIN-SFT` | Ch29 / Ch25 | Refine — schedule and on-policy distribution contract | `books/part-04-training-system/29-sft.md` |
| Flexible Entropy / Dr. MAS / iGRPO / BAE / RLTR / ERL / DICE | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — typed credit and independent entropy actuator | `books/part-04-training-system/33-grpo.md` |
| Step 3.5 Flash | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Refine — owner-oriented collective branch | `books/part-04-training-system/36-distributed-training.md` |
| Voxtral Realtime | `INFER-KV-CACHE` | Ch45 / Ch41 | Integrate — resumable streaming state lifecycle | `books/part-05-inference-system/45-why-kv-cache-speeds-up.md` |
| FeatureBench / CLI-Gym / Gaia2 / Aletheia / SciAgentGym / VLM robustness / BrowseComp-V3 | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — result/artifact/process/environment evidence ladder | `books/part-06-ai-infrastructure/66-evaluation-system.md` |
| DeAction | `PLATFORM-SECURITY` | Ch72 / Ch68 | Integrate — pre-execution off-task guardrail | `books/part-06-ai-infrastructure/72-security.md` |
| StateLM | `AGENT-CONTEXT` | Ch75 / Ch71 | Integrate — model-managed visible context | `books/part-07-agent/75-context.md` |
| INTENT | `AGENT-PLANNING` | Ch79 / Ch75 | Integrate — costly-tool budget planning | `books/part-07-agent/79-planning.md` |
| UniT | `AGENT-WORKFLOW` | Ch81 / Ch77 | Integrate — sequential artifact refinement | `books/part-07-agent/81-workflow.md` |
| ARC | `AGENT-PLATFORM` | Ch84 / Ch80 | Integrate — query-wise approved-option scheduling | `books/part-07-agent/84-agent-platform.md` |

W07 独立 Review 结果：所有 52 项都有最终 disposition；没有把 blocked、product fact 或 disputed mechanism
写入正文。Archive Completion Gate 仍保留 InternAgent full text 与 engineering/discovery recall gap。
