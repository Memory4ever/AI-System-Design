# 2026-06-04 / 05 / 08 / 09 V3 strict final fresh audit

审计日期：2026-09-10（Asia/Shanghai）

## 结论先行

本次是非作者、fresh-context 语义复核。判断依据是 title + canonical abstract；只有边界项才回看 archive 中的 exact-v1 Method / Evaluation / Limitations。旧 `Candidate`、`Integrate`、Books trace、marker 与 ROADMAP 可映射性均不作为准入证据。

四天当前 V3 分母都不能直接作为最终 authority：06-04、06-05、06-08、06-09 分别有 8、8、5、12 个 strict-retained false positive；06-05、06-08、06-09 分别有 3、3、2 个 strict-demoted false negative。06-09 另有一组两进两出的 identity 错位。纠偏后的 Candidate 为 `65 / 71 / 48 / 115`，合计 299。

旧 archive 的 63 项 `Integrate` 中，59 项在当前 Books 的 `Review notes` 前已有等价机制，应改判 `Existing Coverage`，不是新的正文写入授权；4 项应撤销采用链。真正仍需合并的正文 proposal 为 0 组，正文缺口为 0 组。

| 日期 | V3 Candidate | retained de-admit | demoted restore | identity 修正 | 最终 Candidate | 旧 Integrate → Existing | 撤销采用链 | 正文缺口 | Gate |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: | --- |
| 06-04 | 73 | 8 | 0 | — | 65 | 3 | 0 | 0 | Reopen |
| 06-05 | 76 | 8 | 3 | — | 71 | 8 | 0 | 0 | Reopen |
| 06-08 | 50 | 5 | 3 | — | 48 | 10 | 3 | 0 | Reopen |
| 06-09 | 125 | 12 | 2 | `-06529/-06545; +09711/+09809` | 115 | 38 | 1 | 0 | Reopen |

## Authority 与覆盖口径

逐日读取并交叉核对：

- `papers/2026/06/{04,05,08,09}/README.md`；
- `papers/2026/06/_sources/daily-202606{04,05,08,09}/V3_SCREENING_LEDGER.md`；
- 同目录 `V2_1_EVIDENCE_ARCHIVE.md` 与 `V3_RECOVERY_BLOCKERS.md`；
- canonical raw identity gzip packet 与涉及 Books 决策的 exact-v1 evidence；
- `ROADMAP.md`、研究/报告合同，以及所有目标 Books owner 的 `Review notes` 前正文。

下面是完整的 exception ledger。未列为 exception 的逐项结论由以下集合差精确定义，不是抽样外推：

- retained-pass = 当日 V3 `Strict-retained` 全集减去本账本的 identity-error 与 retained de-admit；
- demotion-pass = 当日 V3 strict demotion/Close 全集减去本账本的 restore；
- 因而每个 V3 retained 与 demoted family 都恰好落入 pass、restore、de-admit 或 identity-error 四类之一。

## 06-04

### Retained corrections — 8 de-admit

| ID | 结论 | 题摘所证明的真实边界 |
| --- | --- | --- |
| 2606.04233 | de-admit | robot-only benchmark；大模型/Infra 没有成为被设计的系统对象。 |
| 2606.04460 | de-admit | CyberGym 是网络安全垂直 benchmark/PoC 流程；benchmark 完整不等于形成通用大模型系统合同。 |
| 2606.04507 | de-admit | SCORE 的增量是局部 co-evolution / training recipe；未给独立 runtime、release 或 state owner。 |
| 2606.04536 | de-admit | TMEM 把在线 LoRA 当参数记忆，是局部 adapter/representation 机制；没有跨 workload 的系统接口。 |
| 2606.04660 | de-admit | LifeSide 是数字陪伴场景的长期会话 benchmark，贡献仍由单一应用任务定义。 |
| 2606.04847 | de-admit | MusaCoder 是 GPU kernel generation 的训练 recipe；kernel 任务对象不把训练方法变成 Infra 合同。 |
| 2606.04883 | de-admit | Lean theorem proving 的局部 Agent workload；未形成可迁移的执行或发布机制。 |
| 2606.04970 | de-admit | wearable/procedural assistance 数据与任务 recipe；长期交互对象本身不足以准入。 |

Retained 覆盖：`65 pass + 8 de-admit = 73`。

### Demotion audit

V3 的 137 个 strict demotion 全部维持 Close，restore 为 0。尤其：

- 2606.04197 只在固定 16-agent Naming Game 上观察 topology × memory 的描述性效应；它能提示实验变量，却没有新的控制协议或 owner；
- 2606.04511 的核心是 Forecast projection、selector distillation 与 sparse-attention architecture；CPU–GPU prefetch overlap 是该局部模型机制的实现结果，不能反向把它提升为通用 Infra candidate。

因此最终 Candidate = `73 - 8 = 65`。

### Books decision

旧 3 项 `Integrate` 全部改判 Existing Coverage：

- 2606.04071 → `PLATFORM-SECURITY`，正文“多 Agent Cascade 需要跨 Channel 的 Influence Graph”已形成 message/shared-memory/delegation/tool-result 的传播图、独立 policy authority、误归因 failure 与隔离/降权/阻断边界；
- 2606.04145 → `TRAIN-RLHF`（Evaluation 为相邻 owner），RLHF 的 reward-hacking/独立 reference 与 Evaluation 的预声明停止、淘汰、完整评测 fallback 已覆盖 world-feedback early stopping 的长期机制；
- 2606.04929 → `PLATFORM-SECURITY`，当前有 Review notes 前 semantic-body binding，且相邻正文已把 poisoning 写成 model/data/runtime/release 联合攻击面与回滚边界。

没有新增正文 proposal。

## 06-05

### Retained corrections — 8 de-admit

| ID | 结论 | 题摘所证明的真实边界 |
| --- | --- | --- |
| 2606.05402 | de-admit | ReasoningFlow 是 reasoning-trace annotation / DAG representation 与描述性分析；monitorability 可能性不是控制机制。 |
| 2606.05711 | de-admit | latent communication 文献综述与 taxonomy；没有提出或验证新的长期机制。 |
| 2606.05868 | de-admit | 金融 LLM 的 GQA→MLA 结构转换、蒸馏和 SFT recipe；并发收益绑定该模型与 Ascend 实现。 |
| 2606.05946 | de-admit | 通用 ML/GDPR supply-chain 短综述；不是大模型系统贡献，也没有可执行实现合同。 |
| 2606.06036 | de-admit | MRAgent 是 Cue-Tag-Content graph 上的局部 retrieval/reasoning algorithm；benchmark 收益不足以形成系统 owner。 |
| 2606.06079 | de-admit | SkillComposer 是 create/improve/merge 的训练 recipe；部署模式枚举不等于 runtime contract。 |
| 2606.06087 | de-admit | LatentSkill 是 text-skill→LoRA 的局部表示与 hypernetwork 方法。 |
| 2606.06438 | de-admit | CarbonSim 是通用 CPU hardware-refresh carbon simulator；没有大模型/Infra 特有对象。 |

Retained 覆盖：`68 pass + 8 de-admit = 76`。

### Demotion corrections — 3 restore

| ID | 结论 | 为什么是合同级增量 |
| --- | --- | --- |
| 2606.05558 | Candidate | ADWM 把离线 Agent evaluation 定义为 policy 与 learned world 交替、因果次序保持的 OPE harness；它改变 evaluator/environment state boundary，而非只报告模型分数。 |
| 2606.05559 | Candidate | CLaaS 把部署中经验、replay buffer 与异步训练封装为 service boundary，明确一次性环境样本、更新与保留之间的状态 ownership。 |
| 2606.05828 | Candidate | 本地 preference harness 将统计偏好状态与远端 LLM semantic decision 分权，形成可替换的 control boundary 与 regret-based 验收。 |

其余 `627/630` strict-demoted family 维持 Close。特别是 2606.05606 的 Bayesian rollout allocation 仍是 post-training recipe，2606.05646 的 downstream-impact memory utility 仍是局部 benchmark/optimization signal，不能因出现 budget 或 evaluation 字样恢复。

最终 Candidate = `76 - 8 + 3 = 71`。

### Books decision

旧 8 项全部是 Existing Coverage：

| IDs | canonical owner | Review notes 前等价正文 |
| --- | --- | --- |
| 2606.05304 | `AGENT-MULTI-AGENT` | “Message 不是 State”“Coordination State 必须有显式 Owner 与 Commit Transition”已覆盖 action-state message 的身份、提交、失败与 typed handoff。 |
| 2606.05679 | `PLATFORM-SECURITY` | 数据 value/sink、monotonic authority、跨 channel taint 与 effect-boundary 已覆盖 policy/data-flow enforcement。 |
| 2606.05933 | `INFER-SCHEDULING` | SLO-aware admission、future-state reservation、滑动窗口 hazard、mode-switch failure 与 fixed-policy fallback 已覆盖。 |
| 2606.05951 | `TRAIN-DISTRIBUTED-TRAINING` | “从 Collective Call 到 Kernel 内 Remote Memory”已覆盖 NVSHMEM 式远端访问的 completion/ownership/trade-off。 |
| 2606.06090、2606.06240 | `AGENT-MEMORY` | Persistent Memory 的显式状态操作、bitemporal valid/write time、transaction/rollback 已覆盖。 |
| 2606.06256 | `INFER-KV-CACHE` | head-level exact owner、importance/attention distortion、reuse/eviction 与保守 fallback 已覆盖。 |
| 2606.06453 | `INFER-TENSORRT-LLM`（纠正旧 `INFER-PAGED-ATTENTION` 路由） | “两种稀疏性必须共享地址合同，却不必共享 Kernel”、irregular compute plan 与 verifier 已覆盖；Ch47 只拥有 KV page 管理，不拥有任意 sparse-attention program。 |

没有新增正文 proposal。

## 06-08

### Retained corrections — 5 de-admit

| ID | 结论 | 题摘所证明的真实边界 |
| --- | --- | --- |
| 2606.06818 | de-admit | Terastal 是 heterogeneous accelerator 上的通用 multi-DNN/layer-variant scheduler，并非大模型或大模型 Infra。 |
| 2606.07017 | de-admit | sim-to-real MDP 立场/研究框架绑定机器人迁移，没有可复验的大模型系统机制。 |
| 2606.07119 | de-admit | Three-Ring 是概念分层与宣传式 reference architecture；摘要没有足够实现 authority，不能靠 Structural Candidate 路由准入。 |
| 2606.07190 | de-admit | PUM 是局部 prefix utility scoring/benchmark method；没有独立 execution 或 release owner。 |
| 2606.07412 | de-admit | Socratic-SWE 是局部 self-evolution/training recipe；软件工程对象不自动构成 Agent platform contract。 |

Retained 覆盖：`45 pass + 5 de-admit = 50`。

### Demotion corrections — 3 restore

| ID | 结论 | 为什么是合同级增量 |
| --- | --- | --- |
| 2606.06915 | Candidate | ThinkBooster 除 benchmark 外还给出 OpenAI-compatible proxy、adaptive compute/scorer selection 与 trajectory debugger，形成 inference-time compute 的 service/control surface。 |
| 2606.06991 | Candidate | SVLS 用 frame-driven FSM 与 token pacer 将感知和生成交织为 per-frame runtime state，明确 cadence、预算和同步 failure。 |
| 2606.07054 | Candidate | TRACE 的 Triage–Inspect–Judge loop 持久累计跨 step evidence，改变长程 Agent monitoring 的 observation/aggregation contract。 |

其余 `445/448` strict-demoted family 维持 Close。最终 Candidate = `50 - 5 + 3 = 48`。

### Books decision 与撤销链

旧 13 项中 10 项是 Existing Coverage：

- 2606.06521 → `INFER-TENSORRT-LLM`：量化逐例一致性、分布漂移、format/layout/phase identity 与 correction/fallback 已覆盖；
- 2606.06523 → `AGENT-WORKFLOW`：state machine、deterministic spine、verification/admission authority 与 recovery 已覆盖；
- 2606.06697、2606.07131、2606.07150 → `PLATFORM-SECURITY`：OS effect boundary、skill lifecycle、cross-channel provenance/influence graph 已覆盖；
- 2606.06888 → `TRAIN-PRETRAINING`：当前 Review notes 前有 exact semantic-body binding；
- 2606.06924 → `INFER-SCHEDULING`：routing calibration、capability/value estimate 成本、policy/placement 分权和 conservative pool fallback 已覆盖；
- 2606.07019 → `TRAIN-DISTRIBUTED-TRAINING`：“从静态通信配置到受验证的 Collective Policy”已覆盖；
- 2606.07379、2606.07462 → `PLATFORM-EVALUATION-SYSTEM`：reference artifact、process/environment evolution、trajectory evidence 与 deterministic verifier 已覆盖。

3 项采用链必须清除：

| ID | 当前残留 | 要求 |
| --- | --- | --- |
| 2606.06818 | Ch63 Review notes 前 semantic-body binding + Review notes 后 trace | 删除两处；通用 DNN scheduler 不能留作 Books 正文 authority。 |
| 2606.07067 | Ch72 Review notes 后 trace | V3 已撤回但 trace 仍在，删除。 |
| 2606.07470 | Ch72 Review notes 后 trace | V3 已撤回但 trace 仍在，删除。 |

没有新增正文 proposal。

## 06-09

### Identity authority correction

`canonical-raw-identity-inventory-v2.1.json.gz` 与旧 archive 都把 2606.09711、2606.09809 的 canonical owner 定为 2026-06-09；当前 V3 prior-retain 表却漏掉这两项，并错误纳入 2606.06529、2606.06545。后二者属于更早日期，且不在 06-09 canonical raw inventory。

因此必须先执行集合替换：`-2606.06529 -2606.06545 +2606.09711 +2606.09809`。这一步净计数为 0，但不修正就无法声称逐项 denominator closure。2606.09711、2606.09809 都是有效 Candidate；后者的 Evaluation Cards 也继续进入下述 Books Existing 判断。

### Retained corrections — 12 de-admit

| ID | 结论 | 题摘所证明的真实边界 |
| --- | --- | --- |
| 2606.07624 | de-admit | sequential inference discussion/perspective；只提出统计过程控制方向，没有新 mechanism 或 implementation。 |
| 2606.07937 | de-admit | 多 Agent hallucination cascade 的描述性实验；没有 intervention、control owner 或 release protocol。 |
| 2606.07963 | de-admit | SAE latent feature、activation steering 与 CAFT 是局部表示/训练 defense。 |
| 2606.08317 | de-admit | AI-ready database 的九维 selection framework 与 case study 是通用 architecture taxonomy，不是新的大模型 data-plane mechanism。 |
| 2606.08372 | de-admit | synthetic tabular data reconstruction SoK/benchmark；不是大模型系统对象。 |
| 2606.08625 | de-admit | rubric 演进综述/taxonomy；没有提出新的 evaluator runtime 或 release contract。 |
| 2606.08806 | de-admit | GATF 绑定 autonomous software testing 垂直任务，摘要中的 governance accuracy/风险比例没有给出足以承担通用平台结论的 authority。 |
| 2606.09060 | de-admit | ATTAIN 的 LLM finite-state tool loop服务 CVE version attribution；贡献与验收由该垂直软件安全任务定义。 |
| 2606.09090 | de-admit | Context Rot 是 position/research roadmap，并复用既有文档一致性 checker；没有新 Agent configuration mechanism。 |
| 2606.09537 | de-admit | STEPS 的大模型只是 natural-language parser，实际对象是通用 edge-service potential-game scheduling。 |
| 2606.09659 | de-admit | LCLM 是 encoder-decoder context compression architecture 与大规模 pretraining recipe。 |
| 2606.09730 | de-admit | SearchSwarm 的核心贡献是 harness-generated SFT data 与 30B model training recipe。 |

在修正 owner identity 后，原 retained 集有 `111 pass + 12 de-admit + 2 wrong-owner = 125`；再加入两个缺失 owner family。

### Demotion corrections — 2 restore

| ID | 结论 | 为什么是合同级增量 |
| --- | --- | --- |
| 2606.08615 | Candidate | Streaming Harness 把任意 VLM 接入 per-second response decision、12-hour memory 与 sub-second processing 的可部署 state/control surface；准入理由是 harness contract，不是其 dataset/benchmark。 |
| 2606.08892 | Candidate | Diffuse AI Control 定义 weak trusted score、red-team adversarial search 与 blue-team robust optimization 的分权控制回路，明确 fuzzy-task 长时攻击与 scorer failure。 |

其余 `1,108/1,110` V3 strict-demoted family 维持 Close。特别是：2606.08446 仍是 sparse rollout/training recipe；2606.08486 仍是 Speech-LLM transducer architecture/training recipe；2606.08779 仍是 discrepancy-constrained RL algorithm；2606.08813 是仅在 `N=10,000` 向量上验证的通用 ANN layout，均不因 cost、streaming、contract 或 vector-memory 用语恢复。

最终 Candidate = `(125 - 2 wrong-owner - 12) + 2 missing-owner + 2 demotion-restore = 115`；Close = 1,120。

### Books decision

除已撤回的 2606.09774 外，旧 39 个 Integrate 中其余 38 个全部是 Existing Coverage。按 canonical owner 合并如下：

| canonical owner | Existing IDs | Review notes 前等价机制 |
| --- | --- | --- |
| `AGENT-MEMORY` | 07684 | compact/exact state、persistent operation、visibility/commit/rollback 与 evidence archive。 |
| `PLATFORM-EVALUATION-SYSTEM` | 07783、07822、07834、07874、08200、08960、09809 | RAG stage attribution、activation-oracle calibration、Judge evidence acquisition/authority、benchmark hardening、Evaluation Identity 与 versioned evaluation object。 |
| `AGENT-MULTI-AGENT` | 07790、07805 | topology、Byzantine governance、verification delay、participation graph 与 environment failure 分层。 |
| `PLATFORM-SECURITY` | 07808、07833、07867、07943、08403、08539、09005、09084 | instruction/authority mutation、skill injection、runtime consumption、sandbox/effect boundary、跨 channel influence 与独立 adjudication。 |
| `INFER-KV-CACHE` | 07878 | compaction、lossy draft/full commit、error budget、page format 与 recovery。 |
| `TRAIN-PIPELINE-PARALLEL` | 07881 | 当前 Review notes 前有 exact semantic-body binding。 |
| `PLATFORM-MONITORING` | 07889 | pre-failure sensor identity、hidden-state sensor authority、independent observation path 与 red-team loop。 |
| `INFER-SCHEDULING` | 07923、09613 | semantic predicate/query-plan state、calibrated config search、saturation-aware capacity 与 simulator identity。 |
| `AGENT-WORKFLOW` | 08049、08919 | versioned notebook/DAG、clean reference run、Human-in-the-Loop 与人工容量/分权边界。 |
| `AGENT-PLATFORM` | 08106 | anytime-valid acceptor、self-modification admission 与 recovery proof。 |
| `INFER-DECODE` | 08411 | diffusion block/phase runtime state、cadence、shared-prefix execution 与保守 autoregressive fallback。 |
| `TRAIN-DISTRIBUTED-TRAINING` | 08476 | Context Parallel buffer/communication lifetime、collective policy 与 failure path。 |
| `INFER-PD-DISAGGREGATION` | 08635 | progressive verified KV handoff、transfer cost、partial state 与 full-transfer fallback。 |
| `AGENT-REFLECTION` | 08671 | persistent diagnosis/belief state、intervention value 与 stopping state。 |
| `INFER-GPU-MEMORY` | 08761 | quantized runtime pages、format/layout identity、质量/吞吐 trade-off 与 higher-precision fallback。 |
| `AGENT-RAG` | 08950 | index layout/maintenance、vector dimension、search-vs-update state 与 immutable-generation fallback。 |
| `INFER-PREFILL` | 09441 | Sparse Prefill selection cost、engine contract、block-union reuse 与 dense fallback。 |
| `INFER-KSERVE-TOPOLOGY` | 09643 | fixed model Pod → base-plus-extension / compound graph、desired/runtime state 分权、compatibility/cold-start failure 与 independent deployment fallback。 |
| `INFER-TENSORRT-LLM` | 09682、09686 | generated/checked kernel admission、typed schedule、numeric conformance、逐例一致性与 reference-kernel fallback。 |
| `PLATFORM-TRACE` | 09692 | delegated execution 的 trace authority、promotion 与 evidence identity（当前已有 Review notes 前正文锚点）。 |
| `TRAIN-RLHF` | 09711 | reward-hacking reference、process sensor、policy-shifted red team 与独立 release evidence。 |

这 38 项均不应再以 source-specific Review note 或 trace 声称“待写 Integrate”。正文已经拥有旧边界→新机制→trade-off/failure→共存/fallback 的长期论证。

2606.09774 采用链仍未撤净：Ch81 `Review notes` 前 semantic-body binding 和 `Review notes` 后 trace 都还存在，必须同时删除。其题摘贡献是 scientific-simulator-specific lightweight coding adapter，当前合同已将其 de-admit/延后；通用 Workflow 正文可以保留独立于该来源成立的机制，但不能继续由该 family 作为 authority。

没有新增正文 proposal。

## 撤销采用链总表

| ID | 当前状态 | 完整撤销条件 |
| --- | --- | --- |
| 2606.06818 | 新 de-admit；Ch63 body marker + trace 残留 | 删除两处 marker/来源专属正文与 trace。 |
| 2606.07067 | V3 已 de-admit；Ch72 trace 残留 | 删除 trace。 |
| 2606.07470 | V3 已 de-admit；Ch72 trace 残留 | 删除 trace。 |
| 2606.09774 | V3 已 de-admit；Ch81 body marker + trace 残留 | 删除两处 marker/来源专属正文与 trace。 |

这四项未清前，不能把 Books Gate 或报告 `Complete` 写成通过。

## 06-23～30 旧 post-review B 标签 reconciliation

对 `papers/2026/06/{23,24,25,26,27,28,29,30}/README.md` 进行当前全文检索后，11 个旧 B family 中只有一个拥有当前 strict Daily authority：

| ID | 当前 owner report / row | 结论 |
| --- | --- | --- |
| 2606.22932 | `papers/2026/06/23/README.md:84`；source review heading `:401`；exact-v1 evidence `:405` | 有当前 owner；canonical owner 为 `TRAIN-DISTRIBUTED-TRAINING`，正文锚点“Gradient 不必在 Backward 与 Optimizer 之间完整物化”。 |
| 2606.23589 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.22783 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.22826 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.23112 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.24722 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.27681 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.29066 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.29038 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.28772 | none | 只存在 stale legacy Books block；撤回 B。 |
| 2606.28955 | none | 只存在 stale legacy Books block；撤回 B。 |

这里的 `none` 是“当前 23～30 strict README 没有 owner row”，不是“尚未找到更方便的引用”。因此不能用 legacy trace/marker 自证 current Daily candidate。另行复核的 2606.25453 是 C，当前 23～30 README 也无 owner row。

## 最终 Gate

- Candidate Gate：06-04、05、08、09 全部 **FAIL / Reopen**，必须把最终分母改为 65、71、48、115，并修正逐项 disposition；
- Identity Gate：06-09 **FAIL**，必须完成 `06529/06545 ↔ 09711/09809` owner correction；
- Evidence Gate：本账本不把旧 exact-v1 receipt 自动继承给新增恢复项；8 个 restore 需要按当前报告合同继续 score、owner route 与 Evidence review；
- Books Decision：旧 Integrate 的 fresh 结论是 `Existing Coverage 59 / new Integrate 0 / de-admit adoption chains 4`；
- Books body Gate：正文缺口 0 组，但撤销链未清，故仍 **FAIL**；
- Report Complete：四日均需重开，不能以 validator、旧 blocker 或 trace 代替上述语义修复。

审计未修改 Books、Daily README、archive、blocker、ROADMAP 或 `LEARNING_STATE`。
