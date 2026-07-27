# AI Research Weekly — 2025-W30

> Coverage Window: 2025-07-21～2025-07-27
> Research Mode: Retrospective Backfill
> Accessed: 2026-07-31
> Backfilled: 2026-07-31

## Executive Summary

本周保留 2 项长期证据：Qwen3-Coder、SpecForge。重点是约束、机制、trade-off 与演进，不是发布热度。

## Coverage Window and Limitations

- 按官方发布日期、GitHub Release 或 arXiv v1 归档；后续修订回链首次公开周。
- Scholar、OpenAlex、DBLP 负责 discovery/去重；论文事实回到正文。Crossref 仅交叉检验 metadata。
- 历史回填不创建 Daily；Accessed 统一为 2026-07-31。
- 作者/厂商 benchmark 缺少完整 workload contract 时不外推。

## 1. 模型与研究机构

### Source Coverage

按固定机构顺序扫描国内外模型公司、研究机构与 Hugging Face Blog。

- 保留：Qwen3-Coder（2025-07-22）。

## 2. 论文与学术来源

按 arXiv → Google Scholar → OpenAlex → DBLP 扫描，回到 v1 正文核验。

- 本组无达到保留门槛的候选。

## 3. AI Infra 与工程项目

按 PyTorch → JAX → CUDA → Triton → vLLM → SGLang → Dynamo → TensorRT-LLM → Ray → KServe → Kubeflow → Kubernetes → Hugging Face → DeepSpeed → Megatron-LM → llama.cpp → ONNX Runtime → OpenXLA 扫描。

- 保留：SpecForge（2025-07-25）。

## Candidate Scoring

| Candidate | Technical Novelty | System Impact | Practical Value | Source Reliability | Project Relevance | Longevity | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Qwen3-Coder | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；只沉淀 environment scaling 与 verifiability |
| SpecForge | 4 | 4 | 4 | 4 | 5 | 3 | 24/30 | Must Read；与 W10/W29 形成 training→serving 链 |

### Deep Analysis 1 — Qwen3-Coder

- First Public: 2025-07-22
- Status: Official open-weight model/blog
- Primary Source: https://qwenlm.github.io/blog/qwen3-coder/
- Evolution Relationship: Direct Evolution

#### Why

repo-scale coding agent 的主要训练压力从单次代码补全扩展到长 context、可执行反馈和长时工具交互。

#### Principle and Mechanism

官方材料披露 code-heavy pretraining、execution-driven RL、long-horizon agent RL 与大规模并行环境。

#### Trade-off and Evidence Boundary

可验证测试提供强 reward，但测试覆盖会塑造行为；环境并行提高数据生成吞吐，也引入 sandbox 成本、偏差和 leakage 风险。

#### Connection and Evolution

知识树位置：第 23～25、29、62、74～77 章。Must Read；只沉淀 environment scaling 与 verifiability。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

### Deep Analysis 2 — SpecForge

- First Public: 2025-07-25
- Status: Official open-source framework/blog
- Primary Source: https://www.lmsys.org/blog/2025-07-25-spec-forge/
- Evolution Relationship: Layering / Dependency

#### Why

speculative decoding 的上线瓶颈不只在 runtime 支持，还在 draft model 的训练、评测和目标模型版本对齐。

#### Principle and Mechanism

SpecForge 提供 EAGLE-3 draft-head training、online/offline modes 与 training-time test pipeline，并与 SGLang runtime 对接。

#### Trade-off and Evidence Boundary

端到端工具链降低训练门槛，却新增 target/draft version coupling、数据分布漂移和 benchmark tuning 风险。

#### Connection and Evolution

知识树位置：第 44、47、62 章。Must Read；与 W10/W29 形成 training→serving 链。若进入 Books，将保留旧方案仍成立的条件，并区分官方事实、作者实验和跨来源推断。

## Full Source Review

### Qwen3-Coder-480B-A35B-Instruct

- **Candidate / Week / Score:** Qwen3-Coder / 2025-W30 / 24/30。
- **Source Family ID:** `QWEN3-CODER-2025-07`。
- **Source Type:** official research/release blog、model card/weights、Qwen Code repository。
- **First-public Date / Revision History:** first release 2025-07-22；后续模型尺寸、CLI 与 API变化不回写为初始 release 事实。没有同步发布可阅读全文的 technical report。
- **Direct Primary Sources:** Qwen official Qwen3-Coder blog；Qwen3-Coder-480B-A35B-Instruct model card/config；`QwenLM/qwen-code` release-time documentation。
- **Related Primary Sources:** Qwen3/Qwen2.5-Coder reports用于 architecture/data lineage；SWE-bench harness只用于理解评测对象。
- **Access and Verification Status:** Verified for official disclosures and released artifacts；RL objective、reward implementation、environment scheduler、test generation质量、training hardware与完整 evaluation protocol Not Disclosed。
- **Full-read Coverage:** 已阅读全文的 pretraining、Code RL、long-horizon Agent RL、20,000 environments、Qwen Code/interface与future work；核对 model config/context/template 和 CLI tool protocol。因无 technical report，不能声称已获得 method/ablation/limitations全文。
- **Original Problem:** repo-scale software engineering不是单次补全：模型需在长 context中规划、调用工具、读取执行反馈并跨多轮修正，而可验证环境生成速度成为RL瓶颈。
- **Why the Previous Design Was Reasonable:** code-heavy pretraining+SFT对函数/文件级生成成本低、稳定；competition problem的unit tests提供清晰reward，单轮RL更易扩展。
- **Changed Constraint:** pull request与SWE tasks引入跨文件context、长时交互、环境side effects和delayed credit；训练吞吐受sandbox/environment而非仅GPU forward限制。
- **Mechanism:** 480B-total/35B-active MoE；7.5T pretraining tokens、官方称70% code，native 256K并以YaRN外推至1M；post-training将自动扩展test cases的execution-driven Code RL与multi-turn Agent RL结合，并运行20,000个独立环境。
- **State Ownership:** model/trainer拥有policy/checkpoint；environment service拥有repo snapshot、tool execution与test outcome；reward pipeline把可执行结果映射为训练signal；workflow/runtime仍拥有部署时authorization和side effects。
- **Control Flow / Data Flow:** code/repo/PR corpus → pretraining → generated/validated tests → rollout in isolated repo environment → tool observations/tests → trajectory reward/credit → policy update；发布blog未披露 failure/retry/lease 与污染隔离实现。
- **Implementation Details:** 官方只披露environment parallelism规模、Qwen Code基于Gemini CLI并定制prompt/function-calling protocol；sandbox isolation、resource quota、snapshot cache、scheduler与训练并行 Not Disclosed。
- **Evaluation Setup:** 发布图覆盖agentic coding/browser/tool use与SWE-bench Verified，声称无 test-time scaling；公开页面没有统一列出每项temperature、samples、scaffold版本、max steps、hardware与token budget。
- **Baselines / Ablations / Sensitivity:** 没有公开 20,000 environments 的scaling curve、Code RL vs Agent RL controlled ablation、test coverage sensitivity或leakage audit；cross-model榜单不能分离data/model/harness。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** 480B/35B active、256K native/1M extrapolated、20,000 environments披露；training GPU/precision/global batch、per-env resources、rollout length、online serving concurrency/SLO Not Disclosed。
- **What the Evidence Actually Proves:** 官方artifact与说明证明“environment fleet”已成为coding-agent训练系统的一等资源，并展示hard-to-solve/easy-to-verify任务可用execution feedback扩展。
- **What It Does Not Prove:** 不证明自动tests覆盖真实specification，不证明20,000并发本身提高sample efficiency，不证明SWE-bench结果可泛化到私有repo或不可自动验证工程任务。
- **Limitations / Threats to Validity:** 缺technical report与消融；generated tests可能错误/泄漏/奖励投机；环境镜像与scaffold影响结果；长context外推不等于1M有效利用；作者benchmark未独立复现。
- **Trade-offs / New Failure Modes:** execution reward比model judge更客观但只验证被编码的行为；environment scaling提高rollout吞吐却新增sandbox escape、flaky test、resource contention、snapshot drift与delayed/partial reward。
- **Where the Previous Design Still Applies:** 小函数、静态分析、缺可靠tests或执行风险高时，pretraining/SFT、human review和少量受控environment仍合理；不可逆production action不能用training sandbox成功替代approval。
- **Evolution Relationship:** `Direct Evolution`：code pretraining/SFT → execution-verifiable Code RL → long-horizon Agent RL → environment fleet成为training control plane。
- **ROADMAP Node:** Ch23～25、Ch27～29、Ch62、Ch74～77。
- **Target and Adjacent Chapters Read:** 已阅读 Ch22～30、Ch61～63、Ch73～77；Training负责reward/data contract，Workflow负责deployment side-effect semantics，不能混为一个“Agent能力”。
- **Existing Coverage:** Ch27/29已说明verifiable reward的coverage边界，Ch62已要求harness contract，Ch74/77已区分tool proposal与durable execution。新信号主要是environment fleet scaling，是否进入正文取决于它能否补全training-system resource ownership而不复述产品能力。
- **Integration Decision:** `Weekly Only — Version/Product Fact / Mechanism Partially Disclosed`。
- **Changed Files or Rejection Reason:** 不改 Books；agentic coding benchmark 不反推 workflow runtime。
- **Open Questions:** RL objective/credit assignment、environment scheduler/isolation、test generation audit、data leakage、per-trajectory cost与independent reproduction。

### SpecForge

- **Candidate / Week / Score:** SpecForge / 2025-W30 / 24/30。
- **Source Family ID:** `SPECFORGE-2025`（后续 SpecBundle 另作同族演进事件）。
- **Source Type:** official engineering blog、open-source repository/code、released EAGLE3 draft heads。
- **First-public Date / Revision History:** initial release 2025-07-25；repository当前已包含2025-12与2026方法/拓扑，review以release blog和当时artifact为准，current main只用于识别演进，不能倒投为v0能力。
- **Direct Primary Sources:** LMSYS SpecForge release blog；`sgl-project/SpecForge` 2025 release code/docs；released Llama 4 Scout/Maverick EAGLE3 draft heads。
- **Related Primary Sources:** EAGLE-3 paper/official implementation；SGLang speculative serving path；W10 EAGLE-3与W29 MTP packets。
- **Access and Verification Status:** Verified for 2025 feature/data paths and public experiment; exact release commit、training GPU topology、runtime version与end-to-end reproduction仍不完整。
- **Full-read Coverage:** 已阅读 blog全篇的problem、TTT、online/offline、FSDP/TP、experiments、artifact与roadmap；检查repository的trainer/config/data layout和SGLang handoff。后续DFlash/SpecBundle/current disaggregated topology不计入2025能力。
- **Original Problem:** speculative serving已有draft/verify算法，但高质量draft model训练缺少可维护、与目标runtime兼容且能承载大MoE target的公共pipeline。
- **Why the Previous Design Was Reasonable:** 手工/offline precompute hidden states使draft训练可在少量GPU上独立重复；研究代码针对单一model时更容易保持算法清晰。
- **Changed Constraint:** Llama 4等大target的hidden state体积、EAGLE3 recursive TTT mask、MoE与SGLang artifact contract使“训练一次再手工移植”代价过高。
- **Mechanism:** EAGLE3 draft head以target hidden features训练并用Training-Time Test模拟多步draft；online mode训练时即时运行target、低disk但需要更多GPU，offline mode预计算并复用hidden states、target不驻留训练期、可低至1 GPU但示例数据约12TB。
- **State Ownership:** immutable target model/version拥有teacher distribution；producer/preprocess拥有hidden-state artifact；draft trainer拥有draft checkpoint；serving runtime拥有compatibility/parser与acceptance telemetry；每项必须绑定版本与data provenance。
- **Control Flow / Data Flow:** raw conversations → target hidden-state production（online或offline）→ EAGLE3 TTT/recursive draft training → training-time test → draft artifact → SGLang load/verify benchmark → acceptance/performance feedback。
- **Implementation Details:** 2025 blog公开FSDP与tensor parallel、modular target/draft registration；TTT依赖special attention masks与recursive data loops。current repo已扩展typed topology，不能作为初始release的既有实现。
- **Evaluation Setup:** 320K ShareGPT+UltraChat samples，Llama 4 Scout/Maverick draft heads，MT-Bench；`speculative-eagle-topk=8`、`speculative-num-draft-tokens=10`并sweep steps，作者报告2.0×/2.18× speedup。
- **Baselines / Ablations / Sensitivity:** sweep draft steps；没有完整报告训练GPU/时长/precision、target-only绝对latency、concurrency/length/SLO、online-vs-offline quality/cost或跨domain acceptance。
- **Hardware / Model / Precision / Length / Batch / Concurrency / SLO:** model/data size与draft flags披露；GPU型号/数量、precision、batch、MT-Bench length/concurrency、TTFT/TPOT/SLO Not Disclosed，因此2.0×/2.18×不能外推。
- **What the Evidence Actually Proves:** 证明draft training是独立artifact lifecycle，且online/offline是在GPU与storage/reproducibility之间搬移成本；公开draft heads与代码提供可检查实现入口。
- **What It Does Not Prove:** 不证明“训练完即可无适配上线”对任意target/runtime版本成立，不证明MT-Bench speedup代表production workload，也不证明roadmap中的Kimi/Qwen/VLM支持当时已实现。
- **Limitations / Threats to Validity:** 作者自评、workload contract不完整；offline hidden states可随target/tokenizer/kernel变化而stale；online target提高资源耦合；训练data与deployment traffic分布漂移会降低acceptance。
- **Trade-offs / New Failure Modes:** online节省disk且随target同步，却增加GPU、target availability与failure coupling；offline便于复用/少GPU却新增大artifact、schema/version drift、storage integrity与重算成本。
- **Where the Previous Design Still Applies:** 小target、一次性实验或已有稳定hidden-state pipeline时，简单offline脚本仍合理；acceptance不足或draft维护成本大于saved target iterations时，标准decode更好。
- **Evolution Relationship:** `Layering / Dependency`：EAGLE-3 method → SpecForge training/artifact lifecycle → SGLang serving；后续SpecBundle是curated artifact distribution，不覆盖这条训练路径。
- **ROADMAP Node:** Ch31、Ch44、Ch47、Ch62。
- **Target and Adjacent Chapters Read:** 已阅读 Ch30～32、Ch43～48、Ch61～63；Ch44 已按本 packet 核对 online/offline 与版本耦合。
- **Existing Coverage:** Ch44已拥有draft artifact lifecycle和online/offline trade-off；Ch31覆盖checkpoint/version identity，Ch62覆盖evaluation。Books Gate应去除任何把roadmap写成实现或把2.18×写成通用收益的句子。
- **Integration Decision:** `Refine — Existing Argument`；主 owner Ch44，draft training 成为独立 artifact pipeline。
- **Changed Files or Rejection Reason:** 已复核 `books/part-04-inference-system/44-speculative-decoding.md`。
- **Open Questions:** 2025 exact commit、hardware/training cost、online/offline quality parity、target升级兼容/rollback与不同traffic分布下acceptance。

## Evidence Level

- Official facts 只覆盖公开接口、版本、权重和文档。
- arXiv / technical report 为作者实验，默认 Experimental，未等同独立复现。
- 跨来源演进关系是本项目推断，已显式标注。

## Cross-Week Deduplication

- release、paper v1 与后续集成若日期不同，分别记录证据角色，但只建立一个 Books source packet。
- 新方案不静默覆盖旧方案；记录新增状态、成本和 failure modes。

## Knowledge Tree Position

- Qwen3-Coder → 第 23～25、29、62、74～77 章（Direct Evolution）
- SpecForge → 第 44、47、62 章（Layering / Dependency）

## Recommended Action

- Qwen3-Coder：Must Read；只沉淀 environment scaling 与 verifiability
- SpecForge：Must Read；与 W10/W29 形成 training→serving 链

## Event-Date Daily Decision

历史回填不创建 Daily；证据保留在本 Weekly。

## Books Integration Decision

Books Gate 已完成。该周候选的最终 disposition 已写入各自 Full Source Review；没有评分候选的周保持 No Material Update，不为制造 diff 修改 Books。


## Ignored Noise

- 忽略转载、旧内容重发、无 primary evidence 的榜单与缺条件 benchmark。
- API alias/价格变化若不形成机制，只作为版本治理信号。

## Repository Changes

- 新增 papers/2025/weekly/2025-W30/README.md。
- 本周候选已完成最终 Books disposition；实际章节修改或拒绝理由见各候选的 `Changed Files or Rejection Reason`。

## Open Questions

- execution-driven RL 的测试覆盖、sandbox bias 与 leakage 风险仍不能由发布 benchmark 排除。
- online/offline draft training 的数据漂移、回滚和 target compatibility 仍需生产证据。

## Sources

- Qwen3-Coder — https://qwenlm.github.io/blog/qwen3-coder/（First Public: 2025-07-22；Accessed: 2026-07-31）
- SpecForge — https://www.lmsys.org/blog/2025-07-25-spec-forge/（First Public: 2025-07-25；Accessed: 2026-07-31）
- SpecForge repository — https://github.com/sgl-project/SpecForge（2025 release artifact；Accessed: 2026-07-31）
