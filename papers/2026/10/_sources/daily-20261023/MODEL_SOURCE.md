# Oct23 Daily — 15 篇模型/系统必要 Source 切片

窗口：2026-10-22 BJT。只处理 root 委派 exact-v1；公开日与身份复用同目录 ARXIV.md 官方 Oct22 list mapping（CL/LG/AI/MA 的具体序号），不把 submitted Oct20 改成公开日期。本文不授予日级完成，不写 Books。只保存必要 Source 与处置/PRE，独立复核另由 reader/root 执行。

原件：`model-source-2610.<ID>-v1.txt` 为官方 `https://arxiv.org/html/2610.<ID>v1` 文字抽取，可能含页面脚本/公式双重文本及抓取输出上限；只以实际读到的段落作证，不称完整附件/代码已读或实验复现。精确网页仍为权威原件。抓到不等于已审。

## M2 — 2610.28819v1 LIFT（已关闭）

身份：[LIFT](https://arxiv.org/abs/2610.28819v1)，官方 Oct22 CL[7]；同窗独立家族，无更早稿/撤回信号触发。评分 1+1+2=4，新增命题是 long-form 文档按 leaf section/artifact 的 scope 计分，把可验证格式约束和内容要求共同作为训练 reward；是单组件评价/训练配方增量，不因“可靠性”术语抬高 Reach。

实际读 §3.1–3.2：flat 的全局 scope 与 structured 每叶 scope 的 density 不同尺度；结构10%、内容90%为发布配置，判内容的 Gemma-4-31B 对人工 F1=.73，不是机械证明的语义正确性。该权重使仅凑格式的答案难拿高分，但没有消除 judge/reward hacking 的一般保证。身份/日证/具体机制已足以四分关闭，不采用配方为长期通用原则，不另进入 Books，不把 source 关闭叫作已验证所有训练结果。Books：仅报告。

## M4 — 2610.28886v1 SANE（必要 Source、actual owner 与 PRE 独核通过）

评分 2+1+2=5：新增不是 metamorphic testing 的成熟原则，而是从 scorer 的 specification/implementation/output contract/代表输入，自动推导 scorer-specific capability→perturbation recipe→expected relation；通用 verbosity 在 concision 与 coverage 上可有相反方向，不能直接复用固定 recipe。

实际读 §3–6（官方HTML，保存抽取约lines450–990）：生成之后分别验证 recipe/关系是否对 scorer intent、文本是否实现扰动、该关系是否适用于实际样本；J=A×Z×I，而不是只看原/改写文本相似。每 recipe 抽10例，至少6例 joint-valid 才认 validated family，case分析只用独立 joint-valid case。这个多数阈值是作者预算配置，不是通用安全阈值。

对照：5种 scorer 均为 summarization 来源，四数据各300例，共1200；SANE 与 JRH 皆用 Opus5、无人工筛选/编辑，JRH保其已发布 recipes/prompts/relations。验证为三次独立 GPT-5.2 预测多数决，不是三种模型，更不是人工 gold。77/133 与21/35 validated-family（57.9% vs60.0%），3.7倍来自更大适用 recipe inventory，不是每例有效率更高；故不写成同总调用/总美元预算效率优势。31 vs10 fault-detecting families，coherence 中 JRH3/4、SANE4/11，固定库适用时仍合理。

judge ranking 对照为11模型，排除生成器 Opus5 与 oracle GPT-5.2；独立777个 FaithBench 人工标签，SANE165/JRH55 joint-valid faithfulness cases，Spearman .852 vs .100，指标比较的是模型排序，不是逐样本预测与人工一致率。不同 case 数与模型 panel 范围限定该结果。§6明确未有人审估计 oracle error、未验证弱生成器迁移，只有 faithfulness 的人类ranking外证。代价包含 recipe探索、全部生成、三次oracle、scorer调用与独立人工审校，不称 production可靠性。

拟采用边界：生成测试的效度必须沿 recipe→实现→relation 三段核查；仅有默认变形库或自动生成数量不能证明 scorer 能测其准则。actual Ch66 的“Benchmark生成器也会塑造被评估的任务人口”保存generator/filter/verifier，但没有scorer-specific关系方向与三段效度；“动态知识系统需要关系型回归”已有mutation/relation，却是RAG corpus关系而非judge意图适用性。拟 Ch66 前者整合一段，精确PRE：

> 自动生成scorer测试之前，应先从其准则、实现与输出合同推导扰动和预期关系，而不把同一变形库默认用于所有judge：增加细节对coverage可能应加分，对concision却可能应减分。生成后再分别检查recipe是否符合准则、实际文本是否实现扰动，以及预期关系是否适用于这对文本，只有三者成立的case才进入违规统计。[SANE的受限比较](https://arxiv.org/html/2610.28886v1)以同一生成器和来源扩展适用recipe，但更大家族数不等同总调用预算下更有效；其自动oracle仍可能同错，人工外证只支持faithfulness的模型排序，不能替代逐case真值。Recipe探索、生成、重复oracle、scorer调用与独立审校均付费；准则或关系不可靠时，保留固定经核测试与人工anchor，不由更多生成例或低违规率签发可靠性。

## M1 — 2610.28767v1 SkillEval（必要 Source、actual owner 与 PRE 独核通过）

2+1+2=5。§2的新增为GPT4o-mini逐题提完整技能list，经SBERT/HAC聚成100skill，形成多热Q-matrix；NCDM以`α_j(θ_i-d_j)⊙q_j`及单调非负MLP预测正确性；冻结文本encoder、projection预测新item参数。§3–4为3811模型/9523题、五bench；OOD是item-wise heldout响应，taxonomy却用全部item文本/metadata构造，选K参考下游表现，故transductive技能表示、非真正新domain零接触。IRTNet的heldout预测较好但本router top1较低，不能用AUC替代routing结果；SkillEval三seed top1为65.46±.34，对训练集所选最强单模型61.57；KNN top5/top10更好。GFLOPs cost曲线不是美元/时延，更没有包含全response bank/标签/拟合成本。

§4.2冻结网络、仅拟合200个新模型的100维profile，与random同一最终估计器；adaptive规则`p(1-p)×skillcount`倾向高不确定、多标签题，20答的平均bench误差.061接近100随机答；只在本题库/一个network/<=500答成立。Appendix O必要反侧已读：human assignment检查needed而不查missing；HAC/prompt/embedder未联合稳健性检验；排除MuSR+IFEval响应训练后IFEval路由.410低于random.437。Co-mastery关系阈值敏感、非因果先修链，不采用成认知发现。

actual Ch66 WILD段已承载多维IRT、adaptive更新、目标预测/费用与holdout边界，不重复写CAT成熟原则；新增只有语义Q taxonomy与量尺transductive支持边界。拟唯一owner PLATFORM-EVALUATION-SYSTEM Ch66，在WILD完整两段后，精确PRE：

> 多维profile还可把题目显式绑定到可解释技能：由题干提出多标签，经聚类形成Q-matrix，再用题目难度、区分度与模型各技能熟练度预测回答；冻结测量网络后，新模型只用少量回答拟合自己的profile。[SkillEval的受限验证](https://arxiv.org/html/2610.28767v1)支持这种固定题库内诊断，但taxonomy若已由全部测试题文本构造，heldout响应不等新技能或新领域迁移；技能命名可读也不证明标签完整、独立能力或因果先修。预测AUC、路由top1与shortlist覆盖须分别验收，co-mastery不能当课程因果。题库响应、技能标注/聚类、拟合及自适应调用均付费；taxonomy支持不足或域外反退时，保留分项实测、普通随机/分层题集和独立任务验证，不让profile或较少答题替发布签字。

## M3 — 2610.28838v1 Parallel Pretraining（必要 Source、actual owner 与 PRE 独核通过）

2+1+2=5。§2–5及Limits：SPT独立抽source/translation文档，PPT同一2,048窗串联且轮流语言在前；同双语corpus、同初始权重、同AR目标，两语都计loss，同200B总tokens。1.3B、EN–FR/EN–SW；组合从60/100/160B分支续20B（SW仅100→120B），两方向组合均重启optimizer+rewarm，而连续SPT/PPT不重启，故同总tokens不隔离restart/schedule的全部因果。PPT-only没有持续理解优势且翻译曲线不稳；PPT→SPT在所测阶段/语言对兼顾两者，逆序某些理解更好，不能写普遍支配。

§4固定目标continuation，对应/无关source和阻断相应attention比较支持paired context参与；PPT后SPT改善单语loss且保留超过SPT的对应上下文收益，是受限机制解释，不证明全部task增益唯一由此造成。代价是译文配对/构造、两阶段训练、重启状态与方向/任务回归。实际Ch27:957已有同窗配对/前后顺序/因果条件，Ch28:75–98已有目标可见性切换和粗阶段恢复，但没有“同AR目标、paired训练条件→独立文档恢复”的边界。拟唯一TRAIN-PRETRAINING Ch28；精确PRE：

> 即使next-token目标不变，训练时反复提供同内容的另一语言，也会改变部署所需的条件。可先把文档与译文放在同窗、轮换前后语言，再续以独立抽样文档，让模型适应没有对应译文的普通输入。[1.3B双语受限对照](https://arxiv.org/html/2610.28838v1)中，始终配对并无持续理解优势，先配对后独立训练则兼顾单语预测与跨语上下文使用；逆序在部分理解任务仍更好，两语对不能成为普遍课程。配对、有效tokens、切换checkpoint、optimizer重启与rewarm须共同保存，同token预算不隔离所有schedule效应；翻译/配对、完整续训与两语回归均付费。译文不可靠、单语恢复或净收益不足时，保留原独立mixture及较短配对阶段，不把同窗或局部BLEU改善等同无损语义迁移。

## M5 — 2610.28887v1 Autonomous Research Teams（必要 Source、actual owner 与 PRE 独核通过）

2+2+2=6；非AI4Science应用，研究对象是Agent组织及attention设计。§2–3已读：同一GPT6Astra/high，16个学科profile、persistent private session/notes、共享proposal/review/实验/失败记录，每10轮提炼；折扣UCB分配后续实验，reward为开始时best utility的非负改进，失败/拒绝仍记预算0reward。先串行proposal防重复，最多8并行；80迭代只63实际评估，不是80成功训练。1.2x baseline step-time门在训练前检查，utility固定三指标scale，不是部署安全。

实验150M搜索再1.3B验证、各architecture按FLOPs调tokens（不同tokens），CFDN部分150M CSR反退，不能写全面支配。组织对照固定model/iteration/candidate budget/feedback，fresh-memory与uniform复用首16轮、nobackground从头；best utility 1.04/.54/.56/.76、主run63对variants65–68 eval，支持本单run组合局部作用，不足因果证明学科profile“跳出局部最优”或任意任务协作优越。LM-only与三目标有指标tradeoff，search NIAH为teacher-forced proxy非开放answer。全proposal/review/implement/失败/全部训练、反思/共享维护都付费。

actual Ch82:170–200已有局部工作视图/共享工作板、derived evidence及跨run promotion，220信誉还明确UCB名称不授独立reward；本篇差额是“共享实验记录之外仍比较保留私有研究history、并按真实实验增量分配下一机会”。拟AGENT-MULTI-AGENT Ch82在工作板完整两段后最小PRE（待reader）：

> 长期探索还可以同时保留两种连续性：研究者自己的假设、失败理由与未决问题，以及团队可复用的proposal、审阅和真实实验记录；共享成果不必等于每次都抹去个人history。有限实验预算下，可依据已完成实验相对开始时best的增量与探索项分配下一机会，而不只轮流调用。[受限attention架构搜索](https://arxiv.org/html/2610.28887v1)比较了保留/移除private history与固定/自适应分配，但单次搜索、共享起点和复合组织变量不能证明学科persona或UCB普遍优越，失败与拒绝也必须计入预算。全部调用、审阅、失败实现/训练与共享维护均付费；reward不可靠、历史污染或探索收益不足时，保留小型固定团队、独立候选与真实实验验收，不由更高search utility自签发现正确或跨run权限。

## M7 — 2610.28957v1 Scan or Index（标准必要 Source 完成）

2+1+2=5。§2–4：396QASPER（320可答/76不可答）+8本OpenStax80问（主要模型合成references、仅核原文quote，非独立人工truth）；known-document retrieval，500token/75overlap，共同top5和2500token reader预算，gpt4.1mini固定generator、gpt6.1sol/RAGAS judge。QASPER395/396 hybrid pool已含整篇，不足分离全扫与preselection；book662–2245段，全扫初始见过所有段却在多轮reduction丢证据。EC按全部assigned（失败0），AA仅completed且不同分母；case不能混用。

book Jev在共同成功76问中hybrid EC94.9 vs scan93.2；各方法reduction损失阶段不同，全扫≠最终证据完整。检索覆盖和answer不是同一结果：无证据book AA.808，引用准确未验证；packing还丢已检索支持，40不可答中几种scans只abstain11–14。延迟为不同hardware/precision/API concurrency（GB10 FP32/BF16、API2并发）实测，hybrid表只rerank不含candidate，不能跨部署泛加速。重复query cost=P+NQ投影含prepare但local GPU不定价，unknowncharges为lowerbound；不把第六query crossover当通用常数。Books实际NC/PRE待核，不先重复检索分阶段原则。

## M8 — 2610.29171v1 TrainBridge（标准必要 Source 完成）

2+2+2=6。§2.4/3/4/6：从同workload eager→compiled GPU图、postfusion IR、generated kernels与profile提取“被消除/融合/重组什么”optimization intent；semantic supernode对齐NPU源，只有同类低效仍存在才target-native rewrite，再profile NPU剩余host/comm/memory瓶颈，不直接搬GPU kernel。KeyShift overlappingview重写的5.13x仅单算子[1,24576,6,128]BF16，不能当端到端收益。

GPU up to8 H100SXM PyTorch2.7/CUDA12.8，NPU up to8 Ascend910C torch2.7.1/CANN8.5/torch-npu2.7.1.post2，单node。Record50与generic同initial port/12h、同GPT5.6SOL/medium三run，best validated419.2s vs283.2s；Stage2-only约334s，GPUevidence先至299.7再profile285s，支持此处互补。27record每项一次<=18h，other4每项一次8h，不与三run混；训练time排tuning，bestwithinbudget非总体自动收益。NanoGPT保step/schedule并val loss<3.28，不保证任意训练语义/数值bitexact。依赖成熟源GPU可编译证据、不覆盖multinode，全部迁移/编译/分析/搜索/profile/验证成本须计。actual owner/PRE待比。

## M9 — 2610.29225v1 DiagSafe（4分关闭+统计纠错必要深入完成）

1+1+2=4，但与机构README同一family的数字纠错已定点深读§3.1、4.2/Tables3–4、§7；不重复家族计数。Prompt-specific S-items含逐风险exemptions，U-items独立映射0–3分，降低只凭泛safety标签的误判；这仍是dialogue safety测量配方，不是Agent轨迹保障。

人工gold仅236 sampled responses。Table3 rubric三judge对人工分别89.41/90.25/95.34%，不能说全部>93%。Table4的93.33–94.78%是judge彼此一致率、κ.828–.864，不能偷换人工正确率；README本窗两commit将宣传all>93修到>89与表一致，表本身未新增实验（ORG.md定点记录）。336prompts/252rubrics的人审是另两个样本，不与236合分母。LLM生成label规格限制rare/emerging/localized覆盖，11localmodels/单inference mode不等商业provider safeguards，§7明确未覆盖agents。仅报告具体量尺/纠错，不据成熟安全效度原则另抬分、另写书；root统一family当前论点。

## M6 — 2610.28897v1 Refusal Direction（重要反证受影响域深入完成）

3+1+2=6。HTML不可用，官方PDF通过下载并续取恢复；12页文字原件已存。实际读正文pp1–8 §4–8与AppD pp12必要CI，不追无关翻译例。Qwen2.5-14B-Instruct、单A100，复用PolyRefuse pipeline扩Belarusian/Bashkir/Tajik，GoogleCloud翻译后由邻近语言知识人工核而非母语验证，尤其Bashkir可信度最低。WildGuard拒绝判断取补集作compliance，不把“未拒绝”直接认定每份回复具体有害或实际effect成功。baseline英语4.9%、be24.7%、ba87.9%、tg92.0%，必须按target剩余headroom校正`(post-base)/(1-base)`，否则已近上限误作ablation转移成功。

§5.3/Table4：英语/白俄源广泛提升未拒率，ba/tg源在自己/对方接近0或负归一效应；be→ba仅.13，不能说alltransfer完美。英语方向addition只将ba/tg从.88/.92降至.41/.43，不是普适恢复安全。§5.5的geometry在英语选的layer30/-4与跨层结果不同；其他层cos对齐不等该处干预有效，不据此说这些语言“没有拒答表示”。AppD1000次bootstrap复采已有judgments/points不重跑inference，不表达独立训练/生成seed不确定性。单model、三语言、翻译/文化harm未母语闭合，不能把resourcelevel归为唯一因果。全部翻译、白盒抽取/干预、跨层扫描、判分和母语复核均有费用。

actual Ch72“Refusal Behavior不等于危险知识已经删除”两段承载拒答/知识/effect分离，随后累积方向段承载多方向可转移，但未含跨语headroom与source/target不同条件。唯一PLATFORM-SECURITY；拟在上述两完整段后、累积方向段前精确PRE：

> 跨语言复用拒答方向时，还要分别保存方向来自哪种语言、在哪层/位置提取，以及目标语言干预前已多少次不拒答。目标本来接近不拒答上限时，干预后仍高不能证明方向成功转移，应同时报告原始变化与剩余headroom。[单Qwen模型的低资源语言反证](https://arxiv.org/pdf/2610.28897v1)中，部分源方向在强失配目标上并无可靠新增作用，而另一层几何对齐也不等当前层的行为控制；邻近语言辅助核译、单模型与拒答judge又限制安全解释。翻译/母语审校、方向搜索、白盒干预和行为回归均付费；标签或迁移不稳时，保留本语言独立红队、原模型与外置policy，不由共享向量或低拒答率签发跨语安全或知识删除。

## M10 — 2610.29249v1 MOSAIC（标准必要完成；已有覆盖拟NC）

2+1+2=5。已读§3/5/6/8、AppG关键反侧：923题=784可答+139拒答controls、11–24session合成persona/media；固定Gemini3.5 reader（无extendedthinking）/prompt/packer/judge比较goldsymbolic/native/generictext/structuredtext、retrievedall/capped，top50 manifest冻结，budget top20/每modality3/100MB。必须另测完整chain在retrieved与真正serializedrequest的coverage，不把delivery当读取。Goldsymbolic .846残余是reader+format+judge混合，不是纯读取因果；native.783、generictext.690、structured.704，恢复+1.4 CI[-.9,3.7]不显著；retrieval7.6和packing3.8是matchedprotocol关联，gold/retrieved distractors组成仍变，不能因相减就宣完全因果隔离。

视频n56–64/MDE8.9–11.2pt，ordered/shuffled不显著不证明无时序信息；rawaudio-ASR+.8、goldprosody+1.5近null同时有词汇情感线索/其他hop泄漏，不能说ASR保存所有声学；correct vs swapped goldtag -4.6只证明selector敏感，不等真实prosodytagger有效。secondreader仅120pilot、uncapped MiMo timeout未复制；人审与生成筛选不能消除分布选择。全表示写入/检索/媒体上传、全部control/reader/judge及人工费用继续计。

Books拟已有覆盖：actual Ch66“RAG端到端评估必须保留阶段级归因”的完整receipt链明确候选→assembledcontext/provenance→generator→配置和端到端；同段前requiredinformation/替代chunk集又明确partialcoverage≠全部必要信息≠答案；Ch77:43完整段明确表示可保存connectivity却丢metric/chronology，原始证据/派生结构按查询充分性分责。当前采用的是这组分账约束的omnimodal受控验证，不将本篇合成population的阶段差额当新普遍瓶颈，也不另起多模态memory owner；拟NC，无diff，待reader核。

## M11 — 2610.29250v1 SearchWeaver（标准+小gap深入完成）

2+2+2=6。§2–3/Limitations：固定model与corpus，proposer从全部候选taskreward/trace和optimizationquery gold docIDs同时修改持久corpusartifacts、可执行tools、instructions，允许换basesystemprompt/contextpolicy。每corpus10次各1候选，取optimizationquery最高mean，再对从未反馈的testqueries评价；BCP30opt/800test、BRIGHT4subsets213opt/210test，不称在线自主改任意生产工具。Searchagent GPT5.4nano/Pi，proposer Opus5.5/ClaudeCode；基础retrieval资源不同方法非完全相同，所以headline不唯一归因“joint”这一变量。

相同loop prompt-only对照平均52.0而完整55.0，Economics promptonly41.8 >完整38.3；删除artifact+tools+usageinstructions一起至48.7，不隔离各者因果。工具耗时42.4→32.9/63.2→36.6秒明确不含modelinference，亦不含10轮离线搜索/准备、人工核与全token费，不叫全链42%省时。迁移Gemini3.5FlashLite一次无reopt局部支持reuse，evolvingcorpus更新何时必要/如何incremental未研究。所有准备/优化失败候选/测试/重建费用应保存，版本变动独立回归。

actual Ch76 Persistent Corpus Structure段已有共享map/有限预算导航/可达≠实现证据与预处理更新成本，但没有一起搜索“哪些预存信息、工具承载哪部分计算、agent保留哪项判断”。拟AGENT-RAG，在该完整段及marker后、OnlineRetrievalPipeline标题前精确PRE：

> 持久语料结构的设计还可以与工具和使用说明一起优化：冻结语料与搜索模型，让提案者读取开发query的执行轨迹与reward，同时修改预计算artifact、可执行操作和调用说明，再冻结候选交独立query检验。这样改变的不只prompt，而是哪些工作提前完成、哪些交给工具、哪些仍由Agent判断。[SearchWeaver的受限对照](https://arxiv.org/html/2610.29250v1)中，联合接口在平均上有益，但部分子域prompt-only更好，联删多个组件也不隔离单项因果；工具耗时不含模型推理和离线优化。全部候选/准备、调用、更新与独立支持核验均付费；语料变动、gold泄漏或净收益不稳时，保留原文路径、固定检索/人工接口并重做持出验证，不由一次开发高分授长期freshness、事实或工具权限。

## M12 — 2610.29255v1 HMDLM（标准+gap必要深入完成）

2+1+2=5。§4/Eq5–12：token与hierarchylevel在跨step状态共同mask/reveal，同step先预测level和是否揭露，再用该level预测token；中间(m,revealedlevel)仅两pass之间存在，不能当永久decoupledstate。每level不同schedule/hazard使高层更早revealed但为softorder，不是硬topology。相同weights共享backbone、不同heads，仍两串行forward；预测level未知、训练teacherforcedgold与推理sampled差额保留。KL按hierarchy/token两项分解不自动认证任意β的完整trainingloss仍精确NELBO，本次不采用完整loss或渐近保证。

§5/6：LM1B128ctx/33或65Btokens，table1多个baseline数取旧ADLM报告，自己trainADLM梯度爆炸；tau5时99.16%同level、HMDLM≈MDLM，tau1才有分级。WikiHow从OWT checkpoint finetune，不同length过滤且每model同split，HMDLM因较低maskfraction训更久，不是等epochs/FLOPs；频率F在modelPPL/MAUVE优，位置P genPPL优且1024 MAUVE .07<MDLM.12，不能只用genPPL宣多样性无损。Sudoku6/25M、rule-round gold层级训练、测试由head预测，solve有限提高不等开放推理。生成256step*twoforward、label构造、额外训练、head与完整质量回归都付费，不宣推理省时。

actual Ch24 diffusion opening已有schedule/并行/commit费用，但没有层级与token联合state、先level后token的软顺序。唯一MULTIMODAL-GENERATIVE-PARADIGMS，在完整代价bullet列表后、“图像和视频往往容忍整体画面…”段前精确PRE：

> Masked diffusion也可以在每个位置携带一个优先层级，与token一起遮蔽；每轮先预测层级和是否揭露，再在这份层级条件下预测token，使不同level的noise schedule形成软生成顺序。[HMDLM的受限构造](https://arxiv.org/html/2610.29255v1)因此不需要把所有位置同等对待，但level是模型预测而非真值，层级已知而token仍mask只存在两pass之间，已揭露状态继续保留。两次串行forward、层级标签和额外训练都付费，较好生成PPL也可伴MAUVE退步；小模型/短文本与Sudoku不认证长文质量或端到端加速。层级无区分、标签或总质量失配时，保留uniform masked diffusion、普通采样schedule与任务verifier，不由先揭露少数位置签发推理正确或安全停止。

## M13 — 2610.29292v1 CATS（标准必要完成；仅报告拟）

2+1+2=5。§2–4/6：固定agentpool/prompts/models/tools，handcraftedDAGsupergraph每步独立Bernoulliedge抽K候选，源不可达node拒绝；Gemma4-31B attributer读同题各candidate的taskscore、cappedoutputs/toolcalls/finalartifact，给node [-1,1] credit，再归一advantage给所有firedincomingedges相同更新、unfired小更新、概率低于initialfraction时剪边/不可达node，4step后选bestfinalcandidate，非直接部署整个prunedsupergraph。与random/scoreonly同candidateeval数非同compute，attribution本身额外付费。

codingagent Gemma4-12B、BigCodeBench/MBPP各100heldout/三seed；BigCode48±5 vs scoreonly42.7±4.9，有overlap，MBPP与handcraft近似且deploymenttokens多于handcraft。搜索token在两coding少28/35%，poisonHotpot反约2倍；54%deploymenttoken少不等生命周期省费。3/6codingteam无interagentedge但共享环境仍沟通，不能归“communicationoptimization”因果。Hotpot6poison/4honest的固定攻击池三seed不留poison，不是适应对手安全；attributer见systemscore，credit-success只是selfconsistency，未做人审/leaveoneout真值，scoreonly未单独调参、不隔离credit机制。

actual Ch82:277–293已分模型/边/协议/graph身份与proposal接受、全生命周期费用、固定小图和独立verifier；260的MASPO段还明确judgepreference非causalcredit。本文新增具体offline启发式对所测pool有局部收益，但nodecredit均分到入边不提供新边级责任/安全协议，结果不识别通信改图的独立价值。拟仅报告保算法和反侧，不把它硬升为新长期owner段；此为具体处置，不称摘要初筛完成或所有topology已验证。

## M14 — 2610.29340v1 Reader–Writer Coupling（认知gap受影响域深入完成）

2+1+3=6。实际§3–6及AppH必要功能反侧。MLP branch `J=Σv_h ũ_hᵀ`，effective reader含activationderivative和pre-normalizationJacobian，排除residualidentity；对称score C=<J,Jᵀ>/||J||²会丢单通道polarity，还含crosschannel/assignmentdenominator，不能拿C>0证明所有反馈negative。Signed `m_h=<mean_panel ũ_h,v_h>`是panelmean Jacobian trace贡献；top16|m|只是几何core，不是16个全部重要neuron。单侧writer重配保持两因子集合统计但改函数，两侧共同permutation才等函数；999重配ranktest依赖assignmentexchangeability，测组织结构非loss因果比例。

Tiny28.9M/Small123.6M/Medium405.3M、GELU/preLN/RoPE/FineWebEdu/三seed，releasedOLMo/Pythia/GPT2延伸但rawweightcos与effective在gated/inputblock可分离。core大多opposed、shuffled/unigram未形成同样符号，不能说已识别哪项语言结构唯一导致。writer连optimizermoments打乱后续训，writer往newreader重建而loss可先回baseline、writer只recovercos≈.5，说明不唯一配对也可同loss。§6原因仍open。

AppH关键收窄：单侧pairbreak也改变spectralshape，不能“仅破reciprocity”；equalweight/Jacobian/output disturbance配对后6独立seed的symmetrydamage关联loss仅4–9millinats，属conditionalassociation；parallelcomponentdeletion与matchedrandom完整重算支持功能代价，但sharedreader方向保留约6成damping，不能把全部deletionloss都归特定couple。符号翻转/删除是大范围干预，安全pruning/editing仍未来工作。m<0也不推出完整`I+J`全局contractive/stable，更不等删除知识或自动剪枝证书。完整activationpanel/Jacobian/999重配、干预与续训成本须计。

actual Ch16“MLP是不是知识库”明确feature可读≠使用与非数据库，随后PerturbationProbing结合输入扰动与指定outputreadout；未承载同indexreader/writer耦合、单侧vs共同permutation与effective-reader符号。唯一MODEL-FFN，在“因此更准确的表述是…”完整段后、PerturbationProbing段前精确PRE：

> MLP的reader和writer还应按同一个channel配对阅读：只看两组权重各自的norm或spectrum，会漏掉谁把何种检测结果写回哪条方向。共同重排两侧只是重命名，单侧重配则可保留这些集合统计却改变函数；pre-norm层的有效reader还包含activation导数和normalization Jacobian。[受限耦合测量与干预](https://arxiv.org/html/2610.29340v1)发现多数强pair的writer反向作用于自己的reader，但这是所测输入panel上的局部符号，不证明完整residual更新全局收缩，也不等每个neuron都向logits写入同一概念。重配同时改变谱形，损失关联和删除代价不能只归某一对称性；Jacobian、重配、干预与续训均付费。需要解释或编辑时，保留原模型、真实行为/非目标回归与多路径证据，不由负cosine或几何core自行批准剪枝、事实修改或安全保证。

## M15 — 2610.29352v1 LCCP Scaling（标准+gap必要深入完成）

2+1+2=5。§3–5/Eq1–2：五scale nonembeddingN31M/61M/104M/245M/821M（总165M–1.22B不可混），4Kshort Ds、32Klong Dl分开，S1–4的5×5grid共100，S5九configs；Llama3.1-8B按fullvs4Kchunk loss选token后，统一GovReport32K集合的logLongPPL拟合7参数additive law。heldoutscale R²>.95/MAPE<2%只在logLongPPL space；offset C<0，与NLL≥0长期冲突，作者明确有限区间经验law，不写渐近定律或任何长度无限增长保证。

ConstantLast4为constantLR单轨迹保最新raw继续训练、仅平均最新四checkpoint作evaluation；观测器不反馈训练参数，更不能从merged恢复原optimizer状态。S1–4 constant轨迹三run、S5固定Ds450N至Dl120N≈100B、24merged观测，prefixfit后续heldout支持有限range预测。32KRULER每subtask500、128Kextension仍额外2.10B+RoPE/mixture变化、longSFT2.10B三trainingdataseed、agentSFT4.20B三evalrun分开，不把这些消费成本算免费。主要增益中等难retrieval，LongPPL是reference选的proxy，短文饱和不能推long停止，反之也不能无限续训。保模型/history/data/schedule/observation身份与全longsequence激活、data、存储/平均、downstream回归费用。

actual Ch22共同前提:187–197已区分位置关系有效性、longsample/activation与系统容量，不含short/long训练预算分开和rawtrajectory/mergedobservation。唯一MODEL-LONG-CONTEXT，在“因此这条路线的主要输出是模型有效性，不是系统容量。”段后、位置扩展恢复分支前精确PRE：

> 决定长窗继续训练何时停止，还应把先前短窗tokens与新增长窗tokens分账，并区分训练轨迹和评价读出。可保持constant学习率继续训练，保存最新raw checkpoint用于续跑，只对近期数份权重平均后测量；平均观察更平滑，不等训练已回滚或免费恢复optimizer。[受限LCCP scaling对照](https://arxiv.org/html/2610.29352v1)用reference模型选出的长依赖tokens拟合有限区间曲线，负offset已排除其渐近解释，不能由短文loss饱和宣布长窗无收益，也不能由此批准无限续训。长样本、activation、checkpoint存储/平均和后续适配都付费；proxy、长短任务或边际收益失配时，保留预算终点、raw与merged分开验收及原较短窗口，不把更低LongPPL换成部署容量、真实检索或SLO保证。

## 定点 Books 处置与复核状态

- M1/M3/M4/M5：reader已独核必要Source、actualowner与逐字PRE通过并发root；root唯一写入/POST另行验收。M1在WILD两段及marker后/GrowingPains前；M3在完整TokenSuperposition段后/LET前；M4在完整Bloom段后/角色目标场景前；M5在工作板完整第二段后/Librarian前。
- M2：reader已核4分关闭通过。M4标准Source也通过，无重复审阅需要。
- M7拟已有覆盖：actual Ch76 persistent corpus段已明“可访问完整语料”不等决定性证据实现，Ch66 RAG阶段receipt与requiredinformation段分别保存candidate→assembledcontext→answer及partial/complete；本篇同known-document扫描的reduction失效/成本是具体验证，无新存储或执行不变量，拟NC而保报告限定结果。
- M8实际Ch80 62–86已有generic执行反馈/可行动诊断和原检验义务，但没有用成熟后端compiled变化做异构后端“优化意图”参照。拟唯一AGENT-REFLECTION，位置在“遵循反馈也未必意味着修到了被检测的缺陷…”完整段后、“已有observation也未必自动成为经验…”前；精确PRE如下，待reader：

> 性能修复的反馈还可来自同一程序在成熟后端的eager与compiled执行差异：先识别哪些计算被消除、融合或重排，再确认目标后端仍有对应低效，提出本地算子、布局或局部编译改写；最后重新profile目标端剩余瓶颈。它转移的是优化意图，不是把源kernel或速度比例原样搬过去。[TrainBridge的单节点受限比较](https://arxiv.org/html/2610.29171v1)支持源编译证据与目标profiling互补，但质量门仍需原训练step/验证目标，低trainingtime排除了离线调优费用。迁移、编译取证、全部搜索/profile/失败验证都付费；源栈不成熟、语义或目标质量回归时，保留原port、目标侧profile和独立正确性检查，不由一个融合案例批准跨硬件或多节点通用加速。

以上为提交时状态；后续reader消息已确认15项必要Source/评分/处置独核层全部通过，10个精确PRE实际owner/邻接也通过（详同日REVIEW R30–31及相应首批记录）；M7/M9/M10/M13 NC/仅报告通过。M9两exact官方patch另存DIAGSAFE_CORRECTION.md，人工agreement与judgepair一致性不混。这里只确认独核层，不替root实际保存/POST或授日级完成。没有代码运行/复现/生产能力声明；root必要Books/POST仍由其唯一执行，不是资料blocked。
