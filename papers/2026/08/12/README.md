# Daily Research — 2026-08-12

**Archive Date:** 2026-08-12（Asia/Shanghai）

**Coverage Window:** 2026-08-10 09:08 ～ 2026-08-12 09:08（Asia/Shanghai）

**Archive Clock:** Wednesday；只生成 Daily，不生成当前周 provisional `2026-W33`。

**Status:** No Material Update；实际覆盖与访问边界已记录；Books Integration Evaluated — No Change

## Executive Summary

本次没有发现能在过去 24～48 小时内同时满足“首次公开日期可核验、存在 primary technical
evidence、形成长期 AI System 机制增量”的新候选。模型与研究机构的可访问官方索引没有出现
8 月 11～12 日的新 Research event；学术检索返回的相关条目要么已由 8 月 11 日 Daily 按 first-public
date 收录，要么无法把搜索摘要与 arXiv 正文、作者和 revision history 对齐；工程检索也没有完成
release tag、官方说明、代码路径与 workload contract 的联合核验。

因此今天不修改 Books。SwiftQK 与 QueryProof 继续归 8 月 11 日 Daily，Beyond Routing 继续归
8 月 9 日；搜索索引的延迟、旧页面重排和社区 benchmark 不产生新的事件。这个结论表示“本次未取得
足够证据”，不是对完整互联网作出“绝对没有发布”的负面证明。

## 1. 模型与研究机构

### Source Coverage

按固定顺序检查 OpenAI、Anthropic、Apple Machine Learning Research、Google DeepMind、Google
Research、Meta AI / FAIR、Microsoft Research、NVIDIA Research、xAI、Amazon Science、Cohere Labs、
Ai2、Mistral、Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Seed、Baidu ERNIE、Tencent
Hunyuan、Huawei Noah、Shanghai AI Lab / InternLM、StepFun、Xiaomi MiMo、InclusionAI / Ant 与
Hugging Face Blog 的 Research / Publication / model report 入口。

- OpenAI Research index 当前最新可见的高信号 publication 早于本窗口；没有把产品、项目计划或旧内容
  重排记为新的模型机制。
- Google Research index 当前最新可见条目也早于本窗口；没有 8 月 11～12 日可核验的新增 Research。
- 其余来源若只返回搜索摘要、无稳定日期列表或没有 technical report / system card / primary artifact，
  一律保留为 coverage limitation，不补猜发布日期和实现。

### Candidate Scoring

本组没有达到候选门槛的可验证窗口内事件。

## 2. arXiv / 学术来源

### Source Coverage

检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`cs.CR` 与 `stat.ML` 的 recent/new
入口，并用 Hugging Face Papers、OpenReview/TMLR、Google Scholar、OpenAlex、Semantic Scholar 与
DBLP 做 discovery、metadata 和重复关系交叉检查。

- 搜索未返回能够以 arXiv metadata 和 primary text 双重确认 `Submitted on 11/12 Aug 2026`、且与本书
  直接相关的新论文。
- 8 月 11 日 Daily 已拥有 SwiftQK、Beyond Routing 与 QueryProof 的正文审计；其中 Beyond Routing
  first-public date 为 8 月 9 日。今天不因再次命中检索结果而重复评分。
- ElastiCo 与 OasisKV 属于 W32 的 8 月 8 日 discovery-only blocked gaps，不改写为 W33 事件；在正文
  可访问前不评分、不推断机制、不分配 Books owner。

### Candidate Scoring

本组没有新增评分候选。Evidence Level 为 `No Newly Verified Candidate`。

## 3. AI Infra 与工程项目

### Source Coverage

按 PyTorch、JAX、CUDA、Triton、vLLM、SGLang、NVIDIA Dynamo、TensorRT-LLM、Ray、KServe、
Kubeflow、Kubernetes、Transformers、Accelerate、DeepSpeed、Megatron-LM、Unsloth、MLX、llama.cpp、
ONNX Runtime 与 OpenXLA 的顺序检查官方 Release、文档、RFC 与重要 PR 入口。

- 未找到能在本窗口内联合核验 tag date、行为变化、相关代码路径和 workload contract 的稳定事件。
- 搜索结果中的旧 release、未来日期、社区性能帖和缺少 model / hardware / precision / length /
  batch / concurrency / SLO 的 benchmark 不进入候选。

### Candidate Scoring

本组没有达到候选门槛的可验证窗口内事件。

## Evidence Level and Fact Boundary

- **Official fact:** 只记录官方 Research index、项目 Release 入口和 arXiv metadata 在本次访问时可见的状态。
- **Paper evidence:** 今天没有新增完整 Source Packet，不形成新的论文机制结论。
- **Community evidence:** 社区帖子和聚合页只作 discovery，不进入事实或评分。
- **Inference:** 索引延迟或页面访问限制可能解释检索空白，但不能替代后续复核。
- **Performance numbers:** 今天不引用任何缺少完整 workload contract 的性能数字。

## Knowledge Tree Position

无新增候选需要定位 ROADMAP node。8 月 11 日的 SwiftQK、Beyond Routing 与 QueryProof 仍分别保留
Ch33、Ch21、Ch62/77 的候选映射；今天不重复建立 owner。

## Recommended Action

`Daily Only — No Books Change`。下一次运行继续以 first-public date 去重；若索引延迟暴露属于本窗口的
primary source，应幂等回写本 Daily，而不是按发现日制造新事件。

## Ignored Noise

- 旧论文、旧 Research 与旧 Release 的重新索引；
- 缺少 technical report、model/system card 或 artifact 的产品 headline；
- 社区排行榜、单机性能帖与未绑定 workload contract 的 benchmark；
- 无法从搜索摘要核对作者、标识符、first-public date 和 revision 的论文标题。

## Repository Changes

- 新建 `papers/2026/08/12/README.md`，记录 No Material Update 与实际覆盖边界。
- 未修改 Books、ROADMAP 或 DECISIONS；稳定认知与学习进度没有变化。
- 同次运行完成 W14/W15 attribution 与 forward checkpoint 同步：SkVM 按 v1 回拨 W14；W15 的五项
  accessible papers 完成全文审计，GameWorld 因 primary PDF 不可稳定读取转入 blocked backlog，
  TensorRT-LLM RC 只作低分版本边界。这些属于历史归档修复，不作为今日研究候选，也没有触发 Books 修改。
- 同次运行完成 W19 fixed official/Infra checkpoint：周报由 25 扩展至 35 个 scored families，
  `30/30` accessible `20+` Full Source Reviews 与 `1/1` low-score boundary 完成；四项 primary-text
  blocked backlog 保留，cross-index discovery 仍开放。该历史修复没有绕过 Historical Books Gate，
  因而未修改 Books。
- 同次运行完成 W20 fixed official/Infra checkpoint，并在 anti-miss review 中回拨 5 月 14 日 Vera Rubin
  agentic-inference scale-up contract：周报最终扩展至 31 个 scored families，`29/30` `20+` Full Source
  Reviews 完成，Qwen-Image-2.0 继续作为 blocked backlog。新增审计
  Kubernetes PSI / Workload-Aware Scheduling / Mixed Version Proxy、OpenAI supply-chain incident / safety
  summary、NVIDIA Fleet Intelligence、Vera Rubin execution contract 等十一项官方或工程来源；单一 counter、best-practice 与 patch release
  均未被误写为新通用机制。Historical Books Gate 保持关闭，未修改 Books。
- 同次运行完成 W21 fixed official/Infra checkpoint：W21 扩展至 31 个 scored families（19 high / 11 mid /
  1 low），26/30 `20+` Full Source Reviews、1/1 low-score boundary 完成；SkillsVote、LongLive-2.0、WorldKV、
  QUEST 保留 blocked backlog，current-review queue 为 0。新增 OpenAI layered content provenance、NVIDIA
  verified Agent Skills、Slurm topology-aware scheduling simulation、Agent evaluation guide、Transformers
  v5.9.0 与 token-metered reference architecture；每项均保留 signal/signature/simulation/version/economic
  evidence boundary。Historical Books Gate 保持关闭，未修改 Books；forward cursor 下一检查点仍为 W22。
- 同次运行继续完成 W22 fixed official/Infra checkpoint：W22 扩展至 43 个 scored families（30 high /
  12 mid / 1 low），15/42 `20+` Full Source Reviews、1/1 low-score boundary 完成，27 项 blocked、0 项
  ordinary pending。新增 Dynamo Snapshot、DynoSim、DOCA security plane、Vera CPU、DSX OS 与 STAC-AI
  workload-contract case；未 upstream/future support、simulation calibration、DPU trust、vendor hardware/
  facility claims 与 benchmark conditions 均保持显式。Historical Books Gate 继续关闭，未修改 Books；下一
  fixed-source 检查点为 W23。
- 同次运行完成 W23 fixed official/Infra checkpoint：W23 从 29 扩展至 33 个 scored families（21 high /
  12 mid），`21/33` current-version Full Source Reviews 完成，12 项 blocked、0 项 ordinary pending。
  新增 SGLang decoupled parallel speculative-decoding roadmap、vLLM v0.22.1、Transformers LightGlue
  nested-config RCE disclosure/fix 与 Datasets 5.0.0。SGLang 只形成 Ch44 provisional
  `Refine / Experimental / Revision-sensitive`，current roadmap 不倒写为 6 月 6 日已实现；其余三项分别是
  Ch46/53、Ch68 与 Ch23/62 的版本/纠错案例去重。fixed checkpoint 已通过，W23 broader discovery 与
  Historical Evidence Gates 仍开放，Historical Books Gate 继续关闭；下一 cursor 为 W24。
- 同次运行完成 W24 fixed official/Infra checkpoint：W24 从 35 扩展至 38 个 scored families（26 high /
  11 mid / 1 low），`6/37` `20+` Full Source Reviews 完成，31 项 blocked、0 项 ordinary pending；
  FastContext 保持 withdrawn low-score boundary。新增 KServe v0.19.0、AA-AgentPerf 与 NVIDIA
  FP8 checkpoint→ONNX Q/DQ→TensorRT chain；分别得到 Ch57 provisional refine、Ch62/66 provisional
  live-benchmark refine 与 Ch45 `No Change`。vLLM v0.23.0 依据 6 月 15 日 official release date 归 W25。
  W24 fixed checkpoint 已通过，broader discovery/Historical Evidence Gates 仍开放，Historical Books Gate
  继续关闭；下一 cursor 为 W25。
- 同次运行完成 W25 fixed official/Infra checkpoint：W25 从 32 扩展至 35 个 scored families（24 high /
  10 mid / 1 low），新增并完成 vLLM v0.23.0、NVIDIA sync-free MoE fused kernels 与 MLPerf Training
  v6.0 primary-source review；当前 `7/34` `20+` Full Source Reviews、27 blocked、0 current-review pending。
  三项分别形成 Ch46 version-sensitive refine、Ch21 bounded mechanism refine（Ch36/45 handoff）与 Ch62
  benchmark-contract refine；vendor microbench、submitter statement、suite rules/ownership 已分层。fixed
  checkpoint通过，cursor推进 W26；W25 broader discovery/Historical Evidence Gates仍开放，Historical
  Books Gate关闭。
- 同次运行完成 W26 fixed official/Infra checkpoint：W26 从 38 扩展至 40 个 scored families（25 high /
  14 mid / 1 low），新增 DFlash cross-runtime integration 与 TensorRT 11 multi-device inference并完成
  Source Review；当前`6/39` `20+` Full Source Reviews、33 blocked、0 current-review pending。DFlash与
  W06/W16去重为engineering node并对Ch44 `No Change`；TensorRT 11暂定Ch45 version-sensitive refine，
  明确rank-local engine/context、communicator lifetime、all-rank collective progress与support/failure matrix。
  fixed checkpoint通过并推进W27；broader discovery/Historical Evidence Gates仍开放，Historical Books Gate关闭。
- 同次运行完成 W27 fixed official/Infra checkpoint：W27 从 31 score rows / 30 unique families 扩展至
  33 rows / 32 unique families（23 high / 10 mid），当前 `11/32` unique Full Source Reviews、21 blocked、
  0 current-review pending。新增 Secure Agent Workspace Reference Design 与 TensorRT Edge-LLM v0.9.0：
  前者暂定 Ch80 reference-architecture refine（Ch68 handoff），并明确 OpenShell 当前 alpha/single-player、
  Kubernetes/GPU experimental 的访问时边界；后者只作 Ch45 version fact，不从 support matrix 推断通用机制。
  fixed checkpoint 通过并推进 W28；Historical Books Gate 继续关闭，未修改 Books。
- 同次运行完成 W28 cross-week spillback / fixed-source checkpoint：W29/W30 已声明回拨却未真正进入
  owner week 的 7 个 identities 已补入 W28，分别是 ABot-AgentOS、GRASP、Weak-to-Strong Direct OPD、
  What LLM Forecasters Know、PolicyShiftGuard、Root Causes 与 DeepSearch-World。因 primary metadata/正文
  当前不可访问，七项保持 unscored blocked，不从标题补机制。W28 仍为 21 scored rows，但 unique families
  从 21 增至 28；7 scored reviews complete、14 scored + 7 unscored blocked、0 current-review pending。
  这是 attribution repair 的中间账目；同日后续 ReOPD 与 ReflectWorld-MM 全文审计已将最终 W28
  账目更新为 23 scored + 7 unscored / 30 unique、9 reviews complete。Historical Books Gate 继续关闭，
  未修改 Books。
- 同次运行完成 W29 fixed-source / spillback checkpoint：将 8 月 11 日 Daily 已确认 v1 为 7 月 14 日、
  但未回写 owner week 的 `Training Variable Long Sequences with Data-Centric Parallel`（2608.07524）
  补为 unscored blocked identity。W29 保持 26 scored rows、unique families 增至 27；7 reviews complete、
  19 scored + 1 unscored blocked、0 current-review pending。未从标题推断 data-centric parallel 机制。
- 同次运行核对 W30 所称 14 个 pre-window spillbacks：RESOURCE2SKILL（2606.29538v1，6 月 30 日）
  回写 W27；ReflectWorld-MM 与 ReOPD 按 7 月 6 日回写 W28；其余 11 项按 7 月 16～19 日回写 W29。
  随后 ReOPD 完成全文、proof、实验、limitations、official artifact、29/30 评分与相邻章节审计；
  ReflectWorld-MM 完成 v1/v2、完整 architecture/appendices、实现、mixed-provenance evaluation、
  answer-time ablation、official repository 与 Ch72～74/80 去重审计，评分 28/30。当时其余 12 项保持
  unscored blocked；随后 OPD² 与 Recursive Harness Self-Improvement 完成 Full Source Review，将最终
  剩余数降至 10。摘要不替代 Full Source
  Review；四项均只形成 provisional Books disposition。
- 同次运行继续完成 W29 的 OPD² Full Source Review：核验 v1 全文、teacher/base delta 与 sign-gated
  objective、三域 14-benchmark evaluation、training dynamics、ablations、H100 workload、appendix、
  8 月 5 日 official code/recipes 及 Ch27～30/23 去重。W29 更新为 27 scored + 11 unscored / 38 unique，
  8 reviews complete。该结果只形成 Ch29 provisional Experimental refine，Historical Books Gate 继续关闭。
- 同次运行继续完成 W29 的 Recursive Harness Self-Improvement Full Source Review：核验 v1 全文、
  trajectory-local preference objective、revision/self-history ownership、synthetic repository benchmark、
  judge/resource contract、component ablations、information-theoretic hypothesis、appendices 与 Ch76～78/62
  去重，评分 27/30。W29 更新为 28 scored + 10 unscored / 38 unique、9 reviews complete；只形成
  Ch77 provisional Experimental refine，Historical Books Gate 继续关闭，未修改 Books。
- 同次运行继续完成 W29 的 Muon Agentic RL Full Source Review：核验 event-time v1 的单 seed、0.5B、
  ALFWorld 全文与 appendices，并把 7 月 20 日、7 月 30 日、8 月 2 日 revisions 和 official `verl-muon`
  repository 作为 post-window verification 单独处理。v4 的 multi-seed、scale/transfer、RMS-matched control
  与 FSDP `NO_SHARD` implementation 将结论收窄为特定 RL recipe 下的 effective-update-scale headroom，
  不证明 universal optimizer ranking 或 spectral causality。评分 26/30；W29 更新为 29 scored + 9 unscored /
  38 unique、10 reviews complete，只形成 Ch29 provisional Experimental refine 与 Ch35/31 handoff；
  Historical Books Gate 继续关闭，未修改 Books。
- 同次运行继续完成 W29 的 Xiaomi-Robotics-1 Full Source Review：核验 v1 全文、VLM+DiT / Choice Policy、
  embodiment-free UMI auto-label pipeline、cross-embodiment action schema/instruction alignment、pretraining
  scaling、real-robot/downstream/simulation evaluation 与 Ch23～25/10/62 邻接；7 月 22 日 v2 和 8 月 3 日
  code/checkpoints 只作 post-window verification。评分 27/30；W29 更新为 30 scored + 8 unscored / 38
  unique、11 reviews complete。只形成 Ch23 provisional Experimental refine 与 Ch24/25/10/62 handoff，
  不把 100K-hour headline、作者 benchmark 或“no saturation”外推为通用 scaling law；Historical Books Gate
  继续关闭，未修改 Books。
- 同次运行继续完成 W29 的 DSWorld Full Source Review：核验 sole-v1 全文、四组件 hybrid
  execution/simulation architecture、SFT + Reflective World Model Optimization、real/synthetic transition data、
  evaluation/ablation/limitations/appendices 与 Ch75～77/10/62 邻接。评分 27/30；W29 更新为 31 scored +
  7 unscored / 38 unique、12 reviews complete。稳定增量是 predicted state 不得取代 authoritative execution
  state，以及 cost/fidelity routing 必须配套 timeout cancellation/reconciliation；但论文 `~14x versus Compiler`
  的文字与 Table 2 的 335/277 min 冲突，标记 Disputed，anonymous artifact 也保持 unavailable。只形成
  Ch77 provisional Experimental refine，未修改 Books。
- 同次运行继续完成 W29 的 Cost-Aware Security Agents Full Source Review：核验 event-time v1 的
  Cybench/BOTS harness、refusal/cost accounting、results、contamination/scaling、limitations、Appendices A～E，
  并把 v3 expanded models/provider conditions 作为 post-window verification；评分 28/30。W29 更新为
  32 scored + 6 unscored / 38 unique、13 reviews complete。其 operating-point、cost-per-valid-outcome、
  refusal 与 public-benchmark contamination contract 已由 Ch62/66/68 具体覆盖，判定 `No Change — Already
  Covered / Experimental Evaluation Case`，未修改 Books。
- 同次运行继续完成 W29 的 SeerGuard Full Source Review：核验 sole-v1 的 instruction/action 双阶段
  pipeline、SAWM data/training、MobileSafetyBench / MobileRisk / Next-State-QA evaluation、ablations、latency、
  appendices、当前 official project/repository/model artifacts 与 Ch68/74/77/62/10 邻接，评分 27/30。W29
  更新为 33 scored + 5 unscored / 38 unique、14 reviews complete。稳定增量是把 pre-execution semantic
  consequence prediction 定位为 instruction filter 与 deterministic authorization 之间的 policy-bound sensor；
  environment 仍拥有实际 state，生产系统仍需 uncertainty/approval 与 prediction reconciliation。当前 artifacts
  仅作 post-window verification；不把作者二元 benchmark 或提前拒绝混合后的平均 latency 外推为通用结论。
  只形成 Ch68 provisional Experimental refine，Historical Books Gate 继续关闭，未修改 Books。
- 同次运行继续完成 W29 的 Environment-free API data / ESAT Full Source Review：完整阅读 82 页 event-time
  v1 的 task synthesis、per-task/per-app virtual state、input/output schema checks、read-response semantic judge、
  structured retry、trajectory filtering、AppWorld/OfficeBench results、judge/simulator quality、yield/failure/coverage、
  training contract 与全部相关 appendices；v2 与 Apple Research page 仅作 post-window verification。评分 29/30，
  W29 更新为 34 scored + 4 unscored / 38 unique、15 reviews complete。它补全 Ch23 的 spec-only stateful
  simulation 分支，但 write API 仅做结构校验、model judge 不等于 executable truth、per-app history 不证明 cross-app
  invariant；因此真实 side-effect state、sampled execution calibration 与 final environment evaluation 必须保留。
  Historical Books Gate 继续关闭，未修改 Books。
- 同次运行随后复查 W29 剩余 cross-week identities：Distilled RL 的 arXiv HTML/PDF 与作者仓库、JoyNexus
  正文、DataFlow-Harness 正文与 artifact 均被已保存的访问策略阻断。三项按 blocked-skip 规则保持
  unscored `Unverified / Blocked`；没有把摘要中的名词扩写成机制、实验或 Books 结论。W29 仍为
  34 scored + 4 unscored / 38 unique、15 reviews complete；Historical Evidence Gate Open，Books Gate Closed。
- 同次运行完成 forward-terminal 对账：W31/W32 均有 7/7 Daily，W32 的 44 scored、24 reviewed、16 blocked、
  2 unscored gaps 与 0 ordinary pending 一致，历史 forward sweep 已抵达当前最新完整周 W32。随后从 W13
  启动 post-forward backlog sweep；ClawKeeper 与 W14 的 Backdoor Attacks / Cactus 精确重试后仍无可核验
  primary text，继续 unscored blocked，backlog cursor 进入 W15。该检查点不关闭 Historical Evidence Gate，
  也不授权 Books Integration。随后继续重试 W15 GameWorld 与 W18 ViPO / Safety Drift 的精确 primary
  入口，均仍无法取得完整正文；W16/W17 无 ordinary pending，post-forward cursor 已推进至 W19。
- 随后完成 W19 blocked retry：MolmoAct2、OpenSearch-VL、Skill1、StraTA 的精确 arXiv/题名/ID入口仍未
  返回可读 primary paper text；四项不升级为 Full Source Review，post-forward cursor 进入 W20。
- W20 Qwen-Image-2.0 的 arXiv PDF、official repository 与等价镜像重试后，46 MB report 仍无可读正文；
  保持 24/30 blocked，post-forward cursor 进入 W21。
- W21 SkillsVote、LongLive-2.0、WorldKV、QUEST 的精确 HTML/PDF/题名/ID入口也已重试；完整正文仍不可读，
  artifact 不替代 paper，四项保持 blocked，post-forward cursor 进入 W22。
- W22 的 27 项 blocked candidates 分三批逐一重试精确 arXiv HTML；全部仍无可验证正文，账目保持
  15/42 reviewed + 27 blocked，post-forward cursor 进入 W23，Books Gate 继续关闭。
- W23 的 12 项 blocked families 与 StreamMA v1 PDF 也已逐一重试；全部仍无可验证正文，W23 保持
  21/33 reviewed + 12 blocked + v1/artifact sub-gap，post-forward cursor 进入 W24。
- 同次运行完成 W30 fixed official/Infra checkpoint：复核已有 Dynamo v1.3、SGLang v0.5.16 与
  Nunchaku Lite source packets；随后关闭 14 项 pre-window identity/date attribution，但不把归周误记为
  Full Source Review。W30 保持 25 scored families、9 reviews complete、16 blocked、0 current-review
  pending；broader Historical Evidence Gate 仍 Open，Books Gate 关闭。

## Open Questions

1. 下一次 arXiv listing 是否会暴露 first-public date 实属 8 月 11～12 日、但本次索引尚未返回的候选？
2. ElastiCo 与 OasisKV 的 primary text 可访问后，是否达到 W32 retained threshold，还是仅为已有机制的
   benchmark / implementation variation？
3. SwiftQK 的 sufficient-statistic collective 原则能否获得第二个独立算子或跨互联实现证据？

## Sources

- OpenAI Research index（accessed 2026-08-12）：https://openai.com/research/index/
- Google Research index（accessed 2026-08-12）：https://research.google/blog/
- arXiv recent / new submissions（accessed 2026-08-12）：https://arxiv.org/list/cs.AI/recent
- Hugging Face Daily Papers（accessed 2026-08-12）：https://huggingface.co/papers
- OpenReview（accessed 2026-08-12）：https://openreview.net/
- OpenAlex（accessed 2026-08-12）：https://openalex.org/
- DBLP（accessed 2026-08-12）：https://dblp.org/
- vLLM releases（accessed 2026-08-12）：https://github.com/vllm-project/vllm/releases
- SGLang releases（accessed 2026-08-12）：https://github.com/sgl-project/sglang/releases
- PyTorch releases（accessed 2026-08-12）：https://github.com/pytorch/pytorch/releases
- SGLang parallel speculative-decoding roadmap（historical W23 source；accessed 2026-08-12）：
  https://github.com/sgl-project/sglang/issues/27462
- vLLM v0.22.1（historical W23 source；accessed 2026-08-12）：
  https://github.com/vllm-project/vllm/releases/tag/v0.22.1
- GitHub advisory GHSA-fgcw-684q-jj6r（historical W23 source；accessed 2026-08-12）：
  https://github.com/advisories/GHSA-fgcw-684q-jj6r
- Hugging Face Datasets 5.0.0（historical W23 source；accessed 2026-08-12）：
  https://github.com/huggingface/datasets/releases/tag/5.0.0
- KServe v0.19.0（historical W24 source；accessed 2026-08-12）：
  https://github.com/kserve/kserve/releases/tag/v0.19.0
- AA-AgentPerf methodology（historical W24 source；accessed 2026-08-12）：
  https://artificialanalysis.ai/methodology/agentperf
- NVIDIA FP8→ONNX→TensorRT engineering chain（historical W24 source；accessed 2026-08-12）：
  https://developer.nvidia.com/blog/model-quantization-turn-fp8-checkpoints-into-high-performance-inference-engines-with-nvidia-tensorrt/
- vLLM v0.23.0（historical W25 source；accessed 2026-08-12）：
  https://github.com/vllm-project/vllm/releases/tag/v0.23.0
- Recursive Harness Self-Improvement（historical W29 source；accessed 2026-08-12）：
  https://arxiv.org/abs/2607.15524
- When Does Muon Help Agentic Reinforcement Learning?（historical W29 source；accessed 2026-08-12）：
  https://arxiv.org/abs/2607.16169
- `verl-muon` official artifact（post-window verification；accessed 2026-08-12）：
  https://github.com/x66ccff/verl-muon
- Xiaomi-Robotics-1（historical W29 source；accessed 2026-08-12）：
  https://arxiv.org/abs/2607.15330
- Xiaomi-Robotics-1 official project page（accessed 2026-08-12）：
  https://robotics.xiaomi.com/xiaomi-robotics-1.html
- Xiaomi-Robotics-1 official artifact（post-window verification；accessed 2026-08-12）：
  https://github.com/XiaomiRobotics/Xiaomi-Robotics-1
- DSWorld（historical W29 source；accessed 2026-08-12）：https://arxiv.org/abs/2607.15901
- DSWorld v1 full text（accessed 2026-08-12）：https://arxiv.org/html/2607.15901v1
- DSWorld anonymous artifact（unavailable on 2026-08-12）：https://anonymous.4open.science/r/DSWorld
- Beyond Success Rate（historical W29 source；accessed 2026-08-12）：https://arxiv.org/abs/2607.15263
- Beyond Success Rate v1 full text（accessed 2026-08-12）：https://arxiv.org/html/2607.15263v1
- Frontier Evals artifact（unavailable on 2026-08-12）：https://evals.frontier.security
- SeerGuard（historical W29 source；accessed 2026-08-12）：https://arxiv.org/abs/2607.15550
- SeerGuard v1 full text（accessed 2026-08-12）：https://arxiv.org/html/2607.15550v1
- SeerGuard official project（post-window verification；accessed 2026-08-12）：https://seerguard.github.io/
- SeerGuard official evaluation artifact（post-window verification；accessed 2026-08-12）：
  https://github.com/Autonomous-Agent-Team/SeerGuard
- SAWM official weights（post-window verification；accessed 2026-08-12）：https://huggingface.co/xue-26/SAWM
- Environment-free API data（historical W29 source；accessed 2026-08-12）：https://arxiv.org/abs/2607.16900
- Environment-free API data v1 full paper（accessed 2026-08-12）：https://arxiv.org/pdf/2607.16900v1
- Apple Research page（post-window verification；accessed 2026-08-12）：
  https://machinelearning.apple.com/research/environment-free
