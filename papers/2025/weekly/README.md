# 2025 Weekly Research Index

> Coverage: 2025-W01～2025-W52
> Calendar Window: 2024-12-30～2025-12-28
> Backfilled: 2026-07-31
> Weekly Rebuild Started: 2026-08-17
> Research Mode: Retrospective Discovery and Evidence Rebuild
> Current Status: `Paused after 2025-W41 Reclosure — Next Forward Week: 2025-W42`
> Books Integration: `Deferred — existing decisions are legacy/provisional input`

## Archive Contract

- 使用 ISO week-year 和完整 Monday～Sunday。2025-W01 包含 2024-12-30～2025-01-05；
  2025-12-29～12-31 属于现有 2026-W01，不在本年度重复。
- 历史回填只生成 Weekly，不补造 Daily；事件日期、first-public date、来源和 evidence
  boundary 直接保留在对应周。
- 模型 release、paper v1、model card 与后续工程集成按不同证据角色记录；同一技术只形成一个
  Books source packet。
- Google Scholar、OpenAlex、DBLP 用于每日 discovery 和去重；Crossref 用于 Weekly
  metadata 交叉检查；机制结论回到 primary source。
- 当前 75 个评分条目只是旧版 discovery seed，不是年度候选召回已经闭合的证明。2026-08-17
  起按 2026 最后一轮历史 Weekly 标准重新扫描 W01～W52；候选总数、分数区间与 Full Source
  Review 分母只在逐周 replay 完成后重新计算。
- 本阶段只修复 Weekly evidence，不创建历史 Daily、不修改 Books，也不作新的 `Integrate / Refine /
  No Change` 判断。已完成 Weekly 证据的候选统一进入 `Books Pending — Integration Deferred`。

## Coverage Map

| Weeks | Calendar Window | Main Evidence Cluster |
| --- | --- | --- |
| W01～W05 | 2024-12-30～2025-02-02 | reasoning RL、hybrid/linear attention、test-time scaling、vLLM V1、research agents |
| W06～W13 | 2025-02-03～2025-03-30 | KV-constrained scheduling、native sparse attention、speculative decoding、Dynamo、interpretability/privacy |
| W14～W20 | 2025-03-31～2025-05-18 | multimodal/MoE model families、hybrid reasoning、compiler/runtime evolution、evaluator-driven agents、RAG sufficiency |
| W21～W26 | 2025-05-19～2025-06-29 | Kubernetes-native distributed inference、KServe/Gateway、user-level DP、long-reasoning co-design |
| W27～W33 | 2025-06-30～2025-08-17 | Kimi/GLM/Qwen agentic models、MTP/SpecForge、open-weight reasoning 与 safety |
| W34～W40 | 2025-08-18～2025-10-05 | hybrid model contracts、Kubernetes DRA、dual sparsity、NSA→DSA productization |
| W41～W46 | 2025-10-06～2025-11-16 | symmetric memory、policy-as-data safety、TPU backend portability、distributed DP runtime |
| W47～W52 | 2025-11-17～2025-12-28 | pipeline fusion、DeepSeek-V3.2、test-time memory、private telemetry、speculative artifact lifecycle |

## Cross-Week Evolution Routes

### Reasoning Training and Runtime Policy

```text
W04 DeepSeek-R1 / Kimi k1.5: outcome reward 与长 rollout
→ W05 s1: inference budget 也能成为能力杠杆
→ W09 Claude 3.7 / W18 Qwen3: thinking 与 non-thinking 合并为同一模型 contract
→ W16 o3/o4-mini: reasoning 中选择工具
→ W25 MiniMax-M1: attention architecture 与 RL rollout cost 联合设计
→ W34 DeepSeek-V3.1 / W49 V3.2: thinking state 进入 tool-use runtime
```

这条路线不是“RL 替代 SFT”。R1-Zero 暴露了纯 outcome optimization 的可读性边界，R1 的
cold start 与多阶段 pipeline 说明 SFT、筛选和偏好训练仍承担行为约束。后续 hybrid models
把训练收益转化为运行时 mode、reasoning budget、parser 与 capacity-planning 问题。

### Long Context and Memory

```text
W01 Titans: test-time neural memory
→ W03 MiniMax-01: hybrid linear/softmax attention
→ W07 Native Sparse Attention: trainable + hardware-aligned sparsity
→ W16 MIRAS: memory architecture / bias / retention / optimizer 设计空间
→ W25 MiniMax-M1: long context 与 long-reasoning RL co-design
→ W37 Qwen3-Next: hybrid attention + sparse MoE + MTP
→ W40 DeepSeek-V3.2-Exp: DSA 进入可服务模型
→ W49 DeepSeek-V3.2: sparse attention + tool reasoning
→ W49 Google Research synthesis: 对 W01/W16 的机构级解释与证据补强
```

这些分支解决不同问题：linear/recurrent state 控制随长度增长的成本，sparse attention 保留
选择性精确访问，test-time memory 允许在线更新参数化状态。它们分别引入压缩损失、稀疏
index/kernel 复杂度以及污染、遗忘、回滚和 session ownership。

### Speculative Decoding as an Artifact Lifecycle

```text
W10 EAGLE-3: draft architecture 与 training-time test
→ W29 SGLang MTP: draft/verify 进入 PD + EP runtime
→ W30 SpecForge: draft training 成为独立系统
→ W52 SpecBundle: target-specific draft weights 成为 versioned serving artifact
```

演进压力从“能否预测多个 token”转为 acceptance、verification cost、batch shape、训练数据、
target/draft compatibility、provenance 与持续重训。新工具链不改变 speculative decoding 在
高并发或低接受率场景可能失效的基本 trade-off。

### Distributed Inference Control Plane

```text
W05 vLLM V1: 单 engine 内统一 request/scheduler/execution state
→ W12 Dynamo: planner、router、KV transfer 与 telemetry
→ W21 llm-d: vLLM data plane + Kubernetes-native distributed stack
→ W22 KServe v0.15: multi-node/KV/autoscaling 进入声明式 API
→ W23 Gateway API Inference Extension: InferenceModel/Pool 与 endpoint selection
→ W35～W38 DRA: accelerator allocation、sharing 与 health 进入平台资源语义
```

单机 runtime、分布式 inference runtime、serving control plane、gateway 和 device scheduler
是分层依赖，不是互相替代。每上移一层都会获得更全局的决策信息，也会新增 freshness、
ownership、failure recovery、API lifecycle 与跨组件兼容性成本。

### Privacy from Algorithm to Operational Evidence

```text
W12 inference-time DP synthetic data
→ W21 user-level DP fine-tuning
→ W46 JAX-Privacy: clipping/noise/accounting/auditing 的 distributed runtime
→ W23 Urania paper / W50 Google Research follow-up: privacy-preserving usage telemetry
```

四个节点保护的 object 不同：query/record、user contribution、training pipeline、aggregate
usage insight。不能用“采用 DP”代替 privacy unit、threat model、epsilon/delta、accounting
和 utility boundary。

## 2025 Weekly Rebuild Gate

当前状态：`Discovery/Evidence Rebuild In Progress / Books Integration Deferred`。

当前只确认了以下结构事实：52 个 ISO Weekly 目录连续覆盖 2024-12-30～2025-12-28，旧版总账
包含 75 个评分条目。它们不能证明 fixed-source discovery、academic cross-index、revision、spillback
或所有 `20+` Full Source Review 已经闭合。W01～W52 将严格单向重放；每周只有完成来源召回、
日期归属、Source Family 去重、评分、全文或明确 blocked ledger 后，才通过该周 Candidate Evidence
Gate。存在 blocked 项可以继续 forward cursor，但年度 Archive Completion Gate 保持 Open。

Forward cursor checkpoint（2026-08-22）：`W04/W09/W10 Passed；W11 canonical-owner reconciliation Reopened；W12～W20 Discovery/Re-audit In Progress`。W12当前文件可复算43项owner identities：22项已完成Full Source Review，21项spillback仅完成identity/date核验，blocked为0。W13已校准为60个owner identities：47项20+、13项低分，另有3个related-evidence node；46/47项20+完成全文与strict schema，只有RLHF Data Scaling仍为Review Pending，13/13低分闭合，blocked为0。W14校准为46个owner identities：42项20+、4项低分；42/42项20+完成全文与strict schema，4/4低分闭合，ordinary pending与blocked均为0。ACTalker与WikiVideo的实现artifact缺口、OpenCodeReasoning artifact drift及SkyReels-A2 disputed ablation均保留为证据边界；AGI Safety报告没有Appendix，第108～145页均为References。W15校准为28个owner identities：21项20+、7项低分，另有3项跨周related/spillback node；20/21项20+完成strict schema，A2A事件时spec为唯一ordinary pending，7/7低分闭合，blocked/disputed为0。W16的39项lower-bound账本已写回：38项20+、1项低分，5/38 strict Full Review、33项Review Pending。W18已重建为36项owner：31项20+、5项低分，30/31 strict Full Review，PIPA pending、VideoHallu disputed，且7项前置spillback仍待评分/全文；UQLM已由W28回拨并闭合。W19已从错误空周重建为25项lower-bound：24项20+、1项低分，4/24 strict Full Review、20项pending。W11因Gemini Robotics与Cyberattack Capability Framework两个canonical owner回拨而重新打开。年度Archive Completion Gate与Historical Books Gate关闭。

Superseding forward checkpoint（2026-08-24）：W12已收束为107个W12 owners（95 strict、6 low、6 Unverified/Blocked，ordinary Review Pending 0，Evidence Gate因六项明确source blocker保持Open，另有4项按v1回拨W11）；W15已通过root Review并写回41个scored owners（34个20+ strict、7个低分闭合，ordinary Pending/Blocked/Disputed 0；Discovery/Archive Gate仅因cross-index export与A2A event-time tree保持Conditional Open）；W16的50-row六维评分总账已补齐并由root复算通过（21 high、25 medium、4 low，46/46 retained packet、4/4 low closure，ordinary Review Pending 0）；Codex CLI P2 Artifact Blocked与ReZero P3 Revision Disputed均有精确材料请求，因此Candidate Evidence Gate与Discovery/Archive Gate保持Conditional Open；W17经root复核闭合发现与80-row账本（22 high、44 medium、14 low，61/66 retained strict、14/14 low，ordinary Pending 0），CameraBench等5项拥有精确P1材料请求，因此Candidate Evidence Gate保持Not Passed但forward cursor可继续；W18经root复核闭合为43项（18 high、18 medium、7 low，36/36 retained strict、7/7 low，Pending/Blocked为0，VideoHallu保留source-complete terminal Disputed），Candidate Evidence Gate通过且Archive Gate因immutable cross-index export保持Conditional；W19经root复核闭合为27项（14 high、12 medium、1 low，26/26 retained strict、1/1 low，Pending/Blocked/Disputed均为0），Discovery与Candidate Evidence Gate通过；W20以81个owners通过Candidate Evidence Gate；W21经root独立复算后闭合为127个owners（60 high、56 medium、11 low，116/116 retained strict、11/11 low，Review Pending 0，五项revision dispute均冻结event-time边界），Candidate Evidence Gate通过；账外P0 identity gap `Teaching Models to Lie` 使Discovery/Archive Completion保持Conditional；W22已通过root Review并写回85个owners（47 high、36 medium、2 low，83/83 retained strict、2/2 low，Pending/Blocked/Disputed 0），Candidate Evidence Gate与Discovery Replay Gate均通过。Annual Archive Completion Gate与Historical Books Gate继续关闭。

W25 forward checkpoint（2026-08-22）：旧2项已扩展为40个owner identity lower-bound，35项达到20+，其中11项strict Full Source Review、24项Review Pending；5项低分全部闭合，Blocked与family-level Disputed为0。AceReason-Nemotron 1.1与Guru各保留numerical subclaim dispute；RLVR Correct Reasoning、Reasoning with Exploration已按Pass@K/CoT-Pass@K measurement boundary闭合。CRITICTOOL与FedNano按v1日期回拨W24；fixed-organization、cross-index与06-19～22 replay仍有Discovery Gap，因此W25 Candidate Evidence Gate保持Not Passed，Historical Books Gate关闭。

W23 superseding correction（2026-08-24）：对原43-row账本的遗漏复核已闭合。Saffron-1（`2506.06444`）、Astra（`2506.06205`）、Cartridges（`2506.06266`）、ConfQA（`2506.07309v1`；当前v2改名ConfRAG）、ECoRAG（`2506.05167`）与Bootstrapping World Models（`2506.06006`）均已回拨并完成Full Source Review；最终账本为49项（34 high、11 medium、4 low），45/45 retained strict与4/4 low均闭合，Review Pending与Blocked均为0。ConfQA→ConfRAG作为revision-lineage Disputed终态保留；`Comment on The Illusion of Thinking`（`2506.09250`）归W24且未在W23重复计分。W23 Candidate Evidence Gate通过，年度Archive Completion与Historical Books Gate继续关闭。

W26 forward checkpoint（2026-08-22）：错误的空周结论已重建为44个scored owner family；33项25～30分、7项20～24分、4项低分。40/40 retained candidates已完成strict Full Source Review，4/4低分完成来源/日期/评分/拒绝闭合，Review Pending、Blocked与Disputed均为0。相邻工程release已按官方日期回拨W22、W24或W25。W26 Candidate Evidence Gate通过，但年度Archive/Discovery Gate与Historical Books Gate仍关闭。

W27 superseding checkpoint（2026-08-24）：W28中RAT、GradOT、S³与DP-Fusion按2025-07-06 v1日期回拨后，W27最终为41个scored owners（19 high、18 medium、4 low）；root复算41/41六维Total并核对36个source-complete retained packets、1个精确P1 Full-text Blocked和4/4低分closure。普通Review Pending为0；MARVIS `2507.01544v1`缺事件时全文，已有可接受材料与补审范围。Candidate Evidence Gate按blocked-skip为Conditional Pass，年度Archive/Discovery Recall与Historical Books Gate继续Open/Closed。

W24 superseding checkpoint（2026-08-24）：已写回账本从旧1项扩展为163个scored owner；119项25～30分、33项20～24分、11项低分。152项retained中151项完成source review；Institutional Books 1.0保持`Review Pending — Full Text Blocked`。Illusion of Thinking短评的4页v1已全文复核并以`Disputed — Source Complete / Artifact Not Released`闭合，不把缺raw outputs误记为论文未读。11/11低分闭合，其中SFT→ICL理论稿为`Disputed / Reject`。fixed-org replay新增AWS Bedrock Qwen import、Adobe/Gardenia workflow、E.ON/Nova multimodal cases、Nemotron AWS availability与Bedrock billing taxonomy；KServe #4520/#4525合并为同一CRD/HTTPRoute family。fixed-org/HF/cross-index recall仍Open，archive/discovery completion和Historical Books Gate均不开放。

W29 superseding checkpoint（2026-08-22）：旧1项账本已扩展为35个scored owner lower-bound；22项25～30分、11项20～24分、2项低分。32/33 retained完成strict Full Source Review，仅166页Context Engineering survey仍为Review Pending，2/2低分闭合，Blocked为0；field disputes与artifact/revision boundaries均显式保留。Diffuman4D、TAIL、π³、VisionThink、CSD-VAR、OpenBEATs与Franca均已闭合非模板化packet；RedOne与Teach Old SAEs回拨W28。fixed-org/release/cross-index recall仍Open，Historical Books Gate关闭。

W27 forward checkpoint（2026-08-22）：旧1项已扩展为37个scored owner lower-bound；16项25～30分、17项20～24分、4项低分。当前29/33 retained candidates完成strict Full Source Review；MARVIS因事件时`2507.01544v1`正文缺失保留Review Pending / Material Gap，vLLM RFC #20283、vLLM Q3 roadmap #20336与SGLang Q3 roadmap #7736保留Proposal Pending / Not Shipped；按blocked-skip规则不阻塞后续周，4/4低分闭合，Disputed为0。大量June-v1 identity回拨W25/W26，vLLM v0.9.2 release归W28。fixed-org/cross-index recall未闭合，因此W27 Candidate Evidence Gate Not Passed，Historical Books Gate关闭。

W28 forward checkpoint（2026-08-22）：旧1项校准为95个scored owner lower-bound；68项25～30分、22项20～24分、5项低分。当前42/90 retained完成strict Full Source Review，48项Review Pending；SARA/ECom-Bench、DRAGOn/HIRAG与Omni-Router已闭合全文。DRAGOn v1 baseline/evaluator被2026 bug fixes与v3重算取代，机制可核但结果保持Disputed；HIRAG与Omni-Router保留event-time artifact边界。UQLM回拨W18；Teach Old SAEs、Agent KB、POLAR、Response Attack与Spatio-Temporal LLM仍因event-time材料缺口不计strict。5/5低分闭合，Blocked 0；compact drafts不计全文审计，Discovery/Evidence Gate保持Open，Historical Books Gate关闭。

W30/W31 forward checkpoint（2026-08-22）：W30从旧2项扩展为3个scored/strict owner，新增heterogeneous agent-system scheduling论文；Discovery仍Open，旧“Books Gate完成”已撤回。W31从旧2项扩展为6个scored/strict owner，新增SLAI、Graph-R1、DICE与Graph-Augmented LLM Agents survey；只剩withdrawn/full-text-unavailable的G-Core unscored Blocked identity。Graph-R1的reward claim mismatch、Fano/theory dispute与artifact drift，以及DICE的formal-claim dispute均保留。W31 Historical Evidence Gate Open，Historical Books Gate Closed。
discovery / ownership ledger：恢复 61 个本周 arXiv family、AI co-scientist Blog family 与 3 个本周 engineering release family，
并把 arXiv:2502.09245、arXiv:2502.11271、MUDDFormer（arXiv:2502.12170）与 SGLang v0.4.3 按 first-public date 回拨 W07。
当前 65 个 W08 owner family 中，AI co-scientist、MLGym、Qwen2.5-VL、SigLIP 2、SuperGPQA、
LoRA Knowledge Capacity、Soundwave、Embedding Space Capacity、S*、Magma、RDLM、Logic-RL、SWE-Lancer、TrustGen、MMTEB、HumanUP、SongGen、Small Model Learnability Gap、Multimodal Mamba、RAD、Decomposed Reward Models、MoM、FLAG-Trader、SoFar、Craw4LLM、PC-Agent、S2R、Selective Question Answering、SafeRoute、RelaCtrl、YOLOv12、CLIPPER、Explorer、Template-Anchored Safety、NExT-Mol、video-SALMONN-o1、InfiR、LongPO、Temporal Heads、LongWriter-V、Intuitive Physics from Natural Videos、Autellix、Sailor2、Thinking Preference Optimization、HermesFlow、Atom of Thoughts、Dynamic Concepts Personalization、RealSyn、Diffusion-Sharpening、Revisiting Test-time Scaling、AlphaMaze、PAFT、CoSyn、LServe、From RAG to Memory / HippoRAG 2、LoRAM、Text2World、HeadInfer、AdaptiveStep、AIDE、Model-guidance、Transformers v4.49.0、Accelerate v1.4.0 与 vLLM v0.7.3 已完成完整 Source Review；HermesFlow、Diffusion-Sharpening、AlphaMaze、LoRAM、AdaptiveStep 与 Model-guidance 因 objective / result / executable / scope contract 冲突保持 `Disputed`；Quantum Error Correction with RL 已完成低分来源/日期/拒绝核验；MUDDFormer 已在 W07 完成 v1-locked Full Source Review。前一检查点曾以W08 65/65 owner通过Gate，后来被spillback discovery重开；fixed-org replay补回LUME、SmolVLM2、Grok 3与Mistral Saba，W09 HF replay再回拨23个W08-owner family。当前所有可访问项已闭合，RIFLEx携带P1 blocked ledger，W08再次通过Candidate Evidence Gate。Source Family：`Jailbreaking to Jailbreak` 的 v1 为 2 月 9 日，回拨 W06；LLaDA、Overthinking、
Step-Video-T2V 等 v1 位于 2 月 10～16 日，回拨 W07；推荐日期从不替代事件日期。W02 replay
发现 2025-01-09 榜单中的 DPO Kernels v1 实际属于 2025-01-05；该 family 已回拨 W01 并完成第 37 份
Full Source Review。W01 在确认 01-10 与 01-13 连续两页无新增 owner 后，重新通过 37/37 scoring、
discovery、review、owner mapping 与 13/13 low-score checks。W02 已恢复 30 余项 discovery candidates，
并完成 rStar-Math、Search-o1、Cosmos、LLaVA-Mini、Meta-CoT、Agent Laboratory、URSA、
InfiGUIAgent 与原有 vLLM 共 9 份非模板化 Full Source Review；
随后完成 Sa2VA、MotionBench、PPTAgent 与 Diffusion as Shader，当前共 13 份；GeAR 作为 replay
遗漏候选补回 census。MotionBench 的 arXiv HTML 返回无关页面，已用同 ID v1 PDF、abs metadata 与
official repository 三方闭合并保留异常记录；随后完成 OpenOmni、Dolphin、Segmenting Text and
Learning Their Rewards 与 Modern GAN Baseline；再完成 GeAR、Toto、DriveBench 与 Centurio，纠正
GeAR 的名称和 owner；随后完成 SWE-Fixer、VideoRAG、SCRIT 与 LlamaV-o1。SWE-Fixer 的 HTML
错配已用 v1 PDF/abs/repository 闭合；LlamaV-o1 的 runtime/complexity 冲突保留为 `Disputed`；随后完成
OmniManip、OVO-Bench、Migician 与 Multiagent Finetuning，明确 physical feedback、streaming runtime、
multi-image identity 与 majority pseudo-label 的证据边界；再完成 ReFocus、ConceptMaster、Video Alchemist
与 FinDaP，纠正 FinDaP event date并保留 ReFocus数据量冲突。原论文/Research共 33 份，普通
`Review Pending = 0`；Transformers 4.48.0 已完成 20分 Release/PR Source Review，llama-cpp-python 0.3.6
已完成低分 version/changelog/rejection核验。最终复核确认35/35评分、34/34 `20+` Source Reviews、
1/1低分 disposition、日期、字段、owner和Markdown曾在原分母内闭合；W03 replay 随后发现
Transformer-Squared、Tensor Product Attention与ChemAgent的v1实际仍属于W02，均已回拨并完成全文、
revision/artifact、实验合同、limitations与owner审计。继续扫描01-14～15延迟发现页面，又回拨MinMo、
O1 Replication Journey Part 3、VideoAuteur、SPAM、Grad-Mimic、Padding Tone与3DIS-FLUX。前六项完成
非模板化30字段Full Source Review；3DIS-FLUX完成低分来源、日期和拒绝核验。W03后续页又找回
Beyond Sight / FuSe（v1 2025-01-08），已回拨并完成论文、项目页、代码和数据artifact联读。最终W02通过
46/46评分、44/44 `20+` Full Source Review、2/2低分disposition、评分合计、字段、owner与Markdown检查；Process
Reward Model lessons（arXiv:2501.07301，v1 01-13）确认归W03。W03 已完成 56 项 discovery census，
并完成 MiniMax-01、PRESERVE、Process Reward Model lessons、BIOMEDICA、WebWalker、FAST、Diffusion APT、
HALoGEN、Inference-Time Scaling for Diffusion 与 Scaling Visual Tokenizers，以及 Trusted Models for
Private Inference、Physics-IQ、The Heap、TA-TiTok / MaskGen，以及 Omni-RGPT、Output-Centric Feature
Descriptions、OpenCSG 与 MMDocIR，以及 RLHS、Tarsier2、Best Practices for Open Datasets 与 uCO3D，
再加 MatchAnything、PIIP、CityDreamer4D 与 RepVideo，以及 Ouroboros-Diffusion、OmniThink、
LLMs as Judges of Unstructured Text、Advanced Patient Simulators、PokerBench、Multimodal Aesthetics；
fixed-source replay 另补回 JAX 0.5.0，并纠正 device-polymorphic export 实际属于 JAX 0.4.38。
W03 一度通过 41/41 scoring、33/33 `20+` 非模板化 30 字段 Full Source Review 与 8/8 低分
identity/date/score/rejection disposition；但 W04 的 01-20～24 Hugging Face discovery 页面随后分批暴露
22 个 arXiv v1 实际属于 01-14～19 的延迟 owners。W03 因此按 first-public date 四次重开并完成回拨审计；
最终为 63/63 scoring、46/46 `20+` Full Source Review、17/17 low-score disposition，评分、30字段、owner、
revision 与 Markdown 检查通过，cursor 进入 W04。最后两批补回 Learn-by-interact、Step-KTO、Control LLM、
DiffuEraser、GauSTAR 与 EMO2；前三项完成全文审计，后三项完成可审计低分处置。
W04 已把旧 3 项 seed 扩展为 53 项候选 census：44 项 `20+`、9 项低分。DeepSeek-R1、Kimi k1.5、
Chain of Agents、Agent-R、Mobile-Agent-E、Demons in the Detail、MMVU、UI-TARS、Hunyuan3D 2.0、
InternLM-XComposer2.5-Reward、Video Depth Anything、MAGI、EmbodiedEval、Condor、VideoLLaMA 3、
FilmAgent、TPO、Autonomy-of-Experts 与 Pairwise RM 已完成非模板化 30 字段 Source Review；当前
44/44 high-score Full Source Review 与9/9低分identity/date/score/rejection disposition均已完成，W04 Gate Passed。EMO2 已按 v1 日期回拨 W03；
Video Depth Anything、MAGI、EmbodiedEval、Condor 与 TPO 的 HTML/PDF 访问异常均通过同 ID primary
source 或官方 artifact 闭合并保留 version boundary；Temporal Preference Optimization 已完成 PDF 审计。
W05 replay 新发现 Qwen2.5-VL 的官方 release 实际发表于 2025-01-26，已回拨 W04，并通过后续同 family
technical report/model card 完成 architecture、training、evaluation 与 evidence-boundary 复核。
Hugging Face 1月28日 discovery 另暴露 Qwen2.5-1M 的 arXiv v1 为1月26日；已一并回拨，完成 progressive
training、DCA/MInference、chunked Prefill、DCPP/TAG 与 batch-1 TTFT 边界的全文审计。
随后 1月27～28日 discovery replay 又回拨 HLE、CoRAG、ICRL、MLLM benchmark redundancy、RealCritic、
Baichuan-Omni-1.5、ARWKV、MoE sparsity scaling 与 CodeMonkeys；9项均完成30字段Source Review。DeepFlow
也因v1为1月24日回拨，补齐serverless request/job/task、FlowServe、RTC/DistFlow、PD/locality scheduling
与fast-scaling的生产系统边界；W05 fixed-source replay 又确认 Transformers 4.48.1 首发于1月20日，
作为低分 release fact 回拨。W06 replay 又发现 MatAnyone 的 v1 为1月24日；该窄域 video-matting
memory case 已回拨并完成低分核验，TracksTo4D 则因 first-public 为2024年未重复计分。因此 W04 最终
重新通过53/53 disposition、44/44高分全文审计和9/9低分拒绝核验。W06延迟发现的 Continuous 3D
Perception / CUT3R 也按1月21日v1回拨，补齐 recurrent persistent scene state、read/write separation、
online pointmap/pose evaluation 与 state compression failure modes。
Books Gate 仍关闭。
W05 已从旧 3 项 seed 扩展为55项候选 census：39项 `20+`、16项低分。除重新核验 vLLM V1、s1 与
OpenAI deep research 外，补齐 PyTorch 2.6、Streaming DiLoCo、Janus-Pro、Mixture-of-Mamba、
SFT-vs-RL、FP4 Training、Over-Tokenized Transformer、interpretability research agenda、TAID、Critique
Fine-Tuning、Atla、external o3-mini safety、Virus、Underthinking、GuardReasoner、SANA 1.5、WildChat-50M、
MedXpertQA 与 PhysBench。PhysBench 的 HTML、appendices、项目页和评测仓库已经恢复，明确区分
multiple-choice benchmark、tool/memory-assisted reasoning 与 embodied control evidence。W05 最终通过
55/55 disposition、39/39非模板化30字段 Full Source Review、16/16低分核验、评分/日期/revision/owner/
Markdown检查。W06 discovery spillback 额外恢复 Constitutional Classifiers、ChunkKV、Reward-Guided
Speculative Decoding、learning-rate scheduling、SafeRAG、adversarial inference-time compute、
Scalable-Softmax、PixelWorld、SAeUron、MM-IQ、Rethinking Mixture-of-Agents、Federated Sketching LoRA、
Activation Approximation Safety、Concept Steerers、RAG Interrogation Attack、HackerRank-ASTRA 与
Weak-to-Strong Diffusion；八项低分 domain candidates 也完成来源与拒绝核验。
Constitutional Classifiers 联读2月3日官方说明与2月13日 demo failure，避免只保留发布时正面结果；
未修改 Books，cursor 进入 W06。W06 旧版“无保留候选”已被推翻，当前恢复 63 项候选 census：38 项
达到 `20+`，25 项进入低分核验。OmniHuman-1、PRIME、DeepRAG、FastKV、vLLM 0.7.2、SmolLM2、
LIMO、recurrent-depth latent reasoning、Sliding Tile Attention、QuEST、BOLT、Satori 与 QLASS 已完成
30 字段 Full Source Review；On-device Sora随后通过arXiv metadata、CC BY v1全文副本与official repository
恢复正文。KVFundaBench/ShotKV、AlphaGeometry2、ScoreFlow、VideoRoPE、SCONE、InferenceGuard、
Transformer World Models、LongDPO、VideoJAM、Inverse Bridge Matching Distillation、Demystifying Long CoT
与 Teacher Hacking 又按事件时 arXiv v1 完成全文审计，其中 KV family 明确隔离 2026 v4 的改题与扩展结果，
World Model family 明确隔离后续摘要的69.66结果。Token Assorted、PyCapsule、ConceptAttention、UltraIF、
Goku 与 Self-Backtracking 随后完成事件时版本全文审计；UltraIF 的普通 HTML 返回错误，因此明确锁定
arXiv v1 PDF，未以当前 v2 或摘要替代。DuoGuard、Symbolic World Models、CMoE、CodeSteer、VectorQ
与 Gemini 2.0 GA 又完成非模板化30字段 Source Review；Gemini 仅保留 release/model-card 版本事实，
不从产品能力反推内部机制。随后对低分账目逐项校准，发现 Preference Leakage、MGA、HMA、particle
inference、Speak Easy、SliderSpace、MakeAnything、TwinMarket 等 22 项被低估了 Project Relevance / Longevity；
W06 因此首轮校正为 60 个 `20+` 和 3 个低分候选。60/60 high-score Full Source Review 完成；除 MGA、HMA、
particle inference、Speak Easy、verification scaling 与 Preference Leakage 外，又闭合 Direct Alignment、
AlignVLM、ZebraLogic、ACECODER、AStar、JUMP、ReasoningWeekly、RandLoRA、Improved Latent Consistency、
COCONut-PanCap、SynCD、AIM、3D point-regularized video generation、output-distribution capability decomposition、
fixed-grid procedural generation 与 multi-agent environment feedback。Transformers 4.48.3、MLX 0.22.1 与
LayerTracer 完成低分版本/identity/rejection核验。W07 discovery replay 随后暴露 The Curse of Depth、
Social-Deduction MARL、LM2、Hierarchical Drafting、Gemstones、CTRL 与 NoLiMa 的 arXiv v1 均落在
2月5～9日；七项按 first-public date 回拨 W06，并完成事件时版本 Method、evaluation、limitations、artifact、
30字段与 owner 审计。W06 首轮为 70/70 disposition、67/67 `20+` Full Source Review、3/3 low-score verification；
评分、日期、revision、Markdown 与 Books-closed boundary 检查通过后进入 W07。
W07 discovery replay 随后把旧版 3 项 seed 扩展为 31 项候选：13 项达到 `20+` 并完成非模板化
30 字段 Full Source Review，18 项完成 identity、v1/官方日期、评分与拒绝边界核验。新增高分证据包括
reward-aware test-time compute、OREAL、Matryoshka Quantization、Jakiro、InSTA、Hephaestus、
WebLI-100B VLM data scaling、prompt-cache timing audit、TransMLA、Distillation Scaling Laws 与 LASP-2；
旧版 W07 Books 完成声明和 changed Books paths 已撤回，Historical Books Gate 保持关闭。W07 的日期账本
同时确认 CODESIM、Competitive Programming、APE、Hypencoder、Éclair 与 CAD-Editor 的 v1
早于 2 月 10 日，不能留在 W07；arXiv:2502.05415 还暴露 revision-identity 风险：2 月 v1 实为
Show-o Turbo，5 月 v2 才改为 UniCMs，不能用当前 metadata 覆盖事件时内容。四个 `20+` family 已完成
全文、Method、evaluation、limitations/artifact与30字段审计，三个低分family完成拒绝核验。W06 最终
重新通过 77/77 disposition、71/71 Full Source Review、6/6 low-score verification；W08 look-ahead 后又把
`Jailbreaking to Jailbreak` 按 2 月 9 日 arXiv v1 回拨，最终通过 78/78 disposition、72/72 Full Source
Review 与 6/6 low-score verification。该 family 的 2 月 17 日 Hugging Face 推荐日期不再冒充 event date。
第三批明确保留 TCME 的概念性 trust boundary、Physics-IQ
的 heterogeneous model contract、The Heap 的 temporal contamination 边界与 TA-TiTok 的
text-conditioned reconstruction 风险；第四批进一步闭合 region-token temporal identity、
output-conditioned interpretability、中文语料版本边界与多模态文档检索的 storage/evaluation contract。
第五批进一步闭合 outcome-conditioned feedback、video data/SFT/DPO curriculum、open-data governance
与 real/synthetic 3D asset lineage；第六批闭合跨模态 correspondence supervision、resolution-capacity
allocation、生成式4D场景与 causal world model 的边界，以及跨层 feature cache 的执行代价；各项都保留
作者实验、未披露 workload 和 artifact access 的外推边界。第七批锁定 OmniThink v1、隔离当前 v5
revision bleed，并闭合 FIFO long-video memory、evidence-tree/derived-pool、human/model agreement 与
inquiry/diagnosis simulator 的状态、评测和 failure-mode 边界。最终批次进一步区分 PokerBench 的
single-spot solver proxy 与 adaptive gameplay、ArtCoT 的 rubric correlation 与 universal aesthetics，
以及 JAX deterministic PRNG 与跨版本 bitwise stability。新 spillback 包括 VideoWorld、Mind Evolution、
MSTS、PaSa、ComplexFuncBench、GameFactory、SEAL、Go-with-the-Flow、Geometry of Tokens、IntellAgent、
Learn-by-interact、Step-KTO、Control LLM 及 9 个低分窄域/校准候选；13 个 `20+` spillback 已完成非模板化
30 字段全文审计，8 个低分项完成可审计拒绝记录。
Books Gate 保持关闭。

W08 look-ahead 又发现 Hugging Face 2 月17～18日推荐页中有 42 个 Source Family 的 arXiv v1
实际落在 W07，另有 1 项回拨 W06。W07 完成逐项重评后，38/38 高分 spillback 形成非模板化 Full Source Review，
4/4 低分 spillback 完成 identity/date/score/rejection 核验；合并原有候选后最终通过 73/73 scoring、
51/51 `20+` Source Review 与 22/22 low-score disposition。后批次补齐 small-model adapter、TSP3D、
V2V-LLM、MRS、CLaMP3、MIKASA、Cuckoo、professional fact-checker evidence requirements 与
atomic data-alignment under budget；所有 Books disposition 仍为 Deferred，forward cursor 进入 W08。

W08 首轮重放已纠正旧版“论文与工程无候选”的结论。当前 ledger 包含 61 个本周 arXiv
identity、Transformers v4.49.0、Accelerate v1.4.0 与 vLLM v0.7.3；AI co-scientist Blog event
与 W09 paper v1 共享同一 Source Family。Soundwave 的普通 arXiv HTML 暂不可用，已通过对应
27-page v1 PDF 与官方 architecture/inference repository 完成全文核验；2025-05-03 权重发布只作
revision lineage，不倒写为 W08 event-time artifact。
Transformers v4.49.0 已锁定官方 tag `a22a437`，并完成完整 Release、compare、selected Cache/processor/quantizer/
parallel-plan/correctness PR 审计；其 315-commit integration surface 只支持 framework compatibility migration，
不支持 Release-wide 性能、全硬件可移植性或各集成模型质量结论。该 family 归 `PLATFORM-MODEL-REGISTRY`，
标记为 `Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate`。
Accelerate v1.4.0 已锁定官方 tag `b431d1f`，并完成 TP/DataLoader、torchao/DeepSpeed FP8、dtype estimator 与
GradientState/DataLoader weak-reference lifecycle 审计。它说明 thin wrapper 仍参与 process-group、sample identity、
precision 和 lifetime correctness，但不拥有 TP collective math 或平台调度；标记为 `Books Pending — No Change Candidate`。
vLLM v0.7.3 已锁定 signed tag `ed6e907`，完成完整 Release/compare 及 concurrent partial Prefill、KV hash owner、
n-gram/MTP speculation、msgpack、metrics 与 V1 pipeline paths 审计。它支持“调度对象扩展为带 KV/phase/proposal 的
token state”这一既有结论，但 constructed single-A100 TTFT 与各硬件 PR 数字不能合并为 Release-wide 性能结论；
标记为 `Books Pending — No Change Candidate`。W09 已于 2026-08-20 恢复单向重放，当前状态见上方 forward cursor。
随后完成 MLGym 与 Qwen2.5-VL 的 30 字段全文审计：前者只支持可执行、异构 artifact 的
Research-Agent evaluation contract，不支持“自治科学发现”；后者支持 native-resolution + absolute-time
representation contract，但缺少组件 ablation、完整 workload 和独立复现，不能从 benchmark 表外推生产效率。
SigLIP 2 的 30 字段审计进一步确认：其贡献是多目标训练配方、local/dense supervision 与 NaFlex
native-aspect-ratio artifact 的组合演进；缺少组件级因果 ablation，且 private WebLI、TPUv5e 训练规模和未披露
serving contract 阻止把作者 benchmark 外推为通用表示或生产效率结论。SuperGPQA 将长尾专业评测推进到
taxonomy/provenance/prompt-budget contract，
LoRA Knowledge Capacity 说明小 adapter 不代表小 behavioral blast radius；Soundwave 则把 speech-text
representation alignment 与 content-dependent sequence shrinking 拆成不同 owner，但 10k/520k 小时比较、
72 ms TTFT 与 2.5% sequence ratio 都只在作者披露的局部实验条件内成立。
Embedding Space Capacity 已严格回到 Transformer-only v1；6 月加入的 Mamba/entropy-coder/ACL evidence 未倒写。
其长期证据是 per-sample optimized input vector 的 uncertainty-reduction ceiling，而不是可部署的 1,568× compressor；
5,000-step encoding、teacher-forced threshold、未声明 precision 和 scattered/non-canonical latent geometry 保持为边界。
S* 进一步把 code test-time compute 拆成 parallel coverage、execution-grounded sequential repair 与 adaptive selection；
其长期价值是 Workflow ownership，而不是“小模型超越大模型”的榜单叙事。单次实验、competition-code scope、
未披露成本/SLO 与论文内部 headline 数字不一致均保留为证据边界。
SuperGPQA 的 v1 256-page source packet 与 artifact 复核确认：其长期价值是 taxonomy-aware EvalSpec、
human/LLM/rule quality pipeline 和 prompt/sampling sensitivity，而不是“61.82% 代表距离 AGI 的刻度”。STEM 集中、
Chinese-source translation、shared-model filtering、contamination 与未披露 compute contract 均保留为证据边界。
LoRA Knowledge Capacity 已回到 14-page v1，而没有把 v3 新增的 Mistral evidence 倒写到 W08。其证据支持
adapter promotion 必须同时检查 target recall、negative shifts、refusal 与 external slices；单模型、rank-1、
train/test overlap 和未披露 hardware 不能推出通用“可装入事实数量”或 LoRA capacity law。
TrustGen 已锁定 2025-02-20 的 v1，而没有把 ICLR 2026 的 39-model 版本或当前 toolkit 倒写到 W08。
其长期证据是 `metadata curator → test-case builder → contextual variator` 的动态评测流水线，以及
dataset、generator、variator、target 与 scorer 必须共同版本化；跨维度平均分不等于部署风险概率，
event-time code/data hashes、per-module ablation、judge calibration、成本和独立复现仍缺失。
MMTEB 已锁定 2025-02-19 v1 与论文指定的 results commit；它证明在所选公开模型/任务上，task-correlation
selection、retrieval pooling 与 embedding reuse 可以显著降低评测成本并大致保留相对排名，但不能证明对未来
model family 继续无损。v1 的 131/132、40/41 任务数冲突、mixed MTEB versions、pool-model blind spot 与
缺失的统一环境 manifest 已保留为 evidence boundary。
HumanUP 已锁定 2025-02-17 v1，并把 4 月后的 RSS revision 与 simulation code 仅作为 lineage。其两阶段机制
把 contact-rich sparse-reward motion discovery 与 full-mesh、posture/terrain randomization、strong control
regularization 下的 deployability refinement 分开；这支持 G1 受限环境中的 sim-to-real feasibility，但 event-time
artifact、真实试验完整分母、deadline/safety controller 与独立复现缺失，不能外推为开放世界自动恢复。
SongGen 已锁定 2025-02-18 v1；3～7 月的 checkpoints、test set 与 training code 只作 lineage。它把 mixed audio、
training-only vocal supervision、parallel dual-track 与 interleaved dual-track 还原为不同 state-layout 分支：统一 decoder
减少 cascade 边界，却没有消除 codec、condition encoder、data provenance 与 waveform decoder；interleaving 增强作者
workload 下的同步质量，也明确增加 sequence/KV 成本。16 kHz、English、30-second contract、非等成本 baseline 与缺失
serving evidence 阻止把结果外推为长音乐、跨语言或生产效率结论。
Small Model Learnability Gap 已锁定 W08 内最后修订的 2025-02-22 v2；11 月 v3、ACL publication 与当前 artifact
只作 lineage。它证明在作者数学、Qwen/Llama、SFT contract 中，teacher strength 和 trace length 不是脱离 student
capacity/domain prior 的总序；Mix Distillation 是 student-conditioned data policy，而不是“弱 teacher 永远更好”。
`<=3B`、1:4 mixture、distribution-shift 归因、judge-assisted scores 与缺少 seed/compute-matched ablation 均保留为边界。

Multimodal Mamba 已锁定 2025-02-18 v1；3 月 v2 与 2 月 19 日公开的代码/权重只作 lineage。它把
Transformer-to-SSM 替换重述为状态迁移问题：先继承可对应的 projection，再用逐层局部 MSE 对齐 recurrent
state 的行为，最后以 end-to-end KL 修复组合误差；纯 SSM 与 hybrid 因此是不同约束下的并存分支，而非线性
替代关系。20.6x headline 只绑定单张 RTX 4090、103K context、next-token latency 的作者测试；长上下文任务
质量、并发、SLO 与精度未披露，不能外推为通用 serving 吞吐结论。

RAD 已锁定 2025-02-18 v1；9 月核心代码、11 月 3DGS environment 与 NeurIPS 版本只作 lineage。它把 open-loop
IL 的 distribution gap 改写为可执行环境中的 policy-induced state problem：3DGS worker 产生闭环 rollout，PPO
探索安全关键偏差，dense directional objectives 改写完整 action distribution，IL 则约束 human alignment。
作者的 3x collision headline 只属于 337 个 held-out、non-reactive 3DGS dense-traffic scenes；actor log replay、
renderer boundary、未披露硬件与无 real-road denominator 阻止把它升级为真实道路安全或因果理解结论。

Decomposed Reward Models 已锁定 2025-02-18 v1；ACL publication 只作 lineage。它把单一 scalar reward 演进为
versioned latent basis：chosen/rejected embedding difference 经 PCA 形成 signed heads，再用少量 adaptation labels 组合
成当下 reward。关键边界是 PCA 只最大化 feature variance，论文与 Bradley-Terry 的联系依赖近似，component 的
benchmark correlation 不等于已命名或 causal 的人类价值；无代码、硬件、真实用户与跨版本稳定性证据也阻止把
“lightweight / interpretable”外推成生产 contract。

MoM 已锁定 2025-02-19 v1；5 月、10 月、11 月修订以及 9 月 varlen kernel 只作 lineage。它把线性序列模型的
单一 recurrent state 演进为 top-k routed local state bank 加 shared state：以固定但更大的 state capacity 和路由
复杂度，换取对不同 token 更新的隔离。作者两种规模与 2K recall contract 支持“优于所测单状态线性基线”，不支持
消除 interference、替代 KV、任意长度质量或 production throughput；single state、hybrid 与 dense KV 仍是条件分支。

FLAG-Trader 已锁定 W08 最后 revision v3（2025-02-19）。它把 prompt-only action generation 推进为外部环境
reward 驱动的 partially tuned LLM actor-critic，但复用的是 PPO/GAE 主线，不是新的 RL 算法。六个资产、单一历史
窗口、median-trajectory selection、无 fees/slippage/market impact、无 seed 与无 artifact，使其只支持机制可运行与
作者 backtest operating point，不支持盈利部署或“135M 普遍优于大模型”。

SoFar 已锁定 2025-02-18 v1 event，并把 2025-09-24 v2 的全文、appendix、artifact 与 NeurIPS 状态隔离为后续
lineage。其持久价值是 `position-only state → canonical pose → language-conditioned semantic direction → calibrated target
pose → controller/environment feedback`：语言可以选择任务相关的功能轴，但不能取消 camera/world/tool frame，也不能
取得 actuator authority。作者 ablation 与受限 sim/real experiments 支持该模块化机制在其 contract 中可行，不支持
开放世界 6-DoF、实时控制或 certified safety。

阶段边界：

- `Weekly Evidence Gate`：本轮唯一执行 Gate；所有可访问 `20+` 候选完成非模板化 Full Source
  Review，低分候选完成 identity/date/score/rejection 核验，ordinary `Review Pending = 0`。
- `Archive Completion Gate`：只有 W01～W52 discovery replay、spillback、revision 与 Materials Request
  Ledger 全部可复算后才能关闭。
- `Books Integration Gate`：本阶段不启动。Stable Node 只用于候选定位；相邻章节可以只读核对，但
  不修改 Books，不产生新的 integration disposition。

Claude Opus 4.5 保持用户已批准的 `Excluded / Unverified`；它不计 Full Source Review、不能支持机制
结论，也不阻止 forward cursor。若未来重新纳入，必须先取得并阅读全文，再重开候选级 Evidence Gate。

## Legacy Candidate and Books Ledger（Provisional Seed）

下表是 2026-07-31 旧轮次保存的 75 个候选与 Books 判断，只作为 discovery seed 和交叉检查入口。
表中的 `Complete`、`Refine`、`No Change` 或 `Weekly Only` 均不代表本轮 Weekly Gate 已通过；逐周
重放后，新候选、纠正日期、revision 和 evidence state 以对应 Weekly 的新记录为准。

| Week | Candidate | Score | Source Review | Current Disposition |
| --- | --- | ---: | --- | --- |
| 2025-W01 | Certaindex / Dynasor | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | SWE-Gym | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Titans | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | EnerVerse | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Scaling Laws for FP Quantization Training | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | REINFORCE++ | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | DPO Kernels | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Do NOT Think That Much | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Reconstruction vs. Generation / VA-VAE + LightningDiT | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | 2.5 Years in Class | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | VideoRefer Suite | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Unifying Specialized Visual Encoders / MERV | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | SeedVR | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | VisionReward | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | BoxingGym | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | VITA-1.5 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | CodeElo | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Dynamic Scaling of Unit Tests | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | TAPE: Contextualized Equivariant Positional Encoding | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | WeAudit | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | LTX-Video | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | HUNYUANPROVER | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | AutoPresent | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | ToolHop | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | A3: Android Agent Arena | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | State Space Model Bottlenecks | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | TangoFlux | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | ProgCo | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Personalized Graph-Based Retrieval | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Virgo | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Segment-Level DPO | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | LUSIFER | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Auto-RT | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | MLLM-as-a-Judge for Image Safety | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | HumanEval Pro / MBPP Pro | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | VideoAnydoor | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | CVPR 2025 Photorealistic Avatar Challenge | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W01 | Nested Attention | 19 | Low-score Source/Date/Rejection Verified | Low-score Rejected；narrow personalization branch |
| 2025-W01 | Population Aware Diffusion | 19 | Low-score Source/Date/Rejection Verified | Low-score Rejected；domain-specific synthetic-data objective |
| 2025-W01 | MapEval | 18 | Low-score Source/Date/Rejection Verified | Low-score Rejected；domain benchmark without new system mechanism |
| 2025-W01 | SeFAR | 18 | Low-score Source/Date/Rejection Verified | Low-score Rejected；task-specific self-supervised action recognition |
| 2025-W01 | finetrainers CogVideoX T2V LoRA support | 16 | Low-score Source/Date/Rejection Verified | Low-score Rejected；scoped engineering support event |
| 2025-W01 | Graph Generative Pre-trained Transformer | 19 | Low-score Source/Date/Rejection Verified | Low-score Rejected；graph-generation-specific mechanism |
| 2025-W01 | Test-time Computing Survey | 19 | Low-score Source/Date/Rejection Verified | Low-score Rejected；secondary taxonomy without new primary experiment |
| 2025-W01 | GS-DiT | 19 | Low-score Source/Date/Rejection Verified | Low-score Rejected；narrow 3D generation branch |
| 2025-W01 | Graph-Aware Isomorphic Attention | 19 | Low-score Source/Date/Rejection Verified | Low-score Rejected；narrow graph inductive bias |
| 2025-W01 | DepthMaster | 18 | Low-score Source/Date/Rejection Verified | Low-score Rejected；domain-specific depth estimation |
| 2025-W01 | Ingredients | 18 | Low-score Source/Date/Rejection Verified | Low-score Rejected；recipe aggregation with weak attribution |
| 2025-W01 | Generalizable Origin Identification | 18 | Low-score Source/Date/Rejection Verified | Low-score Rejected；limited threat-model coverage |
| 2025-W01 | MagicFace | 17 | Low-score Source/Date/Rejection Verified | Low-score Rejected；identity-specific generation branch |
| 2025-W02 | Cosmos World Foundation Model Platform | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | rStar-Math | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Domain-adaptive Post-training for Financial LLMs | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | DriveBench | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | SCRIT / Self-Evolving Critic | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | OmniManip | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | URSA | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Search-o1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Segmenting Text and Learning Rewards | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | GeAR / Generation Augmented Retrieval | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Autoregressive Pre-training from Videos / Toto | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | SWE-Fixer | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Multiagent Finetuning | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | ReFocus | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Tensor Product Attention / T6 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Transformer-Squared / Self-adaptive LLMs | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | ChemAgent / Self-updating Library | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | SPAM | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Grad-Mimic / Mimic Score | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | MinMo | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | VideoAuteur | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | O1 Replication Journey Part 3 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Padding Tone | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Beyond Sight / FuSe | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Towards System 2 Reasoning / Meta-CoT | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | LLaVA-Mini | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Sa2VA | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | MotionBench | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | PPTAgent | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | OpenOmni | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Centurio | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | OVO-Bench | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Migician | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Multi-subject Open-set Video Personalization | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Diffusion as Shader | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Agent Laboratory | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | InfiGUIAgent | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Dolphin | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | VideoRAG | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | ConceptMaster | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | LlamaV-o1 | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Modern GAN Baseline | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | vLLM 2024 Retrospective and 2025 Vision | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | Transformers 4.48.0 | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W02 | llama-cpp-python 0.3.6 | 17 | Low-score Source/Date/Rejection Verified | Low-score Rejected；upstream pin / scoped bugfix |
| 2025-W02 | 3DIS-FLUX | 18 | Low-score Source/Date/Rejection Verified | Low-score Rejected；narrow renderer case，缺少独立系统机制 |
| 2025-W03 | MiniMax-01 | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Lessons of Developing Process Reward Models | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | FAST Action Tokenization | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | BIOMEDICA | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Diffusion Adversarial Post-Training | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | HALoGEN | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Inference-Time Scaling for Diffusion | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Trusted Models for Private Inference | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Scaling Visual Tokenizers | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Physical Principles in Generative Video Models | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | The Heap | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | WebWalker | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | TA-TiTok / MaskGen | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Omni-RGPT | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Output-Centric Feature Descriptions | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | OpenCSG Chinese Corpus | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | MMDocIR | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | RLHS | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Tarsier2 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Best Practices for Open Datasets | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | PRESERVE | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | UnCommon Objects in 3D | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | MatchAnything | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Parameter-Inverted Image Pyramid | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | CityDreamer4D | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | RepVideo | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Ouroboros-Diffusion | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | OmniThink | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | LLMs as Judges of Unstructured Text | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Advanced Patient Simulators | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | JAX 0.5.0 | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | PokerBench | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Multimodal Aesthetics | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | XMusic | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | Large Reasoning Models Survey | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Secondary Source |
| 2025-W03 | MangaNinja | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | FramePainter | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | Graph-PReFLexOR | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | CaPa | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | SynthLight | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | Multi-modal AI Copilot | 17 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | VideoWorld | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Evolving Deeper LLM Thinking | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | MSTS | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | PaSa | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | ComplexFuncBench | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | IntellAgent | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Learn-by-interact | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Step-KTO | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Control LLM | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | GameFactory | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | SEAL | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Go-with-the-Flow | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Geometry of Tokens | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W03 | Multiple Choice Confidence after Reasoning | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | Bridging Language Barriers in Healthcare | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | X-Dyna | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | Textoon | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | HiFi-SR | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | GaussianAvatar-Editor | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | DiffuEraser | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | GauSTAR | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W03 | EMO2 | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only |
| 2025-W04 | DeepSeek-R1 | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Kimi k1.5 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | UI-TARS | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Qwen2.5-VL | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Qwen2.5-1M | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Agent-R | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Demons in the Detail | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Improving Video Generation with Human Feedback | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Sigma / DiffQKV | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Mobile-Agent-E | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | InternLM-XComposer2.5-Reward | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Image Generation with CoT | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | VideoLLaMA 3 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | MMVU | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Continuous 3D Perception / CUT3R | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Test-Time Preference Optimization | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Autonomy-of-Experts | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Pairwise RM | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Temporal Preference Optimization | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | EmbodiedEval | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Video Depth Anything | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Taming Teacher Forcing | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | FilmAgent | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | O1-Pruner | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | SRMT | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Fast3R | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Video-MMMU | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Hunyuan3D 2.0 | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Condor | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Debate Helps Weak-to-Strong | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Imagine-E | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Triton 3.2.0 | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Chain of Agents follow-up | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Hallucinations in Drug Discovery | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Chain-of-Retrieval Augmented Generation | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | CodeMonkeys | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Humanity's Last Exam | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Parameters vs FLOPs / MoE Sparsity | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Baichuan-Omni-1.5 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | RealCritic | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Redundancy Principles for MLLM Benchmarks | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | RL + Transformer / ICRL | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | ARWKV | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | DeepFlow | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | YuE | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W04 | Reasoning Language Models: A Blueprint | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Survey Blueprint |
| 2025-W04 | TokenVerse | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Personalization |
| 2025-W04 | PAINT / Fixing Imbalanced Attention | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Experimental Case |
| 2025-W04 | One-Prompt-One-Story | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Experimental Case |
| 2025-W04 | EchoVideo | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Experimental Case |
| 2025-W04 | MatAnyone | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Video-Matting State Case |
| 2025-W04 | GPS as a Control Signal | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Conditioning Case |
| 2025-W04 | Panoramic Interests / SCAPE | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Domain Personalization |
| 2025-W04 | Transformers 4.48.1 | 16 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Patch Release |
| 2025-W05 | vLLM V1 Alpha | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | PyTorch 2.6 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Streaming DiLoCo | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Janus-Pro | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Mixture-of-Mamba | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | SFT Memorizes, RL Generalizes | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | FP4 Training | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | s1: Simple test-time scaling | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Over-Tokenized Transformer | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | GuardReasoner | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | SANA 1.5 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | OpenAI deep research | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Open Problems in Mechanistic Interpretability | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | TAID | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Critique Fine-Tuning | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Virus harmful fine-tuning attack | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | WildChat-50M | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Early external o3-mini safety testing | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Underthinking / Thought Switching Penalty | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | MedXpertQA | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | PhysBench | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Atla Selene Mini | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Constitutional Classifiers | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | ChunkKV | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Reward-Guided Speculative Decoding | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Learning-Rate Scheduling for Large Model Training | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | SafeRAG | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Trading Inference-Time Compute for Adversarial Robustness | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Scalable-Softmax | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | PixelWorld | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | SAeUron | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | MM-IQ | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Activation Approximation Safety | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Rethinking Mixture-of-Agents | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Federated Sketching LoRA | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Concept Steerers | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | RAG Interrogation Attack | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | HackerRank-ASTRA | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Weak-to-Strong Diffusion | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W05 | Qwen2.5-Max | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Version Fact / Mechanism Not Disclosed |
| 2025-W05 | Mistral Small 3 | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Model Release Fact |
| 2025-W05 | OpenAI o3-mini | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Product Contract / Mechanism Not Disclosed |
| 2025-W05 | MR.Q | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — General RL Research |
| 2025-W05 | DiffSplat | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow 3D Generation Case |
| 2025-W05 | LLMs Think Too Fast | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Single-environment Exploratory Study |
| 2025-W05 | CowPilot | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Research Prototype |
| 2025-W05 | SSQR | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow KG Representation Case |
| 2025-W05 | Multi-View Geometric Diffusion | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow 3D Generation Case |
| 2025-W05 | AIN | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Language-Specific Multimodal Model Case |
| 2025-W05 | Pathology Foundation Model Site Shift | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Domain Robustness Case |
| 2025-W05 | News Summarization Capability Study | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Task Evaluation |
| 2025-W05 | INT Promptable Segmentation | 17 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Vision Recipe |
| 2025-W05 | Transformers 4.48.2 | 16 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Compatibility Patch |
| 2025-W05 | Text-to-CAD / CADFusion | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow CAD Generation Case |
| 2025-W05 | Low-Resource Programming-Language Code Generation | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified；Weekly Only — Narrow Empirical Study |
| 2025-W06 | vLLM 0.7.2 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | OmniHuman-1 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | PRIME / Process Reinforcement through Implicit Rewards | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | FastKV | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | DeepRAG | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | SmolLM2 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | LIMO | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Latent Reasoning Test-Time Scaling | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Sliding Tile Attention | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | QuEST | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | On-device Sora | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | BOLT | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Satori | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | QLASS | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | KV Cache Compression Fundamental-Abilities Study | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | AlphaGeometry2 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | ScoreFlow | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | VideoRoPE | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | SCONE / Scaling Embedding Layers | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Almost Surely Safe Alignment | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Improving Transformer World Models | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | LongDPO | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | VideoJAM | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Inverse Bridge Matching Distillation | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Demystifying Long Chain-of-Thought | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Teacher Hacking | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Token Assorted | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | LLM Guided Self-Debugging | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | ConceptAttention | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | UltraIF | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Goku | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Self-Backtracking | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | DuoGuard | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Symbolic World Models via Test-time Scaling | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | CMoE | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | CodeSteer | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | VectorQ / Adaptive Semantic Prompt Caching | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Gemini 2.0 Flash GA / Flash-Lite Preview | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | The Curse of Depth | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Social-Deduction MARL | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | LM2 / Large Memory Models | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Hierarchical Drafting | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Gemstones / Multi-Faceted Scaling Laws | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | CTRL / Teaching Language Models to Critique via RL | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | NoLiMa | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Transformers 4.48.3 | 16 | Low-score Source/Date/Rejection Verified | Low-score Verified — patch/compatibility version fact |
| 2025-W06 | MLX 0.22.1 | 15 | Low-score Source/Date/Rejection Verified | Low-score Verified — tag/version fact；mechanism not disclosed |
| 2025-W06 | Direct Alignment Algorithms are a Blur | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Preference Leakage | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | AlignVLM | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | SliderSpace | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | MakeAnything | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | ZebraLogic | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | ReasoningWeekly / PhD Knowledge Not Required | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | RandLoRA | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Improved Latent Consistency Training | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | ACECODER | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Sample, Scrutinize and Scale | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | COCONut-PanCap | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Multi-Image Synthetic Data | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | TwinMarket | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | AStar / MCTS for Multimodal Reasoning | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | LayerTracer | 18 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only / Narrow-domain principle reuse |
| 2025-W06 | Particle-Based Inference Scaling / Rollout Roulette | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | JUMP / Universal Multi-Prompt Jailbreak | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Activation-Informed Model Merging | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | MGA / Pretraining Data Reformulation | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Physical Understanding in Video Generation | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | HMA / Learning Real-World Action-Video Dynamics | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Speak Easy | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Jailbreaking to Jailbreak | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | CODESIM | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | APE / Adaptive Parallel Encoding | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Hypencoder | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Show-o Turbo / arXiv:2502.05415v1 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W06 | Competitive Programming with Large Reasoning Models | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only / Capability Evidence |
| 2025-W06 | Éclair | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only / Domain Application |
| 2025-W06 | CAD-Editor | 19 | Low-score Source/Date/Rejection Verified | Low-score Verified — Weekly Only / Domain Application |
| 2025-W07 | Online Scheduling for LLM Inference with KV Cache Constraints | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Native Sparse Attention | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Can 1B LLM Surpass 405B LLM? | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | OREAL | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Matryoshka Quantization | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Jakiro | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | InSTA | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Hephaestus | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Scaling VLM Pre-training to 100B Data | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Auditing Prompt Caching | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | TransMLA | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Distillation Scaling Laws | 30 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | LASP-2 | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | MUDDFormer | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | LLaDA / Large Language Diffusion Models | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | The Danger of Overthinking | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Step-Video-T2V | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Region-Adaptive Sampling | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | ZeroBench | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | MM-RLHF | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | ImageRAG | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | DarwinLM | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | FoNE | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Precise Parameter Localization for Textual Generation | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Selective Self-to-Supervised Fine-Tuning | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | STMA | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | CRANE | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | The Mirage of Model Editing | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | I Think, Therefore I Diffuse | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | ReLearn | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Knowledge Circuits for Continual Pre-Training | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | IHEval | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Talk Structurally, Act Hierarchically | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Dyve | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | CALM | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | SURGE | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | EQ-VAE | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Counterexample-Driven Conceptual Reasoning | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Diverse Inference and Verification | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Better Embeddings with Coupled Adam | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Data Valuation for Instruction Fine-Tuning / NN-CIFT | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Cluster and Predict Latent Patches / CAPI | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | small Models, BIG Impact | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Text-guided Sparse Voxel Pruning / TSP3D | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | V2V-LLM | 21 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | MRS: Fast Sampler for Mean Reverting Diffusion | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | CLaMP 3 | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Memory, Benchmark & Robots / MIKASA | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Cuckoo | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Show Me the Work | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | Data-Efficient Atomic Property Pretraining | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W07 | We Can't Understand AI Using Our Existing Vocabulary | 18 | Low-score Source/Date/Rejection Verified | Low-score verified; position paper |
| 2025-W07 | AdaPTS | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Agentic End-to-End Protein Design / VibeGen | 19 | Low-score Source/Date/Rejection Verified | Low-score verified; narrow domain evidence |
| 2025-W07 | Ask in Any Modality survey | 19 | Low-score Source/Date/Rejection Verified | Low-score verified; survey only |
| 2025-W07 | Building AI for the pluralistic society | 18 | Low-score Source/Date/Rejection Verified | Weekly only; mechanism not disclosed |
| 2025-W07 | ReasonFlux | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | EVEv2 | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Efficient-vDiT | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | CodeI/O | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Demonstration Structure for Reasoning | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Goedel-Prover | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Mask-Enhanced Autoregressive Prediction | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Vision SAEs | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | BenchMAX | 18 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Continuous Concepts | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | WorldGUI | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | DPO-Shift | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Next Block Prediction | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | EmbodiedBench | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Thai Reasoning Model Merge | 17 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | Predictive Red Teaming | 19 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W07 | FailSafe Long-Context QA | 17 | Low-score Source/Date/Rejection Verified | Low-score verified |
| 2025-W08 | AI co-scientist | 22 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | MLGym | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Qwen2.5-VL Technical Report | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SigLIP 2 | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SuperGPQA | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | LoRA Knowledge Capacity | 23 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Soundwave | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Embedding Space Capacity | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | S*: Test Time Scaling for Code Generation | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Magma | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Continuous Diffusion Model for Language Modeling | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Logic-RL | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SWE-Lancer | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | TrustGen | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | MMTEB | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | HumanUP | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SongGen | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Small Model Learnability Gap | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Multimodal Mamba | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | RAD: 3DGS-based Reinforcement Learning for End-to-End Driving | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Decomposed Reward Models / Preference PCA | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | MoM: Mixture-of-Memories | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | FLAG-Trader | 23 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SoFar | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Craw4LLM | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | PC-Agent | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | S2R: Self-verification and Self-correction via RL | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Selective Question Answering under Test-time Scaling | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | SafeRoute | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | RelaCtrl | 25 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | YOLOv12 | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | CLIPPER | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Explorer: Web Trajectory Synthesis | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Template-Anchored Safety | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | NExT-Mol | 25 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | video-SALMONN-o1 | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | InfiR | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | LongPO | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Temporal Heads | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | LongWriter-V | 27 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Intuitive Physics from Natural Videos | 26 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Autellix | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Sailor2 | 28 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | Thinking Preference Optimization | 24 | Complete | Books Pending — Integration Deferred |
| 2025-W08 | HermesFlow | 24 | Complete | Disputed — Books Frozen |
| 2025-W08 | Atom of Thoughts | 25 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Dynamic Concepts Personalization | 25 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | RealSyn | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Diffusion-Sharpening | 23 | Complete | Disputed — Books Frozen |
| 2025-W08 | Revisiting Test-time Scaling of o1-like Models | 26 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | AlphaMaze / GRPO | 18 | Complete | Disputed — Weekly Only / Books Frozen |
| 2025-W08 | PAFT | 24 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | CoSyn / Scaling Text-Rich Image Understanding | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | LServe | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | From RAG to Memory / HippoRAG 2 | 28 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Train Small, Infer Large / LoRAM | 24 | Complete | Disputed — Books Frozen |
| 2025-W08 | Text2World | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | HeadInfer | 27 | Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | AdaptiveStep | 24 | Complete | Disputed — Books Frozen |
| 2025-W08 | AIDE | 27 | Complete | Books Pending — No Change Candidate |
| 2025-W08 | Diffusion Models without Classifier-free Guidance / Model-guidance | 26 | Complete | Disputed Scope Claim — Books Frozen |
| 2025-W08 | Transformers v4.49.0 | 22 | Complete | Weekly Only — Version/Integration Fact / Books Pending — No Change Candidate |
| 2025-W08 | Accelerate v1.4.0 | 23 | Complete | Books Pending — No Change Candidate |
| 2025-W08 | vLLM v0.7.3 | 27 | Complete | Books Pending — No Change Candidate |
| 2025-W08 | Low-weight Quantum Error-Correcting Codes with RL | 18 | Low-score verified | Weekly Only — Outside Knowledge-tree Scope |
| 2025-W08 | LUME: LLM Unlearning with Multitask Evaluations | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Claude 3.7 Sonnet and Claude Code | 23 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W09 | SWE-RL | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | SpargeAttn | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Drop-Upcycling | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Kanana | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Towards Optimal Multi-draft Speculative Decoding | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | WebGames | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | OmniAlign-V | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Language Models' Factuality Depends on the Language of Inquiry | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Rank1 | 25 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | DeltaBench / Can LLMs Detect Errors in Long CoT? | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Agentic Reward Modeling | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | VEM: Environment-Free Exploration for Training GUI Agent | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | CritiQ: Mining Data Quality Criteria from Human Preferences | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Training LLMs with MXFP4 | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Self-Training Elicits Concise Reasoning | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Granite Embedding Models | 27 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | WorldModelBench | 28 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | LongRePS | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | PersonaBench | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | Safety Tax | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | ARIES: Autonomous Reasoning on Interactive Thought Graphs | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | GUI Pivot / Query Inference | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | RaPID: Retrieval-Augmented Long Text Generation | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Babel Multilingual LLMs | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | LADDER / Test-Time Reinforcement Learning | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | What Makes a Good Diffusion Planner? | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Ray 2.43.0 LLM APIs | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | JAX 0.5.1 | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Unsloth Direct Windows Support | 19 | Low-score Verification Complete | Weekly Only — Version/Compatibility Fact / No New Core Mechanism |
| 2025-W09 | GPT-4.5 research preview | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Mechanism Partially Disclosed |
| 2025-W09 | DeepSeek FlashMLA v1 | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged |
| 2025-W09 | DeepSeek DeepEP V1 | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / V1 Artifact Mutable |
| 2025-W09 | DeepSeek DeepGEMM v1 | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / W09 Snapshot Not Tagged |
| 2025-W09 | DeepSeek DualPipe code artifact | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Mechanism Pre-window |
| 2025-W09 | DeepSeek EPLB initial artifact | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Initial Snapshot Partially Recovered |
| 2025-W09 | DeepSeek 3FS open-source artifact | 29 | Full Source Review Complete | Books Pending — Structural/Refine Candidate / W09 Snapshot Not Tagged |
| 2025-W09 | DeepSeek smallpond open-source artifact | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / 3FS-coupled Evidence |
| 2025-W09 | DeepSeek V3/R1 Online Inference System Overview | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Vendor Production Case |
| 2025-W09 | Wan2.1 code and weights release | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Later Report Evidence |
| 2025-W09 | Ai2 olmOCR model/data/pipeline release | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Teacher and Pipeline Coupled |
| 2025-W09 | Microsoft Phi-4-mini + Phi-4-multimodal launch family | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Later Report Evidence |
| 2025-W09 | Cohere Command R7B Arabic open-weights release | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Regional Post-training Branch |
| 2025-W08 | SmolVLM2 official release | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | Grok 3 Beta | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Mechanism Partially Disclosed |
| 2025-W08 | Mistral Saba | 22 | Full Source Review Complete | Weekly Only — Version/Product Fact / Mechanism Partially Disclosed |
| 2025-W08 | SurveyX | 25 | Full Source Review Complete | Books Pending — No Change Candidate / Experimental Self-Evaluation Coupling |
| 2025-W08 | SIFT | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Experimental Self-Confirmation Boundary |
| 2025-W08 | U-SAFEBENCH | 26 | Full Source Review Complete | Disputed Model Identity / Refusal-only Policy Contract — Books Frozen |
| 2025-W08 | AlchemyBench / Automated Materials Discovery | 26 | Full Source Review Complete | Disputed Dataset Verification / Feasibility Judge Contract — Books Frozen |
| 2025-W08 | MedHallu | 25 | Full Source Review Complete | Disputed Dataset Admission / Ground-truth Contract — Books Frozen |
| 2025-W08 | Think Inside the JSON / ThinkJSON | 22 | Full Source Review Complete | Disputed Objective/Verifier/Evaluation Contract — Books Frozen |
| 2025-W08 | o3-mini Reasoning/Performance Analysis | 23 | Full Source Review Complete | Disputed Causal/Probability Contract — Books Frozen |
| 2025-W08 | InterFeedback | 25 | Full Source Review Complete | Books Pending — No Change Candidate / Experimental Provider-conditioned Evaluation |
| 2025-W08 | Tree-of-Debate | 25 | Full Source Review Complete | Disputed Evidence-filter / Tree-depth Contract — Books Frozen |
| 2025-W08 | Audio-FLAN | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Preliminary Artifact Partial |
| 2025-W08 | CodeCriticBench | 25 | Full Source Review Complete | Books Pending — No Change Candidate / Experimental Judge-derived Advanced Ground Truth |
| 2025-W08 | RIFLEx | — | Unverified / Blocked — v1 full text unavailable | Books Frozen — P1 Full Text Required |
| 2025-W08 | MMIR | 26 | Full Source Review Complete | Disputed Dataset Count / Privileged Evaluation-helper Contract — Books Frozen |
| 2025-W08 | Reflective Planning | 26 | Full Source Review Complete | Disputed DDM Test Leakage / Simulator-only Evaluation Contract — Books Frozen |
| 2025-W08 | TAG / TAME Hierarchical MARL | 24 | Full Source Review Complete | Books Pending — No Change Candidate / Experimental Scope-limited MARL Hierarchy |
| 2025-W08 | Curie | 27 | Full Source Review Complete | Books Pending — No Change Candidate / Experimental Rigor-workflow Evaluation |
| 2025-W08 | Scale-Distribution Decoupling | 26 | Full Source Review Complete | Disputed Theory/Figure Contract — Books Frozen |
| 2025-W08 | Prompt-to-Leaderboard | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W08 | LaTIM | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Experimental Approximate Decomposition |
| 2025-W08 | MolSpectra | 25 | Full Source Review Complete | Books Pending — No Change Candidate / Experimental Domain-specific Multimodal Pretraining |
| 2025-W08 | DOEI | 18 | Low-score verified | Weekly Only — Domain-specific WSSS mechanism / No New Core Owner |
| 2025-W08 | CODESYNC | 25 | Full Source Review Complete | Disputed API Ground Truth — Books Frozen |
| 2025-W08 | Guardians of the Agentic System | 16 | Low-score Verification Complete | Weekly Only — Unreliable Empirical Contract / No Books Owner |
| 2025-W09 | Make LoRA Great Again / GOAT | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Stable-SPAM (v1) | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | VideoGrain | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | DICEPTION (v1) | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Mobile-Agent-V (v1) | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Thus Spake Long-Context LLM (survey v1) | 25 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | KV-Edit | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | K-LoRA | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | ART / Anonymous Region Transformer | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Artifact Withdrawn |
| 2025-W09 | Clustering-On-Difficulty downstream scaling | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Headline Metric Disputed |
| 2025-W09 | Visual Perception Token | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | MLLMs Know Where to Look / ViCrop | 27 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | Finding the Sweet Spot / Preference Data | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | WiCkeD | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | TheoremExplainAgent (v1) | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | BIG-Bench Extra Hard (v1) | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | GHOST 2.0 | 18 | Low-score verified | Weekly Only — Outside Core Knowledge-tree Scope |
| 2025-W09 | Plutus | 25 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | Project Alexandria | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Legal Status Jurisdiction-Specific |
| 2025-W09 | Can Language Models Falsify? / REFUTE | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Distill Any Depth | 22 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | MMKE-Bench | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Artifact Metadata Inconsistent |
| 2025-W09 | FSPO | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Accented ATC ASR | 18 | Low-score verified | Weekly Only — Domain Case / No New Core Mechanism |
| 2025-W09 | AISafetyLab technical report | 26 | Full Source Review Complete | Books Pending — No Change Candidate / Code Event Spillback W01 |
| 2025-W09 | PosterSum | 24 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | Beyond Next-Token / xAR | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | LongRoPE2 | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | ArtGS | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | FUSED / Reversible Federated Unlearning | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Relation-Specific Neurons | 26 | Full Source Review Complete | Books Pending — No Change Candidate |
| 2025-W09 | MAMUT | 22 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Downstream Model Evidence Missing |
| 2025-W09 | DVPO / Pretrain Value, Not Reward (v1) | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Theorem Assumptions Restricted |
| 2025-W09 | NeoBERT | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Ext2Gen v1 | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Artifact Unreleased at v1 |
| 2025-W09 | SuperRAG | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Core Parser Not Open |
| 2025-W09 | R2-T2 | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / High Test-time FLOP Cost |
| 2025-W09 | Self-rewarding Correction | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Internal Reward Not Independent |
| 2025-W09 | SoRFT | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Proxy Reward False Negatives |
| 2025-W09 | UniTok | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | EDGS / Sparse Time-Variant Gaussian Splatting | 23 | Full Source Review Complete | Books Pending — No Change Candidate / Rendering Evidence Only |
| 2025-W09 | FINEREASON | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | FlexiDiT | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | MedVLM-R1 v1 | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Reasoning Faithfulness Unverified |
| 2025-W09 | Mobius | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Training-Free Base-Model Bound |
| 2025-W09 | Dream Engine / Multimodal Representation Alignment | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | R1-T1 v1 | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / v1 Evidence Incomplete |
| 2025-W09 | Variational Consistency Training / VCT | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Predictive Data Selection / PreSelect | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Chain of Draft | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Prompting Case |
| 2025-W09 | DeepSolution / SolutionRAG | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Domain Case |
| 2025-W09 | ViDoRAG / ViDoSeek | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | LettuceDetect | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | TeleRAG | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | DexGraspVLA | 27 | Full Source Review Complete | Books Pending — Experimental Embodied Branch |
| 2025-W09 | TokenSwift / Ultra-long Sequence Generation | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Efficient Test-Time Scaling via Self-Calibration | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | DuoDecoding | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Web AI Agent Vulnerability | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | LLM as a Broken Telephone | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W09 | Evaluating Intelligence via Trial and Error | 22 | Full Source Review Complete | Books Pending — Experimental Evaluation Frame / Extrapolation Disputed |
| 2025-W10 | EAGLE-3 | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Mistral OCR | 19 | Low-score Verification Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W10 | Visual-RFT | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Cognitive Behaviors / Four Habits of STaRs | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | LLM Apprehension and Uncertainty | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Liger | 27 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W10 | Large-Scale Data Selection for Instruction Tuning | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | SampleMix | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | RSQ | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | MultiAgentBench | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | MPO / Meta Plan Optimization | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Mask-DPO | 27 | Full Source Review Complete | Books Pending — Experimental Factuality Alignment |
| 2025-W10 | PipeOffload | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | IVR / Evolutionary Guided Decoding | 26 | Full Source Review Complete | Books Pending — Experimental Guided-Decoding Branch |
| 2025-W10 | AppAgentX | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | HoT / Highlighted Chain of Thought | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate / Over-trust Risk |
| 2025-W10 | Process-based Self-Rewarding Language Models | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | KodCode | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Gen3C | 25 | Full Source Review Complete | Books Pending — Experimental Generation Branch |
| 2025-W10 | ToolRet / Retrieval Models Aren't Tool-Savvy | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | START | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | STORM | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Audio Flamingo 2 | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | JAX 0.5.2 | 17 | Low-score Verification Complete | Weekly Only — Patch Release / No New Core Mechanism |
| 2025-W10 | LLMVoX | 19 | Low-score Verification Complete | Weekly Only — Domain Model |
| 2025-W10 | EgoLife | 19 | Low-score Verification Complete | Weekly Only — Application Case |
| 2025-W10 | LINGOLY-TOO | 18 | Low-score Verification Complete | Weekly Only — Evaluation Case |
| 2025-W10 | IFIR | 19 | Low-score Verification Complete | Weekly Only — Domain Retrieval Benchmark |
| 2025-W10 | Unified Reward Model | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Sketch-of-Thought | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Forgetting Transformer / FoX | 28 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W10 | R1-Searcher | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | SafeArena | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Learning from Failures / Multi-Attempt RL | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Linear-MoE | 28 | Full Source Review Complete | Books Pending — Experimental Architecture Branch |
| 2025-W10 | WildIFEval | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Long-Output LLM Survey | 23 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | VisualSimpleQA | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | MoE-X / Intrinsically Interpretable MoE | 27 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W10 | Capacity-Aware Inference | 28 | Full Source Review Complete — v1 mechanism locked | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Collapse of Dense Retrievers | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | OTTER | 27 | Full Source Review Complete | Books Pending — Experimental Embodied Branch |
| 2025-W10 | MagicInfinite | 26 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W10 | AI4SE Benchmark Review / BenchScout / BenchFrame | 25 | Full Source Review Complete — v1 census locked | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | LaMaTE / LLM as MT Encoder | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | More Documents, Same Length | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | ONNX Runtime v1.21.0 | 26 | Full Source Review Complete — W11 fixed-source spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Trajectory Distribution Matching / TDM | 29 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W10 | ProJudge | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | ARMOR v0.1 | 27 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W10 | GoalFlow | 27 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Embodied Branch |
| 2025-W10 | DropletVideo | 28 | Full Source Review Complete — Teacher/Prompt/Compute Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W10 | Mechanistic Interpretability Adversarial Attack / SSR | 26 | Full Source Review Complete — White-box/Small-model/Transfer Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Gemma 3 | 21 | Full Source Review Complete | No Change — Already Covered |
| 2025-W11 | OpenAI Responses API / Agents SDK launch | 26 | Full Source Review Complete | Books Pending — Refine Agent Platform Interface Contract |
| 2025-W11 | Block Diffusion / BD3-LM | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Search-R1 | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Transformers without Normalization / DyT | 28 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | DiLoCo Scaling Laws | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Self-Taught Self-Correction / STaSC | 25 | Full Source Review Complete | Books Pending — Experimental Self-Correction Branch |
| 2025-W11 | World Modeling Planner / D²PO | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | VisualPRM | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Open-Sora 2.0 | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | GTR / Guided Thought Reinforcement | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | CoRe² | 26 | Full Source Review Complete | Books Pending — Experimental Inference-Guidance Branch |
| 2025-W11 | VisualWebInstruct | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | R1-Onevision | 26 | Full Source Review Complete | Books Pending — Experimental Multimodal Reasoning Branch |
| 2025-W11 | CoSTAast | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Hugging Face Model Atlas | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | SGLang v0.4.4 | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Gemini Embedding | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Domain Draft Models for Speculative Decoding | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | LMM-R1 | 27 | Full Source Review Complete | Books Pending — Experimental Multimodal RL Branch |
| 2025-W11 | ProjectEval | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | FaceID-6M | 24 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Words and Deeds Consistency Test | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | MOMA-QA / SGVLM | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | ARRA | 27 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | NFIG | 27 | Full Source Review Complete with Revision Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | SEA-VL | 26 | Full Source Review Complete with Revision Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Meta Reinforcement Fine-Tuning / MRT | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Seedream 2.0 | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | OmniMamba | 28 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | LocAgent | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Second Me | 25 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Perplexity-Trap | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Ideas in Inference-time Scaling for Generative Pre-training | 22 | Full Source Review Complete | Weekly Only — Position Paper / Primary Evidence Required |
| 2025-W11 | Inductive Moment Matching | 29 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Exploiting Instruction-Following Retrievers for Malicious IR | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Implicit Reasoning through Shortcuts | 26 | Full Source Review Complete — ACL paper used after v1 HTML failure | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Video Action Differencing / VidDiff | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | SegAgent / HLMAT | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | LightGen | 27 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Semanticist / PCA-like Visual Tokens | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | RFLAV | 26 | Full Source Review Complete with HTML/PDF Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | RayFlow | 26 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | QuoTA | 27 | Full Source Review Complete with HTML/PDF Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | PlainQAFact | 25 | Full Source Review Complete — v1 locked | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | NullFace | 24 | Full Source Review Complete | Books Pending — Experimental Privacy Mechanism / No Guarantee |
| 2025-W11 | TPDiff | 27 | Full Source Review Complete with HTML/PDF Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Cost-Optimal GQA | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | MoC / Mixture-of-Chunkers | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | BIMBA | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | RewardSDS | 27 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | VLog | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Alias-Free LDM | 26 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | GoT / Generation Chain of Thought | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | SANA-Sprint | 28 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Light-R1 | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | DiT-Air | 27 | Full Source Review Complete with HTML/PDF Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | GroundingSuite | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | ARPG / Randomized Parallel Decoding | 28 | Full Source Review Complete with Revision Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | M-Attack / Simple Black-box LVLM Attack | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | TruthPrInt | 28 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Curse of Conditions / C²OT | 29 | Full Source Review Complete with Revision Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Silent Branding Attack | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | 4D LangSplat | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | OmniPaint | 27 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | New Trends for Modern Machine Translation with LRMs | 22 | Full Source Review Complete | Weekly Only — Position Paper / Primary Evidence Required |
| 2025-W11 | Distilling Diversity and Control in Diffusion Models | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Long Context Tuning for Video Generation | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | CINEMA | — | Unverified / Blocked — v1 full text unavailable | Books Frozen — P1 Full Text Required |
| 2025-W11 | Taxonomy Image Generation Benchmark | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Image Transform Understanding Limitations | 25 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | ConsisLoRA | 26 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Piece it Together / IP-Prior | 25 | Full Source Review Complete | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Whisper Quantization Comparative Analysis | 18 | Low-score Verification Complete | Weekly Only — Small-sample Implementation Study |
| 2025-W11 | Influential Neuron Path in Vision Transformers | 26 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | UniGoal | 27 | Full Source Review Complete with Revision Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | MinorBench | 27 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Bug-report Toxicity Study | 14 | Low-score Verification Complete | Weekly Only — Outside AI System Core Scope |
| 2025-W11 | PerCoV2 | — | Unverified / Blocked — v1 full text unavailable | Books Frozen — P1 Full Text Required |
| 2025-W11 | PoseLess | 21 | Full Source Review Complete | Books Pending — Experimental Embodied Branch |
| 2025-W11 | Classifier(-Free) Guidance Study | 28 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Cohere Command A | 29 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | ERNIE 4.5 / X1 Joint Launch | 26 | Full Source Review Complete — Mechanism Partially Disclosed | Weekly Only — Books Frozen |
| 2025-W11 | Accelerate v1.5.0 | 20 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Kubernetes v1.32.3 | 22 | Full Source Review Complete | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | SmolDocling | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | ReCamMaster | 27 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W11 | PLADIS | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W11 | VGGT | 29 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | API Agents vs. GUI Agents | 23 | Full Source Review Complete — Position/Survey Evidence | Weekly Only — Primary Comparative Evidence Required |
| 2025-W11 | Adversarial Data Collection | 27 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Vamba | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W11 | FlowTok | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W11 | TxAgent | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | State Space Models Survey | 23 | Full Source Review Complete — Evolution Taxonomy | Weekly Only — Primary Papers Own Mechanism Claims |
| 2025-W11 | Gradient Inversion Attacks in Federated Learning | 27 | Full Source Review Complete with Revision Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | GROVE / HowToGround1M | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Kolmogorov-Arnold Attention / KArAt | 25 | Full Source Review Complete — Negative Evidence Preserved | Books Pending — Experimental Alternative Branch |
| 2025-W11 | ETCH | 22 | Full Source Review Complete | Weekly Only — Domain-specific Mechanism Case |
| 2025-W11 | Neighboring Autoregressive Modeling / NAR | 28 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Experimental Alternative Branch |
| 2025-W11 | SPIRE | 27 | Full Source Review Complete — W12 recommendation-lag spillback | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | MaRI | 26 | Full Source Review Complete — Cross-domain Representation/Data Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | CHOrD | 27 | Full Source Review Complete — Static Scene / World-model Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | TreeMeshGPT | 27 | Full Source Review Complete — Topology/Ordering Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Analogical Reasoning under Perceptual Uncertainty | 28 | Full Source Review Complete — Symbolic Uncertainty Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Cockatiel | 27 | Full Source Review Complete — Scorer/Teacher/Data Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Open-World Skill Discovery | 28 | Full Source Review Complete — Conditional Boundary-signal Assumptions | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Group-robust Machine Unlearning | 27 | Full Source Review Complete — Group-annotation / Classification Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Being-0 | 29 | Full Source Review Complete — Timescale/Connector/Safety Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | SPIN-Bench | 27 | Full Source Review Complete — Harness/Judge/Assignment Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | reWordBench | 28 | Full Source Review Complete — Transformation/Judge/Calibration Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | V-STaR | 27 | Full Source Review Complete — Ground-truth Injection / Missing Supplement Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | WISA | 27 | Full Source Review Complete — Semantic Physics / Evaluator Boundary | Books Pending — Experimental Alternative Branch |
| 2025-W11 | Personalize Anything | — | Unverified / Blocked — v1 PDF exceeds access path and HTML is template | Books Frozen — P1 Full Text Required |
| 2025-W11 | Human-Aligned Uncertainty | 24 | Full Source Review Complete — Human-group / Correctness-calibration Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | Multimodal CoT Survey | 23 | Full Source Review Complete — Survey Taxonomy / No Primary Mechanism | Weekly Only — Primary Papers Own Claims |
| 2025-W11 | LVAS-Agent | 27 | Full Source Review Complete — Role/Artifact/Benchmark Boundary | Books Pending — Refine Existing Argument Candidate |
| 2025-W11 | AudioX | 27 | Full Source Review Complete — Masking/Data/Revision Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W11 | CapArena | 27 | Full Source Review Complete — Human/Judge/Ranking Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W11 | Atlas | 27 | Full Source Review Complete — Hierarchy/Upsampling/Runtime Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W11 | Gemini Robotics family | — | Canonical Owner Review Pending — first public 2025-03-12; W13 report is related evidence | Books Frozen |
| 2025-W11 | A Framework for Evaluating Emerging Cyberattack Capabilities of AI | — | Canonical Owner Reconciliation Pending — v1 2025-03-14; review packet recommends 27, W14 announcement is related evidence | Books Frozen |
| 2025-W12 | Private prediction for large-scale synthetic text generation | 23 | Source Review Complete — Weekly Gate Reopened | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | NVIDIA Dynamo | 27 | Source Review Complete — Weekly Gate Reopened | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | SGLang joins PyTorch ecosystem | 20 | Source Review Complete — Weekly Gate Reopened | Books Frozen — Governance Fact |
| 2025-W12 | RWKV-7 / Goose | 29 | Full Source Review Complete — Constant-state / Finite-memory Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | DAPO | 29 | Full Source Review Complete — Math/Verifier/Rollout-cost Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | R1-VL / StepGRPO | 27 | Full Source Review Complete — Teacher-key-step / Format-reward Boundary | Books Frozen — Provisional Experimental Candidate |
| 2025-W12 | VideoMind / Chain-of-LoRA | 28 | Full Source Review Complete — Proposal/Verifier/Latency Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | DreamRenderer | 27 | Full Source Review Complete — Local/Global Binding / Artifact-timeline Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | MicroVQA | 26 | Full Source Review Complete — Constructor Bias / MCQ / Expert-sample Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | Edit Transfer | 23 | Full Source Review Complete — Relation/Layout/Unseen-edit Boundary | Books Frozen — Provisional Experimental Candidate |
| 2025-W12 | BlobCtrl | 27 | Full Source Review Complete — Typed-state/Baseline/Single-element Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | WideRange4D / Progress4D | 22 | Full Source Review Complete — Curriculum/Synthetic/Non-causal Boundary | Books Frozen — Provisional Experimental Candidate |
| 2025-W12 | R0 / Rewards Are Enough | 28 | Full Source Review Complete — Prior/Reward/Evaluator-circularity Boundary | Books Frozen — Provisional Experimental Candidate |
| 2025-W12 | Impossible Videos / IPV-Bench | 26 | Full Source Review Complete — Counterfactual-prompt / Judge-coupling Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | Creation-MMBench | 25 | Full Source Review Complete — Creative-quality / Visual-factuality / Judge-policy Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | DeepPerception v1 / later KARL family | 28 | Full Source Review Complete — CoT-teacher / Grounding-reward / Revision Boundary | Books Frozen — Provisional Experimental Candidate |
| 2025-W12 | Infinite Mobility | 25 | Full Source Review Complete — Executable-articulation / Rule-authorship / Sim-to-real Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | Multimodal Preference Alignment Survey | 24 | Full Source Review Complete — Survey Taxonomy / No Primary Mechanism | Weekly Only — Source Map |
| 2025-W12 | Frac-Connections | 27 | Full Source Review Complete — Fixed-width State / Unmeasured Runtime Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | Cosmos-Transfer1 | 29 | Full Source Review Complete — Typed Control-map Fusion / Rack-contract Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | Measuring AI Ability to Complete Long Tasks | 29 | Full Source Review Complete — Human-time / Reliability-horizon Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | FlexWorld | 24 | Full Source Review Complete — Imagined Observation / Persistent-state Commit Boundary | Books Frozen — Provisional Refine Candidate |
| 2025-W12 | When Less is Enough | — | Review Pending — identity/date verified; arXiv:2503.16660 v1 2025-03-20 | Books Frozen |
| 2025-W12 | MAPS | — | Review Pending — identity/date verified; arXiv:2503.16905 v1 2025-03-21 | Books Frozen |
| 2025-W12 | Long Context Survey | — | Review Pending — identity/date verified; arXiv:2503.17407 v1 2025-03-20 | Books Frozen |
| 2025-W12 | MARS | — | Review Pending — identity/date verified; arXiv:2503.16874 v1 2025-03-21 | Books Frozen |
| 2025-W12 | RoboFactory | — | Review Pending — identity/date verified; arXiv:2503.16408 v1 2025-03-20 | Books Frozen |
| 2025-W12 | Creative Writing Post-training | — | Review Pending — identity/date verified; arXiv:2503.17126 v1 2025-03-21 | Books Frozen |
| 2025-W12 | Bridging Continuous and Discrete Tokens | — | Review Pending — identity/date verified; arXiv:2503.16430 v1 2025-03-20 | Books Frozen |
| 2025-W12 | OpenVLThinker | — | Review Pending — identity/date verified; arXiv:2503.17352 v1 2025-03-21 | Books Frozen |
| 2025-W12 | Versatile Controls | — | Review Pending — identity/date verified; arXiv:2503.16983 v1 2025-03-21 | Books Frozen |
| 2025-W12 | MathFlow | — | Review Pending — identity/date verified; arXiv:2503.16549 v1 2025-03-19 | Books Frozen |
| 2025-W12 | ETVA | — | Review Pending — identity/date verified; arXiv:2503.16867 v1 2025-03-21 | Books Frozen |
| 2025-W12 | FastCuRL | — | Review Pending — identity/date verified; arXiv:2503.17287 v1 2025-03-21 | Books Frozen |
| 2025-W12 | AgentRxiv | — | Review Pending — identity/date verified; arXiv:2503.18102 v1 2025-03-23 | Books Frozen |
| 2025-W12 | Judge Anything | — | Review Pending — identity/date verified; arXiv:2503.17489 v1 2025-03-21 | Books Frozen |
| 2025-W12 | Vision-R1 | — | Review Pending — identity/date verified; arXiv:2503.18013 v1 2025-03-23 | Books Frozen |
| 2025-W12 | LEMMA | — | Review Pending — identity/date verified; arXiv:2503.17439 v1 2025-03-21 | Books Frozen |
| 2025-W12 | V-Seek | — | Review Pending — identity/date verified; arXiv:2503.17422 v1 2025-03-21 | Books Frozen |
| 2025-W12 | CODA | — | Review Pending — identity/date verified; arXiv:2503.17760 v1 2025-03-22 | Books Frozen |
| 2025-W12 | Mind with Eyes | — | Review Pending — identity/date verified; arXiv:2503.18071 v1 2025-03-23 | Books Frozen |
| 2025-W12 | PhysTwin | — | Review Pending — identity/date verified; arXiv:2503.17973 v1 2025-03-23 | Books Frozen |
| 2025-W12 | MDocAgent | — | Review Pending — identity/date verified; arXiv:2503.13964 v1 2025-03-18 | Books Frozen |
| 2025-W13 | Gemini 2.5 Pro | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Tracing the thoughts of a large language model | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Reasoning Features via SAE | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | SimpleRL-Zoo | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | xKV | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | FFN Fusion | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Video SimpleQA | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Trajectory Balance with Asynchrony | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | CoMP multimodal continual pretraining | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Video-T1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Aether | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | LookAhead Tuning | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | CaMeL | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | CFG-Zero* | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Reasoning to Learn from Latent Thoughts | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | FAR | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Inference-Time Scaling for Flow Models | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | ReSearch | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Video Hallucination | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Dita | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Think Twice | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | PS3 / Scaling Vision Pretraining to 4K | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | LogQuant | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | LEGO Puzzles | 19 | Low-score Source/Date/Rejection Verified | Low Score — Narrow benchmark scope |
| 2025-W13 | Open Deep Search | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Qwen2.5-Omni Technical Report | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | ViLBench | 19 | Low-score Source/Date/Rejection Verified | Low Score — Narrow evaluation evidence |
| 2025-W13 | MCTS-RAG | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Synthetic Video Physical Fidelity | 19 | Low-score Source/Date/Rejection Verified | Low Score — Evaluation-only evidence |
| 2025-W13 | GPT-4o Image Generation | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | DAT / Dynamic Alpha Tuning | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Aurelia | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Evolutionary Prompt Optimization for VLMs | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | RARE | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Shape and Texture Recognition in Large Vision-Language Models | 18 | Low-score Source/Date/Rejection Verified | Low Score — Representation diagnostic only |
| 2025-W13 | A Survey on Unlearnable Data | 19 | Low-score Source/Date/Rejection Verified | Low Score — Secondary synthesis only |
| 2025-W13 | Anthropic Economic Index: Insights from Claude 3.7 Sonnet | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Usage/sampling evidence |
| 2025-W13 | Meta / Cornerstone XR Training with Llama | 10 | Low-score Source/Date/Rejection Verified | Ignored Noise — Product case without mechanism contract |
| 2025-W13 | Unified Multimodal Discrete Diffusion | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | JavisDiT | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | AdaptiVocab | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Exploring Data Scaling Trends and Effects in RLHF | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Scaling Laws in Scientific Discovery with AI and Robot Scientists | 18 | Low-score Source/Date/Rejection Verified | Low-score closure — Conceptual perspective without scaling evidence |
| 2025-W13 | ResearchBench | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Olympiad Math Benchmark | 19 | Low-score Source/Date/Rejection Verified | Low Score — Incremental benchmark evidence |
| 2025-W13 | Agent Survey | 19 | Low-score Source/Date/Rejection Verified | Low Score — Secondary synthesis only |
| 2025-W13 | UI-R1 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Embodied-Reasoner | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | ReaRAG | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | LeX-Art | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | VBench 2.0 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Lumina-Image 2.0 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Video-R1 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Understanding R1-Zero-Like Training | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | CodeARC | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Quamba2 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Landscape of Thoughts | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Towards Trustworthy GUI Agents | 19 | Low-score Source/Date/Rejection Verified | Low Score — Secondary source map |
| 2025-W13 | Megatron-LM Multi-Token Prediction support | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W13 | Transformers 4.50 patch family | 14 | Low-score Source/Date/Rejection Verified | Low Score — Version patch family |
| 2025-W13 | DeepSpeed v0.16.5 | 16 | Low-score Source/Date/Rejection Verified | Low Score — Patch-family implementation facts |
| 2025-W13 | vLLM 2025 Q2 roadmap | 16 | Low-score Source/Date/Rejection Verified | Low Score — Planning intent, not shipped behavior |
| 2025-W14 | Llama 4 Scout and Maverick | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Open-Reasoner-Zero | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Multi-Token Attention | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Open-Qwen2VL | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Agent S2 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | PaperBench | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | ZClip | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Generalist Reward Modeling | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Rethinking RL Scaling for VLMs | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Expanding RLVR | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | JudgeLRM | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | vsGRPO | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | RIG | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | ILLUME+ | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | YourBench | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | MergeVQ | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | ShortV | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | KServe v0.15.0 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | vLLM v0.8.3 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Accelerate v1.6.0 | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | VerifiAgent | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Z1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | When To Solve, When To Verify | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | SEED-Bench-R1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | GenPRM | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Efficient LLaMA-3.2-Vision | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | m1 Medical Reasoning | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Thinking Intervention | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Query and Conquer | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Any2Caption | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | ScholarCopilot | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | RISEBench | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Speech–Text Scaling | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | FreSca | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Sparse Autoencoders for VLMs | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Nova Act | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Transformers v4.51.0 | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | An Approach to Technical AGI Safety and Security | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | ACTalker | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | SkyReels-A2 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | WikiVideo | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | OpenCodeReasoning | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Entropy-Based Adaptive Weighting for Self-Training (EAST) | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | AdaMMS | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Scaling Language-Free Visual Representation Learning | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Command A | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | GeometryCrafter | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Recitation over Reasoning (RoR-Bench) | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Chapter-Llama | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | AnimeGamer | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | DreamActor-M1 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | VideoScene | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Articulated Kinematics Distillation | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Safeguarding Vision-Language Models | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth) | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Instruction-Guided Parameter Generation (IGPG) | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Rethinking Reflection in Pre-Training | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W14 | Foundation Agents Survey | 19 | Low-score Source/Date/Rejection Verified | Low Score — Secondary taxonomy/source map |
| 2025-W14 | Test-Time Scaling Survey | 19 | Low-score Source/Date/Rejection Verified | Low Score — Secondary synthesis only |
| 2025-W14 | GPT-ImgEval | 19 | Low-score Source/Date/Rejection Verified | Low Score — Proprietary UI/version capability snapshot |
| 2025-W14 | TensorRT-LLM v0.18.0 | 18 | Low-score Source/Date/Rejection Verified | Low Score — Version/Dependency/Breaking Fact |
| 2025-W15 | Kimi-VL | 22 | Full Source Review Complete — Weekly Only — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W15 | Agent2Agent / A2A | 28 | Full Source Review Complete — Refine Candidate — narrowed launch boundary | Books Frozen — Historical Gate Closed |
| 2025-W15 | Google ADK v0.1.0 | 26 | Full Source Review Complete — No Change — Existing contract | Books Frozen — Historical Gate Closed |
| 2025-W15 | Ironwood TPU | 25 | Full Source Review Complete — Weekly Only — Hardware fact | Books Frozen — Historical Gate Closed |
| 2025-W15 | Amazon Nova Sonic | 24 | Full Source Review Complete — Weekly Only — Mechanism not disclosed | Books Frozen — Historical Gate Closed |
| 2025-W15 | Hogwild! Inference | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | HybriMoE | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | VAPO | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | OLMoTrace | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | SmolVLM | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | One-Minute Video Generation with TTT | 25 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W15 | T1 / Tool-integrated Verification | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | Quantization Hurts Reasoning? | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | A Sober Look at Progress in LM Reasoning | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | SkillWeaver | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | Auditing Model Substitution in LLM APIs | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | Scaling Laws for Native Multimodal Models | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | Missing Premise exacerbates Overthinking | 25 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | DDT | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W15 | C3PO | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W15 | SGLang v0.4.5 | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | Seaweed-7B | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | GigaTok | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | MineWorld | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | VLM-R1 | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | PixelFlow | 25 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W15 | Pangu Ultra | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | SpecReason | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | PRIMA.cpp | 28 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | VL-Rethinker | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | AgentRewardBench | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | The AI Scientist-v2 | 26 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W15 | DUMP | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | MLRC-Bench | 27 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W15 | Nova Reel 1.1 | 18 | Low-score Source/Date/Rejection Verified — Weekly Only — Product fact | Books Frozen — Historical Gate Closed |
| 2025-W15 | TensorRT-LLM v0.18.1 | 16 | Low-score Source/Date/Rejection Verified — Weekly Only — Dependency revision | Books Frozen — Historical Gate Closed |
| 2025-W15 | Transformers v4.51.1/2 | 18 | Low-score Source/Date/Rejection Verified — Weekly Only — Patch facts | Books Frozen — Historical Gate Closed |
| 2025-W15 | Gemini 2.5 Flash preview | 19 | Low-score Source/Date/Rejection Verified — Weekly Only — Version fact | Books Frozen — Historical Gate Closed |
| 2025-W15 | VCR-Bench | 19 | Low-score Source/Date/Rejection Verified — Weekly Only — Benchmark | Books Frozen — Historical Gate Closed |
| 2025-W15 | MM-IFEngine | 19 | Low-score Source/Date/Rejection Verified — Weekly Only — Dataset/eval case | Books Frozen — Historical Gate Closed |
| 2025-W15 | SoTA with Less | 19 | Low-score Source/Date/Rejection Verified — Weekly Only — Author experiment | Books Frozen — Historical Gate Closed |
| 2025-W15 | PaperBench v3 | — | Related Primary Evidence — canonical owner/score is W14 | Books Frozen — No duplicate score |
| 2025-W15 | Rethinking Reflection | — | Spillback — arXiv v1 2025-04-05, canonical owner W14 | Books Frozen — No duplicate score |
| 2025-W15 | vLLM 2025 Q2 roadmap | — | Spillback — issue opened 2025-03-29, canonical owner W13 | Weekly Only — No duplicate score |
| 2025-W16 | GPT-4.1 API family | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Claude Research | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | OpenAI o3 and o4-mini | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Gemini 2.5 Flash preview | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | OpenAI Codex CLI | 25 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W16 | OpenAI Preparedness Framework v2 | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | RealHarm | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | AlayaDB | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Heimdall | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | M1 | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | SAIL | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | InternVL3 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | xVerify | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Layer-wise Gradients | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Efficient Reasoning Models Survey | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | ReZero | 21 | Disputed — Event-version Boundary | Books Frozen — Historical Gate Closed |
| 2025-W16 | Fluid-guided WAIT | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Minimalist Reasoning | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Seedream 3.0 | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | DataDecide | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | TextArena | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | SimpleAR | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | ReTool | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | DFloat11 | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | BitNet b1.58 2B4T | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | WorldMem | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | BrowseComp | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | FramePack | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | InstructRAG | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Conflicting RAG | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | EEF | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Antidistillation Sampling | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Nemotron-CLIMB | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Generate, but Verify | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Sleep-time Compute | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | MIRAS | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | PerceptionLM | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Perception Encoder | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | vLLM v0.8.4 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | From Large to Super-Tiny | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Time Up! | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | High-Throughput LLM Inference on Heterogeneous Clusters | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | HPU | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | SlimPipe | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Knowledge and Dataset Distillation Survey | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Don't Retrieve, Generate | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W16 | Transformers v4.51.3 | 16 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W16 | Self-Correction Makes LLMs Better Parsers | 18 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W16 | Multi-Agent Hazardous Object Detection | 18 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W16 | FAIRGAME | 19 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W17 | LUFFY | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | OTC-PO | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Efficient Pretraining Length Scaling / PHD Transformer | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Adaptive Parallel Reasoning | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | FlowReasoner | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Eagle2.5 | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | TTRL | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Tina | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Skywork-R1V2 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | AIMO-2 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | ThinkPRM | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Paper2Code | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Sparse Frontier | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | BitNet v2 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Kimi-Audio | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Pleias-RAG | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | PropRAG | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | OpenAI gpt-image-1 API | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Anthropic Harms Framework | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | Anthropic malicious-use report | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | PyTorch 2.7 | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Kubernetes v1.33 | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | SGLang v0.4.6 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | EasyEdit2 | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Kuwain 1.5B | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Trillion-7B technical report | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | VisuLogic | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Describe Anything Model | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Bitter Lesson from 2,000+ Multilingual Benchmarks | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | LiveCC | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | WALL-E 2.0 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | LLMs are Greedy Agents | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | ReflectionFlow | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Vidi | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | PHYBench | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Full-Stack Safety Survey | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Pre-DPO | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | I-Con | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | QuaDMix | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | MMLA benchmark | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | SAVA tokenizer adaptation | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | CameraBench | 22 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W17 | Zero-shot Subject Video Generation | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Step1X-Edit | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | RefVNLI | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | UniME | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | APC Mental Imagery | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Token-Shuffle | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | TimeChat-Online | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | DyMU | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Code-grounded math evaluation | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Auto-SLURP | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | DRAGON distributional reward optimization | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Quicksviewer adaptive video tokens | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Roll the Dice, but Look Before You Leap | 23 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W17 | RainbowPlus automated red teaming | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | CRUST-Bench | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | IV-Bench image-centric video understanding | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | MR Video long-video MapReduce | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | RePOPE hallucination re-evaluation | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | ReDi joint image-feature diffusion | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | DreamO unified image customization | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | DeGLA global-local vision-language alignment | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | Semantic Orders for autoregressive image generation | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W17 | RealisDance-DiT | 21 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W17 | All-Angles Bench | 20 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W17 | Uni3C unified 3D human control | 21 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W17 | DianJin-R1 | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | IberBench | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | VideoVista Cultural | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | Conversational Assistant study | 16 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | Preferred-MedLLM | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | MultiMind | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | Google Lyria 2 / Music AI Sandbox | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | CAPTURe occluded-object counting | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | IPBench intellectual-property reasoning | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | ViSMaP long-video summarization | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | DiMeR diffusion mesh reconstruction | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | 3DV-TON virtual try-on | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W17 | Dynamic Camera Poses dataset | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | GPT-4o sycophancy rollback and postmortem | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Qwen3 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Phi-4-reasoning | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Phi-4-Mini-Reasoning | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | DeepSeek-Prover-V2 | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | MiMo-7B release | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Amazon Nova Premier | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Llama-Nemotron technical report | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Mem0 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | One-shot RLVR | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | The Leaderboard Illusion | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | UniversalRAG | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | ReasonIR | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Meta Policy Optimization | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | WebThinker | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Softpick | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | TesserAct | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | NORA | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Mixture of Sparse Attention | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Graph-of-Tokens MoE routing | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Ava agentic video analytics | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Transferable black-box VLM attacks | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Self-generated in-context agent examples | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | PIPA interactive planning evaluation | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Always Tell Me The Odds | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | UQLM uncertainty-quantification suite | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | VideoHallu | 22 | Strict Full Source Review Complete — Terminal Disputed | Books Frozen — Historical Gate Closed |
| 2025-W18 | Towards Safer Pretraining / HarmFormer | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Ray 2.45.0 | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | TD-Eval | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Spark scientific idea-generation system | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | ARTIST / Agentic Reasoning and Tool Integration via RL | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | R&B Domain Regrouping and Data Mixture Balancing | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | SWE-smith | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Who&When Multi-Agent Failure Attribution | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Practical Efficiency of Muon for Pretraining | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W18 | Taming the Titans survey | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | A Survey on LLM-based Human-Agent Systems | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | Parameter-Efficient Transformer Embeddings | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | Controllable Weather Synthesis and Removal | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | Retrieval-augmented ICL for Multimodal Disease Classification | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | A Survey on Inference Engines for Large Language Models | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W18 | Low-Precision Training of Large Language Models | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W19 | Gemini 2.5 Pro I/O Preview update | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Anthropic Web Search API | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Anthropic AI for Science Program | 14 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W19 | Voila | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | LLaMA-Omni 2 | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | RM-R1 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | FormalMATH | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | R1-Reward | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | RetroInfer | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | ReplaceMe | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Absolute Zero | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | VITA-Audio | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | OpenHelix | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | OSUniverse | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | X-Reasoner | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | ZeroSearch | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | HunyuanCustom | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | OpenVision | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | General-Level / General-Bench | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | RL^V | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | SweRank | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Flow-GRPO | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Elastic Reasoning | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | ICon: In-Context Contribution | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | StreamBridge | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Toxicity in LLaVA pretraining data | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W19 | Seed1.5-VL Technical Report | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | AlphaEvolve | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Sufficient Context for RAG | 25 | Full Source Review Complete — 2025 Follow-up Node | Books Frozen — Historical Gate Closed |
| 2025-W20 | DeepSeek-V3 Hardware Co-design | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | BLIP3-o | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | OpenAI Codex cloud preview | 25 | Full Source Review Complete — Product Fact | Books Frozen — Historical Gate Closed |
| 2025-W20 | Parallel Scaling Law / ParScale | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | WorldPM | 25 | Full Source Review Complete — Primary Source Recovered | Books Frozen — Historical Gate Closed |
| 2025-W20 | MiniMax-Speech | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MLE-Dojo | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | OpenThinkIMG | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | EnerVerse-AC | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | GuardReasoner-VL | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Visual Planning | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MMLongBench | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | KServe v0.15.1 | 23 | Full Source Review Complete — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W20 | EWMBench | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Group Think | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MuToR | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | IKEA adaptive search | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Learning from Peers | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | DanceGRPO | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Continual-pretraining Learning Dynamics | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Overflow Prevention for Recurrent Long Context | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | ARC Text-to-Audio | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | AM-Thinking-v1 | 20 | Full Source Review Complete — Model Recipe Fact | Books Frozen — Historical Gate Closed |
| 2025-W20 | Aya Vision | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MulDimIF | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | NavDP | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | TRAIL | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Tests as Prompt / WebApp1K | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | System Prompt Optimization with Meta-Learning | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | CoT Encyclopedia | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | J1 Judge RL | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | WavReward | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Omni-R1 Audio | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Beyond Aha! | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | End-to-End Vision Tokenizer Tuning | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | SuperCoder | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Follow the Path | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MatTools | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Symbiotic Watermarking | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MPS-Prover | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Domain Case |
| 2025-W20 | GIE-Bench | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Domain Benchmark |
| 2025-W20 | VCRBench | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Domain Benchmark |
| 2025-W20 | SageAttention3 | 27 | Full Source Review Complete — Artifact Date Disputed | Books Frozen — Historical Gate Closed |
| 2025-W20 | UCGM | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | H3DP | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | R2R2R | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | TokenAdapt | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Continuous VAR | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Deep Fusion | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | UniSkill | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | PointArena | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Memorization-Compression Cycles | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Step1X-3D | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | MathCoder | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | Depth Any Prior | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | RAG hyperparameter sensitivity | 21 | Full Source Review Complete — Limited Study | Books Frozen — Historical Gate Closed |
| 2025-W20 | Behind the Scenes of Maya | 20 | Full Source Review Complete — Threshold Candidate | Books Frozen — Historical Gate Closed |
| 2025-W20 | HealthBench | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | OMol25 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | UMA | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W20 | NVIDIA NVLink Fusion | 23 | Full Source Review Complete — Mechanism Partially Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W20 | Time-R1 | 24 | Full Source Review Complete — W21 Spillback | Books Frozen — Historical Gate Closed |
| 2025-W20 | Orthogonal Residual Updates | 25 | Full Source Review Complete — W21 Spillback | Books Frozen — Historical Gate Closed |
| 2025-W20 | Synthetic Data RL | 25 | Full Source Review Complete — W21 Spillback | Books Frozen — Historical Gate Closed |
| 2025-W20 | BARREL | 23 | Full Source Review Complete — W21 Spillback；Numeric/Reward-order Dispute Preserved | Books Frozen — Historical Gate Closed |
| 2025-W20 | LightLab | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Generation Case |
| 2025-W20 | Style SVG | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Application |
| 2025-W20 | Agent taxonomy | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — Survey/Taxonomy |
| 2025-W20 | ReSurgSAM2 | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Segmentation |
| 2025-W20 | 3D-Fixup | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Limited System Transfer |
| 2025-W20 | QuXAI | 15 | Low-score Source/Date/Rejection Verified | Weekly Only — Weak Project Relevance |
| 2025-W20 | AdaptCLIP | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Incremental Adaptation |
| 2025-W20 | MetaUAS | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Anomaly Branch |
| 2025-W20 | OneNIP | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Imaging Pipeline |
| 2025-W20 | AnoGen | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Anomaly Generation |
| 2025-W20 | SkillFormer | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Insufficient System Principle |
| 2025-W20 | ViMRHP | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — Weak Transfer |
| 2025-W20 | VISTAR | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Incremental Benchmark |
| 2025-W20 | Meta brain-language study | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Scientific Explanation |
| 2025-W21 | llm-d community launch | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Claude 4 | 22 | Strict Full Source Review Complete — Version Fact / Mechanism Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W21 | User-level DP follow-up | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | AdaptThink | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | BRPO / AnytimeReasoner | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Efficient Agent Training for Computer Use | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | RLVR-World | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | UniVG-R1 | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Visual ARFT | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Scaling Law for QAT | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Vid2World | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Reasoning Models Better Express Confidence | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Hunyuan-Game | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Latent Flow Transformer | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Self-Braking Tuning | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Quartet | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Reward Reasoning Model | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | BAGEL / Emerging Properties in Unified Multimodal Pretraining | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Scaling Reasoning, Losing Control | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | RL-Tango | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Entropy Minimization in LLM Reasoning | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | BanditSpec | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Scaling DiT via muP | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Web-Shepherd | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Adaptive Self-Recovery Reasoning | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | LASER-D adaptive length reward | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Soft Thinking | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | dKV-Cache | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | VerifyBench: Benchmarking Reference-based Reward Systems | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | MMaDA | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Streamline Without Sacrifice / ProxyV | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Pixel Reasoner | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | QuickVideo | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Embodied MEMENTO | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | AceReason-Nemotron | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Tool-Star | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | WebAgent-R1 | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Jenga / Dynamic Token Carving | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | LLaDA-V | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | NovelSeek (renamed InternAgent in later revision) | 26 | Strict Full Source Review Complete — Dispute Boundary Preserved | Books Frozen — Historical Gate Closed |
| 2025-W21 | Dimple | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | GoT-R1 | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | QwenLong-L1 | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | TabSTAR | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Flex-Judge | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | VerIPO | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Data-centric compression | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | PATS | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | DeepResearchGym | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | NLWeb | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Anthropic API code execution / MCP connector / Files API | 22 | Strict Full Source Review Complete — Version Fact / Mechanism Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W21 | Anthropic ASL-3 safeguards | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Gemini Diffusion experimental preview | 19 | Low-score Source/Date/Rejection Verified — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W21 | Gemini universal-assistant / world-model vision | 18 | Low-score Source/Date/Rejection Verified — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W21 | Veo 3 / Imagen 4 launch family | 18 | Low-score Source/Date/Rejection Verified — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W21 | Gemma 3n preview | 19 | Low-score Source/Date/Rejection Verified — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W21 | Transformers v4.52.1 | 18 | Low-score Source/Date/Rejection Verified — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W21 | JAX v0.6.1 | 17 | Low-score Source/Date/Rejection Verified — Version Fact | Books Frozen — Historical Gate Closed |
| 2025-W21 | Distilling LLM Agent into Small Models with Retrieval and Code Tools | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Reasoning Model is Stubborn / ReasoningTrap | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | One RL to See Them All: Visual Triple Unified Reinforcement Learning | 23 | Strict Full Source Review Complete — Dispute Boundary Preserved | Books Frozen — Historical Gate Closed |
| 2025-W21 | PhyX | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | QwenLong-CPRS | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | EvoSearch | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | MOOSE-Chem3 | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | VeriThinker | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Direct3D-S2 | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | s3: You Don't Need That Much Data to Train a Search Agent via RL | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | AudioTrust | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | FullFront | 19 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W21 | TemplateRL / TAPO title-lineage family | 23 | Strict Full Source Review Complete — Dispute Boundary Preserved | Books Frozen — Historical Gate Closed |
| 2025-W21 | Trinity-RFT | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | CUB: Benchmarking Context Utilisation Techniques for Language Models | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Interactive Post-Training for Vision-Language-Action Models (RIPT-VLA) | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | ReflAct | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | NOVER | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Not All Models Suit Expert Offloading | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Keep Security! / CoPriva | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | FREESON | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Thinkless | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | OSWorld-G / Jedi | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | VSA sparse attention | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | LatentSeek | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | MM-PRM | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | FedSVD | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | R3 reward model | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | GS-Jacobi / TarFlow | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Low-Rank Clone | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Neurosymbolic Diffusion | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | AutoMat | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | CompeteSMoE | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | QZO | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | PiFlow | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | VisualQuality-R1 | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | RICE cognitive experts | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Distillation source matters | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Vittle | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Latent knowledge elicitation | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | AgentIF | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Think-RM | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | TinyV | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | LaViDa | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | FoVer | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | SafeKey | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | OViP | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | TON selective reasoning | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | SophiaVL-R1 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | BYE backdoor cleaning | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | SpatialScore | 24 | Strict Full Source Review Complete — Dispute Boundary Preserved | Books Frozen — Historical Gate Closed |
| 2025-W21 | OCR Heads | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | VLM-R3 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | LLM retraction / admit mistakes | 26 | Strict Full Source Review Complete — Dispute Boundary Preserved | Books Frozen — Historical Gate Closed |
| 2025-W21 | vLLM V0 deprecation RFC | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | MMMG | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Implicit multi-hop scaling | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | NFT negative-aware fine-tuning | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | SVL spiking V-L pretraining | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | MSPGT | 19 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W21 | MUG-Eval | 19 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W21 | Just as Humans Need Vaccines, So Do Models: Model Immunization to Combat Falsehoods | 18 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W21 | MemeReaCon | 19 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W21 | Reasoning Path Compression | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Lessons from Defending Gemini Against Indirect Prompt Injections | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | The Hallucination Tax of Reinforcement Finetuning | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | Be Careful When Fine-tuning On Open-Source LLMs | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | How Should We Enhance the Safety of Large Reasoning Models | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W21 | This Time is Different / Toto + BOOM | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | DeepSeek-R1-0528 | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Enigmata | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ARM | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Trajectory-Aided Reasoning | 17 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W22 | Intuitor | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Surrogate Signals | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Lifelong Safety Alignment | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | SynLogic | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | GraLoRA | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | rStar-Coder | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VeriFree | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Active-O3 | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VisTA | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Entropy Mechanism | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | SWE-rebench | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | R2R | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Skywork OR1 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | MM-UPT | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | WebDancer | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Multi-Agent Debate | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Fast-dLLM | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ZeroGUI | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | The Climb | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ATLAS | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Satori-SWE | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | UniRL | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | SWE-bench Live | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | KServe v0.15.2 patch | 17 | Low-score Source/Date/Rejection Verified | Books Frozen — Historical Gate Closed |
| 2025-W22 | Paper2Poster | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ScienceBoard | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Table-R1 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | MME-Reasoning | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Spatial-MLLM | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | BizFinBench | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | One-Step Text Generation | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VF-Eval | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | OpenS2V-Nexus | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Sherlock | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | SageAttention2++ | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | cadrille | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VideoReasonBench | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | UI-Genie | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | MME-VideoOCR | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | RenderFormer | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Multimodal RL Cold Start | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | D-AR | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Next-Event Prediction | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Video-Holmes | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Reasoning Models and Hallucination | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | KronSAE | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | LoRAShop | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | MotionPro | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ImgEdit | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Multi-Domain Preference Explainability | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VidText | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | FAMA | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Sentence-by-Sentence Prediction | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Omni-R1 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | StructEval | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | StressTest | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | JQL multilingual filtering | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Language neurons | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | REARANK | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | HoliTom | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VideoREPA | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Segment Policy Optimization | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Visual Embodied Brain | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Adaptive Parallel Decoding | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Gradient Grouping | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | VRAG-RL | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Text2Grad | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | MUSEG | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | KVzip | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | SafeScientist | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | GeoDrive | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | One-shot Entropy Minimization | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | MLR-Bench | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Reasoning-data Influence Functions | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | Afterburner | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | WINA | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ScaleKV | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | AIDSAFE | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | HoPE | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | ViGoRL | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W22 | TrustVLM | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Gateway API Inference Extension | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Beyond the 80/20 Rule | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | SmolVLA | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | UniWorld-V1 | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | GUI-Actor | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | SynthRL | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Sparse-vDiT | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Co-Evolving LLM Coder and Unit Tester | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | LongBioBench | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | MiMo-VL Technical Report | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | OpenThoughts3 | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Rectified Sparse Attention | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Qwen3 Embedding | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | ComfyUI-Copilot | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | The Common Pile v0.1 | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | SeedVR2 | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Video World Models with Long-term Spatial Memory | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | RoboRefer | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Diagonal Batching | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Surfer-H Meets Holo1 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Inference-Time Hyper-Scaling with KV Cache Compression | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Evaluation is All You Need | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Search Arena | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | StreamBP | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | MINT-CoT | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | MedAgentGym | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | ReVisual-R1 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | SuperWriter | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Voyager | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Shortcut Neuron Evaluation | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Small Language Models for Agentic AI | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | PosS | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Critique-GRPO | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Urania | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Contextual Integrity via Reasoning and RL | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Watermarking Degrades Alignment | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Quantitative LLM Judges | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | AmbiK | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | VisCoder | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | ECoRAG | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Bootstrapping World Models from Dynamics Models | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Astra | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Cartridges | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | Saffron-1 | 28 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W23 | ConfQA | 28 | Strict Full Source Review Complete — Revision Lineage Disputed | Books Frozen — Historical Gate Closed |
| 2025-W23 | EOC-Bench | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W23 | MMR-V | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W23 | Kinetics | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W23 | Scaling Laws for Robust Comparison of Open Foundation LVMs | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W24 | Reinforcement Pre-Training | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | MiniCPM4 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | τ²-Bench | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | V-JEPA 2 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | MVP / Minimal Video Pairs | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | CausalVQA | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | IntPhys 2 | 24 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | Measuring multi-calibration / McMetric | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | NVIDIA GR00T N1.5 | 29 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | GTA1 / Grounding-R1 | 27 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | HF/NVIDIA Training Cluster as a Service | 24 | Full Source Review Complete | Weekly Only — Version/Product Fact |
| 2025-W24 | Scientists' First Exam | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | AutoMind | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | AbstentionBench | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | DeepResearch Bench | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | CUDA-LLM | 24 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | VIKI-R | 24 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | Mirage-1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | FGN / probabilistic weather forecasting from marginals | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Domain2Vec | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | SWE-Factory | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | VerIF | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Thinking vs. Doing / TTI | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Self Forcing | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | NoLoCo | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | SAFEFLOW | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Build the Web for Agents | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Through the Valley | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Draft-based Approximate Inference | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | RuleReasoner | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Ming-Omni | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | ReasonMed | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | SpatialLM | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | BitVLA | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | CyberV | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | GUI-Reflection | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Compound AI Systems Optimization survey | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | EmbodiedGen | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | VideoDeepResearch / VideoExplorer v1 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Magistral | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | SGLang v0.4.7 | 27 | Full Source Review Complete | Weekly Only — Version/Product Fact |
| 2025-W24 | vLLM v0.9.1 | 29 | Full Source Review Complete | Refine — Existing Argument / Versioned Engine Contract |
| 2025-W24 | NVIDIA TensorRT for RTX first SDK release | 28 | Full Source Review Complete | Refine — New Execution-Plan Lifecycle / SDK Contract |
| 2025-W24 | NVIDIA Cosmos Predict-2 open artifact release | 27 | Full Source Review Complete | Emerging / Experimental — Open World-Model Artifact |
| 2025-W24 | NVIDIA Data Flywheel Blueprint | 26 | Full Source Review Complete | Refine — Continuous Model Promotion Contract |
| 2025-W24 | Unified NVIDIA NIM model/backend-selection workflow | 25 | Full Source Review Complete | Refine — Serving Profile Selection Contract |
| 2025-W24 | Open-source NVIDIA AI-Q Blueprint | 27 | Full Source Review Complete | Refine — Typed Enterprise Agent Workflow |
| 2025-W24 | cuEquivariance v0.5 triangle-operation kernels | 28 | Full Source Review Complete | Integrate — New Domain-Specific Execution Mechanism |
| 2025-W24 | Holoscan Sensor Bridge v2.0 | 27 | Full Source Review Complete | Refine — Real-Time Sensor State Contract |
| 2025-W24 | OneIG-Bench | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | ViGaL / Play to Generalize | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | Resa / SAE-Tuning | 23 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | Optimus-3 v1 | 23 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | OpenAI o3-pro launch | 20 | Full Source Review Complete | Weekly Only — Mechanism Not Disclosed |
| 2025-W24 | Apple Foundation Models framework | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | NVIDIA NIM security | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W24 | UTBoost | 29 | Full Source Review Complete | Refine — Existing Argument / Books Frozen |
| 2025-W24 | ChineseHarm-Bench | 28 | Full Source Review Complete | Refine — Existing Argument / Books Frozen |
| 2025-W24 | Foundation Models in Autonomous Driving survey | 24 | Full Source Review Complete | No Change — Already Covered / Survey Evidence |
| 2025-W24 | Ray 2.47.0 | 28 | Full Source Review Complete | Refine — Existing Argument / Version-bounded Case |
| 2025-W24 | Distributed LLM Framework Bugs | 28 | Full Source Review Complete | Refine — Existing Argument / Reliability Evidence |
| 2025-W24 | OPT-BENCH | 26 | Full Source Review Complete | Refine — Existing Argument / Benchmark Evidence |
| 2025-W24 | EQA-RM | 25 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | VGC-Bench v1 | 24 | Full Source Review Complete | Refine — Existing Argument / Benchmark Evidence |
| 2025-W24 | COPE v1 / Collaborative LLM Inference via Planning | 26 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Chelsea v1 / later CentroidKV | 28 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | QA-LIGN v1 | 27 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | TACA | 25 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Uncertainty-o | 28 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | SUDER / Dual Self-Rewards | 25 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Latent Multi-Head Attention for Small Language Models | 20 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Brevity is the Soul of Sustainability | 25 | Full Source Review Complete | Refine — Existing Argument / Books Frozen |
| 2025-W24 | MIRAGE retinal OCT foundation model | 25 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | DeepForm / CSFRC / C-ReMax | 23 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | ReGuidance | 22 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | GA-LLM structured optimization | 17 | Low-score Source/Date/Rejection Verified | Rejected — Circular Evaluator / Qualitative Evidence |
| 2025-W24 | Dreamland | 27 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | ASVR | 26 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | DRAGged into Conflicts / CONFLICTS | 29 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | Kyvo / Aligning Text, Images, and 3D Structure | 27 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | AniMaker | 22 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | VRBench | 26 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | HeadHunter / SoftPAG | 24 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | LLM Unlearning Should Be Form-Independent / ORT + ROCR | 28 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | TaxoAdapt | 26 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | ClaimSpect / Beyond True or False | 27 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | HCA / Hierarchical Latent Capabilities | 29 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Discrete Audio Tokens: More Than a Survey! | 27 | Full Source Review Complete | Integrate — New Mechanism / Survey + Benchmark Evidence |
| 2025-W24 | PosterCraft | 24 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | CreatiPoster | 25 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | DreamActor-H1 | 21 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | Attention, Please! / Efficient Probing | 27 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | UniPre3D | 25 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | StreamSplat | 26 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | SNMF MLP feature decomposition | 27 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Text-Aware Image Restoration / TAIR–TeReDiff | 25 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | Token Perturbation Guidance | 24 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | TeleMath | 22 | Full Source Review Complete | No Change — Already Covered / Domain Case |
| 2025-W24 | AutoSDT / AutoSDT-5K | 29 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | PartPacker / Dual Volume Packing | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | TaskCraft | 29 | Full Source Review Complete | Integrate — New Mechanism / Experimental |
| 2025-W24 | Formalizing Learning from Language Feedback / HELiX | 29 | Full Source Review Complete | Integrate — New Mechanism / Theory-bounded |
| 2025-W24 | RAG+ | 27 | Full Source Review Complete | Refine — Existing Argument / Experimental |
| 2025-W24 | Configurable Preference Tuning | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W24 | Comment on The Illusion of Thinking | 20 | Disputed — Source Complete / Artifact Not Released | Books Frozen — Preliminary Comment |
| 2025-W24 | Institutional Books 1.0 | 29 | Review Pending — Full Text Blocked | Books Frozen — Material Gap |
| 2025-W24 | Eliciting Fine-Tuned Transformer Capabilities via ICL | 14 | Low-score Source/Date/Rejection Verified | Disputed / Reject — Existence Argument Exceeds Evidence |
| 2025-W24 | NVIDIA Biomedical AI-Q Research Agent Blueprint | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Product Workflow Example |
| 2025-W24 | Mistral Compute | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Mechanism Not Disclosed |
| 2025-W24 | PyTorch June newsletter | 15 | Low-score Source/Date/Rejection Verified | Ignore — Newsletter Aggregate |
| 2025-W24 | Anthropic FedRAMP announcement | 18 | Low-score Source/Date/Rejection Verified | Cross-week Duplicate / Spillback W21 |
| 2025-W24 | Featherless AI HF Inference Provider | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Version/Product Fact |
| 2025-W24 | Sensitivity-Aware Mixed-Precision Quantizer v1 | 19 | Low-score Source/Date/Rejection Verified | Weekly Only / Emerging — Below Threshold |
| 2025-W24 | Distillation in Practice / Gemma 3 ablations | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Community Case |
| 2025-W24 | PAL / Audio Encoder-to-LLM Information Transfer | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | PersonaLens | 25 | Full Source Review Complete — Benchmark Evidence | Books Frozen — Historical Gate Closed |
| 2025-W24 | Query-Level Uncertainty / Internal Confidence | 29 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Feedback Friction | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Farseer / Refined Scaling Law | 29 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Chain-of-Action | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | ViCrit | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Multimodal Dialogue Response Retrieval Integration | 21 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Generalization or Hallucination? / Out-of-Context Reasoning | 28 | Full Source Review Complete — Theory + Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Dense Retrievers / Granularity Dilemma | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Auto-Regressive vs Flow-Matching for Text-to-Music | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Self-Refining ASR via TTS-Synthesized Data | 25 | Full Source Review Complete — Domain Case | Books Frozen — Historical Gate Closed |
| 2025-W24 | LoRA-Edit | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | FT-UKE / Unstructured Knowledge Editing Locality | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | Only-Style | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | MMMG / Knowledge-Image Generation | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | CC-RAG v1 / later SARG | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | POET / Orthogonal Equivalence Transformation | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | TACTIC | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | VGR / Visual Grounded Reasoning | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W24 | HPSS LLM survey | 15 | Low-score Source/Date/Rejection Verified | Rejected — Domain Perspective |
| 2025-W24 | DeepSpeed v0.17.1 patch release | 23 | Full Source Review Complete — Version Fact | Weekly Only — Version/Product Fact |
| 2025-W24 | Amazon Bedrock Custom Model Import adds Qwen support | 24 | Full Source Review Complete — Versioned Import/Serving Contract | Weekly Only — Version/Product Fact / No Change |
| 2025-W24 | Adobe Unified Support with Amazon Bedrock Knowledge Bases | 26 | Full Source Review Complete — Bounded Production Case | No Change — Already Covered / Weekly Only |
| 2025-W24 | Gardenia ESG disclosure workflow on Amazon Bedrock | 26 | Full Source Review Complete — Bounded Production Case | No Change — Already Covered / Weekly Only |
| 2025-W24 | E.ON smart-meter video diagnostics with Amazon Textract | 27 | Full Source Review Complete — Field-testing Evidence | Emerging / Experimental — Books Frozen |
| 2025-W24 | Accessible audio-description pipeline with Amazon Nova | 22 | Full Source Review Complete — Early Experimental Case | Weekly Only — Experimental / No Change |
| 2025-W24 | NVIDIA Nemotron Super/Nano availability in AWS catalogs | 20 | Full Source Review Complete — Version/Product Fact | Weekly Only — Version/Product Fact |
| 2025-W24 | Amazon Bedrock public-sector cost model | 24 | Full Source Review Complete — Official Billing Taxonomy | No Change — Already Covered / Weekly Only |
| 2025-W24 | mlx-lm 0.25.2 | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Package Revision / Change Set Not Disclosed |
| 2025-W24 | KServe LLMInferenceService CRD and managed HTTPRoute design | 24 | Full Source Review Complete — Emerging Design Task | Books Frozen — Historical Gate Closed |
| 2025-W24 | Effective Red-Teaming of Policy-Adherent Agents / CRAFT + τ-break | 28 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | The Diffusion Duality / Duo | 29 | Full Source Review Complete — Experimental | Integrate — New Mechanism / Books Frozen |
| 2025-W24 | LiveCodeBench Pro | 28 | Full Source Review Complete — Benchmark Evidence | Refine — Existing Argument / Books Frozen |
| 2025-W24 | Beyond Homogeneous Attention / FourierAttention | 28 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | SwS / Weakness-driven Synthesis | 26 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | DeepVideo-R1 / Reg-GRPO | 25 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | pLSTM / DAG Linear RNN | 26 | Full Source Review Complete — Experimental | Integrate — New Mechanism / Books Frozen |
| 2025-W24 | Don't Pay Attention / Avey | 26 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | InterSyn + SynJudge | 26 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | SkillBlender / SkillBench | 26 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | Infinity Instruct | 27 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | Reward Models Enable Scalable Code Verification | 29 | Full Source Review Complete — Experimental | Integrate — New Mechanism / Books Frozen |
| 2025-W24 | Learning a Continue-Thinking Token | 26 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | U-CoT+ / Decoupled Harmful Meme Understanding | 25 | Full Source Review Complete — Experimental Domain Evidence | Refine — Existing Argument / Books Frozen |
| 2025-W24 | Inherently Faithful Attention Maps / IFAM | 25 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W24 | Med-PRM | 29 | Full Source Review Complete — Domain-bounded Evidence | Integrate — New Mechanism / Books Frozen |
| 2025-W24 | Aligned Novel View Image and Geometry Synthesis / MoAI | 23 | Full Source Review Complete — Experimental / Incomplete Result Preserved | Refine — Existing Argument / Books Frozen |
| 2025-W24 | JAFAR | 25 | Full Source Review Complete — Experimental | Refine — Existing Argument / Books Frozen |
| 2025-W25 | MiniMax-M1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W25 | Gemini 2.5 Pro/Flash GA | 20 | Full Source Review Complete — Version Fact | Weekly Only — Version/Product Fact |
| 2025-W25 | Essential-Web v1.0 | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W25 | Ego-R1 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W25 | AceReason-Nemotron 1.1 | 24 | Full Source Review Complete — Experimental / Numerical Subclaim Disputed | Books Frozen — Historical Gate Closed |
| 2025-W25 | RLVR Implicitly Incentivizes Correct Reasoning | 26 | Full Source Review Complete — Experimental / Judge-calibration Boundary | Books Frozen — Historical Gate Closed |
| 2025-W25 | LongLLaDA | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W25 | Xolver | 21 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Reasoning with Exploration | 25 | Full Source Review Complete — Experimental / Entropy-actuator Boundary | Books Frozen — Historical Gate Closed |
| 2025-W25 | Stream-Omni | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | From Bytes to Ideas | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Ring-lite | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | AgentSynth | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | xbench | 25 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | MultiFinBen | 20 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | Efficient Medical VIE via RL | 20 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Align Your Flow | 20 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Guaranteed Guess | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Optimizing Length Compression | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Taming Polysemanticity | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Sekai | 21 | Full Source Review Complete — Dataset / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | All is Not Lost / CheckFree | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W25 | ProtoReasoning | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Embodied Web Agents | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | SwarmAgentic | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Semantically-Aware Rewards | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | SciVer | 26 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | Truncated PPO | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | MoTE | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Evolutionary Caching / ECAD | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | OS-Harm | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W25 | GenRecal | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | ImmerseGen | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | GMT | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | PictSure | 18 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | Guru / Cross-domain RL | 26 | Full Source Review Complete — Experimental / Numerical Subclaim Disputed | Books Frozen — Historical Gate Closed |
| 2025-W25 | Show-o2 | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | SonicVerse | 17 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | RE-IMAGINE | 21 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | Ray 2.47.1 | 16 | Low-score closure — Patch Fact | Weekly Only — Low-score Closure |
| 2025-W25 | LazyEviction | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | EvoLM | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | SparseLoRA | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | SCALE Optimizer | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | GRPO-CARE | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | LMR-BENCH | 25 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | TabArena | 25 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | LLM Safety under Latent Perturbations | 23 | Full Source Review Complete — Security / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | Mathematical Proof Litmus Test | 22 | Full Source Review Complete — Evaluation | Books Frozen — Historical Gate Closed |
| 2025-W25 | Tower+ | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W25 | DualTHOR | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | Hunyuan3D 2.5 | 19 | Low-score closure — Vendor Case | Weekly Only — Low-score Closure |
| 2025-W25 | Vision-guided Chunking | 18 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | Multi-hop RAG Generation | 17 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | OmniReflect | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | MEXA | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W25 | SGLang GB200 PD + Large-scale EP | 27 | Full Source Review Complete — Engineering Case | Books Frozen — Historical Gate Closed |
| 2025-W25 | TensorRT-LLM v0.20.0 | 26 | Full Source Review Complete — Version + Public Mechanism | Books Frozen — Historical Gate Closed |
| 2025-W26 | Gemini Robotics On-Device | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | AlphaGenome | 22 | Full Source Review Complete | Weekly Only — Domain Evidence |
| 2025-W26 | Gemma 3n full release | 26 | Full Source Review Complete | Weekly Only — Version/Product Fact |
| 2025-W26 | Qwen VLo preview | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Mechanism Not Disclosed |
| 2025-W26 | Hunyuan-A13B | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Project Vend 1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Vision as a Dialect | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | ReasonFlux-PRM | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | CommVQ | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | LongWriter-Zero | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Adaptive Activation Steering / STU-PID | 20 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | Understanding Software Engineering Agents | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Context-Aware CodeLLM Eviction | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Chain-of-Experts | 27 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | SlimMoE | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | AggTruth | 24 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | HOLA | 26 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | PARALLELPROMPT | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Radial Attention | 25 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | HiMA-Ecom / JoyAgents-R1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | KnowRL | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Why Do Open-Source LLMs Struggle with Data Analysis? | 22 | Full Source Review Complete | Weekly Only — Evaluation Evidence |
| 2025-W26 | SAGE query rewriting | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | SRFT | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | PLoP precise LoRA placement | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Leaner Training, Lower Leakage | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Decrypto Benchmark | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Evaluation Case |
| 2025-W26 | π-CoT / Prolog-Initialized CoT | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | CoMind / MLE-Live | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | When Life Gives You Samples | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | AIMeter | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | BehaviorBench / Model Editing as a Double-Edged Sword | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Evaluation Case |
| 2025-W26 | DiffuCoder | 27 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | Perry cyber deception framework | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Domain-specific Security Case |
| 2025-W26 | Grokking in LLM Pretraining? | 21 | Full Source Review Complete | Weekly Only — Interpretability Evidence |
| 2025-W26 | Potemkin Understanding | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Mind2Web 2 | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Bridging Offline and Online RL for LLMs | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Efficient and Reusable Cloud Configuration Search | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Automated LLM Speedrunning Benchmark | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | HyperCLOVA X THINK | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | QuickSilver dynamic token halting | 24 | Full Source Review Complete | Emerging / Experimental |
| 2025-W26 | OptScale | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W26 | Sub-MoE | 26 | Full Source Review Complete | Emerging / Experimental |
| 2025-W27 | SPIRAL | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Calligrapher | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W27 | VMoBA | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Thinking with Images for Multimodal Reasoning | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | JAM-Flow | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | μ²Tokenizer | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | GLM-4.1V-9B-Thinking | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Does Math Reasoning Improve General LLM Capabilities? | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | SciArena | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | ARIG | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Thinking Beyond Tokens | 16 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W27 | Mixture of Reasonings | 20 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | FreNBRDF | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W27 | ZeCO | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Kwai Keye-VL Technical Report | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | LongAnimation | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | VLA Models: An Action Tokenization Perspective | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Locality-aware Parallel Decoding | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | MARVIS | 20 | Unverified / Blocked — Precise Material Request | Books Frozen — Historical Gate Closed |
| 2025-W27 | Depth Anything at Any Condition | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | FreeMorph | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Low-score Archive |
| 2025-W27 | IntFold | 21 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Skywork-Reward-V2 | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Energy-Based Transformers | 29 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | AsyncFlow | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | WebSailor | 30 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Decoupled Planning and Execution | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Fast and Simplex | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Can LLMs Identify Critical Limitations? | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Self-Correction Bench | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Answer Matching Outperforms Multiple Choice | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | LangScene-X | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Heeding the Inner Voice | 24 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Bourbaki | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | vLLM CompilationConfig / CLI -O RFC #20283 | 25 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | vLLM Q3 2025 Roadmap #20336 | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | SGLang Q3 2025 Development Roadmap #7736 | 23 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | RAT / Recurrent Attention Transformer | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | GradOT | 26 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | Controllable diffusion LM / S³ | 22 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W27 | DP-Fusion | 27 | Strict Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | Grok 4 official | 22 | Full Source Review Complete — Mechanism Not Disclosed | Weekly Only — Version/Product Fact |
| 2025-W28 | SmolLM3 | 30 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | Kimi K2 release | 27 | Full Source Review Complete — Release Fact | Weekly Only — Version/Product Fact |
| 2025-W28 | vLLM v0.9.2 | 29 | Full Source Review Complete — Official Release/Code Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | DeepSpeed v0.17.2 | 21 | Full Source Review Complete — Version Fact | Weekly Only — Version/Product Fact |
| 2025-W28 | Transformers v4.53.2 | 19 | Low-score closure — Version Fact | Weekly Only — Low-score Closure |
| 2025-W28 | NVIDIA Helix Parallelism | 30 | Full Source Review Complete — Simulated Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | RedOne / SNS domain post-training | 20 | Full Source Review Complete — Experimental Spillback | Books Frozen — Historical Gate Closed |
| 2025-W28 | PRIME dual-memory (2507.04607) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Knowledge-Aware Self-Correction (2507.04625) | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W28 | Cross-Distillation (2507.04636) | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | XiYan-SQL (2507.04701) | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | LOOM-Scope (2507.04723) | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | CoSteer (2507.04756) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Reason-to-Rote (2507.04782) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | ArtifactsBench (2507.04952) | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | Information Utility in KV Memory (2507.05158) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | OpenS2S (2507.05177) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | POLAR policy discriminators (2507.05197) | 26 | Unverified / Blocked — P1 Event-time v1 Full Text | Unverified / Blocked — Historical Gate Closed |
| 2025-W28 | Response Attack (2507.05248) | 28 | Unverified / Blocked — P1 Event-time v1 Full Text | Unverified / Blocked — Historical Gate Closed |
| 2025-W28 | MemoryAgentBench (2507.05257) | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | TokenShapley (2507.05261) | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W28 | LCDS (2507.05319) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Cascade private inference (2507.05228) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Spatio-Temporal LLM (2507.05258) | 25 | Full Source Review Complete — Experimental / v1 Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | Red Teaming AI Red Teaming (2507.05538) | 26 | Full Source Review Complete — Position Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | Prompt-injection detector limits (2507.05630) | 27 | Full Source Review Complete — Experimental Failure Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | SpaceVerse (2507.05731) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Function Calling vs MCP security (2507.06323) | 26 | Full Source Review Complete — Architecture-label Confounding Disputed | Books Frozen — Historical Gate Closed |
| 2025-W28 | Agent KB (2507.06229) | 29 | Unverified / Blocked — P3 Event-time v1 Revision | Unverified / Blocked — Historical Gate Closed |
| 2025-W28 | Next-token predictors and inefficient reasoning (2507.05362) | 23 | Full Source Review Complete — Experimental Trace Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | AutoTriton (2507.05687) | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | MobileGUI-RL (2507.05720) | 27 | Full Source Review Complete — Experimental / Configuration Disputed | Books Frozen — Historical Gate Closed |
| 2025-W28 | SARA (2507.05633) | 27 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W28 | ECom-Bench (2507.05639) | 26 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W28 | DRAGOn (2507.05713) | 25 | Full Source Review Complete — Mechanism Verified / v1 Evaluation Superseded and Disputed | Books Frozen — Historical Gate Closed |
| 2025-W28 | HIRAG (2507.05714) | 24 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W28 | Omni-Router (2507.05724) | 27 | Full Source Review Complete — Experimental / Event-time Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W28 | OpenFActScore (2507.05965) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | RabakBench (2507.05980) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Conditional Multi-Stage Failure Recovery (2507.06016) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Data Compressibility Quantifies Memorization (2507.06056) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | NeoBabel (2507.06137) | 24 | Full Source Review Complete — Experimental / Open Artifact | Books Frozen — Historical Gate Closed |
| 2025-W28 | Skywork-R1V3 (2507.06167) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | CriticLean (2507.06181) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Survey on Latent Reasoning (2507.06203) | 19 | Low-score closure — Secondary Evidence | Weekly Only — Low-score Closure |
| 2025-W28 | Reranking FLOPs (2507.06223) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | PERK test-time learning (2507.06415) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Reward Model Correct Itself (2507.06419) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | PAPO (2507.06448) | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Hybrid Linear Attention analysis (2507.06457) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Verbal Confidence robustness (2507.06489) | 25 | Full Source Review Complete — Experimental / Failure Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | SpindleKV (2507.06517) | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | SlimCaching (2507.06567) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | LPPO (2507.06573) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Decoder-Hybrid-Decoder (2507.06607) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Uncertainty layer-wise dynamics (2507.06722) | 22 | Full Source Review Complete — Preliminary Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | Checklist Engineering LLM Judges (2507.06774) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Adaptive Termination (2507.06829) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Set Selection for RAG (2507.06838) | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Open-source AI evaluation repository (2507.06893) | 25 | Full Source Review Complete — Practice Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | VisualTrap (2507.06899) | 29 | Full Source Review Complete — Security Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | Verification for code generation (2507.06920) | 28 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | FlexOlmo (2507.07024) | 30 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | Frontier LLMs simple reasoning (2507.07313) | 26 | Full Source Review Complete — Failure Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | CCQ low-bit quantization (2507.07145) | 29 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | SAND (2507.07441) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | RLEP (2507.07451) | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Machine Bullshit (2507.07484) | 30 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | PLAN-TUNING (2507.07495) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Teaching LLM to Reason (2507.07498) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Selective-DPO (2507.07725) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Krul (2507.08045) | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | Compactor (2507.08143) | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W28 | TruthTorchLM (2507.08203) | 28 | Full Source Review Complete — Tooling Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | Simple Mechanistic OOC Reasoning (2507.08218) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | KAT-V1 (2507.08297) | 25 | Full Source Review Complete — Experimental / Revision-bounded | Books Frozen — Historical Gate Closed |
| 2025-W28 | ChainEdit (2507.08427) | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | clembench dialogue-game evaluation (2507.08491) | 26 | Full Source Review Complete — Practice Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | LLaPa procedural planning (2507.08496) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | KELPS verified autoformalization (2507.08665) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | KV Cache Steering (2507.08799) | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Self-Improving Model Steering (2507.08967) | 22 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | OpenCodeReasoning-II (2507.09075) | 22 | Full Source Review Complete — Dataset Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | CompassJudger-2 (2507.09104) | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Detrimental neuron pruning (2507.09185) | 24 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W28 | Continual pretraining Dense/MoE Tibetan (2507.09205) | 25 | Full Source Review Complete — Experimental / Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W28 | DATE-LM (2507.09424) | 24 | Full Source Review Complete — Evaluation Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | Ref-Long (2507.09506) | 26 | Full Source Review Complete — Benchmark Evidence | Books Frozen — Historical Gate Closed |
| 2025-W28 | GoalfyMax (2507.09497) | 16 | Low-score closure — Disputed identity/approval | Weekly Only — Low-score Closure |
| 2025-W28 | Teach Old SAEs New Domain Tricks with Boosting | 23 | Unverified / Blocked — P3 Event-time OpenReview Revision | Unverified / Blocked — Historical Gate Closed |
| 2025-W29 | (Almost) Free Modality Stitching of Foundation Models | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | Mixture-of-Recursions | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W29 | Reasoning or Memorization? | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W29 | REST stress testing reasoning models | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W29 | EmbRACE-3K | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | Diffusion LM emergent safety vulnerability | 27 | Full Source Review Complete — Experimental Security Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | EXAONE 4.0 | 24 | Full Source Review Complete — Vendor Technical Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | Seq vs Seq / Ettin | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W29 | ElasticMM | 28 | Full Source Review Complete — Experimental / Correctness Claim Disputed | Books Frozen — Historical Gate Closed |
| 2025-W29 | CodeJudgeBench | 27 | Full Source Review Complete — Experimental Evaluation Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | Multiple Choice Learning of Low-Rank Adapters / LoRA-MCL | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | How Many Instructions Can LLMs Follow at Once? / IFScale | 26 | Full Source Review Complete — Experimental Evaluation Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | Deep Hidden Cognition | 26 | Full Source Review Complete — Experimental / Calibration Boundary | Books Frozen — Historical Gate Closed |
| 2025-W29 | SENTINEL | 25 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | PhyWorldBench | 25 | Full Source Review Complete — Experimental Evaluation Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | ECP high-resolution MLLM framework | 23 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | Astrogator formal verification for LLM-generated code | 25 | Full Source Review Complete — Experimental / Language-specific | Books Frozen — Historical Gate Closed |
| 2025-W29 | Einstein Fields | 19 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W29 | RiemannLoRA | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | GitChameleon 2.0 | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W29 | SWE-Perf | 28 | Full Source Review Complete — Method Field Disputed | Books Frozen — Historical Gate Closed |
| 2025-W29 | MMHU | 24 | Full Source Review Complete — Experimental Domain Benchmark | Books Frozen — Historical Gate Closed |
| 2025-W29 | PhysX-3D | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | MindJourney | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | Mono-InternVL-1.5 | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | FLEXITOKENS | 26 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | AnyCap Project | 22 | Full Source Review Complete — Experimental / Fields Disputed | Books Frozen — Historical Gate Closed |
| 2025-W29 | FantasyPortrait | 18 | Low-score closure | Weekly Only — Low-score Closure |
| 2025-W29 | Inverse RL Meets LLM Post-Training survey | 21 | Full Source Review Complete — Survey Taxonomy / Fields Disputed | Books Frozen — Historical Gate Closed |
| 2025-W29 | Automating Steering for Safe MLLMs | 27 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | Voxtral | 23 | Full Source Review Complete — Version/Technical Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | AbGen | 26 | Full Source Review Complete — Experimental Evaluation Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | Generative Energy Arena | 23 | Full Source Review Complete — Preliminary Human-preference Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | Turing Machine Imitator | 26 | Full Source Review Complete — Experimental / Fields Disputed / Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W29 | Context Engineering survey | 27 | Full Source Review Complete — Narrative Survey / Search Protocol Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W29 | Diffuman4D | 21 | Full Source Review Complete — Experimental 4D Generation Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | π³ visual geometry learning | 25 | Full Source Review Complete — Experimental / Event-time Artifact Partially Available | Books Frozen — Historical Gate Closed |
| 2025-W29 | VisionThink | 27 | Full Source Review Complete — Experimental / Event-time Artifact Revision Boundary | Books Frozen — Historical Gate Closed |
| 2025-W29 | Russian speech data-centric framework / Balalaika v1 | 20 | Full Source Review Complete — Experimental | Books Frozen — Historical Gate Closed |
| 2025-W29 | CSD-VAR | 21 | Full Source Review Complete — Experimental / Event-time Artifact Not Available | Books Frozen — Historical Gate Closed |
| 2025-W29 | OpenBEATs | 24 | Full Source Review Complete — Experimental / Event-time Training Artifact Boundary | Books Frozen — Historical Gate Closed |
| 2025-W29 | Franca | 25 | Full Source Review Complete — Experimental / Event-time Artifact Revision Boundary | Books Frozen — Historical Gate Closed |
| 2025-W29 | SGLang Multiple Token Prediction integration | 25 | Full Source Review Complete — Version Evidence | Books Frozen — Historical Gate Closed |
| 2025-W29 | Introducing ChatGPT agent | 22 | Full Source Review Complete — Mechanism Partially Disclosed | Weekly Only — Version/Product Fact |
| 2025-W29 | Logic-layer Prompt Control Injection | 19 | Low-score closure — Conceptual Security Taxonomy | Weekly Only — Low-score Closure |
| 2025-W29 | Prompt Injection 2.0 | 18 | Low-score closure — Narrative Threat Synthesis | Weekly Only — Low-score Closure |
| 2025-W29 | VLA Models in Robotic Manipulation survey | 19 | Low-score closure — Survey / No New Mechanism | Weekly Only — Low-score Closure |
| 2025-W29 | DeepResearchEco | 19 | Low-score closure — Domain Workflow Evidence | Weekly Only — Low-score Closure |
| 2025-W29 | Enterprise structured-data RAG | 17 | Low-score closure — Artifact/Evaluation Contract Insufficient | Weekly Only — Low-score Closure |
| 2025-W29 | Visual Input for Robotic Path Planning | 18 | Low-score closure — Simplified Benchmark | Weekly Only — Low-score Closure |
| 2025-W29 | Probing for Arithmetic Errors | 19 | Low-score closure — Narrow Arithmetic Mechanism | Weekly Only — Low-score Closure |
| 2025-W29 | Thought Purity | 19 | Low-score closure — Event-time Security Evidence Narrow | Weekly Only — Low-score Closure |
| 2025-W29 | Cross-task Activation Steering / CAST | 19 | Low-score closure — Experimental Transfer Case | Weekly Only — Low-score Closure |
| 2025-W30 | Qwen3-Coder | 24 | Weekly Only — Mechanism Partially Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W30 | GUI-G² | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | GR-3 | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Being-H0 | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | STITCH | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Dual-Token Constraints / Archer | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Latent Denoising Tokenizer | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | TokensGen | 24 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | LLM Economist | 21 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | PhysGym | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | SPAR | 22 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Does More Inference-Time Compute Really Help Robustness? | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | LAPO | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Hierarchical Budget Policy Optimization | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | True Multimodal In-Context Learning | 24 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Beyond Context Limits / TIMRUN | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Step-Audio 2 | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | MegaScience | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | ThinkAct | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Semi-off-Policy RL / SOPHIA | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Experience is the Best Teacher | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Yume | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Turing Eye Test | 26 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Multi-Domain Reasoning via RL | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | RAVine | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Re:Form | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | PUSA V1.0 | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Finding Dori | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Group Sequence Policy Optimization | 28 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | GLiNER2 | 23 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | TTS-VAR | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | DriftMoE | 23 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | TeleChat2 / 2.5 / T1 Technical Report | 24 | Weekly Only — Model/Training Report | Books Frozen — Historical Gate Closed |
| 2025-W30 | TeEFusion | 24 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | SpecForge | 24 | Refine — Existing Argument after Books Gate | Books Frozen — Historical Gate Closed |
| 2025-W30 | Efficient Agents | 26 | Emerging / Experimental — Internal Manuscript Date Conflict Not Used for Owner | Books Frozen — Historical Gate Closed |
| 2025-W30 | InstructVLA | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Dens3R | 25 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | Efficient and Scalable Agentic AI with Heterogeneous Systems | 27 | Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W30 | SeC | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | Spelke Segments | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | SegDT | 18 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | HOComp | 18 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | Task-specific Zero-shot QAT | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | CAFT | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | DesignLab | 19 | Archive Only — Domain-specific benchmark | Weekly Only — Low-score Closure |
| 2025-W30 | Ultra3D | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | Captain Cinema | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | EarthCrafter | 19 | Archive Only — Narrow evidence | Weekly Only — Low-score Closure |
| 2025-W30 | Agentar-Fin-R1 | 19 | Archive Only — Domain-specific model | Weekly Only — Low-score Closure |
| 2025-W30 | A New Pair of GloVes | 18 | Archive Only — Local model mechanism | Weekly Only — Low-score Closure |
| 2025-W30 | HLFormer | 18 | Archive Only — Narrow architecture | Weekly Only — Low-score Closure |
| 2025-W30 | Ray Q3 2025 Roadmap | 16 | Weekly Only — Design Intent, Not Release | Weekly Only — Low-score Closure |
| 2025-W30 | Zebra-CoT | 19 | Unverified / Blocked — Full Text | Unverified / Blocked — Historical Gate Closed |
| 2025-W31 | GLM-4.5 | 25 | Must Read；与 Qwen3/DeepSeek V3.1 比较 hybrid contract | Books Frozen — Historical Gate Closed |
| 2025-W31 | Kimi K2 technical report | 27 | Must Read；Books 只形成一个 K2 source packet | Books Frozen — Historical Gate Closed |
| 2025-W31 | Optimal Scheduling Algorithms for LLM Inference / SLAI | 27 | Full Source Review Complete — Emerging / Experimental / Artifact Not Disclosed | Books Frozen — Historical Gate Closed |
| 2025-W31 | Graph-R1 | 26 | Full Source Review Complete — Emerging / Experimental / Theory Claim Disputed | Disputed — Historical Gate Closed |
| 2025-W31 | DICE | 24 | Full Source Review Complete — Emerging / Experimental / Formal Claims Disputed | Disputed — Historical Gate Closed |
| 2025-W31 | Graph-Augmented Large Language Model Agents survey | 21 | Full Source Review Complete — Secondary Taxonomy / No Change Already Covered | Books Frozen — Historical Gate Closed |
| 2025-W31 | Geometric-Mean Policy Optimization (GMPO) | 26 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Reinforcement Learning from Self-Feedback (RLSF) | 25 | Full Source Review Complete — Emerging / Calibration Boundary | Books Frozen — Historical Gate Closed |
| 2025-W31 | AutoTIR | 25 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Multi-Agent-as-Judge / MAJ-Eval | 23 | Full Source Review Complete — Emerging / Human-Alignment Boundary | Books Frozen — Historical Gate Closed |
| 2025-W31 | MemTool | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W31 | Persona Vectors | 27 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Accelerating Prefilling via Decoding-time Contribution Sparsity / TriangleMix | 27 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Falcon-H1 technical report | 29 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W31 | GEAK Triton Kernel Agent and Benchmarks | 29 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W31 | TTS-1 Technical Report | 25 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Compressed History States for Web Agent Automation | 25 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Self-Evolving Agents survey | 23 | Full Source Review Complete — Secondary Taxonomy | Books Frozen — Historical Gate Closed |
| 2025-W31 | G-Core RLHF Trainer | 26 | Full Source Review Complete — Disputed / Withdrawn Source | Disputed — Historical Gate Closed |
| 2025-W31 | Watch the Weights | 26 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | CoT Mirage / DataAlchemy | 24 | Full Source Review Complete — Emerging / Controlled Synthetic Evidence | Books Frozen — Historical Gate Closed |
| 2025-W31 | Beyond Fixed / DAEDAL | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | SitEmb-v1.5 | 25 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W31 | LiveMCPBench | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W31 | Representation Shift | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | A Glimpse to Compress / GlimpsePrune | 23 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | SWE-Exp | 26 | Full Source Review Complete — Refine Candidate | Books Frozen — Historical Gate Closed |
| 2025-W31 | SWE-Debate | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Cyber-Zero | 26 | Full Source Review Complete — Emerging / Security Boundary | Books Frozen — Historical Gate Closed |
| 2025-W31 | FACTORY | 26 | Full Source Review Complete — Refine Evaluation Contract | Books Frozen — Historical Gate Closed |
| 2025-W31 | RoboMemory | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | Web-CogReasoner | 24 | Full Source Review Complete — Emerging / Experimental | Books Frozen — Historical Gate Closed |
| 2025-W31 | FRED hallucination detection and editing | 19 | Reject — narrow activation-editing study; no system contract | Weekly Only — Low-score Closure |
| 2025-W31 | Conformative Decoding | 18 | Reject — method signal retained; project relevance too narrow | Weekly Only — Low-score Closure |
| 2025-W31 | Text Embeddings survey | 17 | Reject — secondary overview; already covered | Weekly Only — Low-score Closure |
| 2025-W31 | Multilingual Self-Taught Faithfulness Evaluators | 19 | Reject — limited language/task transfer evidence | Weekly Only — Low-score Closure |
| 2025-W31 | NeedleChain | 18 | Reject — benchmark-only owner, limited system mechanism | Weekly Only — Low-score Closure |
| 2025-W31 | IFEvalCode | 19 | Reject — evaluation asset, not a new system mechanism | Weekly Only — Low-score Closure |
| 2025-W31 | Discrete Tokenization for Multimodal LLMs survey | 19 | Reject — secondary taxonomy; Part III already owns mechanism | Weekly Only — Low-score Closure |
| 2025-W31 | PRGB Benchmark | 18 | Reject — placeholder benchmark does not change RAG contract | Weekly Only — Low-score Closure |
| 2025-W31 | CoT Mechanistic Interpretability with Sparse Autoencoding | 19 | Reject — exploratory interpretability evidence | Weekly Only — Low-score Closure |
| 2025-W31 | LENS multi-LLM confidence integration | 19 | Reject — ensemble confidence lacks deployment calibration | Weekly Only — Low-score Closure |
| 2025-W31 | Super Experts in MoE LLMs | 19 | Reject — analysis does not establish routing redesign | Weekly Only — Low-score Closure |
| 2025-W31 | User Feedback as a Noisy Learning Signal | 18 | Reject — observational evidence; no robust update mechanism | Weekly Only — Low-score Closure |
| 2025-W31 | RL-PLUS | 19 | Reject — hybrid-policy claim not yet system-general | Weekly Only — Low-score Closure |
| 2025-W31 | MetaAgent | 19 | Reject — tool meta-learning evidence too narrow | Weekly Only — Low-score Closure |
| 2025-W31 | Pro2Guard | 19 | Reject — probabilistic-checking prototype lacks production contract | Weekly Only — Low-score Closure |
| 2025-W31 | Cognitive Kernel-Pro | 19 | Reject — deep-research framework evidence not yet durable | Weekly Only — Low-score Closure |
| 2025-W32 | gpt-oss | 27 | Must Read；联合模型卡与 safety paper 全文复核 | Books Frozen — Historical Gate Closed |
| 2025-W32 | GPT-5 | 24 | Worth Watching；只作为 inference policy 信号 | Weekly Only — Version/Product Fact |
| 2025-W32 | GLM-4.5 technical report | 25 | Must Read；不重复计算为第二个 Books 事件 | Books Frozen — Historical Gate Closed |
| 2025-W32 | Qwen-Image technical report | 27 | Must Read；多模态表示与生成 owner | Books Frozen — Historical Gate Closed |
| 2025-W32 | Seed Diffusion | 27 | Must Read；parallel decoding 受限案例 | Books Frozen — Historical Gate Closed |
| 2025-W32 | Agent Lightning | 29 | Must Read；trajectory schema 与 training-agent disaggregation | Books Frozen — Historical Gate Closed |
| 2025-W32 | SWE Agent RL | 27 | Must Read；stateful environment RL contract | Books Frozen — Historical Gate Closed |
| 2025-W32 | VeriGUI | 25 | Must Read；subtask-level executable verification | Books Frozen — Historical Gate Closed |
| 2025-W32 | SEAgent | 27 | Must Read；derived guidebook、world-state reward 与 curriculum | Books Frozen — Historical Gate Closed |
| 2025-W32 | CompassVerifier | 27 | Must Read；verifier 是 versioned evaluation/reward component | Books Frozen — Historical Gate Closed |
| 2025-W32 | R-Zero | 27 | Must Read；challenger-solver curriculum branch | Books Frozen — Historical Gate Closed |
| 2025-W32 | Dynamic Fine-Tuning | 26 | Must Read；token-gradient weighting 的受限替代分支 | Books Frozen — Historical Gate Closed |
| 2025-W32 | VeOmni | 27 | Must Read；model-centric distributed recipe | Books Frozen — Historical Gate Closed |
| 2025-W32 | ToolTrain | 25 | Must Read；tool policy 与 repo-search environment coupling | Books Frozen — Historical Gate Closed |
| 2025-W32 | AttnTrace | 23 | Worth Watching；attention attribution 不等于因果证据 | Books Frozen — Historical Gate Closed |
| 2025-W32 | TensorRT-LLM v0.21.0 | 26 | Must Read；typed feature-combination 与 known-issue contract | Weekly Only — Version/Product Fact |
| 2025-W32 | Goedel-Prover-V2 | 19 | Weekly Only；formal proof domain，机制主线已有覆盖 | Weekly Only — Low-score Closure |
| 2025-W32 | TRACEALIGN | 18 | Emerging；理论与经验边界不足以形成 owner | Weekly Only — Low-score Closure |
| 2025-W32 | IFDecorator | 19 | Weekly Only；instruction-following data method，长期独立性不足 | Weekly Only — Low-score Closure |
| 2025-W32 | Skywork UniPic | 19 | Weekly Only；统一图像生成案例，未改变 Ch24 结论 | Weekly Only — Low-score Closure |
| 2025-W32 | Beyond the Trade-off | 18 | Emerging；self-supervised instruction-following RL 仍依赖作者 evaluator | Weekly Only — Low-score Closure |
| 2025-W32 | Trainable Dynamic Mask Sparse Attention | 19 | Emerging；未形成可迁移 runtime contract | Weekly Only — Low-score Closure |
| 2025-W32 | Sparse-dLLM | 18 | Emerging；与 Seed Diffusion 同路线但证据较弱 | Weekly Only — Low-score Closure |
| 2025-W32 | Dynaword | 18 | Weekly Only；动态 tokenization 案例 | Weekly Only — Low-score Closure |
| 2025-W32 | Sculptor | 18 | Weekly Only；active context management 未改变 context owner 主线 | Weekly Only — Low-score Closure |
| 2025-W32 | CoAct-1 | 18 | Weekly Only；computer-use action case | Weekly Only — Low-score Closure |
| 2025-W32 | InfiAlign | 19 | Weekly Only；alignment data pipeline case | Weekly Only — Low-score Closure |
| 2025-W32 | DeepPHY | 19 | Emerging；physics-grounded video case，机制外推受限 | Weekly Only — Low-score Closure |
| 2025-W32 | Genie Envisioner | 19 | Emerging；embodied imagination case，环境闭环未充分验证 | Weekly Only — Low-score Closure |
| 2025-W32 | CellForge | 16 | Domain Only；AI for Science workflow 未改变系统 contract | Weekly Only — Low-score Closure |
| 2025-W32 | HarmonyGuard | 19 | Weekly Only；safety benchmark case | Weekly Only — Low-score Closure |
| 2025-W32 | Learning to Reason for Factuality | 19 | Weekly Only；factuality RL 证据边界不足 | Weekly Only — Low-score Closure |
| 2025-W32 | ChartCap | 16 | Domain Only；chart understanding dataset | Weekly Only — Low-score Closure |
| 2025-W32 | StepFun-Formalizer | 16 | Domain Only；formalization model fact | Weekly Only — Low-score Closure |
| 2025-W32 | MiDashengLM | 17 | Domain Only；audio model release case | Weekly Only — Low-score Closure |
| 2025-W32 | LeanK | 18 | Weekly Only；learnable K-cache channel pruning 的受限 KV 优化分支 | Weekly Only — Low-score Closure |
| 2025-W32 | Double-Bench document RAG evaluation | 19 | Weekly Only；evaluation snapshot，未改变证据框架 | Weekly Only — Low-score Closure |
| 2025-W32 | Sotopia-RL | 18 | Emerging；social-agent reward case | Weekly Only — Low-score Closure |
| 2025-W32 | VLM RL in synthetic worlds | 18 | Emerging；sim-to-real 边界未闭合 | Weekly Only — Low-score Closure |
| 2025-W32 | Agentic e-commerce evaluation | 19 | Weekly Only；domain harness case | Weekly Only — Low-score Closure |
| 2025-W32 | Multi-agent document QA / MACT | 18 | Weekly Only；未给 compute-matched single-agent headroom | Weekly Only — Low-score Closure |
| 2025-W33 | ASearcher / Beyond Ten Turns | 28 | Must Read；long-horizon agentic RL runtime | Books Frozen — Historical Gate Closed |
| 2025-W33 | Tricks or Traps? Part I | 27 | Must Read；RL technique interaction evidence | Books Frozen — Historical Gate Closed |
| 2025-W33 | Multi-head Transformers Learn Symbolic Multi-step Reasoning | 23 | Worth Watching；受限理论证据 | Books Frozen — Historical Gate Closed |
| 2025-W33 | Human-Alignment and Calibration of Inference-Time Uncertainty | 22 | Worth Watching；calibration boundary | Books Frozen — Historical Gate Closed |
| 2025-W33 | Can LLMs Detect Their Confabulations? | 23 | Worth Watching；uncertainty-guided probe | Books Frozen — Historical Gate Closed |
| 2025-W33 | SafeKV | 27 | Must Read；privacy-aware shared KV state | Books Frozen — Historical Gate Closed |
| 2025-W33 | BrowseMaster | 25 | Must Read；planner/executor browser pair | Books Frozen — Historical Gate Closed |
| 2025-W33 | LogicIFGen / LogicIFEval | 23 | Worth Watching；executable instruction contract | Books Frozen — Historical Gate Closed |
| 2025-W33 | OpenCUA | 27 | Must Read；open computer-use data/model stack | Books Frozen — Historical Gate Closed |
| 2025-W33 | SMA membership audit | 24 | Worth Watching；source-aware RAG privacy audit | Books Frozen — Historical Gate Closed |
| 2025-W33 | P/D-Device | 27 | Must Read；cloud/device state ownership | Books Frozen — Historical Gate Closed |
| 2025-W33 | Neural Bandit LLM Selection for Task Pipelines | 23 | Worth Watching；downstream-aware routing | Books Frozen — Historical Gate Closed |
| 2025-W33 | Nested-ReFT | 25 | Must Read；off-policy rollout cost branch | Books Frozen — Historical Gate Closed |
| 2025-W33 | Shadow in the Cache / KV-Cloak | 26 | Must Read；KV inversion threat model | Books Frozen — Historical Gate Closed |
| 2025-W33 | Memory Decoder | 25 | Must Read；learned plug-in memory branch | Books Frozen — Historical Gate Closed |
| 2025-W33 | mSCoRe | 21 | Worth Watching；scalable multilingual evaluation | Books Frozen — Historical Gate Closed |
| 2025-W33 | Masked Diffusion Text Style Transfer / Inference-time Scaling | 22 | Worth Watching；proposal/correction branch | Books Frozen — Historical Gate Closed |
| 2025-W33 | MCP-Guard | 25 | Must Read；layered MCP detection pipeline | Books Frozen — Historical Gate Closed |
| 2025-W33 | SeamlessFlow | 28 | Must Read；trainer-agent isolation and tag scheduling | Books Frozen — Historical Gate Closed |
| 2025-W33 | ADMIRE-BayesOpt | 26 | Must Read；multi-fidelity data-mixture search | Books Frozen — Historical Gate Closed |
| 2025-W33 | SafeSieve | 24 | Worth Watching；feedback-driven communication pruning | Books Frozen — Historical Gate Closed |
| 2025-W33 | CRAFT-GUI | 24 | Worth Watching；curriculum GUI RL | Books Frozen — Historical Gate Closed |
| 2025-W33 | Dynamic Quality-Latency Edge Routing | 22 | Worth Watching；quality-latency control policy | Books Frozen — Historical Gate Closed |
| 2025-W33 | vLLM 1.0 RFC | 23 | Weekly Only；official interface-governance plan | Books Frozen — Historical Gate Closed |
| 2025-W33 | GPT-5 Multimodal Medical Reasoning | 19 | Weekly Only；third-party API snapshot | Weekly Only — Low-score Closure |
| 2025-W33 | VGGSounder | 19 | Weekly Only；benchmark repair case | Weekly Only — Low-score Closure |
| 2025-W33 | MAMEX cold-start recommendation | 18 | Domain Only；MoE mechanism不改变主线 | Weekly Only — Low-score Closure |
| 2025-W33 | PRECISE cyberattack compliance | 17 | Domain Only；critical-infra case | Weekly Only — Low-score Closure |
| 2025-W33 | IBPS legal prediction | 16 | Domain Only；legal RAG/application case | Weekly Only — Low-score Closure |
| 2025-W33 | Urban-STA4CLC | 16 | Domain Only；urban disaster model | Weekly Only — Low-score Closure |
| 2025-W33 | NEXICA traffic causality | 17 | Domain Only；traffic-specific causal model | Weekly Only — Low-score Closure |
| 2025-W33 | SYNAPSE-G | 18 | Domain Only；rare-event graph case | Weekly Only — Low-score Closure |
| 2025-W33 | Hopfield Memorisation and Forgetting | 18 | Weekly Only；theory analogy，不外推 LLM memory | Weekly Only — Low-score Closure |
| 2025-W33 | FROGENT | 19 | Domain Only；drug workflow case | Weekly Only — Low-score Closure |
| 2025-W33 | HumanSense | 18 | Domain Only；empathetic multimodal benchmark | Weekly Only — Low-score Closure |
| 2025-W33 | Activate Me! FHE activations | 19 | Emerging；FHE-specific activation trade-off | Weekly Only — Low-score Closure |
| 2025-W34 | MCPGauge / Help or Hurdle | 24 | Retain — MCP benefit must be measured against tool overhead | Books Frozen — Historical Gate Closed |
| 2025-W34 | ToolACE-MT | 25 | Retain — verifier-owned multi-turn tool data pipeline | Books Frozen — Historical Gate Closed |
| 2025-W34 | Reinforcement Learning with Rubric Anchors | 25 | Retain — open-ended reward contract | Books Frozen — Historical Gate Closed |
| 2025-W34 | HeroBench | 24 | Retain — executable hierarchical-plan evaluation | Books Frozen — Historical Gate Closed |
| 2025-W34 | Atom-Searcher | 25 | Retain — atomic search-state reward assignment | Books Frozen — Historical Gate Closed |
| 2025-W34 | Matrix-Game 2.0 | 26 | Retain — action-conditioned interactive world state | Books Frozen — Historical Gate Closed |
| 2025-W34 | POML | 24 | Retain — prompt as versioned declarative artifact | Books Frozen — Historical Gate Closed |
| 2025-W34 | Embodied-R1 | 25 | Retain — pointing as embodiment-agnostic interface | Books Frozen — Historical Gate Closed |
| 2025-W34 | RynnEC | 23 | Retain — region-owned embodied perception state | Books Frozen — Historical Gate Closed |
| 2025-W34 | DuPO | 25 | Retain — dual tasks produce intrinsic verification feedback | Books Frozen — Historical Gate Closed |
| 2025-W34 | NVIDIA Nemotron Nano 2 | 27 | Retain — hybrid architecture, pruning and budget control co-design | Books Frozen — Historical Gate Closed |
| 2025-W34 | MCP-Universe | 25 | Retain — execution-based real MCP evaluation | Books Frozen — Historical Gate Closed |
| 2025-W34 | Quantization Meets dLLMs | 24 | Retain — PTQ contract changes under iterative denoising | Books Frozen — Historical Gate Closed |
| 2025-W34 | Deep Think with Confidence | 26 | Retain — confidence-aware test-time compute routing | Books Frozen — Historical Gate Closed |
| 2025-W34 | Mobile-Agent-v3 | 26 | Retain — environment-owned GUI trajectory lifecycle | Books Frozen — Historical Gate Closed |
| 2025-W34 | LiveMCP-101 | 24 | Retain — parallel live-reference evaluator | Books Frozen — Historical Gate Closed |
| 2025-W34 | Intern-S1 | 27 | Retain — scientific modality/data/reward co-design | Books Frozen — Historical Gate Closed |
| 2025-W34 | DeepSeek-V3.1 | 25 | Retain — Version Fact / Mechanism Not Disclosed | Weekly Only — Version/Product Fact |
| 2025-W34 | 4DNeX | 25 | Retain — RGB/XYZ joint representation for feed-forward 4D generation | Books Frozen — Historical Gate Closed |
| 2025-W34 | Next Visual Granularity Generation | 24 | Retain — coarse-to-fine visual token state hierarchy | Books Frozen — Historical Gate Closed |
| 2025-W34 | S²-Guidance | 22 | Retain — stochastic self-guidance without a separately trained weak model | Books Frozen — Historical Gate Closed |
| 2025-W34 | Precise Action-to-Video | 25 | Retain — visual action representation across embodiments | Books Frozen — Historical Gate Closed |
| 2025-W34 | FLARE | 27 | Retain — SDPA-native low-rank gather/scatter routing | Books Frozen — Historical Gate Closed |
| 2025-W34 | MeshCoder | 25 | Retain — executable program as editable 3D state | Books Frozen — Historical Gate Closed |
| 2025-W34 | Dissecting Tool-Integrated Reasoning | 25 | Retain — accuracy/cost contract for tool reasoning | Books Frozen — Historical Gate Closed |
| 2025-W34 | TPLA | 28 | Retain — shard latent KV without discarding full-head information | Books Frozen — Historical Gate Closed |
| 2025-W34 | AgentFly / Memento | 27 | Retain — memory read/write as online agent policy adaptation | Books Frozen — Historical Gate Closed |
| 2025-W34 | aiXiv | 18 | Reject — platform case lacks independent quality-control evidence | Weekly Only — Low-score Closure |
| 2025-W34 | LLaSO | 18 | Reject — useful speech artifact, limited current owner fit | Weekly Only — Low-score Closure |
| 2025-W34 | Fin-PRM | 19 | Reject — narrow domain evidence, no general reward conclusion | Weekly Only — Low-score Closure |
| 2025-W36 | UI-TARS-2 Technical Report | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | SimpleTIR | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | VerlTool | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Baichuan-M2 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | OpenVision 2 | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | DynaGuard | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | LMEnt | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Planning with Reasoning using Vision Language World Model | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Beyond Correctness | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Towards a Unified View of LLM Post-Training | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | DeepResearch Arena | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Why Language Models Hallucinate | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Set Block Decoding | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | On Robustness and Reliability of Benchmark-Based Evaluation of LLMs | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Loong | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Emergent Hierarchical Reasoning through RL (HICRA) | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Hunyuan-MT Technical Report | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Manipulation as in Simulation | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Inverse IFEval | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Transition Models | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Delta Activations | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | False Sense of Security: Why Probing-based Malicious Input Detection Fails to Generalize | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Kubernetes DRA GA design details | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W36 | Landscape of Agentic RL for LLMs | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — survey, no new primary mechanism |
| 2025-W36 | Reasoning Vectors | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | POINTS-Reader | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — document conversion specialization |
| 2025-W36 | Gated Associative Memory | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | Kwai Keye-VL 1.5 | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — model report |
| 2025-W36 | Implicit Actor-Critic Coupling for RLVR | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | GenCompositor | 15 | Low-score Source/Date/Rejection Verified | Reject — narrow video composition workload |
| 2025-W36 | Jointly Reinforcing Diversity and Quality | 18 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | Benchmarking Optimizers for LLM Pretraining | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — bounded optimizer comparison |
| 2025-W36 | Flavors of Moonshine | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — edge ASR specialization |
| 2025-W36 | DCPO | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | FlashAdventure | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — GUI evaluation case |
| 2025-W36 | Fantastic Pretraining Optimizers | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | M3Ret | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — domain representation evidence |
| 2025-W36 | ViSTA-SLAM | 17 | Low-score Source/Date/Rejection Verified | Reject — robotics perception specialization |
| 2025-W36 | Robix | 19 | Unverified / Blocked — Exact P1 Request | Weekly Only — Blocked |
| 2025-W36 | LuxDiT | 15 | Low-score Source/Date/Rejection Verified | Reject — lighting estimation specialization |
| 2025-W36 | WildScore | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — domain benchmark |
| 2025-W36 | LatticeWorld | 18 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | WinT3R | 17 | Low-score Source/Date/Rejection Verified | Reject — reconstruction specialization |
| 2025-W36 | Bootstrapping Task Spaces for Self-Improvement | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | U-ARM | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — teleoperation hardware case |
| 2025-W36 | Behavioral Fingerprinting of LLMs | 19 | Low-score Source/Date/Rejection Verified | Emerging — LLM-judge dependence |
| 2025-W36 | MedVista3D | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — medical benchmark/model case |
| 2025-W36 | Symbolic Graphics Programming with LLMs | 18 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | Attributes as Textual Genes | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | Discrete Noise Inversion for Next-scale Autoregressive Image Editing | 17 | Low-score Source/Date/Rejection Verified | Reject — narrow image-editing branch |
| 2025-W36 | AMBEDKAR | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W36 | Panel of Peers | 19 | Low-score Source/Date/Rejection Verified | Emerging — self-generated preference evidence |
| 2025-W36 | MedDINOv3 | 17 | Low-score Source/Date/Rejection Verified | Weekly Only — medical segmentation specialization |
| 2025-W36 | Self-Supervised Cross Reconstruction for Point Clouds | 16 | Low-score Source/Date/Rejection Verified | Reject — point-cloud pretraining specialization |
| 2025-W36 | MOSAIC | 16 | Low-score Source/Date/Rejection Verified | Reject — personalized image-generation specialization |
| 2025-W36 | Drivel-ology | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — bounded diagnostic benchmark |
| 2025-W36 | From Editor to Dense Geometry Estimator | 18 | Low-score Source/Date/Rejection Verified | Emerging — diffusion geometry estimator |
| 2025-W36 | NER Retriever | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — typed retrieval specialization |
| 2025-W36 | Few-step Flow for 3D Generation | 18 | Low-score Source/Date/Rejection Verified | Emerging — bounded 3D distillation branch |
| 2025-W36 | Durian | 16 | Low-score Source/Date/Rejection Verified | Reject — portrait-animation specialization |
| 2025-W36 | Ray 2.49.1 | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — patch fact |
| 2025-W36 | TensorRT-LLM 1.1.0rc3 | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — prerelease fact |
| 2025-W36 | OpenAI sensitive-conversation routing plan | 19 | Low-score Source/Date/Rejection Verified | Version Fact / Mechanism Not Disclosed |
| 2025-W36 | Anthropic regional sales restrictions | 16 | Low-score Source/Date/Rejection Verified | Weekly Only — governance policy fact |
| 2025-W38 | GPT-5-Codex | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Fun-ASR Technical Report | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Phi: Preference Hijacking | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Reasoning-Aware Compression | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | C3T speech-language preservation benchmark | 19 | Low-score Source/Date/Rejection Verified | Reject — Narrow Evaluation Evidence |
| 2025-W38 | RAGs to Riches | 19 | Low-score Source/Date/Rejection Verified | Reject — Role-play Case Study |
| 2025-W38 | MedicalOS | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Workflow Evidence |
| 2025-W38 | Learning to Generate Pointing Gestures | 18 | Low-score Source/Date/Rejection Verified | Reject — Narrow Embodied Case |
| 2025-W38 | Legal-Critical Software / Synedrion | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Graph-Based Confidence Estimation | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | H2R: Hierarchical Hindsight Reflection | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Opportunistic GPU Inference with Pervasive Context Management | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | LLMs Imitate Logical Reasoning, but at what Cost? | 19 | Low-score Source/Date/Rejection Verified | Reject — Diagnostic Study Only |
| 2025-W38 | Multi-Agent LLM Defense Pipeline Against Prompt Injection | 19 | Low-score Source/Date/Rejection Verified | Reject — Defense Composition Case |
| 2025-W38 | Reversible Deep Equilibrium Models | 19 | Low-score Source/Date/Rejection Verified | Reject — Architecture-Specific |
| 2025-W38 | Black-box Model Merging for LMaaS | 19 | Low-score Source/Date/Rejection Verified | Reject — Early Repository Case |
| 2025-W38 | Bi-level Personalization for Federated Foundation Models | 19 | Low-score Source/Date/Rejection Verified | Reject — Narrow Federated Case |
| 2025-W38 | Token-Level Differential Privacy in Memory Sculpting | 19 | Low-score Source/Date/Rejection Verified | Reject — Continual-Learning Case |
| 2025-W38 | Data Scaling Laws for Radiology Foundation Models | 18 | Low-score Source/Date/Rejection Verified | Reject — Domain-Specific Scaling |
| 2025-W38 | HPIM Accelerator | 19 | Low-score Source/Date/Rejection Verified | Reject — Simulator-Only Accelerator Case |
| 2025-W38 | Synthetic Bootstrapped Pretraining | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Process-Supervised RL for Tool-Use Agents | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | FAMAS Failure Attribution | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | InfraMind | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | DSCC-HS | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Prosocial Ability Profiles of Multi-Agent Populations | 18 | Low-score Source/Date/Rejection Verified | Reject — Evaluation Case Only |
| 2025-W38 | CAMPUS Curriculum Instruction Tuning | 19 | Low-score Source/Date/Rejection Verified | Reject — Training Schedule Case |
| 2025-W38 | PromptSE | 18 | Low-score Source/Date/Rejection Verified | Reject — Narrow Robustness Metric |
| 2025-W38 | AgentCTG | 19 | Low-score Source/Date/Rejection Verified | Reject — Multi-Agent Wrapper Case |
| 2025-W38 | Helpfulness-Exploiting Jailbreak | 19 | Low-score Source/Date/Rejection Verified | Reject — Attack Variant |
| 2025-W38 | TENET Ternary Edge Inference | 19 | Low-score Source/Date/Rejection Verified | Reject — Architecture-Specific |
| 2025-W38 | FlowDrive | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Model Case |
| 2025-W38 | VCBench | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Benchmark |
| 2025-W38 | CoopQ | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | FlowRL | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Evil Vizier | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | TDRM | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Pre-training under Infinite Compute | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | ATTS | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | LEAP PIM-NoC Inference | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Participant-Aware Access Control | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | LLM Jailbreak Detection for (Almost) Free | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | DeepRefusal | 19 | Low-score Source/Date/Rejection Verified | Reject — Safety Fine-tuning Case |
| 2025-W38 | Generalizable Geometric Image Caption Synthesis | 18 | Low-score Source/Date/Rejection Verified | Reject — Data Synthesis Case |
| 2025-W38 | Black-box Layers via Low-rank Surrogate Optimization | 19 | Low-score Source/Date/Rejection Verified | Reject — Specialized Optimizer Case |
| 2025-W38 | Ask-to-Clarify: Vision-Language-Action Model with Clarification | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Fast and Fluent Diffusion LMs via Convolutional Decoding | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Robot Control Stack | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Cognitive-Failure Diagnostics for Multi-Agent Expert Systems | 19 | Low-score Source/Date/Rejection Verified | Reject — Narrow Diagnostic Workflow |
| 2025-W38 | Beyond Spurious Signals in Multimodal Learning | 19 | Low-score Source/Date/Rejection Verified | Reject — Task-Specific Debiasing Case |
| 2025-W38 | SmolRGPT | 19 | Low-score Source/Date/Rejection Verified | Reject — Small Domain VLM Case |
| 2025-W38 | Explainable Supervisory Control | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Control Case |
| 2025-W38 | RPG: Repository Planning Graph | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | MANZANO | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | BaseReward | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | VLAC: Vision-Language-Action-Critic | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | M-Spoiler | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | HAPO | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Audio-Conditioned Diffusion Language Models for ASR | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | FESTA | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | NUMINA | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Benchmark |
| 2025-W38 | Decoding Uncertainty | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | SMART: Sycophancy Mitigation via Adaptive RL | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Roundtable Policy | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | End-to-End Combinatorial Optimization Solvers | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Optimization Case |
| 2025-W38 | seqBench | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Audio-Visual Navigation with Stereo Attention | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Navigation Case |
| 2025-W38 | SWE-Bench Pro | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Governing Automated Strategic Intelligence | 18 | Low-score Source/Date/Rejection Verified | Reject — Preliminary Governance Review |
| 2025-W38 | MCTS-EP | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | ARE: A Research Environment for Agentic Systems | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Shall We Play a Game? | 18 | Low-score Source/Date/Rejection Verified | Reject — Revision-Sensitive Scoping Review |
| 2025-W38 | RoE: Routing of Experts for Hyper-Parallel MoE Inference | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Can Agents Judge Systematic Reviews Like Humans? | 18 | Low-score Source/Date/Rejection Verified | Reject — Domain Evaluation Case |
| 2025-W38 | Mind the Gap / AgentSeer | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Prompt-Driven Agentic Video Editing | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | AI-assisted Nursing Skills Assessment | 18 | Low-score Source/Date/Rejection Verified | Reject — Synthesized Domain Workflow |
| 2025-W38 | LLMs as Layout Designers / LaySPA | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Layout Optimization |
| 2025-W38 | Quantum Abduction | 17 | Low-score Source/Date/Rejection Verified | Reject — Conceptual Case Studies |
| 2025-W38 | KAHAN Financial Data Narration | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Narration Workflow |
| 2025-W38 | Domain-Landmark Graph Learning | 19 | Low-score Source/Date/Rejection Verified | Reject — Classical Planning Case |
| 2025-W38 | RALLM-POI | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Retrieval Case |
| 2025-W38 | Intention-aware Hierarchical Diffusion for Trajectory Anomaly Detection | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Anomaly Case |
| 2025-W38 | Native PyTorch Quantized LLM Inference on Intel CPUs | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | Reducing PT2 Compilation Time for Meta Workloads | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | TorchAO Quantized Models and Recipes on Hugging Face | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | DRA Resource Health in Pod Status | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W38 | DRA Consumable Capacity | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Qwen3-Omni Technical Report | 30 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | LIMI: Less is More for Agency | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | EpiCache | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Strategic Dishonesty | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Reinforcement Learning on Pre-Training Data | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | MAPO | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | CompLLM | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Video Models Are Zero-Shot Learners and Reasoners | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | SIM-CoT | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | VCRL | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Thinking Augmented Pre-training | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | UserRL | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | When Judgment Becomes Noise | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | ReflectDrive | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Mixture of Thoughts | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | MMR1 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Tree Search for LLM Agent RL | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | TrustJudge | 30 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | CE-GPPO | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | LongLive | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | MinerU2.5 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Language Models Can Learn from Verbal Feedback Without Scalar Rewards | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | SPEAR | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | UltraHorizon | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | WoW | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | PromptCoT 2.0 | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | StableToken | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Multiplayer Nash Preference Optimization | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Sequential Diffusion Language Models | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Semantic-Space Exploration and Exploitation in RLVR | 20 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | ToolUniverse | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | SparseD | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | HunyuanImage 3.0 Technical Report | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | VideoScore2 | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | MCPMark | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Winning the Pruning Gamble / Q-Tuning | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | d2Cache | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | SINQ | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | The Rogue Scalpel | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | SLA: Sparse-Linear Attention | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Tool-Light | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | Constrained-MDP LLM Distillation | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | ChatInject | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | RLP: Reinforcement as a Pretraining Objective | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W39 | DeepSeek-V3.1-Terminus | 19 | Low-score Source/Date/Rejection Verified | Weekly Only |
| 2025-W39 | Better Late Than Never | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Effective Reasoning Requires Good Demonstrations | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Hyper-Bagel | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Soft Tokens, Hard Truths | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Lavida-O | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | SimpleFold | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Blueprints of Trust | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | EmbeddingGemma | 19 | Low-score Source/Date/Rejection Verified | Weekly Only |
| 2025-W39 | Seedream 4.0 | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | SciReasoner | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Hunyuan3D-Omni | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Recon-Act | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | LayerNorm Induces Recency Bias | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | EPO | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Quantile Advantage Estimation | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | Variational Reasoning for Language Models | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | VoiceAssistant-Eval | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | StateX | 18 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W39 | WebGen-Agent | 19 | Low-score Source/Date/Rejection Verified | Reject |
| 2025-W35 | InternVL3.5 | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Hermes 4 Technical Report | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Model/Version Fact |
| 2025-W35 | Visual-CoG | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W35 | MMTok | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | UQ | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Neither Valid nor Reliable? | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Evidence Caution |
| 2025-W35 | CTF-Dojo | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | A.S.E | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | TiKMiX | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | VibeVoice | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Understanding Tool-Integrated Reasoning | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | UltraMemV2 | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | ThinkDial | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Optimal MoE Sparsity for Reasoning | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | StepWiser | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Vision-SR1 | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W35 | CODA | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Analysing CoT Dynamics | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Discrete Diffusion VLA | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Diffusion LMs Know the Answer Before Decoding | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Mind the Third Eye | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | DeepScholar-Bench | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Taming the Chaos | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Kubernetes v1.34 / DRA core GA | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | rStar2-Agent | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Pref-GRPO | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | MCP-Bench | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | AWorld | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | OneReward | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W35 | CogVLA | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | R-4B | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Model Recipe |
| 2025-W35 | EO-1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Model–Task Alignment and RL Conclusions | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Experimental Caveat |
| 2025-W35 | UItron | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | AHELM | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Domain Benchmark |
| 2025-W35 | Morae | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Interaction Study |
| 2025-W35 | ELV-Halluc | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Open Data Synthesis for Deep Research | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Metis | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Camlang | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | SQL-of-Thought | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | LLaVA-Critic-R1 | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | SATQuest | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | USO | 19 | Low-score Source/Date/Rejection Verified | Emerging / Experimental |
| 2025-W35 | TCIA | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Narrow Data Recipe |
| 2025-W35 | Provable Benefits of In-Tool Learning | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Rank-One Safety Injection | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Mixture of Contexts | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | OnGoal | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Interaction Study |
| 2025-W35 | Universal Deep Research | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | Face-MoGLE | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | MobiAgent | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W35 | C-DiffDet+ | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — Domain Detection Case |
| 2025-W37 | Qwen3-Next | 27 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | SAPO collective RL experience sharing | 28 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | WebExplorer | 26 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Paper2Agent | 26 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | SFR-DeepResearch | 24 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | AgentGym-RL | 27 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | CDE curiosity-driven RL | 25 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Parallel-R1 | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Visual Representation Alignment | 22 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Mini-o3 visual search | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Reconstruction Alignment | 22 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | F1 VLA | 26 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Language Self-Play | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Causal Attention with Lookahead Keys | 24 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | SimpleQA Verified | 25 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | RewardDance | 22 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | HuMo | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | EchoX | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Entropy-Modulated Policy Gradients | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | VLA-Adapter | 27 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | SimpleVLA-RL | 26 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | OmniEVA | 25 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | LoCoBench | 25 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Understanding-Generation Coexistence | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | SpatialVID | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Reverse-Engineered Reasoning | 22 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | dLLM RL framework | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | UniVerse-1 | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Off-policy RL + multi-agent tree search step-provers | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Guided Decoding for RAG | 25 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Test-Time Scaling on Knowledge-Intensive Tasks | 25 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | MachineLearningLM | 23 | Retained — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | AU-Harness | 26 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | Reasoning poisoning attacks | 26 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | PyTorch Distributed Checkpoint | 29 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | PyTorch native XCCL | 27 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | PyTorch-vLLM disaggregated inference | 28 | Core Candidate — Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W37 | MAS-Bench | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | Interleaving Reasoning for Text-to-Image | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | Kling-Avatar | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | mmBERT | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | FLUX-Reason-6M / PRISM-Bench | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | EnvX | 18 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | HumanAgencyBench | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | RL for Deep Research survey | 18 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | RL for Large Reasoning Models survey | 18 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | 3D and 4D World Modeling survey | 18 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | Fuzzing Brain | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | Capability-Adaptive Hint Scaffolding | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | RLVR divergence choice | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | vLLM 0.10.2 | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | SGLang 0.5.2 | 19 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | SafetyKit GPT-5 case study | 16 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W37 | Veo 3 Vertex AI GA | 15 | Archive Only — Low-score Closure | Weekly Only — Low-score Closure |
| 2025-W40 | DeepSeek-V3.2-Exp / DSA | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | SANA-Video | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | RL Skill Composition | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | DataMind | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Socratic-Zero | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | AgentDebug | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | GRPO-MA | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Dragon Hatchling / BDH | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Vision-Zero | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | dParallel | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | DeepSearch | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | GEM: A Gym for Agentic LLMs | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | VLA-RFT | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Predictability of RL Dynamics | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | LongCodeZip | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | ExGRPO | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Ovi | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | TOUCAN | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Scaling Agents for Computer Use | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | Hallucination Span Detection | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W40 | EasySteer | 19 | Low-score Source/Date/Rejection Verified | Reject — Framework Case |
| 2025-W40 | ROVER | 19 | Low-score Source/Date/Rejection Verified | Reject — Stylized RL Evidence |
| 2025-W40 | SCI-Verifier | 19 | Low-score Source/Date/Rejection Verified | Reject — Narrow Verifier Case |
| 2025-W40 | More Thought, Less Accuracy | 19 | Low-score Source/Date/Rejection Verified | Reject — Diagnostic Study |
| 2025-W40 | Muon Tail-End Memory | 19 | Low-score Source/Date/Rejection Verified | Reject — Narrow Optimizer Mechanism |
| 2025-W40 | DeepScientist | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Workflow |
| 2025-W40 | Attention as a Compass | 19 | Low-score Source/Date/Rejection Verified | Reject — Early Process-RL Case |
| 2025-W40 | Regression LM for Code | 19 | Low-score Source/Date/Rejection Verified | Reject — Code-Specific Objective |
| 2025-W40 | Specialization after Generalization | 19 | Low-score Source/Date/Rejection Verified | Reject — TTT Analysis |
| 2025-W40 | Knapsack RL | 19 | Low-score Source/Date/Rejection Verified | Reject — Budget-Heuristic Case |
| 2025-W40 | Beyond Log Likelihood | 19 | Low-score Source/Date/Rejection Verified | Reject — Objective Sensitivity |
| 2025-W40 | MixtureVitae | 19 | Low-score Source/Date/Rejection Verified | Reject — Dataset Report |
| 2025-W40 | StockBench | 18 | Low-score Source/Date/Rejection Verified | Reject — Domain Benchmark |
| 2025-W40 | F2LLM | 19 | Low-score Source/Date/Rejection Verified | Reject — Embedding Recipe |
| 2025-W40 | Interactive Training | 18 | Low-score Source/Date/Rejection Verified | Reject — Early Feedback Loop |
| 2025-W40 | ModernVBERT | 18 | Low-score Source/Date/Rejection Verified | Reject — Narrow Retriever |
| 2025-W40 | Tree-based Dialogue RPO | 19 | Low-score Source/Date/Rejection Verified | Reject — Attack-Generation Case |
| 2025-W40 | CLUE | 19 | Low-score Source/Date/Rejection Verified | Reject — Hidden-State Verifier |
| 2025-W40 | RewardMap | 19 | Low-score Source/Date/Rejection Verified | Reject — Visual-RL Case |
| 2025-W40 | Aristotle | 19 | Low-score Source/Date/Rejection Verified | Reject — Theorem-Proving Case |
| 2025-W40 | Sparse Query Attention | 19 | Low-score Source/Date/Rejection Verified | Reject — Architecture-Specific |
| 2025-W40 | VOGUE | 19 | Low-score Source/Date/Rejection Verified | Reject — Visual Exploration Case |
| 2025-W40 | DrBench | 19 | Low-score Source/Date/Rejection Verified | Reject — Domain Benchmark |
| 2025-W40 | Self-Forcing++ | 19 | Unverified / Blocked — Exact Material Request | Unverified / Blocked — Full Text Required |
| 2025-W41 | OpenAI Codex GA / `official:openai:codex-ga-2025-10-06` | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Google AI security frontier strategy / `official:google:saif2-2025-10-06` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | OpenAI political-bias evaluation / `official:openai:political-bias-eval-2025-10-09` | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Agentic Context Engineering / `arxiv:2510.04618` | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Hybrid Architectures for Language Models / `arxiv:2510.04800` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Reinforce-Ada / `arxiv:2510.04996` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Watch and Learn / `arxiv:2510.04673` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Multi-Agent Tool-Integrated Policy Optimization / `arxiv:2510.04678` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | BIRD-INTERACT / `arxiv:2510.05318` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Context Denoising Training / `arxiv:2510.05862` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | In-the-Flow Agentic System Optimization / `arxiv:2510.05592` | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | D2E / `arxiv:2510.05684` | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | TaTToo / `arxiv:2510.06217` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Asymmetric Ratios for Outcome-Supervised RL / `arxiv:2510.06062` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Lumina-DiMOO / `arxiv:2510.06308` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Webscale-RL / `arxiv:2510.06499` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Ming-UniVision / `arxiv:2510.06590` | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | RLinf-VLA / `arxiv:2510.06710` | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | SWE-IF / `arxiv:2510.07315` | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Artificial Hippocampus Networks / `arxiv:2510.07318` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Native Hybrid Attention / `arxiv:2510.07019` | 25 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | When Benchmarks Age / `arxiv:2510.07238` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | TTRV / `arxiv:2510.06783` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | WristWorld / `arxiv:2510.07313` | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Your Harness is Not Secure / `arxiv:2510.06607` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | When Thoughts Meet Facts / `arxiv:2510.07499` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Hybrid Reinforcement / `arxiv:2510.07242` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Learning to Route LLMs from Bandit Feedback / `arxiv:2510.07429` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Agent Learning via Early Experience / `arxiv:2510.08558` | 29 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | MM-HELIX / `arxiv:2510.08540` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | UniVideo / `arxiv:2510.08377` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | DeepPrune / `arxiv:2510.08483` | 23 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | First Try Matters / `arxiv:2510.08308` | 22 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Learning on the Job / `arxiv:2510.08002` | 28 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Memory Retrieval and Consolidation in LLMs through Function Tokens / `arxiv:2510.08203` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | Thinking with Camera / `arxiv:2510.08673` | 27 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | BigCodeArena / `arxiv:2510.08697` | 26 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | OpenRubrics / `arxiv:2510.07743` | 24 | Full Source Review Complete | Books Frozen — Historical Gate Closed |
| 2025-W41 | LightCache / `arxiv:2510.05367` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — narrow evidence |
| 2025-W41 | StaMo / `arxiv:2510.05057` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — narrow evidence |
| 2025-W41 | OBS-Diff / `arxiv:2510.06751` | 18 | Low-score Source/Date/Rejection Verified | Weekly Only — narrow pruning evidence |
| 2025-W41 | ARMOR / `arxiv:2510.05528` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — insufficient system delta |
| 2025-W41 | Global Planner Training / `arxiv:2510.05608` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — narrow task evidence |
| 2025-W41 | LongRM / `arxiv:2510.06915` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — benchmark-bound reward model |
| 2025-W41 | Training-Free GRPO / `arxiv:2510.08191` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — naming exceeds evidence |
| 2025-W41 | Alignment Waltz / `arxiv:2510.08240` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — preliminary alignment study |
| 2025-W41 | NaViL / `arxiv:2510.08565` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — narrow multimodal variant |
| 2025-W41 | CoMAS / `arxiv:2510.08529` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — system delta not isolated |
| 2025-W41 | Beyond Turn Limits / `arxiv:2510.08276` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — benchmark-specific |
| 2025-W41 | A2Search / `arxiv:2510.07958` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — search variant |
| 2025-W41 | BEAR / `arxiv:2510.08759` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — benchmark family only |
| 2025-W41 | Which Heads Matter for KV Compression / `arxiv:2510.08525` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — sensitivity result |
| 2025-W41 | Don't Waste Mistakes / `arxiv:2510.08696` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — training recipe evidence |
| 2025-W41 | ARES / `arxiv:2510.08457` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — limited generality |
| 2025-W41 | Speculative Jacobi-Denoising / `arxiv:2510.08994` | 19 | Low-score Source/Date/Rejection Verified | Weekly Only — no independent production evidence |
| 2025-W42 | PyTorch 2.9 | 25 | Complete | Refine — Existing Argument |
| 2025-W44 | gpt-oss-safeguard | 24 | Complete | Refine — Existing Argument |
| 2025-W44 | SGLang-JAX | 25 | Complete | Refine — Existing Argument |
| 2025-W45 | Kimi K2 Thinking | 23 | Complete | No Change — Already Covered |
| 2025-W45 | SGLang Diffusion | 22 | Complete | No Change — Already Covered |
| 2025-W46 | JAX-Privacy 1.0 | 25 | Complete | Refine — Existing Argument |
| 2025-W47 | Gemini 3 | 22 | Complete | Weekly Only — Version/Product Fact |
| 2025-W47 | Real-time speech-to-speech translation | 23 | Complete | Refine — Existing Argument |
| 2025-W48 | Claude Opus 4.5 | 21 | Excluded / Unverified | User-approved exclusion / Unverified |
| 2025-W49 | DeepSeek-V3.2 | 29 | Complete | Refine — Existing Argument |
| 2025-W49 | Mistral 3 | 23 | Complete | Refine — Existing Argument |
| 2025-W49 | Google Research synthesis of Titans + MIRAS | 22 | Complete | No Change — Already Covered |
| 2025-W50 | Differentially private chatbot-use analytics | 25 | Complete | Refine — Existing Argument |
| 2025-W50 | GPT-5.2 | 22 | Complete | Weekly Only — Version/Product Fact / Mechanism Not Disclosed |
| 2025-W51 | Gemini 3 Flash | 20 | Complete | Weekly Only — Version/Product Fact |
| 2025-W52 | SpecBundle and SpecForge v0.2 | 24 | Complete | Refine — Existing Argument |

## Weekly Links

- [2025-W01](./2025-W01/README.md)
- [2025-W02](./2025-W02/README.md)
- [2025-W03](./2025-W03/README.md)
- [2025-W04](./2025-W04/README.md)
- [2025-W05](./2025-W05/README.md)
- [2025-W06](./2025-W06/README.md)
- [2025-W07](./2025-W07/README.md)
- [2025-W08](./2025-W08/README.md)
- [2025-W09](./2025-W09/README.md)
- [2025-W10](./2025-W10/README.md)
- [2025-W11](./2025-W11/README.md)
- [2025-W12](./2025-W12/README.md)
- [2025-W13](./2025-W13/README.md)
- [2025-W14](./2025-W14/README.md)
- [2025-W15](./2025-W15/README.md)
- [2025-W16](./2025-W16/README.md)
- [2025-W17](./2025-W17/README.md)
- [2025-W18](./2025-W18/README.md)
- [2025-W19](./2025-W19/README.md)
- [2025-W20](./2025-W20/README.md)
- [2025-W21](./2025-W21/README.md)
- [2025-W22](./2025-W22/README.md)
- [2025-W23](./2025-W23/README.md)
- [2025-W24](./2025-W24/README.md)
- [2025-W25](./2025-W25/README.md)
- [2025-W26](./2025-W26/README.md)
- [2025-W27](./2025-W27/README.md)
- [2025-W28](./2025-W28/README.md)
- [2025-W29](./2025-W29/README.md)
- [2025-W30](./2025-W30/README.md)
- [2025-W31](./2025-W31/README.md)
- [2025-W32](./2025-W32/README.md)
- [2025-W33](./2025-W33/README.md)
- [2025-W34](./2025-W34/README.md)
- [2025-W35](./2025-W35/README.md)
- [2025-W36](./2025-W36/README.md)
- [2025-W37](./2025-W37/README.md)
- [2025-W38](./2025-W38/README.md)
- [2025-W39](./2025-W39/README.md)
- [2025-W40](./2025-W40/README.md)
- [2025-W41](./2025-W41/README.md)
- [2025-W42](./2025-W42/README.md)
- [2025-W43](./2025-W43/README.md)
- [2025-W44](./2025-W44/README.md)
- [2025-W45](./2025-W45/README.md)
- [2025-W46](./2025-W46/README.md)
- [2025-W47](./2025-W47/README.md)
- [2025-W48](./2025-W48/README.md)
- [2025-W49](./2025-W49/README.md)
- [2025-W50](./2025-W50/README.md)
- [2025-W51](./2025-W51/README.md)
- [2025-W52](./2025-W52/README.md)

## Legacy Books Integration Summary（Not Revalidated in This Phase）

Status: `Frozen legacy snapshot / 2025 Weekly rebuild does not modify Books`。

本轮以 74 个已核验候选的 primary evidence 重新审查相邻章节；`Refine` 只表示候选补强或修正
了长期机制，不表示每个同族事件都重复生成一段正文。

| Evolution Route | Primary Weekly | Books Owner | Integrated Understanding |
| --- | --- | --- | --- |
| hybrid / sparse / test-time memory | W01、W03、W07、W16、W40、W49 | Ch22；Ch73 boundary | dense、linear/recurrent、hybrid、native sparse、DSA 与 neural memory 是不同约束下的分支；新增 selector、kernel、online state、隔离与恢复成本 |
| reasoning RL | W04 | Ch29 | pure RL 展示 emergence；cold start、筛选/SFT、第二阶段 RL 与 distillation 分别解决可读性、行为约束和部署成本，不互相覆盖 |
| speculative artifact lifecycle | W10、W29、W30、W52 | Ch44 | drafter 从独立小模型演进到 EAGLE-3、MTP、训练系统和 target-coupled bundle；收益受 acceptance、verification 与 workload 约束 |
| accelerator resource contract | W35、W36、W38 | Ch59 | DRA core GA、health alpha、consumable-capacity alpha 分层；driver、scheduler、admission 与 recovery 各有 owner |
| differential privacy stack | W12、W21、W46、W50 | Ch68 | privacy unit 从 record/query、user contribution 延伸到 distributed training runtime 与 production telemetry；DP 不是省略 threat model/accounting 的标签 |
| RAG control loop | W20 | Ch72 | relevance、context sufficiency、faithfulness 和 abstention 分开治理 |
| evaluator-driven search | W20 | Ch77 | evaluator、candidate lineage、evaluation cascade、diversity、held-out verification 与 human deployment authority 构成 Workflow，不等于模型自我改进 |
| interpretability evidence | W13 | Ch5 | probing→sparse replacement→attribution graph→原模型 intervention；更可读的图以 reconstruction、pruning 与 attention blind spot 为代价 |
| reasoning budget and rollout state | W04、W05、W18、W32 | Ch20、Ch29、Ch52 | stopping/effort、partial trajectory、route identity 与 serving capacity 是不同 owner 下的同一 compute contract |
| distributed runtime evolution | W05、W12、W42、W44 | Ch32、Ch45、Ch46、Ch48 | collective call、one-sided memory、backend portability、single-engine state 与 distributed paths 分层演进，不互相覆盖 |
| training resilience and distillation | W13、W49 | Ch24、Ch25 | elastic recovery 要保持 trajectory semantics；cascade distillation 用更多 lineage 换取更平滑的 teacher/student capacity gap |
| streaming pipeline fusion | W47 | Ch38 | cascade 的可替换/可诊断性与 end-to-end streaming 的 latency/voice continuity 共存；fusion 收紧 failure domain |

未写入的主要类别：

- Claude、Gemini、Gemma、Mistral、GPT、Qwen、Kimi、GLM 等产品/模型版本若没有公开的新机制，
  仅保留版本事实和 evidence boundary；
- llm-d、KServe 与 Gateway API 的长期分层原则已由 Ch48、Ch49、Ch58 覆盖；vLLM V1、Dynamo、
  PyTorch 2.9 与 SGLang-JAX 只把新的演进边界 refine 到 Ch46、Ch48、Ch32、Ch45；
- PRESERVE、Chain of Agents、AI co-scientist、Mistral OCR、pluralistic alignment 等候选仍受
  硬件、任务、评测或实现披露限制，保留为 Weekly evidence；
- 所有厂商 benchmark 与单篇论文实验均未升级为无条件生产结论。

Claude Opus 4.5 是唯一没有全文核验的候选，已按用户明确批准排除。除该 exclusion 外，
2025 的 74 个候选已完成 primary-source review、相邻章节复核和最终 disposition；没有把厂商
benchmark、后发报告或产品能力写成无条件事实。

## 2026-08-24 W25 Superseding Closure

- W25 已从 40 行 lower-bound 扩展并闭合为 58 个唯一 owner：17 项高分、30 项中分、11 项低分。Root 逐行复算 58/58 六维 Total，核对 47/47 retained Full Source Review 与 11/11 low-score closure；普通 `Review Pending = 0`、`Blocked = 0`、family-level `Disputed = 0`。
- Discovery replay 额外恢复 10 个 2025-06-19～20 paper owner、6 个低分 family，以及 SGLang GB200 PD + large-scale EP 和 TensorRT-LLM v0.20.0 两个 Infra owner。vLLM v0.9.1 按 2025-06-10 tag 回拨 W24，不在 W25 重复评分。
- AceReason-Nemotron 1.1 与 Guru 各有一个内部 headline/table 数值冲突，只保留为 source-complete numerical subclaim dispute，不扩大为 family-level disputed。W25 Candidate Evidence Gate 通过；年度 Archive Completion 与 Historical Books Gate 仍关闭。

## 2026-08-24 W29 Superseding Closure

- W29 已从 35 行 lower-bound 扩展并闭合为 53 个唯一 owner：30 项高分、12 项中分、11 项低分。Root 逐行复算 53/53 六维 Total，并核对 42/42 retained strict Full Source Review 与 11/11 low-score closure；`Review Pending = 0`、`Blocked = 0`。
- 新恢复 9 个 20+ owner：ElasticMM、CodeJudgeBench、LoRA-MCL、IFScale、Deep Hidden Cognition、SENTINEL、PhyWorldBench、ECP 与 Astrogator。166 页 Context Engineering v1 已分节阅读全文；“1400+ papers”仅保留为作者口径，因为正文没有可复算 search protocol。
- RedOne 与 Teach Old SAEs 按 first-public date 回拨 W28，FlowSpec v2 保持 W27 owner，不在 W29 重复评分。数值、字段和 event-time artifact 差异均作为 source-complete evidence boundary 保留。W29 Candidate Evidence Gate 通过；Historical Books Gate 关闭。

## 2026-08-24 W28 Full Reconciliation

- W28 的 95 行旧账去重为 91 个 scored owners：65 项高分、21 项中分、5 项低分。Root 复算 91/91 六维 Total；RAT、GradOT、S³、DP-Fusion 按 2025-07-06 v1 回拨 W27，W27/W28 与 W28/W29 scored arXiv owner 交集均为 0。
- 86 个 retained 中 82 项完成 strict Full Source Review，4 项为精确 `Unverified / Blocked`，普通 `Review Pending = 0`；5/5 low-score closure 完成。NeoBabel 与 Spatio-Temporal LLM 的 v1 已恢复，不再列为 blocker。
- 剩余材料缺口为 POLAR v1 全文、Response Attack v1 全文、Agent KB 2025-07-08 v1 revision、Teach Old SAEs 2025-07-08 OpenReview original submission。每项均记录已知来源、现有材料不足、可接受替代、建议文件名与补回审计范围。Candidate Evidence Gate 为 Conditional，academic immutable cross-index recall 与年度 Archive Completion 保持 Open；Historical Books Gate 关闭。

## 2026-08-24 W31 Full Reconciliation

- W31 已从 6 行 strict baseline 扩展并闭合为 36 个 scored owners：16 项高分、4 项中分、16 项低分。Root 复算 36/36 六维 Total，核对 20/20 retained Full Source Review 与 16/16 low-score closure；普通 `Review Pending = 0`、`Unverified / Blocked = 0`。
- G-Core `2507.22789` 的 2025-07-30 事件时 16 页 v1 已恢复；由于 v2 次日以“未经公司批准”撤回，该 family 保持 source-complete `Disputed — Withdrawn Source / Mechanism Evidence Frozen`，不作为正常公司发布，也不得进入 Books。Graph-R1 与 DICE 的 claim-level formal disputes同样保留。
- H-MEM、ARPO、GEPA、Deep Researcher、Beyond Binary Rewards、Quantization Geometry回拨W30；TensorRT-LLM rc5/0.21.0归W32。W30/W31/W32 scored arXiv owner 去重通过。W31 Candidate Evidence 与 Discovery Replay Gate 通过；年度 Archive Completion 与 Historical Books Gate 关闭。

## 2026-08-24 W30 Full Reconciliation

- W30 已从 3 行旧账扩展并闭合为 51 个 scored owners：26 项高分、10 项中分、14 项普通低分和 1 项低分材料 blocker。Root 复算 51/51 六维 Total，核对 36/36 retained Full Source Review 与 15/15 low-score/blocked closure；普通 `Review Pending = 0`。
- 唯一材料缺口是 Zebra-CoT `2507.16746v1`：identity/v1 date可核，但全文不可得，当前 19 分只代表摘要边界，不把缺正文洗成可信拒绝。材料请求明确为 v1 PDF/HTML/TXT 或作者同版 manuscript，补回后重做 Method、实验、ablation、Appendix、limitations、score 与 disposition。
- 14 个 pre-W30 owner 回拨 W29，未重复评分。W30 Candidate Evidence Gate 为 `Conditional Pass — 1 Exact External Material Blocker`，允许 forward cursor 继续，但阻塞无材料缺口与 2025 Archive Completion 声明；Historical Books Gate关闭。

## 2026-08-24 W30/W31 Spillback Reopen from W32

- W32 的 event-date replay 发现 Efficient Agents (`2508.02694`)、InstructVLA (`2507.17520`) 与 Dens3R (`2507.16290`) 归 W30，但未进入刚写回的 51 行账本，因此 W30 的 51 行 closure 被重开。
- 同一 spillback ledger 有 14 个 W31 owner；Cognitive Kernel-Pro 与 RL-PLUS 已在 W31 低分账本，其余 12 项尚未进入 W31 canonical score ledger。W31 的 36 行 closure 也被重开，必须在 W30 修复后串行复核。
- 在两周重新完成评分、20+ review/低分 closure、去重与 Gate writeback 前，年度索引中的 W30/W31 行只是 superseded snapshot，不得作为完成证明；Historical Books Gate继续关闭。

## 2026-08-24 W30 Spillback Reclosure

- W30 已吸收 W32 路由的 Efficient Agents、InstructVLA 与 Dens3R，最终账本由 51 行重闭合为 54 个 scored owners：29 项高分、10 项中分、14 项普通低分及 1 项低分材料 blocker。Root 复算 54/54 六维 Total，并核对 39/39 retained Full Source Review 与 15/15 low-score/blocked closure；普通 `Review Pending = 0`。
- Efficient Agents 按 arXiv v1 的 2025-07-24 路由；正文 title page 的 2026-08-11 与 submission history 冲突，只作为 manuscript 内部日期异常记录，不用于 owner 路由。InstructVLA 与 Dens3R 分别按 2025-07-23、2025-07-22 v1 归 W30。
- Zebra-CoT `2507.16746v1` 仍是唯一精确外部材料 blocker，因此 W30 Candidate Evidence Gate 为 `Conditional Pass`，并不等于年度 Archive Completion。W30 reopen 已闭合；W31 的 12 个遗漏 owner 仍待重建，Historical Books Gate继续关闭。

## 2026-08-24 W31 Spillback Reclosure

- W31 已补入 W32 路由发现且旧账缺失的 12 个 canonical owner；RL-PLUS 与 Cognitive Kernel-Pro 作为已收录低分 owner 去重保留。最终账本由 36 行重闭合为 48 个 scored owners：21 项高分、11 项中分、16 项低分。
- Root 复算 48/48 六维 Total，核对 32/32 retained Full Source Review、16/16 low-score closure 以及 12/12 新增非模板化 review；普通 `Review Pending / Unverified / Blocked = 0 / 0 / 0`。W30/W31 scored owner 无重复；W32 对这些 ID 的出现仅为 spillback 路由，不是第二次计分。
- W31 Candidate Evidence 与 Discovery Replay Gate 重新通过；W32 暴露的 W30/W31 spillback 已全部写回 owner week。年度 Archive Completion 与 Historical Books Gate仍关闭，本检查点未修改Books。

## 2026-08-24 W32 Full Reconciliation

- W32 已从 3 行旧账扩展并闭合为 41 个 scored owners：14 项高分、2 项中分、25 项低分。Root 复算 41/41 六维 Total，核对 16/16 retained Full Source Review 与 25/25 low-score closure；普通 `Review Pending / Blocked / family-level Disputed = 0 / 0 / 0`。
- VeriGUI v1 与 2026 年改名重构后的 VeriWeb v2 被严格版本隔离；SWE Agent RL、SEAgent、R-Zero、Dynamic Fine-Tuning、VeOmni、ToolTrain、AttnTrace revision均未倒灌。旧“Books Gate已完成”冲突已删除，Historical Books Gate关闭。
- 17 个跨周发现全部按 first-public date 路由；其中新暴露的 W30/W31 omissions 已在独立 reopen checkpoint记录，不影响 W32 自身 41 行 Gate。W32 Historical Weekly Evidence Gate通过，年度 Archive Completion保持Open。

## 2026-08-24 W33 Full Reconciliation

- W33 已撤回旧“空周”结论并闭合为 36 个 scored owners：12 项高分、12 项中分、12 项低分。Root 复算 36/36 六维 Total，核对 24/24 retained Full Source Review 与 12/12 low-score closure；普通 `Review Pending / Unverified / Blocked / family-level Disputed = 0 / 0 / 0 / 0`。
- 所有 owner 按 2025-08-11～2025-08-17 的 first-public/v1 日期归档；同周 revision 合并，早周 v1 的后续 revision 与 W32 spillback只回链不计分。vLLM 1.0 RFC只作为公开计划事实，不写成已发布 runtime 能力。
- 独立 Review Checkpoint 已复核 denominator、Total、primary evidence、日期、Source Family、Stable Node owner、事实与推断边界及 Markdown。W33 Historical Weekly Evidence Gate通过；Historical Books Gate与年度 Archive Completion继续关闭。

## 2026-08-24 W34 Full Reconciliation

- W34 的 21-row 初稿在独立 recall Review 中被推翻，补回 4DNeX、Next Visual Granularity、S²-Guidance、Precise Action-to-Video、FLARE、MeshCoder 与 Dissecting Tool-Integrated Reasoning 后，最终闭合为 28 个 scored Source Families：17 项高分、8 项中分、3 项低分。
- Root 复算 28/28 六维 Total，核对 25/25 retained Full Source Review 与 3/3 low-score closure；Source Family、日期、revision 与相邻周 spillback去重通过，普通 `Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- W34 Candidate Evidence Gate通过；DeepSeek-V3.1只保留公开 version/artifact/API contract，不反推未公开内部机制。Historical Books Gate与年度 Archive Completion继续关闭，本检查点未修改Books。

## 2026-08-24 W34 Owner-Date Reopen from W35

- W35 相邻周复核与 root 对 arXiv submission history 的独立核验确认：TPLA `2508.15881` v1 为 2025-08-21；`2508.16153` 是 Memento（不是 AgentFly），v1 为 2025-08-22。两项都属于 W34，而不是 W35。
- W34 当前 Cross-Week ledger 把两项错误写成 2025-08-25 W35 owner，且误标了第二项身份。因此 28-row closure 已重开；在 TPLA 与 Memento 完成评分、Full Source Review、身份/日期纠正、年度 writeback和新 Gate 前，不得把该快照视为最终 denominator。
- W35 必须排除两项重复计分；Historical Books Gate与年度 Archive Completion继续关闭。

## 2026-08-24 W34 Owner-Date Reclosure

- W34 已补入 TPLA 与 event-time AgentFly→current Memento lineage，账本由 28 行重闭合为 30 个唯一 Source Families：19 项高分、8 项中分、3 项低分。Root 复算 30/30 六维 Total，核对 27/27 retained Full Source Review 与 3/3 low-score closure。
- TPLA v1 2025-08-21、AgentFly v1 2025-08-22；两项 2025-08-25 v2与标题 revision只作 same-family evidence，不在W35计分。普通 `Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- W34 Independent Review与Weekly Evidence Gate重新通过；owner-date reopen已闭合。Historical Books Gate与年度Archive Completion继续关闭。

## 2026-08-24 W35 Full Reconciliation

- W35 已从 1 项 legacy seed 重建并闭合为 36 个 canonical Source Families：19 项高分、8 项中分、9 项低分。Root 复算 36/36 六维 Total，核对 27/27 retained Full Source Review 与 9/9 low-score closure；普通 `Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- TPLA 与 event-time AgentFly→current Memento lineage按 v1 日期回拨 W34，没有进入 W35 评分；Kubernetes v1.34/DRA core GA归 W35，9月后续说明只作同 family evidence node。
- 独立 Review Checkpoint已复核 denominator、日期、revision、Source Family、Stable Node owner、相邻周去重、事实边界与Markdown。W35 Weekly Evidence Gate通过；Historical Books Gate与年度 Archive Completion继续关闭。

## 2026-08-24 W35 Owner-Date Reopen from W36

- W36 相邻周 replay 发现 7 个 v1 日期属于 W35 且不在当前 36 行 canonical ledger 的 owner：LLaVA-Critic-R1 `2509.00676`（2025-08-31）、Metis `2509.00404`（08-30）、Open Data Synthesis `2509.00375`（08-30）、Camlang `2509.00425`（08-30）、SQL-of-Thought `2509.00581`（08-30）、SATQuest `2509.00930`（08-31）、ELV-Halluc `2508.21496`（08-29）。
- 36-row closure 已重开；7 项完成评分、Full Source Review或低分 closure、去重、年度 writeback与新 Gate 前，该快照不得作为最终 denominator。W36 不重复计分。
- Historical Books Gate与年度 Archive Completion继续关闭。

## 2026-08-24 W35 Owner-Date Reclosure

- W35 已补入 W36 replay 暴露的 7 个 owner-date spillback，账本由 36 行重闭合为 43 个唯一 Source Families：23 项高分、11 项中分、9 项低分。Root 机械复算 43/43 六维 Total，核对 34/34 retained Full Source Review 与 9/9 low-score closure；普通 `Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- ELV-Halluc、Open Data Synthesis、Metis、Camlang、SQL-of-Thought、LLaVA-Critic-R1 与 SATQuest 均按 2025-08-29～31 的 arXiv v1 日期归 W35；W34/W36 评分表未重复计分。
- W35 Independent Review 与 Weekly Evidence Gate 重新通过；Historical Books Gate 与年度 Archive Completion继续关闭，本检查点未修改 Books。

## 2026-08-24 W35 Second Owner-Date Reopen from W36

- W36 denominator stabilization确认 Universal Deep Research `2509.00244` 的v1为2025-08-29，必须从W36移出并回拨W35；同一replay又发现 Mixture of Global and Local Experts `2509.00428`、MobiAgent `2509.00531` 与 C-DiffDet+ `2509.00578` 的v1均为2025-08-30，且不在W35当前43行账本。
- W35的43-row reclosure再次重开。四项完成评分、Full Source Review或低分closure、去重、年度writeback与新Gate前，该快照不得作为最终denominator；W36不得重复计分。
- Historical Books Gate与年度Archive Completion继续关闭。

## 2026-08-24 W14 Gap Reclosure

- W14 已从46项下界重闭合为61个scored owners：43项高分、14项中分、4项低分。Root复算61/61六维Total与候选唯一性，核对57/57 retained Full Source Review和4/4 low-score closure；ordinary `Review Pending / Unverified / Blocked = 0 / 0 / 0`。
- 新恢复15项，包括由W15回拨的Rethinking Reflection；ACTalker/WikiVideo artifact gap、OpenCodeReasoning artifact drift与SkyReels-A2 revision/ablation dispute都保留为source-complete evidence boundary，不误写成已复现。
- W14 Candidate Evidence Gate通过，Discovery Replay Closed，Archive Completion因artifact/revision边界为Conditional；年度索引已从旧47行related-mixed账本同步为61个canonical scored owners。Historical Books Gate关闭，本检查点未修改Books。

## 2026-08-24 W37 Full Reconciliation

- W37 已从 1 项 legacy seed 重建并闭合为 54 个 canonical owners：19 项高分、18 项中分、17 项低分。Root 复算 54/54 六维 Total，核对 37/37 retained Full Source Review 与 17/17 low-score closure；普通 `Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- 九个 v1 属于 W36 的 family均只作spillback：串行对账确认其中七项已在W36 rebuilt ledger，真正触发W36补录的是 `2509.03646` 与 `2509.05209`；W37没有重复计分。
- W37 Candidate Evidence Gate通过；Discovery/Archive Gate仅因缺immutable Scholar/OpenAlex export保持Conditional，Historical Books Gate关闭。

## 2026-08-24 W12 Gap Reclosure

- W12 已从旧43-owner下界重新闭合为110个owner identities：98项strict Full Source Review、7项低分closure、5项精确`Unverified / Blocked`，ordinary `Review Pending = 0`。Root核对分母分解、五项材料请求、四个W11 spillback排除关系与Markdown；ETVA v1、vLLM v0.8.1、Transformers v4.50.0和JAX v0.5.3已恢复。
- TokenBridge、Judge Anything、TULIP v1、One-Step Residual Shifting Diffusion v1与VideoRFSplat v1仍缺event-time全文，每项均有已知URL、缺失原因、可接受材料、建议文件名和补回后的审计范围。按用户授权执行blocked-skip，Candidate Evidence Gate为Conditional Pass；Archive source-complete与年度Archive Completion仍Open。
- Historical Books Gate关闭，本检查点未修改Books。年度候选明细表仍需从旧43行同步到110-owner最终账本，该索引差异已纳入全局账本修复，不能以旧行数解释W12内容分母。

## 2026-08-24 W36 Full Reconciliation

- W36 已从1项legacy seed重建为65个canonical owners：13项高分、11项中分、41项低分；24/24 retained Full Source Review与41/41 low-score closure闭合，root复算65/65六维Total且Source Family无重复，ordinary `Review Pending = 0`。
- Robix `2509.01106v1`是唯一`Unverified / Blocked`，已有精确P1全文材料请求；按用户授权blocked-skip，W36 Weekly Evidence Gate为Pass with disclosure，年度Archive source-complete仍Open。
- 十一个v1属于W35的family均未在W36计分：原七项已由W35恢复，新增四项触发W35 second reopen。年度索引已从旧1行同步到65行；Historical Books Gate关闭，本检查点未修改Books。

## 2026-08-24 W38 Full Reconciliation

- W38 已从2项legacy seed重建为50个scored Source Families：24项高分、3项中分、23项低分。Root复算50/50六维Total、50个唯一Source Family与窗口日期，核对27/27 retained Full Source Review和23/23 low-score closure；`Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- W37与当前W39均无重复计分；八个earlier-owner family只作spillback，其中`2506.02153`已确认存在于W23 canonical ledger，不构成新遗漏。年度索引已从旧2行同步到50行。
- W38 Weekly Evidence Gate通过；Historical Books Gate与年度Archive Completion继续关闭，本检查点未修改Books。

## 2026-08-24 W13 Gap Reclosure

- W13 已从60项下界重闭合为62个scored owners：39项高分、9项中分、14项低分。Root复算62/62六维Total与候选唯一性，核对48/48 retained Full Source Review和14/14 low-score closure；`Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。
- RLHF Data Scaling `2503.22230v1`已恢复全文；Megatron-LM MTP implementation event与DeepSpeed v0.16.5被补回。Transformers v4.50.0按03-21归W12，W13只保留v4.50.1～3 patch family；三个related evidence node不重复计分。
- W13 Candidate Evidence Gate通过，Discovery Replay因无法冻结历史cross-index exhaustive export为Conditional Pass。年度索引已从旧63行related-mixed账本同步为62个canonical scored owners；Historical Books Gate关闭，本检查点未修改Books。

## 2026-08-24 W35 Second Owner-Date Reclosure

- W35 的second reopen没有停在指定四项补丁：完整submission-history与recommendation回查又恢复USO、TCIA、In-Tool Learning、Rank-One Safety Injection、Mixture of Contexts与OnGoal。最终账本从43扩展为53个唯一Source Families：28项高分、12项中分、13项低分。
- Root复算53/53六维Total、Source Family唯一性与ROADMAP owner，核对40/40 retained Full Source Review和13/13 low-score closure；`Review Pending / Unverified / Blocked / Disputed = 0 / 0 / 0 / 0`。W36 routing ledger的四项已改为Recovered，且未在W36 Candidate Scoring重复计分。
- W35 Discovery与Evidence Gate重新通过，年度索引已同步53行；8月30～31日HF feed不可访问的召回边界仍明确披露，不被写成全网穷尽证明。Historical Books Gate与年度Archive Completion继续关闭。

## 2026-08-24 W38 Owner-Date Reopen from W39

- W39 look-ahead确认至少9个v1日期属于W38且不在当前50行账本的owners：RPG `2509.16198`、MANZANO `2509.16197`、BaseReward `2509.16127`、VLAC `2509.15937`、Ask-to-Clarify `2509.15061`、Audio DLM `2509.16622`、ARE `2509.17158`、SWE-Bench Pro `2509.16941`与HAPO `2509.16591`，first-public均为2025-09-18～21。
- W38的50-row closure与年度50行快照已重开；九项完成评分、Full Source Review或低分closure、去重、年度writeback与新Gate前不得宣称最终完成。W39只保留spillback关系，不重复计分。
- Historical Books Gate与年度Archive Completion继续关闭。

## 2026-08-24 W01 / W40 Ledger Synchronization

- W01 年度明细已补回此前只存在于周文件低分 ledger 的 13 项记录；年度账本现为 50/50，分解为 37 项 Full Source Review 与 13 项 source/date/score/rejection closure。该修复只同步既有结论，没有重开 W01 Weekly Evidence Gate。
- W40 已从 1 项 legacy seed 完整重建为 44 个 canonical owners：20 项 `20+` retained、23 项普通低分和 1 项精确 full-text blocker。Root 复算 44/44 六维 Total，核对 20/20 Full Source Review、24/24 low/blocked closure 与 22/22 W39 spillback 排除关系；年度索引已同步 44 行。
- Self-Forcing++ `2510.02283v1` 仍缺事件时全文，保持 `Unverified / Blocked — Exact Material Request`；按 blocked-skip 允许 forward sweep，但年度 Archive Completion 不得关闭。Historical Books Gate 保持关闭，本检查点未修改 Books。

## 2026-08-24 W38 / W39 Final Reclosure

- W38 没有停在最初 9 项补丁或 80 行中间快照：完整 9 月 18～21 日 feed replay 最终将账本从旧 50 行重闭合为 88 个唯一 owner，分解为 38 项高分、10 项中分与 40 项低分。48/48 retained Full Source Review 与 40/40 low-score closure 已闭合，评分 Total、日期、Source Family、ROADMAP owner 和相邻周边界均通过独立复算；ordinary `Review Pending / Blocked / Disputed = 0 / 0 / 0`。
- W39 已从 1 项 legacy seed 重建为 64 个唯一 owner：34 项高分、10 项中分、20 项低分；44/44 retained Full Source Review 与 20/20 low-score closure 已闭合。W40 暴露的 22 个 W39 owner 全部回收，12 个 earlier-owner spillback 只路由、不在 W39 重复计分；`Review Pending / Blocked / Disputed = 0 / 0 / 0`。
- 年度明细表已分别同步 W38 的 88 行与 W39 的 64 行。两周 Weekly Evidence Gate 通过，但年度 Archive Completion 与 Historical Books Gate 继续关闭；本检查点未修改 Books。

## 2026-08-24 Historical Forward Pause after W41

- 本次收口组已完成并独立复核 W38～W41。最终账目为：W38 `88 = 38 high + 10 medium + 40 low`，W39 `64 = 34 + 10 + 20`，W40 `44 = 20 + 0 + 24`，W41 `55 = 27 + 11 + 17`；各周 retained/low-or-blocked closure 分别为 `48/40`、`44/20`、`20/24`、`38/17`，ordinary `Review Pending = 0`。
- W41 从错误的 No Material Update 重建为 55 个唯一 Source Families，并从 W42 feed/history 回拨 21 个 first-public 属 W41 的 owner。年度候选明细已同步 W41 的 55 行；W38～W41 的周文件、年度行数与分类账现一致。
- 用户要求在本组结束后暂停。Historical Forward Cursor 固定为：`W01～W41 已处理；Next: W42`。下次不得跳过 W42，也不得直接进入 Historical Books Integration。
- 已知索引维护 backlog：W12 周文件已闭合为 110 个 owner identities，但年度明细仍保留旧 43 行，需在后续单独按分段账本同步；这不改变 W12 文件的 `98 strict + 7 low + 5 blocked` 条件闭合，也不得被误报为 43-owner final denominator。
- Annual Archive Completion 与 Historical Books Gate 继续关闭。本轮没有修改 Books，没有执行 stage、unstage、commit、push、reset、checkout 或 clean。
