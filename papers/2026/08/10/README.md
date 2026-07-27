# Daily Research — 2026-08-10

**Coverage Window:** 2026-08-08 09:02 ～ 2026-08-10 09:02（Asia/Shanghai）
**Access Date:** 2026-08-10
**Archive Clock:** Monday；仅生成 Daily，不生成 provisional `2026-W33`
**Status:** No Material Update；检索窗口与证据缺口已记录；Books Integration 不启动

## Executive Summary

本次检索没有发现能在过去 48 小时内以 primary source 同时确认首次公开日期、机制与长期
AI System 增量的候选。官方模型/研究机构入口没有返回可核验的新 Research；arXiv 周末窗口没有
形成可安全归档的新 listing；工程 Release 搜索结果主要是旧版本、未来/缓存错位页面或缺少明确
event date 的聚合结果。Hugging Face 首页出现的社区文章与榜单更新不等于官方研究证据，未进入评分。

因此今日不修改 Books，也不把搜索空白解释为“确认没有任何发布”。W32 的 2026-08-09 Daily 当前
缺失，且完整 Sunday Weekly 尚不能在缺少七日 Daily coverage 的情况下静默补造；该 gap 留待后续
按 primary-source 与 archive-clock 规则单独修复。

## 1. 模型与研究机构

### Source Coverage

按固定来源顺序检查 OpenAI、Anthropic、Apple ML Research、Google DeepMind/Research、Meta AI、
Microsoft Research、NVIDIA Research、Amazon Science、Cohere Labs、Ai2、Mistral、Hugging Face Blog，
以及 Qwen、DeepSeek、Kimi、Zhipu、MiniMax、ByteDance Seed、ERNIE、Hunyuan、Huawei Noah、
InternLM、StepFun、MiMo 与 InclusionAI/Ant 的公开入口和搜索索引。

- **No verified in-window Research event**：可访问的 official index 没有显示 8 月 8～10 日首次公开、
  且带 technical report/system card/primary artifact 的新事件。
- **Coverage limitation**：搜索索引存在抓取延迟；部分国内机构页面没有稳定的按日期列表。本结论只表示
  “本次无法验证”，不表示绝对没有发布。
- **Noise rejected**：Hugging Face community posts、榜单名次、旧文章重收录和缺少机制材料的产品宣传。

### Candidate Scoring

本组没有达到评分门槛的可验证窗口内候选。

## 2. arXiv / 学术来源

### Source Coverage

检查 arXiv `cs.AI`、`cs.CL`、`cs.LG`、`cs.DC`、`cs.IR`、`cs.CR` 与 `stat.ML` recent/new 入口，
并用 Hugging Face Papers、OpenReview/TMLR、Google Scholar、OpenAlex、Semantic Scholar 与 DBLP
作 discovery/cross-check。8 月 8～9 日处于周末，检索结果未提供可由 arXiv metadata 与正文共同核验的
新 first-public event；聚合索引中的相邻日期论文不能在未核对 v1 日期前归入今日。

### Candidate Scoring

本组没有达到评分门槛的可验证窗口内候选。Evidence Level 为 `No Verified Candidate`，不是对未来
revision 或索引延迟的否定。

## 3. AI Infra 与工程项目

### Source Coverage

检查 vLLM、SGLang、PyTorch、TorchRL、KServe、Ray、TensorRT-LLM、Triton 与 Kubernetes 的 release
入口。搜索返回的 vLLM/SGLang 等页面包含旧 release 或缓存中的不一致日期，无法确认属于本窗口；
TorchRL 页面只显示此前已发布的 SGLang integration。未发现需要进入长期知识树的新 stable release、
RFC、重要 PR 或明确行为变化。

### Candidate Scoring

本组没有达到评分门槛的可验证窗口内候选。

## Evidence Level and Fact Boundary

- **Official fact**：只记录官方索引、release page 与 arXiv metadata 在本次访问时可见的状态。
- **Paper evidence**：今日没有完成新的全文 Source Packet，因此不形成论文机制结论。
- **Community evidence**：Hugging Face community article 只作为 discovery signal，未当作事实来源。
- **Inference**：索引延迟、周末 listing 节奏可能解释空白，但这只是推断，不能替代后续复核。
- **Performance numbers**：今日不引用任何缺少 model、hardware、length、batch/concurrency、precision
  与 SLO contract 的数字。

## Knowledge Tree Position

无新候选需要定位 ROADMAP node。现有 Ch20～30、Ch38～59、Ch62～69 与 Ch71～80 的结论不变。

## Recommended Action

`Daily Only — No Books Change`。下次运行重新检查周末后出现的 arXiv Monday listing、官方 Research
入口和 stable release date；若发现 first-public 属于本窗口的候选，应回写本 Daily，而不是按发现日错归。

## Ignored Noise

- 旧研究在搜索结果中的重新收录；
- 没有 technical report/model card/system card 的产品功能 headline；
- 社区 benchmark 排名与未绑定 workload contract 的性能宣传；
- release 页面缓存或搜索摘要中无法与 tag date 对齐的版本信息。

## Repository Changes

- 新建 `papers/2026/08/10/README.md`，记录 No Material Update 与实际覆盖边界。
- 未修改 Books、ROADMAP 或 DECISIONS。
- Historical W18 修复属于同次自动运行的独立检查点：扩展 title/date reconciliation 确认的 9 项中，
  World-R1 已完成 26/30 评分、v1/v4/官方 artifact 全文审计和 Ch29/62 邻接定位；Tuna-2 已完成
  24/30 评分、v1/v2/官方 project/code、pixel-space architecture、training/evaluation contract 与
  Ch4～6/23～24 邻接审计，并因 revision-integrity 冲突保留为 Experimental/Disputed。current retained set
  当时达到 33/33 Full Source Reviews。Conversational User Simulation survey 又完成 23/30 评分、v1 全文、
  taxonomy、evaluation、limitations/ethics 与 Ch61～63/71～74/77 邻接审计；现有 Ch62/71/73 已覆盖
  simulator identity、population/calibration、history/memory/drift/provenance，故为 No Change / Already Covered。
  Perceval 随后完成 26/30 评分、CVPR/arXiv v1、official code/checkpoints、token-span advantage、
  truncate/regenerate、evaluation/sensitivity 与 Ch28～30/62 邻接审计，暂定 Ch29 Experimental refine；PRM
  未做独立 span calibration，self-reported hallucination plateau 也不能证明没有 reward hacking。Turning TIDE
  又完成 26/30 评分、arXiv v1 全文/Appendix、official code/model/data、TIDAL/CompDemo/Reverse CALM、
  training/evaluation contract 与 Ch24～26/30/40 邻接审计，暂定 Ch25 Experimental refine；它没有证明 dLLM
  普遍优于 AR，单 H100 的受控 workload 中同尺寸 AR 反而更快。Step-level Optimization 随后完成 28/30
  评分、14-page PDF/HTML、三组完整 prompts、StepWise detector weights、event-driven cascade、evaluation 与
  Ch57～59/61～63/76～80 邻接审计，暂定 Ch77 Experimental refine；paper 未公开所称 hysteresis/bounded
  recovery 实现，overlapping-window split 也未说明是否按 trajectory 分组。InteractWeb-Bench 随后完成
  25/30 评分、v1 HTML/PDF、全部 prompts、project/repository/data、synthetic persona/user/judge contract 与
  Ch61～63/73～77 邻接审计；其 hidden-answer user、model-judged TCR/IAS/CHR 与 hallucination-outside-TCR
  边界不能支持真实用户或生产网站结论，现有 Ch62 已完整覆盖，故为 No Change / Already Covered。FlashRT
  又完成 28/30 评分、v1 全文/Appendix、current author code、white/black-box threat contract、selective
  recomputation、context-subsampled gradient、sensitivity 与 Ch22/49～51/67～69 邻接审计，暂定 Ch68
  Experimental refine；它说明 red-team compute/memory/attempt feasibility 与 approximation policy 必须进入
  evidence identity，却不能把四 H100/BF16/white-box 结果外推为通用 Serving 优化或 production risk。
  ReVSI 随后完成 28/30 评分、v1/v2 metadata、作者公开全文副本与相关 Appendices、ICML/OpenReview record、
  official repository/project/dataset 和 Ch61～63 邻接审计。其 observation-conditioned answerability 与
  evidence-removal counterfactual 暂定 refine Ch62；作者专家兼任 annotation/verification、5% visibility
  heuristic、mixed frame/FPS contracts、proprietary tiny subset、无独立 audit/CI 等边界不支持通用排行榜
  或 3D reasoning 结论。继续逐项回放 HF 全页又恢复 10 个确认在窗、此前未入账的 families：Visual
  Generation survey、Verifier-Based RL、Meta-CoT、FAMA、terminal task synthesis、reasoning
  controllability、Zero-to-CAD、step-level advantage selection、onchain agent controls 与 Semi-DPO。
  其中 Step-Level Advantage Selection 已完成 28/30 评分、v1 全文/Appendix、official VeRL artifact、
  short-context truncation 与 asymmetric advantage masking 机制、evaluation/ablation/overhead contract 和
  Ch28～30 邻接审计，暂定 Ch29 Experimental refine；AIME24 同时参与 checkpoint selection、单模型/单硬件、
  无独立 step-gold calibration 与无 training-seed CI 限制其外推。Semi-DPO 随后完成 27/30 评分、ICLR
  conference full text、Appendix 6.1～6.11、official project page、current 404 code boundary 与 Ch29～31
  邻接审计，暂定 Ch30 Experimental refine、Ch31 handoff。其 durable mechanism 是把 scorer committee、
  consensus partition、teacher checkpoint、timestep threshold 与 pseudo-label orientation 纳入 offline preference
  objective identity；3,992-pair set 进入 threshold control、committee/evaluation scorer 重叠、无 human audit/
  seeds/完整 SDXL recipe/可用 artifact 限制其外推。Onchain Operating-Layer Controls 随后完成 28/30
  评分、唯一 v1 全文/全部表图/Limitations/Appendix prompt template、官方 AgentVault/Core Contracts/
  whitepaper/Terms 与 Ch79～80 邻接审计，暂定 Ch80 Experimental refine、Ch68/77 handoff。其
  policy-valid submitted transactions 的 99.9% settlement 条件率不等于 rejection-inclusive mandate success、
  收益或安全；raw/replay traces、完整 runtime、SLO 与独立复现未公开。Visual Generation survey 随后完成
  24/30 评分、v1 全文、v2 revision metadata、作者 living-roadmap artifact 与 Ch61～63/Ch9～10/Ch38
  邻接审计。其长期价值是区分 perceptual、structural、executable 与 causal evidence，但 Ch62 与 Ch10 已有
  相同观点，故为 `No Change — Already Covered`；闭源 frontier architecture 和 silent verifier loop 是作者
  明确标注的猜想，selected qualitative cases 也不能证明排行榜或 causal mechanism。Edit-R1 又完成 arXiv
  v1 全文、公式/实验/prompts/appendices 与 OpenReview date/source-family reconciliation；同一九位作者和
  同一 principle decomposition、GCPO、RRM-guided GRPO 机制已于 2025-09-03 first-public，故移入 2025
  backlog，不计 W18 score。Meta-CoT 随后完成唯一 v1 主文、公式/算法、training/evaluation contract、
  公开 artifact surface 与 Ch25/27～30/62 邻接审计；26/30，暂定 Ch29 Experimental refine，Ch25/62
  short handoff。其 task/meta-task/target plan、CEC reward、early-timestep Flow-GRPO 与冻结 understanding
  expert 构成机制增量；但五类 primitive 的 basis/entropy 论证位于未能独立读取的 supplement，训练与
  evaluation 又高度依赖闭源 judges，不能外推为通用编辑 ontology 或可靠 reasoning。Compliance versus
  Sensibility 与 Zero-to-CAD 已在后续检查点完成全文、artifact/metadata 和章节邻接审计；FAMA 与
  Terminal Task Synthesis 的访问阻塞也已解除。FAMA 完成 v1 全文、四类 failure analyzer、orchestrator/
  helper-subset rerun、评测/开销与 Ch76/78/80 邻接审计，27/30，因 Ch78 已覆盖相同长期机制而为
  `No Change — Already Covered`。Terminal Task Synthesis 完成全文、Appendices、scenario-skill graph、
  inverse-frequency path sampling、constructor/verifier/repair、评测/消融与 Ch23/77/80 邻接审计，28/30，
  暂定 Ch23 Experimental refine；118,806-node giant component 与 82,073 scenario nodes 的 counting
  semantics 未披露，且无公开 artifact，不能外推。随后重新打开 official/infra
  source list，Kubernetes
  v1.36 controller staleness mitigation 完成官方设计、client-go v0.36.0 cache API 与 Ch53/54/63 邻接审计；
  27/30，暂定 Ch53 Version-Grounded refine。该证据只支持四类 built-in controllers 的 read-your-writes
  guard，不支持 global linearizability 或任意 custom controller 已受保护。Suspended Job mutable
  resources 随后完成 official blog、Jobs concept、feature-gate/API reference 与 Ch56/59/60 邻接审计；
  28/30，暂定 Ch56 Version-Grounded refine。它把资源 contract 细化为 execution 前受控协商、resume
  后冻结，但不证明减少 GPU 后训练拓扑、收敛、成本或 fairness 正确。Tiered Memory QoS 又完成
  feature Blog、Kubernetes QoS/resource/cgroup-v2、Linux kernel memory-controller docs 与 Ch59/63/67
  邻接审计；27/30，暂定 Ch67 Alpha/Version-Grounded refine。它将 request 映射为 hard/soft reclaim
  protection，并把 throttling 与 reservation 解耦；没有 workload benchmark，不能声称降低 OOM、提高
  utilization 或改善 latency。In-place Pod-level scaling 又完成 feature Blog、resize/status task docs 与
  Ch53/56/59 邻接审计；28/30，暂定 Ch53 Version-Grounded refine。它把 spec intent、node-admitted
  allocation 与 applied cgroup state 分层，不证明 recommendation 正确、无中断或优于 recreate。W18
  Pod-Level Resource Managers 随后完成 feature Blog、resource-manager/feature-gate docs 与
  Ch53/56/59 邻接审计；28/30，暂定 Ch59 Alpha/Version-Grounded refine。它把 aggregate Pod budget
  分解为 exclusive slices 与 shared remainder，并显式暴露 scope、quota、persistent pool、metrics 与
  checkpoint rollback contract；没有 workload benchmark，不能外推 ML throughput、tail latency 或
  utilization。Microsoft Research 固定源随后恢复 4 月 30 日 multi-agent network red-team，并完成
  official report、internal-platform setup、四类 network-only attack、qualitative emergent defense、
  mitigation/evidence boundary 与 Ch68/78/80 邻接审计；28/30，暂定 Ch78 Experimental refine。它证明
  指定环境中的 failure-mode existence，不给出普遍 attack rate、model ranking 或防御有效性。NVIDIA
  固定源又恢复 4 月 30 日 TileGym kernel-translation skill，并完成 official Blog、semantic mapping、
  static validator/CPU-reference test contract 与 Ch45/77 邻接审计；24/30，因 Ch77 已覆盖相同长期机制，
  为 `No Change — Already Covered`。repository 未独立核验，单次 GEMM 的耗时/token 不能外推。W18
  固定机构扫描随后恢复 xAI Custom Voices 与 ERNIE-5.1 Preview。Custom Voices 完成 4 月 30 日
  announcement、current API docs、两阶段 enrollment、team-scoped artifact lifecycle、证据边界和
  Ch67～69 邻接审计；24/30，暂定 Ch68 Version-Grounded refine，但没有公开 threshold、spoof/deepfake
  evaluation、human escalation 或 derived-artifact deletion proof。ERNIE Preview 只有同日 LMArena
  leaderboard announcement，15/30，保留为 Product/Leaderboard Fact，不借 5 月正式发布材料反向补写
  mechanism。Compliance versus Sensibility 随后完成作者公开全文、reasoning-conflict、probe/CAA
  intervention、judge validation、implementation 与 Ch16～18/27～28/62 邻接审计；26/30，暂定 Ch17
  Experimental refine，但不把 linear decodability 或窄任务 steering gain 外推为 deliberate reasoning choice。
  Zero-to-CAD 又完成作者公开全文、OpenReview/官方 dataset、distributed synthesis、三层 validation、
  bootstrapping evaluation、完整训练配置与 Ch22～24/61～63/76～78 邻接审计；28/30，暂定 Ch23
  Experimental refine。它支持 verifier-bounded executable synthetic programs 与受限 synthetic-to-program
  bootstrapping，不证明 DFM、真实设计意图或 matched dataset superiority。W18 随后从 Mistral 官方索引
  恢复 4 月 27 日 Workflows public preview；announcement、当前 workflow/activity/event/deployment/security
  docs 与 Ch76～80 已完成联合审计，28/30，结论为 `No Change — Already Covered` / Ch77。current docs
  不是 launch-day frozen snapshot，客户叙述也不是 reliability benchmark。Z.ai 官方固定源又恢复 4 月
  30 日 Scaling Pain incident report，并完成 PD abort/RDMA completion/KV reuse、HiCache read-before-ready、
  speculative anomaly telemetry、LayerSplit、evaluation contract 与 Ch19/44/50～52/63 邻接审计；29/30，
  暂定 Ch51 Version-Grounded refine。Amazon Science 固定源随后恢复 4 月 29 日 privacy-training-data
  reproduction，完成全文、related-primary entry points、三类 disclosure surfaces、DP/MPC layering、
  evidence limits 与 Ch63/67～69 邻接审计；24/30，因 Ch68 已完整覆盖，结论为 `No Change — Already
  Covered`。同一索引的 C3LLM 解读也联读 20 页 v3 论文，但 arXiv v1 为 2025-10-04，故转入 2025
  backlog，不在 W18 重复计分。PyTorch fixed-source pass 随后恢复 AutoSP 与 LightSeek-SMG：AutoSP
  已读 arXiv v1 全文、compiler graph rewrite、sequence-aware checkpoint min-cut、evaluation/ablation，
  28/30，暂定 Ch33 Experimental refine；LightSeek-SMG 已读完整官方 engineering report，核对 CPU/GPU
  ownership、gRPC、tokenizer cache、routing 与不完整 benchmark contract，27/30，暂定 Ch38 Experimental
  refine。两项 repository surface 均受当前权限限制，没有把作者实现声明当作独立核验事实。W18 在该中间检查点变为
  71 个 scored families、67 个 `20+` 且 67/67 Full Source Reviews；Google DeepMind 4 月 27 日韩国合作
  公告作为独立低分 Source Family 记录，不与 Google Research 5 月 1 日条目合并；首轮
  显式恢复的 4 个 Kubernetes resource-management families 已审。Broader Kubernetes index 的 7 个相邻
  条目也已完成跨周分流：Manifest Admission、Sharded List/Watch、DRA 归 W19，PSI 与 Workload-Aware
  Scheduling 归 W20，Agent Sandbox 归 W12，Gateway API v1.5 是 W09 release / W17 publication node；
  它们不计入 W18。当前已知 academic Full Review blockers 已解除；其他 title/date 与 fixed-source
  reconciliation 仍未闭合。OpenAI、Apple、Ai2、Mistral、DeepSeek、NVIDIA、
  Amazon、Cohere、Qwen Code 与 MiniMax 官方索引边界已经记录；其他具名机构、framework/RFC/PR 与
  academic cross-index 仍保持 Open。W18
  Discovery/Evidence Gate 保持打开；状态已同步到 W18 Weekly、
  年度索引与 Learning State，Books Gate 仍关闭。同步时重新逐表复算 W01～W30 当前六维评分行，发现
  旧年度 subtotal 漏计 later incremental scoring tables；加入 AutoSP 与 LightSeek-SMG 后
  该中间检查点为 927 rows（551 high / 336 mid / 40 low），
  这是档案账目修复，不表示任何未完成的 Evidence Gate 已通过。
  Microsoft Research/EuroSys cross-index 随后恢复 Concord。已阅读全文并核对 proceedings、DBLP/DOI、作者
  publication/news pages、CI flow、production evaluation 与 evidence boundary；但 2025-08 acceptance、
  Microsoft PDF 的 `2025/10` path 与 2026-04-27 formal publication 不能确定唯一 first-public date，故记为
  `2025 Backlog — Disputed First-public / W18 Formal-Publication Node`，不增加 W18 score row，也不修改 Books。
  第二轮 IBM Research fixed-source scan 又恢复 4 月 29 日 Granite 4.1 release；announcement 已全文读取，
  Language、Vision、Guardian、Embedding 与拆成 AR/Plus/NAR 的 Speech 被划分为 7 个 mechanism-level
  source-family reviews。Language 已完成
  official technical article、3B/8B/30B cards、8B config/history、training/evaluation 与章节邻接审计，24/30，
  暂定 Ch24 Version-Grounded refine；512K training exposure 与 131,072 released artifact contract 已拆分。
  Vision 也已完成 current card/config/history、ChartNet v1/dataset、八路 multi-depth/spatial feature
  injection、training/evaluation 与章节邻接审计，24/30，暂定 Ch17 Experimental refine；current 4.2M
  dataset 与 5～6 月 subsets 未倒写为 launch training manifest。Speech NAR 又完成 NLE sole-v1 全文、
  current card、CTC draft→interleaved slots→bidirectional editor→CTC collapse 状态流、matched AR/CTC
  evaluation、ablation/sensitivity/error/limitations 与 Ch38～41/44/62 邻接审计；27/30，暂定 Ch40
  Experimental refine。论文 NLE/NLE++ 与 current artifact 的 data/projector/LoRA/batch contracts 分开，
  不把 27× 外推为通用 latency 结论。Speech AR 也完成 current card、2025 predecessor architecture paper、
  W11 Self-Speculative paper、174K-hour data/task schema、dual-head/importance pooling/modality adapter、
  evaluation/safety/runtime 与 Ch5/17/38～40/44/62 邻接审计；26/30，暂定 Ch5 Experimental refine。
  4.1 artifact、earlier paper runs 与 current runtime examples 保持分离。Speech Plus 随后也完成 current
  card、SAA 与 In-Sync 两篇 related paper 的全文阅读，核对 relative-speaker/timestamp output grammar、
  conversation/prefix/client state、synthetic data lineage、baseline/ablation、malformed-output 与限制；26/30，
  暂定 Ch38 Experimental refine。当前 2B artifact 与两篇 8B paper 的 architecture、长度、timestamp encoding
  和 evaluation contracts 保持分离，incremental decode 也未被外推为 bounded-compute streaming。Guardian
  随后完成 current card/docs 与 2024 predecessor paper 全文，核对 policy/risk prompt grammar、score formula、
  human/synthetic data lineage、OOD/BYOC/function/RAG/JETTS evaluation、限制与 Ch62/68/69/77 邻接；
  26/30，暂定 Ch68 Version-Grounded refine。4.1 claims 未与前代训练 run 混写，thinking trace 与 vendor
  score 也未被升级为 calibrated safety guarantee。Embedding 随后完成 current artifact、完整后发论文、
  layer/vocabulary reduction、language-routed two-teacher distillation、512→4K retrieval training、long-context
  evaluation、per-language regression、runtime-dependent unpadding throughput 与 Ch22/45/62/72 邻接审计；
  27/30，暂定 Ch72 Version-Grounded refine。4 月 29 日 artifact 与 5 月 W20 paper 保持为两个时间节点，
  32K accepted length 未被写成 32K training/effective quality，runtime/library 变化也被纳入 retrieval identity。
  后续 fixed-source pass 完成 Kimi model-evolution 与 MiniMax model-release 日期边界核对，并从 Hugging Face
  Blog 补回 DeepInfra Inference Provider integration（19/30）与 NVIDIA/Siemens Raw2Insights-US
  investigational prototype（17/30）两个低分 families。两项均完成 source/date/rejection 核验，没有新增
  `20+` review 分母。framework release pass 随后补回 vLLM v0.20.0（29/30）与 Transformers v5.7.0
  （26/30）：前者完成 official release、stale request-slot、tenant cache salt、IR/kernel dispatch、HMA/offload/
  NIXL 与 Ch41～52 邻接审计，暂定 Ch46 Version-Grounded refine；后者完成 release、长生成 PR #45530、
  tag-pinned Continuous Batching API/architecture 与同一章节区间审计，暂定 Ch42 Version-Grounded refine。
  独立页面不可访问的 PR 只按 release/docs 级事实记录；SGLang v0.5.10 按 4 月 6 日回到 W15。
  该 framework checkpoint 结束时，W18 为 75 scored families（53 high / 16 mid / 6 low），69/69
  `20+` Full Source Reviews。随后逐日重放 Hugging Face 2026-04-27～05-01 pages，证明此前 weekly-page
  discovery 仍漏候选。Diffusion Templates 已完成唯一 v1 全文、template cache/model/pipeline/training、
  11 类 model-zoo、evidence boundary 与 Ch54～56 邻接审计；28/30，暂定 Ch55 Experimental refine，
  Ch26/45 short handoff。作者唯一约 `1.8x` editing speedup 没有硬件、dtype、resolution、并发或 SLO
  contract，未被外推。Refinement via Regeneration 随后完成唯一 v1、官方 current repository/inferencer/
  model card、experiments/ablations 与 Ch22～24 邻接审计；27/30，暂定 Ch23 Experimental refine，Ch25/62
  handoff。作者结果只绑定 BAGEL/H800/training-mix/50-step CFG contract，没有外推为 identity/locality、
  multi-round convergence 或 production-cost 结论。Mutual Forcing 又完成唯一 v1、全部 method/experiments/
  appendices、official project、demo-only current repository 与 Ch24～26 邻接审计；28/30，暂定 Ch25
  Experimental refine，Ch38/40 handoff。4/8 NFE、25 秒和 FPS 只保留为作者 workload evidence，online fake
  model 也没有被“teacher-free”标签隐去。W18 当前更新为 78 scored families（56 high / 16 mid /
  6 low），72/72 当前 `20+` Full Source Reviews。Co-Director 又完成唯一 v1、全部 method/evaluation/
  appendices/prompts、current official code 与 Ch62/76～78 邻接审计；27/30，`No Change — Already Covered` /
  Ch77。T=4 MAB 只保留作者 workload evidence；judge-generated factored reward 与 prompt 的 forced
  strategic/execution correlation 未被写成 causal credit。W18 当前更新为 79 scored families（57 high / 16 mid /
  6 low），73/73 当前 `20+` Full Source Reviews。MAIC-UI 随后完成唯一 v1、全部 method/evaluation/
  appendices、current official implementation 与 Ch62/76～78 邻接审计；28/30，`No Change — Already
  Covered` / Ch77。current code 支持 citation-to-line、full-context prompt 与 diff-first fallback 的存在；
  full-system lab study 未隔离组件贡献，单校 observational deployment 也不能证明因果学习收益。W18 当前
  更新为 80 scored families（58 high / 16 mid / 6 low），74/74 当前 `20+` Full Source Reviews。GoClick
  随后完成唯一 v1、全部 method/evaluation/limitations、current official repository/model/data/eval surfaces
  与 Ch10/23/62/74～78 邻接审计；28/30，暂定 Ch10 Experimental refine，Ch23/62/75/78 handoff。L20、
  batch 1、BF16 的 latency 与 frozen-trajectory Step SR 只保留为作者 workload evidence，不外推真实 device
  SLO 或 online task success。W18 当前更新为 81 scored families（59 high / 16 mid / 6 low），75/75 当前
  `20+` Full Source Reviews。AutoGUI-v2 随后完成唯一 v1、51 页主文/Appendix、current official repository、
  公开 dataset surfaces 与 Ch61～63/75/77 邻接审计；27/30，`No Change — Already Covered` / Ch62。该
  static suite 能分离 appearance、intent、function 与 single-step outcome，但不执行 action，也不测 multi-step
  planning、environment transition 或 task success。W18 当前更新为 82 scored families（60 high / 16 mid /
  6 low），76/76 当前 `20+` Full Source Reviews。X-WAM 随后完成 v1 全文/Appendix、项目页、current
  later-release code/checkpoint/data boundary、evaluation contract 与 Ch9～10/20/38/62 邻接审计；28/30，
  暂定 Ch10 Experimental refine。ANS 支持不同模态 deadline 使用不同 completion schedule，但 predicted
  RGB-D 不等于 causal world state，6 月才公开的 artifact 也不能倒写为 W18 同步发布。W18 当前更新为
  83 scored families（61 high / 16 mid / 6 low），77/77 当前 `20+` Full Source Reviews。ExoActor 随后完成
  唯一 v1 的 case/failure/ablation/latency/discussion、Appendix prompts、项目页与 404 code boundary、
  Ch9～10/38/62/75/77 邻接审计；24/30，`No Change — Already Covered` / Ch10。它支持 modular
  representation handoff 与 error amplification，却没有任务/trial denominator、success rate、uncertainty 或
  可复现 artifact，不能证明普遍 zero-shot humanoid control。W18 当前更新为 84 scored families（61 high /
  17 mid / 6 low），78/78 当前 `20+` Full Source Reviews。Representation Fréchet Loss 随后完成唯一 v1、
  全部 appendices、current official repository surface、population estimator、evaluation contract 与 Ch23～25/62
  邻接审计；29/30，暂定 Ch62 Experimental refine。它支持 population-estimation 与 gradient window 解耦，
  同时暴露 stale Queue/EMA state 与 scorer-as-loss 的 Goodhart surface；缺少硬件/成本合同，不外推 FD-SIM 或
  one-step 的通用优势。W18 当前更新为 85 scored families（62 high / 17 mid / 6 low），79/79 当前 `20+`
  Full Source Reviews；年度 provisional ledger 为 941 rows（562 high / 337 mid / 42 low）。ElementsClaw 经官方 arXiv submission history 核验为
  4 月 26 日 W17 v1、4 月 29 日 W18 v2
  revision node 与 5 月 4 日 v3，故不在 W18 重复计分，留待 W30 forward sweep 后回补 W17。recovered
  denominator 仍未冻结：ViPO 与 Safety Drift 两个已确认在窗 families 因当前 browser permissions 拒绝
  arXiv primary text 与 author-artifact discovery 而标记 `Unverified / Blocked Backlog`，未评分且不计入 Full Review；另有若干 page hits
  待 primary-date reconciliation。How Much Is One Recurrence Worth 按 4 月 22 日 v1 归 W17，4 月 27 日
  v2 只作 W18 revision node。用户于 2026-08-11 明确授权将两项暂记 blocked 后跳过，因此 forward cursor
  移入 W19；W18 Historical Evidence Gate 与 Historical Books Gate 仍保持关闭，Books 未修改，blocked items
  与 discovery gaps 留待 post-forward backlog sweep。

## Open Questions

1. Monday arXiv listing 是否会补录 8 月 7 日之后 first-public 的论文？
2. W32 缺失的 2026-08-09 Daily 与 Sunday Weekly 应如何在不伪造逐日覆盖的前提下补齐？
3. 搜索索引中日期不一致的工程 release，能否由 signed tag、release API 或 changelog 交叉确认？
4. 恢复 primary-source 只读访问后，ViPO 与 Safety Drift 的全文、artifact、日期/revision、评分与章节邻接
   审计会形成什么 disposition？其他尚未完成日期核验的 page hits 哪些应进入 W18、低分拒绝或 earlier-week
   spillback？
5. Refinement via Regeneration 能否提供 independent evaluator、样本级 provenance、multi-seed variance、
   matched-compute RvE comparison、identity/locality/safety human evaluation 与多轮 stop/rollback contract？
6. Mutual Forcing 何时公开 code/checkpoint/frozen data-eval manifest？online fake model、Multi/Few mode、
   context buffer 与 recovery point 怎样共同持久化；matched hardware/resolution 与长于 25 秒结果能否复现？
7. Co-Director 的 immutable dataset/run manifest、independent judge、axis-interaction ablation 与 multi-seed/
   cost-matched T sweep 能否公开？取消 strategic/execution score 强制同向后，factored-MAB 增益是否仍成立？
8. AutoGUI-v2 能否公开 immutable paper-run manifest、element-captioning dataset、human agreement、independent
   question audit、contamination 与 repeated-run uncertainty，并验证 static functionality 是否预测 interactive
   outcome？
9. X-WAM 能否公开 event-time immutable artifact、v1/v2 semantic diff、完整 latency contract、multi-seed
   uncertainty 与 matched-compute 专用 baselines？在 history/KV、causal intervention、action cancellation 与
   独立 real-robot replication 下，ANS 和 predicted RGB-D 的长期结论是否仍成立？
10. ExoActor 能否公开 official code/data/run manifest、完整 task/trial denominator、success/failure rubric、
    hardware/network/video contract 与 independent audit？移除 target support、加入 streaming feedback 与
    perturbation recovery 后，imagined-demo interface 是否仍能转化为安全、可执行动作？

## Sources

- Diffusion Templates metadata/revision: https://arxiv.org/abs/2604.24351
- Diffusion Templates HTML v1: https://arxiv.org/html/2604.24351v1
- Refinement via Regeneration metadata/revision: https://arxiv.org/abs/2604.25636
- Refinement via Regeneration HTML v1: https://arxiv.org/html/2604.25636v1
- Refinement via Regeneration official repository: https://github.com/LeapLabTHU/RvR
- Refinement via Regeneration official inferencer:
  https://raw.githubusercontent.com/LeapLabTHU/RvR/main/inferencer.py
- Refinement via Regeneration current model card: https://huggingface.co/JiayiGuo821/RvR-7B-MoT
- Mutual Forcing metadata/revision: https://arxiv.org/abs/2604.25819
- Mutual Forcing HTML v1: https://arxiv.org/html/2604.25819v1
- Mutual Forcing official project page: https://mutualforcing.github.io/
- Mutual Forcing current official repository: https://github.com/HVision-NKU/MutualForcing
- Co-Director metadata/revision: https://arxiv.org/abs/2604.24842
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
- How Much Is One Recurrence Worth? metadata/revisions: https://arxiv.org/abs/2604.21106
- OpenAI Research index: https://openai.com/news/research/
- Anthropic News: https://www.anthropic.com/news
- Google Research Blog: https://research.google/blog/
- Google DeepMind, Republic of Korea partnership (2026-04-27):
  https://deepmind.google/blog/announcing-our-partnership-with-the-republic-of-korea/
- Hugging Face Blog: https://huggingface.co/blog
- Hugging Face, DeepInfra on Inference Providers (2026-04-29):
  https://huggingface.co/blog/inference-providers-deepinfra
- NVIDIA / Siemens Healthineers, NV-Raw2Insights-US (2026-04-28):
  https://huggingface.co/blog/nvidia/raw2insights-adaptive-ultrasound-imaging
- Kimi official model-evolution timeline:
  https://www.kimi.com/help/agent/agent-overview
- MiniMax official model release notes:
  https://platform.minimax.io/docs/release-notes/models
- arXiv cs.AI recent: https://arxiv.org/list/cs.AI/recent
- arXiv cs.CL recent: https://arxiv.org/list/cs.CL/recent
- arXiv cs.LG recent: https://arxiv.org/list/cs.LG/recent
- vLLM releases: https://github.com/vllm-project/vllm/releases
- vLLM v0.20.0: https://github.com/vllm-project/vllm/releases/tag/v0.20.0
- vLLM stale request-slot fix: https://github.com/vllm-project/vllm/pull/39833
- vLLM LMCache `cache_salt` isolation: https://github.com/vllm-project/vllm/pull/39837
- vLLM IR skeleton: https://github.com/vllm-project/vllm/pull/33825
- Hugging Face Transformers v5.7.0:
  https://github.com/huggingface/transformers/releases/tag/v5.7.0
- Transformers long-generation Continuous Batching PR:
  https://github.com/huggingface/transformers/pull/45530
- Transformers v5.7.0 Continuous Batching architecture:
  https://huggingface.co/docs/transformers/v5.7.0/en/continuous_batching_architecture
- SGLang releases: https://github.com/sgl-project/sglang/releases
- PyTorch releases: https://github.com/pytorch/pytorch/releases
- KServe releases: https://github.com/kserve/kserve/releases
- xAI Custom Voices announcement: https://x.ai/news/grok-custom-voices
- xAI Custom Voices current docs:
  https://docs.x.ai/developers/model-capabilities/audio/custom-voices
- Baidu ERNIE Blog index: https://ernie.baidu.com/blog/posts/
- Compliance versus Sensibility: https://arxiv.org/abs/2604.27251
- Compliance versus Sensibility author-public full text:
  https://www.researchgate.net/publication/404333039_Compliance_versus_Sensibility_On_the_Reasoning_Controllability_in_Large_Language_Models
- Zero-to-CAD: https://arxiv.org/abs/2604.24479
- Zero-to-CAD author-public full text:
  https://www.researchgate.net/publication/404249340_Zero-to-CAD_Agentic_Synthesis_of_Interpretable_CAD_Programs_at_Million-Scale_Without_Real_Data
- Zero-to-CAD official 100K dataset: https://huggingface.co/datasets/ADSKAILab/Zero-To-CAD-100k
- PyTorch, Introducing AutoSP: https://pytorch.org/blog/introducing-autosp/
- AutoSP arXiv HTML v1: https://arxiv.org/html/2604.27089v1
- PyTorch, LightSeek-SMG: https://pytorch.org/blog/lightseek-smg/
- IBM Research, Granite 4.1 release:
  https://research.ibm.com/blog/granite-4-1-ai-foundation-models
- Granite Speech 4.1 2B AR current model card:
  https://huggingface.co/ibm-granite/granite-speech-4.1-2b
- Granite-speech predecessor paper: https://arxiv.org/abs/2505.08699
- Granite-speech predecessor HTML v2: https://arxiv.org/html/2505.08699v2
- Self-Speculative Decoding for LLM-based ASR: https://arxiv.org/abs/2603.11243
- Self-Speculative Decoding HTML v1: https://arxiv.org/html/2603.11243v1
- Granite Speech 4.1 2B NAR current model card:
  https://huggingface.co/ibm-granite/granite-speech-4.1-2b-nar
- NLE arXiv metadata and sole-v1 history: https://arxiv.org/abs/2603.08397
- NLE arXiv HTML v1: https://arxiv.org/html/2603.08397v1
- Granite Speech 4.1 2B Plus current model card:
  https://huggingface.co/ibm-granite/granite-speech-4.1-2b-plus
- Speaker-attributed ASR metadata: https://arxiv.org/abs/2604.11269
- Speaker-attributed ASR PDF v1: https://arxiv.org/pdf/2604.11269
- In-Sync timestamp metadata: https://arxiv.org/abs/2604.22817
- In-Sync timestamp PDF v1: https://arxiv.org/pdf/2604.22817
- Granite Guardian 4.1 official docs: https://www.ibm.com/granite/docs/models/guardian
- Granite Guardian 4.1 8B current model card:
  https://huggingface.co/ibm-granite/granite-guardian-4.1-8b
- Granite Guardian predecessor paper: https://arxiv.org/abs/2412.07724
- Granite Guardian predecessor HTML: https://arxiv.org/html/2412.07724
- Granite Embedding 97M Multilingual R2 current model card:
  https://huggingface.co/ibm-granite/granite-embedding-97m-multilingual-r2
- Granite Embedding Multilingual R2 paper metadata/revisions: https://arxiv.org/abs/2605.13521
- Granite Embedding Multilingual R2 HTML v1: https://arxiv.org/html/2605.13521v1
- Granite Embedding models repository: https://github.com/ibm-granite/granite-embedding-models
- Kubernetes v1.36 controller staleness mitigation:
  https://kubernetes.io/blog/2026/04/28/kubernetes-v1-36-staleness-mitigation-for-controllers/
- client-go v0.36.0 cache package: https://pkg.go.dev/k8s.io/client-go@v0.36.0/tools/cache
- Kubernetes v1.36 resource-management blog index: https://kubernetes.io/blog/page/3/
- Mutable Pod Resources for Suspended Jobs:
  https://kubernetes.io/blog/2026/04/27/kubernetes-v1-36-mutable-pod-resources-for-suspended-jobs/
- Kubernetes Jobs concept: https://kubernetes.io/docs/concepts/workloads/controllers/job/
- Tiered Memory Protection with Memory QoS:
  https://kubernetes.io/blog/2026/04/29/kubernetes-v1-36-memory-qos-tiered-protection/
- Linux kernel cgroup v2 memory controller: https://docs.kernel.org/admin-guide/cgroup-v2.html
- In-Place Vertical Scaling for Pod-Level Resources:
  https://kubernetes.io/blog/2026/04/30/kubernetes-v1-36-inplace-pod-level-resources-beta/
- Resize CPU and memory resources assigned to Pods:
  https://kubernetes.io/docs/tasks/configure-pod-container/resize-pod-resources/
- Operating-Layer Controls for Onchain Agents: https://arxiv.org/abs/2604.26091
- Visual Generation in the New Era: https://arxiv.org/abs/2604.28185
- Visual Generation HTML v1: https://arxiv.org/html/2604.28185v1
- Visual Generation official living roadmap: https://github.com/EvolvingLMMs-Lab/Evolving-Visual-Generation
- Visual Generation stress-test artifact:
  https://raw.githubusercontent.com/EvolvingLMMs-Lab/Evolving-Visual-Generation/main/docs/stress_tests.md
- Verifier-Based RL in Image Editing: https://arxiv.org/abs/2604.27505
- Verifier-Based RL in Image Editing HTML v1: https://arxiv.org/html/2604.27505v1
- Edit-R1 first-public OpenReview record: https://openreview.net/forum?id=hKWCGxuD5v
- FAMA metadata: https://arxiv.org/abs/2604.25135
- FAMA HTML v1: https://arxiv.org/html/2604.25135v1
- Terminal Task Synthesis via Skill Graphs metadata: https://arxiv.org/abs/2604.25727
- Terminal Task Synthesis HTML v1: https://arxiv.org/html/2604.25727v1
- Terminal Task Synthesis PDF: https://arxiv.org/pdf/2604.25727
- DX Terminal Pro Agent Vault Contract API:
  https://docs.terminal.markets/docs/resource-section/agent-vault-contract-api/
- DX Terminal Pro Core Contracts:
  https://docs.terminal.markets/docs/resource-section/core-contracts/
- Mistral Workflows announcement: https://mistral.ai/it/news/workflows/
- Mistral Workflows documentation:
  https://docs.mistral.ai/studio-api/workflows/getting-started/overview
- Z.ai Scaling Pain of Coding Agent Serving: https://z.ai/blog/scaling-pain
- Z.ai GLM-5 release/workload context: https://z.ai/blog/glm-5
- OpenAI Research release index: https://openai.com/research/index/release/
- Apple Machine Learning Research ICLR 2026 index:
  https://machinelearning.apple.com/research/iclr-2026
- Ai2 News index: https://allenai.org/news
- DeepSeek API changelog: https://api-docs.deepseek.com/updates/
- NVIDIA Dynamo tag index: https://developer.nvidia.com/blog/tag/nvidia-dynamo/
- Amazon Science privacy-training-data reproduction:
  https://www.amazon.science/blog/preserving-the-privacy-of-ai-training-data
- Amazon Science C3LLM explanation: https://www.amazon.science/blog/how-catastrophic-is-your-llm
- C3LLM arXiv metadata: https://arxiv.org/abs/2510.03969
- Microsoft Research, Concord publication page:
  https://www.microsoft.com/en-us/research/publication/concord_learning_network_configuration_contracts/
- Concord full PDF:
  https://www.microsoft.com/en-us/research/wp-content/uploads/2025/10/eurosys26-spring-final215.pdf
- EuroSys 2026 papers: https://2026.eurosys.org/papers.html
- DBLP EuroSys 2026: https://dblp.org/db/conf/eurosys/eurosys2026
- MAIC-UI arXiv metadata: https://arxiv.org/abs/2604.25806
- MAIC-UI HTML v1: https://arxiv.org/html/2604.25806v1
- MAIC-UI official implementation: https://github.com/THU-MAIC/MAIC-UI
- GoClick arXiv metadata: https://arxiv.org/abs/2604.23941
- GoClick arXiv PDF v1: https://arxiv.org/pdf/2604.23941
- GoClick official repository: https://github.com/ZJULiHongxin/GoClick
- GoClick-Large model card: https://huggingface.co/HongxinLi/GoClick-Large
- GoClick-Base model card: https://huggingface.co/HongxinLi/GoClick-Base
- AutoGUI-v2 arXiv metadata/revision: https://arxiv.org/abs/2604.24441
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
