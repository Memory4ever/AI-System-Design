# 八个具名跨窗项：必要公开日有限恢复

准备者mar13_supplement，仅03-13补充Mar12 BJT自然日。不改已校准窄P/决定core，不将日期不明误作无贡献、未读Source误作访问受阻。当前只准备date隔离，不授正式候选/评分/Books/OUT/DAY。

## 实际身份与原字段

已实际逐份重新读SUP_ABS3_11090/11099/11110/11114/11126/11132/11142/11149精确v1完整题摘、作者、Comments、history；当前所见无withdraw/correction，后v2不当Mar12重要修订。复用DATE3/4的identifier/arxiv.content/findable及registered日上界，八项均Mar13 UTC01:47–01:48（11126在DATE4）。原范围仍Mar12–13 BJT，不单由Submitted/Updated或late注册授OUT。

新SUP_EIGHT_OAI_<ID>.raw全八GET200，见SUP_EIGHT_DATE_MANIFEST_RESULT.json，UTC2026-10-10T04:37:16–19。实际逐字段核id/title/作者、created/updated、header datestamp。这里使用metadataPrefix=arXiv（**不是versioned arXivRaw**）：11090当前created Apr8/modified Apr9，11132 Mar19/20、11149 Mar18/20为later版本；11099 createdMar11/modifiedSep10；11110/11114/11126/11142 createdMar11/modifiedMar13。这些当前记录字段不倒填v1公开日；v1提交/版本身份由已保存精确ABS/history和DATE dateInformation核，不伪称八OAI都给v1date或Mar13stamp。它们没有给可确认Mar12的announcement day。

## 已触发具名入口与真实停止

SUP_EIGHT_DATE_VENUE_MANIFEST/RESULT、SUP_EIGHT_DATE_FALLBACK_MANIFEST/RESULT与SUP_EIGHT_DATE_LAST_MANIFEST/RESULT保存每个URL/status/finalURL/UTC/bytes/error。只目标venue/author条目，没有机构或会议全站/全月列表。

- **11090 CausalTimePrior**：TSALM具名JbTgx2L9Z2由官方索引仅恢复身份。正常forum返回challenge（4787B），API1/API2与pdf HTTP403；不据索引‘6 months’授早日或实际稿件已读。作者thummd/CausalTimePrior repo API GET200、createdFeb19/default main，正确main README GET200实际同题/两作者/Jb note，arXiv链接只是注释TODO；repo创建/当前引用不签本稿公开day，README没有可采用的原稿日级release记录。不递归commithistory/代码。
- **11099 Graph Tokenization**：官方ICLR单篇2c0781...Abstract-Conference GET200/9517B，同题四作者和完整AB，仅ICLR2026无原公开day。jCctxI1BGF forum challenge、API1/API2/pdf403。精确官方repo API default release（不是猜main），createdFeb26；正确release README GET200/16062B同题/OR/arxiv，对当前结构与paper-scope说明，只年2026没有dated原稿发布；不把created当同稿公开，不读实验/全branch史。
- **11126 VAS-CFA**：实际官方ICASSP PaperNum6168 GET200/10218B同题三作者、May7 17:50–18:10是presentation，不作论文firstday；精确Crossref DOI11460611同三作者，published-print May3、createdApr21只是deposit。IEEE exact document正常202/0B不授正文或公开日期。原决定core的testprompt gold选择与26/31组合口径有效保留，不在date检查扩全文。
- **11142 Attention Gathers/MLPs Compose**：AAAI DAI non-archival具名vijHjECwMj由官方索引发现；normalforum challenge，API1/API2/pdf403。索引‘10months’和Accepted不能授官方note同稿正文/公开日，原正文/作者可由精确arxiv确认，但必要venue首次公开门未解。只请求该note可见原公开day及同稿身份，不要求代码数据availableuponrequest。
- **11110 ResWM、11114 routing signatures、11132 WebWeaver、11149 jailbreak scaling**：本日精确v1 ABS/OAI没有dated原公开入口；具名title/id和作者有界补搜只回arxiv当前提交史或第三方（ResWM编目/11114生成综述等），未获得官方日公告。WebWeaver/11149安全标题仅作日期恢复，不生成攻击内容/可执行复现。题摘当前未给目标作者dated稿，不能凭空猜repo或把‘no code’当受阻。必要日公告历史恢复限制复用本日已实际失败/有限month导航，不重扫月/其它日期；search zero不是当窗zero。

实际有界搜索2026-10-10T04:37–41Z：四具名venue标题（TSALM/GraphTokenization/AttentionGathers/ValueAlignment）；四其余title（routing/ResWM/scaling/WebWeaver）；精确11132/11149 announced/date及ResWM/routing officialarxiv list、作者MOE-XRAY/ResWM github identity。搜索只发现上面的primary URLs，所有日期裁决用保留原响应；无有效日公告原件。宽第三方列表不变queue，不作证据。

## 八项逐一请求与重开范围

| ID / 原P身份 | 当前精确缺口 / 一次请求 | 现在不能采用 |
| --- | --- | --- |
| 11090 Interventional Time Series Priors for Causal Foundation Models | 本arxiv原公告day，或JbTgx2L9Z2同稿原note公开day/作者dated完整稿 | 不确认Mar12训练prior新事件 |
| 11099 Graph Tokenization for Bridging Graphs and Transformers | 本arxiv原公告day，或jCctxI1BGF同稿原note公开day/作者dated完整稿 | 不确认Mar12可逆serialization新事件 |
| 11110 ResWM: Residual-Action World Model for Visual RL | 精确ID官方v1公告day或同题四作者dated完整公开稿 | 不确认Mar12 residual world/policy事件 |
| 11114 Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers | 精确ID官方v1公告day或同题单作者dated完整公开稿 | 不确认Mar12 routing telemetry事件 |
| 11126 Enhancing Value Alignment of LLMs with Multi-agent system and Combinatorial Fusion | 精确ID官方v1公告day或同题三作者dated完整公开稿 | 不确认Mar12 fusion评价事件 |
| 11132 WebWeaver: Breaking Topology Confidentiality in LLM Multi-Agent Systems with Stealthy Context-Based Inference | 精确ID官方v1公告day或同题六作者dated完整公开稿 | 不确认Mar12威胁/防御评价事件 |
| 11142 Attention Gathers, MLPs Compose: A Causal Analysis of an Action-Outcome Circuit in VideoViT | 精确ID官方v1公告day，或vijHjECwMj官方同稿note/作者稿公开day | 不确认Mar12机制干预事件 |
| 11149 Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models | 精确ID官方v1公告day或同题三作者dated完整公开稿 | 不确认Mar12安全费用评价事件 |

必要有限入口现无法消解Mar12/13边界，八项精确日期终态隔离，保留窄P与所有已读core；**不是已证窗外/EX或Source完成**。不要求时分秒、全网无早稿证明、全版本差分或实现。哪个primary到达仅重开其date；证Mar12新事件才最小评分/Source/owner，早稿或窗外按具体归属/重要修订门。没有采用剩余claim或Books，不能以本包清除其他尚可执行普通项。非准备者root已实际逐份OAI/所有结果与两README、ICLR/ICASSP/Crossref必要原件核通过，裁决见主独核末节；本日日期20→28、ordinary−8，不评分/候选/Source/Books/OUT，不授DAY。
