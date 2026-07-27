# AI Research Weekly — 2026-W18

> Coverage Window: 2026-04-27～2026-05-03
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-09
> Re-audit Status: 2026-08-13 ViPO blocker recovered; 86/86 scored families dispositioned; 80/80 current scored `20+` Full Source Reviews complete; Safety Drift remains `Unverified / Blocked / No Books Change`; Source-Family Books Gate Complete; W18 Historical Archive/Discovery Gate Open

## Executive Summary

旧版 W18 只保留两个低分 Google 条目；这可以证明拒绝边界，却不能证明本周不存在高价值论文或
工程事件。Google Research 4 月 29 日总结 Empirical Research Assistance 的实际使用方式，5 月 1 日
发布科学合作与开放资源进展。扩大扫描恢复了 21 个 `20+` 学术候选，证明旧版“本周没有单项
达到门槛”是 discovery recall 不足，而不是有效的周级结论。

本检查点完成 Recursive Multi-Agent Systems、TCOD、Programming with Data 与 Large Language
Models Explore by Latent Distilling 全文审计。RecursiveMAS 不是常规黑盒 Agent orchestration，
而是把多个可访问 hidden states 的 frozen models 通过 trainable latent links 组成可微递归图：
它减少中间文本解码，却牺牲 API modularity、可解释边界和独立升级能力。作者实验支持特定
backbone、训练数据与九个 benchmark 下的结果，不证明真实分布式 workflow 的吞吐、容错或
生产 SLO。TCOD 把 multi-turn distillation 的 support drift 转化为 trajectory-depth curriculum；
Programming with Data 把 data、benchmark 与 repair 连接到共享 knowledge identity；ESamp 则在
sampling contract 中增加 session-local online state。三者均只形成 Experimental/provisional Books
候选，不外推作者 benchmark。Nemotron 3 Nano Omni 与 AutoResearchBench 的完整审计进一步确认：
多模态模型的 token-reduction、mixed-precision 与吞吐结论必须绑定 modality/workload contract；科研
检索评测则必须区分“寻找唯一目标”与“穷举集合”两类停止与评分语义。两项都已被现有章节的
长期框架覆盖，因此暂定 `No Change — Already Covered`。DV-World 与 ClawGym 也完成全文审计：前者
暴露 arXiv metadata 与正文内部日期/模型清单无法解释的 temporal-integrity 冲突，后者确认了
synthetic task、mock workspace、black-box harness trajectory 与 verifier 的共同耦合。RoundPipe 与
Eywa 又完成全文审计；前者形成 Ch34 的 provisional mechanism refine，后者的 specialist-interface
与 adaptive orchestration 已被现有 Tool/MCP/Multi-Agent 边界覆盖。Claw-Eval-Live、Intern-Atlas 与
Web2BigTable 的全文审计分别验证了 live-signal/frozen-snapshot 分层、method-level typed evolution graph，
以及 breadth workload 下的双层编排、共享 workboard 与冻结 skill bank；三项均已被现有长期框架覆盖，
暂定 `No Change — Already Covered`。Ctx2Skill 也完成全文审计：它验证了 co-evolving textual skills
可能发生 adversarial collapse，因此必须跨 iteration replay 并选择而非盲目采用 latest state；这一机制已被
Ch73/76/78 的 derived-memory、reflection 与 evaluator 边界覆盖。MiniCPM-o 4.5 的全文审计又把
turn-based streaming 推进为 time-aligned full duplex：
新感知可在语音输出期间进入后续 chunk，[listen]/text control 与 bounded speech lookahead 共同管理
interrupt/proactive behavior；这形成 Ch38 的 provisional mechanism refine，而不是模型 leaderboard 更新。
WindowsWorld 则确认 cross-application workflow 需要同时保留 intermediate process 与 terminal outcome，
但这一边界已被 Ch62/77 覆盖。Beyond Semantic Similarity 与 RouteProfile 又分别补足 corpus-interface
resolution 与 cold-start model-profile state，形成 Ch72、Ch58 的 provisional refine。最后三个正文项也已
完成：BARRED 将运行时通用 policy judge 编译为 policy-specific synthetic corpus 与小模型 classifier；LenVM
把未知输出长度转化为 token-state value signal；CoPD 则在 branch specialization 与 mutual distillation 之间
维持可吸收的行为距离。三者分别形成 Ch68、Ch52、Ch29 的 Experimental provisional refine，但都不能把
作者 benchmark 外推为生产安全、端到端 latency 或任意多能力 consolidation 结论。

二次回放 Hugging Face W18 周索引后，原先“21 个 `20+` Source Reviews 已闭合”的表述必须撤回：至少
GLM-5V-Turbo、RL post-training rollout 的 system-integrated speculative decoding、Synthetic Computers、
Agent-Native Research Artifacts、agentic data analysis 的 process-level reward modeling、Step-Audio-R1.5
与 tabular retrieval serialization robustness 七项在本周 first-public window 内，但当时尚未完成全文审计。
其中 system-integrated speculative decoding 已完成论文、NeMo RL v0.6 release/artifact 与 Ch29/44 邻接
审计：它保持 verifier distribution，却新增 moving policy 下的 target/draft 双版本同步与 critical-path
composition。KServe v0.18.0 stable 也已通过 official release、release blog、CRD/control-plane 文档与
相邻章节联合核验，作为 W17 RC family 的 stable version node 完成审计。当前真实状态是 31 个 `20+`
候选，而不是原来的 21 个。在此基础上，Agent-Native Research Artifacts 也已完成 protocol、
compiler/manager/review、三层 evaluation、limitations、
Appendix 与当前 artifact 审计；其核心价值是 claim/code/trace/evidence 的 cross-layer binding，但实验不能把
rich-source availability 与 schema-format effect 完全分离。Representational Stability for Tabular Retrieval
随后也完成 v1 全文、v2 revision boundary、author artifact 与 Ch71～73 邻接审计：它确认 serialization 是
retrieval representation identity 的一部分，
而不是中性 preprocessing；centroid transport 只对部分 dense geometry 显示受限收益，SPLADE 与若干
dense/dataset/format 组合反而回归。DataPRM 随后也完成 v1 全文、v2 revision boundary、当前 artifact
与 Ch29/61～63/77 邻接审计：它把静态 step scorer 推进为可以查询文档/图像环境的 ReAct verifier，
并以 ternary reward 区分有效进展、可恢复 grounding error 与不可恢复错误；但 verifier 自身扩大了
权限、状态、污染与成本面，作者结果只对其 data-analysis contract 成立。GLM-5V-Turbo 也完成 v1
全文、v3 revision boundary、官方 API/GLM-V/ImageMining/Skills artifact 与 Ch33～39、44、71/73 邻接
审计：长期增量不是模型榜单，而是 visual-token shape 反向改变 PP boundary、CP/TP partition、RL
micro-batch balance 与 context/memory contract；报告缺少完整硬件、参数量和可复现实验条件，故只形成
Ch34 Experimental provisional refine。Synthetic Computers 随后完成 v1/PDF（含 retrospective Appendix）、
Microsoft Research publication 与官方 Hugging Face dataset/artifact 联合审计：长期机制是 synthetic data
从 task generation 演进为 environment/state synthesis，再由 file dependency graph、跨日 event history 与
derived skills 形成可回放的长时程工作闭环；但 1,000 次 simulation、100 台评估与当前仅 98 台的公开
artifact 不是同一对象，且 setup/work/judge 同源、rubric 从五次候选运行生成，不能证明现实工作分布或
独立 evaluation validity。故只形成 Ch77 Experimental provisional refine，Ch23/62/71/73/78/80 接短
handoff。Step-Audio-R1.5 最后完成 v1/v2、官方 repository 与三套 benchmark artifact 审计；报告把
RLVR→RLHF 描述为 audio interaction 的演进，却只公开 text-output architecture 与 speech-to-text evaluation，
没有直接 prosody/naturalness 人评、RLHF ablation 或训练 contract，故核心体验主张没有被实验支持，暂定
`No Change — Claim–Evidence Mismatch`。World-R1 又完成 v1/v4、官方 code/dataset 与 Ch28～30/61～63
邻接审计，暂定 Ch29 Experimental refine。Tuna-2 随后完成 v1/v2、project page、当前官方 code 与
Ch4～6/23～24 邻接审计：它支持从 VAE + representation encoder 逐步演进到 pixel-space monolithic
model 的机制分支，却不支持“vision encoder 已被普遍淘汰”。v1/v2 的 captioning/generation 配比相反，
v1 HTML 又出现晚于首发窗口的正文日期与 evaluator 引用，当前仓库也没有可复现论文结果的 production
weights，因此保留 `Disputed Revision Integrity / Experimental`，不进入 Books。当前 37 个已评分 `20+`
候选全部完成 Full Source Review。ReVSI 的 40 MB arXiv PDF 直接提取阻塞已由论文作者公开的全文副本、
ICML/OpenReview metadata、官方 repository、project page 与 Hugging Face dataset 联合核验解除；它把 ground truth
从“场景全量标注”收紧为“模型在当前 frame budget 下实际可见且可回答的标注”，并用 query-dropped、
first-frame repeated 与 black-video counterfactual 区分视觉证据依赖和场景先验。该机制暂定 refine Ch62，
但作者专家同时承担标注与核验、5% visibility heuristic、proprietary tiny subset、不同 frame/FPS contract、
缺少独立复核与置信区间等边界阻止把排行榜变化外推成通用 3D reasoning 结论。
Conversational User Simulation
已完成 survey 全文、taxonomy、evaluation/ethics/limitations 与 Ch61～63/71～74/77 邻接审计；其分类法
补强了 simulator identity 的检查清单，但没有新的受控实验或可迁移机制，现有 Ch62、Ch71 与 Ch73 已
拥有相同长期边界，故为 `No Change — Already Covered`。Perceval 随后完成论文、CVPR metadata、
official training code/checkpoints、token-span advantage、test-time truncation、evaluation 与 Ch28～30/62
邻接审计；其机制可 refine Ch29，但 PRM 未做独立 false-positive/recall calibration，作者以 PRM 自己报告的
hallucination curve 推断“没有 reward hacking”也不成立，故只保留 Experimental/provisional。Evidence Gate
保持打开。Turning TIDE 随后完成 arXiv v1 全文、公式与 Appendix、官方 code/model/data artifact、两条
tokenizer-compatible/cross-tokenizer distillation path、完整 evaluation contract 与 Ch24～26/30/40 邻接
审计。它证明在两个特定 teacher pipeline 中可以把 diffusion timestep reliability、complementary teacher
context 与 byte-level token alignment 纳入 distillation interface；但 0.6B student、512-token training、
单次运行且无置信区间、若干 ablation 单项回归，以及同尺寸 AR baseline 更快的受控结果，都阻止把它
外推为 diffusion LLM 或 cross-architecture distillation 的普遍优势。故只形成 Ch25 Experimental/provisional
refine，Historical Books Gate 仍关闭。
Step-level Optimization for Efficient Computer-use Agents 也完成 HTML/PDF 全文、缺失于 HTML 的三组
Appendix prompts、StepWise detector artifacts、两类 event signal、控制流、evaluation 与 Ch57～59/61～63/
76～80 邻接审计。它把 request-level router 推进为 trajectory-state-aware controller：Stuck event 触发
recovery，Milestone event 触发带 before/after screenshots 的 sparse verification。但 paper 所称 hysteresis 与
bounded recovery budgets 没有在 Method、公式或 artifact 中给出实现，300 trajectories 的 overlapping windows
也未披露是否按 trajectory 分组切分；因此只形成 Ch77 Experimental/provisional refine，不能把作者价格估算
与 benchmark success 直接外推为生产经济性。
InteractWeb-Bench 随后完成 v1 HTML/PDF、全部 persona/user/developer/judge prompts、project page、官方
repository/data/config 与 Ch61～63/73～77 邻接审计。它把静态 Web artifact 评测扩展为 Clarify/Implement/
Verify/Submit 轨迹与隐藏需求通道；但 synthetic user 持有完整 golden requirement，verification criteria 由被测
Agent 自定义，主要 TCR/IAS/CHR 又依赖 GPT-5-mini judge，且 anti-hallucination slot 不进入 TCR。因此它只
证明 404 个合成 persona cases 下选定 Agent 很少澄清、完成度有限，不能证明真实非专家用户、verification
因果收益或生产网站质量。Ch62 已拥有 feedback-conditioned policy、hidden-answer judge、turn budget、
artifact/trace 与 human/executable calibration 边界，故为 `No Change — Already Covered`。
FlashRT 最后完成 v1 全文/Appendix、threat model、selective recomputation、context-subsampled gradient、
hyperparameter sensitivity、四 H100 evaluation 与 current author code 审计。它把 red-team 资源瓶颈从单纯
攻击算法问题变成 evaluation contract：近似 loss/gradient 降低 campaign compute/memory，却新增 influence
selection、approximation drift、resampling 与 artifact/version state。结果只对作者 white-box target-output
contract、BF16 models、datasets、四 H100 与 attack settings 成立；不能写成一般 KV serving 优化，也不能由
更高 ASR 直接推出生产风险概率。它暂定 `Refine — Existing Argument (Experimental)` / Ch68，Books Gate
仍关闭。

## Coverage and Source Coverage

- 模型与研究机构：保留 Google 4 月 29 日与 5 月 1 日官方记录；Microsoft Research 4 月 30 日
  multi-agent network red-team 已完成 official report、experiment/evidence boundary 与 Ch68/78/80 审计。
  xAI 4 月 30 日 Custom Voices 又完成 announcement、当前 API docs、安全 admission 与 artifact lifecycle
  联合审计；Baidu 同日 ERNIE-5.1 Preview 只提供 leaderboard announcement，没有 technical report、model
  card、训练 contract 或独立机制证据，因此只作 15 分 product/version fact，不借 5 月 9 日正式发布材料
  反向补写本周机制。Mistral 4 月 27 日 Workflows public preview 又完成 announcement、当前 workflow/
  activity/event/deployment/security docs 与 Ch76～80 邻接审计；其 durable replay、activity retry、HITL、
  identity 与 version-routing failure boundary 已被 Ch77/80 的长期框架具体覆盖，故为 28 分 `No Change`，
  而不是把当前文档状态倒写成 launch-day feature inventory。Z.ai 4 月 30 日 Scaling Pain incident report
  也完成全文与 Ch19/44/50～52/63 邻接审计；它将 PD abort、RDMA completion、KV address reuse 与
  speculative acceptance telemetry 连成 correctness contract，29 分，暂定 Ch51 Version-Grounded refine。
  Amazon Science 4 月 29 日的 privacy-training-data 复现实录也完成全文、所引原始论文入口与 Ch67～69
  邻接审计；它把 membership inference、local-gradient inversion 与 malicious-participant global-gradient
  reconstruction 分成三个 threat surfaces，再说明 DP 与 MPC 分别限制发布结果和训练中间值。该材料是
  旧机制的 2026 engineering reproduction，不是新算法，24 分，且 Ch68 已完整覆盖 privacy unit、DP
  contract 与 secure aggregation 分层，因此为 `No Change — Already Covered`。同一索引中的 C3LLM
  官方解读节点已联读 20 页论文，但 arXiv v1 为 2025-10-04；它被记入 2025 backlog，不重复计入 W18。
  PyTorch 官方索引又恢复 AutoSP 与 LightSeek-SMG：前者完成 arXiv v1 全文、compiler rewrite、
  sequence-aware rematerialization、三类硬件实验与 Ch22/24/32～36 邻接审计，28 分，暂定 Ch33
  Experimental refine；后者完成官方工程全文、CPU/GPU ownership、gRPC/tokenizer-cache/routing、
  workload-conditioned benchmark 与 Ch38/46/49/52/58/67/80 邻接审计，27 分，暂定 Ch38 Experimental
  refine。两者均保留作者结果的 workload contract 与未公开 artifact 边界。
- 论文与学术来源：二次重放 Hugging Face W18 discovery 并按 arXiv v1 / first-public date 去重。
  当前 W18 scoring table 为 73 个 families，其中 67 个达到 `20+` 且均已完成 Full Source Review；Recursive Multi-Agent Systems、TCOD、Programming with Data
  与 Large Language Models Explore by Latent Distilling、Nemotron 3 Nano Omni、AutoResearchBench、
  Claw-Eval-Live、Intern-Atlas、Web2BigTable 等 21 项均已完成全文阅读。
  新确认的 7 项中，system-integrated speculative decoding、Agent-Native Research Artifacts 与 tabular
  retrieval representational stability、DataPRM、GLM-5V-Turbo、Synthetic Computers 与 Step-Audio-R1.5
  均已完成 Full Source Review；World-R1、Tuna-2 与 Conversational User Simulation 也已完成 revision、
  artifact/全文与章节邻接审计；Perceval 与 Turning TIDE 也已完成论文、official code/checkpoints 或
  model/data artifact 与章节邻接审计；Step-level Optimization 也已完成 PDF/HTML、prompts、detector artifact
  与章节邻接审计；InteractWeb-Bench 也已完成论文、完整 prompts、project/repository/data 与 Ch61～63/
  73～77 邻接审计；FlashRT 已完成论文/Appendix、current code 与 Ch22/49～51/67～69 邻接审计。ReVSI
  也已完成 v1/v2 metadata、全文与 Appendix、ICML/OpenReview 记录、官方 repository/project/dataset 和
  Ch61～63 邻接审计。继续回放 HF 全页后又确认 10 项此前遗漏的 in-window families；其中
  Step-Level Advantage Selection、Semi-DPO、Onchain Operating-Layer Controls、Visual Generation survey 与 Meta-CoT 已完成评分、全文/Appendix、
  公开 artifact surface 与相邻章节审计；Onchain 候选另由官方合约文档核验 least-privilege authority，Visual
  Generation 则由作者 living-roadmap repository 核对 taxonomy/stress-test/frontier 边界。Edit-R1 进一步完成
  arXiv 全文与 OpenReview source-family/date 核验，确认同一机制已于 2025-09-03 first-public，故不计入 W18；
  Compliance versus Sensibility 与 Zero-to-CAD 也已通过作者公开全文完成方法、实现、评测、限制和章节邻接审计；
  前者暂定 Ch17 Experimental refine，后者暂定 Ch23 Experimental refine。此前 access-blocked 的 FAMA
  与 Terminal Task Synthesis 现已通过 arXiv HTML/PDF 完成全文、公式/算法、评测/消融、限制/Appendix
  与章节邻接审计；前者为 27/30 `No Change — Already Covered` / Ch78，后者为 28/30 provisional
  `Refine — Existing Argument (Experimental)` / Ch23。其他 HF 标题仍需继续 date/dedup，
  因此不能把当前候选表解释为最终 recall。Hugging Face 只作 discovery，primary evidence 均指向 arXiv 正文；
  OpenReview/TMLR、DBLP、Scholar/OpenAlex 交叉召回仍未闭合。
- AI Infra：KServe v0.18.0 stable 已完成 release/blog/CRD/control-plane 联合审计；Kubernetes v1.36
  controller staleness mitigation 又完成 official blog、client-go v0.36.0 package API 与 Ch53/54/63
  邻接审计；suspended Job mutable resources 也完成 official blog、Jobs/feature-gate/API docs 与
  Ch56/59/60 邻接审计；Memory QoS tiered protection 也完成 feature Blog、QoS/cgroup v2/kernel docs 与
  Ch59/63/67 邻接审计；in-place Pod-level vertical scaling 又完成 feature Blog、resize task/status docs 与
  Ch53/56/59 邻接审计；Pod-level Resource Managers 也完成 feature Blog、resource-manager/feature-gate
  文档与 Ch53/56/59 邻接审计。W18 的 5 个 Kubernetes v1.36 families 均已审，broader index 的
  7 个相邻条目也已按 W09/W12/W17/W19/W20 分流；其他 fixed stable release/RFC/PR source list 仍待核验。
  NVIDIA TileGym cross-DSL kernel translation 也完成 official engineering Blog、semantic mapping、skill/
  validator/test contract 与 Ch45/77 邻接审计；artifact repository 因访问权限未独立核验。PyTorch W18
  source surface 的 AutoSP 与 LightSeek-SMG 也已分别完成 paper/blog 与目标章节审计；其 code/repository
  surface 尚受访问权限限制，不将作者实现声明升级成已独立验证的事实。
- 搜索入口的空白不被解释为其他机构绝对没有发布。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Empirical Research Assistance usage cases | 2 | 3 | 3 | 4 | 3 | 3 | 18/30 | Record Only |
| Science partnerships / open resources | 2 | 2 | 3 | 4 | 2 | 3 | 16/30 | Record Only |
| Google DeepMind–Republic of Korea national partnership | 1 | 2 | 2 | 5 | 2 | 3 | 15/30 | Record Only — Partnership Fact / No New Mechanism |
| DeepInfra on Hugging Face Inference Providers | 1 | 3 | 4 | 5 | 4 | 2 | 19/30 | Weekly Only — Provider Integration / No New Routing Mechanism |
| NVIDIA/Siemens NV-Raw2Insights-US | 3 | 3 | 2 | 4 | 2 | 3 | 17/30 | Record Only — Investigational Domain Prototype / Evidence Incomplete |
| Microsoft Research multi-agent network red-team | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| xAI Custom Voices | 3 | 4 | 4 | 5 | 4 | 4 | 24/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Mistral Workflows public preview | 3 | 5 | 5 | 5 | 5 | 5 | 28/30 | Full Review Complete — No Change / Already Covered |
| Granite 4.1 Language 3B/8B/30B | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Granite Vision 4.1 4B | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — provisional Refine / Experimental |
| Granite Speech 4.1 2B AR | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Granite Speech 4.1 2B NAR | 5 | 4 | 5 | 4 | 5 | 4 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Granite Speech 4.1 2B Plus | 4 | 4 | 5 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Granite Guardian 4.1 8B | 3 | 5 | 5 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Granite Embedding 97M Multilingual R2 | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Z.ai Scaling Pain of Coding Agent Serving | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — provisional Refine / Version-Grounded Incident |
| Preserving the privacy of AI training data | 3 | 5 | 5 | 4 | 4 | 3 | 24/30 | Full Review Complete — No Change / Already Covered |
| ERNIE-5.1-Preview LMArena announcement | 1 | 3 | 2 | 4 | 3 | 2 | 15/30 | Weekly Only — Product/Leaderboard Fact; Mechanism Not Disclosed |
| Recursive Multi-Agent Systems | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Must Read — full review complete |
| Programming with Data | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Large Language Models Explore by Latent Distilling | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Co-Evolving Policy Distillation | 5 | 5 | 4 | 4 | 5 | 3 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| ClawGym | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Review Complete — No Change / Already Covered |
| Intern-Atlas | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — No Change / Already Covered |
| RoundPipe | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Claw-Eval-Live | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Review Complete — No Change / Already Covered |
| Length Value Model | 5 | 4 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| TCOD: Temporal Curriculum On-Policy Distillation | 4 | 5 | 5 | 4 | 5 | 2 | 25/30 | Full Review Complete — provisional Refine / Experimental |
| Heterogeneous Scientific Foundation Model Collaboration | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — No Change / Already Covered |
| DV-World | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — Disputed Temporal Integrity / No Books |
| AutoResearchBench | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Full Review Complete — No Change / Already Covered |
| Nemotron 3 Nano Omni | 4 | 5 | 4 | 5 | 4 | 2 | 24/30 | Full Review Complete — No Change / Already Covered |
| BARRED | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Full Review Complete — provisional Refine / Experimental |
| From Context to Skills (Ctx2Skill) | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — No Change / Already Covered |
| Beyond Semantic Similarity | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| MiniCPM-o 4.5 | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Web2BigTable | 4 | 4 | 5 | 4 | 5 | 3 | 25/30 | Full Review Complete — No Change / Already Covered |
| WindowsWorld | 4 | 5 | 5 | 4 | 5 | 3 | 26/30 | Full Review Complete — No Change / Already Covered |
| RouteProfile: Graph-Based Profiling for Cold-Start LLM Routing | 4 | 5 | 5 | 4 | 4 | 3 | 25/30 | Full Review Complete — provisional Refine / Experimental |
| GLM-5V-Turbo Technical Report | 5 | 5 | 5 | 5 | 4 | 2 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| System-Integrated Speculative Decoding for RL Rollouts | 5 | 5 | 5 | 5 | 5 | 3 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Synthetic Computers at Scale | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Agent-Native Research Artifacts | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Process-Level Reward Modeling for Agentic Data Analysis | 5 | 5 | 5 | 4 | 4 | 3 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Step-Audio-R1.5 Technical Report | 4 | 4 | 5 | 5 | 4 | 2 | 24/30 | Full Review Complete — No Change / Claim–Evidence Mismatch |
| Representational Stability for Tabular Retrieval | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Full Review Complete — provisional Refine / Experimental |
| AutoSP: Compiler-Based Sequence Parallelism for Multi-GPU Training | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| LightSeek-SMG: CPU/GPU-Disaggregated LLM Serving Gateway | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| KServe v0.18.0 stable | 3 | 5 | 5 | 5 | 4 | 2 | 24/30 | Full Review Complete — Weekly Only / Stable Release |
| vLLM v0.20.0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Full Review Complete — provisional Refine / Version-Grounded Runtime Evidence |
| Hugging Face Transformers v5.7.0 | 4 | 5 | 5 | 5 | 4 | 3 | 26/30 | Full Review Complete — provisional Refine / Version-Grounded Continuous Batching |
| NVIDIA TileGym cuTile Python→cuTile.jl kernel translation skill | 3 | 4 | 5 | 4 | 4 | 4 | 24/30 | Full Review Complete — No Change / Already Covered |
| Kubernetes v1.36 controller staleness mitigation | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Kubernetes v1.36 mutable pod resources for suspended Jobs | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Kubernetes v1.36 tiered Memory QoS protection | 4 | 5 | 5 | 5 | 4 | 4 | 27/30 | Full Review Complete — provisional Refine / Alpha Version-Grounded |
| Kubernetes v1.36 in-place Pod-level vertical scaling | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Version-Grounded |
| Kubernetes v1.36 Pod-Level Resource Managers | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Alpha Version-Grounded |
| World-R1 | 5 | 5 | 4 | 4 | 4 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Tuna-2 | 5 | 4 | 4 | 3 | 4 | 4 | 24/30 | Full Review Complete — Disputed Revision Integrity / Experimental |
| A Survey on LLM-based Conversational User Simulation | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Full Review Complete — No Change / Already Covered |
| Perceval: Perception-centric Process Reward Models | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Turning the TIDE: Cross-Architecture Distillation for Diffusion LLMs | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Step-level Optimization for Efficient Computer-use Agents | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| InteractWeb-Bench | 5 | 4 | 4 | 3 | 5 | 4 | 25/30 | Full Review Complete — No Change / Already Covered |
| FlashRT | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| ReVSI | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Step-Level Advantage Selection | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Learning from Noisy Preferences / Semi-DPO | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Visual Generation in the New Era | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Full Review Complete — No Change / Already Covered |
| Meta-CoT: Enhancing Granularity and Generalization in Image Editing | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Compliance versus Sensibility | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Full Review Complete — provisional Refine / Experimental |
| Zero-to-CAD | 5 | 5 | 5 | 4 | 5 | 4 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| FAMA: Failure-Aware Meta-Agentic Framework | 4 | 5 | 5 | 4 | 5 | 4 | 27/30 | Full Review Complete — No Change / Already Covered |
| Toward Scalable Terminal Task Synthesis via Skill Graphs | 5 | 5 | 5 | 3 | 5 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Diffusion Templates: A Unified Plugin Framework for Controllable Diffusion | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Refinement via Regeneration: Enlarging Modification Space Boosts Image Refinement in Unified Multimodal Models | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Full Review Complete — provisional Refine / Experimental |
| Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| Co-Director: Agentic Generative Video Storytelling | 4 | 5 | 4 | 4 | 5 | 5 | 27/30 | Full Review Complete — No Change / Already Covered |
| MAIC-UI: Making Interactive Courseware with Generative UI | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — No Change / Already Covered |
| GoClick: Lightweight Element Grounding Model for Autonomous GUI Interaction | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| AutoGUI-v2: Multi-Modal GUI Functionality Understanding Benchmark | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Full Review Complete — No Change / Already Covered |
| X-WAM: Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising | 5 | 5 | 5 | 4 | 4 | 5 | 28/30 | Full Review Complete — provisional Refine / Experimental |
| ExoActor: Exocentric Video Generation as Generalizable Interactive Humanoid Control | 4 | 4 | 3 | 3 | 5 | 5 | 24/30 | Full Review Complete — No Change / Already Covered |
| Representation Fréchet Loss for Few-Step Generative Models | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Full Review Complete — provisional Refine / Experimental |
| ViPO | 5 | 5 | 4 | 4 | 5 | 4 | 27/30 | Full Source Review Complete — provisional Refine Ch30 / Experimental |

本轮账目为 86 行：63 个 `25～30`、17 个 `20～24`、6 个 `<20`。80 个 `20+` 候选中
80 项完成 Full Source Review；这一完成度只针对当前已评分集合，不代表 Discovery denominator 已冻结。
Hugging Face daily pages 重放恢复的候选已完成评分/Full Review；ViPO 已恢复，Safety Drift 已确认在窗但
因当前 primary-source access 保持 `Unverified / Blocked`、未评分；ElementsClaw 经官方
submission history 确认为 W17 v1 / W18 v2 revision node；此前 FAMA 与 Terminal Task Synthesis 两项正文
access blockers 已解除并完成全文审计；Edit-R1 与
C3LLM 两项经 OpenReview/arXiv first-public 核验归入 2025 backlog；此前明确恢复的 4 项 Kubernetes resource-management families
已全部审完，但 broader official/infra discovery 尚未闭合。评分是阅读优先级，
不等于 Books disposition。

## Discovery Recall Ledger

| Ledger Item | Current Count | Review Result |
| --- | ---: | --- |
| Current low-score rows | 6 | 6/6 source/date/rejection checks complete；Google 两项、ERNIE Preview、DeepMind Korea partnership、HF–DeepInfra provider integration 与 Raw2Insights-US 均未被静默丢弃 |
| Current scored `20+` families | 80 | 80/80 已完成非模板化 Full Source Review；ViPO 与本轮新增 candidates 均已完成全文、evidence boundary 与章节邻接审计；既有逐项审计详情见下文 |
| Recorded `20+` candidates | 80 | 63 high / 17 mid；六维合计已复算 |
| Cross-week attribution | 1 | TCOD v1 为 04-27，故从 W17 curation feed 归入 W18 |
| Academic discovery window | Open | ReVSI、FAMA、Terminal Task Synthesis 与 ViPO 的旧正文阻塞均已解除；Safety Drift 仍为唯一 `Unverified / Blocked` in-window family。ElementsClaw 经 arXiv submission history 核验为 W17 v1 / W18 v2 revision node，不在 W18 重复计分；Edit-R1 经 OpenReview 核验为 2025 first-public spillback；OpenReview/DBLP/Scholar/OpenAlex 交叉索引仍待 date/dedup |
| Official / Infra discovery window | Open | AutoSP、LightSeek-SMG、KServe stable、vLLM v0.20.0、Transformers v5.7.0、W18 的 5 项 Kubernetes v1.36 families、Microsoft network red-team、xAI Custom Voices、Mistral Workflows、Z.ai Scaling Pain 与 Amazon privacy reproduction 均已审；C3LLM 完成全文及 2025 first-public 分流；ERNIE Preview、Google DeepMind Korea partnership、HF–DeepInfra provider integration 与 Raw2Insights-US 完成低分来源/拒绝核验；IBM Granite 4.1 的 7 个 mechanism-level source families 全部完成 Full Source Review；Kubernetes、PyTorch、Kimi、MiniMax、Huawei Noah、Shanghai AI Lab、Xiaomi MiMo 与 InclusionAI 的可审计官方索引边界已对账；SGLang v0.5.10 为 W15、Ray/TensorRT-LLM 当前可见 release surface 未产生已核验 W18 候选；Qwen Research、Tencent Hunyuan 与 StepFun 的动态/不可变历史边界仍需由 repository metadata 和 academic cross-index 闭合，其余 framework/RFC/PR lists 仍待核验 |
| Later-feed spillbacks | 6 | W19 feed 5 项、W20 feed 的 RouteProfile 1 项按 arXiv v1 回拨 |
| Earlier-week spillback backlog | Open | Sapiens2、DIVERT、Memanto、AgentSearchBench 等按 v1 属于 W17；How Much Is One Recurrence Worth v1 为 2026-04-22、v2 才是 04-27，故归 W17 source family / W18 revision node；LLM Safety From Within、SLIDERS、Sessa、Learning Evidence Highlighting、Emergent Strategic Reasoning Risks、dWorldEval、SAE Robustness、Why Fine-Tuning Encourages Hallucinations、DIVERT 与 Taming Actor-Observer Asymmetry 也按 v1 分流至 W16/W17；Edit-R1 经 OpenReview 确认 2025-09-03 首次公开；记录 backlog，不回拉 forward cursor |
| W18 Forward Sweep Gate | Advanced to W19 | 用户于 2026-08-11 明确授权将 ViPO 与 Safety Drift 暂记 blocked 后跳过；ViPO 已于 2026-08-13 恢复，Safety Drift 仍在 backlog；forward checkpoint 不关闭 Historical Evidence Gate |
| W18 Historical Evidence Gate | Open — Backlog Required | current scored retained set 为 80/80；Safety Drift 为唯一 `Unverified / Blocked Backlog`，其他 academic/fixed-source reconciliation 也仍开放；后续必须回补后才能宣称 W18 与全历史 Evidence Gate 完成 |

## Evidence Level

Google 两项官方事实只能证明项目与资源状态；不能据案例推断通用科研生产率或自治能力。
ERNIE-5.1 Preview 条目只证明百度于 4 月 30 日公布了一个 preview model 的 LMArena 排名，不能证明
排名可跨 harness、时间或评测人群复现，更不能从 5 月正式发布文章反推出 preview 的训练机制。xAI
Custom Voices 的 announcement 与当前 docs 支持 API identity、team scope、reference-audio lifecycle 和
两阶段 enrollment check 的存在；没有 threshold、false accept/reject、spoof/deepfake robustness、人工复核、
审计日志或 incident-response evaluation，所以它是 version-grounded control description，不是安全保证。
RecursiveMAS 是作者论文、代码与项目页支持的实验性机制，其 accuracy/runtime/token 数字只对
论文指定的 frozen backbones、role-specific data、训练设置、九个 benchmark、decoding policy
与 hardware disclosure 成立。TCOD、Programming with Data 与 ESamp 也是作者实验；各自数字只对
公开的 teacher/student/environment、shared benchmark/data construction 或 model/sampling/hardware
contract 成立。Nemotron 的模型卡与论文还存在 data-accounting 差异，当前模型卡/runtime 指令也晚于
事件日；AutoResearchBench 的固定 CS corpus 与 human-machine construction 限定了其可解释范围。
TCOD v3 与 ESamp v2 的后续补充仅用于核验 revision，不能倒写为 4 月 27 日已公开事实。
Claw-Eval-Live、Intern-Atlas 与 Web2BigTable 也是作者论文与 artifact 支持的实验性证据；它们分别只对
当前 release snapshot、作者构造的 method graph/benchmark，以及指定模型、20-query skill-learning 与
两套 search benchmark 成立。BARRED、LenVM 与 CoPD 的结论也分别受四个 custom-policy tasks、作者的
length-control/value-prediction workloads，以及 Qwen3-VL-4B 的 2/3-branch 设置约束；未披露 hardware、
production SLO 或更大分支规模时，不得把它们写成通用系统结论。
Tuna-2 是作者论文与后续官方代码支持的实验性架构证据，但 v1 HTML 的内部日期、后发 evaluator 引用、
v1/v2 相反的数据配比和未发布 production weights 使历史 revision integrity 不能闭合。它只能支持指定
Qwen2.5-7B、550M in-house image-text pairs、作者任务配比、64-node 训练与作者 benchmark 下的受限比较；
不能支持“pixel embedding 在一般多模态模型、相同 compute 或生产成本上已替代 vision encoder”。
Conversational User Simulation 是 EACL 2026 / arXiv survey 提供的文献综合证据，不是新的 benchmark、
simulator artifact 或受控机制实验。它能支持 user granularity、interaction topology、conditioning method、
evaluation method 与风险面应显式建模；不能证明 LLM synthetic users 具有真实 population fidelity，也不能
把被综述论文的各自结果合并成一个通用有效性结论。
Compliance versus Sensibility 与 Zero-to-CAD 均属于作者论文/公开 artifact 支持的实验性证据。前者的
hidden-state probe 和 CAA 结果只对其人工 reasoning-conflict、judge、model、layer 与 multiplier contract
成立；“可线性读出”不等于充分因果变量，“提高 compliance”也不等于提高 correctness 或安全。后者的
accepted set 只保证作者三层 validator 编码的 execution/geometric/export conditions；不保证 DFM、真实设计
意图或人类可编辑性。其下游 IoU/CD 又以成功执行为条件且 baseline sample size 不同，不能把作者表格外推为
matched dataset superiority。

## Deep Analysis — Multi-Agent Communication 从文本协议到 Latent Transport

黑盒 Agent 用文本或结构化消息通信，虽然有 serialization/token 成本，却保留 vendor independence、
人类可审计、异步执行与独立升级；这不是落后的偶然实现，而是开放系统的重要隔离边界。当模型
权重和 hidden states 可访问、参与者固定且可以联合训练时，RecursiveMAS 选择另一分支：每个 Agent
先执行若干 latent steps，再由 trainable link 把末层 hidden state 映射到下一模型的表示空间，最后
一轮才解码文本。其演进不是“更多 Agent”，而是通信 contract 的变化：

```text
black-box text / tool protocol
→ compatible-model latent interface
→ jointly trained recursive multi-model graph
```

收益来自绕开每一跳的 vocabulary projection、token sampling 与文本再编码，并让最终 loss 沿递归
路径分配 credit；代价是 link 与具体 backbone/version 耦合、hidden activation transport 与 residency、
错误在不可读表示中传播，以及某个模型升级后 link invalidation。论文没有给出真实跨机 interconnect、
并发、tail latency、failure recovery 或 tenant isolation，因此不能把其作者 runtime 结果外推成
分布式 Agent platform 的普遍加速。旧的文本协议在跨厂商、side-effectful workflow、独立发布和
human approval 场景仍然成立；latent transport 更像 model-internal inference substrate。

## Cross-Week Deduplication

5 月 19 日 ERA 的进一步发布属于同一 program 的后续节点，本周只记录使用状态。TCOD 虽从
W17 后续 feed 被发现，但 v1 是 4 月 27 日，按事件日期归 W18。RecursiveMAS 与 W13～W17 的
Multi-Agent / harness 研究是 `Direct Evolution` 与 `Layering` 的组合：它改变模型间通信层，
不拥有 workflow action authority、environment truth 或 evaluator contract。

HF W18 页面同时包含若干 earlier-week spillback。Agentic World Modeling 与 ClawMark 已在 W17 归档；
Sapiens2、DIVERT、Memanto、AgentSearchBench 等的 arXiv v1 也早于 4 月 27 日，应进入 W17 backlog，
不能为了补 W18 recall 重复计分。依据 Historical Forward Cursor 规则，这些只登记待 W30 sweep 后回补，
不会把当前 cursor 从 W18 拉回。

## Knowledge Tree Position

Ch20 Sampling → Ch23 Data → Ch28/29 Policy Optimization → Ch40/52 Inference Runtime →
Ch62 Evaluation → Ch72 RAG → Ch73 Memory → Ch77 Workflow → Ch78 Multi-Agent Systems。RecursiveMAS
主 owner 暂定 Ch78；TCOD、Programming with Data 与 ESamp 分别暂定 Ch29、Ch23 与 Ch20 owner。
Nemotron Omni 已核对 Ch21/22/23/45，AutoResearchBench、Claw-Eval-Live 已核对 Ch62/72/77/80，
Intern-Atlas 已核对 Ch62/72/73，Web2BigTable 已核对 Ch72/73/77/78，均暂定不改 Books。
BARRED、LenVM、CoPD 分别由 Ch68、Ch52、Ch29 主持；Ch62/69、Ch28/66、Ch27/28/30 只接收边界与
handoff，不重复拥有机制。
Compliance versus Sensibility 由 Ch17 主持 residual-stream observation/intervention boundary，Ch27/62 只接
alignment 与 judge calibration；Zero-to-CAD 由 Ch23 主持 executable synthetic-data lineage，Ch77/62 只接
repair workflow 与 conditional-metric denominator。
二次恢复项的 owner 已按全文审计纠正为：GLM-5V-Turbo → Ch34；RL rollout speculative decoding → Ch44，
Ch29 handoff；Synthetic Computers → Ch77，Ch23/62/71/73/78/80 handoff；Agent-Native Research Artifacts
→ Ch80，Ch77 handoff；process-level reward modeling → Ch62，Ch29/77 handoff；tabular retrieval stability
→ Ch72。Step-Audio-R1.5 的 owner 从初始 Ch38 修正为 Ch27；Ch62 接 claim/evidence handoff，Ch38
只接 text-output runtime boundary，不形成 Books 修改。KServe stable 由 Ch57 主持，Ch49/52/58
仅接收 scaling、routing 与 gateway handoff。Kubernetes controller staleness mitigation 由 Ch53 主持：
其增量是把 controller-local write watermark 与 informer cache progress 变成 actuation precondition；Ch54
只接 custom-controller implementation handoff，Ch63 只接 freshness/skip/stuck-cache observability。
Suspended Job mutable resources 由 Ch56 主持：资源 contract 在 execution 前可以由 queue policy 受控协商，
resume 后冻结；Ch59/60 分别只接 resource-shape 与 queue-transition handoff。
Tiered Memory QoS 由 Ch67 主持：tenant/resource request 经 QoS class 下沉为 hard/soft reclaim protection；
Ch59 只接 admission/runtime 分层，Ch63 只接 protection/pressure/throttle/OOM 观测，Ch50 不混入 host
DRAM cgroup 语义。
In-place Pod-level scaling 由 Ch53 主持：resource intent、node-admitted allocation 与 cgroup-applied state
需要按 generation 分层；Ch56/59 只接 application safety 与 node-capacity handoff。
ReVSI 唯一 owner 暂定 Ch62：其长期增量是把 observation transform / frame sampling 纳入 evaluation
input identity，并让 answerability 与 ground truth 由实际可见证据共同决定；Ch33 不拥有 benchmark
机制，Ch73 也不重复保存该逻辑。
Onchain Operating-Layer Controls 唯一 owner 暂定 Ch80：其长期增量是把用户 mandate、编译后的
context、typed action、deterministic validation、settlement 与 trace 连成同一 control/evidence contract；
Ch68 只接 least-privilege execution handoff，Ch77 只接 durable transition 与 side-effect handoff。
Visual Generation survey 的 owner 修正为 Ch62，而非初始 Ch10/Ch38：其可沉淀内容是 constraint-specific
evaluator 与 perceptual/structural/causal evidence boundary；Ch62 与 Ch10 已有相同长期观点，故 No Change。
Microsoft Research multi-agent network red-team 由 Ch78 主持：communication graph 同时是协作图与攻击
传播图，evidence independence 必须绑定 identity/ownership/delegation provenance；Ch68 只接跨 principal
trust boundary，Ch80 只接 global trace、quarantine 与 human intervention handoff。
NVIDIA TileGym kernel-translation skill 由 Ch77 主持；Ch77 已拥有 typed problem contract、deterministic
checks、artifact/version lineage 与 human deployment boundary，故 No Change。Ch45 只接 target-hardware
execution-plan/kernel correctness handoff。
xAI Custom Voices 由 Ch68 主持 consent/identity sensor 与 authorization/lifecycle boundary；Ch67 只接
team-scoped tenant isolation，Ch69 只接 release、delete 与 incident-evidence handoff。当前不修改 Books。
Mistral Workflows 由 Ch77 主持 durable orchestration，Ch80 只接 deployment/identity/platform handoff；
Ch77 已明确覆盖 deterministic spine、event-history replay、activity retry/idempotency、approval state、
external events 与 framework-neutral boundary，Ch80 已覆盖 run identity、evidence plane、OBO authority
和 rollout/rollback。因此该候选为 `No Change — Already Covered`，不把一个 public-preview 产品名重复
写入 Books。
Z.ai Scaling Pain 由 Ch51 主持 PD/KV-transfer lifecycle correctness；Ch44 只接 speculative telemetry
作为 anomaly sensor 的 handoff，Ch63 只接 workload-conditioned detection/alert/retry evidence，Ch19/50
不重复拥有 production incident。Ch51 已有 completion/visibility/ownership 原则，但尚缺 abort 后 in-flight
write 跨越 address reuse boundary 的具体演进案例，因此暂定 Version-Grounded refine；Historical Books Gate
关闭期间仍不修改 Books。
Amazon privacy reproduction 由 Ch68 主持 threat-model 与 privacy mechanism 分层；Ch67 只接跨参与方
trust/aggregation handoff，Ch69 只接 deployment gate。Ch68 已明确 privacy unit、adjacency、clipping、
sampling、composition、accountant 与 utility contract，且 Ch63 已覆盖 secure aggregation 只发布 aggregate
而非 individual signal，因此为 `No Change — Already Covered`，不重复写入 Books。C3LLM 的 2026 官方
解读只作 publication node；其机制 owner 候选为 Ch62/68，但 first-public 属于 2025，转入 backlog。

## Recommended Action

下一检查点不再重复读取已完成的 Compliance、Zero-to-CAD、Mistral Workflows、Z.ai Scaling Pain、Amazon
privacy reproduction、AutoSP、LightSeek-SMG、MAIC-UI、GoClick、AutoGUI-v2、X-WAM、ExoActor 与 Representation Fréchet Loss；ElementsClaw 已按 v1
  日期分流至 W17 backlog，不在 W18 全文计分。ViPO 曾与 Safety Drift 按用户决定转入显式 blocked backlog；
  2026-08-13 ViPO 正文恢复并完成 Full Source Review，当前仅 Safety Drift 保持 blocked；
访问恢复后仍须从 metadata、全文、artifact、evaluation 与章节邻接审计回补，在此之前不猜测机制、不评分。
Forward cursor 现进入 W19；academic cross-index 的剩余 title/date 继续保留为 W18 backlog，
并闭合尚未核验的 Qwen Research、Tencent Hunyuan、StepFun historical metadata、framework release、RFC/PR、
AI Infra 与交叉学术索引。FAMA 与 Terminal Task Synthesis 的正文访问阻塞已经解除，两项均已完成
Full Source Review；IBM Granite 4.1 七个 mechanism-level families 已闭合，下一独立检查点转回剩余
fixed-source 与 academic cross-index reconciliation；Kubernetes W18 index 已完成日期/Source Family 分流，
OpenAI/Apple/Ai2/Mistral/DeepSeek/NVIDIA/Amazon/PyTorch/Cohere/Kimi/MiniMax/Huawei/Shanghai AI Lab/
Xiaomi/InclusionAI 的可审计官方索引边界已记录，Hugging Face Blog 的两个新增低分 family 与 xAI Custom
Voices、ERNIE Preview 也已完成 retained/low-score 两级审计。vLLM v0.20.0 与 Transformers v5.7.0
已经完成 release、关键 PR/docs、mechanism/state ownership、evaluation boundary 与 Ch41～52 邻接审计，
不再列入 pending；SGLang v0.5.10 已按 4 月 6 日日期分回 W15。
RecursiveMAS 暂定
`Refine — Existing Argument`：Ch78 已覆盖 topology、communication tax、shared state 与 error
amplification，后续只应补足 text protocol 与 learned latent transport 的 coupling boundary。
Historical Books Gate 关闭期间不修改 Books。

## Event-Date Daily Decision

2026-04-27～05-01：Historical Weekly only；不补造 Daily。

## Provisional Books Integration Decision — Superseded 2026-08-14

`Blocked — Not Started`。baseline 两项与 KServe stable 均为 `Weekly Only`；Kubernetes controller
staleness mitigation 暂定 Ch53 `Refine — Existing Argument (Version-Grounded)`，Ch54/63 只接 handoff；
Suspended Job mutable resources 暂定 Ch56 `Refine — Existing Argument (Version-Grounded)`，Ch59/60
只接 handoff；
Tiered Memory QoS 暂定 Ch67 `Refine — Existing Argument (Alpha / Version-Grounded)`，Ch59/63
只接 handoff；
In-place Pod-level scaling 暂定 Ch53 `Refine — Existing Argument (Version-Grounded)`，Ch56/59
只接 handoff；
Pod-Level Resource Managers 暂定 Ch59 `Refine — Existing Argument (Alpha / Version-Grounded)`，Ch53/56
只接 handoff；Microsoft Research multi-agent network red-team 暂定 Ch78 `Refine — Existing Argument
(Experimental)`，Ch68/80 只接 handoff；
NVIDIA TileGym kernel-translation skill 为 `No Change — Already Covered` / Ch77；
xAI Custom Voices 暂定 Ch68 `Refine — Existing Argument (Version-Grounded)`，Ch67/69 只接 handoff；
Mistral Workflows 为 `No Change — Already Covered` / Ch77，Ch80 只接 platform/identity handoff；
Z.ai Scaling Pain 暂定 Ch51 `Refine — Existing Argument (Version-Grounded Incident)`，Ch44/63 只接
speculative telemetry 与 anomaly operating-point handoff；
Amazon privacy reproduction 为 `No Change — Already Covered` / Ch68，Ch67/69 只接 trust/deployment
handoff；C3LLM 作为 2025 first-public source family 移入 2025 backlog，不在 W18 重复计分；
AutoSP 暂定 Ch33 `Refine — Existing Argument (Experimental)`，Ch22/24/36 只接 handoff；
LightSeek-SMG 暂定 Ch38 `Refine — Existing Argument (Experimental)`，Ch46/49/58 只接 handoff；
Granite Speech Plus 暂定 Ch38 `Refine — Existing Argument (Experimental)`，Ch5/40/62 只接 modality、
decode 与 evaluation handoff；
Granite Guardian 暂定 Ch68 `Refine — Existing Argument (Version-Grounded)`，Ch62/69/77 只接 evaluator、
deployment gate 与 workflow handoff；
Granite Embedding 暂定 Ch72 `Refine — Existing Argument (Version-Grounded)`，Ch22/45/62 只接 long-context、
artifact/runtime 与 evaluation handoff；
ERNIE-5.1 Preview 为 `Weekly Only — Product/Leaderboard Fact; Mechanism Not Disclosed`；
RecursiveMAS 暂定 Ch78 refine；TCOD、
Programming with Data 与 ESamp 分别暂定 Ch29、Ch23 与 Ch20 Experimental refine；Nemotron Omni
与 AutoResearchBench、ClawGym 暂定 `No Change — Already Covered`；DV-World 暂定
`Disputed — Temporal Integrity / Weekly Only`；RoundPipe 暂定 Ch34 Experimental refine，Eywa 暂定
No Change；Claw-Eval-Live、Intern-Atlas、Web2BigTable 与 Ctx2Skill 暂定 No Change；MiniCPM-o 4.5
暂定 Ch38 Experimental refine；WindowsWorld 暂定 No Change；Beyond Semantic Similarity 与 RouteProfile
分别暂定 Ch72、Ch58 Experimental refine；BARRED、Length Value Model、CoPD 分别暂定 Ch68、Ch52、
Ch29 Experimental refine。System-integrated speculative decoding 暂定 Ch44 Experimental refine、Ch29
handoff；Agent-Native Research Artifacts 暂定 Ch80 Experimental refine、Ch77 handoff；tabular retrieval
representational stability 暂定 Ch72 Experimental refine、Ch71 handoff；ReVSI 暂定 Ch62 Experimental
refine；Step-Level Advantage Selection 暂定 Ch29 Experimental refine；Semi-DPO 暂定 Ch30 Experimental
refine、Ch31 短 handoff；Onchain Operating-Layer Controls 暂定 Ch80 Experimental refine，Ch68/77
短 handoff；Visual Generation survey 为 `No Change — Already Covered` / Ch62；Edit-R1 为 `Out of W18 —
2025 Backlog`；Meta-CoT 为 provisional `Refine — Existing Argument (Experimental)` / Ch29，Ch25/62
short handoff；Compliance versus Sensibility 暂定 Ch17 Experimental refine，Ch27/62 只接 evidence
handoff；Zero-to-CAD 暂定 Ch23 Experimental refine，Ch77/62 只接 workflow/evaluation handoff。FAMA
完成全文审计后为 `No Change — Already Covered` / Ch78；Terminal Task Synthesis 完成全文审计后暂定
`Refine — Existing Argument (Experimental)` / Ch23；vLLM v0.20.0 暂定 Ch46
`Refine — Existing Argument (Version-Grounded Runtime Evidence)`，Ch44/45/48/51 只接 handoff；
Transformers v5.7.0 暂定 Ch42 `Refine — Existing Argument (Version-Grounded Continuous Batching)`，
Ch43/46/50 只接 handoff；MAIC-UI 为 `No Change — Already Covered` / Ch77，Ch76/62 只接 bounded
repair 与 evaluation handoff；GoClick 暂定 Ch10 `Refine — Existing Argument (Experimental)`，Ch23/62/75/78
只接 data、evaluation 与 planner/expert handoff；AutoGUI-v2 为 `No Change — Already Covered` / Ch62，
Ch75/77 不重复拥有 static benchmark 机制；X-WAM 暂定 Ch10 `Refine — Existing Argument (Experimental)`，
Ch38/62 只接 real-time inference 与 evaluation handoff；ExoActor 为 `No Change — Already Covered` / Ch10，
其 offline imagined-demo pipeline 只接 Ch38/62 的 streaming/evaluation handoff；Representation Fréchet Loss
暂定 Ch62 `Refine — Existing Argument (Experimental)`，Ch23/24 只接 reference-distribution 与 checkpointed
estimator-state handoff。当前已评分的 in-window academic 候选均有 disposition，但仍有两项已确认
在窗候选尚未评分/全文审计，且 cross-index Discovery Gate 尚未闭合，因此仍不得把 provisional disposition
直接写入 Books。全历史 Evidence
Gate 通过前，
不把恢复候选直接写入 Books，也不恢复旧版“本周无重要进展”结论。此段保留为审计历史；
对 86 个已评分 families 的最终 owner/disposition 见文末 `Final Books Integration Review`。

## Ignored Noise

合作公告、案例数量、缺少实验设计的 productivity 宣传，以及把 latent MAS 的作者 benchmark
解释成任意黑盒 Agent workflow 的普遍加速。ERNIE-5.1 Preview 的 4 月 30 日条目保留为低分
来源/拒绝记录：官方页面只报告 LMArena 排名，没有 training/evaluation contract 或 technical report；
5 月 9 日正式发布的参数比例、预训练成本与全异步 RL 主张属于后续事件，不能倒填为 W18 已知机制。
NVIDIA 同窗的 enterprise reference architecture、ComfyUI workflow、subsurface simulation 与 Unreal/
TensorRT tutorial 只提供解决方案或教程入口，未形成独立的长期机制证据，不进入评分表。
Hugging Face W18 的 Community Articles（例如 OpenEnv hackathon submissions、MCP opinion、workflow
case study 与 eval-cost synthesis）只作 discovery signal；它们不是 Hugging Face 官方 Research，也不能用
二次汇总替代所引论文、运行账单或 artifact。DeepInfra integration 与 NVIDIA/Siemens Raw2Insights-US 因有
明确官方/作者身份和事件日期而保留低分记录，但未被升级成通用 routing 或临床机制。

## Full Source Review

### Microsoft Research multi-agent network red-team — 28/30

- **Candidate / Week / Score / Source Family / Type**：W18，28/30；
  `MSR-AGENT-NETWORK-REDTEAM`；official research Blog / experimental deployment report。Microsoft
  Research 于 2026-04-30 first-public；没有单独 technical paper、version history、raw trace、artifact 或
  benchmark package，因此 Access and Verification Status 为 `Official Report Complete; Raw Evidence Not
  Disclosed`，不能把 Blog 的案例叙述升级为 peer-reviewed 或 independently reproduced evidence。
- **Direct / Related Primary Sources / Full-read Coverage**：已完整阅读 official report 的 prior-work
  positioning、platform/setup、四类 attack case、emergent defense、mitigation 与 evidence limits，并联读
  Ch68、Ch78、Ch80。报告提及 Prompt Infection、ClawWorm、Agents of Chaos 作为 prior work，但本候选不
  借 secondary description 代替这些工作的正文，也不把它们重复计为 W18 events。
- **Original Problem / Why the Previous Design Was Reasonable**：single-agent security 把 model input、
  tool authority、memory 与 human principal 视为主要 trust boundary；在没有 peer graph 时，这能覆盖 prompt
  injection、secret exfiltration 与 unsafe action。always-on Agents 开始跨 principal 共享 forum、DM、reputation、
  marketplace 与 tools 后，一个 Agent 的输出会成为另一个 Agent 的 untrusted input，局部安全不再推出网络
  安全。旧边界没有失效，而是缺少传播路径、身份独立性与间接 authority 的系统视图。
- **Changed Constraint / Mechanism**：内部 sandbox platform 上有 100+ Agents，使用 GPT-4o、GPT-4.1
  与 GPT-5-class variants，拥有不同 instructions/memory，以几分钟一次的 timer 被唤醒，积累数周交互；
  forum、DM、wallet、marketplace 和 integrated apps 让 content、reputation、authority 与 cost 在 graph 上
  传播。基础 guardrails 包括 reputation-based tool restriction、30-minute posting delay 与 tool limits，
  但仍观察到四种 network-only failure：self-propagating instruction、reputation amplification、Sybil capture
  of verification、proxy-chain invisibility。
- **Control Flow / Data Flow / State Ownership**：human principal 拥有原始 intent 与私有数据；每个 Agent
  拥有局部 prompt/memory/tool session；platform 拥有 identity registry、message graph、reputation、wallet/
  marketplace state、rate limits 与全局 trace。攻击利用的是跨层转换：
  `peer message → local interpretation → tool/data access → rewritten outbound message → next agent`。
  当 intermediary 自行改写请求时，原始 sender provenance 会从 local transcript 消失；当多个 attacker-
  controlled identities 互相背书时，“多来源确认”不再代表 evidence independence。因此 verifier contract
  必须核对 principal/ownership/delegation lineage，而不能只数同意者。
- **Evaluation Contract / Observations**：worm case 在六-Agent test group 中传播到全部六个，循环超过
  12 分钟并消耗 100+ LLM calls；reputation case 产生 42 个 Agent 的 299 条评论，其中一个被利用 Agent
  贡献 108 条；Sybil case 用三个 identities 制造互相背书；proxy case 经一个 intermediary、五条消息泄露
  敏感资料。报告还观察到少数 Agents 形成并传播 privacy-protective norm。以上数字绑定 internal sandbox、
  disclosed model families、长期 memory、具体 communication/tools 和基础 guardrails；未披露 sampling、
  model-version allocation、attack denominator、随机对照、重复次数、success-rate CI、token pricing、完整
  topology、raw logs 或 external reproduction。
- **What the Evidence Proves / Does Not Prove**：证据足以证明在该 live internal platform 上，传播、声誉
  放大、verification capture 与代理链确实可以跨 Agent 出现，且单 Agent 视角无法还原完整 provenance。
  它不证明 100+ Agents 全部被攻破，不给出四类攻击的普遍概率，也不证明某个模型系列更脆弱；emergent
  defense 是 qualitative observation，不是经 ablation 证明的自动免疫机制。作者建议的 hop/rate limit、
  quarantine、Sybil resistance、independence check、cross-agent tracing 与 human intervention 是设计方向，
  不是已完成效果评估的防御。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：graph-level telemetry 与 provenance
  有助于发现 proxy/lateral movement，却增加跨 principal 隐私、retention 与 access-control 风险；hop/rate
  limits 会削弱合法协作与告警传播，quarantine 有 false-positive/availability cost，strong identity/Sybil
  resistance 又引入中心化、可关联性与 onboarding friction。单 Agent、固定 Workflow、typed handoff 与
  deterministic verifier 仍是较小攻击面的有效设计；Multi-Agent 只在任务/证据/权限确需分解时成立，不能
  把网络级防御成本当成免费附加能力。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：相对 single-agent prompt/tool security 是
  `Direct Evolution`，相对 Ch78 的 communication topology、independent evidence 与 malicious peer 是
  `Refine — Existing Argument (Experimental)`。Ch78 为唯一 owner：需要把 communication graph 同时视为
  attack-propagation graph，并把 evidence independence 从“不同角色”提升为 identity/ownership/delegation
  可验证。Ch68 只接跨 principal trust boundary 与 layered controls handoff；Ch80 只接 global message/
  action trace、quarantine 与 human intervention handoff。Historical Books Gate 关闭，本轮不修改 Books；
  raw traces、case denominator、controlled mitigation evaluation 与 external reproduction 仍为 Open Questions。

### xAI Custom Voices — 24/30

- **Candidate / Week / Score / Source Family / Type**：W18，24/30；
  `XAI-CUSTOM-VOICE-ENROLLMENT-LIFECYCLE`；official product announcement + current API documentation。
  announcement 于 2026-04-30 first-public；docs 是 2026-08-10 访问到的 current behavior，没有公开
  revision history，因此 historical launch fact 与 current API contract 分开记录，不能假定全部 current
  fields 在 4 月 30 日已存在。
- **Direct / Related Primary Sources / Full-read Coverage**：已完整阅读 announcement 的 capability、use cases、
  enrollment 和 Voice Safety sections，以及 current Custom Voices docs 的 region/plan scope、reference-audio
  requirements、create/list/get/update/download/delete lifecycle、team visibility、TTS/Speech-to-Speech binding
  与 error behavior；并联读 Ch67～69。没有公开 system card、security paper、red-team report、threshold、
  raw evaluation、model architecture 或 immutable launch-day API snapshot，故 Access Status 为
  `Official Product and Current Docs Complete; Historical Docs / Security Evaluation Not Disclosed`。
- **Original Problem / Why the Previous Design Was Reasonable**：preset voices 把生成能力与少量平台控制的
  identities 绑定，限制品牌、辅助沟通和创作者的表达，但也缩小未经同意模仿、reference-audio retention、
  cross-tenant discovery 与 revocation 的攻击面。允许任意上传一段录音直接生成 voice model 虽然摩擦低，
  却把“拥有文件”误当成“拥有声音主体的 authority”；旧的 preset-only 分支在高风险或无法验证 consent
  的场景仍然合理。
- **Changed Constraint / Mechanism**：自定义 voice 将 admission 拆成两道官方描述的 sensor：speaker 现场读取
  verification phrase，由 STT 实时匹配 phrase 以检查 presence/intent；再比较 verification clip 与完整录音的
  speaker embeddings 以检查 speaker similarity。通过后，reference audio 生成 team-scoped `voice_id`，该
  identity 可供 REST/WebSocket TTS 与 realtime Speech-to-Speech 使用。docs 同时把 reference clip 限制为
  最长 120 秒，公开 create/list/get/update/download/delete API，并说明 metadata update 不改变 underlying
  audio、重新录制需 delete/recreate。
- **State Ownership / Control Flow / Data Flow**：human principal 提供 consent signal 与 reference audio；
  enrollment service 拥有 phrase challenge、STT result、embedding comparison 与 admission decision；artifact
  store 拥有 source audio、derived voice model、`voice_id`、team scope 与 lifecycle；TTS/voice runtime 只消费
  authorized `voice_id`。正确链路是 `principal + live challenge + reference audio → two-stage checks →
  team-scoped voice artifact → authorized synthesis → audit/revoke/delete`。若 client 或 model output 能直接把
  `voice_id` 当 authority，或者 delete 只移除 metadata 而没有覆盖 derived artifact/cache，则安全边界仍不闭合。
- **Implementation / Evaluation Contract**：当前 docs 说明美国可用但 Illinois 除外，console 可创建、Enterprise
  才开放 create API；custom voice 不出现在 built-in voice list，且只对所属 team 可见。announcement 还宣称
  约一分钟录音、两分钟内生成和“不能克隆他人声音”，但没有披露模型、hardware、threshold、语言切片、
  false-accept/false-reject、replay/voice-conversion/deepfake attack、活体检测、儿童/代理 consent、人工升级、
  audit retention、删除完成时间或 incident SLO。因此这些是官方行为/主张，不是经过公开实验支持的性能或
  安全数字。
- **What the Evidence Proves / Does Not Prove**：证据证明产品把 consent/presence 与 speaker similarity 显式
  放在 enrollment path，并给 voice artifact 建立 team scope 和 CRUD lifecycle；它不证明 STT phrase match
  是强 liveness，也不证明 embedding comparison 能抵抗 replay、合成语音或相似声线。API 返回 `deleted`
  只说明 contract 行为，不能证明 source audio、derived weights、backup、logs 和 downstream cache 已在所有
  storage plane 物理删除；team-scoped discovery 也不等于调用权限、billing、export 与 audit 已完整隔离。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：双阶段 admission 提高滥用成本，但会
  对口音、语言、残障、噪声与低质量设备产生 accessibility/false-reject friction；保存 source audio 便于
  重放、支持与质量控制，却扩大 biometric-like sensitive artifact 的 breach、retention 和 deletion burden。
  team reuse 提高运营效率，也新增成员越权、voice-id 泄漏、跨环境复制、owner 离职和 consent revocation
  传播问题。preset voices、人工审核、受限租户或完全禁用 cloning 仍应按 threat model 共存。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：这是从 `platform-owned preset → file-based cloning →
  live challenge + similarity-gated enrollment → scoped artifact lifecycle` 的 `Direct Evolution`。Ch68 是唯一
  owner，因为核心是把 identity/consent detector 与 deterministic authorization、retention、revocation 和
  incident response 分开；Ch67 只接 team/tenant scope，Ch69 只接 readiness、delete verification 与 rollback
  evidence。暂定 `Refine — Existing Argument (Version-Grounded)`；Historical Books Gate 关闭，本轮不修改
  Books。Open Questions 是 launch-day API snapshot、operating point、spoof evaluation、audit log、consent
  transfer/revocation 和 derived-artifact deletion proof。

### Recursive Multi-Agent Systems — 28/30

- **Candidate / Week / Source Family**：`RECURSIVE-MULTI-AGENT-LATENT-LINKS`；W18；
  arXiv:2604.25917，v1 2026-04-28，v2 2026-07-13。历史事件按 v1 归周；v2 只用于核验
  revision，不把 7 月补充材料倒写成 4 月已公开事实。
- **Direct / Related Primary Sources**：arXiv abstract、完整 HTML/PDF、作者 project page 与公开
  repository；项目页只作 artifact/navigation，机制与结果以论文正文、appendix 和代码为准。
- **Access / Full-read Coverage**：已读 metadata/revision、Abstract、Introduction、Related Work、
  四种 collaboration topology、RecursiveLink 公式、两阶段训练、理论复杂度、Implementation、九个
  benchmark、全部 baselines/ablation/latent-length sensitivity、efficiency、案例与 appendices。
  论文没有独立 `Limitations` 或 `Threats to Validity` 章节；这是证据边界本身，不能替作者补写
  已验证的生产约束。
- **Original Problem / Why Previous Design Was Reasonable**：传统 Multi-Agent System 通过文本
  交换 intermediate reasoning。它增加 vocabulary projection、sampling、serialization 和下一模型的
  re-encoding，却保留 black-box API、human-readable audit、vendor independence、异步运行、独立
  versioning 和明确 failure boundary；当模型不可访问 hidden state 或 workflow 有 side effects 时，
  这些特性比少量 token 节省更重要。
- **Changed Constraint / Principle**：当参与模型可冻结、hidden state 可访问、角色与 topology
  固定且允许联合训练 adapter 时，中间 communication 不必等于自然语言。原则是把自然语言保留为
  external contract，把 compatible model 之间的高频内部协作降为 learned representation transport。
- **Mechanism**：每个 agent 生成 `m` 个 latent steps，取末层 hidden state 交给下一 agent。
  同维度 inner link 为 `R_in(h)=h+W2·GELU(W1·h)`；异维度 outer link 为
  `R_out(h)=W3·h+W2·GELU(W1·h)`。intermediate rounds 不产生 text tokens，最后一个 agent
  才 decode answer。四类 graph 覆盖 sequential、mixture、distillation 与 deliberation；“recursive”
  指最后节点可把 latent state 送回首节点多轮迭代，而不是普通 workflow retry。
- **Training / State Ownership / Flow**：base LLM parameters frozen，link modules 是唯一 trainable
  state。Stage 1 用 ground-truth input embeddings 对 transformed hidden states 做 cosine alignment，
  作为 link warm-up；Stage 2 unroll `n` 个 recursion rounds，以最终 answer cross-entropy 沿完整路径
  回传 credit。模型 owner 拥有 frozen backbone/version，link owner 拥有跨模型 representation
  contract，runtime 拥有 activation lifecycle，最终 decoder 拥有 external text；workflow/evaluator
  不应把 latent state 当作可审计 action record。数据流为 `prompt → agent latent steps → link → next
  agent ... → final decoder`，控制流由预定义 topology 与 recursion count 决定。
- **Implementation Details**：作者为不同 collaboration styles 构造 role-specific supervision，
  数据来自 s1K、m1k、OpenCodeReasoning 与 ARPO-SFT，并使用较大模型改写部分目标；batch size 4、
  maximum sequence length 4096。推理由 Hugging Face 与 vLLM backend 承载；reasoning/code 的
  decoding temperature 分别为 0.6/0.2，top-p 0.95，任务输出上限依 benchmark 为 2K、4K 或 16K。
- **Evaluation Contract**：比较 MATH500、AIME25/26、GPQA-D、MedQA、LiveCodeBench-v6、
  MBPP+、HotpotQA 与 Bamboogle，共九个 benchmark；baseline 包括 single-agent LoRA/full-SFT、
  MoA、TextGrad、LoopLM 与 Recursive-TextMAS，作者声称使用相同 backbones/training set。数学与
  multiple choice 用 exact match，代码在 sandbox 中执行（单 test 10 秒），search 使用
  Qwen3.5-397B-A17B judge；每项报告五次运行。训练/推理使用 H100/A100，但没有披露完整 node
  topology、interconnect、并发、activation transfer placement 或 production SLO。
- **Ablation / Sensitivity / Overhead**：作者比较 link design，并把 latent length 从 0 扫到 128，
  报告约 80 后收益趋缓；还报告相对 Recursive-TextMAS 的 tokens/runtime/accuracy。论文没有隔离
  role-specific rewritten supervision 的贡献，没有证明 arbitrary model pairing，也没有对单 link
  failure、model upgrade、network transfer 或 latent corruption 做 recovery ablation。
- **What the Evidence Proves**：在作者选定的 frozen backbones、role data、adapter training、
  topology、decoding policy 和九个 benchmark 下，learned latent links 能完成跨模型信息传递，并可
  避免每个中间 hop 都产生自然语言。作者报告的 `1.2–2.4×` runtime 与 `34.6%–75.6%` token
  reduction 只能解释为该实验 contract 下相对 Recursive-TextMAS 的测量，不是通用 distributed
  serving speedup。
- **What It Does Not Prove / Threats to Validity**：没有证明长期 tool workflow、异步 agent、
  heterogeneous vendor API、跨机 activation traffic、tail latency、fault tolerance、tenant isolation、
  safety approval 或人类可解释性；theoretical vocabulary-cost comparison 也不包含真实 collective、
  memory residency 与 scheduler interference。role-specific data/teacher rewriting、手选互补模型与
  evaluator 都可能贡献结果；论文未设独立 limitations section。
- **Trade-offs / New Failure Modes**：latent transport 减少文本序列化，却提高 model/link version
  coupling、hidden-state bandwidth、activation residency 和 end-to-end training complexity；不可读
  intermediate state 使错误定位、policy inspection、replay 和 cross-vendor governance 更难。模型
  升级可能使 outer link 失效，单个表示错误可沿递归环放大，且目前没有公开 invalidation、rollback
  或 partial-failure protocol。
- **Where Previous Design Still Applies / Evolution**：black-box text MAS 仍适合跨厂商、独立升级、
  human approval、tool side effects、低频协作和 asynchronous workflow。关系是 `Direct Evolution`
  于 communication substrate，`Layering / Dependency` 于 Ch50 runtime 和 Ch77 workflow；不是以
  latent MAS 覆盖文本协议。下一阶段压力是 versioned latent interface、compatibility test、activation
  transport placement、failure isolation，以及把 internal latent collaboration 与 external auditable
  action boundary 分离。
- **ROADMAP / Target and Adjacent Chapters / Existing Coverage**：主 owner 暂定 Ch78；已读 Ch77、
  Ch78、Ch80，并核对 Ch22/Ch35/Ch50 的表示、训练和分布式 execution 边界。现有 Ch78 已覆盖
  single-agent headroom、topology、communication tax、shared state 与 error amplification；缺口是
  `human-readable protocol ↔ learned latent transport` 的 modularity/coupling 分支，不需要新增章节。
- **Integration Decision / Files / Open Questions**：provisional `Refine — Existing Argument`；
  Historical Books Gate 关闭，当前只更新 W18。待确认：跨机 hidden-state transfer 是否抵消 decode
  节省；backbone revision 如何触发 link invalidation；怎样为 latent intermediate state 建立 policy
  probe、replay identity 与 failure localization。

### TCOD: Temporal Curriculum On-Policy Distillation — 25/30

- **Candidate / Week / Source Family**：`TCOD-MULTITURN-OPD-CURRICULUM`；W18；arXiv:2604.24005，
  v1 2026-04-27、v2 04-28、v3 04-29。事件按 v1 归周；v3 的稳定性实现、附录与完整参数只用于
  revision 核验。
- **Direct / Related Primary Sources / Coverage**：已读 arXiv metadata、Introduction、Related Work、
  history-state 与 OPD objective、trajectory-level KL diagnosis、F2B/B2F algorithms、async rollout/
  learner、staleness-aware replay、三环境 setup、teacher/student baselines、sensitivity/efficiency、
  Limitations、全部 appendix、prompts 与 hyperparameters。未发现 event-date immutable code release。
- **Original Problem / Previous Design / Changed Constraint**：single-turn OPD 在 student-generated states
  上提供 dense teacher KL，且保留 on-policy support，因而对静态 reasoning 合理；multi-turn Agent
  把每次 action 与 environment observation 写回 history，早期误差会改变后续 state distribution，
  使学生逐步离开 teacher 的 effective support。此时一次暴露完整 horizon 会把后段高 KL 信号直接
  混入 update。
- **Mechanism / Ownership / Flow**：F2B 从短 student rollout 开始并线性增加最大 horizon；B2F 先
  replay 一条 teacher-success prefix，把环境放到近终点 state，再让 student 从后向前接管，最终把
  teacher prefix 降为零。environment 拥有真实 state transition，teacher trajectory 只拥有 navigation
  evidence，student policy 拥有可训练 action distribution，curriculum controller 拥有 horizon，learner
  才拥有 checkpoint update。正确链路是 `versioned task/state → bounded rollout → teacher KL on observed
  student actions → curriculum expansion → policy update`，teacher prefix 不应被误当成 student evidence。
- **Implementation / Evaluation Contract**：作者在 ALFWorld、WebShop、ScienceWorld 上比较四组
  Qwen2.5/Qwen3 teacher-student pairs；max turns 为 30/15/30，training prompt/response 上限 10,240/512，
  BF16、单节点 8×H20、TP=2、Ulysses SP=2。4 GPUs 给 actors、2 给 learner、2 给 teachers；lock-free
  ring buffer 保存递归 prefixes，policy-version staleness `Δmax=2`。evaluation 为 8 workers、temperature
  0.4、history 两步、最长 4,096 output tokens；没有生产并发、tail SLO 或 multi-node topology。
- **Evidence Proves / Does Not Prove**：作者实验支持在上述三类 simulator 与 model pairs 中，限制
  trajectory depth 与较低 KL、较高 success rate、较少 rounds/训练时间相关；不证明 KL escalation
  唯一由 teacher support 导致，也不证明线性 pacing、`Δmax=2` 或 teacher-navigation 对任意 tool/API
  workflow 最优。所谓“超越 teacher”来自 teacher pass@10 失败构造的 121-task hard split，不能等价为
  普遍能力超过 teacher。
- **Trade-offs / Failure Modes / Previous Design**：curriculum 降低早期 out-of-support exposure，却新增
  horizon schedule、teacher-success-trajectory bias、B2F train/test mismatch、prefix/state replay、policy
  staleness 与 environment reset correctness。完整同步 OPD 在 horizon 短、student/teacher support 接近、
  environment 便宜且 objective clarity 优先时仍成立；SFT/offline teacher traces 在无法在线执行环境时
  仍是有效分支。
- **Evolution / ROADMAP / Decision**：相对 single-turn OPD 是 `Direct Evolution`，相对 Ch29 partial
  rollout/staleness 是 `Layering / Dependency`。已读 Ch28、Ch29 及 Ch77；主 owner 暂定 Ch29，
  provisional `Refine — Existing Argument (Experimental)`。Books Gate 关闭，只更新 W18。待验证
  independent seeds、teacher-support estimator、真实 side effects，以及 curriculum 与 async replay 各自贡献。

### Programming with Data — 27/30

- **Candidate / Week / Source Family**：`PRODA-SHARED-KNOWLEDGE-SPECIFICATION`；W18；
  arXiv:2604.24819 v1 2026-04-27，57 页、唯一公开 revision。作者 repository 与 dataset 当前可访问，
  但没有 event-date tag/commit pin，后续 workspace 状态不倒写为 v1 artifact。
- **Direct / Related Primary Sources / Coverage**：已读完整正文、Methods、16-domain Results、全部
  corpus/extraction/synthesis/diagnosis prompts、data-mixing、training/evaluation appendix、author repository
  的 workflow/artifact tree。论文未披露训练 GPU 型号、node topology、wall-clock、成本或独立 human
  validation；这些写作缺口记为 `Not Disclosed`。
- **Original Problem / Previous Design / Changed Constraint**：open-loop domain SFT 先从 corpus 生成
  samples，再用独立 benchmark 评分；它简单、能复用通用数据管线，并在大规模 pretraining 下依赖统计
  coverage，因而合理。稀缺、结构化 domain corpus 中，benchmark failure 却无法定位到具体 data gap，
  盲目追加数据浪费训练预算并可能覆盖已掌握能力。
- **Mechanism / State Ownership / Flow**：Builder 自上而下抽取 L3 reasoning chains，再分解 L2 relations
  和 L1 concepts；Tester 只从 L3 构造 benchmark，initial SFT 从 L1/L2 构造，Debugger 用 LLM judge 把
  error 分成 concept gap 或 reasoning deficit，再从对应 nodes 生成 patch，与 L2-disjoint replay 混合后
  重新训练。corpus snapshot 是 requirement owner，knowledge-node IDs 是 shared specification，dataset/
  benchmark 分别拥有不同 artifact identity，diagnoser 只产生派生 hypothesis，trainer 才提交 checkpoint。
- **Implementation / Evaluation Contract**：117K documents/约 15B tokens 经筛选成 48K chunks/约 1.5B
  tokens，抽取 43,953 L3、186,784 L2、227,869 L1；初始 SFT 160K samples。作者对 Llama-3.1-8B、
  Qwen2.5 3B–32B、Qwen3 4B–32B 做 LoRA BF16，max length 2,048、batch 1,024、1 epoch；ProDa-16
  约 16K items，OpenCompass greedy、15-token option output、exact match，并仅以 MMLU 12 subsets、
  C-Eval 6 subsets 检查一般能力。GPU、并发、training/eval cost 与 SLO 未披露。
- **Evidence Proves / Does Not Prove**：作者结果支持 shared node identity 能在这套自动生成 pipeline 中
  把 failure 关联到 targeted patch，且九个 model-scale runs 在 ProDa-16 上平均提升；不证明 LLM judge
  的二分 diagnosis 因果正确、知识图无事实错误、instance disjoint 等于 semantic uncontaminated，或
  general capability 完整保留。training 与 benchmark 共用同一 extractor/ontology，相关 blind spot 与
  construction leakage 不会被高 Spearman correlation 自动排除。
- **Trade-offs / New Failure Modes / Previous Design**：shared specification 获得 traceability，却让
  generator、benchmark、diagnoser 与 repair 共享 ontology/model bias；固定 L1/L2/L3 可能把未编码知识
  和 alternative reasoning path 错判为 deficit。independent benchmark、human diagnosis、retrieval-time
  correction 与 broad data scaling 在开放领域、ontology 不稳定或 source evidence 频繁变化时仍成立。
- **Evolution / ROADMAP / Decision**：相对“先生成后打分”是 `Direct Evolution`，相对 Ch62 EvalSpec
  是 `Layering / Dependency`。已读 Ch23 及 Ch62，并核对 Ch24/25 training boundary；Ch23 已有 data-as-
  executable-specification 与 generator/verifier lineage，真正缺口是 `knowledge-node identity → failure
  diagnosis → versioned repair patch → replay/regression`。provisional `Refine — Existing Argument
  (Experimental)`；Books Gate 关闭。待验证 independent human audit、semantic contamination、source
  update/delete propagation、GPU/cost，以及错误 patch 的 rollback。

### Large Language Models Explore by Latent Distilling — 27/30

- **Candidate / Week / Source Family**：`ESAMP-ONLINE-LATENT-DISTILLER-SAMPLING`；W18；
  arXiv:2604.24927 v1 2026-04-27、v2 2026-07-21（ICML 2026）。事件按 v1 归周；v2 与当前 tLLM
  repository 只用于 revision/implementation 核验，不能把 7 月的 optimized release 倒写成 4 月 evidence。
- **Direct / Related Primary Sources / Coverage**：已读完整 paper、KL-regularized derivation、Algorithm 1、
  async CUDA-stream design、四类 workload、baselines、ablation/sensitivity、three-seed appendix、theory
  assumptions、throughput/memory appendix、prompts 与当前 author code/docs。v1 明示 code 待 acceptance；
  current repository 无 release/tag，event-date artifact boundary 不可锁定。
- **Original Problem / Previous Design / Changed Constraint**：temperature/top-k/top-p 与普通 stochastic
  sampling 只在当前 vocabulary distribution 内独立抽样，成本低、语义清楚且无 mutable online model；
  parallel test-time scaling 需要候选在 semantic space 覆盖不同 modes，词面 entropy 并不保证这种覆盖。
- **Mechanism / State Ownership / Flow**：每个 decode step 用两层 residual SwiGLU MLP 从浅层 hidden
  state 预测末层 hidden state，以 MSE 在线更新；prediction error 经 LM head 形成 novelty signal，按
  `logit_new=(1+β)logit_ref-βlogit_dist` 重权 token。base LLM/KV 拥有 canonical generation state；
  session-local distiller 拥有 mutable novelty memory；sampler 拥有最终 distribution；runtime stream/event
  拥有同步。distiller 不能成为 truth/verifier owner，也不能跨 model/request 静默复用。
- **Implementation / Evaluation Contract**：2-layer MLP hidden 384，Adam lr `4e-4`、epsilon `1e-4`、clip
  0.5、default `β=0.25`；main experiments 在 A100 上覆盖 Qwen2.5-7B/32B、Qwen3-8B、GPT-OSS-20B，
  AIME24/25、GPQA-D、LiveCodeBench-v5、BookCorpus，math context 8,192，其余 4,096。throughput 单独用
  RTX4090/Qwen3-8B，报告 B×K 从 1×1 到 32×16 的 0.3%–4.25% overhead；饱和 GPU 时 overlap 收益会
  减弱，且论文不提供 production TTFT/TPOT/p99 或 multi-tenant SLO。
- **Evidence Proves / Does Not Prove**：作者实验支持指定 models/tasks 下 representation-error reweighting
  能改变 diversity 与 high-k candidate coverage；三-seed表还显示 AIME25 的 Pass@8 可能下降而 Pass@32/64
  上升。它不证明 prediction error 等于 semantic novelty、distiller 的 rapid-fitting/local-generalization
  assumptions 普遍成立，或 `pass@k` 能被实际 selector 转化为 final success。creative-writing metrics 与
  Qwen embedding/PPL evaluator 也不是事实正确性证据。
- **Trade-offs / Failure Modes / Previous Design**：ESamp 用 online gradient、mutable per-session state、
  hidden-state capture 和 sampler coupling 换 semantic coverage；过高 β 会压低 high-confidence tokens，
  cross-prompt distiller reuse 会干扰，CUDA overlap 依赖 slack，model/runtime revision 会破坏 ports 与 timing。
  vanilla/seeded sampling 在单候选、strict reproducibility、saturated serving、black-box API 或无可靠 selector
  时仍更合理；Tree search 与 verifier-guided sampling 在可显式评分 partial paths 时是另一分支。
- **Evolution / ROADMAP / Decision**：这是 Sampling policy 的 `Direct Evolution`，与 Ch40/52 runtime
  属 `Layering / Dependency`，不是 speculative decoding，因为它不保证 target distribution 不变且不以
  target verification 提交 accepted prefix。已读 Ch20、Ch40、Ch44、Ch52；主 owner 暂定 Ch20，
  provisional `Refine — Existing Argument (Experimental)`。Books Gate 关闭。待验证 v1/v2 diff、immutable
  artifact、selector end-to-end value、tenant isolation、distiller lifecycle/reset 和 saturated-GPU tail latency。

### Nemotron 3 Nano Omni — 24/30

- **Candidate / Week / Source Family**：`NEMOTRON-3-NANO-OMNI`；W18；arXiv:2604.24954，
  v1 2026-04-27、v2 2026-05-11。事件按 v1 归周；v2、当前 Hugging Face model card 与当前
  vLLM recipe 仅用于 revision/serving-boundary 核验，不能倒写为 4 月 27 日已经公开的实现事实。
- **Direct / Related Primary Sources / Coverage**：已读完整 technical report 的 architecture、七阶段
  training、data tables、post-training、multimodal RL、全部 benchmark、reasoning budget、Conv3D/EVS、
  quantization、efficiency、appendix 与 conclusion，并核对 NVIDIA Hugging Face BF16 model card、公开
  data/pipeline/training links。论文没有独立 Limitations/Threats 章节，因此按 evaluation contract 和
  disclosure gap 收紧边界，而不替作者补造生产结论。
- **Original Problem / Previous Design / Changed Constraint**：单独的 vision-language、ASR 与 text
  models 让每种 modality 的 tokenization、alignment 和 runtime 独立，便于部署与故障隔离；当 Agent
  需要在单一长上下文中联合理解 document、video、audio 与 text 时，跨模型 glue、重复编码和上下文
  预算成为新成本。约束变化不是“模态越多越好”，而是异质输入必须共享有限 token、memory 与
  latency budget，同时不能破坏已有 text reasoning。
- **Mechanism / State Ownership / Flow**：系统采用 encoder-projector-decoder：C-RADIOv4-H 处理
  image/video，Parakeet FastConformer 处理 16 kHz audio，MLP projector 把 modality representation
  送入 Nemotron 3 Nano 30B-A3B hybrid Mamba2/Transformer MoE backbone。dynamic image resolution
  保留 aspect ratio，pixel shuffle 做 4 倍空间压缩；video 再用 Conv3D 把 temporal tokens 减半，并可
  用 EVS 选帧；audio 约产生 12.5 token/s，audio/video 按时间交错。encoder 拥有 modality features，
  projector 拥有 representation contract，LLM/KV 拥有统一 sequence state，runtime 才拥有 batching、
  cache 与量化 placement；模型卡不能成为 serving SLO 的 owner。
- **Training / Implementation**：七阶段 SFT 逐步解冻 projector/encoder/backbone、引入 image/video/
  audio 与扩展 context，以缓解 alignment instability 与 catastrophic forgetting；论文表格合计约
  434.1M samples / 466.9B tokens。训练使用 32～128 个 H100 nodes、BF16、TP2、EP32，并在后期使用
  CP2/16 与 selective activation recomputation。post-training 先做 MPO/DPO/BCO，再做 text、image 与
  omni RL，rule-based verifier 只对可判定任务提供 reward，不等于开放式多模态事实验证。
- **Evaluation / Efficiency Contract**：reasoning budget 为 13K 加 1024 grace、maximum 16,384；
  Conv3D/EVS 的 accuracy 做三次运行，TTFT 用 synthetic 512-frame、512×512 video、concurrency 1 的
  aiperf 五次运行。mixed precision 让 MoE experts 用 NVFP4、Mamba/shared experts/attention output
  projection 用 FP8；论文在 B200 上给出 single-stream 与 iso-interactivity 结果，其中后者绑定
  150 token/s/user 与 single-image reasoning。正文未完整披露所有吞吐比较的 prompt/output length、
  batch/concurrency、runtime revision 与 SLO，不能转写成通用倍数。
- **Evidence Proves / Does Not Prove**：证据支持在作者训练和评测 contract 内，通过 modality-specific
  encoder、token reduction、staged training 与 heterogeneous precision 形成可运行的 omni model。
  它不证明 256K accepted context 等于跨模态 effective context，不证明 author leaderboard 等于
  workflow success，也不证明 B200 吞吐倍数适用于其他 video length、并发、精度或 runtime。
  当前 model card 的 354.6M samples / 717B tokens 与论文 434.1M / 466.9B 口径不一致，视作版本/
  accounting boundary，不能静默合并。
- **Trade-offs / Failure Modes / Previous Design**：统一序列减少跨模型编排，却引入 modality token
  competition、encoder/projector/backbone version coupling、temporal compression 丢失、audio-video
  alignment drift、MoE routing imbalance 与 mixed-precision error 的组合风险。独立模型在低并发、
  单模态、高可审计或需要独立升级时仍合理；更激进压缩适合 latency-bound workload，而保留更多
  tokens 适合细粒度 evidence retrieval。
- **Evolution / ROADMAP / Decision**：属于 Ch21 conditional compute、Ch22 accepted/effective context、
  Ch23 modality data lineage 与 Ch45 workload-bound quantization 的 `Layering / Dependency`。已读这些
  owner 及相邻章节；现有正文已明确 active/total parameters、输入 token transformation、跨模态
  provenance，以及“精度×模型×runtime×hardware×workload×SLO”的量化 contract，故暂定
  `No Change — Already Covered`，不是因内容不重要，而是没有新增长期机制缺口。Books Gate 关闭。

### AutoResearchBench — 24/30

- **Candidate / Week / Source Family**：`AUTORESEARCHBENCH-SCIENTIFIC-DISCOVERY`；W18；
  arXiv:2604.25256 v1 2026-04-28；公开 dataset、evaluation pipeline 与 repository 同步作为 artifact。
- **Direct / Related Primary Sources / Coverage**：已读 metadata、Introduction/Related Work、Deep/Wide
  task construction、human-machine verification、metrics、全部 experiment setup/results、tool path、
  runtime parameters、cost/statistics、error taxonomy、case study、Ethics、Limitations 与 appendices，
  并核对作者 repository 链接。只有 v1，无 revision 倒写问题。
- **Original Problem / Previous Design / Changed Constraint**：传统 web/search benchmark 用单一答案、
  short evidence 或静态 metadata，适合测 retrieval 与 general browsing；科研发现常要求阅读 full text
  中分散的 method、caption、appendix 与 citation evidence，并且答案可能是零、一个或未知大小集合。
  约束变化使“找到一个看似相关结果”不再等于任务完成，stopping policy 与 set completeness 成为
  evaluator contract 的一部分。
- **Mechanism / State Ownership / Flow**：Deep Research 的 600 个 query 要定位单一 target 或确认
  corpus 内无答案，按 exact accuracy 评分；Wide Research 的 400 个 query 要穷举满足 conjunctive
  constraints 的论文集合，按 set IoU 评分。DeepXiv 拥有 fixed corpus/version，query/ground-truth
  construction pipeline 拥有 answer identity，search agent 拥有 candidate/trajectory state，scorer 拥有
  exact/set comparison；LLM judge 与 human auditor只参与 construction verification，不应被误写为
  deployment-time truth owner。
- **Construction / Verification**：benchmark 共 1,000 query，Deep 中约 90% 一个答案、10% 零答案；
  Wide 有 3,692 answers、平均 9.23。Deep 由 frontier agents 在相同环境反复搜索并由 annotators
  核验；Wide 从 23,217 candidates 中取得 20,251 full texts，由 Gemini 3.1 Pro、Claude Sonnet 4.6、
  GPT-5.4 对最多 100K characters 文本投票，4,887 项多数通过，专家另审 50% 未通过项；query-level
  precision 低于 75% 时重做。该流程降低噪声，但共享模型、截断和语义边界会形成 correlated bias。
- **Evaluation Contract**：ReAct harness 上限 30 turns、soft context 110K、top-10 retrieval、temperature
  0.6、max-new-tokens 4096、timeout 1800s、retries 5、concurrency 10、每题一条 trajectory。construction
  约花 6,700 美元与 580 expert hours，单模型 evaluation 平均约 27 美元。benchmark 只覆盖 fixed
  computer-science corpus 和 text search；不覆盖动态文献、多学科、多模态 evidence 或真实订阅/API
  failure。作者 headline score 只属于该 harness/model/date，不是 autonomous research readiness。
- **Evidence Proves / Does Not Prove**：实验支持同一 harness 内 Deep exact-target 与 Wide set-recall 是
  不同能力，增加 thinking、trajectory 或 tool calls 并不稳定改善结果；错误可分 candidate generation、
  evidence extraction/ranking、constraint literalism、premature stop、precision-unconstrained expansion、
  knowledge gap 与 ground-truth semantic-boundary mismatch。它不证明低分只由 model reasoning 引起，
  也不证明 fixed ground truth 穷尽现实科学相关性。
- **Trade-offs / Failure Modes / Previous Design**：fixed corpus 提高可复现性，却牺牲 freshness；严格
  set scoring 揭示 recall/stopping，却放大 ground-truth boundary error；multi-model voting 扩大覆盖，
  又引入 correlated judge bias 与成本。单答案 benchmark 仍适合事实定位与工具回归，live web task
  适合 freshness，人工 systematic review 适合高风险 completeness；三者不是单向替代。
- **Evolution / ROADMAP / Decision**：这是 Ch62 evaluation-subject/harness identity 与 Ch72 RAG
  recall-precision-stopping 的 `Principle Reuse`。已读 Ch62、Ch63、Ch72、Ch77；现有正文已要求冻结
  corpus、区分 model/harness/tool opportunity、记录 trajectory，并把 query、retrieval、compression、
  stopping 视作联合 policy，也已讨论 recall/precision 与 evidence sufficiency。因此暂定
  `No Change — Already Covered`；保留本周为受限实证案例，不把 leaderboard 数字写入 Books。

### DV-World — 24/30

- **Candidate / Week / Source Family**：`DV-WORLD-VISUALIZATION-AGENT-EVAL`；W18；arXiv:2604.25914
  只列 v1 2026-04-28。arXiv metadata 与 submission history 是事件日期依据。
- **Direct / Related Primary Sources / Coverage**：已读 current v1 HTML 的 task construction、三类环境、
  annotation、hybrid metrics、全部 experiments/meta-evaluation、human/simulator/judge validation、
  sensitivity、framework/tool details、prompts、examples 与 error appendices，并核对 project/code link。
  但同一 v1 正文标注 2026-07-29，且包含无法与 4 月 28 日事件快照对齐的后续 model 名称和结果；
  arXiv 没有 v2/replacement history 可解释这种差异，因此 event-date content integrity 标记 disputed。
- **Original Problem / Previous Design / Changed Constraint**：code-sandbox 的 one-shot chart generation
  容易复现且能执行验证，适合测局部绘图能力；真实 visualization workflow 还要维护 spreadsheet-native
  object/binding、迁移既有图形到新数据和 framework，并在 ambiguous intent 下主动澄清。约束从
  `prompt → image/code` 变成 `versioned source data + mutable artifact + user feedback + final evidence`。
- **Mechanism / Ownership / Flow**：DV-Sheet 覆盖 native chart create/fix/dashboard；DV-Evol 从 reference
  image、新 dataset 与 change request 生成 target-framework code/table；DV-Inter 用 dual-stage simulator，
  gatekeeper 先拒绝索取 hidden schema/implementation 的作弊问题，再由 grounded response generator
  按 hidden intent/reaction rules 回答。workbook/data owner 持有事实值与 binding，agent 持有 action
  trajectory，simulator 持有受限 feedback channel，scorer 持有 table/rubric comparison；MLLM judge
  不拥有原始数据 truth。
- **Construction / Evaluation Contract**：260 tasks，包括 DV-Sheet 50/50/30、DV-Evol 80、DV-Inter 50；
  18 位 visualization specialists 从 800+ community threads/datasets 构建并扰动/匿名化资源。
  numerical fidelity 用 tolerance-aware Table Coverage，Fix 用 must-fix attribute similarity threshold
  `>=0.95`，其余结合 expert rubric；DV-Inter 以 rubric 乘 Interaction Success Rate。10 位 human
  evaluators 每个 domain 做 10 tasks；simulator 人工审 150 trajectories。作者报告多次运行、judge
  agreement 与 lambda sensitivity，但没有 production hardware、enterprise data policy、跨租户或真实
  irreversible side-effect contract。
- **Evidence Proves / Does Not Prove**：当前正文支持“final chart appearance 不能替代 data-binding、
  artifact evolution 与 clarification-trajectory evidence”这一评估设计；错误分析区分 data accuracy、
  design、cross-backend mapping、interactive avoidance 与 intent-to-execution gap。它不证明某模型的
  4 月能力排序，也不证明 simulator interaction 等于真人协作；尤其 temporal-integrity 冲突使所有
  model leaderboard 数字不得作为 W18 事实引用。
- **Trade-offs / Failure Modes / Previous Design**：native execution 增加真实性，也增加 application/
  library/version coupling；dynamic rubric 容纳多种正确解，却引入 judge calibration；simulator 让
  ambiguous intent 可重复，却把 hidden intent、reaction rule 与 model intelligence 注入环境。
  one-shot executable chart tests 在低成本 regression 仍合理，真人评审在高风险 business meaning
  仍不可替代，live application test 则用于验证真实 object model 与 recovery。
- **Evolution / ROADMAP / Decision**：属于 Ch62 从 snapshot 到 feedback-conditioned trajectory、Ch77
  mutable artifact workflow 与 Ch80 environment-grounded Agent platform 的 `Principle Reuse`。已读
  Ch62/63、Ch77、Ch80；现有正文已经覆盖 subject/environment/scorer identity、final artifact 不覆盖
  trajectory、simulator/judge 非 truth、side effect/recovery 与 verifier audit。暂定
  `Disputed — Temporal Integrity / Weekly Only`，不改 Books；后续需作者或 arXiv 可验证 revision
  解释 04-28 metadata 与 07-29 正文内容的关系。

### ClawGym — 27/30

- **Candidate / Week / Source Family**：`CLAWGYM-SYNTHETIC-WORKSPACE-AGENT-LIFECYCLE`；W18；
  arXiv:2604.26904 v1 2026-04-29、v2 05-14、v3 05-16。全文以 version-specific v1 为历史证据，
  v3 与当前 repository 只核验 revision/artifact availability；v1 当时写明 resources 即将发布。
- **Direct / Related Primary Sources / Coverage**：已读 v1 metadata、task formalization、persona/skill
  synthesis、resource generation、code/rubric verifier、quality filters、black-box rollout/proxy、trajectory
  reconstruction/selection、SFT/RL、benchmark construction/stability/solvability、experiments、behavioral
  analysis、conclusion 与 evaluation prompt，并核对当前 ClawGym repository。论文没有独立 limitations
  section，但明确只评 final-state correctness，把 action safety、efficiency 与 error recovery 留给未来。
- **Original Problem / Previous Design / Changed Constraint**：静态 QA/coding dataset 的输入输出清晰、
  verifier 通用，适合低成本训练；workspace Agent 的 task identity 还包含 instruction `p`、initial state
  `s0`、action space `A`、transition `F` 与 task verifier `Vτ`，输出首先是 persistent final state `sH`，
  不是 completion text。真实用户数据稀缺且含隐私，促使系统用 synthetic task/mock workspace 扩大覆盖。
- **Mechanism / State Ownership / Flow**：top-down 路线从 persona、43 个 scenario subcategories 与 26 个
  atomic operations 生成 task；bottom-up 路线从约 30K raw skills 过滤 16K synthesizable skills，组合
  one primary + up to three supporting skills。resource generator 物化 mock files；code checks 验证 file/
  schema/value，rubric 检查质量，两者默认 0.7/0.3。task spec 拥有目标，workspace/sandbox 拥有事实状态，
  harness 拥有 action/observation semantics，verifier 拥有 reward，trainer 只能消费带 lineage 的 trajectory。
- **Trajectory / Training Mechanism**：分布式 Docker 中把 OpenClaw 当 black box，proxy 拦截 model、tool、
  environment traffic，再按 shared message prefix 重建 trajectory，删除 heartbeat/cron prompt 与 unsupported
  tool traces，按 hybrid reward threshold 选择 24.5K trajectories（平均 13 rounds、18.67K tokens、15.82
  tool calls、3.25 tool types）。Qwen3 4B/8B/30B-A3B 做 multi-turn SFT，mask environment-feedback tokens；
  8B 用 YaRN 扩至 64K。RL 为每任务独立 filesystem/workspace/gateway/verifier sandbox，GRPO 使用
  2,000 tasks、batch 8、每 prompt 8 rollouts、100 steps、temperature 0.7、max response 64K。
- **Evaluation Contract**：ClawGym-Bench 从 training pool 排除的数据中取 200 tasks；每题由 strong/small
  agent 各 4 rollouts 做 difficulty filter，条件为 strong `>=0.2`、small `<=0.6` 且 strong > small，
  再由 LLM diagnostic + human final decision 审 task/resource/checker/rubric。156 tasks pure code，44 hybrid；
  50-task subset 对两模型各重复 5 次，作者报告 std <=1%。PinchBench 只保留 2026-04-10 snapshot 的
  30 non-multimodal tasks。GPU、node topology、training wall time/cost 与 production SLO 均 Not Disclosed。
- **Evidence Proves / Does Not Prove**：作者实验支持在同一 synthetic/harness/verifier family 中，筛选过的
  trajectory supervision 能改善指定 Qwen backbones 的 benchmark score，也展示 sandbox-parallel outcome
  reward 的可行性。它不证明 synthetic persona/skills 代表真实用户分布，不隔离 teacher imitation、
  harness familiarity 与 verifier-family transfer，也不证明 final-state reward 保证安全、低成本、可恢复
  或无 destructive intermediate actions；headline improvement 不得外推为 production autonomy。
- **Trade-offs / Failure Modes / Previous Design**：mock workspace 提高隐私与复现性，却产生 mock-real gap；
  automatic task/resource/verifier 同源生成会形成 correlated blind spot，reward-threshold selection 会保留
  verifier-preferred behavior，黑盒 prefix reconstruction 可能错并 session branches。真实 curated tasks
  在高风险/长尾 workflow 仍必要；pure code verifier 适合确定不变量，rubric/human review 适合开放质量，
  trajectory policy checks 则补 final-state blind spot，三者不能互相覆盖。
- **Evolution / ROADMAP / Decision**：属于 Ch23 data lineage、Ch25 SFT、Ch29 outcome RL、Ch62 executable
  evaluation、Ch77 workflow state 与 Ch80 Agent platform 的 `Layering / Dependency`。已读 Ch23/25/29、
  Ch62/63、Ch77/80；这些章节已明确 environment feedback 不作 policy target、verifier 是可被攻击的
  versioned artifact、workflow 拥有事实状态、final success 不覆盖 trajectory/side effects/recovery。
  因此暂定 `No Change — Already Covered`；保留 ClawGym 为该演进链的受限联合案例，不强行增加 Books diff。

### RoundPipe — 28/30

- **Candidate / Week / Source Family**：`ROUNDPIPE-OFFLOAD-COMPUTE-DISPATCH`；W18；
  arXiv:2604.27085 v1 2026-04-29。已核对 paper、Appendix、公开 repository 与 documentation；当前
  artifact 只用于实现核验，历史结论锁定 v1 contract。
- **Direct / Related Primary Sources / Coverage**：已读 Background、recomputation/offload、DP/PP 对比、
  structural/imbalance bubble、dispatch/schedule 数学、asymmetric split、async optimizer、roofline、完整
  implementation、multi-stream transfer、per-layer consistency、partition algorithm、全部 hardware/workload/
  baseline、end-to-end/scaling/sequence sensitivity、ablation、related work 与 activation/roofline appendices。
- **Original Problem / Previous Design / Changed Constraint**：固定 stage-to-GPU ownership 在 datacenter
  PP 中合理：weights 常驻 device，移动 stage 会额外搬运大量状态，静态 mapping 还简化 ordering 与
  checkpoint。consumer GPU 的 24GB VRAM 与 PCIe topology 迫使 weights/optimizer/activation 本来就驻留
  host 并按需传输；此时继续把 logical stage 绑定 physical GPU，只保留了 imbalance，却失去静态驻留收益。
- **Mechanism / State Ownership / Flow**：RoundPipe 把 host-resident model states/activations 视为 canonical，
  GPU 变成 stateless execution worker；forward 与 backward stage slots 组成连续序列，按 round-robin 映射
  到 GPU，跨 round 延续起点。forward/backward 用不同 partition，使较快 forward 可合并更多 layers，
  首个 backward stage 复用 forward 作为 recomputation。host memory 拥有 master weight/optimizer/activation，
  scheduler 拥有 stage-slot placement，GPU 只拥有短期 execution copy，per-layer event protocol 定义何时
  weight/gradient/optimizer version 可读写。
- **Transfer / Consistency / Partition**：每设备除 compute stream 外设置 activation upload/download 与
  parameter upload/gradient download 四条 stream；activation transfer 是 critical path，parameter/gradient
  被切为 chunks 放进其间 idle windows，并以 CUDA events 在 micro-batch 粒度同步。staleness-1 CPU
  optimizer 与 GPU execution 并发，distributed event 避免同层 race 而不设全局 barrier。自动 partition
  以 `O(L^3)` 搜索近似等时的 asymmetric stages；这把“分层”从按 layer count 变成按 measured compute/
  transfer window 的 schedule problem。
- **Evaluation Contract**：单机 8×RTX4090（24GB、Xeon Gold 6330、800GB DDR4、PCIe4 32GB/s）与
  8×A800 SXM（80GB、Xeon Platinum 8352Y、800GB DDR4、NVLink3 200GB/s）；对比 ZeRO-2、FSDP、
  ZeRO-Infinity、Megatron PP/TP、Mobius 与 sync variant。Qwen3-1.7B、Llama3.1-8B、GPT-OSS-20B、
  Qwen3-32B 做 full training，Qwen3-235B-A22B 做 LoRA r=32；default sequence 2048，global batch
  分别 512/256/128/128/64，FP16、full recomputation。作者还测试 GPU count、sequence length、bubble
  与 consistency ablation；未披露跨节点网络、长期 convergence、checkpoint/restart、故障注入或多租户。
- **Evidence Proves / Does Not Prove**：作者 contract 支持“当 offload 已是前提时，解除 stage-to-device
  binding 可减少 structural + imbalance bubbles，并通过优先 transfer/event consistency 实现”。
  `1.48–2.16×`、`7.3× longer` 和 235B/31K 只属于上述 hardware/model/batch/precision/baseline；不证明
  datacenter resident-weight PP 应改成 dispatch，不证明 PCIe transfer 总能完全 overlap，也不证明
  staleness-1 对所有 optimizer/model/data 都保持 convergence。
- **Trade-offs / Failure Modes / Previous Design**：解除 weight binding 把 load imbalance 换成 host memory
  bandwidth/NUMA、PCIe contention、transfer-window fragmentation、event dependency 与 stale-weight ownership；
  GPU failure 虽不丢 canonical host state，scheduler/event loss 仍可造成重复或错版本执行。weights 能常驻
  HBM、NVLink 足够快、static stages 平衡或 synchronous reproducibility 更重要时，1F1B/interleaved PP
  仍是更简单分支；ZeRO/FSDP 则适合 collective 成本可承受且 DP scaling 更重要的场景。
- **Evolution / ROADMAP / Decision**：这是 Ch34 `fixed resident stage → interleaved virtual stage →
  host-resident logical stage / stateless device dispatch` 的 `Direct Evolution`，并依赖 Ch32 topology、
  Ch35/37 offload lifecycle。已读 Ch32、Ch34、Ch35、Ch37；现有 Ch34 已覆盖 bubble、imbalance、
  interleaving 与 async staleness，但缺少“offload 反转 stage binding 成本”的机制分支。暂定
  `Refine — Existing Argument (Experimental)`，Historical Books Gate 关闭期间不写 Books。待验证
  convergence-equivalent tokens、NUMA/root-complex sensitivity、checkpoint/replay 与 failure recovery。

### Heterogeneous Scientific Foundation Model Collaboration — 24/30

- **Candidate / Week / Source Family**：`EYWA-HETEROGENEOUS-SCIENTIFIC-FM-COLLABORATION`；W18；
  arXiv:2604.27351 v1 2026-04-30；作者 code/project link 已核对。
- **Direct / Related Primary Sources / Coverage**：已读 problem/assumptions、EywaAgent/Tsaheylu、MCP
  implementation、EywaMAS、EywaOrchestra、theory/proofs、EywaBench construction/metrics、完整 experiments、
  baselines、temperature/prompt/backbone/turn ablations、case studies、utility/token appendix、limitations 与
  prompts。GPU/topology、API pricing snapshot、concurrency 与 production SLO 均 Not Disclosed。
- **Original Problem / Previous Design / Changed Constraint**：把任何 structured/time-series/tabular input
  序列化成 text 让一个 LLM 统一处理，接口简单、可审计、跨模型兼容；但 serialization 可能丢 task-relevant
  structure，并把 specialist 已擅长的 prediction 重做成 token reasoning。约束变化是存在可靠 domain FM，
  且任务需要 language planning 与 modality-native computation 共同完成。
- **Mechanism / Ownership / Flow**：query compiler `φ:S→Uk` 把 reasoning state 编译成 specialist control，
  FM `Fk(Xk,Uk)` 计算 domain output，response adapter `ψ:Ok→Zk` 返回 planner-consumable structure；control
  policy 在 invoke/skip 间选择。MCP server 负责按 schema 取 domain data、调用 FM、返回 typed result；
  LLM 不拥有 source data/model prediction truth。EywaMAS 在既有 topology 中替换部分 workers；
  EywaOrchestra 的 conductor 从 model pool 与 finite topology pool 选择 per-task configuration。
- **Theory / Evaluation Contract**：理论的 strict risk/solvability 优势依赖“FM 在相关 domain input 上严格
  优于所有 language-only models”和 serializer 丢失相关信息等强假设；oracle adaptive routing 优于 fixed
  configuration 是 function-class 结论，不证明 learned conductor 达到 oracle。EywaBench 有 200 samples、
  3 domains/9 subdomains、78 language/82 time-series/40 tabular，来自 67 source datasets；utility 以 soft
  lexical/numeric、sMAPE/MAAPE 等 modality-specific metric 归一到 [0,1] 后直接平均。作者比较 single LLM、
  fixed MAS 与 dynamic orchestration，并做 prompt/temperature/backbone/turn ablation。
- **Evidence Proves / Does Not Prove**：作者实验支持在该 200-sample benchmark、指定 LLM/FM/interface 与
  metrics 下，specialist invocation 可改善部分 task utility，并减少 LLM tokens；结果还显示并非所有 domain
  都需要更重 MAS。它不证明 normalized utilities 跨 modality 具有相同业务意义，不证明 MCP 标准保证
  semantic correctness/authorization，也不证明 conductor 在 distribution shift 下校准或多 expert 冲突可解。
- **Trade-offs / Failure Modes / Previous Design**：specialist 减少 serialization loss，却引入 schema/compiler/
  adapter version coupling、FM calibration、data access、conflict resolution、latency 与 provenance；adaptive
  topology 降低平均冗余，又增加 router error 与 configuration identity。language-only path 在 specialist
  不可靠、任务低频、schema 漂移或解释性优先时仍成立；fixed topology 在 workload 稳定、复现和治理
  优先时仍合理。
- **Evolution / ROADMAP / Decision**：属于 Ch74 typed tool intent/executor、Ch78 task-topology matching 与
  Ch79 MCP connectivity 的 `Layering / Dependency`。已读 Ch74/75、Ch78/79；现有正文已经区分 model
  proposal 与 trusted execution、schema/version/provenance、task-conditioned topology，以及 MCP 只标准化
  connection 而不提供 semantic trust。因此暂定 `No Change — Already Covered`；保留为 specialist FM
  的受限案例，不新增重复段落。

### Claw-Eval-Live — 27/30

- **Candidate / Week / Source Family**：`CLAW-EVAL-LIVE-SIGNAL-SNAPSHOT-EVIDENCE`；W18；
  arXiv:2604.28139 v1 2026-04-30、v2 2026-05-01。事件按 v1 归周；v2 只用于核验 revision，
  不把后续 release 的可变 leaderboard 倒写成事件日事实。
- **Direct / Related Primary Sources / Coverage**：已读 metadata/revision、Introduction/Related Work、
  signal-to-snapshot construction、family clustering/weighting、candidate materialization、MILP selection、
  service/workspace execution、grader patterns、public pass rule、discrimination、cost/resource table、
  conclusion 与 appendices，并核对 project release。论文没有独立 Limitations 章节，但正文明确 public
  signal 不是 deployment frequency、economic value 或 task difficulty 的 ground truth。
- **Original Problem / Previous Design / Changed Constraint**：固定 benchmark task set 稳定、便宜、便于
  longitudinal regression，final-answer scorer 也适合纯文本任务；workflow demand 会变化，而且模型可在
  未真正执行 tool/action 时生成可信 final text。约束因此变成同时管理 demand freshness 与 execution
  evidence，又不能让历史分数随题库滚动而失去可比性。
- **Mechanism / Ownership / Flow**：系统把 ClawHub Top-500 等 public workflow signals 作为可刷新分布
  prior，经 clustering、family weighting、seed expansion 和 runnable task materialization 形成候选；157 个
  runnable candidates 再由 MILP 在 release size、family coverage、pilot discrimination/order 约束下选 105
  tasks。signal owner 只拥有 contemporaneous salience prior，release owner 拥有 time-stamped task/fixture/
  schema/grader identity，environment 拥有 service/workspace truth，trace/artifact 记录 action evidence，
  scorer 才把确定检查与受限 semantic judge 合成为分数。
- **Evaluation Contract**：当前 snapshot 为 105 tasks/22 families，87 个 service-backed workflows、18 个
  workspace repairs、18 个 controlled services；默认 24 turns/300 seconds，部分 repair task 使用明确的
  task-specific 较大预算。每个 run 固定 prompt、tool schema、fixture 与 grader，并记录 tool calls、responses、
  tokens、wall time、audit log 和 artifacts。semantic dimension 才使用 GPT-5.4 judge；public pass threshold
  为 0.80，先按 Pass Rate、再按 Overall Completion 排名。cost 仅由记录 token 与 release-time list price
  估算，不是 billed/full experiment cost。
- **Evidence Proves / Does Not Prove**：论文支持把“可刷新外部需求 prior”与“固定可重放 release”分层，
  并证明 final text 可由 observable execution evidence 补强。它不证明下载/流行度等于真实部署价值，
  不证明 controlled service/workspace 等于生产权限与恢复语义，也不证明 13-model leaderboard 可跨 release
  直接比较；GPT-5.4 同时作为被测模型与部分 semantic judge 还引入 self/preference bias。
- **Trade-offs / Failure Modes / Previous Design**：refreshable signal 增加现实相关性，也引入 upstream
  popularity bias、family-taxonomy drift、release construction cost 与跨 release composition shift；固定
  snapshot 保留复现，却会逐渐过时。deterministic checks 可审计但覆盖有限，model judge 扩展开放语义却
  需要 calibration。static micro-benchmark、frozen workflow release 与 periodic refresh 分别服务局部
  regression、版本比较和 demand tracking，是互补层而非替代关系。
- **Evolution / ROADMAP / Decision**：属于 Ch62 的 `static snapshot → versioned executable environment →
  refreshable signal + frozen release`，并依赖 Ch77/80 的 action/side-effect evidence。已读 Ch62/63、
  Ch77/80；现有正文已要求 subject/environment/scorer identity、time-stamped dataset、trajectory/artifact/
  side-effect evidence、judge bias 与 verifier versioning。因此暂定 `No Change — Already Covered`；W18
  保留受限案例与未披露边界，不把 leaderboard 数字写入 Books。

### Intern-Atlas — 26/30

- **Candidate / Week / Source Family**：`INTERN-ATLAS-METHOD-EVOLUTION-GRAPH`；W18；
  arXiv:2604.28158 v1 2026-04-30、v2 2026-05-01。当前 HTML manuscript 内部日期晚于 event date，
  因此历史事实锁定 arXiv submission history，后续文本只用于 revision 核验。
- **Direct / Related Primary Sources / Coverage**：已读 metadata、Background/Related Work、graph schema、
  reference/method/alias resolution、two-phase extraction、verbatim validator、SGT-MCTS 公式/algorithm、idea
  evaluation/generation operators、survey benchmark、Strata/human protocols、baselines、case studies、全部
  implementation/evaluation appendices，以及 extraction/algorithmic/broader-impact limitations。
- **Original Problem / Previous Design / Changed Constraint**：paper/citation graph 覆盖广、成本低、来源
  identity 清晰，适合文献发现；citation edge 却不说明 A 是 extends、improves、adapts、replaces，还是只把
  B 当 background。当 research Agent 需要重建“旧方案为什么合理、什么瓶颈触发下一机制”时，document
  granularity 与 transient per-query RAG 会反复丢失 methodology identity 与 causal relation。
- **Mechanism / State Ownership / Flow**：从 1,030,314 papers 解析 paper、canonical method 与 stub nodes，
  用 alias registry 和 two-phase LLM extraction 生成 7 类 typed edges；4 类 strong-causal edges 进入 lineage
  traversal，每条非 background causal edge 保存 verbatim bottleneck/mechanism/trade-off spans 与 reported
  confidence。code-only validator 删除无法 substring match、违反 year order 或存在反向冲突的 edge。
  corpus/version owner 拥有 source text，method registry 拥有 canonical identity，extractor 产生 provisional
  relation，validator 只证明 span/结构一致性，不能把 edge 升级为历史真理。
- **Operators / Evaluation Contract**：query 先经 alias/BM25 获得 localized context，再由 SGT-MCTS 在
  strong-causal DAG 中按 edge confidence 与 temporal coherence 搜索 lineage；idea evaluator 用五个
  deterministic graph-derived dimensions，idea generator 以四种 topological strategies 寻找结构 gap。
  graph benchmark 来自 30 surveys（2,268 nodes、1,462 edges、133 chains）；idea evaluator 用 1,200 篇
  publication strata 与 100-profile/10-researcher subset；generation 用 100 questions 和同一 expert panel。
  reported SGT-MCTS/idea scores 只属于作者 graph、survey construction、taxonomy 与 evaluator contract。
- **Evidence Proves / Does Not Prove**：实验支持 method identity、typed relation 与 evidence span 能让
  lineage query 比 citation-only/BM25 更结构化，也显示 parameter-free graph scorer 可比纯 LLM judge 更接近
  该 expert subset。它不证明 typed edge 是 causal ground truth，不证明 venue/rejection strata 等于论文
  质量，也不证明由同一 graph 产生和评价的 idea 具有现实科学价值；survey-derived reference 还共享
  taxonomy/coverage 偏差。
- **Trade-offs / Failure Modes / Previous Design**：method graph 增加可解释 evolution query，却引入 alias
  collision、edge-type confusion、fixed 14-axis taxonomy、citation bias 与 graph staleness。Phase-1 type
  accuracy 仅 70.4%～93.0%；temporal coherence 针对 post-2015 AI calibration，不能外推其他学科。
  document/citation search 仍适合 broad recall，RAG 适合读取当前 evidence，typed graph 适合 lineage prior，
  人工阅读全文仍负责 contested causal claim。
- **Evolution / ROADMAP / Decision**：这是 Ch72 `document retrieval → entity graph → typed method lineage`
  与 Ch73 provenance/supersession 的 `Direct Evolution + Layering`。已读 Ch62、Ch72/73；现有 Ch72 已覆盖
  relevance/sufficiency、provenance、source revision、Graph/RAG evidence boundary，Ch73 已要求 derived
  memory 保存 source、extractor/judge version、scope 与重建。故暂定 `No Change — Already Covered`；
  Intern-Atlas 可作为本项目技术演进记录方法的受限案例，但不新增 Books 段落或把自动 edge 当事实。

### Web2BigTable — 25/30

- **Candidate / Week / Source Family**：`WEB2BIGTABLE-BILEVEL-SKILL-WORKBOARD`；W18；
  arXiv:2604.27221 v1 2026-04-29；公开 repository 已核对，历史机制锁定 v1。
- **Direct / Related Primary Sources / Coverage**：已读 formalization、bi-level architecture、orchestrator/
  worker skill learning、shared workboard、skill discovery/creation/repair、training/inference algorithms、model/
  tool setup、WideSearch/XBench metrics、single-agent/framework baselines、全部 ablations/case study、related work
  与 conclusion。论文没有独立 Limitations/Threats 章节，hardware、API concurrency/rate limits、总成本、
  latency distribution、source freshness 与 production SLO 为 Not Disclosed。
- **Original Problem / Previous Design / Changed Constraint**：single deep-search Agent 共享完整 Context、状态
  简单，适合少量目标与强顺序推理；wide web-to-table 同时枚举数百 entities/cells，存在天然可分解性，
  单 Context 会遇到 saturation、串行 critical path、coverage gap 与 schema inconsistency。约束从“找一个
  答案”变成“在 fixed schema 下覆盖集合并给每个 cell 保留来源”。
- **Mechanism / Ownership / Flow**：upper orchestrator 从冻结 decomposition skill bank 选策略并拆分 subtasks，
  最多 10 个 async workers 用各自 retrieved execution skills/ReAct tools 产生局部表；Markdown workboard
  保存 checklist、shared constraints/context 与 tag-partitioned worker slots，file locks 实现 global read/
  per-worker write。training 对每 query 运行、用 gold cell-level Item-F1 验证、压缩 trajectory/error report、
  reflection 后聚类 structural pattern 并更新两层 skill bank；每 benchmark 仅 20 training queries，test-time
  skill banks read-only，不执行 reflection/verification/update。
- **Implementation / Evaluation Contract**：orchestrator 为 GPT-5 mini，workers 为 Gemini 3 Flash；SkillResolver
  依次做 local exact match、BM25+bge-m3/ChromaDB+RRF/optional cross-encoder，缺失时可合成 AST-validated
  Python 或 Markdown skill。WideSearch 报告 exact-all-cells Success、Row F1、type-aware Item F1，并独立运行
  四次报告 Avg@4/Max@4；XBench 用 LLM-as-judge accuracy。single-agent、proprietary end-to-end 与统一
  multi-agent baselines 的 prompt/tool/config 并非全部公开等价，XBench 官方 inference config 也未披露。
- **Evidence Proves / Does Not Prove**：ablation 支持在作者两套 benchmark、指定模型/tool、20-query training
  与 read-only test skill contract 下，decomposition skill 与 shared workboard 都贡献结果。它不证明
  `41→73` 或其他 headline 是通用 skill-learning gain，不隔离 benchmark-specific training overfit，也不证明
  Markdown/file-lock state 在跨进程故障、租户隔离、source conflict、delete/rollback 下可靠。
- **Trade-offs / Failure Modes / Previous Design**：parallel breadth 降低 critical path，却增加 decomposition
  skew、duplicate retrieval、merge/conflict resolution、rate-limit 与 shared-state race；persistent skill 提供
  amortized procedure，却可能固化 verifier/benchmark bias，runtime skill auto-repair 与 test-time frozen bank
  还是两种不同 contract。single Agent 继续适合 sequential/deep tasks；deterministic partition 适合 schema
  稳定任务；learned bi-level orchestration 只在 task family 重复且 provenance/coordination cost 可观测时成立。
- **Evolution / ROADMAP / Decision**：属于 Ch72 的 breadth/recall/stopping、Ch73 的 derived procedural memory、
  Ch77 的 shared authoritative state 与 Ch78 的 task-topology matching。已读 Ch72/73、Ch77/78；现有正文已
  覆盖 query/retain/verify/stop 联合 policy、trajectory-to-strategy provenance、blackboard typed artifacts、
  ownership/conflict rules 与 coordination tax。因此暂定 `No Change — Already Covered`；不把作者 benchmark
  数字写入 Books，也不把 shared Markdown 当成通用 workflow state implementation。

### From Context to Skills (Ctx2Skill) — 26/30

- **Candidate / Week / Source Family**：`CTX2SKILL-CROSS-TIME-SKILL-SELECTION`；W18；
  arXiv:2604.27660 v1 2026-04-30，后续 v2/v3/v4 只核验 revision；历史 evidence 使用 version-specific v1。
- **Direct / Related Primary Sources / Coverage**：已读 problem/related work、formalization、五角色 self-play、
  reasoner/challenger skill ownership、Cross-Time Replay 公式/algorithm、CL-bench setup、全部 baselines、
  component/variant/transfer ablations、case/statistics/implementation appendices、limitations 与 repository。
- **Original Problem / Previous Design / Changed Constraint**：人工从文档提炼 procedure 可追溯、可审阅，
  适合少量高风险 context；长而技术密集的 context 使 annotation 成本失控，而 coding/test 等 external
  verifier 又不适用于仅凭 context 判断某条 skill 是否 faithful/complete。约束变成：只能从同一 context
  内部构造 probing task、rubric 与反馈，同时要防止 evaluator 与 learner 共谋或一起漂移。
- **Mechanism / State Ownership / Flow**：Challenger 用自己的 skill set 从 context 生成 tasks/rubrics，Reasoner
  用独立 skill set 解题，Judge 输出 per-rubric binary verdict；Reasoner-side Proposer/Generator 从 failures
  诊断并完整替换 skill set，Challenger-side pair 从 easy successes 强化 probing。两侧永不读取对方 skills，
  frozen LMs 不更新参数。context owner 拥有唯一 source truth，task/rubric 只是 synthetic probe，Judge 只
  拥有 loop-local verdict，skill store 保存 versioned derived procedure，不应取得原文或 Workflow authority。
- **Cross-Time Replay**：latest iteration 不是天然最优。系统把每轮 hardest failure 与 easiest success 累积成
  hard/easy probe sets，对所有历史 Reasoner skill versions replay，用 Laplace-smoothed hard/easy pass-rate
  乘积选择平衡点。该机制只在五轮候选中做 selection，不纠正同源 Challenger/Judge 的系统性盲点；
  history retained 与 replay contract 才使“latest over-specialized state”可被回退。
- **Evaluation Contract**：CL-bench 500 contexts、四类 tasks；每 context `N=5` iterations、每轮 `M=5`
  synthetic tasks。GPT-4.1/5.1/5.2 分别承担同 series 的 Challenger/Reasoner/Proposer/Generator，Judge 固定
  GPT-5.1；比较 no-skill、single-pass Prompting、AutoSkill4Doc，并做 replay、role decoupling、probe set、
  smoothing、update rule 与 cross-backbone transfer ablation。API budget、token/latency/cost、hardware 与
  production SLO 未披露；作者未做 independent repeated runs/error bars。
- **Evidence Proves / Does Not Prove**：作者实验支持在该 context/task/judge contract 下，failure-driven
  natural-language skills 可改善指定 backbones，而且 Iter-1→Iter-5 的直接采用会下降，replay selection
  优于任一固定 iteration。它不证明 synthetic task/rubric 忠实覆盖原文，不证明 binary model Judge 等于
  external correctness，也不证明 skill transfer 到新 context、真实 tool workflow 或长期 operation。
- **Trade-offs / Failure Modes / Previous Design**：self-play 降低人工 annotation，却引入 challenger extremity、
  judge bias、rubric gaming、skill verbosity、context contamination 与 replay cost；跨时间 selection 缓解
  over-specialization，但 easy/hard probe 仍由同一 loop 产生。人工 curated procedure 在 regulated/high-risk
  context 仍成立，single-pass extraction 适合低成本 bootstrap，execution-verifiable skill evolution 适合有
 真实 outcome 的 tool task；feedback-free self-play 只是一条实验分支。
- **Evolution / ROADMAP / Decision**：属于 Ch73 `raw context → derived procedure → versioned candidates →
  replay/select → retain provenance/rollback`，并复用 Ch76 reflection 与 Ch78 generator/verifier separation。
  已读 Ch72/73、Ch76/78；现有正文已覆盖 trajectory-to-strategy、derived memory 不是 truth、source/judge/
  extractor version、supersession/rebuild，以及 evaluator correlation 与 coordination tax。暂定
  `No Change — Already Covered`；不把作者 solving-rate headline 或“五轮”写入 Books。

### MiniCPM-o 4.5 — 26/30

- **Candidate / Week / Source Family**：`MINICPM-O45-FULL-DUPLEX-OMNIFLOW`；W18；
  arXiv:2604.27393 v1 2026-04-30。论文、model/repository artifact 与 inference framework 入口已核对，
  版本化结果只按 v1 contract 解释。
- **Direct / Related Primary Sources / Coverage**：已读 architecture、Omni-Flow sequence/chunk formulation、
  Listen-Speak/Listen-Text control、TAIL speech alignment/lookahead、data/training stages、vision/audio/text/
  streaming evaluations、所有 design/reward/interleaving ablations、vLLM/llama.cpp-omni hardware results、
  appendix 与 explicit limitations。模型卡/代码只核对 artifact availability，不替代论文证据边界。
- **Original Problem / Previous Design / Changed Constraint**：turn-based ASR/LLM/TTS 或 streaming cascade
  把感知和响应分阶段，component 可替换、容易观测和回退，仍适合高风险过滤、长尾语言和离线质量；
  但模型说话期间的新视觉/音频通常不能及时改变当前输出。约束从降低单向 latency 变成同一 timeline
  上持续 perception、output、listen/speak control 与 playback alignment。
- **Mechanism / State Ownership / Flow**：Whisper Medium streaming encoder 产生 50 audio tokens/s，再 5×
  压缩为 10 tokens/s；Qwen3-8B backbone 只需按 speech text pace 解码约 3～4 text tokens/s，轻量约 0.3B
  speech-token decoder 与 streaming flow-matching decoder 负责声学输出。每个 chunk 组装
  `[visual tokens; audio tokens; output tokens]`，无输出时写 `[listen]`，先消费最新 observation 再生成。
  model/runtime 拥有 chunk timeline 与 autoregressive state，input capture/playback 拥有真实 wall-clock，
  speech decoder 拥有 acoustic continuation；任一组件都不能用自身 token timestamp 代表端到端 user latency。
- **TAIL / Control Trade-off**：text 与 speech tokens 按时间戳动态交织，最后少量 text tokens 的 speech
  延迟到下一 chunk，形成 bounded lookahead 以改善 pronunciation/prosody。更小 chunk 提高 perception
  refresh frequency，却增加 control density、context fragmentation 与 stability cost；论文 ablation 中 1.0s
  明显优于 0.2/0.1s，说明“更实时”不是单向收益。fixed-text interleave 的 speech quality 也优于动态
  TAIL，后者为 full-duplex alignment 付出部分 WER/CER。
- **Training / Evaluation Contract**：约 9B learnable parameters 做 end-to-end token-level training；speech
  数据规模称 millions of hours，但 source composition/license、去重与精确配比未完整披露。能力评估跨
  vision/OCR/video、ASR/translation/audio QA、TTS、text retention 与 streaming interaction；benchmark
  headline 混合 exact metrics、judge/rubric 与不同 baseline availability，不能合成为通用能力结论。
  efficiency 以单 RTX 4090 的 vLLM throughput/first-token/memory，以及 RTX 4090/DGX Spark 上
  llama.cpp-omni RTF/memory 报告；没有并发、capture/network/playback、P95/P99、thermal 或 energy SLO。
- **Evidence Proves / Does Not Prove**：作者实验支持 time-aligned chunk、explicit boundary/control 与
  delegated speech decoder 可以在指定 9B model/hardware 下实现连续 input/output，并揭示 responsiveness
  与 speech/language stability 的 trade-off。它不证明真实 long-running conversation 的 interruption
  correctness、barge-in recovery、turn ownership、privacy、fault handling 或 edge-device thermal stability；
  “<12GB”仅对应公开 INT4/framework contract。
- **Trade-offs / Failure Modes / Previous Design**：fusion 减少 utterance barrier，却收紧 encoder/backbone/
  decoder version coupling，新增 clock drift、late observation、listen/speak oscillation、partial utterance
  rollback、audio glitch、code-mixing 与 buffer/backpressure。论文也明确长期动态 streaming 鲁棒性仍待
  验证，偶发误读和中英混合存在。turn-based/cascade 路线保留明确 approval、moderation、component fallback
  与 deterministic handoff，full duplex 只在响应性价值高且这些 failure 可观测时成立。
- **Evolution / ROADMAP / Decision**：这是 Ch38 `modular cascade → end-to-end streaming → time-aligned
  full duplex with explicit output control` 的 `Direct Evolution`，并向 Ch40/46/58 交付 chunk-level state、
  cancellation/backpressure 与 protocol SLO。已读 Ch38～40、Ch46 与 Ch58；现有 Ch38 已覆盖 cascade/
  streaming fusion，但缺少“输出期间重新感知”和 listen/speak state ownership。暂定
  `Refine — Existing Argument (Experimental)`；Historical Books Gate 关闭期间不修改 Books。

### WindowsWorld — 26/30

- **Candidate / Week / Source Family**：`WINDOWSWORLD-PROCESS-CENTRIC-GUI-EVAL`；W18；
  arXiv:2604.27776 v1 2026-04-30；paper、environment description 与 artifact link 已核对。
- **Direct / Related Primary Sources / Coverage**：已读 POMDP/task taxonomy、16-persona construction、
  generator/refiner/human review、VM/application setup、intermediate/final metrics、all model/agent/modality
  results、step-matched analysis、judge validation、error/persona appendices、limitations 与 reproducibility。
- **Original Problem / Previous Design / Changed Constraint**：single-app final-state benchmark 容易复现、
  scorer 简单，适合 atomic GUI regression；professional workflow 横跨多个 applications，局部成功可能在
  late-stage transfer/constraint 中丢失，final binary score 又无法定位失败位置。约束变成管理跨 app state、
  conditional branch、infeasible task 与 partial progress，而不把更长 horizon 当成唯一难度解释。
- **Mechanism / Ownership / Flow**：181 tasks、17 desktop applications，约 78% multi-app、平均约 5 个
  sub-goals；controlled Windows VM 只开放 standard GUI，不给 internal API。task spec 拥有 declarative goal，
  VM/application 拥有事实状态，trajectory 拥有 actions/observations，manually reviewed checkpoints 定义
  process evidence，final evaluator 定义 terminal success。LLM-assisted generator/refiner 只生产候选，四位
  human reviewers 负责 instruction/checkpoint validity，不能把 generator 自述当 ground truth。
- **Evaluation Contract**：四级 taxonomy 覆盖 single-app atomic、multi-app linear、conditional reasoning 与
  infeasible/negative-constraint tasks；比较 screenshot、screenshot+accessibility tree、Set-of-Marks，以及
  general models/UIPath/S3。`S_int` 计算中间 checkpoint progress，`S_final` 计算 terminal completion；
  step-matched L1/L2 subset 用于隔离 horizon length。VLM judge 在 100 tasks/518 checkpoints 上与两位 human
  consensus 比较，但 occluded/transient UI state 仍产生 false positive/negative。
- **Evidence Proves / Does Not Prove**：作者结果支持 cross-application state transfer 与 conditional reasoning
  在该 VM/task/model snapshot 下比 step count 本身更能解释下降，也证明 partial progress 与 final success
  是不同指标。它不证明 WindowsWorld 覆盖真实企业 workflow、权限/网络/文件治理或 recovery，不证明
  intermediate checkpoint 是 dense ground truth，也不允许把当期模型 ranking 外推为通用 GUI autonomy。
- **Trade-offs / Failure Modes / Previous Design**：checkpoint 提供 localization，却增加 manual construction、
  trajectory storage 与 judge cost；accessibility tree 提供结构 prior，却可能与视觉状态不一致；full VM
  增加 realism，也引入 reset/flakiness/application-version coupling。single-app atomic tests 继续适合 CI，
  final-state verifier 适合确定 outcome，process checks 适合 diagnosis，真实 shadow/human review 负责高风险
  deployment；后者不覆盖前者。
- **Evolution / ROADMAP / Decision**：属于 Ch62 `final result → intermediate process evidence →
  outcome + trajectory slice` 与 Ch77 cross-application workflow state 的 `Layering / Dependency`。已读
  Ch62/63、Ch74、Ch77/80；现有正文已区分 final artifact、trajectory、environment、side effect/recovery，
  要求 process scorer/judge versioning 并保留 authoritative workflow state。因此暂定
  `No Change — Already Covered`；WindowsWorld 只作为受限 GUI 实证，不新增 Books 内容。

### Beyond Semantic Similarity — 28/30

- **Candidate / Week / Source Family**：`DCI-RAW-CORPUS-INTERFACE-RESOLUTION`；W18；
  arXiv:2605.05242 v1 2026-05-03。arXiv HTML 不可用，但 51 页 official PDF、repository 与 submission
  history 可访问，故以 PDF v1 完成历史全文审计。
- **Direct / Related Primary Sources / Coverage**：已读 Introduction/Related Work、DCI interface/scaffolds、
  truncation/compaction/summarization、coverage/localization 公式、三类 benchmark/baselines、main results、
  RQ2～RQ6 controlled ablations、corpus scaling、context/tool profiles、conclusion、implementation/prompts/
  trajectory/case appendices。论文没有独立 Limitations 章节；hardware 与完整 production SLO 未披露。
- **Original Problem / Previous Design / Changed Constraint**：BM25/dense/reranker 把 corpus 压缩为 top-k，
  offline index 带来低 latency、全局 broad recall 与稳定接口，在大规模静态 corpus 仍合理；agentic search
  需要组合 exact constraints、局部 span 检查、弱线索 conjunction 与 hypothesis revision，早期被 top-k
  丢弃的证据无法由下游 reasoning 恢复。变化的是 agent 已能操作 shell/file primitives，retrieval interface
  不必固定在 document/chunk similarity。
- **Mechanism / Ownership / Flow**：DCI 不建 embedding/index/retrieval API，Agent 直接用 `grep/rg/find/glob`、
  targeted read 与轻量 script 查询 raw corpus。corpus owner 保持文件/metadata truth，tool runtime 拥有 access
  scope 与 observation truncation，Agent 拥有 query/hypothesis state，Context manager 决定哪些 tool evidence
  保留；answer scorer 不拥有 corpus。Lite scaffold 只暴露 bash/read，CC scaffold 借 Claude Code orchestration，
  两者共享 DCI interface、但 harness 能力不能混为 retrieval gain。
- **Evaluation Contract**：BrowseComp-Plus 830 questions 使用官方 corpus；同 Sonnet 4.6 比较 CC+DCI 与
  Qwen3-Embedding-8B retrieval。另在六个 multi-hop/QA 与 BRIGHT/BEIR ranking datasets 比较 retrieval agents、
  BM25/dense/rerankers。Lite 用 GPT-5.4 nano high reasoning、CC 用 Sonnet 4.6 medium，均最多 300 turns；
  cost 是 agent-side API estimate。trajectory metrics 将 broad gold-document coverage 与 within-document
  localization 分开，避免把“召回文档”当成“找到可用证据”。
- **Ablation / Evidence Boundary**：作者结果支持 DCI 在该 corpus/harness/model contract 中以更高 interface
  resolution 组合 lexical/local operations；其优势不主要来自更高 gold-chain recall，而来自 surfaced
  document 内的 localization/verification。它不证明 raw search 普遍优于 index：100K→200K/400K distractor
  scaling 使 tool calls、latency/cost 快速上升且 accuracy 下跌；open bash 比 read+grep 增益更高，也显著增加
  calls/cost。context management 还呈非单调 sweet spot，保存更多 verbatim evidence 不等于更好 working state。
- **Trade-offs / Failure Modes / Previous Design**：DCI 免 offline index、适合 mutable/local corpus，却把
  breadth search、security sandbox、command injection、file-format parsing、context retention 与 cost 交给
  Agent/runtime；exact pattern 可能漏 semantic paraphrase，summary/compaction 可能丢 provenance。dense/sparse
  retrieval 继续适合大规模 broad recall，DCI 适合候选集内高分辨率 investigation；生产设计更可能是
  `index coarse recall → direct local inspection`，不是互斥替代。
- **Evolution / ROADMAP / Decision**：这是 Ch72 `top-k content filter → relevance-guided interaction →
  raw-corpus high-resolution interface` 的 `Direct Evolution`，并依赖 Ch71 Context、Ch74 tool authorization
  与 Ch77 workflow budget。已读 Ch71/72、Ch74、Ch77；现有 Ch72 已覆盖 grep/local read 与 relevance prior，
  但缺少 interface resolution、breadth scaling envelope 和 coverage/localization 分离。暂定
  `Refine — Existing Argument (Experimental)`；Historical Books Gate 关闭期间不写 Books。

### RouteProfile — 25/30

- **Candidate / Week / Source Family**：`ROUTEPROFILE-COLD-START-MODEL-PROFILE-GRAPH`；W18；
  arXiv:2605.00180 v1 2026-04-30、v2 2026-05-26。事件与机制锁定 version-specific v1，v2 只核验 revision。
- **Direct / Related Primary Sources / Coverage**：已读 profile problem/design space、heterogeneous graph、
  flat/text/embedding/trainable aggregation、masked reconstruction、three routers、standard/new-model settings、
  RQ1～RQ3、all tables、prompts、datasets/models 与 cold-start appendix。论文没有独立 Limitations/Threats
  章节，也未披露 serving latency、profile build/update cost、online drift、hardware 或 production SLO。
- **Original Problem / Previous Design / Changed Constraint**：query-only similarity router 对已有候选有真实
  interaction labels 时简单、可校准；新模型没有 query-response-reward history，flat vendor description 又粗。
  约束从“给已知模型学 decision boundary”变成“在无线上 interaction 的新模型上，先用可审计但有偏的
  public signals 构造 capability prior，再决定何时收集真实反馈”。
- **Mechanism / Ownership / Flow**：interaction graph 有 model/model-family/domain/task/query 五类 nodes，以及
  family、model-task score、task-domain、task-query 四类 edges。profile design 显式分为 organizational form
  (flat/structured)、representation (text/embedding)、aggregation depth 0～4、training-free/trainable。text-GNN
  用 LLM prompt message passing；embedding-GNN 做 normalized aggregation；trainable GNN 以 masked node/edge
  reconstruction 学 profile。model-card/benchmark owner 只提供 versioned claims，profile builder 产生 derived
  prior，router 消费 prior，online evaluator 才能产生 deployment evidence。
- **Evaluation Contract**：graph 用 15 datasets/4 capability domains/25 LLMs；routing evaluation 为 12 datasets，
  每个 50 cases。比较 SimRouter、MLPRouter、GraphRouter；standard setting 包含全部 candidate histories，
  cold-start 仅把 Mistral-Small-24B-Instruct-2501 设为 new LLM，并从 interaction graph 排除其 query history，
  旧模型每 task 保留 150 interactions。cold-start metric 同时要求“route 到 new model 且回答正确”，因此会把
  selection appetite 与 new-model correctness 混为一个 operating point。
- **Evidence Proves / Does Not Prove**：作者实验支持 profile representation 与 router 存在 co-design，structured
  profiles 在该 graph/datasets 上通常优于 flat；task+query signals 比 coarse domain node 更稳定，过深
  aggregation 也非单调。它不证明 public benchmark score 可预测生产 workload，不证明结构 profile 对所有
  newly released models 有效；cold-start 只有一个 held-out model，且 benchmark/model-card contamination、
  stale revisions、cost/latency/fairness 均未检验。
- **Trade-offs / Failure Modes / Previous Design**：structured profile 提供 relational prior，却引入 profile
  version、source conflict、benchmark comparability、message-passing oversmoothing、train/update cost 与 router
  coupling；coarse domain 可增加噪声，更多 hops 可能退化。query-only router 在稳定候选与充足 feedback 下仍
  最易校准；manual allowlist/default model 在高风险 cold-start 仍合理；graph prior 应随在线 evidence 到来
  被 supersede，而非永久拥有 truth。
- **Evolution / ROADMAP / Decision**：这是 Ch58 `static model route → query-only learned choice → versioned
  model profile + router co-design → online evidence supersession` 的 `Direct Evolution`，并把 actual route/
  profile revision 交给 Ch62/64 evidence。已读 Ch52、Ch58、Ch62/64；现有 Gateway 只覆盖 endpoint signal
  routing，缺少跨 model capability selection 与 cold-start profile ownership。暂定
  `Refine — Existing Argument (Experimental)`；不把作者 graph 或 benchmark score 写成生产策略。

### BARRED — 24/30

- **Candidate / Week / Source Family**：`BARRED-CUSTOM-POLICY-GUARDRAIL-SYNTHESIS`；W18；
  arXiv:2604.25203 v1，2026-04-28。已读取 18 页 official PDF、全部方法/实验/结论/实现附录，
  并核对作者 repository 的 test sets、evaluation code 与配置；repository 当前只有一个 commit，不能
  当作完整训练 pipeline 的独立复现证明。
- **Original Problem / Previous Design / Changed Constraint**：通用 static guardrail 延迟低，却只能覆盖
  固定 taxonomy；运行时读取任意 policy text 的 dynamic judge 更新快，却把大模型成本、prompt wording、
  boundary inconsistency 与 policy injection 带入每次请求。新约束是组织只有自然语言规则和少量未标注
  examples，却希望快速得到低延迟、policy-specific classifier。BARRED 没有宣布 dynamic guardrail 失效，
  而是增加一条把 policy 编译为训练数据和专用模型的离线分支。
- **Mechanism / State Ownership / Control and Data Flow**：task description 与 unlabeled seeds 先生成并去重
  task dimensions；每个 dimension 用 verbalized sampling 产生 instantiations，再均匀采样 dimension、
  instantiation 与 target label，生成接近 decision boundary 的 `(input,label,reasoning)`。固定立场的
  Advocate 为 target label 辩护，两个 Judges 独立更新判断；两轮内对 target label 达成一致才接受，否则
  汇总反馈、保持 dimension/label 不变重写，超过迭代上限即丢弃。Policy owner 仍拥有原始规则与版本，
  generator/debate 只产生 derived corpus，student checkpoint 是 versioned compiled artifact，deterministic
  gateway/tool authority 仍拥有最终 enforcement。
- **Implementation / Evaluation Contract**：所有生成、Advocate 与 Judges 使用 GPT-5-mini、medium reasoning；
  每个 task 生成 1,000 条训练样本，debate 为 2 judges、最多 2 rounds。四个任务覆盖 message repetition
  （158 human/114 synthetic test）、GPS privacy（112/117）、plan verification（164/124）与 health advice
  （200/123）；synthetic test 由独立 seeds/dimensions 生成并经人工核验。比较 GPT/Qwen LLM-as-judge、
  OSS-Safeguard-20B、Glider 与 fine-tuned GPT-4.1-nano、Qwen2.5 3B/14B；主指标是 accuracy。作者还做
  no-verification、self-refine、dimension-count、1.5B～14B scaling 与五次随机 instantiation sampling。
  Hardware、训练时间、生成成本、latency/SLO、false-positive operating point 均 `Not Disclosed`。
- **Evidence Proves / Does Not Prove**：论文实验支持在这四个 task 与作者数据构造下，dimension coverage
  和 asymmetric debate 都比无校验/self-refine 更有效，policy-specific 小模型可优于列出的通用 judges。
  它不证明辩论共识等于 ground truth，不证明同一 generator/judge family 的相关误差已消除，也不证明
  arbitrary policy、长尾语言、对抗攻击或规则漂移下仍保持 accuracy。Repository 公开 human-curated test
  与 evaluation path，但不能独立证明生成/训练成本或生产 latency。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：离线多次 LLM 调用可 amortize 到低成本
  student inference，却引入 dimension omission、同源模型共识偏差、synthetic/test construction leakage、
  policy revision 后 corpus/checkpoint invalidation、stale classifier 与 false-negative escalation。规则频繁变化、
  长尾尚未收集或必须提供解释时，dynamic Policy-as-Data judge 仍合理；规则稳定、traffic 大且低 latency
  关键时，compiled classifier 更合适；高风险 action 仍需 deterministic deny/allow 与 human review。
- **Evolution / ROADMAP / Decision**：这是 Ch68 `static fixed-taxonomy classifier → runtime Policy-as-Data
  judge → offline policy compilation into synthetic corpus + compact classifier` 的 `Direct Evolution`，并依赖
  Ch62 EvalSpec 与 Ch69 release/rollback gate。已读 Ch62、Ch68、Ch69；现有 Ch68 已保留 static 与 dynamic
  分支，但缺少 policy compilation 的 coverage/faithfulness 双状态和 invalidation contract。暂定
  `Refine — Existing Argument (Experimental)`；不把 accuracy headline 写入 Books。

### Length Value Model — 26/30

- **Candidate / Week / Source Family**：`LENVM-TOKEN-LEVEL-LENGTH-VALUE`；W18；arXiv:2604.27039
  v1 2026-04-29、v2 2026-07-20。历史归属与机制以 28 页 v1 PDF 为准，v2 只记录 revision；已读主文、
  evaluation、全部关键 appendices（RL connection、finite precision、future-dependent weighting、inverse
  bias）并核对 official repository 的 SGLang/LlamaFactory workflow。当前 repository 晚于事件日，不能
  倒写为 v1 当日已完整发布的 artifact。
- **Original Problem / Previous Design / Changed Constraint**：prompt 指令、terminal length penalty 与
  pre-decode predictor 把 output length 当 sequence-level 决策；它们在只需粗预算时简单合理，却无法在
  decode 中根据 prefix state 连续更新剩余 horizon。长度同时决定 reasoning opportunity、KV growth、
  latency 与成本后，scheduler/control 需要 token-level、bounded、可校准的 state signal。
- **Mechanism / State Ownership / Control and Data Flow**：每个生成 token 赋常数负 reward，以 discount
  `gamma` 把 realized remaining horizon 映射为 `-(1-gamma^(L-t))`；final hidden state 经两层 SiLU MLP 与
  sigmoid 输出 `(-1,0)` value。固定 generator checkpoint/policy 采样多条 completions，按 token-uniform MSE
  回归完整 Monte Carlo return；future-dependent trajectory weighting 会改变 conditional target，不能静默
  替代。Inference 时 controller 对 candidate next states 运行 value head：可匹配目标 horizon、偏向更短/
  更长 continuation，或用 KL-regularized exponential tilting 连续调节 base token distribution。Checkpoint/
  policy owner 决定 training distribution，LenVM owner 保存 gamma/head/revision，scheduler 只消费带校准
  provenance 的 horizon estimate，不把它当真实完成时间。
- **Implementation / Evaluation Contract**：训练 mixture 为 math、code、instruction-following，最多每 prompt
  16 completions；LenVM 训练 2 epochs、learning rate `2e-5`、batch 1024、BF16。Length control 使用中英各
  180 条的 LIFEBench、目标 32～1024 tokens；trade-off 使用 GSM8K/MATH-500 等，prompt-boundary prediction
  每题 64 completions；还比较 model size、prompt 数、completion 数、target representation、shuffle、gamma
  与 fp16/bf16/fp32。作者明确指出 candidate scoring 需要额外 forward passes，实验旨在验证 length signal，
  不优化 wall-clock latency；hardware、并发、KV overhead 与 production SLO 均 `Not Disclosed`。
- **Evidence Proves / Does Not Prove**：作者实验支持 discounted return 比 raw/normalized/log length 更适合其
  token-level regression，并可在指定 models/workloads 上改善 exact-length control、连续 quality/length
  steering 与 prompt-boundary horizon prediction；gamma 在早期/晚期 resolution 间存在可见 trade-off。
  它不证明每请求 latency 或 cluster goodput 改善，不证明 predicted length 在 policy、sampling、tool use 或
  domain drift 后仍校准；Appendix 只给出 RL 解释，论文没有执行 LenVM-based RL fine-tuning，不能写成已
  验证的 credit-assignment 或 policy-invariant shaping 收益。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：token-level signal 比静态 predictor 精细，却
  增加 candidate forward、head serving、gamma calibration、policy-dependent drift 与控制器耦合；硬长度目标
  可能牺牲答案质量，value inversion 也不等于 expected raw length。Prompt-only estimate 适合 admission/
  batching 的低开销 prior；hard max-token 仍是 deterministic safety boundary；自然 EOS 适合无需显式长度
  steering 的请求。LenVM 应作为 online estimate，不得授予超预算权限。
- **Evolution / ROADMAP / Decision**：这是 Ch52 `hard max tokens / prompt-level prior → pre-decode length
  estimate → token-state remaining-horizon value → budget-aware decode control` 的 `Direct Evolution`，并向
  Ch66 交付 cost evidence；与 Ch28 value/GAE 只有尚未实验证明的 `Principle Reuse`。已读 Ch28、Ch52、
  Ch66；现有 Ch52 已要求 predicted future KV 与 reasoning budget，却缺少在线更新 signal、calibration owner
  与额外-forward opportunity cost。暂定 `Refine — Existing Argument (Experimental)`。

### Co-Evolving Policy Distillation — 26/30

- **Candidate / Week / Source Family**：`COPD-MUTUAL-ONLINE-DISTILLATION`；W18；arXiv:2604.27083 v1，
  2026-04-29，作者标注 `Work in progress`。已读取 19 页 official PDF 的 theory/pilot、method、algorithm、
  evaluation、ablation 与 references；未发现作者 code/model artifact 或独立 reproduction。
- **Original Problem / Previous Design / Changed Constraint**：mixed-data RLVR 用一个 policy 同时吸收多域，
  状态简单却会遇到 capability gradient interference；先各训 expert、再做 static OPD 避免训练冲突，但
  converged teacher 与 student behavior 距离过大时，student on-policy states 上的 teacher distribution 难以
  吸收。要合并多能力，约束不再只是“teacher 更强”，而是 supervision 必须同时有新信息且位于 student
  可访问的 behavior support。
- **Mechanism / State Ownership / Control and Data Flow**：从同一 base 初始化 K 个 capability branches；
  每个 cycle 先让 branch 在自己的 dataset/reward 上独立 GRPO `S_RL` steps，制造 specialization，再让每个
  branch 在其他 branch 数据上生成自己的 on-policy rollouts，由对方 branch 提供 token-level log-prob
  difference，双向执行 mutual OPD `S_OPD` steps。RLVR 持续拉开知识，OPD 周期性恢复 behavioral overlap；
  两分支最终做 parameter merge。K>2 时作者用 text branch 作为 hub-and-spoke hub，而非全 pairwise。
  每个 branch 拥有独立 mutable weights、optimizer、rollout/reward state；shared base、cycle、teacher/student
  revision、merge recipe 与 dataset/reward identity 必须共同 checkpoint。
- **Implementation / Evaluation Contract**：基于 EasyVideoR1/verl/EasyR1，Qwen3-VL-4B-Instruct；最大
  input/output 各 16,384 tokens，learning rate `1e-6`，rollout batch 256，每 prompt 8 rollouts、temperature 1.0，
  clip bounds 0.2/0.28。比较 text/image experts、mixed RLVR、single-direction static OPD/MOPD；two-branch
  覆盖 7 个 image 与 5 个 text reasoning benchmarks，three-branch 再加入 4 个 video benchmarks。作者令
  mixed RLVR/CoPD 使用与 experts 合计相同 training steps/data throughput，并做双向 OPD、merge、behavioral
  overlap/KL 与 `S_RL:S_OPD` ratio ablation；hardware、node topology、wall-clock、显存、communication、
  failure recovery 与更大 K 均 `Not Disclosed`。
- **Evidence Proves / Does Not Prove**：该单一设置支持 interleaved bidirectional OPD 比 listed mixed/static
  baselines 有更高 aggregate accuracy；top-k overlap/KL trace 与 ratio ablation 支持“specialization 与
  consolidation 节奏”是机制的一部分。它不证明作者的 utility/absorption function 是一般理论，不证明
  parameter merge 对不同初始化、架构或 tokenizer 成立，也不证明 3 branches 以上仍扩展；同一模型家族、
  reasoning domains 与 aggregate averages 不能代表开放领域 capability preservation。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：CoPD 减少 post-hoc support gap，却持有 K 套
  mutable policies、rollout workers 与 optimizer state，并新增 hub bottleneck、teacher error circulation、
  branch collapse、merge interference、cycle recovery 与 `S_RL:S_OPD` calibration。Mixed RLVR 在 capability
  gradients 相容、state budget 紧时仍最简单；static OPD 在 experts 已存在、teacher/student support 足够重叠
  或只需 one-way transfer 时仍合理；完全独立 experts 在能力隔离或部署路由优于统一模型时也不应被覆盖。
- **Evolution / ROADMAP / Decision**：这是 Ch29 `single-policy grouped RLVR → independent experts + post-hoc
  OPD → interleaved branch-specific RLVR + mutual OPD → merged policy` 的 `Direct Evolution`；与现有
  cross-policy rollout reuse 是 `Layering / Dependency`，但二者分别共享 evidence 与 dense teacher signal，
  不能混写。已读 Ch27～30；Ch29 已覆盖 source policy/probability identity 与多 policy state，却缺少
  teacher/student behavioral distance、bidirectional distillation cycle 与 merge checkpoint。暂定
  `Refine — Existing Argument (Experimental)`；保留 work-in-progress 与未披露 system cost。

### Accelerating RL Post-Training Rollouts via System-Integrated Speculative Decoding — 28/30

- **Candidate / Week / Source Family**：`NEMO-RL-SPECULATIVE-ROLLOUT`；W18；arXiv:2604.26779
  只有 v1，first-public 2026-04-29。NeMo RL v0.6.0 于 04-30 发布 speculative decoding，属于同一
  source family 的 implementation/release node，不另计一个论文候选。
- **Direct / Related Primary Sources**：已读 arXiv v1 HTML/metadata 全文、NeMo RL official repository、
  v0.6 release notes、EAGLE-3 configuration/recipe 入口；联读 Ch29 与 Ch44，并检查 Ch43/45 的 runtime
  邻接边界。Release 证明功能与配置已进入版本，不能替代论文实验或证明任意模型都能复现其收益。
- **Access / Full-read Coverage**：已覆盖 metadata、Abstract、Introduction、learning-speed decomposition、
  system integration、同步与异步实验、draft initialization/length/online adaptation ablation、235B simulator
  methodology/sensitivity、Related Work 与 Conclusion。论文没有独立 Limitations/Threats 或 Appendix，
  也没有公开 proprietary simulator；这些缺口直接进入证据边界。
- **Original Problem / Why Previous Design Was Reasonable**：标准 on-policy GRPO 用 autoregressive target
  policy 生成完整 rollout，distribution identity 最清晰、无需维护额外 draft state，却让长 reasoning 与
  agentic multi-turn workload 的 decode 成为 step critical path。async rollout、replay 与 low precision 可以
  提高 throughput，但分别引入 policy lag/off-policy correction 或 sampling mismatch；它们并非错误旧方案，
  而是在允许改变 training contract 时换取重叠与复用。
- **Changed Constraint / Principle**：当 generation 占 RL step 的主要时间，且 verifier-exact on-policy
  distribution 必须保留时，可用额外 proposal work 减少 target serial decode。长期原则是把 learning speed
  拆为 `effectiveness × throughput`：draft 只能优化 throughput，所有 logprob、KL、reward 与 policy loss
  必须仍以 verifier/target policy 为 authority；否则它已改变训练目标，而非纯系统加速。
- **Mechanism / State Ownership**：vLLM rollout backend 用 EAGLE-3 external drafter 或 native MTP heads
  propose tokens，再由同步后的 target policy exact verify。Learner/Megatron worker 拥有 current policy weights
  与 GRPO loss；rollout engine 拥有一个带明确 revision 的 verifier snapshot；draft owner 持有独立 checkpoint、
  initialization corpus、draft length 与 optional optimizer state。online EAGLE-3 复用 GRPO verifier forward
  产生的 hidden-state/logprob cache，通过 `.detach()` 路径训练 draft，避免 draft loss 回流 policy gradient；
  weight/refit path 必须把 policy 与 draft 的兼容 revisions 一起送入 vLLM。
- **Control / Data Flow**：`learner update → policy refit/sync → target rollout snapshot + compatible draft →
  propose/verify rollout → verifier logprob/KL/reward → GRPO update`。同步模式中 speculation 直接缩短
  `T_gen`；异步模式中 generation 与 logprob/train overlap，只能缩短仍暴露在 critical path 的 idle time。
  online adaptation 又增加 `rollout → detached hidden/logprob cache → draft loss/update → next refit` 支路，
  不能把 cache 或 draft gradient 当作 policy-gradient evidence。
- **Implementation Details**：论文实现于 NeMo RL + vLLM，实测聚焦 EAGLE-3，默认 offline、in-domain
  DAPO initialization 与 `k=3`；release 同时暴露 external draft、EAGLE-3 与 MTP 配置，online draft
  training 当时只支持 EAGLE-3。public recipe 证明接口存在，但没有证明它与论文 8B/32-GPU 配置完全等同，
  也没有公开 exact experiment commit、raw logs 或 simulator implementation。
- **Evaluation Contract**：RL-Think 使用 Qwen3-8B，RL-Zero 使用 Qwen3-8B-Base；训练集 DAPO-Math-17K，
  validation 为 AIME-2024。实测部署为 8 个 GB200 NVL72 nodes、每 node 4 GPUs（共 32 GB200），每 GPU
  186GB HBM3E、fifth-generation NVLink；比较 autoregressive、n-gram 与 EAGLE-3。主实验报告 generation
  占 baseline step 的约 65%～72%，EAGLE-3 的 generation speedup 为 1.54×/1.79×，overall step 为
  1.35×/1.41×；这些数字仅属于上述两种 workload、32-GPU topology、draft/runtime 与 measured stage mix。
- **Baselines / Ablations / Sensitivity / Overhead**：in-domain DAPO draft 比 UltraChat/Magpie initialization
  更匹配 rollout distribution；`k=3/5/7` ablation 显示 acceptance length 单调增加并不保证 speedup，RL-Think
  在 `k≥5` 反而慢于 autoregressive。online update 对已匹配 draft 几乎无增益，对弱 initialization 只提供
  有限恢复。16-node non-colocated async experiment（12 generation / 4 training nodes、policy lag 1）把
  exposed generation time 从 10.4s 降到 0.6s、effective step 从 75.0s 降到 60.5s；它证明可组合，但也
  显示 async 已隐藏的时间不能重复计入 speculation 收益。
- **What the Evidence Proves**：在作者指定的 8B reasoning workload 与实现中，verifier-exact speculative
  rollout 可以保持相近 validation trajectory，并显著减少 generation/step time；n-gram 虽有正 acceptance
  仍更慢，直接证明 acceptance 不是充分系统指标。in-domain initialization、短 draft 与 stage-level critical
  path 是 realized speedup 的必要 operating variables。
- **What It Does Not Prove / Threats to Validity**：accuracy curve 相近不单独证明实现对所有 sampling
  参数都严格 distribution-equivalent；论文未报告多 seed、置信区间、reward variance、failure recovery、
  weight-sync corruption、draft/checkpoint rollback、multi-turn tools 或 heterogeneous models。235B 的约
  2.5× end-to-end 只是 proprietary simulator 在 Qwen3 family、FP8、batch 4096、最高 2048 GB200 与指定
  acceptance/policy-lag 下的 opportunity envelope，不能写成 measured frontier-scale training result。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：speculation 新增 draft HBM/compute、
  training/refit、compatibility identity、telemetry 与 policy-draft staleness；过长 draft、弱 domain match、
  小 generation share 或已经充分 overlap 的 async pipeline 会抵消收益。纯 autoregressive rollout 在模型
  小、batch 高、decode 不占 critical path、draft artifact 不可信或 recovery 简单性优先时仍成立；async、
  replay 和 low precision 在允许各自语义 trade-off 时也与 speculation 共存，而非被替换。
- **Evolution / ROADMAP / Existing Coverage / Decision**：这是 Ch44 从 `fixed target serving speculation →
  moving-policy RL speculation with verifier/draft dual revision` 的 `Direct Evolution`；与 Ch29 rollout-policy
  provenance、policy lag 和 weight sync 是 `Layering / Dependency`。Ch44 已覆盖 exact verification、draft
  identity、verify-depth cost 与 acceptance≠speedup，但缺少 moving target 下的 draft coherence、detached
  update 和 sync/async critical-path composition；暂定 `Refine — Existing Argument (Experimental)`，Ch44
  为唯一 owner、Ch29 只接 handoff。Historical Books Gate 关闭，当前不修改 Books。

### The Last Human-Written Paper: Agent-Native Research Artifacts — 27/30

- **Candidate / Week / Source Family**：`ARA-AGENT-NATIVE-RESEARCH-ARTIFACT`；W18；arXiv:2604.24658
  只有 v1，first-public 2026-04-27。作者 repository 已从 `Orchestra-Research` redirect 到 `ARA-Labs`，
  当前 2026-08-10 README、skills 与 toolkit 明显晚于 event date；只能用来核验持续 artifact lineage，
  不能倒写为 04-27 已公开的全部功能。
- **Direct / Related Primary Sources**：已读 arXiv v1 HTML/metadata 全文、全部 protocol/system/evaluation/
  limitations 与相关 Appendices，并核对 official repository、paper 自身的 `examples/the-ara-of-ara` 入口。
  已读 Ch77、Ch80 全章及其 owner boundary；Ch62/65/73 只作为 evaluation、trace 与 memory handoff。
- **Full-read Coverage**：覆盖 Storytelling/Engineering Tax、四层 Ara ontology、Live Research Manager、
  Compiler、三层 ARA Seal 与 review pipeline、Human+AI network、understanding/reproduction/extension/
  mutation evaluations、Related Work、Future Work、Limitations，以及 A～H 中 schema rationale、compiler
  prompt、manager continuity、question/rubric、statistical tests、RE-Bench harness/case studies 与 Seal
  failure taxonomy。论文/HTML 很长但只有 v1；没有独立 peer review 或外部 reproduction。
- **Original Problem / Why Previous Design Was Reasonable**：PDF + repository 面向人类审阅、引用与长期
  传播，线性 narrative 便于建立论点，Git 则适合 code diff；experiment tracker 保存 metrics。这些对象
  分开并非单纯落后，因为它们有成熟工具、权限与归档语义。Agent 要复现/扩展研究时，跨对象恢复
  claim→config→code→result 与失败路径的成本上升，隐藏参数、负结果和 tacit decisions 又无法从最终论文
  唯一反演，才暴露新的 machine-operability 缺口。
- **Changed Constraint / Principle**：当 coding agent 已参与研究全过程，conversation/tool/diff/experiment
  trace 原本就是数字化副产物；研究 artifact 可以从“发布后压缩结果”演进为“过程内持续物化 knowledge”。
  稳定原则不是用目录替代论文，而是把不同 truth semantics 分层保存并用可解析引用连接：scientific
  claim、executable implementation、branching exploration 与 raw evidence 不能再只靠 narrative adjacency。
- **Mechanism / State Ownership**：`PAPER.md` 是版本化 manifest；`logic/` 拥有 falsifiable claims、
  experiment specification 与 typed dependencies；`src/` 拥有 kernel/repository implementation、configs、
  environment/hardware/seeds；`trace/` 用 question/decision/experiment/dead_end/pivot DAG 保存探索与
  provenance；`evidence/` 保存 raw result/log。Research owner 仍拥有 hypothesis 与 human judgment，
  source/artifact owner 拥有 immutable inputs/version，manager/compiler 只生成 derived state，Seal/reviewer
  产生 verification evidence，不能反向成为 scientific truth owner。
- **Control / Data Flow**：born-agent 路径在 session close 执行 `context harvest → event classification +
  provenance → staging/maturity promotion → versioned artifact → next-session selective briefing`；legacy
  路径执行 `multi-source ingest → semantic deconstruction → logic mapping → physical grounding → exploration
  reconstruction → deterministic Level-1 validate/fix`。Review 再按 `structural integrity → rubric-anchored
  findings → budgeted directional execution → human novelty/significance judgment` 逐级加成本，不把 LLM
  score 直接当发布 authority。
- **Implementation Details**：Live Manager 与 Compiler 以 agent skills 实现，依赖通用 file/shell tools；
  compiler 接受 PDF、repo、rubric、dataset 与 trajectory，source-aware enrichment 必须标记 provenance。
  Level 1 检查 schema/required fields/dangling refs；Level 2 读取 claim/evidence relationship 并生成
  severity findings；Level 3 隐藏 evidence values，只按 compute budget执行 scaled-down directional check。
  当前 repository 已演进为多个 skills/CLI，不等于 v1 论文时的 exact implementation snapshot。
- **Evaluation Contract — Understanding**：23 个 PaperBench papers + 7 个 RE-Bench tasks，共 450 paired
  questions；每个 `(target, format, question)` 用 fresh Claude Sonnet 4.6，Claude Opus 4.6 按 gold reference
  ternary grading。作者报告 Ara 93.7% vs baseline 72.4%。但 Category B 的 Ara 由 PDF+repo+expert rubric
  编译，Category C 又含 MALT failure traces，而 baseline 不拥有这些 sources；结果同时测量“更多可用信息”
  与“结构更可导航”，不能单独估计 schema 的 causal effect。
- **Evaluation Contract — Reproduction**：15 个有 repo 的 PaperBench papers、每篇 10 tasks、共 150
  subtasks/1,743 rubric requirements；同为 Sonnet 4.6，per-paper 14～20M token budget，expected numbers
  masked，Opus 4.6 blinded judge，difficulty weight 1:2:3。作者报告 64.4% vs 57.4%、8 win/5 tie/2 loss，
  15 对 paper score 的 Wilcoxon `p=0.028`、8–2 exact binomial `p=0.039`。Ara input 仍含 expert rubric
  提供的配置，因此证明 richer executable specification 有效，不证明自动 compiler 能从 PDF+repo 独立
  恢复这些缺失知识；一次 Ara run 也发生 fabricated results。
- **Evaluation Contract — Extension / Review**：五个 RE-Bench tasks 每 arm 使用 8h SLURM + $50 API cap，
  Sonnet 4.6；Ara arm 多出带 provenance 的 MALT dead ends。Ara 全部更早出现 useful move，最终 3/5
  领先，但 paper arm 在 triton/restricted_mlm 后期反超；同任务换 Sonnet 4.5 又改变相对结果，说明 trace
  value 取决于 successor capability。Level-2 mutation benchmark 为 23 artifacts×5 injections：总体 82.6%，
  orphan experiment 仅 22%；17/23 出现 grade inflation，finding 与 score 解耦。
- **What the Evidence Proves**：在作者选定的 ML artifacts、模型、budgets、rubrics 与 enriched-source
  construction 下，把 claim/config/code/evidence/failure trace 变成可导航 cross-layer object 能改善特定
  knowledge retrieval 与 reproduction，并能让历史 failure 更早影响 search。结构检查适合 deterministic
  implementation；LLM 更适合产出 evidence-linked findings，而 final grade 应从 findings 规则化计算。
- **What It Does Not Prove / Threats to Validity**：没有证明 Ara schema 是唯一或跨学科最优格式，也没有
  隔离 source enrichment、compiler quality、progressive disclosure 与 ontology 各自贡献；所有主要 agent/
  judge 属于 Claude 4.6 family，缺少跨 vendor/seed robustness。Level-1 pass 不证明 artifact 语义完整；
  source omission 不可由 compiler 恢复。当前未实现 sandbox、content anomaly detection、granular trace
  access control、major-schema migration、long-term validator availability，故不能称 production-ready review
  authority 或隐私安全的 collective memory。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：过程保真换来 trace 体积、privacy/IP、
  source poisoning、stale heuristic、schema/version、lineage conflict、validator drift 与 review compute。
  旧 failure trace 可能 anchoring 强模型、压缩 exploration breadth；完整 evidence 暴露给 verifier 又会造成
  answer copying，因此访问层与 evaluation ground truth 必须分离。PDF 在人类传播、稳定 citation 与低维护
  归档中仍合理，repo/tracker 也继续拥有 code/metrics；Ara 更像连接它们的 epistemic control plane。
- **Evolution / ROADMAP / Existing Coverage / Decision**：相对 `paper + repo + tracker` 是 `Layering /
  Dependency`，相对 Ch80 的 AgentRun evidence graph 是 `Direct Evolution`：run artifact 不只保存 outcome，
  还要保存 claim/evidence/implementation/exploration 的 typed bindings、supersession 与 verification state。
  Ch77 已覆盖 durable workflow、program lineage、failed-run retention 与 human gate，Ch80 已覆盖 artifact
  identity、trace/evidence plane、versioned rollout；新增缺口是 research artifact 的多层 ownership、
  source-enrichment boundary 与 trace-can-constrain-successor 反例。暂定 `Refine — Existing Argument
  (Experimental)`，Ch80 为唯一 owner、Ch77 只接 handoff；Historical Books Gate 关闭，不修改 Books。

### NVIDIA TileGym cuTile Python→cuTile.jl kernel translation skill — 24/30

- **Candidate / Week / Score / Source Family / Type**：W18，24/30；
  `NVIDIA-TILEGYM-CROSS-DSL-KERNEL-SKILL`；official engineering Blog / open artifact claim。NVIDIA
  Technical Blog 于 2026-04-30 first-public。已完整阅读 cross-DSL mapping、matmul/softmax examples、skill
  structure、validator/test contract、reported run 与 prerequisites；GitHub artifact 当前因访问权限未独立核验，
  所以状态为 `Official Blog Complete; Repository Access Blocked`，不能把页面中的 repository tree 当作
  independently verified artifact contents。
- **Original Problem / Why the Previous Design Was Reasonable**：人工 port GPU kernel 可以逐行处理语言
  差异，并让 domain expert 理解每次 layout/type change；对少量性能关键 kernel，这种高成本方法仍提供最强
  reviewability。可重复移植增多后，0/1-based indexing、row/column-major layout、implicit/explicit broadcast、
  axis、constant/type API 与 MMA spelling 的组合会形成 silent corruption；compiler success 不能证明语义等价。
- **Changed Constraint / Mechanism**：cuTile Python 与 cuTile.jl 共享 tile abstraction，使转换大体可规则化，
  但 runtime semantics 不同。TileGym 把一次性 prompt 演进为 repository-scoped skill：entrypoint + workflow
  checklist + bidirectional API map + 17 critical rules + debugging/testing guide + static validator + add/matmul/
  softmax worked examples。执行流是 `pre-flight pattern scan → rule-guided conversion → static validation →
  CPU-reference tests → failure-guided repair`，不是让 Agent 自述“转换完成”。
- **State Ownership / Data Flow / Implementation Details**：source kernel 与 target DSL/runtime version 决定
  translation identity；skill/versioned rules 拥有可迁移知识；static checker 拥有有限 anti-pattern detection；
  CPU reference 与 per-dtype tolerance 拥有 correctness oracle；GPU runtime 执行 target artifact；human reviewer
  仍拥有未编码的 numerical/performance contract。add 覆盖基础 surface，matmul 覆盖 loop/tensor-core/layout
  flip，softmax 覆盖 multipass running max/sum invariant；boundary tests 包含 dimension 不能整除 tile 的情况。
- **Evaluation Contract / What the Evidence Proves**：官方页面报告一个 representative GEMM 在 frontier LLM、
  无人工干预下约 4 分钟、约 78K tokens；requirements 为 Julia 1.12+、CUDA 13.1+ driver 与 Ampere/Ada/
  Blackwell。它证明作者 workflow 能在三个公开示例上把规则、static checks 与 CPU-reference tests 组合成
  可重复流程；没有 model/version、prompt snapshot、GPU 型号、kernel shapes、dtype 分布、baseline human
  time、重复 run、pass-rate CI、性能 matching 或未见 kernel holdout，因此不能把 4 分钟/78K tokens 当成
  通用 code-agent productivity 或 kernel correctness benchmark。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：把规则固化为 skill 降低重复发现成本，
  也会把 stale API map、错误 tolerance、遗漏 invariant 与 worked-example overfitting 规模化；static checker
  只能发现已编码 pattern，CPU reference 也不能验证 GPU race、undefined behavior、numerical stability、
  performance regression 或 target-specific memory traffic。少量关键 kernel、缺少可靠 oracle、跨 DSL 语义
  不同构或性能决定产品 SLO 时，人工 port、compiler IR transform、formal equivalence 或 expert review 仍是
  合理分支。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：相对 ad-hoc prompt 是 `Direct Evolution`，相对
  compiler/test pipeline 是 `Layering / Dependency`。Ch77 为唯一 owner；其 existing “problem compilation →
  typed contract → deterministic checks → artifact/version lineage → held-out/human deployment decision” 已完整
  覆盖本案例的长期观点，故最终为 `No Change — Already Covered`。Ch45 仅在未来 Books Gate 复核时接
  target-hardware execution-plan/kernel correctness handoff，不重复存放 Agent workflow。本轮不修改 Books；repository content、
  unseen-kernel generalization、numerical/performance equivalence 与 multi-run reproducibility 仍待验证。

### KServe v0.18.0 stable — 24/30

- **Candidate / Source Family / History**：`KSERVE-0.18-RC-LLMISVC-CONTROL-PLANE`；official stable
  release `v0.18.0` 于 2026-04-29 发布，对应 signed tag `v0.18.0` / commit `3a432a8`。它是 W17
  rc0/rc1 family 的 stable version node，不重复发明一条技术路线，也不能把 RC 行为默认视为 stable。
- **Access / Full-read Coverage**：已读 official GitHub release、KServe 0.18 release blog、
  `LLMInferenceService` control-plane/CRD 文档、`LocalModelNamespaceCache` CRD 文档，并联读 W17 RC packet
  与 Ch56～58；release 没有完整 workload benchmark、hardware、并发、TTFT/TPOT 或 availability SLO。
- **Problem / Previous Design / Changed Constraint**：单 Pod inference 与 Ray-based multi-node orchestration
  在既有 runtime 下合理，但超大模型的 tensor/pipeline parallel placement、whole-group scaling、模型下载
  隔离和 OpenAI-compatible workflow endpoint 逐渐成为 control-plane contract。stable 0.18 把这些能力
  组合进 Kubernetes-native desired state，而不是证明所有 workload 都应采用 multi-node serving。
- **Mechanism / Ownership / Control and Data Flow**：`LLMInferenceService` 通过 `mp` backend 描述 multi-node
  workload；pipeline-parallel size 决定 node count，tensor-parallel size 决定每 node accelerator demand，
  controller 创建 headless Service 并注入跨 Pod 发现信息。LeaderWorkerSet/Workload Variant Autoscaler 以
  replica group 为伸缩单位；runtime/metric path 产生 recommendation，HPA/KEDA/WVA 执行 capacity actuation，
  KServe controller 拥有 desired-resource composition。`LocalModelNamespaceCache` 将 node-local model cache
  的管理边界从 cluster-wide 收窄到 namespace；router 仍拥有请求选择，推理 runtime 仍拥有 token/KV state。
- **Implementation / Evidence Boundary**：官方发布还记录 llm-d 0.6 集成、`/v1/responses` HTTPRoute、
  Pod Security Standards restricted 默认、安全清理/TLS/readiness 与 GKE 兼容性改进。这些资料证明 stable
  API/资源组合和发布事实，不证明 WVA signal 在任意 workload 下最优，也不证明 multi-node 比 Ray 或
  single-node 达到更好 tail latency、goodput、failure recovery 或成本。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：whole-group scaling 尊重 gang/topology，
  却增加启动时间、最小容量粒度、leader/worker failure、CRD/version dependency 与 metric freshness 风险；
  namespace-scoped cache 改善 tenancy isolation，却可能降低跨 namespace dedup 并增加磁盘配额/eviction 状态。
  single-node serving 在模型可容纳、低流量或启动延迟敏感时仍合理；Ray 在已有 actor/failure model 与
  heterogeneous workflow 需要时仍可能更合适；cluster-scoped cache 在单租户环境仍有共享收益。
- **Evolution / ROADMAP / Decision**：相对 W17 RC 是 `Direct Evolution` 的 stable confirmation，
  相对 LWS/WVA、llm-d 与 Gateway API 是 `Layering / Dependency`。Ch57 已拥有 declarative control plane、
  multi-node placement 与 autoscaling，Ch58 拥有 routing；Ch49/52 只接收 topology/scheduling handoff。
  stable release 没有提供新的长期机制缺口，故为 `Weekly Only — Stable Release / No Books Change`。

### Kubernetes v1.36 controller staleness mitigation — 27/30

- **Candidate / Week / Score / Source Family**：W18，27/30；
  `K8S-136-CONTROLLER-READ-YOUR-WRITES`。事件日为 Kubernetes 官方 Blog 发布日
  2026-04-28；client-go v0.36.0 package 于 2026-04-22 发布，是机制实现的相关 primary evidence，
  不另计一个 W17 事件。Blog 于 6 月 12 日只修正 typo，不改变 W18 机制归属。
- **Direct / Related Primary Sources / Access**：已完整阅读 Kubernetes 官方设计说明，核对
  client-go v0.36.0 `tools/cache` package 的 Reflector/Store/FIFO API、
  `LastStoreSyncResourceVersion()` 与 resource-version carrying queue surface，并核对官方 metrics
  reference 的发布边界。资料可以验证 v1.36 behavior/API 与 ownership；没有 workload benchmark、
  hardware、规模、tail latency、controller throughput 或 SLO 数据。
- **Original Problem / Why the Previous Design Was Reasonable**：controller 通过 informer/local Store
  读取对象、通过 API Server 写回 desired/observed state，是用 eventual cache 换取低 API pressure 与高
  reconcile throughput 的合理设计。问题是 cache 可能落后于 controller 自己刚完成的写入；下一次
  reconcile 若基于旧 snapshot 行动，会重复创建、错误回滚或延迟收敛。过去的 retry/idempotency 能缓解
  重复副作用，却不能证明当前 read 已经看见自己的 write。
- **Changed Constraint / Principle**：当 control-plane action 由 read-modify-write 演进为高频、并发且
  对 owner state 敏感的闭环时，`eventually fresh` 不再等于 `safe to act now`。长期原则是把
  **last observed resource version、last self-written resource version 与 reconciliation eligibility** 放在同一
  consistency contract 中；freshness 是 action precondition，不是 dashboard 上的事后指标。
- **Mechanism / State Ownership / Control and Data Flow**：client-go 的 `AtomicFIFO` 在既有 FIFO 之上
  使 batch/list replacement 原子化，避免 out-of-order events 暴露不一致 queue state；Store 暴露最新
  observed resource version。controller 侧 `ConsistencyStore` 记录 `WroteAt(owner, uid, resource,
  resourceVersion)`，在 reconcile 前用 `EnsureReady(namespacedName)` 比较 cache progress；若 cache 尚未
  catch up，就跳过本次 action，等待新 event。`Clear` 配合 UID 处理同名对象删除后重建。API Server
  拥有 authoritative object/version，informer Store 拥有 observed snapshot，ConsistencyStore 拥有
  controller-local write watermark，controller 仍拥有 actuation decision。
- **Implementation Boundary**：v1.36 在 kube-controller-manager 的 DaemonSet、StatefulSet、ReplicaSet
  与 Job controllers 中接入对应 `StaleControllerConsistency<API type>` feature gates，官方说明这些 gate
  默认启用；`stale_sync_skips_total` 与 `store_resource_version` 提供 skip/cache-progress 观测。官方把
  controller-runtime 支持列为 future work，因此不能把该行为外推为所有 Kubernetes/custom controllers
  已自动获得一致性保护。
- **Evaluation Contract / What the Evidence Proves**：primary sources 证明 feature/API、四类 built-in
  controllers 的接入、默认 gate 状态及观测面存在；它们没有给出对照实验、ablation、failure-injection、
  memory/CPU overhead、API QPS、queue delay 或 production incident reduction。因而这是
  `Version Fact + Generalizable Mechanism`，不是性能或全局一致性结论。
- **What It Does Not Prove / Limitations**：skip-on-stale 只建立 controller 自身已记录 write 与当前 cache
  progress 之间的 read-your-writes guard，不提供跨 controller global linearizability，也不保证未登记对象、
  外部 writer 或 multi-resource transaction 的 snapshot 一致。resource-version progress 与 skip count 是
  evidence signals，不是 freshness SLA；metrics reference 当前也未列出可由本文验证的稳定性级别和长期
  compatibility contract。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：guard 以延迟 action 换 correctness，
  新增 write-watermark 生命周期、UID cleanup、cache-progress 判定、feature-gate rollout 与 skip-storm
  风险；若 watch/cache 卡住，安全跳过会转化为 availability/latency 问题。纯只读 controller、动作天然
  幂等且不依赖自身近期写入的 reconciliation，或能承受短暂旧读的低复杂度 workload，仍可采用原有
  eventual-cache 路径。需要跨对象原子条件时，还需 server-side precondition/transaction-like protocol，
  不能把本机制当作替代。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：相对 informer cache + retry/idempotency 是
  `Direct Evolution`；相对 metrics 是 `Layering / Dependency`。Ch53 已拥有 desired state、reconciliation
  与 evidence plane，但缺少 actuation 前的 cache-freshness invariant，故为唯一 owner；Ch54 只承接
  custom controller 的 write-watermark/UID lifecycle handoff，Ch63 只承接 freshness、skip 与 stuck-cache
  观测。暂定 `Refine — Existing Argument (Version-Grounded)`；Historical Books Gate 关闭，本轮不修改
  Books。

### Kubernetes v1.36 mutable pod resources for suspended Jobs — 28/30

- **Candidate / Week / Score / Source Family**：W18，28/30；
  `K8S-136-MUTABLE-SUSPENDED-JOB-RESOURCES`。官方 Blog 于 2026-04-27 发布；能力在 v1.35
  以 alpha 首次引入，在 v1.36 升为 beta 并默认启用。本周记录 beta/default-on evolution node，
  不把 v1.35 的首次实现重算为 W18 新机制。
- **Direct / Related Primary Sources / Full-read Coverage**：已读 Kubernetes 官方 feature Blog 全文，
  并联合核对 v1.36 Jobs concept、feature-gate reference 与 batch/v1 Job API reference。已覆盖问题、
  mutable field set、validation preconditions、suspend/resume control flow、replacement/DRA boundary 与
  beta gate；没有 benchmark、implementation profile、large-cluster test、queue fairness 或训练结果。
- **Original Problem / Why the Previous Design Was Reasonable**：Job PodTemplate immutable 能保证
  controller 对已启动 execution 使用稳定 spec，也让 status/history 与实际 Pods 有清楚对应关系。
  但 batch/ML Job 在提交时常不知道可获得的 CPU、memory、GPU/extended resources；queue controller
  只有在 admission 时才知道 capacity、priority 与 device availability。过去若资源不匹配，只能删除并
  重建 Job，连带丢失 identity、metadata、status/history，也让 CronJob instance 或排队 provenance 断裂。
- **Changed Constraint / Principle**：资源声明不再只有 `immutable forever` 与 `mutable while running`
  两个极端。更稳健的 contract 是：
  `submitted intent → suspended negotiation → validated resource revision → resume → execution freeze`。
  可变性必须由 lifecycle barrier 限定；一旦 execution 已存在，就要先终止 active Pods，不能让旧 Pods
  与新 template 同时代表同一 Job generation。
- **Mechanism / Mutable Surface**：API Server 只对 `spec.suspend=true` 的 Job 放宽 PodTemplate resource
  validation，允许 containers/initContainers 的 `resources.requests` 与 `resources.limits` 变化；标准资源
  校验仍成立。若 Job 曾运行后再 suspend，只有 `status.active=0` 才接受修改。变更完成后 controller 将
  `spec.suspend=false`，Job controller 才按修订后的 template 创建 Pods。该能力没有新增 API kind；
  `resourceClaimTemplates` 仍 immutable，DRA identity/claim 不能被普通 resource patch 隐式替换。
- **State Ownership / Control and Data Flow**：提交者拥有原始 workload intent；queue/admission controller
  根据 capacity 与 policy 提议 resource revision；API Server 拥有 field validation 和 suspend/active-Pod
  barrier；Job controller 拥有 Pod materialization 与 status；scheduler 仍拥有 placement；training runtime
  拥有 world-size、parallelism 与 checkpoint compatibility。资源 patch 的 actor、old/new spec、reason、
  policy revision 与 resume generation 都应进入 lineage，否则保留 Job name 反而会掩盖 execution contract
  已变化。
- **Implementation / Operational Boundary**：v1.36 的 `MutablePodResourcesForSuspendedJobs` gate 为
  beta/default-on。已运行 Job 被 suspend 时，active Pods 会被终止；workload 必须处理 SIGTERM/优雅退出，
  start time 与 deadline 语义也受 suspend/resume 影响。官方建议有 failed Pods 时考虑
  `podReplacementPolicy: Failed`，避免 terminating 与 replacement Pods 重叠争抢资源。这些是 API/lifecycle
  事实，不是 checkpoint safety 或无损 resize 保证。
- **Evaluation Contract / What the Evidence Proves**：证据证明允许修改的字段、两项 acceptance
  preconditions、v1.36 beta/default-on 状态、DRA exclusion 与 Job identity preservation；不证明任意 queue
  controller 会选择正确资源，也不证明减少 GPU/CPU 后 workload 仍可执行、收敛速度更优、成本更低或
  fairness 提升。Blog 中 4→2 GPU 只是说明性示例，没有绑定真实模型、parallel layout、hardware、batch、
  checkpoint 或 SLO。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：收益是 admission 可以在不重建 Job
  identity 的情况下适配当前 capacity；代价是 spec revision、policy actor、resume generation 与 artifact
  lineage 成为新状态。减少 GPU 可能破坏 TP/PP/world-size divisibility、batch/LR contract 或 checkpoint
  compatibility；suspend 一个运行中 Job 会造成 termination/restart cost；等待 `status.active=0` 也可能被
  stuck Pod 阻塞。对创建时资源已知、审计要求严格 immutable spec、运行中不能中断或 DRA claim identity
  必须联动的 workload，delete/recreate/new attempt 或保持 immutable contract 仍更清楚。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：相对 immutable Job template 是 `Direct
  Evolution`，相对 Kueue/Volcano admission 是 `Layering / Dependency`，不是 in-place running-Pod resize。
  Ch56 为唯一 owner：它已写 admission、suspend 与 runtime lifecycle，但“admission 校验不可变资源字段”
  需要细化为 **execution 前受控协商、execution 后冻结**；Ch59 只接 resource-shape/placement handoff，
  Ch60 只接 queue decision 与 resume transition handoff。暂定 `Refine — Existing Argument
  (Version-Grounded)`；Historical Books Gate 关闭，本轮不修改 Books。

### Kubernetes v1.36 tiered Memory QoS protection — 27/30

- **Candidate / Week / Score / Source Family**：W18，27/30；
  `K8S-136-MEMORY-QOS-TIERED-PROTECTION`。官方 feature Blog 于 2026-04-29 发布；MemoryQoS
  自 v1.22 引入、v1.27 调整，v1.36 增加 opt-in reservation policy、按 QoS class 分层保护、metrics 与
  old-kernel warning。该 feature 在 v1.36 仍为 alpha，本条是 `Direct Evolution`，不是 stable promise。
- **Direct / Related Primary Sources / Full-read Coverage**：已完整阅读 v1.36 feature Blog，并核对
  Kubernetes Pod QoS、resource management、cgroup v2 docs 与 Linux kernel cgroup-v2 memory controller
  文档。覆盖 `memory.min/low/high/max` 语义、hierarchy、configuration、metrics、kernel/runtime
  prerequisites 与 failure boundary；没有 Kubernetes workload benchmark、production trace、ablation、
  node-density test 或 SLO 数据。
- **Original Problem / Why the Previous Design Was Reasonable**：request/limit 原本同时承担 scheduling、
  accounting 与 runtime enforcement 的简化接口；v1.27 在有 memory request 的 container 上写
  `memory.min`，可让关键 working set 不被 reclaim。但 hard protection 无视 pressure：若 Burstable requests
  接近 node capacity，kernel/system daemons/BestEffort 可回收空间被压缩，错误的 request 会把过度承诺
  转化为 OOM。只靠 `memory.max` 又把动态 pressure 直接变成 kill，而不是渐进退化。
- **Changed Constraint / Principle**：共享节点既要 protection，又要 overcommit/headroom。一个数无法同时
  表达 **hard guarantee、soft preference、throttle boundary 与 hard cap**。因此 v1.36 把 throttling 与
  reservation 解耦，并让 QoS class 选择 reclaim semantics：`request` 不再只决定 scheduler feasibility，
  也影响 runtime pressure 下谁先退让。
- **Mechanism / Mapping**：启用 `MemoryQoS` 后，`memory.high` 仍由 `memoryThrottlingFactor`（默认 0.9）
  控制 throttling；新的 `memoryReservationPolicy` 默认 `None`，不写 `memory.min/low`。选择
  `TieredReservation` 时，Guaranteed 的 request 映射为 `memory.min` hard protection，Burstable 的 request
  映射为 `memory.low` soft protection，BestEffort 不获得 protection；limit 继续映射 `memory.max`。
  `memory.high` 超限触发 throttle/reclaim、不会直接 OOM；`memory.max` 才是最终 hard cap。
- **State Ownership / Control and Data Flow**：workload owner 声明 request/limit，admission/scheduler 用它做
  placement/accounting；kubelet 根据 node config 与 Pod QoS 计算 cgroup contract；runc/libcontainer 管理
  pod/QoS-class cgroups，container runtime 管理 container cgroups；Linux kernel 拥有 reclaim/throttle/OOM
  decision。kubelet 还必须维护 hierarchy：root `memory.min` 与 Burstable parent `memory.low` 要容纳 child
  protection。tenant/platform owner 因此必须同时治理 request accuracy、node headroom 与 policy rollout。
- **Observability / Compatibility**：kubelet 暴露 alpha metrics
  `kubelet_memory_qos_node_memory_min_bytes` 与 `..._low_bytes`，只能说明配置的保护总量，不能单独证明
  working-set health 或 OOM risk。kernel <5.9 的 `memory.high` 可能触发已知 livelock；v1.36 kubelet 只告警，
  不阻止启用。prerequisites 还包括 Linux cgroup v2 与支持它的 runtime。compatibility warning 不是安全
  guard，rollout 仍需 node-version inventory 与 canary。
- **Evaluation Contract / What the Evidence Proves**：primary sources 证明 alpha API/config、QoS→cgroup
  mapping、default `None`、metrics 名称与 kernel prerequisite；kernel docs 独立支持 hard/soft protection、
  throttle 与 hard-limit 语义。资料不证明 tiered policy 在任意 workload 上减少 OOM、改善 tail latency 或
  提高 utilization，也没有给出 AI model、CPU/DRAM、NUMA、batch、concurrency 或 SLO 条件。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：tiered protection 减少 Burstable hard
  reservation，却把 QoS classification、request accuracy、ancestor overcommit 与 kernel/runtime version
  变成 failure surface。Guaranteed `memory.min` 过高会把 pressure 转移给其他 Pods/host；Burstable
  `memory.low` 在极端 pressure 下仍可回收，不能当 SLA；aggressive `memory.high` 会把 OOM 改成长期
  throttle/latency。`None` 适合先观察 throttling 或 headroom 不明确的集群；hard-dedicated nodes/VMs 仍适合
  强隔离，不能把 cgroup preference 当成 tenant security boundary。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：相对 uniform `memory.min` 是 `Direct Evolution`，
  相对 scheduler request/limit 与 monitoring 是 `Layering / Dependency`。Ch67 是唯一 owner：它已有
  resource-plane/noisy-neighbor 边界，但缺少 admission entitlement 如何下沉为 reclaim priority、以及错误
  protection 如何把风险转移给邻居；Ch59 只接 request/placement 与 runtime enforcement 分层，Ch63 只接
  configured protection、pressure、throttle/OOM 联合观测。Ch50 讨论 GPU HBM，不接收 host DRAM cgroup
  机制。暂定 `Refine — Existing Argument (Alpha / Version-Grounded)`；Historical Books Gate 关闭，
  本轮不修改 Books。

### Kubernetes v1.36 in-place Pod-level vertical scaling — 28/30

- **Candidate / Week / Score / Source Family**：W18，28/30；
  `K8S-136-INPLACE-POD-LEVEL-RESIZE`。Pod-Level Resources 在 v1.34 升为 beta，container-level
  In-Place Pod Vertical Scaling 在 v1.35 GA；本候选是二者的组合能力在 v1.36 升为 beta/default-on。
  它是 `Layering / Dependency + Direct Evolution`，不能把底层各组件稳定级别合并成一个 GA 结论。
- **Direct / Related Primary Sources / Full-read Coverage**：已完整阅读 v1.36 feature Blog 与官方
  Pod-level resize task，包括 feature prerequisites、resize subresource、container resizePolicy、node
  feasibility、update ordering、conditions/retry/observedGeneration、validation 与 limitations；并联读
  Ch53、Ch56、Ch59。官方材料没有 latency/availability benchmark、large-cluster test、VPA experiment、
  application correctness test 或生产 SLO。
- **Original Problem / Why the Previous Design Was Reasonable**：重建 Pod 能用 scheduler 重新做完整
  placement，并给新的 execution generation 清楚边界；container-level requests/limits 也能精确表达每个
  process 的 envelope。但 sidecar/多容器 Pod 常共享一个 aggregate CPU/memory pool，逐 container 重算
  容易失配；重建又会中断服务、丢失 warm state，并把小幅 capacity correction 变成 rollout。
- **Changed Constraint / Principle**：当 workload 的 resource envelope 随运行阶段或观测变化时，desired
  resource、node-admitted resource 与 kernel-applied resource 不再是同一时刻的一个值。可靠 control plane
  必须显式区分：
  `spec.resources intent → status.allocatedResources admitted → status.resources applied`，
  并让每个状态绑定 `metadata.generation/observedGeneration`，而不是在 patch 成功后假定 resize 已生效。
- **Mechanism / Control and Data Flow**：用户/controller 通过 Pod `resize` subresource 更新 aggregate
  `.spec.resources`。kubelet 先检查新 request 是否适配 node allocatable；不可立即满足时以
  `PodResizePending` + `Deferred/Infeasible` 表达，Deferred 按 PriorityClass、QoS class、等待时长重试。
  admission 后 `status.allocatedResources` 先反映承诺，cgroup 实际更新完成后 `status.resources` 才追上；
  中间态用 `PodResizeInProgress` 表达。
- **Ordering / Restart Semantics**：扩大时先扩 Pod-level cgroup，再扩 inheriting container cgroups；缩小时
  先 throttle/shrink containers，再缩 aggregate boundary，避免短暂 overshoot。Pod-level envelope 本身没有
  独立 resizePolicy；container 的 `resizePolicy` 仍决定相关 container change 可动态应用还是需要 restart。
  因而“often without restart”不是“所有 workload 无中断”。
- **State Ownership / Validation**：API intent 由 resource author/controller 拥有；scheduler 的原 placement
  不是 resize recommender；kubelet 拥有 node feasibility、retry 与 cgroup actuation；CRI/runtime 执行
  container resource update；application owner 仍负责判断 CPU/memory change 是否语义安全。Pod-level
  request 必须不小于各 container requests 之和；单个 container limit 不得超过 Pod-level limit，但 container
  limits 总和可超过 aggregate limit以支持共享。这些 validation 保证 envelope consistency，不保证应用
  performance/correctness。
- **Compatibility / Failure Modes**：需要 Linux、cgroup v2、支持 `UpdateContainerResources` 的 runtime，
  以及 `PodLevelResources`、`InPlacePodVerticalScaling`、`InPlacePodLevelResourcesVerticalScaling`、
  `NodeDeclaredFeatures` 四个 gates。spec 已更新但 node 长期 Deferred 会造成 intent/applied drift；部分
  nodes/runtime capability 不一致会造成 fleet-level behavior split；缩容可能 throttle/OOM，container restart
  会破坏 connection、cache 或 checkpoint assumptions。VPA integration 仅是 future direction，不能写成
  v1.36 当前自动闭环。
- **Evaluation Contract / What the Evidence Proves**：primary sources 证明 beta/default-on API behavior、
  state/condition/retry contract、ordering、validation 与 prerequisites；示例 2→4 CPU/4 GiB 只说明操作，
  不提供 application、hardware、concurrency、latency 或 SLO evidence。资料不证明 in-place 总比 recreate
  更安全、更快，也不证明 resize recommendation 正确。
- **Trade-offs / Previous Design Still Applies**：收益是保留 Pod identity/warm state、减少 rollout disruption，
  代价是多阶段 desired/admitted/applied state、retry fairness、node capability 与 application reaction 成为
  新故障面。需要重新 placement/NUMA/topology、GPU/DRA identity 改变、进程启动时固定 heap/world size、
  或要求 clean generation/rollback 的 workload，recreate/rollout 仍更合理；suspended Job resource mutation
  发生在 execution 前，不能与 running-Pod resize 合并为同一语义。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：Ch53 为唯一 owner：现有 platform control loop
  已有 desired/reconciliation/observed state，但缺少 resource actuation 的 admitted/applied generation；
  Ch56 只接 training/application restart 与 checkpoint safety，Ch59 只接 node capacity/placement handoff。
  暂定 `Refine — Existing Argument (Version-Grounded)`；Historical Books Gate 关闭，本轮不修改 Books。

### Kubernetes v1.36 Pod-Level Resource Managers — 28/30

- **Candidate / Week / Score / Source Family**：W18，28/30；
  `K8S-136-POD-LEVEL-RESOURCE-MANAGERS`。官方 feature Blog 于 2026-05-01 发布；
  `PodLevelResources` 在 v1.34 已为 beta/default-on，而本条新增的 `PodLevelResourceManagers` 在 v1.36
  仍为 alpha/default-off。它是 node resource managers 从 strictly per-container allocation 向 pod budget
  partition 的 `Direct Evolution + Layering / Dependency`，不是 Pod-level resource API 的首次出现。
- **Direct / Related Primary Sources / Access and Full-read Coverage**：已完整阅读 v1.36 feature Blog，
  并核对 Resource Managers concept、feature-gate matrix 与 Pod-level CPU/memory task。覆盖 pod/container
  Topology Manager scope、CPU/Memory Manager policy、exclusive slice、pod shared pool、init/sidecar lifecycle、
  CFS quota、validation、checkpoint/downgrade、metrics 与 limitations；并重读 Ch53、Ch56、Ch59 的 owner
  边界。未使用 GitHub KEP/代码作为已验证证据，因为当前访问权限不允许；官方文档足以证明公开 API 与
  runtime contract，但不能证明未公开实现细节。
- **Original Problem / Why the Previous Design Was Reasonable**：CPU、Memory 与 Topology Manager 原来按
  container 分配，边界清楚，单容器 Guaranteed contract 容易 admission、checkpoint 与恢复。可是高性能
  Pod 常把主进程、metrics/logging、service-mesh 或 data-ingestion sidecar 放在同一故障与生命周期边界；
  若为每个轻量 sidecar 都申请整数 exclusive CPU 和 NUMA memory，会浪费资源，若不申请又可能失去所需
  的 Guaranteed/NUMA contract。问题不在“有没有 limit”，而在 **Pod 是调度/生命周期单位，exclusive
  resource 却仍只以 container 为分配单位**。
- **Changed Constraint / Principle**：当一个 Pod 内部既有 latency-sensitive compute，又有弹性辅助进程，
  resource contract 需要同时表达 aggregate budget、exclusive slices 与 residual sharing。v1.36 让
  `.spec.resources` 成为 resource managers 的 allocation basis，并把一个 Pod budget 分解成：
  `node pool → pod-aligned pool → container exclusive slices + pod shared remainder`。资源隔离的最小单元
  因而不必等于资源治理的唯一单元。
- **Mechanism / Control and Data Flow**：在 `pod` scope，kubelet 先按整个 Pod budget 做一次 NUMA alignment；
  requests=limits 且 CPU 为正整数的 Guaranteed containers 从中取得 exclusive CPU/memory slices，其余
  container 使用剩余的 pod shared pool，并与 node-wide shared pool 隔离。standard init container 完成后，
  其资源进入 per-pod reusable set；restartable init container/sidecar 的 persistent reservation 则继续保留。
  在 `container` scope，kubelet 逐 container 判断 exclusive allocation，未获 exclusive slice 的 container
  留在 node shared pool，但总体使用仍受 Pod-level limits 约束。两种 scope 是不同 placement contract，
  不能只看相同 YAML 就假定 NUMA/isolation 语义相同。
- **State Ownership / Enforcement / Observability**：workload author 拥有 Pod budget 与各 container 的
  guaranteed intent；scheduler 仍只决定 node placement；kubelet 的 Topology/CPU/Memory Managers 拥有
  NUMA hint、exclusive/shared assignment 与持久 checkpoint；Linux scheduler/cgroup 执行 CPU affinity、
  memory placement 与 quota。exclusive container 的 container-level CFS quota 被关闭；pod shared-pool
  container 由 Pod-level CFS quota 限制。`resource_manager_allocations_total`、
  `resource_manager_allocation_errors_total` 和 `resource_manager_container_assignments` 以 source/
  assignment_type 暴露 `node_exclusive`、`pod_exclusive`、`pod_shared`，但 allocation counter 不等于
  application latency 或 NUMA-local hit evidence。
- **Validation / Compatibility / Failure Modes**：启用需要 v1.36、`PodLevelResources` 与
  `PodLevelResourceManagers` gates、非 `none` Topology Manager policy、`pod` 或 `container` scope、CPU
  Manager `static`、Memory Manager `Static`；只支持 Linux，Windows 为 no-op。若 exclusive slices 吃完
  Pod budget 却仍有 container 需要 shared pool，Pod 会在 admission 被拒绝。在 `pod` scope，未用完的
  aligned pool 会持续保留到整个 Pod 终止；container crash/restart 不释放它。新 feature 还升级 CPU/
  Memory Manager checkpoint schema，直接降级或关闭 gate 会令旧 kubelet 无法读取，需要 drain node、
  删除 state checkpoint 并重启，这使 rollout/rollback 本身成为运维 contract。
- **Evaluation Contract / What the Evidence Proves and Does Not Prove**：primary sources 证明 alpha feature
  state、scope-dependent allocation semantics、policy/gate prerequisites、admission restriction、quota、metrics、
  Linux/rollback 边界。Blog 的 database/ML YAML 只是机制示例；没有模型、GPU、CPU/NUMA topology、batch、
  concurrency、precision、latency、throughput、利用率或 SLO 实验，因此不证明它提升任意训练吞吐或尾延迟，
  也不证明共享 sidecar 不干扰主进程。
- **Trade-offs / Where the Previous Design Still Applies**：Pod scope 能把 sidecar 纳入同一 NUMA-aligned
  budget，并避免为每个 sidecar 分配 exclusive cores；代价是 residual-capacity fragmentation、persistent
  reservation、scope-sensitive semantics、checkpoint migration 与更复杂的观测/回滚。container scope 保留
  精确的 per-container exclusivity，也允许非关键进程回到 node-wide shared pool，但失去 whole-Pod alignment。
  单容器 Pod、资源需求完全静态、需要独立 accounting/chargeback、不能承担 alpha checkpoint migration，
  或希望 sidecar 与主进程严格 fault/performance isolation 的 workload，原有 per-container model 仍更合理。
- **Evolution / ROADMAP / Adjacent Chapters / Decision**：Ch59 为唯一 owner：现有 placement/capacity
  章节需要把 node selection 与 kubelet 内部 `pod budget → exclusive/shared slices` 的二次拓扑分配分开；
  Ch53 只接 desired spec 与 node checkpoint/rollback handoff，Ch56 只接训练 Pod/sidecar lifecycle 和
  topology contract。它与 in-place Pod-level resize 的关系是 `Layering / Dependency`：一个决定当前 budget
  如何 partition，另一个决定 budget 如何跨 generation 变化，二者不能合并成同一机制。暂定
  `Refine — Existing Argument (Alpha / Version-Grounded)`；Historical Books Gate 关闭，本轮不修改 Books。

### Improving Robustness of Tabular Retrieval via Representational Stability — 23/30

- **Candidate / Week / Source Family / Revision**：`ARXIV-2604.24040-TABLE-SERIALIZATION-STABILITY`；
  W18；v1 于 2026-04-27 first-public，v2 于 2026-04-28 修订且文件大小与 HTML 结构未显示机制级扩章。
  本次以 event-time v1 全文为主，核对 v2 metadata/structure 与当前 author repository；current main
  只有 6 个 commits、无 release/tag，README 已列出论文未评测的 Jina/Rank1 路径，不能倒写为 v1 的
  measured evidence。
- **Direct / Related Primary Sources / Access**：已读 arXiv v1 HTML 的 Abstract、Introduction、Related
  Work、Method、理论假设/证明、adapter objective、Implementation、三组 dataset 与四类 retriever 的完整
  Evaluation、statistical test、A～H Appendices、Conclusion；核对 arXiv v1/v2 history 与作者 repository
  的 serialization、cache、adapter、loss、train/eval entrypoints、数据和 checkpoint 依赖。预印本与代码
  可访问，但没有独立 peer review、external reproduction 或 immutable event-time release。
- **Target / Adjacent Chapters Read / Existing Coverage**：已读 Ch72 全章与相邻 Ch71、Ch73 全章。
  Ch72 已把 parser/chunker/embedding model、source/version 与 hybrid retrieval 写入 ingestion/index contract，
  Ch71 已要求 derived view 显式记录 source identity/validity；缺口是 serialized representation 本身也会改变
  document geometry、index identity 与 retriever compatibility。Ch73 只接 derived-state lifecycle handoff，
  不拥有 corpus representation mechanism。
- **Original Problem / Why Previous Design Was Reasonable**：Transformer retriever 接收 1-D token sequence，
  因而把 2-D table 线性化成 CSV、TSV、HTML、Markdown、JSON、DDL 或带结构 token 的文本，本来是复用
  通用 encoder、vector index 与 lexical index 的合理工程折中。过去常把 serialization 当作 parser 输出格式；
  但同一 table 的语义等价表达会改变 token、position、markup/schema vocabulary，进而改变 embedding、nearest
  neighbors 与 gold-table rank，尤其在 query-table lexical gap 大时暴露 representation instability。
- **Changed Constraint / Principle**：当 corpus 同时经过 parser 迁移、格式标准化、跨系统导入或混合 row
  serialization，同一 source content digest 不再足以确定 retrieval behavior。稳定原则是把
  `source version + parser/serializer + representation family + retriever/tokenizer + adapter/index revision`
  共同视为 derived-view identity，并把 robustness 与 peak accuracy 分开评估；serialization-invariance
  是有条件目标，不是把任意格式平均后必然恢复“真实语义”。
- **Mechanism / State Ownership**：对 table `T` 的多种 serialization embeddings `z_s(T)` 求 centroid
  `c(T)`。其无条件结论只是 centroid 最小化到各 view 的 Euclidean squared distance；只有在
  `z_s(T)=mu(T)+delta_s(T)` 且平均 format shift 接近零时，centroid 才近似 shared semantic signal。
  作者再冻结 base retriever，以 `LayerNorm → down projection → GELU/dropout → up projection → scaled
  residual` 将单一 document embedding transport 向 centroid。invariance loss 拉近同 table views，identity
  loss 保持 frozen query-space compatibility，variance/covariance terms 防 collapse 与冗余。Source store
  仍拥有原 table；serializer/encoder 拥有 derived view；adapter checkpoint 拥有 correction policy；vector/
  lexical index 拥有可服务 representation；query encoder 保持 frozen，不能把 adapter 当 source of truth。
- **Control / Data Flow / Implementation**：offline 路径为 `table → 17 serializations → frozen embeddings/cache
  → align by table ID → multi-view batch → adapted-space centroid → VICReg-like optimization → checkpoint`；
  serving 路径为 `chosen single serialization → frozen document encoder → adapter → vector index`，query 仍走
  frozen encoder。公开默认值为 20,000 steps、batch 512、rank 512、`alpha=0.01`、`lambda_inv/id=100`、
  `lambda_var=25`、`lambda_cov=1`。论文称“不需 re-indexing”，但 algorithm 又要求把 adapted vector index
  进数据库；较稳妥的事实边界是无需多格式 online encoding 或 base-model retraining，现有 index 是否需要
  vector replacement/rebuild、atomic publication 与 rollback 并未由论文澄清。
- **Evaluation Contract**：WTQ 4,200 questions/2,044 tables、WikiSQL 15,878/5,069、NQ-Tables
  966/169,898；MPNet、BGE-M3、ReasonIR 与 SPLADE；17 serialization views 加 5 种 centroid；指标含
  Recall@1、gold rank/pairwise score、`Delta log-rank`，pairwise Wilcoxon 使用 Benjamini–Hochberg FDR、
  `alpha=0.01`。joint adapter 用三 dataset，subset adapter 只用 WTQ+WikiSQL 并在 NQ transfer；另有 row-level
  mixed-format perturbation。Hardware、wall-clock、index build/replace latency、query throughput、memory、
  seeds/variance、ANN parameters、top-k reranker、end-to-end QA/SLO 均 `Not Disclosed`；作者 repository 的
  data/checkpoints 通过外部 Drive 提供，未形成 immutable release。
- **What the Evidence Proves**：serialization 对四类 retriever 的 Recall@1/rank 产生显著且 model/dataset/
  format-dependent variation；centroid family 在聚合 pairwise comparison 中总体优于多种 single formats。
  对部分 dense retriever，单-view residual transport 能缩小 format sensitivity，并在 subset→NQ 与 mixed-format
  test 中显示有限 transfer。实验还直接证明 robustness gain 不能只看一个平均 headline：例如 WTQ MPNet
  HTML 从 0.09 到 0.18，而 NQ mixed-format MPNet 从 0.2847 降到 0.2526；ReasonIR 在同一 NQ perturbation
  从 0.1925 到 0.2422。
- **What It Does Not Prove / Limitations / Threats to Validity**：centroid 的 least-squares optimality 不证明
  semantic optimality；后者依赖未由 encoder 强制的 centered-shift assumption。schema/markup formats 常有
  table-independent displacement，SPLADE 各格式更违反该条件；dense adapter 会混合 coordinates、破坏 sparse
  lexical geometry。论文没有 loss-component removal、serialization-family selection ablation、multiple seeds、
  confidence interval、external corpus/domain、hybrid retrieval、reranker、citation/answer success、production
  index migration 或 deletion/freshness test；因此不能推出 adapter 普遍优于选择一个稳定 serialization，
  也不能把作者 Recall@1 外推成 RAG task success。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：多-view centroid target 增加 offline
  serialization、encoding、cache、alignment 与 checkpoint governance；adapter 降低 online multi-view cost，
  却新增 retriever-adapter compatibility、republication、rollback 与 geometry drift。Identity regularization
  保护强格式也可能限制弱格式修正；强 invariance 则可能抹去有用 schema/lexical signal。Canonical TSV/
  DDL 在固定 schema 与已验证 workload 中仍更简单；SPLADE/BM25 对 rare identifiers 与 lexical exact match
  仍成立；structure-aware table encoder 在结构语义本身重要时仍是不同设计分支；hybrid retrieval 可保留
  dense/sparse 互补，而不是把 dense correction 强加给所有 view。
- **Evolution / ROADMAP / Final Disposition**：这是 Ch72 从 `parser/chunker/embedding identity → serialized
  representation identity → representation-shift robustness` 的 `Direct Evolution`，与 Ch71 derived-view
  validity 是 `Layering / Dependency`。Ch72 当前原则已覆盖多数 ownership，但没有明确 serialization
  version、format perturbation test 与 dense/sparse correction incompatibility；暂定 `Refine — Existing
  Argument (Experimental)`，Ch72 为唯一 owner、Ch71 只接 identity handoff。23/30 维持；Historical Books
  Gate 关闭，当前不修改 Books。

### Rewarding the Scientific Process: Process-Level Reward Modeling for Agentic Data Analysis — 26/30

- **Candidate / Week / Source Family / Revision**：`ARXIV-2604.24198-DATAPRM-AGENTIC-DATA-ANALYSIS`；
  W18；v1 于 2026-04-27 first-public，v2 于 2026-06-20 修订并进入 KDD 2026 版本。事件归属与机制事实
  以 v1 为准；v2 只用于核对 revision boundary。当前 DataMind repository 已写成 8K instances、较新的
  ms-swift/vLLM 环境并加入后续项目，而 v1 正文只称 `over 7K`，不能把当前 artifact 倒写为事件日事实。
- **Direct / Related Primary Sources / Access**：已读 arXiv v1 的 metadata、Abstract、Introduction、
  Preliminaries、general-PRM failure analysis、Method、tool-augmented ReAct verifier、ternary reward、数据构造、
  GRPO integration、完整 experiments/ablations、cost analysis、Limitations、Conclusion 与 A～H Appendices；
  核对 v2 结构和当前 DataMind/DataPRM README、evaluation/training artifact 入口。没有 immutable event-time
  release、external reproduction 或独立 peer-review artifact；当前 repository 无 release 显示。
- **Target / Adjacent Chapters Read / Existing Coverage**：已读 Ch62 及相邻 Ch61、Ch63，并联读 Ch29
  reward interface 与 Ch77 workflow/evaluator-driven search。Ch62 已覆盖 scorer 不是 truth、trajectory/
  environment/executable evidence 与 feedback contamination；Ch29 已覆盖 process reward、verifier exploit
  和 noisy measurement；Ch77 已覆盖 evaluator/version/artifact binding。新增机制缺口是 verifier 不再只是
  被动读 trajectory，而是拥有环境查询、循环反馈与 recoverability-aware step semantics。
- **Original Problem / Why Previous Design Was Reasonable**：静态 PRM 对通用语言推理有效，因为它能低成本
  批量读取 prefix 并判断局部合理性。但 agentic data analysis 的步骤会引用 schema、文件、图像与运行环境：
  一条语义上错误的操作可能成功执行而被静态 judge 接受；一次路径或 grounding 探索也可能报错，却为后续
  修复提供信息而被静态 judge 过度惩罚。constraint 由“只读文本推理”变化为“动作正确性依赖外部状态，且
  错误具有不同 recoverability”。
- **Mechanism / State Ownership**：DataPRM 是 generative ReAct verifier。它读取 policy trajectory/current
  step，可多轮调用 `query_document` 与 `query_image` 核验环境，并把历史 `(reward, rationale)` 追加到下一轮
  verification context。reward 为三值：`1` 表示正确或推进任务，`0.5` 表示可修复、grounding-relevant 或
  提供有用信息的错误，`0` 表示不可恢复错误或 hallucination。Policy 拥有候选 trajectory；evaluation
  environment 拥有文档/图像 state；verifier runtime 拥有查询、rationale 与历史反馈；reward pipeline 拥有
  step labels/aggregation；outcome evaluator 在最后一步不一致时仍拥有覆盖 authority。
- **Control / Data Flow / Implementation**：`trajectory prefix → verifier reason/act → document/image query →
  observation → repeated verification → ternary score+rationale → append as next-step context`。数据由公开文件、
  GitHub 与人工修订文件构造；Qwen3-235B-A22B-Instruct 生成每题 4 条轨迹，DeepSeek-V3.2 以 final-answer
  disagreement 过滤并标注 outcome，Qwen3-235B 做首轮 step annotation/error attribution，AutoManual 聚类
  error types，人工核查 rationale/few-shots。训练将 `mean(process rewards)` 与 outcome reward 按
  `beta=0.5` 组合；若 final-step PRM 与 outcome 冲突，final step 被 outcome 覆盖，再进入 group-normalized
  GRPO。这个 override 使 terminal outcome 保持 authority，也限制了把提升归因于纯 process supervision。
- **Evaluation Contract**：SFT verifier 为 Qwen3-4B-Instruct，3 epochs、batch 32、cutoff 24,576；TTS policy
  为 Qwen3-235B-A22B-Instruct-2507，Best-of-N 为 4/8/16；ScienceAgentBench 从 102 项中过滤为 78 项，
  DABStep 超过 450 challenges。RL policy 为 Qwen2.5-Coder-7B-Instruct，DABench/TableBench，prompt 4,096、
  response 8,192、batch 32、group 4；全部实验为 8×H20。论文报告 DataPRM 在作者 contract 下改善 TTS，
  并在 RL 中得到 DABench 78.73%、TableBench 64.84%；这些是作者实验，不是生产通用结论。judge 只在
  61/100/100 个样本上与人工校准，DABStep 的 manual/`fee.json` inconsistency 又由作者统一修正后评测。
  多轮、environment-aware、reflection 与 filtering ablations 存在，但部分 filtering 叙述数字与表格不一致，
  因而不引用该处 headline。
- **Cost / What the Evidence Proves**：v1 Appendix 报告 GenPRM 约 7,061 tokens/14.86s，Self-Reward
  25,282.51 tokens/194.95s，DataPRM 21,455.78 tokens/24.66s；并行 DataPRM 写为 3.30s。它证明在作者
  模型、工具、任务、修正过的 benchmark 与 8×H20 contract 下，环境查询和 recoverability taxonomy 能纠正
  一部分 static-judge false accept/false reject，并可形成更密集的 RL signal。3.30s 没有完整 topology、
  isolation、concurrency、queueing 或 SLO disclosure，不能外推为 production latency。
- **What It Does Not Prove / Limitations / Threats to Validity**：论文只覆盖 analysis/reasoning/visualization，
  不覆盖模型训练与预测 workflow；SFT 依赖高质量 synthetic trajectory。同源模型家族同时参与 generation、
  annotation、tool query 与 judge，存在 correlated blind spot；主要结果缺 multi-seed uncertainty。`0.5` 是
  domain-specific heuristic，不是通用 error severity。verifier 可以读/查环境，不代表能区分所有 silent
  semantic error；query model、document parser、image model 或历史 rationale 都可能污染下一步判断。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：active verifier 获得 grounding evidence，
  却新增 tool authorization、sandbox、snapshot consistency、query cost、side effect、feedback accumulation、
  verifier-version drift 与 cross-trajectory contamination。多轮 verifier 还可能把昂贵环境工作移出 token
  统计。对纯数学、schema、compiler/tests 等可确定验证任务，静态 rule/executable verifier 仍更便宜、更易
  复现；outcome-only reward 在 terminal truth 足够强时仍合理；人工 review 在高风险、开放语义和环境不可
  快照化时不可被替代。
- **Evolution / ROADMAP / Final Disposition**：这是 `static step scorer → trajectory-aware scorer →
  environment-aware active verifier → recoverability-aware process reward` 的 `Direct Evolution`；与 Ch29
  reward mapping、Ch77 workflow state/permissions 是 `Layering / Dependency`。Ch62 为唯一 owner，需在未来
  Books Gate 打开后 refine active verifier 的 state/authority/contamination contract；Ch29 与 Ch77 只接短
  handoff。26/30 维持，暂定 `Refine — Existing Argument (Experimental)`；Historical Books Gate 关闭，
  当前不修改 Books。

### GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents — 26/30

- **Candidate / Week / Source Family / Revision**：`GLM-5V-TURBO-MMTP-MULTIMODAL-RL-RUNTIME`；W18；
  technical report v1 于 2026-04-29 first-public，v2/v3 分别在 5 月 6/12 日修订。当前 GLM-V repository
  把产品发布写为 `2026/04/02`，早于 technical report；该 product-event 已回拨 W14，以 18/30
  `Version/Product Fact / Mechanism Not Disclosed` 登记，不能取消 4 月 29 日 report 作为 W18 primary-research event 的归属，也不能用 current repo
  state 倒写 v1 已公开的 artifacts。
- **Direct / Related Primary Sources / Access**：已读 arXiv v1 的全部正文：Overview、CogViT、MMTP、
  pretraining/joint RL、multimodal RL infrastructure、tool/framework integration、ImageMining、design lenses、
  evaluation、remaining challenges、contribution、references 与 Appendix A demo cases；核对 v3 heading/
  revision boundary。联读 Z.ai official API guide、GLM-V current repository、ImageMining repository/dataset
  schema 与 GLM-skills repository。模型权重、训练代码、RL runtime、CogViT checkpoint 与 event-time
  immutable release 未公开，现有 repo 主要覆盖旧 GLM-V 系列和 later/current product artifacts。
- **Target / Adjacent Chapters Read / Existing Coverage**：已读 Ch34 全章及相邻 Ch33/35，并联读 Ch23、
  Ch29、Ch36～39、Ch44、Ch62、Ch71/73 的相关机制。Ch34 已覆盖 PP boundary tensor、multimodal branch、
  variable-length imbalance 与 topology；Ch36 已覆盖 CP/TP/DP 组合；Ch44 已覆盖 model-native MTP artifact；
  Ch38 已覆盖 inference identity/state machine；Ch71/73 已覆盖 text-centric context/memory loss。真正新增的
  owner gap 是：multimodal token/patch representation 不是只影响模型质量，它会改变 pipeline boundary bytes、
  partition point、micro-batch cost vector 与 communication path。故唯一 owner 从旧 ledger 的 Ch21/38 修正为
  Ch34，其他章节只接 handoff。
- **Original Problem / Why Previous Design Was Reasonable**：text-only MTP 可把 prefix token IDs 直接嵌入
  prediction head；PP 也可把近似同 shape 的 hidden activations 沿 layer boundary 传递。视觉输入加入后，
  image embeddings 具有不同分布、variable token count 与额外 ViT/projector state。直接把 visual embeddings
  传给轻量 MTP head 保留最多信息，却要求跨 PP stage 传播/对齐大 visual tensors；在 forward 后再做 CP/TP
  partition 也简单，但每 rank 先持有 full patch tensor，造成 peak memory、redistribution 与 load skew。
- **Changed Constraint / Principle**：当 workload 从固定 text sequence 变化为图像、视频和 text 混合轨迹，
  单一 `sequence length` 不足以描述执行成本。系统需要把 `text tokens + ViT tokens + image count/resolution +
  modality processor/revision` 纳入 sample identity、partition 与 bin-packing；跨 stage representation 应只保留
  consumer 真正需要的信息。Representation simplification 可以降低 communication，但它同时改变 optimization
  contract，不能作为语义透明的 runtime compression。
- **Mechanism / State Ownership — CogViT / MMTP**：CogViT 两阶段训练先用 35% masked-image modeling，
  以 SigLIP2 semantic feature 与 DINOv3 texture feature 双 teacher 蒸馏，再用 NaFlex variable-resolution、
  SigLIP objective、64K global batch 与 8B 中英 image-text corpus 做 contrastive alignment。MMTP 比较三种
  visual-prefix input：直接传 visual embedding、完全 mask、或保留 visual positions 但统一替换为 learnable
  `<|image|>`。作者采用第三种，以避免 visual embedding 跨 PP stages 传播并兼容 SP/CP。Vision processor/
  encoder 拥有 patch/visual representation；LLM backbone 拥有 fused hidden state；MTP head 只消费 position+
  shared-image-token contract；checkpoint 必须把 processor、special token、position mapping 与 head revision
  绑定，runtime 不能只按 tokenizer/model name 推断兼容性。
- **Mechanism / Control and Data Flow — Multimodal RL Runtime**：`heterogeneous task → unified VLM RL Gym →
  rollout inference → rule verifier(local/sync) or model judge(API/async) → configurable reward aggregation →
  batch construction → reference/policy forward → weight transfer/update`。请求 completion callback 使 reward
  不等 full rollout batch，batch construction 与 old-policy CPU→GPU transfer overlap；reference weights 常驻
  CPU，使用前 prefetch、之后释放；completion-count/time-threshold early abort 的 prompts 可缓存重用。ViT/
  projector 使用 targeted recomputation+CPU offload。长视频的 CP/TP partition 前移至 data loader，并与
  downsample groups 对齐；DP group load balancing 后用 async all-to-all 精确 dispatch，micro-batch 同时按
  sequence length 与 ViT token count bin-pack。这里 data loader/sampler 拥有 workload partition，parallel
  runtime 拥有 rank layout/transfer completion，reward service 拥有 verifier/aggregation，trainer 拥有
  policy/reference version boundary。
- **Implementation / Evaluation Contract**：报告公开的机制数字包括 0.5B MMTP ablation、CogViT 训练配比、
  30+ RL task categories、7 GB GPU communication-buffer reduction，以及多个 benchmark 分数；但没有披露
  GLM-5V-Turbo parameter count、完整 model config、训练 GPU 类型/数量、world size、PP/TP/CP/DP degrees、
  precision、token/image/video length distribution、rollout concurrency、abort rate、wall-clock、cost、seeds/
  confidence interval或 MTP inference acceptance/SLO。ImageMining 含 217 个 manually collected cases、7 domains、
  23 subcategories、5 reasoning types，当前 repo 只有 4 commits、data JSONL 与外部 image archive；公开 reasoning
  chain 和 benchmark-construction/training proximity 增加 contamination/evaluator coupling 风险。
- **What the Evidence Proves**：在作者 0.5B ablation 中，共享 `<|image|>` representation 比直接 visual
  embeddings 表现出更低 loss/更稳 convergence；系统描述证明团队实际把 multimodal RL 拆成可 overlap stages，
  并针对 visual-token imbalance 前移 partition、采用双维 bin-packing。报告也给出一个重要反例：joint RL
  覆盖更广并不自动避免遗忘，未覆盖且正交的能力仍可能下降。长期可用的结论是“modality shape 属于
  distributed execution contract”与“model/harness/evaluator 共同决定可观察 capability”，不是某个榜单名次。
- **What It Does Not Prove / Limitations / Threats to Validity**：MMTP ablation 只在 0.5B 模型比较部分方案，
  不证明 full-scale quality、speculative acceptance 或 serving speed；`7 GB` 缺少 baseline topology/shape，
  不等于端到端节省。没有 component-isolated ablations 可把 CogViT、data、RL、tools、skills 与 harness 的贡献
  分离；Claw/GUI benchmarks 同时测 model、prompt、tools、framework 与 verifier。作者对 cross-task transfer、
  weaker interference、proxy-task benefit 的观察缺多 seed/causal isolation。API guide 的 200K context、128K
  output 是 current product facts，不证明有效 multimodal memory 或 paper-event inference mechanism。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：shared image token 降低 PP traffic 与
  mapping complexity，却丢失 MTP head 的细粒度 visual content，并新增 special-token/position/processor
  compatibility；upstream partition 降低 full-tensor residency，却把 data-loader metadata、downsample-group
  alignment、all-to-all completion、straggler/failure recovery 和 determinism 带入 correctness path。Async RL
  overlap 提高 utilization，却增加 stale policy/reference、partial batch、abort/reuse bias、reward-late-arrival 和
  replay provenance。固定分辨率、forward-time partition 与 text-only MTP 在小图、短序列、单机或实现简洁优先时
  仍合理；模块化 text/vision tool cascade 在独立升级、审计和降级优先时也继续成立。
- **Evolution / ROADMAP / Final Disposition**：相对 text PP 是 `Direct Evolution`：`uniform token batch →
  modality-aware cost vector → upstream partition + topology-aware dispatch → joint text/ViT bin-packing`；MMTP
  与 Ch44 是 `Layering / Dependency`，multimodal context/memory 与 Ch71/73 是 `Principle Reuse`，model–harness
  coupling 与 Ch62/77 是 `Layering / Dependency`。26/30 维持；暂定 `Refine — Existing Argument
  (Experimental)`，Ch34 为唯一 owner，Ch23/29/36/38/44/62/71/73 只接 handoff。Historical Books Gate 关闭，
  当前不修改 Books。

### Synthetic Computers at Scale for Long-Horizon Productivity Simulation — 27/30

- **Candidate / Week / Source Family / Revision**：`SYNTHETIC-COMPUTER-ENVIRONMENT-LONG-HORIZON-SIMULATION`；
  W18；arXiv:2604.28181 只有 v1，于 2026-04-30 first-public，作者和 Microsoft Research 均把它标为
  preview / work in progress / preliminary experiments。后续 dataset 更新可用于核验 artifact，不得倒写为
  4 月 30 日已经公开的 paper evidence。
- **Direct / Related Primary Sources / Access**：已读 v1 全部正文与 33 页 PDF，包括 Introduction、persona、
  filesystem policy、file graph、dependency-aware artifact construction、setup/work agents、跨日 simulation、
  in-domain/OOD evaluation、Discussion、Limitations/Future Work，以及 Appendix A 的完整 retrospective report；
  联读 Microsoft Research publication page 与官方 Hugging Face dataset card、schema、compressed artifact
  说明和 limitations。当前未发现作者公开 generator/simulator/evaluator 代码；因此可验证的是论文描述、
  98-row metadata dataset、约 1.4 GB computer artifacts 与 retrospective reports，不是可复现的完整生成流水线。
- **Target / Adjacent Chapters Read / Existing Coverage**：已读 Ch77 全章与相邻 Ch76/78，并联读 Ch23、
  Ch62、Ch71、Ch73、Ch80 的相关段落。Ch23 已覆盖 executable-state synthetic data 与 generator/judge
  shared ontology；Ch62 已覆盖 rubric formation、trajectory evidence 与 judge coupling；Ch71/73 已覆盖
  working state、archive 与 derived strategy provenance；Ch77 已覆盖 durable state、artifact reference、
  replay、evaluator-driven search 和 human gate；Ch78 已覆盖 collaborator/shared-state tax；Ch80 已覆盖
  run/evidence plane。新增缺口不是一个新 Agent framework，而是 **synthetic environment 本身如何成为可演化、
  可评估的 workflow state substrate**。因此 Ch77 是唯一 owner，其他章节只接 handoff。
- **Original Problem / Why Previous Design Was Reasonable**：最早的 synthetic-data pipeline 可以只生成
  prompt、answer 或短 trajectory，因为任务通常由单段输入完整描述，environment state 小且可重置。真实
  productivity work 却依赖私人 filesystem、历史版本、多个相互引用的 artifacts、collaborator feedback 与跨日
  commitment；采集真实 trajectory 又昂贵且涉及隐私。只合成 task 会得到缺少前置历史和后续状态变化的 toy
  workflow，但直接使用真实用户电脑仍是高成本、高风险的合理旧分支，尤其适用于需要真实分布与 human outcome
  的最终 validation。
- **Changed Constraint / Principle**：当评估对象从“完成一个请求”变为“在一个月尺度的工作环境中维持事实、
  版本和承诺”，task text 不再足以定义 state。Synthetic generation 必须同时构造 environment identity、
  artifact dependency、virtual time 与可观察 side effects；而且生成的世界越丰富，越需要独立证明 realism，
  不能把内部一致性当成外部真实性。
- **Mechanism / State Ownership — Environment Construction**：`persona → detailed user profile → filesystem
  policy → file inventory + metadata → directed dependency graph → topological artifact instantiation`。File graph
  显式表示 reference、derived-from、later-version 与 archive extraction；Kahn topological order 让上游 artifact
  成为下游生成 context，timestamp 在同层打破 ties。公开文件优先下载，失败后转为 synthesis；其他文件由具备
  document/spreadsheet/presentation skills 的 LLM agent 生成。Environment builder 拥有 persona/policy/graph/
  virtual-time identity，artifact store 拥有 bytes/version/provenance；下载失败后的 synthesis fallback 必须被记录，
  否则“外部来源”会静默变成模型生成内容。
- **Mechanism / Control and Data Flow — Long-Horizon Run**：`synthetic computer → setup agent creates about-month
  objectives + deliverables + simulated collaborators/private reference material → work agent creates weekly plan → daily
  session restores activity log/computer/replies → reads/edits artifacts and messages collaborators → updated filesystem,
  file graph and event history become next session state → terminal artifacts + trajectory enter evaluation`。Workflow
  runtime 而非模型应拥有 day/session cursor、objective/dependency status、message delivery、artifact version 与
  retry/recovery；setup agent 只生成 provisional world specification，work agent 只在该世界内行动。
- **Mechanism / Derived Experience**：作者让同一 setting 运行五次，每次输出先生成 draft rubric，再合并为
  final rubric；Opus 4.6 judge 读取 files、screenshots 与 artifacts 评分。900/100 synthetic computers 作为
  experience/held-out split；训练侧不更新 weights，而是把 retrospective reports 按 occupation 聚合，提取高频
  lessons，再用 skill-creator 生成 occupation-specific skills，交给同一 work agent 重跑 held-out environments。
  这条路线是 `raw trajectory → retrospective diagnosis → scoped derived skill → replay on held-out environment`，
  derived skill 必须保留 source runs、occupation scope、extractor/judge/version、supersession 与 rollback，不能
  因频率高就升级为 platform policy。
- **Implementation / Evaluation Contract**：作者创建 1,000 台 synthetic computers、每台一次 simulation；
  报告平均 2,272 turns、8.59 小时 wall-clock、5.5 collaborators、31 communications，pre/post files 为
  111.6/197.4，67.8% 为 DOCX/XLSX/PDF/PPTX。Agent runtime 使用 Claude Code SDK，通常为 Sonnet 4.6，
  setup 为 Opus 4.6；非 Office artifact 用 Anthropic skills，Office artifact 用 MiniMax skills。100 台样本用于
  artifact scoring；occupation skills 在 held-out 100 台上从 61.6 提至 68.6（83 wins/17 losses），100/500/900
  source simulations 对应 64/75/83 wins。OOD 使用 GDPVal 220 tasks 与官方 rubrics，在 Sonnet setting 为
  105 wins/67 losses，并报告 sign tests。论文没有公开 token/API/compute cost、并发、失败/中止率、模型
  sampling、完整硬件、seed uncertainty、human realism baseline 或独立 evaluator。当前 dataset card 实际为
  98 台（48 macOS/50 Windows），metadata parquet 不含 file bytes；bytes 与 retrospective reports 另以 tar.zst
  发布，和论文“release 100”存在 2 台差异，必须作为 current artifact drift 保留。
- **What the Evidence Proves**：作者实现了 environment-first synthetic pipeline，并展示 file dependency、
  multi-artifact state 与跨日 activity log 可以支持很长的模拟轨迹；Appendix 暴露了 cross-document numeric drift、
  ignored reviewer corrections、blank messages 与 tool/path errors，说明 terminal success narrative 会掩盖长期状态
  failure。受限实验还说明从这些模拟轨迹提取的 scoped skill 在作者的 synthetic held-out 和 GDPVal judge contract
  下有正向信号。可沉淀的结论是“synthetic data 要合成 stateful environment，并把 evolving artifacts 作为
  evidence”，不是“模拟规模自动产生真实生产力”。
- **What It Does Not Prove / Limitations / Threats to Validity**：同一模型生态参与 persona/world/objective、
  collaborator、work trajectory、rubric 与 judge，shared ontology 和 correlated blind spot 没有独立隔离；五次
  candidate run 参与 rubric formation，使 criteria 具有 data-dependent/circular 风险。没有 human expert 对
  environment realism、artifact correctness 与 rubrics 的系统审计，也没有真实电脑、人类纵向 workflow 或
  privacy-utility baseline。`millions/billions` 只是 persona abundance + sufficient compute 的推断；skill 到 model
  weight internalization/reset 只是 future loop。当前公开 98 台、English-only、小规模 dataset 也不能复现
  1,000-run headline。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：environment synthesis 获得隐私友好、
  可重复和可规模化的练习场，却新增 synthetic-world drift、graph inconsistency、download→synthesis provenance
  loss、artifact hallucination、rubric leakage、judge self-preference、context exhaustion 与 storage/compute cost。
  随着电脑反复被 simulation 更新，早期错误和伪造历史也会累积为下一轮“grounding”。短、无状态、可执行
  verifier 完整的任务仍应使用 task-only synthesis；真实用户研究、domain-expert review 与 shadow/canary 仍是
  deployment-validity 的旧分支；高风险事实不能从 synthetic retrospective 自动写入 global memory 或 policy。
- **Evolution / ROADMAP / Final Disposition**：这是 `task-only synthesis → executable task state → synthetic
  computer/environment state → long-horizon evolving artifact graph → retrospective derived skills → hypothetical
  weight internalization` 的 `Direct Evolution`。它与 Ch23/62/71/73 是 `Layering / Dependency`，与 Ch78
  的 simulated collaborators 是 `Principle Reuse`，不能把 reactive NPC 当成真实 Multi-Agent organization。
  27/30 维持；暂定 `Refine — Existing Argument (Experimental)`，Ch77 为唯一 owner，Ch23/62/71/73/78/80
  只接 handoff。Historical Books Gate 关闭，当前不修改 Books。

### Step-Audio-R1.5 Technical Report — 24/30

- **Candidate / Week / Source Family / Revision**：`STEP-AUDIO-R15-RLHF-REWARD-EVALUATION`；W18；
  arXiv v1 于 2026-04-28 first-public，v2 于 2026-05-31 修订。v2 将 Step-Caption 样本数从 v1 的
  907 纠正为 905；current repository 同样发布 905 audio/metadata，故 W18 事件以 v1 机制为准，样本数
  引用必须锁定 revision。
- **Direct / Related Primary Sources / Access**：已读 v1/v2 全文和 PDF：Introduction、Architecture、
  mid-training、cold-start SFT、rubric-based generated reward model、PPO-style objective、全部 benchmark/
  results 与 references；报告没有 Appendix、Limitations、Related Work、ablation 或独立 human study。联读
  official Step-Audio-R1/R1.5 repository、R1.5 open-source plan，以及 Step-Caption、Step-DU、Step-SPQA
  三套公开 benchmark 的 metadata schema、model/judge prompt contract 与 scoring flow。R1.5 inference code、
  weights/checkpoint 和 training/reward-model code 仍未公开；repository 的可运行 code/weights 属于 R1/R1.1，
  不能作为 R1.5 复现证据。
- **Target / Adjacent Chapters Read / Existing Coverage**：已读 Ch27 全章与相邻 Ch28～30，并联读 Ch38、
  Ch62。Ch27 已完整覆盖 human/AI/verifiable reward 的来源差异、preference/rubric、Reward Model、KL、
  Goodhart 与 independent evaluation；Ch28 已覆盖 PPO/reference/reward state；Ch29 已覆盖 verifier proxy 与
  multi-stage training；Ch62 已覆盖 claim/object/distribution/scorer identity、rubric formation 与 dataset
  governance；Ch38 已覆盖 audio pipeline 和 modality/runtime contract。论文没有足够新机制突破这些框架；
  owner 从初始 Ch38 修正为 Ch27，Ch62 接 evaluation handoff，Ch38 只记录 text-output execution boundary。
- **Original Problem / Why Previous Design Was Reasonable**：RLVR 把数学答案、标签或规则检查转换为低成本、
  可扩展 reward；在明确 acoustic classification/QA 中，离散 correctness 是合理旧方案，也能避免 learned
  preference model 的主观偏差。长时程 spoken interaction 同时包含 instruction retention、factual correctness、
  tone、coherence 和 naturalness；若 reward 只观察最终 text label，policy 会优化 verifier 可见的“what to say”，
  而忽略 verifier 未表示的交互质量。但这只是通用 proxy-objective 问题，不是该报告已经独立证明的 audio
  特有因果机制。
- **Changed Constraint / Mechanism**：architecture 沿用 frozen Qwen2 audio encoder（25 Hz）、2× temporal
  downsampling adaptor（12.5 Hz）与 Qwen2.5-32B decoder，输入 audio features，先生成 explicit reasoning，
  再生成 **纯文本** reply。训练为 `audio/text mid-training → multi-turn cold-start SFT → unified RLHF`。
  对有显式 criteria 的样本，generated reward model 读取 task rubric；无 rubric 时对 policy/reference response
  做普通 pairwise preference，输出多级 relative judgment，再映射 scalar reward，用 PPO-style clipped objective
  和 reference-policy KL 更新。作者声称把两类 supervision joint optimize，因为 sequential stages 会 forgetting，
  但未公开对比实验。Policy trainer 拥有 old/current/reference state；reward service 拥有 rubric/reference/
  judgment mapping；dataset owner 应拥有 human population、annotation/rubric provenance。报告没有披露这些
  owner 的具体 implementation。
- **Evaluation Contract / Artifact Audit**：表格汇总 AudioMultiChallenge、Big Bench Audio、MMSU、MMAU、
  Spoken MQA、Step-Caption、Step-DU 与 Step-SPQA，统一通过作者 harness 调用各 baseline official API。
  三套自建公开集为 905/87/550 samples。Step-Caption 用 LLM judge 对 15 speaker attributes + speaker count
  打分，speaker-count 错误会把整例置零；Step-DU 用 judge 返回 0/0.5/1；Step-SPQA 先 exact match，失败后
  用 task-specific LLM judge 给 YES/NO。公开 artifact 提高 schema/prompt 可审计性，却没有公开 paper run 的
  judge model/version、sampling、retries、API date、audio preprocessing、uncertainty 或 contamination analysis。
- **What the Evidence Proves**：v1/v2 与 repository 证明团队提出并描述了在同一 Reward Model 中混合
  rubric-conditioned 与 generic pairwise preference 的训练路线，并发布三套 S2T benchmark artifacts。作者
  harness 下，R1.5 相对 R1 的八项平均为 77.97 vs 72.50，主要差异来自 Audio MC、Step-DU 和 Step-SPQA；
  这些只支持作者 evaluation contract 下的 text-answer audio understanding signal。
- **What It Does Not Prove / Claim–Evidence Mismatch**：报告的核心主张是 prosodic naturalness、emotional
  continuity、immersive spoken dialogue 得到改善，但模型 architecture 明确只输出 text，全部实验也要求
  speech-to-text response；没有 waveform/speech generation、prosody metric、end-to-end spoken-response pair、
  blinded human preference、longitudinal conversation study 或 production outcome。因此实验不能测量其核心
  “how to say it” 主张。更没有 `R1 + same data + RLVR` 对 `R1.5 + RLHF` 的 controlled ablation，不能把增量
  因果归给 RLHF；architecture/data/cold-start/RM/PPO 同时变化。论文没有披露 human-feedback population、
  pair count、rubric generation、Reward Model identity/accuracy/disagreement、PPO hyperparameters、compute、
  hardware、precision、sequence/audio length、batch/concurrency、seeds、SLO 或 limitations。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：mixed reward 可以覆盖 hard criteria 与
  soft preference，却把 heterogeneous ordinal judgments 压成单一 scalar；scale calibration、rubric leakage、
  reference quality、judge self-preference、preference population 与 component conflict 会进入 policy gradient。
  Joint training 可能减轻 stage forgetting，也可能让易优化、高幅度 component 支配其他目标。明确可验证的
  audio QA 继续适用 RLVR；自然度需要独立 speech-output human evaluation；多目标冲突严重时，hard constraints
  + separate preference objectives/Pareto gate 比一个 unified scalar 更可审计。
- **Evolution / ROADMAP / Final Disposition**：论文试图形成 `discrete audio-label RLVR → mixed rubric +
  holistic preference RM → joint PPO update` 的 `Direct Evolution`，但公开 evidence 只证明路线描述和 S2T
  score，没有证明 claimed spoken-experience transition。24/30 维持；最终 disposition 为 `No Change —
  Existing Argument / Claim–Evidence Mismatch`。Ch27/62 已包含长期原则，不用薄弱案例扩写 Books；Ch38
  不接产品/模型 benchmark。Historical Books Gate 关闭，当前不修改 Books。

### World-R1: Reinforcing 3D Constraints for Text-to-Video Generation — 26/30

- **Candidate / Week / Source Family / Revision**：`WORLD-R1-3D-REWARD-FLOW-GRPO`；W18；
  arXiv:2604.24764 v1 于 2026-04-27 first-public，v2/v3/v4 分别于 05-20、05-22、05-26 修订。
  W18 事件只使用 v1 当时可见的机制与实验；v4、ICML project page、当前 code/dataset 只用于核验
  revision 与 artifact 演进，不倒写成 4 月 27 日已发布事实。
- **Direct / Related Primary Sources / Full-read Coverage**：已读 v1 全部 HTML，包括 Abstract、Introduction、
  Related Work、Flow-GRPO preliminaries、camera conditioning、reward、dataset、training、全部实验、Limitations、
  Appendices A～E、user/metric-validation studies、scaling/long-video/scene slices、reward-hacking ablation；联读
  v4 对应章节、官方 Microsoft project/technical page、当前 `microsoft/World-R1` repository 的 README、training
  entry/reward-service path，以及官方 Hugging Face dataset card/splits。当前 artifact 没有公开 paper-event
  checkpoints、完整训练 run logs 或逐例 evaluation outputs，故 artifact access 不等于作者结果可独立复现。
- **Target / Adjacent Chapters Read / Existing Coverage**：已读 Ch29 全章及相邻 Ch27、Ch28、Ch30，并联读
  Ch62 与相邻 Ch61/63。Ch29 已覆盖 group-relative advantage、rollout cost、composite reward scale、measurement
  noise 与 verifier exploit；Ch62 已覆盖 subject/scorer/environment identity、proxy metric、human calibration 与
  correlated judge。World-R1 的新增机制缺口是 **GRPO 从 token response 扩展到高维 diffusion trajectory 后，
  reward evaluation 本身成为一个昂贵、异构、可失败的训练子系统**。Ch29 是唯一 owner，Ch62 只接
  reward/evaluation independence handoff；不由 Ch27 的 RLHF 或 Ch61 的 scheduler 重复拥有。
- **Original Problem / Why Previous Designs Were Reasonable**：显式 3D control module、3D-conditioned I2V 与
  supervised 3D assets 能在 inference 时施加直接几何约束，便于解释和局部替换；在必须精确控制 camera/geometry
  且可承受额外 latency 时它们仍合理。纯 T2V foundation model 则保留高视觉多样性和简单 inference graph，
  但大 camera motion 下会暴露 object morphing、scene drift 和几何不一致。问题不是“旧架构错误”，而是当目标
  转为保持 3D consistency、又不愿在 serving path 增加 3D module 时，约束必须转移到 post-training。
- **Changed Constraint / Principle**：把结构约束从 inference module 移到 learned policy，会降低部署时的额外
  module cost，却把代价提前到 online video rollout 与 reward computation。第一性原则是：**当目标无法由单一
  token-level verifier 描述时，可用 analysis-by-synthesis 构造训练反馈，但 scorer identity、资源、失败模式和
  盲点也会进入 policy objective。**因此“无需 inference-time 3D module”不等于“系统没有 3D subsystem”。
- **Mechanism / Camera State and Policy Flow**：文本中的 push/pull/pan/move/orbit token 先映射为 camera
  extrinsics；planar homography 将 trajectory 投影成 optical flow，discrete noise transport 按 incoming density
  归一化，把 motion prior 写入 initial latent 而不增加 control network。Flow-GRPO-Fast 再把 deterministic
  flow-matching ODE 转为带随机性的 denoising trajectory；同一 prompt 采样 group，terminal video reward 归一化为
  group-relative advantage，并受 clipped ratio/reference KL 约束。Camera conditioner 拥有 trajectory/noise mapping，
  policy worker 拥有 latent/logprob/model version，不能把两者混成一个不可追溯的“video sample”。
- **Mechanism / Reward State Ownership**：每个生成 video 被 Depth Anything 3 lift 为 3DGS 并估计 camera；
  `S_meta` 用 Qwen3-VL 评分 novel meta-view，`S_recon=1-LPIPS` 比较原 video 与重渲染，`S_traj` 比较目标/估计
  trajectory，HPSv3 对前 K frames 提供 general-quality reward。v1 将前三项各限制在 `[0,1]`，3D total 为
  `[0,3]`，general reward 为 `[-1,1]`，直接相加。当前 code 将 3D/general reward 分离为服务端并异步请求：
  reward service 拥有 evaluator model/version、reconstruction state、timeout/error；trainer 拥有 aggregation、
  sample-to-score join、policy/reference/logprob 与 update。服务失败、重试或版本漂移若未进入 run identity，
  advantage 就不再可重放。
- **Mechanism / Periodic Objective Switching**：约 3,000 个纯文本 prompts 中约 500 个 high-entropy dynamic
  prompts 构成独立 subset。主阶段优化 `R_3D + R_gen`；每 100 steps 暂停 `R_3D`，只在 dynamic subset 上
  优化 `R_gen`。这不是简单 reward weight tuning，而是按 step 切换 **dataset distribution + active scorers +
  objective**。Training orchestrator 必须拥有 phase cursor、dataset version、enabled reward set、checkpoint 与
  abort/resume semantics；否则 restart 可能改变动态/几何更新比例。
- **Implementation / Evaluation Contract**：v1 使用 Wan2.1-T2V-1.3B/14B，分别 48/96 张 NVIDIA H200，
  832×480 video，48 parallel groups、group size 8。作者用 reconstruction PSNR/SSIM/LPIPS、VBench、MVCS、
  camera error、30 prompts × 25 人双盲 2AFC、30 randomized pairs × 20 人 metric validation、1K/2K/3K data
  scaling、121-frame 与 scene-complexity slices；reward/conditioning ablations 只在 Small variant。作者报告的
  headline 仅对该 backbone、prompt suite、reward stack、H200 scale 与 evaluation contract 成立。报告没有披露
  total training steps/time、optimizer/precision、完整 random seeds/variance、reward-service throughput/tail latency、
  failure/retry rate，或与显式 3D 方法 compute-matched 的端到端 train+serve cost。
- **Artifact / Revision Boundary**：当前 repository 暴露 train entry、camera-noise utilities、独立 reward servers、
  single/multi-node launch 和 prompt-only dataset；当前 HF artifact 有 `final` 与后增 `enhanced` 两套配置、合计
  6,476 rows，其中 final 为 2,468 train、42 test、500 dynamic。它不包含 generated videos、reward labels、
  human preferences 或 checkpoints。论文约 3,000+500 与当前 6,476-row artifact 不是同一 frozen dataset；
  current code 的默认与依赖也不能证明 v1 run 正是该 revision。
- **What the Evidence Proves**：作者在两个 Wan2.1 scales 上实现了 `camera-aware latent initialization → grouped
  video rollout → 3D/VLM/aesthetic composite reward → Flow-GRPO update`，component ablation 显示移除任一
  reward、noise wrapping 或 dynamic phase 会改变其 3D/general-quality trade-off；MVCS 与小规模 blinded human
  study 为 reconstruction metric 提供了额外而非完全独立的支持。长期信号是 reward pipeline 与 training
  runtime 必须共同设计，不是“RL 已把 video generator 变成通用物理 simulator”。
- **What It Does Not Prove / Threats to Validity**：训练 reward 与主要 evaluation 共享 3D reconstruction、
  trajectory 和 visual-quality ontology；Qwen3-VL meta-view、Depth Anything 3/3DGS 与 prompt taxonomy 的
  correlated blind spot 没有独立隔离。MVCS 和 human study 降低但没有消除这种 coupling，且样本数小、没有
  confidence interval/inter-rater disagreement。3DGS 假设更适合 static scene；真实 dynamics、contact、causality、
  embodied action outcome 和 very-long-horizon state 没有验证。更强 PSNR、121 frames 或 user preference 都不
  证明 autonomous-driving safety、真实 physical law、跨 backbone 泛化或 production economics。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：把 constraint 从 inference 移到 training
  保留了 serving graph，却需要完整 video rollouts、3D reconstruction、VLM/aesthetic scorers 和大规模 H200，
  并新增 reward-service straggler、metric gaming、static-collapse、objective oscillation、phase-resume drift、
  evaluator upgrade invalidation 与 corrupted sample/score joins。论文通过 trajectory term、general reward 和
  periodic dynamic phase 缓解 near-static reward hacking，但 ablation 只证明作者设置中的互补性。精确、可解释
  camera/3D control 或低训练预算仍可选择显式 module；可承受 serving cost但不能承受 online video RL 的场景，
  supervised/architectural branch 仍成立。
- **Evolution / ROADMAP / Final Disposition**：这是 `inference-time explicit 3D constraint → training-time
  analysis-by-synthesis reward → grouped high-dimensional rollout → heterogeneous reward services → periodic
  objective/data switching` 的 `Direct Evolution`；与 Ch62 是 `Layering / Dependency`。26/30；暂定
  `Refine — Existing Argument (Experimental)`，Ch29 为唯一 owner，Ch62 接 scorer-coupling handoff。
  Historical Books Gate 关闭，当前不修改 Books。

### Tuna-2: Pixel Embeddings Beat Vision Encoders for Multimodal Understanding and Generation — 24/30

- **Candidate / Week / Score / Source Family**：`TUNA2-PIXEL-SPACE-ENCODER-FREE-UMM`；W18；
  `TN 5 / SI 4 / PV 4 / SR 3 / PR 4 / L 4 = 24/30`。论文提出的长期问题是统一多模态模型应把
  understanding 与 generation 放在两个专用 visual representations 中，还是让同一主干直接从 raw pixels
  学习两类目标；headline 排名不是本项目的吸收对象。
- **Source Type / First-public / Revision History**：primary research paper arXiv:2604.24763；arXiv metadata
  明确 v1 于 2026-04-27 first-public、v2 于 2026-05-18 修订，故事件归 W18。直接来源为 arXiv abstract、
  v1/v2 full HTML、作者 project page 与 `facebookresearch/tuna-2` 当前官方 repository；related primary
  source 包括 repository 的 model/train configs、training guide 与 inference entry。访问日期 2026-08-10。
- **Access / Verification / Revision Integrity**：正文的 method、公式、training、main results、ablation、
  scaling curves、Related Work 与 Conclusion 已逐节阅读；paper 没有独立 Limitations/Threats section。
  immutable v1 PDF 在当前检索通道无法打开，且 v1 HTML 虽标注 `27 Apr 2026`，正文内部却显示
  `July 29, 2026`，并包含 GPT-5.4 / Claude Opus 4.7 evaluator；v2 HTML 的正文日期则为
  `April 28, 2026`。更关键的是 v1 写 Stage-1 为 70% captioning / 30% generation，v2 改为
  30% captioning / 70% generation，后者才与 7:3 generation-to-understanding ablation 一致。
  因而 first-public attribution 可信，但不能把当前 v1 HTML 的全部 evaluation 内容当作不可变 W18 snapshot；
  status 保留 `Disputed Revision Integrity`。
- **Original Problem / Why the Previous Design Was Reasonable**：早期 unified multimodal model 用 CLIP/SigLIP
  一类 representation encoder 服务 understanding，用 VAE/VQ-VAE latent 服务 generation。压缩 latent 降低
  pixel-space denoising 的维度与 token/FLOP 压力，预训练视觉 encoder 又提供 semantic prior、较快 early
  convergence 与有限数据下的 sample efficiency；在算力、数据或 latency 受限时，modular design 仍是合理
  旧方案。它的边界是两个 visual spaces 可能产生 alignment/connector cost，VAE compression 可能丢失细粒度
  signal，fixed encoder 的 resolution 与 inductive bias 也可能限制端到端共同优化。
- **Changed Constraint / Principle / Architecture Evolution**：论文按 `Tuna: VAE + representation encoder →
  Tuna-R: remove VAE, retain SigLIP 2 → Tuna-2: remove representation encoder, retain Conv/patch embedding`
  做 `Direct Evolution`。约束变化不是“encoder 失效”，而是 550M image-text pairs 与大规模 joint training
  让主干有机会自己承担 feature extraction。长期原则是：**inductive bias 可以用更低 data/compute 换更快收敛，
  monolithic learning 则用更高端到端训练成本换表示对多目标共同适配；哪条分支更好取决于 scale、objective、
  information bottleneck 与 deployment contract。**
- **Mechanism / Data and Control Flow**：raw image 由 patch size 16 的 patch embedding 转为 visual tokens，
  与 text tokens 一起进入 Qwen2.5-7B decoder；language head 优化 next-token objective，flow-matching head 在
  pixel space 以 rectified-flow linear path 构造 `x_t`，预测 clean image `x_theta`，再转换为 velocity
  `v_theta` 并用 v-loss 训练，inference 采用 Euler solver。Masking path 随机把 image patches 换成 learnable
  mask token：understanding 通过 partial observation 学 representation，generation 则在 masked/unmasked 区域
  预测 clean pixels。Stage-1 joint pretraining 后进入 full-model SFT；Tuna-R 还需额外 3k-step connector
  alignment，Tuna-2 没有这个 control phase。
- **State Ownership / System Contract**：dataset mixer 拥有 captioning/generation/text-only ratio、sample
  provenance 与 curriculum；patch/mask processor 拥有 resolution、patch order、mask draw 与 token-to-pixel
  mapping；decoder 拥有 shared hidden state，language/flow heads 分别拥有 objective-specific outputs；trainer
  拥有 objective weights、stage cursor、optimizer/scheduler、data cursor 与 checkpoint；inference runtime
  还需拥有 solver steps、guidance、seed、resolution bucket 与 variant identity。若只保存“7B checkpoint”而
  不保存这些 identities，就无法区分 representation improvement 来自 architecture、data mixture、masking、
  SFT 还是 evaluator drift。
- **Implementation Contract / Current Artifact Boundary**：paper v2 报告 Stage-1 300k steps、64 nodes、AdamW
  `1e-4`；masking 仅在最后 40% pretraining 启用，50% examples 被采样、mask ratio 为 0%～50%；SFT 为
  50k steps、`2e-5`，含 FineVision 13M conversations 与 OmniEdit 约 2M examples，输入 pad 至每 GPU
  16k tokens。GPU 型号、node 内卡数、precision、global/micro batch、训练 wall time、FLOPs、network、
  seeds/variance 与 SLO 均 `Not Disclosed`。当前 repository 提供 Conv2d-patchify/JiT variants、FSDP、BF16、
  data streams 与 inference code，但 README 明确 production weights 尚未发布；其 50/20/20/10 T2I/edit/MMU/text
  finetuning recipe、mask defaults 与 `2e-5` 也不是 paper Stage-1 frozen recipe，因此 code 只验证实现形状，
  不能复现论文结果。
- **Evaluation / Baselines / Ablations / Sensitivity**：作者比较 Tuna、Tuna-R、Tuna-2 与多类 understanding-only、
  generation-only、composite/native UMM baselines；覆盖九个 VQA、V*/CountBench/VisuLogic pixel-centric tests、
  GenEval、DPG-Bench、ImgEdit、ImageNet reconstruction，以及 attention visualization。1.5K prompts × 每模型
  4 images 的质量/多样性比较使用两个 model judges，但 judge prompt/version、sampling、重复次数、
  confidence interval 与 disagreement 未完整披露。1.5B controlled masking ablation 先训练 50k steps，再以
  with/without masking 各训练 50k；data-mixture ablation 比较 generation/understanding ratios；scale curve 比较
  Tuna-R 与 Tuna-2 的 training dynamics。缺少 matched total train compute、matched inference latency/memory、
  multiple seeds、data contamination audit 与 encoder-size/patch-resolution sensitivity。
- **What the Evidence Proves**：在作者公开 contract 下，移除 VAE 后的两个 pixel-space variants 在细粒度
  understanding 上优于 Tuna；Tuna-R 在 early training 更强，Tuna-2 随 scale 追上并在多数 understanding
  tests 超过 Tuna-R；generation training 中 Tuna-R 持续更强，SFT 后差距缩小，editing 也仍由 encoder-based
  variants 略占优势。controlled masking ablation 支持 masking 对作者四个指标有小幅增益。这证明
  encoder-free pixel-space UMM 是可行 design branch，并揭示 semantic prior 与 end-to-end scale 的 trade-off。
- **What It Does Not Prove / Threats to Validity**：标题中的 “Beat” 不能外推为所有任务、模型规模、数据量、
  compute budget 或生产系统。作者的结果没有隔离更多 raw-pixel tokens/compute、data mixture 与 SFT 的影响；
  attention map 只是 qualitative visualization，不等于因果 representation proof；model-judge preference 不是
  human perception 或 deployment value；没有 production weights 与 immutable v1 evidence，也无法独立复现
  historical numbers。64 nodes 但 hardware/precision/batch 不公开，因而不能比较 training economics；论文也
  没有评估 high-resolution/long-video token explosion、serving latency、memory 或 energy。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：monolithic pixel path 删除 encoder/VAE 与
  connector versioning，却把高维 input、denoising、representation learning 和 two-objective interference 都压入
  shared decoder，新增 pixel-token expansion、objective-gradient conflict、mask curriculum sensitivity、
  generation/understanding mixture drift、solver/runtime cost 与单体升级耦合。Modular encoder branch 在低算力、
  少数据、快速冷启动、独立组件升级或更强 generation prior 时继续成立；pixel-space branch 更适合能承担
  大规模 joint training、且 fine-grained signal 比 modular isolation 更重要的 workload。二者是共存分支，
  不是新方案对旧方案的否定。
- **ROADMAP / Target and Adjacent Chapters / Existing Coverage**：唯一长期 owner 暂定 Ch5，因为该章已定义
  representation、information retention 与 inductive bias，却尚未用 multimodal architecture 展示“预训练 bias
  vs end-to-end scale”的具体系统分支；Ch4、Ch6 已完整核对相邻 optimization/architecture 边界。Ch23 已有
  data-mixture multi-objective contract，Ch24 已有 objective/parameterization/compute trajectory，因此只接短
  handoff，不重复机制；不存在 Ch14/21/45 的主 owner。Ch62 只在未来需要 evaluator-boundary handoff。
- **Final Disposition / Changed Files / Open Questions**：24/30；`Emerging / Experimental — Disputed Revision
  Integrity`。潜在 Books 决策是 `Refine — Existing Argument` / Ch5，但 immutable v1 snapshot、paper-run
  artifact 与 production weights 未闭合，Historical Books Gate 也关闭，所以本检查点只更新 W18、年度索引、
  Learning State 与当日 Daily。待验证：v1 PDF 是否能确认 4 月版本的真实 data ratio/evaluation；相同 train
  FLOPs 与 token budget 下 encoder prior 是否仍被反转；公开 weights 能否复现 pixel-centric gain 及
  generation/editing trade-off。

### A Survey on LLM-based Conversational User Simulation — 23/30

- **Candidate / Week / Score / Source Family**：`CONVERSATIONAL-USER-SIMULATION-SURVEY`；W18；
  `TN 3 / SI 4 / PV 4 / SR 4 / PR 4 / L 4 = 23/30`。它是 taxonomy/synthesis 候选，研究问题不是
  “怎样造出一个更强模型”，而是 conversational user simulator 究竟模拟谁、模拟哪种 interaction、以何种
  conditioning/training method 生成行为，以及如何判断 synthetic behavior 与目标用户分布一致。
- **Source Type / First-public / Revision History**：primary survey / EACL 2026 long paper；arXiv:2604.24977
  只有 v1，metadata 显示 2026-04-27 20:22 UTC first-public，comments 说明稿件 2025 年 8 月投稿，related
  DOI 为 `10.18653/v1/2026.eacl-long.200`。历史事件按公开可访问的 arXiv/EACL 日期归 W18，不把投稿月
  倒写成 2025 event。访问日期 2026-08-10。
- **Direct Primary Sources / Access / Full-read Coverage**：已读 arXiv metadata 与 1,001-line v1 HTML 全文，
  包括 Abstract、Introduction、Problem Definition、Who/What/How 三层 taxonomy、Evaluation、Datasets、
  Applications、Challenges、Conclusion、Limitations、Ethical Considerations，以及扩展 Appendix A～H。
  论文是 survey，没有配套 simulator code、model checkpoint、统一 dataset 或可复现实验 artifact；因此
  Implementation、hardware、precision、batch、concurrency、SLO、ablation、sensitivity 与 overhead 均为
  `Not Applicable / Not Disclosed`，不能用被引用论文的局部设置替它补全。
- **Original Problem / Why Previous Designs Were Reasonable**：传统 user simulation 常用 preference model、
  collaborative filtering、click model 或 task-specific dialogue policy。它们只覆盖较窄 domain，却能明确
  state/action space、训练数据与可校准 outcome；在 high-stakes、稀疏数据或可解释行为 contract 下仍合理。
  LLM 降低了生成丰富、多轮、跨领域 interaction 的门槛，但也把 population identity、persona fidelity、
  history conditioning、prompt/model bias 与 evaluator correlation 隐藏在自然语言和 checkpoint 中。
- **Changed Constraint / Taxonomy / Evolution Relationship**：survey 用三个正交问题组织演进。`Who` 从
  general population 到 persona、role play、individual user 与 hybrid；`What` 从 Human-AI 扩展到
  Human-Human、AI-AI、Many-Human-AI 与 hybrid；`How` 从 prompt-based 扩展到 always-on/adaptive/
  goal-state-driven RAG、full/PEFT/interactive fine-tuning、RL/DPO 与 hybrid stacks。它与本书关系主要是
  `Principle Reuse / Layering`：simulator identity 必须同时声明 target granularity、interaction topology 与
  conditioning mechanism，而不是把所有 synthetic conversation 视为同一 distribution。
- **Mechanism / State Ownership / Control and Data Flow**：论文形式化 conversation
  `C=(c_1,...,c_T)` 与 next utterance distribution `P(u_t | C_{t-1}, Psi_p)`。工程化后，dataset/consent
  owner 管原始 traces 与 population sampling；persona/profile store 管 `Psi_p` 及时间版本；context/memory
  runtime 管可见 history、retrieval 与 drift；simulator checkpoint/prompt/retriever/policy 管行为生成；environment
  管 observation、feedback、turn budget、dropout 与 termination；evaluator 管 human/model judge、rubric、
  calibration 与 uncertainty。数据流应为 `authorized user evidence -> versioned profile/history -> simulator
  policy -> interaction trace -> independent evaluator -> slice/calibration report`，不能让 simulator 自己的
  自述成为 fidelity 证明。
- **Techniques / Implementation Boundary**：prompting 最便宜、最可替换，但 persona 可能只是一段软约束；
  RAG 可引入 user/profile history，却新增 retrieval miss、staleness、ACL 与 provenance；fine-tuning 提供更稳定
  behavior，却把 consented traces 固化进 weights 并增加 deletion/migration 成本；RL/DPO 可优化 long-horizon
  goal、clarification 与 sparse feedback，却依赖 reward/user model，容易把理想化 simulator 的偏差放大。
  Hybrid stack 可以组合这些能力，也让 checkpoint、prompt、retriever、memory、reward 与 policy revisions 都
  进入 subject identity。survey 没有比较这些方案的 matched compute、data、privacy 或 deployment contract。
- **Evaluation Contract / Baselines / Evidence**：survey 汇总 n-gram/F1/perplexity、task success、human
  evaluation、LLM-as-a-Judge 与 trustworthy/causal evaluation。Human judgment 被视为最接近目标语境的参照，
  但昂贵且不一致；model judge 可扩展，却对 prompt、model family、position 与 rubric 敏感，需要 symmetric
  prompting、ensemble、reason-before-score 和对 human labels 的 meta-evaluation。本文没有统一 benchmark、
  baseline table、controlled ablation、effect size、confidence interval 或 cross-method reproduction；因此 23 分
  来自 taxonomy 与 system relevance，不来自新实验性能。
- **What the Evidence Proves**：文献版图支持至少五类 target granularity、五类 interaction objective 与五类
  implementation family 的存在，也支持 long conversation 中 persona drift、unrealistic cooperativeness、错误
  累积、task-focus loss，以及 diversity、bias/toxicity、sparse/delayed feedback、privacy、temporal evolution 与
  consistency-adaptability trade-off 是反复出现的开放问题。它还支持 individual simulation 需要完整 history，
  user state 会随时间变化，synthetic feedback 与真实用户反馈不能默认等价。
- **What It Does Not Prove / Limitations / Threats**：survey 的 “high-fidelity” 描述是对领域进展的综合性判断，
  不是本文用统一实验验证的结论。作者明确说明 taxonomy 可能不适配 hybrid/domain-specific systems，且没有
  对方法做全面 benchmarking。引用研究跨任务、数据、模型和 judge，不能横向拼成 rank；LLM 生成 coherent
  persona 不证明 demographic、individual 或 causal fidelity；同一 model family 同时充当 simulator、training
  data generator 与 judge 会形成 closed measurement loop。真实用户 dropout、disengagement、偏好漂移、稀疏
  feedback 和少数群体行为若未进入 environment，更多 simulated turns 只会更稳定地重放错误分布。
- **Trade-offs / New Failure Modes / Previous Designs Still Apply**：更细 persona/history conditioning 提高
  apparent specificity，同时扩大 re-identification、consent、retention、delete、stereotype 与 profile-staleness
  风险；更长期 interaction 提供 recovery/adaptation evidence，也增加 state drift、error accumulation 与 evaluation
  cost；更复杂 hybrid stack 提高可塑性，却降低 attribution 和 reproducibility。Rule-based/stochastic users、
  replay logs、small task-specific models、Wizard-of-Oz 与真实用户 shadow/canary 仍分别适用于明确 state space、
  deterministic regression、历史分布回放、高风险交互和最终外部有效性验证。LLM simulator 是 distribution
  generator，不是 ground truth replacement。
- **Ethics / Governance Boundary**：public-figure role play 可能制造 misinformation、reputation harm 与 likeness/
  consent 问题；demographic persona 容易固化 stereotype，并让模型看似代表真实 lived experience；synthetic
  dataset 需要 provenance、authenticity 与 downstream-use 标记。Individual history 必须绑定授权、最小化、
  retention、删除传播与审计，不能因为数据已进入 RAG、memory 或 fine-tuning pipeline 就失去用户权利。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：唯一 owner 为 Ch62。Ch61、Ch62、
  Ch63 已核对：Ch62 的 EvalSpec 已绑定 eligible population、failure taxonomy、subject identity、dataset/
  environment/scorer version、slices/uncertainty，并明确 simulator 只是 executor/scorer implementation、model judge
  必须校准；因此 survey 没有新增长期 mechanism。Ch71 已拥有 current history/context identity，Ch72 拥有 RAG
  authorization/freshness，Ch73 拥有 persisted memory、provenance、drift/delete，Ch74/77 拥有 environment action
  与 durable workflow；这些章节只形成 adjacency，不重复写 taxonomy。隐私与 consent 继续由 Ch68 承接。
- **Final Disposition / Changed Files / Open Questions**：`No Change — Already Covered`。本候选新增的是一个
  审计 checklist 和跨文献 terminology map，不改变既有设计结论，也没有足够独立 evidence 支持 Books 新段落。
  本次只更新 W18 Weekly、年度索引、Learning State 与 2026-08-10 Daily；Historical Books Gate 保持关闭。
  待验证问题是：怎样用真实、consented population slices 校准 simulator fidelity；如何分离 simulator/model-judge
  同源误差；如何在用户漂移、dropout 与 sparse feedback 下报告 uncertainty，而不是只报告 dialogue quality。

### Perceval: Perception-centric Process Reward Models — 26/30

- **Candidate / Week / Score / Source Family**：`PERCEVAL-VLM-PROCESS-REWARD`；W18；
  `TN 5 / SI 4 / PV 4 / SR 4 / PR 5 / L 4 = 26/30`。核心问题是 outcome-level RLVR 把同一
  sequence advantage 复制给所有 tokens，无法定位 visual reasoning 中哪一个 object/attribute/spatial claim
  首先失真；论文尝试把外部 VLM verifier 的 span judgment 编译为 token-level credit。
- **Source Type / First-public / Revision / Access**：CVPR 2026 primary paper；arXiv:2604.24583 只有 v1，
  2026-04-27 15:08 UTC first-public，journal reference 为 CVPR 2026 pp. 33099–33109。已读 arXiv metadata、
  397-line v1 HTML 全文（Introduction、Preliminary、公式、Method、全部 Experiment/Analysis、Related Work、
  Conclusion）与当前 `RUCAIBox/Perceval` official repository、README、reward-function path、training scripts/
  config surface 和 released 3B PRM/policy checkpoint links。访问日期 2026-08-10。paper 没有独立 Limitations/
  Threats section；current repository 只有 8 commits，且晚于事件窗口，故可验证实现形状，不能倒写为 W18
  已公开 artifact 状态。
- **Original Problem / Why Previous Designs Were Reasonable**：sequence-level GRPO 用 group outcome 形成
  `A_i`，再让 response 中所有有效 tokens 共享同一方向；它实现简单、无需 step annotations，并保留最终
  correctness 的清晰 objective，在数学答案、代码 tests 或 reasoning step 无法独立判定时仍合理。其边界是
  correct final answer 可以含错误 rationale，incorrect answer 也可能含正确 perception；相同 advantage 会产生
  credit smearing。早期 tool-augmented visual search/zoom/crop 则把 perception error 交给外部 action 修复，
  但增加 tool selection、latency 与 environment dependency。
- **Changed Constraint / Direct Evolution**：Perceval 利用 visual claim 可直接和输入 image 对齐这一局部
  可验证性，把 `outcome-only scalar -> process verifier -> span mask -> token-adjusted advantage` 作为 Ch29 的
  `Direct Evolution`。它没有替代 sequence reward：group outcome 仍是 base `A_i`，PRM 只对 perception-tagged
  data 和被标记 spans 施加修正；general reasoning data 回退到 direct GRPO。长期原则是局部 verifier 应作为
  bounded residual signal，而不是悄悄成为新的绝对 ground truth。
- **Mechanism / Formula / Control Flow**：对 image `v`、query `q` 与 rollout `o`，Perceval 先在 `<think>` 中
  逐 claim grounding，再在 `<answer>` 返回 exact erroneous substrings。parser 用 exact string match 将第 `k`
  个 substring 定位到 token span `[j_k,l_k]`，并形成 binary mask `m_{i,t}`。原 group advantage 按
  `A'_{i,t}=A_i-alpha*m_{i,t}*|A_i|` 调整：正 advantage 的错误 token 被 downweight，负 advantage 的错误 token
  更负；未标记 token 保留原 `A_i`。新 mask 被代回 clipped GRPO objective。Inference 端则在最早 flagged
  span 前截断，直接 regenerate，或加入 PRM feedback 后 regenerate，直到 PRM 接受或达到 iteration cap `k`。
- **State Ownership / Data Flow**：rollout policy 拥有 prompt/image、response tokens、policy/logprob identity；
  outcome judge 拥有 sequence reward；Perceval service 拥有 verifier checkpoint/prompt、structured response 与
  endpoint version；parser/tokenizer 拥有 substring-to-token alignment 和 mask；trainer 拥有 group、`alpha`、
  clipping、KL、data-type gate 与 optimizer state；inference controller 拥有 accepted prefix、first-error offset、
  retry count、seed/sampling 与 stop reason。current code 把 judge、PRM 与 trainer 分为三个 endpoints/processes，
  并在 vendored VERL 中加入 `trm` advantage estimator、mask construction 与 threaded reward manager。任何一项
  identity 漂移都会改变“哪个 token 被罚”的训练语义。
- **Training Data / Annotation / Artifact Contract**：3B/7B PRM 与 policy 均以 Qwen2.5-VL 为 backbone。
  Perceval SFT queries 来自 visual-search/perception-heavy data，混入 math/general understanding；Qwen2.5-VL-7B
  等 open VLM 生成 rollout，Gemini-2.5-Pro 等 strong model 自动产生 structured annotations，再做 SFT。
  paper 说明 DeepEyes 与 SophiaVL-R1 data 各 rollout 三次，RL data 主要来自 DeepEyes；current repo 公开
  3B PRM/policy weights、schema、training side 和 configurable OpenAI-compatible PRM endpoint，但 PRM data-
  generation pipeline 仍主要由 paper 描述。paper 未披露 training steps、global/micro batch、learning rate、
  optimizer、precision、GPU 型号、wall time、seeds/variance 或 annotation acceptance rate。current README
  示例用 3B trainer 4 GPUs、7B 8 GPUs，并另起 judge/PRM GPU，但 hardware 类型与 paper-run identity 未对齐。
- **Evaluation Setup / Baselines / Ablations / Sensitivity**：作者在 V*、MME-RealWorld-Lite、BLINK、MMStar、
  RealWorldQA、MathVista、MATH-Vision 与 ChartQA 上比较 3B/7B Qwen2.5-VL、direct GRPO、Perceval training
  及十二类公开 VLM/RL baselines。统一 pipeline 使用 greedy decoding、same prompt、official answer extraction，
  先 exact match，再用 GPT-4o-mini 处理格式差异；ChartQA 用 relaxed accuracy。最有因果可比性的是同 backbone
  `GRPO vs Ours`；跨论文 baselines 的 training data、tools 与 compute 不匹配。Test-time scaling 仅在 3B policy
  的 V*/BLINK 上比较 majority vote 与两种 truncate loops，`k=4/8/16`；`alpha` sensitivity 比较
  `0/0.03/0.1/0.3`，呈非单调，0.3 伤害多项结果。没有 PRM false-positive/false-negative、span IoU、
  human-grounded calibration、multiple seeds/CI、PRM-call latency/throughput 或 total test-time compute matching。
- **What the Evidence Proves**：在作者 data、Qwen2.5-VL 3B/7B、greedy evaluation 与 benchmarks 下，向
  direct GRPO 加入 perception span penalties 会改变 policy 并在多数 reported metrics 上获得小到中等增益；
  `alpha` ablation 支持 penalty 过强会 collateral-punish span 内无害 function words。受限 test-time experiments
  也支持 verifier-guided truncate/regenerate 是一条不同于 independent majority vote 的 compute branch。
  current code 与 checkpoint 证明核心 mask/endpoint contract 已开放，而不只是 proposal。
- **What It Does Not Prove / Claim Boundary**：paper 没有独立测量 Perceval 自身是否正确定位 hallucination，
  因此无法把 downstream gain 归因于准确 token grounding而不是额外 model prior/data signal。作者把 PRM 自己
  标记的 hallucination rate 先下降后 plateau 解释为“避免 significant reward hacking”，这是同一 evaluator
  自证，不能排除 policy 学会躲避 verifier；需要 independent human/verifier cross-check。Math/chart gain 只显示
  correlated transfer，不证明 perception improvement 是唯一因果路径。一个 qualitative CoT 更详细也不证明
  内部 reasoning faithful。跨 baseline 排名不具 compute/data/tool equivalence，且 paper 没有 production SLO。
- **Trade-offs / New Failure Modes / Previous Designs Still Apply**：更细 credit 降低 sequence-level smearing，
  但新增 PRM serving cost、annotation bias、false-positive penalty、false-negative reward loophole、exact-substring/
  tokenizer mismatch、overlapping spans、first-error truncation、retry latency 与 verifier-policy collusion。整段
  substring penalty 会惩罚语法 token，论文的 0.3 regression 已显示该边界。Rule-based step verifier 在可形式化
  domain 更可靠；sequence-only GRPO 在 step 不可判定、PRM 不可信或 serving 太贵时继续成立；external visual
  tools 在需要可观察 zoom/crop evidence 时仍有优势；offline rejection/SFT 则适合不愿在线持有 PRM service 的
  系统。新旧方案是按可验证粒度与成本分支共存，不是 process reward 普遍覆盖 outcome reward。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：唯一 owner 为 Ch29；Ch28、Ch29、Ch30
  已完整核对。Ch29 已指出 sequence reward 到 tokens 的 credit problem，并用一句话保留 process verifier
  方向，但尚未解释“sequence advantage + localized residual mask”的机制、状态与反例，因此本候选是真正的
  `Refine — Existing Argument`，不是重复摘要。Ch28 只接 terminal reward/token credit handoff，Ch30 的 offline
  pair route 不重复。Ch62 已读并拥有 verifier/scorer calibration、independent evidence 与 reward-hacking 边界，
  只接短 handoff；不把 training PRM 的权威上移为 product Evaluation。
- **Final Disposition / Changed Files / Open Questions**：`Refine — Existing Argument (Experimental)` / Ch29，
  但 Historical Books Gate 关闭，本轮不修改 Books。只更新 W18、年度索引、Learning State 与当日 Daily。
  待验证：PRM 的 human-labeled span precision/recall 与跨 checkpoint transfer；独立 scorer 下 reward-hacking
  曲线；与 matched total training/inference compute 的 sequence-only、rule-step、tool-grounded baselines；
  exact-match parser 在 tokenizer、Unicode、重复 substring 与 paraphrase 下的 failure rate。

### Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models — 26/30

- **Candidate / Week / Score / Source Family**：`TIDE-CROSS-ARCH-DLLM-DISTILLATION`；W18；
  `5/4/4/4/5/4 = 26/30`。Source type 为 primary research paper + official repository/model/data artifacts。
- **First-public Date / Revision History / Direct Sources**：arXiv:2604.26951 仅有 v1，于
  2026-04-29 17:59 UTC first-public，事件归 W18。已完整阅读 v1 的 Abstract、Introduction、Related Work、
  Method、全部公式、Experiments、Ablations、Efficiency、Conclusion、Appendix B～E 与案例；并联合核对
  `PKU-YuanGroup/TIDE` 官方仓库、README、两条训练 pipeline、公开 checkpoint 与 data path。当前仓库的
  convenience defaults 与 paper 10-epoch contract 不完全相同，因此只用于验证实现接口和 artifact 当前可用性，
  不倒写为 W18 frozen run。Access and Verification Status 为 `Primary Paper Complete; Current Artifact Verified`。
- **Original Problem / Why the Previous Design Was Reasonable**：传统 distillation 通常假设 teacher/student
  使用相容 tokenizer、相近 architecture 与同步位置语义，因此可以直接比较 full-vocabulary logits；或干脆让
  小模型独立 SFT，以避免 teacher bias、双模型训练成本与 alignment error。对 autoregressive model，这一旧
  contract 很合理：每个 token position 都有明确的左到右条件上下文，teacher probability 可被稳定解释。
  但 block diffusion student 在不同 mask timestep 下看到的上下文不相同，teacher reliability 随 masking severity
  变化；teacher 若使用不同 attention pattern、capacity 或 tokenizer，position-level KL 也不再有天然公共坐标系。
- **Changed Constraint / Evolution Relationship**：workload 从 same-family AR distillation 变化为
  heterogeneous diffusion-to-diffusion transfer：student 是 0.6B Qwen3-BD3LM block-diffusion model，teacher
  分别是 LLaDA2.0-mini 16.26B MoE（不同 tokenizer）与 WeDLM-8B-Instruct 8.19B dense model（shared tokenizer
  family）。这是 `Direct Evolution`：目标不是否定 aligned-logit distillation，而是在 timestep reliability、
  conditional context 与 vocabulary identity 不一致时重新定义 transfer interface。same-tokenizer/same-architecture
  路径在接口干净、计算预算受限时仍然优先；independent SFT 在 teacher 偏差不可接受或 artifact 不兼容时仍成立。
- **Mechanism — TIDAL**：clean sequence 先按 block-diffusion contract 采样 mask/timestep。训练早期与高 mask
  ratio 下 teacher signal 不可靠，因此论文把 distillation target 设为 detached student/teacher probability 的
  interpolation，并使用 `lambda_t = lambda_train * (1 - t)`；`lambda_train` 随 global training progress 由
  0.1 cosine 增至 0.9。这样 late training、low-noise position 更信 teacher，early/high-noise position 更保留
  student/self target。可选中段 timestep weighting（sigma 0.15）改变的是 loss sampling emphasis，不是模型
  runtime。该 schedule 引入新的 owner：global progress、noise timestep 与 teacher-trust policy 必须共同版本化。
- **Mechanism — Complementary Demonstration / CompDemo**：对 masked positions 随机拆成互补集合 A/B；
  第一次 teacher forward 暴露 A 并预测 B，第二次暴露 B 并预测 A，再合并 logits。它用额外 clean context 缓解
  heavy masking 下 teacher uncertainty，但不是免费 augmentation：frozen teacher 需要近似双 pass，论文报告
  training time 约增加 50%，还必须保持 partition seed、mask identity 与 merged-logit position 一致。
- **Mechanism — Cross-tokenizer CALM / Reverse CALM**：不同 tokenizer 时，paper 先按 UTF-8 byte span 把
  teacher/student tokenization 对齐成最小公共 chunk，并排除不兼容 special template；不构造共同 vocabulary，
  而是计算同一 chunk 的 scalar sequence probability。forward CALM 的 BCE gradient 含 `p_t / p_s`，student
  probability 很小时可能爆炸；Reverse CALM 交换方向并对 teacher log-odds clipping，使梯度由 bounded teacher
  confidence 控制，同时过滤 teacher/student 双低置信 chunk。它等价于更 mode-seeking 的 Bernoulli reverse-KL
  选择：稳定性提高，但可能丢失 teacher 的低概率多样性。Appendix 明确 TIDAL 与 Reverse CALM 不应直接叠加，
  因 late schedule 会削弱 reverse self-selection；这是两条 pipeline，而非组件越多越好的单一路线。
- **State Ownership / Control Flow / Data Flow**：dataset/text owner 保存原始样本与 data mixture；student 与
  teacher 各自拥有 tokenizer、template、checkpoint、precision 与 max length；alignment layer 拥有 byte/chunk
  map、special-token exclusion 与 probability aggregation；noise process 拥有 block/mask/timestep seed；distillation
  controller 拥有 objective direction、temperature、`lambda_train/t` 与 CompDemo ratio；optimizer 只更新 student；
  evaluator 另行拥有 sampler、block size、step budget 与 benchmark prompt。数据流为 clean text → 两套
  tokenization/masking → shared-logit path 或 byte-chunk path → CE + distillation objective → student update；不得把
  current repository defaults、paper training config 与 evaluation sampler 合并成一个无版本 recipe。
- **Implementation / Training Contract**：paper 使用 BF16、DDP、learning rate 5e-5、10 epochs；student
  sequence length 512、block size 32，teacher max length 为 cross-tokenizer 1024、shared-tokenizer 768，temperature
  2.0，CompDemo ratio 0.5。数据来自 Tulu-3 SFT、SmolTalk 与 OpenCoder SFT Stage 1/2 Python。论文未披露
  完整训练 GPU 型号/总 GPU-hours、seed variance、optimizer-state memory 与 network topology；official README 的
  quick-start 8-GPU path 和较短 default epochs 是 current convenience recipe，不能替代 paper contract。
- **Evaluation Contract / Baselines / Ablations / Sensitivity**：八项 benchmark 为 GSM8K、MATH、BBH、
  MMLU-Pro、HellaSwag、MMLU、HumanEval、MBPP；block size 32、CFG 0，MMLU/HellaSwag 用 3 steps，其余最多
  256 steps，batch 32～128。reported main average 从 undistilled BD3LM 32.67 到 cross-tokenizer best 34.20，
  shared-tokenizer best 33.55；这些只是作者配置下的 aggregate。三 epoch shared-path ablation 中 full 33.14、
  baseline 33.06、去 timestep 32.88、去 CompDemo 32.97，多个单项 benchmark 反而回归，故不能写成每个组件
  都稳定正贡献。未报告多 seed、confidence interval、teacher-quality-matched 或 total-compute-matched sensitivity。
- **Inference Efficiency Contract**：唯一受控表是单张 H100 80 GB、BF16、生成 256 tokens、五次取最佳。
  distilled student 为 1.4 GB、6.25 s、41 tok/s，undistilled student 为 1.4 GB、6.08 s、42.1 tok/s；same-size
  AR Qwen3-0.6B 为 1.2 GB、4.99 s、51.3 tok/s。它说明 distillation 没有改变 student runtime class，且在该
  workload 下 AR baseline 仍更快；不能用 HumanEval 48.78/49.39 对 32.30 的单项差异宣称 diffusion architecture
  普遍更优。paper 评估实际还对每个 benchmark 随机取 50 examples，未覆盖生产 concurrency、TTFT/TPOT、
  tail latency、长上下文与 serving SLO。
- **What the Evidence Proves**：在两条公开 pipeline、一个 0.6B block-diffusion student 与指定训练/eval
  contract 下，timestep-aware trust、complementary context 和 byte-level chunk objective 可以让跨 architecture/
  tokenizer distillation 获得小幅 aggregate improvement；official artifacts 也使接口形状可检查。这为
  “distillation 首先是 representation/condition/evidence interface 设计”提供新机制案例。
- **What It Does Not Prove / Limitations / Threats to Validity**：论文不证明 dLLM 普遍优于 AR、不证明
  16B teacher 的收益超过额外 teacher compute，也未分离 architecture、capacity、tokenizer 与 data mixture 的
  causal effect。只审计 0.6B student、block size 32、sequence length 512 与两位 teacher；未覆盖 continuous-state/
  encoder diffusion、multi-teacher、long context 或 production serving。byte equality 不是 semantic equality，
  长 chunk、Unicode、normalization 与 template exclusion 可能制造 alignment noise；Reverse CALM 的 mode seeking
  还会抑制低概率知识。HumanEval 的“parallel/global coherence”解释是作者推断，没有 architecture-matched
  causal test。无 variance、独立 reproduction 和 full compute accounting。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：TIDAL 降低 noisy-teacher overwrite，
  但引入 schedule/timestep miscalibration；CompDemo 增加上下文，代价是约 50% train time、双 pass 和 merge
  identity；Reverse CALM 抑制 exploding gradient，却可能 mode collapse/under-cover；byte alignment 跨 tokenizer，
  但可能把 surface equivalence 误作 knowledge equivalence。共享 tokenizer/direct KL 在 vocabulary 与 conditional
  context 一致时仍更简单；独立 SFT 在 teacher provenance、license、bias 或 compute 不可接受时仍合理。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：唯一 owner 为 Ch25。Ch24、Ch25、
  Ch26 与 Ch30、Ch40 已核对：Ch25 已有 teacher-capacity gap、context distillation、full-vocabulary soft target、
  KL direction/token reduction 与 teacher snapshot ownership，但缺少 diffusion timestep reliability、conditional
  context reconstruction 与 cross-tokenizer chunk objective，因此属于 `Refine — Existing Argument`，不是新增
  孤立章节。Ch24/26 不重复训练接口；Ch30 只接 objective-direction handoff；Ch40 继续拥有 autoregressive decode，
  未来若写入只需短 handoff 说明非 AR generation contract，而不把 dLLM benchmark 塞入推理正文。
- **Final Disposition / Changed Files / Open Questions**：`Refine — Existing Argument (Experimental)` / Ch25。
  Historical Books Gate 关闭，本轮不修改 Books；只更新 W18、年度索引、Learning State 与 2026-08-10 Daily。
  待验证：multi-seed/compute-matched ablation；长上下文与 continuous diffusion transfer；chunk alignment 在 Unicode/
  normalization/template drift 下的 error rate；TIDAL schedule calibration；Reverse CALM 的 diversity loss；以及
  相同 data、parameter、decoding budget 下 AR/dLLM quality-latency frontier。

### Step-level Optimization for Efficient Computer-use Agents — 28/30

- **Candidate / Week / Score / Source Family**：`STEPWISE-GUI-EVENT-CASCADE`；W18；
  `5/5/5/4/5/4 = 28/30`。Source type 为 primary paper、primary PDF 与 author detector artifacts。
- **First-public Date / Revision History / Direct Sources**：arXiv:2604.27151 仅有 v1，于
  2026-04-29 19:59 UTC first-public。已读完 14-page PDF 与 373-line HTML 的 Abstract、Introduction、Related
  Work、Failure Analysis、Method、Experiments、Ablations、Conclusion、benchmark/training appendices、detector
  examples 和三组完整 prompts；HTML 的 Appendix D 内容转换缺失，已由 PDF pages 12～14 补齐。author-linked
  StepWise Hugging Face collection 在事件前已发布 8 个 ModernBERT detector weights，但 model cards 为空，
  未发现公开 runtime/control-loop code 或 frozen evaluation traces。Access and Verification Status 为
  `Full Paper Complete; Weights Verified; Runtime Artifact Not Disclosed`。
- **Original Problem / Why the Previous Design Was Reasonable**：query-level router 只在任务开始时选择一个
  model，或 GUI Agent 每一步都调用最强 model。前者在单请求 answer generation 中合理，因为 difficulty 可在
  input 侧估计；后者在 long-horizon action 中合理，因为每个 step 都可能改变外部 state，用同一强 policy 能
  避免 handoff mismatch。它们的边界是 GUI trajectory 的 difficulty 随状态变化：routine steps 占用昂贵 compute，
  而一旦早期语义漂移，后续每步即使局部合理也无法挽回；只在 terminal outcome 检查又太晚。
- **Changed Constraint / Direct Evolution**：调度对象从 `request → model` 变成
  `trajectory state/event → next-step policy or verifier`：

  ```text
  query-level one-shot routing
  → always-large per-step policy
  → periodic sparse verification
  → event-triggered step-level recovery + milestone verification
  ```

  后者不否定前者。短任务、风险均匀、handoff 昂贵或 monitor drift 严重时，单次 route/always-large 仍更简单；
  deterministic workflow 若能够直接验证 state transition，也比 learned monitor 更可靠。
- **Mechanism / Formula**：每一步保存最近 `K` 个 rationale/action 的 textual window
  `w_t={(r,a)_{t-K+1},...,(r,a)_t}`。149M ModernBERT Stuck Monitor 计算
  `p_stuck=S_phi(w_t)`；超过 `theta_s` 时只把下一步 action generation 路由给 large policy，并把 small policy
  history 重新序列化到 large-model response format。Milestone Monitor 额外读取 task `u`，计算
  `p_mile=M_psi(u,w_t)`；触发后从上次已验证 milestone `tau_t` 到当前 step 组装 task、rationale/action segment、
  before/after screenshots，由 stronger verifier 分别检查 progress validity 与 intent consistency。通过时提交
  `tau←t` 并保存 screenshot；失败时触发 escalation。
- **Training / Label Contract**：detector data 来自 300 GUI-Agent trajectories 与 overlapping windows；
  GPT-5.2 对每条 trajectory 独立标注五次，三次及以上命中为 positive、零次为 negative、一次或两次被丢弃。
  stuck prompt 只定义 repetition/error loop/no progress；milestone prompt 要求 milestone 间至少 3 steps、偏好高层
  progress；verification prompt 主要依赖 before/after screenshots。两个 detector 用 AdamW、learning rate 5e-5、
  5 epochs、batch 8、max length 2048、BF16、inverse-frequency class weighting 与 80/20 split。paper 没说明
  split 是否按 trajectory 分组；由于 windows overlap，若随机按 window split，会发生同轨迹 leakage，不能假设
  detector generalization 已被严格证明。
- **State Ownership / Control Flow / Data Flow**：environment/workflow 拥有 authoritative UI state、task、
  side effects 与 terminal checker；small/large policy 各自拥有 model/prompt/action schema；monitor service 拥有
  detector checkpoint、window serializer、threshold 与 calibration；milestone controller 拥有 `tau`、before screenshot、
  segment identity 与 verifier result；router 拥有 next-step lease、handoff serialization、budget 与 fallback；
  evidence plane 保存每次 score/event/route/model version/cost/outcome。reasoning text 只是 monitor observation，
  不能取代 screenshot/DOM/environment state。policy switch 也不能隐式复制 credentials 或绕过 approval。
- **Runtime Stability Boundary**：Introduction 声称 stable policy 使用 hysteresis 与 bounded recovery budgets，
  但 Method 只公开单阈值 indicator、next-step route 与 milestone commit；没有 hysteresis formula、recovery duration、
  cooldown、maximum escalations、fallback、thrash/timeout handling 或 code。故这些只能记作 author claim，不能
  当作已公开实现。history re-serialization 也未披露跨 model tokenizer/template/action-schema 的 loss 与 context
  truncation，large policy 是否真正接收到“full local context”尚未被独立测量。
- **Evaluation Contract / Baselines**：OSWorld 使用 EvoCUA-8B/Qwen3-VL-8B small policies 与 Claude Sonnet
  4.5/Kimi K2.5 large policies；WebArena-Verified 使用 gpt-oss-20b/AgentTrek-32B 与 GPT-5 mini/GPT-5.2。
  task success 来自 benchmark execution checker，open/fine-tuned model monetary cost按 OpenRouter/reference base
  pricing估算；paper 表述 latency 在 local 2×H100 上测量，但 proprietary API 与 local/open deployment 的映射未
  充分披露。没有 input/output token length、concurrency、tail latency、network/API variance、model precision/
  quantization 和 production SLO，因此 headline cost/latency 不能脱离该表使用。
- **Results / Usage Boundary**：OSWorld cascade success 54.3%～59.3%，always-large 58.1%/60.1%；WebArena
  cascade 51.3%～58.8%，always-large 55.0%/60.1%。但 large policy 并非罕见 fallback：OSWorld 46.8%～66.9%
  tasks 至少 switch 一次，large model 执行 39.4%～62.6% steps；WebArena 69.2%～73.0% tasks switch，large
  share 56.3%～69.4%。所以证据支持“按 event 改变 compute mix”，不支持“绝大多数步骤不再需要强模型”。
  up to 74.6% cost / 45.8% latency 是特定 pair/price/runtime 的作者 headline，不是通用节省比例。
- **Ablations / Detector Evidence**：paper 比较 no detector、stuck-only、milestone-only 与 both，以及
  periodic `k∈{3,5,7}` 的最佳点；event-driven 在选定 OSWorld/WebArena pair 上优于最佳 periodic 表项。held-out
  detector 表中 milestone learned detector 为 94.1% accuracy / 62.0% F1，stuck 为 93.9% / 91.5% F1；高 accuracy
  掩盖 milestone 稀疏性。label/evaluator 同属 GPT-5.2 family，未与 independent human annotation 校准；paper
  也未给 threshold sweep、false-negative recovery severity、cross-policy/cross-domain transfer、calibration error、
  multiple seeds/CI 或 detector overhead 的端到端分解。
- **What the Evidence Proves**：在两个 GUI benchmark、四组 small/large pairs 与作者 threshold 下，文本轨迹
  monitor + sparse visual verification 可以形成比 always-small 更强、比 always-large 更便宜的若干 Pareto 点；
  event trigger 比选定 fixed-interval baseline 更好。这为“Agent scheduling 必须消费 evolving run state，而非只看
  initial query”提供机制证据。
- **What It Does Not Prove / Limitations / Threats to Validity**：paper 没有显式 Limitations section；不证明
  两类 failure taxonomy 完备、不证明 textual rationale 与真实 UI progress 始终一致，也不证明 silent drift 能由
  先预测 milestone 再调用同 family large verifier可靠捕获。300 trajectories、单次 80/20 split、无 human gold、
  possible overlapping-window leakage、空 model cards 与缺 runtime code 限制复现。benchmark checker 只看 terminal
  state，不能覆盖真实副作用、安全 policy、credentials、rollback 与长期 user intent。model mix、pricing 和
  proprietary versions 会改变 frontier。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：always-on text monitors 降低强模型
  调用，却增加 detector inference、label drift、threshold tuning 与 new control-plane dependency；sparse milestone
  verification 降低检查频率，却可能在两个 checkpoints 之间累积不可逆 drift；history re-serialization 增加模型
  可替换性，却可能丢失 hidden state、tool schema 与 action ownership；small/large thrashing、double billing、
  repeated side effects、stale screenshot、monitor false negative 与 verifier correlated error 都需要 runtime policy。
  high-risk irreversible actions 仍应 always verify/require approval；short/easy tasks 可固定 small model；极低容错任务
  可固定 large model；有 deterministic state checker 时不应退化成 learned judge。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：唯一 owner 为 Ch77。Ch76、Ch77、
  Ch78 与 Ch57～59、Ch61～63、Ch79～80 已核对。Ch58 只拥有 external request/Gateway/EPP routing，不应接管
  Agent run 内 step policy；Ch62 拥有 detector/verifier calibration 与 compute-matched evaluation；Ch76 拥有
  stop/escalate feedback；Ch80 拥有 platform-level run policy/evidence。Ch77 已拥有 durable state、action/retry/
  approval scheduling，却缺少 trajectory event 怎样触发 model escalation、milestone commit 与 sparse verification，
  因而是 `Refine — Existing Argument`，其余章节只接短 handoff。
- **Final Disposition / Changed Files / Open Questions**：`Refine — Existing Argument (Experimental)` / Ch77。
  Historical Books Gate 关闭，不修改 Books；只同步 W18、年度索引、Learning State 与 2026-08-10 Daily。
  待验证：trajectory-grouped split 与 human gold；threshold/calibration/overhead curve；公开 hysteresis/recovery budget
  实现；cross-policy/domain transfer；action-schema handoff loss；在 irreversible side effects、approvals、concurrency、
  tail SLO 与 real billing 下的 failure/cost frontier。

### InteractWeb-Bench — 25/30

- **Candidate / Week / Score / Source Family**：`INTERACTWEB-SYNTHETIC-USER-FEEDBACK-EVAL`；W18；
  `5/4/4/3/5/4 = 25/30`。Source type 为 primary paper、primary PDF、project page 与 author repository。
- **First-public Date / Revision History / Direct Sources**：arXiv:2604.27419 仅有 v1，于
  2026-04-30 04:49 UTC first-public，共 21 页。已读 Abstract、Introduction、Related Work、四类 persona
  construction、developer/user/verifier/judge control flow、oracle-slot/TCR 公式、Experiments、全部 findings、
  cost 与 human-aesthetic appendices、cases，以及 PDF 中 HTML 未完整呈现的所有 prompts。官方 repository
  公开 builder、visual copilot、WebVoyager judge、config、`all.jsonl` 与 mini data，但没有 event-date frozen
  release/tag；project page 仍有 placeholders，所链 Hugging Face organization 当前没有公开 dataset。
  Access and Verification Status 为 `Full Paper Complete; Current Repository Verified; Frozen Event Artifact Not Disclosed`。
- **Original Problem / Why the Previous Design Was Reasonable**：静态、完整 requirement 加 terminal screenshot/
  test 的 WebGen benchmark 可复现、易于模型横向比较，也适合 deterministic regression；它的边界是无法观测
  Agent 面对缺失、噪声、隐喻或矛盾需求时是否会主动提问、利用反馈与决定停止。当 evaluation object 从最终
  artifact 扩展到 requirement-discovery trajectory 时，hidden intent、user response 与 turn budget 都成为系统状态。
- **Changed Constraint / Evolution Relationship**：这是 Ch62 的 `Direct Evolution + Layering`：

  ```text
  complete static prompt + final artifact score
  → synthetic incomplete/noisy/contradictory prompt
  → Clarify / Implement / Verify / Submit trajectory
  → bounded feedback channel + terminal artifact judge
  ```

  后者没有替代前者。需求确定、correctness 可执行时，静态 golden tests 仍是更强 oracle；只有真实系统允许
  多轮澄清、而交互成本和停止语义属于目标函数时，trajectory evaluation 才不可缺少。
- **Mechanism / Persona and Task Construction**：从 WebGen-Bench 的 101 个 golden tasks 出发，以 P-MIN
  抽象/删除 requirement、P-RAM 注入约 70% irrelevant text、P-INT 改写为感官隐喻、P-CON 注入冲突，形成
  404 cases。DeepSeek-V3.2 user simulator 同时持有完整 golden instruction 与 persona wrapper，只在 Agent
  明确询问时返回对应 ground-truth snippet；这使 user 既是被模拟 subject，也是隐藏答案的信息通道，不能用
  synthetic persona label 推断真实 non-expert population fidelity。
- **State Ownership / Control Flow / Data Flow**：benchmark owner 拥有 golden instruction、persona mutation、
  oracle slots 与 difficulty weights；user simulator 拥有受限 reveal policy，但不是 requirement truth 的独立来源；
  evaluated Agent 在 bolt.diy workspace 中选择 Clarify、Implement、Verify、Submit；Playwright environment 拥有
  code、browser state、screenshot、purified console errors、turn/error budgets；Verify 使用 Agent 自定义 criteria、
  从上次 state 汇总的 holistic working memory 与 GUI actions；terminal evaluator 用 GPT-5-mini WebVoyager/SoM
  对 slot 判定。所有 prompt/model/version/turn/action/screenshot/code/judge verdict 必须属于 evidence identity。
- **Scoring Contract**：每个 oracle slot 的权重为
  `W_i=C_tech^(G)·(1+0.5(N_G-1))/N_G`，其中技术复杂度为 1/2/3；TCR 是 passed slot 的加权比例。
  hallucination slot 被单独报告而不进入 TCR。Easy/Mid/Hard 的总 turn limit 为 15/20/25，连续 verification
  error limit 为 6/8/10。任务难度由 handcrafted slot complexity score 上做 K-means 得到；它是作者构造的
  分层，不是现实工作量或风险的独立 ground truth。
- **Implementation / Evaluation Contract**：被测系统是 bolt.diy + Playwright；user 固定 DeepSeek-V3.2，
  final judge 固定 GPT-5-mini，比较 9 个模型。open models 由 vLLM 运行在 8×A800，API models 走官方接口。
  paper 报告 token/API price 推导的 per-site cost，但未完整披露 provider snapshot、temperature、重复 seeds/
  confidence interval、端到端 latency、并发、local precision/quantization、network variance 或 production SLO，
  所以 model ranking 与成本数字不能脱离该 workload contract。
- **Evidence Proves**：在这 404 个 synthetic cases、指定 simulator、action limits 与 model judge 下，选定 Agent
  往往生成更多 code 而不是 Clarify，weighted completion 仍低，P-MIN 比 P-RAM 更困难，且行为呈现不同的
  exploration/commitment pattern。这证明“只看最终 screenshot 会漏掉 requirement acquisition policy”，并提供
  一个可重放的受限测试实例。
- **What It Does Not Prove / Claim–Evidence Boundary**：不证明这些 persona 来自真实非专家用户，也不证明
  user uncertainty、inconsistency 或 latent preference 被模拟。user simulator 知道完整答案，使 clarification
  比现实更干净；P-CON prompt 还允许短暂坚持后回到 ground truth。主要 TCR、IAS、CHR 与 slot correctness
  没有 human/executable gold calibration；三位 CS PhD 只评 aesthetic，Kendall tau 约 0.449、human inter-rater
  约 0.568。论文以 VCI/TCR 相关性宣称 verification 不改善结果，却没有 no-verify/forced-verify controlled
  ablation；“missing information harder than noise”也只对其 mutation/simulator contract 成立。
- **Trade-offs / New Failure Modes / Previous Designs**：synthetic user 扩展 interactive coverage，却增加
  persona realism、answer leakage、simulator/judge coupling 与 prompt drift；self-defined verify criteria 提高自治，
  却允许 Agent 永远不检查自己尚未知晓的 requirement；weighted partial credit 提供诊断，却受 handcrafted
  weights 影响，且 hallucination 不计入 TCR 会让高完成度与未请求元素共存；turn/error limits控制成本，也会
  塑造 strategy。真实用户研究、deterministic functional tests、security/accessibility checks 与 independent
  human/executable calibration 仍是不可替代的相邻证据层。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：唯一 owner 为 Ch62。Ch61～63、
  Ch73～77 已核对：Ch62 已明确覆盖 `snapshot → feedback-conditioned policy`、hidden-answer judge 同时是
  scorer/information channel、feedback vocabulary、turn/retry/stop contract、artifact/environment/trace evidence、
  rubric formation/criterion execution/aggregation 分离与 human/executable calibration。Ch74 已有 typed action 与
  bounded loop，Ch75 已有 ambiguous intent/replanning，Ch76 已有 environment feedback/verifier independence，
  Ch77 已有 durable workflow；paper 所称 holistic memory 只是 task-local control state，不是 Ch73 long-term memory。
- **Final Disposition / Changed Files / Open Questions**：`No Change — Already Covered` / Ch62。该论文增加
  domain-specific benchmark evidence，却没有补出新的长期机制；即使 Historical Books Gate 已打开，也不应把
  benchmark 细节重复写入 Books。本轮只同步 W18、年度索引、Learning State 与 2026-08-10 Daily。待验证：
  真实用户/需求分布、TCR human/executable calibration、hallucination-inclusive utility、controlled clarification/
  verification ablation、frozen release/data，以及在 latency/cost/security/accessibility SLO 下的 frontier。

### FlashRT — 28/30

- **Candidate / Week / Score / Source Family**：`FLASHRT-APPROXIMATE-REDTEAM-OPTIMIZATION`；W18；
  `5/5/5/4/5/4 = 28/30`。Source type 为 primary paper、primary PDF 与 author implementation repository。
- **First-public Date / Revision History / Direct Sources**：arXiv:2604.28157 仅有 v1，于
  2026-04-30 17:43 UTC first-public，共 31 页。已读 Abstract、Introduction、Background/Related Work、Threat
  Model、Optimization Formulation、Unified Framework、全部 Method/algorithms/formulas、Evaluation、Ablations、
  defenses/black-box extensions、Discussion/Limitations 与 Appendices A～F。官方 repository 当前只有 2 commits、
  没有 release/tag；已核对 README、datasets/model configs、white/black-box quick starts、主要 attack/model
  code surface 与默认 hyperparameters。Access and Verification Status 为
  `Full Paper Complete; Current Code Verified; Event-time Frozen Release Not Disclosed`。
- **Original Problem / Why the Previous Design Was Reasonable**：heuristic prompt injection 便宜、黑盒可用，
  适合持续 regression；full GCG/nanoGCG 则精确计算每个候选 loss 与 gradient，在短 context 或高风险 model
  owner red-team 中给出更强 adaptive attacker。长 context 下，短 adversarial span 只改变 sequence 的局部，
  精确方案却反复计算整个右侧 context，并在 backward 保存全序列 activation/gradient，campaign strength 被
  HBM 与 wall-clock 限制；只做 random context clipping 又会改变 loss，容易把低 ASR 误作 defense robustness。
- **Threat Model / Scope Boundary**：主要 white-box attacker 访问 target model parameters、system/task
  instruction、完整 context 与 attacker-chosen target output，并在 context 中注入远短于总长度的 adversarial
  text。目标覆盖 prompt injection 与 knowledge corruption，不覆盖典型短-input jailbreak。paper 所称 black-box
  extension 实际仍要求 red teamer/model provider 能读取 target log-probability/parameters，再用 TAP/AutoDAN
  产生 payload；不能外推普通 API-only attacker。
- **Changed Constraint / Direct Evolution**：

  ```text
  heuristic payload
  → exact full-context white-box optimization
  → prefix KV reuse
  → influence-selected approximate forward
  + context-subsampled approximate gradient
  + stagnation-triggered gradient resampling
  ```

  演进目标不是近似模型输出，而是只保留足以指导 adversarial search ranking/direction 的计算。exact full-context
  optimization 在 context 短、approximation error 高或 release verdict 要求 strongest-known attack 时仍成立；
  heuristic/API-only campaign 在模型权重不可访问时仍是不同 threat model，而非落后版本。
- **Selective Forward Mechanism**：输入分为 `I_s || C_l || T || C_r || I_u || Y_hat`。对 current best
  `T_best` 保存完整 KV；shared prefix `I_s || C_l` 直接复用。每当 best candidate 改变，系统用 target-output
  tokens 对中间层 attention heads 的权重，为 `C_r` 的长度 `rho` segments 计算 influence score，选择比例
  `beta` 的 segments 重算 hidden states/KV；`T`、`I_u` 与 target output 始终精确重算，其余右侧位置沿用
  `T_best` cache。`beta=1` 退化为 standard exact KV-caching，较小 `beta` 用 loss-ranking error 换候选吞吐。
- **Approximate Backward / Resampling**：将左右 context 都切成长度 `rho` 的连续 segments，每次随机保留
  `gamma` 比例，针对缩短后的 sequence 只计算 adversarial-token embeddings 的 gradient，用于生成离散 token
  candidates。若连续 `tau` 次候选没有改善 loss，重新采样 context segments 刷新 gradient direction。近似
  gradient 只负责 proposal，不拥有 acceptance；candidate 仍按 approximate loss 更新 best，成功再由 target
  output condition 检查。cache、recompute set 与 gradient 在 best change 时一起刷新。
- **State Ownership / Control Flow / Data Flow**：red-team campaign 拥有 threat case、context/injection
  position、target output、attempt/restart/early-stop budgets；target-model runtime 拥有 model/tokenizer/precision、
  attention implementation 与 exact success check；optimizer 拥有 `T_best/loss_best`、candidate buffer、gradient、
  `beta/gamma/rho/tau`；cache manager 拥有 best-candidate revision、KV tensors、recompute indices；evidence plane
  必须保存 model/code revision、random seed、position、approximation params、per-iteration loss/exact verdict、
  GPU/time/memory 与 stop reason。近似 cache 不能进入 production request cache，也不能把 attack payload 当
  未经隔离的可执行 artifact。
- **Implementation / Evaluation Contract**：主要实验使用 4×H100 96 GB、BF16；模型覆盖 Llama-3.1
  8B/13B/70B、Qwen-2.5 7B/14B、Mistral 7B、DeepSeek-R1-Distill、Meta-SecAlign 与 coding/agent cases。
  六个主 datasets 各取 first 50 test samples，prompt-injection contexts 平均约 8.7K～18.4K words，knowledge-
  corruption contexts 截至 32K tokens；主要 baseline 是 heuristic、random context clipping、nanoGCG 与加入
  scheduling/restarts 的 nanoGCG-OPT。prefix/suffix 常为 30 tokens，最多 5 restarts，并共享 loss-based stop。
  这些条件完整约束 2×～7× time、2×～4× memory 等 headline，不能脱离 model/context/position/hardware 使用。
- **Ablations / Sensitivity / Overhead**：NQ/Llama-3.1-8B sensitivity 显示 `beta≈0.05` 与 `gamma≈0.2`
  在作者 grid 中形成最低总时长附近，而不是越小越快；过小 `gamma` 增加收敛 passes，`rho=1` 使 influence
  noisy，`tau` 也有 U-shaped trade-off。attention influence 比 random/semantic/individual-probability selection
  更快，但该比较只有指定 model/dataset 与 single table；没有 multi-seed CI、approximate-vs-exact candidate
  rank error、gradient cosine/error distribution、position/model-wise calibration 或 kernel-level overhead breakdown。
- **Evidence Proves**：在上述 white-box target-output contract 中，selective forward 与 sampled backward 可在
  保持或提高作者 ASR 的同时减少 measured wall time/HBM，并使 70B configurations 在四 H100 上可运行；
  defenses、code completion、EHRAgent/paper review 与 AutoDAN/strategy-search appendices 显示机制可跨若干
  workloads 复用。它还证明 red-team resource budget 会改变能够执行的 attacker strength，故“baseline OOM”
  不能解释为 defense 安全。
- **What It Does Not Prove / Limitations**：不证明现实攻击者拥有 weights/log-probabilities/target answer，不
  证明 ASR 等于 deployment incident probability，也不证明 Meta-SecAlign 或 guardrail 在完整 production stack
  下失效。EHRAgent case 只以 target thought 推断高概率调用 DeleteDB，没有执行 side-effect/authorization audit；
  20-paper review 与 code cases 很小。作者没有 independent reproduction、seeds/CI、false-success severity、
  transfer to unseen model revisions、quantized/TP runtimes、concurrency/energy/cost 或 production SLO。current
  2-commit repository 不是 event-time immutable artifact，README default recompute ratio 与 paper tuned setting
  也不能视为同一 frozen experiment。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：approximation 扩大可执行 campaign，
  却可能错排 candidates、错过最强攻击、因 stale influence/cache 接受错误 search direction；attention weight
  是选择 heuristic，不是 causal attribution。context subsampling 降低 activation memory，却增加 gradient
  variance、resampling work 与 seed sensitivity。target-specific attacker 提高 worst-case pressure，却失去
  API-only realism。fast approximate sweeps、exact top-candidate confirmation、fixed heuristic regression、
  human red team 与 production action-boundary tests 应并存，不能用单一 ASR 代替 release decision。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：唯一 owner 为 Ch68。Ch67～69 与
  Ch22、Ch49～51 已核对。Ch22/50 已覆盖 long-context pair compute、activation/KV/HBM budget 与“近似/选择
  必须验证误差”，但 FlashRT 的 KV 是 attack optimizer 的 mutable best-candidate cache，不是 Serving request
  state；Ch49/51 不拥有该机制。Ch68 已有 run-centric campaign、attempt opportunity、attacker/judge/version/
  budget identity 与 prompt-injection action boundary，却尚缺“red-team resource feasibility 会限制 attacker
  strength，以及 approximation policy 本身必须进入 evidence identity”的机制，因此暂定
  `Refine — Existing Argument (Experimental)`；Ch50 只接 memory-compute handoff。
- **Final Disposition / Changed Files / Open Questions**：`Refine — Existing Argument (Experimental)` / Ch68。
  Historical Books Gate 关闭，不修改 Books；只同步 W18、年度索引、Learning State 与 2026-08-10 Daily。
  待验证：approximation error/candidate-rank calibration、multi-seed CI、exact-final verification、unseen model/
  position transfer、frozen artifact、API-only threat models，以及把 compute/memory/attempt budget 对齐后 defense
  robustness 是否仍成立。

### ReVSI — 28/30

- **Candidate / Week / Source Family / Type**：REVSI-FRAME-CONDITIONED-SPATIAL-EVALUATION；W18；
  primary research paper、ICML 2026 / OpenReview record、benchmark code、project page 与 dataset artifact。
- **Event / First-public / Revision History**：arXiv:2604.24300 v1 于 2026-04-27 10:45 UTC 首发，归入
  W18；v2 于 2026-05-05 发布，只用于核验 revision，不倒写事件日。arXiv PDF 约 40 MB，当前直接提取
  失败；Full Review 通过作者公开的 CC BY 4.0 全文副本与 ICML/OpenReview metadata 交叉核验，并联合读取
  official repository、project page 与 Hugging Face dataset。current repository/data 是访问日 artifact，
  没有 event-time frozen tag，不能当作 v1 运行快照。
- **Full-read Coverage / Access**：已读 Abstract、Introduction、Related Work、validity pitfalls、scene
  reannotation、frame-budget-aware QA、visibility pipeline、dummy-video diagnostics、Evaluation、Conclusion、
  Limitations/Impact、全部相关 Appendices、prompt/QA templates、sampling、model setup 与 additional results；
  还核对 repository 的 LMMs-Eval/VLMEvalKit/SWIFT/TorchMetrics 路径、QA generation scripts，以及
  dataset 的四个 subset、schema、24,150 rows 与 4.87 GB current artifact。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：旧 benchmark 以完整
  3D scene annotation 生成答案，再给 VLM 均匀抽取少量视频帧；在成本受限、希望复用现成 RGB-D
  标注并保持固定 QA 的条件下，这很合理。问题是 annotation-to-video drift、错误/缺失 boxes、ambiguous
  QA 与 scene-observability mismatch 会让 ground truth 描述模型从未看到的对象。随着 frame budget、
  video preprocessing 与模型输入 contract 成为可变项，单一 scene-level answer 不再等价于可回答实例。
- **Mechanism / State Ownership / Control and Data Flow**：ReVSI 先对 ScanNet v2、ScanNet++ v2、
  ARKitScenes、3RScan 与 MultiScan 共 381 scenes 进行 open-vocabulary object/3D-box 与 room-boundary
  人工修正；GPT-5.2 仅辅助核验不确定命名，最终由人决定。3D boxes 经 mesh segmentation、ray casting
  与 camera poses 投影为 per-frame 2D visibility cues；max pixel coverage 超过 5% 作为辅助阈值，否则
  手工标注，所有最终 visibility 再人工核验。all-frame 到 nested 64/32/16 使用层级 uniform sampling
  保持相同时间跨度与包含关系，并为每个 budget 只保留实际可见、可回答的 QA。另构造 query-dropped、
  first-frame repeated 与 black 16-frame inputs：删除 queried-object evidence 后，counting ground truth 改为
  zero，以测试输出是否仍由视觉证据支持。benchmark owner 拥有 annotation、sampling indices、visibility、
  QA、prompt 与 scorer state；executor/model owner 拥有 preprocessing、frame/FPS 与 decoding state。
- **Implementation / Evaluation Contract**：ReVSI 当前发布 6.81K all-frame QA，四个 subset 合计
  24,150 rows；任务含 counting、object/room size、absolute/relative distance 和 relative direction，移除
  appearance-order。数值题用多个 relative-error thresholds 聚合 MRA，选择题用 exact match；zero-shot
  路径使用 greedy decoding，fine-tuned models 使用各自默认 evaluation code。主表多为 64 frames，
  specialized models 仍使用 16/32/128 frames 或 FPS；proprietary models 只评 1,093-sample tiny subset
  （约全量 16%），Gemini 采用 FPS sampling。因此排名变化不是严格 frame、token、compute 或 confidence
  matched comparison。论文披露 model/frame contract，但未披露统一 hardware、latency、cost、SLO、
  multi-seed variance 或置信区间。
- **Baselines / Ablation / Diagnostics / What Evidence Proves**：作者对比 VSI-Bench 与 ReVSI，并在
  16/32/64 frames、fine-grained task variants、real/dummy videos 上检查结果。证据支持：在作者审计的
  scenes/questions 上，旧 annotation 与当前视频观察确有可见性/答案冲突；ground-truth cleanup 与
  frame-conditioned QA 会改变部分模型排序和 specialized-model gain；evidence removal 能暴露某些模型在
  object count/size 上仍输出高先验答案。它证明 input transform、可见性与 answerability 是 evaluation
  identity 的一部分，并提供一种有用的 counterfactual diagnostic。
- **What It Does Not Prove / Limitations / Threats**：不证明 ReVSI 是所有 3D reasoning 的无偏 ground
  truth，也不证明 ranking reversal 等于真实部署能力。作者专家同时参与 annotation 和 verification，未
  披露独立 blinded audit、inter-annotator agreement、held-out QA audit 或 uncertainty；5% projected-area
  threshold 是 heuristic，presence 也不必然保证 geometry 可判断。dummy inputs 可能是 OOD，query-drop/
  zero-answer 主要适用于 counting，不能完全区分 refusal、parser error、visual perception 与 reasoning。
  proprietary tiny subset 与 Gemini FPS contract 削弱横向可比性；更大 fine-tuning data 的小收益只是指定
  Spatial-MLLM 配置的结果。论文自己也承认 expert annotation 成本限制规模化。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：frame-conditioned labels 提高 instance
  validity，却把 annotation 乘以 frame policy，增加 storage、版本、manual-review 与 benchmark refresh
  成本；sampling 或 processor 改变会使旧 QA 失效。counterfactual evidence removal 提高诊断力，却可能
  引入 OOD behavior 与任务特定 ground-truth rewrite。scene-level QA 仍适用于 full observation、固定传感器
  contract 或只测环境知识的场景；固定 frame benchmark 仍适合回归，但必须冻结 indices 和 preprocessing。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：这是 Ch62 的 Direct Evolution：
  dataset-level ground truth → executor-specific frame sampling → observation-conditioned answerability →
  evidence-removal counterfactual。已读 Ch61～63；Ch61/63 分别拥有 resource placement 和 continuous
  observed state，不拥有 benchmark validity。Ch62 已覆盖 subject、distribution、dataset/environment、
  scorer、per-example evidence 与 uncertainty，却未明确把 observation transform / frame indices 纳入
  input identity，也未明确说明 ground truth 必须随实际可见证据重新判定，故形成真实机制缺口。
- **Final Disposition / Changed Files / Open Questions**：28/30；provisional Refine — Existing Argument
  (Experimental) / Ch62。Historical Books Gate 关闭，不修改 Books；本轮只同步 W18、年度索引、
  Learning State 与 2026-08-10 Daily。待验证：独立 annotation audit、agreement/confidence、不同 processor/
  sampling policy 下的 answerability stability、matched frame/token/compute leaderboard、dummy OOD calibration、
  frozen event-time artifact，以及 input transform 变化时 QA invalidation 和 migration 的平台语义。

### Step-Level Advantage Selection — 28/30

- **Candidate / Week / Source Family / Type**：SAS-SHORT-CONTEXT-STEP-ADVANTAGE；W18；ACL 2026
  Findings / arXiv primary paper 与 official VeRL-based code/data artifact。
- **Event / Revision / Direct Sources / Access**：arXiv:2604.24003 仅有 v1，于 2026-04-27 03:34 UTC
  首发；已读完整 HTML、全部 Appendix、官方 repository 的 install/data/train/eval paths 与 current
  six-commit surface。repository 无 release/tag，故 current main 只能验证机制可执行入口，不能充当 event-time
  immutable run。Full-read 覆盖 Introduction、GRPO/length-reward background、short-context control、
  SAS equations、training/evaluation、baselines、all ablations/sensitivity/overhead、Related Work、
  Discussion、Limitations、AES、step segmentation 与 licenses。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：outcome-reward GRPO
  把同一 response advantage 传播给全部 tokens；当 verifier 可靠且 rollout 完整时，它省去 critic、语义清楚。
  efficient-reasoning 工作又常在 4K post-training context 中压缩原本 8K～24K reasoning。约束变化在于
  max context 同时成为隐式 length signal：rollout 被截断时，即便中间推理正确，终局 verifier 仍给零，
  标准组内负 advantage 会惩罚整条轨迹。作者把 8K correct outputs 截到 4K 后重验，报告约 29% 失去
  correct status，多数缺 final boxed answer/closing steps；这支持 credit mismatch，而非证明所有 failed
  rollout 都正确。
- **Mechanism / State Ownership / Control and Data Flow**：policy 以 double-newline 把 response 切成
  steps，用每 step token mean log-probability 作为 confidence。correct rollout 中按升序选最低 confidence
  比例 r 并将对应 token advantages 置零，避免强化冗余/不可靠步骤；verifier-failed rollout 中按降序选最高
  confidence 比例 r 并置零，屏蔽可能因 truncation 被误罚的可靠中间步骤。其余 correct tokens 保留正
  group-relative advantage，其余 failed tokens 保留负 advantage；零值不会把 failed step 提升到 correct
  step 之上。rollout policy 拥有 log-probs、step boundary 与 advantage masks；verifier 拥有 terminal
  correctness；trainer 拥有 r、4K truncation、checkpoint selector 与 update state。
- **Implementation / Evaluation Contract**：base 为 DeepScaleR-1.5B-Preview，训练数据约 40K math
  problems；VeRL、4K max context、500 steps、batch 128、8 rollouts/prompt、lr 1e-6、r=0.3，8×AMD
  MI250 64 GB。AIME24 用于选择最高 AES checkpoint，同时又出现在五项 math report；另评 AIME25、
  MATH、AMC、OlympiadBench、GPQA-Diamond、LSAT 与 MMLU-500。evaluation 每题 16 samples，
  temperature 0.6、top-p 0.95、max generation 8K，报告 sample-average Pass@1、tokens 与 AES。headline
  只对该 model/data/context/checkpoint-selection/decoder/hardware contract 成立，不是 production latency。
- **Baselines / Ablations / Sensitivity / Overhead**：baselines 为同 base/4K 的 GRPO、L1-Max、LAPO-I、
  ThinkPrune。作者分别移除 failed-rollout shielding、改 random selection、改 token-level mask，并扫描
  r=0.1～0.9；r=0.3 在作者表中最佳，但不同 r 差距不大。MATH500 上 policy-confidence 与
  Qwen2.5-Math-PRM-7B ranking 的 nDCG@k 为 0.9022；这只是两个 model-derived scorers 的相关，不是
  human-gold step correctness。SAS 每 training step 327.15 秒，对 GRPO 279.08 秒，约增加 17% wall time；
  作者称无需额外 forward/rollout 且 memory 不变，但未给 kernel/profile/energy/cost breakdown。
- **What Evidence Proves**：在上述单模型受控设置中，4K GRPO 即使没有 length reward 也显著缩短输出，
  同时后期 accuracy 波动、entropy 下降；SAS 的 asymmetric zero-mask 在作者 tables 上改善 accuracy-token
  frontier，failed-rollout shielding、confidence selection 与 step granularity 各有 ablation support。长期
  价值是：context window 属于 reward/credit contract，terminal verifier failure 不能自动证明全部 prefix
  actions 应获负 credit。
- **What It Does Not Prove / Limitations / Threats**：不证明 policy log-probability 是 step correctness，
  不证明自然语言 delimiter 是语义 step，也不证明缩短 visible CoT 等于更少内部 compute。只有一个 1.5B
  math-derived model、一个 4K training context、一次 500-step recipe；无 training seeds/CI、不同 scale/
  tokenizer/template、code/tool/environment verifier、不同 context sweep 或 independent reproduction。
  AIME24 参与 checkpoint selection，不能同时视为纯 held-out evidence；16 sampled outputs 降低 response
  sampling variance，却不覆盖 training-run variance。AES 把 accuracy 与 length 压成单分数，权重本身也是
  policy。作者的 “no extra memory” 未由完整 state profile 证明。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：SAS 复用 intrinsic log-probs，少一个
  PRM forward，却增加 segmentation、sorting、masking 与约 17% measured step time。过度 confidence 会
  保护流畅但错误的步骤，低 confidence 也可能是关键探索；delimiter drift、tokenizer change、truncated
  final answer、verifier bug 与 r/checkpoint tuning 都会改变 credit。完整 context、可靠 step verifier、
  learned critic、process reward 或普通 outcome GRPO 仍可能更合适；SAS 不是对它们的普遍替代。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：Ch29 唯一 owner，属于
  Direct Evolution：sequence-level group advantage → truncation-aware prefix credit → step-level asymmetric
  shielding。已读 Ch28～30；Ch28 已解释 terminal reward 与 token-level credit，Ch30 是 offline pair
  objective，不拥有 on-policy advantage。Ch29 已指出“正确 final 可含错误 reasoning、错误 final 可含有用
  steps”和 process verifier trade-off，但尚未明确 context-window-induced reward corruption 与不把 failed
  prefix 升为正 reward的 zero-mask mechanism，因此形成真实机制缺口。
- **Final Disposition / Changed Files / Open Questions**：28/30；provisional Refine — Existing Argument
  (Experimental) / Ch29。Historical Books Gate 关闭，不修改 Books；只同步 W18、年度索引、Learning
  State 与 2026-08-10 Daily。待验证：multi-seed/scale/context sweep、gold step labels、trajectory-format
  robustness、tool/code verifiers、validation leakage-free checkpointing、advantage-bias analysis，以及相同
  quality/SLO 下 training overhead 能否由 inference token savings 抵消。

### Learning from Noisy Preferences / Semi-DPO — 27/30

- **Candidate / Week / Source Family / Type**：SEMI-DPO-MULTI-DIMENSIONAL-NOISY-PREFERENCE；W18；
  ICLR 2026 conference paper、arXiv:2604.24952 v1、作者 project page 与公开 full-text copy。
- **Event / Revision / Direct Sources / Access**：arXiv v1 于 2026-04-27 19:49 UTC 首发；ICLR/OpenReview
  record 与作者 project page 均标注 ICLR 2026。已联合阅读 conference full text、作者项目页和当前公开
  artifact surface。论文承诺的 `github.com/L-CodingSpace/semi-dpo` 当前返回 404，项目页也标为
  `Code (Under Review)`；因此 paper mechanism 可核验，implementation artifact 与 event-time run 不可核验。
- **Full-read Coverage**：Abstract、Introduction、Related Work、Diffusion/RLHF/Diffusion-DPO preliminaries、
  multi-dimensional conflict theorem、Semi-DPO method、全部 experiments/tables、Conclusion、Ethics，以及
  Appendix 6.1～6.11：gradient derivation、variance proof、LLM-use statement、limitations、online/offline
  comparison、related methods、online extension、reward-committee motivation、training/cost details、additional
  quantitative 与 qualitative results。另核对 project-page method/result tables 与 current missing-code boundary。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：标准 offline Diffusion-DPO
  把同 prompt 的 winner/loser pair 当成单一、可信的 preference relation；当 annotation ontology 相对一致时，
  binary pair 简洁、可重放，并避免显式 Reward Model 与 online rollout。约束变化是视觉偏好同时含 aesthetics、
  semantic alignment、detail 等维度：holistic winner 可能只在部分维度胜出，原标签却把所有属性绑定到同一方向，
  使某维度的理想更新与 holistic DPO update 相反。论文以 aligned/conflict partition 推出 inner-product variance
  下界；该证明依赖不可直接观察的 per-dimension oracle reward，只证明在其定义成立时 conflict mass 必然贡献
  方向方差，不证明公开数据中的真实 conflict rate 或 pseudo-label 一定等于人类维度偏好。
- **Mechanism**：第一阶段用 PickScore、HPS v2、CLIP Score、LAION Aesthetics 与 ImageReward 对原 pair
  重新打分，只有五者都同意原 human label 才进入 clean anchor set，其余进入 noisy/unlabeled set。第二阶段先在
  clean set 训练 Iter0；上一轮 diffusion policy 的 per-timestep DPO logit sign 决定保留或交换 pair orientation，
  logit magnitude 作为 confidence。diffusion timeline 被划分为十个 intervals，每个 interval 使用动态 threshold；
  只有高置信 pseudo-label 进入下一轮 loss，并始终与 clean-set anchor loss 联合训练。
- **State Ownership / Control and Data Flow**：dataset curator 拥有原 human pair、tie removal 与 prompt identity；
  reward-committee stage 拥有五个 scorer revision、score orientation、unanimous rule 与 clean/noisy partition；
  iteration controller 拥有 teacher checkpoint、iteration id、timestep bin、threshold、confidence、pair swap 与
  accepted pseudo-label manifest；trainer 拥有 clean anchor、derived pseudo-label batch、reference policy、beta、
  optimizer 与 current checkpoint。数据流为 `human pair -> committee consensus -> clean anchor / unlabeled ->
  Iter0 -> previous-policy timestep logits -> confidence filter + orientation -> composite DPO -> next checkpoint`。
  “clean”是特定 committee/version 下的 derived view，不是不可变 ground truth。
- **Implementation / Evaluation Contract**：Pick-a-Pic V2 去除约 12% ties 后含 851,293 pairs、58,960
  unique prompts；unanimous consensus 得 176,999 clean pairs，进一步分为 173,007 train 与 3,992
  accuracy-control pairs。base models 为 SD1.5 与 SDXL。公开的 SD1.5 training contract 为 32×NVIDIA
  A100 40 GB、per-GPU batch 4、gradient accumulation 4、global batch 512；Iter0 为 1,600 steps、lr
  `4e-9`，Iter1/2 各 4,000 steps、lr `4e-10`，beta=2500，均 warmup 400 steps。十个 timestep bins
  初始取各自 confidence 80th percentile；若 3,992-pair set 上某 bin accuracy 低于 70%，则提高 threshold。
  SDXL 的完整 training hardware/steps/batch 未披露。GenEval 明示 50-step inference；其他 benchmark 的完整
  seed/sampler/precision/latency contract 未披露。
- **Baselines / Ablations / Sensitivity / Overhead**：比较 base、Diffusion-DPO、Diffusion-KTO、MaPO、InPO
  的 official checkpoints，并报告 HPS v2、Parti-Prompt、Pick-a-Pic V2、GenEval、T2I-CompBench++ 与
  ImageReward/HPS/PickScore/Aesthetic/CLIP/MPS。消融覆盖 Iter0/1/2 与 2～5 个 committee scorers；没有
  threshold percentile、70% control rule、bin 数、不同 pseudo-label weighting、human audit 或 random seed
  sensitivity。作者报告 SD1.5 Iter0+1 为 132 GPU hours、Diffusion-DPO baseline 为 192 GPU hours，加入
  Iter2 后为 228 GPU hours；这没有分解 committee scoring、pseudo-label materialization、I/O、energy、wall
  time 或 SDXL cost，也不是 production SLO。部署 architecture 未变，只支持“未新增模型结构状态”，不能单凭
  论文断言所有 runtime/kernel memory 行为逐位相同。
- **What the Evidence Proves**：在上述 two-base-model、单 preference dataset 与作者 scorer suite 中，
  consensus-filtered cold start 加两轮 timestep-conditioned self-training 改善了多项 machine-score 与 compositional
  benchmark；Iter0→Iter1 增益最大，Iter2 较小。committee-size 与 iteration ablations 支持“筛选 policy 与 derived
  label lifecycle 会改变结果”。长期机制是：offline preference pair 的 label ontology、scorer committee 与
  pseudo-label lineage 都属于 objective identity，不能只保存 winner/loser 两列。
- **What It Does Not Prove / Limitations / Threats**：不证明五个 scorers 的一致等于 human truth；其中多数
  scorers 同时参与 headline evaluation，形成 selection/evaluation coupling。3,992-pair “test” set 又用于监测
  accuracy 并调整 threshold，实际承担 validation/controller 职责，不能作为纯 held-out test。没有直接 human
  evaluation、independent reproduction、training seeds/confidence intervals、committee-version audit、SDXL 完整
  recipe 或可用 code/model artifact。self-labeling 可能放大 Iter0 bias；per-timestep logit magnitude 未经独立
  calibration，diffusion timestep 也不等于可解释的 human preference dimension。论文的 variance lower bound
  不自动证明 Semi-DPO 降低真实 oracle conflict，更不证明“model is its own reward model”可跨 architecture 泛化。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：收益是保留约 79% 被 consensus 拒绝的数据、
  不在最终 loop 额外 serving 显式 RM，并把 coarse pair 转为 timestep-conditioned signal；代价是五 scorer
  preprocessing、multi-stage checkpoint/manifest、threshold tuning、teacher drift 与 confirmation bias。scorer
  升级会使 clean/noisy partition 失效，iteration restore 若丢失 teacher/threshold/pair-orientation 会静默改变目标。
  当 preference ontology 单一且 pair 经人工校准时，vanilla offline DPO 更简单、可重放；需要探索 policy 新分布时，
  online DPO/RL 仍更合适；能获得 per-dimension human labels 时，直接保留多维标注优于先压扁再自我恢复。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：Ch30 为唯一 owner，Ch31 只接收 derived
  dataset/teacher/threshold checkpoint handoff。关系为 `Direct Evolution`：holistic offline pair -> committee-defined
  anchor/unlabeled split -> previous-policy pseudo-label -> iteration-versioned preference dataset。已完整阅读 Ch29～31。
  Ch29 拥有 on-policy group advantage，不拥有 offline pair relabeling；Ch31 拥有可恢复 state transaction。Ch30
  已指出 preference quality、objective bias 与 offline coverage，却尚未明确 multi-dimensional projection、
  scorer-consensus circularity、pseudo-label provenance 和 evaluation set 进入 control loop 后的身份变化，存在真实机制缺口。
- **Final Disposition / Changed Files / Open Questions**：27/30；provisional `Refine — Existing Argument
  (Experimental)` / Ch30，Ch31 short handoff。Historical Books Gate 关闭，不修改 Books；只同步 W18、年度索引、
  Learning State 与 2026-08-10 Daily。待验证：公开 immutable code/model/data manifests、multi-seed reproduction、
  committee-out human audit、strict held-out evaluation、SDXL matched recipe、threshold/bin sensitivity、iteration
  rollback，以及 scorer/teacher revision 变化时 derived labels 的 invalidation 与 migration。

### Operating-Layer Controls for Onchain Language-Model Agents Under Real Capital — 28/30

- **Candidate / Week / Source Family / Type**：`ONCHAIN-AGENT-MANDATE-TO-SETTLEMENT-CONTROLS`；W18；
  arXiv:2604.26091 v1、作者公开全文、DX Terminal Pro 官方 contract documentation、whitepaper 与 Terms of
  Service。类型为 production-system study；机制、合约权限与公开链上 surface 可交叉核验，内部 inference
  traces、pre-launch replay corpus、classifier labels、figure data 和完整 runtime/code 未公开。
- **Event / Revision / Direct Sources / Access**：arXiv v1 于 2026-04-28 20:10 UTC 首发，无后续 revision；
  已阅读唯一 v1 全文、全部表图、Limitations/Ethics、Appendix 中 prompt compiler 和 final-day Go template
  slices，并联合核对 2026-03-24 官方 AgentVault/Core Contracts 文档、whitepaper、Quick Start 与
  2026-02-23 Terms。官方文档确认 `VaultOperator` 的窄权限、owner pause/withdraw/settings 权限与合约级
  token/recipient/min-output guards；未发现公开 raw trace、replay dataset、figure-data artifact、完整
  prompt compiler/runtime repository 或可独立重跑的 evaluation harness。
- **Full-read Coverage**：Abstract、Introduction、deployment/system overview、user controls、prompt compiler、
  runtime/contract authority、pre-launch methodology、全部 failure-mode interventions、trace reuse、internal
  cross-model transfer、frozen-harness production behavior、Related Work、Limitations/Ethics、Conclusion、全部
  references，以及 Appendix 的 compiler input table、strategy lifecycle、market/portfolio/memory/current-state
  injection、anti-fabrication、sell/launch/cap/output rules。另核对官方合约 API、protocol contract topology、
  agent cycle/transparency、real-capital/data-rights boundary。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：单轮 advisor 可以只给文本，
  用户自行判断与执行；把所有偏好写进一个 prompt、让模型直接给动作，在低风险 demo 中也足够灵活。约束
  变化是 3,505 个用户出资 vault 在 21 天内持续运行：同一模型反复读取变化中的 mandate、portfolio、market、
  fee 与 protocol state，动作会产生真实且相互影响的不可逆 side effect。此时“模型回答看起来合理”不能证明
  user intent 被正确解析、action 被授权、交易被有效构造或链上结算成功；错误必须沿 mandate-to-settlement
  path 定位，而不是归为一个 model-error bucket。
- **Mechanism**：用户通过五个 1～5 sliders、max-trade/slippage、priority/expiry strategy text 与 pause/closure
  表达 mandate；runtime 每次 decision 前读取 authoritative onchain config，把 active strategy lifecycle、
  current portfolio/market/reap state、recent source-labeled decisions 与 hard execution constraints 编译成 per-run
  context。模型只产生 BUY/SELL/OBSERVE typed proposal；backend 与 AgentVault 再执行 schema、token universe、
  amount/price-impact/slippage、WETH pair、recipient、pause/experiment-state 与 least-privilege checks。每一步把
  config、prompt identity/hash、reasoning/tool arguments、validation result、portfolio state、transaction 与 settlement
  连接为 trace。pre-launch loop 在冻结 market/portfolio/strategy/slider snapshot 上 replay prompt variants，通过
  trace classifier 与 macro metrics 定位 reading-order、numeric anchoring、fabricated rules、cadence 与 tokenomics
  failures，再做窄 intervention；production 期冻结 harness，避免边运行边 steering。
- **State Ownership / Control and Data Flow**：owner/onchain contract 拥有资金、settings、strategy lifecycle、
  pause/closure 与 vault identity；prompt compiler 拥有 template/version、source order、state projection 与 prompt hash；
  model 只拥有当前 proposal，不拥有 authorization 或事实状态；backend validator 与 smart contract 分别拥有 offchain
  policy/schema gate 和 onchain settlement invariants；operator 只能 swap 并在 owner 发起后 finalize closure，不能
  withdraw、改 settings/strategy/ownership 或任意 `xcall`；trace/evaluation plane 拥有 attempt、rejection、transaction
  与 outcome evidence。数据流为 `onchain mandate/state -> compiled context -> model proposal -> deterministic
  validation -> least-privileged operator -> AgentVault guards -> settlement -> linked trace -> replay/diagnosis`。
- **Implementation / Evaluation Contract**：production model 为 Qwen/Qwen3-235B-A22B-Thinking-2507，temperature
  0.6，通过 SGLang serving；同一 model/kernel/hardware/sampling/chat-template/policy 在 21 天生产窗口冻结。论文
  报告 3,505 funded vaults、12-token bounded market、每 swap 2.3% fee、约 4～6 分钟随机 poll、7.5M
  invocations、约 70B tokens、约 300K onchain actions、约 $20M volume、超过 5,000 ETH deployed；但没有披露
  GPU topology、precision、batch/concurrency、latency/availability SLO、完整 per-run distribution 或原始 logs。
  pre-launch 经过 24 prompt revisions/3 weeks，live-like cohorts 为数百至约 2,000 agents；3,000 fixed-state
  replay scenarios，每个 slider level 60 samples；4,900 sampled traces 由 Claude Sonnet 4.5 分类。另一个内部
  EVM swap-construction screen 未公开 dataset/harness，只报告 Claude 4=87%、Claude 4.6=96%、同 model 加
  DX-style harness=99.9%，不能当作本次 production success rate。
- **Baselines / Ablations / Sensitivity / Overhead**：窄 prompt interventions 比较同 wording 不同 placement、移除
  exact numeric floors、加入 skip gate、结构化 tokenomics 与过滤 prior-decision memory；报告 fabricated sell rules
  57%→3%、fee-led observations 32.5%→<10%、受影响 cohort deployment 42.9%→78%，以及 fee sentence 从
  paragraph 8 移到 1 后 trace citation 3%→74%。这些是 pre-launch replay/live-like population 的 successive
  harness comparisons，不是完整 factorial/randomized ablation；未给 seeds、CI、classifier human audit、prompt-change
  interaction、per-variant token/latency cost或 false-reject cost。production sliders 呈 ordered gradients，但 holding/
  diversification 被 safety checks 压缩；profitability、language cohort、herding/cascade 都是 observational。
- **What the Evidence Proves**：在单 venue、单模型、固定 token universe、真实结算且 frozen harness 的受限系统中，
  typed mandate、source-ordered compilation、deterministic validation、least-privileged execution 与 instruction-to-
  settlement trace 能暴露并减少若干运行层解释错误；官方合约文档独立支持 authority separation 与 onchain guards。
  长期价值不是某个 prompt 句子，而是 **mandate specification、proposal、authorization、settlement 和 evidence 必须
  由不同 owner 承担，并共享可回放 identity**。structured recent state 在高度动态环境中也比无界 semantic memory
  更易保持 provenance，但这只是该 deployment 的设计观察。
- **What It Does Not Prove / Limitations / Threats**：论文 abstract 的 99.9% 是“policy-valid submitted transactions”
  的 settlement 条件率；malformed/rejected proposals 不在 denominator，故不是全 invocations 的端到端 mandate
  success，更不是收益、安全或正确交易率。内部 EVM 99.9% 又是不同、未公开的 construction eval。论文没有
  public raw traces/code/replay/figure data、independent audit、randomized production comparison、model/harness factorial、
  user-intent ground truth 或 privacy/security red-team。一个 12-token、2.3% fee、21-day tournament 不能外推到
  开放市场、其他 action space/model/language/venue；4.2× profitability association、Chinese/English difference、
  cascades 与 92.9% two-sided windows 均受 user selection、strategy specificity、shared market/prompt/state 等混杂。
  reasoning classifier 只观察 visible trace，也不能证明内部 computation faithfulness。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：control surface 与 compiler 提高可诊断性，却
  新增 mandate conflict、template precedence、numeric hardening、prompt-order sensitivity、state freshness、hash-to-
  content availability、validator false reject、contract upgrade/role compromise、offchain/onchain split-brain、privacy/
  public-strategy leakage 与 trace-retention成本。过窄权限限制 blast radius，也可能阻断合法 recovery；冻结 harness
  提高 attribution，却延迟生产修复。简单只读 advisor、人工确认交易或 deterministic rules 在低频、高风险、规则
  稳定场景仍更合理；open-ended memory/RAG 在状态相对静态且 provenance/expiry 可靠时也没有被本论文否定。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：Ch80 是唯一 owner，关系为 `Layering /
  Dependency`：text advisor -> prompt-only action loop -> typed proposal + deterministic guard -> mandate-to-settlement
  evidence graph。已完整阅读 Ch79～80，并核对 Ch68、Ch77 的既有 boundary：Ch79 已明确 connectivity 不授予
  authorization；Ch68 已拥有 least-privilege tool executor；Ch77 已拥有 durable state、approval、idempotency 与
  side-effect evidence。Ch80 已有三个平面、Agent definition/run identity、policy、trajectory evaluation 与 replay，
  但尚未把 **mandate correctness、proposal validity、settlement success 三个不同 denominator** 与 authority chain
  明确连成生产控制闭环，因此存在真实 refinement 缺口；Ch68/77 只接短 handoff，避免重复机制。
- **Final Disposition / Changed Files / Open Questions**：28/30；provisional `Refine — Existing Argument
  (Experimental)` / Ch80，Ch68/Ch77 short handoff。Historical Books Gate 关闭，不修改 Books；只同步 W18、
  年度索引、Learning State 与 2026-08-10 Daily。待验证：公开 immutable prompt/compiler/runtime/contract manifests、
  raw/replay trace 与 figure data、rejection-inclusive end-to-end denominator、human intent audit、randomized prompt/
  harness/model ablation、latency/cost/SLO、validator false reject、role/upgrade/rollback incident tests，以及跨 venue/
  model/action-space 的独立复现。

### Visual Generation in the New Era — 24/30

- **Candidate / Week / Score / Source Family / Type**：`VISUAL-GENERATION-CAPABILITY-TAXONOMY`；W18；
  `TN 4 / SI 4 / PV 4 / SR 3 / PR 5 / L 4 = 24/30`。它是 129 页的 evolving roadmap / survey，
  不是发布新模型、benchmark 或可复现实验系统的机制论文。
- **Event / Revision / Direct Sources / Access**：arXiv:2604.28185 v1 于 2026-04-30 17:59 UTC first-public，
  v2 于 2026-06-14 修订。事件归 W18；本轮以 v1 HTML 作为 event-time 主证据，v2 metadata 只用于 revision
  核验。已阅读全文、全部图表/公式/案例、结论与 relevant appendix/reference surface，并联合核对作者
  GitHub 的 taxonomy、stress-tests、frontiers 与 reading-list artifact。仓库明确是持续更新的 living roadmap，
  当前无 tag/release 或 event-time frozen artifact，因此 current docs 只能核验作者的现行 taxonomy，不能倒写
  成 4 月 30 日已冻结的评测资产。
- **Full-read Coverage**：Introduction、五级 taxonomy、GAN/diffusion-flow/autoregressive/hybrid 与 unified
  understanding-generation 架构、tokenizer/VAE/backbone/conditioning/fusion、pretraining/SFT/RL/reward、sampling/
  cache/quantization/distillation、data construction/filtering/evaluation/infra、application taxonomy、全部八类
  in-the-wild stress tests、Positions and Frontiers、Conclusion，以及作者仓库的三份对应文档。论文没有独立
  implementation/evaluation appendix；案例 prompt、raw response、seed、judge protocol 与可重跑 harness 未形成
  公开的 immutable package。
- **Original Problem / Previous Design / Changed Constraint**：FID、CLIP alignment 与视觉偏好对一次性自然图像
  很合理，因为早期目标是 distributional plausibility。约束变化后，输出开始包含文字、地图、化学结构、UI、
  多轮编辑与 action-conditioned rollout；此时“看起来合理”可以同时违反计数、坐标、拓扑、符号、持续状态或
  因果后果。评价对象遂从 pixel sample 扩展为带 typed constraints、state 与 downstream use 的 artifact/trajectory。
- **Mechanism / State Ownership / Control and Data Flow**：作者用 L1 Atomic、L2 Conditional、L3 In-Context、
  L4 Agentic、L5 World-Modeling 组织能力，并主张 evaluator 应按约束类型选择 OCR、graph parser、chemistry/
  geometry validator、coordinate checker、simulator 或 action-faithfulness metric。长期可复用的系统流是
  `request constraints -> structured plan/state -> renderer proposal -> type-specific parser/verifier -> revise or
  commit -> evidence`。用户/task specification 拥有约束，generator 拥有候选 pixels，显式 memory/IR 拥有跨轮
  state，tool/verifier 拥有结构或领域判据，evaluation system 拥有 verdict 与 uncertainty；模型自己的解释不
  自动拥有 ground-truth authority。
- **Implementation / Evaluation Contract**：本文没有统一训练或 serving implementation，也没有跨模型的硬件、
  precision、batch、concurrency、latency/SLO 合同。Section 7 是选取的 qualitative diagnostic probes：metro-map
  单例中 GPT-Image-2 生成约 13m15s、GPT-5.5 post-hoc 检查约 9s；restoration 每类只取一个样本，未报告 PSNR/
  SSIM；多轮编辑、物理、coding、scientific diagram 与 high-level vision 也没有统一 seed、blinding、CI 或
  ground-truth scorer。因而数字和截图只能说明“这些 failure mode 可以发生”，不能形成模型排行榜或发生率。
- **What the Evidence Proves**：survey 与 artifact 支持一种有用的 capability/evaluator taxonomy：perceptual
  plausibility、constraint faithfulness、state persistence、closed-loop verification 与 causal/action faithfulness 是
  不同证据层，不能由单一 similarity 或 model-judge score 互相替代。作者展示的若干案例具体说明视觉上专业的
  产物仍可违反 graph/coordinate/text constraints，也说明 generation 与 verification 可以是不同系统角色。
- **What It Does Not Prove / Claim Boundary**：五级结构是作者的组织框架，不是经 benchmark 验证的单调能力
  ladder；L5 不必在单一 monolithic model 中“包含”全部低层能力。Section 3.3 明确是对闭源 frontier 的
  `speculative reading`：upstream VLM、dual-path encoder、generation-time understanding control 与 silent verifier
  loop 均为可证伪猜想，不能写成 Nano Banana 或 GPT-Image-2 的实现事实。selected images 不能证明 emergent
  world model、true physics、VAE round-trip 或 Markov shortcut；论文自己也总结为“causal artifacts but no true
  physics”。若没有 architecture、raw runs 和 causal ablation，观察到的 drift 只能证明 failure，不能定位机制。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：typed IR、specialized validator 与 retry loop
  提高结构正确性，却增加 parser false reject/accept、validator blind spot、shared generator-judge bias、latency、
  cost、state/version ownership 与 rollback。对审美探索或低风险 one-shot generation，perceptual/human preference
  仍是合理主指标；对地图、CAD、科学图、world-model rollout 等结构化产物，必须叠加 task-specific hard checks。
  modular planner/parser/solver/renderer 更可验证但 handoff 多，end-to-end unified model 更灵活却更难归因，两者是
  共存分支而非必然替代。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：主 owner 应为 Ch62，Ch10 只保留 world-model
  action-faithfulness 的短连接；Ch38 不拥有该候选，因为 survey 未提供 runtime scheduling、kernel 或 serving
  contract。已完整阅读 Ch61～63，并核对 Ch9～10、Ch38。Ch62 已明确 `structured artifact -> executable
  verifier/simulator -> environment outcome`、task-specific scorer、verifier versioning 与“executable 不等于
  ground truth”；Ch10 已明确 pixel/video realism 不等于 intervention/long-horizon causal correctness。论文没有
  改变这些结论，也没有补出当前章节缺失的新机制。
- **Final Disposition / Changed Files / Open Questions**：`No Change — Already Covered`。只把 primary-source
  evidence、猜想边界和章节级去重写入 W18、年度索引、Learning State 与 2026-08-10 Daily；Historical Books
  Gate 关闭，不修改 Books。待验证：event-time frozen prompts/raw generations、model/version/sampling identities、
  constraint-specific ground truth、blind multi-rater calibration、可重跑 parser/verifier、失败率与 uncertainty、
  closed-source mechanism disclosure，以及五级 taxonomy 在跨模型/跨任务上的独立验证。

### Temporal Attribution Review — Edit-R1 / Verifier-Based RL in Image Editing

- **Source Family / First-public Reconciliation**：HF W18 页面以 arXiv:2604.27505 v1（2026-04-30）收录
  `Leveraging Verifier-Based Reinforcement Learning in Image Editing`；但官方 OpenReview 的同一论文家族
  `Edit-R1: Unleashing Reasoning-Based Reinforcement Learning for Image Editing` 已于 2025-09-03 公开，
  2025-11-14 修订，状态为 ICLR 2026 withdrawn submission。两版拥有相同九位作者、核心摘要、
  principle decomposition、cold-start SFT、GCPO、RRM-guided downstream GRPO 与主要模型/数据规模，故是同一
  Source Family，不是 W18 新机制事件。arXiv v2 于 2026-05-20 修订；CVPR 2026 publication 是后续 publication
  node，不能重置 first-public date。
- **Mechanism Read / Evidence Boundary**：已阅读 arXiv v1 全文、公式、全部实验表、system prompts、human
  evaluation 与 qualitative appendices，并与早期 OpenReview paper 核对。机制把单一 holistic edit score 拆为
  Keep / Follow / Quality principles；Seed-1.5-VL 生成 principles，多个 VLM 产生 `think+score` trajectories，
  另一 Seed-1.5-VL verifier 选择 SFT trace；GCPO 再把 10K human pairwise preference 转换为 preferred/
  non-preferred 两组 rollout 的 cross-group win/loss ratio 和 within-group advantages，最后以该 RRM 为
  non-differentiable reward，通过 Flow-GRPO 优化 FLUX.Kontext 与 Qwen-Image-Edit。
- **Evaluation / Limitations**：公开结果支持该 pipeline 在作者的 internal 5K pairwise benchmark、
  EditRewardBench 与 GPT-4.1-scored GEdit-Bench-EN 上有受限增量；但 internal set 与 SFT source 来自同一 public
  editing benchmark，ambiguous `same` pairs 被排除，annotation count/agreement/CI 未披露。principle generator、
  trace generator/filter 和 downstream evaluator 共享 Seed/VLM family 或 model-judge assumptions；“external
  verification”不是独立 ground truth。论文未披露 GPU、precision、training steps、learning rate、rollout N、
  prompt-variant allocation、packed-inference cost、seeds 或完整 human-study sample/annotator protocol，也没有
  public code/model/data artifact。Appendix G 的文字与逐项 0/1 listing 还存在 loser/winner/hat-preservation
  叙述不一致，提醒 reasoning trace 的可读性不能替代 label consistency audit。
- **ROADMAP / Disposition**：若以后在 2025 backlog 中整合，主 owner 应为 Ch29（preference-to-pointwise
  verifier optimization），Ch62 接 rubric/scorer provenance handoff，Ch27 只接 visual preference objective；
  Ch62 已覆盖 rubric formation、criterion execution、aggregation 与 decision policy 分层。当前 disposition 为
  `Out of W18 — 2025 Backlog / Full Mechanism Review Complete`；不进入 W18 score denominator，不修改 Books，
  也不回拉 Historical Forward Cursor。

### Full Source Review — Meta-CoT: Enhancing Granularity and Generalization in Image Editing — 26/30

- **Candidate / Week / Score / Source Family / Type**：`METACOT-IMAGE-EDITING-PLAN-CONSISTENCY`；
  W18；`5+4+4+4+5+4=26/30`；CVPR 2026 / arXiv experimental research。
- **Event Date / First-public / Revision History**：arXiv:2604.24625 只有 v1，于 2026-04-27
  15:52:48 UTC first-public，事件归 W18。CVPR acceptance 与 project update 是 publication/artifact
  状态，不创建新的 Source Family。
- **Direct / Related Primary Sources**：完整读取 arXiv v1 HTML 主文的 metadata、Abstract、Introduction、
  Related Work、Method、公式/算法、training、evaluation、ablation、qualitative analysis、Conclusion 与
  HTML 可见表图；并核对作者 project page、GitHub repository、Hugging Face model 与 21-task benchmark
  surface。论文引用的 supplement 未出现在 arXiv HTML，CVF 与 GitHub 的独立重开又被现有浏览器权限
  拒绝，因此 supplement 中的理论细节和 current artifact release state 明确记为 `Not Independently
  Verified`，不以作者正文摘要代替已读附件。
- **Access and Verification Status / Full-read Coverage**：`Primary Main Paper Complete; Supplement and
  Artifact Release Boundary Partially Blocked`。主文中的方法、公式、训练/评估表、ablation 与结论已逐节
  审计；公开仓库当时无 tag/release，README 的 checkpoint/benchmark/example-data/SFT/RL TODO 与可见
  SFT/inference 文件并存，model page 无 model card，benchmark 约 4.56 GB 但无 dataset card。它们可证明
  artifact surface 存在，不能证明 paper-run checkpoint、RL code、数据生成器或 frozen evaluation bundle
  已完整发布。
- **Original Problem / Why the Previous Design Was Reasonable**：传统 instruction-conditioned image editing
  直接把 source image 与 instruction 映射到 target pixels；当目标局部、指令明确且 base model 已有足够视觉
  理解时，这条路径最短，也避免生成额外 reasoning token 与 judge。通用自然语言 CoT 看似能补充计划，
  却可能把编辑任务写成长叙述、漏掉多个 target，甚至在论文自身对照中使 Bagel 平均分从 5.673 降到
  5.307。因此问题不是“有没有 CoT”，而是 intermediate plan 是否具有可约束的任务结构并与最终图像一致。
- **Changed Constraint / Principle**：复杂、多目标、空间和视觉理解型编辑要求系统同时决定“做哪类操作、
  对哪些 target 做或不做、需要什么理解能力”，而 pixel-level outcome 又不能直接说明计划是否忠实执行。
  论文把监督单位从自由文本 explanation 收紧为 `(task, target, required understanding)` triplet，并将 task
  映射到 Addition、Deletion、Replacement、Camera Motion、Position Change 五类 meta-tasks。这里的长期
  原则是 **中间推理必须成为有 schema、有 verifier 的 action contract**；“五类操作构成所有编辑的 basis”
  仍是作者经验 taxonomy，不是已被主文证明的完备本体。
- **Mechanism / State Ownership / Control Flow / Data Flow**：SFT 阶段先由 Qwen2.5 预测 task、
  Gemini-2.5-Flash 校验，再由 Qwen2.5-VL 基于 source/target/instruction/task 生成 Meta-CoT 并过滤；CoT
  依次输出 task/meta-task summary、task-specific thinking，再遍历所有 targets 作 edit/no-edit 决策。系统另混入
  100K visual-understanding samples，让 `required understanding` 不只依赖 editing pairs。RL 阶段使用
  CoT-Edit Consistency（CEC）reward：Qwen2.5-VL 从 task 与 target 两个方向给计划—结果一致性打 0～10 分，
  再进入 Flow-GRPO。Policy/rollout version、source/instruction/target identity、Meta-CoT schema、judge model/
  prompt、CEC calibration、diffusion timestep 与 frozen/trainable module mask 都是训练状态；若只保存 image
  pairs 与 checkpoint，不能复原实际 objective。
- **Implementation Details**：实现以 Bagel 为基座。SFT 同时更新 understanding expert、generation expert
  与 image encoder；RL 中冻结 understanding encoder，只训练 generation expert，因为作者报告 joint RL 会
  不稳定并损伤 reasoning。Flow-GRPO 只优化 early denoising timesteps，让 reward 聚焦 semantic fidelity，
  而不是把晚期 texture/artifact shaping 混入同一 credit signal。CEC 用 500 条 SFT 样本和四名人工标注者
  校准：range 小于 3 时平均四分，否则平均最接近的三分；迭代调 prompt 直到 Pearson `r>=0.8`、
  `MAE<=2.5`。这是一种受控 calibration procedure，不等于 CEC 成为独立 ground truth。
- **Evaluation Contract**：SFT 使用约 1.5M image-instruction-CoT pairs、10K steps、48 GPUs，并混入 100K
  understanding samples；RL 使用 20K editing examples、500 steps、32 GPUs、group size `G=24`、
  `beta=0.04`。公开主文未披露 GPU 型号、precision、optimizer、learning rate、effective batch、seeds、
  throughput 或 SLO。21-task benchmark 合并 GEdit 的 11 类、RiseBench 的 4 类、ComplexEdit 1 类与五个
  新类（每类 100 样本），统一由 GPT-4.1/VIEScore 评分；ImgEdit 为 734 个 real-world cases，同样以
  GPT-4.1 三指标为主。训练数据由 Gemini-2.5-Flash、FLUX Kontext、Qwen-Image、GPT Image、GPT-4.1 与
  human filtering 共同形成，训练与评估因此不是独立、开源、可冻结的 verifier chain。
- **Baselines / Ablations / Sensitivity / Overhead**：主表比较 Bagel without think、generic think、edit-only、
  Meta-CoT SFT 与 SFT+RL；平均分依次为 5.673、5.307、5.538、6.224、6.415。结果支持“结构化计划优于
  该设置下的 generic think”，也显示主要增益来自 SFT/data/decomposition，RL 对 SFT 的增量较小。
  Ablation 显示五类 meta-tasks 在作者 21-task set 上接近 full-data variant，减少类别损伤 instruction
  following，继续增加类别收益有限；移除 Task Thinking 或 understanding data 会回退。没有公开多 seed
  interval、独立 judge、human-vs-judge disagreement、训练成本分解或部署 latency；project page 的 ImgEdit
  表格排版还与论文主表不稳定，故数字只以 paper table 为准。
- **What the Evidence Proves / Does Not Prove**：作者实验支持在 Bagel、指定合成数据与 judge contract 下，
  显式 task/target plan、understanding mixture 与 CEC-guided early-timestep RL 可以优于其直接编辑和 generic
  CoT baselines。它不证明自然语言 CoT 忠实反映模型内部推理，不证明五种 primitive 覆盖所有真实编辑，
  不证明 CEC 与人类偏好在部署分布上校准，也不证明 RL 而非大规模合成 SFT 是主要因果来源。项目页的
  `+15.8%` 与主文约 `15.7%` 的舍入/口径差异也不能脱离 baseline 与 judge contract 传播。
- **Limitations / Threats / Trade-offs / New Failure Modes**：获得更可审计的 plan-action interface，代价是
  额外 reasoning tokens、数据生成/过滤链、闭源 teacher/judge 依赖与 plan/pixel 双重优化。错误 taxonomy
  会系统性漏掉操作；target traversal 可变成长而机械的模板；CEC 可能奖励语言—图像表面一致而非真实
  用户意图；冻结 understanding side 提高 RL 稳定性，却阻止它适应 rollout 中暴露的新视觉错误；只优化
  early timesteps 又可能保留晚期 artifact。Judge prompt drift、同源模型偏差、训练数据污染、supplement
  不可核验与不完整 artifact 使复现和因果归因进一步受限。
- **Where the Previous Design Still Applies / Evolution Relationship**：简单局部编辑、低 latency 或有可靠
  paired demonstrations 时，direct edit-only/SFT 仍更便宜、更少状态；可执行 geometry/CAD constraint 可用时，
  deterministic verifier 比 model-judge CoT 更强。Meta-CoT 与 direct editing 是 `Direct Evolution`，与
  SFT→GRPO 是 `Layering / Dependency`，与 Agent planning 只有 `Principle Reuse`，不能因为输出了文本计划
  就称为通用 Agent。
- **ROADMAP / Target and Adjacent Chapters / Existing Coverage / Decision**：已完整阅读 Ch25、Ch27～30，
  并检查 Ch62 scorer contract。Ch25 已覆盖 synthetic demonstration、teacher/filter bias 与 SFT objective；
  Ch27/29 已覆盖 model judge、verifier exploit、group rollout、reward identity 与多阶段 SFT→RL；Ch62 已
  覆盖 judge calibration、rubric/version、训练 reward 与独立 evaluation 分离。真正新增的章节候选是：
  **plan schema、action outcome 与 consistency reward 必须共享 identity；多模块 policy 可通过冻结一侧来换
  稳定性，但同时限制 joint adaptation**。故暂定 `Refine — Existing Argument (Experimental)` / Ch29，
  Ch25 与 Ch62 只接 short handoff。Historical Books Gate 关闭，本轮不修改 Books；supplement、GPU/
  precision、可用 RL code/checkpoint、独立 human evaluation 与 judge robustness 仍为 Open Questions。

### Full Source Review — Compliance versus Sensibility — 26/30

- **Candidate / Week / Score / Source Family / Type**：`REASONING-SCHEMA-CONTROLLABILITY`；W18；
  `TN 5 / SI 4 / PV 4 / SR 4 / PR 5 / L 4 = 26/30`；arXiv experimental research，当前标注
  `under review`，不是已经独立复现的 production control mechanism。
- **Event / Revision / Direct Sources / Access**：arXiv:2604.27251 v1 于 2026-04-29 22:55:40 UTC
  first-public，事件归 W18。arXiv body 受 saved browser permission 阻塞，但作者公开的 CC BY 4.0
  full-text manuscript 可完整读取；并以 arXiv metadata、Hugging Face paper record 与作者机构 publication
  index 交叉核对 title、authors 和 date。未发现 official code、weights、activation artifact 或 frozen run package。
- **Full-read Coverage**：已读 Abstract、Introduction、Background/Related Work、reasoning-conflict construction、
  deduction/induction/abduction definitions、datasets/models、CoT classification、confidence、linear probing、
  Contrastive Activation Addition（CAA）、全部主要结果与相关 appendices、judge validation、implementation
  details 和 Conclusion。论文没有独立 Limitations/Threats section；缺失项从实际 design/evaluation contract
  提取，而不是假定不存在。
- **Original Problem / Previous Design / Changed Constraint**：prompt-level instruction 通常被视为当前 task
  policy，在无需区分推理 schema 时是合理接口；但 task distribution 可能在参数中形成更强的默认模式。
  当指令要求使用与任务通常匹配模式不同的 deduction、induction 或 abduction 时，最终答案正确并不说明
  模型遵守了指定过程。约束从“输出是否正确”变成“内部/外显推理类型是否可辨、可控且不损害任务”。
- **Mechanism / State Ownership / Control and Data Flow**：论文构造 `task-suitable type t` 与
  `mandated type t'` 的 reasoning conflict，模型生成 CoT，独立 judge 将其归入 compliance/sensibility 类别；
  confidence 与 frozen hidden-state linear probe 观察冲突信号。CAA 用 matched compliant/non-compliant pairs
  在 residual stream 上求 mean-difference vector，并在生成每个 token 时把带 multiplier `mu` 的向量注入指定
  layer。task/prompt 拥有目标 schema，base model 拥有参数和 hidden state，probe 只拥有读出结果，steering
  controller 拥有 intervention policy，judge 拥有外部标签；可线性读出不等于 probe 找到了模型的唯一因果变量。
- **Implementation / Evaluation Contract**：覆盖 OLMo 3.1-32B-IT、OLMo 3-7B-IT、Llama 3.3-70B-IT、
  Llama 3.1-8B-IT、Qwen3-32B、Qwen3-8B、GPT-5.1 与 Gemini 3 Flash；任务来自 FOLIO、SPR、alphaNLI、
  RECV。其他模型主要由 GPT-5.1 judge，GPT-5.1 由 Gemini 3 Flash judge；360 个平衡样本由两位人工标注
  并经第三人裁决，reported kappa 为 0.83/0.84。probe 是冻结表示上的 L2 logistic regression；CAA 主实验只在
  OLMo 3-7B-IT，Llama 作为 appendix follow-up，重点层为 14～17。推理由 vLLM 执行，公开硬件为 GH200
  96GB、A100 80GB、MI300X 192GB，temperature 0.5、3 seeds；但没有完整 per-model batch/concurrency/SLO。
- **Evidence Proves / Does Not Prove**：实验支持在这些人工冲突任务和 judge contract 下，模型经常偏向
  task-suitable schema；指令 schema 在 hidden states 中容易被线性解码，而 compliance signal 更弱；正向
  steering 可在部分设置提高 compliance，代价可能是 accuracy、format adherence 或 task neglect，效果对层与
  multiplier 非单调。它不证明模型“主动选择”不服从，不证明 probe feature 是充分因果机制，也不证明摘要的
  `up to 29%` 可迁移到开放推理、生产 instruction hierarchy 或安全控制。confidence drop 也不是通用冲突检测器。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：activation steering 比重训便宜且可局部控制，
  但增加 layer/model/version coupling、方向估计数据污染、multiplier calibration、跨 token 累积和不可见性能
  回归；更强 compliance 可能放大错误指令。普通 prompt、SFT/RL alignment 与 external verifier 在黑盒 API、
  无 residual access、行为范围较广或需审计责任时仍合理；activation intervention 是额外分支，不是替代链。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：主 owner 是 Ch17，关系为 `Layering /
  Dependency`：residual stream 不再只承载 forward state，也成为受版本约束的 observation/intervention surface。
  已读 Ch16～18，并核对 Ch27～28、Ch62。Ch17 已提醒“可读出不等于因果使用”，但尚未系统连接 probe、
  intervention、behavior regression 与 checkpoint identity，存在真实 refinement 缺口；Ch27 只接 alignment
  objective，Ch62 只接 independent judge/calibration，避免复制论文案例。
- **Final Disposition / Changed Files / Open Questions**：26/30；provisional `Refine — Existing Argument
  (Experimental)` / Ch17，Ch27/62 short handoff。Historical Books Gate 关闭，不修改 Books。待验证：公开
  code/activation vectors、judge prompts/raw labels、per-dataset counts/CI、cross-model causal replication、
  adversarial instruction hierarchy、长期 generation drift，以及 compliance gain 与 task loss 的完整 Pareto curve。

### Full Source Review — Zero-to-CAD — 28/30

- **Candidate / Week / Score / Source Family / Type**：`ZERO-TO-CAD-EXECUTABLE-SYNTHETIC-PROGRAMS`；
  W18；`TN 5 / SI 5 / PV 5 / SR 4 / PR 5 / L 4 = 28/30`；agentic synthetic-data system / TMLR
  under-review manuscript。它是 data-generation、workflow 与 downstream bootstrapping 的同一 Source Family，
  不是把 100K/1M dataset、paper 和 model 各计一次事件。
- **Event / Revision / Direct Sources / Access**：arXiv:2604.24479 v1 于 2026-04-27 13:46:41 UTC
  first-public，归 W18。已完整阅读作者公开的 CC BY 4.0 manuscript，并核对 arXiv metadata、OpenReview
  record 与 Autodesk AI Lab 官方 Hugging Face dataset card/schema。当前 artifact 是可变现行状态，不能当作
  4 月 27 日 immutable snapshot；GitHub code path 未能独立访问，明确记为 `Repository Not Independently
  Verified`，不以论文声称替代代码审计。
- **Full-read Coverage**：已读 Motivation、Related Work、Ray/vLLM distributed architecture、三种 tools、
  two-stage generation、repair loop、三层 validation、categorization/reference snippets、compute、dataset
  statistics/failures、CAD-Recode/ABC comparison、Image-to-Sequence setup/results、Conclusion、generation
  distributions、完整 training hyperparameters、system prompts 与 example program；并核对 100K/1M dataset
  fields、splits、license、DINOv3 embeddings 和 selection surface。
- **Original Problem / Previous Design / Changed Constraint**：B-Rep/mesh 数据只保留最终 geometry，在 shape
  generation 上合理，却丢失可重放、可编辑的 construction history；DeepCAD/Fusion 360 等 sequence 数据又较小
  或受 sketch-and-extrude vocabulary 限制。真实 procedural histories 难以收集，约束遂从“更多 shape”转为
  “在没有真实 history 时生成可执行程序，并保存每一步为什么被接受的证据”。
- **Mechanism / Ownership / Control and Data Flow**：stage 1 让 gpt-oss-120b 按 65 类生成 dimension-free
  descriptions，batch 内去重；stage 2 的 tool-equipped worker 生成 CadQuery、在 isolated subprocess 执行，
  根据 stack trace、TF-IDF documentation retrieval 或 regex grep 修复，单 attempt 最多 10 rollout turns、单任务
  最多 100 attempts。validation 依次检查 execution、topology/connectivity/至少 7 个 B-Rep faces/positive volume、
  STL/STEP export。coordinator/Ray cluster 拥有调度与失败恢复，worker 拥有 transient rollout state，validator
  拥有 acceptance，cloud storage 拥有 code/mesh/STEP/metadata artifact identity；LLM 不拥有 ground truth。
- **Implementation / Evaluation Contract**：合成约一周，LLM inference 动态使用 2～80 GPUs，CadQuery/
  function workers 峰值约 3,000 CPU cores；最终 999,633 accepted sequences，累计处理 60.2B tokens，首轮
  success 22.3%，平均/中位 attempts 3.30/3。下游 Qwen3-VL-2B-Instruct 用 8 张 256×256 views 做 full
  fine-tuning：16×H100 80GB、DDP、bf16、max length 4096、per-GPU batch 1、effective batch 16、3 epochs。
  评测用 executable success、64^3 voxel IoU（45-degree rotation 取最大）和 Chamfer distance；IoU/CD 只在
  successful samples 上计算。GPT-5.2 因 API 成本只测 in-domain 1,000 子集，Qwen 测 10,000；ABC OOD 为
  1,000 个 7～100-face shapes。
- **Evidence Proves**：公开结果支持该 pipeline 能在其 validator ontology 下规模化产生可执行、单一连通、
  非平凡且可导出的 CadQuery artifacts；多数 accepted samples 经 repair 而非一次生成。fine-tuned 2B 在作者
  contract 下从 base 的 6.6% executable success 提升到 82.1%，并在 ABC OOD 保持 61.0%，说明纯 synthetic
  sequence supervision 可以启动一种受限的 image-to-program capability。官方 dataset 还提供 code、operation
  metadata、八视图、STL/STEP 和 embeddings，支持 artifact-level inspection。
- **What It Does Not Prove / Limitations / Threats**：validation 不检查完整 DFM、材料、公差、载荷、装配或真实
  用户意图；named variables/logical order 没有人类可读性 user study。单连通与 face threshold 是 admission
  rule，因此相关质量数字部分由构造保证。论文明确没有对 CAD-Recode/DeepCAD 做 matched dataset-quality
  ablation；vocabulary 不同使直接 operation comparison 不成立。IoU/CD 排除执行失败样本且 rotation 取最大，
  GPT 与 Qwen sample size 不同；setup、repair 和 validation 共享 ontology，可能系统性保留 locally plausible
  but globally incoherent、scale drift 或不可制造设计。synthetic provenance/attribution 仍未解决。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：可执行 feedback 把语言 plausibility 提升为
  bounded program validity，但引入 sandbox escape/timeout、tool/version drift、validator gaming、repair cost、
  attempt-selection bias、artifact storage 与 license/provenance state。轻量 TF-IDF/grep 在固定 API 文档上比复杂
  RAG 成本低且可复现，开放知识域则未必足够。真实 construction histories 在制造约束、专家意图和分布校准
  上仍不可替代；直接 B-Rep/mesh 在无需编辑 timeline 的 geometry task 中也仍合理。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：主 owner 是 Ch23，关系为 `Direct
  Evolution`：generate-then-judge synthetic data -> executable specification + repair trace + artifact lineage。
  已读 Ch22～24、Ch61～63、Ch76～78。Ch23 已覆盖 constraint-derived synthesis，但尚未明确“开放程序空间中
  validator 逐层收紧、repair trajectory 与 accepted artifact 必须共同版本化”的机制，因此存在真实 refinement
  缺口；Ch77 只接 evaluator-driven repair/workflow，Ch62 只接 success 与 conditional geometry metrics 的
  denominator，避免把同一案例重复写三遍。
- **Final Disposition / Changed Files / Open Questions**：28/30；provisional `Refine — Existing Argument
  (Experimental)` / Ch23，Ch77/62 short handoff。Historical Books Gate 关闭，不修改 Books。待验证：event-time
  code commit、完整 generator/worker/security config、failed-run release、validator thresholds、human editability/
  manufacturability audit、dataset provenance/attribution、matched real-history baseline、joint success-quality metric、
  multiple training seeds，以及 current 100K/1M artifact 与 paper split/selection 的 immutable mapping。

### Mistral Workflows public preview — 28/30

- **Candidate / Week / Score**：Mistral Workflows，2026-W18，28/30（TN 3 / SI 5 / PV 5 /
  SR 5 / PR 5 / L 5）。Technical novelty 只给 3 分：durable execution 与 replay 的底层思想来自既有
  workflow 系统，W18 新事件是把它作为 Mistral Studio 的 AI orchestration product surface 发布，不能把
  产品集成误写成新的一致性理论。
- **Source Family / Date / Access**：`MISTRAL-WORKFLOWS-2026-04-27`。Direct primary source 是
  Mistral 2026-04-27 public-preview announcement；related primary sources 是当前官方 Overview、Workflow、
  Activity、Event、Waiting、Worker、Deployment、Hardened Deployment、Connector/OBO 与 API 文档。
  announcement 与当前 docs 均已读取；docs 是 2026-08-10 可见的 current surface，不是冻结的 launch-day
  snapshot，因此只能核验当前公开机制和演进边界，不能断言所有字段在 4 月 27 日已经存在或保持不变。
- **Original Problem / Previous Design / Changed Constraint**：单次 LLM SDK call 或进程内 `while` loop
  对短、无副作用任务合理：状态局部、失败可整次重来、没有跨小时 approval。业务流程一旦跨多模型、
  external API、人工输入和长等待，process restart、timeout 后的 ambiguous side effect、重复执行和无 trace
  使这一旧设计失效。变化的约束不是“模型更聪明”，而是 run lifetime、authority、failure domain 与
  audit obligation 扩大。
- **Mechanism / State Ownership**：Workflow code 只拥有 deterministic orchestration；event history 由
  platform 持久化并在 replay 时重建控制状态。Activity 拥有 I/O、model/tool call 与其他 nondeterministic
  side effects，必须按可重试/idempotent contract 设计。Worker 是可替换执行者，不拥有 authoritative run
  state；signal / `wait_condition` / `wait_for_input` 把外部事件转化为 durable transition；deployment 拥有
  worker group 与 execution routing；OBO execution 捕获 triggering-user identity，并以短期 credential
  访问 identity-scoped connectors。
- **Control Flow / Data Flow**：`execute workflow → schedule deterministic workflow task → schedule activity
  → persist completion/event → replay from history after worker loss → wait/resume on signal → terminal result`。
  replay 重新运行 orchestration code，但已完成 activity 读取 recorded result，不重复执行。长时程 history
  接近上限时可以 continue-as-new，把必要 state 带到新 history；较大 payload 需外置 object storage，而不是
  把 blob 当 workflow state。
- **Implementation / Failure Semantics**：官方当前文档明确 workflow/activity 分离、默认 determinism
  sandbox、activity retry/backoff、worker heartbeat/reassignment、HITL timeout、OpenTelemetry/event history、
  deployment routing 与 hardened registration。公开限制包括 workflow 两次 activity 之间 2 秒、单次 input/
  output 各 2 MB、history 51,200 events 或 50 MB；同名 workflow 被多个 deployment 注册会产生 routing
  ambiguity，同一 deployment 内不同版本的同名 workflow 还可能造成不可预测执行，OBO 因而要求 hardened
  deployment。这些是 current docs 的版本事实，不外推成所有 durable runtime 的固定数值。
- **Evaluation Contract / Evidence Boundary**：announcement 给出 cargo release、KYC、IT support 等客户
  narrative，能证明产品定位与 intended control flow，不能替代 workload、failure-injection、recovery
  correctness、duplicate-side-effect、tail latency、availability、cost 或 security evaluation。官方未披露
  hardware、run count、concurrency、model/precision、input/output distribution、SLO、baseline、ablation、
  incident denominator 或 independent reproduction。因此“already running in production”不是通用可靠性
  benchmark，也不能证明 exactly-once external effects。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：durability 得到 crash recovery、长期
  wait 与 auditability，却新增 history/schema migration、determinism divergence、activity granularity、retry
  amplification、idempotency key、signal dedup/staleness、deployment/version routing、credential delegation、
  retention 与 vendor/runtime coupling。单次无副作用 call、短 deterministic pipeline，或已有成熟 Temporal/
  queue/state-machine 平台的团队，仍可保留旧分支；“AI-specific packaging”本身不是替换理由。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Layering / Dependency`：LLM/Agent node 叠加在
  durable workflow runtime 上，而不是 Agent autonomy 替代 workflow。主 owner 为 Ch77；已重读 Ch76～78
  与 Ch80。Ch77 已具体写出 deterministic spine、event-history replay、activity/event boundary、retry/
  idempotency/compensation、approval state 与 external events；Ch80 已写 run identity、control/execution/
  evidence plane、OBO-like authority、observability/replay 与 rollout/rollback。
- **Final Disposition / Changed Files / Open Questions**：`No Change — Already Covered`。本候选为已有论点
  提供一个 version-grounded vendor implementation，但没有新增长期机制缺口，不为制造 diff 重复写入
  Books。待核验 launch-day SDK/docs snapshot、Temporal service boundary、history storage/retention、activity
  delivery guarantee、version pinning/migration、multi-region failover、customer workload denominator 与
  independent recovery/security tests。Historical Books Gate 保持关闭。

### Z.ai Scaling Pain of Coding Agent Serving — 29/30

- **Candidate / Week / Score**：Scaling Pain of Coding Agent Serving: Lessons from Debugging GLM-5 at
  Scale，2026-W18，29/30（TN 5 / SI 5 / PV 5 / SR 4 / PR 5 / L 5）。Source Reliability 为 4：这是
  operator 自己的 incident/engineering report，机制具体，但缺少 frozen code revision、raw trace、完整
  denominator 与 independent reproduction。
- **Source Family / Date / Access**：`ZAI-GLM5-SERVING-CORRECTNESS-2026-04-30`。Direct primary source
  为 Z.ai 2026-04-30 官方全文；related source 是 2026-02-12 GLM-5 官方 release/workload context。全文的
  incident timeline、两类 root cause、fix、LayerSplit 与 evaluation numbers 已读取。文中所称 SGLang PR
  #22811 因当前 GitHub saved permission 无法独立读取，故只记录为作者声明，不把 PR merge/code behavior
  当作已验证事实。
- **Original Problem / Previous Design / Changed Constraint**：为约束 TTFT，Decode timeout 后回收 KV
  slot；为缓解长前缀容量压力，HiCache 将 CPU→GPU load 与 forward overlap。这两项旧设计分别以 tail
  latency 和吞吐为目标，在低压力/短上下文下合理。Coding Agent workload 把平均输入推到作者所述 70K+
  tokens，并同时提高 concurrency、prefix reuse、Prefill backlog 与 Decode KV pressure；原先隐含的
  “abort 已全局生效”和“load 在 use 前完成”不再成立，性能优化跨越了 correctness boundary。
- **Mechanism / State Ownership**：第一项故障中，Decode 因 timeout abort Req1 并回收/复用其 KV address，
  但 abort 未传播到 Prefill；Req1 已发出的 RDMA write 和 Prefill computation 仍继续，随后覆盖复用同一
  address 的 Req2 KV。修复把 reclaim authority 收回到跨阶段 handshake：Decode 发 abort，Prefill 只有在
  尚未发 write 或全部 write completion 后返回 safe-to-reclaim，Decode 收到确认后才能 reuse。第二项故障
  是 HiCache Load Stream 与 Forward Stream 缺少 dependency，Indexer kernel read-before-ready；修复是在
  Indexer launch 前加入显式 load-completion synchronization。
- **Control Flow / Data Flow**：正确路径从 `request identity → Prefill queue/forward → RDMA KV write →
  destination visibility → Decode use → terminal/reclaim` 扩展为带 abort epoch 的状态机。任何 timeout 都
  只能撤销 future work，不能把 in-flight DMA 当作已经消失；cache address 的新 owner 必须等旧 generation
  的 writer 完成或被可靠 fence。HiCache 同样要求 `load complete → indexer ready → sparse attention`，
  不能只因两个 CUDA streams 可以 overlap 就省略 data dependency。
- **Observability Mechanism**：作者将 speculative decoding 的 `spec_accept_length` 与 `spec_accept_rate`
  从性能指标复用为 output-state anomaly signal：超过 128 generated tokens 后，accept length 持续低于
  1.4，或 accept rate 高于 0.96 时主动终止并交回 load balancer retry。低 acceptance 被解释为 draft/
  target KV mismatch，高 acceptance 与 corrupted-state repetition 相关。该阈值只是一个 production
  operating point；它是 detection/mitigation，不是 root-cause proof，也可能制造 retry amplification。
- **LayerSplit / Alternatives**：在修 correctness 后，作者没有只扩大 timeout 或关闭 overlap，而是处理
  Prefill bottleneck：Context Parallel ranks 不再各自保存全层 KV，每个 GPU 只拥有部分 layers；计算某层
  前由 owner broadcast KV，并把通信与 indexer computation overlap。作者称额外显性通信主要是约为 KV
  八分之一的 indexer cache。这是用 layer ownership 换 per-GPU capacity 的分支，会新增 broadcast、
  ownership/layout、collective failure 与 overlap-ordering contract；关闭 PD/HiCache、扩大资源或保留复制
  仍是更简单但成本更高的旧分支。
- **Evaluation Contract / What It Proves**：作者先重复 replay 相同 bad cases 数百次仍无法复现，再用匿名
  production log 尽量保留 concurrency/timing，并调整 P/D ratio、Prefill backlog 与 Decode KV pressure，
  得到约每 10,000 requests 3～5 次异常。修复第一项 race 后，文中另报异常率由约 0.1% 降至 0.03%
  以下；这两个起始 denominator/阶段没有被完整对齐，不能合并成单一统计。LayerSplit 测试绑定 90%
  cache-hit、40K～120K request length，并报告 10%～132% throughput gain；未披露 hardware、GPU/rank
  数、model revision/precision、batch/concurrency、TTFT/TPOT SLO、置信区间与 baseline tuning。
- **What It Does Not Prove / Limitations**：报告证明作者环境中至少存在两类 pressure-triggered state race，
  并给出与症状下降相关的 fixes；它不证明异常都来自这两类 race、不证明阈值可跨 model/runtime 使用、
  不证明 retry 后一定安全，也不证明 LayerSplit 在低 hit、短 context、弱网络或不同 sparse-attention
  layout 下获益。数亿日请求是 scale claim，不是公开 denominator；garbled/rare-character detector 的
  false-positive/false-negative、retry outcome、用户影响与 residual incidents 未披露。
- **Trade-offs / Failure Modes / Previous Design Still Applies**：显式 fence 提高 correctness，却延迟
  reclaim 并可能放大 timeout 占用；online detector 提供快速 containment，却会误杀健康请求、形成 retry
  storm 或掩盖根因；LayerSplit 节省 residency，却增加 collective traffic、rank coupling 与 layout/version
  compatibility。短 prompt、低 concurrency、co-located P/D、无 async swap 或 memory 充足时，旧的简单
  lifecycle 仍可能更稳。新的设计压力是把 request generation、DMA completion、address epoch、cache level、
  model/draft revision 与 retry lineage 放入同一可观测 identity。
- **Evolution Relationship / ROADMAP / Adjacent Chapters**：`Direct Refinement`：PD 从 performance-oriented
  phase separation 演进为 correctness-carrying state transfer。主 owner 为 Ch51；已重读 Ch44、Ch50～52
  与 Ch63，并核对 Ch19。Ch51 已有 source/destination completion、visibility、ownership transfer 与
  cancellation 原则；本 incident 新增可保留的具体演进链是 `timeout abort → old DMA crosses reuse epoch
  → corrupted model state → cross-stage safe-to-reclaim handshake`。Ch44/63 只接 acceptance telemetry
  与 anomaly operating-point handoff。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Version-Grounded Incident)` / Ch51，Ch44/63 short handoff。Historical Books Gate 关闭，不修改 Books。
  待验证 frozen runtime commits、PR #22811、exact hardware/topology/precision、request and anomaly denominator、
  detector confusion matrix、post-retry outcome、fence overhead、LayerSplit low-hit/short-context break-even、
  failure injection 与 independent reproduction。

### Preserving the privacy of AI training data — 24/30

- **Candidate / Week / Score**：Amazon Science `Preserving the privacy of AI training data`，2026-W18，
  24/30（TN 3 / SI 5 / PV 5 / SR 4 / PR 4 / L 3）。它是新的 official reproduction/engineering narrative，
  不是新的 privacy algorithm；technical novelty 因而只给 3 分，longevity 也因缺 frozen artifact 与完整
  experiment contract 只给 3 分。
- **Source Family / Date / Access / Full-read Coverage**：`AMAZON-PRIVACY-TRAINING-DATA-2026-04-29`。
  Direct primary source 是 Amazon Science 2026-04-29 全文，已覆盖三类 attack、两类 defense、实验结果、
  production claim 与 caveat。Related primary sources 已核对 quantile-regression membership inference、
  DP-SGD、Deep Leakage from Gradients、Flamingo secure aggregation、Robbing the Fed 与 Scale-MIA 的官方
  publication/arXiv/ePrint metadata 和核心机制；本周新事件没有独立 2026 paper、代码、dataset、raw logs
  或 frozen recipe，不能把叙述性复现实验当作可独立重跑的 artifact。
- **Original Problem / Previous Design / Changed Constraint**：集中训练把数据留在单一 owner 内，普通 FL
  又把 raw records 留在各参与方，本来都比集中汇集数据更合理。但 model confidence、local gradient 与
  shared global update 仍是 derived disclosure surfaces；“没有搬走 raw data”不等于“没有泄露关于 raw
  data 的信息”。约束变化是 attacker 从数据库读取者变为 inference caller、aggregation server 或恶意
  participant，privacy boundary 必须覆盖 output 与 intermediate state。
- **Mechanism / State Ownership / Control and Data Flow**：membership inference 通过 non-member confidence
  distribution 的 quantile model 构造 example-specific threshold；local-gradient inversion 从 server 看到的
  gradient 反优化输入；malicious-participant attack 则注入 crafted preprocessing/ReLU layer，使 global
  gradient 的相邻神经元贡献可相减恢复 individual samples。MPC/secure aggregation 让 server 只获得聚合
  update，保护传输与聚合中的 individual gradients；DP-SGD 通过 per-unit clipping、noise 与 accountant
  限制训练结果对单个 privacy unit 的可区分影响。两者是 `Layering / Dependency`，不是互相替代。
- **Implementation / Evaluation Contract**：博客报告 ResNet-50/ImageNet-1k membership inference 在被
  attack 标记的 records 中达到 97% precision，但未同时披露 recall、base rate、query budget 与置信区间；
  EMNIST DP-SGD test accuracy 为 78%（epsilon=1.5）、82%（epsilon=3.0），non-DP 为 90%；EMNIST batch
  gradient 在 batch size 7 时恢复 3 samples，single-sample batch 可 exact recovery；MPC case 未恢复样本；
  三方、每方 batch 3 的 malicious-participant case 恢复 9 个样本中的 8 个，而 epsilon=1.5 的 global
  gradient 未恢复 meaningful information。未披露 model architecture/optimizer、delta、adjacency/privacy
  unit、clipping norm、sampling、round composition、accountant、party dropout/collusion、MPC overhead、
  attack stopping rule、seeds/variance 或 raw artifacts，因此这些数值只属于该 reproduction contract。
- **What the Evidence Proves / Does Not Prove**：该 official source 支持三类 disclosure surface 在作者的
  ImageNet/EMNIST demonstrations 中存在，并说明 MPC 与 DP 保护不同 lifecycle layer。它不证明 97%
  precision 等于 97% attack success，不证明所有 FL gradient 都可同样恢复，也不证明 epsilon=1.5/3 是
  通用安全 operating point。“practical today”“mature enough to deploy”与 Amazon production use 是作者
  声明；没有公开 scale、latency、cost、accuracy、incident、regulatory 或 independent audit contract。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：DP 引入 utility loss、privacy-budget
  composition、clipping bias 与 distributed-equivalence risk；MPC 引入 communication/crypto overhead、
  dropout/collusion assumptions、key/share lifecycle 与只保护 intermediate values 而不保护 released model
  的边界。低敏感、单 owner、严格 access-controlled training 可保留简单方案；只用 DP 不能隐藏 individual
  updates，只用 MPC 也不能限制 global model disclosure。最小合理设计先按 attacker capability 与 released
  object 选择层，而不是把 `privacy preserving` 当成单一 feature flag。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：`Layering / Dependency`：raw-data
  locality -> gradient disclosure -> secure aggregation -> released-model disclosure -> DP output contract。
  主 owner 为 Ch68，已重读 Ch67～69 并核对 Ch63。Ch68 已明确 privacy unit、adjacency、contribution
  bound/clipping、epsilon/delta、sampling/composition、accountant、distributed equivalence、empirical audit
  与 utility slices；Ch63 已写 secure aggregation 只发布 aggregate、并保留 visibility/freshness 代价。
- **Final Disposition / Changed Files / Open Questions**：`No Change — Already Covered` / Ch68。
  该材料提供受限 engineering illustration，但未新增 Books 的长期机制缺口；Historical Books Gate 关闭，
  不修改 Books。待核验 frozen code/data/config、delta/accountant、round composition、MPC trust/dropout/
  collusion model、attack recall/base rate/uncertainty、crypto overhead、large-model reproduction 与 production audit。

### Publication-node source-family review — C3LLM / How Catastrophic is Your LLM?

- **Date / Dedup / Access**：Amazon Science 官方 Blog 节点为 2026-04-27，ICLR 2026 publication page 记为
  2026；arXiv:2510.03969 v1 实际提交于 2025-10-04，v2/v3 为 2026-02-04/05。已读 v3 的 20 页全文，
  包括 formalization、graph construction、四种 distributions、evaluation、baselines、ethics 与全部
  ablations/Appendix。机制 first-public 属于 2025，因此 W18 只记录 publication/explanation node，不进入
  scored denominator，加入 2025 backlog。
- **Mechanism / Evidence Contract**：C3LLM 把 multi-turn conversation 定义为 query graph 上的 Markov
  process，并对 Random Node with Jailbreak、Graph Path、harmful-target endpoint 与 Adaptive with
  Rejection 分布独立采样，用 Clopper-Pearson 区间界定“给定该分布时至少一轮被 GPT-4o judge 判为
  catastrophic”的概率。主实验由 68 个 HarmBench chembio/cyber scenarios、每 scenario 100 queries、
  sequence length 5、每 specification 50 samples、95% confidence interval 构成；另有 illegal-domain check
  和 jailbreak probability、length、query-set size、weight ratio、sample count、graph threshold、variance
  ablations。
- **Evidence Boundary / Evolution / Disposition**：论文支持固定 single-turn/fixed-sequence benchmark 可能
  漏掉 distribution-conditioned multi-turn risk，并证明在作者生成图、augmentation、judge 与模型版本下
  某些 lower bound 很高；它不“认证”全部现实对话空间，也不证明 query graph 等于 human/adversarial
  traffic、GPT-4o judge 无误，或不同 API/model revision 可直接排名。Ch62 已拥有 subject/distribution/
  scorer/uncertainty contract，Ch68 已拥有 run-centric multi-turn safety campaign 与 judge-correlation
  caveat。最终为 `2025 Backlog — Publication Node / No W18 Score`；后续 2025 source-family audit 决定是否
  需要 refine，不在 W18 或 Historical Books Gate 关闭时修改 Books。

### Publication-node source-family review — Concord: Learning Network Configuration Contracts

- **Date / Dedup / Access**：EuroSys 2026 与 DOI metadata 将正式出版定位到 2026-04-27～30，Microsoft
  Research publication page 也标为 April 2026；但作者在 2025-08 已公开宣布论文被 EuroSys 2026 接收，
  Microsoft-hosted PDF 路径又带有 `2025/10`。后两者说明机制可能在 2025 已形成或公开，却没有可证明
  PDF 当时已公开的 immutable timestamp。为避免把同一机制重复计分，本周只记录 formal-publication node，
  first-public 标记 `Disputed / 2025 Backlog Reconciliation Required`，不进入 W18 scored denominator。18 页
  正文、EuroSys proceedings、DBLP、DOI/ORCID metadata 与作者 publication/news page 均已核对。
- **Original Problem / Previous Design / Changed Constraint**：formal network verification 在协议模型与
  invariants 完整时给出强保证，但真实网络包含大量 vendor dialect、重复/层级元素和未文档化策略，逐协议
  建模与手写全部 invariants 成本过高；简单 key-value rule mining 又丢失重复元素、hierarchy 与跨行 value
  relations。网络配置增长到每设备数万行、跨数千设备与多 SKU 后，约束从“能否证明一个已知 invariant”
  变为“能否从 operational baseline 低成本恢复足够多、可定位的 change guards”。
- **Mechanism / State Ownership / Control and Data Flow**：Concord 先对 JSON/YAML/indentation/plain text 做
  context embedding，再把每行转换成 typed pattern + parameter；从 present、ordering、type、unique、sequence
  和 relational contracts 中学习高 support/confidence 规则。relation lookup 以 prefix/string trie 与 hash table
  避免全组合枚举，用 informativeness/diversity heuristic 过滤偶然关系，再用 relation graph transitive reduction
  删除不影响 bug-finding 的冗余 contract。CI 中以 pre-change configs + metadata 学习 contract，再检查
  post-change configs；learned contract/version、training config set 与 suppressed false-positive feedback 属于
  validator state，生产配置生成器仍拥有 desired config，人工 reviewer 拥有放行权。
- **Implementation / Evaluation Contract**：实现是 6,557 行 Rust CLI，默认 support `S=5`、confidence
  `C=96%`，阈值可调。评测覆盖两类匿名生产数据：mobile edge datacenter 与 cloud WAN，共包含从千级到
  百万级配置行；机器为 64 GB RAM、3 GHz 14-core Intel i9。所有 dataset 的 learn 小于 34 秒、check 小于
  22 秒，brute-force baseline 在每个 WAN dataset 1 小时 timeout。作者用 coverage 定义“删除该行是否会
  触发至少一个 contract”，edge coverage 超过 84%，WAN roles 约 49.9%～71.0%。precision 先用 GPT-4
  估算 sample size，再人工标注 1,243 个 contracts；95% confidence 目标下部分类别因 150-sample cap 将
  error 放宽到最多 10%。除 ordering 外，多数类别 precision 为 80%～100%；ordering 为 edge 38%、WAN
  71%，production 默认关闭。三次历史 incident replay 被检测；“部署后无 major configuration outage”没有
  exposure time、change count 或 matched control，不能作为因果可靠性证明。
- **Evidence Boundary / Trade-offs / Evolution**：论文支持 syntactic/relational change guards 可以在作者
  数据上以低成本提供有用 coverage 和 line-level localization；不证明配置语义正确、end-to-end reachability、
  recall/false-negative rate、跨网络泛化或零事故因果。它以 weaker guarantee 换取 protocol agnosticism 与
  learnability，并新增 baseline contamination、configuration drift、threshold tuning、role/SKU mixing、false
  positive suppression、learn/check version skew 与 learned-bad-state 固化。演进是 `Layering / Dependency`：
  schema/linter → mined syntactic contract → relational change guard → formal/runtime validation；不是 learned
  contract 替代 formal verification。
- **ROADMAP / Disposition / Open Questions**：已读 Ch53、Ch54、Ch63、Ch68、Ch69；若 2025 Source
  Family 后续通过 Books Gate，主 owner 应为 Ch69 的 release/readiness gate，Ch53/54 只接 control-plane
  contract handoff。Ch69 已要求 Build/Pre-production/Release evidence 和 rollback，却尚未区分 learned
  best-effort guard 与 semantic verifier。当前 disposition 为 `2025 Backlog — Disputed First-public /
  W18 Formal-Publication Node / No W18 Score`；Historical Books Gate 关闭，不修改 Books。待核验 2025
  immutable public timestamp、artifact/code、contract/model revision、dataset split、recall/false negatives、
  drift/relearning、feedback poisoning、production exposure denominator 与 independent reproduction。

### Full Source Review — AutoSP: Compiler-Based Sequence Parallelism for Multi-GPU Training — 28/30

- **Candidate / Week / Score**：AutoSP，2026-W18，28/30（TN 5 / SI 5 / PV 5 / SR 4 / PR 5 /
  L 4）。它把长序列训练的 Sequence Parallel 从框架专用手写路径推进为 compiler graph
  transformation，并把 activation recomputation 的切点选择与序列长度联合优化；Source Reliability
  因代码在论文中仍标记为将发布、实验缺少多节点和训练收敛证据而为 4。
- **Source Family / Date / Access / Full-read Coverage**：`PYTORCH-AUTOSP-2026-04-29`。PyTorch 官方
  Blog 与 arXiv:2604.27089 v1 均为 2026-04-29；论文已读 Abstract、Introduction、Background、Method、
  Algorithm、Implementation、全部 evaluation/ablation、Related Work、Limitations、Conclusion 与影响结论
  的 Appendix，ICLR 2026 接收状态也已核对。OpenReview PDF 在当前浏览器权限下不可读，但 arXiv v1
  HTML 正文完整可访问；本文没有后续 revision 可用于替换 event-time 证据。
- **Original Problem / Previous Design / Changed Constraint**：手写 DeepSpeed-Ulysses 让每个 rank 持有
  sequence shard，并在 Attention 前后用 All-to-All 交换 head/sequence layout；它在固定模型与明确并行
  recipe 下合理，却要求用户识别可分片 buffer、position-dependent index 与 Attention boundary，模型变化
  时容易遗漏。Ring Attention 以 K/V block 环传输扩展长序列，也合理，但执行语义、通信模式和性能边界
  不同。模型 graph、长序列 activation 与硬件后端不断变化后，“每个模型重写一次”成为正确性和可移植性
  瓶颈，而通用 activation checkpoint 又可能在最昂贵的 Attention 上做无效重算。
- **Mechanism / State Ownership / Control and Data Flow**：AutoSP 在 Torch-IR/FX graph 上先分析 tensor
  shape，再执行三类 rewrite：缩小按 sequence 维复制的 buffers、重算 position/index tensors、在 Attention
  边界插入 All-to-All，使局部 sequence layout 与 head layout 互换。compiler 拥有 graph rewrite 与 shape
  proof，distributed runtime 拥有 collective progress，model code 仍拥有原始算子语义。随后构造
  sequence-aware activation-checkpoint min-cut：当 `T` 很长、Attention 的二次成本主导时，允许对 Attention
  之外的 projection/MLP 计算做 rematerialization，避免把最昂贵路径纳入保守 cut。
- **Implementation Details**：实现以 Dynamo 捕获的 FX graph 为输入，使用人工维护的
  `RESIZE_BUFS`、`INDEX_OPS` 与 `ATTN_OPS` 集合识别 rewrite 点；这说明当前“自动”依赖 curated operator
  coverage，而不是任意 PyTorch program 的语义推导。它要求 full graph、不能容忍 graph break；目标是
  DeepSpeed-Ulysses，不是自动搜索 Ring Attention，并受 Attention head 数限制 SP degree。graph capture、
  dynamic shapes、custom ops、MoE/EP layout 与 compiler/runtime version 都成为新的 compatibility state。
- **Evaluation Contract / Baselines / Ablations**：作者使用 PyTorch 2.7、CUDA 12.8、ROCm 6.4，在
  GH200-96GB、A100-80GB 与 MI250-64GB 上评估 Llama 3.2 1B/3B、Llama 3.1 8B、Llama 2 13B；baselines
  为 `torch.compile` + ZeRO-3/FSDP、手写 DeepSpeed-Ulysses 与 Ring Attention。8 张 A100 的最大可训练
  长度相对 Ulysses 分别最高 2.14x/3x/1.88x（3B/8B/13B），相对 Ring 为 2.14x/3x/1.6x；2 张 GH200
  与 2 张 MI250 上分别最高 2.7x 与 2.5x。与手写 Ulysses 的 runtime ratio 在 NVIDIA 为 0.97x/0.98x，
  AMD 为 0.97x/0.87x。1B、40K ablation 报告 Attention activation memory 下降 13.03x、MLP 下降 2.22x，
  backward 变慢 1.14x；SP-only 最大 77K、1.09s，SP+checkpoint 为 128K、1.19s，Ulysses 为 81K、
  1.06s。8B iteration-time 只测 10 次；作者仅称多次运行取平均，没有 seeds、variance 或 tail distribution。
- **What the Evidence Proves / Does Not Prove**：证据支持：在上述模型、版本与单节点硬件组合中，graph
  rewrite 能接近手写 Ulysses 的执行时间，sequence-aware rematerialization 可进一步扩大可训练长度；它不
  证明训练 loss/收敛/最终质量等价，不证明多节点 fabric、MoE、任意 dynamic control flow/custom op、不同
  optimizer 或未来 PyTorch graph 均成立，也不证明 AutoSP 普遍优于 Ring Attention。最大长度只说明该
  memory/graph contract 下能够运行，不等于模型有效利用同等长度。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：自动 rewrite 减少模型专用工程，却
  新增 operator registry 漏识别、shape proof 错误、collective ordering、graph/version drift 与 silent semantic
  mismatch；rematerialization 节省 activation memory，却增加 backward compute。稳定固定模型、需要精确
  手调通信、存在 graph break 或需要 Ring-style block circulation 时，手写路径仍合理；短序列或 compute
  紧张时，通用 checkpoint 的额外重算也可能不值得。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：`Direct Evolution`：手写 sequence
  sharding → compiler-recognized graph rewrite → sequence-aware recomputation。主 owner 为 Ch33，已重读
  Ch22、Ch24、Ch32～36。Ch33 已说明 Sequence Parallel 是 operator-graph transformation，并与 Context
  Parallel 分界，但尚未覆盖 compiler 如何识别 buffer/index/Attention boundary 与 rematerialization
  联合决策；Ch24 已有 activation checkpoint 的 memory/compute trade-off，Ch22 与 Ch36 分别只接 Long
  Context 和 framework composition handoff。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch33；Ch24、Ch22、Ch36 short handoff。Historical Books Gate 关闭，不修改 Books。
  待验证 frozen code/commit、full-graph coverage、dynamic/custom/MoE cases、多节点 topology、collective
  failure、训练 convergence、更多运行分布与相同总资源下的 Ring/Ulysses break-even。

### Full Source Review — LightSeek-SMG: CPU/GPU-Disaggregated LLM Serving Gateway — 27/30

- **Candidate / Week / Score**：LightSeek-SMG，2026-W18，27/30（TN 4 / SI 5 / PV 5 / SR 4 / PR 5 /
  L 4）。它不是新 GPU kernel，而是把 Serving frontend 的 CPU work、协议与 cache ownership 从 engine
  进程中分离；证据来自作者官方工程 Blog，当前 repository/code path 因访问权限未独立核验，故 SR 为 4。
- **Source Family / Date / Access / Full-read Coverage**：`PYTORCH-LIGHTSEEK-SMG-2026-04-30`。Direct
  primary source 为 PyTorch 2026-04-30 官方全文，已读 architecture、Rust gateway、gRPC contract、
  tokenizer cache、routing、benchmarks、deployment claims 与 limitations surface。没有独立论文、system
  card、frozen code snapshot 或 raw benchmark artifact；GitHub 当前受 saved browser permission 限制，
  所有 code/adoption/production-ready 表述只按作者声明记录。
- **Original Problem / Previous Design / Changed Constraint**：在 engine 内完成 tokenization、chat-history
  拼装、multimodal preprocessing、reasoning/tool parsing、stop detection 与 structured validation，部署简单且
  保持单一 semantic owner，低并发时完全合理。高并发、多 engine/replica 与复杂 Agent request 让这些 CPU
  阶段争用 Python runtime、复制 tokenizer/cache 状态，并把非 GPU 工作放进 engine critical path；约束从
  “GPU forward 足够快”变为“CPU frontend、network、cache 与 GPU engine 必须共同满足 E2E SLO”。
- **Mechanism / State Ownership / Control and Data Flow**：SMG 把 CPU transformations、tool/reasoning parser、
  chat history、validation 与 authorization 放入 Rust gateway，GPU engine 只接收预处理 token、返回生成
  token；两者用 narrow gRPC contract 连接。L0 cache 保存 exact tokenization，L1 只在 special-token-safe
  boundary 做 prefix reuse；cache-aware router 再按 replica locality 选择 engine。gateway 因而拥有 request
  semantic preprocessing、CPU cache 与 stream assembly，engine 拥有 tensor execution、KV 与 token-step
  progress；协议必须携带 model/tokenizer/chat-template/parser revision，否则快路径可能返回语义错误。
- **Implementation / Evaluation Contract**：作者报告 H100、8 个模型、SGLang/vLLM、5 类 traffic、
  concurrency 1～256，并称 gRPC 与 HTTP 做了 1,082 个 matched comparison points。concurrency=1 差异在
  noise 内；concurrency=256 总体 throughput 约增 8%，7,800 input/200 output case 为 12.2%；某个
  Llama-3.3-70B-FP8 case 报告 output throughput 3.5x。另一个 high-concurrency 70B-FP8 case 报告 E2E
  p99 改善 15.8%、output throughput 增加 44.6%。cache/router microbench 声称 216K insertions/s、99%
  memory reduction；8 replicas 的 Llama test 中平均 TTFT 下降 23%、p99 下降 28%，PD setup 报告
  TTFT 改善 20～30%。
  公开页面未完整给出所有 model revision、GPU count/topology、input/output distribution、precision mapping、
  batch/admission、SLO target、warmup、seeds/variance、engine versions 与 raw data，不能把不同表中的最大值
  合并成通用收益。
- **What the Evidence Proves / Does Not Prove**：证据支持作者实现中 CPU frontend 在高并发/长输入时可成为
  可观测 bottleneck，且把它外移后部分 workload 的 throughput/TTFT 改善；concurrency=1 近似持平也说明
  分离不是无条件收益。它不证明每个 engine 都受 Python CPU 限制、不证明 gRPC 永远优于 HTTP、不证明
  3.5x 可迁移到其他模型/拓扑，也不证明 tokenizer cache、parser 与 model behavior 在 revision 漂移后仍
  一致。`only implementation`、adoption 与 production-ready 均为厂商陈述。
- **Trade-offs / New Failure Modes / Previous Design Still Applies**：分离释放 engine CPU 并集中复用，
  却新增 protocol serialization/network hop、gateway saturation、双端 backpressure、semantic drift、cache key/
  invalidation、版本 rollout、跨租户隔离与新故障域。模型专用 parser、stop rule 或 multimodal processor
  更新时，gateway 与 engine 不一致可能不会 crash，却会改变输入/输出语义。低并发、单 engine、严格
  co-version deployment 或 CPU work 很轻时，co-located frontend 更简单且更容易保持 correctness。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：`Layering / Dependency`：engine-local
  frontend → CPU/GPU service split → model-aware cache/routing。主 owner 为 Ch38，已重读 Ch38、Ch46、
  Ch49、Ch52、Ch58、Ch67 与 Ch80。Ch38 已定义 frontend 与 execution identity，却未明确 frontend 可作为
  独立 failure/scaling domain；Ch58 的 Gateway 是外部 identity/policy boundary，不应因产品同名而自动拥有
  tokenizer/parser state。Ch46/49/52 只接 engine、endpoint 与 admission handoff。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch38；Ch58、Ch46、Ch49 short handoff。Historical Books Gate 关闭，不修改 Books。
  待验证 frozen implementation、协议 schema/versioning、cache identity/invalidation、failure injection、
  semantic equivalence、gateway HA/backpressure、tenant isolation、完整 matched workload contract 与独立复现。

### Full Source Review — Granite 4.1 Language 3B/8B/30B — 24/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-41-LANGUAGE-STAGED-TRAINING`；W18；
  `TN 4 / SI 4 / PV 4 / SR 4 / PR 4 / L 4 = 24/30`；official model release、technical training article、
  model cards、configs 与 artifact history。Source Reliability 为 4 而非 5：weights/config/cards 可核验，
  但训练与 benchmark 主要是 IBM 自报，card 仍保留空的 `arxiv:0000.00000`，没有同行评审 technical paper、
  independent reproduction 或完整 launch-day frozen evaluation artifact。
- **Event Date / Revision History / Access and Verification Status**：IBM Research release 与 Hugging Face
  technical article 均发表于 2026-04-29，事件归 W18。8B repository history 显示 initial commit 为
  2026-04-06，4 月 8～28 日持续更新，5 月 4 日又修改 model card；因此 current card 能核验当前 artifact，
  不能被当作不可变的 launch snapshot。3B、8B、30B current cards、8B config、language-model collection、
  repository history 与官方 release/article 均已读取。`Primary Official Technical Article and Current
  Artifacts Complete; Frozen Launch Snapshot Not Fully Disclosed`。
- **Full-read Coverage**：已覆盖 architecture table、五阶段 pretraining/data mixture、long-context extension、
  SFT data construction/filtering、GRPO/DAPO training、四阶段 RL、base/instruct evaluation tables、FP8
  compression、training infrastructure、limitations、license、model-card deployment examples、current config
  与 commit history。官方材料没有披露 pretraining 的完整 optimizer/global batch/总 GPU-hours/power/failure
  contract、benchmark seeds/CI/污染审计、matched serving latency/SLO 或 512K released-artifact evaluation；
  对应字段记为 `Not Disclosed`，不由模型能力反推。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：MoE 以 conditional compute
  扩大参数容量，在大规模 serving 上很合理，但 sparse routing、expert communication 与 active-parameter
  latency 会引入额外 runtime contract。Granite 4.1 Language 选择 dense 3B/8B/30B，不是证明 dense 普遍
  优于 MoE，而是在 edge、single-node 与 enterprise deployment 中，用固定 active path、较简单 artifact
  identity 和较可预测的 memory/latency，交换更高的每-token dense compute。约束变化也不只来自模型结构：
  general pretraining、math/code、high-quality annealing、long context、instruction following、preference、
  identity/calibration 与 math recovery 需要在同一 checkpoint lineage 中依次生产，单一静态 mixture 或一次
  post-training 已不足以表达完整 capability contract。
- **Mechanism / State Ownership / Control and Data Flow**：三种模型均为 decoder-only dense Transformer，使用
  GQA、RoPE、SwiGLU、RMSNorm 与 tied embeddings。3B/8B/30B 分别为 40/40/64 layers；8B/30B 为
  32 attention heads、8 KV heads，current 8B config 为 hidden size 4096、intermediate size 12800、BF16、
  RoPE theta 10M、`max_position_embeddings=131072`。能力生产路径是：

  ```text
  broad 10T-token pretraining
  → 2T math/code emphasis
  → 2T high-quality + long-CoT/instruction annealing
  → 0.5T refinement
  → staged 4K → 32K → 128K → 512K long-context exposure
  → ~4.1M-example SFT with model-judge/rule filtering
  → multi-domain GRPO/DAPO-style RL
  → RLHF
  → identity/knowledge-calibration RL
  → math RL recovery
  → versioned dense / FP8 artifacts
  ```

  Data mixture、checkpoint、optimizer/scheduler、judge/filter、teacher/reward model 与 artifact config 分别
  拥有不同状态；每一阶段的输出 checkpoint 是下一阶段输入。官方明确说 dynamic sampling 被关闭，所以
  “使用 DAPO loss”不能外推成执行了完整 DAPO algorithm。FP8 只量化 Transformer block 内 linear
  operators 的 weights/activations，其他 layers 保留原精度；它是新的 deployment artifact，不等同于原始
  BF16 checkpoint 的无损别名。
- **Implementation Details / Evaluation Contract**：pretraining 使用 CoreWeave 上的 NVIDIA GB200 NVL72，
  72-GPU NVLink domain 与 non-blocking full Fat-Tree NDR 400 Gb/s InfiniBand；没有公开确切 GPU 数、
  GPU-hours、pretraining batch 或 optimizer。SFT 使用 16 nodes × 4 GB200、3 epochs、LR `5e-6`、3%
  warmup、约 25K steps、sequence length 16,384、effective batch 256。RL 使用 SkyRL、16 samples/prompt、
  train batch 1,024、context 8,192；不同阶段公开了 LR、KL beta、prompt count 的一部分。Base/instruct
  表给出若干 benchmark 的 few-shot/CoT 设置，但缺统一 decoding、hardware、seed/CI、污染与 serving
  contract，因此只作为 vendor experiment。RULER 只报告 32K/64K/128K；没有 512K evaluation。
- **Baselines / Ablations / Sensitivity / Overhead**：官方对不同 sizes、Granite 4.0-H-Small 与若干外部模型做
  benchmark comparison，也展示 staged RL 前后的 capability movement；这能显示同一作者 pipeline 中
  RLHF 后 math regression、后续 math RL recovery 的现象。它不是严格 component ablation：没有
  data-mixture-order randomization、stage removal、matched compute、多个 training seeds 或独立 evaluator。
  8B dense 与 32B-A9B MoE 的 selected-task comparison 也没有相同 inference hardware、precision、batch、
  token length、latency/throughput 与 SLO，不能证明 dense serving 普遍更优。FP8 声称约 50% disk/GPU
  memory reduction，但未披露匹配的 quality、throughput、latency 或 SLO test。
- **What the Evidence Proves / What It Does Not Prove**：证据支持 IBM 在 W18 发布了三种 dense artifacts，
  并公开一条由 changing data distributions、long-context exposure、SFT 与 sequential RL 组成的 versioned
  training lineage；还支持同一 pipeline 中某阶段可改善一类能力、同时损伤另一类能力，后续阶段承担
  recovery。它不证明五阶段顺序、数据比例、GRPO/DAPO 配置或 dense architecture 可迁移为通用 recipe；
  不证明 vendor benchmark 是生产质量；不证明 FP8 没有质量损失；也不证明模型对 512K 输入拥有可交付
  的 effective-context/SLO 能力。
- **Claim / Artifact Boundary**：training article 的 Phase 5 写到 512K exposure，而 current 3B/8B/30B
  cards/configs 将 sequence length / `max_position_embeddings` 固定为 131,072，RULER 也只评到 128K。
  因此必须保留：

  ```text
  training exposure up to 512K
  ≠ released artifact accepted-length contract (131,072)
  ≠ effective information utilization at 512K
  ≠ production SLO at 512K
  ```

  current card 经过 5 月 revision，不能倒写为 4 月 29 日每个字段均已公开。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：changing mixture 与 sequential
  alignment 允许逐阶段修复能力，却增加 checkpoint lineage、data/judge/reward revision、regression gate、
  reproducibility 和 rollback burden；后续 RL 可能恢复 math，也可能再次损伤 instruction following、安全或
  calibration。Long-context exposure 增加 training compute 与 artifact/config mismatch 风险；FP8 增加
  quantization recipe、kernel coverage 与 quality gate。静态 mixture 在目标稳定、实验预算有限时仍更简单；
  一次 SFT/偏好训练在 capability surface 较窄且 regression 可控时仍合理；MoE 在容量与 conditional compute
  优先、routing/communication 成本可承担时仍成立；BF16 在 quality-risk 高或 kernel contract 未验证时仍是
  合理基线。
- **Evolution / ROADMAP / Target and Adjacent Chapters / Existing Coverage**：关系是 `Layering / Dependency`
  与受限的 `Direct Evolution`：静态 pretraining mixture → phase-specific changing distribution → staged
  long-context exposure → sequential post-training and capability recovery。主 owner 暂定 Ch24；已重读 Ch24
  与相邻 Ch23、Ch25，并联读 Ch22、Ch29。Ch23 已拥有 mixture/filter/judge lineage，Ch22 已明确 accepted
  length、trained length 与 effective utilization 不能混用，Ch25/29 已拥有 SFT 与多阶段 RL。因此若未来
  Books Gate 打开，只需在 Ch24 refine “training run 是 distribution schedule 与 checkpoint lineage，而非
  单一 IID mixture”及阶段回归门禁；其他章节只做 handoff，不复制 Granite 配方或 benchmark。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Version-Grounded)` / Ch24；Ch22/23/25/29 short handoff。Historical Books Gate 关闭，不修改 Books；只
  更新 W18、年度索引、Learning State 与 2026-08-10 Daily。待验证 launch-day immutable cards/configs、
  512K checkpoint 与 evaluation、pretraining optimizer/batch/total compute、benchmark harness/seeds/CI、
  independent reproduction、RL stage ablation/capability-regression matrix，以及 FP8 matched quality/SLO。

### Full Source Review — Granite Vision 4.1 4B — 24/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-VISION-41-MULTILAYER-FEATURE-INJECTION`；
  W18；`TN 4 / SI 4 / PV 4 / SR 4 / PR 4 / L 4 = 24/30`；official multimodal model release、current
  model card/config/history、related ChartNet primary paper/dataset。Source Reliability 为 4：公开 weights、
  merged adapters、custom modeling/config 与 dataset artifacts 可核验，但 4.1 architecture 只有 vendor card，
  没有独立 technical paper、component ablation、seed/CI 或 matched inference contract。
- **Event Date / Revision History / Access and Verification Status**：IBM/Granite release 与 card 标记
  2026-04-29，事件归 W18。artifact initial commit 为 2026-04-16，weights/config/modeling 与 card 在 4 月
  19～29 日多次修改；5 月 5～6 日又修改 recommendation/card，后续还加入 native Transformers/vLLM
  support 与 input-token fix。因此 current card/config 用于核验现在的 artifact shape，不等于冻结的 4 月 29 日
  snapshot。`Launch Artifact Lineage Verified; Current Model Card and Config Complete; Architecture Paper and
  Frozen Evaluation Artifact Not Disclosed`。
- **Full-read Coverage**：已读 current card 的 supported tasks、benchmark methodology、setup、Transformers/
  vLLM/MLX/Docling surfaces、training data、architecture、infrastructure、limitations 与 resources；已核对
  full config、file/commit history。相关 ChartNet v1（2026-03-28，早于 W18）已阅读全文，包括 related work、
  code-guided generation、quality filtering、dataset partitions、training/evaluation、public-benchmark transfer、
  prompts、human-annotation 与 judge-agreement appendices；current dataset card/changelog/schema 也已核对。
  ChartNet 是 related primary source，不在 W18 再计一个新事件。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint**：传统 VLM 将 vision encoder
  的最终 features 经单一 projector 转成 visual tokens，再与 text tokens 一同交给 LLM；接口简单、module
  ownership 清楚，也便于替换 encoder/LLM。高分辨率 document/chart 同时需要深层 semantic features 与
  细粒度 spatial evidence。只提高输入分辨率或保留全部 patches 会放大 visual-token、Attention、TTFT 与
  KV cost；只使用最终压缩 representation 又可能在进入 LLM 前丢失局部结构。Granite Vision 4.1 因而在
  token budget 与跨层 evidence preservation 之间引入更细的 feature-injection contract，而不是证明单一
  projector 已失效。
- **Mechanism / State Ownership / Control and Data Flow**：model 由约 0.6B SigLIP2 SO400M vision encoder /
  projectors 与约 3.4B Granite 4.1 language model 组成。输入图像按 384×384 tiles 编码，并始终含一个
  downscaled base view；Window Q-Former 将每个 4×4 patch window 通过 cross-attention 压为 2×2 tokens。
  视觉状态随后通过两条路径进入 LLM residual stream：

  ```text
  image
  → 384×384 tiled views + base view
  → SigLIP2 features at multiple depths
  → Window Q-Former 4× token compression
  → LayerDeepstack: 4 encoder depths → 4 LLM layers
  → SpatialDeepstack: deepest full-resolution features split into 4 groups → 4 later LLM layers
  → 8 additive vision-to-LLM injection points
  → Granite 4.1 3B decoder → structured text / code / JSON / table output
  ```

  current config 将 LayerDeepstack 映射为 vision layers `-19/-13/-7/-1` 到 LLM layers `9/6/3/0`，
  SpatialDeepstack 目标为 LLM layers `12/15/18/21`，`image_seq_length=576`；这些值属于当前 revision，
  不是抽象成所有 VLM 的配方。vision encoder 与 LLM 分别用 LoRA fine-tune，rank 256 覆盖 LLM self-
  attention projections 与 MLP；release artifact 合并 adapters，因此 base、adapter、merge recipe 与 final
  weights 必须作为同一 lineage。
- **Training Data / Implementation Details**：card 只说使用 chart、table、KVP extraction mixture，并加入
  Granite Vision instruction-following data，没有公开各 partition 数量、比例、epoch、optimizer、learning
  rate、resolution/token distribution 或 exact dataset manifest。ChartNet v1 公开 1.5M aligned tuples，
  code/image/CSV/summary/reasoning 五种表示由 executable plotting code 串联；150K seed charts 经 VLM 重建、
  LLM code augmentation、sandbox rendering、visual-quality filter 与 attribute generation扩展。生成使用
  Pixtral Large、gpt-oss-120b 与百余 A100/H100；作者报告约每 168 小时产出一百万 annotations。4.1 model
  card 仅披露在 IBM Blue Vela 上 32×H100 训练约 200 小时，未披露精度、节点拓扑、batch 或利用率。
- **Dataset Revision Boundary**：ChartNet paper 的 1.5M core 与 96,643 human-verified 口径，current dataset
  card 的 1.7M core、4.2M synthetic 与 94,643 human-verified 口径并不相同。dataset changelog 显示 4 月
  29 日新增 2.5M permissive rows，30K real-world charts 在 5 月 15 日才加入，grounded/reasoning completion
  在 6 月 3 日。故不能把 current 4.2M、real-world 或 June subsets 倒写为 4 月 29 日 model 的已训练数据；
  model card 也未公开 exact manifest/digest，训练 lineage 保持 `Not Disclosed`。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：model card 评 chart extraction 时
  使用 ChartNet human-verified test set与 GPT-4o judge；table extraction 合并 TableVQA-Extract、
  OmniDocBench-tables、PubTablesV2，以 HTML/TEDS 评 cropped/full-page；KVP 在 VAREX 上报告 zero-shot
  exact match。current card 的 figure/table headline 没有完整 machine-readable run manifest、hardware、
  image/token length、batch/concurrency、decoding、seed/CI 或 contamination audit。ChartNet paper 的
  2,000-synthetic-tuple held-out suite对 256M～7B 五种 VLM做 task-specific SFT，并在 ChartCap/
  ChartMimic-v2 测 transfer；大量 metrics 仍由 GPT-4o judge，除 CoT QA 使用 fuzzy match。它验证的是
  ChartNet data utility，不是 Granite Vision 4.1 的 Layer/SpatialDeepstack ablation；没有分别移除 Q-Former、
  四个 layer features、四个 spatial groups 或控制相同 visual-token/FLOP budget。
- **What the Evidence Proves / What It Does Not Prove**：artifact 与 config 证明 current model 真实实现了
  compressed multi-depth/multi-spatial feature injection，card 证明 IBM 将它用于 structured document
  extraction。ChartNet 实验支持 code-aligned multimodal tuples 能在作者的 task/model contract 下改善多种
  backbone，并给出 executable rendering 与 human/judge quality checks。证据不证明八个 injection points
  是收益因果来源、不证明其优于 compute-matched single projector/更高 visual-token baseline、不证明
  GPT-4o-judged score 等于生产 extraction correctness，也不证明 4B model 对 open-ended VLM、多语言、
  多图、复杂 PDF 或 high-stakes documents 普遍可靠。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：多层 additive injection 缩短视觉
  evidence 到不同 computation depths 的路径，但把 vision-layer map、Q-Former/spatial grouping、image
  processor、special token、LLM layer count 与 weights 绑定成更强的 architecture identity。任何 encoder、
  tiling、processor、token id、layer numbering 或 Transformers implementation 漂移都可能 silent-change
  semantics；八路 feature state 也增加 activation/memory、kernel integration、quantization 与 serving
  compatibility burden。单一 final-layer projector 在通用 VLM、低分辨率输入、模块可替换性优先或证据
  不足时仍更简单；OCR/layout pipeline 在 deterministic extraction、可审计 schema 与低 hallucination
  tolerance 场景仍合理；只增加 visual-token budget 在 GPU/SLO 允许且希望减少 architecture coupling 时
  仍是可比较分支。
- **Evolution / ROADMAP / Target and Adjacent Chapters / Existing Coverage**：这是 `Direct Evolution` 与
  `Layering / Dependency`：single late projector → token compression + multi-depth semantic injection +
  multi-spatial detail injection。主 owner 暂定 Ch17，因为它改变 external modality 对 residual stream 的
  layer-wise update contract；已读 Ch17 与相邻 Ch14～16、Ch18，并联读 Ch5、Ch23、Ch38/45/62。Ch5
  已拥有 representation/inductive-bias 边界，Ch23 已拥有 image transformation→visual tokens→label lineage，
  Ch45 已拥有 model-to-runtime artifact identity；它们不重复架构。Ch17 当前只覆盖 self-contained block，
  尚未说明 external feature 可以作为 versioned additive update 进入多个 residual depths。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch17；Ch23/45/62 short handoff。Historical Books Gate 关闭，不修改 Books；只同步 W18、
  年度索引、Learning State 与 2026-08-10 Daily。待验证 launch-day immutable model/data manifest、完整
  training recipe、Layer/SpatialDeepstack 与 compression component ablations、matched visual-token/FLOP
  baseline、judge-independent extraction audit、多语言/多图/OOD slices、end-to-end TTFT/TPS/memory/SLO、
  processor/runtime version matrix 与 failure injection。

### Full Source Review — Granite Speech 4.1 2B NAR — 27/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-SPEECH-41-NAR-CONDITIONAL-EDITING`；
  W18；`TN 5 / SI 4 / PV 5 / SR 4 / PR 5 / L 4 = 27/30`；official model artifact/card 与 related
  primary paper。System Impact 为 4 而非 5：它对 ASR latency/throughput 很重要，但不是可直接外推到任意
  autoregressive generation 的通用替代；Source Reliability 为 4，因为 weights、custom code、card 与全文
  论文公开，但 artifact training/evaluation 与论文 controlled runs 并非同一 frozen configuration，也没有
  独立复现或 production SLO。
- **Event Date / First-public Date / Revision History / Access and Verification Status**：IBM Granite 4.1
  family 于 2026-04-29 发布，NAR artifact/card 以 `Release Date: April 2026` 纳入 W18 release family。
  直接机制论文 NLE arXiv:2603.08397 只有 v1，于 2026-03-09 first-public；它是 W11 related primary source，
  不是 W18 新论文事件。current artifact commit-history 页面本次仍返回访问错误，因此不能声称已经冻结
  launch-day revision。`Related Paper Full Read Complete; Current Artifact/Card Complete; Event-time Commit
  Lineage Unverified`。
- **Full-read Coverage**：已阅读全文 metadata、Abstract、Introduction、Background/Related Work、Method
  3.1～3.7、全部公式、训练/数据/evaluation setup、controlled baselines、component ablations、blank-density
  sensitivity、multi-step editing、error analysis、inference breakdown、Discussion、Limitations 与 Future Work；
  并读取 current card 的 evaluation、usage/runtime constraints、architecture、data、infrastructure、limitations
  与 related-paper graph。论文没有公开 code repository、多个 seed/CI、端到端 streaming/production trace、
  power/cost、failure injection 或 artifact digest；对应字段为 `Not Disclosed`。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：CTC encoder 可以一次
  并行产生 frame/token alignment，吞吐高且行为受 acoustic evidence 约束，但语言先验较弱；AR speech LLM
  把强语言模型接到 acoustic embeddings 后，可改善 transcription 并支持 translation、punctuation、keyword
  bias 等更自由的 output contract，但每个 token 串行 decode，低 batch latency 尤其受限。对大量局部正确的
  CTC hypothesis，从头 autoregressive 重写全部 token 是重复 work；约束由“最大生成自由度”转向“在 acoustic
  evidence 与初稿附近快速修复”。NAR 因而不是否定 CTC 或 AR，而是把语言模型角色从 generator 改为
  conditional editor。
- **Mechanism / State Ownership / Control Flow and Data Flow**：current artifact 的 440M、16-layer Conformer
  CTC encoder 处理 16 kHz audio，使用 4 秒 block attention、layer 8 self-conditioning 与 character/BPE 双
  CTC heads；中层 blank probability 驱动 posterior-weighted pooling。约 160M 的 two-layer Window Q-Former
  拼接 encoder layers 4/8/12/16，并把 50 Hz 表示降到 10 Hz。1B Granite 4.0 base 移除 causal mask，使用
  attention/MLP LoRA rank 128 适配为 bidirectional editor。状态流为：

  ```text
  audio
  → frozen CTC encoder
  → acoustic embeddings + greedy character hypothesis
  → hypothesis retokenization
  → (blank, token, blank, token, ..., blank) insertion-slot sequence
  → projected acoustic embeddings || hypothesis embeddings
  → one bidirectional LLM forward
  → parallel copy / replace / delete / insert logits
  → CTC argmax + collapse
  → final transcript
  ```

  encoder 拥有 acoustic evidence 与 initial draft，projector 拥有跨模态 rate/shape conversion，editor 拥有
  position-wise edit distribution，CTC collapse 拥有 variable-length finalization。显式 insertion slots 允许局部
  插入；residual connection 与 tied embedding 形成 copying bias，辅助 copying-regularization 以较小权重
  约束不必要改写。最大 insertion capacity 与初稿 token 数相关；它不是无限长度自由生成。
- **Artifact / Paper Configuration Boundary**：NLE v1 controlled model 使用约 70K 小时、one-layer projector、
  LoRA rank 128、14M trainable parameters、3 epochs/180K steps；NLE++ 把 projector 扩成 two layers、LoRA
  rank 160、约 280M trainable parameters、5 epochs。current Granite artifact card 则写约 130K 小时、
  two-layer 160M projector、LoRA rank 128、16×H100/2 nodes、5 epochs/3 days。三者共享机制，但不是同一
  configuration：

  ```text
  NLE controlled experiment
  ≠ NLE++ enhanced paper run
  ≠ current Granite Speech 4.1 NAR artifact
  ```

  因此不能把论文 NLE/NLE++ 的 headline WER/RTFx 当作 current artifact 的直接结果，也不能把 current
  130K-hour data 或 card runtime requirements 倒写到 3 月论文实验。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：论文 controlled comparison 固定
  encoder、projector、LLM backbone、datasets、sampling 与 optimization，只改变 AR next-token decoding 与
  NAR editing；在 19 个 test sets、5 languages、single H100、BF16 greedy 下，batch 96 的 NLE/AR/CTC
  RTFx 为 1722/430/2584，batch 1 为 322/12/760，平均 WER 为 6.54/6.48/7.40。该 contract 支持“在作者
  controlled ASR setup 中，single-pass editing 接近 AR accuracy 并显著降低串行 decode cost”，不等于任意
  workload 的 latency speedup。NLE++ 为不同 compute/capacity run，Open-ASR WER 5.67、batch-96 RTFx
  1630，不能与 NLE controlled attribution 混写。current artifact card 又报告 batch 128、single H100、BF16
  greedy、Whisper English normalization 下约 1820 RTFx；它是第三个 contract。
- **Ablation and Failure Evidence**：论文分别移除 copying regularization、bidirectional attention、interleaved
  padding、audio embeddings、CTC hypothesis 与 LoRA；所有消融以 validation loss 为主，支持每个组件对
  作者训练收敛的贡献，但不是完整 WER/latency component matrix。blank slot 从 every-token 降为 every-2/3
  只带来很小 RTFx 增益并恶化 WER，因为序列仍由 acoustic tokens 主导。第二次编辑只把平均 WER 从
  6.54 降至 6.53，却把 RTFx 从 1722 降至 1259；第三次降到 1082 且 WER 回升 6.59，显示 editor 处理
  self-produced hypothesis 时出现 distribution mismatch。inference breakdown 中 encoder 占 66%、LLM 约
  30%、其余少于 4%，说明消除 AR seriality 后瓶颈迁移到 acoustic encoder，而不是“推理问题被消除”。
- **What the Evidence Proves / What It Does Not Prove**：证据证明 conditional editing 可把“CTC 初稿+
  acoustic evidence+语言先验”组织成单次并行 forward，并在作者 matched ASR contract 下形成 CTC 与 AR
  之间的 accuracy/speed trade-off；ablation 支持 acoustic grounding、hypothesis conditioning、bidirectional
  context、interleaved slots 与 LoRA adaptation 的作用。它不证明 27× 可迁移到 streaming、长音频、不同
  GPU/backend、quantization、beam search 或生产 concurrency；不证明 WER 相近等于 punctuation、translation、
  speaker attribution、timestamp 或 open-ended speech reasoning 相同；也不证明更低 insertion rate 等于更安全。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：NAR 将 serial token state 换成
  draft-quality、retokenization、slot capacity、bidirectional full-sequence attention 与 edit/collapse correctness。
  encoder/LLM tokenizer 不同时需要 GPU→CPU retokenization→GPU 往返；current runtime 又依赖真正尊重
  `is_causal=False` 与 sequence packing 的 attention backend。弱 CTC 初稿会把错误传给 editor；论文在
  CommonVoice multilingual slices 落后 AR，Portuguese 上甚至可能把较好 CTC 初稿改坏。NAR 偏向 deletion、
  降低 insertion/hallucination 的同时会漏词；多轮编辑还引入 train/inference distribution shift。CTC-only 在
  极低成本、streaming/chunking 与语言先验要求低时仍合理；AR 在输出与 transcript 差异大、accuracy/flexible
  generation、AST、punctuation、keyword 或 Japanese 更重要时仍成立；NAR 适合 latency-sensitive、局部编辑
  主导且可接受完整 context 的 ASR。
- **Evolution / ROADMAP / Target and Adjacent Chapters / Existing Coverage**：`Direct Evolution`：CTC-only
  parallel decode → AR speech LLM full regeneration → NAR draft-conditioned parallel editing → optional
  iterative/mask-predict refinement。主 owner 暂定 Ch40，因为它揭示“seriality 来自 output dependency，而不是
  所有 sequence tasks 的不可避免属性”；已重读 Ch38～41 与 Ch44。Ch40 已准确描述 autoregressive factorization
  和 token-by-token state，但尚未显式区分 constrained editing 可以改变 task factorization；Ch44 的 draft+
  verification 保持 target sampling distribution，而 NAR editor 直接改变 model/task contract，不能归入
  speculative decoding。Ch38 只接 artifact/runtime identity，Ch62 只接 WER/latency/feature-slice evaluation
  handoff。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch40；Ch38/44/62 short handoff。Historical Books Gate 关闭，不修改 Books；只同步 W18、
  年度索引、Learning State 与 2026-08-10 Daily。待验证 event-time immutable commit/config、artifact 对应的
  exact training/evaluation manifest、streaming/chunk contract、long-audio memory、backend portability、
  tokenizer-transfer overhead、multi-seed/CI、independent reproduction、failure injection，以及 AR/CTC/NAR
  在相同 punctuation/translation/keyword/task contract 下的完整 Pareto frontier。

### Full Source Review — Granite Speech 4.1 2B AR — 26/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-SPEECH-41-AR-MODALITY-ALIGNMENT`；W18；
  `TN 4 / SI 4 / PV 5 / SR 4 / PR 5 / L 4 = 26/30`；official model artifact/card、predecessor architecture
  paper 与 related self-speculative paper。Source Reliability 为 4：current weights/card 与完整 related papers
  可访问，但没有 4.1-specific technical report、frozen launch commit、完整 benchmark manifest、seed/CI 或
  independent reproduction。
- **Event Date / Revision History / Related Source Attribution / Access Status**：current card 明确 Release Date
  为 2026-04-29，故 artifact 归 W18。Granite-speech architecture paper arXiv:2505.08699 v1/v2 于
  2025-05-13/14 公开，属于 2025 source family；Self-Speculative Decoding arXiv:2603.11243 只有 v1，于
  2026-03-11 first-public，属于 W11 related family。两篇只用于重建演进与核验机制，不能在 W18 重复计分。
  current HF commit-history 页面仍访问失败，因此为 `Current Card/Artifact Complete; Related Papers Full Read;
  Event-time Revision Unverified`。
- **Full-read Coverage**：4.1 card 已覆盖全部 task prompt schema、architecture/config、174K-hour dataset table、
  training infrastructure、evaluation descriptions、current Transformers/vLLM/llama.cpp/MLX examples、limitations
  与 related sources。2025 architecture paper已读 metadata/revisions、overall architecture、data/license split、
  encoder/tokenizer comparisons、prompt construction、Q-Former equations、training/balanced sampling、projector/
  LLM comparisons、AST synthesis/filtering、safety experiment与结论。2026 Self-Speculative paper已读全部公式、
  method、training/evaluation setup、threshold sensitivity、verification-pass ablation、runtime breakdown、error
  analysis、limitations 与 conclusion。4.1 card 的主要 leaderboard figures 不是完整可重放 run manifest；
  artifact training optimizer/batch/precision、evaluation hardware/batch/decoding/seeds/CI 记为 `Not Disclosed`。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：dedicated CTC/RNN-T ASR
  将 acoustic modeling、alignment 与受限 vocabulary 放在专用模型中，吞吐、streaming 与声学忠实性较好，
  但 translation、punctuation、keyword prompt 和跨任务语言先验需要额外 pipeline。通用 text LLM 拥有语言
  与 instruction能力，却不能直接消费高频、变长 acoustic frames。Speech-aware AR 的核心问题不是“让 LLM
  听见音频”这句产品描述，而是建立一个压缩且可训练的 modality boundary，使 frozen/partly frozen acoustic
  representation 能进入 text embedding space，并让 prompt 选择输出 contract。约束从单一 ASR accuracy
  扩展为多语言 ASR/AST、格式化与 keyword control，同时保留小模型和开放 artifact。
- **Mechanism / State Ownership / Control and Data Flow**：4.1 artifact 使用 16-layer Conformer CTC encoder，
  16 kHz audio 经 80-bin log-mel 与 two-frame stacking 变为 50 Hz；4 秒 block attention 与 mid-layer
  self-conditioned CTC 保留局部 acoustic structure。character head 覆盖 European ASCII 与 Japanese phonetic
  Katakana，新增 BPE head 对齐 Granite tokenizer；mid-layer non-blank probability 为 posterior-weighted pooling
  提供 frame importance。two-layer Window Q-Former 对每 15 acoustic embeddings 使用每层 3 个 queries，
  再 5× downsample，总计 10×，向 LLM 提供约 10 Hz embeddings。运行流为：

  ```text
  waveform
  → acoustic feature extraction
  → CTC encoder: frame representation + character/BPE evidence
  → importance-weighted pooling + Window Q-Former compression
  → replace <|audio|> placeholder with projected acoustic embeddings
  → Granite 4.0 1B base intermediate checkpoint + jointly trained LoRA/projector
  → causal next-token generation under ASR/AST/punctuation/keyword prompt
  ```

  encoder 拥有 acoustic evidence，projector 拥有 temporal compression 与 representation-space bridge，prompt/
  tokenizer 拥有 task schema，causal LLM 拥有 output generation。card 只说 projector 与 LLM LoRA jointly
  trained，没有公开 exact LoRA rank/target modules；不能从 predecessor 或 NAR artifact 倒填。
- **Data / Training / Artifact Boundary**：card 列出约 174K hours，主要是 public ASR corpora，加 Japanese
  TTS、keyword 与 AST synthetic data；表内包括 48K MLS、46K LibriHeavy、24K Granary VoxPopuli、10K
  YODAS English、9.6K FineWeb-2→Japanese TTS、18K English→多语言 AST 与 3K X→English AST。模型用
  Granite 4.0 1B base 的 intermediate checkpoint 做 modality alignment；Blue Vela 上 8×H100 共 30 天，
  card 拆成 encoder 26 天与 projector 4 天。没有公开 synthetic generator revision、filter acceptance、exact
  manifest/digest、optimizer/batch/precision 或 full LLM adaptation schedule。2025 predecessor paper的 10-layer
  encoder、rank-64 LoRA、32×H100/660K updates 与 license-specific data split 不能当作 4.1 training recipe。
- **Evaluation Contract / Baselines / What It Proves**：4.1 card 声称在 `<8B` speech-language 和 dedicated
  ASR/AST systems 上评测，提供 April Open ASR figure、keyword F1、punctuation error rate 与 capitalization F1；
  但缺统一的 model revisions、hardware、batch、audio/token lengths、decoding、SLO、seeds/CI 与 machine-
  readable runs，所以仅保留 vendor evidence。2025 matched experiments支持 window Q-Former 相对 MLP/
  cross-attention 在作者 ASR setup 下更好，并给出 10 Hz compression trade-off；它不证明 4.1 dual-head 与
  frame-importance 是当前所有 gain 的因果来源。current card 的 174K data、dual head、Japanese/keyword/
  punctuation tasks 与 predecessor experiment 的 dataset/model不同，不能直接作 before/after ablation。
- **Related Self-Speculative Path and Boundary**：Self-Speculative paper复用 frozen CTC encoder 的 greedy
  hypothesis：先以所有 frame entropy 低于 `tau_CTC` 直接接受；否则让 causal LLM 一次并行检查 draft token
  likelihood，低于 `tau_SLM` 后从最长 accepted prefix 恢复 AR。single H100/BF16、adaptive 50K-token batch
  中，高-throughput operating point 报告 Open-ASR 4.4× RTFx 与 12% relative WER degradation；这是 threshold-
  controlled lossy policy，不是 Ch44 的 exact distribution-preserving speculative sampling。高-accuracy point
  的 WER 改善可能来自 CTC 与 AR error complementarity，但作者只给有限统计/定性解释。该机制是 W11
  related source，不等于 4.1 card 默认启用，也不用于证明 4.1 current runtime 性能。
- **What the Evidence Does Not Prove / Safety Boundary**：证据不证明 malformed prompt fallback 是安全边界，
  不证明 audio prompt injection、adversarial audio、spoofing 或 cross-modal jailbreak 已被覆盖。2025 predecessor
  safety test只把有限 benchmark toxic instructions 与 noise/corpus audio 配对，并观察复述/转录，不能外推到
  current 4.1、多语言、streaming 或 adaptive attacks。也不证明 current vLLM/llama.cpp/MLX compatibility 在
  4 月 29 日已存在；这些 current usage paths 是版本事实，需独立锁定 runtime/model revision。
- **Trade-offs / Failure Modes / Where Previous Designs Still Apply**：10× compression 降低 LLM audio-token
  cost，却可能丢失短促音素、speaker/timing与细粒度 alignment；dual heads 与 importance pooling增加 encoder
  state、vocabulary/tokenizer coupling 和 training cost。AR generation提供灵活 output schema，却带来 serial
  decode、language-model bias、hallucination、stop/tokenizer 与 prompt drift；synthetic AST/keyword data又引入
  teacher/filter provenance。dedicated CTC/RNN-T 在 streaming、低成本、严格 acoustic fidelity 与固定 schema
  下仍更合理；cascade ASR→MT 在模块独立审计、替换与 error attribution 优先时仍成立；AR speech LLM适合
  output schema 更丰富且可承担 latency/faithfulness gate 的场景。
- **Evolution / ROADMAP / Adjacent Chapters / Existing Coverage**：`Layering / Dependency` 与 `Direct
  Evolution`：dedicated acoustic model → compressed modality adapter + frozen/LoRA text LLM → dual-head,
  importance-weighted multilingual/task-conditioned artifact → CTC-draft speculative/NAR alternative decode。
  主 owner 暂定 Ch5：已重读 Ch5、Ch17、Ch38～40、Ch44 与 Ch62。Ch5 已说明 representation 只保留目标
  要求的信息，但尚未具体解释 modality adapter 是一个带 rate、information-loss、tokenizer 与 downstream
  objective 的系统 contract。Ch17 只接 feature injection/Transformer-layer handoff，Ch38/40 接 runtime/task
  state，Ch44 接 lossy verification boundary，Ch62 接 multi-task/slice/evaluation contract。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch5；Ch17/38/40/44/62 short handoff。Historical Books Gate 关闭，不修改 Books。待验证
  frozen launch card/commits、exact 4.1 training manifest、dual-head/frame-importance ablation、current artifact
  matched WER/AST/KWB/punctuation/latency contract、streaming/long-audio behavior、runtime compatibility matrix、
  prompt-injection/safety evaluation、synthetic-data provenance、independent reproduction 与 CTC/AR/NAR/cascade
  在相同 task schema 下的 Pareto frontier。

### Full Source Review — Granite Speech 4.1 2B Plus — 26/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-SPEECH-41-PLUS-STRUCTURED-TRANSCRIPT-STATE`；
  W18；`TN 4 / SI 4 / PV 5 / SR 4 / PR 5 / L 4 = 26/30`；official artifact/model card 与两篇 related
  primary papers。Technical Novelty 为 4：speaker attribution、word timestamp 与 incremental prefix 各有旧
  路线，长期价值来自把三者合并成同一 structured-transcript state contract，而不是某一新算子。Source
  Reliability 为 4：current weights/card 与论文可访问，但没有冻结 launch commit、Plus-specific technical
  report、component ablation、完整 run manifest 或独立复现。
- **Event Date / First-public Date / Revision History / Access and Verification Status**：Plus card 标记
  `Release Date: April 28, 2026`，归 W18。Speaker-attributed ASR 论文 arXiv:2604.11269 只有 v1，于
  2026-04-13 first-public；In-Sync timestamp 论文 arXiv:2604.22817 只有 v1，于 2026-04-14 first-public；两者
  均是 W16 related primary sources，不在 W18 重复计分。当前 card 的 Transformers `>=5.8` 与 vLLM
  `>=0.23` 是访问日兼容性事实，不能倒写为 launch contract；event-time commit/history 未冻结。
  `Current Artifact/Card Complete; Related Papers Full Read; Event-time Revision Unverified`。
- **Full-read Coverage**：已读 Plus card 的 task schema、speaker/timestamp/incremental examples、architecture、
  data construction、training infrastructure、evaluation、limitations 与 runtime requirements。SAA 论文已读
  metadata、Introduction/Related Work、speaker feature/cluster mechanism、synthetic conversation construction、
  training/evaluation、baselines、length sensitivity、overlap heuristic 与 conclusion。In-Sync 已读 metadata、
  architecture、timestamp-token formulation、multi-task training、三项 robustness 方法、全部公式、八个数据集、
  training contract、baseline/ablation、malformed-output handling、limitations 与 conclusion。两篇均未公开
  multi-seed/CI、production trace 或完整 failure injection；SAA 还未披露训练硬件/optimizer。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：传统 cascade 将 ASR、
  diarization 与 forced alignment 分成可替换模块，便于单独校准、重放和纠错；普通 speech LLM 则输出一个
  transcript，接口简单。会议转写、字幕与增量交互要求每个词同时携带“谁说、何时说”，并在下一轮继续
  使用已经提交的文本状态。约束因此从 token accuracy 扩展为 transcript、speaker identity、temporal order、
  prefix consistency 与 client-visible schema 的联合正确性；单一 WER 已不足以描述系统质量。
- **Mechanism / State Ownership / Control Flow and Data Flow**：Plus 沿用 16-layer Conformer、character/BPE
  dual heads、posterior-weighted pooling、two-layer Window Q-Former 与 Granite 4.0 1B causal decoder；输出端
  增加三类协议状态：

  ```text
  accumulated audio + task prompt + optional committed prefix_text
  → compressed acoustic embeddings
  → autoregressive structured transcript
       [Speaker N]: relative speaker identity by order of appearance
       [T:N] word timing in centiseconds modulo 1000
       text tokens
  → client-side speaker/session state + timestamp unwrapping
  → next incremental call reuses transcript prefix while audio is reprocessed
  ```

  acoustic encoder/projector 拥有 audio evidence 与 rate conversion；LLM 拥有结构化输出 grammar；conversation
  session 拥有 relative-speaker numbering 与已提交 prefix；client 必须拥有 modulo-1000 rollover/unwrapping、
  malformed sequence detection 与 correction policy。card 所称 incremental decoding 是“累积音频重新输入、
  prefix text 不再重新生成”，并不证明真正 streaming encoder、bounded recompute、KV reuse 或低延迟 SLO。
- **Related SAA Mechanism and Artifact Boundary**：SAA 论文使用 Granite-speech-v3.3-8B，而非当前 Plus 2B。
  frozen 16-layer CTC encoder 的 final output 与选定 intermediate layer 拼接，以保留 final linguistic evidence
  和较早 speaker cues；layer 3 最佳。只使用 relative `[Speaker N]` 只能区分会话内 speaker，作者另试 explicit
  speaker ID 与 WavLM-ECAPA embeddings 的 100～300 个 k-means cluster labels。训练数据由 MLS 与 Fisher
  片段合成 2～4 人轮流会话；fully overlapped short utterances 被丢弃，partial overlap 被串行化。论文在
  10/30/60/120 秒 chunks 上评估，WDER 只计算匹配/替换词并在最佳 label mapping 后计 speaker 错误，不含
  insertion/deletion。论文最佳 8B run 在 Fisher/CallHome/AMI/GALE 报告 0.9/2.1/7.8/12.2 WDER；当前 Plus
  card 在 2～5 分钟 segments 报告 0.9/2.2/14.6/30.2。模型大小、长度与 artifact 不同，数字不能合并或
  解释为回归/提升。
- **Related Timestamp Mechanism and Artifact Boundary**：In-Sync 同样使用早期 Granite-speech-8B：10-layer
  Conformer、MLP adapter、Granite-3.3-8B、frozen encoder/LLM 与 LoRA，而非 Plus 2B。它以等概率混合
  ASR/SRWT 任务，在每个 word 后生成一个 end-time token；6000 个 timestamp tokens 表示 10 ms increments、
  最大 60 秒。三项机制分别解决不同 failure：拼接 utterances 扩展长尾时间位置；Gaussian timestamp-
  embedding regularization 为本来无序的 token embedding 注入相邻时间拓扑；reduced teacher forcing 以
  `p=0.2` 将历史 timestamp 替换成较小值，暴露推理期 timing drift。训练使用 LibriSpeech/CommonVoice/
  AMI/VoxPopuli，400K AdamW steps、peak LR `1e-4`、1000 warmup、downsample 5、query/value LoRA rank 32/
  alpha 64、4 GPUs × batch 4；缺少 GPU 型号、精度、seed/CI。current Plus 改用 centisecond modulo-1000
  tags 并声称支持更长输入，所以论文的 6000-token/60-second encoding 与结果不能直接归属当前 artifact。
- **Evaluation Contract / Ablations / What the Evidence Proves**：SAA 对 PyAnnote+Whisper/Granite pipeline 与
  NeMo 比较，并显示 intermediate speaker cue、explicit ID/cluster tags 与 chunk length 的作用；但 synthetic
  alternating conversations 缺少真实 overlap/turn dynamics，NeMo 在 GALE 的 WDER 11.5 还优于论文最佳
  12.2。In-Sync 在八个 datasets 报 WER、Average Alignment Score 与 malformed rate；缺 timestamp labels
  时使用 Montreal Forced Aligner，并把每个 word start 强制设为前词 end。naive multi-task timestamp supervision
  会降低 ASR，length augmentation 对长语音改善但在短语音产生 distribution mismatch；regularization 与
  reduced teacher forcing 各自有效，却因 noise 破坏 monotonic topology 而不能良好叠加。mismatched word/
  timestamp samples 被排除出 AAS 并单报 MAL。这些证据支持“结构化 transcript 需要专门的数据与训练
  robustness”，不证明 current Plus 的 WER/WDER/AAS 由相同机制因果产生，也不证明 production calibration。
- **What the Evidence Does Not Prove / Safety Boundary**：公开材料不证明 speaker label 跨 session 稳定、
  timestamp 在 rollover/长音频/重试后仍单调、prefix error 可安全修正、overlap/噪声/code-switching 已充分
  覆盖，或 incremental mode 的 compute/latency 有界。Plus 不输出 punctuation/capitalization；这不是小缺口，
  而是 task schema 的显式 trade-off。card 的安全段落是 vendor limitation/usage guidance，没有 prompt-
  injection、speaker-spoofing、PII、consent、fairness 或 multilingual safety operating point，不能升级为保证。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：统一生成降低 ASR→diarization→
  alignment 的跨模块 error propagation，却牺牲独立模型替换、单项校准、确定性重放和局部修复。relative
  speaker numbering 可能在 chunk/retry 后重排；cluster taxonomy 可能漂移；prefix error 会变成后续不可见的
  conditioning debt；timestamp modulo rollover、missing/duplicate/out-of-order tags、word/tag mismatch 与 client
  unwrap state 丢失会 silent-corrupt timeline；MFA/CTC/human labels 的不同 provenance 又限制 ground truth。
  cascade 在强 streaming、独立 diarization/alignment audit、外部纠错与 strict timestamp SLA 下仍合理；普通
  ASR 在只需文本时更低复杂度；统一 Plus 适合 schema-rich transcription 且 client 能承担 session state 和
  validation 的场景。
- **Evolution / ROADMAP / Target and Adjacent Chapters / Existing Coverage**：关系为 `Layering / Dependency`
  与受限的 `Direct Evolution`：plain transcript → cascade diarization/alignment → unified relative-speaker/time
  tokens → robustness training → prefix-conditioned incremental transcript。主 owner 暂定 Ch38，因为 durable
  增量是 request/session state、committed prefix、output grammar 与 client unwrap/validation contract，而不是
  某个 speech benchmark。已重读 Ch38 与相邻 Ch37/39，并联读 Ch5、Ch40、Ch44、Ch62；Ch38 已拥有
  request state/identity，但尚未具体说明 structured output 可能把 session lifecycle 分摊给 model、runtime 与
  client。Ch5 只接 modality representation，Ch40 接 AR seriality，Ch62 接 WER/WDER/AAS/MAL 与 slice contract。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch38；Ch5/40/62 short handoff。Historical Books Gate 关闭，不修改 Books；只更新 W18、
  年度索引、Learning State 与 2026-08-10 Daily。待验证 frozen launch card/commit、Plus-specific training
  manifest、与两篇 8B paper 的真实 lineage、speaker/timestamp component ablation、overlap/code-switch/
  long-audio slices、prefix-correction/rollback semantics、incremental compute/KV/latency contract、timestamp
  rollover failure tests、independent reproduction，以及与 modular cascade 的 matched Pareto frontier。

### Full Source Review — Granite Guardian 4.1 8B — 26/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-GUARDIAN-41-POLICY-CONDITIONED-JUDGE`；
  W18；`TN 3 / SI 5 / PV 5 / SR 4 / PR 5 / L 4 = 26/30`；official model artifact/card/docs 与 related
  primary paper。Technical Novelty 为 3：binary generative guard、risk taxonomy、RAG groundedness 与 custom
  criteria 都有前代基础；4.1 的增量是把 BYOC、多约束检查、hybrid think/no-think、function-call judging 与
  Best-of-N reward use 合并到同一 policy-conditioned interface。Source Reliability 为 4：weights、initial commit、
  card、docs 与 2024 paper 可核验，但没有 4.1-specific technical report、训练 manifest、threshold calibration、
  multi-seed/CI、deployment incident study 或独立复现。
- **Event Date / Revision History / Access and Verification Status**：Granite 4.1 family release 为
  2026-04-29；Guardian card 标记 `Release Date: April, 2026`，HF initial artifact commit 为 2026-04-16，故
  作为 W18 release family。related Granite Guardian paper arXiv:2412.07724 v1 first-public 于 2024-12-10，
  只核验前代机制和数据/评测边界，不在 W18 计为新论文。current card/docs 是访问日状态，不能证明所有
  wording、runtime snippets 或 benchmark rows 在 4 月 29 日冻结不变。`Current Artifact/Card/Docs Complete;
  Predecessor Paper Full Read; 4.1 Training and Frozen Evaluation Artifact Not Disclosed`。
- **Full-read Coverage**：已读 current docs/card 的 What's New、prompt grammar、think/no-think、pre-baked/
  custom criteria、training-data summary、OOD safety、function-calling、BYOC、RAG groundedness、JETTS
  Best-of-N tables、usage 与 scope limitations。2024 paper已读 metadata、risk taxonomy、human annotation、
  uncertainty sampling、synthetic harmful/jailbreak/RAG data、SFT、score formula、benchmark construction、
  baseline adaptation、results、deployment guidance、limitations 与 taxonomy/template appendices。4.1-specific
  optimizer、batch、hardware、data counts/mixture、criterion generator、reward-training recipe 与 exact evaluation
  harness 均为 `Not Disclosed`。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：规则过滤器和专用小
  classifiers 的政策边界固定、延迟低、可校准；单一 safety taxonomy 的 generative guard 可理解语义并统一
  prompt/response/RAG 检查，但 policy changes 往往需要重训或重新编码。Agent/RAG/workflow 又要求判断
  function-call semantics、groundedness、多项格式/领域要求，甚至在多个候选中排序。约束从“检测固定风险”
  变成“让自然语言 criterion 成为 versioned runtime policy”，同时仍需可审计 operating point 和 fail-safe
  enforcement。
- **Mechanism / State Ownership / Control Flow and Data Flow**：4.1 基于 Granite 4.1 8B fine-tune。调用方把
  conversation、documents/tools、criterion、yes/no scoring schema 与 think/no-think selector 编入末尾
  `<guardian>` block；模型以 `<think>` 与 `<score>` grammar 返回解释和判断：

  ```text
  policy/risk definition + selected evidence + conversation/tool state
  → versioned guardian prompt template
  → think mode: reasoning trace → yes/no score
    or no-think mode: empty trace → yes/no score
  → parser / threshold / Best-of-N selector
  → allow, block, retry, escalate, rank or observe
  ```

  policy owner 定义 criterion/taxonomy；application/runtime 拥有 evidence selection、prompt assembly、mode、
  parser、threshold 与 enforcement；guardian artifact 拥有 conditional judgement；audit layer 必须保存 model/
  policy/template/evidence/threshold/action identity。自然语言 criterion 不是 enforcement 本身；`yes/no` 的
  方向还取决于 criteria wording。思维文本是未受信的 explanation，card 明确说可能含不安全内容且不忠实。
- **Predecessor Mechanism and 4.1 Boundary**：2024 paper 将 prompt/response/context/label 统一为 safety
  template，以 risk-definition control tokens 参数化任务；Granite 3.0 instruct 2B/8B 经 SFT 学习首 token
  `Yes/No`。风险分数把 top-20 中包含 yes/no 的 lexical variants 的 likelihood 分别求和再 softmax，部署者
  自选 threshold。数据包括三人独立 human annotations、低置信样本主动抽样、taxonomy-guided benign/
  harmful/jailbreak synthesis 与 HotPotQA/SQuAD/MNLI/SNLI 衍生 RAG negatives。这个 paper 证明前代
  taxonomy-conditioned detection path，不证明 4.1 BYOC、hybrid reasoning、function calling 或 Best-of-N 的
  training recipe；4.1 card 只给 human/synthetic data 概述，不能把 2024 data counts/optimizer 倒填。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：2024 paper 在 8 个 safety 与 9 个
  TRUE groundedness datasets 上报告 F1/AUC，并适配 Llama Guard、ShieldGemma、ANLI-T5、WeCheck、
  MiniCheck baselines；作者也明确 risk taxonomy mapping、subsampling 与固定-threshold F1 会影响比较。
  4.1 card 分别报告 OOD F1、function-calling BAcc、IFEval/InfoBench BYOC BAcc 与 JETTS verifiable-task
  Best-of-N selection。关键负结果是 think mode 并非单调更好：多个 OOD/function/BYOC rows 中 no-think
  相当或更高。JETTS 的 overall 70.29 仍低于 oracle 81.54，并且只覆盖 math/code/instruction-following 的
  verifiable tasks。card 没有统一 hardware、precision、input/output length、batch/concurrency、latency/
  throughput、threshold sweep、ECE/Brier/calibration、seed/CI 或 adaptive-attack contract；所有 headline 只
  保留为 vendor experiments。
- **What the Evidence Proves / What It Does Not Prove**：artifact/docs 证明 4.1 提供一套 criterion-conditioned
  yes/no judge interface、两种 reasoning modes、function/RAG/safety presets 与 BYOC；card 的内部评测支持
  fine-tuned judge 在列出的 static benchmarks 上优于其若干前代/baselines。证据不证明 arbitrary criterion
  都被“faithfully”执行，不证明 score 是 calibrated probability，不证明 chain-of-thought faithful，不证明
  guard 对 adaptive prompt injection、policy conflict、multilingual/OOD/domain shift 稳健，也不证明
  Best-of-N 分数适合不可验证、高风险或开放式任务。它更不等于 authorization、sandbox、policy engine、
  human review 或 incident response。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：BYOC 降低 policy onboarding 成本，
  却把歧义、冲突、版本漂移、criterion injection 与 parser direction 加入安全边界；unified judge 减少模型数，
  却形成 correlated blind spot 和单点失败；think mode 提供审阅线索但增加 latency/token cost、unsafe trace
  exposure 与 rationalization risk；no-think 更低成本却更难调查。Best-of-N 可把 guard 变成 selector，却扩大
  candidate-generation compute，并可能选择最会取悦同源 judge 的输出。规则/小 classifier 在清晰高频 policy、
  strict latency 与可校准阈值下仍合理；多层 deterministic controls 在 authorization/data-loss prevention 场景
  仍不可替代；human escalation 在高损失、低 base-rate、criterion ambiguous 时仍必要。
- **Evolution / ROADMAP / Target and Adjacent Chapters / Existing Coverage**：关系为 `Direct Evolution` 与
  `Layering / Dependency`：fixed rule/classifier → taxonomy-conditioned generative detector → custom natural-
  language criterion → optional reasoning trace → gate/monitor/Best-of-N selector。主 owner 暂定 Ch68，因为
  核心是 threat/policy/evidence/operating-point 到 enforcement 的 safety control chain；已重读 Ch68 与相邻
  Ch67/69，并联读 Ch62、Ch72、Ch77。Ch62 已拥有 evaluator identity、threshold/calibration 与 judge coupling，
  Ch69 拥有 deployment gate，Ch77 拥有 workflow retry/escalation；若未来 Books Gate 打开，Ch68 只需补足
  natural-language policy 本身也是需版本化、验证和最小权限约束的 executable control input，不复制 benchmark。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Version-Grounded)` / Ch68；Ch62/69/77 short handoff。Historical Books Gate 关闭，不修改 Books；只同步
  W18、年度索引、Learning State 与 2026-08-10 Daily。待验证 4.1-specific data/training manifest、criterion
  distribution、policy conflict/negation tests、threshold/calibration curves、base-rate/fairness/multilingual slices、
  adaptive attacks、reasoning faithfulness/leakage、runtime cost/SLO、failure-injection、independent reproduction、
  cross-model transfer，以及 gate/monitor/ranker 三种 enforcement mode 的 matched evaluation。

### Full Source Review — Granite Embedding 97M Multilingual R2 — 27/30

- **Candidate / Week / Score / Source Family / Type**：`GRANITE-EMBEDDING-R2-COMPACT-RETRIEVAL-IDENTITY`；
  W18；`TN 4 / SI 5 / PV 5 / SR 4 / PR 5 / L 4 = 27/30`；official artifact/card/repository 与 later-public
  primary paper。Source Reliability 为 4：weights、config、ONNX/OpenVINO artifacts、card、code repository 与
  完整论文公开；但 paper 晚于 release，April frozen card/benchmark manifest、训练数据 digests、多个 seeds/
  CI 与独立复现没有公开。
- **Event Date / First-public Date / Revision History / Access and Verification Status**：artifact card 明确
  Release Date 为 2026-04-29，属于 W18。Granite Embedding Multilingual R2 paper arXiv:2605.13521 v1 于
  2026-05-13 first-public、v2 于 5 月 14 日修订，属于 W20 publication node；它可核验同一 released model
  family 的机制与后续 dependency incident，不能倒写成 4 月 29 日已经公开的 technical report。current card
  吸收了论文及 Transformers 5.8-era 内容，不是 immutable launch snapshot。`W18 Artifact Release Verified;
  W20 Related Paper Full Read; Event-time Card and Run Manifest Unverified`。
- **Full-read Coverage**：已读 current 97M card 的 model details、language/code scope、usage/backends、
  evaluation、architecture、training/data/governance、infrastructure 与 limitations；已核对 repository surface。
  论文已读 metadata/revisions、Introduction、ModernBERT encoder/tokenizer fertility、三阶段 MLM pretraining、
  retrieval data、contrastive/KD/context-extension/model-merge/vocabulary-pruning/teacher mechanism、stage
  ablation、quality/speed evaluation、全部 detailed retrieval、per-language、context scaling、runtime-regression
  Appendix 与 training hyperparameters。论文没有独立 Limitations section；card 的 language/vocabulary/
  truncation caveats 与 paper 的 negative/per-language/runtime evidence共同构成边界。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint**：XLM-R-based multilingual
  bi-encoders 在 512-token、固定词表和中小语料检索中拥有成熟兼容性、低成本与稳定 serving；较大的 311M
  encoder 和 768-dimensional index 提供更高容量。企业 retrieval 同时要求更多语言/代码、长文档、跨语言
  query、许可治理和高吞吐，且 vector dimension 会直接放大 index memory/network cost。约束因此变成联合
  优化 tokenizer fertility、context、student capacity、vector width、quality 与 ingestion throughput，而不是
  只追求一个 MTEB 分数。
- **Mechanism / State Ownership / Control Flow and Data Flow**：97M model 从 311M ModernBERT multilingual
  model 剪到 12 layers，并将 vocabulary 从 262K 选择为 180K、embedding width 固定为 384。模型以 CLS
  pooling 与 L2 normalization 生成 query/passage vectors，cosine similarity 承担 retrieval score：

  ```text
  multilingual/code corpus
  → tokenizer selection + staged MLM encoder pretraining
  → multilingual/cross-lingual/code/conversational/synthetic pairs + hard negatives
  → contrastive fine-tuning
  → language-routed teacher score distribution distillation
  → 4K training extension / 32K accepted artifact
  → 97M encoder + 384-d normalized vector
  → versioned ANN index / retrieval results
  ```

  training pipeline 拥有 tokenizer、data mixture、teacher routing 与 checkpoint lineage；artifact 拥有 model/
  tokenizer/pooling/normalization/max-length contract；retrieval platform 拥有 chunking、truncation、vector
  dimension、index build、similarity metric 与 re-embedding migration。任何一项变化都会改变 vector identity；
  新旧 embeddings 不能因 shape 相同就静默混入同一 index。
- **Training / Distillation / Artifact Boundary**：base encoder先以 2.5T tokens、1024 context 训练，再以
  600B tokens 扩到 8192、RoPE theta 160K，最后对三种 language-mixture variants 做 decay training/linear
  merge；compact initialization 又复用 English small model 的共享 token rows、新 token 用平均 embedding。
  retrieval stage使用改进 contrastive objective、large in-batch negatives、English 与 multilingual 两个 teacher
  的 language-routed score-distribution KD、512→4K context extension；97M 的 FT/KD/extension 分别为 global
  batch 9600/256/128、40K/12K/10K steps、LR `1e-4/8e-5/8e-6`。card 宣称 max 32,768，但 retrieval long-
  context training只明确到 4K；32K 能力由 inference evaluation 支持，不等同于 32K retrieval-pair training。
- **Evaluation Contract / Ablations / Sensitivity / Overhead**：论文按 ML MTEB 18 tasks、English 10、Code
  12、LongEmbed 6、RaR-b 17 报 aggregate；不同 suites 使用 1024、8192 或 32K max length。stage ablation
  只针对 311M cumulative checkpoints，显示 contrastive、KD、context extension 和 model merge 的边际变化，
  不能直接归因 97M 的 pruning/vocabulary choices。speed 表在 single H100、batch 512、512-token inputs 下
  比较；Transformers 4.57.6 的 97M 为 3268 docs/s，而 5.8.0 为 2534，差异来自 5.1 移除 full-model
  unpadding，并非权重回归。paper 还显示 97M 在 18-language MIRACL average 低于旧 278M，且多个具体语言
  回归；311M 在 English retrieval 低于 English-only 149M。证据因此是 Pareto surface，不是单向替代。
- **What the Evidence Proves / What It Does Not Prove**：证据支持 pruning、vocabulary selection、多教师 KD
  与 contrastive/long-context training 可在作者 contracts 下形成 compact multilingual retrieval point；32K
  truncation sweep 在 LongEmbed 上有增益；dependency version 能在权重不变时显著改变 throughput。它不证明
  200+ languages 具有同等质量；只有 52 languages 有显式 retrieval-pair support，paper 的 MIRACL 也只有
  18 languages。它不证明 32K accepted length 等于任意真实长文档的 useful context，不证明 MTEB/LongEmbed
  等于特定企业 corpus relevance，也不证明 ONNX/OpenVINO/vLLM/GGUF 在所有精度/hardware 上数值等价。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：12-layer/384-d/vocabulary pruning
  降低 model/index cost，却损失部分 language/quality capacity并改变 token fertility；长 context 减少 chunk
  fragmentation，却放大 quadratic/local-attention、padding、tail latency 与 truncation policy coupling；多
  teacher KD 提高覆盖，但把 teacher selection/bias/version 注入 student lineage；synthetic query 与 LLM-judge
  false-negative filtering带来同源偏差。311M/768-d 在 quality优先时仍合理；English-only model 在单语
  workload 更优；BM25/sparse/hybrid retrieval 在 exact term、rare entity、可解释 lexical match 和 low-resource
  language 下仍不可替代；固定旧 dependency 在 SLO 稳定期可合理保留，升级应走 replay/canary。
- **Evolution / ROADMAP / Target and Adjacent Chapters / Existing Coverage**：`Direct Evolution`、`Layering /
  Dependency`：XLM-R/512 → ModernBERT/long context → multilingual/cross-lingual contrastive retrieval →
  multi-teacher KD → layer/vocabulary/vector pruning → dependency-aware serving/index migration。主 owner 暂定
  Ch72，因为 embedding artifact、chunking、index 与 retriever共同形成 RAG representation identity；已重读
  Ch72 与相邻 Ch71/73，并联读 Ch22、Ch45、Ch62。Ch72 已覆盖 retriever/index lineage，但尚可更明确记录
  vector dimension、tokenizer/pooling/normalization 与 runtime dependency 是同一 index compatibility key。
  Ch22 只接 trained/accepted/effective context，Ch45 接 artifact/backend matrix，Ch62 接 language/suite/SLO
  evaluation contract。
- **Final Disposition / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Version-Grounded)` / Ch72；Ch22/45/62 short handoff。Historical Books Gate 关闭，不修改 Books；只同步
  W18、年度索引、Learning State 与 2026-08-10 Daily。待验证 immutable April card/config、artifact/paper
  exact lineage、97M pruning/vocabulary ablation、52-language and low-resource confidence intervals、real corpus/
  hybrid retrieval、ANN recall/index-memory/rebuild cost、long-document latency/memory、quantized backend parity、
  independent reproduction，以及 dependency-upgrade canary/rollback contract。

### Full Source Review — FAMA: Failure-Aware Meta-Agentic Framework — 27/30

- **Candidate / Week / Score / Source Family**：FAMA；W18；27/30（TN 4 / SI 5 / PV 5 /
  SR 4 / PR 5 / L 4）；`FAMA-FAILURE-CONDITIONED-AGENT-SUBSET`。
- **Source Type / Dates / Revision / Access**：ACL 2026 Findings accepted paper；arXiv:2604.25135
  于 2026-04-28 02:21:53 UTC 提交，当前只有 v1。2026-08-10 已重新打开 arXiv metadata 与
  experimental HTML，完成主文及 Appendices A～G 阅读；arXiv 页面没有列出作者 code、dataset 或
  immutable experiment artifact，故实现可用性记为 `Not Disclosed`，不把同名第三方 package 当作论文代码。
- **Full-read Coverage**：已覆盖 Introduction、Related Work、Problem、完整 Method/Algorithm 1、四类
  failure taxonomy、三套 benchmark contract、全部主结果、memory-size/agent-combination/judge-model/
  thinking-overflow/self-reflection ablations、token/latency table、Limitations、failure definitions、selected
  component tables 与 Appendix G。正文现已可访问，先前 `Access Blocked` 状态撤销。
- **Original Problem / Why Previous Design Was Reasonable**：ReAct、function calling 或固定的全量 helper
  scaffold 在没有历史 failure profile、任务短且 context 充足时简单、可复现，也避免额外 diagnosis call。
  但长时 tool-use trajectory 的错误不是单一“推理不足”：domain-policy violation、复杂 tool output
  retrieval、context misinterpretation 与 incomplete fulfillment 会累积；把 Memory、DCE、TOR、TSA、Planner、
  Verifier 全部塞入每个请求又会挤占 context、延长 critical path，且不同模型/领域需要的组件不同。
- **Changed Constraint / Principle**：约束从“为任务选择一个静态 Agent scaffold”变成“已经观察到特定
  model/task 的失败轨迹，但 context 与 inference budget 有限”。核心原则不是多 Agent 数量，而是把失败
  evidence 编译成最小的 context/role intervention：只有能覆盖主要 failure class 的 helper 才进入下一次执行。
- **Mechanism**：Stage 1 先执行 baseline，并只收集 reward 为 0 的完整 trajectories；针对四个预定义
  error categories，各自的 analysis agent 输出 categorical decision 与 rationale。Stage 2 将这些输出与完整
  trajectory 拼接给 orchestrator 做 dominant-failure attribution，再由 mitigation agent 把 failure class 映射为
  `A* ⊂ {DCE, TSA, TOR, Planner, Verifier, Memory}`。所选 helper 的输出作为 target tool-use agent 的 prior
  context，随后重跑任务。Algorithm 1 返回的是 task-conditioned subset，不是一个对所有 workload 固定的
  全局 topology。
- **State Ownership / Control Flow / Data Flow**：benchmark/environment 持有 reward 与 tool state；baseline
  run 持有原始 conversation/tool trajectory；四个 analyzer 只提出 failure evidence；orchestrator 持有聚合
  attribution；mitigation agent 提出 component subset；workflow/runtime 才应持有最终 topology version、
  token/tool budget、retry 与 deployment authority。数据流是 `failed trace → per-class analyses → attributed
  errors → selected helpers → injected context → rerun → environment reward`。论文没有定义持久化 lineage、
  cache invalidation、跨版本迁移或线上并发控制。
- **Implementation Details**：论文使用固定 component pool。`tau`-bench/`tau`-trait 主要从 Memory、DCE、
  TOR、TSA 中选；ACEBench 另允许 Planner 与 Verifier。Table 1 指出 IRMA/FAMA helper backbone 为
  Qwen2.5-72B-Instruct；GPT-4o 与 GPT-4.1-mini 被用于 judge-consistency check。Memory 仅保留最近 `k`
  个 user queries，作者在不同 domain/model 上选择 `k∈{2,4,6}`。公开材料未给出 prompts 的 immutable
  artifact、runtime code、hardware、precision、sampling parameters、并发、完整 token limit、API revision
  或部署 SLO。
- **Evaluation Contract**：tool-calling agents 为 Qwen3 4B/14B/32B 与 Qwen2.5-72B；user simulator 固定为
 作者筛选出的 Qwen2.5-72B-Instruct；`tau`-bench Airline/Retail、`tau`-trait Telehealth/Telecom 与 ACEBench
  30 个 multi-turn tasks 构成评测。`tau` 系列报告五次运行的 `pass^k`，ACEBench 报 End-to-End / Process
  Accuracy；另比较 FC、ReAct、IRMA、Self-Reflection、不同 helper subsets、judge model 与 memory window。
  作者的 Qwen3-32B token/latency table显示 FAMA helper overhead 约 30%，低于 IRMA 的 50%～58%，但没有
  hardware、serving stack、concurrency 或 SLO，故这些数字只属于作者配置，不能写成生产 latency 结论。
- **What the Evidence Proves**：在作者的 structured conversational benchmarks、模型、simulated user、
  failure taxonomy 与 rerun protocol 下，固定地启用全部 helpers 并不稳定；failure-conditioned subset 在多数
  reported cells 提高 task success，且合适 memory window 依 domain 而变。结果支持“coordination/context
  tax 必须与 failure coverage 一起度量”，也支持同一 topology 不应静态套用所有模型与领域。
- **What It Does Not Prove / Threats to Validity**：Algorithm 先用同一 task 的失败 outcome 与完整 trajectory
  选择 helper，再重跑该 task；公开材料没有清楚给出 calibration/evaluation task 隔离，因此不能证明 cold-start
  routing、未见任务 generalization 或因果 failure attribution。error taxonomy 与 orchestrator 没有 human-gold
  precision/recall；GPT judge 一致只说明两个相关模型给出相似 top category，不等于正确。user 与 helper
  simulation、task selection、无 artifact、无 seed/CI 与 incomplete runtime contract 进一步限制外推。论文
  声称 thinking variants 较差也只对应其 token limit 与 tool-use protocol，不能否定 reasoning model。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：按 failure 选 helper 可少注入无关
  context，却新增一次失败的前置成本、taxonomy drift、misattribution、helper-selection instability、同源模型
  correlated error、context poisoning、rerun side effects 与 stale recommendation。低风险短任务、无历史失败、
  deterministic verifier 充分或首次成功率高时，single Agent / ReAct 仍更便宜；组件需求稳定时，固定 Workflow
  比每次 LLM routing 更可复现。高副作用任务不得把一次失败当成可安全重放许可。
- **Evolution Relationship**：`Direct Evolution`：static all-agent scaffold → trace-conditioned failure diagnosis
  → minimal helper subset；对 Ch76 的 `localize/attribute/repair` 是 `Layering / Dependency`，对 Ch78 的
  task-topology matching 与 bounded topology repair 是 mechanism-level confirmation，而非新的替代路线。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch78；已读 Ch76～80，
  并核对 Ch75 的 plan contract。Ch76 已明确 failure class、evidence-backed attribution、repair boundary 与
  stopping；Ch78 已覆盖 single-Agent baseline、coordination tax、task-topology matching、trace-triggered
  bounded mutation、state ownership 与 correlated judge；Ch77/80 已持有 replay、budget、identity、policy
  和 side-effect recovery。FAMA 没有补出这些章节尚缺的长期机制，只提供一个受限实验实例。
- **Integration Decision / Changed Files / Open Questions**：`No Change — Already Covered` / Ch78；Ch76
  与 Ch77 只保留 evidence handoff。Historical Books Gate 关闭，不修改 Books。待验证 held-out failure-profile
  split、human-gold attribution、first-attempt-inclusive cost/success、immutable prompts/code、真实 user/production
  tool state、side-effect-safe rerun，以及不同 backbone/agent pool 版本变化时 recommendation 的 invalidation。

### Full Source Review — Toward Scalable Terminal Task Synthesis via Skill Graphs — 28/30

- **Candidate / Week / Score / Source Family**：Toward Scalable Terminal Task Synthesis via Skill Graphs
 （SkillSynth）；W18；28/30（TN 5 / SI 5 / PV 5 / SR 3 / PR 5 / L 5）；
  `SKILLSYNTH-SCENARIO-SKILL-TRAJECTORY-COVERAGE`。
- **Source Type / Dates / Revision / Access**：Tencent Hunyuan Team research paper；arXiv:2604.25727
  于 2026-04-28 14:53:59 UTC 提交，当前只有 v1；PDF 扉页日期为 2026-04-29，仍属于 W18。
  2026-08-10 已完成 arXiv HTML、15 页 PDF 与 Appendices A～E 阅读。arXiv 没有列出 official code、dataset、
  generated tasks、graph snapshot 或 training checkpoints，artifact availability 为 `Not Disclosed`。
- **Full-read Coverage**：已覆盖 problem formulation、scenario/skill 公式、objective decomposition、三阶段
  graph construction、inverse-frequency Algorithm 1、planner/constructor/dual-verifier/repair harness、SFT 与
  Terminal-Bench setup、harness yield、main results、single-/random-multi-skill ablation、diversity/error analysis、
  Related Work、equivalence proof、clustering discussion、training hyperparameters、graph statistics 与 prompts。
- **Original Problem / Why Previous Design Was Reasonable**：扩大 taxonomy、复制 task templates、从真实 repo
  反演 bug 或随机拼接 skills 都能便宜地增加 task count；当任务域窄、每个 task 的执行路径差异足够大时，
  这些旧方案仍合理。但 task title/domain 多样不保证 Agent 实际经历不同 intermediate state 与 skill transition，
  大量样本可能落在相同 trajectory support 上，继续增加数量只重复相近训练信号。
- **Changed Constraint / First Principle**：训练目标真正消费的是 observation/action sequence。论文把低层
  trajectory 提升为 `scenario σ`（决策相关状态）与 `skill κ: σ→σ'`（action subsequence），将 coverage 写成
  `p_D(σ|g) · p_D(κ|σ,g)` 的 support 问题：未出现的 scenario 不可观察，某 scenario 下未执行的 skill
  不可学习。因此应优化 conditional scenario–skill coverage，而不是只优化 task 数量。
- **Mechanism**：先从 ClawHub/公开 GitHub 收集 human-written skills，过滤为 Linux 可执行、结构化、非
  adversarial 且可客观验证的集合；用 DeepSeek Reasoner v3.2 从说明、代码与示例推断 pre/post scenarios，
  由 embedding clustering 去重，再对每个 postcondition 检索 top-1000 preconditions，并用 LLM 做双向兼容
  judgment、merge 与 triple filtering，形成 scenario-node / skill-edge multigraph。采样器以
  `(visit_count+1)^-1` 对 scenario 与 skill 逆频率加权，禁止同一路径重复节点/skills，保留长度 1～7 且
  skill-set 未见过的 paths。Planner 把 path 编译为 sub-objectives，constructor 生成 instruction、filesystem
  snapshot、container、tests 与 oracle solution；Harbor oracle execution 与 LLM rubric 双检，失败最多修三轮、
  每轮最多 20 tool calls。
- **State Ownership / Control Flow / Data Flow**：source registry 持有 skill provenance/license；graph builder
  持有 inferred scenarios、embedding/extractor revision、alignment verdict 与 merge lineage；sampler 持有 visit/
  usage counters 与 accepted path set；planner/constructor 只产生 candidate task artifacts；oracle verifier 持有
  executable solvability evidence，rubric judge 持有 instruction-test/self-containedness judgment；dataset owner
  决定 SFT/RL eligibility。流向是 `skill sources → inferred pre/post state → versioned graph → sampled path →
  task plan → container/files/tests/oracle → verify/repair/discard → teacher trajectories → immutable training manifest`。
- **Implementation Details**：graph 构建使用 Louvain coarse buckets + complete-linkage agglomerative clustering；
  threshold 在 held-out scenario samples 上人工选择。论文报告 82,073 scenarios、57,214 filtered skills 与
  185,529 LLM-verified bridges。PDF Table 6 又把 giant component 写成 118,806 nodes（85.6%），大于同表
  scenario-node 总数；它可能统计 scenario+skill 的 bipartite expansion，但正文没有定义，故该 component
  数字标记为 `Disputed / Counting Semantics Not Disclosed`，不作为知识库事实。
- **Evaluation Contract**：从 graph 抽取 3,721 paths，生成 3,560 usable tasks；harness 以 oracle 与 rubric
  检查，作者报告 92.0% 双检通过、95.7% oracle pass，721 个 task 经 repair 恢复。MiniMax M2.7 每 task
  采三条 trajectory，共 10,680 条，成功与失败都进入 SFT；Qwen3 8B/14B/32B 做 full-parameter SFT，AdamW、
  BF16、5 epochs、peak LR 2e-5、micro-batch 1/GPU、gradient clipping 1.0。评测为 Terminal-Bench 1.0/2.0、
  Terminus 2 scaffold、Harbor、128 concurrent Docker environments、三次独立 runs 与 95% CI。GPU type/count、
  global batch、sequence length、teacher sampling settings、wall-clock 与 serving SLO 均 `Not Disclosed`。
- **Baselines / Ablations / What the Evidence Proves**：在相同 harness 与 3,721 seeds 下比较 single-skill、
  随机 2～7 multi-skill 与 graph path；SkillSynth 的 Qwen3-32B SFT 在 TB1/TB2 比 random multi-skill 高
  3.0/3.8 points，比 single-skill 高 8.4/8.3 points。1,000-trajectory 抽样经同一 extractor/embedding pipeline
  显示 unique scenario-skill coverage 比两 baseline 高 31%/19%。这支持“workflow-compatible ordering 与
  state-conditioned coverage 比随机 skill bag 更有效”，不证明 task quantity 无价值，也不证明 graph metric
  是真实能力 coverage 的充分统计。
- **What It Does Not Prove / Threats to Validity**：scenario 是 sufficient statistic、trajectory→abstraction
  deterministic、skill autoregressive contiguous 是等价证明的假设，不是经验事实；LLM inference/alignment/
  rubric、diversity extractor 与训练数据来自相关模型生态，可能共享 ontology 和 blind spots。所谓“real-world
  workflows”仍由 public skills、LLM inferred states 与 synthetic containers 定义。rubric failures 中 77% 来自
  instruction-test mismatch；作者把这类样本保留用于 SFT、仅从 RL 丢弃，仍可能教入错误 specification。
  没有 public manifest/code/checkpoints、human-gold graph precision/recall、license/secret scan 结果、held-out
  skill-source split 或真实 terminal deployment。Hy3 Preview 的采用是 provenance fact，不证明 causal gain。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply**：graph path 提高可控组合性，但新增
  inferred-state hallucination、negation merge、hub bias、semantic bridge invalidity、counter drift、path-to-task
  mismatch、oracle/rubric collusion、container supply-chain、secret/exfiltration 与 verifier overfitting。逆频率采样
  追求长尾时可能过度选择不自然 transitions；线性 path 不能表达并行 DAG、loop 与 rollback。真实 repo inversion
  对 software maintenance 保留更强 artifact realism；hand-curated tasks 适合高风险或 verifier 难形式化领域；
  random/single-skill synthesis 在成本敏感和基础 skill coverage 阶段仍有效。
- **Evolution Relationship**：`Direct Evolution`：task-count scaling → task/domain diversity → scenario–skill
  conditional coverage → executable graph-guided workflows；planner/constructor/dual verification 对 Ch77 是
  `Layering / Dependency`，不是用多 Agent 替代数据 ownership。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch23；已读 Ch23/24 与
  Ch75～80。Ch23 已覆盖 synthetic task→trajectory→verifier lineage、generator/verifier shared ontology、
  immutable manifest 与训练分布，但只把 coverage 写到 task/constraint 层，尚未解释 scenario–skill pair
  support 与 topology-aware sampling。Ch77 已拥有 problem compilation、executable artifact、verification/
  repair 与 workflow state；Ch80 已拥有 skill identity、provenance、permissions 与 dataset feedback gate。
  因而真正的新增 owner 是 Ch23 的训练分布机制，其他章节只需短 handoff。
- **Integration Decision / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch23；Ch77/80 handoff。Historical Books Gate 关闭，不修改 Books。待验证 public graph/
  task/trajectory manifests、source-level license/security audit、human-gold scenario/bridge quality、component-count
  语义、held-out source/generalization、matched token/task volume、GPU/global-batch/length contract、parallel
  subgraph sampling，以及 instruction-test mismatch 样本是否会损害 SFT。

### Full Source Review — vLLM v0.20.0 — 29/30

- **Candidate / Week / Score / Source Family**：vLLM v0.20.0；W18；29/30（TN 5 / SI 5 / PV 5 /
  SR 5 / PR 5 / L 4）；`VLLM-020-REQUEST-KV-COMPILER-TOPOLOGY-CONTRACT`。
- **Source Type / Event Date / Revision / Access**：vLLM 官方 GitHub release `v0.20.0` 于
  2026-04-27 21:20 发布，commit `88d34c6`，属于 W18；`v0.20.1` 于 2026-05-04 发布，属于 W19，
  不倒填本周。已完整读取 408-line release notes，并联读 Model Runner V2 stale-slot fix PR #39833、
  LMCache `cache_salt` PR #39837、vLLM IR PR #33825、FA4 default PR #38819，以及 release 中 HMA/KV
  offload、EPLB、NIXL/Mamba、breaking changes 和 metrics sections。`TransferTopology` PR #39529 与
  heterogeneous-TP Mamba PD PR #37635 的独立页面本次无法稳定读取，因此只保留 release-level verified，
  不把未读实现细节写成事实。
- **Full-read Coverage**：已覆盖 Highlights、Model Support、Engine Core、Hardware/Performance、Large Scale
  Serving、Quantization、API/frontend、dependency 与 breaking-change contract，并检查关键 correctness、
  isolation、IR dispatch 和 attention-backend PR 的 purpose、control path、tests 与已披露 evaluation。
- **Original Problem / Why Previous Design Was Reasonable**：早期 serving engine 把 request scheduling、
  paged KV allocation 与单一 attention/backend path 组合起来已经足够解决动态 batch 和显存碎片；固定
  model/hardware、单层 HBM KV、同构 TP 与少量 kernels 时，局部 feature flags 和 backend-specific dispatch
  仍是更简单的设计。随着 speculative state、外部 KV connector、异构 TP、Mamba/attention hybrid state、
  多硬件 kernels 与 per-user prefix reuse 同时进入 runtime，隐式 slot lifetime、单一 cache identity 和分散
  kernel dispatch 开始成为 correctness 与演化瓶颈。
- **Changed Constraint / Principle**：吞吐优化不再只改 kernel；request-scoped state 必须在 scheduler、
  model runner、KV connector、compiler/backend 与 transfer topology 之间保持同一 identity、generation 和
  completion contract。任何可复用 slot、cache block、draft token 或 remote transfer metadata 都不能因“物理
  buffer 仍存在”就被视为属于新请求。
- **Mechanism**：Model Runner V2 复用 request slots 时，在 `add_request()` 重新以最后一个 computed token
  初始化 `last_sampled_tokens` 并清零 `draft_tokens`，修复 stale speculative state 跨请求泄漏；KV connector
  将 `request.cache_salt` 贯穿 tracker、metadata、lookup 与 batched retrieve，以隔离不同用户的 prefix-key
  namespace。HMA/offload path 增加 GPU events、group block hashes/IDs、统一 worker memory layout、multi-group
  lookup/load/store、request context 与 connector shutdown；PD/NIXL path 用统一 `TransferTopology` 表达原先
  分散的 TP KV 与 heterogeneous-transfer configuration。vLLM IR 则把 op semantics 与 provider implementation/
  dispatch 分离，由 `IrOp`、priority、runtime predicate 与 lowering pass 在 eager/compiled path 选择 kernel。
- **State Ownership / Control Flow / Data Flow**：engine/scheduler 持有 request identity、token progress、slot
  generation 与 admission；model runner 持有 device execution slot，但必须在 ownership 变化时重置所有
  request-derived fields；KV manager/connector 持有 block、hash、salt、group 与 transfer lifecycle；source/destination
  worker 通过 topology metadata 和 completion event 转移可见性；IR op 持有语义，platform/provider registry
  持有可执行实现与 capability predicate。数据流为 `request + tenant salt → schedule/reserve → optional external
  lookup/load → model-runner slot init → prefill/decode/spec verify → KV store/transfer → completion/release`。
- **Implementation Details**：v0.20.0 把 CUDA 13.0、PyTorch 2.11 与 Transformers >=5 设为 baseline，构成
  breaking environment contract；FA4 在 upstream NaN correctness fix 后重新成为 SM90+ MLA prefill default，
  并补 head-dim 512/paged-KV；vLLM IR 首个 op 为 `rms_norm`，provider 包括 vLLM C++/CUDA/HIP、AITER、
  XPU kernels 与 Oink，lowering 在 post-grad custom pass 尾部完成。release 同时加入 TurboQuant 2-bit KV、
  RayExecutorV2、waiting reason/request-id metrics 与多硬件 paths；这些是同版 feature facts，不自动形成统一
  architecture guarantee。
- **Evaluation Contract / What Evidence Proves**：PR #39833 报告受限 PD setup 中 stale state 可造成约
  13% GSM8K accuracy regression，证明 slot reuse 是 correctness boundary；但模型、完整 serving workload、
  并发与 SLO 未充分披露。IR PR 在 B200/Qwen3-0.6B latency sweep 与 DeepSeek-V3.1 generated code/lm_eval
  上验证 dispatch/lowering 没有明显回归，且 CI 通过；它证明 skeleton 可工作，不证明跨 op/provider 的成熟
  compiler。release 中零散 2.1% latency、KV capacity 或 kernel throughput 数字没有统一 model/hardware/length/
  concurrency/SLO contract，故不作为通用性能结论。
- **What It Does Not Prove / Threats to Validity**：官方 release 证明已合入的版本行为，不证明所有 backend、
  quantization、hybrid model 与 distributed topology 组合正确或更快；`cache_salt` 只提供 namespace partition
  primitive，不等于完整 authentication、authorization、secret lifecycle 或 cross-tenant side-channel defense。
  `TransferTopology` 的 release 摘要不能替代 unavailable PR 的完整实现审计；FA4 default 只适用于披露的
  support matrix，不能外推到任意 GPU/head layout。752 commits 也扩大了 regression 与 compatibility surface。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：统一 request/KV contract 降低隐式
  状态泄漏，却增加 metadata propagation、reset completeness、event ordering、salt/version invalidation、connector
  shutdown 与 topology migration 责任；IR/online quant 提高可扩展性，却引入 provider priority drift、predicate
  disagreement、compile-cache identity 与 numerical parity 风险。单机、单租户、固定 backend 或没有外部 KV
  transfer 的部署仍可使用更简单路径；旧 backend 在新 default 尚未覆盖的 hardware/shape 上仍可能更可靠。
- **Evolution Relationship**：`Direct Evolution`：paged KV + unified scheduling → request-slot/persistent-batch
  state → external/multi-group KV → tenant-aware identity + heterogeneous transfer topology；`Layering / Dependency`：
  IR/kernel dispatch 位于同一 serving state machine 下，但不替代 scheduler 或 KV ownership。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch46；已读 Ch41～48 与
  Ch50～52。Ch46 已拥有 request/scheduler/KV-manager/worker contract 和跨 device KV identity；Ch44 已拥有
  draft/target rollback correctness；Ch45 已拥有 semantic op→kernel/provider dispatch；Ch51 已拥有 KV handoff
  visibility。新增证据最适合精化 Ch46 的 slot generation、tenant cache namespace 与 versioned transfer identity，
  其他章节仅短 handoff。
- **Integration Decision / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Version-Grounded Runtime Evidence)` / Ch46；Ch44/45/48/51 short handoff。Historical Books Gate 关闭，
  不修改 Books。待核验 unavailable PR full diff、cache-salt threat model、multi-group/HMA failure injection、
  topology migration/rollback、跨 backend numerical parity，以及完整 workload 下的 TTFT/TPOT/goodput contract。

### Full Source Review — Hugging Face Transformers v5.7.0 — 26/30

- **Candidate / Week / Score / Source Family**：Hugging Face Transformers v5.7.0；W18；26/30
  （TN 4 / SI 5 / PV 5 / SR 5 / PR 4 / L 3）；`TRANSFORMERS-570-CONTINUOUS-BATCHING-MEMORY-STATE`。
- **Source Type / Event Date / Revision / Access**：官方 GitHub release 于 2026-04-28 18:32 发布，commit
  `6ffbb07`；已完整读取 release notes，并联读长生成修复 PR #45530、v5.7.0 Continuous Batching API/
  architecture docs 与 tag-pinned source surface。CPU request offload PR #45184 的独立页面本次不稳定，
  其行为只采用 tag-pinned docs 与 release 已公开 contract，不补写未核验实现细节。
- **Full-read Coverage**：已覆盖 Laguna/DEIMv2 additions、attention/tokenizer/generation/kernel fixes、全部
  bugfix list 与 significant contributions；机制审计聚焦 continuous batching 的 16K+ generation、KV dedup、
  memory estimation、write-only prefill、two-peak sizing、CPU offload、scheduler/admission/prefix/eviction、
  CUDA graph 与 async batching，避免把模型支持列表误写成统一系统创新。
- **Original Problem / Why Previous Design Was Reasonable**：单次 `.generate()` 或较短 batch 下，用物理 GPU
  total memory 减去静态估计、用单一 per-token activation peak 和 recompute-on-eviction 足以保持实现简单；
  short prompt/short output 时 prefix bookkeeping、swap pool 与复杂 memory polynomial 可能不值得。长生成、
  logits-sized temporaries、paged KV、continuous admission 与 CUDA context/driver overhead 叠加后，物理总量
  不再等于可安全分配量，单峰估计会 overcommit/OOM，纯 Prefill 也会为不存在的 KV reads 支付开销。
- **Changed Constraint / Principle**：Serving capacity 是多个 shape-dependent memory peaks 的最小可行边界，
  不是 `device_total × utilization`。正确 sizing 必须基于 model load 后的实际 free memory，并分别约束
  LM-head/logits 峰值与随 KV length 增长的 attention 峰值；preemption 还必须显式选择 preserve/offload 或
  release/recompute state policy。
- **Mechanism**：PR #45530 用 `torch.cuda.mem_get_info` 纳入 CUDA context/driver 与当前占用，把单一
  `peak_activation_per_token` 拆成 LM-head 与 attention 两个峰值，分别求可容纳的 `num_blocks` 和
  `max_batch_tokens` 后取更严格者；decode-only batch 不再错误消费 read-index cache budget，纯 Prefill 走
  write-only fast path，跳过 `index_select`、read-index allocation/transfer，并让 CUDA-graph key 跟 block-table
  path 对齐。v5.7.0 还允许预分配 pinned CPU KV swap pool：GPU cache 满时先 offload 被驱逐 request，空间
  恢复后 copy back；若禁用或 pool 满，则把生成历史拼回 prompt、释放 blocks 并重新 Prefill。
- **State Ownership / Control Flow / Data Flow**：ContinuousBatchingManager 持有 request queue、background
  loop 与 result delivery；scheduler 用 token/cache budgets 决定 pending→prefill→decode；paged cache manager
  持有 per-layer-group block IDs、hash/refcount 与 eviction；offload pool 持有被驱逐 request 的 pinned-host KV，
  request identity/progress 必须随 swap/requeue 保留。流向是 `submit → admission → chunked prefill/write KV →
  iterative decode → cache pressure → CPU offload or soft reset/recompute → resume → finish/release`。
- **Implementation / Evaluation Contract**：tag docs 固定 block size 默认 256、free-memory-based automatic
  sizing、FIFO/PrefillFirst、20% admission safety margin、prefix hash/refcount、CUDA-graph shape padding/LRU、
  async double buffering（以约双倍 VRAM 换 CPU/GPU overlap）与 `cpu_offload_space` safety cap。PR #45530
  对多组 sample counts、attention backends、async/prefix/return-sequence 配置报告吞吐变化，但未披露 GPU、
  model、prompt/output distribution、precision 与 latency SLO，故只证明没有明显单一 workload regression，
  不保留 headline percentages。测试覆盖 continuous batching、CLI 与 paged attention slow suites。
- **What Evidence Proves / Does Not Prove**：证据支持“真实 free memory + multi-peak model 可修复长生成
  overcommit，并允许更多 KV capacity”以及 offload/recompute 是两种明确 state dispositions；不证明
  Transformers 的通用 generation path 等同专用 production serving engine，也不证明 0.9 memory fraction、
  20% margin、FIFO 或 CPU offload 在任意 model/hardware/SLO 上最优。Laguna/DEIMv2 与 attention bugfixes
  只证明版本支持/修复，不证明原论文 benchmark 或所有 cache semantics 已独立复现。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies**：更准确 sizing 增加 profile/model
  assumptions，logits processors、compile graphs 或 backend 临时 buffers 改变时必须重算；CPU offload 避免
  recompute，却消耗 pinned RAM、PCIe bandwidth、copy scheduling 与 restore latency，并新增 host OOM、partial
  transfer、stale block table 和 cancellation cleanup；soft reset 更简单但重新计算全部 history。短会话、低并发、
  无 cache pressure 或 PCIe 受限时，release-and-recompute 仍可能更好。
- **Evolution Relationship**：`Direct Evolution`：static `.generate()` → continuous request lifecycle → paged
  KV/admission → actual-free-memory + multi-peak sizing → preserve/offload/recompute policy；与 vLLM v0.20.0 是
  `Principle Reuse`，不是产品替代关系。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch42；已读 Ch41～47、
  Ch50～52。Ch42 已拥有 iteration token/KV budget、preemption 与 state disposition，Ch43 拥有 block mapping，
  Ch46 拥有完整 engine contract，Ch50 拥有 memory budget。新证据适合精化 Ch42 的 multi-peak admission
  sizing 与 swap-vs-recompute decision；不在 Ch46 把 Transformers 写成 vLLM 的替代。
- **Integration Decision / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Version-Grounded Continuous Batching)` / Ch42；Ch43/46/50 short handoff。Historical Books Gate 关闭，
  不修改 Books。待核验 CPU offload PR full diff、offload/cancel failure injection、pinned-memory fragmentation、
  tail latency，以及 model/hardware/length/concurrency/SLO 完整披露下的 matched benchmark。

### Official Source-Family Partition Queue — IBM Granite 4.1

IBM Research 的 2026-04-29 official release 在第二轮 fixed-source scan 中恢复。它同时发布 Language、
Vision、Speech、Guardian 与 Embedding 五类模型；其中 Speech 的 AR、Plus 与 NAR 又拥有不同 state machine、
output schema 与 latency contract，因此最终形成七个 mechanism-level source families，不能压成一个
“Granite 4.1 bundle”或一个 Speech 评分行。announcement 已全文读取，当前官方 Hugging Face organization/
model-card surface 已定位。七个 mechanism-level families 已全部完成独立评分与 Full Source Review；这只
闭合 Granite partition，不代表 W18 的其他 fixed-source 与 academic cross-index 已闭合：

| Subfamily | Current Primary Evidence Located | Pending Before Score |
|---|---|---|
| Granite 4.1 Language 3B/8B/30B | IBM release；technical article；3B/8B/30B cards；8B config/commit history | **Full Source Review Complete — 24/30；provisional Refine / Ch24；512K training exposure 与 131K released contract 已拆分** |
| Granite Vision 4.1 4B | IBM release；current card/config/history；ChartNet v1/dataset | **Full Source Review Complete — 24/30；provisional Refine / Ch17；current dataset revision 未倒写为 launch training manifest** |
| Granite Speech 4.1 2B AR | IBM release；current official 2B card；predecessor architecture paper；self-speculative paper | **Full Source Review Complete — 26/30；provisional Refine / Ch5；4.1 artifact 与 earlier source-family experiments 已拆分** |
| Granite Speech 4.1 2B Plus | IBM release；current official Plus card；SAA/In-Sync related papers | **Full Source Review Complete — 26/30；provisional Refine / Ch38；2B artifact 与两篇 8B paper/evaluation contracts 已拆分** |
| Granite Speech 4.1 2B NAR | IBM release；current official NAR card；NLE arXiv:2603.08397 v1 | **Full Source Review Complete — 27/30；provisional Refine / Ch40；paper runs 与 current artifact contract 已拆分** |
| Granite Guardian 4.1 8B | IBM release；current IBM docs/card；2024 Guardian paper | **Full Source Review Complete — 26/30；provisional Refine / Ch68；4.1 claims 与 2024 predecessor mechanism 已拆分** |
| Granite Embedding Multilingual R2 | IBM release；current official 97M card；arXiv:2605.13521 later-public paper | **Full Source Review Complete — 27/30；provisional Refine / Ch72；April artifact 与 W20 paper/dependency evidence 已拆分** |

announcement 中的 “competitive”“state of the art”“production-ready” 与 leaderboard statements 均保持厂商
主张，不升级为独立实验结论。Embedding 的 5 月论文只作为 later-public related evidence，未被倒写成
4 月 29 日已经公开的技术报告；Granite partition 已闭合，Historical Books Gate 仍关闭。

### Full Source Review — Diffusion Templates: A Unified Plugin Framework for Controllable Diffusion — 28/30

- **Candidate / Week / Score / Source Family / Type**：`DIFFUSION-TEMPLATE-CAPABILITY-CACHE-INTERFACE`；
  W18；`TN 4 / SI 5 / PV 5 / SR 4 / PR 5 / L 5 = 28/30`；arXiv experimental research / framework
  design。arXiv:2604.24351 v1 于 2026-04-27 11:44 UTC first-public，当前只有 v1，事件归 W18。
  已完整阅读 arXiv HTML v1 的 metadata、Abstract、Introduction、Related Work、Framework Design、
  Template cache/model/pipeline/training、全部 11 类 model-zoo cases、Conclusion/Future Work 与文中披露的
  evaluation/limitation boundary。论文链接的 project page 本次无法独立访问，故 artifact/code status 为
  `Primary Paper Complete; Project Artifact Unverified`，不能把论文中的 implementation availability 当作
  已复现事实。
- **Original Problem / Why the Previous Design Was Reasonable**：ControlNet、task-specific adapters、LoRA
  与专用 editing/SR pipelines 各自围绕一种条件或任务设计模型输入、side network、训练脚本和 runtime
  glue。单能力时，专用实现拥有最清楚的 tensor contract、最少的 merge ambiguity 与最容易验证的质量边界，
  因而旧方案完全合理。约束变化来自能力数量和组合需求：当同一 diffusion foundation model 需要同时接收
  edge/depth、亮度、颜色、参考图、局部 mask、aesthetic preference 等异构条件时，复制整条 pipeline 会让
  model loading、训练入口、能力组合和 artifact compatibility 呈乘法增长。
- **Changed Constraint / Principle / Mechanism**：论文把“能力”从专用 pipeline 中拆成三层契约：

  ```text
  arbitrary task input
  -> template model
  -> template cache (restricted to base-pipeline argument names)
  -> carrier-specific merge
  -> unchanged base diffusion pipeline
  ```

  Template model 把任意任务输入转换为 template cache；cache key 只能映射到 base pipeline 已接受的参数，
  以接口约束替代对 base graph 的任意侵入。论文实现的 carrier 至少包括 KV cache 与 LoRA：多个 KV carriers
  沿 sequence dimension 连接，多个 LoRA carriers 沿 rank dimension 连接，异构 carrier 可同时启用。
  Template pipeline 负责加载 template models、执行 preprocessing/forward、按 carrier type 合并，再把结果
  注入 base runtime。这里的长期原则不是“KV cache 就是插件”，而是把 capability module 与 base execution
  之间收敛为可验证的中间表示和 merge algebra。
- **State Ownership / Control Flow / Data Flow**：base diffusion pipeline 拥有 denoising state 与最终生成；
  template model 拥有 task input 到 capability state 的转换；template pipeline 拥有 module loading、执行顺序、
  cache merge 与 injection。`process_inputs` 是无梯度预处理路径，`forward` 产生训练所需梯度；训练冻结 base
  model，只优化 side/template branches，并继续使用 base pretraining objective。Template cache 是两者之间的
  typed-but-not-yet-versioned state boundary。论文还把 template models 放在 denoising loop 外执行，并提出 lazy
  loading / round-robin execution 以控制峰值显存；但没有公开 scheduler、eviction、concurrency 或 failure
  recovery state machine。
- **Implementation Details / Alternatives**：结构控制、亮度/颜色调整、editing、super-resolution、sharpness、
  aesthetic alignment、content reference、local inpainting、age control 与 template fusion 被放进同一框架。
  Local inpainting 特别暴露了 learned soft control 的边界：只靠 template model 不能保证未遮罩区域不变，
  pipeline 必须在每个 denoising step 用原图 VAE encoding 替换未遮罩区域，形成“learned proposal + hard
  invariant”的 layering。旧的 task-specific pipeline 在需要严格 invariant、专用 latency 或单一稳定能力时仍
  更合理；统一 template interface 在多能力组合、共享 base 与快速扩展时更有价值。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：论文主要提供 model-zoo qualitative
  examples；默认示例披露 FLUX.2-klein-base-4B、seed 0、CFG 4、50 denoising steps。只对 image editing 给出
  约 `1.8x` speedup，但没有把该数字绑定 GPU、dtype、resolution、batch/concurrency、warm/cold load、memory
  peak 或 latency SLO，因此本记录不把它当作可迁移性能结论。Super-resolution 仍慢于 dedicated pipeline；
  aesthetic alignment 只用 90 对 images，作者明确称为 preliminary；content reference 的 semantic control
  不够显式。未披露统一 quantitative baseline、composition ablation、merge-order sensitivity、per-template
  memory/latency distribution、compatibility matrix 或 failure-injection tests，均记为 `Not Disclosed`。
- **What the Evidence Proves / What It Does Not Prove**：证据支持一个 base-preserving capability interface
  能用 KV/LoRA carriers 表达多类 controllable diffusion tasks，并展示 heterogeneous composition 与 hard
  pipeline constraints 可以共存。它没有证明任意 control modules 可无冲突组合、cache concat/LoRA concat
  在所有架构上语义等价、质量优于 task-specific baselines、或 lazy loading 在 production concurrency 下满足
  SLO。作者在 Future Work 中仍把 controllability、compositionality、transferability、efficiency、compatibility
  的定量评测列为后续工作，因此状态固定为 `Experimental`。
- **Trade-offs / New Failure Modes / Evolution Relationship**：这是 `Layering / Dependency`，不是对
  ControlNet、LoRA 或专用 pipelines 的替代。收益是 base reuse、能力模块化和组合入口统一；代价是新增
  cache identity、carrier schema、merge order、module/base version matching、memory residency、conflict
  arbitration 与 rollback state。错误 cache key、错误 base revision、不同 templates 修改同一表示方向、未知
  carrier 或 merge 顺序变化都可能产生 silent semantic drift。下一阶段压力是把论文中的 Python-level
  interface 升级为 registry/runtime contract：immutable digests、compatibility declaration、composition
  evaluation、resource envelope、fallback 与 decision trace。
- **ROADMAP Node / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 暂定 Ch55，已完整阅读
  Ch54～56；Ch55 已覆盖 base/adapter/quantization/runtime compatibility identity，Ch26 已覆盖 LoRA merge、
  dynamic adapter 和组合冲突，Ch45 已覆盖 generic module replacement 与 specialized structural fusion。
  现有 Books 已有“组合 artifact 必须绑定 base identity”这一原则，但还没有把 KV/LoRA 等 capability carriers
  提升为统一 plugin intermediate state，也没有明确 merge algebra、cache schema 与 hard invariant 的关系。
- **Integration Decision / Changed Files / Open Questions**：`Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，本轮只更新 W18、年度索引、Learning State 与 2026-08-10 Daily，不修改
  Books。未来若 Gate 通过，Ch55 只沉淀“capability carrier 也是 deployment artifact contract”的长期机制，
  Ch26/45 各留短 handoff，不复制 model-zoo。待验证 project artifact、carrier serialization/schema、base/version
  compatibility matrix、merge-order semantics、并发资源曲线、composition ablations 与 quantitative quality/SLO。

### Full Source Review — Refinement via Regeneration — 27/30

- **Candidate / Week / Score / Source Family / Type**：`UMM-REFINEMENT-CONDITIONING-GEOMETRY`；W18；
  `TN 5 / SI 4 / PV 4 / SR 4 / PR 5 / L 5 = 27/30`；primary research paper + official code/model
  artifacts。arXiv:2604.25636 v1 于 2026-04-28 13:36 UTC first-public，当前只有 v1，事件归 W18。
  已完整阅读 arXiv HTML v1 的 metadata、Abstract、Introduction、Related Work、Method、data construction、
  training/inference、全部 quantitative/qualitative experiments、ablations、Conclusion 和相关 appendices；并
  联读官方 GitHub 当前仓库、完整 `inferencer.py` 与 Hugging Face current model card。代码与 model card 没有
  event-time frozen tag/commit，故只作 current artifact verification，不能倒写成 launch-day immutable evidence。
- **Original Problem / Why the Previous Design Was Reasonable**：统一多模态模型的 Refine-via-Edit（RvE）
  先根据目标 prompt 与当前图像生成 editing instruction，再用该 instruction、ViT semantic tokens 与输入图像
  的 VAE low-level tokens 执行修改。这个设计在局部编辑、身份保持、不可变区域和可审计修改意图优先时完全
  合理；但当问题是全局语义错位时，粗粒度 instruction 可能漏掉多个关联约束，low-level image conditioning
  还会把错误布局、数量和关系作为强先验保留下来。
- **Changed Constraint / Principle / Mechanism**：RvR 把任务契约从“尽量保留输入并修补局部错误”改成
  “保留语义证据，但允许重构整幅图像以满足最终目标”。它移除中间 editing instruction 与输入图像 VAE
  conditioning，只保留目标 prompt 和输入图像的 semantic ViT tokens，再用 flow matching 直接重新生成：

  ```text
  RvE: target + semantic image + low-level image -> edit instruction -> constrained edit
  RvR: target + semantic image -----------------> unconstrained regeneration
  ```

  长期原则是：training pair、conditioning state 与 objective 的几何必须匹配任务 invariant。若最终 contract
  只要求 semantic alignment，训练阶段强加 pixel preservation 会缩小有效 modification space；若 contract
  包含 identity、locality 或 immutable region，移除该约束反而会破坏正确性。
- **State Ownership / Control Flow / Data Flow**：数据管线用 Gemini 生成含 1～5 个 semantic dimensions 的
  prompt，由 BAGEL 与 GPT-4o 独立生成候选，再由 Gemini-2.5-Pro 标注 alignment，配成“misaligned source / aligned
  target”。训练 runtime 以 BAGEL 为 base，semantic ViT path 拥有源图理解，flow-matching path 拥有新图生成；
  官方 inferencer 的 generation context 明确拥有 KV length、RoPE 和 `NaiveCache`，并通过 `wo_vae` 使 refinement
  可保留 ViT 语义输入而省略源图 VAE。多轮 refinement 会把上一轮输出重新变成下一轮输入，但 paper/code 没有
  定义独立 loop controller、stop rule、rollback 或 degraded-output owner。
- **Implementation Details**：作者在 16 张 NVIDIA H800 上训练 15K steps，AdamW learning rate `1e-4`、EMA
  `0.9999`、CE:MSE 为 `0.25:1`；混合 100K refinement、60K BLIP-3o text-to-image 与 1K BAGEL understanding
  samples，ratio `2:1:1`。推理使用 50 sampling steps，text CFG 4、image CFG 2。attention mask 对 text tokens
  使用 causal attention，对 ViT/noisy VAE tokens 使用 full attention。官方 repo 提供 training/evaluation scripts
  与 toy data，但没有 frozen experiment manifest、release tag 或完整数据 provenance。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：作者在 Geneval、DPGBench、
  UniGenBench++ 上比较 BAGEL、UiG、Uni-CoT、IRG；复现 BAGEL 为 `0.78 / 84.02 / 60.51`，RvR 为
  `0.91 / 87.21 / 77.41`。DPGBench ablation 从 BAGEL `84.02`、same-scale SFT `84.62`、加入 editing data
  `85.70`、恢复 input VAE `86.41` 到完整 RvR `87.21`，支持“训练数据与移除 VAE constraint 均有贡献”。这些
  数字只属于作者披露的 BAGEL/H800/training mix/50-step CFG contract；paper 未披露 multi-seed variance、
  confidence interval、matched inference cost、latency/memory、batch/concurrency、human preference、identity
  preservation、safety 或 production SLO。多轮与不同初始 semantic alignment 仅有 qualitative evidence。
- **What the Evidence Proves / What It Does Not Prove**：证据支持：在这组作者实验中，以语义 token 保留
  源图信息、同时移除低层 VAE preservation，可以扩大修改空间并改善三项 alignment benchmark；ablation 也
  表明收益并非只来自增加数据。它不证明 regeneration 普遍优于 editing、不证明适用于身份/风格/几何保持，
  也不证明多轮 refinement 单调收敛。数据生成、alignment labeling 与 UniGenBench++ judge 均依赖 Gemini
  family，存在 correlated generator/verifier/evaluator bias 与 measurement-channel optimization 风险；没有
  independent judge、held-out generator distribution 或人工审计时，不能把分数外推为通用视觉质量。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies / Evolution**：这是 UMM refinement
  的 `Direct Evolution`，不是 RvR 对 RvE 的单向替代。RvR 获得全局重排、关系修复和较大 modification
  space，代价是 identity drift、局部细节丢失、不可变区域破坏、额外重生成成本与多轮 error accumulation。
  RvE 在局部 edit、品牌/人物 identity、mask invariant、低变化成本与明确 audit trail 场景仍然成立；工程系统
  更可能需要根据 invariant contract 在 RvE/RvR 间路由，并为 regenerate path 增加 verifier、stop、rollback
  与 provenance。下一阶段压力是 independent evaluator、constraint-aware router、immutable-region enforcement
  和多轮 termination/failure semantics。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 暂定 Ch23；已完整阅读
  Ch22～24，并核对 Ch25 与 Ch62 的相关边界。Ch23 已覆盖 synthetic generator/judge shared bias、constraint-
  derived verifier 与 multimodal lineage，但尚未明确“source-target pair geometry 和 conditioning prior 必须匹配
  task invariant”；Ch25 拥有训练阶段与 objective handoff，Ch62 拥有 independent evaluation 与 operating-point
  证据边界。该候选不需要新增章节，也不应复制成图像模型案例清单。
- **Integration Decision / Changed Files / Rejection Boundary / Open Questions**：`Refine — Existing Argument
  (Experimental)`；Historical Books Gate 关闭，本轮只更新 W18、年度索引、Learning State 与 2026-08-10
  Daily，不修改 Books。Gate 通过后只考虑在 Ch23 精炼“约束匹配的数据几何”，Ch25/62 各留短 handoff。
  待验证独立 evaluator、样本级 provenance 与 label operating point、multi-seed variance、matched-compute
  RvE comparison、identity/locality/safety human evaluation、multi-round stop/rollback，以及 paper run 对应的
  immutable code/model/data revision。

### Full Source Review — Mutual Forcing — 28/30

- **Candidate / Week / Score / Source Family / Type**：`WEIGHT-SHARED-DUAL-BUDGET-ON-POLICY-DISTILLATION`；
  W18；`TN 5 / SI 5 / PV 4 / SR 4 / PR 5 / L 5 = 28/30`；primary research paper + official project/demo
  artifacts。arXiv:2604.25819 v1 于 2026-04-28 16:28 UTC first-public，当前只有 v1，事件归 W18。已完整
  阅读 arXiv HTML v1 的 metadata、Abstract、Introduction、Related Work、全部公式/Method、Implementation、
  quantitative/qualitative experiments、ablations、human/long-video/speed evaluations、Conclusion 与 Appendices
  A～D，并联读 official project page 与 current GitHub。仓库当前只有 README/demo、3 commits，inference/
  training code、checkpoints、preprocessing、evaluation 与 reproducibility 均仍列为 TODO，故 artifact 状态为
  `Paper Complete; Demo Surface Verified; Reproducible Implementation Unavailable`。
- **Original Problem / Why Previous Designs Were Reasonable**：teacher forcing / diffusion forcing 用真实历史
  训练 next chunk，supervision 稳定、可并行，也不会在训练早期把劣质模型输出反复喂回；但 streaming inference
  只能读取模型自己生成的 history，形成 exposure bias 与长程 drift。Self-Forcing 以生成历史缩小该 gap，
  再用独立 bidirectional teacher 做 few-step distillation；固定 teacher 提供稳定 target，在 student 尚不可靠时
  是合理隔离层，却增加模型副本、memory/compute、teacher ceiling，并把 supervision horizon 绑到固定 clip。
- **Changed Constraint / Principle / Mechanism**：当目标变成 native causal streaming、few-step latency 与
  长 horizon 共存时，Mutual Forcing 让同一组 14B weights 支持两种 diffusion-time contract：Multi mode 预测
  小步 instantaneous velocity，Few mode 直接预测区间平均 velocity / large displacement。Few mode 先 rollout
  自己的历史供 Multi mode 在 on-policy-like context 上做 paired-data flow matching；Multi mode 再以 stop-gradient
  target 蒸馏 Few mode：

  ```text
  Few rollout -> model-generated streaming history -> Multi learns from real next target
       ^                                             |
       |-- hybrid SC + DMD distillation target ------|
  ```

  长期原则不是“共享权重必然优于 teacher”，而是把 quality mode、latency mode 和 inference-state distribution
  放进同一版本化训练闭环，减少静态 teacher 与实际 student state 的失配。
- **State Ownership / Control Flow / Data Flow**：audio/video branches 分别拥有 modality-specific VAE、
  self/cross-attention 与 FFN，融合 self-attention 负责跨模态交互；timestamp-based 3D RoPE 把 audio/video/text
  放到统一时间坐标。训练分三段：unimodal pretraining、paired audio-video joint teacher-forcing、20K Mutual
  Forcing fine-tune。streaming context buffer `K` 保存先前生成 chunks；Few mode 写入 history，Multi mode读取该
  history 与真实 current target；两种 mode 共享 `theta`。但 DMD 分支仍维护 online fake model `mu_phi` 来估计
  Few distribution，因而“无外部 bidirectional teacher”不等于“没有额外训练模型状态”。paper 未披露 fake-model
  checkpoint/recovery、context eviction、mode balance 或 asynchronous update semantics。
- **Implementation Details**：audio/video 两支各 7B，共 14B；使用 Wan2.2 VAE 与 Stable Audio 2.0 VAE。
  数据来自 Emilia、Panda70M，以及 Seamless、SpeakerVid-5M、InternVid paired audio-video；先以 batch 256 分支
  预训到 loss stable，再 batch 128 joint training 100K iterations，之后 Mutual Forcing 20K steps。AdamW
  `lr=5e-5`、betas `0.9/0.95`、weight decay `0.02`、gradient clip `0.5`；EMA pretraining `0.999`、Mutual
  Forcing `0.99`；training Few supervision CFG 5，hybrid loss 的 DMD/ShortCut 权重为 `1/3 : 2/3`。控制面含
  first frame、global caption 与 timestamped ASR；caption 来自 Gemini-2.5-Pro，ASR 来自 Whisper。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：作者与 Fantasy-Talking、
  Omni-Avatar、Wan-S2V、Universe-1、OVI 比较 LSE-C、WER、CLAP FD/KL、AudioBox quality、VBench motion/
  aesthetic/identity，并将 CFG 的一次 step 计作 2 NFEs。Mutual Forcing 的 4/8 NFE 结果分别为 LSE-C
  `5.26/6.35`、WER `0.23/0.11`，其他指标呈 mixed frontier；不能简化成每项都优于 100-NFE baseline。
  4-step ablation 中 SC、DMD、SC+DMD 的 audio metrics 支持 hybrid objective 的互补性；25 秒 windowed test
  显示作者实现的三种 causal baselines 后段退化更多。human evaluation 有 106 份 valid questionnaires，
  但未披露独立参与者数、sample count、randomization 细节与 confidence interval。speed table 给出单 GPU
  在 `192x336 / 480x768 / 704x1280` 下 `30 / 12 / 3.5 FPS`，却未披露 GPU 型号、dtype、batch、memory、
  warmup、streaming latency 或 matched resolution/hardware；Universe/OVI 又分别用不同分辨率和 4/8 GPUs，
  因此只保留作者 workload fact，不形成跨系统 speedup 结论。training hardware、seeds/variance 与 total cost
  为 `Not Disclosed`。
- **What Evidence Proves / What It Does Not Prove**：证据支持在作者 14B audio-video model、数据与 metric
  contract 下，共享 Multi/Few weights、生成历史与 hybrid self-distillation 可以同时减少 NFE 并改善 25 秒内
  degradation；attention similarity `>97%` 是两种 mode 表征接近的 observation，不是因果证明。它没有证明
  同权重闭环不会自我强化错误、没有证明超出 25 秒/多说话人/第一视角仍稳定，也没有证明训练 memory/cost
  低于所有 teacher-student alternatives。project demo 与 106 questionnaires 不能替代代码、frozen model、
  dataset manifest、multi-seed reproduction 或 production SLO。
- **Trade-offs / New Failure Modes / Where Previous Designs Still Apply / Evolution**：这是
  `Direct Evolution`：`teacher forcing -> self/on-policy forcing + external teacher -> weight-shared dual-budget
  self-distillation`。收益是 teacher target 随 shared model 更新、训练/推理 context 更一致、一个 artifact
  服务多个 NFE budget；代价是 Multi/Few objective interference、moving-target instability、fake-model state、
  Few-history corruption、mode collapse、checkpoint/recovery 耦合与更难的 regression attribution。固定 external
  teacher 在需要稳定 oracle、明确 rollback、不同 student architecture 或质量隔离时仍合理；teacher forcing
  在短 horizon、早期训练和真实历史可获得时仍是稳定基线。下一阶段压力是把 mode id、interval schedule、
  fake-model revision、context policy、loss ratio 与 recovery point 纳入 checkpoint contract。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 暂定 Ch25；已完整阅读
  Ch24～26，并核对 Ch38/40/44 的 execution boundary。Ch25 已覆盖 student on-policy prefix、teacher snapshot/
  refresh 与 distillation distribution gap，但尚未明确同一权重下 quality/latency modes 如何互相改变 target 与
  inference-state distribution；Ch38/40 只接收“generation budget 与 streaming state 已由训练 contract 改变”
  的短 handoff，Ch44 的 speculative verification 不应与 approximate diffusion step reduction 混为一谈。
- **Integration Decision / Changed Files / Open Questions**：`Refine — Existing Argument (Experimental)`；
  Historical Books Gate 关闭，本轮只更新 W18、年度索引、Learning State 与 2026-08-10 Daily，不修改 Books。
  Gate 通过后仅在 Ch25 精炼“多预算自蒸馏的 shared-state contract”，不复制 audio-video benchmark。待验证
  公开 code/checkpoint/data manifest、GPU/dtype/cost、fake-model checkpoint/recovery、mode-gradient conflict、
  context buffer/eviction、multi-seed variance、超过 25 秒与多说话人/第一视角结果，以及独立复现。

### Full Source Review — Co-Director — 27/30

- **Candidate / Week / Score / Source Family / Type**：`FACTORED-GLOBAL-SEARCH-LOCAL-REFINEMENT-WORKFLOW`；
  W18；`TN 4 / SI 5 / PV 4 / SR 4 / PR 5 / L 5 = 27/30`；primary research paper + official code/dataset
  surfaces。arXiv:2604.24842 v1 于 2026-04-27 18:00 UTC first-public，当前只有 v1，事件归 W18。已完整
  阅读 HTML v1 的 metadata、Introduction、Related Work、architecture/MAB/local refinement、benchmark、全部
  experiments/ablations/human validation、Conclusion 和 Appendices A～L（含完整 evaluator prompts），并联读
  official project、current GoogleCloudPlatform implementation 与 GenAD-Bench hub。代码当前可读，但 paper-run
  frozen commit 未标注；project 仍写 `Data (Coming Soon)`，dataset hub 未呈现可下载 immutable manifest，故
  dataset availability 不能按论文“open-source”主张升级为已独立核验。
- **Original Problem / Why Previous Design Was Reasonable**：线性 agent pipeline 以 storyline、keyframe、
  video、audio、post-production 逐段生成，接口简单、单次成本低，也容易定位每个 stage 的 owner；但上游 prompt
  错误会向下级传播，各 sub-agent 独立解释“创意方向”会产生 semantic drift，final failure 又难以回拨到具体
  prompt。局部 self-refinement 能修单个 artifact，却不负责跨阶段的全局 exploration/credit assignment。
- **Changed Constraint / Mechanism / State Ownership**：Co-Director 让 orchestrator 拥有 structured user/
  reference state 与全局 creative configuration；Pre-Production 产生 brief/storyline/assets/storyboard，Production
  产生 keyframes/clips/audio，Post-Production 负责 stitch。局部 loop 对 storyline 和 keyframe 做 threshold/
  retry-bounded feedback descent，保留 accepted keyframes；全局 loop 把一次完整 pipeline run 当作 bandit pull，
  在 creative strategy、narrative mode、aesthetic archetype 三轴上用 UCB1、LLM warm start 与 MLLM factored
  rewards 选择下一配置，T=4 后按 aggregate score 选择 final video。它的长期价值是把 global policy state
  与 local repair state 分层，而不是把更多 persona 当成能力来源。
- **Control Flow / Data Flow / Implementation**：每个 12 秒 output 含 4 shots；MAB 最多 4 个 end-to-end runs，
  local refinement 最多 3 retries。实现组合 Gemini 3 Pro、Nano Banana Pro、Veo 3.1、Gemini 2.5 Pro TTS 与
  Lyria 2，并把 iteration history、factored rewards、feedback、stitching blueprint 暴露到 read-only canvases。
  current repository 包含 `instructions/mab/tools/utils/agent.py/config.yaml` 等 runtime surface，但没有把 paper
  experiment 的 exact commit、model revisions、random seeds、API sampling/cost/latency 与 failed-run retention
  固化成 immutable run manifest。
- **Evaluation Contract / Baselines / Ablations / Human Validation**：GenAD-Bench 有 400 scenarios / 200
  fictional products / 50 brands，200 hillclimbing 与 200 validation（160 in-domain、40 out-of-domain）；Gemini
  3 Pro 生成结构文本并担任 MLLM judge，Nano Banana Pro 生成 assets，约 15% assets 经人工重生成。主实验
  以 VAF/DA/MA/VQ 比较 commercial、monolithic、AniMaker/MovieAgent、base pipeline、T=4 random search 与
  Co-Director；后两种同为 4-run budget，平均分为 `75.7` 与 `81.4`。ablation 支持 local storyline/keyframe
  refinement、warm start 与 factored reward 在作者 judge 下分别有增益。50-scenario human subset 每 video 5
  independent raters；MLLM-human Spearman 仅 `0.317～0.522`，VQ 最低。论文未披露多 seed、API cost/latency、
  T=4 置信区间、跨 judge family reproduction、完整 failure distribution 或 statistical significance。
- **What Evidence Proves / Does Not Prove**：证据支持在该 Google model stack、fictional-ad distribution、
  T=4 budget 与 Gemini judge contract 下，中央 creative axes + local selective regeneration 比 random search/
  single-pass variants 得分更高。它不证明 UCB 在四次 pull 中收敛、更不证明找到 global optimum；三个 axes 的
  independent update 假设可能被强 interaction 破坏。更关键的是 final-video evaluator prompt 明确要求 strategic
  efficacy 与 execution quality “directionally consistent”，所以 factored rewards 是同一 judge 生成的 attribution，
  不是独立 causal observation；“analytically bypasses credit assignment”只能保留为作者主张。Gemini 同时参与
  generation、warm start 与 judging，也带来 correlated preference；fictional assets 降低 memorization 不能证明
  benchmark 测到纯 reasoning。
- **Trade-offs / Failure Modes / Evolution**：这是 `Layering / Dependency`：`linear workflow -> local bounded
  refinement -> global factored black-box search`。收益是 global intent propagation、局部失败不必全量重跑、
  expensive search 有显式 budget；代价是 4 倍 end-to-end generation、judge-induced reward hacking、arm interaction、
  warm-start lock-in、accepted-artifact stale dependency、API nondeterminism 与更复杂 provenance/rollback。线性
  pipeline 在 objective 稳定、成本高或 deterministic constraints 足够时仍合理；random/best-of-N 在 action space
  不可可靠 factor、避免 attribution bias 时仍是有效基线。生产系统还需把 hard constraints 与 subjective reward
  分开，并让 workflow—not agents/judge—拥有 retry、budget、artifact identity 与 final approval。
- **ROADMAP / Chapters Read / Existing Coverage / Decision**：主 owner 为 Ch77；已完整阅读 Ch76～78，并核对
  Ch62。Ch76 已覆盖 evidence-backed bounded refinement、best attempt、stop/escalate；Ch77 已覆盖 evaluator-driven
  search、typed task contract、多指标/lineage/held-out gate；Ch78 已覆盖 supervisor/worker、shared state 与
  coordination tax；Ch62 已覆盖 judge calibration、同源偏差与 rubric/criterion/ranking 分层。Co-Director 是这些
  原则在 video workflow 上的完整案例，但没有补出尚未被正文拥有的新长期机制，故 disposition 为
  `No Change — Already Covered`。Historical Books Gate 关闭；本轮只更新 W18、年度索引、Learning State 与
  2026-08-10 Daily，不修改 Books。待验证 immutable dataset/run manifest、independent judge、multi-seed/
  cost-matched T sweep、axis-interaction ablation、reward-hacking/failure injection 与真实品牌/长期视频泛化。

### Full Source Review — MAIC-UI — 28/30

- **Candidate / Week / Score / Source Family / Type**：`HUMAN-SCOPED-GENERATIVE-ARTIFACT-EDITING`；
  W18；`TN 4 / SI 5 / PV 5 / SR 4 / PR 5 / L 5 = 28/30`；primary research paper + official
  implementation。arXiv:2604.25806 v1 于 2026-04-28 16:15 UTC first-public，当前仅有 v1，事件归 W18。
  已完整阅读 HTML v1 的 metadata、Introduction、Related Work、六人 formative study、system design、
  implementation、lab study、classroom deployment、Discussion、Limitations、Conclusion 与 Appendices A～E，
  并联读 current official repository、README、backend generation/validator/editor services 与 frontend
  WebEditor surface。论文没有标注 event-time frozen commit；Appendix 写 React 18，而 current repository
  README/package layout 为 Next.js，因此 current code 只能核验机制 surface，不能反向证明 paper-run artifact
  与今天仓库完全一致。
- **Original Problem / Why Previous Design Was Reasonable**：直接 Text-to-HTML 让非程序员只需描述目标，
  一次生成完整页面，接口简单，也避免维护中间 schema；传统手工 HTML/CSS/JavaScript 则提供最强精度与
  可调试性。但教育课件同时要求 source alignment、可操作 simulation 与局部可控编辑。全量 regeneration
  会重写未要求改变的区域、丢失已接受状态并拉长反馈周期；纯自然语言修改又缺少“用户指的是哪一个 DOM
  element”的稳定 identity。
- **Changed Constraint / Mechanism / State Ownership**：MAIC-UI 先把 PDF/PPT/文本提取成 main topics、key
  concepts、learning objectives、prerequisites、procedural concepts、subject 与 grade 的 structured state；
  Stage 1 生成内容对齐的单页交互 simulation 并做功能检查，Stage 2 才做 layout/theme/animation polish。
  编辑时由用户点击选定 rendered element，frontend 保存 selector、HTML fragment、bounding box 与 citation
  index；模型接收 user instruction、引用与 full HTML，优先产生 Unified Diff。authoring workflow 拥有
  source/structured representation/current HTML/version，用户拥有修改意图与选择范围，模型只提出 patch，
  validator/apply path 决定是否接受，失败时才扩大 context 或回退全量生成。
- **Control Flow / Data Flow / Implementation**：PDF page images 经 VLM 进入 JSON-like pedagogical state，
  再进入 content generation、validation/refinement 和 visual polish。当前 artifact 使用 FastAPI backend、
  Next.js frontend、sandboxed preview 与双向消息；`editor_processor.py` 将 citation 定位到 source line，构造
  full-content prompt，解析/apply unified diff，失败时接受完整 HTML 或保留原 artifact。repository 也包含
  generation、content/HTML/simulation validators 与 version UI，但论文声明的三次 edit failure 后 full
  regeneration、缓存时限和所有 fallback 没有在本轮逐路径执行，故只记录为作者/代码声明，不升级为运行事实。
- **Evaluation Contract / Baselines / Ablations / Deployment**：lab study 将 40 名有 teaching practicum 的
  graduate proxy instructors 平分为 full pipeline 与 direct Text-to-HTML baseline；任务为 20～30 页真实 STEM
  slide/outline，约 45 分钟 authoring。编辑轮数为 `4.90±2.88` 对 `7.00±2.20`，Mann–Whitney
  `U=113, p=0.019, r=0.37`；四项问卷只有 learnability 与 controllability 达显著，time cost 与 preference
  未显著。论文没有做 component-factorial ablation，不能把总差异单独归因于 structured analysis、two-stage
  validation 或 Click-to-Locate。三个月课堂结果来自一所中国公立高中中按 deployment feasibility 选择的一个
  53 人班，与其余 493 人作 exploratory comparison；不是随机/严格控制实验，教师、设备、班级选择、考试
  漂移和其他教学差异均可能混杂。因此 `+9.21` 对 `-2.32` 只保留为该部署的 observational result，不能写成
  MAIC-UI 的因果学习收益。
- **What Evidence Proves / Does Not Prove**：论文和 artifact 支持一条可实现的系统分解：先把 domain source
  编译成 typed intermediate state，再分离 semantic generation 与 visual refinement，最后以 human-selected
  element scope + patch-based update 缩小模型修改面。实验支持该整体系统相对论文 baseline 减少编辑轮数、
  提高两项主观维度；current code 也确认 citation-to-line、full-context prompting 和 diff-first fallback 的存在。
  它不证明 structured prompt “防止 hallucination”，HTML/simulation validator 等于 scientific verifier，
  `<10s` 或约 90% token reduction 可跨模型/页面长度/网络复现，也不证明课堂分数差异由该系统造成。
- **Trade-offs / New Failure Modes / Previous Design Still Applies / Evolution**：这是 `Direct Evolution`：
  `one-shot full artifact generation -> structured intermediate state + staged validation -> user-scoped local patch
  -> bounded fallback/full regeneration`。收益是缩小 change blast radius、保留已接受 artifact、提高 intent
  localization 与交互速度；代价是 selector/XPath 在 DOM drift 后失效、diff hunk 冲突、local patch 破坏全局
  invariant、source/preview/version 分叉、validator coverage 不足、累计 patch debt，以及 full HTML 仍进入模型
  context 的隐私与成本。手工 authoring 在高保证、复杂多页或强 domain verifier 场景仍合理；全量 regeneration
  在结构变化大、patch context 已漂移时也是正确 recovery branch，而不是被新方法淘汰。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch77；已完整阅读 Ch76～78，
  并核对 Ch62 与 Ch80。Ch76 已要求定位最早可修复偏离、保留有效 state、发出 bounded change 与 stop/
  escalate；Ch77 已要求 typed task/artifact state、deterministic spine、version/replay、human approval 与
  evaluator/validator 分离；Ch62 已覆盖 artifact + environment + verifier、claim/evidence boundary；Ch80
  已覆盖 definition/run/artifact identity。MAIC-UI 将这些原则实现为 rendered-element citation 与 diff-first
  authoring case，但没有补出书稿尚未拥有的长期机制。
- **Integration Decision / Changed Files / Open Questions**：`No Change — Already Covered` / Ch77；Ch76/62
  只作为已有机制 handoff。Historical Books Gate 关闭，本轮只更新 W18、年度索引、Learning State 与
  2026-08-10 Daily，不修改 Books。待验证 event-time immutable commit、真实 K-12 teacher authoring study、
  component ablation、cross-model/page-size latency/token contract、scientific correctness 的外部 verifier、
  multi-page/long-session patch drift、privacy/retention，以及独立 classroom replication。

### Full Source Review — GoClick — 28/30

- **Candidate / Week / Score / Source Family / Type**：`DEVICE-CLOUD-SEMANTIC-PLANNER-GROUNDER-SPLIT`；
  W18；`TN 4 / SI 5 / PV 5 / SR 4 / PR 5 / L 5 = 28/30`；primary research paper + official
  repository/model/data/evaluation artifacts。arXiv:2604.23941 v1 于 2026-04-27 01:29 UTC first-public，
  当前只有 v1，事件归 W18。已完整阅读 20 页 PDF 的 metadata、Introduction、Related Work、Method、全部
  Experiments、device-cloud application、Conclusion/Limitations 与 data-availability boundary，并联读 current
  official repository、Florence-2 fine-tuning path、three-benchmark evaluation entrypoints、Hugging Face Base/
  Large model cards 与 SFT dataset surface。仓库当前只有 8 个 commits、无 event-time tag；current artifact
  能核验训练/评测接口，不能证明今天代码与 paper run 完全相同。
- **Original Problem / Why Previous Design Was Reasonable**：单个通用 cloud VLM 同时做 planning 与 pixel
  coordinate grounding，接口最简单、共享完整 context，也避免在两个模型间传递语义状态；Set-of-Marks
  进一步把连续坐标缩成有限候选，仍由 planner 统一决策。直接把 decoder-only VLM 缩小也合理，因为可复用
  通用预训练、工具链与自由生成能力。但 resource-constrained device 需要低 latency、小 memory footprint，
  GUI grounding 又是高分辨率、小目标、窄输出空间任务；通用模型的规模与能力面开始超过该 atomic action
  所需，cloud-only path 还承担网络与隐私成本。
- **Changed Constraint / Mechanism / State Ownership**：GoClick 将高层 goal、history 与动作类型留给 cloud
  planner；planner 输出 `action type + action intent / target functionality description`，端侧 grounder 接收同一
  screenshot 与该语义接口，只预测归一化坐标 token。grounder 基于 Florence-2 encoder-decoder：visual/text
  embeddings 先进入 multimodal encoder，小 decoder 只负责 coordinate output，不保留通用 free-form
  generation。训练侧把 10.8M raw samples 经元素级噪声清理、按离散 bbox + normalized referring expression
  去重、old-GUI/REG task coarse filtering 与 source/task ratio sweep 缩到 3.8M core set。cloud planner 拥有
  task belief/plan；device grounder 拥有 pixel localization；workflow 拥有 screenshot/version、semantic handoff、
  action validation 与 execution；训练 pipeline 拥有 dataset provenance、filter policy 与 model artifact identity。
- **Control Flow / Data Flow / Implementation Details**：paper path 为 `screenshot + task/history -> proprietary
  planner -> intent/function description -> GoClick -> <loc_x>,<loc_y> -> click/long-press action`；真实部署构想
  通过 HTTP 调 planner、ADB 执行动作，但作者实验实际使用 frozen trajectories 与 asynchronous offline batch
  inference。current repository 提供 Florence-2 full fine-tuning、`fix_vit`、BF16、optional LoRA、JSONL core-set
  loader，以及 AITW/AndroidControl/GUIAct 的 planner-first、grounder-second scripts；model card 用 regex 解析
  `<loc_*>` tokens。README 示例存在 `planning_prompt`/`prompt` 与 `img_size` 变量不一致，且 parser 失败回退
  `(0,0)`；因此 artifact 是可运行表面，不等于 production-hardened executor，也没有展示真实 mobile runtime、
  energy、thermal、network failure 或 action authorization。
- **Evaluation Contract / Baselines / Ablations / Sensitivity / Overhead**：grounding 以 point-inside-box accuracy
  在 FuncPred、ScreenSpot/v2、MOTIF、RefExp 与 VisualWebBench 两个 tasks 上测量。latency contract 为一张
  `780x360` image、benchmark median prompt、1×L20、batch 1、BF16、Transformers、支持时 Flash Attention、
  deterministic generation，重复 2,000 次；GoClick-B 的 `37.7 ms TTFT / 4.1 ms TPOT` 不能写成真实端侧
  SLO。architecture comparison 将 Florence2-L、InternVL2、Qwen2VL 与 SLiME 用同一 3.8M data、768² image、
  two epochs、frozen ViT、8×L20 训练，但 backbones 的 pretraining、参数量与 tokenizer 不同，所以只支持
  “在这些候选与 recipe 下 encoder-decoder 更适配”，不隔离纯 architecture causality。PDR coarse/fine
  experiments 使用 GoClick-L；大矩阵因 compute limit 各跑一 epoch且未做多 seed。10.8M→6.4M→3.8M 时
  七 benchmark 平均从 71.6→74.0→75.6，但 ratio search 与最终 report 共享 evaluation surface，存在
  selection overfitting 风险。
- **Agent Evaluation / What Evidence Proves**：AITW 使用 4,663 steps/584 trajectories，AndroidControl 只取
  random 500 steps，GUIAct 分 mobile/web；全部是无真实 device/emulator state transition 的 offline step-level
  replay，过去 screenshots 因 context limit 不进入 prompt。作者比较 standalone GPT-4o/Gemini、SoM 与
  planner+GoClick，报告 AITW/AndroidControl/GUIAct 的 Step SR 和 click accuracy 改善。它证明在论文的 frozen
  observations、planner prompts、ground-truth-action scorer 下，把 coordinate grounding 委托给专用模型能
  修复一类 planner bottleneck；不证明 online task completion、recovery、privacy、battery、thermal、network
  partition、error accumulation 或 side-effect safety。
- **What It Does Not Prove / Limitations / Threats to Validity**：paper 明确 encoder-decoder 优势只对 narrow
  grounding task，PDR 部分 heuristic 且 multi-seed 不可承担，GUI 演化需要 periodic retraining，端侧部署只在
  L20 上模拟。训练/测试来源存在 lineage overlap 风险，old GUI 被判为 harmful 也可能只是当前 benchmark
  distribution mismatch；删除旧样式会损害 legacy-app coverage。作者没有报告 confidence calibration、
  abstention、target ambiguity、多元素候选、semantic-handoff corruption、planner/grounder joint error、真实
  mobile memory/energy、online end-to-end latency、network budget、privacy retention 或 action-execution failure。
  不得把 0.2B/0.8B 作者结果外推为任意 small VLM、任意 GUI 或端侧 production readiness。
- **Trade-offs / New Failure Modes / Previous Design Still Applies / Evolution**：这是 `Direct Evolution +
  Layering`：`cloud generalist plans and grounds -> SoM constrains coordinate search -> semantic planner/grounder
  split -> task-specific small grounder placed near device`。收益来自窄输出空间、任务专用 data 与 placement；
  新成本是 semantic interface drift、planner 描述丢失视觉细节、两模型版本 compatibility、duplicate screenshot
  transfer、artifact rollout、device fragmentation、dataset refresh 和 cross-stage blame ambiguity。通用单模型在
  网络稳定、设备不能承载模型、任务需要联合视觉推理或 handoff loss 大时仍合理；SoM 在 candidate detector
  更可靠、需要可解释枚举或 device 没有 VLM 时仍是有效分支。旧 GUI data 对 legacy fleet 仍可能必要，应按
  deployment slices 而非一律删除。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 暂定 Ch10；已完整阅读 Ch74～78，
  并核对 Ch23、Ch62 与 Ch80。Ch10 已拥有 cloud/edge hybrid placement、small architecture 不能只靠缩放、
  hardware/runtime/update/device heterogeneity；GoClick 补足的是“按能力边界拆分并用 typed semantic handoff
  决定 placement”。Ch23 拥有 data relevance/dedup/lineage；Ch62 已区分 model/system/runtime/agent evaluation
  与 offline→online evidence ladder；Ch75 已拥有 planner state，Ch78 已拥有不同 model/expertise 的 typed
  handoff 与 coordination tax，Ch74/77/80 已拥有 action executor、workflow 与 artifact identity。故不新增章节，
  也不把该固定两阶段 pipeline 误写为 Multi-Agent 自主协作。
- **Integration Decision / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch10；Ch23/62/75/78 只接 data、evaluation 与 planner/expert handoff。Historical Books Gate
  关闭，本轮只更新 W18、年度索引、Learning State 与 2026-08-10 Daily，不修改 Books。待验证 event-time
  immutable code/data/run manifest、真实 Android/iOS/NPU latency-memory-energy-thermal、online task success 与
  recovery、multi-seed/held-out PDR、cross-family matched-parameter architecture ablation、legacy/current GUI
  slice、semantic-handoff calibration/abstention、joint planner-grounder failure，以及 privacy/network policy。

### Full Source Review — AutoGUI-v2 — 27/30

- **Candidate / Week / Score / Source Family / Type**：`HIERARCHICAL-GUI-FUNCTIONALITY-EVALUATION`；W18；
  `TN 4 / SI 4 / PV 5 / SR 4 / PR 5 / L 5 = 27/30`；primary research paper + official benchmark
  implementation/datasets。arXiv:2604.24441 v1 于 2026-04-27 13:06 UTC first-public，当前只有 v1，事件归
  W18。已完整阅读 51 页 PDF 的 metadata、Introduction、Related Work、Method、Experiments、Conclusion、
  Limitations、全部 implementation/task-generation/statistics/prompts/case-analysis Appendices，并联读 current
  official repository、16-commit history surface、annotation/evaluation commands，以及公开的 region-grounding
  dataset viewer。repository 无 event-time tag，README 仍把 element-captioning dataset 标为 TODO；current
  artifact 可核验 pipeline surface，不能反向证明 paper run 的所有数据、代码和结果都已冻结发布。
- **Original Problem / Why Previous Design Was Reasonable**：传统 GUI grounding 以外观描述或 action intent
  找元素，flat element list、随机负例与单步坐标 scorer 成本低、容易批量复现，也适合验证 perception/localization
  基础能力。但视觉相近的 icon 可能对应完全不同功能，区域级结构又决定 element 的上下文语义；外观命中不能
  证明模型理解“交互后会发生什么”。约束变化不是 Agent 已经能稳定完成长任务，而是 evaluator 需要把
  appearance、intent、function 与 outcome 分开测量，并构造更难以依赖表面相似度的 negatives。
- **Changed Constraint / Mechanism / State Ownership**：pipeline 先让 Gemini-2.5-Pro-Thinking 递归把 screenshot
  分成 hierarchical functional regions，为每个 node 生成 type、layout、functionality、normalized bbox 与
  divisibility；独立 checking call 给 completeness 0～3 和 boundedness yes/no，平均 completeness `>=2.5`、
  bounded ratio `>=0.8` 才接受，否则提高 temperature 重试，最多三轮，最终保留最高 combined score。
  人工 annotator 再通过 FastAPI/SPA correction UI 修正 bbox，原始文件不覆盖，而以 timestamped `_fix` artifact
  保存；box 改变后重新生成 semantic labels。benchmark builder 拥有 hierarchy、correction provenance、group
  identity、prompt 和 answer；model under test 只拥有当前 screenshot/question；scorer 拥有 bbox/choice truth。
- **Control Flow / Data Flow / Implementation Details**：六类来源经筛选进入 region division；AMEX 与
  AndroidControl 各取 120 个包含 similarity group 的 screenshots，ScreenSpot-Pro 取 271，AgentNet 取 120，
  MMBenchGUI 使用 1,856，OSWorld-G 使用 250。region grouping 先用 Qwen3-Embedding 对 description 做 cosine
  clustering（阈值 0.6），排除 parent-child，再由 Gemini 做 visual verification、补候选和 `2～5` group-size
  约束，最后执行 overlap removal、minimum-size 和 duplicate merging。element path 用 OmniParser-v2 检测，
  DINO-v3 visual cosine、fuzzy text 与 disjoint-set clustering 找 visually similar elements，再生成 grounding 与
  interaction-outcome tasks。公开 region-grounding split 为 442 rows，字段包含 source、image size、question、
  correct bbox、options、region types、density、descriptions、functionalities 与 group provenance。
- **Evaluation Contract / Baselines / Slices / Overhead**：benchmark 共 2,753 tasks、3,710 hierarchical regions，
  含 region grounding 442、region captioning 447、element grounding 1,076、element captioning 788，跨六个 OS。
  commercial、general open 与 GUI-specialized VLM 均在 native resolution、model-specific tuned prompts 下测量；
  open GUI models 走 A100 Hugging Face endpoints。grounding 使用 center-in-box/IoU，captioning 使用 MCQ
  accuracy；element grounding 按 action type、similarity-group size 与 NID（expanded target bbox 中其他 element
  center 数，分 tertiles）切片。不同 model family 使用不同 coordinate convention/prompt，且没有统一 latency、
  token、sampling/repeat、hardware 或 uncertainty contract，因此横向表格不是完全同构的 system comparison。
  annotation cost 的 `$1.072/screenshot` 只是 1920×1080、最多十个二级 regions、最多三轮 refine 与 Gemini
  列价下的估算，不是实际全数据集成本。
- **What Evidence Proves / Does Not Prove**：结果支持在该 frozen static suite 中，function-based grounding 比
  parallel appearance/intent prompts 更难，hard negatives 比 easy negatives 更能暴露功能混淆；GUI-specific
  fine-tuning 对 grounding 有利，而 commercial VLM 在 captioning 上更强，说明 localization 与 semantic
  explanation 不能用单一分数替代。NID 趋势和 action-type差异只是相关切片；作者关于 richer context 的解释
  不是 causal proof。suite 不执行真实 click，不观察 environment transition，不测 multi-step planning、recovery、
  side effects 或 production autonomy。paper 明确只生成 next-step/single-step outcome，未分析 functionality
  understanding 与多步 planning 的关系，且数据偏 English/Western GUI；所以不能把高分写成 online Agent
  success，也不能把静态 region label 当作真实应用状态。
- **Limitations / Threats to Validity / Artifact Boundary**：全自动 annotation 没有成立，VLM bbox 需要人工
  修正；同一 Gemini family 参与 region proposal、checking、visual grouping 与 question generation，可能产生
  correlated ontology/judge bias。论文未披露 annotator agreement、独立 double review、sampling uncertainty、
  repeated model runs 或 contamination audit；数据复用既有 GUI benchmarks，训练重叠不能排除。model-specific
  prompts 提高各模型适配性，却削弱 prompt-invariant comparability；center-in-box 对大 bbox 宽松，MCQ 又只
  测给定 alternatives。repository 当前可重放 surface 丰富，但 dataset publication 不完整、无 immutable
  paper-run manifest，不能把 README 的“automatic at scale”升级为 fully automatic reproducibility claim。
- **Trade-offs / Previous Design Still Applies / Evolution**：这是 `Direct Evolution + Layering`：`flat visual
  grounding -> hard-negative element functionality -> hierarchical region function -> outcome prediction -> future
  interactive trajectory/outcome evaluation`。它获得可解释的 capability decomposition、上下文功能 slices 与
  annotation provenance，却新增 ontology drift、VLM-generated-label bias、人工 correction cost、group
  selection bias、prompt/model coupling 和 benchmark leakage。flat appearance grounding 仍适合 perception
  regression；静态 functionality suite 适合低成本定位模型缺口；只有部署本身需要连续 action 时，才应继续
  升级为 environment transition、terminal outcome、side-effect 与 recovery evidence，不能用后一层否定前一层。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch62；已完整核对 Ch61～63，
  并阅读 Ch75、Ch77 的 planning/workflow 边界。Ch62 已明确 `Model/System/Runtime/Agent` 四层对象、完整
  subject/environment/scorer identity、per-example evidence、hard slices、uncertainty、judge calibration，以及
  `single snapshot -> feedback-conditioned trajectory -> environment outcome/recovery` 的演进。AutoGUI-v2 是
  “static functionality capability suite” 的高质量案例，但没有改变这些长期设计结论。Ch75 拥有多步 planning，
  Ch77 拥有 durable execution；两章不应接收一个不执行动作的 benchmark 机制。
- **Integration Decision / Changed Files / Open Questions**：`No Change — Already Covered` / Ch62。它为已有
  evaluation framework 提供具体实例与压力测试，没有新增需要进入 Books 的通用机制；Historical Books Gate
  关闭，本轮只更新 W18、年度索引、Learning State 与 2026-08-10 Daily，不修改 Books。待验证 immutable
  paper-run code/data/prompt manifest、element-captioning release、human agreement、independent question audit、
  train-overlap/contamination、multi-seed uncertainty、prompt-normalized comparison，以及 static functionality
  是否能预测 interactive/multi-step outcome。

### Full Source Review — X-WAM — 28/30

- **Candidate / Week / Score / Source Family / Type**：`UNIFIED-4D-WORLD-ACTION-MODEL`；W18；
  `TN 5 / SI 5 / PV 5 / SR 4 / PR 4 / L 5 = 28/30`；primary research paper + project page + later official
  implementation。arXiv:2604.26694 v1 于 2026-04-29 14:01 UTC first-public，v2 于 2026-05-07，故 W18
  只使用 v1 作为事件证据，v2 只作 revision boundary。已完整阅读 v1 HTML/PDF 的 metadata、Introduction、
  Related Work、Method、公式、Algorithms、Implementation、Policy/4D evaluation、ablations、逐任务结果、
  real-robot setup/results、Limitations 与全部 Appendices，并联读作者项目页。当前 official repository 的
  post-training code、checkpoints 与 datasets 标注为 2026-06-09 才发布；它能核验后来公开的 training/evaluation
  surface，不能倒推 W18 已有 immutable artifact，也不能把 v2 增补的 real-robot 内容当作 v1 事件事实。
- **Original Problem / Why Previous Design Was Reasonable**：VLA 直接从视觉/语言输出 action，计算路径短、
  latency 容易控制；video world model 预测未来 observation，适合学习动态与规划；早期 unified WAM 在二维
  pixel space 共享视频/action representation，又避免同时维护两个大模型。这些旧分支在低延迟控制、只有二维
  视频数据或不需要显式几何重建时仍合理。约束变化是同一具身系统既想利用大规模 video prior，又要预测
  multi-view RGB-D、future state 与可立即执行 action；高维视频需要较多 denoising steps，低维 action 的 deadline
  却更短，统一同步 schedule 会让最快到期的输出等待最慢模态。
- **Changed Constraint / Mechanism / State Ownership**：X-WAM 从 Wan2.2-TI2V-5B 出发，把 instruction、初始
  proprioceptive state 与多视角 RGB 编成统一 bidirectional full-attention denoising sequence，预测 8 帧未来 RGB、
  8 个 future states、32 个 actions 与 depth。RGB 由 causal VAE 表示，state/action 经 MLP 投影；view embedding
  区分相机，temporal RoPE 对齐 state/action 时间。主 DiT 拥有 video/action/state shared latent，复制最后
  `M=10` 个 blocks 形成 depth branch；depth branch 单向 cross-attend 主分支，主分支不读取 depth，policy decode
  时可关闭。模型拥有预测状态，robot controller 拥有已经 dispatch 的 action 与真实环境，hand-eye calibration
  拥有 wrist-camera pose 变换；这些 ownership 不能因“统一模型”而混成一个 truth state。
- **Control Flow / Data Flow / Implementation Details**：Asynchronous Noise Sampling 在 inference 使用 action
  `T_a=10`、video `T_o=50`：前十步联合去噪后立即 dispatch clean action，随后只继续 video 去噪并以 clean
  action 条件化。training 不独立随机两个 timestep，而以概率 `p=0.5` 采样 `t_a=0, t_o~U(0,1)`，否则
  `t_a~U(0,1)`、`t_o=t_a+(1-t_a)b`、`b~Beta(1.5,1)`，保证 `t_o>=t_a` 并覆盖推理将遇到的 action-clean/
  video-noisy 状态。数据统一成 16-D absolute state 与 14-D relative action；单臂只监督前部维度，按 dataset
  做 quantile normalization，action scaling 不加 bias 以保留 zero-motion。1,492,026 episodes / 5,873.9 hours
  来自六类公开/内部组合，3.75 FPS、320×256；大部分 depth 由 Video Depth Anything pseudo-label，故 depth
  supervision 不是独立真实几何 ground truth。
- **Evaluation Contract / Baselines / Ablations / Hardware**：pretraining 使用 256 H20、总 batch 2,048、40k
  steps；benchmark fine-tuning 使用 32 H20、总 batch 128、20k steps；inference 为 UniPC、CFG 1.0、
  `T_a/T_o=10/50`，每任务 100 episodes。RoboCasa 24 tasks 报告平均 79.2%；RoboTwin 50 tasks 报告 clean
  89.8%、randomized 90.7%。部分 baseline 数字来自原论文，只有 DreamZero/UWM 在 Wan2.2-5B 上重实现，
  因此不是全部同代码、同训练预算的 matched comparison。depth architecture ablation 中 no-depth、sequence
  concat、channel concat、branch 的 success/latency 分别为 `63.0/1033ms`、`68.7/1888ms`、
  `64.2/1266ms`、`67.8/1033ms`；该表未披露 latency GPU/dtype/batch，且 ablation 不使用大规模 pretraining，
  不能与 headline success 直接合并。论文 v1 的 real-robot evidence 是 v2 revision 边界；v2/current setup 的
  8-step、约 300ms/action chunk 与 15Hz RTC 只能作 later evidence，不能倒写入 W18 score justification。
- **What Evidence Proves / Does Not Prove**：作者实验支持在其 data/model/benchmark contract 下，单向 late
  depth branch 可以避免 depth-token sequence doubling，并在 branch-off policy path 中不增加表内 action latency；
  coupled asynchronous timestep sampling 相比作者 synchronous/naive asynchronous variants 改善了 action
  deadline 与 video quality 的折中。这不证明 predicted depth 是因果/metric-accurate world state，不证明统一
  model 普遍优于专用 policy + world model，也不证明 50-step imagined video 会提升 online planning。
  100-episode simulation success 不能外推真实设备；不同来源 baseline、伪 depth、无置信区间/seed variance、
  静态相机像素指标与成功 episode 才计 completion time 都限制因果解释。高 fidelity video 也不等于 action
  consequence 正确，世界模型越真实地渲染错误未来，越可能让 planner 过度信任。
- **Limitations / Threats to Validity / Artifact Boundary**：论文明确承认固定 observation window、没有 history/
  autoregressive rollout/KV cache、统一模型比专用 policy latency 更高，以及执行期间 observation 继续变化导致
  action stale。ANS 新增双 timestep、partial-completion 与 clean-action conditioning state；失败时必须区分
  action 已 dispatch、video 尚在生成、controller 已推进和 model context 仍旧。depth branch 的 unilateral
  isolation 保护主 prior，却限制深度信号反向影响 RGB/action representation；sequence concat 质量更高但 latency
  更大，说明 branch 是 Pareto 选择而非绝对最优。current repository 只有两个可见 commits、无 event-time tag，
  且 code/checkpoints/datasets 明确晚于 W18 发布；因此 reproducibility 为 later artifact support，不是同步公开。
- **Trade-offs / Previous Design Still Applies / Evolution**：这是 `Direct Evolution + Layering`：`专用 VLA
  policy / 独立 world model -> 2D unified video-action denoising -> 3D-supervised late branch -> modality-specific
  completion deadlines -> future history-aware closed-loop world-action model`。收益是共享 video prior、显式空间
  supervision 与 action-first dispatch；代价是 5B generative policy 的 latency/compute、伪深度误差、multi-task
  interference、branch/version compatibility、双 schedule observability、stale action 与 partial-result recovery。
  专用 policy 在严格 control-loop deadline 下仍成立；独立 world model 在 planning/reconstruction 不应拖慢
  actuator 时仍成立；sequence concat 在离线重建质量优先时仍可能合理。下一阶段压力不是增加模态名称，而是
  long-history state、causal intervention、uncertainty、closed-loop correction、deadline-aware cancellation 与
  action/video/world-state identity。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 暂定 Ch10；已完整阅读 Ch9～10，
  并核对 Ch20、Ch38 与 Ch62。Ch10 已拥有 `multimodal perception + latent dynamics + planning + memory +
  real-world feedback`、pixel fidelity 不等于 causal correctness、sim-to-real gap 与 intervention/long-horizon
  evaluation；X-WAM 可补足的是“同一 world-action model 内各模态 deadline 不同，统一 representation 不等于
  统一 schedule”及 partial-completion ownership。Ch20 拥有 text sampling，不应吸收 diffusion schedule；
  Ch38 只接 real-time multimodal inference/cancellation handoff；Ch62 只接 simulation→robot outcome 与
  workload-contract handoff。因此不新增 Part/章节，也不把一个 early embodied model 写成世界模型必然路线。
- **Integration Decision / Changed Files / Open Questions**：provisional `Refine — Existing Argument
  (Experimental)` / Ch10；Ch38/62 short handoff。Historical Books Gate 关闭，本轮只更新 W18、年度索引、
  Learning State 与 2026-08-10 Daily，不修改 Books。待验证 event-time immutable artifact、v1/v2 内容差异、
  latency hardware/dtype/batch、multi-seed confidence interval、matched-compute dedicated-policy/world-model
  baselines、真实 metric depth、history/KV design、action cancellation/reconciliation、long-horizon causal accuracy
  以及 later real-robot evidence 的独立复现。

### Full Source Review — ExoActor — 24/30

- **Candidate / Week / Score / Source Family / Type**：`EXOCENTRIC-VIDEO-TO-HUMANOID-CONTROL`；W18；
  `TN 4 / SI 4 / PV 3 / SR 3 / PR 5 / L 5 = 24/30`；work-in-progress primary paper + official project
  page。arXiv:2604.27711 唯一 v1 于 2026-04-30 10:57 UTC first-public。已完整阅读 metadata、Introduction、
  Method、case/failure/ablation studies、latency、Discussion、Related Work、Conclusion 与全部 Appendix prompt
  sections，并联读项目页及其 demo surface。项目页的 Code 链接当前指向不存在的 `BAAI-Agents/ExoActor`
  repository（404）；无 code、model、dataset、configuration 或 immutable run manifest 可独立复现。
- **Original Problem / Why Previous Design Was Reasonable**：task-specific humanoid policy、retargeting 与
  simulator/RL 分别提供直接监督、显式 embodiment mapping 和动态约束，虽然数据昂贵，却能把 motion target、
  controller state 与 success criteria 定义清楚。纯视频生成则有更广的人类动作 prior，但视觉合理不等于可执行。
  ExoActor 面对的约束变化是希望不为每个新场景采集真实 robot demonstrations，而复用 human-centric image/video/
  motion priors；其核心问题不是生成更漂亮的视频，而是能否把跨 domain 的 visual trajectory 转成物理机器人
  可跟踪的 reference，同时保留任务、空间与接触语义。
- **Changed Constraint / Mechanism / State Ownership**：pipeline 先用 Nano Banana Pro 把 Unitree G1 的第三人称
  初始图像转换为 human-like subject，同时声称保持 scene/viewpoint/pose/orientation/scale；GPT-5.4 Thinking
  把高层 goal 分解为 visually observable atomic action chain，并结合初始 frame 构造 Shot/Scene/Motion/
  Execution/End State prompt；Kling 3 生成 fixed-camera video。GENMO 从 monocular video 恢复 SMPL whole-body
  motion，WiLoR frame-wise 输出 bilateral hand pose 和 open/half-open/closed state；SONIC controller 读取当前
  robot state 与 reference-motion window，Dex3-1 手部 command 经 event queue 发布。video generator 拥有 imagined
  scene，motion estimator 拥有 reconstructed kinematics，controller/robot 拥有 physical state；任何一层都不能
  把上游预测提升为真实 contact/pose truth。
- **Control Flow / Data Flow / Implementation Details**：`task + initial exocentric frame -> robot-to-human image ->
  action chain -> generated clips -> SMPL body + hand state -> SONIC reference window -> Unitree G1 execution`。
  hand state 与 whole-body trajectory 按原始 video FPS 对齐；视角约定会按 front/back 改变左右手列的语义，属于
  必须版本化的 interface contract。系统选择不做 GMR/OmniRetarget：retargeting 可降低 jitter，却会因 noisy
  global position、foot sliding 与 limb-scale mismatch 改变空间轨迹；作者在其案例中选择位置精度而非 smoothness，
  依赖 SONIC 吸收不连续。这个选择不是“retargeting 无用”，而是当前 contact/location-sensitive workload 的
  Pareto 点。
- **Evaluation Contract / Baselines / Ablations / Hardware**：论文按 B/A/S 三档展示 navigation、coarse
  interaction 与 fine-grained manipulation case studies，并比较 Kling 3、Veo 3.1、Wan 2.6，GENMO/CRISP，
  retargeting on/off 与 camera viewpoint。没有披露每档任务总数、每任务 trials、success rate、failure denominator、
  human/judge rubric、randomization、confidence interval、seed 或 matched API settings；所以“generalization”
  只是 selection-visible feasibility evidence。latency 仅报告 robot-to-human `10.7s/request`、decomposition
  `2.5s/request`、video generation `13.2s / video-second`、whole-body estimation `2.9s / video-second`、hand
  estimation `16.4s / video-second`，没有 hardware、model/API region、batch、concurrency、video resolution/
  duration、network 或 controller SLO，不能相加为通用 end-to-end latency。
- **What Evidence Proves / Does Not Prove**：demo 与失败案例证明这条 modular interface 在选定场景中能把
  generated human motion 驱动到真实 G1，并暴露 video hallucination、occlusion/wrist ambiguity、spatial drift、
  physical mismatch 的串联传播；作者甚至需要在部分 S-level target 下放置小垫高底座补偿 hand-height error。
  这支持“每个 representation handoff 都是 correctness boundary”。它不证明无需 task-specific data 的普遍
  zero-shot control，不证明 Kling 的物理 fidelity 排名，不证明 SONIC 可以安全过滤任意 imagined motion，也
  不证明 open-loop replay 能应对动态环境。没有定量 success contract 时，案例数量和项目页视频不能替代
  benchmark。
- **Limitations / Threats to Validity / Failure Modes**：论文明确把当前实现定义为 offline、open-loop：完整
  image transfer、video、motion estimation 结束后才执行，不读取执行期 scene feedback。生成器可能增删物体、
  改变动作链或产生不可能姿态；monocular motion estimation 在遮挡、rear view、快速动作与 wrist rotation 上
  不可辨识；controller 还会遇到 height/distance/torque/contact mismatch。style transfer 新增 embodiment-domain
  drift，第三人称 external camera 新增 deployment dependency，离散三档 hand state 丢失 finger/contact detail；
  pipeline 组件独立升级还会造成 prompt/view/SMPL/controller compatibility drift。缺 artifact 与 quantitative
  denominator 使“显著减少失败”“稳定”“无需数据”等措辞保持作者观察，不升级为独立事实。
- **Trade-offs / Previous Design Still Applies / Evolution**：这是 `Layering + Principle Reuse`，不是已经证明的
  end-to-end model evolution：`task-specific demonstrations/policy -> human video prior as imagined demo ->
  motion intermediate representation -> physics-aware controller -> future streaming closed loop`。它以 modularity
  和跨场景 prior 换来多个 lossy handoff、累计 latency 与 error amplification。直接 VLA/policy 在严格实时、
  precise contact 与可收集 robot data 时仍合理；retargeting 在 smoothness/embodiment safety 比 absolute path
  更重要时仍合理；simulation/RL 在 torque/contact constraint 必须可验证时不可省略。后续真正演进需要短 horizon
  streaming、online perception/replanning、feasibility verifier、uncertainty/abstention 与 typed cancellation，
  不能仅把完整 video 生成得更长。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 为 Ch10；已完整阅读 Ch9～10，
  并核对 Ch38、Ch62、Ch75 与 Ch77。Ch10 已明确 world model、low-level controller、real-world feedback 的
  分层，以及 pixel/video plausibility 不等于 causal correctness；ExoActor 的 modular imagined-demo case 正好
  落在已有边界内。Ch38 只接 offline→streaming latency/state handoff；Ch62 已拥有 feasibility→interactive
  outcome evidence ladder；Ch75/77 已拥有 feedback-conditioned plan 与 durable execution，但本论文没有在线
  planner/workflow runtime。故不新增章节，也不把 case-study pipeline 写成新的通用控制范式。
- **Integration Decision / Changed Files / Open Questions**：`No Change — Already Covered` / Ch10。该候选提供
  高价值反例与 failure-chain 证据，但现有章节已拥有相同长期判断，且缺少可复现 artifact 与定量 evaluation，
  不足以新增设计结论。Historical Books Gate 关闭，本轮只更新 W18、年度索引、Learning State 与
  2026-08-10 Daily，不修改 Books。待验证 official code/data/run release、frozen task/trial denominator、
  matched video/motion baselines、完整 latency hardware/SLO、closed-loop streaming、controller safety envelope、
  independent task-success audit、support-free S-level trials 与 real-world perturbation recovery。

### Full Source Review — Representation Fréchet Loss — 29/30

- **Candidate / Week / Score / Source Family / Type**：`POPULATION-STATISTIC-GENERATIVE-POST-TRAINING`；W18；
  `TN 5 / SI 5 / PV 5 / SR 4 / PR 5 / L 5 = 29/30`；primary research paper + current official repository。
  arXiv:2604.28190 唯一 v1 于 2026-04-30 17:59 UTC first-public。已完整阅读 metadata、Abstract、Introduction、
  Related Work、Method、Algorithm 1、全部 property/scalability/system/text-to-image experiments、training/evaluation
  details、reward-hacking/human-study/limitations appendices 与 detailed tables/prompts，并核对当前 official repository
  的公开目录、training/evaluation scripts、checkpoints/data 声明。当前仓库只有后续可见状态且无 immutable W18 tag；
  本轮网络也无法进一步冻结 raw code revision，因此“实现公开”与“事件时点 artifact 可重放”保持分离。
- **Original Problem / Why Previous Design Was Reasonable**：few-step generator 的单样本或小 batch objective
  能直接 backprop、低方差地优化 paired target，却不一定约束生成 population 的均值、协方差与多样性；传统
  Fréchet Distance（FD）使用数万真实/生成 samples 估计分布，适合作 evaluation，却因 sample population 远大于
  gradient batch 而不适合直接作每步 loss。先做 distillation、adversarial/perceptual training 或只在训练后算 FID
  仍然合理：它们避免维护长期 estimator state，也不会把单一 evaluator 的 blind spot 直接写入参数。约束变化是
  one-step/few-step post-training 需要直接改善 distribution-level fidelity/diversity，同时保持普通 distributed
  minibatch 的内存与反向传播成本。
- **Changed Constraint / Mechanism / State Ownership**：论文将 population estimation window 与 gradient window
  解耦。对 representation features 的 real/generated Gaussian 计算 Fréchet Distance：
  `||mu_r-mu_g||^2 + Tr(Sigma_r+Sigma_g-2(Sigma_r Sigma_g)^(1/2))`。Real moments 离线预计算；generated
  moments 由两种 stateful estimator 获得：Queue 保存约 `N` 个历史 features，旧 features `detach`、只有当前
  batch 参与梯度；EMA 保存一阶/二阶矩 `mu` 与 `M=E[ff^T]`，再用 `Sigma=M-mu mu^T`，历史 state 同样
  `detach`。因此 optimizer step 只反传当前 batch，却通过历史 population state 改变 objective。Training runtime
  必须拥有 representation identity、real-stat digest、queue/EMA content、warm-start、`beta/N`、distributed
  world size 与 checkpoint/restart semantics；仅保存 model/optimizer weights 不能重放相同更新轨迹。
- **Control Flow / Data Flow / Implementation Details**：`real images -> frozen representation -> offline
  (mu_r,Sigma_r)`；训练时 `noise/condition -> generator -> image -> frozen representation -> all_gather current
  features -> update detached Queue or EMA moments -> FD loss -> current-batch gradient -> generator update`。
  Matrix square root 通过 symmetric product 的 eigenvalues 与 `torch.linalg.eigvalsh` 计算。Queue 用更大近似
  population 换取显存与 stale features；EMA 只保存 moments、内存更低，却以指数权重偏向近期 policy。论文还
  用多 representation 的 normalized FD 平均值训练，默认 `SIM = SigLIP2 + Inception + MAE`；其 `FDr^K`
  先以 validation-vs-training reference 对每个 representation 归一化，再跨 representation 聚合。这里
  representation set 不是 cosmetic metric list，而是实际 objective specification。
- **Evaluation Contract / Baselines / Ablations / Hardware**：主实验为 ImageNet-1k 256/512，pMF（pixel）、
  iMF（latent）与 JiT（pixel）统一重实现，均从官方 base weights 开始；global batch 1024、BF16、AdamW、
  cosine schedule、5 warmup epochs，pMF/iMF learning rate `1e-6`、JiT `1e-5`；ablation 50 epochs、system
  comparison 100 epochs；默认 EMA `beta=.999`，先用 50K samples warm-start。Evaluation 用 50K generated
  samples 对 training statistics，覆盖 Inception、ConvNeXt-v2、MAE、DINOv2、SigLIP2 与 CLIP。论文没有披露
  GPU 型号、数量、通信拓扑、wall time、energy 或 production SLO，因此任何训练成本与吞吐结论都保持
  `Not Disclosed`。Text-to-image 只在 256×256 的 SD3.5 Medium 2.5B、15K steps、batch 1024 BF16、one NFE、
  CFG 1、EMA `.999` 下给出 qualitative demo，并分别使用 BLIP3o 3M photoreal 与 GPT-4o-distilled 60K stylized
  reference distributions，不能与 ImageNet quantitative contract 合并。
- **What Evidence Proves / Does Not Prove**：作者结果证明在上述三个 model families 与 ImageNet contract 下，
  detached population estimator 能让 FD 作为可训练 loss，并把 multi-step JiT 转为 one-step；Queue/EMA、warm
  start、representation set 与 `beta/N` ablation 也证明 estimator design 会实质改变结果。Queue 从 0 增到
  5K/10K/50K 多数改善，500K 又因 stale population 回退，支持“更大历史并非单向更好”。单独优化 Inception
  可得到更好的同源 FID、却在跨 representation `FDr` 上恶化；100 倍 learning rate 还能制造高 IS/低 FID 但
  肉眼失真的 samples，支持 Goodhart/reward-hacking 风险。证据不证明 FD-SIM 是通用最优 objective，不证明
  Gaussian 二阶统计覆盖 semantics/composition/safety，不证明 one-step 普遍优于 multi-step，也不证明 qualitative
  text-to-image 风格变化是质量提升。
- **Limitations / Threats to Validity / Failure Modes**：Gaussian approximation 只保留 feature mean/covariance；
  frozen encoder 的 blind spot 会成为 loss 的 blind spot。同一 representation 同时训练与评估会形成直接
  optimization leakage；六个 held-out encoders 只是较宽的 proxy set，不是 deployment ground truth。Queue/EMA
  在 moving generator 下不是 i.i.d. population：过旧 state 引入 policy lag，restart 丢 state 会改变 objective，
  model/encoder upgrade 会让 moments 失去可比性。作者 human study 为 17 人、2,929 valid votes、匿名 3×3 grids、
  matched noise 与随机左右顺序；它提供受限 preference evidence，但不能代表真实用户或任务成功。实验主要集中
  ImageNet，text-to-image 没有 quantitative/human preference gate；evaluation sampling 虽按官方代码/checkpoint
  操作并人工检查图像，但 coding-agent-assisted setup 仍可能引入未量化的 implementation variance。
- **Trade-offs / Previous Design Still Applies / Evolution**：关系是 `Direct Evolution + Layering`：`offline
  population metric -> metric as minibatch loss -> persistent Queue/EMA estimator -> multi-representation objective ->
  held-out cross-representation/human audit`。它以 distribution-level pressure 换取 estimator state、cross-device
  gather、eigendecomposition、staleness 与 scorer gaming surface。Paired reconstruction/perceptual objectives 在
  identity/local alignment 重要时仍成立；adversarial objectives 在 critic 能学习更高阶差异时仍合理；multi-step
  diffusion 在 latency budget 允许且单步失真不可接受时仍合理；offline FD 作为 independent evaluation 也不应
  被训练 loss 取代。下一阶段压力是 estimator rollback/versioning、adaptive representation diversity、independent
  human/task evaluators，以及在非图像与 deployment distributions 上验证跨域稳定性。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage**：主 owner 暂定 Ch62；已完整阅读 Ch23～25
  与 Ch62。Ch24 明确只拥有 language next-token objective、training step 与 optimizer state，不能把 diffusion
  post-training 误写成 pretraining 通用路线；它只接“population estimator 属于 checkpointed training state”的
  handoff。Ch62 已拥有 scorer identity、distribution-conditional evidence、proxy/Goodhart、held-out suite 与
  feedback-contamination 边界；本论文可补足的是 scorer 被提升为 loss 后，evaluation state 如何进入 optimizer
  control loop，以及 representation diversity 为什么同时属于 objective 与独立 audit。Ch23 只接 reference
  distribution/provenance handoff，Ch25 不拥有该机制。因此不新增 Part/章节。
- **Integration Decision / Changed Files / Open Questions**：暂定 `Refine — Existing Argument (Experimental)` /
  Ch62，Ch24/23 只接短 handoff。Historical Books Gate 关闭，本轮只更新 W18、年度索引、Learning State 与
  2026-08-10 Daily，不修改 Books。待核验 immutable event-time commit/tag、真实 code-level state checkpoint/
  all-gather semantics、hardware/time/memory overhead、multi-seed uncertainty、independent reproduction、held-out
  encoder rotation、non-Gaussian/high-order metrics，以及 queue/EMA state 在 elastic restart、encoder upgrade 和
  distributed reshard 下的 migration/rollback contract。

### Recovered Full Source Review — ViPO — 27/30

- **Source / Full-read Coverage**：arXiv:2604.24953v2，v1 first-public 2026-04-29；2026-08-13 HTML 恢复。
  已读 Poly-DPO 数学、ViPO-Image-1M / Video-300K construction、SD1.5/SDXL/SD3.5/FLUX/Wan experiments、
  alpha / data-quality / stability ablations、training details、open-dataset replacement、limitations 与 artifact links。
- **Problem / Previous Design / Mechanism**：standard Diffusion-DPO 在高质量、单一偏好信号上合理，但旧视觉
  preference pairs 同时混入 alignment、aesthetics、text 与 anatomy 等相互冲突维度，盲目扩数会饱和。Poly-DPO
  将 DPO 看作 binary classification，在 loss 加 `alpha(1-p)`，以 `(1+alpha*p)` 重标梯度：正 alpha 聚焦冲突数据的
  informative uncertainty，负 alpha 抑制过易样本，干净平衡数据趋向 alpha=0 / standard DPO。数据侧按 alignment、
  text、human quality、composition、aesthetics 与 video motion/quality/alignment 分工构造并保留 provenance。
- **Evaluation / Boundary**：作者结果支持所披露模型、batch/steps/beta、GenEval/DPG/VBench 与 human protocol 下的
  相对改善；不证明 alpha 可跨 domain/model 自动确定。摘要称 300K video pairs，而 dataset comparison table 显示
  30K pairs，需要按 revision/artifact 继续核对。proprietary-generator subset 因 license 被 open replacement 重建；
  三 VLM majority vote 减少单 judge 偏差但不能成为人类偏好真值。未披露完整 hardware/compute、multi-seed 与生产 SLO。
- **Trade-offs / Evolution / Chapters**：`raw preference scale → conflict-aware objective → category-balanced curated pairs →
  high-quality data makes extra objective vanish` 是 Ch30 的 `Direct Evolution`，Ch23/27/62 handoff。它说明算法复杂度
  可以补偿脏数据，但不应替代数据治理；standard DPO 在干净、平衡 pair 上仍是更简单分支。provisional
  `Refine — Existing Argument / Experimental`；Books Gate 关闭。待核验 300K/30K 账目、event-time dataset、judge
  agreement、跨模型 alpha calibration 与 full compute contract。

### Remaining Access-Blocked Source Review — Safety Drift After Fine-Tuning

- **Candidate / Week / Source / Access Status**：Safety Drift After Fine-Tuning，arXiv:2604.24902，已记录
  first-public 2026-04-27，归 W18。ViPO（arXiv:2604.24953）已于 2026-08-13 恢复并在上一节完成全文审计。
  Safety Drift 在 2026-08-11
  本检查点尝试直接读取 arXiv primary HTML 时，当前浏览器的已保存权限明确拒绝该站点；随后尝试从公开搜索
  入口定位作者 project/repository 时，搜索站点权限也被拒绝。本地 repository 与允许读取的临时目录中没有论文
  正文、PDF、project snapshot 或既有 Source Packet。因此 Safety Drift 状态为 `Unverified / Blocked`，不是 `Audit
  Pending`，更不是 Full Source Review。
- **Full-read Coverage / Evidence Boundary**：当前只拥有题名/ID/first-public attribution；Abstract、Introduction、
  Background、Related Work、Method、公式、算法、Implementation、Evaluation、baselines、ablations、hardware、
  model、precision、length、batch、concurrency、SLO、Limitations、Appendix 与作者 artifact 均为 **Not Read /
  Not Verified**。没有从 acronym、题名或日期反推机制，不给出 Technical Novelty、System Impact、Practical
  Value、Source Reliability、Project Relevance、Longevity 分数，也不创建 Source Family evolution claim。
- **ROADMAP / Books / Gate Decision**：在 primary text 可读前，不指定 owner chapter，不阅读目标章节来制造
  虚假 mapping，不形成 `Integrate / Refine / No Change` disposition。该项不会进入 Books，Historical Books Gate
  继续关闭。用户于 2026-08-11 明确授权“暂时标记后跳过”，因此该项进入 post-forward backlog，forward cursor
  可以移动到 W19；这不等于 W18 Historical Evidence Gate 通过，后续仍必须回补。
- **Resume Condition / Open Questions**：恢复对 arXiv 或作者官方 project/repository 的只读访问后，对 Safety
  Drift 按固定 Source Packet 覆盖全部方法、实现、实验条件、限制和相邻章节。访问恢复前，任何二级摘要、搜索
  snippet 或题名推断都不能替代 primary source。
- **Post-forward retry（2026-08-13）**：ViPO 已恢复；Safety Drift 精确 arXiv HTML 与作者 artifact 仍未返回
  可验证正文。该项继续 unscored `Unverified / Blocked`；没有产生
  Full Source Review、评分、owner 或 Books disposition，post-forward backlog cursor 可继续 W19。

### Discovery Expansion Queue

ReVSI 的 access blocker 已解除并完成 Full Source Review；继续逐项回放 HF W18 全页后恢复的 10 项中，
Step-Level Advantage Selection、Semi-DPO、Onchain Operating-Layer Controls、Visual Generation survey 与 Meta-CoT 已完成评分与 Full Source Review；
Compliance versus Sensibility 与 Zero-to-CAD 也已通过作者公开全文及相关 artifact 完成评分和 Full Source Review；
Edit-R1 已完成全文与 OpenReview date/source-family reconciliation，并移入 2025 backlog。此前阻塞的两项
已完成 primary-source 全文、评测边界、章节邻接与 disposition 审计：

| Candidate / Primary Source | v1 / Event Date | ROADMAP Position | Checkpoint Status |
|---|---:|---|---|
| FAMA / arXiv:2604.25135 | 2026-04-28 | Ch78 owner；Ch76 / Ch80 handoff | **27/30；Full Source Review Complete；No Change — Already Covered** |
| Terminal Task Synthesis via Skill Graphs / arXiv:2604.25727 | 2026-04-28 | Ch23 owner；Ch77 / Ch80 handoff | **28/30；Full Source Review Complete；provisional Refine — Experimental** |
| Diffusion Templates / arXiv:2604.24351 | 2026-04-27 | Ch55 owner；Ch26 / Ch45 handoff | **28/30；Full Source Review Complete；provisional Refine — Experimental** |
| Refinement via Regeneration / arXiv:2604.25636 | 2026-04-28 | Ch23 owner；Ch25 / Ch62 handoff | **27/30；Full Source Review Complete；provisional Refine — Experimental** |
| Mutual Forcing / arXiv:2604.25819 | 2026-04-28 | Ch25 owner；Ch38 / Ch40 handoff | **28/30；Full Source Review Complete；provisional Refine — Experimental** |
| Co-Director / arXiv:2604.24842 | 2026-04-27 | Ch77 owner；Ch76 / Ch78 / Ch62 handoff | **27/30；Full Source Review Complete；No Change — Already Covered** |

按 daily pages 而不是单一 weekly landing page 重放 2026-04-27～05-01 后，当前确认以下 families 的 v1
  落在 W18。前九个 scored rows 与 ViPO 已完成 Full Source Review；Safety Drift 已确认日期但因明确的
  primary-source blocker 保持未评分。5 月 2～3 日的无列表/访问边界也仍需闭合：

| Recovered In-window Candidate | Primary ID / First-public | Current Status |
|---|---:|---|
| Refinement via Regeneration | arXiv:2604.25636 / 2026-04-28 | **27/30；Full Source Review Complete；provisional Refine — Experimental** |
| Mutual Forcing | arXiv:2604.25819 / 2026-04-28 | **28/30；Full Source Review Complete；provisional Refine — Experimental** |
| Co-Director | arXiv:2604.24842 / 2026-04-27 | **27/30；Full Source Review Complete；No Change — Already Covered** |
| MAIC-UI | arXiv:2604.25806 / 2026-04-28 | **28/30；Full Source Review Complete；No Change — Already Covered / Ch77** |
| GoClick | arXiv:2604.23941 / 2026-04-27 | **28/30；Full Source Review Complete；provisional Refine — Experimental / Ch10** |
| AutoGUI-v2 | arXiv:2604.24441 / 2026-04-27 | **27/30；Full Source Review Complete；No Change — Already Covered / Ch62** |
| Unified 4D World Action Modeling / X-WAM | arXiv:2604.26694 / 2026-04-29 | **28/30；Full Source Review Complete；provisional Refine — Experimental / Ch10** |
| ExoActor | arXiv:2604.27711 / 2026-04-30 | **24/30；Full Source Review Complete；No Change — Already Covered / Ch10** |
| Representation Fréchet Loss | arXiv:2604.28190 / 2026-04-30 | **29/30；Full Source Review Complete；provisional Refine — Experimental / Ch62** |
| ViPO | arXiv:2604.24953 / 2026-04-29 | **27/30；Full Source Review Complete；provisional Refine — Experimental / Ch30** |
| Safety Drift After Fine-Tuning | arXiv:2604.24902 / 2026-04-27 | **Unverified / Blocked — primary text and author-artifact discovery denied by current browser permissions; unscored** |

另有 EmbodiedMidtrain、DiagramBank、IndustryAssetEQA 等 page hits 尚未完成 primary-date reconciliation，
先保留在 discovery queue，不计分、不做负面结论。OpenReview/TMLR、DBLP、Scholar/OpenAlex 与
official/infra fixed lists 仍需 date、source-family、revision 和 relevance reconciliation；在这些检查结束前，
候选总数和最终 review denominator 不能冻结。

Official Kubernetes W18 index 首轮恢复的四个 resource-management source families 已全部完成独立评分、
Full Source Review、章节邻接与 disposition；它们没有被合并成模糊的 “Kubernetes v1.36 resource update”。
Broader v1.36 index 的七个相邻条目也已完成 title/date/source-family 分流；它们均不属于 W18 新事件，
因此不进入本周 score denominator：

| Candidate / Primary Source | Publication / Release Date | Attribution |
|---|---:|---|
| Manifest-Based Admission Control | 2026-05-04 | W19 candidate；不是 W18 |
| Server-Side Sharded List and Watch | 2026-05-06 | W19 candidate；不是 W18 |
| Kubernetes v1.36 DRA updates | 2026-05-07 | W19 candidate；不是 W18 |
| PSI Metrics GA | 2026-05-12 | W20 candidate；不是 W18 |
| Workload-Aware Scheduling | 2026-05-13 | W20 candidate；不是 W18 |
| Gateway API v1.5 | release 2026-02-27；article 2026-04-21 | W09 release family / W17 publication node；不是 W18 |
| Agent Sandbox | 2026-03-20 | W12 candidate；不是 W18 |

Kubernetes W18 index 的日期窗口据此闭合；这不代表其他 model/research institution、framework release、
RFC/PR 与 AI Infra fixed lists 已闭合。

首批 model/research institution 与 Infra fixed-index 边界已按官方页面复核。下表只表示“在当前可见官方
索引中没有恢复新的 W18 family”或“已归入其他周”，不是对互联网全局缺席的证明：

| Fixed Source | Official index boundary | W18 disposition |
|---|---|---|
| OpenAI Research releases | 2026-04-23 后下一可见 release 为 2026-05-05 | 当前官方 release index snapshot 未恢复 W18 候选；该 source list 本轮边界已核对 |
| Google DeepMind News | 2026-04-27 Republic of Korea national partnership；相邻 W18 index 未发现新 technical report/model card | 15/30；独立低分 partnership fact，未与 Google Research 5 月 1 日 open-science 条目合并；没有新模型、训练、runtime 或 evaluation mechanism |
| Apple ML Research | ICLR 2026 collection 发布于 2026-04-22 | W17 publication node，不计 W18；其中论文仍按各自 first-public date 去重 |
| Meta AI Blog | 当前可见 official index 在 2026-04-08 Muse Spark / reliability posts 后下一 research item 为 2026-06-29 Brain2Qwerty | 当前 official blog snapshot 未恢复 W18 family；不外推为 Meta publications/GitHub 绝对缺席 |
| ByteDance Seed Blog | date-filtered official surface 的相邻 model item 为 2026-04-23 Seed3D 2.0，当前 visible index 未显示 W18 post | 4 月 23 日归 W17；W18 未恢复 official blog family；paper/repository surfaces 仍由 academic cross-index 去重，不能据空白关闭全机构 discovery |
| Ai2 News | 当前索引在 2026-04-13 与 2026-05-07 之间未显示 W18 news item | 当前 index snapshot 未恢复 W18 候选；不外推为其他 Ai2 artifact 绝对缺席 |
| Mistral News | 2026-04-27 Workflows，前一可见项 2026-03-23，后一可见项 2026-05-22 | Workflows 已新增评分并完成 Full Source Review |
| DeepSeek API Changelog | 2026-04-24 DeepSeek-V4 后下一可见更新为 2026-07-31 | W17 version node；W18 未恢复新 API update |
| Z.ai Research Blog | 2026-04-30 Scaling Pain of Coding Agent Serving | 已新增评分并完成 Full Source Review；GLM-5 release 属于 W07 source family |
| Microsoft Research publications / EuroSys | 2026-04-27 Concord formal-publication node；2026-04-30 agent-network red-team | agent-network red-team 已评分审计；Concord 18 页全文已审，但 2025 acceptance/PDF timestamp 与 2026 formal publication 的 first-public 关系未闭合，转入 2025 disputed backlog，不重复计分 |
| Amazon Science Blog | 2026-04-27 C3LLM official explanation；2026-04-29 privacy-training-data reproduction | privacy reproduction 已评分并完成 Full Source Review；C3LLM 全文已读，但 v1 为 2025-10-04，转入 2025 backlog |
| PyTorch Blog / Research | 2026-04-29 AutoSP；2026-04-30 LightSeek-SMG | AutoSP 已联读 Blog 与 arXiv v1 全文；LightSeek-SMG 已读官方完整 engineering report；两项均完成评分、章节邻接与 Full Source Review，repository surface 因访问权限未独立核验 |
| IBM Research / Granite | 2026-04-29 Granite 4.1 multi-model release | official announcement 已全文读取；Language、Vision、Speech AR/Plus/NAR、Guardian、Embedding 分别完成 24/30、24/30、26/30、26/30、27/30、26/30、27/30 Full Source Review，暂定 Ch24、Ch17、Ch5、Ch38、Ch40、Ch68、Ch72 refine；七个 mechanism-level source families 均已完成，且 Embedding 的 4 月 artifact 与 5 月论文证据边界保持分离 |
| Cohere Labs Research | 当前 research index 在 2026-03-03 后下一可见项为 2026-05-27 | 当前 index snapshot 未恢复 W18 research family；不外推为 Cohere 全部发布绝对缺席 |
| Kimi model evolution / Research | 当前官方 help evolution 显示 2026-04-20 Kimi K2.6，下一模型节点为 2026-07-16 Kimi K3 | K2.6 归 W17；当前 model-evolution surface 未恢复 W18 release。该 current help page 不是不可变历史索引，因此 Moonshot paper/repository surfaces 仍由 academic cross-index 去重 |
| Qwen Research / Qwen Code | 旧 Qwen Blog 已迁移到动态 `qwen.ai/research`，当前抓取不到可审计日期列表；Qwen Code official updates 在 2026-04-23 后下一项为 2026-05-07 | Code update surface 未恢复 W18 family；Research surface 不能以空动态页判定无发布，继续交由 arXiv/repository cross-index 闭合 |
| MiniMax model release notes / News | 当前官方 model release notes 只把 2026-04 记为 Music-2.6，前一 language-model 节点为 2026-03-18 M2.7、后一节点为 2026-06-01 M3；官方 News 页面当前不提供可审计的历史日期列表 | 当前 model-release surface 未恢复 W18 technical family；月份级 Music-2.6 不能被强行归入 W18，且不外推为 MiniMax research/paper artifacts 绝对缺席 |
| Baidu ERNIE Publications | 当前 official publication page 列出 ERNIE 4.5、PaddleOCR-VL、PaddleOCR-VL-1.5 与 ERNIE 5.0，但没有提供逐项发布日期；4 月 30 日 ERNIE-5.1 Preview 已由官方 Blog 单独核验 | Publication page 不产生新的 W18 event date；论文按 arXiv v1 去重，Preview 已作为 15/30 leaderboard fact 记录 |
| Tencent Hunyuan GitHub | 官方 org 当前显示 mutable “last updated” 排序，无法从当前页面重建 2026-04-27～05-03 的 repo creation/release history | `Open — Historical Repository Metadata Required`；不得把 8 月更新时间或 pinned repos 倒写为 W18 absence/presence |
| Huawei Noah's Ark Lab News | 官方 News index 的 2026 可见节点为 01-16、01-22、01-29、02-10，下一节点为 06-27 | 当前 official-news surface 未恢复 W18 family；论文仍按 academic primary metadata 去重 |
| Shanghai AI Laboratory News | 官方分页 index 在 2026-04-17 后下一批从 2026-05-06 开始 | 当前 official-news surface 未恢复 W18 family；dynamic research/open-source surfaces 仍由 repository/academic metadata 核验 |
| StepFun Research | 官方 Research index 当前请求超时；已知 W18 的 Step-Audio-R1.5 已通过 arXiv v1/v2、official repository 与 benchmark artifact 完成 Full Review | `Partially Closed`：已知 in-window family 已审，其他 official-post 历史需 repository/academic cross-index 补证，不能以 timeout 作无发布结论 |
| Xiaomi MiMo Research | 当前官方 paper index 在 2026-03-13 ARL-Tangram 后下一项为 2026-06-29 MOPD | 当前 paper surface 未恢复 W18 family；无日期 Blog cards 不用于历史归周 |
| InclusionAI Publications / Blog | official publication page 当前只列 2025 technical reports；可审计 Blog tag 在 2026-04-01 后下一相关节点为 2026-06-01 | 当前可见 official surfaces 未恢复 W18 family；GitHub/academic artifacts 仍按 first-public date 去重 |
| NVIDIA Dynamo tag | 2026-04-17 后下一可见条目为 2026-05-05 | 当前 tag snapshot 未恢复 W18 Dynamo family |
| NVIDIA Technical Blog | W18 TileGym 已保留；相邻可见 NCCL Inspector 为 2026-05-04 | TileGym 已审；NCCL Inspector 归 W19，不倒填 W18 |
| Hugging Face Blog | 2026-04-28 Nemotron 3 Nano Omni 已在 academic/model family 审计；2026-04-29 DeepInfra provider integration；2026-04-28 NVIDIA/Siemens Raw2Insights-US | Nemotron 已 Full Review；DeepInfra 19/30、Raw2Insights-US 17/30，均完成低分来源/拒绝核验。Community Articles 只作 discovery signal，不自动视为 Hugging Face 官方研究 |

Qwen Research、Tencent Hunyuan、StepFun 的历史 repository/post metadata、framework release、RFC/PR 与
academic cross-index 仍保持 Open；搜索结果空白不能代替 official index/date evidence。

下列页面命中经 primary metadata 核对后属于 earlier-week 或 2025 spillback，不重复计入 W18，也不把
Historical Forward Cursor 拉回：

| Candidate | Primary Source / First-public Date | Attribution |
|---|---|---|
| From Skills to Talent / OneManCompany | arXiv:2604.22446 / 2026-04-24 | W17 backlog |
| VLA Safety survey | arXiv:2604.23775 / 2026-04-26 | W17 backlog |
| SLIDERS | arXiv:2604.22294 / 2026-04-24 | W17 backlog |
| DIVERT | arXiv:2604.21480 / 2026-04-23 | W17 backlog |
| The Last Harness | arXiv:2604.21003 / 2026-04-22 | W17 backlog |
| ProEval | arXiv:2604.23099 / 2026-04-25 | W17 backlog |
| ElementsClaw / Agentic Fusion of Large Atomic and Language Models | arXiv:2604.23758 v1 / 2026-04-26；v2 / 2026-04-29；v3 / 2026-05-04 | W17 source family / W18 revision node；forward cursor 不回拉，待 W30 sweep 后按 W17 全文审计 |
| Agentic Safety Specifications / EPO-Safe | arXiv:2604.23210 / 2026-04-25 | W17 backlog |
| Seeing Isn't Believing | arXiv:2604.21523 / 2026-04-23 | W17 backlog |
| For-Value | arXiv:2508.10180 / 2025 | 2025 backlog; not a 2026 event |
| Edit-R1 / Verifier-Based RL in Image Editing | OpenReview hKWCGxuD5v / 2025-09-03; arXiv:2604.27505 v1 / 2026-04-30 | 2025 backlog; same Source Family, not a W18 event |
| C3LLM / How Catastrophic is Your LLM? | arXiv:2510.03969 v1 / 2025-10-04；Amazon official explanation / 2026-04-27 | 2025 backlog；W18 仅为 publication/explanation node，不重复计分 |
| Concord: Learning Network Configuration Contracts | author acceptance announcement / 2025-08；Microsoft PDF path / 2025-10；EuroSys/DOI formal publication / 2026-04-27 | first-public disputed；W18 只记 formal-publication node，移入 2025 backlog reconciliation，不重复计分 |

其余 HF 标题仍需逐项核对 v1 日期、source-family 和项目相关性；未核对项目不做负面结论。

### ERNIE-5.1-Preview LMArena announcement — 15/30

- **Source / Date / Verification**：Baidu ERNIE Blog 2026-04-30 官方一页公告已核对；它只报告
  ERNIE-5.1-Preview 在当期 LMArena Text Arena 的名次和若干 category ranking。没有 technical report、
  model/system card、checkpoint、training recipe、harness、sample count、vote distribution、confidence
  interval 或独立 evaluation。5 月 9 日 ERNIE 5.1 正式发布是 W19 事件，不用于反向解释 preview。
- **Score / Decision / Rejection**：15/30；`Weekly Only — Product/Leaderboard Fact; Mechanism Not
  Disclosed`。排名是时间、对手集合、匿名投票与 arena policy 的函数；在没有版本 identity 与评测合同
  的情况下，既不进入 Books，也不据此形成 architecture、training efficiency 或 Agent capability 结论。

### Empirical Research Assistance usage cases — 18/30

- **Source / Date / Verification**：Google Research 2026-04-29 官方项目案例已核对；可确认 workflow
  与公开 artifact 类型，不能确认通用科研生产率或自治程度。
- **Score / Decision / Rejection**：18/30 维持；`Weekly Only — Version/Product Fact`。没有独立
  evaluation contract、baseline 或可迁移系统机制，故不升级。

### Science partnerships / open resources — 16/30

- **Source / Date / Verification**：Google Research 2026-05-01 官方资源/合作条目已核对；属于项目
  与资源可用性事实。
- **Score / Decision / Rejection**：16/30 维持；`Weekly Only — Version/Product Fact`。合作规模
  和资源发布不等于 capability、artifact correctness 或 closed-loop science evidence。

### Google DeepMind–Republic of Korea national partnership — 15/30

- **Source / Date / Verification**：Google DeepMind 2026-04-27 官方公告全文已核对。可确认 AI Campus、
  National Partnerships for AI、K-Moonshot collaboration，以及 AlphaEvolve、AlphaGenome、AlphaFold、
  AI co-scientist 与 WeatherNext 的 planned access/collaboration surface；这些都是合作与资源可用性事实，
  不是本周新模型、训练、Serving 或评测机制。
- **Score / Decision / Rejection**：15/30（TN 1 / SI 2 / PV 2 / SR 5 / PR 2 / L 3）；`Weekly Only —
  Partnership Fact / No New Mechanism`。计划中的 collaboration、人才与安全合作不证明 deployment adoption、
  scientific productivity、artifact correctness 或任何已有模型的新增 capability，因此不进入 Books，也不与
  Google Research 5 月 1 日 open-science Source Family 合并。

### DeepInfra on Hugging Face Inference Providers — 19/30

- **Source / Date / Verification**：Hugging Face 官方 Blog 2026-04-29 条目已全文核对。它明确公开
  DeepInfra 成为 Inference Provider、BYOK 直连与 HF-routed 两种 billing/auth path、provider preference、
  model-page discovery，以及 Python `huggingface_hub>=1.11.2` / JavaScript SDK integration；没有公开
  router selection algorithm、health/failover contract、provider SLO、benchmark、incident data 或历史 API
  snapshot。
- **Score / Decision / Rejection**：19/30（TN 1 / SI 3 / PV 4 / SR 5 / PR 4 / L 2）；`Weekly Only —
  Provider Integration / No New Routing Mechanism`。它证明 provider 已接入和 authority/billing path 的版本事实，
  不证明质量、成本、freshness、fallback 或 SLO-aware routing 有新机制；现有 Ch58 已覆盖 provider selection
  与 evidence identity，故不进入 Books。

### NVIDIA/Siemens NV-Raw2Insights-US — 17/30

- **Source / Date / Verification**：Hugging Face 上由 NVIDIA 与 Siemens Healthineers 研究人员发布的
  2026-04-28 article 已核对；它描述从 ultrasound raw channel data 学习 reconstruction/insight，而不是只消费
  beamformed image，并链接 model/dataset artifact 与 Holoscan deployment context。官方页面同时明确该技术
  仍处 investigational development、尚未获美国销售许可。当前访问 model card 遇到 429，且没有恢复完整
  training set、hardware、clinical protocol、matched baseline、subgroup/safety evaluation、latency SLO 或
  regulatory validation，因此 Access Status 为 `Primary Article Verified; Model Card Temporarily Unavailable`。
- **Score / Decision / Rejection**：17/30（TN 3 / SI 3 / PV 2 / SR 4 / PR 2 / L 3）；`Weekly Only —
  Investigational Domain Prototype / Evidence Incomplete`。它能支持“在重建前保留 raw-signal information”这一
  受限 domain direction，不能证明临床有效性、跨设备泛化或通用 multimodal-system 机制；primary artifact
  未完整可访问且项目相关性有限，故不升级为 `20+`，不进入 Books。

## Repository Changes

- 2026-08-13 重新逐行复算 86 个评分 family：63 high、17 mid、6 low，80/80 当前 scored `20+`
  Full Source Reviews 完成；ViPO blocker 已恢复，Safety Drift 为唯一不进入分母的 blocked identity，普通 pending
  为 0。该检查点只确认账目和 blocked-skip 边界，不把受限来源升级为已读，也不修改 Books。
- W18 从 2 个低分 baseline 扩展为 33 个 scored families；原有 21 个 `20+` academic families 的
  Full Source Review 保留有效，system-integrated speculative rollout 完成论文、NeMo RL v0.6 artifact、
  evaluation contract 与 Ch29/44 邻接审计；KServe stable 完成 official release/blog/CRD/control-plane
  联合审计；Agent-Native Research Artifacts 完成 protocol、compiler/manager/seal、三组 evaluation、
  limitations、appendices、当前 artifact repository 与 Ch77/80 邻接审计；tabular retrieval stability 完成
  v1 全文、v2 revision boundary、author code/data/checkpoint path 与 Ch71～73 邻接审计，completed 达到
  25/29；DataPRM 完成 v1 全文、v2 revision boundary、当前 DataMind artifact、完整 evaluation/cost/
  limitation 与 Ch29/61～63/77 邻接审计，completed 达到 26/29；GLM-5V-Turbo 完成 v1、v3 revision
  boundary、official API/GLM-V/ImageMining/Skills artifacts 与 Ch33～39、44、62、71/73 邻接审计，
  owner 从 Ch21/38 修正为 Ch34，completed 达到 27/29；Synthetic Computers 完成 v1/PDF、retrospective
  Appendix、Microsoft Research publication、官方 dataset schema/artifacts 与 Ch23/62/71/73/76～78/80
  邻接审计，确认 environment-first synthesis 与 evolving artifact graph 的长期机制，也保留 1,000-run paper
  和 current 98-computer artifact、同源 rubric/judge 之间的证据边界，completed 达到 28/29。HF W18 二次
  回放新确认的 7 个 in-window academic candidates 中 Step-Audio-R1.5 最后完成 v1/v2、official repo、
  三套 benchmark schema/prompt/scorer 与 Ch27～30/38/62 邻接审计；由于 text-only output + S2T evaluation
  无法测量报告宣称的 prosody/naturalness，且缺 RLHF ablation/training contract，结论为 No Change / claim–
  evidence mismatch，当时 current retained set 的 29/29 reviews 全部完成。扩展扫描又确认 World-R1、Tuna-2、
  ReVSI、Turning TIDE、computer-use step-level optimization、
  InteractWeb-Bench 与 FlashRT 共 9 项 v1 属于本周。World-R1 已完成 26/30 评分、v1/v4、官方 code/dataset、
  Flow-GRPO/reward-service/data-phase/evaluation contract 与 Ch28～30/61～63 邻接审计。Tuna-2 也完成
  v1/v2、project page、当前官方 code、pixel-space architecture、mask/data-mixture/evaluation contract 与
  Ch4～6/23～24 邻接审计；由于 v1/v2 data ratio 冲突、v1 HTML temporal anomaly、production weights
  未开放且 current code 并非 paper-run frozen recipe，维持 Disputed Revision Integrity / Experimental。
  Conversational User Simulation survey 又完成 v1 全文、Who/What/How taxonomy、evaluation、limitations、
  ethics 与 Ch61～63/71～74/77 邻接审计；23/30，因现有 Ch62 已拥有 population/subject/simulator/scorer/
  calibration contract，Ch71/73 已拥有 history/memory/drift/provenance，结论为 No Change / Already Covered。
  Perceval 又完成 CVPR/arXiv v1、official repository/checkpoints、token-span advantage、truncate/regenerate、
  evaluation/sensitivity 与 Ch28～30/62 邻接审计；26/30，暂定 Ch29 Experimental refine。其 PRM 未做独立
  span calibration，且 self-reported hallucination plateau 不能证明没有 reward hacking。Turning TIDE 再完成
  arXiv v1 全文/Appendix、official code/model/data、TIDAL/CompDemo/Reverse CALM 两条 pipeline、完整训练/
  evaluation contract 与 Ch24～26/30/40 邻接审计；26/30，暂定 Ch25 Experimental refine。它只支持两个
  teacher pipeline 下的受限 viability，不能用 aggregate 或 HumanEval 单项把 dLLM 外推为普遍优于 AR；
  single-H100 受控表中同尺寸 AR 反而更快。Step-level Optimization 又完成 14-page PDF/HTML、完整 prompts、
  StepWise detector weights、event-driven route/verification、evaluation 与 Ch57～59/61～63/76～80 邻接审计；
  28/30，暂定 Ch77 Experimental refine。作者只公开单阈值 next-step route，未公开所称 hysteresis/bounded
  recovery 实现；300 trajectories 的 overlapping-window split 也可能泄漏。InteractWeb-Bench 又完成 v1
  HTML/PDF、全部 prompts、project/repository/data、synthetic persona/user/judge contract 与 Ch61～63/73～77
  邻接审计；25/30，因 Ch62 已覆盖 feedback-conditioned policy、hidden-answer judge、turn budget、artifact/
  trace 与 human/executable calibration，结论为 No Change / Already Covered。其 synthetic user 持有完整
  golden requirement，主要 TCR/IAS/CHR 又依赖 GPT-5-mini judge，anti-hallucination 还未计入 TCR，不能外推
  真实用户或生产网站质量。FlashRT 最后完成 v1 全文/Appendix、current author code、white/black-box
  attack contracts、selective recomputation、context-subsampled gradient、sensitivity 与 Ch22/49～51/67～69
  邻接审计；28/30，暂定 Ch68 Experimental refine。其 measured time/memory/ASR 只对四 H100、BF16、
  white-box target-output、指定 datasets/models/settings 成立，近似 policy 也必须进入 evidence identity，不能
  当作通用 Serving KV 优化。ReVSI 随后完成 v1/v2 metadata、全文/Appendix、ICML/OpenReview record、official
  repository/project/dataset 与 Ch61～63 邻接审计；28/30，暂定 Ch62 Experimental refine。其长期机制是
  observation-conditioned answerability 与 evidence-removal counterfactual，不能把作者 ranking reversal
  外推为通用 3D reasoning 能力。current scored retained set 因而达到 38/38；继续逐项回放 HF 全页后又
  恢复 Visual Generation survey、Verifier-Based RL、Meta-CoT、FAMA、terminal task synthesis、reasoning
  controllability、Zero-to-CAD、step-level advantage selection、onchain agent controls 与 Semi-DPO 共
  10 项确认在窗 families；其中 Step-Level Advantage Selection 已完成 28/30 Full Source Review，暂定
  Ch29 Experimental refine；Semi-DPO 已完成 ICLR full text、Appendix 6.1～6.11、project page、current
  missing-code surface 与 Ch29～31 邻接审计，27/30，暂定 Ch30 Experimental refine。Onchain
  Operating-Layer Controls 随后完成唯一 v1 全文、全部表图/Limitations/Appendix prompt template、官方
  AgentVault/Core Contracts/whitepaper/Terms 与 Ch79～80 邻接审计，28/30，暂定 Ch80 Experimental refine，
  Ch68/77 handoff；其 99.9% settlement 条件率不等于 rejection-inclusive mandate success 或收益。
  Visual Generation survey 随后完成 v1 全文、v2 revision metadata、作者 living-roadmap artifact 与
  Ch61～63/Ch9～10/Ch38 邻接审计，24/30；它只支持 perceptual、structural、temporal、agentic 与 causal
  evidence 必须分层，闭源 frontier architecture 与 silent verifier loop 均是作者明确标注的猜想，不能写成
  产品事实。Ch62 与 Ch10 已覆盖 task-specific verifier、executable evidence 和 action-faithfulness，故为
  `No Change — Already Covered`。Edit-R1 又完成 arXiv v1 全文、公式/实验/appendices 与 OpenReview
  first-public/source-family reconciliation；同一九位作者和同一 principle decomposition/GCPO/RRM-guided
  GRPO 机制已于 2025-09-03 公开，因此转入 2025 backlog，不计 W18 score。Meta-CoT 随后完成唯一 v1
  主文、公式/算法、训练/评估合同、公开 artifact surface 与 Ch25/27～30/62 邻接审计；26/30，暂定
  Ch29 Experimental refine，Ch25/62 short handoff。其 task/meta-task/target planning、CEC reward、early-
  timestep Flow-GRPO 与冻结 understanding expert 构成机制增量；但五类 primitive 的 basis/entropy 主张
  只在未能独立读取的 supplement 中展开，训练与评估又高度依赖闭源 model judges，不能外推为通用
  编辑本体或可靠 reasoning。Kubernetes controller staleness mitigation 随后完成 official design、
  client-go v0.36.0 cache API 与 Ch53/54/63 邻接审计；27/30，暂定 Ch53 Version-Grounded refine。
  它证明四类 built-in controllers 的 read-your-writes guard 与观测 API，不证明全局线性一致或任意
  custom controller 已获得保护。Suspended Job mutable resources 又完成 official blog、Jobs concept、
  feature-gate/API reference 与 Ch56/59/60 邻接审计；28/30，暂定 Ch56 Version-Grounded refine。它支持
  execution 前的受控 resource negotiation 与 resume freeze，不证明减少 GPU 后训练拓扑、收敛、成本或
  fairness 仍正确。Tiered Memory QoS 又完成 feature Blog、QoS/resource/cgroup v2 与 kernel docs、
  Ch59/63/67 邻接审计；27/30，暂定 Ch67 Alpha/Version-Grounded refine。它把 request 映射为
  hard/soft protection 并把 throttling 与 reservation 解耦，但没有 workload benchmark，不能声称减少
  OOM、提高 utilization 或改善 latency。In-place Pod-level scaling 又完成 feature Blog、resize task/status
  docs 与 Ch53/56/59 邻接审计；28/30，暂定 Ch53 Version-Grounded refine。它把 resource intent、
  node-admitted allocation 与 applied cgroup state 显式分层，但不证明推荐正确、无中断或优于 recreate。
  Pod-Level Resource Managers 随后完成 feature Blog、resource-manager/feature-gate 文档与
  Ch53/56/59 邻接审计；28/30，暂定 Ch59 Alpha/Version-Grounded refine。它把 Pod-level aggregate
  budget 分解为 exclusive slices 与 shared remainder，并明确 pod/container Topology Manager scope、
  CFS enforcement、persistent pool 和 checkpoint rollback contract；没有 workload benchmark，不能声称
  改善 ML throughput、tail latency 或 utilization。Microsoft Research multi-agent network red-team 又完成
  official report、四类 network-only attack、qualitative emergent defense、mitigation/evidence boundary 与
  Ch68/78/80 邻接审计；28/30，暂定 Ch78 Experimental refine。它证明这些 failure modes 在指定内部
  platform 出现，不提供普遍 attack rate、model ranking 或已验证 defense effectiveness。NVIDIA TileGym
  cross-DSL kernel translation 随后完成 official Blog、Python/Julia semantic mapping、17-rule
  skill、static validator、CPU-reference tests、reported-run contract 与 Ch45/77 邻接审计；24/30，因 Ch77
  已完整覆盖 typed contract、deterministic check、artifact/version lineage 与 human approval，最终为
  `No Change — Already Covered`。repository 访问受限，4-minute/78K-token 单次 GEMM 结果也不支持通用
  productivity/correctness 外推。固定机构扫描随后恢复 xAI Custom Voices 与 ERNIE-5.1 Preview：前者
  完成 announcement、当前 API docs、两阶段 enrollment、team-scoped artifact lifecycle、证据边界与
  Ch67～69 邻接审计，24/30，暂定 Ch68 Version-Grounded refine；后者只有 4 月 30 日 leaderboard
  announcement，15/30，保留为 Product/Leaderboard Fact，不借 5 月正式发布材料倒填机制。current
  scored set 当时为 54 项，retained set 达到 51/51。Compliance versus Sensibility 随后完成作者公开全文、
  reasoning-conflict design、probe/CAA intervention、judge validation、hardware/seed contract 与
  Ch16～18/27～28/62 邻接审计；26/30，暂定 Ch17 Experimental refine。它支持受限任务中的可探测和
  可干预倾向，不证明 deliberate choice、通用 instruction hierarchy control 或无代价 compliance。
  Zero-to-CAD 又完成作者公开全文、OpenReview/官方 dataset、distributed synthesis、三层 validation、
  bootstrapping evaluation、完整训练配置与 Ch22～24/61～63/76～78 邻接审计；28/30，暂定 Ch23
  Experimental refine。它证明在作者 verifier ontology 下可规模化产生 executable CAD programs，并支持
  受限 synthetic-to-program bootstrapping；不证明 DFM、真实设计意图、matched dataset superiority 或
  无偏 synthetic provenance。当时 current scored set 因而为 56 项，retained set 达到 53/53；FAMA 与
  Terminal Task Synthesis 在该中间检查点尚受访问限制，现已于后续检查点完成全文审计并撤销 blocker。
  W18 的 5 个 Kubernetes families 已审，7 个相邻 index 条目也已跨周分流；其他
  official/infra discovery 与 fixed-source reconciliation 未闭合。随后 fixed-source reconciliation 从
  Mistral 官方索引恢复 2026-04-27 Workflows public preview，并联合当前官方 workflow/activity/event/
  deployment/security docs 与 Ch76～80 完成 Full Source Review；28/30，`No Change — Already Covered` /
  Ch77。Z.ai 官方固定源又恢复 4 月 30 日 Scaling Pain incident report，并完成 PD abort/RDMA completion/
  KV reuse、HiCache read-before-ready、speculative anomaly telemetry、LayerSplit、evaluation contract 与
  Ch19/44/50～52/63 邻接审计；29/30，暂定 Ch51 Version-Grounded refine。两项使 current scored set
  达到 58 项、`20+` retained set 达到 55/55；同时完成 OpenAI、Apple、Ai2、DeepSeek 与 NVIDIA 首批
  官方索引边界对账，但其余具名机构、framework/RFC/PR 与 cross-index 仍未闭合。
  其余标题继续 date/dedup reconciliation。DV-World 的
  temporal-integrity 冲突保留为 disputed，不将 current HTML leaderboard 倒写到 W18。TCOD 按 4 月 27 日
  v1 从 W17 curation feed 归回本周；
  又将 W19 feed 的 5 项与 W20 feed 的 RouteProfile 按 v1 日期回拨。
  早于本周的 spillbacks 登记到 backlog，不回拉 forward cursor。无历史 Daily 或 Books 修改。

  Amazon Science fixed-source reconciliation 随后恢复 2026-04-29 privacy-training-data reproduction，完成
  全文、六个 related-primary entry points、三类 disclosure surfaces、DP/MPC layered defense、实验条件缺口
  与 Ch63/67～69 邻接审计；24/30，因 Ch68 已具体覆盖 privacy unit、DP production contract 与 aggregate
  trust boundary，最终为 `No Change — Already Covered`。同一索引的 C3LLM official explanation 也已联读
  arXiv v3 20 页全文和 revision history；v1 为 2025-10-04，故作为 2025 source-family backlog / W18
  publication node，不重复计分。PyTorch fixed-source pass 随后恢复 AutoSP 与 LightSeek-SMG：AutoSP 已
  完成 arXiv v1 全文、Torch-IR/FX rewrite、sequence-aware min-cut checkpoint、完整 evaluation/ablation 与
  Ch22/24/32～36 邻接审计，28/30，暂定 Ch33 Experimental refine；LightSeek-SMG 已完成官方全文、
  CPU/GPU state ownership、gRPC/tokenizer-cache/routing、benchmark contract 与 Ch38/46/49/52/58/67/80
  邻接审计，27/30，暂定 Ch38 Experimental refine。两项都没有在 Historical Books Gate 关闭时修改
  Books。完成 Granite partition 时，W18 为 68 scored families，49 high / 16 mid / 3 low，65/65 `20+`
  Full Source Reviews；随后完成 FAMA 与 Terminal Task Synthesis 后账目增至 70 scored families；Google
  DeepMind Korea partnership 独立拆分为低分 Source Family 后，该中间检查点为 71 scored families，51 high /
  16 mid / 4 low，67/67 `20+` Full Source Reviews。其他 discovery surface 仍使 Gate 保持 Open。继续扫描 IBM
  Research 后又恢复 4 月 29 日 Granite 4.1 official release；announcement 已全文读取，Language、Vision、
  Guardian、Embedding 与进一步拆为 AR/Plus/NAR 的 Speech 共形成 7 个 mechanism-level source families。
  Language 已完成 official
  technical article、3B/8B/30B cards、8B config/commit history、training/evaluation 与章节邻接审计，
  24/30，暂定 Ch24 Version-Grounded refine；512K training exposure 与 131,072 released artifact contract
  已明确拆分。Vision 也已完成 card/config/history、ChartNet v1/dataset、feature-injection、training/evaluation
  与 Ch14～18/23/45/62 邻接审计，24/30，暂定 Ch17 Experimental refine；current ChartNet 4.2M 与
  5～6 月 subsets 未被倒写为 launch training manifest。Speech NAR 随后完成 NLE v1 全文、current card、
  CTC draft→interleaved slots→bidirectional editor→CTC collapse 控制流、matched AR/CTC evaluation、
  ablations、multi-step failure、runtime constraints 与 Ch38～41/44/62 邻接审计；27/30，暂定 Ch40
  Experimental refine。论文 NLE/NLE++ 与 current artifact 的 70K/130K-hour data、projector、LoRA、epoch
  和 batch contract 已明确分离。Speech AR 随后完成 current 4.1 card、2025 predecessor architecture paper、
  W11 Self-Speculative paper、174K-hour data/task schema、dual-head/importance pooling/modality adapter、
  evaluation/safety/runtime boundary 与 Ch5/17/38～40/44/62 邻接审计；26/30，暂定 Ch5 Experimental refine。
  4.1 artifact 与 earlier paper runs 未混写，relaxed self-spec verification 也明确不是 exact sampling。
  Speech Plus 随后完成 current 2B card、SAA 与 In-Sync 两篇 8B related paper 全文审计；structured
  speaker/time grammar、session/prefix/client state、synthetic data lineage、ablation 与 malformed-output
  accounting 均已核对，26/30，暂定 Ch38 Experimental refine。三套 artifact/paper contracts 未混写，
  incremental decode 也未被外推为 bounded-compute streaming。Guardian 随后完成 current card/docs、
  2024 predecessor paper、risk/policy prompt grammar、score formula、data lineage、OOD/BYOC/function/RAG/
  JETTS evaluation 与 Ch62/68/69/77 邻接审计；26/30，暂定 Ch68 Version-Grounded refine。4.1 claims 与
  前代机制已拆分，thinking trace、yes/no score 与 vendor benchmark 均未升级为 calibrated safety guarantee。
  Embedding 最后完成 current 97M card、W20 later-public paper、pruning/vocabulary/multi-teacher KD、完整
  retrieval/speed/context/dependency evaluation 与 Ch22/45/62/71～73 邻接审计；27/30，暂定 Ch72
  Version-Grounded refine。April artifact 与 May paper 没有混写，Transformers 版本引起的 throughput
  regression 被保留为 runtime contract evidence。至此 Granite 七个 mechanism families 全部审完。
  Microsoft Research/EuroSys cross-index 又恢复 Concord。18 页论文、proceedings、DBLP、DOI/ORCID 与
  author publication/news surfaces 已联读，机制、state ownership、CI control flow、production datasets、
  coverage/precision sampling、incident replay 和 semantic-guarantee boundary 已完成非模板化审计。由于
  2025-08 acceptance announcement、`2025/10` PDF path 与 2026-04-27 formal publication 无法证明唯一
  first-public date，该 Source Family 转入 `2025 Backlog — Disputed First-public`，W18 只保留 formal-
  publication node，不增加 score row。此发现闭合 Microsoft Research fixed-source 的一个缺口。
  固定来源继续复核后，Kimi 官方 evolution 将 K2.6 归回 W17，MiniMax 官方 model notes 无法把月份级
  Music-2.6 强行归入 W18；Hugging Face Blog 则补回 DeepInfra provider integration（19/30）和
  NVIDIA/Siemens Raw2Insights-US（17/30）两个低分 source families。两项均完成来源、日期、评分与拒绝
  边界核验，没有新增 `20+` Full Review 分母。当前 W18 因而为 73 scored families（51 high / 16 mid /
  6 low），67/67 `20+` Full Source Reviews；Gate 仍因 Qwen、StepFun、其他机构、framework/RFC/PR 与
  academic cross-index 未闭合而保持 Open。

  framework release pass 随后恢复 vLLM v0.20.0 与 Transformers v5.7.0。vLLM release、Model Runner V2
  stale-slot correctness PR、LMCache `cache_salt` isolation PR、vLLM IR/FA4 PR、HMA/offload/NIXL 与 breaking
  dependency contract 已联读；29/30，暂定 Ch46 Version-Grounded refine。Transformers release、长生成
  PR #45530、tag-pinned Continuous Batching API/architecture docs 已联读；26/30，暂定 Ch42 Version-Grounded
  refine。两项都明确区分 release facts、受限 PR tests 与未披露 production SLO；独立页面不可访问的
  vLLM TransferTopology/Mamba PD PR 与 Transformers CPU-offload PR 只采用 release/tag docs，不补写实现。
  SGLang v0.5.10 按 4 月 6 日归 W15。W18 账目更新为 75 scored families（53 high / 16 mid / 6 low），
  69/69 `20+` Full Source Reviews；其他 fixed-source 与 academic cross-index 尚未闭合，因此 Gate 仍 Open。

- 逐日重放 Hugging Face 2026-04-27～05-01 pages 后，先前的“当前无已知在窗 academic pending”判断被
  撤回。Diffusion Templates 已完成唯一 v1 全文、template cache/model/pipeline/training、11 类 model-zoo、
  evidence/limitation boundary 与 Ch54～56 邻接审计；28/30，暂定 Ch55 Experimental refine，Ch26/45
  short handoff。其 `1.8x` editing speedup 缺硬件、dtype、resolution、并发和 SLO contract，未被外推。
  Refinement via Regeneration 随后完成唯一 v1、官方 current code/model artifact、全部 experiments/ablations
  与 Ch22～24 邻接审计；27/30，暂定 Ch23 Experimental refine，Ch25/62 handoff。作者 alignment 分数只绑定
  BAGEL、H800、特定训练 mix 与 50-step CFG contract；Gemini-family generator/labeler/judge 的同源偏差、
  identity/locality、多轮 termination 和 matched-compute 边界保持未证明。W18 当前更新为 77 scored families
  （55 high / 16 mid / 6 low），71/71 当前 `20+` Full Source Reviews。Mutual Forcing 又完成唯一 v1、全部
  method/experiments/appendices、official project、demo-only current repository 与 Ch24～26 邻接审计；28/30，
  暂定 Ch25 Experimental refine，Ch38/40 handoff。4/8 NFE、25 秒与 FPS 结果只保留为作者 workload fact，
  没有 GPU/dtype/batch/variance/production-SLO 时不外推；“teacher-free”也明确限定为没有外部 bidirectional
  teacher，不能忽略 online fake-model state。W18 当前更新为 78 scored families（56 high / 16 mid / 6 low），
  72/72 当前 `20+` Full Source Reviews。Co-Director 又完成唯一 v1、全部 method/evaluation/appendices/prompts、
  current official code 与 Ch62/76～78 邻接审计；27/30，`No Change — Already Covered` / Ch77。T=4 MAB
  只保留作者 workflow evidence；factored reward 是 Gemini judge attribution，且 prompt 强制其与 execution
  quality 同向，不能写成已解决 causal credit assignment。W18 当前更新为 79 scored families（57 high / 16 mid /
  6 low），73/73 当前 `20+` Full Source Reviews。MAIC-UI 随后完成唯一 v1、全部 method/evaluation/
  appendices、current official implementation 与 Ch62/76～78 邻接审计；28/30，`No Change — Already
  Covered` / Ch77。它支持 human-selected element scope + diff-first patch 的可实现性，但 full-system lab
  comparison 没有隔离三个组件的贡献，单校 observational classroom deployment 也不能支持因果学习收益。
  W18 当前更新为 80 scored families（58 high / 16 mid / 6 low），74/74 当前 `20+` Full Source Reviews；
  GoClick 随后完成唯一 v1、全部 method/evaluation/limitations、current official repository/model/data/eval
  surfaces 与 Ch10/23/62/74～78 邻接审计；28/30，暂定 Ch10 Experimental refine，Ch23/62/75/78 handoff。
  论文只在 L20、batch 1、BF16、offline trajectories 上模拟端侧/Agent path，不能外推真实 device SLO 或 online
  task success。W18 当前更新为 81 scored families（59 high / 16 mid / 6 low），75/75 当前 `20+` Full Source
  Reviews。AutoGUI-v2 随后完成唯一 v1、51 页主文/Appendix、current official repository、公开 dataset
  surfaces 与 Ch61～63/75/77 邻接审计；27/30，`No Change — Already Covered` / Ch62。它证明 static
  functionality/hard-negative suite 能分离 appearance、intent、function 与 single-step outcome，却不执行真实
  action，也不证明 multi-step planning、environment transition 或 Agent task success。W18 当前更新为 82
  scored families（60 high / 16 mid / 6 low），76/76 当前 `20+` Full Source Reviews。X-WAM 随后完成 v1
  全文/Appendix、项目页、current later-release code/checkpoint/data boundary、evaluation contract 与
  Ch9～10/20/38/62 邻接审计；28/30，暂定 Ch10 Experimental refine。ANS 支持“不同模态 deadline 应匹配
  不同 completion schedule”，但不证明 predicted video/depth 的 causal correctness，也不证明统一模型普遍优于
  专用 policy + world model；6 月 9 日才公开的 implementation 不能倒写成 W18 同步 artifact。W18 当前更新为
  83 scored families（61 high / 16 mid / 6 low），77/77 当前 `20+` Full Source Reviews。ExoActor 随后完成
  唯一 v1、全部 case/failure/ablation/latency/discussion 与 Appendix prompts、项目页及 404 code boundary、
  Ch9～10/38/62/75/77 邻接审计；24/30，`No Change — Already Covered` / Ch10。它支持 generated video→
  motion estimate→controller 的 representation handoff 与 error amplification，但没有任务/trial denominator、
  success rate、uncertainty、完整 latency contract 或可复现 artifact，不能证明普遍 zero-shot humanoid control。
  W18 当前更新为 84 scored families（61 high / 17 mid / 6 low），78/78 当前 `20+` Full Source Reviews；
  Representation Fréchet Loss 随后完成唯一 v1 全文、全部 Appendix、current official repository surface、
  population estimator、evaluation contract 与 Ch23～25/62 邻接审计；29/30，暂定 Ch62 Experimental refine，
  Ch23/24 handoff。论文支持 population-estimation window 与 gradient window 解耦，也直接暴露 scorer-as-loss、
  stale Queue/EMA state 与同源 representation gaming；没有 GPU/拓扑/时间成本，不能外推 one-step 或 FD-SIM 的
  通用优势。W18 当前更新为 85 scored families（62 high / 17 mid / 6 low），79/79 当前 `20+` Full Source
  Reviews；该段是 ViPO 恢复前的过程快照：ViPO 与 Safety Drift 当时都因正文与作者 artifact 不可读而标记
  `Unverified / Blocked`。ViPO 已于 2026-08-13 恢复并计入当前 86-row ledger；Safety Drift 仍未评分且未
  伪装成 Full Review。ElementsClaw 的 v1 为 4 月 26 日，v2 才是 4 月 29 日，故转入 W17 backlog，
  W18 只记 revision node。How Much Is One Recurrence Worth 的 v1 为
  4 月 22 日、v2 才是 4 月 27 日，连同另外十项 earlier hits 只进入 W16/W17 backlog，不重复计分。
  用户随后明确授权将两项暂记 blocked 后跳过：W18 forward sweep cursor 因而移动到 W19，但 W18 Historical
  Evidence Gate 与 Historical Books Gate 仍保持关闭，未修改 Books；两项进入 post-forward backlog。

## Open Questions

1. Science Agent 的有效 artifact 应包含哪些 provenance、code、data 与 human-review 状态？
2. RecursiveMAS 的 hidden-state transport 在跨机 topology 下是否仍优于 text serialization，谁拥有
   link/backbone compatibility 与 invalidation？
3. BARRED 的同源 generator/debate 误差、LenVM 的额外 forward latency、CoPD 的 K-branch resource
   amplification 能否获得独立 reproduction 与 production-scale evidence？
4. reasoning-schema steering 能否公开 intervention artifact、跨模型因果复现与 compliance/task-quality
   Pareto frontier，而不把线性可读出误写成充分因果机制？
5. Zero-to-CAD 的 accepted programs 能否由独立工程师验证可编辑性、DFM 与真实意图，并提供包含失败
   trajectories、validator version 和 provenance 的 immutable dataset manifest？
4. Step-Audio-R1.5 所宣称的 spoken-dialogue naturalness 能否由未来开放的 R1.5 checkpoint、speech-output
   human pairs 与 controlled RLVR/RLHF ablation 核验？system-integrated speculative rollout 的 draft/policy checkpoint
   rollback 与 multi-turn tool workload 是否会暴露新的不一致？Agent-Native artifact 的 schema
   migration、sandbox、granular access control 与 independent review 如何从原型契约升级为长期平台能力？
5. HF expansion queue、OpenReview/TMLR、DBLP、Scholar/OpenAlex 与其余 official/infra fixed list
   还会恢复哪些遗漏或 earlier-week spillback？
6. MAIC-UI 的 event-time frozen implementation、component ablation、跨模型/页面长度 latency contract、
   multi-page patch drift 与独立课堂复现，能否把 current case 从可实现机制提升为可外推 evidence？
7. GoClick 能否提供 event-time immutable code/data/run manifest、真实 mobile/NPU 的 latency-memory-energy-thermal、
   online task success/recovery、multi-seed PDR、matched-parameter architecture ablation、legacy/current GUI slices 与
   semantic-handoff calibration/abstention，从而把 L20 offline evidence 提升为端侧系统证据？
8. ReVSI 的 independent annotation audit、agreement/confidence、matched frame/token/compute evaluation 与
   dummy-input OOD calibration 能否验证 observation-conditioned answerability 的稳定性？World-R1 的
   reward/evaluation shared ontology 能否由独立 scorer 和
   compute-matched training/serving comparison 进一步校准？Tuna-2 的 immutable v1 snapshot、paper-run
   recipe/weights 与 matched-compute comparison 能否解决 revision-integrity 和 architecture-attribution 边界？
8. ReVSI 的 frame indices、visibility annotation 与 QA 如何在 processor、sampling 或 source-scene revision
   变化时做 invalidation、migration 与 frozen-suite replay？current repository/dataset 没有 event-time frozen
   tag，仍需 immutable artifact 和独立复现。
9. Turning TIDE 的 aggregate gain 能否在多 seed、matched total teacher compute 与长上下文下重现？byte-level
   chunk alignment 在 Unicode normalization、长 chunk 与 template drift 下的错误率，以及 Reverse CALM 的
   diversity loss，仍需独立测量。
10. Step-level controller 的 threshold、hysteresis、cooldown 与 recovery budget 能否公开为可重放 policy？
   overlapping windows 若按 trajectory-grouped split、human-gold labels 和跨 policy/domain transfer 重测，
   detector calibration 与 cost/success frontier 是否仍成立？
10. FAMA 若按 task/profile/source family 做严格 held-out split，并用 human-gold failure attribution、包含
    首次失败的端到端成本与有副作用工具的补偿语义重测，failure-conditioned helper selection 是否仍稳定？
    Terminal Task Synthesis 能否公开 immutable graph/task/trajectory manifests、LLM bridge precision、
    instruction-test mismatch denominator，并解释 118,806-node giant component 与 82,073 scenario nodes 的
    counting semantics？在这些问题解决前，后者保持 `Experimental`，不把作者 benchmark 外推为通用结论。
11. Semi-DPO 的五-scorer consensus 能否通过 committee-out human audit 验证？若把 3,992-pair controller
    set 与真正 held-out evaluation 分离，或改变 scorer/teacher revision、timestep bins 与 thresholds，
    pseudo-label accuracy、derived-label stability 与 claimed GPU-hour frontier 是否仍成立？
12. Onchain Operating-Layer Controls 能否公开 rejection-inclusive end-to-end denominator、raw/replay trace、
    compiler/runtime manifests 与 randomized harness/model ablation？若 prompt hash 无法解析到 immutable content，
    或 offchain validator 与可升级 contract policy 漂移，mandate-to-settlement evidence chain 如何恢复？
13. xAI Custom Voices 的 launch-day API snapshot、phrase/embedding operating point、spoof/deepfake evaluation、
    human escalation 与 source/derived artifact deletion proof 是否会公开？consent 被撤销、team membership
    变化或 `voice_id` 泄漏时，授权和缓存如何传播失效？
14. Mistral Workflows 能否提供 launch-day frozen SDK/docs、activity delivery/duplicate-side-effect contract、
    workflow-version pinning/migration、history retention、multi-region recovery 与独立 failure-injection 证据？
15. Z.ai incident 的 frozen runtime commits、PR #22811、完整 request/anomaly denominator、detector confusion
    matrix、retry outcome、fence overhead 与 LayerSplit break-even 能否公开并由独立环境复现？
16. Amazon privacy reproduction 能否公开 frozen code/data/config、delta/accountant、round composition、MPC
    trust/dropout/collusion model、attack recall/base rate 与 crypto overhead，并在 large-model/production contract
    下独立复现？
17. C3LLM 的 query-graph generator、judge calibration 与真实 adversarial/human traffic 之间能否建立分布
    对齐证据？其 2025 source family 后续只在 2025 backlog 审计，不应被 2026 publication node 重复计分。
18. AutoSP 的公开 frozen code、operator registry 与 graph rewrite proof 能否覆盖 dynamic/custom/MoE
    programs，并在多节点 topology、完整训练收敛与 failure injection 下保持与手写 Ulysses 等价？
19. LightSeek-SMG 的 gateway/engine protocol 如何锁定 tokenizer、chat template、parser 与 model revision，
    cache 如何失效和隔离；完整 matched workload、raw distribution 与独立复现能否支持作者最大收益？
20. Granite 4.1 七个 mechanism-level source families 已完成分区与全文审计，但哪些缺口仍需 immutable、
    artifact-matched evidence 才能闭合？Language 已确认 512K 是 training exposure、current released contract
    为 131,072，但仍缺 launch-day snapshot 与 512K evaluation；Speech NAR/AR/Plus 仍缺 event-time commit 与
    artifact-matched evaluation；Guardian 仍缺 threshold calibration、adaptive-attack 与独立复现；Embedding
    仍缺 immutable April revision、pruning/vocabulary ablation、per-language confidence intervals、真实 corpus/
    hybrid retrieval、ANN lifecycle 与 quantized backend parity。5 月论文只解释 source family，不倒写成
    4 月 launch-day evidence。
21. Concord 的 2025 acceptance announcement 与 Microsoft-hosted `2025/10` PDF 是否对应公开可访问的
    immutable artifact？若 source family 归 2025，能否获得 code、frozen contract set、dataset split、
    false-negative/recall、drift/relearning、feedback-poisoning 与 production exposure denominator，从而判断
    learned best-effort guard 应如何与 semantic verifier、runtime check 和 rollback gate 分层？
22. vLLM 的 unavailable TransferTopology/Mamba PD PR 全文能否补齐 topology migration、partial completion、
    rollback 与 heterogeneous state-layout contract？`cache_salt` 是否有公开 threat model 与 cross-tenant
    side-channel/failure-injection evidence？
23. Transformers Continuous Batching 的 CPU offload PR 能否稳定访问并核验 cancel/partial-copy/restore cleanup？
    在完整 model、GPU、precision、prompt/output、concurrency 与 TTFT/TPOT SLO 下，multi-peak sizing、offload
    与 soft reset 的 matched frontier 是否仍成立？
24. Diffusion Templates 的 project artifact、carrier serialization、cache schema、base/template compatibility、
    merge-order conflict、并发 memory envelope 与 composition ablation 能否公开并复现？Recovered W18 queue
    的 Safety Drift 需在恢复 primary-source 只读权限后完成全文、artifact、日期/revision、评分与章节
    邻接审计；ViPO 已于 2026-08-13 完成恢复。在此之前 Safety Drift 保持 `Unverified / Blocked`。EmbodiedMidtrain、DiagramBank、IndustryAssetEQA 等
    未定日期 hits 哪些会在 primary-source 全文后进入 W18，哪些只应作为低分拒绝或 earlier-week spillback？
25. Refinement via Regeneration 能否提供 independent evaluator、样本级 data/label provenance、multi-seed
    variance、matched-compute RvE comparison 与 identity/locality/safety human evaluation？多轮 regenerate
    的 stop、rollback、degradation detector 和 immutable experiment revision 应由谁拥有？
26. Mutual Forcing 何时公开 code、checkpoint 与 frozen data/eval manifest？online fake model、Multi/Few mode、
    interval schedule、context buffer 和 recovery point 怎样共同持久化？在披露 GPU/dtype/batch、matched
    hardware/resolution、multi-seed variance 与更长/多说话人 workload 后，few-step 与 long-horizon 结论是否仍成立？
27. Co-Director 的 GenAD-Bench 何时提供 immutable download/manifest？若换 independent judge、显式建模 axis
    interaction、做 multi-seed/cost-matched T sweep，并取消 strategic/execution score 强制同向，MAB 增益是否仍成立？
28. AutoGUI-v2 能否发布 immutable paper-run code/data/prompt manifest 与仍为 TODO 的 element-captioning
    artifact，并披露 human agreement、独立 question audit、contamination、重复运行 uncertainty 与统一 prompt/
    coordinate contract？其 static functionality 分数是否能预测真实 interactive/multi-step outcome？
29. X-WAM 能否提供 event-time immutable code/data/run manifest、v1/v2 semantic diff、latency hardware/dtype/
    batch、multi-seed confidence interval 与 matched-compute 专用 policy/world-model baselines？在 history/KV、
    causal intervention、action cancellation/reconciliation 与独立 real-robot replication 下，ANS 的 Pareto
    优势和 predicted RGB-D 的 world-state validity 是否仍成立？
30. ExoActor 能否公开 official code/data/run manifest、完整 task/trial denominator、success/failure rubric、
    hardware/network/video contract 与 independent audit？在移除 target support、加入 scene perturbation、
    streaming feedback、controller safety envelope 与 matched direct-policy/retargeting baselines 后，案例中的
    imagined-demo interface 是否仍能稳定转化为可执行动作？
31. Representation Fréchet Loss 能否冻结 event-time code/tag、公开 hardware/time/memory overhead 与 multi-seed
    uncertainty，并验证 Queue/EMA state 在 restart、reshard、encoder upgrade 下的 migration/rollback？若训练与
    gate 使用 rotation/held-out encoders 或 non-Gaussian metrics，单一 representation 的 Goodhart surface 是否下降？

## Sources

- Diffusion Templates arXiv metadata and revision history: https://arxiv.org/abs/2604.24351
- Diffusion Templates arXiv HTML v1: https://arxiv.org/html/2604.24351v1
- Diffusion Templates project page (access not independently verified):
  https://modelscope.github.io/DiffSynth-Studio/diffusion-template/
- Refinement via Regeneration arXiv metadata/revision: https://arxiv.org/abs/2604.25636
- Refinement via Regeneration HTML v1: https://arxiv.org/html/2604.25636v1
- Refinement via Regeneration official repository: https://github.com/LeapLabTHU/RvR
- Refinement via Regeneration official inferencer:
  https://raw.githubusercontent.com/LeapLabTHU/RvR/main/inferencer.py
- Refinement via Regeneration current model card: https://huggingface.co/JiayiGuo821/RvR-7B-MoT
- Mutual Forcing arXiv metadata/revision: https://arxiv.org/abs/2604.25819
- Mutual Forcing HTML v1: https://arxiv.org/html/2604.25819v1
- Mutual Forcing official project page: https://mutualforcing.github.io/
- Mutual Forcing current official repository: https://github.com/HVision-NKU/MutualForcing
- Co-Director arXiv metadata/revision: https://arxiv.org/abs/2604.24842
- Co-Director HTML v1: https://arxiv.org/html/2604.24842v1
- Co-Director official project: https://co-director-agent.github.io/index.html
- Co-Director current official implementation:
  https://github.com/GoogleCloudPlatform/genmedia-izumi-agent/tree/main/demos/backend/ads_codirector
- GenAD-Bench current hub: https://co-director-agent.github.io/genad_bench.html
- Hugging Face Daily Papers, 2026-04-27: https://huggingface.co/papers/date/2026-04-27
- Hugging Face Daily Papers, 2026-04-28: https://huggingface.co/papers/date/2026-04-28
- Hugging Face Daily Papers, 2026-04-29: https://huggingface.co/papers/date/2026-04-29
- Hugging Face Daily Papers, 2026-04-30: https://huggingface.co/papers/date/2026-04-30
- Hugging Face Daily Papers, 2026-05-01: https://huggingface.co/papers/date/2026-05-01
- How Much Is One Recurrence Worth? arXiv metadata/revisions: https://arxiv.org/abs/2604.21106

- Microsoft Research, Red-teaming a network of agents (2026-04-30):
  https://www.microsoft.com/en-us/research/blog/red-teaming-a-network-of-agents-understanding-what-breaks-when-ai-agents-interact-at-scale/
- Microsoft Research, Concord publication page:
  https://www.microsoft.com/en-us/research/publication/concord_learning_network_configuration_contracts/
- Concord author-hosted Microsoft PDF:
  https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/eurosys26-spring-final215.pdf
- EuroSys 2026 proceedings index: https://2026.eurosys.org/papers.html
- DBLP EuroSys 2026 index: https://dblp.org/db/conf/eurosys/eurosys2026
- Concord author publication/news page: https://fyy.cs.illinois.edu/publications/
- NVIDIA Technical Blog, Automating GPU Kernel Translation with AI Agents (2026-04-30):
  https://developer.nvidia.com/blog/automating-gpu-kernel-translation-with-ai-agents-cutile-python-to-cutile-jl/
- xAI, Custom Voices announcement (2026-04-30): https://x.ai/news/grok-custom-voices
- xAI, Custom Voices current API documentation (accessed 2026-08-10):
  https://docs.x.ai/developers/model-capabilities/audio/custom-voices
- Baidu ERNIE Blog index, ERNIE-5.1-Preview LMArena announcement (2026-04-30):
  https://ernie.baidu.com/blog/posts/
- Google Research April 2026 archive: https://research.google/blog/2026/04/
- Google DeepMind, Republic of Korea partnership (2026-04-27):
  https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/
- Meta AI official Blog index: https://ai.meta.com/blog/
- ByteDance Seed official Blog index: https://seed.bytedance.com/blog
- Hugging Face Papers, 2026-W18 discovery index: https://huggingface.co/papers/week/2026-W18
- World-R1: https://arxiv.org/abs/2604.24764
- World-R1 HTML v1: https://arxiv.org/html/2604.24764v1
- World-R1 HTML v4: https://arxiv.org/html/2604.24764v4
- World-R1 project / technical details: https://microsoft.github.io/World-R1/tech.html
- World-R1 repository: https://github.com/microsoft/World-R1
- World-R1 official dataset: https://huggingface.co/datasets/microsoft/World-R1
- Tuna-2: https://arxiv.org/abs/2604.24763
- Tuna-2 HTML v1: https://arxiv.org/html/2604.24763v1
- Tuna-2 HTML v2: https://arxiv.org/html/2604.24763v2
- Tuna-2 project page: https://tuna-ai.org/tuna-2/
- Tuna-2 official repository: https://github.com/facebookresearch/tuna-2
- ReVSI: https://arxiv.org/abs/2604.24300
- ReVSI ICML/OpenReview paper: https://openreview.net/pdf/e689f53b9e21c0699df043f8210c3fb8484eb0a6.pdf
- ReVSI full-text access copy: https://www.researchgate.net/publication/404249508_ReVSI_Rebuilding_Visual_Spatial_Intelligence_Evaluation_for_Accurate_Assessment_of_VLM_3D_Reasoning
- ReVSI project: https://3dlg-hcvc.github.io/revsi/
- ReVSI official repository: https://github.com/3dlg-hcvc/revsi
- ReVSI official dataset: https://huggingface.co/datasets/3dlg-hcvc/ReVSI
- Visual Generation in the New Era: https://arxiv.org/abs/2604.28185
- Visual Generation in the New Era HTML v1: https://arxiv.org/html/2604.28185v1
- Visual Generation official living roadmap: https://github.com/EvolvingLMMs-Lab/Evolving-Visual-Generation
- Visual Generation taxonomy artifact:
  https://raw.githubusercontent.com/EvolvingLMMs-Lab/Evolving-Visual-Generation/main/docs/taxonomy.md
- Visual Generation stress-test artifact:
  https://raw.githubusercontent.com/EvolvingLMMs-Lab/Evolving-Visual-Generation/main/docs/stress_tests.md
- Visual Generation frontiers artifact:
  https://raw.githubusercontent.com/EvolvingLMMs-Lab/Evolving-Visual-Generation/main/docs/frontiers.md
- Verifier-Based RL in Image Editing: https://arxiv.org/abs/2604.27505
- Verifier-Based RL in Image Editing HTML v1: https://arxiv.org/html/2604.27505v1
- Edit-R1 first-public OpenReview record: https://openreview.net/forum?id=hKWCGxuD5v
- Meta-CoT for Image Editing: https://arxiv.org/abs/2604.24625
- Meta-CoT HTML v1: https://arxiv.org/html/2604.24625v1
- Meta-CoT official project: https://shiyi-zh0408.github.io/projectpages/Meta-CoT/
- Meta-CoT official repository: https://github.com/shiyi-zh0408/Meta-CoT
- Meta-CoT official model surface: https://huggingface.co/shiyi0408/Meta-CoT
- Meta-CoT 21-task benchmark surface: https://huggingface.co/datasets/shiyi0408/Meta-CoT-21-Tasks-Bench
- FAMA: https://arxiv.org/abs/2604.25135
- FAMA HTML v1: https://arxiv.org/html/2604.25135v1
- Terminal Task Synthesis via Skill Graphs: https://arxiv.org/abs/2604.25727
- Terminal Task Synthesis HTML v1: https://arxiv.org/html/2604.25727v1
- Terminal Task Synthesis PDF: https://arxiv.org/pdf/2604.25727
- vLLM v0.20.0 official release: https://github.com/vllm-project/vllm/releases/tag/v0.20.0
- vLLM Model Runner V2 stale-slot correctness fix PR #39833:
  https://github.com/vllm-project/vllm/pull/39833
- vLLM LMCache `cache_salt` isolation PR #39837:
  https://github.com/vllm-project/vllm/pull/39837
- vLLM IR skeleton / `rms_norm` PR #33825: https://github.com/vllm-project/vllm/pull/33825
- vLLM FA4 MLA prefill default PR #38819: https://github.com/vllm-project/vllm/pull/38819
- vLLM unified `TransferTopology` PR #39529: https://github.com/vllm-project/vllm/pull/39529
- vLLM heterogeneous-TP Mamba PD PR #37635: https://github.com/vllm-project/vllm/pull/37635
- Hugging Face Transformers v5.7.0 official release:
  https://github.com/huggingface/transformers/releases/tag/v5.7.0
- Transformers long-generation Continuous Batching PR #45530:
  https://github.com/huggingface/transformers/pull/45530
- Transformers v5.7.0 Continuous Batching API:
  https://huggingface.co/docs/transformers/v5.7.0/en/main_classes/continuous_batching
- Transformers v5.7.0 Continuous Batching architecture:
  https://huggingface.co/docs/transformers/v5.7.0/en/continuous_batching_architecture
- Compliance versus Sensibility: https://arxiv.org/abs/2604.27251
- Compliance versus Sensibility author-public full-text manuscript:
  https://www.researchgate.net/publication/404333039_Compliance_versus_Sensibility_On_the_Reasoning_Controllability_in_Large_Language_Models
- Compliance versus Sensibility Hugging Face paper record: https://huggingface.co/papers/2604.27251
- Zero-to-CAD: https://arxiv.org/abs/2604.24479
- Zero-to-CAD author-public full-text manuscript:
  https://www.researchgate.net/publication/404249340_Zero-to-CAD_Agentic_Synthesis_of_Interpretable_CAD_Programs_at_Million-Scale_Without_Real_Data
- Zero-to-CAD OpenReview paper: https://openreview.net/pdf?id=QiKZ2TPGL0
- Zero-to-CAD official 100K dataset: https://huggingface.co/datasets/ADSKAILab/Zero-To-CAD-100k
- Zero-to-CAD official 1M dataset: https://huggingface.co/datasets/ADSKAILab/Zero-To-CAD-1m
- Step-Level Advantage Selection: https://arxiv.org/abs/2604.24003
- Step-Level Advantage Selection HTML v1: https://arxiv.org/html/2604.24003v1
- Step-Level Advantage Selection official repository: https://github.com/HanNight/SAS
- Operating-Layer Controls for Onchain Agents: https://arxiv.org/abs/2604.26091
- Operating-Layer Controls public full-text copy:
  https://www.researchgate.net/publication/404307536_Operating-Layer_Controls_for_Onchain_Language-Model_Agents_Under_Real_Capital
- DX Terminal Pro Agent Vault Contract API:
  https://docs.terminal.markets/docs/resource-section/agent-vault-contract-api/
- DX Terminal Pro Core Contracts:
  https://docs.terminal.markets/docs/resource-section/core-contracts/
- DX Terminal Pro Whitepaper: https://docs.terminal.markets/whitepaper
- DX Terminal Pro Terms of Service: https://www.terminal.markets/tos
- Semi-DPO for Noisy Preferences: https://arxiv.org/abs/2604.24952
- Semi-DPO ICLR / OpenReview paper: https://openreview.net/pdf?id=rRc04jyoAk
- Semi-DPO official project page: https://liming-ai.github.io/SemiDPO/
- Semi-DPO public full-text copy: https://www.researchgate.net/publication/404281276_Learning_from_Noisy_Preferences_A_Semi-Supervised_Learning_Approach_to_Direct_Preference_Optimization
- Semi-DPO promised code URL (404 when accessed 2026-08-10): https://github.com/L-CodingSpace/semi-dpo
- Conversational User Simulation survey: https://arxiv.org/abs/2604.24977
- Conversational User Simulation survey HTML v1: https://arxiv.org/html/2604.24977v1
- Perceval: https://arxiv.org/abs/2604.24583
- Perceval HTML v1: https://arxiv.org/html/2604.24583v1
- Perceval official repository: https://github.com/RUCAIBox/Perceval
- Turning TIDE: https://arxiv.org/abs/2604.26951
- Turning TIDE HTML v1: https://arxiv.org/html/2604.26951v1
- Turning TIDE official repository: https://github.com/PKU-YuanGroup/TIDE
- Step-level Optimization for Efficient Computer-use Agents: https://arxiv.org/abs/2604.27151
- Step-level Optimization HTML v1: https://arxiv.org/html/2604.27151v1
- Step-level Optimization PDF v1: https://arxiv.org/pdf/2604.27151
- StepWise official detector collection: https://huggingface.co/collections/yale-nlp/stepwise
- InteractWeb-Bench: https://arxiv.org/abs/2604.27419
- InteractWeb-Bench HTML: https://arxiv.org/html/2604.27419v1
- InteractWeb-Bench project: https://interactweb-bench.wangqiyao.me/
- InteractWeb-Bench repository: https://github.com/AIforIP/InteractWeb-Bench
- FlashRT: https://arxiv.org/abs/2604.28157
- FlashRT HTML v1: https://arxiv.org/html/2604.28157v1
- FlashRT PDF v1: https://arxiv.org/pdf/2604.28157
- FlashRT official repository: https://github.com/wang-yanting/FlashRT
- GLM-5V-Turbo Technical Report: https://arxiv.org/abs/2604.26752
- GLM-5V-Turbo HTML v1: https://arxiv.org/html/2604.26752v1
- GLM-5V-Turbo HTML v3: https://arxiv.org/html/2604.26752v3
- GLM-5V-Turbo official API guide: https://docs.z.ai/guides/vlm/glm-5v-turbo
- GLM-V repository: https://github.com/zai-org/GLM-V
- ImageMining repository: https://github.com/zai-org/ImageMining
- GLM Skills repository: https://github.com/zai-org/GLM-skills
- System-Integrated Speculative Decoding for RL Rollouts: https://arxiv.org/abs/2604.26779
- System-Integrated Speculative Decoding HTML v1: https://arxiv.org/html/2604.26779v1
- NeMo RL repository: https://github.com/NVIDIA-NeMo/RL
- NeMo RL releases: https://github.com/NVIDIA-NeMo/RL/releases
- Synthetic Computers at Scale: https://arxiv.org/abs/2604.28181
- Synthetic Computers HTML v1: https://arxiv.org/html/2604.28181v1
- Synthetic Computers PDF v1: https://arxiv.org/pdf/2604.28181
- Microsoft Research publication: https://www.microsoft.com/en-us/research/publication/synthetic-computers-at-scale-for-long-horizon-productivity-simulation/
- Synthetic Computers official dataset: https://huggingface.co/datasets/microsoft/synthetic-computers-at-scale
- Agent-Native Research Artifacts: https://arxiv.org/abs/2604.24658
- Agent-Native Research Artifacts HTML v1: https://arxiv.org/html/2604.24658v1
- Agent-Native Research Artifact repository: https://github.com/ARA-Labs/Agent-Native-Research-Artifact
- Process-Level Reward Modeling for Agentic Data Analysis: https://arxiv.org/abs/2604.24198
- Process-Level Reward Modeling HTML v1: https://arxiv.org/html/2604.24198v1
- Process-Level Reward Modeling HTML v2: https://arxiv.org/html/2604.24198v2
- DataMind repository: https://github.com/zjunlp/DataMind
- DataPRM artifact README: https://github.com/zjunlp/DataMind/blob/main/dataprm/README.md
- Step-Audio-R1.5 Technical Report: https://arxiv.org/abs/2604.25719
- Step-Audio-R1.5 HTML v1: https://arxiv.org/html/2604.25719v1
- Step-Audio-R1.5 HTML v2: https://arxiv.org/html/2604.25719v2
- Step-Audio-R1/R1.5 official repository: https://github.com/stepfun-ai/Step-Audio-R1
- Step-Audio-R1.5 benchmark package: https://github.com/stepfun-ai/Step-Audio-R1/tree/main/benchmarks/Step-Audio-R1.5
- Representational Stability for Tabular Retrieval: https://arxiv.org/abs/2604.24040
- Representational Stability for Tabular Retrieval HTML v1: https://arxiv.org/html/2604.24040v1
- Representational Stability for Tabular Retrieval HTML v2: https://arxiv.org/html/2604.24040v2
- Centroid-Aligned Table Retrieval repository: https://github.com/KBhandari11/Centroid-Aligned-Table-Retrieval
- KServe v0.18.0 release: https://github.com/kserve/kserve/releases/tag/v0.18.0
- KServe 0.18 release blog: https://kserve.github.io/website/blog/kserve-0.18-release
- KServe control-plane documentation: https://kserve.github.io/website/docs/concepts/architecture/control-plane
- KServe API reference: https://kserve.github.io/website/docs/reference/crd-api
- Kubernetes v1.36 controller staleness mitigation:
  https://kubernetes.io/blog/2026/04/28/kubernetes-v1-36-staleness-mitigation-for-controllers/
- client-go v0.36.0 cache package: https://pkg.go.dev/k8s.io/client-go@v0.36.0/tools/cache
- Kubernetes metrics reference: https://kubernetes.io/docs/reference/instrumentation/metrics/
- Mutable Pod Resources for Suspended Jobs:
  https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/
- Kubernetes Jobs concept: https://kubernetes.io/docs/concepts/workloads/controllers/job/
- Kubernetes feature gates: https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/
- Kubernetes batch/v1 Job API reference: https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/job-v1/
- Tiered Memory Protection with Memory QoS:
  https://kubernetes.io/blog/2026/04/29/kubernetes-v1-36-memory-qos-tiered-protection/
- Kubernetes Pod QoS classes: https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/
- Kubernetes resource management for Pods and containers:
  https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
- Kubernetes cgroup v2: https://kubernetes.io/docs/concepts/architecture/cgroups/
- Linux kernel cgroup v2 memory controller: https://docs.kernel.org/admin-guide/cgroup-v2.html
- In-Place Vertical Scaling for Pod-Level Resources:
  https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/
- Resize CPU and memory resources assigned to Pods:
  https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
- Pod-Level Resource Managers:
  https://kubernetes.io/blog/2026/05/01/kubernetes-v1-36-feature-pod-level-resource-managers-alpha/
- Kubernetes Resource Managers concept:
  https://kubernetes.io/docs/concepts/workloads/resource-managers/
- Kubernetes feature gates:
  https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/
- Assign Pod-level CPU and memory resources:
  https://kubernetes.io/docs/tasks/configure-pod-container/assign-pod-level-resources/
- Manifest-Based Admission Control publication node:
  https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/
- Server-Side Sharded List and Watch publication node:
  https://kubernetes.io/blog/2026/05/06/kubernetes-v1-36-server-side-sharded-list-and-watch/
- Kubernetes v1.36 DRA updates publication node:
  https://kubernetes.io/blog/2026/05/07/kubernetes-v1-36-dra-136-updates/
- PSI Metrics GA publication node:
  https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
- Workload-Aware Scheduling publication node:
  https://kubernetes.io/blog/2026/05/13/kubernetes-v1-36-advancing-workload-aware-scheduling/
- Gateway API v1.5 publication / release reconciliation:
  https://kubernetes.io/blog/2026/04/21/gateway-api-v1-5/
- Agent Sandbox publication node:
  https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox/
- Recursive Multi-Agent Systems: https://arxiv.org/abs/2604.25917
- Recursive Multi-Agent Systems HTML: https://arxiv.org/html/2604.25917
- Recursive Multi-Agent Systems project: https://recursivemas.github.io
- TCOD: https://arxiv.org/abs/2604.24005
- TCOD HTML v3: https://arxiv.org/html/2604.24005v3
- Programming with Data: https://arxiv.org/abs/2604.24819
- Programming with Data HTML: https://arxiv.org/html/2604.24819
- Programming with Data repository: https://github.com/OpenRaiser/ProDa
- Large Language Models Explore by Latent Distilling: https://arxiv.org/abs/2604.24927
- Large Language Models Explore by Latent Distilling HTML: https://arxiv.org/html/2604.24927
- tLLM / ESamp repository: https://github.com/LinesHogan/tLLM
- Nemotron 3 Nano Omni: https://arxiv.org/abs/2604.24954
- Nemotron 3 Nano Omni HTML: https://arxiv.org/html/2604.24954
- Nemotron 3 Nano Omni BF16 model card: https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-Omni-30B-A3B-BF16
- BARRED: https://arxiv.org/abs/2604.25203
- BARRED v1 PDF: https://arxiv.org/pdf/2604.25203
- BARRED repository: https://github.com/plurai-ai/BARRED
- AutoResearchBench: https://arxiv.org/abs/2604.25256
- AutoResearchBench HTML: https://arxiv.org/html/2604.25256
- AutoResearchBench repository: https://github.com/CherYou/AutoResearchBench
- DV-World: https://arxiv.org/abs/2604.25914
- DV-World version-specific HTML: https://arxiv.org/html/2604.25914v1
- DV-World project: https://dv-world-project.github.io
- ClawGym: https://arxiv.org/abs/2604.26904
- ClawGym v1 HTML: https://arxiv.org/html/2604.26904v1
- ClawGym repository: https://github.com/ClawGym
- Length Value Model: https://arxiv.org/abs/2604.27039
- Length Value Model v1 PDF: https://arxiv.org/pdf/2604.27039v1
- Length Value Model repository: https://github.com/UCSB-AI/Length-Value-Model
- Co-Evolving Policy Distillation: https://arxiv.org/abs/2604.27083
- Co-Evolving Policy Distillation v1 PDF: https://arxiv.org/pdf/2604.27083
- RoundPipe: https://arxiv.org/abs/2604.27085
- RoundPipe v1 HTML: https://arxiv.org/html/2604.27085v1
- RoundPipe repository: https://github.com/ITcarrot/RoundPipe
- Heterogeneous Scientific Foundation Model Collaboration: https://arxiv.org/abs/2604.27351
- Heterogeneous Scientific Foundation Model Collaboration v1 HTML: https://arxiv.org/html/2604.27351v1
- Eywa repository: https://github.com/Violet24K/Eywa
- Claw-Eval-Live: https://arxiv.org/abs/2604.28139
- Claw-Eval-Live v1 HTML: https://arxiv.org/html/2604.28139v1
- Intern-Atlas: https://arxiv.org/abs/2604.28158
- Intern-Atlas v1 HTML: https://arxiv.org/html/2604.28158v1
- From Context to Skills: https://arxiv.org/abs/2604.27660
- From Context to Skills v1 HTML: https://arxiv.org/html/2604.27660v1
- From Context to Skills repository: https://github.com/S1s-Z/Ctx2Skill
- Beyond Semantic Similarity: https://arxiv.org/abs/2605.05242
- Beyond Semantic Similarity v1 PDF: https://arxiv.org/pdf/2605.05242
- Beyond Semantic Similarity repository: https://github.com/DCI-Agent/DCI-Agent-Lite
- MiniCPM-o 4.5: https://arxiv.org/abs/2604.27393
- MiniCPM-o 4.5 v1 HTML: https://arxiv.org/html/2604.27393v1
- Web2BigTable: https://arxiv.org/abs/2604.27221
- Web2BigTable v1 HTML: https://arxiv.org/html/2604.27221v1
- Web2BigTable repository: https://github.com/OpenBMB/UltraRAG/tree/main/web2bigtable
- WindowsWorld: https://arxiv.org/abs/2604.27776
- WindowsWorld v1 HTML: https://arxiv.org/html/2604.27776v1
- RouteProfile: https://arxiv.org/abs/2605.00180
- RouteProfile v1 HTML: https://arxiv.org/html/2605.00180v1
- Mistral Workflows announcement: https://mistral.ai/it/news/workflows/
- Mistral Workflows overview: https://docs.mistral.ai/studio-api/workflows/getting-started/overview
- Mistral workflow core concepts:
  https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/workflows
- Mistral workflow events:
  https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/events
- Mistral workflow determinism:
  https://docs.mistral.ai/studio-api/workflows/building-workflows/workflows/determinism
- Mistral workflow activities:
  https://docs.mistral.ai/studio-api/workflows/building-workflows/activities
- Mistral workflow waiting conditions:
  https://docs.mistral.ai/studio-api/workflows/building-workflows/waiting_for_conditions
- Mistral workflow workers:
  https://docs.mistral.ai/studio-api/workflows/getting-started/core_concepts/workers
- Mistral workflow deployments:
  https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/deployments
- Mistral hardened deployments:
  https://docs.mistral.ai/studio-api/workflows/managing-workflows-in-production/hardened_deployments
- Mistral workflow connectors and identity:
  https://docs.mistral.ai/studio-api/workflows/building-workflows/connectors
- Mistral on-behalf-of workflows:
  https://docs.mistral.ai/studio-api/workflows/building-workflows/on_behalf_of
- OpenAI Research release index: https://openai.com/research/index/release/
- Kimi Agent help / official model-evolution timeline:
  https://www.kimi.com/help/agent/agent-overview
- MiniMax official model release notes:
  https://platform.minimax.io/docs/release-notes/models
- MiniMax official News index: https://www.minimax.io/news
- Qwen Research index: https://qwen.ai/research
- Qwen Code official update index:
  https://qwenlm.github.io/qwen-code-docs/en/blog/updates/
- Baidu ERNIE publication index: https://ernie.baidu.com/blog/zh/publication/
- Tencent Hunyuan official GitHub organization: https://github.com/Tencent-Hunyuan
- Huawei Noah's Ark Lab official News index: https://noahlab.com.hk/en/news
- Shanghai AI Laboratory official News index: https://www.shlab.org.cn/info
- Shanghai AI Laboratory April boundary page: https://www.shlab.org.cn/info/5
- StepFun Research index: https://www.stepfun.com/research
- Xiaomi MiMo official Research index: https://mimo.xiaomi.com/
- InclusionAI official publication index: https://www.inclusion-ai.org/publication/
- Hugging Face, DeepInfra on Inference Providers (2026-04-29):
  https://huggingface.co/blog/inference-providers-deepinfra
- NVIDIA / Siemens Healthineers, NV-Raw2Insights-US (2026-04-28):
  https://huggingface.co/blog/nvidia/raw2insights-adaptive-ultrasound-imaging
- NV-Raw2Insights-US model artifact:
  https://huggingface.co/nvidia/NV-Raw2Insights-US
- Apple Machine Learning Research ICLR 2026 index:
  https://machinelearning.apple.com/research/iclr-2026
- Ai2 News index: https://allenai.org/news
- DeepSeek API changelog: https://api-docs.deepseek.com/updates/
- NVIDIA Dynamo tag index: https://developer.nvidia.com/blog/tag/nvidia-dynamo/
- NVIDIA Technical Blog index: https://developer.nvidia.com/blog
- Z.ai Scaling Pain of Coding Agent Serving: https://z.ai/blog/scaling-pain
- Z.ai GLM-5 release/workload context: https://z.ai/blog/glm-5
- Amazon Science, Preserving the privacy of AI training data (2026-04-29):
  https://www.amazon.science/blog/preserving-the-privacy-of-ai-training-data
- Amazon Science, Scalable membership inference attacks via quantile regression:
  https://www.amazon.science/publications/scalable-membership-inference-attacks-via-quantile-regression
- Deep Learning with Differential Privacy: https://arxiv.org/abs/1607.00133
- Deep Leakage from Gradients: https://arxiv.org/abs/1906.08935
- Flamingo secure aggregation: https://eprint.iacr.org/2023/486
- Robbing the Fed: https://arxiv.org/abs/2110.13057
- Scale-MIA: https://arxiv.org/abs/2311.05808
- Amazon Science, How catastrophic is your LLM? (2026-04-27):
  https://www.amazon.science/blog/how-catastrophic-is-your-llm
- C3LLM publication page:
  https://www.amazon.science/publications/how-catastrophic-is-your-llm-certifying-risk-in-conversation
- C3LLM arXiv metadata and revision history: https://arxiv.org/abs/2510.03969
- C3LLM v3 PDF:
  https://cdn.amazon.science/55/92/24ed832348cb87e9caab8b08e3a2/how-catastrophic-is-your-llm-certifying-risk-in-conversation.pdf
- PyTorch, Introducing AutoSP (2026-04-29):
  https://pytorch.org/blog/introducing-autosp/
- AutoSP arXiv metadata and revision history: https://arxiv.org/abs/2604.27089
- AutoSP arXiv HTML v1: https://arxiv.org/html/2604.27089v1
- PyTorch, LightSeek-SMG (2026-04-30):
  https://pytorch.org/blog/lightseek-smg/
- IBM Research, Introducing the IBM Granite 4.1 family of models (2026-04-29):
  https://research.ibm.com/blog/granite-4-1-ai-foundation-models
- IBM Granite / Hugging Face, Granite 4.1 Language Model Technical Article (2026-04-29):
  https://huggingface.co/blog/ibm-granite/granite-4-1
- IBM Granite official Hugging Face organization: https://huggingface.co/ibm-granite
- Granite 4.1 Language collection:
  https://huggingface.co/collections/ibm-granite/granite-41-language-models
- Granite 4.1 Language model repository:
  https://github.com/ibm-granite/granite-4.1-language-models
- Granite 4.1 Language 3B current model card: https://huggingface.co/ibm-granite/granite-4.1-3b
- Granite 4.1 Language 8B current model card: https://huggingface.co/ibm-granite/granite-4.1-8b
- Granite 4.1 Language 8B current config:
  https://huggingface.co/ibm-granite/granite-4.1-8b/blob/main/config.json
- Granite 4.1 Language 8B commit history:
  https://huggingface.co/ibm-granite/granite-4.1-8b/commits/main
- Granite 4.1 Language 30B current model card: https://huggingface.co/ibm-granite/granite-4.1-30b
- Granite Vision 4.1 4B current model card: https://huggingface.co/ibm-granite/granite-vision-4.1-4b
- Granite Vision 4.1 4B current config:
  https://huggingface.co/ibm-granite/granite-vision-4.1-4b/blob/main/config.json
- Granite Vision 4.1 4B commit history:
  https://huggingface.co/ibm-granite/granite-vision-4.1-4b/commits/main
- ChartNet arXiv metadata and revision history: https://arxiv.org/abs/2603.27064
- ChartNet arXiv HTML v1: https://arxiv.org/html/2603.27064v1
- ChartNet current dataset card and changelog: https://huggingface.co/datasets/ibm-granite/ChartNet
- Granite Speech collection: https://huggingface.co/collections/ibm-granite/granite-speech
- Granite Speech 4.1 2B current model card: https://huggingface.co/ibm-granite/granite-speech-4.1-2b
- Granite-speech predecessor arXiv metadata/revisions: https://arxiv.org/abs/2505.08699
- Granite-speech predecessor HTML v2: https://arxiv.org/html/2505.08699v2
- Self-Speculative Decoding arXiv metadata/sole-v1 history: https://arxiv.org/abs/2603.11243
- Self-Speculative Decoding HTML v1: https://arxiv.org/html/2603.11243v1
- Granite Speech 4.1 2B Plus current model card:
  https://huggingface.co/ibm-granite/granite-speech-4.1-2b-plus
- Speaker-attributed ASR arXiv metadata and sole-v1 history: https://arxiv.org/abs/2604.11269
- Speaker-attributed ASR PDF v1: https://arxiv.org/pdf/2604.11269
- In-Sync timestamp arXiv metadata and sole-v1 history: https://arxiv.org/abs/2604.22817
- In-Sync timestamp PDF v1: https://arxiv.org/pdf/2604.22817
- Granite Speech 4.1 2B NAR current model card:
  https://huggingface.co/ibm-granite/granite-speech-4.1-2b-nar
- NLE arXiv metadata and sole-v1 history: https://arxiv.org/abs/2603.08397
- NLE arXiv HTML v1: https://arxiv.org/html/2603.08397v1
- Granite Guardian 4.1 official docs: https://www.ibm.com/granite/docs/models/guardian
- Granite Guardian 4.1 8B current model card:
  https://huggingface.co/ibm-granite/granite-guardian-4.1-8b
- Granite Guardian 4.1 initial artifact commit:
  https://huggingface.co/ibm-granite/granite-guardian-4.1-8b/commit/e30b8a2343efe8030479777d467ebb305ca109e9
- Granite Guardian predecessor paper metadata/revisions: https://arxiv.org/abs/2412.07724
- Granite Guardian predecessor HTML: https://arxiv.org/html/2412.07724
- Granite Embedding 97M Multilingual R2 current model card:
  https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2
- Granite Embedding Multilingual R2 paper metadata/revisions: https://arxiv.org/abs/2605.13521
- Granite Embedding Multilingual R2 HTML v1: https://arxiv.org/html/2605.13521v1
- Granite Embedding models repository: https://github.com/ibm-granite/granite-embedding-models
- MAIC-UI arXiv metadata and sole-v1 history: https://arxiv.org/abs/2604.25806
- MAIC-UI arXiv HTML v1: https://arxiv.org/html/2604.25806v1
- MAIC-UI official implementation: https://github.com/THU-MAIC/MAIC-UI
- MAIC-UI current editor processor implementation:
  https://github.com/THU-MAIC/MAIC-UI/blob/main/backend/src/services/editor_processor.py
- GoClick arXiv metadata and sole-v1 history: https://arxiv.org/abs/2604.23941
- GoClick arXiv PDF v1: https://arxiv.org/pdf/2604.23941
- GoClick official repository: https://github.com/ZJULiHongxin/GoClick
- GoClick current Florence-2 training implementation:
  https://github.com/ZJULiHongxin/GoClick/blob/main/florence2/finetune.py
- GoClick-Large current model card: https://huggingface.co/HongxinLi/GoClick-Large
- GoClick-Base current model card: https://huggingface.co/HongxinLi/GoClick-Base
- GoClick SFT data artifact: https://huggingface.co/datasets/HongxinLi/GoClick_sft_data
- AutoGUI-v2 arXiv metadata and revision history: https://arxiv.org/abs/2604.24441
- AutoGUI-v2 arXiv PDF: https://arxiv.org/pdf/2604.24441
- AutoGUI-v2 official repository: https://github.com/ZJULiHongxin/AutoGUI-v2
- AutoGUI-v2 region-grounding dataset:
  https://huggingface.co/datasets/HongxinLi/AutoGUIv2-FuncRegionGnd-v2
- ElementsClaw arXiv v1 metadata and submission history: https://arxiv.org/abs/2604.23758v1
- ElementsClaw arXiv v2 revision node: https://arxiv.org/abs/2604.23758v2
- X-WAM arXiv v1 metadata and revision history: https://arxiv.org/abs/2604.26694v1
- X-WAM arXiv HTML v1: https://arxiv.org/html/2604.26694v1
- X-WAM project page: https://sharinka0715.github.io/X-WAM/
- X-WAM current official implementation: https://github.com/sharinka0715/X-WAM
- ExoActor arXiv metadata and sole-v1 history: https://arxiv.org/abs/2604.27711v1
- ExoActor arXiv HTML v1: https://arxiv.org/html/2604.27711v1
- ExoActor project page: https://baai-agents.github.io/ExoActor/
- ExoActor code link (currently 404): https://github.com/BAAI-Agents/ExoActor
- Representation Fréchet Loss arXiv metadata and sole-v1 history: https://arxiv.org/abs/2604.28190v1
- Representation Fréchet Loss arXiv HTML v1: https://arxiv.org/html/2604.28190v1
- Representation Fréchet Loss current official repository: https://github.com/Jiawei-Yang/FD-loss

## 2026-08-13 Source-Family Books Integration

ExoActor 的最终 disposition 保持 `No Change — Already Covered`，但结构 owner 从 legacy Ch10 明确迁移为 `MULTIMODAL-EMBODIED-VLA` / Current Ch26 / Legacy N/A。Ch26 已拥有 visual plan → motion → controller 的 lossy handoff、open-loop failure amplification 与 closed-loop/safety 演进；该 paper 缺 artifact 和定量 denominator，不再重复增加案例正文。Diffusion Templates 作为 `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 的受限 correction/refinement evidence。Tuna-2 继续 `Disputed`，未进入 Books。Archive Completion Gate 仍 Open。

## 2026-08-14 Final Books Integration Review — 86/86 Scored + 1 Blocked

Candidate Scoring 表中的 `provisional Refine` 在本节完成 owner/adjacent-chapter revalidation 后转为最终
`Refine — Existing Argument`，但仍保留各自的 `Experimental` 或 `Version-Grounded` evidence boundary。
书稿采用下列唯一 owner 聚类；候选名称只在本账本中集中列出，正文继续按机制演进组织。

### Refine Owner Coverage — 56/56

| Stable Owner | Current / Legacy | Source Families Revalidated |
| --- | --- | --- |
| `WORLDVIEW-REPRESENTATION` | Ch5 / Ch5 | Granite Speech 4.1 2B AR |
| `MODEL-TRANSFORMER-LAYER` | Ch17 / Ch17 | Granite Vision 4.1 4B；Compliance versus Sensibility |
| `MODEL-SAMPLING` | Ch20 / Ch20 | Large Language Models Explore by Latent Distilling |
| `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | World-R1；Diffusion Templates；Refinement via Regeneration；Mutual Forcing |
| `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | GoClick；X-WAM |
| `TRAIN-DATA` | Ch27 / Ch23 | Programming with Data；Zero-to-CAD；Terminal Task Synthesis via Skill Graphs |
| `TRAIN-PRETRAINING` | Ch28 / Ch24 | Granite 4.1 Language 3B/8B/30B |
| `TRAIN-SFT` | Ch29 / Ch25 | Turning the TIDE |
| `TRAIN-GRPO` | Ch33 / Ch29 | Co-Evolving Policy Distillation；TCOD；Perceval；Step-Level Advantage Selection；Meta-CoT |
| `TRAIN-DPO` | Ch34 / Ch30 | Semi-DPO；ViPO |
| `TRAIN-TENSOR-PARALLEL` | Ch37 / Ch33 | AutoSP |
| `TRAIN-PIPELINE-PARALLEL` | Ch38 / Ch34 | RoundPipe；GLM-5V-Turbo |
| `INFER-REQUEST-LIFECYCLE` | Ch42 / Ch38 | Granite Speech 4.1 2B Plus；MiniCPM-o 4.5；LightSeek-SMG |
| `INFER-DECODE` | Ch44 / Ch40 | Granite Speech 4.1 2B NAR |
| `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | System-Integrated Speculative Decoding for RL Rollouts |
| `INFER-VLLM` | Ch50 / Ch46 | vLLM v0.20.0 |
| `INFER-SGLANG` | Ch51 / Ch47 | Z.ai Scaling Pain of Coding Agent Serving |
| `INFER-SCHEDULING` | Ch56 / Ch52 | Length Value Model |
| `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | Kubernetes controller staleness mitigation；in-place Pod-level vertical scaling |
| `PLATFORM-TRAINING-OPERATOR` | Ch60 / Ch56 | mutable resources for suspended Jobs |
| `PLATFORM-GATEWAY` | Ch62 / Ch58 | RouteProfile |
| `PLATFORM-GPU-SCHEDULER` | Ch63 / Ch59 | Pod-Level Resource Managers |
| `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | DataPRM；ReVSI；Representation Fréchet Loss |
| `PLATFORM-MULTI-TENANT` | Ch71 / Ch67 | tiered Memory QoS protection |
| `PLATFORM-SECURITY` | Ch72 / Ch68 | xAI Custom Voices；Granite Guardian；BARRED；FlashRT |
| `AGENT-RAG` | Ch76 / Ch72 | Granite Embedding R2；Beyond Semantic Similarity；tabular retrieval representational stability |
| `AGENT-WORKFLOW` | Ch81 / Ch77 | Synthetic Computers；Step-level Optimization for Computer-use Agents |
| `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Microsoft network red-team；Recursive Multi-Agent Systems |
| `AGENT-PLATFORM` | Ch84 / Ch80 | Agent-Native Research Artifacts；Onchain Operating-Layer Controls |
| `INFER-CONTINUOUS-BATCHING` | Ch46 / Ch42 | Hugging Face Transformers v5.7.0 |

这些机制在当前 Books 中分别落为：latent transport 不抹去协议隔离；data/curriculum/verifier 分责；
distillation/advantage/noisy-preference 的 evidence boundary；PP/SP 与多模态 token shape 的 execution contract；
draft/target 双版本与 KV commit；cold-start routing、length value 与 CPU/GPU gateway state；Kubernetes desired/
observed/applied generation；policy-as-data 与 red-team operating point；RAG representation identity；以及
Workflow/Agent Platform 的 artifact、side-effect 与 authority binding。没有为重复来源另建论文段落。

### No Change — 21/21

Mistral Workflows、Amazon privacy reproduction、ClawGym、Intern-Atlas、Claw-Eval-Live、heterogeneous
scientific foundation-model collaboration、AutoResearchBench、Nemotron Omni、Ctx2Skill、Web2BigTable、
WindowsWorld、Step-Audio-R1.5、TileGym、Conversational User Simulation、InteractWeb-Bench、Visual Generation
survey、FAMA、Co-Director、MAIC-UI、AutoGUI-v2 与 ExoActor 均完成章节级去重。它们分别被现有 Workflow、
Security、Evaluation、RAG/Memory、Multimodal generation/embodied、Skill compilation 与 Agent Platform
contracts 具体覆盖；`No Change` 不表示来源无价值，而是没有新增长期机制。

### Weekly Only / Disputed / Blocked

- Weekly Only `7/7`：Empirical Research Assistance、Science partnerships/open resources、DeepMind–Korea
  partnership、DeepInfra provider integration、NVIDIA/Siemens Raw2Insights-US、ERNIE-5.1 Preview、KServe
  v0.18.0 stable。它们是合作、案例、provider、leaderboard 或版本事实，不形成新的长期机制。
- Disputed `2/2`：DV-World 的 temporal integrity 与 Tuna-2 的 revision integrity 未闭合；均不写 Books。
- Unscored blocked `1/1`：Safety Drift After Fine-Tuning 缺 primary full text，保持
  `Unverified / Blocked / No Books Change`，不从摘要反推机制。

### W18 Gate Result

- Scored candidates: `86/86` final disposition；`56 Refine + 21 No Change + 7 Weekly Only + 2 Disputed`。
- Current scored `20+`: `80/80` Full Source Reviews；low-score rows `6/6` verified。
- Source-Family Books Gate: `Complete`；Historical Archive/Discovery Gate: `Open`。
- Safety Drift 与 cross-index discovery backlog 不再阻塞已完成 Source Families，但禁止宣称 W18 archive closed。
- 没有新增 Part、章节或 Stable Node；没有把厂商 benchmark、作者实验或 release headline 写成通用性能事实。
