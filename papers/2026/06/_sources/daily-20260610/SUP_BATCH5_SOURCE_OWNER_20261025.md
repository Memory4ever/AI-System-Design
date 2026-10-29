# Jun09 第5批标准必要与actual owner（不替代唯一独核）

## 09483 DCPM（2+2+2=6）：双输入空间collision控制跨域抽象候选

作者已实读exact-v1 §2–5及Eq1/Algorithms1–2必要，未读全部代码/复现。准入时已核核心collision不重开：within-domain schema的LLM行为抽象与原schema文本分别用同bge-m3编码（不是两份独立知识真值）；behavior cos高且semantic cos低的跨域pair→union-find→core-schema induction。这里有具体候选选择机制，不能只用nighttime/dualprocess名或supersedes成熟链借分。

实际执行还包括explicit add_memory才同步raw→extract/reconcile→ADD/UPDATE/SUPERSEDE，保双向revision链；异步fresh facts两阶段DBSCAN→once/cluster induction/evidence edges，再扫crossdomain pairs。查询vector hit后链遍历与evidence_vdb_ref取高层，无query-time LLM，但read前已付行为抽象/induction/evidence存储与quadratic pairscan，原复杂度/‘identicallatency’不是实测SLO或全生命周期免费。原raw persist只保用户内容不丢，不能改叫事实groundtruth/数据库可靠性证明。

§3 paired no-think DeepSeekV4Flash/Kimi2.5 extraction/inference，reconcile同backbone，LongMemEvalS由Gemini3Flashjudge；PersonaMem/PersonaMemV232K是不同人口。QdrantHNSWm32/ef128、bge1024dense/BM25 .7、reconcilek5/DBSCANeps.35/.25，behavior/semantic阈值.72/.40在PersonaMemV2heldout调。baseline配置/版本与全部token费未充分闭，precision/hardware/重复seed/CI未披露，不补造。

Table1 full在LongMemEval/PersonaMem多数不胜fullcontext，不授一般memory替代。核心collision off为4.1pt受限消融；之后再删schema/intention1.1、再删supersedes2.9是累加而非各独立因果。§3.3baseline58.20与Table1 58.46不同不能拼统一精确优势。supersedes触达78%correct vs31%incorrect是相关，不证明因果middle必要。§3.4暂态被错当稳定revision过火、阈值benchmark敏感明确保留；union-find传递聚合不保证组内每一pair均满足条件，core描述是可撤销派生假设非人格/用户真值，也不认证未来care正确或获授权。

actual`AGENT-MEMORY` Ch77:527–600完整读，现有schema多projection/候选低重叠选择、tri-granularity、协作atoms及异步consolidation等，但没有同用户双输入embedding高behavior/低semantic collision→跨域core这一具体候选population。拟在2609.21940完整两段后/“Derived experience的支持集…”前单段+本人trueH2注。相邻原文保持，不泛重复supersedes/authority；待reader必要/owner/唯一literal一次核/root窄授：

> 跨域抽象还可以反过来寻找“行为相似而表面语义不同”的记录，而不只合并近邻摘要。一条[受限双空间分支](https://arxiv.org/html/2606.09483v1#S2.SS3)先把各领域schema改写为行为描述，再分别编码行为描述与原schema；仅将行为相似度高、原文相似度低的跨域pair聚合，离线归纳更高层core，并回指成员及原事实。两空间来自不同输入，不是独立证据；pair的传递聚合和LLM归纳也不保证稳定偏好或真实人格。受限消融支持这种候选选择有局部价值，后续累加删除不能分别归因为独立组件贡献，阈值与暂态revision误判仍会退化。行为改写、全pair扫描、归纳和图维护均计费，无读时LLM不等免费或恒定latency；跨域支持、来源或质量失配时保within-domain schema、原episode和普通检索，不让抽象相似度自行修改用户事实、扩大披露或批准主动行动。<!-- source-family:SF-2026-ARXIV-2606-09483 -->

## 07937 Hallucination Cascade（2+1+2=5）：指标不互签的受限观察，中心测量/动力学待闭

作者实读exact-v1 §III/IV、§V-A–D/G/I–J与§VI必要（未把未读V-E/F/H/K或图像点值称已核）。新候选理由保留：作者实测表中normalized hallucination与factual metric可同降，是拟核原比较反证，而非因其余模块成熟或审阅费时删候选。500runs=250长度2+250长度3、1250stage outputs/750transitions、10主题，每后stage读原prompt+所有前文；model/version/role位置与depth绑定需拆开。TableVI GPT500/DS500/LLaMA250与stage人口不相同，不用aggregate模型均值证明深度因果。§V-I另有六order表，但未给各order采样人口及匹配，不能默认解掉主表混杂。

§III估计器依赖LLM抽claim+rule/ref embedding与LLMprob加权。Eq10把softmax相似向量对其argmaxonehot的JS当h，这不是事实真值；Eq25 cos本可[-1,1]却Eq29默认[0,1]，无明确clip；Eq36 E[q|y1]≈1/E[q|y0]≈0是理想可分非通常calibration定义。§IV factual accuracy仅描述‘claim与verified facts一致’，未给独立分母/标签程序、KB来源、judge/headweights/阈值验证细节；hallucination与factual指标不同方向的数值可保作者观察，但不能据此认证真实事实丢失/因果压缩。§VI承认claim/KB/judge偏差，没有给该缺口原件。

§V-B主表chain2 h .412643→.345248/factual .794701→.790212；chain3 h .422485→.272413/factual .789425→.769147；这是不同proxy/不同末模型与人口，不说真实correctclaim一定被删。§V-J Wilcoxon有p/effectsize但1250stage相关，§V-A Eq77按独立1250算窄CI不能直接作cluster稳健证据。价格仅tokens×统一1e-6、硬件/precision/providerexactIDs/并发/全judge费未披露，不比较GPT/DS/LLaMA线上性价比。

理论中心也需隔离：保h历史标量不推出累积全文context Markov，Gaussian ε不保持[0,1]，|α|<1至多在模型前提下给平稳/期望行为，非随机路径收敛到常数；Eq74信息量乘积是设定非从claimmetric导出的定理。不能由论文形式方程签长期多agent稳定或普遍指数信息损失。正文未给artifact/code URL（仅publisher反馈/LaTeXML等），不以没有可选代码单独阻塞；必要的是同run原outputs/claims/reference与独立事实标签/测量定义、model-role匹配、cluster统计或勘误。

actual`AGENT-MULTI-AGENT` Ch82:1–79完整已读：现有单agent基线、因果别归到人数/角色以及依赖/独立观测与协作税，但不是此h/factual两指标实测链的E；不能借通用警句造diff。拟保5候选，有限作者表仅报告，中心测量/动力学归因H、Books暂缓无新写；等待reader一次必要/actualowner核。重开只上述具名必要原件或勘误，不扩全部代码/benchmark，也不把普通未读其他候选改称H。

## 09388 TV-DiSP（2+2+2=6）：guard-system行为蒸入prefix的部署替代边界

作者实读§3、§4.1–4.6、§5与A1.1–1.2/B1–2/D3必要；先前gate域未变复用，不读无关所有附录/代码。Teacher p(r|x)=sum_y p(y|x)[safe(x,y)δ_y+unsafe(x,y)δ_refusal]，不是单纯分类器logits；冻结base训练100连续prefixvectors，将独立1B guard筛选后的生成/固定拒答行为转成单模型+artifact部署。TV双重表示只给定p/q和有界phi的条件界，优化log surrogate不等实际测全response-TV/unknown x安全；guard错误与伪标签都继承，不采用LoRA‘inheritssafety’绝对说法。

四base Qwen2-1.5B/Gemma2-2B/Llama3.2 1B/3B，4bit optimum-quanto模拟edge，teacher LlamaGuard3-1B、evaluator3-8B不同角色；Beavertails固定10K/Toxigen5K prompt一epoch、Adamε1e-7，soft100/参数匹配LoRAr2或3/SVlayer13。七LR扫描，最优按SGS+MMLU选，不把selected point当未选择独立质量。HarmBench400、DetectJailbreak500普通构造非adversarial prompt injection、Beavertails test1K；未披露独立seed/CI，不能认证adaptivewhitebox/完整安全。

gate已核4.2–4.3/4.5–4.6/D3：同数据/预算的PEFT比较与四模型FLOPs/memory提供真实独立guard驻留→prefix部署frontier，不借TV/KL成熟原理分。FLOPs单token固定context512、内存权重估算非实测latency；Snapdragon8EliteGen5 ondevice utility是另slice，不能拼GPU吞吐或完整训练/guard费。Table1四TV数字65.4/53.5/48.5/49.6均低base68.9/58.4/52.5/52.2，不猜HTML合并header列名，不叫utility无损。更多prefix增FLOPs/KV/训练费，模型/guard/policy变更需要再蒸馏/验收，不会自动更新externalpolicy或授工具权限。

actual作者读Ch72 1188–1235/1748–1795/1820–1855完整：已有sensor/reference monitor分层、probe→classifier cascade、pre-guard成本与first-positionprefix detector、assessment/generation分离；没有把safe-system条件行为蒸为连续prefix、部署时不驻留独立guard的具体artifact接口。唯一`PLATFORM-SECURITY`，拟pre-guard两完整段+2605.19321 marker后/“输入侧的廉价检测…”前一段+本人trueH2注；不改原guard或counter。待reader必要/owner/唯一literal一次核/root窄授：

> 设备放不下独立guard时，还可把“原生成器产出、guard判断后保留或换固定拒答”的组合行为作为teacher，冻结base，只训练连续prefix并在部署时随输入加载。[受限soft-prompt蒸馏](https://arxiv.org/html/2606.09388v1#S3)因此移走的是在线guard的驻留与调用，不是取消安全判断的训练来源，也不把prefix变成独立reference monitor。Teacher错误、拒答与正常能力的取舍会进入artifact；模型、policy、guard与prefix身份须共同版本化并重新验收，不能靠修改外部规则自动更新其行为。四bit小模型的匹配PEFT对照支持局部安全分数—FLOPs/内存frontier，但效用仍退步，固定context FLOPs非实测延迟，有界TV条件也未认证未知攻击安全。伪标签制备、训练/选择、额外prefix/KV和独立红队全计费；威胁、效用或更新要求超出支持域时，保独立output guard、原模型与确定effect gate，不让已蒸馏的拒答表现取得执行授权或替代完整防护。<!-- source-family:SF-2026-ARXIV-2606-09388 -->

## 09071 REFLECT（2+1+2=5）：修复干预的成功rollback位置与解释文本分账

作者实读exact-v1 §3–4全部、§5、Appendix D verification与A5/A6 repair/contrastive prompts，未声称全附录或复现。Static diagnosis先给候选earliest decisive step，转为root cause/instruction/forbidden action/expected tool结构plan；从候选及更早邻域逐点rollback，保prefix后注入system guidance重新运行。首个regenerated step由规则/LLM检查是否遵plan，soft/hard gate可重试；独立任务verifier核最终答案。最终step归因机械取首个成功repair所用rollback位置，而非让contrastive explanation LLM自由改index；后者只更新理由/错误类型。全部失败回退原diagnosis仍是假设，不是已验证归因，也不等唯一/最早根因。

§4与Appendix D中expected answer对localizer/diagnostician/repair agent可见，主实验是有oracle的开发诊断，不是无答案部署证明；WTQ/GAIA normalized-string verifier可能误拒等义答案，BBM格式比较及SWE测试也只覆盖所选规格。WTQ137/119human、GAIA117/83、BBM150/150、SWE31/30的trace/label人口不混；gpt-5.2-2025-12-11 temp0同时audit/repair，不据温度0保证provider确定。Table3 BBM REFLECT34.5低于Opus AAO60.1，proxy BBM AUROC .561不授跨任务优越。

Table5 WTQ119、3samples/temp.2的correct hint成功78.7、nohint35.6、placebo46.3、wrongstep46.2，支持此语义干预的局部价值；wrongstep adherence60.3仍不等正确归因。首步faithfulness只证开始照plan，不能证全轨迹。Table7 gate/diagnosis组件并不处处单调，最后relocalization的65.7→76.3是rollbackindex更新，不借解释文字签因果。Table8 SWE Verified EM77.7高于Off1 75.0与包含关系冲突，未采该精确行/跨人口coverage或一致性优势；没有因这一测量争议删掉可支持的干预接口，也不借可选代码缺失暂缓全项。完整预算Appendix K未读，故不采用“不是更多compute导致”及等预算优越主张。

actual作者已读Ch66:706–745及5382–5454完整邻接：TraceElephant局部probe、2509.06822自产理由改选和CAR same-policy run-forward总效应均已存在；未承载diagnosis-specific repair plan→firststep gate→oracle→机械rollback index与解释文本分账。唯一`PLATFORM-EVALUATION-SYSTEM`，拟CAR完整段后/Failure Catchability H3前单段+本人trueH2注。保CAR总效应反侧不覆盖，待reader一次必要/actualowner/唯一literal核与root窄授：

> 若要检验一份具体diagnosis，而不是从同一policy重采总效应，可以固定事实prefix，把候选附近的修复计划、禁止动作和期望tool作为显式干预，再用独立任务oracle验重放结果。[REFLECT的受限接口](https://arxiv.org/html/2606.09071v1#S3)先检查首个新step是否照计划起步，按邻近rollback点搜索，将首次成功所用的位置机械记录为受该干预支持的step，再另生成原/新continuation的解释；位置与解释文字不互相代签。首步遵从不保证整轨迹faithful，成功rollback点也不是唯一或最早根因；全部修复失败时的原候选仍是假设。已知答案可见的开发期实验、字符串/测试oracle和任务间反退限制采用范围，不能等同无oracle在线诊断或全规格正确。保存prefix/state、计划与错位/安慰剂对照、所有重试和验证全计费；真实effect不可安全重放、oracle不稳或不同干预仍有歧义时，保多候选与Unknown，不由一份成功修复解释批准生产操作。<!-- source-family:SF-2026-ARXIV-2606-09071 -->

## 07874 Contextual Safety Judges（2+2+2=6）：新事实的susceptibility不等新policy的steerability

作者实读exact-v1 §2–6、A1–6必要，未把所有B/C/D图像或原调用复现称已核。主线原增量不是简单‘judge会错’，而是同judging接口将三轴分开：task demo、未知事实context、policy定义变化；再以label-neutral A/B分类表述检验语义关联。新增事实可局部修正知识缺口，不推出judge会按enterprise policy改边界，human-agreement/base准确率也不能替这两轴验收。

MultilingualPrompts779（unsafe310/safe469，Fr/Ar/Ko/Ja）、NovelPrompts194（61/133，特定postJuly2025概念，人工标category/severity及context）、SorryBench随机1000/7000是不同人口，后者主要response-compliance非同prompt任务。13judges，temperature0/max512，5seeds的mean/std不等独立模型随机样本或CI；model具体Table2可核，但hardware/precision/provider完整snapshot未披露，不推出成本优越。A3称格式error计错又从finalscore排除、只纳<2%error，部分judge/experiment因filter删去；保该人口选择边界，不将13×所有表当共同完整分母。

§4demo平均F1 .68→.71/.57→.59但Sorry .69→.65，misleading大多不动也有显著退；正确novelcontext平均+.06而Multilingual无稳定收益，Qwen3亦轻退，不说context普遍改善。Irrelevant shuffle对照存在，strongprior解释只获相关支持：FineWeb1/2每语10B词频、drop200stopword、prompt最稀词proxy，不等查过各厂商实际pretraining数据/证明内部prior因果。Novel另25%OOV vsMultilingual3%，样本/语言因素非逐项控制。

§5同prompt在base/改定义后按granular人工标重新构gold，Multilingual平均只5%flip而目标>15%；base定义有无准确率近似不证明所有policy可省。A/B framing在该对照提高两倍多flip但仍非完美；absurd sports多数通过与Claude15–35%/专用guard反侧证明并非一律不跟指令。Susceptibility/steerability/accuracy不互等，按该实验定义的模型相关不是稳定跨版本本质。A4三中性模板控制有限支持非纯stylistic变化，不认证全部prompt robustness。No universal safety truth/未知攻击或执行授权。

actual作者Ch66:5068–5154完整已读：policy-preserving rewrite已有target-preserving invariance，后接density sensor与EvidenceChain，但缺target-changing policy/事实context双轴及二者不互签的具体失败边界；6274旧trace只有泛‘已吸收’且日期旧，不代正文，不改trace。唯一`PLATFORM-EVALUATION-SYSTEM`，拟policy-preserving rewrite完整binding-end后/density sensor前一段+本人trueH2注。待一次reader必要/actualowner/唯一literal核/root窄授：

> 还要把“policy不变时不该翻转”和“policy确实变化时应当翻转”分开验收。可在同一请求上分别补充决定判断的新事实、替换安全定义，并按新定义重标anchor，再测逐例flip与正确率；[受限judge对照](https://arxiv.org/html/2606.07874v1#S4)显示，能借context补知识不等能采用新policy，高human agreement也不保证任一能力。将相同分类边界改用中性标签在局部实验改善policy响应但仍不完美，不能把换标签当可靠部署recipe；正确/误导demo、无关context、原定义与中性改写需分别控制。词频只代理既有知识，观察相关不证明训练prior是唯一原因，语言、样本与格式失败筛选亦限制外推。新定义标签制作、跨policy/context配对、重复调用与误拒回归全计费；policy改了却判断未按anchor变化、事实来源不可信或标签资格不足时，保独立规则、原judge适用域与人工裁定，不让一段新prompt静默取得policy更新或执行权。<!-- source-family:SF-2026-ARXIV-2606-07874 -->

## 07834 Cherry-pick Override（2+2+2=6）：结构冲突证据与directional confidence的互不替代

作者实读exact-v1 §2–8、A1 cases5/6，必要机制/直接反侧足；不借后版expanded insufficient/probe。合同明示Conflicting且gold C时方向S/R才是CCO；3-opt不暴露C的.887 panel vs.840single是pre-contract描述，AB把typed schema混写，不当in-contract amplification。四类S/R/I/C是verdict，NoCommit是controller route，不能以成熟authority分层自身借贡献。具体新证据是同coverage下structured-evidence与confidence残余互补、同k且同promote-to-C动作随机veto对照，而非新‘分层’口号。

AVeriTeC stratified285含pureS/R100/C150/I30，三数总280与总N285尚不闭，不补剩5标签；VitaminCMixed250由support/refute句拼接，gold非独立重标。Panel Haiku4.5/Sonnet4.5/4omini，validator仍Haiku4.5 fewshot decomposition，并非独立模型/事实oracle；greedy也不证明provider确定。5000pairedbootstrap/2000randomsubsets，无multiplecomparison correction，hardware/precision/endtoendlatency/alltoken费未披露，不授生产净成本或riskbound。

§4.6先materialmixed把S/R promote为C，再confidence不足返回NoCommit。Validator标签material本身不是语义真值：A1case5边缘subclaim冲突误挡主要support，case6不同分解误挡正确29年算术；46% CCO检出、21%pureS/R误报及typedC17%pureS/R额外拒绝均是边界。§5.1 validatorclassifier ΔAcc=-.190/CI与§5.5/6及table .78→.39冲突，不统一精确降幅。不同分母SE/CCON/CCOC/AccSR/RecC不可按‘单分母’宣传直接相加。

matchedcoverage约.28，F.85 SE.200/CCON.046对E.90 .207/.056，bootstrap差值CI跨零，不称magnitude优势；random同k promotion支持经验selectivity，不是distributionfree guarantee。关于每promotion非S/R即C的严格两轴代数忽略I人口，不采用该证明或宣称两个独立测试。VitaminC panelamplification不复现，部分极低coverage两者tie；LLMvalidator只改风险覆盖/错挡取舍，不取代facttruth或执行许可。完整decomposition/validator/panel调用、threshold选择/随机null/独立标签与escalation均付费，非全系统效果演示。

actual作者Ch66:667–687完整相邻已读：competence/directional bias与verbalconfidence不得直接route已存在，但缺subclaim结构conflict与confidence的具体残余、matched-action null不证明幅度这一设计反证；旧6270 trace非E不改。唯一`PLATFORM-EVALUATION-SYSTEM`，拟2609.12002/12101两注后、动作质量评价前单段+本人真H2注。待reader一次必要/owner/唯一literal核/root窄授：

> 当验收合同允许“证据冲突”时，还应把支持/反驳方向的confidence与关键subclaim的证据结构分开测。可由独立调用提出support/refute/mixed/insufficient状态，仅把mixed作为结构veto，再对剩余方向提案施加confidence门；无授权承诺的No-Commit是路由状态，不是新事实标签。[受限双通道对照](https://arxiv.org/html/2606.07834v1#S4.SS6)显示，两信号各留残余，结构validator直接替代judge又会误挡外围冲突或错误分解；其输出仍是可错证据，不因独立调用成为真值。比较应固定原人口、匹配commit coverage，并让随机null执行相同数量和类型的promotion；局部选择非随机不等整体错误幅度显著改善，更不授形式riskbound，三选项的强制方向现象也不能当四选项合同内的投票放大。分解、panel/validator、阈值选择与独立审核全计费；gold合同、结构标签或净覆盖不可靠时，保原typed judge、人工复核和Unknown，不让更高confidence或更强veto自行决定事实与发布。<!-- source-family:SF-2026-ARXIV-2606-07834 -->

## 08565 EinSort（2+1+2=5）：先置换数值条目再分解，索引与逆变换也占预算

作者实读exact-v1 §2–4、D1及P/Q必要；不扩其余所有tensor/quantum/weight/VLA附件。不是仅axis transpose：任意数值条目permutation π后tensor decomposition再πinverse恢复原layout，可令原高rank tensor在此重排后低rank；uniform iid order-statistics D1只证明entrywise Op(L^-1/2)近rank≤3，不授任意KV全局Frobenius/算子误差消失。原张量信息未被‘凭空低秩’，排列metadata保部分复杂性。

§2.5 full1024² permutation理想Lehmer需18.6bit/entry、row8.6，可能超过FP16。按某axis共享slice排序的tradeoff是较低metadata换较差重建，非给全部tensor同quality的免费d倍。非负分解另存原sign1bit，θ/shape/metrics也须绑定；这些理想bit数不是实际已实现factoradic编码/peakresident节省。§3 main是WT2 prefilling64/generate64、KV压缩，Qwen/Gemma；Qwenhead共享索引约1.44、Gemma3.14、Phi.35bit/KVparam不是统一constant。AppendixQ又写alllinear weight decomposition，和mainKV对象需分账，不借权重全部模型任务替本KV实验扩域。

§3 Table1 reduction/exponent择优、Table2CP PPL略好但Table3CP CPU3.3%/GPU3.7%原throughput，SVD78.7/79.6%、TT62/61.9%、TR62.7/55.6%、TD32.5/28.6%，均不加速；原M1CPU/A40GPU，AppendixQ另A40/A100训练setting不拼设备。P/Q承认factorization/search昂贵、兼容optimizedCUDA kernel尚无，precision/batch/concurrency/重复seedCI/SLO未披露。PPL局部前沿可支持机制，不认证长context质量/净压缩/净吞吐或通用所有tensor。

actual作者Ch45:680–727完整读，已有fixedrank/softthreshold producer、mixedlayout和重构成本，但缺数值permutation→factorization→inverse及理想索引熵反吃码率的这一具体branch。唯一`INFER-KV-CACHE`，拟producer投影2604.02570完整段之前（旧sharing/混合layout两段后）一段+本人H2注。待reader一次必要/owner/literal核/root窄授：

> 固定张量布局下难以低秩化时，还可先重排数值条目，再分解，重建时用逆排列回到原KV坐标；这不同于只交换轴或按token重新排队。[受限tensor分支](https://arxiv.org/html/2606.08565v1#S2.SS5)将一部分复杂性移入排列metadata：全排序的理想编码位数甚至可超过原FP16，共享slice排列可省索引，却不保证相同重建质量；非负分解还须存sign。低rank不等整个artifact更小，均匀iid排序的entrywise结论也不覆盖任意KV或最终attention误差。原短prefill/短decode对照中，各分解都降低吞吐，PPL较好的结构可特别慢；排列搜索、分解、索引驻留、逆变换与临时重构均须结算。原布局、位置与质量/费用无法共同验收时，保普通SVD/固定layout或FullKV，不由排序后的漂亮谱图签发长context能力、净省显存或服务加速。<!-- source-family:SF-2026-ARXIV-2606-08565 -->

## 08454 INNSteer（2+1+2=5）：恒定latent shift在原空间是输入相关的可逆hook

作者实读exact-v1 §3–6、E/F、H1–5、I1、J2/J7必要。各层训练RealNVP affinecoupling+ActNorm，归一stats仅train、pair80/20split、NLL+meanseparation+logdetmean/var；latent差均值向量不unitnormalize。h→zscore→φ→+αv→φinverse→denorm，每steered activation两INN pass。F1 C² diffeomorphism/小α时 Δ=αJφ(h)^-1v+O(α²)，除该向量局部恒定外，不是一份逆投影到原空间后可处处复用的固定方向；φaffine才退为线性。F3仅σ各项非零/同map/shift后在域内的hook代数反转，不是已经生成轨迹/模型行为可回滚或安全。Logdet不能控制所有Jacobian奇异值/conditionnumber，未借‘reliableinverse’宣传授数值保证。

Persona六标签含宗教/自觉/联盟/影响偏好，只测targetanswer probability不叫普遍alignment/真实信念。Llama3.2-3B链接与主文Llama3-3B名称区分，另Llama3-8B/Qwen2.5 3/7/32B；temp.7/top-p.9/reppenalty1.1，3B L40S/大模型H100/CUDA12.8，precision/端到端SLO未披露。300epochs与coupling2–6/width128–2048/3LR及lossweight搜索计费，J2三seed变split/init/order，不能当所有baseline同随机控制。Table1 Qwen32B PPL多退、I1平均PPL11.57→12.37，较高目标prob不等流利无损或semantic目标纯。J7 393x headline把含LoRA训练的11400s对INN29s、base20s，未闭统一生命周期成本，不采部署393x。无需全J4–6生物/攻击例或代码即可支持受限hook，不授通用安全改善。

actual作者Ch05:274–303完整读：已有2605.14749非线性可逆坐标交换/数值逆误差边界；具体新增是恒定latent translation如何通过局部inverseJacobian形成input-conditioned方向、analyticcoupling的零shift/反shift恢复对象，而不是泛‘非线性更好’。唯一`WORLDVIEW-REPRESENTATION`，拟14749完整段后/稀疏训练分支前一段+本人H2注。待reader一次必要/owner/唯一literal核/root窄授：

> 同一可逆坐标也可用于平移而非交换：先把当前activation映入latent，沿训练对比样本的差均值移动，再对这个新点求逆。小幅平移在原空间约为局部inverse-Jacobian作用于latent方向，因此通常随输入变化；只有affine变换或该作用恰好恒定，才等价于一份固定原空间方向。[受限coupling-hook分支](https://arxiv.org/html/2606.08454v1#S4)给出零shift恢复和同一层反shift的代数条件，不保证数值稳定、整条生成可回滚或语义不受影响；logdet正则也不控制全部条件数。归一统计、层位、坐标artifact、对比标签和强度须一起绑定，训练/搜索与每个受干预activation的forward/inverse均计费；目标回答概率提高仍可伴随PPL退化。坐标或消费者质量失配时，保原模型、较弱线性干预与独立行为回归，不由可逆性签发无副作用、安全或更快部署。<!-- source-family:SF-2026-ARXIV-2606-08454 -->

## 09508 EntropyInfer（2+2+2=6）：印刷recipe与可核执行分开，已生成query延后逐出

作者实读exact-v1 §3–6/A1–2，reader已独读同必要。Alg2 elementwise max两个归一矩阵不保row归一，H不自动Shannon；Alg3 line14 max(min(Bi,B0),3B0)恒3B0、line12除旧entropy无floor，不能直接声称实现[B0,3B0]adaptive clip；A1保N²项，小系数不等渐近linear。Alg4 ND未用、window如何含生成queries未闭，S=QKᵀ无softmax不同attentionmass。以上不通过删6候选解决，也不把普通未读改H。

完成一次针对性恢复：repo官方contents root/entropy_infer目录仅路由，两文件ops.py/modeling_patch.py current JSON；raw host reset一次后API成功。再查ops.py截至Jun09的最近commit，API返回`9c6fe2e3e8517bc83fcfde56489638f3efa69b47`，committer2026-06-05T03:43:10Z，仅精确恢复该commit的ops.py与hijack_pangu.py，没有全历史/全代码diff。原件`SUP_ENTROPYINFER_{OPS,HIJACK}_JUN05_20261026.json`保downloadURL/blobSHA；ops blob`a2f56d73014300014a9a62f8033d9ba8ae45c05d`与current同，hijack`f94cf35b4be76435748f4ab8b728a638a8bb7528`。commit时间不改名首次public，也不把Pangu路径当已复现Llama/Qwen历史build；作者代码早commit不是另有早论文正文的证明。

作者实际解码读ops65–213/339–420及hijack276–356必要：ops116–134先max/min proxy logits组合再causalmask/softmax，166entropy+1e-9，183 signed delta/(old+1e-9)、185 clamp[0,1+δt]、189 clamp[base,3base]；因此原paper的softmax后max/absdelta/夹序不能默默统一成同一个正确伪码。代码提供可执行variant但不签两者实验对应或通用语义重要性；该精确prefillrecipe及归因争议仅报告隔离，不用一般dynamichead原则造diff。

同commit真实延后逐出链明确：hijack is_prefill按qlen!=1，decodedtokens重置-1并随cache update递增，累计prefill末若干及真实decode queries于obs_query；到decode_gap+1调用compress_kv更新持久cache，当前local K/V仍旧，故本次attention尚用旧全量、后续cache才生效，不是先猜future再丢弃draft。ops372–403对该querywindow×fullkeys作scaledsoftmax、window内causalmask，聚合历史importance并pool，TopK(Bd-window)加protectedrecentwindow；GQA在该hijack实际assertfalse，pooling/window/gap路径资格不可省。它仍是经验attention代理，真实已生成queries不保证更晚需求，累计query/fullKV峰值及窗口包含prefill比例必须计费；不授完备cacheposition/任意engine兼容。

实测仅作者Llama3.1-8B/Qwen2.5-7B、H10080G/CPU192GB8cores，prefillbase2048/decode1024，precision/batch/concurrency/重复seedCI未披露。LongBench平均ours48.55/47.68低base48.94/48.82，GovReport35.18w/oLD→30.02LD、Qwenretrieve100base→91.5ours；InfiniteBench亦不全胜。最高2.39×是修改needle做summarization固定100output/4K–140K输入的requestruntime，不是长输出/生产SLO、完全同质量。附Pangu各表仍有退，单部署路径不能给全部主结果背书。

actual作者已读Ch43:120–171及Ch45:824–884完整，已有head/segment共享probe+pattern/budget及futurelearned/synthetic/真实draft用后丢，没有把首段正式输出queries积累后才改持久cache的population/生效时点明确承载。唯一拟`INFER-KV-CACHE` Ch45，在LORE-KV两完整段后/“未来问题未知时…”前一段+本人H2注；不改Ch43，不写未闭prefill伪码。待reader核定该窄差额/唯一literal及root窄授：

> 不另生成再丢弃future draft时，也可先保较完整的历史，让首段正式输出积累真实query，再按这份观察窗口选择较早KV并保护recent window；它改变的是何时不可逆逐出，而非获得未知未来。[受限延后分支](https://arxiv.org/html/2606.09508v1#S4.SS3)的[具名执行路径](https://github.com/SHA-4096/EntropyInfer/blob/9c6fe2e3e8517bc83fcfde56489638f3efa69b47/entropy_infer/hijack_pangu.py#L311)在触发step更新持久cache，本次attention仍用旧局部状态，后续才消费压缩结果；已生成queries与prefill末查询的比例、gap、pooling和protected window共同定义selector人口，不能混称丢弃式lookahead。正式输出省去额外draft，却要先支付全量驻留、query累积和排序，晚期需求漂移仍可丢关键证据；局部摘要质量反退与短输出runtime不认证质量无损或长输出SLO。原印刷prefill归一/夹序与代码variant不一致，此处不采用其精确recipe。观察不足、位置/布局不兼容或净质量—费用不合时，延后逐出、扩大预算或保FullKV，不由真实query身份自签未来充分性。<!-- source-family:SF-2026-ARXIV-2606-09508 -->

## 08068 DICE（2+1+2=5）：保候选，HQRE曲率/LLM稳定保证中心争议

作者实读exact-v1 §3.1–4.2/5、§6.1–6.2.3与6.7.2–4必要，B2/B3/B6；6整体一次输出中段截断，未把未完整6.2.4/6.3–6.6或全部11bench tables称已读/采用。DICE-PC冻结executor但训练belief/controller/critic/mixer，DICE-FT LoRA+clippedKL/entropy；共享context70tokens/round不等无通信/无训练，末checklist的PC‘no training required’不能替代§5/6训练事实。主4A10080G、reasoning/interactive分别训练200/500iter、5seed依初始化/顺序/rollout，std只>0.5%时列，closedreference不同协议不受控，不给跨pipeline全优势或SLO。

新HQRE机制/条件潜贡献保留5，不因理论争议preN。§3 persistent低福利mode→linearregret的条件命题不意味着所有多均衡/所有debate必linear，也不证明sublinear必须收敛单一均衡（可在等福利最优mode间切换）。§4 entropy强可使固定点选择稳定但福利反退，§6.2.1两动作toy条件与§6.7过强regularization/PlanBench容量瓶颈、部分TravelPlannerseed早期负margin明确保留。KLold/ref只是proxy，6.1.2已明largeLLM未直接估Lc，不能与6.7部署checklist的uniqueness监控混为全规模证书；有限样本estimatedmargin不自动globalLc bound。

中心具体冲突：Eq4 Ent_i(pi)=E_pi sum gamma^t alpha H(pi_i(h))，其occupancy本身随pi变化；B6Step2却把其负梯度差按任意固定positive w_i加权simplex entropy曲率相加，未处理occupancy导数/下界。作者独立反例只检该强单调不等式：单agent、两步、zero reward（Lc=0）、alpha=1，root以epsilon=.01到二动作child、gamma=.5，两策略root相同而child由(.4,.6)变(.6,.4)，取固定w_child=.25。左侧仅gamma*epsilon*.4*log(1.5)≈.000811；右alpha*w_child*||delta||_1²=.04，违反Theorem12宣称。root梯度虽随child变，delta root=0无内积贡献；root与child均fullsupport，不是只靠不可达boundary例。该反例不证明所有HQRE都不存在/不唯一，但足以隔离当前证明链/由其认证的LLM稳定与boundedregret。

B6Lemma37又额外假设J_i对selfpolicy concave，main Theorem12未列而一般historybehavior参数未证明；Eq5 Q只累计原reward、和含未来entropy的Eq4优化关系需另闭。B2/B6/Cor14 wmin>0粗界只适finite信息态；无限可数history positive weights sum1不可能uniformpositive，不将其finite常数照搬无限期LLM。上述均非‘理论难’或optionalcode缺失，而是具名公式/证明对象失配。

actual作者Ch82:498–539完整已读，CoopEval存在≠选择/到达、publicstream/identity与belief已具体，但不承载HQRE新曲率或定量regret，不假E。拟Books H无diff，PC/FT局部recipe与作者表仅报告，不借成熟critic/PPO/entropy或泛authority造I。重开仅修正Eq4 occupancy-dependent geometry/对应field与Eq5的条件证明、明确concavity/finite-state/迭代interior与残差假设，或具名勘误；实测LLM稳定采用另需可核Lc上界/同对象诊断与等budget独立验证。已够中心审阅，不扩全附件/代码；待reader一次必要/actualowner/H独核。

## 09135 Seed Steganography（2+2+2=6）：不改权重/采样器仍有seed控制信道，防御与来源边界

作者实读exact-v1 §3.1–3.7/§4.1–4.4/§6必要；正文提PubMed仅作文本生成分布，不开展领域科学推断。只研究风险面/测量/防御，不提供可操作payload或seed恢复代码。潜新增不是更复杂改造sampler，而是sender仅获seed控制、receiver具同model/已知deterministic PRNG与完整postfilter概率/完整原输出时，正常seed→text确定映射可承载有限隐式信号。payload均匀和被动warden是论文threatmodel；边际输出分布与默认随机seed一致不证明任意固定payload/真实自然串谋不可检测。

Unknownprompt还依恒定PRNGdraw人口，原top_p=1是所选sampler充分条件非任何runtime保证；nucleus近确定token的no-draw、retokenization歧义与后处理会破坏对齐。当前API常只给toplogprobs或远端不确定性，不能说拿得到完整distribution/同采样器，亦不从网页当前default列表推所有生产配置满足。主Q4_K_M llama.cpp六model/fourarchitecture，sender ARM/receiverx86只局部浮点兼容；sameweights不认证跨quant/版本/过滤/硬件通用。

Knownprompt6×125=750samples、100s timeout、84.5%正确恢复；代码域56.7低于news约96–97%，失败44timeout+72无唯一，successful均34s H200不含所有失败总成本。Unknowngrid原seed仅[0,10000]、搜索10^6，后length选有利setting并按长度删短样本，再扩大searchspace；其24/30cells最大长度100%不是均匀总体/所有length/所有seed真实payload，部分code0/0/.5，长序列有非单调歧义。12s仅search，重算prob耗时约再次生成另计，未列independentseedCI/并发SLO。未测试paraphrase/truncate/activewarden，不认‘undetectable’跨变换；能argmax一个seed不等真实origin/身份认证。

actual作者Ch72:1336–1360/1443–1465完整读：已有被篡改PRNG/watermarkseed-layer与attestation，但缺未修改sampler、仅caller-controlled seed也形成通信边界这一条件反证。唯一`PLATFORM-SECURITY`，拟watermark信任根两完整段后、跨host执行attestation导入前一段+本人H2注，不写恢复算法/优化参数配方。待reader一次必要/actualowner/唯一literal核/root窄授：

> 随机源未被篡改，也不代表生成链没有额外通信面：若调用方可选seed，而另一端能复现同模型、采样器与概率接口，正常的确定seed到文本映射本身就可能携带可恢复信号。[受限seed-channel反证](https://arxiv.org/html/2606.09135v1#S3.SS1)因此把caller对随机性输入的控制纳入威胁身份，而不只检查权重和采样代码是否改动；均匀载荷下的边际分布一致不等所有固定消息不可检测，也不证明自然模型已串谋。完整原输出、同quant/tokenizer/过滤及PRNG消耗规则限制恢复，后处理、代码低熵与变长draw可使其失败；局部成功不授任意API或来源认证。审计可保独立生成记录、限制不可信seed控制并校验runtime身份，恢复评估须另计概率重算、搜索和超时失败；高风险出域仍由权限与effect gate控制，不由‘未改模型’或未检出信号批准安全。<!-- source-family:SF-2026-ARXIV-2606-09135 -->

## 07819 TOGA（2+1+2=5）：静态结构×精度同预算artifact搜索，不是运行时token controller

作者实读exact-v1 §2–3、§4.1–4.2/4.4–4.6/§5–6；§4.3主方向/表2已读但其完整表1未读不采逐项全胜。HTML仅main（没有其引用的Appendix实际section），不把宣称‘详见Appendix’算必要原件已核；此处不采用完整kernel/export/超参recipe，main已足支持搜索分支与直接反侧。结构mask/高低precision mask共supernet，base权重冻结、hypernetwork经GumbelSoftmax+STE接受global LM CE+targetbudget log-ratio penalty；从原按层局部saliency/fixed稀疏率再量化，改为同总码率下同时选静态width与precision。不是新发明STE/结构化剪枝、也不按TOGA算法名借分。

该budget是理论FP16-relative parameterfootprint，如sparsity×平均weightbit，不含完整KV、scale、索引、temp/runtime；softpenalty不授严格等目标/全局最优。mainEq3 W声明dout×din却diagPin左乘及后式selectors记号/shape不一致，Eq4简写MHA(XP1...)未保完整Wqkv；不照录此代数作正确export、也不认证任意model rewiring。头数/headdim按主文固定，模块输入/输出mask与相邻维度传播仍需实际工程验收。

评价单A10080G训练hypernetwork，WT2128calibration、quantonly2000steps/joint10000、batch1/重复5次均值无CI；matched-dataset不等同baseline全部搜索预算。Joint比sequentialDISP+PTQ，fixedsparsity variant与freebranch分别报告；SPGPT/OBR的非/半结构与结构宽度不是同函数/布局，ultralow时按PPL失败剔除baseline不能叫全配置dominance。仍低FP16、部分任务单项反退（如Llama3 ARC_c TOGA-q47.1<Atom47.4/ResQ49.2），globalCE目标不签所有能力。

§4.5 L40、Llama2-7B、input2048/异batch/100runs的prefill峰值约2x/OBR1.3x，FP16batch>=12OOM；decode报告peakmemory6.5x而非decode TPOT，含INT4KV与customCUTLASS/RMSNorm-reorder-quant fusion，收益非纯searchaxis因果。模型大小/precision/backend/finalartifact、校准/10000search/完整质量回归/实际kernel全费；80G实现最多32B，70BOOM是披露边界，不授生产SLO/所有大模型。无需为了有限机制扩全代码/所有Appendix。

actual作者Ch49:627–669与1854–1915完整已读：MNK/深宽搜索与recovery、2:4×precision资源口径、在线token三近似jointcontroller都有；具体缺静态结构×precision masks同一CE/理论总字节搜索、离线交付与在线tokencontroller分账。唯一`INFER-TENSORRT-LLM`，拟MoP完整两段后/目标runtime分层搜索前一段+本人H2注。不复制不闭shape公式/完整导出recipe，只保原设计分支及不保证。待reader一次必要/owner/唯一literal核/root窄授：

> 精度也可选择时，结构搜索还可把保留哪些通道与哪些通道留高bit放进同一静态候选，而不先冻结稀疏率再量化。[受限联合分支](https://arxiv.org/html/2606.07819v1#S3.SS2)用hypernetwork的离散mask近似，在同一language-model loss与理论总字节惩罚下权衡width和precision；它产出离线artifact候选，不是按当前token动态分预算，也不由STE或soft budget penalty保证全局最优、严格码率或完整export正确。理论参数bit不含全部scale/KV/临时状态，质量与硬件支持仍须分验；同数据比较也未配平全部搜索/恢复费用，局部任务可退。作者prefill结果还包含custom mixed-precision kernel、融合与KV降精度，decode峰值内存不等TPOT，不能把全部收益归给联合搜索。校准、全模型搜索、layout/量化与回归难以摊销时，保固定结构后PTQ、成熟2:4或原稠密高精度分支，不由更好的离线Pareto点签发同质量服务加速。<!-- source-family:SF-2026-ARXIV-2606-07819 -->

## 07790 Byzantine Cheap Talk（2+1+2=5）：实际可见图与被告知的图/人数不是同一变量

作者实读exact-v1 §3–9与Pt0.A1.5–7/C–D必要，不读全部trace或复现。4-player StagHunt五round/trial、20trials/condition，trial重置而round共享全部历史；单词cheap-talk/JSONaction、temp0/max512无API或Python显式seed，不认证端点确定。六family三cohorts与n2/3/4/5/6改变peercomposition，不能把family、人数、规模/训练独立归因。A7单次重问仍失败就排该round，未给完整失败率/有效分母与CI resampleunit，不按独立100round精确推总体；APIexactstrings/cohort可核，precision/hardware/fullcost未披露。

真正题摘潜贡献是actual messagefilter相同而explicit/silent元信息条件可有明显不同结果，不能因一般framing成熟就删5候选。主Table2 ring group5±5 vs100±0/star0±0 vs80±13，silent同时移除visibility提示和playercount，不是只改一个topologycue，也不是等token实验；meta-reasoning是作者conjecture，可见CoT非因果证明。因此可采用的设计边界是transportgraph、可见消息与visibility/人数metadata分账并做交叉控制，而非‘隐瞒图更安全’或已定位战略不确定性唯一原因。

A1.5 adversary bypassLLM由harness固定stagmessage/Hareaction（soft则harnessBernoulli），unanimity奖项下硬Byz group0是结构保证，不等模型攻破/自然PI检出失败。非Byz继续Stag/改Hare及局部收益才是行为人口；读reasoning提到betrayal不等可靠检测器、action不同不证明唯一alignmenttrait。DP阈值>50%本是finite-trial后观察分类，Table5GPT4o在4人cohortDP而Table6n5/n6CP，不能称全family/人数不变；Byz×star13vs28非‘乘性作用’因果估计，也非真实外部权限promptinjection等价证明。

actual作者Ch82:17–42/79–132完整读，已有单agent虚拟同伴hint控制与真实topology/domain/反思分账，但缺actualfilter相同与所告知visibility/playercount分开交叉的这一接口；不是trace泛E。唯一`AGENT-MULTI-AGENT`，拟topology/domain dependence完整段后/MiroFlow processor对照前一段+本人H2注。仅受限证据/新测试轴，不把未闭原因写入机制；待reader一次必要/owner/唯一literal核/root窄授：

> 通信图还应与“Agent被告知自己能看见谁”分开：固定实际消息filter后，再交叉改变可见性说明与人数提示，分别保存真实收件集合、提示metadata和共同历史，而不把三者合成一个topology标签。[受限cheap-talk对照](https://arxiv.org/html/2606.07790v1#S5)在同filter下观察到不同合作结果，但silent条件同时删除可见性说明和人数，不能唯一归因于隐藏图信息或把它当防御recipe。脚本化对手始终背叛时，全员一致的目标本就不可达；group零成功不独自衡量攻击强度，检测到背叛、个人回报与共同成功也须分开。短局、peer组成与格式失败排除限制模型trait和原因解释，元信息/通信控制与重复执行全计费；未能隔离原因或效果依赖提示时，保明确协议、实际权限和小组基线，不由更少透明度或合作率批准开放协作安全。<!-- source-family:SF-2026-ARXIV-2606-07790 -->
