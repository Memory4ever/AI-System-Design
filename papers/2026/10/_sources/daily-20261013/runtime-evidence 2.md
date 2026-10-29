# 2026-10-13 Daily：runtime / generation / Agent 定点证据

执行者：today_runtime。窗口仅北京时间2026-10-12全天；历史暂停，不生成Weekly。assigned16的Mon12官方公告身份复用root已核有效层，精确v1完整题摘本轮实际读回。当前为分批工作记录，不代日报或独立验收。只维护本文件；Books写入须root先独立Source/PRE复核并授独占窄锁，报告/LS/index不由本执行者改动。

**批一终态：**13708/13778/13325的必要Source/PRE经root独核，实际Ch45两处/Ch42一处正文与本人三末注已写；root已完整局部正文/邻接/末注非writer POST通过，本人仅同步三注并回读，两个窄锁已释放。13060具体已有覆盖经root原证/正文复核通过。以下早期“待核”描述仅记录当时层次，不覆盖此终态。

**批二终态：**13605/13485/13321/13375 Source/PRE经root独核后实际Ch11/82/27/66各一正文/一注；root实际正文/邻接/本人注非writer POST通过，本人四注同步回读与限定diff-check通过，四窄锁释放。

**作者最终冻结层：**本作者23唯一候选＝原19＋尾generation3＋停止时灰标题13935；20项真实Books整合、3具体已有覆盖（13060/13303/13935）。全部必要受限Source/owner处置经root独核接纳，20实际正文/完整邻接/本人注root非writer POST均通过，作者注同步回读及限定diffcheck通过；所有窄锁已释放。13935最后必要Source/actual Ch66 NC packet已root实际读回接纳，统计冲突精确隔离。作者普通待办0，发现停止，不代全日报DAY。新增12970为贡献前EX不进23/评分；9系统/6VLA/尾2的候选处置归其他指定owner，不重复计入。root全日报另冻结60＝53实际整合＋6具体NC＋13816必要证据隔离1，尚待today_institutions非Report作者DAY；本作者不修改Report/LS/index。

## 批次一：必要Source完成，PRE待独立核

### [ReplaySSM — 2610.13778v1](https://arxiv.org/html/2610.13778v1)

准入：逐步全量物化SSM state使IO、speculative rollback及误差递推耦合→缓存输入、周期checkpoint、output-only及两种精度角色分离→改变state写回与rollback设计。评分2+2+3=7，深入完成（非复现）。实际读§3–6 Eq4–6/Alg1–3、§7.1–7.4/T1–2。只flush committed inputs，环容量L+T，acceptance后仅推进cursor；GDN低精生成的u须在高精flush时用缓存v重算。误差隔离不等于零误差：高精路径及当前低精read仍有误差。四hybrid模型/单H100或B300/无TP，性能用FP32 state、L16、B256；标准decode收益B1近零，speculative T4/GSM8K/256输出tokens，低精quality另测teacher-forced PG19及三任务，不合并速度与精度宣称。

Owner `INFER-KV-CACHE` Ch45，已实际读§“Recurrent State也需要写回与回滚协议”及前后邻接。现有dense base+log覆盖周期物化，但未说明accepted-input buffer、output-only与高/低精角色隔离。拟在现有DeltaLog段之后、应用层abort段之前融入两段，不写Ch48重复owner。PRE文本另发root，未写Books。

### [GraphTok — 2610.13325v1](https://arxiv.org/html/2610.13325v1)

准入：高prefix reuse省掉prefill但全文tokenization仍在lookup前→按family predicate保序pretoken/BPE、预分配graph区分capacity/occupancy→frontend成为独立capacity及exactness决策。评分2+2+2=6，因Ch42具体长期缺口深入。实际读§2–4核心、§6.2–6.3 correctness/对照、§6.10 sharing、§6.12限制；NFC/config识别/truncation仍在graph外，五具体配置不是任意tokenizer支持。只等token数或decode文本不等reference IDs；CPU fallback适用短输入，现有safe-boundary token缓存仍成立。单H100 NVL/vLLM实测与Dynamo模拟GPU前端容量分开；模拟关闭prefix tokenizer cache，不证明multi-GPU端到端TTFT或任意共享负载无干扰。

Owner `INFER-REQUEST-LIFECYCLE` Ch42现有frontend归一化和TTFT拆分，只提tokenization语义/时延，缺prefix hit后CPU stage主导及fixed-graph执行合同。拟在Frontend段后最小插入一段，PRE待root独核；未写Books。

### [KV-Repurpose — 2610.13060v1](https://arxiv.org/html/2610.13060v1)

准入：prefix键不能共享不同前文下同document→naive segment reuse公开跨document推理失效证据→校正“cache hit等价质量”的设计判断。评分2+2+2=6；设计反证触发深入受影响部分。实际读§2.1、§4.1–4.4/T1–2及§3.2：unrotated key重新RoPE只对齐位置，不重算前文attention；单GPT-OSS-120B/H200/vLLM0.20/NVMe，LongBench/Pro与三次run，伪retrieval固定相关文档，multi-document过滤仅部分恢复。Zipfian2500请求/30GB/20%固定datetime前缀的命中63.9% vs3.3%属合成负载，不外推production。

Books拟已有覆盖（具体NC）：`INFER-KV-CACHE` Ch45 §“非Prefix复用必须绑定Position-aligned Segment与Correction State”（当前1681–1690附近）明确positional/context conditioning不同、边界选择性修正、approximate标记及exact重算回退，下一§“KV intervention必须冻结Layer Scope、Position与Conditioning”也分开position与conditioning。新反证加强而不改变该论点，不添加论文摘要或引用充当正文融入。NC仍待独立Source/正文复核。

### [Adaptive DHiSparse — 2610.13708v1](https://arxiv.org/html/2610.13708v1)

准入：fixed每request cache在低负载浪费fetch/高负载占admission→required/optional residency与speculative union staging分责→负载变时改变物理容量而保持原selector/acceptance。评分2+2+2=6，Ch45长期具体缺口深入。实际读§2–3.5核心/Eq3–11、§4评价及直接成本，未遍历附件。Optional不得借走hot/tail，copy完成才publish-ready、host backup和reader完成后才reclaim；speculative union去重copy但保各query causal selection，overflow staging按Kmax*k/source分配且读完/copy-back后才layer-group复用；draft ring仅在其原window内。额外drafter/metadata挤压index容量，optional免费页不等总成本为零。性能采GLM5.3与DeepSeekV4.1Flash作者特定长ctx/concurrency/TP配置，不授一般SLO或通用exact。

Owner `INFER-KV-CACHE` Ch45现有§“完整可寻址历史与HBM Residency可以分离”只有语义eviction vs placement和fused fetch，拟就该段refine required/optional及ready/backup/readers顺序，Ch54不重复解释。§4.1实读配置为8×B300 node、269GiB/GPU、4.3TB host/PCIe，GLM4prefill+4decode、DeepSeek2+2，100K/500K input与2048output cap；GLM FP8 KV/k2048/B4096。output除以decode GPU不含prefill，post-wave排除首C请求。§4.3.1直接反侧：C16→C256 reclaim备份使slots填满53s而off为3s，后续population恢复也慢；更宽verification并非收益更大。PRE待独核与窄锁，未写Books。

## 逐字最小PRE提案（未落Books）

### Ch45 / 13708：原addressable-history段与其来源comment之间追加

固定小 working set 在高负载下保护 admission，却会在低负载时反复从 host 取回本可驻留的历史。可把容量再分为不可借走的 hot cache、mutable tail 与 verification reservation，以及只占空闲页的 optional immutable history。分配不等于 ready：副本完成后才发布位置；回收前必须完成 host backup 并等待旧读者，确保任意历史 row 始终可在 GPU 读取或从 host 恢复。多 query 的 speculative verification 可以合并缺失 row 的搬运，但不能合并各 query 的 selection 或 causal mask；overflow staging 也只能在消费者和必要 copy-back 完成后复用。负载上升时备份、回收和重新填充会增加等待，短 context 能全驻留时反而无需这些工作。作者B300、特定模型/前缀/并发实验只支持这一受限 placement 分支，不证明一般服务尾延迟或不同 selector 的等价性。<!-- source-family:SF-2026-ARXIV-2610-13708 -->

### Ch45 / 13778：原DeltaLog来源comment后、应用层abort段前追加

当递推能展开为旧 checkpoint 加近期输入贡献时，buffer 还可以保存这些输入而非每个 draft 的完整 state：常态仅计算 output，周期 flush 才物化 checkpoint。验证先追加 tentative inputs，acceptance 后推进 committed cursor；被拒绝的尾部覆盖即可，而 flush 只能折叠已经提交的输入。这样把 speculative rollback 从全 state snapshot 改为 buffer 边界操作，但窗口越长，输入 replay 计算与缓存读取也越多。该分支依赖具体递推可展开，不是任意 recurrent model 的免费回滚。<!-- source-family:SF-2026-ARXIV-2610-13778 -->

output 与未来递推不必消费同一精度的 checkpoint：低精副本只供常态读取，高精版本负责 flush，避免低精舍入再次流入后续更新；当前 output 的读误差和高精路径误差仍存在。对 Delta-rule 更新，若近期 correction 曾从低精状态计算，flush 还须用保留的原始输入在高精状态上重算，不能只换 checkpoint dtype。ReplaySSM的单GPU hybrid模型实验支持此机制，不建立TP或所有架构保证；state小、batch低或replay代价高时，逐步物化仍成立。

### Ch42 / 13325：Frontend现有tokenizer身份段后追加

高 prefix-cache hit 会省掉多数 Prefill，却不自动省掉 lookup 之前的 tokenization：全文重新编码仍可能成为 TTFT 和共享 frontend 的容量瓶颈。可在保持模型原始 token IDs 的前提下，将 family-specific pre-token边界、保序BPE与结果组装放入预分配 GPU graph，以固定 capacity 承载动态 occupancy；仅匹配 token 数或还原文本不能证明输入语义相同。safe-boundary token复用和短输入CPU路径继续合理，GPU也要支付搬运、buffer和共享执行成本。GraphTok的五配置/单H100研究支持有限编码分支，Dynamo模拟只测前端容量；request-level template、截断及未支持配置仍须保留原有契约和fallback。<!-- source-family:SF-2026-ARXIV-2610-13325 -->

## 批二：必要Source/PRE已成熟，待独核

### [zip2zip++ — 2610.13605v1](https://arxiv.org/html/2610.13605v1)

2+2+2=6，Ch11具体长期缺口深入。实际§2–4/§5、Appendix F必要多view反侧：动态LZW hypertoken输出存在prefix竞争而input要读完整内容，shared hyperencoder冲突；解耦、base-span RoPE、protected digits及canonical-prefix下target多view评分。四LoRA模型/8000steps/同数据配置/merge4；strict gap只约一半，digit protection主导math，14B code/IF不改善，更多compressed预训练PPL好而reasoning退。多view不是全文所有segmentation marginal，无lossless质量或端到端速度证明。

Owner `MODEL-TOKENIZER` Ch11 §Tokenizer与checkpoint联合行为接口实际正文与相邻byte/local decoder已读：有多segmentation行为差异，但无dynamic codebook输入/输出角色、span position和target-score口径。拟在此节第一段后插入：

固定词表使输入与输出共享同一套 token 身份；在线动态 codebook 则让多个不同长度的合并 token 竞争同一文本前缀。输入组合需要保留整个 span 的内容，输出分类又需区分这些前缀竞争者，因此一个共享组合器可能承受不同几何目标；可分开 input/output encoder，并按原始 token span 定义位置，而非只用压缩后序号。合并 digits 等敏感单元还会改变推理质量。动态词表要另报同文本的合法切分概率：只在 canonical prefix 下汇总 target 的多种切分，不等于全文 segmentation 的联合边缘概率。它增加组合、codec和评分成本；zip2zip++的受限LoRA对照仍有代码/指令反退，压缩无损只指可还原文本，不授模型质量无损或服务加速。<!-- source-family:SF-2026-ARXIV-2610-13605 -->

### [POrchestra — 2610.13485v1](https://arxiv.org/html/2610.13485v1)

2+2+2=6，Ch82具体缺口深入。实读§3.2–3.3/Eq3–8、§4.1–4.5、B.2、E.3/G。worker pause发status/request/evidence；orchestrator revise记录进入原local trajectory或stop。OPOD将归因足够的hindsight hint给同backbone teacher、reverseKL+RWR，用户新要求不归罪原delegation。GAIA/2/SWE，Gemini/DeepSeek执行，Qwen3.5-9B编排；同300/500steps但top2每类别两次其余一次。API成本不含训练生命周期；现仅单active worker，不能外推并发。工具撤销对照/轮询连续性、task/resource及协议消融支持局部机制。

Owner `AGENT-MULTI-AGENT` Ch82 §Topology运行时有界修复，现有clone/archive与fanout预算未解释同worker mid-lifecycle harness revision及反馈归因。拟在clone/archive段后：

运行中的子 Agent 也不必等完成或报错后才重建：它可以在局部障碍出现时暂停，提交 progress/uncertainty、修改请求和支持该请求的 tool evidence；orchestrator 决定是否改 subgoal、context、tools 或剩余预算，将 revision 作为 observation 记入原 local trajectory 后继续，或显式终止。这保留执行连续性，却增加通信、版本与全局责任协调；请求本身不授权扩大用户范围或工具权限。反馈还可用于学习 delegation，但应先区分原配置失配与后来外生要求变化，仅把可归因的 hint 用作训练期 self-teacher，最终 outcome 仍单独监督。POrchestra的有限对照只执行一个active子Agent，非并发协调或普遍成本最优保证；反馈不可靠、任务稳定或副作用强时，固定配置与有界返回交接仍合理。<!-- source-family:SF-2026-ARXIV-2610-13485 -->

### [ARTS-Hybrid — 2610.13375v1](https://arxiv.org/html/2610.13375v1)

2+2+2=6，Ch66具体缺口深入。实际§3.1–3.3/T1–4、§4.1–4.3/Eq1–6、§5结果/B.2/C必要校准与反側。equal generator-call tree coverage仍增；controlled counterfactual violation树routing遮蔽leaf而path不剪枝较好。750RubricBench preference/2judges，6responses×2校准只作候选选择非final。语义validity先筛，校准分response discrimination、judge variance、criterion redundancy；仅校准可选invalid，复杂聚合收益小、Focus calibration消融近似。离线生成/评分有费，有限judge共偏与人工gold条件人口不等真值。

Owner `PLATFORM-EVALUATION-SYSTEM` Ch66 §criterion-level判断段与gold人口段已实际读，缺tree组织/执行剪枝分责。拟在现有criterion粒度段后：

Rubric 的层级还要区分组织与执行用途：父维度可以帮助生成覆盖完整的 leaf，也可作为逐 leaf 判定的语义 context；若先判断父节点再剪掉子树，一次上层漏检会让整组违规不再被检查。ARTS-Hybrid的受限对照支持保留 path context 而不依赖这种 pruning。标准写得清楚也不自动让 judge 判得准：先检查语义可接受，再用独立校准 responses 分别测 response 间区分、同response的judge稳定性与标准冗余，不能只奖励共识或更复杂聚合。校准调用和离线生成有费，标签/人口/模型变化仍需重核；可靠的固定checklist、可执行checker与独立人工anchor继续成立。<!-- source-family:SF-2026-ARXIV-2610-13375 -->

### [Host-Aware Crawling — 2610.13321v1](https://arxiv.org/html/2610.13321v1)

2+2+2=6，Ch27具体缺口深入。实际§3.1–3.5/§4.1–4.4/§6.1及Limitations。224WARC/CC2024-10约0.25%/3.01M文档/host至少3样本；10fastText（6质量4topic），full-crawl Gneiss另复核。固定fetch预算下先每host探3页再加深高score host接近oracle；HC与语言混杂，未评新增URL discovery或下游训练。估58M已知uncrawled是假定同host未抓页相似，不精确计数；低score host可能有别处链接且allocation压缩语言多样性。

Owner `TRAIN-DATA` Ch27 Quality filtering已有scorer偏差/retention分布，但没有采集前host budget选择。拟在retention段后：

选择还发生在抓取之前：有限 fetch budget 要同时决定访问哪些 host、以及每个 host 抓多深，不能把已有文档过滤分数直接当 Web discovery 能力。可先按 host 获取少量样本，再以其质量 density 提出加深预算；graph centrality 与语言、链接发现价值是另一种信号。Host-aware crawling的受限模拟只在已抓页面上比较预算分配，classifier yield 不是下游训练收益，也不证明少数样本足以代表任意host。偏向高score来源会改变语言/地域/内容覆盖，须保留探索份额与分布检查；广泛发现、未知host或scorer失配时，centrality探索与均匀/分层抓取仍合理。<!-- source-family:SF-2026-ARXIV-2610-13321 -->

## 批三：反证、sampling 与训练环境

最终有效层：13287/13171/13166 三实际正文与本人注经 root 非 writer POST 通过，作者同步注并实际回读，Ch66/20/27 窄锁释放。13303 上述具体 NC 的必要源与 actual owner 已经 root 独核通过，不增引用或正文。

### [Agreement without Alignment — 2610.13303v1](https://arxiv.org/html/2610.13303v1)

准入：以judge disagreement选rubric edits→equal-count/random未选clause对照测consensus和human alignment分离→修正共识改善即可自动修标准的判断。评分2+1+2=5，设计反证深入。实读§3、§4.1–4.6、§5/T3–4、§6–7。五judges/三provider/75criteria，先dev probing后一次局部编辑，随机对照同editor/example规则；129770requests不含retries。SummEval paired cluster-bootstrap/10000/9tests Holm：alpha+0.069但tau变化-0.007区间跨0。HealthBench/USR不达predefined effect；stage1 checker转移0，不授checker收益；no detectable不等equivalence。三English dataset/人工gold噪声、provider/size混杂、preflight修改保留。

拟具体NC：`PLATFORM-EVALUATION-SYSTEM` Ch66 §criterion粒度/gold人口（当前433–437附近）明确“judge spread缩小也不证明正确”、独立人工anchor、争议/Unknown不能被总体高分代替。§judge与用户rubric-feature段亦分开user/judge weights；本窗反证不改变这些实际论点，不加引用充当融入。待root独核。

### [Prompt Optimizer Contract Regression — 2610.13287v1](https://arxiv.org/html/2610.13287v1)

准入：single objective收益与unscored requirements退化→同prompt 200→1024cap拆出共同extraction失败→修改“每类requirement独立退化”的读法。2+2+2=6，设计反证深入。实读§3–7/T1–6；Haiku4.5task/Sonnet5.5proposer/temperature0/500calls/1–10prompts，54runs、3seeds。strict JSON vs metric first-object extraction，没object算所有content违反；1629失败全部达200tokens但原stop-reasons未存。1024cap4500 outputs全parseable、content net低而reasoning preamble仍contract违约，无post-hoc显著性；原seed格式>90%已坏、少clusters区间不稳。两gates都未满足兼顾50%violations/≤1point目标损失，不采通用gate效果。

Owner `PLATFORM-EVALUATION-SYSTEM` Ch66 成功五层表当前有contract/semantic分开，Ch74 constraint-residual段实际已读但没上游parse共因；新增归因/评价边界由Ch66拥有，不在Ch74重复。拟在五层表后、交集段前：

自动 prompt 优化还会把评分器与实际消费者的差异放大：宽松 parser 可从 reasoning preamble 后抽出答案并提高 accuracy，严格 JSON 消费者却仍拒收；固定 output cap 又可能把对象截掉。若一次上游 extraction failure 被记成引用、拒答和长度全失败，不能据此判定三种内容能力各自退化，须分开可解析人口、截断与真正内容错误，并冻结预算和抽取规则。对同一批prompt放宽cap的事后检查只能提供受限反解释，不证明普遍消除副作用。较长输出、额外回归和约束gate都有费用与误拒；稳定prompt、严格schema与独立分项检查继续合理，target metric提高不能代contract验收。<!-- source-family:SF-2026-ARXIV-2610-13287 -->

### [PreSTO — 2610.13171v1](https://arxiv.org/html/2610.13171v1)

准入：PowerMH accept/reject serial决定下个proposal→有条件共享prefix预取未来MH决策子树、保持原核→可把延迟换成未被使用的计算而不改sampler语义。2+1+2=5，Ch20具体长期缺口深入。实读§3.1–3.3/Condition1/Alg1–2、Prop1 A1–A3（必要声明非整proof）、§5、D.2–D.3及关键反侧。cut'≤cut保证prefix一致；defer保cut/random inputs且eventually evaluate；exact原acceptance、both children可能，不用预测confidence决定MH真值。预测只分prefetch budget，未抵达分支浪费。单GH200 H10096GB/Grace/vLLM0.27.1patched，首20prompts/K100/Npf20/固定1024无EOS；速度是mean model-call累计时间而非full服务。29/38 mean likelihood/confidence TOST通过不是distribution等价证明，且只在rescoring合格pairs；额外KV/废分支计费。

Owner `MODEL-SAMPLING` Ch20 power-SMC段及相邻sequence sharpness段实际读：说明目标不同与finite sampler，但无MH核与并行预取的边界。拟在Power-SMC第二段后：

Sequence power目标也可由有限步MH逼近；此时每次accept/reject确定下一状态，天然形成串行依赖。若后续suffix proposal所需prefix已经确定，可先批量生成若干未来决策分支，再沿原MH规则走实际路径；未满足prefix条件的请求延后，保留其随机输入而非重抽，未走到的分支只消耗资源。这种预取改变执行顺序，不改变每个已提交transition的proposal和acceptance；预测可分配预取预算，却不能删除可能结果或替代精确接受规则。PreSTO的受限单GPU/固定长度实验只测model-call时间，有限MH仍不等已经达到power目标；废分支、KV和更大batch成本必须另计，收益不足时保留串行MH或普通采样。<!-- source-family:SF-2026-ARXIV-2610-13171 -->

### [TerminalHorizon — 2610.13166v1](https://arxiv.org/html/2610.13166v1)

准入：可执行合成环境可能提前完成核心工作→public-only independent challenge找work gaps后重构，并依赖前步进展扩展→数据验收不能只看任务长或testpass。2+2+2=6，Ch27具体缺口深入。实读§2.2–2.3/Eq3–8、§3–4.3、F过程过滤；不采用science应用/12h案例结论。Challenger不看blueprint/reference/private tests，verifier requirements须public可发现；重构不惩罚合法高效解。1535packages/2852teacher trajectories/Qwen3.5-27B SFT3epochs/BF16/144H20，12benchmark作者局部改善；model-size/data-scale改变多个因素，没单独isolate synthesis组件。F用模型读完整trace、无reward label，不是人工真值；成功不自动收，合法错误恢复可有训练价值。

Owner `TRAIN-DATA` Ch27 executable state→trajectory→verifier pipeline及后续fail-before/pass-after段实际读，缺“构造已替solver做完工作”与public-only challenge-reconstruction。拟在该pipeline代码块后：

环境可执行、任务可通过，仍不证明预期工作真的留给了求解器：初始文件可能已经实现核心函数，只剩改常量。可让未参与构造的 challenger 只读公开instruction和环境，依据真实trace找出是合法高效解、还是构造阶段提前消解了探索/实现/验证，再重构起始状态和依赖并重试。扩展horizon应让新要求依赖此前证据、artifact或反馈，不仅加长文本；verifier也不能添加公开证据无法发现的要求。TerminalHorizon的有限训练对照支持这条数据构造分支，不证明轨迹长本身造成能力或模型review为真值。构造、challenge与重试均计费；缺独立公开视域、评价不可信或工作本已明确时，原人工任务和可核执行日志仍更稳。<!-- source-family:SF-2026-ARXIV-2610-13166 -->

## 批四：原候选的低精度与连续生成

Source/PRE 已经 root 独核通过。四正文/四注实际写入，root actual POST 已完整顺读 Ch49 1214–1228/2383–2408 与 Ch24 392–410/本人四注通过；作者同步四注并实际回读/限定diffcheck通过，Ch49/24 窄锁释放。CDLM actual 改为“训练路径与可见 token 条件”，DoubleCat 不增加 network forward 次数但训练/corruption有成本，不采外部 token commit 语义。

### [RAMP — 2610.13041v1](https://arxiv.org/html/2610.13041v1)

2+1+2=5，精度次序具体长期缺口深入。实际§3–4/Theorem3.1–3.2声明、§6.1–6.3/T1–2：local rho<1及uniformδ保证只是upperbound次序，不是任意looped网络最优；Huginn0125 T32、24FP8 dense-linears后8BF16，其余hidden/prelude/coda皆BF16。WikiText/PG19固定32endpoints/tail64，20冻结random schedules matchedbudget；H100 first-prefill开始GPU-resident tokens/emptycache，结束firstlogit，tokenize/transfer/network/decode不计；128/256反慢约0.80/0.77×，不是TTFT普效。

Owner `INFER-TENSORRT-LLM` Ch49量化逐例诊断/局部精度保护与邻接段已实际读，缺同shared block不同recurrent depth次序。拟在“所测2-bit干预失败不能推所有格式不可修复”段后：

精度也可分配给同一shared block的不同recurrent steps，而非只给不同层。若该运行区间的递推对扰动局部收缩，早期低精误差还会经历后续收缩，末端误差则直接保留；可在固定低/高精步数预算下先低精、再以高精完成refinement。这个依据只是带收缩与统一误差上界的bound排序，不是所有looped模型的最优定律。RAMP的Huginn/H100对照只量首次prefill至logits，短输入会更慢，也未计tokenization、传输和后续decode。双精度权重、转换与kernel调度有成本；收缩不成立、预算或质量回归时，原统一精度与逐层校准仍合理。<!-- source-family:SF-2026-ARXIV-2610-13041 -->

### [DualQuant — 2610.13767v1](https://arxiv.org/html/2610.13767v1)

2+1+2=5，weight/activation双尺度具体缺口深入。实际§4.1–4.3/Eq1–4/Alg1、Theorem1条件、§5.1–5.3及packed§5.2/T3：weight MSE BCD row/columnscale，columnβ通过Xdiag(β)^-1改activation；不最小化无X的joint误差，projection相关异质。定理仅Q稳定+非degenerate时坐标stationary，不全局最优。六Llama/Qwen/alllinears/fullprecisionlmhead；fake GH200的MX/NV与real RTX4090 Llama3.1-8B INT4/G64路径分开，B1/16、prefill82、decode100/KV182，weight+activation+KV总memory均计；activationquant占4.3–6.1%GPUtime非免费。

Owner `INFER-TENSORRT-LLM` Ch49 §离线权重重建分支及前后MoE诊断/量化发布已实际读，缺weight-derivedscale可被activation消费但不授joint最优。拟在离线weight reconstruction段后：

重建参数还可被执行侧复用：同时优化row和column尺度以减少weight MSE，再将column尺度的逆应用到activation、row尺度并入输出/格式scale，就得到一条不读校准activation的W+A分支。这里的weight目标只是代理，不自动最小化joint量化误差；尺度需投影到目标格式支持集，求解器的坐标stationarity也不是全局最优。DualQuant的有限Llama/Qwen对照与单4090 packed INT4路径支持该分工，不把MX/NV fake-quant分数变成native速度证明。重建、scale保存及activationquant有费；weight/activation相关失配、格式或任务回归时，代表性校准与高精度回退继续成立。<!-- source-family:SF-2026-ARXIV-2610-13767 -->

### [PSF — 2610.12898v1](https://arxiv.org/html/2610.12898v1)

2+2+2=6，Ch24 concrete latent分工缺口深入。实际§2.1–2.5/Eq2–7、§3.1–3.5/T1–3与Limitations：shifted causal context不看own block，joint flow生成plans，K blocks内部AR，next-block第一token作landingtarget但不保证长文coherence。50Euler+L/K serial，encoder/decoder stagedtraining+rollout-state source标签/optional codes有成本。OWT1024/T5/GPT2Largejudge/1000docs，197M与677M trained54B/17B而ELF46B/BD3 524B，不同budget不合因果；有states-only PPL更好但topic/diversity/coherence退，FLOP省仅大batch变throughput，AR仍领先。未采全文质量无损或通用低latency。

Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24连续高斯→离散文本section与前后采样/状态机制已实际读。拟在该节现有self-conditioning段后：

连续prior还可不承担每个离散token的选择：把每块之前的context编码成predictive state，由flow共同生成短state轨迹，再让各block decoder并行、块内AR完成局部token。下一块先生成的第一token可作为landingtarget约束接缝，但它不是完整跨块内容或长程一致性保证。Predictive-State Flows的受限OWT对照说明“预测下一块需要的信息”与“编码本块全部内容”是不同latent目标；更低PPL还能伴主题持续性、多样性与coherence退步。多阶段训练、prior步数、局部decode与可选refinement均有费，FLOP减少也只在大batch转成吞吐；长文、prompt依赖或小batch延迟未验收时，原AR和content-latent分支仍合理。<!-- source-family:SF-2026-ARXIV-2610-12898 -->

### [CDLM design — 2610.13834v1](https://arxiv.org/html/2610.13834v1)

2+2+2=6，Ch24具体训练支持缺口深入。实际§2/§3.1–3.2/Eq3.1–3.7、§4.3、§5/T1–3：onehot nearclean训练vertices而inference denoiser stays simplex interior，DoubleCat双层corruption提高此支持而不额外forward；SemiCat随机reveal使noise-dominated token有cleanconditioning。TinyGSM 256NFE同batch200K vs标准250K不同，49.94还调sampler，不移纯architecture收益；1.7B DiT/2.1T Nemotron/256H100/2048，likelihoodproxy非实际概率，4/6优且OBQA反退。embedded直接搬DoubleCat发散/self-conditioning仍可再改善，不称普遍替代。

Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 existing396–398已有discrete多峰/SC cost，但未解开simplex统计失配与token-identifiability。拟在该节上述PSF段之前（同锚先SC后PSF）：

one-hot连续flow还有更具体的训练支持问题：接近clean时训练状态集中在token vertices附近，实际denoiser的非零熵输出却使轨迹停在simplex内部。双层corruption可先在simplex内混合目标、再加Gaussian，以较少额外求值扩展这种支持；另用随机discrete reveal，让部分位置成为可辨认的clean条件，解决高范数noise遮蔽token的问题。这改变训练路径与commit接口，不是无代价恢复原分布。DoubleCat/SemiCat的有限TinyGSM和1.7B结果含sampler、训练预算及likelihoodproxy条件；嵌入空间直接迁移会不稳定，self-conditioning仍能有额外收益。支持或质量不合适时，原SC、离散diffusion和AR继续保留。<!-- source-family:SF-2026-ARXIV-2610-13834 -->

## 批五：原三含糊条目最小准入后的必要源与 PRE

必要Source/actual owner/PRE三项已经root完整独核通过。13157/13025实际写Ch33 66/Ch80 315及本人注，13912实际Ch25 64/本人1460注；三项root actual POST正文/完整邻接/本人注通过，作者同步三注回读及限定diffcheck通过，Ch33/80/25窄锁释放。

三条准入已 root 同意继续必要 Source/Books，以下仅 general code/GUI/search/Agent，不使用 RSI 科学实验，亦不以模型自报来源当因果证明。

作者实际当前官方 cs.CL recent 日期段复核：原HTML `Mon,12` h3 line118、`Fri,9` h3 line3025；13912 identity line123、13157 line965、13025 line1167，精确v1 HTML链接均同段。这三原池身份有效，不仅按Submitted作归属。

### [RSI-Anything — 2610.13912v1](https://arxiv.org/html/2610.13912v1)

准入链：policy改变会改变预测器的支持→reliability/data/budget控制是否构建更新，组件通过后仍成对验收→不能以单个predictor或policy分数放行组合。2+2+2=6，Ch25实际pair retention缺口深入。实读§2.1/2.4–2.5 Eq10–18（特别Eq17–18）、§3.1/§6.1 code/GUI条件；不采用实验室/反应/免疫science结果。候选须当前policy与predictor comparator，data不足为unknown而非可靠；组件可各自保留旧版，pair失败整体保留旧pair，update/gate/heldout audit人口不同。CodeContests200×3seeds/up3rounds，fixed ReasonFluxCoder7B每轮4候选，fixed WM vscapacity-matchedstatic verifier29.2%vs26.3%，paired+2.83CI[.17,5.50]，onlinecalls3.71vs3.72；adaptive31.2不是免费，训练/selection/evaluation仍计费。该对照不证明普遍递归无限提升或各域模型真实性。

Owner `MULTIMODAL-WORLD-MODELS` Ch25实际58–66现有policy revision→invalidation/retraining/重新验证→channel/counterfactual calibration；缺成对retain与数据不足不能签可靠。逐字最小PRE拟在该support段与“现有证据给出了...”之间：

预测器与policy一起修订时，可靠性判断只能覆盖已获得真实feedback的候选支持；数据不足应保留Unknown，不能据低误差或无失败宣布可用。可先在预算内构建候选更新，分别比较各组件与当前版本，再在同一评价条件下验收组装后的policy–predictor pair；单组件通过仍不保证二者兼容，pair失败则保留整个旧pair。更新数据、决定保留的gate数据与最终held-out audit须分开。RSI-Anything的受限代码/GUI证据支持这条更新控制分支，不授任意counterfactual准确或递归持续增益；采集、重训、组件及pair回归都有费。支持、评价或预算不足时，固定policy、原predictor与真实执行反馈继续合理。<!-- source-family:SF-2026-ARXIV-2610-13912 -->

### [SOAR — 2610.13157v1](https://arxiv.org/html/2610.13157v1)

准入链：terminal outcome reward不能区分自报内部与检索来源→workflow分别产生两stream并给claim/answer consistency reward→可改变训练可观察接口但须重验faithfulness。2+1+2=5，claim-vs-provenance反证深入。实读§3.2.2–3.2.3/Eq2–6、§4.1–4.4/Table2–4、AppB/D与human200样本197judge一致。内部stream只query不带当前reasoning，不保证参数真值；defaultVerify exactmatch answer与指定stream，不是实际reasoning因果证明；modeljudge prompt也仅判declaredfacts与依赖，四run/200人核同criterion不授truth。Qwen2.5-3/7Base，E5base/Wiki2018/top3，GRPO5rollouts/search5；七QA/EM与fabricationjudge指标分责。Eq6已有gamma而AppD复合式再次gamma，完整系数recipe隔离；不靠该冲突排整个机制。

Owner `TRAIN-GRPO` Ch33实际64 reward definition不自动可验证→reference-likelihood→latent-consensus边界已读；缺显式来源claim分支与claim不是trace。逐字PRE拟在“GRPO 的定义不自动保证 reward 可验证或正确。”之后：

检索训练还可把“答案对”与“声明使用哪条来源”分开：对同一query并列呈现外部检索和不读取当前推理的内部回答，让policy显式选择来源，再分别奖励答案、格式和回答与所声明stream的一致性。这样的结构让来源声明可观察，却没有直接观察真实内部推理；exact-match或modeljudge的匹配只支持所定义的一致性，不证明答案实际由该来源因果产生。SOAR的有限QA对照支持这条reward接口，未签精确信用分配或无fabrication保证。双stream生成、检索、匹配及独立评价都计费，系数/判分不明确、共错或质量退步时，保留可靠outcome reward与可追溯检索日志，不让声明奖励代provenance验收。<!-- source-family:SF-2026-ARXIV-2610-13157 -->

### [Evo2 — 2610.13025v1](https://arxiv.org/html/2610.13025v1)

准入链：语言reflection只临时改context→训练共享proposer/reflector的持久evolver权重，从实际harness edits结果学习→须区分executor固定、evolver变化与harness接受。2+2+2=6，Ch80具体trainedevolver缺口深入。实读§3.1–3.3.3/Eq2–3与恢复段、§4.1–4.2/4.5–4.6/Table5；fixed executor Qwen3.8-27BFP8greedy，proprietary配置不等自身权重更新。两个role同一参数但prompt不同，reflector建议实际实施后按same tasks/matched execution delta奖，keep0，positivecredit须trace显示机制跑过。edit extraction/prefixcontinue恢复lastsuccessfulapplied harness并重生成失败suffix，仍需应用、启动、任务checks。SFT+interleavedGRPO改变evolver，不证明taskexecutor自身递归训练；Table5固定search/executor/parent只换trainedweights支持局部差额。Polyglot三runs/部分benchmark单条件，最终calls/tokens更少不等预先训练/search成本免费或泛化保证。

Owner `AGENT-REFLECTION` Ch80实际27–44已区分verbal与episode参数，313 ParamMem持久诊断generator→外部error bank上下文已读；缺从可执行harness修改结果训练持久编辑/诊断器。逐字PRE拟接ParamMem段后：

持久参数也可学习“怎样改执行harness”，而不是直接更新完成任务的executor：共享evolver按role分别提议edit或给reflection，建议被实际应用后，用匹配任务与执行条件下的score差监督，keep保持原候选。失败后续edit还可截在最后成功应用的位置，恢复该harness再重生成suffix；从文本抽取或恢复的修改仍经过应用、启动和真实任务检查，不能因格式已修复就认证有效。Evo2的有限coding/memory对照支持训练evolver与保留harness经验的分工，不证明executor权重自改或全局持续提升。训练、搜索、恢复及回归都有费，反馈不可靠、分支污染或预算不值时，原固定evolver、verbalreflection与有限retry仍合理。<!-- source-family:SF-2026-ARXIV-2610-13025 -->

## 批六：尾段具名 generation/representation 贡献

必要Source/actual owner/PRE三项已经root完整独核通过。13858实际写Ch23 442及本人1513注，13944/13941实际Ch24 270/314及本人2109/2111注；三项root actual POST正文/完整邻接/本人注通过，作者同步注回读及限定diffcheck通过，Ch23/24窄锁释放。ImagesTalkBack唯一owner为Ch24 guidance，不在Ch23重复机制。

本作者额外实际精确日期门：[official cs.CV recent](https://arxiv.org/list/cs.CV/recent?show=2000) `Mon, 12 Oct 2026`（153/153）之下，13944为[2]/题名行32、13941[3]/行43、13858[10]/行108；均在该日而非Fri9下。exact-v1题摘当前撤回false，首版本；只引用日值不造时刻。web实际必要定位，非把该153题摘全部审阅。

原 compact multimodal query 的零基 items index：13944=1、13941=3、13858=9，实际jq定点回读 title/id 与保存的exact题摘一致。本文所有query rank/#均为零基（official `[2]` 等列表编号则为原一基）。

### [InstantFusion — 2610.13944v1](https://arxiv.org/html/2610.13944v1)

准入链：相同shape的不同generator中间态不能直接交接→共享空间state与有限步displacement联合对齐→state映射不够，需trajectory兼容。2+2+2=6，Ch24具体中途交接缺口深入。实读§3.3–3.5/Eq3–14、§4.1–4.2/4.4–4.6/T1/5/7/8、§5。所有generator必须shared frozenVAE和兼容time；每model LAE、reconstruction/align/dynamics/norm四loss，50K VisPrompt/backbones冻结。只align可collapse、去rec保真退、去dyn OPD发散；有限共同步interval的位移不是exactJacobianmatching。Eq13normalized difference的s与Eq14 similarity threshold方向/范围未闭合，adaptive criterion/optimalhandoff不采用。T7六次序GenEval/HPS明显并非完全相同，不签invariance；roundtrip重复保真退。T8 1024²/50NFE/3warmup20runs单配置秒数，无额外denoiser不等免费：LAE与多个同时驻留backbones memory/storage更高，硬件precision/batch主文未披露则Not Disclosed。

Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24现有表示端点bridge（268附近）只有domain桥，缺中途state+local dynamics接口。拟接该共享端点bridge段后：

共享端点也不等于不同生成器的中途状态能直接交接：即使shape相同，各自latent与局部更新方向仍可不兼容。一条条件分支在共同VAE和兼容时间参数下，为每个冻结generator训练到共享空间的encoder/decoder，既约束状态与重建，又对齐同一有限时间区间内的位移；只对齐状态可能丢失内容或使后续动力学失配。InstantFusion的有限图像对照支持这个接口，不证明异构VAE、任意时钟、最佳自动切换或次序不变。交接不增加denoiser求值仍需LAE计算、训练与多个backbone驻留，重复往返也会累积误差。几何、时钟或净预算未通过时，保留单generator、原域bridge和独立重建/终态质量验收。<!-- source-family:SF-2026-ARXIV-2610-13944 -->

### [Images Talk Back — 2610.13941v1](https://arxiv.org/html/2610.13941v1)

准入链：encodedprompt固定不等text residual不变→双向MMDiT的I2T可把当前图像偏差写回条件→有限反向消息干预与匹配sign对照修正“条件只单向约束”。2+2+2=6，designcounterevidence深入。实读§2.1–2.3/§3.1–3.3 matched12signsettings、AppD/F/G必要scope；冻结promptencoder与jointtextactivations不同。干预在softmax/value聚合后projection前缩放I2T/T2I，input logits/norm不变但以后状态会变。auxbranch放大I2T/弱T2I后guide-away；iSFG在原conditionalforward反方向改消息，不增加NFE但A80080/BF16/batch1/CFG7.5/paired3runs后warmup局部仍+0.31s/2.86%。SD3/3.5/FLUX1024²28/40steps，GenEval553×6seeds、相同prompt/seed；image前20%与video7/25是不同窗口。pairedsuccess/failure和normmatchedcontrols支持局部消息可干预，不证明普遍自增强、真实internaltruth或heldout可靠warning；retention/disruption仍存在，probe改善不能替最终图像验收。HunyuanVideo/VBench非物理真实性或长期闭环。

Owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 guidance的Sparse/保共享条件负分支actual310–316已读，缺负分支改变I2T反馈而非抹condition。拟接SparseGuidance段、负分支共享context段之前：

双向图文生成里，固定的prompt编码不等于后续text表示保持不变：当前图像消息可写回text residual，使错误内容也进入下一轮条件。负reference因而可保留同一prompt，只加强image→text反馈并削弱text→image作用，再沿原预测远离这一受损分支；另一条in-place路径直接抑制前者、加强后者。干预的是聚合后的定向消息，不是取得新的事实或更改用户目标。ImagesTalkBack的匹配符号/消息对照支持有限可控性，不授所有双向模型必然自增强或probe等于最终质量；零额外NFE也仍有消息计算与局部墙钟费用。窗口、质量、多样性或净成本不合适时，保留原joint生成、CFG和已验收的单向条件路径。<!-- source-family:SF-2026-ARXIV-2610-13941 -->

### [LapMerge — 2610.13858v1](https://arxiv.org/html/2610.13858v1)

准入链：hard token selection丢弃未选输入、densepooler M×Ninteraction→有序位置上的nonnegative mass/CDF equal-mass分区与scan→可按恰好N聚合而非把预算当内容保真。2+1+2=5，表示聚合差额深入。实读§3/Eq3–6/Prop1声明与§4.1/4.3、§5、D.1–3；科学临床histopathology不采用。orderedp/给定r/固定width&positions的(r,x) forward/JVP/VJP O((M+N)d)，router softtopk排序额外MlogM，native logcumsumexp/fused只是backend分支；convex、massweightedfirstmoment保存不等所有信息不丢。GH200B1d512FP32/5warmup30repeat timing仅reducer、precomputedmasses，上游scorer/routing未计。Qwen2.5VL7B frozenVisionSelector scorer/同kept原M-RoPE位置，只改values，10/30%budget；POPEdefaultwidthvsgridtunedmax后者仅referenceceiling不公平比较，overwide低于hard selection；localitybias非任意order/语义保证。

Owner `MULTIMODAL-REPRESENTATION` Ch23 actual36–59思想实验Tensor≠semantics与后ReinPatch硬预算、431rate/distortion均已读。拟在rate/distortion四项代码块后、视觉teacher监督前：

输入token预算还可由有序聚合满足，而不只是保留top-k：为有序位置分配非负mass，用连续kernel的CDF划成恰好N个等mass区间，各输出取加权输入的凸组合。给定mass与顺序时，prefix/suffix scans可避免M×N分配矩阵；产生mass的softtop-k排序、scorer及重排却仍另计。LapMerge的有限视觉/VLM对照支持这条表示分支，weightedfirstmoment保留不是全部信息保真，宽kernel或不合适order仍可破坏局部证据；frozenbackbone也不保证mergedvalues与原位置语义兼容。应独立验预算、表示损失、位置接口与完整成本，局部性、质量或收益不成立时保留hardselection、原dense表示或其他pooler，不以恰好N签发无损压缩。<!-- source-family:SF-2026-ARXIV-2610-13858 -->

## 13935 HnS：停止时的单项灰标题最终必要源与具体NC

[Hide and Seek exact-v1](https://arxiv.org/html/2610.13935v1)准入经root最小core校准：概念代理分数可能与受控shortcut依赖相离→在固定概念库中改变训练cue依赖并对比mask/scorer→解释代理应回行为/扰动合同验收；2+1+2=5，designcounterevidence受影响深入。必要实际源仅§3.1–3.3/Eq1–7、§4.1.1–4.2、§5.1、§6/AppG/H，不扩其它应用/全部附录/code。当前officialCV Mon12[4]，完整exact题摘未撤回。

新增接口是SigLIP检索top50，patch cosine threshold(mu+1.5sigma)定位，7fill中按原/填补imageembedding差与concept方向最大cosine选strategy，再取blackbox输出差；cohen-d式global尺度非causal effect。多fill/参数/检索人口、orthogonalization可噪与不能保证隔离、abstractconcept不能spatialmask均保留。三ImageNet-pretrainedViT/ConvNeXt/ResNet在CelebA/COCO分类fine-tune；reference用人标/GroundedSAM segments zero-fill的输出差，与被测法同mask目标相似，作者自己承认同源评价。caption只换成gender-word概率sum difference，忽略无gender词，不授全生成事实归因。AppH在固定classifier/groundtruth下换retrievalpool会降低correlation，crop造成concept不可见；不由无标签检索签全支持。

AppG controlledshortcut构造固定位置class色块，按11个注入率0–100%训练classifier，比较同一26/103concept bank分数与clean/cued任务表现。此设计把concept-label agreement与真实行为依赖拆开；但body称cleanaccuracy及4rates，Fig/Table11称clean-cued accuracygap及11rates，所报sign/相关系数/统计口径不闭合。**隔离具体.82/.85、p值、各method全面优越及caption faithful/因果真值，不能补猜重算；不取消已准入，必要受限机制/边界可安全处理。** 定点重开条件为作者澄清Table11 estimand、rate人口及对应raw，非要求全文或生产复现。

实际唯一owner `PLATFORM-EVALUATION-SYSTEM` Ch66已完整顺读246–248及3315–3360：

- 246–248已把“已知标签一致”与“干预后模型怎样变”分开，用实际nexttoken分布/随机大小匹配组件对照；高cluster匹配与低交换差均不授全部因果回路，保raw行为/独立任务/失配降级。
- §Attribution当前3317明确每causalclaim需estimand、identification、assumptions和可推翻stress test；3323已有cue-only falsifier/necessity/sufficiency与失配Unknown，3327把scorer evidence与acceptance分责。
- 3329软遮挡要求匹配扰动预算、冻结mask分布/实现位置/output/zero或replacement baseline，承认相同token数不等语义；3356–3360“替换Baseline改变被检验因果命题”区分移除内容与OOD轨道，多baseline/pairedcontrols和rawpatchrecord不授完整机制。

最终**具体已有覆盖/NoChange**：HnS剩余可采的是“概念匹配/归因proxy需与受控行为依赖分测、填补干预不认证概念因果”及检索支持域边界；上述实际正文已经完整承载，遮挡/检索/差分组合和caption score口径不新增长期解释。统计歧义隔离，不在Books新增framework段、引用或相关系数；该已有覆盖不意味着HnS整体有效性已证实。root已实际读Ch66三段并通过具体NC，最终必要Source packet实际读回接纳，普通待办0。只隔离具体相关系数与全面优越，不取消准入或把完整框架当已证实。

## 有界 arXiv 发现的实际停止与归并

恢复四原件：model 276/start0 实得100，multimodal263/start0实得100，agents53/start0实得53，systems10/start0实得10。恢复的宽原件仅线索，不自动成为逐项题摘/Source义务。API Submitted 窗不作公开日证明；与官方 recent `Mon, 12 Oct 2026` 新事件/相关重要修订交叉核验，既有36身份有效层保留，不以存在crosslist/replacement扩全部 submitted 范围。

本轮补检按原主题 API 的 start100/start200、每页100定点取尾元数据，只使用本窗官方日门交集与相关新命名标题；不读全部 raw648题摘。start200：model 实得76/total276，首11766与末11019均 submitted Oct8，尾交集只有rank211 12530 CacheScope、rank221 12528 GlucoPRISM、rank271 12522 MolP2SBench；后两为暂缓 science 标题范围排除。multimodal实得63/total263，首11818与末11037均Oct8，尾本窗交集只有rank214 12530。两API均已到各自末页；这个停止依据只证明上述有界查询元数据尾段已处理，不证明所有276/263条题摘或全分类召回。不得在第一页第一个非Mon12就停，较晚crosslist还可能落Mon12。

official recent 按本日标题补检 CL/LG/AI/CV/RO 与 DC/AR/PL/OS/PF/IR/MA 的相关机制，新命名子切片实际包含 DC19、AR10、PL4、OS5、PF3、IR11、MA19 标题；其余宽池并未逐项读题摘。12分类 Mon12身份union648只作日期身份集合，不作为648已筛、648候选或全文分母。原start0合并输出中段曾截断，不能据已下载声称所有model/multimodal标题已读；只采用实际可读相关标题、日门交集和以下具名补检。

新增完整题摘保存于 `runtime-discovery-abstracts.json`：CompileMask13474/Layout13679/Orthros13735/DuoRate13328/SlackSwap13003/RDMA12815/Ember13408/DCOCO12570/AutoIndexer12545 九项已交 today_institutions 独立准入/必要源，非本作者最终处置；12970 Minions 本作者保留。具体线索：Orthros原model#23、DuoRate#59、Minions#96；DCOCO model rank137/multimodal131、AutoIndexer139/132；Layout原systems#0。其余四来自上述官方DC/OS相关新命名子切片。九项真实完整题摘已提供机构reader，不凭口头mapping准入。

`runtime-generation-discovery-abstracts.json` 保存13944 InstantFusion、13941 Images Talk Back、13858 LapMerge（本作者必要源/Books继续）与12544 Transformer-Based Masked Diffusion Models Provably Learn Distributions with Latent Structure、12530 CacheScope（today_models/root处置）。12544实际 stat.ML Mon12行可见于Fri9 header之前，不能以Oct8 submitted或ID切点误排除。VLA六条相关标题切片已转root：multimodal start0 #5 13929 Chronos Policy、#17 13816 Dream to Remember、#25 13740 SmolWAM、#27 13732 LAPT-Scale、#44 13516 RESCUE、start100 rank108 12818 LeWAM，不在本作者重复Source。

### 具名贡献前排除：12970 Minions

停止时定点灰标题13935（原model items index0、officialCV Mon12[4]）完整exact-v1题摘读存`runtime-late-title-abstract.json`；root最小core校准通过受控反证准入2+1+2=5，必要测量及NC最终见上方同名节。原gray待办已关闭，不将其误当贡献前EX或未评分；不扩其他标题/全文池。

完整 exact-v1 题摘已读、当前abstract无撤回标记，最小core§2–3用于决定增量：DB unique(team,project,task,subtask)任务获取、REST pull、5分钟heartbeat/watchdog重排和host preference在闲置Mac上编排。所示新增是成熟工作队列和离线集群的组合，未给出改变状态交付、重复执行边界或成本设计选择的新机制/可比反证；不因“可映射runtime”准入。贡献前排除，不评分/Books；未读fencing，不授exactly-once。日期不再为不影响此处置额外追查。不把此结论推广为排除所有agent运行时论文。

其他36原池首批具名EX最新有效层：13627/13476/12495三项完整题摘经root/机构reader独核具体EX，不在本作者重做；**13348旧EX已由决定准入的最小core改判**，有真实机制、2+1+2=5，必要源/actual Ch77具体NC经root通过，完整改判链在`institution-evidence.md` §13，归机构owner正式候选，不计本作者23。最终报告reader采用这个当前层而非旧“四EX”说法，并记录剩余未抽检范围。所有查询只限本日，未扫每周源、其他日期或任意源码/旧版/全proof。
