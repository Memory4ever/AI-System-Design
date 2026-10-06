# 五项必要证据及 owner 差额（原源/PRE/actual POST 已独核）

root已实际核五项必要原源与对应owner PRE，并授窄锁；作者完成下述窄段后，root亲自读正文、完整邻接及末注，五项POST全部通过、锁释放。最终Books整合：12662 TRAIN-GRPO Ch33 L1753/1755；13013 TRAIN-DATA Ch27 L317；12852 TRAIN-DATA Ch27 L468；12916 MODEL-SAMPLING Ch20 L380；13055 TRAIN-DPO Ch34 L253。下文保留写前差额提案与原证据，不将历史待PRE文字视作当前待办；不授日级完成。

共同：本窗 exact-v1 日期原值 V3_PRIMARY_DATE_FIELDS.json；已过准入复用。下列必要原源已实际读，未运行代码/实验。原始 B 块为 HTML 位置，不冒充 PDF 行。current event 轻量检查原输出 V3_CURRENT_EVENT_FIVE.txt；13055 admin substantial text-overlap 标记保留，不当撤回或新机制证书；12916 v2 存在但没有 correction/withdrawal 标记，本次拟命题仅精确 v1，不比较全版本。

## 2602.12662 Think Fast and Slow: Step-Level Cognitive Depth Adaptation for LLM Agents

2+1+2=5。标准必要源 V3_ADMISSION_12662_CORE.txt B65–87（§3/Eqs1–6）及 V3_EVIDENCE_12662_EVAL.txt B89–104/138–176（配置/Table2/4.4）。拟采用的具体接口缺口加深，不凭 cognitive 命名或公式加分。

仅成功 action 在相同 observation/history 下扩成四个 cognitive-level thinking，保留同一个原 action；平均 action logprob 在同组标准化后 softmax 得到重分配系数，乘原轨迹 advantage，失败轨迹不扩。它比较的是同成功 action 条件下的生成兼容性，不认证 thinking 正确或最合理级别。系数和为一不保存真实总梯度幅值：Eq6 成功分母是全部扩展 tokens，thinking 长度与 sampled condition 也改变。失败也 confidence 扩展在 Table2 降到83%，支持只作成功条件分支而非 universal preference gate。

Llama3.1-8B/Qwen2.5-7B；CoSFT500随机环境/GPT4o expert levels；ALF2420训练、200测试；RL group16/组8/150iter。同 CoSFT 的 Qwen 消融：CoPO92.5/1739.4tokens、固定Max89/1664.9、Min81.5/1227.7；noCoSFT86/2496.2 与 expert SFT87.5/2871.6不能合为单一RL效应。更高成功率不等于最少token；confidence不是truth，不能把4level混合=探索完备。训练精度/全walltime/独立seed CI Not Disclosed；不采用ScienceWorld应用结果，采用ALF离散tool-action机制和局部反侧。

owner TRAIN-GRPO Ch33 L461已有 quality-token 改rollout mode，L713已有环境 continuation 的 counterfactual segment credit，L1745有 confidence/outcome mask；都未承载“成功 action 固定而thinking level改写、重评分same action”训练接口。拟1–2段独特差额：区别改变action的探索与固定action的认知深度重分配，明确成功support/额外生成scoring/不同token分母及普通GRPO回退。不是泛confidence安全段。待root必要源→owner PRE和文件锁。

## 2602.12852 WebClipper: Efficient Evolution of Web Agents with Graph-based Trajectory Pruning

2+1+2=5。标准必要源 V3_ADMISSION_12852_CORE.txt §3/B33–64 及 V3_EVIDENCE_12852_EVAL.txt B100–138；当前ACL comment且v2存在不支持把currentabstract数字移到v1。

action/info bipartite graph，action cost1、info cost0，由初始query到最终answer的shortest path选行动，并纳入“some shortest path 的 predecessors”（B47），不是全部必要依赖完备闭包。三个完整action sets至少两个完全一致才接受，不是逐node majority。删动作会改变学生可见history；只对原本不相邻且现在相邻的后继thought，用完整原context（含随后删掉的动作）改写，三rewrites取最低base PPL。PPL仍不是事实证据，privileged deletedcontext通过teacher进入新target的风险要独立验。

TongyiDeepResearch30B-A3B，extractor/rewriterQwen3-235B-A22B-Instruct2507，32H800/LR5e-6cosine；Serper/Jina，o3-mini judge；GAIA103text/HLE500text。3 evalseed均值不当3训练CI。Eff-only HLE.353低于base.358；Hybrid.361，且xbench unpruned-distill.746高于Hybrid.733。Hybrid混合原trace支持能力/效率取舍，不证明graph单一因果；F-AE harmonic Acc 与1-rounds/100不是真实成本或安全SLO。生成/图提取/改写筛选离线费用计入，precision/完整训练token/walltime Not Disclosed。

owner TRAIN-DATA Ch27 L447–462已保存搜索 evidence graph/trajectory grounding，但不做 shortest-path trace transformation 或 selective adjacency rewriting。Ch29 L130–139 loss mask明确保留history，不能充作已有覆盖（本项实删history）。拟Ch27一段新增“删条件输入→只修邻接thought→保存raw/pruned/rewrite lineage”数据变换分支，条件不足回退完整verifiedtrace/普通loss mask；不把图路由签成依赖完备。待PRE与窄锁。

## 2602.12916 Reliable Thinking with Images

2+1+2=5。标准必要源 V3_ADMISSION_12916_CORE.txt §3/B34–60 + V3_EVIDENCE_12916_EVAL.txt B128–161/175–182。dual-stage entropy分别衡量cue mining与reasoning文本，top-k高entropy token的negative-log信号仅textproxy，不能认证视觉cue truth。positive reliability leap与两段总值聚合用于trace voting，filtered earlyexit须保warmup/quantile/τ身份。

默认 Qwen3-VL8B-Thinking，32trace上限/warm8；offline32全生成/warm32；α.4、τ thinking.1/instruct1。online consensusβ.9基线也加同停止策略，但B160还pre-generate32 complete traces评估，reported token saving不等实际producer总计算、parallel latency或已上线earlycancel。Table4 default Vstar83.4/HR4K78.6 vsSC78.8/75.3；w/oDF80.8/77.1、w/oRV81.9/77.9。tool高entropytoken占比与cue consistency不是grounding因果证明。full hardware/precision/concurrency/walltime/训练seed CI Not Disclosed。

owner MODEL-SAMPLING Ch20 L340–378已有prefix gate/query-local confidence distribution与self-verification界限；没有分cue producer与reasoning consumer的两段proxy及warmup→filter→vote的预算身份。拟一段该分段selector branch，不把本文top-k规则/α写成长期常数；实际pre-generation成本、被删视觉证据和truth独立验收，信号失配回退完整样本/普通vote/外部verifier。若root判该具体启发式不改变长期接口可仅报告，但不可因“局部/不普遍”本身拒差额。待必要源与owner决定。

## 2602.13013 Towards Universal Video MLLMs with Attribute-Structured and Quality-Verified Instructions

2+1+2=5。标准必要原源 V3_ADMISSION_13013_CORE.txt §3/B77–89 + V3_EVIDENCE_13013_EVAL.txt B191–210（Tables7/8）。ASR/WhisperX与timestamp是独立audio anchors；Seed1.6同时integrator和attribute reviewer，非独立judge。先互补多caption合并，再按attribute分Error/Missing只修affected字段，其他validated内容保存，formatcheck另行而非factcheck。

125K原video→121K retained，eightattributes+allcaption，300manualspot >98%非全data统计保证。Table7同QwenOmni3B/20k优化，multiattr miss25.5/hall18.9/total43.4 vsnonattr30.6/18.5/49.1；missing改善伴hall稍升。Table8 S1 42.1/12.8→S2 24.8/19.9→S3 23.4/18.3，不写每阶段hall单调改善。S3额外longcontext训练且该stage表用fullDATA，不能跟20k消融拼成matched总budget。B86 200K caption与§5.3 20k并存不造统一数量；精度、统一训练walltime和独立seedCI Not Disclosed。没有重跑数据生成/人工审计。

owner TRAIN-DATA Ch27 L253–259已有phrase sensitivity selection但非修caption；L312–314为generic delete-vs-corrective rewrite，不拥有audio/transcript anchor+attribute Error/Missing局部修复。拟一段独特差额：先保互补coverage、按原证拆missing/error、局部修复不重写全caption、ASR/time lineage保留；同Seed循环与coverage/hall取舍近正文，回退可信单source/人工验证。不将1M规模或“universal”名称入书。待PRE/窄锁。

## 2602.13055 Curriculum-DPO++: Direct Preference Optimization via Data and Model Curricula for Text-to-Image Generation

2+1+2=5。必要原§III-B Eqs6–7 B51–56，V3_ADMISSION_13055_CORE.txt；评价/配置/反侧 V3_EVIDENCE_13055_EVAL.txt B70–130。同PF-ODE两点由冻结diffusion θ前进一步，preferred/rejected用相同fixed consistency reference f_ref作d距离target并减reference自身residual；trainable fϕ替换第一端，reference冻结而非EMA。sigmoid差的是reference-centered consistency residual，不是已导出的endpoint logdensity ratio，不能继承DPO exact KL概率保证。

LCM从SD1.5 distilled但768²/8step，SD256²/50DDIM；不横合quality/latency。D1 67500/6750pairs或aesthetic22500/2250，D2 DrawBench200×500训练/50eval，D3PickaPic150kpairs/500prompts。SBERT/LLaVA prompt-caption、LAION/CLIP、HPSv2皆proxy非新humanlabel。singleH100/10kiter/bs16/acc2/AdamW5e-5；LCM64GB/48h/LoRA64，SD36GB/24h/LoRA8，但modelcurriculum SD6→16另改变capacity不称fixedrankmatched。βconsistency200、diffusion5000；同时更换objective/curricula，不能认定全部收益源于residual。reward-freepromptmask假定原胜破损，Table2 LCM D2text.5577低于base.5602、SDD2HPS.2695低于.2708，保反侧；Table1D3 SD/LCM某行重复字段不采。precision/独立trainingseed CI Not Disclosed。

owner TRAIN-DPO Ch34 L244–251 diffusion pairlabel/time与pseudo correction不承载consistency residual，L426 exact policy/reference logratio是需保留的旧推导。拟一段近probability identity→alternative residual目标，明确两个时间点/PFODE/fixedtarget identity，surrogate而非概率证明，curricula不搬整recipe，成本/反侧/fallback普通Diffusion-DPO或可信pair保留。actual admin text-overlap with 2405.13637是旧Curriculum-DPO lineage信号，本文采用差额只在Consistency-DPO，不给旧curriculum成熟原则计分。待root必要原源/owner PRE。
