# 2025-09-19 非作者独立验收

复核者：sept07_10_author（非本日报作者 Tesla）；检查时间：2026-10-06T19:59:25+08:00。窗口仅09/18 09:00～09/19 09:00+08。本次独立重读 AGENTS、Prompt、研究/Report 当前合同、Daily/arXiv 来源、ROADMAP 与相关路由 checkpoint，再加载本日 README、FETCH、FIRST_BATCH、NARROW_SOURCE_SAFETY_HANDOFF 和原件；不继承别日候选/coverage，不读 Weekly，不改共享 Books。

## 1. FIRST 与实际范围

实际独立完整读作者65份精确v1题摘，包括15114/15255/15478的abs恢复；完整浏览本日月段14500～15500内62标题，不按ID或submitted决定公开时间。所有论文潜力的具体约束→增量→设计选择按 FIRST_BATCH 逐项核对。没有把这些题摘扩成65篇全文任务。

原三项重开14834/14851/15027均成立：本次另实际补读其受影响原方法/对照/限制，见§2。另发现14943的关闭理由不足，定点读§3～5恢复局部数据分布转移反侧。余12标题中15089 OpenRE三阶段自纠错并非明确领域标题，补完整v1题摘后恢复潜力；14504 OmniGEC及15048 maiBERT补完整v1题摘，maiBERT另看方法/对照核心，具体关闭。其余9标题分层核为临床/医学、领域情感、专利语料、领域mine/历史压迫评估，无新增通用系统机制提示；两HF science标题不扩附件。原范围/关闭记录保留，以下差额覆盖旧结论。

最终完整题摘68份：63贡献潜力、5关闭（原06216/14515/14752，追加14504/15048）；另MiMo-Audio官方先发潜力1。正式候选0、标准/深审 Evidence 完成0、Books 实际修改0。FIRST通过仅指此贡献/日期处置，不授日期、性能、安全或Books许可。

风险逐项保留：14624自生成forget不等隐私擦除；14651 MCTS攻击需完整预算/误拒；14760动态spec trade-off不等安全保证；14837视觉干预有off-target；15206 90%保留不等零退化；15260地域多语guardrail须具体反例；15335同事实词形混杂；15361反事实专家不等一般因果无偏；15478文本略强不能授全模态防护；14712伪标签agreement不等truth；15174解释分类改善不等忠实；15339 AQE题面与模型信号尚不能支持真正自觉；15403保证只限定义的解释不确定性、非事实/医学可信度。均已读完整原题摘，日期隔离后没有拟采用安全结论，故不虚报完成深审。

性能/理论反侧保留：14900输入相关Self-Routing与可merge等价性待证明；15038 attentionmass不是value/output保真，CUR选择/E2E成本待核；15148 onlineconformal失配、56.7x/4.14x分母不混；15218 Blocking本身可能损害能力；15248 compute-matched与重复基线是具体准入潜力非1T规模标签；14882 quantizer声学提升/语言退化、14930 speech引入text退化、14653 UMA英语subtoken失效、15114概率不能代理语法、15476模态增加非单调，都保留局部验证/反例，不因不普遍而否准入。其余表示/蒸馏/检索/动作压缩/数据生成/输出控制潜力保留 FIRST_BATCH 的条件，题摘性能数不作采用证据。

## 2. 必要误排/安全原件

- 14834 RES：实际§2.2、§3.1～3.3/Table2及Appendix C。dialectical personas在一次generation中模拟，非独立Agent通信；同GPT局部无DR .439→有DR .483且P6 .607→.606。原稿说trait/agent边际收益下降，不应写成平均收益下降。每essay .6秒→1.7分钟/$ .0021→.0100，非免费协作或可靠独立共识；必要消融可支持评价输出设计潜力。硬件、服务并发/SLO和重复不确定性未披露。
- 14851 Empathy-R1：实际§3.3 reward、§4.1.5、§4.2.2、§4.3/Table4。reward为regex结构+经contrastive训练query/answer embedding余弦阈值；可优化代理不证明安全。SFT-only局部指标退化；无CoE ROUGE .054优于有CoE .045，作者深推理解释不证明忠实。20名一般公众/100样本匿名随机六模型相对Win@1，不是临床或伤害评价。只保留训练负迁移/评价边界，不引入医学疗效知识链。
- 15027 CLEAR：实际§5.2～5.5与Appendix G。每dataset10条Llama3.1人工发现新增虚构引用、薄弱论据未修；另20条盲相对偏好79%、agreement65.83%可同时成立。两个reviewer为作者、计算机背景，不授独立专业事实复核或所有模型都不保真。已有局部反侧，旧“无保真反证”关闭撤回。
- 14943：实际§3.1～3.4、§4/Tables6～8及§5。GPT生成paired explicit/implicit biography、五职业分类；混合训练→implicit与explicit-only→implicit有明确落差（Llama .933→.716，DeepSeek .907→.671，Phi .925→.581），不是只报告训练集fit。恢复局部分布/暴露条件验证潜力；同数据生成器与职业集合不能授开放域泛化，各模型LoRA rank/epochs不同不可互作等预算。RQ1先写BLEURT而§4又称Sentence-BERT，原描述冲突保留、不汇总不明确的距离结论。仍日期隔离，不授Evidence/Books。

五项关闭不是领域/小样本/benchmark自动拒绝：06216明确conceptual scaffold/roadmap且无执行语义或可靠性反证；14515 taxonomy/metric归纳未提供新增设计对照；14752 private evaluator到80%阈值只是污染缓解计划，未呈现具体污染/评价反例；14504混合人改/GPT银标与两模型fine-tune题摘仅披露本GEC数据/任务改善，未出现新合成选择机制或质量条件比较；15048实际v1题名Can maiBERT Speak for Maithili，MLM/BERT分类与相异语料基线，不提供新学习/预算可比或迁移边界，不能由单语言新模型授系统增量。后两原件在INDEPENDENT_SCOPE_CORE/INDEPENDENT_MAIBERT_CORE，保留失败的15048abs缓存请求。15089完整v1题摘明确relation discovery→cross-validation可靠实例denoise→re-predict，自纠错输出机制值得保留，可靠实例不能先当真标签，日期待原公开证据。

## 3. 官方核心、去重和来源停止

Google：实际读19core0 Sensible完整机制/研究结果与DIVE publication完整摘要，19precise旧DIVE/TTD完整v1题摘，19recovery TTD完整核心至availability。Sensible what/how、YAMNet+VLM、六few-shot、提案→用户确认、10人12情景等与旧09255v1身份一致；时间28.5s比16.4s长、SUS不显著，不能仅保留偏好提升。DIVE人口分层伤害知觉及judge/steerability贡献已在2507.13383v1题摘，不因安全benchmark而关闭，仅此次收录无新增量。TTD原Blog的draft/refinement/self-evolution与旧2507.16075v1相同；另窄核旧§2、§3.4～4/Table1～2已有ADK、同结果及消融，不是Blog才出现对照；baseline默认不同模型，Cloud一句产品availability不披露新系统边界。Blog一处消融数字概括不匹配旧表，不能授新的正面结果。只为本日去重读旧对应窄段，不开启7月研究；新增原件在INDEPENDENT_GOOGLE_DUP_CORE/INDEPENDENT_TTD_RESULTS_CORE。三本次再阐述关闭通过，不等原研究已经深审或首次日期已确定。

MiMo：实际decode本日最早9bc65b003c18完整README，与正确原official Demo/当前README核心核架构身份；1.2B tokenizer25Hz/8RVQ、patch4步→6.25Hz与delayed decoder具体保留。原mimo-blog.raw为失败404，不能称其成功；有效核心为mimo-demo.raw/initial README/19mimoidentity，保留错路由。repo.created_at00:46:49Z、firstcommit00:48:29Z、下一commit01:05:50Z、当前public均不证明09:00北京时间前已public；date-only Sep19不能自行授完全落窗。12月2512.23808仅误身份纠正，不作9月证据。

14来源均按本日原响应/receipt核有限停点：OpenAI RSS1247原GMT无窗内项；Anthropic174 publishedOn/172身份，两Sept15及Sept5都窗外；Qwen本日60配置无UTC18T01～19T01，Next/TTS夹窗，不由draft授事件。DeepSeek正确updates正文Sep29→22→Aug21、Kimi目录Sep16→5、ERNIE page2 Sep12→Aug14跨下界；MiniMax英文12最早Oct27、中文13跨Jan15、Agent一条2026，不授全站历史。Hunyuan POST9最早2026、ZAI18末页hasMorefalse minDec7只是历史缺段。Seed type2原15/49区分pinned跨Aug/Jul；type1原0及20/40/60/80，80has_morefalse且total94、20仅June SwiftSpec，其余缺array不是0。MiMo官网Paper8与两正确chunk：Blog15全部标题/描述，实际More同数组slice(0,8)/slice(8)没有未执行下一网络页；无date故不授历史。

Google月页12条Sep19/18至Sep11确已有限处理、DeepMind历史不齐；Metareset/严格域名查询空不授零历史事件。arXiv主题/系统超时、历史new参数无历史头、month两个部分响应及62完整标题，HF19推荐19标题恢复17相关，全部都非first-public依据。没有将2200月库存、94论文total或任何普通未读全文称外部终态。

## 4. DAY/Books 与重开

结论：通过（当前边界内）。正式0/Evidence0/Books0；无当前日期成立的拟采用条目，因而无普通必要审阅、owner写入或POST任务未完成。Books0由无可采用候选导致，不是已有coverage，也没有新增窄段建议或共享文件写入。

外部终态保留63论文家族（FIRST_BATCH原61潜力＋恢复14943＋新增15089；完整名单按原表与本差额），以及MiMo先发日期；原公开公告/作者公开事件或完整落窗区间恢复时只重开受影响精确版本的准入、必要证据及实际owner比较。不采用submitted/HF/DOI/commit替公开。上述日期与Meta/Hunyuan/ZAI/Seed论文/DeepMind/MiMo历史缺段不支持正面证据、候选、Books或无遗漏/全站覆盖断言；普通未读附件不是终态。

README六部分、来源/候选/证据/Books/缺口/非作者复核一致。完成同步后V3校验与本日限定diff检查实际通过；机器校验独立于本语义验收，不复现代码/实验。发生具体新增事实/反例时局部重开，不重跑未变化有效审阅。
