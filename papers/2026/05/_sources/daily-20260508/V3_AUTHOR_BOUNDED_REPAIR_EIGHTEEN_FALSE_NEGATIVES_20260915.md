# 2026-05-08：18 项 false negative 限定返修

## 范围与结论

本轮只重开 fresh non-author reviewer 指定的 18 个既有 `619` raw Source Family；没有扩展日期、来源、候选 sibling 或重新枚举。18 份 official exact-v1 HTML 均可访问，题名与 canonical ledger 一致，页面未见 withdrawal banner；`blocked / disputed / withdrawn = 0 / 0 / 0`。

返修后机械账为 `619 = 184 retained + 435 closure`，184/184 已完成 Evidence Review，新增 `5 deep + 13 standard`，累计 `129 deep + 55 standard`；Score V3 累计 `108` 项 7～9 分、`76` 项 5～6 分。18 项中 15 项需要 root Books writeback，3 项为具体 `No Change — Existing Coverage`。作者不编辑 Books，本日报继续 `Ongoing`，不得自签最终 Gate。

## 身份、评分与 disposition

| arXiv | Score V3（Delta+Reach+Durability） | Review | Stable Node | Books Decision |
| --- | --- | --- | --- | --- |
| `2605.05245` | `2+3+2=7` | Deep | `AGENT-RAG` | Integrate — Pending root writeback |
| `2605.05277` | `2+3+2=7` | Deep | `PLATFORM-SECURITY` | Integrate — Pending root writeback |
| `2605.05386` | `2+2+2=6` | Standard | `AGENT-PLANNING` | No Change — Existing Coverage |
| `2605.05415` | `3+2+2=7` | Deep | `TRAIN-RLHF` | Integrate — Pending root writeback |
| `2605.05438` | `2+2+2=6` | Standard | `TRAIN-SFT` | Integrate — Pending root writeback |
| `2605.05495` | `2+1+2=5` | Standard | `MODEL-TRANSFORMER-LAYER` | No Change — Existing Coverage |
| `2605.05503` | `2+2+2=6` | Standard | `PLATFORM-SECURITY` | Integrate — Pending root writeback |
| `2605.05638` | `2+2+2=6` | Standard | `PLATFORM-EVALUATION-SYSTEM` | Integrate — Pending root writeback |
| `2605.05718` | `3+2+2=7` | Deep | `INFER-DYNAMO` | Integrate — Pending root writeback |
| `2605.05980` | `2+2+2=6` | Standard | `AGENT-REFLECTION` | Integrate — Pending root writeback |
| `2605.06040` | `2+1+2=5` | Standard | `AGENT-PLANNING` | No Change — Existing Coverage |
| `2605.06052` | `2+2+2=6` | Standard | `INFER-TENSORRT-LLM` | Integrate — Pending root writeback |
| `2605.06247` | `2+2+2=6` | Standard | `MULTIMODAL-WORLD-MODELS` | Integrate — Pending root writeback |
| `2605.06376` | `2+2+2=6` | Standard | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate — Pending root writeback |
| `2605.06480` | `2+2+2=6` | Standard | `PLATFORM-EVALUATION-SYSTEM` | Integrate — Pending root writeback |
| `2605.06583` | `3+2+2=7` | Deep | `TRAIN-RLHF` | Integrate — Pending root writeback |
| `2605.06601` | `2+2+2=6` | Standard | `AGENT-WORKFLOW` | Integrate — Pending root writeback |
| `2605.06667` | `2+2+2=6` | Standard | `MULTIMODAL-GENERATIVE-PARADIGMS` | Integrate — Pending root writeback |

## 逐项 Evidence Review

### `2605.05245` — AdaGATE

- **Baseline → mechanism/state:** fixed top-k 与 additive retrieval 在多跳问题中不能显式修复 bridge-fact gap。§3.1～3.4 让 controller 持有 `evidence set / entity ledger / unresolved gaps / token budget`，由 gap micro-query、question fallback 与 coverage/corroboration/novelty/redundancy utility 更新集合。
- **Evaluation / boundary:** §4～5 仅在 HotpotQA clean/redundancy/noise 与 `k=3` 下比较 evidence F1、grounding 和 token；预算甚至未充分 binding。启发式权重、web-scale 与 conservative abstention 未解决。
- **Trade-off / fallback / Books:** 以额外 ledger、LLM primitives 与停止校准换更小 context 和显式 repair；gap 不可靠时回退 question-anchored retrieval，低风险单跳仍用 fixed top-k。Ch76 已有 setwise selection 与 sufficiency，但没有“未决 gap 拥有迭代 repair/control state”这一命题，需写回。

### `2605.05277` — GLiNER Guard

- **Baseline → mechanism/state:** moderation 与 PII 分开运行会重复编码；§3 用共享 encoder 在一次 forward 中输出 classification 与 span extraction，uni/bi/omni 分支分别交换 schema interaction、label cache、吞吐与 transfer，policy 仍拥有最终判决。
- **Evaluation / boundary:** §4～6 与 Appendix D 的 serving 只绑定 single A100、作者 batching/context、公开 safety suites 和合成俄语 PII-Bench；response moderation、长上下文、多语言仍弱，端到端 PII 还混有规则组件。
- **Trade-off / fallback / Books:** always-on encoder 降低成本但牺牲复杂推理；不确定请求升级 autoregressive moderator，detector 失校准则人工/规则 fail-closed。Ch72 已有 PII sensor contract，却没有统一 forward 与 tiered cascade 的 execution boundary，需由 Ch72 写回、Ch42 只 handoff request path。

### `2605.05386` — BALAR

- **Mechanism / evidence:** §4.2～4.7 维护 factorized latent belief，以 expected mutual information 选择澄清问题，并在现有维度不足时扩展 state；§5～7 只支持三个作者 benchmark 与其 LLM/user simulator。
- **Trade-off / fallback:** 结构化 belief 和 sleep-time initialization 降低每轮搜索，却引入 prior、likelihood、维度生成与用户回答噪声；高风险或 belief 不可校准时回退直接 tool observation、显式澄清或人工判断。
- **No Change:** Ch79 已明确 `policy(goal, belief, plan)`、主动查询 latent state，以及 `belief + tool reliability + expected information gain → ask/act/verify/stop`，并保留主观概率不是 authority 的边界；本证据不改变该命题。

### `2605.05415` — Warden

- **Baseline → mechanism/state:** continuous adversarial training 对观测攻击样本近似均匀聚合。§3 让 training objective 在 f-divergence ambiguity set 内求 worst-case reweighting；KL dual 形成 log-sum-exp，`epsilon/lambda` 拥有 robustness–utility 强度。
- **Evaluation / boundary:** §4～5 只覆盖披露的 instruction-tuned models、HarmBench subset 与 CAT/CAPO/MixAT attack pipeline；重权 hard observed samples 不证明 unseen attacks robust。
- **Trade-off / fallback / Books:** 更关注 residual vulnerability，却可能过拟合少数高 loss 样本并引入 dual 超参；半径/utility regression 不稳时回退 uniform aggregation 与更广 attack suite。Ch31 未承载 ambiguity-set/worst-case aggregation，需写回。

### `2605.05438` — Semantic Loss

- **Baseline → mechanism/state:** cross-entropy 只奖励标签，在 class imbalance/structured reasoning 下可由 constant answer 取得表面高 accuracy。§4 用 graph-consistency semantic constraint 与动态 lambda 将结构违反纳入 SFT objective。
- **Evaluation / boundary:** §5～6、Appendix A/B 只覆盖 Gemma 270M、transitivity/d-separation 与作者构造数据；`200k+` evaluation samples 不能证明通用 causal reasoning，论文的“essential”措辞不得外推。
- **Trade-off / fallback / Books:** 结构约束阻止局部 collapse，却依赖正确 graph/schema 和 loss schedule；结构先验错误时会固化偏差。Ch29 已讲 output collapse 与多轴验收，但缺 label loss 与 semantic constraint 的 objective 分权，需写回；无可靠规则时回退 CE + balanced slices/behavioral tests。

### `2605.05495` — Continual LEGO

- **Mechanism / evidence:** §3～5 在受控 continual compositional task 中比较 BERT feed-forward 与 ALBERT shared recurrent block；前者形成 shortcut，后者对 forward transfer 更有利，但两者跨 experience composition 仍失败，replay/combined experience 的收益也非通用。
- **Boundary/fallback:** 小模型、人工代数任务与 architecture confound 不证明 recurrence 普遍优于 depth；固定 stack 在吞吐、可预测和开放任务证据不足时仍是默认。
- **No Change:** Ch17 已完整拥有 `fixed parameter stack → shared recurrent block → execution-depth state`、组合任务证据、shortcut/停止/吞吐 failure 与 fixed-depth fallback；无需重复论文案例。

### `2605.05503` — Chainwash

- **Baseline → mechanism/state:** 单次 paraphrase robustness 不能代表 provenance signal 的多轮存活。§3～5 将 rewrite model/style/hop 与 detector threshold 组成 threat state，连续无密钥 rewriting 使原始 DLM watermark 信号接近 null。
- **Evaluation / boundary:** 证据只绑定 LLaDA-8B-Instruct、同一 watermark 配置、四个 1.5B～8B rewriter、五种 style、约 300-token outputs；不证明所有 DLM watermark 或更长文本同样失效。
- **Trade-off / fallback / Books:** watermark 便宜但在语义保持的变换链上脆弱；release/attribution 不得由单 detector 拥有，需 provenance、签名或受控 origin record 交叉验证。Ch72 尚缺 multi-hop laundering threat contract，需写回。

### `2605.05638` — Label-free OOD

- **Baseline → mechanism/state:** class-conditional labels或专用 fine-tuning 常被视为 OOD 必需；§3～5 对 frozen representation 同时应用 global Mahalanobis 与 local score-curvature probe，并把 detector difference 与 backbone representation geometry 分账。
- **Evaluation / boundary:** 59 个 vision/language backbone-task pairing 支持作者范围的收敛趋势；只比较两类 label-free detector，未覆盖所有 modality、hard shift 或 production threshold。
- **Trade-off / fallback / Books:** 无标签 probe 便宜且可部署，却会把 representation saturation/geometry drift 变成 calibration state；检测器失配时回退 labeled slice、task-specific detector 与人工 release gate。Ch66 有 OOD/representation sensor 的原则，但缺“先验 representation quality 可主导 detector choice”的受限演进，需写回。

### `2605.05718` — CE-FI

- **Baseline → mechanism/state:** conventional federation/cooperative inference 共享 raw input、parameters 或 common encoder。§III 用 unlabeled shared data 训练 consensus embedding 与 cooperative output，使 heterogeneous intermediate states 对齐后再 ensemble。
- **Evaluation / boundary:** §IV 覆盖 CIFAR、text/time-series 与 non-IID slices；alignment 是主要瓶颈，reconstruction test 不等于 privacy proof，规模、通信、advanced attacks 未验证。
- **Trade-off / fallback / Books:** 少共享换来 alignment training、通信与新的 intermediate-leakage surface；对齐/隐私不成立时回退 solo inference、同构 ensemble 或受控 parameter federation。Ch52 缺跨组织 heterogeneous model state 的 inference contract，需写回；Ch71 只接收 tenant/privacy handoff。

### `2605.05980` — TACT

- **Baseline → mechanism/state:** 只在 tool failure 后 reflection 无法提前识别 overthinking/overacting。§2 把 trajectory step 标注为 calibrated/两类 drift，抽取正交 residual axes，并在 test time 把 activation 拉回 calibrated region。
- **Evaluation / boundary:** §3 在 SWE-bench Verified、Terminal-Bench 2.0、CLAW-Eval 与两模型报告 outcome/steps；LLM-as-judge 标签、线性可分与 coding domain 不证明 causal、跨模型或安全泛化。
- **Trade-off / fallback / Books:** 无额外 LLM call 换来 white-box activation access、probe calibration 与错误 steering 风险；轴漂移时回退 observation-based loop guard、budget/stop rule 和外部 verifier。Ch80 有行为级 reflection，但没有 trajectory drift sensor 与 intervention authority 分离，需写回。

### `2605.06040` — Novelty ToT

- **Mechanism / evidence:** novelty judge 以额外 prompts 判断 node 与既有 search tree 的重复/新颖性，换取 branch pruning；作者实验既报告良好配置下大幅 token 节省，也报告错误配置近零 solve rate 和成本上升。
- **Boundary/fallback:** novelty 实质常退化为 duplicate detection，无 solution-quality guarantee；judge 与 proposer 共享盲点。配置不稳时回退 fixed-width/单链搜索、hard budget 与外部 verifier。
- **No Change:** Ch79 已完整表达 ToT 的指数分支、pruning/heuristic/budget/verifier、动态 branching 的校准与“搜索更多不单调可靠”；本论文只提供受限案例，不改变 owner 命题。

### `2605.06052` — XtraMAC

- **Baseline → mechanism/state:** fixed-datatype datapath、upcast 或复制 MAC 会浪费 FPGA DSP。§III～V 将 INT/FP mantissa 归一为共享 integer product，用 datatype-specific sign/exponent/accumulation 与 dynamic packing 实现 cycle-level switching。
- **Evaluation / boundary:** §VI 只绑定 AMD Xilinx U55c、所列 formats/kernels 与 simulation/representative LLM workloads；component density、constant latency 不证明完整 serving goodput 或 GPU/NPU 可迁移。
- **Trade-off / fallback / Books:** 共享 datapath提高利用率，却增加 packing/control、format coverage 与数值验证；不支持的 shape/dtype 回退固定精度 MAC。Ch49 有 execution-plan/mixed-precision 原则，但缺 datatype-adaptive shared-MAC 的硬件 lowering 分支，需写回。

### `2605.06247` — CKT-WAM

- **Baseline → mechanism/state:** output imitation/dense hidden matching 假设 teacher/student interface 同构且更新成本高。§3 从 teacher intermediate states 以 learnable-query cross-attention 压缩，再经 always-on adapter、router、sparse specialized adapters 注入 student text conditioning；backbones frozen。
- **Evaluation / boundary:** §4～5 只覆盖 LIBERO-Plus、四个 real tasks 与作者 WAM/backbone；1.17% trainable parameters 和 success rate 不证明开放环境、跨架构语义对齐或 physical safety。
- **Trade-off / fallback / Books:** compact context减少改动，却引入压缩丢失、router collapse、teacher bias与latent interface mismatch；失败时回退 output distillation/full tuning或独立模型。Ch25 未有 heterogeneous WAM contextual interface，需写回；Ch30 handoff adapter placement/PEFT。

### `2605.06376` — CDM

- **Baseline → mechanism/state:** few-step DMD 在固定离散 anchors 上匹配，reverse-KL mode seeking/trajectory truncation 易丢细节，常依赖 GAN/reward auxiliary。§3 用随机长度 continuous schedule 与 student-velocity off-trajectory alignment 修正 truncation drift。
- **Evaluation / boundary:** §4 与 appendices 只覆盖 SD3-Medium、Longcat-Image、作者 metrics 与 few-step settings；不证明 continuous supervision 对其他 modalities/backbones 或 production latency普遍占优。
- **Trade-off / fallback / Books:** 去掉辅助模块换来更复杂 trajectory sampling/velocity estimation；off-trajectory state 错误会放大。Ch24 缺 discrete-anchor → continuous/off-trajectory 的 distillation 演进，需写回；训练不稳时回退 discrete DMD/consistency或更多 steps。

### `2605.06480` — Patch-effect Graph Kernels

- **Baseline → mechanism/state:** 大量 activation patches 是不可比较的 raw tensor。§3 将 component interventions 变成 direct-influence/partial-correlation/co-influence graph，再用 kernels 比较 slice；graph builder 只拥有 compression/diagnostic artifact。
- **Evaluation / boundary:** §4～5 在 GPT-2 Small、IOI/induction/GT 与 DistilGPT-2 pilot 中比较 graph、prompt-only、raw tensor、learned encoder；§6 明确不是 task-general causal-circuit proof，full DI 仍有 `O(|V|²)` cost。
- **Trade-off / fallback / Books:** 图提高结构可读性却引入 edge-definition、screening bias 与 compression loss；必须保留 raw/surface controls 和 paired patching。Ch66 尚缺 interpretability artifact 的 evidence hierarchy，需写回。

### `2605.06583` — Deterministic Adjoint Matching

- **Baseline → mechanism/state:** flow-model preference tuning 常用 full-trajectory quadratic/KL control。§3～4 把 pretrained velocity field 视为 base dynamics、trainable delta 视为 control，以 terminal reward adjoint产生 matching target；truncation只反传 reward-relevant terminal segment，并允许非二次 regularizer。
- **Evaluation / boundary:** §5、Appendix D 只覆盖 SiT-XL/2、FLUX.2-Klein-4B 与作者 metrics；terminal concentration、deterministic dynamics 与最佳 truncation尚非通用，未覆盖 stochastic control/video/discrete diffusion。
- **Trade-off / fallback / Books:** 省 trajectory compute、保 diversity，却可能遗漏早期 credit、依赖 VJP/base model 和 truncation calibration；不稳时回退 full adjoint、普通 reward/KL fine-tuning。Ch31 缺 flow velocity-field optimal-control 分支，需写回。

### `2605.06601` — Patch2Vuln

- **Baseline → mechanism/state:** end-answer security Agent 会把 diff/ranker/context/reasoning/validation failure 混在一起。§4 将 ELF extraction、binary diff、function ranking、dossier export、offline reasoning 与 bounded validation做成 resumable typed stages，各阶段保存 failure receipt。
- **Evaluation / boundary:** §5～6、Appendix E 仅有 25 个 Ubuntu `.deb` pairs；10/20 localization、11/20 root-cause 与两个 behavior differential，不含 crash/exploit proof。六项先败于 diff/ranker、一项败于 context export。
- **Trade-off / fallback / Books:** 分段归因提高可恢复性却增加工具链、oracle annotation 与敏感 artifact；证据不足保持 unknown，回退人工 reverse engineering。Ch81 有 durable workflow 与 Ch72 有 security trace，但没有 binary-patch pipeline 的 pre-model failure ownership，需写回 Ch81、handoff Ch72。

### `2605.06667` — ActCam

- **Baseline → mechanism/state:** pose-only control不能同时约束 viewpoint，持续 depth guidance又会过约束细节。§3 构造 target-camera-aligned pose/depth，并在同一 denoising run 早期用 pose+depth锁 global geometry、后期仅 pose 恢复 high-frequency motion。
- **Evaluation / boundary:** §4 只覆盖固定 backbone、公开/作者 camera-motion benchmarks、human preference 与 ablation；depth/pose estimation、occlusion、多角色和真实 3D consistency 未获得保证。
- **Trade-off / fallback / Books:** staged condition减少 static/dynamic interference，却依赖 calibration、depth alignment 与 schedule；失败时回退 pose-only、固定 camera或训练式 controller。Ch24 尚缺 condition ownership 随 denoising phase 转移的分支，需写回。

## Root handoff 与 Gate

- 精确写回队列：`ROOT_BOOKS_WRITEBACK_QUEUE_EIGHTEEN_FALSE_NEGATIVES_20260915.json`，15 项。
- 三项 No Change 已对读 owner 主正文，不依赖 Review notes：`2605.05386`、`2605.05495`、`2605.06040`。
- 十二项上一轮实际已写回的 item-level disposition 已与 Books 事实同步为 Applied。
- 作者检查在 root 写回与新的 non-author post-write review 前停止。`final_independent_signoff = false`。
