# 2603.09643 — MM-tau-p²必要Source与Ch66具体已有覆盖（非作者通过）

[exact-v1](https://arxiv.org/html/2603.09643v1)。第三包完整题摘准入由root独核，准入只限具体必要人工升级的相反judge标签与难度相关测量盲区，不按新benchmark/12指标数或persona主题加分。作者实际完整§2–4、Tables2–5、§5及Appendix A.3/Table6全部文字；没核Figure2/3曲线像素，不沿用currentv5指标或声称代码/复现。重新官方abs/current轻核仍v5、无withdrawn或已见纠错说明，题摘同v1；版本号不是重要修订证据，不扩全版本差异。原字段见SUP_EXACT_BATCH3.json，fresh helper回读一致。

## 身份、日期与采用命题

Mar10UTC13:18:02 v1提交处于官方deadline批次；official availability/no-advance finalID/DOI最早公开下界Mar11BJT08；owning arxiv.content/findable DOI registeredMar11UTC02:18:28已可发现上界，同BJT03-11夹证，不用Submitted/Updated/注册单独public。current comment没有accepted先稿线索，projectpage仅个人页非已知先稿冲突，不无限追参考文献；root待独核日期字段。

2+1+2=5，标准审阅：自动对話判分把必要人工升级和任务未最终完成混成单一success→相似SIM-lock升级获得相反标签、改rubric仍分歧且困难任务更常升级→域/模态比较必须检查success构念、评分仪器与难度切片，不把pass差全部归Agent能力。局部judge/测量对象的边界是评分对象，成熟ASR/TTS、JSON和persona流程不计新机制。既有具体正文已承载采用命题，拟已有覆盖，不为凑diff再写段。

## 方法、关键评价与直接反侧

§2.1–2.6 Telecom/Retail模拟任务、None/Easy/Hard用户，text/voice经ASR→agent→TTS，保存中间transcript/tool/output；persona/context每3用户消息由最近16条同模型推断再注入。scorer用rubric turn/conversation标签，turn仅当时prefix避免hindsight；但scorer schema/结构化JSON不是标签正确性证明。范围/真实工具效果、合法升级和最终用户目标不能从persona或judge叙述取得。

§4.1–4.1.1与A.3/Table6具体例子：SIM PIN/PUK需要权限外人工解锁，同类轨迹或平行评估分别标“已尽scope正确升级”为成功与“bot未解锁”为失败；自然语言rubric最初必要升级含糊，改成SIM-lock域特例后作者称2例消歧、3例仍split。表保留正反判断，不是仅某一个低分指标。作者推论困难任务更常需要升级，所以误标签会随难度相关；本轮支持需要分层审计的风险，未披露逐项全人口label-noise估计/独立人工gold，不把它认作已测部署噪声率或领域难度因果。

§4.1.2 GPT5较乐观把多数升级算成功，但也纳入不应升级的假阳性，说明更高pass并非更准确；正文声称voice Telecom最大17pp差，本轮未核Fig2像素/完整原始轨迹，不采用精确17pp为已独算值。A.3示例可支持相反标签，不证明所有Agent失败都是测量误差；正确交接与最终真实问题完成仍分开。§4.2明确voice/text不同ASR/TTS路径、模拟器反应和noise可能改变后续conversation，不能当同题只改模态的严格因果实验。

Tables2–4同一评价协议的分账也不支持§5所有域/两judge的persona安全单调下降：Retail GPT4.1 SafetyRecall .43→.49→.49、SafetyPrecision .47→.54→.521，GPT5 SR .36→.43→.408，方向并非全面下降。Table3–4相对Δ解释与部分文字方向需保留冲突，不采用全域退步规律或context universally better。§2.7的MRS<.7、RTC≤2等是作者拟阈值，无独立production校准。SafetyPrecision在结果中出现而方法Safety项只定义IAS/SR，不能补造统一12指标可执行规格；零分母、统计独立性/episode人口/seed/CI、模型精确revision、ASR模型配置/音频人口/完整费用、硬件/precision/SLO Not Disclosed。域、人设、Agent与judge不完全分离，双judge一致也不能排除共同偏差。Eq1 composite自定义权重没有总体安全发布权，不直接采用。

## actual owner与具体已有覆盖提案

唯一owner `PLATFORM-EVALUATION-SYSTEM`，[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)。actual opening/65与67开篇交接及以下完整局部已读：

- 329–362：346明确temperature0也非endpoint确定性、保留原始输出/方向与难度切片及人工校准；348固定答案仅变judgeprompt时先属仪器稳定性问题，稳定/aggregate相关不等配对正确；350task competence与leniency分开、同源共误不获truth。
- 699–725：712/714求助是否发生、外部resolver能否完成、不必要升级分账；升级本身不证真实outcome，不能把router收益当模型认识能力。
- 1081–1117：1101/1103case目标/resolution consistency与真实tool effect权限分离，judge替换可改变短case显著性、case相关分母与Unknown/人工回退明确。
- 2819–2847：rubric formation、criterion execution、aggregation/decision分层，legitimate alternative判错与owner/version/holdout；2838/2840条件适用/共同上游障碍不重复扣分，但未完成目标不可改为成功，unknown/人工裁决不让自报受阻自动免责。

这些不是主题相似：必要合法升级须核criterion适用而最终目标仍另验，正是SIM-lock反例的测量对象冲突；同案相反评分/难度相关噪声已由346/348的测量身份与切片处理，费用和校准失配回退由上述局部完整承载。采用有限反例强化原判断，不采用本benchmark自定阈值/aggregate/persona普遍收益或逐项新指标，故拟No Change/已有覆盖。根节点不改，不扩Ch81/语音架构，无写锁请求。必要Source/日期及具体NC尚待非作者实际核，未授DAY。

实际独核：root实际v1§2/3 Tables2–4、完整§4/5及A.3 Table6相反verdict，原日期owning/findable registered与official no-advance下界同BJT日，以及actual Ch66 329–362/699–725/2819–2847具体instrument、难度切片、真实resolver与criterion/outcome分离，通过必要Source/date/5分标准与具体NC。未核Fig2精确17pp/曲线，不授v5重要修订或全部指标真值；无Books新写，不授DAY。
