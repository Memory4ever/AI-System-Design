# Daily Research — 2026-06-10

**规范：** V3
**窗口：** 2026-06-09T09:00:00+08:00 ～ 2026-06-10T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-01T10:02:46+08:00

## 1. 结论

本轮确定落窗的候选为2个唯一发布家族：Kimi Code 0.12.0/0.12.1的goal重放/暂停和限流批次执行约束，6分、重要发布深入必要范围；MaxProof的policy可利用verifier误差边界，6分标准审阅、窄已有覆盖经root独立核。Kimi已在Ch81:1158/1160、Ch82:184/186各整合两段，root必要源→actual owner/literal及实际写后均PASS；本轮为1家族实际整合、1家族窄已有覆盖。root最终非作者安全终态日Gate通过，普通待办0；日期与历史来源外部限制继续精确隔离，不是52篇Evidence通过。

旧54行实际为52个arXiv身份加两个发布家族；52个arXiv的旧08–09公开范围依赖DataCite Created/正常schedule，不能证明公开上界，全部终态日期保留，不计本轮正面候选或Evidence/Books通过。旧49E/5I与685宽身份的逐项标签不继承，有效研究及既有正文保留于[唯一packet的legacy区](../_sources/daily-20260610/V3_RECOVERY_BLOCKERS.md#旧完整报告非本轮验收)。本轮不将宽发现清单变成全文队列，不称无遗漏。

## 2. 来源覆盖

本轮2026-10-01逐源独立读取下列有限入口，停止位置不是全站历史覆盖。详情及必要源在[唯一packet](../_sources/daily-20260610/V3_RECOVERY_BLOCKERS.md)。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 原RSS实返1240项，按UTC[06/09 01,06/10 01)取LSEG/Nextdoor/Notion三事件；实际核心分别54–122/39–59/33–60，见packet具体关闭 | 已检查 | 初次403后有限UA替代成功；只覆盖该RSS及三原文，不断言全Research历史 |
| SRC-ANTHROPIC | Research可读58行、raw HTML316846bytes提取173个publishedOn；邻接06/08 13:20Z→06/16 11:00Z，无Jun09/10字段 | 已检查 | 仅当前索引字段，不证明失收历史项不存在 |
| SRC-GOOGLE-AI | DeepMind curated309行；GenAI/NLP/MachineIntelligence各首12条，分别06/24→06/03、06/24→06/05、未达目标；官方June09/10主题查询空，翻页javascript失败后停止 | 受阻 | curated/12条标签页不能证明目标批次完整；需当窗原始发布批次或可访问主题分页 |
| SRC-META-AI | publication目录444行，2026前缀06/29→06/05 SIRA→05/27/26，随后进入旧年；停止2026前缀 | 已检查 | 目录无当窗条目不等于所有论文首公开日期已证 |
| SRC-QWEN | research API60条最新2025-12-23、news17条最新2025-04-28；官方Jun09主题补检空 | 受阻 | 2026目标历史目录未恢复，不能零材料/全覆盖 |
| SRC-DEEPSEEK | 当前News39行：模型09/10→04/24，Research06/24→02/25，无目标日期；停止可见列表 | 已检查 | 查看更多/不可恢复历史批次不作无遗漏 |
| SRC-MOONSHOT | PlatformBlog109行可见27条止2025-11；release API81项，两0.12事件原published_at落窗，必要552/555/424及584精确patch | 已检查 | Blog历史切片缺口；只核本次必要patch，不称全release安全/测试复现 |
| SRC-TENCENT-HUNYUAN | publicList POST pageNum1/pageSize100/renderType0，code0,totalNum9/list9；publicAt从07/06跳04/30，九项原public/display/published字段分别检查 | 已检查 | display不替代publicAt，链接论文first-public另需证明；不推广为机构所有历史 |
| SRC-ZAI | Research175行首14项；08/26→08/14→06/16→05/20，停止越过本窗 | 已检查 | 当前Research目录限定，不称GitHub全部artifact覆盖 |
| SRC-BYTEDANCE-SEED | public_papers page1/13、首20/242；06/11范围外科学→06/04→06/03 MetaPoint→05/29，停止越过本窗，不读242全文 | 已检查 | calendar目录非精确论文首公开时钟 |
| SRC-BAIDU-ERNIE | 技术博客68行page1/2，首10最新05/09→04/30，已越目标；不扩旧页 | 已检查 | 当前博客列表，不代表未收录历史技术报告不存在 |
| SRC-XIAOMI-MIMO | homepage338行，Paper8（06/29→03/13）、Blog15无日期；有限official Jun09/10搜索仅返回06/08 UltraSpeed原页 | 受阻 | 原页June8 calendar与June9 trial start不证明新论文/机制在本窗首次公开；需带时区发布字段/目标历史批次，不继承邻日DateHold |
| SRC-MINIMAX | 英文blog76行，06/09 MaxProof→06/01→05/27；中文重定向minimax.cn/blog68行仅壳、AgentTech15行仅导航；MaxProof原HTML JSON-LD与core67–259实读 | 已检查 | 中文/AgentTech历史目录缺口隔离；MaxProof采用仅窄命题 |
| SRC-ARXIV | exact10794v1 history仅Submitted；正确2026-06 cs.CL首25/2718无daily headers；短260610404；advanced123行明确announcement仅年月；两个官方ID/date查询空，保旧inventory作身份材料 | 受阻 | 项目主题CL/LG/AI/DC及CV/RO/AR/PL/OS/PF/IR/MA的当窗原始公开批次未恢复，不能以cs.CL代表全项目；52具名DateHold及分类历史覆盖缺口隔离，不将提交/Created/Updated补造上界 |

## 3. 候选与判断

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Kimi Code 0.12.0 / 0.12.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.12.0) | 2026-06-09T11:56:11+08:00 | goal journal重建与恢复执行权降级、ready-weighted限流/同agent重试/部分结果Join，2+2+2=6；两个release在同一家族处理，后事件17:04:14见§4 | 深入完成 | 整合：`AGENT-WORKFLOW`—[Ch81](../../../../books/part-07-agent/81-workflow.md) Resume末1158/1160与`AGENT-MULTI-AGENT`—[Ch82](../../../../books/part-07-agent/82-multi-agent.md) bounded fan-out后184/186；实际两段各已写、root独立pre与写后PASS |
| [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution) | 2026-06-09T21:43:00+08:00 | 平均accuracy不规定policy可利用false positive、训练reward不可自签独立验收；2+2+2=6 | 标准完成 | 已有覆盖：`TRAIN-GRPO`—[Ch33](../../../../books/part-04-training-system/33-grpo.md) verifier-spec、相关误差/可利用路径及更新权威；root窄PASS，不覆盖完整min/进化配方 |

## 4. 证据与知识整合

### [Kimi Code 0.12.0 / 0.12.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.12.0)

官方release API81条中两精确record ID336356016/336468037，published_at分别03:56:11Z/09:04:14Z，draft/prerelease均false；created_at不是日期依据。552=`db82e33a20fd1ec204672df4ba5bc38800ce8dea`实际agent/records把goal create/update/clear/fork接入重放；goal normalize清旧wall-clock anchor、active降paused需显式resume、complete残留清除，取代metadata当goal事实来源。555=`41ebe9fb9f403e2ee6a8721640a79faa64e9210a`把runtime错误pause与语义blocked分账，并仅一次、受step预算限制的outcome continuation；生成消息不是成功verifier。旧Ch81 Resume/effect ledger与0.9暂态/lazy child并无这一goal projection差额，已依窄锁写两段而不覆写旧机制。

424=`72c4b0adaa6ae0466875cd8e4066c42456195f21`实际subagent-batch：正常5项初始+700ms ramp不以active硬封顶；429后容量从ready数量初始化并收缩，同agent retry优先、3/6/12秒等待、3分钟无新限流才探测增容；结果按输入槽保留，并区分已启动/未启动abort和可resume身份。单task timeout与整batch取消不同，剩余唯一task仍限流可终态failed。审批policy仅Swarm mode里的AgentSwarm工具，不放行全部child tool。未证明最优配额、持久queue、crash exactly-once、副作用回滚或生产SLO。现Ch82一般预算/fanout未具体承载这些分账，已依窄锁写两段；literal与精确seam见[packet](../_sources/daily-20260610/V3_RECOVERY_BLOCKERS.md#kimi-012必要实现与实际-owner-差额本轮已窄写并通过写后)。root实际亲读Ch81:1158/1160、Ch82:184/186及两侧，写后PASS并释放两锁。

0.12.1的584=`11bb62c12f38d380a0ca1bb89ee2df67f93300e1`仅必要兼容性：config/schema移除unknown experimental ID的拒绝校验，仍string→boolean record；tests显示obsolete id忽略而registry已知项/环境优先性仍区分。测试文本不是本轮执行结果。xhigh修补只记录release事实，不采用未知推理质量命题，不扩全release附件。

### [MaxProof](https://www.minimax.io/blog/minimax-maxproof-math-proof-evolution)

原HTML159743bytes，JSON-LD datePublished/dateModified均13:43:00Z；core67–259已读。三expert闭环及三个配置judge取min、低组内std过滤、再修复筛选和evolutionary TTS是厂商披露的配方；M2既有失败实验不是M3受控消融，同一judging体系反复筛选也不产生独立oracle。完整model/prompt/hardware/训练和搜索成本细项未披露，不外推到通用RL/生产Agent，未复现实验。

只采用平均准确率与policy可利用FP必须分账、训练reward不能自签验收；实际Ch33:476–549 verifier specification、组内相关误差/visitation利用路径和更新权威已具体承载。root独立读VerifierDesign88–128/Reward-hacking147–158及actual owner窄PASS。不是完整min聚合/进化搜索recipe的E，更不是math领域任务进入AI-for-Science；无新增Books。

## 5. 缺口与下一步

普通可执行待办0。原文阅读、14有限source stop、Kimi两owner实际窄写与root写后、最终非作者日级Gate均已收口。以下均为本窗终态保留项，不支持正面证据、Books或无遗漏断言；各项缺失材料、必要性与定点重开条件列在对应段：

52个旧arXiv身份均缺首次公开上界。35item owner receipt实际27scheduleMatchesyes/8no，Created登记/正常最早schedule不证明公开；Updated也非公共可见上界。source-review-receipts与source README/AccessStatus为0bytes，不能继承完成。可接受替代为官方带day header的原始New公告、公告存档或作者/出版方带时区的first-public字段，且范围完全落窗；材料到达只重开对应ID的日期及其准入/采用链，不重审685。旧5I正文保留，但不计本轮I，不能据本日旧采用段反证日期已核。

| 材料身份（同一材料仅此一份日期请求） | 本轮终态 |
| --- | --- |
| [From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents](https://arxiv.org/abs/2606.09863v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Alignment Collapse Under KV Cache Quantization: Diagnosis and Mitigation](https://arxiv.org/abs/2606.09864v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [IntentKV: Cross-Turn Intent-Aware KV Cache Pruning for Agent Inference](https://arxiv.org/abs/2606.09916v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [RKSC: Reasoning-Aware KV Cache Sharing and Confident Early Exit for Multi-Step LLM Inference](https://arxiv.org/abs/2606.09937v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [RATrain: A Resource-Aware Training Runtime for Large Language Models on Bandwidth-Constrained Heterogeneous Supercomputing Platforms](https://arxiv.org/abs/2606.10415v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [ASTRA-sim 3.0: Next-Level Distributed Machine Learning Simulations via High-Fidelity GPU and Infrastructure Modeling](https://arxiv.org/abs/2606.10440v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [SpenseGPT: Practical One-shot Pruning Enabling Sparse and Dense GEMMs for LLM Inference](https://arxiv.org/abs/2606.10445v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/abs/2606.10493v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Prefilling-dLLM: Predictive Prefilling for Long-Context Inference in Diffusion Language Models](https://arxiv.org/abs/2606.10537v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Unifying Local Communications and Local Updates for LLM Pretraining](https://arxiv.org/abs/2606.11081v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic Reinforcement Learning](https://arxiv.org/abs/2606.11119v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [OpenPCC: Open and Confidential LLM Serving on Commodity TEEs](https://arxiv.org/abs/2606.11145v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [ReasonAlloc: Hierarchical Decoding-Time KV Cache Budget Allocation for Reasoning Models](https://arxiv.org/abs/2606.11164v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Piper: A Programmable Distributed Training System](https://arxiv.org/abs/2606.11169v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability](https://arxiv.org/abs/2606.09936v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Right Family, Wrong Skill: Benchmarking Risk Exposure in Agent Skill Retrieval](https://arxiv.org/abs/2606.10388v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [STAGE-Claw: Automated State-based Agent Benchmarking for Realistic Scenarios](https://arxiv.org/abs/2606.10394v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Trace2Policy: From Expert Behavior Traces to Self-Evolving Decision Agents](https://arxiv.org/abs/2606.10457v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Learning What to Remember: Observability-Safe Memory Retention via Constrained Optimization for Long-Horizon Language Agents](https://arxiv.org/abs/2606.10616v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Decentralized Multi-Agent Systems with Shared Context](https://arxiv.org/abs/2606.10662v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [RedAct: Redacting Agent Capability Traces for Procedural Skill Protection](https://arxiv.org/abs/2606.10813v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Provenance Tracking in AI Compilers through the Lens of Coalgebra](https://arxiv.org/abs/2606.10937v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Provenance-Grounded Gating and Adaptive Recovery in Synthetic Post-Training Data Curation](https://arxiv.org/abs/2606.11127v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [When RL Fails after SFT: Rejuvenating Model Plasticity for Robust SFT-to-RL Handoff](https://arxiv.org/abs/2606.09932v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [GitInject: Real-World Prompt Injection Attacks in AI-Powered CI/CD Pipelines](https://arxiv.org/abs/2606.09935v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Stop Early, Spend Less: Hidden-State Probes as a Practical Recipe for Streaming Moderation of LLM Outputs](https://arxiv.org/abs/2606.10487v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Fingerprinting All AI Cluster I/O Without Mutually Trusted Processors](https://arxiv.org/abs/2606.10724v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents](https://arxiv.org/abs/2606.10742v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Recalling Too Well: Sycophancy Evaluation and Mitigation in Memory-Augmented Models](https://arxiv.org/abs/2606.10949v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [CIAware-Bench: Benchmarking Control Intervention Awareness Across Frontier LLMs](https://arxiv.org/abs/2606.11063v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Operator Fusion for LLM Inference on the Tensix Architecture](https://arxiv.org/abs/2606.09879v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [WebChallenger: A Reliable and Efficient Generalist Web Agent](https://arxiv.org/abs/2606.10423v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Streaming Knowledge Compilation: Proactive Materiality-Scored Pinning for Time-Evolving LLM Wikis](https://arxiv.org/abs/2606.09877v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Less Context, More Accuracy: A Bi-Temporal Memory Engine for LLM Agents Where a Lean Retrieved Context Beats the Full History](https://arxiv.org/abs/2606.09900v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [ActiveMem: Distributed Active Memory for Long-Horizon LLM Reasoning](https://arxiv.org/abs/2606.10532v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [SkillAxe: Sharpening LLM-Authored Agent Skills Through Evaluation-Guided Self-Refinement](https://arxiv.org/abs/2606.10546v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Infini Memory: Maintainable Topic Documents for Long-Term LLM Agent Memory](https://arxiv.org/abs/2606.10677v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [REAL: A Reasoning-Enhanced Graph Framework for Long-Term Memory Management of LLMs](https://arxiv.org/abs/2606.10694v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [The Arbiter Agent: Continually Monitoring Multi-Agent Conversations to Detect Emergent Misalignment](https://arxiv.org/abs/2606.10747v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [READER: Robust Evidence-based Authorship Decoding via Extracted Representations](https://arxiv.org/abs/2606.10794v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [CollabSkill: Evaluating Human-Agent Collaboration On Real-World Tasks](https://arxiv.org/abs/2606.09833v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [FailureScope: Cross-Regime Behavioral Diagnosis of Language Model Weaknesses](https://arxiv.org/abs/2606.09878v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [PreAct-Bench: Benchmarking Predictive Monitoring in LLMs](https://arxiv.org/abs/2606.09890v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [IDP-Bench: Benchmarking ability of LLMs to protect personal information in interdependent privacy contexts](https://arxiv.org/abs/2606.09908v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Quality Is Not a Safety Proxy Under Quantization](https://arxiv.org/abs/2606.10154v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Catching One in Five: LLM-as-Judge Blind Spots in Production Multi-Turn Transaction Agents](https://arxiv.org/abs/2606.10315v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [AgentCanary: A Security Evaluation Framework for Autonomous AI Agents in Real Executable Environments](https://arxiv.org/abs/2606.10484v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Assessing Automated Prompt Injection Attacks in Agentic Environments](https://arxiv.org/abs/2606.10525v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [When the Defense Writes the Refusal: Auditing Keyword-Scored Evaluation of Inference-Time Defenses for Multimodal Large Language Models](https://arxiv.org/abs/2606.10904v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [VISTA: A Versatile Interactive User Simulation Toolkit for Agent Evaluation](https://arxiv.org/abs/2606.11079v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [The Interlocutor Effect: Why LLMs Leak More Personal Data to Agents Than Humans](https://arxiv.org/abs/2606.09844v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |
| [Deployment-Time Memorization in Foundation-Model Agents](https://arxiv.org/abs/2606.10062v1) | Date Hold；首公开上界未核，不计当窗候选/本轮Evidence或Books采用 |

来源外部限制按五组去重：arXiv当窗原始分类公告缺口（上述52共享同一恢复条件）；Google curated/标签分页目标历史批次；Qwen2026历史索引；Moonshot Blog与MiMo dated历史事件页（release单独已闭合，trial开始不替代first-public）；MiniMax中文/AgentTech导航壳。恢复需相应目标窗原始列表/官方发布字段，不以同接口反复重试、全篇论文或邻日完成声明替代。本次没有新增窗外候选待办；旧目录线索不移归本日。

## 6. 复核

复核者：root（非报告作者）
结论：通过

root最终安全终态日Gate实际范围：本轮14源有限停止对照当前清单，52具名唯一DateHold及五组历史限制全部隔离；不是52全文、全部原始来源无遗漏或旧5I重新验收。两个全正侧必要source→actual owner通过：MaxProof官网VerifierDesign/Reward-hacking→Ch33仅窄E，Kimi552/555/424实际API→两owner/literal及Ch81:1158/1160、Ch82:184/186两侧写后通过。root另直接API核81 release、两published_at/flags和584 schema保string:boolean仅移unknown拒绝；不扩全release正确性、安全/SLO或测试复现。直接独立核三个OpenAI核心：客户adoption没有公开新机制/可比counter，前分母关闭成立。日期语义、风险采用限制与现有正文/legacy保留相容；普通待办0，无新日期扫描或Books队列。

当前完成态V3格式/一致性与四文件限定diffcheck实际PASS，仅证明机械一致性，语义依据上述非作者实际范围。未stage、commit或push。
