# 第六三项venue日期门：独立必要性复核

复核者：`mar13_admission_review`；准备者：`mar14_supplement`。本次仅03-14独立上下文，补充窗口为2026-03-13北京时间自然日。只裁11650/11947/12138三个venue信号的必要性，不改README、Books、主ledger或LEARNING_STATE，不授DAY。

## 实际范围

本次重读AGENTS、当前Research/Report合同、统一Prompt、Sources说明/Daily组/arXiv主题及会议恢复边界，ROADMAP相关路由、最新checkpoint路由、03-14 README开头/§5停点。第六八项完整题摘/决定core与root实际Mar13 arXiv日级夹证有效复用，不重算日期。

直接读取`SUP_VENUE_SIXTH.md`及三个本日`SUP_ABS_<ID>.txt`的完整题名、署名、abstract、Comments和显示v1 history；原件身份分别为2603.11650v1、2603.11947v1、2603.12138v1，保留页未见撤回/纠错标记。实际读取11650 Crossref原JSON的title/六署名/publisher/DOI/WWW容器/event/publication_history日期/created/indexed/resource/relation字段，12138 CVF完整页面转录、原HTML的citation日期和同ID arXiv链接，以及`SUP_SIXTH_VENUE_MANIFEST_RESULT.json`。不重新搜索、不抓正文/全会议/全作者/全版本，不认证后续正式稿与arXiv v1逐字相同。

## 逐项裁定

| 身份 | 实际原字段及同稿关系 | 必要性裁定 |
| --- | --- | --- |
| **11650 QChunker** | Crossref DOI `10.1145/3774904.3792433`，title与arXiv一致；Jihao Zhao、Daixuan Li、Pengfei Li、Shuaishuai Zu、Biao Qin、Hongyan Liu六署名逐项同序，publisher ACM，WWW2026容器/event。`published-online`/`issued`及publisher `Published` assertion均2026-04-12，print04-13；created04-27/indexed07-31是元数据操作字段，relation为空。 | **现有限原证足够继续Mar13处理，不再保留必须恢复ACM早稿日期的门。** 这些字段支持同一材料家族的更晚正式发表，不把Apr12移作首次公开，也不证明绝无早稿。ACM exact DOI页403仍如实保留，但本次没有具名更早全文记录需要它消解；不能因403制造本项日期受阻。 |
| **11947 Resurfacing Paralinguistic Awareness** | arXiv题名与六署名对应具名论文，唯一当前可见venue说明为`Submitted to Interspeech 2026`。没有在实际保留材料中指向本稿更早公开正文的日期、official release或original note。 | **现有限原证足够继续Mar13处理。** 投稿是向venue提交，不是向公众公开；纯投稿说明不构成必须搜遍ISCA/作者记录、证明从未早公开的缺口。未找到ISCA exact页不等于必要正文或已知日期缺失，不列永久受阻。 |
| **12138 HATS** | arXiv Comments `Accepted by CVPR 2026`；CVF exact页面title、Rui Shao至Gongwei Chen八署名、abstract核心机制相符，HTML直接链接 `https://arxiv.org/abs/2603.12138`。BibTeX June2026，citation_publication_date仅2026；没有本稿page首次上线日。CVF通用“except watermark identical to accepted versions”不证明与arXiv v1逐字相同。 | **现有限原证足够继续Mar13处理，不再保留必须恢复OpenReview首公开note的门。** 接受信号和June会议月份不证明早公开，也不当首次正文日期。准备包所述第三方OpenReview标签/另一综述引用不是本稿original note；没有可用具名本稿更早公开记录，故不由该标签扩出必须恢复的对象。 |

11650 Crossref实际GET200，20686bytes，2026-10-10T01:08:37.334822Z，final URL为同DOI API；ACM直接GET为403。12138 CVF实际GET200，6819bytes，2026-10-10T01:08:37.335664Z，final URL为该HATS exact页面。这里只确认这些已保存原证与字段权限，不把元数据接口成功说成ACM页面成功，不把CVF会议月份补成精确页面公开日。

## 日期采用边界与停止

**三个venue门均可结束当前必要恢复，沿用已通过的2026-03-13 arXiv公开日期继续对应最低证据审阅。** 当前判断是有限发现/具名核对范围内，没有实际早公开反证需要阻断归属；不是只核arXiv事件后故意忽略已知早稿，也不是全球无早稿证明。后续发表不会迁移本日日期，未找到早稿也不被包装为互联网上绝无更早版本。

研究合同要求处理已知实际首公开记录与必要版本信息，来源合同要求有界精确恢复，二者都不要求对每个投稿/接受说明遍历全网以证明一个否定命题。这里没有剩余具体必要日期材料可请求；本项不再将ACM不可读、ISCA无精确入口、CVF无上线日/OpenReview无本稿note泛化为三项外部日期保留。若后续出现具名同稿且可核验的更早正文/公开note，只定点重开该ID首公开归属或同家族事件去重；重要修订按实际变化处理，不重跑全会。

本裁定仅结束三个日期门，不预授评分、Source/Books或日报完成，也不重复第六八项已通过的题摘/core审阅。
