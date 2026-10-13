# SimpleQA Verified：本日单篇必要证据与Books协调

作者Schrodinger；Anscombe实际日期/准入/必要Evidence及具体Books PRE已通过[独核§7](SUP_INDEPENDENT_20261011.md)，root实际两段窄锁/逐字PRE§11后作者已写，两段/完整前后邻接及本人末注非writer实际POST§12通过。以下写前比较与逐字方案作为历史依据，当前普通只DAY/FINAL，不沿旧待writer停点。新Sep10完整BJT自然日，旧Qwen行/日期/6分及连续§4不动。

## 身份、日期与准入

[精确v1](https://arxiv.org/html/2509.07968v1)作者Lukas Haas/Gal Yona/Giovanni D'Antonio/Sasha Goldshtein/Dipanjan Das，与[作者原发布](https://www.linkedin.com/posts/lukas-haas_we-just-launched-simpleqa-verified-a-new-activity-7371560388712181760-yrHH)正文和本人comment中的论文/Kaggle链接相同。`SUP_simpleqa-author_20261012.raw` JSON-LD SocialMediaPosting datePublished=`2025-09-10T15:09:13.600Z`，[Kaggle原发布](https://www.linkedin.com/posts/kaggle_new-benchmark-launch-simpleqa-verified-activity-7371561234418151424-C-ma)同类型=`2025-09-10T15:12:35.237Z`，两者转换到BJT均为2025-09-10，仅以日期落窗；不是submitted、搜索索引时间或雪花ID推算。`SUP_simpleqa-kaggle_20261012.raw`返回6109bytes shell，不假称已读dataset/leaderboard实现。

原SimpleQA的题目分布/答案标签/判分规则混杂能力比较 → 对同一来源家族做unique-URL与语义/词汇去重、source reconciliation、answer-type/topic rebalancing和numeric-range/hedge规则修订 → 模型比较必须重新指定人口与scorer对象，不能把分数变化都解释为能力进步。拟评分2+2+2=6，评价纠错深入受影响证据，不用分数逃过Books判断。

## 实际证据

原件`SUP_core-simpleqa_20261012.raw`精确v1：作者实际读完整正文HTML paragraphs0–56、全部七表、Appendix A完整prompt（section id A1）；引用/无关链接不作全文队列。未运行代码、未重标1000题、未复现模型API评价。

- §2/Table2：4326→3095 uniqueURL→2871 semantic→2664 TFIDF→1855 publisher-access→1218 type/topic→1117 nonnumeric reconciliation→1073 numeric reconciliation→1000 hardest。序贯数据人口共同变动，没有singlefactor matched-population消融。119个municipality founding-date题说明冗余，但人类raters的激励归因是作者假说；原release未提供rater IDs。
- §2.5：search-augmented模型和原URLs只能支持来源核对流程，不认证所有gold truth；nonnumeric歧义排除/修标签，numeric源间5%检查与最终scorer per-input容许区间不是同一规则。去掉robots限制域和选择旧模型答错题会改变estimand，不证明用户请求代表性或完全无污染。
- §2.7：人工修URL/date precision和metadata，但没有独立全题truth审计。3.7%reasoning/7.3%multistep由prompted classifier给出，不当客观能力类别。
- §3/Table4–6/A：旧scorer在temperature2.0重复10次定位disagreement，再人工检查反例；不是新scorer全人口独立准确率认证。numeric target明确allowed range：小离散计数/标识保持exact，中等约1%、大数约5%的任务约定，不是统一5%规则。直接answer正确时可忽略不矛盾的附加信息/对问题修正；这是answer-slot对象，不认证whole-response事实。多个hedge候选须最终commit一个，否则notattempted；commit错误仍incorrect，不能把拒答当全输出安全。
- §4/Table7：without tools、作者称standard API parameters，gpt-4.1-2025-04-14同一新版autorater同时评原SimpleQA/Verified，分数差是人口/标签改变的条件事实，不是scorer-only因果。模型snapshot并未对所有商业别名完整冻结；temperature/max-token/repetition/总调用成本未披露。hardware/precision/batch/concurrency/SLO对本包所采用scorer语义不适用；不能由API成绩推出系统性能。F1为overall correct与correct|attempted的harmonic mean，不是普通binary precision/recall，也必须并报attempted/hedged人口。Gemini2.5Pro55.6仅该作者protocol结果，不授所有事实性/降低真实幻觉。p53重复Verified名称的平均比较是原文typo，不照录。

## 具体Books比较与待root协调

唯一owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。作者实际读正文14–60的四身份/拒答激励、87provenance、611–650分布假设、2152–2195 deterministic/judge分权及完整相邻交接；定点查询SimpleQA/2509.07968无结果，未全书扫描。

已有具体承载：14/47的对象、分布、环境、scorer条件化身份；51–60的覆盖/条件正确率/错误拒答成本；611–631的错误分布/scorer不会由更多样本修复；2152–2182的matcher/judge分责及annotation版本化。只是这些原则的又一benchmark验证可仅报告，不因没有论文名就声称gap。

待独核的真实最小差额：numeric answer的数量/identifier/日期精度与容许区间须进入gold-target contract；`answer-slot正确`、`whole-response事实`及`最终commit/未尝试`是三个测量对象，不能由同一个F1接收。当前上述具体正文没有这一受限语义接口的一段论证，拟一段放scorer对象/分责邻接，保留source reconciliation非truth、chosen hard人口、人工/多次judge成本和gold不可核时Unknown回退。不拟收排行榜、4326→1000配方或统一容差数值到书稿，不改其他owner。是否形成长期差额由Anscombe实际owner PRE和root协调决定；作者禁止写Books/LS/index/scripts，不先称整合完成。

当前风险轻核发现官方google HF dataset有具名纠错；`SUP_simpleqa-current-fix_20261012.raw`完整commit diff实际读，0dc97e0d28d8233463e005cdc4475cc2a13ba2dc/2026-03-09T15:58:14只有original_index55问题latitude改longitude，数值33.7738及allowed-range原样。支持问题对象本身也须冻结，不把current main或“Verified”名称等同Sep10原数据/全部truth认证。只处理受影响结论反侧，不扩2026研究/全dataset或history；该窗外纠错不另加family、不改首公开日期/评分。原v1 scorer语义命题仍可采用，gold可核性限制加深。

普通待办：root协调已被非作者确认的一段scorer语义gap、独立实际POST；本日source/日期/六部分继续，不等待无关日期。作者不代Books写入或独立签名。

## Root窄锁下最终逐字方案（PRE档案）

root于2026-10-12明确授作者唯一窄锁：Ch66唯一句“让更强模型打分”是一种 measurement design，不是 ground truth 的替代。之后、既有verifier纠错反馈段之前两段；仅另增本人SF-2025-ARXIV-2509-07968章末Review notes。不触既有2026正文/marker/末注。以下逐字方案已获Anscombe实际§11 PRE通过，并已实际写入正文2806/2808及本人末注5957；非writer POST仍待完成。已有效Source/Evidence不重读。上面单段建议/root授权待办均为写前历史停点，当前改为两段已写/实际POST与DAY/FINAL待办，不沿用“作者禁止Books写入”作为当前窄授权边界。

第一段：

Reference-based scorer 还必须先固定“什么答案算对”。问题的语义、reference 的精度、逐题允许的 numeric tolerance / range 及单位，应与 dataset 和 scorer 的精确 revision 一起版本化；否则同一个数值可能回答了另一个问题，同一标签也可能在换判分器后获得不同 verdict。对近似测量允许误差，不等于可以放宽离散计数或 identifier；来源核对时使用的一致性阈值，也不能自动成为模型答案的判分容差。简单、语义明确的 exact rule 仍然有效，新增合同只是明确它究竟比较哪个对象，而不是让 judge 自行放宽规则。来源一致、搜索辅助 reconciliation 或“已验证”标签不自行证明 reference 为真；语义、单位、容差和标签的维护、人审及独立核验都要计入成本，gold 无法可靠确认时保留 Unknown，并回退独立 oracle 或人工裁决，而不是把模糊 reference 强行变成对错。

第二段：

还要区分答案槽位与整份输出：direct-answer slot 符合 reference，只能证明该槽位在当前规则下匹配，不能认证回答里所有附加事实。若一次输出给出多个 hedge 候选，scorer 应按冻结规则检查它是否最终 commit 到一个答案；已 commit 的错误答案仍是 incorrect，未 commit 的输出则进入 not attempted，而不是通过候选中恰有正确项获得成功。结果因此要并列 overall correctness、correct | attempted 与 attempted 的原分母及比例，另保留未尝试人口；删除未尝试者或只报条件正确率会改变被测对象。这两种正确率的 harmonic F1 仍只是该回答策略与人口下的汇总，不是校准概率，更不是整段事实或部署安全率。[必要评价纠错证据](https://arxiv.org/html/2509.07968v1#S3)支持这一受限测量边界，不证明所有 gold 或 judge 已可靠；高风险、语义含糊或参考失配时，仍由独立证据和人工裁决接手，再付相应复核成本。

本人末注拟文（实际PRE通过后才记录通过；POST未发生不先签）：

- `SF-2025-ARXIV-2509-07968` — Daily2025-09-11补Sep10；[exact-v1](https://arxiv.org/html/2509.07968v1) §2/Table2、§3/Tables4–6、§4/Table7与Appendix A1完整prompt，2+2+2=6，评价纠错深入必要局部。采用question/reference精度/逐题range/单位与scorer语义对象、commit及attempted分母；人口/标签/规则共同改变不授纯模型进步，source reconciliation不自证truth，current official dataset单行latitude→longitude纠错不认证current main等于v1或全gold可靠。root具名两段窄锁，Anscombe必要Source/Evidence/具体owner及逐字PRE通过；Schrodinger写入两段，非writer实际POST待完成。未核实现、重标全dataset或复现。
