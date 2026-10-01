# 2026-06-09 V3 recovered-candidate evidence

本包覆盖最终 denominator 中 38 个 closure-recovered Candidate。37 项读取 official exact-v1 HTML；2606.09483 的主站 body/PDF 连续超时后，改由同属 arXiv 官方域的 `export.arxiv.org` exact-v1 PDF 恢复正文，不用旧 trace 补权。第二轮全表复核将 2606.07909、2606.08300 与 2606.08702 降回 pre-denominator closure；其中前两项曾进入本恢复包，以下不再保留其 Source Review。

## Enabling KV Caching of Shared Prefix for Diffusion Language Models

- **Identity / Method：** `arXiv:2606.07571v1`；§4 Observations、§5 BiCache。浅层 exact-prefix KV 在高相似度区域复用；共享前缀比例决定安全层深，深层按刷新间隔重算。
- **Evaluation：** §6；LLaDA、B200 180GB、batch=1、generation length=256、steps=128；相对无缓存报告 36.3%～82.8% 加速，组合路径最高 98.3%，准确率差异 0～1.8%。
- **Limitations：** §9；exact prefix、offline profiling、单一 LLaDA family/current DLM ecosystem，不外推其他 architecture、accelerator 或生产 SLO。
- **Books：** `已有覆盖`，owner=`INFER-KV-CACHE`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## OmniMem: Perturbation-aware Memory Compression for Streaming Audio-Visual LLMs

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07577v1) §3.1–3.3：chunk后按Attention importance与hidden-state cosine redundancy提议淘汰；audio/visual独立cache，逐层/模态预算在小视频集校准。不是未来Query的无损保证；SFT另用hidden-state carrier与截断反向，不等于原淘汰器本身的收益。
- **Evaluation：** §4.3、§5/Table2–3：SALMONN 4B/8B、Qwen2.5-Omni 7B，1FPS/360p，默认每层8K budget，H800。比例变化呈现音频/视觉的任务取舍；Qwen Contextual 34.2低于HERMES 34.5。SFT仅SALMONN，32×H800/36h，不能与training-free成本混同；precision、batch/concurrency、SLO未披露。
- **Limitations：** §7明确hidden-state驻留开销、长音视频benchmark不足与linear-attention需要重设计。校准不覆盖未来问题、并发和硬件迁移；未复现实验。
- **Books：** `整合`：Ch45旧Prefill/Decode query校准没有独立modality budget。6分保留，因确认知识缺口深入必要范围；`INFER-KV-CACHE`已在该段之后写入两段机制/代价/反例。sep21_resume_v3准入、必要证据与实际写后独立通过；不代表整日日级验收已通过。

## Training-Inference Kernel Contracts: Bounding Divergence in Post-Training and Deployment

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07581v1) §4–6给kernel-indexed policy、分slice合同与per-token梯度偏差界；§6.1要求support overlap、有界advantage与score norm，不控制trajectory乘积或完整训练收敛。
- **Evaluation / Counterevidence：** §8只是待执行protocol，Appendix C明确未随论文发布的实现草图，无生产实测。§6.3 Eq17在c=0时clip(w,1,1)=1，退回Eq15的有偏估计器，不能如正文声称强制policy equivalence；large c的文字解释也与不截断可恢复Eq14的方向不一致。
- **Limitations：** §11含测量、proxy Goodhart、观测不完整与recovery自身风险；概念合同不证明实现或正式保证。上述中央公式/解释冲突不能用已有章节覆盖标签抹去。
- **Books：** 保留原6分，纠错触发深入必要范围；`争议/暂缓`，不写入Books、不作为正面保证。重开需作者纠正Eq17及clip/bias解释并明确per-token与trajectory范围。root与sep21_resume_v3实际独立核准冲突；未复现实验。

## From Human Guidance to Autonomy: Agent Skill System for End-to-End LLM Deployment on Spatial NPUs

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07586v1) §IV将人工协作的NPU部署记录分为CPU参考、逐kernel、单block、全model、prefill/decode优化与集成等阶段；各阶段数值门后保留human checkpoint，最终独立context evaluator重跑数值与profile。Skill提出编译/优化，验收不由自身成功trace授予。
- **Evaluation：** §V为Ryzen AI9 HX370/XDNA2、MLIR-AIR、2048序列、Claude Code/Opus4.7，8新模型加Llama3.2-1B参考；roofline归一化利用率不等实际绝对时延。部分耗时为估计，未有去除Skill/独立review的受控因果消融；权重/KV为BF16的bytes模型亦不证明任意kernel数值等价，在线并发/SLO未披露。
- **Limitations / Books：** §VI将MoE/MLA/其他spatial devices列未来，少量human debug仍存在，独立evaluator不能被外推为防止一切reward hacking。`已有覆盖`：Ch84“Skill Compiler必须绑定Target Profile”及“reproduction boundary”正文已分别规定target-specific候选、独立held-out admission与fresh executor重执行，正好承载本次采用的边界；不为八阶段实施案例另建机制owner。

## The Routing Plateau: Understanding and Breaking the Accuracy Limits of LLM Routers

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07587v1) §4–6区分query-only预测与生成后correctness oracle：不同router可频繁交换选择却赢输抵消；data/encoder scale及task fine-tuning改进instance-level预测，不能仅靠router类别决定上限。
- **Evaluation：** 21方法/5 benchmark，§5按hard-query与paired wins/losses拆分，而非只看aggregate；§6.2–6.3中30K→300K、base→large与FT分别消融，但仍残留oracle gap。该oracle需要事后标签，不是deployable免费route；五类离线工作负载结果无生产并发、SLO或跨model-pool保证。
- **Limitations / Books：** §6.4与Appendix B保留query-only困难和后续partial generation成本。`已有覆盖`：Ch56“Cascade与Pregen Router的成本坐标不同”“效用预测与委派率预算需要分别校准”实际正文已经区分事前不确定性、逐例expert增量预测与标签authority；不把模型平均更强当当前请求必有收益。这里只用受限反证验证这项已有判断，不声称原章含本论文全部实验。

## AgentCompile: An LLM-Guided Compiler for Direct CUDA Inference

- **Identity / Method：** `arXiv:2606.07665v1`；§2–§3。LLM 只给 metadata、ranking 与参数建议；compiler/runtime 构造 bounded candidates，负责模板、静态检查、验证、benchmark 与 fallback，不让 LLM 直接准入可执行 CUDA。
- **Evaluation：** §4；A800 SXM4 80GB、FP16，Llama3.2 1B/3B 与 Qwen3 1.7B/4B，输入 128～40960、输出 32～32768；full hybrid 相对 vLLM 约 1.06～1.07×，消融未独立隔离 LLM guidance。
- **Limitations：** §7；prototype、Transformer region、unsupported fallback，搜索不保证 optimal。
- **Books：** `已有覆盖`，owner=`INFER-TENSORRT-LLM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## Fast LLM-Based Semantic Filtering: From a Unified Framework to an Adaptive Two-Phase Method

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08090v1) §3–6将cluster voting的已标注样本复用于proxy训练；mixed clusters触发第二阶段，另取score-stratified校准，再对全语料重打分；训练、校准、oracle fallback与proxy成本共同结算。设计不是“cluster全同票即真值”。
- **Evaluation / Boundary：** §8三10K-document语料及各20 query，以固定oracle label为truth；oracle相对accuracy不等外部正确性。§5.2的经验率与Clopper–Pearson上界加权仍小于完整上界，不能据此宣称同置信水平保证；§5.5的独立Bernoulli/同分布条件也不消除训练使用校准集带来的依赖。实验95%query达目标不是全query硬SLA。
- **Books：** `仅报告`：成熟token interaction、两阶段复用与校准启发式的组合提供受限成本案例，但未支持更强概率保证。Ch56现有流式semantic predicate段已有label authority、质量—委派成本与失配升级原则，不把此blend写成新的形式保证；原6分标准审阅保留，不因为本轮不采用而删候选或降分。

## FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09079v1) §2训练query-side低秩indexer，对冻结compressed keys作Sigmoid阈值lookahead；离线未来window目标、跨layer筛选与每64 decode step更新，把冷CPU chunks按预测迁回HBM。HCA及recent/decode窗口仍保留，不是常数总cache。
- **Evaluation / Counterevidence：** §3.1–3.3固定所述DS-V4骨干/保留路径；context-independent请求的绝对保留仍随长度增长，MRCR严重退步，golden-chunk oracle也不消除密集全局依赖。短训长测的失败不能由pointwise打分形式排除，文中“恰好2倍”只属于该测例，不是一般理论边界。
- **Books：** `已有覆盖`：Ch45“隐式lookahead”正文已绑定future-importance target、selector identity、kept indices与未知query回退，CPU可恢复tier已有独立owner。此案例验证这些具体适用边界，不把局部headline或固定layer sweet spot写成普遍部署recipe；未复现，benchmark性能不推production SLO。

## Beyond FLOPs: Benchmarking Real Inference Acceleration of LLM Pruning under a GEMM-Centric Taxonomy

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09080v1) §3–5/B按GEMM M/N/K及static/dynamic拆pruning，通过真实operator replacement和统一profiling解释删FLOPs与可执行工作不同；额外projection、selector、GEMM分解与非GEMM成本可抵消理论收益。
- **Evaluation：** Llama3.1-8B/RTX Pro6000(sm120)，CUDA graph、尺寸16对齐，零样本最大4096评测；不同family训练预算非同一条件：dynamic M需更多steps、static K不能vanilla LoRA merge。throughput的shape模拟/单step计时不能与真实production请求队列等同，precision及线上concurrency/SLO未披露不补造。
- **Limitations / Books：** Limitations排除MoE、Hopper/数据中心Blackwell并说明高层DSL与hand CUDA差异。`已有覆盖`：Ch66的runtime/configuration-conditional evidence与Ch49硬件/FLOPs及单kernel≠完整Serving正文已承载实际采用命题；不同family的质量—成本frontier是局部证据，不采用普遍最优pruning排名。

## Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09138v1) §3.1–3.3、4.1–4.5：Gateway 接黑盒 model calls/白盒 callbacks，Data Pool 持久保存 tokens、reward、trajectory relation、policy/source metadata；ready batch 由 trainer pull，prefix-tree 合并共享前缀但各步 reward/训练语义仍独立。
- **Evaluation / Boundary：** §4 是 dashboard demo，不是质量、吞吐或 RL 收敛对照；未披露可支持性能数字的模型/硬件/precision/长度/并发/SLO。可见数据不证明 reward 正确、完整轨迹兼容或任意算法无偏。
- **Books：** `已有覆盖`，`TRAIN-GRPO` 的“Agent RL …不同终态”和“从 Opaque Harness Call 到可训练 Trajectory Tree”实际承载 token lineage、版本/环境/reward completeness、共享prefix与独立训练消费。采用数据接口分责，不采用未验证的效率承诺；标准审阅及 sep22_resume_v3 必要来源→具体既有正文独立复核通过，不代表整日日级通过。

## Resource-aware Computation-Communication Overlap for multi-GPU ML Workloads

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09200v1) §3.1–3.3：用每block shared-memory占用塑造 GEMM residency，双stream/event维持依赖，给 collective 较高priority以减少尾部；priority不是抢占保证。
- **Evaluation / Counterevidence：** §4.1–4.3：4×A40/A100/H100与8×MI250X，896MB collective；GEMM 8192×8192×8192或8192×57344×8192，64×64×{32,64}tiles。高block数MI250X可更慢，communication priority的收益可被compute residency损失抵消。作者kernel/collective实验不是完整model训练质量或线上SLO；precision未披露不补造。
- **Books：** `已有覆盖`，`TRAIN-DISTRIBUTED-TRAINING` 的“Overlap不是免费隐藏：Communication与Compute共享资源预算”实际解释共同争用、critical path、资源分配及profile/fallback。采用条件性overlap，不采用跨GPU通用提升；标准审阅及 sep22_resume_v3 必要来源→具体既有正文独立复核通过，不代表整日日级通过。

## From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09508v1) §3–4：分块observation attention的entropy区分head行为，动态head按entropy变化分配读取预算，rigidhead固定额度；生成Nd个tokens后再用output-query选择decode留存，区别于prefill末尾query proxy。entropy是选择sensor，不是未来无损证书。
- **Evaluation / Counterevidence：** §5：Llama3.1-8B/Qwen2.5-7B，单H10080GB、192GBCPU/8cores；LongBench/InfiniteBench，延迟改写needle为summary并生成100tokens。作者prefill2048/decode1024与StreamingLLM4096+4sink不等统一预算，precision/线上concurrency/SLO未披露。§4.4保留小系数N²项，“近线性”不能改写成渐近O(N)。短context profiling成本限制收益。
- **Books：** 保留6分，中心争议触发深入：`争议/暂缓`。exact HTML Algorithm3 L14/PDF p5 L12 的 `max(min(Bi,B0),3B0)` 在正 B0 下恒为3B0；§3.1 entropy 集中/均匀定义与 dense/near-deterministic 分类说明不一致。sep22_resume_v3 独立确认。不用于正面证据、Books或性能保证；重开需作者修正算法与分类并给出实现/实验对应。

## BUDDY: BUdget-Driven DYnamic Depth Routing for Adaptive Large Language Model Inference

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09514v1) §4.1–4.4：first-layer KV作为prefix sensor，scorer+offline prior选top-k中间层，首尾层始终执行；无指定budget时GRPO predictor提议depth，decode可逐token改变路径。
- **Evaluation / Counterevidence：** §5.2.1/D.4/D.5/C.2/Limitations：Llama3-8B/Qwen2.5-7B、V10032GB/A10080GB配置，Alpaca/SAMSum输出128tokens；轻剪枝routing/gather-scatter可抵消节省，decode固定路径可更快，GSM8K大幅质量损失。全部weights仍驻留，batch异路径导致skipped-layer cache miss，论文以zero-fill表达未执行状态，不是exact完整cache。precision、input长度/batch/concurrency/SLO未完整披露。
- **Books：** `整合`：`INFER-TENSORRT-LLM` Ch49 early-exit 后已写逐 token layer-path、缺失 KV/zero-fill、routing 代价与固定路径回退。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过。

## FuseFSS: Efficient Secure LLM Inference with Function Secret Sharing

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09551v1) §3.1、4.2、Theorem4.6/4.7：spec-compatible scalar gate把masked comparison和interval coefficient payload编成至多两次noninteractive backend interface evaluation；仍有Horner/Beaver乘法、fixed postprocessing和域转换，vector reduction另由MPC处理，不是整模型仅两次通信。
- **Evaluation / Security Boundary：** §6.1–6.4/B.4：两server各RTX PRO6000 Blackwell/EPYC9654/CUDA13；BERT/GPT、32–512token；LAN/WAN延迟为投影非真实WAN测量。gate-level semi-honest、至多腐化一方/non-collusion，显式shape leakage与fresh uniform masks依赖primitive/subprotocol安全。compiled program可复用但每inference的keys/masks/triples一次性；padding消除mask-dependent shape增加离线/在线成本。未复现、未证明malicious安全或任意Transformer统一收益。
- **Books：** `整合`：`PLATFORM-SECURITY` Ch72 隐私推理分支实际加入 compiled shape 与每执行 fresh preprocessing 分责、非共谋威胁面及 padding 代价。6分知识缺口深入；sep22_resume_v3 源→owner与实际正文/邻接写后通过。

## Rosetta Memory: Adaptive Memory for Cross-LLM Agents

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07711v1) §3.1–3.2 Eq1–3/4.1–4.2：writer按source model profile将本步observation/action形成memory entry，reader按target profile和当前observation从bank构造使用context；二者不能互换。Flan-T5-small soft-prefix双模块，reward-filtered expert iteration保留topα，并以minimum gain偏置抽样跨模型组合。sep22非作者定点核验纠正了初稿中read/write角色写反的问题，纠正后才写入Books。
- **Evaluation / Boundary：** §5.2–5.6/Implementation Details，六种API profile、Hotpot/2Wiki/MuSiQue，normalized containment及GPT-5.4-mini judge并非exact match或独立真值。held-out API transfer限所测混合；reader移除在部分任务仍竞争，η过强会降益，硬件、precision、并发/SLO未披露。
- **Books：** `整合`：`AGENT-MEMORY` Ch77 late construction 后实际加入 source writer 与 target reader、迁移训练成本/局部反例/固定模型回退。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过；初稿角色纠正在写书之前完成。

## Decision-Aware Memory Cards: Counterfactual-Inspired Context Selection and Compression for Tool-Using LLM Agents

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08151v1) §3.1–3.6：用反事实启发的action/outcome/necessity/negative-transfer效用选结构化cards；selection前压缩可改变选中ID，selection后只压缩同组证据。图/provenance/schema审核不证明因果识别或语义忠实。
- **Evaluation / Boundary：** §4–5/7，SWE-bench Verified仅file-level 50例；Codex-5.5仅5例。合成Repo设置中generic summary可强于cards；postselection节省tokens不等task增益。stale/harmful证据仍会被选，MLP/QLoRA拟合agreement不等真实任务质量，API硬件/precision/SLO未披露。
- **Books：** 仅报告：保留局部selection/compression反证，不把counterfactual-inspired打分写成因果或通用Memory增益。Ch76既有retrieval relevance与answer utility分责继续成立；原6分标准审阅，不因不改书删候选，非作者复核待完成。

## Causal Agent Replay: Counterfactual Attribution for LLM-Agent Failures

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08275v1) §2–3/5–7：固定prefix与mock tool环境，对action/observation/context/policy做干预，K次随机continuation比较outcome分布，并以same-policy resample作null；总效应不是直接效应，承诺点与Shapley估计受预算和方差约束。
- **Evaluation / Boundary：** §5在planted SCM ground-truth上验证归因，API temperature=0也不能保证重放相同；本地seed与action-match仅受控域。common random numbers列未来，judge outcome有噪声，真实不可逆tool/外部effect不在mock replay保证内。
- **Books：** `整合`：`PLATFORM-TRACE` Ch69 prefix-preserving replay 后实际加入 same-policy null、随机 continuation/CI、总效应非直接效应及不可逆操作边界。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过。

## Autonomous Incident Resolution at Hyperscale: An Agentic AI Architecture for Network Operations

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09122v1) §III/IV：Intake→Planning→带锁/授权Execution→health/bake-in Verification与rollback；typed skills限blast radius，at-least-once ack消息不等exactly-once effect。
- **Evaluation / Boundary：** §VI/VIII，>90%、hours→minutes及zero critical等无可核sample窗口、分母、matched comparator或不确定性；model、hardware、precision、并发/SLO未披露。范围仍是有限network incidents，formal verification与跨域扩展为未来。
- **Books：** 仅报告：architecture提供运维实现背景，未支持新的可靠性保证；不把其headline写为生产事实。Ch84已有action authority、bounded capability、rollback原则，不能仅凭主题将整篇宣布已覆盖。原6分标准审阅，非作者复核待完成。

## Anything2Skill: Compiling External Knowledge into Reusable Skills for Agents

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09316v1) §3–4：taxonomy prior引导资源抽取，生成skill contract并与registry reconciliation，versioned SkillBank投影层级检索；程序性skill与declarative RAG共同消费，源文档不因此获得执行authority。
- **Evaluation / Boundary：** §4.1/§5命令行任务success对照分别检验无task-time retrieval和skill+RAG；不证明所有资源可安全执行或跨harness泛化。未披露的硬件/precision/并发/SLO不补造；只采用结构化资产分责，不采用通用效能倍率。
- **Books：** 已有覆盖：Ch84“Resource和trajectory…不能共享无类型summarizer”实际含typed tuple、provenance/schema/dedup/permission/smoke-test、temporary pool、held-out admission与publish/rollback。该处承载采用命题而非论文全实验；标准完成，非作者复核待完成。

## What Should a Skill Remember? Quality--Cost Trade-offs in Cost-Aware Skill Rewriting for Language Model Agents

- **Identity / Method：** `arXiv:2606.09421v1`；§3。profile task/skill 后选择 source-native、workflow、API/code、rule/formula preservation anchor，并审计缺失 anchor；目标是受约束的 quality–cost utility，而非最短 rewrite。
- **Evaluation：** §4；SkillsBench 88 skills、86 runnable，固定 task/environment/verifier，覆盖 Gemini 3 Flash/Pro、GPT-5.4 Codex 与 Claude Opus 4.6；held-out total cost -7%、downstream token -6%，cross-model 均值约 -14.7%/-13.7%。
- **Limitations：** 受控 textual skills；不覆盖动态资源、持续更新 skill、生产 latency/pricing/caching/hardware 或人工复核，lightweight audit 不能替代人工安全审阅。
- **Books：** `已有覆盖`，owner=`AGENT-PLATFORM`；当前正文覆盖对应 state/control/evaluation contract，new Integrate=0。

## AliyunConsoleAgent: Training Web Agents in Real-World Cloud Environments via Distillation and Reinforcement Learning

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09447v1) §3.2/4/5.1–5.2：SoM+DOM观测；隔离account/sandbox，META记录资源create/verify/destroy依赖，ResourceCoder按需provision。环境缺资源应区别于policy失败；group/batch两级normalization、σ=0跳过改变训练语义。
- **Evaluation / Boundary：** §6/7.4，400单动作×3runs；278任务/12产品含76标准202hard，相同环境3runs pass@1与any-pass@3分开；two-judge/human对齐不保证ORM无false positives。32B仍gray test，旧frontier线上数据与projected成本不等32B生产实测。DOM维护/provision成本与环境真实性限制收益。
- **Books：** `整合`：`TRAIN-GRPO` Ch33 service 环境后实际加入 create/verify/destroy 资源前置条件、provision失败与policy失败分账及成本/旧固定环境回退。6分知识缺口深入；sep22_resume_v3 源→owner及实际正文/邻接写后通过。训练 admission/cleanup 记录是工程推断，不冒称作者已实现收据系统。

## Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents

- **Identity / Method：** `arXiv:2606.09483v1`；official export PDF §2 Method、§2.1 Cognitive Capability Hierarchy、§2.2 Synchronous Daytime Writer、§2.3 Asynchronous Nighttime Sweeper、§2.4 Read Path and Latency。
- **Evaluation：** §3 Experiments，含 §3.1 Setup、§3.2 Main Results、§3.3 Ablation 与 §3.4 Analysis。
- **Limitations：** 独立 Limitations；只覆盖披露的 vector store、benchmarks 与双进程 memory implementation，不外推到未列模型、真实用户隐私、并发或生产 SLO。
- **Books：** `已有覆盖`，owner=`AGENT-MEMORY`；当前正文的 episodic/semantic consolidation、在线写入/离线归并、visibility/commit 与读路径已覆盖。

## SecureClaw: Clawing Back Control of LLM Agents

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09549v1) §3.1–3.3：untrusted runtime只能planning；gateway把plaintext存trusted handle store，以caller/session/TTL/object/sink绑定opaque handle。bounded schema summary是显式declassification。executor独占effect sink，重算canonical request digest并核freshness/replay/confirmation后commit。
- **Evaluation / Boundary：** §4.1/6，ASB/AgentDojo/AgentLeak同harness；AgentLeak仍16/496 leakage、AgentDojo4/629 ASR，不能声称zero所有风险。可信gateway/policy/executor、完整sink mediation和字段分类为前提；合法动作语义错误/summary泄漏/utility损失未消除，未复现实验。
- **Books：** `整合`：`PLATFORM-SECURITY` Ch72 在既有 handle/授权论证内补齐读侧 plaintext 驻留于 trusted store、caller/session/TTL/object/sink 绑定，以及 bounded summary 的显式 declassification；executor 的 effect 授权保持独立。必要知识缺口已深入核验，sep22_resume_v3 源→owner及实际两段/邻接写后通过；不采用跨部署安全保证，不代表整日日级通过。

## Collaborative Human-Agent Protocol (CHAP)

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09751v1) §4–8：workspace/participant/task/audit接口，accepted envelope原子推进authoritative task projection与event；human override记录base/diff/reviewer identity，rollback追加corrective evidence而非删史。
- **Evaluation / Boundary：** normative protocol/reference v0.2不是实测性能或法律合规证明；optional Ed25519/SCITT只绑定身份/日志，不证明override正确。shadow/trial/production policy不同，append-only原始敏感数据仍需治理，concurrency/SLO未披露。
- **Books：** 已有覆盖：Ch81“对象已保存→状态已激活”实际规定predecessor authority、revalidation和Commit/Reject/Quarantine/Defer，event persistence/approval与compensation也有独立职责；Ch84 human consent仍不是truth。采用该已有合同，不宣称原书含每个API；标准完成，非作者待完成。

## VisualLeakBench: Reproducible Action-Boundary Propagation Failures in Vision-Language Agents

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07595v1) §2/4–5：将image中标为non-propagatable的字符串是否进入tool argument，区别于chat response泄露和真实downstream harm。按no tool/safe tool/response-only/tool-only/both拆trace分母。
- **Evaluation / Boundary：** §4/8每model/scenario通常50，parse-error格用非error45/47/49/42/46不可混同；simulated单步tool未执行effect、无multi-turn recovery。PII prompt多靠抑制tool use降传播，不能由低ASR推utility保持或全链安全。
- **Books：** 已有覆盖：Ch72实际typed tool/action boundary、最小数据暴露与effect授权段已要求同时审查参数和输出，benchmark补充受限验证而不授新安全保证。6分安全约束必要范围深入，非作者待完成。

## Finite Certificates for In-Context Determinacy and a Threshold Theory of Emergence in Language Models

- **Identity / Theory：** [exact-v1](https://arxiv.org/html/2606.07623v1) §2–6外置many-sorted first-order semantic presentation，prompt约束/preference与decoder kernel分开；compactness下有限certificate、finite deterministic task family pair separator、finite-field rank见§4–5，不是Transformer内部实现或任意LLM的可计算证书。
- **Evidence Boundary：** §6的latent-confidence与不连续metric threshold是数学构造；不提供参数模型可识别的语义measure、可操作oracle或真实model calibration实验。有限certificate存在性不等有效求解/小样本可学；不能据此声称解决hallucination或必然涌现。
- **Books：** 仅报告：保留逻辑/解码/指标的区分及严格假设，不将外置语义模型当已验证模型机制。原6分标准理论审阅，非作者必要定理与边界复核待完成。

## SWE-Marathon: Can Agents Autonomously Complete Ultra-Long-Horizon Software Work?

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07682v1) §3.1–3.3/4.1–4.4：Harbor容器最终状态与hidden verifier计分，visible development feedback分离；reference oracle/no-op/exploit search构成task admission。CLI产品与固定Terminus scaffold不同，不是只比较模型权重。
- **Evaluation / Counterevidence：** §5，20tasks×13configs×5=1300rollouts，2–10h、CPU/内存/GPU按task，pass@1及binomial SE；human expert时长是估计。failure分析仅10task subset，141infra+79证据不足被隔离，526分类不等全部1300独立判断。post-hoc judge嫌疑不是作弊因果证明，cached/API costs与context/provider配置不同。
- **Books：** 已有覆盖：Ch66 actual harness/model/environment identity与agent process/effect评价、Ch84 held-out independent executor已承载采用判断。受限长任务验证不证明开放任务成功率，也不把新suite当新owner；标准完成，非作者待完成。

## When Behavioral Safety Evaluation Fails: A Representation-Level Perspective

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.08044v1) §2–4 / dissociated construction / KL note / §7：在保持回答拒答的 SFT+KL 约束下，另用 harmful-prompt indicator 和分离 optimizer 改变隐状态 probe 的可分性；标签不是逐回答的真实危害。行为不变与表示分数改变可被人为解耦。
- **Evaluation / Boundary：** Gemma2-2B、Llama3.2-3B、Qwen2.5-3B 和固定 HarmBench/probe；受控白盒构造不证明黑盒生产攻击，probe 层、prompt 前缀、训练分布改变可改变结论。未验证任意 detector，未复现。
- **Books：** 已有覆盖：`PLATFORM-SECURITY`；拒答行为与representation probe可解耦；版本化sensor不拥有真值。源→owner及具体已有正文已由 sep22_resume_v3 独立通过，整日日级Gate另验收。

## Decoy-Calibrated Failure Audits for Language Models

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09046v1) §2.1–2.3：冻结错误标签与 descriptor library，置换每个描述子的布尔成员保持 prevalence，用同一 lift/support 规则比较真实与假 descriptor；经验 FDP 阈值后固定 survivor，再要求 holdout 支持、同方向和最小绝对 lift。
- **Evaluation / Boundary：** §3–5：Claude Haiku4.5，controlled multi-table 与 MuSiQue/LongBench v2；后两者不确认任何 finding。单 descriptor 置换不保持联合相关，估计 FDP 不是 finite-sample FDR；不能把零 finding 当错误不存在或相关当因果。硬件、precision、服务 concurrency/SLO 未披露/非此比较目标。
- **Books：** 整合：`PLATFORM-EVALUATION-SYSTEM`；假descriptor经验底线→冻结幸存集合→holdout；非FDR/因果。源→owner及实际两段/邻接写后已由 sep22_resume_v3 独立通过，整日日级Gate另验收。

## REFLECT: Intervention-Supported Error Attribution for Silent Failures in LLM Agent Traces

- **Identity / Method：** `arXiv:2606.09071v1`；§3。诊断 candidate 后执行 prefix-preserving targeted replay；diagnosis-specific faithfulness gate 阻止无关恢复，失败时 verified rollback，并以 contrastive explanation 更新诊断。
- **Evaluation：** §4；WTQ 137/119、GAIA 117/83、BBM 150/150、SWE 31/30，gpt-5.2 auditor/agent、temperature=0；主实验使用 oracle expected answer 与 exact-match localization。
- **Limitations：** Appendix R；结构化环境、oracle 依赖、不可逆副作用与缺失环境会阻止 replay；只处理 single earliest decisive error。Outcome flip 支持 intervention 的充分性，不证明归因唯一或最小。
- **Books：** `整合`，owner=`PLATFORM-TRACE`；实际正文写入 prefix preservation、diagnosis-specific faithfulness gate 与 sufficiency/non-uniqueness 边界；`AGENT-REFLECTION` 只保留短 handoff。sep21_resume_v3必要来源、实际写后与邻接独立通过。

## Precision Is Not Faithfulness: Coverage-Aware Evaluation of Grounded Generation with a Complete Oracle

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09376v1) §3–6 / §8 / §11：FastF1 结构化提取生成 race facts oracle；将输出 claim 分成 supported/contradicted/unverifiable，同时核对目标事实覆盖，verifier-guided edit 补漏。所谓 complete 仅限派生 schema/fact types，非所有实体、因果或自然语言含义。
- **Evaluation / Boundary：** 7253 构造样本与207 test/season holdout；完整性提示可使 recall 从.60降到.47，部分模型反向变化。抽 claim 漏检、过拆分与 oracle 派生错误都是 evaluator error；提高 precision 可能只是删 claim。非开放世界 gold、未复现。
- **Books：** 已有覆盖：`PLATFORM-EVALUATION-SYSTEM`；atomic precision/目标事实coverage与派生oracle的有限完备性。源→owner及具体已有正文已由 sep22_resume_v3 独立通过，整日日级Gate另验收。

## WeaveBench: A Long-Horizon, Real-World Benchmark for Computer-Use Agents with Hybrid Interfaces

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09426v1) Task Admission / P1–P3 / Main Results / Failure Analysis：114任务按通道不可替代、交错及跨 app admission；冻结 Linux VM/任务材料，judge 新进程重新取实际 artifact、评估 clause 与过程维度，防只看 final claim。
- **Evaluation / Boundary：** GUI-only/CLI-only 低分受 task construction 必须混合通道影响，不证明通用界面优劣；harness/model/thinking budget 和 best setting 不全可比。final-only 重打分差额不是识别出的真实 cheating 因果率，judge 并非独立 human gold，timeout/context overflow须分账。
- **Books：** 仅报告：保留受限任务 admission 与 artifact re-fetch 的实现案例；不把一个 benchmark 的混合通道需要升为普遍架构条件，也不以 Ch66 同主题冒充具体机制已覆盖。

## H2HMem: A Multimodal Memory Benchmark for Agents in Human-Human Interactions

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09461v1) §3–5 / annotation：human directors+LLM scripts 构造有 speaker/time/modality 归属的多会话内容，人工问答检验 current facts、更新冲突与跨人引用。memory retrieval 与归属/更新可分。
- **Evaluation / Boundary：** dyadic/multiparty 会话密度、长度不相同，不能归因 participant 数；caption+text 与 multimodal 输入信息不同。human200 子集 judge κ=.84 不覆盖全体；100 selected failures 的 misalignment/speaker 比例非总体频率。memory build 与 query inference 延迟不横比；模型为所测 Qwen2.5VL3B/7B/GPT4.1nano。
- **Books：** 仅报告：受限 benchmark 暴露归属/更新误差，但尚未支持新的 memory 改进机制或通用因果结论。保留6分标准审阅，不因不改书删除候选。

## Multi-Turn Evaluation of Deep Research Agents Under Process-Level Feedback

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09748v1) §3 / §4.1–4.4 / §5：LC-ODR 每轮重新 plan/search/report，RGI 从固定 rubric 给 process feedback；将新 criterion incorporation 与已满足 criterion regression 分开，不能只看总分增长。
- **Evaluation / Boundary：** 50 DRACO任务/10域、三轮、三配置，反馈 GPT4.1、评判 GPT5.2/Tavily 检索设置。不同 criterion 分母不能直接横比净率；Turn3 非单调，rubric/反馈/评分共用 gold 与 API budget 限制独立性。案例不证明长期自改善。
- **Books：** 仅报告：保留反馈收益与旧 criterion 回退并存的受限证据；不将既有迭代流程新命名作为机制，也不把自动反馈的本地增益写成跨任务可靠性。

## iOSWorld: A Benchmark for Personally Intelligent Phone Agents

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09764v1) §3 / Evaluation / §4.2：26 cloned native apps、固定 persistent user state，133 tasks 分 single/multi-app/memory；运行50step后按实际交互结果 judge。Vision+XML 有额外访问面，非同信息纯视觉对照。
- **Evaluation / Boundary：** API computer-use 系统与 Qwen35B/vLLM 设置不同，closed/open 与 harness 混杂；128human subset κ=.77不提供全部gold。分任务成功率不相乘为综合概率，step budget failures 不等规划不能；cloned simulator 不证明真实手机权限/生产隐私。
- **Books：** 仅报告：任务/环境实现与失败诊断有上下文价值，但不产生新的长期 Agent 执行机制或跨模型能力排序。

## MC-PDD: Masked Corpus-Level Pretraining Data Detection for Black-Box Large Language Models

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.07996v1) §IV–VI / limitations：按实体/TF-IDF 挑 corpus-specific words，遮盖后黑盒候选补全，用语料级 hit 差异与 reference/non-specific baseline 比较；无需 logits，不是逐记录 membership oracle。
- **Evaluation / Boundary：** SteamMIA 有标记参考语料，Llama3.1 instruct 与10次重复；API release date proxy、BBC 年份不能确认旧语料必然 member。OLMo arXiv 某些设置区间/差异不显著；topic/time/word uniqueness、shadow/reference 差异可解释效果，需 instruction 能力。
- **Books：** 仅报告：保留概率性 corpus 检测在身份核验中的限制，不把统计线索写为法律归属或已知 pretraining provenance；原6分不改，未核验代码/未复现。

## Benchmarking Empirical Privacy Protection for Adaptations of Large Language Models

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09401v1) §2–4 / §5 / §7：固定 pretrained checkpoint，仅对 adaptation 集执行 DP；分别测 full/LoRA/prefix/head、IID/overlap/OOD、不同 shadow/attacker knowledge。被保护邻接单位是 adaptation 数据，不是固定 pretraining 历史。
- **Evaluation / Boundary：** Pythia/GPT-Neo/OLMo 70M–1.4B 的公开参数/概率攻击，utility 与攻击接口、shadow 匹配一起改变实测 MIA。相同 ε不保证相同经验 attack rate；高攻击分不等 DP 数学失效。当前图表未完整核数字，不采用数值排名、closed API 外推或 unlearning 保证。
- **Books：** 整合：`PLATFORM-SECURITY`；adaptation DP邻接不追溯fixed pretraining；MIA与accountant分账。源→owner及实际两段/邻接写后已由 sep22_resume_v3 独立通过，整日日级Gate另验收。

## Now You (Still) See Me: Detecting Evasive Steganographic Payloads in LLMs

- **Identity / Method：** [exact-v1](https://arxiv.org/html/2606.09411v1) §3–5 / Appendix F：将32bit secret 映射到固定 output embedding 的 token buckets，受限 teacher 生成 SFT 数据，输出 embedding 冻结；定期重拟合的 detached ridge probe 可被 evasion 训练绕开，同时以 bucket NLL/KL 保留 payload。recontextualization 冻结模板/改变话题以压低无关变化。
- **Evaluation / Boundary：** 五类开放8B/14B模型与短固定secret/白盒训练，不覆盖任意 detector/未知生产攻击。nuisance slack 是有假设的理论/代理，不是实测完整熵；Appendix F 明确代理 KL 不约束任意完整表示探测器。信息可恢复不等实践中有稳定通用检测器。
- **Books：** 整合：`PLATFORM-SECURITY`；受控recontext检验nuisance捷径；proxy KL非完整检测保证。源→owner及实际两段/邻接写后已由 sep22_resume_v3 独立通过，整日日级Gate另验收。
