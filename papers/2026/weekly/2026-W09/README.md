# AI Research Weekly — 2026-W09

> Coverage Window: 2026-02-23～2026-03-01
> Research Mode: Retrospective Backfill
> Accessed / Backfilled: 2026-07-31；Discovery Reopened: 2026-08-08
> Re-audit Status: Source-Family Books Gate Complete — 62/62 final dispositions reviewed: 52 Refine, 6 No Change, 4 Weekly Only; 58 Full Source Reviews and 4 low-score source/rejection checks complete; 3 cross-index records excluded after first-public correction to 2024-09-22、2025-09-23 and 2025-12-16; Archive Completion Gate remains Open because Google Scholar/OpenAlex historical discovery coverage is not independently closed

## Executive Summary

旧版只保留 Anthropic persona selection 与 OpenAI malicious-use report，两项不足以代表本周
研究面。初轮按事件首次公开日期恢复到 33 项；随后检查 03-02/03 的 discovery-lag spillover，
又找回 15 项 first-public date 属于本周的候选，总账扩为 48 项，覆盖
Agent orchestration、安全与可执行评测、terminal-task 数据工程、Context Parallel、KV I/O、
FSDP、GUI/Deep Research benchmark、memory-augmented workflow 与 serving runtime。Persona 与
malicious-use 的原 Source Review 仍成立；本轮新增完成 DualPath、Untied Ulysses、terminal-capability data
engineering、veScale-FSDP、General Agent Evaluation、TTT/KV Binding、Agents of Chaos、
ARLArena、SkillOrchestra、GUI-Libra、Deep Research ranking、SWE-Protégé、EMPO²、AgentDropoutV2、
Search More, Think Less、ISO-Bench、TAPE、Aletheia / FirstProof、Multi-Vector Index Compression、
DPE、Reflective Test-Time Planning、Adaptive Text Anonymization、OmniGAIA、MobilityBench、DSDR、
Implicit Intelligence、PyVision-RL、ACE 与 Trinity of Consistency 二十九份学术全文复核，并完成
SGLang v0.5.9、vLLM v0.16.0 两份工程 Full Source Review。初轮 33 项均已获得逐项 disposition；
spillover 中 CUDA Agent、LK Losses、dLLM、STATIC、SWE-rebench V2 与 Memory Caching 已完成全文复核，
Cognitive Templates 完成低分 position-paper 拒绝核验；Tool-R0、LongVideo-R1、RLAD、CiteAudit、
Recovered in Translation、SenCache、CL4SE 与 Online World Modeling / MPAIL2 也已完成全文和章节
边界复核。随后扫描 HF 03-04～03-06 又恢复出 10 项 first-public date 属于 W09 的论文，总账扩为
58 项；其中 3 项低分候选已完成来源、日期与拒绝理由核验，另外 7 项进入 Full Source Review。随后 DBLP
交叉索引恢复出 HF spillover 页面也遗漏的 IMMACULATE、LLMServingSim 2.0、AMA-Bench、
Replicate-and-Quantize 与 MINAR。进一步核验发现 Replicate-and-Quantize 的同一核心方法已于
2024-09-22 在 OpenReview 公开，2026 arXiv v1 是扩展版本而非 W09 first-public event，故从候选总账剔除并
保留 Cross-Year Exclusion。MINAR 随后也确认已于 2025-09-23 在 OpenReview 公开，2026 arXiv 同样不是
first-public event。两项排除后 W09 总账曾为 61 项；新增的三个 in-window 候选分别补回黑盒 LLM API 可验证
审计、异构/disaggregated serving simulation 与 long-horizon Agent memory evaluation。三项均已完成全文审计；
IMMACULATE 把 model commitment、discrete-state commitment、LDD 与随机抽样组合为 service-integrity
evidence，但其实验实例仍依赖 CPU TDX enclave，公开仓库也未提供完整 VC/commitment protocol，故只能作为
`Experimental` Books Candidate。

CUPID 的论文、AAAI 正式页与 Appendix 已完成全文审计，但 first-public 复核再次改变账目：作者所在
Chung-Ang University 已在 2025-12-16 的官方成果公告中公开论文标题、shortcut unlearning、CUPID
框架及 Waterbirds/BAR/Biased NICO++ 实验对象。因此 2026-02-25 arXiv v1 是完整 manuscript 的后续公开，
不是 2026-W09 的首次事件。该记录从 W09 Candidate Scoring 与 Census 移除，保留为第三项
Cross-Year Exclusion，并应在后续 2025-W51 修复中归档。当时 W09 in-window 总账据此更正为 60 项；
这个数字随后又被 post-week spillover 检查修正，不能继续视为当前完成状态。在修复 W10 的
post-week discovery-lag 时又发现 Qwen3-Coder-Next（arXiv v1 2026-02-28）和
SkillNet（arXiv v1 2026-02-26）同样属于 W09，却未进入原总账。W09 因此再次重开为 62 项。
两项现已完成论文主体、Appendix、官方 model/repository 与目标/相邻章节联读；总账由此闭合为
58 项 Full Source Review 与 4 项低分来源/拒绝核验。Google Scholar/OpenAlex 的历史窗口仍是
documented discovery limitation，但不再与候选级 Evidence Gate 混写；它表示无法证明 discovery
recall 的数学完备性，不表示已审候选的 evidence packet 不完整。

交叉索引候选中，LLMServingSim 2.0 与 AMA-Bench 已完成全文、官方文档/数据与 artifact 联读。
LLMServingSim 2.0 把 simulation
identity 从单一 hardware profile 扩为 `workload + cluster + policy + operator profile + runtime revision`，
并以同一事件循环表达 request state 与 hardware/network/memory feedback；但作者的 aggregate error 不能
外推为未见 workload、tail SLO 或 hypothetical hardware 的通用精度，真实 replay/canary 仍拥有部署裁决权。
AMA-Bench 则把 Agent trajectory memory 拆为 construction 与 retrieval 两个 failure channel，并以
action-observation dependency、state update 与 abstraction 区分普通对话记忆；全文 Appendix 还纠正了项目页
旧数字，真实子集为 208 trajectories / 2,496 QA。它只证明特定离线 QA contract 下 causal graph 与非纯相似度
检索的增量价值，不证明图记忆是所有 Agent 的默认结构，也未覆盖 cross-task/lifelong memory。
AgentVista 的全文与 harness 复核进一步说明，benchmark task population 本身会被 filter model、tool rule、
no-tool baseline 与短答案可评分性塑造；post-hoc 单标签 error taxonomy 也不是 causal root cause。论文的
`temperature=0.6` 又与当前公开 quick-start 默认 `0.0` 不一致，必须把 paper-run 与 current artifact 分开。
CIRCLE 则把 open-world multimodal ICL 的 demonstrations 从静态输入改为可迭代的 derived state：固定未标注
context images，维护 pseudo-label vector，以 leave-one-out 方式并行重标并重复若干轮。它提供了“上下文也可被
状态化 refinement”的机制证据，同时暴露 self-conditioning error amplification、语义一致但 task-misaligned
的收敛、`O(T*m)` model calls 与 streaming memory update 开销；因此只能作为 Ch71 Context lifecycle 的
Experimental 候选，不能据作者表格声称 LMM 普遍优于 VLM。

前一批三项全文证据形成的稳定问题并不是某个作者 benchmark 的峰值数字，而是三类系统 contract：

1. 长多轮、短增量、高 KV 命中率的 Agent workload 会把 PD 系统的 storage read path 推到
   prefill SNIC，DualPath 用双路径、layerwise streaming 与联合调度重新分配网络瓶颈；
2. 长上下文训练的 capacity 不只由 attention 复杂度决定，DS-Ulysses 为所有 heads 同时物化
   buffer 的实现选择也会成为内存上限，Untied Ulysses 以 head-wise pipeline 换取容量；
3. terminal capability 的训练数据必须同时拥有任务、环境和 executable verifier；失败 trajectory
   可能包含 recovery signal，但论文没有在等数据量条件下证明“失败数据天然更好”。

后一批又补出三条长期边界：FSDP shard placement 必须保留 optimizer/quantization 的 block
semantics；Agent 评估对象必须绑定 model、architecture、protocol adaptor 与 benchmark；TTT-KVB
在满足 theorem assumptions 时更接近 history-dependent linear attention，而不是可逐项回读的
事实存储。后者可能修正 Ch22 对 test-time memory 的泛化，但不否定 KVB 之外的 online learning。

第三批进一步说明：Agent security 的 runtime principal 不能由 display name 或自然语言上下文隐式决定；
multi-turn RL 的 clipping、advantage、filtering 与 policy staleness 必须作为联合 contract；动态 orchestration
也需要把 skill taxonomy、agent competence、cost 与 handbook version 当成受控状态，而不是一次 prompt
选择。三项均有机制价值，但证据仍分别受开放式 case study、特定 RL recipe 与固定 agent pool 限制。

第四批补出三个不能混写的系统对象：partial-verifiability 会改变 GUI RL 的 policy-update contract；
Agentic retrieval 的 query dialect、ranker training distribution、retrieval unit 与 reader budget 共同决定排序；
稀疏 expert assistance 的关键状态是 escalation、advice provenance 与 follow-through，而不是把 expert
误写成拥有行动权的 peer Agent。三项都形成了章节级机制缺口，但论文证据分别受特定 GUI benchmark、
不完整 factorial matrix 与单一 coding-agent stack 限制。

第五批又区分出三条演进路线：EMPO² 用临时 memory scaffold 连接跨 rollout 探索与参数内化；
AgentDropoutV2 在 Multi-Agent message edge 上加入带 failure-memory 的 rectify/reject gate；SMTL 将
长时程 search 的扩展轴从单链 reasoning depth 转向受依赖约束的并行 evidence acquisition。三者都
不能被简化成“记忆越多”“过滤越严”或“并行越多”越好，分别新增 off-policy drift、false reject/
global reset 和 context/merge/resource contention。

第六批把三个容易被 headline 混淆的对象重新拆开。ISO-Bench 评估的是 coding Agent 能否产生既
达到性能目标、又保持功能正确、且真正命中瓶颈机制的 patch；TAPE 将“计划本身不可行”与“执行
动作偏离计划”分成不同 error channel，再由 plan graph、外部 solver、constrained execution 与
mismatch-triggered replanning 分层治理；Aletheia / FirstProof 则表明 proof artifact 的数学内容、补全
成本、发表标准和自治程度不能压缩成单一 solved/unsolved 标签。三项都形成章节级机制候选，但分别
受单卡/局部 patch benchmark、合成 budgeted tasks 与作者主导 expert assessment 的条件限制。

第七批继续拆开 storage representation、training feedback loop 与 deployment-time adaptation。Multi-
Vector Index Compression 将 late-interaction document state 压到固定 vector budget，但 encoder 仍需先
消费原始 multimodal input，因而“索引更小”不等于 indexing path 或端到端 latency 等比下降；DPE
把当前 checkpoint 的 failure taxonomy 编译成下一轮 data quota、生成要求和难度过滤，但 diagnostic /
validation Agent 本身也会把 measurement bias 写回训练分布；Reflective Test-Time Planning 则在 episode
内用 retrospective reflection 更新 LoRA/weights，已经越过普通 verbal reflection，属于 reflection-guided
test-time parameter adaptation。三条路线均保留旧方案成立条件与新增 drift/failure modes。

第八批进一步修正了三个容易被“效果更好”掩盖的系统边界。Adaptive Text Anonymization 学到的是
特定 attacker、utility metric 与 task distribution 下的经验 Pareto policy，不提供 Differential Privacy
保证；OmniGAIA 把 native perception、按需 perception tool、tool-integrated trajectory 与 fine-grained
preference correction 放在同一实验中，但 360 个合成/人工筛选任务和 LLM judge 只能支持该 benchmark
contract；MobilityBench 用 frozen API response replay 获得可重复的 route-agent 诊断，却也冻结了交通、
天气与服务漂移，不能等价于在线 mobility readiness。三项都具有长期机制价值，但不能把作者排行榜
外推为通用模型或 Agent 架构排序。

第九批把 exploration、implicit requirements 与 multimodal interaction 分别落到可审计 contract。DSDR
只在 verifier 判为正确的轨迹上增加 global diversity，并把 local entropy 导向更 distinctive 的 mode；
Implicit Intelligence 用 YAML-declared state/rules/rubric 把“用户没说什么”变成可探索环境，但 LLM world
model 的 98.6% consistency 也说明它不是严格 deterministic executor；PyVision-RL 同时修改 reward、group
selection 与 media materialization，缓解 interaction collapse 的同时新增 tool inflation、difficulty sampling
bias 与 Python sandbox 风险。三者都不是“diversity/tool calls/隐式推断越多越好”的单向演进。

最后两项把 RLVR error heterogeneity 与 world-model evaluation 的证据边界补齐。ACE 不按错误内容
分类，而按 policy 相对 reference 的 trajectory-level confidence shift 调整 negative advantage；收益依赖
reference calibration、binary verifier、长度归一化与理论假设。Trinity / CoW-Bench 则把 modal、spatial、
temporal consistency 及交叉项拆为 atomic checks，但公开实现仍以四帧 grid + `gpt-4.1` judge 评分，且
论文 1,485 条与公开 dataset 1,435 rows 存在版本差异。因此前者形成 Ch29 机制候选，后者只作为
Ch10/62 已有原则的受限案例，不强行写入 Books。

工程交叉检查纠正了旧结论：SGLang v0.5.9 于 02-24、vLLM v0.16.0 于 02-25 发布，均是
W09 的独立 stable-release 事件。前者把 LoRA load 从同步阻塞改成 scheduler-visible 的异步
readiness state，并用后续 Spec V2 修复暴露了跨 CUDA stream buffer lifetime contract；后者让
asynchronous scheduling 与 Pipeline Parallel 共存，以 last-stage sampled-token broadcast 和本地
in-flight row mapping 替代 CPU round-trip，但后续 stuck chunked request 与 multi-node context
contamination 报告说明同步点被移除后，ownership、ordering 与 recovery 必须被显式化。两项 release
headline 性能均不能脱离各自 workload contract 外推。

既有 33 项候选阅读账目已闭合。02-28 与 03-01 没有独立 arXiv announcement batch；arXiv 官方材料
说明常规公告每周五天，本轮 date query 与来源交叉检查也未恢复出额外 W09 first-public event。
Google Scholar、OpenAlex、DBLP 的历史索引完整性无法由一次回填证明，已保留为 documented discovery
limitation，而不是把“未发现”写成“绝对不存在”。更关键的是，Hugging Face 2026-03-02 页面延迟收录
了从 02-24 到 02-27 first-public 的 papers；03-03 页面还继续出现 W09 事件。进一步检查 03-04～03-06
又恢复出 10 项 W09 论文，而 Spilled Energy 与 AgentConductor 经 primary metadata 复核后归回 W08。
当前 in-window ledger 为 62 项：58 项完成 Full Source Review，4 项完成低分来源/拒绝核验；另有
3 项交叉索引记录因 first-public date 早于 W09 窗口被排除。候选级 Evidence Gate 已通过，Books
Integration 可按 owner/adjacent-chapter 顺序开始；Google Scholar/OpenAlex coverage gap 继续保留为
Discovery Limitation，不能据此宣称历史候选绝对无遗漏。

## Coverage and Source Coverage

- 模型与研究机构：核验 Anthropic 2 月 23 日 persona research、OpenAI 2 月 25 日 threat-intelligence
  report；二者分别是解释性研究与平台观测，不披露可复现的生产内部机制。
- arXiv / 学术来源：初轮按 arXiv v1 first-public date 恢复 29 项；检查 post-week 延迟收录后
  又恢复 27 项，DBLP 等交叉索引再恢复 5 项，共发现 61 条学术记录。经 source-family first-public
  复核，Replicate-and-Quantize、MINAR 与 CUPID 三条分别归回 2024、2025-W39 与 2025-W51，故 W09
  有效学术候选为 58 项。HF/DBLP date 只作为 discovery signal，事件归周以 primary metadata 为准；
  至少要向后检查下一工作周，不能把 Weekly 页面窗口误当 first-public 窗口。
- AI Infra 与工程项目：确认 SGLang v0.5.9（02-24）与 vLLM v0.16.0（02-25）为本周 stable
  release，并联读 release notes、关键 merged PR、RFC、代码 diff 与后续 correctness issue。Dynamo
  v0.9.0 在 W07、v0.9.1 在 W10；PyTorch 2.11.0 在 W13，均不重复计入 W09。
- Discovery limitations：Hugging Face 2026-02-28 与 2026-03-01 Daily 页面返回错误。arXiv 官方
  annual report 说明常规公告每周五天，因此周末没有独立 announcement batch；date query 与交叉索引
  尝试未发现额外 W09 event，但 Google Scholar、OpenAlex、DBLP 的历史收录完整性仍不能视为已证明。
  本轮 DBLP 交叉索引已恢复 5 条记录并完成 source-family 去重；OpenAlex 当前官方 Works API 要求 API key，
  未认证查询未能获得可审计结果；Google Scholar 的限定周窗口查询也未返回可用结果。两者不能被写成
  “已扫描且无遗漏”，只记录为明确 coverage gap，后续有可用访问路径时幂等重开。

## Candidate Scoring

| Candidate | TN | SI | PV | SR | PR | L | Total | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| Persona selection model | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | No Change — Ch5/Ch66/Ch72 already separate explanation, evidence and policy authority |
| Disrupting malicious uses of AI | 2 | 4 | 4 | 5 | 4 | 4 | 23/30 | No Change — Ch72 already owns threat-to-control boundaries; operational evidence remains Weekly |
| SkillOrchestra | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-PLATFORM` / Ch84 |
| Agents of Chaos | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `PLATFORM-SECURITY` / Ch72 |
| DSDR | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Refine — `TRAIN-GRPO` / Ch33 |
| TAPE | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `AGENT-PLANNING` / Ch79 |
| Implicit Intelligence | 3 | 3 | 4 | 3 | 4 | 4 | 21/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| ISO-Bench | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| Data Engineering for Terminal Capabilities | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Refine — `TRAIN-DATA` / Ch27 |
| TTT with KV Binding | 5 | 4 | 4 | 4 | 5 | 5 | 27/30 | Refine — `MODEL-LONG-CONTEXT` / Ch22 |
| PyVision-RL | 3 | 3 | 3 | 4 | 4 | 4 | 21/30 | Refine — `TRAIN-GRPO` / Ch33 |
| Multi-Vector Index Compression | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Refine — `AGENT-RAG` / Ch76 |
| Untied Ulysses / UPipe | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `TRAIN-DISTRIBUTED-TRAINING` / Ch36 |
| Aletheia / FirstProof | 4 | 4 | 3 | 5 | 4 | 4 | 24/30 | No Change — Ch66 already separates artifact correctness, significance and autonomy |
| Reflective Test-Time Planning | 4 | 3 | 3 | 4 | 4 | 4 | 22/30 | Refine — `AGENT-REFLECTION` / Ch80 |
| Adaptive Text Anonymization | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Refine — `PLATFORM-SECURITY` / Ch72 |
| Overconfident Errors Need Stronger Correction | 3 | 3 | 3 | 4 | 4 | 3 | 20/30 | Refine — `TRAIN-GRPO` / Ch33 |
| DualPath | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `INFER-PD-DISAGGREGATION` / Ch55 |
| ARLArena | 4 | 5 | 4 | 4 | 5 | 4 | 26/30 | Refine — `TRAIN-GRPO` / Ch33 |
| GUI-Libra | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` / Ch33 |
| Revisiting Text Ranking in Deep Research | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-RAG` / Ch76 |
| veScale-FSDP | 5 | 5 | 5 | 4 | 5 | 5 | 29/30 | Refine — `TRAIN-ZERO` / Ch39 |
| SWE-Protégé | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-MEMORY` / Ch77 |
| Trinity of Consistency | 3 | 3 | 2 | 4 | 2 | 4 | 18/30 | No Change — Ch25/Ch66 already separate causal world-state and scorer evidence |
| DPE | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine — `TRAIN-DATA` / Ch27 |
| MobilityBench | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| OmniGAIA | 4 | 4 | 3 | 4 | 4 | 4 | 23/30 | Refine — `AGENT-TOOL-CALLING` / Ch78 |
| EMPO² | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` / Ch33 |
| AgentDropoutV2 | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | Refine — `AGENT-MULTI-AGENT` / Ch82 |
| Search More, Think Less | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-PLANNING` / Ch79 |
| General Agent Evaluation | 4 | 5 | 5 | 4 | 5 | 5 | 28/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| LongVideo-R1 | 3 | 3 | 4 | 4 | 5 | 4 | 23/30 | Refine — `AGENT-PLANNING` / Ch79 |
| Tool-R0 | 4 | 4 | 4 | 4 | 5 | 5 | 26/30 | Refine — `TRAIN-GRPO` / Ch33 |
| Recovered in Translation | 3 | 3 | 4 | 4 | 4 | 4 | 22/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| dLLM framework | 4 | 4 | 5 | 5 | 4 | 3 | 25/30 | Refine — `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 |
| CiteAudit | 3 | 4 | 4 | 4 | 4 | 4 | 23/30 | No Change — Ch66 already separates citation existence, entailment and claim provenance |
| Vectorizing the Trie / STATIC | 5 | 5 | 5 | 4 | 4 | 4 | 27/30 | Refine — `INFER-TENSORRT-LLM` / Ch49 |
| Reinforcement-aware Knowledge Distillation | 4 | 4 | 4 | 3 | 5 | 4 | 24/30 | Refine — `TRAIN-GRPO` / Ch33 |
| CL4SE | 3 | 3 | 4 | 4 | 4 | 3 | 21/30 | No Change — Ch75/Ch66 already own typed Context and evaluation identity |
| Cognitive Models as Agent Templates | 2 | 2 | 2 | 4 | 3 | 5 | 18/30 | Weekly Only — position paper without incremental system mechanism |
| CUDA Agent | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Refine — `TRAIN-GRPO` / Ch33 |
| LK Losses | 5 | 5 | 5 | 4 | 5 | 3 | 27/30 | Refine — `INFER-SPECULATIVE-DECODING` / Ch48 |
| Memory Caching | 5 | 4 | 4 | 4 | 5 | 4 | 26/30 | Refine — `MODEL-LONG-CONTEXT` / Ch22 |
| SenCache | 4 | 4 | 4 | 4 | 4 | 3 | 23/30 | Refine — `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24; former structural gap closed by Part III |
| SWE-rebench V2 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Refine — `TRAIN-DATA` / Ch27 |
| Online World Modeling for IRLfO | 4 | 4 | 4 | 4 | 4 | 4 | 24/30 | Refine — `MULTIMODAL-EMBODIED-VLA` / Ch26 |
| QEDBENCH | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| Humans and LLMs Diverge on Probabilistic Inferences | 3 | 2 | 3 | 4 | 4 | 4 | 20/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| IMMACULATE | 5 | 5 | 4 | 4 | 5 | 5 | 28/30 | Refine — `PLATFORM-SECURITY` / Ch72 |
| LLMServingSim 2.0 | 5 | 5 | 5 | 5 | 5 | 4 | 29/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| AMA-Bench | 4 | 4 | 5 | 4 | 5 | 5 | 27/30 | Refine — `AGENT-MEMORY` / Ch77 |
| Transformers Converge to Invariant Algorithmic Cores | 4 | 3 | 3 | 3 | 5 | 5 | 23/30 | Refine — `WORLDVIEW-REPRESENTATION` / Ch5 |
| AgentVista | 3 | 4 | 4 | 4 | 5 | 4 | 24/30 | Refine — `PLATFORM-EVALUATION-SYSTEM` / Ch66 |
| Large Multimodal Models as General In-Context Classifiers / CIRCLE | 3 | 3 | 3 | 4 | 3 | 4 | 20/30 | Refine — `AGENT-CONTEXT` / Ch75 |
| Truncated Step-Level Sampling / SLATE | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `TRAIN-GRPO` / Ch33 |
| BBQ-to-Image | 3 | 3 | 3 | 4 | 2 | 3 | 18/30 | Weekly Only — low project relevance; no new owner mechanism |
| Simulating Social Media Users with LLMs / CCP | 3 | 2 | 3 | 4 | 3 | 4 | 19/30 | Weekly Only — operational-validity case covered by Ch66 evaluation contract |
| SGDC | 3 | 2 | 3 | 4 | 1 | 4 | 17/30 | Weekly Only — domain method outside current AI System mechanism scope |
| SGLang v0.5.9 | 4 | 5 | 5 | 5 | 5 | 4 | 28/30 | Refine — `INFER-SGLANG` / Ch51 |
| vLLM v0.16.0 | 4 | 5 | 5 | 5 | 5 | 5 | 29/30 | Refine — `INFER-VLLM` / Ch50 |
| SkillNet | 4 | 4 | 4 | 4 | 5 | 4 | 25/30 | Refine — `AGENT-PLATFORM` / Ch84 |
| Qwen3-Coder-Next Technical Report | 4 | 4 | 5 | 5 | 5 | 4 | 27/30 | Refine — `TRAIN-SFT` / Ch29 |

评分是 discovery 阶段的初始优先级，不是论文结论已验证。完成全文阅读、artifact 联读和相邻章节
复核后允许升降分；在此之前 `20+` 只表示必须继续审计。

## Recovered Candidate Census

| Event Date | Candidate | Primary Source | Discovery / Family Signal | Initial Scope Decision | Review State |
| --- | --- | --- | --- | --- | --- |
| 2026-02-23 | Persona Selection Model | Anthropic Research | official research | Ch5/68 | Full Review Complete — No Change |
| 2026-02-23 | SkillOrchestra | arXiv:2602.19672 + official code | HF 02-24 / orchestration | Ch80 main candidate; Ch75/77/78 boundary | Full Review Complete — Books Candidate |
| 2026-02-23 | Agents of Chaos | arXiv:2602.20021 + interactive logs | HF 02-24 / live-lab security | Ch68 main candidate; Ch62/77/78/80 boundary | Full Review Complete — Books Candidate |
| 2026-02-23 | DSDR | arXiv:2602.19895 + official code link | HF 02-24 / RLVR diversity | Ch29 main candidate; Ch28 boundary | Full Review Complete — Books Candidate |
| 2026-02-23 | TAPE | arXiv:2602.19633 + official code | HF 02-24 / planning with solver | Ch75 main candidate; Ch74/76/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-23 | Implicit Intelligence | arXiv:2602.20424 + official leaderboard | HF 02-24 / implicit-intent eval | Ch62 main candidate; Ch71/74/75 boundary | Full Review Complete — Books Candidate |
| 2026-02-23 | ISO-Bench | arXiv:2602.19594 + official code/data | HF 02-24 / inference optimization agents | Ch62 main candidate; Ch46/47/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Data Engineering for Terminal Capabilities | arXiv:2602.21193 | HF 02-25 / executable training data | Ch23 main candidate; Ch25/62/75/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | TTT with KV Binding | arXiv:2602.21204 v1; v4 2026-05-12 + NVIDIA project page | HF 02-25 / linear-attention interpretation | Ch22 main candidate; Ch14/19 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | PyVision-RL | arXiv:2602.20739 + official code/data/models | HF 02-25 / vision RL | Ch29 main candidate; Ch62/74 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Multi-Vector Index Compression | arXiv:2602.21202 + official code | HF 02-25 / retrieval index | Ch72 main candidate; Ch71/62 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Untied Ulysses / UPipe | arXiv:2602.21196 v1; v2 2026-07-10 | HF 02-25 / Context Parallel | Ch32/36 main candidates; Ch22/33/34 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Aletheia / FirstProof | arXiv:2602.21201 + DeepMind raw artifacts | HF 02-25 / proof artifacts | Ch62 main candidate; Ch77 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Reflective Test-Time Planning | arXiv:2602.21198 + official code | HF 02-25 / learning from trials | Ch76 main candidate; Ch29/73/75/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Adaptive Text Anonymization | arXiv:2602.20743 + official code | HF 02-25 / privacy policy | Ch68 main candidate; Ch62 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Overconfident Errors Need Stronger Correction | arXiv:2602.21420 | HF 02-25 / confidence-aware correction | Ch29 main candidate; Ch28/30 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | SGLang v0.5.9 | official release + merged PRs #15512/#14668/#18958 | stable release / serving runtime | Ch46 main candidate; Ch47/52 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | OpenAI malicious-use report | OpenAI Threat Intelligence | official report | Ch68/77 | Full Review Complete — No Change |
| 2026-02-25 | vLLM v0.16.0 | official release + PR #32618 + RFC/issues | stable release / async PP scheduling | Ch46 main candidate; Ch34/52 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | DualPath | arXiv:2602.21548 v1; v2 2026-02-26 | HF 02-26 / KV I/O path | Ch51 main candidate; Ch48/50/52 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | ARLArena | arXiv:2602.21534 v1; v3 2026-07-04 + official code | HF 02-26 / agentic RL systems | Ch29 main candidate; Ch25/33/62/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | GUI-Libra | arXiv:2602.22190 v1; v2 2026-05-25 + official code | HF 02-26 / GUI-agent RL | Ch29 main candidate; Ch25/62/74/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | Revisiting Text Ranking in Deep Research | arXiv:2602.21456 + official code/artifact | HF 02-26 / ranking in research workflow | Ch72 main candidate; Ch62/71/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | veScale-FSDP | arXiv:2602.22437 v1; v3 2026-04-21 + official partial artifact | HF 02-26 / sharding runtime | Ch35 main candidate; Ch32/36 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | SWE-Protégé | arXiv:2602.22124 | HF 02-26 / sparse expert collaboration | Ch77 main candidate; Ch74/76/78 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | Trinity of Consistency | arXiv:2602.23152 + CoW-Bench artifacts | HF 02-27 / world-model framing | Ch10 concept; Ch62 evaluation boundary | Full Review Complete — No Change / Weekly Only |
| 2026-02-26 | DPE | arXiv:2602.22859 + official code/models | HF 02-27 / diagnostic data iteration | Ch23 main candidate; Ch29/62 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | MobilityBench | arXiv:2602.22638 + official code/data | HF 02-27 / domain Agent eval | Ch62 main candidate; Ch74/75 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | OmniGAIA | arXiv:2602.22897 + official code/data/models | HF 02-27 / multimodal Agent eval | Ch74 main candidate; Ch27/62/75 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | EMPO² | arXiv:2602.23008 v1; v2 2026-03-06 + official Agent Lightning integration | HF 02-27 / exploratory memory RL | Ch29 main candidate; Ch73/75 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | AgentDropoutV2 | arXiv:2602.23258 v1; v2 2026-05-28 + official code | HF 02-27 / multi-agent information flow | Ch78 main candidate; Ch73/76/77/80 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | Search More, Think Less | arXiv:2602.22675 v1; v2 2026-02-27 | HF 02-27 / parallel search policy | Ch75 main candidate; Ch71/72/77/78 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | General Agent Evaluation | arXiv:2602.22953 v1; v2 2026-05-11 + Exgentic artifacts | HF 02-27 / evaluation framework | Ch62 main candidate; Ch63/69/75/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | LongVideo-R1 | arXiv:2602.20913 v1 + code/data | HF 03-02 spillover / active video navigation | Ch75 owner candidate; Ch29/62/74 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | Tool-R0 | arXiv:2602.21320 v1 + code/models/logs | HF 03-03 spillover / self-play tool learning | Ch29 owner candidate; Ch23/74/75/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-25 | Recovered in Translation | arXiv:2602.22207 v1 | HF 03-02 spillover / multilingual benchmark pipeline | Ch62 owner candidate; Ch23 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | dLLM framework | arXiv:2602.22661 v1 + official code | HF 03-02 spillover / diffusion-LM system | Ch20 candidate; Ch19/21/38/40/62 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | CiteAudit | arXiv:2602.23452 v1; v3 2026-05-01 + code/data | HF 03-02 spillover / citation verification | Ch62 owner check; Ch72/73/77 boundary | Full Review Complete — No Change / Weekly Only |
| 2026-02-26 | Vectorizing the Trie / STATIC | arXiv:2602.22647 v1; v2 2026-07-20 | HF 03-02 spillover / accelerator-constrained decoding | Ch40 candidate; Ch20/45/46/52/72 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | Reinforcement-aware Knowledge Distillation | arXiv:2602.22495 v1; v3 2026-06-17 | HF 03-02 spillover / on-policy distillation | Ch29 owner candidate; Ch24/28/30 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | CL4SE | arXiv:2602.23047 v1; v3 2026-04-06 | HF 03-02 spillover / SE context benchmark | Ch71 owner reviewed; Ch62/77 boundary | Full Review Complete — No Change |
| 2026-02-26 | Cognitive Models as Agent Templates | arXiv:2602.22523 v1 | HF 03-02 spillover / position paper | Ch78 concept boundary | Source/Date Verified — Weekly Only |
| 2026-02-27 | CUDA Agent | arXiv:2602.24286 v1 + project/artifact | HF 03-02 spillover / executable kernel RL | Ch29 candidate; Ch62/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-27 | LK Losses | arXiv:2602.23881 v1; v2 2026-06-01 | HF 03-02 spillover / speculative-draft objective | Ch44 candidate; Ch29 boundary | Full Review Complete — Books Candidate |
| 2026-02-27 | Memory Caching | arXiv:2602.24281 v1 | HF 03-02 spillover / growing recurrent memory | Ch22 candidate; Ch14/19/41/73 boundary | Full Review Complete — Books Candidate |
| 2026-02-27 | SenCache | arXiv:2602.24208 v1 | HF 03-02 spillover / diffusion inference cache | Ch38/40 structural boundary | Full Review Complete — Weekly Only / Structural Gap |
| 2026-02-27 | SWE-rebench V2 | arXiv:2602.23866 v1; v2 2026-06-01 + artifacts | HF 03-03 spillover / executable SWE data | Ch23 candidate; Ch24/25/29/62/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-27 | Online World Modeling for IRLfO | arXiv:2602.24121 v1; v2 2026-06-18 + project | HF 03-03 spillover / robot learning | Ch10 owner candidate; Ch29/74/62 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | QEDBENCH | arXiv:2602.20629 v1; v3 2026-07-06 + benchmark | HF 03-04 spillover / proof-judge alignment | Ch62 owner candidate; Ch77 boundary | Full Review Complete — Books Candidate |
| 2026-02-24 | BBQ-to-Image | arXiv:2602.20672 v1 | HF 03-04 spillover / structured image control | Ch27 boundary | Source/Date Verified — Low Project Relevance |
| 2026-02-26 | Humans and LLMs Diverge on Probabilistic Inferences | arXiv:2602.23546 v1 + data/code | HF 03-04 spillover / probabilistic reasoning eval | Ch62 owner candidate; Ch5/20 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | IMMACULATE | arXiv:2602.22700 v1 + author code | DBLP cross-index recovery / verifiable LLM-service audit | Ch68 owner candidate; Ch64～66/69 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | LLMServingSim 2.0 | arXiv:2602.23036 v1 + GitHub/Zenodo artifact | DBLP cross-index recovery / heterogeneous and disaggregated serving simulation | Ch62 owner candidate; Ch45/48/50～52/59 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | AMA-Bench | arXiv:2602.22769 v1 + project/code/dataset | DBLP cross-index recovery / long-horizon agent memory evaluation | Ch73 owner candidate; Ch62/72/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | Simulating Social Media Users with LLMs / CCP | arXiv:2602.22752 v1 | HF 03-04 spillover / operational validity | Ch62/68 boundary | Source/Date Verified — Weekly Only |
| 2026-02-26 | Transformers Converge to Invariant Algorithmic Cores | arXiv:2602.22600 v1; v2 2026-07-06 + code | HF 03-04 spillover / interpretability | Ch5 owner candidate; Ch4/6/62 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | SGDC | arXiv:2602.23496 v1 + code | HF 03-04 spillover / medical segmentation | Ch27 boundary | Source/Date Verified — Low Project Relevance |
| 2026-02-26 | AgentVista | arXiv:2602.23166 v1; v2 2026-03-02 + code/dataset | HF 03-06 spillover / multimodal-agent eval | Ch62 owner candidate; Ch74/75/77 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | Large Multimodal Models as General In-Context Classifiers / CIRCLE | arXiv:2602.23229 v1 + CVF/project | HF 03-06 spillover / multimodal ICL | Ch71 owner candidate; Ch62/72 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | Truncated Step-Level Sampling / SLATE | arXiv:2602.23440 v1; v4 2026-07-09 + code | HF 03-06 spillover / retrieval RL credit assignment | Ch29 owner candidate; Ch72/75 boundary | Full Review Complete — Books Candidate |
| 2026-02-26 | SkillNet | arXiv:2603.04448 v1 + official project/code | post-week spillover / skill asset infrastructure | Ch80 owner candidate; Ch73/77/78 boundary | Full Review Complete — Books Candidate |
| 2026-02-28 | Qwen3-Coder-Next Technical Report | arXiv:2603.00729 v1 + official model/repository | post-week spillover / coding-agent model and executable training | Ch25 owner candidate; Ch21/23/29/62/77 boundary | Full Review Complete — Books Candidate |

`Recovered Candidate Census` 只证明候选身份、primary URL、v1 date 与初始知识树位置已经核对。
它不证明摘要中的机制、作者 benchmark 或 Books disposition 已经成立。

## Full Source Review

### Persona selection model

- **Candidate / Week / Score:** Persona Selection Model / 2026-W09 / 23/30；
  `Source Family ID: persona-selection-assistant-axis`。
- **Source Type / Date / Sources:** Anthropic Alignment Research conceptual/empirical synthesis，
  2026-02-23；联读完整 alignment post 与其引用的 persona/assistant-axis、emergent-misalignment evidence。
- **Full-read Coverage:** Verified；检查 pretraining persona simulation、post-training selection/refinement、
  behavioral/generalization/interpretability evidence、development implications 与模型不完备性声明。
- **Problem / Previous Design / Mechanism:** 把 assistant 当普通程序或独立 goal object 无法解释 roleplay、
  broad trait generalization；PSM 把 post-training理解为在 pretrained persona space 中选择/细化 Assistant。
  这是解释模型，不是 runtime state-machine specification。
- **Evidence Boundary:** 相关行为、steering 与 cross-domain trait generalization 支持 PSM 是一种有用视角；
  作者明确不确定其是否 exhaustive、是否存在 persona 外 agency、以及更强 post-training 后是否仍成立。
- **Trade-offs / Previous Design:** anthropomorphic model 可帮助提出 red-team hypotheses，却易把隐喻当本体、
  忽略 optimization/data/runtime；behavioral specification 与 causal intervention 仍需独立证据。
- **Evolution / ROADMAP:** `Layering / Dependency` with W04 Assistant Axis；Ch5/68。已读相邻章节；Ch5
  evidence ladder 已要求从 explanatory model 走向 intervention/replication。
- **Integration Decision:** `No Change — Already Covered`；不把理论视角写成普遍内部机制。
- **Open Questions:** 如何设计能区分 persona simulation、goal-directed policy 与 Context-conditioned
  behavior 的 falsifiable intervention？

### Disrupting malicious uses of AI

- **Candidate / Week / Score:** Malicious-use report / 2026-W09 / 23/30；
  `Source Family ID: openai-threat-intelligence-workflow-2026`。
- **Source Type / Date / Sources:** OpenAI 官方 threat-intelligence/abuse disruption report，
  2026-02-25；案例是平台观测，不是全行业 prevalence study。
- **Coverage / Mechanism:** 已检查案例分类、攻击 workflow 中模型与传统工具的组合、disruption action、
  attribution/evidence caveats。具体 detection models、threshold 和 internal enforcement Not Disclosed。
- **State Ownership / Flow:** adversary account/tool/model/external infrastructure 构成跨系统 trajectory；
  provider 拥有 account telemetry 与 enforcement，外部平台各自拥有 action evidence。孤立 prompt 不是完整
  security object。
- **Evidence Boundary:** 证明报告所述组合式滥用被观察和处置；不估计总体发生率，不证明模型是攻击
  成功的充分原因，也不公开足够机制供独立复现 detection precision/recall。
- **Trade-offs / Previous Design:** workflow correlation 可发现分散 signal，却扩大 surveillance、privacy、
  false-positive、cross-provider identity 和 evidence-retention 成本；单请求 filters 对明显 content 仍有用。
- **Evolution / ROADMAP:** `Layering / Dependency`；Ch68 主 owner，Ch64/65/77 相邻。现有正文已覆盖
  identity、tool chain、side effects 与 evidence graph。
- **Integration Decision:** `No Change — Already Covered`；Weekly only operational evidence。
- **Open Questions:** 跨模型/工具/平台的最小化 telemetry 如何支持 appeal、attribution 和 privacy-preserving
  threat correlation？

### Data Engineering for Scaling LLM Terminal Capabilities

- **Candidate / Week / Score:** Data Engineering for Scaling LLM Terminal Capabilities / 2026-W09 /
  28/30；`Source Family ID: terminal-data-environment-verifier-2026`。
- **Source Type / Date / Revision:** arXiv paper，v1 2026-02-24；本轮读取 arXiv metadata、HTML
  全文、实验表格和与结论有关的 Appendix prompts / skill taxonomy。未发现后续 revision。
- **Direct Primary Sources / Access:** arXiv:2602.21193；paper 可访问。作者表示 release “most”
  synthetic datasets，因此公开 artifact 不能被表述为完整训练数据和生成 pipeline 的逐项复现。
- **Original Problem / Why Previous Design Was Reasonable:** 通用 instruction data 和人工收集的
  terminal tasks 便于审查、分布明确，也不依赖复杂 sandbox；但规模扩大后，任务 breadth、难度、
  environment validity 与 executable verification 很难同时保持。只生成自然语言 instruction 会把
  “任务像真的”误当成“任务可执行、可判定”。
- **Changed Constraint / Mechanism:** 论文并行使用 dataset adapters、seed-based generation 与
  skill-taxonomy generation；每个生成任务包含 instruction、files/environment 与 pytest verifier，
  reference solution 不暴露给训练 Agent。数据再经过 14-gram decontamination、identity/Chinese
  filters，并比较 incomplete、successful 与 mixed trajectories。这里真正改变的是数据对象：

  ```text
  instruction-only sample
  -> task + environment + executable verifier
  -> trajectory generated under a named agent/runtime
  -> filtering/mixing policy
  -> SFT example
  ```

- **State Ownership / Control and Data Flow:** 数据生成器拥有 task specification 与 seed/skill lineage；
  Harbor/Singularity 环境拥有文件和进程状态；pytest verifier 拥有可执行 success signal；Terminus 2
  拥有 action trajectory；训练 pipeline 只消费经过过滤和 serialization 的样本。环境构建失败、
  verifier 漏洞和 agent/runtime version 都必须独立记录，不能只保留最终 reward。
- **Implementation Details:** 论文用 Harbor 管理 benchmark environment，并以 Singularity 在 HPC
  上运行；作者报告少量 fakeroot/overlay failure。训练使用 veRL SFT。评测使用 Daytona 与
  Terminal-Bench 2.0 / Terminus 2 harness。这些是版本化实现事实，不构成所有 terminal training
  pipeline 的固定栈。
- **Evaluation Contract:** Qwen3 8B/14B/32B；最大 sequence length 32,768，global batch 128，
  micro-batch 1，AdamW、learning rate `2e-5`、weight decay `1e-4`、2 epochs、cosine schedule、
  10% warm-up。8B/14B 使用 32 GPUs，32B 使用 128 GPUs，并启用 CPU offload。作者报告
  Terminal-Bench 2.0 分数分别从 2.47→13.0、4.04→20.2、3.37→27.4；这些数字绑定上述
  model、harness、agent 与训练 contract，不能外推到其他模型或真实运维任务。
- **Baselines / Ablations / Sensitivity:** skill-based synthetic data 是合成增益的主要来源；叠加
  seed-based data 主要降低方差，没有提高均值。论文中的 no-filtering 高于 complete-only 与
  success-only，支持“失败 trajectory 可能含 recovery signal”的假设；但没有用等数据量对照排除
  volume/confounding。Two-stage curriculum 低于 mixed training，不能由此否定其他 curriculum。
- **What Evidence Proves / Does Not Prove:** 证明在披露的 Qwen3 SFT + Terminus2/TB2 contract 中，
  executable task/environment/verifier 联合生成可以显著改变 terminal benchmark performance；不证明
  数据工程普遍优于 RL，不证明失败样本天然更优，也不证明 benchmark gain 等于生产 shell safety。
- **Trade-offs / New Failure Modes:** executable verifier 提供更强监督，却新增 reward hacking、
  environment drift、test incompleteness、secret leakage、sandbox escape 与 artifact versioning 成本。
  失败 trajectory 可教 recovery，也可能放大无效 action 或错误惯例。人工任务在高风险、难以自动
  判定或 verifier 成本高的领域仍然合理。
- **Evolution / ROADMAP:** `Direct Refinement` of instruction-data engineering；Ch23 是主 owner
  候选，Ch25、62、75、77 是 boundary/handoff。已读 Ch75、77 以确认 planning/workflow 不应拥有
  训练数据主论证；Ch23 及相邻 Ch24/25 的写入前复核尚未完成。
- **Integration Decision:** `Full Review Complete — Books Candidate / Data-Verifier Contract`；
  Books Gate 关闭，本周不写入正文。
- **Open Questions:** 如何用 held-out tasks、mutation testing 与 adversarial verifier tests 分离
  genuine capability、harness familiarity 与 test exploitation？失败 trajectory 的增益在等 token、
  等 task diversity 条件下是否仍成立？

### Untied Ulysses / UPipe

- **Candidate / Week / Score:** Untied Ulysses: Memory-Efficient Context Parallelism via Head-Wise
  Pipelining / 2026-W09 / 29/30；`Source Family ID: context-parallel-head-pipeline-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-24，v2 2026-07-10。本周事件按 v1
  归档；当前 HTML 的 v2 只用于机制与 revision 核验，不能把 7 月新增内容反写成本周事件。
- **Direct Primary Sources / Full-read Coverage:** arXiv:2602.21196 metadata + HTML；已读
  Abstract、Introduction、Background、mechanism、GQA schedule、implementation、全部 experiment
  setup、baseline、ablation、numerical validation、scope/limitations 与相关 Appendix。
- **Original Problem / Why Previous Design Was Reasonable:** DeepSpeed-Ulysses 以 sequence shard
  配合 All-to-All，在完整 Q/K/V heads 上执行 attention；当 context 与 head 数较小时，一次 materialize
  全部 heads 的 buffer 可以减少 pipeline stages 与 launch overhead，机制简单、吞吐较好。随着 context
  进入百万 token，attention buffer 本身会先于数学 FLOPs 成为 capacity ceiling。
- **Changed Constraint / Mechanism:** UPipe 以 head chunks 处理 Q/K/V。设 query heads 为 `H`、
  context-parallel degree 为 `C`、每 stage 处理 `U` heads，要求 `U` 可被 `C` 整除；总 stage 数约为
  `H/U`，复用固定通信/attention buffer，使额外 buffer 从与 `H` 相关降为与 `U` 相关。GQA 下通过
  head ordering 避免同一 K/V group 被无谓重复通信。

  ```text
  all heads materialized
  -> split heads into stages
  -> All-to-All + attention per stage
  -> reuse bounded buffers
  -> concatenate output heads
  ```

- **State Ownership / Control and Data Flow:** FSDP/data-parallel mesh 拥有 parameter shards；context
  parallel ranks 拥有 sequence shards；UPipe scheduler 拥有 head-stage order 与 reusable buffers；
  collective runtime 拥有 All-to-All completion。Checkpointing、CPU offload、tiled CE/FFN 仍分别
  管理其他 activation/model-state pressure，UPipe 不会自动消除它们。
- **Implementation Details:** 作者基于 TorchTitan、FlashAttention-3 与 FSDP2 实现，并在 context
  dimension 使用 Ulysses，剩余 mesh 使用 Ring hybrid。论文只修改 attention execution，不改变
  attention 数学语义；不同 operation order 会带来小的 floating-point variation。
- **Evaluation Contract:** 8×H100 nodes，每卡 80 GiB，节点内第四代 NVLink 900 GB/s，节点间
  400 Gbps InfiniBand，Intel Xeon 8480+、约 1.9 TiB host memory。模型为 Llama3-8B 与
  Qwen3-32B，context-parallel degree 8；作者在 8 H100 上把 Llama3-8B 扩到 5M tokens，在
  16 H100 上到 8M，并对 Qwen3-32B 做百万 token 评测。精确 throughput 必须连同模型、长度、
  offload/checkpoint 与 head-chunk 配置读取，不能摘成通用倍率。
- **Baselines / Ablations / Sensitivity:** baseline 包括 DS-Ulysses、Ring Attention 与 FPDT。短
  context 时 UPipe 可能比 Ulysses 慢；更小 head chunk 降低 memory，却增加 kernel/collective launch
  和 pipeline overhead。FPDT 某些配置有更低 allocated GPU memory，但 CPU/offload overhead 更高、
  throughput 更低。释放的显存可用于减少 offload/checkpoint 或增加 batch，收益是 capacity headroom，
  不是保证单 step 更快。
- **What Evidence Proves / Does Not Prove:** 证明在披露的 H100/TorchTitan/model/mesh contract 中，
  head-wise staging 能突破 DS-Ulysses 的 attention-buffer capacity ceiling，并呈现清晰的
  memory-throughput trade-off；不证明 UPipe 在短 context、其他 topology、其他 head layout 或所有
  framework 中更快，也不证明长上下文训练只剩 attention buffer 一个瓶颈。
- **Trade-offs / New Failure Modes:** 新增 stage ordering、buffer reuse lifetime、collective launch、
  head/GQA divisibility 与 overlap tuning；stage 越细，capacity 越好但 latency/throughput 风险越大。
  传统 Ulysses 在 context 适中、buffer 可承受且希望减少 orchestration overhead 时仍合理。
- **Evolution / ROADMAP:** `Direct Refinement` of Ulysses implementation；Ch32/36 为主 owner 候选，
  Ch22/33/34 是边界。已读 Ch32 并确认本机制是 collective/buffer schedule 的条件化分支，不是新的
  collective 语义；Ch33～36 的相邻章节写入前复核尚未完成。
- **Integration Decision:** `Full Review Complete — Books Candidate / Memory-Throughput Trade-off`；
  Books Gate 关闭，本周不写入正文。
- **Open Questions:** 在跨节点多 rail、不同 GQA ratio 与 fault recovery 下，最优 `U` 是否能由
  runtime 动态选择？释放的显存用于减少 offload 与用于增大 batch，哪条路径提供更好的端到端
  tokens-per-dollar？

### DualPath

- **Candidate / Week / Score:** DualPath: Breaking the Storage-to-Prefill Network Bottleneck in
  Agentic LLM Inference / 2026-W09 / 29/30；`Source Family ID: agentic-kv-dual-read-path-2026`。
- **Source Type / Date / Revision:** arXiv systems paper；v1 2026-02-25，v2 2026-02-26。事件按
  v1 归档，v2 是同周 revision。
- **Direct Primary Sources / Full-read Coverage:** arXiv:2602.21548 metadata + HTML；已读
  Introduction、background、bottleneck measurement、architecture、traffic manager、scheduler、
  implementation、evaluation setup、全部 baseline/ablation/scaling 与 Discussion/Appendix。
- **Original Problem / Why Previous Design Was Reasonable:** 在传统请求或首轮长 prompt 中，
  external KV cache 主要由 Prefill worker 读取，`storage -> prefill` 是自然数据路径；Decode worker
  只需消费 handoff 后的 KV。对于轮数少、cache miss 高或 prefill compute 主导的 workload，这条单路径
  简单、ownership 清晰，也不必占用 Decode 网络和 buffer。
- **Changed Constraint / Mechanism:** 作者 trace 的目标 workload 平均 157 turns、平均 context
  32.7K tokens、每轮 append 429 tokens，并报告 98.7% KV cache hit。长多轮短增量使 Prefill compute
  很小、external KV read 反复发生，Prefill SNIC 饱和而 Decode SNIC 空闲。DualPath 增加
  `storage -> decode -> prefill` RDMA path，与原 `storage -> prefill` 并存；KV 按 layer streaming，
  并用小型 PE/DE DRAM buffer 解耦读取与转发。

  ```text
  single storage->prefill path
  -> observe asymmetric SNIC utilization
  -> add storage->decode->prefill path
  -> schedule reads across two paths
  -> isolate compute collectives from storage traffic
  ```

- **State Ownership / Control and Data Flow:** external KV store 拥有持久 block；central scheduler
  同时观察 GPU token queues 与 storage-read queues；Decode node 可暂存并转发 KV，但不能因此取得
  request 的最终 cache authority；Prefill node 只有在 layer data 到达并校验后才能消费。Traffic
  manager 以 CNIC-centric isolation 避免 collective burst 与 storage flow 在缺少 PCIe QoS 时互扰。
- **Implementation Details:** 作者在内部 inference stack 上修改约 5K LOC，使用 FlashMLA、
  DeepGEMM 与 DeepEP。系统的 exact implementation/source code 未公开；因此只能核验论文披露的
  architecture 与实验，不能把内部 stack 行为当成开源 runtime 的现成功能。
- **Evaluation Contract:** DeepSeek 27B、DeepSeek 660B、Qwen 32B；典型部署含 1P1D、2P4D、
  1P2D。Offline 以 JCT，online 以 TTFT/TTST/TPOT 为指标。论文报告相对内部 Basic baseline
  最高 1.87×；ablation 中 layerwise prefill 平均降低 17.21% JCT，dual path 进一步降低 38.19%，
  scheduler 后总降幅 45.62%。这些数字必须保留模型、P/D ratio、trace、network 与 baseline 条件。
- **Baselines / Ablations / Sensitivity:** 内部 Basic 是最可解释的增量 baseline。作者明确承认
  SGLang + HiCache + Mooncake 比较并不完全公平，且部分配置报错。1,152 GPU scaling 展示系统可运行，
  但没有在各自调优 worker ratio/parallelism 后证明大型 unit 比多个小 unit 有更高 cost-normalized gain。
- **Assumptions / What Evidence Proves:** bottleneck-free 分析假设 PCIe 配置充分、scheduler 能负载均衡、
  compute network 不拥塞、storage 已饱和。论文证明双 read path 可在作者的 long-turn/high-hit/PD/
  separate-fabric contract 中把闲置 Decode ingress 变成 KV I/O capacity；不证明所有 Agent traffic、
  单路径 PD 或 shared-NIC cluster 都应采用该拓扑。
- **Trade-offs / New Failure Modes:** 双路径新增 buffer capacity、queue coupling、flow ordering、
  backpressure、partial-transfer cleanup、Decode contention 与跨路径 fairness。作者讨论 working set
  可能随 tool-latency gap 呈二次增长、实验成本呈三次增长，但没有实证。原单路径在 cache miss
  较高、Prefill compute 较重、Decode network 忙或拓扑简单时仍合理。
- **Evolution / ROADMAP:** `Direct Refinement` of external-KV-aware PD serving；Ch51 主 owner 候选，
  Ch48、50、52 为 boundary。已读 Ch51 并确认它补充的是“workload 改变后 network path 也必须
  重规划”的受限机制，而不是推翻 PD break-even；相邻章节写入前复核尚未完成。
- **Integration Decision:** `Full Review Complete — Books Candidate / Workload-Topology Contract`；
  Books Gate 关闭，本周不写入正文。
- **Open Questions:** 当 storage、Prefill、Decode 共用 NIC/PCIe root complex 时，双路径是否仍有净收益？
  scheduler 如何在 TTFT、TPOT、storage queue 与 partial-transfer recovery 之间给出可审计决策？

### veScale-FSDP

- **Candidate / Week / Score:** veScale-FSDP: Flexible and High-Performance FSDP at Scale /
  2026-W09 / 29/30；`Source Family ID: ragged-shard-layout-contract-2026`。
- **Source Type / Date / Revision:** arXiv systems paper；v1 2026-02-25，v2 2026-02-27，v3
  2026-04-21。本周事件覆盖 v1/v2；当前 HTML v3 只用于 revision 与公开机制核验。
- **Direct / Related Primary Sources:** arXiv:2602.22437 metadata + HTML；volcengine/veScale
  官方仓库。论文称 RaggedShard 已开源，但仓库 README 同时明确这里只公开内部 veScale 的
  “small piece”，旧实现已移入 `legacy/`、新 veScale 仍在迁移，因此不能把论文 7.6K LOC backend、
  全部 production deployment 或 benchmark harness 视为完整可复现 artifact。
- **Full-read Coverage:** 已检查 Background、DTensor/JaggedTensor/FSDP 对比、RaggedShard、
  structure-aware planner 的优化问题和算法、DBuffer、end-to-end/scale/optimizer/planner/component
  evaluation、Lessons Learned、Conclusion 与官方 artifact 边界。论文没有独立 Limitations/
  Threats to Validity 章节，限制需从 setup、revision 和公开代码范围重建。
- **Original Problem / Why Previous Design Was Reasonable:** ZeRO/FSDP 的 element-wise 或 even
  row-wise shard 简单、与普通 element-wise optimizer 和 uniform tensor layout 兼容；在不要求
  block-wise quantization 或 matrix optimizer 时，这种规则布局便于 collective、checkpoint 与 API
  实现。新约束是 Muon/Shampoo 等操作需要完整 2D matrix，FP8/8-bit optimizer 又要求 quantization
  block 不跨 owner。固定 shard boundary 会迫使 model/optimizer 加 padding、copy 或额外 gather。
- **Changed Constraint / Mechanism:** RaggedShard 把“不可切分的原子单位”显式提升为 placement
  metadata，可按 element、row 或自定义 2D block 定义 granularity，并允许 devices 持有不等数量的
  blocks。它与 DTensor placements 组合；对 `Shard(0)` 引入 stride/reorder metadata，对其他维度用
  stride 与用户 granularity 的 LCM 防止切穿结构。

  ```text
  state sharding saves replicas
  -> fixed shard layout collides with block semantics
  -> RaggedShard preserves atomic block ownership
  -> planner permutes tensors and pads between tensors
  -> DBuffer binds planned layout to persistent zero-copy buffers
  ```

- **Planner / State Ownership:** planner 选择 uniform per-device buffer size `S` 与 tensor intervals，
  同时满足 block 不跨 shard、tensor contiguous、device load balanced，并最小化 padding/communication
  volume。问题 NP-hard；实现用 transformer-structure heuristics、DP 与 binary search，作者给出
  2-approximation 路径和一次性 planning overhead。DTensor 拥有 global tensor identity/placement；
  planner 拥有 layout；DBuffer 拥有 persistent pointer mapping、allocation 与 stream dependency；
  collective 负责 AllGather/ReduceScatter completion；checkpoint 仍依赖 global metadata。
- **Implementation Details:** DBuffer 对 grouped tensors 融合 add/scale/zero/copy，执行 batched
  allocation、in-place communication/computation，并让 parameter view 映射到持久 buffer，避免
  FSDP2 的 interleaved copy path。Muon case 选择 root，先把完整 matrix redistribute 到 root 做
  Newton–Schulz，再分发更新；这没有消除 gather，也新增 root load balancing 与完整 matrix capacity。
- **Evaluation Contract:** end-to-end 主要在 8×H800/node、80 GB HBM、节点内 400 GB/s NVLink
  cluster；scale/optimizer experiments 使用 NVIDIA Hopper cluster，但论文没有在相同粒度披露所有
  fabric details。Baselines 为 DeepSpeed ZeRO 0.17.6、PyTorch 2.7.1 FSDP1/FSDP2、
  Megatron-FSDP，均 ZeRO-3、FP32 master weights + BF16 forward/backward。Workloads 包括
  LLaMA-3-70B、GPT-OSS-120B 与 internal MoE，dense sequence 4096、MoE sequence 8192；
  GPT-OSS baseline OOM 时另报 SGD，不能与 AdamW 行直接等价比较。
- **Results / Ablations / Sensitivity:** 论文报告相对 baselines 5～66% throughput gain、16～30%
  peak reserved-memory reduction；范围跨模型与配置，不是单一 contract。32-GPU GPT-OSS-style
  8-bit Adam ablation 中，移除 DBuffer 后 normalized throughput 92.8%，移除 planner 后 65.4%，
  无 RaggedShard 被记为 N/A 而非可比较 baseline。Granularity 1/16 rows 时两个模型 padding 多数
  低于 3%；GPT-OSS 的 128-row case 可 spike 到 18%，说明 LCM、parameter layout 与 group size
  会制造离散 cliff。作者报告 planner <0.3s，但这是所测模型/规模的一次性 initialization cost。
- **Scale Boundary:** weak/strong/model scaling 说明该 stack 能在作者环境扩展到 10K GPUs；作者也
  明确小规模外推要求 topology、collective algorithm/protocol 与 bandwidth saturation 和目标规模相似，
  并以 HSDP/EP 限制 group size。2.4T/1K GPUs 与 production deployment 是作者证据，当前公开
  artifact 不足以独立复现全部规模结论。
- **What Evidence Proves / Does Not Prove:** 证明 sharding granularity 是 optimizer/quantization
  correctness 与 communication layout 的一等 contract，且 RaggedShard + planner + DBuffer 在作者
  workload 中同时减少 copy/padding/fragmentation；不证明所有 FSDP job 都应使用 ragged layout，
  不证明零拷贝没有 lifecycle cost，也不证明 headline 性能跨 fabric、model 或 PyTorch version 稳定。
- **Trade-offs / Previous Design Still Applies:** 灵活 layout 引入 placement metadata、planning、LCM
  cliff、pointer lifetime、checkpoint compatibility、root imbalance 与更复杂 debugging。普通 AdamW、
  规则 tensor shape、小 DP group 或 upstream interoperability 优先时，FSDP2/Megatron 的固定 layout
  仍可能更简单；planner 的收益只有在避免的 copy/padding/redistribution 大于新复杂度时成立。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of FSDP state lifecycle；Ch35
  主 owner，Ch32/36 为 handoff。已读 Ch35、Ch32、Ch36：现有正文完整覆盖 stage、collective 与
  checkpoint ownership，但没有把 shard layout granularity 与 optimizer/quantization semantics 连起来，
  属于真实机制缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Shard-Layout Contract`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** v1→v3 具体结论和公开代码范围变化是什么？不同 checkpoint backend 能否无损
  round-trip RaggedShard metadata？planner 在非 Transformer、不规则 multimodal tensor 与 elastic
  world-size 下怎样退化？

### General Agent Evaluation / Exgentic

- **Candidate / Week / Score:** General Agent Evaluation / 2026-W09 / 28/30；
  `Source Family ID: agent-evaluation-protocol-factorial-2026`。
- **Source Type / Date / Revision:** arXiv evaluation-systems paper；v1 2026-02-26，v2 2026-05-11；
  事件归 W09，当前 v2 用于 revision 核验。Presented at ICLR 2026 Workshop on Agents in the Wild。
- **Direct / Related Primary Sources:** arXiv:2602.22953 metadata + HTML；Exgentic official site、
  leaderboard、公开 code/config/traces 入口。站点是持续更新 artifact，当前排名不等于 v1 event-time
  snapshot；本 Review 以 paper 的 pinned versions、tables 与 released run contract 为证据边界。
- **Full-read Coverage:** 已检查 Unified Protocol、manual benchmark/agent adapters、orchestrator、
  benchmark/agent/model selection、metrics/statistics、全部 results、failure analysis、Discussion、
  framework/agent/benchmark adaptation、tool-shortlisting ablation、step counts、statistical appendix、
  reproducibility configuration、failure taxonomy/validation 与 Limitations。
- **Original Problem / Why Previous Design Was Reasonable:** Domain-specific harness 把 agent、tools、
  benchmark 与 protocol 一起定制，可以保护任务语义、减少 adapter ambiguity，也更容易做深度优化；
  但它无法区分表现来自 backbone、agent architecture 还是 per-benchmark glue。统一到一种 web/CLI
  transport 又会排除其他原生 agent/environment。
- **Changed Constraint / Mechanism:** Unified Protocol 只暴露 `task + context + typed actions`，并可
  指定 message/final-answer actions。每个 benchmark 从 reference agent 提取语义接口，每个 agent
  通过 wrapper 适配；Exgentic orchestrator 把双方作为 black boxes，在 isolated sessions 中执行。

  ```text
  benchmark-specific agent wiring
  -> canonical task/context/action mediation
  -> independent agent and benchmark adapters
  -> full model x architecture x benchmark factorial
  -> separate outcome, cost, zero-step and failure-taxonomy evidence
  ```

- **State Ownership / Control and Data Flow:** benchmark session 拥有 environment state 与 native scorer；
  agent wrapper 拥有 native protocol translation；orchestrator 拥有 session lifecycle、turn cap、action/
  observation queues 与 failure reason；run artifact 绑定 model version/defaults、agent version/prompt、
  adapter、task id、trajectory、native score 与 cost。Adapter 不是透明 plumbing，它是被评估对象的一部分。
- **Evaluation Contract:** 5 architectures × 5 LLMs × 6 benchmarks，100 tasks/benchmark，
  `tau²-Airline` 50，100-turn cap，共 150 configuration cells；模型使用 provider documented defaults，
  每 cell 单次运行，没有逐任务重复采样；总成本约 $20K。Benchmarks 覆盖 AppWorld、BrowseComp+、
  SWE-Bench Verified 与 `tau²` 三域，不覆盖 multimodal continuous-action/robotic environments。
- **Statistical and Comparison Boundary:** closed-source 15 configurations 的 cell success rate 分解中，
  model main effect 27.8%、architecture main effect 0.5%、interaction estimate 5.4%；加入两个
  open-weight checkpoints 后 architecture effect 可检测。此分解依赖所选 models、architectures、benchmarks
  与 aggregation，不是“模型永远比 harness 重要 58 倍”的系统定律。每 cell Wilson half-width 约
  7～13pp；specialist comparison 用 100-sample subset，而原 leaderboard 可能使用 full benchmark。
- **Ablations / Failure Evidence:** schema guard 与高分相关，但 architectures 同时有其他差异，属于
  observational pattern；tool shortlisting 是受控 ReAct ablation，在 AppWorld 的约 468 actions 中对
  4/5 models 提升、对 DeepSeek-V3.2 回退。GPT 5.2 的 128-tool API ceiling 导致多组 zero-score，
  说明 capability、API contract 与 adapter exposure 不能合并解释。2,868 个 failed trajectories 的
  27-category ErrorMap 分析显示 architecture-specific failure profiles，但分类仍需 judge validation，
  不等于逐例 causal ground truth。
- **What Evidence Proves / Does Not Prove:** 证明在这组 pinned systems 中，model、architecture、
  protocol compatibility 与 benchmark 发生强交互，aggregate score 会隐藏 zero-step/integration 与
  behavioral failures；不证明 general agents 在任意未知域等同 specialists，不证明 schema guard 因果增益，
  也不证明两个 open-weight checkpoints 代表整个 open-weight 类别。
- **Limitations / New Failure Modes:** 新 benchmark/agent 仍需开发 adapter；manual semantic extraction
  可能改变任务信息或 action shape；每 cell 单次随机运行无法估计 stochastic variance；native automated
  scorers 缺少人类 partial-credit review；provider defaults 牺牲了 tuned-best comparison；leaderboard
  演进还会引入 model/API drift。
- **Previous Design Still Applies:** 需要验证某一生产 workflow、风险策略或 domain-specific side effect
  时，深度定制 harness 仍合理；Unified Protocol 更适合隔离 architecture/model effects，不应强迫所有
  environment 丢失原生语义。二者是 `Layering / Dependency`。
- **Evolution / ROADMAP / Existing Coverage:** Ch62 主 owner，Ch63/69/75/77 为 handoff。已读 Ch62/63：
  现有 Evaluation System 已要求完整 subject identity、environment、trace 与 uncertainty，但尚未明确
  protocol adapter、zero-step integration failure 和 factorial model×architecture×benchmark 设计，属于
  可 refine 的机制缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Evaluation-Protocol Contract`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 怎样给 adapter 建立 semantic-equivalence tests？跨 provider tool/API ceiling 如何
  区分 model capability 与 interface opportunity？重复采样、human partial-credit 与 live leaderboard drift
  加入后，factorial conclusions 是否稳定？

### Test-Time Training with KV Binding Is Secretly Linear Attention

- **Candidate / Week / Score:** TTT with KV Binding Is Secretly Linear Attention / 2026-W09 / 27/30；
  `Source Family ID: ttt-kvb-linear-attention-reinterpretation-2026`。
- **Source Type / Date / Revision:** arXiv/ICML 2026 paper；v1 2026-02-24、v2 2026-02-27、
  v3 2026-05-04、v4 2026-05-12。事件按 v1 归档；当前 HTML v4 只用于 revision/机制核验。
- **Direct / Related Primary Sources:** arXiv:2602.21204 metadata + HTML；NVIDIA Research project
  page。项目页在本轮抓取未返回可检查正文/代码；论文说明实验基于 LaCT 与 ViTTT 的 official
  implementations，因此 artifact evidence 仅限作者披露与这些 upstream implementations，不能宣称
  本文提供了独立 end-to-end reproduction package。
- **Full-read Coverage:** 已检查 Related Work、TTT-KVB definition、四组反记忆实验、三个 theorem
  及证明、LaCT/ViTTT derivation、六步 reduction、parallel prefix formulation/equivalence、三任务
  experiment setup、non-reducible cases、Conclusion/limits。论文无通用独立 Limitations section，但
  结论明确限制在 KVB、linear bias-free final layer 与所测 LaCT/ViTTT。
- **Original Problem / Why Previous Design Was Reasonable:** TTT-KVB 在每个 token 用 `k -> v` 自监督
  loss 更新 fast weights，再以 `q` 读取更新后的 function；把它解释为 test-time storage/retrieval 很自然，
  也促使设计者增加 inner steps、optimizer capacity、momentum 与更深 MLP。若 inner objective 真代表
  写入质量，更低 inner loss 应至少不伤害 downstream task。
- **Changed Constraint / Empirical Contradictions:** 增加 inference-time inner steps 会降低 inner loss 却
  恶化 task；gradient ascent models 是从头按 sign-flipped inner loop 训练，表现仍相近；Q/K distribution
  在 NVS analysis 中不对称；把 Q 替换为 K 后所测 LaCT/ViTTT 仍接近 baseline。尤其 gradient-ascent
  实验不是对同一 checkpoint 临时翻转，因此证明的是 outer training 能吸收 update sign，而不是任意
  pretrained TTT 可在部署时改用 ascent。
- **Mechanism / State Ownership:** 若 inner function 末层为 linear、bias-free，写成
  `f(x)=phi(x;Theta)W`，一次 update 后输出可表示为：

  ```text
  o = q_hat (S0 + k_hat^T v_hat)
  ```

  多 token update 展开为历史 outer products 的累积；momentum 进入 effective value mixing。Fast-weight
  `W_t` 因此可看作固定大小、history-dependent linear-attention state，而不是可逐 key 精确回读的
  durable memory。若只更新末层并移除 weight normalization，kernel 固定且 update associative，可用
  parallel prefix；更新 dynamic kernel 或逐步 normalization 会破坏 associativity，必须保留递归执行。
- **Reduction / Alternatives:** 六步 reduction 依次只更新末层、移除 weight normalization、把多层
  MLP 降为 linear、移除 per-token learning rate、momentum 与 orthogonalization。最终得到标准 linear
  attention。论文自己的 ablation 显示并非全部组件无价值：NVS 从 deeper MLP 获益，LLM 从 gradient
  orthogonalization 获益；因此“可重写”不等于“复杂机制一定应删除”。
- **Evaluation Contract:** LaCT-LLM 760M，FineWeb-Edu 100B tokens，8×A100，20K iterations、
  约 56h，Book-3 2.5B-token perplexity；LaCT-NVS 114M，RealEstate10K，4×A100，20K iterations、
  约 38h、PSNR；ViTTT-B 90M，ImageNet-1K，2×H100，60 epochs、top-1 accuracy。其余
  hyperparameters 继承 upstream configs，论文没有披露通用 serving concurrency/SLO contract。
- **Results / Performance Boundary:** full reduction 相对原 TTT 在作者总结中只带来小幅 task degradation；
  某些指标在不同段落采用不同 reduction/comparison口径，不能混成单一数字。Parallel LaCT 在 single
  batch 的 **TTT layer attention calculation** 上最高 4.0× throughput，配合前两步 simplification
  带来 1.19× end-to-end training speedup；这不是完整 autoregressive service 的 4×，也没有跨模型、
  batch、length、hardware 与 SLO 的 production benchmark。
- **What Evidence Proves / Does Not Prove:** 证明满足 theorem assumptions 的 TTT-KVB 可以被解释为
  learned linear-attention operator，并为 LaCT/ViTTT 提供受限实验支持；不证明所有 test-time training、
  nonlinear-final-layer memory 或 end-to-end task adaptation 都是假记忆。Titans/Atlas 被作者判断满足
  assumptions，但因实现不可用未做经验验证，必须标 `Emerging` 而非已证实。
- **Trade-offs / Previous Design Still Applies:** linearization 提供更清楚的 state/parallelism contract，
  却可能牺牲 dynamic-kernel capacity、normalization stability 或 task-specific gains。真正需要在线适应
  distribution shift、end-task loss 或 nonlinear state transition 的 TTT 分支仍可能合理；外部 RAG/
  Agent Memory 继续拥有 provenance/delete semantics，也不被本论文替代。
- **Evolution / ROADMAP / Existing Coverage:** `Explanatory Correction` / `Direct Refinement` limited to
  TTT-KVB。Ch22 主 owner，Ch14/19 为边界。已读三章：Ch22 已把 test-time neural memory 写成独立
  分支并保留限制，但尚未区分“可学习 fast-weight state”与“可按 key 回读的 memory”；本论文可用于
  修正解释边界，不能删掉 Titans/MIRAS 演进路线。
- **Integration Decision:** `Full Review Complete — Books Candidate / State-Mechanism Reinterpretation`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** v1→v4 的 theorem/experiment wording 如何变化？Titans/Atlas 的公开实现能否验证
  reduction？在 long-context autoregressive serving 中，parallel form 的 state size、prefill/decode path、
  numerical stability 与 end-to-end latency 是否仍优于 tuned linear-attention baseline？

### Agents of Chaos

- **Candidate / Week / Score:** Agents of Chaos / 2026-W09 / 26/30；
  `Source Family ID: live-agent-authority-state-security-2026`。
- **Source Type / Date / Revision:** exploratory red-teaming report，arXiv v1 2026-02-23，无后续
  revision。已读 84 页 PDF 的 setup、evaluation method、11 个成功攻击 case、5 个未按攻击者预期
  展开的 safety cases、Discussion、Related Work、Conclusion 与决定 evidence boundary 的 Appendix；
  联读作者 interactive report、Discord/session-log 入口和 OpenClaw repository。
- **Access / Artifact Boundary:** 作者页面开放 case-level evidence 与经脱敏的部分 logs；当前 OpenClaw
  repository 会继续演进，论文也记载研究期间曾升级 runtime，因而不能用现行代码反推当时 exact
  commit/config。原始 email、credential 与全部 provider-side state 不公开，artifact 支持事件复核，
  不是精确 replay package。
- **Original Problem / Why Previous Design Was Reasonable:** isolated chat benchmark 易控制、可统计，
  也避免真实副作用；但 Agent 一旦同时拥有 persistent memory、email/Discord、filesystem、shell、
  cron 与多方互动，安全对象从单轮文本变成跨 channel 的 principal、state 与 effect chain。用自然语言
  表达 owner、policy 与 persona 在低权限助手中成本低，却不足以承担系统授权。
- **Evaluation Contract:** 六个 OpenClaw Agent 运行于隔离 VM，各有 20GB persistent volume；四个使用
  Kimi K2.5、两个使用 Claude Opus 4.6。20 名研究者在两周内进行开放式 benign/adversarial 互动；
  Agent 拥有 unrestricted shell，部分拥有 sudo，且可修改自己的 markdown instructions/memory。
  多数行动仍由人触发，配置过程大量依赖人工；heartbeat/cron 在研究期内有 bug。方法目标是寻找
  counterexample，不是随机抽样或估计 failure rate。
- **Mechanism / State Ownership:** 失败集中在四条没有被 runtime 显式拥有的边界：
  1) display identity 与 authenticated principal 混合，跨 channel 后 owner authority 可被重建；
  2) untrusted conversation、retrieved document 与 mutable instruction/memory 共处语言上下文，外部内容
  可持久改变后续 policy；3) Agent self-report 被当成 effect truth，真实 email/file/process state 没有
  独立 postcondition；4) audience、resource 与 delegation 没有 typed model，private reasoning 仍可经
  file、tool output 或公共 channel 泄露。跨 Agent teaching 又使 capability 与 compromised practice
  共享同一传播路径。
- **Observed Evidence / Positive Controls:** 报告给出 non-owner compliance、PII forwarding、owner
  spoofing、unbounded loop/storage、mutable “constitution” propagation 和 report-vs-state mismatch 的
  具体 counterexamples；也记录多次 injection/refaming refusal、API boundary preservation 与跨 Agent
  safety warning。正反结果共存说明风险不能简化为“模型总会服从攻击”。
- **What Evidence Proves / Does Not Prove:** 证明在该高权限、低约束 live-lab configuration 中，上述
  failure modes 可以发生，并揭示 model、scaffold、channel 与 authority 的组合风险；不证明任一模型
  的总体攻击成功率，不比较六个 Agent 的因果安全差异，也不证明所有问题都是 foundation-model
  defects。开放式参与、case selection、运行中升级、人工干预与 post-window case 使频率和模型排名
  都不可识别。
- **Trade-offs / Previous Design Still Applies:** 更强 authentication、least privilege、approval、resource
  quota、immutable policy 和 effect verification 能消除多项 contingent failures，却增加交互摩擦、
  recovery state 与 operator load；prompt injection 和 audience 理解仍可能保留模型层脆弱性。低权限、
  单用户、短生命周期助手继续适合较轻 contract；高副作用 Agent 必须把 authority 与事实状态移出
  conversation。二者是 `Direct Evolution`，不是一律禁止 autonomy。
- **Evolution / ROADMAP / Existing Coverage:** Ch68 主 owner，Ch62/77/78/80 为 handoff。已读 Ch68、
  Ch77、Ch78、Ch80：现有内容已覆盖 tool executor、least privilege、durable state、delegation 与
  coordination tax，但尚未把 authenticated principal、channel audience、mutable behavioral state、
  postcondition evidence 和 cross-agent propagation 组合成一条 security contract，存在可 refine 缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Authority-State-Effect Contract`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** exact runtime revision 与 per-case configuration 如何固定？怎样为 owner、audience、
  mutable instructions 和 side effect 建立统一 label/taint model？在 least-privilege deployment 与更多
  model families 上，哪些 failure 仍能复现？

### ARLArena / SAMPO

- **Candidate / Week / Score:** ARLArena / 2026-W09 / 26/30；
  `Source Family ID: multi-turn-agent-rl-stability-2026`。
- **Source Type / Date / Revision:** arXiv/ICML 2026 paper；v1 2026-02-25、v2 2026-03-07、
  v3 2026-07-04。事件按 v1 归档；当前 v3 PDF 用于机制、追加实验与 revision 核验。已读 27 页
  全文，包括 policy-gradient decomposition、standardized recipe、SAMPO、四任务实验、staleness、
  8B validation、prompt/rollout examples 与关键 Appendix；联读 official ARL-Arena code repository。
- **Artifact Boundary:** repository 提供 verl-based agent system、recipes、environment preparation 与
  training 入口，README 固定 Python 3.11、verl 0.4.0、PyTorch 2.6.0、vLLM 0.8.5；但公开页未提供
  本轮可核对的 commit-to-paper mapping、完整运行日志或逐 seed 结果，因此是 mechanism artifact，
  不是 headline 的独立复现。
- **Original Problem / Why Previous Design Was Reasonable:** GRPO/PPO-style token clipping、group
  advantage 与 filtering 源自单轮 reasoning，目标清楚且实现简单。Multi-turn Agent rollout 却把
  action format、environment transition、variable length 与多个 policy update 连成 trajectory；同一
  token-local 规则可能保留看似正常的 loss，同时让整条失败 trajectory 在 off-policy drift 下主导更新。
- **Decomposition / Mechanism:** 论文把 Agent policy gradient 分成 loss aggregation、importance-sampling
  clipping、trajectory filtering/resampling 与 advantage design。稳定 testbed 先做 behavior cloning，
  再加入 format penalty、必要的 KL regularization 与 method-specific tuning。分析观察到 collapse 时
  negative-advantage、low-IS-ratio sequence 的 KL share 突增；sequence-level ratio/masking 比单纯增大
  KL 或 mini-update batch 更直接地截断该路径。SAMPO 组合 sequence-level clipping、episode+anchor-
  state step advantage 与仅保留非全同 reward group 的 dynamic filtering。
- **Control / Data Flow:** environment rollout 生成完整 multi-turn trajectory，runtime 再切成 single-turn
  samples；reward/group identity、behavior-policy logprob 与 anchor state 共同进入 advantage/ratio。
  这使 trajectory segmentation、policy version 与 environment state 成为算法语义，而非仅是吞吐实现。
  Batch 内后续 mini-update 若消费较旧 rollout，会放大 staleness；降低 rollout-to-update lag 因此与
  objective design 同属稳定性 contract。
- **Evaluation Contract:** ALFWorld、WebShop、Sokoban、TIR Math；policy 主要为 Qwen3-4B base/RFT，
  另用 Qwen3-8B 检查趋势；NVIDIA H200/B200，verl rollout + vLLM。最大 interaction steps 分别为
  50/15/15/5，group rollout size 8/8/8/5，prompt/response limits 与 KL、learning rate、mini-batch
  均按任务不同。作者还比较 GRPO、GSPO、CISPO、SAPO、GIGPO、EMPG、DAPO variants；closed-model/
  debate 对比没有形成同训练预算、同模型能力的因果实验。
- **Ablation / Evidence:** sequence-level masking 可使原先 collapse 的 tolerant-clipping variants 恢复，
  GIGPO 的 step-level signal 能缓解稀疏 reward；dynamic filtering 与 GRPO 结合时反而可能删掉早期
  all-failure group 中的 format-learning signal，只有与更丰富 advantage 配合才较稳定。增加 staleness
  在作者设定中使 ALFWorld 与 math 指标下降；loss aggregation 对不同 task/length variance 呈相反方向。
  因此单一“新 optimizer 更稳”的总结会丢掉组件交互。
- **What Evidence Proves / Does Not Prove:** 支持在所测 Qwen3-4B/8B、四环境和 recipe 下，trajectory-
  aware ratio、credit 与 filtering 的联合设计比直接移植单轮配置稳定；不证明 SAMPO 普遍优于所有
  PPO/GRPO implementations，不证明 sequence-level clipping 对任意 reward/horizon 必要，也不证明
  与 frontier API/MAS 的 score 差异来自训练算法而非 model、prompt、tool 或 opportunity contract。
- **Trade-offs / Previous Design Still Applies:** sequence-level控制降低 harmful trajectory 的影响，却
  可能把少量关键 token 与整条 sequence 一起屏蔽；step advantage 要求可对齐的 environment state；
  filtering 提升有效 batch density，也可能删除 early curriculum signal；低 staleness 要付出更紧耦合的
  rollout/update pipeline 与较少复用。单轮、短 horizon、dense reward 仍可使用较简单 GRPO/PPO。
- **Evolution / ROADMAP / Existing Coverage:** Ch29 主 owner，Ch25/33/62/77 为 handoff。已读 Ch29：
  现有章节已经警告同名 GRPO 的 aggregation、clipping、rollout version 与 reward 差异，也覆盖 partial
  rollout；缺口是 multi-turn environment 中 trajectory-level IS、step credit、filtering/format interaction
  与 staleness 的联合演进，可作为 `Direct Refinement`，不是用 SAMPO 覆盖 GRPO。
- **Integration Decision:** `Full Review Complete — Books Candidate / Multi-Turn Optimization Contract`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** v1→v3 的方法与实验差异是什么？不同 seed、model family、continuous reward 与
  asynchronous rollout 下 collapse attribution 是否稳定？sequence mask、rollback 与 partial-rollout
  resume 怎样共享 trajectory identity？

### SkillOrchestra

- **Candidate / Week / Score:** SkillOrchestra / 2026-W09 / 25/30；
  `Source Family ID: skill-conditioned-agent-routing-2026`。
- **Source Type / Date / Revision:** arXiv paper，v1 2026-02-23，无后续 revision。arXiv HTML 不可用；
  已读 42 页 PDF 的 Related Work、formalization、handbook learning/refinement/selection、routing
  algorithm、十项 benchmark、transfer/ablation、implementation Appendix 与案例；联读作者 GitHub。
- **Artifact Boundary:** repository 提供 `explore → learn → select → test` pipeline、SGLang/model endpoints、
  Qwen3-Embedding/FAISS retriever 与 pool/pricing/config入口。它提高机制可检查性，但 paper-run commit、
  API responses、pricing snapshot 与完整 trajectory outputs 没有在 README 中固定；涉及 proprietary
  endpoints 的结果不能由代码仓独立重放。
- **Original Problem / Why Previous Design Was Reasonable:** query-level router 便宜、稳定，适合一次性
  model selection；end-to-end RL router 能观察多轮 state，却训练昂贵，agent pool 或价格变化后需要
  重新适配，并可能 collapse 到单一强模型。新约束是 workflow 每一步所需 capability 会变化，而
  model/tool competence 与 cost 也在演进。
- **Mechanism / State Ownership:** Skill Handbook 把 orchestration state 分成 mode-level transition/use
  insights、hierarchical skill registry 与 agent profiles。系统对同题/同 mode 的成功和失败 traces 做
  contrast，由 LLM discoverer 抽象 capability gap；每个 agent-skill 用 Beta posterior 累积 success/failure，
  再按 profile variance split 过宽 skill、合并冗余 skill。validation 在 performance-cost 平面为目标
  orchestrator 选择 handbook 子图，避免低能力 orchestrator 被过细 taxonomy 误导。
- **Runtime Control Flow:** 每一步先基于 current interaction state 选择 Search/Code/Answer 等 mode，
  再识别 active skills，以 posterior competence 与 mode-specific cost 的加权目标选择 agent；可按 query
  embedding 追加近邻 skills。`lambda_cost` 与 handbook/version 决定选择边界，因此 state owner 应是
  platform/control plane，不是 Agent 自述或不可追溯的 prompt context。
- **Evaluation Contract:** model-routing 使用 Qwen2.5-3B orchestrator、六模型 pool，覆盖 NQ、TriviaQA、
  PopQA、HotpotQA、2Wiki、Musique、Bamboogle、MATH、AMC；最多四次外部 model call，低数据 regime
  每 dataset 的 train/validation 各少于 50 samples。agent-orchestration 使用 Qwen3-8B、FRAMES、
  Search/Code/Answer 三 mode、最长 50 turns，并固定 Tavily、FAISS/Qwen3-Embedding、Python sandbox
  与一组 open/proprietary models；accuracy 由 GPT-5-mini judge，cost 由当时 USD price 计算。
- **Ablation / Evidence Boundary:** 作者报告 handbook transfer 到多个 orchestrator backbone 且无需重新
  学习；100 个 FRAMES tasks 的 ablation 显示 no-handbook、no-refinement/selection、coarse skills 与
  full system 在 accuracy/cost 上不同。该结果支持 granularity 与 competence/cost profile 有用，但样本小、
  judge/model/API/pricing version 会漂移；“700×/300× learning cost reduction”比较的是特定 RL baseline
  的训练路径，不是所有 routing 方法的总拥有成本。
- **What Evidence Proves / Does Not Prove:** 证明在所测 pool/benchmark 中，从 trace 派生的显式 skill
  state 可形成较好的 performance-cost frontier，并能跨部分 orchestrator backbone 重用；不证明 LLM
  抽取的 skill 是 causal ground truth，不证明 posterior 在 task/model drift 后仍校准，也不证明 handbook
  transfer 到新工具、权限域或未知 workflow 时无需再验证。
- **Trade-offs / New Failure Modes:** 显式 taxonomy 带来解释、更新和 cold-start reuse，却新增 skill
  alias/merge 错误、sparse profile、stale cost、selection overfit、embedding 误召回与 compromised trace
  poisoning。End-to-end RL 在 reward 可定义、pool 稳定且 interaction pattern 复杂时仍可能更合适；静态
  router 在短任务和低控制面成本场景继续成立。三者是并行 design branches。
- **Evolution / ROADMAP / Existing Coverage:** Ch80 主 owner，Ch75/77/78 为 handoff。已读四章：Planning
  已有可验证 decomposition，Workflow 拥有 durable state，Multi-Agent 要求 task-topology matching，
  Agent Platform 已管理 definition/run/Skill artifact；但尚未区分“可安装 Skill asset”与“由 traces
  派生、按 agent pool/version 校准的 routing skill state”，存在可 refine 的 control-plane 缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Skill-Competence Routing State`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** profile 的 decay/uncertainty 与 drift detector 如何设计？失败 trace 被攻击或 judge
  错判时如何回滚 handbook？model/API/price/tool version 变化后，何时只更新 profile、何时重做 skill
  discovery 与 Pareto selection？

### GUI-Libra

- **Candidate / Week / Score:** GUI-Libra / 2026-W09 / 25/30；
  `Source Family ID: gui-partial-verifiability-policy-update-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-25，v2 2026-05-25。事件按 v1
  归档；v2 仅用于核验 revision、完整 method、proof 与追加实验，不改变历史事件日期。
- **Direct / Related Primary Sources:** arXiv:2602.22190 metadata + v2 HTML；GUI-Libra 官方
  repository。仓库含 SFT、EasyR1 接入、reward functions 与 evaluation 入口，但没有以不可变 tag
  绑定 v1 论文表格、训练数据和模型，因此提供机制可检查性而不是独立复现实验结论。
- **Full-read Coverage:** 已检查 Introduction、Related Work、POMDP formalization、offline data、
  action-aware SFT、partial-verifiability theory、KL trust region、success-adaptive negative gradient
  scaling、reward design、全部实验/ablation/implementation、Limitations、proofs 与案例 Appendix。
- **Original Problem / Why Previous Design Was Reasonable:** GUI imitation data 通常只记录一条成功
  action；把演示动作视为唯一正确标签，适合 action space 较窄、状态近似完全可观测的 supervised
  learning。进入 online RL 后，同一 screen state 可能有多条有效路径；只奖励示范动作会把未被展示的
  有效动作当负例，而长 horizon 又放大 state-occupancy drift。问题不是简单的 label noise，而是
  verifier 只观察 success 的一个子集。
- **Changed Constraint / Mechanism:** action-aware SFT 先保留示范 action 附近的行为；online stage
  再以 KL trust region 约束 policy drift，并只对 negative-advantage samples 使用 success-adaptive
  scaling，降低 partial verifier 对可能有效但未证实动作的过强惩罚。其演进关系是：

  ```text
  single demonstrated action as target
  -> recognize multiple valid but partially verified actions
  -> constrain occupancy drift with KL
  -> scale only negative updates by observed group success
  -> retain exploration without treating every unseen action as correct
  ```

- **State Ownership / Control and Data Flow:** environment 拥有 screen/UI state 与真正 side effect；
  dataset 只拥有一条 demonstrated trajectory；verifier/reward code 拥有可观测 success signal；rollout
  group 产生相对 advantage；trainer 拥有 reference-policy KL、negative-gradient scaling 与 checkpoint
  version。Policy 不能根据自己的自然语言解释把 action 宣告为 valid，runtime 也不能把任务成功等同于
  side-effect 安全。
- **Implementation Details:** 训练以 VERL/EasyR1、FSDP 与 vLLM 为基础，官方代码公开对应 reward
  与训练入口。论文中的 theorem 依赖 occupancy/support 等假设；工程实现并不会自动验证这些假设，
  因此理论解释和 production guarantee 必须分开。
- **Evaluation Contract:** Qwen2.5-VL 3B/7B 与 Qwen3-VL 4B/8B；8×B200、BF16、300 iterations、
  global batch 128、group size 8、prompt 8,092、response 1,500、temperature 1；默认 KL 0.001，
  7B 为 0.005。Offline 数据来自 MM-Mind2Web-v2/AndroidControl-v2；online evaluation 覆盖
  AndroidWorld、WebArena-Lite-v2 与 Online-Mind2Web，后者使用 o4-mini/WebJudge-7B judges。
- **Baselines / Ablations / Sensitivity:** paper 将 ASFT、KL 与 scaling 拆开，并检查不同 model sizes、
  offline/online domains 与 KL sensitivity。结果支持三个组件在所测 recipe 中互补；它没有建立
  “KL-GRPO 对所有 GUI RL 必要”的一般性结论，也未把 judge variance、真实副作用或 cross-app
  permission failures 纳入完整 verifier contract。
- **What Evidence Proves / Does Not Prove:** 证明 partial verifiability 可使 naive negative updates 与
  long-horizon occupancy drift 耦合，且受控 trust-region/scaling 在作者 contract 中改善结果；不证明
  所有未匹配示范的动作都有效，不证明 benchmark success 等于生产 GUI 操作正确，也不证明作者
  benchmark 可跨硬件、model family 或 verifier 直接外推。
- **Trade-offs / Previous Design Still Applies:** KL 过强会抑制探索，过弱不能控制 drift；negative
  scaling 可减少 false punishment，也可能保留真实坏动作；group success 又受 sample count 与 reward
  sparsity 影响。动作唯一、verifier 完整或 side effect 风险高时，严格 imitation/allowlist 仍然合理。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of GRPO under partial
  verifiability；Ch29 主 owner，Ch25/62/74/77 为 handoff。已读 Ch28～30 与 Agent evaluation/tool/
  workflow 邻章；现有 Ch29 覆盖 group-relative optimization、clipping 与 reward contract，但没有把
  “多有效 action + 单演示标签 + occupancy drift”写成独立 policy-update contract。
- **Integration Decision:** `Full Review Complete — Books Candidate / Partial-Verifiability
  Trust-Region Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 当 verifier coverage、side-effect severity 与 rollout diversity 可估计时，KL 与
  negative scaling 能否由风险预算联合控制？如何识别被保留的是合法 alternative 还是 reward gap？

### Revisiting Text Ranking in Deep Research

- **Candidate / Week / Score:** Revisiting Text Ranking in Deep Research / 2026-W09 / 25/30；
  `Source Family ID: agentic-ranking-query-unit-reader-contract-2026`。
- **Source Type / Date / Revision:** arXiv/SIGIR 2026 paper，v1 2026-02-25；本轮读取完整 HTML、
  tables、failure discussion 与官方 artifact。未发现会改变本周归属的 earlier public version。
- **Direct / Related Primary Sources:** arXiv:2602.21456 + 作者 repository。artifact 提供 corpus/index、
  encrypted traces 与运行脚本，但没有不可变 paper-run tag、完整 seed/GPU disclosure 或所有 API state；
  可用于检查 pipeline，不等于本轮已独立重跑实验。
- **Full-read Coverage:** 已检查 Introduction/Related Work、agentic retrieval pipeline、query and
  document representations、five retrievers、three rerankers、all result matrices、depth/unit/query
  analyses、failure cases、limitations/conclusion 与 repository contract。
- **Original Problem / Why Previous Design Was Reasonable:** 传统 ranking benchmark 给定短 query，
  对固定 document/passages 排序；BM25 或单阶段 dense retrieval 成本低、容易缓存和解释。Deep Research
  Agent 会反复生成带推理痕迹、答案草案或先前 evidence 的查询，并把 top results 喂给有限 context
  reader。此时 ranking 的输入分布和消费方都变了，离线 relevance 不能单独代表 workflow utility。
- **Changed Constraint / Mechanism:** 论文系统比较 query-to-document 与 query-to-query retrieval、
  raw query 与 `query + reasoning` 表达、document/passages、五种 first-stage retrievers、三种 rerankers
  及不同 rerank depth。核心不是宣布一个 universal winner，而是把 ranking identity 扩展为：

  ```text
  agent query dialect + retriever training distribution
  + retrieval unit and length normalization
  + reranker and rerank depth
  + reader context budget
  -> evidence opportunity seen by the research workflow
  ```

- **State Ownership / Control and Data Flow:** Agent 生成 query 与 reasoning state；retrieval index 拥有
  document/passages 和 embedding/version；retriever/reranker 拥有各自 training distribution、tokenization
  与 score semantics；workflow runtime 拥有 depth、dedup、context budget 与 trace；reader 只消费被选中的
  evidence。Query rewriting 不能覆盖原 query，必须作为有 lineage 的新检索状态。
- **Evaluation Contract:** BrowseComp-Plus 830 queries；agents 为 gpt-oss-20b 与 GLM-4.7-Flash 30B，
  使用 vLLM 0.15、max output 40K、最多 100 iterations，每次读取 top-5 × 512 tokens。First stage 为
  BM25、SPLADE、RepLLaMA、Qwen3-Embed、ColBERT；rerankers 为 monoT5、RankLLaMA、Rank1；depth
  10/20/50。GLM matrix 因 GPU 限制不完整，系统性 Q2Q 分析主要在 gpt-oss 上完成。
- **Baselines / Sensitivity / Failure Evidence:** `Q2Q(query + reasoning)` 对部分 neural rankers 有益，
  却可能伤害 BM25；没有一个 reranker 在所有 query form、unit、depth 上稳定占优。BM25 document-level
  结果对 length normalization 和在完整 evaluation set 上调参敏感，作者明确提示潜在偏置。因此这些
  表格是 interaction evidence，不是 “BM25 universally wins” 或 “passages always win”。
- **What Evidence Proves / Does Not Prove:** 证明 Agent-generated query distribution、ranker training
  distribution、unit 和 reader budget 的失配能改变 end-to-end answer opportunity；不证明该结果跨语种、
  web freshness、其他 Agent/reader 或生产 latency/cost SLO 仍成立，也没有隔离所有 query generation
  与 final-answer variance。
- **Trade-offs / Previous Design Still Applies:** query expansion 提高语义召回但会注入错误 reasoning；
  passage 减少 length bias 却丢失 document context；更深 rerank 增加 recall opportunity，也消耗 latency、
  GPU 与 reader budget。短 query、稳定 corpus、严格 latency SLO 下，BM25/浅层 rerank 仍是合理分支。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of Agentic RAG；Ch72 主 owner，
  Ch62/71/77 为 handoff。已读 Ch71～73、Ch62 与 Ch77：现有 Ch72 已覆盖 chunking、hybrid retrieval、
  reranking 与 sufficiency，但尚未把 Agent query dialect、ranker training distribution、retrieval unit、
  reader budget 合成一个可版本化 contract。
- **Integration Decision:** `Full Review Complete — Books Candidate / Agentic Ranking Contract`；
  Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 如何在不泄露 reasoning 的前提下记录 query dialect？ranking offline metric 怎样与
  answer correctness、citation support、latency 和 token budget 建立可校准的 multi-objective link？

### SWE-Protégé

- **Candidate / Week / Score:** SWE-Protégé / 2026-W09 / 25/30；
  `Source Family ID: coding-agent-learned-escalation-follow-through-2026`。
- **Source Type / Date / Revision:** arXiv paper，v1 2026-02-25，无后续 revision；已完整阅读 34 页
  PDF，包括 formalization、两阶段训练、reward/curriculum、experiments、ablations、limitations、prompts、
  hyperparameters 与案例 Appendix。
- **Access / Artifact Boundary:** paper mechanism verified；本轮未定位到作者公开 repository、weights
  或 immutable run logs。搜索结果中的非作者镜像/项目页不作为证据。因而只能核验论文披露，不能宣称
  代码级复现或把实现细节补成公开事实。
- **Original Problem / Why Previous Design Was Reasonable:** 强模型全程执行 coding task 能减少 delegation
  boundary，却昂贵；小模型全程独立运行成本低，但容易在 command loop、错误诊断和 patch verification
  上停滞。固定在开头询问 expert 或随机调用实现简单，却无法把稀缺 advice 分配给真正卡住的状态。
- **Changed Constraint / Mechanism:** 学生先以 expert-augmented successful trajectories 做 SFT，再用
  GRPO 学习何时调用 `ask_expert_llm` 以及如何使用建议。reward 不只奖励最终 patch，还惩罚重复 command
  loop、衡量 expert call 是否 warranted，并奖励 advice 后的 follow-through；curriculum 先学减少 loop，
  再学执行建议。演进不是“加入第二个 Agent”，而是：

  ```text
  fixed or no escalation
  -> expose bounded advisory tool
  -> detect stalled trajectory
  -> request advice with projected history
  -> preserve student action authority
  -> verify follow-through and final patch
  ```

- **State Ownership / Control and Data Flow:** student Agent 始终拥有 shell/edit/test action authority；
  expert 只返回 tagged observation，无权直接修改 workspace。Runtime 拥有 max expert calls、history-tail
  projection、Docker state、75-step budget 与 test execution；reward pipeline 拥有 loop detection、call
  warrantedness、follow-through 和 patch correctness。Advice 必须绑定 request、history projection、expert
  model/version 与后续 actions，才能审计“问了什么、为何问、是否照做、结果怎样”。
- **Implementation / Training Contract:** Qwen2.5-Coder-7B；Phase I 使用约 4.9K expert-augmented
  trajectories；Phase II 在 100 个 SWE-Gym tasks 上 GRPO，6 rollouts、batch 16、160 steps，使用
  8×A100/H100 80GB。SWE-agent 设 75 steps、禁用 test-time scaling，默认最多 6 次 expert calls；
  experts 覆盖 Claude Sonnet 3.7/4.5 与 Opus 4.1，evaluation 为 SWE-bench Verified。
- **Ablations / Comparison Boundary:** 仅减少 loops 对 correctness 帮助有限，follow-through shaping
  才补上“收到 advice 但未执行”的断点；fixed/random invocation 弱于 learned policy；history projection
  会改变触发价值。部分 baseline 数字来自 SWE-smith 而非同环境重跑，成本又依赖当时 API pricing，
  所以不能将 headline 写成“7B 普遍击败 32B”或把 expert token cost 当作整套系统 TCO。
- **What Evidence Proves / Does Not Prove:** 证明在该 Python-heavy SWE-agent/SWE-bench contract 中，
  escalation timing 与 follow-through 可以被显式训练并提升 bounded collaboration；不证明该 policy 能
  跨语言、repo size、tool stack 或 expert family 泛化，也不保证 expert advice 正确、无 prompt injection
  或低于人类 review 风险。
- **Trade-offs / Previous Design Still Applies:** 稀疏 expert call 降低平均成本，却新增 context projection
  丢失、advice provenance、bad-advice propagation、budget exhaustion 与 silent non-follow-through。
  高风险变更仍需 deterministic policy/human approval；简单任务继续由小模型独立完成，全程强模型在
  escalation overhead 大于节省时仍合理。
- **Evolution / ROADMAP / Existing Coverage:** `Layering / Dependency` on workflow recovery；Ch77 主
  owner，Ch74/76/78 为 handoff。已读 Ch74～78：现有 Workflow 覆盖 durable state、retry、approval 和
  compensation，但没有把 learned escalation 与 follow-through 作为两段独立 transition；Ch78 的 peer
  Multi-Agent topology 不是主 owner，因为 expert 没有行动权。
- **Integration Decision:** `Full Review Complete — Books Candidate / Learned Escalation and
  Follow-through Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 如何给 expert advice 建立 confidence、provenance 与 rollback？history projection
  多大才足以判断 stall？当 expert 与 verifier 冲突时，谁拥有最终 escalation/abort authority？

### EMPO²

- **Candidate / Week / Score:** Exploratory Memory-Augmented LLM Agent via Hybrid On- and
  Off-Policy Optimization / 2026-W09 / 25/30；
  `Source Family ID: temporary-memory-exploration-self-distillation-2026`。
- **Source Type / Date / Revision:** arXiv/ICLR 2026 paper；v1 2026-02-26，v2 2026-03-06。
  事件按 v1 归档；本轮以 v2 HTML、ICLR/OpenReview 版本与 Appendix 核验完整机制和 revision。
- **Direct / Related Primary Sources:** arXiv:2602.23008、OpenReview paper、作者 project page 与
  Microsoft Agent Lightning 当前 EMPO² integration。官方代码可检查 multi-step environment、memory
  server 与训练入口，但 main branch 不是 paper-run immutable snapshot，不能据此宣称复现实验表格。
- **Full-read Coverage:** 已检查 exploration problem、GRPO preliminaries、self-generated memory、三种
  rollout/update mode、importance-ratio解释、ScienceWorld/WebShop setup/results、OOD adaptation、mode/
  intrinsic-reward ablations、p/q sensitivity、pseudocode、prompts、implementation、cost analysis、
  reproducibility/safety statements 与 qualitative tips。
- **Original Problem / Why Previous Design Was Reasonable:** 普通 on-policy GRPO 让每批 trajectory 只经
  scalar return 影响参数；在任务可由 pretrained prior 覆盖、奖励较密时，保持 rollout/update distribution
  一致更简单也更稳定。Hard exploration 环境中的失败却可能发现新 state/action，若 trajectory 间没有
  可读连续性，下一批仍会重复同一高置信错误。
- **Changed Constraint / Mechanism:** policy 从 rollout 自己生成 tips，写入外部 memory；后续 rollout
  可带或不带 retrieved tips。带 tips 的 trajectory 一部分保持同 conditioning 做 on-policy update，另一部分
  在 update 时移除 tips，以 advantage 加权方式把 scaffold 下发现的行为蒸馏到 no-tip policy：

  ```text
  scalar reward only across rollouts
  -> summarize trial into retrievable tips
  -> use tips to reach novel states
  -> learn tip-conditioned behavior on-policy
  -> selectively distill useful behavior into no-tip policy
  -> keep memory available for fast OOD adaptation
  ```

- **State Ownership / Control and Data Flow:** environment 拥有真实 transition/reward；rollout worker
  拥有 trajectory/log-prob/policy version；memory service 以 task/buffer identity 存 tip、embedding、score、
  insertion order，并执行 threshold/retrieval/eviction；trainer 决定 memory/no-memory rollout 与 update
  mode。Tip 是 policy-derived hypothesis，不是 environment truth；写入、检索、蒸馏与删除都应保留 lineage。
- **Implementation Details / Ambiguity:** v2 示例 memory buffer 去重 exact text、最多保留 1,000 条，
  cosine threshold `>0.5` 后按 score 返回 top-10。论文 prose、pseudocode 与 cost appendix 对 `p/q` 哪个
  分支概率的符号存在不一致，current integration 也不是 pinned paper run；因此 branch probability 必须
  从实际 config/log 核验，不能只凭符号复述。
- **Evaluation Contract:** Qwen2.5-7B-Instruct；ScienceWorld 19 tasks、30 steps、32 tokens/step、
  4,500 total response tokens、group 8、mini-batch 16、LR `1e-6`、KL 0、8×A100 40GB；WebShop
  15 steps、512 response tokens、group 8、mini-batch 64、rollout temperature 1.0、validation 0.4、
  KL 0.01、discount 0.95，同为 8×A100 40GB。WebShop 报三 seeds；测试主结果使用 no-memory policy。
- **Baselines / Ablations / Cost:** 对比 Reflexion、Retrospex、GRPO 与 GiGPO。去掉 memory-on-policy 或
  off-policy 分支均使两项 ScienceWorld curve 变差；`p/q` 极端值退化；去掉 intrinsic reward 造成 plateau，
  不同 intrinsic mechanism 的 final level 接近。作者测得带 memory rollout 每 iteration 额外约 50.4 秒、
  约占所测 rollout time 19%；这不是跨环境固定 overhead。
- **What Evidence Proves / Does Not Prove:** 支持 temporary memory 可以把跨 rollout exploration signal
  与参数更新连接，并在作者两种 text environment 中改善学习；不证明 self-generated tips 真实或安全，
  不证明 off-policy conditioning removal 对任意 policy/version 无偏，也不证明 OOD 几次 memory trial
  能替代生产 adaptation、human approval 或持续 memory governance。
- **Trade-offs / Previous Design Still Applies:** scaffold 加速发现新状态，却引入 stale/poisoned tips、
  retrieval bias、memory-policy co-adaptation、importance-ratio drift 和额外 rollout cost；蒸馏减少 inference
  依赖，也可能固化错误 shortcut。奖励密、环境简单或 failure cost 高时，memory-free on-policy training
  仍更容易审计。
- **Evolution / ROADMAP / Existing Coverage:** `Layering / Dependency` between external Agent memory
  and policy optimization；Ch29 主 owner，Ch73/75 为 handoff。已读 Ch29 与 Ch73/75：Ch73 已治理
  derived memory，Ch29 已覆盖 on-policy/staleness，但尚未解释“memory-conditioned behavior → no-memory
  policy”的 conditioning/importance-ratio contract；因此训练章节拥有主机制，Agent Memory 只作边界。
- **Integration Decision:** `Full Review Complete — Books Candidate / Temporary Memory Scaffold and
  Policy-Internalization Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 怎样对 tip correctness、policy-version compatibility 与 distillation regret 建立
  verifier？论文 `p/q` 记号不一致在 paper-run config 中如何解析？memory poisoning 是否会被参数永久化？

### AgentDropoutV2

- **Candidate / Week / Score:** AgentDropoutV2 / 2026-W09 / 23/30；
  `Source Family ID: mas-message-rectify-reject-failure-memory-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-26，v2 2026-05-28。事件按 v1
  归档；当前 v2 与 repository 只用于核验后续机制、动态/fixed MAS 结论和 artifact 边界。
- **Direct / Related Primary Sources:** arXiv:2602.23258 current full text + official repository。仓库称
  2026-02-27 初始 release，当前包含 37 commits、paper-facing config/result snapshots、math/code pools、
  launchers 与 pool construction；但 05-22 后才补 bundle，且没有绑定 v1 table 的 immutable tag，
  不能把 current artifact 当成 event-date 完整复现包。
- **Full-read Coverage:** 已检查 agent/information/control-flow formalization、rectify/reject algorithm、
  indicator retrieval、failure-driven mining/dedup、global fallback、zero-shot path、math/code setup、main/
  transfer results、iteration/top-k/random/dedup ablations、dynamics、prompts、dataset statistics、pseudocode
  与案例。论文没有独立 Limitations/Threats to Validity section。
- **Original Problem / Why Previous Design Was Reasonable:** 固定 broadcast/chain topology 让信息流和
 责任清晰；在 agents 输出可靠或有 deterministic verifier 时，直接传递最便宜。错误 message 在 shared
  context MAS 中会级联，但直接 dropout 整个 agent 又可能删除可修正信息并破坏 connectivity。
- **Changed Constraint / Mechanism:** system 在 agent output 发往 successors 前拦截消息；rectifier 从
  当前 scenario/action 生成 query，检索历史 failure-derived indicators，逐项判 violation。通过即传播，
  可修复则把 rationale 返回原 agent 重试，预算耗尽则拒绝；有效 message 数低于 threshold 时全局 reset。

  ```text
  unconditional message propagation
  -> message-edge audit with retrieved failure patterns
  -> pass / retry / reject
  -> connectivity check
  -> bounded global fallback instead of silent sparse consensus
  ```

- **State Ownership / Control and Data Flow:** source agent 拥有候选 output 但无权自证通过；indicator store
  拥有 error name/definition/trigger/embedding/version；rectifier 产生 violation flag/rationale；orchestrator
  拥有 retry budget、successor edges、accept/reject event、remaining-message threshold 与 global reset。
  Ground-truth answer 只用于离线 mining/evaluation，不应在部署时被假定可用。
- **Evaluation Contract:** AutoGen SelectorGroupChat，max chat turns 6、reflection rounds 3；selector 为
  GPT-4.1-mini-2025-04-14；participants/rectifier 为 non-thinking Qwen3-8B/4B；teacher GPT-4o-2024-08-06、
  deduplicator GPT-4.1-mini、embedding Qwen3-Embedding-8B。九个 math benchmarks + 四个 code benchmarks；
  math indicators 来自 MATH/AQuA train failures。Rectifier temperature 0，其余 0.7；硬件、precision、
  context length、并发、latency/cost SLO 与 repeated-seed variance `Not Disclosed`。
- **Ablations / Evidence Boundary:** default 3 retries/5 indicators 优于所测 0/2/4 与 3/8；random indicators
  和 no-dedup 退化。Qwen3-8B math average 从 AutoGen 48.95 到 55.25；4B transfer 与 code generic
  indicators 增益较小。小样本 AIME 百分比、同源 LLM audit 与未披露重复采样意味着不能把平均增益
  写成通用 MAS reliability guarantee。
- **What Evidence Proves / Does Not Prove:** 支持在所测 reasoning MAS 中，message-level repair/reject
  可减少已知错误模式传播；不证明 LLM rectifier 是 sound verifier，不证明 “build once, deploy anywhere”，
  也不证明 reset 后必然产生独立证据。Indicator 可能继承 teacher、training split 和 retrieval bias。
- **Trade-offs / New Failure Modes:** 更严格 gate 会增加 false reject、latency、token cost 与 topology
  starvation；feedback 可能制造新错误；global reset 可恢复 connectivity，也会重复成本并在 correlated
  agents 上复现同一失败。Deterministic verifier、单 Agent + checker、typed workflow 或静态 topology
  在证据明确、任务短或成本严格时仍优先。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of error propagation control；Ch78
  主 owner，Ch73/76/77/80 为 handoff。已读这些章节：Ch78 已覆盖 error amplification、topology repair
  与 authoritative shared state，但缺 message edge 的 pass/retry/reject/fallback contract；Ch76 拥有一般
  feedback semantics，Ch73 只拥有 indicator provenance，不重复主机制。
- **Integration Decision:** `Full Review Complete — Books Candidate / Message-Edge Rectify-Reject
  Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 如何用 deterministic evidence 校准 LLM violation flag？false reject 如何申诉/回放？
  global reset 怎样设预算并避免同源失败循环？indicator pool 在 task/model drift 后如何失效和回滚？

### Search More, Think Less

- **Candidate / Week / Score:** Search More, Think Less / 2026-W09 / 25/30；
  `Source Family ID: parallel-evidence-acquisition-plan-context-contract-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-26，v2 2026-02-27，均属于 W09。
  已读当前 v2 HTML 的 full paper、algorithms、tables、analysis、prompts 与 cases。
- **Access / Artifact Boundary:** 本轮未定位到作者公开 repository、model card、training logs 或 immutable
  dataset artifact；paper 披露 method 与 recipe，但无法做 code-level control-flow 核验或复现。硬件、
  precision、SFT/RL corpus size、wall-clock latency 与 total tool/token cost `Not Disclosed`。
- **Full-read Coverage:** 已检查 related work、parallel workflow、graph/subgraph data construction、
  deterministic/open-ended synthesis and verification、SFT curation、RLOO recipe、all benchmark setup/results、
  step/top-k analysis、context management、tools、judge prompts 与 case study；论文无独立 Limitations section。
- **Original Problem / Why Previous Design Was Reasonable:** sequential ReAct/search 将每次 observation
  立刻用于下一步，依赖清晰、merge 成本小，在强顺序任务和低 tool concurrency 环境仍合理。长时程研究
  同时含多个相对独立 evidence goals；把所有搜索串成一条 reasoning chain 会让 latency、重复 query 与
  context growth 随 interaction depth 累积。
- **Changed Constraint / Mechanism:** initial plan 将问题编成带依赖的 subtasks；runtime 只并发执行 ready
  nodes，记录 pending/completed sets，并每 5 steps 或 context overflow 时 refine plan。128K overflow 时
  生成新 plan 后丢弃 pre-plan context，以 plan 作为压缩后的执行状态。训练数据也奖励每 step 多 tool calls
  与较短成功轨迹，SFT 后以 modified RLOO、sequence importance correction 与 outcome judge 继续训练。

  ```text
  sequential search/reason chain
  -> explicit dependency-aware subtask plan
  -> parallel evidence acquisition
  -> periodic synchronization and plan refinement
  -> overflow-triggered plan checkpoint
  -> final synthesis under bounded context
  ```

- **State Ownership / Control and Data Flow:** planner 生成 plan hypothesis；workflow runtime 拥有 node
  readiness、dependency、tool concurrency、completed evidence、budget 和 plan versions；retrieval tools
  拥有 source observations；context manager 只能在 durable plan/evidence references 已保存后丢弃历史；
  final synthesizer 消费 verified/linked evidence。并行 tool output 不是自动一致的 shared truth。
- **Training / Evaluation Contract:** Qwen3-30B-A3B-Instruct-2507；SFT 3.5 epochs、batch 128、AdamW、
  LR `1.4e-5`、max 65,536 tokens；RL batch 32、8 rollouts/question、LR `1e-6`、max 128K、120 turns、
  60 steps。Inference vLLM/128K，通常 100 steps，另测 300；Deep Search 六 benchmarks，Deep Research
  Bench RACE 四维 judge。Deep Search trajectories 蒸馏自 DeepSeek-V3.2，Research 来自 GPT-5。
- **Results / Ablations / Metric Boundary:** BrowseComp 上 SMTL-100 平均 60.4 assistant steps、3.5 tool
  calls/step、44.6 accuracy，SMTL-300 为 150.7/3.7/48.6；step budget 与 retrieval top-k 增大时表现提高且
  diminishing returns。Assistant steps 不是 total tool calls、tokens、GPU time 或 wall-clock latency；多条
  baseline 数字来自 prior work，未统一重跑。论文没有完全隔离 parallel workflow、synthetic data、
  SFT/RL recipe 与 context reset 的 factorial ablation，因此不能把全部收益因果归给并行。
- **What Evidence Proves / Does Not Prove:** 支持 evidence breadth / information density 是不同于单链
  reasoning depth 的有效 scaling axis，并展示依赖感知并发 + replanning 在所测 search contract 中可形成
  accuracy-step frontier；不证明“search more”总是更便宜、更快或更可靠，也不证明被 plan summary 丢弃的
  evidence 可无损恢复。
- **Trade-offs / Previous Design Still Applies:** 并行降低 critical path，却增加 tool fan-out、rate limit、
  duplicate/conflicting evidence、merge、context burst 与 side-effect coordination；plan reset 节省 tokens，
  却可能丢 provenance 和 unresolved uncertainty。强顺序依赖、高副作用或低 concurrency 时，sequential
  workflow 继续成立。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of planning under search workload；
  Ch75 主 owner，Ch71/72/77/78 为 handoff。已读相邻章节：Ch75 已有 dependency/parallel/replanning/
  critical-path 原则，但缺 “assistant step ≠ tool/token/wall-clock cost”、plan checkpoint 与 evidence-density
  scaling 的机制边界；Ch78 明确 single Agent + parallel tools 不应误写为 Multi-Agent。
- **Integration Decision:** `Full Review Complete — Books Candidate / Parallel Evidence-Acquisition and
  Plan-Checkpoint Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 如何用 total tool calls、token、wall-clock、failure/merge cost 重画 Pareto frontier？
  plan reset 后怎样保留 citation/provenance 与 unresolved evidence？并行 search 的 rate-limit/fairness 谁治理？

### ISO-Bench

- **Candidate / Week / Score:** ISO-Bench / 2026-W09 / 24/30；
  `Source Family ID: inference-optimization-patch-evaluation-contract-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-23，无后续 revision。已读 HTML
  全文的 benchmark construction、hard/soft metrics、quadrant analysis、functional-correctness
  validation、agent setup、全部实验与案例、Limitations、Appendix 和 reproducibility details；联读
  official repository 与 Hugging Face dataset card。
- **Artifact Boundary:** repository 提供 dataset generation、Agent harness、baseline/human/agent 三路 GPU
  benchmark、soft-metric analysis 与 LM Evaluation Harness correctness path；Hugging Face artifact 共
  54 rows（39 vLLM、15 SGLang）。但当前 main、外部 analysis repository、Docker image、submodule 与
  gated model 共同决定执行语义，页面没有提供不可变 release/tag 将所有组件绑定到论文运行；代码能
  检查 pipeline，不等于本轮独立重跑了作者数字。
- **Original Problem / Why Previous Design Was Reasonable:** coding benchmark 用 unit tests 或 runtime
  speedup 作为 hard metric，便宜、确定且可自动扩展；对于普通 bug fix 也常足够。Inference optimization
  patch 却可能通过跳过计算、改变 workload、损坏模型质量或偶然命中另一条路径来“变快”；反过来，
  Agent 也可能找到正确瓶颈，却写不出可运行实现。性能结果、机制意图与功能正确性因此是三个不同对象。
- **Task Construction / Changed Constraint:** 作者从 vLLM 与 SGLang merged performance PR 抽取任务，
  经 keyword filter、GPT-5-mini 分类和人工审阅后，保留改动少于 10 files、具可测性能变化的局部 patch。
  Agent 获得优化前 commit 与 bottleneck description，输出 patch；human merged PR 作为机制和性能参照。
  这种构造提高 replay 可行性，也系统性排除了多模块重构、长期 profiling 与架构级 redesign。
- **Mechanism / State Ownership:** benchmark runtime 应分别拥有：task/commit/workload identity；patch
  provenance；hard benchmark 的 command、环境与 measurement；soft judge 的 model/prompt/verdict；
  correctness suite 与结果。论文以两个维度把 patch 分成 true success、good intent/bad execution、
  lucky win 与 complete failure；这不是让 soft judge 取代 execution，而是防止单一 throughput 代理同时
  冒充“优化正确”和“实现正确”。
- **Control / Data Flow:** pre-optimization commit 与任务说明进入 Agent sandbox；Agent patch 先应用到
  isolated worktree，再与 baseline/human path 在相同 benchmark contract 下比较；hard-success case
  继续进入 LM Evaluation Harness 功能检查，代码差异另由 model judge 比较 bottleneck location 与
  implementation approach。最终 verdict 必须引用三条 evidence，而不是把一个 scalar 写成总成功。
- **Evaluation Contract:** 54 tasks；每任务隔离 Docker/worktree、network allowed and logged、单张
  NVIDIA H100 80GB、8 CPU、64GB RAM、120 分钟上限。论文比较 Claude Code/Sonnet 4.5、Codex
  CLI/GPT-5 high 与 TRAE 的 Sonnet/GPT-5 configurations。hard metric 按原 PR 使用 TTFT 或 throughput，
  相对 human result 超过 5% 记 outperform、±5% 记 comparable；soft metric 使用
  Gemini-3-Flash-Preview。具体 model、batch、length、precision 因 task 而异，应由逐任务 record 读取，
  不能把 54 项压成统一 serving SLO。
- **Results / Failure Evidence:** 作者设置中，vLLM true-success rate 分别为 46.2%、28.2%、17.9%、
  20.5%，SGLang 为 26.7%、80.0%、86.7%、80.0%（对应论文所列四个 agent/scaffold）；同一
  Sonnet backbone 在不同 scaffold 和 codebase 上结果反转，说明 observed subject 是
  `model + scaffold + repository + task`。一个 Bamba case 在性能通过后，LM Eval accuracy 从 32%
  降至 0，直接展示“更快但语义已损坏”。这些是作者单卡/该任务集结果，不是 agent 排名或通用退化率。
- **What Evidence Proves / Does Not Prove:** 支持 inference-optimization Agent 评估至少需要性能、
  correctness 与 mechanism-intent 的正交证据，并证明在该 benchmark 中单一 hard metric 会产生 false
  success；不证明 soft judge 与 human optimization 是 ground truth，不证明与 human patch 不同的机制
  就是错误，也不证明 scaffold 对模型能力的独立因果贡献。soft judge 未经独立人工校准，公开 PR 还
  可能形成 contamination。
- **Trade-offs / Previous Design Still Applies:** 多轴评估降低 reward hacking，却增加 GPU cost、
  flaky benchmark、judge disagreement、task-specific correctness coverage 与 artifact pinning 负担；
  human patch 也可能不是全局最优。确定性 unit test 对窄 bug fix 仍合理；microbenchmark 对 kernel
  regression 仍必要；只有当 claim 升级为“真实 workload 优化”时才需要组合 gate。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of executable evaluation；Ch62 主
  owner，Ch46/47 只接收 workload-contract handoff，Ch77 接收 evaluator-driven patch workflow。
  已读 Ch62、Ch46、Ch47、Ch77：Ch62 已覆盖 executable artifact、runtime/service evaluation、scorer
  与 verifier 缺陷，但尚未把 performance intent、functional correctness、bottleneck localization 与
  patch provenance 组成 inference-optimization 专用 gate；将论文写入 serving 机制章节会误置 owner。
- **Integration Decision:** `Full Review Complete — Books Candidate / Optimization-Patch Evaluation
  Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 怎样让 task workload、GPU clock、driver/kernel、model/precision/length/batch 与
  SLO 可复现？soft intent judge 如何用 human disagreement 校准？当 Agent 找到不同于 human PR 的有效
  优化时，怎样避免 false reject？跨文件系统重构如何扩展而不失去 replayability？

### TAPE

- **Candidate / Week / Score:** TAPE / 2026-W09 / 24/30；
  `Source Family ID: plan-feasibility-execution-conformance-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-23，无后续 revision。已读 problem
  formulation、完整 method/ILP、theory、四任务实验、error analysis、sensitivity、ablation、Limitations、
  proofs、implementation pseudo-code、prompts 与 additional results；联读作者 repository。
- **Artifact Boundary:** repository 提供 Python 3.10 dependency、Sokoban/ALFWorld/arithmetic entry points、
  dataset generation 和 smoke commands；公开 README 没有 paper-run tag、完整 raw trajectories、API
  response snapshot 或统一四任务 reproduction manifest，MuSiQue 路径也未在入口说明中闭合。artifact
  支持控制流检查，不能消除 proprietary API version 与随机采样漂移。
- **Original Problem / Why Previous Design Was Reasonable:** ReAct 逐步 observation→action，适合世界
  模型不可靠、需要频繁适应的环境；Plan-and-Act 先给出一条计划，减少局部漂移且控制简单。出现
  irreversible state、tight budget 与长 horizon 后，两类失败开始分离：planned action 本身可能没有
  viable continuation（planning error），生成出来的 action 也可能偏离 planned action（sampling error）。
- **Formal Boundary:** 论文在 G-MDP 中以“该 action 后仍存在正概率到达 goal 的有限 continuation”
  定义 viable action，并用常数 `epsilon_p`、`epsilon_s` 以及 sampling deviation 破坏/恢复 viability 的
  条件概率建模。由多个候选降低 planning error、constrained decoding 令 sampling error 近零的理论
  排序依赖这些简化假设、graph 中存在 viable path 及成本/状态预测可信；不是对任意动态环境的无条件保证。
- **Mechanism:** TAPE 先采样 `M` 条 abstract plans，把“相同 observation 与 task progress”的状态合并
  为 plan graph，使用 LM 预测 terminal reward 与 edge cost；外部 ILP 在 time-expanded graph 中选择满足
  horizon/budget 的 path；constrained decoding 只允许下一 prescribed action；真实 observation 或剩余
  budget 与 predicted node 不一致时，重新采样、建图和求解。
- **State Ownership / Control and Data Flow:** LM 拥有候选 proposal、state projection 和 cost/reward
  prediction，不拥有事实环境；solver 只保证 encoded graph/constraint 内的可行性；executor 拥有 action
  grammar；environment/runtime 拥有 realized state、actual cost、budget 与 mismatch event。plan graph 是
  可验证/可替换的 IR，而不是把自然语言 plan 提升为 ground truth。
- **Evaluation Contract:** Sokoban、ALFWorld、GSM-Hard、MuSiQue，hard setting 由最优路径附近的 step
  budget 或合成 tool time/cost budget 构造；主图使用 gpt-4.1-mini，并另测 gpt-4.1-nano/mini/4.1、
  gpt-5-nano、claude-4.5-haiku。除 gpt-5-nano default unknown 外 temperature 0.3，top-p 与 repetition
  penalty 为 1。Sokoban easy/hard optimal length 分别 6/10，每难度 10 maps、每 map 10 runs；硬件、
  API snapshot、wall-clock、token 与能耗 `Not Disclosed`。
- **Results / Ablation / Sensitivity:** gpt-4.1-mini 的 Sokoban 分析中，ReAct/Plan-and-Act/TAPE 的
  planning error 为 50.7/47.7/36.7%，sampling error 为 8.3/4.7/0.0%，success 为 5/17/46%；planned
  action 由 gpt-4.1-mini parser 抽取，再以 BFS oracle 判 viability，测量并非完全独立于 model judge。
  在 Sokoban easy ablation 中，完整系统 46%；去 solver/constraint/replanning 后分别为 42/36/38%。
  `M=4` 优于 2 与 8；更多 plans 会因 LM state merging 的全局不一致反而降低 graph quality。
- **What Evidence Proves / Does Not Prove:** 支持把 plan feasibility、execution conformance 与
  observation mismatch 分成不同 runtime gates，并在所测合成/模拟 contract 下展示互补收益；不证明
  ILP 是所有 planning 的最佳 solver，不证明 constrained output 等于 semantic correctness，也不证明
  论文的 constant-error theory 描述真实 Agent 的 nonstationary/correlated failure。对开放 Web、长副作用
  workflow 和不可枚举 action space 的适用性尚未验证。
- **Trade-offs / Previous Design Still Applies:** 多计划提高找到 viable branch 的概率，却增加 sampling、
  state-merge、annotation、solver 与 latency 成本；formal solver 只对已编码约束可靠；hard constraint 会
  排除 grammar 外的合法 recovery；频繁 replanning 会产生 plan thrash。短任务、可逆 action、世界模型
  高度不确定时 ReAct 仍合理；约束简单且静态时单计划也更便宜。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of plan-as-hypothesis；Ch75 主 owner，
  Ch74/76/77 为 handoff。已读四章：Ch75 已有 state graph、constraint、critical path 与 replanning，
  但尚未明确区分“选择可行计划”与“保证执行动作符合已选计划”，也未把 plan graph 作为 solver IR；
  Ch74 拥有 action validation，Ch76 拥有 mismatch diagnosis，Ch77 拥有 durable transition。
- **Integration Decision:** `Full Review Complete — Books Candidate / Plan-Feasibility and Execution-
  Conformance Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** state merging 错误怎样被 detector 捕获并回滚？predicted cost uncertainty 如何进入
  robust/chance-constrained solver？constrained decoding 与真实 tool schema/authorization 如何组合？动态
  action discovery、parallel branches 与不可逆副作用下，replan 的最小安全边界是什么？

### Aletheia / FirstProof

- **Candidate / Week / Score:** Aletheia tackles FirstProof autonomously / 2026-W09 / 24/30；
  `Source Family ID: autonomous-proof-artifact-credibility-2026`。
- **Source Type / Date / Revision:** Google DeepMind technical report；v1 2026-02-24、v2 2026-02-27、
  v3 2026-03-15。事件按 v1 归档，当前 v3 用于核验后续 expert assessment 与 revision，不把 3 月内容
  当作 W09 新事件。已读 challenge interpretation、HAI/autonomy boundary、method、per-problem evaluation、
  inference-cost disclosure、verification/extraction prompt、pre-deadline record 和核心 raw outputs Appendix；
  联读官方 `superhuman/aletheia` raw artifact directory。
- **Related Family / Artifact Boundary:** 联读 Aletheia system report（arXiv:2602.10177）只用于理解
  Generator/Verifier family，不重复计为 W09 event；与 W08 OpenAI FirstProof 属于同一 challenge 的
  `Layering / Dependency`，不是一个系统的直接演进。官方 artifact 发布 prompts、PDF/LaTeX outputs 与
  submission material，但不发布 Gemini weights、agent runtime code、完整内部 logs、hardware 或 absolute
  inference tokens/cost，因此可以审查 proof artifact 与 timing，不能独立重放 Agent。
- **Original Problem / Why Previous Design Was Reasonable:** 研究级数学以 final answer 或自动 exact
  match 评分几乎没有意义；专家审稿能够检查逻辑与学术标准，却昂贵、有领域依赖且会混合“核心论证
  是否成立”和“是否已达到可发表完整度”。FirstProof 自身被作者描述为 experimental trial 而非 formal
  benchmark，规则对 clarification、minor revision 与 expert-in-the-loop 的边界存在解释空间。
- **Autonomy / Control Flow:** 团队把 FirstProof 原始 LaTeX problem statement 不修改地交给两个
  Aletheia configurations（A 使用 2026-02 Gemini 3 Deep Think base，B 使用 2026-01 Gemini base）；
  candidate 经预先确定的 verification/extraction prompt 产生 `[WRONG] / [FIXABLE] / [CORRECT]` verdict
  与最终 LaTeX。团队声明 pipeline 中不向模型追问澄清、也不人工修改中间数学内容；随后由至少两位
  academic mathematicians 独立反馈，低置信 case 再扩大专家集合。系统自检、artifact selection 与外部
  scientific judgment 是三层 owner，不能合并成“模型自证正确”。
- **Evaluation Contract:** 10 个 problems，release 2026-02-05、deadline 2026-02-13 23:59 PST；每题
  best-of-2，从 A/B candidates 中取可用结果。最终 v3 报告多数 expert 将 P2/P5/P7/P8/P9/P10 评为
  correct，其中 P8 为 5/7、其余公开计数为 4/4、4/4、3/3、4/4、2/2；P1/P3/P4/P6 两个配置均无
  output。团队在 deadline 前私发结果以建立 no-post-solution timing evidence，但这不排除 broader
  pretraining contamination。
- **Failure / Disagreement Evidence:** A 与 B 各自至少产生一个 false positive：P5 有 problem
  interpretation 分歧，P7 的 A candidate 含关键 finiteness fallacy，P8 的 A candidate inadequate；P8 B
  的专家在数学主线基本一致，却对遗漏细节是否超过“minor revisions”分歧，并普遍认为未经修订不可
  发表。verification prompt 过滤一个 P3 wrong candidate，并对 P5/P7 A 触发 autonomous revision。
- **Inference / Resource Boundary:** 论文只把每题 inference cost 表示为相对 Erdős-1051 solution 的
  倍数，并明确两个 base models 不同、比较并非同口径；P7 高出既往 observed scale 一个数量级。硬件、
  token、parallelism、wall-clock 与 monetary cost `Not Disclosed`。独立的人类编排 Gemini 3 Deep Think
  以更少 inference scaling 得到 P10，说明“更多 compute”与“更高自治”也不是同一轴。
- **What Evidence Proves / Does Not Prove:** 支持该 pipeline 在限定 deadline、best-of-2 与作者组织的
  expert-review contract 下产生六个多数专家认为可信的 proof artifacts，并揭示 self-filtering、candidate
  diversity 与 external review 的价值；不支持无条件写成“自治解决 6/10”，不证明多数票等于 formal
  proof，不证明 A/B 改进来自 base model 还是 scaffolding，也不把 FirstProof 变成稳定、可比较的通用
  benchmark。P8 应保留 `Disputed at publication-completeness boundary`。
- **Trade-offs / Previous Design Still Applies:** 多候选与 verifier 降低单次 false positive，却增加巨大
  inference 与 selection bias；专家评审接近领域质量，却有带宽、利益关联、reviewer threshold 与跨领域
  不一致；强 self-filtering 提升 precision，也会降低 coverage。形式验证适合可形式化子域，人工审稿
  仍是开放数学主张的必要 authority，二者不会被 model judge 替代。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of artifact evaluation；Ch62 主 owner，
  Ch77 接收 research workflow / human-review handoff。已读两章：Ch62 已覆盖 structured artifact、human
  judgment、model judge 与 claim provenance，但缺“数学可信度 / 缺失细节 / publishability / autonomy”
  的分层 verdict，以及 best-of-N selection 对 claim 的影响；Ch75 不是主 owner，因为本报告没有公开足够
  planning mechanism 让 Books 沉淀。
- **Integration Decision:** `Full Review Complete — Books Candidate / Proof-Credibility and Autonomy
  Evaluation Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** 如何预注册 expert rubric、处理 reviewer affiliation 与 majority/unanimity？best-of-N
  的 N、abstention/no-output 和 verifier revision 怎样进入结果 identity？数学内容正确但不可发表应如何
  分级？何种 transcript/provenance 足以支持“autonomous”而不泄露 private reasoning 或内部系统细节？

### Multi-Vector Index Compression in Any Modality

- **Candidate / Week / Score:** Multi-Vector Index Compression in Any Modality / 2026-W09 / 23/30；
  `Source Family ID: query-agnostic-multivector-index-budget-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-24，无后续 revision。已读 late-interaction
  formalization、SeqResize/MemTok/H-Pool、AGC method、四类 modality/dataset setup、全部 results、budget
  sweep、transfer、utilization analysis、ablation、method limitations 与 Future Work；联读作者
  `omni-col-press` repository。
- **Artifact Boundary:** repository 提供 text/image/video/audio 的 modular train/index/retrieve pipeline，
  显式暴露 AGC、memory-token、hierarchical-pooling、sequence-resize 与 uncompressed ColBERT configs。
  当前 main 未用 release/tag、environment digest 和 immutable benchmark manifest 绑定论文表格；代码
  提高机制可检查性，不是本轮独立复现。训练 hardware、index build wall time、online query latency、
  peak memory 与 energy `Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable:** single-vector retrieval 用一个 embedding 表示
  document，存储和 ANN 成本低，却会丢细粒度 token-region match；ColBERT-style late interaction 为每个
  query token 对 document vectors 做 MaxSim，保留细节但使 storage 与 scoring cost 随 document/modal
  length 线性增长。text document 较短时多向量 index 合理；视频、视觉文档和音频可产生上千 vectors，
  大量静帧、背景或静音又是冗余，旧的“每个 token 都保留”才暴露出系统边界。
- **Formal Contract / Changed Constraint:** document mapping `pi(d)` 必须在 query 未知的 indexing time 完成，
  输出固定 `m × h` vectors；online score 仍为对每个 query vector 取 document-vector 最大内积再求和。
  因而压缩必须 query-agnostic 地保留未来可能区分 positive/hard-negative 的局部证据，不能直接复用依赖
  当前 prompt attention 的 KV pruning。
- **Mechanism:** SeqResize 以 sequence-axis MLP 投影到固定长度；MemTok 让 learnable tokens 汇聚文档；
  H-Pool 用 Ward-style hierarchical merging；AGC 则用 learned universal queries 从 self-attention 中选
  salient centroids，以 hard assignment 保留不同 semantic groups，再用 attention saliency 对 cluster
  token 加权聚合。hard clustering 减少 MemTok over-smoothing，soft weights 缓解硬分配的优化不连续。
- **State Ownership / Data Flow:** encoder 仍拥有完整 raw multimodal encoding；compression module 产生
  versioned derived representation；index service 拥有 vector budget、quantization/layout 与 publication；
  query path 消费 compressed vectors 做 MaxSim。source asset、encoder/compressor checkpoint、`m`、modality
  sampling、index format 与 qrels 必须共同进入 index identity。压缩 representation 不是 source of truth，
  source 更新、模型更新或 budget 变化都需要 rebuild/migration policy。
- **Evaluation Contract:** BEIR（text）、ViDoRe v2（visual documents）、MSR-VTT（24-frame video）与
  MultiVENT 2.0（最多 24 frames、audio 4kHz）。文本使用 gte-modernbert-base、10k steps、batch 20、
  LR `1e-4`、bf16、query/document max 32/300、FastPlaid 4-bit residual；多模态使用 Qwen2.5-VL-3B/
  7B、Qwen3-VL-4B 或 Qwen2.5-Omni-3B，2 epochs、LR `1e-5`、bf16，global batch 分别为
  112/28/8。budgets 为 BEIR 32、ViDoRe 64、MSR-VTT 32、MultiVENT 64。
- **Results / Measurement Boundary:** 作者表中 AGC 在固定 budgets 下相对 uncompressed nDCG 保留约
  97%，MSR-VTT 的 32-vector AGC R@1 56.9 高于 1318-vector baseline 55.7；这支持 redundancy removal
  可兼具 regularization effect，不证明压缩一般会提高检索。ViDoRe/MultiVENT 的 uncompressed representation
  无法装入目标 index，部分比较退回 flat search，MultiVENT 还把 audio 从原训练 16kHz 降到 4kHz 才能
  fit batch；因此没有同 serving backend、同 latency/memory 的 end-to-end production speedup 结论。
- **Ablation / Sensitivity:** learned attention centroid、hard clustering 与 weighted aggregation 都有贡献；
  5/32/128-vector sweep 显示更大 budget 通常更好，但 SeqResize 较平坦，提示 unused capacity。
  MSR-VTT 中只约 1% document tokens 在一次 evaluation pass 成为 MaxSim match；该 utilization 来自特定
  query set，不能代表未见查询或长尾 fact。AGC 可在训练 32 后测试 5/128，H-Pool 无训练但 budget
  flexibility 不同；固定全库 `m` 仍会对信息密度差异大的 documents 过压或浪费。
- **What Evidence Proves / Does Not Prove:** 支持“sequence-vector budget”是 late-interaction index 的独立
  compression axis，并在四个公开 contract 下表明 saliency-guided hard clustering 比所测 alternatives 更
  稳；不证明 AGC 是所有 modality/corpus 的默认，不证明 `1% utilization` 等于 99% tokens 永远无用，也
  不证明 storage ratio 会等比例转化为 index-build、network、query latency 或 whole-RAG task success。
- **Trade-offs / Previous Design Still Applies:** fixed budget 使容量和 MaxSim work 可控，却新增 training、
  centroid-selection bias、long-tail detail loss、reindex 与 budget migration；先完整 encode 再压缩不会降低
  upstream encoder cost。single-vector 适合粗召回和成本优先场景；uncompressed multi-vector 适合 corpus
  小、细节召回高风险；H-Pool 适合无训练/快速迁移；AGC 适合有训练数据且 index pressure 高的分支。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of retrieval physical design；Ch72 主
  owner，Ch71 与 Ch62 为 handoff。已读 Ch71～73 与 Ch62：Ch72 已有 ingestion/index identity、retrieval/
  rerank/packing，却把 document embedding 近似写成单一对象，缺 late interaction 的 storage-quality
  evolution、query-agnostic compression 与 source/derived-index rebuild contract。
- **Integration Decision:** `Full Review Complete — Books Candidate / Late-Interaction Index-Budget
  Contract`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** per-document dynamic `m` 如何进入 ANN layout 与 SLO admission？长尾 query 是否会
  专门依赖低-utilization vectors？encoder、compression、quantization 与 ANN pruning 的误差怎样分层归因？
  source deletion 与 compressor checkpoint 更新时，能否增量 rebuild 而保持 index consistency？

### DPE / Diagnostic-driven Progressive Evolution

- **Candidate / Week / Score:** From Blind Spots to Gains / DPE / 2026-W09 / 23/30；
  `Source Family ID: diagnostic-feedback-data-mixture-loop-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-26、v2 2026-05-07。事件按 v1 归档，
  当前 v2 用于完整 method/evaluation/revision 核验。已读 diagnosis、multi-Agent question generation、
  validation gate、GRPO/difficulty theory、11-benchmark results、static/diagnosis/diversity/quality ablations 与
  conclusion；论文没有独立 Limitations section。联读 official code、model-zoo 与 iterative entry point。
- **Artifact Boundary:** repository 提供 `weakness analysis → question generation → score/filter → RL/SFT`
  pipeline、Docker/environment、model checkpoints 与 VLMEvalKit 入口；current main 没有 immutable paper-
  run tag、third-party API snapshots、完整 per-iteration generated/accepted manifests、seeds 或 raw judge logs。
  它支持 lifecycle 检查，不能独立证明表格。训练 GPU、precision、global batch、GRPO group size、KL/
  clipping、wall-clock 与 cost 多数 `Not Disclosed`。
- **Original Problem / Why Previous Design Was Reasonable:** static curated data 分布稳定、易去重与复现；
  generic self-generation 用 entropy/quality filter 扩大样本，能在缺人工标注时持续训练。固定分布会在已会
  categories 上饱和，盲目生成又可能 template collapse、category drift 或反复训练模型已掌握的内容。
  新问题是有限 data budget 应随 checkpoint blind spots 变化，而不是把 Evaluation 与 Data 当两套系统。
- **Diagnostic Mechanism:** 每轮从 diagnostic pool 采样 `N=200`，按 12 个 image/capability categories
  统计 step-aware correctness，并让 diagnostic agents 归纳 category weakness、failure patterns 与 generation
  hints；结果形成 `R^(k) = category quotas + per-category failures + actionable instructions`。这把 evaluation
  result 编译成下一轮 sampling specification，但 capability taxonomy 和 attribution 仍是 model-mediated
  measurement，不是可观测 ground truth。
- **Generation / State Ownership:** Planner 把 quota/hints 编成 per-sample image/question requirements；
  Image Selector 用 Serper top-3、Qwen-Image-Edit 等工具取得/修改图像；Question Generator 构造 question/
  reference；Validation Agent 同时检查 category consistency、solvability/completeness、answer verifiability
  与 format，任一 gate 失败则 regeneration。data control plane 应拥有 diagnostic pool/version、quota
  ledger、source/license、generator/judge identity、accepted/rejected lineage 与 target checkpoint。
- **Difficulty and Update:** DPE 只保留 moderate-difficulty samples：binary pass rate 接近 0 或 1 时 group
  reward variance 低，GRPO 几乎没有相对 signal，接近 0.5 时 learnability 较高。通过过滤后用 GRPO 更新
  Qwen2.5-VL-7B-Instruct 或 Qwen3-VL-8B-Instruct，再开始下一轮 diagnosis。这个推导说明 reward variance
  与 sample usefulness 的关系，不保证 `p≈0.5` 对所有 verifier、curriculum 或 generalization 最优。
- **Evaluation Contract:** 从 Vision-SR1-47K 前 1K seeds 出发，four-agent generator 使用 OpenAI o3、
  Claude Sonnet 4、Gemini-2.5-Pro、Qwen-VL-Max；论文称约 4K generated candidates/iteration，对比
  VisPlay 8K/iteration。表 3 又把三轮 DPE training data 标为约 3K，与生成/过滤后的确切 accounting 未
  完整解释。用 VLMEvalKit 覆盖 11 benchmarks，比较 Qwen2.5-VL-7B、Qwen3-VL-8B 与 VisPlay/static
  baselines；closed model 横向分数不具同训练/数据/decoding 因果可比性。
- **Results / Ablations:** Qwen2.5-VL-7B 的 overall average 从 57.29 经三轮到 59.29，Qwen3-VL-8B
  从 65.64 到 68.04，但 individual benchmarks 有回落（如 ChartQA）。去 diagnostics 后 CharXiv 轨迹
  36.8→36.7→37.5→36.7，full DPE 为 36.8→37.7→38.1→40.91；作者还以 200 samples/iteration 的
  Qwen3-VL embeddings/UMAP 和 model-rated quality 展示 diversity。它支持闭环 targeting 在该 recipe
  中有用，不证明“少量动态数据”因数据量本身胜过 47K static data，generator models、image source、
  validation、difficulty filter 与 iterative RL 没有完整 factorial isolation。
- **What Evidence Proves / Does Not Prove:** 支持 Evaluation→diagnosis→quota→generation→validation→
  training 形成可执行 data feedback loop，并揭示 data mixture 应绑定 current checkpoint；不证明 model-
  generated diagnosis 是 causal blind spot，不证明跨 11 benchmarks 的提升来自单一模块，不证明开放
  image search 已处理版权/PII/contamination，也不证明 repeated benchmark-guided iteration 未对评测集
  过拟合。
- **Trade-offs / Previous Design Still Applies:** targeted data 提高有限预算的信息密度，却新增 evaluator/
  generator bias feedback、benchmark overfitting、source drift、label circularity、API/version cost 与 rare
  capability forgetting。frozen curated data 在可复现、高风险与法规场景仍成立；人工 domain curriculum
  在 taxonomy 稳定时可能更可靠；DPE 适合 verifier 可校准、iteration 可回滚的 experimental branch。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Refinement` of data-as-specification；Ch23 主 owner，
  Ch29/62 为 handoff。已读 Ch23、Ch24、Ch29、Ch62：Ch23 已说明 mixture `alpha_k` 定义梯度权重与
  filtering selection bias，但缺“评估当前 checkpoint 后动态重写 mixture”的闭环、diagnostic identity 与
  accepted/rejected generated-data lineage；GRPO 机制由 Ch29 已覆盖，不在 Ch23 重写。
- **Integration Decision:** `Full Review Complete — Books Candidate / Diagnostic Data-Mixture Control
  Loop`，`Status: Experimental`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** diagnostic pool 与 final eval 如何隔离以避免 training-on-eval？category quota 的置信
  区间、minimum coverage 与 forgetting guardrail 怎么定义？external image 的 license/PII/contamination
  怎样进入 acceptance gate？generated/accepted/trained counts 与每轮 checkpoint 能否由 manifest 重放？

### Reflective Test-Time Planning

- **Candidate / Week / Score:** Learning from Trials and Errors: Reflective Test-Time Planning for Embodied
  LLMs / 2026-W09 / 22/30；`Source Family ID: reflection-guided-test-time-parameter-adaptation-2026`。
- **Source Type / Date / Revision:** arXiv paper；v1 2026-02-24、v2 2026-05-10、v3 2026-05-25。
  事件按 v1 归档，current v3 用于完整 method、追加 HM3D/robot/efficiency experiments 与 revision 核验。
  已读 algorithms、losses、two benchmarks、ablations、compute-matched/efficiency、human reflection audit、
  hyperparameters、single-step vs receding horizon、dataset/model/TTT Appendix；论文没有独立 Limitations
  section。联读 project repository。
- **Artifact Boundary:** repository 提供 BEHAVIOR/OmniGibson setup 与部分运行材料，但 current page 没有
  immutable paper-run manifest、full robot logs、all training/evaluation artifacts 或 exact hardware topology。
  GPT-5-generated tasks、LLaVA-3D dependencies 和 later revision code 构成复现边界；机制可检查，作者
  headline 不能视为独立 reproduction。
- **Original Problem / Why Previous Design Was Reasonable:** fixed inference model + retry 避免在线 weight
  drift，行为 identity 稳定，适合短任务和安全关键部署；verbal reflection 只改变 context/memory，便宜且
  可回放。Embodied long-horizon task 中，动作可能执行成功却战略上阻塞后续，单步 feedback 又会把
  non-local consequence 归因错；重复 trials 若既不保留 evidence、也不改变 decision policy，会反复犯错。
- **Mechanism / Boundary Correction:** Reflection-in-Action（RIA）每步从 action model 采样 `N` candidates，
  internal reflection model 生成 critique/0–100 score，选最高者执行。Reflection-on-Action（ROA）由 frozen
  external reflection model 根据真实 observation 评价已执行动作；每 `K` steps 或 milestone 触发
  retrospective reflection，用后见状态重评早期 actions。随后 SFT 更新 internal reflector，REINFORCE
  用 `r=2s/100-1` 更新 action model；这不是普通 context-level Reflection，而是由 reflection 生成 label/
  reward 的 in-episode test-time parameter adaptation。
- **State Ownership / Control Flow:** environment 拥有 physical state 与 execution result；external reflector
  拥有 provisional diagnostic signal，不是真实 authority；working/retro buffers 保存 action、observation、
  score、hindsight window；runtime 决定 update trigger、budget、base/adaptor checkpoint、rollback 与
  episode scope。internal/action LoRA 只能作为 run-scoped derived policy；若跨 task 持久化，必须经过第 31/
  55/62 章的 artifact/evaluation gate，不能由 Agent 自行升级为 production model。
- **Forgetting Control:** 除 retrospective examples 外，系统从 unexplored actions 采样当前 internal model
  outputs 作 regularization targets，试图锚定未覆盖 state；实验采用 50/50 retrospective/regularization。
  这降低局部 catastrophic forgetting，但同一模型输出不是独立 teacher，无法证明未观察能力被保留。
- **Evaluation Contract:** LLaVA-3D/Llama 7B unified model 先以 action/internal/external prompts SFT，部署时
  实例化三份，external frozen，另两份 LoRA/weights 可更新。LoRA `r=4, alpha=8, dropout=0.15`，RIA
  默认 candidate optimum 在 Cupboard ablation 为 `N=6`，retro window `K=5`；Long-Horizon Household
  由 GPT-5 基于 BEHAVIOR-1K scene graph 构造四类 3–7 room tasks，另测 MuJoCo cupboard、HM3D OOD
  与 Franka Panda。具体 GPU model、precision 与完整 task/seed counts `Not Disclosed`。
- **Results / Ablation / Compute:** Household 中 full average 33.7%，去 RIA/ROA 为 8.79%，同 3× time
  budget vanilla 为 8.46%；RIA 与 ROA 单独移除有时比都移除更差，说明两个 learned components 也可能
  mismatch。Cupboard LoRA TTT 60.2%、full-weight 57.4%；real robot 的 fit/correct 从 fine-tuned no-
  reflection 20.7/7.2 到 full 44.2/16.6。作者报告 naive full path 约 3× per-step wall time；parallel scoring、
  batching、early stop、QLoRA、多 GPU 累积可降到 relative 0.45×、success 31.5%，但 baseline absolute
  time、hardware、resource cost 未披露，不能外推 production latency。
- **Reflection Evidence Boundary:** author human audit 将 external/retro reflections 的 factual/causal/useful
  评分报告为 95–99%，但 annotator count、sampling 与 independence 披露不足；external reflector 与 action
  system 来自同 unified-model family，错误可能相关。Retrospective score 改善 credit assignment 的结果
  绑定该合成 household/cupboard contract，不证明 language critique 能可靠替代 robotics safety verifier。
- **What Evidence Proves / Does Not Prove:** 支持“执行后 observation + hindsight”可生成比 immediate
  feedback 更有用的 long-horizon credit signal，并展示 reflection-driven test-time update 是区别于 verbal
  retry 的真实分支；不证明部署时改 weights 一般安全，不证明 single-step learned anticipation 普遍优于
  model-based planning，不证明未披露 physical failures、policy drift 或 OOD behaviors 已受控。
- **Trade-offs / Previous Design Still Applies:** online adaptation 可把 episode time 转成 learning，却新增
  compute、model-copy memory、nonstationarity、catastrophic forgetting、feedback poisoning、rollback 与
  subject-identity drift；external evaluator 错误还会被参数化放大。固定 model + durable context/reflection
  对高风险、短 task 与低重复场景仍更合理；explicit receding-horizon planning 在约束可建模且 solver 可
  验证时仍成立；parameter TTT 只适合 scoped、可回滚、反复试验环境。
- **Evolution / ROADMAP / Existing Coverage:** `Boundary Correction` / `Layering`；Ch76 主 owner，Ch29/
  73/75/77 为 handoff。已读这些章节：Ch76 当前把 Reflection 定义为不更新参数的 inference-time loop，
  该定义对 verbal reflection 仍正确，但已不足以覆盖 reflection-generated supervision；应增加 taxonomy，
  明确 context adaptation 与 parameter adaptation 的 ownership/rollback。Ch75 不应因论文标题而拥有主机制，
  因其核心不是显式 plan graph；Ch29 已拥有 policy-gradient math。
- **Integration Decision:** `Full Review Complete — Books Candidate / Reflection-to-Test-Time-Training
  Boundary Correction`，`Status: Experimental`；Evidence Gate 未通过，本周不修改 Books。
- **Open Questions:** online adapter 的 episode/task scope、rollback 与 promotion gate 如何定义？external
  reflection 被 prompt injection 或 sensor error 污染时如何阻断 gradient？同一 unified model 的 correlated
  blind spots 如何用 deterministic/physical evidence 校准？多租户 robot runtime 如何隔离 per-run updates？

### DSDR / Dual-Scale Diversity Regularization

- **Candidate / Week / Score:** DSDR / 2026-W09 / 22/30；
  `Source Family ID: dsdr-correct-mode-diversity-rlvr`。
- **Source Type / Date / Sources:** arXiv:2602.19895，v1 2026-02-23；完整 HTML、公式、theory appendix、
  experiments 与作者标注 official code 入口联读。当前 arXiv 仅一版，未发生跨周 revision。
- **Full-read Coverage:** Verified；覆盖 GRPO background、global/local diversity definition、coupling、
  correctness-preservation theorem、implementation equations、training/evaluation setup、main results、
  ablation、training dynamics、diversity judge、hyperparameter sweeps 与 appendix proof。
- **Original Problem / Previous Design:** vanilla GRPO 用同 prompt group 的 reward mean/std 构造 advantage，
  在 all-correct/all-wrong 时失去组内排序；统一 entropy bonus 可增加 token randomness，却不保证产生不同且
  正确的 solution modes。旧方案仍合理，因为它简单、便宜，并避免把难以定义的 semantic diversity 写入
  reward；问题只在 reward saturation 与 correct-mode collapse 成为主要瓶颈时出现。
- **Mechanism:** global signal 只在 `r=1` 的 rollout 上计算 group-relative distinctiveness，并以 clipped
  diversity bonus 扩充 reward；local signal 使用按 sequence length 平均的 token conditional entropy，避免
  长 response 因 token 数更多天然获得更大 regularization；global-to-local softmax/coupling 把更强 local
  entropy 分配给更 distinctive 的 correct trajectories，而非平均扰动所有样本。
- **State / Control / Data Flow:** rollout policy 生成 `G=8` trajectories；binary verifier 拥有 correctness
  gate；diversity scorer/representation 产生 trajectory relation；trainer 拥有 clipping、global/local
  coefficient、coupling temperature、policy/reference identity 与 update。diversity 不是 environment truth，
  只能在 correctness gate 之后改变相对 credit；其 implementation/version 必须进入 reward specification。
- **Theory Boundary:** 论文在 bounded regularization、binary verifier 与给定 diversity definition 下推导
  optimal correctness preservation 和 diversity-tilted allocation；这不是 finite neural-network optimization
  的收敛保证，也不证明 semantic diversity scorer 无偏，更不证明非 binary/open-domain reward 下仍成立。
- **Evaluation Contract:** Qwen2.5-Math-1.5B、Qwen3-1.7B/4B，DAPO-Math-17K-Processed，最大 response
  4K/8K，batch 256、minibatch 16、group 8、LR `1e-6`、8×A100 40GB；在 AIME24/25、MATH500、
  Minerva、Olympiad 上报告 Pass@1、Avg@16 与 Pass@k。diversity analysis 另用 GPT-5.2 judge；训练
  wall-clock、energy、seed variance、judge calibration 与完整 code-to-paper manifest `Not Disclosed`。
- **Ablation / Sensitivity:** 在 1.7B/4B 上分别去掉 global diversity 与 coupling 均降低作者平均结果；
  training curves 显示无 global signal 时 entropy 可能过快上升，无 local/coupling 时后期 exploration 收缩。
  论文 sweep `lambda_d`、`lambda_l` 与 temperature 后选默认值，因此主结果包含调参选择；没有完整的
  等 compute、不同 verifier noise、不同 domain/model-family factorial，不能外推为通用 RLVR recipe。
- **What Evidence Proves / Does Not Prove:** 支持“correct trajectories 之间仍需可定义的 learning signal”，
  以及 sequence-length-invariant local entropy 与 trajectory diversity 是不同控制轴；不证明更多表面表达
  差异等于更多 reasoning modes，不证明 GPT judge diversity 与真实策略独立，也不证明增加 pass@k 会提高
  calibration、faithfulness 或 production reliability。
- **Trade-offs / Failure Modes:** 获得 targeted exploration，付出 extra pair/group scoring、judge/embedding
  compute、reward complexity 与新 hyperparameters；可能鼓励 paraphrase/formula formatting diversity、
  使长尾 correct mode 过度加权，或在 verifier 漏洞下扩展 reward-hacking modes。低成功率阶段没有 correct
  pool 时 global signal无效；高可靠 verifier 不存在的开放领域，朴素 GRPO/PPO 或 offline preference
  仍可能更稳妥。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution` from group-relative reward saturation；
  Ch29 主 owner，Ch28/30 boundary。已读 Ch28、Ch29，并核对 Part III 邻接结构；Ch29 已覆盖 all-equal
  group ratio、reward correctness 与 group-size trade-off，但缺少“correct-only trajectory diversity →
  length-invariant local entropy → coupled allocation”的演进分支。
- **Integration Decision:** `Full Review Complete — Books Candidate / Correct-Mode Exploration Contract`；
  `Status: Experimental`，Books Gate 未通过，本周不修改正文。
- **Open Questions:** diversity representation 如何避免把措辞变化当推理变化？verifier false positive 与
  diversity bonus 联合时会怎样放大 exploit？能否用 effective mixed/correct-mode ratio 动态启停 regularizer，
  并在等 rollout tokens 下与 curriculum、larger group 或 search 做因果对照？

### Implicit Intelligence / Agent-as-a-World

- **Candidate / Week / Score:** Implicit Intelligence / 2026-W09 / 21/30；
  `Source Family ID: implicit-requirements-declarative-world-eval`。
- **Source Type / Date / Sources:** arXiv:2602.20424，v1 2026-02-23；完整 HTML、appendix YAML/
  prompts/model endpoints 与官方 Labelbox benchmark/leaderboard 联读。Leaderboard 后续模型不是 W09
  event，本次只用于验证评估 surface 持续存在。
- **Full-read Coverage:** Verified；覆盖四类隐式要求、AaW specification/world model/protocol、seed 与
  adversarial generation、expert validation、dataset/evaluator methodology、16-model experiment、world-
  model consistency、failure analysis、limitations、完整 YAML/trajectory/prompt appendices。
- **Original Problem / Previous Design:** hand-built simulator 提供可执行、可重复 state transitions，却让每个
  domain 的工程成本很高；纯文本 synthetic task 易扩展，却没有可探索环境，无法判断 Agent 是否主动发现
  未明说但可观测的 constraints。显式 instruction benchmark 对“严格照做”有效，但真实用户常省略 privacy、
  accessibility、timing 与 irreversible-risk requirements。
- **Mechanism:** 单一 YAML 声明 context、entities、typed actions、mutable state、hidden execution rules、
  return templates 与 evaluation rubric。Primary Agent 只看到 user prompt/entity surface，最多 50 turns；
  fixed World Model 检查 action/precondition、按规则更新 state 并返回 observation；Evaluator 在结束后依据
  action history/final state 对 binary criteria 判定。场景通过 Plan→Attempt→Refine 挖掘 frontier failure，
  再由作者、两名 independent experts 与 difficulty gate 筛选。
- **State Ownership / Trust Boundary:** YAML/spec owner 定义 world truth 与隐式 requirement；World Model 是
  rule interpreter，不应发明 intent；Primary Agent 只拥有 proposal/trajectory；Evaluator 拥有 rubric mapping，
  不拥有真实用户偏好。论文称 world execution “deterministic”，但实际 executor 仍是 LLM，作者测得最高
  consistency 98.6%，因此严格说是高一致性的 empirical simulator，不是 deterministic program。
- **Evaluation Contract:** 205 iOS-centric scenarios：70 implicit reasoning、56 catastrophic risk、46 privacy/
  security、33 accessibility；约 303 native actions，每 scenario 3–5 entities、2–4 actions/entity、3+
  criteria/rules。Scenario Pass Rate 要求全部 criteria 通过，Normalized Scenario Score 记录部分完成；
  evaluator-human agreement 只被定性为 high，human sample size、agreement statistic 与完整 raw labels
  `Not Disclosed`。环境 timeout/step、model endpoint 与 confidence interval 有披露，硬件/成本不适用于 API
  模型且未完整报告。
- **Evidence Boundary:** 结果支持受测 Agent 常在 proactive exploration、dependent configuration 与 state
  preservation 上失败；extended thinking 对不同模型方向不一，说明更多 reasoning budget 不是稳定修复。
  但 benchmark 在构造时主动保留“至少一个 frontier fail、至少一个 pass”的场景，不能用通过率估计现实
  prevalence 或模型总体能力；作者文化视角、iOS temporal drift 和固定 action space 都限制外推。
- **Simulation / Evaluation Failure Modes:** LLM world executor 可能产生非确定漂移或同源偏差；natural-
  language rules 可能含歧义；单一 author/expert expectation 可能把有争议的 social norm 写成 ground truth；
  difficulty mining 会过拟合当前 models。Evaluator 即使只查 state，也仍需解析 natural-language rubric；
  没有公开完整 dataset/harness artifact 可在本轮独立 replay，机制可审但 paper scores 尚未复现。
- **Evolution / Previous Design Still Applies:** `Layering / Dependency`：文本 task 适合低成本 discovery；
  declarative LLM simulator 用少量环境工程换可交互 state；coded/replay sandbox 在安全关键、精确 semantics
  与可重复性要求高时仍更可靠；最后还需 shadow/real environment 检查 sim-to-real gap。AaW 不是对真实
  environment 的替代，而是位于静态 QA 与 executable sandbox 之间的 evidence tier。
- **ROADMAP / Adjacent Chapters / Existing Coverage:** Ch62 主 owner，Ch71/74/75 boundary；已读 Ch62、
  Ch71、Ch74、Ch75。Ch62 已要求 environment identity、trajectory/outcome evidence，但缺少 declarative LLM
  simulator 的 evidence strength 与 “deterministic” claim boundary；Ch71 已拥有 Context trust，不需复制
  implicit-requirement taxonomy；Ch75 的 constraints 仍应由 policy/runtime enforce，不由模型猜测授权。
- **Integration Decision:** `Full Review Complete — Books Candidate / Declarative Simulator Evidence Tier`，
  `Status: Experimental`；Books Gate 未通过，本周不修改正文。
- **Open Questions:** 哪些 execution rules 必须从 LLM interpreter 下沉到 code/schema？如何对不同文化与
  user preference 表达 uncertainty/clarification 而非单一 hidden truth？如何版本化 scenario、OS/action
  semantics 并量化 sim-to-real transfer？

### PyVision-RL

- **Candidate / Week / Score:** PyVision-RL / 2026-W09 / 21/30；
  `Source Family ID: pyvision-interaction-collapse-active-vision-rl`。
- **Source Type / Date / Sources:** arXiv:2602.20739 v1 2026-02-24；arXiv metadata、完整 v1 paper mirror、
  作者 project page、official GitHub/eval repo 入口、Hugging Face data/model cards 联读。arXiv PDF 因体积
  无法由当前浏览器直接载入，但 v1 全文镜像覆盖正文与 appendix，artifact 用官方来源交叉核验。
- **Full-read Coverage:** Verified；覆盖 scaffold、on-demand video context、reward、rollout selection、GRPO
  modification、SFT/RL data、training/evaluation settings、benchmarks、四项 ablation、training dynamics、
  appendix algorithm/prompts/data distribution、released code/config/model/data surface。论文没有独立
  Limitations section，未披露项在本 packet 明确保留。
- **Original Problem / Previous Design:** uniform video frame sampling 的 state/control 简单、batching 友好，
  但长视频会把大量无关 visual tokens 放入 context；固定 crop/zoom tool 安全可控，却限制新视觉操作；
  arbitrary Python 支持动态组合，却扩大 sandbox 与 reward-hacking surface。GRPO 在 Agent rollout 中还会
  遇到 broken code、all-equal groups，以及 tool count 与 group normalization 共同造成 interaction collapse。
- **Runtime Mechanism:** image 同时进入 MLLM context 与 Python runtime；video 只先进入 runtime，模型按
  query/observation 生成 Python 选择/plot frames，再把 rendered evidence 追加回 context。这是 model-guided
  context materialization：runtime 拥有完整 media 与 code sandbox，model 只决定下一块 derived view。
- **Training Mechanism:** reward 为 `R_acc + 0.1*n_tool*I(R_acc=1)`，仅正确 answer 获 tool-call bonus；
  oversample `alpha*B` prompts，每题生成 group，过滤全 broken/zero-variance group，按 reward std 排序并取
  top informative groups；同时去掉 GRPO advantage 的 std normalization。目标是避免没有 gradient 的组、
  runtime-failure contamination 和 correct-but-short trajectory 被负 advantage 压制。
- **Data / Implementation Contract:** Qwen2.5-VL-7B base；image SFT 约 7K（先过滤错误或少于两次 tool
  turn）、video SFT 44K；image RL 44K、video RL 15K。两模型 RL 700 steps、oversampling batch 32、
  train batch 16、group 8、LR `1e-6`、8×H100；code release 使用 verl/vLLM、32K prompt/20K response
  limits、FSDP offload、LLM judge endpoint 与 max-turn controls。event-date exact commit、H100 memory、
  precision、wall-clock、energy、sandbox isolation policy 与 seed repeats `Not Disclosed`。
- **Evaluation / Ablation:** image 覆盖 visual search、multimodal math、TIR-Bench；video 用 VSI-Bench。
  四项 one-factor ablation 分别降低 max turns、去 tool reward、去 std ranking、恢复 std normalization；作者
  curves 支持 tool reward/max-turn 的收益主要在训练后期，ranking 帮助早期稳定。video 约 5K visual tokens
  与 uniform baseline 约 45K 的比较绑定 VSI-Bench、sampling/model/config；SpaceR 仍有相近或更高 accuracy，
  因此不能写成全面 Pareto dominance。
- **What Evidence Proves / Does Not Prove:** 支持 Agent RL 的 environment failure、interaction budget、
  reward shaping 与 group selection 是联合 contract，也支持按需 frame materialization 可把 visual token
  budget 从固定 sampling 变成 policy decision；不证明更多 tool calls 本身有因果价值，不证明 arbitrary
  Python 优于 typed vision tools，不证明该 reward 在开放任务安全，也不证明 benchmark gains 泛化到实时视频。
- **Trade-offs / Failure Modes:** correct-only bonus 避免奖励明显错误 calls，却仍可能鼓励能答对样本中的
  redundant tool inflation、长 response 与 latency；std ranking 聚焦中等难度，却系统性丢弃 all-correct/
  all-wrong tasks，改变训练分布并可能遗忘 easy/hard tails；过滤 broken trajectories 提高稳定性，却也移除
  学习 recovery 的负例。Python dynamic tooling 增加 RCE、dependency、timeout、nondeterminism 与 output-
  rendering validation；fixed tools 或 uniform frames 在低延迟、高安全、短视频场景仍合理。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`；Ch29 主 owner（interaction-collapse
  reward/rollout contract），Ch74 承接 active perception/Python tool trust boundary，Ch62 承接 evaluation。
  已读 Ch28、Ch29、Ch62、Ch74。Ch29 已覆盖 all-equal groups 与 measurement/reward interface，但缺少
  environment-broken rollout、correct-only interaction bonus 与 difficulty-ranked group selection 的耦合；
  Ch74 的 perception placement 可与 OmniGAIA 合并，不重复写两篇论文。
- **Integration Decision:** `Full Review Complete — Books Candidate / Interaction-Budget Reward and Rollout-
  Selection Contract`，`Status: Experimental`；Books Gate 未通过，本周不修改正文。
- **Open Questions:** 如何把 marginal information gain、tool cost 与 redundancy penalty 代替 raw call count？
  broken trajectory 应过滤、修复还是进入 recovery curriculum？difficulty ranking 如何保留 easy regression/
  impossible detection？Python sandbox 的 syscall/network/data policy 如何进入训练与评估 identity？

### Full Source Review — Adaptive Text Anonymization

- **Candidate / Week / Score:** Adaptive Text Anonymization / 2026-W09 / 22/30；
  `Source Family ID: adaptive-anonymization-prompt-policy`。
- **Source Type / Date / Sources:** arXiv:2602.20743，v1 2026-02-24、v2 2026-04-20；ACL 2026
  Findings paper、完整 HTML 与作者 repository 联读。事件归属锁定 v1，v2 仅用于 revision 核验。
- **Full-read Coverage:** Verified；覆盖 problem framing、three-stage GEPA、五类任务/privacy-utility
  metrics、baselines、implementation、two-stage ablation、model/evaluator robustness、DP comparison、
  human study、compute/hardware、limitations、artifact 与可复现实验入口。
- **Original Problem / Why Previous Design Was Reasonable:** entity masking、固定人工 prompt、Local DP
  rewriting 与 adversarial refinement 各自解决了不同 threat model：前两者简单且低控制面成本，DP
  以随机机制换正式 privacy guarantee，adversarial method 则针对经验 re-identification attacker。问题在于
  同一文本用于分类、问答或内容保留时，允许删除的信息不同，单一静态 anonymizer 很难表达多目标边界。
- **Mechanism:** 不改本地 anonymizer weights，而将自然语言 instruction 视为可搜索 policy。Stage 1
  建立 train/validation split 与 generic seed；Stage 2 用 scalar privacy/utility feedback warm-start；Stage 3
  用包含残留 sensitive cues 的 rich feedback 继续 GEPA proposal，并以 validation 上的 Pareto ranking/
  pruning 保留多种 operating points。它优化的是 task-、model-、metric-specific prompt，不是通用脱敏器。
- **State Ownership / Control Flow:** dataset owner 定义 privacy objective、utility objective、split 与允许外发
  边界；optimizer 拥有 prompt pool、trace、budget、validation score 与 Pareto frontier；local model 生成
  anonymized text；外部 evaluator 只提供 measurement signal，不能自行放宽 policy。被选 prompt 应作为
  versioned policy artifact，与 model/evaluator/dataset revision 一起进入第 62 章的 Evaluation Run。
- **Evaluation Contract:** DB-Bio、SynthPAI、TAB、PUPA、MedQA 五类任务分别使用 identity inference、
  demographic inference、entity leakage、PII leakage、stylometric distance 与 task-specific utility；比较
  OpenPII、DP-Prompt、Adversarial Feedback、RUPTA、人工 prompt。Mistral-Small-3.2-24B、Gemma-3-
  27B-it、Qwen3-30B-A3B 使用 111 train + 111 validation、其余 test；每次优化 1,500 LLM forward
  passes，patience 5、refinement validation sample ratio 0.3、reflection minibatch 3。硬件为两张 24GB
  Quadro RTX 6000 与 Xeon Silver 4114；论文未给出完整 wall-clock、energy、重复 seed 方差与 production SLO。
- **Baselines / Ablation / Human Evidence:** 两项代表任务的等 budget ablation 支持 warm-start 与 rich-
  feedback refinement 的组合比单阶段或 MIPROv2 更好，但不是五任务全 factorial；100 个 DB-Bio/PUPA
  样本由 7 名作者机构内 annotators、每例至少 3 人盲评，支持自动 metric 的方向一致性，不能替代独立
  privacy audit。作者 API cost 是当时价格下的估算，不是跨 provider 的持久性能结论。
- **What Evidence Proves:** 在披露的 task/model/attacker/metric contract 下，prompt optimization 能发现
  多个经验 privacy–utility Pareto points，并让较小的本地 open model 避免每个输入重新推理策略；固定
  prompt 不是唯一可维护的 policy layer。
- **What It Does Not Prove:** 方法自身没有给出 Differential Privacy 保证；与 DP baseline 的指标优势不
  等于更强形式化 privacy。固定 attacker 或 judge 上的低 re-identification 不能证明面对新 attacker、
  linkage auxiliary data 或 distribution drift 仍匿名。使用 closed evaluator 时，少量敏感/匿名文本仍可能
  越过 trust boundary，论文也明确未解决“什么 anonymized output 已安全到可外发”。
- **Limitations / Failure Modes:** metric gaming、validation overfit、attacker shift、utility proxy 偏差、
  hallucinated rewrite、prompt/model coupling 与 evaluator data exposure；平均两个目标无法表达 hard privacy
  constraint、lexicographic policy 或法律责任。每 task 仍需标注集和优化 compute，prompt revision 也会使
  既有评估失效。
- **Evolution / Previous Design Still Applies:** `Layering / Dependency`：entity masking 适合显式字段和
  低成本路径；DP 适合必须提供可组合 formal guarantee 的场景；固定 domain prompt 适合 policy 稳定、
  变更频率低的系统；adaptive prompt search 用额外 evaluation/control cost 换取经验 Pareto discovery。
  后者不能覆盖前三者，而应由 threat model 和 release gate 决定是否组合。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch68 主 owner，Ch62 为 measurement handoff；
  已读 Ch62、Ch68、Ch69。旧 census 的 `Ch65/68` 已纠正：Ch65 是 Trace，不是 privacy owner。Ch68 已
  区分 anonymization、DP 与 threat model，但缺少“可学习 privacy policy 必须与 attacker/evaluator/version
  共同身份化”的机制；Ch62 已具备 scorer 与 dataset contract，可直接承接评估状态。
- **Integration Decision:** `Full Review Complete — Books Candidate / Empirical Privacy-Policy Contract`，
  Books Gate 未通过，本周不修改正文。
- **Open Questions:** 如何用 held-out attackers 与 auxiliary-data suites 检查 prompt 对 threat model 的
  overfit？怎样把 hard privacy constraints、human appeal 和 DP accounting 与 Pareto prompt 合成同一
  release policy？外部 evaluator 的输入应如何最小化、加密、审计与删除？

### Full Source Review — OmniGAIA / OmniAtlas

- **Candidate / Week / Score:** OmniGAIA / 2026-W09 / 23/30；
  `Source Family ID: omnigaia-omniatlas-active-perception-agent`。
- **Source Type / Date / Sources:** arXiv:2602.22897，v1 2026-02-26、v3 2026-07-02；26 页论文 PDF、
  作者 GitHub、Hugging Face benchmark/SFT/model artifacts 联读。事件归属锁定 v1，当前 code/model
  是后续可用 artifact，不反写为 event-date capability。
- **Full-read Coverage:** Verified；覆盖 benchmark comparison、event-graph construction、tool schema、
  fuzzification/quality inspection、OmniAtlas trajectory synthesis、masked SFT、OmniDPO、evaluation、
  error/tool-call analysis、native-vs-tool perception ablation、training details、prompts、impact statement、
  released runner/data/model surface。
- **Original Problem / Previous Design:** 仅把完整 video/audio/image 一次性塞入 multimodal context 的
  优点是控制流简单、端到端联合表征，缺点是长媒体 token cost 与 downsampling 信息损失；把 ASR/VQA
  当外部 tool 则可按需调用、替换与审计，但增加 tool latency、schema/observation error 和跨模态整合负担。
  既有 benchmark 多把 perception 与开放网络/tool execution 分开，难以定位长链 failure。
- **Benchmark Mechanism:** 从公开 video-with-audio 与 image+audio 数据抽取事件、ASR/OCR/object 等信号，
  由 Agent 用 search/browser/image/code tools 扩展 event graph，再通过 event fuzzification 隐去直接实体，
  生成需要多跳恢复的 QA。LLM committee 与 human review 检查自然性、模态必要性、可解性和唯一答案；
  最终 360 tasks、9 domains，98.6% 要求 web search、74.4% 要求 code/computation。
- **Runtime / State / Data Flow:** trajectory 为 `(reasoning state, action, observation)` 序列；模型可直接
  消费 native media，也可调用 `read_video/read_audio/read_image` 选择 segment/region，将原始 media
  追加到 context，再交替使用 search/browser/code。runtime 拥有 tool execution、timeout、budget、media
  range validation 与 observation provenance；模型只提出选择。event graph、annotated answer 与 judge
  属于 benchmark construction/evaluation state，不能泄漏给 test Agent。
- **Training Mechanism:** Gemini-3-Flash 先把 media 转成 detailed description；DeepSeek-V3.2 在每步采样
  `k=3` reasoning/action continuations，Gemini-3-Flash 在可见 ground-truth answer 条件下 pruning，只保留
  successful trajectories。masked SFT 不拟合 tool observation token；随后 OmniDPO 让 Gemini 定位 failed
  trajectory 的首个 perception/reasoning/tool error 并生成 corrected prefix，形成局部 win/lose pair。
- **Evaluation / Implementation Contract:** Pass@1 由 exact match 后接 DeepSeek-V3.2 equivalence judge；
  所有模型共享 search/browser/code tools。OmniAtlas 在 Qwen2.5-Omni 3B/7B 与 Qwen3-Omni 30B-A3B
  上全参数训练，2,156 条 synthetic trajectories，SFT 2 epochs + DPO 2 epochs，4 nodes × 8 H20-
  141GB。公开 runner 有 max actions、concurrency、timeout、active-perception 开关与输出 trace，但 current
  repository/model revision 未以 immutable manifest 绑定 event-date paper run。
- **Evidence / Ablation:** 作者报告 Qwen3-Omni baseline 13.3→SFT 18.9→OmniDPO 20.8 Pass@1，说明大部分
  增益来自 SFT，DPO 是增量修正；native-vs-tool matched-family ablation 显示强 Gemini native path 更准且
  calls 更少，较弱 Qwen 的 tool perception 改善部分 easy/medium、却降低 hard。tool calls 太少与大量
  thrashing 都相关失败。这些是该 360-task、同 judge/tool configuration 下的作者结果，不是通用架构定律。
- **What Evidence Proves / Does Not Prove:** 支持“perception placement 是 runtime policy，而不是 native
  或 tool 的二选一标签”，以及 failure-localized preference pairs 可作为 trajectory-level SFT 后的 refinement；
  不证明 parameter scaling 无效，不证明 active perception 在所有任务更优，不证明 LLM-generated event
  graph/answers 无污染或 judge 无同源偏差，也不证明 benchmark success 等同现实自治。
- **Trade-offs / Failure Modes / Old Branches:** native perception 提高联合表征 ceiling、降低 calls，却绑定
  model/modalities 并增加 context/compute；tool perception 可 modular upgrade、按需取证和补缺失模态，却
  增加 latency、tool failures、prompt injection、evidence merge 与 thrashing。teacher/verifier 依赖会把
  correlated blind spots 写进 SFT/DPO；ground-truth-conditioned correction 不能在部署时直接复用。短媒体、
  固定模态与低 tool budget 下，一次性 native input 仍合理；缺失模态或长媒体局部取证时 tool path 更合适。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`；Ch74 主 owner，Ch62/75 为
  evaluation/planning handoff，Ch27 承接 DPO objective。已读 Ch62、Ch74、Ch75；Ch74 已有 tool proposal/
  executor split、untrusted observation 与 loop boundaries，但缺少“native input ↔ active perception tool”的
  placement policy；Ch75 已覆盖 search/replanning，不需复制训练 recipe；Ch62 已覆盖 Agent outcome 与 judge。
- **Integration Decision:** `Full Review Complete — Books Candidate / Active-Perception Placement Contract`，
  `Status: Experimental`；Books Gate 未通过，本周不修改正文。
- **Open Questions:** 如何以 task uncertainty、media length、native confidence、tool latency 和 cost 动态选择
  perception placement？segment/crop request 如何携带 provenance 并防止遗漏关键上下文？独立 human/
  executable scorer 能否复核 LLM judge 与 teacher-generated corrections？

### Full Source Review — MobilityBench

- **Candidate / Week / Score:** MobilityBench / 2026-W09 / 22/30；
  `Source Family ID: mobilitybench-deterministic-agent-replay`。
- **Source Type / Date / Sources:** arXiv:2602.22638，v1 2026-02-26、v2 2026-06-10；完整 HTML、作者
  GitHub、公开 CLI/config/data surface 联读。事件归属锁定 v1；KDD 2026 Oral 与 current repository 属于
  后续 revision/availability facts。
- **Full-read Coverage:** Verified；覆盖 route-agent problem、episode/task taxonomy、ground-truth SOP、
  deterministic replay sandbox、100K dataset statistics、instruction/planning/tool/outcome/efficiency metrics、
  ReAct-vs-Plan-and-Execute、scenario/model/thinking studies、appendix tools 与 released runner。
- **Original Problem / Previous Design:** live map API 最接近真实交通、天气和服务状态，却因时间变化、
  rate limit 和 backend update 难以复现；静态 QA 可重复，却丢失 tool selection、schema、constraint 与 final
  itinerary 的执行链。传统 route solver 对结构化约束可靠，但不擅长从自然语言恢复隐式意图；LLM 适合
  semantic parsing，却不应替代 authoritative routing computation。
- **Mechanism:** episode 定义为 `(anonymized query, context, fixed replay snapshot, structured ground truth)`。
  domain experts 先以 scenario SOP 构造最小 tool program，抽取/规范化 slots、解析 POI/coordinates、调用
  routing/traffic/weather 并验证 constraint；评估时禁用 live API，以 canonical arguments 命中 recorded
  response，必要时使用受 threshold 约束的 fuzzy entity 或 nearest-coordinate fallback，schema/lookup
  failure 显式计为 tool failure。
- **State Ownership / Control Flow:** benchmark 拥有 immutable episode、tool schemas、snapshot、SOP 与
  hidden structured reference；Agent runtime 拥有 framework、history、tool calls、budget 与 final answer；
  authoritative map service 只在 ground-truth capture 阶段提供外部状态。replay key canonicalization、fallback
  policy 与 snapshot date 是 environment identity，不能隐藏在 benchmark name 后。
- **Evaluation Contract:** 100,000 filtered executable episodes，22 countries、350+ cities、11 intents；
  将链路分为 intent detection、information extraction、task decomposition、tool selection、schema compliance、
  delivery rate、final pass rate，并记录 cumulative input/output tokens。论文比较 ReAct 与 Plan-and-Execute、
  open/closed models，另取 1,000 episodes 比较 thinking mode。API provider/version、完整 model snapshots、
  token price、wall-clock、hardware、sampling repeats 与 statistical intervals `Not Disclosed`，作者数字不能
  作为 production capacity 或模型排名。
- **Evidence Boundary:** deterministic replay 证明同一 frozen evidence 下可以重复比较 trajectory，并将
  final failure 分解到 intent/plan/tool/schema/outcome；作者观察到 ReAct 平均输入 token 更高、不同 scenario
  的 framework 排序不同，支持“反馈闭环与预先结构化计划存在 workload trade-off”。但同一论文一处称
  ReAct 总体 FPR 较高，另一处称 preference-constrained planning 中 Plan-and-Execute 更好，恰好说明不能
  摘取单一 winner。
- **What It Does Not Prove:** replay 不测 live traffic drift、API outage/rate limit、new POI、user clarification、
  GPS uncertainty 或真实副作用；所有 episode 被设计为初始 query 即可解且不允许追问，低估 ambiguity
  handling。ground-truth 是专家 SOP 的一条最小 tool program，不代表只有这一条合法 plan；fuzzy replay
  fallback 也可能接受现实 API 不会返回的近似调用。
- **Trade-offs / Failure Modes / Old Branches:** frozen replay 用 environmental realism 换 reproducibility；
  live shadow/canary 用可比性和风险换 current validity。ReAct 用额外 context/tool cost换 observation-driven
  recovery，Plan-and-Execute 在 structured constraints 下更节省且可预测，却可能对动态 feedback 脆弱；
  conventional solver 仍应拥有 route feasibility，LLM 主要负责 intent/constraint 与解释。
- **Evolution / ROADMAP / Adjacent Chapters:** `Layering / Dependency`；Ch62 主 owner，Ch74/75 handoff。
  已读 Ch62、Ch74、Ch75。Ch62 已区分 offline/replay/shadow/canary，但缺少 replay snapshot 如何同时带来
  reproducibility 与 temporal-validity loss 的完整例子；Ch75 已明确 plan 是可修正假设，因此无需复制
  benchmark 排名；Ch74 可短链到 tool schema/failure evidence。
- **Integration Decision:** `Full Review Complete — Books Candidate / Deterministic Environment-Replay
  Contract`；Books Gate 未通过，本周不修改正文。
- **Open Questions:** 如何在 frozen replay 之外增加 time-sliced snapshots、live shadow 与 counterfactual
  traffic tests？怎样允许 clarification 并评估提问成本/价值？ground-truth tool program 如何表达多个等价
  plan、SOP revision 与 region-specific policy？

### Full Source Review — Overconfident Errors Need Stronger Correction / ACE

- **Candidate / Week / Score:** Overconfident Errors Need Stronger Correction: Asymmetric Confidence
  Penalties for Reinforcement Learning / 2026-W09 / 20/30；
  `Source Family ID: rlvr-negative-rollout-confidence-2026`。
- **Source Type / Date / Revision / Access:** arXiv paper，v1 2026-02-24；本轮读取 arXiv metadata、
  HTML 全文、method、theory、全部主实验、diagnostic experiments、ablation、limitations 与 Appendix
  A～E。未发现后续 revision；作者只提供论文内 PyTorch sketch，未定位到可绑定 paper run 的官方代码
  与 checkpoint。
- **Original Problem / Why Previous Design Was Reasonable:** GRPO/RLVR 的 group-relative advantage
  先按 verifier reward 区分正确与错误，再用组内 normalization 控制 prompt difficulty；全局 KL 则限制
  policy 对 reference 的整体漂移。这套设计简单、可批量执行，也避免为每种错误建立额外标注。但在
  binary reward 下，同一 group 的所有错误 rollout 得到相同基础 advantage，无法区分 policy 已主动
  降低概率的错误与训练过程中反而被强化的错误。
- **Changed Constraint / Mechanism:** ACE 为每条错误轨迹计算相对 reference policy 的长度归一化
  confidence shift：

  ```text
  c_i = (log pi_theta(y_i|x) - log pi_ref(y_i|x)) / T_i

  negative advantage
  = GRPO negative advantage * (1 + alpha * Softplus(c_i))
  ```

  正确 rollout 保留原 advantage；错误 rollout 则按相对 reference 的 probability drift 获得不同惩罚。
  这不是“错误越离谱惩罚越大”的 semantic classifier，而是只观察 policy/reference log-probability ratio。
- **State Ownership / Control and Data Flow:** rollout worker 产生 `prompt_id / trajectory / generating-policy
  version / token logprobs`；verifier 拥有 binary correctness；reference checkpoint 与 tokenizer/template
  定义 confidence 坐标；trainer 聚合 group statistics、sequence length 与 current/reference logprobs 后
  构造 advantage。Reference identity、policy version、length normalization 和 reward state 若未绑定，
  同一个 `c_i` 就不再可比较。
- **Implementation Details / Cost Boundary:** 论文在 veRL 中把 ACE 放入 negative-advantage computation，
  每条错误轨迹增加一次 Softplus，并报告在其训练栈中 wall-clock overhead `<0.1%`。该结论依赖训练本来
  已计算 reference logprobs；对 reference-free 或未保留 sequence logprob 的 pipeline，额外 reference
  forward、存储与版本同步不能被写成“零成本”。论文使用 sequence-level aggregation，token-level 版本
  只作为可能分支。
- **Evaluation Contract:** DAPO-Math-17K，binary verifier；Qwen2.5-Math-7B、Qwen3-8B-Base
  （thinking disabled）与 Llama-3.1-8B-Instruct；GRPO/DAPO baselines；每 prompt 8 rollouts，10 epochs，
  max response 分别 3,000/8,192/4,096 tokens，KL coefficient 0.001。MATH-500 以 5 次独立训练的
  95% CI 报告，AIME 2025 只有 30 题而只报 point estimate；推理评测使用 temperature 0.7、top-p 0.95
  与 Pass@1～32。训练 GPU 型号、节点数、互联、精度和总 wall-clock `Not Disclosed`。
- **Baselines / Ablations / Sensitivity:** ACE 分别与 GRPO、DAPO 组合并保持同模型内 recipe/budget
  对齐；作者跟踪 held-out errors 的 overconfident-error fraction、mean magnitude 和早期 token entropy。
  Softplus/ReLU ablation 只在 Qwen2.5-Math-7B + MATH-500 上进行；`alpha` sensitivity 也只覆盖该设置，
  论文观察 `alpha=1.0` 最好、过大时 Pass@1 回落。没有与 DSDR 等 correct-mode regularizer 做正交
  factorial comparison，也没有开放领域、continuous reward 或超长 CoT 实验。
- **What the Evidence Proves:** 在上述三类 7B/8B 模型、两个数学 benchmark 与 matched recipes 中，
  confidence-aware negative reweighting 相对各自 GRPO/DAPO baseline 改善作者报告的完整 Pass@k 曲线；
  两个 Qwen diagnostic 还显示 ACE 降低相对 reference 的 overconfident-error 指标并减缓早期 entropy
  collapse。证据支持“相同 verifier reward 内的错误异质性可以成为 advantage shaping 维度”。
- **What It Does Not Prove / Theory Boundary:** `c_i>0` 只表示相对 reference 概率上升，不证明错误在
  semantic 或 causal 意义上更危险；reference 若校准差，标签会失真。论文的 selective-regularizer
  decomposition 是 on-policy、`G -> infinity` 与 stop-gradient 条件下的分解，并含 residual；gradient
  quality 改善还依赖 overconfident-error gradient 与优化方向正相关、baseline gradient 高方差等假设。
  Softplus 在 `c_i<=0` 时仍为正，因此 exploratory/self-correcting errors 并非严格“不受惩罚”，只是增量
  较小。作者实验不能证明对所有 RLVR、所有 reward 或生产推理质量普遍有效。
- **Trade-offs / Failure Modes / Old Branches:** ACE 获得 rollout-level error selectivity，却新增 reference
  calibration、policy/reference logprob 对齐、length normalization、`alpha` 和更高 gradient variance；
  标准 GRPO 在短输出、reference 不可靠、计算栈不保留 reference logprobs 或错误异质性弱时仍更简单。
  DSDR 针对“正确轨迹之间的 mode diversity”，ACE 针对“错误轨迹的 confidence drift”，二者是
  `Layering / Dependency`，不是互相覆盖，也尚未被论文证明组合后无冲突。
- **Evolution / ROADMAP / Adjacent Chapters:** Ch29 主 owner，Ch28/30 boundary；已读三章。Ch29 已覆盖
  group normalization、all-equal groups、verifier、entropy/diversity 与 reference regularization，但缺少
  “同 reward 的错误仍应按训练诱发的概率漂移分层”这一机制；Ch28/30 只需保留 pi_old/pi_ref 与
  offline pair boundary，不重复 ACE 公式。
- **Integration Decision:** `Full Review Complete — Books Candidate / Confidence-Shifted Error-Weighting
  Contract`，`Status: Experimental`；Books Gate 未通过，本周不修改正文。
- **Open Questions:** `c_i` 对 reference calibration、tokenizer/template、response length 与 policy lag
  有多敏感？continuous/process reward 下如何定义 error set？ACE 与 DSDR、Clip-Higher、entropy bonus
  同时启用时，是互补、重复还是造成过强 regularization？

### Full Source Review — Trinity of Consistency / CoW-Bench

- **Candidate / Week / Score:** The Trinity of Consistency as a Defining Principle for General World
  Models / 2026-W09 / 18/30；`Source Family ID: world-model-cross-consistency-cow-bench-2026`。
- **Source Type / Date / Revision / Access:** survey + benchmark paper，arXiv v1 2026-02-26；本轮联读
  metadata、alphaXiv 全文镜像、作者项目页、Hugging Face dataset card、公开 `cut.py/evaluate.py` 与
  survey repository。arXiv HTML 不可用且 17.6 MB PDF 超出浏览器抓取上限，alphaXiv 提供了论文全篇
  文字、表格与 Appendix；未发现后续 arXiv revision。
- **Original Problem / Why Previous Design Was Reasonable:** 视觉生成长期使用 FID/FVD、CLIP 或单帧
  human preference，原因是它们便宜、可规模化，也适合衡量感知质量；专用 3D、video 或 multimodal
  模块则能分别优化几何、动态和语义。但“看起来真实”不能证明 instruction、object identity、geometry
  与 state transition 在多帧中同时成立，单轴 benchmark 也会掩盖 cross-axis rupture。
- **Changed Constraint / Framework:** 论文把 general world model 的要求组织成 modal、spatial、temporal
  consistency 三轴及三种两两交叉，并用 CoW-Bench 将每个 family 拆为 5 个 sub-metrics，再复用 16 个
  atomic checks（identity lock、constraint non-relaxation、worldline stability、occlusion、3D coherence
  等）。长期价值在于把“逼真”重写为可归因的 constraint-satisfaction vector；它是一套评价 taxonomy，
  不是证明三轴在数学上充分或必要的定理，也没有提出单一 world-model architecture。
- **State Ownership / Control and Data Flow:** dataset sample 声明 prompt、initial image/state 与 expected
  output；generation system 产生 image/video；`cut.py` 从视频均匀抽 4 帧组成 2×2 grid；rubric 将 task
  family 映射到 atomic checks；公开 `evaluate.py` 把 grid 与 rubric 发送给 `gpt-4.1`，保存 0～2 分及
  rationale。因而 leaderboard 实际评估对象是 `generator + sampling protocol + judge model/prompt +
  aggregation`，不是 generator weights 本身。
- **Dataset / Evaluation Contract:** 论文称 1,485 samples、18 sub-tasks，每类 69～91 条并额外含 50 个
  maze cases；public Hugging Face card 当前显示 1,435 rows，二者相差 50，且 card/category spelling
  与论文 taxonomy 也存在版本差异。视频只均匀抽取 4 帧；每个 atomic check 由 judge 给 0/1/2 ordinal
  score，再按 family 等权聚合。作者报告 18 个 sub-task 的多种 closed/open image/video models，但
  generation seed、API snapshot、sampling config、judge endpoint revision、重复次数与 uncertainty
  并未形成可独立重放的 immutable manifest。
- **What the Evidence Proves:** 论文和公开 artifact 证明 CoW-Bench 确实提供 multi-frame、modal/spatial/
  temporal 及 cross-axis 的结构化任务与 rubric，且 paper run 中不同 models 在 identity binding、rule-
  guided evolution、maze goal tracking、multi-view anchoring 等 slice 上呈现不同 failure profile。它支持
  “world-model evaluation 应测跨帧约束保持，而非只测 perceptual plausibility”的工程原则。
- **What It Does Not Prove:** 四帧抽样会漏掉 frame-between failure，不能证明 long-horizon continuity；
  `gpt-4.1` judge 仍是论文自己批评的 model-evaluating-model 路线，fine-grained checklist 只能降低、不能
  消除 shared blind spots。任务由 reasoning models 扩展并经 human-machine audit，但 paper 未披露足够的
  annotator agreement、judge calibration 与独立 human baseline。排行榜不能证明某模型拥有 causal
  world representation，论文从 constraint backoff 推断 action-space representation 的结构性原因也不是
  被 intervention/ablation 直接验证的结论。
- **Trade-offs / Failure Modes / Old Branches:** atomic rubric 获得 diagnosability，代价是 judge cost、
  rubric coverage 与大量条件状态；四帧 grid 获得统一接口，代价是 temporal aliasing。Physics engine、
  executable simulator 和 dense trajectory checks 在可形式化领域仍提供更强 hard evidence；FID/FVD 与
  human preference 也仍适合感知质量，不能被 consistency benchmark 全面替代。
- **Evolution / ROADMAP / Adjacent Chapters:** `Principle Reuse`；Ch10 是概念 owner、Ch62 是 evaluation
  boundary。已读 Ch9～10 与 Ch62。Ch10 已明确 world model 必须预测 action 后果、像素逼真不等于因果
  正确，并要求 intervention、long-horizon prediction 与 control outcome；Ch62 已把完整 subject identity、
  scorer version、model-judge calibration、per-slice evidence 与 executable verifier 写成 Evaluation
  contract。因此 Trinity 的三轴 taxonomy 和 CoW-Bench 是有用受限案例，但没有改变现有设计结论。
- **Integration Decision:** `Full Review Complete — No Change — Already Covered / Weekly Only Benchmark
  Evidence`；不因论文篇幅或术语新颖度强行修改 Ch10/Ch62。
- **Open Questions:** paper 1,485 与 public dataset 1,435 的 50 条差异是否正是 maze split/version drift？
  能否用 dense frame/state trace、physics engine 与 human calibration 复核 gpt-4.1 judge？三轴 pairwise
  consistency 是否足以覆盖 agent/social causality、partial observability 与 intervention semantics？

### dLLM framework

- **Candidate / Week / Score:** dLLM framework / 2026-W09 / 25/30；
  `Source Family ID: diffusion-lm-lifecycle-and-sampler-contract`。
- **Source Type / Date / Sources:** arXiv:2602.22661 v1，首次公开 2026-02-26；本轮阅读全文、
  Appendix B reproduction tables，并检查作者仓库的 trainer、sampler、evaluation 与 recipe 入口。
  论文只存在 v1；仓库是随时间演进的 implementation evidence，不等同于 event-date immutable artifact。
- **Full-read Coverage:** Metadata、Abstract、Introduction、Preliminaries、Trainer、Sampler、Evaluation、
  open recipes、Related Work、Conclusion/Future Work 与 Appendix reproduction tables 已读。正文没有独立
  `Limitations` 或 `Threats to Validity` 章节；因此限制必须从实验矩阵、复现差异、未披露条件和 future
  work 反推，并明确标为本轮分析，而不是作者声明。
- **Original Problem / Why Previous Designs Were Reasonable:** Masked Diffusion、Block Diffusion、
  EditFlow 等 text diffusion 路线拥有不同 corruption objective、data collator、generation API 与 eval
  post-processing。各论文保留自己的代码能最快验证新想法，在研究早期是合理选择；但当模型、sampler
  与 benchmark 横向比较时，复制并微调私有 pipeline 会把实现差异误当成架构差异。
- **Principle / Changed Constraint:** Autoregressive generation 的一次 token selection 通常由固定 prefix
  推进；MDLM 从被 mask 的全局/局部状态反复 denoise，BD3LM 又在 block 间 autoregressive、block 内
  diffusion。于是“checkpoint identity”不再足够：noise schedule、mask policy、remasking/parallel-update
  rule、step count、padding/EOS/CFG、block size 与 post-processing 都会改变实际生成过程。
- **Mechanism:** dLLM 将生命周期拆为 `Trainer + Sampler + Evaluation`。Trainer 用 MDLM/BD3LM
  wrapper 固定 corruption/loss boundary；AR-to-MDLM 通过 BOS 与 shifted logits 适配，SFT wrapper
  让 padding EOS 保持可见并训练额外 mask 位置产生 EOS。`Sampler(model).sample()` 将 model forward
  与 denoising algorithm 解耦；Fast-dLLM sampler 再组合 block-wise approximate KV caching 与
  confidence-based parallel token update。Evaluation 扩展 lm-evaluation-harness，但仍为每个
  model-task pair 显式复刻 preprocessing、decoding hyperparameters 与 post-processing。
- **State Ownership / Control and Data Flow:** Trainer 拥有 `clean tokens → sampled time/noise → masked
  state → weighted denoising loss`；sampler 拥有 `masked/padded state → repeated model calls → confidence /
  remask decision → committed tokens`；evaluation adapter 拥有 prompt formatting、EOS suppression、CFG、
  temperature、parallel-update width、step budget 与 output normalization。Fast-dLLM cache 只复用其
  block 近似认为稳定的 state；它不是标准 causal KV Cache 的无条件等价物。
- **Implementation Details:** 框架基于 Hugging Face Trainer/Accelerate/PEFT，提供 MDLM、BD3LM 与
  EditFlow reference trainer、terminal decoding visualizer，以及 BERT/AR checkpoint 转 DLM recipes。
  “只换 sampler/trainer”降低 plumbing 成本，却没有消除 objective-specific wrappers；这些 wrappers
  正是必须版本化的 semantic adapter，而不是可以忽略的样板代码。
- **Evaluation Contract:** reasoning SFT 使用 LLaDA/Dream Base/Instruct、s1K、max length 4096、20
  epochs、global batch 32、LoRA `r=128/alpha=256`、8×A100、ZeRO-2；结果显示 Instruct variants 多数任务
  改善，但 Base variants 在部分 OOD planning/coding 上回退。small-model recipes 与 AR baselines 并非
  全部同一训练预算。Fast-dLLM 表格依 model、max-new-tokens 256/512、cache/parallel configuration
  报告 throughput；hardware、concurrency、SLO 和端到端 serving overhead 未完整披露。
- **Baselines / Sensitivity / What Evidence Proves:** 单独改变 EOS suppression、CFG、temperature 或
  parallel-update width 就可能显著改变得分；Appendix 中 official 与 dLLM reproduction 也并非逐项完全
  相同。这足以证明 DLM evaluation 对 inference contract 敏感，以及统一接口仍需 model-task-specific
  adapter；不能证明 dLLM 的默认配置是跨模型“公平真值”，也不能证明 diffusion LM 已普遍优于 AR。
- **Trade-offs / New Failure Modes / Old Branches:** 统一抽象提高可比较性和 recipe reuse，却新增
  adapter semantic drift、默认参数误用、cache approximation error、parallel commit/remask ordering、
  EOS/padding mismatch 与 framework-version identity。原作者 pipeline 在追踪最新机制、复现特殊
  post-processing 或框架尚未覆盖的新 objective 时仍合理；AR runtime 在严格 causal state、成熟 KV
  管理和 latency contract 更重要时也没有被替代。
- **Evolution Relationship:** `Layering / Dependency`：MDLM/BD3LM 定义生成过程，dLLM 把其差异提升为
  lifecycle interface；Fast-dLLM 是 sampler 层 acceleration branch，不是对 DLM objective 的替代。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 主 owner 候选为 Ch20，因为该章已把完整
  decoding config 定义为 generation identity，却只沿 autoregressive token-selection 主干展开；已读
  Ch19～21、Ch38～40 与 Ch62。Ch38/40 负责 runtime loop，Ch62 负责 evaluation subject。现有正文尚未
  明确“非 AR 生成中 sampler/noise/remask/step budget 也是模型工件身份”的长期边界。
- **Integration Decision:** `Full Review Complete — Books Candidate / Generative-Process Artifact
  Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续优先 refine Ch20 的生成
  分支与 Ch62 handoff，不把 framework feature list 写入 Books。
- **Open Questions:** 如何为不同 DLM family 定义 semantic-equivalence test，而不把 task-specific tuning
  固化成默认公平配置？approximate cache 与 parallel token commit 的 quality/latency frontier 如何绑定
  hardware、length、steps 和 SLO？event-date code 与持续演进仓库怎样形成可复现 artifact manifest？

### Vectorizing the Trie / STATIC

- **Candidate / Week / Score:** Vectorizing the Trie / STATIC / 2026-W09 / 27/30；
  `Source Family ID: constrained-decoding-state-representation`。
- **Source Type / Date / Sources:** arXiv:2602.22647 v1，首次公开 2026-02-26；当前 v2 为
  2026-07-20。本轮阅读全文、公式、两项算法、online/offline experiments 与 Appendix A～G 的 memory、
  latency、branch-factor 和 JAX implementation。v2 用于机制核验；不能把 7 月修订当作 W09 新事件。
- **Full-read Coverage:** Metadata、Introduction、Related Work、generative retrieval/prefix-tree background、
  problem formulation、STM/CSR conversion、hardware-accelerated decode、VNTK、YouTube deployment、Amazon
  cold-start、Conclusion/Future Work 与全部相关 Appendix 已读。正文没有独立 limitations 章节；动态
  update、实验外推和 baseline comparability 限制分别从 Future Work 与 evaluation contract 提取。
- **Original Problem / Why Previous Designs Were Reasonable:** Trie 用 prefix 节点和 child pointer 精确
  表示合法输出集合，CPU pointer traversal 易实现、易动态更新，并可在每个 beam step 返回合法 token；
  小 constraint set、CPU decode 或低吞吐时，这个控制流设计合理。问题出现在 accelerator-hosted model：
  每步 TPU→CPU callback 会暂停 graph，GPU beam 的不同 child count 又造成 warp divergence。
- **Principle / Changed Constraint:** 约束语义没有变化，变化的是执行介质：accelerator/ML compiler 偏好
  static shape、coalesced memory access 与 branch-free dataflow。因此真正的演进不是“Trie → 非 Trie”，
  而是 `logical prefix automaton → different physical representation and transition kernel`。
- **Mechanism:** STATIC 将每个 prefix 映射成 integer state，把 `(state, token) → next_state` 编译成
  stacked CSR transition matrix。每个 level 预计算最大 branch factor `B_l`；VNTK 总是 gather 固定
  `B_l` 个连续 entries，再用 `Range/Where` 清除超出真实 child count 的槽位，并 scatter 成 vocabulary
  mask。前 `d` 个高分支层使用 dense mask，后续低分支层使用 sparse gather，随后执行 masked beam
  top-k 与 next-state gather。
- **State Ownership / Control and Data Flow:** Offline builder 拥有 constraint snapshot、prefix-to-state
  mapping、CSR rows 与 per-level branch bounds；每个 beam 拥有当前 state id 和 score；device kernel
  拥有 `logits → valid transition mask → selected token/beam → next state`。论文 production configuration
  在每张 chip 复制 transition state，避免每步 collective；因此 inventory freshness、matrix version、
  rollout/rollback 与 request-to-version pinning 成为 serving control-plane responsibility。
- **Implementation Details:** stacked `(token_id,next_state)` layout 让一次 coalesced read 同时取得两项；
  dense prefix mask 用 HBM 换 early-level branch throughput。论文 JAX/XLA reference 以 `take/gather/scatter`
  构造静态 graph，并说明 PyTorch/Inductor 可映射到相同 primitives。variable-length ID 可用 null state
  表达，但主要实验使用固定长度 Semantic IDs，不能据此宣称任意 grammar/FST 已完整覆盖。
- **Evaluation Contract:** YouTube path 使用 3B dense Gemini-based model、SID length 8、vocab 2048、
  20M fresh-item constraint、beam 70、batch 2/chip、TPU v6e、100 trials；STATIC 的约束逻辑增量为
  `0.033±0.008 ms/step`，约占该配置 inference time 0.25%。它相对 CPU Trie、exact/approx PPV 与
  hash bitmap 的数字绑定这些条件；approx PPV 只检查 top-50，hash bitmap 有 false positive，故不是
  等价 exact baselines。内存上界约为 17.3MB dense mask + 1.44GB later-level CSR，并在各 chip 复制。
- **Additional Evidence / Boundary:** YouTube A/B 报告 100% constraint compliance 与 fresh-view/CTR
  改善；这证明特定 recommendation deployment 的产品影响，不证明所有 constrained decoding 会改善
  用户价值。Amazon cold-start 使用 Gemma 1B、SID length 4、vocab 256、beam 20、batch 16、TPU v6e，
  并报告训练 70 epochs 中 peak Recall@1；它不是严格相同 compute/data 的通用 dense-vs-generative
  retrieval verdict。
- **What Evidence Proves / Does Not Prove:** 实验与 reference code支持 static CSR + branch-free fixed-width
  gather 能在给定 accelerator/workload 下精确执行 prefix constraints，并显著降低 constraint overhead；
  不证明 headline 47～1033× 能跨 vocab、branch distribution、beam、hardware 与 compiler 迁移，也不
  证明对 unconstrained generation 有收益，更不证明 offline rebuild 对高频 inventory change 足够。
- **Trade-offs / New Failure Modes / Old Branches:** 收益来自移除 host callback 和 divergence；成本是
  replicated HBM、offline construction/JIT、max-branch padding、dense/sparse split tuning，以及 constraint
  snapshot stale、matrix/request version mismatch、update thundering herd 和 rollback。论文明确把 dynamic
  sparse update 留作 future work。CPU Trie 在约束快速变化、小规模、可容忍 callback 或 memory 更紧时
  仍合理；approximate bitmap/top-k verification 在允许 false positive/recall loss 时仍是容量分支。
- **Evolution Relationship:** `Direct Evolution` of the physical execution of exact Trie constraints；不是对
  Trie semantics 的否定。它同时是 `Layering / Dependency` 于 generative retrieval：retrieval policy
  决定 constraint set，decode kernel 只保证输出属于该 snapshot。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 相邻阅读后将主 owner 从初筛 Ch52 修正为
  Ch40；Ch20 已定义 grammar mask 属于 token selection，Ch40 拥有逐步 state transition 与 runtime
  cadence，Ch45/46 是 engine implementation，Ch52 只负责 admission/scheduling，Ch72 负责 retrieval
  policy。现有 Ch20/40 只提 grammar state，没有解释“控制流 automaton 如何编译为 accelerator-native
  dataflow”及其 snapshot ownership，存在真实机制缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Constraint-State Representation and
  Snapshot Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续以 Ch40 为 owner，
  Ch20/72 只作短 handoff，production A/B 数字留在 Weekly。
- **Open Questions:** online inventory 如何增量更新 CSR 并给 in-flight request 保持 snapshot isolation？
  constraint matrix 与 model/tokenizer/SID codebook 怎样共同 version？高 branch factor、通用 grammar、
  variable length 与 beam cancellation 下的 HBM/latency frontier 是否仍成立？

### SWE-rebench V2

- **Candidate / Week / Score:** SWE-rebench V2 / 2026-W09 / 28/30；
  `Source Family ID: executable-swe-data-funnel-and-diagnostics`。
- **Source Type / Date / Revision:** arXiv:2602.23866 v1，首次公开 2026-02-27；当前 v2 为
  2026-06-01（ICML 2026）。本轮阅读全文、Appendix prompts/tables、作者 code repository，以及两份
  Hugging Face dataset cards。v2 和当前 artifacts 用于核验，不倒填成 W09 新事件。
- **Full-read Coverage:** Metadata、Introduction、Related Work、pipeline 3.1～3.7、setup/clarity
  experiments、task diagnostics、Discussion/Limitations、Conclusion、prompts、language funnel、per-language
  results 与公开 artifact surface 已读。
- **Original Problem / Why Previous Designs Were Reasonable:** 人工核验的 executable SWE benchmark
  能获得高可信环境和 oracle，适合发布门禁；单语言 template 又能可靠处理该 ecosystem。它们在数据量
  较小、evaluation stakes 高时合理，但 RL 需要大量可反复执行的环境，逐 task 人工 setup 无法跨 build
  system、dependency manager、test runner 与长尾语言扩展。
- **Changed Constraint / Principle:** SWE training sample 不是 `issue text + gold patch`，而是
  `repository snapshot + dependency closure + executable environment + F2P/P2P oracle + specification +
  diagnostic metadata`。所谓 language-agnostic 也不是零语言知识，而是统一 funnel 复用/生成少量
  language-specific base image、runner 与 log parser。
- **Mechanism / Data Flow:** pipeline 从 GitHub Archive 和 local git history 恢复 PR/issue/commit，要求
  permissive license、merged fix 与 test changes，将 diff 拆为 solution/test patch；setup Agent 按 repository
  合成 base Dockerfile、install/test commands 与 parser，成功配置在同 repo tasks 间复用。Validation 在
  base+test-patch 与 gold+test-patch 上提取 fail-to-pass/pass-to-pass，并用三次执行筛掉不稳定实例；LLM
  clarity filter 和 credential scan 再清理不明确/敏感样本，最后以 model trajectories 标注 test coupling、
  implicit naming、external dependency 等 confounders。
- **State Ownership:** source commit/PR 拥有任务历史；image digest/install config 拥有 executable snapshot；
  F2P/P2P lists 与 log parser 拥有 reward interpretation；clarity/diagnostic labels 绑定 judge、prompt、run
  与 confidence；dataset row 绑定 license、base commit、image 与 metadata。若只版本化 problem statement，
  training reward 无法审计。
- **Scale / Funnel Evidence:** 29.5M PRs 经 tests、issue linkage、repo filters、setup/validation 与 clarity
  funnel 收敛为 32,079 stable issue-linked tasks、3,617 repos、20 languages；另发布 120K+ PR-derived tasks。
  后者的 problem statement 由 PR description + patch 生成，在 509 项 leakage audit 中 23.0% 含某种 leakage、
  2.4% 含 explicit solution leakage，故是规模更大但更低置信的训练资源，不应与 issue-linked set 合并
  成单一 quality tier。
- **Evaluation Contract:** setup synthesis、prompt/model/ensemble clarity ablation 与 300-task diagnostic
  study 分开进行。diagnostic study 每种 Python/JavaScript/Go/Rust/Scala 抽 60 tasks，七个 models、
  mini-SWE-agent default parameters、每 task 三次运行；A 与 B* 比较匹配 language、modified files/lines。
  Verified-E clarity prompt 取 precision 优先，但 recall 很低；这会减少错误接纳，同时丢弃大量可能有效
  task，是 intentional operating point 而非“最好 judge”。
- **What Evidence Proves / Does Not Prove:** 论文证明自动 funnel 能产生大量可执行、多语言、带诊断
  metadata 的候选，并证明 A/B* labels 与该 300-task model-run success 存在明显分层；不证明 labels 是
  causal noise taxonomy，也没有执行 filtered-vs-unfiltered、clean-first-vs-noisy-first 的端到端 RL ablation。
  七模型 pass rates 评估的是 `model + mini-SWE-agent + environment + tests`，不是纯模型能力排行榜。
- **Limitations / Failure Modes:** 作者明确承认 Docker 仍受 package registry、system dependency、network
  resource drift 影响，single-container design 覆盖不了 database/queue/distributed services；自动 pipeline
  保留 underspecification、test coupling 与 environment noise。额外风险包括 regex 拆 test/solution 误判、
  repo-level setup 在 task 间失效、judge selection bias、PR-derived leakage、container supply-chain 与 image
  retention。当前 repository/dataset 是 mutable surface，未提供本轮可确认的 paper-run immutable manifest。
- **Old Branches / Evolution:** `Direct Evolution` from manually verified evaluation sets to automated
  training substrate，随后以 diagnostics 恢复部分 quality control。人工 verified subset 仍适合高风险 eval；
  automated noisy tiers 适合大规模 exploration；复杂 multi-service tasks 仍需要 richer environment orchestration。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch23 为主 owner；已读 Ch23～25、Ch29、Ch62
  与 Ch77。Ch23 已有 data provenance、dedup、quality gates 与 terminal `task + environment + verifier`
  contract；本候选新增的是把 environment/spec/oracle failure taxonomy 变成 curriculum/filter metadata，
  同时明确“diagnostic correlation 不等于训练收益”。Ch62/77 只需 evaluation/workflow handoff。
- **Integration Decision:** `Full Review Complete — Books Candidate / Executable-Environment Diagnostics as
  Data-Control Signal`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续与本周 terminal data
  engineering 合并 refine Ch23，避免重复两套 pipeline 描述。
- **Open Questions:** labels 在独立 human audit、不同 Agent harness 与未来 dependency snapshot 上是否仍
  校准？filtered/unfiltered curriculum 在等 tokens/compute 下怎样影响 RL？image、package mirror、test log、
  judge output 与 dataset revision 怎样绑定为可长期重放的 manifest？

### Memory Caching

- **Candidate / Week / Score:** Memory Caching: RNNs with Growing Memory / 2026-W09 / 26/30；
  `Source Family ID: recurrent-memory-capacity-granularity`。
- **Source Type / Date / Sources:** arXiv:2602.24281 v1，首次公开 2026-02-27；本轮阅读全文、公式、四种
  aggregation/selection 分支、complexity derivation、全部 experiments/ablation/efficiency、Related Work 与
  Appendix B。没有定位到作者公开 code/artifact；论文只有 v1。
- **Full-read Coverage:** Metadata、Introduction、Preliminaries、Memory Caching 3.1～3.4、proof-of-concept
  discussion、segmentation、SWLA/DLA/Titans mapping、LM/needle/retrieval/LongBench/MQAR、ablation、
  efficiency、Conclusion、Related Work 与 Experimental Details 已读。论文没有独立 Limitations/Threats
  章节；本轮根据未披露 hardware、artifact 缺失和实验范围标明外推边界。
- **Original Problem / Why Previous Designs Were Reasonable:** recurrent/linear-attention model 用固定大小
  state 压缩全部历史，带来 O(L) update 与固定 decode state，适合长流式处理；Transformer 保存 token-level
  history，取得直接寻址与强 recall，却承担 O(L²) attention 与随长度增长的 KV。两者都针对不同 capacity/
  compute 目标合理，问题是固定 recurrent state 在 recall-intensive long context 中被持续覆盖。
- **Changed Constraint / Principle:** Memory Caching 把“保存所有 token / 只保留最后 state”的二元选择
  变成粒度轴：按 segment 保存压缩 memory checkpoints。segment 越短，历史分辨率与 cache 数越高；
  segment 越长，compute/memory 越低但压缩冲突更大。它增长的是 compressed-state capacity，不是恢复
  token-level provenance。
- **Mechanism:** sequence 被分成 N 个 segments，每段 recurrent memory 继续在线 update，并缓存段末
  state。Residual Memory 对当前 query 聚合全部 cached states；Gated Residual Memory 用 query 与 segment
  pooled context 计算 `gamma`；Memory Soup 先插值 memory parameters，再执行 query，对 nonlinear deep
  memory 不再等价于 output ensemble；SSC 用 MoE-style router 选 top-k segment memories，只加载所选
  states。系统还区分单一 memory 的 optimization checkpoints 与彼此独立的 segment compressors。
- **State Ownership / Control and Data Flow:** segmenter 拥有 boundary/length；online memory 拥有当前段
  update；cache 拥有每段 checkpoint 与 segment summary/key；router/gate 拥有 query-to-segment selection；
  aggregator 产生当前 output。迁移/重试必须同时恢复 online state、cached checkpoints、segment boundary
  与 router parameters；只恢复“最后 hidden state”会丢掉算法语义。
- **Complexity / Alternatives:** update 仍约 O(L)，若每 token 对 N 个 memory states 做 retrieval，总成本
  O(NL)（更细写为 O(L+pNL)）。固定 segment C 得到约 O(pL²/C)；logarithmic segmentation 可到
  O(pL log L)，却降低远历史分辨率并可能让某些大段 memory overflow。N=1 退化为 fixed-state RNN，
  N=L 接近 token-level growing memory；SSC 再用 selection 把 load/compute 与全部 cache 容量部分解耦。
- **Evaluation Contract:** 760M/1.3B models 分别训练 30B/100B tokens，vocab 32K、train length 4K～32K、
  AdamW、0.5M-token batch；比较 Transformer++、Samba、RetNet、DeltaNet、RWKV-7、MIRAS、SWLA、DLA、
  Titans 及 MC variants，并覆盖 LM/common-sense、needle、六类 retrieval、LongBench、MQAR。论文未披露
  GPU/TPU 型号、precision、并发或 serving SLO，throughput figure 因而不能外推为生产 speedup。
- **Ablation / Evidence Boundary:** GRM/Soup/SSC 多数任务改善 base recurrent model，但最佳分支随
  task/architecture 变化；Transformer 在 in-context recall 仍最好。context-dependent gate、gating 与 deep
  memory ablations 支持各组件在该 recipe 的贡献，但 Table 5 的 shared-u/q rows 显示 `00.0`，不能当有效
  测量。论文证明 checkpoint granularity 是可行 capacity/compute axis，不证明 attribution“收益只来自
  larger effective memory”，也不证明任意 RNN、超长 deployment 或 untrained extrapolation 成立。
- **Trade-offs / New Failure Modes / Old Branches:** 新增 checkpoint memory、per-query aggregation/router
  compute、segment-boundary sensitivity、router miss/load imbalance、state spill/migration、checkpoint
  staleness 和 nonlinear soup instability。固定 RNN 在 streaming、极低 memory 和 approximate history
  足够时仍合理；full attention 在精确 recall、provenance 和高 quality budget 下仍合理；hybrid window+
  recurrence 是另一条共存分支。
- **Evolution Relationship:** `Direct Evolution` from fixed recurrent compression to checkpointed
  multi-resolution compressed history；与 full attention 是 continuum/coexistence，而不是单向替代。
  与 Agent Memory 只有 `Principle Reuse`，不具备用户 consent、durability、provenance 或 delete semantics。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch22 为主 owner；已读 Ch14、Ch19、Ch22、
  Ch41 与 Ch73。Ch22 已有 Titans/MIRAS、fixed latent state 与 exact KV coexistence，但尚未把“缓存多个
  compressed checkpoints + segmentation/selection”写成 attention↔recurrence 之间的显式容量轴。Ch41 的
  KV cache 与 Ch73 的 Agent memory 只作语义边界，不能复用其治理结论。
- **Integration Decision:** `Full Review Complete — Books Candidate / Compressed-State Checkpoint
  Granularity Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续 refine Ch22，
  保留 Transformer 与 fixed-state RNN 的成立条件，不写作者平均分或 throughput headline。
- **Open Questions:** checkpoint identity、segment boundary 与 router state 怎样进入 production cache/migration
  contract？SSC selected states 若不常驻 accelerator，load latency 与 batch divergence 如何影响 TPOT？
  更长于 train context、不同 segment distribution 与 fixed HBM budget 下的 quality frontier 是否可复现？

### Tool-R0

- **Candidate / Week / Score:** Tool-R0: Self-Evolving LLM Agents for Tool-Learning from Zero Data /
  2026-W09 / 26/30；`Source Family ID: competence-frontier-self-play-tool-learning`。
- **Source Type / Date / Sources:** arXiv:2602.21320 v1，首次公开 2026-02-24；本轮阅读全文、公式、
  Generator/Solver prompts、dataset construction、全部 evaluation/ablation、Challenges 与 Appendices B～H，
  并核验作者 project page、GitHub implementation、Hugging Face models 与公开 W&B 链接。论文只有 v1；
  W&B 链接本轮无法直接抓取，不能把 dashboard 当作独立 reproduction evidence。
- **Full-read Coverage:** Metadata、Introduction、Related Work、grounded task specification、Generator/
  Solver rewards、三轮 self-play、supervised baselines、scaling/iteration analysis、training dynamics、
  challenges、完整 hyperparameters、evaluation adapter 与 algorithm appendix 已读。公开仓库有 reward、
  generation、verification、curriculum selection 和 solver training scripts，但仅 2 次 commit，未提供锁定
  paper run 的 immutable environment/manifest。
- **Original Problem / Why Previous Designs Were Reasonable:** curated tool-call demonstrations 能提供
  human-selected tasks、稳定 gold calls 与清晰训练分布，适合接口固定、失败成本高或 verifier 难以自动化
  的环境；静态 synthetic generation 也便于一次审查后复用。边界在于 Solver 能力随训练变化后，固定数据
  可能持续落在过易、过难或偏离部署需求的区域，数据生成本身没有闭环感知当前 competence frontier。
- **Changed Constraint / Principle:** Tool-R0 把 curriculum generation 与 policy learning 组织成两个
  相互反馈但参数分离的 optimization loops：Generator 生成 Solver 当前可能学会的任务，Solver 的成功率
  反过来定义下一轮难度。这里所谓“zero data”只表示没有外部 task-level training examples；系统仍依赖
  pretrained base model、人工定义的 30 多个 domain/config distributions、结构化 prompts、reward rules
  以及五个外部 evaluation benchmarks，不能外推为零先验或零人工设计。
- **Mechanism:** Generator 输出 `<question>`、`<available_tools>` 与 gold `<tool_call_answer>`；format reward
  检查 tags/JSON，validity reward 检查 tool 存在、required arguments 与 argument value 是否在问题中出现。
  当前冻结 Solver 对每题采样 `K=8`，用 pass-rate band `[0.25,0.75]` 和 Gaussian width `0.12` 奖励
  competence-frontier tasks，再以 Solver judge 给 semantic coherence。每轮先用 2,000 self-generated
  samples 训练 Generator，冻结后生成 10,000 tasks，经 canonical dedup、cross-solver agreement 与
  difficulty balancing 筛成 2,000 Solver samples；Solver reward 再分解 parse/normalize、tool-name/key/value
  match 和额外调用 penalty。
- **State Ownership / Control and Data Flow:** practitioner 拥有 domain/tool-distribution specification；
  Generator checkpoint 拥有 task proposal policy；frozen Solver snapshot 同时充当 difficulty probe 与
  semantic judge；curation pipeline 拥有 generated-task identity、dedup signature、agreement 和 bucket；
  Solver checkpoint 拥有 execution policy。每轮必须绑定 Generator/Solver versions、prompt/reward versions、
  sampled tasks 和 selection result，否则无法区分 curriculum 进步、judge drift 与 Solver 进步。
- **Training / Evaluation Contract:** Qwen2.5 0.5B/1.5B/3B 与 Llama-3.2-3B；主要实验三轮、每轮两侧各
  50 steps。Generator/Solver 均使用 GRPO、bf16、4 rollouts、max length 4096、learning rate `1e-6`，
  global batch 分别 24/32；论文只披露 mixed-precision ZeRO-3 训练使用 3 GPUs，未披露 GPU 型号、总
  wall-clock、能耗或 deployment SLO。评测为 ToolAlpaca、SealTool、NexusRaven、API-Bank、SNIPS 的
  AST matching；1.5B 平均 24.85→47.84 只属于上述 benchmark adapter 与该 checkpoint/recipe。
- **Ablation / Evidence Boundary:** shared weights、frozen Generator、移除 difficulty reward 与 hard-cliff
  reward 分别在该 recipe 下下降 17.42、6.19、4.30、3.74 percentage points，支持角色分离和动态难度
  的局部贡献；但没有多 seed standard error，作者明确受 compute/hardware 限制。training-corpus 与 test
  corpus cosine similarity 只能说明相关性，不能证明“模型最知道自己需要什么数据”。小模型第三轮附近
  饱和或回落也只是有限迭代观察，不能证明 Nash equilibrium 或知识边界。
- **Trade-offs / New Failure Modes / Old Branches:** 获得 adaptive curriculum 的代价是每题 8 次 difficulty
  probes、双 checkpoint、反复生成/过滤与更大的 reward-governance surface。Generator 与 Solver 共用
  prior 和 judge blind spots，可能形成 collusion、reward hacking、semantic false positives、curriculum
  collapse、benchmark-shaped distribution 与 early saturation；schema 只检查 required fields、未严格检查
  types，generated gold 证明的是 closed-world consistency，不是真实 API execution correctness。curated
  human data 在高风险、长尾语义、真实副作用和独立 ground truth 必要时仍然成立，hybrid self-play→human
  post-training 也是论文自己观察到的共存分支。
- **Evolution Relationship:** `Direct Evolution` from static synthetic curriculum to solver-calibrated
  co-evolution；与 GRPO 是 `Layering / Dependency`，与 Tool Calling runtime 是 training/runtime boundary，
  不是“训练成功即可授权执行真实工具”。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch29 为主 owner candidate；已读 Ch23～25、
  Ch28～30、Ch74、Ch75 与 Ch77。Ch29 已有 group success-rate、curriculum、verifier-as-interface 与多阶段
  training，但尚未明确双 policy 的 role separation、competence feedback 和 cross-version curriculum
  identity。Ch74 只接收“training correctness 不等于 runtime authorization/execution correctness”的短
  handoff；Ch23/75/77 不重复生成流程。
- **Integration Decision:** `Full Review Complete — Books Candidate / Co-evolving Curriculum and
  Role-Separation Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续只在 Ch29
  refine 双控制环及其失败模式，不写“zero data”宣传语或 benchmark headline。
- **Open Questions:** 如何用独立 verifier、held-out real API tasks 与 periodically refreshed human data 防止
  Generator/Solver 共谋？difficulty probe 的 8 倍 rollout cost 能否用 calibrated loss/learning-progress signal
  替代？checkpoint promotion、curriculum rollback、model-family transfer 和真实副作用 safety gate 怎样进入
  production training contract？

### LongVideo-R1

- **Candidate / Week / Score:** LongVideo-R1: Smart Navigation for Low-cost Long Video Understanding /
  2026-W09 / 23/30；`Source Family ID: hierarchical-active-perception-video-navigation`。
- **Source Type / Date / Sources:** arXiv:2602.20913 v1，首次公开 2026-02-24；本轮阅读全文、算法、
  reward、三组 benchmark、全部 ablation/cost tables、implementation/training appendix、data-generation
  prompts 和 failure cases，并核验作者 GitHub/data/model entry。论文只有 v1；仓库是当前可变 artifact，
  未定位到锁定论文结果的 immutable manifest。
- **Full-read Coverage:** Metadata、Introduction、Related Work、hierarchical video definition、CoTWT data
  curation、SFT、GRPO、reward design、LVBench/MLVU/Video-MME-long、ultra-long cases、future directions、
  Appendices A～D 已读。论文没有独立 Limitations/Threats 章节；本轮以作者 failure case、tool dependence、
  per-question assumption、training-data construction 和未披露 serving conditions建立外推边界。
- **Original Problem / Why Previous Designs Were Reasonable:** uniform/adaptive frame sampling 把视频直接交给
  MLLM，路径短、batch 友好，并适合全局摘要或短视频；固定间隔 caption/indexing 预计算成本清晰，也能
  在一段视频对应多问题时摊薄。长达数小时且问题只依赖局部片段时，这些方案会在 irrelevant frames 上
  消耗 tokens/compute，或让 sampling density 随 duration 线性增长。
- **Changed Constraint / Principle:** 当 relevant evidence 稀疏、问题到来后才知道应看哪里时，感知本身
  变成 budgeted search，而不是一次性 model input。LongVideo-R1 以固定深度、随 duration 调宽的时间树
  提供 coarse-to-fine address space，让 reasoning model 在 caption 的廉价全局线索与 leaf-level video QA
  的昂贵精查之间选择；收益来自 placement policy，不等于 underlying MLLM 视觉能力本身提升。
- **Mechanism:** 视频构造成 `D=3` 的均匀 temporal tree，leaf 约 16 秒，`W≈(Duration/16)^(1/D)`，通常
  4～8。`video_cap` 可访问已展开节点，`video_qa` 仅用于 leaf；不同层用 256/128/64/32 frames 并调分辨率，
  使单次 caption visual-token budget 近似恒定。Agent 从最高层 child captions 出发，反复 reasoning→选择
  node/tool→接收 observation→更新 history，直到回答或 max rounds。RL reward 合并 answer correctness、
  访问区间与 clue-ground-truth 区间的 F1-like localization reward，以及 repeated-visit penalty。
- **State Ownership / Control and Data Flow:** tree builder 拥有 segment identity、depth/width 和 timestamp；
  caption/QA tools 拥有各自 model/version 与 observation；planner history 拥有 visited nodes、reasoning rounds
  和 answer state；runtime 拥有 max rounds/cost。训练期 location oracle 属于 dataset/reward system，不是
  deployment observation。若要缓存/复用，必须绑定 video hash、tree policy、caption model/prompt 与 node
  outputs；只保存自然语言 history 无法重建同一搜索状态。
- **Data / Training Contract:** CG-Bench 约 1,200 videos/12,000 QA；800 videos 用于 SFT data construction，
  filtering 后得到约 5,600 CoTWT trajectories，另 400 videos/约 4,200 QA 用于 RL。root-only GPT-5 teacher
  约 30% 失败后，pipeline 改为先展示所有 top-level children，并在失败时逐层注入 clue-grounded timestamp
  hints 直至回答正确；因此 SFT trajectory 含 oracle-assisted localization，不能称为 agent 独立发现路径。
  central model Qwen3-8B，8×H800 80GB、mixed precision/FSDP、sequence 32K；SFT/RL 分别 3/2 epochs、
  global batch 32/12、384/696 steps，RL 16 rollouts，2 GPUs serving Qwen2.5-VL-32B QA、6 GPUs training。
- **Evaluation / Cost Contract:** evaluation 使用 Qwen2.5-VL-72B caption、32B QA，测试 LVBench（103 videos、
  1,549 QA、平均 4,038 秒）、Video-MME-long（300 videos、每视频 3 QA、平均 41 分钟）和 MLVU（1,337
  videos、3 分钟～2 小时），均按 multiple-choice exact match。A800 timing 将 reasoning、caption、QA calls
  分解；Video-MME-long 平均 10.5 reasoning、14.14 caption、0.36 QA calls，估算约 135 秒/题。没有披露
  concurrency、batching、preprocessing amortization 或 serving SLO，不能把“2～3 分钟”写成通用成本。
- **Ablation / Evidence Boundary:** full SFT data、RL 与 localization reward 在该 setup 中改善结果；但
  `w/o r_loc` 仍包含 RL，不能把差值归成“RL 是否有效”的完整对照。caption model size 与 max rounds
  tables 展示 accuracy/cost 非单调 frontier；updated variant 又换成 Qwen3-VL-32B caption 并重新 SFT，不能
  与原始模型混为单一机制增益。LongVideo-R1 在 LVBench 的 retrieval/grounding slice 更强，但在 MLVU/
  Video-MME 并未领先 open-source MLLMs；超长视频只给 case evidence，不是规模化 evaluation。
- **Trade-offs / New Failure Modes / Old Branches:** coarse-to-fine search 减少无关 frame exposure，却新增
  caption hallucination/omission、错误 branch lock-in、semantically related distractor、tree-boundary miss、
  repeated traversal、tool-model bottleneck、history growth 和多模型 deployment cost。作者 failure case 显示
  简单 hint 可纠偏，也说明系统缺少稳定自我回退。uniform sampling 在短视频、全局问题和大 batch 下仍
  合理；预计算 index 在 multi-QA/增量问答中可摊薄；更强 native long-video MLLM 是并存分支。
- **Evolution Relationship:** `Direct Evolution` from fixed observation placement to query-conditioned
  hierarchical active perception；与 Ch74 Tool Calling 是 `Layering / Dependency`，与 Ch29 localization
  reward 是 training layer，不能用后者覆盖 runtime planning/cost semantics。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch75 为主 owner candidate；已读 Ch29、Ch62、
  Ch74、Ch75 与 Ch77。Ch75 已覆盖 partial observability、tree search、replanning 和 budgets，但尚未把
  “observation acquisition itself is a typed, costed plan action”及 coarse-to-fine evidence placement 写成
  明确机制。Ch74 已有 tool contract/loop boundary，只需短 handoff；Ch62 负责 benchmark/environment identity。
- **Integration Decision:** `Full Review Complete — Books Candidate / Hierarchical Active-Perception Search
  and Cost Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续 refine Ch75 的主动
  observation placement、cost model 与 fallback，不复制视频 benchmark 表。
- **Open Questions:** tree width/depth 能否由 question uncertainty、caption confidence 与 cost budget 动态选择？
  错 branch 如何触发 backtracking/replanning？多问题共享同一视频时，caption/index cache 的 provenance、
  invalidation 和 amortized SLO 怎样定义？去掉 clue-grounded hints、换弱 caption/QA tools 或长于训练分布时，
  localization policy 是否仍保持收益？

### Reinforcement-aware Knowledge Distillation / RLAD

- **Candidate / Week / Revised Score:** Reinforcement-aware Knowledge Distillation for LLM Reasoning /
  2026-W09 / 24/30（初筛 25；`Source Reliability 4→3`）；
  `Source Family ID: advantage-aware-on-policy-reasoning-distillation`。
- **Source Type / Date / Revision:** arXiv:2602.22495 v1 首次公开 2026-02-26；当前 v3 为 2026-06-17，
  标注 ICML。本轮阅读全文、全部公式、logic/math setups、baselines、ablation、efficiency、limitations 与
  Appendices A～C；v3 用于机制和 revision 核验，不把六月新增内容倒填为 W09 新事件。未定位到作者公开
  code、training logs 或 immutable artifact。
- **Original Problem / Why Previous Designs Were Reasonable:** offline trace distillation 只需一次 teacher
  generation，训练稳定、可缓存且不要求同时部署 teacher，适合预算受限和高质量 demonstrations 可获得的
 场景；on-policy KL distillation 则在 student 自己的 rollout 上查询 teacher，可减轻 exposure mismatch。
  但 fixed traces 不跟随 student distribution 演化，而无条件 teacher KL 可能与当前 reward advantage 冲突，
  尤其 teacher/student 差距大或 teacher 在某些轨迹上并不优时。
- **Changed Constraint / Mechanism:** RLAD 不把 teacher divergence 作为独立、始终同向的 loss，而把
  teacher 置入 clipped policy ratio 的 anchor。对 student rollout token，TRRD 使用
  `(π_new/π_old)^α · (π_new/π_teacher)^(1-α) = π_new /(π_old^α π_teacher^(1-α))`，再乘同一
  group-relative advantage 并执行 PPO/GRPO-style clipping。正 advantage 且 teacher 也偏好的 token 可在
  更晚处触及 upper clip；teacher 低概率 token 更早被限制。负 advantage 时，teacher 高概率 token 的下降
  同样更早受 lower clip 约束，因此 imitation 被 reward sign 调制，而不是拥有独立梯度方向。
- **Formula / Revision Integrity Boundary:** 按公式，`α=1` 才退化为 standard GRPO，`α→0` 才趋向
  teacher-anchored imitation；Appendix C 也如此解释。但 v3 主文第 4.1 节有一句把两个端点反写。这个
  内部矛盾是本轮下调 Source Reliability 的直接原因；Books 若吸收只能引用公式与 Appendix 一致的解释，
  不能照抄错误 prose。teacher/student 初始 ratio 过大时，作者另把 log ratio clamp 到 `[-1,1]`，这也是
  objective 的实质实现条件，不是可省略的数值技巧。
- **State Ownership / Control and Data Flow:** old student 生成 rollouts 并定义 on-policy anchor；current
  student 接收 update；teacher 只对 student rollout 计算 token log-probabilities；fixed reference 仍承担
  原 GRPO KL；verifier 产生 sequence reward/advantage。一次可恢复训练必须同时绑定四个 policy identities、
  tokenizer/vocabulary alignment、rollout policy version、teacher-logprob cache、`α`、clip/log-ratio clamp 与
  reward version。closed-source teacher 无 logits 时，该机制不能直接使用。
- **Evaluation Contract:** logic 使用 Qwen3-0.6B/1.7B students、Qwen3-8B teacher、K&K Logistics、8×H200、
  group 8、global batch 256、2K/8K generations；math 使用 105K Skywork-OR1、Qwen3 1.7B/8B base 与
  post-trained students、8B/32B teachers、8K/30K response budget、64×H200、global batch 256、最多 5 epochs。
  五个 math tests 以 temperature 0.6、top-p 0.95、32 decodes 报 Mean@32/Pass@32。checkpoint 按 AIME24
  validation 最优选择，但论文又报告 AIME24；未说明 selection/evaluation 是否严格隔离，需保留调参边界。
- **Ablation / Efficiency / What Evidence Proves:** `α` sweep、weak-teacher test 和 clipping-frequency trace
  支持“mixture anchor 在该 recipe 下确实生效且比独立 KL 更不易被弱 teacher 拉偏”。但没有 multi-seed
  training variance；STD@32 只是同 checkpoint decoding variance。32×H200 efficiency experiment 中，teacher
  与 student colocated，global/micro batch 256/16；RLAD/KDRL 约比 GRPO 增加 12% batch latency，只能用于该
  placement。作者关于 remote teacher overhead 会更接近 GRPO 的说法没有远程实验支撑，也未计网络/SLO。
- **Trade-offs / New Failure Modes / Old Branches:** 获得 adaptive teacher guidance 的代价是每个 student
  rollout 的 teacher logits、额外 model residency/communication、tokenizer compatibility 和四-policy state。
  新增 teacher-logit staleness、ratio under/overflow、clamp-induced bias、teacher blind spot、reward-verifier
  bias 与 validation selection leakage。offline distillation 在 teacher serving 昂贵、data distribution 稳定或
  reproducibility 优先时仍合理；plain GRPO 在 teacher 不可信/不可用时仍合理；independent KL 在需要明确
  可解释 imitation strength 时仍是可审计分支。
- **Evolution Relationship:** `Direct Evolution` from offline/off-policy trace imitation → on-policy KL
  distillation → advantage-conditioned mixture-anchor distillation；并非 RLAD 单向取代前三者。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch29 为主 owner candidate；已读 Ch24、Ch28～30。
  Ch29 已有 offline reasoning-trace distillation、group-relative advantage、reference KL 与 curriculum，但尚未
  写明 teacher guidance 可以进入 trust-region anchor 并由 advantage sign 选择性调制。Ch28 只需 old/reference
  state handoff，Ch30 只保留 Appendix 所称 DPO-like analogy，不把 TRRD 等同于离线 preference DPO。
- **Integration Decision:** `Full Review Complete — Books Candidate / Advantage-Conditioned Teacher-Anchor
  Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续 refine Ch29 时必须连同公式
  端点纠错、四 policy state 与 teacher-logit cost 一起写入。
- **Open Questions:** v1→v3 的公式/prose 改动是否引入端点反写？AIME24 checkpoint selection 与 reported
  evaluation 是否使用独立 split？跨 tokenizer/vocabulary teacher 怎样定义 token ratio？在等 total compute、
  多 seed、remote teacher 与 stale logprob 下，RLAD 相对 offline/KDRL 的收益和 stability 是否仍成立？

### CiteAudit

- **Candidate / Week / Score:** CiteAudit: You Cited It, But Did You Read It? / 2026-W09 / 23/30；
  `Source Family ID: bibliographic-existence-and-metadata-audit`。
- **Source Type / Date / Revision:** arXiv:2602.23452 v1 首次公开 2026-02-26；当前 v3 为 2026-05-01，
  revision note 说明 benchmark construction、verification pipeline 与 results 已更新。本轮阅读全文、taxonomy、
  benchmark construction、human annotation、multi-agent SOP、全部 experiments/cases/prompts，并核验作者
  GitHub code 与 9,442-row dataset。v3 用于核验 current evidence，不把五月结果倒填为事件周事实。
- **Original Problem / Why Previous Designs Were Reasonable:** DOI/arXiv/title exact lookup 成本低、规则透明，
  在 citation 格式完整且 bibliographic database 覆盖充分时比 LLM judge 更可靠；fuzzy matching 可容忍格式
  变化。但真实 PDF extraction、preprint→publication metadata、author name normalization 与跨库 coverage
  让单库/单字段匹配产生 false reject/accept，尤其“真实 work + 错 metadata”与“完全不存在”需要不同证据。
- **Benchmark Mechanism:** generated test 含 3,586 real + 2,500 controlled fake citations；real-world test 含
  2,889 real + 467 naturally observed errors，总计 9,442。taxonomy 覆盖 title、author、venue/year/identifier
  和 compound perturbations。作者团队以 web/search/scholarly sources 逐项验证，至少两名作者独立审查，
  disagreement 通过团队 consensus，无法 consensus 的项被排除；没有报告 inter-annotator agreement 或
  excluded count，random recheck 比例也未披露。
- **System Mechanism / State Ownership:** paper 把 PDF→metadata extraction、verified-memory fast path、web
  search、judge consistency check、Scholar fallback 和 final verdict 编排成四级 SOP。citation tuple 保留
  title/author/URL/venue/year；cache 命中阈值 0.92；未命中才升级至 web，再将 unresolved case 升级至
  scholar source。extractor 拥有 parsed metadata，retrievers 拥有 source candidates，judge 拥有 field-level
  verdict，memory 拥有 previously verified result，orchestrator 拥有 escalation state。可靠 cache identity 必须
  包含 citation canonicalization、source/version、verdict time、evidence URL/digest 与 supersession policy。
- **Implementation / Evaluation Contract:** paper reports Qwen3-VL-235B-A22 extraction on B200、Gemini 3
  Flash planning/judgment、Google Search/Scholar retrieval、Mem0 memory、thread pool 4、temperature 0、
  10-reference runtime and provider price estimates。当前 repository 只有 1 commit，公开 `pdf_processor.py`、
  `serp_verify.py`、runner 与 dataset；README 运行路径依赖 Gemini/OpenAI/SerpAPI、约 8K～9K SerpAPI calls，
  并未完整呈现论文所述 five-agent/Mem0/B200 orchestration。故 code 证明可运行的简化 pipeline 与数据存在，
  不足以独立复现论文 headline metrics。
- **Evidence Boundary / Statistical Concerns:** generated-vs-real fidelity 只以 GPTZero 对两组 fake citations 的
  `Pred Fake/Pred Real` 2×2 chi-square 得到 `p=0.994`；这最多说明该单一 detector 的二元输出比例相近，
  不能证明 error taxonomy、difficulty 或全体系统上的 distributional equivalence。real-world ambiguous cases
  被排除会弱化最难 deployment slice。论文没有 component ablation，无法把收益归因于 multi-agent 分工、
  scholar fallback、memory 或 judge。模型/API 版本、provider retrieval 和 live web 都会漂移；价格也不是
  可长期复现的系统属性。
- **Trade-offs / Failure Modes / Old Branches:** staged escalation 可把昂贵 search 留给 ambiguous cases，并
  保存 provenance；新增 OCR extraction error、false cache hit、stale/corrected publication metadata、source
  coverage bias、judge over-rejection、API nondeterminism、rate/quota failure 和 poisoned web evidence。exact
  identifier verification 在 DOI/arXiv ID 可用时仍应是 deterministic fast path；high-impact rejection 需要
  human appeal，不能由 binary model verdict 自动覆盖作者记录。
- **Evolution Relationship:** `Layering / Dependency`：deterministic identifier lookup → normalized/fuzzy field
  match → multi-source retrieval → evidence-bearing escalation；不是“多 Agent 数量越多越可靠”。citation
  existence/metadata consistency 与 claim-to-source entailment 是两种不同 evaluation objects。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 复核 Ch62、Ch72、Ch73 与 Ch77 后，主 owner
  仍是 Ch62，但现有正文已明确 claim-level provenance、citation existence 不等于观点支持、subject/source/
  scorer/version identity 与 evidence-bearing evaluation。Ch72 已覆盖 source provenance/freshness，Ch73 已覆盖
  memory provenance/supersession，Ch77 已覆盖 deterministic spine/escalation。因此当前论文没有形成新的
  长期机制缺口；其具体 taxonomy、benchmark 数值和 product stack 留在 Weekly。
- **Integration Decision:** `Full Review Complete — No Change / Already Covered / Weekly Only Benchmark
  Evidence`。不修改 Books，不把 v3 benchmark headline 或当前 vendor/model names 写入长期正文。
- **Open Questions:** v1/v2/v3 dataset 与 headline results 如何逐版本变化？论文 five-agent architecture 与公开
  简化代码之间哪些组件缺失？如何对 retraction、author correction、preprint/final merge、同名 work 与
  poisoned search result 建立 time-aware source authority？citation existence 通过后，claim entailment 应由谁
  独立验证？

### Recovered in Translation

- **Candidate / Week / Score:** Recovered in Translation: Efficient Pipeline for Automated Translation of
  Benchmarks and Datasets / 2026-W09 / 22/30；
  `Source Family ID: multilingual-benchmark-semantics-preserving-compilation`。
- **Source Type / Date / Sources:** arXiv:2602.22207 v1，首次公开 2026-02-25；本轮阅读全文、方法、
  translation/evaluation tables、language-specific error cases、appendix 与 Limitations，并核验作者 GitHub
  pipeline、configuration contract 和公开 benchmark dataset entry。论文只有 v1；当前 repository/Hub
  artifact 可继续变化，未见锁定论文运行的 immutable manifest。
- **Original Problem / Why Previous Designs Were Reasonable:** 把每个 field 独立机器翻译，成本低、吞吐高，
  对普通 corpus sentence 或高资源语言常是合理起点；直接复用已有 multilingual benchmark 也保持了跨工作
  可比性。但 benchmark 的 question、context、choices 与 answer identity 是联合对象，独立翻译会造成语义
  drift、语法不一致、选项可见线索和 task structure 破坏，使最终分数同时测到模型能力与翻译 artifact。
- **Changed Constraint / Mechanism:** framework 明确区分 `Dataset` 与 `Benchmark` mode。SC 做 zero-shot
  translation 与可选独立 self-check；Best-of-N 采样后由 judge 打分选择；USI 让 evaluator 综合多个候选；
  T-RANK 用多个 prompt 生成候选、轮换位置做多轮排序，再修正首选。长期机制不是“多调用更好”，而是把
  localization 当作带 schema、cross-field constraints、selection policy 与 correction stage 的编译过程。
- **State Ownership / Control and Data Flow:** source benchmark 拥有 item/schema/label identity；translator
  拥有 candidate text 与 model/prompt/sampling identity；judge/ranker 拥有排序和修正 evidence；pipeline
  负责把 question/choices 保持为同一 translation unit；publisher 拥有 target-language dataset digest。
  可审计 artifact 还需记录 source row id、field mapping、candidate lineage、selected candidate、human
  override 与 target-language QA，不能只保存最终字符串。
- **Evaluation Contract:** 方法先在 WMT24++、FLORES 的 English→Ukrainian 上用 XCOMET-XL reference
  COMET 比较，主要 translator 为 `GPT-4o-mini-2024-07-18`；随后在八种 Eastern/Southern European
  languages 上用 COMET-QE、LLM-as-a-judge，并以 Gemma 3、Qwen 3、Llama 3.1 运行 MMLU、HellaSwag、
  ARC-Challenge、Winogrande。不同实验使用的 translator、judge、prompt、sample count 与 benchmark/model
  matrix 不完全相同，不能把汇总平均提升写成单一、普遍的 translation gain。
- **What the Evidence Proves / Does Not Prove:** COMET 与逐例语言错误支持“联合上下文与多候选选择在该
  language/task matrix 中可改善部分翻译”；Winogrande morphology 和 HellaSwag cohesion cases 直接说明
  schema-aware translation 的必要性。但 T-RANK 即使轮换仍明显偏好 input position 2；USI/T-RANK 并非
  所有表格都优于简单分支，部分 downstream model/benchmark cells 为零或负增益，专业 Bulgarian
  Winogrande translation 仍优于自动方案。更高 model accuracy 也不能单独证明 translation 更忠实：新版本
  可能只是更容易、产生 leakage，或改变 item difficulty。
- **Limitations / Artifact Boundary:** 作者明确承认 Best-of-N selection 依赖 LLM scorer、未按 item
  difficulty 自适应选方法、昂贵方法在短文本上未必更好、主要使用 closed models，语言范围也局限于
  Eastern/Southern Europe。公开代码证明 SC/BoN/USI/T-RANK、multi-provider config、COMET/LLM-judge
  与 manual-review path 存在；它不等于所有发布数据已由独立人类逐项确认，也不固定 provider API 行为。
- **Trade-offs / New Failure Modes / Old Branches:** multi-candidate pipeline 以更多 token、latency、API
  nondeterminism 与 correlated judge bias 换取候选多样性；新增 label leakage、answer identity drift、
  position bias、model-family self-preference、language-specific morphology failure 与 dataset version
  fragmentation。SC/人工翻译在短文本、高风险、小规模或审计优先场景仍更合理；专业人工 translation
  是 stronger evidence branch，不被自动 pipeline 取代。
- **Evolution Relationship:** `Direct Evolution` from field-wise text translation → schema-aware benchmark
  localization → multi-candidate selection/correction → language-specific and human audit。它与 Ch23 data
  lineage 是 `Layering / Dependency`，但 evaluation-claim ownership 属于 Ch62。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch62 为主 owner candidate；已读 Ch23 与 Ch62。
  Ch62 已要求 dataset identity、schema/task definition、scorer identity、position-bias calibration 与 per-example
  evidence，但尚未明确 derived/translated benchmark 必须保留 task invariants、label identity、difficulty
  comparability 与 transformation lineage。Ch23 只负责通用 data lineage/contamination，不重复评测语义。
- **Integration Decision:** `Full Review Complete — Books Candidate / Benchmark Translation as
  Semantics-Preserving Compilation Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；
  后续只 refine Ch62 的 derived-evaluation-asset contract，不复制八语言表格或厂商模型名。
- **Open Questions:** 如何以 bilingual human gold 分别校准 semantic fidelity、item difficulty 与 label
  leakage？翻译后是否还保持原 benchmark 的 IRT/difficulty ordering 和跨语言 comparability？当 translator
  与 evaluated model 同源时，如何识别 shared preference？source benchmark 修订后怎样执行 item-level
  incremental rebuild、supersession 与 rollback？

### SenCache

- **Candidate / Week / Score:** SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware
  Caching / 2026-W09 / 23/30；`Source Family ID: sensitivity-bounded-diffusion-output-reuse`。
- **Source Type / Date / Sources:** arXiv:2602.24208 v1，首次公开 2026-02-27；本轮阅读全文、公式、算法、
  implementation、三模型 experiments、ablation、discussion 与 appendix，并核验作者 GitHub 中 Wan2.1、
  CogVideoX、LTX-Video 的实现目录、sensitivity calculation 与运行参数。论文只有 v1；当前代码有 22 个
  commits，但未以 immutable manifest 锁定全部 paper-run environment。
- **Original Problem / Why Previous Designs Were Reasonable:** diffusion/video generation 需要连续执行多次
  denoiser forward。固定 skip schedule、TeaCache 的 time-embedding residual 与 MagCache 的 residual
  magnitude 便宜、无需每次估计 Jacobian，在模型/采样器稳定、离线调参充分时仍合理；但 static schedule
  无法按 sample difficulty 调整，只看 latent 或 time 的单一 proxy 也可能漏掉另一方向的 output variation。
- **Principle / Mechanism:** 对相邻 trajectory state 做一阶展开，将输出变化上界近似为
  `S = ||J_x||·||Δx|| + ||J_t||·|Δt|`。runtime 从最近 refresh point 累积 latent displacement 与 time gap；
  `S<=ε` 且连续 reuse 未达 `n` 时复用完整 denoiser output，否则执行 forward、刷新 cache 与 anchor。
  `n` 是对局部线性近似漂移的硬保护；因此系统同时拥有 tolerance policy 与 max-staleness policy。
- **Sensitivity / State Ownership Contract:** exact Jacobian 太贵，论文在每个模型上用 8 个 calibration videos
  沿 solver direction 做 finite-difference secant estimation，并把 timestep-dependent `α_x/α_t` profile 离线
  缓存。所谓 per-sample adaptation 主要来自实际 `Δx` 累积，而 sensitivity coefficient 仍是 model-level
  calibration artifact。可靠 identity 必须绑定 model、sampler/timestep schedule、conditioning path、
  calibration data/profile、`ε(t)`、`n`、cached output 与 refresh state；换 sampler/model 后不能静默复用。
- **Evaluation Contract:** Wan2.1、CogVideoX、LTX-Video 均用 50 steps，主评测覆盖完整 VBench prompts；
  以 NFE/cache ratio 表示 compute，以相对 uncached output 的 LPIPS、PSNR、SSIM 表示 fidelity，并与
  TeaCache/MagCache 比较。ablation 使用 70 个 T2V-CompBench prompts；additional efficiency 只在 GH200、
  Wan2.1 上报告 182.3s→107.3s。未披露该 latency 的 batch、concurrency、precision、offload 与 SLO，且
  pixel/perceptual closeness 不等于 text-video semantic quality 或 human preference。
- **What the Evidence Proves / Does Not Prove:** `n` 与 `ε` ablation 支持明确的 quality/compute frontier，8
  与 4096 calibration samples 的 profile 对比支持该 setup 下小 calibration set 足够；三模型结果也说明
  sensitivity pattern 不可跨模型假设一致。但 conservative Wan setting 与 MagCache 几乎持平，aggressive
  settings 才拉开部分差异；不能外推到 audio/motion、其他 samplers 或 production serving，也不能把 NFE
  reduction 直接等同端到端 latency/goodput。
- **Heuristic and Global-Optimization Boundary:** 论文仍把前 20% denoising steps 固定为 `ε=0.01`，其余
  threshold 又按模型/slow-fast regime 设为 Wan 0.1/0.2、CogVideoX 0.6、LTX 0.5，因此“无需 heuristic
  tuning”不能按字面外推。作者 appendix 也承认 local sensitivity 只是一次追加 skip 的 marginal proxy；
  多次局部小误差可累积，global scheduler 才能跨 timesteps 分配 error budget，未来可用动态 `ε(t)` 连接两者。
- **Trade-offs / New Failure Modes / Old Branches:** training-free reuse 避免改模型，却引入 calibration
  artifact、threshold search、first-order truncation error、stale output accumulation 与 model/sampler drift。
  小 `n` 稳定但少 reuse，大 `n` 提速却增 drift；局部 policy 易错过全局 budget allocation。固定 schedule
  在 workload 稳定、校准/控制面越简单越重要时仍合理；distillation/few-step model 在可承担训练且追求更大
  step reduction 时是并存分支，不是被 caching 否定。
- **Evolution Relationship:** `Direct Evolution` from static/one-proxy full-forward caching → joint latent/time
  sensitivity + sample-specific displacement → future global error-budget scheduling。与 LLM KV Cache 仅为
  `Explanatory Analogy`：前者近似复用 denoiser output 并允许受控质量误差，后者保存 exact autoregressive
  state；不能把两者写成同一种 cache correctness。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 已读 Ch38、Ch40、Ch42、Ch52。Ch40 明确拥有
  autoregressive token Decode，Ch42/52 分别拥有 multi-request batching 与 serving scheduling；把 diffusion
  denoiser-output reuse 塞进这些章节会混淆生成语义和 correctness contract。Ch38 当前也以 LLM request
  lifecycle 为边界。机制具有长期价值，但现有 80 章没有不突兀的 owner；按计划只登记 structural gap，
  不为产生 Books diff 扭曲章节。
- **Integration Decision:** `Full Review Complete — Weekly Only / Structural Gap / No Coherent Owner`，
  `Status: Experimental`。未来若 ROADMAP 增加 multimodal/generative inference 的统一分支，可沉淀
  `Sensitivity-Bounded Approximation Cache and Error-Budget Contract`；本轮不修改 Books/ROADMAP。
- **Open Questions:** sensitivity profile 对 sampler、guidance、resolution、precision 与 model revision 的
  transfer 如何验证？局部 threshold 怎样和全局 error budget、human/VBench semantic quality 及 latency SLO
  联合优化？calibration drift 如何监控并触发 invalidation？代码 README 参数与论文 threshold 的尺度映射
  是否有稳定、可复核定义？

### CL4SE

- **Candidate / Week / Score:** CL4SE: Benchmarking Context Learning on Software Engineering / 2026-W09 /
  21/30；`Source Family ID: task-conditioned-software-engineering-context-benchmark`。
- **Source Type / Date / Revision:** arXiv:2602.23047 v1 首次公开 2026-02-26；v2 2026-03-31，当前 v3
  2026-04-06。v1 与 v3 的 title、authors 和组织均有变化；本轮阅读全文、四类 dataset construction、
  retrieval controls、全部 task tables/discussion，并核验作者 GitHub 与 Hugging Face dataset。current revision
  用于机制/边界核验，不把 3～4 月修改倒填为 W09 新事件。
- **Original Problem / Why Previous Designs Were Reasonable:** zero-shot 或统一 few-shot template 成本低、
  易比较，在模型已有足够 parametric knowledge、task 简单或没有项目私有 context 时仍合理。但 software
  engineering 任务需要不同信息：project style、可解释 solution path、review conversation、correct/overfit
  contrasts。把 context 只当 prompt 文案，会忽略来源、任务结构与选择策略。
- **Benchmark Mechanism:** 论文把四类 context 一对一映射到四个任务：interpretable examples→code
  generation，project-specific examples→summarization，procedural review history→code review，positive+
  negative examples→patch correctness。数据含 636 generation problems、8,225 summary pairs、1,916 PR
  review items、2,274 Defects4J patches；retrieval 使用 Chroma/Qwen3-Embedding-4B，排除 target 本身和晚于
  target timestamp 的样本。它测量的是多套 task-context pipeline，不是一个 context operator 的统一 ablation。
- **State Ownership / Control and Data Flow:** source repo/problem/PR/patch 拥有 target identity；retriever
  拥有 candidate pool、embedding、time filter 与 top-k；assembler 拥有 example type/order/count；model run
  拥有 model/API/prompt/token budget；task-specific evaluator 拥有 tests 或 lexical/classification metrics。
  若进入生产，context artifact 还必须绑定 commit、authorization、freshness 和 leakage audit，而非只记录
  “5-shot”。
- **Evaluation Contract:** 五个 models 中四个经官方 API、concurrency 32，GPT-Oss-120B 在 4×RTX 5880、
  bfloat16 本地部署，temperature 0。code generation 用 Pass@1；summarization 用 BLEU/ROUGE/METEOR/
  BERTScore；review/patch 用 accuracy/precision/recall/F1。硬件只适用于本地 model，论文没有把 API model
  revision、prompt token length、pricing/latency 与 repeated-run variance 形成统一 immutable run contract。
- **What the Evidence Proves / Does Not Prove:** 在这些固定 pairing 中，部分 targeted context 相对 zero-shot
  改善作者指标；summarization 1-shot 后继续加样本反而单调退化，且 lexical gain 远大于 BERTScore，说明
  style copying 与 semantic improvement 不可混为一谈。Qwen3-Max code generation 的 interpreted 1-shot 仅
  小幅改善且 plain example 下降；negative-only patch context 也可伤害某些模型。由于四类 context 没有在
  同一 task/dataset 上完整交叉，论文不能因果证明 taxonomy 与 task 的“一一最优匹配”，24.7% 又跨不同
  metric/normalization 聚合，不是可迁移的系统收益。
- **Data / Artifact Boundary:** generation tests 部分由 Qwen3-Coder-Plus 生成后人工修正，difficulty/test split
  又以 Qwen3-32B repeated pass rate 排序；这引入 model-conditioned selection。PR label 与 conversation
  还会受 repository policy、merge/reject reasons 和 project imbalance 影响。公开 repo 仅 4 commits；HF
  artifact 有四个 heterogeneous splits，但统一 viewer 当前因 schema cast error 失败。artifact 存在不等于
  paper run 已由 immutable manifest 完整锁定。
- **Trade-offs / New Failure Modes / Old Branches:** task-aware context 能提供 local convention、decision
  history 与 counterexamples，却增加 token/Prefill cost、retrieval leakage、stale project state、style
  overfitting、context poisoning 和 metric gaming。zero-shot 在 context 不可信、成本敏感或 base model 已有
  足够能力时仍合理；少量高相关 context 可能优于更多 context；executable repository state 也不能被自然
  语言 demonstrations 替代。
- **Evolution Relationship:** `Principle Reuse` from generic ICL → typed context assembly → task-specific
  selection/evaluation。论文没有证明四类 context 构成单向成熟度阶梯，也没有证明 context 越多越好。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 已读 Ch62、Ch71、Ch77。Ch71 已把 Context
  定义为有 provenance、authorization、ranking、placement、budget 与 evaluation 的 working set，并明确
  selection recall/precision、model use、cost 与 privacy；Ch62 已要求 task-specific scorer 和 dataset identity；
  Ch77 已覆盖 executable workflow context。CL4SE 的可靠结论未形成新的长期机制缺口。
- **Integration Decision:** `Full Review Complete — No Change / Already Covered / Weekly Only Benchmark
  Evidence`。不修改 Books，不把 taxonomy、24.7% aggregate 或 vendor model ranking 写成通用 context
  engineering 规律。
- **Open Questions:** 四类 context 在同一 task 上的 full-factorial、等 token-budget 与 random/irrelevant
  controls 会否支持相同结论？PR outcome 是否真正等同 review correctness？model-conditioned split 与 generated
  tests 是否偏向某些 model families？怎样把 current commit、dependency graph 与 executable tests 加入
  context identity，而不只检索历史文本？

### Online World Modeling Enables Real-World IRLfO / MPAIL2

- **Candidate / Week / Score:** Online World Modeling Enables Real-World Inverse Reinforcement Learning
  from Observation / 2026-W09 / 24/30；`Source Family ID: observation-only-online-world-model-irl`。
- **Source Type / Date / Revision:** arXiv:2602.24121 v1 首次公开 2026-02-27；当前 v2 为 2026-06-18。
  本轮阅读全文、全部 objectives/algorithms、architecture、real/sim experiments、baselines、ablations、
  checkpoint tables、hardware/task setup 与 Limitations，并核验作者 interactive project page。项目页声称
  提供 code/videos，但本轮未定位到可独立审查、锁定 paper run 的 public repository/commit。
- **Original Problem / Why Previous Designs Were Reasonable:** Behavior Cloning 直接从 action-labeled expert
  demonstrations 学 policy，训练稳定、离线且不承担真实环境探索风险；reward-specified RL 能明确优化目标；
  simulation 则可安全扩大 interaction。它们分别依赖 teleoperation/action labels、reward engineering 或
  sim-to-real pipeline。只有 observation/video demonstration 时，learner 不知道 expert action、reward、真实
  dynamics 或 terminal state，传统 IRLfO 又因 sample inefficiency 与 brittle policy 难以直接上机器人。
- **Changed Constraint / Mechanism:** MPAIL2 同时在线学习 encoder、latent dynamics、adversarial transition
  reward、Q-ensemble value 与 multi-step policy。world model 用 replay 中真实 `(o,a,o')` 自监督学习 latent
  prediction；reward discriminator 比较 demonstration transition 与 learner transition；value/policy 通过
  off-policy imagined returns 更新。MPPI planner 以 policy proposal warm-start，滚动预测 `H=7` 的 latent
  trajectories，用 learned reward + terminal Q 评分并只执行 receding-horizon action。
- **State Ownership / Control and Data Flow:** demonstration buffer 只拥有 observation transitions；online
  replay buffer 拥有 learner action transitions；encoder/dynamics 拥有当前 predictive representation；reward
  model 拥有 inferred task preference；Q/policy 拥有 return/proposal；planner 拥有 transient candidate plans，
  physical runtime 拥有 action clipping、reset 与 safety boundary。所有组件共同漂移，一次 checkpoint 必须
  原子绑定它们及 replay cursor、target networks、planner hyperparameters 和 robot/calibration identity。
- **Why the Integration Matters:** world model 不只加速 policy learning。它同时把 reward discrimination
  限制在 learner interaction 支持的 representation 上，并允许 planner 在执行前比较可能后果；Q 又补足
  finite horizon 之外的 return。policy 主要负责 proposal/warm start，而不是独占决策。因此演进是
  `demonstration imitation → online task inference → predictive state model → model-predictive correction`，
  不是“有 world model 就不需要 policy/reward/value”。
- **Evaluation Contract:** simulation 使用 IsaacLab/Franka、5 seeds；real tasks 使用 Franka 或 Kinova Gen3、
  双 `64×64` RGB + proprioception、3 seeds/task，10～15 demonstrations（1,025～1,802 transitions），并
  汇总 96+ on-robot scratch runs。real results 每 task 50 trials，报告 best 与 final checkpoint；MPAIL2 与
  strengthened IRL ablations、RLPD 和 diffusion BC 在 matched interaction/demonstration budgets 下比较。
  7.1M-parameter system 的 real Push action rate 约 10.28 Hz；论文未披露训练 compute/GPU 与 end-to-end
  safety SLO，`<40 min` 只绑定其 robot/task/control loop。
- **Evidence / Ablation Boundary:** removing planner、world-model components 或 off-policy training 在作者
  matrix 中明显降低 sample efficiency/stability，支持这些组件的 joint contribution；video-only external
  camera 与 positive transfer 也提供受限 real-world evidence。但 baselines 为吸收 MPAIL2 部件后的 strengthened
  implementations，不等同原论文 recipe；某些弱 baseline 因 simulation 表现差未进入 real experiment。
  best checkpoint 又从每 10 episodes 保存的多个 checkpoints 中、在大致开始成功后筛选，会引入 selection
  optimism，故应同时看 final checkpoint。3 seeds 与较大的 task-to-task variance 不能支持普遍机器人结论。
- **What It Does Not Prove:** observation-only 不等于零监督：demonstration selection、robot reset、workspace
  bounds、success evaluation、camera/calibration 和 operator safety 都是外部 contract。learned reward 只依据
  transition resemblance，可能将视觉 shortcut 当目标，也无法从有限 demonstrations 唯一识别 intention。
  论文没有验证跨 embodiment、long-horizon partial observability、安全关键 exploration 或通用 pretrained
  world model；也不证明 learned reward 普遍优于 hand-designed reward。
- **Trade-offs / New Failure Modes / Old Branches:** 少 action/reward engineering 换来 online robot
  interactions、planner compute、多模型 joint non-stationarity 与 reward ambiguity；新增 compounding model
  error、planner exploitation、representation collapse、replay staleness、unsafe exploration、actuation delay 与
  checkpoint-selection risk。BC 在 demonstration coverage 足、禁止探索和 offline reproducibility 优先时仍
  合理；hand-designed reward 在目标可精确定义、安全约束强时更可审计；simulation 在可建立可信 dynamics
  时仍能承担危险探索。
- **Evolution Relationship:** `Direct Evolution` from MPAIL-style planning robustness plus simulated
  interaction → MPAIL2 online/off-policy latent modeling and planning directly on robot；与 Ch10 的一般 world
  model 叙述为 `Mechanism Elaboration`，与 Ch29 LLM GRPO、Ch74 Tool Calling 仅是边界关系，不能混为同一 RL
  或 Agent runtime。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch10 为主 owner candidate；已读 Ch10、Ch29、
  Ch62、Ch74/75。Ch10 已说明 latent dynamics→imagined trajectories→policy 与 real-world feedback，但尚未
  展开“只有 observations 时 task objective 也必须被在线推断”，以及 reward/world model/value/planner 的
  ownership 与 joint-drift trade-off。Ch29 专属 LLM group-relative policy optimization，不承接 robotics IRL；
  Ch62 只负责 real-world evaluation contract。
- **Integration Decision:** `Full Review Complete — Books Candidate / Observation-only Task-Inference and
  Online World-Model Planning Contract`，`Status: Experimental`。Books Gate 关闭，本周不修改正文；后续只
  refine Ch10 的世界模型演进与失败模式，不搬运 robot success headline。
- **Open Questions:** reward ambiguity 如何用 language、negative evidence 或 human correction 消解而不重新
  引入高监督成本？world/reward/value joint drift 怎样 checkpoint、rollback 和 shadow-evaluate？hardware delay
  与 hidden temporal state 如何进入 recurrent/probabilistic observer？planner 在错误 model 上 exploitation 时，
  哪些 uncertainty/safety constraints 能阻止真实设备危险 action？

### QEDBENCH

- **Candidate / Week / Score:** QEDBENCH / 2026-W09 / 24/30；`Source Family ID: proof-judge-alignment-gap`。
- **Source Type / Date / Revision / Access:** primary research + benchmark artifact。arXiv:2602.20629 v1
  首次公开 2026-02-24；v2 2026-03-02，当前 v3 2026-07-06；HF 03-04 是 discovery lag，
  不改变事件周。本轮阅读全文 v1 的 Metadata、Introduction、Related Work、Methods、Results、Discussion
  与含 rubric、judge prompts、bias/reliability、contamination、case studies 的 Appendices；再读 v3 新增的
  protocol/robustness/limitations，并检查作者 GitHub 的公开 split、logs schema 与复算脚本。
- **Original Problem / Why Previous Design Was Reasonable:** open-ended mathematical proof 没有唯一字符串答案，
  exact match 无法区分合法替代证明、局部缺口与完全错误；逐题 domain expert grading 更可信，却需要昂贵
  专家时间。因而用明确 rubric 加 model judge 扩展评测是合理演进，但前提不是“judge 更强”，而是 judge
  对目标专家判断的 measurement error 已在相同任务分布上被校准。
- **Changed Constraint:** 当 proof 从短答案扩展到 upper-undergraduate / early-graduate 的长逻辑链时，
  表面上成立的局部陈述可以组合成全局错误；同一 judge 还可能在离散结构题上 lenient、在连续分析题上
  harsh。总体均值相近因此不能证明逐例 verdict 或 domain slice 可靠，增加 prompt/rubric 细节也未必能
  修复 judge 不具备的验证能力。
- **Mechanism / State Ownership / Control Flow:** QEDBench 收集 272 道、10 个数学领域的证明题，五个
  solver 各生成一份 LaTeX proof；48 名匹配研究领域的专家使用离散六档
  `[0, 0.25, 0.5, 0.75, 0.9, 1]` rubric 给出 score、理由和错误位置。每题同时有允许 expert common
  knowledge 的 Expert Rubric 与限制超纲工具的 Course-Specific Rubric；七个 judge 在两套 rubric 下形成
  fully crossed `7 judges × 5 solvers` 评价矩阵。人类专家拥有 reference verdict，rubric 拥有允许的证明
  边界，judge run 拥有 model/prompt/rubric/temperature identity；最终分析分别计算 mean/pass threshold、
  score delta、false-positive leniency、false-negative harshness 与 domain-conditioned correlation，而不是把
  单一 judge 平均分当 truth。
- **Implementation Details / Revision Boundary:** v1 已公开题目重写、o3-deep-research web audit、48 名
  专家与 1,000+ 小时标注、双 rubric、两阶段 judge prompt、污染比较和大量逐例分析；但 v1 主文没有披露
  temperature、two-expert/third-adjudicator protocol、same-family regression、binary-prompt robustness 或
  LaTeX-density 分析。v3 才明确自动评价 `T=0`，称每题“whenever possible”由两位专家独立评分并由第三人
  裁决，并加入 self-preference mixed-effects regression、binary grading、critique/score separation、format
  bias 与 formal-verification 边界。因此这些补充只能作为后续 revision 对机制和局限的核验，不能倒写成
  02-24 的完整公开 contract。
- **Evaluation Contract:** 五个 event-period solver 使用最长 16,384 output tokens、2,000 秒 streaming
  timeout、最多三次 retry；失败默认记零。主分析以 human score 均值和 `score >= 0.9` pass rate 为能力
  指标，并用七个 judge 对同一 proof/rubric 评分。污染分析只覆盖 214/272 道高置信分类题：88 道找到
  online solution、126 道未找到，58 道 ambiguous（含全部 19 道 Graph Theory）被排除；跨五个 solver
  得到 1,070 个 model-problem pairs。论文对该 split 报告 Welch test、Mann–Whitney test 与 Cohen's d；
  judge calibration 还报告 Pearson correlation、MAE、pass-rate bias 和 false-positive/false-negative rate。
  公开材料未给出 solver API temperature、完整 provider revision、费用/延迟、每个题目的专家覆盖比例、
  adjudication rate、inter-rater reliability 或 judge uncertainty interval，硬件也不适用于 API 模型评价。
- **What the Evidence Proves:** 在这组题、solver snapshots、rubric 和 human labels 中，judge 的误差方向
  具有明显 domain dependence；相同总体 pass rate 可以同时隐藏 leniency 与 harshness。v1 的 controlled
  rubric comparison 还显示其最佳 judge 的 Expert/Course-Specific 相关性约为 `0.69/0.67`、MAE 约为
  `0.13/0.14`，说明增加 pedagogical instruction 没有显著改变该配置下的对齐结构。逐例 case studies
  进一步证明部分 judge 会识别局部错误却仍给过高分，或奖励格式完整但逻辑链断裂的 proof。
- **What It Does Not Prove:** 它不证明某个 vendor 模型普遍是最佳 solver/judge，也不证明相关性差异来自
  某个内部“reasoning architecture”；`T=0` 只降低采样变化，不保证 provider backend 可重放。未检出
  online-solution score uplift 也不能证明没有 pretraining contamination：web-search detector 有覆盖盲区，
  58 道 ambiguous 被排除，且 model-problem pairs 在同一题内相关。双 rubric 的小差异也不能推出所有
  prompt engineering 无效，更不能直接证明 process supervision 或 fine-tuning 必然修复 judge。
- **Limitations / Artifact Boundary:** static expert ground truth 可能漏掉非标准但正确的 proof，范围只覆盖
  英文和十个数学领域；rubric 初稿由 GPT-5.2 Pro 合成、Gemini 验证后再由专家迭代，存在 measurement
  construction/self-preference 风险。v3 的多专家 protocol 比 v1 更强，但未报告实际双评覆盖率和一致性。
  GitHub 公开 README 本身同时写 `dev/test = 48/224` 与目录树 `49/226`，论文则说 272 problems、
  1,300+ proofs；test solutions 又被 withheld，公开复算脚本只承诺 pass-rate 与 leniency 分析。因此仓库
  是有价值的局部 artifact，不足以独立复现论文全部 figures、human adjudication 与 revision history。
- **Trade-offs / New Failure Modes / Where Previous Design Still Applies:** domain-calibrated human gold、双向
  error decomposition 与多 rubric 审计提高 judge 可解释性，却增加专家成本、rubric ownership、版本治理、
  disagreement adjudication 和 slice sample-size 压力。Exact/executable verifier 在可形式化结论上仍更强；
  单专家 rubric 在低风险、窄领域或探索阶段仍可接受；formal proof checker 在 theorem 与 translation 已可靠
  形式化时提供更强 correctness guarantee，但 autoformalization 又会引入“证明了另一个命题”的边界错配。
- **Evolution Relationship:** 与 Aletheia / FirstProof 为 `Layering / Dependency`：后者评估高难 proof artifact
  和自治边界，QEDBench 审计自然语言 proof 的 measurement layer。稳定演进是
  `exact/final answer -> human rubric -> scalable model judge -> human-gold calibration by domain and error
  direction -> executable/formal verifier where semantics can be preserved`；各层共存，不是后一层覆盖前一层。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch62 为主 owner；已读 Ch62 全章及 Ch27、
  Ch75/77 的相关 rubric/verifier 边界。Ch62 已有 judge versioning、human/verifier calibration、disagreement、
  trajectory success/failure recall 和 slice principles，但尚未把“总体 strictness 相近不等于逐例可靠”展开为
  domain-conditioned leniency/harshness contract，也没有说明 judge 能生成正确 critique 与最终 score calibration
  是两个不同能力。Ch27 负责 reward signal 的偏差，Ch77 负责 proof/evidence-producing workflow，不重复
  承接 evaluator calibration。
- **Integration Decision:** `Full Review Complete — Books Candidate / Domain-Conditioned Judge Calibration
  and Critique–Verdict Separation Contract`，`Status: Experimental`。Evidence Gate 尚未关闭，本轮不修改
  Books；后续只 refine Ch62 的通用 measurement contract，不复制模型排名或 proof benchmark 数字。
- **Open Questions:** 实际 two-expert coverage、disagreement/adjudication rate 与 inter-rater reliability 是多少？
  如何把 leniency/harshness 置信区间、domain drift 和 rubric revision 纳入 release gate？judge 已识别错误却仍
  给高分时，应校准 decision head、score mapping 还是 verifier composition？公开 artifact 的 split 数量差异和
  withheld test evidence 如何由 immutable manifest 解释并复算？

### Humans and LLMs Diverge on Probabilistic Inferences

- **Candidate / Week / Score:** Humans and LLMs Diverge on Probabilistic Inferences / 2026-W09 / 20/30；
  `Source Family ID: probabilistic-inference-distribution-evaluation`。
- **Source Type / Date / Access / Full-read Coverage:** primary research + public data/code。arXiv:2602.23546
  只有 v1，首次公开 2026-02-26；HF 03-04 为延迟发现。本轮阅读全文的 data construction、human study、
  metrics、八模型实验、temperature/reasoning/persona ablations、reasoning-chain analysis、Limitations 与全部
  appendices，并检查作者 GitHub 的 dataset、raw/processed results、batch inference workflow、analysis
  notebooks 与 canary policy。仓库当前只有 3 commits，未发布 immutable release/tag。
- **Original Problem / Why Previous Design Was Reasonable:** 传统 NLI/COPA 把答案压成 entailment、
  contradiction、neutral 或二选一，适合可判定任务，却丢失“在有限信息下有多大可能”的 graded judgment。
  单一 mean/majority label 也会把人群 disagreement 当 annotation noise。对于本来没有 deterministic gold 的
  commonsense effect inference，比较完整 response distribution 比只比一次答案更符合 measurement target。
- **Changed Constraint:** 当评估目标从“是否答对”变为“能否表达 epistemic uncertainty 或特定人群判断”时，
  ground truth 不再是标量标签；同一模型多次 sampling 的 variation、模型 verbalized confidence 与不同人群的
  belief variation 是三个不同随机变量。提高 temperature 可以扩大输出随机性，却不自动得到正确人群分布，
  reasoning budget 增加也不等价于 calibration 改善。
- **Mechanism / State Ownership / Data Flow:** 作者从 COPA test set 随机抽取 105 个 effect questions，将
  每个二选一 alternative 拆成两个 premise–hypothesis pairs，形成 210 项 ProbCOPA。328 名来自英国、美国、
  加拿大的 native-English Prolific participants 在 0～100 slider 上评分；每人先完成五个带反馈 calibration
  examples，再答最多 30 项与五个 attention checks，失败超过一次者全部丢弃，最终每题保留 25～30 个独立
  人类评分（median 28）。八个 reasoning-model snapshots 对每题在 provider default temperature 下采样 30 次，
  输出 verbalized 0～100 likelihood。dataset version 拥有 item identity；participant cohort/scale/prompt 拥有
  human target distribution；model/provider/temperature/reasoning budget/prompt 拥有 model distribution；分析层
  用 item median、differential entropy 与 1-Wasserstein distance 分离 location、spread 与 distribution gap。
- **Human Baseline / Reproducibility:** 30 个随机 items 由 30 名新 participants 重新标注，另有一轮 30 名新
  participants 使用更接近 model prompt 的措辞。两轮 item-mean 与原标注的 Spearman correlation 分别为
  `0.98`、`0.97`，two-sample KS tests 在 `alpha=0.05` 下未发现显著 distribution difference。这个结果只
  支持该 30-item subset、同类英语人群和相同 calibration UI 下的重测稳定性；它不是全部 210 项的跨文化、
  跨时间 population invariance proof。
- **Evaluation / Inference Contract:** 主实验使用八个具体 2025/early-2026 model/API snapshots；每项 30
  samples，GPT-5/Qwen/Kimi/GLM/DeepSeek reasoning effort 为 medium，Gemini/Claude thinking budget 为
  1024，main max-new-tokens 为 2048。temperature 使用各 provider default，因而跨模型 sampling entropy
  并非受控同量纲比较。30-item ablation 才改变 temperature、low/high reasoning（Gemini/Claude 512/4096）
  与 personas，并把 max tokens 提到 4224；reasoning-effort median comparison 使用 bootstrap 95% CI。
  公开仓库保留 prompts、provider scripts、results 与 plotting notebooks，但 provider backend、default
  temperature 和 hosted model behavior 仍会漂移。
- **What the Evidence Proves:** 在该英语 effect-likelihood task 与 experiment contract 中，fresh human cohort
  能近似复现原 human distribution，而八个 model 的 verbalized likelihood samples 在 middle-likelihood items
  上与 human distribution 差距更大、variation 通常更小。提高 temperature 在 30-item subset 上能增加
  variation，有时降低 Wasserstein distance，却同时提高无可用答案/随机 token 序列；提高 reasoning effort
  未让任一 item median 出现作者 bootstrap criterion 下的显著变化。八模型 ensemble 更接近 human baseline
  但仍未达到它，支持“diversity source 与 target distribution 必须分别验证”。
- **What It Does Not Prove:** human-like distribution 不等于事实正确、well-calibrated probability 或适合生产
  决策；这里没有真实 event frequency 可计算 Brier score/expected calibration error。verbalized number 不是
  token probability 或内部 belief，30 个 API samples 也不是 30 个独立模型/人。论文把 extreme responses
  解释为 overconfidence 具有合理关联，但没有 outcome gold，不能证明这些数值在频率意义上过度自信。
  reasoning-chain length 与 human entropy 的相关性也不证明共享认知机制；100 条人工检查中 90 条枚举
  alternatives 只说明可见文本模式，作者亦承认 CoT faithfulness 未建立。
- **Limitations / Threats:** 数据来自旧 COPA test sentences，可能已进入训练；只保留 effects、不覆盖 causes，
  只招募三个英语国家 native speakers。五个 calibration examples 与 range labels 会塑造 human distribution，
  raw scores 又刻意不做 participant normalization，因此“真实分歧”与个人 scale-use 差异没有完全分离。
  每题约 28 个样本估计 continuous entropy 较脆弱，正文未给 bandwidth/estimator sensitivity；Silverman test
  在每项小样本下不拒绝 unimodality也不能证明分布确实单峰。follow-up ablations 只用 30/210 items，且
  default temperature 跨 provider 不可比。部分 API 不暴露真实 CoT，输出 token 数只是 proxy。
- **Trade-offs / Previous Design Still Applies:** distributional evaluation 保存 disagreement 和 uncertainty，
  代价是更多 repetitions、population definition、elicitation/scale bias、density-estimation variance、provider
  sampling drift 与更复杂 release criteria。存在 deterministic outcome、法律/安全 hard constraint 或 executable
  verifier 时，单一正确性 gate 仍然合理；需要 individual decision 时，模仿群体分布甚至可能掩盖 minority
  risk。只有目标明确是代表某个 population belief 时，human-distribution alignment 才应成为 primary metric。
- **Evolution Relationship:** `binary/majority label -> scalar confidence -> repeated-sample distribution ->
  human-cohort baseline -> slice/population-conditioned distributional gate` 是 `Direct Evolution`；Ch20 的
  decoding stochasticity 是 measurement dependency，不是 epistemic calibration 本身。增加 temperature、persona
  或 model ensemble 属于不同 diversity interventions，必须按 target distribution 与 failure cost分别验证。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch62 为主 owner；已读 Ch62、Ch20 和 Ch5 相关
  部分。Ch62 已说明分布、scorer uncertainty、per-example evidence 与 human disagreement，但尚未区分
  `target population variation`、`single-model sampling variation` 与 `verbalized uncertainty`，也没有说明
  distribution matching 何时本身是目标。Ch20 已完整拥有 temperature 如何改变 token distribution；Ch5 只
  提供 representation/distribution-shift 边界，两章均不重复承接 evaluation specification。
- **Integration Decision:** `Full Review Complete — Books Candidate / Distributional Target, Elicitation and
  Sampling-Identity Contract`，`Status: Experimental`。Evidence Gate 尚未关闭，本轮不修改 Books；后续可
  refine Ch62，在 Ch20 只保留短 handoff，不写八模型排名。
- **Open Questions:** 怎样用 event outcomes 将 verbalized likelihood 与 population disagreement 分开校准？
  human cohort 的 geography、demographics、instruction 与 time drift 怎样进入 dataset identity？小样本 entropy /
  Wasserstein 的 uncertainty 和 estimator sensitivity 怎样进入 gate？当 individual fairness 或 high-risk tail 与
  population matching 冲突时，哪个是 hard constraint？

### Replicate-and-Quantize for MoE Load Balancing

- **Source-Family Identity / Date Correction:** 2026 arXiv:2602.19938 v1 于 2026-02-23 公开，但同一核心方法
  `Replicate and Quantize: A Plug-and-Play Strategy for Load Balancing in Sparse Mixture-of-Experts LLMs`
  已于 2024-09-22 在 OpenReview 公开、2025-02-05 修改。两版共享 LIS、per-layer heavy-hitter identification、
  Wanda-based low-importance expert、lower-bit replica、fixed-memory-budget quantization 与 streaming history/
  previous-window 两种 policy。2026 版扩充作者、模型与实验，不改变 source family 的 first-public date。
- **Access / Coverage:** 已核验 OpenReview primary record 与全文，并阅读 2026 扩展版 public CC BY 4.0
  full-text mirror 的 Introduction、Related Work、全部 Method/Algorithms、implementation、models/datasets、
  main results、streaming experiment、ablations 与 Conclusion。未定位到 public author code、immutable
  paper-run manifest 或独立 system implementation。
- **Mechanism / Evidence Boundary:** 方法按 calibration/trace 统计每层 token count，选择最常用 expert；以
  Wanda-style weight-activation score寻找低重要度 expert；复制并量化 heavy hitter，同时量化低重要度 expert，
  试图在原 memory budget 内增加 parallel capacity。Switch Transformer 从 FP32 降 FP16，LLaMA-MoE/
  DeepSeek-MoE 从 FP16 降 8-bit。LIS 评估设置甚至把 `max_new_tokens=1`、batch=1 与 accuracy generation
  的 batch=16 分开；论文报告的主要系统量是 routing-count imbalance，不是端到端 TTFT/TPOT、throughput、
  tail latency、collective traffic 或 GPU utilization。论文声称“不改 router”却没有公开 runtime 如何把发往同一
  expert ID 的 tokens 分摊到 original/replica、如何放置跨设备副本或保持 precision-mixed output semantics，
  因此 LIS 改善不能被解释为已验证的 distributed serving speedup。
- **Evolution / Trade-off Boundary:** inference-time replication 是 training-time auxiliary-loss/router balancing
  之外的合理分支；quantization 用释放的 bytes 购买复制容量，但新增 calibration drift、expert-importance drift、
  mixed-precision error、routing-table/replica identity、warm-up/eviction、failure recovery 与 topology-aware
  placement 问题。旧 router balancing 在训练分布稳定、模型可重训时仍成立；runtime sharding/replication 在
  有真实 placement/scheduler contract 时仍是另一层，不应被 LIS proxy 覆盖。
- **Disposition:** `Cross-Year Exclusion — First Public 2024-09-22 / Not a 2026-W09 Event`。本项不进入
  W09 Candidate Scoring、Recovered Census、Evidence Gate denominator 或 Books Integration Decision。
  2026 扩展版可在未来审计 2024 source family 或专题演进时作为 revision evidence，但不得伪装成 2026 新技术。
- **Open Questions:** replica token dispatch 到底由 router、dispatcher 还是 scheduler 拥有？同一 expert 的
  FP16/INT8 outputs 如何在数值上保持等价？在真实 multi-GPU EP topology、decode microbatch、matched memory
  和 tail-SLO contract 下，LIS 与实际 latency/throughput 的相关性是否成立？

### MINAR

- **Source-Family Identity / Date Correction:** arXiv:2602.21442 v1 于 2026-02-24 公开，但 official OpenReview
  record 显示同题、同作者、同两项 GNN case studies 的 MINAR 已于 2025-09-23 公开，2025-10-27 修改，作为
  NeurIPS 2025 NPGML Poster。2026 arXiv 是后续归档/扩展，不构成 W09 first-public event。
- **Access / Mechanism Boundary:** 已核验 OpenReview primary record/full paper、2026 full-text mirror 与 PNNL
  repository identity。方法把 EAP/EAP-IG 类 attribution patching 适配到 GNN hidden-state edges，分析单任务
  Bellman-Ford 与 shortest-path/reachability multi-task reuse。两个受控 case studies 可以作为 attribution-based
  circuit discovery 的机制证据，但不证明 attribution score 等于 causal necessity、跨 seed/architecture/task
  circuit 稳定，或 GNN 结论可直接外推到 Transformer/LLM production safety。
- **Disposition:** `Cross-Year Exclusion — First Public 2025-09-23 / Not a 2026-W09 Event`。本项从 W09
  Candidate Scoring、Recovered Census、Evidence Gate denominator 与 Books Decision 移除；应在后续
  2025-W39 修复中按完整 source-family 与 Ch5/62 边界审计，而不是在 2026 重复计分。
- **Open Questions:** graph node/edge hidden-state intervention unit、patching baseline 与 corruption distribution
  如何改变归因？被剪除或复用的 circuit 是否通过 necessity/sufficiency、跨 seed 与 OOD graph-size 验证？

### IMMACULATE

- **Candidate / Week / Score:** IMMACULATE: A Practical LLM Auditing Framework via Verifiable Computation /
  2026-W09 / 28/30；`Source Family ID: black-box-llm-service-verifiable-audit`。
- **Source Type / Date / Access / Full-read Coverage:** arXiv:2602.22700 v1 首次公开 2026-02-26；DBLP、
  public CC BY 4.0 full-text mirror 与作者 repository identity 一致。已读 Introduction/Related Work、Threat
  Model、hybrid computation/LDD 定义、Propositions 与 Appendix proofs、randomized-audit protocol、Top-K
  optimization、adaptive-adversary analysis、全部 experiments/parameter study/overhead、Conclusion 和
  Appendices A～G；并检查 redirected repository 的 1-commit、无 release/tag 三套 source trees。
- **Original Problem / Why Previous Designs Were Reasonable:** 黑盒 API user 看不到实际 model、precision、
  hidden reasoning-token count 或 internal states。直接 re-execution 在 proprietary weights 不可得时失效；GPU
  TEE 提供完整 runtime integrity 但绑定特定硬件并有系统成本；纯 ZK/VC 可减少硬件信任，却常要求 deterministic/
  integer execution、单次 prover 成本高；empirical fingerprint 便宜但缺少对 committed computation 的证明。
  这些分支在硬件、proprietorship 与 cost 约束不同的场景仍合理。
- **Threat Model / Changed Constraint:** trusted auditor 必须伪装为普通 user，server 在收到 response 后才知道
  audit identity；server 被假设为经济理性、至少在 `alpha=10%` requests 上作弊，且无法区分 audit requests。
  排除了“花更多 compute 提供另一模型”等攻击。因而保证不是针对 arbitrary Byzantine provider，也不覆盖
  可识别 auditor、低频 targeted cheating、colluding auditor、reference/model-owner compromise 或 denial of proof。
- **Mechanism / State Ownership / Flow:** provider 先对 claimed full-precision reference model 做 commitment；
  online execution 在 token selection/MoE routing 等 discrete decisions 记录并 commit runtime logits/Top-K indices；
  audited query 再以 reference continuous transforms 重放同一 discrete path，证明 output/token count 与 committed
  decisions 一致，并输出 runtime/reference logits 的 LDD。auditor 用 request 内 tail statistic `p(t1)` 与阈值
  `t2` 判定，再跨随机 audits 聚合 detection probability。身份必须同时包含 model/weights commitment、runtime
  precision/kernel/software、prompt/sampling、discrete trace、threshold-ceremony dataset/version、auditor policy
  与 proof backend；否则 LDD drift 与恶意 deviation 不可区分。
- **Formal and Evidence Boundary:** randomized gate 的一般关系是 audit count 随 `alpha × per-request detection`
  下降；论文示例在 zero-FP、1% conditional detection、`alpha=0.1` 时约需 3,000 audits 达到 95% 至少一次检测。
  实验用允许最多 3 个 flags 的另一月度 rule，单日抓到 4+ 的概率只报告 `>=0.3`，再依赖多日持续作弊降低
  evasion。model substitution/precision reduction 的 propositions 描述其 LDD bias/variance signature；adaptive
  proof 还假设 fixed compute budget 下 adversary 总选择最接近 reference 的最佳 approximation。它们不证明任意
  自适应 adversary 都会产生可分 LDD，也不证明 token overbilling 的现实 provider 必须实现论文构造的 dummy
  hybrid steps。
- **Evaluation Contract:** LLaMA3-70B、Qwen3-32B、Qwen3-30B-A3B、DeepSeek-V2-Lite；GSM8K、TriviaQA、
  WebQuestions 各 500 prompts，另每数据集 200 prompts 做 threshold setup；Top-20 sampling；2×NVIDIA RTX
  6000 Pro 96GB、TP=2；vLLM online execution，Hugging Face Transformers FP32 reference/VC in CPU TDX。
  攻击为 FP8 与选定 smaller-model substitution；token overreporting 未单独实验。quantization 的 per-request
  detection 最低 1.3%，substitution >40%。benign test 规模只有 thousands，未观察到 FP，因此 `<1e-5` FP 是
  EVT tail extrapolation，不是直接频数证据；`t1/t2` ceremony 又含要求 setup detection 约 5% 的 ad-hoc rule。
- **Cost / Implementation Boundary:** 所有请求承担 logits/Top-K commitment 与临时 storage；作者估计最大
  open models 约 1KB/token。单次 CPU-TEE VC 比 GPU inference 慢约 400～900×，`<1%` throughput overhead
  依赖 audit fraction `<1e-5` 的服务规模摊销。论文声称不需要 trusted hardware 过宽：其实实验实例使用 CPU
  TDX enclave；更准确的是“不要求 GPU TEE，VC 可由不同 backend 实例化”。公开 repository 只有一个 commit、
  无 immutable paper-run manifest，主体是 modified vLLM/Transformers trees；未公开完整 commitment、auditor、
  threshold ceremony、TDX attestation 与 end-to-end VC protocol，不能独立复现完整安全主张。
- **Trade-offs / New Failure Modes / Old Branches:** selective proof 把 every-request cryptographic cost 换成
  sampling risk、audit indistinguishability、threshold drift、commit-log privacy/storage、reference replay cost 与
  delayed detection；LDD 还受 model revision、kernel、hardware、precision、prompt mix 与 output length 影响。
  GPU TEE 在需要逐请求强 integrity 且硬件可用时仍成立；ZK 在不接受 TEE trust 且能承担 prover cost 时仍成立；
  empirical audit 在低风险/低成本场景仍有位置。三者不是单向替代史。
- **Evolution Relationship:** `Direct Evolution`：black-box output fingerprint → full-execution TEE/ZK proof →
  hybrid-state commitment + probabilistic selective proof；与 Ch64/65 evidence correlation、Ch66 amortized cost、
  Ch69 readiness gate 是 `Layering / Dependency`。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 已完整阅读 Ch67、Ch68、Ch69，并检查 Ch64、
  Ch66。主 owner 从错误的 Ch65 修正为 Ch68。Ch68 已覆盖 artifact provenance、trust boundary 与 audit，但尚未
  区分 **artifact integrity** 与 **每次远端 execution 是否遵守声明 model/precision/billing contract**，也未展开
  selective audit 的 commitment/sampling/operating-point failure modes。Ch64 只拥有 audit evidence schema，
  Ch65 只拥有 request correlation，Ch66 只拥有 proof/audit cost，Ch69 只拥有 rollout/readiness gate。
- **Integration Decision:** `Full Review Complete — Books Candidate / Probabilistic Service-Integrity Audit and
  Hybrid-State Commitment Contract`，`Status: Experimental`。Evidence Gate 尚未关闭，本轮不修改 Books；
  后续只 refine Ch68，并向 Ch64/66 增加最短 handoff，不写 `<1%` headline 为通用 production fact。
- **Open Questions:** 如何让 auditor identity 与 query distribution 真正不可区分？model/runtime/kernel upgrade 后
  LDD baseline 怎样原子切换？EVT tail 在 domain drift 与长输出下是否仍校准？怎样用公开 ZK 或可验证 TDX
  attestation 补齐 current artifact？在低于 10% 的 targeted cheating、auditor collusion 与 selective proof refusal
  下，detection SLO 和 escalation 应如何定义？

### LLMServingSim 2.0

- **Candidate / Week / Score:** LLMServingSim 2.0: A Unified Simulator for Heterogeneous and
  Disaggregated LLM Serving Infrastructure / 2026-W09 / 29/30；
  `Source Family ID: llm-serving-runtime-hardware-cosimulation`。
- **Source Type / Event Date / Revision / Access:** system-simulation paper；arXiv:2602.23036 v1 首次公开
  2026-02-26，随后获 ISPASS 2026 Best Paper。全文按 v1 镜像逐节阅读，并与作者 project、official docs、
  GitHub、ISPASS bibliographic record 及 2026-03-06 Zenodo frozen artifact 联读。它与 IISWC 2024
  LLMServingSim、CAL 2025 `arXiv:2511.07229` 属于 `Direct Evolution`；后发 conference status、artifact
  与 current v1.1.0 只用于核验，不倒填 event-date availability。
- **Full-read Coverage:** 已覆盖 metadata/revision、Abstract、Introduction、Background、Motivation、Method
  Sections IV～V、Execution Planner、MSG、memory/power/operator/system models、PD/prefix/MoE use cases、
  Methodology、全部 Evaluation/基线/case studies、Related Work、Conclusion 与 artifact appendix/workflow。
  论文没有独立 Limitations section；未披露项与可外推边界在本 Review 显式补列。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint:** 旧 hardware-centric
  simulator 精细刻画 accelerator/network，却假定静态、重复 graph；旧 serving-level simulator追踪 arrival、
  batching 或 configuration search，却常简化 memory hierarchy、contention 与 heterogeneous placement。这些
  拆分在 homogeneous GPU、single instance、稳定 graph 下合理。PD、multi-tier prefix cache、MoE EP/offload、
  异构 GPU/TPU/PIM/CXL 同时出现后，policy 会改变 data movement 与 contention，反过来又改变下一轮
  batching/routing；把两层离线拼接会丢掉 feedback loop。
- **Mechanism / State Ownership / Control and Data Flow:** 输入 contract 是 workload、cluster configuration 与
  per-operator hardware profiles。Execution Planner 初始化 Router、每模型一个 Model Serving Group（MSG）和
  System Simulator；MSG 拥有 request queue、batch scheduler、device pool、KV/memory/power model、operation
  mapper/scheduler。每轮由 Router 投递到达请求，MSG 依据 capacity/cache/policy 形成 batch 和 operation DAG，
  再把 compute、collective、KV/load/store、同步与 power annotations 交给扩展的 ASTRA-Sim/Chakra 执行；完成
  时间回写 request/queue/memory state并推进 simulated clock。PD 由 prefill/decode MSG 与 layer-wise KV-transfer
  edges 表达；prefix cache 在 device/CPU/CXL tiers 维护；MoE graph 显式加入 expert routing、load 与 All-to-All。
- **Implementation / Artifact:** 当前官方实现为 Python serving frontend + C++ analytical backend，二者以
  generated Chakra graph/file path 和文本 pipe 交互。Profiler 对单个 model-device pair 的一个 decode block
  采集 operator latency/power，再复用到 graph；官方文档还给出 request lifecycle、scheduler、memory、MoE、
  trace format 与 validation pages。Zenodo v1 冻结 90.8 MB artifact，含 Figures 5～10 的 scripts、reference
  outputs、`compare.sh` 和环境说明；但冻结时间晚于事件周，current GitHub 的 65 commits 也不能代表 v1 code。
- **Evaluation Contract:** real-system validation 使用 vLLM：4×RTX A6000 40 GB + Xeon Gold 6326、
  8×H100-SXM 80 GB，以及 TPU-v6e-1；模型含 Llama 3.1-8B/70B、Phi-mini MoE、Mixtral 8×7B，H100
  70B/Mixtral 用 TP4。默认 workload 从 ShareGPT 抽 300 requests，Poisson arrival 10 req/s；memory test
  另用 burst/idle 与 vLLM block 16、LMCache CPU block 256。比较 Vidur、APEX、TokenSim、旧版
  LLMServingSim，只在各 baseline 能执行的配置上比较。作者报告 time-series throughput error A6000 5.66%、
  H100 2.98%，aggregate throughput/latency error 0.85%/1.59%；power energy error 1.34%，single/multi-instance
  memory/prefix error 0.93%/0.41%。TPU 仅 single-instance dense，per-timestep 4.24%、aggregate <0.2%。
  PIM case 是仿真而非 real-PIM validation：256 requests、128/512 tokens、256×1 GB HBM2 channels，报告
  decode-period 1.43× throughput；SBI 只在 batch ≥256 时有利。
- **What Evidence Proves / Does Not Prove:** 证据支持作者实现能在上述硬件、模型、trace 与 policies 下重现
  多类 temporal/aggregate behavior，并能统一表达原 baseline 不支持的 PD/MoE/multi-tier-memory scenarios。
  它不证明 0.97% 是跨 metric、tail、硬件和 workload 的通用误差；aggregate mean 会掩盖 time-series、p99
  与 unsupported configurations。单-block profile portability 未覆盖 unseen kernel shape、compiler/runtime
  revision、contention phase 或 failure/retry；hypothetical TPU/PIM/PD 组合是 design exploration，不是部署证明。
- **Trade-offs / New Failure Modes / Previous Design Still Applies:** 统一事件循环获得 interaction fidelity、
  state visibility 与 design-space coverage，代价是 profile calibration、simulation runtime、配置/模型复杂度和
  更多 hidden assumptions。profile/model/policy 任一 identity 漂移都会产生“精确地模拟错误系统”；reference
  outputs 还可能把实现 bug 固化为 golden。静态 analytical model 仍适合 kernel/roofline pruning，真实 replay/
  canary 仍拥有最终 deployment authority；预测差距小于 simulator validation error 时应视为 near tie。
- **Evolution / ROADMAP / Adjacent Chapters Read / Existing Coverage:** `static operator/communication model ->
  request-driven serving simulator -> heterogeneous MSG + multi-tier state -> runtime policy/hardware feedback loop ->
  frozen artifact and real-system calibration` 是 `Direct Evolution`。主 owner 修正为 Ch62 的 Runtime/Service
  Evaluation contract；已读 Ch45、Ch48、Ch50～52、Ch59、Ch62。Ch51 已有 simulator 只用于 pruning、
  best-vs-best 与 near-tie real replay 的原则，Ch52 已有 workload contract；Ch62 尚未明确 simulator subject
  identity 必须同时绑定 workload、hardware profile、policy、runtime revision 与 validation envelope，存在可
  refine 的长期缺口。Ch45～52 只作被模拟对象的 handoff，不复制 feature list。
- **Integration Decision:** `Full Review Complete — Books Candidate / Runtime-Driven Simulation Identity and
  Validation-Envelope Contract`。Evidence Gate 仍打开，本轮不修改 Books；后续只 refine Ch62 的评估证据
  层级，并在 Ch51 保留一句“simulator prediction 不拥有 deployment authority”。
- **Open Questions:** profile 对 unseen shape、fused kernel、compiler/runtime revision 与 concurrent contention
  怎样校准？tail/p99 与 failure/retry 的 validation envelope 如何建立？event-date code 与 Zenodo/current
  release 的具体差异是什么？怎样对 simulator 做 mutation tests，避免 reference outputs 把 shared bug 当正确？

### AMA-Bench

- **Candidate / Week / Score:** AMA-Bench: Evaluating Long-Horizon Memory for Agentic Applications /
  2026-W09 / 27/30；`Source Family ID: agent-memory-environment-trajectory-evaluation`。
- **Source Type / Event Date / Revision / Access:** benchmark + memory-system paper；arXiv:2602.22769 v1
  首次公开 2026-02-26。已读取公开 CC BY 4.0 全文及 Appendix，并联读作者 project、repository、dataset
  与后发 OpenReview version。HF spillover 未收录该事件，由 DBLP cross-index 恢复；ICML 2026 接收状态和
  后发 revision 只用于核验，不倒填事件周。
- **Full-read Coverage:** 已覆盖 metadata、Abstract、Introduction、Related Work、POMDP/memory formalization、
  四类 capability、real/synthetic benchmark construction、Empirical Motivation、AMA-Agent Method、全部
  Evaluation、construction/retrieval ablations、Conclusion/Limitations，以及 dataset/domain statistics、baseline
  configs、judge calibration、prompts、needle synthesis 与 case-study Appendix。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint:** dialogue memory 主要处理
  自然语言、冗余与主观表达，summary/embedding similarity 因而是合理的压缩与检索策略。Agent trajectory
  却包含 HTML/JSON/SQL/code/ASCII 等 machine-generated artifacts；`action -> latent state transition ->
  observation` 形成时序与因果约束，信息密度也更高。相同压缩会删掉低层 state，纯相似度又可能找不到
  lexical overlap 很低但因果必要的 evidence。
- **Formalization / Capability Contract:** 作者把环境写成 POMDP `M=(S,A,O,P,r)`，history 为
  `h_t=(x,a_1,o_1,...,o_t)`；Memory System 分为 `Build: H -> M_mem` 与
  `Retrieve(m_t,q_t)=c_t`，policy 再据 `q_t,c_t` 行动。评测将三个机制拆成四类能力：retrieval 拥有
  temporal recall 与 causal inference，evolution 拥有 state updating，condensation 拥有 state abstraction。
  这比“能否找回一句话”更接近 agent state，却仍只测 QA evidence，不直接测 durable write authority。
- **Dataset Construction / State and Evidence Flow:** real subset 从 WebArena、SWE-bench/OpenHands、
  Spider2、ALFWorld/ALFRED、BALROG/lmgame、GAIA/CoSight 收集 208 trajectories、2,496 QA；每条选中
  trajectory 由 graduate-level annotator 编写 12 个 trajectory-grounded QA，并由第二人 cross-review。
  Appendix Table 8 的总数纠正了项目页曾显示的 207/2,481。synthetic subset 用 BabyAI/TextWorld 的可执行
  backend、difficulty vector `phi`、action noise `epsilon`、observation verbosity `gamma` 生成 1,200 QA，覆盖
  8K/16K/32K/64K/128K、每档 240；needle 是回答所需的最小 turn-id set，可由 backend state验证。
- **AMA-Agent Mechanism / Ownership:** construction 对相邻 `(o_(t-1),a_t,o_t)` 抽取 environment/object
  state 和 dependency，生成 directed causal edges、undirected associations 与可 embedding 的 global graph。
  retrieval 先取 top-5 similar nodes，再由 model 判断 sufficiency；不足时选择 bounded graph traversal，或生成
  code 执行 keyword/statistical search，最后合成 answer。Graph、node/edge provenance、tool execution 与
  sufficiency decision 都成为新状态；论文实现没有给出生产级 transaction、authorization、supersession、
  deletion 或 rollback semantics。
- **Evaluation Contract:** 15 类 long-context/RAG/memory-agent baselines；RAG、memory agents 与 AMA-Agent
  统一用 Qwen3-8B/32B backbone，但各 baseline 沿用作者默认 embedding/index settings，因此不是所有
  retrieval opportunity 与 construction cost 的完全 factorial control。长上下文超过各 model limit 时保留首尾
  各 50%、丢弃中段，并预留 4K output。主指标为 Qwen3-32B binary judge Accuracy 与 token-level F1；judge
  只在 GPT-5.2 outputs 的 300 samples 上由至少两人标注、第三人仲裁，报告 92.67% agreement accuracy，
  仍未覆盖所有 model/method、domain 与 machine-format slices。
- **Evidence / Ablations:** 在 Qwen3-32B contract 下，作者报告 AMA-Agent average accuracy 0.5722；
  HippoRAG2 0.4480、MemoRAG 0.4606。移除 graph 后 0.57->0.43，移除 tool retrieval 后 0.57->0.44；
  BabyAI needle decomposition 还显示 construction loss 与 retrieval loss 是不同 failure channels。结果支持
  “对该 benchmark，causal state representation 与非纯相似度检索都有增量贡献”，不证明因果图是所有
  Agent Memory 默认结构，也不证明 synthetic ranking 可无条件预测 production task success。
- **Limitations / Threats / What Is Not Proved:** 论文明确只覆盖 in-episode memory，不含 cross-task/lifelong。
  real traces 多由既定 agent/framework 或 expert demonstrations 产生，selection 偏向长 trajectory；offline QA
  未直接检查在线 action success、failure recovery、stale-state invalidation、conflicting writers 或 side effects。
  causal edges 本身由 LLM 从局部 turns 抽取，并非 environment backend 的 ground-truth causal graph；judge、
  graph builder 与 answerer 的 shared model-family bias、token/cost/latency、graph growth 和 tool sandbox 风险均
  未形成完整 production evaluation。
- **Trade-offs / Previous Design Still Applies:** causal graph保留 state dependency并支持 multi-hop traversal，
  代价是 extraction error、graph growth、edge/version ownership 与更新成本；tool search减少 similarity miss，
  代价是 extra calls/code execution、sufficiency false-positive 与 latency。对短、自然语言、低冲突的 history，
  raw context 或 simple hybrid retrieval 仍更简单；高风险 authoritative state仍应留在 transactional workflow，
  而不是把 graph 当 source of truth。
- **Evolution / ROADMAP / Adjacent Chapters Read / Existing Coverage:** `dialogue replay -> semantic retrieval /
  lossy summary -> typed action-observation trajectory -> causal/state representation -> similarity + graph/lexical tools
  -> online state validation and governed persistence` 是 `Direct Evolution`。Ch73 为主 owner；已读 Ch72～74、
  Ch62 与 Ch77。Ch73 已有 provenance、typed transition、consolidation、supersession/delete/rollback 与 derived
  memory 不是 authority 的原则，但尚未把 machine-generated trajectory 的 dense objective state、construction
  loss 与 retrieval loss、causal dependency preservation 写成同一演进链，存在真实 refine 缺口。Ch62 只承接
  benchmark/judge identity，Ch72 只承接 hybrid/tool retrieval，Ch77 保留 authoritative workflow boundary。
- **Integration Decision:** `Full Review Complete — Books Candidate / Causal Trajectory Memory and
  Construction-vs-Retrieval Loss Contract`，`Status: Experimental`。Evidence Gate 未关闭，本轮不修改 Books；
  后续 refine Ch73，不写模型排行榜和 11.16% headline。
- **Open Questions:** 如何用 environment transition 与 downstream task success 校准 offline QA？graph edge
  如何携带 source turn、extractor/version、confidence、supersession 与 delete propagation？失败/retry 和 tool
  nondeterminism 如何进入 trajectory identity？不同 memory methods 在等 token、latency、construction compute、
  retrieval calls 与 judge-independent verification 下，收益是否仍成立？

### Transformers Converge to Invariant Algorithmic Cores

- **Candidate / Week / Score:** Transformers Converge to Invariant Algorithmic Cores / 2026-W09 / 23/30；
  `Source Family ID: cross-run-algorithmic-core-interpretability`。
- **Source Type / Event Date / Revision:** interpretability / representation-analysis paper；arXiv v1 首次公开
  2026-02-26，v2 2026-07-06。事件按 v1 归 W09；v1 的 language experiment 仅含 GPT-2 Small/Medium/Large，
  v2 才扩为 GPT-2 三个规模、LLaMA-3.1 8B、Gemma-2 9B 与 Qwen2.5 32B，并补充更完整的 grokking
  seed/appendix 表。后发六模型证据只用于 revision 核验，不倒写成 02-26 已公开事实。
- **Direct / Related Primary Sources:** 完整阅读 arXiv v1、current v2 的 method、three experiment families、
  causal intervention、operator fitting、grokking sweep、limitations 与相关 appendix；检查作者 repository
  README 及 `markov.py`、`modadd.py`、`grok_sweep.py`、`sva.py`。仓库当前只有少量 commits、没有 release/
  immutable paper-run tag，因此 code availability 不等于实验 artifact 已完整冻结。
- **Original Problem / Why Previous Design Was Reasonable / Changed Constraint:** 单神经元、固定坐标或
  probe coefficient 易于观察，同一模型内也能有效生成 hypothesis；但不同 random seed、训练路径、宽度乃至
  architecture 会旋转或重参数化表示空间，相同功能未必落在相同坐标。约束从“某模型能否读出特征”变成
  “不同 realization 是否实现同一可因果验证的低维计算”，因此需要对 basis change 更稳健的比较对象。
- **Mechanism:** Algorithmic Core Extraction (ACE) 先对 task-conditioned activations `H` 做 mean centering，
  再堆叠 task outputs 对 hidden state 的 Jacobian `J`，对 interaction `H J^T` 做 SVD；由领先左奇异向量
  回投得到 hidden-space core，经 QR 形成投影 `P`。实现还可用 `H^T H` 与 `J^T J` 的低维 factorization
  避免显式构造大 interaction matrix。rank 先按 singular-energy threshold 选择，再用 intervention refinement
  检查：`P h` 的 core-only 作为 sufficiency，`h-P h` 的 core-removed 作为 necessity。论文把它类比为
  reachability/observability 与 balanced truncation；在非线性网络中这是解释性类比，不是精确的最小实现定理。
- **State Ownership / Control and Data Flow:** core 不是模型原生 runtime state，而是由指定 dataset、target
  output、layer、centering、Jacobian 与 rank rule 共同定义的离线分析 artifact。原 activation 进入候选 layer，
  analyzer 估计 task-active 与 task-sensitive directions，得到 projector；干预时以 core-only、core-removed 或
  reflected activation 替换 residual state，再执行剩余 forward path。dataset、target margin、layer selection、
  projector version 和 intervention strength 都是 provenance，不能只存一个“方向向量”。
- **Implementation / Evaluation Contract:** Markov 实验使用三个单层、`d_model=64`、四词表 Transformer，
  3,000 条长度 32 序列；modular addition 使用两个 layer、`d_model=128`、模 53 的 2,809 个输入对并做
  50/50 split，另以多个 modulus/weight-decay 条件做 grokking sweep；language 实验构造 1,200 条五模板的
  singular/plural subject–verb prompts，并只评估最后位置 `{are, were}` 与 `{is, was}` 的 number margin。
  v2 报告六个模型，但所有 language cores 都由同一窄任务、同一 prompt family、同一 output margin 提取；
  cross-model comparison 又包含 z-score、sign alignment 与相同输入，不能解释为不同维度空间中存在一条
  字面相同的 universal vector。
- **Evidence / Baselines / Ablations:** Markov 的 3D core 在三次训练中 core-only 保留接近目标 transition
  accuracy、core-removed 接近 chance，且拟合的 operator spectrum 对应已知 transition structure；modular
  addition 中 core 在 grokking 附近形成，继续 weight decay 时 necessary removal rank 扩大而 sufficient rank
  保持较小，并出现可拟合的 rotational modes；v1 的 GPT-2 三模型、v2 的六模型在受限 agreement margin 上
  均呈现高 core-only AUC、低 removed/flipped AUC。grokking sweep 的 12 seeds/condition 与多项 ablation
  提供重复性，但理论 scaling fit 依赖 memorization 后近零 loss、weight-decay drift、加性 modes 等假设，
  常数还由实验拟合。
- **What the Evidence Proves:** 在这些受控任务和干预定义下，ACE 能找出比逐坐标比较更 compact、对
  basis change 更稳健、同时具有 task-specific sufficiency/necessity evidence 的子空间；几何上近乎正交的
  learned representations 仍可能通过 canonical coordinates 呈现相似 operator structure。它加强了
  “functional equivalence 不等于 coordinate equality”的证据，并表明跨 run 比较应优先比较可执行计算与
  causal effect，而不是神经元编号或 raw cosine。
- **What It Does Not Prove:** 同一 target、test activations 与 intervention family 同时参与 core 提取、rank
  选择和验证，存在 selection/circularity 边界；operator fitting 的部分 transition 可以 hold out，但不等于
  整个 core discovery 在独立 task distribution 上完成。projection 会产生 off-manifold residual states，
  core-removed 的性能下降也可能包含 intervention damage；分布式或冗余实现会让“necessary”依赖删除方式。
  subject–verb agreement 不能证明模型的全部语言、推理或 world model 压缩为同一 algorithm；generation
  steering 每步需多次 forward、以 verb-token mass gating，属于为同一任务设计的控制器。synthetic grokking
  与 weight-decay scaling 不能外推到 frontier pretraining，跨模型相关也不证明共享人类概念。
- **Limitations / Threats to Validity:** 三个 family 都是作者选定且结构清楚的任务；layer 又按最大 flip effect
  选择。language dataset 含刻意不合语法模板，输出目标只有四个 verb tokens；未测试 multi-step reasoning、
  multifunction decomposition、真实 distribution shift 或 adversarial counterfactual。core-only AUC 有时高于
  原模型，可能是投影消除了 competing information，而不是重建完整 computation。当前 code 没有锁定所有
  model weights、provider/environment 与 paper tables 的 immutable manifest。
- **Trade-offs / Previous Design Still Applies:** ACE 把 readout 与 causal subspace intervention 连成一条
  较强证据链，代价是需要 output Jacobian、task dataset、layer/rank search、多轮 ablation 和 off-manifold
  风险；它得到的是 task-conditioned equivalence class，而不是廉价、全局、唯一的 feature dictionary。
  probe、single-neuron analysis、sparse decomposition、activation patching 与 replacement-model graph 仍各自
  适合快速定位、稀疏可读性、path-specific hypothesis 或更完整 computation reconstruction，不能被 ACE 替代。
- **Evolution Relationship:** `coordinate/neuron match -> decodable direction -> localized intervention ->
  sufficient/necessary task subspace -> cross-run canonical operator -> cross-architecture replication` 是
  `Direct Refinement` of interpretability evidence；与 control theory 是 `Explanatory Analogy`。旧坐标分析在
  architecture 相同、feature sparse、debug latency 优先时仍合理；新方法解决 equivalence under reparameterization，
  同时引入 task definition、projector provenance、selection bias 与 intervention validity 新问题。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch5 为主 owner，Ch62 为 evidence-governance
  handoff；已读 Ch4、Ch5、Ch6。Ch4 负责 optimization，不应吸收 synthetic weight-decay scaling；Ch6 负责
  Transformer 信息路由，也不把 narrow agreement core 写成通用架构规律。Ch5 已有 correlation → decodability
  → localized intervention → downstream change → cross-context/cross-model replication 的证据阶梯，并已警告
  Jacobian local approximation、replacement faithfulness 与 intervention 连带影响；真实缺口是没有明确区分
  coordinate similarity、basis-invariant functional equivalence，以及 sufficiency/necessity 在 redundancy 与
  off-manifold intervention 下为何不对称。
- **Integration Decision:** `Full Review Complete — Books Candidate / Cross-Realization Invariant and
  Causal-Subspace Contract`，`Status: Experimental`。Evidence Gate 尚未关闭，本轮不修改 Books；后续只能
  refine Ch5 的现有证据阶梯，不写模型排名、不把 synthetic scaling 写成一般规律。
- **Open Questions:** 如何用独立 discovery/test distributions、pre-registered layer/rank rule 与 in-distribution
  intervention 降低 circularity？多任务共享与 task-specific core 怎样分解？冗余路径下 necessity 应如何定义？
  operator 在 model revision、fine-tuning、quantization 与 distribution shift 后是否保持，projector provenance
  又怎样进入可复现实验 contract？

### Easy to Learn, Yet Hard to Forget / CUPID

- **Candidate / Week / Score:** Easy to Learn, Yet Hard to Forget / CUPID；原 W09 screening score
  21/30；`Source Family ID: bias-aware-machine-unlearning`；经 first-public 复核后不计入 W09 分母。
- **Source Type / Event Date / Revision / Access:** AAAI-26 full paper + institutional research announcement；
  Chung-Ang University 官方成果页已于 2025-12-16 公开标题、shortcut unlearning、CUPID 框架与三套实验
  数据，因此事件归 2025-W51。arXiv:2602.21773 v1 于 2026-02-25 提供完整 manuscript，AAAI proceedings
  页面于 2026-03-14 正式发布，二者只作为同一 source family 的后续全文与出版证据。已逐节阅读 arXiv
  HTML v1、Appendix 与 AAAI 官方页面；未发现作者公开 code/release，第三方 `Code: TBD` 只作为缺失线索，
  不作为 primary evidence。
- **Full-read Coverage:** metadata 与 publication history、Abstract、Introduction、Related Work、问题定义、
  shortcut-unlearning analysis、三阶段 Method 与全部公式、两组主实验、metrics、baselines、component/
  gradient/sharpness ablations、Conclusion，以及 Appendix 的 dataset construction、hardware、optimizer、
  batch、epoch 与 hyperparameters 均已覆盖。正文没有独立 Limitations/Threats section，也未披露 seed、
  confidence interval、完整 MIA attacker contract、运行成本或端到端 artifact manifest。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint:** exact retraining 是删除某类
  训练影响的理想 comparator，却通常成本过高；NegGrad、relabeling、distillation 与 sparse-parameter update
  因而用低成本近似“在 forget set 上降低保留”。这些方法在目标属性可从其他表示中近似分离时合理。
  新约束是训练数据存在强 spurious correlation：模型对 class 的预测同时依赖 class feature 与 shortcut，
  平均 forget accuracy 降低可能只表示 shortcut 被移除，甚至让 bias-conflicting 的待忘类别准确率反而提高。
- **Mechanism / State Ownership / Control and Data Flow:** CUPID 只持有原模型 `theta_o` 与 class-wise forget
  set，不需要 retain set。第一步为每个 forget sample 沿归一化 gradient 做参数扰动，以 loss change 作为
  local-sharpness proxy；按 top `k%` 把样本分为 causal-approximated 与 bias-approximated derived subsets。
  第二步在 causal-approximated subset 上用 `0.5 * theta_i^2 * E[H_ii]` 排序，以 percentile mask `m_c`
  划出所谓 causal pathway，其补集为 bias pathway。第三步把全 forget gradient 投影到 causal-subset
  average gradient，得到 `g_proj`，把正交余量定义为 `g_bias`，再分别路由到 `m_c` 与 `1-m_c` 参数。
  原始数据与模型是 authoritative state；sharpness、partition、Hessian-diagonal mask 和 gradient decomposition
  都是 model- and hyperparameter-dependent derived state，不能升级成已识别的真实因果结构。
- **Evaluation Contract:** 三个视觉分类数据集为 Waterbirds、BAR 与作者构造的 Biased NICO++；train 中
  bias-aligned:bias-conflicting 固定为 99.5:0.5，test 为 50:50。每个数据集随机选择一个 class 做 class-wise
  forgetting，模型统一为 ResNet-50。原模型在单张 NVIDIA RTX 3090 上训练 10 epochs、AdamW、初始
  learning rate `1e-4`、weight decay `1e-3`、cosine schedule、batch 128；所有 unlearning 方法运行 1 epoch、
  AdamW、固定 `1e-5`、batch 64。CUPID 固定 `k=5%`、扰动 `eta=1e-3`、mask ratio 50%。baselines 包括
  Retrain、NegGrad、Random Label、Bad Teaching、Boundary Shrink/Expand、SALUN 与 DELETE；metrics 为
  retain accuracy、forget accuracy、BA/BC gap、forget-set worst-group accuracy 与 membership-inference score。
- **Evidence / Ablations:** 在上述受控 contract 中，CUPID 的 forget accuracy、group gap 与 worst-group
  accuracy 优于所列 approximate baselines，并接近但未等同 exact retraining；主表同时显示部分 retain-
  utility 代价。三组件 ablation 与 `g_proj`/`g_bias` ablation 支持 partition、mask、gradient routing 在该
  implementation 中均有增量；sharpness percentile 分析明确显示 causal-approximated subset 并不纯，作者
  观察到 `k=5%` 而非最纯 partition 最好，并将其解释为 regularization。该证据支持“biased representation
  会让平均 unlearning metric 误判，以及 pathway-aware update 是可行研究分支”，不证明 sharpness 等于
  causal semantics、Hessian mask 找到真实 causal circuit、MIA 分数构成删除证明，或该机制可直接扩展到
  LLM、instance/concept unlearning 与不同 bias ratios。
- **Limitations / Threats / Trade-offs / New Failure Modes:** 单架构、三个视觉数据集、单一重偏置比例、每库
  一个随机 forget class 且无 seed/区间，限制 external validity；没有公开 code 与 immutable run manifest，
  新构造 Biased NICO++ 的 exact sample list 也无法从论文单独冻结。per-sample adversarial gradient、
  Hessian diagonal 与 mask construction 增加计算/内存成本；固定 5%/50% threshold 对数据、checkpoint、
  class frequency 和 curvature scale 敏感；derived partition 若错，会把 retain utility、bias behavior 与删除
  目标一起改写。低 forget accuracy 仍可能来自 decision-boundary damage，而不是训练影响被移除。
- **Where Previous Designs Still Apply / Evolution Relationship:** exact retraining 在法规、高风险审计或数据量
  可控时仍是最强 comparator；retain-set distillation 在保留数据可访问、utility 优先时仍合理；uniform/sparse
  approximate update 在目标较可分、成本严格受限时仍有价值。演进路线是
  `exact retraining -> output/loss-level approximate forgetting -> sparse update -> bias-sliced evaluation ->
  proxy-pathway targeted update -> deletion certificate under explicit threat model`。CUPID 只推进到倒数第二步，
  属于 `Direct Refinement`，没有替代前序分支，也没有完成最后的可验证删除。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage:** Ch68 为主 owner，Ch62 为评估证据
  handoff；已读 Ch67～69、Ch62 与 Ch25。Ch25 owner 是 demonstration-conditioned SFT，不应吸收一般模型
  删除算法；Ch68 已要求先定义 privacy unit/threat model，却缺少“删除目标与 spurious attribute 纠缠时，
  平均 forget metric 会奖励错误机制”的长期边界；Ch62 已有 distribution/slice/scorer contract，可承接
  BA/BC slice、exact-retrain comparator 与 uncertainty，不复制 CUPID recipe。该归属不要求新增 Part 或章节。
- **Integration Decision:** `Cross-Year Exclusion — First Public 2025-12-16 / Not a 2026-W09 Event`。
  全文 disposition 为 `Books Candidate / Unlearning Target-Specification and Shortcut-Forgetting Evaluation
  Contract`，`Status: Experimental`；后续应在 2025-W51 归档并经其 Evidence Gate 决定是否 refine Ch68，
  W09 不产生 Books Decision。
- **Open Questions:** 如何为 instance/user/concept unlearning 定义可验证 target unit，而不是借 class accuracy
  代替？partition/mask 在不同 bias ratios、多个 forget classes、Transformer/LLM 与 repeated deletion 下是否
  稳定？能否用 exact-retrain distance、extraction/MIA、group slices、utility、compute 与 repeated-seed
  uncertainty 共同组成 deletion evidence？proxy pathway 的 provenance、supersession 与 rollback 如何进入
  Model Registry 和 release gate？

### AgentVista

- **Candidate / Week / Score:** AgentVista / 2026-W09 / 24/30；
  `Source Family ID: realistic-multimodal-agent-evaluation`。
- **Source Type / Event Date / Revision / Access:** multimodal-Agent benchmark + dataset + evaluation harness；
  arXiv:2602.23166 v1 首次公开 2026-02-26，v2 于 2026-03-02。事件按 v1 归 W09；已阅读全文、Related
  Work、全部 construction/evaluation/analysis 与 Appendix，并联读作者 project、GitHub repository、HF dataset
  card/viewer 和 current harness。HF 03-06 是 discovery lag；v2/current code 只用于 revision 与 artifact 边界，
  不倒填 first-public date。
- **Full-read Coverage:** metadata、Abstract、Introduction、benchmark comparison、taxonomy、三个 design
  principles、四阶段 data construction、tool environment、14-model setup、main results、tool distribution/
  ablation、error analysis、test-time scaling、Related Work、Conclusion/Impact Statement，以及 Appendix 的
  source composition、tool schema、open-model baselines、construction/evaluation prompts、error taxonomy 与
  good/bad trajectories均已覆盖。
- **Original Problem / Why Previous Designs Were Reasonable / Changed Constraint:** static VQA 或单一视觉工具
  benchmark 便于控制变量、降低网络漂移并提供确定评分；但真实多模态 Agent 要从 cluttered image 提取细节，
  再把视觉操作、web/image search、page visit 与 computation 交错成多步 workflow。约束由“固定 context 中
  答对”变为“在给定工具、预算和在线信息环境中保持视觉 grounding、constraint state 与最终 outcome”。
- **Dataset Construction / Selection Ownership:** 原始池超过 300K images/scenarios；Stage 1 用
  Claude-Opus-4/4.1 model-assisted filtering 加人工筛查留下 568 initial states，Stage 2 expert rewriting 得到
  315 tasks，Stage 3 在同一 tool environment 执行并用 Gemini-3-Flash 筛 tool-use diversity，同时用无工具的
  Gemini-2.5-Pro 排除 prompt-only 可解项，留下 241，Stage 4 两轮独立复核后得到 209 tasks / 308 images、
  7 categories / 25 sub-domains。每项平均约 4 小时构造、expert 平均约 30 分钟求解。该 pipeline 提高视觉依赖
  与 answer validity，也把 filter models、tool schema、minimum-two-tool-category rule 和“确定短答案”偏好写入
  benchmark distribution；它不是自然流量的无偏抽样。
- **Harness / State / Control and Data Flow:** subject 接收 image(s)+query，在最多 30 次交互内每轮只能调用一个
  tool；四类工具为 web search、image search、visit 与 stateful Python code interpreter。tool output、生成图像、
  accumulated context、remaining turns/tokens、model/prompt/provider 与外部 search/page snapshot 都参与下一步
  state。最终 `<answer>` 由固定 GPT-4.1 judge 对 annotated short answer 评分；因此测量对象是
  `model snapshot + prompt + four-tool implementation/provider + web state + budgets + judge + dataset revision`，
  不是裸模型能力。
- **Implementation and Reproduction Boundary:** 论文统一报告 `temperature=0.6`、30 tool turns 与 accuracy；
  current repository 的 `run.sh` 设置 30 turns、100 images、65,536 total tokens，却没有显式传 temperature，
  因而落到 `infer.py` 当前默认 `temperature=0.0`。README quick start 同样不能自动重现论文 sampling contract。
  repository 当前 main 只有少量 commits、无 release/tag 或 immutable paper-run manifest；Serper/Jina、model API
  和网页内容又会漂移。公开 code/dataset 提高可检查性，但不等于 paper tables 已冻结复现。
- **Evaluation Contract / Results:** dataset 为 209 条小样本、单图 151、多图 58；14 个公开/闭源 model
  snapshots 在相同 headline protocol 下比较，作者报告 Gemini-3-Pro overall 27.27%，GPT-5.2 平均 13.85 tool
  turns。多图 slice 较高不能解释为 multi-image 本身更容易，因为 task composition/difficulty 没有配对控制。
  tool ablation 只在 Gemini-3-Pro 与 Claude-Sonnet-4.5 上比较 all/vision/search/no-tool，并随 capability 改写
  prompt；它支持“在这两种 subject 和该 dataset 上工具组合有增量”，不是各工具的独立因果效应。Best-of-K
  只在 Gemini-3-Flash 上以同一模型作 reward selector；K=16 的 BoN 30.62% 与 Pass@16 51.67% 显示主要瓶颈
  同时包含 candidate discovery 与 selection，但不能证明 RL 是唯一解。
- **Failure Evidence / Attribution Boundary:** 四个 model 的错误由 Gemini-3-Flash 读取 trajectory 后自动标为
  tool execution、visual misidentification、knowledge hallucination、calculation、instruction misinterpretation 或
  other，作者观察 visual misidentification 为主。该 taxonomy 是有用 hypothesis generator，却没有披露逐类
  human calibration、inter-rater reliability 或 multi-label/causal adjudication；早期视觉错误会级联为 retrieval、
  reasoning 与 final-answer error，单一 primary label 不能视作根因真值。final-answer judge 也不验证 intermediate
  evidence provenance、unsafe side effect、retry/recovery 或路径效率。
- **What the Evidence Proves / Does Not Prove:** 证据证明作者构造出一个公开的、视觉依赖、混合工具、短答案
  可评分的受控 workload，并在给定 snapshot/harness 下暴露较低 task success 与长轨迹 failure。它不证明
  “真实世界 Agent”总体准确率、闭源模型长期排序、更多图片通常更容易，或某个 failure label 是模型固有原因；
  更不覆盖 browser action side effects、authorization、dynamic UI、long-running recovery、用户 clarification 和
  open-ended artifact quality。
- **Limitations / Threats / Trade-offs / Old Branches:** 强制 hybrid-tool 与 difficulty filtering 增加诊断压力，
  代价是 construct validity 与 selection bias；短、确定答案让评分便宜，却排除了计划、报告、推荐和多合法答案；
  live web 提高现实性，也削弱 temporal reproducibility；单一 model judge 可扩展，却带来 shared-family/style/
  format bias。static VQA、单工具 suites、frozen replay 和 executable environment 仍分别适合隔离 perception、
  component regression、长期可比与真实 side-effect correctness，不能被 AgentVista 单向替代。
- **Evolution Relationship:** `static multimodal QA -> isolated visual/tool capability -> controlled hybrid-tool
  trajectory -> vision-centric live-information workflow -> outcome + provenance + side-effect/recovery evaluation`
  是 `Direct Evolution`；最后一步仍是 AgentVista 未覆盖的下一阶段压力。benchmark construction model、runtime
  harness 与 judge 都必须成为 evaluation identity，属于 Ch62 已有 subject/environment/scorer contract 的
  `Principle Refinement`。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage:** Ch62 为主 owner；已读 Ch61～63，
  并复核 Ch74、Ch75、Ch77 的 tool、plan 与 workflow边界。Ch62 已明确完整 subject identity、相对分布、
  Agent outcome、trajectory evidence、judge calibration 与 dataset governance，故“模型分数不能脱离 harness”
  已覆盖；真实 refine 缺口是没有把 **construction-time filter model/tool rule 对 task population 的选择** 与
  **post-hoc single-label error attribution 不等于 causal root cause** 连成同一 measurement chain。Ch74 只拥有
  tool contract，Ch75 只拥有 plan state，Ch77 只拥有 durable side effect/recovery，不复制 benchmark 结果。
- **Integration Decision:** `Full Review Complete — Books Candidate / Task-Construction–Harness Coupling and
  Failure-Attribution Boundary`，`Status: Experimental`。Evidence Gate 未关闭，本轮不改 Books；后续只能 refine
  Ch62 的 Dataset/Trajectory Judge 既有论证，不写模型排行榜或 27.27% headline。
- **Open Questions:** filter model、no-tool baseline 与 minimum-tool rule 对不同 model families 的选择偏差有多大？
  怎样冻结 search/page evidence 又保留现实 drift？怎样用 independently sampled human/executable evidence 校准
  judge 与 error taxonomy？在 matched task、provider、prompt、token/turn/cost budgets 下，visual grounding、
  retrieval、planning 与 tool execution failure 如何做 counterfactual attribution？

### Large Multimodal Models as General In-Context Classifiers / CIRCLE

- **Candidate / Week / Score:** Large Multimodal Models as General In-Context Classifiers / CIRCLE /
  2026-W09 / 20/30；`Source Family ID: multimodal-in-context-classification`。
- **Source Type / Date / Revision / Access:** arXiv:2602.23229 v1 首次公开 2026-02-26；CVPR Findings 2026。
  已读 official CVF accepted-paper page、作者 project/author pages，以及在本轮 arXiv direct access 不可用时使用的
  public full-text mirror。已覆盖 Metadata、Introduction/Related Work、全部 closed/open-world Method 与算法、
  实验 protocol、全表、context-size/refinement-round ablation、streaming experiment、Conclusion/Limitations 和
  Supplementary implementation/results。未定位到 public code repository 或 immutable paper-run manifest；
  HF 03-06 只作为 discovery-lag signal，不作为论文证据。
- **Original Problem / Why Previous Designs Were Reasonable:** closed-world classification 已知 label set，
  CLIP-like VLM 可直接比较 image/text embeddings，Tip-Adapter 再用 labeled support cache 修正 logits；LMM 则把
  label set 写成 MCQ，并拼接 `(image,label)` demonstrations。在 label taxonomy 稳定、labeled support 可靠、
  task 与 prompt 对齐时，这些静态方案仍合理。open-world 场景没有固定 label set，context 又只有 unlabeled
  images；独立 pseudo-label 会把局部命名噪声直接写入 demonstrations，random/similarity context 也无法保证
  多个 examples 形成一致的 task structure。
- **Changed Constraint / Mechanism:** CIRCLE 把 context images 视为 immutable observations，把 pseudo-label
  vector 视为 mutable derived state。先独立生成初始 labels；随后对每个 image `j` 使用其余 `m-1` 个
  `(image, previous-label)` pairs 构造 leave-one-out context，并行重标 `j`；重复 `T` 轮后再用 refined context
  分类 query。这不是参数更新，而是 self-conditioned context-state refinement。closed-world 中 VLM 使用平衡的
  `k × |S|` support，而 LMM 因 context budget 只使用 `k` 个 random 或 CLIP-retrieved pairs；论文虽报告 k-NN
  baseline，仍不能把两类 architecture/opportunity contract 当成严格等资源比较。
- **State Ownership / Control and Data Flow:** run identity 至少包含 context image IDs、pseudo-label vector、
  round/order、context-selection/retriever、prompt/template、model/tokenizer、decoding、image resolution 与 query。
  数据流为 `unlabeled images → independent labels → leave-one-out relabel → synchronized label snapshot → next
  round → query classification`。并行 relabel 必须读取同一上一轮 snapshot；若异步读取新旧 labels，论文算法的
  round semantics 已被改变。retrieval 只负责 demonstration selection，故 Ch72 是 handoff 而非主 owner。
- **Evaluation Contract:** 10 个 classic image datasets；CLIP ViT-B/32、B/16、L/14 与 Qwen2-VL 7B、
  Qwen2.5-VL 7B、LLaVA-OneVision 7B、Phi-3.5-Vision、Phi-4-Multimodal。closed-world `k=4/8/16`；
  open-world 默认 `m=16`，以 LI、SS、bCS、mCS 四类语义/包含度量评估。补充材料披露 greedy decoding、最多
  64 output tokens、context images 缩放为 224×224；A100 40/64/80GB，简单实验单卡，大 context 最多 4 卡，
  per-GPU batch 随模型降为 8/4/2。streaming 的 Food101/SUN397 作者报告需 8～10 小时，但未披露固定 GPU
  型号/数量组合、random seeds、方差/置信区间、总 token/FLOP/energy 或 SLO，不能做跨系统性能结论。
- **What the Evidence Proves / Does Not Prove:** 在作者限定的 models、datasets、prompts 与四种 metrics 下，
  naive/random/pseudo context 经常使 open-world output 不稳定，leave-one-out iterative refinement 在多数组合上
  改善 semantic consistency；context-size 与 round ablation 也支持收益递减。它证明的是“相互依赖的 derived
  labels 可优于独立 pseudo-label”这一受限机制证据，不证明 LMM 普遍优于 VLM、CIRCLE 找回真实 latent
  taxonomy，或 broad concept lists 等同高质量分类。作者自己说明 bCS 可能被宽泛且未 grounding 的 label list
  抬高；streaming 只是从既有 test stream 随机取历史 items，不是 drift、adversarial arrival 或生产 online
  memory 的验证。
- **Trade-offs / New Failure Modes / Old Branches:** 每轮约需 `m` 次 LMM calls，主体成本随 `T*m` 增长并
  叠加 query；还新增 mutually reinforcing wrong labels、semantic collapse、order/selection sensitivity、
  coherent-but-task-misaligned convergence、context token/VRAM 与 streaming update overhead。作者明确承认无
  supervision 会收敛到语义一致但 task-misaligned 的解释。固定 taxonomy + labeled support、VLM similarity/
  adapter 与独立 zero-shot 在低成本、强监督或 context-noise 风险更高时仍成立；新机制不是对旧分支的覆盖。
- **Evolution Relationship:** `Direct Evolution`：static/random ICL → independent pseudo-labeled context →
  dependency-aware iterative refinement；与 Ch72 retrieval 为 `Layering / Dependency`，与 Ch62 metric/harness
  contract 为 measurement boundary，不把 evaluation metric 当作 task truth。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** 已完整阅读 Ch70、Ch71、Ch72，并复核本轮已读
  Ch62。主 owner 修正为 Ch71；Ch27 是 RLHF，与该机制无关。Ch71 已覆盖 assembly、derived-view lifecycle、
  context identity、compression loss 与 evaluation，但尚未明确 **model-generated demonstrations 本身也可能是
  带 lineage 的 mutable derived state**，更未展开 iterative self-conditioning 的 snapshot、convergence 与
  error-amplification contract。Ch62 只承接 metric validity/opportunity parity，Ch72 只承接 example retrieval。
- **Integration Decision:** `Full Review Complete — Books Candidate / Self-Conditioned Context Refinement and
  Error-Amplification Contract`，`Status: Experimental`。Evidence Gate 未关闭，本轮不修改 Books；后续只 refine
  Ch71 的 derived-view/context identity 论证，并向 Ch62/72 增加短 handoff，不复制模型排名或 headline 数字。
- **Open Questions:** 怎样以 confidence、agreement 或 external verifier 阻止 mutually reinforcing label errors？
  同步 round snapshot 与 asynchronous/streaming update 的语义如何定义？何种 stopping/convergence signal 能区分
  稳定正确与稳定错位？在 matched context tokens、GPU-hours、retrieval opportunity、多个 seeds 和真实 drift 下，
  refinement 相对 static support/adapters 是否仍有净收益？

### Truncated Step-Level Sampling / SLATE

- **Candidate / Week / Score:** Truncated Step-Level Sampling / SLATE / 2026-W09 / 25/30；
  `Source Family ID: retrieval-rl-step-credit-assignment`。
- **Source Type / Date / Revision / Full-read Coverage:** arXiv:2602.23440 v1 首次公开 2026-02-26；v2
  2026-03-12、v3 2026-04-01、当前 v4 2026-07-09。HF 03-06 只是延迟 discovery signal。已读 v1 的
  Introduction、Related Work、全部 Method/公式、Theory/证明、Experiments、baselines、ablations、
  training dynamics、group-size sensitivity、algorithm 与 reward prompts；并联读 current v4 新增的
  computational-cost、reward-hacking、bias/limitations、rollout-volume 与 hyperparameter 边界，以及作者
  repository。后续 revision 只用于补足边界，不作为 W09 新事件。
- **Original Problem / Why Previous Designs Were Reasonable:** Search-R1 的完整 trajectory + outcome EM
  reward 实现简单、terminal signal 可验证，不需要主观 process labels；StepSearch 等 full-trajectory process
  reward 又能保留所有分支的未来结果。在 horizon 短、terminal verifier 强、每一步难以局部判定时，两者
  仍合理。但同一 sequence advantage 作用于所有 tokens，会把其他 steps 的随机性混入当前 action；完整
  branching 还让生成成本随 group size 与 horizon 增长。
- **Changed Constraint / Mechanism:** SLATE 固定当前 prefix `tau_<t`，从同一 state 采样 `k` 个单步
  `(think, query)` 或 answer candidates，分别由 Gemma3-27B judge 给出 thinking/query/answer 的 ternary
  reward，再做 step-local group normalization。只按 reward-weighted sampling 选择一个 candidate 进入下一
  prefix，其余 candidates 只贡献当前步 gradient。retrieved tokens 被 loss-mask；answer candidate 另加
  `lambda(B-t)/B` early-termination bonus。它把比较条件从“同 prompt 的完整 responses”收紧到“同 prefix
  的 next actions”，但也主动放弃同一 trajectory 内的 retroactive future credit。
- **State Ownership / Control and Data Flow:** training sample 拥有 question/gold answer；2018 Wikipedia
  snapshot、E5 index 与 top-3 retriever 拥有 environment observation；prefix 只保留选中 action 与 retrieval；
  policy/old/reference versions 拥有 sampling、importance ratio 与 KL；judge rubric/version 拥有 local reward；
  group statistics 拥有 step advantage；early-stop bonus 拥有 search-budget pressure。若这些 identity 不进入
  run manifest，reward drift、retrieval drift 与 policy staleness 会被误写成算法收益。
- **Theory Boundary:** “不高于 full trajectory variance”的 bound 需要 current reward 与 future reward 的
  conditional covariance 非负、且 group size matched；`T` 倍结论还要求 conditional independence 与各步
  variance 近似对称。sample-efficiency 推论再假设每步平均 token 为 `L/T`。这些是假设下的 scalar-advantage
  结果，不是对真实 policy-gradient variance、wall-clock 或任意 long-horizon Agent 的无条件保证；论文没有
  用直接 variance measurement 验证这些 assumptions。current v4 自己也承认 local reward 可能把 globally
  dead-end action 评为 promising，且方法不把 later reward 追溯给 earlier action。
- **Evaluation Contract:** policies 为 Qwen2.5-7B-Base 与 3B-Base；训练 NQ+HotpotQA，评测 7 个 factoid QA
  datasets；2018 Wikipedia + E5/top-3；`k=5`、`B=4`、`eta=0.7`、`lambda=0.1`、LR `1e-6`、clip `0.2`、
  KL `0.001`；LoRA rank 16/alpha 64、BF16、batch 32、max length 4096、500 steps、2×A100。主指标为 EM。
  论文未报告 random seeds、方差/置信区间、judge-human agreement、judge calibration、judge GPU/latency、
  wall-clock 或总 energy/cost。repository 当前只有 4 commits，未以 immutable manifest 锁定 paper run。
- **What the Evidence Proves / Does Not Prove:** 在作者 recipe 中，full SLATE 相对相同 7B recipe 的
  no-truncation ablation 平均只增加 1.1 EM，而移除 LLM-judge reward 降 2.4 EM；这支持 prefix isolation 与
  dense reward 有互补贡献，也说明 headline 不能全归因于 truncated sampling。7B/3B 对 Search-R1 的结果
  只绑定该模型、retriever、短 budget 与 EM protocol。StepSearch 训练数据不同且只报告 multi-hop，repository
  又显示 Search-R1 参考配置为 1005 steps/8×A100，不能据此声称 compute-matched 全面优越。不同方法的
  training-reward curves 量纲不同，current v4 已明确只能比较各自 convergence 形状，不能比较 reward 高度。
- **Trade-offs / New Failure Modes / Old Branches:** prefix isolation 降低局部 confounding，却把 exploration
  收缩成每步单一路径，并新增 judge bias、reward hacking、local/global objective mismatch、early-answer bias、
  judge serving cost、group all-equal 与 shared-prefix blind spot。完整 trajectory outcome reward 在 verifier
  可靠、局部步骤不可评、deceptive reward 或强跨步依赖时仍成立；tree/full-trajectory exploration 在需要保留
  多个未来分支时仍成立。更成熟系统应把 local process reward 与 terminal outcome/retroactive correction
  组合，而不是把后者覆盖掉。
- **Evolution Relationship:** `Direct Evolution`：outcome-only full trajectory → full-trajectory process reward
  → shared-prefix step-local comparison；与 Ch72 iterative retrieval 为 `Layering / Dependency`，与 Ch75
  planning/search branching 为 boundary，不把 training credit assignment 写成 deployment planner。
- **ROADMAP / Adjacent Chapters Read / Existing Coverage:** Ch29 为主 owner；已读 Ch29、Ch72、Ch75。
  Ch29 已说明 sequence reward 抹平 token credit，process reward 会增加 evaluator/exploit surface，但尚未把
  “comparison cohort 从同 prompt 缩到同 prefix”作为独立设计轴，也未展开 local credit 与 future credit 的
  trade-off。Ch72 拥有 retrieval data path，Ch75 拥有 inference-time planning，不重复机制正文。
- **Integration Decision:** `Full Review Complete — Books Candidate / Shared-Prefix Local-Credit Contract`，
  `Status: Experimental`。Books Gate 仍关闭；后续只 refine Ch29，保留 theorem assumptions、judge contract、
  terminal outcome 共存条件与 local/global failure mode，不搬运作者 leaderboard。
- **Open Questions:** 非负 covariance、conditional independence 与 variance symmetry 在真实 search traces 中
  是否成立？如何用 terminal return 给 earlier action 做低方差 correction，而不恢复 full-trajectory confounding？
  judge version/calibration、retriever snapshot 和 policy checkpoint 怎样共同 version？matched total judge+
  rollout compute、多个 seeds 与更长 horizon 下，prefix isolation 的收益是否仍存在？

### BBQ-to-Image

- **Candidate / Week / Score:** BBQ-to-Image / 2026-W09 / 18/30；
  `Source Family ID: structured-parametric-image-control`。
- **Source / Rejection Check:** arXiv:2602.20672 v1 首次公开 2026-02-24；HF 03-04 延迟发现。论文将 numeric
  bounding boxes 与 RGB triplets 编码进 structured text conditioning，主要解决 text-to-image 的位置/颜色
  控制。来源与日期可信，但与当前以 AI System lifecycle/infrastructure 为主的 ROADMAP 只有 Ch27 边界关系。
- **Disposition:** `Source/Date Verified — Low Project Relevance / Weekly Only`。不因 headline alignment
  指标升级为 Books；未来若形成跨模态 structured-control interface 演进链再重开。

### Simulating Social Media Users with LLMs / CCP

- **Candidate / Week / Score:** Simulating Social Media Users with LLMs / CCP / 2026-W09 / 19/30；
  `Source Family ID: operational-validity-of-silicon-subjects`。
- **Source / Rejection Check:** arXiv:2602.22752 v1 首次公开 2026-02-26，WASSA/EACL 2026；HF 03-04
  延迟发现。研究以 authentic comments 对 Conditioned Comment Prediction 做 operational-validity 检验，
  摘要报告 SFT 可能改善表面形式却损害 semantic grounding。
- **Disposition:** `Source/Date Verified — Weekly Only`。其长期提醒已被 Ch62 的 construct validity、
  distribution shift 与 model-judge/metric boundary 覆盖；若全文显示新的 simulation provenance 或
  persona-privacy contract，可幂等升级。

### SGDC

- **Candidate / Week / Score:** SGDC / 2026-W09 / 17/30；
  `Source Family ID: structure-guided-medical-segmentation-convolution`。
- **Source / Rejection Check:** arXiv:2602.23496 v1 首次公开 2026-02-26，附作者代码；HF 03-04 延迟发现。
  机制用受监督 structure-extraction branch 引导 dynamic kernels/gates，证据集中在特定 medical segmentation
  datasets 与 boundary metrics。
- **Disposition:** `Source/Date Verified — Low Project Relevance / Weekly Only`。它没有改变当前模型、训练、
  serving、evaluation 或 Agent 章节的长期设计结论；不把 domain SOTA headline 写入 Books。

### CUDA Agent

- **Candidate / Week / Score:** CUDA Agent / 2026-W09 / 29/30；
  `Source Family ID: executable-kernel-rl-environment-2026`。
- **Source Type / Event Date / Revision:** arXiv:2602.24286 v1，2026-02-27；联读 v1 HTML 的
  Introduction、Related Work、Method、Experiments、全部 ablation、data/agent-loop appendix、case studies
  与 Limitations。HF 03-02 只是延迟 discovery signal，不改变 first-public week。
- **Original Problem / Why Previous Designs Were Reasonable:** training-free search 能用 compiler、tests 与
  profiler 迭代 kernel，不需要训练新模型，适合任务少、frontier model 已有足够 CUDA prior 的场景；固定
  execution-feedback fine-tuning 则易复现、成本边界清楚。但前者受 base-model intrinsic capability 限制，
  后者把全部历史塞进 context，并把 debugging/search/profiling 固定在人工 loop 中，难以形成可迁移 policy。
- **Changed Constraint / Mechanism:** 系统先从 PyTorch/Transformers operators 构建 seeds，再用最多五个
  operators 做 compositional synthesis，以 eager/compile 可执行性、determinism、anti-hacking、1～100 ms
  eager runtime 和 AST similarity threshold 过滤成 6K tasks。Agent 在受保护的 CUDA development
  environment 中编译、验证、profiling 与迭代；reward 不回归 noisy raw speedup，而用 correctness、超过
  eager/`torch.compile` 5% 等 milestones 映射到 `{-1,1,2,3}`。为处理 domain mismatch 与低概率 CUDA
  tokens 导致的 importance-ratio instability，训练先做 single-turn RL，再用成功 trajectory 做 actor RFT，
  用 trajectory/value targets 预热 critic，最后进行 long-context multi-turn PPO。
- **State Ownership / Control and Data Flow:** task generator 拥有 problem/spec identity；CPU Docker sandbox
  拥有编译与 terminal state；独占 GPU pool 拥有 profiling measurement；protected verifier/profiler 拥有
  correctness/performance judgment；trajectory 绑定 actor/critic/policy version；reward mapping 把测量编译成
  update signal。工具权限禁止修改 verifier、禁止 fallback API，并用 warmup、device synchronization、重复
  measurement 与平均值约束 timing noise。换言之，`environment + verifier + profiler + reward mapping`
  共同构成被 policy 优化的接口，而非模型外部的中立设施。
- **Evaluation Contract:** Seed1.6 MoE（23B active / 230B total），global/mini-batch 1024，actor/critic
  learning rates `3e-6/6e-6`，single-turn/agentic context 32K/128K，150 training steps，training/eval 最多
  150/200 turns；CPU/GPU decoupled sandbox 与 128 NVIDIA H20。KernelBench L1～L3 共 250 tasks，baseline
  agent 使用同一 loop；报告 pass rate、faster rate 与 correct solutions 的 geometric-mean speedup，并从每条
  trajectory 选 best-performing solution。论文报告整体 98.8% pass、相对 `torch.compile` 96.8% faster-rate
  与 2.11× geomean；这些数字只属于上述 contract。
- **Ablation / Evidence Boundary:** 移除 agent loop、robust reward、RFT 或 value pretraining 均降低 faster
  rate；后两项 ablation 在 collapse 前取最后 validation step，不能与稳定完成训练的 full system 当作完全
  对称 endpoint。AST similarity `>0.9` 去重只排除高结构相似，不证明无语义 contamination。论文证明在
  KernelBench/H20/该 sandbox 下“数据 + environment + reward + warm-up”联合系统有效，未通过 factorial
  design 唯一归因每个子机制，也未证明跨 GPU、dynamic shapes、生产并发或任意 compiler 都成立。
- **Trade-offs / New Failure Modes / Old Branches:** 获得 intrinsic kernel policy 的代价是 128-GPU isolated
  profiling pool、长 rollout、编译队列、best-of-trajectory selection 与 verifier governance；新增 timing
  noise、reward hacking、numerical precision mismatch、sandbox-to-production drift、benchmark overfit 和
  expensive failed rollouts。论文未比较 TVM 等更强 compiler，作者也明确资源门槛。training-free search、
  compiler autotuning 与 human kernel engineering 在低频任务、硬件迁移、可解释性或训练预算受限时仍成立。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Evolution` from evaluator-driven search to
  policy-internalized optimization，Ch29 是 training-contract candidate，Ch62/77 是 executable evidence 与
  workflow boundary。Ch29 已覆盖 measurement-as-reward interface，Ch62/77 已覆盖 artifact、sandbox、
  verifier 与 evaluator-driven search；新增候选机制主要是 domain/precision mismatch 下 actor+critic
  staged warm-up，而不是再次复制“可执行 verifier 很重要”。Books Integration 前仍需完整重读 Ch28～30、
  Ch62 与 Ch77 并确定一个 owner。
- **Integration Decision:** `Full Review Complete — Books Candidate / Domain-Warm-up and Executable
  Reward Contract`；保持 `Experimental`，不把 KernelBench leaderboard 写成通用 CUDA-agent 结论。
- **Open Questions:** 训练/推理 precision 分别是什么、importance-ratio floor 如何随实现变化？在固定 total
  rollout compute 下，RFT、value pretraining、larger curriculum 与更强 training-free search 如何正交比较？
  dynamic shapes、multiple dtypes、different GPU generations 与 production concurrency 下如何重验？

### LK Losses

- **Candidate / Week / Score:** LK Losses / 2026-W09 / 27/30；
  `Source Family ID: acceptance-aligned-drafter-objective-2026`。
- **Source Type / Date / Revision:** arXiv:2602.23881 v1，2026-02-27；当前 v2 为 2026-06-01，标注
  ICML 2026。本轮联读当前 HTML 的 background、全部公式/gradient derivation、method、training/evaluation
  contract、results、appendix 与 limitations；v2 用于 revision verification，不把六月修改倒填为 W09 event。
- **Original Problem / Why KL Was Reasonable:** speculative drafter 常用 forward KL 对齐 target；若 draft
  capacity 足以达到全局最优，`KL=0` 与 acceptance `=1` 同时成立，KL 还在随机初始化时提供稳定、按误差
  幅度缩放的 gradient。因此 KL 不是“错误旧方案”。问题出现在 capacity-limited drafter、architecture/
  vocabulary mismatch 与可达的 suboptimal region：更低 KL 不必对应更高实际 acceptance。
- **Principle / Mechanism:** 单 token acceptance
  `α = Σ_x min(p(x), q(x)) = 1 - TV(p,q)`，所以目标应看到 verification 真正消费的 distribution overlap。
  纯 TV 虽方向正确，但 diffuse draft 下 gradient 可能随 vocabulary 变大而消失。论文给两条分支：
  adaptive hybrid 在 acceptance 低时保留较强 KL、对齐后逐步转向 TV；negative log-acceptance
  `L=-log α` 用 `1/α` 自适应放大 TV gradient。对 truncated vocabulary，out-of-vocabulary `q=0` 自然贡献
  零 overlap，避免把 masked target KL 变成 proxy-of-proxy。
- **State / Data Flow:** target logits `p` 与 draft logits `q` 生成 per-position overlap；training scheduler
  根据当前 acceptance 调整 KL/TV mix；各 draft heads 以 exponential decay 聚合；最终 checkpoint 进入
  runtime 的 chain draft → target verification → sequential acceptance。Training objective 只改变 proposal
  distribution，不改变 exact verification 对 target distribution 的语义责任。
- **Evaluation Contract:** 六个 targets：Llama-3.1-8B、Llama-3.3-70B、gpt-oss-20B/120B、
  Qwen3-235B-A22B 与 DeepSeek-V3-0324 685B；EAGLE-3、MEDUSA、MLP 与 native MTP 四类 drafter。
  660K Infinity-Instruct prompts、target-generated responses、8K train sequence，batch 64，10 epochs
  （DeepSeek-MTP 一 epoch），temperature 1。evaluation 使用 patched vLLM v0.11.0、完整 MT-Bench/
  HumanEval/GSM8K、T=0/1、chain sampling；EAGLE/MTP `K=7`，MEDUSA/MLP `K=6`。主要指标 `τ`
  是每 speculation round expected generated tokens；paper appendix 报 tokens/s，但没有披露可归一化到
  本书的完整硬件、并发与 SLO contract。
- **What the Evidence Proves / Does Not Prove:** 在该 train/eval matrix 中，两类 LK objective 相对作者
  KL baseline 普遍提高 acceptance，低-capacity drafter 与 stochastic sampling 的相对收益更明显；这支持
  “训练 proxy 应与 runtime acceptance 对齐”。它不证明 acceptance 增量等于 end-to-end goodput 增量，
  也未验证 tree drafting、block verification、continuous batching 与 production scheduler；`η=3`、固定
  head decay 和 generated corpus diversity/epoch trade-off 均未充分 ablate。
- **Trade-offs / Old Branches:** direct objective 改善 local optimum alignment，但增加 scheduler/aggregation
  hyperparameters，低 `α` 的 gradient amplification 需要数值稳定性与 clipping；训练更贴近某个 target/
  sampling distribution，也增加 target revision、domain、temperature 与 runtime coupling。KL 在 early
  training、general distribution matching、充分 capacity 或需要更平滑 optimization 时仍是合理分支；hybrid
  本身就是保留旧分支的演进，而不是否定 KL。
- **Evolution / ROADMAP / Existing Coverage:** `Direct Evolution` within drafter training；Ch44 是主 owner
  candidate，Ch29 只承接 optimization-objective 边界。Ch44 已完整解释 exact acceptance、drafter artifact
  identity、verify-length/scheduler cost 与 acceptance≠speedup，但尚未解释“KL 与 acceptance 共享全局最优，
  却在受限 capacity 的可达点失配”以及 direct-overlap loss 的 gradient trade-off。Books Integration 前需
  重读 Ch43～45 并确认只 refine Ch44。
- **Integration Decision:** `Full Review Complete — Books Candidate / Objective-to-Runtime Acceptance
  Alignment`，保持 `Experimental`；不写入作者 8～10% headline，除非同时保留 model/drafter/domain/
  temperature/runtime 条件。
- **Open Questions:** v1→v2 对公式、表格和结论具体改了什么？tree/block verification、mixed traffic 与
  online target drift 下，acceptance-aligned loss 是否仍优于 KL？`-log α` 在极低 overlap 时如何避免 exploding
  gradient，同时不失去其 early-stage signal？

### Cognitive Models and AI Algorithms Provide Templates for Designing Language Agents

- **Candidate / Week / Score:** arXiv:2602.22523 / 2026-W09 / 18/30；first-public 2026-02-26，HF
  2026-03-02 才进入 Daily discovery。
- **Verification Scope:** metadata、abstract、position-paper framing 与 agent-template definition 已核验；
  论文主张从 cognitive models/AI algorithms 抽取角色与组合模板，但不提供新的 production runtime、
  controlled system experiment 或可执行 artifact 证据。
- **Decision / Reason:** `Source/Date Verified — Weekly Only / Position Paper`。它可作为 Ch78 设计类比，
  但本书已经用 task decomposability、state ownership、communication tax、authority 与 failure isolation
  判断 Multi-Agent topology；不因 survey taxonomy 新增 Books 机制。若后续出现 controlled evidence，
  再升级为 Full Source Review。

### SGLang v0.5.9

- **Candidate / Week / Score:** SGLang v0.5.9 / 2026-W09 / 28/30；
  `Source Family ID: adapter-readiness-cross-stream-lifetime-2026`。
- **Source Type / Event Date / Revision:** official stable release，2026-02-24；联读 release notes、LoRA
  overlap PR #15512、FlashInfer All-to-All dispatcher PR #14668 与 Spec V2 correctness fix PR #18958。
  三项 PR 分别在 01-19、01-24、02-19 merge；W09 事件是 02-24 stable release availability，不能把
  PR merge date 或后续文档日期改写成 event date。
- **Access and Full-read Coverage:** Verified；检查 release highlights、LoRA loader/scheduler/memory-pool
  diff、dispatcher backend/format/workspace contract、Spec V2 failure reproduction 与 `record_stream`
  lifetime fix。NSA kernel 的 3～5× headline 未取得完整、条件对齐的 PR benchmark，只保留为版本事实。
- **Original Problem / Why Previous Design Was Reasonable:** 同步 LoRA H2D load 在 request admission 前
  完成，因果关系清楚、不会让未就绪 adapter 进入 batch，也简化 slot eviction；但当 adapter 大、切换
  频繁时，copy latency 会直接进入 TTFT，甚至阻塞其他 adapter 的调度。旧设计在 adapter 小、切换少、
  host/device memory 紧张或更重视确定性时仍合理。
- **Changed Constraint / Mechanism:** v0.5.9 的 overlap path 把 CPU weights 放入 pinned memory，在独立
  CUDA load stream 上执行 non-blocking H2D，并为每个 adapter 保存
  `NOT_LOADED → LOADING → LOADED` event state。scheduler 用 `event.query()` 判断 readiness；需要消费时，
  current stream 显式 `wait_event`。memory-pool capacity 同时计算 running adapters 与 in-flight load，
  loading 或无 slot 的 request 被 defer，而不是假装 adapter 已可用。overlap path 一次启动一个 adapter，
  不是无界并发搬运。
- **State Ownership / Control and Data Flow:** CPU pinned copy 是 source；load stream/event 拥有传输进度；
  LoRA memory pool 拥有 device slot；scheduler 拥有 admission/defer；model stream 只有在 event dependency
  成立后才消费 weights。该链路把 adapter 从静态 asset 变成 scheduler-visible state machine：
  `request → adapter identity → slot reservation → async copy → ready event → batch admission/use`。
- **Secondary Mechanism / Implementation Boundary:** FlashInfer All-to-All 是 token dispatcher 的新增
  pluggable backend，显式定义 dispatch/combine format、workspace 与 per-rank token upper bound；它与
  `none`、DeepEP、Mooncake、Ascend FuseEP 是 backend branch，不证明任何一个 backend 普遍替代另一个。
  Spec V2 PR #18958 还证明逻辑依赖不足以保证 CUDA correctness：default stream 分配的
  `future_indices.indices` 在 forward stream 读取前失去 Python reference，修复必须用 `record_stream`
  延长 allocator-visible lifetime。
- **Evaluation Contract:** release 宣称大 adapter workload 上 TTFT 下降约 78%、TPOT 下降 34.88%，但
  #15512 diff 未披露足以复核的 hardware、model、adapter size、request concurrency 与 SLO，故只记录
  vendor claim，不进入长期性能结论。Spec V2 bug 在 Llama-3-8B/H200 和 disaggregated reproduction 中被
  确认；这证明特定 lifetime bug 与修复路径，不证明所有 speculative/disaggregated 配置均正确。
- **What the Evidence Proves / Does Not Prove:** code diff 能证明 readiness event、slot accounting、
  scheduler defer 与 cross-stream lifetime 是实现 contract；不能证明 headline speedup 可迁移到小 adapter、
  低切换率、不同 interconnect 或其他 engine，也不能从 release notes 推断 NSA kernel 的普遍质量边界。
- **Trade-offs / New Failure Modes:** pinned host memory、额外 stream/event、slot reservation 和更多
  scheduler branches 换取 overlap；新增 cancellation 后 event/slot 回收、eviction 与 in-flight use 竞争、
  head-of-line/fairness、load failure fallback、stream lifetime 与组合测试矩阵。同步 load 保留为简单可靠分支。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution` of dynamic adapter serving；Ch46 是
  generic serving lifecycle owner，Ch47 记录 SGLang implementation handoff，Ch52 只接调度公平性边界。
  已读 Ch46～47 与 Ch52；Ch46 已讨论 LoRA identity/compatibility，但未把 readiness、slot reservation 与
  stream lifetime 纳入 request-state contract，因此存在真实机制缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Adapter-Readiness and Cross-Stream
  Lifetime Contract`；本轮只修 Weekly，待统一 Books Integration 时 refine Ch46，并在 Ch47 短交接。
- **Open Questions:** cancellation、timeout、load failure 和 eviction 如何原子地回收 event/slot？不同
  adapter size 与 arrival distribution 下，defer policy 是否产生 starvation？release headline 能否在固定
  hardware、model、adapter size、concurrency 与 SLO 下独立复现？

### vLLM v0.16.0

- **Candidate / Week / Score:** vLLM v0.16.0 / 2026-W09 / 29/30；
  `Source Family ID: async-pp-request-state-handoff-2026`。
- **Source Type / Event Date / Revision:** official stable release，2026-02-25；release branch cut 02-08，
  累积 440 commits / 203 contributors。联读 async scheduling + Pipeline Parallel PR #32618、native RLHF
  weight-sync RFC #31848、pause/resume RFC #32103、NIXL connector PR #33339，以及 release 后的
  chunked-PP fix #38726 与 multi-node data-leak report #38903。后两者只作为机制的后续 failure evidence，
  不倒填成 W09 事件。
- **Access and Full-read Coverage:** Verified；检查 release notes、#32618 discussion/files、benchmark
  contract、request/input-batch mapping、PP token broadcast，以及上述 RFC/connector/failure evidence。
- **Original Problem / Why Previous Design Was Reasonable:** 同步 scheduler 等待 sampled token 回到 CPU，
  再更新 request state 并准备下一步；在 PP 中只有 last rank 产生 token，因此这条 round-trip 同时充当
  stage 间顺序屏障。它牺牲 overlap，却让 token ownership、request row 与 failure recovery 更直观。
  async scheduling 移除 CPU wait 后，原 `new_token_ids` feedback path 不再适用于 PP，非 last stage 可能
  缺少下一步 token 或把 in-flight row 与错误 request 对齐。
- **Changed Constraint / Mechanism:** #32618 让 last PP stage 在 GPU 上广播 sampled token IDs 到所有
  stages；async PP 的 scheduler output 不携带常规 token payload，各 stage 的 cached input batch 用上一
  batch row mapping 和 placeholder 跟踪 in-flight progress，在 CPU output round-trip 完成前准备下一步：
  `last-stage sample → ordered PP broadcast → per-stage row mapping → placeholder/in-flight state → next step`。
  placeholder 不是 committed content；正确性依赖各 stage 对 request identity、row ordering 与 token commit
  建立同一 happens-before relation。
- **State Ownership / Control and Data Flow:** Engine Core/scheduler 拥有 request lifecycle 与 token budget；
  last PP rank 是本步 sampled token 的 producer；PP group transport 拥有 ordered broadcast；每个 stage 的
  input batch 拥有本地 row/cache view。任何 retry、chunking、abort 或 rank failure都必须防止 placeholder
  被当成真实 token、旧 row 被新 request 复用或不同 request context 交叉。
- **Evaluation Contract:** PR 给出 `Qwen/Qwen3-30B-A3B-Thinking-2507-FP8`、PP=4、
  `max-num-seqs=128`、128 prompts、random input length 2、output length 512、16 warmups；报告
  11.72 req/s 与 mean TPOT 21.01 ms，对 main 的 8.95 req/s / 27.70 ms，作者换算约 30.8% throughput
  与 31.8% TPOT 改善，并附 GSM8K exact-match check。硬件、跨节点 topology 与生产 SLO 未披露，
  因而结果只绑定该 PR workload，不是 PP 通用收益。
- **Related Release Families:** native weight sync RFC 将 trainer rank 0 与 vLLM workers 通过 native NCCL
  联接，以增量 receive/load 降低峰值内存，并抽象 `WeightTransferEngine`；versioning、dynamic group、
  quantization 仍是 open design。pause/resume RFC 的 `abort/finish/keep` 把请求处理策略显式化，`keep`
  保留 scheduler state 以支持快速 weight update。NIXL connector v2 增加 cross-layer KV layout。这些是
  v0.16.0 的并行演进分支，不与 async PP 合并成单一性能结论。
- **What the Evidence Proves / Does Not Prove:** release/PR 证明 async scheduling 与 PP 的具体 token
  handoff 和一组受限 benchmark；不能证明 multi-node、chunked prefill、取消/重试与所有 model topology
  已满足 isolation。后续 #38726 修复 async scheduling 下 chunked PP 卡住；#38903 在 2 nodes × 8 H100、
  PP=2/TP=8、并发用户条件报告 cross-request context contamination，关闭 async scheduling 后消失，但
  issue 尚未隔离唯一 root cause，不能写成已证实由 #32618 单点导致。
- **Trade-offs / New Failure Modes / Old Branches:** overlap 降低 CPU scheduling bubble，但把原隐式屏障
  拆成 distributed ownership contract；新增 row/token ordering、broadcast failure、placeholder rollback、
  cancellation、chunk boundary、cross-request isolation 与 replay/idempotency 风险。同步 scheduler 在 CPU
  开销较小、跨节点正确性优先或 recovery 语义尚未完备时仍是合理分支。
- **Evolution / ROADMAP / Adjacent Chapters:** `Direct Evolution` of serving request-state scheduling；Ch46
  是 owner，Ch52 接 admission/fairness，Ch34 只作为训练侧 Pipeline Parallel 语义边界。已读 Ch34、
  Ch46～48 与 Ch52；现有 Ch46 解释 async scheduling 的 overlap，但尚未明确“移除控制面 round-trip
  等于必须重建 token ownership、stage ordering 与 rollback barrier”，因此存在长期机制缺口。
- **Integration Decision:** `Full Review Complete — Books Candidate / Async-PP Request-State Handoff
  Contract`；本轮不修改 Books，后续 refine Ch46，并以短 handoff 连接 Ch34/52。
- **Open Questions:** #38903 的最小 root cause 是否是 request-row reuse、broadcast ordering、prefix cache
  interaction 或其他 multi-node path？abort/retry 后如何证明所有 stage 对 committed token 和 placeholder
  达成一致？权重 version、paused requests 与 KV/cache identity 如何共同进入 rollout serving contract？

### Qwen3-Coder-Next Technical Report

- **Candidate / Week / Score:** Qwen3-Coder-Next Technical Report / 2026-W09 / 27/30；
  `Source Family ID: executable-agentic-coding-training-qwen3-coder-next`。
- **Source Type / Date / Revision / Access:** arXiv:2603.00729 v1，首次公开 2026-02-28，当前无后续
  arXiv revision；联读 v1 HTML/PDF、Qwen 官方 Hugging Face model card 与 Qwen3-Coder repository。
  已覆盖 Metadata、Introduction、task synthesis、MegaFlow infrastructure、全部 mid-training/SFT/
  expert-training sections、evaluation setup/results、Limitations、task statistics、tool-template checklist、
  Best-Fit Packing 实现与 ablation。模型权重与 deployment entry 可访问，但训练数据、内部模型、
  MegaFlow deployment manifest、paper-run checkpoint 与完整训练代码未公开。
- **Original Problem / Why Previous Designs Were Reasonable:** 静态代码 corpus、单文件 completion 与
  一次性 SFT 能低成本学习 syntax、API pattern 和局部 edit，在任务短、tool schema 固定、compiler/test
  环境不可规模化时仍合理。但 coding Agent 的真实 failure surface 来自 repository state、长时工具交互、
  executable feedback、错误恢复和 scaffold-specific protocol；只增加模型参数或静态 code tokens，不能
  自动提供这些状态转移的监督。
- **Changed Constraint / Principle / Mechanism:** 报告先从 issue-related PR 构造 buggy/fixed/test 三元组，
  由 environment-building agent 生成 Docker environment 和 verifier，再以自动 detector 与 QA agent 排除
  non-functional verifier、ambiguous task 和 test mismatch；另一条分支在已有 containerized repositories 中
  注入可由现有 tests 触发且可由 revert 修复的 controlled bugs，并隐藏触发 tests。由此形成约 80 万条、
  九种以上语言的 executable tasks。训练随后按 `continued pretraining/mid-training → SFT → domain expert
  RL → expert distillation` 分阶段推进，而不是把所有信号混成一次 fine-tuning。
- **State Ownership / Control and Data Flow:** task manifest 拥有 repository/commit、bug/fix/test、container
  digest 与 verifier identity；trajectory 拥有 scaffold/tool-template、teacher/policy checkpoint、termination
  与 environment result；MegaFlow 把 rollout、独立 evaluation container 与 post-processing 表达为 Argo
  workflow，并在 rollout pod 内 colocate agent 与 execution environment。训练侧再把 corpus snapshot、
  decontamination、context length、packing/mask、SFT/RL split、expert checkpoint 与 distillation teacher
  lineage 绑定到 stage。若只保存最终 response 或 unified checkpoint，就无法解释收益来自 task、scaffold、
  verifier、reward 还是 expert composition。
- **Implementation Details:** mid-training 主要使用 natural data，辅以较少 synthetic data；repository-level
  context 扩到 262,144 tokens，作者报告约 600B repository tokens，并使用多种 repository serialization。
  Multi-turn trajectories 来自 SWE-agent、Mini-SWE-agent、OpenHands、Claude Code、Qwen Code 与 Terminus，
  以 Qwen3-Coder-480B-A35B-Instruct 为 teacher，并过滤失败、缺 termination 与 malformed tool calls。
  Best-Fit Packing 保留 document/trajectory boundary；超长文档先 split，重复片段可 loss-mask。SFT 再用
  executable user-simulator 过滤 response；Software Engineering RL 将 final outcome、unfinished trajectory
  与 invalid tool-call token penalty 组合，并增加 network/URL heuristic，阻断 agent 重新获取 ground-truth
  commit 的 reward hacking。最后将 Web、UX、single-turn QA 与 SWE experts 蒸馏回单一部署模型。
- **Evaluation Contract:** 模型为 80B total / 3B active 的 hybrid attention + MoE，官方 model card 披露
  48 layers、512 experts、每 token 10 个 activated experts 加 1 个 shared expert，以及 native 262,144
  context。Agent evaluation 覆盖 SWE-Bench Verified、Multilingual、Pro 与 TerminalBench 2.0；SWE tests
  对各 baseline/scaffold 重新运行、移除 remotes/branches/tags，并设最多 300 turns。报告还覆盖 Aider、
  LiveCodeBench、CodeForces、HumanEval/MBPP、MMLU/GPQA/AIME 等。正文没有给出评估 hardware、precision、
  batch、concurrency、token/cost/latency 或 SLO；因此表格只支持该 harness 下的 model-quality 比较，不支持
  “3B active 即代表生产成本/吞吐”的结论。
- **Ablations / Sensitivity / Evidence Boundary:** 报告显示同 scaffold 的 agentic mid-training 随 token
  增加而改善，但 cross-scaffold transfer 有限且不对称；这支持 **scaffold 是训练分布的一部分**，不证明
  多模板即可获得任意 runtime portability。Web rewrite、tool-template diversity、RL task diversity 与 BFP
  分别有作者 ablation，但未形成覆盖全部 training stages 的 factorial design。BFP Appendix 使用 agentless
  SWE-bench、模型/ground-truth location、patch similarity 与 empty-patch ratio，不是完整 Agent execution，
  不能外推成 long-horizon outcome。作者比较结果与 reward-hacking blocker 均未提供独立 reproduction。
- **What the Evidence Proves / Does Not Prove:** primary evidence证明该模型公开了一个把 executable task、
  environment、trajectory protocol、stage-specific objective 与 expert consolidation 连起来的训练 recipe，
  并在作者限定 benchmark/scaffold 中取得与 active footprint 相称的结果。它不证明 80B/3B architecture、
  80 万任务、262K context、某一数据比例或 expert distillation 是所有 coding Agent 的通用最优方案；也不
  证明 heuristic blocker 覆盖所有 exfiltration/reward-hacking path，或数学 benchmark 增益由 code reasoning
  唯一因果产生。
- **Trade-offs / New Failure Modes / Old Branches:** executable task synthesis 提高 reward density，却新增
  container drift、test incompleteness、verifier overfitting、ground-truth leakage、network exfiltration 与
  expensive failed rollout；多 scaffold 增加 portability coverage，也扩大 prompt/tool schema、trajectory
  identity 与 regression matrix。分 expert 后再 distill 避免在线 expert routing，但可能产生 capability
  interference、teacher bias 与无法定位的 regression。静态 corpus、单 scaffold SFT、training-free Agent
  search、compiler/test feedback 与在线 multi-model orchestration，在数据稀缺、runtime 固定、任务低频或
  需要独立 expert rollback 时仍成立。
- **Evolution Relationship:** `Direct Evolution`：static/file-level code learning → repository/PR data →
  executable task + environment → multi-scaffold trajectories → environment-rewarded expert training →
  consolidated deployment model。与 Ch23 数据/verifier、Ch21 MoE、Ch29 RL reward、Ch62 evaluation 和
  Ch77 workflow 分别是 `Layering / Dependency`，不能把这些 owner 合并成一个“coding model feature”。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage:** 已读 Ch21、Ch23～26、Ch29、Ch62、
  Ch77。Ch23 已有 executable specification 与 verifier lineage；Ch29 已有 measurement-as-reward 和
  reward-hacking 边界；Ch62/77 已有 artifact、sandbox 与 workflow contract。Ch25 已解释 demonstration、
  distillation 与 catastrophic forgetting，却尚未把 **scaffold identity、stage-specific expert ownership 与
  consolidation regression** 组织成同一 SFT/post-training 演进链，因此主 owner 保留 Ch25；Ch23/29/77
  只作短 handoff。
- **Integration Decision:** `Full Review Complete — Books Candidate / Scaffold-Bound Staged Specialization
  and Expert-Consolidation Contract`。候选级 Evidence Gate 已通过；Books Integration 仍需与 W09 其他
  Ch25/29 candidates 一起去重，正文只吸收长期机制，不写模型排名或厂商 recipe 为默认配方。
- **Open Questions:** 如何用 held-out scaffold/schema 与 unseen tool protocol 区分 format memorization 和
  capability transfer？如何对 expert distillation 做 per-domain retention、negative transfer 与 rollback？
  verifier/test coverage、network policy 与 ground-truth isolation 能否由独立 red-team/reproduction 核验？
  在 matched training/serving compute 下，active-parameter architecture 与 staged recipe 的贡献如何拆分？

### SkillNet

- **Candidate / Week / Score:** SkillNet / 2026-W09 / 25/30；
  `Source Family ID: agent-skill-asset-lifecycle-and-relation-graph`。
- **Source Type / Date / Revision / Access:** arXiv:2603.04448 v1，首次公开 2026-02-26，当前无后续
  arXiv revision；联读 v1 HTML/PDF、官方 SkillNet repository、`skillnet-ai` CLI/SDK 文档和公开 API/
  integration 说明。已覆盖 Agent Skills 定义、SkillNet framework、creation/evaluation/analysis、全部定量
  evaluation、applications、Related Work、Discussion、Limitations 与 repository command surface。官方站点
  本轮不可稳定访问，但 repository 与 API 文档可核验；current repository 在 2026-07 已扩展索引规模，不能
  将 current count 倒写成 2 月论文事件。
- **Original Problem / Why Previous Designs Were Reasonable:** Prompt、workflow 与成功 trajectory 可快速
  在单个 Agent 内复用，不需要新的 registry/ontology；静态 package directory 也便于人工审核。在 skill
  数量小、producer/consumer 同域、依赖固定且操作风险低时，这些旧方案仍合理。规模扩大后，纯目录不能回答
  哪个 skill 可替代、组合或依赖另一个 skill，也缺少统一 admission、evaluation、supersession 与 retrieval
  contract，Agent 会重复构造近似能力或把不可信 package 直接带入执行环境。
- **Changed Constraint / Principle / Mechanism:** SkillNet 把 skill 定义为包含 `SKILL.md`、metadata、
  instructions 及可选 scripts/templates/resources 的可移植 package；读取路径是 metadata discovery → full
  instruction activation → optional execution。系统从 trajectory/conversation、GitHub repository、PDF/PPT/
  Word 与自然语言 prompt 自动生成 package，再以 taxonomy、skill entity、package 三层 ontology 连接。
  typed edges 包含 `similar_to`、`belong_to`、`compose_with` 与 `depend_on`，由 embedding candidate generation、
  dependency extraction、execution-trace alignment 与 LLM inference 构造 relation graph。
- **State Ownership / Control and Data Flow:** source artifact/trajectory 拥有 provenance；creation model/
  prompt/schema 拥有 derived package；registry 拥有 immutable skill identity、category、version 与 publication
  state；evaluator 拥有 rubric/model/sandbox result；relation builder 拥有 embedding/model/threshold、edge type
  与 evidence；runtime 只应将已解析版本的 skill 安装进 workspace，并由 workflow 决定 activation、authority
  与 side effects。论文的自动构造与 current repository command 并未定义完整 immutable version、signature、
  revocation propagation 或 dependency lock，因此 production lifecycle 不能由“可下载”反推为安全。
- **Implementation Details:** 论文使用 MD5 检查 `SKILL.md` 与目录结构做重复检测，这只能覆盖 exact
  duplicates，不能证明 semantic/operational near-duplicate 已处理。质量维度包括 Safety、Completeness、
  Executability、Maintainability 与 Cost-awareness；主要由文中称为 `GPT-5o-mini` 的 LLM evaluator 打分，
  code/tool skills 辅以 sandbox execution，输出 Good/Average/Poor。该 model identity 在公开资料中不清楚，
  必须保留为 evaluator provenance ambiguity。Current SDK 提供 search/download/create/evaluate/analyze，
  orchestration 只支持特定 scene，并依赖 Claude Agent SDK-compatible gateway；它不是通用 autonomous
  skill-to-agent compiler。
- **Evaluation Contract:** 自动 evaluator 用随机 200 skills 和三名 CS PhD blind review 校验，论文报告
  五个维度 MAE < 0.03、QWK 近 1.000，但没有给出 confidence intervals、class balance、原始 annotations、
  adjudication procedure 或跨 domain/risk slice。Agent evaluation 在 ALFWorld、WebShop、ScienceWorld 的
  seen/unseen split 上，以 ETO expert trajectories 合成 benchmark-specific skill collections，比较 ReAct、
  Expel 与 +SkillNet，backbones 为 DeepSeek V3.2、Gemini 2.5 Pro、o4-mini，指标是 average reward 与 steps。
  论文称 experience 与 test split 不重叠，但未披露 inference hardware、token/tool budget、latency/cost、
  concurrency、random seeds、方差/置信区间或完整 contamination audit。
- **What the Evidence Proves / Does Not Prove:** 论文与 artifact 证明 search、package creation、multi-axis
  evaluation 和 typed relation analysis 可以形成一个可运行的 skill lifecycle prototype；限定 benchmark 下，
  task-specific skills 与 Agent loop 联用取得较高 reward、较少 steps。它不证明 15 万级 curated repository
  全部经过同等强度的 executable review，不证明自动 evaluator 在安全关键领域可靠，不证明 relation edges
  等于可执行 composition，也不证明从 expert trajectories 生成的 benchmark-specific skills 能跨 domain、
  cross-version 或真实生产 workload 泛化。
- **Limitations / Threats / New Failure Modes:** 作者明确承认私有/tacit skill coverage 不完整、自构造质量
  不能保证、大量 skills 缺少严格系统评估、poisoned/adversarial skills 无法完全缓解，且 natural-language
  requirement → fully instantiated agent 的端到端 pipeline 尚未建立。系统还新增 dependency confusion、
  stale relation、LLM-generated edge hallucination、unsafe transitive composition、package revocation lag、
  evaluator monoculture、prompt injection 与 skill/tool authority escalation。人工 curated directory、固定
  workflow、单租户私有 registry 和不执行代码的 textual playbook 在高风险、低规模或强审计场景仍成立。
- **Evolution Relationship:** `Direct Evolution`：ad-hoc prompt/trajectory reuse → packaged skill → searchable
  registry → multi-axis admission → typed relation graph → runtime selection/composition。Memory→skill 是
  `Principle Reuse`，skill→workflow 是 `Layering / Dependency`；relation graph 不拥有 Workflow state，
  marketplace 也不拥有 tool authorization。
- **ROADMAP / Target and Adjacent Chapters Read / Existing Coverage:** 已读 Ch73、Ch77～80。Ch73 已覆盖
  trajectory→derived memory 的 provenance/consolidation；Ch77 拥有 authoritative workflow；Ch78 拥有
  responsibility/communication；Ch79 拥有 MCP connection。Ch80 已有 Skill registry identity、dependency、
  evaluation、supersession/revocation 与多 trace audit，因此不是全新对象；真实缺口是 **关系边的 evidence/
  version、composition admission 与 transitive risk** 尚未被组织为 registry lifecycle。主 owner 为 Ch80。
- **Integration Decision:** `Full Review Complete — Books Candidate / Typed Skill-Relation and Composition-
  Admission Contract`，`Status: Experimental`。后续优先 refine Ch80 现有 Skill 小节，不新增孤立文件；若
  relationship evidence、version 与 runtime authorization 不能形成增量，只保留 `No Change — Already Covered`。
- **Open Questions:** `similar_to/compose_with/depend_on` 如何由可验证 evidence 而非单次 LLM judgment
  建立，并随版本升级失效？组合前如何计算 transitive permission、dependency lock 与 side-effect risk？
  近乎完美的人机一致性在 class-balanced、adversarial、domain-specific 与 executable-only slices 上是否
  可复现？poisoned skill 的 quarantine、revocation、downstream run invalidation 与 rollback 谁负责？

## Evidence Level

- **Full Source Review Complete (58/62):** Persona Selection Model、OpenAI malicious-use report、
  Data Engineering for Terminal Capabilities、Untied Ulysses、DualPath、veScale-FSDP、
  General Agent Evaluation、TTT with KV Binding、Agents of Chaos、ARLArena、SkillOrchestra、
  GUI-Libra、Revisiting Text Ranking in Deep Research、SWE-Protégé、EMPO²、AgentDropoutV2、
  Search More, Think Less、ISO-Bench、TAPE、Aletheia / FirstProof、Multi-Vector Index Compression、
  DPE、Reflective Test-Time Planning、Adaptive Text Anonymization、OmniGAIA、MobilityBench、DSDR、
  Implicit Intelligence、PyVision-RL、Overconfident Errors Need Stronger Correction、Trinity of Consistency、
  SGLang v0.5.9、vLLM v0.16.0、CUDA Agent、LK Losses、dLLM、STATIC、SWE-rebench V2、Memory Caching、
  Tool-R0、LongVideo-R1、Reinforcement-aware Knowledge Distillation、CiteAudit、Recovered in Translation、
  SenCache、CL4SE、Online World Modeling for IRLfO / MPAIL2、QEDBENCH、ProbCOPA、Algorithmic Cores、
  Truncated Step-Level Sampling / SLATE、LLMServingSim 2.0、AMA-Bench、AgentVista、CIRCLE、IMMACULATE、
  Qwen3-Coder-Next Technical Report、SkillNet。
- **Low-score source/date/rejection check complete (4/62):** Cognitive Models as Agent Templates、
  BBQ-to-Image、Simulating Social Media Users / CCP、SGDC；加上已完成 Full Review 的低分 Trinity，
  当前低分候选 5/5 已核验。
- **Candidate Evidence Gate:** `Passed — 62/62`。58 项 `20+`/升级候选拥有非模板化 Full Source Review，
  4 项低分候选拥有来源、日期、评分和拒绝理由核验；无 `Audit Pending`。Google Scholar/OpenAlex
  的不可审计历史窗口继续标为 Discovery Limitation，不再被错误写成候选 evidence 未完成，也不据此
  声称 discovery recall 绝对完备。
- **Official observation:** OpenAI report 能证明报告中的 workflow-style abuse cases 被平台观察和处置，
  不能估计全行业 prevalence；Anthropic persona model 是解释性/经验性研究，不是 runtime specification。
- **Paper evidence:** 所有已完成的学术 Full Review 结论只绑定各自公开 method、artifact 和 evaluation contract。
  作者 benchmark 不外推为默认架构选择。
- **Cross-year exclusions (3):** Replicate-and-Quantize 与 MINAR 分别于 2024-09-22、2025-09-23 在
  OpenReview first-public；CUPID 已由作者机构于 2025-12-16 公开核心问题、方法与实验对象。三项的
  2026 arXiv 版本只作为 source-family revision/full-manuscript evidence，不计入 W09。
- **Repository / implementation evidence:** DualPath exact internal stack 未公开；terminal data 只承诺
  release “most” synthetic datasets；veScale repository 明确只公开内部系统的一小部分；TTT project
  page 未提供本轮可检查的独立 reproduction package；Untied Ulysses、General Agent Evaluation 和
  TTT 当前 revision 均晚于事件周；GUI-Libra 与 Deep Research ranking 的 repository 未固定
  paper-run artifact；SWE-Protégé 与 SMTL 未定位到作者公开代码；EMPO²/AgentDropoutV2 current code
  均未绑定 event-date paper run；ISO-Bench/TAPE 仓库未以不可变 manifest 锁定全部 paper run，Aletheia
  只公开 proof artifacts、不公开 runtime；Multi-Vector/DPE/Reflective TTP 的 current repositories 也未以
  immutable paper-run manifest 绑定全部结果；Adaptive Anonymization、OmniGAIA 与 MobilityBench 的 current
  repositories 同样未以不可变 manifest 锁定 event-date paper run；Implicit Intelligence 未公开本轮可独立
  replay 的完整 dataset/harness，PyVision-RL current repo 也未固定 event-date commit；ACE 没有独立
  paper-run artifact；CoW-Bench 公开 evaluator 使用 `gpt-4.1`，且 paper/public dataset 数量不一致。全部
  保留边界。SGLang LoRA headline 缺完整 benchmark contract；vLLM async-PP benchmark 未披露硬件，
  release 后 correctness reports 只能证明风险存在，不能把未隔离 issue 当成唯一根因证明。Tool-R0
  repository 与 LongVideo-R1 repository 都是当前可变 artifact，未用 immutable manifest 锁定全部 paper-run
  环境；Tool-R0 W&B dashboard 本轮也无法独立抓取，因此均不提升为可复现结论。RLAD 未提供公开 code，
  且 v3 主文存在 `α` 端点解释与公式/Appendix 不一致；CiteAudit current repository 又未完整呈现论文
  five-agent/Mem0 pipeline，二者均保留 artifact/revision 边界。Recovered in Translation 的 current
  repository/Hub artifact 未锁定 paper-run provider outputs；SenCache current repository 也未以 immutable
  manifest 锁定三模型实验，并且 paper 的 local sensitivity policy 仍含 model-specific thresholds。CL4SE
  current repository 仅有少量提交，HF heterogeneous splits 当前又无法在统一 viewer 中完成 schema cast；
  MPAIL2 项目页声称提供 code，但本轮未定位到可独立审查并锁定 paper run 的 public repository/commit；
  Algorithmic Cores 当前 repository 没有 release/tag 或 immutable paper-run manifest，v2 才增加的模型范围
  也不得倒写为 v1 事件事实。AgentVista current repository 同样没有 paper-run release/tag，并且论文的
  `temperature=0.6` 与 current quick-start 实际继承的 `infer.py` default `0.0` 不一致；公开 harness 可检查，
  但默认命令不能作为论文表格的直接 reproduction contract。Qwen3-Coder-Next 的权重/model card 可访问，
  但 MegaFlow、训练数据、内部 teacher/judge、paper-run checkpoint 和完整训练实现未公开；SkillNet current
  repository 已在事件后扩展，论文中的 `GPT-5o-mini` evaluator identity、200-skill annotations 与完整
  paper-run manifests 又未公开，均不提升为独立可复现结论。
- **Reopened discovery boundary:** arXiv 常规 announcement 每周五天，02-28/03-01 没有独立 paper
  announcement batch；HF 03-02～03-06 持续延迟呈现 02-24～02-27 papers，证明仅扫描同周或只向后
  两天会漏掉 post-week curation lag。03-04/05/06 页面逐项检查已完成：恢复 10 项 W09 候选，另将
  Spilled Energy 与 AgentConductor 按 v1 date 排除至 W08；交叉索引另恢复 IMMACULATE、
  LLMServingSim 2.0、AMA-Bench、Replicate-and-Quantize 与 MINAR，证明 HF spillover 仍不是完备集合。
  候选级全文/低分审计与 DBLP 恢复项已全部闭合；Google Scholar/OpenAlex 的历史窗口没有获得可审计
  结果，因此保留 Discovery Limitation，不用“查询失败”冒充“未发现遗漏”。该限制不撤销已审 62 项的
  Candidate Evidence Gate，但禁止将本周写成 discovery recall 的数学完备性证明。

## Cross-Week Deduplication

- Persona Selection 与 W04 Assistant Axis：`Layering / Dependency`；只有作者明确引用并改变旧机制
  才升级为 `Direct Evolution`。
- PETS (arXiv:2602.16745)、Anatomy of Agentic Memory (2602.19320)、K-Search (2602.19128)、
  DREAM (2602.18940)、Benchmark Test-Time Scaling (2602.18998)、RankEvolve (2602.16932)、
  AI Gamestore (2602.17594) 的 v1 均早于 2026-02-23，保留在 W08 或更早周，不因 02-23 后
  discovery 页面再次出现而重复记入 W09。
- Query-focused reranking (2602.12192)、LongCLI (2602.14337)、Step 3.5 Flash (2602.10604)、
  UI-Venus (2602.09082)、Code2World (2602.09856) 同理归入其首次公开周。
- Aletheia 与 W08 OpenAI FirstProof 属于同一 proof-artifact/evaluation family，但来源与技术对象不同；
  已核验为 `Layering / Dependency`，不把二者合并成一个事件，也不交叉外推 solved count。
- TTT with KV Binding、Untied Ulysses、veScale-FSDP 分别触及 attention state、Context Parallel 与
  state sharding，不因都讨论 memory 就视为直接替代关系。
- HF 03-02 页面中的 DUET-VLM（arXiv:2602.18846）v1 为 02-21，归 W08；LongVideo-R1、Tool-R0、
  Recovered in Translation 等按各自 v1 date 回归 W09。discovery page date 不参与归周。
- HF 03-04 页面中的 Spilled Energy（arXiv:2602.18671，v1 02-21）与 AgentConductor
  （arXiv:2602.17100，v1 02-19）同样归 W08；其 W09 revision 或 HF discovery date 不构成新事件。
- CUPID 的完整 manuscript 于 2026-02-25 进入 arXiv，但作者机构已在 2025-12-16 公开标题、核心机制与
  实验对象，故作为同一 source family 的 manuscript revision 归回 2025-W51，不计 W09 新事件。

## Knowledge Tree Position

本周有效候选分布在以下节点；Source Review 的 owner 已定位，最终是否写入正文仍需 Books Gate 逐项去重：

```text
Model / Training:
  Ch14/19/22 attention and long context
  Ch23/25 data and SFT
  Ch29 RL / RLVR
  Ch32/35/36 distributed training and sharding

Inference:
  Ch46/47 request lifecycle and serving-engine implementation
  Ch48/50/51/52 distributed runtime, memory, PD and scheduling

Evaluation / Security:
  Ch62/63/65/68/69

Agent:
  Ch71～80, especially retrieval, memory, planning, workflow and multi-agent
```

已完成全文候选中目前最清晰的主 owner 候选是：terminal data → Ch23；TTT-KVB
reinterpretation → Ch22；
ARLArena → Ch29；Untied Ulysses → Ch32/36 待二选一；veScale-FSDP → Ch35；DualPath → Ch51；
General Agent Evaluation → Ch62；Agents of Chaos → Ch68；SkillOrchestra → Ch80；GUI-Libra → Ch29；
Deep Research ranking → Ch72；SWE-Protégé → Ch77；EMPO² → Ch29；AgentDropoutV2 → Ch78；
Search More, Think Less → Ch75；ISO-Bench → Ch62；TAPE → Ch75；Aletheia / FirstProof → Ch62；
Multi-Vector Index Compression → Ch72；DPE → Ch23；Reflective Test-Time Planning → Ch76；Adaptive
Text Anonymization → Ch68；OmniGAIA → Ch74；MobilityBench → Ch62。
DSDR → Ch29；Implicit Intelligence → Ch62；PyVision-RL → Ch29。
ACE → Ch29；SGLang adapter readiness / stream lifetime → Ch46；vLLM async-PP request-state handoff →
Ch46；CUDA Agent staged domain warm-up → Ch29 candidate；LK objective-to-acceptance alignment → Ch44；
dLLM generative-process artifact identity → Ch20；STATIC constraint-state representation → Ch40；
SWE-rebench V2 environment diagnostics → Ch23；Memory Caching checkpoint granularity → Ch22；
Tool-R0 co-evolving curriculum → Ch29；LongVideo-R1 hierarchical active perception → Ch75；
RLAD advantage-conditioned teacher anchor → Ch29；Recovered in Translation benchmark compilation → Ch62；
Online World Modeling / MPAIL2 observation-only task inference and online planning → Ch10。
QEDBENCH domain-conditioned judge calibration → Ch62；ProbCOPA distributional target / elicitation → Ch62；
Algorithmic Cores cross-realization invariant / causal subspace → Ch5
candidate；SLATE shared-prefix local credit assignment → Ch29。
Qwen3-Coder-Next scaffold-bound staged specialization / expert consolidation → Ch25；SkillNet typed
skill-relation / composition admission → Ch80。
Trinity / CoW-Bench 的 taxonomy 与受限 benchmark evidence 已被 Ch10/62 的现有
原则覆盖，CL4SE 的 typed-context benchmark evidence 已被 Ch71/62/77 的现有原则覆盖，均不新增 owner；
SenCache 暴露的是当前 LLM-centric inference 章节的 structural gap，不强设 owner。
一个候选最终只设置一个主 owner，其他章节只写短 handoff。

## Post-Integration Action

1. Candidate Evidence Gate 与 Source-Family Books Gate 已分别闭合；62 项最终 disposition 为
   52 Refine、6 No Change、4 Weekly Only。CUPID 因 2025-12-16 first-public 归为 Cross-Year Exclusion，
   后续在 2025-W51 接续，不计入 W09。
2. Google Scholar、OpenAlex 的补漏路径恢复后继续幂等检查，并用 Crossref/primary metadata 交叉验证；
   2603.* 记录仍按 primary first-public date 归周，早于 02-23 的事件归回 W08 或更早周。
3. 后续只在 primary source、artifact 或章节结构出现实质新证据时幂等重开本周；不得因 revision 或产品
   headline 重复追加已融合机制。
4. vLLM/SGLang 的版本事实继续留在 Weekly；Books 只保留 async-PP request-state commit 与 adapter readiness /
   cross-stream lifetime 的长期 contract。
5. 所有跨章节引用继续使用 Stable Node ID；旧 Ch23～80 编号仅作为 legacy mapping，不解释成当前章节号。
6. 后续若 OpenAlex、Google Scholar、DBLP 或作者 artifact 恢复出 first-public date 属于 W09 的遗漏项，
   幂等重开 ledger；当前通过状态不表示索引覆盖的数学完备性证明。

## Event-Date Daily Decision

Historical Backfill 只维护完整 ISO Weekly，不补造 2026-02-23～03-01 Daily。候选的真实事件日期、
revision 与 Source Review 直接保留在本周档案。

## Final Source-Family Books Integration

`Source-Family Books Gate Complete — 62/62 final dispositions: 52 Refine, 6 No Change, 4 Weekly Only`。
Archive Completion Gate 仍为 Open：Google Scholar/OpenAlex 历史发现覆盖尚无独立可复算闭合证据；这不与
已完成的 62 个候选 Source Review 混写，也不撤销当前 Source-Family Books Gate。

| Stable owner / Current chapter | Integrated source families | Result |
| --- | --- | --- |
| `WORLDVIEW-REPRESENTATION` / Ch5 | Algorithmic Cores | basis-invariant functional evidence |
| `MODEL-LONG-CONTEXT` / Ch22 | TTT-KVB, Memory Caching | fast-state interpretation and checkpoint granularity |
| `MULTIMODAL-GENERATIVE-PARADIGMS` / Ch24 | dLLM, SenCache | process identity and bounded approximation cache |
| `MULTIMODAL-EMBODIED-VLA` / Ch26 | MPAIL2 | online world-model planning retained under physical-action boundary |
| `TRAIN-DATA` / Ch27 | Terminal Data, DPE, SWE-rebench V2 | executable row and diagnostic curriculum loop |
| `TRAIN-SFT` / Ch29 | Qwen3-Coder-Next | scaffold-bound specialization and expert consolidation |
| `TRAIN-GRPO` / Ch33 | DSDR, ACE, ARLArena, GUI-Libra, EMPO², PyVision-RL, Tool-R0, CUDA Agent, SLATE, RLAD | typed exploration, credit and verifier boundaries |
| `TRAIN-DISTRIBUTED-TRAINING` / Ch36 | Untied Ulysses | bounded Context Parallel buffers |
| `TRAIN-ZERO` / Ch39 | veScale-FSDP | structure-aware ragged shard placement |
| `INFER-SPECULATIVE-DECODING` / Ch48 | LK Losses | objective-to-acceptance alignment |
| `INFER-TENSORRT-LLM` / Ch49 | STATIC | constraint-state execution mapping |
| `INFER-VLLM` / Ch50 | vLLM v0.16.0 | distributed async request-state commit |
| `INFER-SGLANG` / Ch51 | SGLang v0.5.9 | adapter readiness and stream lifetime |
| `INFER-PD-DISAGGREGATION` / Ch55 | DualPath | workload-conditioned dual KV paths |
| `PLATFORM-EVALUATION-SYSTEM` / Ch66 | General Agent Evaluation, ISO-Bench, Implicit Intelligence, MobilityBench, Recovered Translation, QEDBENCH, ProbCOPA, LLMServingSim 2.0, AgentVista | subject, environment, derived benchmark, judge and simulator contracts |
| `PLATFORM-SECURITY` / Ch72 | Agents of Chaos, Adaptive Anonymization, IMMACULATE | principal/policy/effect, empirical privacy and service-integrity boundaries |
| `AGENT-CONTEXT` / Ch75 | CIRCLE | bounded self-conditioned Context refinement |
| `AGENT-RAG` / Ch76 | Deep Research ranking, Multi-Vector Compression | query dialect and index budget |
| `AGENT-MEMORY` / Ch77 | SWE-Protégé, AMA-Bench | escalation advice and construction-vs-retrieval attribution |
| `AGENT-TOOL-CALLING` / Ch78 | OmniGAIA | active perception as a typed tool action |
| `AGENT-PLANNING` / Ch79 | TAPE, Search More Think Less, LongVideo-R1 | feasibility, execution conformance and parallel evidence acquisition |
| `AGENT-REFLECTION` / Ch80 | Reflective TTP | verbal reflection versus parameter adaptation |
| `AGENT-MULTI-AGENT` / Ch82 | AgentDropoutV2 | message-edge rectify/reject contract |
| `AGENT-PLATFORM` / Ch84 | SkillOrchestra, SkillNet | competence-aware routing and typed skill relations |

`No Change` 的六项均有具体去重依据：Persona 已由 Ch5/66/72 的 explanation/evidence/authority 分层覆盖；
OpenAI malicious-use report 只增加 dated operational evidence；Aletheia 已由 Ch66 的 artifact correctness、
significance 与 autonomy 分层覆盖；Trinity 已由 Ch25/66 的 causal world-state 与 scorer boundary 覆盖；
CiteAudit 已由 Ch66 的 citation existence、claim entailment 与 provenance 覆盖；CL4SE 已由 Ch75/66 的
typed Context 与 evaluation identity 覆盖。

四项 `Weekly Only` 为 Cognitive Models as Agent Templates、BBQ-to-Image、Social User Simulation/CCP 与
SGDC：它们分别因 position-only、低项目相关性、已有 operational-validity 原则或领域方法不形成新的长期
AI System mechanism。原 SenCache structural gap 已由 Part III/Ch24 关闭，不再列为 Weekly Only。

## Pre-Integration Decision Snapshot（Superseded）

Historical state at this snapshot: Candidate Evidence Gate had passed for 62 in-window candidates, with 58 Full
Source Reviews and 4 low-score rejection checks complete; the Books pass had not yet been executed, the documented
cross-index discovery limitation remained, and 3 cross-year records had been excluded.

以下逐项列表保留 2026-08-13 写入前的 owner hypotheses，仅作为审计历史；其 `Books Candidate`、legacy
chapter 与 `Pending` 状态全部由上方 Final Source-Family Books Integration 和 Candidate Scoring 最终列覆盖。

- Persona Selection：`No Change — Already Covered`。
- OpenAI malicious-use report：`No Change — Already Covered / Weekly Operational Evidence`。
- Terminal data engineering：`Books Candidate / Data-Verifier Contract`，待 Ch23 及相邻章节复核。
- Untied Ulysses：`Books Candidate / Memory-Throughput Trade-off`，待 Ch32～36 owner 去重。
- DualPath：`Books Candidate / Workload-Topology Contract`，待 Ch48/50～52 相邻章节复核。
- veScale-FSDP：`Books Candidate / Shard-Layout Contract`，Ch35 存在真实机制缺口。
- General Agent Evaluation：`Books Candidate / Evaluation-Protocol Contract`，Ch62 可 refine。
- TTT with KV Binding：`Books Candidate / State-Mechanism Reinterpretation`，可能修正 Ch22 解释边界。
- Agents of Chaos：`Books Candidate / Authority-State-Effect Contract`，Ch68 存在组合边界缺口。
- ARLArena：`Books Candidate / Multi-Turn Optimization Contract`，Ch29 可保留 GRPO→Agent RL 演进。
- SkillOrchestra：`Books Candidate / Skill-Competence Routing State`，Ch80 可区分 asset 与 derived state。
- GUI-Libra：`Books Candidate / Partial-Verifiability Trust-Region Contract`，Ch29 存在机制缺口。
- Deep Research ranking：`Books Candidate / Agentic Ranking Contract`，Ch72 可 refine。
- SWE-Protégé：`Books Candidate / Learned Escalation and Follow-through Contract`，Ch77 可 refine。
- EMPO²：`Books Candidate / Temporary Memory Scaffold and Policy-Internalization Contract`，Ch29 可 refine。
- AgentDropoutV2：`Books Candidate / Message-Edge Rectify-Reject Contract`，Ch78 可 refine。
- Search More, Think Less：`Books Candidate / Parallel Evidence-Acquisition and Plan-Checkpoint Contract`，
  Ch75 可 refine。
- ISO-Bench：`Books Candidate / Optimization-Patch Evaluation Contract`，Ch62 可 refine。
- TAPE：`Books Candidate / Plan-Feasibility and Execution-Conformance Contract`，Ch75 可 refine。
- Aletheia / FirstProof：`Books Candidate / Proof-Credibility and Autonomy Evaluation Contract`，Ch62 可
  refine；P8 保留 publication-completeness dispute。
- Multi-Vector Index Compression：`Books Candidate / Late-Interaction Index-Budget Contract`，Ch72 可
  refine，但不把 index compression 写成 end-to-end latency 结论。
- DPE：`Books Candidate / Diagnostic Data-Mixture Control Loop`，Ch23 可 refine，保持 `Experimental`。
- Reflective Test-Time Planning：`Books Candidate / Reflection-to-Test-Time-Training Boundary Correction`，
  Ch76 现有“不更新参数”定义需要加 scope，而不是被新分支覆盖。
- Adaptive Text Anonymization：`Books Candidate / Empirical Privacy-Policy Contract`，Ch68 可补足 attacker、
  evaluator、prompt policy 与 formal guarantee 的边界。
- OmniGAIA：`Books Candidate / Active-Perception Placement Contract`，Ch74 可 refine，保持 `Experimental`。
- MobilityBench：`Books Candidate / Deterministic Environment-Replay Contract`，Ch62 可 refine。
- DSDR：`Books Candidate / Correct-Mode Exploration Contract`，Ch29 可 refine，保持 `Experimental`。
- Implicit Intelligence：`Books Candidate / Declarative Simulator Evidence Tier`，Ch62 可 refine，保持
  `Experimental`。
- PyVision-RL：`Books Candidate / Interaction-Budget Reward and Rollout-Selection Contract`，Ch29 可 refine，
  perception placement 只在 Ch74 短 handoff。
- Overconfident Errors / ACE：`Books Candidate / Confidence-Shifted Error-Weighting Contract`，Ch29 可与
  DSDR 形成“正确 mode exploration / 错误 confidence correction”分层演进，保持 `Experimental`。
- Trinity / CoW-Bench：`No Change — Already Covered / Weekly Only Benchmark Evidence`；Ch10 已有
  world-model causal/long-horizon/intervention 边界，Ch62 已有 atomic scorer 与 model-judge 校准 contract。
- SGLang v0.5.9：`Books Candidate / Adapter-Readiness and Cross-Stream Lifetime Contract`；Ch46 为主
  owner，Ch47/52 只做实现与调度边界 handoff；不把未披露 workload 的 release headline 写进正文。
- vLLM v0.16.0：`Books Candidate / Async-PP Request-State Handoff Contract`；Ch46 为主 owner，
  Ch34/52 只做 Pipeline Parallel 与 scheduling handoff；后续 issue 作为 failure evidence，不倒填事件日期。
- CUDA Agent：`Books Candidate / Domain-Warm-up and Executable Reward Contract`；优先检查 Ch29 是否
  只需补 actor/critic staged warm-up，Ch62/77 已有内容不重复复制。
- LK Losses：`Books Candidate / Objective-to-Runtime Acceptance Alignment`；Ch44 可能存在 KL-global-
  optimum 与 capacity-limited local mismatch 的机制缺口，保持 `Experimental`。
- dLLM：`Books Candidate / Generative-Process Artifact Contract`；Ch20 可补非 AR sampler/noise/remask/
  step-budget identity，Ch38/40/62 只作 runtime 与 evaluation handoff，保持 `Experimental`。
- STATIC：`Books Candidate / Constraint-State Representation and Snapshot Contract`；相邻章节复核后主
  owner 从初筛 Ch52 修正为 Ch40，Ch20/72 只作 token-selection 与 retrieval-policy handoff。
- SWE-rebench V2：`Books Candidate / Executable-Environment Diagnostics as Data-Control Signal`；与 terminal
  data engineering 合并审查 Ch23，论文未做 end-to-end RL curriculum ablation。
- Memory Caching：`Books Candidate / Compressed-State Checkpoint Granularity Contract`；Ch22 可补 attention
  与 fixed recurrence 之间的容量轴，保持 `Experimental`。
- Tool-R0：`Books Candidate / Co-evolving Curriculum and Role-Separation Contract`；Ch29 可补双 policy
  competence feedback、cross-version curriculum identity 与 collusion/reward-hacking 边界，保持 `Experimental`。
- LongVideo-R1：`Books Candidate / Hierarchical Active-Perception Search and Cost Contract`；Ch75 可补
  observation acquisition 作为 typed/costed plan action 的机制，Ch29/62/74 只作短 handoff。
- RLAD：`Books Candidate / Advantage-Conditioned Teacher-Anchor Contract`；Ch29 可补 offline→on-policy
  KL→advantage-conditioned distillation 演进，必须纠正 v3 的 `α` 端点 prose 冲突，保持 `Experimental`。
- CiteAudit：`No Change — Already Covered / Weekly Only Benchmark Evidence`；Ch62 已有 citation existence、
  claim entailment 与 claim-level provenance 边界，不重复写入 vendor-specific multi-agent stack。
- Recovered in Translation：`Books Candidate / Benchmark Translation as Semantics-Preserving Compilation
  Contract`；Ch62 可补 derived benchmark 的 task invariants、label identity 与 transformation lineage。
- SenCache：`Weekly Only / Structural Gap / No Coherent Owner`；其 approximation-cache 机制不等同 LLM KV
  Cache，当前不硬塞 Ch38/40/42/52，也不因此擅自调整 ROADMAP。
- CL4SE：`No Change — Already Covered / Weekly Only Benchmark Evidence`；Ch71 已有 context provenance、
  selection、placement、budget 与 evaluation contract，论文的一对一 task-context pairing 不足以形成新机制。
- Online World Modeling for IRLfO / MPAIL2：`Books Candidate / Observation-only Task-Inference and Online
  World-Model Planning Contract`；Ch10 可补 reward/task inference、online model/reward/value/policy/planner
  联合 ownership 与 drift 边界，保持 `Experimental`。
- QEDBENCH：`Books Candidate / Domain-Conditioned Judge Calibration and Critique–Verdict Separation
  Contract`；Ch62 可补总体 strictness、domain-conditioned leniency/harshness 与 critique/score 分离，保持
  `Experimental`，不写 vendor 排名。
- ProbCOPA：`Books Candidate / Distributional Target, Elicitation and Sampling-Identity Contract`；Ch62 可补
  population disagreement、verbalized likelihood 与 single-model sampling variation 的边界，Ch20 只作短
  handoff，保持 `Experimental`。
- Algorithmic Cores：`Books Candidate / Cross-Realization Invariant and Causal-Subspace Contract`；Ch5
  可 refine basis-invariant functional equivalence、sufficiency/necessity asymmetry 与 projector provenance，
  保持 `Experimental`，不把 synthetic grokking 或 narrow agreement 写成通用机制。
- LLMServingSim 2.0：`Books Candidate / Runtime-Driven Simulation Identity and Validation-Envelope Contract`；
  Ch62 为主 owner，Ch51 只保留 simulator prediction 不拥有 deployment authority 的 handoff。
- AMA-Bench：`Books Candidate / Causal Trajectory Memory and Construction-vs-Retrieval Loss Contract`；
  Ch73 为主 owner，Ch62/72/77 只承接 benchmark、retrieval 与 authoritative-workflow 边界；保持
  `Experimental`，不把离线 QA 排名外推成生产 memory architecture 结论。
- AgentVista：`Books Candidate / Task-Construction–Harness Coupling and Failure-Attribution Boundary`；
  Ch62 为主 owner，Ch74/75/77 只承接 tool、plan 与 durable-workflow contract；保持 `Experimental`，不写
  model 排行或把 model-labeled error taxonomy 当 causal root cause。
- CIRCLE：`Books Candidate / Self-Conditioned Context Refinement and Error-Amplification Contract`；Ch71 为主
  owner，Ch62/72 只承接 metric validity 与 retrieval selection；保持 `Experimental`，不把作者模型比较或
  semantic-consistency metrics 外推为真实 taxonomy recovery。
- IMMACULATE：`Books Candidate / Probabilistic Service-Integrity Audit and Hybrid-State Commitment Contract`；
  Ch68 为主 owner，Ch64/65/66/69 只承接 evidence、correlation、cost 与 readiness；保持 `Experimental`，不得把
  CPU-TDX prototype 写成无 trusted-hardware 证明，或把 EVT false-positive estimate 写成生产事实。
- CUPID：`Cross-Year Exclusion / No W09 Books Decision`；first-public date 为 2025-12-16。全文复核形成
  `Unlearning Target-Specification and Shortcut-Forgetting Evaluation Contract` 候选，后续只在 2025-W51
  Evidence Gate 下决定是否 refine Ch68，Ch62 作评估 handoff。
- Replicate-and-Quantize、MINAR：`Cross-Year Exclusion / No W09 Books Decision`；first-public dates 分别为
  2024-09-22、2025-09-23，2026 arXiv 只作为 source-family revision evidence。
- SLATE：`Books Candidate / Shared-Prefix Local-Credit Contract`；Ch29 可补同 prompt→同 prefix comparison
  cohort、local/future credit trade-off 与 judge/retriever/run identity，保持 `Experimental`。
- Qwen3-Coder-Next：`Books Candidate / Scaffold-Bound Staged Specialization and Expert-Consolidation
  Contract`；主 owner Ch25，Ch23/29/77 只作 executable data、reward 与 workflow handoff。模型排名、
  80B/3B、80 万任务与 262K context 不作为通用配方。
- SkillNet：`Books Candidate / Typed Skill-Relation and Composition-Admission Contract`；优先 refine Ch80
  现有 Skill registry 小节，若 relation evidence/version 与 transitive authorization 不能形成增量则降为
  `No Change — Already Covered`，保持 `Experimental`。
- BBQ-to-Image、Simulating Social Media Users / CCP、SGDC：`Weekly Only — Low Project Relevance or
  Existing Principle Covered`；仅完成可信来源、日期与拒绝理由核验，不把 domain headline 写入 Books。

## Ignored Noise

- 将个案数量外推为总体威胁率，或将 persona explanation 推广成所有模型的内部实现。
- 仅因论文出现在 HF Daily 热榜就抬高 Evidence Level，或把 discovery date 当 first-public date。
- 摘取“最高倍率”而丢失 model、hardware、precision、length、batch、concurrency、topology、baseline
  与 SLO；本周所有性能数字均要求绑定完整 workload contract。
- 把 head-wise Context Parallel、storage-to-Prefill 双路径或 executable terminal data 写成单向替代史；
  旧方案在低复杂度、低复用、短 context、简单 topology 或人工验证更可靠时仍成立。

## Repository Changes

- 幂等扩充本文件：初轮候选由 2 项恢复为 33 项；post-week discovery-lag 又找回 15 项，总账为
  48 项；继续扫描 HF 03-04～03-06 又恢复 10 项，交叉索引再发现 IMMACULATE、LLMServingSim 2.0、
  AMA-Bench、Replicate-and-Quantize 与 MINAR。IMMACULATE 已完成 Full Review；Replicate-and-Quantize 因
  first-public date 更正至 2024 被
  排除；MINAR 同样因 2025 OpenReview first-public 被排除；CUPID 在全文复核后确认作者机构已于
  2025-12-16 公开核心方法，亦归回 2025-W51。随后 post-week spillover 又补回 Qwen3-Coder-Next 与
  SkillNet，in-window 总账现为 62 项。两项现已完成全文、Appendix、官方 artifact 和相邻章节联读；
  当前完成 58 项 Full Source Review、4 项低分来源/拒绝核验，另保留 3 项 Cross-Year Exclusion。
  Candidate Evidence Gate 已通过；Google Scholar/OpenAlex coverage gap 继续作为 Discovery Limitation。
- 纠正“本周无 stable release”的旧结论，纳入 SGLang v0.5.9 与 vLLM v0.16.0，并记录 Dynamo、
  PyTorch 的相邻周去重依据。
- 已按 owner chapter 分组完成 Books Integration，并在每组后检查围栏、尾随空白、来源入口与局部 diff；
  最终涉及 Ch5、22、24、26、27、29、33、36、39、48～51、55、66、72、75～80、82、84。没有新增孤立章节，
  没有把版本 feature list 或作者 benchmark 复制进正文。
- 逐组 Review 纠正了书稿中 DPE 的错误 arXiv 入口：`2602.21624` 更正为 primary source `2602.22859`。

## Open Questions

1. Persona/state transition 如何进入 runtime policy、audit log 与 red-team coverage，同时避免把解释模型
   当作可观测真值？
2. DualPath 的收益在 shared NIC/PCIe、较低 cache hit、较少 turns 和不同 P/D ratio 下如何变化？
3. UPipe 的 head chunk `U` 能否按 context、GQA layout、topology 与 free-memory budget 动态调节？
4. Terminal failed trajectories 的收益能否在等 token、等 task diversity 与独立 held-out verifier 下复现？
5. Google Scholar、OpenAlex、DBLP 后续索引刷新是否还会恢复出当前 62 项以外、
   first-public date 确属 W09 的候选？
6. SGLang adapter cancellation/eviction 与 vLLM async-PP abort/retry 如何分别证明 slot/event、token row
   与 placeholder 已被所有并行 participant 一致回收？
7. Evaluation protocol adapter 的 semantic-equivalence、FSDP shard-layout checkpoint round-trip 与
   TTT-KVB revision 差异能否分别由公开 artifact 独立复核？
8. GUI verifier coverage、Agentic ranking 的 query-dialect drift 与 coding-agent escalation budget
   能否形成可共同审计、但不混淆 authority 的 runtime evidence？
9. ACE 的 confidence shift 在 moving reference、continuous/process reward 与超长 CoT 下是否仍是稳定
   error signal？它与 DSDR/Clip-Higher 的交互是否经过正交 ablation？
10. CoW-Bench 论文 1,485 与公开 dataset 1,435 rows 的差异如何解释？四帧 `gpt-4.1` judge 能否由
    dense trace、physics verifier 与独立 human calibration 复核？
11. dLLM 的 sampler/noise/remask/EOS 配置如何形成跨 framework 可比较的 immutable artifact identity？
    STATIC 的 constraint snapshot 又如何支持增量更新、request pinning 与失败回滚？
12. Tool-R0 的双 policy 如何防止 shared blind spot/collusion，并给 curriculum checkpoint 提供 promotion、
    rollback 与独立 ground-truth gate？LongVideo-R1 的错误 observation branch 又如何触发可审计 backtrack？
13. Qwen3-Coder-Next 的 cross-scaffold transfer、expert distillation retention 与 reward-hacking blocker，能否在
    held-out tool schemas、独立 verifier 和 matched training/serving compute 下复现？
14. SkillNet 的 relation edge 怎样绑定生成 evidence、version 与失效条件？组合 skill 时，transitive
    permission、dependency lock、poisoning quarantine、revocation propagation 与 rollback 应由谁拥有？

## Sources

- Qwen3-Coder-Next Technical Report metadata (v1 2026-02-28):
  https://arxiv.org/abs/2603.00729
- SkillNet metadata (v1 2026-02-26): https://arxiv.org/abs/2603.04448
- Qwen3-Coder-Next full HTML (v1): https://arxiv.org/html/2603.00729v1
- Qwen3-Coder-Next official model card: https://huggingface.co/Qwen/Qwen3-Coder-Next
- Qwen3-Coder official repository: https://github.com/QwenLM/Qwen3-Coder
- SkillNet full HTML (v1): https://arxiv.org/html/2603.04448v1
- SkillNet official repository and SDK: https://github.com/zjunlp/SkillNet
- Anthropic Research index, “The persona selection model,” dated 2026-02-23:
  https://www.anthropic.com/research
- OpenAI, “Disrupting malicious uses of AI,” published 2026-02-25:
  https://openai.com/index/disrupting-malicious-ai-uses/
- SkillOrchestra: https://arxiv.org/abs/2602.19672
- SkillOrchestra full PDF: https://arxiv.org/pdf/2602.19672
- SkillOrchestra official code: https://github.com/jiayuww/SkillOrchestra
- Agents of Chaos: https://arxiv.org/abs/2602.20021
- Agents of Chaos full PDF: https://arxiv.org/pdf/2602.20021
- Agents of Chaos interactive evidence: https://agentsofchaos.baulab.info/
- OpenClaw repository (current code; not a pinned paper revision): https://github.com/openclaw/openclaw
- DSDR: https://arxiv.org/abs/2602.19895
- DSDR full HTML: https://arxiv.org/html/2602.19895
- DSDR official code: https://github.com/SUSTechBruce/DSDR
- TAPE: https://arxiv.org/abs/2602.19633
- TAPE full HTML: https://arxiv.org/html/2602.19633
- TAPE official code: https://github.com/UW-Madison-Lee-Lab/TAPE
- Implicit Intelligence: https://arxiv.org/abs/2602.20424
- Implicit Intelligence full HTML: https://arxiv.org/html/2602.20424
- Implicit Intelligence official leaderboard:
  https://labelbox.com/leaderboards/implicit-intelligence/
- ISO-Bench: https://arxiv.org/abs/2602.19594
- ISO-Bench full HTML: https://arxiv.org/html/2602.19594
- ISO-Bench official code: https://github.com/Lossfunk/ISO-Bench
- ISO-Bench official dataset: https://huggingface.co/datasets/Lossfunk/ISO-Bench
- Data Engineering for Scaling LLM Terminal Capabilities:
  https://arxiv.org/abs/2602.21193
- Data Engineering full HTML: https://arxiv.org/html/2602.21193
- Test-Time Training with KV Binding Is Secretly Linear Attention:
  https://arxiv.org/abs/2602.21204
- PyVision-RL: https://arxiv.org/abs/2602.20739
- PyVision-RL v1 full-text mirror: https://www.alphaxiv.org/abs/2602.20739v1
- PyVision-RL official code/data/model entry: https://github.com/agents-x-project/PyVision-RL
- PyVision-RL official project page: https://agent-x.space/pyvision-rl/
- Multi-Vector Index Compression in Any Modality: https://arxiv.org/abs/2602.21202
- Multi-Vector Index Compression full HTML: https://arxiv.org/html/2602.21202
- Multi-Vector Index Compression official code: https://github.com/hanxiangqin/omni-col-press
- Untied Ulysses: https://arxiv.org/abs/2602.21196
- Untied Ulysses full HTML: https://arxiv.org/html/2602.21196
- Aletheia tackles FirstProof autonomously: https://arxiv.org/abs/2602.21201
- Aletheia / FirstProof full HTML: https://arxiv.org/html/2602.21201
- Aletheia / FirstProof official raw artifacts:
  https://github.com/google-deepmind/superhuman/tree/main/aletheia
- Learning from Trials and Errors / Reflective Test-Time Planning:
  https://arxiv.org/abs/2602.21198
- Reflective Test-Time Planning full HTML: https://arxiv.org/html/2602.21198
- Reflective Test-Time Planning official code:
  https://github.com/Reflective-Test-Time-Planning/Reflective-Test-Time-Planning
- Adaptive Text Anonymization: https://arxiv.org/abs/2602.20743
- Adaptive Text Anonymization full HTML: https://arxiv.org/html/2602.20743
- Adaptive Text Anonymization official code:
  https://github.com/gabrielloiseau/adaptive-text-anonymization
- Overconfident Errors Need Stronger Correction: https://arxiv.org/abs/2602.21420
- Overconfident Errors full HTML: https://arxiv.org/html/2602.21420
- DualPath: https://arxiv.org/abs/2602.21548
- DualPath full HTML: https://arxiv.org/html/2602.21548
- ARLArena: https://arxiv.org/abs/2602.21534
- ARLArena full PDF: https://arxiv.org/pdf/2602.21534
- ARLArena official code: https://github.com/WillDreamer/ARL-Arena
- GUI-Libra: https://arxiv.org/abs/2602.22190
- GUI-Libra full HTML (current v2, used only for mechanism/revision verification):
  https://arxiv.org/html/2602.22190v2
- GUI-Libra official code: https://github.com/GUI-Libra/GUI-Libra
- Revisiting Text Ranking in Deep Research: https://arxiv.org/abs/2602.21456
- Revisiting Text Ranking in Deep Research full HTML: https://arxiv.org/html/2602.21456
- Revisiting Text Ranking official artifact:
  https://github.com/ChuanMeng/text-ranking-in-deep-research
- veScale-FSDP: https://arxiv.org/abs/2602.22437
- veScale-FSDP full HTML: https://arxiv.org/html/2602.22437
- veScale official partial artifact: https://github.com/volcengine/veScale
- SWE-Protégé: https://arxiv.org/abs/2602.22124
- SWE-Protégé full PDF: https://arxiv.org/pdf/2602.22124
- The Trinity of Consistency: https://arxiv.org/abs/2602.23152
- Trinity full-text mirror: https://www.alphaxiv.org/abs/2602.23152
- CoW-Bench official project: https://openraiser.github.io/CoW-Bench/
- CoW-Bench public dataset and card: https://huggingface.co/datasets/OpenRaiser/CoW-Bench
- CoW-Bench public evaluation code:
  https://huggingface.co/datasets/OpenRaiser/CoW-Bench/blob/main/eval_code/evaluate.py
- Trinity survey repository: https://github.com/openraiser/awesome-world-model-evolution
- From Blind Spots to Gains / DPE: https://arxiv.org/abs/2602.22859
- DPE full HTML: https://arxiv.org/html/2602.22859
- DPE official code and model links: https://github.com/hongruijia/DPE
- MobilityBench: https://arxiv.org/abs/2602.22638
- MobilityBench full HTML: https://arxiv.org/html/2602.22638
- MobilityBench official code/data entry: https://github.com/AMAP-ML/MobilityBench
- OmniGAIA: https://arxiv.org/abs/2602.22897
- OmniGAIA full PDF: https://arxiv.org/pdf/2602.22897
- OmniGAIA official code/data/model entry: https://github.com/RUC-NLPIR/OmniGAIA
- EMPO²: https://arxiv.org/abs/2602.23008
- EMPO² full HTML (current v2, used only for mechanism/revision verification):
  https://arxiv.org/html/2602.23008
- EMPO² ICLR/OpenReview paper: https://openreview.net/forum?id=UOzxviKVFO
- EMPO² author project page: https://beanie00.github.io/empo2/
- Microsoft Agent Lightning current EMPO² integration:
  https://github.com/microsoft/agent-lightning/tree/main/contrib/recipes/envs
- AgentDropoutV2: https://arxiv.org/abs/2602.23258
- AgentDropoutV2 current full HTML: https://arxiv.org/html/2602.23258
- AgentDropoutV2 official current code: https://github.com/TonySY2/AgentDropoutV2
- Search More, Think Less: https://arxiv.org/abs/2602.22675
- Search More, Think Less full HTML: https://arxiv.org/html/2602.22675
- General Agent Evaluation: https://arxiv.org/abs/2602.22953
- General Agent Evaluation full HTML: https://arxiv.org/html/2602.22953
- Exgentic official artifact and leaderboard: https://www.exgentic.ai/
- TTT with KV Binding full HTML: https://arxiv.org/html/2602.21204
- NVIDIA Research project page: https://research.nvidia.com/labs/sil/projects/tttla/
- Hugging Face Daily discovery, 2026-02-23: https://huggingface.co/papers/date/2026-02-23
- Hugging Face Daily discovery, 2026-02-24: https://huggingface.co/papers/date/2026-02-24
- Hugging Face Daily discovery, 2026-02-25: https://huggingface.co/papers/date/2026-02-25
- Hugging Face Daily discovery, 2026-02-26: https://huggingface.co/papers/date/2026-02-26
- Hugging Face Daily discovery, 2026-02-27: https://huggingface.co/papers/date/2026-02-27
- Hugging Face Daily discovery gaps (pages unavailable during this pass):
  https://huggingface.co/papers/date/2026-02-28 and
  https://huggingface.co/papers/date/2026-03-01
- arXiv 2022 Annual Report (announcement cadence: five days per week):
  https://info.arxiv.org/about/reports/2022_arXiv_annual_report.pdf
- OpenAlex official Works API documentation (historical coverage attempt; API key required by current endpoint):
  https://developers.openalex.org/api-reference/works/list-works
- DBLP official publication-search API documentation:
  https://dblp.org/faq/13501473.html
- SGLang v0.5.9 release: https://github.com/sgl-project/sglang/releases/tag/v0.5.9
- SGLang LoRA weight-loading overlap PR #15512:
  https://github.com/sgl-project/sglang/pull/15512
- SGLang LoRA weight-loading overlap code diff:
  https://github.com/sgl-project/sglang/pull/15512/files
- SGLang FlashInfer All-to-All dispatcher PR #14668:
  https://github.com/sgl-project/sglang/pull/14668/files
- SGLang Spec V2 cross-stream lifetime fix PR #18958:
  https://github.com/sgl-project/sglang/pull/18958
- vLLM v0.16.0 release: https://github.com/vllm-project/vllm/releases/tag/v0.16.0
- vLLM async scheduling + Pipeline Parallel PR #32618:
  https://github.com/vllm-project/vllm/pull/32618
- vLLM async scheduling + Pipeline Parallel code diff:
  https://github.com/vllm-project/vllm/pull/32618/files
- vLLM native weight-sync RFC #31848: https://github.com/vllm-project/vllm/issues/31848
- vLLM pause/resume RFC #32103: https://github.com/vllm-project/vllm/issues/32103
- vLLM NIXL connector v2 cross-layer layout PR #33339:
  https://github.com/vllm-project/vllm/pull/33339/files
- vLLM async-PP chunked-request fix PR #38726:
  https://github.com/vllm-project/vllm/pull/38726
- vLLM multi-node cross-request contamination report #38903:
  https://github.com/vllm-project/vllm/issues/38903
- Dynamo releases (W09 cross-week exclusion): https://github.com/ai-dynamo/dynamo/releases?page=2
- PyTorch releases (W09 cross-week exclusion): https://github.com/pytorch/pytorch/releases
- Hugging Face Daily discovery spillover, 2026-03-02:
  https://huggingface.co/papers/date/2026-03-02
- Hugging Face Daily discovery spillover, 2026-03-03:
  https://huggingface.co/papers/date/2026-03-03
- Hugging Face Daily discovery spillover, 2026-03-04:
  https://huggingface.co/papers/date/2026-03-04
- Hugging Face Daily discovery spillover, 2026-03-05:
  https://huggingface.co/papers/date/2026-03-05
- Hugging Face Daily discovery spillover, 2026-03-06:
  https://huggingface.co/papers/date/2026-03-06
- CUDA Agent metadata: https://arxiv.org/abs/2602.24286
- CUDA Agent full HTML v1: https://arxiv.org/html/2602.24286v1
- CUDA Agent project and released artifacts: https://cuda-agent.github.io/
- LK Losses metadata and revision history: https://arxiv.org/abs/2602.23881
- LK Losses full HTML v2: https://arxiv.org/html/2602.23881v2
- dLLM metadata: https://arxiv.org/abs/2602.22661
- dLLM full HTML v1: https://arxiv.org/html/2602.22661v1
- dLLM official code: https://github.com/ZHZisZZ/dllm
- CiteAudit metadata: https://arxiv.org/abs/2602.23452
- CiteAudit full HTML v3: https://arxiv.org/html/2602.23452v3
- CiteAudit official code and benchmark: https://github.com/shiiiikw/CiteAudit
- Memory Caching metadata: https://arxiv.org/abs/2602.24281
- Memory Caching full HTML v1: https://arxiv.org/html/2602.24281v1
- SenCache metadata: https://arxiv.org/abs/2602.24208
- SenCache full HTML v1: https://arxiv.org/html/2602.24208v1
- SenCache official code: https://github.com/vita-epfl/SenCache
- Vectorizing the Trie / STATIC metadata: https://arxiv.org/abs/2602.22647
- Vectorizing the Trie / STATIC full HTML v2: https://arxiv.org/html/2602.22647v2
- LongVideo-R1 metadata: https://arxiv.org/abs/2602.20913
- LongVideo-R1 official code/data entry: https://github.com/qiujihao19/LongVideo-R1
- Reinforcement-aware Knowledge Distillation metadata:
  https://arxiv.org/abs/2602.22495
- Reinforcement-aware Knowledge Distillation full HTML v3:
  https://arxiv.org/html/2602.22495v3
- CL4SE metadata: https://arxiv.org/abs/2602.23047
- CL4SE full HTML v1: https://arxiv.org/html/2602.23047v1
- CL4SE current full HTML v3 (revision-boundary verification only):
  https://arxiv.org/html/2602.23047
- CL4SE official code: https://github.com/Tomsawyerhu/CodeCL
- CL4SE official dataset: https://huggingface.co/datasets/tomhu/codecl
- SWE-rebench V2 metadata: https://arxiv.org/abs/2602.23866
- SWE-rebench V2 full HTML v2: https://arxiv.org/html/2602.23866v2
- SWE-rebench V2 official code: https://github.com/SWE-rebench/SWE-rebench-V2
- SWE-rebench V2 issue-derived dataset: https://huggingface.co/datasets/nebius/SWE-rebench-V2
- SWE-rebench V2 PR-derived dataset: https://huggingface.co/datasets/nebius/SWE-rebench-V2-PRs
- Tool-R0 metadata: https://arxiv.org/abs/2602.21320
- Tool-R0 full HTML v1: https://arxiv.org/html/2602.21320v1
- Tool-R0 official code: https://github.com/emrecanacikgoz/Tool-R0
- Tool-R0 project page: https://emrecanacikgoz.github.io/Tool-R0/
- Tool-R0 model collection: https://huggingface.co/collections/emrecanacikgoz/tool-r0
- Tool-R0 public logs link (access not independently verified in this run):
  https://api.wandb.ai/links/acikgoz2-university-of-illinois-urbana-champaign/olowdrg5
- LongVideo-R1 full HTML v1: https://arxiv.org/html/2602.20913v1
- Online World Modeling for IRLfO metadata: https://arxiv.org/abs/2602.24121
- Online World Modeling for IRLfO current full HTML:
  https://arxiv.org/html/2602.24121
- MPAIL2 official project page: https://uwrobotlearning.github.io/mpail2/
- QEDBENCH metadata: https://arxiv.org/abs/2602.20629
- QEDBENCH full HTML v1: https://arxiv.org/html/2602.20629v1
- QEDBENCH current full HTML v3 (revision-boundary verification only):
  https://arxiv.org/html/2602.20629
- QEDBENCH official benchmark repository: https://github.com/qqliu/Yale-QEDBench
- Humans and LLMs Diverge on Probabilistic Inferences metadata:
  https://arxiv.org/abs/2602.23546
- Humans and LLMs Diverge on Probabilistic Inferences full HTML v1:
  https://arxiv.org/html/2602.23546v1
- ProbCOPA official data/code repository:
  https://github.com/McGill-NLP/probabilistic-reasoning
- Replicate-and-Quantize for MoE Load Balancing primary metadata:
  https://arxiv.org/abs/2602.19938
- Replicate-and-Quantize original OpenReview record (first public 2024-09-22):
  https://openreview.net/forum?id=0wfmHoKQX6
- Replicate-and-Quantize original OpenReview full paper:
  https://openreview.net/pdf?id=0wfmHoKQX6
- Replicate-and-Quantize 2026 expanded public full-text mirror:
  https://www.researchgate.net/publication/401132003_A_Replicate-and-Quantize_Strategy_for_Plug-and-Play_Load_Balancing_of_Sparse_Mixture-of-Experts_LLMs
- Replicate-and-Quantize DBLP cross-index record:
  https://dblp.org/rec/journals/corr/abs-2602-19938
- MINAR primary metadata: https://arxiv.org/abs/2602.21442
- MINAR official OpenReview record (first public 2025-09-23):
  https://openreview.net/forum?id=3PbQUU9rgu
- MINAR official OpenReview full paper:
  https://openreview.net/pdf?id=3PbQUU9rgu
- MINAR public full-text mirror:
  https://www.researchgate.net/publication/401229176_MINAR_Mechanistic_Interpretability_for_Neural_Algorithmic_Reasoning
- MINAR DBLP cross-index record: https://dblp.org/rec/journals/corr/abs-2602-21442
- MINAR official code: https://github.com/pnnl/MINAR
- IMMACULATE primary metadata: https://arxiv.org/abs/2602.22700
- IMMACULATE public CC BY 4.0 full-text mirror used because direct arXiv access was unavailable in this run:
  https://www.researchgate.net/publication/401280057_IMMACULATE_A_Practical_LLM_Auditing_Framework_via_Verifiable_Computation
- IMMACULATE DBLP cross-index record: https://dblp.org/rec/journals/corr/abs-2602-22700
- IMMACULATE official code (redirected author repository):
  https://github.com/paulguoyanpei/Immaculate
- LLMServingSim 2.0 primary metadata: https://arxiv.org/abs/2602.23036
- LLMServingSim 2.0 v1 full-text mirror used because direct arXiv access was unavailable in this run:
  https://www.alphaxiv.org/abs/2602.23036v1
- LLMServingSim 2.0 official project: https://llmservingsim.ai/
- LLMServingSim 2.0 official architecture documentation:
  https://llmservingsim.ai/docs/simulator/architecture
- LLMServingSim 2.0 official validation documentation:
  https://llmservingsim.ai/docs/validation
- LLMServingSim 2.0 official code: https://github.com/casys-kaist/LLMServingSim
- LLMServingSim 2.0 frozen ISPASS artifact: https://zenodo.org/records/18879965
- LLMServingSim 2.0 DBLP cross-index record:
  https://dblp.org/rec/journals/corr/abs-2602-23036
- LLMServingSim2.0 CAL 2025 family metadata (cross-version deduplication):
  https://arxiv.org/abs/2511.07229
- AMA-Bench primary metadata: https://arxiv.org/abs/2602.22769
- AMA-Bench public CC BY 4.0 full-text mirror used because direct arXiv access was unavailable in this run:
  https://www.researchgate.net/publication/401279596_AMA-Bench_Evaluating_Long-Horizon_Memory_for_Agentic_Applications
- AMA-Bench official project: https://ama-bench.github.io/
- AMA-Bench official code: https://github.com/AMA-Bench/AMA-Bench
- AMA-Bench DBLP cross-index record:
  https://dblp.org/rec/journals/corr/abs-2602-22769
- Transformers Converge to Invariant Algorithmic Cores metadata:
  https://arxiv.org/abs/2602.22600
- Transformers Converge to Invariant Algorithmic Cores full HTML v1:
  https://arxiv.org/html/2602.22600v1
- Transformers Converge to Invariant Algorithmic Cores current full HTML v2 (revision-boundary verification only):
  https://arxiv.org/html/2602.22600
- Transformers Converge to Invariant Algorithmic Cores official code:
  https://github.com/joshseth/cores
- Easy to Learn, Yet Hard to Forget / CUPID metadata:
  https://arxiv.org/abs/2602.21773
- Easy to Learn, Yet Hard to Forget / CUPID full HTML v1:
  https://arxiv.org/html/2602.21773v1
- Easy to Learn, Yet Hard to Forget / CUPID official AAAI proceedings page:
  https://ojs.aaai.org/index.php/AAAI/article/view/37499
- Easy to Learn, Yet Hard to Forget / CUPID official AAAI paper PDF:
  https://ojs.aaai.org/index.php/AAAI/article/download/37499/41461
- Chung-Ang University official AAAI-26 research announcement (2025-12-16; first-public correction):
  https://gsaim.cau.ac.kr/bbs/board.php?language=EN&mode=VIEW&num=52&tbl=bbs61
- AgentVista metadata: https://arxiv.org/abs/2602.23166
- AgentVista public CC BY 4.0 v1 full-text mirror used because direct arXiv access was unavailable in this run:
  https://www.researchgate.net/publication/401278460_AgentVista_Evaluating_Multimodal_Agents_in_Ultra-Challenging_Realistic_Visual_Scenarios
- AgentVista official project: https://agentvista-bench.github.io/
- AgentVista official code: https://github.com/hkust-nlp/AgentVista
- AgentVista official dataset: https://huggingface.co/datasets/Warrieryes/AgentVista
- Large Multimodal Models as General In-Context Classifiers metadata:
  https://arxiv.org/abs/2602.23229
- Large Multimodal Models as General In-Context Classifiers official CVF accepted-paper page:
  https://openaccess.thecvf.com/content/CVPR2026F/html/Garosi_Large_Multimodal_Models_as_General_In-Context_Classifiers_CVPRF_2026_paper.html
- Large Multimodal Models as General In-Context Classifiers public full-text mirror used because direct arXiv
  access was unavailable in this run:
  https://www.researchgate.net/publication/401278846_Large_Multimodal_Models_as_General_In-Context_Classifiers
- CIRCLE official project: https://circle.marcogarosi.com/
- CIRCLE author publication page: https://alessandroconti.me/papers/2602.23229.html
- Truncated Step-Level Sampling / SLATE metadata:
  https://arxiv.org/abs/2602.23440
- Truncated Step-Level Sampling / SLATE full HTML v1:
  https://arxiv.org/html/2602.23440v1
- Truncated Step-Level Sampling / SLATE current full HTML v4 (revision-boundary verification only):
  https://arxiv.org/html/2602.23440
- Truncated Step-Level Sampling / SLATE official code:
  https://github.com/algoprog/SLATE
- BBQ-to-Image metadata: https://arxiv.org/abs/2602.20672
- Simulating Social Media Users with LLMs / CCP metadata:
  https://arxiv.org/abs/2602.22752
- SGDC metadata: https://arxiv.org/abs/2602.23496
- Spilled Energy metadata (cross-week exclusion to W08): https://arxiv.org/abs/2602.18671
- AgentConductor metadata (cross-week exclusion to W08): https://arxiv.org/abs/2602.17100
- Cognitive Models as Agent Templates metadata: https://arxiv.org/abs/2602.22523
- Recovered in Translation metadata: https://arxiv.org/abs/2602.22207
- Recovered in Translation full HTML v1: https://arxiv.org/html/2602.22207v1
- Recovered in Translation official code: https://github.com/insait-institute/ritranslation
- Recovered multilingual benchmarks artifact:
  https://huggingface.co/datasets/insait-institute/multilingual-benchmarks
- DUET-VLM metadata (cross-week exclusion to W08): https://arxiv.org/abs/2602.18846

## 2026-08-13 Source-Family Books Integration

Online World Modeling / MPAIL2 已通过独立 Source-Family Books Gate：Owner `MULTIMODAL-EMBODIED-VLA`，Current Ch26，Legacy N/A；其 online learned dynamics、observation refresh 与 real-robot evaluation contract 已作为 Experimental 分支融入 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`。该 integration 不把所测 robot/task 结果外推为通用 VLA 优势。Archive Completion Gate 仍 Open。

SenCache 的原 structural owner gap 已由 ADR-008 关闭。Owner 为 `MULTIMODAL-GENERATIVE-PARADIGMS`，Current chapter Ch24，Legacy N/A；最终 disposition 为 `Integrate — sensitivity-bounded approximation cache / Experimental`。书稿明确把 denoiser-output approximation cache 与 AR KV exact-state cache 分开，保留 static schedule、distilled/few-step model 的共存条件，并把 calibration identity、quality tolerance、max staleness 与 global error budget 写成机制 contract。作者 NFE 与 GH200 单 workload latency 没有被外推为生产 goodput。修改文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`。Open questions 仍是 sampler/model drift、semantic quality calibration 与 local-to-global budget allocation；Archive Completion Gate 仍 Open。
