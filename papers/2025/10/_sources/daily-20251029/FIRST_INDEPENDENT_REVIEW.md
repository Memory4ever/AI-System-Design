# 2025-10-29 FIRST 独立准入校准

复核者：Peirce / Codex，非作者Curie；继承当前模型，不换模型。窗口：`[2025-10-28T09:00:00+08:00,2025-10-29T09:00:00+08:00)`。

fresh实际读取AGENTS、研究合同、来源使用说明/每日组/arXiv范围、Report合同、统一Prompt、ROADMAP及最新相关checkpoint；只加载本日[日报](../../29/README.md)、[CURRENT_STOP](CURRENT_STOP.md)、[FIRST_CALIBRATION](FIRST_CALIBRATION.md)、[SCREENING](SCREENING.md)与本日原件，不继承他日筛选池。

**FIRST结论：safeguard唯一家族最小准入通过，2+2+2=6；具体安全边界继续必要core深入，不因6分降为只读摘要。代表性排除抽检如下通过。DAY未通过，本文件不授十四来源全覆盖、七项安全反侧或最终Books完成。**

## 1. 事件、身份与最小贡献

实际打开[Introducing gpt-oss-safeguard](https://openai.com/index/introducing-gpt-oss-safeguard/)技术core L36–76、[report入口](https://openai.com/index/gpt-oss-safeguard-technical-report/)L24–29；实际解析本日[RSS原XML](openai-rss.raw)1245项的窗内切片，共6条。两篇safeguard的原字段均`Wed, 29 Oct 2025 00:00:00 GMT`，即BJT08:00，支持本次文章/research-preview发布事件1家族。两个网页显示Oct29，report入口直接链接本轮所读PDF；不由RSS推权重首次上传、PDF历史字节不变或此前从未可访问，不另计第二家族。

最小链条：固定label分类器改变政策通常需要新的标注/重训；本次开放reasoning classifier把policy与待分类content作为推理输入，可在所述接口下迭代policy；这使规则迭代快但推理较贵的风险面可考虑reasoner，稳定低延迟风险仍可保留专用classifier。新增的是此具体可用设计与受限分类证据，不是“防御要分层”“policy应版本化”等成熟原则，也不是把20B/120B名称或发布标签当贡献。

Design Delta2：具体政策更新/分类机制选择；Reach2：规则生命周期与在线判别/下游处置的交接；Durability2：可复用但受模型、policy及评价协议限定的条件。总6，不用Books已有正文撤销准入，不加机构权威、内部16%compute或一般治理原则的分。

## 2. 必要原报告实际核验与采用边界

实际打开[原技术PDF](https://cdn.openai.com/pdf/08b7dee4-8bc6-4955-a219-7793fb69090c/Technical_report__Research_Preview_of_gpt_oss_safeguard.pdf)封面/Introduction、§2/2.1与Tables1–2、§3区分、§4.1评价定义/必要Tables4–5、§4.2–4.5及相关Tables6–9。只读受影响分类/安全边界；未遍历旧gpt-oss附件、全部引用或运行实现/复现。

采用边界：multi-policy exact match、外部F1和直接聊天not_unsafe不是同一测量；MMMLU也不是provided-policy分类的多语言证明。高质量大样本专用classifier可更好，reasoning增加成本；内部Safety Reasoner与公开模型分开。20B jailbreak可退化，Table7两种公开模型的injection hijacking均低于基座；CoT未直接优化且可偏离所给policy。Table8末列表头重复120b确实存在，不擅改身份或引用该列作尺寸结论。聊天安全/事实问答结果不授任意policy、攻击或生产安全保证。部署硬件/batch/长度/并发/SLO与完整评价抽样未披露，不能换算公开模型成本优势。

以上原件必要core已由本人实际核验，可以供作者正式Evidence采用时复用，不要求其重新下载/全附件重审。当前日报仍是拟采用/待独立校准；作者须实际同步受限采用与审阅结果，不能由本文件代填已落实。

## 3. 代表性排除与查询范围

实际打开[Doppel原core](https://openai.com/index/doppel/)L48–99：filter/并行确认/RFT label/复验/低置信人审回流是具体编排，但未给足可比对照、阈值或新增可靠性条件，80%/3x不能归因成一般机制增量。本core贡献排除通过；不授其自动takedown生产安全。RSS原时刻为Oct28 10:00GMT，BJT18:00落窗。其他三条组织/公司治理标题实际RSS切片已核，未逐篇正文重读。

实际打开[StreetReaderAI原Blog](https://research.google/blog/streetreaderai-towards-making-street-view-accessible-via-context-aware-multimodal-ai/)L132–192，并读本日原提取core：当前view/geography输入与Gemini Live session context提供虚拟街景交互；11人实验及真假/朝向困难仍是应用评价，未披露新的通用表示或状态执行机制。该core排除通过，不授现实行走安全；日名Oct29无时区未补造时刻。未读所链论文全文或视频，不称整个家族无增量。

独立读本日Atom完整题摘4个样本：2510.24013v1（单机tardiness启发式，收益归领域算法非模型/系统机制）；2510.24031v1（日志clustering/router/parser组合，摘要未揭示新的执行/可靠性条件）；2510.24152v1（驾驶问型prompt/router/裁图及任务成绩，未形成通用新机制）；2510.24476v2（hallucination分类归纳本身，不把taxonomy当已验证防护）。这些有限题摘分类排除通过；后者当前v2更新2026-09-27，不授原v1正文已读或初版日期，更不授全引用反侧已审。

实际解码三条原request.json，并解析原Atom：12分类、`submittedDate:[202510271800 TO 202510281800]`、start0/max50/ascending，返回29/9/32与total一致，均小于50。主题限制没有变成全分类队列；submitted范围和当前版本不证明first-public。月首50只作线索，2666库存不转逐项队列。此轮未独立逐项审核66命中或全部潜力，不能把4个样本写成66项排除通过。

## 4. Books与后续具体范围

实际定点读[Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md)Policy-as-Data正文及前后交接，并读[Ch71](../../../../../books/part-06-ai-infrastructure/71-multi-tenant.md)开头tenant identity/隔离平面与[Ch73](../../../../../books/part-06-ai-infrastructure/73-production-best-practice.md)开头生产proof obligations。Ch72确实直接以safeguard承载policy artifact+untrusted content→typed decision→deterministic enforcement、sensor非authority、policy版本/回退与静态classifier共存；不能只凭主题或作者“已有覆盖”标签。当前最小命题未见必须新增的窄差额。Ch66本日Books比较尚未由我fresh独核；此处是有界PRE支持，不代最终Books Gate。

请主任务转交Curie：FIRST已通过，可落实本家族受限Evidence与最终已有覆盖/OnlyReport理由后交DAY。没有要求重跑有效core或增加书稿diff。DAY仍需独立核本日十四来源实际有限停止、七项必要安全/设计反侧精确v1及最终owner理由；本轮只核到这些ID当前Atom版本身份，**没有打开其精确v1 core**，作者已读标签不算完成。上述日期隔离可保留具名恢复条件，不无限追查全部历史版本，也不自动当已审重复。

本次仅写本FIRST及本日FINAL停点；未修改作者材料、Books、共享索引/state，未stage/commit/push，不授其他日期覆盖。
